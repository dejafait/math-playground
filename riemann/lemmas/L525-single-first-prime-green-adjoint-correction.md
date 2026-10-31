# L525 — One reference Green correction of the first-prime adjoint cusp

## Hypotheses

Use exactly the translated fixed model of L518: I=(0,ell), ell=2a,
0<a<A, ell>d=log(2), zero extension E_I, and

    Psi(xi)=(1/2)log(1+xi^2), n(t)=exp(-|t|)/(2|t|),
    c=log(2pi), k(t)=2cosh(t/2),
    d_n=log(n), w_n=Lambda(n)/sqrt(n), w=w_2,
    mu_A=nu_rho+sum_(n>=2,d_n<=2A)w_n(delta_(d_n)+delta_(-d_n))
                         -k(t)1_(|t|<=2A)dt,
    Bf=c f+R_I(mu_A*E_I f), A_I=G_I-B.

Here nu_rho has the even density
rho(t)=exp(-t/2)/(1-exp(-2t))-exp(-t)/(2t), t>0. G_I is the
nonnegative self-adjoint smooth-core part operator from L513--L515;
Dom(A_I)=Dom(G_I). This is the killed Levy process realization.
The full-Weil identification retained in L516 remains an unaudited
external input; the result below concerns this specified model.

Use L513's exact V,v normalization and L518's f_L=v1_I, exterior
tail E_L, raw residual R_L=E_L-Bf_L and smooth cutoffs phi_epsilon.
Select

    0<r<min(d/4,(ell-d)/4,(log(3)-d)/4,exp(-8)),
    eta in C_c^infinity((d-r,d+r)), 0<=eta<=1,
    eta=1 on [d-r/2,d+r/2],
    q(x)=w eta(x)v(x-d)1_(x>d), q_m(x)=min(q(x),m), m>=1.

The value at d is immaterial. Thus q is nonnegative and integrable,
supported in [d,d+r], strictly inside I and away from other prime
cusp locations. No uniformity as ell decreases to d is asserted.

Only for the weak trace identity, assume a real u in Dom(A_I),
A_Iu=0 and ||u||_2=1. No existence, simplicity, positivity or
first-zero property is asserted. By L515, u and h=G_Iu=Bu are bounded;
L513--L514 give its continuous representative and normalized traces.

The pre-existing EXPLORE gate is
`drafts/literature/2026-10-30-weil-first-prime-adjoint-correction-coverage.md`.
This is one standard Green-potential specialization and singular-limit
calculation, not a new Green theorem or a correction iteration.

## Conclusion

Let K_I be the killed Green kernel for G_I, and put

    z_m=G_I^(-1)q_m, z(x)=integral_I K_I(x,y)q(y)dy,
    F=f_L+z, R_new=R_L+q-Bz.                                  (1)

Only the reference inverse G_I^(-1) occurs. It exists as proved below;
no inverse, spectral gap or positivity of A_I is assumed. The z_m
belong to Dom(G_I), are bounded and nonnegative, and increase to z
in L1 and almost everywhere. In particular z and R_new are integrable.
The zero extension satisfies

    (G E_I z)|_I=q, (G E_I F-BF)|_I=R_new                    (2)

in distributions on I. F is not in L2, so (2) does not place it in
an operator or form domain. For s->0+, with constants depending on
the fixed data and eta,

    z(d+s)=O(1/[s(log(1/s))^(5/2)]),
    R_new(d+s)=O(1+[s(log(1/s))^(5/2)]^(-1))=o(v(s)).          (3)

These estimates use the Green-potential representative away from d;
values on null sets may instead be omitted. All arithmetic translates
of z, both shifts of every atom including equality, nu_rho, the signed
pole and E_L remain in R_new. In particular the corrected residual is

    R_new(x)=E_L(x)-c[v(x)+z(x)]
       -integral_I rho(x-y)[v(y)+z(y)]dy
       -sum_(n>=2,d_n<=2A)w_n[F(x-d_n)+F(x+d_n)]
       +integral_I k(x-y)[v(y)+z(y)]dy+q(x),                 (4)

where F is zero outside I. The pole cutoff is one on I-I since ell<2A.

For the assumed nullvector the admissible tests phi_epsilon+z_m give,
first letting epsilon->0 at fixed m and then m->infinity,

    0=tau_L(u)+integral_I u R_new,
    integral_I u(q-Bz)=0.                                   (5)

All integrals are absolute. Thus the coefficient of tau_L is exactly
one. It is not inferred from a zero V-trace of z, which is not claimed.
The two limits can also be reversed in these scalar pairings, for the
explicit separated convergence reasons below, but (2) alone would
not justify either pairing limit.

This passes the separate conceptual audit recorded below under the
stated fixed-model hypotheses. It is a verified local specialization,
not a claim of originality or RH progress beyond the sources checked.
The residual still satisfies

    R_new(x)/v(x) -> -c as x->0+.                             (6)

No sign of its pairing with a special nullvector, trace vanishing,
family O(lambda) rate, correction-series convergence, collars or Xi
transfer is proved. Other prime cusps remain uncontrolled. In fact
(5)'s second equality explicitly preserves the original scalar pairing.

## Proof

### Imported reference facts and their applicability

Import Grzywny--Ryznar, *Potential theory of one-dimensional geometric
stable processes*, [arXiv:1107.0745v1](https://arxiv.org/html/1107.0745v1),
4 July 2011, Section 2, Proposition 3.5, Lemmas 4.1 and 4.3, and
Theorem 4.4 (especially (4.7)--(4.14)). Their parameter is alpha=2.
L513 supplies the time normalization: K_I=2K_I,GR and
V=sqrt(2)V_GR, v=sqrt(2)v_GR. L515 supplies the part-process
identification, with Fukushima--Oshima--Takeda, *Dirichlet Forms and
Symmetric Markov Processes*, second revised and extended edition,
Theorems 4.4.2--4.4.3, pp.173--175. These inputs are imported,
not independently reproved here.

The precise consequences needed are symmetry and nonnegativity of
K_I; its occupation interpretation; and

    integral_I K_I(x,y)dy=E^x tau_I
                       <=V(min(x,ell-x))V(ell)<=H,
    H=V(ell/2)V(ell)<infinity.                                (7)

Domain monotonicity gives K_I<=K_+, where

    K_+(x,y)=integral_0^min(x,y) v(x-t)v(y-t)dt.                (8)

For fixed ell and x,y in I, x!=y, Theorem 4.4 at alpha=2 gives

    K_I(x,y)<=C_ell[1+j(|x-y|)],
    j(t)=1/[t(log(1/t))^2] for 0<t<exp(-4), and 0 otherwise.   (9)

Indeed its boundary factor is at most one and its additional term
is V_GR(min(x,y)), bounded on I. Distances at least exp(-4) are
absorbed in C_ell. No bounded diagonal or whole-line transience is
used. The reference renewal estimates, already used in L518, are

    v(s) comparable to 1/[s(log(1/s))^(3/2)],
    V(s) comparable to (log(1/s))^(-1/2)                     (10)

near zero, with v positive and decreasing. These exact reference
inputs cover the hypotheses; the singular convolution and signed
arithmetic specialization below are additional calculations.

### Reference inverse, monotone L1 limit and transposition

For completeness, justify the reference inverse rather than presuming
a full-operator inverse. Let T_t=exp(-tG_I). The integral from 0 to N
of its nonnegative symmetric kernel has every row and column integral
at most H by (7). Schur's test bounds integral_0^N T_t dt on L2 by H.
Its spectral multiplier is (1-exp(-N lambda))/lambda (value N at
lambda=0). The spectral theorem and this bound for every N exclude
spectral mass at zero or below 1/H: on any spectral interval in
[0,1/H), the multiplier eventually exceeds H. Thus G_I>=H^(-1)I
and G_I^(-1) is bounded on L2. Its kernel is K_I, by monotone time
integration and the same spectral theorem. This conclusion concerns
G_I alone, not G_I-B.

Since 0<=q_m<=m, q_m is in L2; z_m=G_I^(-1)q_m belongs to Dom(G_I),
G_Iz_m=q_m, and 0<=z_m<=mH. The kernel definition and Tonelli give

    ||z||_1<=H||q||_1,
    ||z-z_m||_1<=H||q-q_m||_1 ->0.                           (11)

Here q_m increases to q in L1 because integral_0^r v=V(r)<infinity.
Thus the defining z is finite almost everywhere. This establishes
the required singular-source limit rather than importing an L1
operator-domain claim.

If psi is compactly supported and smooth in I, then psi is in
Dom(G_I) and G_Ipsi is bounded, as verified in L518. Self-adjointness
and (11) give

    integral_I z G_Ipsi
       =lim_m integral_I z_m G_Ipsi
       =lim_m integral_I q_m psi=integral_I q psi.             (12)

This is the first distributional equation in (2). Since B is bounded
on L1 with norm at most |c|+||mu_A||_TV, (11) also gives Bz_m->Bz
in L1. L518's distributional equation for f_L now proves (2) and
the full expansion (4). All its terms are integrable. Moreover
z>=0 and f_L is nonnegative and not in L2 by L518, so F>=f_L is
not in L2. No claim that F is an admissible uncut weak test follows.

More generally, for the bounded u,h in the hypotheses, the exact
domain identity integral h z_m=integral u q_m passes in L1 against
bounded h,u. Consequently

    integral_I h z=integral_I u q.                            (13)

Evenness of mu_A permits transposition of B; its absolute convolution
pairing is at most ||u||_infinity ||mu_A||_TV ||z||_1. Since h=Bu,
(13) proves integral u(q-Bz)=0. The possible kernel of A_I has not
been removed or inverted.

### Singular convolution estimate and every shifted correction

Write L=log(1/s) and take 0<s<r/4, sufficiently small for (10).
The constant part of (9) contributes O(||q||_1). At x=d+s the
remaining contribution is bounded by a fixed multiple of

    integral_0^r v(t)j(|s-t|)dt.                              (14)

For 0<t<s/2, j(|s-t|)<=C/(s L^2), and the v integral is
V(s/2)=O(L^(-1/2)). This contribution is O(1/(s L^(5/2))).
For s/2<t<2s, v(t)<=v(s/2)<=C/(s L^(3/2)), while

    integral_(s/2)^(2s) j(|s-t|)dt
          <=2 integral_0^s dt/[t(log(1/t))^2]=2/L.

This gives the same bound. For 2s<t<r, |s-t| is between t/2 and t,
so the integrand is at most C/[t^2(log(1/t))^(7/2)]. To bound its
integral without dropping the logarithm, put
J(t)=1/[t(log(1/t))^(7/2)]. Since log(1/t)>8 on this range,

    -J'(t)=[1-7/(2log(1/t))]/[t^2(log(1/t))^(7/2)]
           >=(1/2)/[t^2(log(1/t))^(7/2)].

Thus this last part is at most 2C J(2s)=O(1/(s L^(7/2))).
The sum proves the first bound in (3). It is o(v(s)) by the lower
bound in (10). The value at t=s is irrelevant; j is integrable
across its singularity.

We also need boundedness away from d, not just the estimate at d+s.
For any fixed delta>0 and |x-d|>=delta, split the q integral at
|y-d|<delta/2. On that part (9) has a bounded separated kernel;
on the other part q is bounded and (7) applies. This proves a uniform
bound for z on all of I with |x-d|>=delta, including points tending
to either endpoint. More precisely, (8) and the support of q give

    z(x)<=v(d/2)||q||_1 V(x), 0<x<d/2,
    z(ell-x)<=C||q||_1 V(x) for sufficiently small x>0.        (15)

For the first inequality, y>=d and y-x+t>=d/2 in (8). For the
second, reflect the interval and use the positive distance of
[d,d+r] from ell. These are upper estimates, not zero normalized
V-traces.

The rho density is bounded on [-ell,ell], with removable value
rho(0)=3/4, as checked in L518. The k kernel is bounded there as
well. Their convolutions with z are therefore bounded by constants
times ||z||_1. Now at x=d+s every translated argument x+/-d_n
is either outside I or is separated from d by at least d/2 for
small s. There are finitely many displacements, all at least d.
Hence all translated z terms are bounded there by the preceding
away-from-d estimate. This includes arguments crossing the opposite
endpoint, where (15) gives a bound. At d_n=ell, or d_n>ell, both
compressed shifts are identically zero almost everywhere; no atom
has been removed from the formula.

It follows that

    (Bz)(d+s)=c z(d+s)+O(1)=O(1+1/(s L^(5/2))).             (16)

L518 gives R_L(d+s)=-w v(s)+O(1). For s<r/2 we have q(d+s)=w v(s)
exactly. Equations (1) and (16) prove the second bound in (3) for
the *full* residual, not just for its reference-operator part.

To verify the limitation (6), take x->0+. Then q(x)=0,
z(x)=O(V(x)), and among the positive shifts only z(x+d_2) approaches
the singular source location. Its bound from (3) is O(v(x)/log(1/x));
all other positive shifts are bounded and all negative shifts vanish.
The two continuous convolutions stay bounded. Thus Bz=o(v(x)),
whereas L518 gives R_L(x)/v(x)->-c. This proves (6) without an
endpoint-trace assertion for z.

### Admissible ordered limits and the unchanged trace coefficient

For every epsilon>0 from L518 and each finite m,
phi_epsilon+z_m belongs to Dom(A_I). Self-adjointness and A_Iu=0
give

    0=<u,A_I(phi_epsilon+z_m)>
     =<u,G_Iphi_epsilon-Bphi_epsilon>+integral_I u(q_m-Bz_m).

First fix m. L518's exact cutoff pairing, including its exterior
tail, gives as epsilon->0

    0=tau_L(u)+integral_I u[R_L+q_m-Bz_m].                    (17)

Next (11), q_m->q in L1, boundedness of B on L1 and boundedness
of u pass (17) to (5). Every integral is absolute by these estimates
and L518's absolute exterior bound. In particular the coefficient
of tau_L remains one; no trace term of z was discarded in passing
to this limit. At finite m its contribution was computed by the
operator-domain equality G_Iz_m=q_m, not by treating it as a raw
boundary density.

For clarity about the two parameters, the correction error in the
scalar pairing is bounded, independently of epsilon, by

    ||u||_infinity [||q-q_m||_1
                  +( |c|+||mu_A||_TV )||z-z_m||_1],

and the raw-cutoff error is exactly the one in L518, independent
of m. Both tend to zero separately. Thus reversing the iterated
limits yields the same scalar identity, although no uncut F is in
Dom(A_I), and distributional convergence by itself cannot produce
the boundary term. Equation (13) also verifies directly that the
new residual has precisely the old pairing with u.

This completes one correction. No iteration, summation of corrections,
sign estimate or endpoint flux conclusion is made.

### Separate conceptual audit, 2026-10-30

The prior approved EXPLORE assessment
`drafts/literature/2026-10-30-l525-single-green-correction-audit-coverage.md`
covers this independent application audit. Equations (1)--(6) pass;
no conclusion, constant or direct mathematical input is changed.
This is verification of the existing specialization (REPRODUCTION),
not a new theorem. GR's manuscript and the complete-Weil identification
remain imported, with the qualifications above.

**Reference kernel and inverse.** The exact GR v1 statements and the
essential separated/diagonal cases of Theorem 4.4 were checked against
the use above. At alpha=2 its additional term is V_GR(min(x,y));
on I this is bounded. Its other factor is at most one, and
log(2+1/t)>=log(1/t) for t<exp(-4). For t>=exp(-4) the remaining
factor is bounded on (0,ell]. Killing on I before the half-line exit
gives domain monotonicity. Thus (9) applies even when a point approaches
an endpoint; it never asserts a finite diagonal. The half-speed
normalization doubles the Green kernel and multiplies both renewal
factors by sqrt(2), preserving (7)--(8) with their stated constants.
The FOT part-process import is used only for the specified regular
symmetric form on the open interval, not a different fractional power
of a Dirichlet generator.

To make the spectral exclusion precise, fix 0<b<1/H. If the spectral
projection of G_I on [0,b] were nonzero, its integrated-semigroup
multiplier would be at least (1-exp(-Nb))/b on that range. For N large
this exceeds H, contradicting the Schur bound. Exhausting [0,1/H)
by such intervals excludes it, including zero. The same spectral
calculus gives strong convergence of the time integrals to G_I^(-1).
For nonnegative L2 data the increasing kernel integrals agree almost
everywhere with this limit; extension by linearity identifies the
inverse kernel. No property of the spectrum of A_I is inferred.

**Singular limit and transposition.** Symmetry turns the occupation
row bound into the column bound required in (11). Tonelli gives
the estimate for q and for q-q_m separately, and dominated convergence
gives ||q-q_m||_1->0. This proves L1 convergence, monotonicity and
almost-everywhere finiteness, without placing z in L2. The compact
smooth tests used in (12) have bounded G_I images and belong to its
operator domain by L518's form-core argument. Their pairings therefore
converge in exactly the dual L1/L-infinity topology asserted. Pairing
with u,h uses their established boundedness in the same way.
The finite measure has bounded L1 convolution norm, and evenness
legitimates its transpose after an absolute Fubini estimate. Thus
both (2) and (13) follow, but for different test classes; the former
alone is not used to infer the latter or a boundary coefficient.

**Complete cusp estimate.** The three regions of (14) give respectively
O(s^(-1)L^(-5/2)), O(s^(-1)L^(-5/2)) and
O(s^(-1)L^(-7/2)). In the middle region the integral of j is at most
2/L, so the diagonal singularity is integrable and loses no extra
power. In the last region r<exp(-8) ensures
1-7/(2log(1/t))>1/2; the upper endpoint contribution -J(r) is
nonpositive and can be dropped in an upper bound. Constants comparing
L with log(2/s) or log(1/(2s)) are fixed as s->0. Since the first
bound tends to infinity, it also absorbs the constant part of (9).
Division by the lower bound for v(s) gives O(1/L), as required.

Away from d, split the source near its singular endpoint and on the
bounded-density complement. The first part has uniformly separated
kernel arguments, the second is bounded by the row integral H.
This proves the claimed bound right up to both interval endpoints.
Formula (8) additionally yields (15) by separation of the support
from the respective endpoint; the right-hand separation is positive
because r<(ell-d)/4. In particular neither estimate says z/V->0.
For every translated argument at d+s, its distance from d is
|s+/-d_n|>=d-s>d/2 whenever the argument lies in I. The number of
atoms is finite. Both signs of every shift are therefore controlled,
including crossing endpoints; equality and larger shifts vanish after
compression. The two continuous kernels are bounded on I-I and
act on an L1 potential. Only c z retains the local singular order.
The exact q=w v(s) cancels L518's selected -w v(s); E_L and all
other raw terms are bounded near this fixed interior point. This
verifies (3) for the entire signed expression (4).

At the left endpoint, the only translated correction approaching d
is z(x+d_2); (3) bounds it by O(v(x)/log(1/x)). All other translated
arguments stay separated from d or outside I, and the continuous
terms are bounded. With z(x)=O(V(x))=o(v(x)), this proves Bz=o(v(x))
and retains the exact negative coefficient -c in (6).

**Boundary-reaching scalar limits.** Already at each finite m,
<u,q_m-Bz_m>=<G_Iu,z_m>-<u,Bz_m>=0 by the operator-domain
identity and symmetry of B. Its limiting equality is justified by
(11), not by cancelling formal singular distributions. For the raw
part, L518's cutoff limit supplies tau_L+<u,R_L> with coefficient
one in L513's normalization and with the complete exterior tail.
At fixed m these add to (17). The correction error displayed after
(17) is independent of epsilon; the raw-cutoff error is independent
of m. Hence both ordered scalar limits are legitimate and agree.
The boundedness of u makes every residual pairing absolute. No
normalization or hidden endpoint term can be lost in these limits.

The canonical DAG row is unchanged: L513 fixes the renewal/trace
normalization, L514--L515 give the realization and bounded nullvector
data, L516 supplies the complete model and L518 its residual/cutoff
pairing. The external GR and FOT inputs are cited in the proof.
The audited correction supplies no orthogonality beyond the old
pairing: (5) preserves it exactly. Other cusps, trace annihilation,
the O(lambda) family estimate, collars and Xi transfer remain open.

## Mathlib

Full matching coverage of this singular-source limit and complete
arithmetic adjoint specialization has not been checked. The imported
Green and renewal theorems are cited above; L513--L518 retain their
source qualifications. Supporting tools are the spectral theorem,
Schur's test, Tonelli, L1 convergence, finite-measure convolution and
elementary integral bounds. No matching Mathlib declaration, absence
claim or Lean verification is asserted.
