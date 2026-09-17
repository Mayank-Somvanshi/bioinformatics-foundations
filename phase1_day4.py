sequences = ["ATCG", "GCTAGCTA", "TTAAGGCC", "ATCGATCGATCG"]

print(f"Total sequences: {len(sequences)}")
print(f"First sequence: {sequences[0]}")
print(f"Last sequence: {sequences[-1]}")

for sequence in sequences:
    g = sequence.count("G")
    c = sequence.count("C")
    total = len(sequence)
    gc = (g + c) / total * 100
    print(f"{sequence}, GC: {gc}%")


def longest_sequence(sequences):
    longest = sequences[0]
    for sequence in sequences:
        if len(sequence) > len(longest):
            longest = sequence
    return longest


print(f"Longest sequence: {longest_sequence(sequences)}")
