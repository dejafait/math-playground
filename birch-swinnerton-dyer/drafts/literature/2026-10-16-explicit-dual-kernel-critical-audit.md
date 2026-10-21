# Explicit dual-kernel critical audit — approved source scope

TARGET: Critically audit L073's explicit dual-kernel presentation and complete replay over all eight direction fibers.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused exact-statement, stronger-result and algorithm searches in drafts/literature/2026-10-16-explicit-dual-kernel-algebra.md; compared the complete L073 proof, step-263 replay record, L072 audit history/260, scalar and quotient audit assessments, and ATTEMPTS/035--037. This is a new audit-scope comparison, not a repeated discovery search or novelty claim.
SOURCE_EVIDENCE: Reuse inspected BMSS arXiv:cs/0609020v1 Theorem 2(2) p.2, sections 2.4--2.5 pp.5--6 and 4.1--4.3 pp.8--13, Proposition 4.1 and fastElkies-prime correctness; Sutherland Fall 2023 Lecture 5 sections 5.5--5.6, Lemma 5.20/Theorem 5.21 pp.10--12 and Lemma 5.24 p.14; Fall 2025 Lecture 6 Theorem 6.7 Case 1 pp.3--4 and Lemma 6.10 p.5; Sage 10.7 baseWI lines 32--40 and 158--203; Stacks 00UB/00UC and previously inspected 03QR; precise qualifications and direct links below.
COMPARISON: Known reconstruction, multiplication, dual uniqueness and standard-etale criteria cover the fixed characteristic-zero models and entire D. They support auditing the actual scaling, both-coordinate compositions and monic two-stage presentation; they do not certify any stored coefficient, recurrence transcription, exceptional point or preservation claim automatically.
GAP: Source scope is sufficient for the separate bounded audit, but L073's correctness is not critically verified by this review. A distinct exact check and complete fresh replay/evidence inspection remain required; no incidence/norm or arithmetic descent is supplied.
REASON: The new critical-audit target has now been compared theorem by theorem with L073 and the existing adequate assessments. A separate RESEARCH / REPRODUCTION proof_audit is supported; general theorem reproof or additional discovery browsing is unnecessary.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED requested separate approval of this new audit target after the construction; unchanged construction coverage is reused, not refreshed.
SCOPE: Exact TARGET only on the conductor-389 curve at seven, full degree-eight D, raw short models, both coordinates and all eight fibers. Exclude L069, partial columns, field decomposition, incidence/norm and descent arithmetic.

## Relevance, duplicates and stopping evidence

The main gap is rank E(Q)=m(E) for arbitrary E/Q with m(E)>=2.
The intermediate target is the critical audit of the explicit affine-line
algebra L073. Reliability of that input could support a later incidence
pullback/norm for L066. Functions, complete units/classes, local data and
bounds, Selmer containment, all other L026 premises, successful localization,
rational membership, divisible Sha removal and arbitrary-curve comparison
remain independent unresolved requirements. This is not a BSD candidate.

Read L073 in full and its step-263 record. The construction assessment
explicitly left this audit pending. History/260 records the completed L072
abstract-family audit; it does not duplicate the explicit-presentation audit.
The earlier homology dual-kernel work concerns a different object.
ATTEMPTS/035--036 retain the two column cost stops; neither presentation
is resumed. ATTEMPTS/037 retains the factor-eight transcription failure
in the even division recurrence. The repaired factor-two replay is the
object to audit, not fresh independent source evidence by itself.

Inputs are audited L067/L068/L070/L071/L072, canonical L073, complete
h/cubic, mixed inverse and both coordinate transports, quotient-254 maps,
original dual-262 evidence and complete dual-263 replay. Accept audited
upstream inputs without claiming a new upstream audit. No cross-notebook
input, selected embedding, rational subgroup generator or root-of-unity
trivialization is permitted. The read of stage-wrapper/check labels only
identified evidence scope; no replay or mathematical check ran this turn.

## Theorem-level comparison and qualifications

[BMSS, arXiv:cs/0609020v1](https://arxiv.org/pdf/cs/0609020v1),
*Fast algorithms for computing isogenies between elliptic curves*,
Theorem 2(2), Proposition 4.1 and sections 2.4--2.5, 4.1--4.3, are reused
from the construction assessment. Numbering is the inspected PDF dated
1 February 2008 (v1 header 6 September 2006), not a newly compared publisher
text; journal citation Math. Comp. 77 (2008), 1755--1778,
DOI 10.1090/S0025-5718-08-02066-8. The characteristic-zero field hypothesis
and normalized degree-seven input are the relevant conditions. L071/L072
provide existence; L073 uses a scaled codomain. The audit must check that
transport before relying on reconstruction. The general precision schedule
and rational-reconstruction bounds must match the actual certificate.
Field-operation complexity gives no runtime guarantee over D. Stark and
unread subgroup-push algorithms are not substitutes approved here.

[Sage 10.7 baseWI](https://raw.githubusercontent.com/sagemath/sage/10.7/src/sage/schemes/elliptic_curves/weierstrass_morphism.py),
lines 32--40 and 158--203, fixes coordinate direction and inverse powers.
Reuse the inspected convention and the construction assessment's dual()
branch (ell_curve_isogeny.py lines 3000--3071). These are implementation
comparisons, not certificates. In the audit, J and its inverse, raw-model
49/343 factors, differential seven and both composition denominators must
be checked explicitly. No minimal Neron-model or period claim is covered.

[Sutherland, Fall 2023 Lecture 5](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf),
sections 5.5--5.6, Lemma 5.20, Theorem 5.21 and Lemma 5.24, supply the
recurrences, parity, multiplication coordinates and noncancellation.
Reuse the scalar-audit assessment's inspected odd/even and negative-index
cases. Analogous numerator verifications are omitted in the notes; the
named theorem is imported, not claimed to have been fully reproved there.
Washington second edition Theorem 9.33 remains an unread proof reference.
The nonsingular short curves over characteristic-zero D meet the hypotheses.
The repaired recurrence and every division must be checked in the audit;
source coverage does not excuse a second transcription error.

[Sutherland, Fall 2025 Lecture 6](https://math.mit.edu/classes/18.783/2025/LectureNotes6.pdf),
Theorem 6.7 prime-degree Case 1 and Lemma 6.10, supply the unique dual and
both compositions. Degree seven is prime to characteristic zero, and
L071 supplies the separable quotient over D. Comparing a candidate to the
actual dual by dominant pullback is within this coverage. Curve substitution
alone does not establish that the candidate is the dual. Reuse the inspected
Vélu local/quotient coverage in
`drafts/literature/2026-10-16-direction-quotient-critical-audit.md` for the
projective exceptional-point audit; no new general quotient proof is needed.

[Stacks Definition 10.144.1, 00UB](https://stacks.math.columbia.edu/tag/00UB)
and [Lemma 10.144.2, 00UC](https://stacks.math.columbia.edu/tag/00UC) give
the monic/invertible-derivative standard-etale criterion and its base-change
statements. Their omitted proofs remain explicitly standard-theorem imports.
The audit must verify the actual k-prime and cubic unit witnesses and the
quadratic derivative, not assume reducedness from a dimension count.
Successive monic bases require uniqueness, as well as spanning.

Reuse L072's separately audited family identification and
`drafts/literature/2026-10-16-quotient-affine-line-critical-audit.md`:
[Stacks 03QR](https://stacks.math.columbia.edu/tag/03QR) applies after exact
equivariant identification, retaining all orbits. L073 must preserve that
identification, inverse ordinary-functional labels and Cartier cyclotomic
action. Viewing a D-scheme over Q is composition, not Weil restriction.
This review neither reopens L072 nor infers an algebra isomorphism from 48
points alone. No essential source gap was found within this exact scope;
no primary text was newly retrieved or claimed newly read this turn.

## Bounded separate audit

1. Read the actual producer, repaired verifier and wrappers before running
   them. Inventory originals first. Save fresh reports in a fresh audit
   directory; never invoke the old verifier in place, since it writes reports.
   Review all normalization, series, reconstruction and constant-unit evidence,
   the two-coordinate maps, symbolic divisions and original recurrence failure.
2. Perform one fresh full replay over D, inspecting complete relevant residuals,
   both composition orders in both coordinates, every retained recurrence/series
   coefficient, all units and the full product table. Complete exact evidence,
   rather than previews or passed flags, is necessary.
3. Add a distinct exact multiplication/composition cross-check using the
   elliptic group law through the chain 1,2,3,6,7, independent of the compressed
   division recurrence and BMSS producer. Keep both coordinates and the entire
   D. A full symbolic check is permitted; exact evaluation/interpolation is an
   alternative only with explicit proved numerator-degree bounds, enough
   distinct points and certified nonzero denominators. Random or selected-root
   samples cannot pass. This is verification of the imported multiplication
   theorem's fixed instance, not a new multiplication theorem.
4. Critically review every projective kernel point, both signs over every root,
   O, pole orders, numerator noncancellation and exact degree. Check both monic
   quotient bases, derivative units, identity removal and all eight embeddings.
   Do not require or infer fieldness of the 48-dimensional algebra.
5. Preserve and accurately describe the old preliminary rejection tests.
   Add bounded fresh malformed-evidence cases for normalization, sign and a
   changed late coefficient, recording exactly which checks ran and failed.
   Do not report an early condition rejection as a full malformed replay.
   Check hashes of all inventoried original and upstream files after work.

All new arithmetic, including fresh rejection checks and the distinct check,
belongs to one audit stage capped at 180 seconds, external watchdog 181
seconds, with at most 128 MiB new evidence. Do not restart a failed stage,
raise caps or retrospectively subdivide it. Save work notes before running;
write full certificates and print compact actual/required bounds and paths.
Use the shared bounded inspector for selected complete load-bearing fields.
Continue only if source hypotheses, complete replay, distinct exact check,
exceptional-point/basis review and preservation all pass. On a discrepancy
or cap, stop and preserve the precise incomplete claim before dependent use;
an uncovered replacement requires separate REVIEW_REQUIRED coverage.

This approval is source sufficiency only. It derives no new mathematical
result, certifies no coefficient, changes no lemma or mathematical script,
and does not declare L073 audited. Full matching Mathlib coverage remains
not checked; unknown availability is not absence. The next turn defaults
to the exact mathematical proof audit, rather than additional literature.
