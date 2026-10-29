# L297 — Leading infrared cancellation for the complementary covariance

## Hypotheses

Use exactly L296's SU(2) relative cube, with even N>=2, a=8/N,
Euclidean counting measure, boundary-contained links pinned, gauges
fixed at every boundary vertex, and every other link variable,
including both normal endpoint cases. Retain L282(1)'s exact reflected
product bump, all three colors, L279's Wilson normalization, and
L280's ambient all-link jets on its own relative-Coulomb slice. The
full density is D_N from L280(16), tensored with the color identity.
No boundary replacement, counterterm, running vertex, longitudinal
Gaussian variable, or effective-action identification is assumed.

On the fixed one-color transverse space H=ker B*, let Q be an
orthonormal inclusion and use L296(1)'s matrices

\[
 A=Q^*C^*CQ,\qquad K_i=Q^*C^*\operatorname{diag}(h_i)CQ,
 \qquad A(s,t)=A-sK_--tK_+,\quad i\in\{-,+\}.
 \tag{1}
\]

Here C is the relative plaquette incidence. Sources are real in
(|s|+|t|)F<eta<1, F=||f_*||_infinity. In particular 0<=K_i<=F A
and A(s,t)>0. Define the extended edge covariances

\[
 G(s,t)=QA(s,t)^{-1}Q^*,\quad
 H_r(s,t)=QA(s,t)^{-1}e^{-rA(s,t)}Q^*,\quad
 \mathcal C_r(s,t)=G(s,t)-H_r(s,t).
 \tag{2}
\]

All covariance slots below include the color identity. With exactly
L280(19)'s contractions and affine tensors T(s,t), U(s,t), put

\[
 R_N(X;s,t)=\tfrac1{12}\mathcal B(T(s,t),T(s,t);X,X,X)
       -\tfrac18\mathcal U(U(s,t);X,X)
       +\operatorname{Tr}(D_N X),
\]
\[
 \tau_N(r)=\left.\partial_s\partial_t
  \{R_N(G(s,t);s,t)-R_N(\mathcal C_r(s,t);s,t)\}\right|_{0,0}.
 \tag{3}
\]

The notation D_N in the trace includes all three colors. In every
source derivative, r is held fixed, including at

\[
 \lambda_0=12\sin^2(\pi/(2N)),\quad
 \theta_N=\tfrac32\log N,\quad r_N=\theta_N/\lambda_0.
 \tag{4}
\]

Use the audited local results L282(18) for the complete density,
L283(17) for the contracted quartic operator, L287(12)--(13) for
the cubic curl energies, and L289(12),(16) for the internal-curl
operator and its integral identity. These are applied to the same
sampled smooth ground modes, not imported as estimates of (3).
L296 supplies the relative spectral gap, heat-line estimates and
complete all-tail bounds. L291's uncut cancellation is not an input.

## Conclusion

The complete complementary-covariance response passes the specified
necessary leading-order test:

\[
 \boxed{\displaystyle
 \frac{\tau_N(r_N)}{N^{1/2}(\log N)^2}\longrightarrow0
 \quad(N\longrightarrow\infty,\ N\text{ even}).}
 \tag{5}
\]

The mixed Wilson lines cancel the coefficient of L296's negative
infrared term. This is a statement about the entire expression (3),
including both source derivatives of the heat factor, both insertion
tensors and the full density. Terms containing at least two H_r lines
have mixed response tending to zero at r_N; no difference of uncontrolled
uncut asymptotic errors is used.

Equation (5) gives neither a rate for its little-o, a bounded tail,
an O(1) shell estimate, nor a quantitative bound for the uncut kappa_a.
It establishes no uniform higher perturbative remainder, interacting
reflection lower bound, nonzero continuum theory satisfying the field
axioms, or positive infinite-volume mass. This is a new local
specialization within the saved EXPLORE target, not a claim of
originality beyond the sources checked. The separate conceptual audit
in section 7 accepts (5) under these inputs; this is not a complete-solution
candidate and does not audit the upstream inputs afresh.

## Proof

### 1. Covariance hypotheses and the exact mixed polynomial

For a positive eigenvalue x of A(s,t), both x^-1 exp(-rx) and
x^-1(1-exp(-rx)) are positive when r>0. Thus H_r and mathcal C_r
are positive on H and zero on its orthogonal complement, and their
sum is G. At r=0 the second covariance is zero, which is permitted
as a positive semidefinite covariance. All are analytic in the
source variables near zero at each fixed N and fixed r.

The finite Wick and covariance-addition inputs are
Bauerschmidt--Brydges--Slade, *Introduction to a Renormalisation
Group Method*, LNM 2242 (2019),
[arXiv:1907.05474v2](https://arxiv.org/pdf/1907.05474v2),
Propositions 2.1.6 and 2.1.9 and Corollary 2.1.11, printed pp. 31--33.
They apply to finite real symmetric positive semidefinite covariances,
including singular support. The verified positivity above and the
fixed transverse inclusion meet these hypotheses, with no added
longitudinal integration. Polynomial Wick contraction, rather than
convergence of an exponential of truncated vertices, is all that is
used. The cubic internal color contractions vanish as in L280(19).
No general Gaussian theorem is reproved here.

For arbitrary symmetric covariance slots, define the operator
contractions on edge/color indices by

\[
 \mathcal E(T_w,T_v;X,Y)_{il}
   =\sum_{j,k,m,n}(T_w)_{ijk}(T_v)_{lmn}X_{jm}Y_{kn},\qquad
 \mathcal A(U_w;X)_{ij}=\sum_{k,l}(U_w)_{ijkl}X_{kl}.
 \tag{6}
\]

Thus mathcal B(T_w,T_v;Z,X,Y)=Tr(mathcal E(T_w,T_v;X,Y)Z)
for symmetric Z; this follows by its index sum even when mathcal E
is not symmetric. The tensors are fully symmetric in their slots.
Put, retaining all source arguments,

\[
 W_N(s,t)=D_N+\tfrac14\mathcal E(T(s,t),T(s,t);G(s,t),G(s,t))
                   -\tfrac14\mathcal A(U(s,t);G(s,t)).
 \tag{7}
\]

In (7) D_N again includes the three colors. Expanding the two
polynomials in (3) gives the exact identity

\[
 \begin{split}
 R_N(G;s,t)-R_N(G-H;s,t)
 ={}&\operatorname{Tr}(W_N H)
     +\tfrac18\mathcal U(U;H,H)\\
   &-\tfrac14\mathcal B(T,T;H,H,G)
     +\tfrac1{12}\mathcal B(T,T;H,H,H),\qquad H=H_r(s,t).
 \end{split}
 \tag{8}
\]

Indeed the cubic difference has multiplicities 3,-3,1 and the
quartic difference 2,-1. This retains all mixed assignments before
differentiation. It is an identity for the registered scalar
polynomial, not an identification with a Wilsonian effective action.

### 2. Uniform energy bounds for every required source derivative

Let ell_N=log(eN) and, on H with colors, J_N=I+ell_N A. Operators
on edges in this section are compressed by Q when used with J_N.
For alpha equal to the empty set, {-}, {+}, or {-,+}, write a
subscript alpha for the corresponding zero-source derivative.
There is a constant independent of N such that

\[
 \|J_N^{-1/2}(W_N)_\alpha J_N^{-1/2}\|\le C_F,
 \qquad \|(W_N)_\alpha\|\le C_F\ell_N.
 \tag{9}
\]

Here is the full source accounting and the proof of these bounds.
On H put M_i=A^-1/2 K_i A^-1/2, so ||M_i||<=F. The covariance
derivatives, extended by Q when necessary, have the form

\[
 G_\alpha=G^{1/2}Z_\alpha G^{1/2},\quad
 Z_\varnothing=I,\quad Z_i=M_i,\quad
 Z_{-+}=M_-M_++M_+M_-.
 \tag{10}
\]

Both inverse orders are present. Inverses or square roots of the
singular extended G mean restriction to H. In (10), the corresponding
conjugation on H is understood, so ||Z_alpha||<=max(1,F,2F^2).
In particular |(G_alpha)_{ef}|<=30||Z_alpha|| by L280's bounded
diagonal and Cauchy--Schwarz, also on every normal endpoint.

For a bounded real plaquette weight w, T_w is the exact cubic jet
of sum_p w_p(Cx)_p dot zeta_p(x). L287's argument, with the weight
specialization proved in L296 section 4, gives

\[
 \|(G^{1/2}\otimes G^{1/2})T_w[u,\cdot,\cdot]\|^2
 \le C\|w\|_\infty^2
       (\|u\|^2+\ell_N\|Cu\|^2).
 \tag{11}
\]

The tensor norm is exactly the quadratic form of
mathcal E(T_w,T_w;G,G). The weights enter L287's curl coefficient
vector and conjugate its positive Schur-product matrix by diag(w);
the full plaquette/edge multiplicities are unchanged. Thus (11)
applies to 1, h_-, h_+, with the latter two extended by zero to
other orientations. Tensor-product Cauchy--Schwarz now yields, for
X=G^1/2 Z_X G^1/2 and Y=G^1/2 Z_Y G^1/2,

\[
 \|J_N^{-1/2}\mathcal E(T_w,T_v;X,Y)J_N^{-1/2}\|
 \le C\|w\|_\infty\|v\|_\infty\|Z_X\|\|Z_Y\|.
 \tag{12}
\]

This holds also for signed X,Y and unequal tensors; it does not
discard cross terms or use positivity of a source derivative.

For precision, every source derivative of the cubic operator in
(7) is the following finite sum over disjoint labeled subsets:

\[
 \partial_\alpha\mathcal E(T,T;G,G)
 =\sum_{\alpha_1\sqcup\alpha_2\sqcup\alpha_3\sqcup\alpha_4=\alpha}
       \mathcal E(T_{\alpha_1},T_{\alpha_2};
                         G_{\alpha_3},G_{\alpha_4}).
 \tag{13}
\]

Here T_empty=T, T_i=-T_{h_i}, and T_{-+}=0; the same convention
holds for U. Distinct placements of the two labels are counted
separately. Equations (10)--(12) bound each term uniformly in the
J_N form norm. Thus neither the two insertion derivatives nor any
internal inverse derivative has been suppressed.

For the quartic operator the analogous two-factor product rule is
sum_{alpha_1 disjoint-union alpha_2=alpha}
mathcal A(U_{alpha_1};G_{alpha_2}). L283(9)'s constant
C_U=sup_i sum_{jkl}|U_ijkl| is uniform; a bounded weight multiplies
it by at most ||w||_infinity. The entry bound following (10) and
the symmetric row-sum bound therefore give a uniform operator norm
for every such term. The full D_N has norm <=241/4 and has zero
nonempty source derivatives. This proves the first part of (9).
Finally ||A||<=16, so ||J_N||<=1+16ell_N, proving the second.

These estimates are for complete finite-domain tensors, not just
bulk rows. They also imply the useful bound

\[
 \|\widehat A^{-1/2}(W_N)_\alpha\widehat A^{-1/2}\|\le C_F,
 \qquad \widehat A=A/\lambda_0,
 \tag{14}
\]

because J_N=I+ell_N lambda_0 widehat A, widehat A>=I, and
sup_{N>=2} ell_N lambda_0<infinity.

### 3. The complete zero-source ground compression

Let P_N be the rank-four one-color ground projection of L296
section 2. L003 section 2's exact interval sine/cosine normalization
makes each sampled continuum ground mode have unit physical norm,
with inner product a^4 times the edge sum. Multiplication by a^2
therefore gives its unit counting vector, on its actual vertex and
midpoint grids, including the own-direction constant cosine mode.
Thus the strong physical-norm limits L282(18), L283(17), and
L289(12) apply to its counting-normalized vectors. For their
one-color blocks they give, after compression by P_N,

\[
 D_N\longrightarrow d_*I,\qquad
 \mathcal A(U;G)\longrightarrow a_*I,\qquad
 E_N^{\rm int}\longrightarrow e_*I,
 \tag{15}
\]
\[
 d_*=-\tfrac18-I_1,\qquad
 a_*=8Z_0-\tfrac32+4I_1,\qquad e_*=24I_1.
 \tag{16}
\]

The norm assertions in (15) are only on the four-dimensional ground
space. They do not assert operator-norm convergence on the entire
lattice. The cited local proofs control all boundary layers by
uniform polynomial approximation before taking their smooth-field
limits. Their hypotheses are exactly the domains, tensors and
normalizations of (1)--(3), so no new boundary specialization is needed.

It remains to replace E_N^int by E_N=mathcal E(T,T;G,G).
For u,v in the colored ground space, ||Cu||=sqrt(lambda_0)||u||.
L287(12)--(13), with DV[u]=mathsf A(u;x)+mathsf B(u;x), gives

\[
 |u^*(E_N-E_N^{\rm int})v|
 \le C\{\ell_N\lambda_0+\sqrt{\ell_N\lambda_0}\}
                           \|u\|\|v\|\longrightarrow0.
 \tag{17}
\]

Indeed the difference is twice the sum of the A/A, A/B and B/A
Gaussian pairings; their L2 bounds are respectively
C ell_N lambda_0, C sqrt(ell_N lambda_0), and the same reversed.
This retains the external-curl part of the actual cubic vertex.
Global color rotations make D_N, mathcal A, E_N and W_N scalar
in color, as in L283 and L287. Write W_N^(0) for the one-color
block of W_N(0,0) compressed to H. Equations (15)--(17) imply

\[
 \|P_NW_N^{(0)}P_N-w_*P_N\|\longrightarrow0,
 \quad w_*=d_*-\tfrac14a_*+\tfrac14 e_*
           =\tfrac14-2Z_0+4I_1=0.
 \tag{18}
\]

The last equality is precisely L289(16)'s already justified
identity I_1=Z_0/2-1/16. Its proof checks the vanishing small-sphere
flux at the Brillouin singularity; no new integration by parts
assumption is made. Thus this cancellation uses Wilson-specific
quartic and cubic constants with the full density, not generic
gauge identities and not L291's uncut response.

### 4. Both heat-source orders and the entire spectral remainder

We need a norm form of L296's contour argument because W_N has
norm O(ell_N), not a uniform unweighted operator bound. Put
theta=r lambda_0>=1, f_theta(z)=exp(-theta z)/z, and
B_i=K_i/lambda_0=widehat A^1/2 M_i widehat A^1/2.
Use the low circle |z-1|=1/12 and the high rays
z=7/6+u +/- iu, u>=0, exactly as in L296(12)--(14).
The spectral gap is from 1 to at least 4/3, with all relative
sectors and both normal endpoints included.

The imported finite matrix inputs are Higham--Lin, *Matrix
Functions: A Short Course*,
[MIMS EPrint 2013.73](https://eprints.maths.manchester.ac.uk/2067/1/paper.pdf),
section 3.1.3, Definition 3.3, p. 6, and Schweitzer,
*Integral representations for higher-order Frechet derivatives of
matrix functions*,
[arXiv:2203.03930v1](https://arxiv.org/pdf/2203.03930v1),
section 2.1, Lemma 1 and Theorem 2, pp. 2--3. The contours enclose
the stated spectral sets, exclude zero for f_theta, and remain
valid on L296's fixed complex source polydisc. The second derivative
has both ordered resolvent products. In the convention A-sK_--tK_+,
the first resolvent derivative is -R B_i R and the mixed derivative
is R B_- R B_+ R+R B_+ R B_- R. No scalar differentiation of a
noncommuting matrix function is used.

Write R_z=P_N/(z-1)+S_N(z) on the low circle. The gap gives uniform
bounds for widehat A^1/2 S_N(z) widehat A^1/2 and for its needed
z derivatives. Inserting B_i=widehat A^1/2 M_i widehat A^1/2
shows that every coefficient with a P_N factor in a first or
mixed resolvent derivative has bounded trace norm even after
multiplication by widehat A^1/2 at both outside ends. Each such
coefficient has rank at most four. For example the mixed products
S_N B_i S_N B_j P_N and S_N B_i P_N B_j S_N factor, after that
weighting, into bounded factors widehat A^1/2 S_N widehat A^1/2,
M_i, M_j and P_N. Products with two P_N factors and their one
z derivative have the same property. This covers all six placements
other than the all-P and no-P products for each source order.

The all-P products have pole order three. Products with two P_N
factors have pole order two and those with one have pole order one;
the no-P product is analytic inside the circle. Consequently, for
the one-color covariance on H, its low part satisfies

\[
 \lambda_0(H_{-+})^{\rm lo}
 =\tfrac12 f_\theta''(1)
  (P_NB_-P_NB_+P_N+P_NB_+P_NB_-P_N)+L_{-+},
\]
\[
 \|\widehat A^{1/2}L_{-+}\widehat A^{1/2}\|_1
      \le C_F(1+\theta)e^{-\theta},\quad
 \|\widehat A^{1/2}\lambda_0(H_i)^{\rm lo}
                         \widehat A^{1/2}\|_1
      \le C_F(1+\theta)e^{-\theta},\quad
 \lambda_0H^{\rm lo}=f_\theta(1)P_N.
 \tag{19}
\]

Here ||.||_1 is trace norm. In particular the residue estimate uses
f_theta(1), f_theta'(1), and f_theta''(1), rather than the largest
value of f_theta on the low circle. The latter would lose an
exponential factor. The coefficients for double poles also include
the z derivatives of their analytic factors, controlled above.

For the entire high part, including its first and mixed source
derivatives, L296(14) and its separate audit prove

\[
 \|\lambda_0(H_\alpha)^{\rm hi}\|_1
             \le C_F e^{-7\theta/6},\qquad |\alpha|\le2.
 \tag{20}
\]

Specifically Tr(widehat A^-3)<=C uniformly, from the relative
four-dimensional mode count. On the fixed complex source polydisc
the inverse has uniformly bounded Schatten-3 norm, and its cube
and source derivatives have uniformly bounded trace norm. The high
functional calculus is widehat A(s,t)^-3 times the integral of
z^2 exp(-theta z)(z-widehat A(s,t))^-1. The resolvent and both
source derivatives have operator norm <=C/(1+|z|). Trace ideal
bounds reduce the complete integral to
C int_0^infinity (1+u)exp(-theta(7/6+u))du. This is (20), with
no lattice-dimension factor. The source dependence of the spectral
split itself is included by differentiating the fixed contours.

The finite-dimensional trace/ideal inequalities used here are those
cited in L296's audit: Watrous, *The Theory of Quantum Information*,
[2018 draft](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf),
section 1.1, pp. 32--33, (1.165)--(1.175), together with Schatten
Holder as stated by Ponge, *Introduction to Noncommutative Geometry*,
[Summer 2025, chapter 4](https://raphaelponge.org/wp-content/uploads/2025/07/summer-chap4-1.pdf),
slide 56. They apply to these finite complex matrices with
dimension-independent constants; the spectral count and contour
bounds are the local input, not consequences of fixed-dimensional
analyticity alone.

Combining (19)--(20), using widehat A>=I, also gives the convenient
unweighted bounds

\[
 \|H_\alpha\|_1
      \le C_F\lambda_0^{-1}(1+\theta)^{|\alpha|}e^{-\theta},
                  \qquad |\alpha|\le2.
 \tag{21}
\]

All formulas in (19)--(21) tensor with the three-color identity;
this changes trace-norm constants by a factor three.

Now differentiate the first term of (8). The complete result is

\[
 \partial_-\partial_+\operatorname{Tr}(W_NH)
 =\operatorname{Tr}(W_NH_{-+}+(W_N)_-H_+
                          +(W_N)_+H_-+(W_N)_{-+}H).
 \tag{22}
\]

For each low remainder, use (14) against the weighted trace norms
in (19). For every high term, use ||(W_N)_alpha||<=C_F ell_N
against (20). Define

\[
 b_N=\operatorname{Tr}_{H}
       (W_N^{(0)}P_NB_-P_NB_+P_N).
 \tag{23}
\]

Transposition and trace cyclicity make the two all-P traces equal,
since W_N^(0), B_i and P_N are real symmetric. Hence (22) is

\[
 \frac3{\lambda_0}e^{-\theta}(\theta^2+2\theta+2)b_N
 +O_F\!\left(\lambda_0^{-1}
      \{(1+\theta)e^{-\theta}+\ell_Ne^{-7\theta/6}\}\right).
 \tag{24}
\]

The factor three is exactly the color trace; each ordered all-P
residue has f_theta''(1)/2. There is no extra source-order factor.
Since ||P_N B_i P_N||<=F and the rank is four, (18) implies
|b_N|<=4F^2||P_NW_N^(0)P_N|| -> 0. This is the only qualitative
operator limit required for the leading coefficient; no convergence
rate is tacitly assumed.

### 5. Every term with two or three heat lines

The mixed derivatives of the last and the quartic terms of (8)
are, respectively, L296's complete all-tail cubic response and the
negative of its complete all-tail quartic response. Therefore at
r=r_N their bounds are

\[
 O(N^{-1/20}\log(eN)^3),\qquad
 O(N^{-17/20}\log(eN)^2),
 \tag{25}
\]

and both tend to zero. These imported bounds retain every insertion,
all covariance derivatives, and every finite-domain vertex.

The remaining term mathcal B(T,T;H,H,G) needs a different estimate
from the crude O(N^4) tensor norm. Use c=9/10 and
m_r=1+log(1+16r). L296(16) gives, in the G-relative norm,

\[
 \|G^{-1/2}H_\beta G^{-1/2}\|
       \le C_Fm_r^{|\beta|}e^{-c\theta},\qquad |\beta|\le2.
 \tag{26}
\]

For beta empty, the sharper exp(-theta) bound also implies (26).
Any term in its complete mixed derivative has two weighted cubic
tensors and covariance slots H_alpha,H_beta,G_gamma, with disjoint
derivative labels in all five factors. At most two labels in total
are distributed among those factors. All tensor derivatives are
the signed T_h or zero specified in (13), and G_gamma includes
both orders if it receives both labels.

Regard H_alpha as the outside trace line. Equations (10),(12),(26)
bound the internal contraction E'=mathcal E(T_w,T_v;H_beta,G_gamma)
by ||J_N^-1/2 E' J_N^-1/2||<=C_F m_r^|beta| exp(-c theta).
The trace ideal inequality and (21) then give

\[
 \begin{split}
 |\operatorname{Tr}(E'H_\alpha)|
 &\le C_Fm_r^{|\beta|}e^{-c\theta}
                          \|J_N^{1/2}H_\alpha J_N^{1/2}\|_1\\
 &\le C_F\lambda_0^{-1}\ell_N
     m_r^{|\beta|}(1+\theta)^{|\alpha|}e^{-(1+c)\theta}.
 \end{split}
 \tag{27}
\]

This permits signed differentiated heat lines and unequal vertices.
The finite product rule assigns each of two labeled derivatives to
one of five factors, counting all placements; terms with two
derivatives on one affine tensor vanish. Since the total derivative
degree is two, summing (27) yields

\[
 |\partial_-\partial_+\mathcal B(T,T;H,H,G)|
 \le C_F\lambda_0^{-1}\ell_N(1+\theta+m_r)^2
                                      e^{-(1+c)\theta}.
 \tag{28}
\]

At r_N, lambda_0^-1=O(N^2), m_r=O(log(eN)), and
exp(-(1+c)theta_N)=N^-57/20. Thus (28) is
O(N^-17/20 log(eN)^3), which tends to zero. No covariance line,
source assignment, or boundary layer in this mixed term is dropped.

### 6. Comparison with the required scale

At r_N the two explicit remainders in (24) are, respectively,
O(N^1/2 log(eN)) and O(N^1/4 log(eN)). Both are
o(N^1/2(log N)^2). Its leading factor divided by that scale tends
to 9/(4pi^2), multiplying b_N->0. The remaining terms of (8)
tend to zero by (25),(28). This proves (5) for the complete response.

Equivalently, L296's compressed sources converge to mathsf B, and
the potential leading constant of (3) is

\[
 \frac9{4\pi^2}\operatorname{Tr}(\mathsf B^2)
        (d_*-a_*/4+e_*/4)=0.
 \tag{29}
\]

The density alone still contributes L296's strictly negative constant.
Its cancellation here comes from one internally uncut covariance in
the quartic term and two in the cubic term of (7). It does not revise
or contradict the bare all-tail
obstruction. All limits above keep r fixed during differentiation
and only subsequently set r=r_N; all high-spectrum and mixed-line
errors are uniform in N. The qualitative compression (18) has no
proved rate, so (5) cannot be upgraded to a bounded terminal term
or to a logarithmic uncut estimate. The independent higher-remainder,
interacting, continuum and mass gaps remain unchanged.

### 7. Separate conceptual audit (2026-10-28)

This RESEARCH / REPRODUCTION audit accepts (5), conditional on the
stated canonical inputs. It independently checks the new uniform
specializations in (9)--(14), (17)--(24) and (26)--(28). The standard
inputs remain the precisely cited BBS Propositions 2.1.6/2.1.9 and
Corollary 2.1.11 in section 1, Higham--Lin Definition 3.3 and
Schweitzer Lemma 1/Theorem 2 in section 4, and the trace-ideal and
Schatten inequalities cited there. Their finite-dimensional hypotheses
are satisfied as checked below; none supplies the uniform Wilson
estimates by itself. No new external theorem or stronger conclusion
is imported.

**Source domain, normalization and full polynomial.** On the fixed
transverse space, A(s,t)>=(1-(|s|+|t|)F)A>0 for real sources in
the specified domain. Functional calculus therefore makes both
pieces of (2) positive; their extended singular covariances are
permitted by the finite Gaussian inputs. The tensors are the same
ambient all-link jets as in L280(19), not extensions chosen after
restriction. Alternating color contracts every cubic tadpole to zero
for all three scalar-in-color covariance slots. Symmetry in the
three slots gives cubic difference coefficients 3,-3,1; symmetry
in the two quartic slots gives 2,-1. With the factors 1/12 and -1/8
these are exactly (7)--(8), including the density with coefficient one.
Neither a source-dependent transverse projection nor an additional
Gaussian normalization is differentiated.

**Every source derivative of the one-line operator.** On H, (10)
follows from differentiating the inverse: the mixed derivative is
the sum of the two ordered products, irrespective of commutation.
For a test vector u, let F_w(u) be T_w[u,.,.] transformed by G^(1/2)
in its two remaining slots. L287(12)--(13) and L296 section 6's
bounded-weight specialization give
||F_w(u)||^2<=C||w||_infinity^2 <u,J_N u>.
For arbitrary vectors u,v the contraction in (12) is the pairing
of F_w(u) and (Z_X tensor Z_Y)F_v(v). Cauchy--Schwarz proves (12)
as a bilinear operator bound, including signed slots and unequal
vertices. It does not require their contraction operator to be positive.

The two derivative labels in (13) independently choose one of four
factors. Of the sixteen assignments, the two with both labels
on one affine tensor vanish by affinity; both inverse orders are retained when
one covariance receives both labels. For the quartic contraction,
the bounded row sum of its exact finite local tensor and
|(G_alpha)_{ef}|<=30||Z_alpha|| give the uniform row and column
bounds, also for its signed mixed inverse derivative. D_N contributes
only at derivative degree zero. Thus (9) holds on the full domain.
Since J_N and Ahat commute,
||J_N^(1/2)Ahat^(-1/2)||^2
=||Ahat^(-1)+ell_N lambda_0 I||<=1+ell_N lambda_0.
This verifies (14); it is not an unjustified removal of energy weights.

**Ground-space applicability and Wilson constants.** L003 section 2
puts the own-direction constant cosine on all N normal midpoints
and the other three sine modes on interior vertices. Each physical
ground vector has exactly unit a^4 counting norm and divergence
zero, so its unit counting vector is a^2 S_a psi_mu in H. These
four fixed smooth fields meet the full-grid hypotheses of L282(18),
L283(17) and L289(12); multiplication by a^2 converts each physical
error exactly into its counting error. Their fixed-rank compression
limits therefore apply without a boundary omission. The original
proofs' fixed-polynomial-then-mesh limits are retained; no simultaneous
limit or quantitative rate is inferred.

In L287(13), the factor two relates E_N to the Gaussian pairing of
DV. Removing its external-curl part leaves precisely E_N^int of
L289, with the same factor two. On a ground vector ||Cu||^2=lambda_0||u||^2.
The A/A term is O(ell_N lambda_0) and each A/B term is
O(sqrt(ell_N lambda_0)); polarization proves (17) for all ground
pairs. The scalar color blocks and the constants in (16) consequently
give d_*-a_*/4+e_*/4=1/4-2Z_0+4I_1=0 by L289(16).
This verifies (18) without appealing to L291 or a source-sandwich-only
convergence statement.

**All low poles with outside energy weights.** Put P=P_N,
D=Ahat^(1/2) and V(z)=D S_N(z) D. The spectral gap gives uniform
bounds for V and V' on and inside the low circle. Also DP=PD=P
and B_i=D M_i D. After multiplication by D on both outside ends,
the analytic coefficients of the six nonleading pole terms for each
ordered pair (i,j) have the following exact forms:

| Resolvent factors | Energy-weighted coefficient |
| --- | --- |
| P B_i P B_j S_N | P M_i P M_j V |
| P B_i S_N B_j P | P M_i V M_j P |
| S_N B_i P B_j P | V M_i P M_j P |
| P B_i S_N B_j S_N | P M_i V M_j V |
| S_N B_i P B_j S_N | V M_i P M_j V |
| S_N B_i S_N B_j P | V M_i V M_j P |

Each coefficient has rank at most four and uniform norm. The first
three have double poles and need the derivative of their sole V;
these derivatives have the same rank and bound. The last three
have simple poles and need only their values at 1. Thus their
residues use only f_theta' and f_theta, giving the weighted
O((1+theta)e^-theta) remainder in (19). The all-P term has residue
f_theta''(1)/2; the all-S term is analytic and integrates to zero.
Both ordered pairs are included. For the first source derivative,
the all-P double pole gives -f_theta'(1)P B_i P; its two cross
terms have weighted coefficients P M_i V and V M_i P and simple
poles. This verifies every bound in (19), including the outside
weights that were not present in L296's density-only application.

**Whole high spectrum and the differentiated trace.** L296 section 6
proves uniform resolvent estimates on a fixed complex source polydisc
for the same low circle and high rays. In particular, the first and
mixed derivatives of the high resolvent have norm O((1+|z|)^-1).
The relative mode count gives ||Ahat^(-1/2)||_6<=C. Factoring the
perturbed inverse through the bounded matrix
(I-sM_--tM_+)^-1 gives a uniform Schatten-3 inverse norm, hence a
uniform trace norm for its cube. Cauchy's formula on a smaller
fixed polydisc gives the same trace bound for its needed derivatives.
In (20) the high integral therefore has bound
C integral_0^infinity (1+u)e^(-theta(7/6+u))du,
including every product-rule placement. This is O(e^(-7theta/6))
for theta>=1 with no dimension factor. The calculus excludes zero;
the fixed contours differentiate the moving spectral subspaces too.

Pair the low weighted trace norms with (14), and the high trace
norms with (9). The four terms in (22) are exhaustive. Only W H_-+
has an all-P triple pole. Transposing the full real matrix product
and cycling its trace makes the two ordered traces equal without
assuming B_- and B_+ commute. Each carries the half residue, and
there are exactly three equal color blocks. This gives (24) with
the stated factor three, not six. Finally the rank-four trace bound
|b_N|<=4F^2||P_N W_N^(0)P_N|| proves b_N->0 and uses no rate.

**Signed multiple-heat-line terms.** In each product-rule term for
B(T,T;H,H,G), choose either heat slot as the outer trace. The other
heat slot has G-relative norm bounded by (26); the uncut slot has
bounded G-relative norm by (10), even when it receives both labels.
The already verified bilinear bound (12) thus applies to E' in (27).
For a signed outer slot, the ideal property, without any positivity
assumption, gives
||J_N^(1/2) H_alpha J_N^(1/2)||_1
<=||J_N|| ||H_alpha||_1.
Using (21) yields exactly (27), with only one ell_N loss. Each of
the two labels chooses one of the five factors; the two same-affine-
tensor assignments vanish and all other placements are bounded by
(27), with |alpha|+|beta|<=2. Hence their complete finite sum obeys
(28). No summation over edge coordinates is added to this trace-ideal
bound, so there is no hidden O(N^4) factor. The remaining H,H and
H,H,H expressions are exactly the complete all-tail inputs in L296,
with the quartic sign reversed, as recorded in (25).

At theta_N=(3/2)log N, the mixed H,H,G exponent is
2-(19/10)(3/2)=-17/20, with at most three logarithms. The other
two exponents are -17/20 and -1/20 with two and three logarithms.
All three contributions tend to zero. The two one-line remainders
in (24) are O(N^(1/2)log(eN)) and O(N^(1/4)log(eN)), smaller than
the required N^(1/2)(log N)^2 scale. Using lambda_0~3pi^2/N^2,
the normalized leading factor is 9/(4pi^2) times b_N->0.
This accepts the complete response (5), not only its formal ground
coefficient. Throughout, r is fixed during differentiation and is
set to r_N afterwards. The audit gives no quantitative compression
rate, bounded tail, stronger uncut estimate or uniform higher remainder;
the interacting construction, continuum axioms and mass gap remain open.

## Mathlib

Full matching Mathlib coverage for this complementary-covariance
Wilson response has not been checked. No absence or formal-verification
claim is made. The finite Gaussian and matrix-function theorems and
trace inequalities used are named and linked in the proof; their
finite, positive-semidefinite, analytic-domain and norm hypotheses
are verified above. Mathlib coverage of those supporting results
has not been checked in this step. The new content is the exact
Wilson/source specialization and its complete normalized estimate,
not a reproof or originality claim for those general theorems.
