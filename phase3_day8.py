CODON_TABLE = {
    "UUU": "Phenylalanine", "UUC": "Phenylalanine",
    "UUA": "Leucine",       "UUG": "Leucine",
    "UCU": "Serine",        "UCC": "Serine",
    "UCA": "Serine",        "UCG": "Serine",
    "UAU": "Tyrosine",      "UAC": "Tyrosine",
    "UAA": "Stop",          "UAG": "Stop",
    "UGU": "Cysteine",      "UGC": "Cysteine",
    "UGA": "Stop",          "UGG": "Tryptophan",
    "CUU": "Leucine",       "CUC": "Leucine",
    "CUA": "Leucine",       "CUG": "Leucine",
    "CCU": "Proline",       "CCC": "Proline",
    "CCA": "Proline",       "CCG": "Proline",
    "CAU": "Histidine",     "CAC": "Histidine",
    "CAA": "Glutamine",     "CAG": "Glutamine",
    "CGU": "Arginine",      "CGC": "Arginine",
    "CGA": "Arginine",      "CGG": "Arginine",
    "AUU": "Isoleucine",    "AUC": "Isoleucine",
    "AUA": "Isoleucine",    "AUG": "Methionine",
    "ACU": "Threonine",     "ACC": "Threonine",
    "ACA": "Threonine",     "ACG": "Threonine",
    "AAU": "Asparagine",    "AAC": "Asparagine",
    "AAA": "Lysine",        "AAG": "Lysine",
    "AGU": "Serine",        "AGC": "Serine",
    "AGA": "Arginine",      "AGG": "Arginine",
    "GUU": "Valine",        "GUC": "Valine",
    "GUA": "Valine",        "GUG": "Valine",
    "GCU": "Alanine",       "GCC": "Alanine",
    "GCA": "Alanine",       "GCG": "Alanine",
    "GAU": "Aspartate",     "GAC": "Aspartate",
    "GAA": "Glutamate",     "GAG": "Glutamate",
    "GGU": "Glycine",       "GGC": "Glycine",
    "GGA": "Glycine",       "GGG": "Glycine"
}


def find_all_orfs(rna_sequence):
    orfs = []
    i = 0
    while i < len(rna_sequence) - 2:
        if rna_sequence[i:i+3] == "AUG":
            protein = []
            for j in range(i, len(rna_sequence) - 2, 3):
                codon = rna_sequence[j:j+3]
                if len(codon) < 3:
                    break
                amino_acid = CODON_TABLE.get(codon, "Unknown")
                if amino_acid == "Stop":
                    orfs.append({
                        "start": i + 1,
                        "protein": protein
                    })
                    break
                protein.append(amino_acid)
        i += 1
    return orfs


def reverse_complement(dna):
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join(complement[base] for base in dna)[::-1]


def six_frame_scan(dna_sequence):
    results = {}
    rna_forward = dna_sequence.replace("T", "U")
    rev_comp = reverse_complement(dna_sequence)
    rna_reverse = rev_comp.replace("T", "U")

    for frame in range(3):
        frame_rna = rna_forward[frame:]
        orfs = find_all_orfs(frame_rna)
        results[f"Frame +{frame + 1}"] = orfs

    for frame in range(3):
        frame_rna = rna_reverse[frame:]
        orfs = find_all_orfs(frame_rna)
        results[f"Frame -{frame + 1}"] = orfs

    return results


hbb_dna = "ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACTGGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAA"

hbb_results = six_frame_scan(hbb_dna)

print("\nHBB Gene 6-Frame Scan:")
for frame, orfs in hbb_results.items():
    print(f"{frame}: {len(orfs)} ORFs found")
