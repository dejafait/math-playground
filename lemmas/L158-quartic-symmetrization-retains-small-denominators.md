# Lemma 158: quartic symmetrization retains small denominators

**Hypotheses.** Use L157's finite window I, real coefficients A_n,
frequencies λ_n, variables z_n, H, Q, B, χ, M, N and expectation E_T.
Put J=Σ_n A_n' exp(i(t−π/2)λ_n), and for r≠s put
Δ_rs=λ_r−λ_s. Constants may depend on the fixed window and χ.

**Conclusion.** There is an exact decomposition

R=R_amp−(1/M)E_T[χ'(Q/M)K],

|R_amp|≤CN/(MT),                                         (1)

K=Σ_(r≠s,m≠n) ½(Δ_rs/Δ_mn+Δ_mn/Δ_rs)
                    z_r bar(z_s) z_m bar(z_n).           (2)

Thus the amplitude part tends to zero for fixed M. The phase kernel in
(2) does not have a uniformly bounded coefficient after full monomial
collection: for the fixed window [N/2,3N], N=k an integer ≥2, the
coefficient of z_k² bar(z_(k+1)) bar(z_(2k)) in K is

log(1+1/k)/log 2 + log 2/log(1+1/k) ∼ k log 2.           (3)

This is an algebraic obstruction to universal coefficientwise cancellation
of the small denominators. It is not a lower bound on R or its time
average, and does not disprove the actual cutoff-tail target.

**Proof.**

Differentiation of the finite sum gives

H'=J+iΣ_n λ_n z_n,
Q'=2 Re(J bar H)+P,
P=Σ_(r≠s) iΔ_rs z_r bar(z_s).

The diagonal phase terms vanish. Both P and B are real by conjugate
pairing. Insert this identity in R=−E_T[χ'(Q/M)Q'B]/M from L157.
The amplitude contribution is exactly

R_amp=−(2/M)E_T[χ'(Q/M) Re(J bar H) B].

L156 proves E_T|H|²≤C. Its finite-sum mean-square argument also gives
E_T|J|²≤C/T²: apply that argument to coefficients d_n=T A_n'.
Indeed |d_n|≤CT^(−1/4) and |d_n'|≤CT^(−5/4), using L156's first
and second derivative estimates and treating T as a fixed parameter.
Consequently Cauchy–Schwarz and L157's |B|≤CN yield

|R_amp|≤(2||χ'||∞ CN/M)(E_T|J|² E_T|H|²)^(1/2)
         ≤CN/(MT).

No differentiation of χ' is needed; χ is only C¹.

Multiplying the finite sums for P and B cancels i and gives

PB=Σ_(r≠s,m≠n) (Δ_rs/Δ_mn) z_r bar(z_s)z_m bar(z_n).

Exchanging (r,s) with (m,n) preserves the summation domain and monomial.
Averaging these two expressions proves K=PB and (2). This is a real
quartic polynomial evaluated on the z_n. To test whether further
collection of identical monomials cancels its denominator, regard z_n
and bar(z_n) as formal variables, with conjugation imposed on evaluation.
For the monomial in (3), the only ordered choices are

(r,s,m,n)=(k,k+1,k,2k) and (k,2k,k,k+1).

Both are admissible and there are no other choices because the two
unconjugated indices must both be k. With x=−log(1+1/k) and y=−log 2,
the collected coefficient is x/y+y/x. This proves (3), since
k log(1+1/k) tends to 1. The conjugate monomial has the same real
coefficient, so taking the real part does not remove it algebraically.
All these indices lie in the stated fixed window, and T=2πk² realizes
N=k within the hypotheses. This provides an allowed family, without
asserting that every window has these particular indices. ∎

## Scope and verification

The unbounded coefficient does not give a large value of the evaluated
polynomial: the monomials have their actual amplitudes and oscillatory
phases, and χ'(Q/M) is an additional correlated factor. Other monomials
can cancel after evaluation or time integration. In particular, this is
not a counterexample to a bound for the actual series. The algebraic
substitution alone supplies no such bound.

For a pair of gaps x,y, the symmetrized kernel equals
(x+y)²/(2xy)−1. On the exact zero-total-frequency part x+y=0 it equals
−1, so there is cancellation on that part even though (3) rules out
universal cancellation. Estimating its contribution with the cutoff
present, and estimating the remaining part, are not established here.

Verification consists of the finite chain rule, the two pair orders in
(3), signs of i, and the mean-square normalization. A standalone rational
frequency check in scripts/heat/check_quartic_symmetrization.py also
checks the polynomial identity and collected coefficient exactly; it is
a regression check, not a numerical proof about the zeta function.
Formalization would require finite polynomial multiplication and
reindexing, coefficient collection, Cauchy–Schwarz, the finite-sum
mean-square estimate of L156, and the elementary logarithm limit.

**Mathlib.** The availability of a Mathlib theorem for this full statement has not yet been established. Mathlib documentation:

https://leanprover-community.github.io/mathlib4_docs/

**Lean proof status.** Not yet formalized or validated. This status does not assert that the mathematical statement is incorrect.

**Lean proof command.**

Not available until a complete Lean proof has been validated.

**Lean proof code.**

Not yet available.
