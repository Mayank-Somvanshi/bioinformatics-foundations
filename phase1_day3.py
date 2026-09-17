def analyze_sequence(dna):
    dna = dna.upper().replace(" ", "")
    length = len(dna)

    if length == 0:
        return "Error: empty sequence"
    elif length < 10:
        return "Short sequence"
    elif length < 50:
        return "Medium sequence"
    else:
        return "Long sequence"


def full_analysis(dna):
    dna = dna.upper().replace(" ", "")

    for base in dna:
        if base not in "ACTG":
            print("Invalid sequence")
            return

    length = len(dna)
    g = dna.count("G")
    c = dna.count("C")
    gc_content = (g + c) / length * 100

    print(f"Length: {length}")
    print(f"GC Content: {gc_content}%")
    print(analyze_sequence(dna))


sequence = input("Enter DNA sequence")
full_analysis(sequence)
