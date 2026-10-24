# L123 — An explicit supported global class removed at two

## Hypotheses

Use L114's smooth proper marked curve C with

    Y²=G(t)=11F(t),
    F(t)=275t⁸−2860t⁶+6930t⁴−3564t²+243,

and its entire algebra K=Q[t]/(G), with theta the image of t. By L115
this is one degree-eight field. Let S consist of all maximal-ring primes
above {2,3,5,11}, and retain the real place as in L114. The global ambient
space is the supported part of

    H_Q={delta in K*/(K*² Q*): N_(K/Q)(delta) in 3025 Q*²}.

Use L122's audited entire localization K tensor Q2=L×L, actual
theta=(alpha,−alpha), complete square/norm/common-scalar conventions,
and exact five-class point image. No completeness of global supported
units or S-class two-torsion is assumed.

## Conclusion

All eight elements delta_abc=theta^a(1−theta)^b(1+theta)^c, a,b,c in
{0,1}, are nonzero S-units. Exactly two of them have the required global
norm class: delta_000=1 and delta_011=1−theta². The latter satisfies

    N_(K/Q)(1−theta²)=(1024/275)²,

but has local common-scalar quotient label (1,1), outside L122's image
{(0,0),(0,5),(0,8),(0,22),(2,6)}. Consequently the two-adic point filter
removes an identified element of H_Q(S); its intersection with that
supported global ambient space is proper. No rational point of C has
fake image [1−theta²]. Identity survives. This supplies no supported-class
enumeration, rational-point completeness, integer exclusion or Beal
resolution. The separate critical mathematical audit below passes.

## Proof

### Imported inputs and exact norm convention

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-23-marked-octic-small-global-witness.md`.
The general method is imported, not reproved. Precise standard inputs are:

- J.S. Milne, *Algebraic Number Theory*, v3.08, 19 July 2020,
  [author PDF](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
  integrality and Propositions 2.4/2.6 pp.26–28; multiplication-determinant
  norm, Proposition 2.19 and Corollary 2.20 pp.31–32; ideal norm and
  Proposition 4.1(c), with its non-Galois proof, pp.68–69. These give
  the conjugate-product formula, multiplicativity, and equality of the
  norm of a principal ideal with the element norm (up to its rational
  sign for ideal norms).
- Nils Bruin and Michael Stoll, *Two-cover descent on hyperelliptic
  curves*, Math. Comp. **78** (2009), 2347–2370,
  [DOI](https://doi.org/10.1090/S0025-5718-09-02255-8), inspected
  [arXiv:0803.2052v2](https://arxiv.org/pdf/0803.2052v2),
  21 October 2008, Section 2 p.3 and Section 6 pp.11–12: the even-degree
  norm fiber, common scalar quotient and localization filter. L114
  specializes these to C and fixes the leading coefficient and support;
  L122 supplies the full local image and exact local arithmetic.

Here the leading coefficient is 3025=55². Thus N(delta) in 3025 Q*²
is exactly the rational-square condition, including positivity. A single
rational scalar changes a degree-eight norm by its eighth power, so
this condition is well-defined on K*/(K*² Q*).

### All maximal places outside S

The monic polynomial of theta is f=F/275. Therefore theta, 1−theta and
1+theta are integral over Z[1/275]. Explicitly u=275 theta satisfies
the monic integral equation

    u⁸−786500u⁶+144122343750u⁴−5605329726562500u²
        +28902481402587890625=0.

This is exactly 275⁸ f(u/275)=0, not a maximal-order identification.
Every product in the family is consequently integral at every maximal
place over p outside {5,11}. If its degree as a polynomial in theta
is d, then 275^d delta_abc is an integer polynomial in u; all clearing
denominators have support in {5,11}.

The conjugate-product formula in the entire degree-eight field gives

    N(theta)=f(0)=243/275=3⁵/(5²*11),
    N(1−theta)=f(1)=1024/275=2¹⁰/(5²*11),
    N(1+theta)=f(−1)=1024/275.

The signs in the first and third formulas are positive since the degree
is even. These nonzero norms prove invertibility of all three generators
and all products. Each norm has numerator and denominator supported only
at the four stated rational primes. For a rational prime p outside them,
integrality makes every v_P(delta_abc) nonnegative, while the principal
ideal norm formula gives

    0=v_p(N(delta_abc))=sum_(P|p) f(P/p) v_P(delta_abc).

Every residue degree is positive, so every summand valuation vanishes.
This proves S-unit support at every maximal-ring place, without assuming
that Z[theta] or Z[u] is the maximal ring, and without cancellation of
positive and negative valuations in a rational norm.

### Complete family and norm parity

Multiplicativity yields, for all eight vectors,

    N(delta_abc)=3^(5a) 2^(10(b+c)) /
                         (5^(2(a+b+c)) 11^(a+b+c)).                 (1)

All values are positive. The exponent of 3 is even only when a=0;
then the exponent of 11 is even only when b=c. The other two exponents
are always even. Thus only 000 and 011 lie in the required norm fiber.
In particular N(delta_011)/3025=(1024/15125)², retaining the actual
curve leading coefficient. The complete table is below. The last
column is a local scalar-square class, computed even for rows that fail
the global norm test; such rows are not asserted to belong to H_Q(S).

| abc | Exact N(delta_abc) | Global norm-square? | Two-adic common-scalar label |
| --- | --- | --- | --- |
| 000 | 1 | yes | (0,0) |
| 001 | 1024/275 | no | (2,23) |
| 010 | 1024/275 | no | (3,4) |
| 011 | 1048576/75625 | yes | (1,1) |
| 100 | 243/275 | no | (0,5) |
| 101 | 248832/75625 | no | (2,3) |
| 110 | 248832/75625 | no | (3,2) |
| 111 | 254803968/20796875 | no | (1,25) |

There are no local collisions among these eight quotient labels. Equality
of two global scalar-square classes would imply equality after
localization, so none collide globally either. We do not infer global
equality from a local equality or assume generator independence.

### Exact localization of the rejected class

Use precisely L122's field L=Q2(pi), with its monic Eisenstein polynomial

    E(X)=(9150625X⁴−48315300X³+91279980X²
                          −74245842X+22130658)/9150625,

normalized by v_L(pi)=1 and v_L(2)=4. L122 defines

    r=468−1126pi+(2585/3)pi²−(5500/27)pi³,
    r²=2(pi−1), alpha²=1+4r,
    theta=(alpha,−alpha).

Thus the rejected product transports **exactly**, without an approximate
root substitution, to

    (1−alpha²,1−alpha²)=(−4r,−4r).

Both components have valuation 10. Divide by pi¹⁰, a square, before
labeling. Exact quotient-field multiplication and reduction in
O_L/pi⁹O_L, whose coefficient moduli are (8,4,4,4), gives

    (−4r)/pi¹⁰ = (1,2,3,3) modulo pi⁹.

This is precisely unit representative 25 in L122's lexicographic
convention. The pi⁹ test is exact because 9>2v_L(2)=8, as proved there.
The raw pair is therefore (25,25). Its complete orbit under the **one**
diagonal rational scalar image is

    {(1,1),(7,7),(11,11),(16,16),
      (20,20),(25,25),(27,27),(30,30)}.

Its canonical member is (1,1), absent from L122's exact point image.
Equivalently, 25 is outside the rational scalar label set
{0,5,8,12,15,19,22,29}, so this diagonal pair is not the identity class;
identity is the only diagonal class in the five-element point image.
This also proves that the global class [delta_011] is nonidentity.
No subgroup property of the point image is used.

For completeness, all other rows of the table use L122's certified
generator labels. The raw labels of theta, 1−theta and 1+theta are,
respectively, (22,8), (13,10) and (10,13). Multiplication in the full
square-class table followed by the same diagonal scalar projection
gives each displayed row. The finite alpha approximation differs from
the exact Hensel root by valuation at least 20. The component valuations
of these generators are (0,0), (6,4), (4,6); hence the relative error
bounds are (20,20), (14,16), (16,14), all strictly greater than eight.
Each generator label is exact; multiplying those certified labels
requires no unproved error bound for a product. The load-bearing 011
row also has the exact −4r computation above.

### Evidence, interpretation and limitations

Run from the active notebook:

    python3 scripts/pair-genus-two/marked_octic_small_global_witness.py
    python3 scripts/pair-genus-two/replay_marked_octic_small_global_witness.py

Full artifacts are
`scripts/pair-genus-two/marked-octic-small-global-witness-certificate.json`
and `scripts/pair-genus-two/marked-octic-small-global-witness-replay.json`.
The producer stores all eight exact coordinates, clearing denominators,
full multiplication matrices and rational determinant traces, complete
norm factorizations, every scalar orbit and all collisions. All 48 checks
pass: support rows 8/8, norm-admissible rows 2/8 and rejected rows 1/2;
the minimum generator relative precision is 14>8, with no failures.

The arithmetic replay imports neither producer nor local implementation.
It reconstructs all eight coordinates and matrices through companion
shifts, computes each determinant by the complete signed-permutation
formula, and compares all entries and norms. It independently normalizes
the exact −4r by ten multiplications by the polynomial expression for
pi^(-1), obtaining the full residue (1,2,3,3), label 25 and full scalar
orbit above. All 40 checks pass, with no failures. It uses L122's already
audited finite tables as inputs. This replay verifies instance arithmetic;
it is not a separate critical mathematical audit or new source approval.
The proof of support and norm parity is given above, not inferred from
certificate flags or previews.

The intermediate threshold is met: the local filter excludes an actual
supported global norm-square class. This is local notebook progress by
specializing known methods, not progress beyond the general theory
checked in the assessment. It does not compute the fake Selmer set or
show that this element passes any other place. L114's known rational
infinity points still have identity class and prevent an empty-set
shortcut. Global unit completeness, ordinary S-class two-torsion,
surviving-cover points, degree-nine root recovery, compatible remaining
factors, both L095 integer systems and minus-eleven remain unresolved.
L108 and ATTEMPTS/050–052 are preserved.

### Independent critical mathematical audit, 2026-10-24

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-24-marked-octic-global-witness-critical-audit.md`.
The independent audit confirms the entire statement without a mathematical
correction. This is REPRODUCTION of an instance of the cited norm and
descent methods, not a new general theorem. The mathematical inputs remain
L114, L115 and audited L122. Neither L116/L117 nor a class or unit backend
is needed. The producer/replay evidence above is preserved unchanged.

**Support and the global norm fiber.** L115 identifies the whole quotient
with a degree-eight field, so the conjugate-product and principal-ideal
norm theorems quoted above apply to exactly this K. Dividing F by 275
gives a monic polynomial over Z[1/275]. Closure of integral elements under
addition and multiplication puts all three generators and every product
in the integral closure of that ring. The displayed monic equation for
u=275 theta and each of the eight cleared integer expressions check
coefficientwise. Consequently every normalized maximal-prime valuation
over p outside {5,11} is nonnegative. The three nonzero rational norms
are obtained by evaluating F/275 at 0,1,−1, with the even-degree signs
retained. Multiplicativity gives (1) for every row. For p outside
{2,3,5,11}, the ideal norm has p-valuation zero, and its expression as a
sum of positive residue degrees times nonnegative maximal-prime
valuations forces each valuation to be zero. This proves S-unit support
at all such primes; rational-norm support alone would not prove it.
No polynomial-order ideal factorization or cancellation of opposite
valuations is used. The real place is retained for subsequent point
testing, not asserted to pass in this support argument.

All eight norm signs are positive. Their exact exponent vectors at
(2,3,5,11) are (10(b+c),5a,−2(a+b+c),−a−b−c). Hence square norm
requires a=0 and b=c, and these conditions also suffice. Because
3025=55², this is precisely L114's norm fiber, not a change of twist.
In particular the required ratio for 011 is
N(delta_011)/3025=(1024/15125)². Multiplication by a field square or
a single rational scalar preserves this condition: their norm factors
are respectively a square and an eighth power. The six failed rows
are S-units but are not members of H_Q(S), even if a local class agrees
with a local point class. This distinction is retained in every row.

**Exact local input, precision and all eight products.** The auditor
checks L122's polynomial, actual transport (alpha,−alpha) and input
certificate hash. In the specified quartic quotient it verifies the
exact r identity and reconstructs both Newton steps from beta=1+2r.
The residual valuations are 12,16,24 and the derivative valuation is
four, so the final approximation has error at least 20 relative to
the same exact Hensel root. The generator valuations are (0,0), (6,4),
(4,6), giving relative precision (20,20), (14,16), (16,14).
Every entry is strictly above 2v_L(2)=8. Thus the approximate/exact
ratios lie in the square neighborhood and the generator labels are
exact. For a product, each ratio is 1 plus an element of valuation at
least 14; their finite product has the same lower bound. This justifies
the additional direct product-label check for all eight rows without
assuming that the unnormalized approximation error stays 20 under
multiplication. The inherited square test uses precision 9>8.

The norm-free local arithmetic includes the six globally inadmissible
rows. Direct quartic multiplication and normalization recover the
generator labels (22,8), (13,10), (10,13) and every product label.
Each agrees with multiplication of the certified generator classes.
The exact identity delta_011=(−4r,−4r) supplies a separate check:
v_L(r)=2, hence each component has valuation ten, and pi^10 is a square.
The complete exact normalized coefficient vector, reduced in the
maximal-ring quotient, is (1,2,3,3), giving label 25. All eight scalar
orbit members printed above are checked. Their minimum is (1,1).
Only one rational scalar acts simultaneously on both components;
independent component scalars would change the quotient and are never
used. The complete eight product orbits have different minima, so
there are no local collisions and therefore no global collisions.
Localization equality is not used to infer global equality.

**Properness and its limits.** L122's exact image is the stated
five-element set, which omits (1,1). Localization of L114's fake map
commutes with evaluation, so a rational point with class delta_011
would give an impossible local point class. Thus, stated precisely,
the inverse image of the two-adic point image under localization meets
H_Q(S) in a proper subset. Identity lies in that subset, as witnessed
by each of the two distinct rational infinity points. This argument
uses no subgroup property of the five-element point image. It proves
neither that the removed class passes the real or other finite tests,
nor that this dyadic restriction is independent of those tests.
It computes no complete supported group or fake Selmer set, and gives
no rational-point or integer classification. All previously stated
independent gaps remain open.

Run the independent auditor from the notebook:

    python3 scripts/pair-genus-two/audit_marked_octic_small_global_witness.py

Full evidence is
`scripts/pair-genus-two/marked-octic-small-global-witness-audit-certificate.json`.
The standard-library auditor imports none of the producer, replay or
local implementation. It uses L122's already audited finite tables as
inputs rather than reauditing the local coordinate disks. All 74 checks
pass with no failures. For every row it reconstructs the entire global
multiplication matrix, every linked elimination pivot, the complete
signed-permutation determinant terms, the norm factorization, cleared
integral expression, both local labels, all eight scalar orbit members,
norm admissibility and point-image test. It compares all producer row
fields and all replay determinant terms, checks the replay's complete
normalized witness coefficients, and checks both saved reports for
comparison/flag consistency. The numerical margins are 14>8 for the
minimum relative generator precision and 9>8 for the square test;
the full family has eight rows, two admissible rows, one rejection and
zero collisions. The mathematical all-place argument and properness
review above are essential in addition to these arithmetic checks.

## Mathlib

Full coverage of this supported even-degree fake two-cover quotient,
its exact dyadic transports and this instance was not checked. Supporting
norm and integrality results are used through the precise Milne citation,
and the descent conventions through Bruin–Stoll and the canonical local
inputs. No absence or formal-verification claim is made.
