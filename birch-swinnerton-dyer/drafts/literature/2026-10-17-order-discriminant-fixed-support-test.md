# Fixed discriminant-support test — source scope approved

TARGET: Test whether L077's absolute order discriminant is supported on {2,3,7,389} by complete exact division, retaining all valuations and the residual cofactor.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 281 starting-order/maximality coverage, step 283 construction and step 285 audit; inspected L077 and ATTEMPTS/040. Searched exact nonmaximal-order index/discriminant terminology and Milne discriminant/index-square terminology; direct primary statements below cover the mechanism, with no inspected executed four-prime test or novelty claim.
SOURCE_EVIDENCE: Del Corso--Dvornicich--Simon, Acta Arith. 120.3 (2005), 231--244, publisher PDF https://www.impan.pl/shop/en/publication/transaction/download/product/82018 ; directly read p.231 nonmonic index rule, p.232 hypotheses/order definition and p.234 complete Proposition 4 proof. Milne, Algebraic Number Theory v3.08 (2020-07-19), https://www.jmilne.org/math/CourseNotes/ANT.pdf , Lemma 2.23 and Remark 2.25, printed pp.33--34, statements and full determinant proofs inspected.
COMPARISON: The known index-square identity applies to L077's nonmonic order and bounds possible index primes by order-discriminant primes. Euclidean division and exact reconstruction decide the fixed support claim without general factorization. Sources establish the method, not this integer's valuations or cofactor; no new theorem or general reproof is needed.
GAP: No essential source gap remains for the bounded test; actual valuations/cofactor remain uncomputed. Maximality, field discriminant, complete units/classes and all descent/rank conclusions remain outside scope.
REASON: Separate review closes the missing nonmonic index-discriminant comparison for the changed finite target; ready starting-order coverage is reused and repetitive source confirmation stays parked under ATTEMPTS/040.
SCOPE: Audited L067 and L077, the full signed order discriminant and complete exact evidence; no L026 premise, cross-notebook input, assumed ramification support, general factorization or maximal-order construction.

LITERATURE_REASON: The new fixed-support target required the previously missing precise index-discriminant comparison; this is its separate approval, not repeated confirmation of the already audited starting-order construction.

## Approved finite contract, not executed

Use the entire signed integer from
`scripts/seven-torsion/nonmonic-order-283/discriminant.json`, with its
step 285 audit and input hashes. Start with its positive absolute value.
For each of the explicitly prime integers 2,3,7,389, divide as long as
the remainder is zero, preserving the exponent and exact residual.
Retain every division, the full final cofactor and the reconstruction
of the original absolute integer from the four powers and that cofactor.
An independent replay must verify every division, the reconstruction and
nondivisibility of the final cofactor by all four primes. The negative
sign of the original order discriminant is retained separately.

Use one aggregate stage with 30 seconds internal, 31 external and at most
16777216 new bytes, including production and complete independent replay.
No retry, enlarged prime set, factoring of the cofactor or cap increase.
The stopping decision is cofactor=1 versus cofactor>1. The former proves
only complete order-discriminant support on the four primes; the latter
refutes that finite support claim and preserves its exact obstruction.
It does not refute BSD or the usefulness of L077. Neither branch produces
local/global maximality, field discriminant, complete units/classes,
faithful power classes or Selmer/rational-direction evidence.

Plausible downstream use is to delimit possible index-prime work before
attempting radical/idealizer certificates. That use is covered by the precise
index-discriminant comparison recorded below. No
ramification-support theorem is assumed or proposed for derivation here.
The small prime list is a discriminating hypothesis motivated by the
model scaling, seven-torsion degree and bad prime 389, not a known
consequence of those data. Extra order primes remain possible.

## Source applicability and limits (step 286)

Del Corso--Dvornicich--Simon take a Dedekind ring and primitive irreducible
polynomial with nonzero leading coefficient. Their Section 2 order and
Proposition 4 match L077 over Z with H=343h, degree 48. Their p.231
index rule explicitly includes the nonmonic case. This imports a known
identity; no integrality of t or monogenic maximal order is required.

Milne Remark 2.25 independently states the lattice index-square formula
for a full-rank submodule of a finite free Z-algebra with nonzero trace
discriminant; its proof uses the determinant of the integral basis-change
matrix, with Lemma 2.23 supplying discriminant transformation. Here the
ambient algebra is O_K and the submodule is audited O_H. L067 supplies
the number field and L077 supplies the full-rank integral order. Thus the
applicable identity is disc(O_H)=[O_K:O_H]^2 disc(O_K). No basis of O_K
needs to have been computed to import this identity. Its use only bounds
possible index primes; an order-discriminant prime need not divide the
index, and support does not certify maximality. No ramification theorem
or Selmer premise is imported for this test.

The finite arithmetic uses the standard Euclidean division algorithm.
The proposed replay must check whole integer values, all successful exact
divisions and each terminating nonzero remainder, and reconstruct the
original signed value. Any capped or incomplete run is inconclusive.
The four stated integers must be certified prime by trial division up to
their square roots (for 389, primes through 19 suffice); this is a finite
input check, not a new mathematical lemma. Retain zero valuations too.
No division, primality test, support calculation or script was executed in
this literature turn. Future production/replay is REPRODUCTION under this
SPECIALIZE assessment; source citations cannot validate its saved data.

Duplicate/failure check: L077 and its full separate audit establish the
order discriminant, with no factor-support conclusion; step 281 treats
maximality criteria but does not evaluate this support. ATTEMPTS/040 parks
unchanged starting-order source confirmation, not this independent finite
test. General factorization and seven-only maximality remain outside the
contract. A larger cofactor abandons only the proposed four-prime support
claim and must not be silently factored or met by enlarging the list.
Full/supporting Mathlib coverage remains unchecked; no absence is inferred.

The review approves this unchanged exact Next action for the following
research turn. No lemma, mathematical script, DAG or argument was changed.
The main gap remains arbitrary analytic-order-at-least-two rank equality;
unit/class completeness, faithful power classes, local descent bounds,
successful localization and rational membership remain unresolved.

