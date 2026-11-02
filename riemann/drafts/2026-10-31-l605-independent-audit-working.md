# L605 bounded specialization audit — working record

The approved target is the exact L605 audit in
`literature/2026-10-31-l605-reciprocal-hazard-audit.md`.
This is a mathematical audit, not new source discovery or a new sign mechanism.
The main gap is actual-Xi all-degree signs at unbounded heights. The
intermediate target is only the full-theta Stein nonincrease premise;
its possible downstream use requires a separate first-sign transfer.

Read L605 and L019 in full. Preliminary replay gives K(u)=4 Phi(u/2),
Z=16 integral_0^infinity Phi(t) dt, and
h(u)/p(u)=2 integral_(u^2/4)^infinity q(s) ds/q(u^2/4).
The auxiliary normalization J cancels independently of Z. This replay
is not yet the completed audit: verify exact source hypotheses,
full-line centering/smoothness, open-support conditions, and both tails.

Known contrasts checked narrowly: C233b rules out its fixed Gaussian
mixture as a monotone-Stein countermodel; L604 leaves an integrated
signed remainder. Neither supplies a missing Fourier-sign implication.
Only L019 is a direct local mathematical input to L605.

Pass/error test: check every identity and applicability condition,
including u=0 and infinite tails; repair a concrete error or preserve
and stop a failed specialization. A pass secures only the premise.
Original 1988 shape proof and full Mathlib coverage remain unaudited.

## Completed audit

Pass, with no mathematical correction. The canonical proof in L605
now records the explicit full-line normalization and the complete
right-tail absolute-derivative integral. Replayed source Theorem
4.1(i)-(iv), Theorem 4.2(b), the hazard Theorem 3/Corollary 2 and its
complete concave proof case, and Saumard (5)-(6). The previously
recorded hazard sign/reference typo is not a new finding or an input.
The auxiliary interval is open; neither a smooth zero extension nor
a vanishing left-endpoint density is required. Full-line smoothness
comes from imported even analyticity, not an arbitrary even extension.
The centered numerator tends to zero at both infinities. The two
normalizations and the factor 2 pass separately, including u=0.

This verifies a known-result specialization and does not claim progress
beyond the checked sources. The argument and DAG inputs do not change;
PROOF.md and DAG.md are therefore left unchanged. The full audit
qualification, citations and proof remain canonical in L605.

No scripts, numerical certificates, new lemmas, new sign implications,
or parameter variations were used. First-sign transfer and L604's
integrated remainder are unresolved. A fixed prescribed-Stein model
is nominated for source coverage in the continuation assessment only;
no reconstruction or Fourier calculation has been attempted here.
