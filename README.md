# Beta-Lactam AMR Profiler

A Python-based tool for identifying and profiling beta-lactam antimicrobial resistance determinants from nucleotide FASTA sequences.

The Beta-Lactam AMR Profiler analyzes nucleotide FASTA sequences against a curated reference panel of 8 beta-lactamase gene determinants.

The tool performs sequence processing and reference-based local alignment, evaluates sequence identity and query coverage, and links detected determinants to relevant biological metadata such as beta-lactamase family, resistance mechanism, and antibiotic class.

The results are presented through an interactive Streamlit interface.

WORKFLOW:

1. The user provides a nucleotide sequence in FASTA format.
2. The FASTA parser reads and validates the input sequence.
3. Basic sequence statistics including sequence length and GC content are calculated.
4. The input sequence is compared against the beta-lactamase reference database using local sequence alignment.
5. Potential matches are evaluated using sequence identity and query coverage thresholds.
6. Detected resistance determinants are linked to their corresponding metadata.
7. The results are displayed as an interpretable genomic resistance profile through the Streamlit interface.

The current prototype uses the following screening thresholds:

- Sequence identity ≥ 90%
- Query coverage ≥ 70%

These thresholds are intended for this particular prototype and are not clinically validated diagnostic criteria.


Reference Database

The current beta-lactamase reference database contains 8 gene determinants:

- blaCTX-M — CTX-M family
- blaIMP — IMP family
- blaKPC — KPC family
- blaNDM — NDM family
- blaOXA-48 — OXA-48 family
- blaSHV — SHV family
- blaTEM — TEM family
- blaVIM — VIM family

These reference sequences are used by the profiler for sequence comparison and beta-lactamase determinant identification.


## Technologies

- Python
- Biopython
- Streamlit
- FASTA
- Pairwise sequence alignment
- Git/GitHub


Limitations include:

a.) The reference database contains only 8 selected beta-lactamase determinants.
b.) The alignment approach is intended for prototype screening and is not a replacement for validated AMR detection pipelines.
c.) Detection of an AMR-associated genetic determinant does not establish phenotypic or clinical antibiotic resistance.
d.) The current identity and coverage thresholds have not been clinically validated.
e.) The tool does not provide antibiotic treatment recommendations.




