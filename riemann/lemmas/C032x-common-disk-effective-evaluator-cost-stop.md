# Corollary C032x: literal common-disk effective-evaluator cost stop

## Hypotheses

Retain C032m/q/w's actual-divisor normalization, multiplicities,
zero-ordinate exclusion, strip/counting, finite-zero, heat and fixed-v1
qualifications. Use precisely C032w(4),(6)-(13), on the common disk M=2,
with T>=5, D=sqrt(T^2+1), R=T^2+1, r=T^2/R, H=P_D+d,
0<a<=1, A>=2D, integer N>=2, J>=1 and K>=1. Primitive coefficient
and final arithmetic errors are nonnegative additional allowances.
No individual finite-zero coordinates or actual kernel table is assumed.

For the separate box-model statement, take the dictionary of real and
imaginary components of C032q's kappa at real/purely imaginary arguments
{1/4,1/2,1,2,i/4,i/2,i,2i}, and its four positive Laplace functions at
{1/16,1/4,1,4}. Propagate the common symmetric E-error radius independently
for every odd column, without pruning by other known bounds or shared
primitive correlations. The four Laplace coefficients are nonnegative.
The finite centers preserve E/O's real-coefficient parity on these axes.
This independence describes a conservative enclosure method, not the
actual kernels or arbitrary evaluators.

## Conclusion

Let Delta_E=8*[T*(d+d_K)+tau_2(T)] be the analytic E-error allowance
in C032w(12). If Delta_E<1, necessarily

    T>2240, K>12,588,154,880,000, J>10^3345066.

If Delta_E<1/8, necessarily

    T>17920, K>51,561,082,388,480,000, J>10^214084266.

If Delta_E>=1, the raw independent interval model in the hypotheses
cannot certify a uniform dictionary residual strictly below1/2:
its worst-case residual at even one width is at least3/5.

These statements concern the displayed error allowances and literal
midpoint/polynomial implementation. They are not lower bounds on the
actual approximation errors, the actual dictionary residual, or the
complexity of different evaluators. In particular they refute neither
C032w's analytic effectivity nor a feasible measure or successful
certificate in C032q's actual cone. The result is a computational route
stop, not progress beyond the checked general sources or an RH argument.
The restricted claim passed independent audit1604 below; no source-wide
verification of the qualified external inputs is asserted.

## Proof

The unchanged ready assessment1570 covers this dictionary calculation
and its effective-error/coefficient obligations. C032w, audited in1575,
supplies the formulas used here. Its general explicit-formula input is
Alain Connes, *Heat Expansion and Zeta*, arXiv:2402.13082v1, Section2,
equations(4)-(7), printed p.4,
https://alainconnes.org/wp-content/uploads/heat-zeta.pdf . The compact
holomorphic integration input is Friedrich Haslinger, *Complex Analysis*,
Theorem2.39, pp.67-68,
https://www.mat.univie.ac.at/~has/scriptneu.pdf . Their previously checked
coverage in notes1572/1555 is reused; no general theorem is reproved or
newly browsed. Only elementary consequences of C032w's saved bounds
are calculated. The integer/rational certificate is
`scripts/smoothed-law/bounded_variation_effective_cost_1576.json`, produced
by `python3 scripts/smoothed-law/bounded_variation_effective_cost_1576.py`.

### Independent primitive-error boxes

The dictionary arguments are real or purely imaginary. Conjugate
symmetry makes E real on these axes; O is respectively real or purely
imaginary. Thus the retained real component of each odd kernel has the
form c_j=exp(-E_hat_j) times sinh(O_hat_j) or sin(theta_hat_j).
Suppose the implementation propagates the common symmetric E-error
interval [-Delta_E,Delta_E] independently for each odd column, as a
straight interval implementation of C032w permits. Fix the O intervals
at their centers. If Delta_E>=1, these boxes contain simultaneous scaling
of all c_j by either1/2 or2, since log2<1. Retain any allowed positive
values of the Laplace columns; their nonnegative coefficients give a
contribution p>=0. Writing x=sum a_j*c_j, any box residual upper bound
must therefore be at least

    max(|1+p+x/2|, |1+p+2*x|) >= (3/5)*(1+p) >=3/5.

Indeed 4*(1+p+x/2)-(1+p+2*x)=3*(1+p); the triangle
inequality bounds the left absolute value by five times that maximum.
This argument also covers zero odd columns. It is only an obstruction
for this deliberately independent interval model: its simultaneous
perturbations are not asserted to be actual kernels. Extra correlations,
one-sided information or tighter errors could remove it. In particular
this is not a lower bound for the actual dictionary.

Consequently Delta_E<1 is a useful necessary preflight condition for
this implementation, already weaker than a finished residual certificate.
The calculation below concerns exactly the analytic error bound in
C032w(12); arithmetic errors in(13) are nonnegative extra allowances.

### Necessary costs of the displayed error bound

Write d,d_K,tau as in C032w(6)-(12). With M=2 the common analytic
even-primitive error radius is

    Delta_E=8*[T*(d+d_K)+tau_2(T)], T>=5,
    tau_2(T)=4*[10*(2+log(1+T))+P_2]/(3*T).

Every omitted contribution to this error radius is nonnegative. From
C032w(4), exactly

    P_2=exp(25/16)+6*exp(2)+7/2+exp(81/16)>210.

The strict lower inequality is certified by summing the positive
exponential Taylor series through degree32 for each exponential and
comparing the resulting exact rational number with210. Thus

    Delta_E >=8*tau_2(T)>2240/T.                     (1)

In particular Delta_E<1 requires T>2240, independently of N,a,A,J,K
and the arithmetic precision. This is a lower bound on the displayed
*error allowance*, not on the actual approximation error.

Let R=T^2+1, r=T^2/R and H=P_D+d, D=sqrt(R). C032w(4),(10) give

    H>=4*exp(R/2),
    d_K=(H/R)*r^K*((K+1)-K*r)/(1-r)^2 >=H*R*r^K.

The latter inequality uses (K+1)-K*r>=1 and 1-r=1/R.
If Delta_E<1, its nonnegative term8*T*d_K is below1, hence

    K*log(1+1/T^2)>log(8*T*H*R)>R/2.

Since log(1+u)<u for u>0 (integrate 1/(1+u)<1), this implies

    K>T^2*R/2>T^4/2.                                (2)

For the midpoint term in C032w(7), B0=exp(A/2)/(2*a)>=1/(2*a)
and C0=1/2+coth(a)>=1/a. To check the latter elementary inequality,
a*cosh(a)-sinh(a) vanishes at0 and has derivative a*sinh(a)>=0;
divide by a*sinh(a)>0. The bracket in L includes the positive term
(exp(D*A)+1)*C0. With 0<a<=1 and A>=2*D,

    L>=exp(D*A)/(2*a^2)>=exp(2*T^2)/2.

Also A-a>=2*D-1>T for T>=5. Since pi<4, the quadrature allowance
therefore satisfies

    d_quad=L*(A-a)^2/(8*pi*J)
          >exp(2*T^2)*T^2/(64*J).

The term8*T*d_quad must be below1 if Delta_E<1. Necessarily

    J>exp(2*T^2)*T^3/8.                             (3)

Use T>2240 in(2)-(3). Since e>8/3 implies e^3>10 and T^3/8>1,
the exact consequences are

    K>12,588,154,880,000,
    J>10^3345066.                                   (4)

No integer with millions of digits is allocated to establish(4):
floor(2*2240^2/3)=3,345,066, and monotonicity plus e^3>10 give
the power inequality. For comparison, the stronger chosen primitive
tolerance Delta_E<1/8 requires T>17920, K>51,561,082,388,480,000,
and J>10^214084266. The script checks these integers rather than
treating decimal previews as evidence. Neither tolerance includes the
still-unpaid O-error, coefficient accuracy, final exponentials/sinh,
kernel coefficients or width-cell amplification. Paying these additional
errors cannot reduce(1)-(4).

This cost concerns literally enumerating the midpoint sum and Taylor
polynomial of C032w. Replacing them by an analytic evaluation, compressed
sum, sharper error analysis, argument-dependent disks or correlated
intervals is outside the implementation tested here. No complexity lower
bound for those alternatives is asserted. The box argument above is
likewise not a statement about correlations of the actual dictionary.

### Independent audit1604, 18 November 2026

Assessment1603 approves exactly this audit. C032w(4),(6)-(13) and its
audit1575 are inputs; C032m/q retain the stated divisor, multiplicity,
zero-ordinate, strip/counting, finite-zero, heat and fixed-v1
qualifications. This audit does not reverify those external inputs.
No invalid inequality was found in the restricted claim. In particular,
the two tolerances can be checked together without assuming T is an
integer. Put epsilon in {1,1/8} and suppose Delta_E<epsilon.

All four terms of d in C032w(6)-(7) are nonnegative: the cutoffs have
positive denominators, B0,C0,L are positive, and A>a. The numerator
of d_K is 1+K/R>0. Also tau_2(T)>0 and H=P_D+d>=P_D.
Substituting D=2 in P_D combines exp(2)+4*exp(2)+exp(2) into
6*exp(2), and the constants into 7/2. The independently evaluated
rational sum

    S=sum_(n=0)^32 (25/16)^n/n!
      +6*sum_(n=0)^32 2^n/n!+7/2
      +sum_(n=0)^32 (81/16)^n/n!

satisfies 210<S<211. Each exponential has strictly positive omitted
terms, so P_2>S>210. Hence Delta_E>=8*tau_2(T)>2240/T and
T>t0:=2240/epsilon. The upper bracket on S is not an upper bound
on P_2 and is not used as one.

Since r=T^2/R lies strictly between zero and one and 1-r=1/R,
d_K=H*R*r^K*(1+K/R)>=H*R*r^K. Thus

    r^K<epsilon/(8*T*H*R),
    K*log(1+1/T^2)>log(8*T*H*R/epsilon)>R/2.

The last inequality uses H>=4*exp(R/2), T>=5, R>=26 and
epsilon<=1, so its discarded logarithm log(32*T*R/epsilon) is
strictly positive. Integrating 1/(1+s)<1 for 0<s<=1/T^2 gives
log(1+1/T^2)<1/T^2. Consequently K>T^2*R/2>T^4/2>t0^4/2.

For the quadrature check, a*cosh(a)-sinh(a)>0 for a>0 follows
by integrating its derivative a*sinh(a)>0 from zero. Thus C0>1/a.
Retaining only B0*exp(D*A)*C0 in L, and using a<=1, gives
L>=exp(D*A)/(2*a^2)>=exp(2*T^2)/2. Moreover
A-a>=2*sqrt(T^2+1)-1>T because T>1. With pi<4 these yield
d_quad>exp(2*T^2)*T^2/(64*J). The retained error term
8*T*d_quad<epsilon therefore gives

    J>exp(2*T^2)*T^3/(8*epsilon)>exp(2*T^2).

Let n=floor(2*t0^2/3). Then 2*T^2>2*t0^2>=3*n and
exp(3)> (8/3)^3=512/27>10. Thus J>10^n strictly.
For t0=2240 and17920, respectively, exact arithmetic gives
(t0^4/2,n)=(12588154880000,3345066) and
(51561082388480000,214084266). For integer K the strict bounds
mean at least one more than each displayed integer. T need not be
integer; the saved certificate's integer-T entries are conditional
on choosing an integer spatial cutoff. Neither tolerance requires
constructing an integer of the size 10^n.

For the box statement, real coefficients and even/odd parity imply
E_hat is real on both axes, while O_hat is real on the real axis
and purely imaginary on the imaginary axis. Thus the nonzero real
dictionary component is exp(-E_hat)*sinh(O_hat), or
exp(-E_hat)*sin(theta_hat), respectively. The other component
vanishes. Since log(2)=integral_1^2 dt/t<1, both choices
E_hat+log(2) and E_hat-log(2) are inside every radius Delta_E>=1.
Holding O at its center scales each retained component by 1/2 or2,
including zero components. The assumed independent boxes allow
choosing either scale simultaneously for all odd columns at one
fixed width, while keeping the Laplace entries fixed and positive.
This last freedom would require separate justification in any
enclosure that shares primitive errors with its Laplace columns;
such a correlated enclosure is outside the stated model.

With real coefficients let x be the odd-column sum and let p>=0
be the nonnegative Laplace contribution. Write u=1+p,
A=u+x/2 and B=u+2*x. The coefficient identity 4*A-B=3*u
and the triangle inequality give max(|A|,|B|)>=3*u/5>=3/5.
At x=-4*u/5 both absolute values equal3*u/5, confirming the
direction of the minimax inequality. A box supremum contains these
two simultaneous choices, so one width already prevents a uniform
box certificate below1/2. No realization by the actual kernels is
inferred, and the box floor is not claimed when Delta_E<1.

Reproduce the independent rational comparison with
`python3 scripts/smoothed-law/common_disk_cost_audit_1604.py`.
Its full certificate is
`scripts/smoothed-law/common_disk_cost_audit_1604.json`.
All37 exact checks passed; their complete values and the empty failure
list were inspected. The checker independently uses powers/factorials
for S and compares both saved cost rows with1576, which is read-only.
The analytic reductions and box admissibility are established above,
not by the script. This verifies a local implementation-specific stop,
not a new general theorem or progress beyond the sources checked.

## Mathlib

Full matching coverage has not been checked and is unknown. The present
finite arithmetic and error-bound specialization needs no new Mathlib
input. Supporting exponential, finite-sum and real-log inequalities are
proved above or retained in C032w; no full matching formal theorem is
claimed. A script replay checks the integer/rational comparisons, not the
analytic reductions or the external hypotheses.
