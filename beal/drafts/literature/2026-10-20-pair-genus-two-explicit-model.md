# Pair genus-two explicit model — source comparison

TARGET: Construct an explicit hyperelliptic model of L109's genus-two curve B with rational functions s and z and verified birational maps.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the pair-cover assessment's exact-instance/Putz comparison; searched polynomial variants, A11/degree-55/genus-two Belyi covers and canonical/Weierstrass-model algorithms; inspected the primary methods below and Putz's complete GFE/3511.m, finding no matching explicit pair-curve model in the inspected sources.
SOURCE_EVIDENCE: Read van Hoeij arXiv:math/0203130v1 Sections 1–4 pp.1–4; Poonen ANTS-II (1996) Sections 2–3 author pp.2–4; van Bommel–Costa–Poonen–Srinivasan arXiv:2506.14026v1 Theorem 3.1 p.2, Section 5 steps 1–6 pp.4–5 and Lemma 6.2 p.8; Magma Handbook V2.29 model/canonical/differential interfaces; Stacks 53.2.6 and its map-extension proof.
COMPARISON: Known methods cover constructing genus-two quintic/sextic models over Q without an assumed rational point; they do not compute L109's equation, inverse maps, transported s,z or exceptional charts. A nonsplit hyperelliptic quotient conic is not an existence obstruction in even genus.
GAP: Compute and certify canonical data, an exact Q-model and inverse function-field maps for L109, retaining s=H0(u,z), the exact z and v²=z; none has been computed here.
REASON: Essential method coverage and rationality comparison are complete for the unchanged target; perform its instance-specific construction in a separate research invocation, importing the general results rather than re-proving them.
SCOPE: Exactly TARGET on L109's specified open and smooth proper normalization over Q; canonical-differential/Riemann–Roch construction, exact elimination and inverse-map verification are covered; rational points, rank, degree-nine lifting, other twists and integer elimination are excluded.
LITERATURE_REASON: The saved explicit-model target was REVIEW_REQUIRED and outside the ready pair-cover assessments; model-construction and rational-conic hypotheses required this separate comparison.

## Proposed target and relevance

The main gap is still residual-signature integer exclusion. In this
branch even rational-point control is unavailable. An explicit low-degree
model retaining the original scalar and the minus-three square class
could enable a later assessment of rational-point methods. No rank,
Jacobian arithmetic or point-classification method is assumed feasible.

Essential mathematical input: audited L109, using its definitions of
B, H0, H1, s and z, and its independently verified pair certificate.
L106/L107 are already inputs to L109; L108's unfinished boundary
decomposition is not required for this proposed task. The same original
polynomial and same Q-form must be retained. The marked companion is
still defined by v²=z, not by an arbitrary twist of a proposed model.

The proposed discriminating test is an exact smooth genus-two model over
Q together with inverse rational maps on specified dense opens, explicit
s and z, and a justified extension to the same smooth proper curve.
If a rational double-cover presentation uses a conic, its actual Q-form
must be kept; do not assume a rational point or a Q-line parametrization.
An implicit equation without verified inverse maps does not meet this
test. The source review must determine suitable bounded construction
methods and known obstructions before approving it.

Rational points, degree-nine rational-root recovery, compatible remaining
factors, both L095 power/gcd/positivity systems and minus-eleven remain
independent unresolved assumptions. An explicit model alone resolves none
of them. Mathlib coverage has not been checked. No new lemma, equation,
birational map is supplied by this review.

## Inspected primary methods

M. van Hoeij, *An algorithm for computing the Weierstrass normal form
of hyperelliptic curves*, [arXiv:math/0203130v1](https://arxiv.org/pdf/math/0203130),
14 March 2002, **Sections 1–4, pp.1–4**, read in full.
The input is an irreducible plane polynomial over C. Section 1 describes
an index-two rational subfield, quadratic generator by a resultant,
square completion, square-factor removal and inverse coordinate
expressions. Sections 2–3 use holomorphic differentials; at genus two
the whole differential space already has dimension two. Section 4
displays maps in both directions for a different curve. This covers
the method, not preservation of Q by every complex-coordinate
implementation. The cited differential-basis and inverse-coordinate
subroutines refer respectively to Deconinck–van Hoeij (2001) and
van Hoeij (1995); these papers were not separately read and their
implementations are not independently verified premises. No Maple
backend availability or execution is claimed.

B. Poonen, *Computational aspects of curves of genus at least 2*,
**ANTS-II, LNCS 1122 (1996), pp.283–306**, author version dated
10 April 1996, [primary PDF](https://math.mit.edu/~poonen/papers/ants2.pdf),
**Sections 2–3, author pp.2–4**.
For a perfect field of characteristic different from two, Section 2
states the genus-two quintic/sextic result; footnote 1 distinguishes
general conic obstructions from even genus. A quintic requires a
rational Weierstrass point; a sextic suffices here. Section 3 gives a
canonical-divisor/Riemann–Roch construction without an assumed rational
point. These statements cover rationality, not B's computed canonical
data. The historical algorithm references were not separately read.

R. van Bommel, E. Costa, B. Poonen and P. Srinivasan,
*Curve equations from expansions of 1-forms at a nonrational point*,
[arXiv:2506.14026v1](https://arxiv.org/html/2506.14026v1),
16 June 2025, **Theorem 3.1 p.2; Section 5 steps 1–6 pp.4–5;
Lemma 6.2 p.8**, checked in versioned HTML and the author PDF.
Input hypotheses: smooth projective geometrically integral Q-curve,
finite K=Q(P), a uniformizer at P, and expansions of a Q-basis of
regular one-forms to precision 19g+48. The even-genus output is a
separable degree-(2g+1) or degree-(2g+2) polynomial over Q. The relevant
proof cases recover the quadratic extension and parametrize the
quotient using an odd-degree divisor; Lemma 6.2 justifies precision.
The method needs no rational P, but does require certified input
differentials and expansions. It does not itself output s,z or inverse
maps. This is an optional construction method, not an application or
expansion calculation performed here. Only v1 was available and is used;
the attempted v2 HTML URL returned 404.

The [Magma Handbook, Special Forms of Curves](https://magma.maths.usyd.edu.au/magma/handbook/text/1468),
**V2.29, 3 August 2026**, documents `IsHyperelliptic` with a
Weierstrass model and map, and `IsGeometricallyHyperelliptic` with a
degree-two map to a line for even genus or conic for odd genus.
The method uses the canonical map and function-field differentials.
Read the associated
[canonical/Riemann–Roch interfaces](https://magma.maths.usyd.edu.au/magma/handbook/text/1473)
and [holomorphic-differential interfaces](https://magma.maths.usyd.edu.au/magma/handbook/text/1471)
for their basis and function-field output contracts. No runtime,
license, execution or correctness of a returned instance is assumed.
A map involving a singular plane model must be checked birationally
on its normalization; the documentation's word “isomorphic” cannot
replace that check. These are implementation references, not a required
paid service.

Reuse [Stacks Theorem 53.2.6, tag 0BY1](https://stacks.math.columbia.edu/tag/0BY1),
also rechecked in primary HTML, including extension of rational maps
and the normal-projective/function-field equivalence. Verified inverse
Q-function-field maps identify the same smooth proper curve in
characteristic zero. The theorem does not supply those maps or license
substitution at a plane singularity. No reproof is justified.

## Exact-instance search, duplicates and preserved failures

Queries included `genus 2 curve hyperelliptic model canonical map rational
conic algorithm plane curve van Hoeij`, `"(3t^2+t+1)^5" curve`,
`"3x^2+x+1" "genus" "11"`, `"unordered pairs" "genus 2" "Belyi"`,
`Belyi "55" "A11" genus`, `"genus two" "degree 55" curve`,
and `Putz "3,5,11" quadratic factors genus`.
No inspected matching model resulted; search silence proves no novelty.

The Putz query led to the author's
[etale-algebra-family repository](https://github.com/CPutz/etale-algebra-family).
Read its complete 257-line
[GFE/3511.m](https://raw.githubusercontent.com/CPutz/etale-algebra-family/master/GFE/3511.m),
master branch retrieved 2026-10-20; no immutable commit was exposed
by the fetched view. It contains the same phi and local étale-family
routines, including coefficient/ramification variants, but supplies no
pair-curve hyperelliptic equation or maps. No statement about all other
repository files or execution is made. Reuse the Putz thesis and
different-map example comparison in
`2026-10-20-forget-distinguished-root-quotient.md`; its special-coefficient
terminal exclusions do not apply here. No new thesis theorem is imported.

Compared L109's model and audit, the ready construction/audit assessments
and history/376. Their scopes exclude this target. ATTEMPTS/048 stops
direct rational scaling as an exclusion shortcut; the minus-three
ATTEMPTS/046 stops standalone exclusion at seven by an exact witness.
Neither stop is reopened. L108's unfinished boundary decomposition is
independent and preserved. No sibling notebook was read.

The target was rechecked at
[Mauldin's live primary page](https://sites.math.unt.edu/~mauldin/beal.html):
positive integer bases and exponents greater than two, with a prime
common to all three bases, agreeing with GOAL.md. The nominated AMS
page again failed retrieval; its current contents and prize rules are
not asserted to have been read. This adds no mathematical hypothesis.

## Bounded construction obligations

These are requirements for the future attempt, not new proved claims
about B. Start with L109's exact Q-function field and closure of the
specified open. Use the cited canonical-differential or Riemann–Roch
method. If computing from the singular plane closure, certify regularity
of canonical data on every normalized branch, including infinity.
Dimension two or a guessed pair alone does not certify regularity.

The desired certificate has a squarefree quintic or sextic over Q and
coordinate expressions in both directions. Verify defining relations
and both compositions in the correct function fields, on explicit
nonempty dense opens with denominators nonzero. Transport the actual
s and z and check s=H0(u,z). Preserve the marked extension v²=z;
a changed generator requires an explicit rational square multiplier,
including its constant. Matching numerical invariants or an isomorphic
Jacobian is insufficient.

Distinguish the smooth proper model from a singular plane closure.
Use 0BY1 only after verifying the function-field isomorphism and identify
exceptional charts by normalization. Reuse L109's unit-residue lifting
rule at zeros and poles of z. The even-genus sources remove the need
to assume a rational point for the hyperelliptic parameter; any auxiliary
conic produced by an implementation still needs a verified
Q-parametrization. Do not infer that B itself has a rational point.

One exact construction attempt is justified. Success requires the
same smooth proper Q-curve, inverse maps and explicit s,z; an equation
alone is incomplete. Stop the selected implementation and preserve
unfinished output if it requires an unavailable backend or cannot
certify canonical data or inverse maps within the bounded attempt.
That is not a mathematical nonexistence result. No purchase, API or
numerical fitting is approved. Rational-point work needs a separate
target and assessment. Both L095 systems and all other gaps above remain.

This LITERATURE / EXPLORATION / NOVELTY_UNCHECKED step supplies source
readiness, not a new mathematical result beyond the inspected sources.
Full matching and supporting Mathlib coverage were not checked. No
lemma or mathematical script was written and no certificate was rerun.
