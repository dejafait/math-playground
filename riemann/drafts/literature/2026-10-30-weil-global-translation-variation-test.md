# Global translation variation: proposed bounded mathematical test

TARGET: Attempt a global bound sup_{0<h<h0} ||Eu(.+h)-Eu||_1/h<infinity under L520's fixed-model hypotheses, using its localized inverse and L513's renewal representation while retaining every signed term.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed global-BV source comparison in 2026-10-30-weil-nullvector-bounded-variation-coverage.md: searches for logarithmic-Laplacian BV/W1,1 eigenfunctions, geometric-stable gradients, zero-order BV regularity and translation quotient measures found no adequate full-model bound. Scoped Weil assessments/stops and L513/L515/L516/L520 contain no duplicate global closure.
SOURCE_EVIDENCE: Galerne (2016), https://www.cambridge.org/core/services/aop-cambridge-core/content/view/83627D38EAB49283AE917366027E8BE7/S0001867816000604a.pdf/random_fields_of_bounded_variation_and_computation_of_their_variation_intensity.pdf, Section 2 Lemma 1/Theorem 1 pp.951–953 with proofs; Kulczycki–Ryznar https://arxiv.org/pdf/1307.7158v1 Theorem 1.1/Proposition 6.7/Example 7.2; Jarohs–Kassmann–Weth https://arxiv.org/html/2311.15337v2 Theorems 1.5/5.1 and A3_2. Full citations, hypotheses, proof cases and exclusions are in the completed comparison; L520 (4)–(14) and L513 (3)–(4) supply existing local tools.
COMPARISON: The global difference-quotient characterization is known and must be cited. Harmonic gradient estimates and continuity theorems do not supply the requested bound for this signed translated equation. Only the full-model closure beyond those inputs is proposed for investigation; no originality is certified.
GAP: Prove a global uniform quotient bound from the existing model inputs, or isolate a precise boundary/translate obstruction to the proposed localization-and-renewal closure; no finite variation, smooth forcing, integrable gradient or trace-error derivative may be assumed.
REASON: This is a concrete missing estimate identified by the completed source review, not a new theorem already derived there. The separate literature-only recovery review on 2026-10-30 confirms the reused coverage and direct primary URLs; the exact saved target is approved for one bounded mathematical attempt next turn.
SCOPE: Fixed 0<a<A, I=(0,2a), real normalized nullvector of the complete L516 model, nonzero left trace, 2a>log(2), and L520's excluded direct reflected-endpoint collision; all atoms including cutoff equality, nu_rho, c=log(2pi) and signed pole retained. No family-uniform estimate or actual-Weil identification is presumed.

The main gap is L516's signed eigenvalue-relative cancellation and
actual-Xi all-degree positivity. This global variation estimate could
enable individual signed Stieltjes correlations for its prime terms;
it would supply no sign or factor vanishing with the eigenvalue.

Use L513's normalized renewal representation, L515's bounded continuous
zero extension, L516's full weak equation, and L520's audited local
inverse/commutator estimates. Cite Galerne's deterministic theorem
for why the displayed threshold is the desired finite-variation
criterion, rather than reproving the criterion. Its application to
this u is precisely the unproved part. The complete source comparison
is [here](2026-10-30-weil-nullvector-bounded-variation-coverage.md).

One bounded attempt should investigate whether interior localization
and endpoint renewal control yield a closed inequality for the global
quotient norm. An inequality with a strict absorption coefficient
below one and an h-independent finite error would pass the test.
Every constant depending on an interior cutoff must be reconciled
with the endpoint region. Generated translated images may coincide;
smoothness or a finite partition avoiding every image is not assumed.
L520's pointwise little-o is not a derivative estimate. Do not infer
contraction merely from decay of a Fourier multiplier or replace the
complete signed model by a positive one.

Continue only on a proved closure or a quantitatively sharper
independently testable remainder. Otherwise retain the exact term
preventing closure and park this implementation. An estimate restricted
away from the endpoints, a logarithmic modulus, or the assertion BV
itself without a model argument does not pass. Failure of an absolute
estimate is not a counterexample to BV or RH.

Nullvector existence, nonzero trace, imported source realization,
the Stieltjes specialization, arithmetic cancellation, branch rates,
collars and Xi transfer remain unresolved. No mathematical calculation
or new lemma is contained here. Mathlib matching remains unchecked.
No cross-notebook input is used. Separate source-gate approval completed on 2026-10-30. Recommend proof_attempt/development:
the difficulty is global closure of existing local inverse/renewal
estimates with signed shifts, not another automatic source import.

## Separate source-URL recovery review (2026-10-30)

The saved target and scope are unchanged. The publisher DOI failed in
the browser, but the direct publisher PDF above opened successfully.
Rechecked Galerne Section 2, pp.951–953: Lemma 1 assumes finite
directional variation; Theorem 1 requires L1 on an open domain and
characterizes finite variation by a finite quotient liminf. Its proof
uses distributional testing and measure compactness. Thus it supplies
the criterion, not the missing estimate. The proposed use has domain R
and direction 1; L515 supplies integrability. No reproof is needed.

Also reopened the versioned arXiv sources and rechecked
Kulczycki–Ryznar Theorem 1.1 and Jarohs–Kassmann–Weth Theorem 1.5:
the former assumes nonnegative harmonic data and the latter concludes
continuity. The prior detailed comparison and its proof-case readings
remain the coverage record; no renewed mathematical conclusion is claimed.
The kernel-BV and harmonic-gradient scope stops remain in force.
No source blocker remains for the proposed bounded test. This is a
process repair and separate approval, not an advance toward global BV.
No new lemma, mathematical script or full-model bound was produced.
