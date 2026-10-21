# L062 — Everywhere stable one-pointed reduction over the retained F

## Hypotheses

Retain L049's unchanged elliptic curve E_0/Q, at its fixed precision
M>=max(M_tors,31), and F=Q(zeta_60,E_0[30]). Let E_F be its base
change to F, with its original origin O, and X_F=E_F minus O.
L049 supplies semistability at every finite F-place. Retain L051's
pointed models at all F-places above 3 and its interpretation of
IUT I Definition 3.1(b), printed pp.61–62, in the inspected May 2020
reproduction. Author/reproduction byte identity and agreement with
the separate 2021 journal text remain unverified.

No other Definition 3.1 condition is assumed. In particular the native
field-of-moduli inclusion and rho hypotheses are not established here.

## Conclusion

At every finite place t of the same F, the pointed curve (E_F,O)
has a stable one-pointed genus-one model over R=O_(F_t), with unchanged
pointed generic fiber. Thus X_F has stable reduction at every such
place in the qualified native sense above. No extension of F_t is
needed, including in residue characteristics 2 and 3 and at nonsplit
multiplicative places. L051's original cubic can still be used above 3.

This is a known-method specialization, not a new general reduction
theorem. The separate 2026-10-15 critical audit below validates it. It establishes
only the everywhere pointed-reduction prerequisite, not sufficient
initial data, an essential IUT flaw, or original finite B>=A.

## Proof

### Imported results and the local model

Use the pre-invocation SPECIALIZE assessment
`drafts/literature/2026-10-15-everywhere-stable-pointed-reduction.md`.
For minimal integral pointed Weierstrass models and their reduction,
import [Brian Conrad, Minimal models for elliptic curves,
21 November 2015](https://math.stanford.edu/~conrad/BSDseminar/refs/minimalmodel.pdf),
section 2, pp.2,6, and Theorem 5.5 with proof, pp.14–15, together
with [Milne, Elliptic Curves, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
II.3, pp.59–61. Conrad identifies the smooth locus of a minimal
Weierstrass model with the Neron identity open subgroup. The reduction
criteria give smooth special fiber for good reduction and geometric
nodal special fiber for multiplicative reduction. These statements use
general Weierstrass equations and apply to finite extensions of Q_p,
including p=2,3. Splitness of a multiplicative torus is not required
for its geometric fiber to be nodal. We import these results rather
than reprove the semistability/minimal-model bridge.

The family definition is [Hassett, Moduli spaces of weighted pointed
stable curves, arXiv:math/0205009v1 (1 May 2002)](https://arxiv.org/pdf/math/0205009v1),
section 2, pp.2–3, with one marking of weight one. Its conditions are
properness, flatness, connected nodal geometric fibers of fixed genus,
a smooth marking, and relative ampleness of the log dualizing sheaf.
The duality and ampleness statements below reuse the inspected Stacks
coverage in `drafts/literature/2026-10-12-native-all-place-critical-audit.md`.
These are live tags as inspected there, not a pinned Mathlib or Stacks
revision. The general results need no reproof; the application must
check their hypotheses for the actual local model.

Fix any finite place t and put K=F_t, R=O_K, with residue field k.
Here R is a complete noetherian DVR, K is a characteristic-zero local
field, and k is finite, hence perfect. By L049, E_K has good or
multiplicative reduction. Choose a minimal integral general
Weierstrass equation of the same pointed E_K. It gives

W=Proj R[X,Y,Z]/(G),  S=[0:1:0],
G=Y^2 Z+a1 XYZ+a3 YZ^2-X^3-a2 X^2 Z-a4 XZ^2-a6 Z^3,

where all a_i belong to R. The defining pointed K-isomorphism takes
S_K to the actual O, so this is not a twist or a new generic curve.
Minimality is imposed locally; the original global integer equation
is not assumed minimal at arbitrary t. At t above 3, L051 already
provides the claimed stable model on its original cubic. The following
uniform check also works on the local minimal equations at those places.

### Family and geometric fibers

W is projective and of finite presentation over R, hence proper.
The polynomial -G is monic of degree three in X over R[Y,Z].
Its homogeneous coordinate ring is therefore free over R[Y,Z] with
basis 1,X,X^2, and is R-flat. Localizing at a projective coordinate
preserves R-flatness; the degree-zero part is an R-module direct
summand. The standard affine charts are consequently R-flat, proving
flatness of W over R. Since P^2_R is integral and its defining equation
is nonzero, W is an effective Cartier hypersurface of degree three.

Its geometric generic fiber is the smooth elliptic curve E_K. The
imported minimal-model criteria and semistability make its geometric
special fiber smooth or nodal, respectively in the good or
multiplicative case. At a nonsplit multiplicative place this assertion
is geometric: the two node branches need not be k-rational. No extension
of K or R is taken to construct W or S.

For either geometric fiber over an algebraically closed field l, the
cubic hypersurface sequence on P^2_l is

0 -> O(-3) -> O -> O_(W_l) -> 0.

[Stacks, Lemma 30.8.1, tag 01XT](https://stacks.math.columbia.edu/tag/01XT)
gives H^0(O)=l, H^1(O)=H^2(O)=0, H^0(O(-3))=H^1(O(-3))=0,
and H^2(O(-3))=l. Hence h^0(O_(W_l))=h^1(O_(W_l))=1.
In particular the fibers are connected (a disconnection would give a
nontrivial idempotent in H^0) and have arithmetic genus one. The
fibers are pure one-dimensional Cartier hypersurfaces in P^2_l,
so are Cohen–Macaulay and Gorenstein. This uses arithmetic genus,
not the genus of the normalization of a nodal fiber.

### The marking and the whole-DVR hyperplane divisor

On Y=1 put x=X/Y and z=Z/Y. The equation becomes

h=z U-x^3=0,
U=1+a1 x+a3 z-a2 x^2-a4 xz-a6 z^2.

Along S, U=1 and the z-partial of h is 1. The relative hypersurface
Jacobian criterion shows that W/R is smooth along the entire section,
in every residue characteristic. Work on the neighborhood where U is
invertible. There z=x^3/U, so the section ideal (x,z) is (x).
The element x is a nonzerodivisor: in R[x,z], x is prime and does
not divide h, because h mod x is z(1+a3 z-a6 z^2), a nonzero
polynomial. If x a=h b, primality implies b=x b1, and cancellation
in R[x,z] yields a=h b1. This remains true on localization.
Thus S is an effective Cartier divisor over R, and its marking is
in the smooth locus of every fiber. There is no marking-collision
condition to check with only one marking.

Setting Z=0 in the homogeneous equation gives X^3=0. Its projective
zero scheme has coordinate ring R[X,Y]/(X^3), and is entirely in
Y!=0: every homogeneous prime contains X, and a Proj point must then
omit Y. Its chart ring is R[x]/(x^3). Hence the support is exactly
S over the whole DVR, without an extra vertical component. Near that
support z=x^3/U and x is a nonzerodivisor. The hyperplane section Z
therefore defines precisely the Cartier divisor 3S, and

O_W(3S) = O_W(1).

This is an equality of invertible sheaves up to canonical divisor
isomorphism, not merely a fiberwise degree calculation. The terms
a1 and a3 were retained throughout; no short-form argument or division
by 2 or 3 occurs.

### Relative duality and pointed stability

Let i:W -> P=P^2_R, p:P -> Spec R and f=p composed with i.
The base and schemes are noetherian, and i is a finite-presentation
Cartier immersion, hence pseudo-coherent, with normal bundle O_W(3).
The proper flat family f has one-dimensional Cohen–Macaulay geometric
fibers, with the Gorenstein property just checked. Thus all the
relative-curve and Cartier duality hypotheses used below hold;
regularity of W's total space is unnecessary.

[Stacks 0A9W, Lemma 48.15.1](https://stacks.math.columbia.edu/tag/0A9W)
gives p^!O_R=O_P(-3)[2]. The closed-immersion adjoint of
[0A9X, Lemma 48.9.7](https://stacks.math.columbia.edu/tag/0A9X)
and the Cartier formula of
[0AA4, Lemma 48.14.2](https://stacks.math.columbia.edu/tag/0AA4),
with composition as in
[0ATX, Lemma 48.16.3](https://stacks.math.columbia.edu/tag/0ATX), give

f^!O_R=i^!p^!O_R
       =(O_W(-3) tensor O_W(3))[2-1]=O_W[1].

By [0E6N, Lemma 109.19.1 and Definition 109.19.2](https://stacks.math.columbia.edu/tag/0E6N),
the relative dualizing sheaf is H^(-1)(f^!O_R), hence omega_(W/R)=O_W.
[0E6R, Lemma 109.19.3](https://stacks.math.columbia.edu/tag/0E6R)
supplies its invertibility and base-change compatibility for these
Gorenstein fibers. These are precisely the same relative formulas as
in L051, with their hypotheses now checked for general a_i.

Since O_W(1) is relatively very ample, O_W(S) is relatively ample:
its third tensor power is O_W(1), and ampleness is equivalent to
ampleness of a positive tensor power by
[Stacks 01VG, Lemma 29.38.2](https://stacks.math.columbia.edu/tag/01VG)
and its cited Lemma 28.27.2. Therefore omega_(W/R)(S) is relatively
ample. Together with the preceding family, genus, nodality and marking
checks, this verifies Hassett's weight-one stable-family definition.
The pointed generic identification identifies W_K minus S_K with the
unchanged X_K.

The place t was arbitrary, so the test passes at every finite F-place.
No gluing of these local equations into one global minimal equation is
required by the local stable-reduction predicate. Above 3, L051's
stronger split-multiplicative statement and actual model remain intact.
The proof changes neither E_0,F,K_glob=F(E_0[7]), nor the retained
embedded H,N packet, q_0, covers, markings or logs. In particular it
does not set q_0=3^30 or K_glob=N.

This discharges one prerequisite by classical methods. It does not
compute F_mod, prove native rho/field conditions, assemble all initial
data, realize the actual comparison inputs/actions or pilot, or prove
essentiality or finite B>=A. Nonsplit nodes and possibly singular total
spaces cause no failed hypothesis. A regular I_n polygon is not used
as a stable pointed fiber, and the broad descent-model obstruction of
L050/ATTEMPTS/028 is not reopened by this fixed-F-curve argument.

### Separate critical audit — 2026-10-15

**Verdict and scope.** The statement passes under the pre-invocation
SPECIALIZE assessment
`drafts/literature/2026-10-15-everywhere-stable-pointed-reduction-critical-audit.md`.
No mathematical repair or new general theorem is required. The audit
checks the application above, reusing the inspected primary statements
and proof cases in that assessment and the cited L051 assessment.
This validates a known-method prerequisite, not a result beyond those
sources or a candidate essential IUT flaw.

**All finite places and the generic identification.** For an arbitrary
finite t, L049 supplies good or multiplicative reduction of this very
E_F over F_t. Its full-torsion argument uses level 5 at residue
characteristics other than 5, and level 6 at 5; it leaves no exceptional
case at 2 or 3. A minimal integral Weierstrass equation is chosen over
R itself by the cited minimal-model theorem. Its generic isomorphism
is pointed and defined over F_t, not just over an algebraic closure.
The choice therefore introduces neither a twist nor an extension.
The good/multiplicative classification identifies the entire geometric
special fiber as smooth/nodal, respectively; a nonsplit node has two
geometric branches and does not require a model over a splitting field.
Only the two fibers of Spec R need testing. At t above 3, the separately
audited L051 model retains the actual original cubic and split node.

**Family and marking.** The monic polynomial argument is over
R[Y,Z], not over a fraction field. Its free quotient is R-flat;
localization and the graded degree-zero summand prove flatness on
each standard Proj chart. The degree-three Cartier equation remains
nonzero in each geometric fiber. Its projective hypersurface exact
sequence gives H^0=l and H^1=l, so connectedness and arithmetic
genus one hold in every residue characteristic. The hypersurface
fibers are pure dimension one and Gorenstein. These are the needed
family hypotheses, irrespective of singularities in the total space.

On Y=1 the actual equation is zU-x^3, with U|_S=1 and
(partial h/partial z)|_S=1. Thus smoothness holds along the whole
section. After inverting U, its ideal (x,z) equals (x). To verify
Cartierness without assuming a regular total space, x is prime in
R[x,z], while h mod x=z(1+a3 z-a6 z^2) is nonzero; hence
(h):x=(h). This proves that x is a nonzerodivisor in the quotient
and on the required localization. The zero scheme of Z is entirely
in this chart: Proj R[X,Y]/(X^3) has no point with Y=0.
Its support is S over Spec R, and near S the equation z=x^3/U
identifies its Cartier ideal with (x^3). Away from S, Z is a unit
in a local trivialization of O_W(1). These local checks glue to the
whole-DVR Cartier equality Z=3S, excluding any vertical contribution.
They use neither division by 2 or 3 nor rationality of node branches.

**Relative duality and ampleness.** The actual base is noetherian and
affine; P^2_R is quasi-compact and separated, and W is a proper flat
finite-presentation family. Its Cartier immersion is pseudo-coherent,
with normal bundle O_W(3). Thus the cited right adjoints apply to
O_P(-3)[2], a bounded complex of locally free sheaves. Pullback in
the Cartier formula is consequently ordinary pullback on this sheaf;
the normal twist cancels O_W(-3), and the shifts are [2][-1]=[1].
This is a computation on the whole family, so the curve dualizing
sheaf really is H^(-1)(O_W[1])=O_W. The Gorenstein fiber theorem
provides invertibility and base-change compatibility, without requiring
W regular. Finally (omega_(W/R)(S))^3=O_W(1) is relatively very
ample. The positive-power criterion gives relative ampleness of
omega_(W/R)(S), not merely positive degree on selected fibers.
All weight-one stable-family conditions are therefore satisfied.

The continuation test passes over every unchanged F_t. The direct
mathematical inputs remain L049,L051; L045,L048 are inherited through
them. No DAG change is needed. This audit retains the May 2020 native
reproduction and live Stacks version qualifications. It neither
computes F_mod nor verifies native rho or the independent initial-data
clauses; actual input/action, marked pilot transport, essentiality and
original finite B>=A remain open. ATTEMPTS/028's different descent
quantifier and regular I_n polygons supply no counterexample to this
fixed pointed model.

## Mathlib

Full matching Mathlib coverage of this all-finite-place application,
the minimal-Weierstrass/Neron bridge and the pointed-family duality
has not been checked. No absence claim is made. The general inputs
are the precise classical and Stacks results cited above; the remaining
work is their explicit application to the retained curve. No numerical
evidence or mathematical script is used. This is REPRODUCTION under
SPECIALIZE, with no claim beyond the checked literature; the separate
critical audit above validates the application with no mathematical repair.
