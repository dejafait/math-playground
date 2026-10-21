# L067 — Antipodal triangle singleton pairs exclude thirteen additional recoveries

## Hypotheses

Use audited L057's full hypotheses: F=F_(97^20), H the order-sixteen
subgroup of F_97^*, nine distinct triangle labels, distinct original
finite gamma_i, lambda!=0 and p(1-p)q(1-q)r(1-r)!=0. Retain its
actual syndrome pencil, both-zero lifts, all relaxed fourth weights,
mu!=0,-1 and E=rho-(1-rho)mu!=0. Use audited L066's conditional
four-isolated-disjoint-P requirement, not an assumed total count.

Additionally, the three singleton pairs are antipodal:
Y={y,-y}, Z={z,-z}, W={w,-w}. They are disjoint. The ordered
shared labels P=(a,b,c) are any distinct labels outside these pairs.
The weights and original chart still range over F without descent.

## Conclusion

There are at most **three distinct additional isolated recovery scalars
with a four-support disjoint from P**, allowing zero fourth weights.
The number of such original finite parameters is also at most three.
The maximum three is attained by full recovered errors in the displayed
original-chart witness below.

Consequently this restricted family has at most **twelve distinct
additional relaxed recovery parameters**, counting isolated and both-zero
recoveries together. This is a finite-certificate restriction on antipodal
singleton pairs, not a uniform triangle bound or a global improvement.
A separate critical audit on 2026-10-11 found no mathematical defect in
this restricted bound, including full replay and independent scalar
aggregation. No complete challenge candidate or certified originality is
claimed.

## Proof

### Standard input and the six-singleton specialization

The recurrence input is already imported in L057: Przemek Chojecki,
*Shortening Bounds for Reed–Solomon MCA*, live author TeX v9.2,
July 17, 2026, DR2 (`drc:lem-locator-recurrence`) and DR6–DRC
(`drc:thm-exact-compiler`), source lines 2785–2935, including proofs
and zero-direction cases, [author source](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex).
This mutable source is not certified identical to ePrint 2026/1463.
Its distinct weighted Vandermonde columns, nonzero multipliers, R=8,
t=4 and multiplier x hypotheses are unchanged. No general recurrence
theorem is reproved. The ready triangle-count assessment supplies no
simultaneous bound for this restricted family; the additional work is
the evaluation reduction and complete finite count below.

First the following evaluation identity holds for **arbitrary** singleton
pairs, before imposing antipodality. Write S(X) for the product of all
six singleton factors, G_P for the product of the three shared factors,
and Q for the product of the other seven H factors. Thus
Q G_P S=X^16-1 and c_x=Q(x). For K disjoint from P put
f(X)=product_(k in K)(X-k). Define

\[
 u_Y=\sum_{y\in Y}\frac{f(y)}{S'(y)},\qquad
 u_Z=\sum_{z\in Z}\frac{f(z)}{S'(z)},\qquad
 T_Y(X)=\sum_{y\in Y}\frac{f(y)}{S'(y)}\frac{S(X)}{X-y},
 \quad T_Z(X)=\sum_{z\in Z}\frac{f(z)}{S'(z)}\frac{S(X)}{X-z}.
                                                               \tag{1}
\]

The polynomial quotients in (1) are exact, including f(y)=0.
At any singleton h, differentiation and h^16=1 give
c_h h G_P(h)=16/S'(h). L057's m=3 projected vectors are therefore
the scalars 16u_Y and 16u_Z. A support is isolated exactly when both
u's are nonzero; its scalar is mu=u_Z/u_Y in F_97^*. Require mu!=-1.
Both-zero supports are precisely u_Y=u_Z=0 at this projected stage;
they still require L057's restored lift and finite gates.

For x in P, the L057 interpolant on P is
ell_x(h)=G_P(h)/[(h-x)G_P'(x)]. Differentiation at x gives
c_x x=16/[G_P'(x)S(x)]. Substituting both identities in L057 (6)
and cancelling only nonzero label factors yields

\[
 \frac{\beta_x^Y}{c_x}
 =-\frac{S(x)}{f(x)}\sum_{y\in Y}\frac{f(y)}{S'(y)(y-x)}
 =\frac{T_Y(x)}{f(x)},\qquad
 \frac{\beta_x^Z}{c_x}=\frac{T_Z(x)}{f(x)}.                       \tag{2}
\]

All x avoid S and K, so every denominator used here is nonzero.
The leading X^5 coefficient of T_Z-mu T_Y is u_Z-mu u_Y=0.
Thus B=T_Z-mu T_Y has degree at most four. Set R(x)=B(x)/f(x).
L057's three restored equations become exactly

\[
 p=\frac{1-R(a)}{1+\mu},\qquad q=-\frac{R(b)}{\mu},
 \qquad r=R(c).                                                 \tag{3}
\]

This is a specialization of L057's full recovery equations, not an
inference of recovery from projected compatibility. In particular,
every isolated disjoint-P recovery forces the weights in (3) into
F_97, even when the initial weights and chart are over F. Conversely,
when the weight and finite gates pass, L057 gives all eight moments.
Zero fourth weights remain allowed throughout this count.

### Exhaustive label coverage by subgroup scaling

Multiplying every label by s in H preserves H and disjoint supports.
For the scaled union, Q'(sx)=s^7 Q(x). Taking lambda'=s^-7 lambda
preserves each actual base error under the coordinate permutation;
the normalized p,q,r and original gamma_i are unchanged. The j-th
moment is multiplied by s^j, an invertible row operation, preserving
all recovery systems, their isolated/both-zero classifications and
every original finite gate. This also follows directly in (1)–(3):
f'(sx)=s^4 f(x), S'_(scaled)(sx)=s^5 S'(x), u' =s^-1 u,
T'_(pair)(sx)=s^4 T_(pair)(x), and R'(sx)=R(x).

Choose s=y^-1 to normalize Y to {1,96}. Within-pair exchanges do
not change any formula. H has eight antipodal pairs. Choose ordered
Z and W from the other seven pairs: there are 7*6=42 cases. For
each case there are 10*9*8=720 ordered shared triples outside the
six singleton labels. For each triple there are binom(13,4)=715
supports disjoint from P, none equal to a base support. Thus this
enumeration covers the entire stated restricted family, using exactly
30,240 assignments and 21,621,600 support rows. No permutation of
shared roles or of the three pair roles is assumed as a symmetry.

### Exact certificate and independent equation replay

The producer in `scripts/triangle-recovery/antipodal_anchor_sweep.cpp`
precomputes (1)–(3), then enumerates the complete coverage above.
For each ordered assignment, supports appear in lexicographic H order.
It saves five bytes per support: kind, mu, p, q, r. Kinds are
0=both-zero projected row, 1=exactly one zero, 2=isolated mu=-1,
3=eligible isolated scalar failing a weight gate, 4=gated isolated row.
Unused entries are zero. The packed certificate is
`scripts/triangle-recovery/antipodal-anchor-rows.bin`, 108,108,000 bytes,
SHA256 `bf33edaa08cd2cafa51605f5b2f08e1ed70f9f7dafec11ed188f896bb6242e3c`.
The complete producer summary is `antipodal-anchor-sweep.json` in
the same directory. Both-zero rows are marked, not counted as isolated;
no claim is made that their projected test alone passes the lift.

The separate replay branch does not call the interpolation producer.
It independently constructs Q(x), L057's original projected sums (5),
the original three-node interpolants and beta equations (6), then (11).
It compares **every** classification and weight row against the packed
certificate, including all rejected rows. For every gated row it solves
the first four moment equations by four-column Vandermonde inversion
and checks all eight moment residuals against the original numerator.
The inversion is elementary field arithmetic shared only as a support
utility, not a recovery criterion. The two implementations share H,
support enumeration, field arithmetic and scalar aggregation; their
independence is limited to the evaluation/recovery formulas, and is
not by itself a substitute for the separate critical audit recorded below.

At each weight point the counter uses a 97-bit **set of scalars**, so
duplicate witnesses and zero fourth weights cannot inflate its count.
It omits E=0 only to enlarge the set. An actual original finite chart
removes at most its failed E scalar and cannot increase the count.
By L057 its retained scalar-to-original-parameter map is injective.

Replay found no failure in all 21,621,600 rows. The classification
counts, in kind order, are
(352,800; 3,299,328; 1,649,664; 952,056; 15,367,752).
Every one of the 15,367,752 gated rows passes all eight moments;
3,568,320 have a zero fourth weight and remain included. The complete
gated-fiber histogram is: 11,860,104 one-scalar fibers, 4,800 two-scalar
fibers and 96 three-scalar fibers, with none larger. Every assignment's
maximum is saved in `antipodal-anchor-verification.json`.
`check_antipodal_certificate.py` compares the complete summaries and
all 30,240 maxima, hashes the entire packed file, and independently
recovers the displayed maximal fiber by seven-column moment inversion.
Its full evidence is `antipodal-anchor-summary-check.json`.

Reproduce from the notebook directory:

```sh
clang++ -std=c++17 -O3 scripts/triangle-recovery/antipodal_anchor_sweep.cpp -o /tmp/mca-antipodal-anchor-sweep
/tmp/mca-antipodal-anchor-sweep produce scripts/triangle-recovery/antipodal-anchor-rows.bin scripts/triangle-recovery/antipodal-anchor-sweep.json
/tmp/mca-antipodal-anchor-sweep replay scripts/triangle-recovery/antipodal-anchor-rows.bin scripts/triangle-recovery/antipodal-anchor-verification.json
python3 scripts/triangle-recovery/check_antipodal_certificate.py
```

Thus the relaxed isolated disjoint-P maximum is three, below the
four-anchor threshold. This is a complete finite restriction on the
stated H-label family, not a sampled maximum or a general-domain theorem.

### Attainment and the twelve consequence

One maximal fiber has P=(27,79,22), Y={1,96}, Z={8,89}, W={12,85},
and (p,q,r)=(58,3,35). Choose original gamma=(0,1,2) and lambda=1;
then g=1, rho=2, E=2+mu. Independent seven-column inversion gives:

| K (ordered) | mu | numerator weights omega | E | original T |
|---|---:|---|---:|---:|
| (12,33,47,89) | 36 | (55,94,44,12) | 38 | 46 |
| (12,47,75,96) | 87 | (53,23,18,96) | 89 | 24 |
| (33,75,89,96) | 32 | (31,10,70,21) | 34 | 40 |

Every entry is in F_97 embedded in F. All weight gates pass; all
omega entries are nonzero; all eight residuals vanish. E is nonzero,
and the three T's are distinct and avoid 0,1,2. L057 supplies actual
weights omega/E, same-support failure, and the base pencil. This proves
attainment of three in this isolated subcount, not thirteen additional
recoveries or an exact full bad-set count. It also prevents extending
the older sampled at-most-two observation to this complete family.

Finally suppose there were thirteen distinct additional relaxed
recoveries for an antipodal-singleton triangle. Audited L066, invoking
L010 fullness only at that hypothetical threshold, requires at least
four isolated disjoint-P full-weight anchors. They are included in the
relaxed isolated count just proved, which is at most three. This is a
contradiction. Both-zero recoveries are retained through L066's separate
bound and anchor-selection argument; no projected both-zero case is
discarded as an actual recovery. Hence there are at most twelve
additional recoveries in this restricted family. Larger counts would
contain a thirteen-element subset and give the same contradiction.

Other singleton pairs and the uniform triangle bound remain open,
as do other incidence patterns, extraction and challenge definitions.
The global interval remains 11/q–16/q.

### Separate critical audit (2026-10-11, step 154)

The approved audit uses audited L057 and L066, with no change to this
lemma's hypotheses or direct mathematical inputs. The unchanged source
assessment is `drafts/literature/2026-10-11-antipodal-triangle-bound-audit.md`.
The following proof and implementation checks found no defect. This
validates an existing local result; it supplies no larger family bound
or claim of progress beyond the literature checked.

**Evaluation identities and extension-field coverage.** At a singleton h,
differentiating Q G_P S=X^16-1 gives
Q(h)G_P(h)S'(h)=16h^15=16/h. At x in P it gives
Q(x)G_P'(x)S(x)=16/x. Thus the projected scalars in L057 (5)
with J=P are exactly 16u_Y and 16u_Z, including all cancellations.
Both being nonzero is precisely the isolated case because their vectors
have dimension one; one zero cannot give an eligible scalar, and two
zeros require a separate lift. To check the sign in (2), divide L057's
beta formula by c_x and substitute

\[
\frac{c_hh\ell_x(h)}{xc_x}
 =\frac{S(x)}{S'(h)(h-x)}.
\]

The minus sign in beta becomes the denominator x-h in T_Y(x)/f(x).
The same substitution for Z gives R=(beta^Z-mu beta^Y)/c_x;
L057 (11) then yields all three equations (3), including the minus
sign for q. Every divided label difference, S(x), f(x), mu and
1+mu is nonzero in its stated case. No singleton evaluation f(h)
has been inverted. These identities therefore include supports meeting
singleton pairs and all zero recovered weights. The coefficient of X^5
in B is u_Z-mu u_Y=0, so its claimed degree bound also holds.
All row data lie in F_97. One actual isolated disjoint-P recovery forces
each of p,q,r to equal the corresponding prime-field value in (3).
Consequently prime-field enumeration bounds every extension-field
weight choice; if no such row exists the isolated count is zero.
This argument does not descend the original chart.

**Normalization and ordered cases.** The seven missing-label factors
give Q_new(sx)=s^7 Q(x); replacing lambda by s^-7 lambda preserves
each of the three actual base errors at its permuted coordinate.
The moment map has rows j=1,...,8, so every syndrome and recovered
error transforms by diag(s,s^2,...,s^8). This is invertible.
The original gamma_i, normalized weights, rho, mu and E stay unchanged.
In the evaluation formulas the monic quartic scales by s^4, the
six-node derivative by s^5, u by s^-1, and T by s^4 at sx.
Hence both-zero and isolated classifications, restored weights and
finite gates are preserved. A choice s=y^-1 puts the first pair at
{1,96}; exchanging either element of any pair changes no sum or base
weight. The other pair roles remain ordered, as do a,b,c. The loops
include every ordered choice Z,W and every ordered triple outside S.
They use no unproved symmetry of shared labels or of pair roles.

**Shared utilities and complete replay.** The complete 192-line C++
source was inspected, including the shared utilities, not just its
different recovery formulas. Testing x^16=1 among 1,...,96 constructs
exactly H; x<97-x selects one element of each antipodal pair. Strictly
increasing four-index loops list each four-support once in lexicographic
order. Its mask with four set bits intersects the P mask exactly when the support
meets P. The replay computes c_x from the seven complementary labels,
then L057 (5), (6), (11), and the full numerator (12). The five row
kinds exhaust the one-dimensional projected cases and weight gates.
No E test is applied: this intentionally enlarges the counted set.

Field inversion is obtained by exhaustive multiplication modulo 97;
each nonzero residue has one inverse. All inverses actually used have
nonzero arguments: distinct-node derivative products, x f(x), c_x,
eligible mu and 1+mu, or nonzero selected Gaussian pivots. The modular
helper reduces negative residues correctly. The four-column matrix
has entries k^(j+1), j=0,...,3; distinct nonzero k make it invertible.
Its augmented-matrix row swaps, pivot normalization and elimination
produce the inverse with the correct row orientation. Multiplying it
by the first four numerator moments recovers the four weights; all
eight moments are then checked, with no nonzero-weight filter.
Field-arithmetic intermediates stay below 2^31 in absolute value (the
largest unmodded expression is bounded by 96^3+96^2). Masks use only
sixteen bits. Row totals use 64-bit counters, and the fiber counters
are bounded by 21,621,600, within signed 32-bit range.

For each assignment the C++ counter encodes weights as p+97q+97^2r,
which is injective for 0<=p,q,r<97, and records a bit for each mu.
It recreates this map for every assignment. Thus it counts distinct
scalars for fixed labels and weights, neither supports nor mixed
assignments. All 97 bit positions are available. Local maxima and the
global maximum are taken over every map entry, not only displayed
survivors. Packed rows are compared byte-for-byte to the replay;
short reads and a trailing byte both cause failure.

The audit compiled this source with `-Wall -Wextra -pedantic` without
warnings and replayed the entire original packed file. Its fresh
`scripts/triangle-recovery/antipodal-anchor-audit-replay.json` equals
the prior replay in every field. All 21,621,600 rows, 15,367,752
eight-moment checks, 3,568,320 retained zero-weight rows and the
classification totals above were reproduced with zero failures.

The additional checker
`scripts/triangle-recovery/audit_antipodal_certificate.py` uses Python
`itertools` combinations/permutations and tuple-keyed sets in place
of the C++ support loops and packed-weight/bitset aggregation. For all
560 unordered shared triples it verifies equality, including order,
between the mask-filtered support sequence and the independent 715
combinations of the thirteen remaining labels. Ordered pair and shared
triple enumeration is checked for uniqueness and the exact totals 42
and 30,240. It reads every packed row, checks row-kind/gate consistency,
rebuilds every scalar set, and compares all 30,240 assignment maxima
and the entire histogram. The resulting histogram is exactly
11,860,104 one-scalar, 4,800 two-scalar and 96 three-scalar fibers,
with none larger. It verifies the complete 108,108,000-byte length and
the stated SHA256. Its evidence is
`scripts/triangle-recovery/antipodal-anchor-critical-audit.json`.
This independent aggregation complements the full equation replay;
it does not pretend to be another independent row-formula proof.

**Original-chart witness.** The audit separately builds all three
actual base errors from L057 (2), with alpha=(-1,2,-1), gamma=(0,1,2)
and lambda=1. They have full weights and their eight moments obey
s(2)=2s(1)-s(0). Dividing the three displayed omega vectors by their
E values gives actual error weights, in the table's support order,
(4,28,42,82), (54,82,22,85) and (38,6,42,32), respectively.
For T=46,24,40 the checker compares their eight moments directly to
(1-T)s(0)+Ts(1). Every residual is zero. Every E and weight is
nonzero and all three T avoid 0,1,2. Thus these are actual errors
on the original pencil, not just projected or numerator solutions.
Audited L057 supplies same-support failure. This confirms attainment
of three only for the isolated subcount claimed here.

**Twelve assembly and exclusions.** For arbitrary original charts,

\[
 T(mu)-T(nu)=
 \frac{g\rho(1-\rho)(mu-nu)}{E(mu)E(nu)}.
\]

The outside factors are nonzero; eligible scalar counts therefore
bound original finite parameter counts. Removing E=0 cannot increase
them. If thirteen distinct additional recoveries existed, audited
L066 first invokes L010 to obtain full unique errors at all sixteen
parameters. Its six shared-label incidences leave at least seven
additional supports disjoint from P. Its both-zero bound first supplies
an isolated full anchor and then leaves at least four isolated disjoint-P
full anchors. Each is a gated row of the exact relaxed enumeration
above, at the same weights and a different scalar. The bound three
contradicts four. No both-zero lift has been dropped and no relaxed
anchor has been assumed full before the sixteen-total argument.

Audit reproduction, preserving the original certificate and summaries:

```sh
clang++ -std=c++17 -O3 -Wall -Wextra -pedantic scripts/triangle-recovery/antipodal_anchor_sweep.cpp -o /tmp/mca-antipodal-anchor-audit
/tmp/mca-antipodal-anchor-audit replay scripts/triangle-recovery/antipodal-anchor-rows.bin scripts/triangle-recovery/antipodal-anchor-audit-replay.json
python3 scripts/triangle-recovery/audit_antipodal_certificate.py
```

No argument change or new DAG edge was required. Arbitrary singleton
pairs, other patterns, extraction and challenge definitions remain open.

## Mathlib

The full matching restricted count is **not checked** in Mathlib.
Supporting Lagrange interpolation, finite-field arithmetic, Vandermonde
inversion and finite-set counting coverage is also **not checked** here.
No absence claim or Mathlib verification of the certificates is made.
