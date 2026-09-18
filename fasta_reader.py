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
