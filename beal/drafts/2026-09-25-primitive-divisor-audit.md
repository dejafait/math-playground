# Primitive-divisor multiplicity audit — 2026-09-25

One focused audit of the next action in the checkpoint; no complete Beal candidate.

## Starting state, relevance, and discriminating test

The shared instructions, local target and checkpoint, whole overview, DAG, existing changes, L007, and the three recorded failed mechanisms were read. Existing unfinished work is preserved. Mauldin's accessible primary Beal statement was rechecked; retrieval of the nominated AMS page failed again.

The gap is emptiness of the complete coefficient, norm, and positive-trace system in the repeated-cube branch at primes p >= 19 congruent to 1 modulo 3. The proposed intermediate target is a precise application of Bilu–Hanrot–Voutier to L007's Lucas pair, followed by a test of whether a primitive divisor supplies a multiplicity incompatible with U_p = sigma k^p or sigma p k^p. Such a multiplicity restriction could exclude the branch; other residual signatures would still remain. The required threshold is at least one prime outside the exceptional factor p whose valuation is not a multiple of p, for every candidate parameter pair. Mere divisor existence does not reach that threshold.

This does not repeat the unrestricted congruence, isolated quadratic-factor, or exceptional-prime exclusions. L007 already warns that existence alone is insufficient, but no primary primitive-divisor theorem has been applied and no construction of high primitive-divisor multiplicity in this specific Lucas family has been recorded. Continue only if the theorem or the constrained family supplies the missing valuation information; stop this direct inference if the theorem gives only existence and the family admits primitive divisors with multiplicity p. Such a construction need not satisfy the whole coefficient equation and must not be presented as a Beal solution or as a refutation of every possible divisor argument.

## Unfinished reasoning saved before the audit

For gamma=(r+t sqrt(-3))/2 and its conjugate, the sum and product are the coprime integers r,v. The root-of-unity exclusion still needs to be checked. The theorem's published number, primitive-divisor definition, and small-index range must be read in a primary source.

A possible multiplicity control is to fix p=31 and t=3^29, find a simple root modulo an auxiliary prime q of the coefficient polynomial 2^30 U_31(r,(r^2+3t^2)/4), and lift r to obtain exact q-adic valuation 31. A Chinese-remainder condition on r can retain oddness, gcd(r,t)=1, and v congruent to 1 modulo 12. This is a proposed test, not an established construction. The full coefficient equation and trace bound are not assumed in that test.

The primary manuscript has now been read: Theorem 1.4 applies above index 30, and Theorem C with Table 1 covers prime indices 17,19,23,29. Its primitive-divisor definition excludes the discriminant and earlier terms, without requiring valuation one. For the construction, q=373 is prime, sqrt(-3)=177 modulo q, and t=3^29 is 300 modulo q. At r=4 the ratio (r+177t)/(r-177t) is 217, of order 31, and the derivative of the coefficient polynomial is 90, nonzero modulo q. Thus simple-root lifting is available.

A strengthening still to check retains the trace inequality as well. After fixing a residue r_* with exact valuation M modulo q^(M+1), choose positive D with D congruent to r_*-33*3^29 modulo q^(M+1) and D congruent to 5-33*3^29 modulo 24. Set h=1+24*31*q^(M+1)*D*N, t=3^29*h^31, r=33t+D, for positive N. Then r/t approaches 33 from above, where the argument of gamma^31 lies between pi/3 and 2pi/3. Coprimality follows from h congruent to 1 modulo D. This could preserve positive tU_31 and |T_31|<3tU_31 while still leaving the essential condition U_31=k^31 unproved. Exact arithmetic and the angle bounds remain to be written and checked.

## Completed assessment

[L008](../lemmas/L008-primitive-divisor-multiplicity.md) completes the application and the construction, including the strengthened trace test. [The source audit](../foundations/05-primitive-divisor-theorem.md) records the precise primary statements and access qualifications. Nondegeneracy follows because a root-of-unity quotient would force v to divide r^2, contrary to coprimality and v>1. The finite-field order calculation gives ell congruent to plus or minus 1 modulo 6p, and therefore k>=6p-1 in either allowed complete coefficient shape. This is a lower bound; it cannot meet the required zero-solution threshold.

The polynomial has a simple root at r=4 modulo 373. Lifting to precision M and deliberately choosing a non-root next digit gives exact valuation M, not just a lower bound. The subsequent Chinese-remainder construction retains coprimality, v congruent to 1 modulo 12, and t=3^29 h^31 with 31 not dividing h. Its ratio 33<r/t<34 gives a rigorous argument bound proving positive tU_31 and |T_31|<3tU_31. Thus an individual primitive divisor can have multiplicity 31 even with the norm and trace restrictions. No statement about the valuations of all other divisors is inferred.

The [saved exact results](../scripts/primitive-divisors/results.json) check M=1,2,31, with N=1. At q=373 all 30 earlier nonzero-index terms are nonzero, and the prescribed valuation is exact. The recurrence and coefficient polynomial agree, the norm identity and strict trace bound hold, and coprimality holds. Each complete power condition fails modulo 311: the residues of U_31 are respectively 255,88,118, outside the enumerated set of 31st powers. These are auxiliary controls, not Beal solutions. Reproduce with `python3 scripts/primitive-divisors/check_multiplicity.py`.

Outcome: NEGATIVE, because the new arbitrary-multiplicity construction changes the decision on the proposed direct inference. Exploration turns used: 0/3. This is stronger evidence than merely repeating L007's warning, but it does not exclude the family or refute a future theorem controlling some divisor under the complete equation. [Attempt 004](../ATTEMPTS/004-primitive-divisor-multiplicity-inference.md) preserves this limited stop. No complete candidate appeared.

The reason for changing direction is that the audited theorem offers only existence and a lower bound, while the same constrained parameter family admits the allegedly forbidden multiplicity. A fixed smaller repeated-cube signature is an independent unresolved gap in the current assembly and permits a bounded primary-source classification audit. Its sole concrete action is recorded in PROGRESS.md; no part of that separate audit was undertaken in this step.
