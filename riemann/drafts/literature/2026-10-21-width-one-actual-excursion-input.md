# Uncovered actual-excursion input for the width-one signed test

TARGET: Assess whether unconditional actual Hardy-function results supply L450's short monotone interior excursion criterion (22) for the fixed width-one law.
CHECKED: 2026-10-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 297 searched actual Hardy large values, simultaneous derivative large values and short-interval resonance; inspected Soundararajan 0708.3990v2 Theorem 1 and section 2, Ivic (2019) Theorems 1--3 and their relevant proof cases, and Yang 2108.02301v1 Theorem 2(A) and its convolution proof setup; no matching joint excursion theorem was found in this bounded search.
SOURCE_EVIDENCE: Soundararajan arXiv:0708.3990v2 pp. 1--2, 4--5; Ivic, Banach Center Publications 118 (2019), pp. 9--11, 13--18, DOI 10.4064/bc118-1; Yang arXiv:2108.02301v1 pp. 2, 6--7, 13; primary statements and relevant proof cases are compared below, with exact local normalization from L366/L445.
COMPARISON: Inspected theorems give scalar extrema, separate derivative extrema or upper bounds conditional on Z monotonicity; none supplies the jointly required unsaturated two-jet crossing, first-coordinate proportion and duration in L450 (22).
GAP: Occurrence of an actual interval satisfying every hypothesis of L450 (22) remains unsupported; the search neither proves nonoccurrence nor licenses an actual PSD verdict.
REASON: Park application of this certificate; a scalar large-value theorem cannot be imported as the missing simultaneous interval theorem. Independently audit the already written conditional certificate using ready calculus and matrix coverage.
LITERATURE_REASON: Step 296 isolated a previously unread essential actual-data input: a quantitative simultaneous Hardy two-jet excursion, beyond the scalar upper bounds and calculus covered by the ready width-one assessment.
SCOPE: Only source comparison for L450 (22) on the unchanged width-one family, original cutoff, rare components, probabilities, w, m and both diagonals; no new law, amplitude enlargement or actual occurrence is approved here.

This is an uncovered continuation record, not a completed assessment or
an assertion that suitable known results exist. The exact target above
is the next turn's source-review task. Do not apply a large-value result
until its full hypotheses have been compared with all requirements.

The main gap remains global mixed positivity. The intermediate use is
deciding whether L450's signed-interval failure certificate can be
applied to the actual fixed family. Its complete conditional calculation
is canonical in L450 (19)--(22), not a new unconditional input.

At a fixed H, ell=log H, X0=(f,f'/L,f''/L^2), u=|X0|^2 and
L=log(2+t). Here f=F0/A_env is L445's exact real Hardy normalization;
its relationship to any source's Hardy Z convention must be checked,
including ordinary derivatives and gamma normalization. The required
interval J lies in [H+1,2H-1], has u monotone between U and 2U with
2U<ell^6/sqrt(2), and has x0^2>=c u throughout, for a fixed c>0.
Its duration must be at most c U^2/(4 C_T ell^(65/8)), with C_T the
uniform constant bounding 2Lw sqrt(AC) in L450. Either crossing
orientation is allowed. At duration K/ell the sufficient size is
U^2>=4 C_T K ell^(57/8)/c. This comparison does not prove occurrence.
An interval at arbitrarily large actual heights, embedded in an
admissible interior, would suffice to refute an eventual all-real-H
PSD claim; no positive-measure set of H has yet been obtained here.

Essential inputs: L449 (9)--(12), L450 (5)--(6), (19)--(22), L445's
exact normalization and L448's already covered scalar/Cauchy upper
bounds. L438/L443 keep the rest of the family fixed. Read only narrow
proof ranges needed to compare an identified primary theorem. Search
for actual unconditional large values with simultaneous derivative
control or a short monotone excursion; distinguish inspected statements
from leads. A result merely providing a large |f| or |X0|, an upper
bound for derivatives, a mean moment, or unconstrained unit phases is
insufficient without the remaining hypotheses. In particular, neither
monotonicity of u nor x0^2>=c u may be assumed at a large value of f.

A successful comparison must identify a precise applicable theorem
(or a strictly stated remaining specialization) and a discriminating
occurrence test. If the joint hypotheses are unsupported, record the
obstruction and park this certificate rather than repeat the scalar
upper-envelope calculation or derive uncovered mathematics during the
review. Preserve L448's narrow-width stop and the step-295 absolute
certificate stop; neither decides this new actual-data question.

Even an actual signed excess would stop only the fixed width-one
forced block. It would supply no actual clipping, capped nondegeneracy,
regulator margin, global realization or RH conclusion. A pass or lack
of an excess also leaves endpoint layers, other temporal/mean identities
and the main positivity gap unresolved. Mathlib matching coverage of
an actual-excursion theorem is unchecked.


## Completed bounded source comparison — step 297

LITERATURE / NOVELTY_UNCHECKED / literature_comparison; EXPLORATION.
No lemma, mathematical script or new excursion implication is derived.
EXPLORE records a bounded search without an adequate match, not novelty,
nonexistence of a theorem, or approval to assume its missing hypotheses.
The research target and all fixed-family hypotheses above are preserved.

### Primary statements actually inspected

[Soundararajan, *Extreme values of zeta and L-functions*,
arXiv:0708.3990v2, 4 April 2008](https://arxiv.org/pdf/0708.3990v2),
Theorem 1 p. 1: for sufficiently large T, some t in [T,2T] has
|zeta(1/2+it)| >= exp((1+o(1))sqrt(log T/log log T)).
Its further level-set lower bound is for 3<=V<=sqrt(log T/log log T)/5.
Read the resonance ratio on p. 2 and section 2, (2)--(4), pp. 4--5:
a smooth nonnegative weight supported in [1,2] and a resonator of
length N<=T^(1-epsilon) yield a scalar maximum via two moments.
These cases contain no simultaneous relative-jet or crossing-duration
conclusion. This is sufficient scalar magnitude information, but no
interval in the unsaturated band is selected by the theorem.

[Ivic, *On large values of Hardy's function Z(t) and its derivatives*,
BCP 118 (2019), 9--24, DOI 10.4064/bc118-1](https://www.impan.pl/shop/en/publication/transaction/download/product/113095),
Theorem 1 p. 11 gives both signed maxima >> (log T)^(1/4) on
[T,T+h], T^(17/110+epsilon)<=h<=T. Theorem 2 gives separate signed
Z^(k) extrema >> log^k T for fixed integer k>=1 on its stated
power-length ranges. Theorem 3 assumes a zero at T and monotonic Z
on [T,T+h], T^epsilon<=h<=T^(1/6); it concludes an upper bound.
Read sections 3--4, sign decomposition (3.1)--(3.5) and integration
by parts (4.6), pp. 13--17; these are scalar integral/max arguments.
Section 5, (5.1)--(5.2), p. 18 uses the assumed monotonicity to
bound an integral by a smoothed derivative integral. It does not
produce monotonicity, and monotonic Z is not monotonic u.
The subsequent interlacing discussion explicitly uses RH and is
ineligible here. No theorem above gives the required joint event.

[Yang, *Extreme values of derivatives of the Riemann zeta function*,
arXiv:2108.02301v1, 4 August 2021](https://arxiv.org/pdf/2108.02301v1),
Theorem 2(A), p. 2: for fixed integer j>=1, beta in [0,1), and
0<c<sqrt(2(1-beta)), the maximum of |zeta^(j)(1/2+it)| on
[T^beta,T] exceeds exp(c sqrt(log T log_3 T/log_2 T)) for sufficiently
large T. Read Lemma 3's strip-holomorphic convolution hypotheses,
pp. 6--7, and section 5's kernel and resonator integral (22), p. 13.
They concern one derivative order, not simultaneous ordinary Hardy
jets or their relative proportions. Theorem 1 concerns Re s=1 and
is not a critical-line statement. The inspected version is v1;
the published 2022 article's additional short-interval section was
not inspected and is not credited as coverage. PMC access returned
a browser challenge; the arXiv primary version was accessible.

### Normalization and missing joint hypotheses

L366 (1) and L445's positive envelope give exactly
F_0=-p Re Lambda(1/2+it), A_env=p|Gamma(1/4+it/2)|pi^(-1/4),
p=t^2+1/4. Against Ivic's convention Z=chi^(-1/2)zeta with the
usual continuous gamma phase, f=F_0/A_env=-Z. A consistent opposite
square-root sign only reverses this sign; the norms and squares in
this target are unchanged. Derivatives are ordinary real derivatives
of this quotient before division by L^j, as in L445, so there is no
remaining gamma envelope to absorb. Complex derivatives zeta^(j)
are not f^(j); differentiating the Hardy phase mixes lower orders.
This is a normalization comparison, not a new relative-jet estimate.

The local required scale sqrt(U)~ell^(57/32) at proposed duration
K/ell is already recorded in L450. Even scalar extrema above that
scale do not control f'/L and f''/L^2 relative to f throughout an
interval. None of the inspected conclusions supplies a fixed c>0
with x0^2>=cu along a monotone U-to-2U crossing, bounds its duration
by (22), and keeps 2U<ell^6/sqrt(2). Continuity alone cannot be
credited as any of those quantitative conclusions. We do not prove
a general impossibility of extracting them from stronger inputs.
No source is imported as an actual excursion theorem; no reproof
of known scalar theorems is needed. Full matching Mathlib coverage
remains unchecked, not absent.

Queries used: `Hardy Z function large values derivatives simultaneous
large values unconditional`; `resonance method zeta large values short
intervals derivatives Hardy Z function`; `"Hardy" "simultaneous"
"large values" derivatives`; and the exact Yang title plus arxiv.
The 2026 vertical-progression derivative paper and the 2023 derivative
zero-gap paper were search leads only; their theorems are unread and
are not evidence for the interval criterion. No failed search proves
novelty or nonexistence.

### Decision and independent continuation

Park actual use of (22). Reopen only with a precisely stated theorem
or separately assessed mechanism controlling all four interval
requirements, or a rigorous actual interval certificate. Repeating
scalar upper bounds, maxima or the signed identity is not a test.
This source review spends no mathematical exploration turn and does
not reset the two used since step 294. L448's narrow-width stop and
the absolute-envelope stop retain their original scopes.

The independent next target is a critical audit of the written
conditional test, under its explicit hypotheses, without an actual
occurrence claim. Its separate assessment is
`drafts/literature/2026-10-21-width-one-signed-test-critical-audit.md`.
That audit can validate or correct the reusable certificate; it will
not decide width-one PSD, the endpoint layers, actual/global
realization, clipping, capped nondegeneracy, L413's regulator margin
or global mixed positivity. No RH progress beyond local source
comparison or unverified complete candidate is claimed.
