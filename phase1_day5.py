sequences = ["ATCG", "GCTAGCTA", "TTAAGGCC"]

print(f"Original: {sequences}")

sequences.append("ATCGATCGATCG")
print(f"After append: {sequences}")

sequences.remove("TTAAGGCC")
print(f"After remove: {sequences}")

sequences.sort()
print(f"After sort: {sequences}")

print(f"Total sequences: {len(sequences)}")


def filter_by_length(sequences, min_length):
    result = []
    for sequence in sequences:
        if len(sequence) >= min_length:
            result.append(sequence)
    return result


filtered = filter_by_length(sequences, 8)
print(f"Sequences >= 8 bases: {filtered}")
