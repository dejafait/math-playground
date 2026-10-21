# L135 — Occurrence (94,539) has two ineligible planes

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, dimension k=8,
L010's shifted moments and the pinned same-support event on
1/4<=delta<5/16. The actual Hankel determinant D and every actual
coordinate locator are nonzero polynomials. Both coefficient syndromes
belong to U_S, S={1,8,12,18,22,27,33}. Assume sixteen original finite
events and L104's represented t=0 class, with arbitrary extension-field
weights and prescribed original chart. Retain L109's inherited
L010/L103/L104/L040/L069/L086/L056 finite-certificate qualifications.

Assume all four following supports are actual two-overlap errors:

| Row | I subset S | K subset J=H minus S |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,75} |
| 3 | {1,18} | {70,79} |
| 4 | {12,33} | {89,96} |

Use L109's original blocks, z_j=min(S minus I_j), increasing covector
pairs and increasing S-pair exterior columns. These are L125's ordered
full-universe indices (94,539); no exchange quotient or universal
representation/pair extraction is assumed.

## Conclusion

The four-actual-support hypotheses are inconsistent. The original stack
has rank nineteen and complete extension kernel span(B0,B1), where

    B0=E_1 wedge E_12,
    B1=u wedge v,
    u=(1,25,15,0,54,67,84), v=15E_18

in increasing S coordinates. Its complete homogeneous decomposable locus
over every extension of F_97 is exactly [B0],[B1]. Every selected-row
projection has rank one. Both planes have row-two lambda zero and fail
necessary full weights in every prescribed original chart.

This is one indexed exclusion, not a third/pair assembly or global
improvement. All historical 154/118/100 lists remain unchanged. The
global frozen-model interval stays 11/q–16/q. Complete same-step
independent replay passes; the separate step-398 critical audit below
found no defect.

## Proof

### Assessed inputs and scope

The invocation-start assessment is
`drafts/literature/2026-10-21-second-unmatched-locus-review.md`, SPECIALIZE.
This is REPRODUCTION: a specialization of standard coding, exterior and
polynomial algebra with new indexed coefficients and a local exclusion,
not a new general theorem or progress beyond the sources checked.
L109 supplies the necessary nonzero actual wedge and all row gates;
L125 supplies the original ordered domain and record. L133 is a different
kernel and a proof/program precedent only. L132/L134's literal failures
and ATTEMPTS/041–044's sufficient-filter obstructions are history, not
an imported locus or gate verdict. No general theorem is reproved here.

Import the standard inputs through L109 with their assessed hypotheses:
J. I. Hall, *Notes on Coding Theory*, [Theorem 5.1.1 and proof,
printed pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf);
I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004, [accepted manuscript 2016-02-29,
section 5, Definitions 5.1–5.2 and shortening formula after Lemma 5.3,
pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
The sixteen labels are distinct with nonzero multipliers and k=8.
Each row shortens seven distinct J-minus-K labels through positive
dimensions eight to one; all retained difference products are nonzero.
No stronger MDS claim outside that shortening scope is used.

K. Conrad, [*Exterior Powers*, Theorems 4.2, 7.1, 7.5 and relevant
proofs, pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
supports exterior bases and independent wedges representing planes over
any field, here degree two in dimension seven. L109 provides the explicit
Plucker criterion and reconstruction. J. S. Milne, [*Fields and Galois
Theory*, Kea Books 2022, sections 1.6–1.9 pp. 5–7 and Proposition 2.17
p. 34](https://www.jmilne.org/math/Books/FT0.pdf), supplies division,
Bezout and extension-gcd invariance. The locus below splits over F_97;
no quadratic-field membership claim or original-chart descent is needed.
These ready primary extractions are reused, not freshly retrieved.

### Original matrix and complete kernel

For each row set g_j(X)=product_(y in J minus K_j)(X-y). For
x in (S minus I_j) minus {z_j}, use

    c_jx=g_j(z_j)E_x^*−g_j(x)E_zj^*.

Stack the six exterior rows of each four-covector matrix Q_j. This is
L109's original 24-by-21 matrix N, not a changed normalization.
All 504 entries are saved in
`scripts/seven-coordinate/second-unmatched-locus-gates.json`.

The complete original source is `/cases/155` of
`scripts/seven-coordinate/new-pair-filter/third-094.json`, bound by SHA256.
The producer and verifier each bind the unique fourth-index-539 residual
record, its complete basis, minor rows/columns/residue and null residuals.
Independent lexicographic generation of binom(S,2) times binom(J,2)
binds indices 94 and 539 to the displayed supports. The four supports
are distinct and all six intersections have size at most one.

The original minor on zero-based rows

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21

and all columns except 1,17 has integer determinant

    -945819218664996129435665357596016640 = 23 modulo 97.

In increasing exterior columns the two kernel vectors are

    B0=(0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
    B1=(0,0,15,0,0,0,0,84,0,0,0,31,0,0,0,63,62,1,0,0,0).

Both annihilate every original row and their columns 1,17 form the
identity. Thus they are independent and rank(N)<=19. The minor gives
rank(N)>=19, proving completeness of this basis. Its identity submatrix
and the nonzero minor remain nonzero after every scalar extension, so
the same basis spans the entire extension kernel. Independent column
elimination reconstructs the identical ordered basis, rather than trusting
the source rank or nullspace.

### Complete homogeneous locus including infinity

Write p=sB0+tB1. Among all 35 increasing-label Plucker relations
p_ab p_cd−p_ac p_bd+p_ad p_bc, exactly four are nonzero:

| Quadruple | Restriction |
| --- | --- |
| (1,8,12,18) | 13st |
| (1,12,18,22) | 63st |
| (1,12,18,27) | 62st |
| (1,12,18,33) | st |

B0 has only coordinate (1,12), and every B1 coordinate contains label
18. Therefore their individual squares contribute nothing: B0 and B1
are the explicit wedges in the conclusion. The mixed products can have
four distinct labels only at the four displayed quadruples. The first
coefficient is -84=13; the remaining three are 63,62,1. This accounts
for all 35 homogeneous coefficient triples, each independently replayed.

The complete common zero set is consequently st=0 over every extension.
Because fields have no zero divisors, the only projective solutions are
[s:t]=[1:0],[0:1], both nonzero explicit wedges. In the affine chart
s=1 the saved gcd is T; each division identity and the Bezout identity
giving T are verified coefficientwise. At s=0 every t^2 coefficient
vanishes, retaining infinity directly. There is no missing repeated,
nonsplit, empty or whole-line component; this is not a base-field root
search. Call the resulting planes L0 and L1.

### All four row gates and arbitrary original chart

Use (u0,v0)=(E_1,E_12) and (u1,v1)=((1,25,15,0,54,67,84),15E_18).
Their wedges equal B0,B1, respectively. Every restriction
(Q_j u_i,Q_j v_i) has all six minors zero and a nonzero entry, so rank
is exactly one. At its first nonzero component n set
(alpha,beta)=(-Q_j v_i[n],Q_j u_i[n]), h=alpha u_i+beta v_i.
Then h is nonzero and spans the unique intersection with ker Q_j.
Restore lambda=h_z/g_j(z), errors h_x−lambda g_j(x) for x in I_j,
and −lambda g_j(x) for x in K_j. No zero is discarded.

| Plane | Row | First nonzero (Q u,Q v) | (alpha,beta) | lambda | Weights on increasing I then K |
| --- | ---: | --- | --- | ---: | --- |
| L0 | 1 | (0,16) | (81,0) | 0 | (81,0,0,0) |
| L0 | 2 | (12,0) | (0,12) | 0 | (12,0,0,0) |
| L0 | 3 | (0,52) | (45,0) | 0 | (45,0,0,0) |
| L0 | 4 | (54,0) | (0,54) | 0 | (54,0,0,0) |
| L1 | 1 | (46,78) | (19,46) | 66 | (14,88,84,5) |
| L1 | 2 | (44,0) | (0,44) | 0 | (0,78,0,0) |
| L1 | 3 | (61,0) | (0,61) | 0 | (0,42,0,0) |
| L1 | 4 | (87,84) | (13,87) | 82 | (12,48,75,23) |

Extending h by zero off S, the restored error e satisfies
h−e=lambda g_j on all sixteen labels. Hence all eight original shifted
moment differences vanish. The complete 128 pointwise entries and
64 moment residuals are saved and independently replayed. The two full
rows on L1 remain explicit and do not repair its failed rows.

In particular row two has Q_2 E_12=Q_2 E_18=0,
Q_2 E_1=(12,60,56,19) and Q_2 u1=(44,36,37,14), both nonzero.
Its intersection lines on L0 and L1 are exactly F E_12 and F E_18.
Since z_2=1, their z_2 coordinates vanish, forcing lambda zero. The
two outside error weights therefore vanish. L109 requires nonzero
lambda and both overlap weights for every actual full four-error, so
neither exhaustive plane can satisfy the hypotheses.

For arbitrary original bases u_original=A u_i+B v_i,
v_original=C u_i+D v_i, Delta=AD−BC!=0, inversion expresses h's
first original coefficient as (D alpha−C beta)/Delta. Thus the exact
finite-direction condition for each table row is D alpha−C beta!=0.
If it fails the direction is omitted from the original finite chart;
otherwise divide h and e by that first coefficient. Every zero weight
and homogeneous moment identity survives. This argument retains
arbitrary, possibly nonrational A,B,C,D and never replaces a prescribed
chart by a favorable one. Every finite-gate coefficient pair is replayed.

### Complete replay and limits

Reproduce from this notebook:

    python3 -B scripts/seven-coordinate/second_unmatched_locus_gates.py
    python3 -B scripts/seven-coordinate/verify_second_unmatched_locus_gates.py

Full certificates are `scripts/seven-coordinate/second-unmatched-locus-gates.json`
and `scripts/seven-coordinate/second-unmatched-locus-gates-replay.json`.
The producer specializes the inspected L133 method, reusing direct
product, fraction-free determinant and L109 gate helpers. The verifier
imports no producer helper. It constructs H by powers of 8 and obtains
g_j(x), for x in S union K_j, by differentiating X^16−1 at its simple root:

    g_j(x)=16*x^15/product_(y in (S union K_j) minus {x})(x-y).

All denominators are nonzero. Independently scaled ratio covectors
recover every original c_jx and exterior entry. Column elimination
recovers the complete basis; rational elimination independently evaluates
the exact integer minor. All homogeneous coefficients, affine division,
Bezout and infinity identities are checked. Every one of seven nonzero
exterior pivots and all 73 nonzero projection-component choices reproduce
the same intersection and weights up to a verified nonzero scalar.
The complete original moments, pointwise identities and prescribed-chart
coefficients are checked for all eight rows, including both successes.

Actual/required complete loci are 1/1: two points, eight rank-one row
gates, six lambda-zero rows, two full rows, zero passing planes and zero
unresolved components. Both paths share Python and residue arithmetic;
that same-step replay alone is not proof-assistant verification or a
separate critical audit. The separate audit is recorded below.
This exact finite input retains the inherited computational qualifications.

Only this ordered occurrence is excluded here. No enlarged census,
recursive deletion, four-row converse, additional-row test, t=0 realization,
sixteen-event witness, third/pair assembly or universal representation is
inferred. In particular L109's r>=6 converse is not applied to four rows.
Historical 154/118/100 residual lists remain unchanged; independent
challenge definitions, extraction and the global count gap remain open.

### Separate critical audit, 2026-10-21

Step `2026-10-21-mca-398-second-unmatched-critical-audit` completed the
unchanged invocation-start EXPLORE target in
`drafts/literature/2026-10-21-second-unmatched-critical-audit-review.md`
as RESEARCH / REPRODUCTION / proof_audit. The whole proof, both complete
programs and all their called mathematical helpers were inspected.
L109's necessary nonzero-wedge, projection, full-weight and prescribed-
chart arguments and L125's original domain and complete-kernel provenance
were checked against their separately audited scopes. The ready primary
coverage above was reused. No mathematical defect or new dependency was
found; this validates the existing local input, without a new exclusion
or progress beyond the sources checked.

Reproduce the separate audit from this notebook:

    python3 -E -B scripts/seven-coordinate/audit_l135_locus.py

The full manifest, complete original record, execution records and all
thirty checks are in `scripts/seven-coordinate/l135-critical-audit.json`;
the complete execution log is
`scripts/seven-coordinate/l135-critical-audit-replay.log`.
The wrapper copies the four inspected programs/helpers, original shard
and two complete certificates into an isolated temporary directory. Both
programs run with assertions enabled (`-E` ignores inherited Python
optimization settings), reconstructing all evidence. Every copied file
matches its original byte for byte afterward, and all seven original
files are unchanged. All 30/30 audit checks pass with zero failures.
No new support search is performed.

The source binding uses the entire `/cases/155` record, not its preview
or rank flag. Independent full-universe generation gives the displayed
third and fourth labels at indices 94 and 539. The four explicit ROWS
arguments reach every block/gate call; the direct helper's historical
SUPPORTS constant is unused. Differentiation at simple roots of X^16-1
gives the verifier's nonzero g-values. Multiplying its ratio covectors
by g(z)g(x) gives the original covectors, so all 504 exterior matrix
entries are compared in the original normalization. Column elimination
tracks actual relations; all 48 null residuals, the identity on free
columns 1,17 and the nonzero original minor prove the complete kernel.
Rational elimination and fraction-free elimination agree on the exact
integer determinant above and residue 23. These coefficient identities
give rank nineteen and the same two-dimensional kernel over every
extension, not just the base field.

All 35 homogeneous coefficient triples, all affine quotient/Bezout
identities and the separate infinity case agree. In particular the
relation on (1,12,18,33) is st itself, while every other restriction is
a multiple of st. Thus there are exactly the two stated projective
points over every extension. Each is explicitly a nonzero wedge; no
root search or descent of an original chart substitutes for this argument.

All eight row projections have rank exactly one. Reconstructed directions,
lambda values, all four weights per row, all 128 pointwise entries and
64 original shifted moments agree, including the two full rows. Every
one of the seven nonzero exterior pivots and all 73 nonzero projection-
component choices is checked, with a nonzero proportionality scalar for
each recovered intersection, lambda and weight vector. These complete
records were inspected, not merely their success flags. The six failed
rows retain all zero weights. Row two rejects both exhaustive planes:
its intersections are F E_12 and F E_18, respectively, and z_2=1 forces
lambda=0. In particular its two outside weights vanish.

For the original-basis matrix [[A,C],[B,D]], inversion gives the exact
first coefficient (D alpha-C beta)/(AD-BC). If its numerator is zero,
the projective recovery is outside the prescribed finite chart; otherwise
normalization multiplies every recovered weight by the same nonzero
scalar. Therefore neither row-two failure can be repaired, over F or any
extension. This is a symbolic basis-change argument, not a finite chart
sample or a favorable-chart substitution. Only L109's necessary direction
is applied; its r>=6 converse supplies nothing for these four rows.

The argument and direct mathematical inputs are unchanged, so this audit
does not alter PROOF.md or DAG.md. It supersedes their historical pending-
audit wording for L135. Shared Python/residue arithmetic and the inherited
finite-certificate qualifications remain; no proof-assistant check is
claimed. Historical 154/118/100 lists, all stopped-route evidence,
universal representation/extraction, challenge definitions and the global
11/q–16/q gap remain unchanged.

## Mathlib

Full matching indexed locus/exclusion: **not checked**. Supporting
coding, exterior, polynomial and matrix coverage: **not checked** here;
unknown coverage is not absence. Precise imported sources and the finite
certificate qualification are stated above. No novelty claim is made.
