import numpy as np
import pandas as pd


def gc_windows(seq, window_size, step):
    arr = np.array(list(seq))
    positions = []
    gc_values = []
    skew_values = []
    for start in range(0, len(arr) - window_size + 1, step):
        window = arr[start:start + window_size]
        gc = ((window == "G") | (window == "C")).sum() / len(window) * 100
        g_count = (window == "G").sum()
        c_count = (window == "C").sum()
        skew = (g_count - c_count) / (g_count + c_count)
        positions.append(start + window_size // 2)
        gc_values.append(float(gc))
        skew_values.append(float(skew))
    return positions, gc_values, skew_values


seq = "ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACTGGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAA"

positions, gc_values, skew_values = gc_windows(seq, 50, 25)
df = pd.DataFrame({"position": positions, "gc": gc_values})
print(df.head())
print(df.shape)
# df.head() shows the first 5 rows. It’s how you peek at a table without printing all of it.
# df.shape gives (rows, columns), like arr.shape did for arrays.
