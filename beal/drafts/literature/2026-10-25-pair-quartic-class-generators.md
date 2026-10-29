# Finite class-group generator certificate: source assessment

TARGET: Determine a certified Minkowski-bound prime-ideal generating set for the class group of L133's quartic field.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Milne algebraic number theory Minkowski ideal class bound and Stevenhagen number rings prime ideals finite algebra index; compared local L133/L134, the degree-36 workload assessment and ATTEMPTS/019,045,058. No inspected source gives this quartic's evaluated generator list.
SOURCE_EVIDENCE: Milne ANT v3.08 (2020-07-19), pp.14-15 ideal correspondence, Theorem 3.41/Remark 3.43 pp.62-63 with proof, Proposition 4.2 pp.69-70, Theorem 4.3 p.70 with proof pp.79-81; Stevenhagen (2008), Section 8 pp.228-232, Theorems 8.2/8.4 and proofs, including singular-prime Example 8.3.
COMPARISON: Standard unconditional theorems cover finite class generation and ideal enumeration; only exact instance certification remains. No class relations, units or rank result is imported.
GAP: Compute and replay the signature, rigorous integer norm cutoff, complete small-prime list and all required maximal-order prime ideals, including power-order index primes 2,3,5.
REASON: Essential coverage is now inspected; a bounded exact specialization can avoid the unavailable class-group backend. This is a source-review advance, not a new mathematical theorem or evaluated factor base.
SCOPE: Exactly TARGET using L133's field and audited L134's basis, product table, index and discriminant; signature/bound and complete prime-ideal enumeration with independent replay. No class presentation, unit basis, descent, ranks or point computation.
LITERATURE_REASON: The target entered this invocation as REVIEW_REQUIRED; its essential generation and exceptional-prime coverage was unread.

## Relevance and comparison

The main gap is primitive Beal exclusion across residual signatures;
on this route quotient ranks and point control are missing. A certified
finite generating list could support class relations and later supported
descent. It leaves those obligations and units independent and unresolved.

L133 identifies the degree-four field defined by
X^4+64X^3+150X^2-32500X-109375. Audited L134 supplies the maximal
basis, multiplication table, discriminant 2874960 and power-order index
937500=2^2*3*5^7. These are the only mathematical local inputs.
No cross-notebook theorem is used. Neither lemma already lists the
requested primes. ATTEMPTS/058 excludes a quadratic tower, so this
plan stays in the absolute field. ATTEMPTS/019's degree-36 cutoff
failure and ATTEMPTS/045's missing full-class backend do not decide
this separate small-degree finite enumeration. No backend reprobe,
installation or reopening of the parked rank computations is proposed.
Unfinished L108 remains untouched.

## Inspected primary inputs

[J. S. Milne, Algebraic Number Theory, v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorem 4.3, p.70: every ordinary ideal class of a degree-n number
field has an integral representative of norm at most
(n!/n^n)(4/pi)^s sqrt(abs(Delta_K)), where 2s counts nonreal embeddings.
The proof pp.79-81 uses the ideal lattice and norm cancellation;
Proposition 4.2 gives multiplicativity. Theorem 4.4's discussion p.71
uses prime factorizations to enumerate representatives. Theorem 3.41,
Remark 3.43 and their proof pp.62-63 give complete factorization by
irreducible polynomial factors when the index is prime to p. The ideal
correspondence and field-quotient criterion are on pp.14-15.
These statements apply to ordinary classes without GRH or normality.

[Peter Stevenhagen, The arithmetic of number rings](https://library.slmath.org/books/Book44/files/08psh.pdf),
MSRI Publications 44 (2008), Section 8 pp.228-232, Theorem 8.2 and
proof distinguish regular and singular power-order primes. Example 8.3
explicitly shows that a singular prime may split upon normalization.
Theorem 8.4 and proof give sum(e*f)=n for an order regular above p.
Thus a polynomial factor list at an index prime cannot simply be
asserted to describe the maximal order. Read the exceptional cases,
not just the generic theorem. These are standard imported inputs;
there is no need to reprove their general theory.

## Exact instance contract for the next mathematical turn

The following is a proposed verification specification, not a performed
calculation or a derived quartic result. Its new ready assessment must
receive the supervisor's separate next-turn approval before execution.

1. Bind the complete L134 data to the certificate. Seek four disjoint
   rational sign-change intervals for g, using at most 4096 exact
   evaluations; if successful, degree four certifies the signature.
   Otherwise stop this implementation and record the missing signature
   certificate rather than assume total reality.
2. Certify an integer upper norm cutoff U from the theorem with rational
   inequalities, retaining equality at endpoints. A conservative superset
   is allowed; no decimal rounding proof. Continue only if U<=300.
   This is an operational cap, not a claimed evaluated bound.
3. Enumerate all rational primes through U with complete trial-division
   evidence. At p not dividing the recorded index, factor g modulo p,
   retain multiplicities, reconstruct the product, and certify every
   factor irreducible. Since degrees are at most four, exhaustive monic
   divisor tests of degrees at most half the factor degree suffice.
   Lift (p,h(alpha)) as O_K-ideals in the fixed integral basis; save
   generating lattices, multiplication closure and norms p^deg(h).
   Include every resulting prime of norm <=U, allowing redundant classes.
4. At p=2,3,5 use the full multiplication algebra O_K/pO_K. Enumerate
   every subspace of F_p^4 once by reduced row echelon pivot patterns.
   Test invariance under all four basis multiplication maps. Among proper
   invariant subspaces retain all inclusion-maximal ones, recording a
   containing proper ideal witness for every rejected nonmaximal ideal.
   Lift their inverse images as integer lattices; record quotient
   dimensions and norms. This uses ideal correspondence directly and
   avoids assuming that a maximal order has a power basis. Check domain
   coverage and maximality by an independent containment replay.
5. Store all candidates, failed divisibility tests, ideal checks and
   completeness witnesses on disk, then independently replay the full
   relevant evidence. Explain the specialization from bounded integral
   class representatives to prime-ideal class generators in the eventual
   canonical proof. No claim about relations or the class number follows
   from a generating list alone.

Prospective cumulative caps for producer plus replay: 10000000 polynomial
candidate divisions, 100000 exceptional subspaces, 10000000 subspace
containment/closure tests, 1000000000 instrumented exact scalar operations,
dimension four, integer numerator/denominator length 4096 bits. Count
rejected candidates and both executions; save a resumable ledger before
long work. Print actual/required bounds, failures and certificate paths.
These are ceilings, not an unmeasured promise of successful execution.
Stop on a cap or failed completeness check and preserve partial evidence;
do not enlarge the search in the same attempt. A different enumeration
mechanism would need its own coverage if outside this contract.

## Qualifications and continuation test

Approve the source scope as SPECIALIZE for a REPRODUCTION calculation.
The test is a complete replayed finite list under these caps; an incomplete
list or conditional output fails the target. No new lemma, script,
signature, cutoff, prime decomposition or relation was produced here.
Mathlib coverage for the full certificate and supporting bounds has not
been checked; no absence or formal-verification claim is made.

The primary Mauldin statement was reaccessed on 2026-10-25:
https://sites.math.unt.edu/~mauldin/beal.html agrees with the exact local
positive-integer target. The nominated AMS page again returned HTTP 403;
its current content and prize rules were not read. This repeats the
recorded access limitation and does not block standard ideal theory.
