# L090 — Uniform literal recipient-zero exclusion for d=6,...,33

## Hypotheses

Let d be an integer with 6<=d<=33. Take L055's 25 indexed pairs,
changing only H_0=40-d and H_24=32670621+d. Every J is unchanged;
in particular J_0=8,J_1=15. Let b_i be nonnegative integers with
sum b_i=B=9250245, and put a_i=2+18b_i. Use literal indexed order.
Set

\[
\kappa=23/11,\quad G_i=(27/16)^{J_i}(3/2)^{H_i},\quad
Q_i=(12/11)(3/2)^{H_i}+1.
\]

Suppose real s_0,...,s_25 satisfy s_25=s_0, s_i>=540/11 and,
for every 0<=i<25,

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa,\qquad
4J_i\log2\le\log s_i+\log(11/4).
\tag{1}
\]

All logarithms are natural. No minimum, seed, H guard, integer junction,
parity, valuation, actual-word or primitive-count premise is imposed.
C077a supplies definitions only; its failed full conjunction is not assumed.

## Conclusion

Every such tuple has b_0=0. Uniformly over all 28 tables and every
remaining allocation, b_0>=1 would imply s_1<2000000000000, whereas
row1's own-input J guard requires
s_1>=4611686018427387904/11>400000000000000000.

This is local REPRODUCTION under the prior SPECIALIZE assessment
`drafts/literature/2026-10-20-h-transfer-six-through-thirty-three-recipient-zero.md`.
It establishes only this recipient-zero implication. Other recipients,
orders, last-pair/survivor exclusions, actual-word transfer and universal
eventual descent remain independent. No originality beyond the sources
checked is asserted. The separate critical audit below found no defect
within this precise scope.

## Proof

### Imported cap and its precise applicability

Use L085's signed-offset mechanism, importing only L076's audited
guard-conditioned cap proof cases (6)–(7), before its offset-sign premise.
L084 independently checks those cap data for this family; its different
C/H test-allocation caps and its failed full support conclusion are unused.

The underlying formal real-affine composition is supplied by
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The positive-real estimate used in the cap is
[DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1), log(1+x)<x for x>0.
The prior assessment inspected the needed theorem/proof cases. No coding
or parity-realization theorem is reproved or used as a converse.

Here 7<=H_0<=34, H_24=32670621+d and all other pairs are unchanged.
Thus every H_i>=3 and the increasing J_i are exactly L055's. The opposite
H changes preserve sum H=199390205 and sum J=66061058. Consequently,
for every admitted allocation,

\[
K=\sum_i(3J_i+H_i)=397573379,\qquad
N=\sum_i(4J_i+H_i)+50+18B=630138897.
\]

Import the certified analytic enclosure from L055 (2), also verified for
the family in L084 (2) and its independent audit:

\[
0<\lambda:=10584/10^{14}<\Lambda:=N\log2-K\log3<10585/10^{14}.
\tag{2}
\]

To match the cap, put n_i=s_i-kappa>=47 and

\[
\eta_i=\kappa-(12/11)(16/27)^{J_i}
                   -(16/27)^{J_i}(2/3)^{H_i},\qquad
c_i=2^{-a_i}G_i.
\]

Both subtracted terms are positive and their sum is less than
12/11+1=kappa, so 0<eta_i<kappa. Equation (1) becomes
n_(i+1)=c_i(n_i+eta_i), with all quantities positive. The full product
is prod c_i=3^K/2^N; every tail, including the closing tail even when
a_24=2, remains in it. Hence the identity in L076 (6) applies:

\[
\Lambda=\sum_{i=0}^{24}\log(1+\eta_i/n_i).
\]

For i>=1, its own-input J guard gives
n_i>=(4*2^{4J_i}-23)/11>=(4*2^60-23)/11>0. Thus the remaining
cap proof applies with precisely

\[
E=\frac{552}{4611686018427387881},\qquad
\lambda-E=\frac{6101253702379434166563}
 {57646075230342348512500000000000}>0,
\]
\[
s_0<R:=\frac{\kappa}{\lambda-E}+\kappa
=\frac{1325859730438202850942226985830949}{67113790726173775832193}
<U:=20000000000.
\tag{3}
\]

Every inversion has positive denominator. Only the positive eta bounds,
all endpoints, the budget, the J guards and (2) enter this imported cap;
no negative-offset test, minimum location or later-row growth is needed.

### Full signed endpoint uniformly over the approved range

Suppose b_0>=1. Integrality gives a_0>=20. At the actual input,
G_0s_0-Q_0=G_0(n_0+eta_0)>0. Tail replacement therefore gives,
using the positive slope of the tail-20 map and (3),

\[
s_1\le2^{-20}(G_0s_0-Q_0)+\kappa
<F_d(U):=2^{-20}(G_0U-Q_0)+\kappa.
\tag{4}
\]

This compares at an assumed solution's actual input; it constructs no
comparison trajectory. Retain the complete signed offset by factoring:

\[
F_d(U)=2^{-20}(3/2)^{40-d}A+\kappa-2^{-20},\qquad
A=(27/16)^8U-12/11
=\frac{30339110364144756051}{23068672}>0.
\tag{5}
\]

Since 3/2>1 and A>0, F_d(U) is strictly decreasing as integer d
increases. This proves uniformity, rather than inferring it from two
sampled endpoints. Its maximum on the approved range is exactly

\[
F_6(U)=\frac{505970856149948176893405564055875435}
 {415568250492528778805248}<2000000000000.
\tag{6}
\]

The last comparison follows by cross-multiplication with its positive
denominator: 2000000000000-F_6(U) has numerator
325165644835109380717090435944124565 over that denominator.
Neither the negative term -2^(-20)Q_0 nor the outside shift kappa
has been dropped. In particular the signed offset can be positive;
no failed L084 sign premise is repaired or invoked.

Row1's own guard in (1), at the actual output s_1 and J_1=15, gives

\[
s_1\ge(4/11)2^{60}=4611686018427387904/11
>400000000000000000.
\tag{7}
\]

Equations (4)–(7) contradict each other strictly. Hence b_0=0.
The cap accounts for arbitrary later allocations and closure, while the
tail comparison needs only b_0>=1. No other recipient is tested.

### Exact certificate and limitations

Run `python3 scripts/postspell-word-count/certify_uniform_recipient_zero.py`.
Full evidence is
`scripts/postspell-word-count/uniform-recipient-zero-certificate.json`.
It records every changed table and all 28 full signed endpoint values,
both endpoint evaluations, invariant totals, residual, cap, own-input
threshold and complete comparison operands. All 263 exact rational
checks pass, with zero failures. The complete common and uniform
comparison records and all table verdicts were inspected. The symbolic
argument (5) and exact maximum (6) supply the full-range proof; no
preview or sampled allocation is used as proof. The analytic enclosure
(2) is explicitly imported, not recertified by this constructor.

This is construction-time verification, not an independent critical
audit. Attempt 032's sufficient-test failure and both original d0
rational witnesses remain intact. No range extension, retuning,
feasibility verdict, broader allocation/order exclusion or universal
Collatz conclusion follows.

### Independent critical audit — 2026-10-20, step 381

The prior SPECIALIZE assessment
`drafts/literature/2026-10-20-uniform-recipient-zero-critical-audit.md`
licenses this RESEARCH/REPRODUCTION proof audit. No defect was found.
This verifies the existing local implication, without a new exclusion,
stronger bound or claim of progress beyond the sources checked.

**Cap and full-allocation quantifiers.** Independently transcribing all
25 L055 pairs and applying the two opposite H changes reproduces all
28 complete tables. In each table every J_i>=2,H_i>=3 and every
J_i for i>=1 is at least 15. The arbitrary allocation contributes
sum a_i=50+18B=166504460; hence its K,N are precisely those in (2).
The closing tail is included even when b_24=0 and a_24=2.

For each actual input of an assumed tuple, n_i=s_i-kappa>=47.
The bounds 0<eta_i<kappa follow from the two strictly subunit
positive powers in the displayed eta formula. Subtracting kappa
in (1) gives n_(i+1)=c_i(n_i+eta_i). Thus the product of all 25
positive ratios telescopes, including n_25=n_0, and taking its
logarithm gives exactly the identity preceding (3). For each i>=1,
exponentiation of its own non-strict J guard gives
n_i>=(2^62-23)/11. Applying the cited DLMF 4.5.1 at
x=eta_i/n_i>0 makes the 24-term sum strictly below E. The remaining
term is strictly below kappa/n_0. Consequently
lambda-E<kappa/n_0; positivity of the independently checked residual
justifies inversion and yields s_0<R<U. This remains strict if any
original J guard holds at equality.

Only this initial proof case of L076 is used. Its later offset tests
are absent from the preceding argument; neither L084's distinct C/H
test-allocation caps nor any full C077a conjunction enters. No minimum,
later-row growth, seed, H guard or integer-junction premise is needed.

**Signed endpoint and finite-range maximum.** Integer b_0>=1 gives
a_0>=20. The actual bracket G_0(n_0+eta_0) is strictly positive
before the tail is replaced. The tail-20 map has strictly positive
input slope, so the strict cap makes (4) strict even when a_0=20.
The factorization (5) retains both the inside -1 and the outside
kappa, as well as the subtracted (12/11)(3/2)^(40-d).
Its coefficient A is positive. For 6<=d<33 the exact difference is

\[
F_d(U)-F_{d+1}(U)
=\frac{A}{2^{21}}(3/2)^{39-d}>0.
\]

Thus d6 is the maximum on the entire stated range, independently
of the finite evaluation list. The exact numerator and denominator
in (6), their positive comparison difference, and the row1 threshold
in (7) all reconstruct without change. The contradiction is between
the actual s_1<2*10^12 and that same occurrence's required
s_1>=2^62/11>4*10^17. Arbitrary later allocations affect neither
this tail comparison nor the already uniform cap. No other recipient
or order has been tested.

**Independent exact evidence.** Run
`python3 scripts/postspell-word-count/audit_uniform_recipient_zero.py`.
It neither imports nor executes the constructor. It reads the complete
original certificate and reconstructs all its 263 rational comparisons,
including names, operands, relation, exact difference and verdict.
Each sign is separately evaluated by integer cross products. Every
table, numeric field, complete range and summary is matched. Unshifted,
direct shifted and factored endpoint evaluations agree at all 28 d;
all 27 adjacent differences agree with the formula above. The actual
positive brackets and the positive signed offsets also check, preserving
the failure recorded in Attempt 032. All 677 audit checks pass with
zero failures; these are verification counts, not separate advances.

The imported Lambda enclosure is independently checked using the already
assessed positive-real specialization of
[DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4). For t=2,3 put
x=(t-1)/(t+1) in (0,1) and
P=2 sum_(m=0)^95 x^(2m+1)/(2m+1).
Positivity gives P<log t, and bounding all omitted denominators below
by 193 gives the strict upper remainder
2x^193/[193(1-x^2)]. Opposite interval ends in N log2-K log3
retain both amplified errors and place the complete rational interval
strictly inside

\[
105843488/10^{18}<\Lambda<105843489/10^{18},
\]

which is itself strictly inside (2). This verifies an existing analytic
input by its assessed series method, not a new logarithm theorem.

Full evidence is in
`scripts/postspell-word-count/uniform-recipient-zero-audit-certificate.json`:
the original source hash, all reconstructed tables and comparison
operands, all audit checks, 192 series terms, both remainders and both
complete Lambda endpoints. The program checks every original operand;
the complete cap, uniform-maximum, extreme-table and Lambda-enclosure
records were also inspected. The quantified argument above, not a
certificate preview or sampled allocation, supplies uniformity.

Attempt 032 and both original d0 witnesses remain valid. Other recipients,
cyclic order, last-pair/survivor exclusion, actual-word transfer and
universal eventual descent remain unresolved. The mathematical argument
and direct inputs are unchanged, so DAG.md and PROOF.md are unchanged;
this canonical audit supersedes their older pending-audit wording for L090.

## Mathlib

Full matching coverage is unchecked, not absent. Supporting real-log,
affine and rational-arithmetic facts are not a formalization of this
complete quantified specialization. No Lean proof is claimed.
