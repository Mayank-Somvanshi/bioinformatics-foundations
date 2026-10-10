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
        complement_dict = {"A": "T", "T": "A", "C": "G", "G": "C"}
        rev_complement = "".join(
            complement_dict[base] for base in self.sequence)[::-1]
        return rev_complement

    def is_valid(self) -> bool:
        if self.length == 0:
            return False
        return set(self.sequence).issubset({"A", "T", "C", "G"})

    def find_motif(self, motif: str) -> list:
        motif = motif.upper()
        positions = []
        for i in range(len(self.sequence) - len(motif) + 1):
            # i forgot this whole line and peeked ( though since we would be doing 10 min. blank everyday this would be covered)
            if self.sequence[i:i + len(motif)] == motif:
                positions.append(i + 1)
        return positions

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
            preview = f"{self.sequence[:7]}..."  # peeked a little
        # and forgot this line as well
        return f"DNASequence('{preview}', len={self.length})"

    def translate(self) -> str:
        rna = self.transcribe()
        proteins = []
        for i in range(0, len(rna), 3):
            # i wrote len instead of rna here and rna instead of len in the next line changed after checking error by myself
            codon = rna[i:i+3]
            if len(codon) < 3:
                break
            amino_acid = CODON_TABLE.get(codon, "X")
            if amino_acid == "*":
                break
            # i wrote amino_acid.append(proteins) first {changed after checking error by myself }
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

    def six_frame_scan(self) -> dict:
        results = {}
        rev_seq = self.reverse_complement()
        for f in range(3):
            results[f + 1] = self._translate_frame(self.sequence, f)
            results[-(f + 1)] = self._translate_frame(rev_seq, f)
        return results

    def find_all_orfs(self) -> list:
        orfs = []
        stop_codons = ["TAA", "TAG", "TGA"]
        for i in range(len(self.sequence) - 2):
            if self.sequence[i:i+3] == "ATG":  # peeked this line
                for j in range(i, len(self.sequence) - 2, 3):
                    # had written [j:j+3] == stop_codons:
                    if self.sequence[j:j+3] in stop_codons:
                        orfs.append(self.sequence[i:j+3])
                        break
        return orfs

    def longest_orf(self) -> str:
        if self.length == 0:
            return ""
        if not self.is_valid():
            raise ValueError("Invalid DNASequence")
        forward = self.find_all_orfs()
        rev = DNASequence(self.reverse_complement())
        # first wrote  self.find_all_orfs() but then i thought it cant be self for rev so wrote rev
        reverse = rev.find_all_orfs()
        combined_list = forward + reverse
        if not combined_list:
            return ""
        return max(combined_list, key=len)  # haad to take a peek


def check(name, test):
    try:
        ok = test()
    except Exception as e:
        ok = False
    print("✅" if ok else "❌", name)


HBB = "ATGGTGCATCTGACTCCTGAGGAGAAG"
check("gc_content",
      lambda: DNASequence("GCGCAATT").gc_content() == 50.0
      and DNASequence("AAAA").gc_content() == 0.0
      and DNASequence("").gc_content() == 0.0
      and round(DNASequence(HBB).gc_content(), 2) == 51.85)
check("base_composition",
      lambda: DNASequence("AATGC").base_composition() == {
          "A": 2, "T": 1, "C": 1, "G": 1}
      and DNASequence(HBB).base_composition() == {"A": 7, "T": 6, "C": 5, "G": 9})
check("__repr__",
      lambda: repr(DNASequence("ATGC")) == "DNASequence('ATGC', len=4)"
      and repr(DNASequence(HBB)) == "DNASequence('ATGGTGC...', len=27)"
      and repr(DNASequence("ATGCATGCAT")) == "DNASequence('ATGCATGCAT', len=10)")
check("find_motif",
      lambda: DNASequence("ATGATG").find_motif("ATG") == [1, 4]
      and DNASequence("AAAA").find_motif("AA") == [1, 2, 3]
      and DNASequence("ATGC").find_motif("TTT") == []
      and DNASequence(HBB).find_motif("GAG") == [19, 22])
check("find_all_orfs",
      lambda: DNASequence("CCATGAAATTTGGGTAACC").find_all_orfs() == [
          "ATGAAATTTGGGTAA"]
      and DNASequence("ATGAAATT").find_all_orfs() == []
      and DNASequence("ATGAAAATGCCCTGA").find_all_orfs() == ["ATGAAAATGCCCTGA", "ATGCCCTGA"]
      and DNASequence("ATGTAGATGCCTAA").find_all_orfs() == ["ATGTAG"])
check("longest_orf",
      lambda: all(DNASequence(s).longest_orf() == e for s, e in [
          ("", ""), ("CCCCCC", ""), ("ATGAAACCC", ""), ("ATGTAA", "ATGTAA"),
          ("TTACCCAAATTTCAT", "ATGAAATTTGGGTAA"), ("atgtaa", "ATGTAA"),
          ("ATGAAAATGCCCTGA", "ATGAAAATGCCCTGA")]))


def raises():
    try:
        DNASequence("ATGNTAA").longest_orf()
        return False
    except ValueError:
        return True


check("longest_orf raises ValueError on invalid input", raises)
