# Lemma 157: signed cutoff Hilbert remainder

**Hypotheses.** Use the finite window, coefficients A_n, centered frequencies
λ_n, H, Q, w=χ(Q/M), and expectation E_T from L156. In particular
N=sqrt(T/(2π)), 0<a<b are fixed, M>0, and T is sufficiently large.
Constants may depend on a,b,χ only. Set D=Σ_n A_n² and
z_n=A_n exp(i(t−π/2)λ_n). All indices below belong to that fixed window.

**Conclusion.** Define the real signed bilinear forms

B(t)=Σ_(m≠n) z_m conjugate(z_n)/(i(λ_m−λ_n)),

C(t)=Σ_(m≠n) (A_m' A_n+A_m A_n')
             exp(i(t−π/2)(λ_m−λ_n))/(i(λ_m−λ_n)).

Then

B'=Q−D+C,                                                (1)

E_T(Qw)=E_T(Dw)+[wB]_T^(2T)/T−E_T(wC)+R,
R=−E_T(w'B)=−(1/M)E_T[χ'(Q/M)Q'B].                     (2)

Uniformly on the interval,

|B|≤CN,  |C|≤CN/T,                                     (3)

and consequently

|R|≤C sqrt(T)/M,
E_T[Q 1_(Q>2M)]≤C/M+C/sqrt(T)+C sqrt(T)/M.              (4)

The signed Hilbert estimate removes the logarithm in L156's bound but
does not give a small fixed-cutoff tail. Neither a growing lower bound
on R nor failure of the actual tail target is asserted.

**Proof.**

Pairing (m,n) with (n,m) shows that B and C are real: the paired
summands are conjugates because conjugation changes the sign of i
and exchanging the indices changes the sign of the real denominator.
Differentiate the finite sum for B. The phase derivative cancels its
entire denominator and gives Σ_(m≠n)z_m conjugate(z_n)=Q−D;
the two amplitude derivatives give C. This proves (1).
Multiplying (1) by w and integrating by parts proves (2), with both
endpoints included. The chain rule gives the second expression for R.
In particular the correlation with Q' has not been discarded in (2).

For completeness the standard Montgomery--Vaughan generalized Hilbert
inequality, as stated in foundations/notation-and-inputs.md, bounds

|Σ_(m≠n) x_m conjugate(y_n)/(λ_m−λ_n)|
 ≤ C δ^(−1)||x||₂||y||₂

when all distinct frequencies are separated by at least δ. Indeed the
nearest-neighbor version has each inverse gap at most δ^(−1).
Here the mean value theorem gives δ≥1/(bN). L156's coefficient bounds
and the O(N) indices imply

Σ A_n²≤C,   Σ |A_n'|²≤C/T².

Apply Hilbert first with x=y=z. Apply it twice more with x the vector
A_n' exp(i(t−π/2)λ_n), y=z, and with these roles reversed. Multiplication
by 1/i preserves absolute values. These three applications prove (3).
The empty or one-index cases have zero off-diagonal forms and satisfy
the same conclusions without defining a nearest-neighbor gap.

Equation (3) bounds the normalized endpoint and C terms in (2) by
CN/T=O(T^(−1/2)), since 0≤w≤1. L156 gives
E_T(Dw)≤C/M and ∫|w'|≤CT/M. Hence

|R|≤(CN/T)∫|w'|≤CN/M.

This proves (4), using w=1 on Q≥2M. The last step takes an absolute
value in time and therefore does not estimate signed time correlation.
No infinite sums, limiting operations, or numerical inputs occur. ∎

## Correlation audit and scope

There is an exact but circular alternative manipulation. Integrating R
back and using (1) gives

R=−[wB]_T^(2T)/T+E_T[w(Q−D+C)].                         (5)

Substitution into (2) cancels all terms and returns E_T(Qw)=E_T(Qw).
Thus (5) alone is not independent control of the correlation. The
chain-rule integrand in (2) is supported on M<Q<2M; exploiting that
support or additional cancellation remains an open estimate here.
The conclusions concern this application of the Hilbert inequality,
not all possible uses of it. A uniform bound for R and the required
small tail remain unproved. No positive-proportion or RH result follows.

## Verification

Analytic verification checks conjugate pairing, the positive sign of Q−D
in (1), both amplitude derivatives, both endpoint signs, the frequency
gap, the two coefficient energies, and division by T in (2) and (4).
No computation is
required to certify these finite algebraic identities and inequalities.

**Mathlib.** Not checked: availability of a Mathlib theorem for the full statement is unknown. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/
