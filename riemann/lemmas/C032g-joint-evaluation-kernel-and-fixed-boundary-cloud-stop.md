# Corollary C032g: joint evaluation kernel and a fixed boundary-cloud stop

## Hypotheses

Use C032f(12)-(25), with its full theta kernel and constants
0<c<1, alpha=1-c>0, beta=1+c>0 and a=1/8. Put

\[
 \Omega=\{z:\Re z>0\},\qquad H=L^2((0,\infty),du;\mathbb C^2),
 \quad F(z)=2\Xi(2iz),
\]
\[
 d_\sigma(z)=\alpha F(z+\sigma a)-\beta F'(z+\sigma a),\qquad
 R(z)=\frac{F(z+a)+F'(z+a)}{z+1},\qquad \sigma=-,+.
 \tag{1}
\]

The measure and both component norms are unweighted. Inner products
are linear in the first variable. For y in H let

\[
 (Ty)(z)=\sum_\sigma d_\sigma(z)
       \int_0^\infty e^{-zu}y_\sigma(u)\,du.
 \tag{2}
\]

This defines an analytic function, not an asserted bounded map into
the usual H2 output space. Let Z be the common-zero set of d_- and d_+
in Omega. No assumption about Z, simplicity of Xi zeros, or RH is made.

For the boundary test fix a real tau, a positive integer N, and
distinct w_1,...,w_N in Omega. Set z_j(epsilon)=i*tau+epsilon*w_j,
where epsilon>0 tends to zero. N, tau and the w_j remain fixed.

## Conclusion

The evaluation representer and range kernel are

\[
 (k_z)_\sigma(u)=\overline{d_\sigma(z)}e^{-\bar z u},\qquad
 K(z,w)=\langle k_w,k_z\rangle
 =\frac{\sum_\sigma d_\sigma(z)\overline{d_\sigma(w)}}{z+\bar w}.
 \tag{3}
\]

For a finite list z_1,...,z_n in Omega, let
G_ij=K(z_i,z_j) and b_i=R(z_i). The interpolation equations
(Ty)(z_i)=b_i are solvable exactly when b is orthogonal to ker G.
When solvable, their minimum squared H norm is b*G^dagger*b, where
G^dagger denotes the Hermitian Moore-Penrose inverse. If the points
are distinct and outside Z, G is positive definite. Consequently an
incompatible finite set of ordinary evaluations requires a point
z in Z with R(z) nonzero; zero rows with zero RHS and repeated points
create no other incompatibility.

The full equation Ty=R has an H preimage exactly when R vanishes on Z
and these minimum squared norms, over all finite subsets of Omega\Z,
have one finite upper bound. Equivalently there is one M<infinity with

\[
 M^2G-bb^*\succeq0
 \tag{4}
\]

for every finite subset of Omega, including its common-zero points.
No particular M is imposed by C032f. Passing finitely many systems
does not prove this assertion.

For the fixed boundary family above, G_epsilon is positive definite
for all sufficiently small epsilon and its minimum squared norm obeys

\[
 b_\epsilon^*G_\epsilon^{-1}b_\epsilon
 =\epsilon\,\frac{|r|^2}{\|D\|_{\mathbb C^2}^2}
       \mathbf1^*C^{-1}\mathbf1+O(\epsilon^2)\longrightarrow0,
 \qquad C_{ij}=\frac1{w_i+\bar w_j}.
 \tag{5}
\]

Here D is a nonzero vector and r is a scalar specified in the proof;
all constants may depend on the fixed data. Thus this particular joint
family cannot supply either finite incompatibility or diverging minimum
norms, even when the boundary coefficient vector vanishes. Growing N,
varying tau, degenerating w configurations, interior common zeros and
full membership remain undecided. This is a negative test of a proposed
obstruction family, not membership, a delta decision, or Xi positivity.
The conceptual audit1280 below accepts (3)-(9) at this fixed-data
scope without changing their statements.

## Proof

### Imported results and scope

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-17-theta-joint-evaluation-review-1276.md`.
Its source comparison1275/completed1276 is reused without new browsing.
Import R. Hamilton, *Pick Interpolation and the Distance Formula*,
Waterloo PhD thesis (2012), Proposition2.1.7 and Remark2.1.8, pp15-16,
[primary thesis](https://dspacemainprd01.lib.uwaterloo.ca/server/api/core/bitstreams/5cb1b66f-d860-4f95-963e-898cda124537/content).
For an RKHS with nonzero evaluations, membership is equivalent to one
norm bound M making every finite kernel matrix minus the corresponding
rank-one value matrix positive semidefinite as in (4); the least M is
the norm. Its converse uses finite Douglas factorization and weak
compactness. We use the norm convention of its statement and remark.

The range construction and minimum-preimage interpretation are from
J. H. Manton and P.-O. Amblard, *A Primer on Reproducing Kernel Hilbert
Spaces*, arXiv1408.0952v2 (5 November2015), Sections2.5,5.1,6.1-6.2,
Theorem6.2.1 and Proof6.2.2,
[primary text](https://arxiv.org/html/1408.0952v2).
The explicit complex conventions and finite singular systems below
specialize these results; we do not reprove a general RKHS theorem.
The theta symmetry and boundary Taylor orders are additional local
work needed to test the selected family. No global multiplier or
corona theorem is imported.

For comparison with Hardy terminology only, C. Seifert, S. Trostorff
and M. Waurick, *Evolutionary Equations*, OTAA287 (2022), Chapter8,
Theorem8.1.2/Corollary8.1.3, pp121-124,
[primary chapter](https://link.springer.com/content/pdf/10.1007/978-3-030-89397-2_8.pdf),
identify unnormalized half-line Laplace transforms isometrically with
the Hardy norm squared (1/(2pi))*sup_(x>0) integral_R |Y(x+it)|^2 dt.
The argument here stays in H, so no 2pi normalization is suppressed
and no assertion about the weighted sum's Hardy norm is needed.

### Individual evaluations, analytic range and finite systems

For each z in Omega the squared norm of k_z is
(|d_-(z)|^2+|d_+(z)|^2)/(2 Re z), finite. Cauchy-Schwarz gives
(Ty)(z)=<y,k_z>. On compact subsets of Omega, exponential decay
dominates the integrals and their z derivatives against L2 inputs;
for example u^j exp(-eta*u) is in L2 for eta>0 and j=0,1.
Together with the analytic coefficients this proves holomorphy.
Integrating exp(-(z+bar w)u) proves (3) with its stated order of
inner products and conjugations.

Let U be the closed span of the k_z in H. The kernel of the function
map T is U-perp; restriction to U makes its range an RKHS with the
quotient/minimum-preimage norm. This is the cited range construction,
with complex inner products as fixed above. The representer vanishes
precisely at Z. This set is not all of Omega: C032f(21)-(22) show that
the two coefficients never vanish together on the positive real axis.
Apply Hamilton on Omega\Z, where evaluations are nonzero, and impose
R(z)=0 at Z. This proves the full uniform criterion. Alternatively
including such points in (4) forces -|R(z)|^2>=0 in each zero row.
No zero evaluation with a nonzero RHS is discarded.

To spell out the finite singular case, let T_S:H->C^n be evaluation
on the selected list. Its adjoint is T_S*lambda=sum_j lambda_j k_zj,
and T_S T_S*=G. In finite dimensions ran T_S=ran G=(ker G)-perp.
If b belongs to this range, y_0=T_S*G^dagger b solves the equations,
lies in ran T_S*, and is orthogonal to ker T_S. Thus it is the
minimum-norm solution and
||y_0||^2=b*G^dagger G G^dagger b=b*G^dagger b. These formulas
also include G=0,b=0, with minimum zero. The matrix condition (4)
is equivalent to this compatibility and b*G^dagger b<=M^2, by
diagonalizing the Hermitian positive semidefinite matrix G and using
Cauchy-Schwarz on its positive eigenspace. If M=0 it requires b=0.

For distinct z_j outside Z, suppose T_S*lambda=0. In each component,
sum_j lambda_j conjugate(d_sigma(z_j))*exp(-conjugate(z_j)u)=0
almost everywhere in u>0. The continuous functions therefore vanish
everywhere on that interval. Differentiate 0,...,n-1 times at one
u_0>0. The resulting Vandermonde matrix in the distinct numbers
-conjugate(z_j), with nonzero exponential column factors, is
invertible. Hence lambda_j conjugate(d_sigma(z_j))=0 for both
sigma. Each coefficient vector is nonzero, so every lambda_j=0.
It follows that G is positive definite. Duplicate sample points
give duplicate equations with the same RHS; common-zero rows are
the only additional issue. This proves the finite assertions.

### Boundary common zeros and exact vanishing orders

C032f's full-density formula for F makes it an even entire function
with F(bar z)=conjugate(F(z)) and F(0)>0. In particular it is not
identically zero. Fix z_0=i*tau and v=a+i*tau. Evenness and conjugation
give F(z_0-a)=conjugate(F(v)) and
F'(z_0-a)=-conjugate(F'(v)). Therefore

\[
 d_-(z_0)=\alpha\overline{F(v)}+\beta\overline{F'(v)},\qquad
 d_+(z_0)=\alpha F(v)-\beta F'(v).
 \tag{6}
\]

Because alpha and beta are positive, both quantities vanish if and
only if F(v)=F'(v)=0. This does not assert absence of such a zero.

If the vector in (6) is nonzero, take p=0, D=(d_-(z_0),d_+(z_0))
and r=R(z_0). All three functions are analytic near z_0, since
1+z_0 is nonzero, and their Taylor expansions give

\[
 d_\sigma(z_0+h)=D_\sigma h^p+O(h^{p+1}),\qquad
 R(z_0+h)=r h^p+O(h^{p+1}).
 \tag{7}
\]

If both quantities vanish, let the finite multiplicity of the zero
of F at v be m>=2, and write F(v+h)=A h^m+O(h^(m+1)), A nonzero.
The local identity F(-bar v+h)=conjugate(F(v-bar h)) shows that
its leading coefficient at -bar v is (-1)^m*conjugate(A).
Differentiate these analytic Taylor series. Equation (7) now holds
with p=m-1 and

\[
 D_-=-\beta m(-1)^m\bar A,\qquad D_+=-\beta m A,\qquad
 r=\frac{m A}{1+i\tau}.
 \tag{8}
\]

Both components of D and r are nonzero in this case. The Taylor
remainders are genuine analytic remainders in a fixed neighborhood;
there is no assertion uniform in tau or in the zero multiplicity.
In particular the RHS vanishes to the same order as the coefficients,
so a boundary common zero does not leave a lower-order forcing term.

### Simultaneous boundary-family norms

The matrix C in (5) is strictly positive definite: it is the Gram
matrix of the distinct scalar exponentials exp(-bar w_j*u); the
same Vandermonde argument applies. Its smallest eigenvalue is positive.
Every w_j is nonzero, so W=diag(w_1^p,...,w_N^p) is invertible.
Substitute h=epsilon*w_j into (7), with the finite set fixed. The
denominators in (3) are exactly epsilon*(w_i+bar w_j). Thus

\[
 G_\epsilon=\epsilon^{2p-1}
 W\big(\|D\|^2 C+E_\epsilon\big)W^*,\quad
 b_\epsilon=\epsilon^p W(r\mathbf1+e_\epsilon),\qquad
 \|E_\epsilon\|+\|e_\epsilon\|=O(\epsilon).
 \tag{9}
\]

The finite-dimensional remainder bound follows entrywise from the
Taylor remainders and the fixed nonzero denominators; E_epsilon is
Hermitian. Once its norm is less than half the smallest eigenvalue
of ||D||^2 C, that middle matrix is positive definite. Its inverse
is (||D||^2 C)^(-1)+O(epsilon), by the inverse identity or a Neumann
series. Consequently G_epsilon is invertible and substitution into
the minimum-norm formula yields

\[
 b_\epsilon^*G_\epsilon^{-1}b_\epsilon
 =\epsilon(r\mathbf1+e_\epsilon)^*
   (\|D\|^2C+E_\epsilon)^{-1}(r\mathbf1+e_\epsilon),
\]

which proves (5). This also covers r=0. In the common-zero case (8),
|r|^2/||D||^2=1/(2 beta^2(1+tau^2)); it is finite and positive.
Thus even that case has minimum squared norm tending to zero.

The optimizing y may depend on epsilon. Their small norms do not
produce a common solution of Ty=R on Omega: the evaluation points
move to its boundary, and the corresponding functional norms also
vary. No limit interchange, global norm bound, or positivity inference
is made. C032f's witness equivalence and Douglas reduction remain
pending independent audit; (3)-(9) alone do not settle them or delta.
The completed attempt1278 parks this fixed boundary family. It is a
known-RKHS specialization with an explicit negative analytic test,
not a claim of originality beyond the inspected sources.

### Independent conceptual audit — 17 November2026, step1280

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-17-joint-boundary-cloud-audit-review-1278.md`,
separately approved1279. The complete proof above was checked, using
only C032f's stated constants, (16)-(22) and the full-density facts
there supplied by C032e(5)-(9). The latter give an even real positive
density with every fixed exponential moment finite. Consequently F
is even, entire, real under conjugation and nonzero since F(0)>0.
No part of C032f's Douglas or adjoint-witness equivalence is needed
to audit this evaluation range. Their independent audits remain open.
The already inspected Hamilton and Manton--Amblard results are reused
at the exact scope and with the precise citations above.

**Complex orientation and feasibility.** With the first-variable-linear
convention, conjugating k_z in <y,k_z> produces d_sigma(z)e^(-zu),
as required. In <k_w,k_z> the same convention produces
d_sigma(z) conjugate(d_sigma(w)) and denominator z+bar w.
For the finite map, <T_S y,lambda>=<y,sum_j lambda_j k_zj>;
therefore T_S T_S*=G with G_ij=K(z_i,z_j), and
lambda*G lambda=||T_S*lambda||^2. These verify the orientation used
by both the nullspace condition and the minimum-norm formula.
Orthogonality to ker G is essential even when G^dagger exists.
The positive-eigenspace calculation of (4) includes M=0 and the
all-zero system. Distinct points outside Z have independent vector
representers by the displayed componentwise Vandermonde argument;
each point need have only one nonzero component. Thus duplicate rows
with identical R values introduce no extra compatibility condition.

Hamilton is applied only to Omega\Z, with one bound over every finite
set. Nonemptiness of this domain follows from C032f(21)-(22): the
strictly increasing real logarithmic derivative cannot take t0 at
both r-a and r+a. The closed-span range construction gives a preimage
in the original H, not a presumed Hardy output space. At Z the full
equation still requires R=0; the matrix inequality enforces it even
on a one-point set. No finite-family bound is substituted for the
global uniform quantifier, and no additional assertion about derivative
interpolation at interior common zeros is made.

**Every boundary multiplicity.** At z0=i*tau, evenness and real
conjugation give F(z0-a)=bar F(a+i*tau) and the negative sign for
F'. Conjugating d_-(z0)=0 and combining with d_+(z0)=0 gives
2 alpha F(v)=0 and 2 beta F'(v)=0. Since alpha,beta>0 this is
equivalent to F(v)=F'(v)=0. Conversely that simultaneous vanishing
does make both coefficients zero. F is not the zero function, so
any such zero has a finite order m>=2. The full local identity is
F(-bar v+h)=overline(F(v-bar h)); hence its leading coefficient is
(-1)^m bar A. Differentiation of the convergent Taylor series lowers
the order exactly to m-1. The alpha F term has strictly higher order
and cannot cancel -beta F'. Division of F+F' by 1+z0+h is harmless
because 1+z0 is nonzero. This verifies every coefficient and order
in (7)-(8) for every m>=2. In the other case p=0 and D is nonzero,
but r is allowed to vanish. No simplicity or RH premise enters.

**Quantitative check of the fixed-data remainder.** The following
bounds make explicit the inverse-perturbation step already used in
(9); they do not strengthen (5) to varying data. Define analytic
quotients, with their removable values at h=0,

    g(h)=(d_-(z0+h),d_+(z0+h))/h^p,    q(h)=R(z0+h)/h^p.

Choose rho>0 so that both are analytic on a neighborhood of the
closed disk |h|<=rho and rho<|1+z0|. Then g(0)=D, q(0)=r.
Finite derivative suprema L_g,L_q on this disk give
||g(h)-D||<=L_g|h| and |q(h)-r|<=L_q|h| by integration along
the segment from zero to h. Use Euclidean vector norms and their
induced matrix norms. Put

    w_max=max_j |w_j|>0,
    d_min=min_(i,j) |w_i+bar w_j|>0,
    lambda0=||D||^2 lambda_min(C)>0,
    K_E=N(2||D|| L_g w_max+L_g^2 w_max^2)/d_min,
    K_e=sqrt(N) L_q w_max.

The strict positivity of C is the scalar-exponential Vandermonde
case already checked above; positive real parts give d_min>0.
For 0<epsilon<=min(1,rho/w_max), set
eta_j=g(epsilon*w_j)-D. The exact middle-matrix error in (9) is

    (E_epsilon)_ij=
      (sum_sigma g_sigma(epsilon*w_i)
                    conjugate(g_sigma(epsilon*w_j))-||D||^2)
      /(w_i+bar w_j),
    (e_epsilon)_j=q(epsilon*w_j)-r.

The numerator is bounded in modulus by
||D||(||eta_i||+||eta_j||)+||eta_i||||eta_j||.
Thus the maximum entry bound, followed by ||E||<=N max_ij|E_ij|,
gives ||E_epsilon||<=K_E epsilon; also
||e_epsilon||<=K_e epsilon. These are full complex bounds, and
E_epsilon is Hermitian. The factors epsilon^(2p-1), epsilon^p and
W in (9) follow exactly from h^p at each endpoint and the denominator
epsilon(w_i+bar w_j); W is invertible since every w_j is nonzero.

Write A0=||D||^2 C and choose

    0<epsilon<=epsilon0
      =min(1,rho/w_max,lambda0/[2(K_E+1)]).

Then ||E_epsilon||<lambda0/2, so A0+E_epsilon is positive definite,
||(A0+E_epsilon)^(-1)||<=2/lambda0, and the inverse identity gives

    ||(A0+E_epsilon)^(-1)-A0^(-1)||
      <=2 K_E epsilon/lambda0^2.

In the squared-norm expression after (9), expand around r*1.
The preceding estimates, including both cross terms and the e-square,
give the explicit error bound

    |b_epsilon* G_epsilon^(-1)b_epsilon
       -epsilon |r|^2 1*C^(-1)1/||D||^2|
    <=epsilon^2 [2 K_E N|r|^2/lambda0^2
                 +4 sqrt(N)|r| K_e/lambda0+2 K_e^2/lambda0].

This includes r=0; no positive leading coefficient is assumed in
that case. In the common-zero case (8), ||D||^2=2 beta^2 m^2|A|^2
and |r|^2=m^2|A|^2/(1+tau^2), verifying the ratio following (9).
All constants, including rho, derivative bounds, w_max, d_min and
lambda_min(C), are tied to the fixed data. In particular small
lambda_min(C) or moving tau cannot be ignored to obtain a growing
or degenerating cloud estimate.

Audit verdict: (3)-(9) pass without a mathematical repair. The explicit
bound verifies the original O(epsilon^2) assertion and validates the
fixed-family stop1278. It neither supplies a uniform global M nor
tests an interior incompatible common zero. The minimizing profiles
may vary with epsilon. Delta, source metric, the actual-Xi signed
bridge, initialization and all-degree positivity remain unresolved.
This is an audit of a known-framework specialization, not a new
RKHS theorem or a claimed advance beyond the sources checked.

## Mathlib

The complete two-component theta range, its common-zero analysis and
the finite-family asymptotic were not checked in Mathlib. Availability
is unknown. The imported RKHS and half-line transform citations above
are mathematical references, not claims of Lean coverage. No numerical
certificate or formal verification is asserted. The informal conceptual
audit1280 above verifies only the stated fixed-data specialization.
