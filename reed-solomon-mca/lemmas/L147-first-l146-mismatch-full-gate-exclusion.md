# L147 — Complete locus and selected-row exclusion of (274,539)

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, k=8, shifted moments
of orders one through eight, and the pinned same-support event on
1/4<=delta<5/16. Assume sixteen actual original finite events, L104's
represented t=0 class, both coefficient syndromes in U_S for
S={1,8,12,18,22,27,33}, and actual nonzero Hankel determinant and
coordinate-locator polynomials. Original weights and the prescribed chart
are arbitrary over F. Retain L109's inherited
L010/L103/L104/L040/L069/L086/L056 finite-certificate qualifications.
No universal representation or fixed-pair extraction is assumed.

The four assumed actual error supports, in order, are:

| Row | I in S | K in J=H minus S |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,75} |
| 3 | {8,18} | {70,79} |
| 4 | {12,33} | {89,96} |

Use L109's original covectors, z=min(S minus I), lexicographic covector
pairs and increasing exterior columns. These are occurrence (274,539) in
L125's full zero-based lexicographic universe binom(S,2) times binom(J,2).
The complete original record is `scripts/seven-coordinate/new-pair-filter/third-274.json`
at `/cases/155`; audited L146 binds it at `/overlay/7` of
`scripts/seven-coordinate/l144-remaining-literal-reuse.json`.

## Conclusion

The complete original 24-by-21 stack has rank nineteen. Its homogeneous
decomposable kernel locus is exactly s*t=0 over every extension of F_97,
including infinity. Both exhaustive planes have rank-one projection at
every selected row, but both fail the second row's necessary lambda and
full-weight gates. Thus this single indexed occurrence cannot belong to
the hypothesized equality pencil in any prescribed original chart.

Complete same-step independent replay and the separate critical audit
below pass. All 154 historical residuals, 44 L143 mismatches and 26 L146
mismatches remain preserved. No third/pair exclusion, actual-event
construction, universal extraction or global improvement follows.
The frozen-model interval stays 11/q–16/q.

## Proof

### Imported tools and scope

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-24-first-l146-mismatch-locus-review.md`.
This is RESEARCH / REPRODUCTION / calculation of its exact target.
Reuse its primary coverage, stronger-result and duplicate comparisons;
no originality or progress beyond the checked sources is claimed.
ATTEMPTS/045–046 remain valid. L144 is a computational method precedent,
not a mathematical input: its different kernel's locus is not imported.

Through L109 import J. I. Hall, *Notes on Coding Theory*, undated author
GRS chapter, [Theorem 5.1.1 and proof, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, Definitions 5.1–5.2 and
GRS shortening formula after Lemma 5.3, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
The sixteen labels are distinct, multipliers nonzero, and k=8. Each row
shortens exactly seven J-minus-K labels through positive dimensions eight
to one, with all retained label-difference multipliers nonzero. No stronger
parameter assertion of Lemma 5.3 is imported.

K. Conrad, [*Exterior Powers*, Theorems 4.2, 7.1, 7.5 and proofs,
pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
undated 47-page author PDF inspected in the assessment, covers ordered
exterior bases and independent nonzero wedges over every field. Apply it
in dimension seven and degree two. L109 supplies the explicit homogeneous
criterion and pivot reconstruction. J. S. Milne,
[*Fields and Galois Theory*, Kea Books 2022, sections 1.6–1.9,
pp. 5–7 and Proposition 2.17 with proof, p. 34](https://www.jmilne.org/math/Books/FT0.pdf),
covers polynomial division/Bezout and extension-invariance of gcds.
The split coefficient identity below exhausts the locus without any
irreducible or repeated-root branch. These standard tools are imported;
the original matrix coefficients and gates require this specialization.
No general coding, exterior-power or polynomial theorem is reproved.

### Entire original extension kernel

Reproduce from this notebook with assertions enabled:

    python3 -E -B scripts/seven-coordinate/first_l146_mismatch_locus_gates.py
    python3 -E -B scripts/seven-coordinate/verify_first_l146_mismatch_locus_gates.py

Full certificates are `scripts/seven-coordinate/first-l146-mismatch-locus-gates.json`
and `scripts/seven-coordinate/first-l146-mismatch-locus-gates-replay.json`.
The complete original record agrees with L146's saved overlay, including
both ordered null vectors and all original residuals. Its passing separate
audit hashes bind both source bytes and overlay. The universe independently
places the new supports at 274 and 539; all four supports are distinct and
pairwise linear. This establishes provenance, not decomposability.

Set g_K(X)=product_(y in J minus K)(X-y). For each selected row put
c_x=g_K(z)E_x^*−g_K(x)E_z^* for x in (S minus I) minus {z}, and form
its six exterior products. Rebuild this original stack and the original
19-minor with zero-based rows

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21

and columns all except 6 and 17. Its integer determinant is

    -4597290239000163969164847677870211072,

with nonzero residue 16 modulo 97. Modular elimination and independent
fraction-free integer elimination agree. Writing e_x for the S-coordinate
vector, the two ordered null vectors are

    B0 = e_8 wedge e_12,
    B1 = 15 e_1 wedge e_18 + 84 e_8 wedge e_18
         + 31 e_12 wedge e_18 + 63 e_18 wedge e_22
         + 62 e_18 wedge e_27 + e_18 wedge e_33.

Their coordinates on columns 6,17 are the identity matrix, so they are
independent. Every one of their 48 original stack residuals is zero.
The nonzero minor gives rank at least nineteen; the independent null
vectors give rank at most nineteen. These identities persist under
scalar extension, so their span is the entire extension kernel.

The verifier imports neither producer nor mathematical helpers. On
S union K it uses

    g_K(x)=16*x^15/product_(y in (S union K) minus {x})(x-y),

from differentiating X^16−1 at its simple root x. Every denominator is
nonzero. Independently normalized ratio covectors are scaled back to c_x;
all 504 original entries agree. Column-relation elimination reconstructs
both complete ordered null vectors. Rational Gaussian elimination checks
the full integer determinant and residue independently. No historical
filter main routine or reference sweep is run.

### Homogeneous locus over every extension

For p=s*B0+t*B1 restrict all 35 increasing-index relations
p_ab*p_cd−p_ac*p_bd+p_ad*p_bc. Exactly four are nonzero:

| Label quadruple | Restriction |
| --- | --- |
| (1,8,12,18) | 15*s*t |
| (8,12,18,22) | 63*s*t |
| (8,12,18,27) | 62*s*t |
| (8,12,18,33) | s*t |

Every other coefficient triple is zero. Thus their homogeneous ideal on
this projective line is exactly (s*t), over F_97 and every extension.
On s=1 the monic gcd is t: all exact quotients are saved and the last
displayed relation itself is the Bezout certificate. Direct substitution
s=0 verifies all 35 equations at infinity. Exactly [1:0] and [0:1] remain;
there is no additional extension-root, whole-line or exceptional component.
The coefficient, division and Bezout identities are independently replayed;
prime-field root sampling is not used to exclude extension roots.

L109's nonzero-pivot reconstruction gives respective representatives,
in increasing S coordinates,

    u0=(0,1,0,0,0,0,0), v0=(0,0,1,0,0,0,0),
    u1=(1,25,15,0,54,67,84), v1=(0,0,0,15,0,0,0).

Their wedges are exactly B0 and B1. The second plane contains e_18;
this follows from the complete kernel calculation, not a failed filter.

### All selected-row gates and the prescribed chart

For each plane compute Q_j*u,Q_j*v and all six projection minors. All
eight projections have rank exactly one. Select a nonzero component n,
put (alpha,beta)=(-(Q_j*v)_n,(Q_j*u)_n), h=alpha*u+beta*v and
lambda=h_z/g_K(z). The four error weights in I-then-K order are
(h_i−lambda*g_K(i))_(i in I), (−lambda*g_K(k))_(k in K).
Every g_K value on S union K is nonzero. The complete results are:

| Point | Row | (alpha,beta) | lambda | Four error weights |
| --- | --- | --- | --- | --- |
| [1:0] | 1 | (81,0) | 0 | (0,81,0,0) |
| [1:0] | 2 | (0,75) | 0 | (75,0,0,0) |
| [1:0] | 3 | (9,0) | 0 | (9,0,0,0) |
| [1:0] | 4 | (0,25) | 0 | (25,0,0,0) |
| [0:1] | 1 | (19,46) | 66 | (14,88,84,5) |
| [0:1] | 2 | (0,44) | 0 | (0,78,0,0) |
| [0:1] | 3 | (0,38) | 0 | (0,85,0,0) |
| [0:1] | 4 | (13,87) | 82 | (12,48,75,23) |

The first plane fails all four lambda gates. The second fails rows two
and three, retaining full intrinsic recoveries at rows one and four.
In particular row two rejects both exhaustive planes by the necessary
L109 gates. No r>=6 converse is applied to four selected rows.

Every one of 128 pointwise identities h−e−lambda*g_K=0 on H and all
64 original shifted-moment residuals are zero. The verifier reconstructs
all gates, weights and identities independently, retains every zero weight,
and checks all seven nonzero exterior pivots and 67 nonzero projection-
component choices. Alternative representatives are nonzero proportional,
with proportionally identical lambda and weights. Every inverted exterior,
projection, label-difference or g_K denominator is explicitly nonzero.
There is no rank-zero branch in this complete locus; L109's actual
nonpersistence would reject one if present.

For any prescribed original basis u_original=A*u+B*v,
v_original=C*u+D*v with AD−BC nonzero, the first original coefficient
of h is (D*alpha−C*beta)/(AD−BC). Retain the condition
D*alpha−C*beta nonzero separately for every table row. If it vanishes,
the direction is omitted; otherwise normalization divides all weights
by the same nonzero first coefficient. Intrinsic zero lambda/weights
therefore remain zero in every original chart, including nonrational
charts. No change of chart can repair either rejected plane.

L109 puts an actual independent nonzero wedge in the complete kernel
before these gates are applied. Its only two possible planes now fail
necessary gates, contradicting the four supports' simultaneous actuality
under the equality hypotheses. Only occurrence (274,539) is excluded.

Both programs complete with zero failures and zero unresolved components;
zero intrinsic survivors is the required threshold for this exclusion.
They share Python and residue arithmetic. Same-step independent replay
is not a separate critical audit or proof-assistant verification.
No historical list is shortened. Other residuals, assembly, universal
representation/extraction and certified challenge definitions remain open.

### Separate critical audit, 2026-10-24

Step `2026-10-24-mca-447-l147-critical-audit` completed the exact
invocation-start SPECIALIZE target in
`drafts/literature/2026-10-24-l147-critical-audit-review.md` as
RESEARCH / REPRODUCTION / proof_audit. The complete proof, producer,
independent verifier, both called helpers and import initialization were
inspected. L109's necessary independent-wedge, projection, full-weight
and prescribed-chart proofs and prior audit were checked, together with
L125's original-kernel provenance and L146's binding and audit. Ready
primary coverage and the recorded duplicate/failure comparison were reused.
No different-kernel locus or gate conclusion is imported from L144.

Reproduce this separate audit with assertions enabled:

    python3 -E -B scripts/seven-coordinate/audit_l147.py

The full evidence is `scripts/seven-coordinate/l147-critical-audit.json`.
All 131/131 checks pass with zero failures. Both complete original outputs
reproduce byte for byte in an isolated notebook-shaped tree; all fourteen
bound original inputs remain unchanged. Only the two L147 programs run;
the imported historical main routines do not execute. L125's older
complete-replay verdict and 100,764/100,764 scope are distinguished from
L146's 2,344 passing checks. The exact shard, master, overlay, helpers and
essential input proofs bind to their applicable prior audit hashes.

The independent original 504-entry reconstruction, exact integer determinant
and residue 16, complete ordered null basis and identity free coordinates
6,17 agree with the displayed proof and original record. The nonzero minor
and two independent null vectors certify rank nineteen over every extension.
Every homogeneous coefficient is checked: the four nonzero restrictions
are 15*s*t, 63*s*t, 62*s*t and s*t. Hence the ideal is exactly (s*t),
not merely an affine gcd or a finite-field root test. Division/Bezout and
the direct infinity test agree, exhausting exactly [1:0] and [0:1].

Both displayed planes and all eight full projection/weight/chart records
agree with complete independent replay. All 128 pointwise identities,
64 original shifted moments, seven nonzero exterior pivots and 67
projection-component choices pass. Every required denominator is nonzero;
alternative intersection representatives scale lambda and all weights by
a nonzero factor. The first plane fails all four rows; the second fails
rows two and three and retains passing rows one and four. In particular
both fail row two, so zero intrinsic survivors meets the required zero.
There is no unresolved extension component or rank-zero branch.

For an arbitrary prescribed invertible basis, the first coefficient is
(D*alpha-C*beta)/(AD-BC). If its numerator vanishes the direction is
omitted; otherwise all recovered weights are divided by the same nonzero
coefficient. The row-two zero lambda and three zero weights persist,
including in nonrational charts. L109 supplies an actual nonzero wedge
before these necessary gates are used; its r>=6 converse is not invoked
for four rows. Passing rows do not construct actual events.

No mathematical defect, changed dependency or failed audit execution was
found. This validates an existing restricted reproduced input, adding no
indexed exclusion or progress beyond the checked sources. Shared Python
and residue arithmetic, inherited finite certificates and unchecked
Mathlib coverage remain qualifications. Historical 154/44/26 lists and
ATTEMPTS/045–046 are unchanged. Other residuals, assembly, universal
representation/extraction and certified challenge definitions remain open.
This verdict supersedes historical pending-audit wording in the unchanged
overview and certificates; the mathematical argument and DAG are unchanged.

## Mathlib

Full matching and supporting coverage were not checked; unknown coverage
is not evidence of absence. The claim rests on L109's necessary direction,
the cited standard tools and the explicit complete certificates above.
