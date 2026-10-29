# Bounded quartic principal-ideal parity relations — source coverage

TARGET: Determine the F_2-rank of exact principal-ideal relations supported on L135's 32 primes from nonzero elements a_0+a_1 alpha+a_2 beta+a_3 gamma with all |a_i|<=2.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched the exact quartic coefficients with class-group terminology, class-group relations modulo two, and Milne/Stevenhagen ideal factorization; checked local L134/L135, generator assessments, history/483 and ATTEMPTS/019,045,058. No inspected source evaluates this fixed coefficient box.
SOURCE_EVIDENCE: Milne ANT v3.08 (2020-07-19), Theorem 3.7 pp.49–50, Corollary 3.13 and following divisibility remark p.51, Propositions 4.1(c)/4.2 pp.69–70; Stevenhagen (2008), Section 7 pp.224–225 and Section 12 pp.248–249, especially the factor-base exact sequence and partial relation index formula; Stacks Lemma 10.12.10, tag 00DF, statement and full proof; Mathlib finite abelian structure theorem and Dedekind factorization documentation, accessed 2026-10-25.
COMPARISON: Known unconditional theory covers exact ideal relations and the quotient obtained from partial relations; L135 supplies the complete generating factor base. The remaining task is a finite exact instance calculation, not new ideal or class-group theory, and no source gives its rank.
GAP: No element norms, ideal valuations, support decisions or parity rank for this box have been computed. Full execution and independent replay must certify every retained and rejected element before any class-group conclusion.
REASON: Essential relation-method coverage was missing from the generator assessment; the inspected factor-base sequence and norm/divisibility criteria now cover this unchanged target. No backend, GRH or quadratic tower is required.
SCOPE: Exactly TARGET, using L133, audited L134's fixed maximal-order basis/table and audited L135's ordered 32 prime lattices; exact factorization, exhaustive bounded enumeration, parity elimination and its ordinary-class quotient interpretation. No unit basis, full class presentation, localized class computation, descent, rank or point calculation.

## Relevance and overlap

The main gap is still the infinite residual primitive Beal family. This
intermediate target concerns only ordinary class information in the actual
quartic branch field. It could remove a class-two-torsion obstruction in a
later descent; it supplies neither units nor that descent. The independent
rank, rational-point, marked-lift, integer-recovery, degree-nine, L095-system
and remaining-signature obligations stay open. Unfinished L108 is preserved.

The full supplied overview and DAG were used before the targeted reads.
L134 identifies the maximal order, ordered basis and multiplication table;
L135 supplies all 32 primes as actual lattices and their generation theorem.
Its generator/audit assessments explicitly exclude relation calculations;
the scoped search found no duplicate computation for this box. No
cross-notebook input is used.

ATTEMPTS/019 stops a degree-36 Minkowski enumeration, not direct arithmetic
in this audited quartic. ATTEMPTS/045 parks a complete octic class-backend
calculation: partial relations do not answer that target. ATTEMPTS/058
excludes the quadratic tower. None is reopened here. The present target
asks for the rank of one finite relation set, not complete relations or a
backend class number. Repeating backend probes is unnecessary.

## Primary source comparison

[J. S. Milne, Algebraic Number Theory, v3.08](https://www.jmilne.org/math/CourseNotes/ANT.pdf):
reuse the previously inspected unique-factorization theorem and read the
ideal-divisibility criterion on p.51. In a Dedekind domain containment is
reverse divisibility. Read Propositions 4.1(c), 4.2 and their proofs:
principal ideal norms agree with absolute element norms, ideal norms are
indices and are multiplicative. These statements apply to L134's O_K,
including ramified primes. They need no monogenic presentation. Norm one
and the unit ideal must be retained; the zero ideal is excluded.

[Peter Stevenhagen, The arithmetic of number rings, MSRI Publications 44
(2008), pp.209–266](https://library.slmath.org/books/Book44/files/08psh.pdf):
read Section 7's multiplication-determinant definition of norm, pp.224–225,
and Section 12, pp.248–249. Its factor-base exact sequence is

    1 -> O_K^* -> O_{K,T}^* -> Z^T -> Cl(K) -> 0,

where T generates Cl(K), and the middle map records ideal valuations.
The partial-relation quotient maps onto Cl(K); its finite order can
exceed the true class number. The text explicitly handles nonmonogenic
O/pO at index primes. Its analytic class-number/regulator certification
is needed for a complete presentation, which this test does not seek.

[Stacks Project, Lemma 10.12.10, tag 00DF](https://stacks.math.columbia.edu/tag/00DF):
read the statement and complete Hom–tensor proof of right exactness for
arbitrary modules. Apply over Z with N=F_2 to the partial-relation quotient
surjection. Together with the standard structure theorem for finite abelian
groups, this covers the proposed interpretation: rank r gives an upper
bound 32-r for dim Cl(K)/2Cl(K), equivalently dim Cl(K)[2]. Rank 32 would
certify no ordinary class two-torsion and odd class number, not class number
one. A rank shortfall supplies no lower bound. This is source-level scope
approval, not a calculated value or a new lemma proof in this turn.

Searches did not locate an evaluated match for this exact field and basis.
Unrelated relation-matrix search hits were not used as theorem inputs.
No inference of originality is made. The initial candidate Stacks tag
00DL concerns localization and was rejected; 00DF is the inspected input.
One PDF screenshot timed out; the relevant complete text passages were
subsequently accessible, so no essential source blocker remains.

## Approved exact execution and certificate requirements

The following is an implementation contract for the next research turn;
no instance calculation or mathematical script was performed here.

1. Bind inputs to L133/L134/L135 and the full saved prime lattices, retaining
   the exact ordered basis. Enumerate all coefficient tuples in {-2,-1,0,1,2}^4
   except zero, with duplicates/omissions checked. Keep both signs and all
   units, even though duplicate or zero relation vectors cannot raise rank.
2. Compute multiplication matrices in O and their nonzero determinants.
   Use absolute norms. Rational smoothness is only a filter: repeated exact
   division by the distinct rational norms in T can reject a residual
   cofactor greater than one, since every listed prime has norm p. Retain
   the full division record. A passing filter does not certify support.
3. Determine each listed prime valuation by exact membership in successive
   prime-power lattices, stopping at the first failed membership. The norm
   bound limits the exponent to floor(log_2(abs(N(x)))); use integer powers,
   not floating logs. Membership means integral coordinates in a certified
   full lattice, not a congruence in the power order. Compute products from
   all pairwise basis products with exact integer lattice reduction. Retain
   transformations certifying equality of the product span and reduced
   lattice in both directions; replay them independently. All 32 primes,
   including those above 2,3,5, use the maximal order.
4. Retain complete valuation and first-nonmembership witnesses. Compare the
   product of the listed prime norms to abs(N(x)). Equality certifies full
   support; a strict deficit certifies an omitted prime factor. For accepted
   elements also certify the principal lattice equals the product of the
   prime-power lattices by exact containment and index (or both containments).
   Do not silently treat a failed equality or resource stop as rejection.
5. Reduce the full accepted exponent vectors modulo two in the fixed prime
   order. Retain every row, elimination operations, pivot columns and rank.
   Independently replay both the arithmetic and elimination; a rank summary
   alone is insufficient. Use the cited partial-quotient implication with
   L135 generation; do not assume the relation lattice is saturated.

Exact integer lattice reduction is an implementation aid, not an assumed
mathematical oracle: two-way span certificates are required. No general
factorization theorem is to be reproved. The future canonical result must
state the hypotheses, exact achieved rank, proof/certificates, qualifications
and Mathlib coverage, and justify this instance specialization.

Before execution fix a cumulative ceiling of 20,000,000 instrumented scalar
arithmetic operations across producer and replay, 200,000 prime-power
membership tests, and 4096 numerator/denominator bits. Count all generation,
failed trials and replay charges in one new target-specific ledger; preserve
existing ledgers. Use dimension four, exactly this box and the fixed 32
primes. State accounting exclusions explicitly. If a cap is hit, save the
partial certificate and report incomplete; do not enlarge caps or the box
automatically. Output complete evidence to disk with concise summaries.
These are proposed finite-test limits, not established complexity bounds.

## Continue/abandon and Mathlib

Complete the box even if full parity rank appears early: the target is the
rank of the specified complete set. Compare achieved r with required 32.
At 32 retain the ordinary-class simplification for a separately assessed
descent target. At smaller r stop this box, retain its honest upper bound,
and reassess the mechanism rather than enlarge it. Arithmetic failure or
an exhausted cap yields no certified final rank. No outcome resolves Beal.

Inspected supporting Mathlib documentation:
[DedekindDomain.Factorization](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/DedekindDomain/Factorization.html)
provides `FractionalIdeal.count`, `Ideal.finite_factors` and ideal
factorization infrastructure;
[FiniteAbelian.Basic](https://leanprover-community.github.io/mathlib4_docs/Mathlib/GroupTheory/FiniteAbelian/Basic.html)
provides `AddCommGroup.equiv_directSum_zmod_of_finite`. Neither inspected
page certifies this field, box, relation matrix or rank. A full matching
formal theorem and formalized implementation were not checked; no absence
claim or Lean verification is asserted.
