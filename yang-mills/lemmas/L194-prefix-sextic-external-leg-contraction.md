# L194 — External-leg contraction of the prefix sextic

## Hypotheses

Use exactly L182–L183's SU(2) expansion in the relative box (-4,4)^4,
admitted even N, a=8/N, straight lower-rooted direction-1 forest,
complete displacement and both actual L010 probes at tau=1/16.
Bare expansion precedes refinement. Coordinates and adjoints are
ordinary dimensionless full variable-link coordinates, with three
independent Gaussian colors of covariance S. Keep every physical
face, normal end edge, constant own-direction mode and heat mode.
Vertex potentials vanish on all boundary vertices.

Keep L183's complete cubics script R_3, script S_3, residual A=PAP
with both insertion subtractions, B=B_i=PBP, and

    T=2SA, M=TS=2SAS, t=Tz,
    V=q Phi, F=D Phi, H=1-F/2, R=1-F,
    b=[z,Vz]/2-[Fz,Vz]/4, J=2<Bz,b>, W=P db(z)[Tz],
    rho_H=script R_3-d script S_3[Tz].

M is signed; no smooth-input assertion is made about t. Use L184's
skew matrices Gamma_e=-(H_e^T V_e-V_e^T H_e)/2 and its complete
quartic placements Q_1,Q_2,Q_3. For link vectors n,y put

    Gamma_y=sum_e y_e Gamma_e, J_y=P Gamma_y P,
    U_n=diag(Vn)H-diag(Hn)V.                              (1)

J_y is a matrix, distinct from the scalar cubic J. Let r_abc and
s_abc be the full alternating spatial tensors of script R_3 and
script S_3, respectively, in the convention

    C(z)=(1/6)sum_(a,b,c,k,d,f) c_abc epsilon_kdf
                                  z_a^k z_b^d z_c^f
        =sum_(a,b,c) c_abc z_a^1 z_b^2 z_c^3.             (2)

Here c denotes either tensor and epsilon_123=1. L155 and L190
justify these tensors for the full cubics before forest restriction.
For a link vector n write (c_n)_bc=sum_a n_a c_abc; this is a skew
matrix. All link indices in this lemma are unrestricted finite sums.

## Conclusion

The complete retained sextic satisfies

    |E[J_i rho_H]| <= C_i N^3 sqrt(log(eN)).              (3)

In the external-leg contraction below, the placement in which the
tilt reaches the smoothed external leg is only O(sqrt(log(eN))),
and therefore has zero a^3-scaled limit. The other two placements
have the bound in (3); no zero limit is assigned to them.

For any exact decomposition SB=sum_j n_j y_j^T, the remaining
signed prefix group has the finite common-trace formula

    E[J rho_H]-E[dJ[W]]=sum_j Z(n_j,y_j)-Q_1-Q_2,         (4)

    Z(n,y)=-6 Tr(J_y S(r_n-s_(Tn))S)
             +6 Tr(J_y M(2 s_n S+U_n^T)).                (5)

Thus the rough-tilt action slices and Q_3 must be compared in their
actual shared trace order; neither is discarded by skewness. For
the actual probes L185–L186 remove Q_1+Q_2 at cubic scale. L193
removes the co-closed probe contribution at that scale. Combining
(3) with L187 consequently gives the first bound here for the full
joint group G of L181:

    G_(i,a)=O(N^(7/2)),  |a^3 G_(i,a)|<=C_i sqrt(N).     (6)

This misses cubic boundedness by one half power. In particular it
gives no finite scaled limit, growth lower bound, actual-probe sign,
compensation coefficient or finer asymptotics. The logarithmic loss
in (3) also cannot be discarded. Independent f_(i,2),r_0 compensation,
finite matching, the interacting reflected error <=c_box/2, continuum
axioms and infrared finite positive mass remain unresolved.

## Proof

### 1. A local quadratic bound with every face retained

We need the quadratic version of L190's local cubic count. Fix two
different colors d,f and a bilinear polynomial q=sum_lambda q_lambda
in those colors. Suppose each q_lambda uses a bounded-radius stencil,
there are O(N^4) placements with bounded incidence multiplicity, and
its absolute coefficient sum is at most B_N. Then

    ||q||_(L2(S)) <= C B_N N^2 sqrt(log(eN)).             (7)

Indeed write q=sum_ab k_ab z_a^d z_b^f. Its squared norm is
<k,(S tensor S)k>. The positive tensor comparison S<=Sigma from
L190 gives S tensor S<=Sigma tensor Sigma: expand their difference
as (Sigma-S) tensor Sigma+S tensor (Sigma-S). This comparison is
valid for signed k and singular S, without comparing matrix entries.

L190(5), imported from L166's complete relative Green estimate, gives

    |Sigma_ef|<=C[(1+dist(e,f))^-2+N^-2]

on every variable row; different components have zero covariance.
Each cross-placement second moment for q is therefore bounded by
C B_N^2[(1+r)^-4+N^-4], where r is the anchor distance. The estimate
uses (x+y)^2<=2(x^2+y^2) and bounded stencil radii. At radius m the
number of anchors is at most C(1+m)^3. Consequently its sum for a
fixed placement is at most C log(eN)+C N^4 N^-4. Multiplication by
the O(N^4) placements and taking a square root proves (7).
Only two distinct colors occur, so no within-placement contraction
is missing. Boundary stencils and the finite-size Green correction
are retained in this count.

For a fixed output color c and deterministic link vector n, write
n^(c) for that vector in color c, zero in other colors. Differentiating
(2) leaves precisely a bilinear polynomial in the other two colors.
L190's local word count bounds coefficients per action placement by
C and per residual placement by C N. Differentiation in n^(c)
multiplies these bounds by at most C||n||_infinity, because each
stencil has bounded size. Equation (7) gives

    ||d script S_3[n^(c)]||_2
        <=C ||n||_infinity N^2 sqrt(log(eN)),
    ||d script R_3[n^(c)]||_2
        <=C ||n||_infinity N^3 sqrt(log(eN)).             (8)

The directions need only have bounded amplitude. No smooth extension
across the upper forest jump is used for (8).

### 2. A quadratic prefix test and the complete external spectrum

Set K=Phi S Phi^T. L182 gives ||K||_HS<=C N^4 and
||S||_HS<=C N^2 sqrt(log(eN)). For every fixed color c and vector y,
the same bounded-degree matrix estimates as L182(14)–(15) give

    ||<y,b^c>||_2
      <=C ||y||_infinity
             [(||S||_HS ||K||_HS)^(1/2)+||K||_HS]
      <=C ||y||_infinity N^4.                           (9)

Here is why that argument applies to this quadratic rather than
presuming independence of z and Phi z. Expand its two bracket terms
as bilinear forms between z and Phi z, or between two copies of
Phi z, in their distinct input colors. The corresponding matrices
have norm at most C||y||_infinity: D and q have bounded degrees on
the complete pinned complex. In whitened Gaussian coordinates the
second-chaos norm is bounded by sqrt(2) times the independent-copy
bilinear norm, by orthogonal symmetrization and Isserlis' theorem.
The independent-copy squared norms are bounded respectively by
C||y||_infinity^2 ||S||_HS ||K||_HS and
C||y||_infinity^2 ||K||_HS^2. The triangle inequality proves (9).
This changes neither the actual law nor any term of the expectation.

Use L185's exact spectral expansion, including both probe stencils,

    B_i=a^2 sum_(k,l) d_(i;kl) e_k e_l^T,
    sum_(k,l)|d_(i;kl)|p(k)p(l)<=C_(i,p)                 (10)

for every fixed polynomial p. The ordinary normalized Hodge modes
are e_k=a^2 f_k; all component labels and allowed constant indices
remain. Put n_k=S e_k and m_k=T n_k=M e_k. L185(5)–(6) and
L193(4)'s eigenspace estimate imply

    ||e_l||_infinity<=C a^2,
    ||n_k||_infinity<=C p(k),
    ||m_k||_infinity<=C a^2 p(k).                        (11)

For the middle bound, S e_k=lambda_k^-1 P f_k, where lambda_k is
the physical eigenvalue. Projection stays within its complete Hodge
eigenspace; its dimension and every product-mode amplitude are
polynomially bounded in k, as proved in L193. This uses no supremum
contraction property for P. The last bound is L185's actual smooth
tilt estimate, only for M e_k, in its original order. In particular
(9) gives ||<e_l,b^c>||_2<=C N^2.

### 3. Contract the smooth external leg before differentiating rho_H

At fixed mesh ordinary Gaussian integration by parts is valid even
for singular S by taking a Gaussian linear image. The polynomial
b^c contains only the other two colors. Therefore its derivative
in color c is identically zero. For every k,l,c,

    E[(e_k^T z^c)<e_l,b^c> rho_H]
       =E[<e_l,b^c> d rho_H[n_k^(c)]],

    d rho_H[n^(c)]
       =d script R_3[n^(c)]
          -d^2 script S_3[n^(c),Tz]
          -d script S_3[(Tn)^(c)].                     (12)

All maps act identically in color. In particular the last derivative
arises from differentiating t=Tz; it is not omitted. The middle
derivative keeps n fixed and retains both remaining rough slots.

To bound that middle polynomial, whiten S on im P, writing z=Z xi
and ZZ^T=S. The tilt on the whitened coordinates is the real
symmetric matrix E=2Z^T A Z, of norm at most C N by L190, section 3.
The two-color quadratic q=d script S_3[n^(c)] has coefficient tensor
k in these coordinates and ||q||_2=||k||_HS. Acting with Tz on its
two input slots applies E in each tensor factor, with total norm at
most 2||E||. Thus

    ||d^2 script S_3[n_k^(c),Tz]||_2
          <=C N ||d script S_3[n_k^(c)]||_2
          <=C p(k) N^3 sqrt(log(eN)).                  (13)

The direction n_k is not differentiated in this step; the separate
m_k term in (12) has already accounted for that change. Equations
(8),(11) give the same bound for d script R_3[n_k^(c)], while

    ||d script S_3[m_k^(c)]||_2
           <=C a^2 p(k) N^2 sqrt(log(eN))
           <=C' p(k) sqrt(log(eN)).                    (14)

Substitute (12) into J=2a^2 sum_kl d_(i;kl) sum_c
(e_k^T z^c)<e_l,b^c>. Cauchy–Schwarz, (9), (13)–(14) and the
complete sum (10) prove (3), since a^2 N^2=64. The contribution
of the last term in (12) is at most C_i sqrt(log(eN)). This proves
its asserted subcubic property. The other two terms retain the
logarithmic loss in (7); it is not replaced by a uniform constant.

### 4. Retain the common signed trace and its normalization

For any complete alternating cubic C with tensor c in convention
(2), Isserlis' theorem and L184's b tensor give

    E[J C]=6 sum_(e,a,b,c,d,f,g) B_ea (Gamma_e)_bc
                                  c_dfg S_ad S_bf S_cg.

There are six cross-pairings. The factor 1/6 in (2) cancels their
number, and the remaining epsilon contraction contributes 6.
Internal pairings vanish because they identify two distinct colors.
For a term SB=n y^T this contraction is

    6 sum_bc (Gamma_y)_bc (S c_n S)_bc
       =-6 Tr(J_y S c_n S).                            (15)

The minus sign uses skewness; inserting both P factors is exact
because S=PSP. Singular covariance causes no change to this finite
tensor identity.

The spatial tensor of d script S_3[Tz] applies T to each of its
three input slots. Its slice at n is consequently

    s_(Tn)+T^T s_n+s_n T.                              (16)

Since ST^T=TS=M, (15)–(16) give the sextic term per rank-one input

    -6 Tr(J_y S r_n S)+6 Tr(J_y S s_(Tn) S)
       +6 Tr(J_y M s_n S)+6 Tr(J_y S s_n M).

The last two traces agree: transpose the last, using J_y and s_n
skew and S,M symmetric, then cycle. Their sum is
12 Tr(J_y M s_n S). This equality adds the two rough placements;
it does not cancel them. L187(3) gives the entire third quartic
placement per rank-one input as -6 Tr(J_y M U_n^T).
Subtracting that placement and retaining -Q_1-Q_2 proves (4)–(5).
The exact product rule of L187 also permits, only within this
projected trace, U_n^T P=[diag(Vn)-V^T diag(Rn)]P. Both prefixes
and the upper pinned jump persist in this expression.

For (10), (4) reads a^2 sum_kl d_(i;kl) Z(n_k,e_l)-Q_1-Q_2.
L185–L186 bound the last two terms by O(N^(5/2)). No estimate of
Z by cancellation is asserted. Instead (3) and L187's O(N^(7/2))
quartic bound give the same O(N^(7/2)) bound for (4), since
sqrt(log(eN))<=C sqrt(N). L193's o(N^3) co-closed response proves
(6). None of these inequalities is a lower bound or a convergence
argument. Formula (5), rather than termwise removal, is the retained
finite starting point for a sharper joint test.

### 5. Exact checks and qualifications

Run from the notebook:

    python3 scripts/combined-ward-response/check_prefix_sextic_external_trace.py

The certificate is
scripts/combined-ward-response/prefix-sextic-external-trace-certificate.json.
It compares direct sparse polynomial derivatives and complete Gaussian
moments against (15), (16), the signed Q_3 trace and the full (4).
All ten exact rational comparisons pass, including singular supported
covariance. The direct sextic values are -176472 and -25920; subtracting
the complete quartics gives -120744 and -16794. Complete records and
the empty failure list were inspected. The four trace contributions,
including the separately retained smooth-tilt placement, are saved.

These are synthetic tensors and maps, without actual Wilson-action,
residual or probe identities. They check factors and matrix order,
not actual-probe coefficients, rates or the analytic bounds (3),(6).
Those bounds rely on the preceding all-mesh proof and its stated
upstream estimates. No finite fixture is used as evidence for growth
or failure of the requested limit. ATTEMPTS/039–043 remain unchanged.

## Mathlib

Full matching actual-probe bound, common trace and cutoff limit:
**not checked**. Supporting singular Gaussian, tensor comparison,
quadratic-chaos and finite trace coverage: **not checked**; unknown
coverage is not an absence claim. The standard input is the named
Isserlis Gaussian pairing theorem, as already used in L184 and L190.
Only its actual prefix/color specialization, singular covariance
justification and complete heat-sum application are supplied here.
No flow renormalizability theorem is reproved. The unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
covers the same bare joint-group target; a full renormalized
correlation theorem does not import its selected coefficient.
