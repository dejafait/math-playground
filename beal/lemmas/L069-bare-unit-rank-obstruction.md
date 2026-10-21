# L069 — The bare norm-square unit space cannot certify rank below twelve

## Hypotheses

Let K be the entire degree-twelve number field of L033, defined by

    m(k)=k^12-6k^10+6k^9-6k^8-126k^7+104k^6+468k^5
         +258k^4-456k^3-1062k^2-774k-380.

Let E0/K be L033's curve y²+y=x³−x²−10x−20. Put

    g(X)=X³−4X²−160X−1264,     D=K[X]/(g),
    U_F=O_F^*,
    V=ker(N_D/K: U_D/U_D² -> U_K/U_K²).

For the ambient diagnostic, let W be any F2-vector subspace of D*/D*²
that contains the global two-descent Kummer image and retains the entire
image of V. In particular, a norm-square space with only finite valuation
support restrictions retains V, for any finite support set: ordinary units
have zero valuation at every finite prime. No finite-place image conditions
or class-group assumptions are imposed in this diagnostic.

The degree and field assertion for K are the unconditional field input of
L033, not FNS's GRH-dependent Selmer dimensions. L038 identifies the entire
algebra K tensor Q5 as Q5 × U_11, and hence supplies a rational Q5 place.
No primitive integer solution is assumed or constructed.

## Conclusion

D is a single degree-36 number field, not a selected component of an
étale algebra. The signatures of K and D are respectively (2,5) and (2,17).
The actual rational two-torsion is E0(K)[2]={O}, and

    dim_F2 U_K/U_K² = 7,
    dim_F2 U_D/U_D² = 19,
    dim_F2 V = 12.

V injects into D*/D*². Thus every W as above satisfies

    dim W − dim E0(K)[2] >= 12 > 11.

Such an unfiltered ambient space cannot supply the proposed rank upper
bound below twelve. This is a lower bound on the size of an upper space,
**not a lower bound on the Mordell–Weil rank**. It does not obstruct a
smaller containing space obtained by necessary finite local conditions,
nor determine any class group, Selmer group, subgroup index or integer
solution. Rank E0(K)=rank E1(K) by L033's dual isogenies and the named
Mordell–Weil theorem, but no value of either rank follows here.

## Proof

### The integral model, whole algebra and rational two-torsion

The invertible K-change X=4x and Y=8y+4 gives Y²=g(X): using the
original equation, both sides reduce to
64x³−64x²−640x−1264. Its monic integral cubic has discriminant

    disc(g)=−256·11^5=−41229056 != 0.

The origin-preserving change also preserves two-torsion. On Y²=g(X),
a nonidentity point has order two exactly when Y=0, since its negative
is (X,−Y). Thus rational nonidentity two-torsion is equivalent to a K-root
of g.

Project L038's whole local algebra to its Q5 component. This gives a
field embedding K -> Q5: the unital homomorphism from the number field K
is injective. Reduction of g modulo five is X³+X²+1, whose values at
0,1,2,3,4 are respectively 1,3,3,2,1. It has no root. A root of the monic
integral g in Q5 would belong to Z5 (alternatively, a negative valuation
makes its leading cubic term uniquely minimal), and its residue would
be a root of that polynomial. Consequently there is no root in Q5,
and hence none in K. A reducible cubic over a field has a linear factor,
so g is irreducible over K. D is therefore a field of degree three over
K and degree thirty-six over Q, and E0(K)[2]={O}.

This place argument can also be checked directly without using the
degree-eleven factor: m(0)=−380 is zero modulo five and m'(0)=−774 is
one modulo five. Simple-root Hensel lifting gives the same type of Q5
embedding. The proof uses the complete L038 input; this direct check
is a consistency check, not an assumption of a split global cubic.

### All archimedean places

Apply the standard named Sturm theorem to m. The certificate's full
primitive Sturm chain starts with m and m'/6; at every subsequent step
it takes the negative remainder and multiplies by a positive rational
number. Its degrees decrease successively from twelve to zero. The
signs at negative and positive infinity are

    + − + − − − + + − + + + −       (seven variations),
    + + + + − + + − − − + − −       (five variations).

The last polynomial is −1, so no repeated-root qualification is missing.
Sturm's theorem gives exactly 7−5=2 real roots. Since m defines K and
has degree twelve, K has r1=2 and r2=5. Full polynomials, division
quotients, remainders and positive normalization constants, rather than
rounded roots or sampled signs, are recorded in the certificate below.

The real cubic g has negative discriminant and hence one real root
and one nonreal conjugate pair. Equivalently, its entire Sturm chain
is g, 3X²−8X−160, 62X+751, −1, with variation counts two and one.
For EACH real embedding of K, D therefore becomes R × C. For EACH
complex place of K it becomes C³. These account for every factor,
giving r1(D)=r1(K)=2 and r2(D)=r1(K)+3r2(K)=17. The degree check is
2+2·17=36.

At a real base place the square-class groups of R × C and R are both
of order two, and the norm is their sign isomorphism: the complex
factor contributes a positive real norm and has trivial square classes.
Thus every norm-square unit already has trivial local class there.
Complex places have trivial square classes. No extra archimedean
Kummer restriction can remove classes from V in this signature, and
no assumption of total reality or odd narrow class number enters.

### Full unit square classes and their norm

Import the named Dirichlet unit theorem in the form recalled in Denis
Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[DOI](https://doi.org/10.1112/S1461157000000668), Section 1.2, printed p.8:
U_F is the product of the finite cyclic roots-of-unity group and a free
abelian group of rank r1(F)+r2(F)−1. In characteristic zero the cyclic
roots-of-unity group has even order, so its quotient by squares has
dimension one. Hence dim U_F/U_F²=r1(F)+r2(F), including ALL units
and the roots-of-unity contribution. The signatures just proved give
dimensions seven for K and nineteen for D. Found units or an uncertified
subgroup are not substituted for the full unit groups.

Inclusion of scalar units induces i:U_K/U_K² -> U_D/U_D². Norm induces
a homomorphism n in the reverse direction: norms of units are units
and norms of squares are squares. Since [D:K]=3,

    n(i([u]))=[u³]=[u].

Thus n is surjective and i is injective. Rank-nullity gives
dim V=19−7=12, without class-group information or independent norm
surjectivity on unsquared unit groups.

For completeness U_F/U_F² -> F*/F*² is injective for either field F.
If u in U_F equals a² with a in F*, then for every finite prime
2v(a)=v(u)=0. Thus a and a^−1 are integral, and a is a unit. Applying
this to D proves the asserted injection of V; applying it to K shows
that its unit-square norm condition is exactly the norm-square
condition in K*/K*². Finite valuation support restrictions cannot
delete any such ordinary unit class.

This is the elementary Dirichlet/norm argument inspected in Barrera
Salazar–Pacetti–Tornaría, *On 2-Selmer groups and quadratic twists of
elliptic curves*, [arXiv:2001.02263v3](https://arxiv.org/pdf/2001.02263v3),
September 17, 2020, Lemma 2.14 and its complete proof, printed pp.12–13.
Here its field situation is justified by the irreducibility proof above;
their notation gives a=2, b=0, c=5 and a+2b+2c=12. We do not invoke
Hypotheses 2.1 or their global Selmer bound. The short unit argument
is retained to identify exactly why no narrow-class or finite-place
hypothesis from that section is needed for this diagnostic. It is a
reproduction and explicit specialization of known mathematics.

### Comparison with the required threshold

For this integral irreducible cubic, Simon Section 1.1, Propositions
1.1–1.2, printed p.8, give the Kummer injection
E0(K)/2E0(K) -> D*/D*² with square norm. The standard Mordell–Weil
theorem gives dim E0(K)/2E0(K)=rank E0(K)+dim E0(K)[2]. Therefore a
finite-dimensional containing space W provides the sufficient bound

    rank E0(K) <= dim W − dim E0(K)[2].

Since V embeds in W and two-torsion dimension is zero, the right-hand
side is at least twelve, exceeding the required eleven. An infinite
unfiltered space is equally incapable of this finite upper certificate.
The failure is intrinsic to retaining all norm-square units, even before
adding S-units or class contributions. A necessary finite local condition
could remove unit classes; that is a different target, not disproved here.

### Exact verification and qualifications

Run `python3 scripts/bare-unit-rank/check_diagnostic.py`.
The full [certificate](../scripts/bare-unit-rank/diagnostic-certificate.json)
records the two entire Sturm chains and exact divisions, cubic
discriminant, model identity, all five residue values, both signatures
and dimensions. All ten checks pass with no failures. The actual
corrected ambient lower bound is twelve; the required upper-bound
threshold is eleven. The complete load-bearing Sturm and residue
records were inspected, as were the full dimension and check fields.
The certificate verifies arithmetic only; the unit, norm, embedding and
Kummer applicability arguments are given above. The separate independent
critical review below confirms this diagnostic. No branch exclusion follows.

### Independent critical audit (2026-10-14)

The audit finds no correction to the statement or proof. Run
`python3 scripts/bare-unit-rank/audit_diagnostic.py`; its complete
[audit certificate](../scripts/bare-unit-rank/audit-certificate.json)
records 33 passing checks and no failures. It imports no code from the
original checker and does not rerun that checker. All seventeen recorded
Sturm polynomials and all thirteen recorded divisions are checked over Q.
For each division it verifies the coefficient identity A=QB+R by
convolution, deg R<deg B, and the next polynomial = -cR with c>0.
Uniqueness of Euclidean division identifies these witnesses with the
true remainders. The initial derivative scalings are 1/6 and 1, both
positive; both terminal constants are -1. Every infinity sign and
variation is recomputed. Neither sampled roots nor the original script's
success flags stand in for the Sturm proof. The discriminant is independently
calculated by a Sylvester determinant. The complete model, residue,
Hensel, signature and dimension records are also checked.

The field assertion for K is L033's cited unconditional FNS input, not
a consequence of this arithmetic certificate. Its defining coefficients
match exactly. The rational Q5 projection in L038 is an injective map
from that field, so a K-root of g would produce a Q5-root. Monicity and
the five nonzero residue values exclude this. This proves irreducibility
over K, the entire degree-36 field assertion and the zero two-torsion
correction without a class hypothesis. All real and complex embeddings
are counted: each of the two real places gives R times C, and each of
the five complex places gives C cubed. The signatures and degree total
therefore agree with the exact Sturm data.

The unit proof uses the full Dirichlet groups, with roots of unity
included. Norm of a unit and of its inverse is integral, so the norm
map on units is defined; the identity n i=[3]=1 on square classes
proves surjectivity. If a field square is a unit, its square root has
valuation zero at every finite prime, proving the unit-square injection.
The dimension difference is therefore twelve inside D*/D*², not twelve
classes in an unverified unit subgroup. At every real place the norm
kernel on square classes is trivial, so archimedean conditions do not
repair the unfiltered bound. This uses the elementary argument of the
cited Lemma 2.14 without that paper's separate narrow-class or finite-place
Selmer hypotheses.

Simon's integral irreducible-cubic assumptions are met; Mordell–Weil
supplies the rank-plus-two-torsion dimension formula. The dual isogenies
of L033 identify the ranks after tensoring with Q. The audit accepts only
the failure of upper spaces that retain V: their corrected size is at
least twelve, against required at most eleven. It gives no actual rank
lower bound and no reason to reject genuine finite local restrictions.
The arithmetic audit and application review are complete; the global
rank and integer problems remain open.

## Mathlib

The complete explicit field/unit obstruction and matching theorems:
**not checked**. Supporting Sturm, Dirichlet units, integral units,
field norm, Kummer and Mordell–Weil declarations: **not checked**.
Unknown coverage is not absence. This is classified REPRODUCTION,
with no claim of progress beyond the standard theorems checked.
