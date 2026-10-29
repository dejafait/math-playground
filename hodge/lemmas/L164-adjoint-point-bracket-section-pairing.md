# L164 — Actual finite-point adjoint bracket and section-image pairing

## Hypotheses

Retain L071 and L116's conditional family, including L108/L109/L111/L115
as used there. The identical marked projective K3 factors S_1 and B
have their original common hyperkähler metric, real Kähler class h,
ordered triple and fixed holomorphic two-forms. The hypothetical locally
free rank-two F on X=S_1 x B is polystable for the real product class,
has integral c_1(F)=0 and

\[
 \operatorname{ch}(F)=2-14e_1-21e_2-\tau_D+62P,
 \qquad P=e_1e_2,
\]

with the full prescribed mixed tensor and L071's actual connection.
Set V=End_0(F), p:X -> B, C=Rp_*V, M=R^1p_*V, W=R^2p_*V.
Use L116's actual truncation arrows

\[
 M[-1]\xrightarrow{j}C\xrightarrow{a}W[-2],
 \qquad H=H^0(B,M),\quad t=\dim H.
\]

Thus M is locally free of rank 50, M=T_B direct sum N, N has the full
trivial summand O_B^t, and W has length one at each point of the finite,
possibly empty split set Z. At z in Z the actual fibre of F is
L direct sum L^{-1}, where c_1(L)^2=-14 and h.c_1(L)=0. Retain
L094's split coefficient spaces and L111's actual local complex and
trace pairing. No integrability of arbitrary elements of H, vanishing
of their brackets, multiplicative splitting of C, or existence of F
is assumed. Write M(z), W(z) for ordinary residue fibres, to distinguish
them from stalks and from derived fibres.

## Conclusion

Let j_1:H -> H^1(X,V) be induced by j and define the symmetric bilinear
map using the graded commutator convention
[alpha,beta]=alpha cup beta-(-1)^{deg(alpha)deg(beta)} beta cup alpha:

\[
 \beta(u,v)=H^2(a)[j_1u,j_1v]\in H^0(B,W).                 \tag{1}
\]

For each z in Z there are canonical maps

\[
 e_z:M(z)\hookrightarrow E_z:=H^1(S_1,V|_{S_1\times\{z\}}),
 \qquad
 \theta_z:W(z)\xrightarrow{\sim}
                  H^2(S_1,V|_{S_1\times\{z\}}),          \tag{2}
\]

where e_z is the degree-one derived pullback of j and theta_z is top
base change. Their dimensions are 50 -> 52 and 1 -> 1, respectively.
Writing rho_z(u)=e_z(u(z)), the actual projection satisfies

\[
                  \theta_z(\beta(u,v)(z))
                             =[\rho_z(u),\rho_z(v)].     \tag{3}
\]

There is an explicit nondegenerate symmetric form B_z on E_z that
tests this equality's right side. Write
E_z=U_+ direct sum U_-, U_+=H^1(L^2), U_-=H^1(L^{-2}), each of
dimension 26. With the fixed fibre form sigma set

\[
 P_z(x,y)=(2\pi i)^{-2}\int_{S_1}\sigma\wedge(x\smile y),
 \quad x\in U_+,\ y\in U_-,
\]
\[
 B_z((x,y),(x',y'))=P_z(x,y')+P_z(x',y).                 \tag{4}
\]

After pairing (3) with h_0=diag(1,-1), precisely

\[
 \frac{(2\pi i)^{-2}}2\int_{S_1}\sigma\wedge
       \operatorname{Tr}\bigl(h_0\theta_z(\beta(u,v)(z))\bigr)
                =B_z(\rho_z(u),\rho_z(v)).              \tag{5}
\]

Consequently beta vanishes on all Sym^2 H if and only if every actual
rho_z(H) is totally isotropic for B_z. The map rho_z is injective.
If Z is nonempty and t>26, beta is nonzero; this is a conditional
nonvanishing test, not a bound t<=26 for F. Brackets of global
first-order deformations have not been required to vanish.

The restriction of B_z to the full ordinary middle-fibre image e_z(M(z))
has rank at least 48, so a sheaf-level zero-bracket assertion cannot
replace the unknown section-image pairing. For t<=26 this calculation
does not decide isotropy of the actual image. For Z empty or t=0,
beta is zero for the stated vacuous reason.

This is a conditional comparison and an informative stopping result
(NEGATIVE / REPRODUCTION). The separate critical audit below preserves
it (EXPLORATION / REPRODUCTION), finding no substantive error or stronger
conclusion. It does
not construct a nonzero bracket for a realized F, prove or disprove F's
existence, exclude a split cardinality, or advance beyond the general
tools checked. It supplies no primitive Hodge realization or transport.

## Proof

**Imported tools and the precise specialization.** Reuse the prior
SPECIALIZE assessment
`drafts/literature/2026-10-25-adjoint-point-obstruction-projection.md`.
Import derived base change from
[Stacks Lemma 36.30.4, 0B91](https://stacks.math.columbia.edu/tag/0B91)
and cup compatibility with composition and base change from
[20.31.1/3, 0FKU](https://stacks.math.columbia.edu/tag/0FKU),
[20.31.7, 0FP6](https://stacks.math.columbia.edu/tag/0FP6), and
[20.31.8, 0H99](https://stacks.math.columbia.edu/tag/0H99).
Here p is smooth projective and hence proper, flat and finitely
presented; V is locally free and perfect. The actual coefficient
commutator is a morphism V tensor V -> V; extending it to Dolbeault
forms introduces exactly the displayed graded sign. The cup and
base-change theorems apply to this coefficient morphism. They give
functoriality, not ordinary middle base change or a Lie splitting.

The split quadratic obstruction's standard interpretation is also in
Arbarello--Sacca, *Singularities of moduli spaces of sheaves on K3
surfaces and Nakajima quiver varieties*, Advances in Mathematics 329
(2018), 649--703, DOI 10.1016/j.aim.2018.02.003,
[Proposition 6.1, pp. 680--681, with (5.5), p. 675](https://www.math.columbia.edu/~giulia/Quiver.pdf#page=32).
Its polarized algebraic moduli chart is not imported at the present
real h. L094 already supplies the necessary obstruction at this exact
real Kähler form, using Buchdahl--Schumacher, Complex Manifolds 9
(2022), 78--113, DOI 10.1515/coma-2021-0131,
[Lemma 2.5, Proposition 2.6 and Corollary 5.3/(5.1), pp. 83--84,92--93](https://d-nb.info/1262812674/34).
Only the cup comparison and its explicit matrix specialization below
are needed; no quadratic normal-form or unobstructedness theorem is
assumed or reproved.

**Actual ordinary-to-derived maps.** Fix z in Z and let R=O_{B,z},
k=R/m. L111 represents the actual C_R by the minimal finite free
complex in degrees 0,1,2

\[
 K=(R\longrightarrow R^{52}\longrightarrow R),
 \qquad d^0(1)=x a_0+y b_0,
\]

with x,y regular parameters. Its actual alternating trace form omega
has omega(a_0,b_0) a unit. It gives an orthogonal decomposition of
the middle term into P_R=Ra_0+Rb_0 and Q_R=P_R^{perp}, of ranks
2 and 50. The whole complex decomposes as Q_R[-1] plus the
two-parameter Koszul complex in degrees 0,1,2; that Koszul part has
only degree-two cohomology k. In particular M_R identifies with Q_R.

The inclusion Q_R[-1] -> K induces the identity of M_R in degree one
and represents the actual truncation inclusion j_R. Indeed, for the
projective module M_R, morphisms M_R[-1] -> K in the derived category
are Hom_R(M_R,H^1(K)); hence the identity specifies that morphism.
Tensoring this representative with k gives an injection Q_R/mQ_R
into K^1/mK^1. All residual differentials are zero by minimality.
Derived base change identifies the latter with E_z. This proves the
first assertion of (2), without asserting ordinary R^1 base change.

The top ordinary base-change map is an isomorphism: H^2(K)=k, while
H^2(K tensor k)=k and the map is reduction of the same last R term.
This proves the second assertion of (2). Equivalently, applying
Li_z^* to L116's actual triangle, M being locally free implies that
Li_z^*M[-1] has only degree-one cohomology. Thus H^2(Li_z^*a) is an
isomorphism from H^2(Li_z^*C) to H^2(Li_z^*(W[-2]))=W(z). Under
the preceding identification it is theta_z^{-1}. Lower Tor terms
of Li_z^*W are retained; they do not enter this top degree.

**Restriction of the projected global bracket.** The global restriction
H^1(X,V) -> H^1(S_1,V_z) is induced by the fibre square and adjunction.
Applied to j_1u it is rho_z(u): naturality of derived restriction with
j compares it to ordinary evaluation u -> u(z), since M is locally
free. Apply the same restriction in degree two to the commutator of
j_1u and j_1v. Cup compatibility gives their fibre commutator.
The square with the actual a commutes by functoriality of derived
pullback. Its bottom arrow in degree two is theta_z^{-1}, just
identified. On the W side the degree-two restriction of RΓ(W[-2])
is ordinary evaluation H^0(W) -> W(z). This proves (3).
It uses no choice of the global additive splitting in L116.

**The full polarized trace-free value.** L094 gives the split coefficient
decomposition and vanishing of the off-diagonal H^2 spaces. Its Serre
duality input (Huybrechts, *Lectures on K3 Surfaces*, Chapter 1,
Proposition 2.4 and (2.5)--(2.6)) makes P_z a perfect pairing between
U_+ and U_-. For Dolbeault degree-one representatives write

\[
 \xi=\begin{pmatrix}0&x\\y&0\end{pmatrix},\qquad
 \eta=\begin{pmatrix}0&x'\\y'&0\end{pmatrix}.
\]

Their graded commutator is xi wedge eta+eta wedge xi. Its upper
diagonal entry is x wedge y'+x' wedge y. Its lower diagonal entry
is y wedge x'+y' wedge x, which is the negative of the upper entry
by anticommutation of scalar one-forms with the dual line coefficients.
Both off-diagonal entries are zero. Thus it is trace-free and equals
h_0 times that upper entry. Since Tr(h_0^2)=2, pairing with h_0
and dividing by two gives exactly (4)--(5). For xi=eta the bracket
is twice the Yoneda square, as required by polarization. This
factor cannot be dropped if a numerical equality rather than just
vanishing is claimed.

Perfectness of P_z proves nondegeneracy of B_z: vanishing of
B_z((x,y),(0,y')) for every y' forces x=0, and then testing all
(x',0) forces y=0. The form is symmetric. In contrast, the alternating
trace form of L111 is
Omega_z(xi,eta)=P_z(x,y')-P_z(x',y). With A=ad(h_0), acting by
+2 and -2, one has Omega_z(Axi,eta)=2B_z(xi,eta). This checks the
stabilizer sign and distinguishes this obstruction from the scalar
alternating pairing. No positivity or arbitrary-matrix substitute is
being used.

**What is and is not decided on sections.** W is a sum of reduced
length-one point sheaves, so its global section is zero if and only
if all its residues at Z vanish. Equations (3)--(5) and the
one-dimensional target H^2(V_z)=H^2(O_{S_1})h_0 prove the claimed
equivalence with total isotropy of every rho_z(H).

L116 identifies H=H^0(N) with the sections of the full trivial
direct summand O_B^t; the complementary summand has no sections and
H^0(T_B)=0. Thus evaluation H -> M(z) is injective for every z.
Combining with (2), dim rho_z(H)=t. In a nondegenerate bilinear
space of dimension 52 a totally isotropic subspace T is contained
in T^{perp}, whose dimension is 52-dim T; therefore dim T<=26.
If t>26 and z exists, some pair u,v has nonzero (5), proving the
conditional nonvanishing assertion. This does not require every
diagonal bracket to be nonzero. Over C, polarization does imply
that a nonzero symmetric map has some nonzero diagonal value.

Similarly, the 50-dimensional subspace Q=e_z(M(z)) has a
two-dimensional B_z-orthogonal complement in E_z. Its restricted
radical is Q intersect Q^{perp}, of dimension at most two, so
rank(B_z|Q)>=48. In particular the relative bracket cannot vanish
on the entire ordinary middle fibre. This rules out a blanket
sheaf-level vanishing explanation for (1); it does not force the
actual smaller global section image to meet a nonzero pairing.

The threshold sought was beta=0 on the full H, or an evaluation
determining its failure in the actual family. The achieved result
is (3)--(5), the exact isotropy criterion, and conditional nonvanishing
for t>26 at a split point. Neither the actual t nor the section
pairings are determined here. L094's obstruction vanishes on its
two actual base tangent directions, by existence of that family;
it does not say that arbitrary global first-order deformations
integrate. L116's additive splitting likewise imposes no bracket
value. The approved stopping test is therefore met: park this
vanishing mechanism until an independent constraint controls these
specific section-evaluation pairings. Even their vanishing would
leave the other global obstruction component, existence of F,
transport and primitive Hodge realization open.

**Separate critical audit (2026-10-25, step 544).** The invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-25-adjoint-point-bracket-critical-audit.md`
covers exactly this verification. Its inspected primary cup/base-change
statements and real-Kahler qualifications are reused, not reproved.
The direct inputs remain L071, L094, L111 and L116. In particular
the local model and full trivial summand are conditional mathematical
inputs, not consequences of dimension counting alone.

First check the actual j, including its uniqueness. Locally the free
module M_R=Q_R is projective, so

\[
 \operatorname{Hom}_{D(R)}(M_R[-1],K)
       =\operatorname{Hom}_R(M_R,H^1(K)).
\]

This follows by computing Hom from the one-term projective complex:
Hom_R(M_R,-) is exact. The inclusion of Q_R in K^1 and the canonical
truncation map both induce the identity of H^1(K), so they represent
the same derived morphism. The decomposition used here is the one
obtained from L111's actual differential and trace form, with unit
omega(a_0,b_0); it is not inferred from residual dimensions. Reducing
the full complex, rather than its cohomology, gives zero differentials
and the injection of Q_R/mQ_R into k^52. This verifies e_z and its
dimension while retaining the two extra derived middle directions.

For the top arrow, cohomological shifts give
H^2(Li_z^*(W[-2]))=H^0(W derived-tensor k)=W(z).
The other terms of Li_z^*(W[-2]) are Tor_1 in degree one and Tor_2
in degree zero. They are not discarded. In the pulled-back triangle,
Li_z^*(M[-1]) has cohomology only in degree one; hence the neighboring
degree-two and degree-three terms from it are zero. The degree-two
map induced by a is therefore an isomorphism. The explicit last-term
reduction R -> k in K identifies its inverse with ordinary top base
change, fixing the direction of theta_z in (3).

Next check global restriction without choosing a splitting. A section
u is a class map O_B[-1] -> M[-1]; composing with j and pulling back
to z yields e_z(u(z)). A section w of W is similarly represented by
O_B[-2] -> W[-2]; its degree-two pulled-back class is w(z), regardless
of the lower Tor terms. Naturality with a and the imported cup
base-change theorem give exactly (3) for the bracket. The coefficient
operation is the commutator on End_0(F), defined through composition
in End(F), and the Dolbeault grading makes the degree-one bracket
symmetric. No product on a chosen additive decomposition of C is used.

The explicit sign check is
y wedge x'+y' wedge x=-(x' wedge y+x wedge y'). Thus the bracket
is h_0 times the upper diagonal entry, not the scalar alternating
trace pairing. Pairing with h_0 gives twice that entry, and the
factor 1/2 in (5) cancels it. On the diagonal xi=eta the upper entry
is 2x wedge y, so the bracket remains twice the Yoneda square. The
fixed nonzero sigma and normalization multiply the perfect Serre
pairing by a nonzero scalar. With H^2(V_z)=H^2(O)h_0 and
Tr(h_0^2)=2, the scalar test (5) detects the entire fibre obstruction.
These checks verify normalization as well as vanishing.

Finally, L116's actual decomposition N=O_B^t direct sum A with
H^0(A)=0, together with H^0(T_B)=0, identifies the full section space
with C^t. Evaluation into M(z) is injective at each point; it is not
merely generic evaluation. Therefore dim rho_z(H)=t. Perfectness of
P_z makes B_z nondegenerate in dimension 52, so T contained in its
orthogonal complement implies 2 dim T<=52. This proves precisely
the conditional threshold t>26. It does not assert isotropy when
t<=26 or nonexistence of F when the bracket is nonzero.

For Q=e_z(M(z)), dim Q=50 implies dim Q-perpendicular=2 and
rad(B_z restricted to Q)=Q intersect Q-perpendicular. Hence the
restricted rank is at least 50-2=48. To interpret this as a sheaf
test, compose j tensor j, the relative bracket, and a. Since M is
locally free, this is a morphism M tensor M -> W after shifting by
two; its residue is the bracket on Q under theta_z by the same
base-change square. Thus the rank test really rules out zero for
that whole sheaf pairing at a split point. It supplies no lower
dimension or rank for the pairing on the smaller section image.

Reduced length-one support of W makes testing all residues sufficient.
If Z is empty then W=0; if t=0 then the source Sym^2 H is zero.
Both vacuous cases survive. Unknown t and actual section pairings
remain the stopping point. The other global obstruction component
is not killed, and obstructed first-order deformations do not exclude
their central bundle. The audit changes no mathematical claim or
dependency and finds no stronger result; it is EXPLORATION /
REPRODUCTION, not a new advance beyond the assessed sources.

## Mathlib

Full matching Mathlib coverage for this actual relative adjoint-bracket
comparison has not been checked; no absence is claimed. The standard
derived cup/base-change and Serre inputs are precisely cited above.
The finite-dimensional pairing and dimension tests are written out,
not certified by a numerical experiment or formal proof assistant.
The separate critical audit above verifies this specialization informally;
it supplies no formal certification or additional Mathlib coverage.
