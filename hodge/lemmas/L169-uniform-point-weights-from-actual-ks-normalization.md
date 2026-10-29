# L169 — Uniform point weights from the actual KS normalization

## Hypotheses

Retain the entire conditional family and all fixed choices of L168,
including L111's actual incoming Kodaira–Spencer comparison. Thus
X=S_1 x B is the product of identical marked projective K3 surfaces
with their fixed common metric, ordered hyperkähler triple, forms
sigma_1,sigma_B and actual connection. The hypothetical locally free
rank-two product-polystable F has integral c_1=0 and full character
2-14e_1-21e_2-tau_D+62P, with P=e_1e_2. Set V=End_0(F),
p:X -> B, C=Rp_*V and W=R^2p_*V. Its reduced finite split set Z
may be empty.
Retain the actual maps alpha,j,a,r,gamma, the derived top base-change
maps theta_z and the fixed split generators h_0=diag(1,-1).

Use L168's complex bilinear quotient form Q_U on U=H^0(B,W), its
bracket coordinate ell_z, n_z=ell_z^{-1}(1), and its nonzero weights
mu_z=ev_z(gamma_z^{-1}n_z,n_z). Keep the single common nonzero
relative trace scalar kappa of L168 (10), relative to the fibre
integral (2 pi i)^{-2} integral sigma_1 wedge Tr. Here kappa is a
scalar, not the Kodaira–Spencer map. Retain L111's eigenvalue
D[sigma]=2 lambda[sigma], with 1<lambda<5/4.

The fixed base Serre trace is used at every point. More precisely,
let f:B -> Spec C and let chi_B:O_B[2] -> f^!C be the dualizing
isomorphism defining that trace. Write nu_B:omega_B[2] -> f^!C
for Verdier's isomorphism in the source convention specified below.
Define delta_B by

\[
 chi_B=delta_B\,nu_B\circ m_{sigma_B},                    \tag{1}
\]

where m_{sigma_B}:O_B[2] -> omega_B[2] is multiplication by the
fixed form. The proof shows that delta_B is one nonzero complex
constant, rather than separately chosen point normalizations.

No F existence, actual section values, integrability, genericity,
quartic square length, endpoint s=800,t=48 or numerical value of
delta_B is assumed.

## Conclusion

For every z in Z, the actual weights in L168's fixed coordinates are

\[
             \boxed{\displaystyle
             mu_z=\frac{delta_B\,kappa}{2\lambda}.}       \tag{2}
\]

In particular they are independent of z and nonzero. For the
Verdier-normalized base trace delta_B=1; no identification of the
notebook's fixed trace with that numerical convention is required.
Consequently L168's actual bracket formula becomes

\[
 Q_U(\beta(h,h),\beta(h,h))
 =\frac{delta_B\,kappa}{2\lambda}
       \sum_{z\in Z}B_z(\rho_z(h),\rho_z(h))^2.           \tag{3}
\]

Empty Z gives an empty sum on U=0. Singleton Z requires no
between-point comparison and satisfies the same formula.

This is a conditional ADVANCE / REPRODUCTION of the assessed
residue theorem and the two canonical actual-family formulas. It
removes independent point coefficients in these fixed coordinates;
it does not compute the quadrics in (3), their minimum square length,
the complementary operation, a cardinality exclusion, F, transport or
primitive Hodge realization. The separate critical audit below preserves
the result (EXPLORATION / REPRODUCTION), with no substantive correction
or stronger conclusion.

## Proof

**Imported inputs and applicability.** Reuse the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-26-point-weight-uniformity.md`.
Import the oriented fundamental local isomorphism and its passage
to local cohomology from S. Nayak and P. Sastry, *Grothendieck
Duality and Transitivity I: Formal Schemes*, author PDF dated
2019-05-29, C.1–C.2, especially (C.2.4)–(C.2.7), and Lemma C.5.4,
pp. 55–58, 63–64; finite-trace compatibility is Theorem 5.3.8 and
Proposition 5.4.4, pp. 14–17
([primary PDF](https://www.cmi.ac.in/~pramath/mypapers/fub1.pdf)).
Import regular-section residue normalization from the same authors,
*Grothendieck Duality and Transitivity II: Traces and Residues via
Verdier's Isomorphism*, author PDF dated 2019-05-29, Remark 5.3.3
and Theorem 5.4.2, pp. 26–27; use (4.1.2),(4.1.5), pp. 21–22,
for its agreement with the abstract and proper global traces
([primary PDF](https://www.cmi.ac.in/~pramath/mypapers/fub2.pdf)).

Here B is smooth projective over C of dimension two and z is a
reduced C-rational point. Its regular local ring R has a regular
parameter sequence x,y generating its maximal ideal. Shrink to a
smooth affine neighbourhood on which their common zero is just z
and dx wedge dy trivializes omega_B. The closed point is a section
of the structural map to Spec C, hence is finite flat over that
base, as required in the cited residue comparison. It need not be
flat over B. Support/open compatibility lets this local calculation
compute the closed-point contribution to the fixed global trace;
the composite-counit identification is already retained in L168.
No general residue or duality theorem is reproved. The calculation
below is necessary because the sources do not compare L111's c_0
with L168's resolution-defined generator.

**One global comparison scalar.** Both chi_B and nu_B are global
dualizing isomorphisms for the same structural map. Their ratio,
after multiplication by sigma_B, is an automorphism of O_B[2].
Such an automorphism is multiplication by a global invertible
regular function on B. A holomorphic function on the compact
connected K3 surface is constant. Thus (1) defines one
delta_B in C^times. Applying the closed-point upper-shriek functor
and the counit shows that the finite trace used in L168 is
delta_B times the Verdier-normalized trace after multiplication by
sigma_B. It is not legitimate to choose a new scalar at each z.

**The oriented Ext generator.** Fix z and parameters x,y as above.
Let P be L168's augmented free resolution of k=C:

\[
 P:\quad R\xrightarrow{(-y,x)^t}R^2
             \xrightarrow{(x,y)}R\longrightarrow k.
                                                               \tag{4}
\]

The three free modules have cohomological degrees -2,-1,0, in
that order. With the ordered degree-one basis e_x,e_y and top
basis e_x wedge e_y, these are exactly the tensor-ordered
homology Koszul arrows in I, C.1. Let epsilon_{x,y} be the class
of the functional 1 on P^{-2}, as in L168.

There is a sign to retain when comparing this functional with the
source's unsigned-transpose cohomology Koszul complex. Write
N=K^bullet(x,y) for that complex. In degrees 0,1,2 its arrows are

\[
 R\xrightarrow{(x,y)^t}R^2\xrightarrow{(-y,x)}R.
                                                               \tag{5}
\]

In contrast the internal Hom complex Hom^bullet(P,R), with
d(f)=d_R f-(-1)^{deg f}f d_P, has arrows

\[
 R\xrightarrow{-(x,y)^t}R^2\xrightarrow{(-y,x)}R.
                                                               \tag{6}
\]

The isomorphism from (5) to (6) has components

\[
                      1,\quad -I_2,\quad -1.           \tag{7}
\]

Indeed its first chain equation is -(x,y)^t=(-I_2)(x,y)^t,
and its second is (-y,x)(-I_2)=(-1)(-y,x).
This is the comparison inducing the source's map (C.2.3), not
just a cohomology-line identification: for an injective resolution
E^bullet of R, the same components give a chain map
E^bullet tensor N -> Hom^bullet(P,E^bullet). On an element
e tensor q with q of Koszul degree i the multiplier is
(-1)^{i(i+1)/2}. The Hom differential and the tensor differential
give this recurrence, and its Koszul-degree-zero component is the
identity. Hence it commutes with the two natural inclusions of
Hom_R(k,E^bullet), by augmentation of P on one side and the
degree-zero cycles of N on the other. These are precisely the
quasi-isomorphisms defining (C.2.3). Thus the top generator 1 in
N maps to -epsilon_{x,y} in Ext^2_R(k,R).

For r=2, the multiplier (-1)^r in (C.2.4) is +1. In (C.2.7)
the shift by two also leaves the above differentials and the
identification with Ext^2 unchanged. Consequently, if phi denotes
the cited fundamental local isomorphism, then

\[
             phi_R,k(R)(1/(x\wedge y))=-epsilon_{x,y}.
                                                               \tag{8}
\]

Here 1/(x wedge y) denotes the dual determinant element evaluating
to 1 on (x mod m^2) wedge (y mod m^2), not an unoriented scalar
fraction. By I, Lemma C.5.4, its image in local cohomology is the
authors' square-bracket fraction [1/(x,y)]. Thus epsilon_{x,y}
maps to -[1/(x,y)]. Their round- versus square-bracket comparison
has factor (-1)^2=+1; there is no further sign in this dimension.

**Parameter coefficient in the finite trace.** Write, near z,

\[
                 sigma_B=f_z\,dx\wedge dy,\qquad
                 f_z\in R^times.                        \tag{9}
\]

Use (8), multiplication by this fixed form, and the imported
finite-trace and regular-section comparison. II, Remark 5.3.3
and Theorem 5.4.2 evaluate the numerator at z. Hence L168's
functional, with exactly its resolution orientation, is

\[
             tau_z(epsilon_{x,y})=-delta_B f_z(z).        \tag{10}
\]

In particular this trace is generally not 1 in arbitrary local
parameters. The base form's coefficient and the Hom-complex sign
are both essential. The only convention scalar left in (10) is
the single globally justified delta_B of (1).

**The actual KS coefficient and cancellation.** Let u_1,u_2 be
the tangent vectors dual to x,y at z. L111 (6)–(9) identifies the
residual incoming vectors v_1,v_2 of the actual differential and
computes their normalized fibre pairing as

\[
 \Omega_z(v_1,v_2)=-8\lambda\,sigma_B(u_1,u_2)
                         =-8\lambda f_z(z).             \tag{11}
\]

This uses the actual KS map and A=ad_{h_0}, with A^2=4;
it is not a freely chosen symplectic plane. In L111's full
decomposition v=x a_0+y b_0, reduction gives a_0 mod m=v_1 and
b_0 mod m=v_2. Therefore c_0=omega(a_0,b_0), expressed with
L168's common relative trace scalar, satisfies

\[
                      bar(c_0)=-8\kappa\lambda f_z(z).
                                                               \tag{12}
\]

For kappa=1 this is L111's normalization (5),(9). A common
relative trace rescaling multiplies omega and c_0 by that same
kappa, giving (12) for the normalization allowed in L168. No
rescaling of the fixed h_0 or bracket coordinate is made.

Substitute (10) and (12) into L168 (10):

\[
 mu_z=\frac{4\kappa^2}{bar(c_0)}tau_z(epsilon_{x,y})
     =\frac{4\kappa^2(-delta_B f_z(z))}
             {-8\kappa\lambda f_z(z)}
     =\frac{delta_B\kappa}{2\lambda}.
                                                               \tag{13}
\]

All canceled factors are nonzero: sigma_B is nowhere vanishing,
x,y are regular parameters, kappa and delta_B define isomorphisms,
and lambda>1. This proves (2). Formula (3) follows directly from
L168 (4), retaining its actual beta,rho_z,B_z and twice-Yoneda-square
normalization. No independent identity for those quadrics is inferred.

**Checks and limitations.** Reversing the two parameters reverses
both the oriented Ext generator and f_z(z), and reverses the
ordered incoming pairing in (12); the ratio (13) is unchanged.
More generally an invertible parameter change gives the same
inverse Jacobian determinant in (10) and (12). Higher terms
vanish on these residue lines. This agrees with the canonical
choice independence already proved in L168. Multiplying the
common relative trace by c multiplies kappa, c_0 and mu_z by c;
the expression has the scaling required there. Scaling the fixed
base trace scales delta_B and Q_U together.

For Z empty there are no local generators to choose and (3) is
the zero form on U=0. For singleton Z the same local argument
applies. Throughout, the extra two derived middle classes at a
split point have been retained; ordinary middle base change has
not been imposed. Equal nonzero complex coefficients do not
establish nonzero quartic, positivity, genericity, or any lower
square length. ATTEMPTS/092–094 and the independent existence,
complementary-operation and primitive-realization gaps remain.

**Separate critical audit (2026-10-26, step 563).** Use the
invocation-start SPECIALIZE assessment
`drafts/literature/2026-10-26-uniform-point-weights-critical-audit.md`.
This checks (1)–(13) conditional on the actual-family inputs L111 and
L168. Their retained upstream hypotheses are not independently proved
again. In particular the original connection, forms, marked factors,
actual adjoints and derived base change remain essential.

First check the injective comparison, including both differential
directions. Put N=K^bullet(x,y) with the unsigned arrows (5), and
let E^bullet be a bounded-below injective resolution of R. For
e in E^j and q in N^i=Hom_R(P^{-i},R), define

\[
 F(e\otimes q)(p)=s_i q(p)e\quad(p\in P^{-i}),\qquad
 s_i=(-1)^{i(i+1)/2},
\]

with zero values on the other degrees of P. The total degree is
i+j. The E-differential gives s_i q(p)d_E e on both sides.
For the component on P^{-i-1}, the tensor differential followed
by F has coefficient (-1)^j s_{i+1}; the Hom differential applied
after F has coefficient -(-1)^{i+j}s_i. These agree since
s_{i+1}=(-1)^{i+1}s_i. Thus F is a degreewise invertible chain
map, with components (1,-I_2,-1) when E is replaced by R.
There is no additional sign depending on j.

For g:k -> E^j, the inclusion in E tensor N is g(1) in Koszul
degree zero; applying F sends p in P^0=R to p g(1). This is
exactly g composed with the augmentation P -> k. Its components
on the other degrees are zero. Hence the triangle from
Hom_R(k,E) commutes, not just its induced map on a cohomology
line. The augmentation is a quasi-isomorphism, E is injective,
and P is bounded free; therefore this is precisely the comparison
with RHom in I, (C.2.3). It also commutes with R -> E.

The top map N^2 -> k in (C.2.1) is ordinary reduction. For r=2,
(C.2.4) sends 1 to the positive dual determinant generator, so
the inverse of that identification adds no sign. Applying the
construction to R[2] in (C.2.7) also adds none: its differential
and tensor-shift signs involve the even integer two. The preceding
comparison still has s_2=-1. This verifies (8) in the stated
internal-Hom convention. I, C.5.4 identifies its image with the
square-bracket fraction; C.5.3 has sign +1 here. Thus the Ext
generator epsilon, rather than its negative, maps to the negative
fraction used in (10).

Next check that this local map computes the fixed global trace.
The automorphism
(nu_B composed with m_sigma_B)^{-1} composed with chi_B lies in
Hom_D(O_B[2],O_B[2])=H^0(B,O_B)=C. Its invertibility gives
delta_B in C^times, with the direction exactly as in (1).
Applying i_z^! is covariant on this isomorphism, so the resulting
finite functional is multiplied by delta_B, not its inverse.
For the point-to-base composite, finite evaluation and the global
counit are the same composition used in L168 (8). The support/open
and proper-trace comparisons in I, 5.3.8–5.3.9 and II,
(4.1.2),(4.1.5) identify its local computation with the residue.
The hypotheses hold after shrinking around z: the surface is smooth,
x,y form a regular sequence, and z -> Spec C is an isomorphism.
No flatness over B or ordinary middle base-change is inserted.
II, Proposition 5.3.1, Remark 5.3.3 and Theorem 5.4.2 then evaluate
the numerator f_z at z. Multiplication by sigma_B and the negative
fraction give exactly tau_z(epsilon)=-delta_B f_z(z).

Finally check the family-specific scalar, without treating the
incoming vectors as arbitrary. L111 fixes the bottom generator to
h_0 and identifies v_i=-ad_{h_0} KS(u_i). Its trace form obeys
Omega(Aa,b)=-Omega(a,Ab), A^2=4, and
Omega(KS(u_1),KS(u_2))=2 lambda sigma_B(u_1,u_2).
It follows with both incoming minus signs retained that
Omega(v_1,v_2)=-8 lambda f_z(z). Reduction of v=x a_0+y b_0
gives precisely those v_1,v_2. The common relative trace rescaling
therefore makes bar(c_0)=-8 kappa lambda f_z(z); no endpoint
rescaling or point-dependent scalar has entered this identity.
L168 (9) has coefficient bar(s_0)^2/bar(c_0) on (w,w), and
ell_z(w)=bar(s_0)/(2 kappa). Scaling both entries to n_z cancels
bar(s_0)^2 and gives the factor 4 kappa^2 in (13). Its substitution
now gives the stated positive delta_B kappa/(2 lambda).

As a choice check, if (x',y') has Jacobian J at z, the
augmentation-preserving Koszul comparison sends its top generator
to det(J) times the old one. Thus epsilon_{x',y'} equals
det(J)^{-1}epsilon_{x,y} in Ext. Both f_z(z) and the ordered
incoming pairing acquire that same inverse determinant. This
checks coordinate invariance of the cancellation including a
parameter exchange. A common relative trace rescaling multiplies
mu_z by that scalar; a base trace rescaling multiplies it by the
base scalar. These are the scalings of the actual form in L168.

All formulas survive, including empty and singleton Z. The audit
does not set delta_B numerically, compute section quadrics, prove
a square-length bound beyond existing necessary conditions, or
exclude F. ATTEMPTS/092–094 remain applicable. No new lemma input
or DAG edge is required: the source duality is cited here and
the direct mathematical inputs remain L111 and L168. This is
EXPLORATION / REPRODUCTION, not an advance beyond the inspected
source mathematics or a verification of the main conjecture.

## Mathlib

Full matching coverage of this actual-family KS normalization,
finite-point residue and bracket-coordinate specialization has not
been checked. No absence or formal-verification claim is made.
The general duality and residue results are imported by the precise
primary citations above; (4)–(13) give the family-specific informal
comparison. The separate informal critical audit above verifies this
specialization under its retained conditional inputs; it is not a
formal verification or a resolution of the main gap.
