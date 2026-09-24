# Lemma 327: growing-order balanced AFE and the surviving below-five ratio form

**Hypotheses.** Use L326's paired sequence

h=39/8, r=8n/3, p=2n=3r/4,
a=sqrt(4π²exp(4r)−h²), E_r=(1+r)²exp(−r/200),

with integer n tending to infinity, and its finite real sum

S_r(a)=Σ_(jk<exp(2r)) (jk)^(−1/2)
                  (1−log(jk)/(2r))^p exp(ia log(k/j)).

Set q=a/(2π), X=sqrt(q), L=log X, N=floor(X), and λ_j=L−log j for 1≤j≤N. Then L<r, r−L=O(exp(−4r)), and λ_j≥0. Define

χ(s)=2(2π)^(s−1)sin(πs/2)Γ(1−s), χ₀=χ(1/2+ia),
F_a(z)=ζ(1/2+z+ia)ζ(1/2+z−ia),
𝒞_r=[p!/(2(2r)^p)] [z^p]{q^z F_a(z)},
γ=(3/4)log 2−1/2>1/54.

The coefficient is taken at z=0, holding a,r,N fixed. The Hardy–Littlewood approximate functional equation and complex Stirling formula in the foundations are unconditional standard inputs. No zero-free hypothesis in Re s<1 is made.

**Conclusion.** With the actual phases retained, put

K_jk=(jk)^(−1/2)((λ_j+λ_k)/(2r))^p,
B_r=Σ_(j,k≤N) K_jk exp(ia log(k/j)),
P_r=Re[conjugate(χ₀) Σ_(j,k≤N) (jk)^(−1/2)
          ((log k−log j)/(2r))^p exp(−ia log(jk))].

Uniformly along the displayed sequence, including every cutoff transition,

𝒞_r=B_r+P_r+O(sqrt(r)exp(−3r/4)),                       (1)
|P_r|≤C exp(−γr),                                      (2)
S_r(a)=B_r+O((1+r)exp(−γr)+exp(−3r)).                  (3)

In particular 𝒞_r=S_r(a)+O((1+r)exp(−γr)). All these errors are o(E_r). Replacing q^z by exp(2rz) in 𝒞_r changes it by at most O(sqrt(r)exp(−15r/4)).

The surviving ratio matrix K is not positive semidefinite. Its principal determinant on {1,2} is

det K_{1,2}=−d/r+O(r^(−2)),
d=3(log 2)²·2^(−3/4)/32>0.                            (4)

For all sufficiently large r, every positive-semidefinite N-by-N matrix G therefore satisfies

‖G−K‖_op≥d/(4r).                                      (5)

This is much larger than E_r. It excludes a Gram-matrix replacement accurate to o(E_r) in operator norm, not a phase-specific identity or estimate. The actual vector with entries exp(ia log j) is not the vector witnessing (4). Neither B_r nor S_r(a) is proved positive or negative. Thus the balanced expansion supplies no positive margin for L326: after its controlled product terms and errors are removed, its main term is the same unsigned arithmetic sum, truncated with error o(E_r).

**Proof.** We first justify the growing-order coefficient estimate on a fixed disk; fixed-order derivative constants are not used. Let ρ=3/8 and |z|≤ρ. Write s=1/2+ia+z=σ+it, so σ lies in [1/8,7/8] and |t−a|≤ρ. In the Hardy–Littlewood approximate functional equation take x=X fixed and y=t/(2πX). Its named source is Titchmarsh–Heath-Brown, *The Theory of the Riemann Zeta-function*, second edition (1986), [Theorem 4.15 and equation (4.12.4), pp. 79, 81–84](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=44). It gives the two errors O(X^(−σ)) and O(t^(1/2−σ)y^(σ−1)), uniformly on this fixed closed strip.

Multiplication by q^(z/2) makes both errors O(X^(−1/2)): if u=Re z then |q^(z/2)|=X^u, σ=1/2+u, and t is comparable to X² while y is comparable to X. All comparison constants are uniform for |u|≤ρ. Also |y−X|≤ρ/(2πX)<1. Replacing the second cutoff by N changes at most one term, even if X is an integer.

Here is the needed analytic gamma estimate, including the modulus of that endpoint term. Uniformly on the fixed disk,

χ(1/2+ia+z)q^z=χ₀(1+O(1/a)), |χ₀|=1.                (6)

The modulus identity follows from the symmetric multiplier
χ(s)=π^(s−1/2)Γ((1−s)/2)/Γ(s/2) at s=1/2+ia; the two gamma factors there are conjugates. This is the usual multiplier in the [Riemann functional equation, DLMF 25.4.2–25.4.3](https://dlmf.nist.gov/25.4). To verify the uniform error in (6), take a local analytic logarithm of the nonvanishing multiplier on a slightly larger fixed disk. Its logarithmic derivative is

χ'(s)/χ(s)=log(2π)+(π/2)cot(πs/2)−ψ(1−s).

The cotangent is −i+O(exp(−πa)), and ψ(1−s)=log a−iπ/2+O(1/a), uniformly there. The latter follows either from the digamma asymptotic or by differentiating logarithmic complex Stirling on disks of radius comparable to a within a closed sector avoiding the negative real axis. The analytic remainder and Cauchy's estimate justify that differentiation; see [DLMF 5.11.1–5.11.2](https://dlmf.nist.gov/5.11#i) and the [complex remainder bounds](https://dlmf.nist.gov/5.11#ii). Thus χ'/χ=−log q+O(1/a); integrate along the segment from 0 to z and exponentiate to obtain (6). No differentiated real big-O is used.

For an endpoint m comparable to X, (6) gives

|q^(z/2)χ(s)m^(s−1)|≤C X^u X^(−2u)X^(−1/2+u)
                      =C X^(−1/2).

Consequently the cutoff replacement is within the same error. Introduce the finite entire functions

U(z)=Σ_(j≤N) j^(−1/2−ia)exp(λ_j z),
U*(z)=Σ_(j≤N) j^(−1/2+ia)exp(λ_j z).

The star here conjugates coefficients, so U*(z)=conjugate(U(conjugate(z))); it does not denote pointwise conjugation at complex z. Since λ_j≥0, for either choice of sign and for either coefficient conjugation,

|U(±z)|, |U*(±z)|
 ≤X^ρ Σ_(j≤N)j^(−1/2−ρ)≤C X^(1/2).                    (7)

The last bound follows by integral comparison and ρ<1/2. Substituting (6) in the normalized equation adds O(X^(1/2)/a)=O(X^(−3/2)), smaller than its existing error. Thus, as identities of analytic functions with uniformly bounded errors on the disk,

q^(z/2)ζ(1/2+ia+z)=U(z)+χ₀U*(−z)+O(X^(−1/2)),
q^(z/2)ζ(1/2−ia+z)=U*(z)+conjugate(χ₀)U(−z)+O(X^(−1/2)). (8)

The second line follows by conjugating the first at conjugate(z). Although the auxiliary cutoff y in the pointwise theorem moves, the errors in (8) are analytic differences of fixed-cutoff functions. Bound (7) shows that multiplying (8) incurs a uniformly O(1) analytic product error.

Cauchy's coefficient estimate bounds its contribution to 𝒞_r by

C [p!/(2r)^p]ρ^(−p)=C p!/p^p
                    =O(sqrt(r)exp(−3r/4)),             (9)

because 2rρ=p and the ordinary factorial Stirling formula applies. This estimate is uniform as the order grows; it does not use constants indexed by a fixed derivative order.

The product of the two main expressions in (8) is

U(z)U*(z)+U(−z)U*(−z)
 +conjugate(χ₀)U(z)U(−z)+χ₀U*(z)U*(−z).              (10)

The order p is even. The first two terms therefore have the same order-p coefficient; the last two coefficients are conjugates. Using [z^p]exp(vz)=v^p/p!, including at v=0, shows that their normalized contributions are exactly B_r and P_r, with the factors in (1). In particular all product and ratio collisions have been retained as ordered finite sums. Equations (9)–(10) prove (1). Bound (7) and (8) also give |q^zF_a(z)|≤C X on the disk. Since 2r−log q=O(exp(−4r)), replacing q^z by exp(2rz) has disk error O(exp(−3r)). Applying the same coefficient estimate (9) proves the stated O(sqrt(r)exp(−15r/4)) bound.

We next bound P_r without dropping a potentially large growing-order factor. Put α=p/L, so 3/4≤α≤1 for large r. For 1≤j<k≤N let t=log(k/j)∈(0,L]. The elementary inequality log(t/L)≤t/L−1 gives

(t/(2r))^p≤(L/(2r))^p exp(−α(L−t))
             =(L/(2r))^p X^(−α) k^α j^(−α).          (11)

The diagonal is zero, and p is even. By symmetry, (11) bounds the total absolute product coefficient mass by

2(L/(2r))^p X^(−α)
 ·Σ_(j≤N)j^(−1/2−α) Σ_(k≤N)k^(α−1/2)
 ≤C(L/(2r))^p X^(1/2)
 ≤C 2^(−p)exp(r/2)=C exp(−γr).                        (12)

Here the first sum is at most ζ(5/4), and integral comparison bounds the second by C X^(α+1/2), uniformly for α∈[3/4,1]. The last inequality uses L<r. Since |χ₀|=1, this proves (2), with no assumption on the product phases.

For (3), first truncate the original S_r to j,k≤N. Let W_r be its nonnegative coefficient function on real x,y≥1, extended by zero at and beyond xy=exp(2r). This function decreases in each coordinate, since its logarithmic derivative in log x on the positive support is −1/2−p/(2r−log(xy))<0. With B=log N=r+O(exp(−r)), monotone sum-integral comparison therefore bounds the absolute omitted mass by

2∫_N^∞ [W_r(x,1)+∫_1^∞ W_r(x,y)dy]dx
 ≤2∫_B^(2r)(1+t)Q_r(t)dt,
Q_r(t)=exp(t/2)(1−t/(2r))^p.                          (13)

This comparison covers integer cutoffs and does not require any phase cancellation. On t≥B and t<2r, for all sufficiently large r,

(log Q_r)'(t)=1/2−p/(2r−t)≤−1/8,
log Q_r(B)=−γr+O(exp(−r)).                            (14)

The first follows from B/r→1; the second from the mean value theorem near t=r and B−r=O(exp(−r)). Integrating (14) in (13) gives an omitted mass O((1+r)exp(−γr)). All product-cutoff boundary weights are zero by definition.

On the retained square, the two bases

b=1−log(jk)/(2r), b'=(2L−log(jk))/(2r)

satisfy 0≤b'≤b≤1 and b−b'=(r−L)/r. The mean value theorem for the integer power gives |b^p−(b')^p|≤p(r−L)/r=O(exp(−4r)). Since (Σ_(j≤N)j^(−1/2))²≤4N≤4exp(r), the total change from these weights to K is O(exp(−3r)). This proves (3). Notice that the unsigned sum retained by the balanced equation is precisely the retained part of S_r, rather than a new arithmetic lower bound.

For comparison of the errors, integration of the geometric series gives

log 2=2Σ_(m≥0)(1/3)^(2m+1)/(2m+1)
       >2(1/3+1/81)=56/81.

Hence γ>1/54>1/200. Equations (1)–(3), (9), and their polynomial factors imply that every displayed approximation error is o(E_r).

Finally set t=log 2/(2L) and m₀=(L/r)^p=1+O(exp(−4r)). For all sufficiently large r, 0<2t<1 and the principal matrix has entries

K_11=m₀,
K_12=2^(−1/2)m₀(1−t)^p,
K_22=2^(−1)m₀(1−2t)^p.

Thus its determinant is

(m₀²/2)[(1−2t)^p−(1−t)^(2p)]<0,                      (15)

since 1−2t<(1−t)². Taylor's theorem at t=0 gives

p[log(1−2t)−2log(1−t)]
 =−pt²+O(pt³)=−3(log 2)²/(16r)+O(r^(−2)),
(1−t)^(2p)=2^(−3/4)(1+O(1/r)).                       (16)

Substitution in (15) proves (4). Let v have first coordinates (−K_12/K_11,1) and all other coordinates zero. Its squared norm is at most 3/2, hence at most 2, and

v*Kv=det K_{1,2}/K_11=−d/r+O(r^(−2)).

For a positive-semidefinite G, v*Gv≥0. For sufficiently large r this implies v*(G−K)v≥d/(2r); division by ‖v‖²≤2 proves (5). Since (1/r)/E_r→∞, the matrix error is incompatible with an o(E_r) operator-norm replacement. This test vector has neither the prescribed unit amplitudes nor the actual logarithmic phases, so the conclusion cannot be used to sign B_r at a_n. ∎

The achieved analytic errors are smaller than the sufficient arithmetic margin scale in L326. What remains unproved is B_r(a_n)/E_r→+∞, or another lower bound leaving a positive surplus over L326's sector error. The balanced equation and its even coefficient do not supply this inequality. The principal minor only excludes the stated phase-uniform Gram replacement; arithmetic estimates exploiting the actual phases remain possible. L307 is the endpoint self-reproduction precedent, while L297 and L318 are related algebraic obstructions; their conclusions are not used outside their hypotheses. No Laguerre sign, zero-exclusion range or RH-candidate status changes.

The command `python3 scripts/laguerre/check_below_five_balanced_afe.py` independently expands finite exponential jets and checks their normalized even coefficients against (10)'s two ordered pair sums using exact rational complex arithmetic. It also checks the exact order/radius relation and the rational decay-rate comparison. These finite algebra checks do not certify a zeta value or replace the analytic estimates above.

**Mathlib.** Full statement: not checked. Supporting approximate functional equations, analytic gamma estimates, Cauchy coefficient bounds, finite-sum identities, monotone integral comparison and positive-semidefinite matrix facts: not checked for Mathlib coverage; no full or supporting library match is claimed. The precise named external supporting inputs are Titchmarsh–Heath-Brown [Theorem 4.15 and (4.12.4)](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=44), the [Riemann functional equation](https://dlmf.nist.gov/25.4), and [complex Stirling with its sector remainder bounds](https://dlmf.nist.gov/5.11). These sources were checked for the hypotheses used here; none matches this full growing-order statement. The [Mathlib reference portal](https://leanprover-community.github.io/mathlib4_docs/) is retained without a coverage claim. L326 supplies the paired sum and the required sufficient margin; the new coefficient estimates, truncation, product bound and matrix obstruction are proved above.
