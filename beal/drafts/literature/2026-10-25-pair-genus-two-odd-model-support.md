# Pair genus-two odd model and support — source approval

TARGET: Construct and certify an integral monic odd-degree model of L110's genus-two curve, identify its quartic factor field with L133, and determine sufficient two-descent support compatible with L137.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused both named startup assessments; checked L110, L133–L134, L137, ATTEMPTS/045,050,059–060 and the 2026-10-20 pair-rank-lower record. Found the existing monic quintic and inverse maps in rank-lower-certificate.json /model. Searched exact quintic coefficients, rational-Weierstrass normalization, Stoll Corollary 4.7 and Jacobian S-support terminology; no inspected external instance certificate was identified.
SOURCE_EVIDENCE: Directly read Stoll, Acta Arith. 98 (2001), Sections 2–4, pp.246–250, Proposition 4.6 with both discriminant cases and its proof p.252, Corollary 4.7 and factor-product instruction p.253; reused the prior rank assessment's Lemmas 4.9–4.10 and the approved Claborn/Clark localization and Stacks 00DF coverage in 2026-10-25-pair-quartic-localized-parity.md.
COMPARISON: General monic odd-degree normalization and sufficient Jacobian support are known. The local rank-lower attempt already constructed the required quintic, so reuse its complete saved model rather than repeat discovery or point searches. Its quartic-factor identification with L133 and all-prime support certificate remain missing. L137 is a partial class bound, not a Selmer computation.
GAP: Independently certify the saved model and proper inverse maps, transport its quartic factor into the actual L133 field, certify a sufficient finite support, and justify transporting L137 through any further localization. No class/unit completion, local-image enumeration or rank computation is covered.
REASON: Essential theorem coverage now approves this unchanged model/support target. The duplicate check changes execution to reuse plus certification of existing model data, followed by the missing field/support specialization; the exhausted relation and point-search routes stay stopped.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED because its normalization and Jacobian support hypotheses were unapproved; the octic assessment concerns a different curve-point descent. This separate review supplies those missing hypotheses and checks earlier model overlap.
SCOPE: Exactly TARGET for L110 over Q with its original twist and functions, using the existing rank-lower model data and L133–L137. Fixed exact polynomial/field-map/discriminant certificates and support theorem application only; no new model search, relation box, backend probe, unit basis, complete descent, rank or point calculation.

## Gap, intermediate target and downstream use

The main gap remains exclusion of positive primitive solutions in the
infinite residual Beal family. For the pair-image route, a certified
Jacobian descent and rational/integer recovery are still absent. This
intermediate target prepares a precise descent interface on the actual
genus-two quotient; it does not attempt the whole descent.

Use L110's exact W²=11(T²−4)Q4(T), including its constant twist, and
L133's field with alpha=25theta. Audited L134–L137 supply maximal-order
arithmetic, class generators, partial relations and a localized upper
bound. A future rank upper bound could use these inputs only after the
curve's actual descent algebra and sufficient support are identified.
Even successful preparation leaves units or a valid bound avoiding unit
generators, global/local descent completeness, rank, points, marked lifts,
degree-nine and integer recovery, both L095 systems and other signatures
unresolved. No rank threshold is claimed achieved by this review.

## Reusable primary results and exact conventions

Michael Stoll, *Implementing 2-descent for Jacobians of hyperelliptic
curves*, [Acta Arithmetica 98 (2001), 245–277](https://www.impan.pl/shop/en/publication/transaction/download/product/83397),
DOI 10.4064/aa98-3-4; publisher's 33-page PDF, accessed 2026-10-25.
Section 4, p.249, permits monic integral odd-degree normalization when
there is a rational Weierstrass point. Lemma 4.1 and Proposition 4.2,
p.250, use the norm kernel in L*/L*² for L=Q[X]/(F); there is no scalar
quotient. Section 2, p.247, uses maximal integer rings in every field
factor. Proposition 4.6, p.252, makes the odd-prime local image the kernel
of valuation when p² does not divide disc(F). Its proof separately treats
good reduction and discriminant valuation one via the component group.
Corollary 4.7, p.253, therefore gives support
S0={infinity,2} union {p:p² divides disc(F)}. The same page explicitly
allows computing disc(F) from factor discriminants and resultants.
These results are imported; no reproof is needed. A larger finite S is
allowed for containment; it need not be minimal or give complete local
images. The prior rank assessment's Lemmas 4.9–4.10 retain class data
even when explicit unit generators are avoided.

The existing
`drafts/literature/2026-10-20-pair-jacobian-rank-bound.md` is reused for
the rank inequality, full global-arithmetic qualifications and backend
failure. The primary passages above supply the exact support comparison.
`drafts/literature/2026-10-21-marked-octic-two-cover-support.md` concerns
L113 and Bruin–Stoll's curve-point fake descent. Its even-degree scalar
quotient and infinity rows must not be substituted for this Jacobian map.
An upper bound on a supported ambient group alone is not a Selmer or
Mordell–Weil rank computation.

For enlarging support, reuse the inspected primary statements and proofs
in `drafts/literature/2026-10-25-pair-quartic-localized-parity.md`:
Claborn, [Pacific J. Math. 15 (1965), Corollary 1.4 and Proposition 1.5,
p.800](https://msp.org/pjm/1965/15-3/pjm-v15-n3-p06-p.pdf), and Clark,
[Enseign. Math. 55 (2009), Theorem 5 and proof, pp.217–218](https://ems.press/content/serial-article-files/44188).
Ideal extension to a Dedekind overring is surjective on ordinary class
groups, with kernel generated by primes becoming units. This covers
successive localizations, not just the originally tested seven primes.
[Stacks Lemma 10.12.10, tag 00DF](https://stacks.math.columbia.edu/tag/00DF)
supplies right exactness after tensoring with F_2. The future application
must explicitly bind O[1/330] to the transported field and its further
localization; this approves use of these known statements, not a new
localized dimension calculation. L136's prior finite-abelian coverage
is reusable if comparing a finite class group's mod-two quotient with
its two-torsion dimension. Do not assert a map on two-torsion is
surjective merely because the underlying class-group map is surjective.

## Duplicate discovery and recorded failures

The startup proposal overlooked a completed prerequisite. The full
`drafts/2026-10-20-pair-rank-lower-attempt.md` already records a quintic,
its forward/inverse maps and the proper-curve extension argument. The
complete selected `/model` in `scripts/pair-genus-two/rank-lower-certificate.json`
was read with the shared JSON inspector's --full option. It records
c=−36300, X=c/(T−2), Y=c²W/(T−2)³ and inverse
T=2+c/X, W=cY/X³, together with the six integer quintic coefficients.
The producer's model-only coefficient and gcd checks were inspected,
without running it. This is existing evidence, not a freshly verified
model, and the independent search replay does not audit these model
checks. Reuse the complete saved polynomial and recheck this small
interface independently; do not repeat its large search.

ATTEMPTS/050 parks that point/divisor detector after zero eligible
columns, not the underlying quintic. ATTEMPTS/045 concerns an unavailable
complete class backend for another field. ATTEMPTS/059–060 stop the
fixed relation box and the rank-30 augmentation; they do not prohibit
this separate field/support test. No enlarged box, renewed backend
preflight or new rank-lower search is approved. Unfinished L108 and all
initial schema/accounting failures remain preserved.

Queries included `"76835" "2196150000" curve`,
`hyperelliptic curve rational Weierstrass point monic odd degree model
change variables leading coefficient Stoll`,
`"Implementing 2-descent" "4.7" discriminant`, and
`hyperelliptic Jacobian 2 descent S class group localization support
monic odd degree`. The exact-coefficient query supplied no inspected
instance theorem. The inspected numbered Stoll results suffice for
method coverage; no novelty follows from missing search matches.
Search leads on other curve families and implementations were not used
as theorem inputs. No cross-notebook mathematical input is used.

## Approved bounded continuation and decision test

In one research step, reuse the saved quintic rather than discover a
different model. Independently certify its entire coefficient identity,
squarefreeness, integral monic degree five, both inverse compositions
and proper exceptional-point interpretation. Preserve L110's twist
and original s,z functions. Reuse L110's already approved smooth-proper
extension input (Stacks Theorem 53.2.6, tag 0BY1) with its hypotheses.

Factor the quintic exactly into its rational linear and quartic parts;
transport the quartic root using the saved coordinate substitution and
L133's alpha=25theta. Certify both defining relations, inverse generator
compositions and complete power-basis maps. Equal degree, discriminant
or abstract isomorphism without those maps does not bind the descent
coordinate to the audited field and maximal order.

Compute and independently verify the exact quintic discriminant, or its
complete factor-discriminant/resultant certificate. Certify every asserted
rational-prime factor and the absence of an omitted cofactor. Choose a
finite S containing S0, infinity and every rational prime in {2,3,5,11};
all places above its finite primes in every algebra factor are intended.
Extra primes caused by integral normalization may be retained. A field
discriminant alone cannot replace the polynomial discriminant test.
Use the imported localization and tensor statements to justify precisely
how L137 remains an upper-bound input after any further localization.
No improvement below two, equality with two or full class presentation
is assumed. No unit or local-image computation is required for this step.

The scope is one fixed model and one quartic-field identification, with
exact polynomial/linear algebra and rational-prime certificate checks;
no enumeration of relations or points. Before lengthy computation save
the plan and fix any arithmetic/factor-search caps. Scripts must save
complete certificates and replay evidence, print actual/required checks,
failures and paths, and preserve unfinished evidence on any cap stop.

Continue only after every inverse-map, twist, field-binding and
outside-support hypothesis is certified. Any missing identity, incomplete
factorization or incompatible transported lattice withholds the dependent
descent use; report the exact obstruction rather than silently change the
curve or treat a preview as verification. Success completes preparation
only. Failure does not disprove Beal or globally ban Jacobian descent.

## Classification and Mathlib

This literature-only turn supplies source approval and detects existing
model overlap. No new model, discriminant, support list, field map, lemma
or mathematical script was derived or written. The approved calculation
is a reproduction/specialization of known theory, not certified novelty.
Full matching Mathlib coverage for the model/support theorem has not
been checked. Reuse the prior assessments' supporting finite-abelian,
class-group and ideal-factorization coverage; no absence or Lean
verification is asserted. PROOF.md and DAG.md need no change because
the established mathematical argument has not changed.
