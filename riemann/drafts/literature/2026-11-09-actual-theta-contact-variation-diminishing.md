# Actual-theta contact variation diminution: completed source comparison

TARGET: Assess whether a variation-diminishing theorem for the actual tilted theta measure can deduce E[u(log K)'R]>=0 from L874's finite-contact equations for d>=2 and 0<lambda<1/20.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Step183 reused the November5 logarithmic-variation and November6 contact-score comparisons and their recorded stops, inspected L019/L058 and L874 including its audit, and searched exact theta/contact/sign-change terms and stronger Chebyshev-dual terminology; primary passages and queries are recorded below. No matching actual-contact sign theorem was found; no novelty inference follows.
SOURCE_EVIDENCE: Karlin–Novikoff, Pacific J. Math.13(1963),1251–1279, Section3(15)–(20), Theorem1 p1264, LemmasA/B pp1265–1266 and the k=1 example p1266, https://msp.org/pjm/1963/13-4/pjm-v13-n4-p18-s.pdf ; Schoenberg1950 and Choudhury–Yadavv3 coverage reused at its assessed scope.
COMPARISON: Variation diminution alone still supplies only an upper oscillation bound. Karlin–Novikoff supplies a different conditional signed comparison, requiring exact moment orthogonality, minimal sign changes with right-end orientation and comparison-cone membership; these are not supplied by positive density or L874's dilation cancellation. Its k=1 case exposes a concrete one-crossing test for the actual residual.
GAP: No actual-theta residual crossing bound, suitable generalized orthogonality system, comparison-cone membership or contact sign is established. Half-line applicability requires absolute integrability and endpoint/limit checks; initialization, equality/continuation and degree-uniform signs remain open.
REASON: Informative source-scope NEGATIVE: retire automatic variation-diminishing sign import; replace it by a separately nominated, bounded actual degree-two one-crossing test based on the inspected k=1 comparison. This is a new missing-condition test, not a reproof of the contact reduction or a claim of failure of the desired inequality.
LITERATURE_REASON: The saved REVIEW_REQUIRED target lacked theorem-level coverage for the contact residual; the inspected generalized-convex dual criterion adds a specific signed-comparison lead outside the earlier convolution and Stein comparisons.
SCOPE: Completed literature comparison only. No new contact identity, sign inequality, lemma, root computation or mathematical script was produced. The separate next assessment records the proposed mathematical scope and requires its own next-turn approval.

## Original nomination (preserved)

Essential input IDs: L019, L058, L874, L914. Use the canonical L874
definitions of R, the actual tilted expectation and the contact
hypotheses, including H_d positive semidefinite, nonzero c and H_dc=0.
Retain vectors of smaller support; no full-support assumption is granted.
The proposed target has not been derived or approved in step182.

Before source work, search specific local contact-score/sign-change
assessments and recorded failures, including the signed-residual stops;
the narrow date-limited seed search is insufficient. Then retrieve exact
primary theorem hypotheses and essential proof cases before broader
reading. The actual measure cannot be replaced by an arbitrary positive
law; no all-real-zero property or RH-equivalent positivity may be assumed.

Continue only if an inspected theorem supplies a bounded applicability
test or a precise, independently testable missing condition for this
family. Otherwise record the obstruction and abandon this mechanism.
Even a contact-sign result would leave initialization, degree-uniform
continuation and the RH endpoint open. Full/supporting Mathlib coverage
is unchecked. Existing degree-one finite exclusion and all historical
stops remain intact.

## Completed comparison — step183, 9 November 2026

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
The intermediate target was the actual contact score pairing, potentially
useful as a decreasing-parameter boundary sign. The acceptance threshold
was an applicable source condition, not another derivation of L874.

### Duplicates and failures

Read the complete November5 logarithmic-variation assessment, November6
contact-score assessment and their named ATTEMPTS records. Reuse the
former's inspected Schoenberg, Acta Sci. Math.12(1950),97–106, Theorem1
pp98–99, and Choudhury–Yadav arXiv:2307.11822v3, TheoremC/equality case.
Upper oscillation bounds and endpoint signs conditional on count equality
do not supply the present integral sign. Their logarithmic convolution
interface is distinct. No PF/minor sweep or source reproof is justified.
The score assessment's Stein identities and absolute bounds do not sign
this test; GHS cone identification remains unpaid and the later GHS
review stays source-blocked. The contact-polynomial dual discovery's
primary density-operator/pilot comparison was also read: that degree-one
correction is different and its empty-domain pilot is not reopened.

L019/L058 and L874's exact response, score/boundary proof and step11
audit were inspected. Older notes calling L874 unaudited are stale.
L914's audited degree-one exclusion is retained from the supplied
overview. Local searches found no Karlin–Novikoff/generalized-convex
assessment and no matching actual-contact one-crossing test in the
narrow theta/contact records. This is duplicate triage, not originality.

### Primary theorem conditions and proof cases

S. Karlin and A. Novikoff, *Generalized convex inequalities*,
Pacific J. Math.13(1963),1251–1279,
[Section3, pp1262–1266](https://msp.org/pjm/1963/13-4/pjm-v13-n4-p18-s.pdf).
The setup uses positive C^k weights on a finite interval and their
iterated-integral Chebyshev system. Theorem1, p1264, requires all k
moment cancellations and nonnegativity of the paper's iterated
integral; its integration-by-parts proof gives sufficiency, and arbitrary
positive continuous differential images give necessity. LemmaA, p1265,
requires a continuous nonnull density orthogonal to the system.
LemmaB, pp1265–1266, adds exactly k strict sign changes and nonnegative
nonnull right-end sign. Both its determinant-interpolation and repeated-
integration proofs retain the count and orientation. The k=1, psi1=1
example on p1266 concerns increasing comparison functions: zero mass
and one crossing from negative to positive suffice. Section3 p1263
leaves infinite-interval modifications to the reader; no unqualified
half-line extension is imported here.

Read extracted primary text of (15)–(20), the moment lemma, Theorem1's
two directions, LemmasA/B with both B proof cases and the k=1 example.
Some determinant displays extract poorly; screenshot calls supplied no
viewable image. No unread high-order coefficient display is an input.
The k=1 increasing-function example and its orientation are legible.
Shell PDF download failed DNS; primary web text was accessible, so the
limited comparison is not source-blocked. Broader generalizations are
unused leads. No original theorem is imported as an established contact
inequality and no reproof is performed.

### Applicability and route

A prospective k=1 application would compare -R rho_lambda against u^2,
using L874's existing zero mean, where rho_lambda is its exact density.
Its missing crossing premise is that R changes from positive to negative
exactly once on the whole positive half-line. This would target L874's
existing polynomial-flux expression, avoiding an additional score-shape
premise. This is an applicability proposal, not a proved specialization
or residual bound; return to the score requires lambda>0 as in L874.

L874 proves both signs and a negative tail, not a crossing bound.
E[u R']=0 is a dilation cancellation, not orthogonality against a second
specified Chebyshev test. No suitable k-moment system, minimal oscillation
or score-cone membership follows from the inspected sources. Truncating
the measure changes its zero mass: future half-line use must justify
the limit with L874's integrability/endpoints or explicitly reproduce the
integrable one-crossing specialization. No such application occurred.

Retire automatic variation-diminishing sign import. The new source does
supply a concrete missing-condition test, separately nominated in
`drafts/literature/2026-11-09-actual-theta-degree-two-one-crossing.md`.
Continue only on an actual conditional crossing bound, a relevant
structural obstruction or a precise independently testable theta premise.
No contact is asserted; an empty domain is not a new boundary mechanism.
This is a source-scope NEGATIVE with a changed test, not a mathematical
counterexample or progress beyond the literature checked.

Queries included `variation diminishing signed measure single crossing
integral Chebyshev system theorem Ohlin lemma`, `Riemann theta kernel
heat Hankel contact polynomial variation diminishing score sign`,
`sign changes Chebyshev system orthogonal theorem integral polynomial`,
`Karlin Novikoff generalized convex crossing theorem pdf`, and exact
theta/contact/polynomial/sign-change and Hankel/contact/single-crossing
variants. Exact PDF display searches returned unrelated results, unused.
Ohlin, orthogonal-function and Toda/theta-kernel search leads were not
inspected theorem inputs. No exhaustive search or novelty claim is made.
No mathematical scripts or lemmas were written. Full/supporting Mathlib
coverage is unchecked. Initialization, tangency, continuation, all-degree
signs and RH remain open.
