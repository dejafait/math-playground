# Marked genus-three conic presentation — source comparison

TARGET: Construct an exact hyperelliptic model of L111's marked genus-three curve via its conic h²=3(4−T²), retaining reversible maps and boundary lifts.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the marked-quotient comparison and pair-rank failure records; searched exact quartic/conic variants, rational-conic parametrization, smooth proper curve extension and hyperelliptic two-cover descent; inspected Stacks, Bruin–Stoll and Magma primary passages. No inspected source supplies this instance's polynomial/maps; failed searches imply no novelty.
SOURCE_EVIDENCE: Stacks Proposition 53.10.4 (Section 53.10, 0C6L), Theorem 53.2.6 (0BY1) including extension proof, and Section 53.12; Bruin–Stoll arXiv:0803.2052v2 Section 2 p.3, Theorem 3.4/proof pp.5–6, Section 6 pp.11–12, Section 8 pp.14–16 including Example 8.1; Magma Handbook V2.29 Isomorphisms with Standard Models and Two-Selmer Set of a Curve including cutoff qualifications, accessed 2026-10-21.
COMPARISON: Standard results cover parametrization of a smooth rational-pointed conic and extension of verified inverse function-field maps to smooth proper curves; point-cover descent accepts a squarefree hyperelliptic polynomial and can organize rational points despite positive-rank elliptic quotients. They do not give this instance's equation, inverse functions, omitted fibers or point classification.
GAP: Compute and verify the polynomial, exact square rescaling and inverse maps; transport the original functions and all omitted rational fibers. Certified descent arithmetic, surviving-cover point control, root recovery and integer exclusions remain separate gaps.
REASON: Approve one bounded model specialization as a concrete point-cover input, retaining the complementary square condition and known boundary points; construction approval does not certify an executable complete descent or rational-point completeness.
LITERATURE_REASON: The saved REVIEW_REQUIRED target lay outside the L112 audit; essential conic, boundary-extension and concrete point-descent-use coverage required this separate literature-only comparison.
SCOPE: Exact Q-curve/functions of audited L109–L111, with L112's positive-rank obstruction; one parametrization through (T,h)=(2,0), exact model/maps and omitted-fiber accounting. No enlarged search or rank computation.

## Main gap and local comparison

The main gap is primitive positive integer exclusion for residual signatures.
The intermediate target retains the marked curve's square condition,
which the elliptic projection discards. Its possible use is the specific
point-cover input below; another equation alone settles neither points
nor integers.

Use the supplied overview/DAG and the narrow local inputs: L111's
hypotheses, equations, exact maps and smooth charts; the ready
`2026-10-20-marked-pair-genus-one-quotient.md` assessment; relevant
pair-rank assessments; ATTEMPTS/050–051 and history/390–391. L111's
canonical proof records its completed audit despite stale pending-audit
language in the overview. The supplied checkpoint and history/391 record
L112's audit. No audit is repeated here.

L111 already supplies the two-equation marked model and elliptic map,
including denominator/infinity charts and rational boundary points above
T=2. It does not give the proposed one-polynomial model. ATTEMPTS/050
parks its fixed genus-two search caps. ATTEMPTS/051 and audited L112
stop the actual elliptic rank-zero premise, not other marked-point
methods. Preserve both records and unfinished L108; no sibling input
is used.

## Primary coverage and qualifications

[Stacks Proposition 53.10.4](https://stacks.math.columbia.edu/tag/0C6L)
characterizes the projective line: a smooth geometrically integral proper
genus-zero curve with a degree-one invertible sheaf is isomorphic to it.
A rational point supplies that sheaf. Check the projective conic and
known point when applying this standard theorem; do not reprove it.
The inspected proof reduces to the degree-one linear system in Lemma
53.10.2. Explicit formulas and both compositions remain the task.

The primary [Magma Handbook, Isomorphisms with Standard Models](https://magma.maths.usyd.edu.au/magma/handbook/text/1539),
opening discussion and ParametrizationMatrix/Parametrization entries,
describes conic parametrization and the two inverse charts covering the
standard conic. This supports a global construction rather than an
unexamined affine slope chart. A later range request timed out; the
opening discussion and matrix entry had already been read. No software
execution or local availability is inferred.

[Stacks Theorem 53.2.6](https://stacks.math.columbia.edu/tag/0BY1)
identifies transcendence-degree-one fields with normal proper curves
and nonconstant morphisms. Its inspected proof extends the rational map
across the nonsingular source and proves uniqueness. Over Q use it only
after verifying inverse fields. It does not calculate omitted fibers;
explicit smooth charts must still identify their rational points and
transported functions. [Stacks Section 53.12](https://stacks.math.columbia.edu/tag/0C1B),
Lemmas 53.12.1–2 and the characteristic-zero formula, supports a genus
check for a separable map of smooth proper geometrically integral curves,
with all ramification and residue degrees retained.

Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic curves*,
Math. Comp. **78** (2009), 2347–2370, DOI
[10.1090/S0025-5718-09-02255-8](https://doi.org/10.1090/S0025-5718-09-02255-8),
inspected [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
21 October 2008:

- Section 2, p.3: characteristic zero, smooth projective model, squarefree
  polynomial, even degree 2g+2; the point map includes Weierstrass and
  infinity cases. The fake Selmer set contains the rational point image.
- Theorem 3.4/proof, pp.5–6: everywhere locally soluble two-covers occur
  among explicit covers modulo hyperelliptic involution; retain that
  local-solubility hypothesis.
- Section 6, pp.11–12: supported square classes and local images provide
  finite computation inputs.
- Section 8, pp.14–16: surviving classes give factor-curve twists by a
  norm, with rational-coordinate and lifting tests still required.
  Example 8.1 treats positive-rank elliptic quotients, then uses further
  arithmetic to prove point completeness.

The primary [Magma Handbook, Two-Selmer Set of a Curve](https://magma.maths.usyd.edu.au/magma/handbook/text/1619),
V2.29, dated 3 August 2026, provides a specific prospective consumer:
`TwoCoverDescent(C)` returns a set and a map to algebra representatives
for explicit covers. The entry explicitly discusses genus three over
number fields. `PrimeBound` and `PrimeCutoff` can enlarge the returned
set; its worked example additionally needs a finite-index Mordell–Weil
group and Chabauty before lifting back. This is an input interface,
not proof that the computation can currently be run or completed here.

## Approved bounded specialization

Import the general theorems above. Only the missing instance-specific
polynomial, constants, inverse functions and special fibers need
calculation; a general reproof is unnecessary. No parametrization,
polynomial or new lemma is derived in this literature turn.

In the research turn, use one line parametrization through (2,0) on the
conic and substitute into L111's other equation. Retain every constant
twist; remove only verified rational-square factors. Require a squarefree
genus-three model, of degree seven or eight in the usual affine form,
not repeated factors with an unexamined normalization. Verify inverse
Q-function-field compositions; retain the original s,z,v,W and elliptic
projection through L111's formulas.

List all parameter values and denominator zeros excluded by either map.
Use smooth finite/infinity charts to account for every rational point
there, including L111's known T=2 lifts. Coordinate exceptions are not
the entire original s-boundary; no full s-boundary classification is
required. Proper extension alone is not the requested fiber accounting.

Continue only if squarefreeness/genus, inverse maps, original functions,
projection and all omitted rational fibers pass exact checks. Repair a
coordinate error within this one construction, or park if an essential
requirement fails. No enlarged point search, rank upper bound or claim
of rational-point completeness is approved.

## Concrete downstream use and independent gaps

A verified polynomial can feed point-cover descent for candidate square
classes and explicit cover representatives. This is a materially different
input from searching the parked boxes or attempting rank-zero enumeration.
By L111 this marked curve already has rational boundary points. Thus an
empty fake-Selmer-set exclusion cannot work: later descent must retain
their classes and control other points on surviving covers. L112 does
not decide those lifts. These are applicability limits of the inspected
method, not new mathematical results established here.

Any later descent needs certified entire-root-algebra arithmetic: support,
units, class contributions and local images. Rank/subgroup data and
cover-point arguments may also be required. No useful factorization,
rank inequality, complete descent or working backend is assumed; a
separate target must assess their execution. Degree-nine distinguished-root
recovery, remaining factors, both L095 integer systems and minus-eleven
remain unresolved even if marked rational points are eventually controlled.

## Search record, exact target and Mathlib

Queries included `Bruin Stoll Two-cover descent on hyperelliptic curves
2009 section 2 section 8 pdf`, `rational conic parametrization rational
point hyperelliptic curve birational smooth projective curves Stacks`,
`"hyperelliptic" "825" "2112" "1716"`,
`"825" "2112" "198" "hyperelliptic"`,
`"h^2=3(4" "hyperelliptic"`, and Magma TwoCoverDescent/genus searches.
Primary inspected passages are specified above. Other hits, including a
genus-two-only explicit-cover implementation, are not coverage for this
construction. Reuse the prior marked-quotient split-cover/Putz comparison;
no exact-instance matching theorem was identified among inspected sources,
and no novelty is inferred.

The [live Mauldin primary statement](https://sites.math.unt.edu/~mauldin/beal.html),
opening assertion, was checked on 2026-10-21: positive integer bases and
exponents, each exponent greater than two, and a prime common to all
three bases. It matches the local target without height or unit-base
exceptions. The nominated [AMS page](https://www.ams.org/profession/prizes-awards/ams-supported/beal-prize)
again returned HTTP 403; its current contents and rules were not read.
That failure does not block this geometric comparison.

Mathlib coverage of the complete model-construction/point-cover workflow
was not checked; no absence or formal verification is claimed. This turn
supplies source coverage and a bounded specialization specification, not
a new model, point list, rank value or integer exclusion.
