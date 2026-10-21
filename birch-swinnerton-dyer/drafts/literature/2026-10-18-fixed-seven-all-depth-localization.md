# Fixed seven-primary all-depth localization — source comparison

TARGET: Assess whether L034, L081 and L082 certify a split surjective classical localization map Sel_{7^n}(E/Q) -> E(Q_7)/7^nE(Q_7) with a cyclic rational Kummer kernel for every n>=1 on E=[0,1,1,-2,0].
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Read the specific L034/L081/L082 proofs and audits, foundations/02, L005 and the relevant L061/L065/L066 statements, ATTEMPTS/031/034 and histories 309/315; searched the known-point and integral-leading-term assessments for overlap. External exact-curve/localization and Selmer/Kummer/splitting searches found general coverage, but no inspected theorem stating this exact finite-level assembly; queries and exclusions below.
SOURCE_EVIDENCE: Milne, Elliptic Curves, second edition (2021), IV Proposition 1.5 and its connecting-cocycle proof p.108, IV.1.9 pp.110–111, IV.2 equations (28)–(29) and their global/local diagram pp.112–113 inspected; Silverman (2009) VII.2.1–2.2 and IV.6.3(b)/6.4 with errata coverage reused from the known-point assessment, with IV.6.4 and proof reread; Stacks Project Definitions 10.77.1, Lemmas 10.77.2 and 10.78.2 and relevant splitting/free-module proof cases inspected 2026-10-18.
COMPARISON: Known Kummer, reduction, logarithm and module theorems cover the ingredients; L034 supplies published rank two, L081 an actual primitive local value and L082 published seven-primary Sha vanishing. L005 already supplies the rationalized strict-line dimension, but does not assert the proposed integral finite-depth splitting. Only a fixed applicability assembly remains; no mathematical novelty is claimed.
GAP: No essential source blocker remains for the stated fixed target; a separate research turn must justify torsion exclusions, every-depth local cyclicity and primitive-point generation, identify localization via Kummer naturality, and apply splitting and kernel structure. These conclusions are not derived in this review.
REASON: The exact fixed inputs change the stopped generic interface into a source-covered application. General rank equality, coefficient production and rational Kummer membership on arbitrary curves remain open; no reproof of the source theorems or published computations is needed.
LITERATURE_REASON: The saved REVIEW_REQUIRED target changed from a depth-one point test to all finite levels; essential Kummer and module coverage had not been compared. This completes that missing comparison rather than repeating ready literature.
SCOPE: Only E=[0,1,1,-2,0], p=7, all integers n>=1, classical Selmer conditions at every place and localization through the injective local Kummer map; cyclic rational Kummer kernel means a subgroup of E(Q)/7^nE(Q) under the global Kummer identification, not an individual rational point with zero local logarithm. No canonical or explicitly computed kernel generator is requested.

## Relevance and bounded decision

The main gap is still rank E(Q)=m(E) for arbitrary analytic order at least
two. The intermediate target is exactly TARGET above. Its plausible use
is to finish this fixed classical-localization application using actual
rational and Sha inputs without completing the degree-48 arithmetic
route. It cannot produce those inputs uniformly. Continue only with all
finite-depth maps and module hypotheses explicit; stop the assembly if
an essential torsion, primitivity or Kummer hypothesis cannot be justified.
The source-coverage test passes; the mathematical applicability test is
reserved for the next research turn. No new lemma or calculation occurs
in this review.

## Primary coverage and proof cases

[Milne, second edition](https://www.jmilne.org/math/Books/EC2.pdf#page=113):
IV.1.5 constructs the connecting map from a lift and its Galois cocycle.
IV.1.9 describes localization. IV.2, pp.112–113, displays the injective
local Kummer map, commuting global/local diagram and exact sequence
(29) for any integer greater than one; no finiteness of Sha is assumed.
Read the algebraically closed multiplication-surjectivity lemma, the
cohomology sequence and kernel-cokernel argument used there. Substitute
7^n for the source's integer; Q and Q_7 have characteristic zero.
The later prime-to-residue-characteristic lemma IV.3.2 is NOT applicable
to division by seven over Q_7 and is not an input.

[Silverman, second edition](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=150):
IV.6.4(b) applies to a formal group over a complete discretely valued
characteristic-zero field for integer r>v(p)/(p-1); its proof uses the
logarithm/exponential inverse identities and strict convergence estimates.
Reuse the full VII.2.1–2.2 reduction/parameter and author-errata comparison
in `2026-10-18-known-point-local-seven-test.md`, pp.188–191 and 131–132.
At Q_7 the threshold is 1/6. The later application must use the full
reduction sequence with order 13, not just the formal subgroup, and
retain the strict radius. No new logarithm computation is required.

[Stacks Project, Section 10.77](https://stacks.math.columbia.edu/tag/05CD),
Definition 10.77.1 and Lemma 10.77.2, give projectivity and splitting
against a surjection, and prove free modules projective. [Lemma 10.78.2,
tag 00NX](https://stacks.math.columbia.edu/tag/00NX) identifies finite
projectives with direct summands of finite free modules and with finite
locally free modules. Read the splitting proof and local-freeness cases.
These apply to arbitrary commutative rings, including the finite local
ring Z/7^nZ. A research application must first establish surjectivity and
the ranks; the ring is not a field when n>1.

## Fixed inputs and remaining applicability obligations

L030's exact minimal equation and L033's good reduction/count are the
local arithmetic inputs. L034's published rank-two group result is
adequate without assuming its displayed pair is seven-saturated: the
later proof can choose an abstract free basis if needed. L081 supplies
P=(0,0) nonzero locally modulo seven and the verified valuation of [13]P.
L082's separately audited Theorem 12.3 import supplies the primary Sha
input. Retain the unreplayed computational provenance in both global
results; neither a new descent replay nor a general integral upgrade of
Kato divisibility is needed.

The research turn must explicitly check the following obligations rather
than declare them proved by this assessment:

- Exclude local and hence rational seven-primary torsion using the full
  reduction sequence and the strict-radius formal logarithm. Use finite
  generation and rank two for the global finite quotients; no total
  rational torsion classification is required.
- Compare the formal subgroup quotient with the full local quotient at
  every depth, retaining both injectivity and surjectivity and the
  prime-to-seven reduction group. Use L081 only after that comparison
  to test generation at all depths, not merely nonzeroness at depth one.
- Apply Milne with L082, and define the map from Selmer by restriction
  followed by the inverse on the local Kummer image. Verify its agreement
  with point localization and the classical conditions at every place.
- Establish a split surjection as Z/7^nZ-modules and a free rank-one
  kernel, using the cited module results or an explicit unit-coordinate
  argument. Specify that rational Kummer membership is at the quotient
  level. Compatible or canonical choices of splitting are outside the
  requested target unless separately justified.

This list specifies source-covered specialization work; it contains no
proof of the new all-depth assertion. Full matching Mathlib coverage and
supporting theorem names are not checked; no absence claim is made.

## Duplicates, failures and external search record

L005 already gives the rationalized rank-minus-one strict Kummer space,
including a logarithmic linear combination of a supplied rational basis.
Thus a new rationalized dimension lemma would duplicate existing work.
L061 leaves integral finite images and two branches under its different
conditional package; L065 is an uninstantiated full-descent interface,
and L066 requires arithmetic upper-enclosure data. None states the
proposed fixed all-depth application using L082 and L081. Do not claim
to discharge every L026 premise or produce an auxiliary Kato component.
ATTEMPTS/031 stops direct localization import from generic ordinary
semisimplicity; ATTEMPTS/034 stops repeating the conditional interface.
The present fixed inputs are materially different and leave those stops
intact. Histories 309/315 rule out another L081 replay as useful work.

Queries on 2026-10-18: `elliptic curve Selmer Kummer exact sequence
localization E(Qp) p-adic Zp finite group`; `"389a" "localization"
Selmer`; `"Selmer" "split" "Kummer" "Z/p" localization`.
Results included general Selmer papers and nonprimary aggregators; no
exact matching theorem was established by those searches. Only Milne,
Silverman and Stacks are used for new theorem coverage. Search snippets,
secondary discussions and an unrelated recent laboratory manuscript are
not evidence for this target. The prior published fixed-case rank/Sha
assessments are reused rather than browsed again. Failed discovery is
not a novelty claim.
