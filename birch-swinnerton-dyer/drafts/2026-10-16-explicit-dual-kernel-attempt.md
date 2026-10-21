# Explicit dual kernel: bounded attempt stopped at verifier recurrence

Step BSD-2026-10-16-262-explicit-dual-kernel-attempt is RESEARCH /
REPRODUCTION / implementation. The invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-16-explicit-dual-kernel-algebra.md` is reused
unchanged for its exact TARGET. No additional source discovery, new
algorithm, cross-notebook input or new lemma is claimed.

The main gap remains arbitrary-curve rank equality for analytic order at
least two. The intermediate target is the whole explicit nonzero dual
kernel over L070's D, potentially providing the affine-line algebra for
L066. Functions, incidence/norm, complete global power classes, local
identifications/bounds, Selmer containment, the other L026 premises,
successful localization, rational membership, divisible Sha and complex
order comparison remain independent gaps. L067/L068/L070/L071/L072 are
audited inputs; L069 and partial column evidence are excluded. The
recorded stops ATTEMPTS/035--036 concern different presentations.

## Method and evidence

BMSS, *Fast algorithms for computing isogenies between elliptic curves*,
arXiv:cs/0609020v1, Theorem 2(2), §§2.4--2.5 and 4.1--4.3, is imported
with the exact source qualifications in the assessment. Pinned
[Sage 10.7 lines 3147--3188](https://raw.githubusercontent.com/sagemath/sage/10.7/src/sage/schemes/elliptic_curves/ell_curve_isogeny.py)
were retrieved to implement the already assessed Newton linearization;
this is implementation consultation, not a new literature turn.
Characteristic zero and the existing D-defined dual give the reconstruction
hypotheses. The producer uses conservative S precision 52 and T precision
26 with Newton T-precisions 8,16,26; rational reconstruction bounds are
numerator degree seven and denominator degree six. It retains the complete
26-term residual and exact squared-denominator candidate, not a selected
embedding or assumed rational generator.

All new arithmetic was inside one production and one independent replay
stage, each internally capped at 180 seconds with an external 181-second
watchdog. The cumulative new-data bound was 134217728 bytes. Exact
measurements and all produced coefficients are retained under
`scripts/seven-torsion/dual-262/`:

- `production-report.json`: producer completed in 1.0933976250234991
  seconds; external stage 1.1592632919782773 seconds. Its last watchdog
  counted 146909 bytes.
- `normalization.json`, `newton-8.json`, `newton-16.json`,
  `newton-26.json`, `series.json`, `reconstruction.json`, `dual.json`:
  complete unverified candidate data, including both raw-coordinate maps
  and inverse witnesses. These are not canonical mathematical results.
- `replay-report.json`: replay stopped after 0.19687066692858934 seconds
  at `dual_after_quotient_division_degrees`. Its external stage took
  0.2801665000151843 seconds and counted 170125 bytes before that watchdog
  report. Neither watchdog fired. `verify_dual.log` retains the failure.
- `basic-identities.json`: full zero residuals of the checked curve and
  differential identities, and reduced numerator-inverse witnesses. The
  complete replay check list was inspected; earlier checks include degree,
  squarefreeness, disjointness from two-torsion and both numerator units.
  They do not establish either composition or actual dual identification.

The implementation normalizes the codomain to
Y''²=X''³+7⁴aX''+7⁶b with (X'',Y'')=(49X,343Y). Its inverse scales
by (1/49,1/343); normalized dual followed by that inverse has differential
scalar seven. Basic replay checks concern the candidate's displayed maps,
not completion of the required whole-family certificate.

## Exact failure and bounded diagnosis

The independent verifier imports only `verify_certificate` rational
helpers, never producer arithmetic. Its first multiplication-by-seven
check fails before either composite is constructed or saved. No later
reconstruction/ODE replay, rejection test, projective argument or
preservation branch in that verifier executed. No composition file exists.
The failed check is a conjunction of prescribed degrees and leading
coefficients; the runtime report did not save individual failed values.
They must not be described as observed runtime measurements.

Static inspection finds a concrete normalization error at the `p8`
assignment in `verify_dual.py`. The imported recurrence is Sutherland,
MIT 18.783 Fall 2023, Lecture 5 §§5.5--5.6, printed pp.10--14,
Lemma 5.20 and Theorem 5.21, already cited and used in audited L068.
Write r4=psi4/(4Y), r6=psi6/Y and r8=psi8/Y. The existing even
recurrence, without a new theorem or algorithm, specializes to

    psi8 = psi4*(psi6*psi3^2 - psi2*psi5^2)/(2Y),
    r8 = 2*r4*(r6*psi3^2 - 2*psi5^2).

The new verifier uses factor 8 instead of factor 2 in the latter line.
The old L068 verifier retains the division by 2Y explicitly and does
not have this transcription error. With the new verifier's representation,
the standard leading coefficients are r4:1, r6:6, psi3:3 and psi5:5.
Thus the correct r8 leading coefficient is 2*(6*9-2*25)=8; its coded
factor instead gives 32. In the coded x numerator X*psi7^2-c*r6*r8,
this predicts leading coefficient 49-6*32=-143, contrary to the required
one. This is a static diagnosis from the displayed code and imported
recurrence, not an independent finite replay of the saved candidate.
It invalidates this verification attempt and is not evidence against
the existence or validity of the mathematical dual. The psi9/omega7
part and the entire composition assembly remain unaudited.

The declared first-failure rule is obeyed: no repair, second replay,
stage extension or retrospective repartition was performed. The original
failed script and all candidate outputs remain intact. Metadata-only
hash/byte inspection is retained in `preservation-and-size.json` and
`stopped-artifact-manifest.json`; it checks the two complete input files,
not every historical artifact. Those are preservation checks, not
additional mathematical verification.

## Continuation and outcome

EXPLORATION records one incomplete computational attempt, not a new
mathematical advance or informative negative result about a route. No
lemma, DAG edge or PROOF.md argument changes. Mathlib coverage of the
whole computation remains not checked. No ready literature comparison
needs refreshing: target, hypotheses, algorithm and exact success test
are unchanged. Continue on the same exact assessed target in a fresh
invocation, preserve this stopped evidence, correct the explicit even-
recurrence factor and audit its normalization before one fresh bounded
independent replay. Continue only if both composition coordinates,
projective/kernel completeness and full etaleness pass within the saved
bounds; stop at the first failure/cap. Another unproductive mathematical
turn requires route reassessment under the shared rule. No cap increase
or new method is proposed.
