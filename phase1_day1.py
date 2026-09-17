def calculate_gc_content(dna):
    g = dna.count("G")
    c = dna.count("C")
    total = len(dna)
    gc_content = (g + c) / total * 100
    return gc_content


dna_sequence = "ATCGGCTAGCTAGCTA"
result = calculate_gc_content(dna_sequence)
print(f"GC Content: {result}%")


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
