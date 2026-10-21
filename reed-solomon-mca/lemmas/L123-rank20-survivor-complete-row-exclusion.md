# L123 — Complete row census excludes L122's three planes

## Hypotheses

Use L109's necessary equality setting: F=F_(97^20),
H={x in F_97^*:x^16=1}, k=8, shifted moments of orders one through
eight, and the pinned same-support event for 1/4<=delta<5/16.
Assume sixteen actual original finite bad parameters, actual nonzero
Hankel determinant and coordinate-locator polynomials, L104's t=0,
and both coefficient syndromes represented on
S={1,8,12,18,22,27,33}. Retain L010/L103/L104's inherited
finite-certificate qualifications. Weights and the prescribed original
chart are arbitrary over F. No universal representation or fixed-pair
extraction is assumed.

Consider exactly L122's three audited planes, in increasing S order:

| Plane | Historical indices | u | v |
| --- | --- | --- | --- |
| P | (60,666), (295,197) | (1,0,63,89,39,19,65) | (0,69,54,33,34,52,35) |
| Q | (65,671), (300,202) | (1,0,68,64,39,19,65) | (0,69,6,79,34,52,35) |
| R | (145,696), (314,382) | (1,0,92,9,95,30,27) | (0,14,21,51,39,82,90) |

In an indexed application, all four selected supports of that L122
record must be actual equality error supports. Its complete rank-twenty
kernel then forces this plane. Exchanged third/fourth rows remain
separate indexed occurrences.

## Conclusion

For each plane, all 756 supports I union K with I in binom(S,2) and
K in binom(H minus S,2) give precisely four rank-one projections, all
passing the lambda and full-weight gates, and 752 rank-two projections.
There are no rank-zero projections or rank-one failed-weight rows.
The four successful directions are distinct and are exactly the four
selected supports already displayed in L122:

| Plane | I; K | Normalized (alpha,beta) |
| --- | --- | --- |
| P | 1,8; 47,50 | (1,87) |
| P | 12,18; 64,70 | (1,49) |
| P | 1,33; 64,79 | (1,10) |
| P | 22,27; 64,85 | (1,58) |
| Q | 1,8; 47,50 | (1,87) |
| Q | 12,18; 64,70 | (1,49) |
| Q | 1,33; 70,79 | (1,81) |
| Q | 22,27; 70,85 | (1,24) |
| R | 1,8; 47,50 | (1,28) |
| R | 12,18; 64,70 | (1,96) |
| R | 8,33; 70,79 | (1,34) |
| R | 22,33; 50,85 | (1,27) |

Thus every prescribed original chart has at most four full finite
two-overlap directions, eight below L109's necessary twelve. All three
planes, and hence exactly the six specified L122 occurrences, are
excluded from equality. No third or fixed pair is excluded. Historical
599/239 partitions are preserved. Other profiles, universal extraction
and challenge qualifications remain open; the global interval stays
11/q–16/q. Complete same-step independent replay and the separate
step-349 critical proof/program audit below pass.

## Proof

### Imported tools and applicability

Use L109's necessary arbitrary-row criterion and its threshold
r=12+n_0>=12, and L122's separately audited complete kernels, bases,
six indices and arbitrary-basis inversion. L121 supplies an inspected
implementation pattern only; none of its counts is imported. The
invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-19-rank20-survivor-completion-review.md`.
This is REPRODUCTION of covered methods with new finite inputs, not
progress beyond the sources checked or a new coding/exterior theorem.

The standard inputs are imported through L109: J. I. Hall,
*Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf);
I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004, [accepted manuscript 2016-02-29,
section 5, printed pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2 and the GRS shortening formula after Lemma 5.3;
and Keith Conrad, *Exterior Powers*, [Theorems 4.2, 7.1, 7.5,
printed pp. 11–12, 23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf).
Sixteen distinct labels, nonzero multipliers and dimension eight are
unchanged. Every row shortens the seven distinct labels
(H minus S) minus K, reducing dimension eight to one through positive
dimensions and nonzero products of label differences. Exterior degree
two in dimension seven and the field hypotheses are unchanged; the
complete planes are already supplied by L122. No general theorem is
reproved. The new scripts are essential to certify these three specific
finite counts, which neither those sources nor L121 supplies.

### Complete quotient calculation

Reproduce from the notebook:

    python3 scripts/seven-coordinate/rank20_survivor_full_rows.py
    python3 scripts/seven-coordinate/verify_rank20_survivor_full_rows.py

The full certificates are
`scripts/seven-coordinate/rank20-survivor-full-rows.json` and
`scripts/seven-coordinate/rank20-survivor-full-rows-replay.json`.
The producer checks successful step-345 audit executions and every
audit check, its unchanged before/after manifest, the two L122 artifact
hashes and audited program/helper hashes. It binds those two artifacts
and the audit certificate before and after this calculation. The
verifier independently checks the input hashes and each plane's bases
at both exact historical indices. The producer also checks exchange
of rows three and four, including every saved row gate. No old artifact
or historical partition is rewritten.

Put J=H minus S. Enumerate all 21 increasing I pairs and 36 increasing
K pairs, I outermost, with no incidence prefilter. For each row set
g_K(X)=product_(y in J minus K)(X-y), z=min(S minus I), and use the four
L109 covectors c_x(w)=g_K(z)w_x-g_K(x)w_z for
x in S minus (I union {z}). All g_K values on S union K are nonzero.
Save the full Q, Qu, Qv and six projection minors. A nonzero minor
certifies rank two; zero minors with a nonzero entry certify rank one.
The rank-zero branch is explicit and would contradict actual
nonpersistence by L109's whole-plane argument, rather than merely
reject one optional row. No rank-zero branch occurs.

At rank one choose the first nonzero component pair m and set
(alpha,beta)=(-(Qv)_m,(Qu)_m), h=alpha*u+beta*v.
Compute lambda=h_z/g_K(z),
e_i=h_i-lambda*g_K(i) for i in I, and
e_k=-lambda*g_K(k) for k in K. Extend h by zero off S and e by zero off
I union K. Every rank-one row saves all four weights, lambda, all sixteen
identities h_x-e_x=lambda*g_K(x), and all eight original shifted moments
sum_(x in H)(h_x-e_x)x^d=0, d=1,...,8. Lambda zero and either canceled
overlap weight are retained as failed gates, without division by them.

Exactly four rows per plane have rank one, with nonzero lambda and
all four weights. Their raw directions, lambdas and weights agree
entrywise with L122's four selected-row entries; normalization gives
the table above. All 752 other rows per plane have nonzero projection
minors and no nonzero intersection direction. Successes are grouped
by normalized projective direction, retaining duplicate groups; none
are duplicated. Therefore each complete pre-chart count is four.

### Independent original-moment replay and extension completeness

The replay imports neither producer nor producer helpers. It constructs
H from powers of eight, checks the complete 756 distinct row universe,
and reconstructs g_K by coefficient multiplication and Horner evaluation
instead of the producer's direct products. Every Q entry, projected
vector and projection minor agrees.

For every row, including all rejections, it independently constructs
the original eight-by-six matrix with row d=1,...,8 equal to

    (sum_(x in S) u_x*x^d, sum_(x in S) v_x*x^d,
     -i1^d, -i2^d, -k1^d, -k2^d).

Its variables are (alpha,beta,e_i1,e_i2,e_k1,e_k2). Reverse-column-pivot
Gauss–Jordan elimination saves the complete reduced matrix, pivot list,
nonzero pivot values, eight-by-eight left multiplier E and complete
null basis. Every step is a row swap, nonzero scaling or row addition,
so E is invertible over every extension. The full identity E*M=R is
checked, as are the identity on pivot columns and zero remaining rows.
The null vectors have identity free coordinates and satisfy all eight
original equations. Their number is six minus rank, so the kernel
basis is complete. The four error columns independently have rank
four, excluding any pure-error nonzero kernel direction.

For each plane the exact original-matrix ranks are six on 752 rows
and five on four rows, agreeing with quotient rank plus four. Each
rank-six kernel is zero. Each rank-five kernel is its complete unique
line and agrees, up to one nonzero common scale, with all six recovered
coefficients from the quotient calculation. The replay independently
checks the sixteen coordinate identities, eight moments, lambda and
all weight/chart gates, and every nonzero projection-pivot choice.
Every success group and complete disposition count agrees. There are
zero failures or unresolved branches in either complete certificate.

All entries and nonzero pivots lie in F_97. The same invertible row
operations therefore certify the ranks and complete kernels after
extension to F_(97^20), indeed every extension. Nonprime weights or
directions cannot create a kernel at a rejected row or another
projective solution at a rank-five row. This is not base-field sampling.

The initial producer stopped before processing any plane because its
audit adapter expected L120's `replay_returncode` field instead of
L122's `executions` list. Its full failed certificate is preserved as
`scripts/seven-coordinate/rank20-survivor-full-rows-first-schema-failure.json`.
The adapter now checks both actual successful executions; no
mathematical disposition was changed. The full producer and replay
then completed successfully. Both still share Python, residue
arithmetic and the moment convention; the separate audit below retains
these computational qualifications.

### Arbitrary prescribed chart and exclusion

Write u_original=A*u+B*v, v_original=C*u+D*v,
Delta=AD-BC nonzero over F. L122's audited inversion gives
alpha_original=(D*alpha-C*beta)/Delta. A row is original-finite exactly
when D*alpha-C*beta is nonzero. In that case divide h, lambda and e by
alpha_original, obtaining the original parameter
(-B*alpha+A*beta)/(D*alpha-C*beta). This preserves every nonzero weight
and distinct projective direction. Otherwise that direction is omitted.
All twelve gates in the table remain explicit; no prescribed chart
is rationalized. Chart deletion cannot increase four to twelve.

L109 requires at least twelve distinct actual finite two-overlap
directions at t=0 equality, so none of these three planes can occur.
L122's complete one-dimensional kernels force precisely these planes
at the six specified occurrences over every extension, proving their
restricted exclusion. Four selected recoveries are never used to
construct nonpersistence or invoke L109's r>=6 converse. No remaining
equality events, third/pair exclusion or global bound is inferred.
ATTEMPTS/041–043 remain valid stop evidence for their respective filters;
the present test uses the independently specified additional-direction
threshold. This ends the approved three-plane census.

### Separate critical audit, 2026-10-19

Step `2026-10-19-mca-349-rank20-full-row-critical-audit` used the unchanged
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-19-rank20-full-row-exclusion-audit-review.md`.
The full proof and both self-contained programs, including all called
mathematical and provenance functions, were inspected. L109's necessary
criterion and twelve threshold and L122's exact planes, indices and
separate step-345 audit were checked within their stated scopes. The
saved primary extractions cited above are reused; no general theorem
was reproved and no additional census was undertaken.

Reproduce the separate audit from the notebook:

    python3 scripts/seven-coordinate/audit_rank20_full_rows.py

Its complete certificate is
`scripts/seven-coordinate/rank20-full-rows-critical-audit.json`, with
producer/verifier output in
`scripts/seven-coordinate/rank20-full-rows-critical-audit.log`.
All 28 aggregate audit checks and all enclosed row checks pass. Both
complete programs succeed and reproduce their saved certificates byte
for byte. Every bound L122 artifact, audited program/helper hash and
the preserved pre-row schema failure remains unchanged. The repaired
adapter checks the two actual successful L122 executions, all 54 audit
checks and the before/after manifest. The preserved failed certificate
has exactly the missing `replay_returncode` key and no processed planes;
the current adapter and both full successful executions are checked,
rather than assuming the earlier L121 repair applies here.

The replay covers every ordered pair of an increasing I subset S and
an increasing K subset J, with 21*36=756 rows per plane. Every covector,
projection, minor, first pivot and disposition is recomputed. All twelve
successes retain every nonzero projection pivot, lambda, error weight,
sixteen coordinate identities and eight shifted moments. The additional
audit parses both printed tables, checks every basis, support and
normalized direction, and binds each raw recovery to L122. It checks
both historical indices of every plane and the full exchange of rows
three and four and their gates. No selected-row implication is substituted
for full coverage.

Independently of the replay's elimination routine, the audit reconstructs
all 2,268 original eight-by-six moment matrices. For each saved left
multiplier E it computes an exact integer determinant using fraction-free
elimination, checking every exact division, and verifies that the residue
modulo 97 is nonzero. It checks the complete identity E*M=R, all nonzero
pivot values, the identity on pivot columns, and every zero remaining
row. It checks every null vector in all original equations, and the
identity of its free coordinates. It also verifies a nonzero four-by-four
minor of the error columns for every row, excluding a pure-error kernel.
The exact determinants and row identifiers are saved in full.

Consequently E is invertible over every extension of F_97, R has exactly
the asserted rank, and its saved independent null vectors, numbering
six minus that rank, are a complete kernel basis over every such field.
There are 752 rank-six zero kernels and four rank-five kernel lines per
plane. Each of the twelve lines agrees with all six recovered coefficients
up to a single nonzero scale. No nonprime direction or weight can evade
these complete identities. The pre-chart distinct-direction count is
exactly four for each plane, with no duplicate, zero-rank or failed-weight
branch. It is eight below the necessary twelve.

For the arbitrary prescribed chart, direct substitution gives
A*(D*alpha-C*beta)+C*(-B*alpha+A*beta)=(AD-BC)*alpha and
B*(D*alpha-C*beta)+D*(-B*alpha+A*beta)=(AD-BC)*beta.
Thus the stated inversion is valid over the prescribed extension with
AD-BC nonzero. If D*alpha-C*beta vanishes, the other original coordinate
cannot vanish, and the direction is omitted. Otherwise division by the
nonzero original first coordinate preserves all full weights and gives
the unique original finite parameter. The invertible basis change keeps
distinct projective directions distinct. Hence chart deletion cannot
increase the four-direction count, even for nonrational original bases.
This proves the claimed necessary shortfall without any four-row converse
or construction of nonpersistent locators.

No mathematical defect or repair was found. This validates exactly the
restricted three-plane/six-occurrence exclusion, with finite-computation
dependence, shared Python/residue arithmetic and the inherited
L010/L103/L104 qualifications. It supplies no new exclusion, third/pair
conclusion, global improvement or progress beyond the sources checked.
Historical partitions and ATTEMPTS/041–043 remain preserved. The argument
and mathematical inputs are unchanged, so PROOF.md and DAG.md are not
edited; this canonical audit supersedes their pending-audit wording for
L123 only.

## Mathlib

Full matching coverage of this three-plane finite census is not checked,
not asserted absent. The standard coding/exterior results are imported
as cited above. The record-specific complete certificates are explicit
proof inputs, with the separate scoped critical audit above passed; no formal
verification or mathematical originality is claimed.
