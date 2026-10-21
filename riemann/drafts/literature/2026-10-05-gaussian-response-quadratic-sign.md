# First regulator response — quadratic sign source comparison

TARGET: Determine whether L366's response G satisfies G′²−GG″≥c A²T⁴L² for some c>0 and every sufficiently large |ξ|, with T=1+|ξ| and L=log(2+|ξ|).
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Four bounded exact-statement/terminology queries listed below; inspected DLMF scalar statements and their sector/remainder restrictions, reused the recorded primary generalized-Laguerre comparison, and checked local L005/L358/L366/L367 and the common-threshold failure.
SOURCE_EVIDENCE: NIST DLMF v1.2.8 (2026-09-15), 25.2.1/11, 5.11.1–2/9/12–13 and §5.11(ii), 5.15.8–9; reused Csordas–Vishnyakova (2013), Theorem 2.3, Remarks 1.3 and (1), pp. 1644–1646, via the saved coupled-transfer assessment; local L005 and audited L366 (1), L358 (3).
COMPARISON: Inspected sources cover right-half-plane scalar series/product inputs and sector-controlled gamma jets; the full all-level criterion is not a sign theorem for this response. The missing difference is the real-projection quadratic specialization with a uniform margin at the proposed scale, including zeros of G.
GAP: Establish or refute the proposed uniform lower bound by assembling the reflected response, absolute Dirichlet derivative bounds and gamma carrier estimates without dividing by G; no quadratic lower bound is imported or derived here.
REASON: Essential scalar coverage is accessible and adequate for one bounded specialization; no matching ready-made nonlinear theorem was established by this screen, and no novelty is inferred.
LITERATURE_REASON: The target changed from perturbation-error control to a lower sign margin for the reflected response on Re s=5/2; the previous error audit did not assess this assertion.
SCOPE: Exactly the response G and positive A defined in L366/L358, real sufficiently large |ξ|, ordinary frequency derivatives through order two and the stated A²T⁴L² lower-bound scale. No actual-theta sign, linear-cross-term control, higher-level sign, regulator-uniform return onset or common global regulator threshold.

## Search and inspected evidence

Queries actually submitted:

- `"Laguerre" "real part" "Dirichlet" inequalities`
- `zeta absolutely convergent half plane real projection gamma Laguerre inequality`
- `"Laguerre inequalities" "Dirichlet series"`
- `"real part" "completed zeta" "Laguerre"`

No full matching response-tail theorem was identified in inspected material.
Search snippets are not theorem evidence. The cusp-form Turán articles,
level-set papers, coefficient-sequence papers and purported recent
square-variable half-plane preprint remain unread leads, unused as inputs.
None is essential to the direct scalar specialization assessed here.
This bounded search makes no originality claim.

Newly inspected primary/reference passages, with DLMF's displayed version
1.2.8 and release 2026-09-15 confirmed on the retrieved page:

- [DLMF 25.2.1](https://dlmf.nist.gov/25.2#E1) states the zeta Dirichlet
  series for Re s>1; [25.2.11](https://dlmf.nist.gov/25.2#E11) states
  its Euler product on that same domain (source: Apostol, 1976, p. 231).
  These are scalar inputs, not a Laguerre inequality. The response's
  reflected line Re s=5/2 lies strictly inside this domain. Uniform
  lower bounds and differentiated-series estimates still require their
  elementary applicability arguments in the later proof; nonvanishing
  alone is not a uniform positive lower bound.
- [DLMF 5.11.1–2](https://dlmf.nist.gov/5.11#E1) gives log-gamma and
  digamma expansions on |arg z|≤π−δ. Its
  [complex remainder paragraph](https://dlmf.nist.gov/5.11#ii) bounds
  remainders by the first omitted term times the stated secant powers.
  [5.11.9](https://dlmf.nist.gov/5.11#E9) gives gamma modulus asymptotics
  uniformly for real parts in compact intervals. The
  [ratio formulas 5.11.12–13](https://dlmf.nist.gov/5.11#E12) require
  fixed shifts and the same sector. The relevant gamma arguments have
  real parts 1/4 and 5/4 and equal imaginary height; these are fixed
  shifts, unlike a growing shift. These statements do not justify
  differentiating an uncontrolled O term. Use the analytic remainder
  and Cauchy estimates already covered in foundations/notation-and-inputs.md,
  or the separately inspected polygamma formula. If using 5.11.11,
  retain its |arg z|≤π/2 domain and K=1 replacement factor 4.
- [DLMF 5.15.8–9](https://dlmf.nist.gov/5.15#E8) gives trigamma and
  higher-polygamma asymptotics on |arg z|≤π−δ. The fixed positive-real-part
  gamma arguments at large positive or negative height remain inside
  a closed sector away from the negative real axis. This supplies scalar
  derivative coverage, not a quadratic sign assertion.

The three attempted `?plaintext` equation URLs returned internal errors;
the complete relevant formulas and hypotheses were instead read on their
accessible section pages. No essential source blocker remains. Books
referenced by DLMF remain unread; the cited DLMF statements themselves,
rather than an unseen book proof, are the approved supporting inputs.

Reuse the primary criterion comparison in
 drafts/literature/2026-10-05-gaussian-coupled-laguerre-transfer.md:
Csordas–Vishnyakova, *Central European Journal of Mathematics* 11(9)
(2013), 1643–1650, DOI 10.2478/s11533-013-0269-x,
[Theorem 2.3 and Remarks 1.3](https://d-nb.info/1372516522/34).
Its all-level, all-real-point hypothesis gives Laguerre–Pólya membership;
it neither establishes that premise for G nor supplies this quantitative
first-level margin. The previously inspected statement and essential
proof cases are reused without another source read. Paris's scalar
Mellin tools need no new application: the audited response identity is
already available, so a new contour derivation would duplicate L366.

## Local comparison, relevance and later obligations

Read L366's hypotheses and (1)–(2), its reflected-quotient justification,
L358's exact normalization (3), and L367's signed quadratic definition.
Read L005 in full: its absolutely locally uniform prime-log series on
Re s>1 is a ready local input for scalar lower bounds. The Weierstrass
holomorphic-limit theorem and analytic-remainder/Cauchy estimate already
named in foundations/notation-and-inputs.md supply standard support;
any derivative majorant and uniform constant must be written explicitly
in the later specialization. L366 supplies upper jet estimates only.
L367 retains the quadratic term without signing it; re-proving either
upper bound is not the present target.

The main gap is global actual-theta mixed positivity. The intermediate
target could control L367's quadratic response term and inform a later
signed comparison. Even success leaves its linear cross term, the sign
of F_0, remainder-to-margin comparison, higher levels, heights above
forty and endpoint arithmetic margin unresolved.

A bounded later attempt should extract the complex carrier multiplying
the right-line zeta value from L366 (1), control its modulus and first
two frequency jets by the cited gamma inputs, and bound the right-line
zeta jets and reciprocal using absolute series/product majorants.
Then assemble the real-projection quadratic expression retaining every
envelope and phase derivative. Test whether the leading term has a
phase-independent positive lower margin at A²T⁴L² scale and whether all
remaining terms are uniformly smaller. This is a proof plan, not a
new asymptotic identity or a proved sign result. Work at zeros directly;
never take the logarithm of G or divide by it. Negative frequencies
require the inherited conjugation/evenness qualification.

Continue only if a c>0 and finite onset follow with all error comparisons
justified. If the leading term fails the scale/sign test, or the scalar
bounds cannot make the signed error smaller, record that precise failure
and abandon or narrow this particular margin certificate. A failed
search alone would not justify abandonment. Any reproof should be only
the elementary nonlinear assembly absent from the cited scalar inputs,
not a reproof of their gamma or Euler-product theorems.

The stop in ATTEMPTS/2026-10-04-gaussian-common-first-sign-threshold.md
remains intact: L365 concerns fixed positive regulators and does not
supply a regulator-uniform onset. This response-only test neither
reopens nor disproves that stop. No lemma, mathematical script, sign
calculation or proof audit was performed in this literature-only turn.
The initial REVIEW_REQUIRED placeholder is superseded by prospective
SPECIALIZE coverage of the unchanged target, not retroactive validation.
New coverage remains subject to the supervisor's separate next-turn
approval before a mathematical invocation.

## Mathlib and outcome

Full response-tail lower-bound coverage: **not checked**. L005 records
supporting `riemannZeta_eulerProduct_exp_log` and
`riemannZeta_ne_zero_of_one_lt_re` with its direct documentation link;
that supporting coverage is inherited, not newly verified, and is not
a matching quadratic theorem. No absence or novelty inference is made.

Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. The new evidence
is an adequate prospective scalar-source comparison for the exact target;
no mathematical lower bound, improved sign range or RH advance is claimed.
