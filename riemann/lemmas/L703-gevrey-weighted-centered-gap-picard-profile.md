# Lemma 703: a Gevrey-weighted exact centered-gap Picard profile

## Hypotheses

Use the selectable cutoffs and exact supported Picard construction of
L694, with a=1/8, b=3/8 and l=7/16. The Fourier coefficient convention
is f-hat(k)=integral_T f(t)exp(-2*pi*i*k*t)dt. The space Y consists
of the supported distributions with real bounded Fourier coefficients
used there; its norm is the coefficient supremum. A is the unweighted
Wiener algebra. The frequency center is the fixed center of L696:

    d=5/4, U=121/64, A_sp=27/10,
    omega_*=A_sp*integral_0^1 [1/(d+t)-t/(U+d*t)]dt,
    c_*=omega_*/(2*pi) in (a,b).

The initial real even cutoff Phi, compactly supported in (-l,l) and
equal to one on [-b,b], and the initial real even bump eta, supported
in [-1,1], with 0<=eta<=1 and eta=1 on [-1/2,1/2], may be selected
in Gevrey order 2. This is an existence result for such a selection,
not a regularity assertion for every previously chosen smooth cutoff.

Psi is any fixed smooth Hermitian cutoff from L694, compactly supported
in (-l,l) and equal to -1/(2*pi*i*t) on (-b,-a) union (a,b).
It need not be globally Gevrey. The prescription remains exactly

    chi_w(t)=eta((t-c_*)/w)+eta((t+c_*)/w),
    S_w(t)=-exp(pi*i*t)*chi_w(t),
    Q_w(t)=(Psi*S_w)(-t).

All selections are made before any finite-family size n. Spatial
atom masses are one and the added spatial anchor is 0.

## Conclusion

There are fixed r,w,c>0 and the same unique Y-ball Picard solution
T of L694 for these exact Q_w and Phi, with real coefficients
e_m=T-hat(m), such that

    r<=1/8,       sup_m |e_m|<=r,
    sum_m exp(c*sqrt(1+|m|))*|e_m|<infinity,
    r*sum_m |e_m|<=1/(16*pi^2).                              (1)

The positive translation-bounded measure

    mu=delta_0+sum_(m in Z) delta_(m+1/2+e_m)

has an angular Fourier gap
(omega_*-pi*w,omega_*+pi*w), with positive width fixed independently
of n, as in L696. The anchor and all masses are unchanged.

More precisely, for v_c(k)=exp(c*sqrt(|k|)) the same Picard iterates
T_0=Q_w, T_(j+1)=Q_w-R(c(T_j)) converge in A_c, the coefficient
l1_(v_c) space, and in Y to the same T. For some q_c<=1/4,

    ||T||A_c <= ||Q_w||A_c/(1-q_c),
    ||T-T_j||A_c <= q_c^(j+1)*||Q_w||A_c/(1-q_c).             (2)

No smallness or width-uniform bound for ||Q_w||A_c, or a positive
weight exponent uniform as w shrinks, is asserted. This is a
specialization of known Gevrey and Picard tools, not a claim of
certified originality. The separate conceptual audit in Section 6
accepts the stated result and parameter quantifiers. It supplies a
possible signed truncation input; it gives no
full-circle absolute-error payment, scalar logarithmic charge,
full-spatial bound, H/support, Xi realization or RH conclusion.

## Proof

### 1. Precise imported tools and the application difference

The approved comparison is
`drafts/literature/2026-11-03-centered-gap-gevrey-profile-scope.md`.
The following source results and relevant proofs were inspected there
and are reused, without reproving their general theorems.

* N. Lev, *An example concerning Fourier analytic criteria for
  translational tiling*, Rev. Mat. Iberoam. **38** (2022), 1975--1991,
  DOI [10.4171/RMI/1318](https://doi.org/10.4171/RMI/1318), Lemma 4.3,
  p.1984, (4.6); [arXiv:2007.09930v3](https://arxiv.org/html/2007.09930v3#S4.SS3),
  Lemmas 4.2--4.3 and (4.5)--(4.13), Sections 4.5--4.10. L694
  already supplies the supported operator, its unweighted estimates,
  same-limit construction and unit-mass prescription. Lev's
  parameter-integral identity is used below to retain the small factor.
* J.-C. Mourrat and H. Weber, *Global well-posedness of the dynamic
  Phi4 model in the plane*, Ann. Probab. **45** (2017), 2398--2476,
  DOI [10.1214/16-AOP1116](https://doi.org/10.1214/16-AOP1116),
  [published PDF](https://sites.math.northwestern.edu/~auffing/papers/MourratWeber.pdf),
  Section 2.1, Definition 1 and plateau construction, p.2405;
  Appendix Propositions 23--24, pp.2472--2473. Compact Gevrey
  cutoffs of order 2 with the stated supports and plateaux exist;
  products preserve this class, and common factorial-squared
  derivative bounds on a common compact support give Fourier decay
  C*exp(-delta*sqrt(|xi|)) with common positive constants.
* A. Dasgupta and M. Ruzhansky, *Gevrey functions and ultradistributions
  on compact Lie groups and homogeneous spaces*, Bull. Sci. math.
  **138** (2014), 756--782,
  [published PDF](https://backoffice.biblio.ugent.be/download/8585191/8585192),
  Definition 2.1 and Theorem 2.3(R), pp.761--762, forward proof
  pp.771--773 through (3.21). On R/Z, order 2 gives the same
  stretched-exponential coefficient bound, including k=0. The
  character frequencies are 2*pi*k; constants absorb this convention.
  Uniformity follows from common derivative constants in that proof,
  not merely from individual membership in the class.
* K. Groechenig, *Weight Functions in Time-Frequency Analysis*, Fields
  Institute Communications **52** (2007), 343--366,
  [arXiv:math/0611174v1](https://arxiv.org/pdf/math/0611174v1), Lemmas
  2.1(a), 4.1 and the latter's discrete proof, PDF pp.3--5.
  The weight v_c is submultiplicative, and l1_(v_c)(Z) is a Banach
  convolution algebra with norm bound ||a*b||<=||a||*||b||.

Complex-valued functions are covered by applying the real-valued
Fourier-decay statements to both components and summing their bounds.
The application difference is a uniform bound for the exact nonlinear
family, weighted convergence of the original iterates, and compatible
choices of r,w,c. No source is asserted to state this exact conclusion.

### 2. A common Gevrey bound for the exact nonlinear family

Choose Phi and eta as in the hypotheses once and for all. For constants
P,A_Phi>0 the selected Phi satisfies, for every integer p>=0,

    sup_t |Phi^(p)(t)| <= P*A_Phi^p*(p!)^2.

For real |s|<=1 define the entire factor

    h_s(z)=2*pi*i*z*integral_0^1 exp(2*pi*i*theta*s*z)dtheta.

For s!=0 it equals (exp(2*pi*i*s*z)-1)/s; for s=0 it is
2*pi*i*z. For real |t|<=l and |z-t|<=1,

    |h_s(z)| <= H := 2*pi*(l+1)*exp(2*pi).

Indeed |z|<=l+1 and the exponential modulus is at most exp(2*pi)
uniformly in theta and s. Cauchy's derivative estimate on that disk
gives |h_s^(j)(t)|<=H*j! for every j>=0. Set g_s(t)=Phi(t)*h_s(t),
extended periodically; it is smooth across the periodic boundary
since Phi vanishes on a neighborhood of that boundary. Leibniz gives

    sup_t |g_s^(p)(t)|
      <= P*H*sum_(j=0)^p binom(p,j)*A_Phi^(p-j)
                                      *((p-j)!)^2*j!
      <= P*H*(A_Phi+1)^p*(p!)^2.                            (3)

The last inequality uses ((p-j)!)^2*j!<=(p!)^2 term by term.
Outside Phi's support every product derivative is zero. Thus (3)
is global, with common support and constants independent of s.
By the imported Fourier-decay theorem and its uniform derivative
bounds, there are D,delta>0, depending only on this initial kernel,
such that

    |g_s-hat(k)| <= D*exp(-delta*sqrt(|k|)),
                    k in Z, real |s|<=1.                    (4)

Here D may be enlarged to include k=0. Neither constant depends on
r, the prescribed width w, the data Q_w or the solution.

Retain exactly L694's summands

    E_m(u;t)=exp(2*pi*i*m*t)*Phi(t)
             *(exp(2*pi*i*u*t)-1-2*pi*i*u*t)/(2*pi*i*t).

The removable values at t=0 are understood. Differentiating in the
real parameter gives exp(2*pi*i*m*t)*Phi(t)*(exp(2*pi*i*s*t)-1).
Consequently, including t=0 by continuity,

    E_m(v;t)-E_m(u;t)
       =exp(2*pi*i*m*t)*integral_u^v s*g_s(t)ds.

Integration and Fourier coefficient extraction commute on this finite
parameter interval by continuity and the common compact support.
For real |u|,|v|<=r<=1, (4) therefore proves the required estimate

    |[E_m(v)-E_m(u)]-hat(k)|
       <= D*r*|v-u|*exp(-delta*sqrt(|k-m|)).                  (5)

This retains both the small radius and the exact modulation index.
It is a bound on the nonlinear difference, not just on the data.

### 3. Weighted summation, with constants fixed before the data

For 0<=c<=delta/2 put

    kappa(c)=D*sum_(j in Z) exp(-(delta-c)*sqrt(|j|)),
    kappa_*=D*sum_(j in Z) exp(-(delta/2)*sqrt(|j|)).

These sums are finite and kappa(c)<=kappa_*. Finiteness follows, for
example, by grouping indices between consecutive integer squares,
which bounds the sum by a constant times sum_(p>=0)(p+1)*exp(-delta*p/2).

Let alpha,beta be real sequences in l1_(v_c) with supremum norms at
most r. Since v_c(k)<=v_c(m)*v_c(k-m), Tonelli applied to (5) gives

    sum_m ||E_m(beta_m)-E_m(alpha_m)||A_c
       <= r*kappa(c)*||beta-alpha||_(1,v_c).                 (6)

Thus the difference series converges absolutely in A_c. Its sum agrees
with Lev's R(beta)-R(alpha): finite partial sums are identical, A_c
convergence implies A and distributional convergence, and L694's
source-defined distributional sum has a unique limit. Taking alpha=0
also proves R(beta) belongs to A_c. With q_c=r*kappa(c),

    ||R(beta)-R(alpha)||A_c <= q_c*||beta-alpha||_(1,v_c).     (7)

This is precisely the application of weighted convolution to the
coefficient majorant. A small weighted norm of alpha or beta is not
required; their coefficient supremum is what pays the factor r.

### 4. Compatible radius, data width and positive exponent

Fix Psi and M_Psi=max(1,||Psi||infinity). Let C_0 be a valid L694
coefficient constant for the selected Phi, and let
K=sum_(j in Z)(1+j^2)^(-1). L702 Section 2 supplies a number B>0,
depending only on eta and the analytic multiplier on the fixed annuli,
such that ||Q_w||A<=B for every permitted positive w. In particular B
is independent of the later enlargement of C_0, r and w. For precision,
on the annuli put phi(t)=-exp(-pi*i*t)/(2*pi*i*t), let B_j bound
|phi^(j)| there for j=0,1,2, and use L702's explicit choice

    A_0=2*B_0*||eta||L1,
    A_2=2*(B_2*||eta||L1+2*B_1*||eta'||L1+B_0*||eta''||L1),
    B=5*A_0+A_2/(2*pi^2).

Choose a fixed valid coefficient constant and radius by

    C>=max(C_0,kappa_*/K,16*pi^2*B/(3*K)),
    r=min(1/8,1/(4*C*K)).                                   (8)

Then q=C*K*r<=1/4, r*kappa_*<=1/4 and
r<=3/(64*pi^2*B). This keeps L694/L702's form of the radius exactly;
only its permissible coefficient constant has been enlarged.
Now choose the exact L696/L702 width

    w=min((c_*-a)/2,(b-c_*)/2,r/(8*M_Psi))>0.                (9)

Both bump supports lie strictly inside the two annuli. Reflection and
Psi's prescribed values give, on those supports and with zero extension,

    Q_w(t)=phi(t)*chi_w(t).                                 (10)

In particular ||Q_w||Y<=4*M_Psi*w<=r/2 and Q_w is Hermitian.
No assertion about Psi away from these supports is used.

For completeness, the exact data in (10) have Gevrey order 2 for this
fixed w. Choose P_eta,A_eta>0 with
||eta^(p)||infinity<=P_eta*A_eta^p*(p!)^2. The fixed phi is analytic
on complex disks of radius rho=a/2 around both real annuli, since
|z|>=a/2 on those disks. For a finite common H_phi, Cauchy's estimate
gives |phi^(j)(t)|<=H_phi*rho^(-j)*j! there. On either bump support,
Leibniz and scaling then give the global bound

    ||Q_w^(p)||infinity
       <=2*H_phi*P_eta*(rho^(-1)+A_eta/w)^p*(p!)^2.          (11)

Outside the supports Q_w vanishes. All bump derivatives vanish at
their support boundaries; hence extension by zero and the periodic
extension preserve (11). The pole of phi at zero is never included.
The imported Fourier theorem supplies finite D_Q and delta_Q>0 with

    |Q_w-hat(k)|<=D_Q*exp(-delta_Q*sqrt(|k|)).                (12)

These constants may depend on w. Finally set

    c=min(delta/2,delta_Q/2)>0.                             (13)

Then Q_w belongs to A_c by (12), and (7) still has q_c<=1/4
because (8) already paid kappa_* for every c in this whole range.
Thus reducing c after w has been fixed cannot invalidate the earlier
contraction radius. There is no requirement that ||Q_w||A_c be small
or that c remain positive uniformly over a family of shrinking widths.

### 5. The same Picard limit, smallness and exact gap

Write d_Q=||Q_w||Y. L694's ball and map are

    B_Y={T in Y: ||T-Q_w||Y<=d_Q},
    H(T)=Q_w-R(c(T)),       T_0=Q_w,       T_(j+1)=H(T_j).

The symbol c(T) here denotes the entire coefficient sequence, not
the positive weight parameter. For T in B_Y, ||T||Y<=2*d_Q<=r.
L694's coefficient-sup estimate, with the valid enlarged C, gives

    ||H(T)-Q_w||Y<=q*||T||Y<=2*q*d_Q<=d_Q,
    ||H(T)-H(V)||Y<=q*||T-V||Y,        T,V in B_Y.

These are the original supported real-coefficient iterates and their
unique Y-ball fixed point. Since T_0 is in A_c, (7) shows inductively
that every iterate belongs to A_c, without changing its Y-ball bound.
In this norm it also gives

    ||T_j||A_c<=(1+q_c+...+q_c^j)*||Q_w||A_c,
    ||T_(j+1)-T_j||A_c<=q_c^(j+1)*||Q_w||A_c.

For the first difference apply (7) to c(T_0) and zero; thereafter
apply it to two consecutive iterates, whose coefficient suprema
remain at most r. Completeness of l1_(v_c) and the geometric sum give
(2). Its limit is supported in [-l,l], because A_c convergence
implies uniform convergence and all iterates vanish outside that
interval. Coefficient convergence preserves reality. Hence this limit
belongs to Y, and ||V||Y<=||V||A_c identifies it with the original
Y limit in the closed ball. Equation (7) also passes the nonlinear
term to that limit. No different fixed point is substituted.

Call its coefficients e_m. The comparison

    exp(c*sqrt(|m|)) <= exp(c*sqrt(1+|m|))
                         <= exp(c)*exp(c*sqrt(|m|))

turns finite A_c norm into the weighted assertion in (1). Applying
L694's unweighted same-iteration estimate and L702's uniform B gives

    E=sum_m |e_m|<=||Q_w||A/(1-q)<=4*B/3,
    r*E<= [3/(64*pi^2*B)]*(4*B/3)=1/(16*pi^2).              (14)

The coefficient cap follows from membership in B_Y. L694's reflected
prescription argument and L696 Section 2 now apply to these exact
Q_w, Phi, Psi and e, giving

    F_(2pi)mu=1+delta_0-chi_w        on (-b,b).

On (c_*-w/2,c_*+w/2), chi_w is one and the frequency atom at zero
is absent. In the angular convention this is the asserted gap of
radius pi*w. The unit counting masses and the spatial anchor come
from the same distributional differentiation/translation argument
already proved in L694. The real cap r<=1/8 retains separation and
translation-boundedness. All constants, cutoffs, width and the single
profile were fixed without any n-dependent choice.

The L695 absolute-cost and L702 endpoint-only obstructions are not
premises of this proof and are not removed by it. The argument supplies
neither a comparison between stretched-exponential decay and the
finite family's exponential amplification nor signed logarithmic
control. Those are independent unresolved steps toward the main gap.

### 6. Separate conceptual audit — 3 November 2026, step 144

This audit uses the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-03-centered-gap-gevrey-picard-audit-scope.md`
and reuses its step-141 primary-source comparison. The imported
theorems and precise citations are in Section 1; no new general
regularity theorem or source-manuscript audit is asserted. L694's
operator and supported-ball proof, L696 Section 2 and L702 Section 2
and its parameter audit were checked against their uses here.

**Uniform kernel constants.** On the radius-one complex disk around
real t in [-l,l], |Im z|<=1 and |z|<=l+1. Real |s|<=1 therefore
gives |exp(2*pi*i*theta*s*z)|<=exp(2*pi), including s=0.
The integral defining h_s is entire, so Cauchy's estimate applies
with the same H at every such t and s. In Leibniz's formula the
factorial product ((p-j)!)^2*j! is at most (p!)^2; summing the
remaining binomial terms gives exactly (3). All derivatives vanish
off the fixed support of Phi. Thus the imported forward Fourier
estimate has common support, derivative constant PH and derivative
base A_Phi+1. Its proof's constants, including a bound on the zero
mode, can be chosen uniformly in s. Applying it to real and
imaginary parts does not change this uniformity. Individual Gevrey
membership alone would not suffice; (3) supplies the needed input.

The real parameter derivative of E_m is precisely the one displayed
before (5): division by 2*pi*i*t cancels the exponential derivative,
and the subtracted linear term contributes -1. At t=0 both sides
have their continuous zero value. For either order of u and v,
the parameter segment lies in [-r,r] and integral_u^v |s| |ds|
is at most r*|v-u|. Fourier extraction commutes with this integral
on the common compact support; modulation gives k-m. Consequently
(5) retains the radius factor even when the segment crosses zero.

**Absolute weighted summation and the source operator.** For each
m, the sum over k of the right side of (5), multiplied by v_c(k),
is at most r*kappa(c)*v_c(m)*|beta_m-alpha_m|. Summing these
nonnegative majorants proves (6) by Tonelli. The same finite partial
sums define Lev's distributional series. Since A_c convergence
implies uniform and distributional convergence, uniqueness of a
distributional limit identifies the sums. This justifies (7) for
weighted-summable inputs with small coefficient supremum; it does
not assert weighted regularity for arbitrary bounded sequences.
The bound kappa(c)<=kappa_* holds on the entire closed interval
0<=c<=delta/2, before Q_w is selected.

**Actual reflected data and selection order.** Evenness of chi_w
and Psi's prescribed values give
Q_w(t)=Psi(-t)*[-exp(-pi*i*t)*chi_w(-t)]=phi(t)*chi_w(t)
on both support bands, with the sign in (10). Reflection and
Hermitian symmetry preserve real Fourier coefficients. No estimate
on derivatives of Psi outside these bands is used. The pole of phi
is excluded: for |z-t|<=rho=a/2 and a<=|t|<=b one has |z|>=a/2.
For example H_phi=exp(pi*rho)/(pi*a) bounds |phi(z)| there.
Cauchy's estimate and the scaled factorial-squared bounds for eta
therefore give (11). The bump derivatives vanish at their support
boundaries; zero extension through the complementary intervals,
including a neighborhood of zero and the periodic boundary, is
smooth and satisfies the same bound. This verifies (12) for the
actual Q_w, without assuming globally Gevrey Psi.

L702's A_0,A_2 and B use only the initially fixed eta and phi on
fixed annuli. In particular they do not contain the later width,
radius, weight or enlarged coefficient constant. After those initial
choices, (8) gives simultaneously

    C*K*r<=1/4,   r*kappa_*<=kappa_*/(4*C*K)<=1/4,
    r<=1/(4*C*K)<=3/(64*pi^2*B).

The two positive distances of c_* from a,b, already checked in
L696, and r/(8*M_Psi)>0 make (9) a positive fixed width. Its
supports lie strictly inside the prescribed bands and
||Q_w||Y<=4*M_Psi*w<=r/2. Now, and only now, the fixed data
give delta_Q>0 and permit (13). Decreasing c to this value cannot
increase kappa(c) beyond the already paid kappa_*. Neither a small
||Q_w||A_c nor a positive exponent uniform as w tends to zero is
needed. There is no limiting sequence of profiles in this argument.

**Invariant iterates and identity of the limits.** The coefficient-sup
estimate is applied on the original closed supported ball B_Y.
Every iterate stays there because 2*q*d_Q<=d_Q, and therefore
every coefficient sequence entering (7) has supremum at most r.
Starting with Q_w in A_c, the first difference has norm at most
q_c*||Q_w||A_c; induction gives q_c^(j+1)*||Q_w||A_c for
T_(j+1)-T_j. Summing from j onward gives exactly the error in
(2), including j=0. No invariant ball in the weighted norm is
assumed. Completeness gives its limit, uniform convergence preserves
support, and coefficient convergence preserves reality. Hence this
limit lies in Y, and the continuous inequality ||V||Y<=||V||A_c
identifies it with the unique Y-ball fixed point. Equation (7)
also passes the nonlinear term to this same limit.

Finally v_c(m)<=exp(c*sqrt(1+|m|))<=exp(c)*v_c(m), so the
requested weighted summability follows without changing the exponent.
The unweighted bound E<=4*B/3 concerns these same iterates and limit;
the preceding radius inequality gives r*E<=1/(16*pi^2), exactly
L702's threshold. Applying L694's reflection/differentiation and
L696's center placement to these same coefficients gives
F_(2pi)mu=1+delta_0-chi_w. On the positive plateau chi_w=1
and the frequency atom at zero is absent, so the angular gap has
radius pi*w. The real cap prevents collisions with the anchor or
between neighboring atoms; every counting mass remains one.

All scoped assertions pass with their stated quantifiers. No
substantive error, additional premise, stronger theorem or numerical
certificate is needed. This first audit validates the local weighted
specialization, not novelty beyond the cited tools. L695's absolute
cost obstruction and L702's signed-interior obstruction are comparison
results, not inputs to this proof, and retain their scopes. The
weighted norm alone pays no finite-family exponential amplification,
complete logarithmic mean, H/support or Xi realization.

## Mathlib

Full matching coverage of this exact weighted prescription theorem has
not been checked. Coverage of the imported Gevrey characterization and
the specific supported-distribution operator is also not checked.
Banach fixed points, Cauchy estimates and absolute Fourier summation
are supporting mathematics, not a claimed full matching theorem.
Unknown Mathlib availability is not evidence of absence.
