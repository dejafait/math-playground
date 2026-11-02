# Lemma 669: the signed full-root loss need not be logarithmic

## Hypotheses

Use L649's complete product and L666's exact displacement family. Thus
q>=1 is an integer, n=12q+3, M=4q+1=n/3, x=-d=-5/4,
R=11/8, U=121/64, alpha=27/10, H_0=alpha/n, and t_j=j/n,
0<=j<n. For real |e_r|<=1/8, -2q<=r<2q, take the unit-residue set

    Z_e={x} union {x+i*H_0*(r+1/2+e_r): -2q<=r<2q}.

Keep every grid factor, including j=0, and the denominator angle:

    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    T_M(v)=sum_(0<=k<M) v^k,
    G_e(zeta)=R^(-1) sum_(a in Z_e) W_a(-1)*T_M(a*zeta/R),
    m_e(-1)=mean_(|zeta|=1) log|G_e(zeta)|.

The mean is normalized. G_0 and m_0 refer to all e_r=0. The full
straight path is obtained by replacing e_r with s*e_r, 0<=s<=1.
No fixed actual degree, root separation or noncancellation is assumed.

## Conclusion

For each fixed integer K>=0 there are finite constants C_K>0, N_K
and an integer L_K>=1 with the following property. For every
n=12q+3>=N_K, there is an admissible symmetric displacement vector,
supported on the 2L_K nodes with indices -L_K<=r<L_K, such that

    sup_(|zeta|=1) |G_e(zeta)| <= C_K*n^(-K-1),                 (1)
    m_0(-1)-m_e(-1) >= (K+1)*log n-log(2R*C_K).                (2)

Here e_(-r-1)=-e_r for 0<=r<L_K; all other displacements are zero.
In particular there is a sequence of admissible n_K tending to infinity
and displacement vectors e^(K) for which

    [m_0(-1)-m_(e^(K))(-1)]/log n_K >= K,       K>=1.          (3)

Thus there is no absolute C and onset for
m_e(-1)>=m_0(-1)-C*log n uniformly over the prescribed cube.
This is an actual signed full-mean countersequence, not a lower bound
on an absolute perturbation cost. It applies to the root-plus-leading-
factor expression along the prescribed straight paths, with all roots,
multiplicities, circle crossings and degree drops retained.

The constants and onsets in (1) depend on K; no estimate uniform in K
or effective final onset is asserted. Equations (1)--(3) do not decide
the weaker bound m_e(-1)>=-n/100-C*log n, the angular maximum or the
paid-arc criterion. Arbitrary support, Xi realization and mixed signs
remain open. This is a local obstruction under an EXPLORE assessment,
not an RH candidate or certified originality. The separate conceptual
audit in section 7 accepts (1)--(3) with these qualifications.

## Proof

### 1. Source scope and the bounded countersequence test

Reuse the invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-signed-spatial-root-deformation.md`.
It permits an admissible countersequence for the actual full signed
loss, as an alternative to proving the uniform bound. L664 supplies
only its audited undisplaced full-polynomial approximation and the
product derivative bounds identified below. L668 supplies its exact
nonzero finite-moment identity, not its inverse-data cost. L649 and
L666 specify the products and family. No stopped inverse-data or
scalar angular estimate is substituted for the actual polynomial.

Import F. Brunault and W. Zudilin, *Many Variations of Mahler Measures*,
ISBN 9781108794459,
[Propositions 1.4--1.5, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf):
for a nonzero complex polynomial P of actual degree nu, leading
coefficient gamma and roots beta counted with multiplicity,

    mean log|P|=log|gamma|+sum_(j=1)^nu log max(1,|beta_j|).     (4)

This includes constants and roots on the circle. For path continuity
import C. D. Sinclair, *The range of multiplicative functions on C[x],
R[x] and Z[x]*,
[arXiv:math/0509591v2](https://arxiv.org/pdf/math/0509591v2),
13 July 2007, Theorem 1.1, pp.1--2, with Section 2, pp.12--14.
The root function psi(z)=max(1,|z|), continuous and positive with
psi(z)/|z| tending to one, gives a continuous multiplicative Mahler
measure in each fixed finite-dimensional coefficient space, including
limits with leading-factor loss. Those cases were inspected in the
prior source review; no degree-uniform continuity rate is imported.

The construction below is family-specific: it solves actual nonlinear
moment equations for allowed node displacements, then bounds the
entire spatial polynomial. General root regularity is neither reproved
nor invoked. The finite iteration and its convergence are proved here,
so no quantitative inverse-function or sampling theorem is assumed.
The prior source comparison and scoped local search did not identify
this countersequence; that does not establish novelty.

### 2. Product, admissibility and the local oscillatory limit

For real y, division of the full products at u=-1 gives

    W_(x+i*y)(-1)=product_(0<=j<n) (1+i*b_j*y)/(1-i*A_j*y),
    A_j=1/(d-t_j),          b_j=t_j/(U-d*t_j).                    (5)

The j=0 factor has A_0=1/d and b_0=0. As in L668,

    A_j-b_j=[U-d^2+(d-t_j)^2]/[(d-t_j)*(U-d*t_j)]>0.

Also 0<=b_j<A_j<=4. Hence every weight in (5) is nonzero,
has modulus at most one, and its value at -y is the conjugate of
its value at y. These statements retain all phases in the product.

For all allowed displacements, consecutive nonanchor ordinates have
gap at least 3H_0/4 and distance at least 3H_0/8 from the anchor.
Every ordinate satisfies |y|<2q*H_0<9/20. Thus the nodes are distinct,
and |x+i*y|^2<353/200<(273/200)^2=(R-1/100)^2. These bounds hold
on the entire straight path as well. They verify L666's family
hypotheses and the hypotheses of L668's nonzero identity.

Write

    w_n(t)=W_(x+i*alpha*t/n)(-1),
    g_n=n^(-1) sum_j(A_j+b_j),
    g=integral_0^1 [1/(d-v)+v/(U-d*v)] dv,
    kappa=alpha*g.

The continuous integrand gives g_n->g by Riemann sums. L664, section 3,
proves 9/5<g<11/5: its bounds g(R)>9/5 and g(123/100)<11/5,
together with monotonicity in the real-part parameter, apply at d.
Consequently

    243/50<kappa<297/50,       pi<kappa<2*pi.                    (6)

The latter strict inequalities already follow from 3<pi<22/7.
In particular exp(2i*kappa)!=1. This nonresonance is used only for
finite geometric sums below, not as a uniform spacing hypothesis for
spatial roots.

For every fixed finite T, w_n(t)->exp(i*kappa*t) in C^2([-T,T])
as n tends to infinity in the allowed sequence. Here is a direct
verification for this full product. For n>=8*alpha*T, all individual
logarithms in

    ell_n(t)=sum_j[log(1+i*b_j*alpha*t/n)
                          -log(1-i*A_j*alpha*t/n)]

are the branches given by the power series at 1, with arguments of
modulus at most 1/2. The geometric/logarithmic series give

    |ell_n(t)-i*alpha*g_n*t| <=32*alpha^2*T^2/n,
    |ell'_n(t)-i*alpha*g_n| <=64*alpha^2*T/n,
    |ell''_n(t)| <=128*alpha^2/n.                              (7)

For example the first uses |log(1+z)-z|<=|z|^2 for |z|<=1/2
and sum_j(A_j^2+b_j^2)<=32n. The derivative bounds follow by
differentiating each of the finitely many logarithms, whose denominators
have modulus at least 1/2. Exponentiating and differentiating proves
the C^2 convergence. In particular, for fixed T and all sufficiently
large n, the absolute values of w_n, w'_n and w''_n are all <=100,
since the limiting values have moduli 1, kappa<6 and kappa^2<36.
No estimate uniform in a growing T is needed or claimed.

### 3. Paired controls and an invertible finite Gram limit

Fix K>=0 first. For an integer L>=1 let tau_r=r+1/2, 0<=r<L,
and for j=0,...,K define the real functions

    Psi_(n,j,L)(t)=2 Re[(i*t/L)^j*w_n(t)],
    Psi_(infinity,j,L)(t)=2 Re[(i*t/L)^j*exp(i*kappa*t)].

Set F_n:R^L->R^(K+1), on ||e||_infinity<=1/8, by

    (F_n(e))_j=sum_(r=0)^(L-1)
                 [Psi_(n,j,L)(tau_r+e_r)-Psi_(n,j,L)(tau_r)].   (8)

We will solve F_n(e)=b, where b=(-1,0,...,0). All vector norms
on R^(K+1) below are Euclidean; the control norm is the maximum norm.
Let J_infinity be the Jacobian of F_infinity at zero. With
v_r=tau_r/L, its entries are

    (J_infinity)_(j,r)
      =2*kappa*v_r^j*cos(kappa*tau_r+(j+1)*pi/2)
          +(2j/L)*v_r^(j-1)*cos(kappa*tau_r+j*pi/2).            (9)

The second term is interpreted as zero when j=0. For fixed K,

    L^(-1)*J_infinity*J_infinity^T -> Q,
    Q_jk=2*kappa^2*cos((j-k)*pi/2)/(j+k+1).                   (10)

To justify every term, the second terms in (9) are uniformly O_K(1/L)
and hence disappear from the normalized Gram limit. The product-to-sum
identity for the first terms gives a nonoscillatory midpoint Riemann
sum and a constant multiple of

    L^(-1) sum_(r=0)^(L-1) v_r^(j+k)*exp(2i*kappa*tau_r).

This last expression tends to zero. Indeed partial sums of
exp(2i*kappa*r) have modulus at most 2/|1-exp(2i*kappa)| by (6).
Summation by parts, using that v_r^(j+k) is nondecreasing in [0,1]
(constant for j+k=0), bounds the unnormalized weighted sum by
4/|1-exp(2i*kappa)|. Division by L proves the claim. The remaining
Riemann sum tends to integral_0^1 v^(j+k)dv=1/(j+k+1), giving (10).

The real matrix Q is positive definite: for a nonzero real vector a,

    a^T Q a=2*kappa^2*integral_0^1
                         |sum_(j=0)^K a_j*(i*v)^j|^2 dv>0.   (11)

A nonzero polynomial cannot vanish on an interval; alternatively,
vanishing of this nonnegative continuous integrand would force every
coefficient to be zero. Let lambda_K>0 be the minimum of (11) on
the compact Euclidean unit sphere. Entrywise convergence in the fixed
dimension K+1 now gives an integer L_0(K) such that for all L>=L_0(K),

    J_infinity*J_infinity^T >= (lambda_K*L/2)*I.                (12)

This is a family-specific Gram calculation, not an assertion that
an arbitrary inverse Vandermonde or prescribed inverse-data norm is small.

### 4. The actual finite-n nonlinear equations

For t in [tau_r-1/8,tau_r+1/8], 0<=r<L, one has 0<t/L<1.
Once L is fixed, use (7) on [-L-1,L+1]. Differentiating the powers
in Psi and using the bounds 100 for w_n and its first two derivatives
gives, for all sufficiently large n,

    ||(Psi'_(n,j,L)(t))_(j=0)^K||_2 <= B_K,
    ||(Psi''_(n,j,L)(t))_(j=0)^K||_2 <= H_K,
    B_K=200*(K+1)*sqrt(K+1),
    H_K=200*(K^2+K+1)*sqrt(K+1).                              (13)

For the second bound, each component is at most
200*[j(j-1)/L^2+2j/L+1]<=200*(K^2+K+1); the first is
at most 200*(j/L+1). These inequalities are uniform over the whole
control cube. All constants here depend only on K, not on L or n.
The required onset for (13) may depend on L.

Put A_K=4B_K/lambda_K and choose, once and for all, an integer

    L=L_K >= max{L_0(K), K+1, 16A_K, 4A_K^2*H_K}.             (14)

By C^1 convergence in (7) on this fixed interval and (12), the actual
Jacobian J_n=DF_n(0), for all sufficiently large allowed n, satisfies

    J_n*J_n^T >= (lambda_K*L/4)*I.

Thus its real right inverse T_n=J_n^T*(J_n*J_n^T)^(-1) satisfies

    J_n*T_n=I,        ||T_n v||_infinity <= (A_K/L)*||v||_2.   (15)

In fact each row of T_n is a column of J_n, of norm at most B_K,
times an inverse matrix of operator norm at most 4/(lambda_K*L).
This proves the asserted norm and includes all columns.

Write R_n(e)=F_n(e)-J_n e, and set rho=2A_K/L<=1/8. Taylor's
formula in each real coordinate in (8), with (13), gives

    ||R_n(e)||_2 <= (H_K*L/2)*||e||_infinity^2,
    ||R_n(e)-R_n(f)||_2
          <=H_K*L*rho*||e-f||_infinity,
                     ||e||_infinity,||f||_infinity<=rho.      (16)

For the second inequality, the derivative of each coordinate remainder
has vector norm at most H_K*rho; sum its integral over the L coordinate
segments. Independence of the summands in (8) introduces no mixed
second derivatives.

Consider the explicit iteration, starting at e^(0)=0,

    e^(l+1)=Phi_n(e^(l)),
    Phi_n(e)=T_n*(b-R_n(e)).                                 (17)

Equations (14)--(16), with ||b||_2=1, imply

    ||Phi_n(e)||_infinity
       <=(A_K/L)*(1+2H_K*A_K^2/L)<=2A_K/L=rho,
    ||Phi_n(e)-Phi_n(f)||_infinity
       <=(2A_K^2*H_K/L)*||e-f||_infinity
       <=(1/2)*||e-f||_infinity.                             (18)

The iterates stay in the closed cube. Their successive differences
are bounded by a geometric sequence with ratio 1/2, so they are Cauchy
in R^L and converge to a vector e in that cube. Continuity in (17)
gives e=T_n(b-R_n(e)); multiplying by J_n proves
J_n e=b-R_n(e), hence F_n(e)=b. This proves existence for the actual
n, not merely for its limiting exponential model. It also specifies
the vector by a convergent finite-dimensional iteration.

Increase the n onset so that L<=2q, then use these controls on the
positive node pairs by setting e_(-r-1)=-e_r for 0<=r<L and all
other e_r=0. The vector is admissible by (18) and section 2. The order
of choices is K, then L_K, then an onset for every sufficiently large
n in the allowed sequence. No simultaneous uniform limit is used.

### 5. Cancellation and a bound for the whole spatial polynomial

For a function f of the pole variable a, define the finite signed
bookkeeping functional

    D_n[f]=f(x)+sum_(r=0)^(L-1) {
       w_n(tau_r+e_r)*f(x+i*H_0*(tau_r+e_r))
       +w_n(-tau_r-e_r)*f(x-i*H_0*(tau_r+e_r))
       -w_n(tau_r)*f(x+i*H_0*tau_r)
       -w_n(-tau_r)*f(x-i*H_0*tau_r) }.

This expresses the anchor plus the difference of the new and old
unit-residue configurations; it does not change any final original
residue to a signed residue. Conjugation in (5) shows exactly that

    D_n[1]=1+(F_n(e))_0=0,
    D_n[(a-x)^j]=(H_0*L)^j*(F_n(e))_j=0,       1<=j<=K.       (19)

These are the actual finite-product moments. For |zeta|=1 put
f(a)=T_M(a*zeta/R), retaining all M spatial terms. On |a-x|<=1/16
one has |a|<=21/16 and |a|/R<=21/22. Differentiating this finite
geometric polynomial and bounding its derivative by the infinite
geometric majorant gives

    |f^(K+1)(a)|/(K+1)!
       <=1/[R^(K+1)*(1-21/22)^(K+2)]
       =R*16^(K+2).                                        (20)

The bound follows term by term from
sum_(k>=K+1) binomial(k,K+1)*v^(k-K-1)=(1-v)^(-K-2)
for 0<=v<1. This is a convergent scalar majorant, not a replacement
of the actual polynomial. If M<=K+1 the derivative is zero and the
same bound remains true. Taylor's integral remainder on the segment
from x to a, with (20), is therefore at most

    R*16^(K+2)*|a-x|^(K+1).                                (21)

For our fixed L, increase n so that H_0*(L+1)<=1/16. All modified
and old nodes occurring in D_n then lie in this disk. Every weight
has modulus at most one by (5). Equation (19) cancels the Taylor
polynomial of f through order K, and the anchor has zero remainder.
There are 4L remaining terms. Thus, uniformly on the spatial circle,

    R^(-1)*|D_n[T_M(a*zeta/R)]|
          <= C'_K*n^(-K-1),
    C'_K=4L*16^(K+2)*[alpha*(L+1)]^(K+1).                    (22)

L664 applies to the undisplaced family with delta=1/4 and h=2H_0:
its two positive grids h(l+1/4), h(l+3/4) are precisely
H_0(r+1/2), 0<=r<2q. For n>=183 its audited equation (1) is

    sup_|zeta|=1 |G_0(zeta)-R^(-1)*T_M(x*zeta/R)|
                                      <=1000*n*exp(-n/3000). (23)

The exact finite change of nodes gives

    G_e(zeta)=[G_0(zeta)-R^(-1)*T_M(x*zeta/R)]
                           +R^(-1)*D_n[T_M(a*zeta/R)].       (24)

Combine (22)--(24). Since K is fixed, there is an onset after which
1000*n*exp(-n/3000)<=n^(-K-1). Therefore (1) holds with
C_K=C'_K+1. No initial spatial prefix, tail, grid factor or phase has
been discarded; K is a Taylor order in the pole variable, not a
truncation of the spatial polynomial. The constants can be very large,
which is harmless for this countersequence and is not uniform control
as K grows.

### 6. Full roots, the straight path and the divergent signed loss

For each fixed n and its constructed vector, every coefficient of
G_(s e) is real analytic in s on a neighborhood of [0,1]: it is a
finite sum of the rational products (5) and polynomial powers at
affine real ordinates, and all their real-path denominators are nonzero.
No slice G_(s e) is the zero polynomial. Indeed L668's exact identity,
with the degree-at-most-M-1 interpolant F(z_a)=1/W_a(-1) at the
distinct z_a=a/R, reads

    sum_(k=0)^(M-1) f_k*c_k=M/R!=0.

The hypotheses hold at every s by section 2. Only this finite identity
is used; its interpolation cost plays no role in (1).

Sinclair's cited theorem now applies within the fixed coefficient
space of degree at most M-1, separately for each n. The multiplicative
Mahler measure is continuous and positive on this compact path, so
its logarithm m_(s e)(-1) is continuous. For each s let nu_s be the
actual degree, gamma_s its nonzero actual leading coefficient, and
beta_(s,j) its complete multiset of roots. The imported identity gives

    m_(s e)(-1)=log|gamma_s|
                   +sum_(j=1)^(nu_s) log max(1,|beta_(s,j)|). (25)

At a circle contact the corresponding log max term is zero, and every
multiplicity is counted. At a degree change, (25) uses the actual
degree on each side and at the junction; the cited fixed-degree-space
continuity includes the combined leading-factor/escaping-root limit.
It is not legitimate to discard either part of that expression. No
global root labeling, local monic normalization, root derivative or
integration through singular crossings is used here. Monic root
regularity consequently is not an input requiring extra hypotheses.

For each nonzero polynomial, its finite logarithmic mean is bounded
above by the logarithm of its circle supremum. Thus (1) and (25) give

    m_e(-1)<=log C_K-(K+1)*log n.                            (26)

L664, section 5, gives c_0(-1)>=1/(2R) for G_0 after one absolute
onset. Its application of (4) at the constant coefficient gives
m_0(-1)>=-log(2R). Include that onset in N_K. This proves (2) for the difference of the two
complete expressions (25), including their actual leading factors.
It is a bound on the signed net loss, not on absolute root speeds.

For K=1,2,..., choose successively an allowed n_K=12q_K+3 greater
than n_(K-1) and the established onset N_K, and with
n_K>=max{K,2R*C_K}. Use the displacement vector defined by (17)
for this K and n_K. Such an n_K exists because all thresholds are
finite before it is chosen. Equation (2) then gives

    m_0(-1)-m_(e^(K))(-1)
          >=(K+1)*log n_K-log(2R*C_K)>=K*log n_K,

which is (3). This sequence and its allowed straight paths contradict
any absolute logarithmic-loss constant and onset. They provide no
off-line zeta zero and no conclusion on the independent linear-rate
benchmark. The route decision is to stop this stronger uniform
stability claim; the separate audit below accepts that local stop.

### 7. Separate conceptual audit — 2 November 2026

The unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-signed-spatial-root-countersequence-audit.md`
authorizes this audit. The following checks accept (1)--(3), including
their fixed-K onsets and endpoint interpretation. No correction to the
construction or constants was needed. This verifies the existing local
obstruction; it adds no stronger estimate, source theorem or originality
claim. The weaker linear-rate benchmark remains undecided.

**Exact family and limiting product.** At u=-1 the ratio of the j-th
factors is

    (x+t_j)/(x+i*y+t_j) * (U+t_j*(x+i*y))/(U+t_j*x)
       =(1+i*b_j*y)/(1-i*A_j*y).

Thus (5) has the stated signs, including j=0, and uses the complete
product. Its positive denominators give A_j<=4 and
A_j-b_j>0, so |w_n(t)|<=1 for every real t, without a small-t
assumption. The separation and radius estimates in section 2 hold
for every s*e in the original cube, including nonsymmetric vectors;
the constructed vector is a permitted symmetric subfamily.

L664's monotonicity gives g(R)<=g(d)<=g(123/100), hence the strict
bounds used in (6). Since 243/50>22/7 and 297/50<6, they imply
pi<kappa<2*pi using only 3<pi<22/7. This excludes exactly the
resonance exp(2i*kappa)=1 needed in the Gram calculation. For fixed T,
the first log remainder is bounded by
alpha^2*T^2*n^(-2)*sum_j(A_j^2+b_j^2). The differentiated remainders
introduce factors at most 2 and 4, respectively, from the denominators.
The bound sum_j(A_j^2+b_j^2)<=32n therefore verifies all three
constants in (7). Exponentiation gives the claimed C2 convergence
on that fixed interval; no growing-interval limit is used.

**Real rank and the two limits.** Differentiating Psi gives both
terms of (9), with the derivative of t^j interpreted as zero at j=0.
In the leading-term product, the identity for two cosines gives the
factor 2*kappa^2 in (10), rather than 4*kappa^2. The other term is
an oscillatory weighted geometric sum. Its partial sums are bounded
by 2/|1-exp(2i*kappa)|; the endpoint weight and total variation of
v_r^(j+k) are each at most one. This verifies the displayed bound
4/|1-exp(2i*kappa)| and convergence after division by L. The terms
containing j/L or k/L vanish in the normalized sum for fixed K.

The matrix in (10) is real symmetric. Expanding the modulus square
in (11) gives its cosine entries exactly, including zero cross terms
between even and odd indices. A nonzero polynomial has positive
integral of its squared modulus on [0,1], so lambda_K>0. Compactness
and entrywise convergence apply in the fixed dimension K+1. First
choose L using this limiting Gram matrix. Then, for that finite L,
the C1 convergence in n gives the actual Gram bound with denominator
4. Neither order of limits is reversed.

**Actual-n solvability and all cube constraints.** On every coordinate
interval, 0<t/L<1 and L>=1. The first and second derivatives of
(i*t/L)^j supply precisely j/L and j(j-1)/L^2, so (13) bounds
the whole derivative columns and their variations, not just their
values at the undisplaced nodes. Multiplication by the inverse Gram
matrix gives the row bound A_K/L in the Euclidean-to-maximum norm.
The separable sum in (8) has no mixed control derivatives; integrating
each column remainder and summing verifies both bounds in (16).

With L>=4A_K^2*H_K, the self-mapping estimate in (18) is in fact at
most 3A_K/(2L), which is below rho=2A_K/L. Its Lipschitz constant
is at most 1/2, and L>=16A_K gives rho<=1/8. The explicit iteration
therefore converges inside the real closed cube. Multiplying the
fixed-point equation by J_n is valid since J_n*T_n=I and proves
F_n(e)=b for the actual finite product. The subsequent condition
L<=2q keeps all modified nodes in the family. It also implies
M=4q+1>=2L+1>=2K+3: the cancellation order does not exhaust all
M moments and cannot force the zero polynomial by a dimension error.

**Whole spatial polynomial.** The negative node with index -r-1
has ordinate -H_0*(tau_r+e_r), and its weight is the conjugate of
the positive node's. Pairing their centered j-th powers gives
(H_0*L)^j Psi_(n,j,L), with an additional anchor value only for j=0.
This verifies both identities (19), with no missing imaginary equations
and no change to the final unit residues. The paired old terms are
subtracted only in the finite bookkeeping identity (24).

For |a-x|<=1/16, the derivative series majorant in (20) is
R^(-K-1)*22^(K+2)=R*16^(K+2). Taylor's integral remainder along
the straight segment to a has the factor 1/(K+1)!, so (21) follows
with that same constant. All 4L old/new nonanchor terms have weight
modulus at most one and displacement from x at most alpha*(L+1)/n.
The anchor remainder is zero. This verifies C'_K and its independence
of M in (22). In particular the canceled Taylor polynomial is in the
pole variable a; no spatial coefficient or spatial tail is removed.

For delta=1/4, the positive grids of L664 are H_0*(2l+1/2) and
H_0*(2l+3/2), whose union is exactly the positive undisplaced grid.
Their negative partners and additional anchor also match. Thus its
audited full-polynomial error applies to (24). After K and L are
fixed, n^(K+2)*exp(-n/3000) tends to zero, which justifies the
remaining absorption into C_K=C'_K+1 for all sufficiently large
allowed n. There is no estimate uniform in K implicit here.

**Nonzero paths, actual roots and diagonal choice.** Each coefficient
on the straight path is rational in s with no real denominator zero
on [0,1], hence real analytic on a neighborhood of that interval.
At every s the M nodes are distinct and all weights are nonzero.
The finite interpolation identity of L668 therefore has right side
M/R, excluding the identically zero polynomial at each slice. Its
binomial cost bound is not needed and supplies no hidden lower bound
for this audit. Sinclair applies for this fixed n in coefficient
dimension M, allowing actual degree loss. Positivity of Mahler measure
on nonzero polynomials and compactness give a positive path minimum
for this n only. Thus its logarithm is continuous as used in (25).
The imported root formula covers constants, multiple roots and circle
roots; the combined leading-factor/escaping-root limit is retained.
No logarithmic derivative or root labeling is needed.

The circle supremum bounds the finite logarithmic mean from above,
while L664's constant coefficient bounds the undisplaced mean from
below. They give exactly (2). For each K, all thresholds N_K and
2R*C_K are finite before n_K is chosen. Choose the next allowed n_K
strictly larger than the preceding one and at least these thresholds.
Then log(2R*C_K)<=log n_K gives (3). For any proposed absolute
loss constant and onset, a sufficiently large K has both K above
that constant and n_K beyond that onset, yielding a contradiction.
Nothing bounds this loss below by a fixed positive multiple of n_K;
in particular the audit does not contradict the weaker -n/100-C log n
benchmark or control an angular maximum.

## Mathlib

Reuse the inspected official
[MahlerMeasure module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html).
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.mahlerMeasure_pos_of_ne_zero` support the nonzero
full-root interpretation. No formalization of the paired-control
construction, its dimension-dependent onsets or this countersequence
has been checked. Sinclair's full degree-drop continuity coverage in
Mathlib has not been checked here. Unknown availability is not absence.
Section 7 is a separate informal conceptual audit; no Lean verification
or numerical certificate is claimed.
