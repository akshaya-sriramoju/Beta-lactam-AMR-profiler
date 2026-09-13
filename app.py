import streamlit as st

from fasta_parser import parse_fasta
from amr_detector import detect_amr_genes
from amr_metadata import get_metadata
from genomic_profile import create_profile


st.set_page_config(
    page_title="🧬 Beta-Lactam AMR Profiler",
    page_icon="🧬",
    layout="wide"
)


st.title("🧬 Beta-Lactam AMR Profiler")

st.write(
    "Reference-based genomic screening of "
    "beta-lactamase resistance determinants."
)

st.write(
    "A bioinformatics prototype for screening bacterial DNA "
    "sequences for known antimicrobial resistance-associated "
    "genetic determinants and generating an interpretable "
    "genomic resistance profile."
)

st.info(
    "Detection of an "
    "AMR-associated genetic determinant does not establish "
    "phenotypic or clinical resistance."
)


with st.expander("🔬 How does this work?"):

    st.markdown(
        """
        ### Analysis workflow

        **1. FASTA upload**  
        The user provides a bacterial DNA sequence in FASTA format.

        **2. Sequence analysis**  
        The application calculates sequence length and GC content
        and checks whether the sequence contains valid DNA bases.

        **3. AMR screening**  
        The query sequence is compared with reference AMR-associated
        sequences using local pairwise sequence alignment.

        **4. Annotation**  
        Detected determinants are mapped to their resistance mechanism
        and associated antibiotic class.

        **5. Genomic resistance profile**  
        The results are presented as an interpretable profile containing
        sequence identity, query coverage, resistance mechanism,
        and antibiotic class.

        ### Important limitation

        This prototype detects genetic similarity to reference
        sequences. Detection of an AMR-associated genetic determinant
        does **not** by itself establish phenotypic or clinical
        antibiotic resistance.
        """
    )


uploaded_file = st.file_uploader(
    "Choose a FASTA file",
    type=["fasta", "fa", "fna"]
)


if uploaded_file is not None:

    try:

        # =========================
        # Sequence Analysis
        # =========================

        results = parse_fasta(uploaded_file)

        st.success(
            "FASTA file uploaded successfully!"
        )

        st.subheader("Sequence Analysis")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Sequence ID",
                results["id"]
            )

        with col2:
            st.metric(
                "Length",
                f"{results['length']} bp"
            )

        with col3:
            st.metric(
                "GC Content",
                f"{results['gc_content']:.2f}%"
            )

        if results["is_valid"]:
            st.success("✓ Valid DNA sequence")
        else:
            st.error("✗ Invalid DNA sequence")


        # =========================
        # AMR Detection
        # =========================

        st.subheader("AMR Detection")

        st.caption(
            "Prototype screening thresholds: ≥80% sequence identity "
            "and ≥50% query coverage. These thresholds are not "
            "clinically validated diagnostic criteria."
        )

        detection_results = detect_amr_genes(
            results["sequence"],
            "beta_lactamase_database.fasta"
        )

        profile = create_profile(
            results,
            detection_results,
            get_metadata
        )


        # =========================
        # AMR Genomic Profile
        # =========================

        if profile["amr_determinants"]:

            st.success(
                f"{len(profile['amr_determinants'])} "
                "AMR-associated determinant(s) detected"
            )

            st.subheader("🧬 AMR Genomic Profile")

            for determinant in profile["amr_determinants"]:

                st.markdown(
                    f"### {determinant['gene']}"
                )

                st.write(
                    f"**Beta-lactamase family:** "
                    f"{determinant['family']}"
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.metric(
                        "Sequence Identity",
                        f"{determinant['identity']:.2f}%"
                    )

                    st.metric(
                        "Query Coverage",
                        f"{determinant['coverage']:.2f}%"
                    )

                with col2:

                    st.write(
                        "**Resistance Mechanism**"
                    )

                    st.info(
                        determinant["mechanism"]
                    )

                    st.write(
                        "**Antibiotic Class**"
                    )

                    st.info(
                        determinant["antibiotic_class"]
                    )

                st.write(
                    determinant["description"]
                )

                st.divider()


            # =========================
            # Detection Summary
            # =========================

            st.subheader("Detection Summary")

            table_data = []

            for determinant in profile["amr_determinants"]:

                table_data.append({
                    "Gene": determinant["gene"],
                    "Family": determinant["family"],
                    "Mechanism": determinant["mechanism"],
                    "Antibiotic Class": determinant["antibiotic_class"],
                    "Identity (%)": round(
                        determinant["identity"], 2
                    ),
                    "Coverage (%)": round(
                        determinant["coverage"], 2
                    )
                })

            st.dataframe(
                table_data,
                use_container_width=True,
                hide_index=True
            )


            # =========================
            # Download Report
            # =========================

            report_lines = [
                "AMR GENOMIC PROFILE",
                "===================",
                f"Sequence ID: {profile['sequence_id']}",
                f"Sequence Length: "
                f"{profile['sequence_length']} bp",
                f"GC Content: "
                f"{profile['gc_content']:.2f}%",
                "",
                "Detected AMR Determinants",
                "--------------------------"
            ]

            for determinant in profile["amr_determinants"]:

                report_lines.extend([
                    f"Gene: {determinant['gene']}",
                    f"Family: {determinant['family']}",
                    f"Identity: "
                    f"{determinant['identity']:.2f}%",
                    f"Coverage: "
                    f"{determinant['coverage']:.2f}%",
                    f"Mechanism: "
                    f"{determinant['mechanism']}",
                    f"Antibiotic class: "
                    f"{determinant['antibiotic_class']}",
                    ""
                ])

            report_lines.append(
                "Note: Detection of an AMR-associated "
                "genetic determinant does not establish "
                "phenotypic or clinical resistance."
            )

            report = "\n".join(report_lines)

            st.download_button(
                label="📥 Download AMR Report",
                data=report,
                file_name="amr_genomic_profile.txt",
                mime="text/plain"
            )


        else:

            st.warning(
                "No AMR reference matches were found "
                "using the current prototype matching thresholds."
            )


    except Exception as e:

        st.error(
            f"Could not process the FASTA file: {e}"
        )