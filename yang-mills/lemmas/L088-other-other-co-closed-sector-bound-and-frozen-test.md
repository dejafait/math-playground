# L088 — Co-closed rough-sector boundedness and its frozen principal test

## Hypotheses

Use exactly L085–L086's finite SU(2) Gaussian, actual L010 probes
i=3,6, actual L018 residual, lower-rooted direction-1 forest, all-face
relative box, admitted even N, a=8/N and tau=1/16. Take the bare
small-coupling coefficient at fixed mesh first. Coordinates and norms
are ordinary dimensionless stored ones. All transverse plaquettes at
1<=s<N, ordered pairs including coincidences, pinned end rows and
every exterior heat mode remain.

Let X select the concatenated interior transverse links, S=Sigma_F,
K=X S X^T, V=X S A_F S X^T. Put Pcal=I tensor P, Qcal=I-Pcal,
where P is L085's full transverse relative gradient projection. Write

    K_h=Qcal K Qcal=R Qcal,
    V_h=Qcal V Qcal,
    R=(L_D tensor I+I tensor Delta_T)^(-1).

For alpha=(s,p), Lambda_alpha selects L085's (c,b,q) rows. In the
distinct-row class define only the sector

    C^h_ab=Lambda_alpha K_h Lambda_beta^T,
    V^h_ab=Lambda_alpha V_h Lambda_beta^T,
    T_hh=sum_(alpha,beta) sum_(j!=k)
                    det C^h_ab[j:U_ab,k:V^h_ab],             (1)

with U_ab=J_alpha S B_i S J_beta^T unchanged. Both endpoints of
both rough lines are co-closed. These are fixed projections after
normalized differentiation, not derivatives of base-law projection
zeros. This is one of L087's eight rough-line sectors of T_UV.

A separate diagnostic below freezes the exterior transverse stored
field to av, v real, and displacement to real u on the infinite grid.
It retains the exact plaquette traversal and staggered filters. Only
the order-1/a generator residual is kept in this diagnostic. Freezing
does not replace any covariance or coefficient in the finite sector (1).

## Conclusion

For both actual probes,

    |T_hh|<=C_i N^3,       |a^3 T_hh|<=512 C_i.              (2)

Thus this sector has no stronger power than a^-3. This bound gives
neither convergence nor a sign, and does not make a^3 T_hh vanish.
The exact finite compression in (6) below preserves all six placements.

In the separately defined frozen principal diagnostic, the sum of the
two exterior orientations vanishes pointwise at every nonzero full
frequency. This uses the exact paths, not an angular-average argument.
It suggests a signed cancellation mechanism but establishes no
frozen-to-finite remainder estimate. Variable coefficients, actual
exterior circulation, axial profiles, boundaries and the bounded
curvature forms remain in (1). The other six sectors besides L087's
gradient/gradient sector remain uncontrolled by (2).

The complete other/other scaled limit and its required comparison with
-12 gamma D_i are unresolved. Other response jets, N^2 remainders,
slower powers/logarithm, finite matching, interacting error <=c_box/2,
continuum axioms, reflection positivity, infrared control and finite
positive mass remain separate gaps. No candidate is asserted.

## Proof

### 1. Compress the actual six placements without changing U

On the full interior edge space let Cc, Bb, Bq select all c,b,q rows.
All three maps have mesh-independent operator norms: their finite
stencils have bounded row and column multiplicity, including pinned
end rows. In particular Cc=I tensor D. Take v_k in forest coordinates
by restricting L028's retracted full-link exterior column, as in
L086's actual heat expansion. Set z_k=X v_k and write f_k=Cc z_k,
b_k=Bb z_k, q_k=Bq z_k. Define

    Omega_k=Bb^T M_(f_k) Bq-Bq^T M_(f_k) Bb
            +Bq^T M_(b_k) Cc-Cc^T M_(b_k) Bq
            +Cc^T M_(q_k) Bb-Bb^T M_(q_k) Cc.              (3)

Here M denotes a real diagonal multiplier on the complete plaquette
array. Omega_k^T=-Omega_k. Define Omega^h_k=Qcal Omega_k Qcal.
The actual exterior expansion is

    U_ab=sum_(k,l) c_(i;kl) u_(k;alpha) u_(l;beta)^T,
    c_(i;kl)=exp[-tau(nu_k+nu_l)] (B_i^rel)_kl,
    u_(k;alpha)=J_alpha v_k.                               (4)

Its coefficients are real and symmetric in k,l. L028/L086 gives a
mesh-independent polynomial p such that

    ||f_k||_infinity<=C a^2 p(k),
    ||b_k||_infinity+||q_k||_infinity<=C a p(k),
    sum_(k,l)|c_(i;kl)|p(k)p(l)<=C_i.                      (5)

These bounds include transverse end rows and all interior levels;
there is no s=N transverse potential jump in this group.

The exact finite identity is

    T_hh=sum_(k,l)c_(i;kl)
                   Tr(Omega^h_k V_h (Omega^h_l)^T K_h).    (6)

To verify the factor and orientation, for one alpha write its local
matrix as sum_(j,r,t) epsilon_(jrt) u_(k;alpha,j)
Lambda_(alpha,r)^T Lambda_(alpha,t). Expand the trace against the
analogous beta matrix. Its summands are

    epsilon_(jrt) epsilon_(abc) u_(k;alpha,j)
           u_(l;beta,a) (V^h_ab)_tc (C^h_ab)_rb.

Swapping r,t and b,c changes both epsilon signs, leaving precisely
the determinant expansion with U in row j, V^h in row r and C^h
in the remaining row t. Summing j!=r gives all six replacements.
This proves (6), including coincident pairs. There is no outside
factor 3 here; L085 supplies that factor only for O_i. No Wick
contraction is reproved or omitted from L048.

### 2. Bound the complete finite co-closed sector at the tested scale

L086's complete spectrum gives Tr K_h<=C N^4 and
||K_h||<=C N^2. On the co-closed subspace,

    ||Cc K_h^(1/2)||<=1.                                  (7)

Indeed its squared singular eigenvalues are
lambda/(mu_k+lambda)<=1, with all axial Dirichlet modes and full
transverse co-closed spectrum retained, as in L085–L086. Square
roots and restrictions below act on this subspace; their extension
by zero on gradients causes no difficulty.

The actual residual has the two-sided form bound

    -C N K_h <= V_h <= C N K_h.                            (8)

For applicability, Qcal X applied to the forest field removes the
transverse prefix gradient exactly. Its row map in the full Hodge
Gaussian is H=Qcal I_T^T, with interior-level restriction included.
L018's gauge-invariant residual lift then gives
K_h=H Sigma H^T and V_h=H Sigma A_0 Sigma H^T. L020(11) gives
||Sigma^(1/2) A_0 Sigma^(1/2)||<=C/a for this same residual and box.
Testing against H^T y proves (8), since a=8/N. This imports the
actual rough form bound; no smooth-residual-column estimate is used.
Consequently V_h=K_h^(1/2) W_h K_h^(1/2), ||W_h||<=C N.

For either path map B, bounded multiplicity implies

    ||B K_h^(1/2)||<=C N,
    ||B K_h^(1/2)||_HS<=C N^2.                            (9)

For the first two terms of (3), (5) and (9) bound the Hilbert–Schmidt
norm after multiplication by K_h^(1/2) on both sides by
C a^2 p(k) N^3. For each of the other four terms, use (7) on the
curvature side and (9) on the path side, giving C a p(k) N^2.
Projections Qcal commute with K_h and do not alter these estimates.
Hence

    ||K_h^(1/2) Omega^h_k K_h^(1/2)||_HS
       <=C p(k)(a^2 N^3+a N^2)<=C' p(k) N.                (10)

Hilbert–Schmidt Cauchy–Schwarz in (6), using (8), gives an upper
bound C N^3 p(k)p(l) for each trace. Sum by (5) to obtain (2).
Every heat mode, axial level, pinned row and residual placement is
retained. This excludes stronger powers only within this sector;
the estimate is compatible with an a^-3 coefficient of either sign.

### 3. Check the constant-exterior symbol with the exact paths

Use the staggered plaquette-center phases of L070. Write
d_j=2 sin(theta_j/2), eta_j=cos(theta_j/2). In plane mu<nu the
four signed edge rows are

    exp(-i theta_nu/2) e_mu^T,
    exp( i theta_mu/2) e_nu^T,
   -exp( i theta_nu/2) e_mu^T,
   -exp(-i theta_mu/2) e_nu^T.

Thus the circulation row is c=i z with
z=-d_nu e_mu^T+d_mu e_nu^T, and

    b=(eta_nu-i d_nu/2)e_mu^T
                        +(eta_mu+i d_mu/2)e_nu^T,
    q=(-eta_nu-i d_nu/2)e_mu^T
                        +(eta_mu+i d_mu/2)e_nu^T.         (11)

For a constant stored exterior field av,
f=0, b(v)=a(v_mu+v_nu), q(v)=a(v_nu-v_mu). Put

    F=b(v)q-q(v)b=2a r+a v_mu c,
    r=-v_nu eta_nu e_mu^T+v_mu eta_mu e_nu^T.              (12)

Direct substitution of (11) verifies both real and imaginary parts
in (12). The plane symbol of (3) is F^*c-c^*F. The a v_mu c term
cancels exactly, so it is

    2ia(r^T z+z^T r).                                    (13)

It is purely imaginary times a real symmetric matrix. Summing all
transverse planes preserves this property: Omega_v=i S_v with S_v
real symmetric. This calculation retains the imaginary parts of
both two-edge paths; dropping them before (12) would not justify
the exact identity. Actual nonconstant f is excluded only by this
diagnostic definition, not from the finite operator (3).

### 4. Symmetrize both exterior orientations in the principal test

Let theta=(theta_1,...,theta_4), h=sum_j d_j^2>0 and
lambda=sum_(j=2)^4 d_j^2. For lambda>0 put
Pi=I-d_T d_T^T/lambda. This is the transverse co-closed projection.
For lambda=0 choose Pi=I: all transverse circulation symbols and
(13) are then zero. The infinite-grid co-closed covariance symbol is
K_h(theta)=Pi/h, a real symmetric matrix. This is only the formal
local symbol, not the finite two-level covariance of (1).

The exactly frozen L009 clover/endpoint generator has

    K_(nu nu)=(i/a) eta_nu^2
                        sum_(rho!=nu) u_rho eta_rho d_rho,
    K_(nu rho)=-(i/a)u_rho eta_rho eta_nu^2 d_nu
                                              (rho!=nu). (14)

Each clover supplies eta_rho eta_nu and endpoint averaging supplies
the second eta_nu; the centered curl supplies i d/a. This agrees
with L066's retained component formulas. All four components occur.
Thus K=i W/a with W real. For L_0=h I-d d^T, the frozen generator
part of the symmetric residual is

    A_pr=(L_0 K+K^* L_0)/2=i Z/a,
    Z=(L_0 W-W^T L_0)/2,      Z^T=-Z.                    (15)

The frozen full Hodge covariance is h^-1 I. Therefore the symbol
of the projected residual line is
V_pr=i Pi Z_TT Pi/(a h^2), purely imaginary times a real
antisymmetric matrix. The transverse prefix contributes nothing
after Pi. Set Z_h=Pi Z_TT Pi/(a h^2), R_h=Pi/h and
S^h_v=Pi S_v Pi; their transpose properties remain valid.

For two real exterior vectors v,w, the trace symbol from (6) is

    F(v,w)=Tr[(i S^h_v)(i Z_h)(-i S^h_w) R_h]
          =i Tr(S^h_v Z_h S^h_w R_h).                    (16)

Transposing the scalar trace and cyclically moving its last factor
gives F(w,v)=-F(v,w), because Z_h is antisymmetric and the other
three real matrices are symmetric. In particular F(v,v)=0, and
the sum with any real symmetric exterior coefficient matrix is zero
pointwise. L028's actual coefficients c_(i;kl) are symmetric;
freezing each real exterior column at the same spatial point therefore
has exactly this cancellation for either probe. No angular integral,
odd-frequency cancellation, zero axial mode substitution, or assumed
commutation of Pi with S_v is needed.

### 5. What the diagnostic does and does not justify

Equations (2) and (6) are statements about the actual finite sector.
Equations (11)–(16) are statements only about the specified frozen
principal test. To deduce a^3 T_hh->0 from them would require control
of coefficient and exterior differences, their compositions with the
full resolvent/projection, physical boundary corrections, and the
bounded Q_3,Q_6 residual terms. None is proved here. The gradient
prefix and crossed residual blocks remain outside (1), and cannot be
replaced by this pointwise symbol. In particular L070's mixed frozen
symbol is not canceled by this result.

This is one bounded mathematical attempt under the unchanged EXPLORE
assessment `drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
The finite contraction is imported through L085 from L048. The specialization
checks a previously unbounded rough sector and the exact signed
principal test; it is local REPRODUCTION of the recorded spectral,
finite-matrix and stencil methods, with no novelty claim beyond the
sources checked. No numerical script or new literature review is
needed. The comparison value and L082's arithmetic qualifications
remain unchanged; no numerical value of D_i is used.

## Mathlib

Full matching theorem: **not checked**. Supporting finite determinant,
Hilbert–Schmidt, transpose, relative spectral and Fourier-stencil
coverage: **not checked**. Unknown availability is not absence. No
general continuum Ward or flow theorem is imported to control this
isolated bare forest sector.
