# GC12 diagonal Mellin test: source comparison2087

TARGET: Review primary coverage for a one-sided Landau-Mellin test of the actual GC12 diagonal square sum, using its one-variable Mellin transform and retaining all signed and nonlocal contributions.
CHECKED: 2026-11-21
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed2087 searched Landau/Mellin one-sided oscillation, diagonal square-cutoff double Dirichlet series and convolution singularities; checked C034s/C034r and stops2076/2077/2079/2084. Exact queries, inspected ranges and access limits are in drafts/literature/2026-11-21-gc12-diagonal-source-notes-2087.md; no novelty inference.
SOURCE_EVIDENCE: Kaczorowski--Pintz1986 p173 named Landau/Pólya statements; Bhowmik--Ramare--Schlage-Puchta2016 author working PDF Theorem1.2/(1.1)-(1.5) and Section2 pp2,4-6; Matsumoto--Nawashiro--Tsumura arXiv1801.04444v3 Assumption4.1, Theorem4.3 and essential continuation cases pp9-11; Perez-Marco author PDF Proposition2.1/Theorem2.3 and proofs pp7-8; NIST DLMF2.5(i). Full citations and limitations in source-notes2087. Landau1905 original and the2016 publisher PDF were inaccessible; neither is claimed read.
COMPARISON: No direct import supplies GC12's full diagonal singularity or upper contradiction. The quantitative oscillation theorem needs nonreal boundary blowup, real boundary limits and dyadic L2 control; these are unpaid, and its real-boundary hypotheses do not cover the proposed real pole. The nearby Mobius continuation theorem assumes simplicity and reciprocal-derivative growth and concerns a different additive kernel. Hadamard's singularity inclusion does not force a singularity or a sign.
GAP: The complete signed diagonal transform, its continuation from the defining integral, its real convergence boundary and the sign of its full singular part remain unproved. C034s supplies only a local contribution. A nonnegative-defect Landau test must establish those missing facts rather than infer them from the residue.
REASON: The review rules out the inspected direct-import detours and narrows the next attempt to the complete-transform/defect obstruction. Source scope is sufficient for a bounded attempt, not for a GC12 conclusion; no new mathematics was derived here.
LITERATURE_REASON: The exact diagonal transform and one-sided Tauberian implication are outside assessment2084's local bidisk scope; essential theorem-level coverage is missing.

## Exact object and possible use

Use C034s's actual GC12 square sum, with q=2 and its specified bump,
arithmetic weight and ratio kernel. The proposed object to assess is

\[
 \mathcal F(z)=\int_2^\infty
       M_{\lfloor X\rfloor}X^{-z-1}\,dX,
\]

initially only where the integral converges absolutely. This is a
definition of the proposed object, not a derived continuation formula.
The desired source comparison concerns the one-sided bounds
\(M_K\le C_\epsilon K^\epsilon\), for every \(\epsilon>0\),
and whether a hypothetical zero with exact order m>=1 and
0<delta<1/2 can yield a discriminating test through this transform.
In particular, a real singularity at z=2delta is a proposed question,
not a consequence imported from C034s. No global asymptotic or
Omega statement is established by this nomination.

This changes the object from a local bidisk germ to a diagonal
one-variable transform. It could clarify whether a Mellin obstruction
actually bears on the low primitive upper needed downstream of C034r.
The main gap remains L030-L032/C032a actual-Xi algebraic mixed positivity;
the high primitive upper, scale errors, full source energy and transfer
remain independent even if this narrower test succeeds.

## Required comparison and bounded decision

Retrieve exact primary statements and essential proof cases for any
Landau or one-sided oscillation theorem proposed, including the sign,
convergence and continuation hypotheses. Compare the actual signed
square sum with those hypotheses; do not replace it by an absolute
square, a positive GCD form or an unsigned majorant without a paid
comparison. Check existing local literature and recorded failures
before nominating a mathematical subtarget. The source review should
produce one independently testable conditional implication or an
informative reason this diagonal mechanism does not yet discriminate.
It must not derive the diagonal transform or approve a new lemma.

Continue only if that comparison specifies a bounded mathematical
test which retains possible cancellations and does not assume the
desired upper or a zero-free conclusion. Otherwise record precisely
the missing sign or global-continuation premise and park this proposed
implication. Repeating the already audited local nonzero coefficient
does not count as a test of the diagonal question.

Essential input: C034s's actual sum and audited finite/local statements.
C034r supplies the kernel and conditional downstream detector; its
detector is not a statement about GC12 alone. L030-L032/C032a are
relevance only, and C034q/stops2076/2077/2079 are contrasts. GC13/GC18
remain locally unaudited and may not be assumed. There is no RH,
rightmost-zero, simplicity or uniform-separation premise, and no
cross-notebook input. Matching Mathlib coverage is unknown.

The preceding nomination was REVIEW_REQUIRED in2086. Comparison2087
completes that source task; it does not prove the nominated singularity.
The precise mathematical continuation has its own assessment
[defect test2087](2026-11-21-gc12-complete-diagonal-defect-test-review-2087.md).
That newly written continuation requires separate supervisor approval
next turn. No mathematical attempt on it was performed in2087.

## Completed decision2087

Park direct application of the quantitative nonreal-boundary theorem
and direct import of the additive Mobius continuation theorem. These
are hypothesis mismatches, not impossibility results for GC12. The
historical local stop2084 remains unchanged. A nonnegative-defect
approach is independently testable because it asks about the complete
one-variable transform and its real convergence boundary, not another
calculation of the already positive bidisk coefficient. See source-notes2087
for the exact source limits and the continuation's pass/stop evidence.
