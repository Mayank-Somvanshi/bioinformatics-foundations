def clean_sequence(dna):
    dna = dna.upper()
    dna = dna.replace(" ", "")
    return dna


def is_valid_dna(dna):
    for base in dna:
        if base not in "ATCG":
            return False
    return True


sequence = input("Enter a DNA sequence: ")
cleaned = clean_sequence(sequence)

if is_valid_dna(cleaned):
    print(f"Valid sequence : {cleaned}")
    print(f"Length: {len(cleaned)}")
else:
    print("Invalid sequence - contains non-DNA characters")
