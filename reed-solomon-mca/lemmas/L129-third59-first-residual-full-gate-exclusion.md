# L129 — L125 occurrence (59,355) specializes L126's two-plane exclusion

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, k=8, L010's shifted
moments and the pinned same-support event on 1/4<=delta<5/16. The actual
Hankel determinant D and every actual locator are nonzero polynomials.
Both coefficient syndromes belong to U_S, S={1,8,12,18,22,27,33}.
Assume sixteen original finite events and L104's represented t=0 class.
Retain L109's inherited L010/L103/L104 and L040/L069 finite-certificate
qualifications. Original weights and the prescribed chart are arbitrary
in F. These four supports are actual two-overlap errors:

| Row | I subset S | K subset J=H minus S |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,75} |
| 3 | {1,12} | {70,85} |
| 4 | {8,27} | {79,89} |

Use L109's original blocks, z_j=min(S minus I_j), lexicographic
covector pairs and increasing S-pair columns. No universal representation
or extraction of these actual supports is assumed.

## Conclusion

These hypotheses are inconsistent. The original stack has rank nineteen
and complete kernel span(B0,B1), where

    B0=E_1 wedge w,  w=67E_8+68E_12+2E_18+44E_22+54E_27+E_33,
    B1=E_8 wedge E_12.

Its homogeneous decomposable locus over every extension of F_97 is
exactly [B0],[B1], including projective infinity. All eight selected-row
projections have rank one. Both planes fail the necessary first-row
lambda gate; the changed third row also has lambda zero on both planes.
Only rows two and four on the first plane have full intrinsic weights.
Every prescribed original chart retains the exclusion.

This is exactly the indexed occurrence (59,355) in L125's full
lexicographic universe. All 154 historical residuals remain saved. No
third exclusion, fixed-pair exclusion, larger census, sixteen-event
construction or global improvement is claimed. Same-step independent
replay passes; the separate step-374 critical audit found no defect in
this indexed exclusion.

## Proof

### Imported tools, exact identity and scope

L109's necessary direction gives an independent pair of lift coefficients
and hence a nonzero decomposable tensor in the displayed original stack.
Every selected actual row must have rank-one projection, nonzero lambda,
nonzero overlap weights and the prescribed finite-direction gate. Its
four-row converse is not used: its nonpersistence converse requires at
least six rows and further hypotheses.

Import L126's audited complete homogeneous locus and rows one, two and
four after the explicit matrix/kernel/row bindings below. The changed
third row is computed here. L125 supplies index provenance only; neither
its filter partition nor a residual's feasibility is a premise.
The unchanged invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-20-new-pair-third59-first-residual-review.md`.
This is REPRODUCTION of an assessed mechanism on new indexed inputs,
without a claim of progress beyond the checked general literature.

The standard tools are imported through L109/L126: J. I. Hall,
*Notes on Coding Theory*, [Theorem 5.1.1, printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf);
I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
Definitions 5.1–5.2 and the GRS shortening formula after Lemma 5.3;
Keith Conrad, [*Exterior Powers*, Theorems 4.2, 7.1, 7.5, pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf).
The labels are sixteen distinct field elements with unit multipliers and
k=8. Each row shortens exactly seven distinct labels J minus K, reducing
dimension eight to positive dimension one with nonzero products of label
differences. Replacing 79 by 85 changes coefficients without changing
these hypotheses. No general coding or exterior theorem is reproved.
L126's homogeneous locus is used directly; no new splitting theorem or
rational descent argument is needed.

### Complete original kernel and extension binding

Evaluate g_j(X)=product_(y in J minus K_j)(X-y), form
c_jx=g_j(z_j)E_x^*−g_j(x)E_zj^* for increasing x in
(S minus I_j) minus {z_j}, and stack their exterior rows. This defines
all 504 entries of the 24-by-21 matrix N. Complete entries, products,
null residuals and the following minor are saved in
`scripts/seven-coordinate/third59-first-residual-gates.json`.

The minor with zero-based row indices

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,20

and column indices

    0,1,2,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20

has integer determinant

    −183559014313634527018950183616512 = 54 modulo 97.

B0 and B1 have zero residual at all 24 rows. Their coordinates in
columns 5 and 6 form the identity matrix, so they are independent.
Thus rank(N)<=19; the nonzero minor gives rank(N)>=19. These two
vectors span the complete kernel over F_97 and every extension, since
the same minor and null-vector independence persist.

The full 756-row universe binom(S,2) times binom(J,2) puts the third
support at 59 and the fourth at 355. The unique fourth-355 case in
`new-pair-filter/third-059.json` (case position 75) has the same rank,
minor rows/columns/residue, basis and all 48 null residuals. Its SHA256
is `df53d2429ea83f9c85777da586b1b89be4005f11ad6f8d36ca4edae7025415cb`.
This binds the historical occurrence without changing its partition.

The basis is literally L126's basis, in its identical ordered exterior
coordinates. Therefore L126's complete homogeneous classification applies
to this entire kernel, although N itself differs. In particular for
p=sB0+tB1 the only nonzero restrictions among the 35 Plucker relations
are 2st,44st,54st,st, at quadruples (1,8,12,x),
x=18,22,27,33. The other 31 coefficient triples are zero. All 35
triples are compared to L126's full certificate. Its proved zero locus
is st=0, giving exactly [1:0] and [0:1], including infinity, over every
extension. This imports its classification rather than applying a label
symmetry or inferring extension coverage from prime-field samples.
The corresponding planes are L0=span(E_1,w), L1=span(E_8,E_12).

### Unchanged rows and complete changed-row gates

For L0 take u=E_1,v=w; for L1 take u=E_8,v=E_12.
The original blocks, basis vectors and complete gate records at rows
one, two and four equal L126's exactly. Thus its rank-one, lambda,
weight, original-moment and arbitrary-chart conclusions apply to those
rows. In particular its first-row intersection lines are F E_1 and
F E_8, respectively, with z_1=12 and lambda zero in both cases.
This already excludes both planes by L109's necessary full-weight gate.
For completeness retain every gate of the changed third row as required.

At row three, g(X)=product_(y in J minus {70,85})(X-y), z=8.
Its values on S followed by K are:

| x | 1 | 8 | 12 | 18 | 22 | 27 | 33 | 70 | 85 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| g(x) | 54 | 87 | 2 | 13 | 69 | 60 | 79 | 69 | 68 |

The four covectors are 87E_x^*−g(x)E_8^* for
x=18,22,27,33. On L0, Qu=(0,0,0,0), Qv=(79,78,96,32).
On L1, Qu=(84,28,37,18), Qv=(0,0,0,0). Each projection has rank
exactly one: its six minors vanish and a displayed component is nonzero.
Choosing the first nonzero component n, set
(alpha,beta)=(-Qv[n],Qu[n]), h=alpha u+beta v,
lambda=h_8/g(8). L109 recovers e_i=h_i−lambda g(i) on I
and e_k=−lambda g(k) on K. The complete gates are:

| Plane | Row | (alpha,beta) | lambda | Weights on ordered I then K |
| --- | ---: | --- | ---: | --- |
| L0 | 1 | (85,0) | 0 | (85,0,0,0) |
| L0 | 2 | (19,12) | 30 | (9,94,10,9) |
| L0 | 3 | (18,0) | 0 | (18,0,0,0) |
| L0 | 4 | (61,90) | 29 | (88,28,9,53) |
| L1 | 1 | (81,0) | 0 | (0,81,0,0) |
| L1 | 2 | (0,75) | 0 | (75,0,0,0) |
| L1 | 3 | (0,84) | 0 | (0,84,0,0) |
| L1 | 4 | (28,0) | 0 | (28,0,0,0) |

For the changed row h=18E_1 or 84E_12 respectively. Hence h−e=0
at every label and all eight shifted moments vanish, retaining three
zero weights in each case. For every table row, extending h by zero
off S gives h−e=lambda*g_j at all sixteen H labels; all shifted
moments sum_x x^d(h_x−e_x), d=1,...,8, vanish as in L109.
The complete replay verifies all 128 pointwise entries and 64 moments,
including the unchanged rows, without discarding failed weights.

For an arbitrary original basis u_original=A u+B v,
v_original=C u+D v with Delta=AD−BC nonzero, the first original
coefficient of h is (D alpha−C beta)/Delta. Its exact prescribed
finite gate is D alpha−C beta!=0, recorded for all eight rows.
If zero the direction is omitted; otherwise normalizing by that first
coefficient rescales all errors by a nonzero scalar. Thus neither an
arbitrary extension-field chart nor a different nonzero projection or
exterior pivot repairs any zero lambda or weight. No replacement chart
is chosen, and the two successful rows do not give a four-row converse.

### Complete replay and limits

Reproduce from this notebook:

    python3 scripts/seven-coordinate/third59_first_residual_gates.py
    python3 scripts/seven-coordinate/verify_third59_first_residual_gates.py

Full evidence is in `scripts/seven-coordinate/third59-first-residual-gates.json`
and `scripts/seven-coordinate/third59-first-residual-gates-replay.json`.
The producer specializes the existing direct-product/matrix and gate
helpers. The verifier imports no producer helpers: the simple-root
identity g(x)=16x^15/product_(y in (S union K) minus {x})(x−y)
rebuilds the retained evaluations, and normalized ratio covectors are
scaled back to the original covectors before comparing all 504 entries.
Independent column elimination reconstructs both complete null vectors;
rational Gaussian determinant evaluation agrees with modular and
fraction-free elimination. All 35 homogeneous coefficient triples,
quotient/Bezout identities and infinity are checked against the imported
locus. Every row projection, lambda, overlap/outside weight, prescribed
chart coefficient, pointwise identity and original moment is replayed.
All seven nonzero exterior pivots and 106 nonzero projection-component
choices give nonzero multiples of the same intersection lines and weights.

Actual/required classified loci are 1/1, with two complete points,
eight rank-one row gates, six lambda-zero rows, two full-weight rows,
zero surviving planes and zero unresolved components. The complete
certificates are replayed, not inferred from previews. Two initial script
wiring errors (source filename and rank-field location) were corrected
before certificates were produced; neither was a mathematical discrepancy.
Both paths share Python and residue arithmetic; this is a same-step
verification, not a separate critical audit or proof-assistant result.

All historical residuals and ATTEMPTS/041–044 remain preserved. This
uses a complete locus and exact necessary gates rather than restarting
rank/factor/activity filters. Representation/extraction, the other
residuals, third/pair assembly, the global 11/q–16/q interval and the
challenge-definition qualifications remain unresolved.

### Separate critical audit, 2026-10-20

Step `2026-10-20-mca-374-third59-first-residual-critical-audit` used the
unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-10-20-third59-first-residual-audit-review.md`.
The complete proof, both complete programs and every called helper body
were checked, with L109's necessary proof/audit, L126's full proof/audit
and the relevant L010/L103/L104 hypotheses and shortening passages.
No mathematical or program defect, missing essential hypothesis or new
dependency was found. This validates a reproduced restricted input; it
adds no new indexed exclusion or result beyond the assessed sources.

L010 equality supplies full errors and distinct supports before L109
proves independence of the lift coefficients. Consequently every actual
four-row subfamily gives a nonzero decomposable kernel tensor. The
necessary implication holds for this selected subfamily; L109's
six-or-more-row converse is not used. The fixed field, seven-set,
shortening at exactly seven labels, actual nonzero D and locators,
arbitrary original chart and inherited L040/L069 finite-certificate
qualifications are retained. No representation or support extraction is
inferred, and L125 supplies provenance only.

The closed called-helper inventory is `g`, `block`, `rank_and_rows`,
`determinant`, `integer_determinant`, `wedge` in
`zero_anchor_support_filter.py`; and `plucker_polynomials`, `plane_gates`,
`trim`, `add`, `scale`, `mul`, `divrem`, `xgcd`, `gcd_certificate` in
`residual_kernel_gates.py`, together with their field/domain/order
constants. All signs, zero branches and nonzero divisors match the
displayed formulas. Neither helper's historical census is invoked.
Their bytes and the imported L126 certificate match the hashes in
L126's separate audit, which has no failed check.

The new matrix is independently rebuilt before importing any locus:
differentiating X^16−1 at a retained simple root gives the verifier's
product formula, and its normalized ratio covectors are scaled back to
the original covectors. All 504 original entries agree. Independent
column elimination returns the displayed complete basis. The signed
integer minor agrees with rational Gaussian elimination and has residue
54, while the two null vectors have the stated identity submatrix.
Thus rank is exactly nineteen over every extension. The unique
fourth-355 shard record is at position 75, with the displayed hash,
minor and basis; the full lexicographic universe binds its labels.

L126's algebraic subresults, rather than its inconsistent four-support
hypothesis as a whole, are imported. The complete bases have identical
ordered coordinates. All 35 homogeneous coefficient triples agree,
including 31 zero triples and the relation st itself. The quotient and
Bezout identities verify the affine gcd T; all t² coefficients vanish,
retaining infinity. The entire projective locus is therefore precisely
the two displayed nonzero wedges over every extension. Rows one, two
and four have identical original blocks, plane bases and complete gate
records. The changed third row is independently rebuilt and has exactly
the evaluations, projections, directions and weights displayed above.

All eight restrictions have rank one, including a nonzero component;
six have lambda zero and two have full weights. Every pointwise identity
(128 entries) and original shifted moment (64 entries) is checked.
All seven nonzero exterior pivots and 106 nonzero projection-component
choices give nonzero multiples of the same intersection vectors,
lambdas and weights. The original-chart matrix is [[A,C],[B,D]], so
the displayed inverse coefficient (D alpha−C beta)/(AD−BC) is correct.
If it vanishes the recovery is omitted; otherwise normalization only
rescales its zero weights. Thus the first-row lambda failures exclude
both exhaustive planes in every prescribed chart. The two full rows
cannot supply a four-row converse or any additional events.

Reproduce the isolated audit with

    python3 scripts/seven-coordinate/audit_third59_first_residual_gates.py

The full report is `scripts/seven-coordinate/l129-critical-audit.json`.
All 40 checks pass: both complete output certificates reproduce byte for
byte and all nine original program/input/output files remain unchanged.
Audited occurrences are 1/1, complete and excluded points 2/2, with
zero unresolved components. The replay compares all output bytes, not
previews, and supplements the semantic audit above. Python and residue
arithmetic remain shared; no proof-assistant validation is claimed.
All 154 historical residuals and the 11/q–16/q global interval remain.
No third/pair assembly or challenge-level conclusion is added.

## Mathlib

Full matching coverage for this exact labeled specialization: **not
checked**. Supporting coding, exterior, rank and finite-field coverage:
**not newly checked**, not asserted absent. Standard results and the
previously audited local locus are imported with their stated scopes;
the finite certificate retains its reproduction qualifications after
the separate critical audit.
