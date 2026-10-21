# L066 — A retained transverse packet obstructs a uniform mixed residual bound

## Hypotheses

Use L018's dimensionless ordinary full-link coordinates, L008's actual
compact displacement, L009's endpoint-averaged clover generator and
both actual curvature forms, with relative fixed-link boundaries on
(-4,4)^4. Let a=8/N through sufficiently fine admitted even meshes,

    A_0=(L_0 K_a+K_a^T L_0)/2-Q_3-Q_6,  L_0=D_1^T D_1,
    Sigma=(D_1^T D_1+D_0 D_0^T)^(-1).

Let I_T insert components 2–4, Sigma_T=I_T^T Sigma I_T, and
Delta_T=Sigma_T^(-1), the full four-dimensional transverse-component
Hodge block. This Delta_T is not a three-dimensional edge Laplacian.
Let E_0 and G=Delta_3^(-1) be L040's normalized constant axial
component-1 embedding and pinned transverse vertex inverse.

## Conclusion

For constants c,C>0 independent of N, the actual block satisfies

    R_0T=G^(1/2) E_0^T A_0 I_T Sigma_T^(1/2),
    c/a <= ||R_0T|| <= C/a                              (1)

for all sufficiently fine admitted meshes. In particular the O(1)
extension of L065 to the direct transverse input is false. The lower
bound retains the actual coefficients: it is not a frozen-coefficient
counterexample substituted for them. A compact right axial profile
avoids the zero axial mean of u_1.

This is an obstruction to a uniform full-vector residual norm, not
to a signed estimate of L064's contractions, an a²-scaled cancellation,
or the Yang–Mills target. It computes no mixed-response coefficient or
logarithm. It is local specialization/reproduction of finite stencil
and oscillatory test methods under the saved response assessment;
no originality beyond the inspected sources is claimed.

## Proof

### 1. Test the exact dual energy inequality

L026's relative tensor spectrum makes Sigma block diagonal in link
components. For transverse vertex phi and full transverse-component
field x, finite-dimensional change of variables gives

    ||R_0T|| >= |(E_0 phi)^* A_0 I_T x|
                 /sqrt[(phi^* Delta_3 phi)(x^* Delta_T x)].       (2)

Indeed test R_0T against G^(-1/2)phi on the left and
Sigma_T^(-1/2)x on the right. These are invertible positive matrices.
Complex test fields are legitimate here: the norm of a real matrix on
its complexification equals its real norm, since
||R(v+iw)||²=||Rv||²+||Rw||². All energies below are Hermitian ones.
No positivity of A_0 is used.

### 2. Compute the load-bearing frozen symbol

Use staggered cell-center phases, and put

    d_j=2 sin(theta_j/2), c_j=cos(theta_j/2), H=sum_j d_j².

An incidence from vertices to edges has symbol i d_j; its adjoint
has symbol -i d_j. A centered average in either direction has symbol
c_j. In this convention the dimensionless curl energy has matrix

    L_0(theta)=H I-d d^T.

For frozen real u, the exact generator on a pure component-1 input is

    K_11=(i/a)c_1² sum_(j!=1) u_j c_j d_j,
    K_j1=-(i/a)u_1 c_j² c_1 d_j  (j!=1).

The two c_j factors in K_j1 come respectively from the clover and
output endpoint average; they must both be retained. Likewise
K_12=-(i/a)u_2 c_1² c_2 d_1. At

    theta=(0,pi/2,pi,0),
    d=(0,sqrt(2),2,0), c=(1,1/sqrt(2),0,1), H=6,

one has K_21=-i u_1/(sqrt(2)a), K_31=K_41=K_12=0.
Moreover L_21=L_31=L_41=0 and L_22=4. Consequently

    [(L_0 K+K^* L_0)/2]_21=-i sqrt(2)u_1/a.              (3)

There is no contribution of K^* L_0 to this entry, because its only
possible nonzero L_r1 has r=1 and K_12=0. Other generator outputs
were included in L_0 K; the zero K_31,K_41 follows from this carrier,
not an input/output deletion. The direction-dependent averages make
K_(T,1) fail to be a discrete gradient, so transverse curl energy
does not annihilate it. Q_3 and Q_6 have uniformly bounded operators
in these dimensionless coordinates, by their actual bounded weights
and finite incidence/average norms (L008, L028). They are not part
of the 1/a principal term and are retained in the remainder below.

### 3. Localize the carrier and control every discarded order

Define b(t)=exp[-1/(1-t²)] for |t|<1 and zero otherwise, and set

    eta(z_2,z_3,z_4)=b(z_2/2)b(z_3/2)b(z_4/2),
    h(z_1)=b((z_1-5/4)/(3/4)),
    J_eta=integral eta²>0,
    J_1=integral z_1 h(z_1) dz_1>0,
    J_2=integral h(z_1)² dz_1>0.

The transverse support lies in (-2,2)^3, and h is supported in
(1/2,2). On a neighborhood of their joint support L008's actual
discrete displacement is exactly u_a=(z_1,z_2,-z_3,-z_4) for small a:
all central-difference coefficient stencils lie in the core where
rho=1. In particular u_(a,1)=z_1 there.

Index transverse vertices by j_2,j_3,j_4 in {1,...,N-1} and use
z_j=-4+a j. Let

    phi_N(j_T)=a^(3/2) eta(z_T) exp[i(pi j_2/2+pi j_3)],
    y_N=E_0 phi_N.

Thus y_N has component 1 only, constant over all N axial edges,
with entries phi_N/sqrt(N), including both normal end edges.
For the right field take component 2 only, at its midpoint grid:

    (I_T x_N)_2(j_1,r_2,j_3,j_4)
       =-i a^(3/2)/sqrt(N) h(z_(j_1))
          eta(-4+a(r_2+1/2),z_(j_3),z_(j_4))
          exp[i(pi(r_2+1/2)/2+pi j_3)],                  (4)

where j_1,j_3,j_4 are interior vertices and 0<=r_2<N. All other
components are zero. This is an admissible relative field: its normal
end edges are retained and vanish by the compact envelope, and its
tangential boundary values vanish. These packets are fields in the
full finite spaces, rather than a truncated covariance or spectral
replacement. In particular all right axial modes needed to express
h remain available.

Here is a uniform error justification for applying (3) to these
packets. The generator part of A_0 is a finite sum of fixed bounded
shifts/averages/incidences with one u coefficient and one factor 1/a.
In the adjoint compositions that coefficient may occur at a shifted
vertex. Every u_a has a uniform physical Lipschitz bound (L028), so
replacing its shifted value by its value at the output costs O(a).
For each fixed staggered shift delta, the mean value theorem similarly
gives eta(z+a delta)-eta(z)=O(a), uniformly; the carrier phase itself
is transformed exactly. The entry amplitude is

    b_N=a^(3/2)/sqrt(N)=a²/sqrt(8).

The error in each such 1/a term is therefore at most C b_N per
entry. There are O(N^4) entries and finitely many shifts, so its
ordinary l² norm is O(b_N N²)=O(1). All coefficient stencils are
away from the faces; zero extension computes their finite-domain
action exactly. Thus it introduces no artificial periodic or boundary
term. The coefficient derivatives in K_a^T L_0 are precisely included
by the shifted-coefficient estimate. Finally ||y_N||=O(1), and the
actual bounded Q_3,Q_6 contribute O(1) in l² as well. This proves

    (A_0 y_N)_2=-i sqrt(2)u_(a,1)/a times
       [b_N eta(z_T) exp(i(pi(r_2+1/2)/2+pi j_3))]
       +epsilon_N,  ||epsilon_N||_2<=C.                 (5)

For u_(a,1) at a component-2 midpoint one may choose either adjacent
vertex extension: their difference is O(a), already included above;
on the support of x_N both are exactly z_1. Formula (5) holds
globally with the smooth coefficient extension. No smooth-field
consistency claim is applied to the oscillating carrier.

Also ||x_N||=O(1), by its compact envelopes and b_N scaling. Pair
(5) with (4). The conjugate of -i in x_N is i, so the leading term
is positive. Since aN=8, ordinary Riemann sums on the indicated
vertex/midpoint grids give

    a x_N^* I_T^T A_0 y_N -> (sqrt(2)/8) J_1 J_eta>0.     (6)

The contribution of epsilon_N is O(a) by Cauchy–Schwarz.
Hermitian symmetry gives the conjugate limiting value for the
numerator in (2). The zero axial mean of u_1 does not affect (6):
it is weighted by the actual retained h, rather than averaged
against a constant right axial input.

### 4. Retain the complete relative energies

The same finite-shift estimate without the factor 1/a shows that
incidence applied to each packet equals its carrier symbol times
the appropriate shifted envelope, with l² error O(a). For phi_N the
three transverse carrier squares sum to 2+4+0=6. For x_N the full
four-dimensional component Hodge energy is the sum of the three
pinned vertex-direction energies and the own-direction edge energy,
as in L026. Its carrier squares again sum to 6; its axial and fourth
direction differences have O(a) norm. Compact support of x_N ensures
that the own-direction adjoint incidence retains all end edges and
creates no additional endpoint contribution. Therefore

    phi_N^* Delta_3 phi_N -> 6 J_eta,
    x_N^* Delta_T x_N -> (6/8) J_2 J_eta.                 (7)

The second factor 1/8 comes from N^(-1) times the axial vertex sum,
not from a change of covariance. Equations (6)–(7) show that this
specific dual ratio D_N satisfies

    a D_N -> c_0=sqrt(2) J_1/[6 sqrt(8 J_2)]>0.           (8)

For example choose c=c_0/2 for all sufficiently fine meshes.
Equation (2) now proves the lower bound in (1) analytically.

For completeness, L020, proof section 3, equation (11), gives the
full whitened residual ||Sigma^(1/2) A_0 Sigma^(1/2)||<=C/a;
the physical/dimensionless scale identification is L064(7).
The block-diagonal spectrum and zero-mode relation give exactly

    R_0T=E_0^T [Sigma^(1/2) A_0 Sigma^(1/2)] I_T,

because Sigma^(1/2)E_0=E_0G^(1/2) and
Sigma^(1/2)I_T=I_T Sigma_T^(1/2). Both embeddings are isometries.
This proves the upper bound. It is an import of the existing generic
estimate, not a second analysis of the complete response.

### 5. Verification and downstream qualification

Run from the notebook:

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/combined-ward-response/check_mixed_transverse_residual.py

The full certificate is
`scripts/combined-ward-response/mixed-transverse-residual-certificate.json`.
For N=24,32,40,48 the dual ratios are respectively 0.2804705,
0.4027292,0.5167191,0.6326725; their a multiples are 0.09349017,
0.10068231,0.10334382,0.10544542. The complete two-generator-pairing
minus Q_3/Q_6 decomposition agrees with the actual residual to defects
at most 3.74e-17, versus 1e-10 required, with no failures. The actual
a-scaled pairings approach their positive Riemann predictions. These
binary64 diagnostics check signs, phases and stencil composition;
sections 1–4, not those finite values, prove the asymptotic obstruction.

L065's bounded component-1 block remains valid. This result stops its
uniform full-vector extension. It does not make the actual path/path
trace large: L064 additionally composes the right paths, co-closed
K_1, endpoint multipliers, covariance and signed heat coefficients.
A sharper estimate must use that actual composition or signed sum,
rather than assume an O(1) R_0T. The first pair and all other response
groups remain unresolved. All nine placements must return for
subleading powers and logarithms. No conditional sign is assigned to
the mixed response and no shared quartic is counted twice. The
interacting reflected error <=c_box/2, continuum construction, full
reflection positivity, infrared limit and finite positive mass remain
separate open requirements.

## Mathlib

Coverage of the full retained mixed-block obstruction: **not checked**.
Supporting finite spectral calculus, matrix norm duality, complexification
of real operators, finite-shift estimates and Riemann-sum convergence:
**not checked**. No matching theorem or absence claim is made. General
flow renormalizability and stress matching remain precise source imports
in the saved assessment; this proof addresses the actual stencil
specialization, not those general theorems.
