# Corollary 663a: the lattice endpoint route leaves a necessary bottom contribution

## Hypotheses

Use exactly L663's admissible unit-residue lattice: n=6q+3, q>=1,
x=-d=-5/4, R=11/8, U=121/64, eta=1/100, Y=9/20,
h=27/(10n), a_l=x+i*l*h for -q<=l<=q, and r_(a_l)=1.
Thus M=2q+1=n/3. Retain t_j=j/n for every 0<=j<n and

    B_u(v)=product_(j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    c_k(u)=R^(-1) sum_(l=-q)^q W_(a_l)(u)*(a_l/R)^k,
    G(u,zeta)=sum_(0<=k<M)c_k(u)*zeta^k,
    D=sum_(l=-q)^q mean_u |W_(a_l)(u)|^2/(U-|a_l|^2),
    H=max_u mean_zeta log|G(u,zeta)|.

Both means are normalized circle means, |u|=|zeta|=1, and logarithms
are natural. In particular 1/u is the conjugated denominator angle.
No original mass is replaced by a fractional or unsquared mass.

Let Gamma be L663's positively oriented y-plane rectangle
[-Y,Y]+i[-b,c], where b=2/25 and c=1/8. Write

    lambda=20*pi/27,
    K_n(y)=i*lambda*n/(exp(i*lambda*n*y)-1),
    T_M(w)=sum_(0<=k<M)w^k,
    C_*= (221/100)*lambda*exp(8)/(3*pi*R),
    gamma=29/1000, rho_*=261/20000.

Define the complete signed lower-edge polynomial, with its actual
left-to-right contour orientation, by

    Bcal_n(u,zeta)=(1/(2*pi*i*R)) integral_(-Y-i*b)^(Y-i*b)
                W_(x+i*y)(u)*K_n(y)*T_M((x+i*y)*zeta/R) dy,
    Bcal_n(u,zeta)=sum_(0<=k<M) ell_k(u)*zeta^k.

This definition retains the exact kernel and all M spatial moments.
It makes no single-frequency, saddle or noncancellation assumption.

## Conclusion

For every n in this family and every u on the circle,

    |W_(x+i*Y)(u)|, |W_(x-i*Y)(u)| <= exp(8-gamma*n),       (1)
    sup_(u,zeta) |G(u,zeta)-Bcal_n(u,zeta)|
                                      <=C_* n^2 exp(-gamma*n), (2)
    max_(u,k=0,1) |c_k(u)-ell_k(u)|
                                      <=C_* n^2 exp(-gamma*n). (3)

In fact (3) holds for every 0<=k<M. Equations (2)--(3) bound the
combined top and both side contributions, keeping their signs in
the exact identity before applying an absolute bound. They do not
bound the bottom contribution itself.

Put s_n=max_(u,k=0,1)|c_k(u)| and b_n=max_(u,k=0,1)|ell_k(u)|.
Then

    |s_n-b_n|<=C_* n^2 exp(-gamma*n).                         (4)

For fixed A>=0 and rho<rho_*, a lower bound of the form
c n^(-A) exp(-rho*n), with c>0 and one onset, holds for s_n if
and only if it holds for b_n, allowing c and the onset to change.
The strict error-rate gap is

    gamma-rho_* =319/20000 >0.                               (5)

Either lower bound would imply a paid arc for this lattice with
excess over log D-n/16 at least

    2*(rho_*-rho)*n-(2A+5)*log n-C.                          (6)

Neither lower bound is proved. The proposed endpoint-dominated
two-coefficient proof is stopped: its complete top/side contribution
is exponentially smaller than the sufficient scale. Any proof at
that scale must obtain a signed response from Bcal_n. Even a perfect
noncancellation argument for the endpoint pair cannot supply it.

This does not disprove the localized criterion or give a necessary
exponent for that criterion. The diagonal envelope used in (6) is
only an upper bound, and a two-coefficient certificate is only a
sufficient route. In particular (2) does not imply that logarithmic
means of G and Bcal_n are close near zeros. No estimate of b_n, H,
or the signed bottom integral at the required scale is asserted.
General support, Xi realization and signs remain open. The conceptual
audit in C663b section 7 checks this corollary's contour remainder,
coefficient transfer and paid-cost conclusions. It subsequently proves
a bottom lower bound; the absence of such a bound asserted here
describes this corollary alone. The endpoint-dominance stop remains.

## Proof

### 1. Scope, imported tools and prior stops

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`.
It covers the original paid criterion and quantitative isolation of
a remaining term with all spatial, angular and diagonal costs.
L663 supplies the exact finite contour, analytic clearances, product
quadrature, vertical monotonicity and audited interval evidence.
L661 supplies only its general-family diagonal envelope in section 4
below; its special phase census is not substituted for this lattice.
L658 supplies the paid localization of H used there.

The contour input, already inspected and imported in L663, is
R. W. Howell and J. H. Mathews, *Complex Analysis*, online edition,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html)
and [Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
The spatial root formula used below is F. Brunault and W. Zudilin,
*Many Variations of Mahler Measures*, ISBN 9781108794459,
[Proposition 1.4, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
including boundary roots. Their source manuscripts are not newly
audited. No general residue, Jensen or norm theorem is reproved.

The full-circle obstruction, half-turn signed-census result, its
earlier absolute-cost stop, the deweighting limitation and the finite
localized-screen failure were compared. None supplied the uniform
top/side estimate (2) or settled the present lattice's best arc.
L662's elementary coefficient-to-Mahler argument is a methodological
comparison; its special-family endpoint conclusion is not an input.
The new maximum aggregation is necessary because L663 certified an
angular mean rather than this bound on three entire contour edges.
POTENTIALLY_NEW denotes only the scope of the recorded search, not
certified originality or progress beyond all known literature.

### 2. The uniform angular bound on the top and both sides

Use L663's real function

    f(t,u,a)=log|(x-t*u)/(a-t*u)|
                        +log|(U*u-t*a)/(U*u-t*x)|,
    beta(a)=(1/3)log max(1,|a|/R),
    F(theta,s,v)=integral_0^1 f(t,e^(i theta),x-v+i*s) dt
                         -lambda*(-v)_++beta(x-v+i*s).

For every fixed (s,v) on Gamma, its angular second derivative is
bounded below by -100; the nonintegral terms do not depend on theta.
This is the full clearance bound (8) in L663, not a derivative
estimate inferred from numerical grid values. For a compact edge,
the maximum of F+(100/2)*theta^2 is convex. Therefore the maximum
over that edge is bounded above, on an angular interval of length
delta, by the chord of its endpoint values plus 100*delta^2/8.
This also follows directly by applying the same chord inequality
to each fixed (s,v) and then taking its maximum.

At each of theta_k=k*pi/512, k=0,...,512, the audited L663
certificate gives upper bounds for the top and both side maxima.
For the top, its row includes the full spatial cost
(1/6)log[(U+Y^2)/U]. For a side, L663's monotonicity proves that
its maximum is at v=0 and hence equals

    alpha_+(theta)=integral_0^1 f(t,e^(i theta),x+i*Y)dt,
    alpha_-(theta)=integral_0^1 f(t,e^(i theta),x-i*Y)dt,

respectively. Here beta=0 since d^2+Y^2<U. That monotonicity already
counts the spatial cost when |x-v+i*Y|>R and the kernel decay below
the real axis. It is not a two-endpoint sampling assumption.

All 513 source rows include the t-quadrature charge
70/(12*128^2), rounded upwards. Put S=2^72. The maxima of their
top, positive-side and negative-side upper entries are respectively

    -144532751754242218129/S,
    -140704438796847698369/S,
    -141564809277796133564/S.

Use pi<22/7 from the audited arithmetic. The angular chord charge is

    (100/8)*(22/(7*512))^2 =3025/6422528.

After this charge the three continuous upper bounds are, respectively,

    -6973117724975502685121/231395957660612615471104,
    -6785530390063171216881/231395957660612615471104,
    -1706922135907411135359/57848989415153153867776.

Each is strictly below -29/1000. The exact check covers every one
of the 512 angular intervals, for all three bounds. Conjugation
theta -> -theta preserves the top maximum and interchanges the two
side maxima, so the entire angular circle is covered. Thus

    max_(top and both sides) F(theta,s,v) <=-gamma        (7)

uniformly in theta. No bound for the bottom maximum is included.
L663's finite-product error sum_j f<=n integral f+8, applied at
y=+/-Y, now gives (1).

### 3. Exact lower-edge isolation and uniform error

L663 proves that W_(x+i*y)(u) is holomorphic on the full rectangle
and that K_n has precisely its 2q+1 simple lattice poles there,
each of residue one and none on the boundary. Thus its identity is

    G=(1/(2*pi*i*R)) integral_Gamma W*K_n*T_M dy.

Splitting this finite contour leaves Bcal_n plus the top and two
sides with their original orientations. This operation discards no
residue or kernel term. On all edges L663 gives

    |K_n|<=2*lambda*n*exp(-lambda*n*(-v)_+),
    |W|<=exp(8+n integral_0^1 f dt),
    |T_M|<=M*exp(n*beta),

uniformly on both circles. Their product on the three selected edges
is at most 2*lambda*n*M*exp(8-gamma*n), by (7). Their total length
is at most the full length 221/100. Since M=n/3, division by
2*pi*R proves (2) with exactly C_* as stated.

The integrals are finite and the spatial sum is finite. For any
k<M we may extract its coefficient before integrating. On the
contour

    |(x+i*y)/R|^k <= max(1,|(x+i*y)/R|)^(M-1)
                                  <=M*exp(n*beta).

The same estimate therefore proves (3), even for all k<M. This
does not estimate a truncated replacement for G: the full polynomial
has already been bounded in (2). Continuity on the angular circle
and the triangle inequality give (4).

Since gamma-rho>gamma-rho_*=319/20000, the ratio of the error in
(4) to n^(-A)exp(-rho*n) is bounded by
C_* n^(A+2)exp(-(gamma-rho)*n), which tends to zero. Absorb it
by reducing a proposed positive lower constant by a factor of two.
This proves the two directions of the stated lower-bound transfer.
It supplies no such bound for either sequence.

### 4. Why the target rate is sufficient, and what the stop means

For a nonzero complex polynomial P of actual degree d_P, the cited
root formula gives exp(mean log|P|)=|lc(P)| product max(1,|alpha|).
Its constant coefficient is bounded by this product; its first
coefficient, when d_P>=1, is a sum of d_P products of d_P-1 roots,
so is bounded by d_P times the same product. For a constant
polynomial the first coefficient is zero. Zero roots and boundary
roots are included; no coefficient integrality is needed.

L658 verifies that every spatial slice of G is nonzero, including
exceptional angles. Its degree is at most M-1, so

    max(|c_0(u)|,|c_1(u)|)<=M*exp(mean_zeta log|G(u,zeta)|).

Consequently s_n>=c n^(-A)exp(-rho*n) would give
H>=-rho*n-(A+1)log n-C. L658 then supplies an arc of measure
n^(-2) whose paid logarithmic expression is at least
2H-2log n-32*pi^2/9. The general envelope of L661, applicable to
this original unit-residue family, gives

    D<=n*exp(2*kappa*n+6)/(3*sigma^2),
    kappa=91/5000, sigma^2=137/5000.

Here sum_l r_(a_l)^2=n/3 exactly. Combining the inequalities gives
the excess at least

    (1/16-2*kappa-2*rho)*n-(2A+5)log n-C,

which is (6), because 1/32-kappa=rho_*. The onset is existential.

The entire endpoint/top mechanism in (2)--(3) is too small for this
sufficient scale, by (5). If the bottom were negligible at that
scale as an endpoint-dominated expansion requires, then s_n would
also be negligible at that scale. This is the precise obstruction.
A large bottom term is compatible with every bound proved here.
The original logarithmic criterion might also hold by a different
coefficient or a sharper comparison with D. None is ruled out.

### 5. Verification and qualifications

Run

    python3 scripts/one-sided-hankel/lattice-endpoint-remainder.py

The complete certificate is
`scripts/one-sided-hankel/lattice-endpoint-remainder.json`.
The program reads all 513 angular rows, checks equality with their
complete prior replay in L663, retains the already paid t-error,
and checks all three chord bounds on every one of 512 intervals.
It also verifies the inherited replay status, absence of failures,
global arithmetic record, and the exact threshold gap (5).
All checks pass; the full extrema and failures fields were inspected.

This new computation is exact aggregation of previously audited
interval evidence. It is neither a fresh interval-backend replay nor
an independent arithmetic implementation. L663's analytic derivative
and contour hypotheses are essential imported mathematical inputs.
No finite-n numerical screen, midpoint diagnostic or sampled angle
alone is a premise. The exploratory JSON files
`scripts/one-sided-hankel/lattice-endpoint-diagnostic.json` and
`scripts/one-sided-hankel/lattice-endpoint-maximum-diagnostic.json`
are explicitly noncertifying and are preserved separately.

### 6. Audit scope — 2 November 2026

C663b section 7 checks the whole top/side aggregation and its use on
shortened sides, retaining the spatial and kernel corrections in the
vertical monotonicity. All three edge bounds are pointwise before
integration. The chord charge applies to every angular interval and
conjugation covers the remaining half circle. Thus (2)--(3) keep
the exact signed contour before their absolute error estimate.
Triangle inequalities give (4); gamma-rho>319/20000 makes the error
negligible for either lower-bound transfer with fixed A. The full
root formula bounds both selected coefficients by M times the
Mahler measure. Combining this with L658 and L661 gives precisely
(6), including its (2A+5)log n cost. No bound on logarithmic
differences near zeros is inferred.

The existing aggregation program was read and rerun: every one of
the 513 source rows matches its prior audited replay, and each of
the three charged bounds on all 512 intervals is below -29/1000.
The complete summary, all checks and empty failure list were
inspected. This reuses L663's audited interval backend and derivative
coverage; it is not an independent backend or source-manuscript
audit. No constants, hypotheses or mathematical conclusions are
changed. C663b records the signed-bottom result separately.

## Mathlib

No full matching theorem for (1)--(7), this lower-edge isolation or
its interval certificate has been checked. The reused source review
inspected supporting univariate results in
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`
and `Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`.
These do not establish this family-specific contour bound. Analytic
nonzero hypotheses and boundary-root qualifications remain explicit;
unknown wider coverage is not evidence of absence.
