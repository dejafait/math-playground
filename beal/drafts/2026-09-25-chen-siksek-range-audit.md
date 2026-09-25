# Chen–Siksek repeated-cube range audit — 2026-09-25

## Starting state and relevance

Read the shared GOAL.md and PROMPT.md, local GOAL.md and PROGRESS.md, the whole PROOF.md overview and DAG.md, and the relevant L002, L003, L009 and historical failures. No applicable AGENTS.md or pre-existing local changes were found; changes in other notebooks are preserved. The accessible primary formulation at [Mauldin's page](https://sites.math.unt.edu/~mauldin/beal.html) still agrees with the recorded target. The nominated AMS endpoint again failed retrieval.

The main gap is uniform emptiness of all residual reduced signatures. The intermediate target for this single source audit is a precise nonexistence theorem covering X^3+Y^3=Z^n at n=7,11,13. Its downstream use is to exclude all placements of these signatures, original signatures reducing to them through exponent divisors, and both complete L003 factor systems. Large complementary repeated-cube primes and unrelated mixed signatures would still require further work.

The previous Bruin audit explicitly did not import its abstract's reductions at 7,11,13. L004 begins at prime 17; no existing local lemma supplies these small cases. The failed unrestricted congruence, isolated-factor, exceptional-prime, and primitive-divisor multiplicity routes do not refute a cited global modular result. No stopped mechanism is being repeated.

Continue the import only if the primary source gives zero nonzero primitive integer solutions, or a complete classification whose exceptions violate the target hypotheses. Check the exact exponent range, signed coordinates, gcd convention, base-one cases, and any unproved or computational qualifications. Fixed-signature finiteness, a bounded solution search, or a conditional assertion would not meet the zero-solution threshold and would be recorded as such.

## Unfinished reasoning saved before detailed source work

Chen–Siksek's paper and its author's computation repository have been located, but no numbered theorem has yet been imported. For a compatible signed statement the three placements map to (X,Y,Z)=(a,b,c), (c,-b,a), and (c,-a,b); each preserves the absolute-value gcd and nonzero coordinates. The exact source scope remains to be checked. This is one bounded audit, with no complete Beal candidate.

## Completed source audit and assessment

Theorem 2 in the identified author manuscript covers all integer exponents from 3 through 10^9. The single cited statement therefore supplies the sought n=7,11,13 exclusions and a substantially larger range. Its definitions and section 12 fix the signed nonzero primitive scope. The [foundation](../foundations/07-chen-siksek-exponent-range.md) records the exact theorem, source version, small-exponent attribution, and computational qualifications. The author's source code was inspected to distinguish a sufficient modular criterion from a bounded search for solutions; the full computation and the earlier small-exponent proofs were not rerun.

[L010](../lemmas/L010-chen-siksek-exponent-range-exclusions.md) proves the applications. For a composite singleton exponent in a divisor extension, the proof first chooses a divisor in S before invoking L002; it does not apply that lemma outside its stated hypotheses. L003's converse remains valid across the full range, including even exponents. The only direct local mathematical inputs are L002 and L003. Other exclusions and failed mechanisms are context, not premises.

The achieved result is zero primitive positive solutions with unrestricted bases throughout the finite exponent range, all three placements, and the stated divisor extensions. This meets the requested threshold and is not an upper bound on solution height. In conjunction with the already assembled Freitas exclusion, repeated-cube primes can now remain only above 10^9 and in the residue class 1 modulo 3. Other mixed signatures remain unexcluded. No complete Beal candidate appears.

Outcome: ADVANCE by a relevant cited mathematical input; exploration turns used 0/3. Close this finite-range audit. The same source has a separate infinite-family theorem involving exponent congruences, so there is a concrete reason to test its overlap with the remaining prime classes. This step does not import that theorem or its density conclusions. The sole current action is in PROGRESS.md.
