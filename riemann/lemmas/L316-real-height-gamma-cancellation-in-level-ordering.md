# Lemma 316: real-height gamma cancellation in the first level comparison

**Hypotheses.** Let f=Ξ be the completion of L018. Use the exact analytic normalization identities from L313, with

m_j=∫_0^∞u^jK(u)du,
B_1=m_0m_2>0,        B_2=m_0m_4+3m_2²>0,        κ=B_2/B_1>0,
R_1=Q(f)/B_1,        R_2=T(f)/B_2,
Q(U)=U'²−UU'',       T(U)=UU''''−4U'U'''+3U''².

Only L313's exact identities and positivity of its denominators are used, not its finite certificate or arithmetic implementation contracts. Primes on functions of a denote real-height derivatives. Let a>0, s=1/2+ia, w=1/4+ia/2, and set

H(a)=(a²+1/4)π^(−1/4)|Γ(w)|/2,
θ(a)=Im log Γ(w)−a log(π)/2,
Z(a)=exp(iθ(a))ζ(s),       ℓ(a)=log H(a),       β(a)=ℓ(a)+iθ(a).

Use the analytic log Γ on Re w>0 that is real on the positive real axis. H is positive, and Z is the real Hardy transform; its reality is proved below. No assumption on the zeros or the sign of any Laguerre coefficient is made.

**Conclusion.** Put p=ℓ'' and q=ℓ''''. The exact real expression whose nonnegativity is required for the first adjacent comparison is

J(a):=B_2(R_2(a)−R_1(a))/H(a)²
 =T(Z)−(κ+12p)Q(Z)+(q+6p²+κp)Z².                         (1)

As a→+∞,

p=−7/(4a²)+O(a^(−3)),       q=−21/(2a⁴)+O(a^(−5)),
J=T(Z)−κQ(Z)+[21Q(Z)−(7κ/4)Z²]/a²
                    +O(a^(−3))(|Q(Z)|+Z²).               (2)

The last remainder means an absolute bound by C a^(−3)(|Q(Z)|+Z²), with a constant independent of a. It is not a relative estimate for J or its leading arithmetic form.

For an explicit completed-zeta derivative version, write ζ_j=ζ^(j)(s), where these derivatives are with respect to s, and define

C_2=ζ_0ζ_2−ζ_1²,
C_4=ζ_0ζ_4−4ζ_1ζ_3+3ζ_2².

Then

J=Re{exp(2iθ)[C_4−(κ+12β'')C_2
                  +(β''''+6(β'')²+κβ'')ζ_0²]},           (3)
β''=i/(2a)−7/(4a²)+O(a^(−3)),
β''''=i/a³−21/(2a⁴)+O(a^(−5)).                           (4)

These are products without complex conjugation, not modulus squares. In particular the large first derivative of the gamma phase contributes no separate positive leading term.

The leading form T(U)−κQ(U) is indefinite even among real analytic germs with Q(U)=1 at the point in question. The complete right side of (1), with the same H and fixed actual-theta κ, also takes both signs on such germs at every sufficiently large height. These are tests of the differential expression, not claimed realizations by actual Z or by globally normalized theta kernels. Thus gamma estimates alone supply no sign for the actual comparison. No new Laguerre sign range or RH assertion follows.

**Proof.** L018 and s(s−1)=−(a²+1/4) give

f(a)=−H(a)exp(iθ(a))ζ(s)=−H(a)Z(a).

L018 makes f real on the real axis; dividing by the positive H proves reality of Z, including at its zeros. The gamma factor is nonzero near each positive real a, so H, θ and Z have local analytic extensions. They may equivalently be obtained using the two analytic functions log Γ(1/4±iz/2), with conjugate branch choices on the real axis. Only these local extensions, not an entire extension of H, are needed.

For any analytic b and U near a, direct Taylor multiplication gives

U(a+iy)U(a−iy)=U²+Q(U)y²+T(U)y⁴/12+O(y⁶),
exp(b(a+iy)+b(a−iy))
 =exp(2b)[1−b''y²+(b''''/12+(b'')²/2)y⁴+O(y⁶)].

Multiply these expressions and compare coefficients. With F=exp(b)U,

Q(F)/exp(2b)=Q(U)−b''U²,
T(F)/exp(2b)=T(U)−12b''Q(U)+(b''''+6(b'')²)U².            (5)

The sign of F does not matter for either quadratic expression. No division by U was used, so (5) holds at its zeros. In particular b' and b''' cancel exactly. Set b=ℓ and U=Z in (5). Since B_2(R_2−R_1)=T(f)−κQ(f), this proves (1), including all normalization factors.

For (3), put g(a)=ζ(1/2+ia). Then Q(g)=C_2 and T(g)=C_4: the factors i^j from height differentiation give these signs. Also exp(β)=H exp(iθ) and f=−exp(β)g. Apply (5) with b=β and U=g and divide by H². Its value is real because f and its real derivatives are real; taking the real part gives (3). This formula also avoids division by ζ and is valid at every real zero.

The exact gamma derivatives can be read without a zeta expansion. If ψ=(log Γ)' and ψ', ψ''' denote its derivatives with respect to w, then

β''=2(1/4−a²)/(a²+1/4)²−ψ'(w)/4,
β''''=−12(a⁴−(3/2)a²+1/16)/(a²+1/4)⁴+ψ'''(w)/16.        (6)

Indeed β=log((a²+1/4)/2)−(log π)/4−ia(log π)/2+log Γ(w). Differentiating this analytic formula proves (6); the π factor has zero second and higher logarithmic derivatives.

Here is a uniform remainder justification for (2) and (4). On the complex disk |z−a|≤a/4 for all sufficiently large a, w(z)=1/4+iz/2 has modulus comparable to a and lies in a fixed closed sector away from the negative real axis. The polynomial factor z²+1/4 has no zero there. Choose logarithms compatible with their values on the positive real axis. The logarithmic complex Stirling formula and its sector remainder, recorded in the foundations, imply on this disk

β(z)=c_0−πz/4+(7/4)Log z
       +i[(z/2)Log(z/(2π))−z/2−π/8]+E(z),                (7)
c_0=(1/4)log(π/2),       |E(z)|≤C/a.

To check the coefficients, use

Log w(z)=Log(z/2)+iπ/2+Log(1+1/(2iz)),
Log(1+1/(2iz))=1/(2iz)+O(a^(−2)).

In (w−1/2)Log w−w, the constant produced by (iz/2)/(2iz)=1/4 cancels the −1/4 from −w. The remaining logarithmic coefficient is −1/4 from gamma plus 2 from log(z²+1/4), hence 7/4. The real linear term is −πz/4. The constant imaginary term is −π/8, and the π power gives the stated phase. All omitted terms, including the Stirling remainder, are analytic and O(1/a) on the disk.

Cauchy's estimates on a concentric smaller disk give E^(j)(a)=O(a^(−1−j)) for each fixed j. Thus differentiating the explicit terms in (7), with this analytic remainder bound, proves (4). Taking real parts gives the displayed formulas for p and q; no bare real-variable big-O term has been differentiated. Substitution in (1), using q+6p²=O(a^(−4)), proves (2). In particular there are constants A,C>0 such that

|J−(T(Z)−κQ(Z))|≤C a^(−2)(|Q(Z)|+Z²)       for a≥A.      (8)

The leading expression has no automatic sign. Fix a height a_0 and write x=t−a_0. The two real analytic germs

U_−(t)=x,             U_+(t)=x−κx³/6

have U=0, U'=1, U''=0 at a_0. Their third derivatives are respectively 0 and −κ, so both have Q=1, whereas T−κQ equals respectively −κ and 3κ. Since p(a)→0, for all sufficiently large a_0 one has |12p(a_0)|<κ/2. The right side of (1) at U_− is then −κ−12p<−κ/2; at U_+ it is 3κ−12p>5κ/2. The first form Q(−HU)/H²=1 is strictly positive for both. This proves indefiniteness even after the full gamma correction and even with first-level positivity at that point. Here κ is held fixed at the actual-theta value; these are not assertions about the models' own moment normalizations, global zeros or Fourier kernels.

For the actual function there is a useful exact statement of what is still needed at any simple real zero a_0 of Z. Dividing (1) there by the positive Z'(a_0)² shows that R_2(a_0)≥R_1(a_0) is equivalent to

Z'''/Z'≤(3/4)(Z''/Z')²−κ/4−3p,                          (9)

with all terms evaluated at a_0. No simplicity hypothesis at other zeros or sign of this expression is proved here. Equation (9) illustrates the arithmetic derivative information the gamma calculation leaves unresolved. ∎

The actual required bound is J≥0 for every sufficiently large a, followed by coverage of the remaining finite range if a global comparison is sought. The achieved bound (8) controls only a weighted gamma correction to T(Z)−κQ(Z). A lower bound for that arithmetic form exceeding the correction would be sufficient, but is not supplied; the test germs rule out assigning its sign from reality and the envelope alone. This does not refute averaged ordering for actual theta, establish a negative Laguerre coefficient, or affect the endpoint arithmetic margin of the separate saddle route.

The reproduction command `python3 scripts/laguerre/check_gamma_ordering_identities.py` independently checks both identities (5) by the Leibniz rule in an exact integer polynomial ring. It verifies the cancellation of b' and b''' and the factors 12 and 6. This finite algebra check does not replace the analytic remainder proof or supply any zeta sign.

**Mathlib.** Full statement: not checked. Supporting Taylor-product identities, gamma logarithms, complex Stirling and Cauchy derivative estimates: not checked for Mathlib coverage; no matching theorem is asserted. The supporting classical inputs are the named logarithmic complex Stirling formula, [NIST DLMF 5.11.1](https://dlmf.nist.gov/5.11.E1), and its [sector remainder bounds](https://dlmf.nist.gov/5.11#ii), checked for their stated complex domain. These are not matches for the full ordering obstruction. The completed-zeta identity and exact normalizations are the proved inputs specified above. The [Mathlib reference portal](https://leanprover-community.github.io/mathlib4_docs/) is retained without a coverage claim.
