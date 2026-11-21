# Fixed-slice source review — working notes, step423

Literature-only; no zero calculation or new error bound has been performed.
Main gap: actual-Xi positivity/L984(H), not this auxiliary slice.
Reviewed target: the exact step422 fixed-w=3/2 certificate assessment.

Inspected Lagarias–Rains math/0104176v5 Theorem2.1 and its proof,
printed pp8–9, equations(2.6)–(2.10); Section8 Lemma8.1 and its
whole proof, printed p44. Equation(2.9), including both rational pole
terms, is the intended evaluator source. The theorem supplies
entireness and s->w-s. The Section8 displayed 1-rho symmetry must
not be used at w=3/2; it conflicts with the general functional equation.
The numerical departure is a lead, not an enclosure or transport input.

Reuse ready interval-inclusion/integration coverage in
drafts/literature/2026-10-17-bulk-haar-integral-enclosure.md and
drafts/literature/2026-11-01-theta-integrated-layer-compensation-scope.md.
Newly inspected Rump, corrected Acta Numerica2010 author PDF,
Theorem13.3/(13.8) and its whole proof, internal p89: a strict
Krawczyk inclusion for a real two-dimensional system supplies existence;
the scalar interval-Newton theorem alone is insufficient here.
Potential test: certify the two real components of the exact fixed-slice
function in one rational box, enclose that box in a rational disk strictly
inside the requested off-center domain. No inclusion or disk is known.

Read python-flint0.9.0 acb.integral callback contract and archived
Arb2.23.0 acb_calc callback/branch rules. Default python3 has no flint
module; uv and Homebrew executables exist. This is an implementation
availability risk, not an analytic theorem or proof of source blockage.
Current FLINT3.7.0-dev docs disclose an ongoing LLM-assisted revision;
use the primary integration paper and archived API contract as the
mathematical references, and record the eventual actual backend.

Completed: inspected Johansson1806.06725v1 Section1.4.2/(1.18)–(1.20)
and Algorithm1 pp12–13, including the positive geometric denominator;
1802.07942v1 Sections2–2.1/3.2, including achieved-radius/evaluation-limit
and manually bounded improper-tail cases. No effective constants were
derived. Completed source notes and the bounded continuation are in
drafts/literature/2026-11-11-two-variable-fixed-slice-zero-certificate-review-422.md
and drafts/literature/2026-11-11-two-variable-fixed-slice-krawczyk-test-423.md.
Next mathematics must justify differentiated Eq(2.9), uniform theta and
spatial tails, branch domains and full Jacobian inclusion. No source
already supplies the finite certificate; no lemma or script was edited.
Independent signed Li payment and zero transport remain missing; a
creative central attempt is not justified by this fixed test.
