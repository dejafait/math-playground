# L220 — Exact cancellation of the complete linked cubic coefficient

## Hypotheses

Use L218's complete coefficient Gamma_(i,a) of L011(6), for SU(2),
both actual L010 probes i=3,6, flow time 1/16, the relative all-face
cube D=(-4,4)^4, admitted even meshes a=8/N, and the straight
lower-rooted direction-1 forest. The bare small-coupling coefficient
is taken at fixed mesh before refinement. Import L218's existence
assembly and L219(1)--(2), including L219 section 7's separate audit
relative to its analytic inputs. No upstream limit is reproved here.

Use the exact analytic identities in L124(1), L128(1), L132(1)--(2),
L138(1), L139(1)--(2), L140(1)--(3), L145(1)--(2), L154(1),
L174(1) and L180(1). Their common physical normalization is

    A_k=f_k/sqrt(lambda_k),
    c_(i;kl)=exp[-(lambda_k+lambda_l)/16]q_i(A_k,A_l),
    V_(k,a)=A_(k,a)-partial_a integral_(-4)^(x_1) A_(k,1), a=2,3,4.

In particular P_(i,D),P_(i,A),P_(i,X),P_(i,C) are precisely L132's
full forms, B_(i,G) is L140's upper-cumulative form, B_(i,R) is
L145's different form, and D_i is the same diagnostic in L180 and
L218. All modes, constant axial prefix, displacement sectors and
transition terms remain. These identifications are proved in L154
section 1, L174 section 1, L180 sections 2--3 and L219 section 7.
All relevant physical sums are absolutely convergent by those inputs.

Use L070(3)'s exact gamma integral, L127(2)'s tau integral,
L129(5)'s three-dimensional H integrands, L131(5)'s xi integral,
and L153(2)'s scalar Green definition. No numerical enclosures,
IEEE arithmetic premise or values of the physical heat forms are used
in this cancellation. Their upstream analytic limit premises remain
essential. The separate critical audit in proof section 5 accepts this
recombination relative to those analytic inputs.

## Conclusion

In the stated scope the complete cubic coefficient cancels exactly:

    mathcal L_i=0,
    lim_(a->0) a^3 Gamma_(i,a)=0,     i=3,6.                 (1)

L010's bounded divergence coefficient, as imported in L218, has the
same zero cubic limit when added to Gamma. Thus this is a full cubic
compensation identity, rather than compensation of selected groups.
It gives only Gamma_(i,a)=o(a^-3). It does not give an O(a^-2)
remainder, any finer power or logarithmic coefficient, finite matching,
a cutoff-uniform coupling expansion, interacting reflected error
<=c_box/2, continuum axioms or infrared finite positive mass. There
is no complete Yang--Mills candidate. This is local REPRODUCTION by
exact algebra and periodic integration, with no originality claim.

## Proof

### 1. Preserve linked physical forms before collecting coefficients

Write g=g_G, and write x_G,y_G for L153's Green differences
G000-G110,G110-G111, respectively. These lower-case symbols will
not denote frequency energies below. Put t=t_ax and q=a_Q. L124
and L128 give

    K_oo-K_E=K_ax-K_Q+K_G+K_R+K_tr.

Substitute this identity in L219(2). Before further simplification,

    mathcal L_i=Lambda_i+K_(i,T)+K_(i,Vmix)
          +3K_(i,ax)-3K_(i,Q)+3K_(i,G)-(9/2)K_(i,R)
          +3K_(i,tr)+12gamma D_i.                        (2)

The R still inside K_oo has been counted once: 3-15/2=-9/2.
Now 3K_G=3g B_G and L180(1) gives

    K_Vmix=-3g B_G+3g D_i+(3g/2)B_R-(3g/2)P_D.

Thus B_G cancels identically, and the remaining R contribution is
-3g B_R. Substituting the other exact formulas named in the hypotheses
gives, with no extra color or outside factor,

    mathcal L_i=c_D P_(i,D)+c_A P_(i,A)+c_X P_(i,X)
                         +c_C P_(i,C)+c_R B_(i,R)+c_d D_i, (3)

where the universal coefficients are

    c_D=17/2-45x_G+15y_G/2+3t/2-3q+3h_D+3tau-3g/2,
    c_A=-9/2+39x_G-9y_G/2-3q+3h_A,
    c_X=-1+3x_G+3y_G/2+3h_X-3tau/2,
    c_C=6-30x_G-15y_G+3xi+6tau,
    c_R=14-72x_G+6y_G-3g,
    c_d=12gamma+3g.                                      (4)

For example Lambda+T has coefficients 17/2-45x_G+15y_G/2,
-5+39x_G-9y_G/2,-3/4+3x_G+3y_G/2,6-30x_G-15y_G on
P_D,P_A,P_X,P_C and 14-72x_G+6y_G on B_R. The -3K_Q term
then adds (-3q,-3q+1/2,-1/4,0). This checks the constant terms
in (4) independently of any interval evaluations. The task is now to
prove all six c's zero, with the links in (4) retained.

### 2. Put every scalar over the same full-torus denominator

Let brackets be normalized integration over [-pi,pi]^3. Set

    X=2-2cos(theta_2), Y=2-2cos(theta_3), Z=2-2cos(theta_4),
    L=X+Y+Z, a=1-X/4, b=1-Y/4, c=1-Z/4,
    S1=aX+bY+cZ, S2=a^2 X+b^2 Y+c^2 Z.

Only in this section a,b,c denote squared filters. For each scalar s
in the following table, write s=<n_s/L^2>:

| s | Complete numerator n_s |
| --- | --- |
| x_G | L[(X+Y)/2-XY/4] |
| y_G | L(1-X/2)(1-Y/2)Z/2 |
| g | -XY(X-Y)^2/4 |
| gamma | (L S2-S1^2)/3 |
| q | 4aYL |
| t | (4/3)[L^2(a^2+b^2+c^2)-2L S2+S1^2] |
| h_D | X(4+Z)b^2 L/2-2abZ[b(X+Z)+cY] |
| h_X | abZ[(b+c)(X+Z)+2cY] |
| h_A | 2a(bY+cZ)L-n_(h_D)-2n_(h_X) |
| tau | -abZ[YL+(Y-Z)(X+Z)/2] |
| xi | aYZ(Z-Y)^2/8 |

The first two rows follow directly from L153(2): separate angle
reflections replace cos(theta_2+theta_3) by cos(theta_2)cos(theta_3)
and cos(theta_2+theta_3+theta_4) by the threefold product. Thus their
numerators before multiplication by L are 1-(1-X/2)(1-Y/2) and
(1-X/2)(1-Y/2)Z/2. Absolute integrability of the Green kernel
justifies these reflections. The gamma, g, q, H, tau and xi rows are
exactly the cited integrands, without interval or midpoint replacement.
For t, put F=diag(a,b,c), d_j=2sin(theta_j/2), and Q=I-dd^T/L.
Expanding the trace in L139(1) gives

    Tr[(QFQ)^2]=Tr(F^2)-2d^T F^2 d/L+(d^T Fd)^2/L^2,

which is precisely its table entry. In particular both Q's and every
unequal filter remain. All table quotients are locally bounded at
L=0, or have the already imported absolute Green bound; all are
absolutely integrable. No value at that measure-zero point matters.

### 3. Exact polynomial identities and their zero integrals

For a polynomial p(X,Y,Z), let S p be its average over all six
permutations of X,Y,Z. Normalized full-torus integration is invariant
under those permutations, and L is invariant. Define polynomials

    M1=L^2 S(Z-2),
    M2=L^2 S(YZ-4),
    D[p]=S{(2-X)Lp+X(4-X)[L partial_X p-p]}.             (5)

Let N_D,N_A,N_X,N_C,N_R,N_d be obtained from the six lines of (4)
by replacing each scalar s with n_s and each constant with that
constant times L^2. Thus c_j=<N_j/L^2>. Substitution of the table,
followed by ordinary polynomial expansion, gives these exact identities:

| Numerator | Permutation average |
| --- | --- |
| S N_D | (3/2)M1+(9/16)M2 |
| S N_A | -(3/2)M1-(3/16)M2 |
| S N_X | -(3/2)M1+(3/16)M2 |
| S N_C | 3M1+M2/8+D[YZ^2]/4+D[XYZ]/8 |
| S N_R | 6M1-(3/4)M2-3D[Z^2]-(3/2)D[YZ] |
| S N_d | 0 |

This is a polynomial identity table, not a numerical evaluation. It
specifies the full expressions, including all zero coefficients. It
can be checked simply by multiplying out (5) and the preceding table;
the exact complete coefficient checks in section 4 do so. For the last
row there is also a short direct proof: L S2-S1^2 equals
sum_(j<k) X_j X_k(f_j-f_k)^2 with f=(a,b,c), so

    gamma=(1/48)<sum_(j<k) X_j X_k(X_j-X_k)^2/L^2>
          =-g/4.

The second equality uses equality of the three integrated pair terms
under permutation. It proves c_d=0 with its original 12 and 3.

Every expression on the right in the identity table has zero integral
after division by L^2. Indeed <Z>=2 and <YZ>=<Y><Z>=4, since the
normalized angles are independent product integration variables and
the mean cosine is zero. Hence <M1/L^2>=<M2/L^2>=0.

For the four p's used in the table, the chain rule gives on L>0

    [(2-X)Lp+X(4-X)(L partial_X p-p)]/L^2
          =partial_(theta_2)[2sin(theta_2)p/L].           (6)

Here partial_(theta_2)X=2sin(theta_2),
2cos(theta_2)=2-X, and 4sin(theta_2)^2=X(4-X), fixing all factors.
Each p is a monomial of degree at least two in the energies. Near
the only zero of L, writing r=|theta|, p=O(r^4), L is comparable
to r^2, and the vector field in (6) is O(r^3), with first derivatives
O(r^2). It extends C^1 through zero, with zero derivative there.
It is periodic across torus faces, and its normal component also
vanishes at theta_2=+/-pi. Integrating (6) gives zero, with no origin
or face boundary term. The same holds after permutation averaging.
Consequently <D[p]/L^2>=0 for all four p's. No principal value,
unproved singular integration by parts or omitted corner is involved.

The identity table proves all coefficients (4) are zero. Absolute
convergence of the imported full physical forms permits (3), so
mathcal L_i=0 for both actual probes. L218's already-established
finite complete limit now proves (1). This step does not exchange
the small-coupling and mesh limits or claim a quantitative remainder.

### 4. Complete exact certificate and source/review scope

Run from the notebook:

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/recombine_complete_linked_coefficient.py

The full certificate is
`scripts/combined-ward-response/complete-linked-coefficient-certificate.json`.
Seven assembly checks reconstruct (4) directly from the original
group formulas in (2), including the explicit B_G cancellation.
Six fixed polynomial checks expand the identity table in section 3;
every complete defect polynomial is empty. Six additional rational
elimination checks find zero-integral representations without being
supplied the fixed right sides; they use the same polynomial operations
and are not an independent implementation audit. All 19 checks pass,
with zero failures.
The complete six fixed actual/required polynomial pairs and all
assembly/identity defects were inspected. The script uses exact
integer/Fraction polynomial arithmetic only. Its finite identities
are supplemented by the analytic integrability and boundary proof
above; no finite-frequency samples stand in for an integral argument.

The unchanged ready assessment is
`drafts/literature/2026-10-16-complete-residual-coefficient-cubic-assembly.md`.
Its primary flow/Ward comparisons do not evaluate the bare forest
coefficient. This proof recombines already established specialized
functional formulas; it imports no new external theorem and reproves
none. ATTEMPTS/033--035's isolated tensor-removal failures remain
valid: they do not test this linked sum of all groups. No selected
group is assigned forest invariance, no overlapping interval is
called cancellation, and no numerical sign input is necessary.
The separate audit below checks the new recombination and its scalar/
heat normalization; all upstream analytic inputs remain imported.

### 5. Separate critical audit, 2026-10-17

This audit accepts (1)--(6) without correction, relative to the imported
analytic limit statements. It does not recursively certify those limits,
derive a quantitative remainder, or solve the Yang--Mills construction.
The unchanged ready complete-coefficient assessment covers this audit.
Its primary-source comparison is reused; no new external theorem or
source scope is introduced. This is local REPRODUCTION, not an
originality claim or an inference from numerical interval overlap.

**Group signs and full physical normalization.** Starting with
L219(2), L124(1) and L128(1), the R coefficient outside the transverse
H sum is 3-15/2=-9/2. L180(1) contributes +3g B_R/2, leaving
-3g B_R after L145(2). Its -3g B_G cancels L140(3)'s +3g B_G;
B_G and B_R have not been identified. L138(1), L139(2),
L132(2), L154(1) and L174(1) then give exactly (4), including
the constant shifts +1/2 and -1/4 from -3K_Q. The diagnostic term
is +12gamma D_i+3g D_i, with no additional color or outside factor.
These checks use L218 only for its already audited complete limit.

L132(1), L140(1), L145(1), L154(3), L174 section 1 and L180
sections 2--3 all use the same A_k, symmetric c_(i;kl), lower lift
V_k and ell=x_1+4. In ordinary product-mode coordinates, the two
inverse square roots from q_i(A_k,A_l) and the two from V_k,V_l
give precisely one factor exp(-lambda_k/16)/lambda_k per label,
as L132(6) confirms. No second covariance normalization is inserted.
L180(14) retains U_l=(dA_l)_(1T)(4,x_T), so its D_i is exactly
L080(1)--(2)'s upper-curvature diagnostic, also used in L218.
Symmetry of c exchanges its two labels where necessary; it neither
changes the boundary sign nor deletes a probe sector. L180(15)
retains partial_1 ell=1 and div u=0 in its B_R/P_D reduction.
Thus both full probes, both displacement sectors, all exterior labels,
the constant axial prefix and the transition region survive the match.

**Every scalar row.** Independent angle reflections in the absolutely
integrable L153(2) Green integral give the x_G and y_G rows exactly;
the sine products integrate to zero before combining the cosines.
L070(3) has c_j^2=1-X_j/4 and hence gives the stated gamma numerator.
L140(2)/L145(2) gives g with its minus sign and factor 1/4.
L138's distinct-index a_Q is 4aY/L; choosing that ordered pair is
permitted by its integrated permutation invariance. L139(1) has
E^2=diag(a,b,c), not diag(sqrt(a),sqrt(b),sqrt(c)). Cyclic trace and
Q^2=Q give Tr[(QFQ)^2]=Tr(F^2)-2Tr(PF^2)+Tr(PFPF), exactly the
t row. L129(5) gives the h_D,h_X rows with k=X+Z and h_A=g_0-h_D-2h_X.
L127(2) gives the negative tau row, with its second denominator and
factor 1/2 retained. L131(5) gives xi after its justified Y/Z integral
symmetrization; it is not assigned to an unsymmetrized pointwise row.
All measures are normalized full-torus measures. These statements are
analytic identities, so none of their numerical interval premises is
needed. The bounded, possibly directional t limit at zero is sufficient;
continuity of every separate scalar integrand is not assumed.

**Independent complete polynomial verification.** Run

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/audit_complete_linked_coefficient.py

The full certificate is
`scripts/combined-ward-response/complete-linked-coefficient-independent-audit.json`.
This implementation imports neither the production polynomial class
nor its elimination routine. It evaluates the imported group formulas
before collection and independently evaluates the fixed right sides
of section 3, using exact Fraction arithmetic on {0,1,2,3,4,5}^3.
Each numerator and right side has total degree at most five, so its
degree in each separate variable is at most five. A polynomial of
degree at most five in each variable vanishing on that Cartesian
grid is identically zero: fix two variables and apply the six-root
univariate bound, then repeat for the other variables. Thus these
are complete polynomial identities, not frequency samples or an
approximate quadrature. The formal energy value 5 is an interpolation
node and is not asserted to arise from an angle.

All 216 nodes pass: 1,512 original-group/collected coefficient checks
and 1,512 permutation-averaged fixed-identity checks, including the
identically zero B_G component. The 215 nonzero nodes also pass all
2,365 scalar numerator/source-quotient comparisons. The t comparison
uses actual three-by-three QFQ matrix multiplication rather than its
expanded trace formula; gamma uses the weighted-variance pair identity.
All cleared numerators vanish at the omitted origin; no separate
direction-independent source quotient there is asserted. All 5,389
complete rational defects are zero. Every node, all defects, the degree
bound and source hash are saved, with no failures. The original 19
checks were separately replayed and also pass; that replay alone would
not be an independent verification.

**Origin, face and integral argument.** The fixed proof uses only
p=YZ^2,XYZ,Z^2,YZ. Writing r=|theta| near zero, these p satisfy
p=O(r^4), grad_theta p=O(r^3), L comparable to r^2 and
grad_theta L=O(r). For W=2sin(theta_2)p/L this gives W=O(r^3) and
grad_theta W=O(r^2) off zero. Defining W(0)=0 makes it differentiable
there with zero derivative, and the off-zero derivatives converge to
that derivative. It is therefore C^1 on the torus. At opposite faces
the energy variables and cosine derivatives agree; the sine factor
vanishes at both theta_2 faces. There is no singular origin flux or
unmatched face contribution. The ordinary periodic derivative integral
is zero. The exact moments <Z>=2 and <YZ>=4 use product measure,
and averaging all six permutations preserves both L and that measure.
This proves the zero integrals in the table, without relying on the
production elimination's larger divergence basis.

Absolute convergence of the imported physical heat forms justifies
their finite linear recombination. L218 then turns the six verified
zero scalar coefficients into (1), and its bounded divergence input
leaves the full Ward coefficient with the same zero cubic limit.
No joint coupling/cutoff limit, quantitative o(a^-3) rate, finer power,
logarithm, finite matching or interacting estimate has been established.
The isolated failures ATTEMPTS/033--035 remain valid and are not
reopened by this audit.

## Mathlib

Full specialized forest coefficient cancellation: **not checked**.
Supporting polynomial identities, finite permutation averages,
product cosine integration and periodic integration by parts:
**not checked**. Unknown availability is not absence. The finite
algebra and elementary analytic boundary argument are supplied here;
no matching Mathlib result is assumed.
