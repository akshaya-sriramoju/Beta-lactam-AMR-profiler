from Bio import SeqIO
from Bio.Align import PairwiseAligner


def load_amr_database(database_file):

    references = []

    with open(
        database_file,
        "r",
        encoding="utf-8"
    ) as handle:

        for record in SeqIO.parse(
            handle,
            "fasta"
        ):

            references.append(
                {
                    "gene": record.id.split("|")[0],
                    "sequence": str(record.seq).upper()
                }
            )

    return references


def calculate_identity(
    query,
    reference,
    alignment
):

    aligned_query = ""
    aligned_reference = ""

    for (
        (q_start, q_end),
        (r_start, r_end)
    ) in zip(
        alignment.aligned[0],
        alignment.aligned[1]
    ):

        aligned_query += query[
            q_start:q_end
        ]

        aligned_reference += reference[
            r_start:r_end
        ]

    if len(aligned_query) == 0:
        return 0.0

    matches = sum(
        a == b
        for a, b in zip(
            aligned_query,
            aligned_reference
        )
    )

    return (
        matches /
        len(aligned_query)
    ) * 100


def detect_amr_genes(
    query_sequence,
    database_file
):

    references = load_amr_database(
        database_file
    )

    aligner = PairwiseAligner()

    aligner.mode = "local"

    aligner.match_score = 2
    aligner.mismatch_score = -1
    aligner.open_gap_score = -2
    aligner.extend_gap_score = -0.5

    results = []

    query = query_sequence.upper()

    for reference in references:

        ref_sequence = reference[
            "sequence"
        ]

        score = aligner.score(
            query,
            ref_sequence
        )

        # Stronger preliminary filter
        if score < 150:
            continue

        alignments = aligner.align(
            query,
            ref_sequence
        )

        best_alignment = next(
            iter(alignments)
        )

        identity = calculate_identity(
            query,
            ref_sequence,
            best_alignment
        )

        aligned_length = sum(
            end - start
            for start, end
            in best_alignment.aligned[0]
        )

        query_coverage = (
            aligned_length /
            len(query)
        ) * 100

        # Strict prototype screening thresholds
        if identity < 90:
            continue

        if query_coverage < 70:
            continue

        results.append(
            {
                "gene": reference["gene"],
                "identity": identity,
                "coverage": query_coverage,
                "aligned_length": aligned_length
            }
        )

    results.sort(
        key=lambda x: (
            x["identity"],
            x["coverage"]
        ),
        reverse=True
    )

    return results