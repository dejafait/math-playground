# Unshifted Jensen edge: completed source comparison1345

TARGET: Assess whether a uniform coalescing-saddle theorem applies to Ono2610.38870v1's actual unshifted Jensen Cauchy integral at q=q_e+x*d^(-2/3), 1<=x<=4, with an explicit real Airy reference and normalized remainder o(1), checking the entire contour before nominating a sign test.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Exact unshifted/Jensen/Airy/coalescing and Ono2610.38870 searches located no inspected stronger signed edge theorem. Reused the named Laguerre and unshifted-bulk assessments. Primary sources and queries are recorded below; no novelty inference.
SOURCE_EVIDENCE: Ono arXiv2610.38870v1, (2.5)-(3.3), Lemmas7-9/12-13 and relevant full proofs, Proposition15/Corollary16, pp5-14 https://arxiv.org/pdf/2610.38870v1 ; Chester-Friedman-Ursell1957, Theorems1-2/Sections2-5 including bounded scaled-parameter and negative-real cases, pp601-609 https://doi.org/10.1017/S0305004100032655 ; Olde Daalhuis-Temme1994, Sections3/5 and Appendix hypotheses https://ir.cwi.nl/pub/1473/1473D.pdf .
COMPARISON: CFU gives a local uniform cubic map and an Airy expansion conditional on negligible exterior contribution. Ono's published Gaussian formula has a restricted interval. Neither is an already paid full actual-integral signed edge comparison. The 1994 unbounded-parameter theorem does not remove contour and amplitude hypotheses.
GAP: Actual cubic nondegeneracy, real branch/orientation and reference coefficient, uniform normalized complex amplitude bounds, contour connectors and exterior payment remain mathematical obligations. No explicit real Airy reference or nonzero barrier margin has been established.
REASON: The new primary hypothesis comparison stops automatic edge-sign import. Park the full signed-window target pending actual payment. A separate fixed-angle exterior test is concrete and source-covered; it does not require solving or assuming the local Airy problem.
LITERATURE_REASON: Essential unread generic coalescing-saddle hypotheses and stronger unshifted edge coverage were required by nomination1344. Those sources were inspected once; access is sufficient for the present verdict and the narrower continuation.
SCOPE: Literature-only source applicability comparison, K=Q, n=0, d tending to infinity, x in [1,4]. No new asymptotic, specialization, sign test, lemma or mathematical script was derived. Mathlib full matching coverage unchecked.

## Primary theorem comparison

**CFU.** C. Chester, B. Friedman and F. Ursell, *An extension of the
method of steepest descents*, Proc.Cambridge Philos.Soc.53(1957),599-611,
[primary PDF](https://last.hit.bme.hu/download/firtha/spa/S0305004100032655.pdf).
Read Theorem1's regular-branch proof and Theorem2's remainder argument,
Sections2-5, pp601-609. The local analytic phase has a double stationary
point with nonzero cubic coefficient and a simple parameter unfolding.
Theorem1 supplies a locally invertible cubic change; the critical values
fix its parameters. Section5 p607 separately assumes negligible outside
contribution. Theorem2 uses bounded analytic transformed amplitudes on a
fixed neighborhood and admissible finite contour pieces. Its proof
handles bounded scaled parameter and treats negative-real Airy zeros
with both Ai and Ai-prime; no relative division by Ai at a zero is valid.
Contour choice determines which Airy solution occurs. These hypotheses
are not a full-contour estimate for an arbitrary integrand. Direct URL
requests returned404, but opening the indexed primary PDF retrieved the
cached full text. OCR omits some displayed coefficients, so no exact
coefficient or strict numerical remainder is imported from it.

**Ono.** Ken Ono, *An asymptotic Jensen-Polya criterion for GRH*,
[arXiv2610.38870v1](https://arxiv.org/html/2610.38870v1),28October2026.
Use the source's exact T,Lambda,B,A_d,h_q and q_e; its Cauchy identity
(2.9) is valid on every positively oriented origin-centered circle.
Lemma7 identifies the coalescence and the uniform parameter geometry.
Lemma8 controls the complete lower semicircle by a squared difference
of cosines. Lemma12 gives exact gamma factorization; Lemma13 gives a
nonzero saddle amplitude and whole-semicircle polynomial upper bound.
Keep lower logarithmic/square-root branches and conjugate upper branches.
Proposition15 and Corollary16 instead use shrinking saddle intervals;
Corollary16 is stated on I_d=[q_e+M sqrt(log(d)/d),c_0 T]. It supplies
no Airy reference on the saved window. Read the complete proofs of the
named geometric/amplitude estimates and the contour assembly, pp5-14.
No claimed Lean artifact was checked. Theorem1's root-count conclusion
still permits exceptional roots. Its analytic inputs are cited source
inputs, not independently verified here in every foundational detail.

**Other uniform remainder coverage.** A.B.Olde Daalhuis and N.M.Temme,
*Uniform Airy-type expansions of integrals*, SIAM J.Math.Anal.25(1994),
304-321,[final PDF](https://ir.cwi.nl/pub/1473/1473D.pdf),DOI
[10.1137/S0036141090187685](https://doi.org/10.1137/S0036141090187685).
Read Section3's canonical contour/recursion, Section5's Theorems5.1-5.2
and relevant real/imaginary saddle cases, and Appendix exterior-domain
hypotheses. This is not the preliminary AM-R9011 report5700. Theorem5.2
requires those exterior analyticity/growth conditions as well as local
singularity-distance control. Section5 explicitly concentrates on large
saddle parameter rather than giving compact-parameter details. It is
not an automatic two-parameter, degree-dependent amplitude theorem for
this problem. OCR-obscured displays were not used as exact certificates.
The compact edge is better compared with CFU's bounded-parameter proof.
[NIST DLMF2.4(v)](https://dlmf.nist.gov/2.4#v),version1.2.8,was read as
a locator/contour warning, not substituted for these primary hypotheses.

## Applicability ledger and bounded decision

The main gap remains L030-L032/C032a's all-degree actual-Xi algebraic-
square positivity. The intermediate target was a signed Airy comparison
for one bounded unshifted edge window. If eventually paid, it could
supply separated local real-root signs; the outer root deficit, all
other degrees, exceptional roots and identification remain independent.

The following are **unproved specialization obligations**, not results
of this review:

- Put delta=1/Lambda alongside the edge parameter; verify uniform
  analytic neighborhoods, cubic nondegeneracy and simple unfolding.
  Keeping the exact degree-dependent q_e is essential.
- Normalize the actual amplitude on a fixed complex neighborhood.
  A C1 bound on a shrinking real arc does not alone supply all of the
  analytic bounds used by a cubic remainder argument.
- Map the two conjugate local arcs with their orientations, including
  connectors and the transition across the positive real axis. Identify
  the real reference and its coefficient; an arbitrary Ai choice or
  its modulus does not establish the sign of A_d(-q).
- Bound both exterior semicircle pieces on the intended normalization.
  CFU's outside-small assumption is the obligation, not its proof.
- Establish additive normalized o(1) error and separated nonzero
  reference margins before nominating a sign test. Neither is ready.

All original contour sectors were accounted for at the source level:
near-positive-axis conjugate arcs, their connection, and the remaining
lower/upper semicircles through the negative-axis boundary. No sector
was dropped or presumed negligible. This is an inventory of obligations,
not verification of the actual full contour. In particular, no new
specialization or comparison of degree-dependent error rates was done.

**Decision:** stop automatic full-window sign import. This is an
informative source-scope NEGATIVE, not a theorem that the edge expansion
fails. The CFU exterior hypothesis changes the route from an assumed
Airy comparison to an independently testable payment. The concrete new
refinement uses a fixed angular cutoff, rather than extrapolating Ono's
shrinking Gaussian intervals. A separate assessment nominates just that
exterior test; its normalized threshold is a proposed discriminator,
not an established inequality. No further generic Airy browsing is
needed for it. A new ready continuation receives separate supervisor
approval before mathematics. No creative mechanism is claimed for this
standard specialization; signed local cubic control is still absent.

## Searches, duplicates and evidence limits

Queries: `unshifted Jensen Airy`; `Jensen Ono Airy unshifted 2026`;
`2610.38870 edge`; `Jensen polynomials coalescing zeta`;
`unshifted Jensen asymptotic Airy edge`; `Chester Friedman Ursell 1957
coalescing saddle points uniform asymptotic expansions theorem`;
`Uniform Airy type expansions of integrals 1994 theorem 5.1`.
Secondary reviews and unrelated hits were locators only. No inspected
primary source states a stronger matching unshifted signed edge result;
this bounded search proves neither novelty nor absence of such work.

Reuse `2026-11-05-theta-laguerre-uniform-oscillatory-localization.md`
and `2026-11-05-unshifted-jensen-bulk-saddle-discovery.md` without
refreshing their adequate source assessments. Their distinct integral,
scaling and unpaid signed-average issues are preserved. L019/L021/L030
and L795 were read only for the actual kernel, factorial normalization,
main gap and prior interlacing stop; L018's defining line was checked.
No cross-notebook result or improved zero-free region is used. The
new exterior test uses Ono's F directly; it asserts no new local
polynomial-identification lemma. Full Mathlib coverage is unchecked.

Initial active-notebook status/history search output was oversized;
it was not evidence for a claim. Subsequent local reads were named and
bounded. Shell network access failed; primary text remained accessible
through web retrieval. No persistent essential source-access blocker
remains for the exterior test. No lemma, script, PROOF/DAG, shared
infrastructure or supervisor-state edits occurred.

## Retained nomination1344 (target and admission conditions)

Main gap: L030-L032/C032a require actual-Xi algebraic-square positivity
in all degrees. The alternative Jensen route still requires every
unshifted polynomial to be hyperbolic. This proposed local transition
estimate is a possible partial input, never an equivalent-sign premise
or a complete resolution. An edge success would still leave the other
end of the real-root deficit and exceptional zeros uncontrolled.

Use exactly the source's A_d, h_q, T, Lambda and q_e; retain their
d-dependence and the reciprocal transformation back to J_d. Essential
local inputs are L019/L021 for the actual coefficient normalization
and L024/L025/L030 for comparison with the main gap. Import the source
Cauchy identity only after checking its conventions against these.
No cross-notebook theorem is needed. No source-wide Lean or preprint
validation is asserted by the nomination.

Seek a known theorem giving a real Airy reference, its actual positive
or signed prefactor, and a uniform additive error after division by a
specified nonvanishing scale. An o(1) normalized remainder is the
proposed threshold, not a result. Its possible use is to preserve
signs at two explicitly separated reference points with a fixed margin,
if such points lie in this window. Do not divide by an Airy value at
its zeros, infer a sign from an envelope, or assume the desired roots.
A positive density alone is not a signed asymptotic.

Continuation test: inspect the primary theorem hypotheses and relevant
proof cases; identify every actual-contour term, branch and amplitude
bound required to specialize it. Nominate mathematics only if these
produce one precise bounded discriminator with independent payment
obligations. Stop this window if the theorem cannot apply, the global
complement remains an assumed small term, or no nonzero reference
margin can be specified. Any newly ready assessment gets separate
approval before a mathematical attempt; do not derive and approve
an uncovered cubic reduction during this source turn.

Compare the recorded Laguerre full-support/phase stop using only its
named assessment. The new integral is the full Jensen Cauchy integral,
not a pointwise special-function approximation inside a theta average.
Stronger unshifted edge results must be searched before claiming a
new problem or mechanism. The generic coalescing-saddle source is
currently essential unread coverage, so no proof_attempt routing yet.
If it becomes a genuinely new paid mechanism, nominate creative only
with its precise central relevance and bounded test; otherwise use
known specialization or stop honestly. No quota-driven calculation.
