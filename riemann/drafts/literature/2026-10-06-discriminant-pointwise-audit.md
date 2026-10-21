# Coverage for the finite discriminant audit

TARGET: Critically audit L370's zero-safe discriminant identity, L367 normalization and absolute envelope-curvature bound.
CHECKED: 2026-10-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the exact/stronger-result searches and duplicate comparison in 2026-10-06-discriminant-pointwise-decomposition.md; inspected the complete L370 proof, relevant L367 and L369 ranges, and the pointwise and prior L367 audit histories for the changed audit scope.
SOURCE_EVIDENCE: Reinspected NIST DLMF 1.13.4–1.13.5, 5.15.8 with its sector condition, 5.11(ii) complex remainder paragraph and 5.11.9; local L367 (1)–(3), (9), (12)–(15), L369 (4)–(7), and full L370.
COMPARISON: The audit has the same real C² pair, positive C² common envelope, ordinary jets and |t|≥40 domain as the prior EXPLORE assessment; inspected sources cover the named analytic inputs, but no full matching discriminant/sign theorem was established.
GAP: Independently validate L370 (2)–(8), every divisor and zero case, and the use of L367/L369 to obtain a finite uniform absolute bound; residual sign and relative margin are outside this audit.
REASON: Approve the saved bounded critical audit using adequate prior discovery coverage and inspected primary hypotheses; no essential missing source blocks it, and no new mathematical conclusion is approved by this review.
SCOPE: Audit only L370's existing finite identities and absolute bound for L367's actual family on |t|≥40, including its stated arbitrary-real-C² identity specialization; no new residual mechanism, sharp mixed mean, positivity or regulator-curve theorem.
LITERATURE_REASON: The newly written audit continuation required separate scope approval; primary polygamma hypotheses and the distinction between digamma remainder bounds and a separate derivative expansion were checked against the actual proof.

## Source scope and reuse

The prior assessment remains the discovery record:
`drafts/literature/2026-10-06-discriminant-pointwise-decomposition.md`.
Its recorded queries and inspected polynomial comparison are reused, not
repeated. No novelty inference follows from its unsuccessful exact-match
search. Local histories inspected were the October 6 pointwise source
review and reproduction and the October 5 L367 critical audit. No duplicate
independent critical audit of L370 was found in these records. L367's audit
already covers its strip specialization; the next audit checks its use here.

NIST DLMF online pages were read on 2026-10-06; a release number was not
captured, so no release-specific claim is made.
[1.13.4](https://dlmf.nist.gov/1.13.E4) fixes the determinant/Wronskian
convention. [1.13.5](https://dlmf.nist.gov/1.13.E5) uses two solutions
of the same equation 1.13.1 with analytic coefficients on a simply
connected domain. That additional hypothesis is unavailable here;
Abel's nonvanishing conclusions are excluded from the audit.

[5.15.8](https://dlmf.nist.gov/5.15.E8) states the separate Poincaré
expansion of psi prime as z tends to infinity with
|ph z|≤pi−delta, delta>0. The arguments 1/4+it/2 in L369
lie in such a fixed closed sector. This is the supporting source for
L369's derivative estimate, rather than differentiating a bare digamma
error. [5.11(ii)](https://dlmf.nist.gov/5.11#ii) bounds complex
remainders of 5.11.1 and 5.11.2 by sector factors times the first
neglected terms; its displayed paragraph is not itself an explicit
polygamma-remainder bound. No numerical polygamma constant is required
by the saved target. [5.11.9](https://dlmf.nist.gov/5.11.E9) gives the
vertical gamma-modulus asymptotic for real x and y tending to either
infinity, supporting L367's imported positive-envelope scale at x=1/4.
These statements cover the analytic input scope, not the pencil identity
or an actual-theta lower bound. No essential external proof case or
unread sharp-moment theorem is needed for this finite audit.

## Approved audit and decision test

The main gap is global actual-theta mixed positivity and the total L367
comparison margin. The intermediate target is reliability of L370's
existing zero-safe decomposition and absolute correction. Its plausible
use is to isolate a sound residual for a later independently assessed
arithmetic sign mechanism. This review does not perform that audit.

Essential inputs are L370 (1)–(8), L367 (1)–(3), (9), (12)–(15),
and L369 (6)–(7), with the actual positive A and ordinary derivatives.
Audit the denominator A⁴T⁴L⁴, the distinction between G/A and
G/(AT²), and all zero jets. Check the use of evenness, continuity
and the imported asymptotic in obtaining a finite unevaluated K_q,
and the retained constants E_0,E_1,D_0,D_1 in the coarse M bound.
The complete integer-polynomial certificate may be inspected as algebraic
evidence; its previous pass is not analytic verification. Reproof by
finite expansion is justified to independently check these precise
normalizations, including zeros, without a full matching source theorem.

Continue if all coefficients, admissible domains and absolute estimates
survive independent checking; if a coefficient or essential bound fails,
record the precise defect and repair or suspend the claimed input before
using it. Do not require residual positivity for audit success. No
F_0/G division, q derivative, common ODE, regulator differentiation,
real-zero premise or lower bound for the residual is available. L368's
positive response coefficient is a contrast, not a required dependency.
The residual sign, relative margin, full comparison, higher positivity,
heights above forty and endpoint arithmetic margin remain unresolved.
The sharp-mean SOURCE_BLOCKED route and L365 stop are preserved.

Full matching Mathlib coverage remains not checked; supporting determinant
or Wronskian material would not establish the actual-family bound.
No lemma, mathematical script, certificate or main argument was modified
in this literature-only source comparison. The audit is ready for a
separate research turn under this EXPLORE assessment, with REPRODUCTION
classification; this is coverage approval, not mathematical verification.
