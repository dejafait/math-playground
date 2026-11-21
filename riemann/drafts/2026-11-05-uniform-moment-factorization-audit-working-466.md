# Conditional factorization audit — working record, step466

Target is the unchanged SPECIALIZE assessment in
`drafts/literature/2026-11-05-uniform-moment-factorization-audit.md`.
Main gap remains actual-Xi all-degree mixed positivity. This is one
conditional analytic audit, not a new central sign mechanism.

Primary text retrieved: Michałowski, arXiv:2607.16795v1, Section 3,
Lemmas 3.1–3.6 with complete proofs. L019/L021, L786 normalization
and only L776 definitions were read. Prior step385/465 comparisons
exclude an earlier Gate A audit; recorded coefficient stops are unchanged.

Partial reasoning saved before completing the budget:

- Use the full phase, not the initial first-summand phase. The additive
  log(pi) in that initial normalization does not affect the saddle; the
  main term must use log(Phi) exactly.
- Source hypotheses: full saddle drift <=3/200, tube nonvanishing,
  local curvature >=6/sigma^2, third derivative <=100/sigma^2,
  global curvature >=(8/5)k/u_k^2. These antecedents are not audited.
- The proof uses |A|<=14.185 from the proof of Lemma 3.5, not merely
  its stated |A|<=20. Treat the sharper bound as an explicit cited
  hypothesis, with no ancillary replay claim.
- log(k)/k decreases here; log(10^9)<21 bounds the Taylor error by
  sqrt(7/75000)<0.01. The local window is inside radius 1/40.
- Expected relative budget: (0.0103 + exp(-12)/6 + 0.0001)/0.665
  plus the connector, which must be justified, is below 0.0158.
- To check the previously certificate-only connector constant, on
  0<=Re(u)<=0.35, |Im(u)|<=0.015 each absolute summand is bounded
  by its value at Re(u)=0 after replacing cos(4 Im(u)) by cos(0.06).
  The resulting series is <44 exp(-2)/(1-16 exp(-6))<7<24.
  This needs the explicit monotonicity and geometric-series proof.
- Global far tail: b delta^2>k/(125 log(k)^2), delta=1/40;
  the bound is uniformly far below 10^-100. Check both monotonicities.

Outstanding: complete endpoint deformation and branch argument, prove
the scalar bounds with rational margins, and record the conditional
result canonically only if every component closes. No I-nonvanishing
or derivative of an unknown error is assumed. No script is needed.

Completion: the outstanding checks above are finished in
`lemmas/L787-conditional-uniform-complex-moment-factorization.md`.
The complete conditional relative budget is <0.0158<0.018. The
source's analytic antecedents, particularly |A|<=14.185, remain
explicit assumptions; no unconditional actual-I disk is imported.
