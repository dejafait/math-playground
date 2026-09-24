# Lemma 322: the anchored Taylor tail retains the one-quarter barrier on ellipses

**Hypotheses.** Let Ξ be the actual completion, and use L320's notation

H_a(y)=Ξ(a+iy)Ξ(a−iy)=Σ_(n≥0)D_n(Ξ;a)y^(2n),
T=2+|a|,    S_(K,a)(t)=Σ_(n=0)^K D_n(Ξ;a)t^(2n).

Fix an anchor η>1/2. Thus H_a(η)≥A_η(a)>0 by L320, without any assumption on Ξ(a). All logarithms are natural. Cutoffs K are nonnegative integers; B≥0 is fixed independently of a.

For the contour assertions, fix U>η and V>0, and let Γ be the positively oriented ellipse z(θ)=U cos θ+iV sin θ. No condition V>η is imposed. Define its absolute remainder bound, for 0<t≤η, by

E_(K,a)(t)=(t^(2K+2)/(2π))∫_Γ |H_a(z)| |dz|
                                      /(|z|^(2K+1)|z²−t²|).

**Conclusion.** If 0≤c<η/2 and K≤c log T+B, then, for any fixed

max(1/2,2c)<r<η,    δ=η−r−2c log(η/r)>0,

one has uniformly over these K

|S_(K,a)(η)|/H_a(η)≤C T^(−δ),
[H_a(η)−S_(K,a)(η)]/H_a(η)=1+O(T^(−δ)).                (1)

In particular the actual signed tail is not small compared with the anchor. Any contour bound for its absolute value has normalized liminf at least one. This part also applies to contours that vary with a, provided they represent the same Taylor remainder and anchor.

On the stated ellipse the exact identity is

H_a(t)−S_(K,a)(t)
 = (t^(2K+2)/(2πi))∫_Γ H_a(z) dz/[z^(2K+1)(z²−t²)].    (2)

Moreover, put β(U,η)=(U−η)/(2log(U/η)). For every fixed 0≤c<β(U,η), there are ε,C_*>0 such that, for all sufficiently large |a| and every K≤c log T+B,

E_(K,a)(η)/H_a(η)≥C_* T^ε.                             (3)

Thus retaining pointwise growth inside an absolute elliptical remainder integral does not lower the fixed-anchor witness scheme's leading coefficient below 1/4. Indeed β(U,η)>η/2>1/4, and L320's circles already approach the infimum 1/4 over successive fixed choices. This is a barrier for the comparison that makes the omitted tail small at an exterior anchor, not for every possible negative-witness argument. No coefficient sign or zero-exclusion interval is extended.

**Proof.** The separate circle and anchor estimates in L320 give, for every fixed r>1/2 and η>1/2,

max_(|z|=r)|H_a(z)|≤C_r T^(7/2+r)exp(−π|a|/2),
H_a(η)≥A_η(a)≥c_η T^(7/2+η)exp(−π|a|/2).              (4)

These are equations (6) and (7) of its proof. Their proofs impose no ordering between r and η: the strip estimate only needs r>1/2, and the anchor bound only needs η>1/2. Here r<η; we are not applying L320's witness conclusion outside its stated R>η hypothesis. Dividing (4) yields the smaller-circle estimate

max_(|z|=r)|H_a(z)|/H_a(η)≤C T^(r−η).                  (5)

Cauchy's coefficient estimate and the finite geometric sum, with q=(η/r)²>1, give

|S_(K,a)(η)|/H_a(η)
 ≤ C T^(r−η)Σ_(n=0)^K q^n
 ≤ [C/(1−q^(−1))] T^(r−η)q^K
 ≤ C' T^(r−η+2c log(η/r)).                            (6)

The factor q^B is absorbed into C'. The chosen r exists because both 1/2 and 2c are strictly less than η. Furthermore

δ=∫_r^η (1−2c/x)dx>0,

since r>2c. This proves both assertions in (1). No positivity of the individual coefficients is used. In particular a small signed remainder cannot be recovered by changing its integral representation: the remainder itself is (1+o(1))H_a(η).

For (2), apply the residue theorem to its integrand. The ellipse contains 0,t,−t, including when V≤t; none is on its boundary. The residues at t and −t are H_a(t)/2 each, using evenness. Expanding only in a neighborhood of zero, the residue there is

−Σ_(n=0)^K D_n(Ξ;a)t^(2n)=−S_(K,a)(t).

This local residue calculation is valid independently of the smallest boundary modulus. It proves (2) without a geometric-series expansion on a thin ellipse. Taking absolute values proves |H_a(t)−S_(K,a)(t)|≤E_(K,a)(t). Equation (1) gives the stated liminf obstruction, even for varying contours on which the analogous identity holds.

We next prove the sharper fixed-ellipse obstruction (3). By the evenness in a inherited from L018, it suffices to let a tend to positive infinity. On a sufficiently small fixed arc about θ=0, write z=u+iv. Then u>η>1/2 and |z|>η. L018's functional equation and conjugation give

|H_a(z)|=|ξ(1/2+u+i(a−v))| |ξ(1/2+u+i(a+v))|.          (7)

Both real parts are in a fixed compact interval strictly above one, and v stays bounded. L001's absolutely convergent Dirichlet and reciprocal series give uniformly there

1/ζ(1/2+u)≤|ζ(1/2+u+it)|≤ζ(1/2+u).

The same uniform complex Stirling estimate used in L320, together with the completed-zeta formula, therefore bounds the expression in (7) above and below by positive constant multiples of

T^(7/2+u)exp(−πa/2).                                   (8)

To check the power and exponential, each factor has power t^(7/4+u/2) and exponential exp(−πt/4), with t=a±v>0 for large a. Their heights add to 2a and are both comparable to a. All real parts and shifts vary on fixed compact sets, so the constants are uniform on the arc. At the real anchor the same argument gives

H_a(η) ≍ T^(7/2+η)exp(−πa/2).

Consequently, uniformly on this arc,

|H_a(z)|/H_a(η)≥c_* T^(u−η).                           (9)

This lower estimate is on an exterior arc where the reciprocal series converges absolutely; it asserts no lower bound inside the critical strip.

After dividing the integrand defining E_(K,a)(η) by H_a(η), its remaining geometric factor is

[η²|z'(θ)|/(2π|z||z²−η²|)] · (η/|z|)^(2K).

The bracket is bounded below by a positive constant on a still smaller fixed arc: |z'(0)|=V>0 and the denominator has no zero there. Since |z|>η and K≤c log T+B, equations (9) and this factor bound the normalized integrand below by a positive constant times

T^f(θ),    f(θ)=Re z(θ)−η−2c log(|z(θ)|/η).

At the positive real tip,

f(0)=U−η−2c log(U/η)>0

precisely under c<β(U,η). Continuity supplies a fixed arc and ε>0 on which f≥ε. Integrating over that arc proves (3). This uses a positive-length arc, not the value at a single point, and retains the actual modulus of H_a rather than a potentially wasteful strip majorant. It does not imply that the signed contour integral diverges by the same factor.

Finally log(U/η)<(U−η)/η shows β(U,η)>η/2>1/4. Its infimum over U>η>1/2 is 1/4 by first taking U down to η and then η down to 1/2. Independently, (1) shows that for every fixed exterior anchor and every c≤1/4 the actual omitted tail is asymptotically the entire anchor value. Hence no valid absolute contour estimate can make that tail at most A_η(a)/2, as required by the tested version of L266's finite-sum comparison, since A_η(a)≤H_a(η). L320 supplies the opposite approximation to the infimum: for each fixed c>1/4 it chooses fixed radii and anchor and proves a witness cutoff ceil(c log T+B_c). Circles are included among ellipses. No uniform estimate as these parameters approach the boundary is being asserted. ∎

The required improvement was c<1/4. The proved obstruction is stronger at every fixed anchor: below c=η/2 the retained Taylor sum is negligible even with all its signs allowed, and on a fixed ellipse its absolute remainder bound already diverges for c<β(U,η). This stops reshaping that contour as a way to reduce the initial sign target. It does not exclude a different coefficient comparison, an a-dependent anchor, or a sign argument using additional arithmetic information. Low-index positivity at unbounded heights, the endpoint arithmetic margin and heights above forty remain unresolved. This is not a negative actual Laguerre sign, an off-line zero, or an RH candidate.

**Mathlib.** Full statement: not checked. Coverage of the Cauchy estimates, residue identity, uniform gamma estimates and asymptotic tail obstruction is not checked; no full match is claimed. L001 records the supporting reciprocal identity and summability input as present, with sources not rechecked here: [`ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeries_zeta_mul_Lseries_moebius) and [`ArithmeticFunction.LSeriesSummable_moebius_iff`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/LSeries/Dirichlet.html#ArithmeticFunction.LSeriesSummable_moebius_iff). These support the exterior arc bounds only, not the full statement. The standard complex Stirling input already stated in foundations and used in L320 is [NIST DLMF 5.11.3](https://dlmf.nist.gov/5.11.E3), with its closed-sector condition; this classical supporting reference is not a Mathlib match and was not rechecked here. The residue calculation and quantitative comparisons are proved above.
