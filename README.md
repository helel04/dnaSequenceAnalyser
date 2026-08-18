# Interactive Genomic Analysis And Biological Simulation System

> **An Educational Bioinformatics & Dynamic Programming Visualization Platform**  
> *Translating abstract sequence alignment matrices and Central Dogma concepts into readable CLI text dashboards and optional interactive 2D graphical animations.*

![Python Source Compatibility](https://img.shields.io/badge/Python%20Source-3.6%2B-blue.svg)
![Python Recommended Runtime](https://img.shields.io/badge/Python%20Runtime-3.8%2B%20(Recommended)-brightgreen.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0%2B%20(Optional)-green.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-Dynamic%20Programming-orange.svg)
![Project Scope](https://img.shields.io/badge/Scope-Academic%20%2F%20Educational-blue.svg)

The **Interactive Genomic Analysis And Biological Simulation System** is an educational software tool written in Python. It is designed to demonstrate theoretical algorithm design (Needleman–Wunsch global alignment, Smith–Waterman local alignment, and Levenshtein edit distance) alongside diagrammatic visual representations of Central Dogma concepts (DNA-to-mRNA transcription, codon-to-amino-acid translation, base-pairing visual indicators, and dynamic programming matrix backtracking).

---

## Table of Contents

1. [Project Overview](#1-project-overview)
2. [Problem Statement](#2-problem-statement)
3. [Objectives](#3-objectives)
4. [Core Features](#4-core-features)
   - [CLI Genomic Analysis Dashboard](#cli-genomic-analysis-dashboard)
   - [Interactive 2D Visualizer (Optional GUI)](#interactive-2d-visualizer-optional-gui)
5. [Why This Project Is Interesting](#5-why-this-project-is-interesting)
   - [Educational Scope vs. Production Bioinformatics](#educational-scope-vs-production-bioinformatics)
   - [Key Differentiator: Visual Algorithm Step-Through](#key-differentiator-visual-algorithm-step-through)
   - [Technical & Engineering Rationale](#technical--engineering-rationale)
   - [Evaluator & Academic Relevance](#evaluator--academic-relevance)
6. [Algorithms Used](#6-algorithms-used)
   - [Needleman–Wunsch (Global Alignment)](#needleman-wunsch-global-alignment)
   - [Smith–Waterman (Local Alignment)](#smith-waterman-local-alignment)
   - [Backtracking & Traceback](#backtracking--traceback)
   - [DNA Transcription & Translation](#dna-transcription--translation)
   - [Mutation Classification](#mutation-classification)
7. [Data Structures Used](#7-data-structures-used)
8. [Complexity Analysis](#8-complexity-analysis)
9. [System Workflow](#9-system-workflow)
10. [Architecture](#10-architecture)
11. [Project Structure](#11-project-structure)
12. [Technology Stack](#12-technology-stack)
13. [Installation](#13-installation)
14. [Running the Project](#14-running-the-project)
15. [GUI Controls](#15-gui-controls)
16. [Example Output](#16-example-output)
17. [Understanding the Output](#17-understanding-the-output)
18. [DP Matrix Visualization](#18-dp-matrix-visualization)
19. [Central Dogma Diagrammatic Flow](#19-central-dogma-diagrammatic-flow)
20. [Mutation Analysis](#20-mutation-analysis)
21. [Graceful Degradation Architecture](#21-graceful-degradation-architecture)
22. [Visual Design Language](#22-visual-design-language)
23. [Performance & Execution Constraints](#23-performance--execution-constraints)
24. [Scope & Limitations](#24-scope--limitations)
25. [Future Scope](#25-future-scope)
26. [Educational & Academic Relevance](#26-educational--academic-relevance)
27. [Expected Learning Outcomes](#27-expected-learning-outcomes)
28. [Team](#28-team)
29. [Academic Information](#29-academic-information)
30. [References](#30-references)

---

## 1. Project Overview

In computer science and bioinformatics education, 2D Dynamic Programming (DP) score grids and string transformation steps are often presented as static numerical matrices or plain text outputs. Students frequently struggle to trace how cell state dependencies ($S_{i,j}$) construct optimal alignment paths or how sequence variations map onto amino acid translations.

This system provides a combined **sequence analysis engine**, **algorithm visualizer**, and **educational process diagram**:
- A **CLI Analytical Dashboard** running in standard terminal environments, offering nucleotide metrics, transcription/translation mappings, global/local sequence alignment tables, and plain-English mutation descriptions.
- An **Optional Interactive Pygame 2D Visualizer** providing a graphical canvas with wiggling sequence nodes, matrix coordinate path tracing (`lerp`), base-pair connection lines with visual sine-wave vibration, amino acid codon grouping brackets, mouse pan/zoom, and real-time keyboard triggers.

> [!NOTE]
> This platform is an **educational teaching tool** designed for small nucleotide sequence pairs (recommended $\le 100$ bases). It is not a production-grade molecular modeling suite or genomic database query engine.

---

## 2. Problem Statement

This project addresses four specific educational challenges in algorithm pedagogy:

1. **Matrix Interpretation**: Traditional dynamic programming matrices are displayed as static numerical arrays, making it difficult to visualize step-by-step path selection.
2. **Algorithmic Distinction**: Students often find it difficult to contrast global end-to-end sequence alignment (Needleman–Wunsch) with local sub-region pattern matching (Smith–Waterman).
3. **Conceptual Dogma Mappings**: Translating DNA template strands into mRNA (`T` $\rightarrow$ `U`) and grouping codons into amino acids is frequently taught abstractly rather than step-by-step.
4. **Static Command-Line Boundaries**: Plain text outputs lack visual stepping, coordinate navigation (zooming, panning), or interactive keyboard cues to aid concept retention.

---

## 3. Objectives

The primary objectives implemented in the core engine [dna.py](file:///Users/jhum/Documents/Padhai%20stuff/college/mca/coding/python/daaaaaa/dna.py) are:

- **Sequence String Validation**: Validate input strings to ensure they contain only standard nitrogenous base characters (`A`, `C`, `G`, `T`).
- **Genomic Metrics Calculation**: Compute GC-content percentages and output a GC-density sequence map.
- **Global Sequence Alignment**: Implement the Needleman–Wunsch algorithm using dynamic programming to find optimal overall sequence similarity.
- **Local Sequence Alignment**: Implement the Smith–Waterman algorithm using dynamic programming to isolate highly conserved regional sub-segments.
- **Mutation Categorization**: Classify sequence variations into Matches, Insertions/Deletions (Gaps), Transitions, and Transversions.
- **Central Dogma Process Rendering**: Render step-by-step molecular conversion from DNA templates to mRNA and synthesized 3-letter amino acid chains.
- **DP Traceback Rendering**: Highlight optimal routes through dynamic programming matrices in terminal text tables and optional 2D graphics.
- **Pedagogical Enhancement**: Present abstract string alignment algorithms in an accessible, interactive interface.

---

## 4. Core Features

### CLI Genomic Analysis Dashboard
- **Validation**: Restricts input strings to valid uppercase bases (`A`, `C`, `G`, `T`).
- **Genomic Metrics**: Computes sequence lengths, GC-content percentages, and renders a GC-density highlighted string map.
- **Central Dogma Mapping**: Performs DNA $\rightarrow$ mRNA transcription (replacing Thymine `T` with Uracil `U`) and mRNA $\rightarrow$ Protein translation using the universal genetic code dictionary into 3-letter amino acid codes.
- **Dual Alignment Engines**: Computes end-to-end Global Alignment (Needleman–Wunsch) and localized Local Alignment (Smith–Waterman).
- **Mutation Tracker**: Identifies alignment positions and classifies variations into **Transitions** (purine $\leftrightarrow$ purine or pyrimidine $\leftrightarrow$ pyrimidine), **Transversions** (purine $\leftrightarrow$ pyrimidine), and **Gaps** (insertions/deletions).
- **Human-Readable Descriptions**: Generates plain-English descriptions explaining the biological classification of each detected variance.
- **Developer Mode**: Prints full dynamic programming scoring matrices with highlighted optimal paths directly in terminal text.

### Interactive 2D Visualizer (Optional GUI)
- **Pygame 2D Canvas**: Graphics rendering loop targeting 60 FPS when `pygame` is installed.
- **Sequence Strand Nodes**: Rendered nodes representing nucleotides (`A`, `C`, `G`, `T`, `U`) with visual sine-wave vertical offsets.
- **Protein Chain Representation**: Groups mRNA triplets with connecting visual brackets and renders synthesized amino acid nodes.
- **Interactive Keyboard Triggers**: Key `T` triggers an animated transcription visual sequence (glowing Uracil `U` nodes with particle bursts); Key `P` triggers translation (amino acid node rendering).
- **Matrix Debugger Grid**: Renders the 2D DP matrix grid in world coordinates with pulsing path highlights.
- **Traceback Particle Tracer**: Interpolates (`lerp`) a visual tracer dot along ordered matrix cell coordinates $(i, j)$ to demonstrate backtracking.
- **Base-Pair Connection Lines**: Renders indicator lines between matching bases with a pseudo-vibrational sine-wave visual offset.
- **Hover Inspection**: Mouse-over tooltips showing nucleotide and amino acid full names (e.g., *Adenine*, *Methionine (START)*).
- **Canvas Camera Controls**: Mouse scroll (zoom in/out) and left-click drag (pan canvas).
- **Dynamic Window Scaling**: Scales canvas dimensions based on sequence length within safe boundaries ($1280 \times 720 \le W \times H \le 1600 \times 900$).

---

## 5. Why This Project Is Interesting

### Educational Scope vs. Production Bioinformatics
This project is explicitly designed as an **educational software demonstration** for computer science coursework. Unlike production bioinformatics pipelines (such as BLAST, Clustal Omega, or Biopython-backed tools) that handle megabase-scale FASTA files with complex substitution matrices, this system focuses on making small-scale dynamic programming grids and string translation steps visible, interactive, and transparent.

### Key Differentiator: Visual Algorithm Step-Through
The system's primary strength lies in transforming abstract algorithm states into visual step-through displays:
- **Matrix Path Interpolation**: The 2D visualizer reads the exact traceback tuple path $(i, j)$ generated by the Needleman–Wunsch algorithm and animates a linear interpolation (`lerp`) tracer moving cell-by-cell backward through the DP grid.
- **Keyboard-Driven Process Stepping**: Pressing `T` triggers an animated DNA-to-mRNA transcription sequence, while `P` step-translates mRNA codons into amino acid nodes with connecting grouping brackets.
- **Native Algorithm Implementation**: Dynamic programming recurrences, matrix array allocations, traceback paths, codon translation tables, and visual canvas logic are implemented directly in Python standard libraries and basic Pygame primitives, without relying on third-party bioinformatics packages.

### Technical & Engineering Rationale
- **Dual Representation of DP State**: A single matrix calculation populates both a terminal text debugger table and a 2D world-space graphical grid.
- **Graceful Degradation Architecture**: The codebase uses `try...except ImportError` guards (`PYGAME_AVAILABLE`, `RICH_AVAILABLE`). If optional packages are absent, the application gracefully degrades to a fully functional terminal CLI dashboard using native ANSI escape codes.
- **Biologically Accurate Mutation Categorization**: Rather than returning plain numeric edit distances, it evaluates base ring structures to distinguish Purine $\leftrightarrow$ Purine / Pyrimidine $\leftrightarrow$ Pyrimidine substitutions (*Transitions*) from Purine $\leftrightarrow$ Pyrimidine substitutions (*Transversions*).

### Evaluator & Academic Relevance
- **Algorithm Fundamentals**: Demonstrates hands-on implementation of Dynamic Programming recurrence relations, matrix backtracking, string parsing, and state management.
- **Interactive Graphics Math**: Demonstrates 2D coordinate system transformations (`world_to_screen` / `screen_to_world`), camera zooming/panning math, and linear interpolation state loops.
- **Clean Architecture**: Maintains separation between core domain logic (`Dna`), visual UI rendering (`DNAVisualizer`), and fallback handlers.

---

## 6. Algorithms Used

### Needleman–Wunsch (Global Sequence Alignment)
Computes optimal end-to-end global sequence alignment between $S_1$ (length $n$) and $S_2$ (length $m$) using a $(n+1) \times (m+1)$ matrix $F$.

$$\text{Fixed Parameters in Code: } \text{Match } s(a,b) = +1, \quad \text{Mismatch } s(a,b) = -1, \quad \text{Gap Penalty } g = -1$$

**Recurrence Relation:**
$$F(i,j) = \max \begin{cases} 
F(i-1, j-1) + s(S_1[i], S_2[j]) & \text{(Match / Mismatch)} \\ 
F(i-1, j) + g & \text{(Deletion / Gap in } S_2\text{)} \\ 
F(i, j-1) + g & \text{(Insertion / Gap in } S_1\text{)} 
\end{cases}$$

**Initialization:**
$$F(i, 0) = i \cdot g \quad (0 \le i \le n), \qquad F(0, j) = j \cdot g \quad (0 \le j \le m)$$

**Traceback:** Starts at $F(n, m)$ and moves backward to $F(0,0)$, recording path cell coordinates $(i, j)$.

---

### Smith–Waterman (Local Sequence Alignment)
Identifies the highest-scoring local sub-segment similarity between sequences by resetting negative cell scores to zero.

$$\text{Fixed Parameters in Code: } \text{Match } s(a,b) = +2, \quad \text{Mismatch } s(a,b) = -1, \quad \text{Gap Penalty } g = -1$$

**Recurrence Relation:**
$$H(i,j) = \max \begin{cases} 
0 & \text{(Zero reset lower bound)} \\ 
H(i-1, j-1) + s(S_1[i], S_2[j]) & \text{(Match / Mismatch)} \\ 
H(i-1, j) + g & \text{(Deletion)} \\ 
H(i, j-1) + g & \text{(Insertion)} 
\end{cases}$$

**Initialization:**
$$H(i, 0) = 0 \quad (0 \le i \le n), \qquad H(0, j) = 0 \quad (0 \le j \le m)$$

**Traceback:** Starts at $\max_{i,j} H(i,j)$ (maximum matrix cell) and terminates when a cell with score $0$ is reached.

---

### Backtracking & Traceback
Reconstructs aligned sequence strings $(\text{align}_1, \text{align}_2)$ by stepping backward through DP matrix states:
- **Diagonal Step** $(i-1, j-1)$: Emits $S_1[i-1]$ and $S_2[j-1]$.
- **Upward Step** $(i-1, j)$: Emits $S_1[i-1]$ and gap `"-"`.
- **Leftward Step** $(i, j-1)$: Emits gap `"-"` and $S_2[j-1]$.

In [dna.py](file:///Users/jhum/Documents/Padhai%20stuff/college/mca/coding/python/daaaaaa/dna.py), traceback cell coordinates $(i, j)$ are returned in a list used by both terminal matrix tables and the 2D visualizer tracer.

---

### DNA Transcription & Translation
- **Transcription**: Replaces Thymine bases with Uracil ($T \rightarrow U$) to construct mRNA.
- **Translation**: Reads mRNA in consecutive non-overlapping triplets (codons) and maps each to an amino acid via the universal genetic code dictionary:

$$\text{Codon Examples: } \text{AUG} \rightarrow \text{M (Methionine/START)}, \quad \text{UAA/UAG/UGA} \rightarrow \text{\_ (STOP)}, \quad \text{GCU} \rightarrow \text{A (Alanine)}$$

---

### Mutation Classification
Categorizes nucleotide alignment differences:
- **Match**: $S_1[i] == S_2[i]$
- **Gap / Indel**: $S_1[i] == \text{'-'}$ or $S_2[i] == \text{'-'}$
- **Transition Mutation**: Base substitution within the same chemical ring family:
  - Purine $\leftrightarrow$ Purine: $\{A \leftrightarrow G\}$
  - Pyrimidine $\leftrightarrow$ Pyrimidine: $\{C \leftrightarrow T\}$
- **Transversion Mutation**: Base substitution across different chemical ring families:
  - Purine $\leftrightarrow$ Pyrimidine: $\{A/G \leftrightarrow C/T\}$

---

## 7. Data Structures Used

| Data Structure | Implementation | Location in Code | Purpose & Usage |
| :--- | :--- | :--- | :--- |
| **Dictionary (`dict`)** | `self.codon_table`, `self.aa_names`, `self.aa_3letter` | `Dna.__init__()` | Provides $O(1)$ average lookup for 64 codons and amino acid labels. |
| **2D List (`list[list[int]]`)** | `score` matrix | `needleman_wunsch()`, `smith_waterman()` | Stores sub-problem alignment scores for $(n+1) \times (m+1)$ DP tables. |
| **List of Tuples (`list[tuple]`)** | `path` coordinate array | `needleman_wunsch()`, `smith_waterman()` | Stores ordered matrix cell coordinates $(i, j)$ for traceback rendering. |
| **Set (`set`)** | `valid_chars`, `purines`, `pyrimidines`, `path_set` | `validate_dna()`, `classify_mutation()`, GUI matrix | Enables $O(1)$ membership checks for validation, base grouping, and matrix grid highlights. |
| **String (`str`)** | Sequence buffers | Throughout `Dna` class | Stores DNA, mRNA, alignment strings, and ANSI formatting codes. |
| **1D List (`list[int]`)** | `prev_row`, `curr_row` | `edit_distance()` | Reduces space complexity to $O(m)$ for Levenshtein edit distance calculations. |

---

## 8. Complexity Analysis

| Operation / Function | Algorithmic Method | Time Complexity | Space Complexity | Complexity Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **DNA Validation** | Character iteration | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Single pass over string length $n$ using set lookup. |
| **GC Content** | String character counting | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ | Counts occurrences of `G` and `C` in string of length $n$. |
| **Transcription** | Character replacement | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | Creates a new mRNA string of length $n$. |
| **Translation** | Triplet iteration + Dict lookup | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | Processes $n/3$ codons with $O(1)$ dictionary lookups. |
| **Edit Distance** | 2-row Dynamic Programming | $\mathcal{O}(n \cdot m)$ | $\mathcal{O}(m)$ | Uses 2 rows of size $m+1$ for space optimization. |
| **Needleman–Wunsch** | Full Matrix Dynamic Programming | $\mathcal{O}(n \cdot m)$ | $\mathcal{O}(n \cdot m)$ | Computes full matrix for global alignment traceback. |
| **Smith–Waterman** | Full Matrix Dynamic Programming | $\mathcal{O}(n \cdot m)$ | $\mathcal{O}(n \cdot m)$ | Computes full matrix for local alignment traceback. |
| **Traceback** | Matrix Backtracking | $\mathcal{O}(n + m)$ | $\mathcal{O}(n + m)$ | Steps backward along matrix dimensions to build alignment strings. |

---

## 9. System Workflow

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
            │  CLI Dashboard Output   │ │   Pygame 2D Visualizer  │
            │ (ANSI Grids & Tables)   │ │ (Optional GUI Canvas)   │
            └─────────────────────────┘ └─────────────────────────┘
```

---

## 10. Architecture

The application consists of the following components in [dna.py](file:///Users/jhum/Documents/Padhai%20stuff/college/mca/coding/python/daaaaaa/dna.py):

1. **Input & Validation Layer**: Accepts user sequences, converts to uppercase, and verifies `A/C/G/T` characters (`validate_dna`).
2. **Genomic Analysis Engine (`Dna` class)**: Core logic for GC metrics, transcription, translation, and mutation classification.
3. **Alignment Computations**: Implements Needleman–Wunsch, Smith–Waterman, and Levenshtein algorithms.
4. **CLI Dashboard Component (`display_dashboard`)**: Formats terminal text panels, ANSI color highlighting, and DP debug tables.
5. **Interactive 2D Visualizer (`DNAVisualizer` class)**: Optional Pygame visual rendering engine managing world-to-screen coordinate math, particle visual effects, and keyboard event loops.
6. **Fallback Mechanism**: Detects optional dependency availability (`PYGAME_AVAILABLE`, `RICH_AVAILABLE`) via `try...except ImportError` blocks.

---

## 11. Project Structure

```
helel04-dnaSequenceAnalyser/
├── dna.py          # Core application file containing analytical engine and Pygame visualizer
├── .gitignore      # Git exclusion rules for virtual environments, caches, and local files
└── README.md       # Project documentation
```

---

## 12. Technology Stack

- **Core Language**: Python (Source compatible with **Python 3.6+** due to f-string usage; **Python 3.8+ recommended** for pre-compiled dependency binary wheels across platforms).
- **Required Dependencies**: Python Standard Library (`math`, `os`, `re`, `time`).
- **Optional Dependencies**:
  - `pygame` (v2.0+): Optional 2D graphical visualizer canvas.
  - `rich`: Optional terminal text styling (falls back to native ANSI escape sequences if unavailable).

---

## 13. Installation

### Prerequisites
- Python 3.6 or higher installed (Python 3.8+ recommended).

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

3. **Install Optional Dependencies (For GUI Visualization):**
   ```bash
   pip install pygame rich
   ```

---

## 14. Running the Project

Run the application using Python:

```bash
python dna.py
```

### Interactive Prompts
1. `Sequence 1:` Enter the first DNA sequence string (e.g., `ATGCGATCGAT`).
2. `Sequence 2:` Enter the second DNA sequence string (e.g., `ATGCGTCGAT`).
3. `Enable Developer Mode? (y/n):` Enter `y` to print full DP matrix tables in terminal text.
4. `Launch Interactive Bio-Sim? (y/n):` (Appears when `pygame` is installed) Enter `y` to open the 2D visualizer window.

---

## 15. GUI Controls

When the optional Pygame visualizer window is open:

| Key / Input | Action |
| :--- | :--- |
| **`T` Key** | Triggers DNA $\rightarrow$ mRNA Transcription visual sequence (glowing Uracil `U` nodes with particle bursts). |
| **`P` Key** | Triggers mRNA $\rightarrow$ Protein Translation visual sequence (amino acid node rendering). |
| **Mouse Scroll Up** | Zoom in canvas view. |
| **Mouse Scroll Down** | Zoom out canvas view. |
| **Left Click + Drag** | Pan canvas across world coordinates. |
| **Mouse Hover** | Displays base / amino acid label tooltips. |
| **Window Close (`X`)** | Exits GUI visualizer and returns to terminal prompt. |

---

## 16. Example Output

### Execution Sample

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

### Global Alignment Matrix Debugger (Developer Mode Terminal Text)
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

## 17. Understanding the Output

- **Genomic Metrics**: Displays sequence string length, GC-content percentage, and GC-density visual highlighting.
- **Transcription & Translation Box**: Shows template DNA, transcribed mRNA, and synthesized amino acid protein chain.
- **Global Alignment**: End-to-end sequence map using vertical bars (`|`) for matches, dots (`.`) for mismatches, and dashes (`-`) for gaps.
- **Local Alignment**: Displays conserved regional sub-segment matches.
- **Mutation Tracker**: Position-by-position log detailing specific mutation classifications.

---

## 18. DP Matrix Visualization

- **Grid Layout**: Rows represent Sequence 1 ($S_1$), columns represent Sequence 2 ($S_2$).
- **Cell Scores**: Each cell $(i, j)$ contains the alignment sub-problem score.
- **Highlighted Path**: Displays the traceback path selected by the algorithm.
- **Visual Tracer**: In the Pygame visualizer, an animated tracer dot (`lerp`) moves step-by-step backward along matrix coordinates to demonstrate backtracking.

---

## 19. Central Dogma Diagrammatic Flow

The application illustrates the standard educational sequence:

$$\text{DNA Template Strand} \xrightarrow{\text{Transcription (T } \rightarrow \text{ U)}} \text{mRNA Copy} \xrightarrow{\text{Translation (Codons)}} \text{Protein Chain}$$

1. **DNA**: Input template string (`ATGCGATCG...`).
2. **mRNA**: Transcribed messenger copy (`AUGCGAUCG...`).
3. **Protein**: Translated amino acid chain (`[Met][Arg][Ser]...`).

---

## 20. Mutation Analysis

Alignment differences are classified biologically:

- **Match (`|`)**: Nucleotides match.
- **Gap (`-`)**: Base insertion or deletion.
- **Transition Mutation**: Base substitution within the same chemical ring family ($A \leftrightarrow G$ or $C \leftrightarrow T$).
- **Transversion Mutation**: Base substitution across different chemical ring families ($A/G \leftrightarrow C/T$).

---

## 21. Graceful Degradation Architecture

The application handles missing optional dependencies via `try...except ImportError` blocks:

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
     Full CLI Dashboard Output         Full CLI Dashboard Output
                 +                                 +
     Optional 2D GUI Canvas            Terminal Matrix Output
```

---

## 22. Visual Design Language

The interface uses consistent color highlights across CLI ANSI output and 2D canvas graphics:
- **Green**: Sequence Matches.
- **Bright Red**: Transversion Mutations.
- **Dark Red**: Transition Mutations.
- **Yellow**: Insertions / Deletions (Gaps).
- **Magenta**: Uracil (`U`) bases & Transcription steps.
- **Orange**: Protein Amino Acid nodes.

---

## 23. Performance & Execution Constraints

- **GUI Frame Rate Target**: Capped at 60 FPS using `clock.tick(60)` when Pygame is active.
- **Adaptive Canvas**: Window scales between $1280 \times 720$ and $1600 \times 900$ pixels.
- **Memory Bounds**: Matrix size scales as $\mathcal{O}(n \cdot m)$.

---

## 24. Scope & Limitations

- **Educational Scale**: Intended for small teaching sequence strings ($\le 100$ bases). Not designed for megabase genomic assemblies.
- **Fixed Linear Scoring Parameters**: Uses fixed scoring parameters in code (`+1/-1/-1` for global, `+2/-1/-1` for local) rather than user-configurable substitution matrices (such as BLOSUM62 or PAM250).
- **Input Format**: Accepts raw nucleotide strings via interactive prompts; lacks FASTA/FASTQ file parsers or persistent database connectivity.
- **Diagrammatic Visuals**: Graphical elements (wiggling strands, particle bursts, sine-wave lines) are visual indicators, not molecular mechanics or thermodynamic simulations.

---

## 25. Future Scope

- Support for user-configurable substitution matrices (BLOSUM62 / PAM250).
- FASTA / FASTQ sequence file parsing.
- Multiple Sequence Alignment (MSA) using progressive alignment techniques.
- Alignment report export to HTML / PDF.

---

## 26. Educational & Academic Relevance

This project directly aligns with computer science coursework (*Design and Analysis of Algorithms* - MC507):
- **Dynamic Programming**: Practical application of sub-problem reuse and optimal substructure.
- **Backtracking**: Explicit path traversal through dynamic state tables.
- **String Processing**: String comparison, pattern matching, and dictionary translation lookups.

---

## 27. Expected Learning Outcomes

- Visual understanding of Needleman–Wunsch global alignment vs. Smith–Waterman local alignment.
- Step-by-step tracing of dynamic programming matrix backtracking.
- Practical demonstration of Central Dogma sequence processing mechanics.

---

## 28. Team

- **Parijat Chatterjee**
- **Komolika Dagare**
- **Shreyash Dahibhavkar**

---

## 29. Academic Information

- **Program**: First Year Master of Computer Applications (F.Y. MCA)
- **Semester**: Semester II (AY 2025–2026)
- **Course**: Design and Analysis of Algorithms
- **Course Code**: MC507

---

## 30. References

1. Needleman, S. B., & Wunsch, C. D. (1970). A general method applicable to the search for similarities in the amino acid sequence of two proteins. *Journal of Molecular Biology*, 48(3), 443-453.
2. Smith, T. F., & Waterman, M. S. (1981). Identification of common molecular subsequences. *Journal of Molecular Biology*, 147(1), 195-197.
3. Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms* (3rd ed.). MIT Press. (Chapter 15: Dynamic Programming).
4. Pygame Development Team. Pygame Documentation. https://www.pygame.org/docs/
