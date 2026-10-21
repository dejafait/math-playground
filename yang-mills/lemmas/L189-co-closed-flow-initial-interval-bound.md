# L189 — An integrable initial-time bound for the co-closed cubic probe

## Hypotheses

Use L181–L182's SU(2) fixed-mesh expansion, relative box (-4,4)^4,
admitted even N, a=8/N, tau=1/16, complete displacement and both
actual L010 probes i=3,6. Take the small-coupling expansion before
refinement. All coordinates and adjoints below are ordinary
dimensionless full-link coordinates. Boundary links are fixed at
identity; their Taylor coordinates are zero. All variable normal end
edges, physical faces and allowed constant edge modes are retained.

Write D=D_0, C=D_1, L=C^T C, Delta=L+DD^T,
P=1-D(D^T D)^(-1)D^T, S=P Delta^(-1)P and H_s=exp(-s Delta/a^2).
Let z have three independent colors of covariance S. The full action
cubic is script S_3, before forest restriction. The actual quadratic
numerator matrix Q_i is L181's Q_i, with Q_i D=0. Define

    y_s=H_s z,   h_(i,s)=H_(tau-s) Q_i H_tau z,
    U_(i,a)(s,z)=-(2/a^2) d script S_3(y_s)[h_(i,s)].       (1)

By L181(10) and L182, U is exactly the Duhamel integrand of the
co-closed part F_(i,3)(z) of the complete cubic probe. It is not the
integrand on the forest input Rz. No estimate on the effective forest
residual rho(pi_F Rz) is a hypothesis of the unconditional result.

## Conclusion

Put ell(r)=1+log(1+1/r), for r>0. There is a constant C_i independent
of sufficiently fine meshes and of 0<=s<=tau/2 such that

    ||U_(i,a)(s)||_2
      <= C_i [ell(s+a^2)^(1/2)
               +(s+a^2)^(-1/2) ell(s+a^2)^(1/4)].          (2)

The norm is for the actual correlated co-closed Gaussian. In
particular, for 0<delta<=tau/2, the complete initial-time polynomial

    I_(i,a,delta)(z)=integral_0^delta U_(i,a)(s,z) ds

obeys the mesh-uniform estimate

    ||I_(i,a,delta)||_2 <= C_i eta(delta),
    eta(delta)=delta ell(delta)^(1/2)
                    +sqrt(delta) ell(delta)^(1/4) -> 0.   (3)

This retains the entire action cubic and all three differentiated
slots. It uses the circulation in that cubic before taking norms.
No cancellation between different flow times is needed.

For any family of square-integrable polynomials V_a on this same
Gaussian space the precise response consequence is only

    a^3 |E[I_(i,a,delta) V_a]|
         <= C_i eta(delta) a^3 ||V_a||_2.                 (4)

Thus a bound sup_a a^3||rho(pi_F Rz)||_2<infinity would suffice to
remove this co-closed initial interval uniformly at cubic scale.
That residual bound is NOT proved here. In particular (3) alone does
not remove the interval in the actual joint response. L183's signed
residual retraction and the prefix sextic/quartic terms remain, as do
the final observable cubic, the remaining flow interval and their
response limits. There is no coefficient, full cubic response bound,
scaled limit, compensation, finer remainder, interacting reflected
estimate, continuum theory or mass-gap conclusion.

## Proof

### 1. Keep the full action circulation

For a plaquette p let J_p select its four signed full-link coordinates
in traversal order, with only physically fixed links replaced by zero.
Do not impose forest zeros. L048 proof section 1's ordered logarithm
calculation applies to these full coordinates verbatim: if v=J_p y,

    w_1(v)=sum_r v_r=(Cy)_p,
    w_2(v)=(1/2) sum_(r<t) [v_r,v_t],
    script S_3(y)=sum_p <(Cy)_p,w_2(J_p y)>.              (5)

The bracket is minus the color cross product. The action normalization
is 4P_p, so (5) has no further a-dependent coefficient. The formula
holds also for boundary plaquettes with zero selected rows. The full
action is the sum of these words; no bulk approximation is made.

Differentiating (5) gives exactly

    d script S_3(y)[h]
      =sum_p <(Ch)_p,w_2(J_p y)>
       +(1/2) sum_p sum_(r<t) <(Cy)_p,
             [(J_p h)_r,(J_p y)_t]
              +[(J_p y)_r,(J_p h)_t]>.                  (6)

In the first type the smoothed external leg carries C. In each of
the other two types one of the short-time legs carries C. This is a
statement about the whole actual cubic tensor, rather than a
curvature-only replacement of the nonlinear probe or residual.

Every term in (6) is a scalar triple product of three color-diagonal
linear images of z. Its internal Gaussian contractions vanish because
two colors then coincide in an alternating color tensor. Each term,
and their sum, is pure third Gaussian chaos even when its three
arguments are correlated.

### 2. Full-spectrum covariance estimates

Delta commutes with P; on im P its restriction is L. The covariance
of one color of y_s is

    C_s=H_s S H_s=P Delta^(-1) exp(-2s Delta/a^2).

L026(6)–(7) gives the complete relative one-form spectrum: each
component has one cosine index in 0,...,N-1 and three sine indices
in 1,...,N-1. Its dimensionless eigenvalue lambda_k satisfies
lambda_k>=4|k|^2/N^2. The number of modes with max k_j=m is at most
C m^3, counting all components. In particular no zero full one-form
mode is present; the constant own-direction cosine modes ARE present.
Consequently

    ||C_s||_HS^2
      <= Tr[Delta^(-2) exp(-4s Delta/a^2)]
      <= C a^(-4) sum_(m=1)^(N-1) exp(-c s m^2)/m
      <= C a^(-4) ell(s+a^2).                            (7)

Here and below constants can absorb the fixed box length. To check
the last bound uniformly at s=0 as well, the sum is at most C log(eN)
by deleting its exponential; for s>0 splitting at s^(-1/2) and
comparing the remaining decreasing Gaussian tail with its integral
gives C[1+log(1+s^(-1/2))]. The smaller of these two bounds is at most
C ell(s+a^2): max(s,a^2)<=s+a^2<=2 max(s,a^2), and N=8/a.
This proves (7) also in the transition region s comparable to a^2.

The covariance of Cy_s is K_s=C C_s C^T. Its squared Hilbert–Schmidt
norm can be evaluated without introducing a different boundary law:

    ||K_s||_HS^2=Tr(C_s L C_s L)
                =Tr[P exp(-4s Delta/a^2)]
                <= C sum_(m=1)^(N-1) m^3 exp(-c s m^2)
                <= C (s+a^2)^(-2).                       (8)

The second equality uses C_s L=P exp(-2s Delta/a^2). For the final
bound the sum is at most C N^4 for all s, and at most C s^(-2) for
s>0 by a Gaussian integral comparison. Taking the smaller bound and
using N=8/a proves the assertion. All traces are finite full-box
traces. Neither (7) nor (8) removes any low-frequency or boundary row.

### 3. The external leg and its circulation

Let e_k be the complete ordinary orthonormal component product modes
of Delta. Set

    v_(i,k,s)=H_(tau-s) Q_i H_tau Delta^(-1/2) e_k.

Since Q_i annihilates gradients and H commutes with P,

    Cov(h_(i,s))=sum_k v_(i,k,s) v_(i,k,s)^T.              (9)

This equality uses the Hodge inverse only on the smoothed external
leg; it does not change the covariance C_s of either short-time leg.
L182 proof section 2, (12), establishes the needed pre-heat estimate
from the actual two numerator stencils. In its normalization
e_k=a^2 f_(k,a), Delta^(-1/2)e_k=a lambda_(k,phys)^(-1/2)f_(k,a),
and Q_i=a^2 Q_(i,a). Thus, before H_(tau-s),

    ||Q_i H_tau Delta^(-1/2)e_k||_infinity
       <= C_i a^3 p(k) exp(-tau lambda_(k,phys)),          (10)

where p is a fixed polynomial and lambda_(k,phys)>=c|k|^2.
The bound retains the triplet average, the shear clover products,
their coefficient transitions and their compactly supported adjoint
stencils. Its applicability is exactly the same as in L182; no
rough column is assigned this estimate.

The componentwise relative Hodge heat is a supremum contraction, as
proved in L182. We also need, only for r>=tau/2,

    ||C H_r f||_infinity <= C_tau a ||f||_infinity.        (11)

Here is a direct full-box proof including the end rows. L026's
normalized modes give ||e_k||_infinity<=C a^2,
||e_k||_1<=C a^(-2), and ||C e_k||_infinity<=C a^3(1+|k|).
For the last inequality each unscaled incidence difference of a sine
or cosine product contributes at most C a |k|; at normal end rows the
same sine/cosine identities hold with the pinned tangential value
zero. There is no zero extension across a normal free edge. Expanding
H_r in all modes and using |<e_k,f>|<=||e_k||_1||f||_infinity gives

    ||C H_r f||_infinity
       <= C a ||f||_infinity
            sum_k (1+|k|) exp(-r lambda_(k,phys)).

The full infinite-mode majorant is finite uniformly for r>=tau/2,
proving (11). The own-direction constant modes are included. Applying
the contraction and (11) to (10), then summing the squared complete
heat-weighted mode bounds, proves, uniformly for 0<=s<=tau/2,

    sum_k ||v_(i,k,s)||_infinity^2 <= C_i a^6,
    sum_k ||C v_(i,k,s)||_infinity^2 <= C_i a^8.           (12)

### 4. Correlated Gaussian norm estimate in the original action order

Use the named Isserlis Gaussian pairing theorem in the specialization
proved in L182(13). An ordered trilinear expression T with zero
internal contractions satisfies

    ||T(z,z,z)||_2^2 <= 6 E|T(z_1,z_2,z_3)|^2,           (13)

where the right side uses independent copies of the SAME Gaussian.
Indeed representing z as a linear image of standard Gaussian noise
gives 6||sym T||_HS^2<=6||T||_HS^2. This also proves (13) for singular
S. Independent copies are a norm bound, not a replacement of the
actual response or an assertion of independence of its slots.

For clarity, the matrix estimate after conditioning on the external
copy is as follows. For independent one-color vectors u,w of
covariances C_u,C_w and any rectangular matrix M,

    E|u^T M w|^2=Tr(C_u M C_w M^T)
       <= ||C_u||_HS ||C_w||_HS ||M||_op^2.              (14)

This follows from Hilbert–Schmidt Cauchy–Schwarz and
||M C_w M^T||_HS<=||M||_op^2||C_w||_HS. Color sums change only a
fixed constant. For each fixed external vector v, the local matrices
in (6) have operator norm at most C||v||_infinity, with v replaced
by Cv for its first type. Every plaquette has four rows, every edge
belongs to boundedly many plaquettes, and each bracket has bounded
color coefficients; the row and column absolute sums therefore have
this bound. This proves the operator assertion without a volume
factor. Physically fixed rows can only delete entries, and normal end
rows have the same bounded incidence counts.

Apply (13) separately to the finite types in (6), and expand the
independent external Gaussian by (9). For the first type, (14)
uses two copies of C_s and the second bound of (12). Its L2 norm is
at most

    C_i a^4 ||C_s||_HS <= C_i a^2 ell(s+a^2)^(1/2).      (15)

For the remaining types it uses K_s on the circulated short-time
copy and C_s on the other, with the first bound of (12). Their norms
are each at most

    C_i a^3 (||K_s||_HS ||C_s||_HS)^(1/2)
      <= C_i a^2 (s+a^2)^(-1/2) ell(s+a^2)^(1/4).        (16)

The original factor 2/a^2 in (1), the triangle inequality over these
types, and (15)–(16) prove (2). Neither the sign nor any one of the
three derivative placements was dropped in deriving (6); inequalities
are used only after the complete circulation structure is restored.

### 5. Initial interval and scope of pairing

For s>0 the right side of (2) is at most

    C_i [ell(s)^(1/2)+s^(-1/2)ell(s)^(1/4)].             (17)

This is mesh independent and integrable at zero. Explicitly, for
0<t<=1, ell(delta t)<=ell(delta)+log(1/t). For 0<q<=1,
(x+y)^q<=x^q+y^q. Substituting s=delta t in the two integrals in
(17), the constants integral_0^1 log(1/t)^(1/2) dt and
integral_0^1 t^(-1/2)log(1/t)^(1/4) dt are finite: t=exp(-v)
turns them into exponentially decaying integrals of powers of v.
This bounds the integrals respectively by C delta ell(delta)^(1/2)
and C sqrt(delta)ell(delta)^(1/4). At each fixed mesh U is a
continuous polynomial in s on the closed interval; Minkowski's
integral inequality now proves (3), with no mesh-limit interchange.

Finally ordinary Gaussian Cauchy–Schwarz proves (4). L181's original
effective residual remains mesh dependent. L183's exact identity
rho(pi_F Rz)=rho_H(z)-<Lz,W(z)> does not furnish the missing norm
bound, and its two moving prefixes and composed-prefix derivative
cannot be deleted. No consequence for its signed pairing is asserted
without a bound on that pairing or the stated norm hypothesis.
Likewise the forest-probe correction J_i is not estimated by (3).

Verification is analytic: (5)–(6) retain the exact action word and
normalization; (7)–(8) include every spectral shell down to the
constant own-direction modes; (9)–(12) use smoothness only on the
actual external mode; (13)–(16) keep the original local incidence
order; and (17) supplies an integrable majorant including cutoff-scale
times. No numerical mode cutoff, script certificate or unverified
limit approximation is used as proof.

## Mathlib

Full matching result and supporting relative-cochain heat, Gaussian
chaos, Hilbert–Schmidt and integral inequalities: **not checked**.
Unknown coverage is not evidence of absence. The named standard
input is Isserlis' Gaussian pairing theorem, with its precise singular
Gaussian norm specialization proved in L182 and recalled in (13).
The finite trace, mode-sum and integral inequalities needed here are
proved explicitly. The unchanged
[assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
explains why the primary full renormalized-flow results do not settle
this bare selected response. This is local progress using standard
Gaussian and heat estimates, not a claim of a new result beyond the
sources checked or a reproof of flow renormalizability.
