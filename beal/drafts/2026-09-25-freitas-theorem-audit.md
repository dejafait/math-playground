# Freitas repeated-cube theorem audit — 2026-09-25

This records one focused source-and-application step, not a candidate resolution of Beal.

## Starting state and relevance

The shared instructions, local goal, checkpoint, entire overview, and DAG were read before selecting work. The existing tracked and untracked work is preserved. L002 and C002a leave the repeated-cube signatures in the residual set, while L003 gives exact factor systems without excluding them. Attempt 001 rules out unrestricted congruences alone; Attempt 002 rules out discarding the quadratic factor merely because it is a power. Neither obstruction rules out a global modular theorem.

The precise gap addressed is zero positive primitive solutions to a^3+b^3=c^p for a specified infinite set of residual prime exponents. The intermediate target is to audit the exact hypotheses and exponent range of Freitas's located theorem and prove its application to the permitted placements of (3,3,p). Its plausible downstream use is to remove a genuine part of the residual set and restrict the two systems in L003. Complementary primes, small exceptional exponents, and other mixed signatures would still require separate inputs.

The discriminating test is the full numbered theorem, including its definitions of primitive and nontrivial, its prime lower bound, and whether it is conditional. Continue with a qualified exclusion only if the source covers the actual auxiliary integer triples; otherwise retain only the narrower conclusion or reject the application. The required threshold is zero solutions throughout the asserted range, not a density estimate or a finite search.

## Reasoning saved during the audit

The accessible full paper is [Freitas, arXiv:1601.06361](https://arxiv.org/pdf/1601.06361). Its Theorem 3 includes a lower bound omitted from the abstract: p >= 17. The statement identifies the nonsquare condition with p congruent to 2 modulo 3. The introduction defines nontriviality by abc nonzero and primitivity by gcd one. The theorem and the surrounding proof still need a focused reread before import.

All three exponents are odd in this range, so a prospective positive solution a^p+b^3=c^3 would give the signed cube equation c^3+(-b)^3=a^p. A precise application must retain the nonzero coordinates and gcd, and must not claim coverage for p=5 or p=11 from this theorem alone. L003 is potentially useful downstream, but its factorization is not an input to this cited exclusion.

Mauldin's accessible primary target page was retrieved again; the nominated AMS endpoint again returned HTTP 403. The local target and the earlier source-access qualifications are retained.

## Completed assessment

The source test passed with the lower bound retained. The published version and precise citation are recorded in [the foundation](../foundations/03-freitas-repeated-cube-theorem.md); section 2 was read to check that the result is unconditional. Some mathematical signs are damaged in the publisher PDF's text extraction, so the readable arXiv version was used to cross-check the signs. This is a use of the named theorem, not an independent reproof of its modular ingredients.

[L004](../lemmas/L004-freitas-repeated-cube-exclusions.md) contains the full application proof. It checks the residue condition by an elementary finite-group argument, checks all three signed coordinate transformations and their gcds, uses L002 for the original exponent divisibility consequence, and uses L003's converse to exclude both complete factor systems in the admitted range. The earlier results do not already supply this exclusion: C002a treats two copies of the larger prime, whereas this application treats two cubes.

The boundary checks are mathematical, without a finite solution search. Small nonsquare-condition primes fail the lower bound; a complementary prime has an explicit square root of -3. The achieved exclusion reaches the required zero-solution threshold on its exact range, but not on all residual signatures. No computational bound, density, or complete Beal candidate is inferred.

Outcome: ADVANCE through a relevant cited input and its qualified consequences. Exploration turns used without an advance or informative negative result: 0/3. The application audit is complete. The reason for continuing toward the original Kraus result is the divisibility condition quoted in Freitas's introduction: if established at complementary primes with its precise hypotheses, it could eliminate the unramified branch still left by L003. That quoted condition is not used as a separate premise in this step. The stopped elementary shortcuts are not reopened.
