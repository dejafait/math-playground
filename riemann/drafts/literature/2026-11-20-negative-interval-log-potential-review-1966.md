# Fixed negative-interval log potential: nomination1966, review1967

TARGET: Assess source coverage for L1 convergence of d^(-1) log|P_d(x)/x^d| to zero on [-2,-1] for the actual reciprocal Jensen family, retaining all root multiplicities.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1967 searched exact Jensen/Appell logarithmic asymptotics, real-interval L1/small values and stronger potential convergence; compared C028d/f, C029f and named local source/failure records. Queries and read ranges: drafts/literature/2026-11-20-negative-interval-source-notes-1967.md. No matching theorem or novelty conclusion.
SOURCE_EVIDENCE: Reuse C028f/audit1518 and Ru TheoremA1.1.1/CorollaryA1.1.3 pp1-2, https://www.math.uh.edu/~minru/log.pdf ; Boyer--Goh arXiv:0809.1266v1 Definition1/Section3 Theorem1/proof/Corollary1, https://arxiv.org/html/0809.1266v1 ; Bogvad--Hagg--Shapiro Section4.4 Lemma4.12/complete proof (4.16)-(4.18), https://doi.org/10.1007/s00365-023-09657-x ; reuse Fradelizi coverage1966. Exact qualifications are in source-notes1967.
COMPARISON: Inspected Appell and planar-potential conclusions do not directly imply this real-interval limit; median small-value bounds do not identify its scale. Existing uniform growth/count/tail and Jensen logarithmic root sums support a finite-factor real-interval specialization, whose singular and large-root bounds remain to be proved.
GAP: Prove the exact reciprocal normalization, whole-neighborhood absolute-log control for all multiplicities and a uniform logarithmic moment for large reciprocal roots, then show the proposed integral tends to zero. No interval convergence or rate is established by this review.
REASON: Essential source comparison is complete for one bounded classical specialization of the unchanged local target. It can support a later reflection comparison but pays no full complement or signed remainder; no creative central mechanism is ready.
SCOPE: Subsequent specialization only; actual b_j>0,b_0=1,P_d(x)=sum_(j=0)^d binom(d,j)b_j*x^(d-j),d>=3, actual F of order1/2 and C028f's fixed K. Interval [-2,-1], Lebesgue L1, all multiplicities. No RH, real-root, simple-root, finite-type or zero-free-interval assumption.
COVERED_TARGET: Establish or refute integral_[-2,-1] |d^(-1) log|P_d(x)/x^d|| dx -> 0 for the actual reciprocal Jensen family, counting every root multiplicity, using C028f and finite-factor logarithmic estimates.

## Original nomination1966

The displayed limit is a proposed target, not a consequence of1966.
Null-set values at zeros are harmless; neighborhoods may not be discarded.
Compare known logarithmic-potential and reciprocal/Appell asymptotics,
including uniform small-value control and the actual asymptotic scale.
Reuse Fradelizi coverage; do not retry the Carbery--Wright access blocker.

Continue only with a domain-valid bounded test of this exact limit or
an informative obstruction accounting for all singular contributions;
otherwise park it at the first missing hypothesis. No degree/exponent
sweep. Possible downstream use is to compare one fixed negative-real
region with C029f's positive-real region before investigating reflection.
The full complement, paired error, upper payment, H_d=o(d) and actual-Xi
positivity remain unresolved. This nomination reopens none of those
claims. No creative proof is ready without an actual signed-complement
mechanism. Full matching Mathlib coverage remains unknown.

## Completed source review1967

The separate source review is complete; its exact theorem hypotheses,
read proof cases, local comparisons and remaining specialization checks
are in [source-notes1967](2026-11-20-negative-interval-source-notes-1967.md).
SPECIALIZE approves an ordinary method, not a new limit theorem. Reuse
C028f's audited family bounds and its inspected Jensen source. A future
proof must control the entire real-interval logarithmic singularity,
and large-root logarithmic weights, rather than infer a trace limit from
planar L1 convergence or use a degree-dependent median as the asymptotic
scale. Finite-factor one-dimensional integration is the necessary
specialization; no general source theorem needs reproving.

Continue only with an actual-family proof or obstruction for the exact
COVERED_TARGET. Account for all root neighborhoods and limit orders;
otherwise park at the first unpaid bound. No full-window conclusion is
approved. New ready coverage receives separate supervisor approval next
turn without rejecting the completed literature comparison.
