codon_table = {
    "ATG": "Methionine",
    "TAA": "Stop",
    "GCT": "Alanine",
    "CGT": "Arginine",
    "TTT": "Phenylalanine",
    "GGT": "Glycine"
}


def translate_codon(codon):
    if codon in codon_table:
        return codon_table[codon]
    else:
        return "Unknown codon"


print(translate_codon("ATG"))
print(translate_codon("GCT"))
print(translate_codon("XYZ"))


def translate_sequence(dna):
    dna = dna.upper().replace(" ", "")
    protein = []

    for i in range(0, len(dna), 3):
        codon = dna[i:i+3]
        amino_acid = translate_codon(codon)
        protein.append(amino_acid)

    return protein


dna = "ATGGCTCGT"
result = translate_sequence(dna)
print(f"Protein: {result}")

for codon, amino_acid in codon_table.items():
    print(f"{codon} → {amino_acid}")
