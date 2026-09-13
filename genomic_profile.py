def create_profile(
    sequence_results,
    detection_results,
    get_metadata
):
    """
    Create an interpretable AMR genomic profile.

    Prototype screening thresholds:
    - Sequence identity >= 80%
    - Query coverage >= 50%

    These thresholds are for this educational prototype
    and are not clinically validated diagnostic criteria.
    """

    profile = {
        "sequence_id": sequence_results["id"],
        "sequence_length": sequence_results["length"],
        "gc_content": sequence_results["gc_content"],
        "amr_determinants": []
    }

    for result in detection_results:

        if (
            result["identity"] >= 80
            and result["coverage"] >= 50
        ):

            gene = result["gene"]

            metadata = get_metadata(gene)

            determinant = {
                "gene": gene,
                "family": metadata["family"],
                "identity": result["identity"],
                "coverage": result["coverage"],
                "aligned_length": result["aligned_length"],
                "mechanism": metadata["mechanism"],
                "antibiotic_class": metadata["antibiotic_class"],
                "description": metadata["description"]
            }

            profile["amr_determinants"].append(
                determinant
            )

    return profile