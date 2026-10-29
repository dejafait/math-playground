# Step 523 — CM torus period / tame normalizer source comparison

Literature-only review, 2026-10-27. The target is the exact TARGET in
`drafts/literature/2026-10-27-torus-period-tame-normalizer.md`.
No factorization or new moment identity is proved here.

## Primary sources actually inspected

**John Voight, Quaternion Algebras**, GTM 288, Springer (2021),
Chapter 30, published chapter pp.541–567,
<https://doi.org/10.1007/978-3-030-56694-4_30>.
Read the publisher HTML, §§30.5.1–30.5.3 and §§30.6.1–30.6.12,
including the complete proofs of Proposition 30.5.3 and Lemmas
30.6.3/30.6.9. The chapter PDF was also retrieved; theorem comparison
uses the HTML, with no reliance on its missing equation images.

The local base R is a complete DVR with finite residue field; S is a
quadratic order in a separable quadratic F-algebra. Proposition
30.5.3(a) gives one GL_2(R)-conjugacy class of optimal embeddings into
M_2(R). Part (b) gives one normalizer-conjugacy class for the maximal
order of a quadratic field in a quaternion division algebra; its proof
uses uniqueness of the valuation order. For a standard split Eichler
order of level pi^e, e>=0, (30.6.2) describes its normalizer modulo
F^times O^times using the matrix (0,1;pi^e,0). Lemma 30.6.3 normalizes
optimal embeddings; Lemma 30.6.9(a) classifies them by the parameter
modulo pi^e, and (b) describes the normalizer action when the quadratic
discriminant is a unit or e=0. These statements do not require odd
residue characteristic. Part (c) has an additional lifting condition
when the discriminant is not a unit and e>=1. No general transitivity
assertion in that latter case is imported. The proofs distinguish the
three unit-entry cases and the unit/nonunit-discriminant cases.

**Michele Fornea, Plectic Heegner classes**, arXiv:2603.28327v2,
13 April 2026, <https://arxiv.org/html/2603.28327v2>.
Read (2), the level definitions at the start of §2.2, (22), Lemma 4.7,
Theorem 4.13 and Corollary 4.15 statements, (63), Proposition 4.18
and its full proof, Corollary 4.19 and proof, and §4.3–4.4 through the
full proofs of Theorem 4.22 and Corollary 4.24. Construction hypotheses
and the earlier vanishing/projection proof coverage are reused from
L123's step-515 audit and L124's step-520 audit.

The tame level in K_m is the Eichler group K^circ(n^+); only the
p-part acquires the deep unipotent level. Proposition 4.18 acts
simultaneously on the finite coordinate and the S-coordinates of the
specialized Abel–Jacobi map. Its proof tracks vertex lifts and local
kernel constants using Lemma 4.7 and Theorem 4.13. Equation (63) has a
diamond-invariant domain. Theorem 4.22 uses U_{psi,h}, the induced
p-action and the constant in (66); it is not raw measure invariance.
Equations (67)–(68) express the complete cap product over the torus
quotient, with the stated character and stabilizer. These results
retain the source's conductor, residual and incoherence assumptions.
They do not explicitly state L124's proposed norm-moment replacement.

**Gonzalez–Rotger**, *Non-elliptic Shimura curves of genus one*,
author manuscript, Appendix, pp.14–18, Theorem 5.4 and Lemma 5.10,
<https://web.mat.upc.edu/victor.rotger/docs/ShimuraGenusOne.pdf>.
Reused step-518 comparison and rechecked Lemma 5.10 with its local
proof cases. Its square-free Eichler-level scope still prevents direct
import at squared tame level or deep p-level. Voight supplies a
different local input; it does not retroactively enlarge this lemma.

## Applicability and the difference still to prove

The following are obligations for the next attempt, not results of this
review. The conductor-one assumption in L123/L124 must first be matched
to the maximal CM order in each tame Eichler order using source (2).
At split bad tame primes the allowed exponents are one or two and K is
unramified; check the unit-discriminant hypotheses before invoking
Voight 30.6.9(b). At good tame primes use the maximal-order comparison,
including primes ramified in K and residue characteristic two. At
division primes use 30.5.3(b). Do not use 30.6.9(b) for a ramified
quadratic order at positive Eichler level. The conductor-unramified
condition must account for why that case is unnecessary here.

Then compare the fixed embedding and its conjugate, and justify the
centralizer/adelic assembly needed for w=psi(a)W with a_p=W_p=1 and W
normalizing the actual tame level. No such assembly is performed now.
Keep the original n and indexed h_t: a change of n requires an explicit
comparison with L124, rather than silently replacing its w.

For the period comparison, the required object is the complete
q_tau=log_p N_tau integral, not just the source's individual f_tau
integral or a shallow CM divisor trace. Verify that the translated
summands define functions on the same torus quotient, with the actual
stabilizers. Rational torus representatives may have a nontrivial
p-component: use the simultaneous rational action, its p-cell change
and full kernel, before specialization and descent. Prove the
diamond-invariant projection domain of both complete moments. Account
for both local CM orientations in the norm kernel; Theorem 4.22's
aligned CM tuple must not be silently applied to a changed tuple.

This is a finite known-source specialization task with explicit
remaining hypotheses to check. No essential source is inaccessible.
An explicit failed local or projection hypothesis is an admissible
negative result; further scalar/eigenvalue claims are outside this gate.
No whole-source reproof is needed: cite the imported theorems and prove
only this assembly and norm-kernel comparison in a later research turn.

## Search, duplicates, failures and decision

Queries on 2026-10-27: “CM toric period Atkin Lehner normalizer optimal
embedding Eichler order non squarefree level complex conjugation”;
“Plectic Heegner classes torus translation normalizer”; “CM points
complex conjugation arbitrary level Atkin Lehner”; “toric normalizer
Eichler period”; “optimal embeddings normalizer split Eichler order
prime power”. The inspected Voight chapter is the new relevant lead.
Longo's square-free-level CM discussion and other higher-level search
hits were not imported. Search failure establishes no novelty.

Local comparison used L123's hypotheses/definitions, L124's complete
argument, and the step-518 source record with its ATTEMPTS/003/004/030/
058/059 comparison. ATTEMPTS/060 and step 522 preserve the selected
branch/full-Hecke-fiber failure. Neither that failure nor the norm's
unchanged logarithm tests the present torus-period replacement.
L125 is motivation only and remains unaudited.

Decision: SPECIALIZE. New primary coverage removes the need to rely on
the square-free classical conjugation lemma for the tame prime-power
input. It approves a bounded attempt on the saved target, not its
truth. Continue only on a complete projected equality or a precise
failed hypothesis; abandon the proposed replacement if such a failure
cannot be repaired within the saved hypotheses. Do not substitute a
full Hecke fiber. W's scalar action, R, finite local membership,
rational Kummer membership, nonvanishing and the general BSD gap remain
independent. Mathlib coverage of the full replacement was not checked.
