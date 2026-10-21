# Response quadratic margin — critical-audit coverage

TARGET: Critically audit L368's response quadratic margin, checking carrier normalization, uniform remainders, zeros of G and both frequency signs.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the four exact-statement and terminology searches and inspected source comparison in drafts/literature/2026-10-05-gaussian-response-quadratic-sign.md; compared L368's audit obligations with L005, L358 (3), audited L366 (1), foundations and the recorded L365 stop; no new external search.
SOURCE_EVIDENCE: Reused NIST DLMF v1.2.8 (2026-09-15), 25.2.1/11, 5.11.2 and section 5.11(ii), 5.15.8–9; gamma recurrence and Euler integral in foundations/notation-and-inputs.md; local L005, L358 (3) and L366 (1), with its completed audit recorded in history/2026-10-05-gaussian-response-critical-audit.md.
COMPARISON: The assessed sources cover the fixed right-line series/product, uniform sector gamma jets and exact reflected response input, but no matching nonlinear quadratic-margin theorem; the audit must independently verify L368's family-specific real-projection assembly and uniform lower-bound scale.
GAP: Mathematical verification of L368 (3)–(10), normalized asymptotic (1), finite onset (2), zero-safe normalization and both frequency signs remains pending; coverage approval is not validation of those formulas.
REASON: The unchanged scalar hypotheses fall within ready source coverage, permitting one bounded critical audit as a reproduction/specialization; no essential unread source or new discovery search is required.
LITERATURE_REASON: The previous turn created a separate REVIEW_REQUIRED critical-audit target; this turn compares that exact obligation with reusable coverage rather than repeating browsing for scheduling.
SCOPE: Only L368's real-frequency response G from L366 (1), positive A from L358, two ordinary frequency derivatives, uniform eventual A²T⁴L² margin, zeros of G and both frequency signs; no actual-theta, linear-cross-term, higher-level or regulator-uniform sign claim.

## Reused source evidence and applicability

The response-sign assessment records the actual queries, inspected statements,
source version, inaccessible equation-URL attempts and unused leads. Its
accessible section-page evidence resolves those URL failures; there is no
remaining essential source blocker. The books cited by DLMF and unrelated
search leads remain unread and are not inputs. No novelty follows from that
bounded search. This turn read the full assessment and L368, the full L005,
the hypotheses and relevant formulas of L358/L366, the recorded L366 audit,
and narrowly selected foundation passages and failure history.

[DLMF 25.2.1 and 25.2.11](https://dlmf.nist.gov/25.2#E1)
state the Dirichlet series and Euler product for Re v>1. L368's fixed
v=5/2+it is within that domain. L005 already supplies the absolutely,
locally uniformly convergent Euler logarithm there. The audit must check
its use for a uniform lower bound, and check the displayed absolute
majorants and differentiated-series justification; nonvanishing alone
would not suffice. No continuation of prime positivity into the critical
strip is covered or needed for this target.

[DLMF 5.11.2](https://dlmf.nist.gov/5.11#E2) and its
[complex remainder paragraph](https://dlmf.nist.gov/5.11#ii), together with
[5.15.8–9](https://dlmf.nist.gov/5.15#E8), provide the separately controlled
digamma/polygamma expansions on closed sectors away from the negative real
axis. The proposed s=1/4+it/2 has fixed positive real part, within that
assessed scope. The later audit must verify the error orders and real-part
estimates used, without differentiating an uncontrolled O term. Fixed
polynomial carrier factors require elementary rational checks, not a new
gamma theorem. Gamma recurrence is already a named foundation input,
justified there from Euler's integral on Re s>0; conjugation can be checked
from that integral and the absolutely convergent zeta series.

The exact reflected response is a local input from L366 (1), whose previous
critical audit is recorded separately. L358 (3) supplies the envelope
normalization identity, not the new lower bound. Repeating Mellin inversion,
contour shifts or the regulated numerical certificates would duplicate
established inputs and is outside this audit. The previously inspected
Csordas–Vishnyakova (2013), Theorem 2.3, DOI
10.2478/s11533-013-0269-x, as recorded in the response-sign assessment,
requires all levels and all real points; it is not a theorem giving this
response margin or an actual-theta sign. Its proof need not be reread.

## One bounded audit and decision test

The main gap remains global actual-theta mixed positivity. Independent
verification of L368 is the intermediate target; a surviving margin would
make its quadratic coefficient a checked partial input to L367. The linear
coefficient, actual-theta margin, higher levels, heights above forty and
endpoint arithmetic margin remain independent unresolved obligations.

The mathematical turn should independently check, rather than assume:

- L366's reflected identity, the completion factor 1/2, gamma recurrence,
  the carrier in L368 (3), its modulus (4), and the envelope's nonvanishing.
- The fixed-line absolute jet bounds and uniform Euler-log lower bound,
  including their convergence hypotheses and independence of frequency.
- The exact phase/envelope derivatives, sector remainders and all terms in
  the real-projection expansion, including envelope curvature and the
  signed cross term. Uniform upper jet estimates alone are not a margin.
- The passage to A²T⁴L² scale, the numerical coefficient and stated c,
  existence of a single finite onset, validity at zeros of G, and the
  conjugation/parity argument for negative frequencies.

Continue if that full claim survives with the stated uniformity, or if a
precisely qualified correction leaves a useful margin. A failed coefficient,
error order, domain or onset comparison requires recording the exact failure
and narrowing or abandoning this certificate; it does not refute RH. No
numerically evaluated onset is claimed. Division by G, a critical-strip zero
hypothesis or a regulator-uniform onset is neither approved nor implicit.

L365's stopped common-global-first-sign certificate remains preserved in
ATTEMPTS/2026-10-04-gaussian-common-first-sign-threshold.md. A response-only
margin is distinct from that fixed-positive-regulator problem; the proposed
audit does not reopen it. No mathematical audit or derivation was performed
in this literature-only turn, and no lemma, DAG or mathematical script was
changed. The new coverage is prospective, subject to separate next-turn
approval by the supervisor.

## Mathlib and completed outcome

Full response-margin or critical-audit theorem: **not checked**. Supporting
Euler-product coverage is inherited from L005, including
[riemannZeta_eulerProduct_exp_log](https://leanprover-community.github.io/mathlib4_docs/Mathlib/NumberTheory/EulerProduct/DirichletLSeries.html#riemannZeta_eulerProduct_exp_log).
No matching nonlinear theorem or absence from Mathlib is asserted.

Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. The new evidence is
exact audit-scope comparison with adequate reusable inputs. It establishes
no new mathematical result and does not validate L368; the mathematical
exploration budget remains unchanged.
