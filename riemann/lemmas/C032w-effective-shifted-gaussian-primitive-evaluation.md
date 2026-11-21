# Corollary C032w: effective shifted Gaussian primitive evaluation

## Hypotheses

Retain C032m's actual divisor, multiplicity and normalization:
z_rho=(rho-1/2)/i=gamma_rho-i*delta_rho for positive-ordinate zeros,
|delta_rho|<1/2, the zero-ordinate exclusion and the stated counting
input. In particular, for real 1<=sigma<=2,

    G_sigma(z)=exp(-z^2/(4*sigma))/sqrt(4*pi*sigma),
    p_sigma(z)=(1/2)*sum_(rho in Z+)
                       [G_sigma(z-z_rho)+G_sigma(z+z_rho)],
    R_sigma(w)=integral_0^infinity
                (p_sigma(x)-p_sigma(i*w))/(x^2+w^2) dx,
    E_sigma(w)=4*integral_0^w t*R_sigma(t) dt,
    O_sigma(w)=2*pi*integral_0^w p_sigma(i*t) dt.

Every quotient has C032m's continuous removable value. Its inherited
fixed-v1 preprint, finite-zero and heat qualifications remain in force
when using the probability-law/cone interpretation of C032q. The
evaluation below does not use heat positivity, finite individual zero
coordinates, a density, moments, RH or a global sign of p_sigma. It
does not independently verify those other inputs.

Use the unconditional explicit formula of Alain Connes, *Heat Expansion
and Zeta*, arXiv:2402.13082v1 (20 February 2024), Section 2, equations
(4)-(7), printed p.4, [author PDF](https://alainconnes.org/wp-content/uploads/heat-zeta.pdf).
Only its identity over complex nontrivial zeros is imported; the
RH-dependent spectral interpretation and asymptotic theorem are not.
The existing coverage is source-notes1572/1555. The page containing the
Mellin hypotheses and these identities was checked again for constants.

## Conclusion

There is an evaluation of E_sigma and O_sigma, using only elementary
functions, constants and finitely many prime powers, with fully explicit
absolute errors uniform in sigma in [1,2] and |w|<=M. In particular M=3
covers all dictionary1570 arguments, their straight primitive paths and
a neighborhood of the closed disk |w|<=2. Widths remain real; no
complex-width differentiation is asserted or needed.

The formulas and errors (1)-(13) below give an ordered finite procedure
whose errors tend to zero. This is an analytic effectivity result, not
an implemented evaluator, a useful computational complexity bound or a
certificate for the residual below 1/2. Cancellation costs can be very
large. All-degree positivity, full odd cancellation, positive output,
arbitrary variation and unsmoothed Xi realization remain open. This
specialization is recorded on 18 November 2026. Critical audit1575 below
checks the analytic interface under its stated inputs; it does not check
implementation or computational feasibility. No complete RH candidate
is claimed.

## Proof

### 1. Imported identity and exact normalization

Write

    B(t)=exp(t/2)/(exp(t)-exp(-t)), t>0,
    c=log(4*pi)+gamma_E,
    A_sigma(z)=exp(-z^2/(4*sigma)+1/(16*sigma))
                       *cos(z/(4*sigma))/sqrt(4*pi*sigma).

The shifted profile formula is

    p_sigma(z)=A_sigma(z)-c/(4*pi)
      -(1/(2*pi))*integral_0^infinity
           [exp(-sigma*t^2)*cos(z*t)-exp(-t/2)]*B(t) dt
      -(1/(2*pi))*sum_(n>=2) Lambda(n)/sqrt(n)
                    *exp(-sigma*(log n)^2)*cos(z*log n).       (1)

Lambda(p^a)=log p for every prime power, and is zero otherwise.
The subtraction in the integral is part of the integrand. No two
separate integrals with divergent lower endpoints are introduced.

For the source's Mellin test take

    F(v)=exp(-sigma*(log v)^2)*cos(z*log v)/(2*pi),
    f(v)=v^(-1/2)*F(v), v>0.

It satisfies f^sharp=f. On every bounded z set, it and the needed
derivatives decay faster than any prescribed power at zero and
infinity after the displayed v^(-1/2) factor: in y=log v the bound
is a polynomial times exp(-y^2+C*|y|). Thus the smoothness and the
O(v^delta), O(v^(-1-delta)) hypotheses hold for any fixed delta>0.
The Gaussian integral, or the source's Gaussian transform with the
two linear shifts, gives

    tilde f(s)=(1/2)*[G_sigma(z-(s-1/2)/i)
                         +G_sigma(z+(s-1/2)/i)].

The transform identity for complex s,z follows by Gaussian domination
on their compact sets. The corresponding even test in the zero
variable r is entire and has Gaussian decay on every fixed horizontal
strip, uniformly for bounded z and 1<=sigma<=2. This also checks the
strip hypotheses of Chirre-Goncalves, *Bounding the log-derivative of
the zeta-function*, Math. Z.300 (2022), 1041-1053, Proposition 5,
p.1044, [publisher PDF](https://link.springer.com/content/pdf/10.1007/s00209-021-02820-9.pdf).
No real-valued-test restriction is needed for the Mellin identity.

Pair rho with 1-rho, preserving multiplicity and using the exclusion
of ordinate zero. The all-zero sum is 2*p_sigma(z). Positive-ordinate
off-line conjugates are still separate terms; there is no additional
division for them. Both pole integrals equal A_sigma(z). At v=1,
f(1)=1/(2*pi). In the source's equation (7), v=exp(t) gives the
archimedean term c/(2*pi) plus (1/pi) times the integral in (1).
Equation (6) gives (1/pi) times the displayed prime-power sum.
Dividing the all-zero identity by two proves (1). Trivial zeros are
already accounted for by the archimedean term and are not added again.
This imports the general explicit formula; it is not a reproof of it.

### 2. Uniform domination, disk bounds and a real-axis growth bound

The elementary estimates

    B(t)<=1/t                 (0<t<=1),
    B(t)<=2*exp(-t/2)          (t>=1)                         (2)

follow from exp(t)-exp(-t)>=2t, exp(1/2)<2 and
1-exp(-2)>1/2. For |z|<=D and 0<t<=1,

    |exp(-sigma*t^2)*cos(z*t)-exp(-t/2)|
       <=(2+D^2/2)*exp(D)*t^2+t/2.                         (3)

Indeed |1-exp(-sigma*t^2)|<=2t^2, |cos(z*t)|<=exp(D*t),
and the integral form of the second Taylor remainder gives
|cos(z*t)-1|<=D^2*t^2*exp(D*t)/2. At t>=1 the integrand in
(1) has modulus at most

    2*exp(-t^2+(D-1/2)*t)+2*exp(-t).

Its integral is at most 4*exp(D^2/2)+2: use
D*t<=t^2/2+D^2/2 and integral_0^infinity exp(-t^2/2)dt<2.
For l=log n, Lambda(n)<=log n<=n gives

    Lambda(n)*n^(-1/2)*exp(-sigma*l^2)*|cos(z*l)|
       <=n^(-2)*exp(-l^2+(D+5/2)*l).

The sum is at most exp((D+5/2)^2/4), since
sum_(n>=2) n^(-2)<1. These bounds prove locally uniform absolute
convergence. They also apply on a larger z disk whenever derivatives
or Cauchy integrals are used. C032m supplies the corresponding uniform
zero-series convergence. Haslinger, *Complex Analysis*, Theorem 2.39,
pp.67-68, [primary text](https://www.mat.univie.ac.at/~has/scriptneu.pdf),
therefore applies with the displayed integrable compact dominators.
No unbounded spatial integral is exchanged with prime or archimedean
terms at this stage.

For later completely numerical constants define, for D>=0,

    P_D=exp((D+1/2)^2/4)+1
         +(1+D^2/4)*exp(D)+1/2
         +4*exp(D^2/2)+2+exp((D+5/2)^2/4).

Then

    sup_(sigma in[1,2], |z|<=D) |p_sigma(z)| <= P_D.        (4)

The pole term is bounded by the first exponential; |c|/(4*pi)<1.
The other terms follow from (2)-(3), dropping the factor 1/(2*pi)<1.
Here 0<gamma_E<1, 3<pi<4 and 8/3<e<3 suffice for these coarse
constant inequalities.

For real x>=0 a much better growth bound than P_x is available:

    |p_sigma(x)| <= 10*(1+log(1+x)).                        (5)

To prove it, split the archimedean integrand as

    [exp(-sigma*t^2)-exp(-t/2)]*B(t)
       +exp(-sigma*t^2)*(cos(x*t)-1)*B(t).

Each of these two combined terms is integrable at zero. The absolute
integral of the first is at most 3/2+10/3<5, by (2), the bound
2t^2+t/2 on (0,1), and t^2>=t on [1,infinity). For the second,
put a=1/(1+x). On (0,a), integration of x^2*t/2 gives at most 1/4;
on (a,1), integration of 2/t gives 2*log(1+x). On [1,infinity)
its integral is at most 4*integral_1^infinity exp(-3t/2)dt<8/3.
Thus the whole absolute integral is below 8+2*log(1+x).
The pole term has modulus <1. The prime sum is at most
exp(25/16)<9 before its 1/(2*pi) factor. Together with the constant
term <1 and 2*pi>6, these estimates imply (5). No sign or local
zero-density bound was used.

### 3. A finite entire profile approximation with explicit error

Fix D>=0, integer N>=2, 0<a<=1, A>=max(1,2*D), and integer J>=1.
Replace the prime sum in (1) by 2<=n<=N, omit the archimedean
intervals (0,a) and (A,infinity), and use the composite midpoint sum
with J equal cells on [a,A]. Call the resulting exact entire even
function p_tilde_sigma(z). Elementary constants and the pole term
are still exact in this definition. It has no individual zero input.

Put b=D+5/2 and let y_+=max(y,0). Explicit bounds for the three
truncations, already including the factor 1/(2*pi), are

    d_prime=exp(b^2/4-(log(N)-b/2)_+^2)/(2*pi*N),
    d_small=[(1+D^2/4)*exp(D)*a^2+a/2]/(2*pi),
    d_large=[exp(-A^2/2)/A+exp(-A)]/pi.                    (6)

For the first, maximize exp(-l^2+b*l) over l>=log N and use
sum_(n>N)n^(-2)<=1/N. The second integrates (3) with B(t)<=1/t.
For the third, t>=A>=2D gives -t^2+D*t<=-t^2/2 and
integral_A^infinity exp(-t^2/2)dt<=exp(-A^2/2)/A.

Here is an explicit finite-quadrature error, including the lower
endpoint's effect. Set

    B0=exp(A/2)/(2*a),
    C0=1/2+coth(a),
    L=B0*[(4*A+D)*exp(D*A)+1/2
                         +(exp(D*A)+1)*C0],
    d_quad=L*(A-a)^2/(8*pi*J),
    d=d_prime+d_small+d_large+d_quad.                      (7)

For the archimedean integrand I(t), |I'(t)|<=L on [a,A]. Indeed
|F'(t)|<=(4A+D)exp(DA) for F=exp(-sigma*t^2)cos(z*t),
|F-exp(-t/2)|<=exp(DA)+1, B<=B0, and
|B'/B|=|1/2-coth t|<=C0. The midpoint error is at most
L*(A-a)^2/(4J) before division by 2*pi: integrate the distance
to the midpoint on each cell. Consequently

    sup_(sigma in[1,2], |z|<=D) |p_sigma(z)-p_tilde_sigma(z)|<=d.

For fixed D this error can be made arbitrarily small: choose N,A,
then a, then J. The displayed bounds, including their possible large
sizes, determine the choices. No differentiated asymptotic remainder
or unsupported cancellation estimate occurs.

### 4. The noncompact spatial tail and exact removable quotient

Fix M>=0 and T>=max(1,2*M+1). From (4)-(5) and
|x^2+w^2|>=3*x^2/4 for x>=T, |w|<=M, obtain

    sup_(sigma,|w|<=M) integral_T^infinity
          |(p_sigma(x)-p_sigma(i*w))/(x^2+w^2)| dx
       <=tau_M(T)
       :=4*[10*(2+log(1+T))+P_M]/(3*T).                    (8)

This uses the exact integral
integral_T^infinity log(1+x)/x^2 dx
=log(1+T)/T+log(1+1/T), with log(1+1/T)<=1/T.
In particular tau_M(T) tends to zero with an explicit rate.
This is a tail of the original combined quotient, not a termwise
spatial integration of (1).

Write p_sigma(z)=h_sigma(z^2), and likewise p_tilde=h_tilde(z^2).
Evenness makes these entire functions without choosing a square-root
branch. C032m's identity is

    q_sigma(x,w)=integral_0^1
        h_sigma'((1-v)*(-w^2)+v*x^2) dv.                   (9)

It gives the original quotient when x^2+w^2!=0; otherwise it gives
h_sigma'(x^2)=p_sigma'(x)/(2x) for x>0, and h_sigma'(0)=p_sigma''(0)/2
at the origin. These are also the values at both w=ix and w=-ix.
No principal value, detour or division by an unverified nonzero
quantity is introduced.

For the compact calculation now set

    U=T^2, R=U+1, D=sqrt(R), r=U/R, H=P_D+d.

Use (6)-(7) for this D. On |u|<=R, |h-h_tilde|<=d and
|h_tilde|<=H, by taking any square root solely to estimate the value.
Cauchy's radius-one derivative formula gives |h'-h_tilde'|<=d
on |u|<=U. This pays the divided-difference error even at its removable
points; a value error divided by x^2+w^2 would not do so.

### 5. Finite polynomial primitives and complete error propagation

Let h_tilde(u)=sum_(k>=0)c_k*u^k and
h_K(u)=sum_(k=0)^K c_k*u^k, K>=1. Cauchy's coefficient bound is
|c_k|<=H/R^k, uniformly in sigma. Thus, on |u|<=U,

    |h_tilde-h_K|<=eta_K:=H*r^(K+1)/(1-r),
    |h_tilde'-h_K'|<=d_K
       :=(H/R)*r^K*((K+1)-K*r)/(1-r)^2.                    (10)

These are the geometric series and its derivative, not qualitative
Taylor convergence. Both tend to zero as K tends to infinity for
fixed T and profile cutoffs. The coefficients are computable from the
finite pole/exponential/cosine expression p_tilde: c_k is its coefficient
of z^(2k). Finite convolution of the usual exponential/cosine series
computes each such coefficient exactly as an elementary expression.

The polynomial divided difference is

    q_K(x,t)=sum_(k=1)^K c_k*sum_(j=0)^(k-1)
                              x^(2k-2-2j)*(-t^2)^j.

All its apparent quotient singularities have already been removed.
Integrate this finite polynomial over 0<=x<=T and then along 0 to w:

    E_hat(w)=4*sum_(k=1)^K c_k*sum_(j=0)^(k-1)
       (-1)^j*T^(2k-1-2j)*w^(2j+2)
                         /[(2k-1-2j)*(2j+2)],
    O_hat(w)=2*pi*sum_(k=0)^K c_k*(-1)^k*w^(2k+1)/(2k+1). (11)

Finite polynomial integration needs no sum/integral interchange at
infinity. Equations (8)-(10), and the straight-path formulas from
C032m, give the complete analytic error bounds

    |E_sigma(w)-E_hat(w)|
        <=2*M^2*[T*(d+d_K)+tau_M(T)],
    |O_sigma(w)-O_hat(w)|<=2*pi*M*(d+eta_K), |w|<=M.       (12)

For example, the factor 2*M^2 is 4*M^2*integral_0^1 v dv.
On the compact x interval, (9) bounds the quotient error by d+d_K,
and integration costs T. The O estimate uses |-(v*w)^2|<=M^2<=U.
Both primitives retain value zero at w=0, E is even and O is odd.

There is an explicit ordered convergence procedure for (12). First
choose T to reduce 2*M^2*tau_M(T) below a prescribed error allowance.
Then fix this T,D and choose the profile cutoffs to make both
2*M^2*T*d and 2*pi*M*d small. Finally choose K using (10).
No simultaneous limit with uncontrolled changing constants is asserted.
If M=0 the values are exactly zero; otherwise this procedure applies.

Finite arithmetic can also be paid explicitly. If each c_k is evaluated
with absolute error <=epsilon_k, its propagated contribution is at most

    e_E=4*sum_(k=1)^K epsilon_k*sum_(j=0)^(k-1)
        T^(2k-1-2j)*M^(2j+2)/[(2k-1-2j)*(2j+2)],
    e_O=2*pi*sum_(k=0)^K epsilon_k*M^(2k+1)/(2k+1).        (13)

Add these and the absolute errors in final arithmetic to (12). The
pole factor, logarithms, cosines and exponentials can be enclosed by
their convergent elementary series with remainder estimates. For
example the absolute exponential remainder after degree m is at most
exp(|z|)*|z|^(m+1)/(m+1)!. Euler's constant can be enclosed using
0<H_n-log n-gamma_E<1/n; the latter follows by telescoping the positive
differences log(1+1/k)-1/(k+1) and bounding each by 1/[k(k+1)].
Standard convergent enclosures of pi complete the constant evaluation.
Thus the coefficient allowances in (13) can be met without a zero table.
The same formulas and analytic errors hold for every real sigma in the
closed interval; interval evaluation of the finite coefficient expressions
can additionally enclose any closed width cell. No grid values alone
certify such a cell.

This procedure may demand prohibitive cutoffs and arithmetic precision.
P_D grows at least on an exp(D^2/2) scale in this chosen bound,
r=T^2/(T^2+1) approaches one, and the coefficient amplification factors
in (13) contain high powers of T. For a common coefficient allowance,
take epsilon smaller than the desired arithmetic error divided by
the sum of its explicit amplification factors. A sufficient absolute
decimal precision is correspondingly set by their base-ten logarithm
and the desired error; large intermediate values require further
working digits. No favorable cancellation or feasible run time is
claimed. In particular this proof does not pay any future minimax
coefficient amplification automatically.

The only noncompact integral taken throughout is the original R with
the proved tail (8). Source formula terms are used on compact spatial
sets or for (5), where their integrability was checked. Cauchy estimates
are applied on an explicit larger disk; all later integrations are finite
or covered by C032m's domination. This settles the specified evaluation
interface, as checked in audit1575 below, without changing stop1571 or
claiming the fixed dictionary reaches its required residual.

### Critical audit1575, 18 November 2026

The audit checks (1)-(13), reusing assessment1573's SPECIALIZE coverage,
source-scope1574 and notes1572/1555. Connes Section 2, equations (4)-(7),
printed p.4, was reopened to check the Mellin hypotheses and constants;
the other cited source coverage is unchanged. No failed inequality or
missing analytic premise was found within this scope. This is a checked
local specialization, not a new general explicit-formula theorem, an
independent verification of the qualified external inputs, or a numerical
certificate. The following computations record the load-bearing checks.

For (1), put y=log(v) and a=s-1/2. The Mellin integral becomes

    (1/(2*pi))*integral_R exp(-sigma*y^2+a*y)*cos(z*y) dy
      =sqrt(pi/sigma)/(4*pi)
           *[exp((a+i*z)^2/(4*sigma))
                       +exp((a-i*z)^2/(4*sigma))].

The coefficient sqrt(pi/sigma)/(4*pi) is exactly one half of the
Gaussian prefactor. Since a=i*z_s, this is the stated half-sum of
G_sigma(z-z_s) and G_sigma(z+z_s). Gaussian domination on bounded
s,z sets justifies the complex shifts; in the source's original
variable it gives every required endpoint power bound. The involution
rho -> 1-rho sends positive to negative ordinates, preserves
multiplicity and negates z_rho. Thus the all-zero sum is 2*p_sigma,
even when distinct off-line zeros have the same positive ordinate.
The excluded ordinate-zero case is essential to this pairing.

At s=0 and s=1 the two exponentials combine to exactly A_sigma(z).
For the archimedean integral, f=f^sharp and v=exp(t) give

    [2*f(v)-2*f(1)/v]*dv/(v-v^(-1))
      =2*[F(exp(t))-exp(-t/2)*F(1)]*B(t) dt.

Here F(1)=1/(2*pi). The constant, integral and prime terms in the
all-zero identity are therefore c/(2*pi), the integral divided by pi,
and the prime sum divided by pi. Dividing by two gives exactly (1),
with both pole terms already combined. The subtraction stays inside
the integral. Neither an RH-dependent spectral reading nor an added
trivial-zero sum enters this calculation.

For (2)-(4), B(t)=exp(-t/2)/(1-exp(-2*t)); on (0,1) its original
form and sinh(t)>=t give B(t)<=exp(1/2)/(2*t)<1/t. On [1,infinity)
the displayed alternative gives B(t)<=2*exp(-t/2). Integrating (3)
against 1/t on (0,1) gives precisely
(1+D^2/4)*exp(D)+1/2. On the tail,
-t^2+(D-1/2)*t<=-t^2/2+D^2/2, and the integral of exp(-t^2/2)
on the positive half-line is less than2. Completing the square in
-l^2+(D+5/2)*l and using sum_(n>=2)n^(-2)<1 gives the stated
prime bound. Finally

    |A_sigma(z)|<=exp((D+1/2)^2/4),  |z|<=D,

by |cos(z/(4*sigma))|<=exp(D/(4*sigma)) and sigma>=1. These
estimates give every term of P_D. They hold on larger disks as well,
so the holomorphic integration and Cauchy uses have compact
dominators, rather than merely pointwise convergence.

For the real-axis bound (5), the baseline integral on (0,1) is at
most3/2; on [1,infinity) it is less than4/3+2=10/3. With
a=1/(1+x), the oscillatory small interval costs x^2*a^2/4<=1/4,
the middle interval costs2*log(1+x), and the tail costs less than8/3.
Consequently their sum is less than8+2*log(1+x). The pole and
constant cost less than2 together; the prime sum costs less than9
before division by2*pi. Hence the resulting bound is at most

    2+(17+2*log(1+x))/6 < 10*(1+log(1+x)).

This includes x=0, where the middle interval is empty, and requires
no sign information about the profile.

For (6), the supremum over l>=log(N) of exp(-l^2+b*l) is
exp(b^2/4-(log(N)-b/2)_+^2); the discarded integer sum is at most1/N.
This covers every omitted prime power, not just primes. The small
endpoint bound is the preceding integral with endpoint a. On t>=A,
A>=2D gives -t^2+D*t<=-t^2/2, leaving precisely d_large after the
factor1/(2*pi). For (7), differentiation of exp(-sigma*t^2)*cos(z*t)
costs at most(4*A+D)*exp(D*A); differentiating the subtraction costs
at most1/2. Also B<=B0 and |B'/B|<=C0 since coth decreases on
positive reals. Each cell of length h contributes at most L*h^2/4
to the midpoint error. Summing J cells and dividing by2*pi proves
d_quad=L*(A-a)^2/(8*pi*J), including the lower-endpoint dependence.

For (8), x>=T>=2M+1 gives |x^2+w^2|>=3*x^2/4. Integration of
10*(1+log(1+x))/x^2 gives at most10*(2+log(1+T))/T, and the
subtracted value costs P_M/T. Thus tau_M(T) bounds the original
absolute combined tail uniformly, with fixed P_M as T increases.
It does not result from integrating prime-side summands separately
over the whole spatial half-line.

The crucial compact step is a derivative estimate. The even entire
error p-p_tilde defines g=h-h_tilde without a square-root branch.
For |u|<=R every square root has modulus<=D, so |g(u)|<=d. If
|u|<=U, its radius-one Cauchy circle lies in |u|<=U+1=R, giving
|g'(u)|<=d. For 0<=x<=T and |w|<=M the entire segment from -w^2
to x^2 lies in |u|<=U. Applying (9) to g therefore bounds the
quotient error by d everywhere on this compact set. At w=+/-ix,
the segment is constant and the value is h'(x^2)=p'(x)/(2*x) for
x>0; at x=w=0 it is h'(0)=p''(0)/2. The same identities hold for
the approximants. These checks exclude both a hidden principal value
and an unjustified division of a value error by a vanishing denominator.

For (10), differentiating the absolutely convergent geometric majorant
gives

    sum_(k=K+1)^infinity k*r^(k-1)
       =r^K*((K+1)-K*r)/(1-r)^2.

Multiplication by H/R is exactly d_K; summing the undifferentiated
majorant gives eta_K. Here 0<r<1 since T>=1. The quotient polynomial
is the identity (a^k-b^k)/(a-b)=sum_(j=0)^(k-1)a^(k-1-j)*b^j
extended also to a=b, with a=x^2 and b=-t^2. Integrating it first
in x and then against4*t dt gives both positive denominators and
the sign(-1)^j in E_hat. Integrating p_K(i*t) against2*pi dt gives
O_hat. Thus (11) has the correct normalization, parity and zero
initial values, including the imaginary-axis primitive paths.

The compact quotient error is at most d+d_K; its spatial integral
costs T. The straight primitive path costs4*|w|^2*integral_0^1 v dv,
which is at most2*M^2. The O path costs2*pi*M and its value error is
d+eta_K. These are exactly (12). For each fixed M>0, choose finite
T first for the tail allowance, then N,A,a,J for a sufficiently small
d at that T,D, and only then K for eta_K,d_K with those constants
fixed. Increasing T changes D,P_D,H,r and cannot preserve earlier
cutoff choices automatically. For M=0 both primitives are exactly0.
Thus the claimed ordered convergence is valid without a simultaneous
uncontrolled limit or a uniform-in-T error assertion.

Finally (13) is the triangle inequality applied to the finite sums in
(11); the k=0 coefficient contributes only to O. Errors in pi and in
the final products and sums must also be enclosed, as the statement
requires. There is no hidden exact-real arithmetic assumption: the
exponential remainder given above, its cosine specialization, positive
square-root bisection and the convergent logarithm series
log(v)=2*sum_(j>=0)r^(2*j+1)/(2*j+1), r=(v-1)/(v+1), suffice for
the coefficient expressions. For v>0, |r|<1 and its tail after j=m
is at most2*|r|^(2*m+3)/((2*m+3)*(1-r^2)). The standard
Gregory-Leibniz alternating series gives pi with error at most
4/(2*m+3) after j=m. The gamma_E bound follows from the positive
telescoping terms in the proof, whose sum is less than1/n.
All such choices are finite, however inefficient. Since sigma stays
in [1,2], these finite expressions have no denominator singularity
and interval evaluation encloses every closed width cell. This asserts
an enclosure, not that a particular partition or precision is adequate.

No actual dictionary kernel, residual, minimax coefficient or running
time is certified here. Large P_D, r near1 and the amplification in
(13) can make this particular procedure impractical. Future exponentials,
sinh evaluations and dictionary coefficients require their own error
propagation. The new checked interface is a specific sharper input that
may justify retesting dictionary1570 under its existing bounded scope;
stop1571 remains a valid obstruction for its old independent boxes,
not for the actual dictionary. Full odd cancellation, positive output,
unrestricted variation and actual-Xi realization remain open.

## Mathlib

Full matching coverage of this shifted explicit formula plus effective
removable primitive evaluator has not been checked and is unknown.
C032m's previously recorded holomorphic integration coverage is reused;
supporting facts about Cauchy's formula, Gaussian integrals and finite
polynomials would not by themselves constitute this result. No formal
verification, new Mathlib theorem search or absence claim is made.
