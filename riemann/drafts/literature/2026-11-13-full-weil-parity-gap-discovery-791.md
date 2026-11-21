# Proposed spectral-parity comparison: source review required

TARGET: Assess whether the complete localized Weil form on (-1,1) has a strict lowest-even versus lowest-odd Rayleigh gap, checking primary variational results and recorded parity/ground-state failures before nominating one bounded test.
CHECKED: 2026-11-13
DECISION: EXPLORE
SEARCH_EVIDENCE: Step792 searched exact localized-Weil/parity/lowest-eigenvalue/interlacing terminology and narrowly checked the Suzuki, spectral-triples, modulus, nodal and pole-resolvent records. Found primary arXiv:2611.13129v1: its interlacing is numerical and its lower ladder bound is Hypothesis3.4. No exhaustive absence or novelty claim.
SOURCE_EVIDENCE: Read Suzuki2606.09096v2 Theorem1.1, Corollary1.2, Theorem1.4, Sections4.1-4.2,4.5,5.1-5.3; Andrews-Connes-LaGatta2611.13129v1 Sections2.1,3.3,4.3, Lemma6.1 with proof, Lemma8.16 with complete proof. Reused spectral-triples assessments and L759 finite-certificate conclusion; L744(6) and C998z supply local normalization and the retained modulus stop.
COMPARISON: Primary variational theory supplies a closed semibounded realization, discrete spectrum and a smooth core, but no inspected theorem gives the requested strict ordering at half-width1. Suzuki small-window scope is not effective at1; source interlacing tables and L759 finite separation cannot lower-bound the full odd infimum.
GAP: The strict fixed-window ordering remains unproved; its missing arithmetic input is a complete odd-sector lower bound exceeding an even trial upper bound. Abstract attainment belongs to the cited closed realization, not necessarily to the smooth test class; even-sector simplicity and Xi transfer remain separate.
REASON: The review rejects direct import and another finite-only parity computation, and nominates one complete-complement comparison instead. This is useful source-scope/duplicate evidence, not a proof against the parity inequality or a new RH sign input.
SCOPE: Completed literature-only assessment of full unneutralized Q on (-1,1), both poles and all prime powers retained. No lemma, calculation, source-proof repair, positivity replay or semigroup conclusion. The separate continuation assessment specifies the bounded mathematical test.

The proposed inequality is lambda_even<lambda_odd, where each lambda
denotes the infimum of Q(f)/||f||_2^2 over nonzero real smooth compact
tests in (-1,1) satisfying respectively f(-x)=f(x) or f(-x)=-f(x).
This defines the proposed review target; no sign, strict inequality,
existence of minimizers or identification with an operator eigenvalue
is asserted. The source review must check those distinctions.

Essential local inputs for the proposed review are L741's
normalization/semibounded-form discussion, L744(6), and audited C998z.
The next turn should first search narrowly for recorded parity and
ground-state failures, then retrieve precise primary theorem
hypotheses and relevant proof cases. Reuse the adequate limiting-form
comparison in recovery review787; do not repeat the modulus pair or
infer the proposed inequality from positivity of Q. The reflected
bump pair has different Rayleigh quotients, but trial values alone
do not order the infima. No new source result is imported here.

Continue only if that review supplies applicable coverage and an
independently testable inequality not already excluded by recorded
failures. Otherwise preserve the obstruction and select a materially
different central-sign mechanism. Any mathematical continuation needs
its separate literature gate. A parity gap alone would still leave
ground-state simplicity/sign, Xi realization with multiplicities and
all-degree mixed positivity unresolved. There is no cross-notebook
input. Full matching Mathlib coverage has not been checked.

## Completed source comparison — step792, 13 November 2026

The original nomination above is preserved as the question reviewed,
not as an instruction to repeat discovery. Its uncomputed status and
independent gaps remain. No strict ordering has been derived here.

Primary sources actually inspected:

- Masatoshi Suzuki, *Weil’s quadratic form via the screw function*,
  [arXiv:2606.09096v2](https://arxiv.org/html/2606.09096v2),
  Theorem1.1/Corollary1.2 and Sections3.2,4.1,4.5 provide the closed
  realization, smooth core, compact embedding and parity decomposition.
  Theorem1.4 is only for sufficiently small positive half-width, without
  an effective endpoint covering1. Sections4.2 and5.1 retain a bounded
  perturbation of the limiting logarithmic form; Sections5.2-5.3 use
  positivity improvement for that limiting operator and small-parameter
  perturbation. Neither an all-window positive kernel nor a quantitative
  parity gap at1 follows. We import the stated variational framework,
  not an independent audit of these source proofs.
- Ronnie Andrews, Alain Connes and Antonio La Gatta, *The uncertainty
  operator, the Weil ground state and the zeros of zeta: a numerical
  study and conditional positivity of the Weil quadratic form*,
  [arXiv:2611.13129v1](https://arxiv.org/html/2611.13129v1),
  9 November2026. Section2.1 uses the same complete normalization after
  x=log u (half-width1 means lambda=e). Section3.3 Hypothesis3.4 assumes
  the lower ladder estimates; Remark3.5 explains their RH strength.
  Section4.3(36) reports finite computations. Lemma6.1 assumes window
  positivity and a complementary spectral gap; its proof uses a
  one-dimensional ground space and asymptotically small odd trial
  component. It cannot supply those hypotheses at lambda=e.
  Lemma8.16, including its square-completion proof and form-dual
  coupling hypothesis, supplies a conditional Schur criterion only.
  Its nonnegative case gives a zero lower floor, not the smallest
  positive Schur eigenvalue as a full-operator lower bound.

No uniform ladder, Section8 conditional semilocal estimate or external
unpublished Connes-Kastoris theorem is imported. Those are nonessential
leads for this fixed-window test. Its hypotheses must instead be paid
from the explicit complete form. Real smooth tests in the saved question
remain the comparison class; source operator terminology cannot silently
replace their infima without the parity-preserving core argument.

### Duplicate and failure comparison

L759 already certifies a simple-even minimum for lambda=sqrt(13),N=120,
with the separate audit recorded there. It is finite dimensional and at
a different window; it does not settle the present full-operator problem.
L760-L762 retain the separate boundary/realization limitation. Reuse the
November4 spectral-triples determinant and finite-parity assessments
rather than reproduce their real-zero theorem or finite certificate.

C998z explicitly leaves parity infima open and is retained without
repeating its bump pair. The October30 nodal-compression stop concerns
signed dilation slopes, and the nullvector-multiplier stop lacks a
nonnegative full kernel. The pole-resolvent assessment already rejects
generic secular identities without a controlled background and arithmetic
numerator. None provides a full odd lower bound; none is a global ban.
The November4 finite-window certificate assessment also records blocked
external enumeration artifacts. No archive retry or assumed source
certificate is part of the continuation. Positive fixed-window energy
alone cannot order its two sector minima.

### Search record and bounded continuation

Queries issued:
`"Weil" "form" "even" "odd" "Suzuki" eigenvalue`;
`"localized Weil" "ground state" parity`;
`"Weil quadratic form" "lowest" eigenvalue even odd`;
`"Weil" "parity" "gap" "lowest" eigenvalue theorem`;
`"localized Weil" "odd" "lower bound" "eigenvalue"`;
`"Weil quadratic form" "interlacing" theorem`.

Inspected primary passages are listed above; search-result mirrors,
experimental repositories, a negative-prolate interlacing lead and
unread general gap claims are not theorem evidence. The negative-prolate
lead concerns a different operator and is not a replacement input.
A direct shell download failed at DNS; the needed primary HTML passages
were successfully read through the web tool, so essential coverage is
not source-blocked. Initial oversized local search/status output is not
evidence; the substantive comparison used the named bounded records.

The independent bounded test is to bracket the two *full* infima at1
using one even trial and a lower certificate on the entire odd form,
with a fixed120-mode odd block and its complete complement. The new
assessment `2026-11-13-full-weil-parity-complement-test-792.md` is
SPECIALIZE: known variational/Schur machinery, unknown arithmetic
bounds. It receives separate next-turn approval. No mathematical
identity, cutoff computation or spectral enclosure was produced here.
The test may fail or remain inconclusive. Do not replace it by another
finite-only eigenvalue ordering or an unbounded cutoff sweep.

A new creative central-sign mechanism is not justified by this review:
no arithmetic bridge from such a gap to Xi realization has been supplied.
The nominated test is established-route development/reproduction, not
creative work, and a success would still leave simplicity within the
even sector, all-window control and actual-Xi realization unresolved.
Full matching Mathlib coverage has not been checked; unknown is not
absence. No cross-notebook input is used.
