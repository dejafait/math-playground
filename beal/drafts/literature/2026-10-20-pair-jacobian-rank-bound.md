# Explicit pair curve — unconditional Jacobian rank-bound review

TARGET: Compute a certified unconditional upper bound for the Mordell–Weil rank of the Jacobian of L110's genus-two model.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact sextic/quartic coefficient variants, degree-55/A11 genus-two rank variants and standard hyperelliptic two-descent terminology; reused the explicit-model/Putz comparison and checked local rank/backend failure records; no inspected source identifies this exact Jacobian's rank.
SOURCE_EVIDENCE: Read Stoll, Acta Arith. 98 (2001), 245–277, equation (1.1), Sections 3–4 through Lemma 4.10; current Magma Handbook named Selmer, torsion, rank, class-proof and Chabauty entries; University of Sydney public calculator limits, all accessed 2026-10-20.
COMPARISON: Known two-descent gives unconditional upper bounds after complete global arithmetic and local-image certification; it supplies neither this instance's Selmer data nor a bound below two. The model and rational Weierstrass interface are already available.
GAP: No exact Selmer computation, complete class/unit certificate or checked executable submission route is available here; an adequate general theorem is not an instance-specific certificate. Point completeness and the original integer lifts remain independent.
REASON: Essential theorem coverage is sufficient for specialization, but the bounded execution test is unmet; park software-dependent rank computation until an executable route or complete reproducible data exists, and review an independent divisor-class lower-bound test.
LITERATURE_REASON: The saved rank-upper-bound target was REVIEW_REQUIRED; all earlier ready pair-model assessments excluded rank methods and their arithmetic certification.
SCOPE: Only unconditional upper-bound specialization for this exact Q-Jacobian; no rank lower-bound construction, Chabauty execution, new model construction or rational-point classification is approved by this assessment.

## Relevance, threshold and limits

The main gap remains primitive positive integer exclusion for residual
Beal signatures. In the rational-root-plus-minus-three-pair branch of
ordered (3,5,11), L109 supplies a necessary genus-two image and L110 its
audited exact Q-model

    W²=11(T²−4)(7+52T−6T²−64T³−25T⁴).

The intermediate target is an unconditional Jacobian rank upper bound,
with a useful diagnostic threshold strictly below two. This could enable
later rational-point work on the smaller necessary image. Even complete
pair-curve rational points would leave marked lifting, degree-nine root
recovery, compatible complementary factors and both L095 integer power
systems to check. Minus-eleven and other signatures remain unresolved.

Continue execution only with a concrete reproducible request and complete
certification evidence. A certified upper bound at least two merely fails
this sufficient threshold; it is not evidence that the rank is at least
two. Timeouts and missing class/unit completeness give no rank bound.
A separate exact independent-point lower bound could test that threshold
without the missing global completeness; it is not performed or approved
here.

## Primary theorem comparison

[Michael Stoll, Implementing 2-descent for Jacobians of hyperelliptic
curves](https://www.impan.pl/shop/en/publication/transaction/download/product/83397),
Acta Arithmetica 98 (2001), 245–277, DOI 10.4064/aa98-3-4,
p.245 equation (1.1), gives

    rank J(Q) <= dim Sel^(2)(Q,J) − dim J(Q)[2].

This does not assume finiteness of Sha. Sections 3–4, pp.248–255,
require field factorization, units, class groups and ideal maps.
For squarefree monic integral odd-degree f, Lemma 4.1 and Proposition
4.2 identify Kummer classes with norm-square algebra classes satisfying
all local images. Corollary 4.7 reduces testing to infinity, two and
primes whose squares divide disc(f). Lemma 4.9 retains class two-torsion;
Lemma 4.10 offers a coarser bound needing class data but no explicit
fundamental-unit generators. Its omission of unit generators does not
remove its class-group hypotheses.

The odd-degree setup on p.249 explicitly covers curves with a rational
Weierstrass point. L110's displayed squarefree model has points at
T=2 and T=−2 with W=0. Thus this setup is applicable after a verified
Q-coordinate change and integral monic normalization. No transformed
polynomial, field decomposition or rank is computed in this review.
The general theorem is imported; no reproof is warranted.

## Implementation and unconditional proof controls

[Magma Handbook, Jacobians over Number Fields or Q](https://docs.magma-maths.org/ArithmeticGeometry/HyperellipticCurves/jacobians-number-fields.html),
entries `TwoSelmerGroup`, `TwoTorsionSubgroup`, `RankBound`/`RankBounds`,
accept this genus-two integral sextic directly. The Selmer representation
differs between odd and even degree; a displayed algebra subgroup must
not silently be identified with the true Selmer group. `RankBound`
combines Selmer and torsion information. `ReturnRawData` and
`ReturnFakeSelmerData` are documented output options, not independent
proofs of arithmetic completeness. `Fields` can reuse precomputed class
data; only certified data should be supplied. No Sha parity improvement,
analytic rank or BSD premise is needed for the basic inequality.

[Magma Handbook, Ideal Class Groups](https://docs.magma-maths.org/GlobalFields/NumberFieldsAndOrders/ideal-class-group.html),
`ClassGroup` and “Setting the Class Group Bounds”, documents rigorous
defaults based on the Minkowski bound. `Proof := "Full"` alone does not
undo an earlier global `SetClassGroupBounds("GRH")`. A fresh process with
unchanged rigorous defaults, or explicitly verified Minkowski proof maps,
is required. Conditional cached fields must not be reused as certified
inputs. A smaller numerical factor bound or relations alone is not a
completeness certificate. Record the actual field models, maximal orders,
proof bounds and completed verification for every factor used. This
source's guarantee is an implementation contract; no run is claimed.

A useful future certificate must retain complete input code and version,
original model and any inverse model maps, class-proof settings and all
warnings/errors, Selmer and rational two-torsion dimensions, full returned
arithmetic data available for replay, and the claimed upper bound U.
Its summary must print actual U versus required U<2 and every failed
check. This is a certificate specification, not a manufactured result.

## Downstream point-method qualifications

[Magma Handbook, Chabauty's Method](https://docs.magma-maths.org/ArithmeticGeometry/HyperellipticCurves/chabauty-method.html),
introduction and `Chabauty0`, `Chabauty(P)` and `Chabauty(P,p)` entries:
the strict rank-versus-genus condition is essential. Rank one also needs
an infinite-order Jacobian point and a rational curve base point; the
new routine includes saturation, while the older fixed-prime routine
requires index prime to that good prime. `Chabauty0` assumes rank zero
without checking it. None of those computations or point-completeness
claims follows from the present review.

## Exact-instance, duplicate and failure checks

The earlier explicit-model assessment inspected Putz's complete
GFE/3511.m without a matching pair-model/rank certificate; its adequate
comparison is reused. New searches included `"-275" "-704" "1034" curve`,
`"275" "704" "3388" hyperelliptic`, `"11" "7+52*x" hyperelliptic`,
`"genus two" "55" "A11" rank`, and standard Stoll/Schaefer genus-two
rank-bound variants. No matching rank theorem was found in inspected
sources. Unrelated LMFDB search hits and unread papers are not imports,
and absence of a search match does not establish novelty.

Local checks used L110's statement/model charts, history/380, the
explicit-model source assessment, the prior coarse elliptic rank
assessment and ATTEMPTS/032 and 045. L069's old twelve-dimensional
unit obstruction concerns a different elliptic descent over a different
base field; neither its dimension nor its stop applies to this Jacobian.
The scaling and seven-adic stops also do not ban global pair-point work.
No cross-notebook result is used. L108's unfinished work is preserved.
Mathlib coverage of the full rank computation was not checked.

## Execution feasibility and route decision

The [University of Sydney calculator](https://magma.maths.usyd.edu.au/calc/)
page was read: it advertises Magma V2.29-10, 60 seconds per calculation
and 50,000 input bytes. No request containing mathematical code was
submitted. Web retrieval of the page works, but the attempted read-only
Python GET failed with a DNS-resolution error. This establishes only
the failure of this shell transport. The web tool did not expose the
calculator JavaScript; a usable submission-and-full-output path was not
established. An accessible landing page is not an executed backend.
Local `magma`, `sage`, and `gp` PATH probes found none, matching the old
backend prerequisite; this is not fresh mathematical negative evidence
and does not justify repeated availability probes. No installation,
API key or paid service was used.

Accordingly, do not schedule another identical backend preflight. Park
this implementation route until a usable bounded execution path or full
independently checkable external data is available. This is an execution
limitation, not SOURCE_BLOCKED theorem coverage and not a mathematical
obstruction to two-descent. A handwritten complete descent is possible
in principle but no bounded successful plan has been demonstrated here.
The next proposed target is a certified divisor-class rank lower-bound
test, which avoids class-group completeness and must receive its own
separate source approval. No rank or new lemma was obtained today.
