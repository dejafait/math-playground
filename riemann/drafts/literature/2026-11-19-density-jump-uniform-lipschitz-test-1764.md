# Uniform remainder modulus prerequisite1764

TARGET: Test an explicit uniform spatial Lipschitz bound for C033j's densities r_sigma on [3/4,5/4] from the Gaussian heat formula and differentiated convolution series, retaining all fixed-v1 qualifications.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Source-notes1764 compares Post-Widder/Gaver inversion with this signed family, checks named residual reviews and preserved stops1571/1576, and finds no ready uniform quantitative remainder bound; no novelty claim.
SOURCE_EVIDENCE: Sra October-v1 Lemma2.1 p4 and PropositionB.1/proof p17 https://hexagonmath.org/pdf/2610.00584v1 ; November-v1 Proposition3.1 pp5-6 and AppendixC.1 p21 https://hexagonmath.org/pdf/2611.00345v1 ; Euler beta integral https://dlmf.nist.gov/5.12.E1 ; Haslinger Theorem2.39 pp67-68 https://www.mat.univie.ac.at/~has/scriptneu.pdf . Direct sources reopened in recovery1765; reuse notes1740/1764 for prior full coverage; Gaver is downstream context only.
COMPARISON: C033j proves joint continuity and locally uniform density convergence, not a spatial Lipschitz constant. Known heat derivative and beta tools cover ingredients; uniform derivative majorants and summation remain the exact specialization.
GAP: Establish or refute this bounded derivative-majorant mechanism, state all constants/onsets as effective or existential, and justify differentiation despite zero-endpoint convolution singularities; no full separator required or authorized.
REASON: This independently testable prerequisite isolates the missing modulus before quantitative deconvolution. Prove only the new uniform family estimate and import the heat/integration tools precisely.
SCOPE: Exactly C033j's R_sigma=exp(-M_sigma)E(D_sigma(t)dt), D_sigma=ell_sigma-ell_1, sigma in[1,2], and its non-atomic densities on x>0; retain zero atoms and all C032j/q/s,C033i/j qualifications. No global smoothness, effective constants or inverse stability assumed.

Source approval1765 (19 November 2026): direct URLs repaired and primary
statements/relevant proof cases rechecked. SPECIALIZE is approved for the
unchanged target only. No Lipschitz estimate is derived or accepted.

Use C033j's fixed-simplex formula only after proving its needed derivative
majorant, or give a fully bounded-difference alternative. Source coverage
includes separate heat errors through order2, not differentiation of a
big-O term. Keep actual divisor, conjugation, multiplicity, excluded
ordinate zero, strict strip, gamma>14, counting, through100/retained-real-
zero/tail, heat, half-variance and both fixed-v1 qualifications.
Source-wide correctness and finite-zero data remain unverified.

Required threshold: an explicitly parameterized finite Lipschitz bound
on [3/4,5/4], uniform on the entire width interval, with justified
termwise differentiation or bounded differences. Constants must be
identified, including their onsets. A bound in specified existential
heat constants is partial progress, not a computable numerical modulus.
Numerical effectivity remains unpaid. Abandon this derivative mechanism
if an essential uniform singular majorant is not integrable; preserve
the failed estimate. Pointwise smoothness alone does not pass.

Downstream: test Gaver finite-sample resolution of the jump with signed
tail and coefficient cost control. That conversion, numerical optimization
and rational separator data remain parked. Cancellation, moments,
uncapped range and Xi realization are independent gaps. Matching
Mathlib coverage is unchecked and unknown.

## Recovery1765 source check

The sources linked in SOURCE_EVIDENCE were reopened on 19 November 2026.
October-v1 Section2.1/(2.1)-(2.3), Lemma2.1 and its complete proof,
and PropositionB.1 with its complete proof were read. Fixed derivatives
have local absolute convergence on Re t>0. B.1 treats counting and
complex displacement separately for each fixed j, including j=2;
its proof uses a second-order Taylor bound on vertical segments. The
large-time case uses the retained low real zeros and a tail gap.
Constants depending on j and small-time onsets remain nonnumerical.
These are precisely the ingredients already assessed in notes1764;
no differentiated remainder or uniform-in-j estimate is imported.

November-v1 Proposition3.1 and its complete AppendixC.1 proof were
rechecked: t,sigma>0, half-variance sigma, square completion and an
absolute Gaussian majorant justify summing over the actual divisor.
This supplies the width/time identity, not regularity of r_sigma.
DLMF5.12.1 was reopened with Re a,Re b>0. Haslinger2.39's full
statement and dominated difference-quotient proof were retrieved:
positive measure, pointwise parameter holomorphy, integrability and
a common integrable majorant on each disk are hypotheses. Signed use
requires total variation; a real bounded-difference proof may instead
use the already assessed dominated-convergence theorem. Neither tool
supplies the missing majorant automatically.

Reuse the exact-target searches and duplicate/failure comparison in
notes1764, especially its final source-comparison section and preserved
stops1571/1576. No changed target or new general smoothness theorem is
claimed. Uniform differentiated endpoint control and series summation
are still the research obligations. All qualifications above remain.
This repairs source traceability only: STALLED as mathematics, no new
bound, no source-wide correctness certification, Mathlib unknown.
