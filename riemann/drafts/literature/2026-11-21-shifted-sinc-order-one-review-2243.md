# Shifted infinite sinc product: nomination2243, reviewed2244

TARGET: Assess source coverage for G(z)=(2+cos z)/3 times product_{j>=1}sinc(z/(j+sqrt(2))) as an order-one all-real-prefix positive-inverse countermodel, including simple real zeros, all derivative tails and a prefix-uniform second-moment bound.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed2244: local duplicate/failure comparison and bounded external searches for infinite sinc/random harmonic products, zero division, concentration and analytic product tools; queries and inspected passages are in drafts/literature/2026-11-21-shifted-sinc-source-notes-2244.md. No exact shifted-prefix match found and no novelty inference.
SOURCE_EVIDENCE: Durrett PTE version5 (11January2019), Theorems2.5.6 pp84-85 and3.3.14 p130 with proofs; Schmuland2003 sections2,4-5 manuscript pp2,4-7; Hoeffding UNC Mimeo326 (May1962) Theorem2 p6 and proof pp12-13 (3.11)-(3.17); DLMF1.10(ix) M-test and no-extra-zeros conclusion; Eremenko2015 p2 order definition; unchanged finite identities and stronger-criterion comparison2239 reused. Precise links/qualifications are in source notes2244.
COMPARISON: Schmuland supplies substantial infinite-uniform smoothing overlap with different widths, without zero-prefix removal or the full requested tails/growth assertion. C919p supplies the finite-factor identity but its Gaussian tail proof does not transfer. Classical sources cover ordinary tools, not the simultaneous fixed-model conclusion; no checked theorem decides the exact target.
GAP: Later specialization must verify local entire convergence, exhaustive simple real roots and ordered prefix grouping, infinite probability representation, global strictness, every exponential derivative tail, an explicit prefix-uniform moment bound, retained nonreal zero and exact order one. None is proved in this review; order does not assert finite type.
REASON: Essential ordinary-tool coverage is accessible, so a later source-covered REPRODUCTION attempt is justified. Import the named results and prove only their applicability and the model-specific assembly. No countermodel or RH bridge is established in this literature turn.
LITERATURE_REASON: Changed hypothesis and construction: replace finite compact shifts of a Gaussian by a proposed infinite convolution with shrinking widths, require exact order one and retain global strict positivity. Finite-transform coverage does not authorize these limiting assertions.
SCOPE: Only the fixed G and all its finite increasing real-zero prefixes below; no changed widths, weakened positivity or Xi transfer. Review2244 prepares a later specialization; its new continuation receives separate approval next turn.

## Completed review2244

Full citations, theorem hypotheses, proof cases, overlap and remaining
specialization obligations are in
[source notes2244](2026-11-21-shifted-sinc-source-notes-2244.md).
The exact mathematical continuation is in
[assessment2244](2026-11-21-shifted-sinc-model-specialization-2244.md).
The outcome is EXPLORATION: source coverage is completed, while every
proposed mathematical conclusion remains open. No new lemma or
mathematical script was written. PROOF.md and DAG.md are unchanged.

## Preserved nomination2243

The following records the original proposal and then-uninspected
leads. The completed source comparison above supersedes its missing
coverage statements; the proposed mathematical properties are still
unproved.

## Proposed test, not a result

Write sinc(w)=sin(w)/w with value1 at0. The single proposed model is

    G(z)=(2+cos z)/3 * product_(j>=1) sinc(z/(j+sqrt(2))).

Let r_l be the increasing enumeration of the candidate positive-real-zero
set {pi*k*(j+sqrt(2)):j,k>=1}. Exhaustiveness, simplicity and entire
convergence are obligations, not assumed theorems. For N>=0 define
R_N(z)=product_(l=1)^N(1-z^2/r_l^2). Seek for every finite N of this
fixed G, without changing the function with N:

- Entire removability of G/R_N and a smooth even probability inverse
  strictly positive at every real u in the angular Fourier convention.
- For all integers m,p>=0 and real B>=0, derivative integrability with
  weight (1+|u|)^p exp(B|u|), and exp(B|u|)f_N^(m)(u)->0 at both ends.
- An explicit finite second-moment bound independent of N.
- A retained nonreal zero z_*=pi+i log(2+sqrt(3)) and exact order one
  for each finite quotient, established with both growth bounds.

The proposed tool is a series of independent centered uniform variables
with widths1/(j+sqrt(2)), together with C919p's finite atomic factor.
No convergence, support, density, tail, moment, zero or growth conclusion
for this series is established here. Within-factor removals might use
C919p's compact cosine-power identity; the ordered global prefixes and
infinite residual are new obligations. A changing finite approximation
cannot replace the single fixed entire function.

Continue only after essential sources cover the ordinary tools and no
inspected theorem already decides the exact target. Import a matching
theorem instead of reproducing it. Abandon this fixed candidate if a
necessary property is contradicted; a failed estimate alone is inconclusive.
Success could delimit an order-one generic bridge, not settle actual-Xi
mixed positivity. No mathematical derivation is authorized by this file.

## Three mechanisms compared for recovery

1. A further finite actual-Xi removal leaves the arbitrary-prefix and
   sufficiency gaps and adds root/backend premises. The two-real-zero
   approval-loop stop2238 already explains why another approval or
   finite sign does not supply that bridge. No new actual-theta signed
   mechanism is supplied by the completed audit.
2. Compact smoothing in place of the Gaussian could test order one,
   but would leave global strict positivity unmatched. The September23
   compact-spline stop records multiplicity and localization defects for
   its finite-level model; it is not a global ban on compact kernels.
3. Select the shifted infinite-convolution candidate above to test
   order one while attempting to retain global strictness and every
   prefix. It needs new limiting tools and is outside the ready audit.

Narrowly inspected stops: September23 compact-spline masking and nonreal
deflation; finite-block-only extension1117; finite-divisor signed
composition667; two-real-zero approval loop2238. Their named lemmas
were not loaded or imported into this candidate. C919p's growth-class
stop2241 remains intact. No cross-notebook input is used.

Review891 quotes Kwasnicki1710.11023v3 section6.1 p20 on infinite
convolutions of exponential laws and finite-head smoothing. Only that
local source-note range was read; its primary theorem is an unread
applicability lead, and its one-sided/exponential laws are not the
proposed uniforms. Review373's cutoff searches and the other sinc hits
do not supply the needed theorem. Beta-Bessel review782 concerns another
order-one moment-law countermodel, not all real-zero prefixes.

Next compare exact primary hypotheses for random-series convergence,
infinite characteristic products, strict support and smooth-density
criteria, derivative tails, canonical-product order and any existing
zero-removal sufficiency theorem. Read relevant proof cases. No broad
sweep or optional blocked-source retrieval is justified. Full matching
Mathlib coverage remains unchecked. The later proof classification must
follow the source comparison; this nomination is not labelled creative
to satisfy routing frequency and is not an RH candidate.
