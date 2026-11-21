# Weighted endpoint error cost — specialization nomination

TARGET: Specialize Gorodetsky's Lemma 5.2 at s=1 to L988's two endpoints with H=exp(n), and test whether the complete cutoff and jump error is o(exp(n/2)*n^(-3/2)) without prime-power separation.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review254 followed uniform Landau and weighted truncated-explicit-formula searches to the primary weighted theorem; exact local searches found no prior coverage of Gorodetsky2211.08973. Reuse review249's global Laguerre-bound coverage and step253's audited finite E_n definition; do not repeat discovery for these unchanged tools.
SOURCE_EVIDENCE: [Gorodetsky2211.08973v6](https://arxiv.org/pdf/2211.08973v6#page=15), Lemma5.2 p15/(5.5)-(5.6), s=1 convention and complete AppendixA pp21-22 inspected in review254; canonical transcription and qualifications in foundations/2026-11-10-finite-weighted-landau-input.md. [DLMF18.14.8](https://dlmf.nist.gov/18.14.E8)'s degree/parameter/domain contract is reused from review249 and audited L988; no derivative asymptotic is needed.
COMPARISON: The source already proves the finite weighted formula uniformly with its full proximity error and closed height. It does not state the two-endpoint n-dependent K_n specialization or its error relative to L987's benchmark. Only this normalization and error comparison need development; no contour reproof, novelty claim or signed-prime theorem is justified.
GAP: Form the exact finite sum of E_n(rho) with both endpoint signs, the full K_n including -1, weighted arithmetic prefixes, double-pole constant, trivial-zero series, midpoint/full jumps and every source error; establish or refute the stated little-o for the cutoff/jump error only.
REASON: A bounded known-tool specialization tests whether endpoint separation is a real obstruction to restoration at H=exp(n). Passing isolates a technical cost and leaves the signed prefixes unpaid; failure parks this cutoff choice with the exact offending term. No such bound is derived in this literature turn.
LITERATURE_REASON: Supervisor reported the missing direct source URL in this ready nomination; this bounded recovery review repairs traceability and approves the unchanged target, reusing review254 rather than repeating discovery or deriving the specialization.
SCOPE: Actual zeta zeros with analytic multiplicity, every integer n>=2, x=exp(n),exp(2n), H=exp(n), closed symmetric zero cutoff; exact sharp block and full arithmetic endpoint convention. No RH, simple zeros, prescribed clearance, infinite-height exchange, low-zero cancellation, B_n sign or L984(H).

## Imported tools and permitted calculation

Use the [canonical source input](../../foundations/2026-11-10-finite-weighted-landau-input.md),
not an unweighted Landau theorem. The source explicitly includes
s=1; there is no need to take an unproved singular-parameter limit.
The x,T hypotheses hold at both intended endpoints. All zero sums
in the proposed identity are finite. Analytic multiplicity and the
closed ordinate cutoff must agree with audited L988.

Use L985 only for the exact finite Laguerre connection and L988
for T_n,E_n,R_n definitions; its high-zero R_n tail is context,
not an estimate for the restored endpoints. Use L987 only to name
the comparison scale, without asserting an actual zero quartet.
The theorem's S_1 has half weight at a prime power. Restore that
half-jump when writing full arithmetic prefixes; keep the left
and right endpoint signs separately. Do not assume a positive
arithmetic or zero-ordinate distance beyond the theorem contract.

The reused global inequality is DLMF18.14.8: for integer d>=0,
alpha>=0 and u>=0,

    exp(-u/2)*|L_d^(alpha)(u)| <= (alpha+1)_d/d!.

Its source/version/attribution and overlap are in review249.
The intended degree n-1, alpha2 and u=n,2n meet these hypotheses.
Calculate the normalization and all n dependence in the later
attempt, retaining -1 before using absolute values. Bound the
complete source remainder and any full-endpoint conversion cost;
if elementary proximity comparison is used, justify it for the
nearest *other* prime power, including an exact prime-power x.
Do not silently replace the proximity factor by an inverse
distance assumption. No numerical sampling is necessary.

Continuation test: accept this technical component only if the
complete uniform cutoff/jump error is little-o of the stated
benchmark. Otherwise record the precise term preventing it and
stop this height choice. Even a passing test does not sign the
weighted prefixes or identify B_n: those terms must be displayed
as unresolved arithmetic quantities. No repeated absolute-tail
refinement or new creative label is authorized by this review.

## Separate approval and direct-source repair — step255

On 10 November2026, the separate literature-only approval checked
[the primary v6 statement, Section5.2](https://arxiv.org/html/2211.08973v6#S5.SS2),
including the definition immediately before Lemma5.2 and the
explicit s=1 sentence immediately after its error bound. The PDF
link in SOURCE_EVIDENCE fixes the cited version and printed p15;
the HTML uses equations(5.10)-(5.11). The source has x>=4,
T>=2+|Im(s)|, a midpoint arithmetic sum, a closed zero cutoff,
and the nearest-other-prime-power error, as recorded in the
canonical foundation. Reuse review254's completed AppendixA
inspection; no new proof inspection or contour reproof is needed.
The direct DLMF equation link also confirms its nonnegative
argument and alpha>=0 contract; review249's coverage is reused.

Approval is for the unchanged bounded specialization only. This
repairs the missing direct-source URL; it establishes no new
bound and does not repeat the source import as an advance.
DECISION remains SPECIALIZE and permits REPRODUCTION. The next
research turn must inspect the relevant L985/L988 definitions
before calculating. The target, benchmark, signed-prefix gap and
continuation/abandonment test above are unchanged. Full matching
Mathlib coverage remains unchecked.
