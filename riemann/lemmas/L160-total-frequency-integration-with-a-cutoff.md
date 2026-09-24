# Lemma 160: total-frequency integration with a cutoff

**Hypotheses.** Use L159's finite Gaussian window, and L158's notation
x=λ_r−λ_s, y=λ_m−λ_n, h=(x/y+y/x)/2. Strengthen the cutoff
hypothesis to χ∈C²(R), still nondecreasing, zero on (−∞,1] and one
on [2,∞). Fix M>0. Constants depend only on the window and χ.
Write ω=x+y and p=A_r A_s A_m A_n. In sums marked nonres below,
r≠s, m≠n, and rm≠sn. All frequencies and index sets are fixed as t varies.

**Conclusion.** Define real functions

U=Σ_nonres h p exp(i(t−π/2)ω)/(iω),
U_amp=Σ_nonres h p' exp(i(t−π/2)ω)/(iω).

Then U'=K_non+U_amp and the nonresonant remainder of L159 satisfies

R_non=−[χ'(Q/M)U]_T^(2T)/(MT)
       +(1/M)E_T[χ'(Q/M)U_amp]+R_der,
R_der=(1/M²)E_T[χ''(Q/M)Q'U].                         (1)

Uniformly on [T,2T],

|U|≤CN² log(2T),  |U_amp|≤CN² log(2T)/T.              (2)

Consequently the first two terms of (1) together have absolute value
at most C log(2T)/M, while

|R_der|≤CT log(2T)/M².                                (3)

These bounds do not establish a bound uniform in T for fixed M for the
new derivative remainder. Such a bound for the actual remainder remains
unproved; no growing lower bound is asserted.

**Proof.**

All sums are finite. Conjugating a summand and exchanging r with s and
m with n changes ω to −ω, preserves h and p (or p'), and gives another
summand. Thus U and U_amp are real. Differentiating U proves its stated
identity. Substitute K_non=U'−U_amp into
R_non=−E_T[χ'(Q/M)K_non]/M and integrate by parts. The chain rule
(χ'(Q/M))'=χ''(Q/M)Q'/M gives (1), including its endpoint signs.
This derivative is justified by C², not by the earlier C¹ hypothesis.
Such cutoffs exist: use χ(1+v)=10v³−15v⁴+6v⁵ for 0<v<1,
with the stated constant extensions. Its derivative is 30v²(1−v)².

To bound the primitive without multiplying three inverse-gap bounds, use

h/ω=(1/x+1/y)/2−1/ω.                                  (4)

Put c_k=Σ_{r,m∈I,rm=k}A_r A_m, with k ranging over distinct products,
and define

V=Σ_{k≠l} c_k c_l exp(i(t−π/2)log(k/l))/(i log(k/l)).

Let B and D be as in L157. Exact finite regrouping gives

U=B(Q+D)−V.                                            (5)

Indeed the first part of (4), divided by i, summed over all pairs
r≠s,m≠n is B(Q−D). Terms with ω=0 in that first part have
1/x+1/y=0 and therefore contribute zero. The second part is the
negative of the nonresonant quartic primitive with these same exclusions.
The full primitive V includes in addition r=s or m=n. Each equality
contributes DB; their intersection has ω=0 and is absent. Thus that
excluded primitive is V−2DB, proving (5).

There are O(N) window indices, with |A_n|≤CN^(−1/2) and
|A_n'|≤CN^(−1/2)/T by L156. In particular Q≤CN and D≤C.
L157 gives |B|≤CN. Every product index is at most b²N², so distinct
product frequencies log k have separation at least 1/(b²N²), by the
mean value theorem. The generalized Hilbert inequality stated in
foundations/notation-and-inputs.md, applied to the vectors
c_k exp(i(t−π/2)log k), gives

|V|≤CN² Σ_k c_k²=CN²F≤CN² log(2T).

The final inequality is L159's bound on F proved there (rather than an
inference from Z≤F). This proves the first estimate in (2) using (5).
Empty or singleton product sets have V=0 and require no spacing bound.

For clarity, an amplitude derivative means differentiating every A_n
while holding all exponential factors fixed. This operation is a
product-rule derivation on the finite expressions. Applied to (5), it
identifies U_amp exactly. The amplitude derivatives of B, Q and D
satisfy, respectively,

|B_amp|≤CN/T, |Q_amp|≤CN/T, |D_amp|≤C/T.

The first bound is the C bound of L157. The second follows from
Q_amp=2 Re(J conjugate(H)), |J|≤C sqrt(N)/T and |H|≤C sqrt(N);
the third follows by summing 2A_n A_n'. Positivity of A_n and
|A_n'|≤CA_n/T imply |c_k'|≤Cc_k/T. Two applications of the same
bilinear Hilbert inequality therefore give

|V_amp|≤CN² ||c'||₂ ||c||₂≤CN²F/T.

Taking the amplitude derivative of (5) now proves the second estimate
in (2). The relative derivative bound used here follows directly from
A_n'=A_n log(n/N_t)/t in L156, on the fixed window.

Since N²=T/(2π), (2) gives the asserted endpoint and amplitude bounds
in (1). Finally L156's two mean-square bounds and Cauchy–Schwarz yield
E_T|Q'|≤2(E_T|H'|² E_T|H|²)^(1/2)≤C.
Use this and the first bound of (2) to obtain (3). The exact integrand
of R_der is supported on M<Q<2M, since χ'' vanishes elsewhere,
including the endpoints. This support is not removed from the identity;
the absolute estimate (3) simply bounds it by the whole interval. ∎

## A surviving total-frequency denominator

Even full monomial collection does not make the primitive coefficients
uniformly bounded. In the permitted fixed window [N/2,3N], set N=k≥2,
r=m=k and {s,n}={k−1,k+1}. The two ordered terms are the only ones
for z_k² conjugate(z_(k−1)) conjugate(z_(k+1)), where
z_n=A_n exp(i(t−π/2)λ_n). Both are nonresonant. With
x=log(k/(k−1)), y=log(k/(k+1)) and
ω=log(k²/(k²−1)), their collected coefficient in U is

(x/y+y/x)/(iω).

Here kx→1, ky→−1, and k²ω→1, so its modulus divided by k²
tends to 2. Taking conjugate terms makes U real but does not erase
these distinct formal monomials. This proves an algebraic obstruction
to bounded coefficients, not a lower bound for U or R_der after the
actual amplitudes, phases, and cutoff are inserted.

## Verification

Verification is analytic: finite conjugate pairing, (4), the two excluded
diagonals in (5), both integration-by-parts signs, the C² cutoff,
product-frequency spacing, the relative coefficient derivative bound,
and normalized Cauchy–Schwarz. The overall RH argument is unchanged. Neither uniform control of R_der
nor the fixed-cutoff tail target is a proved input.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
