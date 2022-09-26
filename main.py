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

def calc_diag_a(pos):
    x, y = pos
    return x - y

def calc_diag_b(pos):
    x, y = pos
    return y - x

from collections import defaultdict

diagonals_a = defaultdict(list) # from left top to right down
diagonals_b = defaultdict(list) # from left bottom to right top

for pos in canon:
    diag_a = calc_diag_a(pos)
    diag_b = calc_diag_b(pos)
    diagonals_a[diag_a].append(pos)
    diagonals_b[diag_b].append(pos)
    pass

def sort_diag(diag):
    diag.sort(key=lambda pos: pos[0]) # `lambda (x, y): x` is not valid syntax
    pass

for diag, vals in diagonals_a.items():
    if len(vals) < 2:
        continue
    sort_diag(vals)
    print(canon_ids[vals[0]], canon_ids[vals[1]])
    break
    pass
