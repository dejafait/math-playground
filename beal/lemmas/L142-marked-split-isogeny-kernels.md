# L142 — The two finite split-isogeny modules and the point-test limit

## Hypotheses

Work over Q with L110, L111, L113 and L127's smooth proper curves

    Q4(T)=7+52T−6T²−64T³−25T⁴,
    a(T)=−3(T²−4), b(T)=−33Q4(T),
    B: W²=a(T)b(T)/9,
    D: h²=a(T), R²=b(T), E: R²=b(T), O_E=(2,165).

Use the proper maps p_B(T,h,R)=(T,hR/3), p_E(T,h,R)=(T,R),
the proper Q-isomorphism alpha:C→D of L113, and L127's isogenies

    F:Jac(B)×E→Jac(C), F(x,e)=alpha^*(p_B^*x+p_E^*e),
    G:Jac(C)→Jac(B)×E, GF=[2], FG=[2].

Here E is identified with Pic^0(E) by P↦[P−O_E]; p_E^* is the
actual Prym inclusion, not an unspecified isogeny. The cover p_B is
connected and unramified. For the final assertion about all rational
point pairs, also use L138's irreducible quartic H and its exact
coordinate transport from Q4. No rank, Selmer completeness, rational
point completeness or integer recovery is assumed.

## Conclusion

Let Ω be the four roots of Q4 in Qbar, with its actual Q-Galois action.
Put M=F_2^Ω, M_even={v:sum v_i=0}, and 1=(1,1,1,1). Then, as
finite Q-Galois modules,

    ker F ≅ M_even,                 ker G ≅ M/<1>.       (1)

Both isogenies have degree eight. Equivalently, for the finite étale
Q-algebra A_4=Q[T]/(Q4), these finite étale group schemes are

    ker F ≅ ker(N:Res_(A_4/Q) μ_2→μ_2),
    ker G ≅ (Res_(A_4/Q) μ_2)/μ_2,                     (2)

where the last μ_2 is diagonal. These are geometric module descriptions
with the specified root-permutation action, not assertions that eight
kernel points are rational. They require no choice of square roots of
a at the quartic roots, and no computation of an abstract splitting-field
group. The embeddings into the Jacobians are specified in the proof.

The correctly directed rational joint-image condition on
(x,e)∈Jac(B)(Q)×E(Q) is

    δ_G(x,e)=0 in H^1(Q,ker G).                           (3)

It holds exactly for pairs in G(Jac(C)(Q)). It is a necessary condition
for an Abel image of a marked point, not a sufficient condition for such
a point. With q_+=(2,0)∈B(Q) and d_0=(2,0,165)∈D(Q),

    G(alpha^*[d−d_0])=([p_B(d)−q_+],[p_E(d)−O_E]).       (4)

For every rational same-T pair q=(t,w)∈B(Q), P=(t,r)∈E(Q), one has
r≠0 and a rational marked lift d=(t,3w/r,r). Consequently (3) for
([q−q_+],[P−O_E]) adds no restriction to these exact same-T equations.
For an E-point alone, the remaining condition is still precisely
L111's h²=a(t). No nonredundant test on separately represented quotient
Kummer classes, rank improvement or Beal exclusion is established.

## Proof

### Imported kernel construction and the actual branch classes

The prior assessment is
`drafts/literature/2026-10-26-marked-split-isogeny-kernel-descent.md`
(SPECIALIZE). Import Jordan Docking, *2-infinity-Selmer rank parities
via the Prym construction*, J. Number Theory 265 (2024), 208–225,
DOI [10.1016/j.jnt.2024.06.009](https://doi.org/10.1016/j.jnt.2024.06.009),
[arXiv:2108.09564v2](https://arxiv.org/pdf/2108.09564v2), 24 July 2023:
Lemma 4.1 and proof p.6, Lemma 5.3 p.8, Section 5.2.2 pp.8–9,
and Proposition 5.4 Case II and its proof p.9. The statements give
the graph kernel, the reverse kernel p_B^*(Jac(B)[2]), and the
branch-pair preimages for the split quartic/quadratic cover. We import
these theorems; the following work fixes their labels and maps here.

The factors in Case II are f=b/9 with coordinate R/3 and g=a with
coordinate h. Their product is exactly B's polynomial; their simple
root sets are disjoint by L111. L127 verifies the connected unramified
cover and identifies this quartic factor's Jacobian with E through the
actual p_E pullback over Q, using Bruin, *The arithmetic of Prym
varieties in genus 3*, Compositio Math. 144 (2008), 317–338,
DOI [10.1112/S0010437X07003314](https://doi.org/10.1112/S0010437X07003314),
[arXiv:math/0408069v2](https://arxiv.org/pdf/math/0408069v2),
Section 2.2 Proposition 2.2 and proof pp.4–5. Thus no twist or
polarization identification is being substituted in the kernel theorem.

Write q_±=(±2,0) and q_i=(θ_i,0) on B, and e_i=(θ_i,0) on E,
where θ_i ranges over Ω. Let H_B and H_E denote the degree-two
divisor classes of a T-fiber on the respective curves. For an even
branch subset S define its class by the sum of its branch points minus
(|S|/2)H. This is the even-subset description of two-torsion, with
complementary subsets identified. In particular a pair has class
[q_i−q_j], since 2q_j∼H_B; the analogous statement holds on E.
One must use H_E here, not assume H_E∼2O_E.

The cover class is

    ε=[q_++q_−−H_B]=[q_−−q_+].

Indeed div_B(a)=2(q_++q_−−H_B), and adjoining its square root is
the actual function extension Q(D)/Q(B). Its geometric class is
nonzero: the two-element subset {+,-} is neither empty nor the full
six-element branch set. The constant in a is retained in the cover;
this divisor calculation does not identify different Q-twists.

For S⊂Ω even, write x_S for its class on B and e_S for its class
on E, with e_S interpreted in (E,O_E). The map S↦x_S is injective:
two distinct subsets entirely inside Ω cannot be complements in the
six-element set. Moreover x_Ω=ε and e_Ω=0. Proposition 5.4 gives

    p_B^*x_S=p_E^*e_S.                                  (5)

For a two-element S the actual pullbacks of the branch differences
both have the two points (θ_i,±sqrt(a(θ_i)),0) over each θ_i,
with matching signs as divisors. This checks the coordinate transport
in (5), including the radical index at each point; it avoids the
apparent radical-index typo in the last Case II display of the source.
The empty/full subsets follow from the zero class and ε, or additivity.
No choice of the radicals enters the divisor sum.

Docking Lemma 5.3 says that ker F consists exactly of the pairs
(x,e)∈Jac(B)[2]×E[2] with p_B^*x=p_E^*e. Each e has the two
preimages x and x+ε. The four E[2] classes are the even subsets
of Ω modulo Ω; hence all eight pairs, with no omissions, are

    S↦(x_S,e_S),                 S⊂Ω even.               (6)

This proves the first isomorphism in (1), with the embedded kernel.
Every operation in (6) is defined over Q, so σ sends S to σS.

### Reverse kernel and its Galois action

The reverse map is exactly L127's transported version of Docking's
map; no transpose convention is needed. Lemma 4.1's proof gives

    ker G=alpha^*p_B^*(Jac(B)[2]),
    ker(p_B^*:Jac(B)[2]→Jac(D)[2])=<ε>.                  (7)

Thus its abstract module is Jac(B)[2]/<ε>. In the six-branch
description, a vector v∈M representing S⊂Ω maps to the even subset

    S ∪ {+ if |S| is odd}.

Then take the branch class, apply p_B^*, and transport by alpha^*.
This is an F_2-linear map. It is onto (7): after adding ε as necessary,
any even six-branch subset can be represented with the minus branch
absent, at which point the plus branch is fixed by the parity of S.
The vector 1 maps to x_Ω=ε, hence to zero. There are no other
relations: Jac(B)[2] has dimension four, and its quotient by the
nonzero ε has dimension three, while M has dimension four. This
proves the second isomorphism in (1).

In explicit generators, put

    z_i=alpha^*p_B^*[q_i−q_+].

The z_i generate ker G; their only F_2-relation is sum_i z_i=0,
and σ(z_i)=z_(σi) because q_+ is rational. For ker F the actual
classes (6) give the even permutation module. These descriptions
fully specify the Q-Galois action through the roots of the displayed
Q4; they do not replace it by a trivial action. Over Qbar, μ_2 is
the constant F_2 module. Norm is sum of the four coordinates and the
diagonal μ_2 is <1>, giving exactly (2). Characteristic zero makes
the isogeny kernels finite étale; their eight geometric elements
therefore give degree eight for each map.

### The direction and normalization of the joint-image condition

Use the ordinary connecting homomorphism of the exact Galois-module
sequence

    0→ker G→Jac(C)(Qbar)→(Jac(B)×E)(Qbar)→0.

Concretely, choose z over Qbar with Gz=(x,e); the cocycle
σ↦σz−z defines δ_G(x,e). Its class is zero exactly when one can
subtract a kernel element from z to make it Q-rational. This is the
usual isogeny connecting construction, as in E.F. Schaefer,
*Computing a Selmer group of a Jacobian using functions on the curve*,
Math. Ann. 310 (1998), 447–471, DOI
[10.1007/s002080050156](https://doi.org/10.1007/s002080050156),
[corrected arXiv:1507.08325v1](https://arxiv.org/pdf/1507.08325v1),
Section 2 pp.2–3. Only this connecting construction is used; its
cocycle description applies to the present product target as written.
The function-evaluation algorithm and its cohomological injectivity
hypotheses are not being imported for G. A pair is in G's target,
whereas δ_F would take a class in Jac(C)(Q).

It remains to check (4), rather than assume its second component.
On D let τ(T,h,R)=(T,−h,R) and κ(T,h,R)=(T,h,−R). Then
ι=τκ is the deck involution over B. L113 transports κ to the
hyperelliptic involution (t,Y)↦(t,−Y), so κ_* acts as −1 on
Jac(D). Explicitly, d+κ(d) is a fiber of D→{h²=a(T)}; the
base conic has genus zero, so these fiber divisors are linearly
equivalent over Qbar. On degree-zero divisor classes this proves
1+κ_*=0. This short check identifies the actual involutions; it
is not a new general hyperelliptic theorem.

The pullback/norm identity for the degree-two quotient p_E gives

    p_E^*p_E,*=1+τ_*=1−ι_*.

The identity holds on divisors, also at ramification points with their
multiplicities, hence on Jacobians. Because j=p_E^* is an isomorphism
onto the Prym by L127, L127's j^(-1)(1−ι_*) equals p_E,*.
Consequently G=(p_B,*,p_E,*)(alpha^*)^(-1). Pushing forward
[d−d_0], with p_B(d_0)=q_+ and p_E(d_0)=O_E, gives (4).
The chosen d_0 is rational and is the infinity point Z=55 in L113's
chart q=1/t; thus the Abel normalization is defined over Q everywhere.

### Exact redundancy test and its limit

L111 shows that E(Q) has neither a T-infinity point nor a T=−2
point. It also has no R=0 point: L138's coordinate X=−36300/(T−2)
maps any rational root θ of Q4 to a rational root of the irreducible
quartic H. The substitution is valid since Q4(2)=−825, and its
image is not the rational linear root X=9075, which corresponds to
T=−2 with Q4(−2)=−9. This contradicts irreducibility. Thus r≠0
for every rational P=(t,r) on E.

Given also q=(t,w)∈B(Q) with that same t, put h=3w/r. The exact
equations imply

    h²=9w²/r²=a(t),      h r/3=w.

Therefore d=(t,h,r) is a rational point of L111's smooth model and
has exactly those two projections. This includes t=2: then w=h=0,
r=±165, so both ramification points are retained. Equation (4) now
makes (3) automatic. Equivalently, starting with P alone, existence
of a rational same-T q is exactly the old square condition a(t)∈Q²,
with zero included. The signs of q recover the signs of h away from
ramification; no branch sign has been silently discarded.

For arbitrary quotient Jacobian classes, (3) remains a meaningful
abstract joint-image test, but it has not been evaluated. A rational
Jac(C) class lifting a pair need not lie on the Abel image of C;
this proof makes no converse assertion. L138–L141's supported
odd-model Kummer conditions and L118–L125's octic fake point
conditions use different targets and conventions. This proof supplies
no transport between them and no comparison of their full local or
global images with (3). The kernel modules are a concrete structural
input for a separately assessed descent; the proposed extra exclusion
after imposing the exact same-T point equations fails by the displayed
inverse lift. No full Selmer computation, stronger rank bound, point
classification, degree-nine lift or Beal integer exclusion follows.

This is a specialization of known theory under the prior gate, recorded
as REPRODUCTION, not an originality claim. The finite subset argument
and divisor identities above are the complete checks; no arithmetic
search or mathematical script is needed. A separate critical review of
this instance is recorded below.

### Separate critical instance audit — 2026-10-26

The pre-existing SPECIALIZE gate is
`drafts/literature/2026-10-26-marked-split-isogeny-kernel-audit.md`.
The audit accepts (1)–(4) and the exact same-T redundancy assertion,
with no correction to their hypotheses or conclusions. This verifies
an instance of known theory, not a new kernel theorem. The source
assessment is reused; Docking's cited Lemma 4.1 proof, Lemma 5.3 and
the complete Proposition 5.4 Case II proof were also checked directly
in the versioned PDF. L127's audited Bruin specialization supplies the
actual Prym inclusion. No source's function-evaluation algorithm is
being extended to G by this audit.

**Embedded forward kernel.** The polynomial identity ab/9=f_B and
L111's disjoint simple root sets put this cover in precisely Case II,
with quartic factor b/9 and quadratic factor a. On B the zeros of a
have order two at q_+,q_− and its poles have order two at each of the
two geometric infinities. Hence the displayed divisor of a and cover
class ε are correct. Over Qbar the even-subset model makes ε nonzero;
the particular Q-cover still uses the actual constant −3. Thus a
geometric branch calculation has not changed the rational twist.

For distinct i,j let

    d_i^±=(θ_i,±sqrt(a(θ_i)),0).

These are distinct since a(θ_i) is nonzero. Both p_B and p_E are
unramified at them. The actual divisor pullbacks, before taking classes,
are

    p_B^*(q_i−q_j)=d_i^++d_i^−−d_j^+−d_j^−
                    =p_E^*(e_i−e_j).

Here the equality on the right denotes the branch-point divisors on E,
not a claim that an individual e_i is two-torsion relative to O_E.
Indeed 2e_i is equivalent to H_E; it is not replaced by 2O_E.
This fixes each radical's index and verifies the source's branch-pair
specialization independently of its misprinted radical. Pair subsets
generate every even subset of Ω. The empty and full subsets yield
(0,0) and (ε,0). Their images therefore give all eight claimed pairs.
Their first coordinates are distinct: two subsets of Ω cannot be
complements in the full six-branch set. Conversely GF=[2] puts every
kernel pair in Jac(B)[2]×E[2], and the imported graph-kernel statement
leaves just the two ε-related preimages for each of the four E[2]
elements. This checks exhaustiveness, not just eight candidate labels.

**Reverse kernel and the action.** There is also a direct degree check
on the imported reverse-kernel statement. Since F has eight geometric
kernel points and the varieties have dimension three, FG=[2] gives
deg(G)=2^6/8=8. For u=p_B^* and n=p_B,*, L127's identities give
n u=[2] and (1−ι_*)u=0. Consequently G(alpha^*u x)=0 for every
x∈Jac(B)[2]. The image of these sixteen points has size eight,
because ker(u)={0,ε}. It is therefore the whole kernel of G.
All these counts are over Qbar; characteristic zero identifies them
with the degrees of the finite étale kernels.

To check the quotient presentation without an unproved independence
claim, write s for the parity of S⊂Ω. The branch subset S together
with q_+ when s=1 has no q_−. Its class can vanish in Jac(B)[2]
only when S is empty: the alternative full six-element subset contains
q_−. Its class can equal ε only when S=Ω: of the two representatives
{q_+,q_−} and Ω of ε, only Ω omits q_−. Thus the map from M to
Jac(B)[2]/<ε> has exactly the kernel {0,1}. Every even six-branch
subset can have q_− removed by adding {q_+,q_−}, so the map is onto.
This proves both the single relation among the z_i and its completeness.
The rational points q_± are fixed by Galois, and all radical signs in
the pullback sums disappear. Hence the embeddings carry exactly the
root-permutation actions stated in (1), not merely the abstract group
(Z/2Z)^3. On the geometric points of Res μ_2, the norm and diagonal
are respectively coordinate sum and the all-ones vector. This also
checks the two different finite étale descriptions in (2).

**Normalization on all fibers.** Under alpha, κ fixes t and negates
Y, whereas τ negates t and fixes Y. In particular κ is the actual
hyperelliptic involution. Fibers of its genus-zero quotient give
κ_*=-1 on degree-zero classes, even though the chosen origin on E is
not a branch point. Since ι=τκ, this gives 1+τ_*=1−ι_*.
For the degree-two quotient p_E, pushforward followed by pullback
counts d+τ(d); at a fixed point it counts 2d. Thus
p_E^*p_E,*=1−ι_* on every divisor class, including ramification.
Injectivity of the audited j=p_E^* gives
j^(-1)(1−ι_*)=p_E,* with no extra sign or factor of two.
The first coordinate is already n, so G has exactly the two norms
used in (4).

In the infinity chart q=1/t, Z=Y/t^4, the full formulas are

    T=2(1−3q²)/(1+3q²), h=−12q/(1+3q²),
    R=3Z/(1+3q²)².

At q=0,Z=55 they give d_0=(2,0,165), with images q_+ and O_E.
At Z=−55 they give the other rational ramification point. Thus (4)
is a Q-defined Abel normalization, not a generic affine formula
silently extended past an undefined basepoint.

**Rational exceptions and exactness.** L111's smooth infinity chart
has R/T² satisfying S²=825=25·33; at T=−2 one has R²=297=9·33.
Neither fiber has a rational point. If R=0 at a rational finite T=θ,
then θ≠2 since Q4(2)=−825. Put X=−36300/(θ−2), a nonzero rational
number. L138's exact identity
X^4 Q4(2−36300/X)=−825H(X) forces H(X)=0, contrary to its audited
degree-four irreducibility. No division by R is therefore invalid on
E(Q). For every remaining same-T pair, h=3w/r gives both equations
of D and W=hR/3. At T=2 it gives h=w=0 for both r=±165, each a
single smooth ramification point. There is no missing rational
infinity pair or discarded branch sign.

Finally, in the connecting construction a cocycle σz−z is a coboundary
exactly when some translate of z by a geometric kernel element is
rational. This proves the rational-image equivalence in (3), using G's
target, and (4) makes it automatic for the exact point pairs just
checked. It does not put an arbitrary rational lift in the Abel image.
Thus ATTEMPTS/062 remains valid with precisely its original scope.
The audit establishes no evaluated mixed condition on weaker Kummer
data, no rank improvement, and no point or integer completeness.

All new verification here is the finite divisor/module argument above;
no mathematical script, numerical point search, or replay of unrelated
arithmetic certificates was needed. The existing direct inputs in the
DAG are sufficient. L138 is essential for the rational denominator
claim; L139–L141 remain comparisons, not inputs to this proof.

## Mathlib

Full matching coverage of these Prym kernels, their finite Galois
modules and the product-target descent was not checked. No absence
or formal-verification claim is made. The kernel theorem is imported;
the explicit labels, transport and redundancy comparison are informal.
