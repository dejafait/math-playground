# Lemma 658: bounded localization cost at a spatial logarithmic maximum

## Hypotheses

Retain the complete family of L657: n>=5, x=-5/4, R=11/8,
U=R^2, eta=1/100, r_*=R-eta=273/200 and t_j=j/n. The common
set Z has N distinct poles on Re(a)=x with |a|<=r_* and x in Z.
Their original residues r_a are positive integers with
M=sum_a r_a<=n/3. All grid factors and the conjugated angle remain:

    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    G(u,zeta)=sum_(0<=k<M) [R^(-1) sum_a r_a W_a(u)(a/R)^k] zeta^k,
    D=sum_a r_a^2 mean_u |W_a(u)|^2/(U-|a|^2).

Thus D is D_single,n. There is no separation, symmetry or integrality
of polynomial coefficients. Circle measures and arc means are normalized;
logarithms are natural. Write

    m(theta)=mean_zeta log|G(e^(i theta),zeta)|,
    H=max_theta m(theta).

The finiteness and attainment implicit in this notation are proved below.
Use L657's exact clearing G=K/Q, where J=n-1 and

    Q(u)=C_x(u) product_(a!=x) A_a(u),
    C_x(u)=product_(1<=j<n)(U*u-t_j*x),
    A_a(u)=product_(1<=j<n)(a-t_j*u).

K is L657's full polynomial numerator, not a spatial truncation of that
numerator. Its angular degree is at most d_ang=NJ, and Q has degree
d_ang. The spatial polynomial G already contains exactly its prescribed
first M moments.

## Conclusion

H is finite and attained. Choose any maximizing angle theta_m, and let
I_m be its centered connected arc with normalized length n^(-2).
Then

    mean_(I_m) m >= H-16*pi^2/9,                         (1)

and consequently

    log mu(I_m)+2 mean_(I_m x T) log|G|
                  >=2H-2log n-32*pi^2/9.               (2)

Every allowed arc I, of any length at least n^(-2), also obeys the
elementary upper bound

    log mu(I)+2 mean_(I x T) log|G| <=2H.               (3)

Thus angular localization of the *complete* spatial logarithmic mean
has a bounded loss on this particular arc, apart from the explicit
2log n measure cost. The estimate is uniform in the family, including
angular boundary zeros, spatial zeros, angular degree drops and
arbitrarily close poles. No signed cross term or zero/pole charge has
been discarded.

For the approved rate-1/16 criterion, a sufficient remaining estimate is

    H >= (log D)/2-n/32+log n.                          (4)

It would give that criterion with C=32*pi^2/9. Conversely, the criterion
with constant C requires H>=(log D)/2-n/32-C/2 by (3). Neither bound
on H relative to D is established here. The logarithmic difference
between these sufficient and necessary thresholds is retained; this
does not assert equivalence with identical constants at rate 1/16.

The center theta_m maximizes m, not the diagonal. This does not bound
L657's A_0 at a diagonal-maximizing angle. It supplies another uniform
localization cost and leaves the central correlated-response estimate,
actual-Xi realization, matching upper bounds and all-degree signs open.
The full localization argument and its required nonzero-slice and
integrability hypotheses were checked in L662's conceptual audit of
2 November 2026. That audit reuses the named source theorems; it does
not independently audit their manuscripts or assert a bound for H.

## Proof

### 1. Source scope and logarithms

The unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`
covers the exact arc criterion and its full zero/pole/localization costs.
L657 supplies the rational clearing, nonzero angular and spatial slices,
absolute product logarithmic integrability, and the degree bound.
Its primary integrability input is Z. Issa and M. Lalin,
*A generalization of a theorem of Boyd and Lawton*,
[arXiv:1203.5379v1, Remark 3.8 and Theorem 4.1/proof, printed p.7](https://arxiv.org/pdf/1203.5379v1),
24 March 2012, with s=1. No uniform small-value theorem is assumed.

Import the exact one-root circle integral from F. Brunault and
W. Zudilin, *Many Variations of Mahler Measures*, ISBN 9781108794459,
[Proposition 1.4, publisher excerpt pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf):
the mean of log|e^(it)-beta| is log max(1,|beta|), including boundary
roots. The prior assessment inspected its three modulus cases.
The weighted root formula below is a direct specialization by a disk
change of variables. This calculation is needed to retain a uniform
constant on the prescribed shrinking arc; no general Jensen or
integrability theorem is reproved. The result is reported as a standard
potential-theoretic specialization, not a certified new discovery.

G is continuous on the product torus and bounded there; its denominator
has no angular boundary zeros. For each fixed theta its spatial slice
is a nonzero polynomial, so m(theta) is finite by the cited root formula.
Its absolute angular integrability follows from L657 and Fubini.
It is also upper semicontinuous: log|G|, interpreted as -infinity at
zeros, is the pointwise limit along any convergent sequence of angles,
and has a common finite upper bound. Apply Fatou's lemma to that bound
minus log|G|. The resulting inequality is
limsup m(theta_l)<=m(theta) when theta_l->theta. Hence m attains a
finite maximum on the circle. No assumption that G is nonvanishing
on the product torus is made.

### 2. Weighted one-root identity, including boundary roots

For 0<s<1 define the normalized Poisson kernel and its averaging
operator by

    P_s(t)=(1-s^2)/(1-2s cos t+s^2),
    (P_s*f)(theta)=mean_t P_s(t) f(theta+t).

For |gamma|<=1 and |u_0|=1, the exact formula is

    mean_t P_s(t) log|1-gamma*u_0*e^(it)|
                        =log|1-s*gamma*u_0|.            (5)

To justify this directly from the imported root identity, make the
circle change of variables w=(s+v)/(1+s*v), |v|=1. It is a smooth
orientation-preserving bijection. Differentiating its inverse
v=(w-s)/(1-s*w) gives d arg v/d arg w=P_s(arg w).
In particular mean P_s=1, and the left side of (5) becomes

    mean_v log|[(1-s*gamma*u_0)+(s-gamma*u_0)*v]/(1+s*v)|.

Put A=1-s*gamma*u_0 and B=s-gamma*u_0. A is nonzero and

    |A|^2-|B|^2=(1-s^2)(1-|gamma|^2)>=0.

The root identity therefore gives mean log|A+B*v|=log|A|,
including equality |A|=|B| and B=0. It gives mean log|1+s*v|=0
as well. This proves (5), with integrable boundary zeros treated by
the same cited identity and a smooth change of variables.

For any beta in C, on the angular circle write

    log|u-beta|=log max(1,|beta|)+log|1-gamma*u|,
    gamma=conjugate(beta) if |beta|<=1,
    gamma=1/beta if |beta|>1.

Thus |gamma|<=1 in all cases. The elementary identity

    |1-s*gamma*u_0|^2-s*|1-gamma*u_0|^2
                       =(1-s)(1-s*|gamma|^2)>=0

and (5) show that averaging any single root factor loses at most
-(log s)/2 relative to its boundary value. A zero at u_0 gives the
value -infinity and satisfies the extended-real inequality. Factoring
a nonzero polynomial F of actual degree d_F consequently gives

    (P_s*log|F|)(theta)
                      >=log|F(e^(i theta))|+(d_F/2)log s. (6)

The leading coefficient is retained as a constant. Equation (6) uses
the actual degree, so degree drops introduce no roots at infinity.

### 3. All numerator roots and all denominator roots

Apply (6) to K(.,zeta) for each spatial zeta. L657 proves that none
of these angular polynomials is identically zero for |zeta|=1, and
that its degree is at most d_ang. Since log s<0, (6) remains valid
with d_ang in place of its actual degree. Integrating in zeta gives

    P_s*(mean_zeta log|K|)(theta)
       >=mean_zeta log|K(e^(i theta),zeta)|+(d_ang/2)log s. (7)

For each fixed s<1, P_s is bounded. L657's absolute product
integrability justifies Fubini in (7). For the fixed center theta,
its spatial polynomial is nonzero and has a finite logarithmic mean;
its finitely many spatial boundary zeros do not change the integrated
inequality. Thus this step keeps the complete spatial logarithmic mean,
including every spatial root and leading factor.

The roots of C_x are p_j=t_j*x/U, with modulus <80/121<4/5.
The roots of A_a are a/t_j, of modulus >d=5/4. Their reflected
parameters gamma in (5) therefore all have modulus <4/5 too.
Q has precisely d_ang such factors, with multiplicity. For each,

    |log|1-s*gamma*u|-log|1-gamma*u||
       <=integral_s^1 |gamma|/(1-v*|gamma|) dv
       <=4(1-s).

Using (5), summing all factors and retaining the leading constant gives

    |P_s*log|Q|(theta)-log|Q(e^(i theta))||
                                      <=4*d_ang*(1-s).  (8)

Common K/Q factors are counted on both sides with opposite signs;
none is omitted. Subtract (8) from (7), using log|G|=log|K|-log|Q|:

    (P_s*m)(theta)
       >=m(theta)+(d_ang/2)log s-4*d_ang*(1-s).           (9)

The loss in (9) is proportional to d_ang*(1-s), rather than to
d_ang alone. This is the quantitative feature used on the n^(-2) arc.

### 4. Converting the weighted estimate to the required arc

Set h=pi/n^2 and s=1-h. Since n>=5 and pi<4, 0<h<1/4.
The inequality -log(1-h)<=h/(1-h)<=4h/3 in (9), evaluated at
theta_m, implies

    0<=P_s*(H-m)(theta_m)<=(14/3)*d_ang*h.              (10)

Here H-m>=0 on the entire angular circle, not just on I_m. For
|t|<=h, use 1-cos t<=t^2/2 to obtain

    1-2s cos t+s^2=h^2+2s(1-cos t)<=2h^2,
    1-s^2=h(2-h)>=(7/4)h,
    P_s(t)>=7/(8h).

The arc has normalized measure h/pi=n^(-2). Positivity of H-m
allows restriction of its Poisson integral to I_m, so (10) yields

    [7/(8*pi)] mean_(I_m)(H-m)
       <=P_s*(H-m)(theta_m)<=(14/3)*d_ang*h.

The positive integer residues imply N<=M<=n/3. Hence
d_ang=N(n-1)<=n^2/3, and it follows that

    mean_(I_m)(H-m)<=(16*pi/3)*d_ang*h<=16*pi^2/9.

This proves (1). Substitute log mu(I_m)=-2log n for (2).
For (3), m<=H and log mu(I)<=0. Rearrangement gives the sufficient
threshold (4) and the stated necessary threshold. No exchange of an
angular maximum with a spatial mean is used: H is the maximum of
that spatial mean itself.

The result bounds a further cost in the approved criterion, not its
remaining height H. In particular the degree may be O(n^2), but the
proved localization loss is O(d_ang/n^2)=O(1). Replacing this by an
uncontrolled generic degree loss would not give (2). L651 is a possible
downstream use only; neither its open response inequality nor RH is
assumed or proved here. No numerical calculation is a premise.

## Mathlib

The reused assessment inspected
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html).
Supporting univariate results include
`Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.mahlerMeasure_mul`. The analytic nonzero hypotheses are
retained here; totalized real logarithms do not justify ignoring them.
Full matching coverage for this weighted localization of a spatial
Mahler mean, or the explicit uniform constant, has not been checked.
No absence claim for Mathlib as a whole is made.
