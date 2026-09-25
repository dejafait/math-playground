"""Exact finite checks for L006; no interacting renormalization computed."""

from fractions import Fraction
from itertools import combinations, combinations_with_replacement, permutations, product


axes = tuple(range(4))
planes = tuple(combinations(axes, 2))
plane_index = {plane: i for i, plane in enumerate(planes)}
perms = tuple(permutations(axes))
signs = tuple(product((-1, 1), repeat=4))
monomials = tuple(combinations_with_replacement(range(6), 2))


def image_plane(plane, permutation):
    return tuple(sorted(permutation[i] for i in plane))


def plane_character(plane, reflection):
    i, j = plane
    return reflection[i] * reflection[j]


# Project all 21 color-contracted quadratic monomials onto the trivial
# character of the 16 independent coordinate reflections.
reflection_average = {
    (i, j): Fraction(sum(
        plane_character(planes[i], reflection)
        * plane_character(planes[j], reflection)
        for reflection in signs
    ), len(signs))
    for i, j in monomials
}
assert {monomial for monomial, weight in reflection_average.items() if weight} == {
    (i, i) for i in range(6)
}
assert set(reflection_average.values()) == {Fraction(0), Fraction(1)}

# Enumerate ordered-pair orbits directly, rather than assuming intersection
# cardinality is the full invariant of the permutation action.
remaining = set(product(range(6), repeat=2))
orbits = []
while remaining:
    i, j = min(remaining)
    orbit = {
        (plane_index[image_plane(planes[i], p)],
         plane_index[image_plane(planes[j], p)])
        for p in perms
    }
    orbits.append(orbit)
    remaining -= orbit
assert sorted(map(len, orbits)) == [6, 6, 24]
assert {next(iter({len(set(planes[i]) & set(planes[j])) for i, j in orbit}))
        for orbit in orbits} == {0, 1, 2}
assert all(len({len(set(planes[i]) & set(planes[j])) for i, j in orbit}) == 1
           for orbit in orbits)

identity = [[Fraction(i == j) for j in range(6)] for i in range(6)]
complement = [[Fraction(set(planes[i]).isdisjoint(planes[j]))
               for j in range(6)] for i in range(6)]
adjacent = [[Fraction(len(set(planes[i]) & set(planes[j])) == 1)
             for j in range(6)] for i in range(6)]
minus = [[(identity[i][j] - complement[i][j]) / 2
          for j in range(6)] for i in range(6)]


def multiply(left, right):
    return [[sum(left[i][k] * right[k][j] for k in range(6))
             for j in range(6)] for i in range(6)]


zero = [[Fraction(0) for _ in range(6)] for _ in range(6)]
assert multiply(minus, minus) == minus
assert sum(minus[i][i] for i in range(6)) == 3
assert multiply(adjacent, minus) == zero
assert multiply(complement, minus) == [[-x for x in row] for row in minus]

character_inner_product = Fraction(0)
triplet_multiplicity = Fraction(0)
identity_multiplicity = Fraction(0)
for permutation in perms:
    pmat = [[Fraction(plane_index[image_plane(planes[j], permutation)] == i)
             for j in range(6)] for i in range(6)]
    for matrix in (identity, adjacent, complement):
        assert multiply(matrix, pmat) == multiply(pmat, matrix)
    restricted = multiply(minus, pmat)
    triplet_character = sum(restricted[i][i] for i in range(6))
    standard_character = sum(permutation[i] == i for i in axes) - 1
    assert triplet_character == standard_character
    plane_character_trace = sum(pmat[i][i] for i in range(6))
    character_inner_product += triplet_character ** 2 / len(perms)
    triplet_multiplicity += triplet_character * plane_character_trace / len(perms)
    identity_multiplicity += triplet_character / len(perms)
assert character_inner_product == 1
assert triplet_multiplicity == 1
assert identity_multiplicity == 0


def center_offsets(plane):
    i, j = plane
    return {
        tuple(si if k == i else sj if k == j else 0 for k in axes)
        for si, sj in product((-1, 1), repeat=2)
    }


# Offsets are measured in units a/2. All 384 signed permutations must map
# the four plaquette centers at one vertex onto the correct four centers.
geometry_checks = 0
for permutation, reflection in product(perms, signs):
    for plane in planes:
        transformed = set()
        for offset in center_offsets(plane):
            image = [0] * 4
            for i in axes:
                image[permutation[i]] = reflection[i] * offset[i]
            transformed.add(tuple(image))
        assert transformed == center_offsets(image_plane(plane, permutation))
        geometry_checks += 1

# The symmetric test average cancels first moments and has second moments
# a^2/4 along each of the two plane axes, giving the Taylor coefficient a^2/8.
for plane in planes:
    offsets = [tuple(Fraction(v, 2) for v in offset)
               for offset in center_offsets(plane)]
    for i in axes:
        assert sum(offset[i] for offset in offsets) == 0
        for j in axes:
            second_moment = sum(offset[i] * offset[j] for offset in offsets) / 4
            expected = Fraction(1, 4) if i == j and i in plane else Fraction(0)
            assert second_moment == expected

print("Reflection projection: 21 quadratic monomials -> exactly 6 plane squares.")
print("Ordered-pair orbits: 6 equal, 24 overlapping, 6 complementary.")
print("Triplet: irreducible, multiplicity 1; identity multiplicity 0; scalar action checked.")
print(f"Site geometry: {geometry_checks} signed-permutation checks; Taylor moments exact.")
print("No finite matching constant or interacting remainder estimated.")
