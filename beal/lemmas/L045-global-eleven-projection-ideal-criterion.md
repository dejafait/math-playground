# L045 — Ideal criterion and dichotomy for the global eleven projection

## Hypotheses

Let K=Q(k) be L033's degree-twelve number field, with its displayed monic
defining polynomial m, and let O_K be the **maximal** integer ring. Let S
contain exactly all finite primes above five and eleven, and use L033's
group K(S,5) of fifth-power classes with valuations divisible by five
outside S. All valuations below are orders in maximal-order discrete
valuation rings, normalized to give a uniformizer order one.

Let P1,P2,P3 be the global primes corresponding to L041's complete
eleven-adic factors, ordered by the generator residues 8,2,10. Their
ramification indices are 1,1,10 and residue degrees are all one. Let Q5
be the set of **every** prime above five. No decomposition or class data
at five is presumed computed. Write Cl(K) additively and set

    V = Cl(K)/(5 Cl(K) + <[Q] : Q in Q5>),
    u = image of [P1] in V,    v = image of [P3] in V.

V is a finite F5-vector space. Consider the valuation projection

    rho: K(S,5) -> F5^3,
    [alpha] |-> (ord_P1(alpha),ord_P2(alpha),ord_P3(alpha)) modulo five.

Use L044's audited local filter W={(0,2,0),(2,0,0)}. There is no
assumption on GRH, a computed class group, units, rank, Sha, or equality
of Selmer classes with global point classes.

## Conclusion

The exact, but not numerically evaluated, criterion is

    image(rho) = {d in F5^3 : (d1-d2)u+d3 v=0 in V}.

Its cardinality is 5^(3-r), where r=dim_F5 span{u,v}, so is one of
5,25,125. The intersection relevant to this branch has the dichotomy

    image(rho) intersect W = W   if u=0,
                           empty if u!=0.

Exactly one survivor is impossible. Both local vectors are global
valuation vectors if and only if [P1] belongs to
5 Cl(K)+<[Q]:Q in Q5>. This does **not** determine whether u vanishes,
compute the projected image, or exclude the branch. Even when both
vectors survive, no simultaneous unit-class, other-place, modular-fiber,
positivity or integer-power lifting is established.

## Proof

### Imported structure and reason for specialization

The principal fractional ideal/class sequence and its number-field
scope are imported from Romyar Sharifi, *Iwasawa Theory*, Chapter 1,
[author HTML](https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch01.html),
Notation 1.1.1 and Remark 1.1.2; the S-class quotient is Definition
1.3.19, and the S-unit/Kummer/S-class five-torsion sequence is
Proposition 1.4.5. The live version was inspected on 2026-10-10 in the
prior assessment; no source revision date was identified. In the
Kummer statement take n=5 and include the infinite places together
with all places over five. No containment of mu_5 in K is required;
the following lemma's root-of-unity hypothesis is not used. Infinite
places add no odd-power sign constraint here.

Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, Trans.
AMS **356** (2004), 1209–1231,
[DOI](https://doi.org/10.1090/S0002-9947-03-03366-X),
[June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 5, printed pp.8–9, supplies the general K(S,p) construction and
unit/class exact sequence already used in L033. The ideal-map argument
in the proof of Theorem 8.1, printed p.21, is a comparison only: its CM
and split-prime dimension theorem is not applied to K.

These general structure results are imported, not reproved. The following
argument is the assessed specialization to projection at a proper subset
of S, with freedom at five retained. It is necessary because neither
source computes these two classes for this field. It avoids a stronger
full S-unit/S-class computation and does not replace K(S,5) by S-units.
Unique factorization of fractional ideals in O_K, as used in the cited
principal-ideal sequence, is used throughout; factorization in Z[k]
is not substituted.

### Necessity and sufficiency of the ideal criterion

First use arbitrary d in F5^3, choosing integer representatives d_i.
Put D=sum d_i[P_i] in Cl(K). We claim d is attainable precisely when

    D belongs to 5 Cl(K)+<[Q]:Q in Q5>.

For necessity take alpha in K^* with class in K(S,5) and projected
vector d. For each Q in Q5 set e_Q=ord_Q(alpha). At P_i subtract
d_i from ord_Pi(alpha); the difference is divisible by five. At every
prime outside S the order is divisible by five by the definition of
K(S,5). The prime exponents of a fractional ideal have finite support,
so unique ideal factorization gives a fractional ideal A with

    (alpha) = (product P_i^d_i)(product Q^e_Q) A^5.

Taking ideal classes gives D+sum e_Q[Q]+5[A]=0, proving necessity.
This also shows that the criterion is independent of integer lifts d_i.

For sufficiency membership supplies integers e_Q and a class a in Cl(K)
such that D+sum e_Q[Q]+5a=0; signs can be absorbed in e_Q and a.
Choose a fractional ideal A representing a. The fractional ideal

    I=(product P_i^d_i)(product Q^e_Q) A^5

has trivial class. By the principal-ideal sequence I=(alpha) for some
alpha in K^*. Outside S its prime exponents are multiples of five,
and its orders at P_i are d_i modulo five. Thus [alpha] is in K(S,5)
and has the desired projection. A may contain primes in S as well;
their fifth-multiple exponents do not change the projection.

No restriction was imposed on e_Q. In particular this sufficiency
argument retains classes coming from S-class five-torsion, rather than
silently restricting the search to elements whose ideals have support
only in S. Such supported elements are a sufficient witness source,
not asserted to generate the required image.

### Reduction to two classes and the local dichotomy

L041's complete local algebra identifies exactly three primes above
eleven in the maximal order. The prime factorization of (11), using
their proved ramification indices, is

    (11)=P1 P2 P3^10.

Consequently [P1]+[P2]+10[P3]=0 in Cl(K). In V every class is killed
by five, so the images of [P1],[P2],[P3] are u,-u,v. The preceding
criterion becomes (d1-d2)u+d3 v=0. The map F5^3 -> V in this formula
has image span{u,v}: (1,0,0) maps to u and (0,0,1) to v. Its kernel
has dimension 3-r, which proves the cardinality statement. These are
conditional alternatives, not an evaluated rank.

The two vectors in W map to -2u and 2u. The scalar 2 is invertible
in F5, so each lies in the kernel exactly when u=0. Equivalently,
the global class of rational eleven has vector (1,1,10)=(1,1,0)
modulo five, and the two local vectors sum to twice that vector;
membership of one forces membership of the other in the subgroup.
This proves the dichotomy without a class-group computation or use of
L034's affine norm plane for arbitrary global classes.

### Bounded exact witness search and its limits

The implementation `python3 scripts/global-eleven-valuation/check_small_norms.py`
saves every tested element and exact norm in
[the certificate](../scripts/global-eleven-valuation/small-norm-certificate.json).
It tests 61 linear elements k+c, c in [-30,30]; 87,846 quadratic elements
a k^2+b k+c, a in [1,6], b,c in [-60,60]; and 15,625 monic cubic
elements k^3+a k^2+b k+c, a,b,c in [-12,12]. Actual and required count
are both 103,532; there are zero nonzero norms supported only on 5,11.
All norms are nonzero. The earlier monic-quadratic preliminary box is
included in this final certificate.

The norm calculation is exact. For g of degree d, N_K/Q(g(k)) is
Res(m,g) because m is monic and defines K. For linear g=X+c it is
m(-c), since deg(m)=12 is even. For quadratic g=aX^2+bX+c, Horner
reduction computes a^12 m modulo g as uX+v. If beta1,beta2 are the
roots of g with multiplicity, their sum is -b/a and product c/a, so

    Res(m,g) = a^12 product m(beta_i)
             = (a v^2-b u v+c u^2)/a^13.

The script checks this division exactly. For a monic cubic g it computes
R=m modulo g; multiplication by R on Q[X]/(g) has determinant
Res(g,m)=Res(m,g), since 12·3 is even. This determinant identity holds
also for repeated roots. Eight selected norms were independently
checked as twelve-dimensional multiplication determinants on Q[X]/(m);
all eight exact comparisons, full search bounds, empty hit list and
three checks were inspected completely. Selected comparisons check the
implementation; the formulas and exhaustive finite loops specify the
bounded calculation. They are not a certified class table.

Since k is integral and g has integer coefficients, any hit would be
integral in O_K. A nonzero norm with support only at five and eleven
would force its principal ideal to have support only above those primes,
by the maximal-order ideal norm formula. Hence it would give a class in
K(S,5), even without proving Z[k]=O_K. No such witness was found in
these boxes; this is **not** a proof that no suitable element exists.
Other K(S,5) representatives may also have prime exponents divisible
by five outside S and norms with other prime divisors, so this sufficient
test is deliberately incomplete. No outside primes were canceled or
assigned valuations without a proof.

The required threshold was an exact projected image and its evaluated
intersection with W. Only the rigorous criterion and dichotomy are
achieved. Evaluating u,v still needs complete certified ideal relations
or sufficient exact witnesses; neither is presently available. The
bounded search does not supply a route to absence. Dependent global
arithmetic is parked pending materially new input, while an independent
local condition can be assessed. No branch or signature is excluded.

### Independent critical audit, 2026-10-10

The logical criterion, cardinality alternatives and dichotomy pass without
a mathematical correction. This audit uses the approved principal-ideal
and S-class sources cited above; it does not evaluate the quotient classes
or rerun the separate bounded polynomial search.

First, rho is well defined on K^*/K^{*5}: multiplying a representative by
beta^5 changes every normalized order by five times an integer. Its
restriction to K(S,5) is a homomorphism of F5-vector spaces. For an
integer lift d, write J_d=product P_i^d_i. If alpha realizes d, the
fractional ideal

    (alpha) J_d^(-1) product_{Q in Q5} Q^(-ord_Q(alpha))

has every prime exponent divisible by five, including those at all P_i
and Q. Unique factorization in O_K therefore makes it A^5. Negative
orders cause no problem for fractional ideals. Taking classes proves
necessity. Conversely, membership of [J_d] in the stated subgroup gives
a class a and integers e_Q with [J_d]+sum e_Q[Q]+5a=0. Represent a by
any fractional ideal A. Triviality of the class of J_d product Q^e_Q A^5
means exactly that this fractional ideal is (alpha) for a nonzero field
element. Outside S its orders are multiples of five, and at P_i they
are d_i+5 ord_Pi(A). This proves sufficiency with no integrality or
support restriction on A. Replacing d_i by d_i+5n_i merely adds
5 sum n_i[P_i] to its class, so arbitrary lifts give the same test.

In particular this argument never asks that alpha be an S-unit.
It retains the nonzero fifth-multiple orders outside S that can occur
for lifts of S-class five-torsion. It also allows arbitrary orders at
every prime above five, including contributions from A. Identifying
individual five-adic primes or computing their number is unnecessary:
Q5 is the complete set, not a selected subset. The ordinary ideal class
group is the appropriate group; no total positivity condition occurs
in K(S,5), so a narrow-class obstruction must not be inserted. No
assumption mu_5 subset K is needed for this ideal argument.

The local-to-global prime identification was checked from L041's full
factorization proof, rather than from reduction in the power order.
Its two simple factors have roots congruent to 8 and 2. After the shift
X=U-1 the remaining monic factor G reduces to U^10, and its complementary
factor H has unit constant term. Since m(-1)=-209 has eleven-adic
valuation one, G is Eisenstein. Thus the complete tensor algebra has
exactly the three stated fields, with ramification indices 1,1,10 and
residue degrees one. The correspondence between completions and
maximal-order primes yields (11)=P1 P2 P3^10. This identity uses
ramification indices, unlike the norm-valuation identity, which uses
residue degrees. No assertion O_K=Z[k] enters the argument.

The quotient V is killed by five. Hence the principal-ideal identity
gives [P2]=-u in V, and the criterion is precisely the kernel of the
map d |-> (d1-d2)u+d3v. That map has image span{u,v}, so its rank is
0,1 or 2 and its kernel has respectively 125,25 or 5 elements. L044's
already audited set W maps to {-2u,2u}; multiplication by 2 is invertible
in V, proving both implications of the both-or-neither conclusion.
As a separate consistency check, [11] is in K(S,5) and projects to
(1,1,0); the two elements of W sum to twice this vector. Subgroup
closure thus also rules out exactly one survivor. This does not place
the whole subgroup in the affine norm plane: its zero vector is outside
that plane, whereas compatible connecting classes have coordinate sum
two. The distinct uses of these sets remain essential.

The audited threshold is the equivalence and its conditional intersection,
not an evaluated intersection. Whether u=0 is still unknown. Even a
proof that u=0 would supply valuation witnesses only, not matching unit
classes, common global modular points or integer solutions. The audit
adds no mathematical restriction beyond the existing conclusion and no
claim beyond the assessed source methods. Mathlib coverage remains
not checked. The previously recorded finite search is preserved and is
not an input to this logical audit.

## Mathlib

Full matching field-specific projection, quotient-class and dichotomy
theorems: **not checked**. Supporting fractional ideal factorization,
class-group quotient, norm/resultant and finite-vector-space declarations:
**not checked**. Unknown coverage is not evidence of absence. This is
REPRODUCTION of assessed ideal methods, with a local specialization and
bounded calculation, not a claim of progress beyond the checked general
source theory.
