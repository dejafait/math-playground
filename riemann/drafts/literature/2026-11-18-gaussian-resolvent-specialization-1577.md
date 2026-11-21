# Gaussian resolvent analytic specialization — continuation1577

TARGET: Specialize the Gaussian Cauchy transform to C032m's subtracted even zero pairs and prove an explicit uniform spectral-tail error for E_sigma on [1,2] times {|w|<=2}, stating the certified finite-divisor input interface.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed review1577 of the original assessment1576 target; reuse the queries, scoped duplicate/failure comparison and source evidence in drafts/literature/2026-11-18-gaussian-resolvent-source-notes-1577.md. No renewed search or novelty claim is needed for this bounded analytic subtarget.
SOURCE_EVIDENCE: NIST DLMF equations7.7.2 https://dlmf.nist.gov/7.7.E2 and7.7.6 https://dlmf.nist.gov/7.7.E6 with definition7.2.3 https://dlmf.nist.gov/7.2.E3 and reflection7.4.3 https://dlmf.nist.gov/7.4.E3; Ivanov-Adkins(2023), Section3.1/Figure2 p.10 https://doi.org/10.1017/S0022377823000077; Hasanalizade-Shen-Wong arXiv:2107.06506v1 https://arxiv.org/pdf/2107.06506v1 Corollary1.2 p.2 and complete proof p.15. Recovery1578 verified direct primary access; qualifications remain in source-notes1577. Reuse C032m's Haslinger2.39 coverage.
COMPARISON: Known general transforms and counting cover the tools; the paired subtraction, removable primitive identity and effective spectral truncation for this exact family remain to be justified. No full matching theorem was found in the inspected sources; this is a bounded specialization, not a claimed new general transform.
GAP: Establish the exact pair normalization, safe-domain identity, full-disk removable continuation, uniform summable bounds for every exchange, and an explicit primitive tail tending to zero. State necessary finite-input enclosures without pretending the notebook has certified coordinates or a feasible evaluator.
REASON: This analytic interface is independently testable without missing finite coordinates and avoids the stopped expanding-disk error scheme. Newly written continuation: separate supervisor approval precedes invocation; no mathematics was derived during review1577.
SCOPE: Real sigma in[1,2], |w|<=2, C032m's full positive-ordinate divisor with multiplicity, |delta|<1/2 and gamma>14; retain C032j/m/q's zero-ordinate, strip/counting, through100/first-zero/tail, heat and fixed-v1 qualifications. No RH, density, moments, profile sign, finite-coordinate availability, complex-width differentiation or unsmoothed realization is assumed.

## One bounded application and decision test

Import DLMF's general identities by citation. Do not reprove the general
Gaussian Cauchy-transform theorem. Derive only its application to the
even Gaussian zero pair with the actual factor1/2 and the subtraction
in R_sigma. Check complex-centre shifts in an explicitly safe initial
domain. When using continuation, justify agreement with the original
removable combined integral, including w=0 and both imaginary-axis
pole locations. A principal value or an uncorrected lower-half-plane
integral does not supply the required identity.

For the infinite divisor, justify termwise operations with a common
integrable bound, uniform on the closed width interval and disk.
Prove an explicit bound on the contribution of all gamma>H and
propagate it along the entire primitive path, with the error tending
to zero as H increases. The imported counting theorem is available
for this purpose, with its stated source qualifications. Specify the
range of H and endpoint treatment. No decay rate is asserted here.
If desired, estimate the original quotient rather than using a
sectorial erfc asymptotic outside its stated remainder domain.

Success requires both the removable identity and the explicit uniform
vanishing tail. State what certified finite divisor enclosures and
arithmetic error controls would be needed for the finite part. They
are an interface, not supplied data. No optimizer or numerical kernel
table is authorized; do not search for zero coordinates within this
attempt. If a pole, domination or tail obligation fails, preserve the
unfinished derivation and stop at that obligation. A formula with an
uncontrolled tail is not a completed evaluator. Do not respond by
increasing dictionary size, cancellation order or variation budget.

The possible downstream use is unchanged dictionary1570's residual<1/2
test for variation-at-most-2 positive-output annihilators. Source
coverage does not guarantee its feasibility. A proved analytic
interface needs later audit; actual numerical use also needs the
finite data and a cost check. No all-order residual-decay mechanism,
full odd cancellation or unsmoothed actual-Xi realization is supplied.

Essential local inputs are C032m/q and their retained conventions;
C032w/x, notes1572/1555, calculation1564 and stops1571/1576 are
comparisons and preserved evidence. Full matching Mathlib coverage is
unchecked/unknown. This is ordinary established-transform development,
not a justified creative central-gap attempt. Do not repeat this
specialization after failure without materially new input.

## Recovery1578 — direct source URLs and separate source approval

Literature-only check, 18 November 2026. Added direct primary URLs to
SOURCE_EVIDENCE itself; the previous field delegated links to notes1577.
Opened DLMF7.7.2/7.7.6 with their displayed domains, the version-pinned
counting PDF's Corollary1.2 and complete corollary proof (pp.2,15),
and the [institutional Ivanov-Adkins PDF](https://scientific-publications.ukaea.uk/wp-content/uploads/an-analytical-form-of-the-dispersion-function-for-local-linear-gyrokinetics-in-a-curved-magnetic-field.pdf),
Section3.1 and all three contour cases in Figure2 (p.10).
The counting theorem's finite-verification qualification remains; no
individual zero coordinates or database audit is claimed. Reuse the
other inspected source statements, duplicate comparison and recorded
failures in notes1577; no new search for a mathematical mechanism.

The source decision remains SPECIALIZE for exactly the saved target.
This separate review finds its essential coverage adequate within the
stated scope. It establishes no paired identity, tail bound or numerical
interface. No lemma or mathematical script was changed. The completed
step is a metadata repair, honestly STALLED mathematically; it does not
reset exploration or convert known tools into a new result. All pole,
interchange, normalization and tail obligations above remain unpaid.
