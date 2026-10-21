# L201 — Uniform mass approximation of the bulk quadratic factors

## Hypotheses

Use exactly L198 and L200's SU(2) relative cube, admitted even N,
a=8/N, straight lower-rooted direction-1 forest, full compact
displacement and both actual L010 probes i=3,6 at tau=1/16. The bare
expansion is taken at fixed mesh first. All coordinates are ordinary
stored full-link coordinates. Keep all faces, normal end edges,
constant own-direction modes and the complete external heat sums.

Write Delta=C^T C+DD^T, Sigma=Delta^(-1), S=Sigma P=P Sigma,
A=PAP, T=2SA. The three colors of z have covariance S independently.
The signed A includes both residual insertion subtractions. Keep
L194's quadratic b and L198's exact expansion

    SB_i=a^2 sum_(k,l) d_(i;kl) n_k e_l^T,
    n_k=S e_k, beta_k=(I-Pi_n)(I-D Phi)n_k,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p).              (1)

Here beta_k is the bulk exterior only; the actual upper exterior is
still in L198's H. Pi_n is not moved through a projection. Set
b_l^c=<e_l,b^c>. Fix an action collar of a constant number of lattice
layers containing every plaquette stencil touching a physical face,
as in L200 section 3. No residual stencil meets this collar for
sufficiently fine meshes.

For fixed k,c, use the following exact decomposition of the two
quadratic directional derivatives:

    q_R(z)=d script R_3(z)[beta_k^(c)]=q_R^d(z)+q_R^0(z),
    q_S(z)=d script S_3(z)[beta_k^(c)]=q_S^d(z)+q_S^0(z). (2)

The definition of the superscript d is by the original product rule,
not by a projection of covariance. In the action, retain outside the
collar precisely <Cz,dw_2(z)[beta_k^(c)]>. In the residual force/vector
part retain G_1(z)dX_2(z)[beta_k^(c)] and
dG_2(z)[beta_k^(c)]X_1(z). In each of its two insertion subtractions
retain the terms where its linear circulation factor is still a rough
z field and the derivative hits the quadratic factor. Their original
weights and signs are unchanged. All other terms, including the entire
action collar, define q_R^0,q_S^0. This is the splitting in L200
section 4, using L149/L155's full coordinate-correct words.

For 0<epsilon<=1 define the self-adjoint spectral filter

    F_epsilon=(Delta/(Delta+epsilon I))^(1/2),
    z_epsilon=F_epsilon z.                            (3)

This is a coupling to the original Gaussian, not an independent field.
P commutes with Delta, so its covariance is P(Delta+epsilon I)^(-1).
Both prefixes in b, all exterior vectors, and A,T remain unchanged.

## Conclusion

Define the finite signed approximation

    B_(i,N)^epsilon=2a^2 sum_(k,l,c)d_(i;kl)
      E[b_l^c {q_R^d(F_epsilon z)
          -D q_S^d(F_epsilon z)[F_epsilon Tz]}].       (4)

The derivative here acts on both rough colors of the quadratic;
beta_k is held fixed. In particular F_epsilon Tz is in that exact
order. For constants independent of N and epsilon,

    |B_(i,N)-B_(i,N)^epsilon|
      <=C_i[N^(5/2) sqrt(log(eN))+N^3 epsilon^(1/4)], (5)
    limsup_(N->infinity) a^3|B_(i,N)-B_(i,N)^epsilon|
      <=C_i epsilon^(1/4).                            (6)

This regularizes only the local quadratic factors of B, with a
mesh-uniform removable error. The prefix test b and signed tilt are
not regularized. No fixed-epsilon limit of (4), approximation of H
or Q_tr, or limit of the complete joint group is proved. Independent
f_(i,2),r_0, full compensation, finer asymptotics, finite matching,
interacting reflected error <=c_box/2, continuum axioms and infrared
finite positive mass remain open. This is a local specialization of
spectral and Gaussian estimates, not a claim of progress beyond the
sources checked.

## Proof

### 1. The exact discarded quadratic pieces are subcubic after tilt

Import L200 section 4's complete word differentiation, with its
boundary-uniform quadratic norm estimates (6)–(7). There are a fixed
finite number of stencil types and O(N^4) placements. In q_R^d every
term has a same-component rough first difference and coefficients
bounded by C p(k)/a. G_1's two differences can be expanded as a fixed
sum of shifted first differences. In q_R^0 the exterior linear
circulation has been differentiated instead; its O(a p(k)) bound
leaves coefficients at most C p(k), even for the force/vector terms
with their 1/a factor. Both insertion subtractions are included.
Thus

    ||q_R^0||_2<=C p(k) N^2 sqrt(log(eN)).             (7)

For q_S^d the coefficient bound is C p(k), and a rough difference
remains. The rest of the interior action has coefficients O(a p(k)).
The entire action collar has O(N^3) placements with coefficients
O(p(k)); no exterior derivative estimate is assigned to that collar.
Consequently

    ||q_S^0||_2
      <=C p(k)[a N^2+N^(3/2)]sqrt(log(eN))
      <=C p(k)N^(3/2)sqrt(log(eN)).                   (8)

All quadratics have two different remaining colors. These estimates
are for their complete signed polynomials, using positive tensor
comparison only as in L200, never entrywise covariance domination.

On im P whiten z=S^(1/2)xi and put
E_N=2S^(1/2)AS^(1/2), so Tz=S^(1/2)E_N xi and ||E_N||<=CN.
For a quadratic in two different colors its L2 norm is the
Hilbert–Schmidt norm of its whitened coefficient matrix K. Acting
on both colors by E_N replaces K by E_N K+K E_N. Therefore

    ||Dq(z)[Tz]||_2<=2||E_N|| ||q(z)||_2.            (9)

This is L200(14)'s signed two-slot estimate. It is valid also for a
difference of two quadratic polynomials. No positivity of E_N is used.
By L194(9),(11), ||b_l^c||_2<=CN^2. L198(13) gives exactly

    B_(i,N)=2a^2 sum_(k,l,c)d_(i;kl)
                  E[b_l^c {q_R(z)-Dq_S(z)[Tz]}].     (10)

Equations (7)–(10), a^2 N^2=64 and (1) show that replacing q_R,q_S
in (10) by q_R^d,q_S^d costs at most
C_i N^(5/2)sqrt(log(eN)). In particular the action collar is removed
only after its tilt and external contraction have been counted.

### 2. Uniform spectral bounds for the coupled difference field

Set delta z=(I-F_epsilon)z and Q_epsilon=Cov(delta z). Since P and
Delta commute,

    0<=Q_epsilon<=g_epsilon(Delta),
    g_epsilon(lambda)=lambda^(-1)
                (1-sqrt(lambda/(lambda+epsilon)))^2
       <=min(lambda^(-1),epsilon^2 lambda^(-3)).       (11)

The last inequality follows by rationalizing 1-(1+x)^(-1/2),
which is at most min(1,x) for x>=0. L026(6)–(7)'s full product
spectrum has at most C r^3 modes on a shell max_j q_j=r,
lambda_q>=4r^2/N^2, and r>=1. The own-direction index zero
is included in this count. In particular

    Tr Sigma<=C N^4,
    Tr(S 1_(Delta<=t))<=C N^4 t, 0<t<=1.             (12)

For the second estimate only shells r<=N sqrt(t)/2 occur. If this
upper radius is below one the sum is empty; otherwise the shell
bound is C N^2 sum_(r<=N sqrt(t)/2)r<=C N^4 t.

To estimate Tr Q_epsilon let R=N sqrt(epsilon). If R>=1,
split the shell bound from (11) at R to obtain

    Tr Q_epsilon
      <=C[N^2 sum_(r<=R)r
              +epsilon^2 N^6 sum_(r>R)r^(-3)]
      <=C N^4 epsilon.                               (13)

If R<1 use only the second sum starting at r=1. It is at most
C epsilon^2 N^6<=C N^4 epsilon. Thus (13) holds also for
epsilon<N^-2, without deleting low physical modes by assumption.
Moreover lambda g_epsilon(lambda)<=epsilon/lambda, by considering
lambda<=epsilon and lambda>=epsilon separately in (11). Hence

    Tr(Delta Q_epsilon)<=epsilon Tr Sigma<=C N^4 epsilon,
    Q_epsilon<=Sigma.                                (14)

These are positive spectral bounds only for the coupled Gaussian
fields. They are not applied to the signed tilt.

### 3. A local rough-difference quadratic has uniform mass error

Let q be one two-color stencil type with a rough first difference
and coefficient bound B per placement. It can be written

    q(z)=(U z^d)^T K(V z^f), d!=f,
    ||K||<=CB, U^T U<=CI, V^T V<=C Delta.             (15)

Here U selects an undifferentiated link at each placement, V selects
one allowed same-component first difference, and K contains the
variable local coefficients. Bounded stencil radius and placement
multiplicity give the first bound on U. The componentwise relative
Dirichlet/Neumann energy is a sum of squares of these internal
differences plus nonnegative boundary terms, giving the bound on V.
Repeated shifted terms are split into finitely many types. Both
color orders and restrictions to any subset of interior placements
are allowed. No coefficient is moved through a covariance.

It follows from (15) that

    ||V S V^T||<=C,
    ||V Q_epsilon V^T||<=C,
    Tr(V Q_epsilon V^T)<=C N^4 epsilon.               (16)

For example ||V Sigma V^T||=||V Delta^(-1/2)||^2<=C,
and the trace assertion uses cyclicity and (14).
Different colors remain independent under all spectral filters.
For two independent centered vectors x,y the exact bilinear second
moment is Tr(K Cov(y) K^T Cov(x)); bounding one positive covariance
in operator norm bounds this by ||K||^2 times that norm times the
other covariance's trace. This is the Isserlis identity in the
two-color case, with no internal or same-color pairing.

Use the exact coupled decomposition

    q(z)-q(F_epsilon z)
      =(U delta z^d)^T K(V z^f)
        +(U F_epsilon z^d)^T K(V delta z^f).          (17)

By (13),(16) the first summand has norm at most
C B N^2 sqrt(epsilon). For the second split F_epsilon z^d at
the spectral threshold t=sqrt(epsilon), retaining both pieces.
The low piece has covariance trace after U at most C N^4 t by
(12), because F_epsilon is a contraction commuting with S.
Pairing against the second operator bound in (16) gives norm
C B N^2 sqrt(t). The high piece has covariance operator norm
after U at most C/t. Pairing against the trace bound in (16)
gives norm C B N^2 sqrt(epsilon/t). The triangle inequality
therefore proves

    ||q(z)-q(F_epsilon z)||_2
        <=C B N^2 epsilon^(1/4), 0<epsilon<=1.        (18)

The same bound holds for a fixed finite sum of types. The auxiliary
spectral split is an estimate, not a truncation in the definition of
q or F_epsilon. Every relative mode and every original source row
remains. This specializes finite Gaussian second moments and
spectral shell counts to the actual local quadratic tensors; a
general flow-renormalization result would not give (18).

### 4. Apply the original signed tilt after controlling the difference

Apply (18) to the finite stencil types in (2), with respective
coefficient bounds C p(k)/a and C p(k). This gives

    ||q_R^d(z)-q_R^d(F_epsilon z)||_2
                          <=C p(k) N^3 epsilon^(1/4),
    ||q_S^d(z)-q_S^d(F_epsilon z)||_2
                          <=C p(k) N^2 epsilon^(1/4). (19)

Consider q_epsilon(z)=q_S^d(F_epsilon z) as a polynomial on the
original Gaussian space. Its directional derivative is exactly

    D q_epsilon(z)[Tz]
             =D q_S^d(F_epsilon z)[F_epsilon Tz].     (20)

Thus (9) applied to q_S^d-q_epsilon bounds the difference of the
two tilted expressions by C p(k) N^3 epsilon^(1/4). This does not
replace F_epsilon T by T F_epsilon. In whitened coordinates it
compares the coefficient matrices first and applies E_N to that
difference on both slots afterwards. It asserts neither smallness
of a commutator with A nor smoothness of Tz.

Finally multiply (19),(20)'s bounds by ||b_l^c||_2<=CN^2, by 2a^2,
and sum (1) over both probes' full heat coefficients and all three
colors. The total mass error is C_i N^3 epsilon^(1/4). Adding the
separate error of section 1 proves (5). Since a^3=512/N^3, the
first term in (5) tends to zero after scaling, proving (6).

### 5. Verification and the remaining limiting problem

All checks here are analytic: the exact product-rule split retains
both force/vector products and insertion subtractions; the full collar
is counted before removal; the shell bounds include epsilon<N^-2;
the independent-color bilinear identity is applied with the stated
positive covariances; and (20) fixes the noncommuting order. No
numerical fixture or mathematical script is used as evidence.

The test succeeds for one factor of the bulk trace. Even at fixed
epsilon, (4) retains the two moving prefixes through b and the
unregularized signed tilt T. Its convergence is still unproved.
H and Q_tr remain cubic-sized with their original signs in L198's
B+H-Q_tr+E, where a^3 E tends to zero. This result does not permit
discarding either term, choosing an N-dependent epsilon inside an
unproved fixed-epsilon limit, or treating boundedness as convergence.
L197's covariance-commutator obstruction is unaffected.

## Mathlib

Full matching approximation and joint-group scaled limit: **not
checked**. Supporting spectral-calculus, Gaussian and matrix norm
coverage: **not checked**; unknown coverage is not absence. The named
Isserlis Gaussian pairing theorem, Cauchy–Schwarz and finite spectral
calculus are used in their explicit elementary forms above. Exact
relative eigenvalues are imported from L026(6)–(7), local words from
L149/L155 via L200 section 4, and the original signed contraction
from L198(13). The new specialization is the mesh-uniform coupled
mass error with the original tilt retained, not a reproof of a
general renormalization theorem. The unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers the same selected bare joint group.

