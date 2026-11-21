# Lemma 869: the bounded-profile package does not make the Green data jointly positive

## Hypotheses

Fix any real ell and any H>0. Write T2=(R/(2pi Z))^2 and use
the normalized angular Fourier convention

\[
 \widehat h_n(x)=(2\pi)^{-2}\int_{[0,2\pi]^2}
             h(x,y)e^{-i n\cdot y}\,dy.
 \tag{1}
\]

The necessary-condition package being tested consists of a real
nonnegative C1 function h on R2 times T2, its mean m=hhat_0,
and C1 profiles U_n:R->C for every nonzero n in Z2, such that

\[
 \widehat h_n(x)=U_n(n\cdot x),\qquad |U_n(t)|\leq H,
 \qquad m(s,s)=m(\ell,s)=H\quad(s,t\in\mathbb R).
 \tag{2}
\]

Retain reality, so U_(-n)(t)=overline(U_n(-t)). Also require C3
profiles B_n with U_n=B_n-B_n'', and all the opposite-index tests:
for each x, N>=0, and c_0,...,c_N in C,

\[
 a_0(x)=H,\quad a_k(x)=\widehat h_{(k,-k)}(x)\ (k\ne0),
 \qquad \sum_{j,l=0}^{N}c_j\overline{c_l}a_{j-l}(x)\geq0.
 \tag{3}
\]

These are precisely the abstract restrictions specified in the
prior assessment
`drafts/literature/2026-11-06-bounded-profile-green-positivity-scope.md`.
C868a/C868b motivate this package; their actual-F hypotheses are
not asserted here. In particular, this lemma does not assume or
produce real q,r satisfying actual-F domination and both closure
equations. It does not assert that (2)-(3) characterize that class.

The proposed Green data are

\[
 b_0(x)=H,\qquad
 b_n(x)=\frac12\int_{\mathbb R}e^{-|n\cdot x-u|}U_n(u)\,du
                   \quad(n\ne0).
 \tag{4}
\]

## Conclusion

For every ell and H>0 there are explicit finite-mode data satisfying
the entire package above for which, at x*=(ell+12,ell), the matrix
[b_(j-l)(x*)] indexed in the order

\[
 E=(0,(1,0),(0,1),(1,1))
 \tag{5}
\]

has the negative quadratic form

\[
 \sum_{j,l\in E}c_j\overline{c_l}b_{j-l}(x^*)
       =H(4-6\kappa)<-\frac{8H}{7},
 \qquad c=(1,-1,-1,1).
 \tag{6}
\]

Here kappa is the scalar integral specified below. The witness is
analytic, not a sampled eigenvalue. Thus the package does not imply
joint positivity of (4), even on the stated four-index set. The
positive H case suffices to refute that implication. When H=0,
the assumed bound makes every U_n zero and the matrix in (4) zero;
no contrary claim is made for this degenerate case.

The independent exact audit of 6 November 2026 below accepts this
construction without changing its hypotheses or conclusion.
It stops only this necessary-condition implication. It gives neither
a counterexample to the full L868 admissible class, nor a period
inequality, graph realization or conclusion about RH.

## Proof

### Source reuse and the role of the explicit calculation

The invocation-start EXPLORE assessment covers exactly (2)-(5),
including compatibility with one nonnegative h and every test (3).
Its source comparison found no theorem that establishes the joint
implication. Reuse its inspected scalar Green formula from
Klaus-Jochen Engel and Rainer Nagel, *One-Parameter Semigroups for
Linear Evolution Equations*, GTM194, Springer (2000),
[VI.4.1, proof (4.2)-(4.3), pp384-386](https://www.math.uni-tuebingen.de/de/forschung/agfa/members/engel-nagel_one-parameter-semigroups.pdf#page=400).
At lambda=mu=1 the kernel is exp(-|t|)/2. The profiles constructed
below are compactly supported and continuous, hence belong to
the source's continuous functions with finite endpoint limits.
There is no extension to arbitrary endpoint behavior here.
The short split-integral calculation below verifies the additional
C3 requirement for these C1 profiles; it is an applicability check,
not a new general resolvent theorem.

Use the quadratic-form criterion for finite positive semidefinite
Hermitian matrices in Rajendra Bhatia, *Positive Definite Matrices*,
Princeton (2007), [Section1.1, pp1-2](https://assets.press.princeton.edu/chapters/s8445.pdf).
The explicit negative form will disprove positivity directly.
Neither Bochner's converse nor an infinite reconstruction theorem
is needed. The scalar kernel and finite matrix criterion are known
inputs; the source search does not certify originality of this
particular countermodel.

### A compact C1 profile and one globally nonnegative h

Define the even function

\[
 p(t)=
 \begin{cases}
  1,& |t|\leq2,\\
  1-3v^2+2v^3,\quad v=|t|-2,&2<|t|<3,\\
  0,& |t|\geq3.
 \end{cases}
 \tag{7}
\]

On 0<=v<=1 the middle polynomial is (1-v)^2(1+2v),
has derivative 6v(v-1)<=0, and has values 1 and 0 at the
two endpoints. Its derivative vanishes at both endpoints.
Thus 0<=p<=1 and p is C1, including at +/-2 and +/-3;
it is constant near zero, so the absolute value there causes
no regularity problem.

Put X=x1-ell, Y=x2-ell, and set

\[
 p_1(x)=p(X-12),\quad p_2(x)=p(Y),\quad
 p_3(x)=p(X+Y-12),\quad p_4(x)=p(X-Y-12).
 \tag{8}
\]

Define

\[
 \begin{split}
 m(x)&=H\left(1+2\sum_{1\leq i<j\leq4}p_i(x)p_j(x)\right),\\
 h(x,y)&=m(x)+H\bigl(p_1\cos y_1+p_2\cos y_2
              -p_3\cos(y_1+y_2)-p_4\cos(y_1-y_2)\bigr).
 \end{split}
 \tag{9}
\]

These are real C1 functions, and h is periodic in both angles.
Let P=sum p_i and Q=sum p_i^2. Since 0<=p_i<=1, Q<=P.
The cosine terms in (9) are bounded below by -HP. Therefore

\[
 \frac{h(x,y)}{H}\geq1+P^2-Q-P
                  \geq1+P^2-2P=(P-1)^2\geq0.
 \tag{10}
\]

In particular there is one globally nonnegative h, not a collection
of separately chosen coefficients. Each cosine in (9) has zero
angular mean, so its actual mean is exactly m.

On x=(ell,s), write v=s-ell. The four cutoffs in (8) are
0,p(v),p(v-12),p(v+12), where evenness of p was used for the
fourth. The last three have supports contained respectively in
[-3,3], [9,15], [-15,-9], which are pairwise disjoint.
At most one cutoff is nonzero, so every pair product in m vanishes.
Consequently m(ell,s)=H for every real s.

On x=(s,s), write v=s-ell. The cutoffs are
p(v-12),p(v),p(2v-12),0. The first three have supports contained
respectively in [9,15], [-3,3], [9/2,15/2], again pairwise
disjoint. Thus m(s,s)=H for every s. These support statements
include the endpoints, at which p is zero. No limit in s or
interchange of an infinite Fourier series is involved.

### Every profile, its reality condition and the subgroup tests

Let

\[
 n_1=(1,0),\quad n_2=(0,1),\quad n_3=(1,1),\quad n_4=(1,-1),
 \qquad (\varepsilon_1,\varepsilon_2,\varepsilon_3,\varepsilon_4)
                              =(1,1,-1,-1).
\]

With x*=(ell+12,ell), put t_i=n_i dot x*, so
(t_1,t_2,t_3,t_4)=(ell+12,ell,2ell+12,12). For these four
frequencies and their negatives define

\[
 U_{n_i}(t)=\frac{H\varepsilon_i}{2}p(t-t_i),\qquad
 U_{-n_i}(t)=\overline{U_{n_i}(-t)}
            =\frac{H\varepsilon_i}{2}p(t+t_i).
 \tag{11}
\]

For every other nonzero n define U_n=0. The eight listed frequencies
are distinct. The elementary Fourier formula for each cosine in
(9) now gives hhat_n(x)=U_n(n dot x) for every nonzero n.
All these profiles are C1, compactly supported, and bounded in
absolute value by H/2<=H. Their reality identity holds on all R,
not merely at x*.

For fixed x, the coefficients of (3) are

\[
 a_0=H,\qquad a_1=a_{-1}=-Hp_4(x)/2,\qquad a_k=0\ (|k|\geq2).
\]

They are exactly the normalized circle Fourier coefficients of
the nonnegative density rho_x(theta)=H(1-p_4(x)cos(theta)).
Hence for every N and every complex c_0,...,c_N,

\[
 \sum_{j,l=0}^{N}c_j\overline{c_l}a_{j-l}
 =\frac1{2\pi}\int_0^{2\pi}\rho_x(\theta)
       \left|\sum_{j=0}^{N}c_j e^{-ij\theta}\right|^2d\theta\geq0.
 \tag{12}
\]

This verifies the full family (3) by an identity with a finite
sum for arbitrary N; checking selected minors is not being substituted
for that family.

### The C3 profile relation

For each nonzero n let B_n(t) be the Green integral in (4) with
n dot x replaced by t. It converges absolutely, since U_n is
bounded and compactly supported (or zero). For clarity, set

\[
 A_n(t)=\int_{-\infty}^{t}e^{-(t-u)}U_n(u)\,du,\qquad
 D_n(t)=\int_t^{\infty}e^{-(u-t)}U_n(u)\,du.
\]

The fundamental theorem of calculus, with the integrals restricted
to a fixed compact support locally in t, gives
A_n'=U_n-A_n and D_n'=D_n-U_n. It follows that

\[
 B_n=(A_n+D_n)/2,\qquad B_n'=(D_n-A_n)/2,\qquad
 B_n''=B_n-U_n,\qquad B_n'''=B_n'-U_n'.
 \tag{13}
\]

Every derivative displayed is continuous; thus B_n is C3 and
U_n=B_n-B_n''. The even real kernel and the change of variable
u->-u also give B_(-n)(t)=overline(B_n(-t)). Selecting this particular
bounded solution constructs the required profiles. It asserts
neither boundedness nor the removal of homogeneous terms for
arbitrary B_n in the package.

### The complete four-index negative witness

Define the finite positive number

\[
 \kappa=\frac12\int_{\mathbb R}e^{-|u|}p(u)\,du.
 \tag{14}
\]

Since p=1 on [-2,2] and p>=0 elsewhere,

\[
 \kappa\geq1-e^{-2}>6/7.
 \tag{15}
\]

The strict inequality uses the exponential series with positive
terms: e^2>1+2+2+4/3+2/3=7. This gives an exact rational
margin; no rounded value of the integral is needed.

At x*, n_i dot x*=t_i. Substitution u=t_i+v in (4) and (11)
therefore gives b_(n_i)(x*)=H epsilon_i kappa/2. The negative
frequencies have the same real values by (13), or directly by
the evenness of p and the kernel. Write a=kappa/2. In the order
(5) the full matrix, including its prescribed zero coefficient, is

\[
 [b_{j-l}(x^*)]_{j,l\in E}
 =H\begin{pmatrix}
 1&a&a&-a\\
 a&1&-a&a\\
 a&-a&1&a\\
 -a&a&a&1
 \end{pmatrix}.
 \tag{16}
\]

Multiplication by c=(1,-1,-1,1) gives H(1-3a)c.
As sum |c_j|^2=4, the quadratic form is
4H(1-3a)=H(4-6kappa)<-8H/7 by (15). This proves (6).

All the necessary conditions (1)-(3) have now been checked for
the same h and profiles. The matrix fails because the prescribed
mass H need not be the mean where the modes overlap: at x*,
all four p_i equal 1 and the actual mean is 13H. Smoothing the
nonzero profiles does not restore positivity with mass H in this
example. The proof does not test a transform with a different zero
coefficient or with additional actual-F constraints. In particular,
no estimate for K=A+H relative to -|M| follows in either direction.
The earlier one-sided, diagonal and fixed-fiber period stops keep
their original scopes.

### Independent exact audit, 6 November 2026

The audit used the unchanged approved assessment
`drafts/literature/2026-11-06-green-joint-counterexample-audit.md`
and compared the full proof with the exact necessary-condition
package in the preceding assessment. C868a/C868b's full actual-F
premises were read as scope boundaries, not additional assumptions
that this example has proved. The source inputs above are reused;
this audit is verification of the submitted construction, not a
new theorem or a claim of originality.

The following checks are exact and cover the quantifiers in the
statement, rather than a finite radial or angular sample.

1. The transition polynomial has endpoint values 1,0 and endpoint
   derivatives 0,0. It is decreasing on [0,1], so p is globally C1
   and takes values in [0,1]. The absolute value is harmless near
   zero because p is constant there. Thus every p_i, m and h is C1
   on all of R2 times T2. With P=sum p_i and Q=sum p_i^2,
   m/H=1+P^2-Q and h/H>=1+P^2-Q-P>=(P-1)^2. This verifies
   global nonnegativity for the very same h used in all tests.
2. On X=0 the potentially nonzero support intervals in Y are
   [-3,3], [9,15], [-15,-9]; on X=Y the intervals in X are
   [9,15], [-3,3], [9/2,15/2]. They are pairwise disjoint on
   each line, and the fourth cutoff on each line is identically
   zero. Hence all six pair products vanish on both entire lines,
   including endpoints, and both actual means equal H. Translation
   by ell imposes no restriction on ell.
3. The four positive frequencies are distinct and none equals a
   negative one. Their phases in n dot x are centered at
   ell+12, ell, 2ell+12,12 respectively. Formula (11) therefore
   gives every nonzero Fourier coefficient of (9), including the
   negative indices by evenness of p. All other profiles are zero.
   The bound H/2, C1 regularity and conjugacy hold globally, not
   just at the witness point.
4. The only nonzero opposite-index coefficients are a_1=a_-1
   =-Hp_4/2. Expanding the finite square with the negative
   exponential convention in (12) gives exactly a_(j-l), so the
   identity holds for every N, including N=0, and arbitrary
   complex coefficients. Its density is nonnegative because
   0<=p_4<=1. No convergence or reconstruction premise is used.
5. For each profile, including the zero ones, the two split
   integrals have derivatives A'=U-A and D'=D-U. They yield
   B''=B-U and B'''=B'-U', with continuous derivatives across
   every cutoff endpoint. Thus the required global C3 relation
   holds. The real even kernel also gives the asserted negative
   profile conjugacy. This is an existence choice of B, not a
   uniqueness assertion for unrestricted profile solutions.
6. In the order (5), the six differences above the diagonal are
   -n_1,-n_2,-n_3,n_4,-n_2,-n_1. Their entries divided by H
   are a,a,-a,-a,a,a, where a=kappa/2. The corresponding
   c_j c_l are -1,-1,1,1,-1,-1. Thus each unordered pair
   contributes -2Ha and the four diagonal terms contribute 4H.
   This independently gives 4H-12Ha=H(4-6kappa), agreeing with
   the displayed matrix multiplication. The matrix is real
   symmetric, so this is a valid Hermitian quadratic-form test.
7. Integration over [-2,2] gives kappa>=1-e^(-2). The terms
   through degree four in exp(2) sum exactly to 7, and its
   positive degree-five term makes exp(2)>7. Consequently
   kappa>6/7 and H(4-6kappa)<-8H/7 for every H>0. The H=0
   qualification is also correct: all U_n and all b_n vanish;
   this asserts no radial constancy of an original h.

No mathematical defect or missing assumption within the stated
package was found. The accepted result is only the obstruction
to joint positivity with prescribed zero mode H. The actual mean
13H at x* confirms why there is no contradiction with the original
h being nonnegative. In particular, this audit supplies no q,r
obeying actual-F domination or the full closure equations, and no
period, graph-realization or actual-Xi sign conclusion. The
unchanged package is stopped; stronger trace or domination
constraints require a separately assessed test.

## Mathlib

Full matching Mathlib coverage of this counterexample and the
prescribed Green/Fourier operator was not checked. No absence claim
is made. The proof uses finite Fourier polynomials, the cited scalar
Green kernel and a finite quadratic form; no formalization or
machine-checked proof is claimed.
