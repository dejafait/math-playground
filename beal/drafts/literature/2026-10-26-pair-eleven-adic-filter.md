# Fixed-witness 11-adic refinement — source coverage

TARGET: Test whether the 11-adic Kummer condition removes at least one dimension from L140's real-filtered supported group, using only the span of its 39 saved global witnesses.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the pair-rank and real-filter assessments and ATTEMPTS/050,059–061; inspected backend stops ATTEMPTS/045,052. Searched Stoll/Schaefer odd-prime Jacobian local-image terminology and exact coefficients 76835,67760,1581228000,2196150000 with Kummer/Jacobian/curve; no inspected exact-instance answer was identified. The general complete local algorithm is stronger than the conditional branch-first test below.
SOURCE_EVIDENCE: Stoll, Acta Arith. 98 (2001), DOI 10.4064/aa98-3-4, Section 4 pp.249–251, Lemmas 4.1,4.3,4.4 and their proofs, Section 6 pp.267–272 through the extension/generator discussion; Clark's 161-page Algebraic Number Theory II notes, Proposition 2.9/Corollary 2.10 p.65 and Proposition 2.20 p.72, Exercise 2.11/Theorem 2.24 and proof p.73. These passages were read; previous Hensel coverage is reused. Exact links and qualifications below.
COMPARISON: Known theory gives an exact local Kummer dimension and completeness when actual divisor images span it. It does not evaluate this model's branch image, the 39 localizations or their real-compatible combinations. A conditional branch-first test avoids global unit/class completion and all point sampling; a smaller uncertified span may not be used to claim exclusion.
GAP: Essential theorem coverage is sufficient. Certify the field/uniformizer, branch image and dimension matching, local square classes and real-compatible quotient elimination in the next mathematical attempt. No new 11-adic dimension, class or rank improvement is established here.
REASON: Completes missing finite-place coverage for the unchanged target and approves only the capped branch-first specialization, with explicit failure exits.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; the approved real-place audit did not cover finite local fields or a complete 11-adic image.
SCOPE: Exactly TARGET on L138's unchanged odd model, only L140's 39 saved global witnesses, one fixed branch-divisor candidate and one fixed uniformizer candidate; conditional completeness and caps below. No backend, unit/relation-box search, extension-field point search or other local prime.

## Relevance and continuation test

The main gap is exclusion of all residual positive primitive Beal
solutions. The intermediate target is one additional codimension after
the accepted real filter. This could improve the genus-two rank bound
for later point control. Even a successful test leaves the sufficient
rank bound one, points, marked lifting, degree-nine and integer recovery,
L095's retained systems and all other signatures as separate obligations.

Use L138's exact G=(X−9075)H and alpha/eta transport, L135's integral
basis and prime data, L136's accepted ideal records, L137's seven support
indices, L139's supported norm kernel and L140's complete real image W
and 39 saved witnesses. Keep the rational coordinate and signed inverse
norms. No cross-notebook input is needed. Preserve unfinished L108.

Success requires an actual product of these witnesses, real-compatible
with W, whose localization is outside a proved complete local Jacobian
image. If every real-compatible combination satisfies the complete local
condition, stop the fixed-span test without inferring full global
saturation. If field certification or the branch completeness gate
fails, stop with that precise obstruction; no sampled local absence is
an obstruction. No enlarged box or renewed backend preflight follows.

## Primary theorem comparison

[Michael Stoll, *Implementing 2-descent for Jacobians of hyperelliptic
curves*](https://www.impan.pl/shop/en/publication/transaction/download/product/83397),
Acta Arith. **98** (2001), 245–277, DOI 10.4064/aa98-3-4,
Section 4 assumes monic integral squarefree odd-degree f. Lemma 4.1 gives
the natural injection into the full algebra norm kernel. Lemma 4.3(2)
supplies the branch-factor value; 4.3(3) gives two-torsion dimension.
Lemma 4.4(1), including bad odd primes, gives local-image dimension m−1,
where m counts irreducible local factors. Section 6, pp.267–268, gives
infinity value one and branch values; reaching the known dimension
certifies completeness. Lemma 6.1 and its full proof permit divisors of
degree at most the genus. Lemma 6.3 and its full proof cover ordinary,
branch-neighborhood and nonintegral coordinates. The complete recursion
and termination discussion, pp.270–272, can require extension fields;
rational curve points alone need not generate. Import these results.

L138 already verifies the model hypotheses and exact alpha/eta transport.
L135/L137 identify the prime above 11 and its residue field. The next
attempt must certify the full local factorization before using m; a
repeated residue factor alone does not establish irreducibility. Evaluate
the cited branch formula at the rational root 9075 in both algebra
coordinates. Require the resulting span to attain the theorem's dimension;
do not assume that rational two-torsion survives modulo twice the local
Jacobian. Dimension matching covers all divisor classes, including
quadratic divisors and infinity, so no point enumeration is needed when
this branch-first gate succeeds. If it fails, the approved test ends.
This review computes neither the local dimension nor the branch class.

[Pete L. Clark, *Algebraic Number Theory II: Valuations, Local Fields and
Adeles*](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
161-page author-hosted version, accessed 2026-10-26, revision date not
identified: Proposition 2.9 and full proof/Corollary 2.10, p.65, give the
DVR, root uniformizer and residue field for an Eisenstein polynomial over
a DVR. Proposition 2.20 and proof, p.72, split off the valuation.
Exercise 2.11, p.73, states the Henselian odd-residue square-class
dimension; Theorem 2.24 and its proof provide the local-square input.
Use the standard Hensel square criterion: even normalized valuation and
square unit residue characterize nonzero squares at odd residue
characteristic. Keep both bits. Exercise 2.11 is an exercise, not a
separately proved theorem in these notes. The existing eleven-adic
assessment's inspected Hensel coverage is reused, without reproof.

The only uniformizer candidate is alpha+5: next turn check g(U−5) for
Eisenstein at 11 and bind the resulting DVR/residue map to L137's prime
and L138's eta. This is a planned coefficient test, not an assertion
computed here. If it fails, stop without a new uniformizer search. Exact
valuations, normalized unit residues and transport remain instance work.
No novel general local-field theorem is needed or proposed.

## Known results, duplicates and failures

Reuse `2026-10-20-pair-jacobian-rank-bound.md`: full descent requires
arithmetic not supplied by its parked backend route. The real-filter
assessment's stronger general signature comparison does not give this
finite local image. Reuse only the documented Hensel coverage of
`2026-10-17-primitive-eleven-two-descent-image.md`; that assessment's
cubic and correlated fiber are different. Its local image cannot be
imported. A Bruin–Stoll curve-point image cannot replace a Jacobian image.

ATTEMPTS/045,052 preserve global-backend blockers. ATTEMPTS/050 exhausts
a bounded point detector, not this branch-divisor image test.
ATTEMPTS/059,060 stop their relation-box/localization tests; ATTEMPTS/061
stops a dimension-only shortcut. None determines this finite-place
restriction. L140 saturates its real norm quotient; the new test must
first enforce W on witness combinations before counting further losses.
No stop evidence is removed and no backend probe is made.

Queries actually used include `Stoll Implementing 2-descent Jacobians
hyperelliptic curves local image odd p lemma 4.4`, `hyperelliptic Jacobian
local 2 descent image odd prime algorithm Schaefer Stoll`, `"76835"
"Kummer"`, `"76835" "Jacobian"`, `"67760" "1581228000"`, and
`"2196150000" curve`. No matching exact-instance theorem was identified
in inspected material; this does not establish novelty. Schaefer and the
full extension-classification references remain uninspected leads, not
essential missing sources for this conditional branch-only plan.
Matching Mathlib local-Jacobian coverage was not checked; this is not
evidence of absence.

## Approved bounded mathematical attempt

1. Load the complete relevant model, prime and 39 witness records from
   L138/L140 certificates. Bind bases, signed inverse norms and real
   coordinates; reuse support without regenerating the box.
2. Certify only the fixed shifted polynomial, local field, residue map
   and full local factorization. Apply the dimension theorem only after
   its hypotheses are checked; retain full coefficient evidence.
3. Evaluate the rational branch-divisor candidate using the cited formula,
   including both product coordinates and infinity. Save exact
   representatives, valuations and unit residues. Require its span to
   attain the required local-image dimension. Otherwise stop without a
   local obstruction claim. No point sampling or extension enumeration.
4. Localize each saved global class with exact field arithmetic and
   justified normalized valuations/residue reduction in the same product
   coordinates. Check signed norms and multiplicativity. Rational residue
   or valuation parity alone cannot replace the quartic unit bit.
5. Find a coefficient-space basis of combinations of the 39 signs lying
   in W, then their local images modulo the certified complete image.
   No global independence claim is needed: save each coefficient vector
   and recompute every asserted obstruction as an actual product.
6. Positive quotient rank permits an additional codimension argument by
   naturality and rank-nullity on the real-filtered ambient group. Keep c
   explicit and compare any resulting rank bound with one. Zero quotient
   rank ends this fixed-span test, not all local filtering.

Caps: four field coordinates, exactly 39 global input columns and one
branch candidate, at most 39 coefficient-kernel basis vectors, matrices
at most 39 by 39, no enumeration of 2^39 products; absolute normalized
valuations at most 128; rational numerator/denominator bit length at most
4096; at most 100000 exact field arithmetic operations per producer or
replay. These are explicit failure caps, not guaranteed successful bounds.
Stop and preserve any exceeded cap. Save full certificates and an
independent replay, printing actual/required dimensions, quotient rank,
caps, failures and paths. No mathematical program runs in this turn.

This literature step changes essential source coverage only. It derives
no local factorization, image, witness obstruction, filtered rank bound
or Beal result. General known results are cited; only their precise
finite specialization and certification remain. Newly approved scope is
for the exact unchanged target, not any broader local-image algorithm.
