# Two-root coefficient interface — critical audit nomination

TARGET: Critically audit L785's analytic cancellation, coefficient identification and explicit real congruence, including singular coefficient blocks and nullity.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused step456/457 rational-interface queries, primary comparison and duplicate/failure checks; directly checked DLMF analytic statements, de Boor's smooth-function extension and a primary singular-safe Sylvester statement/proof. Searches and exact inspected scope below; no new exact-interface or novelty claim.
SOURCE_EVIDENCE: https://dlmf.nist.gov/1.10 ; DLMF v1.2.8, 1.10.1, Zeros, 1.10.6-7 and removable-singularity paragraph; https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf ; Example2/(10) p.49, Proposition35/proof and Definition37 pp.58-59; https://arxiv.org/pdf/1711.00495v1 ; Nakatsukasa-Noferini Theorem1/full proof p.1 and caveat p.2; Heinig-Rost Proposition7.15/proof p.45 and Proposition9.1/proof p.54 reused from step457.
COMPARISON: The completed two-root attempt identifies a conditional analytic residual using known methods; no source-independent originality or actual-Xi sign conclusion is claimed. An independent audit must check the analytic/local-series distinction and the singular-safe change of basis.
GAP: Source coverage is ready; critical mathematical verification of L785's exact hypotheses, full tail cancellation, six coefficient contributions, map orientation, invertibility and nullity remains outstanding. No actual-Xi coefficient signs or global grouping are supplied.
REASON: A useful coefficient interface should be critically checked before it supports later reasoning; no repeated model diagnostic, new sign theorem or larger-order extension is proposed.
LITERATURE_REASON: The separate audit gate required checking essential analytic, smooth-function divided-difference and singular-safe inertia sources not inspected in the prior rational-interface approval; rational coverage and discovery are reused.
SCOPE: Separate literature approval completed in step459 for one critical audit of L785 only. Preserve sigma>1, disk-neighborhood holomorphy, reality, g(0)>0, exactly two distinct simple negative interior roots and absence of other zeros through sigma; no actual-Xi or all-degree specialization, new sign mechanism or model sweep is approved.

Prior ready coverage is
`2026-11-05-two-root-reciprocal-coefficient-interface.md`; primary
comparison is in `2026-11-05-root-eliminating-reciprocal-bezoutian-review.md`.
That rational evidence is reused; the separate audit gate is completed
below. Do not repeat broad discovery without a changed hypothesis or an
essential unread source.

Essential input is L785, with its complete exact symbolic certificate
`scripts/reciprocal-quartic/two-root-interface-458.json` and implementation.
L784(6)-(8) is motivation/comparison only; L781 and L783 remain contrasts.
No cross-notebook theorem is needed. Full matching Mathlib coverage is
unchecked. A failed audit should identify and preserve a concrete defect;
a passed audit should retain the unpaid actual-Xi coefficient signs,
global grouping, all-degree and other-minor limitations. No candidate
resolution of RH is under review.

## Completed source approval — step459

The main gap is actual-Xi all-degree mixed positivity. The intermediate
target is verification of the conditional two-root coefficient interface,
whose plausible use is a later coefficient sign test without root
isolation. An independently paid signed estimate, actual-Xi grouping,
global coverage and other orders/minors remain unresolved. Approval of
this audit is neither approval of that sign test nor a passed proof audit.

Read all of L785 to inventory its claimed inputs and scope, without
recomputing its coefficient table or testing its certificate. Reused the
ready step457 assessment and step456's primary comparison, including
Heinig-Rost's n-by-n, possibly unreduced rational identity and the
distinct-node evaluation transformation. They are method comparisons,
not premises identifying L785's analytic residual. Their infinity-series
convention and possible singularity must not be transferred silently to
the origin series of 1/g. No reproof of these rational theorems is needed.

### Essential analytic coverage

[NIST DLMF §1.10](https://dlmf.nist.gov/1.10), version1.2.8, released
2026-09-15, read on2026-11-05: §1.10(i), equation1.10.1 and Zeros;
§1.10(iii), equations1.10.6-7 and the removability paragraphs.
Taylor's theorem assumes analyticity in the stated disk and gives
convergence throughout it. The zero-order definition identifies a simple
zero by its first nonzero Taylor coefficient. Laurent's theorem assumes
analyticity on an annulus, gives the contour coefficient formula and
absolute uniform convergence on compact subsets. The punctured-disk
paragraph covers removability when negative coefficients vanish or a
finite limit exists. These are standard inputs, not L785's cancellation
theorem. The audit must justify which canceled function is holomorphic
on which disk before using them; the uncanceled inverse is only local.
The coefficient integral's contour must lie inside the analytic domain,
including when the proof chooses |z|=sigma using neighborhood holomorphy.
These elementary analytic facts need citation and applicability checks,
not a replacement research proof. DLMF states them as reference results;
no claim of reading a DLMF proof is made.

### Divided differences and repeated-node entries

Carl de Boor, *Divided Differences*, Surveys in Approximation Theory1
(2005),46-69, [author PDF](https://pages.cs.wisc.edu/~deboor/sat/papers/2/2.pdf),
dated21December2004: read Example2/(10), printed p.49, and §7,
Proposition35 with its complete proof and Definition37, pp.58-59.
Example2 initially concerns polynomials and gives the two-node quotient
or the derivative at a repeated node. Proposition35 identifies the
derivative-evaluation functionals determining those divided differences;
Definition37 extends them to functions with the required derivatives via
Hermite interpolation. Thus the polynomial wording of Example2 is not
an essential source gap for a holomorphic test function. This covers the
convention only; neither a coefficient table nor matrix inertia follows
from it. L785's matching of node values and derivatives still needs audit.

### Inertia, including singular forms

Yuji Nakatsukasa and Vanni Noferini, *Inertia laws and localization of
real eigenvalues for generalized indefinite eigenvalue problems*,
[arXiv:1711.00495v1](https://arxiv.org/pdf/1711.00495v1), submitted
1November2017; PDF labels its version3November2017. Read §1,
Theorem1 and its entire proof, p.1, and the minmax qualification p.2.
The statement assumes Hermitian matrices of equal size and an invertible
congruence map, with no nonsingularity assumption on the forms. Inertia
explicitly counts positive, zero and negative eigenvalues. The proof
treats zero diagonal entries separately and uses invariance of maximal
positive dimension and rank for the converse. Real symmetric matrices
and real invertible maps fall within this statement. It supplies no
invertibility of L785's proposed map; verifying that is the audit's job.
No generalized-pencil theorem from later sections is used.

The Oxford repository URL returned403. The arXiv primary full text above
resolved access; there is no persistent essential source blocker. The
Pinkham author-hosted book was opened as a possible alternate but its
theorem/proof was not inspected or used. No conclusion rests on a search
snippet. Full matching Mathlib coverage remains unchecked.

### Comparison, decision and audit boundary

Queries used were `site.edu "Sylvester" "law of inertia" "singular"
congruence lecture` and `"Inertia laws and localization of real
eigenvalues" Nakatsukasa Noferini arxiv`. The exact-interface, stronger
rational-result and Xi-sign searches in step456/457 remain adequate for
the unchanged hypotheses and are not repeated. Narrowly checked the
step458 proof/history, step457 approval, and the root-elimination
automatic-sign, linked-factor and local-premise stop records. L784 is
fixed-case motivation; L781 concerns different coefficients; L783
remains an obstruction to automatic index inference, not to this audit.
No additional local duplicate or mathematical obstruction was proved.

EXPLORE is retained for the exact audit rather than IMPORT: the cited
standard inputs are covered, but no inspected theorem verifies L785's
particular canceled tail, six-term coefficient identification or map.
The precise inspection needed is a proof audit, not another source
search or a general congruence reproof. No new mathematics was derived
and no lemma or mathematical script was modified in this literature turn.

Continue only if the audit either validates every claimed step under the
exact stated assumptions, including singular and zero coefficient forms,
or identifies a concrete defect to preserve and repair within this scope.
The audit must check full tail versus local inverse, diagonal residue
signs, all six coefficient contributions, map orientation/invertibility,
and the kernel/nullity assertion without assuming an inverse of a form.
The complete relevant symbolic evidence and implementation must be read
if used; the reported four checks or a preview alone are not verification.
If an essential defect cannot be repaired within these hypotheses, retain
the conditional claim as unaudited/failed as appropriate and close this
attempt without model tuning or a larger-order extension.

The next turn defaults to this one mathematical conceptual audit, using
L785 and its exact certificate/implementation as essential inputs. No
creative central-gap mechanism is justified by these sources: an
independently motivated actual-theta signed inequality is still missing.
This is useful source coverage and gate completion, not mathematical
progress beyond the checked literature or a renewal of exploration.
