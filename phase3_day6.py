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


def translate(rna_sequence):
    protein = []

    start = rna_sequence.find("AUG")
    if start == -1:
        return "No Start Codon Found"

    for i in range(start, len(rna_sequence) - 2, 3):
        codon = rna_sequence[i:i+3]
        if len(codon) < 3:
            break
        amino_acid = CODON_TABLE.get(codon, "Unknown")
        if amino_acid == "Stop":
            break
        protein.append(amino_acid)

    return protein


dna = "ATGCATGGCTAA"
rna = dna.replace("T", "U")
print(f"DNA: {dna}")
print(f"RNA: {rna}")
print(f"Protein: {translate(rna)}")
