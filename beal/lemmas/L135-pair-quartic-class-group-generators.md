# L135 — Certified finite class-group generators for the pair quartic

## Hypotheses

Let K be L133's quartic field Q(alpha), where

    g(X)=X^4+64X^3+150X^2−32500X−109375.

Use audited L134's maximal order O with ordered integral basis

    b=(1,alpha,beta,gamma),
    beta=(alpha^2+14alpha+25)/50,
    gamma=(alpha^3+239alpha^2+4475alpha+19375)/18750,

field discriminant 2874960 and index [O:Z[alpha]]=937500.
All ideal classes below are ordinary ideal classes, not narrow classes.
No class-group backend, GRH, monogenicity of O, or quadratic tower is assumed.

## Conclusion

The field is totally real. The following 32 prime-ideal classes generate
Cl(O). Every listed prime ideal has norm at most 157, and the list is
exactly the prime ideals of norm at most the conservative cutoff 159.
The list may be redundant; no relations, class number, unit basis, descent,
rank, point, lifting or Beal-exclusion conclusion is asserted.

The first 26 ideals are P_(p,c)=(p,alpha+c)O, with each c in the indicated
row giving a separate ideal. Their norms are p.

| p | c |
|---|---|
| 7 | 0 |
| 11 | 5 |
| 13 | 7 |
| 17 | 3, 15 |
| 29 | 15 |
| 31 | 17 |
| 43 | 41 |
| 47 | 8 |
| 71 | 41, 44 |
| 73 | 53 |
| 79 | 1, 77 |
| 97 | 7, 56 |
| 101 | 66 |
| 113 | 37 |
| 127 | 56 |
| 131 | 80 |
| 137 | 119 |
| 149 | 45 |
| 151 | 14, 53 |
| 157 | 10, 86 |

The other six ideals have the following Z-bases, expressed in b. Within
each row the four displayed elements span the ideal as an abelian group.
Their respective norms are the displayed p.

| p | Z-basis of the prime ideal |
|---|---|
| 2 | 1+gamma, alpha+gamma, beta+gamma, 2gamma |
| 3 | 1+gamma, alpha+gamma, beta+2gamma, 3gamma |
| 3 | 1+alpha, beta, gamma, 3alpha |
| 5 | 1+gamma, alpha, beta+2gamma, 5gamma |
| 5 | 1+gamma, alpha+gamma, beta+4gamma, 5gamma |
| 5 | 1+4gamma, alpha, beta+3gamma, 5gamma |

The calculation and independent arithmetic replay below establish this
exact instance of standard ideal theory. The separate critical proof audit
of 2026-10-25 accepts this partial input without a mathematical correction;
its scope and evidence are recorded below. This is not a complete Beal candidate.

## Proof

### Imported results and their specialization

Import J. S. Milne, *Algebraic Number Theory*,
[v3.08 (2020-07-19), Theorem 4.3, p.70, proof pp.79–81](https://www.jmilne.org/math/CourseNotes/ANT.pdf).
Every ordinary ideal class of a degree-n number field has an integral
representative of norm at most

    (n!/n^n)(4/pi)^s sqrt(abs(disc(K))),

where 2s is the number of nonreal embeddings. Import also Proposition 4.2,
pp.69–70, for norm multiplicativity, and Theorem 3.7, p.49, for unique
factorization of nonzero ideals in a Dedekind domain. These apply to the maximal integer ring O,
not merely the power order. If an integral representative is not O, factor
it into nonzero prime ideals. Each prime factor has positive integral
norm at least two, and by multiplicativity has norm no larger than that
representative. Therefore prime ideals up to any rigorous upper bound for
the Minkowski bound generate all ordinary classes. The unit representative
gives the identity class and requires no prime factor. This is the only
class-generation inference needed here; no class relations are inferred.
Stevenhagen, *The arithmetic of number rings*, Section 12, opening
pp.244–245, explicitly gives this prime-ideal class generation statement
with the unconditional Minkowski cutoff. The source distinguishes it
from the GRH-dependent Bach bound; the latter is not used here.

Import Milne, Theorem 3.41 and Remark 3.43, pp.62–63, for complete prime
factorization from the irreducible factors of g modulo p when p does not
divide [O:Z[alpha]]. Import the ideal correspondence and field-quotient
criterion on pp.14–15 for ideals above p as maximal ideals of O/pO.
The exceptional-prime distinction is also explained in Peter Stevenhagen,
*The arithmetic of number rings*, MSRI Publications 44 (2008),
[Section 8, pp.228–232, Theorems 8.2/8.4 and Example 8.3](https://library.slmath.org/books/Book44/files/08psh.pdf).
At 2,3,5 the power-order index is divisible by p, so the generic polynomial
factorization inference is not used. Instead the complete algebra O/pO
is used directly. General Minkowski and ideal theory are cited, not reproved
or claimed as new. The prior SPECIALIZE assessment is
`drafts/literature/2026-10-25-pair-quartic-class-generators.md`.

### Signature and rigorous integer cutoff

Exact evaluations give the four sign changes

    g(-48)=26753,   g(-47)=-15516,
    g(-34)=-10095,  g(-33)=12428,
    g(-4)=19185,    g(-3)=-12172,
    g(20)=-27375,   g(21)=61460.

The four open intervals are disjoint. Continuity gives four distinct real
roots; degree four leaves no nonreal roots. Thus s=0 and the coefficient
4!/4^4 is 3/32. The rational certificate is

    2874960 < 1696^2 = 2876416,
    (3/32) sqrt(2874960) < (3/32)1696 = 159.

Consequently cutoff U=159 is a valid conservative integer upper bound,
and meets the approved U<=300 cap. Retaining 159 causes no endpoint loss.
Every prime ideal of norm <=159 lies above a rational prime p<=159,
since its residue field has cardinality p^f with f>=1. Complete trial
division through the square root of every integer from 2 through 159 gives
the 37 rational primes

    2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,
    67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,
    139,149,151,157.

Every divisor remainder, including those for rejected composite integers,
is retained in the certificate and recomputed by replay.

### Regular primes: complete factors and ideal lattices

For each prime on the list other than 2,3,5, the index 937500 is nonzero
modulo p. The producer factors g mod p by exhausting monic linear and
quadratic trial divisors, retaining successful quotients with multiplicity.
A residual factor is appended once its degree makes further extraction
ineligible. Every factor is then separately certified irreducible by all
monic divisors of degree from one through half its degree. A reducible
polynomial has an irreducible factor of degree at most half its degree,
so this test is exhaustive in degrees <=4. The full factor product is
checked equal to g mod p. In particular repeated factors at ramified
p=11 are retained; g mod 11=(X+5)^4 gives one prime, not four distinct
primes. No squarefree or unramified hypothesis is silently added.

For every distinct factor h, the prime is (p,h(alpha))O with norm
p^deg(h), by the imported regular-prime theorem. Compute all four products
h(alpha)b_i in L134's complete multiplication table, reduce mod p and
take their row span W. This is precisely the reduction of that ideal.
Save its RREF and the full preimage lattice. The replay reconstructs all
products from the power basis, independently evaluates h(alpha) by powers,
and verifies that every image lies in the saved RREF. The regular-prime
theorem gives the image dimension 4-deg(h); the saved independent RREF
rows have that dimension, so containment is equality. This dimension
argument replaces an additional rank/minor computation; none is claimed.

All ideals of norm <=159 obtained at regular primes are the 26 linear
factors in the first table. Every other factor at these primes has norm
>159. The certificate also retains those factors and their excluded norms,
including all irreducible quartic and cubic factors, so omission from the
table is checked rather than assumed.

### Exceptional primes: exhaustive maximal-ideal enumeration

Use L134's full basis multiplication algebra over F_p, p=2,3,5. A subspace
is an ideal exactly when stable under multiplication by all four basis
elements: necessity is immediate, and sufficiency follows by F_p-linearity
of multiplication by any algebra element. Every subspace of F_p^4 has a
unique RREF. Enumerate all pivot subsets and all entries above nonpivot
positions to the right of their row's pivot. This generates every subspace
once, including zero and the full algebra. There are respectively 67,
212 and 1120 subspaces; all 1399 are tested, not only proposed ideals.

For every rejected nonideal save one basis multiplier and row whose
product falls outside the subspace. Replay tests invariance independently
using nonpivot-coordinate equations, and validates every saved rejection
witness. There are respectively 4,7,11 proper invariant subspaces. For each
proper ideal, compare with every strictly larger proper ideal. A maximal
ideal has no such containing ideal; each nonmaximal ideal has a saved
containing proper ideal witness. Independent inclusion replay confirms the
complete lists, leaving respectively 1,2,3 maximal ideals, all of codimension
one. A proper inclusion of finite-dimensional subspaces increases dimension,
so checking only larger dimensions loses no strict enlargement.

By ideal correspondence these are all primes above p in O, including any
splitting obscured in the singular power order. Their preimage lattices are
exactly the six bases in the second table. Each reduces to its corresponding
RREF, contains pO, has determinant p in the fixed O-basis, and is closed
under all four integral basis multiplication maps. Quotients have p elements,
so norms are p. The maximal-ideal enumeration, rather than the determinant
alone, certifies primality and completeness.

### Full lattice verification and reproducibility

For each saved lattice, the four columns are the RREF rows regarded as
integer vectors together with p times the nonpivot coordinate vectors.
Both programs check all four pO-containment vectors and all sixteen
basis-multiplication actions, with complete integral coordinates saved.
The replay computes the determinant by its 24-term permutation expansion.
Containment in the claimed mod-p subspace, inclusion of pO and index
p^(4-dim W) prove equality with its full inverse image. Thus a smaller
unverified sublattice is never substituted for the prime ideal.

Producer: `python3 scripts/pair-genus-two/quartic_class_generate.py`.
Replay: `python3 scripts/pair-genus-two/quartic_class_replay.py`.
The complete producer evidence is
`scripts/pair-genus-two/quartic-class-certificate.json`: binding hash and full
final-order input, all 201 sign evaluations, exact bound, complete rational
prime trials, every modular extraction candidate (including ineligible
candidates), every actual division and irreducibility remainder, full factor
products via retained factors, all exceptional subspaces and witnesses,
every prime lattice and action, and the final 32-element list.

The replay imports only shared accounting/instrumentation, no producer
mathematical implementation. It uses descending polynomial division instead
of ascending arrays, power-basis convolution/reduction and the displayed
inverse integral basis to rebuild every product, determinant expansion
instead of the producer's pivot-coordinate lattice construction, and
nonpivot-coordinate membership equations instead of row subtraction.
It independently enumerates all subspaces by pivot bitmasks and base-p
digits and compares the whole duplicate-free domain. At regular primes it
recomputes all saved divisions and complete monic-divisor domains, rather
than trusting a factorization flag. Both programs use Python exact integers
and Fractions and share accounting, so this is arithmetic independence,
not independent runtimes or formal verification.

The complete replay passes 1409026 checks, with no failures. The saved
verification `scripts/pair-genus-two/quartic-class-verification.json` records
its input hash, every regular factor/norm summary, the complete exceptional
domain sizes and maximal-ideal IDs, generator norms and successful completion.
The full per-candidate arithmetic evidence remains in the producer certificate
and is all consumed by replay; a bounded JSON preview alone is not evidence.
Before the separate audit, the persistent ledger
`scripts/pair-genus-two/quartic-class-ledger.json` retained both executions
without a reset. Their cumulative actual/cap values
are 342350/10000000 polynomial divisions, 2798/100000 exceptional subspaces,
11711/10000000 containment/closure tests, 34536079/1000000000 instrumented
scalar operations, dimension 4/4, integer bits 55/4096, sign evaluations
402/4096. No cap, failure or restart occurred.

Numeric binary/unary operators, explicit comparisons, rational construction
and sum additions are instrumented at AST load time in both source programs;
the persistent budget code contains no field or ideal algorithms. Loop/index
bookkeeping, container allocation and internal container equality, integer
absolute value/conversion, Fraction normalization, serialization and internal
bit operations are outside this scalar-operation metric. This is not a
bit-complexity or wall-clock guarantee. The programs' explicit arithmetic
powers are charged as scalar operations with output bit lengths checked.
The source-code comment correction after replay changes no executable code.

Finally every class has a bounded integral representative and every prime
factor of that representative occurs in these complete lists. This proves
the asserted generating property, not a presentation of Cl(O). Units and
relations, complete descent, quotient ranks and points, marked lifts,
degree-nine recovery, both L095 systems and other exponent signatures
remain unresolved. No negative route evidence or unfinished L108 work is
discarded or reopened by this small-degree calculation.

### Separate critical proof audit — 2026-10-25

The prior SPECIALIZE scope in
`drafts/literature/2026-10-25-pair-quartic-class-generators-audit.md`
approves this exact instance review, not class relations or new ideal theory.
The audit accepts the conclusion with no mathematical correction and no
new dependency. L133 supplies the field and audited L134 supplies its
maximal order; maximality is not inferred again from this factor base.

The complete producer and replay implementations were reviewed. One
additional execution of `quartic_class_replay.py` consumes the entire
unchanged certificate, including rejected candidates, and passes all
1409026 checks. Its producer SHA-256 is
`c5363d1b846188e37fc53590b61de34923bb981da25ddd895cd82e14dda9b73b`.
The full input order and its SHA-256
`4531a1f5ed1b9291da37fe111651bb72ee488cfaeadefb7679dd255fb473680e`
agree with L134's accepted certificate. The fixed basis and inverse,
all sixteen multiplication products, index and discriminant are checked
against that input; the replay independently reconstructs multiplication
from g in the power basis. This is the same field, not a different order
or an assumed isomorphic model with untracked ideal coordinates.

The sign argument uses four distinct real roots, so the Minkowski factor
is exactly 3/32. Both sides of the square-root comparison are positive;
the actual saved upper value is 1696 and the integer cutoff is 159.
The complete trial domain is every integer 2 through 159, not just the
37 integers eventually labeled prime. Every prime ideal with norm at
most 159 has residue characteristic in this domain. The exceptional
set is exactly the prime support of 937500=2^2*3*5^7.

At the remaining 34 primes, the reviewed descending-division recurrence
eliminates one leading coefficient at each step, preserving the polynomial
division identity. The replay reconstructs every extraction state, all
monic-divisor domains and each final factor product. Separate irreducibility
tests cover the full divisor degrees up to half the factor degree; thus
appending a residual factor never silently declares it irreducible.
Distinct factors, not their multiplicities, enumerate prime ideals.
In particular the four copies of X+5 at 11 give one ideal of norm 11.
Milne Remark 3.43 applies since 11 does not divide the power-order index;
ramification in the field discriminant does not invalidate that hypothesis.

For each such factor h, the actual span of h(alpha)O modulo p has
dimension 4-deg(h) by the imported theorem. Every image generator lies
in the saved canonical RREF, whose independent rows have exactly this
dimension; containment therefore proves equality. This is not an
unsupported rank inference from containment. All 26 included ideals are
linear-factor ideals; the other 36 distinct factor ideals have the
fully replayed norms recorded in the audit supplement, all exceeding 159.
Hence primes with no included factors have still been completely covered.

At 2,3,5 the replay independently regenerates the complete RREF domains
by pivot bitmasks and base-p digits, and checks equality with the entire
duplicate-free saved sets. The free positions are exactly nonpivot
columns to the right of each row's leading 1, which characterizes all
RREFs. Canonical pivot columns make the nonpivot-coordinate membership
equations equivalent to membership in the row span, including the zero
and full subspaces. Invariance under each algebra basis multiplier tests
the ideal property by bilinearity. Short-circuit rejection is sufficient
only for a witnessed nonideal; all invariant subspaces are retained.
For every proper invariant subspace, the replay checks all larger proper
ideals for containment. A strict inclusion increases dimension, so no
proper enlargement is missed. The domains 67,212,1120 yield 4,7,11
proper ideals and respectively 1,2,3 maximal ideals, of codimension one.
The maximal space IDs are [58], [185,208], [990,997,1066]. These are
primes of the full maximal order by ideal correspondence, not guesses
from the singular power-order factors or a ramification-degree sum.

Every preimage lattice is checked for integral coordinates, reduction
into its specified subspace, containment of all p times basis vectors,
closure under all sixteen basis actions, and determinant index
p^(4-dim W). The four saved vectors are columns: the replay's determinant
on their list as rows computes the transpose determinant, which is equal.
Containment and equal index identify the full inverse image. These checks
establish the stated norms in O, with no substitution of a proper
sublattice or confusion between an additive basis and ideal generators.

The new supplement `python3 scripts/pair-genus-two/audit_quartic_class.py`
saves `scripts/pair-genus-two/quartic-class-audit.json`. All 353 checks pass.
It binds the current certificate and replay to the accepted order hash,
records hashes of both programs and their accounting code, rejects
nonexact JSON numbers and checks integral lattice coordinates, compares
every regular (p,c) and every exceptional column basis and norm against
the two printed tables, and compares the complete regular and exceptional
replay summaries. It records every excluded regular ideal and its norm.
This closes the statement/output identification obligation. Its comparisons
are not 353 independent theorems and do not replace the full replay or
the mathematical domain arguments above. Both programs still share Python
exact integer/Fraction arithmetic; no formal verification is claimed.

Finally Milne Theorem 4.3 applies to every ordinary class in this maximal
order. Its integral representative has norm less than 159; unique ideal
factorization and multiplicativity put every prime factor on the complete
list just audited. The unit ideal contributes only the identity. Thus
the class-generation conclusion follows without a principal-ideal test,
class-number guess, narrow-class assertion, or GRH assumption. The precise
standard generation citation above is reused, not reproved as new theory.

The cumulative ledger now retains generation, two complete replays and
one audit-supplement execution. Actual/cap values are 513525/10000000
polynomial divisions, 4197/100000 exceptional subspaces, 18530/10000000
subspace tests, 53838792/1000000000 instrumented scalar operations,
dimension 4/4, integer bits 55/4096 and sign evaluations 603/4096.
There are no recorded failures, cap stops or resets. The original
accounting exclusions remain; supplement parsing, hashing and container
inspection are control/data handling rather than a new arithmetic search.
The audit authenticates only these generators. Relations, units, descent,
quotient ranks, point control and all remaining Beal obligations stay open.

## Mathlib

Full matching theorem/certificate coverage and supporting Minkowski,
Dedekind factorization and finite-algebra ideal correspondence results have
not been checked in Mathlib. No absence claim or Lean verification is made.
