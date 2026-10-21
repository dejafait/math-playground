# L060 — The complete column interval contains a full-shell PSD extension

## Hypotheses

Use L053's 1024-point ground set, 68-subsets, positive singleton rho
and unchanged pairs rho*p_i. In particular
p_5=1/68881143660 and p_6=133/9357995374380. Fix D,G at half-distance
six. Retain exactly L056's audited full anchored distance-five shell
and add the index {D,G}, with diagonal and entry against {D} both
rho*p_6. Retain precisely L059's five represented triple entries,
ten forbidden-distance zeros, and nonnegativity of the 21 free entries.
No extra scalar or actual-label constraint is imposed. All matrices are
finite real symmetric matrices, including their singular modes.

## Conclusion

L059's complete invariant nonnegative interval contains a rational column
for which this entire enlarged matrix is PSD. Its scalar generalized-Schur
energy has a unique minimum at a strictly interior parameter. If E_min
denotes the energy after division by rho, then exactly

  199/10^11 < E_min/p_6 < 200/10^11 < 1.

Thus this full-shell one-column extension cannot exclude the fixed
prescription. This is a finite reproduction/specialization of assessed
spectral and singular-Schur tools, without an originality claim.
It does not establish other columns, off-shell or other-anchor PSD,
global consistency, additional scalar constraints, labeled constraints,
a representing measure, an ordinary packing or common-center RS list.
The 955–957 boundary and arbitrary-center 67/68-agreement gap are unchanged.
The separate critical proof review below retains this conclusion.

## Proof

**Imported inputs.** Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-13-full-shell-column-energy.md`.
Import Takashi Sano, *Moore-Penrose inverse, generalized Schur complement
and inertia*, Acta Scientiarum Mathematicarum (27 February 2026),
DOI 10.1007/s44146-026-00231-y,
[Section 2, Theorem 2.6, Corollary 2.2 and Lemma 2.7](https://link.springer.com/article/10.1007/s44146-026-00231-y).
For a finite symmetric retained block C and new column b with scalar
diagonal d, the enlarged matrix is PSD iff C is PSD, b is orthogonal
to ker C and d>=b^T C^dagger b. The inverse acts by reciprocals of
positive eigenvalues on the range and by zero on the kernel. The finite
range is closed; no nonsingularity or maximal-rank assumption is used.

For the complete Johnson product decomposition import
Brouwer–Cioaba–Ihringer–McGinnis,
[arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2), Sections 1.2,3,3.4,
pp. 3,10,12, and Brouwer–Haemers, *Spectra of Graphs*,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf), Sections
11.2,1.4.7 and Theorem 2.7.1(i), pp. 162–163,19,36. Both factors
J(68,5), J(956,5) satisfy n>=10. L054 supplies the full-region dictionary;
audited L056 supplies the complete PSD shell, coefficients and all modes;
critically verified L059 supplies the complete affine interval and its
invariant weighted bases. No general source theorem is reproved.

For the convex quadratic optimality criterion import Boyd,
Vandenberghe and Nobel's revised *Convex Optimization* author slides,
[402-page PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf),
retrieved 13 October 2026, PDF pp. 53–55,97–99,105–106, as inspected in
foundations/10. A feasible point of a differentiable convex function on
an interval is a minimum when its derivative times every feasible
displacement is nonnegative. Here the actual positive curvature and
stationary point are checked exactly. The completed-square identity
below also directly certifies the entire interval, without numerical
optimization, Slater hypotheses or a general QP reproof.

**Transport the enlarged matrix.** Put B=L056's shell block/(rho*p_5)
and R=B-p_5 J. After division by positive rho the retained block and
new column are

  C=[1,p_5*1^T; p_5*1,p_5*B],  b=[p_6;p_5*t],  d=p_6.

Apply L059's invertible anchor congruence to the retained coordinates
and the identity to the new coordinate. The resulting retained block
is diag(1,p_5 R), the new column is [p_6;p_5*v], where v=t-p_6*1,
and the new diagonal remains p_6. Congruence preserves PSD of the
entire enlarged matrix. Apply Sano's criterion to this transported
block itself; do not transport a pseudoinverse through a congruence.
L056 gives R PSD and L059 gives v orthogonal to its full kernel.
Consequently the remaining condition is exactly

  E(t)=p_6^2+p_5*<v,R^dagger v> <= p_6,

where this inner product is over all actual shell supports. Both the
anchor term p_6^2 and the constant shell mode are retained.

**Exact weighted energy.** Use L059's 36 orbits indexed by (i,j),
0<=i,j<=5, with actual sizes

  W_ij=binomial(6,i)binomial(62,5-i)
       binomial(6,j)binomial(950,5-j).

For orbit-constant vectors define <x,y>_W=sum W_ij*x_ij*y_ij.
L059 gives the orthogonal monic factor vectors h_a^(68),h_b^(956).
Write H_ab(i,j)=h_a^(68)(i)h_b^(956)(j),
N_ab=<H_ab,H_ab>_W>0, and lambda_ab for L056's Schur eigenvalue of R.
These 36 products span the invariant space and belong to the full
claimed product eigenspaces. All zero eigenvalues are exactly L059's
20 listed nonconstant modes; every other lambda_ab is positive.
The inverse applied to an invariant vector remains invariant. Its
coefficients are therefore its weighted projections divided by
N_ab*lambda_ab on positive modes and zero on zero modes. Full-mode
multiplicities are not norms of these particular invariant vectors.

Let s=t_23. The complete affine column from L059 is
t_ij(s)=c_ij+m_ij*s, with its 21 free affine entries, five represented
constants and ten zeros unchanged. Its exact interval is [l,u], where

  l=3826948593076525737749263/221908927759242896073805386355372500,
  u=689512027427211313039687769/826754522994296083897677764417880000.

Set v0=c-p_6*1 and v1=m, and define the explicit finite rational sums
f_ab=<v0,H_ab>_W and g_ab=<v1,H_ab>_W. Both projections vanish on
all zero modes, on the entire affine line. Thus

  E(s)=A*s^2+B0*s+C0,
  A=p_5*sum_(lambda_ab>0) g_ab^2/(N_ab*lambda_ab),
  B0=2*p_5*sum_(lambda_ab>0) f_ab*g_ab/(N_ab*lambda_ab),
  C0=p_6^2+p_5*sum_(lambda_ab>0) f_ab^2/(N_ab*lambda_ab).

The factor basis can equivalently be normalized to value one at i=0;
rescaling cancels in each displayed term. The constructor uses that
normalization and verifies its equality with L059's monic basis.
These formulas specify exact coefficients using established rational
inputs. Their complete evaluated fractions are recorded below.

| Coefficient | Exact value |
|---|---|
| A | 98842711196747032115387619172183017083845595551049181306781154534285321001021452881726364744049042346851416242683686243385863228029919937397865552894621739092474431391931860220065495414998055124007653497417524437587317211648064920946121694674254185124646570683937298920000/6130897675527682949869615040104081652201845752941949443836807416867364033437031670656285763780986971057319563139738171555266560947647856300239686044671308745273104256797092590800496134985061366271786538413126845686537994138122536150516979136602802554523147078109711495973 |
| B0 | -802066317399486944458745987816646474814615455950926353365135462116153163077261087542689824641248239195478127385184956708331085621638819788817660620118075520575406463281817059800390251891992142492280041311296817376176468395946962973624833183163132374401662534236119037278/855942343280593305984130841594266330502699807692028515768406474009390528719462088763197411745240191291908945375268839061188752654501350306727544570461291655105288384129701404141229083229898363537464254807108501052996288712957907168246688958137850247565392708217068162079563960007 |
| C0 | 15582868110258643130070071219310122675956952647685270012044466692218083875487766781580004943755580325232072787439030977854713760716336592538594776917514319217677149324896680710949695738574665774560782979217217849055862715752313312261422251973771190792582140425869700267768562160889487019687/371550260052613758308274179317302143021959228929802113753712383452882353909612588849819229881985982240898737496120524230719946927310981832909465853367575968871038807958620444374118514288427328033258963297216292125409614478225528577416773450180699341402754344567653754715195892315637591781295716377160655520000 |

**Whole-interval minimization and verdict.** Exact rational evaluation
gives A>0 and l<s_*=-B0/(2*A)<u, with the tighter certificate

  14530655098541/500000000000000000000000 < s_*
    < 29061310197083/1000000000000000000000000.

The bounds are strict (the exact rational parameter is not an endpoint
of either bounding interval). For every real s,

  E(s)=E_min+A*(s-s_*)^2,  E_min=C0-B0^2/(4*A).

This proves that the unique minimum over the complete closed interval
is E_min at s_*. Exact evaluation gives

  1992907587/10^18 < E_min/p_6 < 498226897/250000000000000000,

which implies the conclusion's simpler strict bounds. Hence E_min<p_6.
L059's complete interval supplies nonnegativity at s_*, including all
fixed entries. Sano's singular criterion now proves PSD of the full
transported enlarged matrix and hence of the original matrix. Every
ordered D,G at distance six has the same four-region description;
L059's transitivity transports this constructed column to each such
pair, preserving precisely the stated unlabeled constraints. This pass
needs no claim about averaging a labeled feasible matrix, nor any
promotion of kernel-only averaging to a full-PSD exclusion theorem.

**Complete rational evidence.** Run from the notebook:

  `python3 scripts/finite-support/full_shell_column_energy.py`

The certificate `scripts/finite-support/full-shell-column-energy-results.json`
contains all 36 affine entries, actual orbit weights, all factor relation
quotients and recurrence bases/norms, every product spectrum and weighted
projection, the full 36-by-36 action of R, inverse intercept/slope vectors,
all inverse-action residuals, the exact quadratic, endpoints, stationary
point, minimum, new diagonal, signed slack and minimizing column.
All 372 checks pass. No floating point or optimizer is used.

For clarity, the action of relation r on intersection classes i,i' in
an n-point factor is reconstructed by the complete four-region count

  Q_r(i,i')=sum_(w=0)^5 binomial(i,w)binomial(6-i,i'-w)
                 binomial(5-i,5-r-w)binomial(n-11+i,r+w-i').

The four choices select X' in X cap U, U outside X, X outside U, and
the remaining region respectively. They exhaust X' of size five with
|X cap X'|=5-r and |X' cap U|=i'. Out-of-range choices vanish.
Therefore the 36-orbit action is

  R_[(i,j),(i',j')]=sum_(r,q) d_rq*Q_r^(68)(i,i')*Q_q^(956)(j,j')
                       -p_5*W_i'j',

using L056's full normalized d including d_00=1. Every row is checked
for weighted self-adjointness, and every coordinate of the action on
all 36 products is checked. This quotient is not ordinarily symmetric;
its inner product is exactly the W inner product above.

Independently run

  `python3 scripts/finite-support/verify_full_shell_column_energy.py`.

It imports no notebook module or constructor and uses no spectral
inversion. It reconstructs the actual action and affine column directly
from the canonical L056 and audited L059 input, checks all 72 residual
coordinates R*y0=v0, R*y1=v1, and checks both inverse vectors against
all 20 zero-mode projections. Thus these are the range inverses in the
actual weighted space. It computes the energy coefficients independently
as p_5*<v1,y1>_W, p_5*(<v0,y1>_W+<v1,y0>_W), and
p_6^2+p_5*<v0,y0>_W. It checks all three complete fractions, the strict
interior condition, completed-square identity, both endpoint energies,
all 36 minimizing entries, exact minimum and positive diagonal slack.
All 177 independent checks pass. Full evidence is in
`scripts/finite-support/full-shell-column-energy-verification.json`.
The full failure lists, all residuals, complete evaluated coefficients,
minimizer and exact comparison have been inspected. This arithmetic
verification is distinguished from the separate critical proof review below.

**Separate critical proof review — step 200, 2026-10-14.** Reuse the
unchanged SPECIALIZE assessment
`drafts/literature/2026-10-13-full-shell-column-energy-critical-audit.md`.
The review retains the hypotheses, exact minimum and full-shell one-column
PSD conclusion. This verifies a local reproduction; it supplies no new
claim beyond the checked sources or improvement to the RS boundary.

First, the anchor change of coordinates is invertible on the actual
finite shell space. Extend it by the identity on the new coordinate.
The transported retained matrix is exactly diag(1,p_5 R), its new column
is [p_6;p_5 v], and its new diagonal is p_6. The imported criterion is
applied to this matrix, not to a purported congruence formula for a
pseudoinverse. With y=R^dagger v, the vector w=[p_6;y] satisfies
diag(1,p_5 R)w=[p_6;p_5 v], and its quadratic value is
p_6^2+p_5*<y,Ry>=E. This verifies the normalization in the scalar
generalized-Schur test, including the anchor term and constant mode.

Second, each four-region occupancy count is a count of actual shell
supports. The lifted orbit basis has inner product W, not the unweighted
quotient inner product. Independently reconstructed monic factor vectors
are in the Johnson modes specified above: their action under every
relation is checked, with positive norms and the complete factor bases.
Their tensor products span all invariant vectors. L056's complete
product spectrum makes the full R PSD, including noninvariant vectors.
For any full kernel vector z, its stabilizer average remains in the
kernel, and an invariant y has <y,z>=<y,average(z)>.
Consequently testing all 20 invariant zero-mode products proves
orthogonality to the full kernel for both affine inverse vectors. Their
36-coordinate identities R*y0=v0 and R*y1=v1 are identities of actual
orbit-constant functions on the shell. They therefore give the full
range inverses used in the energy, with no missing multiplicity factor.

Run `python3 scripts/finite-support/critical_audit_full_shell_column_energy.py`.
The independent script imports no notebook code. It enumerates all four
region occupancies to reconstruct each factor quotient, obtains the
bases by weighted Gram–Schmidt, and compares every factor action, full
weighted shell-action entry, product norm, eigenvalue and projection with
the complete saved evidence. It independently reconstructs both inverse
vectors, checks every residual and kernel projection, and recovers the
quadratic both spectrally and by bilinear products. Every digit of the
three manuscript coefficient fractions is checked. The entire affine
column, represented values and zeros, exact nonnegative interval,
stationary parameter, completed square, endpoint energies, minimizing
entries and both displayed strict bounds agree with both original
certificates. Direct substitution also checks the minimizing column's
range identity and w's quadratic value in the transported enlarged
matrix. The exact positive remainder is p_6-E_min, as required.

All 5707 final audit checks pass. Full reconstructed evidence and check
names are in `scripts/finite-support/full-shell-column-energy-critical-audit.json`.
An initial audit-only assertion unnecessarily required p_5<p_6, which
is false; neither the manuscript nor the proof uses that ordering.
It was replaced by the required separate positivity checks. The initial
failure certificate is preserved at
`scripts/finite-support/full-shell-column-energy-critical-audit-initial.json`.
No original mathematical coefficient or conclusion required repair.

The strict interior minimum and completed-square identity apply to the
entire stated invariant interval, not just its sampled points or endpoints.
All five represented entries, ten forbidden zeros and 21 free coordinates
remain intact. Transport to another ordered distance-six pair preserves
the ordinary unlabeled slice only. The construction remains one added
index at a time: it supplies no cross entries between added indices,
simultaneous PSD, extra scalar constraints, representing measure or RS
realization. ATTEMPTS/042's one-column exclusion remains parked.

## Mathlib

Full matching weighted energy certificate, complete column minimization
and this retained PSD extension: not checked. Supporting Johnson
decomposition, pseudoinverse, singular Schur and convex quadratic results:
not checked. Unknown availability is not evidence of absence.
