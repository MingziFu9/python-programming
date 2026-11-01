words = "包子 很 香 老板 包子 香 包子".split()
counts = {}
for w in words:
    if w == "很":
        continue
    counts[w] = counts.get(w, 0) + 1
print(counts)
