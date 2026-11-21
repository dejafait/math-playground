# Audit continuation: uniform corrected modulation penalty

TARGET: Audit L744's fixed-family complete-energy penalty, checking the arbitrary-window smooth identity, uniform Fourier tails, exact pole cancellation and normalized correction error.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the unchanged mathematical scope and source search in 2026-11-04-uniform-neutral-modulation-energy-penalty.md and its joint-energy parent; step 287 narrowly checked L740-L743 and the recorded prime-only and generic-source stops. No new discovery search or novelty claim.
SOURCE_EVIDENCE: NIST DLMF https://dlmf.nist.gov/5.11.E2 and https://dlmf.nist.gov/5.11.ii, expansion/sector at 5.11(i) and first paragraph of 5.11(ii), directly retrieved and read 2026-11-04 in recovery step 288; Plancherel and smooth Fourier differentiation; audited L740 (4)/(5), L741 Section 2 kernel/symbol/pole identities and L743 (9)-(12). L744 is the proof to audit, not an independently certified input.
COMPARISON: This is the same fixed-K, fixed-M, fixed-chi specialization as the prior ready target, now written in L744. Known scalar asymptotics and finite arithmetic bounds are imported; the audit must verify uniform integration, correction and normalization rather than reprove those known results.
GAP: L744's proof has not received a separate audit. No bounded-frequency sign, growing-K/M estimate, moment-complement sign or unrestricted positivity is covered or supplied.
REASON: Recovery step 288 supplies direct primary URLs and approves unchanged source coverage only; independently inspect the claimed bound with all its quantifiers and the arbitrary-window smooth specialization before using it as a paid component. The separate source-approval step 288 is complete; it does not approve L744's correctness.
SCOPE: Only L744 (1)-(4), the explicit estimates (5)-(18), and their fixed-family hypotheses. No RH input, source positivity computation, closed-domain extension, phase-return theorem, energy-Rayleigh equality or new sign mechanism.

The [prior assessment](2026-11-04-uniform-neutral-modulation-energy-penalty.md)
already covers the mathematical statement and the analytic tools. The
completed [parent comparison](2026-11-04-joint-energy-mechanism-nomination.md)
records the source searches, overlap and failed direct imports. Its
external envelope lead and Zhu's computational positivity are unnecessary
for this audit. No inaccessible source is an essential input.

The [proof to audit](../../lemmas/L744-uniform-neutral-modulation-energy-penalty.md)
uses DLMF's n=1 remainder on z=1/4+i xi/2, whose argument stays in the
right half-plane. Check the global bound for the real symbol, not only
its asymptotic approximation. Check that the probability Fourier measure
has the stated second and fourth moments, including uniformly varying
profiles and the region eta near -t. Check the zero extensions and both
cell endpoint derivatives in the twice-integrated moment estimates.

For the energy identity, use L740 directly and only L741's smooth kernel
identities. L741's L=log(3) domain/sign theorem is not an arbitrary-L
input. Both complex pole moments must vanish exactly; all finite delays
must retain the factor two. Check the positive weight dominating the
absolute symbol, the fixed correction's H2 estimate, and the logarithmic
factor multiplying the norm defect in the normalized quotient. K, M and
chi remain fixed at every limit. No claim uniform in their growth is
under review.

Pass only if the full estimate holds uniformly for every admitted w
and both signs of t with a nonzero denominator. A missing hypothesis,
factor, endpoint term or nonuniform estimate must be repaired canonically
or recorded as a failure. Full matching Mathlib coverage is unchecked;
no formal verification is claimed. Planned classification is REPRODUCTION
and the proof task is a conceptual audit, not a creative central-sign
attempt. No new intermediate mathematics is approved by this record.


## Separate source approval and URL recovery, step 288

LITERATURE_REASON: The supervisor required a literature-only recovery because the ready audit assessment lacked a direct source URL. This is a source-access/metadata repair for the exact saved target, not an additional mathematical investigation.

Read the live [NIST DLMF expansion 5.11.2](https://dlmf.nist.gov/5.11.E2)
and [Section 5.11(ii), first paragraph](https://dlmf.nist.gov/5.11.ii)
on 4 November 2026. The expansion uses the principal logarithm in
sectors separated from the negative real axis. The remainder paragraph
bounds the digamma truncation error by the first omitted term multiplied
by sec^(2n+1)(arg(z)/2). These are the cited scalar inputs; the
right-half-plane substitution in L744 is within the stated sector.
This confirms source scope only, without deriving an energy estimate.
DLMF's equation and section identifiers specify the inspected live
version; the page cites Olver (1997b), pp. 87–88 and 293–295.

Reuse the prior penalty assessment and joint-energy comparison for
search coverage. The prime-only Rayleigh stop and generic-source scope
stop were reread narrowly; neither is overturned, and neither forbids
the distinct complete-energy audit. Zhu's computational positivity,
the generic core-form source and an RH-conditional spectral statement
are not essential inputs to this audit and were not newly retrieved.
No new theorem search or novelty inference is made. The missing URL
is repaired; SPECIALIZE is approved for the unchanged target. Its
mathematical correctness remains pending. Full matching Mathlib
coverage remains unchecked. No lemma or mathematical script was edited.
