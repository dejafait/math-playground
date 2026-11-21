# Lemma 777: conditional interior-zero compression in the original Hilbert norm

## Hypotheses

Use G, r, k=r-1, R, the normalized factors b,c and the operator
A=Q_r H(b)H(tilde c)Q_r of L776. In particular r>=2, R>0, G(0)>0,
G has real coefficients, G(R)>0, there is no zero on |w|=R, and exactly
k zeros lie inside that circle, counted with multiplicity. These are
assumptions about the actual G, not conclusions from minor signs.

Write its distinct normalized interior zeros as alpha_1,...,alpha_s,
with multiplicities m_j>=1 and sum m_j=k. Thus 0<|alpha_j|<1. Put

\[
 P(z)=\prod_{j=1}^s(z-\alpha_j)^{m_j},\quad
 P_j(z)=P(z)/(z-\alpha_j)^{m_j},\quad F(z)=G(Rz)/P(z),\quad
 p(z)=z^{-k}P(z).
\]

Removable values are understood in F. Choose sigma>1 so that F is
holomorphic and zero-free on a neighborhood of |z|<=sigma. Such a
sigma exists for each fixed admissible pair, but no uniform choice or
numerical lower bound is asserted. All Hilbert spaces below are complex;
sequence coordinates start at 1, and the inner product is conjugate-linear
in its first entry. Finite matrix norm means largest singular value,
written ||.||_op; ||.||_HS denotes Hilbert–Schmidt norm, to avoid L776's
different use of the subscript 2.

The error certificate below has additional explicitly conditional input
data. It does not assert that those data have been obtained for Xi.

## Conclusion

The exact factor normalization, with no omitted scalar, is

\[
 \phi_-=p,\qquad \phi_+=F,\qquad b=p/F,\qquad c=F/p=z^kF/P.       \tag{1}
\]

Define the principal-part coefficients and normalized derivative columns by

\[
 d_{j,h}=\frac1{(m_j-h)!}
   \left[\frac{d^{m_j-h}}{dz^{m_j-h}}
     \frac{z^kF(z)}{P_j(z)}\right]_{z=\alpha_j},\quad 1\le h\le m_j,
                                                                    \tag{2}
\]
\[
 v_{j,p}(i)=\frac1{p!}\left[\frac{d^p}{dz^p}z^{i-1}\right]_{z=\alpha_j},
 \quad i\ge1,\quad 0\le p<m_j.                                    \tag{3}
\]

The derivative convention sets this entry to zero when p>i-1; otherwise
it is binom(i-1,p) alpha_j^(i-1-p). Let V have these k columns, let
W=conj(V), and let C be block diagonal, with block j given by

\[
 C_{(j,p),(j,q)}=
 \begin{cases}d_{j,p+q+1},&p+q<m_j,\\0,&p+q\ge m_j.\end{cases}       \tag{4}
\]

Then B=H(tilde c)=VCW*, of rank at most k. With

\[
 U=Q_rH(b)V,\quad Y=Q_rW,\quad
 K=(U^*U)^{1/2}C(Y^*Y)^{1/2},
\]

there is an exact original-norm identity

\[
                         \|A\|=\|K\|_{\rm op}.                     \tag{5}
\]

Both Gram matrices are essential. No selfadjointness, zero simplicity,
real-zero premise, invertible Gram matrix or coefficient-minor sign is
required. The matrix K is finite, but its entries still depend on F;
(5) by itself is not an effective or small upper bound.

Here is one fully specified conditional finite certificate. Choose
0<a<rho<1<sigma and approximate nodes and residues satisfying

\[
 |\alpha_j|,|\widehat\alpha_j|\le a,\quad
 |\alpha_j-\widehat\alpha_j|\le e_j,\quad
 |d_{j,h}-\widehat d_{j,h}|\le e_{j,h}.                              \tag{6}
\]

The multiplicities and the grouping of the true zeros must already be
certified. The e_(j,h) must enclose the complete derivatives in (2),
including uncertainty in F, the evaluation point and P_j; they are not
errors in F alone. Approximating nodes may coincide or vanish. Define

\[
 \widehat S(z)=\sum_{j,h}\frac{\widehat d_{j,h}}{(z-\widehat\alpha_j)^h},
 \quad t=\rho-a>0,\quad
 M_S=\sum_{j,h}|\widehat d_{j,h}|t^{-h},
\]
\[
 E_S=\sum_{j,h}\left(e_{j,h}t^{-h}
                  +h|\widehat d_{j,h}|e_jt^{-h-1}\right),\quad
 h_B=M_S\frac{\rho}{1-\rho^2},\quad
 \delta_B=E_S\frac{\rho}{1-\rho^2}.                                \tag{7}
\]

Let beta_n=b_n for n>=1. Supply m_sigma>0 with
|F(z)|>=m_sigma on |z|=sigma, an integer N>r, coefficients
widehat beta_1,...,widehat beta_N and certified errors
|beta_n-widehat beta_n|<=epsilon_n. Set

\[
 M_b=\frac{(1+a/\sigma)^k}{m_\sigma},\quad q=\sigma^{-2},\quad
 T_N(q)=\frac{q^{N+1}((N+1)-Nq)}{(1-q)^2},
\]
\[
 h_b=\left(\sum_{n=1}^N n|\widehat\beta_n|^2\right)^{1/2},\quad
 \delta_b=\left(\sum_{n=1}^N n\epsilon_n^2+M_b^2T_N(q)\right)^{1/2}.
                                                                    \tag{8}
\]

Construct widehat V,widehat W,widehat C from the hatted nodes/residues
by (3)–(4), and put widehat b(z)=sum_(n=1)^N widehat beta_n z^n.
The nonzero rows of widehat U=Q_rH(widehat b)widehat V are the finite rows

\[
 \widehat U_{i,(j,p)}=
 \sum_{h=1}^{N-i+1}\widehat\beta_{i+h-1}
       \frac1{p!}\left[\partial_z^p z^{h-1}\right]_{z=\widehat\alpha_j},
 \quad r+1\le i\le N.                                             \tag{9}
\]

For widehat Y=Q_r widehat W its finite Gram matrix is explicitly

\[
 (\widehat Y^*\widehat Y)_{(j,p),(l,q)}
 =\frac1{p!q!}
   \left[\partial_x^p\partial_y^q\frac{(xy)^r}{1-xy}\right]
       _{x=\widehat\alpha_j,\ y=\overline{\widehat\alpha_l}}.        \tag{10}
\]

Thus widehat K=(widehat U*widehat U)^(1/2) widehat C
(widehat Y*widehat Y)^(1/2) is a k by k finite matrix. In (10) the q
in a column label is a derivative order, unrelated to q in (8).
All square roots are the positive semidefinite ones. For a certified
finite-matrix upper bound U_fin>=||widehat K||_op, define

\[
 E=\delta_b h_B+h_b\delta_B+\delta_b\delta_B.
 \qquad \boxed{\ \|A\|\le U_{\rm fin}+E\ }.                        \tag{11}
\]

For example, if a computed matrix K_0 has a certified error
||widehat K-K_0||_op<=eta_K and its norm is certified <=u_0, then
U_fin=u_0+eta_K is admissible. The error eta_K must include the Gram
entries, square roots and finite arithmetic; a floating-point SVD alone
does not supply it. The exact matrix, or a rigorous norm enclosure of
it, is required even when its Gram matrices are singular.

An actual certified U_fin+E<1 would pay L776's norm premise for this
pair only. No such inequality or actual enclosure data are proved here.

## Proof

**Known inputs and scope of the specialization.** The finite-rank
rational-Hankel theorem is V. V. Peller, *An excursion into the theory of
Hankel operators*, MSRI Publications 33 (1998), Section 4, Theorem 4.1
and Corollaries 4.2–4.3, printed pp.76–77
([primary chapter](https://library.slmath.org/books/Book33/files/peller.pdf)).
The complex confluent sequence convention is also stated in K.-M.
Perfekt and A. Pushnitski, *On Helson matrices*,
[arXiv:1611.03772v2](https://arxiv.org/pdf/1611.03772v2), Section 6.2,
Theorem 6.1, PDF pp.18–19: derivative evaluations at nodes strictly
inside the disk give bounded finite-rank classical Hankel forms.
No Helson or positivity conclusion is imported.

The metric-correct finite singular-value reduction is W. B. Gragg and
L. Reichel, *On singular values of Hankel operators of finite rank*,
NPS-53-89-003 (November 1988), Section 1, Proposition 1.1,
(1.11)–(1.17) and Remark 1.1, printed pp.1–5
([primary report](https://calhoun.nps.edu/server/api/core/bitstreams/e5e56899-62e6-4986-a73b-d8ee92dba669/content)).
That remark permits confluent data but omits their details. The polar
decomposition used below is the standard theorem, for example J. Shapiro,
*Functional Analysis*, MAT520 Fall 2024, version 25 December 2024,
Section 9.4, Theorem 9.25 and proof, pp.90–91
([author notes](https://web.math.princeton.edu/~js129/PDFs/teaching/MAT520_fall_2024/MAT520_Lecture_Notes.pdf)).

These results give the established mechanism. The calculations below
check its actual-G normalization, repeated-pole indexing and full-product
metric, which the general sources do not state in this form, and give
an explicit Cauchy/triangle-inequality budget. They do not reprove the
general rational-Hankel theorem or supply a new norm-smallness principle.

**Factor identification.** Removing the interior zeros with their exact
multiplicities makes F entire and nonzero on the closed unit disk.
Compactness and isolation of zeros give the asserted neighborhood and
some sigma>1. Since the zero multiset is invariant under conjugation,
P and F have real coefficients. Real roots of P lie in (-1,1), so their
factors 1-alpha are positive; nonreal conjugate pairs contribute
|1-alpha| squared. Consequently P(1)>0 and F(1)=G(R)/P(1)>0.

For |z|>max|alpha_j| the absolutely locally convergent sum

\[
 L_-(z)=-\sum_{j=1}^s m_j\sum_{n\ge1}\frac{\alpha_j^n}{nz^n}
\]

is a logarithm of p, has only strictly negative Laurent powers and
tends to zero at infinity. Conjugation symmetry makes L_-(1) real;
therefore L_-(1)=log P(1), with the real logarithm. The zero-free disk
admits a holomorphic logarithm L_+ of F normalized by
L_+(1)=log F(1). It has only nonnegative Taylor powers. On their common
annulus L_-+L_+ is the logarithm of phi in L776: its value at 1 is
log G(R). Uniqueness with that normalization and uniqueness of Laurent
coefficients identify its negative and nonnegative pieces. Exponentiating
proves (1), including the scalar in phi_+.

**Principal parts and the confluent factor.** On the disk of radius
sigma, c has just the poles alpha_j, with orders m_j. Indeed the
numerator alpha_j^k F(alpha_j) is nonzero and P_j(alpha_j)!=0.
Taylor expansion at each pole gives (2). With
S(z)=sum_(j,h) d_(j,h)/(z-alpha_j)^h, the function c-S extends
holomorphically to the disk, so has no negative Laurent coefficients.
For |z|>|alpha|,

\[
 \frac1{(z-\alpha)^h}
 =\sum_{n\ge h}\binom{n-1}{h-1}\alpha^{n-h}z^{-n}.
\]

In particular the source's zero-based Hankel sequence is c_(-(n+1)).
For i,l>=1 the contribution of this pole to B_(i,l)=c_(-(i+l-1))
is

\[
 \sum_{h=1}^{m_j} d_{j,h}\frac1{(h-1)!}
      \left[\partial_z^{h-1}z^{i+l-2}\right]_{z=\alpha_j}
 =\sum_{p,q\ge0,\ p+q<m_j}d_{j,p+q+1}v_{j,p}(i)v_{j,q}(l).        \tag{12}
\]

This is the normalized Leibniz rule, including its zero cases. The
first two negative coefficients are c_(-1)=sum_j d_(j,1) and
c_(-2)=sum_j(alpha_j d_(j,1)+d_(j,2)), with d_(j,2)=0 when m_j=1.
Thus (12) starts at the coefficient c_(-1), not c_0 or c_(-2), and
the same indexing includes the first nontrivial repeated-pole case.
The columns v are in l2 because polynomial factors times |alpha_j|^i
are square summable. Formula (12) identifies the bounded operators
B=VCV^T=VCW* first on coordinate vectors and then on their dense
span. Both sides are bounded: the right side is finite rank, and the
left side has the annular coefficient bounds in L776 (or the Cauchy
bounds below). The transpose is bilinear; W=conj(V) is essential.
The argument applies equally to the hatted rational S, even with
coincident nodes, zero nodes or vanishing top residues, because the
derivative formula still makes sense. Those approximations need not
have rank k. At a zero approximate node the column with label p is
exactly the coordinate vector e_(p+1); it never requires evaluating a
negative power of zero. Coincident approximate nodes can produce
dependent columns. Neither case affects the support argument below.

**Original-norm compression.** Multiplying the preceding factorization
gives A=UCY*. Write the polar decompositions
U=J_U G_U^(1/2) and Y=J_Y G_Y^(1/2), with G_U=U*U and G_Y=Y*Y.
Their initial spaces are S_U=(ker G_U)^perp and S_Y=(ker G_Y)^perp.
Then A=J_U K J_Y*, and K=P_(S_U) K P_(S_Y). The partial isometries
imply ||A||<=||K||_op. Conversely if K!=0, choose a unit vector x in
S_Y attaining its norm (finite dimension). The vector J_Y x has norm
one, and
||A J_Y x||=||J_U Kx||=||Kx||. The equality is immediate if K=0.
This proves (5) without assuming either Gram matrix invertible. The
same proof gives ||widehat A||=||widehat K||_op for
widehat A=Q_r H(widehat b)widehat B Q_r and
widehat B=H(tilde widehat S).

For completeness the exact U entries are convergent sums
U_(i,jp)=sum_(h>=1) beta_(i+h-1) v_(jp)(h), i>r, with rows zero
otherwise. The geometric beta bound below and the polynomial-geometric
columns justify absolute convergence. The finite version is (9), since
H(widehat b) has rows zero for i>N. Finally, with n=i-1,

\[
 (Y^*Y)_{(j,p),(l,q)}
 =\sum_{n\ge r}\frac{\partial_x^p x^n}{p!}
                         \frac{\partial_y^q y^n}{q!}
       \bigg|_{x=\alpha_j,y=\overline{\alpha_l}}.
\]

The product is conjugated in exactly this order because Y=Q_r conj(V).
On compact subdisks, the geometric series and all the finitely many
derivatives converge absolutely and uniformly. Differentiating
sum_(n>=r)(xy)^n=(xy)^r/(1-xy) proves (10), both for the exact and
hatted Gram matrices. The denominators are nonzero since |xy|<=a^2<1.

**Pole and derivative errors.** On |z|=rho the segment between alpha_j
and widehat alpha_j remains in |alpha|<=a. Differentiating
(z-alpha)^(-h) with respect to alpha and integrating along that segment
gives

\[
 |(z-\alpha_j)^{-h}-(z-\widehat\alpha_j)^{-h}|
       \le h e_j(\rho-a)^{-h-1}.
\]

Split each summand of S-widehat S as
(d-widehat d)/(z-alpha)^h plus widehat d times the difference of the
two powers. Equations (6)–(7) give
sup_(|z|=rho)|S-widehat S|<=E_S and sup|widehat S|<=M_S.
Both rational functions have only strictly negative Laurent powers on
this circle. Cauchy's Laurent formula therefore bounds their nth
negative-coefficient difference by E_S rho^n, and the hatted
coefficient by M_S rho^n, for every n>=1. Since an nth Hankel
coefficient occurs exactly n times,

\[
 \|B-\widehat B\|\le\|B-\widehat B\|_{\rm HS}
   \le E_S\left(\sum_{n\ge1}n\rho^{2n}\right)^{1/2}=\delta_B,
 \qquad \|\widehat B\|\le h_B.                                   \tag{13}
\]

There is no omitted analytic part of c: it contributes zero to B.
If desired, a supplied bound |F|<=M_(F,rho) on |z|=rho gives the
separate exact estimate
||B||_HS <= M_(F,rho)(1-a/rho)^(-k) rho/(1-rho^2).
Neither estimate removes F from the residues (2). An exact choice
widehat alpha=alpha, widehat d=d permits delta_B=0 because (12)
then identifies the entire operator, not just finitely many entries.

**Remaining-factor and truncation errors.** On |z|=sigma,
|p(z)|<= (1+a/sigma)^k. Equation (1) and the supplied lower bound
give |b(z)|<=M_b. Laurent Cauchy estimates yield
|beta_n|<=M_b sigma^(-n), n>=1. Thus

\[
 \|H(b)-H(\widehat b)\|^2
 \le\|H(b)-H(\widehat b)\|_{\rm HS}^2
 \le\sum_{n=1}^N n\epsilon_n^2
       +M_b^2\sum_{n>N}n\sigma^{-2n}=\delta_b^2.                  \tag{14}
\]

The geometric-series derivative gives the displayed T_N(q) in (8).
Also ||H(widehat b)||<=h_b by the same exact coefficient count.
No condition on the negative coefficients of b is needed for H(b).
In particular b need not be holomorphic at zero: the bound uses its
Laurent integral on |z|=sigma in the punctured disk where F is zero-free, not
a Taylor coefficient estimate across the pole of p at zero.

To make the analytic-factor dependence of epsilon_n explicit, the
following is one sufficient way to provide it. Supply a holomorphic,
zero-free approximant widehat F on a neighborhood of |z|<=sigma and
bounds on |z|=sigma

\[
 |F-\widehat F|\le E_F,\quad |F|\ge m_\sigma>0,\quad
 |\widehat F|\ge\widehat m_\sigma>0.
\]

Let widehat p=product_j(1-widehat alpha_j/z)^(m_j), and let
widehat beta_n approximate the nth Laurent coefficient of
widehat p/widehat F to error theta_n. Telescoping the k factors gives

\[
 E_p=\frac{\sum_j m_j e_j}{\sigma}(1+a/\sigma)^{k-1},\quad
 M_p=(1+a/\sigma)^k,\quad
 E_b=\frac{E_p}{m_\sigma}
          +\frac{M_pE_F}{m_\sigma\widehat m_\sigma}.
\]

Indeed p/F-widehat p/widehat F=(p-widehat p)/F+
widehat p(widehat F-F)/(F widehat F). Cauchy's formula now justifies
epsilon_n=theta_n+E_b sigma^(-n). The theta_n must include coefficient
extraction or quadrature errors. Bounds on F and its reciprocal,
or these coefficient enclosures by another valid method, are required
input data; analyticity alone supplies no numerical constants.
The residues still require the derivative enclosures in (6).

**Full-product error and threshold.** Let Delta_H=H(b)-H(widehat b)
and Delta_B=B-widehat B. Expanding the full difference gives

\[
 A-\widehat A=Q_r\bigl(\Delta_H\widehat B
               +H(\widehat b)\Delta_B+\Delta_H\Delta_B\bigr)Q_r.
\]

The projections are contractions, so (13)–(14) and submultiplicativity
bound its norm by E in (11), including the cross error. Applying the
exact norm compression to widehat A and then the triangle inequality
proves (11). This is an operator-norm estimate, not a determinant
error or an unweighted coefficient bound. All its quantities are finite
under the stated conditional data; no favorable size is inferred.

L776's sufficient sign implication can be applied only if these actual
inputs give U_fin+E<1. L776 itself has not received an independent
critical audit here. The present specialization supplies no actual
zero count, enclosure, norm inequality, universal radius, growing-r
estimate or real-zero conclusion. Equal zero moduli or multiplicities
may prevent the required zero counts for some r; other indices and
the all-degree mixed positivity assembly remain open. No numerical
experiment is used in this proof.

**Conceptual audit, 2026-11-04 (step428).** The conditional statements
(1)–(14) pass the normalization, conjugation, confluent-index, singular-
support and error-transfer audit. The checks above include the first
two negative coefficients, zero/coincident approximate nodes, the
projection's starting index n=r, and the punctured-disk Laurent estimate.
The two supports in (5) and the cross term in (11) remain necessary;
neither a raw coefficient matrix nor an unweighted coefficient error
was substituted for the original operator norm. Approximate nodes need
not respect conjugation symmetry: this audit only uses their complex
norm enclosures, not a real determinant sign for the approximation.
No mathematical defect was found and no statement was strengthened.
This validates a local specialization of the cited general results,
not a bound U_fin+E<1 or L776's independently pending Fredholm/sign
identity. Exact true multiplicity grouping, certified derivatives,
positive reciprocal bounds and finite-matrix enclosure remain premises.

## Mathlib

Full matching coverage is not checked; neither presence nor absence
of this complete specialization is claimed. The primary inputs above
and the standard holomorphic logarithm theorem, Laurent/Cauchy
coefficient formula, normalized Leibniz rule, finite-rank polar
decomposition and operator-norm inequalities are the informal coverage.
No formal verification or independently audited Xi norm certificate
is asserted.
