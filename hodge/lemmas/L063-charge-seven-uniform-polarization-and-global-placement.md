# L063 — Conditional charge-seven family has uniform integral polarization and global placement

## Hypotheses

Let B and Y be the two copies of L044's smooth projective complex
K3 surface S, with its marking and algebraic real ample class
h=omega_c in NS(S)_R. Retain precisely L060's conditional rank-two
locally free holomorphic bundle F on B x Y: it is slope-polystable
at p_B^*h+p_Y^*h, with c_1(F)=0 and
ch_2(F)=-6e_1-7e_2+tau_D. In particular L060 supplies, for every
closed x in B, the locally free h-slope-stable bundle

\[
E_x=F|_{\{x\}\times Y},\qquad
\operatorname{rk}(E_x)=2,\quad c_1(E_x)=0,\quad c_2(E_x)=7\eta,
\]

where eta is the integral point class of degree one on Y. These
are actual restrictions of F, not a collection of numerically
compatible hypothetical fibres. Existence of F is not assumed to
have been established.

## Conclusion

There is one ample integral line bundle H on Y for which every
E_x is slope-stable. With the GAGA algebraization of F, this family
induces a global algebraic morphism

\[
f_F:B\longrightarrow M_H^s(2,0,-5),\qquad x\longmapsto[E_x].
\]

Here M_H^s(2,0,-5) is the stable numerical-class locus in the
projective Gieseker moduli scheme for the fixed Hilbert polynomial
P_H(n)=H^2n^2-3. The class is the Mukai vector
v=ch(E_x)sqrt(td(Y))=(2,0,-5). The image consists of locally free
sheaves. We assert neither that H is v-generic nor that this stable
locus is projective. No universal sheaf on the moduli space is used.

This is a conditional specialization of published chamber and
moduli theorems, classified as REPRODUCTION. It establishes neither
F existence, global injectivity, an embedding, a metric identity,
inverse/reconstruction, transverse transport nor a new cycle. In
particular it does not close the universal primitive Hodge gap.

## Proof

**Known input and reason for the specialization.** Import Daniel
Greb and Matei Toma, *Compact moduli spaces for slope-semistable
sheaves*, Algebraic Geometry **4** (2017), no. 1, 40--78,
doi:10.14231/AG-2017-003,
[Definition 2.3, p. 44](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=5)
and [Theorem 6.6 with proof and Section 6.3.3, pp. 74--75](https://content.algebraicgeometry.nl/2017-1/2017-1-003.pdf#page=35).
For fixed topological invariants of torsion-free sheaves on a smooth
complex projective n-fold and compact K in
P(Y)={A^(n-1): A in Amp(Y)_R}, finitely many rational linear walls
give chambers on which slope stability and semistability of every
such sheaf are unchanged. Chambers include connected strata of
lower dimension. The real-polarization theorem is imported, not
reproved. Its finite-wall uniform quantifier, rather than pointwise
openness for individual E_x, is the essential input here.

L044's cone proof puts h in Amp(Y)_R within NS(Y)_R. On this
surface n=2, so A^(n-1)=A; the numerical curve class paired with
first Chern classes is just the numerical divisor class A under
the nondegenerate intersection pairing. Thus P(Y) is the real
ample cone in this identified numerical space. A torsion-free
rank-two sheaf on Y has no Chern classes beyond c_2. Consequently
(2,0,7eta) fixes all the topological invariants required here.

**One rational stratum representative, including equality walls.**
Write V=N^1(Y)_R, with rational structure N^1(Y)_Q. Choose a
compact convex neighborhood K of h whose interior contains h and
which is contained in Amp(Y)_R; this is possible because that cone
is open. Apply the imported theorem to K and the fixed invariants.
Write its finite rational wall equations as ell_i(alpha)=0.
Let I_0={i:ell_i(h)=0} and

\[
W=\bigcap_{i\in I_0}\ker(\ell_i)\subset V.
\]

This is a rational linear subspace and contains h. Row reduction
of its rational defining matrix supplies a rational basis; rational
linear combinations of that basis are dense in W. Every ell_i(h)
for i outside I_0 is nonzero. Finiteness and continuity therefore
give a relative neighborhood U of h in W, inside the interior of
K, on which all those signs agree with their values at h.
Choose a rational alpha in U. It is ample, lies on exactly the
walls containing h, and lies on the same side of every other wall.

Moreover the segment from h to alpha lies in K and in W. Each
nonzero wall functional has the same strict sign at both endpoints
and hence throughout the segment. The endpoints thus belong to
the same connected relative stratum, including when this stratum
has dimension less than rho(Y). The imported theorem gives

\[
E\text{ is h-slope-stable}\quad\Longleftrightarrow\quad
E\text{ is alpha-slope-stable}
\]

simultaneously for every torsion-free E with the specified
invariants. This applies to every E_x. No assumption that h avoids
walls, and no separate perturbation depending on x, has been made.

Choose a positive integer m_0 clearing alpha's denominators in the
divisor lattice and a line bundle H_0 with numerical class m_0 alpha.
Ampleness depends only on numerical class, so H_0 is ample. Choose
a positive integer k sufficiently large that H=H_0^{tensor k} is
very ample, and put m=k m_0. This uses the standard ample-power
criterion (Hartshorne, *Algebraic Geometry*, Chapter II, Theorem 7.6)
on the projective scheme Y. In the
definition mu_alpha(E)=c_1(E).alpha/rk(E), replacing alpha by
m alpha multiplies every slope by the same positive number.
It preserves all strict inequalities. Thus one integral, indeed
very ample, H makes every E_x slope-stable, as asserted. Here and
below H denotes this final power; its square in P_H is the square
of its final first Chern class. The relatively very ample bundle
p_Y^*H on B x Y meets the polarization convention in the cited
openness and moduli construction. No claim that m alpha remains
inside K is needed: after the chamber theorem, scaling preserves
slopes directly. This rational-density and
scaling argument is the necessary surface specialization; no new
general wall theorem or explicit wall enumeration is claimed.

**The actual flat family and its class.** L060's GAGA passage
algebraizes F as a vector bundle on B x Y. The projection to B is
flat and F is locally free on the product, so F is flat over B.
Every closed fibre is locally free, hence pure of dimension two.
Import Huybrechts and Lehn, *The Geometry of Moduli Spaces of
Sheaves*, Aspects of Mathematics E31 (1997),
[Lemma 1.2.13, p. 14](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=26):
for such full-dimensional pure sheaves slope stability implies
Gieseker stability at the same H. Every closed E_x is therefore
H-Gieseker-stable.

Since td(Y)=1+2eta and c_1(E_x)=0, surface Riemann--Roch gives

\[
\begin{aligned}
ch(E_x)&=2-7\eta,\\
\chi(E_x\otimes H^n)
 &=\int_Y(2-7\eta)\exp(nc_1(H))(1+2\eta)
   =H^2n^2-3,\\
v(E_x)&=(2-7\eta)(1+\eta)=2-5\eta.
\end{aligned}
\]

The Riemann--Roch calculation also fixes all Euler pairings with
classes in K_0(Y), not just this polynomial: for any A in K_0(Y),
chi(E_x tensor^L A) is the integral of
(2-7eta)ch(A)td(Y), independently of x. Thus the family has the
fixed numerical K-class recorded by v=(2,0,-5). Equivalently these
are the usual Ext Euler pairings with A dualized; duality permutes
K_0(Y) because Y is smooth. This is stronger than fixing P_H alone.

**All geometric fibres and the coarse map.** Import
[Huybrechts--Lehn Proposition 2.3.1, p. 45](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=57)
for openness of geometric stability in this flat polarized family.
The open geometrically stable locus in B contains every closed
point: their residue field is the algebraically closed field C,
and we just proved stability there. The complement is closed. A
nonempty closed subset of B, a finite-type C-scheme, contains a
closed point. Hence that complement is empty. This checks all
geometric fibres, including those over nonclosed points, rather
than substituting generic stability.

Import the moduli functor of
[Huybrechts--Lehn Section 4.1, p. 80](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=92)
and [Theorem 4.3.4, p. 91](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=103).
It corepresents flat Gieseker-semistable families of fixed Hilbert
polynomial modulo tensoring by a line bundle from the base, with
the stable open corepresenting geometrically stable families.
The actual family F is such an object over B. Applying the
corepresenting natural transformation to it produces an algebraic
morphism from B to the stable open in the projective moduli scheme
of polynomial H^2n^2-3; at a closed point it sends x to [E_x].

Finally use the fixed numerical-class parts described in
[Huybrechts--Lehn Section 8.1, p. 180, before Definition 8.1.4](https://ncatlab.org/nlab/files/HuybrechtsLehn.pdf#page=192).
Numerical Euler pairings are locally constant in flat families,
and fixed numerical-class parts are open and closed. The computed
numerical K-class therefore places this morphism in the part
M_H^s(2,0,-5). We have not identified the whole fixed-polynomial
space with this part. This construction uses corepresentation,
not a universal bundle on that space, and supplies the required
global algebraic map without a fine-moduli hypothesis.

**Critical audit, 2026-10-06.** The conditional conclusion survives
the separate audit. L044 supplies an algebraic real ample class,
not merely a positive-square vector; L060 supplies actual stable
restrictions at every closed point. The rational equations defining
W retain equality walls, and convexity plus strict signs supply
the required connected stratum even when it has lower dimension. The theorem's
fixed-invariant quantifier precedes the choice of E_x, so the same
H works for the entire family. The power choice above makes the
very-ample source convention explicit. GAGA and product flatness
supply an actual flat family, not just closed-point moduli data.
Geometric-stability openness and the closed-point test cover the
nonclosed fibres. The computed Euler pairings, together with the
open-and-closed numerical-class parts, justify factorization as a
morphism, not merely set-theoretic containment of closed points.
The Hilbert polynomial and Mukai vector agree with the final H.
No substantive counterexample or failure of the placement argument
was found. The power clarification and corrected source locator
introduce no new mathematical result beyond the cited inputs.
F existence and every asserted limitation in the conclusion remain
unresolved; the audit does not establish a Hodge candidate.

## Mathlib

Full coverage of the real fixed-Chern uniform chamber theorem and
the stable-family algebraic coarse moduli construction: **not
checked**. No matching declaration or absence is asserted. The
argument uses the cited primary theorems and the explicit surface
and family applicability checks above; it is not a Lean verification.
