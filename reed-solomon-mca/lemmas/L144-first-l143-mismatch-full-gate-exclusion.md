# L144 — Complete locus and selected-row exclusion of (238,647)

## Hypotheses

Use F=F_(97^20), H={x in F_97^*:x^16=1}, k=8, shifted moments of
orders one through eight, and the pinned same-support event on
1/4<=delta<5/16. Both coefficient syndromes lie in U_S for
S={1,8,12,18,22,27,33}. For the exclusion assume sixteen original finite
events, L104's represented t=0 class, and actual nonzero Hankel determinant
and coordinate-locator polynomials. Original weights and prescribed charts
are arbitrary over F. Retain L109's inherited
L010/L103/L104/L040/L069/L086/L056 finite-certificate qualifications.

The four assumed actual error supports, in order, are

| Row | I in S | K in J=H minus S |
| --- | --- | --- |
| 1 | {1,8} | {47,50} |
| 2 | {12,18} | {64,75} |
| 3 | {8,12} | {70,79} |
| 4 | {18,33} | {89,96} |

Use L109's original covectors, z=min(S minus I), and increasing exterior
columns. In L125's full zero-based lexicographic universe
binom(S,2) times binom(J,2), these are occurrence (238,647).
Its exact original record is `scripts/seven-coordinate/new-pair-filter/third-238.json`
at `/cases/182`; audited L143 binds it at `/overlay/0` of
`scripts/seven-coordinate/l141-l142-literal-reuse.json`.
No universal representation or fixed-pair extraction is assumed.

## Conclusion

The complete original 24-by-21 stack has rank nineteen. Its homogeneous
decomposable kernel locus is exactly s*t=0 over every extension of F_97,
including infinity. Both exhaustive planes have rank-one projection at
every selected row and fail necessary lambda/full-weight gates. Thus this
one indexed occurrence cannot belong to the hypothesized equality pencil
in any prescribed original chart.

Complete same-step independent replay and the separate step-435 critical
audit below pass. All 154 historical residuals and 44 L143 mismatches remain
preserved; this is one separately certified exclusion, not a revised
partition, third/pair exclusion, event construction or global improvement.
The frozen-model interval stays 11/q–16/q.

## Proof

### Assessed tools and exact scope

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-23-first-l143-mismatch-locus-review.md`.
This is RESEARCH / REPRODUCTION / calculation of one record-specific
specialization, with no claim of progress beyond checked sources.
The existing exact-statement/stronger-result comparison and scoped
duplicate search are reused. ATTEMPTS/045–046 remain valid; no L141 locus,
L142 capacity, basis conversion or exhausted literal sweep is imported.

Through L109 import J. I. Hall, *Notes on Coding Theory*, undated author
GRS chapter, [Theorem 5.1.1 and proof, pp. 63–64](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
and I. Marquez-Corbella–R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
DOI 10.1016/j.ffa.2016.04.004,
[accepted manuscript 2016-02-29, section 5, Definitions 5.1–5.2 and
GRS shortening formula after Lemma 5.3, pp. 7–8](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf).
Here the sixteen labels are distinct and multipliers nonzero. Each row
shortens exactly seven J-minus-K labels through positive dimensions eight
to one; retained label-difference multipliers are nonzero. No stronger
parameter assertion of Lemma 5.3 is needed.

K. Conrad, [*Exterior Powers*, Theorems 4.2, 7.1, 7.5 and proofs,
pp. 11–12,23–25](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
undated 47-page author PDF inspected in the assessment, covers ordered
exterior bases and the plane represented by an independent nonzero wedge,
over every field. Use exterior degree two in dimension seven; L109 gives
the explicit equations and reconstruction. J. S. Milne,
[*Fields and Galois Theory*, Kea Books 2022, sections 1.6–1.9,
pp. 5–7, and Proposition 2.17, p. 34](https://www.jmilne.org/math/Books/FT0.pdf),
covers division/Bezout and extension-invariance of gcds. The explicit split
identity below leaves no irreducible, repeated-root or whole-line branch.
These general results are imported, not reproved; the needed work is
the original coefficient and gate computation, which the citations do
not supply.

### Complete original kernel

Reproduce from this notebook with assertions enabled:

    python3 -E -B scripts/seven-coordinate/first_l143_mismatch_locus_gates.py
    python3 -E -B scripts/seven-coordinate/verify_first_l143_mismatch_locus_gates.py

Full certificates are `scripts/seven-coordinate/first-l143-mismatch-locus-gates.json`
and `scripts/seven-coordinate/first-l143-mismatch-locus-gates-replay.json`.
The complete original record equals audited L143's overlay, including
both full ordered null vectors and all saved residuals. Source bytes
are hashed and bound to the passing separate L143 audit. The full
756-element universe places the selected third and fourth at exactly
238 and 647; their four supports are distinct and pairwise linear.

For each row set g_K(X)=product_(y in J minus K)(X-y). Form the four
covectors c_x=g_K(z)E_x^*−g_K(x)E_z^* for x in (S minus I) minus {z},
and their six exterior products. The producer rebuilds this exact original
stack, all 48 basis residuals, and the original minor with zero-based rows

    0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,19,21

and columns all except 7 and 14. Its determinant is 84 modulo 97,
independently checked by fraction-free integer elimination. The two null
vectors have identity coordinates on the free columns 7,14. A nonzero
19-minor gives rank at least nineteen, and these two independent null
vectors give rank at most nineteen. Consequently their span is the
entire kernel after any scalar extension.

Writing e_x for the S-coordinate vector, the ordered basis is

    B0 = e_8 wedge e_18,
    B1 = 15 e_1 wedge e_12 + 84 e_8 wedge e_12
         + 73 e_12 wedge e_18 + 63 e_12 wedge e_22
         + 62 e_12 wedge e_27 + e_12 wedge e_33.

The verifier imports no producer or helpers. For x in S union K it
instead uses g_K(x)=16*x^15/product_(y in (S union K) minus {x})(x-y),
the derivative identity for X^16−1 at its simple root x. All denominators
are nonzero. Normalized ratio covectors are scaled back to the original
c_x before comparing all 504 matrix entries. Column-relation elimination
reconstructs both complete ordered null vectors independently of the
producer's row elimination. Rational Gaussian determinant evaluation also
agrees with the full saved integer determinant and residue 84.

### All homogeneous components, including infinity

Restrict all 35 equations p_ab*p_cd−p_ac*p_bd+p_ad*p_bc to
p=s*B0+t*B1. Exactly four are nonzero:

| Increasing label quadruple | Restriction |
| --- | --- |
| (1,8,12,18) | 82*s*t |
| (8,12,18,22) | 34*s*t |
| (8,12,18,27) | 35*s*t |
| (8,12,18,33) | 96*s*t |

Every other coefficient triple is zero. Since 96 is nonzero, the
homogeneous ideal on this line is precisely (s*t). On s=1, the monic gcd
is t; all 35 exact quotients are saved, and the Bezout identity is
96 times the last displayed restriction = t. Independently checking
every coefficient, quotient and identity proves the affine locus over
every extension. At s=0 all 35 restrictions vanish directly, so infinity
is retained. Thus precisely [s:t]=[1:0],[0:1] occur. These are distinct,
with no further component or multiplicity issue. This conclusion uses
coefficient identities, not sampling of F_97 points.

The reconstructed independent plane representatives, in increasing S
coordinates, are respectively

    u0=(0,1,0,0,0,0,0), v0=(0,0,0,1,0,0,0),
    u1=(1,25,0,21,54,67,84), v1=(0,0,15,0,0,0,0).

Their wedges are exactly B0 and B1. In particular the second plane
contains e_12; it is not inferred from a failed sufficient filter.

### Complete selected-row and chart gates

For each representative compute Q_j*u,Q_j*v, all six projection minors,
and a nonzero component n. All eight projections have rank exactly one.
Put (alpha,beta)=(-(Q_j*v)_n,(Q_j*u)_n), h=alpha*u+beta*v and
lambda=h_z/g_K(z). The four error weights in I-then-K order are
(h_i−lambda*g_K(i))_(i in I), (−lambda*g_K(k))_(k in K).
Every g_K value on S union K is nonzero. The complete gate results are:

| Point | Row | (alpha,beta) | lambda | Four error weights |
| --- | --- | --- | --- | --- |
| [1:0] | 1 | (53,0) | 0 | (0,53,0,0) |
| [1:0] | 2 | (0,75) | 0 | (0,75,0,0) |
| [1:0] | 3 | (9,0) | 0 | (9,0,0,0) |
| [1:0] | 4 | (0,25) | 0 | (25,0,0,0) |
| [0:1] | 1 | (51,51) | 24 | (58,32,57,90) |
| [0:1] | 2 | (0,44) | 0 | (78,0,0,0) |
| [0:1] | 3 | (0,75) | 0 | (0,58,0,0) |
| [0:1] | 4 | (13,51) | 82 | (35,48,75,23) |

The first plane fails all four lambda gates. The second fails rows two
and three while retaining full intrinsic recoveries at rows one and four.
This is sufficient to reject both exhaustive planes by L109's necessary
direction. There is no use of its r>=6 converse on these four rows.

All 128 pointwise identities h−e−lambda*g_K=0 on H and all 64 original
shifted-moment residuals are zero. The verifier reconstructs all weights
and identities independently. It also checks every nonzero exterior
pivot (seven in total) and every nonzero projection-component choice
(82 tests), obtaining nonzero proportional intersection representatives
and proportionally identical lambda and weights. Thus a pivot choice
cannot repair a zero weight; all division domains are retained.

For any prescribed original basis
u_original=A*u+B*v, v_original=C*u+D*v with AD−BC nonzero, the original
first coefficient of h is (D*alpha−C*beta)/(AD−BC). Each row retains
the corresponding condition D*alpha−C*beta nonzero with the table's
exact coefficients. If it vanishes, that direction is omitted. Otherwise
normalization divides every recovered weight by this same nonzero first
coefficient. Hence zero lambda and weights remain zero in every chart,
including nonrational charts. Passing rows are retained rather than
misreported as failures; neither plane passes every necessary gate.

L109 puts the actual nonzero independent wedge in this complete kernel
before any gate is used. Both possible planes have now been rejected,
contradicting simultaneous actuality of the four assumed supports under
the equality hypotheses. This excludes only occurrence (238,647).

Both completed programs report zero failures and no unresolved component.
They share Python and residue arithmetic; same-step independent replay
is not a separate critical audit or proof-assistant verification. No
historical list is shortened, no other mismatch is classified, and no
third/pair assembly, support census, nonpersistence construction or
challenge-level conclusion follows. Universal representation/extraction
and certified challenge definitions remain unresolved.

### Separate critical audit, 2026-10-23

Step `2026-10-23-mca-435-l144-critical-audit` used the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-23-l144-critical-audit-review.md`.
The complete proof, both complete programs, every called helper and import
initialization were inspected. L109's necessary independent-wedge,
projection, full-weight and chart arguments and separate audit were checked;
L125's original-kernel certification and L143's original-record binding
were reused with their separate audit qualifications. No mathematical
defect or changed direct dependency was found. This validates the existing
restricted reproduction, without a result beyond the sources checked.

Reproduce this separate audit with assertions enabled:

    python3 -E -B scripts/seven-coordinate/audit_l144.py

The full report is `scripts/seven-coordinate/l144-critical-audit.json`.
All 146/146 checks pass, with zero failures. Both entire producer/replay
outputs reproduce byte for byte in an isolated notebook-shaped tree.
All fourteen bound original inputs remain byte unchanged. Only the two
L144 programs run; neither imported helper's historical main routine nor
any historical filter, reference sweep or support census is executed.
The audit wrapper checks complete saved evidence, not summary previews.

The L125 audit hashes bind the original third-238 shard and helper;
L143's passing 6,674-check audit binds that same shard and its overlay.
The exact `/cases/182` and `/overlay/0` records agree in every field.
Independent full-universe indexing agrees with (238,647). All 504 original
matrix entries, the nonzero 19-minor of residue 84, its full integer
determinant 301994834048563991836699490827272192, both ordered null vectors,
identity free coordinates 7,14 and all 48 null residuals agree. The rank
proof therefore binds the entire extension kernel, not a sampled subset.
The derivative and direct-product constructions agree entrywise; column
relations, modular elimination, fraction-free integer elimination and
rational determinant elimination have the distinct roles stated above.

All 35 homogeneous coefficient triples agree with the four displayed
nonzero restrictions. Every affine quotient and Bezout coefficient is
checked; direct infinity inclusion is retained. Since a nonzero constant
multiple of s*t is itself among the equations and every other equation
is a multiple of it, precisely the two displayed projective points remain
over any extension. There is no untested extension-root component.
Both independent plane reconstructions and all eight selected-row gate
records agree with the written table, including the second plane's two
passing rows. Every projection has rank one; six rows have lambda zero.
All 128 pointwise identities and 64 original shifted moments vanish.
The complete seven exterior-pivot and 82 projection-component cases agree,
with nonzero proportional recovery vectors, lambdas and weights.

The arbitrary-chart conclusion is algebraic, not finite chart sampling:
solving the invertible basis change gives the displayed first coefficient
(D*alpha-C*beta)/(AD-BC). Its zero case omits the recovery; its nonzero
case rescales all weights by a nonzero scalar. Neither repairs lambda
zero. L109 first puts the actual independent nonzero wedge in this entire
kernel; the necessary rank-one and full-weight gates then reject both
planes. Its r>=6 converse is never used on four rows. A plane's passing
rows supply no nonpersistence or event-completion assertion.

The historical 154 residuals and 44 mismatches remain preserved, together
with ATTEMPTS/045–046. This audit adds no third/pair assembly, new locus,
other occurrence, universal representation/extraction or global bound.
Shared Python/residue arithmetic and inherited finite certificates remain
qualifications; no proof-assistant verification is claimed. This section
supersedes historical pending-audit wording in the unchanged overview and
certificates; the mathematical argument and DAG inputs are unchanged.

## Mathlib

Full matching and supporting coverage were not checked; unknown coverage
is not asserted absence. The claim rests on the explicit finite
certificates, necessary L109 direction and cited standard tools above.
