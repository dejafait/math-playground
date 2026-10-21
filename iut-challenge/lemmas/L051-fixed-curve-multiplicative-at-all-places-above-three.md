# L051 — Fixed pointed curve at every F-place above 3

## Hypotheses

Use the same curve chosen in L048, with original equation
E_0: y^2=x^3+c x^2+d x+e and origin [0:1:0], where c,d,e are
integers. Retain its fixed precision M>=max(M_tors,31), its
algebraic closure Omega, and the fields and places in L045:

F=Q(zeta_60,E_0[30]), F_u=H=Q_3(zeta_60),
D=F(E_0[7]), D_w=N=Q_3(zeta_420,3^(1/7)).

In particular F/Q is finite Galois. Put E_F=E_0 over F and
X_F=E_F minus its origin. L048 supplies c=1 and d=e=0 modulo 3,
v_3(Delta)=30, unit c4, and a pointed Q_3-isomorphism
E_0 over Q_3 ≅ E_(q_0), where q_0 belongs to Q_3 and
v_3(q_0)=30 with v_3(3)=1. Do not assume q_0=3^30.

Interpret the native reduction predicate using the inspected May 2020
IUT I Definition 3.1(b), printed pp.61–62, and its pointed-curve
conventions, with the reproduction qualification recorded in
`drafts/literature/2026-10-12-native-selected-place-model-comparison.md`.
This result does not assume the other hypotheses of Definition 3.1
or assert that 3 belongs to a completed selected-place set.

## Conclusion

For every finite place t of F above 3, the fixed E_F has split
multiplicative reduction over F_t. The original projective cubic
over O_(F_t), together with its infinity section, is a stable
one-pointed genus-one family: it is flat and proper, its geometric
fibers are connected and nodal (the generic fiber is smooth), its
marking is smooth, and its relative dualizing sheaf plus the marking
is relatively ample. Its special fiber is an irreducible split nodal
cubic, not the regular I_n polygon.

Consequently the fixed X_F passes the multiplicative-reduction test
at every F-place above 3 in that version of Definition 3.1(b), if
this moduli place is selected. This is one prerequisite only. It is
a specialization of known results, with no claim of mathematics beyond
the checked sources or an essential IUT flaw. The separate 2026-10-12
critical audit below validates this statement with explicit relative
duality citations and Cartier checks over the whole DVR.

## Proof

### Known inputs and the bounded application

Reuse the unchanged pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-12-native-all-places-above-three.md`.
[Milne, Algebraic Number Theory v3.08 (19 July 2020)](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorem 3.34 and its Galois proof, printed pp.59–60, supplies
transitivity on primes above 3. Section 8 and Propositions 8.1–8.2,
pp.135–136, give the finite-separable completion interpretation.
[Kedlaya, Introduction: the Tate curve (fall 2004)](https://kskedlaya.org/18.727/tate-curve.pdf),
Theorems 1–2, pp.3–4 (with Theorem 2 referring to Silverman V.5.3),
give the Tate curve and split-multiplicative criterion over a finite
extension of Q_p. L048 already applies this theorem over Q_3;
neither it nor Galois transitivity is reproved here.
[Hassett, Moduli spaces of weighted pointed stable curves,
arXiv:math/0205009v1 (1 May 2002)](https://arxiv.org/pdf/math/0205009v1),
section 2, pp.2–3, gives the stable-family definition; weight one
recovers ordinary pointed stability. We check that definition on
the actual cubic instead of invoking existence after a field extension.
For relative adjunction, import the precise Stacks statements listed
in the duality calculation below, using the primary source coverage in
`drafts/literature/2026-10-12-native-all-place-critical-audit.md`.
They apply to a Cartier divisor without assuming that divisor smooth.
These are live tag versions inspected on 2026-10-12, not a pinned
repository revision. General duality is imported, not reproved.

The main unresolved claim remains original finite B>=A. This test
could remove a native reduction obstacle to using the retained
arithmetic packet. Continue on a pass at every actual F-completion;
abandon this particular prerequisite application only on a failure
for fixed X_F there. Neither an additive Q_3-descent nor an unstable
regular polygon is that discriminating test. No independent
initial-data or comparison bridge is assumed in this proof.

### All completions and the fixed pointed curve

Let t be any F-place above 3. By L045 and the cited transitivity
theorem, choose sigma in Gal(F/Q) with sigma(u)=t. Here this
means that the absolute value at t applied to sigma(a) equals the
absolute value at u applied to a, for a in F, both extending
|3|_3=1/3. Thus sigma extends by continuity to a valued-field
isomorphism F_u -> F_t. Its inverse is the extension of sigma^(-1),
so this is an isomorphism, not merely an embedding. Since sigma
fixes Q and Q is dense in Q_3, the extension fixes Q_3. It maps
valuation rings isomorphically. In particular F_t is abstractly
Q_3-isomorphic to H, without identifying distinct completions as
embedded subfields of Omega.

All coefficients of E_0 and the coordinates of its origin are
Q-defined. This transport therefore preserves the very equation
and its pointed origin, rather than replacing E_F by a conjugate
F-defined curve. Equivalently each E_(F_t) is the base change of
the same E_0 over Q_3. L048's pointed Tate isomorphism base changes
to E_(F_t) ≅ E_(q_0) over F_t. Its parameter still has absolute
v_3(q_0)=30, hence |q_0|_3<1. The cited Tate criterion over the
finite extension F_t/Q_3 proves split multiplicative reduction.
This already handles every t; the following direct model checks
verify the pointed compactification as well.

### The projective family, flatness and its geometric fibers

Write R=O_(F_t), with residue field k of characteristic 3. Consider

C=Proj R[X,Y,Z]/(Y^2 Z-X^3-c X^2 Z-d X Z^2-e Z^3),
S=[0:1:0].

The rational integer coefficients belong to R. Their reductions
are still c=1 and d=e=0, since the map Z_3 -> R maps 3 into
the maximal ideal. Properness follows from projectivity.
For flatness, multiply the relation by -1 to make it monic of
degree three in X. Its graded coordinate algebra is a free
R[Y,Z]-module with basis 1,X,X^2, so is R-flat. On each
standard projective chart, the localized graded algebra is R-flat
and its degree-zero part is an R-module direct summand. Thus each
chart is R-flat and C -> Spec R is flat. The equation also
defines an effective Cartier hypersurface in P^2_R.

The geometric generic fiber is L048's nonsingular plane cubic.
It is connected of genus one and carries S as its origin. The
geometric special fiber has affine equation

y^2=x^3+x^2=x^2(x+1).

Over an algebraic closure of k this equation is irreducible:
a factorization of the monic quadratic in y would require
x^2(x+1) to be a square in k-bar(x), but its valuation at x=-1
is one. This excludes a square. Its projective homogenization
has no extra component at infinity, since it is not divisible
by Z. Thus the geometric special fiber is integral, hence
connected. The affine partial derivatives are x and 2y, so
its only singular point is (0,0). Its quadratic tangent cone
is (y-x)(y+x), with distinct k-rational lines. It is an ordinary
split node. The only point at infinity is [0:1:0]; the
Z-partial of the homogeneous equation there is 1, so that
point is smooth. There are no further geometric singularities.

Both fibers have arithmetic genus one. For any geometric residue
field K, use the hypersurface sequence
0 -> O_(-3) -> O -> O_C -> 0 on P^2_K and
[Stacks, Lemma 30.8.1, tag 01XT](https://stacks.math.columbia.edu/tag/01XT).
It gives H^0(O)=K, H^1(O)=H^2(O)=0,
H^0(O_(-3))=H^1(O_(-3))=0 and H^2(O_(-3))=K.
The long exact sequence therefore gives h^0(O_C)=h^1(O_C)=1.
This applies also to the singular special fiber; arithmetic genus
is not its normalization's genus. Both geometric fibers are
equidimensional curves and are Cohen–Macaulay and Gorenstein:
locally they are nonzero Cartier hypersurfaces in a smooth surface.

### Smooth marking and relative ampleness

On Y=1 set x=X/Y and z=Z/Y. The equation at S is

z(1-c x^2-d x z-e z^2)=x^3.

The factor in parentheses is a unit along S, and the derivative
of the equation with respect to z is 1 there, over R itself.
Thus C is relatively smooth along S. On this neighborhood the
ideal of S, initially (x,z), equals (x). To check regularity of
this local equation over R, put h=z(1-c x^2-d x z-e z^2)-x^3
in R[x,z]. The prime x does not divide h, since h modulo x is
z(1-e z^2), a nonzero polynomial in the domain R[z]. If
x a=h b, primality forces b=x b_1 and cancellation gives a=h b_1.
Thus x is a nonzerodivisor modulo h, also after localizing at the
factor in parentheses. It follows that S is an effective Cartier
divisor over the entire DVR. The marking lies in the smooth locus of each
fiber. There is just one weight-one marking, so the collision
condition in Hassett's definition is automatic.

Let i:C -> P=P^2_R and p:P -> Spec R, with f=p composed with i.
Here R is a noetherian DVR, P is noetherian, quasi-compact and
quasi-separated, and i is a finite-presentation Cartier immersion
with normal sheaf O_C(3). In particular i is pseudo-coherent.
Both morphisms are proper and of finite type. The already proved
flatness and one-dimensional Cohen–Macaulay geometric fibers make
f a curve family to which relative dualizing-sheaf theory applies.

[Stacks, Lemma 48.15.1, tag 0A9W](https://stacks.math.columbia.edu/tag/0A9W)
for the trivial rank-three bundle over Spec R gives
p^!O_R=O_P(-3)[2].
[Lemma 48.9.7, tag 0A9X](https://stacks.math.columbia.edu/tag/0A9X)
identifies the closed-immersion right adjoint with derived sheaf Hom;
[Lemma 48.14.2, tag 0AA4](https://stacks.math.columbia.edu/tag/0AA4)
gives i^!K=Li^*K tensor^L O_C(3)[-1] for this Cartier immersion.
Composition of the proper right adjoints, as in
[Lemma 48.16.3, tag 0ATX](https://stacks.math.columbia.edu/tag/0ATX),
therefore gives

f^!O_R=i^!p^!O_R
       =(O_C(-3) tensor O_C(3))[2-1]=O_C[1].

By [Stacks, section 109.19, Lemma 109.19.1 and Definition 109.19.2,
tag 0E6N](https://stacks.math.columbia.edu/tag/0E6N), the relative
dualizing sheaf is H^(-1)(f^!O_R). Thus omega_(C/R)=O_C;
[Lemma 109.19.3, tag 0E6R](https://stacks.math.columbia.edu/tag/0E6R)
also supplies invertibility and base-change compatibility from the
Gorenstein fibers. The degree is essential: the two-term resolution
O_P(-3) -> O_P computes ambient sheaf Ext^1(i_*O_C,O_P(-3))
as i_*O_C, while the relative curve complex has its sheaf in degree
-1 because of the ambient shift [2]. No smoothness or regularity
of C's total space is used.

The section Z of O_C(1) cuts out exactly 3S. Indeed its zero
scheme has projective coordinate ring R[X,Y]/(X^3), which
is entirely in the chart Y!=0: every homogeneous prime contains
the nilpotent X and must omit Y to represent a Proj point. Its
chart ring is R[x]/(x^3), over the whole base, so there is no
extra vertical zero component. On the
displayed neighborhood of S, z=x^3 times a unit, so its
Cartier divisor is three times the divisor of x. There are no
other zeros, and it is not identically zero on any fiber
component. Consequently

O_C(3S) ≅ O_C(1).

The latter sheaf is relatively very ample for the projective
cubic embedding. Therefore O_C(S) is relatively ample, since
its third tensor power is relatively very ample, by
[Stacks, Lemma 29.38.2, tag 01VG](https://stacks.math.columbia.edu/tag/01VG)
(using Lemma 28.27.2, tag 01PT). With the
dualizing computation this is exactly relative ampleness of
omega_(C/R)(S). Flatness, properness, connected nodal genus-one
geometric fibers and the smooth marking proved above now verify
all weight-one stable-family conditions in the cited definition.
The generic complement C_(F_t) minus S is the unchanged X_(F_t).

### Verdict and limitations

The test passes for every t above 3, and no extension, curve
reselection or twist was used. The stable special fiber is the
irreducible nodal cubic. A regular minimal model can have an
I_n polygon, whose unmarked components need not be stable; this
proof neither equates those models nor uses regularity as a
stability criterion. The Tate conclusion and pointed model checks
concern the same fixed curve over the actual F_t.

Thus, conditional on selecting this moduli place, the particular
multiplicative-reduction clause of the inspected May 2020 native
definition is satisfied at all its F-lifts. This does not verify
the remaining Definition 3.1 data: K-coricity, covering and cusp
choices, the full selected-place set or other requirements.
No tautological log-curve identification or covering construction
beyond this pointed reduction test is asserted. Actual inputs
and actions, pilot transport, essentiality and finite B>=A remain
unresolved. L049 is unnecessary to this stronger reduction test
at 3; L050 and ATTEMPTS/028 remain conditional exposition results
and do not contradict it. ATTEMPTS/022,025,026,027 are preserved.

### Separate critical audit — 2026-10-12

**Verdict.** The unchanged statement passes the pre-invocation
SPECIALIZE audit assessment. The additions above supply the previously
implicit nonzerodivisor check for the marking and the precise relative
duality application and shifts. They repair justification, without
changing the curve, field, theorem statement or direct inputs L045,L048.
No general reduction or duality theorem has been reproved.

**Quantifiers and model hypotheses.** L045's finite Galois F/Q gives
place transport for each actual t, with inverse transport and equality
on the dense Q inside Q_3. L048's equation and infinity point are
Q-defined, so transport preserves both, and its pointed Tate
isomorphism base changes to each F_t. The absolute parameter valuation
is 30 there; it is not a uniformizer valuation or the assertion
q_0=3^30. The field F_t is a finite extension of Q_3, as required
by the imported Tate theorem. No equality of distinct embedded
completions inside Omega is asserted or needed.

The monic homogeneous equation gives a free R[Y,Z]-module before
chart localization. Localization is R-flat and the degree-zero
summand remains flat, proving flatness on all projective charts.
The nonzero equation on the integral ambient P^2_R is Cartier.
The generic fiber is nonsingular by L048; the special fiber has
exactly the one affine singularity and the smooth infinity point
checked above. Its quadratic-in-y irreducibility test works over
the algebraic closure, since x+1 has odd order at x=-1 even in
characteristic 3. The two rational tangents are distinct there.
Thus all geometric fibers, not just rational points of the special
fiber, meet the nodality, connectedness and dimension requirements.
Their arithmetic genus is established by the full cohomology sequence.

The marking's derivative test and nonzerodivisor argument hold over
R. Near its support, z=x^3 times a unit proves equality of effective
Cartier divisors Z=3S, not merely equality of fiberwise supports.
The full zero scheme Spec R[x]/(x^3) excludes an additional vertical
part. The projective-space duality shift [2] followed by the Cartier
shift [-1] gives [1]; taking H^(-1) yields exactly the relative
curve sheaf. All properness, noetherian, flatness, Cartier and fiber
hypotheses have been checked before this application. The third-power
ampleness criterion then verifies Hassett's actual relative ampleness
condition for omega_(C/R)(S), with one smooth weight-one marking.

This completes the audit of the single native reduction prerequisite
above 3 under the qualified May 2020 source interpretation. It gives
no full selected-place set, K-core, covering/cusp data, log-curve
identification, permitted inputs/actions, pilot transport, essentiality
or finite B>=A. The total space may be singular; regular I_n polygons
and additive Q_3-descents supply no failed hypothesis of this model.
L049 is background and L050 contrast only, so no DAG edge is added.
This is verified local reuse of known methods, not a result beyond
the assessed sources or a candidate essential IUT flaw.

## Mathlib

Full matching coverage of this all-completion and pointed stable-model
specialization has not been checked in Mathlib. No absence claim is
made. The proof imports the cited Galois/completion and Tate results,
the stable-family definition, and standard plane-hypersurface genus
and adjunction formulas; its explicit checks specialize them to the
already chosen cubic. No mathematical script or numerical evidence
is needed, and no novelty beyond the checked sources is claimed.
