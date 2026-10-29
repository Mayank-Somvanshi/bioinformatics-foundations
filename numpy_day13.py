# Stage 1: how range makes window starts

import numpy as np
seq = "ATGGCGTAACGT"
for start in range(0, 12, 4):
    window = seq[start:start + 4]
    print(start, window)
# 0 ATGG
# 4 CGTA
# 8 ACGT

# Stage 2: GC% per window, stored in a list (short sequence)

seq = "ATGGCGCCAATT"
arr = np.array(list(seq))
results = []
for start in range(0, 12, 4):
    window = arr[start:start + 4]
    gc = ((window == "G") | (window == "C")).sum() / len(window) * 100
    results.append(float(gc))
print(results)   # [50.0, 100.0, 0.0]

# Stage 2a: GC% per window, printed directly (no list)

seq = "ATGGCGCCAATT"
arr = np.array(list(seq))
for start in range(0, 12, 4):
    window = arr[start:start + 4]
    gc = ((window == "G") | (window == "C")).sum() / len(window) * 100
    print(start, gc)
# 0 50.0
# 4 100.0
# 8 0.0

# Stage 3: the same loop on HBB, with labels

seq = "ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACTGGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAA"
arr = np.array(list(seq))
print(arr.shape)
results = []
for start in range(0, len(arr), 50):
    window = arr[start:start + 50]
    gc = ((window == "G") | (window == "C")).sum() / len(window) * 100
    results.append(float(gc))
    print(f"Bases {start + 1}-{start + len(window)}: {gc:.2f}%")
print(results)
# (628,)
# Bases: 601 - 628: 14.29%
