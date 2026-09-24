# Lemma 297: endpoint stationary-weight mass and indefiniteness

**Hypotheses.** Retain L288's exact interior stationary weight at h=5. Its identities give 2n=r; the statements below hold for every real r tending to infinity, hence also for any admissible integer-n subsequence. Set

W_r(x,y)=(xy)^(−1/2)(1−log(xy)/(2r))^r

for x,y≥1 and log(xy)<2r, and set W_r=0 otherwise. Let J_r be the positive integers j<exp(3r/4). These are precisely the indices whose stationary argument r−log j exceeds r/4. Define

M_r=Σ_(j,k∈J_r) W_r(j,k),
T_r(a)=Σ_(j,k∈J_r) W_r(j,k) exp(ia log(k/j)).

**Conclusion.** The absolute coefficient mass satisfies M_r=4r+o(r), and |T_r(a)|≤M_r for every real a. For sufficiently large r, the real symmetric matrix (W_r(j,k)) indexed by J_r is not positive semidefinite: its principal minor on {1,2} is strictly negative. Thus these exact weights neither have uniformly bounded total mass nor admit a Gram representation giving nonnegativity for every coefficient vector. This does not assert T_r(a)<0 for any a, and does not evaluate the endpoint theta integral.

**Proof.** The exact-weight identification is L288's formula W_jk=(jk)^(−1/2)(1−b/r)^(2n), b=log(jk)/2, with 2n=r. The interior index condition follows from its stationary coordinates, or directly from the argument r−log j.

For the mass calculation define, for 0≤L<2r,

Q_r(L)=exp(L/2)(1−L/(2r))^r,

and extend Q_r by zero for L≥2r. The elementary inequality log(1−t)≤−t−t²/2 for 0≤t<1 follows by differentiation, starting from equality at zero. Therefore

0≤Q_r(L)≤exp(−L²/(8r)).                         (1)

The full continuous mass, after x=exp(u), y=exp(v), is

A_r=∫₁^∞∫₁^∞ W_r(x,y) dx dy
   =∫₀^(2r) L Q_r(L) dL.

For each fixed z≥0, Taylor expansion at zero gives

log Q_r(sqrt(r)z)=−z²/8+O_z(r^(−1/2)).

After scaling L=sqrt(r)z, inequality (1) dominates the integrand A_r/r by the integrable function z exp(−z²/8). Dominated convergence proves

A_r/r→∫₀^∞ z exp(−z²/8) dz=4.                 (2)

Here and below extending by zero makes the moving upper limit harmless.

The function W_r decreases in each coordinate: in the positive region its logarithmic derivative with respect to log x is

−1/2−1/[2(1−log(xy)/(2r))]<0,

and the function approaches zero at its cutoff. The one-dimensional integral comparison for nonnegative decreasing functions, applied twice, therefore yields

A_r≤Σ_(j,k≥1) W_r(j,k)
   ≤A_r+2∫₁^∞ W_r(x,1) dx+W_r(1,1).

The edge integral equals ∫₀^(2r) Q_r(L)dL≤sqrt(2πr) by (1), while W_r(1,1)=1. In particular the full discrete mass is 4r+o(r).

To verify that the interior restriction has the same leading mass, let N be the largest integer strictly less than exp(3r/4). Monotonicity on the unit squares [j,j+1]×[k,k+1] gives

M_r≥∫₁^(N+1)∫₁^(N+1) W_r(x,y) dx dy.

The part omitted from A_r lies where u or v exceeds B=log(N+1)≥3r/4, and therefore u+v≥B. Its mass is at most

∫_B^∞ L exp(−L²/(8r)) dL
 =4r exp(−B²/(8r))≤4r exp(−9r/128).

Consequently A_r−4r exp(−9r/128)≤M_r≤A_r+2sqrt(2πr)+1. Equation (2) proves M_r=4r+o(r). The triangle inequality proves the asserted bound on T_r, and symmetry shows that T_r is real, but gives no sign.

For the matrix test put t=log(2)/(2r). When r is sufficiently large, both indices belong to J_r and 0<2t<1. The entries satisfy

W_r(1,1)=1,
W_r(1,2)=2^(−1/2)(1−t)^r,
W_r(2,2)=2^(−1)(1−2t)^r.

Thus their determinant is

(1/2)[(1−2t)^r−(1−t)^(2r)]<0,

since 1−2t<(1−t)² and r>0. More explicitly the real coefficient vector (−W_r(1,2),1), extended by zero, has quadratic form equal to this negative determinant. A Gram matrix would have a nonnegative quadratic form for every vector, so no such representation exists. This vector is not asserted to have the special unit-modulus coordinates exp(ia log j); the test does not establish negativity of T_r. ∎

At the normalization exp(Φ_*)/a used by L288, a hypothetical uniform per-pair remainder bounded by ε_r W_r(j,k) would sum to at most (4r+o(r))ε_r. Hence ε_r=o(1/r) suffices for an additive o(1) error for this interior family. Fixed-pair little-o estimates do not supply that bound. Even an additive o(1) error would still need a positive lower bound for T_r(a), or an error smaller than a positive varying lower bound, plus endpoint estimates for all omitted regions. Nothing here extends L296's global sign range.

**Mathlib.** Full statement: not checked. Supporting dominated convergence, monotone sum-integral comparison, and positive-semidefinite principal-minor facts: not checked. No library match is claimed. The exact stationary weights are supplied by L288; all mass estimates and the explicit negative quadratic form are proved here.
