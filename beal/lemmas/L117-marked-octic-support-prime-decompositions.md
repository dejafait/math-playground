# L117 — Complete support-prime decompositions of the marked octic

## Hypotheses

Use the entire degree-eight field of audited L115,

    K=Q[theta], 275theta^8−2860theta^6+6930theta^4−3564theta^2+243=0,

and the maximal-ring basis (b_0,...,b_7) of audited L116, with b_0=1.
All integer coordinates below refer to that exact ordered basis. In
particular theta is not assumed integral, and no power order is
substituted for O=O_K. No normality, class group, unit group, local point
image or rational-point completeness is assumed.

## Conclusion

The complete decompositions, with distinct primes in each row, are

    2O  = P2_1^4 P2_2^4,
    3O  = P3_1^6 P3_2,
    5O  = P5_1^4 P5_2 P5_3^2,
    11O = P11_1^8.

Their residue degrees and quotient maps are specified completely below.
Together they give eight distinct supported primes over {2,3,5,11}.
This is a prerequisite for supported class/unit arithmetic, not such an
arithmetic computation, a rational-point bound or an integer exclusion.

## Proof

### Imported results and specialization

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-23-marked-octic-support-prime-decomposition.md`.
Import H.W. Lenstra, Jr., *Algorithms in algebraic number theory*,
Bull. Amer. Math. Soc. (N.S.) **26** (1992), 211–244,
[arXiv:math/9204234v1](https://arxiv.org/pdf/math/9204234v1),
Sections 2.7–2.8, Theorem 4.9 and its complete algorithm sketch,
manuscript pp.17,20. This supplies arbitrary-order prime discovery by
finite-algebra arithmetic, with residue-field certificates. Take its
order A=O from L116, subring C=Z and base prime (p), for p=2,3,5,11.
These are nonzero prime ideals; no monogenic, normal, tame or large-p
hypothesis is required. We reproduce a fixed instance, not the general
algorithm or a new decomposition theorem.

Also import J.S. Milne, *Algebraic Number Theory*,
[v3.08, 19 July 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorems 3.20, 3.29 and 3.34, printed pp.53,57,59–60:
the integral closure here is Dedekind, nonzero ideals factor uniquely
into nonzero prime ideals, and the complete decomposition satisfies
sum(e_i f_i)=[K:Q]. L115 supplies a characteristic-zero field of degree
eight; L116 supplies its actual maximal ring. Thus these apply without
assuming K/Q Galois. No equality of ramification indices or residue
degrees is imposed between different primes.

The nonmonic equation-order shortcut in Del Corso–Dvornicich–Simon,
*Decomposition of primes in non-maximal orders*, Acta Arith. **120.3**
(2005), Theorem 3 p.240, requires p coprime to the equation-order index.
L116's index is 2^32*3^10*5^2, so it cannot give the needed decompositions
at 2,3,5 from that order. The computation below uses O directly at all
four primes. No reproof of these imported theorems is needed; exact
instance maps and lattice identities are the necessary specialization.

### Residue maps and explicit ideal bases

For each row below let k=F_p[X]/(g). A one-row map has target F_p,
equivalently g=X. A two-row map lists first the coefficient of 1 and
then the coefficient of X. Columns are the images of b_0,...,b_7.
The map on integer coordinates is reduction modulo p followed by Q.

```text
prime  e  f  g(X)             rows of Q
P2_1   4  1  X                (1,1,1,1,0,0,1,0)
P2_2   4  1  X                (1,0,1,1,0,1,1,0)
P3_1   6  1  X                (1,2,2,0,1,1,0,2)
P3_2   1  2  X^2+2X+2         (1,0,1,2,1,1,0,2)
                             (0,1,0,0,0,0,0,0)
P5_1   4  1  X                (1,3,1,2,0,3,3,2)
P5_2   1  2  X^2+3            (1,3,1,2,0,3,4,0)
                             (0,0,0,0,0,0,0,1)
P5_3   2  1  X                (1,3,4,2,0,3,3,2)
P11_1  8  1  X                (1,6,3,7,9,5,9,5)
```

Here is a uniform explicit specification of all eight full integer
ideal bases, including the ordering of their columns. Let
J=(j_0,...,j_(f−1)) be (0) for every f=1 row, (0,1) for P3_2,
and (0,7) for P5_2. The J columns of Q are exactly I_f. For each
j=0,...,7 set

    c_j = p b_j                                  if j belongs to J,
    c_j = b_j + sum_(a=0)^(f−1) r_(a,j) b_(j_a)   otherwise,
    r_(a,j) = the representative of −Q_(a,j) mod p in {0,...,p−1}.

Then (c_0,...,c_7) is the recorded ideal basis of P, and P=ker(Q).
This is a complete basis formula with every coefficient specified by
the displayed rows, not merely a generating subset or an index.
Indeed Q(c_j)=0. Conversely, for any vector in the kernel subtract
its nonpivot coordinates times c_j; only pivot coordinates remain,
and Q being the identity on those coordinates makes them divisible
by p. This proves the reverse lattice inclusion as well. It also
proves pO subset P. The determinant is p^f, and surjectivity follows
from the same pivot columns.

For P3_2 the values of X^2+2X+2 at 0,1,2 are 2,2,1 modulo three.
For P5_2 the values of X^2+3 at 0,1,2,3,4 are 3,4,2,2,4 modulo five.
Both quadratics are therefore irreducible. All linear g=X are
irreducible as well. Every k is consequently the claimed finite field,
of size p^f.

For every displayed Q the full 64 basis-product equations

    Q(b_i b_j) = Q(b_i) Q(b_j) in k,   0<=i,j<=7,
    Q(b_0)=1,

are checked using L116's entire integral multiplication table. The
certificate stores both sides through the product values; the
independent replay reconstructs every equation by polynomial reduction.
Linearity and bilinearity extend these equations to all of O. Thus Q
is a surjective unital ring map and its exact kernel P is maximal.
All eight basis multipliers preserve each ideal; their complete
integer coordinate matrices are retained and replayed too. Within
each p, two-way lattice containment checks certify distinctness.
Primes over different p are automatically distinct by contraction.

### Discovery and complete product certificates

For transparency discovery retains the entire finite-algebra calculation.
On O/pO compute the matrix of x -> x^q with q=8,9,25,11 respectively.
These exponents are p-powers at least eight, so their kernel is the
nilradical. Indeed nilpotents in an eight-dimensional algebra have
nilpotence index at most eight, while a power equal to zero implies
nilpotence. The image is a reduced subalgebra isomorphic to the reduced
quotient: Frobenius is an automorphism on each finite residue field.
Complete row operations and kernel bases give image dimensions 2,3,4,1.
The producer and replay enumerate all 4,27,625,11 image elements,
respectively, and all their idempotents. Their primitive idempotents
number 2,2,3,1. Projection onto each component and a power basis provide
the displayed residue maps. No Frobenius rank is itself treated as a
prime list. More importantly, completeness of the claimed prime list
also follows directly from the certified final ideal products below,
so it does not rest on trusting this discovery procedure.

An ideal product is generated by ALL 64 products of its two ordered
eight-element bases. Every such generator is evaluated in the integral
multiplication table. The resulting 64-by-8 row matrix is reduced by
integer row swaps, row sign changes, and additions of integer multiples
of a different row. These operations are invertible over Z. The
certificate retains the original generator matrix, every operation,
the full reduced row matrix (eight independent rows followed by 56
zero rows), and the transpose of its first eight rows as a column basis.
The replay verifies every operation forward and backward. Consequently
each reported basis has exactly the same lattice as all original
product generators, with both inclusions certified. Norms or determinants
alone are never used to assert equality of ideal products.

For each P, successive powers through P^(e+1) are stored. Multiplying
the inverse power basis by pI_8 gives integral coordinates precisely
at powers 1,...,e; at e+1 at least one coordinate has a nontrivial
denominator. These complete coordinates are retained and replayed.
Thus the claimed last containing power is exact, rather than inferred
from a slope or a partial local factorization. There are 38 such power
products across the eight primes, all within the cap e<=8.

Independently multiply the claimed factors with their positive
exponents, starting from O. The final column bases, in the same L116
coordinates, are exactly

    p=2:   2I_8     (eight prime factors counted with multiplicity),
    p=3:   3I_8     (seven factors),
    p=5:   5I_8     (seven factors),
    p=11: 11I_8     (eight factors).

All 30 intermediate products are certified with the reversible lattice
operations just described. In total all 68 product reductions are
replayed completely. The final matrices are full lattice equalities
with pO, not just matching determinants. Since the displayed factors
are distinct maximal ideals and the exponents are positive, unique
ideal factorization in O proves that these are the COMPLETE
factorizations, with no additional prime possible.

Finally, the independent residue-degree checks give

    p=2:  4*1+4*1       =8,
    p=3:  6*1+1*2       =8,
    p=5:  4*1+1*2+2*1   =8,
    p=11: 8*1           =8.

These meet the required degree-eight threshold at every prime and
agree with Milne's general degree identity. The quotient sizes are
respectively (2,2), (3,9), (5,25,5), (11).

### Complete arithmetic evidence and limitations

Reproduce from the active notebook directory:

    python3 scripts/pair-genus-two/marked_octic_support_primes.py
    python3 scripts/pair-genus-two/replay_marked_octic_support_primes.py

The full producer evidence is
`scripts/pair-genus-two/marked-octic-support-primes-certificate.json`.
The full independent replay is
`scripts/pair-genus-two/marked-octic-support-primes-replay.json`.
Both bind the preceding certificate bytes by SHA-256. The replay imports
no support-prime producer implementation. It uses L116's already
independent replay for Horner field multiplication, subset-expansion
determinants, incremental column ranks and row-operation checks. It
rebuilds all 64 products of the maximal-ring basis directly from the
original polynomial before checking the support-prime evidence.
Frobenius powers are rebuilt by repeated multiplication, polynomial
remainders by a separate descending reduction, and all integer product
operations are checked in both directions. Every residue map, kernel,
ideal basis, stability matrix, containment coordinate, intermediate
product and complete finite discovery record is consumed. All 1,210
comparisons pass, with no failures. The complete presentation of the
maps and bases was also inspected, rather than relying on a bounded
preview. The separate critical audit below confirms the mathematics and
repairs a mutable-record defect in the replay's saved evidence.

This is a REPRODUCTION of assessed standard methods for this fixed
instance, with local progress on a necessary ring-arithmetic input;
no progress beyond those checked general sources is claimed. Actual
supported units, S-class two-torsion, real/finite local point images,
points on surviving covers, degree-nine root recovery, compatible
remaining factors, both L095 integer systems and the minus-eleven
alternative remain unresolved. The known rational infinity points
still prevent an empty fake-Selmer-set shortcut. No complete Beal
candidate results.

### Separate critical audit, 2026-10-23

The unchanged approved scope is
`drafts/literature/2026-10-23-marked-octic-support-prime-critical-audit.md`.
This audit confirms all four decompositions, all eight exact residue maps
and ideal bases, and their completeness. The only correction concerns
serialization of replay evidence, described below; no mathematical
statement, basis, exponent, residue degree or direct input changes.

**The field and ring hypotheses.** Audited L115 identifies the entire
degree-eight characteristic-zero field. Audited L116 establishes the
displayed maximal basis, rather than merely an order with integral-looking
products. The fresh replay uses the original coefficient list
`[243,0,-3564,0,6930,0,-2860,0,275]`; Horner multiplication followed by
the stored inverse basis reconstructs all 64 products and the trace
matrix. The audit compares every entry of the printed L116 basis with
this same input. In particular b_0=1, and the basis order used for every
quotient and ideal is unchanged. The ring is therefore the integral
closure of Z in that field. The cited Milne theorems apply to its nonzero
ideals; they require neither normality nor tameness. All four rational
primes are nonzero, and the kernels contain their respective pO.

**Quotients and exact kernels.** Every coefficient in the printed eight
maps, both quadratic polynomials, all exponents and all residue degrees
matches the full certificate and presentation artifact. The replay
checks unitality and every one of the 512 basis-product equations.
The complete monic-divisor trials verify irreducibility: in this instance
the only nontrivial trials are all three or all five linear divisors
of the two quadratics. The printed pivot columns are precisely the
identity matrices, proving surjectivity. Thus every quotient is the
claimed field, its kernel is maximal, and its contraction to Z is (p).

For each ideal the audit reconstructs all eight columns from the printed
formula, verifies that they map to zero, and also expresses every
normalized finite-kernel lift and every column of pI_8 as an integer
combination of those columns. Those lifts together with pI_8 generate
the entire inverse image: reduce any kernel element modulo p in the
certified complete nullspace and subtract the resulting integer lifts.
This explicitly verifies both inclusions, in addition to the replay's
index-and-inclusion proof. All eight stability matrices per ideal are
integral. Two-way inclusion tests distinguish every pair over the same
p; distinct rational contractions distinguish the other pairs.

**Complete discovery.** The replay reconstructs Frobenius and all its
kernel row operations and independently checks rank and nullity. The
exponents 8,9,25,11 are p-powers at least eight. In an eight-dimensional
algebra each nilpotent element has nilpotence index at most eight, so
these kernels are exactly the nilradicals. Their images are reduced:
if x^q is nilpotent then x is nilpotent, hence x^q=0. Since Frobenius
induces an automorphism on each residue field, these images identify
the reduced quotients. The image dimensions are 2,3,4,1.

The reviewed exhaustive loops cover all 4,27,625,11 image elements and
all their idempotents. A nonzero idempotent is primitive exactly when
there is no different nonzero idempotent below it under ef=f; the full
enumeration therefore finds all 2,2,3,1 components. Their sum is one
and pairwise products are zero. The component dimensions, power-basis
ranks, polynomial relations and linkage of each quotient to the
Frobenius projection are checked in full. The additional audit explicitly
checks that each proposed generator belongs to its reduced component.
The quotient maps can include a Frobenius automorphism of their residue
fields; this does not change their kernels. No raw rank is substituted
for the list, and final-product completeness is independent of discovery.

**Every full lattice product.** All 38 successive-power and 30 assembled
product records are linked to their actual preceding bases, starting
at I_8. Every product retains all 64 basis products. Their entries and
all terminal entries are integral, and every saved operation is a row
swap, a sign change, or addition of an integer multiple of a different
row. These are invertible over Z. The reviewed replay checks the entire
forward and backward programs, all 56 terminal zero rows and the full
rank-eight terminal basis; triangular pivots are positive.

The additional audit makes both lattice inclusions explicit. For a
64-by-8 generator matrix M and terminal column basis B, it computes
B^(-1)M^t, checks all entries integral and verifies reconstruction of
M^t. It also applies the complete operation program to I_64; if U is
the first eight rows of that transform, it checks UM=B^t exactly.
The certificate stores all forward coordinates and the complete exact
operation program specifying U, including its initial identity and
selected rows. This is a finite straight-line specification of all
integer coefficients, not a hash, numerical approximation or omitted
matrix. Its expanded multiplication was checked. Thus the entire
product lattice, not merely its determinant, equals the reported basis.

For each P the complete coordinates B_k^(-1)pI_8 are integral through
k=e and nonintegral at k=e+1, with all entries checked. The exponents
are positive and at most eight. Independently the assembled products
are exactly 2I_8,3I_8,5I_8,11I_8. Their factors are the distinct nonzero
maximal ideals just proved, so unique ideal factorization makes the
lists complete and the stated multiplicities exact. The four residue
degree sums are separately checked to equal eight, and the quotient
sizes are (2,2), (3,9), (5,25,5), (11). No degree-sum shortcut, partial
product or norm-only equality enters this inference.

**Implementation independence and repaired evidence.** The complete
producer and replay implementations and the imported L116 replay helpers
were inspected. The new replay imports no producer: field products use
Horner companion reduction instead of convolution, Frobenius uses
successive multiplication instead of binary powering, and rank checks
use incremental column elimination independently of producer row
elimination. The support-prime replay shares these already audited
L116 helpers; it is not a third independent field implementation.

The first audit found a genuine saved-record defect. After each forward
row-operation comparison the replay stored a reference to `rows` and
then mutated that same outer list during reverse replay. Its comparison
was true when executed, but the serialized actual value in each of the
68 forward records became the original generator matrix instead of the
terminal matrix. The replay now snapshots those rows before reversal.
The original producer certificate and original replay JSON are preserved;
their pass flags alone should not be used as internally consistent
forward-state evidence. The fresh corrected replay has all 1,210
comparisons passing, and every serialized actual value equals its
required value. The 428 additional audit comparisons pass too, with
zero failures and all eight kernels and 68 products covered.

Run from this notebook:

    python3 scripts/pair-genus-two/audit_marked_octic_support_primes.py

Full corrected replay evidence is
`scripts/pair-genus-two/marked-octic-support-primes-audit-replay.json`;
the additional checks, complete inclusion certificates, discovery
records and input hashes are in
`scripts/pair-genus-two/marked-octic-support-primes-audit-certificate.json`.
The original failed audit and its inconsistent fresh replay are retained
as `marked-octic-support-primes-audit-initial-failure.json` and
`marked-octic-support-primes-audit-initial-replay.json` in that directory.
The working note `drafts/2026-10-23-marked-octic-support-primes-audit.md`
also records an intervening output-size failure: expanded transformation
coefficients exceeded Python's decimal conversion limit. The complete
operation-program representation above fixes output without weakening
any arithmetic check. No failed mathematical identity was suppressed.

This establishes an audited arithmetic input by reproduction of the
assessed methods, not progress beyond the cited general results.
Supported units and S-class two-torsion, real and finite point images,
surviving-cover point completeness, degree-nine root recovery, compatible
remaining factors, both L095 systems and minus-eleven remain unresolved.
The known infinity points continue to prevent an empty fake-Selmer-set
shortcut. Beal remains IN_PROGRESS, without a complete candidate.

## Mathlib

Full matching Mathlib coverage of these fixed maximal-prime decompositions
or their exact certificates was not checked. General algebra, ideal and
finite-field support is not asserted to provide a matching formal
verification; no availability or absence claim is made.
