# Direct quartic arithmetic — source-approved certificate target

TARGET: Determine a certified maximal order and field discriminant for the quartic branch field of L110.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Dedekind index criteria, integral-basis algorithms, p-maximal orders and the exact polynomial coefficients; compared L133, ATTEMPTS/058 and the earlier ideal-backend source park. No exact-field certificate was found in the inspected material; this is not a novelty claim.
SOURCE_EVIDENCE: Inspected Conrad, Dedekind's Index Theorem, Theorem 1.4 and proof pp.1,5–7, Theorem 4.1 and proof pp.7–9, algorithm pp.9–10; Milne ANT v3.08 Proposition 2.11, Remark 2.25, Proposition 2.43 and algorithm pp.29,34,40–41; Stevenhagen, The arithmetic of number rings (2008), Lemma 6.4 p.221 and Section 9 pp.233–235 including Proposition 9.3 and proof.
COMPARISON: Established algorithms cover maximal orders without a quadratic tower or monogenic maximal-order hypothesis; the remaining work is exact-instance implementation and complete replay for L133's g, not new maximal-order theory.
GAP: No polynomial discriminant, exceptional-prime list, integral basis or terminal local certificate has yet been computed for this field.
REASON: Primary source coverage now supports one bounded arithmetic attempt; ideal/class/unit, Selmer, rank and point conclusions remain outside scope.
SCOPE: Exactly the saved target for K=Q(alpha), g(alpha)=0, g=X^4+64X^3+150X^2−32500X−109375, using L110, L132 and L133; complete exceptional-prime coverage, p-radical multiplier rings, integral-basis and discriminant replay. No backend reprobe or rank execution.

## Gap, use and local comparison

The main Beal gap remains the unexcluded primitive exponent families;
even this quotient route lacks rank bounds and point control. A certified
integer ring would make later ideal arithmetic meaningful in the actual
quartic branch field. It would not itself supply a descent or a rank bound.

L133 supplies the inverse maps alpha=25theta and theta=alpha/25;
L132 supplies irreducibility. Neither asserts maximality. ATTEMPTS/058
closes quadratic towers, not direct arithmetic. The narrowly inspected
2026-10-11 global-eleven ideal-lattice assessment and ATTEMPTS/025 record
missing backends and uncertified enumeration for a different field.
Their stops remain intact. This proposal uses exact rational/finite-field
linear algebra and no ideal-enumeration backend. No unfinished work is
replaced, and no cross-notebook input is used.

Queries included `Keith Conrad Dedekind index criterion p maximal order
pdf`, `J S Milne algebraic number theory algorithm ring integers
discriminant integral basis`, `ring of integers p maximal order algorithm
enumerate p integral basis Cauchy lattice`, and exact combinations of
`X^4+64`, `32500`, `109375`. Exact-coefficient searches yielded no matching
field certificate among returned material. Searches do not certify absence.

## Inspected standard inputs

[Keith Conrad, *Dedekind's Index Theorem*](https://kconrad.math.uconn.edu/blurbs/gradnumthy/dedekind-index-thm.pdf),
author-hosted 15-page version, accessed 2026-10-25. Theorem 1.4:
for integral primitive alpha with minimal polynomial f, factor f modulo
prime p into distinct monic irreducibles pi_i with multiplicities e_i.
Choose monic integral lifts and put F=(f−product pi_i^e_i)/p.
Then p divides the power-order index exactly when some repeated pi_i
divides F modulo p. This includes small primes and repeated factors.
Theorem 4.1 constructs an extra integer h(alpha)/p using a lift of
fbar/pi_i. Its proof treats primes over distinct factors and the same
factor, with both valuation inequalities in the latter case. The closing
examples explain why changing generators cannot replace general orders.
The pp.9–10 algorithm supplies the local-to-global assembly. These are
imported criteria, not field-specific results computed today.

[J. S. Milne, *Algebraic Number Theory*, v3.08, 2020-07-19](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
Proposition 2.11 tests integrality by the monic minimal polynomial over
an integrally closed base. Remark 2.25 gives the discriminant/index-square
identity for full integral lattices. Proposition 2.43, over a PID in a
finite separable extension, bounds the integer ring between an integral
basis lattice and its discriminant-denominator enlargement; its proof
uses embeddings and Cramer's rule. The following exhaustive-coset
algorithm is complete but explicitly impractical. Its huge global search
is not proposed here. With base Z and field Q, the PID, integral closure
and separability hypotheses hold. L133 supplies the integral primitive
generator. Exact arithmetic replaces approximate coefficient recognition.

[Peter Stevenhagen, *The arithmetic of number rings*, MSRI Publications
44 (2008), pp.209–266](https://library.slmath.org/books/Book44/files/08psh.pdf),
Section 9, pp.233–235, especially Proposition 9.3. For an order R and
prime p, form I_p/pR as the nilradical of R/pR: it is the kernel of an
iterated Frobenius with p^k greater than the algebra dimension. Set
R'={x in K : x I_p is contained in I_p}. Lemma 6.4's determinant trick
proves integrality; R is contained in R', which lies in (1/p)R and in
the p-maximal extension. Proposition 9.3 proves strict enlargement
whenever R is not p-maximal, by a largest-power argument on I_p.
Thus equality certifies termination, including ramified cases. The
subsequent construction computes R'=(1/p)ker(phi), where phi is
multiplication on I_p/pI_p; this is not multiplication on I_p/pR.
No restriction p>degree or squarefree reduction is imposed.

Stein's online Theorem 4.3.5 was inspected as a lead, but its omitted
maximality proof is not needed: Stevenhagen supplies the proof above.
Cohen's book and the original Pohst–Zassenhaus treatment were not read;
no theorem is attributed to an inspected passage of those sources.
Mathlib matching maximal-order algorithm coverage is not checked; no
absence or formal-verification claim is made.

## Approved bounded next attempt, not an executed derivation

Keep the exact TARGET. Reuse the existing field maps and irreducibility;
do not rederive or reapprove unrelated geometry. The intended deliverable
is a canonical exact-instance certificate, with hypotheses and citations.

- Compute the power-basis trace matrix and discriminant exactly. Factor
  it completely with independently checked primality and product identities.
  Any unresolved cofactor is a failed completeness obligation.
- For each prime whose square divides that discriminant, either certify
  the initial index is prime to p by Conrad's criterion, or construct
  successive p-radical multiplier orders using Stevenhagen. Retain exact
  bases, multiplication tables, Frobenius matrices, complete kernels,
  lattice inclusions and every terminal equality. Verify every basis
  contains 1 and is closed under multiplication. Do not assume monogenicity.
- Replay using separately constructed multiplication matrices and exact
  rational lattice membership; checking only candidate generators is
  insufficient. Check all omitted primes via the factored discriminant,
  every terminal multiplier equality, the assembled lattice, and both
  its trace discriminant and determinant/index-square relation.
- Before implementation set hard cumulative caps: 250000 factor/divisor
  trials, 128 strict order enlargements, 2000000 instrumented exact
  scalar operations, degree 4 field arithmetic and 4096 numerator/
  denominator bits. Account for generation and replay, failed trials and
  restarts. Print actual/cap values and certificate paths; retain full
  evidence on disk. These are safety limits, not predicted runtime.

Continue if all local certificates fit those caps and replay succeeds.
If factoring, saturation, lattice handling or verification hits a cap,
save partial evidence and stop without a maximality or field-discriminant
claim. Do not silently enlarge the search or substitute software output
for completeness. The next report must compare actual work with caps
and identify the first unresolved obligation. No discriminant value or
basis is asserted by this source review. This turn writes no lemma or
mathematical script; source approval and execution remain separate.
