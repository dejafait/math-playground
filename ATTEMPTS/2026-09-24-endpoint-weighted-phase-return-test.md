# Endpoint weighted Fourier return test — 2026-09-24

Gap and target: the prescribed endpoint height still has no arithmetic
sign margin. Test whether retaining every Fourier coefficient weight
can place a visit to L339's negative phase box in a translated interval
of length H=exp(2r). Such a visit would assess the exceptional arithmetic
heights on the relevant scale; transfer to the prescribed a_n, the low
Laguerre indices and the global mixed positivity would remain unproved.
The test is whether 2Λ_m/H<b_m−q^m, with the exact reciprocal-frequency
sum Λ_m, product-bump mean b_m, and outside-box maximum q^m.

Redundancy review: read GOAL.md, PROGRESS.md, the whole PROOF.md and
global DAG, and inspected existing modifications and unfinished work.
L336 stops the worst-frequency estimate with a shrinking phase width;
L338–L339 supply a smaller prime cutoff and fixed width. The exact
coefficient-weighted budget has not been evaluated there. L333–L334's
arithmetic moments concern a different function and give no return
certificate for this box. The September 21 admission condition is
superseded by GOAL.md; its mathematical evidence remains intact.

Unfinished reasoning saved before completing the proof: the absolute
Fourier coefficients of ∏_p[(1−cos θ_p)/2]^m form a product probability
distribution. Each coordinate has mean zero and variance m/2. If
V=Σ_(p≤y)(log p)² and b_m is the mass at the zero vector, then
Σ c_k(Σ k_p log p)²=mV/2. Unique factorization removes all other zero
frequencies. Two Cauchy–Schwarz inequalities should give
Λ_m≥(1−b_m)^(3/2)/sqrt(mV/2), without any Diophantine lower bound.
The central binomial recurrence appears to give
b_m≤(3m+1)^(−d/2), d=π(y). Combining these bounds may force the
length required by this certificate to exceed
2^d/(sqrt(d)log y), uniformly in m≥1 when d≥2. An elementary central
binomial prime-count bound would then put log H above a constant times
exp(6sqrt(r))/sqrt(r), far exceeding 2r. Check constants, all-degree
uniformity, the necessary-versus-sufficient distinction, and the prime
count before assigning an outcome. No theorem is claimed at this saved
checkpoint. Zero consecutive unresolved exploration turns preceded it.

Result: [L340](../lemmas/L340-endpoint-weighted-fourier-return-obstruction.md)
proves the saved moment lower bound and all-degree certificate barrier.
For every degree that separates the outside-box maximum from the mean,
the length threshold 2Λ_m/(b_m−q^m) is at least
2^d/(sqrt(d)log y). Its logarithm is at least
c exp(6sqrt(r))/sqrt(r), uniformly in the degree, compared with the
required 2r. The proof uses the exact finite coefficients and an
elementary central-binomial prime-count argument, with no estimate
for the smallest nonzero frequency and no prime-number-theorem input.

WHY IT FAILS: the [canonical proof](../lemmas/L340-endpoint-weighted-fourier-return-obstruction.md)
shows that the growing number of constrained primes makes the product
bump's mean too small relative to its absolute reciprocal-frequency
budget. Its second frequency moment already forces this loss, even
if every frequency is evaluated exactly. The fixed phase width and
smaller cutoff therefore do not rescue the weighted absolute Fourier
certificate. This is not a lower bound on actual waiting time or on
the actual signed discrepancy, and it does not exclude a visit in any
particular interval or a method that retains cancellation between modes.

Assessment: NEGATIVE; stop this absolute Fourier certificate, with
zero consecutive unresolved exploration turns. No arithmetic value is
located at a_n, no Laguerre sign or exclusion range changes, and no
RH candidate appears. The subsequent geometric test concerns the Haar
measure of the phase box swept along a time segment: unlike the failed
Fourier budget, a strict covering deficit could rule out a visit in
every translated interval at this scale. That would decide whether
the uniform full-box target itself should be abandoned, while leaving
a particular coupled interval unresolved. It is a different mechanism,
not another bump-degree or frequency-bound optimization. The sole
current action is in PROGRESS.md.

Verification: reviewed the coefficient normalization, zero-frequency
uniqueness, exact second moment, both Cauchy–Schwarz steps, degree
uniformity, prime valuations and quantifiers in the scale comparison.
The exact check `python3 scripts/laguerre/check_endpoint_weighted_return.py`
passes 624 Fourier coefficient checks, 52 quadratic frequency
coefficients, 700 degree comparisons, 3,899 prime valuations and 128
central-binomial bounds. These supplement the proof without computing
an actual return or a large-dimensional Fourier sum. Full Mathlib
coverage is not checked; no new library result is imported. The direct
mathematical inputs in the DAG are L336's finite Fourier identity and
L339's conditional arithmetic consequence of a visit. All earlier work
is preserved.
