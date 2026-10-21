# L082 — Stable one-pointed reduction over the exact auxiliary Legendre field

## Hypotheses

Retain exactly L078's choices D,s,t,iota, auxiliary pointed curve

    E_L: V^2=X(X-1)(X-t), O=[0:1:0],
    G=Q(t)(iota,E_L[15]), M=G(E_L[7]),

and its embedding and induced places. Division fields include both
coordinates of every geometric torsion point. L078 establishes that
G is a number field, t!=0,1, and the embedded completions are
G_(u_G)=H and M_(w_M)=N. L081 establishes semistability of this
same E_L at every finite G-place. No normality of G/Q or additional
initial-data condition is assumed.

## Conclusion

For every finite place v of this unchanged G, the pointed curve
(E_L,O) has a stable one-pointed genus-one model over R=O_(G_v),
with a pointed generic-fiber isomorphism to (E_L,O) over G_v itself.
No extension of G or G_v is needed, including at residue
characteristics 2,3 and at nonsplit multiplicative places.

L078's field prescription, embedding and H,N completion equalities
are unchanged. This is a reproduction/specialization of known
methods, validated by the separate step325 critical audit below. It closes only the
pointed-reduction prerequisite; it supplies neither sufficient native
initial data nor an essential IUT flaw or the original finite B>=A.

## Proof

### Imported results and scope

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-18-exact-legendre-stable-pointed-reduction.md`.
The general inputs are Brian Conrad, *Minimal models for elliptic
curves*, 21 November 2015, [section 2 pp.2,6 and Theorem 5.5 with
proof and discussion pp.14–16](https://math.stanford.edu/~conrad/BSDseminar/refs/minimalmodel.pdf),
and J. S. Milne, *Elliptic Curves*, second edition (2021),
[II.3 pp.59–61](https://www.jmilne.org/math/Books/EC2.pdf).
They supply minimal integral general Weierstrass equations over a
DVR for the same pointed generic curve. Their reduction criteria
identify the geometric special cubic as smooth for good reduction
and nodal for multiplicative reduction, including nonsplit reduction
and residue characteristics 2,3. Equivalently, Conrad's theorem
identifies the smooth locus with the Neron identity open subgroup;
the geometric node/cusp distinction is part of the cited discussion.
These general theorems are imported, not reproved here.

Use the stable-family definition in Brendan Hassett, *Moduli spaces
of weighted pointed stable curves*, [arXiv:math/0205009v1,
1 May 2002, section 2 pp.2–3](https://arxiv.org/pdf/math/0205009v1),
with one marking of weight one. It requires a proper flat family
with connected nodal geometric fibers of fixed genus, a smooth
marking, and relative ampleness of the log dualizing sheaf. Smooth
fibers are allowed. The precise relative duality, cohomology and
ampleness inputs are cited below; their inspected hypotheses and
essential proof cases are recorded in the approved assessment and
its reused `2026-10-12-native-all-place-critical-audit.md` source
assessment. Stacks references retain the live-version qualification
of those records, not a pinned revision claim.

L062 supplies audited method context for a different curve and field.
Its curve-specific conclusion or models are not mathematical inputs
here. The required specialization is the following actual-family
verification for every completion of the present G.

### The actual local family and fibers

Fix any finite G-place v. Put K=G_v, R=O_K, with residue field k.
R is a complete noetherian DVR with fraction field of characteristic
zero and finite, hence perfect, residue field. By L081 the elliptic
curve E_L/K has good or multiplicative reduction. Choose a minimal
integral general Weierstrass equation for this same pointed curve.
Write its projective model and origin as

    W=Proj R[A,B,C]/(F), S=[0:1:0],
    F=B^2 C+a1 ABC+a3 BC^2-A^3-a2 A^2 C-a4 AC^2-a6 C^3,

where every a_i lies in R. The pointed K-isomorphism from W_K
to E_L/K carries S_K to O. It is defined over K itself, so neither
a twist nor a field extension has been introduced. The literal
global Legendre equation is not presumed integral or minimal at v.

W is projective of finite presentation over R and hence proper.
The polynomial -F is monic of degree three in A over R[B,C].
Thus its homogeneous coordinate ring is free over R[B,C], with
basis 1,A,A^2, and in particular R-flat. Localizing at each standard
projective coordinate preserves R-flatness; the graded degree-zero
part is an R-module direct summand of that localization. The three
standard affine charts are therefore R-flat, proving flatness of W.
The ambient P^2_R is integral and F is nonzero, so W is an effective
Cartier hypersurface of degree three.

The geometric generic fiber is the unchanged smooth elliptic curve.
By the imported minimal-model reduction criteria, its geometric
special fiber is smooth or nodal according as the reduction is good
or multiplicative. A nonsplit multiplicative node is nodal after
geometric base change; its branches need not be k-rational. This
geometric test makes no extension of the actual base R. These are
the only two kinds of fibers to check on Spec R.

For either geometric fiber, over an algebraically closed field l,
the defining cubic is still nonzero (its A^3 coefficient is -1).
The hypersurface exact sequence on P^2_l is

    0 -> O(-3) -> O -> O_(W_l) -> 0.

[Stacks, Lemma 30.8.1, tag 01XT](https://stacks.math.columbia.edu/tag/01XT)
gives H^0(O)=l, H^1(O)=H^2(O)=0, H^0(O(-3))=H^1(O(-3))=0,
and H^2(O(-3))=l. Hence H^0(O_(W_l))=l and H^1(O_(W_l))=l.
The first identity forces connectedness, since a disconnection would
give a nontrivial global idempotent. The arithmetic genus is one.
Each fiber is a pure one-dimensional Cartier hypersurface in the
smooth surface P^2_l, hence Cohen–Macaulay and Gorenstein. This is
arithmetic genus, not the genus of a nodal fiber's normalization.

### Smooth Cartier marking and whole-DVR divisor

On B=1 put a=A/B and c=C/B. The equation is

    h=cU-a^3=0,
    U=1+a1 a+a3 c-a2 a^2-a4 ac-a6 c^2.

Along the whole section S, U=1 and partial h/partial c=1.
The relative hypersurface Jacobian criterion therefore makes W/R
smooth along S in every residue characteristic. On the neighborhood
where U is invertible, c=a^3/U, so the section ideal (a,c) equals
(a). It defines an effective Cartier divisor: in R[a,c], a is
prime, and h modulo a is c(1+a3 c-a6 c^2), a nonzero polynomial.
If a b=h d, primality implies d=a d1; cancellation then gives
b=h d1. Consequently multiplication by a on R[a,c]/(h) is
injective, and remains so on localization. Outside S its ideal
is the unit ideal. Thus the section is a smooth Cartier marking.

The zero scheme of the hyperplane coordinate C is
Proj R[A,B]/(A^3). Every homogeneous prime in this Proj contains
A and must omit B, so it lies entirely in B!=0. There its ring
is R[a]/(a^3); its support is exactly S over the entire DVR.
On the neighborhood of S used above its Cartier ideal is
(c)=(a^3), since U is a unit and a is a nonzerodivisor. Away
from S the hyperplane section is invertible in local trivializations.
These statements identify its Cartier divisor over all of Spec R,
without an extra vertical component:

    div(C)=3S,  O_W(3S)=O_W(1).

This proves the required invertible-sheaf identity, not only a
fiberwise degree. The coefficients a1,a3 are retained throughout,
and nothing divides by 2 or 3 or assumes split node branches.

### Relative duality and stability

Let i:W -> P=P^2_R, p:P -> Spec R and f=p composed with i.
The base is noetherian and affine; P is quasi-compact and separated.
The Cartier immersion i is of finite presentation and
pseudo-coherent, with normal bundle O_W(3). The proper flat
finite-presentation family f has equidimensional one-dimensional
Cohen–Macaulay geometric fibers, which are Gorenstein as checked
above. These verify the hypotheses of the following relative
formulas without any assumption that W's total space is regular.

[Stacks, Lemma 48.15.1, tag 0A9W](https://stacks.math.columbia.edu/tag/0A9W)
for the trivial rank-three projective bundle gives
p^!O_R=O_P(-3)[2]. The pseudo-coherent closed-immersion right
adjoint of [Lemma 48.9.7, tag 0A9X](https://stacks.math.columbia.edu/tag/0A9X),
the effective Cartier formula of
[Lemma 48.14.2, tag 0AA4](https://stacks.math.columbia.edu/tag/0AA4),
and proper composition in
[Lemma 48.16.3, tag 0ATX](https://stacks.math.columbia.edu/tag/0ATX)
yield, on the whole family,

    f^!O_R=i^!p^!O_R
           =(O_W(-3) tensor O_W(3))[2-1]=O_W[1].

The Cartier formula applies to the bounded locally free complex
O_P(-3)[2]; derived pullback here is ordinary pullback of that
line bundle with its indicated shift. The normal twist cancels
the cubic twist. By [Lemma 109.19.1 and Definition 109.19.2,
tag 0E6N](https://stacks.math.columbia.edu/tag/0E6N), the relative
curve dualizing sheaf is H^(-1)(f^!O_R), hence omega_(W/R)=O_W.
[Lemma 109.19.3, tag 0E6R](https://stacks.math.columbia.edu/tag/0E6R)
gives invertibility and base-change compatibility for these
Gorenstein fibers. The relative complex shift [1] is distinguished
from degree-one Ext in the ambient Cartier calculation.

Since W is a closed subscheme of P^2_R, O_W(1) is relatively
very ample. The identity O_W(S)^3=O_W(1) and
[Stacks, Lemma 29.38.2, tag 01VG](https://stacks.math.columbia.edu/tag/01VG),
with [Lemma 28.27.2, tag 01PT](https://stacks.math.columbia.edu/tag/01PT),
imply that O_W(S) is relatively ample. Therefore
omega_(W/R)(S) is relatively ample. All of Hassett's one-marking,
weight-one stable-family conditions now hold. There is no collision
condition with another marking. The pointed generic isomorphism
also identifies W_K minus S_K with E_L/K minus O.

### All places, retention and limitations

The choice of v was arbitrary. General equations and geometric
nodality handle p=2,3 and nonsplit multiplicative places over their
original DVRs. No global minimal equation or gluing of the local
models is required for this local stable-reduction assertion. The
test thus passes at every finite G-place without enlarging G or
any completion. Neither G/Q normality nor everywhere splitness
was used or proved.

The curve, field generators, auxiliary choices and embedding were
fixed throughout, so L078's H,N equalities persist. The original
retained E_0,F,K_glob,q_0 and unfinished work are not replaced.
ATTEMPTS/027,028,031,032,033,034 remain unaffected; in particular,
the different descent-model quantifier and the stopped cyclic
Frobenius separator are not reopened by this construction.

This supplies a local initial-data prerequisite by known methods,
not progress beyond the cited general results. G/Q normality and
the mixed radical/15-torsion kernel, other initial-data clauses,
retained radical memberships/scalar occurrence, native input/action,
marked all-image factorization, pilot transport, essentiality and
the original finite B>=A remain unresolved. The separate critical
audit below validates only this application.

### Separate critical audit — 2026-10-18, step325

The invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-18-exact-legendre-pointed-reduction-critical-audit.md`
covers exactly this audit. Checked the complete proof above, L081's
proof and completed audit, and L078's field/pointed-curve construction
and completed audit. Reused the inspected primary statements and proof
cases at the precise locations cited above; no fresh retrieval or new
general theorem is claimed. L062's completed audit is method context,
not a mathematical input about E_L/G.

**Base and minimal-model bridge.** L078 gives a finite number field G
and t!=0,1, so the generic curve is indeed an elliptic curve with the
specified origin. Every finite completion is a characteristic-zero
complete discrete valuation field with finite perfect residue field.
L081 applies to this curve at every such completion, with no normality
hypothesis. Thus Conrad's minimal general-Weierstrass existence and
reduction criteria apply over each actual R. The isomorphism to E_L
is pointed and defined over K, not merely over an algebraic closure.
No use is made of minimality of the displayed global Legendre equation.
The semistable alternatives are good and multiplicative reduction;
in the latter case the imported criterion is geometric nodality,
including nonsplit tori and residue characteristics 2 and 3. Neither a
regular polygon nor a splitting extension replaces the local cubic.

**Flat family and geometric fibers.** In -F the coefficient of A^3
is 1 and every other A-power is at most two. Polynomial division over
R[B,C] therefore gives the asserted free module with basis 1,A,A^2.
It is R-flat. Each homogeneous localization is R-flat and its integer
grading decomposes it as a direct sum of R-modules; taking the
zero-degree summand preserves flatness. This checks the affine charts
of Proj rather than assuming flatness of Proj from a slogan. The
nonzero cubic section is a nonzerodivisor in each ambient local
trivialization, since P^2_R is integral. It defines the effective
Cartier immersion of finite presentation used in duality. After every
geometric base change its A^3 coefficient remains -1, so the fiber
hypersurface exact sequence is still exact. The stated projective
cohomology gives H^0=l and H^1=l; these prove connectedness and
arithmetic genus one. A nonzero hypersurface in P^2_l is pure of
dimension one and locally a regular ring modulo a nonzerodivisor,
so the needed Cohen–Macaulay and Gorenstein fiber conditions hold.
The imported smooth/nodal criterion supplies reduced nodal fibers;
cohomology alone is not being used to infer nodality.

**Smooth Cartier section and divisor over R.** Substituting B=1 in
F gives exactly c(1+a1 a+a3 c-a2 a^2-a4 ac-a6 c^2)-a^3.
At a=c=0 the c derivative is 1, at the generic and closed points
of the section alike. The section is in the relative smooth locus.
The polynomial h modulo a is c(1+a3 c-a6 c^2), which is nonzero
because its c coefficient is 1. Thus a does not divide h in the
domain R[a,c], while (a) is prime. From a b=h d one obtains a|d
and then b in (h); this proves a is a nonzerodivisor modulo h.
On the open U!=0 containing the entire section, (a,c)=(a) and
(c)=(a^3). Setting a=0 on that open also forces c=0, so this
Cartier ideal has no extra component there. Outside S the section
ideal is the unit ideal. Finally C=0 in Proj forces A^3=0 and
B!=0, so its zero scheme is entirely on this chart and has ring
R[a]/(a^3). Its support is S, and U becomes a unit on it (equal
to 1 plus a nilpotent). Consequently the local identity (c)=(a^3)
and invertibility off S cover the whole zero divisor. There is no
missing vertical component. The equality div(C)=3S is an equality
of effective Cartier divisors over R, yielding O_W(3S)=O_W(1).
None of these steps divides by 2 or 3 or chooses node branches.

**Relative duality and ample marking.** The affine noetherian base,
proper separated finite-presentation maps and pseudo-coherent Cartier
immersion meet the cited right-adjoint/composition hypotheses. The
normal line bundle is O_W(3). The projective formula uses the trivial
rank-three module, so its determinant contributes no additional line:
p^!O_R=O_P(-3)[2]. The Cartier formula is applied only to this
bounded locally free complex, so derived pullback is its ordinary
line-bundle pullback with shift. The normal twist and Cartier shift
give i^!p^!O_R=O_W(-3) tensor O_W(3)[1]=O_W[1].
This is a global relative formula, with H^(-1)=O_W; the ambient
Ext degree is not substituted for the relative degree. The checked
proper flat curve-family and Gorenstein hypotheses allow 0E6N/0E6R
to identify this with omega_(W/R), with the required base change.
The Cartier marking gives an invertible sheaf O_W(S), whose third
power is the relatively very ample O_W(1). The positive-power
ampleness criterion therefore gives relative ampleness of
omega_(W/R)(S). For Hassett's type (g,n)=(1,1) and weight 1,
2g-2+1=1>0; the only marking lies in the smooth locus and there
is no marking collision. All stable-family conditions are satisfied.

**Verdict and limits.** The audit passes without a mathematical
repair, additional hypothesis or field extension. It verifies the
known-method prerequisite at every unchanged finite G-place, not a
new reduction theorem or progress beyond the sources checked. All
choices and the two embedded H,N equalities persist. Direct local
inputs remain L078 and L081; no DAG change is needed. The argument
itself is unchanged, so PROOF.md is left untouched; this canonical
verdict supersedes its pending-audit wording for L082. Normality,
other initial data, actual input/action, marked factorization, pilot
transport, essentiality and original finite B>=A remain unresolved.

## Mathlib

Full matching and supporting Mathlib coverage for this exact-G
application, the minimal-Weierstrass bridge and the relative
pointed-family calculation has not been checked. No absence or
formal-verification claim is made. The general inputs are the
precisely cited classical and Stacks results; the work here verifies
their hypotheses for the unchanged E_L/G. No numerical certificate
or mathematical script is used. Classification: REPRODUCTION under
SPECIALIZE; the separate step325 audit validates the application,
without a formal-verification claim.
