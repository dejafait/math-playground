# Mixed seventh-power conditional character audit

This is the single target screened by the ready SPECIALIZE [assessment](literature/2026-10-04-mixed-seventh-reducible-character-audit.md). The main gap is uniform zero primitive solutions over the residual Beal signatures. The intermediate target is conditional coverage of the reducible sector at the specified prime over 29; its plausible use is supplying the two linear comparison factors in L016. Irreducible-packet exhaustion, the original representation hypotheses, the four curve parameters and the pure-field/global descent are separate unresolved interfaces.

The pass test requires all finite-flat scalar inertia types, both real-place signs, the character conductor bound and the Frobenius value. An omitted type or additional trace stops reliance on this sector. Repeating the finite resultants does not address it. No prior notebook lemma proves this restriction; the earlier local-solubility and Lucas multiplicity failures concern different mechanisms. The exact claim is already printed in Chocian's Section 6.2, so this is a correctness reproduction, not a novelty claim. The ready assessment is reused unchanged; reopening its already-read primary statements for the proof audit is not a new literature search.

## Reasoning saved before verification

Let F=Q(sqrt(5)), epsilon=(1+sqrt(5))/2, and rho^ss=psi plus chi_7 psi^(-1), under exactly the screened hypotheses. Away from 7, the two characters have equal Artin-conductor exponents. Additivity for the semisimplification and its conductor bound give 2 a(psi) <= 3 at 3 and 5, hence a(psi) <= 1.

At the inert prime over 7 the residue field is F_49 and the absolute ramification index is one. A scalar character of the full local Galois group is invariant under Frobenius conjugation; its tame inertia values therefore have order dividing 48. Their minimal field of definition has degree at most two over F_7. Raynaud's finite-flat Jordan–Hölder digit theorem, after strict henselization, then gives the four exponents 0,1,7,8 of the level-two fundamental character, rather than prematurely assuming values lie in F_7.

The unit u=epsilon^8=13+21 epsilon is positive at both embeddings, is 1 modulo 3(sqrt(5)), and is -1 modulo 7. The principal-idele product formula forces psi(rec_7(u))=1. Its value for a level-two digit type (r0,r1) is (-1)^(r0+r1), excluding exactly the mixed types. One of the two global characters can consequently be selected unramified at 7, with finite conductor dividing 3(sqrt(5)); both real places must still be included.

For q=(29,sqrt(5)-11), alpha=6-epsilon has norm 29 and generates q. The element

\[
beta=alpha^2/epsilon^2=85-48 epsilon
     =1+3 sqrt(5)(8 epsilon-12)
\]

is positive at both embeddings, has ideal q^2 and is 1 modulo the finite conductor. A second principal-idele product formula gives psi(Frob_q)^2=1. Since chi_7(Frob_q)=29=1 modulo 7, the trace is in {2,-2}. This direct ray relation needs neither the full ray-group structure nor its claimed exact order at q. It treats arbitrary real-place signs uniformly.

The supporting inputs are the precisely read Raynaud Theorem 3.4.3/Corollary 3.4.4 and Milne Chapter V reciprocity statements named in the prior assessment. The exact checks concern only quadratic-ring identities, residues, norms and the four digit types. No global Beal exclusion follows from this conditional argument alone.

## Completed audit

The pass criterion is met by the full proof in [L017](../lemmas/L017-mixed-seventh-reducible-character-traces.md). Scalar Frobenius invariance is used before Raynaud to justify the field-of-inertia-values degree bound; all four digit types are retained until the global unit test. The conductor estimate applies to the semisimplification, not to just one arbitrarily selected factor. The principal ray relation includes both real places, so it does not overlook odd character signs. At the terminal prime the cyclotomic determinant is 1, giving exactly the required trace inclusion. The asserted C_4 x C_2 ray group and exact nontriviality of the prime's class are unnecessary for this inclusion and are not established by this audit.

The [standard-library checker](../scripts/mixed-seventh-certificate/check_characters.py) passed, with [saved exact output](../scripts/mixed-seventh-certificate/character-results.json). It verifies the two global witnesses, their norm and residue identities, positivity using rational intervals, inertness and digit filtering. It cannot check the general finite-flat or reciprocity theorems. No L016 point counts or resultants were rerun, and no blocked endpoint or external program was retried.

Recorded **RESEARCH / ADVANCE / REPRODUCTION**, with exploration usage 0/3. This is a local correctness gain for a printed conditional claim, without progress beyond the checked literature. The required global zero-solution bound is still missing. The character part now permits reliance under explicit representation hypotheses; original-solution applicability, irreducible packets and parameter coverage remain unresolved. The [pending parameter-bridge assessment](literature/2026-10-04-mixed-seventh-parameter-bridge.md) records changed hypotheses and remains REVIEW_REQUIRED; no second mathematical attempt or source search on that target occurred here.

## Mathlib

Coverage of the exact conditional trace restriction and its supporting finite-flat and class-field inputs: **not checked**. The source claim and named supporting theorem links are preserved in the prior assessment and L017; they are not formal verification.
