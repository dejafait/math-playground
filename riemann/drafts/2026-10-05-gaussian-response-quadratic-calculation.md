# Response quadratic margin — working checkpoint, 2026-10-05

Approved target and scalar coverage are the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-05-gaussian-response-quadratic-sign.md`.
Main gap: global actual-theta mixed positivity. The bounded intermediate
test is the lower bound for the first regulator response's quadratic
term at scale A²T⁴L². It could supply one input to L367's signed comparison;
the linear cross term, actual-theta sign and higher levels remain open.
Continue only if the positive leading term uniformly dominates every
error, including at zeros of G; otherwise preserve the failed comparison.

Existing changes were inspected only in this notebook and preserved.
L005, L358's normalization, L366's identity and audited qualifications,
and L367's quadratic definition were read. Existing calculations give
upper jets and unsigned product subtraction, not this lower bound.
The recorded L365 common-global-sign failure concerns fixed regulators
and is not reopened by this response-only target.

Unfinished calculation: with t=ξ, s=1/4+it/2 and Z=ζ(5/2+it),
L366's reflected quotient and gamma recurrence appear to give
G=Re(Q b Z), b=−s(s+1/2)/π. Its modulus relative to Q is
asymptotic to t²/(4π), and its phase derivative differs from L358's
gamma phase derivative by O(t⁻²). Absolute right-line zeta jets and
L005's reciprocal lower bound should make the phase-square leading
term dominate. Still to check: exact reflected algebra, all signed
projection terms, controlled gamma derivatives, negative frequencies,
and conversion from |t| to T and log|t| to L. No conclusion is yet
recorded here. Full proof, if successful, will be in a canonical lemma.

## Completion

The bounded attempt succeeded. Full carrier algebra, scalar applicability,
uniform error bounds and the explicit positive constant are canonical in
`lemmas/L368-first-regulator-response-quadratic-margin.md`.
The unfinished paragraph above is preserved as the initial checkpoint,
not as a separate proof. This is a local reproduction/specialization;
the linear coefficient and actual-theta sign are still unresolved.
Current routing and the single next action are solely in PROGRESS.md.
