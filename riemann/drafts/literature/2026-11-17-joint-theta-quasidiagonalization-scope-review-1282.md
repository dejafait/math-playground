# Joint theta quasi-diagonalization — completed source comparison1283

TARGET: Assess whether Yafaev's Hankel quasi-diagonalization supplies a common-domain representation of C032f's B*B-d^2 A*A retaining both theta branches and the intermediate transform metric, or only separate inertia statements.
CHECKED: 2026-11-17
DECISION: IMPORT
SEARCH_EVIDENCE: Completed1283 reused review1270 and the 7November separate-inertia comparison; searched Yafaev Hankel quasi-diagonalization bounded-operator/product terminology and read the primary factorization and bounded-extension cases below. No inspected theorem decides the fixed theta relative bound; no novelty inference.
SOURCE_EVIDENCE: Yafaev, Analysis&PDE8(2015),183-221, DOI10.2140/apde.2015.8.183, https://msp.org/apde/2015/8-1/apde-v8-n1-p05-s.pdf, Sections2.1-2.2 pp189-193, Section3.3-3.4 pp199-201, Theorems2.6/3.8, Lemma3.10, Proposition3.11 and Section4.1 p202; Yafaev arXiv1403.3941v1, https://arxiv.org/pdf/1403.3941, Corollary4.2/Theorem4.3 and proof pp13-14 with (2.11); Yafaev arXiv1801.00706v1, https://arxiv.org/html/1801.00706v1#S2, Theorems2.1/2.3, Lemma2.2 and factorization (2.5)-(2.7). Douglas1966 coverage is reused, not retrieved again.
COMPARISON: The source gives a common bounded-form representation, not merely individual inertia. Its general extension maps a weighted space to its dual; the explicit L2 multiplier theorem additionally assumes a bounded sigma-function. Neither supplies the paired squared-output inequality or permission to omit the intermediate metric. Park automatic scalar-sign transfer, not all transform methods.
GAP: Delta, actual adjoint-range inclusion, four theta sign-functions and their product-domain/norm comparison remain unresolved. Bounded theta Hankel operators do not by themselves verify the bounded-sigma hypothesis. No actual-Xi source metric or signing bridge is supplied.
REASON: IMPORT covers the inspected theorem scopes and the negative applicability comparison only. It does not approve an original product formula or another delta witness attempt. The new evidence closes the proposed automatic quasi-diagonalization shortcut while preserving the general common-form representation.
LITERATURE_REASON: The exact joint-product/transform-metric question was outside the ready Douglas/core audit and earlier individual-inertia comparisons. This single source review fills that scope gap; unchanged coverage was reused.
SCOPE: Completed literature-only1283. Fixed full Psi, omega=1/4, z=i,c, complex unweighted H,Y and A,B of C032f(1)-(5); one input and both branches. No theta specialization of a new identity, kernel truncation, delta decision, lemma/script write or actual-Xi signing assertion.

## Completed source comparison1283

The answer has two parts: there is more than separate inertia, but the
inspected results do not turn the relative squared-output problem into
pointwise symbol signs. The continuation test for that shortcut fails.
This is a source-scope negative, not a proof of either value of delta.

### Primary statements and essential cases actually inspected

**Published 2015 paper.** Theorem2.6 and Corollary2.7, p193, represent
Hankel forms for kernels in Z'_+ on D=U^{-1}Z. Here Z is the entire
Paley-Wiener test space, not the notebook's compact smooth D. Read
Lemma2.1's complete convolution/gamma proof, Definitions2.3-2.4 and
the derivation of Theorem2.6. Section3.4, Lemma3.10/Proposition3.11,
pp200-201, extend bounded forms to all original L2 inputs by density
in the weighted spaces E and W=Phi*E. In source notation:

    Delta f(x)=Gamma(1/2+ix) M f(x),
    ||g||_E=||K g||_2,  K(x)=sqrt(cosh(pi x)/pi).

Delta:L2->E and Phi*Delta:L2->W are unitary with these norms.
The convolution and sign operators act E->E' and W->W', respectively;
they are not asserted to be unweighted L2 multipliers. Theorem3.8,
p199, covers bounded Hankel kernels. Theorem4.1, p202, compares
individual form inertias. These statements do not compare squared
output norms. [Publisher PDF](https://msp.org/apde/2015/8-1/apde-v8-n1-p05-s.pdf).

**2014 preprint, distinct from the published source above.** In
arXiv1403.3941v1, Corollary4.2 and its preceding Mellin calculation,
pp13-14, factor the Laplace transform on L2; the inverse gamma factor
grows exponentially. Theorem4.3 assumes (2.11), support of sigma in
[0,infinity), and (4.8), sigma in L-infinity on the positive axis.
Read those hypotheses and the entire short proof through (4.11).
The common transform is a Mellin transform with a gamma phase;
its universal weight is v(x)=sqrt(pi/cosh(pi x)). The represented
operator is V Phi S Phi* V, with V multiplication by v. The weight
is retained: this is not unitary equivalence to S alone. Polynomial
sign-functions are mentioned as additional cases, not a theorem
covering arbitrary theta distributions. [Primary v1 PDF](https://arxiv.org/pdf/1403.3941).

**2018 author exposition.** arXiv1801.00706v1, Section2.1-2.2,
Theorem2.1 states a form identity on compact smooth inputs with
sigma in the dual Laplace-image test space. Lemma2.2 factors the
Laplace transform for all L2 inputs. The explicit common unitary
transform is given before (2.6), and (2.7) retains v on both sides
of s(D). Theorem2.3 assumes sigma in L-infinity on the positive
axis. Read the definitions, theorem statements and full intervening
factorization argument, rather than relying on the introductory
claim of arbitrary-kernel unitary equivalence. It does not eliminate
the weights or state a comparison theorem for two adjoint products.
[Primary v1 Section2](https://arxiv.org/html/1801.00706v1#S2).

### Applicability to the saved local question

C032f(1)-(5) supplies four scalar bounded Hankel components inside two
maps H->Y. This is the relevant already-proved hypothesis for the
published bounded-form extension. Thus rejecting all common-domain
coverage as merely an individual-inertia result would be inaccurate.
There is a source-defined common weighted test-space framework.
The source's unitary maps into E/W use their weighted norms. Their
duals cannot be replaced by the original unweighted output L2 space.
No general theta product identity is derived in this review.

The two sigma branches of C032f are output labels, unrelated to
Yafaev's notation sigma for an inverse-Laplace distribution. Each
of the four kernels would need its own sign distribution. Both
components of either local map must continue to use the same input.
Nothing licenses optimizing them separately or replacing the summed
Y-norm by two unrelated form-sign decisions.

The scalar C032e convention c and its full-theta kernel are unchanged.
No bounded inverse-Laplace density for any of the four kernels has
been verified. Smoothness, rapid decay and the existing boundedness
proof are not a verification of that additional source hypothesis.
Consequently Theorem4.3/2014 or Theorem2.3/2018 cannot simply be
imported as an unweighted multiplication formula for these kernels.

Even their bounded-symbol case retains V. The sources expressly
display the nonconstant intermediate weight; the local question asks
for a relative norm estimate, not the sign of an individual form.
An application would still have to justify composition domains or
the weighted-dual Riesz identification and prove the relative estimate
with that metric present. Neither the individual inertia theorem nor
boundedness provides it. We have not proved that no such application
can work, only that these inspected theorems do not pay that obligation.

No scalar sign criterion, positive d, zero-defect sequence, actual
range inclusion or source-norm identification has been obtained.
The main gap remains all-degree actual-Xi Q>=0 in L030-L032/C032a;
even a delta verdict would leave transport, signing, initialization,
singular Schur cases and the all-degree bridge open. Mathlib coverage
of the joint representation was not checked; no absence is claimed.

### Duplicates, access and route decision

Reuse review1270's Douglas coverage and the 7November individual-index
comparison; those statements were adequate and are not reproved.
The new read fills exactly the common-form/bounded-extension scope
omitted there. Preserve stops1266/1268/1272/1273/1276/1278 and the
31October stop. No pointwise ratio, corona shortcut or boundary-cloud
family is restarted. No novelty follows from the unsuccessful exact
product search.

Queries used were `Yafaev Hankel quasi diagonalization H L* Sigma L
sigma bounded operators products` and `"Hankel operators"
"quasi-diagonalization" "products"`. Primary sources were inspected
at theorem level before their proof passages. The 2018 exposition's
broader introductory language was checked against Theorem2.3's actual
hypothesis. Neither localization search hits nor abstracts are theorem
inputs. A shell PDF download failed DNS; web PDF text/primary HTML
were accessible. Screenshot calls did not expose readable page images
in this wrapper. No disputed OCR sign or constant supports a new
calculation; formulas agree with the readable primary HTML. This is
not an essential source-access blocker.

Park the automatic quasi-diagonalization-to-relative-sign shortcut.
A different bounded source nomination is recorded separately in
`2026-11-17-common-differential-commutant-scope-nomination-1283.md`:
check a common differential commutant, rather than suppressing the
transform metric. It is an unread source lead and unapproved test,
not a mathematical result or a renewed witness budget. Exact local
commutator/Sturm-Liouville searches in drafts/literature, ATTEMPTS and
foundations located no matching assessment; this does not establish
novelty. There is still no independently signed actual-Xi interface,
so no central creative proof attempt is justified by this review.

## Original nomination1282 — retained scope and discriminator

## Exact review discriminator

The completed audit1282 accepts C032f(1)-(5); it does not decide the
range inclusion. The proposed new intermediate target is a correct
common-domain description of the squared-output pencil, if the cited
source machinery permits one. This nomination contains no derivation
and does not approve that mathematical target.

Read primary factorization statements, their test spaces and the
essential extension cases. First determine whether they give operator
identities in the original unweighted L2 spaces or only identities of
quadratic forms on a smaller core. Identify any nonunitary transform,
unbounded inverse, distributional sign function and intermediate
metric. A congruence for an individual Hankel form cannot simply be
squared as if it were a unitary equivalence. Both output components
must still arise from the same h. Any scalar criterion must be justified
for the full product, not inferred from the signs of individual symbols.

Continue to a separately covered mathematical application only if the
review identifies a precise theorem and a checkable applicability plan
that retains these features. If only separate inertia is covered, or
an essential uncontrolled metric recreates the same relative-bound gap,
record that scope limit and park this shortcut. An inaccessible essential
source is SOURCE_BLOCKED, not a mathematical negative; repeated access
attempts must not become a new campaign. No finite fit substitutes for
the required identity or norm control.

## Existing evidence to reuse

Review1270 explicitly left Yafaev's quasi-diagonalization as an unread
lead for this normalized pair. The bounded/core reduction is now
audited in C032f; its Douglas citation remains sufficient for that
reduction and requires no repeat browsing. C032e's exact compact
uniqueness does not decide the quantitative threshold.

The inspected passage in
`2026-11-07-actual-xi-finite-negative-index-discovery.md`, Section2,
records continuous Hankel form hypotheses and a compact perturbation
with infinite negative index. Preserve that obstruction; compactness
alone is not the proposed input. Its individual-form analysis does
not settle this paired product. The rational finite-rank and Carleman
comparisons located by the local search concern other operators and
are not automatically transferable. This bounded search establishes
neither novelty nor absence of other relevant assessments.

Preserve stops1272/1273/1276/1278. In particular do not repeat a
pointwise ratio test, scalar cancellation, a bounded-corona inference
or the fixed boundary-cloud witness family. Their failures do not ban
a different justified transform mechanism, but this nomination by
itself supplies no such justification. C032g is a contrast, not a
mathematical input to the proposed factorization.

## Relevance, unresolved assumptions and routing

The main gap remains all-degree actual-Xi Q>=0 in L030-L032/C032a.
A sound product representation could test the normalized compatibility
diagnostic used to assess a possible branch transport. It would still
leave the source metric, completed transport and any signing bridge
unpaid; it would not itself imply an RH result. Essential local inputs
are C032f(1)-(5) and C032e's full-kernel bounds and scalar conventions.
L016-L020 are used only through their relevant recorded inputs; do not
load unrelated proofs. The conditional H_(d-1)>0, singular Schur cases,
initialization and all degrees remain independent unresolved issues.

No independently signed actual-Xi interface has emerged from the
score/Jacobi/nonlocal/Grunsky/modular comparisons cited in history1280
and review1274. Thus no justified central creative target is ready.
This narrower new source question is not relabeled creative to meet
a scheduling preference, and does not renew the exhausted witness
family. Recommend literature_comparison, standard/high: the useful
result is a precise operator-versus-form scope decision, not another
audit of C032f or approval of the same Douglas coverage. Mathematical
application, if justified, requires a subsequent ready assessment.
No Mathlib coverage of this proposed joint representation has been
checked. No cross-notebook input or complete candidate is proposed.
