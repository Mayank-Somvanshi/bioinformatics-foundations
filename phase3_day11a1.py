import itertools
_bases = "UCAG"
_aa = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODON_TABLE = {a+b+c: _aa[i]
               for i, (a, b, c) in enumerate(itertools.product(_bases, repeat=3))}


class DNASequence:
    def __init__(self, sequence: str):
        self.sequence = sequence.upper()
        self.length = len(self.sequence)

    def transcribe(self) -> str:
        return self.sequence.replace("T", "U")

    def reverse_complement(self) -> str:
        complement_dict = {"A": "T", "T": "A", "G": "C", "C": "G"}
        rev_complement = "".join(
            complement_dict[base]for base in self.sequence)[::-1]
        return rev_complement

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

    def base_composition(self) -> dict:
        return {
            "A": self.sequence.count("A"),
            "T": self.sequence.count("T"),
            "C": self.sequence.count("C"),
            "G": self.sequence.count("G"),
        }

    def __repr__(self) -> str:
        if self.length <= 10:
            preview = self.sequence
        else:
            preview = f"{self.sequence[:7]}..."
        return f"DNASequence('{preview}', len={self.length})"

    def find_motif(self, motif: str) -> list:
        motif = motif.upper()
        positions = []
        for i in range(len(self.sequence) - len(motif) + 1):
            if self.sequence[i:i+len(motif)] == motif:
                positions.append(i + 1)
        return positions

    def translate(self) -> str:
        rna = self.transcribe()
        proteins = []

        for i in range(0, len(rna), 3):
            codon = rna[i:i+3]
            if len(codon) < 3:
                break

            amino_acid = CODON_TABLE.get(codon, "X")
            if amino_acid == "*":
                break
            proteins.append(amino_acid)

        return "".join(proteins)

    def _translate_frame(self, seq: str, frame: int) -> str:
        rna = seq.replace("T", "U")
        proteins = []
        for i in range(frame, len(rna) - 2, 3):
            codon = rna[i:i+3]
            amino_acid = CODON_TABLE.get(codon, "X")
            proteins.append(amino_acid)
        return "".join(proteins)

    def find_all_orfs(self) -> list:
        orfs = []
        stop_codons = ["TAA", "TAG", "TGA"]
        for i in range(len(self.sequence) - 2):
            if self.sequence[i:i+3] == "ATG":
                for j in range(i, len(self.sequence) - 2, 3):
                    if self.sequence[j:j+3] in stop_codons:
                        orfs.append(self.sequence[i:j+3])
                        break
        return orfs

    def six_frame_scan(self) -> dict:
        results = {}
        rev_seq = self.reverse_complement()
        for f in range(3):
            results[f + 1] = self._translate_frame(self.sequence, f)
            results[-(f + 1)] = self._translate_frame(rev_seq, f)
        return results

    def longest_orf(self) -> str:
        if self.length == 0:
            return ""
        if not self.is_valid():
            raise ValueError("Invalid DNA sequence")
        forward = self.find_all_orfs()
        rev = DNASequence(self.reverse_complement())
        reverse = rev.find_all_orfs()
        combined_list = forward + reverse
        if not combined_list:
            return ""
        return max(combined_list, key=len)


HBB = "ATGGTGCATCTGACTCCTGAGGAGAAG"   # start of the human HBB gene
d = DNASequence(HBB)

print(d)                                       # __init__ + __repr__
print("valid:", d.is_valid())                  # is_valid
print("GC%:", round(d.gc_content(), 2))        # gc_content
print("bases:", d.base_composition())          # base_composition
print("RNA:", d.transcribe())                  # transcribe
print("rev comp:", d.reverse_complement())     # reverse_complement
print("motif GAG at:", d.find_motif("GAG"))    # find_motif
print("protein:", d.translate())               # translate

demo = DNASequence("CCATGAAATTTGGGTAACC")
print("ORFs:", demo.find_all_orfs())           # find_all_orfs
print("longest ORF:", demo.longest_orf())      # longest_orf

# six_frame_scan + _translate_frame
frames = demo.six_frame_scan()
for label in [1, 2, 3, -1, -2, -3]:
    print("frame", label, frames[label])
