# Lemma 643: a density saving for the fixed vertical Pick annulus majorant

## Hypotheses

All logarithms are natural. Use L018's actual Xi, zero correspondence
and symmetries, retaining every zero occurrence with its multiplicity.
Use L467's closed unit-shell upper count and the finite rational
identities and concentration-space construction in L641. Explicitly,

    T sufficiently large, N=floor(log T), a=3/2,
    u_j=j/N-1/2 (0<=j<N), I=[-1,1],
    Q_N(z)=product_(j<N)(z-u_j+ia),
    B_N(z)=product_(j<N)(z-u_j-ia)/(z-u_j+ia),
    H_N={P/Q_N: deg P<N},
    ||h||^2=integral_R |h(x)|^2 dx/(2pi).

Let P_N be the boundary orthogonal projection onto H_N, and let E_N
be the spectral subspace of A_N=P_N 1_I P_N|_(H_N) for eigenvalues
at least 1-N^(-1/2). Write d_N=dim E_N and k_E for its reproducing
kernel with this norm. This is L641's fixed E_N, independent of X;
no X-dependent zero constraints are imposed in its definition. The
only finite-space facts imported from L641 are its kernel identity,
boundary diagonal and the leakage inequality for E_N. Its favorable
height and exterior countervectors are not inputs to this proof.

Import the following uniform, unconditional primary density theorem:
S. A. C. Baluyot, *On the Zeros of Riemann's Zeta-function*, PhD thesis,
University of Rochester (2017), Section 1.2, Theorem 1.2.1, printed
p.16 ([repository record](https://hdl.handle.net/1802/32855),
[primary PDF](https://urresearch.rochester.edu/fileDownloadForInstitutionalItem.action?itemFileId=183460&itemId=33320)):

    N_zeta(sigma,H) <<_theta H^[1+theta(1-2sigma)] log H,
    fixed 0<theta<4/7, uniformly sigma>=1/2, H large.          (1)

Here N_zeta(sigma,H) counts beta>sigma, 0<gamma<=H with zero
orders. The saved assessment inspected its near-line proof cases in
Section 3.2, pp.111--114, and Section 3.6, pp.140--143, including
the total-count case within 1/log H. The arithmetic source proof is
imported, not independently audited here. Fix theta=11/20 throughout;
this is less than 4/7. No effective onset is claimed.

The standard finite model-space formulas underlying L641 are in
Baranov--Zarouf, [arXiv:1310.1182v1](https://arxiv.org/pdf/1310.1182v1),
Section 1.1, and Baranov--Jaming--Kellay--Speckbacher,
[arXiv:2304.02385v2](https://arxiv.org/pdf/2304.02385v2), Section 3.1,
(3.1)--(3.3). The standard model conjugation is discussed in
Camara--Klis-Garlicka--Lanucha--Ptak, *Conjugations in L^2*, Analysis
and Mathematical Physics **10**, 22 (2020),
[Section 4 preceding Proposition 4.1](https://link.springer.com/article/10.1007/s13324-020-00364-5).
The Poisson input is the upper-half-plane Poisson integral theorem,
*Complex Analysis*, [Theorem 10.3.1](https://complexanalysis.org/web/sec_poisson-integral-formula.html).
We verify the rational half-plane conjugation and Poisson specialization
below to fix the normalization, eigenspace invariance and interval-edge
loss. These are applications of known tools, not new general theorems.

No RH, simplicity, zero spacing, general weighted Maples--Rodgers
estimate, positive paired zero measure or new zero-density theorem is
assumed. L641's finite kernel, boundary diagonal and E_N leakage inputs
are checked in the scoped audit below; its other arguments are not
certified by this result.

## Conclusion

For real x,y with |y|<1/2 define

    F_N(x,y)=sqrt(k_E(x+iy,x+iy) k_E(x-iy,x-iy)),
    W_T=(1/T) integral_T^(2T)
          sum_(zeta: 1<|Re(zeta)-(X+1/2)|<sqrt(N))
             F_N(Re(zeta)-(X+1/2),Im(zeta)) dX.               (2)

The sum is over all actual Xi zero occurrences. Then

    W_T = O(N^(2-1/80)) = o(N^2).                           (3)

The constant is independent of T and X, but includes the constant
and existential onset in (1) for the one fixed theta=11/20. More
precisely, displacements |Im(zeta)|<=delta_N contribute
O(N^(141/80)), where delta_N=(log N)/(4N); the other displacements
contribute O(N^(159/80)). Critical-line atoms are in the first part.

This local standard-tool specialization passed the scoped conceptual
audit below on 1 November 2026, with the estimate unchanged. It treats
the exact nonnegative majorant nominated after L642 and supplies a
mean estimate, not a signed eigenvalue or RH result. Simultaneous
selection of a height with enough actual-zero nullspace dimension and
small full trace is a separate application, not proved here. The L642
distant-tail result is downstream context, not an input to (3).

## Proof

### Conjugation preserves the concentration subspace

For a polynomial P put P#(z)=overline(P(conjugate(z))), and similarly
for Q_N. Thus B_N=Q_N#/Q_N. If f=P/Q_N belongs to H_N, set

    (Jf)(z)=B_N(z) overline(f(conjugate(z)))=P#(z)/Q_N(z).    (4)

The equality is a rational identity, so any removable expression in
the first formula is interpreted by the last formula. It shows that
J preserves H_N and J^2=1. On the real boundary |B_N|=1, hence J
is an antilinear isometry. Extend J to the ambient boundary L2 by
Jf(x)=B_N(x)overline(f(x)). It is an antiunitary involution there,
and it preserves H_N and its orthogonal complement. Consequently
J commutes with P_N. It also commutes with multiplication by the
real function 1_I. Thus J A_N=A_N J. Since the eigenvalues of A_N
are real, each eigenspace is invariant, and so is E_N.

If f_1,...,f_d is an orthonormal basis of E_N, then Jf_1,...,Jf_d
is another. For 0<=y<=1/2 and z=x-iy, summing the squared absolute
values in (4) therefore gives

    k_E(x-iy,x-iy)=|B_N(x-iy)|^2 k_E(x+iy,x+iy).

All evaluations are finite: the poles have imaginary part -3/2.
Put

    L_N(x,y)=log|B_N(x-iy)|
      =(1/2) sum_(j<N)
          log[((x-u_j)^2+(a+y)^2)/((x-u_j)^2+(a-y)^2)].

Then L_N>=0, and the exact majorant identity is

    F_N(x,y)=exp(L_N(x,y)) k_E(x+iy,x+iy),  0<=y<=1/2.       (5)

This identity uses invariance of E_N, not invariance of the generally
different constrained space U_X. It concerns the positive majorant;
it does not replace a mixed zero contribution by a modulus square.
By definition F_N(x,-y)=F_N(x,y).

### The distinct-pole product has growth coefficient below density decay

Set rho=21/20. Uniformly for |x|>=1, 0<=y<=1/2, we claim

    L_N(x,y) <= rho N y+2y,                                 (6)
    L_N(x,y) <= 3Ny/[ (|x|-1/2)^2+1 ].                       (7)

To prove (6), differentiate the finite logarithmic sum in y. With
0<=v<=1/2 its individual derivative, at d=x-u, is

    psi(d,v)=(a+v)/(d^2+(a+v)^2)
                       +(a-v)/(d^2+(a-v)^2).

It is positive, even in d, decreasing in |d|, and at most 2, since
1<=a-v<=a+v<=2 and each summand is at most its reciprocal height.
On -1/2<=u<=1/2 the function psi(x-u,v) is monotone for |x|>=1.
The left-endpoint Riemann sum on the N intervals of length 1/N is
at most its integral multiplied by N plus 2: for an increasing
function the error is nonpositive; for a decreasing function the
error is at most its endpoint difference, which is at most 2.
This proves the uniform discretization estimate

    sum_(j<N) psi(x-u_j,v)
        <=N integral_(-1/2)^(1/2) psi(x-u,v) du+2.           (8)

The integral is largest at |x|=1, by evenness and monotonicity in
|d|. Its value there is g(a+v)+g(a-v), where

    g(t)=arctan(3/(2t))-arctan(1/(2t))
        =arctan[t/(t^2+3/4)],  1<=t<=2.

The argument of arctan decreases on [1,2], since its derivative
has numerator 3/4-t^2. Hence g(t)<=arctan(4/7). For r=4/7,
the elementary integral inequality
1/(1+s^2)<=1-s^2+s^4, 0<=s<=r, gives

    2 arctan(4/7)
      <2(r-r^3/3+r^5/5)=262904/252105<21/20.                (9)

The final comparison is exact: 21*252105-20*262904=36125>0.
Integrate (8) from v=0 to y, using L_N(x,0)=0. This proves (6).
For (7), each denominator in psi is at least
(|x|-1/2)^2+1, while its two numerators sum to 2a=3. Integrating
this bound proves (7). Both estimates keep the full moving grid.

The full H_N kernel from L641 also yields a useful spatial envelope.
For y>0, its diagonal identities and
B_N(x-iy)=1/overline(B_N(x+iy)) give

    k_H(x+iy,x+iy)=(1-exp(-2L_N))/(2y),
    k_H(x-iy,x-iy)=(exp(2L_N)-1)/(2y).

Projection contraction gives k_E(z,z)<=k_H(z,z), so

    F_N(x,y)<=sinh(L_N(x,y))/y
       <=3N exp(rho Ny+2y)/[(|x|-1/2)^2+1].                 (10)

Here sinh L<=L exp L for L>=0 and (6)--(7) were used. At y=0
the same bound follows directly from L641's boundary diagonal

    k_H(x,x)=sum_(j<N) 3/[(x-u_j)^2+9/4].

Since integral_(|x|>1) dx/[(|x|-1/2)^2+1]<pi, (10) implies

    J_N(y):=integral_(|x|>1) F_N(x,y) dx
          <=3pi e N exp(rho Ny),  0<=y<=1/2.               (11)

The same notation J_N will also be bounded more sharply at small y.
In particular there is no factor sqrt(N) from the spatial annulus.

### Poisson transport retains concentration near zero displacement

Every f in H_N is bounded and analytic on the closed upper half-plane,
has continuous boundary values, and is O(1/|z|) at infinity there.
Its Poisson representation, with P_y(s)=y/[pi(s^2+y^2)], is

    f(x+iy)=integral_R P_y(x-t) f(t) dt,  y>0.

For this rational specialization the formula can also be verified
directly: write the kernel as (2pi i)^(-1)
[(t-x-iy)^(-1)-(t-x+iy)^(-1)], multiply by f(t), and close in
the upper half-plane. There is exactly the pole t=x+iy with residue
f(x+iy)/(2pi i); all poles of f are below the real axis, and the
semicircle integral tends to zero. This checks applicability and the
normalization without assuming a uniform shifted-concentration theorem.
Because P_y>=0 and its integral is one, Cauchy--Schwarz gives

    |f(x+iy)|^2 <= integral_R P_y(x-t)|f(t)|^2 dt.            (12)

Sum (12) over an orthonormal basis of E_N and use Tonelli. Write
K_N(t)=k_E(t,t) and p_y(t)=integral_(|x|>1) P_y(x-t) dx. Then

    integral_(|x|>1) k_E(x+iy,x+iy) dx
                       <=integral_R K_N(t) p_y(t) dt.       (13)

L641's leakage inequality and d_N<=N give

    integral_(|t|>1) K_N(t) dt <=2pi d_N N^(-1/2)
                                      <=2pi sqrt(N),
    K_N(t)<=k_H(t,t)<=4N/3.                                 (14)

For |t|<1,

    p_y(t)=(1/pi){arctan[y/(1-t)]+arctan[y/(1+t)]}.

At endpoints this has the continuous one-sided interpretation, and
endpoints have zero integration measure. For 0<y<=1/2, splitting
the following integral at s=y shows

    integral_(-1)^1 p_y(t) dt
       =(2/pi) integral_0^2 arctan(y/s) ds
       <=y+(2y/pi) log(2/y).                                (15)

Indeed arctan(y/s)<=pi/2 for 0<s<y and <=y/s for y<=s<=2.
On the exterior use only p_y<=1. Equations (13)--(15) imply

    integral_(|x|>1) k_E(x+iy,x+iy) dx
       <=2pi sqrt(N)+(4N/3)y[1+(2/pi)log(2/y)].              (16)

Combining (5), (6) and (16) now gives

    J_N(y)<=exp(rho Ny+2y)
          {2pi sqrt(N)+(4N/3)y[1+(2/pi)log(2/y)]}.           (17)

At y=0, J_N(0)<=2pi sqrt(N) by (14); this case is not discarded
by using a strictly off-line zero-density estimate.

Let delta_N=(log N)/(4N). For large N this is at most 1/2.
The function y[1+(2/pi)log(2/y)] is increasing on (0,1/2],
as its derivative is 1+(2/pi)(log(2/y)-1)>0. At y=delta_N,
N times this function is O((log N)^2). Since (log N)^2=O(sqrt(N)),
(17), including its separate y=0 limit, proves uniformly

    sup_(0<=y<=delta_N) J_N(y)
       <=C N^(rho/4) sqrt(N)=C N^(61/80).                  (18)

This keeps the entire interval-edge cost; a bare boundary norm
contraction would not justify (18) at complex points.

### Height averaging and all zero occurrences

For each actual Xi zero write zeta=gamma+i eta. L018 identifies
eta=1/2-beta and preserves multiplicity. If its term in (2) occurs
for any X in [T,2T], then

    T+1/2-sqrt(N)<gamma<2T+1/2+sqrt(N).

For sufficiently large T this entire padded interval lies in (0,3T).
There are finitely many zeros in the rectangle in question; thus
interchanging this finite sum and the X integral is justified. For
each zero, substitute x=gamma-X-1/2. Its X integral is over a
subset of 1<|x|<sqrt(N), with |dX|=|dx|. Since F_N>=0 and is
even in eta, it is bounded by J_N(|eta|). Therefore

    W_T <= (1/T) sum_(rho: 0<gamma<=3T) J_N(|beta-1/2|).     (19)

This enlarges the padded set but does not claim a short-interval
density theorem. L467's closed unit-shell count, summed over
0<=j<=ceil(3T), gives at most C T log T<=C T N zero occurrences
in (19). Overcounting integer endpoints is harmless. In conjunction
with (18), all terms with |beta-1/2|<=delta_N, including beta=1/2,
therefore contribute at most

    C N * N^(61/80)=C N^(141/80).                           (20)

For the remaining terms use finite displacement bands. Put
K=floor(N delta_N)=floor((log N)/4), which is at least 2 for large N.
For an occurrence with delta_N<y=|beta-1/2|<1/2, let k=floor(Ny).
Then K<=k<=floor(N/2), y>=(k/N)>(k-1)/N and y<(k+1)/N.
The first band may include extra core occurrences, which only
increases this nonnegative upper bound. L018's reflection
beta+i gamma -> 1-beta+i gamma preserves the ordinate and order.
Consequently the total number in this band is at most

    2 N_zeta(1/2+(k-1)/N,3T)
       <=C T log T exp[-(11/10)((k-1)/N)log(3T)]
       <=C T N exp[-(11/10)(k-1)].                          (21)

This is exactly (1) at theta=11/20. The lowering of the horizontal
threshold by 1/N ensures the strict beta>sigma convention includes
every band endpoint. The comparison log(3T)>=N and log T<N+1
is in the favorable direction, and all constants remain independent
of k and T. Both signs of displacement, every multiplicity and all
allowed endpoints have been retained. There is no critical-line
mass in these bands, since K>=2.

Equation (11) bounds the weight of each occurrence in band k by
C N exp[rho(k+1)]. Insert this and (21) into (19), and extend the
resulting finite geometric sum upwards:

    larger-displacement contribution
       <=C N^2 sum_(k=K)^infinity
                       exp[-(11/10)(k-1)+rho(k+1)]
       <=C N^2 exp[-K/20]
       <=C N^(2-1/80).                                     (22)

Here 11/10-rho=1/20>0 and K>=(log N)/4-1. No arbitrary-weight
consequence of an upper-tail density estimate was invoked: (21)--(22)
are explicit nonnegative band bounds. Combining (20) and (22) proves
(3), since 141/80<159/80<2.

The failure of boundary-only transfer in L641 is compatible with
this estimate: (21) uses extra actual-zero horizontal-density input
and averages heights. The deterministic near-annulus envelope in
L642 remains a valid but insufficient upper bound. Neither a full
constrained signed trace at an already selected height nor an
eigenvalue sign has been inferred from the nonnegative mean (3).

### Critical audit — 1 November 2026

**Verdict.** Equations (3), (18), (20) and (22) are retained under the
stated source imports. This checks the quantitative specialization and
its stated finite-space inputs, not the arithmetic density manuscript,
all of L641/L642, or a favorable-height/signed-eigenvalue application.
No repair of the exponent or hypotheses is required.

**Finite-space normalization and leakage.** In L641's displayed basis
each e_j has squared boundary norm

    (1/(2pi)) integral_R 2a/((x-u_j)^2+a^2) dx=1.

For j>k, e_j(x)conjugate(e_k(x)) cancels every upper half-plane
pole and is O(x^(-2)); its upper contour integral vanishes. Thus
these N functions form an orthonormal basis of H_N. Writing
b_j(z)=(z-u_j-ia)/(z-u_j+ia), the one-factor identity

    i[1-b_j(z)conjugate(b_j(w))]/(z-conjugate(w))
      =2a/[(z-u_j+ia)(conjugate(w)-u_j-ia)]

telescopes to the asserted kernel. Its real diagonal is the sum of
2a/((x-u_j)^2+a^2); its two nonreal diagonals are exactly those
before (10), with denominators 2y and no additional 2pi factor.
Both hold in |Im z|<=1/2, away from all zeros of Q_N and Q_N#.
For a unit f in E_N, the spectral definition gives

    <A_N f,f> >= 1-N^(-1/2).

Hence its exterior squared boundary norm is at most N^(-1/2).
Sum over d_N orthonormal vectors and restore
dx from dx/(2pi) to get (14). Only d_N<=N is used; L641's
concentration-dimension lower bound and favorable-height assertion
are not premises. If E_N is empty, W_T=0.

**Antilinear invariance.** Formula (4) sends P/Q_N to P#/Q_N,
without a disk or real-variable factor. The boundary J is an
antiunitary involution preserving H_N and its orthogonal complement,
so it commutes with P_N. The real indicator also commutes with J.
If A_N f=lambda f, then A_N Jf=conjugate(lambda)Jf=lambda Jf,
since lambda is real. This includes threshold eigenvalues and proves
invariance of E_N. Applying J to its orthonormal basis gives (5),
with one product factor. No invariance of U_X is assumed.

**Product growth and integrability.** The quadrature error in (8)
is at most 2 for both signs of x. The integral is even in x and
decreases for x>=1, since every distance x-u is positive and
increasing there. At |x|=1 the arctangent difference is in (0,pi/2),
so its subtraction formula has no missing branch. Its argument
decreases on [1,2] since t^2>3/4. For r=4/7 the doubled
polynomial integral is exactly 262904/252105, with positive gap

    21/20-262904/252105=36125/(20*252105).

Strictness follows from
1-s^2+s^4-1/(1+s^2)=s^6/(1+s^2)>0 for s>0.
Integrating the quadrature error gives 2y uniformly in N. Adding
the two positive numerators before bounding their denominators
proves (7). The spatial integral in (11) equals
pi-2 arctan(1/2)<pi; no sqrt(N) annulus loss occurs. The real
boundary diagonal handles y=0 without division by y.

**Poisson edge and limits.** For fixed N, f=P/Q_N is O(1/|t|)
on sufficiently large upper semicircles. The difference of the two
Cauchy kernels is O(1/|t|^2), so the displayed contour integrand is
O(1/|t|^3). Its only upper pole is t=x+iy, with the stated residue.
This proves the exact complex Poisson formula without a uniqueness
claim for unbounded harmonic functions. The contour limit is taken
for each finite N before uniform estimates, so a uniform-in-N
semicircle radius or decay constant is unnecessary.

Cauchy--Schwarz against the probability density P_y, the finite basis
sum, and nonnegative Tonelli integration give (13). Exterior t use
the full leakage and p_y<=1; interior t use K_N<=4N/3. The
interior integral is exactly (15)'s arctangent integral. Splitting
at s=y retains both edges and gives
y+(2y/pi)log(2/y); t=+/-1 has zero integration measure. Thus
(16)--(17) include the entire edge cost. For y<=delta_N,
exp(rho Ny)<=N^(21/80), exp(2y)<=e, and the other interior
term is O((log N)^2)=O(sqrt(N)) uniformly in y. Direct leakage
handles y=0. This verifies 21/80+1/2=61/80 in (18).

**Occurrences and strict bands.** L018 gives eta=1/2-beta,
multiplicity preservation and reflection at the same positive ordinate.
Padding the X range first puts every contributing ordinate in (0,3T)
for all sufficiently large T. Finiteness then justifies (19) by a
finite exchange, using positivity and evenness of F_N. L467's closed
unit-shell counts sum to O(T log T)=O(TN), including repeated and
endpoint ordinates. This proves 1+61/80=141/80 in the core.

For outer bands K=floor((log N)/4)>=2 and y>=k/N>(k-1)/N,
even at y=k/N. Reflection bounds both displacements by twice the
strict count at sigma=1/2+(k-1)/N. The fixed theta=11/20 is
admissible because 11*7=77<80=4*20. Uniformity in sigma in
the imported theorem is essential: it covers both the shrinking
first threshold and all larger k<=floor(N/2). At H=3T the
prefactor is O(TN), and log(3T)>=N gives (21) in the favorable
direction. The band weight is at most C N exp[(21/20)(k+1)],
including the top band, since actual y remains below 1/2. Exactly,

    sum_(k=K)^infinity exp[-(11/10)(k-1)+(21/20)(k+1)]
      =exp(43/20) exp(-K/20)/(1-exp(-1/20)).

Since K>=(log N)/4-1, this is O(N^(-1/80)) with an absolute
constant. No order, band endpoint or negative displacement is lost;
critical-line atoms belong to the core. This proves (22), with
141/80<159/80<2, uniformly in the growing N and band index.

The direct mathematical inputs remain L018, L467 and the specified
finite-space facts of L641. The external density input is precisely
(1); its manuscript proof and effective onset remain outside this
audit. L642 is downstream context only. The boundary-only transfer
and deterministic-annulus stops remain valid: this mean saving uses
additional actual-zero horizontal density and X averaging.

## Mathlib

Full matching coverage has not been checked; unknown availability is
not absence. Finite orthogonal projections and spectral theory,
antiunitary involutions, Cauchy--Schwarz, the Poisson formula, Tonelli
and finite/geometric summation are supporting mathematics. No matching
formalization of the Baluyot import or this growing-grid weighted
application is claimed. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
