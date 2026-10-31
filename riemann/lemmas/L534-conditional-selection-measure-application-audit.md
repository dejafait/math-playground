# L534 — Conditional selection-measure application audit

## Hypotheses

Use the notation and external-calculus conventions of L533 over
F=Q(sqrt(-3)). This lemma checks a selection interface, not all hypotheses
of L533. Fix the source arithmetic datum, excluded set S, finite character
group Theta, finite slot system, bounded real ranges and positive losses.
Put U=Z^d, 0<d_min<=d<=d_max, T_1=Z^tau>2. The slots have fixed positive
lengths ell_i, scales P_i=Z^ell_i and smooth fixed annular weights W_i.
Their underlying annular prime supports are disjoint before imposing the
fixed ray restriction 1_T and S. In particular their allowed sets are

\[
 \mathcal P_i(Z)=\{p:p\notin S,\ p\in1_T,
                          q_p/P_i\in\operatorname{supp}W_i\}.
\]

There is no additional arbitrary prime selector in this formula. All
natural character zeros and any admissible fixed common masks are retained.
Physical rows are sixth-power-free, q_u comparable to U. Retain the source
bin, global/reciprocal bounds and witness existence/height hypotheses of
`lem:buffered-bins`, `lem:detector-dyads` and `prop:detector-witness`.
Their arithmetic assertions and the construction of the witness zeros are
not proved here. Retained large rows induce outside Theta when a positive
plain slot is used; this arithmetic family condition is an explicit input.

Assume the following moment assertions of the pinned source cited below,
including finite smooth-seminorm bounds, polynomial norm-twist height
costs, and uniformity over their admitted moving labels. These are source
contracts, not an audit of their internal arithmetic proofs.

1. `lem:marked`, at base U and effective row width one, for either common
   character orientation, with row-independent slot supports and bounded
   coefficients, and fixed positive margins
   r+2zeta<=1-c_1 and 2r+8zeta<=3-c_2. The squared row norm of an inverse
   polynomial of length r times those slots is O(U^(1+epsilon)), apart
   from the stipulated finite profile and polynomial height factors.
2. `lem:plain`, for two plain polynomials of lengths m_1,m_2 and total
   slot length zeta, at effective width one. With no live slots there is
   no restriction on bounded m_1,m_2 and the rows must be nonprincipal.
   With live slots require the stated fixed short-slot mesh,
   m_1+m_2+6 kappa zeta<=1, and inducing characters outside Theta.
   Here 3/4<=kappa<=1 and beta_*<=(1+kappa)/2 if kappa<1. Coefficients
   are fixed finite combinations of Theta characters. Its common-mask
   and original-zero-extension conditions hold. The squared row norm
   is O(U^(1+epsilon)) with the stipulated profile/height factors.
3. `lem:inverse-amplification`, for no slots and sixth-power-free rows,
   gives O(U^(e(r)+epsilon)), e(r)=max(1,(1+5r)/6), on bounded r ranges,
   with finite seminorm bounds and the stated rowwise real-power and
   twist-height clause. The auxiliary positive amplification margin is
   fixed before U, including when r approaches one.

For each application fix the physical Mellin tuple, dynamic and amplitude
bin, witness presentation label, dyadic pair D=U^r, N_d=U^m, detector
parameter t, and selected slot indices before taking a row norm. The
fixed character label is denoted nu_ray below; the real Fourier frequency
is v. The source uses nu for both. The remaining witness parameters are
sigma in a fixed compact interval and h=gamma-v with |h|<=C_0 T_1,
where C_0 is fixed. A single complete buffered-coordinate allocation and
global bounds on any extended axes are still inputs when L533 is used.
Full coordinate completeness, internal measure realization, full correction
holomorphy and auxiliary central accounting are not inferred here.

## Conclusion

The following selection-level analytic interface passes conditionally.

- The witness separation has a common, pointwise rapidly decreasing
  Fourier density on each fixed block. Its orders are uniform in U,D,N_d.
- Rowwise (sigma,h) choices are controlled by parameter Sobolev applied
  to the moment polynomials. For marked and plain applications, including
  the squared plain witness, the squared row sum is at most
  C U^(1+epsilon)(1+T_1)^(A+1), for a fixed finite A encompassing the
  physical heights and the finitely many derivative profiles. No common
  measure supported at the rowwise selected frequencies is asserted.
- The inverse/plain dyadic and physical prime transforms used on external
  joins have uniform pointwise decay at every fixed requested order after
  pure twists are translated into their arithmetic arguments. In the
  prime case the imaginary argument is v_p-Im(z_phys).
- Later external decay orders change only external test seminorms and
  constants. They do not increase the fixed internal moment/profile orders
  or the previously fixed polynomial scale and height degrees.

These conclusions discharge these particular external-density and
rowwise-parameter obligations in the use of L533. They do not establish its
entire central estimate, the optimized row count, all of `lem:high-bin`, a
zero-free half-plane, Xi signs, or RH. Progress is local reproduction of a
source-claimed interface, not progress beyond the checked source.

## Proof

Source: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane
Re(s)>7/8*, September 30, 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[primary TeX](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Precise locations are `lem:smooth-calculus`, especially
`eq:parameter-sobolev` and `eq:pointwise-mellin-tail` (retrieval lines
1019–1166); `lem:detector-dyads` and `prop:detector-witness` (4117–4400);
physical slot definitions (6454–6469); `lem:marked` (8682–8730);
`eq:indexed-coefficient-measure` and the commonness/order qualifications
(8939–9026, 9096–9149); `lem:inverse-amplification` (11681–11725);
`lem:plain` with its preceding row/mask definitions (11803–11894);
`lem:bin-prime-bound` (14192–14254); `sec:selection` (14285–14449,
14450–14476 for the uniform no-slot margin); and `lem:high-bin`
(14858–14993). Labels are stable identifiers; lines are retrieval coordinates.
This application proof is needed because citing high-bin would assume the
interface being tested. We reuse L533's external calculus instead of
reproving its contour theorem or the source arithmetic moment estimates.

### Fixed-block commonness and coefficient orientation

Write D_*=U^t, Y_*=U^20 and use the source fixed smooth cutoffs. On a
fixed compact annulus in x the separating profile is

\[
 H_{D,N_d}(x)=\Omega(x)[1-V_{\le}(2DN_dx/D_*)]
           e^{-DN_dx/Y_*}V_{\rm term}(DN_dx/U^{21}).            \tag{1}
\]

It depends on U,t,D,N_d, not on the varying row, its zero, or its
selected frequency. To check uniformity, set L=x d/dx. For j>0,
L^j V(c x) is a fixed linear combination of (cx)^k V^(k)(cx).
The derivatives of either cutoff are supported in a fixed compact
transition interval; the zeroth derivatives are bounded. Each derivative
of exp(-c x) is a polynomial in c x times exp(-c x), bounded for c x>=0.
Leibniz's rule and the fixed support of Omega therefore bound every
fixed L^j H uniformly. This includes blocks meeting either cutoff edge;
there is no sharp, row-dependent endpoint.

Writing H_log(u)=H(exp(u)), its support is fixed and compact. Integration
by parts j times gives |H-hat(v)|<=C_j |v|^(-j) for |v|>=1; its L1
bound gives the missing |v|<1 estimate. Thus

\[
 \sup_v(1+|v|)^j|\widehat H_{D,N_d}(v)|\le C_j.               \tag{2}
\]

Fourier inversion of H(xy) has coefficient
H-hat(v)dv/(2pi), common to the fixed block. Formula (2), with j>J+N+1,
also supplies its weighted integrated tail O(T_1^(-N)). The absolute
density is continuous in v and in its scale parameters, hence jointly
Borel. Row-dependent phases and character zeros stay in the row vector.
Minkowski is legitimate for this common measure if needed before
selection; evaluating one different selected v in each row is a separate
operation treated below. Trivial bounds for the finite blocks have fixed
U powers since D,N_d have bounded logarithmic lengths. Consequently this
Fourier tail can be made negligible using an external order chosen after
tau, without using a larger internal moment order.

Fixing the presentation label and, if necessary, conjugating both witness
factors yields psi_u(n)=nu_ray(n) overline(chi_n(u)). For allowed primes,
nu_ray has modulus one, and

\[
 \overline{\nu_{\rm ray}(p)}1_{p\in1_T}
   =|T|^{-1}\sum_{\theta\in\widehat T}
                      (\overline{\nu_{\rm ray}}\theta)(p).   \tag{3}
\]

Multiplication by psi_u(p) recovers the physical slot character, including
its zero if p divides u. Equation (3) is independent of u and has a fixed
finite character expansion. It verifies the marked coefficient class.
For the plain estimate conjugate the entire product, including both
witness profiles and every selected slot. The absolute square is
unchanged; the row orientation becomes positive and the slot coefficient
becomes nu_ray(p)1_(p in 1_T), again of the required class. No character is
divided out at a natural zero. Disjoint underlying supports remain
disjoint, and common masks remain common. Subdividing rows by a witness
choice does not insert that eligibility into the coefficient profile:
in a nonnegative moment sum one may enlarge the row subset to the
appropriate admissible family.

### Rowwise Sobolev application and the fixed height cost

The untwisted inverse base is B_D(y)=W_1(y)V_le(Dy/D_*); the plain base
is W_2(y). The same cutoff argument as for (1) gives uniform fixed
logarithmic seminorms of B_D. The actual profiles are
B_D(y)y^(-sigma-ih) and W_2(y)y^(-sigma-ih). These are normalized
annular variables: derivatives do not produce log q_n or log U.
For j,k in {0,1},

\[
 \partial_\sigma^j\partial_h^k
       [B(y)y^{-\sigma-ih}]
   =(-1)^j(-i)^k(\log y)^{j+k}B(y)y^{-\sigma-ih}.             \tag{4}
\]

These are admitted annular profiles, with uniform seminorms on a fixed
enlargement of the compact sigma range. Their twist-height costs are the
fixed polynomial costs of the assumed moments. Logarithmic factors do
not change support, row orientation, masks or slot lengths.

At fixed physical parameters let Q_u be the selected product and set
F_u=M_u(sigma,h)Q_u in the marked case, and
F_u=S_u(sigma,h)^2 Q_u in the plain case. The latter choice is essential:
its absolute square is |S_u|^4 |Q_u|^2. Product differentiation of F_u
using (4) is a fixed finite sum. In the plain case each term is a product
of two possibly different logarithmically weighted plain profiles, so
the stated two-profile moment applies with m_1=m_2=m. The inequality
|sum_(j=1)^k a_j|^2<=k sum_j |a_j|^2 reduces every derivative norm to
these moment bounds. Hence, for all j,k in {0,1},

\[
 \sum_{u\in\mathcal R}|\partial_\sigma^j\partial_h^kF_u|^2
 \le C U^{1+\epsilon}(1+|h|+|t_{\rm phys}|)^A,              \tag{5}
\]

uniformly in sigma on that enlarged compact interval. Here A is the
maximum of finitely many admitted height degrees; all retained physical
heights have magnitude O(T_1). Its choice precedes tau and any external
tail order. The moment inequalities, positive margins and family
conditions in the hypotheses must hold for the selected slots. In the
source Part II application kappa=2 beta_*-1, so the plain beta_* condition
holds by equality; this does not prove the assumed moment itself.

Cover the sigma interval and [-C_0 T_1,C_0 T_1] by unit rectangles.
There are O(1+T_1) rectangles, and each enlarged rectangle in
`eq:parameter-sobolev` has bounded area. Apply that inequality to each
smooth finite row polynomial, then sum its nonnegative derivative
integrals over rows and rectangles. Arbitrary rowwise selections satisfy

\[
 \begin{split}
 \sum_{u\in\mathcal B}|F_u(\sigma_u,h_u)|^2
 &\le\sum_{u\in\mathcal R}\sup_{\sigma,h}|F_u(\sigma,h)|^2\\
 &\le C U^{1+\epsilon}(1+T_1)^{A+1}.                       \tag{6}
 \end{split}
\]

No measurable selection of zeros or frequencies is required: for each
fixed physical tuple there are finitely many rows, and (6) holds for
every choice. Enlarging a parameter rectangle by a fixed constant is
allowed in the moment estimate, which has a global polynomial twist
cost; it is not an extension of a buffered reciprocal contour.

The O((log U)^2) choices of dyadic pair and finitely many presentation
labels cost only a preselected arbitrarily small power of U, after
distributing the epsilon losses. A slot subcollection is fixed within
each application. Near zero inverse capacity the no-slot amplification
contract applies to the common B_D with its rowwise clause and bounded
r range; no vanishing marked margin is used. Near zero plain capacity
the zero-slot plain contract applies. The source's fixed decrements,
mesh and optimized selection of those cases are not established by (6).

### Actual external tests and their traces

The physical Gaussian/Mellin factors are already checked in L533.
The additional tests in this interface are the witness H of (1), the
untwisted annular inverse/plain dyadic profiles B_D(y)y^(-sigma) and
W_2(y)y^(-sigma), and the prime test

\[
 V_{i,P,r_z}(y)=W_i(y)y^{r_z-1}/\log(P_i y),
       \qquad r_z=\Re z_{\rm phys}.                         \tag{7}
\]

For the dyadic inversion one may equivalently leave y^(-sigma) out of
the Mellin test and put sigma into the real L-argument, as in source
lines 4154–4161. Both conventions have compact real ranges. Translate
the pure norm twist into the arithmetic argument before applying decay.
If a Sobolev derivative profile is also needed, (4) adds only a fixed
logarithmic factor to these tests.

Each test is smooth on a fixed annulus. For (7), log(P_i y) is bounded
below by a positive multiple of log P_i for all sufficiently large Z,
since ell_i>0 is fixed. The identity

\[
 (y\partial_y)^j[\log(P_i y)^{-1}]
       =(-1)^j j![\log(P_i y)]^{-j-1}                       \tag{8}
\]

and Leibniz's rule give uniform seminorms for every fixed external order.
Thresholds and constants may depend on that order; no power P_i^(c j)
is introduced. Fixed real powers y^(r_z-1) are harmless on the annulus.
The fixed ray restriction is separated into a finite character sum;
the exact physical allowed support above supplies no hidden sharp
row-dependent weight. Natural row zeros stay in the original L-function
presentation, not in the test (7).

Put t_z=Im(z_phys). Mellin inversion of the normalized von Mangoldt sum
with weight V(y)y^(i t_z) has integrand

\[
  \mathcal MV(s)P_i^{s-it_z-1/2}
          \left(-\frac{L'_{\rm orig}}{L_{\rm orig}}ight)
                                      (s-it_z,\chi).         \tag{9}
\]

This follows directly by substituting the Mellin inversion of V and
collecting q_n and P_i powers on the absolute line. The k=1 terms are
the required primes; the prime-power correction is the separate absolute
count in `lem:bin-prime-bound`, not an extra external trace. Formula (9)
has imaginary arithmetic argument v_p-t_z, and scale modulus
P_i^(Re s-1/2). In particular t_z cannot disappear when the test is
declared untwisted.

For any of the annular tests V just named and compact real interval I,
`eq:pointwise-mellin-tail` gives

\[
 |\mathcal MV(\alpha+iv)|\le C_{I,L}(1+|v|)^{-L}
   \sum_{j=0}^L\int y^\alpha|(y\partial_y)^jV(y)|\,dy/y.    \tag{10}
\]

The rightmost sum is uniformly bounded. It proves pointwise decay on
joins, not merely integrated decay. These transforms are jointly
continuous in their real parameters and frequencies. Products with the
physical kernels of L533 and finitely many such densities therefore
meet its pointwise/Borel test condition, in the fixed changes of
coordinates appropriate to these tests. The complete list of arithmetic
arguments and its allocation remain inputs.

Specifically, inverse dyadic tails stay on Re(s+sigma)=2 and their joins
remain in the reciprocal buffer; plain joins use global numerator bounds;
prime tails stay on the absolute logarithmic-derivative line and their
joins use the allocated buffer. Both v_p and t_z occur in the single
allocation of L533. If it is |v_k|<=c_k T_1 with
c_k=1/[2m(1+max_j|a_jk|)], its already proved sum bound includes
v_p-t_z together with all other shifts. No later separation receives
another T_1/2 allowance. A trace extension of another axis is permitted
only if its arithmetic factors have the required global bounds or the
buffer restriction is retained.

### External orders, internal contracts and high-bin boundary

Fix the finitely many derivative profiles in (4)–(5), all internal moment
orders, and the global polynomial scale/height bounds first. Their
arithmetic realization is still an assumption. Choose tau>0 subject to
the detector height conditions. Only then choose the external order in
(2) or (10). For an already fixed bound Z^B(1+|v|)^J, L533 turns these
external pointwise estimates into tails and joins O_N(Z^B T_1^(-N)).
The derivatives fall on H, the untwisted dyadic tests or (7), never on
the recursive internal coefficient measure. Increasing N consequently
does not replace a moment profile by an N-dependent one or demand a
larger internal height moment. B and J remain fixed.

The source's `eq:indexed-coefficient-measure` explicitly requires a
common coefficient measure when passing a separated squared row norm
through an internal integral. Individual rowwise weighted L1 bounds
do not imply that condition. This lemma neither draws that implication
nor verifies each internal edge. Its fixed-block commonness proof is
for (1); its rowwise evaluations use (6). These are distinct operations.

Finally `lem:high-bin` assumes its pointwise cardinality bounds, and
forms amplitude/witness subdivisions only after continuing the full
fixed-bin correction. Equation (6) can support the moment applications
used to obtain such bounds when their other hypotheses hold. It does
not justify integrating separately defined row subsets or continuing
their individual correction pieces. High-bin lines 14921–14926 also
require complete auxiliary estimates including discarded integrals;
the present check of external tests does not prove that accounting.
Those distinctions, along with the complete coordinate list, full
correction construction, bootstrap, H construction and manuscript/import
closure, remain unresolved. No actual-Xi positivity statement follows.

## Mathlib

Full matching coverage for this conditional selection interface has not
been checked. Fourier/Mellin decay, finite sums, product differentiation
and Sobolev inequalities are supporting analytic ingredients, not a
claimed matching formal theorem for these arithmetic contracts. No Lean
certificate or independent arithmetic verification is claimed. This
audit uses exact inequalities and hypothesis checks; no numerical or
symbolic script is needed.
