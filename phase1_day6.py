codon_table = {
    "ATG": "Methionine (Start)",
    "TAA": "Stop",
    "TAG": "Stop",
    "TGA": "Stop",
    "GCT": "Alanine",
    "CGT": "Arginine"
}

print(codon_table["ATG"])
print(codon_table["TAA"])
print(f"Total codons: {len(codon_table)}")
