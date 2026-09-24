# Lemma 314: finite witness signs and exclusion through height twenty

**Hypotheses.** Use the actual-theta completion Ξ of L018–L019 and the coefficients and positive associated kernels of L267. For real a write

Ξ(a+iy)Ξ(a−iy)=Σ_(n≥0)D_n(Ξ;a)y^(2n),
R_n(a)=D_n(Ξ;a)/D_n(Ξ;0).

Assume L037's explicit arithmetic contracts for the saved moment enclosures and finite certificates. These contracts do not include an independently verified implementation. Use the standard gamma reflection identity recorded in foundations.

**Conclusion.** L266's negative-witness cutoff satisfies K(a)≤16 whenever 10≤|a|≤20. On this whole band,

R_n(a)>1/10^6 for every integer 3≤n≤16.

Together with L313, this gives D_n(Ξ;a)>0 for all 1≤n≤16 on the band. Consequently Ξ has no nonreal zero with |Re z|≤20, using L311 for the inner interval. Equivalently, every nontrivial zeta zero of height at most twenty has real part 1/2, under the stated contracts. This does not prove all-level Laguerre positivity beyond height ten or any assertion at unbounded heights, and is not a proof of RH.

**Proof.** First obtain a uniform finite cutoff. L266 gives

M=Ξ(3i)²,
A(a)=((a²+4)(a²+1)/(4π²ζ(2)²))|Γ(1−ia/2)|²,
K(a)=ceil(log(8M/[3A(a)])/log 4).                         (1)

By L018's functional equation and completed-zeta formula,

Ξ(3i)=ξ(7/2)=(35/8)π^(−7/4)Γ(7/4)ζ(7/2)>0.

Hölder's inequality applied to

Γ(7/4)=∫_0^∞(exp(−t))^(1/4)(t exp(−t))^(3/4)dt

gives Γ(7/4)≤1, since both underlying integrals equal one. The decreasing-series integral bound gives ζ(7/2)<1+∫_1^∞x^(−7/2)dx=7/5. L037's rational π enclosure gives π>31/10, and (31/10)^7>7^4. Thus π^(7/4)>7 and

0<Ξ(3i)<7/8, hence M<1.                                (2)

Euler's reflection formula and gamma recurrence give

|Γ(1−ia/2)|²=(πa/2)/sinh(πa/2) for a>0.                 (3)

This is also the direct consequence of the standard modulus identity in [NIST DLMF 5.4.3](https://dlmf.nist.gov/5.4.E3). Substituting (3) into A and differentiating its positive logarithm gives, for 10≤a≤20,

(log A)'=2a/(a²+4)+2a/(a²+1)+1/a−(π/2)coth(πa/2)
         <5/a−π/2<0.

Therefore A(a)≥A(20). Since ζ(2)<2, π<4 and 10π<32, and sinh x<exp(x)/2 for x>0,

A(20)>[5·404·401/(πζ(2)²)]exp(−10π)
      >[5·404·401/16]exp(−32)>50000exp(−32).             (4)

The π inequalities follow from the same rational enclosure. The following entirely rational estimates suffice for the remaining exponential bound:

e<Σ_(j=0)^6 1/j!+8/(7·7!)=31967/11760<87/32,
(87/32)^32<8·10^13.

The tail estimate uses a geometric majorant with successive ratio 1/8 starting at 1/7!. The last inequality is an integer comparison after clearing denominators. Equations (2)–(4) yield

8M/(3A(a))<8·(8·10^13)/(3·50000)
            =12800000000/3<4294967296=4^16.              (5)

Since M and A are positive and A is even, (1) and (5) prove K(a)≤16 throughout the claimed band. This conservative upper bound is sufficient; equality or a sharp cutoff is unnecessary.

We next prove the remaining fourteen signs. Put

m_j=∫_0^∞u^jK(u)du,
f(a)=∫_0^∞K(u)cos(au)du=Ξ(a).

L019's superexponential decay justifies every derivative under this integral and gives

f^(j)(a)=∫_0^∞u^jK(u)cos(au+jπ/2)du,
|f^(j)(a)|≤m_j.                                         (6)

Multiplication of the entire Taylor series for f(a+iy) and f(a−iy) gives exactly

(2n)!D_n(Ξ;a)=(-1)^nΣ_(j=0)^(2n)(-1)^j binom(2n,j)
                                      f^(j)(a)f^(2n−j)(a). (7)

Indeed i^j(−i)^(2n−j)=(-1)^(n+j). At a=0, odd derivatives vanish and f^(2j)(0)=(-1)^j m_(2j), so

B_n:=(2n)!D_n(Ξ;0)
    =Σ_(j=0,2,…,2n)binom(2n,j)m_jm_(2n−j)>0.             (8)

Thus division of (7) by (8) is the normalized coefficient R_n, with no missing factorial. L267 also identifies it with the normalized associated-kernel cosine integral.

Enclose d_j=f^(j)(15) for 0≤j≤64. For K_4=Σ_(m=1)^4 K_m, L310's tail argument gives

∫_0^2u^j(K−K_4)(u)du+∫_2^∞u^jK(u)du≤E,
E=(512/461)2^130exp(−141)+1280exp(−75)+180exp(−520).      (9)

Although its original moment list was even, that proof uses only u^j≤1 on [0,1] and u^j≤u^130 on [1,∞); hence (9) holds for all integer 0≤j≤130, including all odd powers used here. Positivity of the omitted theta terms and |cos|≤1 give a signed error interval [−E,E] for each derivative integral. No sign of an oscillatory tail is assumed.

For the finite part, integrate

g_j(u)=u^jK_4(u)cos(15u+jπ/2), 0≤u≤2.

Use 256 equal panels of half-width h=1/256 and centers c_l=(2l+1)/256, 0≤l≤255. L036 bounds the panel integral by

2Σ_(q=0)^3[g_j^(2q)(c_l)/(2q)!]h^(2q+1)/(2q+1)
            +[−2C_(j,l)h^9/9,2C_(j,l)h^9/9],             (10)

where C_(j,l) encloses |g_j^(8)|/8! on the whole panel. The normalized Taylor coefficients of u^j are binom(j,q)u^(j−q), zero for q>j. The finite theta kernel uses L036's product and exponential recurrences; the normalized trig coefficient is 15^q cos(15u+(j+q)π/2)/q!. Use L312's rational degree-49 trigonometric polynomials after reduction by an integer multiple of 2π, with absolute reduced argument at most four and symmetric remainder |x|^50/50!. This supplies enclosing sine and cosine values under L037 without adding a trigonometric arithmetic contract. Every reduction uses a fixed integer for that interval and checks the resulting radius.

Summing (10) and adding (9) gives intervals I_j containing d_j. The largest accumulated quadrature error upper endpoint is less than 7/10^15; E<9/10^23. The full certificate retains each interval, not merely these abbreviated common bounds.

To control all heights in the band, the inequality 2u^65≤u^64+u^66 gives

m_65≤B:=(m_64+m_66)/2.

For 0≤j≤32 and |δ|≤5, the real Taylor theorem and (6) give

f^(j)(15+δ)=P_j(δ)+e_j(δ),
P_j(δ)=Σ_(l=0)^(64−j)d_(j+l)δ^l/l!,
|e_j(δ)|≤B·5^(65−j)/(65−j)!.                            (11)

Every remainder uses the same derivative f^(65); its moment bound uses L310's saved enclosures of m_64 and m_66. The largest remainder bound in (11), at j=32, is less than 8/10^21.

Let P(δ)=Σ_(k=0)^64 d_kδ^k/k!, so P_j=P^(j). Cover [10,20] by the 512 closed intervals

J_l=[10+10l/512,10+10(l+1)/512], 0≤l≤511.

If b_l is the midpoint of J_l minus 15, write δ=b_l+x with |x|≤5/512. First translate the base polynomial by the exact identity

P(b_l+x)=Σ_(q=0)^64 T_(l,q)x^q,
T_(l,q)=Σ_(k=q)^64 binom(k,q)(d_k/k!)b_l^(k−q).           (12)

Differentiating this finite polynomial gives

P_j(b_l+x)=Σ_(q=0)^(64−j) [(j+q)!/q!]T_(l,j+q)x^q.     (13)

Interval evaluation of (12), followed by interval Horner evaluation of (13) on [−5/512,5/512] and the remainder (11), encloses every derivative f^(j)(a) on J_l. Translating before interval evaluation retains useful cancellation but is an exact polynomial operation. Dependence between enclosed coefficients or derivatives cannot invalidate inclusion; treating them as independent only enlarges the boxes.

Substitute these 33 derivative boxes into the full signed sum (7), and divide by the positive interval (8) from L310's moments. The reproducing command is

`python3 scripts/laguerre/certify_finite_witness_band.py > scripts/laguerre/finite-witness-band-certificate.json`

The certificate stores the source moments' SHA-256 digest, the rational cutoff checks, all 65 derivative integrals with errors, the common tail bound, all height remainders, every mass denominator, and every height cell with its derivative and normalized-coefficient boxes. All 512·14=7168 lower endpoints exceed the exact rational target 1/10^6. The overall minimum occurs for n=3 on J_511=[5115/256,20] and begins

0.000001921201974931247154977919203625017773070700942292940203382826438575883.

This displayed decimal is the saved exact rational endpoint under the arithmetic contracts. Exact fraction comparisons establish the strict target on every cell, with excess greater than 9/10^7 over 1/10^6. The other levels' minima are stored individually. The certificate covers the entire closed band, not only the midpoints.

A separate calculation uses exact rational interval arithmetic and the paired form

(2n)!D_n=binom(2n,n)(f^(n))²
          +2Σ_(j=0)^(n−1)(-1)^(n+j)binom(2n,j)f^(j)f^(2n−j),

with exact interval squares. It verifies all 7168 final signs, the denominator enclosures, recorded minima, the source digest and complete band coverage. It also checks consistency of the first 33 center-derivative boxes with L313. Its command is

`python3 scripts/laguerre/audit_finite_witness_band.py > scripts/laguerre/finite-witness-band-audit.json`

This audit checks the final algebra separately; it does not independently verify the quadrature implementation or discharge L037's contracts. Those qualifications are retained.

Evenness of Ξ, or L267's cosine integral, makes R_n even in a, so these signs hold for negative heights as well. L313 gives the first two signs on the same band. If Ξ had a nonreal zero there, L266 would force a negative coefficient with index at most K(a)≤16, contradicting the established sixteen signs. L311 already excludes nonreal centers with |a|≤10. Combining the two closed ranges proves exclusion through twenty. L018's exact zero correspondence transfers this to the stated bounded-height zeta conclusion. ∎

The achieved normalized bound is greater than 10^(−6) for each newly required sign, compared with the actual required threshold zero. Only sixteen levels were needed because the independent witness cutoff was uniformly at most sixteen. This finite exclusion argument does not turn finitely many global levels into a generic real-zero criterion, and establishes no all-level positivity outside the earlier interval. The unbounded-height low-index gap and endpoint arithmetic margin remain open.

**Mathlib.** Full statement: not checked. Supporting gamma reflection/modulus, Hölder, differentiation under the integral, Taylor products and remainders, polynomial translation and interval arithmetic: not checked for Mathlib coverage. No full matching theorem is asserted. The direct [DLMF gamma modulus identity](https://dlmf.nist.gov/5.4.E3) and [Euler reflection formula](https://dlmf.nist.gov/5.5.E3) are checked standard analytical inputs, not Mathlib coverage or matches for this statement. L037's retained [official Decimal reference](https://docs.python.org/3/library/decimal.html) supports its arithmetic contract, not this full theorem or an independently verified implementation.
