# Corollary 2.2 compact-family occurrence — completed source comparison

TARGET: Determine whether L086's fixed congruence family has infinitely many distinct degree-at-most-six Legendre parameters in one compactly bounded set satisfying Corollary 2.2's 2-adic j condition, while retaining full mod-120 and mod-seven images.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step351 searched compactly bounded Legendre occurrence, congruence-family maximal images and distinct-j counting; inspected GenEll's definition, IV's open-domain correction, Silverman's invariant/Legendre statements and essential proof cases, Milne's local compactness proposition, and Wada's competing theorem scope. Reused step338's fixed-level assessment and checked L086 plus ATTEMPTS/033–034; queries and comparison below.
SOURCE_EVIDENCE: Mochizuki, Arithmetic Elliptic Curves in General Position, Math. J. Okayama Univ. 52 (2010), Example 1.3(i),(ii), pp.5–6; qualified April 2020 IUT IV reproduction, Remark 2.3.1(vi), p.56; Silverman AEC 2nd ed. (2009), III.1 p.45 and Proposition 1.7/proof pp.49–50; Milne ANT v3.08 (2020), Proposition 7.46/proof and Corollary 7.47 p.126; Wada December-2016-linked 29-page manuscript, Definition 1.6 p.5, Theorems 2.1/2.7 pp.6/8 and Lemma 2.3 p.7. Reuse step338 Zywina Proposition 5.7/full proof and composite-level cases without new browsing.
COMPARISON: Known sources supply exact conjugate/domain conditions, the degree-six Legendre map, local compactness and whole-box fixed-level exceptions. Their combination still needs the specific constrained-lattice count, uniform bounds and distinct-moduli argument. Wada's rational-parameter Frey equations do not provide the fixed family or its maximal mod-120 image; no exact matching theorem was imported.
GAP: Source coverage is ready for one bounded known-method specialization, but existence of the common domains and infinite distinct admissible subfamily is unproved. Later-member native field applicability, choices, independent initial data, essentiality and original finite B>=A remain open.
REASON: Newly inspected primary definitions resolve the essential local-domain coverage gap; the remaining work is an explicit application of known formulas, elementary topology/counting and the already assessed occurrence estimate, not a general-theorem reproof.
SCOPE: Exactly TARGET with c,h,d_*,e_* fixed as in L086. Approve a later proof attempt using a fixed parity refinement and positive-area short-coefficient rectangles, bounded-j inverse-image domains at infinity and 2, a same-family union bound and a distinct-j/degree test. Check all conjugates and every finite local extension. No changed constants, uniformity in h, effective coefficients, new field theorem, transfer of L087–L088 to later members or original IUT counterexample is covered.
LITERATURE_REASON: GenEll's exact domains, IV's open-subscheme correction and the constrained distinct-parameter scope were essential and outside step338's ready unconstrained occurrence assessment.

## Completed comparison — step351

The main gap remains original finite B>=A. The intermediate target is
TARGET. If proved, it could allow avoidance of a fixed finite Exc_d
for a single K_V and make the fixed-F construction obligation from
step350 testable. It does not resolve any independent applicability
or essentiality gap. Continue the proposed mechanism only with a
positive constrained count dominating the two exceptional bounds and
infinitely many distinct parameters; abandon it upon boundary approach,
unbounded 2-adic j, incompatible images or finite moduli.

### Primary definitions and theorem coverage

[Mochizuki, GenEll](https://www.math.okayama-u.ac.jp/mjou/mjou52/_01_mochizuki.pdf),
Example 1.3(i),(ii), printed pp.5–6, was read in full. A compact domain
is compact and the closure of its interior. The finite support contains
infinity. Its archimedean domain is nonempty, proper and conjugation
stable. A finite-place domain is a nonempty proper local-Galois-stable
subset of X(Qbar_v) whose intersection with X(K) is a compact domain
for every finite K/Q_v. All conjugate images of a global point must
lie in the domains. This does not assert compactness of Qbar_v.

[IUT IV April 2020 reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
Remark 2.3.1(vi), printed p.56, was read completely: the bounding
domains must themselves lie in the open U, here excluding 0,1,infinity.
Reuse step350 for Corollary 2.2, its 2-adic j bound and fixed-F proof.
Retain the reproduction/journal-identity qualifications in that record;
no authenticated journal-version comparison was obtained here.

[Silverman, AEC, second edition (2009)](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf),
III.1 p.45, gives the short-model discriminant and invariant formulas
in characteristic different from 2,3. III Proposition 1.7(a)–(c),
pp.49–50, gives geometric Legendre representation, its rational
j-formula and six-element generic fibers, with the special fibers at
0 and 1728. Read its whole proof: root differences and the square-root
coordinate change, six root permutations and the exceptional collisions.
Import these results rather than reprove them. The geometric scope
does not promise an isomorphism over Q(t); the next application must
justify the degree bound and all conjugate bounds for its actual t.

[Milne, ANT v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Proposition 7.46 and Corollary 7.47, printed p.126, were read with
proofs. The integer ring of a complete discretely valued field is
compact exactly when its residue field is finite; the displayed ideal
and unit subsets are compact. Use this as supporting local topology.
The particular inverse-image domains still require their own
closedness, interior, nonemptiness and cusp-exclusion checks.

Reuse `drafts/literature/2026-10-19-auxiliary-full-mod120-occurrence.md`
for Zywina's exact fixed-m theorem, determinant criterion and all
composite-level proof cases. L086's displayed coordinate lattice and
bounds were read. The source theorem bounds the whole box, so no new
sector-equidistribution or probabilistic independence theorem is
needed in the proposed application. No such application is proved here.

### Exact missing specialization and bounded test

A concrete proposed test is to retain the existing integral short
coordinates (A,B), restrict to R/2<=A<=R and |B|<=R, and impose B odd.
Proposed domains are inverse images under the cited Legendre j-map of
a fixed closed complex disk (test radius 2000) and O_(Qbar_2), with
support {infinity,2}. These are proposals for the next research turn,
not derived bounds or approved existence claims in this literature turn.
The original c,h,d_*,e_* stay fixed; only u,v may be restricted.

The later proof must check parity compatibility in the actual affine
lattice, a positive quadratic rectangle count with boundary errors,
and dominance over the existing O(R^(3/2) log R) exceptional bounds.
It must verify the invariant bounds on every counted curve, the domain
conditions in every finite extension, the degree-at-most-six bound on
actual ordered-root parameters, and infinitely many distinct j-values
or another rigorous finite-fiber argument. Repeated equations and
quadratic twists cannot be counted as new parameters without proof.
A fixed finite collection of j-fibers must be shown too small for the
surviving count. Exceptional j=0,1728 and singular models must be
handled from actual hypotheses, not silently dropped. No extra
unassessed occurrence theorem or new mathematical script is needed.

This specificity identifies what must be proved without carrying out
the proof and approving it in the same turn. If these proposals fail,
record the precise failure before replacing the mechanism. The
threshold is infinitely many distinct allowed parameters in one fixed
K_V, retaining both full images; one selected curve is insufficient.

### Stronger-result search, overlaps and recorded stops

Queries included `Mochizuki GenEll "Example 1.3" compact`,
`"Legendre" "congruence" "compact" "Galois" elliptic curves Zywina`,
`"elliptic curves" "congruence conditions" "Zywina" "density"`,
`"elliptic curves" "distinct j-invariants" "box" Galois local conditions`,
and `"compactly bounded" "Legendre" parameters`.

The relevant new primary lead was [Yuki Wada, Near Miss abc-Triples
in Compactly Bounded Subsets](https://www.kurims.kyoto-u.ac.jp/~motizuki/2016-12-27%20Near%20miss%20abc-triples%20in%20compactly%20bounded%20subsets.pdf),
the 29-page manuscript at the December-2016-named URL. Inspected
Definition 1.6 p.5, Theorem 2.1 p.6, Lemma 2.3/proof p.7 and
Theorem 2.7 p.8. It supplies compact occurrence for rational abc
parameters and Frey equations with three rational displayed roots.
It asserts neither membership in L086's fixed coefficient family nor
its maximal torsion images. This is an inspected scope mismatch,
not a new obstruction theorem. Its long analytic proof is unread and
unneeded here because the theorem's own scope already fails to supply
the required input. No near-miss estimate is imported. Other search
leads, including newer effective-IUT estimates and image surveys,
were not inspected as theorem inputs and are not coverage or novelty
evidence. The unrelated Sutherland Lecture 2 file supplied no needed
invariant statement; Silverman's primary statement supplies it.

The narrow local search found no prior compact-family proof in the
relevant occurrence/field assessments. ATTEMPTS/033's unnecessary
classification retrieval and ATTEMPTS/034's cyclic Frobenius stop
remain intact. Neither is reopened; this target tests a constrained
count and compactness, not those exhausted separators. L087 and L088
remain single-member results. All their later-member applications,
alternate choices/field repairs, independent initial-data clauses,
source-marked input/action/factorization/pilot transport, essentiality
and finite B>=A are unresolved. Prime seven is retained only as an
existing family condition, not as the corollary's height-selected ell.

The official [7 July 2023 announcement](https://zen.ac.jp/news/0ul6zqed9-0)
and [current prize page](https://zen.ac.jp/en/lp/icp) were rechecked;
the target remains an essential inherent flaw and adjudication remains
separate. No source version change affecting this route was found.
Full matching and supporting Mathlib coverage for the constrained
occurrence is unchecked; no absence claim is made. The ready next
mathematical classification is REPRODUCTION. This completed step is
KNOWN_IMPORTED source clarification, not mathematical progress beyond
the sources. No lemma, script, PROOF or DAG change was made.

## Invocation-start proposal — historical, gate status superseded above

The main gap remains original finite B>=A. This intermediate target
could permit selection outside every fixed finite Exc_d for one common
K_V, thereby making the fixed-F construction obligation testable.
It is not itself a counterexample or proof of essentiality. Degree six
is a proposed threshold for the Legendre parameter, not a proved bound
for an infinite selected subfamily and not a degree bound on F.

Keep L086's original fixed c,h,d_*,e_* and two-parameter family. A
subfamily may restrict its integer parameters but must not silently
reselect old witnesses, change those constants or transfer L087/L088's
fixed-member conclusions to every new member. Exact local inputs are
audited L086, L087 and L088, with the completed step350 source comparison.
The generic field/stabilizer methods have ready source coverage, but
their application to any newly selected member remains separate.

First inspect GenEll's precise definition, including its Galois and
local-domain conventions and IV's open-subscheme correction. Then
compare the proposed constrained occurrence with the already inspected
fixed-level exceptional theorem. Search for the exact statement,
standard terminology, stronger approximation/occurrence results and
known obstructions; a theorem citation must retain its hypotheses.
Reuse the existing Zywina assessment unless that comparison leaves
its scope. Do not repeat composite-level browsing to fill a quota.

The discriminating test is whether a specified subfamily can support
infinitely many distinct allowed parameters and dominate the two
whole-box exceptional counts with all moduli fixed. A finite-parameter
family, boundary degeneration, loss of uniform 2-adic j boundedness or
an incompatible image condition stops that proposed mechanism. This
assessment does not assert any of these outcomes. Finitely many
excluded parameter values must not be confused with finitely many
integral equations or with a new singleton K_V for each equation.

Do not fix the corollary's auxiliary prime to seven: its (C1) selects
ell from height. Retaining mod-seven image here preserves the existing
family conditions only. Choice quantifiers, extension of the native
field screen to later selected members, any alternate-field repair,
all independent initial data and essentiality remain unresolved even
if the proposed compact-family target succeeds. No original numerical
comparison, old-witness verdict or all-choice obstruction follows.
ATTEMPTS/033–034 remain preserved. Full matching and supporting Mathlib
coverage is unchecked. No lemma or script is authorized before a
separate assessment turn approves this target.

## Step351 interim working record — superseded by completion above

Inspected GenEll Example 1.3(i),(ii), printed pp.5–6, and IV
Remark 2.3.1(vi), p.56, using the qualified April 2020 reproduction.
The finite-place requirement is compact-domain intersection in every
finite local extension, with local Galois stability; every conjugate
must satisfy each bound. The domains themselves must avoid the deleted
points. This is not literal compactness of all of Qbar_2.
Reuse step338's full composite-level coverage rather than rebrowse it.
A newly found Wada compact-occurrence lead has been inspected at its
definition and theorem statements, but is not imported as an answer
to the fixed-family/full-image target. No constrained count, new lemma
or mathematical script has been derived or written. Final assessment
decision and exact approved specialization scope remain to be recorded.
