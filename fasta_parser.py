from Bio import SeqIO
from io import StringIO


def parse_fasta(uploaded_file):
    # Handle both Streamlit uploads and normal Python files
    if hasattr(uploaded_file, "getvalue"):
        fasta_data = uploaded_file.getvalue()
    else:
        fasta_data = uploaded_file.read()

    # Convert bytes to text
    if isinstance(fasta_data, bytes):
        fasta_data = fasta_data.decode("utf-8")

    # Read FASTA
    record = SeqIO.read(
        StringIO(fasta_data),
        "fasta"
    )

    sequence = str(record.seq).upper()

    # Check DNA sequence
    valid_bases = set("ATGC")
    is_valid = all(
        base in valid_bases
        for base in sequence
    )

    # Sequence length
    sequence_length = len(sequence)

    # GC content
    if sequence_length > 0:
        gc_count = (
            sequence.count("G")
            + sequence.count("C")
        )

        gc_content = (
            gc_count / sequence_length
        ) * 100
    else:
        gc_content = 0

    return {
        "id": record.id,
        "sequence": sequence,
        "length": sequence_length,
        "gc_content": gc_content,
        "is_valid": is_valid
    }