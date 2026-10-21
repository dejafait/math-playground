# Residual cofactor prime and maximality route — source comparison

TARGET: Review primary results and assess a bounded route from the exact residual cofactor in step 286 to one prime-specific maximality test for L077's order.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared step 281 maximal-order source review, step 286 support assessment, step 287 negative result, L077's hypotheses and L067's finite-field certificate source; targeted local searches for residual-cofactor, trial-division and Dedekind tests found no executed matching test. Searched “Dedekind criterion p maximal order polynomial gcd f gh p index theorem”; inspected the primary nonmonic criterion below rather than relying on search snippets.
SOURCE_EVIDENCE: Del Corso--Dvornicich--Simon, Decomposition of primes in non-maximal orders, Acta Arith. 120 (2005), 231--244, https://www.impan.pl/shop/en/publication/transaction/download/product/82018 ; Section 2 hypotheses, Section 3 factor conventions and Proposition 5 infinity case, Section 4 Proposition 9 and Theorem 2 with its full proof, printed pp.238--240, inspected. Reused Milne's index-square coverage from step 286 and Lenstra Section 5 Test 2 (Rabin), p.181, already imported in L067.
COMPARISON: Theorem 2 decides maximality of precisely the nonmonic order at any supplied prime by a homogeneous three-polynomial gcd. It does not produce a prime dividing the 483-digit residual. A fixed small-prime search can supply that missing input without assuming residual primality or completing its factorization; success or failure remains uncomputed.
GAP: No prime divisor of the residual, finite-field factorization for a selected prime or maximality result is established. A bounded certificate attempt is source-covered, with no guarantee of finding a prime or finishing within its caps. Full index-prime coverage, units/classes and descent/rank conclusions remain independent.
REASON: The failed four-prime support hypothesis changed the essential input: the next test must select and certify a residual divisor before any local maximality assertion. This source comparison supplies a concrete discriminating route, without reviving the refuted support claim or repeating starting-order confirmation.
SCOPE: Audited L067/L077 and exact step-286 residual only; one newly selected prime, no complete integer factorization, overorder iteration, global maximality, L026 assumption or cross-notebook premise.

LITERATURE_REASON: The changed residual-divisor hypothesis needs a prime-selection contract and exact applicability of the local criterion. Existing starting-order coverage is reused; additional source work addresses this previously unassessed continuation only.

## Primary criterion and applicability

Use Del Corso--Dvornicich--Simon's notation F for a primitive irreducible
polynomial over a Dedekind domain R, with nonzero leading coefficient;
R_F is their nonmonic order. Section 3 factors the homogeneous reduction
into distinct irreducibles with multiplicities. Theorem 2 takes H_1 to
be a homogeneous lift of their product without multiplicities, H_2 a
lift of the quotient Fbar/H_1bar, and H_3=xi(H_1 H_2-F), where xi
is a uniformizer of the inverse prime ideal. The order is p-maximal
exactly when the homogeneous gcd of their three reductions is constant.
Proposition 9 identifies this with stabilization of the radical's
multiplier order. Theorem 2 also describes the first enlargement and
its index; neither will be constructed in the proposed test.

The inspected proof on pp.239--240 characterizes the multiplier ideal
by two containment conditions. The first forces the squarefree factor
to divide its polynomial representative; the second reduces to the
least common multiple of H_1 and (H_1/gcd(H_1,H_3))H_2. Its displayed
simplification gives F/gcd(H_1,H_2,H_3). The argument treats the
nonmonic order, rather than silently replacing it with Z[t]. Section 3,
Proposition 5 explicitly covers a factor at infinity by reciprocal
polynomials. These are imported results, not new proofs in this step.

Apply the theorem with R=Z, F=L077's H=343h and its entire degree-48
field. L067 supplies irreducibility and L077 supplies precisely R_H.
For a prime divisor of the step-286 residual, the already certified
nondivisibility by 7 ensures the leading coefficient is a unit modulo
that prime. Thus the Section 3 factorization has no infinity factor.
Do not change the order or assume t globally integral. Compute with
the original integral H and homogenize all lifts at their specified
degrees. The normalization unit in Hbar must be retained in H_2;
replacing Hbar with its monic associate and forgetting this unit is
not an authorized specialization.

For verification of a finite-field factorization, reuse L067's source:
Lenstra, *Factorization of Polynomials*, Section 5, Test 2 (Rabin),
printed p.181, https://infoscience.epfl.ch/server/api/core/bitstreams/3154505c-23e7-4fd4-be73-e8c8b9c85951/content .
The monic degree-d test requires X^(p^d)=X modulo the candidate and
unit gcd with X^(p^(d/l))-X for each prime l dividing d. Record complete
power remainders and Bezout witnesses, also for degree-one factors.
This test certifies supplied factors; it is not an asserted fast
factorization algorithm. Full multiplication including the leading
unit and multiplicities must reconstruct Hbar. No new irreducibility
theorem or reproof is needed.

## Input evidence and duplicate/failure comparison

The selected full value was read with the bounded inspector at /cofactor,
using PYTHONINTMAXSTRDIGITS=20000 for the containing 6870-digit input.
It is the exact 483-digit integer in
`scripts/order-discriminant-support-286/certificate.json`, not a rounded
preview or a claimed prime. This step performs no arithmetic on it.
The inspector's default conversion initially failed on the containing
integer; this is an inspection limit, not mathematical evidence.

Step 287 already refutes support on {2,3,7,389}. The new search does
not repair that hypothesis by enlarging its list: it seeks exactly one
prime for a different local question. ATTEMPTS/040 parks repetitive
starting-order confirmation, not this local criterion. Step 281 had
the general maximality framework but no residual or selected prime;
L077 certifies ring closure and an order discriminant only. None is
a duplicate local maximality certificate.

## Decision and downstream use

The route is feasible as a bounded, independently checkable experiment,
not as a guaranteed successful prime extraction or global algorithm.
Its intermediate target is one certified residual prime and the
three-polynomial maximality verdict at that prime. The complete finite
contract is in `2026-10-17-residual-prime-dedekind-test.md`. It awaits
separate next-turn approval; no calculation or lemma was produced here.
A local verdict could determine whether this starting order needs
correction at that prime before complete global arithmetic is attempted.
It neither bounds all index primes nor completes any unit/class or
Selmer certificate. The arbitrary-curve rank gap remains unchanged.
Mathlib coverage of the complete nonmonic criterion has not been checked;
no absence claim is made.
