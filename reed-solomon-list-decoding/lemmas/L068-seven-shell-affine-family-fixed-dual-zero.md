# L068 — The fixed seven-shell dual attains zero on the compatible family

## Hypotheses

Retain the entire normalized anchored five/six-shell matrix of L061 and
every L062 moment, on all 68-subsets of a 1024-point set. The singleton
normalization rho is the original strictly positive one. Keep all original
pairs, in particular p5=1/68881143660, p6=133/9357995374380 and
p7=3539/248922676958508. Fix a 68-subset D.

At every seven-neighbor G of D, prescribe the same L065 affine column,
with its original coordinate ordering and

  f_j=c_j+u*a^27_j+v*a^33_j+w*a^42_j,  j=0,...,48.

A free normalized moment is p7*f_j; all fixed coordinates, including
the anchor p7, remain unchanged. Impose nonnegativity of every column
entry, Boolean repetitions, forbidden half-distances 1,...,4, and every
equality between complete unordered support triples. Do not add new
scalar upper rows or retune the base or pairs. Consider exactly L067's
unchanged 24 nonzero dual weights on its 64 necessary inequalities (1).

## Conclusion

The maximum of this dual's weighted right side over the stated family
is exactly zero, and is attained by an explicitly specified rational
column with u=v=0. Of the 49 free entries, 47 are strictly positive
and precisely f_27=f_33=0. All fixed entries are nonnegative.

Consequently L067's dual is not strictly obstructing throughout this
family. This does not contradict its strict obstruction at the immutable
L065/L066 point. It proves neither a simultaneous PSD extension nor its
impossibility at the new point. Other duals, base/pairs, global moments,
labels, measures, packings and RS realization remain open; arbitrary-center
safety at 67/68 agreements and the 955–957 bracket are unchanged.
This is a finite REPRODUCTION/specialization of assessed methods, with
no novelty claim. The separate critical proof review below retains this
conclusion and its precise scope.

## Proof

**Imports and why the specialization is necessary.** Reuse the prior
SPECIALIZE assessment
`drafts/literature/2026-10-15-seven-shell-affine-family-fixed-dual.md`.
The unchanged mixed-layer decomposition and dual inequalities are L067's
specialization of Alexander Schrijver, *New code upper bounds from the
Terwilliger algebra and semidefinite programming*, IEEE TIT 51 (2005),
2859–2866, DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64),
printed pp. 5–7. Factor sizes 68,956 and layers 0,5,6,7 remain in its
range. Changing coefficients does not change the source decomposition
or its coherent positive congruence, verified in L067.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, version of record 27 February 2026,
[DOI 10.1007/s44146-026-00231-y](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Section 2, Corollary 2.2, Theorem 2.6 and Lemma 2.7: for a retained PSD
block B, the entire cross block must annihilate ker B, and the remaining
block minus the inverse-on-range energy must be PSD. Singular B is allowed.
No pseudoinverse is transported without the full anchor congruence.

Equal-union moments and ordinary constraint-preserving averaging are
Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
IEEE TIT 65 (2019), 28–38,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Section 1.1
(1)–(3), Proposition 1.1 and proof, p. 2, and Section 1.2, p. 3.
Use the proof's constant-weight conclusion with n=1024,d=10,w=68,
retaining the display qualification in foundations/12. Only the ordinary
slice is used; there is no actual-label averaging or representing measure.

For convex quadratic optimization, import Boyd–Vandenberghe (with
Parth Nobel), *Convex Optimization*, revised 402-page
[author slides](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf),
retrieved 15 October 2026, PDF pp. 53–54,97–98,105,174–175
(slides 5.19–5.20 for sufficient KKT conditions), as recorded in
foundations/10. A verified PSD quadratic Hessian and stationary feasible
point certify a global minimum, permitting singular Hessians and boundary
points. No Slater converse is invoked. The exact square identity below
also provides the global bound directly. These general results are
imported, not reproved. None of the checked sources computes this
prescribed family's coefficients or sign; that is the specialization.

**The entire admissible parameter domain.** For l<=m in {5,6,7} write
E=(D\X) union Y, G=(D\U) union V with |X|=|Y|=l, |U|=|V|=m,
i=|X intersection U|, j=|Y intersection V|. The eight atoms, in mask
order 0,...,7 with D,E,G bits 4,2,1, are

  (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

All 270 types and six presentations per type are retained. The 121 old
types use L062. The 36 five/seven and 49 six/seven types use L065's
affine column, with its fixed/forbidden entries. At seven/seven put
r=7-i,q=7-j,h=r+q. Boolean repetition gives Y77(7,7)=p7;
1<=h<=4 gives zero; h=5,6 gives Y77(7-r,7-q)=Y_(h,7,q,r).
For h>=7 the remaining 36 moments are free, as in L067.

Use a four-vector for an affine expression in (1,u,v,w). For every
presentation, perform the Boolean/forbidden lookup first and otherwise
look up its original complete unordered atom key. Subtract the resulting
four-vectors for every shared key. Every such difference is identically
zero. Thus there are no additional affine equalities restricting (u,v,w).
Every fixed column coordinate is nonnegative, and each free entry has
positive factor p7. The exact parameter domain for this target is hence

  P={ (u,v,w) in R^3 : c_j+u*a^27_j+v*a^33_j+w*a^42_j>=0
                         for every j=0,...,48 }.

These are all 49 inequalities, not only the three active at L065's
original witness. Forced seven/seven entries are either column entries,
Boolean p7 or zero, so add no new nonnegativity requirement. The 36
remaining entries can be nonnegative independently before imposing PSD.
No unassessed scalar upper row is inserted.

The complete equality computation is saved and independently reconstructed
from actual subsets, not from a distance-only dictionary. For this
reconstruction take D={0,...,67}, U={0,...,m-1},
X={0,...,i-1} union {m,...,m+l-i-1},
V={68,...,68+m-1}, and
Y={68,...,68+j-1} union {68+m,...,68+m+l-j-1}.
These realize every stated type. Count all 1024 points in every support
order; this gives precisely its six atom presentations. All complete
keys, affine values and shared-key equalities agree. All orbit ranges
are nonempty. L065's original kernel equations are also checked in all
four affine coefficients; thus every column in this family has the
entire retained-base range compatibility, not just its selected point.

**The exact quadratic being tested.** Use L067's beta formula, its
S_l=binomial(68,l)binomial(956,l), and, for each a,b in {0,...,7},
D_l=binomial(68-2a,l-a)binomial(956-2b,l-b). All present D_l are
positive. Retain exactly the L067 source block

  C_lm=sum_(i,j) beta(68,l,m,a,i) beta(956,l,m,b,j) Y_(l,m,i,j)
        -1_(a=b=0) p_l p_m S_l S_m.

Let B_ab be its fixed old-layer block and let t_ab be the affine vector
of C_l7, l=5 and/or 6 when those layers occur. The anchor correction is
included before this operation, with the original positive p7.

For every singular old block its range equations hold as affine
identities, coefficient by coefficient. Explicitly for
B=[[x,y],[y,z]], det B=0 and x>0 require x*t6-y*t5=0;
if x=0,z>0 require t5=0 (and y=0); if B=0 require both entries zero.
The one-layer zero case requires its whole affine cross entry zero.
All 64 modes, including the 15 new-only modes, are checked. Old blocks
are unchanged PSD by L061. L067's coherent normalization applies to
these variable cross entries without modification.

Let K_ab be the symmetric four-by-four matrix representing

  R_ab=t_ab^T B_ab^dagger t_ab/(p7*D7).

It is uniquely specified by these exact rules: a positive old scalar x
contributes outer(t)/x; a positive determinant two-layer block contributes
(z outer(t5)-y(t5*t6^T+t6*t5^T)+x outer(t6))/(xz-y²).
In the singular cases just described use outer(t5)/x if x>0,
otherwise outer(t6)/z if z>0, otherwise zero. Divide by p7*D7.
Here each t is its four-vector of affine coefficients. These operations
are on fixed inverse-on-range blocks, not an unweighted quotient inverse.

Define F_ab and A_ab exactly as L067:

  F_ab=sum_(r+q<=6) (Y77(7-r,7-q)/p7) E_(68,a)(r) E_(956,b)(q),
  A_ab=1_(a=b=0) p7*S7.

Use L067's explicit h,k and lambda_ab=h_a*k_b, without changing any
of the 24 positive weights. Let L be the four-vector for
sum lambda_ab*(F_ab-A_ab). Set a symmetric four-by-four matrix M by
starting with -sum lambda_ab*K_ab, adding L0 to M00 and adding Lj/2
to M0j and Mj0 for j=1,2,3. This is an exact finite rational definition
of every coefficient, using the original L065 RREF specification of
c,a^27,a^33,a^42. For z=(1,u,v,w) the tested objective is precisely

  Phi(u,v,w)=z^T M z=sum lambda_ab*(F_ab-A_ab-R_ab).

Every one of the 36 coefficients of the remaining seven/seven moments
still cancels: they depend only on the unchanged weights and eigenvalues,
not on (u,v,w). Thus Phi is the very same dual weighted right side,
with the columns allowed to vary. No new dual has been optimized.

**Exact coefficient identities and an attained zero.** Complete rational
evaluation of the preceding definitions gives

  M_ij=0 whenever i or j belongs to {1,2};
  alpha=-M33>0, beta=M03, and alpha*M00+beta²=0.

These specify the rational numbers alpha,beta without an unspecified
solver choice. Put w_star=beta/alpha. The full exact fractions, including
all 16 entries of M, are in both certificates below. The identities give

  Phi(u,v,w)=-alpha*(w-w_star)²<=0

on all R^3, so in particular on P. Equivalently -Phi has a PSD rank-one
Hessian and zero gradient at w_star; the two free null directions have
zero linear term. No compactness, attainment theorem, invertible Hessian,
or interiority assumption is used.

Now set u=v=0,w=w_star. Direct exact substitution in all 49 expressions
c_j+w_star*a^42_j yields f_27=f_33=0 and f_j>0 for every other j.
All fixed coordinates remain nonnegative, all old moments are unchanged,
all unordered equalities hold, and every weighted original kernel
residual is zero. Therefore this is an actual admissible point of P,
and Phi(0,0,w_star)=0 exactly. This proves the asserted attained maximum,
rather than inferring anything from an unattained zero supremum.

As a scope check, substitution at the old u=v=0,w=-c4/a^42_4 reproduces
L067's exact negative value in [-53503520/10^6,-53503519/10^6).
The new admissible point therefore changes the strict-sign verdict for
the whole family while preserving that immutable obstruction.

**Complete arithmetic evidence and qualifications.** From the notebook run

  `PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/seven_shell_affine_fixed_dual.py`

The constructor passes all 2077 checks without failures. Complete evidence
is `scripts/finite-support/seven-shell-affine-fixed-dual-results.json`:
immutable input hashes, all 270 types/1620 presentations, every affine
equality and nonnegativity row, all 64 old blocks, affine cross vectors,
range residuals and energy quadratics, the unchanged dual and all 36
cancellations, M, its exact square certificate and the entire witness.

Independently run

  `PYTHONDONTWRITEBYTECODE=1 python3 scripts/finite-support/verify_seven_shell_affine_fixed_dual.py`.

This imports no notebook code, optimizer or floating arithmetic. It
reconstructs all actual subsets/presentations and all original affine
kernel equations. It recomputes all old source blocks, affine cross
entries, every determinant-case range identity, and the source/Johnson
normalization at every mode. The costs use the determinant formulas
above, independently of the constructor's sequential Schur elimination.
Since the objective is a quadratic, evaluation at 0, plus/minus each
coordinate vector, and each sum of two distinct coordinate vectors
determines all ten coefficients exactly: diagonals are
(Phi(e_i)+Phi(-e_i))/2-Phi(0), the homogeneous linear matrix entries
are (Phi(e_i)-Phi(-e_i))/4, and mixed entries are
(Phi(e_i+e_j)-Phi(e_i)-Phi(e_j)+Phi(0))/2. These reproduce all of M.
It then checks the displayed perfect-square identities, every sign of
the complete rational witness, all 49 original weighted kernel residuals,
all 64 original right sides at that point and their exact weighted zero.
The full 64 right sides are saved; no individual-row feasibility claim
is inferred from their weighted sum. All 7315 checks pass, with no failures.
Complete independent evidence is
`scripts/finite-support/seven-shell-affine-fixed-dual-verification.json`.
Both scripts consume complete relevant arrays. Full summaries and failure
lists, and the exact zero value, were inspected; bounded previews were
not used as proof.

An initial constructor curvature check wrongly stopped at a leading zero
diagonal although a later positive diagonal remained. Its failed report
is preserved as
`scripts/finite-support/seven-shell-affine-fixed-dual-initial.json`.
The corrected positive-pivot square decomposition removes exactly the
positive rank-one form and leaves the zero matrix. No mathematical
coefficient or input changed. An initial verifier stopped at a mistaken
`kernel` field name before writing a report; using the existing
`kernel_basis` field completed every original residual check. Neither
initial failure is hidden or used as mathematical evidence.

The value zero makes this single weighted inequality inconclusive at
the new point. It says nothing about satisfaction of the remaining
individual PSD inequalities, omitted scalar constraints, a simultaneous
completion, other duals or full SDP feasibility. No support cap,
actual list, unsafe-radius witness or main-target candidate follows.

**Separate critical proof review — step 234, 2026-10-15.** Reuse the
prior SPECIALIZE assessment
`drafts/literature/2026-10-15-seven-shell-affine-fixed-dual-critical-audit.md`.
This review retains the statement without changing a coefficient or
mathematical hypothesis. It validates a local reproduction, not a new
general theorem or a radius improvement. The imports above cover the
finite real symmetric blocks, singular ranges, ordinary unordered
moments and quadratic optimization used here. The explicit square and
feasible point prove attainment directly; no converse KKT, strict
convexity or compactness assumption is needed.

The 7315-check independent verifier was rerun successfully. A separate
standard-library-only audit,
`scripts/finite-support/critical_audit_seven_shell_affine_fixed_dual.py`,
passes 9639 additional exact checks. Its complete certificate is
`scripts/finite-support/seven-shell-affine-fixed-dual-critical-audit.json`.
The following explains its mathematical coverage; check totals alone
are not the proof.

The original rho is checked against
(U+1)/(2 binomial(1024,68)), U=binomial(1024,64)/binomial(68,64),
and p5,p6,p7 are unchanged and positive. Import L065's established
complete affine solution, including its rank/exhaustion proof. Its
nonpivot coordinates are exactly f27=u,f33=v,f42=w. Regenerate the
entire 121-type old domain and 86-coordinate column domain, checking
all fixed signs and the anchor p7. For every original whole-base
kernel vector, substitute the four affine coefficient columns into
its weighted inner product, with the original 86 orbit weights.
All four coefficients vanish for each of the 49 kernel vectors.
The 49 original reduced equations also hold coefficientwise. This
checks the whole affine family, not just its old or new chosen point;
L065's averaging argument supplies the full-space interpretation.

Generate the 270 types independently of the saved record list, and
check that the lists coincide exactly. Before introducing seven/seven
entries, form the complete canonical unordered dictionary from all old
and column types. The bit permutations give all six presentations of
every type, with nonnegative atoms, total size 1024 and three support
sizes 68. The independent verifier additionally constructs these actual
supports and counts their regions point by point. Every old lookup,
Boolean repetition, forbidden case and reanchoring agrees coefficientwise,
including orders with incident distances outside the selected layers.
All 36 new free keys are distinct and absent from that dictionary.
For h=5,6 the seven/seven value is exactly the reanchored column entry;
for h=7 the full triple intersection fixes r and q, and h>7 has only
one eligible seven/seven anchor, as in L067. Hence there is no missing
identification among those keys. Every forced seven/seven sign follows
from a column sign, p7 or zero. Setting the remaining free moments to
zero is permissible before imposing PSD. Thus precisely the 49 listed
column inequalities describe the domain P in this statement. They
are not claimed to describe a scalar-plus-PSD feasible domain.

For normalization, import L067's audited direct relation actions on
J(68,l) and J(956,l), l=5,6,7, with their weighted monic bases and
positive norms. These are established mathematical inputs, not newly
proved transition counts in this review. The audit consumes all 118
saved transition matrices and checks every coordinate of their action
on every saved basis vector. The source decomposition and coherent
signed congruence already proved in L067 are independent of the moment
coefficients; they therefore apply to each affine coefficient separately.

More explicitly, write gamma_lm for the tensor product action coefficient,
N_l for the product basis norm, and let g_lm be the sum of these actions
against the affine entries. In mode (0,0), first subtract
p_l p_m S_m from its constant coefficient. This is precisely elimination
of the full positive anchor in orbit-action coordinates. Put
K_lm=N_l g_lm. With L067's positive scales s_l and s7=1, the audit
checks, coefficient by coefficient and in both rectangular directions,

  K_lm=(N7/D7) s_l C_lm s_m.

Old blocks are unchanged. Both variable cross directions agree in their
weighted form. This single coherent congruence handles the whole block;
no isolated pseudoinverse is transported. Source exhaustion supplies all
64 modes, including the 15 new-only modes.

Eliminate these weighted forms in reverse old-layer order, six before
five. Each positive pivot contributes the outer product of its entire
affine cross vector divided by that pivot. Every zero pivot has both
its residual old row and all four cross coefficients zero. Among the
36 two-old-layer modes, 9 have rank two, 8 rank one and 19 rank zero;
among the 13 one-old-layer modes, 10 have rank one and 3 rank zero.
The new-only modes contribute zero inverse cost. Dividing each resulting
four-by-four cost matrix by p7*N7 reproduces every entry of the saved
K_ab (whose source denominator is p7*D7). This verifies all singular
cases and every energy coefficient, rather than checking only the
weighted objective at one point.

Read the unchanged h,k from L067's manuscript and verify all 64 weights,
including exactly 24 positive ones. Reconstruct all 36 cancellations
with the original positive new/new valencies, all fixed affine terms,
the constant anchor correction and the complete weighted energy matrix.
All 16 entries of M agree with both original certificates. In particular
the u,v rows and columns vanish, alpha=-M33 is strictly positive,
beta=M03, and alpha*M00+beta^2=0 exactly. This proves the full identity
Phi=-alpha*(w-beta/alpha)^2, including its constant and linear terms.

At u=v=0,w=beta/alpha, check every free entry separately: precisely
indices 27 and 33 are zero and all other 47 are strictly positive.
Every fixed column entry is nonnegative. Substitute the entire column
back into all 49 original weighted kernel equations and into every
one of the 64 original right sides. All kernel residuals vanish and
the unchanged weighted sum is exactly zero. The right sides are saved
in full; their weighted sum does not certify individual PSD feasibility.
The old parameter -c4/a42_4 still gives the exact L067 value in
[-53503520/10^6,-53503519/10^6), preserving the immutable obstruction.

The initial curvature report is also consumed in full. Its only failed
check is `hessian_positive_semidefinite`. Its domain, all presentations,
all modes, both weighted terms, complete M, stationary point and free
witness are identical to the corrected report. In the Hessian half-form
H=-M[1:4,1:4], the first two diagonal entries are zero and the third is
positive; the full positive-pivot outer-product reconstruction equals H.
Thus the old check stopped too early at a zero pivot; it was not a
negative-curvature counterexample. The earlier field-name failure remains
recorded above and contributes no evidence. No original failed artifact
was overwritten.

Reproduce with the two verifier/audit commands above. Both consume all
relevant rational arrays. Full summaries, empty failure lists and the
exact attained value [0,1] were separately inspected. No mathematical
correction was necessary. This retains only the fixed dual's attained
maximum zero on P. Simultaneous completion, extra scalar rows, other
duals, global moments and RS realization remain unresolved.

## Mathlib

Full matching prescribed affine-family fixed-dual theorem: not checked.
Supporting singular-Schur, mixed-layer decomposition, PSD quadratic/KKT,
finite-group averaging and rational certificate coverage: not checked.
Unknown availability is not evidence of absence.
