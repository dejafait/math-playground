# L645 quantitative detector — nominated independent audit

TARGET: Independently audit L645's every-grid quantitative pole detector, including singular PSD interpolation, the analytic residual bound, uniform Blaschke contraction and strict integer threshold.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the quantitative vertical-Pick assessment and its local overlap/failure screen; on 2026-11-01 directly reopened the three primary URLs below and read their required theorem/proof cases. No new target or broad discovery search.
SOURCE_EVIDENCE: Bolotnikov (2010), definitions (1.1)–(1.7), Theorem 1.1, pp.151–153, https://files.ele-math.com/articles/oam-04-08.pdf ; Zakeri, Notes and Comments Section 8.3 after Example 8.33, https://zakerimath.com/CAbook/COM.html ; Complex.borelCaratheodory and supporting proof, lines 37–110, frozen commit 0d3fb85496130669f472d62be6f25999ca085c59, https://raw.githubusercontent.com/leanprover-community/mathlib4/0d3fb85496130669f472d62be6f25999ca085c59/Mathlib/Analysis/Complex/BorelCaratheodory.lean ; reuse L018 as the local input to the forthcoming audit.
COMPARISON: These previously inspected standard inputs cover the unchanged tools, including singular PSD, finite zero division and a positive real-part upper-bound constant. The audit checks only L645's specialization and quantifiers, not a new positivity mechanism or new source theorem.
GAP: L645 has a complete written proof but no separate critical audit; check its congruence, inverse Cayley denominator, disk margins, factor algebra, threshold equality and every-n conclusion without importing unproved growth or sign control.
REASON: Recovery source review supplies the missing direct URLs and reconfirms the exact required cases. SPECIALIZE is approved for the unchanged audit target; the independent mathematical audit itself remains pending.
SCOPE: Independent conceptual audit of L645 only, with the exact stated simple rho, delta, M_rho, H_rho and K_n arrays. Do not extend to multiple zeros, optimize constants, prove height-only growth, introduce actual positivity or reopen fixed norm reserves.

## Reused coverage and precise limits

The full source record is
`2026-11-01-vertical-pick-quantitative-pole-detection.md`, saved before
the producing research turn and left unchanged. Its hypotheses and
inspected proof cases are sufficient for an audit of that same target.
L645 gives the precise primary citations in its canonical proof. There
is no changed source, essential unread lead or reason for a new broad
literature search. This separate literature turn approves reuse for the unchanged audit;
it does not certify L645.

Essential local input is L018: the entire completion, its derivative
and safe-node nonvanishing. L258 is a different growth-dependent
witness and C644a a fixed-reserve contrast, not premises of L645.
No cross-notebook theorem is used. Reuse the saved comparison of the
external qualitative criterion only as overlap evidence, not as an input.

The bounded audit should check every step of the canonical proof:
the diagonal implication Re F(s_j)>=0; exact congruence to the finite
disk Pick matrix; exclusion of the constant-one inverse with preservation
of other unimodular constants; Borel–Caratheodory for -P with M=1;
the bound on the xi-multiplied residual; the disk inclusion of all
nodes and rho; the uniform q_delta<1; and the floor-plus-one threshold.
Accept only if the claimed implication for each n and stated C_delta
survive, or repair a precise failure while preserving its evidence.

Do not assume lower bounds for |xi'(rho)|, height-only control of H_rho,
actual positive-real continuation, matrix positivity, or simplicity of
other zeros. The comparison with floor(log gamma) is conditional on
the displayed strict growth inequality, and a multiple specified zero
remains outside scope. Independent signed arithmetic control is still
missing; this audit is not a candidate RH review.

Mathlib: the supporting Borel–Caratheodory statement/proof was inspected
at the frozen commit. Full finite interpolation, Blaschke division and
the whole detector have not been checked for matching formal coverage;
no absence claim or local Lean replay is made.

## Recovery source verification, 1 November 2026

LITERATURE_REASON: The supervisor reported missing direct source URLs in
this ready audit assessment. This bounded repair checks access and precise
source scope; it does not repeat discovery or extend the mathematics.

[Bolotnikov, publisher PDF](https://files.ele-math.com/articles/oam-04-08.pdf):
read pp.151–153, definitions (1.1)–(1.7) and all of Theorem 1.1. The
Schur class maps into the closed disk. The statement includes singular
PSD matrices and their unique finite Blaschke interpolant, as well as
positive-definite data. The text explicitly identifies simple-value
interpolation as the case with each jet length one. These are the cases
needed by the audit; no generalized negative-index theorem is imported.

[Zakeri, author notes](https://zakerimath.com/CAbook/COM.html):
read the complete Section 8.3 paragraph following Example 8.33, including
the removable quotient and boundary-modulus maximum-principle argument.
It gives the pointwise finite-product bound, with repeated zeros, without
boundary continuity of the original function. The page is unversioned;
accessed 1 November 2026. Disk rescaling and the particular residual
remain applicability checks in the mathematical audit.

[Mathlib, frozen source](https://raw.githubusercontent.com/leanprover-community/mathlib4/0d3fb85496130669f472d62be6f25999ca085c59/Mathlib/Analysis/Complex/BorelCaratheodory.lean):
read lines 37–110 completely. The general theorem at lines 98–110
requires differentiability on the open ball, positive radius and positive
M, and permits Re f <= M. Its proof handles the nonzero anchor by
subtracting f(0); the preceding Schwarz-transform proof treats the
denominator. Thus the audit may use the already specified M=1 rather
than an unsupported M=0 substitution. No Lean replay was performed.

Reused the saved overlap screen and checked the producing history
`history/2026-11-01-vertical-pick-quantitative-detector-01.md` and
`ATTEMPTS/2026-11-01-vertical-pick-uniform-fixed-reserve-stop.md`. L258
remains a different growth-priced witness; C644a remains a fixed-reserve
obstruction, not a premise. No source changed the sign/growth gaps.
This is a process repair with confirmed standard-tool coverage, not a
new mathematical input or a completed proof audit. Continue on exactly
the TARGET above; repair or reject L645 if its stated hypotheses fail
the bounded audit. Do not extend to multiple specified zeros or infer
height-only control.
