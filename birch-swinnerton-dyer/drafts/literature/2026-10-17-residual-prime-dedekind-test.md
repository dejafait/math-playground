# One residual prime and nonmonic Dedekind test — proposed finite contract

TARGET: Search primes at most 10000 for the least divisor of the exact step-286 residual and, if found, certify L077's maximality verdict at that one prime using the nonmonic Dedekind criterion.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed search, primary comparison and duplicate/failure check in drafts/literature/2026-10-17-residual-cofactor-prime-review.md; this exact finite contract is newly written and requires separate next-turn approval.
SOURCE_EVIDENCE: Del Corso--Dvornicich--Simon, Acta Arith.120 (2005), Section 3 factor convention and Proposition 5, Section 4 Proposition 9/Theorem 2, pp.238--240, https://www.impan.pl/shop/en/publication/transaction/download/product/82018 ; finite-field factor certificates reuse Lenstra Section 5 Test 2, p.181, as imported in L067. Full scope and proof cases are recorded in the paired source comparison.
COMPARISON: Known results decide the prime-specific maximality question from exact supplied polynomial data. The only specialization is finite prime selection and production/replay of that data for L077; no new theorem, guaranteed divisor or runtime claim is proposed.
GAP: Actual divisor selection and polynomial certificates remain uncomputed; no full residual factorization, overorder, field discriminant, units/classes, faithful power classes or descent input follows.
REASON: A new, bounded local test replaces the disproved four-prime support mechanism. Finding no divisor or failing a cap ends this fixed route rather than inviting a larger search.
SCOPE: Exact audited L067/L077, unchanged signed discriminant and step-286 certificate; prime bound 10000, one least residual divisor, original nonmonic H and all its coefficients. No L026 or cross-notebook premise.

## Finite contract for approval

Recheck the step-286 certificate against the original signed discriminant,
all four exact division chains, terminal remainders and reconstruction;
reuse the existing complete replay rather than trusting its summary.
Retain hashes of all read originals. Use L077's audited basis.json for
all 49 coefficients of H, with its unchanged link to L067. This does
not require repeating the complete order-construction audit.

Enumerate all primes <=10000 by a complete elementary sieve, independently
check the list by trial division through each candidate's square root,
and retain exact residual division quotients/remainders until the first
prime divisor. If none exists, report only the full bounded exclusion
and stop. No larger bound, probabilistic primality or residual factoring.
The cap is a resource choice, not a predicted least-prime bound.

If a divisor p is found, certify its primality, exact divisibility and
leastness within the complete preceding list. Check p does not divide
343. Factor Hbar completely over F_p: retain distinct monic factors,
positive multiplicities, the leading unit 343 mod p, full reconstruction
and complete Rabin irreducibility witnesses for every factor. The
producer may use any exact finite-field factoring procedure; completion
within the caps is an experimental question. No unverified factor or
selected subset is enough. Inseparable multiplicities must be retained.

Let H_1 lift the product of all distinct factors, homogeneous at its
own degree. Let H_2 lift Hbar/H_1bar, including the leading unit,
homogeneous at complementary degree. Retain the exact integer identity
p H_3=H_1 H_2-H, all coefficients including zeros, and the full reductions.
Use Theorem 2 on the original H, without root scaling or a substitute
power order. Since H_1 has nonzero top coefficient modulo p, dehomogenized
gcd computation retains the homogeneous criterion without a missing
infinity factor. Check those degrees and coefficients explicitly.

Retain the monic gcd G of the three reduced polynomials, exact divisions
showing G divides each, and extended Euclidean identities expressing G
as their polynomial combination. The independent verifier must check
all coefficients, factor witnesses, reconstructions, divisions and
Bezout identities. Constant G certifies p-maximality of this order;
positive-degree G certifies its failure. Either is a complete verdict
for this one prime only. Do not construct or iterate an overorder.

Use one producer stage and one independent replay stage, each at most
180 seconds internal and 181 seconds external watchdog, aggregate new
output <=67108864 bytes. Save full certificates and partial evidence
under a new notebook-local scripts subdirectory. Print only outcome,
selected prime or tested bound, gcd degree, failures and artifact paths.
No retry, cap increase, repeated factor search with changed limits or
resumption after timeout. Missing evidence, inconsistent data, cap
failure or no divisor stops this contract. A complete bounded exclusion
is a negative selection result, not primality of the residual or
maximality of the order. Preserve all existing evidence.

Continue the local arithmetic route only on a completely verified
verdict; otherwise park this finite search and select a materially
different independently testable target. Even success supplies neither
all index primes nor complete global units/classes, L066's enclosure,
localization, rational membership or arbitrary-curve rank equality.
Mathlib matching coverage is not checked. This is known-method
reproduction and requires no general criterion reproof.
