# L117 — The unchanged product box passes the excluded-anchor five/six matrix

## Hypotheses

Use L021's canonical positive rational primal vector a_i, L098's exact
cardinality normalization, and precisely L112's original box. Set

    N=floor(65537^28/2^128)+1, H=binomial(1024,68), rho=N/H,
    U=binomial(1024,64)/binomial(68,64),
    g_i=binomial(68,i)binomial(956,i),
    c_0=1, c_1=...=c_4=0,
    c_i=(N-1)a_i/((U-1)g_i), 5<=i<=68.

For k=i-5 let q_k and p_k be the unchanged `point[k]` and
`scale_powers[k]` in
`scripts/finite-support/positive-factor-enclosure.json.gz`. Define

    l_i=10^p_k*(q_k-10^25)/10^70,
    u_i=10^p_k*(q_k+10^25)/10^70,
    x_i in [l_i,u_i], 5<=i<=68.

All 64 intervals are retained, with their positive original rational
endpoints. On the universe V of 68-subsets of a 1024-point set, use
the same normalized moments as L112–L114: singleton 1, pair c_i at
half-distance i, and distinct-triple value y=x_i*x_j*x_h if all sides
are at least five. A distinct triple with a side 1,...,4 has y=0;
a repeated triple with sides (0,b,b) has y=c_b, including y=1 when
all three coincide. Nonempty homogeneous moments are rho times these
normalized values. No pair, product factor or Boolean value is varied.

Fix A in V. Retain the index A and every B with |A\B| in {5,6}.
The prescribed source excluded-anchor matrix is

    K_A(B,C)=c_(|B\C|)-y(A,B,C).

No code, representing measure, full source PSD or global uniqueness
of a positive product root is assumed. The joint root/capacity audit,
the Boolean-lower-row audit, and the completed included-anchor audits
are retained in their precise scopes.

## Conclusion

For every A and every x throughout this unchanged box, K_A is PSD.
Its entire A row is zero. Its restriction to both complete shells is
positive definite: all 49 complete source blocks pass, with 36 shared
two-by-two blocks and 13 six-only scalars. All 85 normalized positive
elimination pivots have certified lower endpoints at least

    638512/10^6 > 0.

The minimum lower endpoint among all pivots occurs in the layer-five
pivot of mode (4,0), and the minimum among final layer-six pivots also
occurs at (4,0); both lie in [638512,638513)/10^6. These are bounds
on the interval certificate, not attained minima of actual eigenvalues
or pivot functions over the box.

Consequently L112's enclosed root retains this additional necessary
matrix, together with L113–L114's ordinary scalar and exact-N feasibility
and L116's included-anchor five/six pass. This is a local REPRODUCTION
of assessed tools, not a claim beyond the sources checked. It parks
exclusion by this immutable excluded-anchor slice only. Full source PSD,
other layers, stronger distributions, global root uniqueness, measures,
packings, RS realization and arbitrary-center 67/68-agreement safety
remain open. The 955–957 bracket is unchanged. The separate critical
proof audit below retains this application.

## Proof

**Imported results and applicability.** The prior SPECIALIZE assessment
is `drafts/literature/2026-10-24-fixed-product-excluded-five-six-psd.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE Trans. Inform. Theory 51
(2005), 2859–2866, DOI
[10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (60)–(65), printed p.7, specifically the second matrix in (64).
Cross-check Hyun Kwang Kim and Phan Thanh Toan, *Improved Semidefinite
Programming Bound on Sizes of Codes*,
[arXiv:1212.3467v1](https://arxiv.org/pdf/1212.3467v1), 14 December
2012, III.A Remark 11 and III.B (31)–(35), printed pp.8–9, specifically
(33). These are necessary constraints for nonempty binary constant-weight
codes. Their even-distance conditions d>=4 and d<2w<=n hold for
(n,w,v,d)=(1024,68,956,10). The coefficient is the opposite pair minus
the triple, with its original t-s and repeated cases. The homogeneous
matrix is rho*K_A, so the positive scalar rho does not change PSD.
Schrijver (61)'s qualified complement prefactor is unused; no assertion
about that prefactor or an actual code is needed for this evaluation.

Import the complete unequal-layer algebra from Schrijver (7),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), printed
pp.2,5–7, in the congruent integer-beta convention of foundations/04,09.
The tensor decomposition and extension/reset argument allow arbitrary
invariant coefficients, including this affine difference. For ground-set
sizes 68 and 956, principal restriction selects layers 0,5,6 in the
source layer ranges; equivalently pad the other coordinates with zero
and remove their zero coordinates after decomposition. Thus every
surviving source mode is required. No measure or averaging of arbitrary
labeled RS restrictions is assumed. The actual product prescription
itself is invariant under point permutations fixing A.

Import enclosing expression arithmetic from Siegfried M. Rump,
*Verification methods: Rigorous results using floating-point arithmetic*,
Acta Numerica 19 (2010), 287–449, DOI
[10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
§5.5 (5.16)–(5.17), author p.28; foundations/14 records the inspected
scope. Exact rational endpoints avoid rounding error; repeated variables
may enlarge the enclosures. For positive-pivot Schur congruence import
Brouwer–Haemers, *Spectra of Graphs*,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), p.36, as recorded in foundations/09. Every inverted
pivot below has a strictly positive lower bound. No new root criterion,
spectral theorem, Schur theorem or interval theorem is reproved. The
finite specialization is needed because those results do not give
the sign verdict for this fixed assignment. L063 is a different-witness
method precedent only; none of its moments or signs is imported.

**Complete entries, presentations and zero anchor.** Write

    B=(A\X) union Y, C=(A\X') union Y',
    |X|=|Y|=l, |X'|=|Y'|=m,
    t=|X intersection X'|, s=|Y intersection Y'|,
    h=l+m-t-s.

For (l,m)=(5,5),(5,6),(6,6), all 0<=t,s<=min(l,m) occur. With
A,B,C in bits 0,1,2, the full atoms in mask order 0,...,7 are

    (956-l-m+s,t,l-s,m-t,m-s,l-t,s,68-l-m+t).

All sizes are nonnegative, and atom bijections give exactly the
stabilizer orbits. Their complete count is 36+36+49=121; swapping
B,C supplies the other rectangle. The multiplicity with B fixed is

    D(l,m,t,s)=binomial(l,t)binomial(68-l,m-t)
               *binomial(l,s)binomial(956-l,m-s)>0.

The normalized union entry y_lm(t,s) is c_l if h=0, zero if
1<=h<=4, and x_l*x_m*x_h if h>=5. The excluded entry is

    E_lm(t,s)=c_h-y_lm(t,s).                            (1)

All pairs through c_12 are retained. In particular h=0 occurs only
on the Boolean diagonal l=m,t=s=l, where E=1-c_l. If h is forbidden,
both terms vanish. When a different side is forbidden after reanchoring,
y=0 alone does not imply c_h=0; every presentation uses its own c_h.

The independent verifier constructs actual sets for all 121 relations
and all 726 orders. For each order (R,S,T), it reconstructs
i=|R\S|,j=|R\T|,t'=|(R\S) intersection (R\T)| and
s'=|(S\R) intersection (T\R)|, retaining

    h'=i+j-t'-s', t'-s'=t-s,
    D'=binomial(i,t')binomial(68-i,j-t')
        *binomial(i,s')binomial(956-i,j-s').

The two source multinomials equal g_i*D'=g_l*D(l,m,t,s).
All six orders give the same underlying y, and complete eight-atom
keys check all collisions. Their affine entries need not agree when
the opposite pair changes. The certificate saves each ordered pair,
y interval and affine interval. Endpoint repetitions with j=0 and
with h'=0 have D'=1. The i=0 coincident row has D'=g_j; each of
these three types occurs four times in the 726 orders. Null cases
and their zero capacities are checked explicitly.

If B=A, then h=m and y=c_m, giving K_A(A,C)=0; similarly if C=A.
The all-equal entry is c_0-1=0. The five layer cases
(0,0),(0,5),(5,0),(0,6),(6,0) exhaust the entire anchor row and
column, including both orientations and their actual D. The constructor
and verifier check these identities before removing the zero coordinate.
There is no positive-anchor elimination and no c_l*c_m*J subtraction
in the tested matrix.

**Complete source blocks and coherent rectangular signs.** Put

    beta(n,l,m,a,t)=sum_(u=max(a,t))^min(l,m,n-a)
       (-1)^(u-t)binomial(u,t)binomial(n-2a,u-a)
       *binomial(n-a-u,l-u)binomial(n-a-u,m-u).

Ordinary out-of-range binomials are zero. For each 0<=a,b<=6,
retain T_ab={5,6} if a,b<=5 and T_ab={6} otherwise. Set

    D_l=binomial(68-2a,l-a)binomial(956-2b,l-b)>0,
    B_lm=sum_(t,s) beta(68,l,m,a,t)beta(956,l,m,b,s)E_lm(t,s).

These are the entire shell blocks, with no anchor correction. Their
multiplicities are

    (binomial(68,a)-binomial(68,a-1))
    *(binomial(956,b)-binomial(956,b-1))>0.

Summing over a,b<=5 recovers g_5; summing over a,b<=6 recovers g_6.
The imported full decomposition justifies exhaustion, while these
dimension equalities check its application. The only layer-zero
coordinate was the verified zero coordinate in mode (0,0).

For an independent normalization check, use L116's retained signed
subset method, rather than its PSD signs. For a factor of size n,
the product of a disjoint positive-minus-negative membership differences
on l-subsets has squared norm 2^a*binomial(n-2a,l-a). Its relation
action at an l-set containing all positive members is obtained by summing

    (-1)^z binomial(a,z)binomial(l-a,q)binomial(n-l-a,m-a-q)
    over z,q with t=a-z+q.                             (2)

Denote this signed sum by eta(n,l,m,a,t). All terms, including zero
terms, are saved and checked for both factor sizes, both diagonal
layers and both rectangles. Exact comparisons give

    binomial(n-2a,l-a)*eta(n,l,m,a,t)=beta(n,l,m,a,t),
    binomial(n-2a,l-a)*eta(n,l,m,a,t)
       =binomial(n-2a,m-a)*eta(n,m,l,a,t).

Thus the tensor bilinear blocks are B_lm times the same positive
factor 2^(a+b), retaining both signs in one coherent congruence.
This is a finite check of the imported algebra's normalization,
not a replacement proof of complete-space exhaustion.

**Whole-box interval verdict.** Enclose y in the point interval
[c_l,c_l] on a Boolean diagonal, [0,0] for a forbidden h, and
[l_l*l_m*l_h,u_l*u_m*u_h] otherwise. Subtract its reversed endpoints
from the exact c_h to obtain the interval for (1). Take every signed
beta sum using exact rational endpoints, reversing endpoints for
negative coefficients. Let [A],[B],[C] enclose B_55,B_56,B_66 in
a shared mode. Every A_->0. Squaring [B] uses zero as its lower
endpoint if it crosses zero, and inversion uses
[1/A_+,1/A_-]. Therefore the normalized pivot intervals

    [A]/D_5,
    ([C]-[B]^2*[1/A_+,1/A_-])/D_6                      (3)

enclose the true elimination pivots throughout the original box.
For a six-only mode the interval is [C]/D_6. All 85 lower endpoints
are at least 638512/10^6; all 49 final intervals are strictly positive.
The complete exact least fractions are saved under
`minimum_normalized_pivot.value` and
`minimum_normalized_remainder.value` in the independent certificate.
Both full values and the empty failure list were inspected; exact
integer comparisons give the brackets in the conclusion. No midpoint
sign or sampled box point establishes these inequalities.

By the imported positive-pivot congruence, each shared block is positive
definite, and the six-only blocks are positive. The complete source
decomposition proves positivity on the entire two-shell space. Restoring
the zero anchor gives PSD. At L112's enclosed root these same moments
simultaneously satisfy the retained scalar and exact-N constraints;
those contractions need not hold at other box points.

**Complete evidence and scope.** Reproduce from this notebook:

    python3 scripts/finite-support/fixed_product_excluded.py
    python3 scripts/finite-support/verify_fixed_product_excluded.py

The constructor saves `scripts/finite-support/fixed-product-excluded.json`:
569 checks, zero failures. It binds canonical input files and the
retained root/scalar/included-anchor audits with every input/code/replay
hash, checks all 64 strict inclusion margins and consumed lower rows,
and saves every endpoint, affine entry, zero-anchor case, pair block,
y block, affine block, scaling, pivot interval and verdict. It reuses
the audited root and does not solve the contraction system again.

The independent verifier imports no constructor routine. It saves
`scripts/finite-support/fixed-product-excluded-verification.json`:
3651 checks, zero failures. It reconstructs all actual sets and source
presentations, all 50 signed-action records, both rectangular directions,
all 49 complete blocks and every interval operation. It independently
uses factorial binomials and collects the coefficients of each common
x_l*x_m*x_h expression before enclosing it; these enclosures lie within
the saved entrywise intervals without altering the box. Its diagonal
polynomial traces cancel every distinct-product coefficient and recover
exactly g_l*(1-c_l), not an overestimated interval trace.

For every block it also checks B=P-Y, where P is the independently
reconstructed exact pair block and Y is the L116 union block with only
L116's own prior anchor subtraction undone. This verifies the unchanged
dictionary; no included-anchor correction is applied to B. L115's
audit is retained through the included-anchor input chain, not used
as a sign premise for this excluded-anchor test. All load-bearing
arrays are consumed in full by the independent reconstruction; previews
and success flags alone do not verify them.

No solve, scan, retuning, refinement, old-witness substitution or
omitted-layer test was performed. The pass is one additional necessary
slice, without a full source extension, representing measure, actual
packing or RS realization. ATTEMPTS/045 and /094 remain in their exact
different-witness/different-matrix scopes. The separately approved critical manuscript/evidence audit is
completed below.

**Separate critical proof audit (2026-10-24, step 441).** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-24-l117-excluded-critical-audit.md`.
This review retains the stated conclusion without mathematical repair.
It supersedes historical pending-review wording in the overview and
ATTEMPTS/095. The argument and direct mathematical inputs are unchanged,
so neither the overview assembly nor DAG needs modification. This is a
verified finite application of the cited tools, not a new general theorem
or a claim beyond the assessed sources.

The complete proof, constructor and independent verifier were inspected
against the imported excluded-anchor coefficient rule, unequal-layer
algebra, positive-pivot congruence and enclosing interval arithmetic.
The code hypotheses are needed for necessity of the source constraint,
not for evaluating this explicitly prescribed invariant matrix. Its
invariance follows directly from the fixed distance-product recipe.
Thus no averaging of arbitrary labeled RS restrictions or assumption
of a representing measure supplies the reduction. The unchanged positive
homogeneous factor rho multiplies the whole matrix and changes no sign.
The reviewed root/scalar and included-anchor results are consumed in
exactly their retained scopes; no included-anchor PSD sign is needed to
prove the excluded-anchor verdict.

The eight-atom formula preceding (1) has nonnegative entries throughout
the stated ranges and yields every stabilizer relation by bijections
within A and its complement. The audit reconstructs its 121 rows, then
permutes the complete eight counts in every order. From each permuted
array q, the coordinates are i=q_1+q_5, j=q_1+q_3, t'=q_1,
s'=q_6 and h'=q_2+q_3. All 726 source presentations agree with the
saved coordinates, positive D, t'-s'=t-s and full multinomial counts.
For every presentation the audit checks the common y interval but its
own c_h' and affine interval. The two endpoint-repetition types and
coincidence each occur four times, with the stated D and Boolean values.
The 228 distinct null presentations split into 76 with forbidden opposite
pair and 152 with a forbidden anchored side. In the former the affine
entry is zero; in the latter y is zero but the affine entry retains its
own opposite pair. No equality of these six affine entries is presumed.
The full zero-anchor cases are checked before removing the coordinate;
the all-equal case is c_0-1=0, not an inverse-pivot case.

Every one of the 50 signed-action records is consumed, including all
zero summands. A nonzero signed function selects one point from each
designated pair. After selecting the z negative members and q ordinary
points of the evaluation l-set, the remaining points come from the
n-l-a points outside that set and all designated pairs. This gives (2).
The norm count has 2^a choices of pair members and
binomial(n-2a,l-a) ordinary choices, so its factor 2^a is common to both
layers. All 72 signed rectangular comparisons and every beta comparison
agree. Tensoring preserves the common positive factor 2^(a+b);
there is no independent sign choice on the opposite rectangle.
The complete source theorem supplies exhaustion, and the audit checks
all multiplicities and the exact dimension identity

    1 + sum_(a,b) multiplicity(a,b)*|T_ab| = 1+g_5+g_6.

This includes the zero anchor, 36 shared blocks and 13 six-only blocks.
The imported complete decomposition, rather than dimension counting or
one representative vector alone, justifies whole-space positivity.

The full verifier replay independently reconstructs all canonical c_i,
exact N and rho, all 64 unchanged endpoints/scales, all retained root
margins and consumed lower-row identities, every source entry, both
signed rectangular actions and all complete blocks. Its entrywise signed
sums and independently collected product expressions enclose the same
polynomial; interval dependency is never assumed absent. For every
block the audit additionally retains exactly B=P-Y with no subtracted
anchor term. The earlier included-anchor certificate is used only to
cross-check Y after undoing its own correction. The diagonal polynomial
trace identities in the complete replay cancel every product coefficient
and give g_l*(1-c_l), retaining the Boolean diagonal.

For a shared block let [A_-,A_+], [B_-,B_+], [C_-,C_+] be its saved
entry enclosures. Set q_+=max(B_-^2,B_+^2), and set q_-=0 when the
cross interval contains zero, otherwise q_-=min(B_-^2,B_+^2).
The audit verifies A_->0 and the exact final-pivot interval

    [(C_- - q_+/A_-)/D_6, (C_+ - q_-/A_+)/D_6].

Every saved interval agrees, including possible zero-crossing squares.
In addition to every old-pivot comparison A_-/D_5>=638512/10^6,
the division-free comparisons are checked in all 36 shared modes:

    C_-*A_- - q_+ >= (638512/10^6)*D_6*A_- > 0.

The 13 six-only modes satisfy C_-/D_6>=638512/10^6 directly. With
actual entries A>0, B, C, the determinant-one matrix

    T = [[1,0,0],[0,1,-B/A],[0,0,1]]

sends [[0,0,0],[0,A,B],[0,B,C]] by T^T K T to
 diag(0,A,C-B^2/A). This is precisely the imported positive-pivot
congruence on the shell, with the zero anchor retained and never
inverted. The audit also checks this algebraic identity at all eight
endpoint triples in every shared mode. Those checks verify the stated
identity; whole-box positivity follows from the enclosing inequalities,
not from corner sampling.

The complete list of 85 pivot intervals equals the saved independent
list. Its unique minimum lower endpoint is the layer-five pivot at
(4,0); the 49 final lower endpoints have their unique minimum at (4,0)
also. Both complete rational fractions, inspected without truncation,
satisfy [638512,638513)/10^6 by exact comparisons. These are minima
of certificate endpoints, not attained minima of eigenvalues or of
pivot functions. No zero shell pivot, singular-range assumption,
midpoint sign or global positive-root uniqueness is used.

Reproduce the bounded audit while preserving the original certificates:

    python3 scripts/finite-support/critical_audit_l117.py

The fresh replay is
`scripts/finite-support/l117-critical-reverification.json`.
Its entire JSON object equals the original independent certificate;
all 3651 checks pass. The additional manuscript/evidence certificate is
`scripts/finite-support/l117-critical-audit.json`: 3007 checks, zero
failures, complete pivot intervals, every cross-multiplied threshold
comparison, both exact minima, the dimension and input/code/replay
bindings. Every consumed original remains unchanged. The L115 single
replay-hash schema and the other audits' replay maps are both bound
explicitly. Complete reconstruction and object equality consume every
load-bearing array; hashes, counts and previews are not substitutes for
this verification. The empty failure lists were inspected in full.

The result is box-wide PSD, while simultaneous exact-N feasibility is
asserted only at L112's enclosed root. The joint L112/L113, L114,
L115 and L116 audits are reused without rerunning their already completed
mathematical tasks. No solve, scan, retuning, refinement, substitute
assignment or new-layer test occurred. ATTEMPTS/045,094,095 retain
their precise different-witness or different-matrix stop evidence.
Full source PSD, other layers, stronger distributions, global uniqueness,
measures, packing, RS realization and the 955–957 boundary remain open.

## Mathlib

Full matching constant-weight excluded-anchor theorem, mixed-layer
decomposition and this fixed-product-box result: not checked. Supporting
rational interval, Schur and rectangular-action coverage: not checked.
Unknown coverage is not evidence of absence; no uninspected Mathlib
theorem is assumed.
