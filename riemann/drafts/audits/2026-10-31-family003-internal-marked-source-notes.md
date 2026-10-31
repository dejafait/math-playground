# First internal marked Fourier edge — source review working notes

Literature-only review; no mathematical application verdict. The exact
target is the TARGET in
`drafts/literature/2026-10-30-family003-internal-marked-measure-scope.md`.

Primary source: OpenAI September 30, 2026 manuscript, pinned commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`, `build/paper.tex`.
Web retrieval succeeds; direct curl failed DNS. Source is not blocked.

Located the first transformed-product separation in the recursive proof:
`eq:inverse-first-profile`, `eq:inverse-first-separated`, and
`eq:inverse-first-transform-output` (retrieval lines 9818–10048).
It is nine-dimensional and precedes the second Poisson transformation.
This identifies “first” as the source's first transformed product, rather
than the later initialization or the already audited external witness.

The source explicitly supplies the ambient profile, its original masks,
the two column polynomials, a positive weighted-Cauchy output and an
old-label fibre estimate. `eq:inverse-fourier-moment` supplies the stated
weighted Fourier bound; `eq:indexed-coefficient-measure` requires commonness
and an exponent independent of height order. Essential upstream support,
kernel and normalization cases are being checked before a coverage verdict.

Review completed: the necessary fixed-support, normalized radial-kernel,
first-extraction/localization and positive-Cauchy proof cases are accessible.
The completed comparison and source transcriptions are in the assessment;
the precise future test is in
`drafts/literature/2026-10-31-family003-first-internal-fourier-audit.md`.
Its SPECIALIZE verdict approves coverage only, not the mathematical application.
The intended future audit is conditional on terminal arithmetic estimates;
it must not count an ideal already summed inside a child as outer coefficient
mass. No new lemma, script, source-independent estimate or Xi sign is claimed.
