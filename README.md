\# AMR Gene Detector \& Genomic Resistance Profiler



A Python-based bioinformatics web application for screening bacterial DNA sequences for known antimicrobial resistance (AMR)-associated genetic determinants.



The application accepts FASTA sequences, performs sequence analysis and reference-based local alignment, identifies potential AMR-associated determinants, maps them to resistance mechanisms and antibiotic classes, and generates an interpretable genomic resistance profile.



\## Project Overview



Antimicrobial resistance is a major global health challenge. Genomic analysis can help identify genetic determinants associated with antimicrobial resistance.



This project demonstrates a simplified bioinformatics workflow for screening DNA sequences against a small reference database of AMR-associated genes.



The project is designed as a research and educational prototype and is not intended for clinical diagnosis or antibiotic treatment decisions.



\## Features



\- FASTA file upload

\- DNA sequence validation

\- Sequence length calculation

\- GC content calculation

\- Reference-based AMR sequence screening

\- Local pairwise sequence alignment using Biopython

\- Sequence identity and query coverage calculation

\- AMR determinant filtering using prototype thresholds

\- Resistance mechanism annotation

\- Antibiotic class annotation

\- AMR Genomic Profile

\- Downloadable text report

\- Positive and negative test sequences

\- Automated unit tests



\## Workflow



```text

FASTA Upload

&#x20;    |

&#x20;    v

Sequence Validation

&#x20;    |

&#x20;    v

Sequence Analysis

(length + GC content)

&#x20;    |

&#x20;    v

Reference AMR Database

&#x20;    |

&#x20;    v

Local Pairwise Alignment

&#x20;    |

&#x20;    v

Identity + Coverage

&#x20;    |

&#x20;    v

AMR Determinant Filtering

&#x20;    |

&#x20;    v

Resistance Mechanism

&#x20;    +

Antibiotic Class

&#x20;    |

&#x20;    v

AMR Genomic Profile

&#x20;    |

&#x20;    v

Downloadable Report

