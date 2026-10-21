# L082 — L081's common column has no simultaneous completion

## Hypotheses

Use n=1024,w=68, the original pair prescription of L021, and L053's
positive singleton rho. Divide moment matrices by rho. The old
included-anchor matrix is exactly L073's matrix on the anchor D and all
indices {D,E} with |D\E| in {5,6,7}. Its entire dictionary is L075's:
the original seven-column RREF at (0,v_dagger,w_star), 28 forced and
36 completed seven/seven entries remain immutable. Its PSD conclusion
and ancestral review qualifications are imported, not newly audited.

The new layer consists of all {D,G} with |D\G|=8. Against the old
matrix every column is exactly L081's common admissible L076 column,
transported by point bijections. In L081's canonical notation, let M_1,
M_2 be the two unchanged separator quadratic matrices and set

    s=-M_1[0,4]/M_1[4,4],
    G=(M_2[i,j])_(i,j in (2,3)),
    g=(M_2[i,0]+M_2[i,4]*s)_(i in (2,3)),
    (u,v)^T=-G^(-1)g,
    t_dagger=(0,u,v,s).

Use this exact rational point, not L079's different interpolation.
The original 85 factors are f=c+A_family*t_dagger, with exactly f56=0
and 84 positive factors. Each free column moment is p8*f_j, where

    p8=16792471/1181138102168120460>0.

The anchor, diagonal, all full unordered keys, Boolean cases and forbidden
distinct half-distances 1,...,4 are retained. The 36 forced eight/eight
moments are fixed by these data. Only the other 45 eight/eight moments
may vary; the approved test requires them nonnegative. Include all
81 modes, the full anchor correction, and singular/empty old ranges.
No scalar upper row, other-anchor condition, actual-label restriction,
different base/pairs or global extension is assumed.

## Conclusion

There is no simultaneous included-anchor PSD completion with these data.
An exact separator has 28 positive mode weights, cancels all 45 free
coefficients in both scaled and original moment coordinates, and has
fixed pairing V satisfying

    -1935470/10^14 <= V < -1935469/10^14 < 0.

Consequently even signed choices of the 45 new moments cannot complete
this fixed matrix: the stronger implication uses the same certificate,
without a new search or any nonnegative-moment sign row.

This is a local REPRODUCTION of assessed methods and a fixed-point
negative result, without a source-level novelty claim. L081's two
positive aggregate pairings remain correct; different weights give this
obstruction. Other family points, other base/pair choices and global
moments remain unresolved. No RS list bound or change to the 955–957
bracket follows. The separate critical proof review below retains this result.

## Proof

**Imported methods and applicability.** The pre-invocation SPECIALIZE
assessment is `drafts/literature/2026-10-17-common-separator-column-joint-completion.md`.
Reuse Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. The factors 68,956 and layers 0,5,6,7,8 fall in its
index ranges. L078's reviewed entry-independent subset actions and
coherent positive four-layer congruence apply unchanged when the
prescribed column values change. Both rectangular directions and all
mode multiplicities are retained. No actual-label symmetry is imported.

For singular old blocks use Takashi Sano, *Moore-Penrose inverse,
generalized Schur complement and inertia*, version of record 27 February
2026, [DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2, Theorem 2.6 and Lemma 2.7. The retained finite
real symmetric base is PSD; each cross vector must be in its range,
and the remaining scalar generalized Schur complement must be
nonnegative. Singular and empty blocks are included. All ranges below
are checked explicitly; no quotient Euclidean pseudoinverse is used.

For equal-union moments and constraint-preserving finite averaging use
Sven C. Polak, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Sections 1.1 (1)–(3), Proposition 1.1 and complete
indicator proof p.2, and 1.2 p.3. Preserve foundations/12's qualification
that the displayed final bound omits w, whereas the constant-weight
proof supplies A(n,d,w). Here the ordinary slice has n=1024,d=10,w=68.
Permutations fixing D preserve every imposed datum, including the
transported identical columns, all full keys and signs. Averaging
preserves PSD, so exclusion of the invariant system excludes any
completion satisfying these data. This uses no labeled RS restriction.

The finite linear alternative is imported from Michel X. Goemans,
*Advanced Algorithms*, Lecture 3, 19 September 2001, Theorems 1 and 3,
printed pp.1–2,
[MIT notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf).
The explicit certificate below needs only its sufficient implication;
no Slater hypothesis, optimizer status or converse SDP alternative is
used. Foundations/04,09,10,12 retain their source qualifications. These
general theorems are imported without reproof; they do not give the
prescribed-data verdict, which requires the finite rational calculation.

**Original system at the exact point.** Write C(n,k)=binomial(n,k),
zero outside 0<=k<=n, and S_l=C(68,l)C(956,l). Reconstruct the 85 affine
factors from L076's original RREF with nonpivots 56,63,69,78, substitute
t_dagger, and check all 85 domain rows and 90 original equations.
The entire 150-coordinate column, with orbit weights

    W_0=1,
    W_(l,i,j)=C(8,i)C(60,l-i)C(8,j)C(948,l-j),

annihilates all 90 full weighted kernel vectors. L076 supplies their
exhaustion; this calculation checks every weighted residual at this point.

For l,m in {5,6,7,8}, l<=m, and 0<=i,j<=l, the full membership atoms
of D,E,G are

    (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

These give all 500 types. Construct actual 68-subsets from disjoint
regions and inspect all six ordered presentations. Repetitions use
the original pair value; a forbidden distinct distance uses zero;
otherwise every available old/column lookup must agree on the full
unordered key. All 3000 presentations agree, including reanchorings
outside the retained layers. The 45 unspecified keys are distinct.
For eight/eight, put r=8-i,q=8-j. The 36 forced entries are

    Y_88(8,8)=p8,
    Y_88(8-r,8-q)=0                  if 1<=r+q<=4,
    Y_88(8-r,8-q)=Y_(r+q,8)(q,r)     if 5<=r+q<=7.

For r+q>=8 use lexicographic order and the original positive scaling

    V_rq=C(8,r)C(60,r)C(8,q)C(948,q),
    Y_88(8-r,8-q)=p8*z_rq/V_rq.

In the following beta is precisely

    beta(n,l,m,a,t)=sum_(h=max(a,t))^min(l,m,n-a)
      (-1)^(h-t)C(h,t)C(n-2a,h-a)C(n-a-h,l-h)C(n-a-h,m-h).

For mode (a,b), 0<=a,b<=8, let the old layers be the l in {5,6,7}
with l>=max(a,b). After eliminating the positive anchor, form

    T_lm=sum_(i,j=0)^min(l,m) beta(68,l,m,a,i)beta(956,l,m,b,j)Y_lm(i,j)
         -1_(a=b=0)*p_l*p_m*S_l*S_m,
    B_ab=(T_lm)_(old l,m),  t_ab=(T_l8)_(old l),
    D8_ab=C(68-2a,8-a)C(956-2b,8-b)>0.

When l>m use the symmetric entry with sorted layers. All 306 nonempty
old-block principal minors are nonnegative. Choose a largest nonsingular
principal subsystem, solve for x on it and set other coordinates zero;
directly verify every row B_ab*x=t_ab. This includes every singular
range, with zero vectors for empty old blocks. Define

    F_ab=sum_(forced i,j) beta(68,8,8,a,i)beta(956,8,8,b,j)Y_88(i,j)/(p8*D8_ab),
    H_ab=1_(a=b=0)*p8*S8,
    R_ab=t_ab^T*x/(p8*D8_ab),
    b_(9a+b)=F_ab-H_ab-R_ab,
    A_(9a+b,(r,q))=-beta(68,8,8,a,8-r)beta(956,8,8,b,8-q)/(D8_ab*V_rq).

The full generalized Schur remainder divided by positive p8*D8_ab is
b_i-(Az)_i. Thus every proposed completion requires Az<=b. Retain all
36 three-old-layer, 13 two-old-layer, 15 one-old-layer and 17 new-only
cases. In particular H_00 retains the original positive p8^2*S8^2
before normalization. The independent original-beta reconstruction of
every bound agrees with L081's full quadratic bound at the same point.
No isolated-column energy or aggregate-separator pass substitutes for
these individual inequalities.

**Canonical exact separator.** Number the rows by 9a+b and the 45
lexicographic (r,q) coordinates from zero. Set

    I=(0,1,2,3,4,5,6,7,9,10,11,12,13,15,17,18,19,20,21,22,
       23,24,25,27,28,29,30,31,32,36,37,38,39,40,41,45,46,47,
       48,54,55,56,57,63,64,72),
    J=(-1,0,1,...,44).

Let K_(i,j)=-1 when j=-1 and K_(i,j)=A_ij otherwise, with these orders.
Solve the 46-by-46 system K^T*y_I=e, where e_-1=-1 and all other e_j=0;
put y_i=0 outside I. Exact Gaussian elimination has a nonzero pivot in
every column, uniquely defining this rational vector without a solver.
Substitution into all original rows/columns checks

    y>=0, sum_i y_i=1, exactly 28 y_i>0,
    sum_i y_i*A_ij=0 for every j=0,...,44.

Independently compute every original raw-moment coefficient as

    -sum_(ab) y_(9a+b)*beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)/(p8*D8_ab).

Each equals (sum_i y_i*A_ij)*V_rq/p8=0. Hence no nonnegativity
coefficient or sign-row weight is needed. The complete rational pairing

    V=sum_i y_i*b_i=sum_i y_i*F_i-sum_i y_i*H_i-sum_i y_i*R_i

has the strict interval in the conclusion, verified by integer cross
multiplication. All three weighted contributions agree separately.
Consequently any real z satisfying Az<=b would give

    0=y^T*A*z<=y^T*b=V<0,

which is impossible. This excludes the invariant completion, and the
constraint-preserving averaging above excludes every proposed completion.
Multiplication by positive rho preserves the original-normalization verdict.

**Evidence, failure preservation and limits.** Reproduce from this notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/eight_common_column_joint_completion.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_eight_common_column_joint_completion.py

The constructor stages the exact point and original system before one
bounded Decimal phase-I calculation. That proposes a basis only; the
separator and strict verdict are reconstructed with Fractions. It passes
410 exact checks, with no failures. Full certificate:
`scripts/finite-support/eight-common-column-joint-completion-results.json`.

The separate standard-library verifier uses no optimizer. It recovers
the original RREF family, independently solves the point's 2-by-2 recipe,
checks all weighted kernel residuals, constructs actual supports and all
presentations, rebuilds every original beta coefficient and bound, checks
all 306 old minors and all singular ranges, and solves the explicit
46-by-46 separator system by Gauss–Jordan elimination. All 5722 checks
pass with no failures. Its full rational evidence is
`scripts/finite-support/eight-common-column-joint-completion-verification.json`.
Actual mode-weight minimum is zero, meeting the required bound zero;
every scaled/raw free coefficient is exactly zero. The actual pairing
is in the displayed negative interval, while feasibility requires it
nonnegative. Complete relevant arrays are consumed and compared, not
inferred from previews or hash equality alone.

The initial verifier report is preserved at
`scripts/finite-support/eight-common-column-joint-completion-verification-initial.json`.
Its sole failure was a reporting predicate requiring the coarse interval's
upper endpoint to be strictly negative. That interval was [-10^-6,0),
which already implies strict negativity. Correcting the predicate to permit
an open endpoint zero and adding the finer strictly negative interval
changed no point, coefficient, weight, range or pairing. The initial
5719-check report is not represented as a clean verification.

This arithmetic verification is part of this single completion attempt;
it is not the later dedicated critical proof review. L078's normalization
audit and the base/kernel inputs retain their own review qualifications.
The older fixed-point rejections and L081's two positive aggregate
pairings remain valid. This result neither excludes the whole column
family nor supplies a bound over other pair/base moments, untested anchors,
global moments, actual packings or RS lists.

**Separate critical proof review — step 290, 2026-10-17.** The prior
SPECIALIZE assessment is
`drafts/literature/2026-10-17-common-column-obstruction-critical-audit.md`.
This review retains the fixed-point theorem, including its signed-completion
consequence, without claiming a new result beyond the assessed methods.
The original constructor and verifier and the complete argument above were
inspected against the cited source hypotheses and essential ancestor recipes.
The source qualifications and ancestral review scope remain unchanged.

Reproduce the dedicated audit, which invokes no optimizer or constructor:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_eight_common_column_joint_completion.py

All 13509 exact checks pass with no failures. The complete evidence is
`scripts/finite-support/eight-common-column-joint-completion-critical-audit.json`.
A rerun of the original independent verifier also passes its 5722 checks.
The dedicated audit imports only arithmetic helpers from the inspected
L078 audit; it adapts L080's inspected finite audit machinery to the new
point, with a fresh reconstruction and different elimination order from
L082's verifier. It does not treat agreement of hashes or previews as
mathematical verification.

The audit checks every defining original pair equation and reconstructs
rho and p8, retaining the factor two in the pair prescription. It recovers
the original seven-column parameters and RREF, solves the 35 defining
completion rows together with z_(7,0)=0 in reversed variable order, and
reconstructs all 270 old dictionary entries. These computations import
ancestor uniqueness and source-system contracts; they do not recursively
review their entire proofs. The two quadratic matrices defining the point
are imported from L081's completed audit, then the 2-by-2 system is freshly
solved. All 85 factors agree, with precisely factor 56 zero; every original
compatibility equation and all 90 actual orbit-weighted kernel residuals
vanish. L076's full-kernel exhaustion remains an imported reviewed input.
All 500 types and 3000 actual-support presentations are reconstructed,
including reanchored lookups, Boolean cases and forbidden distances.
All 36 forced entries and 45 distinct free full keys agree.

For coherent normalization, the audit consumes every coordinate of L078's
reviewed weighted bases and direct actions and checks their orthogonality
and positive norms. It independently reconstructs every entry of all 220
factor transition matrices in both orientations. For fixed |U|=8, |X|=l,
|U intersection X|=i, the number of m-subsets Z with |Z intersection U|=j
and |Z intersection X|=k is

    sum_h C(i,h)C(8-i,j-h)C(l-i,k-h)C(n-8-l+i,m-j-k+h).

This is the disjoint-region counting specialization of the reviewed subset
action, not a new general theorem. All entries and row totals agree with
L078's independent actual-subset enumeration. Every signed beta ratio and
reference-eight triangle identity is checked. Thus, with N8 the product
of the two squared norms, the entire weighted block satisfies the single
positive congruence K_lm=(N8/D8)*s_l*T_lm*s_m, s8=1. Both cross directions
agree. In the constant mode the weighted anchor term is
-p_l*p_m*S_m times the row norm, giving exactly the original source term
-p_l*p_m*S_l*S_m. No separate squared rectangular scale or pseudoinverse
congruence is substituted for this whole-block identity.

All 306 old principal minors are recomputed by complete permutation
expansion. Reverse-order elimination of each weighted old block checks
its nonnegative pivots and every zero-pivot row and cross coordinate.
For old-layer counts 3,2,1,0, the rank distributions respectively are
(19,8,4,5), (3,3,7), (4,11), (17), with entries ordered by increasing
rank. Thus all 36,13,15,17 mode cases remain, including zero and empty
ranges. Every original inverse-action residual is also verified directly.
The direct weighted energy equals the original beta energy divided by
p8*D8 in every mode. All full fixed, anchor and required contributions,
all 81 bounds and every one of their 45 original coefficients agree.
Positive multiplicities sum to each layer's full dimension.

Read I and J from this manuscript, rebuild the entire transposed
46-by-46 system, and solve by reverse-variable forward elimination and
back substitution, rather than the original verifier's Gauss--Jordan
elimination. Every pivot is nonzero and every defining equation holds.
The 81 weights agree exactly with both certificates, sum to one, are
nonnegative and have exactly 28 positive entries. Independently summing
all 45 original and raw coefficients gives zero in every coordinate.
The three full weighted contributions separately agree with the original
verifier. Exact rational cross multiplication verifies the stated strict
negative interval; the feasibility requirement would instead be V>=0.

For the signed conclusion, apply the group Sym(D) times Sym(D-complement)
to an arbitrary real union assignment. Each permutation fixes all the
prescribed old entries, identical transported columns, Boolean/forbidden
values and full-key equalities. Its matrix is a permutation congruence of
the original matrix. Their finite average is therefore PSD whenever the
original matrix is PSD, and retains every prescribed linear equality.
This uses neither a representing measure nor nonnegativity of any free
moment. The invariant free moments can have either sign; their positive
rescaling z can likewise have either sign. Since y^T A=0 exactly, the
contradiction 0=y^T A z<=y^T b<0 applies to all such real z. The source
averaging and linear-certificate implications therefore justify the
stronger conclusion without importing Polak's nonnegative-coordinate
hypothesis into this separate linear averaging operation.

Finally, the audit compares all 14 relevant mathematical fields of the
preserved initial report against the corrected verifier, including the
complete records, mode matrices, inverse actions, bounds, minors, kernel
residuals, separator and pairing. All agree. Its sole failure is exactly
`strict_negative_interval`: [-10^-6,0) already forces a negative value,
although its upper endpoint equals zero. The initial false predicate is
preserved, with no altered mathematical certificate. This review tests
no other column, scalar upper row, other anchor, base/pair prescription,
global moment system or RS boundary claim.

## Mathlib

Full matching constrained four-layer completion obstruction: not checked.
Supporting mixed-layer decomposition, singular Schur complement, Farkas
and rational linear algebra coverage: not checked here. Unknown availability
is not absence. General methods are imported by precise citations above;
this finite specialization makes no source-level novelty claim.
