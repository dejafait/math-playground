# Lemma 419: a negative-cone bulk at the actual response

## Hypotheses

Use L418's actual graph and rare kernel p(t) delta_Y(t), for any fixed
lambda>0, on [H,2H] with measure dt/H. Write E for that height average,
ell=log H, w=1-p, and let Q_ij, J_R and D_R denote its unnormalized
second matrix, first Bcal integral and first Delta integral. L418 gives

    E p=O(ell^-4), Q positive semidefinite, tr Q=O(1),
    J_R=O(ell^-2), D_R=O(1).

Retain precisely L416's moment requirements, with no critical first
moments or specified constant terms in the four even second moments.
The actual response and all its derivatives are fixed at their height.
Use L414's exact conversion, L390's uniform response approximation,
L368's absolute right-line series and annulus, L369's gamma-phase
estimates, and L410's constants

    c=1/(4pi), S=zeta(5)zeta(3)^2/zeta(6),
    a_*=c^2 S/15, b0=zeta(3)/(4pi).

No conditional independence of actual jets, phase distribution, or
global critical-function realization is assumed.

## Conclusion

For every sufficiently large real H there is an explicit measurable
six-state conditional bulk mu_(H,t), supported on |X|<=C sqrt(ell)
and Delta(X;t)<0, with one fixed C and onset. The probability kernel

    nu_(H,t)=p(t) delta_Y(t)+w(t) mu_(H,t)

has the exact uniform height marginal and prescribed actual response.
It satisfies all six second moments of L416, with both odd entries
exactly zero, E_nu Bcal=-b0, and E_nu Delta=-a_* ell+o(ell).
It preserves all 23 required quartic coefficients and all absolute
and pointwise bounds, including exact curvature. It avoids the forbidden
joint sign and has a strictly negative clipped square mean.

Its cubic is only

    E_nu(Delta Bcal)=F_lambda(H)+O(ell),                 (1)

where F_lambda is exactly L418 (1). Thus this completes the independent
bulk obligation, not the full feasibility target: the remaining condition
for this particular construction is
F_lambda(H)=beta_* ell^2+o(ell^2). No such equality is proved. This
partial construction is validated by the separate step-155 critical
audit below. It supplies no actual clipped mean, regulator margin or
RH conclusion; the cubic condition remains unverified.

## Proof

The unchanged step-150 SPECIALIZE assessment covers this prescribed-
response feasibility attempt. Existing moment results are imported from
L416 (including its precise Bui--Hall citation and normalization), rather
than reproved. The new work is the simultaneous supported calibration.
The inspected selection/purification results do not supply its values;
the explicit finite construction below needs neither theorem. Its small
matrix and right-line calculations are included to justify measurability,
strict support and fixed constants, not to claim a new general moment or
selection theorem. POTENTIALLY_NEW refers only to the limited comparison
in that assessment, not certified originality.

### Exact quadratic forms and a uniformly negative covariance trace

Put r=q/L^2, where q=(log A)'', and use the actual envelope response v.
Expanding L414's product conversion, with no approximation, gives

    ell_F=y^2-xz-r x^2,
    Ccal=v_1^2-v_0 v_2-r v_0^2,
    Bcal=b(t)^T X,
    b(t)=(-v_2-2r v_0, 2v_1, -v_0).

Define the real symmetric matrix J(t) by Delta(X;t)=X^T J(t) X.
It is uniformly bounded, as are b and the conversion coefficients.
All these functions are continuous. L390's complete response estimate
v=(ca,-ch/2,-ca/4)+O(1/L), with actual curvature retained, gives

    b=c(a/4,-h,-a)+O(1/L).

Consequently |b| is bounded below by a fixed positive constant on an
eventual ray, since a^2+h^2>=zeta(5/2)^-2. No division by a real
response projection, which could vanish, is used.

The required leading raw second matrix is

    K=[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]].

It is positive definite: its (x,z) block has determinant 1/180, and
the remaining eigenvalue is 1/12. Substituting these entries in L414's
leading polynomial d, and then using the O(1/L) coefficient error, yields

    tr(J(t) K)=-c^2(a(t)^2/20+h(t)^2/12)+O(1/L).       (2)

For the a^2 coefficient the arithmetic is
1/80-1/24+1/16-1/12=-1/20; the h^2 coefficient is -1/12,
and both mixed terms vanish. Hence tr(JK)<=-delta_0<0 uniformly
for all sufficiently large t, for one fixed delta_0. This is a
covariance trace, not an assertion that every vector has negative Delta.

### A fixed bounded weight giving the required first-Delta coefficient

Write Z(t)=zeta(5/2+it), W(t)=|Z(t)|^2, M=zeta(5/2).
Only the absolutely convergent Dirichlet series/Euler product is used
here; its domain and derivative hypotheses are those checked in L368,
which cites DLMF 25.2.1 and the local Euler-log input. Put C_0=1 and,
for each fixed integer j>=1, define

    C_j=sum_(n>=1) d_j(n)^2 n^-5,
    zeta(s)^j=sum_(n>=1) d_j(n)n^-s, Re s>1.

All coefficients are nonnegative. Absolute multiplication is justified
by sum d_j(n)n^-sigma=zeta(sigma)^j<infinity for sigma>1.
The exact diagonal and an absolute off-diagonal estimate give

    E W^j=C_j+O_j(H^-1).                              (3)

Indeed the normalized integral of exp(it log(m/n)), m!=n, is at most
2/(H |log(m/n)|)<=2 max(m,n)/H. Summing its product coefficients
costs at most 4 zeta(3/2)^j zeta(5/2)^j/H. This retains both endpoints
and the full series. In particular C_1=zeta(5).

We need one fixed j with C_(j+1)/C_j>S. Here is a bounded-existence
argument, without assuming any actual phase law. Unique factorization
and positive sums give

    C_j=product_p sum_(e>=0) binom(j+e-1,e)^2 p^(-5e).

Each factor equals the circle average of |1-p^(-5/2)exp(i theta)|^(-2j)
by absolute Fourier multiplication. For a fixed prime its j-th root
tends to (1-p^(-5/2))^-2: the upper bound is the maximum, and any fixed
small arc about theta=0 gives the matching lower limit as the arc
shrinks. For finitely many primes multiply these lower bounds. The
remaining Euler factors are at least one. Letting that finite set grow
and using absolute Euler convergence gives

    liminf_(j->infinity) C_j^(1/j)>=M^2.

Conversely W<=M^2 and (3) imply C_j<=M^(2j), so the limit is M^2.
The threshold lies strictly between C_1 and M^2. The first strict
inequality follows from zeta(3)^2>zeta(6). For the second, elementary
decreasing-integrand bounds give zeta(3)<5/4, zeta(5)<67/64 and
zeta(6)>1, whence S<1675/1024. Meanwhile the first five terms give

    M>1+7/40+1/16+1/32+1/60=617/480,
    (617/480)^2>1675/1024.

The rational lower bounds for the terms n=2,3,5 follow respectively
from sqrt(2)<10/7, sqrt(3)<16/9 and sqrt(5)<12/5; n=4 is exact.
Thus M^2>S. If every ratio C_(j+1)/C_j for j>=1 were at most S,
then C_j<=C_1 S^(j-1), contradicting the root limit. Fix once and for
all an integer k>=1 with R_k=C_(k+1)/C_k>S. No k depends on H.

Set

    theta=(S-C_1)/(R_k-C_1),
    g0(t)=1-theta+theta W(t)^k/C_k.                    (4)

Here 0<theta<1. The function g0 is bounded above and below by fixed
positive constants. Equation (3) proves E g0=1+O(H^-1) and
E(g0 W)=S+O(H^-1).

We also require the gamma harmonic to vanish. With R=exp(i phi),
a^2=(W+Re(R^2 Z^2))/2 and h^2=(W-Re(R^2 Z^2))/2. We claim

    E[g0 R^2 Z^2]=o(1).                              (5)

The function g0 Z^2 is an absolutely uniformly convergent sum of fixed
frequency exponentials: it is a fixed finite linear combination of
products of absolutely convergent Z and conjugate-Z series. Approximate
it uniformly by finitely many terms. For each retained frequency u,
the phase 2phi(t)+ut has derivative log(t/(2pi))+u+O(t^-2), bounded
below by (log H)/2 for sufficiently large H, and second derivative
O(1/H), by L369 (6). Integration by parts bounds its unnormalized
integral by O_u(1/log H); division by H gives convergence to zero.
The discarded uniform tail bounds its normalized integral independently
of H. First let H tend to infinity for the finite sum and then let
the tail tend to zero. This proves (5), with no growing-frequency
interchange or independence assumption. In particular

    E[g0(a^2/20+h^2/12)]=S/15+o(1).                  (6)

The weight changes only conditional critical states, not response values
or the height measure. Normalize it against the actual remaining mass:

    N_H=E(w g0), g_H(t)=g0(t)/N_H.

L418 and (3) imply N_H=1+O(H^-1+ell^-4). Thus g_H retains fixed
positive lower and upper bounds, E(w g_H)=1 exactly, and replacing g0
by w g_H in any bounded averaged response expression costs o(1).
Together with (2) and (6), this yields

    E[w g_H tr(JK)]=-c^2 S/15+o(1)=-a_*+o(1).        (7)

### Exact linear-mean and odd-second-moment corrections

Let W_H=E w=1-O(ell^-4), eventually at least 1/2. Define

    d_H=(-b0-J_R)/W_H,
    m_H(t)=d_H b(t)/|b(t)|^2.

These are bounded uniformly, measurable, and b(t)^T m_H(t)=d_H
exactly. Define a symmetric constant-in-t matrix A_H with zero diagonal
and zero (1,3) entry, and with

    (A_H)_12=-(Q_12+E[w m_1 m_2])/W_H,
    (A_H)_23=-(Q_23+E[w m_2 m_3])/W_H.               (8)

All its entries are O(1). Set the conditional centered covariance to

    Sigma_H(t)=ell g_H(t) K+A_H.                     (9)

Uniform positive lower and upper bounds for g_H and positive definiteness
of K imply c_1 ell I<=Sigma_H<=c_2 ell I eventually. Also (2) gives

    tr(J Sigma_H)<=-delta_1 ell                     (10)

for one delta_1>0, uniformly in t, after increasing the onset. These
facts hold even where w=0. The constants may depend on the fixed
lambda, k and theta, never on H.

### A measurable six-state realization strictly inside the cone

We give the finite matrix implementation, including its measurability,
so no selection or stronger general moment theorem is presumed.
Let S_H(t) be the positive square root of Sigma_H(t) and let
J_H'=S_H J S_H. These are Borel matrices; the positive matrix square
root is continuous on positive definite matrices. There is a Borel
choice of orthonormal basis u_1,u_2,u_3 with

    u_i^T J_H' u_i=tr(J_H')/3, i=1,2,3.              (11)

Pointwise existence is the constant-diagonal case of the real
Schur--Horn theorem: Eric A. Carlen and Elliott H. Lieb, *Short proofs
of theorems of Horn and Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), pp. 1--2,
Horn's theorem following (1.1), with proof through (1.2). The constant
trace-average diagonal is majorized by the eigenvalue list of this
real symmetric matrix. Import that existence result; the following
coordinate implementation is needed additionally for Borel dependence,
which the cited theorem does not assert.

Put tau=tr(J_H')/3. If a
diagonal entry equals tau, choose its coordinate vector first (smallest
index breaks ties). Otherwise choose the first pair of indices with
diagonals d_i<tau<d_j. Such a pair exists because their mean is tau.
For off-diagonal entry e, the vector

    u=(e_i+eta e_j)/sqrt(1+eta^2),
    eta=(-e+sqrt(e^2+(d_j-tau)(tau-d_i)))/(d_j-tau)>0

has Rayleigh value tau. Use (-eta e_i+e_j)/sqrt(1+eta^2) and the remaining
coordinate vector as its orthonormal complement. In the equality case
use the other coordinate vectors as complement. The restriction to that
two-dimensional complement has trace 2tau. If its two diagonal entries
are tau, keep the basis; otherwise one is below tau and one above,
and the same formula gives a first vector of value tau. Its orthogonal
complement also has value tau by the trace identity. Choosing pairs and
orders deterministically makes each branch Borel, including all equality
cases. This proves (11) without an eigenvector selection assumption.

Take the six conditional atoms

    X_(i,+)=m_H+sqrt(3) S_H u_i,
    X_(i,-)=m_H-sqrt(3) S_H u_i, i=1,2,3,

each of probability 1/6. Their centered mean is zero and centered
covariance is Sigma_H. Their centered quadratic values are all
tr(J Sigma_H)<=-delta_1 ell, by (10)--(11). Translating by bounded
m_H changes each quadratic value by O(sqrt(ell))+O(1), because
J is bounded and |S_H u_i|=O(sqrt(ell)). Therefore all six atoms
have exact Delta<0 for one common eventual onset. This is an exact
support statement for the actual response and curvature, not support
deduced from an asymptotic discriminant replacement. Every atom has
norm O(sqrt(ell)); finite Borel atoms give the required measurable kernel.

### Simultaneous moment checks and the remaining cubic

Using unnormalized bulk integrals throughout, its second matrix is
E[w(Sigma_H+m_H m_H^T)]. By E(w g_H)=1 and (8), adding the rare
matrix gives both odd entries exactly zero. Every other entry is

    ell K_ij+Q_ij+E[w(m_H m_H^T)_ij]=ell K_ij+O(1),

because A_H has no other entries. These are exactly the four permitted
even errors, not unspecified substitutes for the tiny odd tolerances.
The total linear mean is J_R+W_H d_H=-b0. For the quadratic mean,
(7), (9) and boundedness of m_H,A_H,J yield

    E_nu Delta=D_R+ell E[w g_H tr(JK)]
                       +E[w(tr(J A_H)+m_H^T J m_H)]
               =-a_* ell+o(ell).

All response quantities remain actual. The same norm bound and bounded
coefficients show that every bulk quartic among Delta^2, Delta Bcal^2
and the 21 Delta omega_i omega_j has absolute integral O(ell^2),
including off-diagonal entries and entries with zero leading coefficient.
L418 preserves all 23 actual quartic integrands in its rare part. Thus
all their required leading coefficients survive without any fitting.
Bulk U^2=O(ell^2), while bulk U^(3/2) and |Bcal|^3 are O(ell^(3/2));
adding L418 proves the full O(ell^4) and O(ell^(9/4)) envelopes.

For clarity, the bulk cubic is even smaller than the general bound from
its norm. Write X=m+xi at a fixed height. Central symmetry makes all
odd centered moments zero. Direct multiplication gives

    E_mu[(X^T J X)(b^T X)]
      =(b^T m) tr(J Sigma_H)
           +2 m^T J Sigma_H b+(m^T J m)(b^T m)=O(ell).

Integrating with w<=1 proves (1), using L418's exact rare integral.
This O(ell) term cannot fix a missing leading ell^2 coefficient.

For pointwise critical bounds, the conversion matrix is uniformly
bounded, and sqrt(ell) L(t)^j/T(t)^(1/2) tends uniformly to zero for
j<=2. Hence the bulk obeys the fixed qualitative P_j bounds after one
onset. L418 already verifies them for the rare part. The actual annulus,
response bounds and strict Ccal lower bound are unchanged; every state
uses the exact q and response derivatives. Finite constants are chosen
once and all onsets have a finite maximum covering every sufficiently
large real H. For each fixed H the constructed states are bounded on
the interval, so all observables are absolutely integrable.

The masses p+w=1 hold in every fiber. The rare states already avoid
the joint sign; the bulk has Delta<0 throughout. Its Bcal integral
is -b0-J_R<0 eventually, so a positive bulk measure has Bcal<0.
There the clipped square integrand is strictly negative. Everywhere
else it is nonpositive. Thus its total mean is strictly negative,
without asserting that the unresolved cubic constraint holds.

The support construction closes one genuine independent calibration
gap in the prescribed-response attempt. The rare cubic condition,
actual critical/global realization, actual clipped statistic and the
regulator-scale/full-error comparison remain unproved. No complete
feasible law for the full list, separator, sign extension or RH
candidate is claimed.

### Separate critical audit — 2026-10-16, step 155

This RESEARCH / REPRODUCTION / proof_audit uses the pre-existing
SPECIALIZE assessment
`drafts/literature/2026-10-16-prescribed-response-bulk-critical-audit.md`.
It validates precisely the partial construction in the Conclusion.
It reuses the assessed absolute right-line/gamma inputs, the Bui--Hall
second moments cited and specialized in L416, and the Schur--Horn
theorem cited above. No new zeta moment, distributional independence,
general selection theorem or claim of originality is introduced.
L418 has not received a complete separate audit: its load-bearing
kernel identities and bounds are checked here, but its cubic is not
evaluated and its full-list feasibility is not asserted.

**Exact response and trace.** With r=q/L^2 define

    Fmat=[[-r,0,-1/2],[0,1,0],[-1/2,0,0]],
    b=(-v_2-2r v_0,2v_1,-v_0),
    Ccal=v_1^2-v_0 v_2-r v_0^2.

Expanding the exact P,V conversion cancels every alpha term and gives
ell_F=X^T Fmat X, Bcal=b^T X and
J=b b^T-4 Ccal Fmat. Thus no response approximation is used to
define support. The leading response yields

    b=c(a/4,-h,-a)+O(1/L),
    Ccal=c^2(a^2+h^2)/4+O(1/L),
    tr(Fmat K)=1/6-r,
    b^T K b=c^2(7a^2/60+h^2/12)+O(1/L).

Consequently (2) has exactly the stated negative coefficients. The
(x,z) block of K has determinant 1/180>0 and positive first diagonal;
together with K_22=1/12 this proves positive definiteness. The annulus
and uniform response errors give one delta_0>0 in (2) for all large t.
They also give |b|>=c/(8 zeta(5/2)) after an onset, because the leading
norm is at least c sqrt(a^2+h^2)/4. In particular m_H never divides
by a vanishing response projection. The same Ccal expansion gives
Ccal>=c^2/(8 zeta(5/2)^2)=1/(128 pi^2 zeta(5/2)^2) eventually.
All these estimates retain the actual response; bounded conversion
coefficients follow from bounded alpha and q=O(T^-2).

**Fixed-power weight and gamma limit.** In (3), the complete absolute
off-diagonal sum is bounded by
4 zeta(3/2)^j zeta(5/2)^j/H: use max(m,n)<=m+n and apply the two
absolutely convergent series at 3/2 and 5/2. The diagonal C_j is
finite, positive and independent of H. Its Euler factors follow from
the fixed-j multiplicativity of d_j and nonnegative summation. For
each finite prime set, the small-arc lower bound on each circle
integral gives the product of its maxima in the j-th-root limit.
Only then is the finite prime set increased. Absolute Euler convergence
gives the lower limit M^2, while C_j<=M^(2j) supplies the upper limit.
This argument uses neither actual prime-phase equidistribution nor a
power growing with H.

The rational threshold check is strict: the decreasing-integrand
upper bounds give S<1675/1024, and the five-term lower bound for M
gives M>617/480. Their squared-bound difference is

    (617/480)^2-1675/1024=1907/115200>0.

Also C_1=zeta(5)<S since zeta(3)^2>zeta(6). If all ratios C_(j+1)/C_j
were <=S, then C_j^(1/j) would have upper limit at most S, contrary
to M^2>S. Hence one fixed finite k exists and 0<theta<1. In particular
g0>=1-theta>0 and g0 is bounded above by a fixed constant, however
large the fixed k might be. The identities following (4) are obtained
from (3) for the two fixed powers k and k+1.

For (5), absolute multiplication bounds the total coefficient mass of
g0 Z^2 by (1-theta)M^2+theta M^(2k+2)/C_k. Its finite-frequency
approximations therefore have uniform tails independent of H. At a
fixed retained frequency u, L369 (6) gives
psi'=2phi'+u=log(t/(2pi))+u+O(t^-2) and psi''=O(1/H).
On [H,2H], |psi'|>=(log H)/2 eventually. Exact integration by parts
bounds the two endpoints by O(1/log H) and the integral of
|psi''|/|psi'|^2 by O(1/log^2 H). The normalized integral tends to
zero. Taking H first for each finite head and then the uniform tail
proves (5); no differentiation of an asymptotic remainder is needed.
The coefficients 1/20 and 1/12 average to 1/15, proving (6).

Since 0<=p<=1 and E p=O(ell^-4),
|E(w g0)-E g0|<=||g0||_infinity E p=O(ell^-4).
Thus N_H stays bounded away from zero and infinity, and
E(w g_H)=1 exactly. Replacing g0 by w g_H against a bounded response
expression changes its average by O(H^-1+ell^-4). The O(1/L)
coefficient error in (2) is uniform as L>=ell. This proves (7) with
one onset for all sufficiently large real H.

**Load-bearing rare bounds and simultaneous correction.** In L418
write Rcap=max(lambda ell^2,rho), to distinguish this radius from
curvature. Its exact fiber probability is p=(rho/Rcap)^4 on rho>0,
and p=0 at rho=0. Critical reversal changes Bcal's sign and leaves
Delta and every degree-four observable unchanged. It therefore both
avoids the forbidden joint sign and gives p Q4(Y;t)=Q4(X0;t) for
each of the 23 specified quartics and U^2. All polynomials are at the
same actual height/response, including curvature.

The needed bounds are direct absolute inequalities:

    E p<=E rho^4/(lambda ell^2)^4=O(ell^-4),
    tr Q=E[rho^4/Rcap^2]=O(1),
    |D_R|<=C E[rho^4/Rcap^2]=O(1),
    |J_R|<=C E[rho^4/Rcap^3]=O(ell^-2).

The rare second matrix is positive semidefinite, so each |Q_ij| is
at most tr Q. These are unnormalized rare integrals; no division by
the small rare mass is permissible or used. Since W_H=E w>=1/2,
the definition of d_H and the lower bound for |b| make m_H bounded.
Equation (8) then makes A_H bounded. Positive g_H and K imply
c_1 ell I<=Sigma_H<=c_2 ell I. Its J trace is at most a fixed
negative multiple of ell plus O(1), proving (10) uniformly even at
heights where w=0.

The centered covariance has leading raw contribution ell K exactly,
since E(w g_H)=1. Its entries (1,2) and (2,3) have zero leading
part. Their total raw values after translation and addition of the
rare part are respectively

    Q_ij+W_H (A_H)_ij+E(w m_i m_j)=0, ij=12,23.

Thus both tiny odd tolerances hold exactly. For the other four entries,
A_H contributes zero, and the remainder is Q_ij+E(w m_i m_j)=O(1).
The same kernel has total Bcal mean J_R+W_H d_H=-b0. Its quadratic
mean is D_R+ell E[w g_H tr(JK)]+O(1)=-a_* ell+o(ell), with
a_*=c^2 S/15 as in L410. No constant term in an even second moment
or critical-coordinate first mean is imposed by the selected list.

**Borel branches and uniform strict support.** The symmetric square
root S_H is Borel since Sigma_H is positive definite. In a strict
two-coordinate branch put A=d_j-tau>0 and B=tau-d_i>0. The displayed
eta solves A eta^2+2e eta-B=0. Its radicand e^2+AB is strictly
greater than e^2, its numerator is positive, and its denominator is
nonzero. Thus its normalized vector has Rayleigh value tau exactly.
The displayed complement is orthonormal. Its restriction has trace
2tau, so either both remaining diagonal entries are tau or they
strictly straddle tau. The same lower/upper ordering and formula
apply in the latter case, and the final vector has value tau by trace.
If an initial diagonal equals tau, the coordinate-vector equality
branch gives the same complement trace. Every equality or strict
branch is a Borel set; first-index choices are finite deterministic
choices. Keeping the basis when both restricted diagonals equal tau
does not require their off-diagonal entry to vanish. These cases
exhaust the construction and require no eigenvector selection.

For xi_i=sqrt(3) S_H u_i, (11) gives
xi_i^T J xi_i=tr(J Sigma_H)<=-delta_1 ell.
Also |xi_i|<=sqrt(3c_2 ell). Thus for both signs,

    Delta(m_H +/- xi_i;t)
      <=-delta_1 ell+2||J|| |m_H| sqrt(3c_2 ell)
                            +||J|| |m_H|^2<0

after one common onset. No regularity or boundedness of the chosen
rotation parameters near an equality branch is needed: the resulting
u_i are unit vectors. The six atoms have mean m_H and centered
covariance Sigma_H since their signs cancel and sum_i u_i u_i^T=I.
Their Borel measurability gives a measurable probability kernel; p+w=1
in each fiber retains exactly dt/H as the height marginal.

**All remaining moments and bounds.** At each bulk atom,
|X|=O(sqrt(ell)), |Delta|=O(ell), |Bcal|=O(sqrt(ell)), and
|omega|=O(sqrt(ell)), uniformly at the actual bounded response.
Consequently each of Delta^2, Delta Bcal^2 and the six diagonal and
fifteen off-diagonal Delta omega_i omega_j has absolute bulk integral
O(ell^2)=o(ell^4). This includes every zero or negative leading
matrix coefficient. L418's exact preservation supplies their actual
leading coefficients. Bulk U^2=O(ell^2); bulk U^(3/2) and |Bcal|^3
are O(ell^(3/2)). In the rare part p|Y|^3=rho^4/Rcap<=rho^3 and
p|Bcal(Y)|^3<=C rho^4/Rcap. The actual bounds imported in L418
therefore give the required O(ell^4) and O(ell^(9/4)) envelopes.

For the signed cubic, expanding X=m+xi and using conditional central
symmetry leaves exactly

    (b^T m) tr(J Sigma_H)+2m^T J Sigma_H b
                                  +(m^T J m)(b^T m).

This is O(ell) uniformly. The rare integral is exactly
E[|D B| rho/Rcap]=F_lambda(H), so (1) is verified without replacing
this correlated factor by a moment or an independence premise.

Bulk pointwise P_j bounds follow from bounded conversion and
sqrt(ell)L(t)^j/T(t)^(1/2)->0 uniformly for j<=2. In L418's rare
branch rho>=lambda ell^2, Y is +/-X0 and the actual P_j bounds apply;
in its other nonzero branch |Y|=lambda ell^2, and
ell^2 L(t)^j/T(t)^(1/2)->0 uniformly. The zero branch is harmless.
Choose the constants once, enlarging the actual constants if needed.
All V_j, response errors, the annulus and the Ccal bound remain actual.
At each fixed H all states are bounded over the compact height interval,
so all observables, including signed and clipped ones, are absolutely
integrable. All estimates have fixed constants for the chosen lambda,k,
theta. The finite maximum of their onsets works for every large real H.

Finally the unnormalized bulk Bcal integral is -b0-J_R<0 eventually.
Its total measure is positive; hence its Bcal<0 set has positive measure.
Exact strict Delta<0 on all bulk states makes the clipped integrand
strictly negative there. Everywhere else in the combined law it is
nonpositive by support. The asserted strictly negative mean follows.

No defect in the partial claim or missing direct mathematical input
was found. This audit validates an independent bulk calibration, not
L418's cubic asymptotic or full prescribed-response feasibility. It
does not construct a single global critical function, evaluate actual
clipping, meet L413's regulator/full-error margin, or change any
actual-theta sign or zero-exclusion range. RH remains unresolved.

## Mathlib

Full matching coverage for this prescribed-response bulk construction
has not been checked. Supporting finite-dimensional matrix and series
facts are not claimed absent. No formal verification, numerical fit,
new numerical certificate or new zeta-moment theorem is asserted.
The imported real Schur--Horn theorem's full matching Mathlib coverage
has not been checked; the Borel branch verification above is informal.
