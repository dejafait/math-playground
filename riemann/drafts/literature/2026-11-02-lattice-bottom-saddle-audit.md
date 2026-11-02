# Conceptual audit of the fixed-lattice bottom saddle

TARGET: Critically audit C663b's fixed-lattice signed-saddle lower bound and paid-arc conclusion, including C663a's inherited contour remainder and all kernel frequencies.
CHECKED: 2026-11-02
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the unchanged 2026-11-02-localized-logarithmic-joint-moment.md searches and scoped lattice/endpoint/full-circle failure comparison; on 2026-11-02 retrieved the four direct primary-source URLs below and located the exact cited theorem statements and essential proof cases. No new novelty search was needed for this unchanged audit target.
SOURCE_EVIDENCE: Rechecked Brunault--Zudilin Proposition 1.4 and its three complex-analytic cases p.6, polynomial formula Proposition 1.5 p.7 (https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf); Issa--Lalin arXiv:1203.5379v1 Remark 3.8 and Theorem 4.1/proof p.7 (https://arxiv.org/pdf/1203.5379v1); Howell--Mathews online Sections 8.1 Theorems 8.1.5/8.1.7 and proofs (https://complexanalysis.org/web/sec_residue-thm.html), 6.2 Theorems 6.2.18--6.2.19 and proofs (https://complexanalysis.org/web/sec_contour-integrals.html), accessed 2026-11-02. No new source theorem is required.
COMPARISON: Standard sources cover the residue identity, contour absolute bound, polynomial logarithmic integrability and complete spatial root formula; the new fixed-spacing signed Gaussian limit, all-frequency tail and rate comparison require checking the written specialization, not importing a general asymptotic theorem.
GAP: Independently validate C663b's saddle existence, exact finite-product normalization, contour orientation, signed Gaussian convergence, all-frequency remainder, inherited top/side estimate and fully paid comparison; source manuscripts and general integer support remain outside this audit.
REASON: The direct-URL defect has been repaired and the primary hypotheses rechecked in this separate literature-only approval step. SPECIALIZE remains appropriate for the exact audit target: sources cover standard tools, while the finite-product signed limit and costs require independent mathematical scrutiny. This approves source readiness only, not C663b.
LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this assessment; this bounded source retrieval repairs that process issue for the unchanged target, without repeating discovery or invoking the mathematical audit.
SCOPE: Exactly TARGET for n=6q+3>=9, x=-5/4, full t_j=j/n, spacing 27/(10n), original unit residues, M=n/3, conjugated angle and normalized means; retain every spatial moment and kernel frequency. No general-support extension, effective-onset claim or Xi transfer is covered.

## Evidence to reuse and exact critical claims

The prior ready assessment is
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`.
Its primary theorem statements and boundary-root qualifications remain
unchanged. The supplemental contour source is recorded in L663 and
C663a with exact theorem numbers. The canonical audit subject is
`lemmas/C663b-lattice-bottom-saddle-paid-arc.md` and its rational
certificate is `scripts/one-sided-hankel/lattice-bottom-saddle.json`.

Essential local inputs are L663's admissible lattice, finite rectangle
and product error; C663a's pointwise top/side exponent and original
bottom isolation; L658's complete-polynomial localization and nonzero
slices; and L661's general squared-residue diagonal envelope. C663a
itself is unaudited, so inspect its load-bearing proof and exact
aggregation rather than trusting its summary. L659's differently
spaced resonant lattice and L660's monomial stop are contrasts only.

The critical analytic point is the transition from the fixed continuum
saddle to a positive signed finite-product limit, with an O(1) residual
phase, a uniform Gaussian tail and the complete geometric kernel.
Check that the shortened vertical sides inherit a pointwise bound,
not merely a bound on a cancelled sum; that their error is small
relative to the proved saddle scale; and that the full spatial root,
squared-residue diagonal and n^(-2) arc measure costs are included.
The target is to validate or repair these precise claims, with every
failure preserved. No theorem about arbitrary integer support follows.

No additional literature is proposed merely for balance. This assessment
reuses the prior source evidence for a newly named audit; supervisor
approval must be separate from the completed research. The appropriate
subsequent task is proof_audit/conceptual_audit at deep_research/xhigh.

Mathlib coverage remains the supporting univariate Mahler-measure
theorems named in the prior assessment; a full matching signed-lattice
theorem has not been checked. Unknown coverage is not absence.

## Direct-source recovery and approval — 2 November 2026

The four URLs in SOURCE_EVIDENCE were retrieved successfully. This is a
citation/readiness repair, not a new mathematical advance. The prior search
assessment and the endpoint/full-circle stop evidence remain in force.

**Contour tools.** Howell--Mathews, online edition, Section 8.1,
[Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html):
the residue identity requires a positively oriented simple closed contour,
analyticity on its boundary and interior apart from finitely many interior
isolated singularities. The simple-pole formula is the limit of
(z-z_0)f(z). Read the excised-circle proof and pole formulas. Section 6.2,
[Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html)
requires continuity; the contour bound uses its length and a pointwise
modulus bound. Read both proofs. Applicability to the old and shortened
rectangles still requires the local pole census, orientation and boundary
clearances. A bound on a cancelled sum cannot replace a pointwise side
bound. These sources do not supply C663a's exponent or C663b's signed limit.

**Spatial roots.** Brunault--Zudilin, *Many Variations of Mahler Measures*,
ISBN 9781108794459, publisher excerpt,
[Proposition 1.4 p.6 and Proposition 1.5 p.7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
Read the outside, inside and unit-modulus cases in the complex-analytic
proof. The boundary case uses an indentation with vanishing logarithmic
error. Proposition 1.5 gives the complete nonzero-polynomial root formula,
including leading coefficient and multiplicities. The alternate sampled
real-analytic argument is not used at boundary roots. The local audit must
retain every root and denominator cost and verify the nonzero slices;
these identities provide no uniform paid-arc bound for the changing family.

**Integrability.** Issa--Lalin, *A generalization of a theorem of Boyd and
Lawton*, version 1, 24 March 2012,
[Remark 3.8 and Theorem 4.1 with proof, printed p.7](https://arxiv.org/pdf/1203.5379v1).
The theorem assumes nonzero complex multivariate polynomials. Its s=1
case supplies ordinary logarithmic integrability. Read the small-value
and complement splits in both proof parts; Remark 3.8 concerns fixed
multivariate polynomials. It supplies no degree-uniform control for this
sequence. Rational denominator clearing, nonvanishing and the denominator
logarithm remain local obligations. No uniformity from the earlier
univariate corollaries is imported.

No new lemma, mathematical script, asymptotic derivation or certificate
replay was performed. The exact TARGET and its fixed-lattice SCOPE are
now approved for the next conceptual audit. It must either validate the
stated signed lower bound and fully paid excess, or identify a precise
repair/withdrawal point. General support and Xi realization remain open.
Mathlib coverage is reused with its existing qualifications, not refreshed.
