# Kraus divisibility audit — 2026-09-25

This records one focused source-and-application step, not a candidate resolution of Beal.

## Starting state and relevance

Read the shared rules and prompt, local goal and checkpoint, whole overview, and local DAG before selecting this step. The existing tracked and untracked work is preserved. The primary target on Mauldin's UNT page still agrees with the local positive-integer formulation; the nominated AMS endpoint again failed retrieval.

The gap addressed is the repeated-cube family at complementary primes p congruent to 1 modulo 3. L004 does not exclude those exponents; L003 retains two exact factor systems. The intermediate target is to establish from Kraus's original numbered result that every nonzero primitive integer solution of a^3+b^3=c^p, at prime p >= 17, has 3 dividing c. Its downstream use would be to eliminate system I of L003 without a residue-class restriction on p, concentrating this family on system II. Emptiness of that second system and other residual signatures remain unresolved later steps.

The discriminating test is the source's exact exponent range, primitivity and sign conventions, normalization, and any historical modularity assumption. Import only a conclusion justified for the actual auxiliary triple. If the original statement does not support this range, narrow or abandon the application. A necessary divisibility condition is sufficient for this intermediate target; it must not be presented as the zero-solution theorem required for the whole family.

## Redundancy and prior failures

The original Kraus result is quoted but deliberately not imported in the previous audit. L003's elementary argument allocates powers after choosing a branch; it does not select a branch. Attempt 001 stops unrestricted congruences alone, while Attempt 002 stops rejection of an isolated quadratic factor. A divisibility condition proved using global modular information is a different mechanism and is not ruled out by either failure.

## Reasoning saved during source retrieval

Located the publisher record for Alain Kraus, *Sur l'equation a^3+b^3=c^p*, Experimental Mathematics 7 (1998), no. 1, 1–13, DOI 10.1080/10586458.1998.10504355. Its abstract retains p >= 17 and a historical Taniyama–Weil assumption. The original numbered divisibility statement still needs to be read. The notebook already records the full-modularity theorem in foundations/02-standard-results.md; its applicability must be checked rather than assuming the historical condition away.

Search results also attribute c congruent to 3 modulo 6 and v_2(ab)=1 to Kraus. These stronger restrictions are unverified leads at this point. No theorem is imported from a search snippet, and the finite exponent checks mentioned in the abstract are outside this step.

## Completed assessment

The original full text could not be retrieved. Publisher and Project Euclid endpoints, the author's page, and archive paths were checked; none supplied the original theorem. This limitation is preserved rather than claiming an original-proof audit. The mathematical input was instead established as a precisely cited published result: Bennett–Chen–Dahmen–Yazdani, Proposition 7, restricted to its explicitly attributed Kraus prime range, with Freitas's Theorem 1 as corroboration. The full statements, exponent qualifications, and context were read in the accessible published papers. The exact references and source roles are in [the foundation](../foundations/04-kraus-divisibility-restriction.md).

The symmetric v_2(ab)=1 formulation resolves the labeling issue: exactly one cube base has valuation one, and that base can be named a after swapping. One must not apply an implicitly normalized statement separately to both labels and manufacture a contradiction. The modern restatements are unconditional; full modularity over Q is an already recorded named theorem. No smaller-exponent extension, computational exponent cutoff, or new residue-class exclusion is imported.

[L005](../lemmas/L005-kraus-ramified-branch-restriction.md) proves the application. The condition 3 dividing c forces 3 dividing a+b, and L003's converse excludes every complete system-I datum. Oddness of c forces u,v odd in II. The identity q=s^2-3ab modulo 4 gives v congruent to 1 modulo 4, and L003's prime-support restriction gives v congruent to 1 modulo 3. Their combination is v congruent to 1 modulo 12. The reconstruction and the valuation of s^2-d^2 were checked directly, with 3 dividing u still allowed.

The intermediate zero-solution threshold for branch I is met at every prime p >= 17, including the complementary residue class. The full zero-solution threshold remains unmet because the constrained second system is still unexcluded there. The growing positivity interval remains a size relation, not an upper height bound. This is an application of an established global theorem, not literature novelty or a complete Beal candidate.

Outcome: ADVANCE; exploration turns used without an advance or informative negative result: 0/3. The source-and-application step is complete with the original-source access limitation stated. The new global restrictions make a bounded local feasibility test of the surviving system relevant: the old unrestricted local witnesses need not satisfy them. Such a test can determine whether these restrictions support any obstruction at 2 or 3, without reviving the already refuted unrestricted sieve. The sole concrete current action is in PROGRESS.md.
