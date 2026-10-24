# Coverage: conditional lower-band sign assembly

TARGET: Combine audited L457 and L458 to prove uniform eventual positivity of D_{m/2}(Ξ;a) on 7/8≤m/r≤31/32, retaining the pinned external premise and exact positive normalization.
CHECKED: 2026-10-24
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed lower-band moving-saddle and whole-plane-theta searches and their audit assessments; compared L457/L458 hypotheses, conclusions and final audit passages, C455a and its assembly assessment, the October overlap/input register, and L323/L327/L456 failures. No fresh external search or exhaustive duplicate claim.
SOURCE_EVIDENCE: Reused inspected DLMF 2.4.10–2.4.16 and Temme arXiv:1308.1547v1 Sections 2.2–2.3 and 4.1; Csordas arXiv:1309.0055v2 Lemma 3.6 and Theorem 3.7 (3.10)–(3.14), DLMF 2.3.21–2.3.23 and 7.2.6–7.2.9; Titchmarsh–Heath-Brown (1986), Theorem 14.2 and Section 14.3, pp. 336–339, through the saved Littlewood assessment and audited L457 inputs; pinned September 30 Theorem 1.1 through the register. No primary page freshly fetched or external proof newly verified.
COMPARISON: Audited L457 and L458 have identical positive-real-r, positive-even-m closed-band domains, coupled h,a and full finite S including cutoff equality. L457 supplies a positive moving-saddle scale and uniform arithmetic margin; L458 supplies a complete real additive error and exact positive multiplier. Existing sources and audits cover their mechanisms; only the downstream quantitative application remains.
GAP: Prove the combined sign by comparing the complete additive error with L457's uniform lower margin, using one common onset and unchanged factorial/reflection multiplier; optionally retain its moving-saddle relative normalization. No combined inequality or sign is established in this literature turn.
REASON: The separate exact-scope comparison finds no missing essential source or changed input hypothesis. One REPRODUCTION assembly attempt is covered, without repeating the saddle/sector proofs or substituting the narrower C455a theorem.
SCOPE: The exact conditional L457/L458 application at positive real r tending to infinity, positive even m with 7/8≤m/r≤31/32, h=9/2+m/(2r), a=sqrt(4π²exp(4r)−h²)>0 and the unchanged finite signed sum, including zero at log(jk)=2r. No every-height transfer or smaller-index completion.
LITERATURE_REASON: The saved sign-assembly action lay outside the preceding audit-only assessments and required this separate exact-scope comparison; it is now complete using existing source evidence, without repeated discovery or source retrieval.

## Initial continuation record, preserved

The following nomination records the uncovered state at invocation start.
The completed comparison below discharges its literature requirement;
the new SPECIALIZE decision receives separate supervisor approval next
turn before mathematical work. This record approves coverage only.

Essential input IDs are L457 and L458. Reuse their canonical proofs
and audits, the lower-band moving-saddle coverage and audit coverage,
and the lower-band theta coverage and audit coverage. The older
subendpoint assembly assessment concerns a different band and may
serve as a comparison template, not as approval of this action.
The exact TARGET above is also the sole Next action in PROGRESS.md;
the next invocation is literature-only until this assessment is ready.

L457 states S/M_*=1+O((log r)^3/sqrt(r)), with M_*>0 and
|log M_*|<=C r^(2/3), on this entire closed band. Its conclusion
also states the eventual lower bound S>=exp(-C r^(2/3)). L458
states D_{m/2}=P_{r,m}(S+epsilon), with P_{r,m}>0 and
|epsilon|<=C(1+r)^2 exp(-r/200). These are the input statements,
not an application or comparison derived by this audit turn.

L457 retains L452/L456 and the zeta specialization of OpenAI,
*The Quasi-Riemann Hypothesis: A Zero-Free Half-Plane Re s > 7/8*,
September 30, 2026, Theorem 1.1 at commit
`1581d4cbdd69a0faf34b2089614fe2a814316a6a`. The pole at one
is allowed, nonvanishing is strict to the right of 7/8, and the
external manuscript/import closure has not been independently audited
locally. L458 needs no external zero-free premise and uses L269,
C294b and L455's explicit methods. None of those qualifications may
be removed in an assembly.

The next comparison should check exact agreement of real-r/even-m
domains, h,a and the complete finite S, the scope of the two audits,
the required single onset and exact factorial/reflection multiplier.
Reuse the recorded L323 larger-strip and L327 unsigned/PSD failures;
the proposed application neither changes their conclusions nor treats
them as global bans. Approve only if the existing source coverage
suffices for that precise quantitative comparison. Otherwise identify
the missing source or hypothesis and keep dependent work uncovered.

The main gap is still initial low-index signs and global mixed
positivity. A conditional coupled sign band could be a useful partial
input, but every-height transfer, all remaining small indices, bounded
heights and the selected-law/regulator gaps stay unresolved. No RH
candidate, new sign or originality claim is made. Full matching
Mathlib coverage remains unchecked.

## Completed separate comparison — 2026-10-24

This is a LITERATURE / NOVELTY_UNCHECKED / EXPLORATION step on the
unchanged TARGET. It supplies new exact-scope coverage using existing
source evidence, not a mathematical input or progress beyond the checked
sources. No lemma, mathematical script, DAG or main argument is changed.
Mathematical exploration usage stays 0 of 3; literature neither spends
nor resets that budget. The subsequent covered task is REPRODUCTION.

### Source evidence reused and its limits

The [moving-saddle assessment](2026-10-23-lower-band-moving-saddle-coverage.md)
and [audit coverage](2026-10-23-lower-band-moving-saddle-critical-audit-coverage.md)
record the inspected hypotheses and essential proof cases of
[DLMF 2.4(iii)–(iv), 2.4.10–2.4.16](https://dlmf.nist.gov/2.4#iii)
and [Temme, *Uniform Asymptotic Methods for Integrals*,
arXiv:1308.1547v1 (2013)](https://arxiv.org/html/1308.1547v1),
Sections 2.2–2.3, (2.9)–(2.13), and 4.1, (4.1)–(4.5).
Analytic phase/amplitude neighborhoods, convergence and endpoint gaps,
the two half-paths, direction-selected Gaussian root and separate pole
treatment are required. Neither source states uniformity for this
changing paired-zeta exponent. L457's explicit estimates and completed
audit provide that local input. No general saddle theorem is reproved.

The [theta assessment](2026-10-23-lower-band-whole-plane-theta-coverage.md)
and [audit coverage](2026-10-24-lower-band-theta-critical-audit-coverage.md)
record inspection of Csordas, *Fourier transforms of positive definite
kernels and the Riemann ξ-Function*,
[arXiv:1309.0055v2 (21 February 2014)](https://arxiv.org/html/1309.0055v2),
Theorem 3.5, Lemma 3.6 and Theorem 3.7, (3.7)–(3.14), including the
two admissibility cases and double-integral coefficient identity.
Admissibility and strict logarithmic concavity do not imply positive
definiteness of all associated kernels; that remains a premise in the
real-zero criterion. [DLMF 2.3(iv), 2.3.21–2.3.23](https://dlmf.nist.gov/2.3#iv)
requires smooth phase/amplitude, phase derivative nonzero off the
stationary endpoint, differentiable endpoint expansions and controlled
endpoint limits or uniform convergence; both finite endpoints contribute.
[DLMF 7.2(iii), 7.2.6–7.2.9](https://dlmf.nist.gov/7.2#iii) gives
scalar Fresnel definitions and limits. These are mechanism inputs,
not a signed moving-domain error theorem. L458 supplies the audited
complete reduction and normalization needed here.

Reuse the [Littlewood comparison](2026-10-21-fixed-half-plane-endpoint-derivative-review.md):
Titchmarsh–Heath-Brown, *The Theory of the Riemann Zeta-function*,
second edition (1986), Theorem 14.2, (14.2.1)–(14.2.6), and
Section 14.3, pp. 336–339. Its printed RH assumption is not removed
by citation. L457's audited inherited fixed-disk logarithm construction
is the local specialization under the pinned premise. Inversion,
unit-pole and Stirling sources remain those recorded in its assessments.
The [external-input register](../../foundations/2026-10-quasi-riemann-input.md)
preserves the exact September 30 Theorem 1.1 citation, strict boundary,
allowed pole and unaudited manuscript/import closure. This review
performs no external verification and imports no Euler reciprocal
expansion below one. Liu's stronger boundary is unnecessary here.

The prior queries and source versions are reused without another
discovery search. Flajolet–Sedgewick, Olver/Lyness and the earlier
general stationary-phase leads remain unread and nonessential.
No essential source blocker was found for this application.

### Exact interface and duplicate comparison

Read L457 Hypotheses, Conclusion, Section 1 and its assembly and
separate critical-audit passages, and L458 Hypotheses, Conclusion,
Section 1 and its final normalization/onset audit passages. Their
independent correctness audits are reused, not repeated in this review.
Both use all sufficiently large positive real r, positive even m and
the same closed interval 7/8≤m/r≤31/32. Both use
h=9/2+m/(2r), the positive square root defining a and the identical
positive-part weight of exponent m. In particular both assign zero
at log(jk)=2r, not a half-weight or a different truncated sum.

L457 already states S/M*=1+O((log r)^3/sqrt(r)), M*>0,
|log M*|≤C r^(2/3), and S≥exp(−C r^(2/3)), uniformly.
L458 already states D_{m/2}=P(S+ε), with real ε bounded by
C(1+r)^2 exp(−r/200) and
P=[2^(m−1)/m!]C₀exp(Φ_*)π/a>0. These are input statements,
not combined conclusions. Each has fixed constants and a common
onset over its own full band; no domain extension is required to
apply them at the same pair.

C455a and its [assembly coverage](2026-10-23-subendpoint-laguerre-assembly-coverage.md)
were compared as a known application template. They cover
31/32≤m/r≤63/64 and normalize by a fixed-center zeta square.
They do not already state the present whole-band sign or justify
S/B→1 here. C452a's m=r sequence, L453's rounded endpoint and
L326's m/r=3/4 sequence also have different scopes. L457 alone
is arithmetic; L458 alone is an unsigned reduction. The prior searches
found no matching external assembly theorem; this is no novelty claim.

Read L323 and L327 hypotheses/conclusions and their boundary-strip
and balanced-AFE failure records, and the L456 fixed-circle failure.
The r/4 summed-modulus failure is preserved: L458 uses its audited
smaller-strip proof. The PSD replacement failure is preserved: this
application keeps the actual signed phase sum. Fixed-center freezing
is not retried: use L457's moving-saddle margin, without assuming
relative closeness to the old square. Fixed-r/unit-phase failures do
not contradict a result at the coupled a(r,m). None is a global ban.

### Bounded continuation and decision test

The single next mathematical attempt must apply L457 and L458 at
identical admissible parameters, retain their different constants and
onsets, and compare the full additive error with the stated positive
arithmetic margin. Choose one onset for all required inequalities.
If giving a relative result, use M*, not an unproved fixed-center
square comparison. Keep P exactly; no extra reflection, factorial
cancellation or positivity theorem is needed. A canonical result must
include its full elementary assembly, all hypotheses and Mathlib limits.

Continue if the complete comparison yields a strictly positive margin
uniformly on the entire closed band with one onset. Record a precise
defect and repair or abandon this application if domain agreement,
uniformity or the complete error comparison fails. This review proves
none of those combined inequalities. Essential continuation inputs are
L457 and L458; L457 retains L452/L456 and the pinned external premise.
Every-height transfer, smaller indices, bounded exterior heights,
global mixed positivity and selected-law/regulator gaps remain outside
scope. No RH candidate or new sign is claimed. Full matching Mathlib
coverage is unchecked, not asserted absent.
