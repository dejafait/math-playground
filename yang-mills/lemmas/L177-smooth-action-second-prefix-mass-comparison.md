# L177 — Static second prefix and simultaneous transverse mass comparison

## Hypotheses

Keep L176's hypotheses: SU(2), the relative box (-4,4)^4,
a=8/N through admitted even meshes, the straight direction-1
lower-rooted forest, the complete compact displacement, and both actual
L010 probes i=3,6 at tau=1/16. The bare expansion precedes refinement.
All matrices and norms use ordinary stored coordinates. Use L175's
A^gen, endpoint sum S, signed transverse J_j, action multipliers
m_(j,l), exterior columns h_k and heat coefficients c_(i;kl).
All action faces, normal end links and heat modes remain.

Let P be the axial lower-prefix matrix from N component-1 edge levels
to N-1 interior vertex levels: P_(s,r)=1 for 0<=r<s and zero otherwise.
Let E_1 extract the component-1 links, including both axial end edges.
Thus Phi=(P tensor I) E_1; its output has no boundary-vertex rows.
On transverse interior vertices put G=(Delta_T)^(-1) and
G_epsilon=(Delta_T+epsilon I)^(-1), 0<epsilon<=1. Define

    H_epsilon=M tensor G_epsilon,       M=P P^T,
    F^0=(P tensor G) E_1,
    F^0_delta=(P tensor G_delta) E_1,    0<delta<=1.       (1)

These are comparison matrices, not a replacement Gaussian field law.
In particular the full pinned upper forest jump is not extended smoothly.
For a vertex-to-link cross matrix Z set

    U_i^epsilon(Z)=-6 sum_(k,l) c_(i;kl) sum_(j=2)^4
       Tr[H_epsilon m_(j,l) J_j Z A^gen M_(h_k) S].     (2)

Then L176's W_i^epsilon=U_i^epsilon(F), F=Phi Sigma.

## Conclusion

With constants independent of N,epsilon,delta,

    |U_i^epsilon(F)-U_i^epsilon(F^0)|
                                  <=C_i N^2 epsilon^(-1/2),
    |U_i^epsilon(F^0)-U_i^epsilon(F^0_delta)|
            <=C_i epsilon^(-1/2)[N^2+N^3 delta^(3/4)].   (3)

In particular define the fully transversely massive trace

    W_i^(epsilon,epsilon)=U_i^epsilon(F^0_epsilon).      (4)

L176 and (3) imply

    |V_i-W_i^(epsilon,epsilon)|
       <=C_i[N^(5/2) sqrt(log(eN))
                    +N^2 epsilon^(-1/2)+N^3 epsilon^(1/4)],
    limsup_(N->infinity) |a^3(V_i-W_i^(epsilon,epsilon))|
                                      <=C_i epsilon^(1/4).    (5)

The two axial profiles M and P remain exact and long range. All
multipliers and generator orientations retain the order (2). This
supplies a controlled second-prefix replacement and mass removal,
not a fixed-mass signed limit or a coefficient. In particular no
vanishing or full compensation follows. This is local standard-method
REPRODUCTION, with no novelty claim. The other response jets, finer
asymptotics, interacting comparison and continuum/infrared gaps remain.

## Proof

### 1. Exact rectangular prefix identity on the pinned domains

Write D for the full axial gradient from the N-1 interior vertex
values to the N edges, with endpoint vertex values zero:
(Dx)_r=x_(r+1)-x_r, 0<=r<N. Telescoping gives

    P D=I,     P P^T=M,     P D D^T=D^T,
    L_D=D^T D,             L_E=D D^T.                  (6)

The first identity uses the lower pinned endpoint only; the last
edge r=N-1 remains in D and L_E even though P's last column is zero.
L_E has its constant edge mode. The boundary convention agrees with
L026/L156's component-1 covariance

    Sigma_1=(L_E tensor I+I tensor Delta_T)^(-1).

There are no mixed-component blocks in Sigma. Put
R_D=(L_D tensor I+I tensor Delta_T)^(-1). From
(L_E+lambda)D=D(L_D+lambda) for each transverse eigenvalue lambda,
(6) gives exactly

    F^0-F=R_D(D^T tensor G) E_1.                        (7)

Indeed G-(L_E+lambda)^(-1) equals
lambda^(-1)L_E(L_E+lambda)^(-1); multiply by P and use
P L_E=D^T and the resolvent intertwining. This proof neither removes
nor approximates the zero axial eigenmode: its contribution to the
difference is exactly zero.

Let Delta=Sigma^(-1) be the full link Hodge Laplacian. For
Z=F^0-F, the commuting tensor factors and (7) give

    Z Delta Z^T
       =R_D(L_D tensor G^2)
       <=I tensor G^2.                                 (8)

For example on axial/transverse eigenvalues alpha>0,lambda>0 the
left side is alpha/[(alpha+lambda)lambda^2], bounded by lambda^(-2).
This positive comparison is for the energy square of this cross
matrix. It is not a bound on the signed forest remainder E.

For Z_delta=F^0-F^0_delta put T_delta=G-G_delta>=0. Directly from
(6), without an axial resolvent approximation,

    Z_delta Delta Z_delta^T
       =I tensor T_delta^2
                    +M tensor Delta_T T_delta^2.       (9)

In (9), P L_E P^T=I. Both terms are retained; discarding the second
would incorrectly discard a potentially cubic contribution.

### 2. Massive multiplier energy and the unchanged trace order

For a smooth real sampled scalar m of physical C^2 norm at most b,

    ||H_epsilon^(1/2) m H_epsilon^(-1/2)||<=C b,        (10)

uniformly for N and epsilon. To check its domain and mass dependence,
let B be the lower-anchored backward difference in L159(13), and D_T
the full transverse Dirichlet gradient. Then

    ||H_epsilon^(-1/2)x||^2
       =||(B tensor D_T)x||^2+epsilon||(B tensor I)x||^2.

L159's four-term mixed product identity bounds the first term after
multiplication by m by C b times the original mixed norm, using the
same lower-anchored and transverse Dirichlet Poincare inequalities.
For the second term, the one-direction product identity bounds
||B(mx)|| by C b(||Bx||+N^(-1)||x||)<=C b||Bx||.
The multiplier has its smooth sampled extension at boundary rectangles;
x retains its zero lower/transverse boundary values. Adding the two
squares proves the bound for H_epsilon^(-1/2)m H_epsilon^(1/2).
Transpose it to obtain (10). No constant blows up as epsilon decreases.
In particular b<=C a^3 p(l) for the actual m_(j,l), by L159(6).
The smooth action column is global, including its normal end edges;
it has not been cut off.

For clarity fix k,l,j and set h=h_k,m=m_(j,l),H=H_epsilon.
Choose L175's cutoff chi equal to one on the input support of A^gen.
Use the factors

    B_gen=Sigma^(1/2) A^gen Sigma^(1/2),
    X=Sigma^(-1/2) chi M_h S H^(1/2),
    Y_Z=H^(1/2) m J_j Z Sigma^(-1/2).

Cyclicity and A^gen chi=A^gen give exactly

    Tr(B_gen X Y_Z)=Tr[H m J_j Z A^gen M_h S].          (11)

Thus no multiplier has moved across Z, a covariance or the generator.
L175(7) bounds ||B_gen||<=C N. Since H<=M tensor G,
Tr H<=C N^5, and the compact-input exterior bound is
||chi h_k||_infinity<=C a p(k). Consequently

    ||X||_HS<=C p(k) N^(3/2).                          (12)

Only the residual input is localized. No global O(a) bound across the
upper forest jump is used. Equations (10) and (11) give

    ||Y_Z||_HS^2
       <=C a^6 p(l)^2 Tr[H J_j (Z Delta Z^T) J_j^T].   (13)

To see (13) without a commutation assumption, factor
H^(1/2)m=(H^(1/2)m H^(-1/2))H^(1/2) in Y_Z and apply the
Hilbert--Schmidt ideal inequality. The remaining square is exactly
the positive trace on the right.

### 3. Complete spectral bounds for the first replacement

The transverse skew difference satisfies J_j^T J_j<=4 Delta_T:
write each centered difference as the sum of its two adjacent forward
differences and include the transverse end edges in the energy sum.
Since ||G_epsilon||<=epsilon^(-1), (8) and (13) imply

    ||Y_(F^0-F)||_HS^2
       <=C a^6 p(l)^2 Tr M
                          Tr[G_epsilon J_j G^2 J_j^T]
       <=C a^6 p(l)^2 N^2 epsilon^(-1) Tr G
       <=C p(l)^2 N^(-1) epsilon^(-1).                 (14)

The full transverse spectrum gives Tr G<=C N^3 as in L159(8).
No J_j/G commutation is used: the trace estimate uses
Tr[J_j G^2 J_j^T]=Tr[G^2 J_j^T J_j]<=4 Tr G.
The finite inequality |Tr(B X Y)|<=||B|| ||X||_HS ||Y||_HS,
(12), and (14) give C p(k)p(l) N^2 epsilon^(-1/2).
After the complete exterior heat sum this proves the first part of (3).

### 4. Second inverse regularization, including its cubic term

The first term of (9) obeys precisely (14), since
0<=T_delta^2<=G^2. For its second term, the axial factor in (13)
is Tr M^2<=C N^4. The same J_j energy inequality gives

    Tr[G_epsilon J_j Delta_T T_delta^2 J_j^T]
       <=4 epsilon^(-1) Tr[Delta_T^2 T_delta^2]
       =4 epsilon^(-1) sum_q delta^2/(lambda_q+delta)^2.
                                                               (15)

Every transverse mode is retained. With max q_j=m there are at most
3m^2 modes and lambda_q>=4m^2/N^2. Set t=N sqrt(delta)/2. Then

    sum_q delta^2/(lambda_q+delta)^2
       <=3 sum_(m>=1) m^2 t^4/(m^2+t^2)^2
       <=C t^3<=C N^3 delta^(3/2).                    (16)

For 0<t<1, the series is at most
3t^4 sum m^(-2)<=C t^3. For t>=1, split at m=floor(t).
Below t use sum m^2<=C t^3; above t use
t^4 sum_(m>t) m^(-2)<=C t^3, with a fixed constant also covering
1<=t<2. This proves (16) for all masses and meshes, without imposing
N sqrt(delta)>=1 or dropping low modes.

Combining (9), (13), (15), and (16) yields

    ||Y_(F^0-F^0_delta)||_HS^2
       <=C p(l)^2 epsilon^(-1)
                            [N^(-1)+N delta^(3/2)].    (17)

Use sqrt(x+y)<=sqrt(x)+sqrt(y), then (11)-(12). The trace error
is at most C p(k)p(l) epsilon^(-1/2)[N^2+N^3 delta^(3/4)].
L156(8)'s summability of |c_(i;kl)|p(k)p(l) over every exterior heat
mode proves the second part of (3). The three transverse directions
and the -6 in (2) are included once in these bounds; no new color
factor or action pairing factor is inserted.

Finally choose delta=epsilon, fixed independently of N. Combine (3)
with L176(3), and use epsilon^(-1/2)epsilon^(3/4)=epsilon^(1/4).
This gives (5). In its limsup, a^3 N^2 epsilon^(-1/2) tends to zero
for each fixed epsilon; mass removal occurs only afterwards. This is
not an instruction to select a mesh-dependent mass inside a
fixed-mass convergence theorem.

### 5. Scope and remaining test

The proof uses exact rectangular identities, positive energy squares,
finite trace inequalities and the complete transverse spectral shell
sums. No numerical certificate, external theorem, heat-value enclosure
or mesh extrapolation is used. It retains both axial ends in the
relative inverse and the constant axial mode. The resulting comparison
has an undamped lower prefix, but that substitution is justified only
in (2), at the error scale established above.

A next proof may now test the fixed-epsilon signed limit of (4), where
both transverse inverses are bounded and can be approximated by finite
polynomials. That further step still must control approximation errors,
variable coefficients, boundaries, the exact generator order and both
long axial profiles. Neither a frozen calculation nor (5) supplies it.
The complete-response vanishing test still requires the resulting V_i
coefficient to equal 6K_(i,R)-K_(i,T), with L172/L174's other sectors
retained. No equality is asserted here.

### 6. Separate critical audit of the second-prefix mass modulus

Audit date: 2026-10-21. STEP_ID:
YM-20261021-394-static-upstream-mass-critical-audit.
The verdict is acceptance of (3)--(5), relative to the stated imports
and L176's comparison, audited separately in its proof section 5.
No correction is needed. This closes the uniform-comparison condition
in the separate L179 coefficient-limit audit, without auditing L175's
preceding reduction or asserting a complete response rate.

On the exact rectangular domains, P D=I telescopes from the lower
pinned value. Although P's last column is zero, D has its last edge
row -x_(N-1). Hence P L_E=D^T and P L_E P^T=I hold with that row
retained. For each transverse eigenvalue lambda>0,

    P[lambda^(-1)I-(L_E+lambda)^(-1)]
       =lambda^(-1)(L_D+lambda)^(-1)D^T.

This verifies (7), including its sign and every source edge. The
constant edge vector has D^T value zero, so its contribution cancels
in this difference rather than being omitted. Multiplying on both
sides by the actual component-1 Hodge Laplacian gives (8). For the
second difference the same operation gives exactly

    (P tensor T_delta)(L_E tensor I+I tensor Delta_T)
                         (P^T tensor T_delta)
       =I tensor T_delta^2+M tensor Delta_T T_delta^2.

Thus both terms in (9) are essential and present. There is no
full-link mixed-component block missing: L026's Hodge inverse is
component diagonal, and E_1 includes both normal axial end edges.

The uniform multiplier bound (10) was checked on its precise domain.
With B the n by n lower-anchored backward difference, H_epsilon^(-1)
has quadratic form

    ||(B tensor D_T)x||^2+epsilon||(B tensor I)x||^2.

In the first square, the four-corner product identity in L159 proof
section 3 bounds the mixed difference of mx by a constant times
b times the sum of the mixed difference of x, N^(-1) times its two
first differences, and N^(-2) times x. Slice Poincare inequalities
bound the latter three quantities by the mixed difference. Transverse
end rectangles have zero x values at their pinned vertices and the
smooth extension of m at all four corners. The axial backward
rectangles use only the lower zero value and existing interior levels;
no upper Dirichlet value is inserted. For the second square the
one-direction product rule and ||x||<=N||(B tensor I)x|| give
||(B tensor I)(mx)||<=C b||(B tensor I)x||.
Both estimates have constants independent of epsilon. Adding their
squares and transposing the resulting conjugation inequality proves
(10), for b=C a^3 p(l), including the complete action extension.

The signed factorization (11) has the same exact order as L176's:
no inverse, multiplier, prefix or generator is exchanged. It yields
(13) by a Hilbert--Schmidt ideal inequality. In the first energy
square, use ||G_epsilon||<=epsilon^(-1), then cycle only the finite
trace to use J_j^T J_j<=4 Delta_T. Thus
Tr[G_epsilon J_j G^2 J_j^T]<=4 epsilon^(-1) Tr G;
no commutation of J_j and G is required. Since Tr M=O(N^2),
Tr G=O(N^3), and a^6=O(N^(-6)), its squared norm is
O(p(l)^2 N^(-1)epsilon^(-1)). With ||B_gen||=O(N) and
||X||_HS=O(p(k)N^(3/2)), this gives the first error in (3).

For the second energy square, the I term has that same bound.
The M term instead contributes Tr M^2=O(N^4) and, by the same
ordered trace inequality, at most
4 epsilon^(-1) sum_q delta^2/(lambda_q+delta)^2.
The complete shell estimate (16) is O(N^3 delta^(3/2)):
when t=N sqrt(delta)/2<1 the bound is O(t^4)<=O(t^3);
when t>=1, splitting at t gives O(t^3) on both sides.
It therefore includes all small masses and low modes, without any
mesh/mass restriction. Its squared norm is
O(p(l)^2 N epsilon^(-1)delta^(3/2)). Taking both square roots
and the unchanged B_gen,X factors gives exactly the second error
in (3), including the potentially cubic term.

The full heat sum is taken with the same fixed polynomial envelopes
before any limit. At delta=epsilon, that cubic term becomes
N^3 epsilon^(1/4); the other second-prefix terms are
O(N^2 epsilon^(-1/2)). Combining with L176(3) gives (5).
For each fixed epsilon>0 only the latter N^2 term and the subcubic
prefix-covariance error vanish after multiplication by a^3 and the
mesh limsup. The remaining modulus is C_i epsilon^(1/4), which
tends to zero subsequently. Together with the independently audited
fixed-mass limits in L178/L179, this justifies L179(7)'s mass-Cauchy
identification. It neither sets mass to zero in a limiting density nor
applies a fixed-mass theorem at mesh-dependent mass. All coefficient
levels, long M,P profiles, both generator orders and the sole -6
remain throughout. Other component rates, quantitative assembly and
all interacting, continuum and infrared gaps remain unresolved.

## Mathlib

Full matching theorem: **not checked**. Supporting finite trace/Schatten
inequalities, rectangular resolvent identities and tensor spectral
estimates: **not checked**. Unknown coverage is not absence. Reuse the
unchanged [assessment](../drafts/literature/2026-10-12-cubic-residual-action-cubic-scale.md).
No new external theorem is imported or reproved. The specialization is
needed for the two different prefix placements and the exact pinned
domains; L176 regularized only the left covariance and did not cover
this second factor.
