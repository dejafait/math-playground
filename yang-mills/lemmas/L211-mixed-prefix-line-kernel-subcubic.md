# L211 — The mixed prefix trace is subcubic and the joint cubic limit is zero

## Hypotheses

Use L202 and L210's full fixed-mesh SU(2) setting: relative box
(-4,4)^4, admitted even N with a=8/N, straight lower-rooted direction-1
forest, complete compact displacement and both actual L010 probes
i=3,6 at tau=1/16. Take the bare expansion before mesh refinement.
Use ordinary stored-link coordinates and transposes. Keep all physical
faces, variable normal end edges, allowed constant modes, both residual
subtractions and the complete external heat expansion.

Write C for the dimensionless link-to-plaquette circulation, D for
the pinned vertex incidence, Delta=C^T C+DD^T, Sigma=Delta^(-1),
P for the co-closed projection, S=P Sigma, and A=PAP=A^T for the
actual residual of L018(2). In particular A is a local full-link
matrix; its equality to PAP does not replace its local definition
by an arbitrary projected matrix. Put V=q Phi, H=I-D Phi/2,
R=I-D Phi, retaining the actual pinned prefix and endpoint sum.

Use L209(2)'s exact expansion

    SB_i=a^2 sum_(k,l) d_(i;kl) n_k y_l^T,
    n_k=S e_k, y_l=P e_l,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p)              (1)

for every fixed polynomial p. The original third quartic placement
is Q_(3,i,N), and the original joint group is

    G_(i,a)=kappa_0(f_(i,1),r_1)
                         -kappa_0(f_(i,1),r_0,S_3).

## Conclusion

For the original, unregularized covariance, define

    R^0_(i,N)=6a^2 sum_(k,l)d_(i;kl) Tr(
       A_1T Sigma_T diag(y_T)
       [diag(alpha_T)q_T Phi_1-q_T Phi_1 diag(alpha_1)] Sigma_1),
    alpha=V n_k.                                    (2)

This is L210's mixed trace with Z=Sigma, justified below directly
from the original contraction rather than by reversing a polynomial
approximation. Then

    |R^0_(i,N)|<=C_i N^2,
    |Q_(3,i,N)|<=C_i N^(5/2),                       (3)
    lim_(N->infinity) a^3 G_(i,a)=0,  i=3,6.         (4)

The bound concerns the complete mixed trace, not the mixed residual's
operator norm. Its proof retains the entire coefficient difference
and the full prefix: the latter samples the residual covariance along
only two axial fibers per transverse edge. The essential kernel bound is

    |(Sigma A Sigma)_(h,e)|
           <=C N[(1+dist(h,e))^(-2)+N^(-2)]          (5)

on all variable links, with lattice-unit distances. It is summable
along those fibers. No signed positivity, smoothness through the upper
pin, mass-dependent localization or scalar-to-mixed extension of L065
is used.

This settles the selected joint-group cubic-limit test within the
imported local inputs. It is a standard-method local result, with no
claim of progress beyond the assessed sources. It does not bound the
complete group by O(N^(5/2)): L202's other contributions are retained
as o(N^3). The independent f_(i,2),r_0 term, full compensation, finer
asymptotics, finite matching, interacting reflected error <=c_box/2,
continuum axioms and infrared finite positive mass remain unresolved.

## Proof

### 1. Apply the signed reduction directly to the original covariance

Since A=PAP and P commutes with Sigma,

    M=2SAS=2Sigma A Sigma.

For n=n_k and y=y_l set, exactly as in L209,

    Y=diag(Vn)-diag(Rn)V,
    Bcal=H^T diag(y)V-V^T diag(y)H.

L187(3),(6) and L209 proof section 2 give the finite identity

    Q_(3,i,N)=6a^2 sum d_(i;kl)
                        Tr(A Sigma Y^T P Bcal Sigma). (6)

All identities here are for the original M, not its varying-mass
approximant. L209's proof of projection removal uses the polynomial
only through the bounded right-end filter F_pol=Delta Z. For (6)
that filter is the identity. To check the bound explicitly, let
G_0=(D^T D)^(-1) and E_A=S^(1/2)AS^(1/2). Its two factors are now

    T_k=G_0^(1/2)D^T Y S^(1/2),
    W_l=G_0^(1/2)D^T Bcal S^(1/2).

L209(7),(9),(12) and its full residual form bound give

    ||T_k||_HS<=C p(k)N^3,
    ||W_l||_HS<=C p(l)sqrt(log(eN)), ||E_A||<=CN.

In particular D^T Bcal=-q^T diag(y) uses D^T y=0 and the full
pinned edge product identity, including the normal end rows. The
modal difference after deleting P in (6) is -6Tr(E_A T_k^T W_l).
The Hilbert--Schmidt trace inequality and (1) therefore prove

    Q_(3,i,N)=Qhat^0_(i,N)+O_i(N^2 sqrt(log(eN))),    (7)

where Qhat^0 is the trace in (6) with just that displayed P removed.
This specialization requires no polynomial theorem or limit exchange.

L210 proof sections 1–2 apply unchanged to these modal Y,Bcal:
(Y^T Bcal)_TT=0 and

    (Y^T Bcal)_T1+((Y^T Bcal)_1T)^T
       =diag(y_T)[diag(alpha_T)q_T Phi_1
                                  -q_T Phi_1 diag(alpha_1)].

In particular the upper-only axial part of Rn cancels here because
the upper normal source column of Phi_1 is exactly zero. This is an
algebraic cancellation before inequalities, not omission of an edge.
Expanding Qhat^0 into blocks thus gives exactly

    Qhat^0_(i,N)=D^0_(i,N)+R^0_(i,N).                (8)

For the axial diagonal D^0, L210 proof sections 3–5 likewise apply
with F_1=I. More explicitly, L065's scalar form yields
||Sigma_1^(1/2)A_11 Sigma_1^(1/2)||<=C, and L210(18)–(19) give

    ||Y I_1 Sigma_1^(1/2)||_HS<=C p(k)N^3,
    ||Bcal I_1 Sigma_1^(1/2)||_HS<=C p(l)N^(3/2).

Their trace product, times a^2 and the heat weights, proves

    |D^0_(i,N)|<=C_i N^(5/2).                       (9)

These are the same unprojected full-spectrum counts as in L210,
including its upper rank-one covariance contribution. There has been
no transfer of the scalar residual estimate to A_1T.

### 2. Keep one circulation on each side of the actual residual

L018(2) and L028's exact polarized stencil compositions, in stored
coordinates as also recorded in L166 proof section 1, give

    A=(C^T C K_a+K_a^T C^T C)/2-Q_3-Q_6,
    K_a=a^(-1) E U Ccl C,
    Q_3=C^T W_3 C, Q_6=C^T Ccl^T S_6 Ccl C.        (10)

Here E is the endpoint average, Ccl the ordered clover average,
U contracts with the actual displacement, W_3 is the actual
four-vertex averaged plaquette weight and S_6 is the polarized shear
matrix. S_6 is not the covariance S. These maps retain the original
unequal component filters and symmetric cross-entry factors.
All their stencils have uniformly bounded radius and overlap; U,W_3,
S_6 have uniformly bounded entries and compact interior support.
The factor a^(-1) in K_a is essential.

Consequently the exact factorization is

    A=C^T J C,
    J=(C E U Ccl+Ccl^T U^T E^T C^T)/(2a)
                                 -W_3-Ccl^T S_6 Ccl. (11)

Both generator orders and both insertion subtractions occur in J.
It is a finite-range signed plaquette matrix: for fixed constants
r_*,c independent of N, each row and column has at most c nonzero
entries, |J_(p,q)|<=C N, and J_(p,q)=0 if dist(p,q)>r_*.
Its row and column support lie in a compact interior enlargement
of the displacement/strain support. The incidence in J has not
been discarded; its finitely many entries are bounded here. Shifted
coefficient values in its adjoint are retained exactly. This uses
the local definition (10), rather than the nonlocal formula PAP.

For any variable link e and any plaquette p in that enlargement,
L200(4)'s same-component first-difference Green estimate implies

    |(C Sigma)_(p,e)|
             <=C[(1+dist(p,e))^(-3)+N^(-3)].        (12)

Each circulation is a finite signed sum of first differences on
the appropriate scalar component kernel. No difference between
different component Green functions is asserted. The estimate
includes every external source e, including normal end edges; the
circulation stencils p are interior. L200's estimate was proved
using the full relative spectrum and its allowed constant modes.

### 3. Convolve the two differentiated kernels

Let b(x)=(1+|x|)^(-3) on Z^4, using any fixed lattice norm.
The elementary convolution estimate is

    sum_(z in Z^4) b(z-x)b(z-y)
                                <=C(1+|x-y|)^(-2). (13)

For completeness put R=1+|x-y|. When R is bounded the sum is
bounded by Cauchy–Schwarz and sum b^2<infinity. Otherwise, on
|z-x|<=R/3 the second factor is at most C R^(-3), and
sum_(|z-x|<=R/3)b(z-x)<=CR, by four-dimensional shell counting.
This gives C R^(-2); the region near y has the same bound. In the
remaining region with |z-x|<=3R both factors are at most C R^(-3)
and there are O(R^4) points. On |z-x|>3R the two distances are
comparable, so shells give sum_(r>3R) C r^3 r^(-6)<=C R^(-2).
These four regions prove (13), with bounded stencil shifts and
staggered centers absorbed into C.

In the finite box there are O(N^4) possible plaquette anchors and
each lies within O(N) of a given link. Thus also

    sum_p (1+dist(p,e))^(-3)<=CN.

Using (11) and symmetry of Sigma, the exact kernel is

    (Sigma A Sigma)_(h,e)
       =sum_(p,q) (C Sigma)_(p,h) J_(p,q)(C Sigma)_(q,e).

Take absolute values only after this factorization. The finite range
and bounded overlap of J permit replacing q by p in (12), up to
a constant, and extracting the bound CN. The product of the two
decaying terms is bounded by (13). Each cross term with N^(-3)
has sum at most CN^(-2); the two constant terms have sum at most
CN^4 N^(-6)=CN^(-2). This proves (5). Neither A nor its sandwiched
kernel has been assumed positive. All internal plaquettes and
covariance sources allowed by (11) have been included.

### 4. Sum the actual prefix fibers before the output volume

Let e be a transverse edge of direction mu at axial vertex level s.
Write its transverse endpoints as z and z+e_mu. By the definition
of q_T and the lower prefix, (q_T Phi_1)_(e,h) can be nonzero only
when h is a direction-1 edge at transverse position z or z+e_mu,
with axial level 0<=r<s. An endpoint on a pinned face contributes
zero. Each surviving entry is one; keeping a bound of two would
give the same estimate. The last axial source r=N-1 is zero as
required by the actual prefix, not by a newly imposed truncation.

For these entries, dist(e,h) is comparable, up to a fixed additive
constant, to |s-r|. Equation (5) and the convergent one-dimensional
series sum_(j>=0)(1+j)^(-2) therefore give, uniformly in e,

    sum_h |(q_T Phi_1)_(e,h)|
                          |(Sigma A Sigma)_(h,e)|
               <=CN[sum_(j>=0)(1+j)^(-2)+N*N^(-2)]
               <=C'N.                              (14)

This includes the full lower prefix even at levels near the upper
face. No covariance source or constant mode was removed in deriving
the pointwise bound. The fiber restriction is an exact support
property of the remaining matrix in the trace.

Cyclicity in the finite trace (2), with Sigma componentwise, writes
its modal summand before the outside 6a^2 as

    sum_(e in T,h in 1) (Sigma A Sigma)_(h,e)
             y_e (q_T Phi_1)_(e,h)(alpha_e-alpha_h). (15)

There is no additional factor two: both mixed orientations are
already combined by (8). L187(14)–(15) and L209(8) give globally

    |alpha_e-alpha_h|<=C p(k)N,
    |y_e|<=C a^2 p(l).                              (16)

The first estimate retains even the upper pinned jump; no Taylor
expansion or smallness of the coefficient difference is required.
There are O(N^4) transverse output edges. Applying (14)–(16) to
(15) and then restoring the outside a^2 yields

    |R^0_(i,N)|
       <=C a^2 sum_(k,l)|d_(i;kl)|p(k)p(l)
                                      N^4 a^2 N*N
       <=C_i a^4 N^6=C_i' N^2.                    (17)

This is the required contraction with the actual residual before
estimating the prefix. It does not rely on finite propagation or a
first-moment expansion at varying mass/degree.

### 5. Restore the original joint group

Equations (7)–(9),(17) give

    |Q_(3,i,N)|<=C_i[N^(5/2)+N^2 sqrt(log(eN))+N^2]
                  <=C_i' N^(5/2).

Thus a^3 Q_(3,i,N)=O_i(N^(-1/2)) tends to zero. L202(5), including
its complete co-closed and sextic reductions, states precisely
G_(i,a)=-Q_(3,i,N)+o(N^3). Substitution proves (4) for both probes.
The minus sign is retained even though the resulting coefficient is
zero. The reduction does not assert convergence of H and Q_tr
separately or any forest invariance of this selected group.

All new checks are analytic: the original-covariance specialization,
the exact local factorization, the complete convolution split, the
two-fiber support and the powers in (17). No numerical fixture or
mathematical script is used as proof. This is not a candidate solution
of the Yang–Mills construction problem.

### 6. Separate critical audit, 2026-10-16

The separate audit accepts (3)–(4) relative to the stated imported
inputs. It reconstructed the original finite contraction and checked
the following domains and powers; it is not an independent audit of
every earlier flow or Gaussian-retraction theorem.

**Original covariance and block algebra.** Starting from L187(3),(6),
substitute M=2Sigma A Sigma and Gamma_y=-Bcal_y/2. The resulting
coefficient is +6, and U_n^T P=Y_n^T P gives (6). Thus no limit or
polynomial replacement is used to obtain that starting identity.
Since Sigma A Sigma=S^(1/2)E_A S^(1/2), the correction P-I is
exactly -6 Tr(E_A T_k^T W_l) with the factors in section 1.
The audit checked L209's pinned edge identity and energy estimate:
the latter uses transverse Dirichlet differences but no artificial
endpoint penalty on an own-direction edge interval. Its full inverse
square sum is O(N^4 log(eN)). Hence the correction, including the
outside a^2, is O(N^(-2) N N^3 sqrt(log(eN)))
=O(N^2 sqrt(log(eN))). The identity filter is admissible in these
finite inequalities; it need not belong to L205's polynomial schedule.

Multiplying L210's blocks directly gives C_TT=0 and the two mixed
terms in (5) of that lemma. Their extra product contains
diag(nu_1)Phi_1^T, which is zero: nu_1 is supported on r=N-1,
whereas that source column of Phi_1 is zero. Both orientations then
give exactly (15), with no further factor two. For the axial block,
L065(1) applies to all axial frequencies. Positive sandwiching by
Sigma_1^(1/2) bounds E_11, without bounding A_1T. The audit also
recomputed Tr(U L_D)=2(N-1), including the upper endpoint, so the
two unprojected factors are N^3 and N^(3/2), and their response is
O(N^(-2) N^(9/2))=O(N^(5/2)).

**Stored-coordinate normalization and sources.** L028's conversion
from the physical residual is A=a^2 N_a. Since d_a=C/a, its
generator remains K_a=E U Ccl C/a, whereas multiplying each physical
insertion by a^2 gives exactly the two bounded curvature weights in
(10). This independently checks the single 1/a in J. Neither a
cell-volume factor nor a second 1/a belongs in C Sigma. The common
cochain weight cancels from these adjoints. Both sides of J are
supported in a fixed interior stencil enlargement, including its
shifted adjoint coefficients.

For (12), the case j=1,h=0 of L200(4) suffices: only the
plaquette observation stencil needs a difference, and every source
link remains free. In its heat proof the near images are retained;
the long-time differentiated sum is O(N^-5 exp(-ct/N^2)), whose
integral is O(N^-3). Allowed constant own-direction modes are
included. This verifies the imported boundary domain rather than
requiring a source separated from the boundary. The four-dimensional
convolution of the two r^-3 kernels has bound r^-2; its finite-size
cross terms and constant term are each O(N^-2), before the O(N)
coefficient of J. There is no borderline logarithm in that convolution.

**Fiber count and assembly.** A transverse output e selects exactly
its two endpoint fibers with 0<=r<s; pinned endpoints select none.
The sum of (1+|s-r|)^-2 is uniformly finite even for s=N-1.
The finite-size term contributes at most N*N^-2. Thus the full
fiber kernel sum is O(N), before multiplying alpha_e-alpha_h.
The absolute response count is

    outside a^2 * O(N^4) outputs * O(a^2 p(l)) exterior
      * O(N p(k)) coefficient difference * O(N) fiber sum
        = O(p(k)p(l) N^2).

L209(2)'s uniform polynomial heat summability applies to precisely
these p(k),p(l); there is no hidden mode cutoff or supremum estimate
for P on arbitrary vectors. Finally L202(5), whose signed assembly
was checked against its proof section 5, imports the complete
co-closed reduction, sextic bound and Q_1+Q_2 removal. It is
G=-Q_3+o(N^3), not G=-Q_3 identically. Consequently the accepted
rate O(N^-1/2) applies to a^3 Q_3; only convergence to zero is
asserted for a^3 G. Separate H and Q_tr limits, the other probe jet
and the full response are not certified by this audit. No numerical
test, source refresh or new lemma was needed; Mathlib coverage remains
as qualified below.

## Mathlib

Full matching actual-probe limit and lattice Green bounds: **not
checked**. Supporting finite matrix algebra, Hilbert–Schmidt trace
inequalities and lattice convolution estimates: **not checked**;
unknown availability is not absence. The convolution is proved above
to specify its dimension, boundary correction and subsequent fiber
restriction. The local residual factorization is written explicitly
because its two circulation legs, normalization and boundary support
are essential. The differentiated relative Green theorem is imported
from L200(4) within its stated domains, not replaced by an uninspected
continuum Green theorem. Reuse the unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md).
No general renormalization theorem is reproved and no originality
claim is made.
