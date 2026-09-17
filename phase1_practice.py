def filter_by_gc(sequences, min_gc):
    result = []
    for sequence in sequences:
        g = sequence.count("G")
        c = sequence.count("C")
        total = len(sequence)
        gc_content = (g + c) / total * 100
        if gc_content >= min_gc:
            result.append(sequence)
    return result


sequences = ["ATCG", "GCTAGCTA", "TTAAGGCC", "AAAATTTT"]
filtered = filter_by_gc(sequences, 50)
print(f"Sequences with GC >= 50%: {filtered}")
