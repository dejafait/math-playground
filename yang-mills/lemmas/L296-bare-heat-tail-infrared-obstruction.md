# L296 — Infrared obstruction for the bare heat-tail interpolation

## Hypotheses

Use L280's exact SU(2) relative cube: even N>=2, a=8/N, counting
measure, all boundary-contained links pinned, boundary-fixed gauges,
and every remaining link variable, including both normal endpoint
cases. Use the exact nonnegative reflected product bump of L282(1).
Keep L279's Wilson normalization, all-link jets on L280's own slice,
and the complete density matrix D_N of L280(16). No counterterm,
running vertex, longitudinal covariance, or boundary replacement is
introduced. Sources are real in (|s|+|t|)F<eta<1, F=||f_*||_infinity;
all derivatives in the conclusion are at zero.

Suppress color in the following precision matrices. Q is a fixed
orthonormal inclusion of H=ker B*. On H put

\[
 A=A_N=Q^*C^*CQ,\quad K_\pm=Q^*C^*\operatorname{diag}(h_\pm)CQ,
 \quad A(s,t)=A-sK_--tK_+.
 \tag{1}
\]

Thus 0<=K_pm<=F A and A(s,t)>0. For proper time r>=0 define

\[
 H_r(s,t)=Q A(s,t)^{-1}e^{-rA(s,t)}Q^*.
 \tag{2}
\]

Tensor this covariance with I_3 for the Wilson contractions. With
exactly L280(19)'s tensors and contractions, define the *bare* cutoff
expression and its complete mixed derivative by

\[
 \begin{split}
 R_{N,r}(s,t)={}&\frac1{12}\mathcal B(T(s,t),T(s,t);H_r,H_r,H_r)
 -\frac18\mathcal U(U(s,t);H_r,H_r)
 +\operatorname{Tr}((D_N\otimes I_3)H_r),\\
 k_N(r)={}&\partial_s\partial_t R_{N,r}(0,0).
 \end{split}                                                   \tag{3}
\]

In the trace the three-color interpretation of H_r is understood.
The source dependence inside the exponential is part of (2); its
derivatives are not the inverse-only formulas L280(18). The affine
source jets T(s,t), U(s,t) are unchanged, including both insertions.

The mathematical inputs are L003's relative modes, L279/L280's exact
coefficient and Wilson tensors, L282(18)'s strong density limit on
smooth relative fields, and L287(2)'s curl energy argument. The bounded
weight specialization of the last argument is justified below. L291's
uncut cancellation is context, not an estimate for (3).

## Conclusion

At every fixed mesh, k_N(0)=kappa_a and lim_(r->infinity) k_N(r)=0.
These are exact source-dependent endpoints, with every density and
insertion term retained.

Put

\[
 \lambda_{0,N}=12\sin^2(\pi/(2N)),\qquad
 \theta_N=\tfrac32\log N,\qquad r_N=\theta_N/\lambda_{0,N}.
 \tag{4}
\]

Define the four continuum unit ground modes on [-4,4]^4 by
psi_mu=e_0(x_mu) product_(nu!=mu) v_1(x_nu) dx_mu, where
e_0=1/sqrt(8) and v_1(x)=(1/2)sin(pi(x+4)/8). Set

\[
 \mu_0=3\pi^2/64,\qquad
 \mathsf B_{\mu\nu}=\mu_0^{-1}\int h_+(x)
       (d_{12}\psi_\mu)(x)(d_{12}\psi_\nu)(x)\,dx.
 \tag{5}
\]

This is a positive semidefinite, nonzero four-by-four matrix. With
the strictly negative constant d_* of L282(2), the *complete* cutoff
coefficient satisfies

\[
 \boxed{\quad
 \frac{k_N(r_N)}{N^{1/2}(\log N)^2}
 \longrightarrow \frac{9d_*}{4\pi^2}\operatorname{Tr}(\mathsf B^2)<0,
 \qquad k_N(2r_N)\longrightarrow0.\quad}                       \tag{6}
\]

In particular the signed increment k_N(r_N)-k_N(2r_N) is unbounded.
The same obstruction occurs along a subsequence of the ordinary
dyadic times 2^j; it is not dependent on choosing a different scale
ratio at each mesh. A dyadic telescoping decomposition of (3) with
uniformly O(1) signed increments at every scale therefore fails.
Also, taking r_N as the terminal time gives an unbounded infrared
term despite only O(log(eN)) preceding scales.

This is a negative result for (2)--(3), not for kappa_a, other heat
organizations, or Yang--Mills. It shows neither divergence nor a
logarithmic bound for the uncut coefficient. Short-scale contractions
can cancel a long-scale density term in k_N(0); (6) does not forbid
that. No uniform higher remainder, interacting lower bound, nonzero
continuum sector or positive physical mass follows. This new local
obstruction is accepted by the separate conceptual audit in section 6,
conditional on the stated canonical inputs and only for (2)--(3).

## Proof

### 1. Endpoints, derivatives and dyadic identity

Equation (2) is the proper-time integral int_r^infinity exp(-uA(s,t))du
on the fixed space H. It is analytic near zero sources at every fixed
N. The covariance remains color diagonal, so the alternating cubic
color trace still kills all internal cubic contractions. Thus the
same finite Wick calculation as L280(19) gives exactly (3), including
the complete D_N. No assertion of gauge independence for a cutoff
summand is made.

At r=0, L280(7),(19) identify (3) with L279's mixed coefficient.
At fixed N, source derivatives of e^(-rA) are finite Duhamel integrals
bounded by a polynomial in r times an exponentially decreasing
function, since A is positive. The inverse derivatives are finite.
Consequently k_N(r)->0 without a mesh-limit interchange.

For any b>0 and integer J>=0 there is the exact finite identity

\[
 \kappa_a=[k_N(0)-k_N(b)]
       +\sum_{j=0}^{J-1}[k_N(2^jb)-k_N(2^{j+1}b)]
       +k_N(2^Jb).                                           \tag{7}
\]

Choosing J=ceil(log_2 r_N), b=r_N/2^J in (1/2,1] for large N gives
O(log(eN)) increments and terminal term k_N(r_N). The base and shell
bounds are not assumed. An unbounded terminal term is already enough
to fail the conjunction of bounds sought for this formulation.

### 2. Lowest relative modes and the full density on them

L003's modes, in counting normalization, and L280(21),(26) give
lambda_k=4 sum_nu sin^2(pi k_nu/(2N)). A component mu has k_mu>=0
and the other three indices positive. Exactly one zero index leaves
one transverse component; an all-positive index leaves three
transverse polarizations. Hence the lowest one-color eigenvalue is
lambda_0 in (4), of multiplicity four, with one mode for each
k_mu=0 and k_nu=1 (nu!=mu). Denote its projection on H by P_N.

Every other eigenvalue is at least (4/3)lambda_0. All-positive
indices give this threshold directly. In a one-zero sector with
one other index at least two, for N>=3 the ratio is at least
(2+4 cos^2(pi/(2N)))/3>=5/3. For N=2 there is no such index.
There is no all-zero edge mode. This argument retains the normal
midpoint cosine values and all relative boundary sectors.

The four unit counting modes are exactly a^2 times samples of the
psi_mu in (5). L282(18) therefore gives, on this fixed four-dimensional
space,

\[
 P_NQ^*D_NQP_N\longrightarrow d_*I_4,
 \qquad \|Q^*D_NQ\|\le241/4.                                \tag{8}
\]

This uses L282's proved strong limit, not a pointwise replacement of
D_N at boundary rows. Its polynomial approximation controls the full
density, faces and their intersections. Define on H

\[
 \widehat A=A/\lambda_0,\qquad
 B_\pm=K_\pm/\lambda_0,\qquad
 M_\pm=\widehat A^{-1/2}B_\pm\widehat A^{-1/2};
 \quad 0\le M_\pm\le F I.                                  \tag{9}
\]

Both compressed source matrices P_N B_- P_N and P_N B_+ P_N
are exactly the same matrix, say B_{0,N}. Only ground components
1 and 2 have a nonzero 12-curl. Their time factor v_1(t) is even,
and time reflection preserves the 12 orientation and the finite
plaquette grid. This proves equality for both source orders, not
just equality of their traces.

The centered difference formula in L003 and Riemann sums give
B_{0,N}->mathsf B: each counting ground mode contributes a^2,
its unscaled curl contributes another a, and the sum has factor
a^-4, while lambda_0/a^2->mu_0. This gives exactly (5), with no
extra plaquette weight. Positivity is immediate. Moreover
int h_+ |d_12 psi_1|^2>0: this analytic curl is not identically zero
on the open set where the exact bump is positive. Thus
Tr(mathsf B^2)>0. From (8),

\[
 a_N:=\operatorname{Tr}\bigl((Q^*D_NQ)P_NB_-P_NB_+P_N\bigr)
       \longrightarrow d_*\operatorname{Tr}(\mathsf B^2)<0.
 \tag{10}
\]

### 3. Uniform complete mixed density calculation

For theta>=1 let f_theta(z)=e^(-theta z)/z. In this section r=theta/lambda_0
is held fixed when sources are differentiated. All sources, including
those in the heat cutoff, are differentiated. Write D_H=Q*D_N Q.
We prove the uniform estimate

\[
 \partial_s\partial_t\operatorname{Tr}\bigl((D_N\otimes I_3)H_r\bigr)
 =\frac3{\lambda_0}\left\{
 e^{-\theta}(\theta^2+2\theta+2)a_N
 +O_F((1+\theta)e^{-\theta})+O_F(e^{-7\theta/6})\right\}.
 \tag{11}
\]

Here and below constants may depend on the fixed bump and eta but
not on N, r or theta in the stated ranges. For completeness the
trace remainder, including the growing high spectrum, is controlled
as follows; finite-rank leading terms alone would not suffice.

Apply finite-matrix holomorphic functional calculus to
widehat A(s,t)=widehat A-sB_--tB_+. On a small fixed circle around
1, of radius 1/12, its zero-source resolvent splits as

\[
 (z-\widehat A)^{-1}=P_N/(z-1)+S_N(z).
 \tag{12}
\]

S_N and its required derivatives are analytic there. Their norms
between factors widehat A^(1/2) are uniformly bounded by the gap
1/3, since sup_(lambda>=4/3) lambda/|z-lambda| and the corresponding
derivative bounds are finite. Differentiating a resolvent twice
gives the two ordered products R B_- R B_+ R and R B_+ R B_- R.
Their three-P parts have residue f_theta''(1)/2 each. Transposition
shows their D_H traces are equal, giving f_theta''(1)a_N. Here
f_theta''(1)=e^(-theta)(theta^2+2theta+2).

Every other nonzero residue contains a P_N, has pole order at most
two, and has uniformly bounded finite-rank coefficients. For example
S_N B_pm P_N is bounded because B_pm=widehat A^(1/2)M_pm widehat A^(1/2)
and widehat A^(1/2)P_N=P_N. The other placements have the same
weighted-resolvent bound; derivatives of S_N have it as well.
Their trace norms are uniformly bounded since rank P_N=4.
Their residues use only f_theta(1) and f_theta'(1), so their total
D_H trace is O((1+theta)e^(-theta)). Terms with no P_N are analytic
inside this circle and contribute zero.

To control the remaining spectrum use the two rays
z=7/6+u +/- iu, u>=0, enclosing the high positive spectrum to their
right. For zero sources, on these rays

\[
 \|R_z\|\le C/(1+|z|),\quad
 \|R_z\widehat A^{1/2}\|\le C/(1+|z|)^{1/2},\quad
 \|\widehat A^{1/2}R_z\widehat A^{1/2}\|\le C.
 \tag{13}
\]

These follow by taking the supremum over the real eigenvalues,
which are 1 or at least 4/3. The relative perturbation (9) and a
Neumann series preserve these bounds on a fixed complex source
polydisc about zero. In particular the resolvent and both its source
derivatives have the first bound in (13). The low circle and high
rays remain spectral contours there; finite-dimensional continuation
preserves their spectral counts.

There is also the uniform Schatten bound
Tr(widehat A^-3)<=C. Indeed lambda_k/lambda_0>=c|k|^2 with
c=4/(3pi^2), at most four edge modes per index, and the number of
indices with max k=m is O(m^3); sum m^3/m^6 converges. Using
widehat A(s,t)^-1=widehat A^-1/2 (I-sM_--tM_+)^-1 widehat A^-1/2,
finite-matrix Schatten Holder gives a uniform Schatten-3 norm for
this inverse, hence a uniform trace norm for widehat A(s,t)^-3.
Its first and mixed source derivatives also have uniform trace
norm by Cauchy's formula on the fixed complex polydisc. These are
ordinary finite-matrix inequalities; no infinite-dimensional heat
trace theorem is assumed.

Represent the high spectral part of f_theta(widehat A(s,t)) as

\[
 \widehat A(s,t)^{-3}\frac1{2\pi i}
 \int_{\Gamma_{\rm high}} z^2 e^{-\theta z}
                    (z-\widehat A(s,t))^{-1}\,dz.
 \tag{14}
\]

This is exactly the functional calculus, since z^-3 z^2=z^-1
on each spectral subspace; the inverse commutes with the resolvent.
After up to two source derivatives, its trace norm is bounded by a
constant times int_0^infinity (1+u)e^(-theta(7/6+u))du, which is
O(e^(-7theta/6)) for theta>=1. This accounts for *all* high modes
without a factor equal to the lattice dimension. Equations
(10)--(14), the factor lambda_0^-1 in (2), and three colors prove
(11). No positivity of an individual differentiated heat kernel was
used.

### 4. Heat-derivative bounds sufficient for both full Wilson groups

This section uses the unscaled A on H and G=A^-1. Matrices are
extended by Q to the edges when entries or curls are mentioned.
L280 gives G_ee<=30 and ||A||<=16. Fix c=9/10 and write

\[
 m_r=1+\log(1+16r),\qquad \theta=r\lambda_0\ge1.
 \tag{15}
\]

For source derivatives H_i,H_ij of H_r at zero, with i,j in {-,+},
the following bounds hold (the constants absorb F and colors):

\[
 \begin{split}
 &\|G^{-1/2}H_rG^{-1/2}\|\le e^{-\theta},\\
 &\|G^{-1/2}H_iG^{-1/2}\|\le C m_r e^{-c\theta},\\
 &\|G^{-1/2}H_{ij}G^{-1/2}\|\le C m_r^2 e^{-c\theta},\\
 &|(H_r)_{ef}|\le C N^{-2}e^{-\theta},\\
 &|(H_i)_{ef}|\le C N^{-1}m_r e^{-(1+c)\theta/2},\\
 &|(H_{ij})_{ef}|\le C m_r^2 e^{-c\theta}.
 \end{split}                                                   \tag{16}
\]

Inverses in these norm expressions mean restriction to H. Here is a
direct derivation, also fixing the source differentiation at the
cutoff. Put E(u)=e^(-uA) and M_i=A^-1/2 K_i A^-1/2, so ||M_i||<=F.
Duhamel differentiation gives

\[
 \begin{split}
 A^{1/2}E_i(r)A^{-1/2}
 &=\int_{u_0+u_1=r} A E(u_0)M_iE(u_1)\,du_0,\\
 A^{1/2}E_{ij}(r)A^{-1/2}
 &=\int_{u_0+u_1+u_2=r}
       A E(u_0)M_i A E(u_1)M_jE(u_2)\,du_0du_1
       +(i\leftrightarrow j).
 \end{split}                                                   \tag{17}
\]

The integrations are over nonnegative times. For all u>=0,
||E(u)||<=e^(-c lambda_0 u), while
||A E(u)||<=e^(-c lambda_0 u) min(16,C_c/u), with value 16 at
u=0. The integral of the latter minimum on [0,r] is O_c(m_r).
The double simplex integral is bounded by the corresponding square
integral. Thus (17) is bounded by C m_r e^(-c theta) and
C m_r^2 e^(-c theta), respectively. Transposition gives the bounds
with A^(-1/2) on the left instead. Differentiating H_r=E(r)G and
using G_i=G^(1/2)M_iG^(1/2),
G_ij=G^(1/2)(M_iM_j+M_jM_i)G^(1/2), proves the first three bounds
of (16). The last bound follows from G_ee<=30.

For the sharper undifferentiated entry bound, use the exact relative
Hodge modes: each squared counting-mode entry is at most 16/N^4.
The positive ambient operator L^-1 e^(-rL), L=C*C+BB*, dominates
the transverse extension H_r at zero. The spectral facts above give

\[
 (H_r)_{ee}\le\frac{16}{N^4\lambda_0}e^{-\theta}
 \sum_{\text{component modes}} d_k^{-1}e^{-\theta(d_k-1)}
 \le C N^{-2}e^{-\theta},\qquad d_k=\lambda_k/\lambda_0.
 \tag{18}
\]

The sum is uniformly bounded for theta>=1 since d_k>=c_0|k|^2
and d_k>=1. Off-diagonal entries follow by positive Cauchy--Schwarz.
This includes both normal-edge endpoints and the k_mu=0 sectors.

Finally write H_r=E(r/2)G E(r/2) before differentiating it.
In E_i(r/2)G E(r/2), one factor G^(1/2)E_i(r/2)e_e has norm at
most C m_r e^(-c theta/2) sqrt(G_ee), by (17) and transposition.
The other factor G^(1/2)E(r/2)e_f has norm at most
C N^-1 e^(-theta/2), by (18). The transposed term is identical
in size. The middle term E(r/2)G_iE(r/2) is at most
F sqrt((H_r)_ee(H_r)_ff). This proves the sharper first-derivative
entry bound in (16); merely using its operator bound would lose the
power needed for the quartic comparison.

Differentiate the quartic part of (3). The four terms and their
factors are exactly L280(20)'s quartic formula, with G,G_pm,G_-+
replaced by H_r,H_pm,H_-+. Each Wilson tensor is a sum of O(N^4)
fixed four-slot tensors with bounded coefficients; an insertion adds
only the bounded weight h_pm. Pinned slots are zero. Thus (16),
retaining both differentiated covariance lines, gives for the *whole*
quartic response

\[
 |k_{4,N}(r)|\le C N^2 m_r^2 e^{-(1+c)\theta}.
 \tag{19}
\]

Specifically, the two-action-line terms use H_ij H_r or H_i H_j,
each bounded per plaquette by C N^-2 m_r^2 e^(-(1+c)theta).
The insertion terms use H_i H_r and are smaller. This estimates
all orientations, rows and boundary slots, not a selected local term.

For the cubic part, L287's energy argument also applies to a tensor
T_w from V_w=sum_p w_p(Cx)_p dot zeta_p(x), whenever ||w||_infinity
is bounded. In L287(9), multiplication by w only bounds the vector
of curl coefficients by ||w||_infinity||Cu||. In L287(10)--(11),
it conjugates the positive Schur matrix by diag(w), whose norm is
at most ||w||_infinity. The finite number of types and slot
multiplicities are unchanged. Therefore its proof gives
E_w<=C||w||_infinity^2(I+log(eN) C*C). Consequently

\[
 \mathcal B(T_w,T_w;G,G,G)=\operatorname{Tr}(E_wG)
 \le C\|w\|_\infty^2 N^4\log(eN).                           \tag{20}
\]

Here Tr G<=30 times the number of edge/color slots, and CGC* is
the complete curl projection, with rank O(N^4). This is the needed
bounded-weight specialization, not an assumption of constant sources.
It applies to T, T_- and T_+ on their actual plaquette domains.

To allow signed differentiated covariances, conjugate all three
tensor slots by G^(1/2). If X_l=G^(1/2)Z_lG^(1/2), tensor-product
Cauchy--Schwarz gives

\[
 |\mathcal B(T_w,T_v;X_1,X_2,X_3)|
 \le\prod_l\|Z_l\|
  \sqrt{\mathcal B(T_w,T_w;G,G,G)
         \mathcal B(T_v,T_v;G,G,G)}.
 \tag{21}
\]

This does not assume positivity of X_l. Differentiate the cubic
part of (3) with its exact multiplicities, as in L280(20). Every
term has three covariance lines and at most two source derivatives
in total. Equations (16),(20),(21) give the complete bound

\[
 |k_{3,N}(r)|\le C N^4\log(eN)m_r^2 e^{-3c\theta}.
 \tag{22}
\]

These infrared estimates use no discarded boundary stratum, source
tail or unproved finite-range replacement. They are not proposed as
useful bounds at r=0.

### 5. Comparison at the test scale and ordinary dyadic subsequence

At r=r_N, lambda_0~3pi^2/N^2, theta=(3/2)log N, and m_r=O(log(eN)).
Equation (11), together with (10), gives the first limit in (6) for
the density alone: the low residual is smaller by a factor O(1/log N),
and the high residual is O(N^(1/4)), smaller than N^(1/2)(log N)^2.
The complete Wilson estimates give the actual/required comparison

\[
 \begin{split}
 |k_{4,N}(r_N)|&=O(N^{-17/20}(\log(eN))^2),\\
 |k_{3,N}(r_N)|&=O(N^{-1/20}(\log(eN))^3),\\
 k_{D,N}(r_N)&\sim
       \frac{9d_*}{4\pi^2}\operatorname{Tr}(\mathsf B^2)
           N^{1/2}(\log N)^2.
 \end{split}                                                   \tag{23}
\]

Both Wilson quantities even tend to zero. Thus the density is not
a selected-group diagnosis: it determines the complete signed
coefficient at this cutoff. At 2r_N, (11) is O(N^-1(log N)^2),
and (19),(22) are smaller still. This proves (6) and the complete
signed-increment assertion.

For fixed-origin dyadic times, extend r(x)=(3/2)log x/
[12 sin^2(pi/(2x))] continuously to x>1. It is strictly increasing,
and r'(x)/r(x)=O(1/x) for large x, directly by differentiation.
For each sufficiently large integer j let x_j solve r(x_j)=2^j,
and choose the nearest even N_j. Then N_j->infinity and

\[
 2^j/r_{N_j}=1+O(1/N_j),\qquad
 \lambda_{0,N_j}2^j=\tfrac32\log N_j+O(\log N_j/N_j).
 \tag{24}
\]

All estimates above hold uniformly in theta. Replacing theta_N by
(24) changes the leading exponential and polynomial factors by
1+o(1), and preserves the bounds (23). Hence
k_(N_j)(2^j)-k_(N_j)(2^(j+1)), divided by
N_j^(1/2)(log N_j)^2, has the same strictly negative limit in (6).
These j satisfy j=O(log(eN_j)). This refutes a uniform O(1) bound
on all complete signed dyadic increments for the stated bare path.

No inference is made about their cancellations in (7), an endpoint
at a different fixed physical heat time, a source-frozen cutoff,
or a procedure that changes effective vertices/density with the scale.
Those are different mathematical questions. The uncut o(N^2)
result and all main-target gaps remain intact.

### 6. Separate conceptual audit (2026-10-28)

This audit accepts (6), (23) and the fixed-origin dyadic conclusion
under the stated hypotheses. It checks the uniform specializations
below, rather than importing them from fixed-dimensional matrix
calculus. The completed task is REPRODUCTION: validation of the
written obstruction, not a new mechanism or an originality claim.
L003, L279, L280, L282 and L287 remain the mathematical inputs;
neither L291 nor a one-face replacement is used in this proof.

**Matrix inputs and uniform contours.** The Cauchy functional calculus
used here is Higham--Lin, *Matrix Functions: A Short Course*,
[MIMS EPrint 2013.73](https://eprints.maths.manchester.ac.uk/2067/1/paper.pdf),
section 3.1.3, Definition 3.3, p. 6. The ordered derivative formula is
Schweitzer, *Integral representations for higher-order Frechet
derivatives of matrix functions*,
[arXiv:2203.03930v1](https://arxiv.org/pdf/2203.03930v1),
section 2.1, Lemma 1 and Theorem 2, pp. 2--3. Analyticity on and
inside the relevant contours, with zero excluded for f_theta, is
required. At second order the theorem sums both resolvent orders;
no commutativity of B_- and B_+ is assumed. Finite Schatten Holder
is used in the form stated by Ponge, *Introduction to Noncommutative
Geometry*, Summer 2025,
[chapter 4](https://raphaelponge.org/wp-content/uploads/2025/07/summer-chap4-1.pdf),
slide 56, together with the ideal property on the preceding slides.
For its finite-matrix trace/ideal cases see also Watrous,
[*The Theory of Quantum Information*, 2018 draft](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf),
section 1.1, pp. 32--33, (1.165)--(1.175). These named inequalities
apply to arbitrary complex finite matrices with dimension-independent
constants. They supply no spectral counting or Wilson estimate.

Let Ahat=widehat A. On the low circle and high rays in (12)--(13),
sup ||Ahat^(1/2) R_z Ahat^(1/2)|| is bounded by one constant C_0,
uniformly in N. This follows from the eigenvalues 1 and [4/3,infinity);
on the circle its distance to the latter interval is at least 1/4,
and on the rays their imaginary parts grow with u. Choose delta>0
so C_0 F delta<1/2. Factoring the perturbation through
Ahat^(1/2)(sM_-+tM_+)Ahat^(1/2) and applying its resolvent Neumann
series proves (13) on |s|+|t|<delta, after increasing its constants.
The same factorization proves the two half-weighted bounds there.
The ordered first and second derivatives consequently have norm
O((1+|z|)^-1). Continuation along (s,t) scaled from zero preserves
the low rank four and puts the rest inside the high contour. At each
fixed N the rays can be closed to their right beyond the matrix
norm; the closing arc tends to zero because its real part tends to
positive infinity. The estimates on the rays are independent of this
closure and of N. Thus no dimension-dependent contour length enters.

For clarity, every low-circle residue in the mixed derivative is
controlled, including noncommuting placements. Three P_N factors
give the pole of order three. With two P_N factors the pole has
order two and its analytic coefficient and first z derivative are
bounded; with one P_N it has order one and a bounded coefficient.
For example P_N B_i S_N B_j P_N is bounded by
P_N M_i(Ahat^(1/2)S_N Ahat^(1/2))M_j P_N, and
S_N B_i S_N B_j P_N factors into S_N Ahat^(1/2), M_i,
Ahat^(1/2)S_N Ahat^(1/2), M_j and P_N. The one-P middle placement
is (S_N B_i P_N)(P_N B_j S_N), with both factors bounded. The
remaining two-P placement P_N B_i P_N B_j S_N equals
P_N M_i P_N M_j Ahat^(1/2)S_N. Transposition covers the reversed
placements, and differentiating their sole S_N factor covers the
analytic coefficient derivatives for the double poles.
All such coefficients have rank at most four. Their trace norms
are therefore uniform. The pole-order-two residue uses f_theta'
and f_theta times the coefficient derivative, and the simple pole
uses f_theta only. The no-P term is analytic. This proves the
O((1+theta)e^-theta) low remainder without bounding f_theta on
the leftmost point of the circle, which would lose an exponential.

For the high part, the count sum_m O(m^3)m^-6 is convergent, so
||Ahat^-1/2||_6 is uniformly bounded. With
Z=(I-sM_--tM_+)^-1, Holder gives
||Ahat(s,t)^-1||_3 <= ||Ahat^-1/2||_6^2 ||Z||,
then ||Ahat(s,t)^-3||_1 <= ||Ahat(s,t)^-1||_3^3.
Cauchy's formula on a smaller fixed polydisc bounds the first and
mixed derivatives in trace norm as well. Applying the product rule
to (14) uses these trace norms and the operator norms of R_z and
both its derivatives. Since |z|^2/(1+|z|)=O(1+u), the complete
integral is bounded by C e^(-7theta/6) for theta>=1. This verifies
the full high-mode trace remainder, also for complex sources; it
uses no positivity or normality of the perturbed matrix.

**Ground compression, density and normalization.** In the relative
modes of L003 section 2 and L280(21),(26), the own-direction cosine
zero mode is divergence free. There are exactly four ground states,
and all other sectors have the gap used above, including N=2.
Each ground vector is a^2 S_a psi_mu, so its counting error under
D_N-d_* is exactly the physical-norm error of L282(18). Thus (8)
is a valid finite-dimensional consequence of that strong limit; it
does not require operator-norm convergence of the full D_N.
Only components 1 and 2 have a 12-curl, and their time sine factors
are even. Reflection hence gives the exact equality of compressed
source matrices before taking N to infinity. Their curls scale as
a^3, so the source sum divided by lambda_0 tends to (5), since
a^6 a^-4/lambda_0 -> 1/mu_0. The bump is positive on an open set
where d_12 psi_1 is not identically zero. Consequently mathsf B is
nonzero and positive semidefinite, and (10) has a strictly negative limit.

Each of the two three-P resolvent orders has coefficient f_theta''/2.
Transposition and cyclicity of the finite trace make their traces
equal even before the equal-compression observation. Their sum is
f_theta'' a_N, not twice that amount. The density is color diagonal
with three equal blocks. Together with lambda_0~3 pi^2/N^2 and
theta_N=(3/2)log N this gives exactly 9d_*/(4 pi^2) Tr(mathsf B^2)
in (6). Neither a new a^4 plaquette weight nor an extra color or
source-order factor is present.

**Differentiated heat lines and complete Wilson sums.** In (17) the
source direction is -K_i in A(s,t); differentiating the exponential
therefore inserts +K_i. Conjugating each ordered Duhamel product
gives the displayed A E(u_0) M_i A E(u_1) M_j E(u_2), in that
order. The simplex integral is bounded by a square of the integral
of min(16,C_c/u); all remaining factors have exponential
e^(-c lambda_0 r). This argument works for r/2 too, without requiring
(r/2)lambda_0>=1. Differentiating E(r)G gives E_ij G,
E_i G_j, E_j G_i and E G_ij, retaining both orders in G_ij.
After G-relative conjugation each has the asserted m_r^2 bound.

The sharper first-derivative entry estimate uses the identity
H_r(s,t)=E_{s,t}(r/2)G(s,t)E_{s,t}(r/2), valid before differentiation.
For its first outer derivative, the two vector norms are bounded by
C m_r e^(-c theta/2) sqrt(G_ee) and
sqrt((H_r)_ff)<=C N^-1 e^(-theta/2). The other outer derivative
has the reversed indices. The middle derivative is bounded by
F sqrt((H_r)_ee(H_r)_ff). This proves the N^-1 gain in (16).
The ambient spectral sum in (18) retains both normal endpoints;
positivity is used only for the undifferentiated H_r, never for H_i
or H_ij.

The tensor multiplicities of L280(20) survive any twice-differentiable
covariance in (3). For the cubic term the five coefficients inside
its factor 1/12 remain 2,-6,-6,3,6, and for the quartic term the
four coefficients inside -1/8 remain -2,-2,2,2. The tensors are
affine, so there are no second vertex derivatives. In the quartic
sum the two potentially largest products are H_ij H_r and H_i H_j;
both have entry bound C N^-2 m_r^2 e^(-(1+c)theta). Insertion
products H_i H_r have the stronger bound
C N^-3 m_r e^(-(3+c)theta/2). Summing the fixed four-slot tensors
over all O(N^4) plaquettes proves (19) with every boundary slot.

For the weighted cubic argument, L287(9)'s coefficient vector becomes
w_p(Cu)_p, with squared norm at most ||w||_infinity^2||Cu||^2.
In L287(10)--(11), the positive Schur covariance matrix is conjugated
by diag(w); its norm increases by at most ||w||_infinity^2. The
same edge-selection multiplicity bound applies on the full relative
domain. L287(13)'s normalization then proves the E_w inequality in
(20), including signed real weights. Its trace against G bounds
the squared norm of the tensor transformed by (G^(1/2)) in all
three slots. The tensor-product operator Z_1 tensor Z_2 tensor Z_3
has norm at most the product of their norms, proving (21) for signed
source derivatives. This justifies all five differentiated cubic
groups and (22); no constant-source or separated-vertex hypothesis
has entered.

**Threshold and dyadic check.** With c=9/10, the quartic exponent is
2-(1+c)(3/2)=-17/20 and the cubic exponent is
4-3c(3/2)=-1/20. Their logarithmic factors are respectively two
and three. The density low remainder is O(N^(1/2)log N) and its
high remainder O(N^(1/4)), both smaller than its negative leading
N^(1/2)(log N)^2 term. At twice the time the density is
O(N^-1(log N)^2), and the Wilson bounds also tend to zero. Thus
this comparison is for the complete response, not a selected group.

Directly, r'(x)/r(x)=1/(x log x)+(pi/x^2)cot(pi/(2x))>0 for x>1,
and it is O(1/x) for large x. Rounding the unique large solution
r(x_j)=2^j to the nearest even N_j changes r by relative O(1/N_j)
and theta by O(log N_j/N_j). Uniformity of (11),(19),(22) then
gives the same nonzero limiting constant at the dyadic times and
zero at their doubles. This confirms the failure of uniform O(1)
complete signed increments for this bare path. It gives no estimate
of their cancellations in (7), the uncut coefficient, or a tail
that retains mixed contractions with a complementary covariance.

## Mathlib

Full matching coverage and supporting library coverage for this
source-dependent heat-tail obstruction are **not checked**. No
Mathlib absence, theorem name or matching library link is asserted.
The finite spectral theorem, matrix holomorphic functional calculus,
Duhamel differentiation, Cauchy's formula and finite Schatten Holder
are used in their standard finite-dimensional forms, with the needed
uniform estimates supplied above. The Wilson-specific inputs are
the cited canonical local results, with their hypotheses retained.
No Bałaban/Bauerschmidt renormalization or decomposition theorem is
imported as a bound for (3). The original derivation was classified
POTENTIALLY_NEW only in the saved assessment's limited sense, not
as certified originality.
The later audit is REPRODUCTION and does not change the unverified
Mathlib-coverage status or assert progress beyond the sources checked.
