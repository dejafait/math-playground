# Exact CCM trial trace — nominated standard specialization

TARGET: Specialize periodic Fourier endpoint averaging and Bernoulli jump subtraction to L761's exact trial at lambda=sqrt(13), retaining every seam/cutoff jump and proving an explicit N-tail bound for b(P_N k).
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step374's completed endpoint/jump comparison in 2026-11-04-ccm-projected-boundary-trace.md, including its local duplicate/failure search; no independent new search or mathematics is claimed in this nomination.
SOURCE_EVIDENCE: Lebl section4.3.2/Theorem4.3.1 https://www.jirka.org/diffyqs/html/moreonfourier_section.html ; Batenkov Math.Comp.84(2015) Definitions1/3, Proposition2/6, pp2329–2331 https://dimabatenkov.info/pdf/batenkov_complete.pdf ; DLMF24.8.2–3 https://dlmf.nist.gov/24.8 ; reused qualified Batenkov–Yomdin Lemma2.1 https://dimabatenkov.info/pdf/batyom_alg_fourier.pdf and Osipov–Rokhlin1301.1707v1 Theorem1/(27), Theorem3/Remark6 https://arxiv.org/html/1301.1707v1#S3.SS1 .
COMPARISON: Endpoint averaging and jump subtraction are known. The identified difference is the exact logarithmic-coordinate specialization, complete jump inventory and effective remainder constant. CCM Lemma5.5/Corollary5.6 cannot replace that work without its periodic-domain hypothesis.
GAP: Establish the trial's one-sided data and an explicit tail constant with all normalizations; no such result is presently proved. Do not assume inversion parity, a trace for an L2 error, a nonzero limiting denominator or ground convergence.
REASON: A standard-method reproduction can now test the variable-N boundary question independently of the stopped fixed observable test. Separate source approval completed in step375; direct primary URLs are now in this exact-target assessment. Mathematical invocation remains future work.
SCOPE: Fixed lambda=sqrt(13), h=I4 phi0-I0 phi4, compact extension and basis exactly as in L761/L759; variable integer N>=1, boundary row b as in L760 extended to that basis size. No ground comparison, lambda-family result or Xi sign claim.

Use the parent assessment's bounded test and qualifications. The intended
mechanism is value-jump subtraction, the exact finite jump-model sum and
a paid piecewise derivative remainder. The canonical proof must identify
the periodic midpoint, keep the mean and endpoint-only r=13 convention,
include derivative jumps and justify all tail estimates. Use DLMF's
degree-one B1 model with its endpoint restriction; do not copy the source's
degree/termination wording literally. Derivative
constants may use the source integral representation with proved finite
denominators; an existential O-constant does not meet this target.
A trace bound alone supplies no denominator lower bound or normalized
observable accuracy. Keep C761a unchanged.

This is reproduction/specialization, not creative RH progress. Mathlib is
unchecked. This nomination contains no new trial formula, endpoint
evaluation, bound or proof; separate approval completed in step375.


## Separate source approval and URL recovery — step375

The exact TARGET and SCOPE above are unchanged. This is a process repair,
not an additional theorem or mathematical advance. On 2026-11-04 the
three direct sources below were reopened; remaining inspected source
coverage is reused from the parent assessment, not claimed as freshly read.

- [Lebl, section4.3.2, Theorem4.3.1](https://www.jirka.org/diffyqs/html/moreonfourier_section.html): the finite-partition definition requires finite inward values and a piecewise-continuous derivative. Both convergence cases were checked. The value at a jump is the periodic one-sided average; no rate is given.
- [Batenkov (2015), pp2329–2331, Definitions1/3, Propositions2/6, (2.1)–(2.3)](https://dimabatenkov.info/pdf/batenkov_complete.pdf): periodic matching through derivative order d is required for Proposition2. Section2 explicitly permits seam jumps; Proposition6 concerns the Bernoulli jump model's nonzero coefficients. The smooth remainder's asymptotic estimate is not an explicit trial constant. The model's displayed B_(n+1) formula controls its degree; retain the parent assessment's wording qualification.
- [DLMF24.8.2–3](https://dlmf.nist.gov/24.8): B1's Fourier identity is restricted to the open unit interval. It supplies no literal endpoint substitution. The parent assessment records version1.2.8; this check used the live formula page without independently reconfirming its release metadata.

The parent assessment's precise prolate regularity and CCM domain comparison
remain sufficient and unchanged. Their direct URLs are
[Osipov–Rokhlin v1, section3.1](https://arxiv.org/html/1301.1707v1#S3.SS1),
[CCM v1, section5.3](https://arxiv.org/html/2511.22755v1#S5.SS3), and
[Connes v1, sections6.3–6.4](https://arxiv.org/html/2602.04022v1#S6.SS3).
The qualified 2012 integration-by-parts proof is at
[Batenkov–Yomdin, Lemma2.1, pp280–281](https://dimabatenkov.info/pdf/batyom_alg_fourier.pdf).
These four sources were reused, not reopened in step375.

Local scope was checked against L761's Hypotheses and its recorded
endpoint-only r=13 convention, plus
[the fixed-cell stop](../../ATTEMPTS/2026-11-04-ccm-fixed-boundary-observable-miss.md).
No duplicate all-N trace bound was identified by the reused step374 search;
no broader novelty claim follows. L759/L760/L761/C761a remain the local
inputs. The variable-N extension is an explicit part of the approved
target, not a result already contained in fixed-N L761.

DECISION remains SPECIALIZE. The bounded test and all unpaid obligations
above remain in force: exact inward values, every cutoff and seam jump,
mean, normalization, derivative constants and an effective tail must be
proved during the mathematical attempt. The source supplies the method,
not this trial specialization. No L2-error trace, inversion parity,
nonzero limiting denominator or ground convergence is approved.
Mathlib remains unchecked. This approval permits a REPRODUCTION research
step on the exact TARGET; it establishes no new mathematics.
