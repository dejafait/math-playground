# L537 — Conditional canonical child admissibility and one-step energy loss

## Hypotheses

Use the arithmetic datum, primary representatives, zero-extended
characters and the two conditional Poisson interfaces of L535/L536.
Ideals and column indices are outside the fixed excluded set S; element
rows may be arbitrary nonzero elements of the source's Eisenstein ring.
All scalar lengths range over fixed bounded sets. Fix Z>1 sufficiently
large for the contracted full-support bounds, d>0, 0<eta<=d/16,
tau,pi>0, and a node with c_node>7eta. Fix nonnegative M,N,V,z_0 and put
F=N+V. The parent's puncture is exactly
rho(n)=1_{(n,r_rho)=1}, with r_rho squarefree and independent of the
current row and label. Write Q=log_Z q_(r_rho), and assume

\[
 F-M-Q-z_0\ge c_{\rm node},\qquad
 4F-3M-6z_0\ge c_{\rm node}.                         \tag{1}
\]

The parent has the exact coefficient class of the source's
`lem:canonical-moment`: bar(alpha)(n) gamma_2(n), a genuine fixed
multiplicative finite ray character with full defining modulus supported
on S, rho, the moving characters chi_n(k) chi_n(f)^4, and a product-form
mark. Explicitly, for a fixed subcollection I of disjoint prime lists,

\[
 \mathfrak d_I(n)=\sum_{(p_j)\in\prod_{j\in I}\mathcal P_j}
               \prod_{j\in I}a_j(p_j)1_{p_j\mid n}.       \tag{2}
\]

The individual coefficients are uniformly bounded and independent of
the current k,f. The slot number is at most a fixed K_s, and the sum
of the nominal slot lengths is at most z_0. The nonnegative parent
label weight depends on f alone and satisfies one fixed divisor-power
bound, uniformly in Z and all averaged variables. There is no extra
residual column coefficient, even a bounded one independent of k,f.

Consider one nonterminal block with ell+V>=d and r=N-3ell, and its
dyadic/ray/slot branches. All arithmetic, masked-Poisson, extraction,
source-projection, fixed full-support, fibre/count and principal/tail
contracts of L535/L536 remain hypotheses. In particular:

- The finite-ray factors produced by extraction are characters of the
  fixed source ray group (together with the parent's fixed modulus),
  supported on S. Moving coprimality zeros remain separate punctures.
- Every gamma=(q_0,t',r_g) in the distinct-triple projection Gamma_sigma
  has an actual source witness with d_2|g', r_g=g'/d_2 and
  b_1 b_2=q_0^2 J_2^2 s, J=sJ_2. The ideals s,J_2 are squarefree and
  coprime, and supp(rad(b_1 b_2)) is contained in supp(J q_0).
  Each b_a has center ell; J,t',g',d_2 have centers j,t,g,theta.
  Each corresponding actual logarithmic norm differs from its center
  by at most eta. A_i,V,t,j and all ideal centers are nonnegative.
- Original slot assignments and their priority masks are retained.
  Before positive enlargement, the second child label is J C d_2 v'
  and these factors are squarefree and pairwise coprime on nonzero
  outer support. The first extracted A_i divides rad(b_1 b_2).
- Fresh column and label windows are independent fixed compact
  normalized intervals, chosen before the Z threshold. The full fresh
  column window has |log_Z q_n-N_c|<=6eta; the full label window I_f
  has |log_Z q_f-V_c|<=4eta. The fresh column cutoffs have uniformly
  bounded smooth seminorms and support in [a,b], 0<a<=b, b>=1.
- The free arithmetic, divisor and dyadic losses in this one step
  admit a single aggregate allowance pi, as specified below. Principal
  and raw discarded-tail estimates retain their source bounds before
  formal extension and Fourier absolute values. After the prescribed
  exterior factors, the first principal term is O(Z^(M+pi)), the
  second is O(Z^(F+26eta+tau+pi)); discarded tails fit the claimed
  one-step allowance with finite seminorm and polynomial height costs.
  These estimates and their global simultaneous availability are not
  proved here.

Assume a uniform smaller-row estimate, **only** for admissible canonical
energies with the full coefficient/support hypotheses just stated,

\[
 0\le M'\le M-d,\quad N',V'\ge0,\quad F'=N'+V'\le F+11\eta,
 \quad\text{both margins}\ \ge c_{\rm node}-7\eta:
 \qquad \mathcal E'\ll Z^{F'+\epsilon_{\rm ch}},           \tag{3}
\]

where epsilon_ch>=0 is fixed. The estimate is uniform over frozen
outer ideals, moving moduli, the allowed label weights, and slot
subcollections, with dependence on finitely many test seminorms and
fixed polynomial dependence on norm-twist heights. The energy includes
Z^(-V') outside the label sum and Z^(-N'/2) inside the squared column.
Neither the parent canonical theorem nor its reduction conclusion is
assumed. Full induction, terminal estimates and initialization are not
asserted by (3).

## Conclusion

Every retained nonempty child in Gamma_sigma is in the exact canonical
class, with nonnegative M_ch,N_ch,V_c, row length M_ch<=M-d, and
F_ch<=F+11eta. Its two margins are at least
c_node+delta_N-5eta and c_node+4delta_N-7eta respectively, where
0<=delta_N<=6eta. Thus (3) applies.

Under precisely the retained contracts, the nonterminal block has
the one-step bound

\[
 \text{block}\ll Z^{F+40\eta+\tau+\pi+\epsilon_{\rm ch}}. \tag{4}
\]

The sharper branch allowance before maximizing the clipping error is
28eta+2delta_N+tau+pi. One exterior fixed-count normalization and one
normalized discrete mass occur. Fixed Fourier height orders add no
power of Z. This is conditional reproduction of the source's claimed
one-step reduction, not an improvement to its zeta result. Arithmetic,
terminal/initialization, global order choices, full induction and
actual-Xi signs remain unresolved here.

## Proof

Primary source: OpenAI, *The Quasi-Riemann Hypothesis: A Zero-Free
Half-Plane Re(s)>7/8*, September 30, 2026, commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
[build/paper.tex](https://raw.githubusercontent.com/openai/math/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex).
Exact locators are `old-eq:4.2`, `lem:canonical-moment`,
`eq:canonical-energy`, `eq:inverse-fixed-invariant`,
`eq:inverse-slot-priority`, `eq:inverse-cube-actual`,
`eq:second-poisson-lengths`, `eq:canonical-child-data` through
`eq:inverse-row-decrease`, `eq:inverse-positive-child`,
`eq:canonical-prefactor` and `eq:inverse-step-loss`, including the
following aggregate-loss paragraph. Retrieval ranges are 6819–6872,
8753–8796, 9230–9264, 9364–9487, 9700–9731, 10049–10138,
10274–10492 and 10702–10829. The fixed-ray provenance is stated in
`lem:fixed-gauss-phase` (860–898), with the first ray expansion at
9637–9654 and the second at 10285–10298. Its arithmetic proof remains
within the inherited contracts.

The source already claims (4). Reproduction here tests the application
of L535/L536 to its exact smaller-row hypothesis; simply importing
`lem:canonical-moment` for the parent would bypass that test.

### Canonical coefficients and independent variables

L536 gives, for each fixed pattern, gamma, and second mode zeta, the
column

\[
 Q_{a,\gamma,\zeta}(k,f)=\sum_{n\ {\rm sf}}
 \bar\alpha(n)\gamma_2(n)(\nu_i\bar\vartheta)(n)\rho_\gamma(n)
 \chi_n(k)\chi_n(f)^4\mathfrak d_{I'_a}(n)
 W'_a(q_n/Z^{N_{\rm ch}}),                              \tag{5}
\]

where
\[
 \rho_\gamma(n)=\rho(n)1_{(n,\operatorname{rad}(q_0)t'r_g)=1},\qquad
 W'_a(z)=\omega_{n,a}(Z^{\delta_N}z)z^{\varepsilon_a i\zeta_a}.
\]
Products and conjugates of genuine characters remain genuine
characters on a common fixed ray group. The source's Gauss phase
group has modulus supported over 2,3, contained in S; taking a common
multiple with the original fixed modulus adds no prime outside S.
Thus nu_i bar(vartheta) has the required full defining modulus.
q_0,t',r_g are not absorbed into that character.

The new radical is rad(r_rho q_0 t' r_g), fixed by gamma and the
parent data before either k or f is varied. This matches the required
indicator class; an arbitrary phase in place of rho would not.
L536's zero-extended identity converts the moving factors into exactly
chi_n(k)chi_n(f)^4, also at nonunits, without dividing by a vanishing
character. There is no additional b(n) or real root in (5).

For the marks, apply the retained priority identity slot by slot.
A surviving prime p|n originally had to avoid b_a,A_a,C,t', then
d_2,r_g,v'. On the original transformed support, its avoidance of
J,C,d_2,v' follows from chi_n(J C d_2 v')^4; its avoidance of
q_0,t',r_g follows from rho_gamma. Since A_a divides rad(b_1 b_2)
and the latter support lies in J q_0, the b_a,A_a exclusions also
follow. Hence every survival indicator is redundant *on the original
summand*, including when that summand is zero. The surviving mark
therefore equals (2) for I'_a, with its original lists and coefficients.
Assigned primes and their priority masks stay in the outer weight.
The fixed branch fixes which slots survive, independently of k,f;
it does not freeze the primes in a moving child label.

Now extend this same polynomial (5) to the full independent child
windows in the positive sum of L536. Added f need not contain the
old J or have any old parent reconstruction. No old survival identity
is applied to those added terms: (5) has already been identified on
the original terms, and is the canonical polynomial being extended.
This distinction prevents an invalid use of source-witness identities
on the enlarged domain. The cap remains z_0, even for an empty mark.

The label weight is D_(K_s)(f)=d_O(f)^(9+4K_s), with fixed K_s.
It depends on f alone and has a fixed divisor bound. C_(K_s)(gamma)
is in the triple measure, not in this label weight. Labels remain
squarefree outside S; rows include all nonzero elements in the ball,
with no new coprimality or squarefreeness requirement. A restriction
q_f/Z^V_c in I_f is a summation window, not a Z-dependent redefinition
of D_(K_s). If the canonical convention uses an enclosing fixed label
annulus, positivity gives the needed upper inequality there.

### Nonnegative lengths, witnesses and the two margins

For a selected first side i, abbreviate A_i by A and use the exact
definitions

\[
\begin{gathered}
 s_i=r-A-B-t,\quad H_c=2r-2B-M+4\ell+2V+\delta-j,\\
 N_c=s_i-g-v,\quad V_c=B+\theta+v+j,\quad
 F_c=r-A-t-g+\theta+j,\\
 M_c=2(s_i-g)-H_c+\delta+2\theta
     =M-4\ell-2A-2t-2g+2\theta-2V+j,\\
 M_{\rm ch}=M_c+\eta,\quad
 N_{\rm ch}=\max(0,N_c),\quad
 \delta_N=N_{\rm ch}-N_c,\quad F_{\rm ch}=F_c+\delta_N.
                                                               \tag{6}
\end{gathered}
\]

The nonempty row gate gives M_ch>=0, since every nonzero row has norm
at least one. V_c>=0 by its displayed summands. A nonempty fresh
column with N_c<0 has q_n>=1 and q_n/Z^N_c<=b; hence
Z^delta_N<=b, and the full-support logarithmic bound gives
delta_N<=6eta. For N_c>=0 both assertions hold with delta_N=0.
Thus W'_a has fixed support in [a/b,b]. Its Euler derivatives have
uniform bounds times fixed polynomials in |zeta_a|: Euler
differentiation of omega(Z^delta_N z) evaluates the same derivative
of omega at that argument. There is no unbounded real dilation cost.
These scales depend on centers only. Empty columns give zero and are
omitted. All independent full label bounds are the contracted support
bounds; no parent product identity is needed for them.

For each gamma choose a source witness solely to bound its fixed
puncture. Write hats for actual logarithmic norms, c_hat=log_Z q_(q_0),
and ell_pair_hat=(b_1_hat+b_2_hat)/2. The exact cube identity gives

\[
 2\widehat\ell_{\rm pair}
 =2\widehat c+2\widehat j_2+\widehat s,\quad
 \widehat j=\widehat s+\widehat j_2,
 \qquad \widehat c,\widehat j_2,\widehat s\ge0.
\]

Therefore c_hat<=ell_pair_hat and j_hat<=2ell_pair_hat.
Also theta_hat<=g_hat by actual divisibility. The individual eta
errors imply

\[
 g-\theta\ge-2\eta,\quad j\le2\ell+3\eta,\quad
 \widehat c\le\ell+\eta,\quad \widehat t\le t+\eta,
 \quad\log_Zq_{r_g}\le g-\theta+2\eta.                  \tag{7}
\]

Put D_c=ell+A+t+g-theta+V. Taking a radical can only decrease
the norm of the product, even with repeated prime factors. Thus

\[
 Q_\gamma\le Q+\widehat c+\widehat t+\log_Zq_{r_g}
 \le Q+\ell+t+g-\theta+4\eta\le Q+D_c+4\eta.             \tag{8}
\]

This holds for every member of Gamma_sigma. Count balls alone would
not give the bound on c_hat, so they are never used as the child domain.

Substituting r=N-3ell in (6), without changing the fixed F, gives

\[
\begin{gathered}
 F_c=F-D_c-2\ell+j,\qquad M_c=M-2D_c-2\ell+j,\\
 F_c-M_c=F-M+D_c,\\
 4F_c-3M_c=4F-3M+2(A+t+g-\theta+V)+j.                  \tag{9}
\end{gathered}
\]

Equations (1), (6), (8) give

\[
 F_{\rm ch}-M_{\rm ch}-Q_\gamma-z_0
 \ge c_{\rm node}+\delta_N-5\eta.
\]

The added term in the last line of (9) is at least -4eta by (7)
and nonnegativity of A,t,V,j. Subtracting 3eta for M_ch and adding
4delta_N gives the second margin
c_node+4delta_N-7eta. Both exceed or equal c_node-7eta>0.

Furthermore D_c>=ell+V-2eta and 2ell-j>=-3eta. Hence

\[
 M-M_{\rm ch}=2D_c+2\ell-j-\eta
 \ge2(\ell+V)-8\eta\ge2d-8\eta\ge3d/2\ge d.           \tag{10}
\]

Finally (9) gives F_c<=F-ell-V+5eta and consequently
F_ch<=F+11eta. Together with N_ch,V_c>=0, this bounds both child
column and label lengths in the required range. All hypotheses of
(3), including the original slot cap and independent windows, now match.

### Normalization, height integration and the single loss

Let H_(a,gamma) be L536's positive raw sum, with weight D_(K_s),
full label window I_f and row ball 0<q_k<=Z^M_ch. With these exact
domains, the definition of the canonical energy yields

\[
 \mathcal E_{a,\gamma}
 =Z^{-V_c}\sum_fD_{K_s}(f)\sum_k
          |Z^{-N_{\rm ch}/2}Q_{a,\gamma,\zeta}(k,f)|^2
 =Z^{-F_{\rm ch}}H_{a,\gamma}.                          \tag{11}
\]

A larger fixed canonical row ball or label annulus gives an upper
bound for H instead of equality. Applying (3) gives
H_(a,gamma)<=C(t,zeta) Z^(2F_ch+epsilon_ch), with C a fixed
polynomial in the heights times finitely many fixed test seminorms,
uniformly in gamma. One F_ch comes from (11); one comes from (3).

Use exactly L536's normalized measure

\[
 \nu_\sigma=Z^{-c_\sigma}
       \sum_{\gamma\in\Gamma_\sigma}C_{K_s}(\gamma)\delta_\gamma,
 \quad c_\sigma=C_c+11\eta/2,\quad
 C_c=\ell+R/2-j+t+g-\theta.
\]

Its contracted mass is O(Z^(pi_count+pi_fib)). Each of the two
square-root factors in L536 (17) is bounded using (11). Their product
is bounded by C(t,zeta) Z^(2F_ch+epsilon_ch) ||nu_sigma||, with
one mass, while their exterior normalizations contribute one
Z^c_sigma. The first and second exterior root factors are respectively
Z^(kappa_i+9eta/2) and Z^(lambda_c+18eta+tau), where

\[
 \kappa_i=M-2r-2\ell-V-\delta+A+B-R/2,\qquad
 \lambda_c=H_c-\theta-(s_i-g).
\]

Their exact cancellation is independently checked by substitution:

\[
\begin{split}
 \kappa_i+\lambda_c+C_c
   &=-r+3\ell+V+2A+2t+2g-2\theta-2j,\\
 2F_c&=2r-2A-2t-2g+2\theta+2j,\\
 \kappa_i+\lambda_c+C_c+2F_c&=r+3\ell+V=F.              \tag{12}
\end{split}
\]

For clarity about the nested first Cauchy step, put
dmu_1(t)=|Fhat_1(t)|dt and A_i(t)=Z^(kappa_i+9eta/2) S_i(t),
where S_i is the positive first norm from L535. Then

\[
 \int\sqrt{A_1(t)A_2(t)}\,d\mu_1(t)
 \le\prod_{i=1}^2\left(\int A_i(t)\,d\mu_1(t)\right)^{1/2}. \tag{13}
\]

Apply the second-transform bound separately inside each integral.
The child's finite seminorm cost is polynomial in zeta by the clipped
test estimate; any inherited polynomial t cost is fixed as well.
L536 (13) integrates precisely these costs against
|Fhat_1(t)| |Fhat_(2,t)(zeta)|, with zero additional Z exponent.
It also proves absolute integrability. Nonnegative bounds allow Tonelli;
no row-dependent choice of measure or unjustified signed interchange
is used. Constants may depend on finite requested orders; no exponent
of Z increases with those orders. This proves the one-step assertion
only; it does not fix orders for a whole recursive tree.

Combining (11)–(12), each branch inside (13), before its geometric
mean, has exponent at most

\[
 F+(9/2+18+11/2)\eta+2\delta_N+\tau
       +\pi_{\rm count}+\pi_{\rm fib}+\epsilon_{\rm ch}
 =F+28\eta+2\delta_N+\tau
       +\pi_{\rm count}+\pi_{\rm fib}+\epsilon_{\rm ch}. \tag{14}
\]

The external old-label and beta loss in L535 occurs once after (13).
The square roots do not double (14). Branch-dependent delta_N can
always be replaced by 6eta, giving 40eta. Neither real root is placed
in a child test again. J,C,d_2,v' are already in the child label sum
and its contracted fibre bound; old f,h have been removed by L535.
None is counted again.

Here is the precise aggregate use. Suppose J_step>=1 bounds the
number of free small-power uses and logarithmic factors in a branch,
including the finite unions, and L_pow bounds each scale-product
logarithmic length. The inherited contracts permit choosing each
free exponent <=pi/(2 J_step max(1,L_pow)). Their total scale loss
is <=pi/2. The product of the at most J_step logarithmic factors is
<=C Z^(pi/2) for sufficiently large Z. Thus pi_beta, pi_old,
pi_count, pi_fib and the dyadic-union losses together cost at most
pi. Fixed ray/slot-branch counts are constants. This checks the use
of the aggregate contract; it does not prove the adjustable arithmetic
estimates. No eta or tau is hidden in pi.

By (1), M<=F-z_0-c_node<F, so the contracted first principal
estimate fits (4). The second principal allowance 26eta+tau+pi
is smaller than 40eta+tau+pi+epsilon_ch. The retained discarded-tail
contracts fit as assumed. Finite sums and geometric means preserve
the same bound, yielding (4). This proves the conditional application
and no missing arithmetic contract or recursive base case.

## Mathlib

Full matching Mathlib coverage for this arithmetic canonical-child
interface has not been checked. Generic finite-group character algebra,
norm multiplicativity, Cauchy–Schwarz and integration are supporting
facts only. They do not certify the source's extraction, witness,
support, fibre/count, principal/tail or induction contracts. No absence
or formal-verification claim is made.
