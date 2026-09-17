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


sequences = read_fasta("/home/mayank/python_practice/sample.fasta")

for header, sequence in sequences.items():
    print(f"Header: {header}")
    print(f"Sequences: {sequence}")
    print(f"Length: {len(sequence)}")
    print("___")


def full_dna_report(filename):
    sequences = read_fasta(filename)
    results = []

    for header, sequence in sequences.items():
        sequence = sequence.upper()
        g = sequence.count("G")
        c = sequence.count("C")
        total = len(sequence)
        gc_content = (g + c) / total * 100

        report = {
            "header": header,
            "length": total,
            "gc_content": gc_content
        }
        results.append(report)

    return results


reports = full_dna_report("/home/mayank/python_practice/sample.fasta")

for report in reports:
    print(f"Header: {report['header']}")
    print(f"Length: {report['length']}")
    print(f"GC: {report['gc_content']}%")
    print("---")
