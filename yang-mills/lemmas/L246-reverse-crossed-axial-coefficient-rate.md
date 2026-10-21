# L246 — Axial coefficient replacement in the ordered reverse bulk trace

## Hypotheses

Use exactly L244(1)--(3)'s bulk comparison B_i^b on the transverse
vertex, edge and plaquette grids V,E,F, with its actual staggered
positions and compact extensions from L228(1). Keep the relative
SU(2) cube, lower-rooted direction-1 forest, admitted even N, a=8/N,
tau=1/16, stored coordinates, bare-first order and probes i=3,6.
All imported comparisons retain their separate-audit qualifications.
The present argument does not audit those comparisons.

Write n=N-1, d=s-t, and suppress the bulk superscripts on D,T,Z,W.
The whole-grid Hodge Laplacian has symbol lambda I, where
lambda(theta)=sum_(mu=2)^4 |1-exp(i theta_mu)|^2. Set

    R_d= r_d(Delta_T+epsilon),  G_h=(Delta_0+h)^-1,
    Q_delta=I-T(Delta_0+delta)^-1 T*,
    U_t=T G_h W_t*,       S_st=1_(t<s)+delta_st/2,             (1)

with 0<epsilon,h,delta<=1. Define B_i^eq by replacing only Z_k(s)
by Z_k(t) in both ordered products L244(3), so explicitly

    B_i^eq=a sum_(k,l)c_(i;kl,a) sum_(s,t=1)^n S_st {
      Tr_E[R_d D* Z_k(t) U_t Q_delta Z_l(t)* D]
       -Tr_E[R_d D* Z_k(t) U_t D* Z_l(t)] }.                (2)

The original finite s,t ranges, triangular diagonal half, raw samples,
finite-mesh heat coefficients, all filters, the middle-inverse order
and the sole Q_delta are unchanged. In particular (2) is not L245's
fully frozen F_i,N and uses no continuum heat coefficients.

## Conclusion

Uniformly in the three positive masses,

    |B_i^b(epsilon,h,delta)-B_i^eq(epsilon,h,delta)|
                                                        <=C_i N^2. (3)

Thus at epsilon=N^-1, h=N^(-4/3), delta=N^(-2/3), the imported
L244 comparison gives

    |R_R-B_i^eq|<=C_i N^(5/2) log(eN).                    (4)

The missing comparison with L245's frozen expression is now precisely
B_i^eq-F_i,N. Its transverse coefficient placement, raw continuum
sample matching and finite-mesh/full-continuum heat matching are still
unproved. No bound for that difference is claimed. L245 separately
bounds F_i,N-a^-3 K_(i,R); no outside factor 3 enters (3) or (4).

This is local standard-method progress under the approved reverse
remainder assessment, classified REPRODUCTION, without a claim of
progress beyond the checked sources. The separate critical audit in
proof section 5 accepts this partial rate relative to its imported
inputs. Independent component rates, quantitative
L011 assembly, interacting reflected error <=c_box/2, continuum axioms,
infrared control and finite positive mass remain unresolved.

## Proof

### 1. Axial variation of the actual raw coefficients

L244(2) uses the actual L228 extensions z_k=a v_k, before pinned
zero extension. L228(1) gives support in a fixed box of O(N) side
lengths, |v_k|<=C p(k) and existing-neighbor differences <=C a p(k)
in every direction, including the axial direction. Its clamping and
fixed physical cutoff preserve these bounds. We use the same extension
at every level; we do not choose unrelated extensions for different
slices. The finite path stencils Bb,Bq have fixed ranges and bounded
multiplicity. Hence the normalized raw factor

    Z_k(s)=a^-1[M_(Bb z_k(s)) Bq-M_(Bq z_k(s)) Bb]

obeys, with E_k(s,t)=Z_k(s)-Z_k(t),

    ||Z_l(t)||<=C p(l),
    ||E_k(s,t)||<=C a |s-t| p(k).                         (5)

Indeed each path coefficient is a fixed sum of v_k samples; telescope
its axial neighbor differences along the |s-t| steps and use bounded
row and column multiplicity for the operator norm. This compares only
existing interior levels 1,...,n. It never compares an interior prefix
with the separately pinned potential at s=N.

There are edge and plaquette coordinate selectors chi_E,chi_F, each
of rank <=C N^3, containing the input and output supports of every
Z_k(s), for all s and labels k. The common box is independent of k;
enlarge it by the fixed path range. Thus

    Z_k(s)=chi_F Z_k(s) chi_E,
    E_k(s,t)=chi_F E_k(s,t) chi_E.                        (6)

This compactness belongs to deterministic coefficient stencils, not
to Green or projection kernels. No covariance source is restricted.
Enlarge the fixed polynomial p if needed. The actual heat envelope
imported in L244(10) is then

    sum_(k,l)|c_(i;kl,a)|p(k)p(l)<=C_i.                  (7)

The envelope is over every allowed finite-mesh mode, including constant
component indices, with constants independent of N. We do not compare
it with a continuum series here.

### 2. Keep the middle inverse in its energy factorization

Use L105(2)'s actual filtered map

    (W_t phi)_mu=-C_mu* M_(u_(a,1)(t)) C_mu D_mu phi.

The whole-grid endpoint averages are contractions, displacement is
uniformly bounded, and sum_mu D_mu* D_mu=Delta_0. The same energy
argument as L103(13) therefore gives bounded extensions

    ||T Delta_0^(-1/2)||<=1,
    ||W_t Delta_0^(-1/2)||<=C.                            (8)

On the bulk grid these formulas are interpreted as bounded Fourier
gradient factors, followed by the displayed averages and multipliers.
They do not assert that Delta_0^(-1/2) itself is bounded. First on a
dense spectral domain away from lambda=0, and then by continuity,

    U_t=(T Delta_0^(-1/2)) [Delta_0/(Delta_0+h)]
                            (W_t Delta_0^(-1/2))* ,
    ||U_t||<=C.                                         (9)

Also ||Q_delta||<=1 and ||D||<=sqrt(12). These facts are uniform in
h,delta; the displacement remains in W_t in its original order.
No multiplier or component filter has crossed an inverse.

### 3. Localized spectral trace bounds for both exact orders

For fixed d and epsilon define nonnegative scalar convolution operators
on any of the three-component transverse grids by their symbols

    f_1(theta)=lambda r_d(lambda+epsilon),
    f_(1/2)(theta)=sqrt(lambda) r_d(lambda+epsilon),
    I_j(d,epsilon)=integral f_j(theta) dtheta/(2pi)^3.    (10)

All are bounded at positive epsilon and integrable. The axial scalar
kernel r_d is positive and even, by L245(8). In raw tail coordinates
the bulk curl symbol c satisfies ||c||=sqrt(lambda) when lambda>0:
this follows from c* c=lambda I-tau tau*, tau* tau=lambda. Consequently

    D R_d D*=F_1^(1/2) V_1 F_1^(1/2),
    R_d D*=F_(1/2),E^(1/2) V_(1/2) F_(1/2),F^(1/2),    (11)

where V_1 has symbol c c*/lambda on F, V_(1/2) has symbol
c*/sqrt(lambda) from F to E, and both have norm <=1. Set their
symbols to zero at lambda=0. F_j denotes the scalar operator with
symbol f_j on the indicated component grid. Formula (11) is a
factorization of an adjacent covariance/circulation product; it moves
no coefficient. Staggered phase changes are unitary and give the same
singular values and diagonal scalar norms.

For any coordinate selector chi on one of these grids, the exact
diagonal Fourier identity gives

    ||chi F_j^(1/2)||_HS^2
      =||F_j^(1/2) chi||_HS^2=rank(chi) I_j(d,epsilon).    (12)

This follows by summing <e_x,F_j e_x>=I_j over selected coordinates;
all unselected kernel input/output coordinates remain in the squared
norms. Thus it is a localized Hilbert--Schmidt calculation, not an
assumed finite trace of a whole-grid convolution operator.

For the first ordered difference, exact rectangular trace cyclicity
gives

    Tr_E[R_d D* E_k U_t Q_delta Z_l* D]
      =Tr_E[Z_l* (D R_d D*) E_k U_t Q_delta].             (13)

Use (11) to factor the right side between Z_l* and E_k. In (6),
Z_l*=Z_l* chi_F and E_k=chi_F E_k. Equations (5),(6),(12) show

    ||Z_l* F_1^(1/2)||_HS<=C p(l) N^(3/2) I_1^(1/2),
    ||F_1^(1/2) E_k||_HS
               <=C a |d| p(k) N^(3/2) I_1^(1/2).

Hilbert--Schmidt trace duality, with the contraction V_1 between the
two factors and (9) on the right, therefore bounds (13) by

    C a |d| N^3 p(k)p(l) I_1(d,epsilon).                (14)

For the second ordered difference use instead

    Tr_E[R_d D* E_k U_t D* Z_l]
      =Tr_F[Z_l (R_d D*) E_k U_t D*].                   (15)

Here only one circulation is adjacent to R_d. Apply the second
factorization in (11), using Z_l=Z_l chi_E and E_k=chi_F E_k.
Exactly (12) and (5) give the two Hilbert--Schmidt bounds with I_(1/2)
in place of I_1. The final D* stays on the right and has bounded norm.
Thus (15) is bounded by

    C a |d| N^3 p(k)p(l) I_(1/2)(d,epsilon).            (16)

Every cyclic trace above is legitimate: Z_l and E_k are finite rank,
the positive-mass inverses are bounded, and the displayed factorizations
are products of Hilbert--Schmidt and bounded operators. The inequality
used is |Tr(AB)|<=||A||_HS ||B||_HS for compatible rectangular
factors, with bounded intervening operators handled by their norms.
It retains the signs of the original subtraction until the final
triangle inequality. There is no trace positivity premise for the
actual response.

### 4. Sum the complete axial first moment inside the spectrum

Import L245(8): r_d(mu)=q^|d|/(2 sinh(kappa)), with
q=exp(-kappa), cosh(kappa)=1+mu/2. For mu>0 the absolutely convergent
geometric-series derivative gives sum_(d>=1) d q^d=q/(1-q)^2.
Using mu=(1-q)^2/q and 2 sinh(kappa)=sqrt(mu(mu+4)), this yields

    sum_(d>=1) d r_d(mu)=1/[mu sqrt(mu(mu+4))]
                                       <=1/(2 mu^(3/2)).          (17)

The identity concerns the positive majorant, not a replacement of the
finite response sum. Tonelli applies to its nonnegative summands. For
j=1 and j=1/2,

    sum_(d>=1) d I_j(d,epsilon)
      <=(1/2) integral lambda^j/(lambda+epsilon)^(3/2)
                                                    dtheta/(2pi)^3
      <=(1/2) integral lambda^(j-3/2) dtheta/(2pi)^3
      <=C.                                                        (18)

The last constants are uniform for all epsilon>0. Indeed
lambda>=4|theta|^2/pi^2 on the transverse cube. For j=1/2 the
worst singularity is |theta|^-2, integrable in dimension three;
for j=1 it is only |theta|^-1. Away from zero the integrands are
bounded. All transverse frequencies, including the singular corner,
are included. This is why replacing the transverse integral by a
spectral supremum would unnecessarily lose powers of epsilon.

The diagonal d=0 contributes exactly zero to the coefficient
difference, by E_k(t,t)=0; its half-weight is still present in (2).
For each original t the remaining range is 1<=d<=n-t. Bound that
finite positive error sum by (18); there are at most n choices of t.
Sum (14) and (16), then use the original prefactor a and (7):

    |B_i^b-B_i^eq|
      <=C_i a^2 N^3 n
          sum_(d>=1) d [I_1(d,epsilon)+I_(1/2)(d,epsilon)]
      <=C_i a^2 N^3 n<=C'_i N^2.                        (19)

This proves (3) uniformly before any choice of masses. Both original
ordered terms, every row in their kernels, the original finite axial
range and the complete finite-mesh heat sum have been accounted for.
Only their deterministic coefficient level has changed in (2).

Combining (19) with L244(6) proves (4) at its stated schedule. Nothing
in this proof freezes coefficients transversely or changes the actual
heat coefficients to L245's continuum coefficients. In particular
(2) is not L245's frozen density: its variable transverse factors
remain between the inverses. A subsequent axial spectral summation
must retain these ordered factors and bound its finite endpoint deficit;
that further comparison is not undertaken here. The remaining difference
B_i^eq-F_i,N must be estimated independently. No R_L transpose
transfer, separate first absolute spatial kernel moment, small
projection-commutator norm, or fixed-mass theorem evaluated at varying
mass is used.

### 5. Separate critical audit of the axial replacement

This audit checks (3)--(4) under the unchanged axial-audit SPECIALIZE
assessment. It accepts the replacement relative to the stated inputs;
it does not audit L244's boundary transfer or the upstream inverse,
projection and middle-mass comparisons. No new exponent, coefficient
evaluation or complete-response conclusion is obtained.

**Coefficient and support hypotheses.** L228(1) supplies one extension
on the four-dimensional common index grid, not unrelated slice
extensions. Its clamping preserves every existing-level sample before
the pinned zero extension, and its cutoff has a fixed physical support.
Thus telescoping along the same staggered component between s and t
costs at most C a|s-t|p(k). Applying the fixed Bb,Bq stencils preserves
this estimate and gives (5). The union of their input and output
supports in any slice has at most C N^3 coordinate rows, independently
of the heat label and level. This proves the selector use in (6);
it does not truncate a convolution row. The enlarged fixed polynomial
is included in the actual finite-mesh envelope L244(10). That envelope
is an imported hypothesis here, including all allowed constant labels.
No estimate compares an interior value with the separate upper pin.

**Middle energy order.** In each component of W_t, the sole unaveraged
vertex derivative D_mu remains on the right of both endpoint filters
and the displacement multiplier. For any vertex vector phi in the
dense spectral domain, contraction of the averages gives

    sum_mu ||C_mu* M_u C_mu D_mu Delta_0^(-1/2) phi||^2
        <=||u||_infinity^2 sum_mu
                          ||D_mu Delta_0^(-1/2) phi||^2
        =||u||_infinity^2 ||phi||^2.

Together with the identical gradient-energy identity for T, this
checks (8). The two factors extend boundedly to the whole vertex
space; their adjoints give the bounded extension of
Delta_0^(-1/2) W_t*. Spectral cutoffs away from zero verify (9),
then strong cutoff convergence and boundedness give the identity on
the full space. The middle scalar factor lambda/(lambda+h) is a
contraction. It commutes only with the scalar spectral factors used
in this identity, not with W_t or its multiplier. Consequently the
bound is uniform in h. The symbol of Q_delta has eigenvalue one on
the transverse co-closed range and delta/(lambda+delta) on the
gradient range, so its norm is at most one uniformly in delta.

**Both rectangular words.** Use E for edge and F for plaquette space;
Z_l,E_k:E to F and U_t,Q_delta:E to E. In the first word, cyclicity
gives exactly (13), an E-space trace. Put

    A=Z_l* F_(1,F)^(1/2): F to E,
    B=F_(1,F)^(1/2) E_k: E to F.

It is Tr_E[A V_1 B U_t Q_delta]. For the second word the cyclic
trace (15) is on F; put instead

    A=Z_l F_(1/2,E)^(1/2): E to F,
    B=F_(1/2,F)^(1/2) E_k: E to F.

It is Tr_F[A V_(1/2) B U_t D*], with
V_(1/2):F to E. Thus the second factorization uses only its single
adjacent circulation; the last D* is bounded separately. Neither
word changes the order of U_t and a multiplier. The curl identity
c*c=lambda I-tau tau* makes c*/sqrt(lambda) a contraction, and
c c*/lambda a projection, at almost every frequency. Scalar
multipliers commute with these convolution symbols on their
respective component grids. These facts prove both identities in
(11), including all staggered phases. Assigning zero at the single
zero-frequency point changes no operator on l2(Z^3).

In both cases (6) places a coordinate selector immediately next to
the scalar square root on the coefficient side. Parseval therefore
gives (12) over every convolution input and output, including rows
outside that selector. Each A has Hilbert--Schmidt norm at most
C p(l) N^(3/2) I_j^(1/2); each B has norm at most
C a|d|p(k) N^(3/2) I_j^(1/2). The ideal property and rectangular
Hilbert--Schmidt trace inequality give exactly (14) and (16).
Positive masses make all other factors bounded; the finite-rank
coefficients also justify the cyclic rotations before factorization.
No whole-grid convolution is assumed trace class, and no positivity
of the signed trace is used.

**Complete singular and axial count.** The imported scalar kernel is
L245(8). Its primary scalar framework is Dowker, *Heat-kernels on
the discrete circle and interval*, arXiv:1207.2096v2 (31 August 2012),
sections 2, 7 and 10, (3), (5), (29)--(31), (42)--(48), as inspected
in the saved assessment; those interval formulas do not impose scalar
Dirichlet conditions on the vector field. Here the whole-line kernel
is already an input, so no heat-kernel reproof is needed. Directly
checking the convergent geometric-series derivative gives

    sum_(d>=1) d r_d(mu)
       =[q/(1-q)^2]/[2 sinh(kappa)]
       =1/[mu sqrt(mu(mu+4))].

This elementary verification is needed to check the claimed uniform
moment rather than import an unspecified weighted-moment estimate.
Tonelli applies to the nonnegative majorants in (10). For j=1 and
j=1/2, their full first moments are bounded respectively by the
integrals of lambda^(-1/2)/2 and lambda^(-1)/2. The lower bound
lambda>=4|theta|^2/pi^2 on [-pi,pi]^3 makes the radial integrals near
zero proportional to integral r dr and integral dr, both finite.
The complement is bounded. Uniformity in epsilon thus follows from
the full spectral integral, without an epsilon-dependent supremum.

The diagonal coefficient difference is zero, while S_st is zero for
s<t. For each of the n original t levels, summing the remaining
positive d majorant over all d>=1 is an inequality, not an extension
of the signed response. Each transverse selector contributes rank
at most C N^3; one a comes from the coefficient difference and one
from the original response. The full heat envelope gives
C_i a^2 n N^3 <=64 C_i N^2. This includes both words and both actual
probes, whose only additional use is their imported heat envelope.
The diagonal half stays unchanged in the retained equal-level trace.
There is no doubled axial orientation or outside factor 3.

This verifies (3) for all three positive masses before a schedule is
chosen. Combining it with exactly L244(6), once, yields (4), since
N^2 <= N^(5/2)log(eN). The bound does not establish transverse freezing,
raw continuum/heat matching or any upstream audit. It avoids each of
the operator-norm, termwise projection, varying-mass substitution,
adjoint and separate absolute spatial-moment shortcuts recorded in
ATTEMPTS/028--032. No unsupported assertion was found in the audited
replacement; all independently unresolved comparisons remain qualified.

## Mathlib

Full matching ordered reverse axial coefficient estimate: **not
checked**. Supporting Fourier diagonal identities, geometric-series
derivatives, Hilbert--Schmidt trace duality, Tonelli and local
integrability coverage: **not checked**. Unknown coverage is not
absence. The actual raw extensions, filtered middle-energy argument
and scalar axial resolvent are imported as specified above; their
use on the whole grids is justified in the proof. No continuum Ward
or flow theorem is claimed to supply this isolated bare trace bound.
