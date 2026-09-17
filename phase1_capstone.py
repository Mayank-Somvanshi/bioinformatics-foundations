def read_fasta(filename):
    sequences = {}
    current_header = ""
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_header = line[1:]
                sequences[current_header] = ""
            else:
                sequences[current_header] += line
    return sequences


def is_valid_dna(sequence):
    for base in sequence:
        if base not in "ATCG":
            return False
    return True


def calculate_gc(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    return (g + c) / len(sequence) * 100


def find_longest(sequences):
    longest_header = ""
    longest_seq = ""
    for header, sequence in sequences.items():
        if len(sequence) > len(longest_seq):
            longest_seq = sequence
            longest_header = header
    return longest_header, longest_seq


def analyze_fasta(filename):
    sequences = read_fasta(filename)
    print(f"Total sequences found: {len(sequences)}")
    print("=" * 40)

    for header, sequence in sequences.items():
        sequence = sequence.upper()
        print(f"Header: {header}")

        if not is_valid_dna(sequence):
            print("Status: INVALID sequence")
            print("___")
            continue

        gc = calculate_gc(sequence)
        print(f"Length: {len(sequence)} bases")
        print(f"GC Content: {gc:.2f}%")
        print("Status: VALID")
        print("___")

    longest_header, longest_seq = find_longest(sequences)
    print(f"Longest sequence: {longest_header}")
    print(f"Length: {len(longest_seq)} bases")


analyze_fasta("/home/mayank/python_practice/sample.fasta")
