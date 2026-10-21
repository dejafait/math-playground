# Simultaneous point realization: period-index source comparison

TARGET: Assess primary period-index and simultaneous splitting theorems for L018's two depth-m Sha images, distinguishing bounds for one torsor from a common field and whether any applicable result supplies v_p([F:Q]) < m without finite Sha.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches located Clark's primary period-index proofs and Clark--Sharif's global-field results; exact queries and inspected ranges are below. Existing transfer assessments and ATTEMPTS/020 were reused.
SOURCE_EVIDENCE: Clark, WC-groups II, author-hosted 33-page text, Theorem 4 p. 3, Proposition 11 p. 6, Section 4.2 p. 14, Theorem 30 p. 19 and Section 5.6 p. 20; Clark math/0411413v1, Proposition 6 pp. 2--3; Clark--Sharif 2010, Section 1.1 and Theorems 1--3 p. 152.
COMPARISON: Known geometric splitting bounds apply without finite Sha, but none of the inspected statements supplies L020's strict degree certificate; park generic period-index splitting as a rank-production mechanism.
GAP: Rational realization remains missing; neither individual periods nor the actual common degree are prescribed by the Selmer basis alone. No construction at the strict threshold is obtained.
REASON: The source comparison changes the route: geometric existence is covered, whereas the needed degree improvement is not. No new lemma, reproof or mathematical script is justified by this review.
SCOPE: L018 and L020, m >= 2, one common field for both prescribed classes, no finite-Sha or positive-rational-rank assumption. Only the inspected geometric bounds and their applicability are assessed.

## Gap and discriminating test

The exact main gap remains rank E(Q) = ord_(s=1) L(E,s) for
analytic order at least two. The intermediate source target is a common
point-realizing field for L018's depth-m classes, with p-degree valuation
strictly below m. Such a witness would activate L020's conditional lower
bound. Continue geometric production only if a primary theorem meets
that threshold under the retained hypotheses; otherwise park the generic
mechanism. Production of the two-prime premise, analytic comparison and
higher ranks are independent open gaps.

No mathematical construction is performed here. L018's full finite row
and L020's generating-image/annihilator argument were read. ATTEMPTS/020
stops the equality-threshold inference from the tested formal maps; this
review tests a different, geometric source mechanism and preserves that
stop evidence. The earlier transfer assessments explicitly excluded
period-index coverage, so this is not a duplicate source approval.

## Inspected primary statements

**Clark, WC-groups II.** Use the [author-hosted 33-page text](https://plclark.github.io/PeteLClark/Research/wc2.pdf),
retrieved 2026-10-05; no publication or revision date is inferred.
Theorem 4 (p. 3) says a locally trivial n-torsion torsor under a
strongly principally polarized g-dimensional abelian variety over a
number field splits over a field of degree at most g! n^g.
Section 4.2 (p. 14) requires a principal ample line bundle defined over
the base field. Proposition 11(a) (p. 6) gives period dividing every
splitting degree. Read Theorem 30 (p. 19) and Section 5.6 (p. 20):
local points kill the divisor obstruction, Brauer local-global kills it
globally, and a linear section supplies an effective zero-cycle.
Its closed points supply the asserted field bound, not a divisibility
claim for that field's degree. Section 5.6's heading says “Theorem 3”;
its number-field case proves the displayed Theorem 4. No finite-Sha
hypothesis enters this case.

**Clark, individual torsors.** [There are genus one curves of every index
over every number field](https://arxiv.org/pdf/math/0411413v1),
v1, 2004-11-18, Proposition 6 (pp. 2--3), applies to a genus-one
curve over a number field locally trivial away from at most one place.
It proves period equals index. Read both proofs: the first uses O'Neil's
obstruction and Brauer reciprocity; the second uses the Picard-to-Brauer
exact sequence. These proofs do not assume finite Sha. Use this inspected
primary proof rather than an uninspected attribution to Cassels.

**Clark--Sharif.** [Period, index and potential, III](https://msp.org/ant/2010/4-2/ant-v4-n2-p02-p.pdf),
Algebra & Number Theory 4 (2010), 151--174, Section 1.1 (p. 152),
identifies the genus-one index with the least splitting-field degree,
using Riemann--Roch. Theorems 1--3 (p. 152) respectively construct
prescribed period/index classes with full torsion, classes with pairwise
differences of index P^2, and large Sha over degree-P extensions.
They do not split a prescribed pair of Sha classes over a small common
field. In particular, creating local triviality over an extension in
Theorem 3 is not global torsor triviality. Their proof sections were
not needed or inspected, since their statements do not supply the target.

## Applicability and degree comparison

Write b_i = q_(Q,m)(x_i^(m)) as in L020. Each b_i is represented by
a genus-one E-torsor C_i and is locally trivial, by its Sha membership.
Let P_i be its actual period; the zero class has period one. The
individual result therefore gives index P_i and a splitting field of
degree P_i. It does not say P_1 = P_2 = p^m. L020 already records that
the two images generate Sha[p^m] and that, if r < 2, this group has
exponent p^m. Thus their common annihilator must have p-valuation at
least m; this is the existing obstruction, not a new result of this turn.

For simultaneous applicability, C_1 x C_2 is the torsor for A = E x E
represented by (b_1,b_2); a point on this product is exactly a point on
both factors over the same field. The external product of the two
Q-rational degree-one origin bundles induces a Q-rational principal
polarization on A. This checks the strong-polarization hypothesis;
no rational point on either C_i is assumed. The pair is locally trivial
and killed by p^m. Specializing the inspected bound at g = 2 and n = p^m
gives a common field of degree at most 2p^(2m). Since p >= 5, this
numerical bound only guarantees v_p([F:Q]) <= 2m. It supplies no guarantee
v_p([F:Q]) < m. “At most” must not be replaced by “divides”, and the
index as a gcd for higher-dimensional torsors must not be treated as an
attained degree. The cited theorem itself supplies an actual field bound.

Individual degree bounds cannot be substituted for the common degree.
We do not assert a compositum degree divides the product of two
non-Galois degrees. The product-torsor statement avoids that inference.
No theorem inspected provides a strict witness, and a bounded search
cannot establish that no stronger theorem exists. Under L018 any strict
witness would already force r = 2 by L020; the geometric existence
statements do not settle that missing arithmetic conclusion.

## Search record and leads

Queries used: “Cassels locally soluble genus one curves period equals
index Sha theorem”; “Clark Sharif period index genus one curves
simultaneous splitting number fields torsors”; “Cassels 1962 Arithmetic
curves genus 1 V Theorem 1.3 period index pdf”; “simultaneous splitting
locally trivial torsors elliptic curves number field degree period
index”; and “The period-index problem in WC-groups II 2008 2010 Clark
journal”. Primary passages read are enumerated above. Sharif's prescribed
period/index construction, Cassels's original statement and O'Neil's
original paper are leads, not independently inspected theorem inputs.
The retrieved Clark proofs suffice for this bounded comparison; no
source blocker is asserted.

## Route and continuation

Outcome: NEGATIVE source overlap with an applicable geometric theorem
whose guaranteed degree range misses the required threshold. This is
local route evidence, not progress beyond the inspected sources or an
arithmetic counterexample. Park generic splitting. Reopening requires
an explicit additional arithmetic mechanism controlling a common field,
with its own independent degree test, rather than another transfer audit.

Move to the independent production gap: assess whether analytic order
two can supply the minimal nonzero mod-p two-prime Kurihara premise.
The separate pending assessment records this changed target and its
unresolved assumptions; no approval of that mathematics is claimed here.

## Mathlib

Full matching period-index and common-field theorems: not checked.
Supporting product torsors, polarizations and Riemann--Roch: not checked.
No absence or novelty inference is made. This literature-only turn
changes no canonical lemma, DAG, argument assembly or mathematical script.
