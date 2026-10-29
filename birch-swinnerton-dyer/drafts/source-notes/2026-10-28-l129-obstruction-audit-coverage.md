# Step 537 — source coverage for the L129 obstruction audit

2026-10-28. Literature-only comparison; no mathematical audit,
new lemma, calculation or repair was performed.

The main gap is rank/order equality for arbitrary elliptic curves
over Q. The intermediate target is a separate critical audit of
L129's proposed covariant pushdown obstruction. Its downstream use
is to decide whether the unchanged covariant tower can support L128's
relation transfer; it constructs no scalar, global point or strict
Selmer class. Rationality, nonvanishing, second-factor finite local
membership and applicability to arbitrary curves remain independent.

## Primary source and exact scope

Michele Fornea, *Plectic Heegner classes*,
[arXiv:2603.28327v2](https://arxiv.org/html/2603.28327v2),
13 April 2026. The versioned abstract/submission history was checked;
it lists v2 and describes the revision as correcting Assumption 1.5
and adding a reference. This is version evidence, not an assurance
that every convention or proof is correct.

Newly inspected locations: levels immediately after (6); Section
2.1.2, Definition 2.3 and (15); tower levels, (16)--(18), Definition
2.4; Section 2.2.1 including Definition 2.8 and all proof cases of
Proposition 2.9 (good/tame operators, diamonds, both intermediate
p-level quotients); Corollary 2.10; (21); Remark 2.12; Proposition
2.14 with its proof and Corollary 2.15; Section 2.4 through Corollary
2.23, Proposition 2.24 and the first identification in Proposition
2.25's proof. These are theorem/proof reads, not search snippets.

Source facts relevant to the audit: the local level is the projective
image of upper-unipotent congruence matrices; (15) gives the p-U
representatives. Jacobian action is declared covariant. Proposition
2.9 intertwines coefficient pullback. Equation (21) defines the
ordinary projector. Remark 2.12 uses cohomology and its duality with
homology. Section 2.4 defines the trivial-finite-diamond homology
inverse system under forgetting pushdown; Lemma 2.22 states its
finite-level base-change isomorphism. Its proof uses U and a
cross-level correspondence. It does not explicitly state L129's
covariant pushdown identity. These passages specify the comparison
to audit; they do not identify the two labeled homology actions.

The [versioned PDF](https://arxiv.org/pdf/2603.28327v2), printed
pp.17--18 (zero-based pages 16--17), supplies the control diagram
missing from the HTML. PDF text places forgetting pushdowns on the
horizontal arrows, U_S on the vertical arrows, and names the
cross-level map [K_m eta_{varpi_S} K_{m+1}] in the immediately
preceding sentence. Both endpoint modules and the base change are
printed there. Screenshot calls again returned no visible image;
no fresh visual verification is claimed. The text plus the theorem
statement suffices to expose the map labels for a later audit;
it does not determine an unprinted transported action.

## Reused comparison coverage and specialization obligations

Reuse the inspected primary inputs in
[step 535's source record](2026-10-28-l128-covariant-transfer-coverage.md):
Milne, *Jacobian Varieties* (corrected 12 June 2021), Theorem 2.5,
pp.7--8, Proposition 6.1/Corollary 6.3, pp.19--20; Milne, *Abelian
Varieties*, v2.0 (16 March 2008), I Theorem 2.9, p.14, Remark 10.7,
p.45; Sertoz--Ouaknine--Worrell, *Computing transcendence and linear
relations of 1-periods*, arXiv:2505.20397v1 (26 May 2025),
(4.5.54)--(4.5.55), (7.3.29)--(7.3.36), (7.4.37)--(7.4.43).
Direct primary links and the integral rather than merely rational
comparison are recorded there. Their hypotheses and versions have
not changed; no repeated source extraction is needed.

The proposed application retains smooth proper characteristic-zero
curves, empty markings/punctures, componentwise homology and integral
pushforward/transfer. A chosen complex embedding is available; no
good-reduction-at-p hypothesis or rational basepoint is inserted.
The next audit must check that L129 uses precisely these maps and
cycle multiplicities, including ramification/compactification, before
using the comparison on its Z_p lattices. A standard comparison is
imported by citation; only the claimed local specialization needs
verification. No reproof of Jacobian comparison or Hida control is
called for. L123's original conductor/residual/integral-CM/incoherence
hypotheses remain; the local calculation does not silently establish
new admissible arithmetic data.

## Comparison, duplicates and bounded test

Local reads: complete L129, L123 hypotheses, step-535 comparison
record, ATTEMPTS/063 and histories 535--536; targeted searches in
ATTEMPTS/061/062 and the step-534 critical audit. The old bad-U/full
algebra shortcut and inverse-diamond duality failure are distinct
from the new transition claim. This step approves scrutiny of the
claim, rather than restating a stopped repair as new progress.

Web queries: `"Plectic Heegner classes" "covariant" homology control`,
`"Plectic Heegner classes" "Lemma 2.22"`,
`"2603.28327" "homology" "control"`, and
`"2603.28327" erratum correction`. Results did not supply an inspected
independent theorem proving this exact obstruction or a correction
resolving its convention issue. Secondary indexing/conjecture pages
were not used as mathematical evidence. No novelty, absence or
exhaustive erratum-search claim follows. No additional unread lead
is essential to the bounded audit.

Decision: SPECIALIZE. The strongest relevant imported control
statement concerns its specified M_m^bullet, not an arbitrary
covariant C_m. The source material is sufficient to audit L129's
conditional comparison without proving the unspecified identification.
The exact next target is the assessment's COVERED_TARGET.

Continue/abandon test for that later turn: independently verify the
claimed degeneracy map, the complete cycle multiplicity, transfer
on integral homology, U-invertibility on the stated ordinary lattice,
and the nonzero-target/surjectivity comparison. Preserve original
labels, p/tame levels, full CM list/n/W, N/P/M, R_0/I and complete
invariant domains. Accept only the resulting restricted obstruction
if these checks pass; otherwise correct or withhold its failed part.
Do not infer a contradiction in Fornea's theorem without establishing
its own action conventions. No alternative transition, coefficient
algebra or repair attempt is covered. Mathlib remains not checked.
