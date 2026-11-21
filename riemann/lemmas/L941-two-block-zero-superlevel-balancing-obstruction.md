# Lemma 941: the two-block zero superlevel is not preserved by balancing

## Hypotheses

Use exactly L938's 34 pairs (c_alpha,alpha), with twelve exponent slots
and total exponent twelve, and L939(4)'s factorials. Let Pbar be the
full arithmetic S_12 average defined in L940(1), and H_m its restriction
in L940(3), with m entries q and 12-m entries 1. Put

    s_m(q)=mq+12-m,
    t_m(q)=(q repeated m times,1 repeated 12-m times)/s_m(q), q>0.

The domain is the positive unit simplex. No actual-theta distribution
ordering, integral-preservation, variation-transfer, contact, real-zero,
RH or Decimal hypothesis is assumed. The conclusion is finite rational
algebra for the specified polynomial, retaining every factorial and the
zero exponent slots belonging to the M_0^12 normalization.

## Conclusion

The set {t:Pbar(t)>=0} is not closed under majorization toward the
uniform vector. In particular, for

    q0=541/4096, q1=271/2048, m=4,

we have 0<q0<q1<1, t_4(q1) majorized by t_4(q0), and

    Pbar(t_4(q0))>0, Pbar(t_4(q1))<0.                              (1)

The complete positive-root/sign tables below show inward preservation
on the two-block paths m=1,2,6 and failure on m=3,4,5. All sixteen
positive roots in these tables are simple. Passing paths establish
only their restricted property. The failure stops the proposed global
zero-superlevel sufficient mechanism; it does not refute a crossing
bound for L938's integrated density or any RH assertion.

## Proof

### Applicability: the normalized path and the six block sizes

The homogeneity and full average in L940 give

    Pbar(t_m(q))=H_m(q)/s_m(q)^12.                                 (2)

Since s_m(q)>0, these signs agree. Let u=(1/12,...,1/12) and let v
have first m coordinates 12-m and remaining coordinates -m. Then

    t_m(q)=u+c_m(q)v, c_m(q)=(q-1)/(12s_m(q)), c_m'(q)=1/s_m(q)^2>0.

For q0!=1 and q1 between q0 and 1, rho=c_m(q1)/c_m(q0) lies in [0,1],
and t_m(q1)=rho t_m(q0)+(1-rho)u. The matrix
rho I+(1-rho)J/12 is doubly stochastic (J has every entry 1).
Thus t_m(q1) is majorized by t_m(q0). This is the necessary
specialization of Alexandre Ostrowski, *Sur quelques applications des
fonctions convexes et concaves au sens de I. Schur*, J. Math. Pures
Appl. (9) **31** (1952), 253-292, section I nos.5-8, Theorem I,
pp256-259 ([primary article](https://www.numdam.org/item/JMPA_1952_9_31__253_0.pdf)).
All coordinates are strictly positive, with equal total sum one.
Only the stated matrix/order theorem is imported; no smooth criterion
is applied to a discontinuous indicator.

If m>6, exchange the two blocks and replace q by 1/q. Symmetry and
degree twelve give H_(12-m)(q)=q^12 H_m(1/q); equivalently
t_(12-m)(q) is a permutation of t_m(1/q). Reciprocation takes the
interval between q0 and 1 to the interval between 1/q0 and 1.
Hence the six paths cover both complementary block sizes, without
asserting coverage of vectors having three or more distinct entries.

### Complete coefficients and exact root theorem

Write N_m=d_m H_m, where d_m>0 and the coefficients of N_m, in
ascending order, are as follows. Trailing zero coefficients are omitted.

    m=1, d=1140694410240000:
    (1485,-2562,9415,-9996,6795,-2002,-63)
    m=2, d=401524432404480000:
    (212391,-631974,1179675,4281144,-13010946,17114076,
     -10714242,2843960,-178341,-13734,-665)
    m=3, d=2676829549363200000:
    (393351,-788088,-9432990,63177072,-110220891,62605872,
     67066188,-114016896,62035329,-15230712,1710450,-91056,1331)
    m=4, d=501905540505600000:
    (-3717,287497,-3221575,10631299,-5542978,-29318198,69213634,
     -63981834,29038487,-6214019,451605,13111,-1632)
    m=5, d=3212195459235840000:
    (-144249,2596160,-17860710,26479544,116242861,-492189600,
     792001532,-631356656,256308241,-43460704,-757750,842744,-50661)
    m=6, d=267682954936320000:
    (-9365,161102,-749790,-1567114,19399285,-55776708,77806076,
     -55776708,19399285,-1567114,-749790,161102,-9365)

These identities are reconstructed from each original row by explicit
enumeration of its labelled subsets I of size m:

    H_m(q)=sum_alpha c_alpha/[F_alpha binomial(12,m)]
                    *sum_(|I|=m) q^(sum_(i in I)k_i).

The count binomial(12,m) is the average denominator, not an extra
multinomial multiplier. An independent replay computes each row by
[z^m y^j] product_k(1+z y^k)^alpha_k. Both constructions agree with
the saved L940 coefficients. At q=1 each row equals c_alpha/F_alpha,
and all six full sums equal L939(5)-(6)'s 1/371319795000. No tail
asymptotic or previous Schur witness is required in this calculation.

The root-count input is Michael Eisermann, *The Fundamental Theorem
of Algebra made effective: an elementary real-algebraic proof via
Sturm chains*, [arXiv:0808.0097v4](https://arxiv.org/pdf/0808.0097v4),
26 March 2012 version, sections3.5-3.7, Theorem3.15,
Corollary3.16 and Remark3.17, pp10-12. Signed Euclidean chains count
distinct real roots, and derivative gcds recover multiplicities.
Proposition5.8, p19, puts roots of a monic polynomial with remaining
coefficients c_j strictly inside radius 1+max|c_j|. The ordered ambient
field here is R; rational arithmetic computes the chains exactly.
Q is not being asserted to be real closed.

For each N_m the saved chain starts with positive rational rescalings
of N_m and N_m', then uses negative remainders, each rescaled only by
a positive rational factor. Every division identity

    a=quotient*b-next/factor, factor>0, deg(next)<deg(b),            (3)

is retained and replayed coefficient by coefficient, including the
terminal zero remainder. Positive rescaling preserves the Sturm
sign rules: at an interior node zero its neighbors have opposite
signs; at a simple first-polynomial root the derivative direction
agrees with the second polynomial. The last nonzero remainder is a
nonzero constant in every case. Euclid therefore gives
gcd(N_m,N_m')=1, so no real or complex multiple root is omitted;
the successive-gcd process terminates immediately.

At nonroot rational endpoints a<b, deleting zero chain values and
taking the variation difference counts roots in (a,b). Every endpoint
used below is explicitly checked to be a nonroot. This avoids the
multiple-root endpoint exception in Philippe Pebay, J. Maurice Rojas
and David C. Thompson, *Sturm's Theorem with Endpoints*,
[arXiv:2208.07904v1](https://arxiv.org/pdf/2208.07904v1),
16 August 2022, Theorem1.2 and Lemma1.4, pp1-4. No half-root endpoint
convention is needed. None of these six polynomials is zero or
constant; N_m(0)!=0, so there is no excluded zero-root multiplicity.

### Exhaustive positive-root isolation and signs

Let V be the zero-deleting chain variation. Each B in the table is
strictly larger than 1+max_(j<deg N)|N_j/N_leading|, so no positive
root is at or beyond B. All entries at 0,1,B are nonroots.

| m | degree | B | V(0),V(1),V(B) | positive roots | open-interval signs | inward exits |
|---:|---:|---:|---|---:|---|---:|
| 1 | 6 | 160 | 3,3,2 | 1 | + - | 0 |
| 2 | 10 | 25737 | 5,5,4 | 1 | + - | 0 |
| 3 | 12 | 85664 | 6,6,4 | 2 | + - + | 1 |
| 4 | 12 | 42412 | 8,5,2 | 6 | - + - + - + - | 2 |
| 5 | 12 | 15635 | 7,6,3 | 4 | - + - + - | 1 |
| 6 | 12 | 8310 | 6,5,4 | 2 | - + - | 0 |

The intervals of signs are (0,r_1),(r_1,r_2),...,(r_k,infinity).
The complete disjoint rational isolators are below, in increasing
order within each m. Each contains exactly one root; the listed
endpoint variations differ by one. Their number exhausts V(0)-V(B),
so there are no additional positive roots in any complementary gap.

| m | root | lower | upper | V(lower),V(upper) |
|---:|---:|---|---|---|
| 1 | 1 | 955019/524288 | 1910197/1048576 | 3,2 |
| 2 | 1 | 20115237/4194304 | 80464165/16777216 | 5,4 |
| 3 | 1 | 1649376293/536870912 | 412365489/134217728 | 6,5 |
| 3 | 2 | 24172234905/536870912 | 3021540071/67108864 | 5,4 |
| 4 | 1 | 63/4096 | 1/64 | 8,7 |
| 4 | 2 | 541/4096 | 271/2048 | 7,6 |
| 4 | 3 | 1183/4096 | 37/128 | 6,5 |
| 4 | 4 | 715404985/268435456 | 178861849/67108864 | 5,4 |
| 4 | 5 | 1696201771/268435456 | 848122091/134217728 | 4,3 |
| 4 | 6 | 1863611075/134217728 | 3727264561/268435456 | 3,2 |
| 5 | 1 | 1533/4096 | 767/2048 | 7,6 |
| 5 | 2 | 83372173/33554432 | 41689995/16777216 | 6,5 |
| 5 | 3 | 102740765/16777216 | 205489347/33554432 | 5,4 |
| 5 | 4 | 388719827/33554432 | 97181911/8388608 | 4,3 |
| 6 | 1 | 825/2048 | 1651/4096 | 6,5 |
| 6 | 2 | 166559285/67108864 | 83283797/33554432 | 5,4 |

For each complementary interval an exact nonzero rational evaluation
is saved, including the first positive interval and the unbounded last
interval. Completeness of the root list and continuity make its sign
constant throughout that interval. Alternatively the signs follow from
N_m(0)'s sign and the established simplicity of each root. The tables
thus specify all q>0, not a sampled grid. Splitting at q=1 creates no
new zero: every H_m(1)=1/371319795000>0. The number of roots below one
is respectively 0,0,0,3,1,1.

At every positive root H_m=0, which belongs to {H_m>=0}. If a root
lies below one its inward interval is the interval immediately to its
right; if above one the inward interval is to its left. Inspecting
these adjacent signs, including the roots themselves, gives precisely
the exit counts displayed. The offending roots are root2 for m=3,
roots2 and5 for m=4, and root3 for m=5. When no inward adjacent sign
is negative, any path from a nonnegative starting point toward one
stays nonnegative: a first entry into a negative interval would have
to cross a root with negative inward side. There are no isolated
even-multiplicity zeros here because every gcd is constant. They were
not silently discarded as non-sign-changing roots.

### Rational counterexample without relying on algebraic starting points

Use the endpoints of m=4's second isolator as q0,q1. Direct evaluation
of the displayed integer N_4 gives

    4096^12 N_4(541/4096)
      =240144996270454406660522410541398964574437280>0,
    4096^12 N_4(271/2048)
      =-240865490784023141273305086453025686705012736<0.           (4)

Both q values are strictly positive and q0<q1<1. Division by d_4>0
and s_4(q)^12>0 proves the two signs in (1). More explicitly,

    t0=(541/34932 repeated 4 times,1024/8733 repeated 8 times),
    t1=(271/17468 repeated 4 times,512/4367 repeated 8 times),
    rho=5172847/5174895, t1=rho t0+(1-rho)u, 0<rho<1.              (5)

All entries are positive, each vector sums to one, and (5) proves
the majorization claim by the cited doubly stochastic theorem. Thus
a vector of strictly positive Pbar value is carried inward to a
strictly negative value. This refutes inward preservation even without
using a root as the initial member of the closed superlevel.

### Verification scope and remaining gap

Reproduction commands, from the active notebook:

    python3 scripts/heat/l938-zero-superlevel-58.py
    python3 scripts/heat/l938-zero-superlevel-replay-58.py

The adjacent `.json` files contain the complete rational coefficients,
row reconstructions, input hashes, division identities, all endpoint
values and variations, exact interval samples, multiplicity evidence,
root bounds, and the full rational witness. The producer's 879 checks
and the independent replay's 906 checks pass with empty failure lists.
Replay reads the entire certificate, reconstructs rows by a different
counting method, checks every saved division coefficient, and evaluates
endpoint/sample values by direct power sums instead of Horner's rule.
The complete relevant evidence is checked, not inferred from a preview.
These finite checks rely on Python integer/Fraction implementations;
they are not a Lean proof or a separate later conceptual audit.

The prior EXPLORE assessment is
`drafts/literature/2026-11-09-l938-zero-superlevel-balancing-scope-56.md`.
The arithmetic and imported theorems are known tools. The assessed
search did not settle this fixed sign set; this is a local negative
result, without a certified originality claim. L940's global value
ordering stop is a contrast, not the premise of the sign-set failure.
L938 supplies the rows, L939 the labelled polynomial and balanced
coefficient, and L940 the averaging/restriction definition.

No equality of a symmetrized integral with the actual density is used.
Its singular-face weights, actual-theta ordering, finite-energy
variation count, endpoint signs, contacts, other degrees,
initialization, realization and global continuation remain unresolved.
The main L030-L032/C032a all-degree positivity gap is unchanged.

### Independent proof and evidence audit — 9 November 2026, step60

The audit accepts the stated six tables and the rational counterexample,
with no correction to the mathematical conclusion. It reuses the prior
SPECIALIZE scope in
`drafts/literature/2026-11-09-l941-sign-set-obstruction-audit-scope-58.md`.
This is independent verification of a local obstruction, not a further
originality claim or a density crossing theorem.

The new audit program imports neither producer nor replay. It reads
both complete certificates and verifies their input hashes and successful
check lists. Starting from all 34 original rows, it multiplies the
twelve labelled factors (1+z y^k) one slot at a time. For every row and
block size, it reconstructs every coefficient, the factorial denominator,
the binomial average denominator and the balanced value. These agree
with both the original saved coefficients and every displayed N_m/d_m.
An independent evaluation of the finite Newton recurrence gives the
same balanced determinant 1/371319795000. The input is the twelve-slot
polynomial; no theta asymptotic or Schur discriminator is required.

For each signed Euclidean chain, every coefficient of (3) is checked
exactly, including the final zero remainder. All nonzero members have
nonzero leading coefficient, the first two are positive multiples of
N_m and N_m', and every subsequent factor is positive with strictly
decreasing degree. At an interior chain zero, (3) therefore gives
opposite signs for its neighbors; the initial derivative direction
agrees with that of N_m. The terminal nonzero constant proves the gcd
is one. These facts supply the signed-chain hypotheses of the cited
Sturm theorem and exclude every multiple root, rather than merely
assuming the certificate's multiplicity labels.

Every global endpoint record is explicitly linked to its claimed
coordinate 0,1,B; every isolator record is linked to its printed lower
or upper endpoint. All chain values, signs and zero-deleting variations
are evaluated again by rational power sums. Strict bounds B exceed
the full monic Cauchy bounds. Disjoint isolators each have count one
and their total counts exhaust (0,B): 1,1,2,6,4,2. No root is at zero,
one or any isolator endpoint, or beyond B. Thus all sixteen positive
roots, including the closed-superlevel zeros, are accounted for.
Complementary samples lie outside the isolators in their stated
intervals. Their complete exact values and signs agree with the
tables; simplicity also verifies sign alternation. The below-one
counts are 0,0,0,3,1,1. Correct inward sides give exit-root lists
empty, empty, (2), (2,5), (3), empty, respectively. Every printed
coefficient, bound, variation, isolator, sign and exit count agrees
with the audited evidence and the original replay's complete tables.

The witness polynomial is explicitly linked to this same N_4, and
its two rational arguments to the second isolator. Equation (4)'s
two entire integers and the normalization (2) are verified afresh.
Both vectors in (5) have twelve positive coordinates and sum one;
all 144 entries of rho I+(1-rho)J/12 are positive, its row and column
sums equal one, and its image of t0 is exactly t1. As an additional
independent order check, sorting both vectors and comparing all
eleven proper partial sums gives sum_(i<=k)t1_i <= sum_(i<=k)t0_i;
the twelfth sums both equal one. This verifies the exact applicability
of the cited majorization theorem. The strict positive-to-negative
exit refutes global inward preservation without relying on a
discontinuous differential test or on an algebraic starting point.

Reproduction, from the notebook:

    python3 scripts/heat/l941-independent-audit-60.py

The full certificate is `scripts/heat/l941-independent-audit-60.json`:
590 checks pass, with no failures. It records complete table comparisons,
exact bounds and all sorted witness partial sums, and binds the original
full evidence by hashes. A bounded preview was not used as verification.
The audit still relies on Python integer/Fraction implementations; it
does not add a Lean proof. No new mathematical input or DAG edge is
needed. The global sign-set mechanism remains stopped, while actual
theta ordering, integral preservation, density variation, contacts,
endpoint signs, other degrees and global continuation remain open.

## Mathlib

Full matching Mathlib coverage for this sign-set obstruction, the
normalized-majorization specialization, and the exact Sturm certificate
has not been checked. The primary mathematical inputs are cited above;
unknown formal coverage is not evidence of absence. Supporting rational
polynomial and root-count coverage was not searched in this step.
