"""Supplementary complete incidence and graph check for L087."""
import json
from collections import Counter
from itertools import combinations
from pathlib import Path


def inspect(vertices, blocks):
    pairs = Counter(pair for block in blocks for pair in combinations(sorted(block), 2))
    degrees = Counter(x for block in blocks for x in block)
    intersections = [
        {"blocks": [i, j], "intersection": sorted(set(blocks[i]) & set(blocks[j]))}
        for i, j in combinations(range(len(blocks)), 2)
    ]
    edges = [list(pair) for pair in combinations(vertices, 2) if not pairs[pair]]
    adjacency = {x: set() for x in vertices}
    for x, y in edges:
        adjacency[x].add(y)
        adjacency[y].add(x)
    unseen = set(vertices)
    components = []
    while unseen:
        stack = [min(unseen)]
        component = set()
        while stack:
            x = stack.pop()
            if x in component:
                continue
            component.add(x)
            stack.extend(adjacency[x] - component)
        unseen -= component
        components.append(sorted(component))
    failures = []
    if len(blocks) != 16 or len({tuple(sorted(b)) for b in blocks}) != 16:
        failures.append("Not sixteen distinct blocks")
    if any(len(set(b)) != 4 for b in blocks):
        failures.append("Block size differs from four")
    if any(degrees[x] != 4 for x in vertices):
        failures.append("Vertex degree differs from four")
    if any(len(row["intersection"]) > 1 for row in intersections):
        failures.append("Nonlinear block pair")
    return {
        "blocks": blocks, "degrees": dict(degrees),
        "block_intersections": intersections,
        "pair_multiplicities": [{"pair": list(p), "count": pairs[p]}
                                for p in combinations(vertices, 2)],
        "noncollinearity_edges": edges, "components": components,
        "component_sizes": sorted(map(len, components)), "failures": failures,
    }


vertices = list(range(16))
cyclic = inspect(vertices, [sorted((b + t) % 16 for b in [0, 1, 4, 6])
                            for t in vertices])
# Numeric labels follow L072's coordinate table, row by row:
# a,b,y1,y2,c,d1,d2,d3,z1,d4,d5,w1,z2,d6,w2,d7.
plane = inspect(vertices, [
    [0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15],
    [0, 4, 8, 12], [1, 5, 9, 13], [2, 6, 10, 14], [3, 7, 11, 15],
    [0, 5, 10, 15], [1, 4, 11, 14], [2, 7, 8, 13], [3, 6, 9, 12],
    [0, 6, 11, 13], [1, 7, 10, 12], [2, 4, 9, 15], [3, 5, 8, 14],
])
failures = cyclic["failures"] + plane["failures"]
if cyclic["component_sizes"] != [16]:
    failures.append("Cyclic graph differs from required component size [16]")
if plane["component_sizes"] != [4, 4, 4, 4]:
    failures.append("L072 graph differs from required component sizes [4,4,4,4]")
expected = {tuple(sorted((x, (x + d) % 16))) for x in vertices for d in [7, 8, 9]}
if {tuple(e) for e in cyclic["noncollinearity_edges"]} != expected:
    failures.append("Cyclic complete graph differs from difference set {7,8,9}")
if any(sum(x in edge for edge in plane["noncollinearity_edges"]) != 3 for x in vertices):
    failures.append("L072 graph degree differs from three")
path = Path(__file__).with_name("cyclic-nonrigidity-certificate.json")
path.write_text(json.dumps({"cyclic": cyclic, "L072": plane, "failures": failures}, indent=2) + "\n")
print(f"Cyclic components: actual {cyclic['component_sizes']}; required [16]")
print(f"L072 components: actual {plane['component_sizes']}; required [4, 4, 4, 4]")
print(f"All 120 block pairs and 120 vertex pairs checked per family; failures: {failures}")
print(f"Certificate: {path}")
raise SystemExit(bool(failures))
