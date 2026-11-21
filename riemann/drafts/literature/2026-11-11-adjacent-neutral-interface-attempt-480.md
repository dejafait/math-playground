# Fixed neutral adjacent-cell interface test

TARGET: Test beta_1<1/2 for the fixed adjacent neutral cells by testing exact-moment cancellation of slow exponential interface responses against logarithmic single-cell energy, retaining the prime delay.
CHECKED: 2026-11-11
DECISION: EXPLORE
SEARCH_EVIDENCE: The completed step480 review in drafts/literature/2026-11-11-adjacent-neutral-cell-energy-contraction-479.md searched the exact adjacent-cell, neutral relative-form, angle and strengthened-Cauchy-Schwarz statements and compared recorded failures. No matching strict half bound was located; no originality inference.
SOURCE_EVIDENCE: Zhu v2 Cor6.3 https://arxiv.org/html/2608.24827v2 ; Suzuki v3 Thm1.1/Section2.4 https://arxiv.org/html/2606.09096v3 ; Li paper45 displayed v2 Lemma3.1 https://rstation.ai/problems/riemann_hypothesis/papers/45 ; Perfekt-Pushnitski Lemma2.1 p166 https://archive.intlpress.com/site/pub/files/_fulltext/journals/arkiv/2018/0056/0001/ARKIV-2018-0056-0001-a010.pdf ; DLMF5.7.6 https://dlmf.nist.gov/5.7.E6 . Direct sources reopened in step481; full prior proof-case review and limits remain in the step480 comparison. Local normalization: L741(6)/(21)-(24), L744(6).
COMPARISON: The sources cover positive single-cell energies, the complete interface kernel and exponential-response/Carleman tools; they do not establish a strict1/2 relative norm after neutral compression. L743's prime-only L2 supremum and L742/L749/L750/L752/C744g stops have different quantifiers, windows or metrics. Further source review is needed only if the proposed attempt leaves this scope.
GAP: Determine whether neutral response cancellation plus logarithmic coercivity yields the fixed uniform beta_1<1/2 inequality, or certify an exactly neutral smooth pair with ratio>=1/2. The essential new comparison is unproved; generic block positivity yields only the existing constant1.
REASON: Step481 separately approves bounded exploration after repairing the missing direct source URLs and reusing the completed step480 source comparison. No mathematical bound is approved or derived; the target and hypotheses are unchanged.
LITERATURE_REASON: Supervisor recovery requires direct source URLs in this ready continuation assessment; repair traceability and confirm primary statements without repeating discovery or extending scope.
SCOPE: Exactly ell=log(3)/2, touching cells (0,ell) and (ell,2ell), arbitrary complex cell-interior smooth tests with both exponential moments exactly zero, and the full unshifted energy. No varying separation/threshold, H2 cap, prime-only metric, shifted denominator, remote summability or global positivity.

## Exact objects and inputs

Use L743(2)'s complex class N: f in C_c^infinity(0,ell;C) with
integrals e^(s/2)f(s) and e^(-s/2)f(s) both zero. Let
(tau g)(x)=g(x-ell), with zero extension. E_ell is the complete
single-cell form and H_(2ell) its complete Hermitian polarization,
linear in the first argument. The quantity under test is exactly

    beta_1 = sup_(nonzero f,g in N)
        |H_(2ell)(f,tau g)|/sqrt(E_ell(f)E_ell(g)).

Essential mathematical input IDs are L740, L741, L743 and L744.
L741(6) already gives E_ell(f)>=8.9e-18||f||_2^2 and the weaker
bound beta_1<=1. Its (21)-(24) specify the complete interface,
including the continuous kernel and arithmetic delay. L744(6) is
the smooth full-form identity. Cite these existing results; do not
reprove their source positivity certificate as new mathematics.
The external computation underlying L741's sign remains an imported
theorem, not a locally replayed certificate.

The primary smooth Green/digamma identities and Carleman lemma are
supporting tools with the exact hypotheses recorded in the completed
review. No new response cancellation, energy coercivity improvement
or bounded relative operator has yet been established. Any such step
belongs to the later mathematical attempt, with a full proof in a
canonical lemma if successful. Existing generic block contraction
is not itself a new mechanism or proof of the strict half constant.

## One bounded attempt

Investigate exact-moment compression of the slow separable exponential
responses at the touching interface, jointly with the logarithmic
single-cell energy denominator. The prospective gain is selective
cancellation before taking a norm, rather than a smaller pointwise
prime-comb mass. Derive and justify any kernel representation,
polarization, response summation and moment cancellation used. Keep
all completion and arithmetic terms until an exact cancellation or
support argument is proved. A useful uniform upper bound must cover
the whole complex smooth N, including functions approaching the
interface and unrestricted high-frequency content.

Use one fixed decision test: prove beta_1<=b<1/2 with a rigorous
uniform b, or give nonzero f,g in N with certified ratio>=1/2.
A finite numerical search can locate a lower witness, not establish
the uniform upper bound. A numerical witness needs complete enclosures,
exact moments and a justified smooth representative; approximate
neutrality or a nonsmooth finite-dimensional vector alone does not
suffice. C744h covers its own finite five-cell class and is not an
automatic transfer theorem for a new trial family here.

If neither conclusion is reached, preserve the attempted estimate
and precise unpaid constant/tail as an inconclusive attempt. Do not
retune the half threshold, add a collar or change the separation.
A rigorous ratio>=1/2 parks this target; repetition after an
inconclusive attempt needs a materially new comparison or informative
obstruction under the shared bounded-exploration rules.

Plausible downstream use is a paid nearest-neighbor interaction in
a neutral spatial-cell argument. Distant couplings, non-neutral
moment directions, their mixed terms, odd signs and all-window
propagation remain independent gaps. No RH, global positive spectral
measure, positive-shift substitution or cross-notebook theorem is
assumed. Full matching Mathlib coverage is unchecked.

This is nominated as proof_attempt/creative: the precise obstruction
is the unpaid strict relative energy of the singular complete
interface. The new test concerns whether response-selective neutral
cancellation and logarithmic coercivity give a genuine margin below
1/2. The identities and bounds supplied by the sources are tools,
not the claimed mechanism's conclusion. No new mathematics is derived
or approved for execution in its creation turn.

## Separate source-gate repair and approval, step481

This literature-only recovery changes traceability, not the mathematical
decision. All five direct URLs in SOURCE_EVIDENCE were accessible on
11 November 2026. Reused the completed step480 comparison, including its
exact-query record, duplicate/failure comparison and proof-case review;
no new search for an unchanged target was needed.

Reconfirmed Zhu Corollary6.3: complex L2 tests in [-0.8,0.8] have
Q(f)>=8.9e-18||f||_2^2. Retain the prior smooth-test specialization and
L741 normalization; no supplementary certificate was replayed. Suzuki
Theorem1.1 identifies the Friedrichs extension for every a>0; it does
not supply the required relative constant. Li's displayed v2 Lemma3.1
is on smooth compact parity tests and retains the parity-signed pole.
Its response identity is supporting coverage, not cancellation on the
complex neutral class. Reused the previously inspected finite-sum,
monotone-convergence and interior-support convergence cases of its proof.
Perfekt--Pushnitski Lemma2.1 and its short proof give the A*pi L2
Hankel bound under |h(t)|<=A/t on t>0; no relative-energy bound follows
from the citation alone. DLMF5.7.6 remains scalar digamma coverage,
with the excluded nonpositive-integer poles as recorded previously.

The unchanged EXPLORE assessment is now approved for the exact TARGET
on a later research turn. This is an honest STALLED process repair:
no new mathematical input, informative obstruction, bound or witness.
Known constant1 remains the available local bound; strict1/2 is unpaid.
Preserve every prior stop, the exact prime delay, exact moments and the
unshifted denominator. The essential inputs and independent global gaps
remain as stated above. Matching Mathlib coverage remains unchecked.
