# Finite Euler-phase floor — source coverage and reproduction scope

TARGET: Review source coverage for a ledger-free proof of ell=4*(Theta-arg E_prod)'>24.18 for primes p<=307 throughout L494's closed domain, retaining exact heat weights and the full Euler-phase loss.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the narrow October 30 phase/resultant and failure comparisons; inspected L494/L495 and the grouped-resultant assessment's phase qualifications. Exact web searches for 2609.37164 phase, 24.18022820120347, and Kornaus Euler phase, followed by arXiv-restricted searches, supplied no additional matching primary theorem; secondary search results were not used. Followed Planat reference [7] to Kornaus's Zenodo record; its PDF failed retrieval and remains unread.
SOURCE_EVIDENCE: Michel Planat, arXiv:2609.37164v2, 7 October 2026, https://arxiv.org/html/2609.37164v2 : Section 6.3 Lemma 6.3 and complete proof (PDF pp.18-19), Section 6.6 exact sigma/r_p/ell_hat definitions and reported 24.18022820120347 floor (p.22), Proposition 6.8 computational proof and monotonicity claims (pp.22-23), Section 6.7 exact phase normalization and nu' bounds (pp.26-27) inspected. These supply a scalar method independent of the signed ledger; the endpoint arithmetic and full local-band specialization have not been verified here.
COMPARISON: The source already claims the desired numerical floor and a slightly stronger scalar bound; this is known-source reproduction, with no novelty inference. Lemma 6.3 supplies only the base phase; Sections 6.6-6.7 separately retain the complete Euler loss. L495 assumes ell>0 and L494 supplies remainder bounds, so neither duplicates the proposed certificate. L491's high-tail gamma phase is a different quantity/domain.
GAP: Reproduce the scalar endpoint enclosure with justified uniformity on .16836<=t<=.1718 and x>=6000284561421.5, t*log(x/(4*pi))<=5.17; check every r_p<1, the exact nu' bound, and all endpoint/monotonicity hypotheses. The source's initial-band corner report alone is not a local certificate on that entire domain. No coefficient reserve, separator or collision exclusion follows.
REASON: Essential formulas, base theorem, heat weights and proof method are accessible in the inspected primary source. A small independent scalar calculation can test the printed floor without retrieving any coefficient producer. SPECIALIZE permits only this numerical/domain reproduction, not a new collision mechanism or an assumption of the reported decimal.
LITERATURE_REASON: Changed target from a conditional pointwise charge to a uniform numerical phase floor; the indispensable uniform scalar estimates and their source scope are not covered by the charge-only assessment.
SCOPE: Closed domain .16836<=t<=.1718, x>=6000284561421.5, t*log(x/(4*pi))<=5.17; all primes p<=307; exact L494 prefactor and L495 Euler weights. Covered work is a rigorous scalar enclosure with source-method uniformity checks. Excludes signed-coefficient ledgers, reserve, H1, collision exclusion, global endpoints and zero time.
COVERED_TARGET: Reproduce a ledger-free uniform certificate ell=4*(Theta-arg E_prod)'>24.18 and r_p<1 for every prime p<=307 on L494's closed domain, using Planat v2 Lemma 6.3 and the exact Section 6.6 phase-loss envelope.

## Completed source comparison — 2026-10-30

This is a literature-only step. No new phase estimate, monotonicity
proof, endpoint evaluation, lemma or mathematical script was produced.
The coverage decision changes from REVIEW_REQUIRED to SPECIALIZE;
the numerical inequality remains an unverified reproduction target.

The inspected primary source is [Planat v2](https://arxiv.org/html/2609.37164v2),
with page numbers checked against [its 54-page PDF](https://arxiv.org/pdf/2609.37164v2).
The load-bearing items and limitations are:

1. Section 6.3, Lemma 6.3, pp.18-19, assumes
   x>=6000284561419.5 and .16836<=t<=.2, in the exact Polymath
   prefactor normalization. Its conclusion is 4*Theta'>log(x/(4*pi)).
   The whole printed proof was inspected: it retains the heat correction,
   displays a,b,C,Q for alpha=a+ib and alpha'=C-iQ, and explicitly
   checks its final height condition. This cited theorem's domain contains
   the local one. It is a base-phase input only; its following paragraph
   expressly assigns the Euler phase to a separate numerical charge.
2. Section 6.6, p.22, defines, with the actual prime heat weights,

       sigma=.5+(t/4)*log(sqrt(x*x+1)/(4*pi))-t/(2*(x*x+1)),
       r_p=exp((t/4)*log(p)^2-sigma*log(p)),
       ell_hat=log(x/(4*pi))
                   -4*(.500000000001)*sum_(p<=307)log(p)*r_p/(1-r_p).

   It reports ell_hat>=24.18022820120347 at its new checkpoint.
   This is a source claim, not an interval computed or accepted locally.
   Proposition 6.8's computational proof, pp.22-23, describes outward
   logarithm/exponential seeds and increasing sigma and ell_hat with x
   and t, with the initial time band I=[.16836,.169425]. The proposed
   local continuation must check the scalar uniformity assertions through
   .1718; it may not inherit a grouped-ledger flag to establish them.
3. Section 6.7, pp.26-27, uses the same nu, Theta and Euler product as
   L495; it assumes every r_p<1 and states |nu'|<.500000000001 for the
   finite region. It explicitly identifies this as the justification of
   the Euler phase charge. L495's equation (10) records the exact phase
   identity. Its relation to ell_hat is therefore a source-method replay
   obligation, with the factor 4 and complete loss retained. It is not
   legitimate to substitute the base logarithm for ell.

The source-reported margin over 24.18 is small. A rigorous enclosure must
therefore retain exact heat weights and bound the full finite prime sum;
rounding the source decimal or checking sampled phases cannot certify it.
There is no need to compute any beta_m or squarefree coefficient ledger
for this target. The independently testable deliverables are a complete
prime set, positive denominators, a justified worst-corner or closed-box
reduction, and outward bounds compared with 24.18. Proving those belongs
to the separately routed mathematical turn. No claimed uniformity has
been newly derived in this review.

The source refers to a directed-certificate bundle but its producer was
not retrieved. That omission blocks claiming a replay of its output,
not the proposed standalone scalar reproduction. The related Kornaus
[Zenodo record 22658444](https://zenodo.org/records/22658444) lists the
v1.1 manuscript and a certificate archive. Two attempts to open its
manuscript PDF failed (Unicode-decoding error, then inaccessible URL).
It remains an unread lead; no theorem or phase constant is imported from
it. Planat Section 6.3 itself states that the inherited phase certificate
only covered t>=.172422, which does not supply the requested lower band.
No essential inaccessible Kornaus premise is needed for the finite scalar
test selected here. A later full collision argument would have additional
source obligations.

Narrow duplicate/failure checks used the charge assessment and working
record, the grouped-resultant scope, the gamma-phase source review, and
the charge-approval stop. These preserve the distinction between a
completed charge audit, an unverified phase floor, and an independent
strict reserve. The existing comparison below retains the energy,
inverse-gap and contraction stops. No stopped route is reopened.
The new review provides no actual-Xi structural input that would justify
a creative collision mechanism; the next proposed work is reproduction.
Full matching Mathlib coverage has not been checked and is unknown.

## Approved bounded reproduction and stopping test

The COVERED_TARGET above is the exact proposed mathematical action.
Use L494 for normalization/domain and L495 for the phase identity,
retaining the local-transcription audit qualification of L495. Import
Lemma 6.3 by its precise citation and check its applicability; do not
reprove it as a new result. Independently verify the scalar source claims
needed to obtain a uniform certificate, including the derivative cap.
Continue downstream only if all factors have r_p<1 and the complete
outward lower bound is strictly greater than 24.18 on the closed domain.
If the chosen enclosure fails, save actual/required bounds and the
responsible term/domain; an inconclusive enclosure does not refute the
phase inequality. Do not replace the target by ell>0. A failed replay
requires refined independently testable input or a different target,
not more source-approval cycling. Strict coefficient reserve, H1,
finite collisions, other times and zero time remain independent gaps.

## Original nomination — relevance and candidate comparison

The main gap is actual-Xi all-degree positivity. For the finite positive-time
collision route, L495's charges are usable only with a positive phase
denominator and an independent strict coefficient reserve. This target
addresses the former alone. The source's advertised numerical threshold
is 24.18; it is a target, not a premise being imported.

Reuse L495's exact phase identity, with
J=sum_p log(p)*A_p/(1-A_p), A_p=b_p*p^(-nu), and nu as there.
The nominated test is a rigorous enclosure of the entire Euler-phase
loss Im(nu'*J) against the exact base phase, uniformly on the closed
domain. Every r_p must stay below one. A later mathematical step may
use finite scalar enclosures within the reviewed scope above. No such
calculation was run in the nomination or in this source review.

Continue if a source-covered finite envelope can be tested against
24.18 without importing a ledger or assuming collision exclusion.
If coverage or the proposed numerical floor fails, retain the precise
deficit and reassess the downstream threshold; do not silently treat
ell>0 as the requested numerical result. A persistent inaccessible
producer is grounds to park that source-dependent task.

## Three candidate comparisons for recovery

1. A finite Euler-phase envelope tests an independent missing hypothesis
   of L495. It has explicit inputs and a scalar threshold, requires no
   cancellation of unknown phases, and was selected for source review.
2. Unmollified chirality transversality is the distinct criterion in
   Planat Section 6.4 Lemma 6.4, already inspected as a lead in the
   collective-contraction assessment. On this finite band it still
   requires a uniform nonzero chirality amplitude and a phase-speed
   floor. Those inputs are not supplied by the present audit, so this
   is not a ready mathematical continuation.
3. Backward negative-Laguerre-energy control would address collisions
   more directly, but the L487 quartic obstruction in
   ATTEMPTS/2026-10-30-bounded-backward-laguerre-energy-comparison.md
   excludes its generic bounded-coefficient form. No new actual-Xi
   structural inequality has been specified that evades that example.

The inverse-gap and collective-landing stops are also preserved; no
stopped mechanism is reopened. This selection does not claim a creative
advance. No independently testable new actual-Xi collision mechanism
emerged from this comparison; the available phase prerequisite is a
known-source specialization whose exact coverage is now recorded above. Full
matching Mathlib coverage is unknown. Newly written L495 records the
completed source-claim audit; it has not received a later independent
audit of its transcription.
