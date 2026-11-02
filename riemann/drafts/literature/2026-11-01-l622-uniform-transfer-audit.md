# L622 uniform transfer: source scope approved; critical audit pending

TARGET: Critically audit L622's coefficient-uniform transfer bound (1) for arbitrary unit complex coefficients and one common real observer, checking complex source weights, collision-safe differentiation, conjugate orientation, gcd summation and completion error without attempting a spectral sign.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed collective-arithmetic-signed-spectrum and collective-arithmetic-spectral-test searches, stronger-source comparisons and failures; inspected L622 Sections 1–4 against their scope and the primary theorem below. No discovery search was repeated; no novelty claim.
SOURCE_EVIDENCE: Reopened Hughes–Young https://arxiv.org/pdf/0709.2345v2#page=3, (11)–(17)/Theorem 1.1, printed pp. 3–5, including both local-factor orientations and the p. 5 complete-sum holomorphy remark citing CFKRS Lemma 2.5.1; reused the prior inspected Lemma 6.9/(139)–(155) cases. Local applicability ranges inspected: L619 Sections 1–3, 5 and its H=T audit; L471 (7); L465 Sections 1–2, 5 and its DLMF 5.11.1–2/5.11(ii) imports.
COMPARISON: Exact-source coverage is adequate for the independent audit of the existing specialization. The theorem states nonnegative weights, not L622's complex phase weights; that extension and its uniformity remain proof obligations, not imported conclusions. Complete-sum holomorphy is explicitly covered by the primary remark. No stronger moment theorem or new spectral premise is needed to begin this audit.
GAP: Critically verify or reject L622 (1), including Section 4 as well as Sections 1–3: all-orders source-weight bounds, uniform nonnegative decomposition, holomorphic total error, collision-safe extraction, conjugate orientation, gcd multiplicities, coefficient-summed error and zero-safe completion. Source readiness certifies none of these local steps.
REASON: Approve the unchanged target for a conceptual audit under named arithmetic and holomorphy imports; no essential unread source passage was identified. Do not reprove those imports or reopen the parked scalar cost, row, freezing, prefix or boundary tests.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED nomination needed separate exact-scope approval; this turn matched its obligations to reusable primary coverage, without repeating arithmetic discovery.
SCOPE: Only bound (1) with fixed nonnegative smooth w of integral 1, T<=X<=2T, N=floor(T^(1/100)), arbitrary complex coefficients of squared norm 1, one common real unit observer and the exact phase. Includes completion in Section 4; excludes Section 5's row-sum result, a spectral sign and any enlarged observer/window family.

## Completed source-scope review — 1 November 2026

This is a LITERATURE / NOVELTY_UNCHECKED step. Outcome STALLED:
the source check approves execution scope but supplies no new mathematical
evidence, correction or source-overlap obstruction. It does not count as
a mathematical advance or renew the mathematical exploration budget.
No lemma, mathematical script, DAG or argument overview was changed.

### Primary statement and reuse boundary

The reopened PDF identifies itself as arXiv:0709.2345v2, 27 September
2007, compiled 26 November 2024: C. P. Hughes and M. P. Young,
*The twisted fourth moment of the Riemann zeta function*, J. reine
angew. Math. 641 (2010), 203–236. Theorem 1.1 assumes coprime h,k,
hk<=T^(2/11-epsilon), complex shifts O(1/log T), and a nonnegative
smooth weight supported in [T/2,4T], with every fixed derivative
O_j(T0^(-j)) and T^(1/2+epsilon)<<T0<<T. Its six-term main integral
has prefactor 1/sqrt(hk); its raw error is
O(T^(3/4+epsilon)(hk)^(7/8)(T/T0)^(9/4)). Formula (14) specifies
both prime-power increment orientations. The printed p. 5 remark
asserts holomorphy of the complete main expression and cites CFKRS
Lemma 2.5.1's permutation-sum integral representation. These are
named imports; neither manuscript proof was independently audited.

The ready collective comparison already read the general prime-power
proof cases and excluded stronger results with different coefficient
conventions. That assessment is reused. No essential new divisor
calculation, holomorphy source or amplified positivity theorem is
required for this audit. In particular, the theorem's complex-shift
scope does not dispense with proving the complex-weight extension.

### Exact obligations approved for the next mathematical turn

The following is an audit checklist, not its execution or a proof.

- Check L622 (3)–(6) against (11)–(17), retaining the original
  h/k orientation, all six terms and the ordinary a^*Ka convention.
  Hermitian symmetrization must preserve the actual real integral.
- Check the analytic gamma branches and every fixed t-derivative
  needed for the phase weight, uniformly on a neighborhood of the
  shift polydisc. L465's analytic sector input is covered; the
  all-orders adaptation in L622 (7)–(8) must still be audited.
  The relevant gamma arguments do not import L465's saddle-order
  restrictions or any zero-free result.
- Verify the uniform constants in the nonnegative-weight decomposition
  and source application with eta=1/100 and T0=T. Its real/imaginary
  decomposition need not itself be holomorphic: the claimed total
  remainder must be justified separately as a difference of analytic
  integrals. Use the imported complete sum at every collision, and
  check the asserted local denominator nonvanishing in (10).
- Replay the full finite gcd sum, diagonal multiplicities, Cauchy
  factorials and common-observer normalization. Do not import the
  unaudited summed estimate from L620 or infer uniformity from fixed
  pairs. Compare the result with the precise error asserted in (1).
- Include Section 4. The H=T application audited in L619, rather than
  its other window cases, supplies the proposed absolute observer
  bound. L471 (7) and L465 Section 5 supply the stated completion
  ingredients; verify their actual use on [T,3T], including zeros,
  the polynomial prefactor and the amplifier's absolute cost.

The recorded row-dominance and local-factor-freezing stops were
checked in their specific ATTEMPTS files. They neither settle this
transfer nor authorize repeating their spectral tests. The parked
radial-cost review is likewise not reopened. No cross-notebook input
is needed; full matching Mathlib coverage remains unchecked/unknown.

Success means a complete replay of bound (1) under the exact stated
imports and hypotheses, with any necessary repair explicit. A concrete
mismatch must qualify or invalidate the bound rather than be hidden.
Failure to justify one analytic step is grounds to isolate it, not
to infer a spectral sign. Passing would certify a conditional local
application only; pointwise initial signs, the growing signed spectrum
and all-degree mixed positivity remain open. No new lemma or reproof
is authorized merely to fill a quota.

DECISION SPECIALIZE licenses REPRODUCTION for this audit of a known
theorem application, with proof_audit/conceptual_audit routing. The
earlier nomination has now received its separate source approval;
the next action stays exactly the same and needs no discovery refresh.

## Historical nomination — superseded by the completed review above

The following original nomination is retained as historical context;
its pending-approval instructions no longer apply.

This nomination does not perform or approve the mathematical audit.
The next invocation is literature-only under REVIEW_REQUIRED. It should
reuse [the collective comparison](2026-11-01-collective-arithmetic-signed-spectrum.md)
and [its application coverage](2026-11-01-collective-arithmetic-spectral-test.md)
while determining whether any essential source passage remains missing
for this precise audit. An unchanged covered theorem needs no fresh
discovery search. Do not reopen the parked radial moment under an
audit label.

Essential later local inputs are L622 Sections 1–3/(1), L619's audited
H=T complex germ and absolute bounds, L471's completion identity and
curvature bound, and L018/L465 as qualified in those files. Read only
the ranges needed to check their actual use. Hughes–Young and the
CFKRS holomorphy statement remain named imports; their manuscript
proofs need not be reproved or silently reported as independently
audited. No cross-notebook input is needed. Mathlib matching is unknown.

The audit's success test will be a full coefficient-uniform error
replay, with every assumption matched to its source and every
normalization/conjugation checked. A concrete unrepairable mismatch
should qualify or invalidate the transfer instead of being hidden.
Passing the audit would certify only this conditional local transfer,
not the spectrum, initial signs, radial inequality or RH.

After source approval the appropriate mathematical task is
proof_audit/conceptual_audit, deep_research/xhigh: analytic parameter
dependence and extension from nonnegative to complex weights require
logical scrutiny beyond arithmetic replay. No creative escalation is
claimed. This scoped radial review found no new central mechanism
with adequate quantitative coverage; that is the current blocker to
a justified creative attempt, rather than a reason to relabel a
routine specialization as creative. PROGRESS.md owns current routing.
