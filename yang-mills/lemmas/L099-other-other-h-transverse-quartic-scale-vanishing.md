# L099 — The transverse H generator has zero quartic-scale limit

## Hypotheses

Use exactly L095's R_H,tr for SU(2), both actual L010 probes i=3,6,
L018's residual, the straight lower-rooted direction-1 forest, relative
all-face pinned box (-4,4)^4, sufficiently fine admitted even N, a=8/N
and tau=1/16. Take the bare small-coupling coefficient at fixed mesh
before refinement. All coordinates and norms are ordinary stored ones.
Retain all interior axial levels, transverse end rows, ordered pairs
including coincidences, both generator orientations and every heat mode.

Import L088's actual Omega_k and real symmetric c_(i;kl,a), and put

    Pcal=I tensor P, Qcal=I-Pcal, K_g=M tensor P, M_st=min(s,t),
    K_h=(L_D+Delta_T)^-1 Qcal, A_k=Pcal Omega_k Qcal.

Here P is the transverse relative gradient projection. G_tr is the
complete transverse-displacement part of L009's generator, as defined
in L095, including all diagonal and cross-component terms. It acts
separately at each axial level and satisfies G_tr Pcal=0 (L096).
This selector identity is not an identity differentiated under a tilt.

## Conclusion

For both probes,

    lim_(N->infinity) a^4 R_H,tr=0.                         (1)

This excludes a nonzero quartic coefficient for this actual finite-box
trace. It supplies neither O(N^3) control nor an a^3-scaled limit.
Intermediate powers between N^3 and N^4, and even N^4/log N behavior,
are not excluded. In particular it does not complete the H diagonal
or the comparison of the complete other/other group with -12 gamma D_i.

More precisely, let R_H,tr,epsilon replace only K_h by
K_h,epsilon=(L_D+Delta_T+epsilon I)^-1 Qcal in (2) below. Uniformly
for 0<epsilon<=1,

    |a^4(R_H,tr-R_H,tr,epsilon)|<=C_i sqrt(epsilon).

For fixed epsilon, the axial-static reduction (6) has O_(i,epsilon)(N^3)
error, and a^4 R_H,tr,epsilon tends to zero. This order of limits is
essential. The displayed estimates do not control the mass error at
cubic scale: there the bound is C_i N sqrt(epsilon).

Other response jets, finer remainders and logarithm, interacting
matching and error <=c_box/2, continuum axioms, reflection positivity,
infrared control and finite positive mass remain unresolved.

## Proof

### 1. Preserve both orientations and the complete finite trace

Inserting the transverse generator in L095(1)--(2) and transposing
the second real scalar trace exchanges k,l. Symmetry of c_(i;kl,a)
therefore uses its factor 1/2 exactly once and gives

    R_H,tr=sum_(k,l)c_(i;kl,a)
                 Tr(K_h A_l^T K_g A_k G_tr).              (2)

The adjacent Qcal projections are removed using A_k Qcal=A_k and
Qcal A_l^T=A_l^T. No projection is commuted through a multiplier.
This equality also holds after replacing K_h by K_h,epsilon: that
replacement is symmetric and supported on Qcal. It defines a trace
regularization, not a changed Gaussian contraction or action group.

Identify the identical transverse spaces at each level. Let
W_k(t)=A_k(t)G_tr(t). L095(7) supplies

    ||A_k(s)||<=Ca p(k),
    ||A_k(s+1)-A_k(s)||<=Ca^2 p(k).

L009's finite stencil gives ||G_tr(s)||<=C/a. An axial difference
of its coefficients is O(1): u_a changes by O(a) over one level,
while all transverse incidences and averaging maps are fixed.
Bounded row and column multiplicity, including relative end rows,
therefore implies

    ||W_k(s)||<=C p(k),
    ||W_k(s+1)-W_k(s)||<=Ca p(k).                       (3)

The polynomial p can be enlarged throughout without losing L088's
full heat-sum bound sum |c_(i;kl,a)|p(k)p(l)<=C_i. The displacement
vanishes in fixed physical collars of the two axial endpoints, so
G_tr and W_k vanish there. This does not assume that A_k vanishes
there or extend the forest potential smoothly across its upper pin.

The exact block multiplying K_h in (2) is

    B_(kl;st)=min(s,t) A_l(s)^T W_k(t).

It obeys ||B_(kl;st)||<=C p(k)p(l) N a<=C' p(k)p(l).
Unlike L098's differentiated-prefix block, this is only O(1).

### 2. Control mass removal at its actual scale

For R_lambda=(L_D+lambda)^-1 the positive scalar kernel satisfies

    sum_t (R_lambda-R_(lambda+epsilon))_st
                       <=epsilon/[lambda(lambda+epsilon)].

This is L098(5), following from the resolvent identity and L095's
minimum principle and inverse-mass row sums. Each transverse block
of K_h-K_h,epsilon is positive semidefinite by spectral decomposition
on Q. The trace norm of such a block equals its trace. Applying the
block bound above before summing all levels gives

    |R_H,tr-R_H,tr,epsilon|
      <=C_i (N-1) Tr_Q[epsilon/(Delta_T(Delta_T+epsilon))]
      <=C'_i N^4 sqrt(epsilon).                         (4)

For applicability, the full three-dimensional relative spectrum has
lambda>=4r^2/N^2 and at most Cr^2 labels in shell max m_j=r, including
all components. Its trace is at most
C epsilon N^4 sum_(r>=1) 1/(r^2+epsilon N^2)
<=C N^3 sqrt(epsilon), by the decreasing-integrand comparison on
[0,infinity). This retains low physical modes and every pinned row.
Multiplying (4) by a^4 proves the asserted uniform scaled error.
Multiplication by a^3 instead leaves the extra N; it cannot be dropped.

The same argument with inverse-mass row sums, without their difference,
gives |R_H,tr,epsilon|+|R_H,tr|<=C_i N^4, uniformly in epsilon.
This bound also holds modewise with C_i replaced by Cp(k)p(l).

### 3. Localize only the regularized axial kernel

Fix epsilon>0. For all interior s,t, (3) and
|min(s,t)-s|<=|t-s| imply

    ||B_(kl;st)-s A_l(s)^T W_k(s)||
                                      <=Ca p(k)p(l)|t-s|.          (5)

Indeed the prefix difference costs Ca p(k)p(l)|t-s|; the W difference
costs C s a^2 p(k)p(l)|t-s|, with s a<=8. This estimate uses the
complete prefix, not a diagonal replacement before estimation.

L098(8)'s massive scalar kernel r_m(j)=exp(-kappa|j|)/(2sinh kappa),
where 2cosh kappa-2=m, dominates the finite Dirichlet inverse and has
sum_j(1+|j|)r_m(j)<=C_epsilon for epsilon<=m<=13. Consequently

    sum_(s,t)(1+|t-s|)||(K_h,epsilon)_ts||_1
                                                    <=C_epsilon N^4.

Using (5) in (2) costs at most C_(i,epsilon) a N^4=O_(i,epsilon)(N^3).
On the support of W_k(s), both axial endpoints are distance >=cN away.
The massive Dirichlet row sum differs from 1/(lambda+epsilon) by at
most C_epsilon exp(-c_epsilon N), uniformly over the transverse spectrum.
This is the boundary-deficit recurrence estimate in L098, proof
section 3. Spectral decomposition proves the same operator-norm bound
for the transverse blocks. Multiplying by s A_l(s)^T W_k(s), summing
all transverse rows and all levels, costs a polynomial times this
exponential. Outside that support the product is zero. Thus

    R_H,tr,epsilon
      =sum_(k,l)c_(i;kl,a) sum_s s
         Tr_T[C_epsilon A_l(s)^T A_k(s) G_tr(s)]
            +O_(i,epsilon)(N^3),
    C_epsilon=(Delta_T+epsilon)^-1 Q.                    (6)

No variable coefficient has crossed C_epsilon, P or Q. All transverse
end rows are still present. The O_(epsilon)(N^3) error is negligible
at quartic scale only; it is not claimed negligible at cubic scale.

### 4. Control the finite transverse trace before freezing

Set alpha_k=A_k/a and g=a G_tr. Multiplying (6)'s main term by a^4
gives

    a^4 sum_(k,l)c_(i;kl,a) sum_s (a s)
                   Tr_T[C_epsilon alpha_l(s)^T alpha_k(s) g(s)].    (7)

The normalized factors have mesh-independent operator bounds polynomial
in their mode labels, and ||C_epsilon||<=1/epsilon. The coefficient
differences in Omega_k/a are O(a p(k)) on existing neighboring rows:
the path terms follow from L090(6); the exterior-circulation terms
are themselves O(a p(k)). The underlying normalized exterior edge
fields have the same smooth interior differences by L028's exact
prefix formula, as used in L090. The coefficients of g have O(a)
neighbor differences and compact displacement support.

For delta>0 replace every occurrence of P by
P_delta=T(Delta_0+delta)^-1 T^T and Q by Q_delta=I-P_delta,
including those inside alpha and C_epsilon. L097's full spectral
bound gives ||P-P_delta||_HS<=C N^(3/2) sqrt(delta).
All replacements have bounded operator norm. Telescoping each product
in (7), trace Cauchy--Schwarz pairs this Hilbert--Schmidt error with
a bounded product of Hilbert--Schmidt norm O_(epsilon)(N^(3/2)).
Since a^4 sum_s(a s) N^3<=C, the total normalized error is at most
C_(i,epsilon) sqrt(delta), uniformly in N.

For fixed epsilon,delta approximate each inverse on [0,12] by L097's
geometric polynomial

    p_(t,m)(x)=(12+t)^-1 sum_(j=0)^m [1-(x+t)/(12+t)]^j,
    sup |p_(t,m)(x)-(x+t)^-1|<=t^-1[12/(12+t)]^(m+1).

The finite spectral theorem and telescoping products bound the
normalized error uniformly in N by C_(i,epsilon,delta) times these
approximation errors. This leaves finite-range real operators.
For fixed degrees a transverse collar of that range has O(N^2) rows
per level. Its bounded normalized entries contribute O(1/N) to (7).
On other rows every closed walk stays in the interior. Coefficients
can be replaced by their values at a common physical cell, with
O(a p(k)p(l)) error per diagonal entry. The normalized sum of these
errors is O_(epsilon,delta,m)(a p(k)p(l)).

In particular the O(a) exterior-circulation part of Omega_k/a is
included in this error. For the remaining path/curvature terms,
the actual smooth exterior field divided by a can be frozen to a
real transverse vector v_k at that cell. Fixed staggered offsets
change this vector by O(a p(k)). Both paths and their imaginary
symbol parts must be retained; the following cancellation uses them.

### 5. Cancel the full frozen generator, not individual multipliers

At transverse frequency theta put d_j=2 sin(theta_j/2) and
eta_j=cos(theta_j/2), for j=2,3,4. L088(11)--(13) proves that the
frozen symbol of Omega_k/a is i S_k, with S_k real symmetric, when
the exterior field is the real constant a v_k. This includes the
exact two-edge paths. The derivation is imported, not reproved or
replaced by opposite-edge averages.

The complete frozen transverse generator g has symbol i W, W real,
with

    W_(nu nu)=eta_nu^2 sum_(rho!=nu) u_rho eta_rho d_rho,
    W_(nu rho)=-u_rho eta_rho eta_nu^2 d_nu  (rho!=nu),              (8)

where only transverse indices occur. These are L088(14)'s actual
filters restricted to the displacement terms defining G_tr. They
give W d_T=0, consistently with L096's exact gradient annihilation.
W need not be symmetric and individual diagonal filters are not
commuted with P.

The frozen symbols of P_delta, Q_delta, their polynomial replacements,
and C_epsilon's corresponding replacements are real symmetric in
component-center phases. Denote the last symbol by C. The frozen
alpha_k therefore has form i E_k with E_k real (not necessarily
symmetric). For a fixed pair k,l define

    B_kl=(E_l^T E_k+E_k^T E_l)/2.

B_kl is real symmetric. After the exterior k,l symmetrization, the
integrand of (7) has the form i Tr(C B_kl W). One must not declare
this single orientation zero pointwise. Its adjoint orientation is
-i Tr(C W^T B_kl). The two traces are equal as real numbers, since
transposing the first and cycling yields

    Tr(C B_kl W)=Tr(W^T B_kl C)=Tr(C W^T B_kl).

Their sum is therefore zero pointwise. The adjoint orientation is
legitimate here: the finite real trace in (7) equals the trace of
its transpose. Averaging those two exact expressions before taking
the frozen symbol retains both orientations, rather than assuming
that a real-matrix transpose acts within a single Fourier frequency.
This argument also holds for the regularized polynomial symbols;
it does not require that their projection approximations be idempotent.

Thus, for fixed epsilon,delta and polynomial degrees, the symmetrized
frozen trace is identically zero. The actual normalized finite trace
differs from it by the collar and coefficient errors in section 4,
which tend to zero as N grows. Then send the polynomial degrees to
infinity and delta to zero using the uniform approximation errors.
For each fixed epsilon this proves that (7) tends to zero.

All estimates hold for the symmetrized pair with a fixed polynomial
majorant p(k)p(l). L088's uniform full heat tail (exponential damping
against fixed polynomials, with the relative spectral gap) permits
truncation in exterior labels uniformly in N and subsequent removal
of that truncation. No exterior mode is discarded from the result.

By (6), a^4 R_H,tr,epsilon tends to zero. Equation (4) now gives

    limsup_N |a^4 R_H,tr|<=C_i sqrt(epsilon).

Send epsilon to zero to prove (1). There is no exchange of an
uncontrolled singular limit with a finite trace.

### 6. What this attempt does and does not pass

This is a specialization of the recorded finite spectral, axial-kernel
and finite-range trace methods to the gh/hg H trace. L090's cubic
estimate for the hh sector cannot be imported at this normalization:
the undifferentiated prefix block in section 1 is O(1). At cubic
scale (4) leaves N sqrt(epsilon), so taking N to infinity first fails.
Choosing epsilon depending on N is also unsupported: localization,
inverse approximation and collar constants depend on epsilon. The
proof does not establish a uniform rate that repairs those constants.

Consequently fixed-mass leading-symbol cancellation alone is parked
as a route to cubic control. The new actual quartic-scale exclusion
is retained, while a quantitative signed estimate uniform at cubic
scale, or a different independently testable remaining trace, is needed.
No failed upper bound is interpreted as signed growth.

Completed RESEARCH / REPRODUCTION under the unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`.
This is local standard-method progress, not certified originality or
a result beyond the methods of the checked sources. No numerical
certificate or value of D_i is used; any later numerical comparison
retains L082's saved-table/IEEE qualifications through L084.

## Mathlib

Full matching finite-trace asymptotic: **not checked**. Supporting
finite-dimensional spectral, trace-ideal, polynomial-approximation
and geometric-series coverage: **not checked**. Unknown availability
is not evidence of absence. No general flow or Ward theorem assigns
the coefficient of this isolated forest group.
