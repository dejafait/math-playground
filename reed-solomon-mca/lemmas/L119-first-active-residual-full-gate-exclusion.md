# L119 — The first active residual has two ineligible planes

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, dimension eight,
L010's shifted moments and the pinned same-support event for
1/4<=delta<5/16. The actual Hankel determinant and every actual
coordinate locator are nonzero polynomials. Both coefficient syndromes
belong to U_S for S={1,8,12,18,22,27,33}. Assume sixteen original finite
bad parameters and L104's t=0. Weights and the prescribed original chart
are arbitrary over F. Retain L109's inherited L010/L103/L104 scope and
finite-certificate qualifications. Suppose the following four supports
are actual two-overlap errors, with J=H minus S:

| Row | I subset S | K subset J |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,70} |
| 3 | {1,12} | {75,79} |
| 4 | {8,22} | {79,96} |

Use increasing S-pair columns and L109's original exterior blocks,
with z_j=min(S minus I_j) and lexicographic covector-pair rows.

## Conclusion

These hypotheses are inconsistent. The original four-row stack has rank
nineteen. Write E_x for the coordinate vectors on S and

    w=11 E_8+58 E_12+72 E_18+53 E_22+27 E_27+E_33.

Its entire decomposable projective kernel over every extension of F_97
consists of E_1 wedge w and E_8 wedge E_12. All eight selected-row
projections have rank one. The first plane passes the intrinsic full-weight
gates at rows two and four, but has lambda zero at rows one and three;
the second plane has lambda zero at all four rows. Both therefore fail
the necessary gates in every prescribed original chart.

This excludes exactly the named support family, identified in L116/L118
as occurrence (n,u)=(0,320). No third, fixed pair, arbitrary seven-set or
universal profile is excluded. All 599 historical factor-filter failures
and 239 activity-screen failures remain preserved. No residual census
is recomputed, and the global interval remains 11/q–16/q. Same-step
independent formula replay passes; the separate step-333 critical audit
found no defect in this restricted exclusion.

## Proof

### Imported inputs and applicability

Apply audited L109's necessary direction: the actual independent lift
coefficients give a nonzero decomposable kernel tensor, and each actual
row requires rank-one projection, nonzero lambda, two nonzero overlap
weights and a finite direction in the prescribed original chart. Its
nonpersistence argument rejects rank zero before any weight or chart
division. No converse for four rows, representation theorem or extraction
of these supports is used. L116/L118 provide historical identification;
the matrix, complete kernel and exclusion below are independently checked
from the displayed labels, so their partition conclusions are not inputs.

The standard coding inputs are imported through L109: J. I. Hall,
*Notes on Coding Theory*, GRS chapter,
[Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf);
I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, printed pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2, Lemma 5.3 and the following GRS shortening formula.
All sixteen evaluation labels are distinct and unit multipliers are
nonzero. Each row shortens exactly the seven labels J minus K_j,
retaining positive dimensions eight through one and nonzero products of
distinct label differences. The changed fourth support changes none of
these hypotheses. No standard coding theorem is reproved.

The invocation-start assessment was
`drafts/literature/2026-10-18-first-active-residual-gate-review.md`, EXPLORE.
This is REPRODUCTION of the assessed homogeneous L109 gate method on a
different complete kernel, not a novelty claim or a challenge resolution.
L112/L117's loci are comparisons only; their equations are not imported.

### Original matrix and complete kernel

Construct g_j(X)=product_(y in J minus K_j)(X-y) and the four covectors
c_jx=g_j(z_j)E_x^*−g_j(x)E_zj^*. Stack their six exterior rows to form
the original 24-by-21 matrix N. All 504 entries are saved in
`scripts/seven-coordinate/first-active-residual-gates.json`.
The minor using zero-based rows

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,20

and columns

    0,1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20

has integer determinant

    −19413570831084880785282562746937344,

which is 32 modulo 97. Every original row annihilates both

    B0=E_1 wedge w,    B1=E_8 wedge E_12:

all 48 residual entries are zero. Their columns 5 and 6 form the identity
matrix, so they are independent. The minor gives rank at least nineteen
and these two null vectors give rank at most nineteen. Hence they are
a complete kernel basis. These same base-field identities and nonzero
minor persist over every extension; this is not projective point sampling.

### Entire homogeneous Plucker locus

Write every nonzero kernel vector uniquely as p=s B0+t B1, with
(s,t)!=(0,0). Its only possibly nonzero entries are

    p_(1,8)=11s, p_(1,12)=58s, p_(1,18)=72s,
    p_(1,22)=53s, p_(1,27)=27s, p_(1,33)=s, p_(8,12)=t.

In the relation p_ab p_cd−p_ac p_bd+p_ad p_bc for increasing labels,
the only nonzero restrictions are at (1,8,12,x), for
x=18,22,27,33. They are respectively 72st, 53st, 27st, st.
Indeed, a product of two B0 entries repeats label 1; a product of two
B1 entries repeats 8 and 12; the only product with four distinct labels
is p_(1,x) p_(8,12) for these four x. Thus all other 31 relations
vanish identically. All 35 are independently calculated coefficientwise.

Over any field extension the common zero condition is exactly st=0.
Conversely both B0 and B1 are explicit nonzero wedges. L109's proved
Plucker criterion therefore gives precisely [s:t]=[1:0] and [0:1],
including infinity and every extension-field point. There is no residual
quadratic branch or identically vanishing system. The associated planes
are L0=span(E_1,w) and L1=span(E_8,E_12), both defined over F_97.

### Every selected-row gate and the prescribed chart

For L0 use u=E_1,v=w; for L1 use u=E_8,v=E_12, exactly the L109
pivot reconstructions. For each row the complete certificate gives Q_j u,
Q_j v and all six projection minors. They all vanish, and the following
table records their first component pair; at least one entry is nonzero,
so every projection has rank exactly one. No rank-zero case remains.
Choose the intersection representative h=alpha u+beta v by
(alpha,beta)=(-Q_j v[n],Q_j u[n]) at the first nonzero component n.
Restore lambda=h_z/g_j(z) and the four error weights by L109's formula.

| Plane | Row | First (Q u,Q v) | (alpha,beta) | lambda | Weights on ordered I then K |
| --- | ---: | --- | --- | ---: | --- |
| L0 | 1 | (0,22) | (75,0) | 0 | (75,0,0,0) |
| L0 | 2 | (38,16) | (81,38) | 86 | (30,87,31,91) |
| L0 | 3 | (0,69) | (28,0) | 0 | (28,0,0,0) |
| L0 | 4 | (34,64) | (33,34) | 39 | (21,96,75,37) |
| L1 | 1 | (0,16) | (81,0) | 0 | (0,81,0,0) |
| L1 | 2 | (72,0) | (0,72) | 0 | (72,0,0,0) |
| L1 | 3 | (6,0) | (0,6) | 0 | (0,6,0,0) |
| L1 | 4 | (0,68) | (29,0) | 0 | (29,0,0,0) |

These representatives describe the entire unique intersection line in
each case, rather than selected samples. Both overlap weights and both
outside weights are retained, including zeros. On all sixteen H labels
the restored vectors satisfy h−e=lambda*g_j; all eight original shifted
moment differences sum_x x^d(h_x−e_x), d=1,...,8, are zero. The full
128 pointwise identities and 64 moment residuals are saved and replayed.
The two full rows on L0 are preserved as intrinsic successes; they do
not repair the failures at its other rows.

More directly, at row one Q_1 E_1=0 while Q_1 w has first entry 22,
so L0 intersects ker(Q_1) precisely in F E_1. Similarly Q_1 E_8=0
and Q_1 E_12 has first entry 16, giving intersection F E_8 for L1.
Since z_1=12, both lines have lambda zero. Their restored errors have
three zero entries and fail L109's full-weight gates. This already
excludes both planes, with the remaining rows completely retained above.

For an arbitrary prescribed basis write
u_original=A u+B v, v_original=C u+D v with AD−BC!=0, over F or
any extension. The first coefficient of h is

    alpha_original=(D alpha−C beta)/(AD−BC).

Thus each row is finite exactly when D alpha−C beta!=0. The table gives
the exact linear gate for every row. If it vanishes, that row cannot
be an original finite event. Otherwise divide h and e by
alpha_original: the moment identities persist, and every zero lambda
and zero weight remains zero. A nonrational prescribed omitted point
is allowed; no replacement chart is chosen. Both possible planes
therefore fail necessary gates in every chart, proving the contradiction.

### Verification and limitations

Reproduce from this notebook:

    python3 scripts/seven-coordinate/first_active_residual_gates.py
    python3 scripts/seven-coordinate/verify_first_active_residual_gates.py

The full producer certificate is
`scripts/seven-coordinate/first-active-residual-gates.json`; the complete
same-step replay is
`scripts/seven-coordinate/first-active-residual-gates-replay.json`.
The producer binds the exact L118 audit record and its SHA-256, then
rebuilds the original matrix from products of label differences, checks
both null vectors, and evaluates the rank minor by modular elimination
and exact fraction-free integer elimination. It applies the existing
L109 pivot/gate implementation to both endpoints only after proving
the complete homogeneous locus coefficientwise.

The verifier imports no producer or producer helpers. It generates H
by powers of 8 and obtains g_j(x) on S union K_j from
16*x^15/product_(y in (S union K_j) minus {x})(x-y). This follows by
differentiating X^16−1=g_j(X)*product_(y in S union K_j)(X-y) at x.
Every denominator is nonzero. Normalized ratio covectors, rescaled by
g_j(z)*g_j(x), rebuild every original entry. Fraction-based rational
elimination reproduces the integer minor and residue 32. Explicit
coefficient multiplication checks all 35 quadrics; the two independently
specified plane bases reconstruct every projection, intersection, lambda,
weight, prescribed finite gate, pointwise identity and shifted moment.
All checks pass, with zero unresolved branches or discrepancies.

Both paths still share Python, exact arithmetic, residue field and the
same mathematical formulas; that replay was same-step verification. The
separate critical audit below is not proof-assistant verification. Historical
screen failures are preserved. The calculation supplies one local input,
with no four-row converse, original nonpersistence construction, t=0
realization or sixteen-event completion. Arbitrary t=0 profiles, universal
representation/fixed-pair extraction and challenge qualifications remain
open. It does not improve 11/q–16/q.

### Separate critical audit, 2026-10-19

Step `2026-10-19-mca-333-first-active-residual-critical-audit` checked the
full proof, both programs and every called helper against the unchanged
EXPLORE assessment
`drafts/literature/2026-10-18-first-active-residual-audit-review.md`.
It reused L109's necessary-direction proof and separate audit, including
the inherited L010/L103/L104 finite-certificate qualifications. No
mathematical defect, changed argument or new dependency was found.
This validates an existing reproduced local input; it is not a new
indexed exclusion or progress beyond the sources checked.

The actual sixteen-event hypothesis is used before invoking L109's
independent nonzero wedge and full-weight gates. The four displayed
supports need only be actual selected rows. Neither L086 incidence
extraction nor L109's converse for six or more rows is used. L116/L118
remain historical identification only: the conclusion follows from the
four named supports and their independently reconstructed matrix.

A fresh coefficient-polynomial/Horner construction reproduces all four
quotient matrices and all 504 original exterior entries. Full reduced
row elimination gives exactly nineteen pivots and free columns 5,6,
recovering the complete displayed basis. The original two null vectors
have the identity in those free columns; the displayed original minor
has the exact integer determinant above and nonzero residue 32. Both
producer and independent replay rerun successfully, and both complete
certificates reproduce byte for byte. All seven selected program/input/
artifact hashes are unchanged. Thus no historical partition was replaced
or recomputed by this audit.

The homogeneous argument was checked independently of any sampled
projective points. Two B0 entries always share label 1, and two B1
entries repeat labels 8 and 12. A surviving mixed product must therefore
use (1,x) and (8,12), with x in {18,22,27,33}; its sign is positive in
the ordered quadruple (1,8,12,x). This gives exactly the four displayed
st coefficients, the last one equal to one, and all other coefficients
zero. Consequently st=0 is necessary and sufficient over every field
extension, with both endpoints explicit nonzero wedges. Rank and kernel
completeness persist under scalar extension by the same minor and basis
identities. No unexamined quadratic component or infinity point remains.

All entries of the eight-row printed table match the complete independent
replay. Each projected matrix has zero two-by-two minors and a nonzero
first component pair, so its rank is exactly one. The stated
(-Qv[n],Qu[n]) is nonzero and gives its unique kernel direction. Lambda
is restored at the nonzero g(z), without dividing by lambda. The six
lambda-zero rows each retain three zero weights; the two full rows have
all four weights nonzero. Every one of the 128 pointwise codeword
identities and 64 original shifted moments was checked. The full rows
are intrinsic successes only, not a four-row recovery pencil.

For the chart check put Delta=AD−BC. Besides
alpha_original=(D alpha−C beta)/Delta, the second coefficient is
beta_original=(-B alpha+A beta)/Delta. Substituting the two displayed
original basis vectors gives coefficient alpha on u and beta on v,
identically in arbitrary extension-field A,B,C,D. If alpha_original=0,
the unique row direction is the omitted point and cannot be an actual
finite event. Otherwise rescaling by its inverse multiplies lambda and
every error weight by the same nonzero scalar, so every zero persists.
In particular each plane's first-row failure excludes every prescribed
chart, including a nonrational omitted direction. No chart sampling or
choice of a replacement chart supports this conclusion.

Reproduce the separate audit with
`python3 scripts/seven-coordinate/audit_first_active_residual.py`.
Its complete evidence is
`scripts/seven-coordinate/first-active-residual-critical-audit.json`;
all 42 completeness, transcription and replay checks pass with zero
failures and zero unresolved branches. The saved before-hash record is
`scripts/seven-coordinate/first-active-residual-critical-audit-before.json`.
The audit retains the shared Python/exact-arithmetic limitation. Only
this named support family is excluded; all historical 599/239 screen
failures remain preserved, with this certified exception recorded
separately. Arbitrary t=0 profiles, universal representation/fixed-pair
extraction, challenge qualifications and the global 11/q–16/q gap remain.

## Mathlib

Full matching indexed exclusion: **not checked**. Supporting matrix-rank,
exterior-square, Plucker and finite-field results: **not checked**.
Unknown coverage is not absence. The standard coding results are
imported through L109 with the precise citations and hypotheses above.
The explicit exact finite-certificate qualification remains part of this
local result; its separate step-333 critical audit found no defect.
