import unittest

from fasta_parser import parse_fasta
from amr_detector import detect_amr_genes
from amr_metadata import get_metadata
from genomic_profile import create_profile


DATABASE = "beta_lactamase_database.fasta"


class TestAMRDetector(unittest.TestCase):

    def test_blatem_detection(self):

        with open(
            "test_sequences/blaTEM.fasta",
            "rb"
        ) as fasta_file:

            parsed = parse_fasta(
                fasta_file
            )

        results = detect_amr_genes(
            parsed["sequence"],
            DATABASE
        )

        self.assertGreater(
            len(results),
            0
        )

        self.assertEqual(
            results[0]["gene"],
            "blaTEM"
        )

        self.assertGreaterEqual(
            results[0]["identity"],
            80
        )


    def test_multiple_reference_genes(self):

        genes = [
            "blaTEM",
            "blaSHV",
            "blaCTX-M",
            "blaKPC",
            "blaNDM",
            "blaVIM",
            "blaIMP",
            "blaOXA-48"
        ]

        for gene in genes:

            with self.subTest(
                gene=gene
            ):

                with open(
                    f"test_sequences/{gene}.fasta",
                    "rb"
                ) as fasta_file:

                    parsed = parse_fasta(
                        fasta_file
                    )

                results = detect_amr_genes(
                    parsed["sequence"],
                    DATABASE
                )

                self.assertGreater(
                    len(results),
                    0
                )

                self.assertEqual(
                    results[0]["gene"],
                    gene
                )


    def test_metadata(self):

        metadata = get_metadata(
            "blaTEM"
        )

        self.assertEqual(
            metadata["family"],
            "TEM"
        )

        self.assertEqual(
            metadata["mechanism"],
            "Beta-lactamase production"
        )

        self.assertEqual(
            metadata["antibiotic_class"],
            "Beta-lactams"
        )


    def test_genomic_profile(self):

        sequence_results = {
            "id": "test",
            "length": 1000,
            "gc_content": 50.0
        }

        detection_results = [
            {
                "gene": "blaKPC",
                "identity": 99.0,
                "coverage": 100.0,
                "aligned_length": 1000
            }
        ]

        profile = create_profile(
            sequence_results,
            detection_results,
            get_metadata
        )

        self.assertEqual(
            len(profile["amr_determinants"]),
            1
        )

        determinant = (
            profile["amr_determinants"][0]
        )

        self.assertEqual(
            determinant["gene"],
            "blaKPC"
        )

        self.assertEqual(
            determinant["family"],
            "KPC"
        )


if __name__ == "__main__":
    unittest.main()