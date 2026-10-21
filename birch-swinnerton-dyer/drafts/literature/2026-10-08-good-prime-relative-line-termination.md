# Good-prime full-relative line termination — completed source review

TARGET: Assess whether multiplicity one and the boundary Hecke action guarantee that enumerating good-prime operators makes L029's full-relative geometric-plus dual kernel one-dimensional for every non-CM E/Q.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Checked L029, the 2026-10-07 relative-Hecke and fixed T_2 assessments and ATTEMPTS/022--024; searched good-prime multiplicity one, boundary Hecke spectra and raised-level oldform ambiguity; retrieved the primary textbook statements and cusp-equivalence proof specified below.
SOURCE_EVIDENCE: Stein online v0.1, Computing with Newforms Theorem 9.4 and Example 9.6; General Modular Symbols boundary definition, Theorems 1.39/1.44 and Remark 1.43; Weight Two eigenvector section; Ribet--Stein 2017 Proposition 9.4.3, pp. 80--81; Cremona corrected second edition Proposition 2.2.3 and its proof, pp. 16--17; Sutherland 2017 Lecture 8 Theorem 8.1. Exact URLs, inspected cases and qualifications follow.
COMPARISON: Known inputs separate newform characters and describe cuspidal duality; the raised-level oldform example explains why exact conductor is essential. Cusp equivalence and the full path action cover a direct boundary calculation at primes congruent to one modulo N. No inspected theorem states L029's entire termination certificate verbatim.
GAP: Authorize only the relative-dual specialization: verify the boundary calculation including reduced cusp representatives, injective restriction of eigenfunctionals to absolute cycles, geometric-plus multiplicity, scalar extension and eventual finite intersection. These are proof obligations for the next research turn, not results derived here; no explicit prime cutoff or matrices are supplied.
REASON: Essential source coverage is adequate for this bounded specialization of known inputs. The exact-level target is retained; uniform q supply remains parked. No lemma or mathematical program was written and no termination theorem is claimed as proved in this literature turn.
SCOPE: Minimal non-CM E/Q, normalized rational weight-two newform of exact conductor N, complete full-relative torsion-free Manin presentation and certified operator construction retained. Enumerate primes ell not dividing N in increasing order with exact a_ell(E); no twist q, nonzero central value, Manin constant, finite Sha or BSD assumption.
LITERATURE_REASON: Changed hypothesis: replace L029's granted full-space dimension-one witness by guaranteed eventual attainment. Existing assessments explicitly exclude termination and full-relative uniqueness.
COVERED_TARGET: Prove eventual dimension-one termination of L029's full-relative geometric-plus dual kernel when all good-prime operators are enumerated at the exact conductor of a non-CM E/Q.

## Proposal preserved from invocation

The main gap is still rank E(Q)=m(E) for m(E)>=2. Possible downstream
use is production of the relative line in L028/L036 while the independent
q and coefficient thresholds remain unresolved. Essential local input is
L029; L030 is a fixed benchmark only. Neither supplies uniform termination.

Compare at most three directions: repeated uniform twist-source retrieval
is parked with its access evidence; another fixed twist-value computation
would repeat the L031 mechanism without resolving generic supply; the
selected full-relative Hecke termination question is independent of q and
has the concrete threshold dim_Q K=1 in L029's exact space. This is a
proposal, not a newly proved or approved implication.

Read primary statements and essential proof cases for newform multiplicity
one and the Hecke action on the cusp-boundary quotient. Check exact level,
oldform multiplicities, passage to the relative dual and reflection sign.
Do not infer relative uniqueness from an absolute-only theorem, or assume
semisimplicity of a relative extension without coverage. Compare stronger
known algorithms and bounds; import adequate theorems rather than reprove
them. A specific uniform prime bound is not part of this target.

Continue only if those sources cover eventual dimension one under the
stated hypotheses, or identify a precise useful narrower theorem. If a
boundary or oldform ambiguity survives every good-prime equation, record
that obstruction and abandon this formulation. Do not calculate or prove
this uncovered target in the source-review turn. Complete matrices,
independent q, numerical C, coefficient nonvanishing, rational Kummer
membership, divisible Sha and complex-order comparison remain separate.
Full Mathlib coverage has not been checked.

## Inspected primary inputs and applicability

All retrievals below were made on 2026-10-08. Statements are imported
by citation; the combined relative termination assertion is not imported
as an already inspected theorem.

[Stein, *Modular Forms, a Computational Approach*, online v0.1,
Computing with Newforms](https://www.wstein.org/books/modform/modform/newforms.html),
Theorem 9.4 and the paragraph immediately following its proof, give
Atkin--Lehner--Li decomposition, good-index simple constituents and the
explicit Gamma_0 analogue. The theorem cites Li (1975) and Atkin--Lehner
(1970), rather than proving their theory. Example 9.6 has two level-11
degeneracy copies at level 22 with the same away-from-22 action. Read
these statements and this example, not just the theorem heading.
Theorem 9.23 concerns all bounded-index operators on cusp forms, so
it is not a good-prime cutoff on the full relative module; Remark 9.24
also cautions about replacing bounded indices by primes. No such bound
is approved here.

[Ribet and Stein, *Lectures on Modular Forms and Hecke Operators*,
January 12, 2017](https://www.wstein.org/books/ribet-stein/main.pdf#page=89),
Definition 9.4.2 and Proposition 9.4.3, printed pp. 80--81, state that
the rational anemic Hecke algebra on a cusp-form space is a product of
the coefficient fields of the distinct newform orbits at levels dividing
N; its map sends T_n to the tuple of a_n. Read its setup and the
qualification in Remark 9.4.5 about old multiplicities. This supplies
cross-level character separation that new-subspace multiplicity alone
does not state. Proposition 9.4.1's proof explicitly uses Dirichlet's
theorem for coprime residue classes. Theorem 9.1.9 and its following
paragraph, printed p. 74, were also inspected, but new-subspace uniqueness
alone is not the full relative statement.

Reuse L029's previously assessed real-period duality and path adjointness.
[Stein, General Modular Symbols](https://www.wstein.org/books/modform/modform/modular_symbols.html),
Cuspidal Modular Symbols, defines boundary by endpoint difference and
cuspidal symbols as its kernel. At weight two use the image of boundary,
not surjectivity onto all cusp divisors. Theorem 1.39 is cuspidal duality;
Theorem 1.44 gives signed cuspidal Hecke-compatible pairings. Read
equations (11)--(12) and Remark 1.43: at weight two Stein's star is -j.
These statements do not assert semisimplicity of the full relative
extension. The approved attempt must use L029's geometric j convention.

[Stein, Weight Two](https://www.wstein.org/books/modform/modform/weight_two.html),
Computing Using Eigenvectors, explicitly discusses one-dimensional
good-prime eigenspaces in the new subspace and the Hecke recurrences.
This supports passage from good primes to good indices, but does not
remove boundary directions or by itself exclude an oldform character
at another level. That is why the preceding anemic-algebra statement
is included.

[Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
edition, Chapter 2](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=10),
Proposition 2.2.3, printed pp. 16--17, gives cusp equivalence for reduced
p_j/q_j, including the unit-u condition
q_2=u q_1 modulo N and u p_2=p_1 modulo gcd(q_1,N).
Read the proof of (1) implies (2), the Bezout adjustment for (2) implies
(1), and the final solvable-congruence case proving (1) equivalent to
(3). This is sufficient input to test every transformed cusp in L029's
path formula; it is not an assertion of scalar boundary action.
Infinity and cancellation in transformed fractions must be handled
explicitly in the mathematical turn. The source does not need to be
reproved. Reuse the previously inspected Section 2.1.3 real duality and
Section 2.4 operator normalization.

[Sutherland, MIT 18.783, Spring 2017 Lecture 8](https://math.mit.edu/classes/18.783/2017/LectureNotes8.pdf#page=1),
Theorem 8.1, p. 1, states for every elliptic curve over F_q that
|q+1-#E(F_q)|<=2 sqrt(q). Read its finite-field hypothesis and the proof
through nonnegative endomorphism degree and discriminant. Apply only to
good reductions of E; no bound on arbitrary boundary eigenvalues follows
from Hasse alone.

## Exact authorization and continuation test

The COVERED_TARGET above is a SPECIALIZE / REPRODUCTION proof attempt,
not permission to invoke new source-dependent mechanisms. Keep L029's
complete relative presentation, operator certification and independent
a_ell data as premises. The remaining specialization is necessary because
the sources do not directly compare full relative dual kernels. No
reproof of modularity, multiplicity one, period duality, Hasse or Dirichlet
is justified.

Test the boundary action using a good prime ell=1 modulo N and the
source-backed cusp criterion. The sought scalar on cusp divisors is
ell+1. Verify both ell-divisibility cases of a reduced denominator,
the possible cancellation by ell in transformed fractions, and infinity.
Use the image of the endpoint map and its dual, rather than identify
boundary duals with cuspidal symbols. If this test passes, compare its
scalar with a_ell(E) using Hasse, then test restriction to the absolute
dual without granting a splitting of the relative extension. This is
a proposed calculation sequence, not a derivation performed here.

Next justify one geometric-plus cuspidal direction at the exact level,
including the oldform exclusion from the inspected anemic algebra and
degeneracy statements. Supply the finite-dimensional rational argument
for eventual attainment by the nested finite kernels. A temporarily
unchanged dimension is not a stopping certificate. No fixed number of
operators, largest prime or runtime bound is sought.

Continue if all these checks prove the exact full-relative threshold;
otherwise preserve the surviving boundary/oldform ambiguity and stop
this formulation. Retain non-CM and minimality for compatibility with
L028/L036, without claiming those restrictions drive Hecke uniqueness.
This possible line-production result still grants complete operator
construction and supplies no independent q, normalized C, coefficient,
rational Kummer membership, divisible-Sha elimination or complex-order
comparison. The main BSD gap remains unchanged.

## Discovery/access limits and Mathlib

Queries included `modular forms modular symbols Eisenstein boundary
eigenvalues multiplicity one newform`, `boundary Hecke cusps l+1`,
`Hecke cusps p 1 modulo N`, and `Atkin Lehner Theorem 9.4 Stein`.
Searches found stronger algorithmic and boundary leads, not evidence of
novelty. Diamond--Im's PDF and Kani's lecture PDF returned retrieval
errors; neither is imported. A Greenberg--Stevens Lemma 6.9 boundary
annihilator lead was indexed, but its distribution-module hypotheses and
proof were not fully inspected; it is not used. Primary coverage above
avoids dependence on those leads. A local download fallback also failed
DNS resolution; no API key or account changes were attempted.

Local duplicate checks confirm L029 grants dimension one and the fixed
L030 assessment excludes uniform termination. ATTEMPTS/022--024 retain
the calibration/production failures; none disproves the independently
tested exact-level Hecke mechanism. The literature review changes the
route from uncovered to ready, without proving a new mathematical claim.
Full matching Mathlib termination coverage and supporting APIs: not
checked. Unknown availability is not evidence of absence.
