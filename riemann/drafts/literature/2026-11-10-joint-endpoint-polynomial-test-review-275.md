# Joint endpoint observations: quantitative specialization nomination

TARGET: Test an all-index polynomial lower singular-value bound for L990's exact joint observation matrix J_n using C990a's second-order endpoint phases, retaining the constant corrections.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed step275 exact-statement, deterministic evaluation, small-value and near-collision searches, with local duplicates/failures, are recorded in 2026-11-10-joint-endpoint-observation-conditioning-review-274.md; no inspected theorem matches the quantitative target, and no novelty is inferred.
SOURCE_EVIDENCE: Reuse audited L990(5),(13), C990a(1),(12)-(16), GST1709.09656v1 section3.3 equations81-87, GST1609.00829v1 section2.1.3 equations20-25 and DLMF10.17(iii). Step275 inspected Chretien-Darses Theorem3.1/proof pp4384-4385 https://www.i2m.univ-amu.fr/perso/sebastien.darses/PAMS.pdf, Fukshansky Spring2015 section4 equation13/Theorem4.4 pp25-26 https://www1.cmc.edu/pages/faculty/lenny/classes/spring_2015/m195/m195_lectures.pdf and Bindel CS6210 25August2025 final SVD section https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-08-25.html; hypotheses and limits are in review274's completed comparison.
COMPARISON: Known uniform asymptotics and finite-dimensional conditioning tools supply ingredients; exact cofinite noncollinearity, single-polynomial root spacing and homogeneous algebraic approximation do not supply a polynomial quantitative row-angle estimate. Only that identified difference is proposed for specialization.
GAP: Prove a uniform quantitative separation through all corrected collision neighborhoods and then the exact J_n singular-value bound; no exponent, constant, onset or obstruction to all polynomial bounds is established.
REASON: Essential source comparison is complete for one direct robustness test of the audited recurrence/phase argument. This freshly nominated ready continuation receives separate next-turn approval before mathematics; it is not a completed proof or a new central creative mechanism.
SCOPE: Exactly integer n>=2, L990's corrected kernels at n and 2n, a_hat_n=a_n/||a_n||_2, b_hat_n=b_n/||b_n||_2, c_n=(a_n cross b_n)/||a_n cross b_n||_1 and J_n=[a_hat_n;b_hat_n;c_n], beyond C990a's one existential onset. No change of endpoints, added rows, leading-phase replacement, frequency hypothesis or arithmetic estimate is covered.

The complete search/source comparison and its qualifications are in
[review274](2026-11-10-joint-endpoint-observation-conditioning-review-274.md),
completed in step275. Reuse that evidence; another search with unchanged
hypotheses would need a new essential reason. This file nominates the
same mathematical bound (T), not a broader problem.

Seek C>0, finite A>=0 and N such that

    ||J_n v||_2 >= C*n^(-A)*||v||_2
    for every integer n>=N and every v in R^3.

Essential inputs are the exact L990 rows, recurrence identity and row
scales, and C990a's additive O(n^-2) endpoint phase formula and cofinite
definition. Their audited primary-source contracts can be cited at
their stated hypotheses. No reproof of GST or qualitative nonvanishing
is needed. The proposed missing argument concerns approximate
collinearity, including its error after the O(n)-sized integer phase
expressions are squared; its outcome is not assumed. Use standard SVD
tools only after proving the needed quantitative row separation.
Do not divide by a small phase, pivot or cross product without a bound.

Continue with a rigorous all-index bound or a specific informative
obstruction. A numerical horizon, pointwise invertibility, torus
compactness, or exclusion outside fixed collision neighborhoods does
not decide the target. A negative answer needs an obstruction to every
polynomial bound, not failure of one proposed exponent. Such a negative
answer would not itself rule out weaker subexponential recovery.

Plausible use: recover a three-term actual B-vector from all three
outputs at a polynomial cost if those outputs can independently be
controlled. Bounds for the two additional endpoint outputs, the signed
arithmetic identification, common/shifted intervals, every prime power,
other zeros, both complements and L984(H) are unresolved. Actual-Xi
positivity L030-L032/C032a and L966/L968 signed forcing remain the main
gap. No RH implication or candidate is asserted.

Preserve scalar stops270/272/274 and unfinished working271. L991/L992
are contrasts, not additional hypotheses for this target. No
cross-notebook input. Full matching Mathlib coverage is unchecked.
The intended next mathematical task is proof_attempt/development, not
creative: it extends an established finite-dimensional phase mechanism
and does not yet provide a new signed arithmetic mechanism at the main
gap. Separate approval may reuse this completed source record.
