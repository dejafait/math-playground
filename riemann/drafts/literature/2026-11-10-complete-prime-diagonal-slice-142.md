# Complete-prime diagonal slice — source review completed in step143

TARGET: Determine whether the diagonal {2,3,5,7} slice of L960's complete polynomial at (t,x)=(98/625,6000000185827) has a zero in |z|<=1, retaining every supported smooth term.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step143 checked the scoped step133 comparison, L960 definitions and relevant local failure filenames; searched Schur-Cohn root counting/unit-circle singularities, the Planat–Raymond diagonal test and official Mathlib coverage; read primary passages listed below. No exact-slice certificate was located; this bounded search makes no novelty claim.
SOURCE_EVIDENCE: Planat–Raymond arXiv:2611.06245v1 Section4 definitions, Proposition4.1/Remark4.2, Lemmas4.3–4.4 and Theorem4.5 incl. Section4.3.2, https://arxiv.org/html/2611.06245v1#S4; N.J.Young, Comment.Math.Univ.Carol.19(4)(1978),673–688, Theorem3/proof pp.684–685 and shift specialization p.686, https://dml.cz/bitstream/handle/10338.dmlcz/105883/CommentatMathUnivCarol_019-1978-4_5.pdf; Dym–Young, Proc.Edinburgh Math.Soc.33(1990),337–366, scalar Schur-Cohn statement pp.337,340; NIST DLMF1.10(iv), argument principle (1.10.9) and Rouche theorem, https://dlmf.nist.gov/1.10#iv. Reuse the step139 interval/elementary-source assessment in 2026-11-10-centred-moment-rational-replay-138.md.
COMPARISON: The source stability certificate starts at156821/1000000, strictly above the requested98/625=156800/1000000; its lower-time analytic module is conditional on stability. Proposition4.1 is a necessary Gram-weight ceiling, not a root-location assertion. Young's exact strict criterion supplies a known finite method; the complete-support coefficients, reciprocal orientation and certified matrix/contour bounds still require local specialization.
GAP: No coefficient list, natural index, root count or zero-free margin for this exact slice has been certified. Future work must verify the full smooth support and degree, enclose all coefficients, and obtain a strict Schur or Rouche certificate; ambiguous enclosure/singular cases remain inconclusive unless separately resolved.
REASON: The completed source review approves the unchanged finite test, with no theorem reproof or novelty claim. Its time lies outside the paper's certified stability band, so neither that certificate nor the earlier scalar moment audit supplies the answer. No new mathematical lemma, coefficient construction, root search or script was made in this literature turn.
SCOPE: One exact positive-time corner and one explicitly defined coordinate slice; no parameter sweep, smaller prime head substituted for full support, global stability, torus modulus, collision exclusion or RH claim.

The following nomination and recovery comparison are preserved from step142.
Their pending-source language is superseded by the completed step143 review
below; the mathematical target and its support have not changed.

## Exact proposed object and downstream use

Use the exact L960 definitions of c_pol, sigma, a_n and the right natural
index N at t=98/625 and x=6000000185827. In its complete polynomial set
z_2=z_3=z_5=z_7=z and all other prime coordinates to0. Equivalently the
proposed univariate polynomial retains every n<=N with prime divisors
in {2,3,5,7}, with coefficient a_n and exponent Omega(n); include n=1
and every allowed repeated prime power. This is the target's definition,
not a new proved criterion or a replacement for the physical character.
Do not round x, freeze a guessed N, discard smooth composite terms or
identify this with a four-prime multilinear head.

The intended test is a rigorous count of zeros in the closed unit disk,
including a separate treatment of boundary zeros. A certified zero would
obstruct the complete-polydisc premise at this corner; a zero-free slice
would only pass this necessary test, not establish the full premise.
The review must justify that interpretation and the chosen root-count
method before any computation. Schur-Cohn is an unread algorithmic lead,
not an imported theorem. Compare it with a certified argument-principle
count if a Schur-Cohn boundary or leading-coefficient case is unsuitable.

Continue only if the source comparison leaves a genuinely untested,
finite certificate target and provides exact hypotheses for its method.
If the source already settles precisely this complete slice, import that
result with its qualifications; if it treats only a different truncation,
record the difference. A numerical root approximation, a failed search,
or a zero-free proper head is not decisive. An inconclusive boundary test
must remain inconclusive, with no inferred stability or obstruction.

## Recovery comparison and essential qualifications

The step142 route record compares exactly three mechanisms: a direct
analytic remainder/derivative audit, this finite stability restriction,
and the previously limited collision-energy continuation. The selected
restriction asks a different question from M32, and can be tested without
first certifying the other L960 premises. Preserve the fixed-source
obstruction from step133; historical failure of that source is neither
a proof about this slice nor a ban on a changed complete-support test.

Essential local input is L960's definition and complete-support contract;
the prior moment bound is context, not a root-count premise. L019/L058
only matter to eventual physical normalization, not this polynomial test.
All independent remainder/derivative, companion, phase/support, full
model/modulus, initialization/recovery, seams/exterior, zero-time and
L030–L032/C032a signs remain unresolved. No cross-notebook input.
Mathlib coverage for the proposed root-count method is unchecked.

Next routing is literature_comparison/standard/high. A later finite
specialization is not automatically a creative central proof attempt.
No justified new mechanism for zero-time or all-degree signs emerged in
the scalar audit; missing source comparison and that unbridged central
gap block a defensible creative nomination here. This candid limitation
does not authorize another moment approval/replay cycle.

## Completed primary-source comparison — step143, 10 November 2026

The main gap remains L030–L032/C032a. The intermediate target is exactly
the TARGET above. It tests one necessary restriction of L960's assumed
complete-polydisc nonvanishing; even a positive answer to zero exclusion
cannot pay full stability, the torus modulus, physical errors or zero time.
No coefficient or root calculation was performed in this review.

### Source scope and recorded overlap

Read L960's hypotheses, source convention and step136 coefficient identity;
reuse step133's comparison and its collision-route failure evidence.
The reviewed Section4 of Planat–Raymond, v1 dated 4 November2026, uses
time a=156821/1000000 and cutoff C=690988. Its Theorem4.5 assumes the
source inverse-defect/torus inequalities and three strict leaf gates;
its conclusion is a closed-polydisc modulus bound on a<=t<=1/5.
Section4.3.2 reports the certificate margins. Neither those data nor the
paper's analytic band starting at98/625 extends that stability conclusion
to t=98/625: the latter band is a conditional admission module. The
requested lower corner is therefore outside the certified stability band.
No backwards heat inference or certificate import is licensed.

Proposition4.1 requires positive normalized Gram weights and strict
positivity at the all-ones torus point; its conclusion is only the
necessary ceiling delta_j<2P_(1,j)-S_j. Remark4.2 labels its crossing a
diagnostic for that fixed family. It is not a polynomial-zero certificate.
The proposed slice retains the complete smooth fibre with repeated powers,
at the requested time and actual N; it is not a multilinear prime head.
The paper defines that fibre, so its construction is not a novelty claim.

Read source definitions before the ceiling proof, then the ordinary
recovery and forward-heat cases (including constants, repeated roots and
the equality case), finite-exterior gluing and its parameter range. This
compares theorem scope; it does not independently validate the source
certificate or establish any local specialization of those proofs.

### Primary strict test and degeneracies

N.J.Young, *Norms of certain rational functions of a matrix and Schur's
criterion for polynomials*, Comment.Math.Univ.Carol.19(4)(1978),673–688,
[Theorem3, pp.684–685](https://dml.cz/bitstream/handle/10338.dmlcz/105883/CommentatMathUnivCarol_019-1978-4_5.pdf):
for a complex polynomial p of degree d>=1, let
q(z)=z^d conjugate(p(1/conjugate(z))). If a d-by-d matrix A has spectral
radius<1 and I-A* A is positive semidefinite of rank one, all roots of p
lie in the open unit disk iff q(A)*q(A)-p(A)*p(A) is positive definite.
Read both directions: the converse removes the common-factor issue,
rather than assuming coprimality. The source then chooses the backward
shift S(x_1,...,x_d)=(x_2,...,x_d,0), pp.685–686, recovering Schur's
criterion. This theorem does not assume simple roots or a nonsingular
Schur matrix as an input.

For the future application, first certify the complete slice Q, its
actual degree and nonzero constant/leading coefficients. Apply the cited
test to its reciprocal when testing exclusion from the closed disk;
verify the reversal and matrix sign in the canonical specialization.
Do not apply the open-disk theorem to Q and call that exterior stability.
A strict positive-definiteness certificate for the correctly oriented
form settles exclusion. A certified failure of definiteness for that
exact form can settle existence in the closed disk; an interval pivot
containing zero does not certify such failure. Use a rational nonzero
test vector with a strictly negative enclosed quadratic form, or a
complete certified inertia calculation, for a robust failure witness.

For a complete interior/exterior count, the scalar Schur–Cohn statement in
Harry Dym and Nicholas Young, *A Schur-Cohn theorem for matrix polynomials*,
Proc.Edinburgh Math.Soc.(2)33(1990),337–366,
[pp.337,340, Theorem1.1 and scalar specialization](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5AB9F1B5788EC10C3C510CB2218B26FE/S0013091500004806a.pdf/schurcohn_theorem_for_matrix_polynomials.pdf),
requires the nonconjugacy condition relative to the unit circle in the
ordinary scalar formulation. Certify that condition and the correspondence
with the chosen form before using its signature count. A singular form
alone must not be called a unit-circle root: reciprocal-conjugate pairs
off the circle also cause degeneracy. No singular-case counting extension
is imported. The Young strict criterion remains sufficient for the binary
question when its required strict evidence is available.

### Contour alternative and coefficient evidence

[NIST DLMF1.10(iv)](https://dlmf.nist.gov/1.10#iv), equation1.10.9,
counts zeros minus poles with multiplicity inside a positively oriented
simple closed contour; analyticity and nonvanishing on the contour are
essential. The following Rouche theorem requires analytic f,g on and
inside that contour and the strict inequality |g|<|f| everywhere on it.
These statements were inspected. They support a certified contour count
or isolated interior-root disk if a Schur computation is unsuitable.
On the unit circle, a zero-free contour plus the count resolves the
closed-disk question; a boundary zero prevents that application. Neither
method infers a boundary count from samples or an unresolved enclosure.
There is no selected singular-case algorithm to reprove in this turn.

The finite computation must establish N by enclosing the natural-floor
inequalities, enumerate every supported2,3,5,7-smooth integer once with
all prime powers, collect equal Omega exponents, and enclose the complete
coefficients. The highest retained coefficient must be nonzero; degree
zero, a zero constant or an indeterminate leading coefficient must be
handled explicitly, not silently normalized. These are future certificate
obligations, not results of this review. No guessed N or degree is saved.

Reuse the directly inspected interval/elementary sources in step139 of
`2026-11-10-centred-moment-rational-replay-138.md`: Daumas–Lester–Munoz,
arXiv:0708.3721v1, III, Propositions9/10/12, and the specified NIST
log/exp/arctangent formulas. Positive log inputs, nonnegative square-root
inputs and zero-free interval divisors remain mandatory. They cover
inclusion arithmetic, not the correctness of a new Python implementation.
Only the elementary evaluator is reusable; no moment leaf or Simpson
bound is a root-count input. A rational midpoint polynomial alone is
insufficient: every matrix sign or contour inequality must hold for the
exact coefficients through enclosing intervals and justified finite tails.

### Search/access record, decision and continuation

Locator searches included `Schur Cohn polynomial root counting unit circle
singular Hermitian form theorem primary`, `Planat Raymond polynomial
stability2611.06245`, `Planat Raymond diagonal Schur`, and official Mathlib
Schur-Cohn/Rouche coverage. Local searches used those root-test terms and
the exact paper/proposition identifiers in drafts/literature and ATTEMPTS.
No inspected result answered this exact lower-time slice. This does not
establish originality. The step133 fixed-family warning and step142
moment-loop stop are preserved; neither bans this independent test.

The Utrecht1979 report was a locator lead only: its PDF text/screenshot
delivery was not usable here and shell retrieval failed DNS resolution.
The Hu–Zhan–Chen2015 singular-case PDF returned an access-denied response.
Neither is used as an input. Young1978 supplies the needed accessible
strict theorem, so these optional failures do not block the selected
binary test. Dym–Young's theorem/formula passages were readable, but no
matrix-generalization proof or singular-case extension is imported.
Mathlib: searches did not locate a full matching strict Schur criterion;
the current library sources were not exhaustively checked. Full matching
coverage remains unknown; a reference index or unrelated Schur theorem
is not evidence of coverage or absence.

Decision SPECIALIZE: approve the unchanged TARGET for one bounded finite
certificate attempt, classified REPRODUCTION of a standard root-location
method on this source-defined object, not a new theorem beyond the sources.
Continue only on a certified closed-disk obstruction, a certified exclusion
or informative exact boundary/degeneracy evidence. Stop at unresolved
strict gates and retain INCONCLUSIVE; do not infer stability or refute RH.
No parameter sweep or full-torus reconstruction is approved. Save complete
support, coefficient enclosures, actual/required margins and every failed
gate to disk; inspect the load-bearing evidence before claiming a result.

Essential input is L960's exact coefficient/support definition and the
primary theorem above. L019/L058 are downstream normalization only.
Remainder/derivative, companion, phase/support, full model/modulus,
initialization/recovery/seams/exterior, zero-time and actual-Xi signs
remain independent gaps. No cross-notebook input. The next work is an
ordinary implementation/calculation at standard/high. No defensible new
central creative mechanism was prepared by this narrow source review;
the zero-time and mixed-sign bridge is still missing. That blocker does
not justify another scalar approval loop or an invented creative label.
