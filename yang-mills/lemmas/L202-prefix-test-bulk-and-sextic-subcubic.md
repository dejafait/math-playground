# L202 — A sharper prefix test removes the bulk and sextic at cubic scale

## Hypotheses

Use L194, L198, L200 and L201's exact SU(2) setting: relative box
(-4,4)^4, sufficiently fine admitted even N, a=8/N, straight
direction-1 lower-rooted forest, full compact L008 displacement and
both actual L010 probes i=3,6 at tau=1/16. Take the bare expansion
at fixed mesh before refinement. Use ordinary stored full-link
coordinates and Euclidean adjoints. Retain all physical faces, normal
end edges, constant own-direction modes and full external heat sums.
Vertex potentials are pinned on every physical boundary vertex.

Put Delta=C^T C+DD^T, with C the link-to-plaquette circulation.
Keep the three independent Gaussian colors z of covariance
S=P Delta^(-1)=PSP,
the signed residual A=PAP with both insertion subtractions, and

    T=2SA, V=q Phi, H=I-D Phi/2,
    b=[Hz,Vz]/2=[z,Vz]/2-[D Phi z,Vz]/4,
    rho_H=script R_3-d script S_3[Tz],
    J_i=2<B_i z,b>.

Here H is a link map, distinct from L198's upper-exterior scalar
trace H_(i,N). Phi is the original pinned lower prefix. Use L194's
ordinary normalized product modes e_l and complete expansion

    SB_i=a^2 sum_(k,l)d_(i;kl)n_k e_l^T, n_k=S e_k,
    ||e_l||_infinity<=C a^2,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p)               (1)

for every fixed polynomial p. Keep the definitions of B_(i,N),
H_(i,N), Q_(tr,i,N), E_(i,N) in L198, and B_(i,N)^epsilon in
L201(4), where F_epsilon=(Delta/(Delta+epsilon I))^(1/2),
including its original F_epsilon Tz order. No prefix,
exterior vector or signed tilt is regularized here.

## Conclusion

For every full product mode e_l and output color c,

    ||<e_l,b^c>||_2<=C N^(7/4).                       (2)

Consequently, for both actual probes,

    |B_(i,N)|<=C_i N^(11/4),
    sup_(0<epsilon<=1)|B_(i,N)^epsilon|
                                     <=C_i N^(11/4), (3)
    |E[J_i rho_H]|<=C_i N^(11/4)sqrt(log(eN)).         (4)

Thus B has zero a^3-scaled limit, as does every fixed-mass bulk
approximant, uniformly even if epsilon varies with N. This last
statement follows directly from (3), without interchanging mesh
and mass limits or asserting convergence at another scale. The
complete retained prefix sextic in (4) also has zero cubic limit.

For L181's original joint group G_(i,a), the already established
finite identities therefore give the two compatible reductions

    G_(i,a)=H_(i,N)-Q_(tr,i,N)+o(N^3)
           =-Q_(3,i,N)+o(N^3).                       (5)

Here Q_3 is L184's entire third quartic placement, with its original
positive placement convention before subtraction. In particular
Q_3=O(N^3), by L200's complete-group bound and (5). Neither Q_3
nor H-Q_tr has a proved scaled limit or coefficient. No full joint
limit, compensation, finer asymptotics, finite matching, interacting
reflected error <=c_box/2, continuum axioms or infrared finite
positive mass follows. This is a local consequence of existing
Gaussian and prefix estimates, not progress beyond the sources checked.

## Proof

### 1. Import the differentiated prefix bound with its upper row

Set K=Phi S Phi^T. L182(10) and L186(3),(10) give

    ||K||_HS<=C N^4,
    ||D K D^T||_HS<=C N^(7/2),
    ||S||_HS<=C N^2 sqrt(log(eN)).                    (6)

The differentiated estimate is for the full pinned incidence D.
In L186's proof it follows from K<=U tensor G, U_st=min(s,t),
with D^T D=L_D tensor I+I tensor Delta_T and
UL_D=I+(Uj)j^T. Its last upper-end contribution is retained in
Tr(UL_DUL_D)=n^2+3n, n=N-1. Its three unrestricted trace terms
are O(N^6), O(N^6), O(N^7), respectively. Thus (6) does not
use an upper-free incidence, a compact output restriction or a
deleted boundary covariance row.

The elementary positive-matrix inequality applied to
H S^(1/2)=S^(1/2)-D Phi S^(1/2)/2 gives

    0<=H S H^T<=2S+(1/2)D K D^T.

For positive X<=Y, Tr X^2<=Tr Y^2, since
Tr(Y^2-X^2)=Tr((Y-X)(Y+X))>=0. The last inequality follows
from nonnegativity of the trace of a product of two positive
matrices; it does not assert that their product is positive.
Taking Hilbert--Schmidt norms, using (6) and the uniformly bounded
endpoint map q, proves

    ||H S H^T||_HS<=C N^(7/2),
    ||V S V^T||_HS=||qKq^T||_HS<=C N^4.              (7)

The lower-order S norm in (6) is absorbed into N^(7/2) for N>=2.
These are positive covariance estimates only. Neither A nor its
tilted covariance is assigned positivity.

### 2. A two-color bilinear norm retains the improved H covariance

For deterministic maps X,Y, a diagonal multiplier D_y=diag(y),
and two different colors d,f, independence of z^d and z^f gives
the exact finite Gaussian second moment

    ||(Xz^d)^T D_y(Yz^f)||_2^2
       =Tr(D_y Y S Y^T D_y X S X^T)
       <=||y||_infinity^2
                       ||Y S Y^T||_HS ||X S X^T||_HS. (8)

The equality is the two-color case of Isserlis' pairing theorem.
For the inequality apply Hilbert--Schmidt Cauchy--Schwarz and
||D_y C D_y||_HS<=||y||_infinity^2||C||_HS.
This proof also applies to singular S, either directly by its
covariances or through a finite Gaussian linear image.

For fixed c, [Hz,Vz]^c consists of the two signed orders using the
other two colors d,f. Apply (8) to each order with X=H,Y=V and
use the triangle inequality. The two colors are independent;
H z^d and V z^d within one color are not assumed independent.
Their dependence across the two orders is harmless for this norm
upper bound. Equations (7),(8) give

    ||<y,b^c>||_2
       <=C||y||_infinity N^(15/4).                   (9)

Putting y=e_l and a^2=64/N^2 proves (2). In particular the
N^4 common covariance bound used in L194(9) is unnecessary for
the H slot: L186's earlier N^(7/2) bound saves one quarter power
in this quadratic norm. No cancellation, covariance commutator,
prefix localization or additional regularity is involved.

### 3. Apply the sharper test in the original bulk order

Write beta_k=(I-Pi_n)(I-D Phi)n_k and set

    q_R=d script R_3(z)[beta_k^(c)],
    q_S=d script S_3(z)[beta_k^(c)].

L200(2) proves, with beta_k held fixed,

    ||q_R||_2+||Dq_S(z)[Tz]||_2<=C p(k)N^3.           (10)

This imports its complete rough-circulation count, separate action
collar bound and signed two-slot tilt estimate. Both force/vector
terms and both insertion subtractions are included. In particular
(10) is not inferred by declaring Tz smooth.

Use L198(13) in its exact original order,

    B_(i,N)=2a^2 sum_(k,l,c)d_(i;kl)
                    E[<e_l,b^c>{q_R-Dq_S(z)[Tz]}].   (11)

Cauchy--Schwarz, (2),(10), and the full summable coefficients
in (1) bound (11) by

    C_i a^2 N^(7/4) N^3=C_i' N^(11/4).

This proves the first part of (3). Multiplication by a^3 gives
O(N^(-1/4)), tending to zero, with no unproved trace limit.

### 4. The same bound is uniform for L201's mass approximant

Retain q_R^d,q_S^d exactly as in L201(2), including their coefficients
and signs. Its local types (15) have the form

    q(z)=(Uz^d)^T K_0(V_0z^f), d!=f,
    ||K_0||<=CB_0, U^T U<=CI, V_0^T V_0<=C Delta.

Here K_0 is a coefficient matrix, distinct from the prefix covariance
K in (6). Since S<=Delta^(-1),
||V_0 S V_0^T||<=C and Tr(U S U^T)<=C Tr S<=C N^4.
The same independent-color second-moment identity as (8), now
bounding the first positive covariance in operator norm, gives
||q||_2<=C B_0 N^2. The finite sum of these types has
B_0<=C p(k)/a for q_R^d and B_0<=C p(k) for q_S^d. Hence

    ||q_R^d||_2<=C p(k)N^3,
    ||q_S^d||_2<=C p(k)N^2.                          (12)

On im P, whiten z=S^(1/2)xi. Because F_epsilon commutes with
S and P and is a self-adjoint contraction, replacing a quadratic
q(z) by q(F_epsilon z) multiplies its whitened two-color coefficient
matrix on both sides by contractions. Its Hilbert--Schmidt norm,
and thus its L2 norm, cannot increase. For

    E_N=2S^(1/2) A S^(1/2), ||E_N||<=C N,

L201(9)'s two-slot estimate then bounds the directional derivative
of q_S^d(F_epsilon z), as a polynomial of the original z, by
C p(k)N^3. That derivative is precisely

    Dq_S^d(F_epsilon z)[F_epsilon Tz],

not a reordered expression. Applying (2),(12) in L201(4) proves
the second part of (3), uniformly for 0<epsilon<=1. This argument
does not replace b, T, or either prefix and does not need a mass
approximation for any of them.

### 5. The complete prefix sextic and the remaining quartic

L194(12), after contracting only the smooth external leg, gives

    E[J_i rho_H]=2a^2 sum_(k,l,c)d_(i;kl)
                            E[<e_l,b^c>d rho_H[n_k^(c)]],
    d rho_H[n_k^(c)]
       =d script R_3[n_k^(c)]
         -d^2 script S_3[n_k^(c),Tz]
         -d script S_3[(Tn_k)^(c)].                  (13)

L194(8),(11),(13),(14) bound the L2 norm of the entire derivative
in (13) by C p(k)N^3 sqrt(log(eN)). The last term is retained;
its actual smooth tilt has the smaller O(p(k)sqrt(log(eN))) norm.
Combining that bound with (2),(1) proves (4). Its cubic-scaled
bound is C_i N^(-1/4)sqrt(log(eN)), tending to zero.

L198(4), its a^3 E_(i,N)->0 and the first part of (3) prove the
first equality in (5). Independently L193(3) reduces G to the
sextic minus E[dJ_i[W]] with an o(N^3) error, and L184(4)--(5)
identifies that expectation with Q_1+Q_2+Q_3. L185--L186 give
Q_1+Q_2=O(N^(5/2)). Equation (4) therefore proves the second
equality in (5), with its subtraction sign. L200's G=O(N^3)
then gives Q_3=O(N^3). This is a bound, not a limit for Q_3.

All checks are analytic: the two-color second moment is exact,
the singular-value ideal inequality retains every covariance row,
the N exponents are 15/4-2=7/4 and 7/4+3-2=11/4, and
the Gaussian derivative in (13) retains all three action slots.
No mathematical script or numerical fixture is used as evidence.
The existing factorwise failures remain: neither a covariance
commutator gain nor a smooth rough tilt was assumed. The result
does not establish separate H or Q_tr limits, discard either
at cubic scale, or resolve the independent f_(i,2),r_0 contribution.

## Mathlib

Full matching modal prefix estimate, actual-probe subcubic bulk/sextic
bounds and joint-group limit: **not checked**. Supporting Isserlis,
Hilbert--Schmidt inequalities, positive matrix order and spectral
calculus coverage: **not checked**; unknown coverage is not absence.
The named standard input is Isserlis' Gaussian pairing theorem in
its explicit two-independent-color form (8). The full prefix bounds
are imported from L182 and L186, and the exact contractions and
ordered quadratic bounds from L194, L198, L200 and L201. The only
specialization needed is to use the sharper existing H covariance
in the modal b test and then the original signed pairings. A general
flow-renormalization theorem would not by itself give these bare
selected-group conclusions. The unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers this same target; no source refresh or originality claim is made.
