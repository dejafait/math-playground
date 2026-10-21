# Separate fixed residual-prime audit — source scope approved

TARGET: Critically audit C077a's least residual prime and non-31-maximality verdict, including complete independent evidence replay and homogeneous-criterion applicability.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-statement search in drafts/literature/2026-10-17-residual-cofactor-prime-review.md and the approved residual-prime-dedekind-test.md; compared C077a, L077, histories 287--289, ATTEMPTS/040 and the independent verifier. They record production replay but no separate C077a audit. A targeted Lenstra/Test 2 search returned the same primary EPFL source; no new result is used.
SOURCE_EVIDENCE: Reopened Del Corso--Dvornicich--Simon, Acta Arith.120 (2005), Section 2 definition p.232, Section 3 factor convention/Proposition 5 pp.234--235, Section 4 Proposition 9/Theorem 2 and its full proof pp.238--240, https://www.impan.pl/shop/en/publication/transaction/download/product/82018 . Reuse prior inspected Lenstra Section 5 Test 2, p.181, recorded in L067 and the residual-cofactor assessment; current EPFL fetch failed, so no fresh inspection is claimed.
COMPARISON: The primary criterion covers the original nonmonic order and admissible homogeneous lifts, hence this fixed audit including a second admissible-lift computation. It does not certify stored arithmetic or turn production replay into critical audit. No general theorem reproof is needed.
GAP: No essential source gap remains within this fixed scope. Fresh complete replay, an independently computed alternative-lift gcd and qualified rejection/preservation checks remain unexecuted. No overorder, complete index-prime coverage, field discriminant or descent input follows.
REASON: Approve the saved audit target separately from its completed calculation. Coverage is reused; this process completion supplies no new mathematical evidence and is reported STALLED.
SCOPE: C077a with audited L067/L077, all 49 original H coefficients, unchanged signed discriminant, complete step-286 divisions and scripts/residual-prime-289/ evidence; one fixed audit at 31, no prime search extension, correction, L026 premise or cross-notebook input.

LITERATURE_REASON: The newly selected separate-audit target was REVIEW_REQUIRED at invocation start; its complete-evidence and independent-check scope needed comparison. Construction coverage is reused; further literature on this unchanged target is unnecessary.

## Primary scope and essential cases

The primary source is Del Corso--Dvornicich--Simon, *Decomposition of
primes in non-maximal orders*, Acta Arith.120 (2005), 231--244, linked
above. Its Section 2 assumes a Dedekind domain and primitive irreducible
F with nonzero leading coefficient, and defines R_F using 1 and truncated
leading-coefficient polynomials. Apply it over Z to the original H=343h
and exactly L077's basis; audited L067 supplies fieldness. Check these
premises in the audit; do not substitute a scaled-root power order or
assume the root globally integral.

Section 3 retains homogeneous factors, units and multiplicities, including
infinity. Theorem 2 allows lifts H_1,H_2 of the squarefree product and
complementary quotient, and H_3=(H_1 H_2-H)/31. Its homogeneous three-way
gcd criterion applies to this order. The inspected proof uses the radical's
multiplier order, the two polynomial divisibility conditions and their
lcm simplification on p.240; Proposition 9 gives the maximality equivalence.
Import these results. Enlargement construction and index are outside scope.

The later audit must check the claimed degrees 46,2,48 and the unit top
coefficients before using the affine gcd. H_3 may have smaller affine
degree, but must remain homogenized at degree 48. Retain the leading unit
in H_2. These are explicit applicability checks, not mathematics proved
in this source-review turn.

Reuse Lenstra, *Factorization of Polynomials*, Section 5, Test 2 (Rabin),
p.181, https://infoscience.epfl.ch/server/api/core/bitstreams/3154505c-23e7-4fd4-be73-e8c8b9c85951/content .
Its monic positive-degree test requires the terminal Frobenius condition
and coprimality at every prime divisor of the degree. Check full chains
and Bezout witnesses, including degree-one cases. The current fetch failed;
the unchanged adequate prior inspection is reused. Secondary search results
are not theorem evidence. Full matching Mathlib coverage remains unchecked;
no absence is inferred.

## Approved fixed audit contract

Read C077a's full proof and relevant producer/verifier code. Hash all files
in scripts/residual-prime-289/ and its four named original arithmetic inputs
before and after the audit. Preserve original bytes and reports. Use a new
notebook-local audit directory and disposable evidence copies. Recreate
the verifier's required relative layout or review a path-only adaptation;
never run its one-shot report writer against the occupied original path.
Reuse audited L067/L077 for field/order constructions, without repeating
their entire critical audits.

Run one fresh complete independent replay. Inspect all relevant evidence:
14077 step-286 divisions, four terminal remainders, sign, exponents and
reconstruction; original coefficient/hash links; every selected trial and
the complete prime list; all eleven factors, multiplicities, leading unit,
Frobenius and Bezout witnesses; integer lifts, all 49 H_3 coefficients,
homogeneous degrees, all gcd quotients and the three-way identity. Compare
the least-prime and nonmaximality conclusions with the write-up. Inspect
status and failures explicitly; exit code alone or a preview is insufficient.

For an independently discriminating check, construct second admissible
integer lifts by coefficientwise reducing stored H_1,H_2 to 0,...,30,
retaining their specified homogeneous degrees. Verify their reductions and
recompute the entire integer H_3 from original H. Use separate polynomial
arithmetic to compute the full three-way monic gcd by Euclidean division;
retain every remainder and final divisibility/Bezout witnesses. Only then
compare against the claimed G=T^2+24. This tests different lift arithmetic,
not just replay of the original identity. The source permits these lifts;
no lift-invariance lemma or new result is derived here. Any mismatch fails
the audit.

Use at most six isolated altered-evidence fixtures: one changed selected
trial quotient, factor multiplicity, Frobenius remainder, H_2 leading unit,
H_3 coefficient and gcd quotient. Run the applicable unchanged verifier
checks on disposable copies; record the actual rejection condition. Earlier
condition and hash-only rejections must be qualified, not described as
exercising later checks. Fixtures supplement complete unaltered replay;
they do not prove universal verifier correctness. Preserve stopped evidence.

Allow one fresh replay stage and one aggregate independent-check/rejection
stage, each <=180 seconds internally and <=181 seconds externally, with
new output <=67108864 bytes. Save complete certificates, actual/required
bounds, failures and paths. No retry, enlarged cap, second prime search
or overorder. Missing evidence, mismatch, timeout or preservation failure
leaves the audit unresolved and ends this fixed attempt; resource failure
alone does not mathematically refute C077a.

## Relevance, duplicates and decision

The main gap remains rank equality for arbitrary analytic order >=2.
Reliable audit of this fixed obstruction could validate the need for a
local correction before complete units/classes and a descent enclosure.
All index primes, actual correction, arithmetic generators, Selmer bounds,
localization, rational membership and complex-order comparison remain open.

The step-287 four-prime support failure remains intact. ATTEMPTS/040 stops
repetitive starting-order source confirmation, not the first audit of this
different verdict. Production replay is an audit input, not its duplicate.
Continue only with full applicability, replay, independent agreement and
preservation. Otherwise park the failed mechanism and select a materially
different independently testable target under its own coverage, without
expanding the prime search. Approval completes this saved assessment only;
mathematical execution is next turn. No evidence was replayed here.
