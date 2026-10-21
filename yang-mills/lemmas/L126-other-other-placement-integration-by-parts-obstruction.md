# L126 — Spatial integration by parts retains a displacement tensor

## Hypotheses

Use L120's K_(i,V) and L125's K_(i,sc)+K_(i,en), with exactly
their hypotheses: SU(2), both actual L010 probes i=3,6, the straight
lower-rooted direction-1 forest, relative all-face fixed-link box
D_box=(-4,4)^4, admitted even N, a=8/N, tau=1/16, and the bare
small-coupling coefficient at fixed mesh before refinement. Keep the
original paths, ordered generator signs, prefix including the constant
axial mode, pinned rows and full exterior heat sums. This calculation
imports their coefficient limits and does not take another mesh limit.

Use L119(1)--(2)'s finite stencils A_r=D T_r and C_r. Here D is the
dimensionless transverse circulation; A_r in this file excludes C_r.
Put S=sum_j E_j=D D^*/lambda on the full transverse grid, and
W_r=C_r S, G_r=A_r W_r. These symbols use the original lower-vertex
convention. Define Q_(alpha,beta)=S_alpha^* P_inf S_beta as in L120(1),
M_(r,m;alpha,beta) as in L125(1), and

    b_(r,m;alpha,beta)=sum_j beta_(r,j,m;alpha,beta),
    M^+_(ab)=(M_(ab)+M_(ba))/2,
    M^-_(ab)=(M_(ab)-M_(ba))/2,
    b^+_(ab)=(b_(ab)+b_(ba))/2,
    H_(r,m;alpha,beta)=b^+_(r,m;alpha,beta)
                                      -M^+_(r,m;alpha,beta)/2. (1)

The shorthand ab refers only to path labels alpha,beta, with r,m
fixed. The coefficient c_(i;kl) is real and symmetric in k,l:
L088(4), or L120(2) and self-adjointness of the real probe form.
Every torus integral below uses dtheta/(2pi)^3 on [-pi,pi]^3.

## Conclusion

The absolutely convergent displacement tensor has the formulas

    b_(r,m;alpha,beta)
      =i integral tr[A_r partial_m W_r Q_(alpha,beta)]
      =M_(r,m;alpha,beta)
           -i integral tr[(partial_m A_r) W_r Q_(alpha,beta)]. (2)

Here partial_m in (2) is the frequency derivative. In physical space,
with ell=x_1+4, the exact coefficient identity is

    K_(i,V)+K_(i,sc)+K_(i,en)
      =sum_(k,l)c_(i;kl) sum_(r,m,alpha,beta)
          [H_(r,m;alpha,beta)
             integral_D ell (partial_m u_(rho(r)))
                                phi_(l,alpha) phi_(k,beta) dx
           +M^-_(r,m;alpha,beta)
             integral_D ell u_(rho(r))
                                phi_(l,alpha) partial_m phi_(k,beta) dx].
                                                               (3)

In (3), partial_m is spatial and m=2,3,4. The antisymmetric term
is retained. All sums and integrals in (3) are absolutely convergent.
There is no new color, symmetry or outside factor 3.

The tensor H is not zero, even after summing the complete ordered
generator list at a fixed displacement component. For r=(rho=2,nu=3),
m=2, pi=(23), sum over alpha,beta in {(pi,b),(pi,q)} and write b_*,
M_*,H_* for these sums. Then

    b_*=M_*+P_*,
    H_*=M_*/2+P_*>0,
    P_*=integral 4 eta_3^4 eta_2^2 d_2^2 (d_2^2+d_3^2)/lambda^2>0,
    d_mu=2 sin(theta_mu/2), eta_mu=cos(theta_mu/2),
    lambda=d_2^2+d_3^2+d_4^2.                            (4)

L125(4) gives M_*>0. The other ordered r with rho=2,nu=4 has zero
contribution to this same-plane test, so it cannot cancel (4) in
the universal displacement-2 tensor. Thus the sufficient universal
identity b^+=M^+/2 fails. This stops elimination of the displacement
derivative by that identity; it does not exclude identities after
restriction to the actual probes or combination with K_(i,f).

In L124 only the three coefficients in (3) are regrouped. K_(i,f)
and the other five coefficients retain their original signs and L124's
single outside factor 3. Neither actual-probe coefficient nor
K_(i,oo)+4 gamma D_i is evaluated. No compensation, finer remainder,
logarithmic coefficient, other-jet bound, interacting reflected error
<=c_box/2, continuum axioms, reflection positivity, infrared control
or finite positive mass follows.

## Proof

### 1. Differentiate the correct factor in the original phases

Let w_(r,j)(d)=sum_q C_r(q)e_j(d+q), the kernel of C_r E_j.
L119(2) becomes

    B_(r,j,m)(d)=sum_h (d_m+h_m) A_r(h) w_(r,j)(d+h).

For the convention hat k=sum_d k(d) exp(-i d dot theta), substitution
z=d+h and the weak Fourier derivative give

    hat B_(r,j,m)=i A_r partial_m(C_r hat E_j).         (5)

This is an L2 identity, not a formal manipulation of a nonsummable
absolute moment. L119(10)--(11) gives summable axial bounds for both
||e_j||_2 and || |d| e_j||_2. Finite C_r shifts preserve these bounds,
so sum_j C_r hat E_j converges in periodic W^(1,2). Its value is W_r:
the axial multiplier sums to 1/lambda by L125 proof section 2;
the same bounds identify that pointwise sum with the W^(1,2) sum.
Finite multiplication by A_r is bounded in W^(1,2).

Q has a bounded Fourier symbol and therefore belongs to L2.
Plancherel and L120(14) permit pairing (5) with Q and summing j.
This yields the first formula (2). L125(7)--(8) identifies
M=i integral tr[(partial_m G_r)Q]. Applying the weak product rule
to G_r=A_r W_r proves the second formula. W_r=O(1) and
partial_m W_r=O(1/|theta|) near zero, so these integrals are also
directly locally integrable in three dimensions. They are real by
their original real-kernel definitions. No integration by parts
in a nonperiodic centered entry has been used.

### 2. Symmetrize only the physical coefficient contraction

At each x, symmetry in k,l gives

    sum_(k,l)c_(i;kl) phi_(l,alpha) phi_(k,beta)
      =sum_(k,l)c_(i;kl) phi_(l,beta) phi_(k,alpha).

Thus L120(3)'s contraction of b uses only b^+. In L125(2)'s
contraction of M^+, swapping both k,l and alpha,beta shows that
the same value is obtained with the derivative on phi_l instead
of phi_k. Averaging those equal expressions gives

    (1/2) sum_(k,l)c_(i;kl) sum_(r,m,alpha,beta) M^+_(r,m;alpha,beta)
          integral_D ell u_(rho(r))
                     partial_m(phi_(l,alpha) phi_(k,beta)) dx.

The displacement is smooth and compactly supported inside the box.
For transverse m, partial_m ell=0; physical integration by parts
therefore changes this expression into minus one half the same sum
with (partial_m u) phi_l phi_k. There is no face contribution and
no differentiation of the physical prefix in x_1. For each heat label
the exterior fields and their transverse derivatives are smooth on
that compact set. Their polynomial mode bounds from L121 proof
section 5, and the Gaussian heat majorants in L120/L125, justify
all swaps, averaging and integration by parts through the full sums.
The M^- part is unchanged. Adding K_V proves (3).

### 3. Track centered phases before testing the residual

Use L118's plaquette phase U_2 and R_m=diag_pi
[(1_(m=mu)+1_(m=nu))/2]. Vertices have no phase. Hence

    A_r=U_2 A_(r,c), W_r=W_(r,c) U_2^*,
    Q=U_2 Q_c U_2^*,
    i tr[A_r partial_m W_r Q]
      =i tr[A_(r,c) partial_m W_(r,c) Q_c]
                              +tr[G_(r,c) R_m Q_c].  (6)

L118 proves A_(r,c) imaginary and odd, W_(r,c) real and even,
and Q_c real and even under simultaneous theta reversal.
The last integrand in (6) is thus imaginary and odd; it is integrable
and its integral is zero. This justifies using the first term to
compute b; the phase term was not omitted pointwise. L125(9)
already supplies the corresponding phase check for M.

### 4. A positive symmetric same-plane residual

For r=(rho=2,nu=3), L118 proof section 3 gives

    A_(r,c)=D_c eta_3 e_3,
    W_(r,c)=eta_2 eta_3 epsilon_(23)^T S_c.

The four path-pair sum has Q_*=J epsilon_(23) epsilon_(23)^T,
J=4 eta_3^2 d_2^2/lambda, exactly as in L125 proof section 4.
Put h=(d_2^2+d_3^2)/lambda, a_0=eta_3 d_2 and w=eta_2 eta_3 h.
Only the (23,23) entry enters this trace. Equations (2),(6) give

    b_*=-integral a_0 (partial_2 w) J,
    M_*=-integral partial_2(a_0 w) J,
    b_*-M_*=integral (partial_2 a_0) w J=P_*.

Since partial_2 a_0=eta_3 eta_2, direct substitution gives the
P_* integrand in (4). It is nonnegative, bounded near zero, and
strictly positive near (pi/2,pi/2,pi/2), so P_*>0. L125(4)
supplies the independent positive formula for M_*. Summing over
all four pairs annihilates the antisymmetric label part, giving
H_*=b_*-M_*/2 and (4). No frequency boundary integration by parts
is needed for this witness.

For the other generator with rho=2,nu=4, the (23,4) circulation
entry is identically zero. Thus (A_(r,c))_(23)=0, also after its
theta_2 derivative. With Q_* supported solely on (23,23), both
its M_* and b_* are zero. These are the two possible output components
for displacement rho=2 in the full transverse list. This checks the
stated fixed-displacement qualification without dropping a generator.

This is failure of a universal sufficient identity. Physical mode
fields determine coefficients in all planes and are not arbitrary
independent path values. Accordingly the witness proves neither a
nonzero value of (3) for i=3,6 nor a failure of complete compensation.
K_f and the other coefficients remain essential.

### 5. Scope and method

The calculation is RESEARCH / REPRODUCTION under the unchanged EXPLORE
assessment drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
The coefficient limits, tails and exact stencils are imported by the
equation and section references above. Fourier differentiation and
spatial integration by parts are written out to justify their different
placements, phases and half-factor; no general source theorem assigns
this isolated forest coefficient. The new local evidence is the failed
necessary tensor identity for this elimination mechanism, without a
novelty claim or any mathematical progress beyond the sources checked.

## Mathlib

Full matching tensor obstruction: **not checked**. Supporting weak
Fourier differentiation, product rule, finite symmetrization and compact
spatial integration by parts: **not checked**. Unknown availability is
not absence. This analytic witness requires no numerical certificate
or mathematical script.
