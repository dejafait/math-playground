# L133 — First literal mismatch (94,355) has two ineligible planes

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, k=8, L010's shifted
moments and the pinned same-support event on 1/4<=delta<5/16.
The actual Hankel determinant D and every actual coordinate locator
are nonzero polynomials. Both coefficient syndromes belong to U_S,
S={1,8,12,18,22,27,33}. Assume sixteen original finite events and
L104's represented t=0 class. Weights and the prescribed original
chart are arbitrary over F. Retain L109's inherited L010/L103/L104
and L040/L069/L086/L056 finite-certificate qualifications.

Assume the following four supports are actual two-overlap errors:

| Row | I subset S | K subset J=H minus S |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,75} |
| 3 | {1,18} | {70,79} |
| 4 | {8,27} | {79,89} |

Use L109's original exterior blocks, z_j=min(S minus I_j), increasing
covector-pair rows and increasing S-pair exterior columns. These are
L125's full-universe indices (94,355), without exchange identification.
No universal representation or occurrence of this fixed pair is assumed.

## Conclusion

These four-actual-support hypotheses are inconsistent. The original stack
has rank nineteen and complete kernel span(B0,B1), where

    B0=E_1 wedge w, B1=E_8 wedge E_18,
    w=67E_8+68E_12+2E_18+44E_22+54E_27+E_33.

Its complete homogeneous decomposable locus over every extension of
F_97 consists of exactly [B0],[B1]. Every selected-row projection has
rank one. Both planes have first-row lambda zero, and hence fail a
necessary full-weight gate in every prescribed original chart.

This excludes only occurrence (94,355). L125's 154 historical residuals
and L132's 118 literal mismatches remain preserved. No third/pair assembly,
enlarged census, universal extraction or global improvement follows.
The global frozen-model interval remains 11/q–16/q. Same-step independent
replay passes; the separate step-390 critical audit below found no defect.

## Proof

### Assessed inputs and specialization

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-20-first-unmatched-locus-review.md`.
This is REPRODUCTION of its assessed certificate method, with new
indexed coefficients and an exclusion, not a new general theorem or
progress beyond the sources checked. L126/L127 are method precedents;
their different kernels' loci are not imported. L132's literal mismatch
and ATTEMPTS/041–044's exhausted filters do not decide this locus.

L109 supplies the necessary nonzero decomposable tensor of the actual
independent coefficient directions. Each actual row must have projection
rank one, nonzero lambda and both overlap weights, and its prescribed
finite-direction gate. No four-row converse is used. L125 fixes the
ordered domain and source record; its index is independently rebound below.

Standard results are imported through L109 with these precise sources:
J. I. Hall, *Notes on Coding Theory*, [Theorem 5.1.1 and proof,
printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf);
I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004, [accepted manuscript 2016-02-29,
section 5, Definitions 5.1–5.2 and GRS shortening formula after
Lemma 5.3, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
All sixteen labels are distinct, multipliers are nonzero and k=8.
Each row shortens seven distinct labels J minus K through positive
dimensions eight to one; retained products of distinct differences
remain nonzero. No broader parameter version of Lemma 5.3 is needed.

Conrad, [*Exterior Powers*, Theorems 4.2, 7.1, 7.5 and proofs,
pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
supports exterior bases and the independent-wedge/plane association over
any field, here degree two in dimension seven. L109 already proves the
explicit Plucker criterion and pivot reconstruction. Milne, [*Fields and
Galois Theory*, Kea Books 2022, sections 1.6–1.9 pp. 5–7 and
Proposition 2.17 p. 34](https://www.jmilne.org/math/Books/FT0.pdf), supplies
division/Bezout and extension-gcd invariance. The present locus splits
in F_97; no quadratic-field membership assertion is needed. General
coding, exterior and field theorems are not reproved.

### Original matrix and complete extension kernel

Form g_j(X)=product_(y in J minus K_j)(X-y), and the four covectors
c_jx=g_j(z_j)E_x^*−g_j(x)E_zj^*, x in (S minus I_j) minus {z_j}.
Stack their six exterior rows, as in L109, to get the original 24-by-21
matrix N. All 504 entries are saved in
`scripts/seven-coordinate/first-unmatched-locus-gates.json`.

The source is the entire `/cases/75` record in
`scripts/seven-coordinate/new-pair-filter/third-094.json`, bound by SHA256.
It is the unique fourth-index-355 record and has residual status.
Independently generating binom(S,2) times binom(J,2) gives the displayed
third at 94 and fourth at 355. All four supports are distinct and all
six intersections have size at most one. No other occurrence is tested.

The original minor at zero-based rows

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21

and all columns except 5,7 has integer determinant

    395267624744488680821654751805440000 = 34 modulo 97.

Both displayed basis vectors annihilate all 24 original rows and have
the identity matrix in columns 5,7. They are independent, so rank(N)<=19;
the nonzero original minor gives rank(N)>=19. Thus this is the complete
kernel. The same minor and identity submatrix remain nonzero under
every scalar extension, proving completeness there as well. Independent
column elimination reconstructs the identical ordered basis.

### Complete homogeneous locus, including infinity

Write p=sB0+tB1. The possibly nonzero coordinates are

    p_(1,8)=67s, p_(1,12)=68s, p_(1,18)=2s,
    p_(1,22)=44s, p_(1,27)=54s, p_(1,33)=s, p_(8,18)=t.

Among all 35 increasing-label relations
p_ab p_cd−p_ac p_bd+p_ad p_bc, precisely four are nonzero:

| Quadruple | Restricted polynomial |
| --- | --- |
| (1,8,12,18) | 29st |
| (1,8,18,22) | 44st |
| (1,8,18,27) | 54st |
| (1,8,18,33) | st |

Products of two B0 coordinates repeat label 1, and products of two
B1 coordinates repeat labels 8,18. Only the four displayed mixed products
have four distinct labels. Their signs give −68=29 at the first and
the displayed w coefficients at the other three. This accounts for all
35 coefficient triples, independently replayed in full.

Consequently the common homogeneous zero set is exactly st=0 over
every extension. A field has no zero divisors, so its nonzero projective
solutions are exactly [1:0],[0:1]. Both are explicit wedges. The affine
chart s=1 has gcd T; saved division and Bezout identities are checked
coefficientwise. At s=0 all homogeneous restrictions vanish, retaining
infinity explicitly. No empty, repeated, nonsplit or whole-line component
remains. The two planes are L0=span(E_1,w), L1=span(E_8,E_18).

### Every original-row gate and prescribed chart

For these planes use respectively (u,v)=(E_1,w),(E_8,E_18).
All six minors of each restriction (Q_j u,Q_j v) vanish, and at least
one component is nonzero, proving rank exactly one. At the first
nonzero component n put (alpha,beta)=(-Q_jv[n],Q_ju[n]) and
h=alpha u+beta v. Restore lambda=h_z/g_j(z), overlap weights
h_i−lambda g_j(i), and outside weights −lambda g_j(k).

| Plane | Row | First nonzero component (Q u,Q v) | (alpha,beta) | lambda | Weights on ordered I then K |
| --- | ---: | --- | --- | ---: | --- |
| L0 | 1 | (0,12) | (85,0) | 0 | (85,0,0,0) |
| L0 | 2 | (12,78) | (19,12) | 30 | (9,94,10,9) |
| L0 | 3 | (0,92) | (5,0) | 0 | (5,0,0,0) |
| L0 | 4 | (90,36) | (61,90) | 29 | (88,28,9,53) |
| L1 | 1 | (0,44) | (53,0) | 0 | (0,53,0,0) |
| L1 | 2 | (75,0) | (0,75) | 0 | (0,75,0,0) |
| L1 | 3 | (76,0) | (0,76) | 0 | (0,76,0,0) |
| L1 | 4 | (0,69) | (28,0) | 0 | (28,0,0,0) |

Every h is nonzero and spans the unique intersection with ker Q_j.
All zero weights are retained. Extending h by zero off S, the restored
errors satisfy h−e=lambda g_j at all sixteen labels, hence all eight
original shifted moment differences vanish. The complete 128 pointwise
entries and 64 moment residuals are replayed. Two full rows on L0
do not repair its failed rows.

In particular Q_1 E_1=0 and Q_1 w=(12,50,18,31) is nonzero;
Q_1 E_8=0 and Q_1 E_18=(44,0,0,0) is nonzero. The first-row
intersection lines are exactly F E_1 and F E_8. Since z_1=12, both
have h_12=0 and lambda zero. Outside weights vanish, contradicting
L109's necessary full-four-error gates.

For any prescribed original basis u_original=A u+B v,
v_original=C u+D v, Delta=AD−BC!=0, inversion gives the original
first coefficient (D alpha−C beta)/Delta. Thus each exact finite gate
is D alpha−C beta!=0, with (alpha,beta) from the table. If this fails,
the row direction is not original finite; otherwise rescaling h,e by
that first coefficient preserves every zero weight and moment identity.
No rationality or replacement of the prescribed chart is used.

### Verification and limits

Reproduce from this notebook:

    python3 -B scripts/seven-coordinate/first_unmatched_locus_gates.py
    python3 -B scripts/seven-coordinate/verify_first_unmatched_locus_gates.py

Full certificates are `scripts/seven-coordinate/first-unmatched-locus-gates.json`
and `scripts/seven-coordinate/first-unmatched-locus-gates-replay.json`.
The producer specializes the inspected L126 program and reuses the
direct product, fraction-free determinant and L109 gate helpers. The
verifier specializes its independent replay and imports no producer helper.
It differentiates X^16−1 at each retained simple root to evaluate

    g_j(x)=16*x^15/product_(y in (S union K_j) minus {x})(x-y).

All denominators are nonzero. Normalized ratio covectors recover every
original block entry after nonzero scaling, and independent column
elimination recovers the complete kernel. Rational Gaussian elimination
reproduces the exact integer minor. All homogeneous coefficients,
division/Bezout identities and infinity are checked. Every one of seven
nonzero exterior pivots and all 103 corresponding nonzero projection
component choices reconstruct the same intersection lines and weights
up to a checked nonzero scalar. Original moments and prescribed finite
gate coefficients are retained. Both paths share Python and residue
arithmetic; no proof assistant check or separate critical audit is claimed.

Actual/required complete loci are 1/1, with two points, eight rank-one
row gates, six lambda-zero rows, two full rows, zero passing planes and
zero unresolved components. This is a finite exact indexed input with
the inherited qualifications. Four necessary rows provide no equality
completion, t=0 realization or construction through L109's r>=6 converse.
The independent challenge-definition and universal-extraction gaps remain.

### Separate critical audit, 2026-10-21

Step `2026-10-21-mca-390-first-unmatched-critical-audit` used the unchanged
invocation-start EXPLORE assessment
`drafts/literature/2026-10-21-first-unmatched-critical-audit-review.md`.
The complete proof, both complete programs and every called mathematical
helper were inspected. L109's necessary nonzero-wedge, rank/projection,
full-weight and original-chart argument and its prior audit were checked;
L125's exact ordered domain, rank/kernel certification and prior audit
were checked for provenance. The ready primary sources stated above are
reused with their hypotheses, not retrieved anew. The inherited
L010/L103/L104/L040/L069/L086/L056 qualifications remain; their unchanged
certificates are not rerun. L132 is mismatch history, and L126/L127 are
method precedents, not mathematical inputs for this new kernel.

Reproduce this separate audit from the notebook:

    python3 -B scripts/seven-coordinate/audit_l133_locus.py

The complete audit manifest and comparison results are in
`scripts/seven-coordinate/l133-critical-audit.json`, with the full isolated
execution log in `scripts/seven-coordinate/l133-critical-audit-replay.log`.
Seven original program/helper/source/certificate files are bound by SHA256.
The inspected producer and independent verifier execute in an isolated
copy; both complete certificates reproduce byte for byte. All seven
original files remain unchanged. All 30 wrapper checks pass with zero
failures; the mathematical checks are the complete asserted comparisons
in the inspected programs, not just their summary counters.

The complete original `/cases/75` record is bound, including the unique
fourth index, original rank minor and both full null vectors. Independent
lexicographic generation binds indices 94 and 355 to the stated labels;
four distinct supports and all six linearity tests pass. The producer's
historical helper SUPPORTS constant is unused: every block receives the
new I,K explicitly. The verifier constructs H by powers of 8, while the
producer uses all roots of X^16−1; their complete sets agree. Differentiation
at each retained simple root supplies g(x), with every denominator nonzero.
Its ratio covector is c_x/(g(z)g(x)); multiplying by g(z)g(x) recovers the
original covector before forming its exterior rows. Thus all 504 entries
are checked in the original normalization, not merely up to row equivalence.

Fraction-free integer elimination and independent rational elimination
give the displayed integer determinant and nonzero residue 34. The 48
null residuals vanish and the free-coordinate submatrix is the identity.
These two bounds prove rank exactly nineteen and the full two-dimensional
kernel after every scalar extension. Independent column elimination
recovers the identical ordered basis, without trusting the source rank.

All 35 homogeneous coefficient triples are compared. Only the four
displayed st coefficients are nonzero, one equal to one, so every
extension-field solution has st=0. Conversely both endpoints are explicit
nonzero wedges. The complete affine division/Bezout identities and the
separate s=0 endpoint pass. This is a homogeneous identity argument, not
prime-field point enumeration; no additional extension component is missed.

All eight projections have rank exactly one. All 128 pointwise identities
and 64 original shifted moments pass, retaining every zero weight and the
two full rows. The complete replay checks all seven nonzero exterior pivots
and all 103 nonzero projection-component choices, with a nonzero scalar
relating each reconstructed intersection and its weights to the canonical
one. The first-row lines are exactly F E_1 and F E_8; their z=12 coordinate
is zero. Hence both fail lambda!=0, which L109 requires for actual full
four-errors. No support-compatible kernel is promoted to an event.

For arbitrary A,B,C,D in the prescribed extension with AD−BC nonzero,
the inverse basis matrix gives original coefficients
((D alpha−C beta),(-B alpha+A beta))/(AD−BC). If the first is zero,
the direction is omitted from the original finite chart. Otherwise divide
h and its recovered error by that coefficient; every zero weight remains
zero, and the homogeneous moment identities remain valid. This covers
nonrational chart changes without enumerating or replacing the chart.
The certificate's eight finite-gate coefficient pairs agree with this
formula. Neither the four-row converse nor any additional-row census is used.

No mathematical defect or changed dependency was found. The result is
validation of this reproduced indexed input, not a new exclusion, general
theorem or progress beyond the checked sources. Both paths share Python
and residue arithmetic; no proof-assistant verification is claimed. This
section supersedes the overview's historical pending-audit wording without
changing its argument. All 154 historical residuals and 118 literal
mismatches remain preserved. Other occurrences, third/pair assembly,
universal representation/extraction and challenge definitions stay open.

## Mathlib

Full matching indexed locus/exclusion and supporting coding, exterior,
polynomial and matrix coverage: **not checked**, rather than absent.
The imported standard results and explicit computational qualification
are stated above. No novelty claim is inferred from unchecked coverage.
