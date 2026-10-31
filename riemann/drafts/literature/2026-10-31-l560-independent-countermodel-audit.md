# Nomination: independent audit of the fixed reciprocal-density countermodel

TARGET: Independently audit L560's fixed reciprocal-density countermodel, checking the bilateral transform, conjugate-pole signs, matching at zero, global curvature bounds and exact negative polynomial jet.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the unchanged fixed-model assessment and its parent discovery's exact reciprocal-polynomial/PF2/log-concavity search and local comparisons; no additional search or novelty claim is made. The audit stays within the same polynomial and elementary finite calculation.
SOURCE_EVIDENCE: NIST DLMF https://dlmf.nist.gov/1.14#i (1.14.1--4 and Fourier uniqueness) and https://dlmf.nist.gov/1.14#iii (1.14.17--19 and convergence hypotheses), directly inspected 2026-10-31; these cover standard conventions and convergence only. L560 uses direct finite integration; its rational identities, curvature and jet remain unaudited local claims.
COMPARISON: L049/L055 concern direct Fourier kernels and do not certify this reciprocal density. L560 would refute only the log-concavity-only transfer. The audit checks that narrower conclusion; it neither imports nor tests Sra v2's PF256 assertion or actual-Xi signs.
GAP: The completed calculation and informal proof need independent arithmetic/hypothesis replay before the notebook relies on the countermodel as audited. No uncovered theorem or new model is required, and no parameter tuning or general PF256 extension is covered.
REASON: Recovery source review supplies the missing direct primary-source URLs and verifies their scope without changing the saved audit target. EXPLORE remains appropriate for the local model-specific replay; no matching external countermodel theorem is imported and no mathematical audit is claimed here.
SCOPE: Exactly L560 and scripts/reciprocal-pf2/fixed_model.py with its full certificate; source reuse is confined to the original fixed-model assessment. No new lemma, independent sign mechanism or broader polynomial family is approved here.

The test is to replay the complete rational transform identity and all
load-bearing exact values, verify the exponential-pair curvature
formula and the [0,1]/[1,infinity) bounds, check C2 even extension and
absolute convergence on the open strip, and distinguish the polynomial
jet at 10 from evaluation of the transform outside its convergence
strip. Repair any real error; otherwise mark the qualified countermodel
audited. Its rejection would reopen only the fixed diagnostic, not
establish the proposed transfer.

Prior coverage:
[fixed model](2026-10-31-reciprocal-pf2-first-sign-model.md) and
[parent discovery](2026-10-31-complete-first-sign-mechanism-discovery.md).
Mathlib remains not checked; no absence or formal verification claim.

## Source-gate recovery -- 31 October 2026

LITERATURE_REASON: The supervisor reported missing direct source URLs in this ready assessment; this bounded review repairs that essential provenance field while preserving the exact audit target.

Primary source: [NIST DLMF, section 1.14](https://dlmf.nist.gov/1.14),
live HTML inspected 2026-10-31, using the numbered equations as locators.
The Fourier subsection cites Titchmarsh (1986a), pp. 3--15, 42, 50--59;
the Laplace subsection cites Schiff (1999), pp. 12--57, 91--93, 151--157.
Those books were not newly read.

Equation 1.14.1 uses the positive imaginary Fourier exponent and unitary
normalization. Equation 1.14.3 requires absolute integrability and local
bounded variation and gives one-sided means via principal-value inversion.
The uniqueness paragraph requires continuous absolutely integrable functions
and equality of transforms everywhere. Equations 1.14.17--19 concern
one-sided Laplace transforms: piecewise continuity and a global exponential
growth bound give analyticity strictly to the right of that growth exponent.
They do not supply a bilateral inversion theorem or a curvature sign.

The forthcoming audit must check L560's claimed exponential majorant and
origin matching before relying on these hypotheses. Its direct finite
half-line integration is already covered by the parent assessment; no
inversion theorem needs reproof. All rational identities, conjugate signs,
global inequalities and jet values still require complete independent
replay. Evaluation of the polynomial at 10 must remain distinct from
transform evaluation outside the open strip.

Reused comparison: the fixed-model and parent assessments above retain
the exact-statement search, L049/L055 direct-kernel distinctions, L233's
different model and the failed reciprocal-PF2 transfer. No search for a
broader theorem, new countermodel or actual-Xi mechanism was performed.
Sra v2 and PF256 remain outside the audit's assumptions; its probability
arguments and numerical certificate are not newly read or certified here.
Mathlib coverage remains not checked.

Decision: source provenance repaired, EXPLORE retained for exactly the
saved finite audit. This is process repair, not evidence that L560 is
correct or new. Continue by the full replay stated above; any failure
requires repair or qualification of the countermodel. No mathematical
script was run and no lemma was changed in this literature turn.
