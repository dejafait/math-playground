# L053 — The 96a1 compositum is not normal over Q

## Hypotheses

Use the exact number fields of L051: K96=Q(U), with

    m(U)=U^12-4U^11-264U^7+66U^6-132U^5-2112U^4
         -1320U^3-660U^2-6240U-8007,

and L96=K96(T), where

    h(T)=T^3-4T^2-160T-1264,
    [K96:Q]=12, [L96:Q]=36.

Use L052's audited maximal-ring local conclusion: above 3 in K96
there is a prime q with ramification index e(q/3)=11 and residue
degree one. The other prime and the independent data at 11 are not
needed for this test. Field identifications and degrees retain L051's
precise FNS citation; no source class-group, Selmer or GRH computation
is assumed.

## Conclusion

L96/Q is not normal (and hence is not Galois). In particular, this
extension cannot satisfy the normal-extension premise of the direct
norm-relation framework over Q assessed for the 96a1 branch.

This decides only that applicability condition. It gives no integer
exclusion, class/unit/Selmer completeness, norm relation or full-disk
disjointness. Relative-base, normal-closure and generalized frameworks
are not decided by this conclusion.

## Proof

Write O_K and O_L for the maximal integer rings of K96 and L96.
All fields are finite over Q and therefore separable in characteristic
zero. The integer rings are Dedekind domains, O_L is the integral
closure of O_K in L96, and the nonzero prime q of O_K has a prime r
of O_L above it. Here we import Sutherland, *18.785 Number Theory I*,
Fall 2021, [Lecture 5](https://math.mit.edu/classes/18.785/2021fa/LectureNotes5.pdf),
September 22, Lemma 5.28 and its following paragraph, printed p.8,
for prime existence and contraction in this integral-closure setup.
Lemma 5.30, printed p.9, gives ramification multiplicativity in the
finite separable tower Q subset K96 subset L96. Thus

    e(r/3)=e(r/q)e(q/3)=11 e(r/q),

where e(r/q) is a positive integer. In particular 11 divides e(r/3).
This transport needs no normality of either extension. The index 11
is an index for the actual maximal prime completion by L052, not a
multiplicity in a power-order residue polynomial.

Suppose for contradiction that L96/Q is normal. Characteristic-zero
separability makes this finite extension Galois; this is the standard
interface in Milne, *Fields and Galois Theory*, v5.10, September 2022,
[author notes](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Proposition 2.20 (printed p.32) and Definitions 3.6–3.9 (printed p.37).
Apply Milne, *Algebraic Number Theory*, v3.08, July 19, 2020,
[author notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorem 3.34, printed pp.59–60, to Z, Q, L96 and O_L at the prime 3.
In its Galois case all primes above 3 have common ramification and
residue indices e,f, and

    e f g = [L96:Q] = 36,

where g is the positive number of primes above 3. For the selected r,
e=e(r/3), so 11 divides the left side and would divide 36. But
36=3*11+3, a contradiction. Therefore L96/Q is not normal.

The source's general identity sum e_i f_i=36 alone would not suffice:
a single index 11 need not divide the degree in a non-Galois extension.
We use divisibility only under the contradiction's normality assumption.
Nor do we infer this conclusion merely from nonnormality of a subfield.

The downstream scope is limited to the direct normal-extension
interface: Biasse–Fieker–Hofmann–Page, *Norm relations and computational
problems in number fields*, [author manuscript](https://www.normalesup.org/~page/Recherche/Documents/articles/brauer.pdf),
39-page version linked to [arXiv:2002.12332](https://arxiv.org/abs/2002.12332)
and [JLMS DOI 10.1112/jlms.12563](https://doi.org/10.1112/jlms.12563),
Proposition 3.7 assumes a normal extension and a norm relation. Its
normality premise fails for L96/Q. This does not prove that other
certification methods are unavailable; in particular no assertion
about L96 over the cubic subfield or its normal closure is made here.

This is REPRODUCTION under the prior SPECIALIZE assessment: the
prime/tower/Galois theorems are imported, and their field-specific
applicability is the entire bounded attempt. No reproof or progress
beyond the sources checked is claimed. No mathematical script is
needed: the sole integer comparison is 11 not dividing 36.

## Mathlib

The full field-specific nonnormality result and supporting prime
existence, ramification tower and Galois degree statements are **not
checked** in Mathlib. Unknown coverage is not evidence of absence.
The citations and applicability argument give an informal proof only.
