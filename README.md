# Bioinformatics Foundations: Algorithmic Sequence Analysis in Python

A repository of foundational computational biology pipelines, sequence manipulation algorithms, and bio-data processing scripts implemented in standard Python without external biocomputing dependencies.

Designed as an algorithmic foundation for genomic data analysis, high-throughput sequence parsing, and computational biology research.

---

## Repository Structure & Core Modules

The repository tracks progressive development from raw nucleotide manipulation to a multi-functional sequence analysis pipeline:

| Module / Script | Focus Area | Description |
| :--- | :--- | :--- |
| `phase1_capstone.py` | **End-to-End Pipeline** | Integrated workflow for FASTA parsing, GC content calculations, motif search, transcription, and reverse complement generation. |
| `sample.fasta` | **Benchmark Dataset** | Standardized FASTA format input file used for testing validation and parsing modules. |
| `phase1_day1.py` – `phase1_day3.py` | **Sequence Fundamentals** | Nucleotide validation, purine/pyrimidine ratio calculations, and string transformation routines. |
| `phase1_day4.py` – `phase1_day6.py` | **Genomic Metrics** | GC-content profiling, local window scanning, and open reading frame (ORF) boundaries. |
| `phase01_day07.py` – `phase1_day9.py` | **Bio-Parsing & Motifs** | Custom flat-file FASTA ingestion, dictionary mapping of codons, and pattern-matching logic. |
| `phase1_summary.py` / `phase1_practice.py` | **Review & Drills** | Modular unit exercises testing edge cases in biological string operations. |
| `day5.py` – `day10.py` series | **Algorithmic Drills** | Iterative algorithm implementations covering nested iterations, coordinate mappings, and error-handling. |

---

## Key Capabilities Implemented

* **Strict Sequence Validation:** Checks raw sequence strings against valid IUPAC standard single-letter nucleotide and IUPAC ambiguity alphabets.
* **Compositional Metrics:** Computes overall GC percentage, AT/GC skew ratios, and local composition variations.
* **Central Dogma Logic:** Implements DNA-to-RNA transcription, RNA-to-cDNA reverse transcription, and reverse complement generation using directional base pairing ($5' \rightarrow 3'$).
* **Flat-File Parsing:** Implements native line-by-line streaming of multiline FASTA records to prevent high-memory overhead on large sequence entries.
* **Mutation & Motif Scanners:** Identifies point mutations (transitions vs. transversions), calculates sequence hamming distance, and locates biological target motifs.

---

## Getting Started

### Prerequisites
* Linux / WSL environment
* Python 3.8+

### Running the Capstone Pipeline
Execute the primary integrated pipeline against the test dataset:

```bash
python3 phase1_capstone.py