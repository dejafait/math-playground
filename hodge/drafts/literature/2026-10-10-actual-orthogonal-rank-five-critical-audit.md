# Actual orthogonal rank-five construction — critical audit coverage

TARGET: Critically audit L082's actual orthogonal seed realization, full-vector stability and acyclicity.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read complete L082, L080/L081 hypotheses and conclusions, the ready realization assessment and its source notes, histories/188--189 and ATTEMPTS/053; matched the new audit obligations to that coverage and re-inspected the published analytic slice and uniform stability statements/proof cases.
SOURCE_EVIDENCE: Buchdahl--Schumacher, Complex Manifolds 9 (2022), 78--113, Section 2/Lemma 2.5/Proposition 2.6/(2.4), Theorem 5.4 and Theorem 8.1 with its stable-branch continuity proof; reuse Artin (1968) Theorem (1.2), Rond (2018) Theorem 2.1 and Serre GAGA Section 12 Theorems 1--3 as precisely recorded in the realization assessment.
COMPARISON: The inspected vector slice and fixed-metric stability results cover the general analytic bridges, including a neighborhood bound independent of the harmonic direction and the common-scalar convention; they do not verify L082's particular skew restriction, formal gauge or full-vector orbit calculation.
GAP: Independently verify that L082 meets those hypotheses and that its actual-family, cohomology and individual-fibre algebraization conclusions follow; no mathematical audit verdict is given by this source comparison.
REASON: Existing coverage plus the explicit published uniformity check is adequate for one bounded critical audit of unchanged L082, using citations for general results and checking only the seed-specific specializations.
LITERATURE_REASON: The new audit gate required separate scope comparison; this turn reuses the ready realization coverage and narrowly checks the published uniformity and stability directions rather than repeating broad discovery.
SCOPE: L080's actual marked projective K3 S, exact real h, stable spherical E, J_0 and Q; L081's specified compatible formal direction; complete L082. Only critical review and necessary repair within these unchanged hypotheses are covered. No new seed, image, kernel, spin, prescribed obstruction class or transport construction is approved.

## Relevance and decision test

The main gap remains algebraicity of every primitive rational Hodge class,
even on arbitrary fourfolds. The intermediate target is independent audit
of the actual stable acyclic rank-five block claimed in L082. Its plausible
downstream use is the individual J_5 prerequisite in L079's surviving
branch. Other image existence, a common F with the required mixed action,
and transverse transport remain independent unresolved steps.

Retain L082 only if the same vector slice preserves Q, formal gauge
retains the specified first class, analytic approximation supplies an
actual arc, and the full-vector orbit, uniform exact-h stability,
acyclicity and GAGA passages survive. Localize any failure and preserve
valid seed/formal inputs; failure of this proof does not exclude every
J_5. This approval is a source-scope decision, not an audit or existence
verdict, and supplies no new Hodge algebraicity.

## Source comparison and reuse

The primary analytic source is Buchdahl--Schumacher,
*Polystable bundles and representations of their automorphisms*,
Complex Manifolds **9** (2022), 78--113,
[DOI 10.1515/coma-2021-0131, published text](https://d-nb.info/1262812674/34).
Re-inspected Section 2, pp. 83--84 (gauge, projected equation,
uniqueness and obstruction); Theorem 5.4 and its stability argument,
pp. 93--94; Theorem 8.1 and the stable continuity branch, pp. 103--106.
The latter has epsilon depending only on d_0, unlike Section 7's
ray-dependent bound. Theorem 5.4's stability equivalence assumes
polystability of the actual bundle; Theorem 8.1 supplies that preceding
bridge. Theorem 3, p. 79, summarizes the combined criterion and specifies
quotienting by common scalars. These statements use a fixed compact
Kahler metric, without an integral-polarization requirement.

Reuse the exact Artin/Rond and GAGA statements and access qualifications
in [the ready realization assessment](2026-10-10-orthogonal-seed-realization-and-stability.md).
No new Artin or GAGA hypothesis is introduced by the audit target.
Original Artin proof access was limited; its theorem statement and the
matching Rond formulation were inspected previously. This review does
not upgrade that record to an original-proof read. Grauert's corrected
semicontinuity coverage is available there, but L082's asserted actual
acyclicity uses stability, duality and RR instead; an obstructed central
section is not by itself sufficient. General cited theorems should be
imported, not reproved. Checking their application is the reason for the
separate audit.

## Exact audit obligations, not conclusions of this review

1. Check the dual direct-sum metric, parallel isometric complex-linear
   Q-transpose, invariant Hodge operators and the skew implicit-function
   restriction against the actual Proposition 2.6 complement. Check
   finite-dimensional analytic equations and actual-family regularity.
2. Check every formal gauge order, its skew Green inverse, preservation
   of the first cohomology class and recursive comparison with the
   analytic correction. Apply Artin only to finite convergent equations;
   neither formal-series convergence nor analytic formality is assumed.
3. Check every full-vector weight and nonzero actual-arc component,
   closedness including higher-order coordinates and stabilizer modulo
   common scalars. Apply Theorem 8.1 before Theorem 5.4 at unchanged h.
   Principal simplicity or the orthogonal torus alone is insufficient.
4. Check integral invariants, actual-fibre stability/section vanishing,
   duality/RR and GAGA local freeness, form and orientation. Algebraizing
   individual fibres is distinct from algebraizing the disc family.

Essential inputs: L080, L081, L082; L052 enters through L080 only.
L079 is motivation, not an existence premise. No cross-notebook input.
The ready assessment and history/189 contain the same proposed bridges;
this is their separate audit approval, not an independent duplicate
construction. ATTEMPTS/053 stops the earlier bounded index mechanism,
not this deformation mechanism. Preserve ATTEMPTS/043,/045,/053, the t=2
branch and the parked flat (-10,-17) blocker. No repeated index test or
reopening of those dependent routes is authorized here.

Full matching Mathlib coverage and supporting analytic/GIT declarations:
not checked; no absence or formal-verification claim is made. No lemma,
mathematical script, DAG or PROOF.md change was made in this literature
turn. A future audit must inspect the complete relevant proofs, including
any essential input passage whose use needs checking.
