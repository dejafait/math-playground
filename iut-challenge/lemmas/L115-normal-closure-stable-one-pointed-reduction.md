# L115 — Stable one-pointed reduction over the unchanged normal closure

## Hypotheses

Fix any survivor and ordering o as in L090. In its fixed algebraic
closure retain the literal pointed curve and full-coordinate fields

    E_o: V^2=X(X-1)(X-t_o), O=[0:1:0],
    G_o=Q(t_o)(iota,E_o[15]), iota^2=-1,
    C_o=G_o^nor over Q.

Here t_o!=0,1, G_o is a number field, and every coordinate of every
geometric 15-torsion point belongs to G_o. No ell-integrality assumption
from L098 is imposed: only its explicitly unconditional full-torsion
semistability subargument is used. No stable model, splitting extension
or global minimal equation is assumed.

## Conclusion

At every finite place w of this unchanged C_o, (E_o,O) has a stable
one-pointed genus-one model over R=O_((C_o)_w), with pointed generic
fiber isomorphic to (E_o,O) over K=(C_o)_w itself. This includes residue
characteristics 2,3 and nonsplit multiplicative reduction.

In particular the conclusion applies to the unchanged member chosen in
L105; its prime, fields, torsion and covers need not be reselected. This
is only the all-finite-place stable-reduction requirement in the qualified
IUT I Definition 3.1(b), not the whole clause or complete initial data.
It is a known-method application, validated by the step473 audit below;
no essential IUT flaw or original finite B>=A conclusion follows.

## Proof

### Scope and imported inputs

Use the invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-25-normal-closure-stable-pointed-reduction.md`.
The intermediate target is the conclusion above; its downstream use is
only that stable-reduction requirement. The test is a stable pointed
family over every original DVR, without changing the pointed generic
curve. Other initial-data and numerical gaps are independent.

Import Conrad, *Minimal models for elliptic curves*, 21 November 2015,
[section 2 pp.2,6, Theorem 5.5 and proof/discussion pp.14–16](https://math.stanford.edu/~conrad/BSDseminar/refs/minimalmodel.pdf),
and Milne, *Elliptic Curves*, second edition (2021),
[II.3 pp.59–61](https://www.jmilne.org/math/Books/EC2.pdf).
These give a minimal integral general Weierstrass equation for the same
pointed elliptic curve over a DVR, and identify good/multiplicative
reduction with smooth/geometrically nodal special cubics. Neither
residue characteristic greater than three nor splitness is required.

Use Hassett, *Moduli spaces of weighted pointed stable curves*,
[math/0205009v1, 1 May 2002, section 2, printed pp.3–4](https://arxiv.org/pdf/math/0205009v1),
for the stable-family definition with (g,n)=(1,1) and weight one.
The page numbers are the correction recorded in step470. The general
theorems and definition are imported, not reproved.

L082's sections “The actual local family and fibers”, “Smooth Cartier
marking and whole-DVR divisor” and “Relative duality and stability”,
with their step325 audit, contain universal calculations for a complete
number-field DVR R and arbitrary integral general Weierstrass
coefficients a_i. We use those calculations under exactly those
hypotheses. We do not use L082's E_L/G conclusion, its auxiliary
parameters, H,N equalities, or L078/L081 curve-specific assertions.
The instantiation and its source hypotheses are checked below rather
than duplicating that full calculation as a new general result.

### Same curve and every original completion

Fix any finite w|p of C_o. This is a finite number field because it is
the normal closure of the number field G_o. Thus K=(C_o)_w is a finite
extension of Q_p and R is a complete noetherian DVR with finite perfect
residue field. L090's t_o!=0,1 makes E_o/K a smooth elliptic curve with
the specified rational origin. There is no use of a geometric
isomorphism from another curve to descend a local model.

Apply L098's subsection “Full torsion and semistability at every actual
completion” and its step393 audit. That subargument uses only these
fields and full-coordinate torsion, not the additional premise
v_ell(j(E))>=0 appearing in its support statement. Specifically the
entire E_o[n] is a constant finite etale scheme of rank n^2 over C_o
for n=3,5, since all its points are already rational there. Completion
preserves this disjoint union. Level five when p!=5 and level three
when p=5 are prime levels at least three invertible in R, including
at p=2,3. The imported torsion criterion is Mochizuki, IUT IV, April
2020 [reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%204.pdf),
Proposition 1.8(v), printed p.19, proof p.20, with L098's source
qualification retained. Hence the same E_o/K is semistable. No
conditional support exclusion, ell-integrality, selected place or
splitness is inferred.

Choose the imported minimal general equation over this R, with its
pointed K-isomorphism to E_o/K. In L082's notation its projective family
and marking are

    W=Proj R[A,B,C]/(F), S=[0:1:0],
    F=B^2 C+a1 ABC+a3 BC^2-A^3-a2 A^2 C-a4 AC^2-a6 C^3,
    a_i in R.

This is a new local equation for the same pointed generic curve, not
an assumption that the literal Legendre equation is integral or minimal.
The pointed generic isomorphism is defined over K itself. The base,
coefficient and semistability hypotheses of L082's universal computation
are now all met.

### Applying the covered family calculation

The monic-in-A calculation of L082 makes the homogeneous coordinate
ring free with basis 1,A,A^2 over R[B,C]. Localization and the
degree-zero direct summand give R-flat affine charts. Thus W/R is
proper, flat and of finite presentation; its cubic immersion into
P^2_R is effective Cartier. The imported reduction criterion gives
smooth or geometrically nodal special fiber. A nonsplit node is tested
geometrically; no extension of R is performed. The generic fiber is
the specified smooth elliptic curve.

For each geometric fiber, the cubic exact sequence and
[Stacks Lemma 30.8.1, 01XT](https://stacks.math.columbia.edu/tag/01XT),
as computed in L082, give H^0(O)=k_bar and H^1(O)=k_bar. Thus fibers
are connected of arithmetic genus one. They are pure one-dimensional
hypersurfaces in a smooth surface, hence Cohen–Macaulay and Gorenstein.
Nodality is supplied by the reduction criterion, not by cohomology.

The general a_i computation in L082 applies on B=1 without omitting
a1,a3. In its coordinates a=A/B,c=C/B the equation is cU-a^3=0,
where U=1+a1 a+a3 c-a2 a^2-a4 ac-a6 c^2. Along S the c derivative
is 1. On U!=0 the section ideal is (a), with a a nonzerodivisor,
so S is a smooth effective Cartier marking. L082 checks this over
the whole DVR, including the closed point. Its hyperplane calculation
C=0 gives Proj R[A,B]/(A^3), entirely in B!=0 with support S, and
(c)=(a^3) near that support. Consequently its whole-family Cartier
identity, with no vertical component, applies here:

    div(C)=3S,                 O_W(3S)=O_W(1).

These statements use arbitrary a_i in a DVR and neither the old
curve's parameters nor division by 2 or 3.

For completeness the hypotheses of L082's relative-duality application
also match. R is affine noetherian; the projective ambient scheme is
quasi-compact and separated. The cubic immersion is finite-presentation
and pseudo-coherent, with normal line O_W(3). The proper flat family
has the equidimensional Cohen–Macaulay and Gorenstein geometric fibers
just checked. Thus the projective-bundle, closed-immersion, Cartier and
proper-composition formulas apply:
[48.15.1, 0A9W](https://stacks.math.columbia.edu/tag/0A9W),
[48.9.7, 0A9X](https://stacks.math.columbia.edu/tag/0A9X),
[48.14.2, 0AA4](https://stacks.math.columbia.edu/tag/0AA4), and
[48.16.3, 0ATX](https://stacks.math.columbia.edu/tag/0ATX).
For p:P^2_R -> Spec R and i:W -> P^2_R, L082's cancellation is

    p^!O_R=O(-3)[2],
    (p i)^!O_R=i^!p^!O_R=(O_W(-3) tensor O_W(3))[2-1]=O_W[1].

Here the Cartier formula is applied to a bounded locally free complex;
no regularity of W's total space is assumed. The curve-family
[109.19.1/Definition 109.19.2, 0E6N](https://stacks.math.columbia.edu/tag/0E6N)
and Gorenstein base-change
[109.19.3, 0E6R](https://stacks.math.columbia.edu/tag/0E6R)
therefore identify omega_(W/R)=H^(-1)((p i)^!O_R)=O_W.
The relative degree -1 is not ambient Ext degree one. Stacks inputs
retain the inspected live-version qualification of the reused records.

Finally O_W(1) is relatively very ample and O_W(S)^3=O_W(1).
The positive-power ampleness criterion
[29.38.2, 01VG](https://stacks.math.columbia.edu/tag/01VG), with
[28.27.2, 01PT](https://stacks.math.columbia.edu/tag/01PT),
gives relative ampleness of omega_(W/R)(S)=O_W(S). The one smooth
marking has weight one, no collision, and 2g-2+1=1>0. All of the cited
stable-family conditions hold, with the required pointed generic fiber.

### Quantifier and limitations

The place w was arbitrary, and the construction takes place over its
original DVR. It proves the all-finite-place assertion without gluing
local equations or enlarging C_o. In particular the L105 selection is
retained; none of its image or prime-selection conclusions is needed
as a mathematical premise for this uniform statement.

The target's continuation test passes. This is local progress by known
methods, not mathematics beyond the checked sources. Under the qualified
May 2020 IUT I Definition 3.1(b), printed pp.61–62
([reproduction](https://kyl.neocities.org/books/%5BTEC%20MOC%5D%20inter-universal%20teichmuller%20theory%20-%20vol%201.pdf)),
it supplies only stable pointed reduction. Author/reproduction byte
identity and journal-version equivalence remain unverified. Full
(a)–(c)/initial data/III/P7, directed (*), generation/full repair,
factor-four excess, actual action/factorization/pilot, authentication/
def=, essentiality and original finite B>=A remain separate. No U/B
descent, full B[ell] rationality or global theta splitting is asserted.
ATTEMPTS/031,033–035 remain preserved; this application uses none of
their stopped mechanisms. The separate critical audit follows.

### Separate critical audit — 2026-10-25, step473

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-25-normal-closure-pointed-critical-audit.md`.
This audit checks the full application above and the actual passages
used from L090, L098 and L082. General theorems are imported at the
precise citations above. The step470/472 and 18 October source records,
and the 12 October relative-duality proof-case record, supply adequate
coverage; no new retrieval, authentication or general reproof is needed.
The question is applicability to this curve, not whether the old
E_L/G application already received an audit.

**Unconditional input and actual completions.** L090 defines t_o from
three distinct algebraic roots. Its denominator is nonzero, and its
numerator is neither zero nor that denominator, so t_o!=0,1. The
literal E_o is therefore nonsingular in characteristic zero with
the stated rational origin. Its finite full-coordinate torsion field
G_o and normal closure C_o are number fields. Each actual completion
K is consequently a finite extension of Q_p with complete noetherian
DVR R and perfect finite residue field. These are the base hypotheses
of the imported minimal-model and torsion results.

For n=3,5 the entire E_o[n] lies in E_o[15], and its n^2 geometric
points are C_o-rational, including both coordinates. The finite etale
kernel scheme is thus the disjoint union of n^2 copies of Spec C_o.
Completion preserves this scheme decomposition, not merely a chosen
subgroup or x-coordinate set. At p=2,3 and every p!=5, level five is
an invertible prime at least three; at p=5, level three is such a
prime. IV 1.8(v) yields semistability over K itself in each case.
This verifies L098's extracted subargument without its extra
v_ell(j(E))>=0 premise: neither that premise nor its support
classification occurs in this reasoning. The level argument works
also at the selected ell. It does not assert good reduction there.

**Same pointed curve and family.** The minimal general Weierstrass
equation exists over this R with a pointed isomorphism over K to E_o.
No use is made of the geometric change from the original rational
curve in L090 to descend a model, nor of global Legendre minimality.
Conrad's cited bridge gives smooth or geometrically nodal special
cubics for the semistable cases. Split branches and p>3 are not
hypotheses. Thus the universal computation in L082 has exactly its
required arbitrary integral a_i and complete-DVR inputs here.

Polynomial division in A makes the homogeneous ring free on 1,A,A^2
over R[B,C]; homogeneous localizations remain R-flat, and their
degree-zero pieces are R-module direct summands. This verifies
flatness on all projective charts. The cubic is a nonzero section
on integral P^2_R, hence effective Cartier, and the family is proper
of finite presentation. On each geometric fiber its A^3 coefficient
remains -1. The cubic exact sequence and 01XT give H^0=H^1=k_bar.
Consequently the fibers are connected of arithmetic genus one;
they are pure one-dimensional Cohen–Macaulay and Gorenstein
hypersurfaces. Smoothness or nodality comes from the reduction
criterion, not the cohomology calculation. A DVR has only its generic
and closed fibers to check.

**Whole-DVR marking.** On B=1 the displayed h=cU-a^3 has derivative
1 in c along the entire origin section. The origin is in the relative
smooth locus. The calculation proving a a nonzerodivisor works in
R[a,c]: the ideal (a) is prime and h modulo a has c coefficient 1,
so a b=h d forces d=a d1 and b=h d1. On U!=0, which contains the
whole section, (a,c)=(a). Thus the section is effective Cartier.
The hyperplane C=0 has coordinate ring R[a]/(a^3) on B!=0 and
no support outside this chart. Its support is precisely S; U restricts
there to a unit (1 plus a nilpotent). Hence (c)=(a^3) holds near
all its support, and off S both Cartier ideals are units. This
checks div(C)=3S over R, with no hidden vertical divisor. It uses
the general a1,a3 terms and no division by 2 or 3.

**Duality and stability.** The noetherian affine base, proper
finite-type maps, quasi-compact separated projective ambient scheme
and pseudo-coherent effective Cartier immersion satisfy 0A9W,
0A9X, 0AA4 and the proper case of 0ATX. The ambient projective
bundle is the trivial rank-three bundle, so no determinant line is
missing from O(-3)[2]. The Cartier normal line is O_W(3); its
twist cancels O_W(-3) and its shift is [-1]. Applied to the bounded
locally free complex O(-3)[2], these formulas give f^!O_R=O_W[1].
The checked proper flat curve-family and Gorenstein fiber hypotheses
allow 0E6N/0E6R to identify H^(-1) with the invertible relative
dualizing sheaf, compatible with base change. No regular total-space
assumption or ambient-Ext/relative-degree substitution is made.
The Cartier marking's line bundle has third power O_W(1), which
is relatively very ample. Tags 01VG/01PT therefore give relative
ampleness of omega_(W/R)(S). The single marking is smooth, its weight
is one, and 2g-2+1=1>0. This verifies all the cited stable-family
conditions, with the original pointed K-generic fiber.

**Verdict and limits.** The audit passes without a mathematical
repair, new assumption or field extension. The place was arbitrary,
so the conclusion holds at every original finite completion, including
2,3 and nonsplit nodes. This validates a local known-method input,
not mathematics beyond the checked sources. Direct inputs remain
L082 (universal calculation only), L090 (literal definitions and
nonsingularity), and L098 (unconditional torsion subargument only).
L105 merely identifies a retained member of the uniform assertion;
no additional mathematical input or DAG edge is needed. The argument
is unchanged, so PROOF.md and DAG.md are not edited; this canonical
verdict supersedes PROOF.md's pending-audit wording for L115.
The source-authentication, Mathlib and independent initial-data and
finite B>=A limitations stated above all remain. No complete-solution
candidate or essential IUT flaw is established.

## Mathlib

Full matching and supporting Mathlib coverage for this exact E_o/C_o
application, minimal-Weierstrass bridge and relative pointed-family
argument have not been checked. Unknown coverage is not absence.
Classification: REPRODUCTION under the saved SPECIALIZE assessment.
No mathematical script, numerical evidence or formal-verification claim
is used; the separate step473 audit validates this application only.
