# L130 — L125 occurrence (59,647) specializes L127's two-plane exclusion

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, k=8, L010's shifted
moments and the pinned same-support event on 1/4<=delta<5/16. The actual
Hankel determinant D and every actual locator are nonzero polynomials.
Both coefficient syndromes belong to U_S for S={1,8,12,18,22,27,33}.
Assume sixteen original finite events and L104's represented t=0 class.
Retain L109's inherited L010/L103/L104 and L040/L069 finite-certificate
qualifications. Original weights and the prescribed finite chart are
arbitrary in F. With J=H minus S, assume these four supports are actual
two-overlap errors:

| Row | I subset S | K subset J |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,75} |
| 3 | {1,12} | {70,85} |
| 4 | {18,33} | {89,96} |

Use L109's original blocks, z_j=min(S minus I_j), increasing covector
pairs and increasing S-pair columns. No universal representation or
extraction of these actual supports is assumed.

## Conclusion

These hypotheses are inconsistent. The original 24-by-21 stack has rank
nineteen and complete kernel span(B0,B1), where

    B0=E_1 wedge E_18,
    B1=E_12 wedge w,
    w=82E_1+13E_8+73E_18+63E_22+62E_27+E_33.

Its complete homogeneous decomposable locus over every extension of
F_97 is exactly [B0],[B1], including projective infinity. All eight
selected-row projections have rank one. The first plane fails lambda
at every row; the second fails at rows two and three, while retaining
full intrinsic recoveries at rows one and four. No prescribed original
chart repairs these necessary full-weight failures.

This excludes exactly L125 full-universe occurrence (59,647). All 154
historical residuals remain saved. No third/pair assembly, larger census,
universal representation/extraction, sixteen-event completion or global
improvement follows. Same-step independent replay passes, and the separate
step-378 critical audit below found no defect. The global interval remains
11/q–16/q.

## Proof

### Assessed imports and their applicability

L109's necessary direction gives independent lift coefficients and a
nonzero decomposable wedge in this four-row stack. Each actual selected
row must have rank-one projection, nonzero lambda and overlap weights,
and a finite direction in the prescribed original chart. Its rejection
of rank zero uses actual polynomial nonpersistence. Its converse for
at least six rows is not applied.

Import the audited algebraic locus and unchanged-row subresults of L127
only after the exact matrix/kernel/row binding below. L125 supplies
index provenance, not the new exclusion or residual feasibility. L129
is a method comparison, not a mathematical premise. The unchanged
invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-20-third59-second-residual-binding-review.md`.
It supplies the scoped duplicate check, relevant primary coverage and
ATTEMPTS/041–044 comparisons. This is REPRODUCTION of assessed mechanisms
on one new indexed input, with no originality claim or claimed progress
beyond the general sources checked.

Standard coding inputs enter through L109: J. I. Hall, *Notes on Coding
Theory*, [Theorem 5.1.1 and proof, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf);
I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2 and the GRS shortening formula after Lemma 5.3.
There are sixteen distinct labels, unit multipliers and k=8. Each row
shortens the seven distinct labels J minus K, reducing dimension eight
to positive dimension one with all retained products of label differences
nonzero. Replacing 79 by 85 changes coefficients without changing these
hypotheses. No general coding theorem is reproved.

Keith Conrad, [*Exterior Powers*, Theorems 4.2, 7.1, 7.5 and proofs,
pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
supplies exterior bases and the nonzero-wedge/plane association over any
field. L109 supplies the explicit equations and pivots. L127's complete
homogeneous classification is imported directly, with its polynomial
division/Bezout background from J. S. Milne, [*Fields and Galois Theory*,
Kea Books 2022, sections 1.6–1.9 pp. 5–7 and Proposition 2.17 p. 34](https://www.jmilne.org/math/Books/FT0.pdf).
The coefficient field remains F_97. No new splitting theorem or rational
descent argument is needed. The computations below justify the changed
inputs and exact import identity, rather than reproving those theorems.

### Fresh original matrix and complete extension kernel

Set g_j(X)=product_(y in J minus K_j)(X-y). Form
c_jx=g_j(z_j)E_x^*−g_j(x)E_zj^* for increasing
x in (S minus I_j) minus {z_j}, and stack all six exterior pairs per
row. This defines every entry of the original matrix N. The full entries
and products are saved in
`scripts/seven-coordinate/third59-second-residual-gates.json`.

The original nineteen-by-nineteen minor with zero-based rows

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21

and columns

    0,1,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20

has integer determinant

    3594962637037369699889979396022272 = 85 modulo 97.

This is a new original minor, not L127's residue 9. In increasing
S-pair order B0 has sole entry 1 in column 2. B1 has entries
15,84,73,63,62,1 in columns 1,6,11,12,13,14 and zero elsewhere.
Both vectors have zero residual in all 24 original rows. Their entries
in columns 2 and 14 form the identity matrix, so they are independent.
Thus rank(N)<=19, and the nonzero minor gives rank(N)>=19. They span
the complete kernel over F_97 and every extension, because the same
nonzero minor and null-vector independence persist over extensions.

The lexicographic universe binom(S,2) times binom(J,2) places the third
support at 59 and the fourth at 647. The unique fourth-647 record in
`scripts/seven-coordinate/new-pair-filter/third-059.json`, also at
`/cases/182`, matches the rank, original minor rows/columns/residue,
complete basis and all 48 original null residuals. Its SHA256 is
`df53d2429ea83f9c85777da586b1b89be4005f11ad6f8d36ca4edae7025415cb`.
No historical case is removed, reordered or recursively filtered.

### Binding L127's complete homogeneous locus

The entire ordered basis is literally L127's, with identical exterior
column order. Therefore its algebraic classification applies to this
complete kernel even though N differs. For p=sB0+tB1 the only nonzero
restrictions among the 35 Plucker relations are:

| Quadruple | Restriction |
| --- | --- |
| (1,8,12,18) | 84st |
| (1,12,18,22) | 34st |
| (1,12,18,27) | 35st |
| (1,12,18,33) | 96st |

All 35 coefficient triples, including all zeros, their ordered quadruples,
affine quotients, gcd and Bezout coefficients match L127's full certificate.
The imported locus is st=0, with exactly [1:0],[0:1] over every extension.
All t² coefficients vanish, explicitly retaining infinity. The affine
gcd T and its divisibility/Bezout identities are replayed as binding
checks. This is a complete-locus import, not prime-field point sampling
or a label symmetry. The planes are L0=span(E_1,E_18) and
L1=span(E_12,w).

### Unchanged rows and the changed third row

For L0 use u=E_1,v=E_18. For L1 use L127's canonical basis
u=(1,25,0,21,54,67,84), v=15E_12, whose wedge is B1.
Rows one, two and four have identical labels, g values, original blocks,
plane bases and complete gate records to L127. Its conclusions for
those rows consequently apply. In particular L0 intersects the first
row's V_1 in F E_1, while L1 intersects V_2 in F E_12.
Since z_1=12 and z_2=1, respectively, each has lambda zero. This
already excludes both planes by L109's necessary full-weight gate.
Retain all changed-row calculations as well.

For row three, g(X)=product_(y in J minus {70,85})(X-y), z=8.
Its values on S followed by K are:

| x | 1 | 8 | 12 | 18 | 22 | 27 | 33 | 70 | 85 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| g(x) | 54 | 87 | 2 | 13 | 69 | 60 | 79 | 69 | 68 |

The four covectors are 87E_x^*−g(x)E_8^* for x=18,22,27,33.
On L0, Qu=(0,0,0,0), Qv=(87,0,0,0). On L1,
Qu=(47,63,61,95), Qv=(0,0,0,0). Both projections have rank
exactly one: all six minors vanish and a displayed component is nonzero.
At the first nonzero component n take
(alpha,beta)=(-Qv[n],Qu[n]) and h=alpha u+beta v.
Restore lambda=h_8/g(8), e_i=h_i−lambda*g(i) on I and
e_k=−lambda*g(k) on K. All eight row records are:

| Plane | Row | (alpha,beta) | lambda | Weights on ordered I then K |
| --- | ---: | --- | ---: | --- |
| L0 | 1 | (53,0) | 0 | (53,0,0,0) |
| L0 | 2 | (0,12) | 0 | (0,12,0,0) |
| L0 | 3 | (10,0) | 0 | (10,0,0,0) |
| L0 | 4 | (0,54) | 0 | (54,0,0,0) |
| L1 | 1 | (51,51) | 24 | (58,32,57,90) |
| L1 | 2 | (0,44) | 0 | (78,0,0,0) |
| L1 | 3 | (0,47) | 0 | (0,26,0,0) |
| L1 | 4 | (13,51) | 82 | (35,48,75,23) |

In the changed row h=10E_1 or 26E_12. Thus h−e=0 on all H,
with three zero weights retained in both cases. For all eight records,
extend h by zero off S: h−e=lambda*g_j on all sixteen H labels and
sum_(x in H) x^d(h_x−e_x)=0 for d=1,...,8. All 128 pointwise
entries and 64 original shifted-moment residuals are checked, including
the two full intrinsic rows. These are not four full recoveries.

For any prescribed original basis u_original=A u+B v,
v_original=C u+D v with Delta=AD−BC nonzero, the first original
coefficient of h is (D alpha−C beta)/Delta. Every row retains its
finite-direction gate D alpha−C beta!=0. If zero the direction is
omitted; otherwise normalization divides the errors by this nonzero
first coefficient, preserving every zero weight and moment identity.
This identity permits arbitrary nonrational coefficients and never
replaces the prescribed chart. Neither a chart nor another pivot
repairs either plane's failed lambda gate.

### Complete replay and limitations

Reproduce from this notebook:

    python3 -B scripts/seven-coordinate/third59_second_residual_gates.py
    python3 -B scripts/seven-coordinate/verify_third59_second_residual_gates.py

Full certificates are
`scripts/seven-coordinate/third59-second-residual-gates.json` and
`scripts/seven-coordinate/third59-second-residual-gates-replay.json`.
The producer uses reviewed direct-product/matrix and recovery helpers.
The verifier imports no producer helpers. At each retained simple root
it uses g(x)=16x^15/product_(y in (S union K) minus {x})(x−y),
with all denominator factors nonzero, then rescales ratio covectors back
to the original covectors. It reconstructs all 504 original entries;
independent column elimination gives the complete two-vector kernel.
Rational Gaussian determinant evaluation agrees with the producer's
modular and fraction-free integer eliminations, including row-swap signs.
All 35 homogeneous triples, quotient/Bezout identities, both endpoints,
all eight projections, directions, lambdas, weights, original moments,
pointwise identities and prescribed-chart coefficients are replayed.

All seven nonzero exterior pivots and 88 nonzero projection-component
choices give nonzero multiples of the same intersection lines, lambdas
and errors. Actual/required classified loci are 1/1, with two complete
points, eight rank-one rows, six lambda-zero rows, two full-weight rows,
zero passing planes, zero unresolved components and zero failures.
Complete relevant certificate records are replayed; a preview is not
used as verification. Both paths still share Python and residue
arithmetic. This is same-step verification, pending a separate critical
audit, and no proof-assistant verification is claimed.

All 154 historical residuals and ATTEMPTS/041–044 remain preserved.
Only one indexed occurrence is excluded. Other residuals, third/pair
assembly, universal representation/extraction and challenge-definition
qualifications remain unresolved; no global improvement is inferred.

### Separate critical audit, 2026-10-20

Step 2026-10-20-mca-378-third59-second-residual-critical-audit used the
unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-10-20-third59-second-residual-audit-review.md`.
It checked this complete proof, both complete programs and every called
helper body, L109's necessary direction and audit, L127's complete proof
and audit, and the relevant inherited L010/L103/L104 hypotheses and
shortening/equality passages. The scoped history search found the
calculation and coverage steps, not an earlier separate audit. The ready
primary coverage above is reused; no new general theorem is asserted.

The application of L109 is within scope: equality precedes full weights
and distinct actual supports, and eight-column injectivity makes the lift
directions independent. Hence the necessary wedge is nonzero. All four
supports here are assumed actual; neither extraction nor the r>=6
converse is invoked. Each shortening set J minus K has seven distinct
labels and every retained g-value is nonzero. Inherited L040/L069
finite-certificate qualifications remain.

The producer's products, ordered covectors and six exterior pairs per
row give the stated original stack. Its row reduction selects independent
original rows; modular and fraction-free determinants retain row-swap
signs. The verifier differentiates X^16−1 only at retained simple roots
x in S union K. Dividing by the other retained label differences gives
the exact g(x), with no zero denominator. Rescaling its ratio covectors
by g(z)g(x) gives the original covectors entry by entry. Independent
column elimination and rational Gaussian elimination check all 504
entries, both null vectors and the displayed integer determinant,
whose residue is 85. The independent free-coordinate entries and the
nonzero minor prove both rank inequalities over every extension.

The original third-059 shard hash matches the displayed frozen hash.
The unique fourth_index 647 is case position 182, and the independently
generated universe gives exactly indices (59,647). Its rank, minor
rows/columns/residue, complete basis and all 48 null residuals agree.
The imported L127 certificate and both helper files also match the
hashes in L127's separate audit. More than a named lemma is being reused:
the entire ordered basis, exterior-column order, all 35 homogeneous
coefficient triples, ordered quadruples, affine quotients, gcd and
Bezout coefficients match. The only nonzero restrictions are the four
displayed multiples of st; 84 is nonzero in every extension of F_97.
The sole nonzero Bezout coefficient is 96 on 96T, so the combination
equals T. All pure t² coefficients vanish, retaining infinity. This
justifies the exact two-point import without applying L127's inconsistent
four-support hypothesis to a different support list.

Rows one, two and four have identical original labels, blocks, plane
bases and complete gate records. The changed third row is independently
reconstructed: its g-values are the nine displayed values, and its
projections are (Qu,Qv)=(0,(87,0,0,0)) on L0 and
((47,63,61,95),0) on L1. These give h=10E_1 and h=26E_12,
respectively, with lambda zero and all three canceled weights retained.
All eight projections have rank one. The six failed lambda gates and
two full rows, all 128 pointwise identities and all 64 shifted moments
are checked. Every one of the seven nonzero exterior pivots and 88
nonzero projection-component choices gives a nonzero multiple of its
canonical intersection, lambda and error vector. The complete replay
records are regenerated, not merely their counts.

For arbitrary A,B,C,D in F with Delta=AD−BC nonzero, original coordinates
(a,b) map to (Aa+Cb,Ba+Db). Thus the inverse gives
a=(D alpha−C beta)/Delta and b=(-B alpha+A beta)/Delta.
Substitution recovers both canonical coordinates exactly. A zero a
omits the direction; nonzero a divides the recovered errors by a and
preserves each zero weight. This is an algebraic check for arbitrary
nonrational coefficients, not acceptance of the certificate's formula
strings or sampling rational charts. Neither chart nor pivot repairs
L0's failed first row or L1's failed second row.

Fresh isolated reproduction:

    python3 -B scripts/seven-coordinate/audit_l130.py

Only the two one-occurrence programs, two helpers and their exact input
artifacts are copied into a notebook-local temporary directory. Assertions
are enabled. Both complete output certificates reproduce byte for byte;
all 40/40 audit checks pass, zero components remain unresolved, and all
nine original files remain unchanged. Full hashes, subprocess results
and check outcomes are saved in
`scripts/seven-coordinate/l130-critical-audit.json`. Historical certificates
keep their original same-step/pending-audit wording; this section records
the later separate verdict.

No mathematical defect or missing direct input was found. This validates
one reproduced restricted input, not a new indexed exclusion or progress
beyond the assessed general sources. Python and residue arithmetic remain
shared; no proof-assistant verification is claimed. All 154 residuals and
ATTEMPTS/041–044 are preserved. The argument and direct inputs L109/L127
are unchanged, so PROOF.md and DAG.md are unchanged. No third/pair
assembly, universal representation/extraction or challenge solution follows.

## Mathlib

Full matching coverage for this exact indexed classification: **not
checked**. Supporting coding, exterior-square, matrix-rank, finite-field
and polynomial-gcd coverage: **not newly checked**, not asserted absent.
Standard inputs are imported through the precise citations above; this
restricted reproduction retains explicit finite-certificate qualifications
and passed the separate step-378 critical audit recorded above.
