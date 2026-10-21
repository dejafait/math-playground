# L078 — The immutable distance-eight columns have no joint PSD completion

## Hypotheses

Use n=1024,w=68 and the entire original pair prescription of L021,
with the positive singleton rho of L053. Fix a 68-subset D. The retained
matrix C is exactly L073's included-anchor matrix, divided by rho,
indexed by {D} and all {D,E} with |D\E| in {5,6,7}. Its entire moment
dictionary is L075's, including the original RREF at
(0,v_dagger,w_star), all 28 forced and 36 completed seven/seven entries.
No coefficient is changed. The excluded-anchor matrix is not used as C.

Add every index {D,G} with |D\G|=8. Its column against C must be exactly
L076's active-set (27,33,56,63) column, transported by point bijections.
The anchor entry and diagonal are the original

    p8=16792471/1181138102168120460>0.

Only unrepresented eight/eight unordered moments may be chosen, and they
must be nonnegative. Preserve every represented full atom key, Boolean
repetition and forbidden distinct half-distance 1,...,4. No scalar upper
row, excluded-anchor PSD condition, actual-label restriction, retuning or
global moment extension is imposed.

## Conclusion

There is no such simultaneous included-anchor PSD completion. All 500
relation types and 3000 presentations are consistent. The obstruction
is instead a nonnegative combination of the 81 complete mode inequalities:
27 positive mode weights cancel 44 of the 45 free columns, leave a
positive coefficient on the remaining nonnegative moment (r,q)=(3,6),
and have fixed pairing in

    [-153934054111800,-153934054111799)/10^6 < 0.

Nonnegativity of that one moment is used. Signed completions are not
excluded by this certificate. This finite REPRODUCTION specializes known
tools; it is a new local obstruction, without a source-level novelty claim.
L077's isolated-column PSD conclusion, L067/L071's different obstructions,
and every existing moment value remain intact. No uniform upper bound,
RS safety, unsafe list or change to the 955–957 bracket follows. The
separate critical proof review below retains this fixed obstruction.

## Proof

**Imports and applicability.** Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-simultaneous-eight-shell-fixed-column-completion.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
[DOI 10.1109/TIT.2005.851748](https://doi.org/10.1109/TIT.2005.851748),
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp.5–7. Its complete unequal-layer algebra applies to factors
68,956 and selected layers 0,5,6,7,8. A shell layer l contains mode (a,b)
precisely when max(a,b)<=l; the anchor occurs only in (0,0). Thus all
81 modes 0<=a,b<=8 must be retained. This algebraic theorem needs no
code or representing measure. Its normalization qualifications remain
in foundations/04,09; no complement prefactor is used.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2 and Theorem 2.6. For retained finite real
symmetric C PSD, a block extension is PSD exactly when every cross
column annihilates ker C and the whole new/new generalized Schur remainder
is PSD. Singular C is allowed; diagonal energy tests alone do not suffice.
Here L073 supplies C PSD and L076 supplies each column's compatibility.
Below these ranges are checked again in every complete mode.

For union-moment identifications and constraint-preserving averaging use
Sven C. Polak, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Section 1.1 (1)–(3), Proposition 1.1 and indicator proof,
p.2, and Section 1.2, p.3, with foundations/12's constant-weight
qualification. Here n=1024,d=10,w=68. The rational LP certificate method
is covered by Goemans, *Advanced Algorithms*, Lecture 3, 19 September
2001, Theorems 1 and 3, printed pp.1–2,
[MIT notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf).
Only direct exact inequalities are used below, not a general SDP alternative.
All general results are imported without reproof. None supplies the
prescribed-data verdict, so the finite specialization is necessary.

**Complete entries and reduction.** Write C(n,k)=binomial(n,k), zero
outside 0<=k<=n, and S_l=C(68,l)C(956,l). For shell layers l,m write
E=(D\X) union Y and G=(D\U) union V, with |X|=|Y|=l,
|U|=|V|=m, i=|X intersection U|,j=|Y intersection V|. Their full atom
tuple, with membership bits 4,2,1 for D,E,G, is

    (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

Use its lexicographically least six-permutation tuple as the unordered
key. These nonnegative atoms exhaust every relation type. The 270 old
types and 149 fixed column types remain immutable. Reconstruct L076's
85 free column coordinates as c+A*t from its original affine system,
where t=-(A_I)^(-1)c_I and I=(27,33,56,63). Every original compatibility
equation and nonnegative coordinate passes, and the entire resulting
150-coordinate column agrees with L076. No old RREF or completion is
optimized anew.

For eight/eight put r=8-i,q=8-j. The 36 forced values are

    Y_88(8,8)=p8;
    Y_88(8-r,8-q)=0                     if 1<=r+q<=4;
    Y_88(8-r,8-q)=Y_(r+q,8)(q,r)        if 5<=r+q<=7.

The last formula reanchors at E; its head and tail intersections are
q,r. For r+q>=8 introduce the 45 variables, in lexicographic (r,q) order,

    V_(r,q)=C(8,r)C(60,r)C(8,q)C(948,q)>0,
    Y_88(8-r,8-q)=p8*z_(r,q)/V_(r,q),  z_(r,q)>=0.

Actual 68-element supports and point-by-point atom counts independently
check all 500 types and all 3000 presentations, including reanchorings
outside the selected layer set. Every available immutable lookup agrees;
all fixed signs, Boolean cases, forbidden zeros and repeated full keys
are checked. There are no other free types or additional identifications
among these 45 coordinates. In particular distances alone are not keys.

The permutations fixing D preserve the old dictionary, the transported
fixed columns, every full-key identification, nonnegativity, Boolean cases
and forbidden zeros. Averaging any proposed completion over this finite
group preserves PSD and all imposed constraints and gives an invariant
completion. Thus ruling out invariant coefficients suffices. No labeled
RS restriction is averaged or added.

**Every original mode inequality.** Define

    beta(n,l,m,a,t)=sum_(u=max(a,t))^min(l,m,n-a)
      (-1)^(u-t)C(u,t)C(n-2a,u-a)C(n-a-u,l-u)C(n-a-u,m-u),
    E_(n,a)(r)=sum_(s=0)^r (-1)^s C(a,s)C(8-a,r-s)C(n-8-a,r-s),
    D8_ab=C(68-2a,8-a)C(956-2b,8-b)>0.

Eliminate the positive anchor from the entire matrix. Its source shell
entries, including every rectangle to layer eight, are

    T_lm=sum_(i,j=0)^min(l,m) beta(68,l,m,a,i)beta(956,l,m,b,j)Y_lm(i,j)
          -1_(a=b=0)*p_l*p_m*S_l*S_m.

For each (a,b) let B_ab be the old block on the present layers in
{5,6,7}, and t_ab=(T_l8) its cross vector. Check B_ab PSD and solve
B_ab*x=t_ab exactly; check every residual, including zero-block cases.
Set R_ab=t_ab^T*x/(p8*D8_ab), zero in new-only modes. Independence of
the solution follows from the checked range condition and symmetry.
All 306 old nonempty principal minors are nonnegative. The verifier uses
a largest nonsingular principal subsystem and Cramer's rule, independently
of the constructor's sequential singular elimination. These cover all
36 three-old-layer, 13 two-old-layer, 15 one-old-layer and 17 new-only
modes. None is omitted because its old block is singular or empty.

Put

    F_ab=sum_(r+q<=7) [Y_88(8-r,8-q)/p8]E_(68,a)(r)E_(956,b)(q),
    b_(9a+b)=F_ab-1_(a=b=0)*p8*S8-R_ab,
    A_(9a+b,(r,q))=-E_(68,a)(r)E_(956,b)(q)/V_(r,q).

The source diagonal identity
beta(n,8,8,a,8-r)=C(n-2a,8-a)E_(n,a)(r) gives exactly

    A*z<=b, z>=0.

Each b_i-(Az)_i is the entire new-mode Schur remainder divided by
positive p8*D8_ab. The constant correction retains p8^2*S8^2 before
division. The independent verifier rebuilds A and b directly with beta,
not the constructor's eigen formula, and checks every original row.
The multiplicity (C(68,a)-C(68,a-1))(C(956,b)-C(956,b-1)) is positive;
summing it over the modes of every layer recovers S_l. As a further
check, p8^2+p8*sum_(ab) multiplicity_ab*R_ab/S8 agrees exactly with
L077's full-space isolated-column energy. This trace is a consistency
check, not the joint PSD criterion.

**Coherent normalization check.** For each factor n=68,956, distinguish
an actual eight-set. On layer l use the monic orthogonal polynomials
h_(n,l,a)(i), i=0,...,l, with positive weights C(8,i)C(n-8,l-i)
and squared norms N_(n,l,a). Direct four-region subset counting gives

    T_(n,l,m,k)(i,u)=sum_s C(i,s)C(8-i,u-s)
                    C(l-i,k-s)C(n-8-l+i,m-u-k+s).

Every coordinate of T*h_m,a=gamma_(n,l,m,a,k)*h_l,a is checked, in
both rectangular directions; absent modes have zero action. For nonzero
beta, sigma_lm=N_l*gamma_lm/beta_lm is positive and independent of k;
zero beta gives zero gamma. Check for every present layer pair

    sigma_lm*sigma_88=sigma_l8*sigma_m8,
    sigma_88=N_8/C(n-2a,8-a).

Tensoring these identities establishes one positive diagonal congruence
of each entire source block with its direct weighted action. It does
not merely match squared pairwise normalizations. In the constant mode
the action correction is -p_l*p_m*S_m, agreeing after multiplication by
the layer norm with the complete anchor transport above. Direct weighted
old-block elimination checks every singular range again and recovers
exactly R_ab after division by p8*N_(68,8,a)*N_(956,8,b). This checks the
source reduction's signs and all full-block scaling, without asserting a
pseudoinverse congruence.

**Compact exact separator.** Number rows by 9a+b, and number the 45
lexicographic free coordinates from 0. Let

    I=(1,2,3,4,7,9,10,11,12,14,15,18,19,20,21,22,23,24,
       27,28,29,30,31,32,33,36,37,38,39,40,45,46,47,48,49,
       54,55,56,57,64,72,73),
    J=(-1,0,1,2,3,4,5,6,8,9,10,11,12,13,14,15,16,17,
       18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,
       35,38,39,41,42,43,44).

Define the 42-by-42 matrix M_(i,j)=-1 for j=-1 and A_(i,j)
otherwise, with the indicated row/column orders. Let c_j=-1 for j=-1
and zero otherwise. Solve M^T*y_I=c and put y_i=0 outside I. Rational
Gaussian elimination has 42 nonzero pivots, uniquely specifying y.
The independent verifier reconstructs the same y from these explicit
indices, without the constructor's simplex or basis solver.

Every y_i is nonnegative, precisely 27 are positive, and sum_i y_i=1.
For s_j=sum_i y_i*A_ij, all s_j are nonnegative. Precisely 44 are zero;
the sole positive coordinate is j=7, namely (r,q)=(3,6). Finally the
full exact value v=sum_i y_i*b_i satisfies

    -153934054111800/10^6 <= v < -153934054111799/10^6 < 0.

These statements are exact rational identities/sign comparisons. The full
weights, all original rows, all sums and v are retained in the certificates.
They are reproducible from the finite definitions above; no numerical
solver status establishes any of them. The verifier also computes the
raw-moment coefficients directly as

    -sum_(ab) y_(9a+b)*beta(68,8,8,a,8-r)*beta(956,8,8,b,8-q)
                          /[p8*D8_ab]
      = s_(r,q)*V_(r,q)/p8 >= 0.

Thus the cancellation and the one remaining sign are checked in original
Y coordinates, not only in a scaled LP. It separately reconstructs
the weighted fixed, anchor and required-energy contributions and their
signed sum v.

If a completion existed, its z>=0 and Az<=b would give
0<=sum_j s_j*z_j=y^T*A*z<=y^T*b=v<0, a contradiction. Therefore no
invariant completion exists; the averaging argument rules out any
completion under the stated constraints. Multiplication by rho>0
preserves this obstruction in the original moment normalization.

**Reproducible evidence and qualifications.** From the notebook run

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/simultaneous_eight_shell.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_simultaneous_eight_shell.py

The constructor saves full staged certificates before discovery at
`scripts/finite-support/simultaneous-eight-shell-results.json`. Its Decimal
phase-I calculation proposes a basis only; the entire dual and all signs
and strict inequalities are checked rationally. The independent verifier
imports only the Python standard library, reconstructs actual supports,
the active-set solution, all 3000 presentations, every original beta row,
all 306 old principal minors, all singular ranges, the explicit separator
and original raw coefficients. Its complete evidence is
`scripts/finite-support/simultaneous-eight-shell-verification.json`.
Both complete summaries and empty failure lists were inspected. This
arithmetic verification belongs to the original construction attempt;
the separate critical review is recorded below with its dependency scope.

The final constructor passes 5856 exact checks and the independent
verifier passes 6904, with no failures. The actual minimum mode weight
and column sum are both zero, meeting the required nonnegative bounds;
the complete fixed pairing has the strict negative interval displayed
above, whereas feasibility would require it to be nonnegative. All
306 old-block principal minors and every range residual are consumed.

The working record preserves an initial energy-field lookup KeyError
after the successful consistency stage, before any mathematical verdict.
It was corrected from a nonexistent summary field to the existing full
energy field. No input or mathematical value changed. No failed exact
mathematical check was suppressed. Only this immutable prescription is
rejected; other columns, other base/pair choices, other anchors, global
moments, RS realization and arbitrary-center 67/68 safety remain open.

**Separate critical proof review — step 274, 2026-10-17.** Reuse the
prior SPECIALIZE assessment
`drafts/literature/2026-10-17-simultaneous-eight-obstruction-critical-audit.md`.
This review retains the theorem without changing any mathematical input
or qualification. It establishes an independently reviewed local input,
not a new discovery beyond the sources checked.

The complete proof and both joint-eight programs were checked against
the essential ancestor recipes and foundations/04,09,10,12. The cited
Schrijver decomposition applies to real invariant matrices independently
of code realizability. Selecting layers 0,5,6,7,8 leaves exactly the 81
stated modes: neither factor's upper index restriction removes one of
these layers. The anchor occurs only at (0,0). Sano's theorem includes
every singular case. The averaging group fixes D, permutes its 68 points
and its 956-point complement separately, and preserves the entire
immutable prescription and each represented union key. Averaging a
putative completion therefore preserves precisely the constraints used
in the contradiction. No actual-label condition is transported.

Reconstruct all original pair equations of L021, including the factor
two in p_h, and the exact positive rho of L053. Recover the exact
(0,v_dagger,w_star) parameters and all 49 column coordinates from the
original RREF, checking every original compatibility equation. A fresh
reverse-variable forward elimination and back substitution reconstructs
L073's 36-coordinate solution from its 35 defining mode rows and e_28.
Rebuild all 28 forced entries and compare every one of the 270 old
values to L075. These calculations import the reviewed uniqueness and
source-system contracts; they do not claim fresh recursive audits of
all ancestor theorems. The included-anchor base is independently checked
again by all 306 source principal minors in the rerun verifier.

Reconstruct L076's active-set solution in a different variable order,
retaining all 85 coordinates and precisely its four zeros. All 150
column values agree, including p8 at the anchor. Using the actual orbit
weights, all 90 original weighted kernel residuals vanish. The full-space
exhaustion is L076's reviewed input; its invariant rank is not mistaken
for a full-space rank. Every atom permutation in all 500 types/3000
presentations is reconstructed, and the independent verifier recounts
them on actual supports. Full unordered keys and the source equality
classes (sorted distance triple,i-j) agree. The 36 forced eight/eight
entries match their Boolean/forbidden/reanchored formulas, and the 45
free keys are distinct. This checks the entire dictionary, rather than
only distances or one anchor presentation.

For an independent normalization test, recover each monic polynomial
basis from its weighted moment equations. All lower-degree inner
products vanish and every squared norm is positive. Fix actual sets U,X
with |U|=8, |X|=l, |U intersection X|=i. Enumerate all subsets Z of
U union X, retaining their cardinality and their intersections with U
and X. For each target layer m, completion outside this union contributes
C(n-|U union X|,m-|Z|). This reconstructs all 220 factor transition
matrices on layers 5,6,7,8, in both directions, independently of the
four-binomial formula used by the constructor. Every row total and every
coordinate of every saved action agrees; absent-mode actions vanish.

Read each action coefficient at a nonzero basis coordinate and check
the full vector identity. All signed beta ratios are positive and
relation-independent; zero beta has zero action. Every reference-eight
triangle identity holds. Tensoring the ratios gives, for each entire
weighted block,

    K_lm=(N8/D8)*s_l*T_lm*s_m,  s8=1, s_l>0,

where s_l is the product of the two sigma_l8 ratios divided by N8/D8.
All old entries and cross entries satisfy this single congruence.
The direct eight/eight action also reproduces every original affine row.
The constant mode includes -p_l*p_m*S_m before multiplication by its
row norm, giving exactly the complete anchor correction in the source
block. This checks the full matrix congruence, not a pseudoinverse
transformation or unrelated pairwise squared scales.

Eliminate the old weighted layers in reverse order. Each pivot is
nonnegative; at every zero pivot both the remaining old row and cross
coordinate vanish. Among the 36 three-old-layer modes, ranks 0,1,2,3
occur 19,8,4,5 times. Among 13 two-old-layer modes, ranks 0,1,2 occur
3,3,7 times. Among 15 one-old-layer modes, ranks 0,1 occur 4,11 times.
All 17 new-only modes are retained with zero old cost. Every direct
cost divided by p8*N8 agrees with the source cost divided by p8*D8
and the independent principal-subsystem inverse. All 81 original rows
and bounds agree. The full multiplicity-weighted trace, including the
positive p8^2 term, agrees with L077. This last identity is a consistency
check only; the joint obstruction uses the full mode system.

Read I and J directly from this manuscript. Reverse-variable forward
elimination reconstructs the unique 42-by-42 dual solution with 42
nonzero pivots, independently of the constructor's proposal and the
verifier's Gauss–Jordan solve. All 81 weights agree, sum to one, and
have exactly 27 positive entries. Every one of the 45 scaled and raw
coefficients is reconstructed from the original beta expressions; 44
vanish and only (3,6) is positive. The full weighted fixed, anchor and
range-energy terms reproduce v, with exact integer/rational comparisons
proving the displayed strict negative interval. Thus the required
nonnegative lower bound contradicts v<0 in original moment coordinates.
The sign of Y_88(5,2), corresponding to (r,q)=(3,6), is essential.
No claim about signed completions follows. Goemans's nonnegative-variable
form, or simply the displayed verified inequality chain, suffices;
free-variable cancellation is not asserted.

Run from the notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_simultaneous_eight_shell.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/critical_audit_simultaneous_eight_shell.py

The verifier rerun passes all 6904 checks. The dedicated audit passes
11248 additional exact checks with no failures. Full evidence is in
`scripts/finite-support/simultaneous-eight-shell-critical-audit.json`:
immutable input hashes, reconstructed columns/completion, all atom orders,
complete direct transitions/actions, coherent scales, every reverse
singular elimination, original rows, all dual weights, scaled/raw sums,
pairing contributions and exact interval gaps. Programs consume the full
load-bearing arrays; full summaries and empty failure lists were inspected
with the shared JSON inspector. No mathematical correction was needed.

ATTEMPTS/060 remains a stop on this immutable nonnegative joint
prescription only. L077's isolated-column pass and L067/L071's different
obstructions are retained. Other columns, base/pair choices, anchors,
global moments, RS realization and the 955–957 boundary remain unresolved.

## Mathlib

Full matching finite prescribed-column obstruction: not checked. Full
mixed-layer decomposition, constrained union-moment completion, singular
generalized-Schur criterion and Farkas support: not checked. Supporting
PSD, binomial and rational-elimination coverage: not checked. Unknown
coverage is not evidence of absence. General source theorems are imported;
the new local finite verdict carries no source-level novelty claim.
