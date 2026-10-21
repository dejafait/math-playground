# L117 — First rank-19 residual has only two ineligible planes

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, dimension eight,
L010's shifted moments and the pinned same-support event on
1/4<=delta<5/16. The actual Hankel determinant and every coordinate
locator are nonzero polynomials. Both coefficient syndromes belong to
U_S for S={1,8,12,18,22,27,33}. Assume sixteen original finite bad
parameters and L104's t=0. Weights and the prescribed original chart
are arbitrary over F. Retain L109's inherited L010/L103/L104 and
finite-certificate qualifications. Suppose these four supports are
actual two-overlap errors, with J=H minus S:

| Row | I subset S | K subset J |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,70} |
| 3 | {1,12} | {75,79} |
| 4 | {8,18} | {75,85} |

Use L109's original exterior blocks, increasing S-pair columns,
z_j=min(S minus I_j), and lexicographic covector-pair rows.

## Conclusion

These hypotheses are inconsistent. The four-row stack has rank 19.
Its complete projective decomposable kernel consists of exactly
E_1 wedge E_18 and E_8 wedge E_12, up to nonzero scalar, over every
extension of F_97. Each plane has rank-one projection at each selected
row, but its unique recovery has lambda zero and three zero error
weights. Thus no prescribed original chart makes any of these row
recoveries full.

This excludes exactly the named four-support family, recorded as
L116's historical indexed occurrence (n,u)=(0,279). It does not exclude
its third, its fixed pair, arbitrary t=0 profiles or other seven-sets.
The historical 599 sufficient-filter failures remain preserved: this
result certifies one of them separately, without recomputing a census
or claiming a new residual total. No global bound improves. Same-step
independent replay and the separate step-325 critical audit pass.

## Proof

### Imported gates and scope

Use audited L109's necessary direction. The actual lift coefficients
are independent, their wedge is a nonzero kernel tensor, and every
actual selected row must have rank-one projection, nonzero lambda,
both nonzero overlap weights and a finite direction in the prescribed
chart. All field, shortening and nonpersistence hypotheses are exactly
those above. No r>=6 converse or extraction of the four supports is
used. L114/L116 identify the historical record; their partition
conclusions are not needed for the independent calculation here.

The standard coding inputs are imported through L109: J. I. Hall,
*Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, printed pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2, Lemma 5.3 and the following GRS shortening formula.
The evaluation points are distinct, the multipliers are nonzero and
dimension is eight. Each selected row shortens exactly seven labels
J minus K_j, retaining positive dimension and nonzero products of
label differences at every step. These hypotheses are unchanged by
the chosen third and fourth rows. No standard distance or shortening
theorem is reproved.

The ready EXPLORE assessment at invocation start was
`drafts/literature/2026-10-18-first-rank19-factor-residual-review.md`.
This is REPRODUCTION of the assessed L109/L112 projective gate
mechanism on one different complete kernel, with new local finite
certificates. It is not a claim of originality or a result beyond the
checked literature. In particular, L112's quadratic system is not
assumed to describe this kernel: the present system is calculated.

### Complete kernel and rank witness

Let E_x denote the coordinate vector on S. Construct
g_j(X)=product_(y in J minus K_j)(X-y) and L109's covectors
c_jx=g_j(z_j)E_x^*−g_j(x)E_zj^*. Stack their six exterior rows.
The resulting 24-by-21 matrix N is saved in
`scripts/seven-coordinate/first-rank19-full-gates.json`.
Its minor with zero-based row indices

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,20

and column indices

    0,1,3,4,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20

has integer determinant

    −1442234786736581438195068452790272,

which is 27 modulo 97. The vectors

    B0=E_1 wedge E_18,  B1=E_8 wedge E_12

are zero against every original row: all 48 residual entries vanish.
Their respective columns 2 and 6 form the identity matrix, proving
independence. The minor gives rank at least nineteen and the two
independent null vectors give rank at most nineteen; hence they form
the complete kernel. The same nonzero minor, zero residuals and
identity coordinates prove completeness after every scalar extension.

### Full homogeneous locus

Every nonzero kernel tensor is uniquely p=s*B0+t*B1 with (s,t)!=(0,0).
All 35 homogeneous Plucker restrictions are computed coefficientwise
in the order (s^2,st,t^2). The restriction at labels (1,8,12,18) is

    p_(1,8)*p_(12,18)−p_(1,12)*p_(8,18)+p_(1,18)*p_(8,12)=st.

All other restrictions vanish identically: only the pair coordinates
(1,18) and (8,12) can be nonzero, and a product of these occurs only
in the displayed quadruple. Therefore decomposability requires st=0.
Conversely B0 and B1 are explicit wedges, so the entire projective
locus is exactly [s:t]=[1:0] or [0:1] over every extension field.
This includes infinity and all zero-coordinate branches. There is no
identically zero system, quadratic extension branch or untested point.
The two planes are L0=span(E_1,E_18) and L1=span(E_8,E_12).

### All selected-row gates and arbitrary original charts

For each of these coordinate planes and each row, exactly one of its
two coordinate labels c lies in I_j. The other label d lies in
O_j=S minus I_j. Thus Q_j E_c=0, whereas Q_j E_d!=0: the latter
follows directly from c_jx, since g_j(z_j)!=0, including the case
d=z_j. The projection has rank exactly one, never zero, and the
unique intersection L intersect ker(Q_j) is the line F*E_c.
There are consequently no rank-zero branches left on this locus.

For h=a E_c with a!=0, z_j differs from c, so the restored formula is

    lambda=h_zj/g_j(z_j)=0,
    e_c=a, e_i=0 for the other i in I_j,
    e_k=0 for both k in K_j.

These fail the nonzero-lambda and full-weight gates of L109. The
following complete replay table records one nonzero representative
h=a E_c for every point and row; the scalar is not a sampling choice,
because the unique intersection line has already been proved.

| Plane | Row | c | a |
| --- | ---: | ---: | ---: |
| L0 | 1 | 1 | 53 |
| L0 | 2 | 18 | 38 |
| L0 | 3 | 1 | 4 |
| L0 | 4 | 18 | 89 |
| L1 | 1 | 8 | 81 |
| L1 | 2 | 12 | 72 |
| L1 | 3 | 12 | 6 |
| L1 | 4 | 8 | 65 |

Every error including its zero coordinates is retained. For these
representatives h-e is identically zero on H, hence all eight original
shifted moments vanish, coefficientwise for every scalar multiple.
This is a failed full recovery, not a projected success counted as
an actual four-error.

To keep the prescribed chart explicit, let u,v be the coordinate
basis of L0 or L1 and write h=alpha*u+beta*v. Every prescribed basis
has u_original=A*u+B*v, v_original=C*u+D*v with AD−BC!=0, permitting
arbitrary extension-field entries. Its first coefficient is
(D*alpha−C*beta)/(AD−BC). If D*alpha−C*beta=0 the direction is
omitted and cannot be a finite event; otherwise dividing the restored
error by this first coefficient leaves its three zero weights zero.
Thus neither a nonrational omitted point nor a change of basis repairs
the intrinsic failure. No replacement chart is chosen. Both possible
planes fail the necessary gates, proving the contradiction.

### Exact reproduction and limitations

From the notebook run:

    python3 scripts/seven-coordinate/first_rank19_full_gates.py
    python3 scripts/seven-coordinate/verify_first_rank19_full_gates.py

The first program reconstructs the original matrix, evaluates the minor
both modulo 97 and by integer fraction-free elimination, checks both
complete kernel vectors, all homogeneous quadratic coefficients and
all eight selected-row gates, and saves the complete certificate above.
The historical source is identified by path, SHA-256 and `/cases/3`;
its basis is checked against the independently reconstructed matrix.

The verifier imports no producer/helper routines. At x in S union K
it reconstructs g_K(x) as

    16*x^15 / product_(y in (S union K) minus {x})(x-y).

This is the derivative at the simple root x of
X^16−1=g_K(X)*product_(y in S union K)(X-y). All denominators are
nonzero and 97 does not divide sixteen. It constructs normalized ratio
covectors and scales them back by the exact nonzero g_K(z)g_K(x),
then compares all 504 exterior entries. Rational Gaussian elimination
of the minor gives the identical integer determinant by a distinct
arithmetic path. All 35 homogeneous coefficients, both coordinate
planes, eight rank-one restrictions, recovered errors, 64 moment
residuals, 128 pointwise identity entries and prescribed finite-gate
coefficients agree. Its complete evidence is
`scripts/seven-coordinate/first-rank19-full-gates-replay.json`.

Both programs finish with no failures. They still share Python and
residue arithmetic; this is same-step replay, not a separate critical
proof/program audit or proof-assistant verification. The independent
global gaps and inherited finite-computation qualifications remain.
ATTEMPTS/041–042's rank-only and label-1-only obstructions are preserved;
failure of the eight whole-kernel factor tests is compatible with
this two-point decomposable locus and does not imply feasibility.

### Separate critical audit, 2026-10-18

Step 2026-10-18-mca-325-first-rank19-critical-audit found no defect in
the stated restricted exclusion. It used the unchanged ready assessment
`drafts/literature/2026-10-18-first-rank19-full-gates-audit-review.md`,
read the whole proof, L109's necessary-gate proof and its prior audit,
both complete programs and every called helper path. No new theorem,
support exclusion, coding reproof or dependency is introduced. This
validates the existing reproduced input, not a result beyond the
literature checked. L109's inherited computational qualifications remain.

The original matrix bridge was checked entry by entry in the complete
independent replay. On S union K, the derivative identity uses exactly
sixteen distinct roots of X^16-1. Its denominator is the product over
the other eight labels of S union K, so it is nonzero, and 16 is
nonzero in characteristic 97. Multiplying the ratio covector by
g(z)g(x) gives precisely g(z)E_x^*-g(x)E_z^*. Thus the verifier checks
the original exterior matrix, rather than merely a matrix with the same
rank. All four blocks, twenty-four rows and twenty-one columns are
present. The specified original minor is independently evaluated by
rational Gaussian elimination; it matches the integer fraction-free
determinant and its nonzero residue 27. The two distinct coordinate
unit vectors have all forty-eight original residuals zero and identity
coordinates at columns 2 and 6. These upper and lower rank witnesses
establish the full kernel over every extension, not just its dimension
at sampled points.

All thirty-five restrictions have three homogeneous coefficients; the
only nonzero one is st at (1,8,12,18). Over any field, st=0 implies
s=0 or t=0. Both nonzero endpoints are explicit wedges, proving both
necessity and sufficiency of the saved two-point locus. No affine chart,
root search, quadratic solver or assumption that a rank drop implies
decomposability enters this conclusion.

For each of the eight plane/row combinations, exactly one coordinate
label c is in I and the other d is in O. Q E_c=0. If d differs from z,
the covector indexed by d evaluates to g(z)!=0 on E_d; if d=z,
every covector indexed by x in O minus {z} evaluates to -g(x)!=0.
Thus the restriction has rank exactly one in both cases and its kernel
is precisely the c-coordinate line. This checks the rank-zero issue
directly; it does not discard that branch by division. The restored
lambda vanishes because h_z=0, and the four saved error weights consist
of the one nonzero h_c and three zeros. The full replay reproduces all
eight representatives in the displayed table. Their pointwise h-e=0
identities hold at all sixteen labels, proving all eight shifted moments
for every scalar multiple, including extension-field multiples. These
are failed full-weight recoveries, not actual four-error witnesses.

The prescribed-chart formula follows by inverting the matrix with
columns (A,B) and (C,D): the first original coefficient of h is
(D alpha-C beta)/(AD-BC). Its denominator is nonzero by the basis
hypothesis. A zero numerator omits the direction; a nonzero numerator
only rescales the same error, preserving its three zero weights.
This handles every extension-field chart and does not replace the
original omitted direction. Only L109's necessary direction is used;
its r>=6 converse cannot be applied to these four rows and is not used.

Reproduce the audit from the notebook with

    python3 scripts/seven-coordinate/audit_first_rank19_full_gates.py

This invokes both original programs in order, checks complete artifact
hashes against `scripts/seven-coordinate/first-rank19-critical-audit-before.json`,
and checks explicit collection lengths, written minor indices and value,
all locus coefficients, both endpoints, all eight representatives,
all sixty-four moments, all 128 pointwise entries and chart conventions.
The extra length checks ensure that the programs' zipped comparisons
have not omitted any saved point, block or row. The original independent
verifier checks all 504 matrix entries and every reconstructed gate;
the audit wrapper is not a third independent algebra implementation.
All 34 additional checks pass. Complete run output, check results and
before/after hashes are in
`scripts/seven-coordinate/first-rank19-critical-audit.json`.
The four inspected programs/helpers, both complete certificates and
the historical source artifact reproduce unchanged (seven hashes).

The full historical /cases/3 record agrees with (0,279), its four
supports, complete basis and original residuals. All eight old factor
tests remain false and its historical status remains unresolved;
this audit does not rewrite the old sufficient-filter evidence. Its
provenance does not import L116's census as a mathematical premise.
ATTEMPTS/041–042 remain valid. The two arithmetic paths share Python
and residue arithmetic, with no proof-assistant verification claimed.
No other occurrence, third, fixed pair, universal extraction claim or
global error bound was tested or established in this audit.

## Mathlib

Full matching theorem for this exact four-row exclusion: **not checked**.
Supporting exterior, finite-field and matrix-rank coverage is not
newly checked. The standard coding inputs are imported with their
precise citations and hypotheses through L109. Unknown coverage is
not absence. The local matrix/gate certificate has the computational
qualification above; no formal verification or originality is claimed.
