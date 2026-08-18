import time
import os
import re
import math

# --- ANSI Styling Fallback & Utilities ---
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.table import Table
    RICH_AVAILABLE = True
except ImportError:
    RICH_AVAILABLE = False

try:
    import pygame
    PYGAME_AVAILABLE = True
except ImportError:
    PYGAME_AVAILABLE = False

# ANSI Escape Sequences
CLEAR = "\033[H\033[J"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"

# Colors
GREEN = "\033[38;5;46m"      # Match
RED = "\033[38;5;196m"        # Transversion (Mismatch)
DIM_RED = "\033[38;5;88m"     # Transition (Mismatch)
YELLOW = "\033[38;5;226m"     # Gap
CYAN = "\033[38;5;51m"
MAGENTA = "\033[38;5;201m"
GC_BG = "\033[48;5;238m"      # GC Density background
PATH_BG = "\033[48;5;22m"     # DP Traceback path

def get_visible_len(s):
    """Calculates the visible length of a string, ignoring ANSI escape codes."""
    ansi_escape = re.compile(r'\x1b\[[0-9;]*m')
    return len(ansi_escape.sub('', s))

def pad_to_width(s, width):
    """Pads a string containing ANSI codes to a specific visible width."""
    return s + " " * (width - get_visible_len(s))

class Dna:
    def __init__(self):
        # Universal Genetic Code (mRNA Codons to Amino Acids)
        self.codon_table = {
            'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
            'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
            'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
            'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
            'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
            'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
            'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
            'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
            'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
            'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
            'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
            'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
            'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
            'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
            'UAC':'Y', 'UAU':'Y', 'UAA':'_', 'UAG':'_',
            'UGC':'C', 'UGU':'C', 'UGA':'_', 'UGG':'W',
        }
        self.aa_names = {
            'I': "Isoleucine", 'M': "Methionine (START)", 'T': "Threonine",
            'N': "Asparagine", 'K': "Lysine", 'S': "Serine", 'R': "Arginine",
            'L': "Leucine", 'P': "Proline", 'H': "Histidine", 'Q': "Glutamine",
            'A': "Alanine", 'D': "Aspartic Acid", 'E': "Glutamic Acid",
            'G': "Glycine", 'V': "Valine", 'F': "Phenylalanine", 'Y': "Tyrosine",
            'C': "Cysteine", 'W': "Tryptophan", '_': "STOP Codon"
        }
        self.aa_3letter = {
            'I': 'Ile', 'M': 'Met', 'T': 'Thr', 'N': 'Asn', 'K': 'Lys',
            'S': 'Ser', 'R': 'Arg', 'L': 'Leu', 'P': 'Pro', 'H': 'His',
            'Q': 'Gln', 'A': 'Ala', 'D': 'Asp', 'E': 'Glu', 'G': 'Gly',
            'V': 'Val', 'F': 'Phe', 'Y': 'Tyr', 'C': 'Cys', 'W': 'Trp',
            '_': 'STP', '?': '???'
        }

    def validate_dna(self, dna):
        valid_chars = set("ACGT")
        return dna and all(char in valid_chars for char in dna.upper())

    def get_gc_content(self, dna):
        if not dna: return 0.0
        gc_count = dna.upper().count('G') + dna.upper().count('C')
        return (gc_count / len(dna)) * 100

    def transcribe(self, dna):
        return dna.upper().replace('T', 'U')

    def translate(self, mrna):
        """Translates mRNA sequence into Protein (Amino Acids)."""
        protein = ""
        for i in range(0, len(mrna) - 2, 3):
            codon = mrna[i:i+3]
            aa = self.codon_table.get(codon, "?")
            protein += aa
        return protein

    def get_synthesis_viz(self, dna):
        """Creates a visual 12-character representation of DNA -> mRNA -> Protein."""
        segment = dna[:12].upper()
        mrna = segment.replace('T', 'U')
        protein = self.translate(mrna)
        
        # Highlight mRNA 'U' in Magenta
        mrna_viz = "".join([f"{MAGENTA}{BOLD}{c}{RESET}" if c == 'U' else f"{CYAN}{c}{RESET}" for c in mrna])
        # Format Protein as [Met][Gly][Leu]
        protein_viz = "".join([f"{GREEN}{BOLD}[{self.aa_3letter.get(aa, aa)}]{RESET}" for aa in protein])
        dna_viz = f"{BOLD}{segment}{RESET}"
        return dna_viz, mrna_viz, protein_viz

    def classify_mutation(self, base1, base2):
        purines = {'A', 'G'}
        pyrimidines = {'C', 'T'}
        b1, b2 = base1.upper(), base2.upper()
        if (b1 in purines and b2 in purines) or (b1 in pyrimidines and b2 in pyrimidines):
            return "Transition"
        return "Transversion"

    def edit_distance(self, dna1, dna2):
        if len(dna1) < len(dna2): dna1, dna2 = dna2, dna1
        n, m = len(dna1), len(dna2)
        prev_row = list(range(m + 1))
        for i in range(1, n + 1):
            curr_row = [i] + [0]*m
            for j in range(1, m + 1):
                if dna1[i-1] == dna2[j-1]: curr_row[j] = prev_row[j-1]
                else: curr_row[j] = 1 + min(prev_row[j], curr_row[j-1], prev_row[j-1])
            prev_row = curr_row
        return prev_row[m]

    def needleman_wunsch(self, dna1, dna2):
        n, m = len(dna1), len(dna2)
        match, mismatch, gap = 1, -1, -1
        score = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n + 1): score[i][0] = i * gap
        for j in range(m + 1): score[0][j] = j * gap
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s = match if dna1[i-1] == dna2[j-1] else mismatch
                score[i][j] = max(score[i-1][j-1] + s, score[i-1][j] + gap, score[i][j-1] + gap)
        
        align1, align2, path = "", "", []
        i, j = n, m
        path.append((i, j))
        while i > 0 or j > 0:
            s = match if (i > 0 and j > 0 and dna1[i-1] == dna2[j-1]) else mismatch
            if i > 0 and j > 0 and score[i][j] == score[i-1][j-1] + s:
                align1, align2 = dna1[i-1] + align1, dna2[j-1] + align2
                i, j = i-1, j-1
            elif i > 0 and score[i][j] == score[i-1][j] + gap:
                align1, align2 = dna1[i-1] + align1, "-" + align2
                i -= 1
            else:
                align1, align2 = "-" + align1, dna2[j-1] + align2
                j -= 1
            path.append((i, j))
        return align1, align2, score, path

    def smith_waterman(self, dna1, dna2):
        n, m = len(dna1), len(dna2)
        match, mismatch, gap = 2, -1, -1
        score = [[0] * (m + 1) for _ in range(n + 1)]
        max_score, max_pos = 0, (0, 0)
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                s = match if dna1[i-1] == dna2[j-1] else mismatch
                score[i][j] = max(0, score[i-1][j-1] + s, score[i-1][j] + gap, score[i][j-1] + gap)
                if score[i][j] >= max_score:
                    max_score, max_pos = score[i][j], (i, j)

        align1, align2, path = "", "", []
        i, j = max_pos
        path.append((i, j))
        while i > 0 and j > 0 and score[i][j] > 0:
            s = match if dna1[i-1] == dna2[j-1] else mismatch
            if score[i][j] == score[i-1][j-1] + s:
                align1, align2 = dna1[i-1] + align1, dna2[j-1] + align2
                i, j = i-1, j-1
            elif score[i][j] == score[i-1][j] + gap:
                align1, align2 = dna1[i-1] + align1, "-" + align2
                i -= 1
            else:
                align1, align2 = "-" + align1, dna2[j-1] + align2
                j -= 1
            path.append((i, j))
        return align1, align2, score, path

    def format_alignment(self, align1, align2):
        """Formats alignment with status line and plain-English mutation logs."""
        res1, res2, res_mid, m_log = "", "", "", []
        for i, (a, b) in enumerate(zip(align1, align2)):
            if a == b:
                res1 += f"{GREEN}{a}{RESET}"; res2 += f"{GREEN}{b}{RESET}"
                res_mid += "|"
            elif a == "-" or b == "-":
                res1 += f"{YELLOW}{a}{RESET}"; res2 += f"{YELLOW}{b}{RESET}"
                res_mid += " "
                source = "Sequence 2" if a == "-" else "Sequence 1"
                char = b if a == "-" else a
                m_log.append(f"[Pos {i+1}] {YELLOW}Gap (Missing Base):{RESET} Skips an instruction. Base '{char}' is absent in the target. (This is a deletion/insertion mutation).")
            else:
                m_type = self.classify_mutation(a, b)
                if m_type == "Transition":
                    color = DIM_RED
                    desc = f"Transition Mutation Detected ({a} -> {b}): A simple change between similar-shaped bases."
                else:
                    color = BOLD + RED
                    desc = f"Transversion Mutation Detected ({a} -> {b}): A chemically more difficult mutation."
                res1 += f"{color}{a}{RESET}"; res2 += f"{color}{b}{RESET}"
                res_mid += "."
                m_log.append(f"[Pos {i+1}] {color}Mismatch (Substitution):{RESET} Identifies when the instructions are different. Seq 1 has '{a}' but Seq 2 has '{b}'. ({desc})")
        return res1, res_mid, res2, m_log

    def highlight_density(self, seq):
        res = ""
        for char in seq:
            if char in "GC": res += f"{GC_BG}{BOLD}{char}{RESET}"
            else: res += char
        return res

def draw_dp_table(dna1, dna2, score, path, title):
    print(f"\n{BOLD}{CYAN} {title} Matrix Debugger {RESET}")
    print(f"{BOLD}Note: This table shows the score for every possible character pairing; the highlighted path is the 'Best Route' the computer found.{RESET}")
    w = 4  
    header_chars = ["-"] + list(dna2)
    header_line = " " * w + " | " + " | ".join([c.center(w) for c in header_chars]) + " |"
    print(header_line)
    print("-" * len(header_line))
    path_set = set(path)
    for i in range(len(score)):
        row_char = dna1[i-1] if i > 0 else "-"
        row_str = f"{row_char.center(w)} | "
        for j in range(len(score[0])):
            val_str = str(score[i][j]).center(w)
            if (i, j) in path_set: row_str += f"{PATH_BG}{val_str}{RESET} | "
            else: row_str += f"{val_str} | "
        print(row_str)
    print("-" * len(header_line))

def fake_progress(task):
    print(f"{CYAN}Calculating {task}...{RESET}")
    for i in range(1, 11):
        bar = "█" * i + "░" * (10-i)
        print(f"\r[{bar}] {i*10}%", end="", flush=True)
        time.sleep(0.05)
    print("\nDone.")

if PYGAME_AVAILABLE:
    class Particle:
        def __init__(self, x, y, color):
            self.x = x
            self.y = y
            # Simple pseudo-random velocity without random module
            t = time.time()
            self.vx = ((t * 1000) % 10 - 5) * 0.5
            self.vy = ((t * 500) % 10 - 5) * 0.5
            self.life = 1.0
            self.color = color

        def update(self):
            self.x += self.vx
            self.y += self.vy
            self.life -= 0.02
            return self.life > 0

    class DNAVisualizer:
        def __init__(self, s1, s2, score_matrix, path, dna_obj):
            pygame.init()
            # Dynamic Resolution with safety caps
            raw_w = (len(s2) * 35) + 600
            raw_h = (len(s1) * 35) + 200
            self.win_w = min(1600, max(1280, raw_w))
            self.win_h = min(900, max(720, raw_h))
            self.screen = pygame.display.set_mode((self.win_w, self.win_h))
            pygame.display.set_caption("Interactive Bio-Sim")
            self.clock = pygame.time.Clock()
            self.font = pygame.font.SysFont("monospace", 18, bold=True)
            self.header_font = pygame.font.SysFont("monospace", 28, bold=True)
            self.small_font = pygame.font.SysFont("monospace", 12)
            self.s1 = s1
            self.s2 = s2
            self.dna_obj = dna_obj
            self.score_matrix = score_matrix
            self.path = path  # List of (i, j) from bottom-right to top-left
            self.running = True
            
            # State Variables
            self.zoom_level = 1.0
            self.offset_x = 0
            self.offset_y = 0
            self.is_dragging = False
            self.last_mouse_pos = (0, 0)
            
            # Colors
            self.bg_color = (10, 10, 15)
            self.text_color = (220, 220, 220)
            self.strand_colors = {'A': (50, 200, 50), 'C': (50, 50, 200), 'G': (200, 200, 50), 'T': (200, 50, 50), 'U': (255, 0, 255)}
            self.matrix_color = (25, 25, 35)
            self.path_color = (0, 80, 0)
            self.tracer_color = (0, 255, 0)
            self.accent_color = (0, 200, 255)
            self.bond_color = (100, 200, 255)
            self.protein_color = (255, 150, 50)
            
            # Animation states
            self.transcribe_mode = False
            self.transcribe_idx = -1
            self.translate_mode = False
            self.translate_idx = -1
            
            self.s1_display = list(s1)
            self.s2_display = list(s2)
            self.p1_display = [] # Protein chain 1
            self.p2_display = [] # Protein chain 2
            
            self.tracer_idx = 0
            self.tracer_lerp = 0.0
            self.particles = []
            self.hovered_base = None 
            self.base_names = self.dna_obj.aa_names.copy()
            self.base_names.update({
                'A': "Adenine (Pairs with T)",
                'C': "Cytosine (Pairs with G)",
                'G': "Guanine (Pairs with C)",
                'T': "Thymine (Pairs with A)",
                'U': "Uracil (mRNA variant)"
            })

        def world_to_screen(self, x, y):
            return int(x * self.zoom_level + self.offset_x), int(y * self.zoom_level + self.offset_y)

        def screen_to_world(self, x, y):
            return (x - self.offset_x) / self.zoom_level, (y - self.offset_y) / self.zoom_level

        def get_base_y(self, i, ticks, strand_id, y_start, spacing):
            """Calculates the dynamic Y position of a base, including wiggle and codon gaps."""
            y_wiggle = math.cos(ticks * 0.001 + i * 0.5 + strand_id) * 8
            codon_gap = (i // 3) * 15 if self.translate_mode or self.translate_idx >= 0 else 0
            return y_start + i * spacing + codon_gap + y_wiggle

        def draw_strand(self, seq, x_base, y_start, spacing, ticks, strand_id, label):
            hx, hy = self.world_to_screen(x_base - 50, y_start - 50)
            header = self.font.render(label, True, self.accent_color)
            self.screen.blit(header, (hx, hy))
            mx, my = pygame.mouse.get_pos()
            wx, wy = self.screen_to_world(mx, my)

            for i, char in enumerate(seq):
                curr_wy = self.get_base_y(i, ticks, strand_id, y_start, spacing)
                wiggle = math.sin(ticks * 0.002 + i * 0.5 + strand_id) * 20
                curr_wx = x_base + wiggle
                sx, sy = self.world_to_screen(curr_wx, curr_wy)                
                
                dist = math.sqrt((wx - curr_wx)**2 + (wy - curr_wy)**2)
                is_hovered = dist < 20
                if is_hovered: self.hovered_base = (char, sx, sy)
                
                radius = int((16 if is_hovered else 12) * self.zoom_level)
                if radius < 1: radius = 1
                color = self.strand_colors.get(char, (150, 150, 150))
                
                if self.transcribe_mode and i <= self.transcribe_idx and char == 'U':
                    glow = int((20 + math.sin(ticks*0.01)*5) * self.zoom_level)
                    pygame.draw.circle(self.screen, (255, 0, 255), (sx, sy), glow, 2)
                
                pygame.draw.circle(self.screen, color, (sx, sy), radius)
                if self.zoom_level > 0.4:
                    text = self.font.render(char, True, (255, 255, 255))
                    self.screen.blit(text, (sx - 8 * self.zoom_level, sy - 10 * self.zoom_level))

        def draw_protein(self, protein, x_base, mrna_x_base, mrna_strand_id, y_start, spacing, ticks, strand_id, label):
            hx, hy = self.world_to_screen(x_base - 50, y_start - 50)
            header = self.font.render(label, True, self.protein_color)
            self.screen.blit(header, (hx, hy))
            mx, my = pygame.mouse.get_pos()
            wx, wy = self.screen_to_world(mx, my)

            for i, char in enumerate(protein):
                j = i # Codon index
                # Calculate the Y of the 3 mRNA bases dynamically
                y_coords = [self.get_base_y(3*j + b, ticks, mrna_strand_id, y_start, spacing) for b in range(3)]
                y_avg = sum(y_coords) / 3
                
                wiggle = math.sin(ticks * 0.001 + i * 0.8 + strand_id) * 10
                curr_wx, curr_wy = x_base + wiggle, y_avg
                sx, sy = self.world_to_screen(curr_wx, curr_wy)
                
                # Draw Brackets [ or ] connecting 3 bases to 1 protein
                bracket_color = (100, 100, 120)
                b_top_x, b_top_y = self.world_to_screen(mrna_x_base, y_coords[0])
                b_bot_x, b_bot_y = self.world_to_screen(mrna_x_base, y_coords[2])
                
                # Offset bracket horizontally based on side
                off = 40 * self.zoom_level if x_base > mrna_x_base else -40 * self.zoom_level
                
                # Vertical line of bracket
                pygame.draw.line(self.screen, bracket_color, (b_top_x + off, b_top_y), (b_bot_x + off, b_bot_y), 2)
                # Horizontal ticks
                pygame.draw.line(self.screen, bracket_color, (b_top_x + off, b_top_y), (b_top_x + off/2, b_top_y), 2)
                pygame.draw.line(self.screen, bracket_color, (b_bot_x + off, b_bot_y), (b_bot_x + off/2, b_bot_y), 2)
                # Pointer to protein
                pygame.draw.line(self.screen, bracket_color, (b_top_x + off, (b_top_y + b_bot_y)/2), (sx, sy), 2)

                dist = math.sqrt((wx - curr_wx)**2 + (wy - curr_wy)**2)
                is_hovered = dist < 25
                if is_hovered: self.hovered_base = (char, sx, sy)
                
                radius = int((25 if is_hovered else 20) * self.zoom_level)
                pygame.draw.circle(self.screen, self.protein_color, (sx, sy), radius)
                # Draw connections between amino acids
                if i > 0:
                    prev_y_coords = [self.get_base_y(3*(j-1) + b, ticks, mrna_strand_id, y_start, spacing) for b in range(3)]
                    prev_y_avg = sum(prev_y_coords) / 3
                    prev_wiggle = math.sin(ticks * 0.001 + (i-1) * 0.8 + strand_id) * 10
                    prev_sx, prev_sy = self.world_to_screen(x_base + prev_wiggle, prev_y_avg)
                    pygame.draw.line(self.screen, (200, 200, 200), (prev_sx, prev_sy), (sx, sy), 3)

                if self.zoom_level > 0.4:
                    aa_3 = self.dna_obj.aa_3letter.get(char, char)
                    text = self.font.render(aa_3, True, (0, 0, 0))
                    # Center the 3-letter text
                    self.screen.blit(text, (sx - 18 * self.zoom_level, sy - 10 * self.zoom_level))
        def draw_hydrogen_bonds(self, ticks, spacing, y_start, s1_x, s2_x):
            for i in range(min(len(self.s1_display), len(self.s2_display))):
                if self.s1_display[i] == self.s2_display[i]:
                    # Use get_base_y to match the dynamic wiggle and codon grouping
                    y1 = self.get_base_y(i, ticks, 0, y_start, spacing)
                    y2 = self.get_base_y(i, ticks, 10, y_start, spacing)
                    
                    # Match the wiggle from draw_strand
                    w1 = math.sin(ticks * 0.002 + i * 0.5 + 0) * 20
                    w2 = math.sin(ticks * 0.002 + i * 0.5 + 10) * 20
                    
                    p1 = self.world_to_screen(s1_x + w1, y1)
                    p2 = self.world_to_screen(s2_x + w2, y2)
                    vibrate = math.sin(ticks * 0.02 + i) * 3
                    pygame.draw.line(self.screen, self.bond_color, (p1[0], p1[1] + vibrate), (p2[0], p2[1] - vibrate), 2)

        def draw_matrix(self, x_offset, y_offset, cell_size, ticks):
            hx, hy = self.world_to_screen(x_offset, y_offset - 40)
            header = self.font.render("Scoring Matrix (Liquid Tracer)", True, self.accent_color)
            self.screen.blit(header, (hx, hy))
            rows, cols = len(self.score_matrix), len(self.score_matrix[0])
            path_set = set(self.path)
            scaled_cell = cell_size * self.zoom_level
            pulse = (math.sin(ticks * 0.005) + 1) / 2
            pulse_color = (0, int(150 * pulse + 50), 0)

            for i in range(rows):
                for j in range(cols):
                    wx, wy = x_offset + j * cell_size, y_offset + i * cell_size
                    sx, sy = self.world_to_screen(wx, wy)
                    rect = pygame.Rect(sx, sy, int(scaled_cell), int(scaled_cell))
                    color = pulse_color if (i, j) in path_set else self.matrix_color
                    pygame.draw.rect(self.screen, color, rect)
                    if scaled_cell > 22:
                        val = self.score_matrix[i][j]
                        self.screen.blit(self.small_font.render(str(val), True, (150, 150, 150)), (rect.x + 5, rect.y + 5))

            if len(self.path) > 1:
                p1, p2 = self.path[self.tracer_idx], self.path[(self.tracer_idx + 1) % len(self.path)]
                curr_i = p1[0] + (p2[0] - p1[0]) * self.tracer_lerp
                curr_j = p1[1] + (p2[1] - p1[1]) * self.tracer_lerp
                tsx, tsy = self.world_to_screen(x_offset + curr_j * cell_size, y_offset + curr_i * cell_size)
                pygame.draw.rect(self.screen, self.tracer_color, (tsx, tsy, int(scaled_cell), int(scaled_cell)), 3)

        def run(self):
            while self.running:
                ticks = pygame.time.get_ticks()
                self.hovered_base = None
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: self.running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 4: self.zoom_level += 0.1
                        elif event.button == 5: self.zoom_level = max(0.2, self.zoom_level - 0.1)
                        elif event.button == 1: self.is_dragging, self.last_mouse_pos = True, event.pos
                    if event.type == pygame.MOUSEBUTTONUP and event.button == 1: self.is_dragging = False
                    if event.type == pygame.MOUSEMOTION and self.is_dragging:
                        self.offset_x += event.pos[0] - self.last_mouse_pos[0]
                        self.offset_y += event.pos[1] - self.last_mouse_pos[1]
                        self.last_mouse_pos = event.pos
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_t: self.transcribe_mode, self.transcribe_idx = True, -1
                        if event.key == pygame.K_p: self.translate_mode, self.translate_idx = True, -1
                
                # Update Transcription
                if self.transcribe_mode:
                    old_idx = int(self.transcribe_idx)
                    self.transcribe_idx += 0.08
                    new_idx = int(self.transcribe_idx)
                    if new_idx > old_idx:
                        for s_idx, s_disp in [(0, self.s1_display), (1, self.s2_display)]:
                            if new_idx < len(s_disp) and s_disp[new_idx] == 'T':
                                s_disp[new_idx] = 'U'
                                sx, sy = self.world_to_screen(150 if s_idx == 0 else 350, 100 + new_idx * 30)
                                for _ in range(15): self.particles.append(Particle(sx, sy, (255, 0, 255)))
                    if self.transcribe_idx >= max(len(self.s1), len(self.s2)): self.transcribe_mode = False

                # Update Translation (Protein Synthesis)
                if self.translate_mode:
                    old_aa_idx = int(self.translate_idx)
                    self.translate_idx += 0.03
                    new_aa_idx = int(self.translate_idx)
                    if new_aa_idx > old_aa_idx:
                        # Translate codons from mRNA
                        for s_idx, s_disp, p_disp in [(0, self.s1_display, self.p1_display), (1, self.s2_display, self.p2_display)]:
                            codon_start = new_aa_idx * 3
                            if codon_start + 2 < len(s_disp):
                                codon = "".join(s_disp[codon_start:codon_start+3])
                                if all(c in "ACGU" for c in codon):
                                    aa = self.dna_obj.codon_table.get(codon, "?")
                                    p_disp.append(aa)
                                    sx, sy = self.world_to_screen(150 if s_idx == 0 else 350, 100 + codon_start * 30)
                                    for _ in range(20): self.particles.append(Particle(sx, sy, self.protein_color))
                    if self.translate_idx * 3 >= max(len(self.s1), len(self.s2)): self.translate_mode = False

                self.tracer_lerp += 0.05
                if self.tracer_lerp >= 1.0:
                    self.tracer_lerp = 0.0
                    self.tracer_idx = (self.tracer_idx + 1) % len(self.path)

                self.screen.fill(self.bg_color)
                # New Layout X-coordinates for better spacing
                p1_x, s1_x, s2_x, p2_x = 50, 200, 400, 550
                
                self.draw_hydrogen_bonds(ticks, 30, 100, s1_x, s2_x)
                
                self.draw_strand(self.s1_display, s1_x, 100, 30, ticks, 0, "Sequence 1 (mRNA)")
                self.draw_strand(self.s2_display, s2_x, 100, 30, ticks, 10, "Sequence 2 (mRNA)")
                
                # Draw proteins only for complete codons
                self.draw_protein(self.p1_display[:len(self.s1)//3], p1_x, s1_x, 0, 100, 30, ticks, 20, "Protein 1")
                self.draw_protein(self.p2_display[:len(self.s2)//3], p2_x, s2_x, 10, 100, 30, ticks, 30, "Protein 2")
                
                self.draw_matrix(700, 100, 30, ticks)
                
                self.particles = [p for p in self.particles if p.update()]
                for p in self.particles:
                    pygame.draw.circle(self.screen, p.color, (int(p.x), int(p.y)), int(3 * p.life))

                info_y, ui_cx = self.win_h - 135, self.win_w // 2
                titles = [
                    ("INTERACTIVE BIOLOGICAL SIMULATION", ui_cx - 300, 30, self.header_font, self.text_color),
                    ("Scroll: Zoom | Drag: Pan | 'T': Transcribe | 'P': Protein", ui_cx - 300, 70, self.font, self.accent_color),
                    ("Press 'P' to Translate (mRNA -> Protein)", 50, info_y, self.font, self.protein_color),
                    ("Glow Pulse: Optimal path identified by algorithm", 50, info_y + 25, self.font, (0, 255, 100)),
                    ("Protein (Orange): Amino Acid chain built from mRNA", 50, info_y + 50, self.font, self.protein_color),
                    ("Tracer: Liquid backtracking motion", 50, info_y + 85, self.font, self.tracer_color)
                ]
                for text, x, y, f, c in titles: self.screen.blit(f.render(text, True, c), (x, y))

                if self.hovered_base:
                    char, sx, sy = self.hovered_base
                    tip = self.font.render(f"[{char}] {self.base_names.get(char, 'Unknown')}", True, (255, 255, 255))
                    pygame.draw.rect(self.screen, (40, 40, 60), (sx + 20, sy - 10, tip.get_width() + 10, 30))
                    self.screen.blit(tip, (sx + 25, sy - 5))

                pygame.display.flip()
                self.clock.tick(60)
            pygame.quit()

def run_visualizer(dna_obj, s1, s2):
    if not PYGAME_AVAILABLE:
        print(f"\n{RED}Error: Pygame is not installed. Run 'pip install pygame' to use the visualizer.{RESET}")
        return
    
    # Get Needleman-Wunsch data
    _, _, score_matrix, path = dna_obj.needleman_wunsch(s1, s2)
    viz = DNAVisualizer(s1, s2, score_matrix, path, dna_obj)
    viz.run()

def display_dashboard(dna_obj, s1, s2, dev_mode):
    # Calculations
    fake_progress("Global Alignment (Total similarity)")
    ga_out = dna_obj.needleman_wunsch(s1, s2)
    ga1, ga_mid, ga2, g_log = dna_obj.format_alignment(ga_out[0], ga_out[1])
    g_score, g_path = ga_out[2], ga_out[3]

    fake_progress("Local Alignment (Regional similarity)")
    la_out = dna_obj.smith_waterman(s1, s2)
    la1, la_mid, la2, l_log = dna_obj.format_alignment(la_out[0], la_out[1])
    l_score, l_path = la_out[2], la_out[3]
    
    # Dashboard Assembly
    print(CLEAR)
    print(f"{BOLD}{MAGENTA}╔══════════════════════════════════════════════════════════════════════════════╗")
    print(f"║                   GENOMIC ANALYSIS DASHBOARD                                 ║")
    print(f"╚══════════════════════════════════════════════════════════════════════════════╝{RESET}")
    
    print(f"{BOLD}{CYAN}[ THE DNA WORKFLOW (CENTRAL DOGMA) ]{RESET}")
    print(f" DNA Blueprint (Source Code) stays protected. Transcription copies a segment,")
    print(f" replacing 'T' with 'U'. The mRNA (Portable Copy) then delivers instructions.\n")

    # Top Panel: Metrics & Transcription
    print(f"{BOLD}{CYAN}[ GENOMIC METRICS & TRANSCRIPTION ]{RESET}")
    box_w = 60 # Fixed width for the transcription box
    
    for i, s in enumerate([s1, s2], 1):
        gc = dna_obj.get_gc_content(s)
        density = dna_obj.highlight_density(s)
        dna_seg, mrna_seg, protein_seg = dna_obj.get_synthesis_viz(s)
        
        print(f" {BOLD}Sequence {i}:{RESET} Length: {len(s)} | GC-Density: {gc:.1f}% | Map: {density}")
        
        # Border Top
        print(f"   ┌" + "─" * (box_w - 6) + "┐")
        
        # Title Row
        title = f"   │ {BOLD}TRANSCRIPTION & TRANSLATION{RESET}"
        print(title + " " * (box_w - get_visible_len(title) - 1) + "│")
        
        # DNA Row
        dna_row = f"   │ {'Template DNA:':20} {dna_seg}"
        print(dna_row + " " * (box_w - get_visible_len(dna_row) - 1) + "│")
        
        # mRNA Row
        mrna_row = f"   │ {'Transcribed mRNA:':20} {mrna_seg}"
        print(mrna_row + " " * (box_w - get_visible_len(mrna_row) - 1) + "│")

        # Protein Row
        prot_row = f"   │ {'Resulting Protein:':20} {protein_seg}"
        print(prot_row + " " * (box_w - get_visible_len(prot_row) - 1) + "│")
        
        # Note Row
        note = f"   │ {MAGENTA}Note: U replaces T | Codons form Protein{RESET}"
        print(note + " " * (box_w - get_visible_len(note) - 1) + "│")
        
        # Border Bottom
        print(f"   └" + "─" * (box_w - 6) + "┘")
        print(f"   {MAGENTA}Tooltip: Watch the 'T' bases glow Magenta as they change to 'U'.{RESET}\n")
    
    # Middle Panel: Side-by-Side Comparison
    print(f"\n{BOLD}{CYAN}[ ALIGNMENT COMPARISON ]{RESET}")
    col_width = 45
    print(f"{UNDERLINE}{pad_to_width('GLOBAL (Big Picture Comparison)', col_width)} | {'LOCAL (Pattern Hunter)':<40}{RESET}")
    print(f"{pad_to_width(ga1, col_width)} | {la1}")
    print(f"{pad_to_width(ga_mid, col_width)} | {la_mid}")
    print(f"{pad_to_width(ga2, col_width)} | {la2}")
    
    # Bottom Panel: Mutation Log
    print(f"\n{BOLD}{CYAN}[ MUTATION TRACKER ]{RESET}")
    log = g_log[:4]
    if not log:
        print("No mismatches or gaps found. The sequences are perfectly identical.")
    else:
        for m in log: print(f" • {m}")
        if len(g_log) > 4: print(f" ... and {len(g_log)-4} more differences detected.")

    # Glossary/Legend Panel
    print(f"\n{BOLD}{CYAN}╔════════════════════════════ [ INTERACTIVE BIOLOGICAL KEY ] ══════════════════════════╗")
    print(f"║ {GREEN}■{RESET} Match: Perfect match | {RED}■{RESET} Mismatch: Bases differ | {YELLOW}■{RESET} Gap: Base missing in one seq    ║")
    print(f"║ {BOLD}Global:{RESET} Big Picture Comparison: End-to-End map of evolutionary cousins.              ║")
    print(f"║ {BOLD}Local:{RESET} Pattern Hunter: Pinpoints the hidden matching 'island'.                        ║")
    print(f"║ {BOLD}Tracer:{RESET} Simulates Backtracking: walking backward to find the 'Optimal Path'.           ║")
    print(f"╚════════════════════════════════════════════════════════════════════════════════════════╝{RESET}")
    
    if dev_mode:
        draw_dp_table(s1, s2, g_score, g_path, "Global")
        draw_dp_table(s1, s2, l_score, l_path, "Local")

def main():
    dna_obj = Dna()
    print(CLEAR)
    print(f"{BOLD}{CYAN}DNA Analysis Input Interface{RESET}")
    s1 = input("Sequence 1: ").upper().strip()
    s2 = input("Sequence 2: ").upper().strip()
    dev = input("Enable Developer Mode? (y/n): ").lower() == 'y'
    if not dna_obj.validate_dna(s1) or not dna_obj.validate_dna(s2):
        print(f"{RED}Invalid DNA sequence. Use A, C, G, T only.{RESET}")
        return
    display_dashboard(dna_obj, s1, s2, dev)
    
    if PYGAME_AVAILABLE:
        choice = input("\nLaunch Interactive Bio-Sim? (y/n): ").lower()
        if choice == 'y':
            run_visualizer(dna_obj, s1, s2)
    else:
        print(f"\n{YELLOW}Pygame not detected. Skipping Simulation Mode.{RESET}")

if __name__ == "__main__":
    main()
