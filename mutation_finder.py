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
