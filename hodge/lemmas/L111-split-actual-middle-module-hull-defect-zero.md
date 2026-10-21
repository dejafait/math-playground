# L111 — The actual split middle module has zero hull defect

## Hypotheses

Retain the entire conditional family of corrected L108 and audited
L109/L110. Thus p:S_1 x B -> B is the projection of the identical
marked projective K3 surfaces with the fixed common hyperkähler metric.
The hypothetical locally free rank-two F is polystable at the real
product polarization, has integral c_1(F)=0 and
ch_2(F)=-14e_1-21e_2-tau_D, and has L071's compatible connection.
The full tensor, its self-adjoint action and its eigenvalue
D[sigma]=2lambda[sigma], 1<lambda<5/4, are retained.

Set V=End_0(F), C=Rp_*V, M=R^1p_*V, W=R^2p_*V, E=M** and Q=E/M.
Use L108's perfectness, torsion-freeness, rank fifty and extended Serre
form; L109's actual cup/trace duality and dual-truncation maps; and
L110's actual first-order comparison and W_z of length one. The split
locus Z is finite, possibly empty. At z in Z the actual fibre is
E_0=L direct sum L^{-1}, with c_1(L)=k, k^2=-14 and h.k=0.
Use L094's split cohomology and stabilizer action and L095's all-fibre
harmonic/actual-curvature identities. No ordinary middle base change
at z, chain-level symplectic normal form, metric extension, semistability
of E or N, or bound on |Z| is assumed.

## Conclusion

For every z in Z, with R=O_{B,z}, one has

\[
 M_z\simeq R^{50},\qquad M_z\longrightarrow E_z=M_z^{**}
       \text{ is an isomorphism},\qquad q_z=0.             \tag{1}
\]

The isomorphism to a free module involves choices; the assertion about
the canonical hull inclusion does not. In particular M=E globally,
and for s=|Z| the conditional budget is

\[
 w=s,\quad q=0,\quad
 \operatorname{ch}(E)=50+(-824+s)\eta,\qquad
                  c_2(N)=(800-s)\eta.                    \tag{2}
\]

L109's actual map gamma:W_z^dagger -> W_z is consequently an
isomorphism. It is not set to zero or selected arbitrarily. For Z empty,
s=w=q=0. This is a local ADVANCE / REPRODUCTION under the prior
SPECIALIZE assessment. The separate critical audit below preserves the
result, with outcome EXPLORATION / REPRODUCTION: it finds no substantive
error or stronger conclusion. It sharpens
the conditional defect budget but supplies no cardinality bound,
extension of the chosen metric, semistability, F, cycle or transport.
Universal primitive rational Hodge realization remains unresolved.

## Proof

**Imported tools and exact scope.** Reuse the unchanged prior assessment
`drafts/literature/2026-10-16-split-hull-defect-from-actual-first-order-complex.md`.
Import minimal finite free representatives and their ranks from
[Stacks Lemmas 15.77.6--7, 0BCC](https://stacks.math.columbia.edu/tag/0BCC)
and [0BCD](https://stacks.math.columbia.edu/tag/0BCD). Import realization
of derived morphisms out of bounded-above projective complexes by chain
maps from [Lemma 13.19.8, 064B](https://stacks.math.columbia.edu/tag/064B).
The tensor/Hom differential and graded interchange conventions are
[Sections 15.59, 0GWN](https://stacks.math.columbia.edu/tag/0GWN) and
[15.73, 0A8H](https://stacks.math.columbia.edu/tag/0A8H).
Import regularity of minimal parameters from
[Lemma 10.106.3, 00NQ](https://stacks.math.columbia.edu/tag/00NQ) and
exactness of the positive-degree Koszul complex of a regular sequence
from [Lemma 15.31.2, 062D](https://stacks.math.columbia.edu/tag/062D).

Here R is a regular local C-algebra of dimension two, C_R is perfect,
and its minimal representative K has ranks (1,52,1) in degrees 0,1,2,
by L110. Thus K and K tensor K are bounded finite free complexes, in
the scope of 064B. The pairing is the actual perfect pushforward trace
pairing of L109, which specializes
[Remark 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81) and
[48.12.7, 0E4L](https://stacks.math.columbia.edu/tag/0E4L).
The general theorems are imported, not reproved. What follows selects
the actual incoming linear coefficients and performs the elementary
local-module specialization; it does not assert a general monad or
formality theorem for this coefficient family.

**A strict representative of the actual pairing.** Write

\[
 K:\quad R\xrightarrow{d^0}H\xrightarrow{d^1}R,
 \qquad H=R^{52},\qquad d^i\equiv0\pmod{\mathfrak m}.    \tag{3}
\]

The normalized actual pairing of L109 is a derived map
K tensor K -> R[-2], whose adjoint is the isomorphism
K[2] -> RHom_R(K,R). It is symmetric with respect to graded
interchange: the coefficient form tr(ab)=tr(ba) is symmetric, and
interchanging cohomological factors in cup product has the Koszul
sign. Equivalently, its Dolbeault trace satisfies
tr(a wedge b)=(-1)^{ij}tr(b wedge a) in degrees i,j.
This is symmetry of the actual derived class, not a choice of an
unrelated self-duality.

By 064B choose a chain representative B. If tau is graded interchange,
replace B by (B+B composed with tau)/2. This remains a chain map,
represents the same derived class and is strictly graded symmetric;
division by two is available over R. In total degree two its components
are therefore an endpoint scalar s_0=B(1,e_2)=B(e_2,1) and an
alternating form omega on H. Its adjoint still represents the same
isomorphism. After derived tensor with the residue field, (3) has zero
differentials, so that adjoint is a degreewise isomorphism of vector
spaces. Consequently s_0 is a unit and omega has invertible matrix
over R (their determinants have nonzero residues).
This justifies strict symmetry and nondegeneracy on this actual
representative, without a strictification theorem for other structures.

Put v=d^0(1). The chain-map equation applied to 1 tensor b in
total degree one gives, for every b in H,

\[
                 \omega(v,b)+s_0 d^1(b)=0.              \tag{4}
\]

The residual alternating form omega_bar on the residue space of H is exactly
the normalized split-fibre Serre form

\[
 \Omega_z(a,b)=(2\pi i)^{-2}
      \int_{S_1}\sigma\wedge\operatorname{Tr}(a\wedge b)
                                                        \tag{5}
\]

on H^1(V_0), under natural derived base change. Indeed reduction is
functorial for the same cup/trace map, and homotopic representatives
of a map on the zero-differential residual complex induce the same
degreewise bilinear maps. Normalize the generator of K^0 so its
residue is h_0=diag(1,-1). Endpoint rescaling causes no problem in (4).

**Incoming first variation and the split KS pairing.** Choose regular
parameters x,y of R and let u_1,u_2 be the dual tangent basis. Under
the natural identification of the residue space of H with H^1(V_0),
write the linear column as

\[
      v\equiv x v_1+y v_2\pmod{\mathfrak m^2 H}.       \tag{6}
\]

The same actual coefficient-sequence comparison as in L110, now in
degrees zero to one, identifies v_i with the connecting map on h_0.
More explicitly pull back by x,y -> epsilon times u_i(x),u_i(y).
The induced coefficient differential on endomorphism-valued j-forms
is bar-partial+epsilon[a_i,-], with a_i representing the actual KS
class a_i=kappa_z(u_i). On a degree-zero h_0 its connecting class is
[a_i,h_0]. The zero differential of the residual complex identifies
this with the linearized d^0. Naturality is precisely the actual
derived-base-change/coefficient triangle used in L110; simplicity
and ordinary R^1 base change are not required. Thus

\[
                     v_i=-A a_i,\qquad A=\operatorname{ad}_{h_0}.
                                                        \tag{7}
\]

We need more than KS injectivity: its two-plane must have nonzero
pairing (5). Here that follows from the actual connection at z.
L095 makes r_u^{0,1} a harmonic representative of the actual KS
class, including at a split fibre; the actual-family comparison in
L094/L110 fixes the complex tangent convention. In local holomorphic
base coordinates let a_i denote these representatives for partial_i.
The mixed curvature with base type (1,0) and fibre type (0,1) is
sum_i dz_i wedge a_i. The coefficient of dz_i wedge dz_j in
Tr(R_curv wedge R_curv), with fibre type (0,2), is

\[
 -\operatorname{Tr}(a_i\wedge a_j)
       +\operatorname{Tr}(a_j\wedge a_i)
                   =-2\operatorname{Tr}(a_i\wedge a_j).
\]

Both pure curvature blocks have total type (1,1) and cannot supply
this base-(2,0), fibre-(0,2) term. An exact horizontal gauge
correction changes no trace integral. The ordered factor two cancels
the factorial in ch_2. This is the calculation in L108 (4)--(5),
applied directly to the actual family at z; it uses no stable coarse
space and no ordinary split-point base change. L095's all-fibre
actual-form identity therefore gives

\[
 \Omega_z(\kappa_z(u),\kappa_z(w))
 =-p_*\left(
   \frac{\operatorname{Tr}(R_{\rm curv}\wedge R_{\rm curv})}
                  {2(2\pi i)^2}\wedge p_1^*\sigma\right)(u,w)
                    =2\lambda\sigma_B(u,w).             \tag{8}
\]

The last identity holds on all of B by L095, rather than being an
inference from cohomology on a puncture. Since sigma_B is nowhere
zero and lambda is nonzero, (8) is nondegenerate at z.

L094's splitting H^1(V_0)=H^1(L^2) direct sum H^1(L^{-2}) has
weights +2,-2 for A, with no diagonal degree-one sector. Thus A^2=4.
Invariance of matrix trace under h_0 gives
Omega_z(Aa,b)+Omega_z(a,Ab)=0. Combining this with (7)--(8) yields

\[
 \Omega_z(v_1,v_2)=\Omega_z(Aa_1,Aa_2)
       =-4\Omega_z(a_1,a_2)
       =-8\lambda\sigma_B(u_1,u_2)\ne0.                 \tag{9}
\]

This is the extra actual-family datum absent from L109's duality-only
models. L094's quadratic obstruction vanishing concerns the bracket
of tangent classes; it does not set their alternating Serre pairing
in (8) to zero, nor the pairing in (9).

**The actual middle module.** Since x,y generate the maximal ideal
and v has entries in that ideal, choose a,b in H with v=x a+y b. Their residues are
v_1,v_2 by (6). Thus c_0=omega(a,b) is a unit by (9). The plane
P=Ra+Rb is free and nondegenerate, and

\[
                   H=P\oplus P^{\perp_\omega}.          \tag{10}
\]

For clarity the projection to P is the actual R-linear map
f -> omega(f,b)a/c_0-omega(f,a)b/c_0. It fixes a,b and has
orthogonal kernel, proving (10) without a formal change of base.
The complement is a finite projective module over the local ring R,
hence free of rank fifty. Because v is in P, (4) makes d^1 vanish
on this complement, and d^0 has no component in it. On P, the two
differentials in the ordered basis a,b are exactly

\[
      r\longmapsto(xr,yr),\qquad
      (alpha,beta)\longmapsto
          (c_0/s_0)(y\,alpha-x\,beta).                 \tag{11}
\]

The unit c_0/s_0 does not change its kernel or cokernel. Since x,y
are regular parameters, the imported two-parameter Koszul exactness
says the kernel of the last row of (11) is R(x,y), exactly the
image of its first column. The P part therefore has zero middle
cohomology and last cohomology R/(x,y), while the orthogonal
complement is concentrated in degree one. In particular

\[
              \ker(d^1)/\operatorname{im}(d^0)
                     \simeq P^{\perp_\omega}\simeq R^{50}.
                                                        \tag{12}
\]

All decompositions above are of the actual free complex with the
actual cup/trace pairing; no unrelated local model has replaced it.
The full higher coefficients are retained in a,b and omega. Exact
Koszulness concerns their regular-parameter coefficients in (11),
so no neglect of higher terms, convergence assertion or completion
is involved. The middle module (12) is free, making its canonical
map to its double dual an isomorphism. This proves (1).

**Budget and limits.** M already equals its hull outside Z by L108;
(1) gives the same at every split stalk, so Q=0 globally. L110 gives
w=s. Substituting into the corrected L108 budget gives (2), with
the retained negative sign of both possible defects. Exactness of
L109's 0 -> Q_z -> W_z^dagger -> W_z -> Q_z^dagger -> 0 then
makes its actual gamma an isomorphism; this is a consequence rather
than an assumed transgression value.

The rank fifty of M_z does not give ordinary base change: its
residue-field dimension fifty differs from derived H^1 of dimension
fifty-two. The Koszul summand accounts for the extra derived classes.
Local freeness and the extended algebraic symplectic form do not
extend the chosen stable-open L2 metric or prove semistability.
Nothing bounds s or constructs F. Thus the independent metric,
cardinality, existence and transport gaps survive the exact local
defect computation. The historical stops ATTEMPTS/063/065/066/067
are preserved; the last one excludes only a duality-only bound.

**Separate critical audit, 2026-10-16.** This audit uses the unchanged
prior SPECIALIZE assessment
`drafts/literature/2026-10-16-split-actual-middle-module-critical-audit.md`.
It reuses its inspected primary statements; it does not reprove the
general derived-category, duality or Koszul theorems. The following
checks concern the actual family and the exact local calculation.

First, coefficient trace is symmetric on the degree-zero locally free
V, and the derived cup product is compatible with the symmetric tensor
interchange. Hence the actual derived pairing is fixed by tau. For a
bounded finite free K, its tensor square is also bounded finite free,
so 064B applies to this pairing itself. If B is any representative,
B composed with tau represents the same morphism. Their average still
represents its perfect adjoint. Reducing that adjoint modulo the maximal
ideal is a derived isomorphism; both residual complexes have zero
differentials by minimality. Its endpoint components and middle
component are therefore isomorphisms individually. Nakayama, or the
unit determinant criterion, gives a unit s_0 and an invertible omega
over R. Thus neither averaging nor passage to the residue field loses
perfectness. On 1 tensor b the tensor differential has the terms
v tensor b and 1 tensor d^1(b), with a plus sign. Since the target
has zero degree-one term, their pairing is zero, exactly (4).
Reduction of this same map gives (5), not an arbitrary alternating
form with the same dimension.

Second, L110's audited Cech comparison works in degree zero as well
as degree one. Tensoring its bounded flat coefficient complex and K
with the dual numbers and the residue field gives the same diagram
of short exact sequences, with multiplication by epsilon on the left
and reduction on the right. Its residue identifications are fixed,
independent of u. Lifting h_0 and applying the perturbed Dolbeault
differential gives epsilon(a h_0-h_0 a); division by epsilon gives
[a,h_0]=-A a. Changing the smooth splitting changes this by a
Dolbeault coboundary. Changing the lift of h_0 in K changes no linear
coefficient because both differentials are minimal. This verifies
(6)--(7) for the actual d^0, rather than transposing an unrelated row.

The real/complex normalization is also fixed: for a real base tangent
t, put u=(t-iIt)/2. L094/L095 give r_{It}^{0,1}=i r_t^{0,1}, so
r_u^{0,1}=r_t^{0,1}. The Dolbeault derivative differs from this by
bar-partial of the horizontal connection coefficient. Thus the a_i
in the actual mixed curvature represent precisely kappa_z(u_i),
with no factor two or conjugation. At a split point total integrability
still makes curvature of type (1,1). The two pure blocks have types
(1,1) on their respective factors, so neither they nor their product
contribute base type (2,0), fibre type (0,2). The two mixed products
give -Tr(a_1 wedge a_2)+Tr(a_2 wedge a_1)=-2 Tr(a_1 wedge a_2).
Both moving the fibre one-form past the base one-form and odd trace
cyclicity are retained. Multiplication by the fibre two-form gives no
additional sign. A Dolbeault coboundary in either a_i integrates to
zero because the other class and sigma are closed and S_1 is compact.
Consequently the factor 2 cancels the Chern-character factorial and
the normalized Serre form is minus L095's actual curvature integral.
That integral equals -2lambda sigma_B on all of B. This proves (8)
at the split point without extending a coarse form from the stable
open. It supplies nondegeneracy, a stronger premise than injectivity.

Third, A preserves trace infinitesimally: for degree-one a,b,
Tr([h_0,a] wedge b+a wedge [h_0,b])=Tr([h_0,a wedge b])=0.
There is no extra odd sign here because h_0 has degree zero. Since
H^1(O)=0, all of H^1(V_0) has weights +2 or -2, so A^2=4 on the
entire space used. Thus
Omega(Aa_1,Aa_2)=-Omega(a_1,A^2a_2)=-4 Omega(a_1,a_2).
The two minus signs in v_i=-Aa_i cancel. Equation (9) has nonzero
value -8lambda sigma_B(u_1,u_2). L094's quadratic bracket condition
uses the stabilizer-valued obstruction pairing; it does not assert
that this scalar alternating pairing vanishes.

Fourth, the full column v belongs to mH, and m=(x,y); hence
v=xa+yb in the algebraic stalk itself. Modulo m^2 the independence of
x,y in m/m^2 fixes the residues a_bar=v_1 and b_bar=v_2. Their
pairing c_0 is a unit. Pairing a relation alpha a+beta b=0 with
b and a proves alpha=beta=0. The displayed projection in (10)
fixes a,b; subtracting it from any f gives zero pairing with both.
Its kernel is therefore P-perpendicular and H is the stated direct
sum. The complement is free of rank 52-2=50, since a finite projective
module over a local ring is free. In that direct sum the full column
is (x,y,0) and (4) gives the row
(c_0 y/s_0,-c_0 x/s_0,0). No higher coefficient is dropped.
The maximal ideal has a minimal two-element generating set in the
regular local ring of dimension two. Thus 00NQ and 062D apply to x,y;
their Koszul exactness gives precisely (12), not just its completion
or an associated graded calculation. All remaining cohomology of
the plane is R/m in degree two. The canonical evaluation map from
the free middle module to its double dual is an isomorphism, so the
actual Q_z vanishes independently of the chosen basis or projection.

Finally, L108 already gives local freeness on U, so these stalk checks
give Q=0 on B. L110's independent length-one result gives w=|Z|;
the same length is also visible in (11). L109's actual exact sequence
then has zero outer modules, forcing its specified gamma to be an
isomorphism, without identifying arbitrary length-one maps. In K-theory
[C]=-[M]+[W], and now M=E. Thus ch(E)=50+(-824+|Z|)eta;
subtracting ch(T_B)=2-24eta gives
ch(N)=48+(-800+|Z|)eta and c_2(N)=(800-|Z|)eta. These signs agree
with corrected L108. The rank-fifty ordinary fibre still differs from
the rank-fifty-two derived middle cohomology at z; the residual Koszul
complex explains the difference. For Z empty all local checks are
vacuous and the same global formulas hold with zero defects.

The audit finds no error requiring an argument or dependency change.
The achieved local defect is zero, exactly the required threshold for
this intermediate target. This verifies an existing specialization of
known tools, not a new theorem beyond the inspected literature or a
Hodge resolution. The chosen stable-open metric, its curvature,
semistability, a bound on |Z|, F existence and transport remain outside
the conclusion; the historical stops remain intact.

## Mathlib

Full matching coverage of this actual-family result, its derived trace
representative and its split KS comparison has not been checked.
The supporting imported results are the precise Stacks statements
cited above and the canonical actual-family results specified here.
No absence claim or formal verification claim is made. The local
module and pairing calculation is an informal proof preserved by the
separate critical audit above; it is not numerical evidence or a complete
candidate
for the Hodge conjecture.
