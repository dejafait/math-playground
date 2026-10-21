# L054 — The 96a1 compositum is not normal over its cubic base

## Hypotheses

Use L051's number fields K96=Q(U) and L96=K96(T), with

    m(U)=U^12-4U^11-264U^7+66U^6-132U^5-2112U^4
         -1320U^3-660U^2-6240U-8007,
    h(T)=T^3-4T^2-160T-1264,
    [K96:Q]=12, [L96:Q]=36.

Set F=Q(T), using the same T inside L96. The field identifications
and degrees are imported, as in L051, from Freitas–Naskręcki–Stoll,
*The generalized Fermat equation with exponents 2, 3, n*, Compositio
Mathematica **156** (2020), 77–113,
[DOI](https://doi.org/10.1112/S0010437X19007693),
[final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
June 10, 2019, Section 7.2, printed pp.25–28, Table 5, and
[primary section7.magma](https://www.mathe2.uni-bayreuth.de/stoll/magma/GenFermat/section7.magma),
zero-based lines 315–334 and coordinate transport at lines 265–267.
Here T=4 theta for the source two-torsion coordinate theta. No
GRH-dependent class-group or Selmer computation is assumed.

Use L052's audited maximal-ring conclusion: K96 has a prime q above
3 with e(q/3)=11. No further cubic prime decomposition is assumed.

## Conclusion

L96/F is not normal, and hence is not Galois. Changing the base from
Q to this cubic field does not repair the normal-extension premise
of the previously assessed norm-relation framework.

This rules out that applicability variant only. It supplies no
square-class certificate, class/unit/Selmer completeness, global
intersection, full-disk disjointness or integer branch exclusion.
Normal-closure and frameworks for nonnormal extensions are undecided.

## Proof

First [L96:K96]=36/12=3. Since L96=K96(T), the minimal polynomial
of T over K96 has degree three. The monic degree-three polynomial h
annihilates T, so it is that minimal polynomial. In particular h is
irreducible over K96, and therefore also over its subfield Q: a
factorization over Q would be a factorization over K96. Consequently
[F:Q]=3 and [L96:F]=36/3=12. This does not assert that F/Q is normal.

Write O_K, O_F and O_L for the maximal integer rings. All these
number fields are finite and separable in characteristic zero. We
import prime existence and contraction from Sutherland, *18.785
Number Theory I*, Fall 2021,
[Lecture 5](https://math.mit.edu/classes/18.785/2021fa/LectureNotes5.pdf),
September 22, Lemma 5.28 and following paragraph, printed p.8.
Its Lemma 5.30, printed p.9, gives ramification multiplicativity.
The rings are Dedekind (Corollary 5.27, printed p.7), and O_L is the
integral closure of either O_K or O_F in L96. These statements apply
to the maximal rings, without a principal-ideal or power-order premise.

Choose a prime r of O_L above q, and let p=r intersect O_F. Then p
lies above 3, since q lies above 3 and r contracts to q in O_K.
In the two actual towers Q subset K96 subset L96 and
Q subset F subset L96, multiplicativity gives

    e(r/3)=11 e(r/q)=e(r/p)e(p/3).

Neither use of multiplicativity requires normality. To bound the
cubic-base index b=e(p/3), apply Milne, *Algebraic Number Theory*,
v3.08 (July 19, 2020),
[author notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorem 3.34, printed pp.59–60, in its general separable case to
Z, Q, F and O_F. It gives

    sum_{p' above 3} e(p'/3) f(p'/3)=[F:Q]=3.

All summands are positive integers. Thus 1<=b<=3, even if the cubic
base has several primes above 3 or is nonnormal. In particular
gcd(b,11)=1. The tower equality therefore forces 11 to divide
e(r/p), by primality of eleven. No exact value of b is needed, and
the absolute index e(r/3) is not being substituted for e(r/p).

Suppose L96/F were normal. Characteristic-zero separability would
make it Galois; use Milne, *Fields and Galois Theory*, v5.10
(September 2022),
[author notes](https://www.jmilne.org/math/CourseNotes/FT.pdf),
Proposition 2.20, printed p.32, and Definitions 3.6–3.9, printed p.37.
Apply ANT Theorem 3.34 now to O_F, F, L96 and O_L at the nonzero
prime p. Its Galois case gives common relative indices e,f and

    e f g=[L96:F]=12,

where g is the positive number of primes of O_L above p and
e=e(r/p). Thus 11 would divide 12, a contradiction. L96/F is not
normal. The general sum formula alone would not give this divisibility;
the Galois formula is used only under the contrary assumption.

For the downstream interpretation, the previously assessed
Biasse–Fieker–Hofmann–Page framework, *Norm relations and computational
problems in number fields*,
[author manuscript](https://www.normalesup.org/~page/Recherche/Documents/articles/brauer.pdf),
[JLMS DOI](https://doi.org/10.1112/jlms.12563), Proposition 3.7,
requires a normal extension as well as a norm relation. Its base
may be a number field, but the top extension L96/F fails that premise.
No claim about alternative frameworks follows.

This is REPRODUCTION under the prior SPECIALIZE assessment. The
standard results are imported without reproof; the field-specific
applicability argument handles the changed base. L053 is a contrast,
not an input: its absolute-degree contradiction is not transferred
unchanged. No mathematical script is needed for 1<=b<=3 and 11 not
dividing 12. No progress beyond the checked sources is claimed.

## Mathlib

The exact relative-field result and supporting prime/tower/Galois
statements are **not checked** in Mathlib. Unknown coverage is not
evidence of absence. This is an informal proof, with no formal
verification claimed.
