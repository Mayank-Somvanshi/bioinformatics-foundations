def find_mutations(original, mutated):
    mutations = []

    for i in range(len(original)):
        if original[i] != mutated[i]:
            mutation = {
                "position": i + 1,
                "original": original[i],
                "mutated": mutated[i]
            }
            mutations.append(mutation)

    return mutations


seq1 = "ATCGGCTA"
seq2 = "ATCGTCTA"

result = find_mutations(seq1, seq2)
print(f"Mutations found: {len(result)}")
for mutation in result:
    print(
        f"Position {mutation['position']}: {mutation['original']} → {mutation['mutated']}")
