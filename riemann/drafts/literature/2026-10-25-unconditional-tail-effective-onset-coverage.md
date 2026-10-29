# Effective unconditional-tail onset — completed source comparison

TARGET: Assess whether the sources behind L464 and L465 provide explicit constants sufficient to place C465a's onset at or below t=3*10^12-1/2 for c_0=1.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Inspected paper 41 v4 Sections 4.2–4.4 and 11; checked DLMF 5.11(ii), Platt–Trudgian Theorem 1 and Section 2, and local L464/L465/C465a with the initial-sign assessment and L255. Exact retrievals and access limits appear below.
SOURCE_EVIDENCE: bramble_trace, paper 41 v4 (24 October 2026), Theorem 1a, (18a)–(18h), Section 4.4 and Section 11; NIST DLMF 5.11.1–2 and 5.11(ii); Platt–Trudgian, arXiv:2004.09765v1, Theorem 1, printed p. 2, Section 2. Sra v1 was not retrievable this turn; prior primary-read coverage is retained, not upgraded.
COMPARISON: The source-covered existential tail remains valid at its stated scope; the additional numerical requirement is unsupported by the inspected estimates. Explicit gamma bounds alone do not provide a complete effective onset.
GAP: Numerical zero-count constant, full saddle relative-error constants and validity thresholds, and their common-height comparison are missing. No quantitative specialization is approved.
REASON: Park the dependent numerical-overlap target: this is missing quantitative evidence, not a lower bound on the true onset or a refutation of overlap. Finite-height signs can be assessed independently.
LITERATURE_REASON: The numerical height requirement is outside the earlier existential assembly coverage; this review inspected the essential quantitative source scope.

## Relevance and discriminating test

The main gap is initial actual-Xi signs at unbounded heights, with global
mixed positivity independent. A numerical upper bound on the tail onset
could connect eventual tail coverage to a verified finite-height interval;
it would still leave low orders at larger heights unresolved. Continue to
a numerical calculation only with jointly applicable explicit constants
and thresholds. That test did not pass. No new lemma or mathematical
calculation was attempted.

## Primary passages inspected

1. [bramble_trace, Generalized Laguerre positivity at growing orders,
   paper 41](https://rstation.ai/problems/riemann_hypothesis/papers/41),
   displayed v4, 24 October 2026 07:18 UTC, accessed 25 October 2026.
   Section 4.2 retains implicit constants in (18a)–(18b), complementary
   arcs and the Xi gauge. Section 4.3 retains implicit local zero counts
   and hence an unevaluated C in (18h). Section 4.4 uses sufficiently
   large height. Section 11's finite controls do not certify uniform
   remainders. No numerical common onset is supplied in these passages.
2. [NIST DLMF 5.11](https://dlmf.nist.gov/5.11), equations 5.11.1–2,
   and Section 5.11(ii), first error-bound paragraph, accessed 25 October
   2026. For the expansions truncated at k=n−1, positive-real arguments
   have remainder bounded by the first neglected term; complex arguments
   acquire sec(arg(z)/2) powers 2n and 2n+1 respectively. These are
   actual quantitative component bounds. They do not specify the other
   constants needed by L465. No growing-disk specialization was derived
   during this literature turn.
3. Dave Platt and Tim Trudgian, [The Riemann hypothesis is true up to
   3·10^12](https://arxiv.org/pdf/2004.09765), retrieved PDF identifies
   arXiv:2004.09765v1, 21 April 2020. Theorem 1, printed p. 2, states
   verification through 3,000,175,332,800. The smaller stated height
   3·10^12 is within that range. Section 2, printed pp. 2–3, describes
   completed-zeta sign changes, Turing counting and Arb ball arithmetic.
   This is a precise published computational theorem input; the large
   computation was not rerun here. Publication: Bulletin of the London
   Mathematical Society 53 (2021), 792–797,
   [doi:10.1112/blms.12460](https://doi.org/10.1112/blms.12460).
   No simplicity assumption is needed for the proposed continuation.

## Local comparison, duplicates and access qualifications

L464's proof expresses its C through an unspecified uniform unit-interval
zero-count constant A and convergent sums. L465's displayed error (1)
retains C_(c_0,beta) and an unspecified validity onset. C465a's existing
construction also depends on T_A(c_0). None has been numerically bounded.
These facts locate the missing certificate without modifying those proofs.
The explicit gamma input does not close the zero-count, zeta-strip,
amplitude and Gaussian-error accounting obligations.

The initial-sign assessment already compared finite-height signs and
recorded their limitation. L255 already proves the noncentral product
mechanism on a smaller interval; repeating it as a new discovery would
be a duplicate. A finite-height continuation must handle central zeros
and distinguish nonnegativity from strictness. No RH claim results.

Sra's v1 PDF URL in that assessment returned inaccessible through the web
tool (also with a download query); a shell retrieval failed DNS resolution.
The Titchmarsh scan URL timed out twice. Previously recorded theorem-level
coverage remains in force. Exact Sra hypotheses were not freshly verified
here, and its equality clause must not be silently strengthened. These
access failures do not prevent the negative quantitative-source decision:
the inspected tail manuscript itself leaves the required constants open.
They also do not show the constants are intrinsically ineffective.

Queries: “Platt Trudgian Riemann hypothesis true up to 3 10 12 theorem 1
2021”; “site:suvrit.github.io riem-xi \"Theorem 1.3\"”. Only primary
sources above were used for the comparison. Mathlib coverage was not
checked; it has no bearing on this numerical-onset source gap.

## Route decision

Park the numerical-onset calculation. Reopening requires a complete
explicit remainder and count package, not more finite sample comparisons.
The independently testable proposed continuation is a finite-height sign
specialization, with L018, L024, L026, L027, L255 and Platt–Trudgian as
named inputs. Its source scope needs separate approval, especially the
central-multiplicity case; it assumes no effective tail onset or external
fixed-half-plane theorem. No PROOF.md or DAG change is warranted.
