# L134 — Maximal order and discriminant of the pair branch quartic

## Hypotheses

Use L133's field K=Q(alpha), with alpha integral and irreducible minimal
polynomial

    g(X)=X^4+64X^3+150X^2−32500X−109375.

Its identification with the branch field is alpha=25theta,
theta=alpha/25, as in L133. All lattices below are inside this same
degree-four field over Q. There is no monogenic maximal-order assumption.

## Conclusion

The integer ring O_K has the Z-basis

    1, alpha,
    beta=(alpha^2+14alpha+25)/50,
    gamma=(alpha^3+239alpha^2+4475alpha+19375)/18750.

Its discriminant is

    disc(K)=2874960=2^4 * 3^3 * 5 * 11^3,
    [O_K:Z[alpha]]=937500=2^2 * 3 * 5^7.

This supplies an integer ring for subsequent ideal arithmetic only.
It does not determine class groups, units, Selmer groups, quotient ranks,
rational points, marked lifts, integer recovery or any Beal exclusion.
The computation and independent arithmetic replay below establish this
specialization of standard order theory. The separate critical proof audit
of 2026-10-25 accepts the stated integral basis, index and discriminant;
its scope and exact evidence are recorded below.

## Proof

### Imported order criteria

Import Peter Stevenhagen, *The arithmetic of number rings*, MSRI
Publications 44 (2008), pp.209–266,
[Lemma 6.4, p.221, and Section 9, pp.233–235, Proposition 9.3 and proof](https://library.slmath.org/books/Book44/files/08psh.pdf).
For an order R and prime p, let I_p be the inverse image of the nilradical
of R/pR. The multiplier ring (I_p:I_p) is an integral overorder of R,
contained in (1/p)R. Proposition 9.3 gives a strict enlargement whenever
R is not p-maximal. Thus equality certifies p-maximality. Section 9
computes the nilradical as a Frobenius kernel with p^k greater than the
algebra dimension, and computes the multiplier ring through its action
on I_p/pI_p. No restriction excluding p=2,3, ramification, or
nonmonogenic orders is imposed. The determinant trick in Lemma 6.4
also makes every element of a full unital lattice closed under
multiplication integral. These are imported results, not new order theory.

Import J. S. Milne, *Algebraic Number Theory*,
[v3.08 (2020-07-19), Remark 2.25, p.34](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
for the discriminant/index-square identity. For an order R in K,
disc(R)=[O_K:R]^2 disc(O_K); in particular a prime in its index has
square dividing disc(R). Here K is separable of degree four because
L133 is over Q, and all proposed lattices are full. The prior source
assessment is `drafts/literature/2026-10-25-pair-quartic-maximal-order.md`.

### An explicit integral order and its trace discriminant

Let R be the Z-span of the four displayed elements. Its basis matrix,
with columns in the coordinates (1,alpha,alpha^2,alpha^3), is

    B = [[1,0,1/2,31/30],
         [0,1,7/25,179/750],
         [0,0,1/50,239/18750],
         [0,0,0,1/18750]].

It is nonsingular and contains 1 and Z[alpha]: the defining equations
give alpha^2=50beta−14alpha−25 and then express alpha^3 integrally in
1,alpha,beta,gamma. Reduction by g gives the entire nontrivial product
table below. Products with 1 and reversed products supply all others:

    alpha^2   = −25−14alpha+50beta,
    alpha beta= −275−26alpha−225beta+375gamma,
    alpha gamma=−125−11alpha−100beta+175gamma,
    beta^2    = 236+29alpha+174beta−270gamma,
    beta gamma= 83+11alpha+61beta−88gamma,
    gamma^2   = 25+4alpha+18beta−20gamma.

Thus R is closed and unital, so is an integral order by the imported
determinant trick. This proves integrality of every lattice element,
not merely of individually chosen generators.

The multiplication traces in this basis are (4,−64,60,30). Taking the
trace of every product gives the full Gram matrix

    G = [[4,−64,60,30],
         [−64,3796,−1686,−546],
         [60,−1686,1428,648],
         [30,−546,648,324]].

Its determinant is 2874960=2^4*3^3*5*11^3. Also
det(B)=1/937500 and [R:Z[alpha]]=937500. The independently computed
power-order trace discriminant is

    disc(Z[alpha])=2526820312500000000=2^8*3^5*5^15*11^3
                 =937500^2 * 2874960.

Both factorizations are complete. The certificate retains successive
divisions and all rejected divisors 2 through 11, ending with residual
one; primality of every listed factor is checked independently. No
unresolved cofactor is treated as prime.

### Explicit terminal local maximality

In this paragraph coordinates refer to the R-basis (1,alpha,beta,gamma).
For p=2,3,5,11 the following are the matrices of x -> x^q on R/pR,
with their corresponding integral inverse-image lattice bases J_p for
I_p. The Frobenius columns are the powers of the four basis vectors;
q>4 in each case. All entries of F_p are modulo p, and J_p has columns
in R-coordinates:

    p=2, q=8:
    F_2=[[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    J_2=[[2,1,1,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]].

    p=3, q=9:
    F_3=[[1,1,2,2],[0,2,2,2],[0,2,2,2],[0,0,0,0]],
    J_3=[[3,0,2,2],[0,3,2,2],[0,0,1,0],[0,0,0,1]].

    p=5, q=5:
    F_5=[[1,0,2,3],[0,1,2,3],[0,0,0,1],[0,0,0,1]],
    J_5=[[5,0,3,0],[0,5,3,0],[0,0,1,0],[0,0,0,5]].

    p=11, q=11:
    F_11=[[1,6,4,2],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
    J_11=[[11,5,7,9],[0,1,0,0],[0,0,1,0],[0,0,0,1]].

Their ranks are respectively 1,2,3,1. In each case pZ^4 is contained
in J_p Z^4, F_p J_p=0 modulo p, and det(J_p)=p^rank(F_p).
The equal index proves that J_p Z^4 is the full inverse image of
ker(F_p), hence I_p, rather than a sublattice of it.

Let A_i be multiplication by the i-th R-basis element, derived from
the complete table. All matrices M_i=J_p^(-1) A_i J_p are integral,
as also checked explicitly in the replay. Define a 16-by-4 matrix D_p
whose row (r,c), numbered 4r+c with r,c=0,...,3, is
((M_0)_(r,c),...,(M_3)_(r,c)) modulo p. Its following 4-by-4 minors
already prove full column rank; rows are zero-indexed:

    p=2, rows [0,1,2,3]:
      [[1,1,1,1],[0,1,0,1],[0,0,1,1],[0,1,1,1]], det=1 mod 2.
    p=3, rows [0,1,2,3]:
      [[1,0,1,1],[0,1,1,1],[0,1,1,2],[0,2,0,2]], det=2 mod 3.
    p=5, rows [0,2,3,4]:
      [[1,0,2,0],[0,0,1,0],[0,0,0,1],[0,1,2,0]], det=1 mod 5.
    p=11, rows [0,1,2,3]:
      [[1,6,4,2],[0,3,7,9],[0,7,4,8],[0,9,8,9]], det=5 mod 11.

To check exactly what these minors certify, write x=(sum_i v_i b_i)/p
with v_i integral. Every multiplier of I_p has this form by the
imported containment in (1/p)R. It preserves I_p precisely when
sum_i v_i M_i is divisible entrywise by p: these are coordinates on
I_p/pI_p, not on I_p/pR. Equivalently D_p v=0 modulo p. Each displayed
minor is invertible, so all v_i vanish modulo p. Therefore x belongs
to R and (I_p:I_p)=R. The converse containment is supplied by the
integral M_i. The imported criterion proves p-maximality at all four
primes, including the exceptional small primes.

No other prime can divide [O_K:R], by the complete discriminant
factorization and the imported index-square identity. Hence R=O_K.
In fact the exponent-one prime 5 could have been omitted from the
maximality tests, but its full certificate is retained too. This proves
the asserted basis, index and field discriminant.

### Computation, replay and bounds

Run `python3 scripts/pair-genus-two/quartic_order.py` and then
`python3 scripts/pair-genus-two/verify_quartic_order.py`.
The cumulative ledger is deliberately never implicitly reset; reproduction
adds charges to the existing attempt and stops at its original caps.

The producer saves `scripts/pair-genus-two/quartic-order-certificate.json`:
all nine orders, their complete bases, inverses, multiplication tables,
traces and Gram matrices; twelve sequential radical/multiplier records;
four additional terminal records on the final order; all finite-field
kernels and row operations; all lattice inclusions, actions and indices;
and both full discriminant factorizations. The eight strict enlargements
are two at 2, one at 3 and five at 5; there are none at 11. The final
proof above can be verified directly on R without assuming the
generation sequence is correct.

The independent replay imports only shared accounting, not the producer
or its arithmetic. It rebuilds field products by Horner companion
shift/reduction instead of precomputed power convolution, determinants
by subset expansion instead of elimination, and ranks by incremental
column elimination in addition to replaying every row operation. It
checks every saved order and every radical and multiplier preimage
lattice in both directions using containment and index, the complete
actions, all terminal equalities and both trace/index discriminant
calculations. Its 967 checks all pass, with no mathematical failures.
The full evidence, not just a preview, is
`scripts/pair-genus-two/quartic-order-verification.json`; its selected
terminal witnesses are reproduced above. The original producer JSON
SHA-256 is `4531a1f5ed1b9291da37fe111651bb72ee488cfaeadefb7679dd255fb473680e`.

Before the critical audit, `scripts/pair-genus-two/quartic-order-ledger.json` recorded
94/250000 factor/divisor trials, 8/128 strict enlargements,
591967/2000000 instrumented scalar operations, field dimension 4/4
and maximal numerator/denominator bits 78/4096. These cumulative values
include generation and two replays: the second adds the displayed
terminal minors. An accounting review added eleven divisor-trial
charges omitted by the first replay's primality helper; that helper's
scalar arithmetic was already charged. No mathematical result changed,
no failed mathematical trial or restart was erased, and no cap was hit.
Details remain in `drafts/2026-10-25-pair-quartic-maximal-order-attempt.md`.
Numeric arithmetic, rational division construction, numeric comparisons,
sums and modular inverses use the accounting API. Container/control
bookkeeping, serialization, Fraction normalization and internal bit
operations are excluded; this is not a bit-operation or runtime bound.

This is a reproduction/specialization of inspected standard algorithms,
not a claim of new maximal-order mathematics. The previously excluded
quadratic tower is not assumed to exist or reopened. No class/unit,
rank, point or main-target gap is claimed closed by this local result.

### Separate critical proof audit — 2026-10-25

The audit uses the previously approved SPECIALIZE contract in
`drafts/literature/2026-10-25-pair-quartic-maximal-order-audit.md` and
accepts this lemma without a mathematical correction. It checks the
direct final-order argument, not merely the producer's terminal flags.
No general order criterion is reproved or extended.

The field input is L133, including its use of L132's irreducibility.
The audit supplement independently divides the exact reduction
Q4 mod 19=[7,14,13,12,13] by every one of the 19 monic linears and
361 monic quadratics. Every reconstructed remainder agrees with the
saved L132 record and is nonzero; the whole divisor domain is checked
for completeness and duplicates. Primality of 19 is checked through
divisors 2,3,4. The nonzero leading coefficient and primitive Q4 permit
the reduction argument in L132, and the coefficient identity
g(25T)=−25^3 Q4(T), with inverse scaling T -> T/25, verifies L133's
unchanged field identification. This audits the input used here, not
the unrelated elliptic-cover or cubic-resolvent conclusions.

For the order argument, the audit compares the displayed basis, all six
products, traces, Gram matrix, Frobenius matrices, radical bases and
minor witnesses with the complete saved entries. The inverse basis is

    B^(-1)=[[1,0,−25,−13400],
            [0,1,−14,−1129],
            [0,0,50,−11950],
            [0,0,0,18750]].

Thus containment is in the claimed direction: the power lattice is
contained in R, with index det(B^(-1))=937500. The unital multiplication
table establishes integrality before any order theorem is applied.
Multiplication traces are field traces because these are the matrices
of multiplication in the degree-four Q-algebra K itself. All-prime
coverage uses the final trace discriminant and its complete factorization,
not the claim that a finite search happened to terminate.

At p=2,3,5,11, the four ranks 1,2,3,1 are verified independently of the
saved row-reduction ranks. For each J_p, integrality of p J_p^(-1)
proves pZ^4 is contained in its lattice; F_p J_p=0 proves containment
in the inverse image; determinant p^rank(F_p) proves equality, since
that inverse image has exactly this index in Z^4. The exponents 8,9,5,11
are powers of their respective primes and exceed four, so the imported
Frobenius criterion identifies these kernels with the entire nilradical.
Every conjugated action J_p^(-1) A_i J_p is checked in full and integral.
Its flattened matrix has domain R/pR and codomain End_Fp(I_p/pI_p).
The displayed nonzero minors therefore exclude every multiplier outside
R inside p^(-1)R; they do not only exclude selected generators or act
on the smaller quotient I_p/pR. Stevenhagen's criterion applies at
2 and 3 as well as at the larger primes. The exponent-one prime 5 is
redundant for the index argument, but its full action also passes.

The implementation audit checks the arithmetic independently of success
flags: the replay's Horner recurrence computes a*b modulo g by successive
alpha shifts; its subset determinant counts permutation inversions;
its column elimination establishes rank, while the separate row-operation
replay and free-coordinate identity establish full kernels. Containment
and determinant, rather than a presumed lattice-normal-form routine,
establish both radical and multiplier preimages. The full generation
chain is also replayed, but is unnecessary for the direct proof on R.
The producer and replay share Python exact Fraction arithmetic and the
accounting API; they do not share field, determinant or kernel code.
This is arithmetic independence, not independence of software runtime
or formal verification.

One additional execution of `verify_quartic_order.py` passes all 967
checks, with no failures and the same producer SHA-256 displayed above.
Then `python3 scripts/pair-genus-two/audit_quartic_order.py` saves
`scripts/pair-genus-two/quartic-order-audit.json`: full input hashes,
all 380 reconstructed divisor remainders, the exact scaling and basis
checks, and comparisons of every actual/required entry and flag in the
967-check replay payload. Its 2710 checks pass. The payload comparisons
bind and inspect the complete arithmetic evidence; they are not 2710
independent mathematical results and do not replace the executed replay
or the proof audit above. The supplement was run twice, the second after
replacing its remainder nonzero predicate by `any(rem)` and removing an
unused import; both runs passed and their charges remain recorded.

The current cumulative ledger is 897/250000 factor/divisor trials,
8/128 strict enlargements, 880972/2000000 instrumented scalar operations,
dimension 4/4 and numerator/denominator bits 78/4096. These totals retain
the original generation, three order replays, the earlier eleven-charge
repair and both audit-supplement executions. The original accounting
exclusions remain; the supplement also treats container indices and
nonzero truth tests as control bookkeeping, with the resulting predicate
checked through the accounting API. No cap, mathematical failure or
unrecorded restart occurred. The audit establishes this arithmetic
prerequisite only; every independent limitation in the conclusion remains.

## Mathlib

Full matching and supporting maximal-order, Frobenius-kernel and
discriminant/index theorem coverage have not been checked in Mathlib.
No absence claim, Lean proof or formal certification is asserted.
