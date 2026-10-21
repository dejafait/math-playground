# L019 — Ordinary first-height radical with a compatible divisible Sha tower

## Hypotheses

Use the formal model of L013, with p >= 5, Lambda = Z_p[[T]],
F = Q_p, D = F/Z_p, and t = T/(1+T/2). Its ordinary complex is

\[
C_f=[\Lambda e_1\oplus\Lambda e_2
\xrightarrow{t\,\mathrm{id}}\Lambda e_1^\vee\oplus\Lambda e_2^\vee]
\tag{1}
\]

in degrees one and two. Retain its inverse-parameter self-duality,
local-condition triangles and maps, and marked rational lattice
M = Z e_1. At augmentation put S = F e_1 + F e_2,
W = F e_1, A = S/W and q:S -> A. These markings are formal;
no Galois-cohomological or elliptic-curve realization is assumed.

Use the known first-height construction, Bockstein followed by duality
and evaluation, in Buyukboduk, *Height pairings, exceptional zeros
and Rubin's formula: the multiplicative group*, Section 2.1.3,
[printed pp. 80--81](https://ems.press/content/serial-article-files/43278#page=10).
For its relationship with full-Selmer heights use
Macias Castillo--Sano, *On Selmer complexes, Stark systems and derived
p-adic heights*, arXiv:2603.23978v1,
[Section 4.1, Theorem 4.2](https://arxiv.org/html/2603.23978v1#S4.SS1),
and the first-radical description in Howard, *Derived p-adic heights
and p-adic L-functions*, arXiv:1202.6343v1,
[Theorem 4.2 and Corollary 4.3](https://arxiv.org/pdf/1202.6343v1#page=16).
These are supporting construction/comparison results, not arithmetic
realization theorems for (1). The exact formal specialization has ready
coverage in [the prior assessment](../drafts/literature/2026-10-04-cyclotomic-selmer-height-radical.md).

## Conclusion

The first ordinary Bockstein is

\[
\beta_f(x_1e_1+x_2e_2)
 =(x_1e_1^\vee+x_2e_2^\vee)\otimes\bar t.
\tag{2}
\]

With the evaluation duality in (1), its height is

\[
h_f(x,y)=(x_1y_1+x_2y_2)\bar t.
\tag{3}
\]

A common sign or a nonzero rescaling of the augmentation generator
does not change the conclusion

\[
\operatorname{rad}(h_f)=0,\qquad
q(\operatorname{rad}(h_f))=0\ne A\simeq F.
\tag{4}
\]

This same model admits a coefficient tower with all the following
properties, matching the tower shape in L018 for marked rank one:
S_m = (Z/p^m Z)^2, S_infinity = D^2, natural coefficient inclusions,
downward maps corresponding to multiplication by p on D^2, and
compatible lifts of every prescribed depth-two basis. Its marked
rational and Sha sequences are exact at every depth and in the
inverse limit. The full marked Sha is D with zero Cassels--Tate
pairing, and its Tate module is Z_p. Adding this tower changes none
of L013's local triangles, duality, determinant descent or scalar data.

Thus tower compatibility and the divisible Cassels--Tate radical do
not imply first-height radical surjectivity in this formal package.
The actual arithmetic assertion under L018's hypotheses remains open
here. This is not a BSD counterexample, nor a claim that the formal
model realizes the full arithmetic hypotheses or a Kurihara family.

## Proof

**Ordinary versus relaxed Bockstein.** Work first over
Lambda/(t^2). Lift x in S to the constant vector with coordinates
x_1,x_2 after tensoring with F. Its differential is t(x_1,x_2).
Divide by t and reduce modulo t. The resulting class in
H^2(C_f at t = 0) = S^dual is (2). Equivalently it is the connecting
map for the first-order coefficient extension. Since t = T + O(T^2),
this is also the coefficient using the original cyclotomic generator
modulo T^2. The self-duality of L013 identifies the degree-two
coordinates with e_1^vee,e_2^vee by evaluation, giving (3).
If x is in the left radical, take y = e_1 and y = e_2 to obtain
x_1 = x_2 = 0. The right radical is the same. This proves (4).

The relaxed global complex in L013 instead has differential
(0,t):Lambda^2 -> Lambda f, so its first Bockstein is
(x_1,x_2) |-> x_2 f tensor bar t. Its kernel is W.
Under the ordinary-to-relaxed map, degree one is the identity
and degree two is projection onto the second coordinate. Hence
this relaxed Bockstein is exactly the projection of (2), consistent
with the triangle. Its kernel cannot be substituted for the first
ordinary height radical. The first-order liftable subspace of the
ordinary complex is zero: t x = 0 modulo t^2 forces the augmentation
of x to be zero. This also checks the first derived-filtration radical
description directly for this model.

**Integral coefficient tower.** Specialize the integral free complex
(1) at t = 0 and then reduce modulo p^m. These are derived
specializations computed by the free terms; the differential is zero.
Thus its H^1 is S_m = R_m e_1 + R_m e_2, with R_m = Z/p^m Z.
Define the downward map rho_m:S_(m+1) -> S_m by coordinate reduction,
and the upward coefficient inclusion iota_m:S_m -> S_(m+1) by
v |-> p v. Multiplication by p here is well-defined on residue
coordinates and injective for the upward map.

For v in R_m^2, set

\[
j_m(v)=p^{-m}\widetilde v\pmod{Z_p^2}\quad\text{in }D^2,
\tag{5}
\]

using any integral lift. Changing the lift changes (5) by an integral
vector. This is an isomorphism onto D^2[p^m]. Direct computation gives

\[
j_m\rho_m=pj_{m+1},\qquad j_{m+1}\iota_m=j_m.
\tag{6}
\]

For the first equality the two sides differ only by the integral
vector caused by reducing a lift modulo p^m. The second is literal
equality modulo Z_p^2. The union of all these torsion subgroups is
D^2, so their direct limit is the marked S_infinity. Their downward
inverse limit is Z_p^2. This is the same distinction between upward
inclusion and downward coefficient maps used in L018; it introduces
no implicit inverse-limit exactness or higher prime eligibility.

**Marked Kummer and Sha sequences.** Put W_m = R_m e_1 and
A_m = R_m e_2. The inclusion of the first coordinate and projection
onto the second give split exact sequences

\[
0\longrightarrow M/p^m M\longrightarrow S_m
\longrightarrow A_m\longrightarrow0.
\tag{7}
\]

They commute with both coefficient maps. Under (5), the direct-limit
sequence is 0 -> D e_1 -> D^2 -> D e_2 -> 0. Mark its quotient
D e_2 as Sha_formal. Its p^m-torsion is A_m via (5), and the
downward quotient map corresponds to multiplication by p, exactly
as in (6). Taking compatible coordinates in (7) proves directly

\[
0\longrightarrow Z_p e_1\longrightarrow Z_p^2
\longrightarrow T_p\Sha_{\rm formal}=Z_p e_2
\longrightarrow0.
\tag{8}
\]

Tensoring (8) with F recovers q:S -> A. In particular Sha is a
marked quotient, not an implicitly canonically embedded arithmetic
subspace. The coordinate splitting belongs only to this example.

Give Sha_formal the zero Cassels--Tate pairing, with its restrictions
to all p^m-torsion subgroups also zero. Its entire group is divisible,
so its finite quotient modulo the divisible part is zero and its
pairing kernel is exactly that divisible part. This is compatible with
the property used in L018, supported by Milne, *Elliptic Curves*,
second edition (2021), [Theorem IV.5.4 and Remark 5.2, printed p. 130](https://www.jmilne.org/math/Books/EC2.pdf#page=135).
Nondegeneracy on the finite quotient is vacuous, and nondegeneracy of
the restrictions to Sha[p^m] is not asserted. No comparison identifying
this pairing with the ordinary height (3) is part of these data.

**Keep any prescribed depth-two basis.** Let c_1,c_2 be any R_2-basis
of S_2 and B_2 the matrix of its columns. Lift its entries to B over
Z_p. Its determinant is a unit because its reduction modulo p is
invertible. Then the columns of B modulo p^m are bases of S_m for
all m, reduce to c_i at depth two, and are compatible under rho_m.
This verifies the chosen-basis tower condition, rather than merely
matching the individual group orders. The whole tower is generated
by coefficient specialization of the same integral ordinary complex;
the original integral local maps and homotopies of L013 are therefore
unchanged and specialize compatibly.

All required formal compatibility checks pass while (4) fails the
surjectivity threshold. The ordinary height restricted to W is even
nondegenerate, since h_f(e_1,e_1) = bar t. The achieved marked rank
remains one, short of the required r >= 2. An arithmetic argument must
use an additional property not realized by this marked complex,
such as control of the actual determinant's rational exterior-square
membership; structural tower data and the pairing kernel alone do
not supply it. No such property is proved or assumed here.

This is a REPRODUCTION by specializing the assessed Bockstein-height
construction in the existing model, not progress beyond the checked
literature. Its local value is a precise negative test of the proposed
formal implication. The matrix identities are checked by
`python3 scripts/cyclotomic-determinant/check_model.py`; the argument
above proves tower compatibility for every coefficient depth.

## Mathlib

Full coverage of this marked height/tower compatibility statement:
**not checked**. Supporting Bocksteins, Selmer-complex duality,
coefficient limits, matrix lifting and divisible pairing kernels:
**not checked**. Howard Theorem 4.2/Corollary 4.3 and
Macias Castillo--Sano Theorem 4.2 support the first-height construction
and radical interpretation; Milne Theorem IV.5.4 supports the
divisible Cassels--Tate kernel. None is a full matching theorem for
the proposed arithmetic radical-surjection claim or a Mathlib match.
