# Interactive Genomic Analysis And Biological Simulation System

> **An Educational Bioinformatics & Dynamic Programming Visualization Platform**  
> *Translating abstract sequence alignment matrices and Central Dogma mechanics into intuitive CLI dashboards and real-time interactive 2D simulations.*

![Python Version](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Pygame Version](https://img.shields.io/badge/Pygame-2.6.1-green.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Dynamic%20Programming-orange.svg)
![License](https://img.shields.io/badge/License-MIT-lightgrey.svg)

The **Interactive Genomic Analysis And Biological Simulation System** is a hybrid bioinformatics platform written in Python that bridges theoretical algorithm design (Needleman–Wunsch, Smith–Waterman, Levenshtein edit distance) with step-by-step biological simulation (transcription, codon-to-amino-acid translation, hydrogen-bond dynamics, and dynamic programming matrix backtracking).

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Problem Statement](#2-problem-statement)
3. [Objectives](#3-objectives)
4. [Core Features](#4-core-features)
   - [CLI Genomic Analysis Dashboard](#cli-genomic-analysis-dashboard)
   - [Interactive Biological Simulation (GUI)](#interactive-biological-simulation-gui)
5. [Algorithms Used](#5-algorithms-used)
   - [Needleman–Wunsch (Global Alignment)](#needleman-wunsch-global-alignment)
   - [Smith–Waterman (Local Alignment)](#smith-waterman-local-alignment)
   - [Backtracking & Traceback](#backtracking--traceback)
   - [DNA Transcription & Translation](#dna-transcription--translation)
   - [Mutation Classification](#mutation-classification)
6. [Data Structures Used](#6-data-structures-used)
7. [Complexity Analysis](#7-complexity-analysis)
8. [System Workflow](#8-system-workflow)
9. [Architecture](#9-architecture)
10. [Project Structure](#10-project-structure)
11. [Technology Stack](#11-technology-stack)
12. [Installation](#12-installation)
13. [Running the Project](#13-running-the-project)
14. [GUI Controls](#14-gui-controls)
15. [Example Output](#15-example-output)
16. [Understanding the Output](#16-understanding-the-output)
17. [DP Matrix Visualization](#17-dp-matrix-visualization)
18. [Central Dogma Visualization](#18-central-dogma-visualization)
19. [Mutation Analysis](#19-mutation-analysis)
20. [Graceful Degradation](#20-graceful-degradation)
21. [Design / Visualization Philosophy](#21-design--visualization-philosophy)
22. [Performance / Constraints](#22-performance--constraints)
23. [Limitations](#23-limitations)
24. [Future Scope](#24-future-scope)
25. [Educational / Academic Relevance](#25-educational--academic-relevance)
26. [Expected Outcomes](#26-expected-outcomes)
27. [Team](#27-team)
28. [Academic Information](#28-academic-information)
29. [References](#29-references)

---

## 1. Project Overview

Raw nucleotide sequences and 2D Dynamic Programming (DP) score grids are often opaque when presented solely as numerical tables or text strings. Students and researchers frequently struggle to visualize how cell dependencies ($S_{i,j}$) construct optimal global or local alignment routes, or how nucleotide variations translate into altered protein chains.

This system combines **genomic sequence analysis**, **algorithm visualization**, and **biological simulation** into a single software package. It features:
- A **CLI Analytical Dashboard** providing nucleotide metrics, transcription/translation mappings, global/local sequence alignments, and plain-English mutation logs.
- An **Interactive Pygame 2D Visualizer** featuring animated double-strands, liquid DP tracer backtracks, dynamic hydrogen-bond physics, amino acid codon grouping, mouse pan/zoom, and real-time keyboard triggers.

Designed primarily for educational purposes, the system makes complex string-matching algorithms and Central Dogma mechanics tangible and visually understandable.

---

## 2. Problem Statement

This project addresses four key educational and technical challenges:

1. **Visualization Difficulties**: Traditional dynamic programming matrices are displayed as static numerical arrays, making it hard to follow step-by-step path selection.
2. **Algorithmic Complexity**: Students often find it difficult to grasp the difference between global end-to-end sequence alignment (Needleman–Wunsch) and local sub-region pattern matching (Smith–Waterman).
3. **Difficulty Understanding the Central Dogma**: Translating DNA template strands into mRNA (`T` $\rightarrow$ `U`) and grouping codons into amino acids is frequently taught abstractly rather than dynamically.
4. **Limitations of Static/Text-Only Interfaces**: Standard command-line output lacks interactive exploration (zooming, panning, particle cues, hover tooltips) necessary for deep engagement.

---

## 3. Objectives

The primary objectives implemented in the core engine [dna.py](file:///Users/jhum/Documents/Padhai%20stuff/college/mca/coding/python/daaaaaa/dna.py) are:

- **Analyze DNA Sequences**: Validate raw strings and reject invalid non-nucleotide characters.
- **Calculate Genomic Metrics**: Compute GC-content percentages and map GC-dense regions.
- **Perform Global Alignment**: Implement the Needleman–Wunsch algorithm to find optimal overall sequence similarity.
- **Perform Local Alignment**: Implement the Smith–Waterman algorithm to discover highly conserved regional sub-segments.
- **Detect & Classify Mutations**: Categorize differences into Matches, Insertions/Deletions (Gaps), Transitions, and Transversions.
- **Visualize Transcription & Translation**: Render step-by-step molecular synthesis from DNA to mRNA to amino acid protein chains.
- **Visualize DP Traceback**: Highlight optimal routes through dynamic programming matrices in both terminal tables and interactive 2D graphics.
- **Enhance Pedagogical Value**: Convert abstract computational biology concepts into an accessible, interactive format.

---

## 4. Core Features

### CLI Genomic Analysis Dashboard
- **Validation**: Ensures input strings contain only valid nitrogenous bases (`A`, `C`, `G`, `T`).
- **Genomic Metrics**: Computes sequence lengths, GC-content percentages, and outputs a highlighted GC-density map.
- **Central Dogma Processing**: Performs DNA $\rightarrow$ mRNA transcription (replacing Thymine `T` with Uracil `U`) and mRNA $\rightarrow$ Protein translation via the universal genetic code table into 3-letter amino acid codes.
- **Dual Alignment Engines**: Computes end-to-end Global Alignment (Needleman–Wunsch) and localized Local Alignment (Smith–Waterman).
- **Mutation Tracker**: Identifies base positions and classifies mutations into **Transitions** (purine $\leftrightarrow$ purine or pyrimidine $\leftrightarrow$ pyrimidine), **Transversions** (purine $\leftrightarrow$ pyrimidine), and **Gaps** (insertions/deletions).
- **Human-Readable Logs**: Generates plain-English descriptions explaining the biological impact of each detected variance.
- **Developer Mode**: Displays full dynamic programming scoring matrices with highlighted optimal paths directly in the terminal.

### Interactive Biological Simulation (GUI)
- **Pygame 2D Canvas**: Dynamic graphics engine running at a smooth target rate of 60 FPS.
- **Animated DNA/mRNA Strands**: Wiggling helical strand nodes colored by nucleotide type (`A`, `C`, `G`, `T`, `U`).
- **Protein Chain Rendering**: Groups mRNA triplets with connecting brackets and renders synthesized amino acid nodes.
- **Interactive Triggers**: Key `T` triggers animated transcription (glowing magenta `U` substitution with particle effects); Key `P` triggers translation (amino acid assembly).
- **Scoring Matrix Debugger**: Renders the 2D DP matrix in world space with real-time pulsing path highlights.
- **Liquid Traceback Tracer**: Aninterpolated tracer dot walks along the optimal DP path to demonstrate backtracking.
- **Vibrating Hydrogen Bonds**: Dynamic bond connections rendered between matching nucleotide base pairs.
- **Hover Tooltips**: Mouse-over inspection showing full chemical names (e.g., *Adenine*, *Isoleucine*, *START Codon*).
- **Camera Navigation**: Full Mouse Scroll (zoom in/out) and Left-Click Drag (pan canvas).
- **Adaptive Canvas**: Window dynamically scales based on sequence length, clamped safely between $1280 \times 720$ and $1600 \times 900$ pixels.

---

## 5. Algorithms Used

### Needleman–Wunsch (Global Sequence Alignment)
The Needleman–Wunsch algorithm computes the optimal global alignment between two sequence strings $S_1$ of length $n$ and $S_2$ of length $m$. It uses a 2D matrix $F$ of size $(n+1) \times (m+1)$.

$$\text{Scoring Parameters: } \text{Match } s(a,b) = +1, \quad \text{Mismatch } s(a,b) = -1, \quad \text{Gap Penalty } g = -1$$

**Matrix Recurrence Relation:**
$$F(i,j) = \max \begin{cases} 
F(i-1, j-1) + s(S_1[i], S_2[j]) & \text{(Match / Mismatch)} \\ 
F(i-1, j) + g & \text{(Deletion / Gap in } S_2\text{)} \\ 
F(i, j-1) + g & \text{(Insertion / Gap in } S_1\text{)} 
\end{cases}$$

**Initialization:**
$$F(i, 0) = i \cdot g \quad (0 \le i \le n), \qquad F(0, j) = j \cdot g \quad (0 \le j \le m)$$

**Traceback:** Begins at $F(n, m)$ and moves backward towards $F(0,0)$, prioritizing diagonal steps when matching scores match the recurrence state.

---

### Smith–Waterman (Local Sequence Alignment)
The Smith–Waterman algorithm identifies the highest-scoring local region of similarity between two sequences, resetting negative scores to zero to allow local sub-segment matching.

$$\text{Scoring Parameters: } \text{Match } s(a,b) = +2, \quad \text{Mismatch } s(a,b) = -1, \quad \text{Gap Penalty } g = -1$$

**Matrix Recurrence Relation:**
$$H(i,j) = \max \begin{cases} 
0 & \text{(Zero reset)} \\ 
H(i-1, j-1) + s(S_1[i], S_2[j]) & \text{(Match / Mismatch)} \\ 
H(i-1, j) + g & \text{(Deletion)} \\ 
H(i, j-1) + g & \text{(Insertion)} 
\end{cases}$$

**Initialization:**
$$H(i, 0) = 0 \quad (0 \le i \le n), \qquad H(0, j) = 0 \quad (0 \le j \le m)$$

**Traceback:** Starts at $\max_{i,j} H(i,j)$ (the maximum score anywhere in the matrix) and terminates as soon as a cell with score $0$ is reached.

---

### Backtracking & Traceback
Reconstruction of aligned strings $(\text{align}_1, \text{align}_2)$ follows the path from the ending cell back through the DP matrix:
- **Diagonal Step** $(i-1, j-1)$: Emits $S_1[i-1]$ and $S_2[j-1]$.
- **Upward Step** $(i-1, j)$: Emits $S_1[i-1]$ and gap `"-"`.
- **Leftward Step** $(i, j-1)$: Emits gap `"-"` and $S_2[j-1]$.

In [dna.py](file:///Users/jhum/Documents/Padhai%20stuff/college/mca/coding/python/daaaaaa/dna.py), traceback cell coordinates $(i, j)$ are recorded in a list and passed to both the CLI matrix table display and the Pygame tracer particle system.

---

### DNA Transcription & Translation
- **Transcription**: The template strand is converted to mRNA by replacing Thymine with Uracil ($T \rightarrow U$).
- **Translation**: Reads mRNA in consecutive triplets (codons) and maps each triplet to its corresponding single-letter amino acid using the Universal Genetic Code dictionary:

$$\text{Codon Examples: } \text{AUG} \rightarrow \text{M (Methionine/START)}, \quad \text{UAA/UAG/UGA} \rightarrow \text{\_ (STOP)}, \quad \text{GCU} \rightarrow \text{A (Alanine)}$$

---

### Mutation Classification
Nucleotide differences in aligned positions are classified biologically:
- **Match**: $S_1[i] == S_2[i]$
- **Gap / Indel**: $S_1[i] == \text{'-'}$ or $S_2[i] == \text{'-'}$
- **Transition**: Base substitution within the same chemical class:
  - Purine $\leftrightarrow$ Purine: $\{A \leftrightarrow G\}$
  - Pyrimidine $\leftrightarrow$ Pyrimidine: $\{C \leftrightarrow T\}$
- **Transversion**: Base substitution across different chemical classes:
  - Purine $\leftrightarrow$ Pyrimidine: $\{A/G \leftrightarrow C/T\}$

---

## 6. Data Structures Used

The implementation strictly employs standard Python data structures suited for algorithm performance and readability:

| Data Structure | Implementation | Location / Usage in Code | Academic Rationale |
| :--- | :--- | :--- | :--- |
| **Dictionary (`dict`)** | `self.codon_table`, `self.aa_names`, `self.aa_3letter` | `Dna.__init__()` | Provides $O(1)$ average time complexity for codon-to-amino-acid and abbreviation lookups. |
| **2D List (`list[list[int]]`)** | `score` matrix | `needleman_wunsch()`, `smith_waterman()` | Stores sub-problem scores for DP recurrence relations of size $(n+1) \times (m+1)$. |
| **List of Tuples (`list[tuple]`)** | `path` coordinate array | `needleman_wunsch()`, `smith_waterman()` | Stores ordered traceback coordinates $(i, j)$ for matrix path rendering and tracer movement. |
| **Set (`set`)** | `valid_chars`, `purines`, `pyrimidines`, `path_set` | `validate_dna()`, `classify_mutation()`, GUI matrix | Enables $O(1)$ membership checking for character validation, base grouping, and matrix grid path coloring. |
| **String (`str`)** | Sequence buffers | Throughout `Dna` class | Immutable representations of DNA/mRNA sequences and formatted terminal output. |
| **1D List (`list[int]`)** | `prev_row`, `curr_row` | `edit_distance()` | Reduces space complexity to $O(m)$ for space-optimized Levenshtein edit distance computation. |

---

## 7. Complexity Analysis

| Operation / Function | Algorithmic Method | Time Complexity | Space Complexity | Complexity Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **DNA Validation** | Character iteration | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Single pass over input string against set lookups. |
| **GC Content** | String count | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Iterates over string to sum `G` and `C` occurrences. |
| **Transcription** | String replacement | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | Constructs a new mRNA string of length $n$. |
| **Translation** | Triplet loop + Dict lookup | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | Processes $n/3$ codons with $O(1)$ table lookups. |
| **Edit Distance** | 2-row Dynamic Programming | $\mathcal{O}(n \cdot m)$ | $\mathcal{O}(m)$ | Space optimized using only previous and current matrix rows. |
| **Needleman–Wunsch** | Full Matrix Dynamic Programming | $\mathcal{O}(n \cdot m)$ | $\mathcal{O}(n \cdot m)$ | Computes full matrix for global alignment traceback. |
| **Smith–Waterman** | Full Matrix Dynamic Programming | $\mathcal{O}(n \cdot m)$ | $\mathcal{O}(n \cdot m)$ | Computes full matrix for local alignment traceback. |
| **Traceback** | Matrix Backtracking | $\mathcal{O}(n + m)$ | $\mathcal{O}(n + m)$ | Walks from end/max cell back to start along optimal path. |

---

## 8. System Workflow

```
                        ┌──────────────────────────────┐
                        │   DNA Sequence Inputs (S1, S2)│
                        └──────────────┬───────────────┘
                                       │
                                       ▼
                        ┌──────────────────────────────┐
                        │     Sequence Validation      │
                        │    (ACGT character check)    │
                        └──────────────┬───────────────┘
                                       │
                         ┌─────────────┴─────────────┐
                         ▼                           ▼
            ┌─────────────────────────┐ ┌─────────────────────────┐
            │   Genomic Metrics       │ │   Central Dogma Engine  │
            │ (GC Content & Density)  │ │   DNA ➔ mRNA ➔ Protein  │
            └────────────┬────────────┘ └────────────┬────────────┘
                         │                           │
                         └─────────────┬─────────────┘
                                       │
                                       ▼
                        ┌──────────────────────────────┐
                        │  Dynamic Programming Alignment│
                        │  • Needleman-Wunsch (Global) │
                        │  • Smith-Waterman (Local)    │
                        └──────────────┬───────────────┘
                                       │
                                       ▼
                        ┌──────────────────────────────┐
                        │    DP Matrix Backtracking    │
                        │   (Reconstruct Path & Score) │
                        └──────────────┬───────────────┘
                                       │
                                       ▼
                        ┌──────────────────────────────┐
                        │      Mutation Tracker        │
                        │ (Transition/Transversion/Gap)│
                        └──────────────┬───────────────┘
                                       │
                         ┌─────────────┴─────────────┐
                         ▼                           ▼
            ┌─────────────────────────┐ ┌─────────────────────────┐
            │  CLI Dashboard Output   │ │   Pygame 2D Simulation  │
            │ (ANSI Grids & Tables)   │ │  (Pan/Zoom & Controls)  │
            └─────────────────────────┘ └─────────────────────────┘
```

---

## 9. Architecture

The application is structured into decoupled functional layers:

1. **Input & Validation Layer**: Handles user prompts, string normalization, and base verification (`validate_dna`).
2. **Genomic Analysis Engine (`Dna` class)**: Core domain logic for metrics, transcription, translation, and mutation classification.
3. **Alignment & Matrix Computation**: Implements Needleman–Wunsch, Smith–Waterman, and Levenshtein algorithms.
4. **CLI Dashboard Component (`display_dashboard`)**: Formats visual text boxes, ANSI color codes, and DP matrix debug tables.
5. **Interactive GUI Engine (`DNAVisualizer` class)**: Pygame-driven graphics system managing rendering loops, world-to-screen coordinate transformation, dynamic particle systems, and event handling.
6. **Graceful Fallback Handler**: Detects optional dependency availability (`PYGAME_AVAILABLE`, `RICH_AVAILABLE`) and routes execution appropriately.

---

## 10. Project Structure

```
helel04-dnaSequenceAnalyser/
├── dna.py          # Core application file containing all analytics and Pygame visualizer
├── .gitignore      # Git exclusion rules for virtualenv, caches, and local files
└── README.md       # Complete academic and project documentation
```

---

## 11. Technology Stack

- **Core Language**: Python 3.9+
- **GUI & Graphics Engine**: Pygame 2.6.1 (2D rendering, particle system, math transform)
- **Formatting Utilities**: Rich (Optional ANSI formatting) / Fallback ANSI sequence constants
- **Standard Libraries**: `time`, `os`, `re`, `math`

---

## 12. Installation

### Prerequisites
- Python 3.9 or higher installed.

### Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/helel04/dnaSequenceAnalyser.git
   cd dnaSequenceAnalyser
   ```

2. **Create and Activate Virtual Environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install pygame rich
   ```

---

## 13. Running the Project

Run the main script using Python:

```bash
python dna.py
```

### Interactive Prompts
1. `Sequence 1:` Enter the first DNA sequence (e.g., `ATGCGATCGAT`).
2. `Sequence 2:` Enter the second DNA sequence (e.g., `ATGCGTCGAT`).
3. `Enable Developer Mode? (y/n):` Enter `y` to view full DP matrices in the CLI.
4. `Launch Interactive Bio-Sim? (y/n):` Enter `y` to open the 2D Pygame visualizer.

---

## 14. GUI Controls

When the Pygame Simulation window is active:

| Key / Input | Action |
| :--- | :--- |
| **`T` Key** | Triggers DNA $\rightarrow$ mRNA Transcription animation (glowing Uracil `U` replacement). |
| **`P` Key** | Triggers mRNA $\rightarrow$ Protein Translation animation (amino acid node synthesis). |
| **Mouse Scroll Up** | Zoom in canvas. |
| **Mouse Scroll Down** | Zoom out canvas. |
| **Left Click + Drag** | Pan canvas around world coordinates. |
| **Mouse Hover** | Displays base / amino acid full names in a tooltip box. |
| **Window Close (`X`)** | Exits simulation mode gracefully and returns to terminal. |

---

## 15. Example Output

### Genuine Execution Capture

Input Sequences:
- **Sequence 1**: `ATGCGATCGAT` (Length: 11)
- **Sequence 2**: `ATGCGTCGAT` (Length: 10)

```text
╔══════════════════════════════════════════════════════════════════════════════╗
║                   GENOMIC ANALYSIS DASHBOARD                                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
[ THE DNA WORKFLOW (CENTRAL DOGMA) ]
 DNA Blueprint (Source Code) stays protected. Transcription copies a segment,
 replacing 'T' with 'U'. The mRNA (Portable Copy) then delivers instructions.

[ GENOMIC METRICS & TRANSCRIPTION ]
 Sequence 1: Length: 11 | GC-Density: 45.5% | Map: ATGCGATCGAT
   ┌──────────────────────────────────────────────────────┐
   │ TRANSCRIPTION & TRANSLATION                           │
   │ Template DNA:        ATGCGATCGAT                      │
   │ Transcribed mRNA:    AUGCGAUCGAU                      │
   │ Resulting Protein:   [Met][Arg][Ser]                  │
   │ Note: U replaces T | Codons form Protein              │
   └──────────────────────────────────────────────────────┘

 Sequence 2: Length: 10 | GC-Density: 50.0% | Map: ATGCGTCGAT
   ┌──────────────────────────────────────────────────────┐
   │ TRANSCRIPTION & TRANSLATION                           │
   │ Template DNA:        ATGCGTCGAT                       │
   │ Transcribed mRNA:    AUGCGUCGAU                       │
   │ Resulting Protein:   [Met][Arg][Arg]                  │
   │ Note: U replaces T | Codons form Protein              │
   └──────────────────────────────────────────────────────┘

[ ALIGNMENT COMPARISON ]
GLOBAL (Big Picture Comparison)               | LOCAL (Pattern Hunter)                  
ATGCGATCGAT                                   | ATGCGATCGAT
||||| |||||                                   | ||||| |||||
ATGCG-TCGAT                                   | ATGCG-TCGAT

[ MUTATION TRACKER ]
 • [Pos 6] Gap (Missing Base): Skips an instruction. Base 'A' is absent in the target. (This is a deletion/insertion mutation).
```

### Global Alignment Matrix (Developer Mode Output)
```text
 Global Matrix Debugger 
     |  -   |  A   |  T   |  G   |  C   |  G   |  T   |  C   |  G   |  A   |  T   |
-----------------------------------------------------------------------------------
 -   |  0   |  -1  |  -2  |  -3  |  -4  |  -5  |  -6  |  -7  |  -8  |  -9  | -10  | 
 A   |  -1  |  1   |  0   |  -1  |  -2  |  -3  |  -4  |  -5  |  -6  |  -7  |  -8  | 
 T   |  -2  |  0   |  2   |  1   |  0   |  -1  |  -2  |  -3  |  -4  |  -5  |  -6  | 
 G   |  -3  |  -1  |  1   |  3   |  2   |  1   |  0   |  -1  |  -2  |  -3  |  -4  | 
 C   |  -4  |  -2  |  0   |  2   |  4   |  3   |  2   |  1   |  0   |  -1  |  -2  | 
 G   |  -5  |  -3  |  -1  |  1   |  3   |  5   |  4   |  3   |  2   |  1   |  0   | 
 A   |  -6  |  -4  |  -2  |  0   |  2   |  4   |  4   |  3   |  2   |  3   |  2   | 
 T   |  -7  |  -5  |  -3  |  -1  |  1   |  3   |  5   |  4   |  3   |  2   |  4   | 
 C   |  -8  |  -6  |  -4  |  -2  |  0   |  2   |  4   |  6   |  5   |  4   |  3   | 
 G   |  -9  |  -7  |  -5  |  -3  |  -1  |  1   |  3   |  5   |  7   |  6   |  5   | 
 A   | -10  |  -8  |  -6  |  -4  |  -2  |  0   |  2   |  4   |  6   |  8   |  7   | 
 T   | -11  |  -9  |  -7  |  -5  |  -3  |  -1  |  1   |  3   |  5   |  7   |  9   | 
-----------------------------------------------------------------------------------
```

---

## 16. Understanding the Output

- **Genomic Metrics**: Shows string length, GC-content percentage, and GC-density visual highlighting.
- **Transcription & Translation Box**: Shows template DNA, transcribed mRNA, and synthesized amino acid protein chain.
- **Global Alignment**: End-to-end alignment using vertical bars (`|`) for matches, dots (`.`) for mismatches, and spaces for gaps.
- **Local Alignment**: Pinpoints conserved regional sub-segments.
- **Mutation Tracker**: Position-by-position log detailing specific mutation types.
- **Interactive Key**: Legend summarizing visual indicators across CLI and GUI.

---

## 17. DP Matrix Visualization

In both CLI Developer Mode and the Pygame GUI:
- **Grid Layout**: Rows represent Sequence 1 ($S_1$), columns represent Sequence 2 ($S_2$).
- **Cell Scores**: Each cell $(i, j)$ contains the optimal alignment score for sub-problem $S_1[1..i]$ and $S_2[1..j]$.
- **Highlighted Route**: Displays the traceback path selected by the algorithm.
- **Liquid Tracer (GUI)**: An animated particle interpolation highlights how the computer backtracks from the destination cell to origin.

---

## 18. Central Dogma Visualization

The system models the fundamental process of molecular biology:

$$\text{DNA Template Strand} \xrightarrow{\text{Transcription (T } \rightarrow \text{ U)}} \text{mRNA Copy} \xrightarrow{\text{Translation (Codon Mapping)}} \text{Protein Polypeptide Chain}$$

1. **DNA**: Double-stranded storage template (`ATGCGATCG...`).
2. **mRNA**: Single-stranded messenger copy (`AUGCGAUCG...`).
3. **Protein**: Synthesized amino acid chain (`[Met][Arg][Ser]...`).

---

## 19. Mutation Analysis

Mutation tracking explicitly categorizes sequence differences:

- **Match (`|`)**: Nucleotides match perfectly.
- **Gap (`-`)**: Insertion or deletion mutation.
- **Transition Mutation**: Substitution between base types of the same chemical family ($A \leftrightarrow G$ or $C \leftrightarrow T$).
- **Transversion Mutation**: Substitution between base types of different chemical families ($A/G \leftrightarrow C/T$).

---

## 20. Graceful Degradation

The application features graceful fallback handling for missing external libraries:

```
                  ┌───────────────────────────────┐
                  │    Application Start (dna.py) │
                  └───────────────┬───────────────┘
                                  │
                       Check Pygame Availability
                                  │
                 ┌────────────────┴────────────────┐
                 ▼                                 ▼
      [Pygame Installed]                 [Pygame Missing]
                 │                                 │
     Full CLI Analysis Dashboard       Full CLI Analysis Dashboard
                 +                                 +
     Interactive 2D Simulation           Terminal Matrix Output
```

---

## 21. Design / Visualization Philosophy

The interface follows strict visual semantics across CLI and GUI:
- **Green (`#38;5;46m` / RGB `50,200,50`)**: Perfect Matches.
- **Bright Red (`#38;5;196m` / RGB `200,50,50`)**: Transversion Mutations.
- **Dark Red (`#38;5;88m`)**: Transition Mutations.
- **Yellow (`#38;5;226m`)**: Insertions / Deletions (Gaps).
- **Magenta (`#38;5;201m` / RGB `255,0,255`)**: Uracil (`U`) & Transcription process.
- **Orange (RGB `255,150,50`)**: Protein Amino Acid nodes.

---

## 22. Performance / Constraints

- **Frame Rate Target**: Pygame loop capped at 60 FPS using `clock.tick(60)`.
- **Dynamic Resolution**: Window size scales according to sequence length with safety bounds ($1280 \times 720 \le W \times H \le 1600 \times 900$).
- **Memory Scaling**: Matrix size scales as $\mathcal{O}(n \cdot m)$.

---

## 23. Limitations

- **Fixed Scoring Matrices**: Uses static default linear match/mismatch/gap scores rather than configurable substitution matrices (such as BLOSUM62 or PAM250).
- **Sequence Length**: Pygame 2D grid rendering is designed for educational sequence lengths ($\le 100$ bases).
- **Format Support**: Direct raw sequence string input (no built-in FASTA file parser).
- **Persistence**: Runs in-memory without persistent database storage.

---

## 24. Future Scope

- Integration of BLOSUM62 & PAM250 scoring matrices.
- FASTA / FASTQ file upload and parsing.
- Multiple Sequence Alignment (MSA) using ClustalW-style progressive alignment.
- Exporting alignment reports to PDF / HTML format.

---

## 25. Educational / Academic Relevance

This project directly serves computer science and bioinformatics courses (*Design and Analysis of Algorithms* - MC507):
- **Dynamic Programming**: Practical demonstration of overlapping sub-problems and optimal substructure.
- **Backtracking**: Explicit path reconstruction through state tables.
- **String Processing**: String alignment, metrics, and translation algorithms.

---

## 26. Expected Outcomes

- Enhanced pedagogical understanding of dynamic programming alignment algorithms.
- Clear visual differentiation between Global (Needleman–Wunsch) and Local (Smith–Waterman) alignments.
- Intuitive exploration of Central Dogma mechanics through interactive simulation.

---

## 27. Team

- **Parijat Chatterjee**
- **Komolika Dagare**
- **Shreyash Dahibhavkar**

---

## 28. Academic Information

- **Program**: First Year Master of Computer Applications (F.Y. MCA)
- **Semester**: Semester II (AY 2025–2026)
- **Course**: Design and Analysis of Algorithms
- **Course Code**: MC507

---

## 29. References

1. Needleman, S. B., & Wunsch, C. D. (1970). A general method applicable to the search for similarities in the amino acid sequence of two proteins. *Journal of Molecular Biology*, 48(3), 443-453.
2. Smith, T. F., & Waterman, M. S. (1981). Identification of common molecular subsequences. *Journal of Molecular Biology*, 147(1), 195-197.
3. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press. (Chapter 15: Dynamic Programming).
4. Pygame Development Team. Pygame Documentation (v2.6.1). https://www.pygame.org/docs/
