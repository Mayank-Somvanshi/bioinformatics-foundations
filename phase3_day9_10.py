import itertools
_bases = "UCAG"
_aa = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODON_TABLE = {a+b+c: _aa[i]
               for i, (a, b, c) in enumerate(itertools.product(_bases, repeat=3))}


class DNASequence:
    def __init__(self, sequence: str):
        self.sequence = sequence.upper()
        self.length = len(self.sequence)

    def __repr__(self) -> str:
        preview = (
            self.sequence
            if self.length <= 10
            else f"{self.sequence[:7]}..."
        )
        return f"DNASequence('{preview}', len={self.length})"

    def is_valid(self) -> bool:
        if self.length == 0:
            return False
        return set(self.sequence).issubset({"A", "T", "C", "G"})

    def gc_content(self) -> float:
        if self.length == 0:
            return 0.0
        g = self.sequence.count("G")
        c = self.sequence.count("C")
        return ((g + c) / self.length) * 100

    def transcribe(self) -> str:
        return self.sequence.replace("T", "U")

    def reverse_complement(self) -> str:
        complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
        comp_seq = "".join(complement[base] for base in self.sequence)
        return comp_seq[::-1]

    def find_motif(self, motif: str) -> list:
        motif = motif.upper()
        positions = []
        for i in range(len(self.sequence) - len(motif) + 1):
            if self.sequence[i:i+len(motif)] == motif:
                positions.append(i + 1)
        return positions

    def base_composition(self) -> dict:
        return {
            "A": self.sequence.count("A"),
            "T": self.sequence.count("T"),
            "C": self.sequence.count("C"),
            "G": self.sequence.count("G")
        }

    def translate(self) -> str:
        rna = self.transcribe()
        protein = []

        for i in range(0, len(rna), 3):
            codon = rna[i:i+3]
            if len(codon) < 3:
                break

            amino_acid = CODON_TABLE.get(codon, "X")

            if amino_acid == "*":
                break

            protein.append(amino_acid)

        return "".join(protein)

    def find_all_orfs(self) -> list:
        orfs = []
        stop_codons = ["TAA", "TAG", "TGA"]

        for i in range(len(self.sequence) - 2):
            if self.sequence[i:i+3] == "ATG":

                for j in range(i, len(self.sequence) - 2, 3):
                    codon = self.sequence[j:j+3]

                    if codon in stop_codons:
                        orf_sequence = self.sequence[i:j+3]
                        orfs.append(orf_sequence)
                        break

        return orfs

    def _translate_frame(self, seq: str, frame: int) -> str:
        protein = []
        rna = seq.replace("T", "U")

        for i in range(frame, len(rna) - 2, 3):
            codon = rna[i:i+3]
            amino_acid = CODON_TABLE.get(codon, "X")
            protein.append(amino_acid)

        return "".join(protein)

    def six_frame_scan(self) -> dict:
        frames = {}
        rev_seq = self.reverse_complement()

        for f in range(3):
            frames[f + 1] = self._translate_frame(self.sequence, f)
            frames[-(f + 1)] = self._translate_frame(rev_seq, f)

        return frames

    def longest_orf(self) -> str:
        if self.length == 0:
            return ""
        if not self.is_valid():
            raise ValueError("Invalid DNA sequence")

        forward = self.find_all_orfs()
        rev = DNASequence(self.reverse_complement())
        reverse = rev.find_all_orfs()
        all_orfs = forward + reverse

        if not all_orfs:
            return ""
        return max(all_orfs, key=len)


if __name__ == "__main__":
    tests = [
        ("",                 ""),
        ("CCCCCC",           ""),
        ("ATGAAACCC",        ""),
        ("ATGTAA",           "ATGTAA"),
        ("TTACCCAAATTTCAT",  "ATGAAATTTGGGTAA"),
        ("atgtaa",           "ATGTAA"),
        ("ATGAAAATGCCCTGA",  "ATGAAAATGCCCTGA"),
    ]

    for seq, expected in tests:
        got = DNASequence(seq).longest_orf()
        print("✅" if got == expected else "❌", repr(seq), "->", repr(got))

    try:
        DNASequence("ATGNTAA").longest_orf()
        print("❌ should have raised ValueError")
    except ValueError:
        print("✅ invalid input raises ValueError")

    expected_frames = {1: "P*NLGN", 2: "HEIWVT",
                       3: "MKFG*", -1: "GYPNFM", -2: "VTQISW", -3: "LPKFH"}
    got_frames = DNASequence("CCATGAAATTTGGGTAACC").six_frame_scan()
    print("✅" if got_frames == expected_frames else "❌",
          "six_frame_scan checkpoint")
