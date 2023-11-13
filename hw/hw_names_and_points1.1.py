names = ["Steve", "Alan", "Harry", "John"]
points = [66, 35, 68, 70]
for b, i in enumerate(names):
    for c, a in enumerate(points):
        if b == c:
            print(f"{b + 1}.{names[b]}-{points[c]}")