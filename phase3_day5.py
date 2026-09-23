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


hbb_sequence = """ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACTGGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAA""".replace(
    "\n", "").replace(" ", "")
dna = DNASequence(hbb_sequence)
print(dna)
print(f"Valid: {dna.is_valid()}")
print(f"Length: {dna.length}")
print(f"GC Content: {dna.gc_content():.2f}%")
print(f"ATG motif positions: {dna.find_motif('ATG')}")
print(f"Base composition: {dna.base_composition()}")
