import numpy as np
quals = np.array([32, 18, 40, 9, 35])
print(quals)
mask = quals >= 20
print(mask)
print(quals[mask])
print(mask.sum())
print(mask.astype(int))
print(mask.astype(int).sum())
