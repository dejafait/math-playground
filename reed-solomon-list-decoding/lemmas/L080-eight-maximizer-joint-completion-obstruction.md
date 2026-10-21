# L080 — L079's exact interpolated maximizer has no nonnegative joint completion

## Hypotheses

Use n=1024,w=68 and precisely L021's entire pair prescription, L053's
positive singleton rho, L073's included-anchor PSD base and L075's whole
unordered dictionary. Divide all moments by rho. Fix a 68-subset D;
retain its anchor and every pair index {D,E} at half-distance 5,6,7.
Keep the original seven-column RREF at (0,v_dagger,w_star), all 28 forced
and 36 completed seven/seven entries. No old coefficient is retuned.

Add every index {D,G} at half-distance eight from D. Use exactly L079's
rational interpolated maximizer t_star in L076's original four-parameter
family, with original nonpivots (56,63,69,78). More precisely, write the
85 free column factors as f(t)=c_col+A_col*t. Put

    I0=(27,33,56,63), J0=(5,26,33,56),
    t0=-(A_col[I0,:])^(-1)c_col[I0],
    t1=-(A_col[J0,:])^(-1)c_col[J0],
    alpha=(s_star-t0_78)/(t1_78-t0_78),
    t_star=(1-alpha)*t0+alpha*t1.

Here s_star is exactly L079's stationary parameter, not a decimal
approximation: if M is its specified symmetric pairing coefficient
matrix, with coordinates (1,t56,t63,t69,t78), then
s_star=-M04/M44. L079 establishes 0<alpha<1 and admissibility.
Every new column is transported by point bijections with these same
coefficients. Keep the anchor/diagonal

    p8=16792471/1181138102168120460>0.

Require all represented full unordered atom keys, Boolean repetitions,
forbidden distinct half-distances 1,...,4, and all 36 forced eight/eight
values. Only the 45 unrepresented eight/eight moments are free, and they
must be nonnegative. Impose no scalar upper row, excluded/other-anchor
matrix, actual-label constraint, or global moment extension.

## Conclusion

The complete simultaneous included-anchor matrix has no PSD completion
under these hypotheses. An exact separator on all 81 product modes has
38 positive weights, cancels 44 free coefficients and leaves one positive
coefficient on (r,q)=(6,3), namely Y_88(2,5). Its full fixed pairing v
satisfies

    -25046444520/10^6 <= v < -25046444519/10^6 < 0.

Nonnegativity of that moment is essential to this certificate; signed
completions are not excluded. This is a local REPRODUCTION/specialization
of known methods, with no source-level novelty claim. It stops this fixed
maximizer only. L078's different immutable-column obstruction and L079's
positive maximum for the old weights both remain valid. The entire family,
other pairs/base moments, global feasibility, RS realization and arbitrary-
center 67/68-agreement safety remain open; the 955–957 bracket is unchanged.
The separate critical proof review below retains this fixed-point rejection.

## Proof

**Imported results and applicability.** The pre-invocation SPECIALIZE
assessment is
`drafts/literature/2026-10-17-eight-maximizer-joint-completion.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
[DOI 10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. Factors 68,956 and layers 0,5,6,7,8 meet its index
ranges. All 81 modes 0<=a,b<=8 occur; the anchor occurs only at (0,0).
L078's reviewed coherent positive congruence depends only on these layers,
factor sizes and subset actions, so applies unchanged to the present
coefficients. Keep foundations/04,09's beta convention and qualifications;
no complement prefactor or representing measure is used.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2 and Theorem 2.6. For a finite real symmetric
extension of a PSD base, the cross block must lie in the base range and
the generalized Schur remainder must be PSD. Singular and empty old
blocks are retained. L073 supplies the old PSD matrix; L079 supplies
family-wide range identities, checked again here at t_star.

For equal-union moments and constraint-preserving averaging import Sven
C. Polak, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Section 1.1 (1)–(3), Proposition 1.1 and indicator proof,
p.2, Section 1.2, p.3. Here n=1024,d=10,w=68; foundations/12 retains
the constant-weight display qualification. The finite LP certificate
method is covered by Michel X. Goemans, *Advanced Algorithms*, Lecture 3,
19 September 2001, Theorems 1 and 3, pp.1–2,
[MIT notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf).
The direct verified inequality chain below suffices; no general SDP
alternative or new optimization theorem is proved. None of these sources
supplies the prescribed-data verdict, so this finite specialization is
necessary. The covered sources and recorded failures are reused without
new literature searches.

**Full entries and positive scaling.** Write C(n,k)=binomial(n,k), zero
outside 0<=k<=n, and S_l=C(68,l)C(956,l). For l<=m in {5,6,7,8},
write E=(D\X) union Y, G=(D\U) union V, with head/tail sizes l,m,
i=|X intersection U| and j=|Y intersection V|. The full atom vector
with membership bits 4,2,1 for D,E,G is

    (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

Its least six-permutation tuple is the unordered key. Actual sets
allocated to these eight disjoint regions independently reconstruct all
500 types and 3000 ordered presentations. The old 270 entries retain
L075's values. Each free new-column entry is p8*f_j(t_star); fixed
lookups and the anchor keep their values. All 85 factor signs and all
90 original compatibility equations pass exactly. Every presentation
lookup and shared key agrees. No new equality is inferred from distances
alone. This is the same fixed point as L079, with exactly factors 33,56
zero and the other 83 positive.

For eight/eight put r=8-i,q=8-j. The 36 forced values are

    Y_88(8,8)=p8,
    Y_88(8-r,8-q)=0                       if 1<=r+q<=4,
    Y_88(8-r,8-q)=Y_(r+q,8)(q,r)          if 5<=r+q<=7.

The last formula reanchors at E. All are nonnegative and checked against
the full-key reconstruction. The remaining 45 keys are distinct. In
lexicographic (r,q) order with r+q>=8, define

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q)>0,
    Y_88(8-r,8-q)=p8*z_rq/V_rq, z_rq>=0.

The finite group permuting D and its complement separately preserves
the whole fixed prescription, union keys, signs, zeros and PSD. Averaging
any completion over it therefore gives an invariant completion. No
actual-label restriction is present or transported. It suffices to
exclude these invariant coefficients.

**Every original mode.** Define

    beta(n,l,m,a,k)=sum_(u=max(a,k))^min(l,m,n-a)
      (-1)^(u-k)C(u,k)C(n-2a,u-a)C(n-a-u,l-u)C(n-a-u,m-u),
    D8_ab=C(68-2a,8-a)C(956-2b,8-b)>0.

After eliminating the positive anchor, the source shell block entries are

    T_lm=sum_(i,j=0)^min(l,m) beta(68,l,m,a,i)beta(956,l,m,b,j)Y_lm(i,j)
          -1_(a=b=0)*p_l*p_m*S_l*S_m.

For (a,b) let B_ab be this old block on layers l in {5,6,7} with
l>=max(a,b), and t_ab its cross vector T_l8. Check all 306 nonempty
old principal minors are nonnegative. Solve B_ab*x=t_ab using a largest
nonsingular principal subsystem and set coordinates outside it to zero;
check every original residual. This includes zero blocks and all 17
new-only modes. Independently, sequential singular elimination checks
every zero-pivot cross residual and gives the same cost t_ab^T*x.
Thus all 81 ranges hold; no inverse of a singular block is assumed.

Let F_ab be the contribution of the 36 forced Y_88 entries to T_88,
divided by p8*D8_ab, before the anchor subtraction. Set

    b_(9a+b)=F_ab-1_(a=b=0)*p8*S8-t_ab^T*x/(p8*D8_ab),
    A_(9a+b,(r,q))=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D8_ab*V_rq).

These are the original 81 necessary inequalities Az<=b. The remainder
b_i-(Az)_i equals the entire new-mode Schur remainder divided by
positive p8*D8_ab. In particular the positive p8^2*S8^2 term is retained
before division. Both programs rebuild every row directly with beta;
the constructor also compares every bound with the saved affine/quadratic
family formula evaluated at the exact interpolation. Positive mode
multiplicities and L078's coefficient-independent coherent congruence
justify using these complete source blocks. An isolated-column energy
pass or positive pairing for different weights is not used as feasibility.

**Compact rational separator.** Index modes by 9a+b, variables from 0
in the specified lexicographic order. Let

    I=(0,1,2,5,6,9,10,11,12,13,14,15,18,19,20,21,22,23,24,25,
       27,28,29,30,31,32,33,36,37,38,39,40,45,46,47,48,
       54,55,56,57,63,64,72),
    J=(-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
       19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,
       38,39,40,41,42,43,44).

Define the 43-by-43 matrix K_ij=-1 for j=-1 and A_ij otherwise,
with rows I and columns J in these orders. Solve

    K^T*y_I=c, c_j=-1 if j=-1 and 0 otherwise,

and put y_i=0 outside I. Exact Gaussian elimination is nonsingular;
this uniquely specifies the entire rational certificate. The independent
verifier uses Gauss–Jordan elimination instead of the constructor's
forward elimination/back substitution. No optimizer is used by the
verifier. All weights are nonnegative, their sum is one, and precisely
38 are positive. For s_j=sum_i y_i*A_ij, precisely 44 vanish and the
sole remaining coefficient, at (r,q)=(6,3), is strictly positive.

Direct reconstruction in original raw Y coordinates gives, for each
free (r,q),

    -sum_(a,b) y_(9a+b)*beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)
                       /(p8*D8_ab)
      =s_rq*V_rq/p8>=0.

Thus the cancellation and remaining sign hold in original moments,
not merely in rescaled variables. The verifier separately sums the
weighted forced, anchor and range-cost contributions; their signed sum
is exactly v=y^T*b and obeys the strict rational interval in the conclusion.
All comparisons use integer cross multiplication, with full rational
values retained in the certificates. A feasible z would satisfy

    0<=sum_j s_j*z_j=y^T*A*z<=y^T*b=v<0,

which is impossible. Averaging rules out a noninvariant completion as
well, and multiplication by rho>0 preserves the result. Since s_(6,3)>0,
this argument needs Y_88(2,5)>=0 and does not rule out signed completions.

**Reproduction and limitations.** From the active notebook run

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/eight_maximizer_joint_completion.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_eight_maximizer_joint_completion.py

Full evidence is saved at
`scripts/finite-support/eight-maximizer-joint-completion-results.json`
and `scripts/finite-support/eight-maximizer-joint-completion-verification.json`.
The constructor passes 383 exact checks and the independent standard-
library-only verifier passes 5599, both with empty failure lists. The
complete input hashes, exact point, 500 types/3000 presentations, every
source block/range/inverse, 306 old minors, 81 inequalities, 81 weights,
45 scaled and raw sums and full pairing contributions are consumed by
the verification and saved without truncation. Actual minimum weight
and coefficient sum are zero, meeting the required nonnegative bounds;
the actual pairing lies in the negative interval, contrary to the
required nonnegative lower bound. Decimal phase I proposes the basis
only; its status is not the proof. There was no failed mathematical
check in this attempt. The shared JSON inspector initially encountered
Python's integer-string limit on existing large fractions; setting
PYTHONINTMAXSTRDIGITS=0 resolves inspection without changing any evidence.

This verification is part of the construction attempt, not a dedicated
critical proof audit. The old dictionary and reviewed family contracts
are imported inputs, not freshly audited ancestor proofs. L078 and
ATTEMPTS/060 remain valid at their different fixed column. L079 and
ATTEMPTS/061 correctly stop its old weights' strict family exclusion.
The new separator's behavior away from t_star is untested. No scalar
upper row, other-anchor matrix, global extension, uniform bound, actual
code or unsafe RS list follows from this fixed-point rejection.

**Separate critical proof review — step 282, 2026-10-17.** Reuse the
pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-17-eight-maximizer-obstruction-critical-audit.md`.
This review retains the theorem, its precise fixed interpolation and its
essential nonnegative-moment hypothesis. No mathematical coefficient,
input or conclusion is changed. This is a reviewed local reproduction,
not a discovery beyond the sources checked.

The full manuscript and both original programs were compared with the
source hypotheses and qualifications in foundations/04,09,10,12. The
Schrijver layer ranges contain 0,5,6,7,8 in both factors. Exactly the
81 product modes occur, with the anchor only at (0,0). Their positive
multiplicities sum to S_l on every retained shell. Sano's criterion
covers singular and empty old blocks. The finite averaging group
Sym(D) times Sym(D-complement) preserves the entire prescribed dictionary,
the fixed transported columns, every equal-union identification and the
nonnegative free entries. An arbitrary completion can therefore be
averaged without adding a labeled constraint. Goemans's nonnegative
variable case applies; the free-variable cancellation case does not
justify the nonzero coefficient at (6,3).

The independent verifier rerun passes all 5599 checks. A separate audit
reconstructs L021's original pair equations and factor two, L053's rho,
the exact seven-column parameters and original RREF, and L073's entire
36-coordinate completion from its defining equations in reverse variable
order. Every one of L075's 270 dictionary entries agrees. These are
reconstructions of the imported ancestor recipes, not fresh recursive
audits of every ancestor proof. L076's whole-kernel exhaustion and
L079's stationary-parameter contract remain explicit imported inputs.

Recover all 85 affine rows from the original eight-column RREF with
nonpivots (56,63,69,78). Re-solve both manuscript vertex systems and form
the exact interpolation using s_star=-M04/M44. All coordinates agree
with L079 and both L080 certificates; 0<alpha<1. Exactly factors 33,56
vanish, and the other 83 are positive. Every original compatibility
equation holds. All 90 orbit-weighted kernel residuals vanish, retaining
the anchor. Reconstruct actual supports from their eight disjoint regions
and recount all six presentations of all 500 relation types. Every atom,
distance, lookup and shared full key agrees, both coefficientwise in the
imported family and at the fixed point. There are precisely 36 forced
eight/eight entries and 45 distinct free keys, with the forced formulas
in the proof above unchanged.

For the normalization audit, reuse L078's reviewed 220 complete direct
subset-transition matrices, whose entries depend only on factor sizes
and layers. Check every saved action coordinate again, including absent
modes, positive squared norms, orthogonality, zero-beta cases and both
rectangular directions. For each factor, let N_(l,a) be the squared norm
of its monic degree-a basis and sigma_(l,m,a)=N_(l,a)*gamma/beta. All
nonzero ratios are positive and independent of the relation. The exact
identities

    sigma_(l,m,a)*sigma_(8,8,a)=sigma_(l,8,a)*sigma_(m,8,a)

hold for every retained l,m,a. Tensoring gives one coherent congruence
for the entire block:

    K_lm=(N8/D8)*s_l*T_lm*s_m,  s8=1, s_l>0.

Here K is the direct bilinear block, N8 is the product of the two
reference-eight squared norms, and s_l is the product of the two
sigma_(l,8) values divided by N8/D8. Evaluate every old entry and both
cross directions using these direct actions. Every equality holds.
In the constant mode subtract p_l*p_m*S_m before multiplying by the
row norm; this gives the full source anchor term p_l*p_m*S_l*S_m.
The direct forced diagonal and all 45 free coefficients reproduce every
original mode inequality. Neither pairwise squared scales nor a quotient
pseudoinverse is substituted for this whole-block check.

Expand all 306 old source principal determinants by the complete
Leibniz formula (their sizes are at most three), independently of the
verifier's elimination. Each is nonnegative. The corresponding direct
weighted determinant equals it times the product of the positive
congruence factors. Reverse-order elimination of each direct old block
checks every nonnegative pivot and every zero-pivot old-row and cross
residual. For the 36 three-old-layer modes the ranks 0,1,2,3 occur
19,8,4,5 times; for the 13 two-old-layer modes ranks 0,1,2 occur 3,3,7
times; for the 15 one-old-layer modes ranks 0,1 occur 4,11 times. All
17 new-only modes retain zero old cost. Every original inverse residual
is checked again. The direct cost divided by p8*N8 equals the original
source cost divided by p8*D8 in every mode. All 81 complete right sides
and all 3645 free coefficients agree with both original programs.

Parse I,J from this manuscript and solve K^T*y=c by reverse-variable
elimination and back substitution, independently of the verifier's
Gauss–Jordan solve and without a numerical optimizer. All 43 pivots
are nonzero; every defining equation is checked in the original order.
The full 81 weights agree, sum to one, and have exactly 38 positive
entries. Reconstruct all 45 scaled sums from the direct actions and
all 45 raw sums independently from beta. Exactly 44 vanish and only
(r,q)=(6,3), corresponding to Y_88(2,5), is positive. The weighted
forced, anchor and range-cost terms separately agree with the verifier;
their signed sum satisfies exactly

    -25046444520/10^6 <= v < -25046444519/10^6 < 0.

Thus the required lower bound 0<=sum s_j*z_j contradicts v<0. The
nonnegative sign of Y_88(2,5) is essential. This audit supplies no
signed-completion or family-wide rejection and no scalar upper-row,
other-anchor, global-moment, RS-realization or boundary conclusion.

Run from the notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_eight_maximizer_joint_completion.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_eight_maximizer_joint_completion.py

The dedicated audit passes 13031 additional exact checks with no failed
checks. Full inputs, reconstructed entries, direct actions through their
reviewed transition input, all old minors, singular stages, original
inverse vectors, complete modes, exact dual system/pivots, raw/scaled
sums and pairing components are saved in
`scripts/finite-support/eight-maximizer-joint-completion-critical-audit.json`.
Every load-bearing value is consumed by complete arithmetic checks; a
summary preview is not the evidence. Actual minimum weight and scaled
sum are zero, meeting the required nonnegative bounds; the actual
pairing is strictly negative rather than the necessary nonnegative value.
L078, L079 and ATTEMPTS/060–062 remain valid at their stated scopes.

## Mathlib

Full matching prescribed mixed-layer nonnegative completion obstruction:
not checked. Full mixed-layer decomposition, singular generalized Schur
criterion, constrained equal-union moment LP certificates and supporting
PSD/binomial/rational results: not checked. Unknown coverage is not
absence. General results are imported by precise citations above; no
source-level originality or complete RS resolution is claimed.
