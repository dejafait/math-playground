"""Exact algebra/injectivity regression for L164, not an asymptotic test."""
from itertools import product
from math import gcd, prod

boxes = 0
for a, b, c, d in product(range(-3, 4), repeat=4):
    rows = ((a, b, -a-b), (c, d, -c-d), (-a-c, -b-d, a+b+c+d))
    assert all(sum(row) == 0 for row in rows)
    assert all(sum(rows[i][j] for i in range(3)) == 0 for j in range(3))
    assert max(abs(x) for row in rows for x in row) <= 12
    boxes += 1

seen = {}
checked = 0
for cells in product((1, 2, 3), repeat=9):
    if any(gcd(cells[i], cells[j]) != 1 for i in range(9) for j in range(i)):
        continue
    rows = tuple(prod(cells[3*i:3*i+3]) for i in range(3))
    cols = tuple(prod(cells[3*i+j] for i in range(3)) for j in range(3))
    assert prod(rows) == prod(cols)
    assert tuple(gcd(rows[i], cols[j]) for i in range(3) for j in range(3)) == cells
    key = rows + cols
    assert key not in seen or seen[key] == cells
    seen[key] = cells
    checked += 1

# A prime-power example checks recovery beyond squarefree entries.
cells = (4, 27, 25, 49, 121, 169, 289, 361, 529)
rows = tuple(prod(cells[3*i:3*i+3]) for i in range(3))
cols = tuple(prod(cells[3*i+j] for i in range(3)) for j in range(3))
assert tuple(gcd(rows[i], cols[j]) for i in range(3) for j in range(3)) == cells
print(f'Passed {boxes} displacement identities and {checked + 1} coprime margin recoveries.')
