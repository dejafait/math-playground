# L128 — Five scalars determine the complete retained transverse-H coefficient

## Hypotheses

Import L124's complete other/other assembly and L126(1)--(3),
L125(1)--(3), L123(1)--(2), L118(4)--(9), L127(3)--(4) and
L120(2). The actual coefficient scope is SU(2), both actual L010 probes
i=3,6, the straight lower-rooted direction-1 forest, all-face relative
fixed-link box D=(-4,4)^4, admitted even N, a=8/N, tau=1/16, and the
bare small-coupling coefficient at fixed mesh before refinement. All
coefficient limits and complete axial/heat tails are imported. Retain the
actual displacement, real symmetric c_(i;kl), lower prefix including its
constant axial mode, and all physical exterior fields V_k. No new mesh
limit or replacement of a finite staggered tensor is made here.

Use transverse indices 2,3,4, plaquette order (23),(24),(34), and
normalized torus measure on [-pi,pi]^3. Put ell=x_1+4 and
h_(k,rho a)=partial_rho V_(k,a)-partial_a V_(k,rho), extended
antisymmetrically with zero diagonal. This equals L123's curl of A_k
because V_k=A_k-grad_T Phi_k. All physical derivatives below are
transverse; frequency derivatives are explicitly labeled.

## Conclusion

There are five universal real scalars h_D,h_X,h_A,tau,xi, with
7/1000<tau<1/100, such that the entire retained coefficient

    K_(i,tr)=K_(i,f)+K_(i,V)+K_(i,sc)+K_(i,en)

is exactly

    sum_(k,l)c_(i;kl) integral_D ell {
      h_D (div_T u) (V_l dot V_k)
      +h_X sum_(rho,m) (partial_m u_rho)
                      (V_(l,rho)V_(k,m)+V_(l,m)V_(k,rho))
      +h_A sum_rho (partial_rho u_rho)V_(l,rho)V_(k,rho)
      +tau sum_rho u_rho [V_(l,rho) div_T V_k
                         -sum_a V_(l,a)partial_a V_(k,rho)]
      +xi sum_(rho,a) u_rho V_(k,a) h_(l,rho a) } dx.       (1)

All torus constants, spatial integrals and full exterior heat sums
are absolutely convergent. Their explicit torus definitions are below;
there is no color, symmetry or outside factor 3 in (1). The five-scalar
parameterization is sufficient, without claiming minimality under further
physical integration by parts or identities specific to the probes.

This is a reduction of the actual four retained coefficients, not their
numerical evaluation. The other five L124 coefficients E,ax,-Q,G,R
remain. No value or sign of K_(i,oo)+4 gamma D_i, complete compensation,
finer powers/logarithm, interacting error <=c_box/2, continuum axioms,
reflection positivity, infrared control or finite positive mass follows.

## Proof

### 1. Explicit torus definitions with every physical component retained

Use centered symbols d_mu=2 sin(theta_mu/2), eta_mu=cos(theta_mu/2),
lambda=sum_mu d_mu^2, P=d d^T/lambda, Q=I-P. Let Z be the real
circulation matrix with row -d_nu e_mu^T+d_mu e_nu^T in plane mu nu,
so D_c=i Z, and set S=Z Z^T/lambda. Values at lambda=0 do not affect
any integral. For a physical vector v define

    f(v)_(mu nu)=2(d_nu eta_mu v_mu-d_mu eta_nu v_nu).

L127(4) imports the complete path identity
F(v)^* P F(w)=f(v) f(w)^T/lambda. No plane or b/q path is omitted.
For every ordered rho,nu with nu!=rho, pi is their increasing plane
and sigma_(rho,nu) is +1 for rho<nu and -1 otherwise. Define

    A_nu=Z eta_nu e_nu,
    W_(rho,nu)=sigma_(rho,nu) eta_rho eta_nu epsilon_pi^T S,
    U_rho=sum_(nu!=rho) sigma_(rho,nu) eta_rho eta_nu^2
                                              e_nu epsilon_pi^T,
    B_rho=Z U_rho S,
    J_(rho,m)=sum_(nu!=rho)
       [A_nu partial_(theta_m)W_(rho,nu)
                  -(partial_(theta_m)A_nu)W_(rho,nu)].

Thus i B_rho is the complete centered G_r summed at fixed rho;
i A_nu and W_(rho,nu) are L126's separate endpoint and clover-energy
factors. Define physical tensor entries, for a,b in {2,3,4}, by

    H_(rho,m;ab)=-1/4 integral lambda^-1
       [f(e_b)^T J_(rho,m) f(e_a)+f(e_a)^T J_(rho,m) f(e_b)],
    T_(rho,m;ab)=-1/2 integral lambda^-1
       [f(e_b)^T (partial_(theta_m)B_rho) f(e_a)
                     -f(e_a)^T (partial_(theta_m)B_rho) f(e_b)]. (2)

These are precisely L126's H and M^- after contracting the linked
phi(V) and summing all ordered generators at fixed rho. To check the
signs, L125's i derivative pairs with G_r=i A_nu W_(rho,nu),
so M=-integral f_b^T partial(A_nu W)f_a/lambda. L126's b is
-integral f_b^T A_nu partial W f_a/lambda. Symmetrizing b-M/2
gives H in (2); antisymmetrizing M gives T in (2).

This conversion retains the phase terms until integration. L125(9)'s
phase commutator and L126(6)'s endpoint/clover phase term have imaginary
odd traces under simultaneous frequency reversal against every real
even projected path product. Their integrals are zero, also for the
finite linear combinations f_a f_b^T/lambda in (2). No differentiation
of an individual nonperiodic centered entry by frequency integration
by parts is used. In particular the derivative acts on B or W,
not on the external f_a or f_b.

Set

    h_D=H_(2,2;33), h_X=H_(2,3;23),
    h_A=H_(2,2;22)-h_D-2h_X,
    tau=T_(2,3;23).                                      (3)

L127(1)--(3) identifies the last entry, including all planes and ordered
generators, with its certified tau and gives its stated strict bounds.
The other three constants in (3) are not evaluated here.

### 2. Signed-coordinate covariance of the differentiated tensors

Let R be any signed permutation of transverse coordinates and let R_2
be its induced orthogonal action on oriented two-forms. Transform theta
by R; d transforms by R and eta is permuted with its component, since
cos(theta_mu/2) is even. Directly from the displayed circulation rows,

    Z(R theta) R=R_2 Z(theta),
    P(R theta)=R P(theta) R^T,
    S(R theta)=R_2 S(theta) R_2^T,
    f(R theta,R v)=R_2 f(theta,v).

The complete ordered signs give

    U(R theta,R u)=R U(theta,u) R_2^T,
    U(theta,u)=sum_rho u_rho U_rho(theta).

This identity keeps each unequal eta_nu^2 output filter attached to its
permuted output component. For a single coordinate reflection with signs
s_mu, A_nu acquires s_nu in addition to R_2 on its output; W_(rho,nu)
acquires s_rho s_nu in addition to R_2^T on its input. Their product
therefore acquires s_rho. A frequency derivative in component m adds
s_m to each differentiated factor. The same assertions for permutations
follow by relabeling rho,nu,m and retaining sigma when a plane's order
reverses. Consequently both terms of J and the derivative of B transform
as two-form matrices with the two external polar indices rho,m. The
external f_a,f_b contribute the additional polar indices a,b. Torus
change of variables, with invariant normalized measure, proves that H
and T are invariant rank-four polar tensors under signed permutations.
This is an identity of the imported infinite-grid coefficient integrals;
it asserts no symmetry of a finite shifted path-label entry by itself.

Reflection in a single coordinate changes an entry by (-1) to the power
of the number of occurrences of that coordinate among rho,m,a,b.
An invariant entry is zero unless each coordinate occurs an even number
of times. The only surviving patterns are: all four equal, or two
separate equal pairs. Coordinate permutations identify the values of
all entries of each pairing pattern. H is symmetric in a,b, so its
two crossed pairings have equal values. These patterns, using (3), give

    H_(rho,m;ab)=h_D delta_(rho,m)delta_(a,b)
       +h_X[delta_(rho,a)delta_(m,b)+delta_(rho,b)delta_(m,a)]
       +h_A 1_(rho=m=a=b).                               (4)

T is antisymmetric in a,b, so it vanishes if a=b, including the all-equal
pattern and the rho=m pairing. The two crossed pairings have opposite
values. The surviving entry in (3) therefore gives

    T_(rho,m;ab)=tau[delta_(rho,a)delta_(m,b)
                                -delta_(rho,b)delta_(m,a)]. (5)

This explicit index argument proves the needed invariant-tensor fact;
no uncited representation classification or continuous rotation symmetry
is assumed. Hypercubic anisotropy h_A remains in (4).

### 3. The complete exterior-circulation term has one scalar

L118(6) gives centered paths b_pi=a_pi+i z_pi/2 and
q_pi=c_pi+i z_pi/2, with

    a_pi=eta_nu e_mu^T+eta_mu e_nu^T,
    c_pi=-eta_nu e_mu^T+eta_mu e_nu^T,
    z_pi=-d_nu e_mu^T+d_mu e_nu^T.

For a real two-form h, expand L123's C(h) before projecting:

    C(h)=C0(h)+i C1(h),
    C0(h)=2 sum_(mu<nu) eta_mu eta_nu h_(mu nu)
                                      (e_mu e_nu^T-e_nu e_mu^T),
    C1(h)=sum_(mu<nu) eta_nu h_(mu nu)
                                      (e_mu z_pi+z_pi^T e_mu^T).

The real part is even and the imaginary part odd under simultaneous
frequency reversal. Also the linked physical F(v) has projected real
part R(v) with plaquette column

    R(v)_pi=2[-eta_nu v_nu e_mu+eta_mu v_mu e_nu].

Its remaining imaginary column is -i v_mu z_pi^T, annihilated by P.
Thus L123's alpha(v)=i A(v), A(v)=P R(v) Z Q, and its generator is
g(u)=i G(u), G(u)=U(theta,u)Z. The imaginary part of beta=P C(h)Q
contributes an imaginary odd integrand in each of L123's mixed terms:
it is multiplied by the imaginary odd alpha and imaginary odd g, while
P,Q and lambda^-1 are real even. It is absolutely integrable, so this
part integrates to zero. Retain beta0(h)=P C0(h)Q.

Use symmetry of c_(i;kl) to exchange k,l in L123's second mixed term.
With no additional half or outside factor, its full local contraction is
sum_(k,l)c_(i;kl) E(h_l,V_k,u), where

    E(h,v,u)=-integral lambda^-1 tr Q
        [beta0(h)^T A(v)-A(v)^T beta0(h)] G(u).           (6)

This follows because beta0^* alpha+alpha^* beta0 equals
 i[beta0^T A-A^T beta0], and multiplication by g=iG supplies the
minus sign. Both mixed orientations remain in (6).

C0 has the exact two-form transformation
C0(R theta,R_2 h)=R C0(theta,h)R^T: its skew matrix and the attached
eta factors transform with their respective indices. The projected
R(v) transforms from two-forms to edges as R R(v)R_2^T. The displayed
Z,P,Q,U identities therefore prove E(R_2 h,Rv,Ru)=E(h,v,u).
Unlike C1, whose individual paths single out the lower plane index,
C0 is covariant; it was legitimate to remove C1 only after the integrated
parity check above.

There is only one invariant trilinear contraction of a polar u, polar v
and antisymmetric h under signed permutations. To prove this directly,
write a coefficient for u_rho v_a h_(m b), with h represented by all
antisymmetric indices. Reflection requires even occurrences among the
four indices. The pairing rho=a,m=b vanishes by antisymmetry of h;
the all-equal pattern also vanishes. The other two pairings have opposite
values by antisymmetry and equal magnitudes by permutations. Hence the
functional is a scalar multiple of sum_(rho,a)u_rho v_a h_(rho a).
Define that scalar without orientation ambiguity by

    xi=E(h^23,e_3,e_2), h^23_(23)=1,
       h^23_(32)=-1 and all other entries zero.           (7)

The contraction in this test is exactly one, so
E(h,v,u)=xi sum_(rho,a)u_rho v_a h_(rho a). No value or sign of xi
is claimed. Equation (6) with (7) is its explicit complete torus formula.

### 4. Assemble and check convergence and scope

Substitute (4)--(5) into the physical contraction of L126(3), and (7)
into L123(2). Expanding the Kronecker deltas gives exactly (1). In
particular (5)'s second pairing yields
-sum_(rho,a)u_rho V_(l,a)partial_a V_(k,rho), with no curl-only
replacement or change to H. The first pairing yields V_(l,rho)div_T V_k.
This retains the symmetric-jet obstruction established in L127.

The imported joint moments and coefficient tails already justify the
finite physical contractions and full heat sum. Directly, near theta=0,
f=O(|theta|), A_nu=O(|theta|), W=O(1), partial W=O(1/|theta|),
partial A_nu=O(1). Thus J and partial B are O(1), and every integrand
in (2) is bounded. In (6), beta0=O(1), A=O(|theta|), G=O(|theta|),
so division by lambda is again bounded. The removed imaginary term has
the same or better local integrability. Away from zero all symbols are
bounded smooth expressions on the compact cube. Absolute torus
convergence follows. Actual exterior fields and derivatives have the
polynomial mode bounds and Gaussian heat majorants already established
in L120/L123/L125; compact displacement support eliminates spatial face
terms. No new interchange of a mesh limit is required.

This is RESEARCH / REPRODUCTION under the unchanged EXPLORE assessment
drafts/literature/2026-10-10-other-other-cubic-leading-scale.md. Existing
coefficient limits and path/stencil formulas are imported at the exact
references in the hypotheses. The finite algebra and elementary signed
permutation argument are supplied because those inputs do not give the
full physical-component reduction. This is local progress by standard
methods; no originality claim beyond the checked sources is made. No
new mathematical script or numerical coefficient evaluation is needed.

## Mathlib

Full matching physical-component tensor reduction: **not checked**.
Supporting finite signed permutations, Kronecker-delta tensor algebra,
Fourier parity, finite trace identities and absolute convergence:
**not checked**. Unknown coverage is not evidence of absence.
