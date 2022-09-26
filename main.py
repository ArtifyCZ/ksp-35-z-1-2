# https://ksp.mff.cuni.cz/z/ulohy/35/zadani1.html#task-35-Z1-2

w, h, n = map(int, input().split(" "))

canon_ids = dict()
canon = [(0, 0)] * n

for i in range(0, n):
    x, y = map(int, input().split(" "))
    canon[i] = x, y
    canon_ids[(x, y)] = i
    pass

def is_on_same_diagonal(a, b):
    a_x, a_y = a
    b_x, b_y = b
    x = abs(a_x - b_x)
    y = abs(a_y - b_y)
    return x == y

def on_left(a, b):
    a_x, a_y = a
    b_x, b_y = b
    if a_x < b_x:
        return a
    return b

def on_right(a, b):
    a_x, a_y = a
    b_x, b_y = b
    if a_x >= b_x:
        return a
    return b

def is_between(a, b, c):
    a_x, a_y = a
    b_x, b_y = b
    c_x, c_y = c
    a = on_left(a, b)
    b = on_right(a, b)
    return (c == on_right(a, c)) and (c == on_left(b, c))

# This set does not contain every combination, but some of them.
on_same_diagonal = set()
for i in canon:
    for j in canon:
        if i is j:
            continue
        if (i, j) in on_same_diagonal or (j, i) in on_same_diagonal:
            continue
        if is_on_same_diagonal(i, j):
            on_same_diagonal.add((i, j))
            pass
        pass
    pass

for (a, b) in on_same_diagonal.copy():
    for (c, d) in on_same_diagonal.copy():
        if is_between(a, b, c):
            on_same_diagonal.remove((a, b))
            on_same_diagonal.add((a, c))
            break
        pass
    continue

for (a, b) in on_same_diagonal:
    a = canon_ids[a]
    b = canon_ids[b]
    print(f"{a} {b}")
    break
