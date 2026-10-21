# L127 — New-pair residual (58,647) has two ineligible planes

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, k=8, L010's shifted
moments and the pinned same-support event for 1/4<=delta<5/16. The
actual Hankel determinant D and every actual coordinate locator are
nonzero polynomials. Both coefficient syndromes belong to U_S, with
S={1,8,12,18,22,27,33}. Assume sixteen original finite events and
L104's t=0. Retain L109's inherited L010/L103/L104 hypotheses and
L040/L069 finite-certificate qualifications. Original weights and the
prescribed finite chart are arbitrary over F. With J=H minus S, these
four supports are actual two-overlap errors:

| Row | I subset S | K subset J |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,75} |
| 3 | {1,12} | {70,79} |
| 4 | {18,33} | {89,96} |

Use L109's original exterior blocks, z_j=min(S minus I_j), increasing
covector pairs and increasing S-pair columns.

## Conclusion

These hypotheses are inconsistent. The original 24-by-21 matrix has
rank nineteen and complete kernel span(B0,B1), where

    B0=E_1 wedge E_18,
    B1=E_12 wedge w,
    w=82E_1+13E_8+73E_18+63E_22+62E_27+E_33.

Over every extension of F_97 the complete decomposable projective locus
is exactly [B0],[B1]. All eight selected-row projections have rank one.
The first plane has lambda zero at every selected row. The second has
full intrinsic recoveries at rows one and four, but lambda zero at rows
two and three. Thus neither passes all necessary gates in any prescribed
original chart.

This excludes exactly full-universe occurrence (58,647) in L125.
All 154 historical residuals remain preserved. No third or pair assembly,
new partition, universal representation/extraction, sixteen-event completion
or global bound is obtained; the interval remains 11/q–16/q. Same-step
independent replay passes, and the separate step-366 critical audit below
found no defect in this restricted exclusion.

## Proof

### Imported inputs and bounded scope

L109's necessary direction gives independent lift coefficients and a
nonzero decomposable tensor in the selected stack kernel. Every actual
selected row must have projection rank one, nonzero lambda, both overlap
weights nonzero and a finite direction in the prescribed chart. Rank zero
is rejected by actual polynomial nonpersistence before weight divisions.
Its converse for at least six rows is not used. L125 provides provenance,
not a mathematical premise for the independently reconstructed exclusion.

The standard coding inputs are imported through L109: J. I. Hall,
*Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004, [accepted manuscript 2016-02-29,
section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2 and the shortening formula after Lemma 5.3.
There are sixteen distinct labels and k=8; every row shortens the seven
distinct labels J minus K from dimension eight to positive dimension
one, with nonzero products of label differences. Changed K={89,96}
alters coefficients without altering applicability. No general coding
theorem is reproved. Keith Conrad, [*Exterior Powers*, Theorems 4.2,
7.1, 7.5, pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
supplies exterior bases and the nonzero-wedge/plane association over any
field. L109 supplies the explicit Plucker criterion and pivot formulas.
J. S. Milne, [*Fields and Galois Theory*, Kea Books 2022, sections
1.6–1.9 pp. 5–7 and Proposition 2.17 p. 34](https://www.jmilne.org/math/Books/FT0.pdf),
supplies polynomial division and extension gcd identities.

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-20-new-pair-second-residual-locus-review.md`.
This is REPRODUCTION of the assessed locus/gate method for one changed
record. L126's audited method supplies no coefficients or outcomes here.
The scoped duplicate/source comparison found no completed matching
classification; no novelty or progress beyond those general sources is
claimed. ATTEMPTS/041–044 and every historical filter failure remain.

### Exact original matrix, provenance and complete extension kernel

For each row let g_j(X)=product_(y in J minus K_j)(X-y). On S form
the four covectors c_jx=g_j(z_j)E_x^*−g_j(x)E_zj^* for
x in S minus (I_j union {z_j}); stack their six exterior pairs.
This specifies every entry of the original matrix N. The full entries
are in `scripts/seven-coordinate/new-pair-second-residual-gates.json`.

An original nineteen-by-nineteen minor uses zero-based rows

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21

and columns

    0,1,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20.

Its integer determinant is

    −79930926190995594340952590526545920 = 9 modulo 97.

In increasing S-pair order B0 has its sole nonzero entry 1 in column
2, while B1 has nonzero entries

    p_(1,12)=15, p_(8,12)=84, p_(12,18)=73,
    p_(12,22)=63, p_(12,27)=62, p_(12,33)=1.

Both give zero at all 24 original rows; their entries in free columns
2,14 are the identity matrix. Thus rank(N)<=19 and the nonzero original
minor gives rank(N)>=19. They span the entire kernel. These identities,
the minor and independence persist over every field extension, proving
the complete extension kernel without rational-point sampling.

The historical record is uniquely selected as fourth_index=647 and
also bound to /cases/182 of `scripts/seven-coordinate/new-pair-filter/third-058.json`.
The shard SHA256 is
`5c22d06699cb5a500ffa8ccbbb5161c5652c7a0364ec4cb5aa412825ef87e3f9`.
The independently generated lexicographic 756-row universe
binom(S,2) times binom(J,2) gives the displayed third at 58 and fourth
at 647. The saved rank, original minor, complete basis and all original
residuals agree. No other occurrence is tested or deleted.

### Complete homogeneous locus and infinity

Write p=sB0+tB1. The complete set of 35 increasing-label homogeneous
relations p_ab p_cd−p_ac p_bd+p_ad p_bc has only these nonzero restrictions:

| Labels | Restriction |
| --- | --- |
| (1,8,12,18) | 84st |
| (1,12,18,22) | 34st |
| (1,12,18,27) | 35st |
| (1,12,18,33) | 96st |

Both B0 and B1 are explicit wedges, so all pure s² and t² coefficients
vanish. A mixed product must use the sole B0 pair (1,18) and a disjoint
B1 pair: precisely (8,12),(12,22),(12,27),(12,33). Their signs give
the four displayed coefficients; every other mixed coefficient is zero.
The programs independently check all 105 coefficients, including zeros.

Since 84 is nonzero, the common homogeneous zero set is exactly st=0.
In any extension field a nonzero projective pair therefore equals
[1:0] or [0:1]. Both points are decomposable. On s=1 the full affine
gcd is T; coefficientwise identities q_l=T Q_l and sum U_l q_l=T
are saved and replayed for all 35 restrictions. At s=0 every t²
coefficient is zero, explicitly retaining infinity. This is the entire
locus over extensions: there is no further empty, whole-line, repeated
or nonsplit branch. The two planes are L0=span(E_1,E_18) and
L1=span(E_12,w).

### All original-row gates and arbitrary prescribed charts

For L0 use u=E_1,v=E_18. For L1 use the canonical first-pivot basis

    u=(1,25,0,21,54,67,84), v=15E_12

on ordered S. Its wedge is exactly B1. In every row the projection
(Q_j u,Q_j v) has all six two-by-two minors zero and a nonzero
component, hence rank exactly one. At the first nonzero component n
put (alpha,beta)=(-Q_j v[n],Q_j u[n]) and h=alpha u+beta v.
Restore lambda=h_zj/g_j(z_j) and weights

    e_i=h_i−lambda g_j(i) (i in I_j),
    e_k=−lambda g_j(k) (k in K_j).

| Plane | Row | First nonzero (Q u,Q v) | (alpha,beta) | lambda | Weights on ordered I then K |
| --- | ---: | --- | --- | ---: | --- |
| L0 | 1 | (0,44) | (53,0) | 0 | (53,0,0,0) |
| L0 | 2 | (12,0) | (0,12) | 0 | (0,12,0,0) |
| L0 | 3 | (0,52) | (45,0) | 0 | (45,0,0,0) |
| L0 | 4 | (54,0) | (0,54) | 0 | (54,0,0,0) |
| L1 | 1 | (51,46) | (51,51) | 24 | (58,32,57,90) |
| L1 | 2 | (44,0) | (0,44) | 0 | (78,0,0,0) |
| L1 | 3 | (29,0) | (0,29) | 0 | (0,47,0,0) |
| L1 | 4 | (51,84) | (13,51) | 82 | (35,48,75,23) |

Every nonzero component and every weight is retained, including the two
full rows. For all eight entries h−e=lambda g_j at all sixteen H
labels, with h extended by zero off S, and
sum_(x in H) x^d(h_x−e_x)=0 for each d=1,...,8. All 128 pointwise
entries and 64 original shifted-moment residuals are checked. The
nonzero g_j values on S union K_j and all recovered h are saved.

L0 already fails row one: Q_1E_1=0 and Q_1E_18 has nonzero first
component 44, so the unique intersection is F E_1. Here z_1=12,
giving lambda=0 and zero outside weights. L1 fails row two:
Q_2v=0 and Q_2u has nonzero first component 44, so its intersection
is F E_12. Here z_2=1, again giving lambda=0. Both violate L109's
necessary full-error gate, independently of any other selected rows.

For any prescribed original basis
u_original=A u+B v, v_original=C u+D v, Delta=AD−BC!=0,
the first coefficient of h is

    alpha_original=(D alpha−C beta)/Delta.

Thus each table row retains its exact finite-direction condition
D alpha−C beta!=0. If it vanishes the direction is omitted from the
original finite chart. Otherwise the original error is e divided by
alpha_original, a nonzero rescaling that preserves all zero weights
and moments. The argument allows arbitrary nonrational A,B,C,D and
omitted direction; it never replaces that chart. No chart repairs
either plane's failed lambda gate.

### Complete same-step replay and qualifications

Reproduce from this notebook:

    python3 scripts/seven-coordinate/new_pair_second_residual_gates.py
    python3 scripts/seven-coordinate/verify_new_pair_second_residual_gates.py

The complete certificates are
`scripts/seven-coordinate/new-pair-second-residual-gates.json` and
`scripts/seven-coordinate/new-pair-second-residual-gates-replay.json`.
The producer directly evaluates g and original covectors, and checks
the original minor by modular and fraction-free integer elimination.
The independent verifier imports no producer helpers. At every retained
simple root of X^16−1 it instead uses

    g_j(x)=16x^15/product_(y in (S union K_j) minus {x})(x−y).

All factors are nonzero. Normalized ratio covectors are scaled back
to reconstruct all 504 original matrix entries, rather than merely an
equivalent matrix. Independent column elimination reconstructs the
complete kernel, and rational Gaussian elimination recomputes the
integer determinant with every row-swap sign. It then replays all
homogeneous coefficients, affine divisibility/Bezout identities, the
two endpoints, all projections, directions, lambdas, weights, finite
gates and all pointwise/moment identities above.

Every one of the seven nonzero exterior pivots is reconstructed, and
all 88 nonzero projection-component choices are checked. Each gives
a nonzero multiple of the same canonical intersection, lambda and
error weights, so no alternate pivot restores fullness. All checks
pass: actual/required loci 1/1, two complete points, eight rank-one
rows, six lambda-zero rows, two full rows and zero unresolved components.
The complete relevant data are replayed; a JSON preview is not proof.
The paths still share Python and residue arithmetic. This is a same-step
verification, not a separate critical audit or proof-assistant result.
Other residuals, representation, extraction, event completion and
challenge-definition qualifications remain unresolved.

### Separate critical audit, 2026-10-20

Step 2026-10-20-mca-366-second-residual-critical-audit used the unchanged
invocation-start EXPLORE assessment
`drafts/literature/2026-10-20-new-pair-second-residual-audit-review.md`.
It read this complete proof, both programs, every called helper body
and constant, L109's necessary direction and critical audit, and the
inherited L010/L103/L104 hypothesis and application passages. The scoped
duplicate check found the prior calculation and same-step replay, not a
separate audit of this occurrence. The ready primary-source coverage
above is reused; no new general theorem or novelty claim is made.

The L109 application is valid only after equality supplies full, distinct
actual errors. Its eight-column injectivity argument makes the lift
directions independent, so their wedge is nonzero. All four stated rows
are assumed actual; no support-extraction claim or four-row converse is
needed. The shortening set J minus K has seven distinct labels in every
row, including K={89,96}; every retained g-value is nonzero. L103 and
L104's inherited finite-certificate qualifications remain. No inactive
coordinate, lower-weight equality event or rational original chart is
silently introduced.

The producer's direct products give exactly the four original quotient
blocks, with the specified row and column orders. Its row elimination
selects independent original rows, and its modular and fraction-free
determinants account for each row-swap sign. The verifier's derivative
formula follows by differentiating X^16−1 at a retained simple root and
dividing by the other retained label differences; its use is confined
to S union K. Multiplying the normalized ratio covectors by g(z)g(x)
recovers the original covectors, not just equivalent equations.
Independent column elimination and rational Gaussian elimination check
all 504 matrix entries, the complete two-vector kernel and the exact
integer determinant above. The nonzero minor and independent null
vectors give both rank inequalities over every extension.

The full homogeneous computation includes all 35 relations and all 105
coefficients. Its nonzero restrictions are precisely the four displayed
multiples of st; the coefficient 84 cannot vanish in an extension of
F_97. Hence there are exactly the two stated projective points over
every extension. This conclusion does not use finite-field sampling or
assume rational descent of a general kernel. The affine certificate is
also exact: each restriction divides by T with the saved quotient, and
the only nonzero saved Bezout coefficient is 96 on the restriction 96T,
giving T since 96²=1 modulo 97. All t² coefficients vanish, so infinity
is included. Every called trim/add/scale/multiply/division/extended-gcd
routine was checked against these coefficient conventions.

Both reconstructed bivectors equal their claimed wedges. All eight
projected restrictions have rank exactly one, with every zero component
retained. Their unique intersection lines give the displayed lambda
values and all four recovered weights. The six lambda-zero rows and
two full rows are both retained; neither point passes all rows. All
128 pointwise codeword identities and 64 original shifted moments pass.
The verifier exhausts all seven nonzero exterior pivots and all 88
nonzero projection-component choices. Each reconstructed intersection,
lambda and error vector is a nonzero multiple of the canonical one.
The regenerated complete pivot records agree with the saved replay,
not merely its reported count.

For arbitrary original coefficients A,B,C,D, the change of basis sends
original coordinates (a,b) to (Aa+Cb,Ba+Db). Its inverse therefore gives
the first coordinate (D alpha−C beta)/(AD−BC) exactly as stated.
The nonzero determinant is the only change-of-basis denominator. A
zero first coordinate omits that line; a nonzero first coordinate
rescales its errors and preserves each zero weight. This algebraic
identity holds with nonrational coefficients. Thus no prescribed chart,
alternate pivot or extension-field component repairs either failed
lambda gate.

Fresh isolated reproduction:

    python3 -B scripts/seven-coordinate/audit_l127.py

The audit copies only the four reviewed programs, the exact source shard
and the two certificates into a temporary directory inside this notebook.
It runs only the one-occurrence producer and verifier with assertions
enabled, compares both complete outputs byte for byte, and checks the
full saved coefficient and row records. All 30/30 audit checks pass,
with zero failures; all seven original computation files remain unchanged.
The full audit certificate, including input hashes and subprocess results,
is `scripts/seven-coordinate/l127-critical-audit.json`. The original
certificates retain their historical same-step/pending-audit wording;
this later section supplies the separate audit verdict.

No mathematical defect or missing dependency was found. This validates
a reproduced restricted input, not a further exclusion or progress beyond
the assessed general sources. Both paths still share Python and residue
arithmetic; no proof-assistant verification is claimed. All 154 historical
residuals and ATTEMPTS/044 remain preserved. The argument and direct input
L109 are unchanged, so PROOF.md and DAG.md are not modified. No third/pair
assembly, universal representation/extraction or challenge solution follows
from this audit.

## Mathlib

Full matching coverage for this exact indexed classification: **not
checked**. Supporting coding, exterior, matrix-rank, polynomial-gcd and
finite-field coverage: **not newly checked**, not asserted absent.
Standard results are imported by the precise citations above; this
restricted reproduction retains explicit finite-certificate qualifications
and passed the separate step-366 critical audit recorded above.
