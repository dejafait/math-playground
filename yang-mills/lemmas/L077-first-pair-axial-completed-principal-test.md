# L077 — Completing the frozen axial contraction leaves an N³ principal trace

## Hypotheses

This is a discriminating model for L076's unresolved high left trace,
not that trace or either actual probe coefficient. Keep a=8/N with
even N, all N component-1 axial edges, all N-1 transverse-component
axial vertex levels, and the complete axial Dirichlet matrix L_V from
L075. Let e_0=N^(-1/2)(1,...,1) and use the same E_0 embedding.

Use L008's fixed smooth even cutoff rho, equal to one on [-5/2,5/2]
and zero outside [-3,3]. At axial vertices set

    h_s=(-4+as)rho(-4+as), 1<=s<N, h_0=h_N=0.

This is the actual component-1 axial profile in L075, after freezing
its transverse factor at the central vertex. For this model only set
u_1=h_s, u_2=u_3=u_4=0. It is not the actual compact divergence-free
four-component displacement.

Freeze the transverse coefficients in L070's cell-center convention:
r=a² R, with R in R³, and exterior stored links av, with v in R³,
independent of axial level. Then t_1=0, t_2=a(v_mu+v_nu), and
t_3=a(v_nu-v_mu) in plane mu<nu. Centering these paths changes
nothing, since t_1=0 and D T=0. Use all three transverse planes.
To count frequencies, use a transverse periodic N³ grid solely in
this frozen diagnostic. No periodic boundary condition is substituted
in the actual pinned-box response.

Let K be the exact endpoint-averaged clover generator for these model
coefficients, L_0 the dimensionless four-dimensional curl energy, and
A_gen=(L_0 K+K* L_0)/2. The component covariances, path maps, G,
C_r and S have L070/L075's meanings with these model boundaries.
Write theta for a periodic transverse frequency and put

    d_j=2sin(theta_j/2), c_j=cos(theta_j/2),
    H=sum_j d_j², L=H I-d d^T,
    w=diag(c_j²)d, beta=L w, j=2,3,4.

Restrict the left trace to the fixed high-frequency band H>=1,
so G=H^-1 is always defined. The covariance on this frequency is
(L_V+H I)^-1 on every transverse component. Define the model trace

    F_N^gen=sqrt(N) Tr_(H>=1)
       [G C_r G E_0^T A_gen I_T Sigma_T D^T Q S],       (1)

where Q=M_(t_2) B_3-M_(t_3) B_2. Optionally replace A_gen by
A_gen+B_N, with any real symmetric full-link B_N satisfying
sup_N ||B_N||<infinity. In particular bounded dimensionless
curvature-form subtractions fit this qualification. This qualification
does not assert that the actual variable-coefficient residual differs
from this model by such a B_N.

## Conclusion

Set

    I_N=a² sum_(s=1)^(N-1) s h_s,
    I=integral_(-4)^4 x² rho(x) dx >0.

Each retained frequency has exactly the generator diagonal entry

    F_N^gen(theta)
      =2 I_N (R.(dc))(beta.(cv))/H².                   (2)

Here dc and cv are componentwise products. The complete axial inverse
and its upper-face correction have been retained before contraction;
the equality is an exact finite identity, not a bulk approximation.

Define the strictly positive constant

    gamma_1=(1/3) integral_(H>=1)
       [H sum_j d_j² c_j^4-(sum_j d_j² c_j²)²]/H²
                                           dtheta/(2pi)^3.

Then the band contains order N³ frequencies and

    N^-3 F_N^gen -> 2 I gamma_1 (R.v).                 (3)

For example R=v=(1,0,0) gives a strictly positive limit. Adding B_N
as above changes F_N by only O(N²), so does not change (3).

Thus neither the odd actual axial profile, the normalized constant
axial edge mode, nor retention of the full Dirichlet inverse forces
an O(N²) estimate for every frozen high-frequency circulation/path
composition. An absolute norm estimate discarding the actual exterior
signed contraction cannot use these features alone to gain a power.
This is new negative evidence about that proposed closure, extending
L070's test by its complete finite axial contraction.

It proves no N³ coefficient, sign, lower bound, failure of O(N²),
or logarithm for either actual probe. Variable transverse coefficients,
all displacement components, actual level-dependent exterior columns,
the complete heat sum and pinned transverse trace remain outside the
model. Their signed cancellations can still remove its mechanism.
This is local REPRODUCTION under the unchanged SPECIALIZE assessment,
not a result beyond the literature checked or a Yang–Mills disproof.

## Proof

### 1. Retain the axial generator outputs and curl energy

Work in one transverse Fourier mode. L066's generator symbol and
L065's finite axial averaging conventions give, on a pure component-1
constant axial input y=E_0 phi,

    (K y)_1=0,
    (K y)_T=-(i/(a sqrt(N))) h_s w phi.

Indeed C_1 e_0=N^-1/2 at every interior axial vertex. Each transverse
output includes its clover and endpoint averages, hence c_j² d_j.
There is no deletion of an axial endpoint or replacement of C_1.
The whole component-1 output row of K is zero, since all u_j with
j!=1 are zero in this explicitly defined model.

The constant axial edge mode has zero axial derivative, so
L_0 y=E_0 H phi, with zero transverse components. Consequently
K* L_0 y=0. On a transverse-only input the transverse output block
of L_0 is L_V I+L. Its axial off-block output need not vanish, but
is not in I_T^T A_gen y. Therefore

    I_T^T A_gen E_0 phi
      =-(i/(2a sqrt(N)))
                   [(L_V h)_s w+h_s beta] phi.         (4)

This keeps the axial derivative of h. Replacing (4) by only its
h_s beta term would not be the exact finite generator contraction.
Symmetry gives the reverse row by conjugate transpose, with +i.
The formula is valid on the two end levels because L_V and h have
the specified pinned zero endpoint values.

### 2. Contract the full inverse before taking a limit

The exact right path identity in L070, including all three planes, is

    D^T Q T=2a L diag(c_j) v.

Its constant-exterior circulation t_1 vanishes, so it also describes
the centered circulation/path term. In S the remaining axial factor
is s. Let b_s=s and f=(L_V+H I)^-1 b, the complete profile in L075.
Then the right column in (1), on this mode, is exactly

    x_s=2a f_s L diag(c_j) v.                           (5)

No transverse eigenvalue zero occurs in the selected band. Formula
L075(1) gives f_s=(s-N g_s(H))/H with its upper Dirichlet correction;
we do not discard that term. Algebraically (L_V+H I)f=b.

Use L beta=H beta and w^T L=beta^T. Contracting the reverse of
(4) with (5) gives

    E_0^T A_gen I_T x
      =(i/sqrt(N))(beta.(cv))
                      sum_s [(L_V h)_s+H h_s] f_s.

The two left Green weights and skew matrix have symbol

    G C_r G=-2i a²(R.(dc))/H².

Thus the sqrt(N) in (1) cancels the normalized axial embedding
exactly. Because L_V is the full finite symmetric pinned matrix,

    sum_s [(L_V h)_s+H h_s] f_s
       =sum_s h_s [(L_V+H I)f]_s
       =sum_s s h_s.                                  (6)

This is finite matrix integration by parts, including both end rows.
It cancels the inverse after contraction with the whole curl-energy
block. It neither commutes a variable transverse multiplier through
that inverse nor asserts a corresponding identity for the actual
four-component residual. Substituting (6) proves (2) with its sign
and all powers of a and N retained.

For sufficiently fine N the moment in (6) is positive even before
passing to a limit: pair s and N-s, use h_(N-s)=-h_s and h_s>0
at some levels s>N/2 in the affine core. Their contribution is
(2s-N)h_s>0. The central level has h_s=0.

### 3. Count the actual high lattice frequencies of the model

Since I_N=a sum_s (as)h_s, the Riemann-sum theorem gives

    I_N -> integral_0^8 d(d-4)rho(d-4) dd
           =integral_(-4)^4 x²rho(x) dx = I.

The term 4xrho(x) integrates to zero by evenness. Positivity is
strict since rho=1 on a nonempty interval. This limit retains the
transition region; it does not use only the affine core.

Let S_0=sum_j d_j² c_j². The coefficient of R_j v_k in (2), apart
from 2I_N, is

    d_j c_j d_k c_k (H c_k²-S_0)/H².

It is odd in theta_j for j!=k. The band H>=1 is invariant under
coordinate sign changes and permutations, so off-diagonal integrals
vanish and diagonal integrals agree. Their sum is

    V(theta)=[H sum_j d_j² c_j^4-S_0²]/H².

This is the variance of c_j² with weights d_j²/H, hence V>=0.
At theta=(pi/2,pi,0), H=6 and V=1/18. Continuity supplies a
positive-measure neighborhood within the band, giving gamma_1>0.
This repeats only the elementary angular algebra from L070 for the
explicitly selected band, not a renormalization theorem.

The summand is bounded and smooth where H>=1. Its indicator has
discontinuities only on H=1, a measure-zero smooth surface: all
components of grad H vanish simultaneously only when each theta_j
is 0 or pi, where H is a multiple of 4. The displayed scalar is
periodic (d_j c_j=sin(theta_j), and all remaining factors involve
squares). Consequently the uniform N³-point periodic Riemann sum,
divided by N³, tends to its normalized torus integral. Applying the
parity and permutation argument just given proves (3). For R.v>0,
F_N^gen is therefore Theta(N³), above the proposed O(N²) threshold
for this model. It is not a lower bound for the actual pinned trace.

### 4. Bounded curvature subtractions cannot change this model limit

For H>=1, positivity of L075's full inverse gives 0<f_s<=s/H.
Hence (5) obeys ||x||_2<=C a N^(3/2)|v|. The magnitude of the
left scalar G C_r G is at most C a² |R| on this band, and E_0 is
an isometry. The diagonal perturbation from B_N in one trace mode
is thus bounded by

    sqrt(N) C a² |R| ||B_N|| C a N^(3/2)|v|
                   <= C a³ N² = O(N^-1).

There are at most N³ selected modes, giving O(N²) in total.
This norm argument permits transverse mode mixing in B_N; none is
moved through G or Sigma_T. Dimensionless curvature forms have
bounded norms by the finite incidence/average formulas in L028/L066,
so they fit the assumption when defined in this diagnostic geometry.
It gives no bound for the omitted leading variable-coefficient
generator terms in the original geometry.

The actual coefficients r_k/a² and exterior path columns/a are not
constant R and v. Their exterior heat-weighted signed contraction,
the other displacement components and all actual axial profiles
must be retained to test whether the N³ mechanism survives. L076's
small left sector is distinct from this fixed high-frequency band
and supplies no identification. Centered path/path, exterior defect,
pinned remainder, all nine placements and other response jets remain
unresolved; the shared quartic must still be subtracted exactly once.
No mathematical script or numerical evidence is used in this proof.

## Mathlib

Coverage of the full specialized frozen axial diagnostic: **not
checked**. Supporting finite Fourier diagonalization, symmetric
matrix identities, Cauchy–Schwarz and Riemann sums: **not checked**.
No matching theorem or absence claim is made. The ready assessment
`drafts/literature/2026-09-26-current-target.md` covers the combined
response target; general perturbative flow finiteness and stress
matching are not reproved or used to assign an actual coefficient.
