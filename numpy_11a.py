import numpy as np
primer = "ATGCGCTA"
arr = np.array(list(primer))
print(arr)
print(arr == "G")
print((arr == "G").sum())
gc_mask = (arr == "G") | (arr == "C")
print(gc_mask)
print(gc_mask.sum())
