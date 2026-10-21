# L083 — L082's unchanged separator has an attained zero on the column family

## Hypotheses

Use n=1024,w=68, L021's original pair prescription, L053's positive
singleton rho and p8=16792471/1181138102168120460>0. Divide matrices by
rho. The old included-anchor PSD base is exactly L073's matrix on D
and all {D,E} at half-distances 5,6,7. Preserve L075's entire dictionary,
its original seven-column RREF at (0,v_dagger,w_star), all 28 forced
and 36 completed seven/seven moments. All ancestral review qualifications
remain imported; this is not a new critical audit of those results.

Use L076's original affine family f=c+A_family*t, with original parameter
order t=(t56,t63,t69,t78), and its full domain

    T={t in R^4: c+A_family*t>=0}.

There are 85 factors, with free indices 56,63,69,78 in the rank-81 RREF
of the original 90 compatibility equations. Every new column uses the
same t, free moments p8*f_j, original fixed entries, anchor and diagonal.
Retain all complete unordered keys, Boolean repetitions, forbidden distinct
half-distances 1,...,4 and all 36 forced eight/eight entries. Only the
other 45 eight/eight moments vary. Keep L078's original positive scaling
z, all 81 included-anchor modes, full anchor and singular/empty ranges.

Let y be exactly L082's unchanged nonnegative 81-weight separator,
defined by its canonical 46-by-46 system, not newly optimized. Write

    A_mode*z<=b(t), Phi(t)=y^T*b(t)

in L079/L081's original family-mode notation. This tests only these
fixed weights on T; no new separator, scalar upper row, other anchor,
changed pair/base moment or global extension is imposed.

## Conclusion

There are canonically specified rational gamma>0 and s with

    Phi(t)=-gamma*(t78-s)^2                 for every t in R^4.

The maximum on T is exactly zero and is attained at the rational
interpolation specified below. At that point precisely factors 33 and
56 vanish; the other 83 factors are positive. All 45 original and raw
free-moment coefficients of y remain zero throughout the family.

Thus strict negativity of L082's unchanged separator on all of T is
false. Any simultaneous completion satisfying these original modes
would necessarily have t78=s, even if its free eight/eight moments were
signed. This necessary plane is not asserted to admit a completion.
The attained zero supplies no individual-mode, simultaneous PSD, global
moment, packing, RS-list or boundary verdict. L082's rejection of its
different fixed point remains valid. Arbitrary-center safety at 67/68
agreements and the 955–957 bracket remain unresolved.

This is a local REPRODUCTION of assessed methods and a negative result
for the prescribed uniform strict-exclusion test. It makes no claim of
progress beyond the checked sources as original mathematics. The separate
critical proof review below retains this result.

## Proof

**Imports and their limited application.** The prior SPECIALIZE assessment
is `drafts/literature/2026-10-17-fully-cancelling-separator-family-test.md`.
Use Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. L078's reviewed entry-independent coherent four-layer
normalization is retained on factors 68,956 and layers 0,5,6,7,8, with
both rectangular directions. No actual-label restriction is averaged.

For the singular reduction import Takashi Sano, *Moore-Penrose inverse,
generalized Schur complement and inertia*, version of record 27 February
2026, [DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2, Theorem 2.6 and Lemma 2.7. The retained real
symmetric base is PSD, including its singular blocks. Compatibility of
each affine cross vector with the whole base kernel is checked below;
no Euclidean quotient pseudoinverse replaces the actual weighted action.
Use Sven C. Polak, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Sections 1.1 (1)–(3), Proposition 1.1 and its indicator
proof p.2, and 1.2 p.3, for the ordinary equal-union slice. Preserve
foundations/12's constant-weight display qualification and L082's reviewed
signed averaging justification, which needs no free-moment signs.

The free-variable separator implication is Michel X. Goemans,
*Advanced Algorithms*, Lecture 3, 19 September 2001, Theorems 1 and 3,
printed pp.1–2, [MIT notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf).
Here y>=0 and y^T*A_mode=0. A completion would require Phi(t)>=0.
There is no SDP strong-duality or Slater claim. General theorems are
imported without reproof. The finite coefficient calculation below is
needed because none gives this prescribed family pairing. The assessed
QP theorem is unnecessary: the explicit square and attained zero decide
the maximum directly. Foundations/04,09,10,12 keep their qualifications.

**Recovering the same entire family.** Recover c and A_family from
L076's original RREF: set each of nonpivots 56,63,69,78 in turn, retaining
the original right side. Direct coefficientwise substitution checks all
90 compatibility equations. Build the full 150-coordinate affine column,
including its anchor p8, with orbit weights

    W_0=1,
    W_(l,i,j)=C(8,i)C(60,l-i)C(8,j)C(948,l-j).

All five coefficients of each of the 90 weighted kernel pairings are
zero. L076's reviewed exhaustion therefore supplies the whole original
range condition on the entire affine family, not just at a point.

For l<=m in {5,6,7,8} and 0<=i,j<=l, the complete membership atoms are

    (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

Construct disjoint-region actual supports and all six presentations.
Every available Boolean, forbidden, old or column lookup agrees as a
five-coefficient affine function on each full key. All 500 types and
3000 presentations are retained, with 36 forced eight/eight entries and
45 distinct free keys. No additional affine equality or domain restriction
is introduced. The 270 old entries are constant and unchanged. Independent
bit permutation of the eight atoms reproduces all presentations.

**Exact family-mode specification.** Use C(n,k)=binomial(n,k), zero
outside 0<=k<=n, S_l=C(68,l)C(956,l), and precisely L082's displayed
beta formula. For each mode i=9a+b, 0<=a,b<=8, and old layers l,m in
{5,6,7} with l,m>=max(a,b), let

    T_lm(t)=sum_(u,v=0)^min(l,m) beta(68,l,m,a,u)beta(956,l,m,b,v)Y_lm(u,v;t)
             -1_(a=b=0)*p_l*p_m*S_l*S_m,
    B_i=(T_lm), cross_i(t)=(T_l8(t)),
    D_i=C(68-2a,8-a)C(956-2b,8-b)>0.

Use sorted layers for a reversed direction. B_i is constant. Solve its
largest nonsingular principal subsystem on each of the five affine cross
coefficients, with zero unused coordinates, giving x_i(t). Verify every
original row B_i*x_i(t)=cross_i(t) coefficientwise. All 306 old principal
minors are nonnegative. All 36 three-old-layer, 13 two-old-layer, 15
one-old-layer and 17 new-only modes are retained, including zero blocks.
Define

    F_i(t)=sum_(forced u,v) beta(68,8,8,a,u)beta(956,8,8,b,v)Y_88(u,v;t)/(p8*D_i),
    H_i=1_(a=b=0)*p8*S8,
    R_i(t)=cross_i(t)^T*x_i(t)/(p8*D_i),
    b_i(t)=F_i(t)-H_i-R_i(t).

The affine forced contribution and quadratic cost are thus fully specified
by the original data. The positive p8^2 anchor term is retained before
normalization. These reproduce L079/L081's original family bounds.

Reconstruct y from L082's manuscript I,J and K^T*y_I=(-1,0,...,0),
where K_(i,-1)=-1 and K_(i,j)=(A_mode)_ij. All 46 pivots are nonzero.
The resulting y has sum one, 28 positive entries and all other entries
zero, and agrees exactly with the prior fixed-point certificate. For all
45 (r,q) with 0<=r,q<=8 and r+q>=8, independently check

    sum_i y_i*(A_mode)_(i,rq)=0,
    -sum_(a,b) y_(9a+b)*beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)/(p8*D_(9a+b))=0.

These are respectively the original scaled and raw-moment coefficients.
They have no parameter dependence, so cancellation holds on all of T
and permits signed free moments in the necessary implication.

**Square identity and an attained zero.** Put zeta=(1,t56,t63,t69,t78).
Let the symmetric rational 5-by-5 matrix M be defined uniquely by

    zeta^T*M*zeta = sum_i y_i*(F_i(t)-H_i-R_i(t)).

For each affine constant add it to M_00, split its linear coefficients
equally between M_0j and M_j0, and subtract the quadratic cost matrix.
Complete exact reconstruction gives

    M_ij=0 if i or j is in {1,2,3},
    M_44<0, M_00*M_44=M_04^2.

Define gamma=-M_44>0 and s=-M_04/M_44. These finite rational recipes,
together with the original RREF and canonical weight system, uniquely
specify both constants without rounding. The certificate stores the full
matrix and every contributing rational coefficient. Substitution gives
M=-gamma*e*e^T, e=(-s,0,0,0,1). Therefore Phi(t)=-gamma*(t78-s)^2
on all R^4 and is everywhere at most zero. This is an exact matrix
identity, not a fitted quadratic or numerical rank claim. At L082's
old point it reproduces the original strictly negative pairing.

Let A_I mean the four indicated rows of A_family, and define

    t0=-(A_(27,33,56,63))^(-1)*c_(27,33,56,63),
    t1=-(A_(5,26,33,56))^(-1)*c_(5,26,33,56).

These are L076's active column and L079's domain vertex. Both defining
matrices are nonsingular. Fresh exact solves check all 85 inequalities
at both endpoints, so t0,t1 belong to T. Exact rational comparison gives

    (t0)_78 < s < (t1)_78.

Set alpha=(s-(t0)_78)/((t1)_78-(t0)_78), so 0<alpha<1, and let
t_star=(1-alpha)*t0+alpha*t1. Every affine factor at t_star is the same
convex combination of its two nonnegative endpoint values. Thus t_star
belongs to the full original T, and (t_star)_78=s. Direct substitution
also checks all 85 signs: only factors 33,56 vanish, and 83 are positive.
All original compatibility and full weighted kernel residuals vanish.
The full 81-bound weighted pairing, with forced, anchor and cost terms
separately retained, is exactly zero. This is an attained maximum; no
compactness or unattained-supremum argument is used.

This attained zero refutes strict negativity on T. Conversely, the
necessary separator inequality and square identity force t78=s in any
completion. No individual inequality at this point is claimed to hold;
in particular, zero pairing is not a PSD witness. This is the end of
the approved fixed-weight test.

**Evidence, failures and limits.** Reproduce from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/fully_cancelling_separator_family.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_fully_cancelling_separator_family.py

The constructor passes 7283 exact checks with no failures. Its full
certificate is `scripts/finite-support/fully-cancelling-separator-family-results.json`.
The independent verifier uses no constructor, optimizer or floating
arithmetic. It recovers the original RREF and all affine keys, uses a
different bit-permutation enumeration, reverse-order singular elimination
on all five affine cross coefficients, and Gauss–Jordan rather than
Cramer endpoint solves. Every zero pivot retains its full affine range
row. It checks every original inverse residual and canonical weight
equation, all raw cancellations, the full square matrix identity, all
endpoint/witness signs and every original witness bound. It also compares
the imported step-290 full affine/kernel contracts and all 81 original
fixed specializations, including forced, anchor and range-energy terms.
It passes 5065 exact checks with no failures. Its full certificate is
`scripts/finite-support/fully-cancelling-separator-family-verification.json`.
These are complete-array arithmetic checks within this attempt, not the
later separate critical proof review. Certificate previews are not used
as proofs. Actual pairing is 0 against the required nonnegative bound 0;
actual minimum factor is 0 against the domain bound 0.

The initial unconstrained stationary representative with its other three
parameters set to zero violated factor 33, so it was not used as a
witness. Full evidence is `scripts/finite-support/fully-cancelling-family-diagnostic.json`.
The final interpolation instead verifies all original domain rows. The
first constructor invocation stopped on a Python name-shadowing TypeError
before producing a verdict; `scripts/finite-support/fully-cancelling-family-initial-failure.json`
records it. Renaming the local certificate variable changed no coefficient.
The shared inspector initially hit Python's integer-string limit; using
PYTHONINTMAXSTRDIGITS=0 allowed bounded inspection without changing data.
Preserve L078–L082 and ATTEMPTS/060–064 in their distinct scopes.
Other separators, other anchors, scalar upper rows, changed pair/base
moments, global consistency and RS realization remain unresolved.

**Separate critical proof review — step 294, 2026-10-17.** Reuse the
prior SPECIALIZE assessment
`drafts/literature/2026-10-17-fully-cancelling-family-critical-audit.md`.
The review retains the theorem, its attained-zero family stop and its
conditional necessary plane, including signed free moments. No new
separator or completion was sought, and no source-level discovery is
claimed. Reproduce the dedicated audit from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_fully_cancelling_separator_family.py

All 10777 exact checks pass, with no failures. Full rational evidence is
`scripts/finite-support/fully-cancelling-separator-family-critical-audit.json`.
The audit invokes no constructor, verifier or optimizer. It adapts the
inspected earlier family-audit machinery, importing only exact arithmetic
helpers from L078's audit. It consumes and compares complete relevant
arrays from the step-290 and step-292 certificates, rather than treating
previews, clean-report labels or matching hashes as proofs.

The audit checks L021's original pair equations and reconstructs rho,
p8, the original seven-column parameters and RREF, and L073's completion
from its 35 defining rows and the last zero coordinate. All 270 old
dictionary entries agree. These checks import ancestor uniqueness and
PSD contracts with their recorded qualifications; they are not recursive
reviews of those results. The original rank-81 RREF recovers all 85
affine factors. Every one of the 90 original compatibility equations
and every coefficient of all 90 orbit-weighted kernel equations holds.
L076's reviewed whole-kernel exhaustion remains an explicit input.
Actual disjoint-region supports reconstruct all 500 types and 3000
presentations, the 36 forced entries and 45 distinct free keys.

All 220 factor transition matrices are independently reconstructed by
the four-region binomial formula displayed in L076 and L078, and their
row totals and complete actions agree with L078's reviewed actual-subset
enumeration. Positive weighted norms, orthogonality, signed beta ratios
and all reference-eight identities give the same single coherent
whole-block congruence. Both cross directions are checked on all five
affine coefficients. The constant mode retains the entire anchor term.
All 306 source principal minors are recomputed by permutation expansion.
Reverse-layer elimination keeps every zero-pivot row and all its affine
cross coefficients. By increasing rank, the distributions for 3,2,1,0
old layers are respectively (19,8,4,5), (3,3,7), (4,11), (17).
Thus singular, zero and empty cases are all retained. All five original
inverse equations in every mode hold; their full bilinear cost matrices
agree with direct weighted elimination. Positive multiplicities exhaust
each full layer, not merely the invariant stabilizer coordinates.

The manuscript's entire 46-by-46 system is solved in reversed variable
order with forward elimination and back substitution. All pivots and
defining equations are checked. Its unchanged 81 weights have sum one,
28 positive entries and no negative entries. Every original and raw
free coefficient cancels separately. Fresh reconstruction compares all
25 entries of each mode's quadratic and of their weighted sum, retaining
forced, anchor and inverse-action terms separately. The exact identity
M=-gamma*e*e^T holds with gamma>0 and e=(-s,0,0,0,1). Its specialization
at L082's old point reproduces that theorem's strict negative interval.

The two active sets are read from this manuscript. Fresh nonsingular
solves verify all 85 endpoint signs, with precisely their stated four
zeros, and both strict t78 comparisons. Every interpolated factor is
checked as the same convex combination of endpoint factors. The resulting
point has exactly zeros 33,56 and 83 positive factors. All original
compatibility equations and weighted kernel equations hold there. The
81 reconstructed bounds have weighted sum exactly zero, both directly
and as weighted forced minus anchor minus cost. Thus actual pairing 0
meets the necessary bound 0, and actual minimum factor 0 meets the
domain bound 0. The inadmissible zero representative still violates
factor 33; the earlier pre-verdict TypeError remains preserved.

For every fixed t in the entire original domain, permutations in
Sym(D) times Sym(D-complement) preserve each prescribed coefficient:
the five-coefficient full-key checks establish this uniformly in t.
They fix the parameter value, original pairs, base, anchor and all
Boolean/forbidden entries. Averaging any signed union assignment over
this finite group preserves its linear equalities and PSD by permutation
congruence, without needing signs on unspecified moments. Hence the
checked invariant mode inequalities are necessary also for a signed
completion. With y>=0 and y^T A_mode=0, those inequalities require
Phi(t)>=0; the checked square then forces t78=s. Attainment of zero
does not reverse this implication or verify any individual inequality.
The Schrijver and Sano hypotheses, including all singular cases, match
the imported finite real base and source normalization. No general
theorem is reproved. Other anchors, scalar upper rows, a simultaneous
completion, global consistency and RS realization remain unresolved.

## Mathlib

Full matching fixed-separator family identity and attained-zero verdict:
not checked. Supporting mixed-layer algebra, singular Schur complement,
Farkas, rational linear algebra and quadratic-form coverage: not checked
here. Unknown coverage is not absence. General results are imported by
the precise citations above; no source-level novelty claim is made.
