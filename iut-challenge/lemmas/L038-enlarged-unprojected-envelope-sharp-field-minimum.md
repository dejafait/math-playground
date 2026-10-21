# L038 — Enlarged unprojected envelope has sharp field minimum -6

## Hypotheses

Let L=Q_3(zeta_20,pi), with zeta_20 of order 20, pi^27=3,
theta=zeta_20^4, O=O_L, J=log(O^times), V=ker(Tr_(L/Q_3)),
M=J intersect V and T=(pi J/6) intersect V. Normalize v_3(3)=1
and assign v_3(0)=+infinity. Use audited L031's genuine complete
logarithm, integral field coordinates theta^a pi^r and full basis
b_(r,a). In particular J subset 3^(-2)O and

    v_3(sum_(r,a) c_(r,a) theta^a pi^r)
      = min_(r,a) (v_3(c_(r,a))+r/27).

Use exactly L033's admitted presentation and finite-word reference
subgroup Gamma. Its actual integral decomposition is

    M=F direct-sum E,
    F=Z_3 y_1, E=direct-sum_(j=3)^108 Z_3 y_j.

Set W=Q_3 y_1 and q:V->V/W. Gamma fixes F pointwise and preserves
E; on e_i=y_(2i+1), f_i=y_(2i+2), 1<=i<=53, its paired maps are

    u_i(f_i)=f_i+e_i, v_i(e_i)=e_i-f_i,

with every other basis vector fixed. Its adjacent generators are exactly
those retained in L033, with no extra shear, larger group or exponent
twist. These actions and their applicability at p=3,d=108 are imported
there from **Kaiji Kondo, Anabelian aspects of the outer automorphism
groups of the absolute Galois groups of mixed-characteristic local
fields**, **arXiv:2512.09231v2**, 12 December 2025, **section 1,
Theorem 1.3 and complete even-degree proof**, printed pp. 9–11
([versioned primary text](https://arxiv.org/html/2512.09231v2#S1)).
No presentation generator is assigned a chosen field coordinate.

Use audited L034's complete trace functional in those field coordinates:

    Tr(x)=27 tau(x), tau=(4,-1,-1,-1,0,...,0).

Use audited L036's full input bound and ordinary projected span:

    T subset 3^(-4)M,
    sum_(h in Gamma) Z_3 h(q(T))=3^(-4)q(M).

These are statements about the full genuine lattices and ordinary finite
sums of finite-word images. Their audited certificates and infinite-tail
proofs are reused, rather than recomputed or inferred from previews.
L037's projected dilation result is compatible context, not a direct
input to this proof. L028 is a different-field method comparison only.

For the integral splitting reuse the known idempotent-module theorem
**LinearMap.IsIdempotentElem.isCompl**, Mathlib **Projection.lean**,
commit **e6bbacd0e1b7307ff6e17da09cd2455f60804fa6**
([pinned primary source](https://github.com/leanprover-community/mathlib4/blob/e6bbacd0e1b7307ff6e17da09cd2455f60804fa6/Mathlib/LinearAlgebra/Projection.lean)).
It requires an idempotent linear endomorphism of the module being split;
preservation of the ordinary orbit module is checked below over Z_3.
The general splitting theorem is imported, not reproved. The explicit
word and field-layer computations are necessary local specializations.

## Conclusion

For every admitted presentation in these hypotheses,

    min_(h in Gamma, t in T minus {0}) v_3(h(t)) = -6.

This minimum is attained by an actual finite word h and an actual point
t in T. The word and point may depend on the presentation; no explicit
attaining pair is identified. The smallest centered closed field
valuation disc containing Gamma(T) is pi^(-162)O, of radius 3^6=729.
This is a hull statement, not equality of the orbit with that disc.

More precisely, let p_+,p_- be the actual integral projections of M
onto F,E, respectively, extended Q_3-linearly to V. The ordinary
unprojected orbit module satisfies

    S=sum_(h in Gamma) Z_3 h(T)
      =p_+(T) direct-sum 3^(-4)E.

The embedded decomposition and p_+(T) retain their presentation
dependence, whereas the field minimum and hull above are uniform.
The fixed contribution satisfies p_+(T) subset 3^(-4)F and has
minimum at least -6; the complementary contribution has minimum
exactly -6. There is no field valuation on V/W in this argument.

This is a **REPRODUCTION** of the assessed known methods with a
local specialization, validated by the separate critical audit below. It closes
the auxiliary unprojected minimum target, not the IUT challenge.
Actual/native input and action, packet/global realization, pilot
transport, essentiality and the original finite B>=A remain unresolved.
No original-IUT radius prescription is asserted for this enlarged input.

## Proof

### An actual finite word splits the ordinary orbit module

On each ordered pair (e_i,f_i), the displayed maps have matrices

    U=[[1,1],[0,1]], R=[[1,0],[-1,1]],
    UR=[[0,1],[-1,1]], (UR)^2=[[-1,1],[-1,0]],
    (UR)^3=[[-1,0],[0,-1]].

Composition u_i v_i applies v_i first. Each map is identity on all
other pairs and on F. The 53 disjoint supports therefore show that
the finite word, with factors taken in increasing order,

    s=product_(i=1)^53 (u_i v_i)^3 in Gamma

is identity on F and minus identity on E. This uses precisely the
source generators, without a group-image or closure assertion.
Set p_+=(id+s)/2 and p_-=(id-s)/2. Since 2 is a unit of Z_3,
these are integral endomorphisms of M. Their actions on F,E verify
that they are complementary idempotents, with images F,E. Thus
they are the actual integral projections specified in the conclusion.

Define S by ordinary finite Z_3-sums. Every word preserves M, and
T subset M/81, so every image and finite sum lies in M/81. The
module S contains T. Left multiplication by s permutes the finite
words, including inverses, so s(S)=S. Because 1/2 is integral,
p_+ and p_- are endomorphisms of S. Applying the cited integral
idempotent splitting yields S=p_+(S) direct-sum p_-(S). There is
no average over an infinite group and no closure added to S.

Each generator fixes F and preserves E, hence every word h satisfies
p_+ h=p_+ and p_- h=h p_-. Applying p_+ to a finite expression
in orbit images therefore gives p_+(S)=p_+(T): the projected sum
of the coefficients times its T-points is the projection of a point
of T, since T is a Z_3-module; the identity word gives the reverse
inclusion. Also p_+(T) subset F/81 by the full input bound.

The restriction q:E_Q->V/W is a rational isomorphism and identifies
E with q(M), where E_Q=Q_3 E. Since q p_-=q on V, it maps
p_-(S) onto q(S). By audited L036, q(S)=q(M)/81=q(E/81).
Both p_-(S) and E/81 lie inside E_Q. Injectivity of this same q
there gives the embedded equality p_-(S)=E/81, not merely an
abstract module isomorphism. This proves the asserted formula for S.
No norm or valuation is transported across q.

### Complete lowest field-valuation layer of M

Every x in M lies in J subset O/9 by audited L031. Define

    rho:M -> O/pi O=F_81, rho(x)=9x modulo pi O.

This is an additive Z_3-linear map, with target regarded as an F_3
space; it kills 3M, since 9(3M) subset 3O subset pi O. In the
complete field coordinates it is precisely the first four coordinates
of 9x reduced modulo 3, expressed in the residue basis
1,bar(theta),bar(theta)^2,bar(theta)^3. All terms with r>=1 vanish
modulo pi, while reduction of O_U modulo pi is reduction modulo 3.
Thus rho(x)!=0 exactly when v_3(x)=-2; rho(x)=0 implies
v_3(x)>-2 (including x=0). This uses the actual field valuation.

Trace zero says tau(x)=0 exactly, so tau(9x)=0. Therefore the image
of rho is contained in the three-dimensional F_3-kernel of the
nonzero row (4,-1,-1,-1) modulo 3. This is a necessary condition
on every element of the full M, not only the witnesses below.

To prove the reverse dimension bound, take the actual complete-basis
columns b_a=b_(9,a), a=0,1,2,3, from L031. Their four constant
coordinate columns after multiplying by nine are exactly

    d_0=(4,0,0,0), d_1=(24,24,24,25),
    d_2=(0,1,0,3), d_3=(26,26,2,26).

The full trace depends only on these constant coordinates. Applying
tau gives respectively 16,23,-4,50, so Tr(b_a) is respectively
48,69,-12,150. The following three complete field elements belong
to J and have trace zero:

    x_1=b_1-(23/16)b_0,
    x_2=b_2+(1/4)b_0,
    x_3=b_3-(25/8)b_0.

Indeed all coefficients are in Z_3 and the displayed trace values
cancel exactly. Hence x_1,x_2,x_3 belong to the full M. Reducing
their complete constant coordinates gives

    rho(x_1)=(1,0,0,1),
    rho(x_2)=(1,1,0,0),
    rho(x_3)=(0,2,2,2).

These three vectors lie in the indicated trace-row kernel and are
linearly independent over F_3: the theta^2 coordinate first forces
the third coefficient to vanish, the theta coordinate then forces
the second, and the theta^3 coordinate forces the first. Consequently
dim_F_3 rho(M)=3, and min v_3(M minus {0})=-2. The upper and
lower layer bounds are both established. The full coordinate bound
from L031 accounts for all higher r and all infinite logarithm tails;
the displayed bottom-layer witnesses are elements of its proved full
basis, not truncations claimed to be actual logarithms without a tail.

### The actual complement retains the layer for every presentation

The admitted decomposition M=F direct-sum E gives
rho(M)=rho(F)+rho(E). Since F is rank one over Z_3 and rho kills
3F, dim_F_3 rho(F)<=1. The preceding complete-layer result therefore
forces dim_F_3 rho(E)>=2. In particular there is an actual element
e in E with rho(e)!=0, hence v_3(e)=-2. Conversely E subset M
gives v_3(e')>=-2 for every e' in E. Thus the minimum of E is
exactly -2 for every admitted actual complement, independently of
where the y_j lie in field coordinates. No converse realization of
arbitrary complements or lines is needed.

Rational scaling by 1/81 changes valuations by -4, so E/81 has
minimum -6, attained by e/81. The fixed component p_+(T) lies in
F/81 subset M/81; every element there has valuation at least -6.
The full sum S also lies in M/81, giving the same lower bound on
every element. As E/81 subset S contains the exhibited minimum,
the minimum of S minus {0} is exactly -6. In particular the fixed
component cannot make the uniform bound worse or remove its attainment.

For completeness, the fixed component is a full rank-one lattice in
W, since T is full in V by audited L036 and p_+ is surjective onto
W. Write p_+(T)=3^a F for its actual presentation-dependent integer
a; the containment in F/81 gives a>=-4. This notation imposes no
restriction on the presentation, does not compute a, and is unnecessary
for the sharp uniform minimum. The complementary computation, rather
than an assumed numerical normalization of y_1, determines the answer.

### Return from an ordinary finite sum to an actual finite-word image

Choose e in E as above. The embedded equality E/81=p_-(S) subset S
means that e/81 has an ordinary finite expression

    e/81=sum_(j=1)^n c_j h_j(t_j),
    c_j in Z_3, h_j in Gamma, t_j in T.

Each h_j is a finite word by definition; no limiting group element
is used. Every nonzero h_j(t_j) has valuation at least -6 because
h_j(T) subset M/81. If all nonzero terms h_j(t_j) had valuation
strictly greater than -6, so would every c_j h_j(t_j): integral
coefficients can only raise valuations. The ultrametric inequality
for this finite sum would then give v_3(e/81)>-6, a contradiction.
Thus at least one actual h_j(t_j) has valuation exactly -6. Its
t_j is nonzero because the image is nonzero and h_j is invertible.
This proves actual finite-word attainment, without identifying the
orbit set with its ordinary span or using a closure approximation.

Every orbit point therefore lies in the closed ball v_3>=-6, and an
orbit point lies on its boundary. Since pi^27=3, that ball is
pi^(-162)O and its radius is 729. No smaller centered field valuation
disc contains the orbit. The existence argument is uniform over
presentations although its chosen e, finite expression and attaining
word need not be uniform.

### Relevance, qualifications and remaining gaps

The approved continuation test succeeds: exact finite-source-word
splitting and the complete embedded valuation layer give an attained
sharp full-space minimum. This resolves the local fixed-line limitation
left by L036–L037 for this auxiliary input; it does not transfer the
different-field constants of L028. The sources cover the general
action, integral projection and lattice methods; the local layer and
minimum are the needed specialization, with no novelty claim.

Preserve ATTEMPTS/020,022–024. Whole-kernel residual irreducibility is
still false; only the already audited quotient span is used. No
O_U-module structure on J, prescribed reciprocal coordinates, quotient
field valuation, extra action or set-orbit equality is assumed. An
auxiliary shell envelope is not an actual ind3 input merely because
it is an enclosing region. The radius 729 is not asserted to violate
any original-IUT enclosure. Actual/native input and action,
packet/global realization, pilot transport, essentiality and original
finite B>=A remain open. This is an audited local result,
not an UNVERIFIED CANDIDATE solution of the challenge.

### Separate critical audit, 2026-10-10

The independent audit validates the statement with unchanged hypotheses,
conclusion and argument. It reuses the approved source comparison and
audited L031, L033, L034 and L036. It introduces no new theorem input,
DAG edge, action or presentation constraint. The finite checks are
reproducible by

    python3 scripts/cyclotomic-log/audit_unprojected_minimum.py

The script imports no builder code. Its full evidence is in
`scripts/cyclotomic-log/unprojected-minimum-independent-audit.json`;
124 checks pass with zero failures. It pins the complete L031 input
to SHA256 `ad5ea1741a5cc54d5413ab679fd4fba387e8a2aafc8d9c7c2b6d31e799159102`
and records the L034 input hash. Analytic image completeness and infinite
tails remain L031's audited inputs, not claims established by this script.

For the word, applying v_i then u_i three times on each pair gives
minus identity on that pair. The check applies all 318 individual maps
to each of the 107 basis vectors of M, including the fixed y_1, and
saves every complete image. Distinct pairs have disjoint supports, so
the order of their six-map blocks does not affect the result. L033's
adjacent maps also preserve E and fix F, as do their inverses. Thus
the whole specified finite-word group, not just the constructed word,
has both properties required for p_+h=p_+ and p_-h=hp_-.

The integral module check does not merely appeal to 2 being a unit.
First T is a Z_3-module contained in M/81, by L036, and every word
preserves M/81. Its ordinary finite-sum orbit module S is therefore a
bounded Z_3-submodule. Left multiplication by s permutes the finite
words, so both (id+s)/2 and (id-s)/2 actually preserve S. This verifies
the endomorphism hypothesis of the cited idempotent theorem. Projection
onto F is exactly p_+(T), since a finite integral combination of T-points
is another T-point. Projection onto E has quotient image q(M)/81 by
L036. Both this projected module and E/81 are in E_Q, where the same
q is injective. Their equality follows there; there is no substitution
of an abstractly isomorphic lattice or valuation on V/W. No topological
closure or additional compact-group action enters this argument.

For the field layer, the audit reads every entry of B_int and of
L034's full M basis and kernel transform. It checks all entries of
(9M_0)=B_int A_(columns 1,...,107) and the entire zero trace row.
L034's previously audited invertible integral transform supplies
completeness of this M basis. The finite audit computes the valuation
of every one of the 108 J basis columns and 107 M basis columns;
the minimum in both cases is -2. In particular no unexamined higher
pi coordinate can lower the bound. The first four rows of 9M_0,
reduced over F_3, have rank exactly three; the complete matrix and
its row reduction are saved, rather than inferred from a preview.

Independently of that matrix-rank check, all four full b_(9,a) columns
are extracted and the three displayed rational combinations are formed
in all 108 coordinates. Their coefficients are 3-integral, their exact
traces vanish, their field valuations are -2, and their residual vectors
are exactly (1,0,0,1), (1,1,0,0), (0,2,2,2). The rank-three check uses
the complete residual vectors. The upper rank bound applies to all M:
9M lies in O, higher pi powers vanish modulo pi, and the constant
coefficients obey the nonzero trace row (4,-1,-1,-1) modulo 3.
Since O_U/(pi O intersect O_U)=O_U/3O_U, these four coordinates are
the full residue field F_81. Thus rho(M) has dimension exactly three.
These are genuine elements of the complete logarithm lattice, using
L031's two span containments and infinite-tail argument as audited inputs.

For every admitted presentation, rho kills 3M and the actual F has
rank one. Hence rho(F) has dimension at most one. The equality
M=F direct-sum E implies dim rho(E)>=3-1=2, without requiring the
residual images to form a direct sum. This point prevents a hidden
assumption about the field coordinates of the complement. It gives an
actual e in E of valuation -2, while E subset M gives the matching
lower bound. Rational scaling yields e/81 in S of valuation -6,
and S subset M/81 bounds every element below by -6.

Finally e/81 is in the ordinary sum S, so it has a finite expression
in integral multiples of actual finite-word images of actual T-points.
If every nonzero image in this expression had valuation greater than
-6, the minimum of their finitely many valuations would be greater
than -6. Integral coefficients cannot lower it, and the ultrametric
inequality would contradict v_3(e/81)=-6. At least one image therefore
attains -6. This proves existential attainment for each presentation;
no effective bound on word length or explicit attaining pair is claimed.
The centered disc is consequently pi^(-162)O with radius 729, with
no assertion that every point of that disc is in the orbit.

The audit supplies independent verification of this local known-method
specialization, not a new mathematical conclusion beyond L038. It leaves
ATTEMPTS/020,022–024 intact. In particular input membership in actual
ind3 images, native action identification, packet/global realization,
pilot transport, essentiality and original finite B>=A remain unresolved.

## Mathlib

Supporting integral idempotent splitting is present:
**LinearMap.IsIdempotentElem.isCompl**, with supporting
**LinearMap.IsProj.isCompl**, in the pinned Projection.lean source
above, inspected in the reused assessment. Its module-preservation
hypothesis is checked here explicitly. Full matching enlarged-field
unprojected-minimum theorem and supporting exact logarithm/action/
field-filtration coverage: **not checked**. Unknown availability is
not evidence of absence. No formal verification is claimed.
