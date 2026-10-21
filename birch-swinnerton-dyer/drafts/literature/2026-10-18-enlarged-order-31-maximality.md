# Enlarged-order 31-maximality — source and certificate assessment

TARGET: Assess a bounded 31-maximality test for L078's enlarged order using its full multiplication table and radical multiplier criterion.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-method searches and primary coverage in 2026-10-17-prime-local-overorder-quotient.md and its construction/audit assessments; compared canonical L078, history 297 and ATTEMPTS/041. Retrieved the publisher chapter again only to check the changed-order hypotheses, maximality stopping case and complete lifting paragraph; no broad discovery search was needed.
SOURCE_EVIDENCE: Peter Stevenhagen, The arithmetic of number rings, in Algorithmic Number Theory, MSRI Publications 44 (2008), pp.209--266, Lemma 6.4 p.221; Section 9 pp.233--235, equation (9-2), Proposition 9.3 with proof and following action/kernel/lifting paragraph p.235, https://library.slmath.org/books/Book44/files/08psh.pdf#page=27 . Primary text inspected includes the p-maximal-extension definition, both nilradical cases and strictness proof; exact-method source comparison is retained in 2026-10-17-prime-local-overorder-quotient.md.
COMPARISON: The source explicitly treats nonsimple orders after enlargement. Audited L078 supplies such a full order in the same number field; neither monogenicity nor an identity basis vector is required. The criterion covers a fresh test, but the old kernels, gcd and index do not decide this changed input.
GAP: No new Frobenius, radical basis, action kernel, numerator preimage or equality/index witness has been calculated for O'. Runtime and certificate size remain unproved. Other index primes, global maximality, units/classes, descent and BSD rank equality remain unresolved.
REASON: This supplies the previously missing changed-order applicability and bounded decision contract, using known results only. A later finite implementation/replay is justified as reproduction; this literature turn proves no new lemma and runs no mathematical script.
SCOPE: Audited L067/L077/C077a/L078, entire degree-48 field with original H=343h, L078's full integral basis, identity coordinates, both transports and multiplication table, at prime 31 only. No stopped step-293 power, L026, new prime, cross-notebook input or iteration after this test.
COVERED_TARGET: Test and independently verify whether L078's enlarged order is 31-maximal using the full radical action and exact integral preimages under one aggregate 180/181-second, 134217728-byte contract.
LITERATURE_REASON: L078 changes the input order beyond the earlier first-correction scope. Essential stopping-case applicability and a complete certificate contract for this basis were uncovered at invocation start; ready general source coverage is reused.

## Gap, relevance and source application

The main gap remains rank E(Q)=ord_(s=1)L(E,s) for arbitrary curves
of analytic order at least two. The intermediate target is one certified
31-maximality decision for O'. This could settle or sharpen one local
order obstruction before complete unit/class arithmetic for L066. It
leaves independent global arithmetic, local descent, rational membership
and complex-order comparison gaps; no BSD candidate is proposed.

The cited Section 9 allows any order R, with p not invertible. It obtains
the radical from an iterated Frobenius kernel and computes its multiplier
through the action on the full I/pI. Proposition 9.3 and its following
paragraph give the equality stopping test and the integral lifting rule.
The proof covers strict nonmaximality; the preceding text covers a zero
nilradical and distinguishes ramification from singularity. These are
imported results, not a proposed reproof.

Set R=O' from audited L078 and p=31. It is a full Z-order in audited
L067's field, so 31 is not invertible; its rank is still 48. Section 9's
Frobenius threshold permits two iterates since 31^2>48. Use the actual
identity vector from L078, not e_0. This is the necessary specialization
of the cited algorithm, not a computed nilradical or stopping decision.
The nonmonic Del Corso--Dvornicich--Simon formula was needed to identify
the first correction; it is not reapplied to O' as though O'=O_H.
No new theorem, monogenic presentation or ideal power is needed.

## Complete finite decision contract

The later attempt must retain all rank-48 coordinates, including zeros.
Use a fresh output directory and preserve input hashes before and after.
The following are certificate requirements, not asserted identities
already evaluated on the changed order.

1. Load the full audited O' basis, both rational inverse transports,
   actual identity coordinates and all 110592 product slots. Check the
   transports and identity on both sides. Independently replay each
   product in the original H field, retaining the factor 31 in L078's
   polynomial representation; an abstract table alone is insufficient.
2. Compute both 48-by-48 Frobenius matrices on O'/31O'. Independently
   reconstruct them by exact powering and verify composition. Replay
   full invertible elimination, pivots and every terminal zero row to
   certify the complete kernel of the second iterate; check membership
   against the original matrix. No rank or kernel dimension is prescribed.
   If reducing rational field transports modulo 31 encounters a nonunit
   denominator, do not invert it: use the verified integral O' table and
   exact rational field checks before reduction instead. Powers must
   start with the actual identity vector. Exact integers are preferred;
   fixed-width arithmetic needs a new justified bound for this table.
3. Lift the full kernel and append all 31e_i in O' coordinates to form
   S_I. Give a rank-48 integral basis J, its rational inverse, and integer
   matrices C_I,D_I satisfying J=S_I C_I and S_I=J D_I. Check both inverse
   products. This proves the whole global radical preimage, not only a
   basis over Z_(31). It also covers an empty kernel without a special
   unverified shortcut.
4. For every O' basis element compute its entire integral action A_i
   in the J-basis. Check every slot of J A_i=L_i J over Z before reduction,
   using independently verified field/table multiplication. Stack all
   2304 action rows into the 2304-by-48 matrix for O'/31O' acting on
   I'/31I'. Replay complete elimination and full kernel membership as
   in item 2. Neither I'/31O' nor O'/I' is a substitute.
5. Lift that entire action kernel and append 31e_i to form S_N. Give
   a full integral basis Q, two-sided integer generation witnesses and
   both rational inverse identities, exactly as for J. Retain M=Q/31
   and its inverse T=31 Q^(-1). Verify T is integral, both inverse products,
   and that it transports every old basis vector, including the identity.
   Compute the full exact determinant of T with verifiable operations;
   check the index against 31^d, where d is the certified action-kernel
   dimension. The source lifting rule identifies this lattice as the
   multiplier order. Do not assume Q=J or index 961.
6. Equality requires the complete N=31O' lattice equality, checked by
   integral containment witnesses in both directions, and index one.
   Apply the cited stopping criterion only after all preceding checks.
   If the index is larger, supply an explicit kernel lift whose division
   by 31 has a nonintegral O' coordinate and verify that its product with
   every radical basis element lies in I'. This witnesses nonmaximality
   only. Retain the full numerator lattice and index in either branch;
   do not iterate or compute products in a subsequent enlarged basis.

One aggregate execution, including production and independent replay,
may take at most 180 seconds internally and 181 seconds externally,
with at most 134217728 new bytes in total, including reports and logs.
Use a single watchdog/budget covering both components, not two renewed
allowances. Complete source arithmetic must be reconstructed independently;
matching summaries or hashes alone are not replay. Report actual/required
slot counts, both ranks, index, failures and artifact paths. At a failed
identity, timeout or byte cap preserve partial evidence and stop without
retry, resumption or a larger allowance. No malformed-data fixtures are
required for this first decision attempt. No success is inferred from
prior small runtime or from the existence of the algorithm.

## Duplicate/failure comparison and continuation test

The prior quotient/construction scope explicitly excludes a second-order
test. L078 and its separate audit certify the first correction only;
C077a concerns the old order. Thus this is a new fixed instance of a
known method, not a duplicate theorem or claimed mathematical novelty.
ATTEMPTS/041's full-power byte-cap failure remains permanently parked;
the proposed action uses no power expansion or partial step-293 input.
No source blocker was found: one PDF screenshot request timed out, but
the complete relevant primary text, including the proof and both cases,
was available. There is no unread essential lead for this narrow target.

Continue to a single later calculation because the source supplies the
complete stopping decision in this changed basis and both integral
preimages have finite witness requirements. Equality would settle only
31-maximality; a strict multiplier would settle only nonmaximality of O'.
At a cap or failed witness, abandon this execution and record the precise
failure before selecting a materially different test. A positive decision
still needs a later separate critical audit. The new continuation scope
is ready for the supervisor's separate approval next turn; no dependent
calculation occurs in this review. Mathlib matching coverage is not
checked; no absence is inferred. No lemma, mathematical script, DAG or
argument overview is changed.
