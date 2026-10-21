# Fixed direction-field quotient — prepared construction coverage

TARGET: Construct and independently verify the degree-seven quotient of L067's short curve over L070's direction field from its full kernel cubic, including both coordinate maps, kernel, degree and differential.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the dedicated queries, scoped duplicate/failure comparison and inspected source cases in drafts/literature/2026-10-16-conductor389-direction-velu-quotient.md; this exact fixed-instance certificate was not found in checked paths, and novelty is not claimed.
SOURCE_EVIDENCE: Vélu (1971) §§2--3 equations (7)--(13), Remarks 2--3, translation pp.2--4; Sutherland Fall 2025 Lecture 5 Theorems 5.11/5.15 and Remarks 5.16--5.17 pp.5--8; Shumow (2009) §3.1 p.30 and Theorem 3.2.1 with complete proof pp.54--56; exact hypotheses, direct source links and qualifications are retained in the companion source comparison. Direct sources: https://aghitza.github.io/publications/translation-velu.pdf ; https://math.mit.edu/classes/18.783/2025/LectureNotes5.pdf ; https://www.sagemath.org/files/thesis/shumow-thesis-2009.pdf .
COMPARISON: Known quotient/descent and kernel-polynomial formulas cover this characteristic-zero cyclic subgroup over its field of stability; only fixed arithmetic, full witnesses and independent replay need construction. This is known-method reproduction.
GAP: No quotient instance exists here; every coefficient, equation, denominator, projective/kernel, degree and differential check below remains an obligation. Affine-line identification and arithmetic descent inputs are excluded.
REASON: Prepared after literature-only step BSD-2026-10-16-252-direction-quotient-source-comparison; sources supply the algorithm and existence theorem but not exact instance evidence. Direct-source recovery review BSD-2026-10-16-253 approves this unchanged construction scope for a subsequent research invocation.
SCOPE: Only the exact TARGET, over the whole degree-eight D with the full cubic; independent replay and bounded rejection/preservation checks. No minimal model over D, reverse/dual isogeny, affine-line algebra, incidence, norm, global/local descent arithmetic or BSD conclusion.

## Inputs and applicability

Use audited L067/L068/L070, including the complete `/cubic` value
and mixed inverse in `scripts/seven-torsion/compressed-249/direction.json`
and both coordinate transports. The source is Y²=X³−3024X+46224;
D=Q[Z]/h is L070's full direction field. Its geometric interpretation
supplies the stable order-seven subgroup, not a rational generator.
Retain all inverse pairs and every D-basis coefficient. L069 and partial
relation columns are not premises; no cross-notebook input.

Import the precisely cited formulas and projective quotient theorem in
the companion assessment; do not reprove a general isogeny theorem.
Use the kernel-polynomial algorithm with its recorded text qualifications
and check against Vélu's paired convention. Keep the raw short-model
normalization. Any additionally reported long-coordinate map needs
L067's full change, inverse and differential scale. Short normalization
is not a claim about a new minimal Neron model over D.

## Single bounded construction test

Declare one quotient-production stage and one independent replay stage,
each capped at 180 seconds, with an external watchdog and a 128-MiB
new-certificate bound. Timers cover all new arithmetic in their stages;
record actual/required time and bytes even on failure. Reuse audited
data, not partial-column caches. These bounds do not authorize retrying
or repartitioning either stopped column loop.

Save all exact rational coefficients over D for the target and both
coordinate maps. The independent verifier must not import producer
arithmetic. Required evidence: cubic squarefreeness and disjointness
from the short two-torsion cubic; target discriminant nonvanishing
(an inverse witness is suitable); both coordinate identities and the
cleared curve equation over the whole D-function field; normalized
differential identity; exact numerator/denominator coprimality and
x-map degree. Match the map to the full paired Vélu sum, retaining
three inverse pairs and both signs. Distinguish denominator polynomials
in the free source coordinate from constants of D; supply inverse
witnesses for every constant actually divided.

The cited projective quotient must account for O and all six nonidentity
kernel points, with exact local pole/extension checks or equivalent full
algebra witnesses; affine substitution alone is insufficient.
Degree must be seven, with no extra geometric kernel introduced by
cancellation errors. A software degree label is insufficient.
Preserve all originals and full failure reports; include bounded
altered-evidence rejections without changing upstream bytes.
Write a canonical proof only for an actually established result.
A separate critical audit remains necessary after production.

Success supplies a fixed known quotient input only. Stop on the first
cap or failed exact identity and preserve unfinished work. Future use
as an affine-line presentation needs separate coverage and Galois/dual
twist comparison. Incidence/norm, complete units/classes, functions,
local identifications/bounds, Selmer containment, L026 premises,
successful localization, rational membership, divisible Sha and
arbitrary-curve rank comparison remain independent.

## Direct-source recovery review — 2026-10-16

The three direct PDF URLs in SOURCE_EVIDENCE were opened successfully.
Vélu Remarks 2–3 (printed p.4) were rechecked for differential
normalization and conjugation-stable separable descent. Sutherland
Theorem 5.11 and its following field-of-definition paragraph (p.5),
Theorem 5.15 and Remark 5.16 (pp.7–8) confirm subgroup stability
and the full-point versus inverse-pair convention. Shumow Theorem
3.2.1 (printed pp.54–56; PDF pp.59–61) was rechecked for the
existing separable normalized-isogeny hypothesis and short model;
the previously recorded text qualifications remain in force.

This is a source-link repair and separate approval of the already
assessed fixed target, not a new theorem import or instance result.
The companion assessment retains the prior search and duplicate review;
ATTEMPTS/035–036 were checked again and remain stops on column
presentations. No additional discovery search was needed because
the target, hypotheses and source comparison are unchanged.
Full matching Mathlib coverage remains not checked. The continuation
uses audited L067/L068/L070 only and the unchanged bounded test above.
