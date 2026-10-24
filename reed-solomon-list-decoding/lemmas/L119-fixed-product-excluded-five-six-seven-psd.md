# L119 — The unchanged product box passes the excluded-anchor three-shell matrix

## Hypotheses

Use L021's canonical positive rational primal vector a_i, L098's
normalization and exactly L112's original positive box. Set

    N=floor(65537^28/2^128)+1, H=binomial(1024,68), rho=N/H,
    U=binomial(1024,64)/binomial(68,64),
    g_i=binomial(68,i)binomial(956,i),
    c_0=1, c_1=...=c_4=0,
    c_i=(N-1)a_i/((U-1)g_i), 5<=i<=68.

For k=i-5, let q_k and p_k be the unchanged `point[k]` and
`scale_powers[k]` in
`scripts/finite-support/positive-factor-enclosure.json.gz`. Precisely,

    l_i=10^p_k*(q_k-10^25)/10^70,
    u_i=10^p_k*(q_k+10^25)/10^70,
    x_i in [l_i,u_i], 5<=i<=68.

On the universe V of all 68-subsets of a 1024-point set, use the same
normalized moments as L112–L114: singleton 1, pair c_i at half-distance
i=|B\C|, and distinct-triple value y=x_i*x_j*x_h if all three
half-distances are at least five. A distinct triple with a side in
{1,2,3,4} has y=0. A repeated triple with sides (0,b,b), in any order,
has y=c_b; in particular y=1 when all three coincide. Nonempty homogeneous
moments are rho times these values. No pair, product factor or Boolean
value is changed. All 64 original point integers, scales and intervals
are retained, including unused distances.

Fix A in V and let S_l(A)={B in V: |A\B|=l}. On the index set
{A} union S_5(A) union S_6(A) union S_7(A), prescribe

    K_A(B,C)=c_(|B\C|)-y(A,B,C).

No code, full source PSD, representing measure, global uniqueness of
the positive root, packing or RS realization is assumed. Retain L113's
joint root/upper audit, L114's consumed-lower audit, L116–L117's two-shell
audits and L118's completed included-anchor three-shell audit in their
precise scopes. L116 supplies retained input verification; L117 supplies
the smaller excluded restriction; L118 supplies the comparison dictionary
and coherent three-shell geometry, not this matrix's sign verdict.

## Conclusion

For every A and every x in this unchanged box, K_A is PSD. Its entire
A row and column vanish. The restriction to all three complete shells
is positive definite. All 64 complete source blocks pass: 36 have size
three, 13 have size two, and 15 have size one. All 149 elimination pivots
have strictly positive whole-box interval lower endpoints. Dividing each
layer-l pivot by the positive c_l*d_l(a,b) defined below gives these
uniform lower bounds:

    layer five:  >=60833905223164487/10^6,
    layer six:   >=62140756033549750/10^6,
    layer seven: >=62119685418336245/10^6.                 (1)

Each layer's smallest certified lower endpoint occurs at (a,b)=(4,0)
and lies below its displayed bound plus 10^-6. The normalization in
(1) includes division by c_l; L117 instead divided by d_l alone. These
are certificate endpoint bounds, not attained minima of eigenvalues or
pivot functions. Independently, all 306 nonempty principal minors of
the complete reduced blocks have strictly positive interval lower
endpoints.

At L112's enclosed root this retains another necessary matrix for the
same ordinary scalar and exact-N assignment. It parks exclusion by this
fixed slice only. This is a REPRODUCTION of assessed spectral, Schur and
interval tools; no general result beyond the sources checked is claimed.
Full source PSD, stronger distributions, global root uniqueness, measures,
packings, RS realization and arbitrary-center 67/68-agreement safety
remain open. The 955–957 bracket is unchanged. The separate critical proof
audit below retains this application; there is no complete candidate resolution.

## Proof

**Imported results and applicability.** The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-fixed-product-excluded-five-six-seven-psd.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE Trans. Inform. Theory 51
(2005), 2859–2866, DOI
[10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (60), (62)–(65), printed p.7, especially the second matrix in
(64). Cross-check Hyun Kwang Kim and Phan Thanh Toan, *Improved
Semidefinite Programming Bound on Sizes of Codes*,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), 14 December 2012,
III.A Remark 11 and III.B (31)–(35), printed pp.8–9, especially (33).
The code input is a nonempty binary constant-weight code; the even-distance
conditions d>=4 and d<2w<=n hold at (n,w,n-w,d)=(1024,68,956,10).
The excluded coefficient is the presentation's own opposite pair minus
its triple value, preserving t-s and all Boolean cases. Multiplication
by rho>0 does not change PSD. The qualified complement prefactor in
Schrijver (61) is unused. These are necessary constraints; a passing
assignment is not asserted to arise from a code.

Import the complete unequal-layer algebra from Schrijver (7), Proposition
5 (44)–(47), Theorem 1 (51), III.A (52)–(59), printed pp.2,5–7,
using the congruent integer-beta convention of foundations/04,09.
The tensor decomposition and extension/reset argument apply to arbitrary
invariant real coefficients. Principal layer restriction to 0,5,6,7 is
permitted for both ground-set sizes 68 and 956. Singular and new-only
modes remain included. This algebra requires no code or measure.

Import enclosing expression arithmetic from Siegfried M. Rump,
*Verification methods: Rigorous results using floating-point arithmetic*,
Acta Numerica 19 (2010), 287–449, DOI
[10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
§5.5 (5.16)–(5.17), author p.28. Import the positive-leading-block
Schur congruence from Brouwer–Haemers, *Spectra of Graphs*,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), p.36. Foundations/09,14 retain the inspected hypotheses
and essential cases. All arithmetic below has exact rational endpoints;
dependency overestimation is allowed and every inverted pivot is strictly
positive throughout its enclosure. L112 already supplies the root. No
general theorem is reproved: these imports do not evaluate the frozen
coefficients, which is the finite specialization performed here.

**Full affine dictionary and zero anchor.** Write

    B=(A\X) union Y, C=(A\X') union Y',
    |X|=|Y|=l, |X'|=|Y'|=m,
    t=|X intersection X'|, s=|Y intersection Y'|,
    h=l+m-t-s.

For unordered layer pairs 55,56,57,66,67,77, every 0<=t,s<=min(l,m)
occurs: the head and tail unions have size at most 14, within both
ground-set sizes. In bit order A,B,C the eight atoms (masks 0,...,7) are

    (956-l-m+s,t,l-s,m-t,m-s,l-t,s,68-l-m+t).

They are nonnegative, sum to 1024 and determine the stabilizer orbits;
matching atoms extend to point bijections. There are exactly
36+36+36+49+49+64=270 relations. For fixed B their multiplicity is

    D(l,m,t,s)=binomial(l,t)binomial(68-l,m-t)
              *binomial(l,s)binomial(956-l,m-s)>0.

The source entry is

    E_lm(t,s)=c_h-Y_lm(t,s),
    Y_lm(t,s)=c_l          if h=0,
              0           if 1<=h<=4,
              x_l*x_m*x_h if h>=5.                    (2)

The h=0 case is exactly l=m,t=s=l and gives diagonal 1-c_l;
the forbidden cases give zero. Every pair through c_14 is retained.
The complete anchor cases (0,0),(0,l),(l,0), l=5,6,7, have
opposite pair c_(l+m), Boolean y=c_max(l,m), and difference zero.
Their D is g_m for l=0 and 1 otherwise. Each anchor-to-shell row is
constant by the recipe's stabilizer invariance, so these seven cases
exhaust the entire zero row before it is deleted. No positive anchor
or included-anchor Schur subtraction is used.

The independent verifier constructs actual A,B,C for all 270 relations
and reconstructs all six ordered presentations (R,S,T). It computes
i=|R\S|, j=|R\T|, t'=|(R\S) intersection (R\T)|,
s'=|(S\R) intersection (T\R)|, h'=|S\T| and checks

    h'=i+j-t'-s', t'-s'=t-s,
    D'=binomial(i,t')binomial(68-i,j-t')
       *binomial(i,s')binomial(956-i,j-s').

The two multinomials multiply to g_i*D'=g_l*D(l,m,t,s).
Each of the 1620 presentations records its own c_h', triple interval
and affine difference c_h'-y. Only the y values are required to agree
across presentations; the opposite pairs can differ. Full canonical
eight-atom keys check every y collision. Among these presentations the
coincident case and the two endpoint repetitions each occur six times,
with D'=g_j,1,1 respectively. Null sides retain zero capacities.
The recipe is invariant under all point permutations fixing A; no
subgroup-label restrictions or arbitrary feasible assignment are averaged.

**Complete coherent block reduction.** For 0<=a,b<=7 define

    T_ab={l in {5,6,7}: l>=max(a,b)},
    d_l(a,b)=binomial(68-2a,l-a)binomial(956-2b,l-b)>0,
    beta(n,l,m,a,t)=sum_(u=max(a,t))^min(l,m,n-a)
       (-1)^(u-t)binomial(u,t)binomial(n-2a,u-a)
       *binomial(n-a-u,l-u)binomial(n-a-u,m-u).

Out-of-range binomials are zero. The complete symmetric source block is

    B_ab(l,m)=sum_(t,s) beta(68,l,m,a,t)beta(956,l,m,b,s)
                        *E_lm(t,s), l,m in T_ab.       (3)

There is no correction term in any mode. The multiplicity is

    m_ab=(binomial(68,a)-binomial(68,a-1))
          *(binomial(956,b)-binomial(956,b-1))>0.

For each layer l, summing m_ab over a,b<=l gives g_l. Consequently
sum m_ab*|T_ab|=g_5+g_6+g_7, and the zero anchor adds one dimension.
This checks the imported complete decomposition's application: 36 modes
have three layers, 13 have two and 15 have one. No mode with a>7 or
b>7 has a retained layer; every new-only mode with maximum seven remains.

Independently check the signs and normalization by signed subset functions.
On r-subsets of an n-set use a product of a disjoint signed point-pair
membership differences. Its squared norm is
2^a*binomial(n-2a,r-a): nonzero subsets choose exactly one of each pair
and r-a ordinary points. Evaluating the relation action from m-subsets
at an l-subset containing all positive partners and no negative ones gives

    eta(n,l,m,a,t)=sum_(z,q: a-z+q=t)
       (-1)^z binomial(a,z)binomial(l-a,q)
       *binomial(n-l-a,m-a-q),                         (4)

where 0<=z<=a, 0<=q<=l-a. The two ordinary regions have sizes l-a
and n-l-a. This counts full actual subsets, with their signs. The
verifier saves every term for n=68,956, all nine ordered layer pairs
and every surviving a. Exact integer comparisons give

    binomial(n-2a,l-a)*eta(n,l,m,a,t)=beta(n,l,m,a,t),
    binomial(n-2a,l-a)*eta(n,l,m,a,t)
       =binomial(n-2a,m-a)*eta(n,m,l,a,t).             (5)

Thus tensor bilinear forms are 2^(a+b) times (3), with one common positive
factor across the layers. All 242 rectangular comparisons agree, checking
both directions of each of the three rectangles coherently. Completeness
uses the cited source theorem, not these finite tests alone.

Every block of the smaller L117 restriction is recovered exactly. Its
layer-five and final layer-six pivot intervals agree after dividing
L117's d_l-normalized intervals by c_l. As a separate identity check,
the exact pair-only transform minus (3) reproduces L118's whole triple
transform after restoring its constant-mode anchor correction. This
checks the new coefficients against the unchanged dictionary; L118's
PSD verdict is not transported to the excluded matrix. The verifier's
coefficient-polynomial traces independently give g_l*(1-c_l) for every
diagonal layer, with zero coefficients on all product-factor terms.

**Whole-box signs and independent evidence.** Enclose (2) by
[c_h-Y_+,c_h-Y_-], using exact Boolean/null values and positive endpoint
products [l_l*l_m*l_h,u_l*u_m*u_h] on permitted distinct triples.
Form (3) using signed endpoint sums: negative coefficients exchange
endpoints. Products use all endpoint combinations; squares include zero
when their interval contains zero. For each mode eliminate in layer
order 5,6,7, retaining whichever layers occur. At a pivot enclosure
P=[P_-,P_+] with P_->0 use

    P^(-1)=[1/P_+,1/P_-],
    [B_ij] <- [B_ij]-[B_ki]*[B_kj]*P^(-1).           (6)

Use the square operation when i=j, and the same pre-step matrix for
every update. By enclosing expression arithmetic every resulting entry
contains the actual Schur entry at every point of the original box.
Positive pivot intervals therefore certify each whole block by the
imported invertible Schur congruences. No zero pivot is inverted,
midpoint sign used, box refined or prescription retuned. Dividing the
pivot by c_l*d_l>0 yields (1). Since excluded diagonals are 1-c_l,
rather than c_l, this normalization can be much larger than in L118;
it does not assert correspondingly large original eigenvalues.

The independent verifier reconstructs every source entry from actual
sets, every signed action from (4), every block and all elimination
stages without importing constructor routines. Its separate collected
polynomial enclosures lie inside the uncollected signed-sum intervals.
It also expands every nonempty block principal determinant over all
permutations with rational interval operations. All 306 determinant
interval lower endpoints are positive. It consumes the entire certificate;
no sample, preview or numerical solver status supplies this verdict.

Reproduce the bounded test from this notebook:

    python3 scripts/finite-support/fixed_product_excluded_three_shell.py
    python3 scripts/finite-support/verify_fixed_product_excluded_three_shell.py

The full constructor artifact is
`scripts/finite-support/fixed-product-excluded-three-shell.json`:
1175 checks, zero failures, all 270 entry intervals, seven anchor cases,
64 complete blocks and all elimination stages and pivots. The independent
artifact is
`scripts/finite-support/fixed-product-excluded-three-shell-verification.json`:
8224 checks, zero failures, complete actual presentations, signed actions,
all 149 pivots, 306 minors and per-layer minimum endpoint fractions.
The whole-box verdict is `EXCLUDED_THREE_SHELL_PASSES`, with no negative
or unresolved mode. The full minimum and layer-seven minimum fractions
were inspected, and every relevant entry, pivot and minor is checked
by the complete verifier, not inferred from a preview.

Both scripts bind exact N, canonical pairs, rho and every original endpoint.
The full frozen point/scale/Q/radius/box/N/H object equals L112's original.
They retain every input and replay binding of the joint root/upper audit,
consumed-lower audit, both two-shell audits and completed L118 audit;
every inclusion margin is positive and all 64 consumed lower identities
are checked. Hashes retain the reviewed mathematical inputs; their flags
alone do not supply the proofs of those inputs or of this new application.
Original scripts, certificates, proofs and unfinished work are preserved.

The full shell restriction is positive definite, and adjoining its zero
anchor gives PSD. Positive rho preserves the homogeneous verdict. At
the enclosed root L112 supplies the contractions, L113–L114 supply the
ordinary scalar conditions, and this new matrix passes simultaneously.
This is still only one necessary principal restriction. It excludes no
arbitrary center and establishes no full source feasibility, representing
measure, packing or unsafe RS list. The dedicated critical audit follows.

**Separate critical proof audit (2026-10-24, step 449).** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-24-l119-excluded-three-shell-critical-audit.md`.
This review retains the conclusion without mathematical repair. It
supersedes pending-review wording for L119 in the overview and
ATTEMPTS/097. The argument and direct mathematical inputs are unchanged;
no overview assembly or DAG modification is needed. This is local
verification of an application of the cited tools, not a new general
theorem or a claim beyond the assessed sources.

The entire proof, constructor and independent verifier were checked
against the retained primary statements and essential proof cases in
foundations/04,09,12,14. The source code hypotheses justify necessity;
the algebra evaluates any prescribed invariant coefficient family.
Here the recipe itself is invariant under permutations fixing A because
distances and Boolean repetitions are preserved. The complete head/tail
partitions classify its stabilizer orbits: equal partitions extend to
bijections separately within A and its complement. Thus the reduction
holds for every A without averaging labeled RS constraints or assuming
a code or measure. Multiplication by rho>0 preserves the whole matrix's
PSD. The root/upper, consumed-lower and earlier matrix audits retain
their original scopes; contractions are asserted at the enclosed root,
whereas this PSD conclusion holds throughout the box.

The complete independent verifier was replayed to
`scripts/finite-support/l119-critical-reverification.json`, preserving
the originals. All 8224 checks pass, and its entire JSON object equals
the original verification certificate, including all entries, actual-set
presentations, signed actions, blocks, elimination stages, pivots,
minors and exact minima. All input, code and prior replay bindings agree.
This consumes the complete evidence, rather than substituting hashes
or counts for reconstruction. The additional audit recomputes N,H,rho,
all canonical pairs and all 64 original point/scale/endpoint triples;
the entire frozen extraction equals the authoritative compressed input.
The replay retains all original strict root margins and all 64 consumed
lower identities. No root solve or repeated prior proof audit is needed.

For every one of the 270 relations the additional audit reconstructs
the manuscript's eight atoms, then directly permutes these eight counts
in all six orders, independently of the replay's actual-set method.
From the permuted counts q it obtains i=q_1+q_5, j=q_1+q_3,
t'=q_1, s'=q_6 and h'=q_2+q_3. The full count is
68!*956!/product_(mask=0)^7 q_mask!, agreeing with both g_i*D' and
g_l*D. All 1620 presentations retain t'-s'=t-s, their shared union
interval and their own opposite pair c_h'. The affine entries themselves
need not agree. Coincidence and the two endpoint repetitions each occur
six times. Among 408 distinct null presentations, 136 have a forbidden
opposite side and affine value zero; the other 272 have a forbidden
anchored side and retain their own opposite pair. Permitted entries
keep every third distance through 14. The seven anchor cases exhaust
the whole zero row before deletion, including the all-equal value
c_0-1=0; that zero is never inverted.

All 118 signed-action records are checked term by term, including zero
terms, for both ground sets and all nine ordered layer pairs. Choosing
exactly one point of each designated pair and then ordinary points gives
(4); the norm count is 2^a*binomial(n-2a,l-a). Consequently the common
factor 2^a is independent of l, and the tensor bilinear form uses the
same positive factor 2^(a+b) on all layers. All 242 rectangular
comparisons agree, covering both orientations of all three rectangles.
The complete source theorem supplies the mode spaces and their coherent
matching; these finite checks establish normalization, not completeness
by themselves. Every d_l and multiplicity is positive, and the exact
dimension identity is

    1+sum_(a,b) m_ab*|T_ab| = 1+g_5+g_6+g_7.

The 36 three-layer, 13 two-layer and 15 one-layer modes are exhaustive.
Every block is checked as pair transform minus union transform with no
anchor subtraction. Restoring L118's own constant-mode correction
recovers its triple transform only; no included-anchor PSD sign is used.
Every smaller L117 block agrees exactly. For each old pivot P,

    (P/d_l)/c_l = P/(c_l*d_l),  c_l>0,

is checked at both interval endpoints, for all 85 old pivots across
the 49 smaller modes. Thus (1)'s large numbers do not silently replace
L117's different normalization or claim large original eigenvalues.

For every elimination stage let P=[P_-,P_+] be the shell pivot,
V a remaining cross interval and A a remaining diagonal interval.
Put q_+=max(V_-^2,V_+^2), and q_-=0 if V contains zero, otherwise
q_-=min(V_-^2,V_+^2). The full diagonal update is

    [A_- - q_+/P_-, A_+ - q_-/P_+].

Off-diagonal updates use all endpoint products and the reciprocal
[1/P_+,1/P_-]. Every pre-update matrix and all resulting intervals
agree with the saved stages. Each inversion checks 0<P_-<=P_+.
In addition, for each remaining layer i, with b_i the bound in (1),
the audit verifies the denominator-cleared comparison

    A_-*P_- - q_+ >= b_i*c_i*d_i*P_- > 0.

All 121 such comparisons pass, including both stages in the three-layer
blocks. For actual shell entries P>0, row v and remaining block C,
the determinant-one congruence with first row (1,-v^T/P) sends
[[P,v^T],[v,C]] to diag(P,C-v*v^T/P). Adjoining an unchanged zero
anchor gives diag(0,P,C-v*v^T/P). The audit checks this imported
identity at all 2438 independent entry-endpoint choices across the
64 blocks. These are identity checks; whole-box positivity follows
from interval inclusion and positive pivot bounds, not corner signs.

All 149 normalized pivots satisfy (1). Each layer has its unique
minimum certified lower endpoint at (4,0), strictly below its displayed
bound plus 10^-6. The complete three fractions in
`per_layer_minimum_pivot` were inspected in full. These are minima of
certificate endpoints, not actual pivot-function or spectral minima.

As a second determinant check, each two-by-two principal minor is
enclosed as A*B-D^2, and each three-by-three determinant as

    det [[A,D,E],[D,B,F],[E,F,C]]
       = A*B*C+2*D*E*F-A*F^2-B*E^2-C*D^2.

Zero-aware interval squares and full endpoint products give positive
lower endpoints for all 306 nonempty principal minors. Each closed-form
enclosure lies inside its saved permutation-expansion enclosure;
the complete list, ordering and positive normalization factors agree.
The replay also retains the exact coefficient-polynomial trace
g_l*(1-c_l), including cancellation of every product term. Dependence
overestimation in intervals is allowed throughout.

Reproduce this bounded audit without changing any original certificate:

    python3 scripts/finite-support/critical_audit_l119.py

The complete additional evidence is
`scripts/finite-support/l119-critical-audit.json`: 11727 checks,
zero failures, all original endpoints, full pivot/denominator comparisons,
all closed-form minor enclosures and original/replay bindings. The
entire replay equals the original; every consumed original is unchanged.
No mathematical or execution failure occurred in this audit. Earlier
inspector failures and unfinished work remain preserved in their records.
No solve, scan, retuning, refinement, new assignment or enlarged matrix
was used. The verified result remains only this excluded-anchor slice;
full source PSD, stronger distributions, global root uniqueness, measures,
packings, RS realization and the 955–957 boundary remain unresolved.

## Mathlib

Full matching mixed-layer Terwilliger theorem, excluded-anchor source
constraint and this finite application: not checked. Supporting finite-set,
signed subset-action, Schur and rational-interval PSD coverage: not checked.
Unknown coverage is not evidence of absence; no uninspected Mathlib result
is imported.
