# L212 — Retract the complete quartic probe before its residual contraction

## Hypotheses

Use L011's fixed-mesh bare expansion for SU(2) in the relative box
(-4,4)^4, admitted even meshes a=8/N, the straight lower-rooted
direction-1 forest, the complete L008 displacement and both actual
L010 probes i=3,6 at tau=1/16. Expand in the bare coupling before
refining the mesh. Coordinates, transposes and inner products are
ordinary dimensionless full-link coordinates, including forest links
and every variable normal end edge. Boundary links remain fixed.

Use L182's notation

    D=D_0, L=D_1^T D_1, Sigma=(L+DD^T)^(-1),
    P=I-D(D^TD)^(-1)D^T, S=P Sigma P, R=I-D Phi.

The lower prefix Phi is set to zero at every boundary vertex; its
upper pinned jump is retained. Let z have three independent colors
with covariance S. Its image x=pi_F Rz has the original forest
covariance Sigma_F by L182(8). The bracket is [v,w]=-v cross w in
the basis t_c=i sigma_c/2. Write q phi for the endpoint sum.

Let F_i(U)=mathfrak j_i(W_tau(U)) be the complete uncentered flowed
numerator of L011(1), and let F_(i,m) denote its homogeneous degree-m
Taylor polynomial on arbitrary full initial link coordinates. Thus

    F_(i,2)(z)=sum_c (z^c)^T B_i z^c,
    f_(i,2)(x)=F_(i,4)(I_F x), B_i D=0.

F_(i,4) is the entire four-term expression L011(12), using the full
exponential-coordinate Wilson-flow field and both nested integrals
in L011(11). F_(i,3) is the entire cubic probe, not its observable
or flow summand separately. Use the actual A=PAP=A^T of L018(2),
with both residual insertion subtractions. Put

    r(z)=sum_c (z^c)^T A z^c, t(z)=2SAz, M=2SAS.        (1)

All link maps act identically on colors. Directional derivatives d
below are ordinary derivatives of the displayed full polynomials.

## Conclusion

Set phi=Phi z, y=Rz and

    b(z)=[z,q phi]/2-[D phi,q phi]/4.                  (2)

For each oriented positive variable edge e:v->w, define p=-phi_v,
u=y_e, q=phi_w, and the cubic field

    c_e(z)=([p,[p,u]]+[u,[u,p]])/12+[[p,u],q]/4
          +[p+u,[p+u,q]]/12+[q,[q,p+u]]/12.          (3)

Here the local variable q in (3) is a vertex value, distinct from
the endpoint-sum map in (2). Every vertex value in (2)–(3) uses
the actual pinned Phi, including vertices on faces and corners.
The following is an exact polynomial identity on full-link fields:

    F_(i,4)(Rz)=P_i(z),
    P_i(z)=F_(i,4)(z)+dF_(i,3)(z)[b(z)]
                         +<b(z),B_i b(z)>+2<B_i z,c(z)>. (4)

Inner products include all three colors. Consequently the target
response K_(i,a)=kappa_0(f_(i,2),r_0) has the finite signed reduction

    K_(i,a)=(1/2)E_S[dP_i(z)[t(z)]].                  (5)

For clarity the derivative in (5) is the complete sum

    dF_(i,4)(z)[t]+d²F_(i,3)(z)[t,b]
      +dF_(i,3)(z)[db(z)[t]]+2<B_i b,db(z)[t]>
      +2<B_i t,c>+2<B_i z,dc(z)[t]>.                (6)

In particular, with psi=Phi t,

    db(z)[t]=([t,q phi]+[z,q psi])/2
                 -([D psi,q phi]+[D phi,q psi])/4.   (7)

The derivative dc(z)[t] in (6) differentiates all three arguments
of (3): replace each occurrence of p,u,q in turn by
-psi_v,(Rt)_e,psi_w, respectively, and sum using the bracket product
rule. Thus neither prefix is held fixed during the response derivative.

An equivalent single Wick contraction is as follows. Let T_i be the
unique symmetric four-linear tensor with P_i(z)=T_i(z,z,z,z) on the
full combined link/color space. For hat S=I_3 tensor S and
hat M=I_3 tensor M, all indices unrestricted,

    K_(i,a)=6 sum_(alpha,beta,gamma,delta)
             (T_i)_(alpha beta gamma delta)
                        hat M_(alpha beta) hat S_(gamma delta). (8)

The factor 6 uses M=2SAS; it would be 12 with SAS. The factor 1/2
in (5) is essential: L181's one-side contraction rule for two pure
cubics is not the quadratic-tilt rule for one quartic polynomial.

This removes forest gradients only from the initial arguments of
the retained complete flow jets. Their nested integrals still reach
zero, the correction involving dF_(i,3)[b] still has flow, and every
boundary row, constant mode and external heat mode remains. Equations
(4)–(8) supply no O(N^3) bound, scaled limit, sign or compensation
coefficient. Convergence, finer asymptotics, finite matching, the
interacting reflected error <=c_box/2, continuum axioms and infrared
finite mass remain unresolved. This is local reproduction of finite
gauge Taylor composition and Gaussian integration by parts; no
progress beyond the sources checked or originality is asserted.

## Proof

### 1. Keep the original law and the entire numerator

L010 gives pinned gauge invariance of F_i, since its full Wilson
flow is equivariant and both final numerators are invariant. Its
constant and linear jets vanish by L011. At fixed mesh these are
smooth finite-dimensional functions near identity, so their finite
Taylor composition is legitimate. No flow-time limit is exchanged
with mesh refinement.

L182(8) identifies I_F x=Rz with the actual forest Gaussian.
Moreover AR=A and R^T A=A because AD=0 and A is symmetric. Hence
r_0(x)=r(z) exactly. It follows, without transferring a higher jet
by free gauge invariance, that

    K_(i,a)=Cov_S(F_(i,4)(Rz),r(z)).                  (9)

The higher polynomial is still evaluated at Rz at this stage.

### 2. Compute the full endpoint gauge jets

Fix z and its pinned phi=Phi z during this Taylor expansion in h.
On each edge apply the actual gauge transformation to exp(h y_e):

    exp(-h phi_v) exp(h y_e) exp(h phi_w), y=Rz.      (10)

The linear logarithm of (10) is y_e+(D phi)_e=z_e.
The logarithm through cubic degree is

    h(p+u+q)+h²([p,u]+[p,q]+[u,q])/2+h³ c_e+O(h^4), (11)

with c_e exactly (3). To verify (11), first take the logarithm of
exp(hp)exp(hu), whose second and third terms are [p,u]/2 and
([p,[p,u]]+[u,[u,p]])/12. Composing this logarithm with exp(hq)
adds [[p,u],q]/4 at cubic degree, together with
([p+u,[p+u,q]]+[q,[q,p+u]])/12. This is the degree-three BCH
polynomial, obtained equivalently by multiplying the three finite
exponential series and using log(I+X)=X-X²/2+X³/3 through that
degree. This short specialization is needed to retain the actual
endpoint signs and upper pinned value; no general flow theorem is
being reproved.

To identify its second coefficient, use

    [D phi,q phi]=[phi_w-phi_v,phi_v+phi_w]
                       =-2[phi_v,phi_w].

Then ([p,u]+[p,q]+[u,q])/2=[y,q phi]/2-[phi_v,phi_w]/2
equals b(z) in (2), since y=z-D phi. This agrees with the quadratic
field in L183, but its cubic continuation (3) has not been dropped.
Boundary vertices have phi=0, so (10) preserves every fixed link.
On a variable normal end edge it uses the actual zero endpoint and
retains the other endpoint; no bulk continuation through a face occurs.

Gauge invariance equates F_i(exp(hRz)) with F_i evaluated at (10).
Its logarithm is hz+h²b+h³c+O(h^4). Since F_i has no linear jet,
the omitted fourth logarithm coefficient cannot enter degree four.
Composition at degree four yields F_(i,4)(z), dF_(i,3)(z)[b],
F_(i,2)(b), and 2<B_i z,c>, each once. This proves (4) on every
full-link input. It uses all four original L011(12) terms jointly,
including both observable corrections and both quadratic-flow
vertices. There is no gauge invariance assertion about their
individual terms and no isolated forest-invariance assertion.

### 3. Contract the quadratic residual with the correct tilt factor

On the co-closed color space the Gaussian is nondegenerate and has
covariance hat S restricted there; its inverse is the restriction
of I_3 tensor L. For any ambient polynomial P, two Gaussian
integration-by-parts operations give

    Cov_S(P,r)=sum_(alpha,beta)
           (hat S hat A hat S)_(alpha beta) E_S[partial_alpha partial_beta P]
              =(1/2)E_S[dP[2 hat S hat A z]],        (12)

where hat A=I_3 tensor A. For the second equality, one integration
by parts in E[z_gamma partial_alpha P] gives
sum_delta hat S_(gamma delta) E[partial_delta partial_alpha P].
For the first equality apply the same operation to each of the two
Gaussian factors of r: the term differentiating the other factor
is E[P]E[r] and cancels the covariance subtraction. Thus the formula
does not assume E[r]=0 or E[P]=0. It also applies to the singular
ambient covariance by writing z as a linear image of independent
nondegenerate Gaussian coordinates. Polynomial Gaussian moments
justify all integrations; no quartic exponential integrability is used.

Apply (12) with P=P_i and use (9) and (4). This proves (5).
Differentiate (4) by the ordinary product rule, using symmetry of
B_i and of d²F_(i,3), to obtain (6). Phi and R are linear maps,
so dphi[t]=Phi t and dy[t]=Rt, proving (7) and the stated rule
for dc[t]. The two insertion subtractions remain inside A in t.

Finally, for P=T(z,z,z,z) its expected Hessian is
12 sum_(gamma,delta) T_(alpha beta gamma delta)
hat S_(gamma delta). Insert this in (12) and use
hat S hat A hat S=hat M/2. The coefficient is 12/2=6, proving
(8) with every color and connected subtraction retained.

### 4. Exact checks and what remains

Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/complete_quartic_retraction.py`.
The full rational certificate is
`scripts/combined-ward-response/complete-quartic-retraction-certificate.json`.
Eight independent SU(2) four-link loop fixtures compute logarithms
by direct matrix-algebra series through degree three and compare
degree-four gauge-invariant loop coefficients with (4). Every fixture
passes; across them all three correction types are nonzero, so an
omitted term would be detected. The fixture vectors are arbitrary,
not co-closed or the actual probes, and test finite algebra only.
Separate direct Gaussian moment computations in correlated and
singular two-coordinate examples verify (12) with nonzero covariance
and reject omission of its factor 1/2. These checks support the
analytic identities; they do not verify a cutoff estimate or a limit.

The remaining task is to control (8), or equivalently the full signed
sum (6), in the actual forest setting. The retained cubic derivative
still reaches zero flow time, and b,c contain correlated pinned
prefixes. Cubic boundedness would give bounded a^3 K_(i,a) only;
existence and evaluation of its limit are additional requirements.
The earlier failed termwise transfer in L022 and ATTEMPTS/010 is
avoided, rather than treated as evidence about this signed response.

## Mathlib

Full matching theorem: **not checked**. Supporting coverage of
finite BCH jets, multivariable Taylor composition, Gaussian
integration by parts and Isserlis' formula: **not checked**. No
presence or absence claim is made. The reused
[coverage assessment](../drafts/literature/2026-10-16-complete-quartic-probe-jet-scale.md)
records the inspected primary flow/Ward theorems and their different
scope. None is imported as a bound for this selected bare cumulant;
only its approved finite joint-retraction specialization is used here.
