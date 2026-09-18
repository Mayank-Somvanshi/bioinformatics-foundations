def is_valid_dna(sequence):
    for base in sequence:
        if base not in "ATCG":
            return False
    return True
