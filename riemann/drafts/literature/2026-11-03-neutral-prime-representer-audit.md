# Neutral prime representer: separate conceptual audit nomination

TARGET: Independently audit paper 18/v3 (21)--(28) for Q(u)=⟨q,u⟩ on fixed finite neutral complex vectors, including q∈H, all pole cases and the ordered contour limits.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed neutral-prime-representer-coverage.md source comparison of step 235; no new search or priority claim for this nomination.
SOURCE_EVIDENCE: https://rstation.ai/problems/riemann_hypothesis/papers/18 — bramble_trace, Fixed and growing neutral gradients of the anchored Selberg–Möbius approximant, displayed v3 (22 October 2026), Fixed-probe theorem and An elementary representer of the complete fixed gradient (21)--(28); direct access and these locators rechecked 2026-11-03; standard-input URLs below reuse step 235.
COMPARISON: The source asserts the fixed-generator identity for every m>=2. The proposed audit reproduces the contour proof, checks the finite complex neutral specialization and reuses the already audited finite endpoint; no stronger conclusion is sought.
GAP: Independent verification of Mellin inversion, derivative strip bounds, odd left-edge decay, residues at 1/0/-2k, residue-series convergence, endpoint integrability and conjugations remains.
REASON: An H-representer would connect L729's prime functional with legitimate Hilbert projections; independent replay is warranted for a load-bearing unreviewed analytic input. It supplies no RH candidate or baseline norm decay.
SCOPE: Direct-source-URL recovery review completed in step 236; SPECIALIZE coverage is ready for the exact saved audit. That audit is RESEARCH/REPRODUCTION; do not relabel it creative or expand into saturation, projection optimization or complementary-residual estimates.

Use precisely H, rho_m, a_m, f_m, K_m, T_m, A, B and Q of L729.
Let u=sum_(m=2)^K c_m rho_m with fixed finite K and complex c_m,
A(u)=B(u)=0; the inner product is linear in its first entry. The
proposed identity uses

    q(y)=log(2pi)-{y}+(1/2)log(1-y^(-2)),   y>1.

The primary source and standard-theorem hypotheses, source formulas
and their unresolved verification obligations are in
[the completed coverage assessment](2026-11-03-neutral-prime-representer-coverage.md).
L729 already proves absolute convergence of Q. L730's finite-sum proof
of the conditional endpoint used in (27)--(28) may be reused; its
density conclusion is not needed to prove a fixed-vector identity.
No use of whole-step-space density, RH, zero simplicity, q equal to
the original prime discrepancy, or uniformity in an infinite u-family
is allowed.

The bounded test is the complete fixed-m contour, followed only by
finite conjugate-linear combination and the two neutral cancellations.
Check all of (21)--(28), including transform endpoints, inversion and
Fubini on 1<c<3/2, multiplicity-r cancellation before shifting,
uniformity at sigma=0,1, horizontal decay, odd A>=3 left lines,
T→infinity at fixed A before A→infinity, the double pole at 1,
the residual pole at 0, simple trivial zeros and absolute summability.
Check the final logarithmic majorant in L1 for the pairing and in L2
for q∈H; the first does not imply the second. Verify residue signs
and constants independently, not by a numerical check.

Continue only if the identity survives with all hypotheses and limits
justified. A repair must be explicit and remain within the covered
classical tools; a new mechanism needs another source gate. Preserve
any failure canonically and park dependent projection claims if an
essential boundary estimate or residue cannot be justified. A pass
validates known-source mathematics locally, with no assertion of
originality, full-norm decay, saturation or RH.

Mathlib: exact supporting mellinInv_mellin_eq hypotheses were inspected
in step 235; full matching representer theorem remains unchecked.

## Direct references and recovery review, step 236

LITERATURE_REASON: The supervisor reported missing direct source URLs in
this ready assessment. This review repairs source traceability while
retaining the exact target and the step-235 comparison; it does not
repeat discovery or verify the identity.

Primary source: [bramble_trace, paper 18/v3](https://rstation.ai/problems/riemann_hypothesis/papers/18),
22 October 2026. The accessible HTML again displays v3. Locators:
**Fixed-probe theorem** for definitions and the claimed representer;
**An elementary representer of the complete fixed gradient**, subsections
**Mellin transform and the prime sum** (21)--(22), **Cancellation and
contour boundaries** (23)--(24), **Residues** (25)--(26), and
**Recovering the representer** (27)--(28). Reopened these relevant
passages for access and locator confirmation only. Their mathematical
validity remains the saved audit's task. No source blocker was found.

Direct standard-input references, already inspected with their exact
hypotheses in the linked step-235 coverage, are retained here so the
ready assessment is independently traceable:

- [DLMF 25.5.5](https://dlmf.nist.gov/25.5#E5): fractional-part transform.
- [DLMF 1.14.35](https://dlmf.nist.gov/1.14#E35): Mellin inversion.
- [DLMF 25.4.1--2](https://dlmf.nist.gov/25.4): functional equations.
- [DLMF 25.2.4](https://dlmf.nist.gov/25.2#E4),
  [25.6.1](https://dlmf.nist.gov/25.6#E1) and
  [25.6.11](https://dlmf.nist.gov/25.6#E11): Laurent expansion and values.
- [DLMF 5.11.2 and 5.11.9](https://dlmf.nist.gov/5.11): digamma and gamma asymptotics, with Section (ii) remainder qualifications.
- [Trudgian, A modest improvement on the function S(T), arXiv:1010.4596](https://arxiv.org/pdf/1010.4596), Section 4, pp. 5--6, Lemmas 1--3 and (8)--(14): strip interpolation and its zeta application.
- [Mathlib mellinInv_mellin_eq](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/MellinInversion.html#mellinInv_mellin_eq): supporting inversion only; full representer coverage remains unchecked.

Reuse the earlier coverage's duplicate/failure comparison without a new
novelty claim. The earlier inaccessible alternate sources remain unread;
they are not essential to this source gate. Coverage approval permits
only the specified conceptual replay. It establishes no lemma, no norm
decay and no progress beyond the checked sources.
