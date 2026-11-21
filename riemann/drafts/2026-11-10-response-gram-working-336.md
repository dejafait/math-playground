# Continuum response Gram attempt — step336

Started 10 November; completed 11 November 2026. The pre-invocation EXPLORE
assessment review334, completed in step335 and supplied at startup,
covers exactly: Test continuum-Gram-selected polynomial slope packets
for target value one, subexponential original TV and uniform exponential
suppression on J.

Main gap: L030-L032/C032a actual-Xi positivity and L966/L968 signed
forcing, with L984(H) unpaid. The one intermediate target is the exact
continuum minimizer in degree<=n for one fixed admissible A. Its possible
downstream use is the unpaid point bridge after C997c's bounded branch
recovery. The test requires target exactly one, original TV<=exp(o(n))
and closed-J supremum<=exp(-sigma*n), sigma>0, on an unbounded integer
subsequence, or a rigorous incompatibility for this selection.

Inputs loaded: C997c(1),(4)-(6), C997e's fixed-A definition and target
asymptotic, review329's norm/growth contracts, C997g's audited full-jet
stop. C997g is comparison evidence only. The atomic, unmodulated,
binomial and full-jet stops are preserved; none bans continuum selection.
No cross-notebook input. No new source coverage is needed for this attempt.

Initial line of attack: use the exact Fourier density to decide the
response kernel, use C997e only to establish eventual target feasibility,
and import the covered complex constrained-quadratic theorem with the
correct target conjugation. Then test whether the resulting extremal
geometry yields the simultaneous growing-n rates. Treat finite-rank
formulas and derivative-charged norm transfer as intermediate work,
not as the requested rates. No conclusion is yet established.

Checkpoint during the attempt: exact injectivity can be proved at the
RIGHT upper spectral edge, where the lower interval is absent. If the
whole Fourier transform vanishes, Plancherel makes its compact L2 density
zero. On the edge this density is g_n(t) times a tail integral of the
weighted polynomial. Since g_n has only finitely many zeros, differentiating
that zero tail forces the polynomial to vanish on an interval. Hence the
Gram matrix is positive definite for every n>=2. C997e's P=1 target
asymptotic makes the constraint feasible for all sufficiently large n;
its normalized original TV is O(n^(3/2)). This need not bound the
minimizer's TV.

The covered Li-Zhang Theorem1.3 has general derivative order, not only
the first-order instance highlighted in review334. Its exact statement
and short proof were checked at the already assessed primary PDF,
arXiv2110.12967v1 pp1-3, for the specialization d=1, k=m, j=0,
q=r=2, p=infinity, theta=1/(2m). This is application verification
within ready coverage, not a new literature assessment or a changed
target. The original Fourier-TV bound charges every fixed m-th derivative.
Letting m be any sufficiently large FIXED integer before n tends to
infinity removes the spurious positive minimum decay threshold from a
first-derivative-only argument. No uniform-in-m constant is needed.

Proposed exact reduction: with target diagonal Kcal_n and the weighted
L1 cost M_n of its unnormalized Riesz polynomial, the unique minimizer
has energy 1/Kcal_n and original TV M_n/Kcal_n. The full desired packet
test reduces to simultaneous Kcal_n>=exp(kappa*n), kappa>0, and
log^+(M_n/Kcal_n)=o(n) on an unbounded subsequence. The charged
fixed-order interpolation then gives every band exponent sigma<kappa/2.
Neither of these simultaneous conditioning rates has been established.
Do not label the reduction a successful packet or an obstruction.

Both beta terms, both short intervals, slope endpoints and K's -1
must remain throughout. No discretized Gram matrix, auxiliary coefficient
norm or separate asymptotic branch is the original response/TV norm.
The point bridge, selected/both-sign transfer, C997a(8), original assay,
reconstruction, signed recovery, complements, regulators, L993 and
L984(H) remain unresolved.

Completed intermediate input: the full proof, exact conjugations,
original-TV bounds and fixed-order limiting argument are canonical in
[C997h](../lemmas/C997h-continuum-gram-packet-rate-reduction.md).
Outcome ADVANCE / REPRODUCTION is limited to this local feasibility
and charged norm-transfer input. No joint conditioning rate, successful
packet, class obstruction or progress beyond the imported general
theorems is claimed. The constant feasible comparison supplies only
Kcal_n>=C_A^(-1)n^(-5)exp(-17n/32), which does not pay the positive
exponent test. No mathematical script or numerical certificate was used.
The next attempt can reuse the unchanged review334 target and focus
on its two simultaneous conditioning quantities. Independent audit of
the new specialization remains pending.
