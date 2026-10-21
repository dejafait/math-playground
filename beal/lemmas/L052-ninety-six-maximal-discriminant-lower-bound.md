# L052 — Maximal-field discriminant lower bound for the 96a1 workload

## Hypotheses

Use exactly L051's number fields K96=Q(U) and L96=K96(T), with

    m(U)=U^12-4U^11-264U^7+66U^6-132U^5-2112U^4
         -1320U^3-660U^2-6240U-8007,
    h(T)=T^3-4T^2-160T-1264,
    [K96:Q]=12, [L96:Q]=36.

These field identifications and degrees are the cited FNS inputs in
L051; no class-group or Selmer computation from that source is assumed.
Let Delta_K and Delta_L denote discriminants of the maximal integer
rings, and let s be the number of nonreal conjugate embedding pairs of
L96. Define its true Minkowski cutoff by

    M=(36!/36^36)(4/pi)^s sqrt(|Delta_L|).

## Conclusion

The entire K96 completion at each of p=3,11 has field degrees [11,1]
and ramification/residue pairs [(11,1),(1,1)]. Consequently

    v_3(Delta_K)=10,  v_11(Delta_K)>=11,
    3^30*11^33 divides Delta_L,
    |Delta_L|>=4781853336583741771837630738320908723679154940019,
    M>7646157636>10^6.

Enumeration up to the true Minkowski cutoff fails the proposed 10^6
entry threshold. This does not bound the necessary complexity of class
generation, forbid smaller generating sets or another certification
method, compute the exact discriminant or signature, or exclude a
Beal branch. The separate critical audit below confirms this bound
without a correction or a stronger mathematical conclusion.

## Proof

We import the following standard results without reproof. Milne,
*Algebraic Number Theory*, v3.08, July 19, 2020,
[author notes](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Proposition 7.44, printed pp.125–126, gives root valuations and the
factorization by distinct Newton slopes over a complete discretely
valued characteristic-zero field. Theorem 7.38, Corollary 7.42 and
Remark 7.43, printed pp.123–125, supply unique valuation extension,
the degree ef and the value group (1/e)Z when v_p(p)=1.
Sutherland, 18.785 Fall 2021,
[Lecture 11](https://math.mit.edu/classes/18.785/2021fa/LectureNotes11.pdf),
October 18, Theorem 11.23, pp.8–9, identifies the entire completion
algebra with the product of prime completions, whose degrees are ef.
Keith Conrad, [*The Different Ideal*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf),
author PDF retrieved October 10, 2026, Theorem 4.13, pp.12–14, gives
different exponent e-1 when p does not divide e and at least e when
p divides e. Sutherland,
[Lecture 12](https://math.mit.edu/classes/18.785/2021fa/LectureNotes12.pdf),
October 20, Proposition 12.4 (p.2), Theorem 12.17 (p.6), and Proposition
12.28 (p.10), give completion compatibility, discriminant as the norm
of the different, and the maximal-ring discriminant tower formula.
Milne Theorem 4.3, printed p.70, supplies the stated Minkowski cutoff.

These results apply to number fields and their complete prime fields;
all extensions are finite and separable in characteristic zero and all
residue fields are finite, hence perfect. In particular, the different
and tower statements concern maximal integral closures. No hypothesis
that a polynomial power order is maximal is used.

Here are all coefficients needed for the two Newton polygons. They are
listed in ascending powers, from constant through degree twelve:

    m(V):
    [-8007,-6240,-660,-1320,-2112,-132,66,-264,0,0,0,-4,1],
    v_3:
    [1,1,1,1,1,1,1,1,infinity,infinity,infinity,0,0];

    m(V+3):
    [-977856,-2050752,-1862256,-751344,116193,336072,219054,
     85272,22275,3960,462,32,1],
    v_11:
    [1,1,1,1,1,1,1,1,1,1,1,0,0].

The translation is the exact binomial identity
c_i=sum_{j=i}^{12} a_j binom(j,i) 3^(j-i), with a_j the coefficients
of m. Each finite point of either ascending-coefficient polygon lies
on or above the segments with vertices (0,1),(11,0),(12,0); for
0<=i<=11 this is the integer inequality 11 v_p(c_i)>=11-i.
The endpoint at degree twelve has valuation zero. Thus these are the
complete lower polygons. Their slopes are -1/11 and 0, with horizontal
lengths eleven and one respectively. Ascending-coefficient slopes are
the negatives of root valuations (Milne's indexing is descending).

The slope-factor theorem therefore supplies a monic degree-eleven
factor with all root valuations 1/11 and a degree-one factor with root
valuation zero over Q_p, for each p=3,11. The degree-eleven factor is
irreducible: if an irreducible factor has root alpha and degree d,
write E=Q_p(alpha), with ramification index e and residue degree f.
The extension of v_p has value group (1/e)Z. Since v_p(alpha)=1/11,
we have 11|e; and d=ef>=11. All eleven roots already belong to this
slope block, so there can be only one irreducible factor and d=e=11,
f=1. The remaining length-one factor is Q_p itself. For the translated
polynomial alpha=U-3 generates the same field as U. This accounts for
all twelve degrees at both primes, rather than selecting one factor
or inferring decomposition from a repeated residue polynomial.

In the degree-eleven completion at 3 the ramification is tame, so its
different exponent is 10. At 11 it is wild, so its exponent is at least
11. In each rational factor the different exponent is zero. Taking
the local ideal norm weights each exponent by f=1. Completion and
different/discriminant compatibility now give v_3(Delta_K)=10 and
v_11(Delta_K)>=11 for the maximal field discriminant.

By L051, [L96:K96]=36/12=3. The tower formula is

    Disc(L96/Q)=Disc(K96/Q)^3
                 N_(K96/Q)(Disc(L96/K96)).

The relative discriminant is an integral nonzero ideal, so its norm
is a positive integer and cannot subtract a prime exponent. Hence
v_3(Delta_L)>=30 and v_11(Delta_L)>=33. This proves the divisibility
and the absolute lower bound D0=3^30*11^33 in the conclusion. We do
not require the local tensor products with the cubic field to be fields,
or make any assertion about further ramification in them.

For every actual signature, s>=0 and pi<4 imply (4/pi)^s>=1. Set

    q=36!/36^36=a/b,
    a=167669460258147894921875,
    b=47952233990219156918037822976303300608.

Then M>=q sqrt(D0). With F=7646157636 the exact certificate checks

    F^2 b^2 < D0 a^2 < (F+1)^2 b^2,
    D0 a^2 > (10^6)^2 b^2.

All quantities are positive, so squaring preserves the comparisons
and M>F>10^6. No actual signature or floating-point rounding is used.

Reproduce the field-specific arithmetic with

    python3 scripts/ninety-six-class-generation/discriminant_lower_bound.py

The full certificate is
`scripts/ninety-six-class-generation/discriminant-lower-bound-certificate.json`.
It records complete translated coefficients, valuations, both polygons,
all coefficient inequalities, independent residue identities, the
theorem-based local degree/different conclusions, and exact squared
rounding differences. The local-field conclusions are justified above;
the program verifies their numerical premises, not the source theorems.
This is a specialization of the assessed standard mechanism, needed
because L051's order upper bound cannot establish a maximal-field
lower bound. No novelty beyond the sources checked is asserted.

### Independent critical audit, 2026-10-11

The entire original `/local` and `/cutoff` certificate fields were
checked against an independent computation:

    python3 scripts/ninety-six-class-generation/audit_lower_bound.py

Its complete evidence is saved in
`scripts/ninety-six-class-generation/lower-bound-audit-certificate.json`.
Horner translation and inverse translation check every coefficient,
without using the original binomial-translation routine. The supporting
line inequalities and attained endpoints independently certify both
lower polygons. A product of the fractions i/36, for 1<=i<=36, and
integer bisection independently reproduce q, the strict floor interval
and every squared-comparison difference. Both full local records and
the complete cutoff record agree; there are no arithmetic failures.

The mathematical audit also checks the implications that the program
does not prove. Unique valuation extension makes each irreducible
factor lie in one slope block, so the denominator-eleven argument
cannot overlook a smaller factor or mix the two slopes. The degree-one
block and the degree-eleven block exhaust the separable degree-twelve
algebra. The normalization v_p(p)=1 is used only to infer 11|e; the
different exponents are integer prime-ideal exponents in the extension
ring, with discriminant contribution f times that exponent. Thus there
is no missing factor e in the discriminant calculation. At 3 equality
10 is justified by tameness; at 11 only the lower bound 11 is used.
The relative discriminant is integral in the maximal ring, so its
norm adds nonnegative rational-prime valuations. Finally, q sqrt(D0)
is a lower bound for M for every actual signature, and all quantities
squared are positive. The cited field degrees remain inputs; this is
not an independent proof of FNS's field identifications. The audit
finds no correction, new bound, class completeness or branch exclusion.

## Mathlib

The full field-specific result and supporting Newton-polygon,
completion, different/tower and Minkowski results were **not checked**
in Mathlib. Unknown coverage is not evidence of absence. The exact
arithmetic certificate and informal proof claim no formal verification.
