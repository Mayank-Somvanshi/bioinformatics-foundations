import pandas as pd
reads = {"sample": ["S1", "S2", "S3"], "reads": [1200, 800, 1500]}
df = pd.DataFrame(reads)
print(df)
# it prints:
#    sample  reads
# 0     S1   1200
# 1     S2    800
# 2     S3   1500
# The {...} is a dictionary. Each key ("sample", "reads") becomes a column name, and each list becomes that column’s values.
# pd.DataFrame(reads) turns the dictionary into a table.
# The numbers 0, 1, 2 on the left are row labels, which Pandas adds automatically.
