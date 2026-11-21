# Signed contact-cell test — completed source comparison

TARGET: Test whether contact-parity propagation and L883's signed cell periods obstruct L882's matched conjugate-label branch, retaining every other zero and the d=0 case.
CHECKED: 2026-11-07
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded external searches for constant-phase checkerboards, contact parity, nodal domains and relative signed periods, plus scoped comparison of L879's edge proof, L880's vertex interface, L882's exact odd-fiber census, L883's formula and named failures; no matching theorem was identified. Queries, inspected primary passage and reuse limits are recorded below; no novelty inference.
SOURCE_EVIDENCE: Reopened Lawrence-Yamauchi arXiv:2311.13002v2 Section II B (9)-(16), pp3-4, and its zero-separation paragraph, https://arxiv.org/html/2311.13002v2#S2.SS2 ; reuse inspected Lebl CA v1.10 Theorem2.4.7 pp49-50, https://www.jirka.org/ca/ca.pdf#page=49 , and Merry Differential Geometry (2020-2021) Theorems26.2/26.17 PDF pp213,218-220, https://www2.math.ethz.ch/will-merry/files/Merry%20-%20Differential%20Geometry%20%282021%29.pdf#page=218 , through the named existing assessments and audited local specializations.
COMPARISON: General stationarity permits different phases across zeros; it supplies no contact-parity checkerboard or signed label restriction. L879 already proves open-edge parity and the squared-diagonal comparison, L882 restricts complete odd-label fibers, and L883 evaluates the periods. Their combination for signs within these four cells and any resulting nonautomatic actual-label condition remains a mathematical application, not an imported theorem or completed duplicate.
GAP: Justify domainwise sign propagation using the full finite angular arrangement, then compare only justified signs with all four L883 periods; distinguish a necessary inequality, automatic compatibility and actual branch exclusion. No cell-sign law or incompatibility has been proved in this review.
REASON: Essential source comparison now covers one bounded attempt at the unchanged target; no essential source blocker remains. Reuse the established factorization, parity, fiber and period inputs without reproof; the new signed assembly must be attempted separately after source-scope approval.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changed from common-line cell values to domainwise contact signs and signed-period compatibility; existing tool coverage is reused while this missing theorem comparison is completed.
SCOPE: Exactly L847's actual full form and angular orientation, L879's smooth real periodic stationary u with J nowhere zero, and L882's matched boundary branch eta=theta=conjugate(zeta)!=zeta. Retain all other zeros, simultaneous contacts, diagonal vertices, actual phase lambda and L883's fixed arc lifts. No exchange symmetry, product graph, analytic u, finite pullback-contact census, positivity or nonzero d assumption.

## Completed review — 7 November 2026

STEP_ID: 2026-11-07-signed-contact-cell-source-review-60.
This turn is LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. The target
text is unchanged. Source coverage is local preparation, with no new
mathematical result, sign calculation, lemma or mathematical script.
The new EXPLORE decision requires the supervisor's separate approval
next turn. The historical nomination below is retained; its requests
for missing review are discharged by this section.

### Precise primary comparison and reuse

Scott Lawrence and Yukari Yamauchi, *Convex optimization and contour
deformations*, [arXiv:2311.13002v2, Section II B, (9)-(16), pp3-4](https://arxiv.org/html/2311.13002v2#S2.SS2):
reopened the real functional-gradient convention, integration by parts,
inverse-Jacobian multiplication and following zero-separation passage.
Holomorphic density, an invertible complex Jacobian and unrestricted
variations yield a necessary off-zero phase condition. Different
zero-separated pieces can retain different phases. Neither contact
parity nor signs of these four cells follow from this source alone.
L879 supplies the accepted real-radial specialization; no sufficiency,
flow convergence, global perfection or attainment claim is imported.
Reuse the cosine comparison's already inspected proof and parameter
limits in `2026-11-06-stationary-graph-phase-components.md`; that
generic model is not an actual-G counterexample. The rendered HTML
has formula/date artifacts already noted there; the fixed v2 PDF and
its previously inspected proof remain the version reference, not the
HTML's generated date. No new version claim is made.

Reuse `2026-11-06-stationary-graph-phase-components.md` and
`2026-11-06-odd-contact-boundary-fiber-compatibility.md` for Jiří Lebl,
*Guide to Cultivating Complex Analysis*, v1.10 (5 November 2026),
[Theorem2.4.7 and finite-order factorization, pp49-50](https://www.jirka.org/ca/ca.pdf#page=49).
G is entire and G(0)>0, so this known result applies to its ambient
zeros in the compact annuli used in L879. It asserts no finiteness
of smooth pullback contacts, analytic regularity of u, or sign law.
The existing L879 angular arrangement, rather than a replacement
smooth-nodal or normal-crossing theorem, is the proposed tool.

Reuse `2026-11-07-contact-cell-relative-period-test.md` and
`2026-11-07-l883-contact-cell-period-conceptual-audit.md` for Will J.
Merry, *Differential Geometry*, ETH 2020-2021 (17 July 2021),
[Definitions25.1/25.20 and Theorems26.2/26.17, PDF pp208,211,213,218-220](https://www2.math.ethz.ch/will-merry/files/Merry%20-%20Differential%20Geometry%20%282021%29.pdf#page=218),
and Lebl, [Definition4.1.1/Proposition4.1.2, pp94-95](https://www.jirka.org/ca/ca.pdf#page=94),
[Theorem4.3.3/Corollary4.3.4, pp100-101](https://www.jirka.org/ca/ca.pdf#page=100),
[Theorem4.4.2/Proposition4.4.3, pp104-108](https://www.jirka.org/ca/ca.pdf#page=104).
Their smooth parameter-cube, compact convergence and tracked-logarithm
hypotheses were checked in those assessments and specialized in audited
L883. Use its formula directly; no new homotopy or residue proof is
needed. Proposition4.4.3 has an exercise in place of a proof in the
source; retain that recorded qualification. These tools do not sign
the integrals. No Mathlib matching or supporting coverage was checked;
unknown coverage is not absence.

### Local overlap and the remaining application obligations

Read L847's exact full form and angular orientation, L879's hypotheses,
conclusions and finite-arrangement/edge/intrinsic-contact proof ranges,
L880's incident-wedge-to-exact-fiber interface, L882's hypotheses,
conclusions and exact odd-fiber census proof, and L883's hypotheses,
formula, phase test and conjugate limitation. Reuse their accepted
audits, including the just-completed L883 audit; this is no new audit.

L879 (11)-(13) concerns adjacent faces of an auxiliary finite angular
arrangement. Its added circles may contain noncontact points; zeros
can occupy nonisolated subsets. L882's complete odd-fiber census does
not itself classify isolated simultaneous contacts. Thus a future
domainwise argument must explain its face connectivity within each
open cell and every crossed edge, including auxiliary subdivisions,
even contacts and the squared diagonal. It must keep all vertices
and use their established scope rather than delete them or infer a
finite pullback census. A finite auxiliary arrangement is available
in the existing proof; connectedness of the actual nonzero locus is
not an allowed assumption. These are proof obligations, not a claim
that cell signs have now been obtained.

Read the two exact limitation records
`ATTEMPTS/2026-11-07-contact-cell-conjugate-label-limit-57.md` and
`ATTEMPTS/2026-11-07-boundary-fiber-count-only-limit-55.md` and the L883
audit history. Reuse the finite-real-box and retired two-period
comparisons in the ready cell assessment. No signed four-cell test
was found in the scoped 6/7 November contact/cell assessments,
attempts and cell histories. Those stops forbid neither new signs
nor relative invariants; common-line reality and repeating counts
nevertheless supply no answer to this target. No other notebook was
read or used.

### Bounded searches and decision

External queries issued for this comparison:

- `"perfect contours" "zeros" "phase" Lawrence Yamauchi`;
- `"holomorphic" "divisor" "constant phase" "sign"`;
- `"signed" "periods" "calibrated" submanifolds zeros`;
- `"constant phase" "checkerboard" holomorphic`;
- `"radial graph" "contact" "parity" holomorphic`;
- `"perfect contours" "relative" "zeros"`;
- `"contour deformation" "sign" "nodal domains" zeros`;
- `"locally perfect" "multiplicity" zeros`;
- `"constant phase" "relative periods" zeros`.

The relevant primary result was Lawrence-Yamauchi. Search hits for
optics/checkerboards, radial graph embeddings, algebraic multiplicity
and nodal eigenfunctions did not supply matching hypotheses. A scalar
field paper, a later proceedings/review and broader calibration leads
were not read as theorem inputs and are not coverage or novelty
evidence. No unread source is essential to the proposed elementary
assembly of the accepted local inputs. The bounded search found no
adequate import; it does not establish originality or impossibility.

EXPLORE therefore covers one unchanged-target attempt. First justify
whatever domainwise signs actually follow, with strictness justified
where used, then compare conjugate(lambda)*I_pq using the fixed lifts
and full L883 formula. Retain actual lambda when d=0. Do not compute
new zero-free estimates, replace G, assume a product graph or discard
zeros. No such assembly or comparison was performed today.

Continue if this yields a demonstrably nonautomatic necessary
actual-label restriction, even if its universal sign remains open.
Claim exclusion only with a proved incompatible actual-G condition.
Stop this bounded test if every justified condition is automatic or
if a needed propagation premise is unavailable, recording that exact
limitation. Compatible values do not construct a graph. The main
positivity gap, other branches, graph existence, compactness, sharp
period, higher signs and Xi transfer remain unresolved.

Nominate proof_attempt/creative, deep_research/max, after separate
source-scope approval. The new mechanism is contact-parity signs
against full relative periods on the common-line-compatible conjugate
branch; a successful nonautomatic condition could narrow L879's
strict-mass-gap alternative toward L868. The bounded decisive test
and its failure conditions are stated above. This is not a routine
reproof of stationarity, Stokes or the four period formulas.

## Original nomination — retained historical text

### Intended bounded attempt after adequate source coverage

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. The intermediate question is whether phase *signs*,
rather than membership in one line, constrain the conditional
matched-conjugate branch left by L883. A new incompatibility could
remove that boundary mechanism from L879's odd-contact mass gap
toward L868. The unmatched branch, exterior alternatives, graph
existence, compactness, the sharp threshold, higher signs and Xi
transfer remain independent.

The proposed test is restricted to the same four cells. First determine
whether the existing contact-parity argument, with all its hypotheses
checked on these domains, forces a common sign inside each open cell
and how that sign changes across the distinguished fibers. This is a
question, not an assumption of a checkerboard pattern. Other G zeros,
simultaneous contacts and the squared diagonal cannot be deleted to
make a cell connected. Even if an auxiliary angular arrangement has
finitely many faces, that does not assert a finite census of pullback
contacts. The review must distinguish those statements.

Only if sign propagation is justified should the resulting restrictions
be compared with the exact I_pq in L883. Use conjugate(lambda)*I_pq,
and preserve the actual lambda when d=0. Seek a demonstrably
nonautomatic signed condition on the actual labels, or a proof that
the resulting inequalities are compatible and hence fail to exclude
this branch. Real entries alone, the sum of the entries, and the
already known strict qualitative mass gap do not meet that test.
A conditional useful inequality may leave other independent gaps open;
an untested actual-label inequality is not a branch exclusion.

Stop this bounded mechanism if all justified sign conditions are
automatic for the conjugate period data, or if sign propagation needs
an extra premise unavailable under the stated hypotheses. Record the
exact obstruction or additional premise. Do not infer absence of
actual off-real zeros from a failed graph construction, or graph
existence from compatible numbers. No such calculation or sign proof
has been performed during the L883 audit.

## Reuse, duplicate checks and essential missing review

Reuse the inspected Stokes and Laurent inputs in
`2026-11-07-contact-cell-relative-period-test.md` and the completed audit
scope in `2026-11-07-l883-contact-cell-period-conceptual-audit.md` for
L883's formulas only. The accepted contact-parity and boundary-fiber
assessments are `2026-11-06-stationary-graph-phase-components.md` and
`2026-11-06-odd-contact-boundary-fiber-compatibility.md`; their exact
source and proof scope must be compared with this new domainwise
sign claim before importing it. Use narrowly relevant proof ranges
of L879/L880/L882 only when needed. A theorem for a transverse
normal-crossing divisor or analytic u cannot silently replace the
smooth, possibly nonisolated contacts allowed here.

The local search found the recorded limitations, not an already
completed signed four-cell test. Preserve
`ATTEMPTS/2026-11-07-contact-cell-conjugate-label-limit-57.md` and
`ATTEMPTS/2026-11-07-boundary-fiber-count-only-limit-55.md`.
The finite-real-box and two-period stops also retain their different
scopes. Absence of a local matching result is not evidence of novelty.
The next turn must check exact/stronger known statements and relevant
obstructions, retrieve essential primary hypotheses and proof cases,
and decide IMPORT, SPECIALIZE, EXPLORE or a scoped stop. No new lemma
or mathematical script is authorized by this REVIEW_REQUIRED note.

If adequate coverage supports the nonautomatic signed-period mechanism,
nominate proof_attempt/creative, deep_research/max. The precise
obstruction is that every L883 cell value is real for matched conjugate
labels, so common-line compatibility has no exclusion power there;
the bounded test asks whether forced contact-parity signs conflict
with those same full periods. This adds sign information rather than
repeating counts or the total-period identity. Until source scope is
adequate, the exact TARGET routes to literature_comparison/standard/high.
Mathlib coverage is unchecked, with no absence claim.
