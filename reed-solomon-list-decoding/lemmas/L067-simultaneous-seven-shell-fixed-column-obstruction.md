# L067 — The fixed distance-seven columns have no simultaneous extension

## Hypotheses

Use L061's complete anchored five/six-shell matrix and every unchanged
L062 moment, on the 68-subsets of a 1024-point set. Divide all matrix
entries by the original positive singleton rho. The anchor entry is one;
the original pairs are p5=1/68881143660, p6=133/9357995374380 and
p7=3539/248922676958508. Fix a 68-subset D.

For every G with |D\G|=7, prescribe exactly L065/L066's entire column
against the anchor and both old shells: u=v=0,w=-c_4/a^42_4 in L065's
specified affine system. Its anchor entry and diagonal are p7.
Retain every L062 lookup under all unordered presentations, Boolean
repetitions and forbidden nonzero half-distances 1,...,4. Remaining
moments must agree for the same unordered support triple and be
nonnegative. Test the whole matrix indexed by {D} and all {D,E} with
|D\E| in {5,6,7}. No retuning or extra scalar upper rows are allowed.

## Conclusion

No such PSD extension exists. All fixed unordered presentations are
consistent; the obstruction is a joint PSD obstruction. A nonnegative
24-weight combination of the complete mixed-layer necessary inequalities
cancels all 36 free coefficients and has a strictly negative fixed term
in the exact interval [-53.503520,-53.503519). It therefore also excludes
extensions allowing those remaining coefficients to be signed.

This rejects only the immutable simultaneous prescription. L066's
individual-column PSD extensions and all earlier smaller-slice passes
remain valid. Other choices in L065's compatible family, other base or
pair moments, global feasibility, labeled constraints and common-center
RS realization remain unresolved. The 955–957 bracket and arbitrary-center
safety at 67/68 agreements do not change. This is a REPRODUCTION of
assessed tools with a new local finite verdict, not a novelty claim.
The separate critical proof review below retains this fixed obstruction.

## Proof

**Imports.** Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-14-simultaneous-five-six-seven-shell-extension.md`.
Import Alexander Schrijver, *New code upper bounds from the Terwilliger
algebra and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59) and III.B (64),
printed pp. 5–7. Its mixed-layer decomposition applies to ordinary
invariant matrices without a representing measure. The factor sizes
68 and 956 and layers 0,5,6,7 satisfy the source ranges. All source
blocks meeting these layers are retained, including singular and
new-only modes. Foundations/09 and L061 fix the beta normalization.

Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, Acta Scientiarum Mathematicarum, version of record
27 February 2026, DOI 10.1007/s44146-026-00231-y,
[Section 2, Theorem 2.6 and Corollary 2.2](https://link.springer.com/article/10.1007/s44146-026-00231-y).
For a finite symmetric matrix with retained PSD block B, cross block T
and new block A, PSD is equivalent to T^T ker B=0 and
A-T^T B^dagger T PSD. Neither invertibility nor maximal rank is assumed.
The entire anchor is eliminated by congruence below; no pseudoinverse
is transported alone. Foundations/10 records this source coverage.

The equal-union interpretation and constraint-preserving averaging are
Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
IEEE TIT 65 (2019), 28–38, DOI 10.1109/TIT.2018.2854800,
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), Section 1.1
(1)–(3), Proposition 1.1 and its indicator proof, p. 2, and Section 1.2,
p. 3. Use the proof's constant-weight conclusion A(n,d,w), with
n=1024,d=10,w=68, as qualified in foundations/12. No general theorem
is reproved. The new calculation evaluates this particular prescription.

**All entries and presentations.** Write E=(D\X) union Y and
G=(D\U) union V, with |X|=|Y|=l, |U|=|V|=m,
i=|X intersection U| and j=|Y intersection V|. The atom tuple in masks
0,...,7 for bits D,E,G of weights 4,2,1 is

  (956-l-m+j,m-j,l-j,j,i,l-i,m-i,68-l-m+i).

The half-distances are l,m,l+m-i-j. Each tuple has nonnegative entries,
sum 1024 and support sizes 68. Atom bijections show that these are all
orbits under the point permutations fixing D. There are 270 relation
types: 121 old types, 36 five/seven types, 49 six/seven types and 64
seven/seven types. Denote their normalized moments by Y_(l,m,i,j),
with reversed layers obtained by transposition. On old types use L062;
on five/seven and six/seven use precisely L065's column.

For seven/seven put r=7-i, q=7-j and h=r+q. Complete unordered
consistency forces

  Y_(7,7,7,7)=p7;
  Y_(7,7,7-r,7-q)=0 for 1<=h<=4;
  Y_(7,7,7-r,7-q)=Y_(h,7,q,r) for h=5 or 6.

The last identity reanchors at E, taking G as its h-neighbor and D as
its seven-neighbor. Its two column intersections are q,r. This retains
the actual whole-region moment, not merely its distance triple.
For h>=7 the 36 coefficients are free. At h=7 reanchoring preserves
r,q (the common triple intersection has size 61-r); at h>7 only D
has both incident distances seven. Thus these free coefficients have
no further identifications with one another or the immutable dictionary.

All six support orders were compared for every type, including orders
whose incident distances leave {5,6,7}. Canonical complete atom keys
and all prescribed values agree. The independent verifier realizes
actual subsets, computes every region point by point and checks the
1,620 presentations. It recovers all old entries and the exact affine
column, not a floating approximation. All fixed entries are nonnegative.

The group S_68 x S_956 preserves these fixed data, Boolean rules,
forbidden distances, unordered identifications and nonnegativity. It
permutes rows/columns of the selected matrix. Hence averaging any
hypothetical extension preserves PSD and every condition and produces
an invariant extension. Excluding invariant assignments therefore
excludes all assignments in the hypotheses. No actual-label condition
is averaged or asserted preserved.

**Complete necessary inequalities.** For n in {68,956}, define

  beta(n,l,m,a,t)=sum_(u=max(a,t))^min(l,m,n-a)
    (-1)^(u-t) binomial(u,t) binomial(n-2a,u-a)
    binomial(n-a-u,l-u) binomial(n-a-u,m-u).

For a,b in {0,...,7}, layer l occurs exactly when a,b<=l. Put
S_l=binomial(68,l)binomial(956,l) and
D_l=binomial(68-2a,l-a)binomial(956-2b,l-b), positive for present layers.
After the positive anchor is eliminated from the entire matrix, its
source block entries are

  C_lm=sum_(i,j=0)^min(l,m)
      beta(68,l,m,a,i) beta(956,l,m,b,j) Y_(l,m,i,j)
      -1_(a=b=0) p_l p_m S_l S_m.

The anchor beta entries before elimination are p_l S_l. This explains
both factors in the constant correction. Let B be the present old
layer block (layers 5 and/or 6) and t the corresponding entries C_l7.
The old B is PSD by L061. Every singular range condition is checked;
it also follows from L065's full-base kernel compatibility transported
to every new column. Put R_ab=t^T B^dagger t/(p7 D_7), zero if no
old layer occurs. These numbers are evaluated without numerical inverses:
for B=[[x,t0],[t0,z]], c=(u,v), positive determinant delta gives
(z*u^2-2*t0*u*v+x*v^2)/delta; if delta=0 and x>0, the checked relation
x*v=t0*u gives u^2/x. If x=0,z>0, use v^2/z with t0=u=0;
if B=0 then c=0 and the cost is zero. The one-layer cases use the
same scalar rule. Divide each cost by p7 D_7 to get R_ab.

All 64 modes are included, including modes with only layer 7. Their
positive multiplicities are
(binomial(68,a)-binomial(68,a-1))
(binomial(956,b)-binomial(956,b-1)). Summing over the modes of each
layer gives S_l, checking full-space exhaustion. As a normalization
cross-check the complete energy trace satisfies exactly

  p7^2+(p7/S_7)*sum_(a,b) multiplicity(a,b) R_ab
    = L066's full-space one-column energy.

Define E_(n,a)(r)=beta(n,7,7,a,7-r)/binomial(n-2a,7-a), equivalently
sum_(s=0)^r (-1)^s binomial(a,s)binomial(7-a,r-s)
binomial(n-7-a,r-s), the imported Johnson eigenvalue. Put
v_(r,q)=binomial(7,r)binomial(61,r)binomial(7,q)binomial(949,q)>0.
For r+q>=7 write Y_(7,7,7-r,7-q)=p7*z_(r,q)/v_(r,q).
All z are nonnegative under the hypotheses. Let

  F_ab=sum_(r+q<=6) [Y_(7,7,7-r,7-q)/p7] E_(68,a)(r) E_(956,b)(q),
  A_ab=1_(a=b=0)*p7*S_7,
  H_(ab,rq)=E_(68,a)(r)E_(956,b)(q)/v_(r,q).

The singular-Schur criterion gives the necessary inequalities

  sum_(r+q>=7) -H_(ab,rq) z_(r,q) <= F_ab-A_ab-R_ab.          (1)

Every coefficient and bound is rational. This is the full joint
condition after the verified old-block range tests, not the diagonal
energy tests of L066.

**Explicit dual contradiction.** Use weights lambda_ab=h_a*k_b, where

  h=(1,20435/441,13481000/13671,2688040/217,
     1307664259/13671,5294968393/13671,0,0),
  k=(49/100880416043264,7665/38718903137024,
     17301/551968803584,5461349/2754064239872,0,0,0,0).

Exactly 24 weights are positive and all others zero. Direct substitution
in the finite beta sums gives, indexed by r=0,...,7,

  sum_a h_a E_(68,a)(r)
    =(10424128/21,1271743616/21,6358718080/7,0,0,0,0,0),

and indexed by q=0,...,7,

  sum_b k_b E_(956,b)(q)
    =(21/10424128,1533/200464,1089963/200464,
      114688329/100232,4931598147/72896,0,0,0).

For r+q>=7, either r>=3 or q>=5, so their product is zero. Therefore
every free coefficient in the weighted sum of (1) cancels exactly.
The verifier checks all 36 cancellations directly as well as these
two complete transform identities. No sign assumption on z is used
after cancellation.

For the unchanged fixed entries, the exact finite sums satisfy

  1897002902/10^6 <= sum lambda_ab F_ab < 1897002903/10^6,
   948289785/10^6 <= sum lambda_ab A_ab <  948289786/10^6,
  1002216636/10^6 <= sum lambda_ab R_ab < 1002216637/10^6.

These are rational integer-comparison bounds, not numerical estimates.
Consequently the weighted right side of (1) is strictly less than
-53503518/10^6<0, whereas the left side is zero. The complete exact
value has the tighter interval [-53503520/10^6,-53503519/10^6).
This contradiction proves the conclusion.

**Reproducible arithmetic and limits.** From the notebook run
`python3 scripts/finite-support/simultaneous_seven_shell.py` and
`python3 scripts/finite-support/verify_simultaneous_seven_shell.py`.
The complete certificates are respectively
`scripts/finite-support/simultaneous-seven-shell-results.json` and
`scripts/finite-support/simultaneous-seven-shell-verification.json`.
They contain all input hashes, all presentations, the entire rational
64-by-36 system, every singular-block entry and cost, exact dual,
all coefficient sums, exact fixed value and rational bounds. The
constructor passes 2,337 checks. Its decimal phase-I run proposes only
a dual; all conclusions follow from rational reconstruction.

The independent verifier imports no constructor or optimizer and uses
no floating arithmetic. It recomputes actual subset presentations,
all source beta blocks, determinant-based inverse costs, every dual
coefficient and the exact contradiction. All 5,415 checks pass with
no failures. The explicit product dual and transforms above remove
any dependence of the proof on an optimizer's chosen basis. The prior
L065 affine solution and L062 dictionary are imported established
inputs; their entire derivations are not silently claimed reaudited.
The separate critical review below additionally checks both rectangular
directions and their common three-layer normalization.

An initial constructor run stopped at a source-hash field-name mismatch
before any calculation result; it was repaired to read the existing
energy certificate's `input_hashes`. No source or mathematical parameter
changed. No unsuccessful numeric status is used as evidence.

This finite contradiction is not a bound over other moment prescriptions,
not an actual-support obstruction beyond its hypotheses, and not an RS
safety theorem. It does not contradict any isolated-column pass.

**Separate critical proof review, 2026-10-15.** Reuse the prior SPECIALIZE
assessment
`drafts/literature/2026-10-15-simultaneous-seven-shell-obstruction-critical-audit.md`.
This review retains the statement, coefficients, hypotheses and scope.
It verifies a local reproduction of the cited tools; no original general
theorem or improvement to the RS boundary is claimed. The existing
independent verifier was rerun: all 5,415 checks pass. The additional
independent script
`scripts/finite-support/critical_audit_simultaneous_seven_shell.py`
imports no notebook code, optimizer or floating arithmetic. All 8,736
additional exact checks pass. Its full certificate is
`scripts/finite-support/simultaneous-seven-shell-critical-audit.json`.

The audit verifies original rho=(U+1)/(2 binomial(1024,68)), with
U=binomial(1024,64)/binomial(68,64), all original p5,p6,p7, the full
121-entry L062 dictionary and every L065 column coordinate reconstructed
from its specified affine data. These are imported mathematical inputs;
this audit does not claim to rederive their earlier certificates. It
checks all source hashes, including the rerun verifier's exact inputs.

The independent verifier constructs actual supports and counts all eight
regions point by point at all 1,620 presentations. The additional audit
separately regenerates every atom permutation, Boolean value, forbidden
zero, old lookup and h=5,6 reanchoring from the formulas above. Grouping
by the canonical complete atom key and by
(sorted half-distances, i-j) gives precisely the same unordered
identifications. The 36 free keys are distinct, and all fixed values
agree, including presentations outside the retained layers. For h=7
the common triple intersection 61-r determines r, then q=7-r, so
reanchoring cannot merge different free keys. For h>7 only D has two
incident distances seven. Thus no extra free-key identification or
missing immutable lookup is suppressed. Atom bijections exhaust the
stabilizer orbits. Since the prescribed data depend only on these atoms,
the required averaging preserves the exact ordinary slice. It does not
transport a subgroup-label restriction.

For an independent check of the rectangular normalization, fix a
seven-subset U of an n-set, n=68 or 956. The layer-l intersection orbits
have weights W_l(i)=binomial(7,i)binomial(n-7,l-i), all positive. For
l,m in {5,6,7}, the relation |X intersection Y|=t acts by

  Q_lm^t(i,j)=sum_x binomial(i,x)binomial(7-i,j-x)
    binomial(l-i,t-x)binomial(n-7-l+i,m-j-t+x).

The four factors count Y separately in X intersection U, U outside X,
X outside U and the remaining points. Impossible occupancies contribute
zero. All 118 such matrices, in both directions, are reconstructed.
Their full row sums equal binomial(l,t)binomial(n-l,m-t). Weighted
Gram–Schmidt on 1,i,...,i^l gives monic vectors h_l,a with positive
norms N_l,a. Every coordinate of every action is checked:
Q_lm^t h_m,a=gamma_lm,a(t) h_l,a for a<=l, and zero for a>l.
For l=m the action agrees with the imported Johnson eigenvalue and
beta(n,l,l,a,t)=binomial(n-2a,l-a) gamma_ll,a(t).

For every rectangular relation the audit checks

  N_l,a gamma_lm,a(t)=N_m,a gamma_ml,a(t),
  gamma_lm,a(t)gamma_ml,a(t)
    =beta(n,l,m,a,t)^2/
      [binomial(n-2a,l-a)binomial(n-2a,m-a)].

For nonzero beta, gamma_lm,a(t)/beta is one positive rational constant
across all t; both actions vanish when beta vanishes. Additionally let
sigma_lm=N_l,a gamma_lm,a(t)/beta at any nonzero beta. For every
present l,m, the complete triangle identity

  sigma_lm sigma_77=sigma_l7 sigma_m7

is checked. Thus the two rectangular normalizations and the old 5/6
normalization fit one positive diagonal congruence on the whole
three-layer block. Pairwise squared identities alone would not suffice
to verify that sign compatibility.

Tensor the two direct actions. Let N_l=N_l,a^(68) N_l,b^(956), and
let g_lm be their sum against the actual fixed entries. In the constant
mode subtract p_l p_m S_m from g_lm; this is the actual anchor
elimination before taking the weighted form. Put K_lm=N_l g_lm.
The audit checks every fixed K_lm and both cross directions. Writing
s_l=(sigma_l7^(68) sigma_l7^(956))/(N_7/D_7), s_7=1, it obtains

  K_lm=(N_7/D_7) s_l C_lm s_m,

with all s_l positive. In particular every fixed old block and cross
vector is the asserted congruence of the complete source block, with
the anchor correction intact. Source decomposition, not a count of
quotient vectors alone, supplies full-space exhaustion. Its layer
ranges here give all 64 modes, and the positive multiplicity sums
independently recover S5,S6,S7.

Exact elimination in reverse old-layer order (6 before 5) on these
weighted forms verifies nonnegative pivots and every zero-pivot range
condition. Among the 36 two-old-layer modes, the old ranks are two in
9 cases, one in 8 and zero in 19. Among the 13 one-old-layer modes,
10 have rank one and 3 rank zero; 15 modes are new-only. Every case is
retained. The inverse-action cost in this basis, divided by p7*N_7,
equals the saved R_ab in each of the 64 cases. This independently
checks the denominator p7*D_7 in the source coordinates. All fixed
terms, the entire 64-by-36 coefficient matrix and every right side
agree with the saved system. The complete energy trace, including
p7^2, again equals L066's full-space energy.

Finally the audit reads h,k and both entire displayed transforms from
this manuscript. Direct action evaluation agrees with all their exact
entries, the 24 positive weights, and all 36 separate zero coefficient
sums. Every displayed rational interval is checked by exact comparison.
The resulting fixed term is in [-53503520/10^6,-53503519/10^6), strictly
below zero. Hence the nonnegative sum of the necessary inequalities
would assert zero is at most a negative number. No sign restriction on
the canceled variables is used. This verifies the claimed exclusion of
the immutable simultaneous prescription. It does not exclude other
compatible columns, replace any source theorem, imply a uniform bound,
or contradict the reviewed one-column and five/six-shell passes.

Reproduce the additional audit with
`python3 scripts/finite-support/critical_audit_simultaneous_seven_shell.py`.
The full certificate saves all actual transition matrices, polynomial
bases and norms, signed scales, all mode forms and pivots, exact costs,
complete transforms and dual residuals. No coefficient or mathematical
scope correction was needed. Mathlib availability below is unchanged.

## Mathlib

Full matching fixed simultaneous-column obstruction: not checked.
Full matching mixed-layer decomposition, singular-Schur criterion and
Boolean-constrained completion: not checked. Supporting finite rational
arithmetic, matrix PSD and finite-group averaging coverage: not checked.
Unknown availability is not evidence of absence.
