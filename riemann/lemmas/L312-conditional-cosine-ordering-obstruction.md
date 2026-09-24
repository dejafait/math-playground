# Lemma 312: failure of actual-theta conditional cosine ordering

**Hypotheses.** Let k(u)=K(|u|) be the positive smooth even actual-theta kernel of L019 and L048. For real s,a put

q_s(t)=k(s+t)k(s−t),
C_s(a)=∫_R q_s(t)cos(2at)dt / ∫_R q_s(t)dt.

Assume L037's explicit directed-rounding and exponential arithmetic contracts for the finite calculation below. Use the associated kernels A_n and coefficients D_n of L267 when discussing normalized levels.

**Conclusion.** The derivative in s exists continuously, and

−23/10^6 < ∂_s C_s(16)|_(s=1/5) < −21/10^6 < 0.

Consequently C_s(a) is not nondecreasing in s>0 for every 10≤|a|≤20. This rejects conditional cosine ordering as a sufficient transfer mechanism. It neither supplies a negative Laguerre coefficient nor disproves ordering of the normalized levels after averaging over s. It does not change the established compact sign interval or resolve RH.

**Proof.** Write W=−log k and B_s(t)=W'(s+t)+W'(s−t). Since ∂_s q_s=−B_s q_s, differentiation of the normalized integral gives

∂_s C_s(a)=−Cov_(q_s/∫q_s)(cos(2at),B_s(t)).             (1)

The explicit derivative bounds proved below dominate q_s and its s derivative locally uniformly in s by an integrable function of t. They justify differentiation by dominated convergence. Smoothness and evenness come from L048; the same domination gives continuity. No sign of this oscillatory covariance follows from ordering B_s in |t|.

We certify (1) directly, without dividing by small pointwise values of k. All four integrands are even in t. For the rest of the finite calculation fix s=1/5 and a=16 and use half-line integrals

Z=∫_0^∞ q_s(t)dt,            N=∫_0^∞ q_s(t)cos(32t)dt,
Z_s=∫_0^∞ ∂_s q_s(t)dt,     N_s=∫_0^∞ ∂_s q_s(t)cos(32t)dt.

Then

C_s(16)=N/Z,       ∂_s C_s(16)=(N_s Z−N Z_s)/Z².         (2)

There is no missing factor two in (2): the same factor cancels in the normalized whole-line integral.

For u≥0 put v_m=πm²exp(2u). The exact summands and their u derivatives are

K_m(u)=exp(u/2)(8v_m²−12v_m)exp(−v_m),
K_m'(u)=exp(u/2)(−16v_m³+60v_m²−30v_m)exp(−v_m).         (3)

Every fixed derivative series converges locally uniformly, by its polynomial times Gaussian bound in m. Since 3<π<4 and v_m≥3,

0<K_m(u)≤128m⁴exp(9u/2−3m²exp(2u)),
|K_m'(u)|≤2560m⁶exp(13u/2−3m²exp(2u)).                  (4)

For the second inequality, 16v³+60v²+30v<40v³ when v≥3. The successive majorant ratios in (4) are at most 16exp(−9) and 64exp(−9), respectively, both below 1/2. The elementary inequality exp(3)>20 follows from its positive series through degree eight. Geometric summation therefore yields

K(u)≤256exp(9u/2−3exp(2u))<16,
|K'(u)|≤5120exp(13u/2−3exp(2u))<5120.                   (5)

The first exponent decreases from −3. For the second, exp(2u)≥1+2u+2u² implies 3exp(2u)−13u/2≥3−u/2+6u²>0. The same bounds apply to the finite head K_4=Σ_(m=1)^4 K_m and the absolute sum of its derivatives. Evenness extends (5) to k and k', with |u| in the exponents. These superexponential bounds provide the domination used for (1).

Starting the geometric sums at m=5 and observing that 9u/2−75exp(2u) and 13u/2−75exp(2u) decrease for u≥0 gives the uniform truncation bounds

|K−K_4|≤ε_0:=160000exp(−75),
|K'−K_4'|≤ε_1:=80000000exp(−75).                        (6)

Let q_4 be the product with k replaced by K_4(|u|), and let d_4 be its s derivative on each side of t=s. The possible finite-head derivative jump at t=s is handled by splitting the quadrature there; its value at that single point does not affect any integral. By (5)–(6), off that point,

|q_s−q_4|≤32ε_0,
|∂_s q_s−d_4|≤32ε_1+10240ε_0.                          (7)

Thus on [0,2] the integrated errors for Z,N are at most 64ε_0, and those for Z_s,N_s are at most 64ε_1+20480ε_0. Multiplication by cosine does not increase these bounds. These are bounds for the infinite theta tail, not an assumption that its derivative vanishes at the reflection point.

For the remaining spatial tail t≥2, both t+s and t−s are positive. Using exp(2s)+exp(−2s)≥2 in (5) yields

q_s(t)≤65536exp(9t−6exp(2t)),
|∂_s q_s(t)|≤2621440exp(11t+2/5−6exp(2t)).              (8)

Put t=2+w. Since exp(4)>50 and exp(2w)≥1+2w,

∫_2^∞ q_s(t)dt ≤ 65536exp(−282)/591,
∫_2^∞ |∂_s q_s(t)|dt ≤ 2621440exp(−277)/589.            (9)

The second bound enlarges exp(−277.6) to exp(−277). For the elementary constant, exp(3)>20 and exp(1)>5/2 imply exp(4)>50. Again (9) bounds the cosine-weighted tails as well.

Here is the finite quadrature in full. Partition each of [0,1/5] and [1/5,2] into 128 equal closed panels. On the first interval use K_4(s+t), K_4(s−t); on the second use K_4(s+t), K_4(t−s). The s derivative of the second factor has sign + on the first piece and − on the second. Taylor coefficients always differentiate with respect to t, whose affine slopes are respectively −1 and +1 for that factor. Formula (3) separately supplies the s derivative; these two derivatives are not identified.

For each of q_4, q_4 cos(32t), d_4 and d_4 cos(32t), evaluate normalized Taylor coefficients through order eight. Products use convolution and exponentials use the recurrence in L036. At each panel midpoint c, integrate the coefficients of orders 0,2,4,6 with weights 2h^(j+1)/(j+1), where h is the half-width. Evaluating the same derivative expressions on the entire panel bounds |f^(8)|/8! by an interval magnitude B. Enlarge the midpoint result by [−2Bh^9/9,2Bh^9/9], exactly as proved in L036. Both finite formulas are smooth on their own closed piece, so no Taylor remainder crosses the reflection point.

Trigonometric values require no new transcendental arithmetic contract. For x=32t, choose an integer m and reduce to r=x−2mπ using L037's rational enclosure of π. The calculation checks |r|≤4 on every panel. Degree-49 Taylor polynomials at zero enclose sin r and cos r after adding the symmetric error |r|^50/50!, by Taylor's theorem and the derivative bound one. Cosine's degree-49 polynomial has degree 48 since its odd coefficients vanish. The jth normalized derivative of cos(32t) is 32^j/j! times the cycle cos, −sin, −cos, sin. These enclosures cover all points of each panel, including possible crossings of a preferred period boundary: the chosen integer m is held fixed on that panel and the periodic identity remains exact.

All interval operations obey L037. Sum the panels and add the symmetric bounds (7) and (9). The reproducing command is

`python3 scripts/laguerre/certify_conditional_cosine.py > scripts/laguerre/conditional-cosine-certificate.json`

The certificate stores π, the tail bounds, the accumulated Taylor remainder bounds and the four half-line integral enclosures. For readability, the full endpoints are contained strictly in the following larger exact rational intervals (each terminating decimal is an exact rational):

| Integral | Lower bound | Upper bound |
| --- | --- | --- |
| Z | 0.27866775 | 0.27866776 |
| N | −0.000000120412 | −0.000000120335 |
| Z_s | −2.354742 | −2.354741 |
| N_s | −0.0000051334 | −0.0000051316 |

In particular Z>0. Exact rational interval operations in (2), even on these larger intervals, place the derivative strictly between −23/10^6 and −21/10^6. The narrower interval obtained from the full certificate endpoints is approximately [−0.000022072148,−0.000022063862]; the rational comparisons, not this rounded display, prove the asserted sign. A differentiable nondecreasing function cannot have a negative derivative at an interior point. Continuity even gives a neighborhood of s=1/5 on which C_s(16) decreases.

Finally, to specify the failure scope, define

R_n(a)=∫_R A_n(t)cos(2at)dt / ∫_R A_n(t)dt.

By Fubini and L267, R_n is the generalized Laguerre coefficient divided by its positive mass factor. Let μ_n be the probability measure on s>0 proportional to s^(2n)Z(s)ds, with Z(s) still the half-line conditional mass. Evenness in s and t makes all factors of two cancel. Then

R_n(a)=E_(μ_n)[C_s(a)],
R_(n+1)(a)−R_n(a)=Cov_(μ_n)(s²,C_s(a))/E_(μ_n)[s²].     (10)

The integrals and polynomial weights are absolutely integrable by (5), and |C_s(a)|≤1. Conditional nondecrease would make the covariance in (10) nonnegative by the two-copy covariance identity. Its failure at one s does not determine the averaged covariance. L309's variance ordering, L311's compact all-level signs and any possible weaker averaged ordering therefore remain distinct assertions. ∎

The required threshold for this proposed transfer was ∂_s C_s(a)≥0 for every s>0 throughout the tested height band. The achieved strict negative enclosure violates that threshold for the actual theta kernel under the stated arithmetic contracts. It supplies no extension of the known sign range, no endpoint arithmetic margin and no off-line zero.

**Mathlib.** Full statement: not checked. Supporting covariance differentiation, Taylor quadrature, trigonometric remainder bounds, interval arithmetic and the averaging identity: not checked for Mathlib coverage. No matching library theorem is asserted. The analytic estimates and identities are proved above. L037's [official Decimal reference](https://docs.python.org/3/library/decimal.html) supports the inherited arithmetic contract, not the full theorem or an independently verified implementation.
