# L073 — L072's exact maximizer admits a simultaneous seven-shell completion

## Hypotheses

Use the complete anchored five/six-shell PSD base of L061 and the unchanged
moment dictionary of L062 on the 68-subsets of a 1024-point ground set.
Keep the original pairs through p13 and singleton normalization of L069:

    rho=(binomial(1024,64)/binomial(68,64)+1)/(2 binomial(1024,68))>0,
    p5=1/68881143660, p6=133/9357995374380,
    p7=3539/248922676958508>0.

Fix one 68-subset D. At each seven-neighbor G of D, use exactly L065's
49-coordinate affine column f=c+u*a^27+v*a^33+w*a^42 at L072's rational
maximizer u=0,v=v_dagger,w=w_star. Here w_star is L068's exact zero-square
point and v_dagger is L072's beta_v/alpha, not a rounded approximation.
The anchor and diagonal are p7 after division by rho. All prescribed old
entries, original RREF, Boolean repetitions, forbidden half-distances
1,...,4, unordered identifications and whole-base kernel conditions remain
unchanged. Retain L069/L072's column scalar conditions and old scalar rows.

Consider exactly the included-anchor matrix indexed by {D} and all pairs
{D,E} with |D\E| in {5,6,7}. Its remaining 36 seven/seven coefficients
must be nonnegative. No seven/seven scalar upper rows, other-anchor or
excluded-anchor matrices, labeled restrictions or global moments are
required by these hypotheses.

## Conclusion

There is an exact rational assignment of the 36 remaining coefficients
that makes this whole matrix PSD and preserves every prescribed entry
and unordered identification. In the original positive-valency-scaled
coordinates z_(r,q), r+q>=7, exactly z_(7,0) is zero and the other 35 are
positive. All 64 original Schur inequalities hold: 23 have positive slack
and 41 have zero slack. These are product-mode counts, not full-space
multiplicities. All 3708 inherited ordinary scalar rows also hold.

This is a finite REPRODUCTION/specialization of assessed methods, with a
new local feasibility verdict and no source-level novelty claim. It parks
this included-anchor matrix as an exclusion diagnostic at this point.
It supplies no full SDP feasibility, support/list bound, representing
measure or RS realization. Other points, untested seven/seven scalar
upper rows and other matrices remain unresolved. Arbitrary-center safety
at 67/68 agreements and the 955–957 bracket do not change. Separate
critical proof review below retains this finite result.

## Proof

**Imported tools and applicability.** Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-16-maximizer-simultaneous-seven-shell-completion.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
[DOI 10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. The factor sizes 68,956 and layers 0,5,6,7 meet its index
ranges. Use L067's audited coherent symmetric mixed-layer congruence;
do not replace it by unrelated rectangular normalizations. Restriction to
these layers gives all 64 modes below, including singular and new-only
modes. No representing measure is needed for this matrix decomposition.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2 and Theorem 2.6. For a finite real symmetric
matrix [B,t;t^T,a] with B PSD, PSD is equivalent to t annihilating ker B
and a-t^T B^dagger t>=0. Singular B is allowed. Eliminate the positive
anchor from the entire matrix before computing this energy. Neither a
numerical inverse nor a strict-feasibility hypothesis is used.

For union moments use Sven C. Polak,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and its indicator proof, p.2,
Section 1.2, p.3, with foundations/12's constant-weight qualification.
Here n=1024,d=10,w=68. The assignment below directly uses ordinary
unlabeled relation types; it does not average an actual-label constraint.
The finite rational LP/basis method is covered by MIT 6.854's 2020
[LP notes](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
“Linear Equalities” and “Basic Feasible Solutions”, as recorded in
foundations/10. Only a checked rational feasible point is needed here;
no LP duality or numerical optimizer status supplies the conclusion.
These general inputs are imported without reproof. None supplies this
finite assignment, which is why the specialization is necessary.

**Exact entries and complete system.** Put C(n,k)=binomial(n,k), zero
outside 0<=k<=n. For layer-l and layer-m supports write
E=(D\X) union Y, G=(D\U) union V, with |X|=|Y|=l, |U|=|V|=m,
i=|X intersection U|,j=|Y intersection V|. The complete atom tuple is

    (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

Let Y_(l,m,i,j) be the moment divided by rho. For l,m in {5,6}, use
exactly L062. For l in {5,6},m=7, use L065 at the stated maximizer.
For seven/seven put r=7-i,q=7-j. All 28 forced entries are

    Y_(7,7,7,7)=p7;
    Y_(7,7,7-r,7-q)=0                  if 1<=r+q<=4;
    Y_(7,7,7-r,7-q)=Y_(r+q,7,q,r)     if r+q=5 or 6.

For r+q>=7 set

    V_(r,q)=C(7,r)C(61,r)C(7,q)C(949,q)>0,
    Y_(7,7,7-r,7-q)=p7*z_(r,q)/V_(r,q).

Order these 36 variables lexicographically in (r,q), starting with
(0,7) at index 0. Thus index 28 is (7,0). Set

    beta(n,l,m,a,t)=sum_(u=max(a,t))^min(l,m,n-a)
      (-1)^(u-t) C(u,t) C(n-2a,u-a) C(n-a-u,l-u) C(n-a-u,m-u),
    E_(n,a)(r)=sum_(s=0)^r (-1)^s C(a,s) C(7-a,r-s) C(n-7-a,r-s),
    S_l=C(68,l)C(956,l), D7_ab=C(68-2a,7-a)C(956-2b,7-b)>0.

For a,b in {0,...,7}, a layer l is present iff max(a,b)<=l. After
eliminating the anchor, its symmetric source entries are

    C_lm=sum_(i,j=0)^min(l,m)
      beta(68,l,m,a,i) beta(956,l,m,b,j) Y_(l,m,i,j)
      -1_(a=b=0)*p_l*p_m*S_l*S_m.

Let B_ab be the present old block (layers 5 and/or 6), and t_ab its
cross vector C_l7. Define R_ab=t_ab^T B_ab^dagger t_ab/(p7*D7_ab),
zero in new-only modes. The old block is PSD, and every singular range
condition holds at this exact point. In particular these conditions
are checked anew below, not inherited from the origin's numerical data.

Define the complete rational 64-by-36 matrix A and bound b by

    A_(8a+b,(r,q))=-E_(68,a)(r)E_(956,b)(q)/V_(r,q),
    F_ab=sum_(r+q<=6) [Y_(7,7,7-r,7-q)/p7] E_(68,a)(r)E_(956,b)(q),
    b_(8a+b)=F_ab-1_(a=b=0)*p7*S7-R_ab.

The required inequalities are exactly Az<=b and z>=0. The source beta
identity beta(n,7,7,a,7-r)=C(n-2a,7-a)E_(n,a)(r) is checked for every
coefficient. Hence b_i-(Az)_i equals
(C_77-t_ab^T B_ab^dagger t_ab)/(p7*D7_ab), with the complete anchor
correction p7^2*S7^2 included. These positive denominators preserve signs.

**Compact exact definition of the assignment.** The following defines
the rational vector without displaying thousands of digits. Form a square
36-by-36 matrix M_def whose first 35 rows are the rows A_i, in this order:

    0,1,2,3,4,5,8,9,10,11,12,13,14,16,17,18,19,20,22,
    24,25,26,27,28,29,32,33,34,35,40,41,42,48,49,56.

The last row is the unit row e_28. Let b_def have the corresponding
35 b_i followed by zero. Define z=M_def^(-1)b_def. Every entry is
specified by the preceding finite sums, the original L065 RREF and
L072's exact parameters. The full rational vector is also saved as
`certificate.z` in `scripts/finite-support/maximizer-completion-results.json`.

Exact rational elimination finds 36 nonzero pivots for M_def. Independent
full Gauss–Jordan elimination reconstructs the same z from these original
rows, without the constructor's equality reduction or proposed basis.
It checks all 36 defining equations, all 36 signs and all 64 original
inequalities. The exact zero coordinates are {28}; the exact zero-slack
mode indices are

    0,1,2,3,4,5,8,9,10,11,12,13,14,16,17,18,19,20,22,
    24,25,26,27,28,29,32,33,34,35,40,41,42,43,
    48,49,50,51,56,57,58,59.

Every other variable and slack is strictly positive. Thus the minimum
mode slack is exactly zero, as required, rather than a numerical negative
tolerance. All saved fractions have positive denominators, and all sign
decisions use integer comparisons. Full values of every coordinate,
original row, right side, slack and elimination pivot are retained in
the certificates. This finite certificate is reproducible by the exact
algorithms below; a preview is not used as a substitute for checking it.

**Verification of consistency, ranges and PSD.** The independent verifier
recovers f from L065's original augmented RREF at (0,v_dagger,w_star),
substitutes it in every original compatibility equation and checks all
49 weighted whole-base kernel residuals with the anchor and actual
86 orbit weights. It builds all 270 types from actual 68-element supports
and computes all 1620 presentations point by point. Each prescribed
lookup agrees, including Boolean/forbidden cases; full unordered keys
have unique values. Presentations outside the retained layer set provide
no additional prescribed lookup. All fixed values agree with the
specified base and column. The 2178 old and 1530 column scalar rows are
checked at this same assignment; no seven/seven upper row is included.

For each old two-layer block B=[[x,y],[y,z]] and cross (t,s), the
independent verifier checks x,z,xz-y^2>=0. If xz-y^2>0 its energy is
(z*t^2-2y*t*s+x*s^2)/(xz-y^2). If singular with x>0, it checks
x*s-y*t=0 and uses t^2/x; if x=0,z>0 it checks t=0 and uses s^2/z;
if B=0 it checks the whole cross is zero. One-layer zero blocks likewise
require zero cross, and new-only modes have zero old energy. These cover
all 64 modes. The constructor instead uses sequential positive-pivot
range elimination, providing an independent energy calculation.

The verifier reconstructs every coefficient directly from the beta sums,
and computes the actual C_77 from all 64 seven/seven entries, subtracting
the full anchor term before comparing with the energy. This independently
recovers each original b_i-(Az)_i. It also checks every principal minor
of each complete anchor-eliminated source block on the present layers:
306 minors in total, all nonnegative. Thus no singular branch is passed
solely from a scalar Schur calculation. By the imported mixed-layer
decomposition these PSD blocks exhaust the entire anchor-eliminated
matrix. Restoring the positive anchor by congruence and multiplying by
rho>0 proves PSD of the required original matrix. Nonnegativity follows
from every checked fixed entry, p7>0, V_(r,q)>0 and z>=0. The checked
full-key identifications give the required single value for every
represented unordered triple. This proves precisely the conclusion.

**Discovery and reproducible evidence.** From the notebook run

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/maximizer_completion.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_maximizer_completion.py

The constructor passes 2911 exact checks; its complete certificate is
`scripts/finite-support/maximizer-completion-results.json`. It verifies
the old coefficient-only row transform before reusing it, recomputes the
new 24 right sides, checks consistency and constructs a fresh rank-23
particular solution. L067's zero dual forces these 24 mode equalities.
The remaining 40 modes and 36 signs give a 13-coordinate rational LP.
A 71-pivot Decimal phase-I run only proposes a basis; exact reconstruction
checks the resulting point against every original row and sign. L070's
origin particular solution is never reused. This reduction is a discovery
aid; the separate original-row definition above removes it from the
certificate's mathematical requirements.

The independent standard-library-only verifier imports no notebook code
or optimizer and uses no floating arithmetic. It passes 4793 checks;
the complete evidence is
`scripts/finite-support/maximizer-completion-verification.json`. It reads
all relevant arrays, rebuilds the entries and complete original system,
independently solves M_def, and verifies all 306 principal minors. Both
full summaries and empty failure lists were inspected. Large integers
require `PYTHONINTMAXSTRDIGITS=0` when inspecting these certificates with
the shared JSON inspector; the mathematical scripts already disable the
integer-string limit. No failed mathematical verdict is suppressed.

The independent verifier is arithmetic validation within this research
attempt, not the later dedicated critical proof review. No claim of full
SDP feasibility, measure, packing or common-center list follows. In
particular L067's old-column obstruction and L071's origin obstruction
remain valid: the present column is L072's different maximizer.

**Separate critical proof review — step 254, 2026-10-16.** Reuse exactly
`drafts/literature/2026-10-16-maximizer-completion-critical-audit.md`, saved
as SPECIALIZE before this invocation. The review retains the theorem
without changing its hypotheses, point, coefficients or scope. This is
verification of a local reproduction, not a claim of source-level novelty.

The complete manuscript, its direct input recipes and the precise source
qualifications in foundations/04,09,10,12 were checked. In particular the
source decomposition is an algebraic statement about this invariant
matrix; it needs neither a measure nor actual-label averaging. Its layer
ranges give 36 three-layer, 13 two-layer and 15 new-only blocks. The
positive multiplicity sums recover S5,S6,S7. Layer zero is the single
positive anchor with entry 1 after dividing by rho. Eliminating it changes
every shell pair by -p_l*p_m*J, including both rectangles to layer seven.
Its source constant-mode correction is exactly -p_l*p_m*S_l*S_m.
Thus restoration is one invertible congruence of the entire matrix.

Read the 35 defining mode indices directly from this manuscript and add
the stated e_28 row. Fresh rational forward elimination in reverse
variable order, followed by back substitution, gives 36 nonzero pivots
and exactly the saved z. This is independent of both the constructor's
reduced LP and the verifier's forward-order Gauss–Jordan solve. Every
original row and bound is independently reconstructed, all 36 signs
are checked, and the exact zero-slack indices are read from the manuscript
and matched. There are 35 strictly positive variables and the sole zero
at (7,0); there are 23 positive mode slacks and 41 zeros. The actual
minimum slack and required lower bound are both exactly zero.

Recover the column from L065's original RREF at L072's exact point.
All original equations pass. Independently recover the 86 orbit weights
as 1 for the anchor and C(7,i)C(61,l-i)C(7,j)C(949,l-j) for shell orbits.
All 49 complete weighted kernel residuals vanish. L065's proved exhaustion
and finite stabilizer-averaging argument give the full-space interpretation;
the quotient dimension alone is not used as a full-space kernel claim.
The 28 forced seven/seven entries are rebuilt before solving for the
remaining entries. No previous origin assignment or rounded parameter is
substituted. Every original pair through p13 and rho is unchanged.

For a separate normalization check, use L067's audited monic bases on
intersection orbits. Recompute their positive weighted norms and all
orthogonality relations, then reconstruct all 118 subset-transition
matrices from the four-region counting formula in L067. Check every
coordinate of their actions, in both rectangular directions, including
vanishing actions on absent modes. For each factor let gamma_lm be its
action coefficient and N_l its basis norm. The exact checks give

    N_l*gamma_lm = N_m*gamma_ml,
    gamma_lm*gamma_ml = beta_lm^2/(D_l*D_m).

For every nonzero beta the ratio gamma_lm/beta_lm is positive and
independent of the relation index. With sigma_lm=N_l*gamma_lm/beta_lm,
check sigma_lm*sigma_77=sigma_l7*sigma_m7 for every present layer pair.
These signed triangle identities establish one coherent congruence,
not merely pairwise squared normalizations. Tensoring the factors gives

    K_lm=(N7/D7)*s_l*C_lm*s_m,  s7=1,  s_l>0,

for the complete weighted block. All old entries and both cross
directions agree, and the completed seven/seven entry is checked directly
from the subset actions. In the constant action the correction is
-p_l*p_m*S_m before multiplying by N_l, agreeing with the full anchor
elimination above. This is a congruence of the whole block, not a claimed
congruence identity for a pseudoinverse.

Eliminate the weighted old layers in order six then five. Every pivot
is nonnegative. At a zero pivot the remaining old row and cross residual
are exactly zero. Among the 36 two-old-layer modes the ranks 2,1,0 occur
9,8,19 times; among 13 one-old-layer modes ranks 1,0 occur 10,3 times;
the 15 new-only modes have zero cost. Every resulting cost divided by
p7*N7 agrees with the source energy divided by p7*D7. All 64 completed
weighted Schur remainders agree with the original rational slacks.
Independently reconstruct every entire source block and all 306 principal
minors; they agree entrywise with the verifier and are nonnegative.
The imported complete decomposition and singular-Schur criterion therefore
justify exactly the claimed original matrix PSD, including all singular
cases and restoration of the positive anchor and rho.

The audit consumes the complete certificate arrays. It independently
permutes all eight atoms on all 270 relation types and compares all 1620
presentations, fixed entries, Boolean cases, forbidden zeros and full-key
identifications. Grouping by the sorted distance triple and t-s gives
the same full keys. As t+s=a+b-h, these data uniquely determine t,s
and all atoms for each ordered distance triple, so no source equality
is omitted. All 3708 inherited scalar slacks are recomputed on the same
assignment; their minimum is zero. This checks precisely the old and
column rows. No seven/seven upper row is silently included or claimed.

Run from the notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_maximizer_completion.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_maximizer_completion.py

The verifier rerun passes all 4793 checks. The separate audit passes
8109 additional exact checks. Its full input hashes, reverse-order basis
pivots, witness, presentations, scalar slacks, direct actions, coherent
scales, singular ranges and complete PSD blocks/minors are saved in
`scripts/finite-support/maximizer-completion-critical-audit.json`.
The full summary and empty failure list were inspected. The initial
report is preserved at
`scripts/finite-support/maximizer-completion-critical-audit-initial.json`:
its sole failure was an audit serialization tag, `nonnegative` instead
of the constructor's `sign`, for the same e_28 row. Correcting the tag
changes no equation or mathematical value; the final audit checks all
initial/final mathematical arrays for exact equality. No mathematical
failure is concealed or repaired by changing the target.

Only the included-anchor exclusion diagnostic in ATTEMPTS/055 is parked.
L067's immutable-column and L071's origin obstructions remain intact.
Seven/seven scalar upper rows, excluded/other anchors, compatible global
moments, representing measures and RS realization are independent gaps.
The 955–957 bracket and arbitrary-center 67/68 safety remain unchanged.

## Mathlib

Full matching coverage of the mixed-layer source decomposition, singular
Schur criterion, rational LP/basis machinery and this finite instance was
not checked. Unknown coverage is not evidence of absence. The proof here
uses the precisely cited informal inputs and complete rational certificates;
no Lean verification is claimed.
