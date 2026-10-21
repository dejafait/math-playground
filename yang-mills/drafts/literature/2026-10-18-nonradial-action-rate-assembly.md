# Complete nonradial action rate — assembly applicability comparison

TARGET: Assemble the complete nonradial action O(N^(5/2)) remainder using L213, L215, L230 and L231 for both actual probes.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L213(1)--(3) and proof sections 3--5, L215(5)--(6),(15)--(16), L216(1)--(3),(15)--(16), L217(2),(6),(14), L230 hypotheses/conclusion and section-7 audit, and L231 hypotheses/conclusion and section-6 audit; searched notebook-local rate assessments and ATTEMPTS/011--013. Reused existing primary-source assessments without a new external search; no completed exact quantitative assembly was found in the inspected records.
SOURCE_EVIDENCE: Reuse 2026-10-18-direct-mixed-action-quantitative-remainder.md and its separate audit assessment, and 2026-10-18-plateau-action-quantitative-remainder.md and its separate audit assessment. These record inspected Lawler--Limic (2010), Theorem 4.3.1, Corollary 4.3.3, Proposition 4.6.2(a), Theorem 6.3.8(a), and DLMF section 1.4(vi), (1.4.35)--(1.4.37); L230 section 7 and L231 section 6 accept the local specializations relative to imported inputs. No external result is newly imported or rechecked here.
COMPARISON: L215(15) changes only the positive two-prefix block; L216(1)--(2) defines exactly its plateau replacement, while L217(14) defines the untouched direct/direct and both negative mixed blocks. L230 and L231 use those same blocks and coefficients. Existing estimates cover the proposed assembly inputs; the finite error assembly and its N-independent bound remain a separate research task.
GAP: Write the complete finite-response assembly with L213's discarded classes and L215's replacement error counted once, then combine the two audited block rates relative to the unchanged coefficient P_i+A_i^dm. No additional analytic source gap was identified; no assembled rate is proved in this review.
REASON: The exact target is source-ready as a finite specialization of existing canonical estimates. No Green theorem, continuum limit or component rate needs reproof; preserve all imported hypotheses and justify only the finite assembly and comparison of its error scales next turn.
LITERATURE_REASON: Mandatory separate comparison of the newly registered exact assembly target, which was not preapproved by either component audit assessment; existing essential source coverage is reused.
SCOPE: Same relative SU(2) cube, straight lower-rooted forest, sufficiently large admitted even N, a=8/N, tau=1/16, probes i=3,6, and fixed-mesh bare expansion first. Only the complete nonradial action group is proposed.

## Disposition and relevance

This separate literature-only review replaces the pending registration
with SPECIALIZE for the identical TARGET. A later invocation may perform
the assembly after supervisor approval of this changed assessment. This
turn proves no new inequality and changes no lemma or mathematical script.

The main gap remains ultraviolet-uniform interacting reflected control
<=c_box/2, continuum axioms and infrared finite positive mass. The one
intermediate target is the complete nonradial-action remainder stated
above. Its plausible use is one component of the quantitative L011
program after cubic cancellation. Independent component rates, L220's
critical review and a uniform interacting expansion remain unresolved.
There is no construction candidate or claim beyond the checked sources.

## Exact expression and applicability checks

L213(1) is the complete negative nonradial-action cumulant, not the
whole L011 response. Its (2) retains only the transverse 24-pair class.
Proof sections 3--4 account for the other axial levels, upper three-edge
vertices, transverse 48-pair class and fixed boundary plaquettes. In
particular the upper axial estimates are signed complete sums, rather
than absolute termwise bounds; their use must remain in that scope.

L215(15) has one direct/direct term, two negative mixed terms and one
positive two-prefix term. Only the last is replaced. Its (6) already
includes a bound from the complete response to the replaced contraction;
using that bound and then adding L213's error again would duplicate an
error allowance. Alternatively one may use the two successive errors,
each once. This distinction is bookkeeping, not an uncovered class.

L216(1)--(2) is precisely the replacement's two-prefix contribution.
L217(14) is precisely the other three terms, with each mixed orientation
separate. Both retain L025's original K, U, traversal signs, diagonal
color blocks and -24 contraction. No Gaussian-tilt factor 2, extra
outside factor 3 or separate top/top cubic contribution belongs here.
L216(16) is a qualitative asymptotic statement; the next proof must use
the finite definitions and L215's finite bound instead of assigning a
rate to its o(1).

L230(1)--(2), accepted in its section 7, subtracts the original A_i^dm
of L217(6) and gives O(N^2 log(eN)). L231(1), accepted in its section 6,
subtracts exactly P_i of L216(9) and gives O(N^(5/2)). All six inputs
use the same stored coordinates, a=8/N, admitted even meshes, actual
probes 3 and 6, tau=1/16 and bare-first expansion. Their constants may
depend on the fixed probe/displacement data but not N. The later assembly
must explicitly compare these scales and specify the summed coefficient;
the present review neither evaluates it through L219 nor uses L220.

## Reused literature, duplicates and failures

The two component assessments and their audit assessments above are the
ready source records. Their exact source passages and proof cases remain
applicable: the assembly changes no Green kernel, boundary condition,
smoothness assumption or heat-mode envelope. Lawler--Limic,
[*Random Walk: A Modern Introduction*](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
Cambridge 2010, Theorem 4.3.1 and Corollary 4.3.3 (printed pp. 81--84),
Proposition 4.6.2(a) (p. 97) and Theorem 6.3.8(a) (p. 131), supplies
the recorded transient simple-walk and harmonic difference inputs.
Their scalar Laplacian normalization and dimension restrictions remain
those checked in the component records; they do not directly state a
relative edge-response theorem. The bipartite and source-distance cases
were inspected there. No reproof or fresh specialization of them is
needed for a finite assembly.

[NIST DLMF section 1.4(vi)](https://dlmf.nist.gov/1.4#vi),
(1.4.35)--(1.4.37), supplies the recorded closed-interval C^(n+1)
Taylor formulas. The component assessments record v1.2.8 and separately
qualify their later live URL checks; this review asserts no new version
check. Only smooth deterministic coefficients and modes qualified there.
No Taylor regularity is assigned to a pinned prefix. The optional
Braun--Hudson--Ortner Theorem 3 comparison in the direct/mixed record
remains nonessential; it is not a new input to this assembly.

The local duplicate check found L217's accepted qualitative full-action
limit and the two component rate proofs, not a canonical quantitative
full-action assembly. This limited search does not establish novelty.
The older complete-coefficient assessment's EXPLORE coverage explains
L213--L217's source scope; its historical open gaps are not current
instructions. ATTEMPTS/011--013 stop raw-loop boundedness, bounded local
Wick coefficients and smooth upper-pin extension. The present target
imports the signed bounds that retain those obstructions and does not
reopen any of these failed shortcuts.

## Continuation test and qualifications

Essential inputs are L213 L215 L216 L217 L230 L231, with every upstream
analytic hypothesis imported rather than recursively audited. Continue
with one finite assembly proof only if its partition counts every class
once, matches P_i+A_i^dm with the original a^(-3) normalization, and gives
an N-independent O(N^(5/2)) error for both probes after the full heat
sums. If an unmatched class, coefficient, normalization or scope change
appears, stop that assembly and record the precise missing input; a
changed mathematical target requires REVIEW_REQUIRED. No stronger rate
or uniform interacting conclusion is licensed.

Full matching and supporting Mathlib coverage remain **not checked**.
Unknown availability is not absence. A later proof should cite the
canonical component results and justify only this finite specialization;
no general source theorem needs to be reproved.
