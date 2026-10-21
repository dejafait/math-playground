# Pair Jacobian bounded lower-rank attempt

2026-10-20. Approved target: Test whether rational divisor classes on
L110's Jacobian certify Mordell–Weil rank at least two.
Prior SPECIALIZE coverage: `literature/2026-10-20-pair-jacobian-rank-lower-test.md`.

The main gap is primitive positive integer exclusion in residual Beal
signatures. This test concerns the genus-two necessary pair image for
ordered (3,5,11). A rank lower bound at least two would obstruct the usual
strict rank-below-genus Chabauty threshold. Point completeness, the marked
lift, degree-nine rational-root recovery, remaining factors, both L095
integer systems and minus-eleven remain independent gaps.

Reuse audited L109/L110 and the ready literature comparison, including
Stoll's torsion allowance and Müller's odd-model divisor formula. The
recorded bare-unit obstruction concerns a different Jacobian/base field;
the complete class backend remains parked. No new source search is needed.
Existing L108 unfinished work is preserved.

Plan: verify X=c/(T−2), Y=c²W/(T−2)³ with c=f'(2)=−36300, yielding a
monic integral quintic. Search precisely the approved rational-point and
quadratic-divisor boxes, transport each accepted divisor and reverify it.
Use good odd primes through 101 for a complete finite-factor torsion
allowance and common simple-root character detector. Continue only if
d−t>=2, or a specific defect gives a discriminating correction; otherwise
park this bounded test without asserting rank<2 or dependence.

## Completed bounded calculation

The script `scripts/pair-genus-two/rank_lower.py` uses exact integers,
fractions and polynomial arithmetic. It obtains

    g(X)=X^5−76835X^4+2196150000X^3−29655931140000X^2
         +191519916588000000X−477484407427500000000.

The checked coefficient identity is X^6 f(2+c/X)=c²g(X), with
c=−36300; the inverse is T=2+c/X, W=cY/X³. The quintic is squarefree,
monic and integral. The inverse rational functions identify the smooth
proper curves by the extension input already imported in L110. The
point (2,0) becomes infinity: ord(T−2)=2 and ord(W)=1 give
ord(X)=−2, ord(Y)=−5. L110 and its original s,z are unchanged.

The point loop tests all 304,463 reduced m/n with n>0 and
max(|m|,n)<=500. As f(m/n)=F_h(m,n)/n^6, rational W exists exactly
when the integer F_h(m,n) is a nonnegative square (a rational square
root of an integer is integral). Only (T,W)=(−2,0),(2,0) are found.
These are branch points, discarded under the approved detector scope;
their torsion classes are not asserted trivial. There is no rational
point at sextic infinity, since the leading coefficient −275 is nonsquare.

Of the 2,601 prescribed a=T²+a1*T+a0, eleven are not squarefree and
47 more meet the branch divisor. All 2,543 eligible quadratics receive
the full 1,001 slope tests, −500<=b1<=500: 2,545,543 tests. Write
f mod a=r0+r1*T. Exact divisibility a | f−(b1*T+b0)² is equivalent to

    r1=2 b1 b0−a1 b1²,     r0=b0²−a0 b1².

For b1!=0, b0=(r1+a1*b1²)/(2b1) is determined without a size bound;
the script even permits rational b0. For b1=0 it checks r1=0 and
b0²=r0, including both signs. There is no eligible divisor. No candidate
transport or Kummer class is claimed. The implemented transport would be

    A(X)=[X² a(2+c/X)]/a(2),
    B(X)=((b(2)/c)X³+b1 X²) mod A,

but there are no accepted candidates on which to apply it in this run.

All good odd primes through 101 are completely factored, with modular
irreducibility checked by Frobenius powers and proper-degree gcds.
The selected load-bearing factorization is at p=19:

    g mod 19=(X+7)(X⁴+13X³+6X²+3X+14).

For its quartic q, X^(19^4)−X=0 modulo q and
gcd(q,X^(19²)−X)=1; full residuals are saved and the two factors are
distinct. This certifies irreducibility of q and squarefreeness of the
product. Monic rational factors are integral and retain degree under
reduction; good squarefree reduction cannot merge them. Thus g has at
most two rational irreducible factors. Stoll, *Implementing 2-descent
for Jacobians of hyperelliptic curves*, Acta Arith. 98 (2001), 245–277,
Lemma 4.3(3), gives the allowance dim J(Q)[2]<=1. Its squarefree monic
integral odd-degree hypotheses hold. Full rational torsion is uncomputed.

The quotient and nonbranch-divisor formulas are imported from Stoll
Lemma 4.1/equation (1.1) and Müller, *Rational points on Jacobians of
hyperelliptic curves*, Lemmas 1.17–1.18 and Section 2.4, Proposition 2.7.
The precise links, hypotheses and qualifications remain in the unchanged
ready assessment. No general theorem is reproved. There are zero columns,
so the common-coordinate matrix has 38 rows, zero columns and d=0.
The certificate gives d−t=−1 against required >=2: a vacuous lower
certificate, with only the automatic rank>=0 available. It gives no
evidence that rank is zero or below two.

The first execution stopped on an implementation error before producing
a certificate: a derivative list could be all zero modulo a bad prime.
Trimming both gcd inputs fixes this. Review also corrected degree-one
irreducibility to reduce X modulo its factor before comparison. The final
run has 28 passing checks and no failures; no previous artifact changed.

The full final certificate is
`scripts/pair-genus-two/rank-lower-certificate.json`, SHA-256
`302933814614e4754c26ce76d0488ba411a1535ca8940476baadbadd5a454e72`.
It retains exact model data, complete search bounds/counts, every point
hit, empty divisor lists, all finite factorizations and irreducibility
checks, all 38 coordinate tables, empty matrix/pivots, rejection counts
and named check results. The selected full `/torsion_upper_witness` was
inspected, rather than treating a preview as verification.

## Independent search verification and decision

`scripts/pair-genus-two/verify_rank_lower.py` does not import the producer.
It tests every reduced rational input via the factored homogeneous sextic
and obtains the same two hits. For quadratics it separately computes
powers of T modulo a, then solves the exact equation

    (a1²−4a0) k²+(2a1*r1−4r0) k+r1²=0,     k=b1².

Its leading coefficient is nonzero because a is squarefree. For b1!=0
this equation and b0's formula are equivalent to both original equations.
Discriminants and rational roots therefore enumerate every possible
positive integral-square k in the prescribed slope range, independently
of the producer's slope loop. Zero slope is checked separately. No
eligible divisor is found. Nine replay checks pass with no failures;
all 2543 coefficient/discriminant records and exclusion counts are in
`scripts/pair-genus-two/rank-lower-search-replay.json`.

This is informative NEGATIVE evidence about the prescribed search,
not progress beyond the known source methods or a Beal exclusion.
The threshold failed and no candidate/detector defect survives review:
park this box. Do not increase caps or repeat it without a materially new
reason. No lemma is added merely to record a failed threshold. Mathlib
coverage was not checked; no absence or formal verification is claimed.

A different proposed continuation tests for an explicit genus-one
quotient over Q of L109's marked genus-three curve. A quotient could
constrain rational images on the actual marked locus independently of
unmarked rank. Its existence, twist and usefulness are unproved here;
coverage is REVIEW_REQUIRED for a separate next turn. Historical backend
stops and unfinished L108 work remain intact.
