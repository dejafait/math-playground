# L302 — Complete high one-heat-line response by symmetric inverse regularization

## Hypotheses

Retain the exact hypotheses and upstream premises of L301, L297 and
L296: SU(2), even N>=2, a=8/N, Euclidean counting measure, L282's
reflected smooth 12-bumps, boundary-contained pinned links,
boundary-fixed gauges, and every variable normal endpoint. Use the
fixed one-color transverse space H=ker B*, its orthonormal inclusion
Q, and the ambient Wilson jets on their own relative-Coulomb slice.
Keep the full Haar and both gauge-determinant density contributions.
No change of covariance law, boundary condition or gauge is made.

On H use L301(2)'s A,K_i,lambda_0,theta_N,r_N. Put

\[
 S=A/\lambda_0\ge I,\qquad B_i=K_i/\lambda_0,
 \quad M_i=S^{-1/2}B_iS^{-1/2},\quad \|M_i\|\le F,
 \quad L(s,t)=S-sB_--tB_+ .                         \tag{1}
\]

Here F is the fixed bump supremum. L296's relative mode count gives
Tr(S^-3)<=C independently of N. Its audited high contour consists
of z=7/6+u +/- iu, u>=0, positively oriented around the high spectrum
to the right, with the ground cluster excluded. The spectrum of S is
1 (rank four) and a subset of [4/3,infinity). These contours remain
valid on a fixed small complex source neighborhood of zero, with
the uniform relative-resolvent bounds recorded in L296(13) and its
audit. Complex sources serve only matrix differentiation; no complex
Gaussian probability law is used.

For theta>=1 fixed during source differentiation, let

\[
 F^{\rm hi}_\theta(s,t)=\frac1{2\pi i}
   \int_{\Gamma_{\rm hi}}\frac{e^{-\theta z}}z
                    (z-L(s,t))^{-1}\,dz .             \tag{2}
\]

Define the one-color H^hi(s,t)=lambda_0^-1 F^hi_{theta_N}(s,t).
It is the high part of A(s,t)^-1 exp(-r_N A(s,t)); the complementary
low part is exactly L301(3). A subscript alpha means the derivative
at zero for the labeled set alpha=empty,-,+,-+. Both r_N and the
contour are fixed. Use L301(4) for the complete one-color operator
Wtilde(s,t)=Q*W_N(s,t)Q after internal color contractions. In particular,
write ell_N=log(eN) and

\[
 \|S^{-1/2}\widetilde W_\alpha S^{-1/2}\|
 \le C_f\epsilon_N,\qquad
 \epsilon_N=N^{-1}+N^{-1}\sqrt{\ell_N}+N^{-2}\ell_N.   \tag{3}
\]

All these local analytic inputs remain conditional on their stated
upstream premises; they are not reaudited here.

## Conclusion

For every required alpha and theta>=1,

\[
 \boxed{\quad
 \|S^{1/2}(F^{\rm hi}_\theta)_\alpha S^{1/2}\|_1
          \le C_f e^{-7\theta/6} .\quad}              \tag{4}
\]

Consequently the complete high one-heat-line response satisfies

\[
 \boxed{\quad
 \left|3\left.\partial_s\partial_t
       \operatorname{Tr}_H(\widetilde W(s,t)H^{\rm hi}(s,t))
                        \right|_{0,0}\right|
 \le C_f\epsilon_N\lambda_0^{-1}e^{-7\theta_N/6}
 =O_f(N^{-3/4}\sqrt{\ell_N})=o(1).\quad}             \tag{5}
\]

With L301(5) and L297(8),(25),(28), this also gives the finite
assembly for the registered complete terminal complementary response

\[
 \boxed{\quad |\tau_N(r_N)|
       =O_f(N^{-1/20}\ell_N^3)=o(1).\quad}           \tag{6}
\]

These are a mathematical specialization of the standard matrix
tools cited below, under the saved SPECIALIZE assessment. No
originality beyond the checked sources is claimed. The new weighted
estimate and its assembly await a separate conceptual audit.
The conclusion concerns this terminal scale only. It does not give
uniform shell/full-tail control, an uncut coefficient bound, a uniform
higher perturbative remainder, an interacting reflection lower bound,
continuum field axioms or a positive infinite-volume mass. It is not
a complete-solution candidate.

## Proof

### 1. Symmetric regularization and the fixed outside weights

Write D=L(s,t)^-1 and V=(I-sM_--tM_+)^-1. On a sufficiently small
fixed complex neighborhood, ||V||<=2, and exactly

\[
 D=S^{-1/2}VS^{-1/2}.
\]

Use two inverse factors at each end, instead of L297's one-sided
three-inverse representation:

\[
 F^{\rm hi}_\theta
   =D^2\left\{\frac1{2\pi i}\int_{\Gamma_{\rm hi}}
       z^3 e^{-\theta z}(z-L)^{-1}\,dz\right\}D^2.    \tag{7}
\]

The finite holomorphic functional calculus identifies the middle
integral with L^3 exp(-theta L) times its high spectral projection.
D commutes with this resolvent and projection, since it is an
analytic function of the same invertible L. Thus the right side is
L^-1 exp(-theta L) times that projection, exactly (2). This uses no
commutation with S or M_i and no diagonalizability at nonzero sources.
The source for this standard calculus is Higham--Lin, *Matrix
Functions: A Short Course*, MIMS EPrint 2013.73, Definition 3.3 and
section 3.1.4, p. 6,
[primary PDF](https://eprints.maths.manchester.ac.uk/2067/1/paper.pdf).
Apply it to L296's admitted high subcontour; zero and the low cluster
are outside. No full-spectrum contour is substituted for this one.

Let the outside weights S^(1/2) be fixed at zero sources and set

\[
 X=S^{1/2}D^2=V S^{-1}V S^{-1/2},\qquad
 Y=D^2S^{1/2}=S^{-1/2}V S^{-1}V .                   \tag{8}
\]

These are exact ordered identities. Y need not equal X* at complex
sources. By the mode count,

\[
 \|S^{-1}\|_3=(\operatorname{Tr}S^{-3})^{1/3},\qquad
 \|S^{-1/2}\|_6=(\operatorname{Tr}S^{-3})^{1/6}.
\]

Schatten Holder, with 1/3+1/6=1/2 and all V factors bounded,
therefore gives uniform Hilbert--Schmidt bounds for X and Y.
This is the point at which both outside energy weights are paid for;
no growing bound for ||S|| is used.

The same bounds hold for every needed derivative. In fact

\[
 V_i=VM_iV,\qquad
 V_{-+}=VM_-VM_+V+VM_+VM_-V .                        \tag{9}
\]

Each X_i has the two derivative placements in the two V factors
of (8). Explicitly, writing J=S^-1 and T=S^-1/2,

\[
 X_{-+}=V_{-+}JVT+V_-JV_+T+V_+JV_-T+VJV_{-+}T .     \tag{10}
\]

The first and last terms each contain the two orders in (9).
Thus all six expanded mixed placements occur. The formula for
Y=T V J V has the identical four placements with the initial T
retained. Every differentiated V has bounded operator norm depending
only on F, and each product still has exactly one J in Schatten-3
and one T in Schatten-6. Hence, on a smaller fixed neighborhood,

\[
 \|X_\alpha\|_2+\|Y_\alpha\|_2\le C_f,
                \qquad \alpha=\varnothing,-,+,-+.   \tag{11}
\]

Here derivatives may be taken throughout that neighborhood; the
conclusion only needs their values at zero. The ideal inequalities
are Watrous, *The Theory of Quantum Information*, 2018 draft,
section 1.1, pp. 32--33, (1.165)--(1.175),
[primary PDF](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf),
and general product Holder in Ponge, *Introduction to Noncommutative
Geometry*, Summer 2025, chapter 4, slides 54--57, especially slide 56,
[primary slides](https://raphaelponge.org/wp-content/uploads/2025/07/summer-chap4-1.pdf).
They apply to arbitrary finite complex matrices, with no positivity,
commutativity or dimension factor. Only their quantitative local
specialization is proved here.

### 2. Ordered high resolvents and every derivative placement

Write R(z;s,t)=(z-L(s,t))^-1. L296's uniform bounds on the fixed
high rays imply, with constants independent of N and u,

\[
 \|R\|\le C(1+u)^{-1},\quad
 \|RS^{1/2}\|+\|S^{1/2}R\|\le C(1+u)^{-1/2},\quad
 \|S^{1/2}RS^{1/2}\|\le C .                         \tag{12}
\]

They hold on a sufficiently small fixed complex source neighborhood;
the source radius comes from L296's relative Neumann-series estimate,
not from finite-dimensional analyticity alone. For the sign convention
L=S-sB_--tB_+, the ordered derivatives are

\[
 R_i=-RB_iR,\qquad
 R_{-+}=RB_-RB_+R+RB_+RB_-R .                       \tag{13}
\]

These are Schweitzer, *Integral representations for higher-order
Frechet derivatives of matrix functions*, arXiv:2203.03930v1,
section 2.1, Lemma 1 with its proof, PDF pp. 2--3,
[primary PDF](https://arxiv.org/pdf/2203.03930v1),
with directions -B_i. Each contour point is outside the perturbed
spectrum as required. No use of that paper's full-spectrum Theorem 2
as a spectral-subcontour theorem is necessary.

Insert B_i=S^(1/2)M_iS^(1/2). The first derivative is a product
(RS^(1/2))M_i(S^(1/2)R). Each ordered mixed term is

\[
 (RS^{1/2})M_i(S^{1/2}RS^{1/2})M_j(S^{1/2}R).
\]

The first product has a minus sign, immaterial for its norm. Thus
(12) proves, for all the required alpha,

\[
                 \|R_\alpha\|\le C_f(1+u)^{-1}.      \tag{14}
\]

After applying the fixed outside weights to (7), the integrand is
z^3 exp(-theta z) X R Y. Its complete derivative is

\[
 \partial_\alpha(XRY)=
 \sum_{\alpha_X\sqcup\alpha_R\sqcup\alpha_Y=\alpha}
                X_{\alpha_X}R_{\alpha_R}Y_{\alpha_Y}. \tag{15}
\]

The subsets are labeled and disjoint. At mixed order this includes
the three placements of both labels on one factor and the six
ordered placements on distinct factors. Equations (9)--(10),(13)
retain both orders and every derivative of all four inverse factors
in (7). No regularizing factor has been frozen. From (11),(14) and
Schatten Holder with exponents 2,infinity,2,

\[
 \|X_{\alpha_X}R_{\alpha_R}Y_{\alpha_Y}\|_1
                 \le C_f(1+u)^{-1}.                 \tag{16}
\]

All identities and estimates have been obtained on finite H. For
each fixed N the high rays can be closed at Re z=T beyond the
norm of L on the small source neighborhood. The joining segment
has length O(T), |z|=O(T), and the resolvent is O(T^-1) there;
the polynomial factor z^3 is overcome by exp(-theta T).
Its integral tends to zero as T tends to infinity. Derivatives
also tend to zero, either by (13) at fixed N or uniform holomorphy
on the smaller source neighborhood. Constants for this closing
segment need not be uniform in N: it is removed at each fixed N
before the uniform ray estimate. On the rays, (11)--(16) give an
integrable majorant uniform in sources for the four required
derivatives. This justifies differentiation under the integral;
no limit in N is interchanged with differentiation.

### 3. Uniform weighted trace and the complete scalar

On either ray, Re z=7/6+u, |z|<=C(1+u), and |dz|=sqrt(2)du.
Equations (15)--(16) give

\[
 \begin{split}
 \|S^{1/2}(F^{\rm hi}_\theta)_\alpha S^{1/2}\|_1
 &\le C_f e^{-7\theta/6}
           \int_0^\infty (1+u)^2e^{-\theta u}\,du\\
 &=C_f e^{-7\theta/6}
              (\theta^{-1}+2\theta^{-2}+2\theta^{-3})
 \le C_f e^{-7\theta/6},\qquad\theta\ge1.
 \end{split}                                               \tag{17}
\]

The constants absorb both rays and the finite derivative sum. This
proves (4) with the full high spectral response, including derivatives
of its moving projection.

There are exactly four scalar product-rule terms:

\[
 3\operatorname{Tr}_H\bigl(
 \widetilde W H^{\rm hi}_{-+}
 +\widetilde W_-H^{\rm hi}_+
 +\widetilde W_+H^{\rm hi}_-
 +\widetilde W_{-+}H^{\rm hi}\bigr).                 \tag{18}
\]

For every pair in (18), finite cyclicity gives

\[
 \operatorname{Tr}(\widetilde W_\alpha H^{\rm hi}_\beta)
 =\operatorname{Tr}\bigl[
 (S^{-1/2}\widetilde W_\alpha S^{-1/2})
 (S^{1/2}H^{\rm hi}_\beta S^{1/2})\bigr].
\]

Use trace duality |Tr(UV)|<=||U||||V||_1 from the cited Watrous
inequalities, together with (3),(4). This proves the first inequality
in (5), with no positivity of a differentiated factor. The factor
three is precisely the external color trace; internal color sums
and the two inverse/resolvent source orders are already included.

Since 12/N^2<=lambda_0<=3pi^2/N^2 and
exp(-7theta_N/6)=N^-7/4, that inequality is at most

\[
 C_f\{N^{-3/4}+N^{-3/4}\sqrt{\ell_N}
                              +N^{-7/4}\ell_N\}
       =O_f(N^{-3/4}\sqrt{\ell_N})=o(1).             \tag{19}
\]

Finally L297(8) is an exact finite polynomial identity, so adding
the low contribution L301(5) and its complete multi-heat bounds
L297(25),(28) gives

\[
 \begin{split}
 |\tau_N(r_N)|\le C_f\{&N^{-1/2}\ell_N^{5/2}
                +N^{-3/4}\sqrt{\ell_N}
                +N^{-1/20}\ell_N^3\\
                &+N^{-17/20}\ell_N^2
                +N^{-17/20}\ell_N^3\}.
 \end{split}                                               \tag{20}
\]

Every term tends to zero and the third controls this sum, proving
(6). The one-heat term retains all four source placements and the
multi-heat terms are imported in full, without subtracting uncontrolled
uncut errors. There is no inference to another proper-time scale,
an uncut bound, reflection positivity or a spectral mass gap.

## Mathlib

Full matching coverage for the relative-cube weighted high response
and its Wilson terminal assembly is **not checked**. Mathlib coverage
of the supporting holomorphic calculus and Schatten inequalities is
also not checked here. The precise primary citations above, rather
than an asserted library theorem, supply those standard inputs.
The new quantitative specialization is subject to a separate audit.
