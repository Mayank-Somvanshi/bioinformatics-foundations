def count_bases(dna):
    a = dna.count("A")
    t = dna.count("T")
    c = dna.count("C")
    g = dna.count("G")
    print(f"A: {a}")
    print(f"T: {t}")
    print(f"C: {c}")
    print(f"G: {g}")
    total = len(dna)
    total = len(dna)
    gc_content = (g + c) / total * 100
    print(f"GC Content: {gc_content}%")


count_bases("ATCGGCTA")
