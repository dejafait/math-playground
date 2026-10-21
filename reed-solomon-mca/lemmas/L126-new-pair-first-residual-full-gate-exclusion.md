# L126 — New-pair residual (58,355) has two ineligible planes

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, k=8, L010's
shifted moments and the pinned same-support event on
1/4<=delta<5/16. The actual Hankel determinant D and all actual
coordinate locators are nonzero polynomials. Both coefficient syndromes
belong to U_S for S={1,8,12,18,22,27,33}. Assume sixteen original
finite events and L104's t=0. Retain L109's inherited L010/L103/L104
hypotheses and finite-certificate qualifications. The original weights
and prescribed chart are arbitrary over F. The following four supports
are actual two-overlap errors, with J=H minus S:

| Row | I subset S | K subset J |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,75} |
| 3 | {1,12} | {70,79} |
| 4 | {8,27} | {79,89} |

Use L109's original exterior blocks with z_j=min(S minus I_j),
lexicographic covector-pair rows and increasing S-pair columns.

## Conclusion

These hypotheses are inconsistent. The original stack has rank nineteen
and complete kernel

    span(B0,B1),  B0=E_1 wedge w,  B1=E_8 wedge E_12,
    w=67E_8+68E_12+2E_18+44E_22+54E_27+E_33.

Over every extension of F_97 its entire decomposable projective locus
is exactly [B0],[B1]. All eight selected-row projections have rank one.
The first plane has full intrinsic recoveries at rows two and four but
lambda zero at rows one and three. The second has lambda zero at every
row. Both fail necessary gates in every prescribed original chart.

This excludes exactly the labeled occurrence with full-universe indices
(58,355) in L125. Its 154 historical residuals remain preserved; this
is one separately certified indexed exclusion, not a new partition or
third/pair assembly. The global interval remains 11/q–16/q. Same-step
independent replay passes; the separate step-362 critical audit found no
defect in this indexed exclusion.

## Proof

### Imported inputs and exact scope

Use only L109's necessary direction: actual independent lift coefficients
give a nonzero decomposable kernel tensor; every selected actual row
requires rank-one projection, nonzero lambda, two nonzero overlap weights
and the prescribed finite-direction gate. Rank zero is rejected by its
actual nonpersistence argument before divisions by recovery coefficients.
No four-row converse, universal representation or pair extraction is used.
L125 identifies the historical record; none of its partition conclusions
is needed to prove the independently reconstructed exclusion below.

The standard coding inputs are imported through L109: J. I. Hall,
*Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf);
I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2 and the shortening formula after Lemma 5.3.
Each row shortens exactly seven distinct labels J minus K from dimension
eight to positive dimension one, with nonzero products of distinct label
differences. Changed labels alter the coefficients, not these hypotheses.
Conrad, [*Exterior Powers*, Theorems 4.2, 7.1, 7.5, pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
supports the basis and wedge-plane association; L109 already supplies
the explicit homogeneous criterion and reconstruction formulas.
Milne, [*Fields and Galois Theory*, Kea Books 2022, sections 1.6–1.9,
pp. 5–7, Proposition 2.17 p. 34](https://www.jmilne.org/math/Books/FT0.pdf),
supports polynomial division and extension gcd identities. No general
coding, exterior or field theorem is reproved here.

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-20-new-pair-first-residual-locus-review.md`.
This is REPRODUCTION of its assessed method on the exact new labels.
L117/L119/L120 supply methods, not this record's coefficients or outcomes.
ATTEMPTS/041–044's inexpensive-filter failures remain unchanged.

### Original matrix and complete kernel over extensions

For each row evaluate g_j(X)=product_(y in J minus K_j)(X-y).
Form the four original covectors
c_jx=g_j(z_j)E_x^*−g_j(x)E_zj^* on S, and stack their six
exterior rows. This specifies all 504 entries of the 24-by-21 matrix N;
they are saved in `scripts/seven-coordinate/new-pair-first-residual-gates.json`.

The original minor with zero-based row indices

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,20

and column indices

    0,1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20

has integer determinant

    −16304398318117198723155451969536000 = 8 modulo 97.

Both B0 and B1 have zero residual at all 24 original rows. In columns
5 and 6 their entries form the identity matrix. Thus they are independent,
rank(N)<=19, and the nonzero minor gives rank(N)>=19. They therefore
span the entire kernel. The same nonzero minor and independent null
vectors persist after any field extension, proving complete extension
kernels without rational-point sampling or a descent assumption.

The source audit's `/first_residual` is bound by its hash; the exact
record is also read from `scripts/seven-coordinate/new-pair-filter/third-058.json`,
which is separately hashed. The full 756-row lexicographic universe
binom(S,2) times binom(J,2) gives the displayed third at 58 and fourth
at 355. The selected shard record is unique, has residual status and
the same complete basis. No other occurrence is tested or removed.

### Complete homogeneous locus, including infinity

Write p=sB0+tB1. Its only possibly nonzero coordinates are

    p_(1,8)=67s, p_(1,12)=68s, p_(1,18)=2s,
    p_(1,22)=44s, p_(1,27)=54s, p_(1,33)=s, p_(8,12)=t.

Among the 35 increasing-label Plucker relations
p_ab p_cd−p_ac p_bd+p_ad p_bc, precisely those with labels
(1,8,12,x), x=18,22,27,33, have nonzero restrictions. They are
respectively 2st,44st,54st,st. Every product of two B0 entries
repeats label 1, and every product of two B1 entries repeats labels
8 and 12; the displayed mixed products are the only products using
four distinct labels. Hence the other 31 relations vanish identically.
All 35 full coefficient triples are independently checked.

The common homogeneous zero set is exactly st=0 over every extension
field, since one relation is st itself. For nonzero (s,t), a field
has no zero divisors, so the points are exactly [1:0],[0:1]. Both are
explicit nonzero wedges. Equivalently, on s=1 the complete affine gcd
is T: saved polynomial quotients and Bezout coefficients give
q_l=T Q_l and sum U_l q_l=T coefficientwise. The homogeneous equations
at s=0 separately retain infinity. No repeated, nonsplit, empty or
whole-line branch remains. L109's criterion consequently gives precisely
L0=span(E_1,w) and L1=span(E_8,E_12).

### All original-row gates and prescribed charts

For L0 take u=E_1,v=w, and for L1 take u=E_8,v=E_12.
Every Q_j restriction has all six two-by-two minors zero and a nonzero
component, so its rank is exactly one. At the first nonzero component n
use (alpha,beta)=(-Q_jv[n],Q_ju[n]) and h=alpha u+beta v.
Restore lambda=h_zj/g_j(z_j) and errors
e_i=h_i−lambda g_j(i) on I, e_k=−lambda g_j(k) on K, as in L109.

| Plane | Row | First (Q u,Q v) | (alpha,beta) | lambda | Weights on ordered I then K |
| --- | ---: | --- | --- | ---: | --- |
| L0 | 1 | (0,12) | (85,0) | 0 | (85,0,0,0) |
| L0 | 2 | (12,78) | (19,12) | 30 | (9,94,10,9) |
| L0 | 3 | (0,41) | (56,0) | 0 | (56,0,0,0) |
| L0 | 4 | (90,36) | (61,90) | 29 | (88,28,9,53) |
| L1 | 1 | (0,16) | (81,0) | 0 | (0,81,0,0) |
| L1 | 2 | (75,0) | (0,75) | 0 | (75,0,0,0) |
| L1 | 3 | (70,0) | (0,70) | 0 | (0,70,0,0) |
| L1 | 4 | (0,69) | (28,0) | 0 | (28,0,0,0) |

These representatives exhaust the unique intersection line for each row.
All lambda values, both overlap weights and both outside weights are
retained. For every row h−e=lambda g_j at all sixteen H labels, with h
extended by zero off S; every original shifted moment
sum_x x^d(h_x−e_x), d=1,...,8, vanishes. The certificate and replay
retain all 128 pointwise identities and 64 original moment residuals.
The two full rows on L0 do not repair its other failed rows.

Already at row one, Q_1E_1=0 and Q_1w has nonzero first component 12,
so L0 meets ker Q_1 in exactly F E_1. Similarly Q_1E_8=0 and Q_1E_12
has nonzero first component 16, giving intersection F E_8 for L1.
Here z_1=12. Both recovery lines have h_12=0 and hence lambda=0;
their outside weights vanish and the errors are not full four-errors.
This contradicts the necessary gates supplied by L109 under equality.

For any prescribed original basis u_original=A u+B v,
v_original=C u+D v, Delta=AD−BC!=0, inversion gives

    alpha_original=(D alpha−C beta)/Delta.

Thus the exact finite-direction gate for each table row is
D alpha−C beta!=0. If it vanishes the event is not original finite;
otherwise dividing h and e by alpha_original preserves every moment
identity and every failed zero weight. An arbitrary nonrational omitted
point cannot repair either plane. No replacement original chart is chosen.

### Verification and limits

Reproduce from this notebook:

    python3 scripts/seven-coordinate/new_pair_first_residual_gates.py
    python3 scripts/seven-coordinate/verify_new_pair_first_residual_gates.py

Full certificates are `scripts/seven-coordinate/new-pair-first-residual-gates.json`
and `scripts/seven-coordinate/new-pair-first-residual-gates-replay.json`.
The producer evaluates products directly and its determinant by modular
and fraction-free elimination. The verifier imports no producer helpers:
it differentiates X^16−1 at each simple root to compute
g_j(x)=16x^15/product_(y in (S union K_j) minus {x})(x−y)
on S union K_j. Normalized ratio covectors reconstruct every original
block entry, not merely a rank-equivalent matrix. Independent column
elimination recovers the full basis, and rational Gaussian determinant
evaluation reproduces the integer minor. Every homogeneous coefficient,
gcd/division/Bezout identity, projection, weight and original moment is
checked, including all seven nonzero exterior pivots and all 106 nonzero
projection-component choices. Each alternate intersection and all its
weights are certified nonzero scalar multiples of the canonical values.

All checks pass, with required/actual loci 1/1, two complete points,
eight rank-one row tests, six lambda-zero rows, two full rows and no
unresolved component. A certificate preview alone is not verification:
the complete selected locus and all row data are replayed. Both paths
share Python and residue arithmetic; this calculation-time replay is no
proof-assistant result or separate critical audit. It is a reproduced local input, with no
progress beyond the assessed general literature claimed. Representation,
pair extraction, all other residuals, sixteen-event completion and the
challenge-definition qualifications remain open.

### Separate critical audit, 2026-10-20

Step `2026-10-20-mca-362-new-pair-first-residual-critical-audit` reused the
unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-10-20-new-pair-first-residual-audit-review.md`.
It checked this entire proof, both complete programs, every called helper
body, L109's necessary proof and separate audit, and the relevant
L010/L103/L104 hypotheses and shortening passages. No mathematical or
program defect, missing essential hypothesis or new dependency was found.
The result is a separately validated reproduced input, not a new exclusion
or progress beyond the general literature already assessed.

The precise application uses the actual original sixteen finite events
before full weights and independent lift coefficients. L109 gives a
nonzero decomposable tensor in the four selected blocks even though its
converse needs at least six rows; that converse is not used. Its
inherited L103/L104 smaller-class bounds retain the L040/L069 finite
certificate qualifications, which this audit does not independently rerun.
The 154 historical residuals are neither new mathematical premises nor
deleted cases. L125 supplies provenance only.

The producer's closed helper inventory consists of field/domain/order
constants, `g`, `block`, `rank_and_rows`, `determinant`,
`integer_determinant`, `wedge`, `plucker_polynomials`, `plane_gates`,
and polynomial `trim`, `add`, `scale`, `mul`, `divrem`, `xgcd`,
`gcd_certificate`. Their signs, zero branches and column order agree with
L109. Only the new one-occurrence producer's `run` is invoked; no
historical helper census is executed. The verifier uses standard-library
imports only. Its derivative formula is valid at every retained simple
root of X^16−1: removing the other eight retained factors leaves exactly
g_j. Its ratio covectors are scaled back to the original covectors before
comparing all 504 matrix entries, rather than silently replacing the
matrix by a rank-equivalent one.

Column elimination independently reconstructs both complete null vectors.
The free-column identity matrix proves independence, while the original
signed minor has exactly the displayed integer value and residue eight.
Rational Gaussian elimination accounts for every row swap independently
of the producer's modular and fraction-free determinant paths. Together
these certify rank exactly nineteen, not merely an upper bound, over every
extension. The audit binds `/first_residual` and the unique fourth-355
record in `third-058.json` to their saved hashes, exact supports and
full 756-row lexicographic indices.

All 35 homogeneous coefficient triples are checked, including the 31
identically zero relations. The nonzero relations are precisely
2st,44st,54st,st. The coefficientwise quotient and Bezout identities
give affine gcd T, and the zero t² coefficients explicitly retain the
point at infinity. Hence the proof covers the entire extension-field
locus; neither base-field sampling nor an unexamined splitting case is
used. Both endpoints are reconstructed as nonzero wedges.

All eight original-row projections have rank exactly one, including a
checked nonzero component. The complete table above agrees with the
independent replay, preserving six lambda-zero rows, their canceled
weights, and the two full rows. Every one of the 128 pointwise identities
and 64 shifted-moment residuals is checked. Reconstructing all seven
nonzero exterior pivots and all 106 nonzero projection-component choices
gives nonzero multiples of the same intersection lines, lambdas and
weights. Thus no alternate pivot supplies a missed full recovery.

Finally, the displayed arbitrary-chart inverse has the correct sign and
determinant: the coefficient matrix is [[A,C],[B,D]]. If
D*alpha−C*beta=0, that row is omitted from the prescribed finite chart.
Otherwise its error is multiplied by the nonzero reciprocal of
alpha_original. Neither alternative repairs the zero first-row lambda.
This applies over F without rationalizing A,B,C,D or the omitted point.
Consequently both exhaustive planes contradict the necessary full-error
gate, with no four-row realization or extra-event claim.

Fresh isolated replay is reproducible with

    python3 scripts/seven-coordinate/audit_new_pair_first_residual_gates.py

The full audit record is `scripts/seven-coordinate/l126-critical-audit.json`.
All 29 audit checks pass; both full output certificates reproduce byte for
byte and all eight original program/input/output files remain unchanged.
The isolated copy runs the inspected producer and independent verifier,
and compares every output byte, including all pivot records. Actual and
required audited occurrences are 1/1 and excluded complete points 2/2,
with no unresolved branch. This supplements the semantic audit above;
neither program success nor a JSON preview substitutes for that audit.
Both implementations still share Python and residue arithmetic, and this
is not proof-assistant verification. No third, pair, universal extraction
or challenge-level conclusion is added; the interval remains 11/q–16/q.

## Mathlib

Full matching coverage for this exact labeled residual classification:
**not checked**. Supporting coding, exterior, matrix-rank, polynomial-gcd
and finite-field coverage: **not newly checked**. Unknown coverage is not
absence. Standard results are imported with the precise citations above;
the restricted calculation retains its explicit finite-certificate
qualifications after the separate critical audit above.
