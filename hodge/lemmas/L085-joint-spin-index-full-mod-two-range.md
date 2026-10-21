# L085 — The fixed quaternionic-line class has full joint mod-two index range

## Hypotheses

Let S be L071's marked projective K3 surface, X=S x S, and retain
L079's integral class

\[
u=9e_1+10e_2+\tau_D,\qquad \tau_D^2=156P,
\quad e_1e_2=P,\quad \int_XP=1.
\]

Both factors have their complex orientation and unique spin structure.
Let Q range over **all topological quaternionic lines** on X with
c_2(Q)=u. This range is nonempty by L071 (equivalently the finite-rank
criterion specialized in L050): 9 times 10 is 6 modulo 12.
Write f=[Q] in KSp^0(X)=KO^{-4}(X), and use L084's index convention.
Define virtual real classes on the indicated target factors by

\[
R_G(f)=-(p_2)_!^{\rm spin}f,\qquad
R_H(f)=-(p_1)_!^{\rm spin}f\quad\hbox{in }KO^0(S).
\tag{1}
\]

No holomorphic Q or actual cohomology bundle is assumed. For a virtual
real bundle A-B use w(A-B)=w(A)/w(B). Since H^1(S,F_2)=0, w_1=0
for every such class; consequently w_2 is additive and w_2(-z)=w_2(z).
If L079's holomorphic F exists, audited L084 identifies (1) with its
actual normalized real images. That conditional identification is
retained without imposing it on arbitrary topological Q.

## Conclusion

The complete attainable pair set is

\[
\boxed{\{(w_2(R_G(f)),w_2(R_H(f))):c_2(Q)=u\}
 =H^2(S,F_2)\times H^2(S,F_2).}
\tag{2}
\]

In particular all 2^44 pairs occur. Each pair is attained by a genuine
quaternionic line, not merely a stable arbitrary-rank coefficient.
The stable classes of such lines form an affine torsor under
Tor KSp^0(X)=(Z/2)^44. Their two index differences identify this torsion
group with Tor KO^0(S) x Tor KO^0(S); w_2 identifies each latter
factor with H^2(S,F_2).

Thus this joint w_2 test excludes none of L079's image alternatives.
It includes the repeated E_4 branch with w_2(R_G)=0 and every possible
w_2 for the opposite J_5, including L079's value rho_2(k). This is an
informative NEGATIVE / REPRODUCTION of the assessed topology framework:
stop the joint mod-two exclusion mechanism. It gives no actual image
identification, holomorphic common F, prescribed compatible connection,
algebraic cycle or transverse transport. The separate critical audit
below preserves this specialization; the universal Hodge gap is open.

## Proof

**Imported tools and the necessary specialization.** Use So--Theriault,
*The suspension of a 4-manifold and its applications*,
[arXiv:1909.11129v3, Theorem 1.1, Theorem 5.9 and Proposition 6.1,
pp. 1, 19--20](https://arxiv.org/pdf/1909.11129v3).
Its smooth closed orientable four-manifold has no 2-torsion in H_1;
in the simply connected spin case its suspension is a wedge of b_2
copies of S^3 and one S^5. S is simply connected and spin, with
b_2=22 and torsion-free cohomology, as retained in L050. Hence

\[
\Sigma S\simeq\bigvee_{22}S^3\vee S^5.                 \tag{3}
\]

Use the product splitting in Hatcher, *Algebraic Topology* (2002),
[Proposition 4I.1, p. 467](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf#page=476),
and the coefficient groups and real Thom module theorem in
Atiyah--Bott--Shapiro, *Clifford modules*, Topology 3, Supplement 1
(1964), [Table 2 and Theorems (6.9), (11.5), (12.1),
pp. 12, 15, 28, 30](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/abs.pdf).
The degree-four type change is also stated in Eschenburg--Hanke,
[arXiv:2011.14368v2, Theorem 10.7(b), p. 35](https://arxiv.org/pdf/2011.14368v2#page=35).
All bases here are finite CW spaces; all Thom maps below are spin
maps. General splitting, periodicity and Thom theorems are imported,
not reproved. We must still identify the actual two pushforwards and
verify finite-rank representability; an additive splitting alone does
neither. The prior assessment did not contain (2).

**Torsion on a factor is detected exactly by w_2.** From (3), suspension
and the coefficient table give

\[
KO^0(S)=Z\oplus\widetilde {KO}^0(S),\qquad
\widetilde {KO}^0(S)\cong Z\oplus(Z/2)^{22}.             \tag{4}
\]

Here the sphere contributions are KO^{-2}(pt)=Z/2 and
KO^{-4}(pt)=Z. To identify w_2 without assuming naturality of a
noncanonical splitting, choose maps from 22 copies of S^2 representing
an integral basis of H_2(S,Z), possible by the Hurewicz theorem.
Their wedge W maps to S and induces an isomorphism on H_2. Its
homotopy cofiber C is simply connected, has reduced integral homology
Z in degree four only, and is homotopy equivalent to S^4. Indeed
successive Hurewicz gives 3-connectivity and a generator S^4 -> C;
this homology equivalence of simply connected CW spaces is a homotopy
equivalence by the homological Whitehead theorem.
The reduced KO exact sequence of W -> S -> C is therefore

\[
0\longrightarrow Z\longrightarrow\widetilde {KO}^0(S)
 \xrightarrow{r}(Z/2)^{22}\longrightarrow0.             \tag{5}
\]

The adjacent groups vanish because KO^{-1}(W)=0 in reduced theory
and \widetilde {KO}^1(S^4)=KO^{-3}(pt)=0. The kernel of r is torsion-free.
By (4) the torsion subgroup has order 2^22, so its restriction by r
is an isomorphism onto the group of the same order in (5).
For the Hurewicz and homological Whitehead inputs here, import
Hatcher, *Algebraic Topology* (2002), [Theorems 4.32/4.37 and
Corollary 4.33, printed pp. 366--368 and 369--373](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf#page=375).
The spaces are simply connected CW complexes; the absolute Hurewicz
case is obtained with subspace a point. The natural Hurewicz map
identifies the chosen sphere maps with the integral homology basis.
No homology equivalence of nonsimply connected spaces is used.

On S^2 the nonzero reduced KO class is the oriented real plane of
an odd complex line minus its trivial rank: w_2 is c_1 modulo two
and evaluates to one. This is the usual real Hopf-plane representative
of KO^{-2}(pt). Naturality on the **actual sphere maps** now shows

\[
w_2:\operatorname{Tor}KO^0(S)\xrightarrow{\sim}H^2(S,F_2).
\tag{6}
\]

We used no ring identification from (3). The Whitney/inverse and
realification conventions are those of Milnor--Stasheff,
*Characteristic Classes* (1974), [Section 4, Lemma 4.1 and
Problem 14-B](https://aareyanmanzoor.github.io/assets/books/characteristic-classes.pdf).
In particular additivity here uses w_1=0, including for virtual ranks.

**The complete stable fixed-character fibre.** Stably (3) gives
S_+ = S^0 vee 22 S^2 vee S^4. Smashing the two finite sphere splittings
(or using Hatcher's product splitting first) gives sphere multiplicities
1,44,486,44,1 in dimensions 0,2,4,6,8 respectively for X_+.
Since KSp^0=KO^{-4}, the contributing coefficient groups in that order
are Z,0,Z,Z/2,Z. Consequently

\[
KSp^0(X)\cong Z^{488}\oplus(Z/2)^{44}.                 \tag{7}
\]

The rational Chern character of the underlying complex class is
injective on KSp^0(X) tensor Q. In this particular splitting this needs
only the sphere statement: complexification on each free coefficient
in dimensions 0,4,8 is multiplication by a nonzero integer, by the
ABS real/complex coefficient comparison, and the complex Chern
character on an even sphere is a rational isomorphism. The torsion
coefficients in dimension six map to zero. Thus the kernel of rational
character on the integral group (7) is exactly its torsion subgroup.
This also follows from the standard rational Chern-character theorem.

Every quaternionic line with c_2=u has complex character

\[
2-u+u^2/12=2-9e_1-10e_2-\tau_D+28P,                  \tag{8}
\]

since u^2=(180+156)P=336P, c_1=0 and rank truncation gives c_3=c_4=0.
Fix one such f_0 by L071. Every other line of this c_2 differs from
f_0 by torsion. Conversely, every f_0+delta with delta torsion has
rank one over H and the same integral Chern classes: rational equality
follows from (8), and integral cohomology of X is torsion-free.
For the converse to describe **lines**, rather than just stable
classes, the following finite-rank argument is essential.

Represent f_0+delta+[H] by a quaternionic rank-two bundle V.
Here is why a representative of exactly this rank exists. A virtual
class has a presentation [A]-[H^m], by a quaternionic complement to
its negative bundle. Its rank is two. Repeatedly split a trivial
quaternionic line from A until rank two is reached, using Husemoller,
*Fibre Bundles*, third edition (1994), [Chapter 9 Section 1,
Proposition 1.1 and Theorem 1.2, pp. 111--112](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/husemoller.pdf#page=132).
At each removed rank k>=3 the section bound is dim X=8<=4k-1.
This yields the asserted rank-two representative.

The top complex Chern class c_4(V) is zero: its stable Chern classes
are those of Q_0 plus a trivial quaternionic line, and integral
H^8(X,Z) is torsion-free. The Euler class of the underlying oriented
real rank-eight bundle is c_4(V), hence also zero. On an eight-dimensional
CW base its unit sphere bundle has fibre S^7: there are no section
obstructions through the seven-skeleton, and the sole remaining
obstruction is this Euler class in H^8(X,Z). Thus V has a nowhere-zero
section. Its quaternionic span is a trivial quaternionic line and its
Hermitian orthogonal complement is a quaternionic line Q. Then
[V]=[Q]+[H], so [Q]=f_0+delta and c_2(Q)=u.
This is precisely the zero-Euler splitting used in Cadek--Crabb--Vanzura,
*Obstruction theory on 8-manifolds*, corrected 8 July 2008,
[Section 8 and proof of Corollary 8.4, pp. 11--13](https://www.math.muni.cz/~cadek/papers/8_manifolds.pdf#page=11);
see also Milnor--Stasheff, Theorem 12.5 for the Euler obstruction.
No cancellation at quaternionic rank one is assumed or needed.
We have therefore proved that the complete stable fibre of lines is
f_0+Tor KSp^0(X); different unstable lines may have the same stable class.

**Two independent torsion variations with the actual Gysin maps.**
Choose a point x in the first S and y in the second. Let
j_1:S -> X send s to (x,s), and j_2:S -> X send s to (s,y).
Their normal bundles are the corresponding oriented spin tangent
four-planes at x and y, trivial along the embedded S. Use the complex
orientation for these normal planes. Let b be the invertible Bott
class in KO^{-8}(pt), fixed compatibly with L084's convention.
For alpha,beta in Tor KO^0(S), define

\[
T_1(alpha)=b(j_1)_!alpha,\qquad
T_2(beta)=b(j_2)_!beta\quad\hbox{in }KO^{-4}(X).         \tag{9}
\]

Indeed each embedding pushforward raises degree by four; multiplication
by b lowers it by eight. These are torsion classes. In these degrees
the index in (1) is I_i=b^{-1}(p_i)_!, where the latter pushforward
lowers degree by four. The spin Thom projection formula and composition
give

\[
I_2T_1(alpha)=alpha,\quad I_1T_2(beta)=beta,\qquad
I_1T_1(alpha)=0,\quad I_2T_2(beta)=0.                  \tag{10}
\]

For clarity, the first identity cancels b and b^{-1} and integrates
the Thom extension over the same first-factor four-plane: p_2 j_1=id.
Its positive oriented local Thom class integrates to the unit. The
second identity uses the same convention in the second factor, with
p_1 j_2=id. This is local Thom excision followed by its inverse, not
an identification of a sphere-splitting summand with a Gysin map.
The spin structures compose to the identity structure since the
same oriented normal and vertical planes cancel.

For the cross term, p_1 j_1 is the constant map factoring as
q:S -> pt followed by i_x:pt -> S. Thus it is i_{x!}q_!(alpha).
The first map lands in KO^{-4}(pt)=Z, so it kills torsion alpha.
This proves the third identity; the fourth is the identical argument
with the factors exchanged. Product spin orientations are compatible
in both orders: exchanging oriented real four-planes contributes
(-1)^{4 times 4}=+1. In any event the cross term is already zero
integrally, not merely rationally. No complexification was used in
(9)--(10).

In particular T_1+T_2 injects (Z/2)^44 into Tor KSp^0(X), since
(I_2,I_1) is its left inverse. By (7) the groups have equal finite
order, so it is an isomorphism. Equations (9)--(10) describe all
stable torsion variations, with their actual two index changes.

**Extract the range and test the branches.** Given any pair
(v_G,v_H) in H^2(S,F_2)^2, choose alpha,beta by (6) with

\[
w_2(alpha)=v_G+w_2(R_G(f_0)),\qquad
w_2(beta)=v_H+w_2(R_H(f_0)).
\]

Take the quaternionic-line representative established above for
f=f_0+T_1(alpha)+T_2(beta). Then (10) gives
R_G(f)=R_G(f_0)-alpha and R_H(f)=R_H(f_0)-beta in KO. The virtual
Whitney formula with w_1=0 yields exactly (v_G,v_H). This proves
surjectivity onto the full codomain; the reverse inclusion is automatic,
so (2) is complete. It retains both orientation conventions and every
finite-rank lift; it neither selects one convenient f nor drops torsion.

L079's repeated determinant-trivial E_4 has real reduction the underlying
real E_4, hence w_2=0. Choosing v_G=0 and v_H=rho_2(k) attains that
recorded necessary pair; choosing any other v_H also works. More
generally (2) retains every w_2 pair arising from every L079 branch.
It is irrelevant to this conclusion whether the separately constructed
J_5 has that particular topology: all its possible w_2 values are
included. The real indices are virtual throughout this construction;
no statement that these Q have odd IT, compatible curvature or the
specified actual direct images follows. Higher or analytic compatibility
conditions are outside this test. The mod-two exclusion route stops.

### Separate critical audit — 2026-10-10

This is a REPRODUCTION proof audit under the prior SPECIALIZE assessment
`drafts/literature/2026-10-10-joint-spin-range-critical-audit.md`.
The complete range (2), not merely one compatible pair, is the threshold.
The general suspension, coefficient, Thom and section theorems cited
above are imported. Their specializations pass the following checks;
no substantive correction or stronger conclusion was found.

**Initial line and unchanged hypotheses.** L050's K3 topology gives
simple connectivity, spin, b_2=22, and torsion-free integral cohomology
in degrees zero, two and four. L071 applies its finite-rank theorem to
the changed sign and checks the full Steenrod condition. At the present
u its characteristic number is -48(9+10)/4+336/2=-60, divisible by
12. Thus f_0 exists independently of every image or holomorphic-kernel
assumption. L079 retains the entire mixed square 156P, all alternatives,
and the unchanged marked factors. Audited L084 fixes both negative
indices for the same coefficient, without complexification injectivity.

**Actual sphere restriction and all exact-sequence degrees.** Use the
mapping-cylinder cofiber of the wedge map W -> S. Van Kampen makes it
simply connected. Its integral homology exact sequence gives H_2(C)=0
by surjectivity of H_2(W) -> H_2(S) and H_3(C)=0 by injectivity of that
map. It gives H_4(C)=Z since H_4(W)=H_3(W)=0. The remaining reduced
homology groups vanish, including all degrees above four. Hatcher 4.32
successively gives pi_2(C)=pi_3(C)=0 and pi_4(C)=H_4(C)=Z. The map of
S^4 representing a generator is an integral homology isomorphism in
every degree; Corollary 4.33 therefore gives C homotopy equivalent to
S^4. Hatcher 4.37 ensures that the original W sphere maps evaluate on
the chosen basis, rather than on an unspecified additive splitting.

In reduced KO the terms adjacent to (5) are
KO^{-1}(W)=22 KO^{-3}(pt)=0 and KO^1(C)=KO^{-3}(pt)=0;
KO^0(C)=KO^{-4}(pt)=Z. Thus the actual restriction is onto and has
torsion-free kernel. The suspension computation independently gives
exactly 2^22 torsion elements in KO^0(S), so restriction on torsion is
bijective. The Hopf-plane class evaluates to one under w_2 on each
sphere. Integral H_2(S) is free and H_1(S)=0, so these evaluations
identify H^2(S,F_2) completely. Additivity of w_2 on these virtual
classes uses w_1=0, including virtual negatives. This verifies (6)
without treating a noncanonical wedge equivalence as a natural map.

**Character-kernel completeness and finite-rank sufficiency.** The stable
smash has respectively 1,44,486,44,1 spheres in dimensions 0,2,4,6,8:
the dimension-four number is 22^2+2, and dimension six has two sets of
22. The KO^{-4-d}(pt) coefficients are Z,0,Z,Z/2,Z. Thus there is no
additional free or torsion contribution to (7). The forgetful complex
character is nonzero on every free sphere generator, and rational
Chern character separates those generators; its kernel is precisely
the displayed torsion. Formula (8) therefore makes every line's stable
class a torsion translate of f_0, and no nontorsion translate can occur.

For the converse, let f=f_0+delta and write f+[H]=[A]-[H^m] using a
quaternionic complement for a representative negative bundle. Then A
has quaternionic rank m+2. At each rank k>=3 the section inequality
8<=4k-1 holds, so repeated splitting gives an actual rank-two V with
[V]=f+[H]. Its full rational character equals that of Q_0 plus H.
The Chern identities determine all rational Chern classes; the integral
Kunneth groups are torsion-free, so c_4(V)=0 integrally, not just its
characteristic number. The underlying real rank-eight bundle is
oriented; its S^7 section fibre is 6-connected. The first and only
possible obstruction on the eight-dimensional base is in H^8(X,Z),
with trivial local coefficients because the structure group preserves
orientation. It is its Euler class, equal to c_4(V), hence zero by
Milnor--Stasheff 12.5 and the cited CCV splitting argument. A section
and its quaternionic multiples trivialize one H-line; its orthogonal
complement is an actual H-line Q with [Q]=f and c_2(Q)=u. No rank-one
cancellation or uniqueness of unstable representatives is invoked.

**Both oriented pushforwards and the full torsion group.** For j_1 and
j_2 the normal plane has real rank four, so (j_i)_!alpha has KO degree
four and b(j_i)_!alpha has degree -4. For f of degree -4, (p_i)_!f
has degree -8, and b^{-1} puts its index in degree zero. In the same
factor compositions p_2 j_1=id and p_1 j_2=id, the oriented normal
plane cancels the oriented vertical plane. Local spin Thom integration
is the inverse of its extension and gives the unit; the two planes
use the same complex orientation and spin structure. The scalar b
commutes by the projection formula and cancels b^{-1}. This gives the
two diagonal identities in (10) with no factor of two. For a cross
composition the domain-to-point spin pushforward sends degree zero
to KO^{-4}(pt)=Z, hence is zero on torsion; the point embedding then
still gives zero. Exchanging the real four-planes has sign +1. These
are actual Thom compositions, not formulas inferred from sphere ranks.

Consequently (I_2,I_1) is a left inverse to T_1+T_2 on the complete
factor torsion group. Its order 2^44 agrees with the complete torsion
order in (7), so it is also onto that group. Each torsion variation is
represented by the line just constructed, and the virtual negative
index has the same additive w_2 variation as its positive index.
Thus every prescribed pair is realized by a line of exactly this u.
The check retains every L079 alternative and all possible J_5 values.
It does not show that the virtual indices are actual images, or that
these lines admit compatible connections, odd IT or holomorphic F.
ATTEMPTS/054 remains stopped; the universal Hodge gap is unchanged.

## Mathlib

Coverage of this full specialized joint-range theorem is **not checked**.
No matching declaration or absence from checked sources is asserted.
The directly cited suspension, KO coefficients, spin Thom and stable
rank/Euler results are the imported general inputs; their specialization,
including all finite-rank lifts and both Gysin maps, is the work above.
The result is a REPRODUCTION under the saved SPECIALIZE assessment,
not a claim of originality or of new Hodge-class algebraicity.
