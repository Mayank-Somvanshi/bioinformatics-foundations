import matplotlib.pyplot as plt
import numpy as np


def gc_windows(seq, window_size, step):
    arr = np.array(list(seq))
    positions = []
    gc_values = []
    skew_values = []                                   # NEW
    for start in range(0, len(arr) - window_size + 1, step):
        window = arr[start:start + window_size]
        gc = ((window == "G") | (window == "C")).sum() / len(window) * 100
        g_count = (window == "G").sum()                # NEW
        c_count = (window == "C").sum()                # NEW
        skew = (g_count - c_count) / (g_count + c_count)   # NEW
        positions.append(start + window_size // 2)
        gc_values.append(float(gc))
        skew_values.append(float(skew))                # NEW
    return positions, gc_values, skew_values           # NEW: three lists now


seq = "ACATTTGCTTCTGACACAACTGTGTTCACTAGCAACCTCAAACAGACACCATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGCTAATGCCCTGGCCCACAAGTATCACTAAGCTCGCTTTCTTGCTGTCCAATTTCTATTAAAGGTTCCTTTGTTCCCTAAGTCCAACTACTAAACTGGGGGATATTATGAAGGGCCTTGAGCATCTGGATTCTGCCTAATAAAAAACATTTATTTTCATTGCAA"

positions, gc_values, skew_values = gc_windows(
    seq, 50, 25)   # NEW: three names
print(len(positions), gc_values[0], skew_values[0])

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.plot(positions, gc_values)
ax1.set_ylabel("GC content (%)")
ax1.set_title("HBB GC content and GC-skew, window 50, step 25")
ax2.plot(positions, skew_values)
ax2.axhline(0, color="gray", linewidth=0.8)
ax2.set_ylabel("GC-skew")
ax2.set_xlabel("Position in HBB (bases)")
plt.savefig("hbb_gc_skew.png")
