# L063 — The canonical witness kills the quotient obstruction

## Hypotheses

Use L045's degree-twelve field K, maximal integer ring O_K and
S consisting of every finite prime above five or eleven. Put

    V = Cl(K)/(5 Cl(K) + <[Q] : Q lies above five>).

The eleven primes P1,P2,P3 have generator residues 8,2,10 and
normalized maximal-DVR orders, as in L045. Write u=[P1] and v=[P3]
in V, and let rho:K(S,5) -> F5^3 be its ordered valuation projection.
Use L062's audited canonical global class alpha_sigma, for one fixed
rational identification of the entire fiber at s=9261/8 with K.
No integer solution, ordinary principality, computed class group,
unit basis, GRH, rank or Sha hypothesis is assumed.

## Conclusion

The previously unevaluated obstruction u vanishes:

    [P1] belongs to 5 Cl(K) + <[Q] : Q lies above five>.

Consequently, with W={(0,2,0),(2,0,0)},

    image(rho) intersect W = W,
    image(rho) = { (d1,d2,d3) in F5^3 : d3 v=0 }.

The remaining alternatives are image(rho)=F5^3, of size 125, if
v=0, or image(rho)={(d1,d2,0)}, of size 25, if v!=0.
No choice between these alternatives is made. Both vectors are attained
by global K(S,5) classes; the proof does not assert that both have
the same five-adic class or satisfy every other restricted local image.
The quotient obstruction cannot exclude the 54a1 branch.

## Proof

### Reused known inputs and specialization

L045 imports the ordinary fractional-ideal/class sequence and S-class
quotient from Romyar Sharifi, *Iwasawa Theory*, Chapter 1,
[author HTML](https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html),
Notation 1.1.1, Remark 1.1.2, Definition 1.3.19 and Proposition 1.4.5.
Its audited criterion retains arbitrary orders at every prime above five
and arbitrary fifth-power fractional ideal factors elsewhere. The
ordinary class group, rather than the narrow class group, is used.
L062 imports general point-class support and localization from
Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans.
AMS **356** (2004), 1209–1231,
[June 13, 2001 manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Proposition 4.6, p.7, and Section 5, pp.8–9. Its entire canonical-fiber
and local applications have been audited there. These imported general
results and existing proofs are reused, not reproved. Neither cited
general source evaluates this field-specific quotient class; the
approved SPECIALIZE step is their short combined application below.

### Matching the interfaces and applying the criterion

Both inputs use L033's same K and K(S,5), with every prime above five
and eleven. L062's support conclusion applies to its global point
without an integer-solution premise. Its local vector uses the same
P1,P2,P3 order, including uniformizer order one in the ramified third
factor. Thus L062 supplies d=rho(alpha_sigma) in W, in image(rho).
The fixed sigma need not be computed or chosen to distinguish the two
rational factors: both possibilities will give the same conclusion.

L045's exact necessity criterion gives

    (d1-d2)u+d3 v=0 in V.

For d=(0,2,0) this is -2u=0; for d=(2,0,0) it is 2u=0.
The group V is killed by five. Multiplication by two is invertible
there, since 2*3=1 modulo five; multiplication by minus two is likewise
invertible. Therefore u=0 in either case. By definition of V this is
exactly the stated ordinary-class subgroup membership.

Substitute u=0 in L045's full necessity-and-sufficiency criterion.
It yields image(rho)={d:d3 v=0}, and every vector of W has d3=0,
so both are attained. If v=0 this condition is vacuous. If v!=0,
its order is five, so d3 v=0 holds precisely when d3=0. This proves
both cardinality alternatives without deciding v or computing a class
basis. In particular L045's former size-five alternative is eliminated.

The achieved threshold is u=0 and the evaluated intersection with W;
it is not ordinary principality of P1 or even [P1] in 5 Cl(K) alone.
No power-order lattice identity or principal supported element is
constructed. The exhausted finite lists remain incomplete searches
and are not inputs. The witness's five-adic membership is not needed
for this quotient application. Full eleven-adic units, simultaneous
restricted images at all places and rational/integer power lifting
remain independent gaps. This is local notebook progress by reproduction
of assessed methods, with no claim of novelty beyond the sources checked.

### Independent critical application audit, completed 2026-10-13

The application passes without a mathematical correction. The approved
source coverage above is reused, as are L045's completed ideal-criterion
audit and L062's completed global-witness audit. This review checks their
combination; it does not repeat a source theorem, local enumeration or
finite generator search.

**Identical domain and places.** Both inputs use L033's field K and
all finite primes above five and eleven in S. L062 supplies a nonzero
global point class in K(S,5), using the general support theorem rather
than a premise that an integer solution exists. Its fixed rational
fiber identification is localized at every factor. The eleven-adic
coordinates are orders at the maximal primes with generator residues
8,2,10, in that order. These are precisely L045's coordinates: extension
to a completion preserves normalized uniformizer orders. In particular
the third order is not the extension of the rational valuation with
v11(11)=1. No permutation involving the degree-ten factor or division
by its ramification index is allowed. The two permitted rational-factor
orders are exactly the two possibilities already retained in L062.

**Necessity in both witness cases.** Write a for the one global class
from L062. Since a belongs to the domain of rho, its vector d satisfies
L045's necessary equation (d1-d2)u+d3v=0. The two possible d give
-2u=0 and 2u=0, respectively. By construction 5V=0. In the second
case multiplication by 3 gives 6u=u=0; in the first it gives -6u=-u=0.
Thus neither case requires a value of v or knowledge of which vector
the fixed identification produces. This proves membership of [P1] in
5 Cl(K)+<[Q]:Q above five>, with no smaller subgroup substituted.

**Sufficiency is indispensable and available.** For any integer lifts
of d, L045 tests D=sum d_i[P_i] in the ordinary class group. Membership
in its specified subgroup supplies integers e_Q and a fractional ideal
class a0 with D+sum e_Q[Q]+5a0=0. A fractional ideal A representing a0
makes product P_i^d_i product Q^e_Q A^5 principal, say (beta). At every
prime outside S the order of beta is a multiple of five; at P_i it
is d_i+5 ord_Pi(A). Consequently [beta] is in K(S,5) with vector d.
This is the already proved sufficiency interface, with all Q above
five, negative exponents and arbitrary fractional A retained. It needs
neither an S-unit generator nor an ordinary principal power of P1.
The relation (11)=P1 P2 P3^10 used in L045 reduces the images of the
three prime classes to u,-u,v. Substituting u=0 therefore gives the
asserted exact image {d:d3v=0}, rather than only a necessary superset.
Each vector of W has d3=0, proving both-vector attainment.

**Complete alternatives and their scope.** If v=0, all three coordinates
are free and there are 5^3=125 vectors. If v is nonzero, its order is
exactly five, since 5V=0. Any nonzero scalar in F5 is invertible, so
d3v=0 forces d3=0. The first two coordinates are free and there are
5^2=25 vectors. These exhaust the possibilities; the old size-five
case cannot occur after u=0. No finiteness or dimension calculation
of the whole class group is required beyond the existing ideal input.

These cardinalities concern the full valuation projection of K(S,5),
not the set of compatible connecting classes, its affine norm slice,
or an all-place intersection. The sufficiency witnesses need not be
global point classes and are not asserted to retain a prescribed
five-adic localization. L062's one point class passes its two stated
filters, but the quotient argument supplies no full eleven-adic unit
image, ordinary principality, value of v, or rational/integer lift.
The direct inputs remain exactly L045 and L062. The review confirms
the existing consequence and route retirement; it adds no restriction
or discovery beyond the cited and previously proved inputs.

## Mathlib

Full matching field-specific quotient consequence and canonical witness:
not checked. Supporting class-group quotient, normalized valuation and
F5-linear algebra results: not checked. Unknown coverage is not absence.
The separate critical application review above is complete.
