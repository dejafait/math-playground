# Corollary 997f: positive binomial phase modulation loses the target

## Hypotheses

Use the COMPLETE response H_n^+(z;mu) of C997c(1), with integer n>=2,
K_(n+2)=(L_(n+1)^(2)-1)/(n+1), and

    J=[15/8,17/8], delta=1/8, z_star=1+i/8,
    theta(c)=arccos(1-c/2),
    phi(c)=theta(c)+sqrt(c*(4-c))/2.

Take the real branches on J and their local holomorphic extensions
from audited C997e(4),(15)-(16). Fix kappa>0, tau>0 and A before n,
with A>=C997e's existential A_0 and A>kappa*tau^2/2. Set

    m_n=floor(kappa*n), P_n(c)=(1+i*tau*(c-2))^m_n,
    M_n=integral_J exp(-A*n*(c-2)^2)*|P_n(c)|dc,
    dmu_n(c)=M_n^(-1)*1_J(c)*exp(-A*n*(c-2)^2)*P_n(c)
                                      *exp(i*n*(phi(c)-c))dc. (1)

These are finite hypothetical complex slope measures, not zeta zeros.
The polynomial degree is exactly m_n, including degree zero at any
initial index where m_n=0. No parameter is allowed to vary with n.

## Conclusion

Every mu_n has original total variation one. There are constants
eta>0, C<infinity and n_0, depending only on the fixed parameters and
analytic neighborhood, such that

    |H_n^+(z_star;mu_n)|<=C*(n+2)*exp(-eta*n), n>=n_0.       (2)

Here is a specific admissible eta. Choose h>0 so that a neighborhood
of the closed rectangle 2-delta<=Re(c)<=2+delta, 0<=Im(c)<=h lies
in C997e's amplitude domain and Re(phi'(c))>=1/3 there. Put

    D=A-kappa*tau^2/2>0, B=A+kappa*tau^2/2,
    y_0=min{h/2,kappa*tau/(4*B)},
    eta=min{kappa*tau*y_0/4,D/64,1/16}>0.                  (3)

Consequently limsup n^(-1)*log|H_n^+(z_star;mu_n)|<=-eta, with
log(0)=-infinity. No unbounded integer subsequence can satisfy the
required target bound |H_n^+(z_star)|>=exp(-a_n), a_n>=0, a_n/n->0.

Equivalently, if a scalar multiple nu_n=s_n*mu_n satisfies that target
bound at any sufficiently large index, its ORIGINAL variation obeys

    ||nu_n||_TV>=exp(eta*n-a_n)/(C*(n+2)).                  (4)

In particular, normalization to |H_n^+(z_star;nu_n)|=1 requires this
exponential variation cost with a_n=0. If the unscaled response is zero,
that normalization is impossible. Equations (2)-(4) stop only the
positive binomial phase family (1) under A>kappa*tau^2/2. They do not
assert any data-band bound or exclude arbitrary polynomial multipliers.

Step331, 10 November 2026: RESEARCH / POTENTIALLY_NEW, outcome NEGATIVE
under the pre-invocation EXPLORE review329 and its unchanged covered
polynomial-packet target. This is a local subclass obstruction obtained
by a known contour method; the checked sources did not state this exact
normalized response bound. No originality certification or RH advance
is asserted. Independent conceptual audit remains pending.

## Proof

### Reused analytic input and the specialization being made

Use audited C997e(4),(15)-(16)'s EXACT two-branch representation on a
fixed complex neighborhood of J, uniformly for u in [0,2]:

    L_(n+1)^(2)(c*(n+u))/(n+1)
      =n^(-3/2)*exp(c*(n+u)/2)*[
        exp(-i*n*phi(c))*B_(-,n)(c,u)
        +exp(i*n*phi(c))*B_(+,n)(c,u)].                     (5)

Both B_(+/-,n) are holomorphic in c and uniformly bounded on the
fixed domain for all sufficiently large n. Its source is M. Vanlessen,
*Strong asymptotics of Laguerre-type orthogonal polynomials and
applications in random matrix theory*,
[math/0504604v2, 29 August 2005](https://arxiv.org/pdf/math/0504604v2),
Theorem2.4(b)/(2.13), Remarks2.3/2.5, Proposition3.31,
Theorem3.32/(3.110), and Proposition5.1/(5.5)-(5.6), printed
pp5-7,32-34,39. The specialization Q(x)=x, alpha=2, degree N=n+1,
normalization and exact analytic error matrix were justified and
audited in C997e. They are unchanged here and are not reproved.

The necessary new specialization is an exponential contour estimate
for the degree-growing P_n with its ORIGINAL M_n. The polynomial
growth is paid explicitly below. No weighted norm theorem, Gaussian
full-line substitution or continued real-axis O term is used. The
primary weighted Bernstein-Markov/Bernstein-Walsh tools assessed in
review329 are not needed for this explicit polynomial. Cauchy's
integral theorem for a rectangle and finite-integral Fubini are used
in their standard named forms. No new asymptotic theorem is imported.

### Original normalization and the complete target response

On J the phase phi-c is real, and

    |P_n(c)|=(1+tau^2*(c-2)^2)^(m_n/2)>=1.

Thus M_n>0, (1) has variation exactly one, and for all n with
1/sqrt(A*n)<=delta,

    M_n>=integral_J exp(-A*n*(c-2)^2)dc
        >=2*exp(-1)/sqrt(A*n).                            (6)

The last inequality integrates over |c-2|<=1/sqrt(A*n); no replacement
of the original normalization is made. We need a lower bound on M_n
only, since the goal is an upper bound on its normalized response.

Expand the cosh and K in the upper interval of C997c(1). The positive
beta Laguerre term, including its sign, is

    -integral_J exp(-c*n/4)*integral_(cn)^(c(n+2))
       [L_(n+1)^(2)(t)/(n+1)]*exp((-1/8+i*z_star)*t)dt dmu_n(c).

Substitute (5) and t=c*(n+u). Since i*z_star=i-1/8, multiplication
by the phase in (1) leaves beta_(z_star)=1/8+i*(z_star-1)=0.
Consequently the COMPLETE response is exactly

    H_n^+(z_star;mu_n)=n^(-3/2)*M_n^(-1)*(I_(-,n)+I_(+,n))+R_n,
    I_(-,n)=integral_J exp(-A*n*(c-2)^2)*P_n(c)*a_(-,n)(c)dc,
    I_(+,n)=integral_J exp(-A*n*(c-2)^2)*P_n(c)
                                *exp(2*i*n*phi(c))*a_(+,n)(c)dc,
    a_(+/-,n)(c)=-c*integral_0^2
                      exp(c*u*(3/8+i*z_star))*B_(+/-,n)(c,u)du. (7)

The a_(+/-,n) are holomorphic and uniformly bounded on a neighborhood
of the closed rectangle in (3), by (5) and finite integration. The
polynomial P_n is NOT absorbed into that bounded-amplitude assertion.
Every integral defining (7) is finite on a compact rectangle, which
justifies the initial Fubini rearrangement.

For clarity, R_n contains the reflected-beta Laguerre upper term, the
ENTIRE upper constant subtraction and the COMPLETE lower interval.
L997(4), based on [DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), gives
|L_(n+1)^(2)(t)/(n+1)|<=C*(n+2)*exp(t/2) for t>=0 after adding
back 1/(n+1). At the target, |exp(i*z_star*t)|=exp(-t/8)<=1.
The reflected-beta upper term is therefore bounded by its fixed
length times C*(n+2)*exp(-cn/4-3t/8), t>=cn. The entire constant
subtraction is bounded by a constant times
exp(-cn/4-t/8), t>=cn. Both decay faster than exp(-n/16), uniformly
for c in J. Integrating these bounds uses ||mu_n||_TV=1, so all
polynomial growth on the REAL interval is already accounted for.

C997c(5) bounds the lower spectral measure's variation by
8*exp(3/4)*(n+2)*exp(-n/16)||mu_n||_TV. Its support is t>=n,
so evaluation at z_star multiplies its absolute density by at most
exp(-n/8). In particular, with a constant independent of n,

    |R_n|<=C_0*(n+2)*exp(-n/16).                           (8)

Thus neither beta sign, interval, nor K's -1 has been discarded.

### The polynomial's charged complex growth

Write c=2+x+i*v, where x is real and 0<=v<=h, and put
kappa_n=m_n/n. For n>=2/kappa, kappa/2<=kappa_n<=kappa.
The elementary inequality r<=exp(r-1), r>=0, gives

    |1+i*tau*(x+i*v)|^m_n
      <=exp((m_n/2)*[-2*tau*v+tau^2*(x^2+v^2)]).

This includes r=0; it does not require choosing a logarithm at a
polynomial zero. Multiplying by the modulus of the Gaussian gives

    |exp(-A*n*(c-2)^2)*P_n(c)|
       <=exp(n*[-(A-kappa_n*tau^2/2)*x^2
                    +(A+kappa_n*tau^2/2)*v^2-kappa_n*tau*v])
       <=exp(n*[-D*x^2+B*v^2-kappa*tau*v/2]).              (9)

Every positive polynomial-dependent contour cost is present in B
and D. Since phi is real on J and Re(phi')>=1/3 on the rectangle,
vertical integration gives Im(phi(2+x+i*v))>=v/3. Hence

    |exp(2*i*n*phi(2+x+i*v))|<=exp(-2*n*v/3)<=1.           (10)

The same (9) bound therefore controls the plus branch as well.

### Deform both exact integrals and retain both endpoints

The integrands of (7), without the indicator of J, are holomorphic
on a neighborhood of the closed rectangle. Deform the REAL interval
to its horizontal translate at height y_0, keeping both vertical
endpoint segments. This does not assume that the indicator extends
holomorphically. All three segments have bounded total length, and
the exact a_(+/-,n) have a common bound on them.

On the horizontal segment, B*y_0<=kappa*tau/4 yields

    -D*x^2+B*y_0^2-kappa*tau*y_0/2
        <=-D*x^2-kappa*tau*y_0/4.                         (11)

On either vertical endpoint x=+/-delta, 0<=v<=y_0,

    -D*delta^2+B*v^2-kappa*tau*v/2
        <=-D*delta^2-kappa*tau*v/4<=-D/64.                (12)

Using (9)-(12) and Cauchy's theorem separately for I_(-,n) and
I_(+,n), we obtain, with n-independent C_1,

    |I_(-,n)|+|I_(+,n)|
       <=C_1*[exp(-kappa*tau*y_0*n/4)+exp(-D*n/64)].        (13)

There is no unestimated cancellation, saddle coefficient or isolated
data zero in this bound. It holds for the exact analytic amplitudes,
including all their errors.

By (6), n^(-3/2)/M_n<=exp(1)*sqrt(A)/(2*n). Combining (7),(8),(13)
with (3) proves (2) after increasing C and n_0. If the required target
lower bound held on any unbounded integer subsequence, it would imply
eta*n<=a_n+log(C*(n+2)) there. Division by n contradicts eta>0.
Finally complex linearity of H and ||s_n*mu_n||_TV=|s_n| prove (4).
This is a necessary normalization lower bound, not a failed data
upper estimate interpreted as impossibility.

### Qualifications and downstream use

The proposed mechanism was an added positive phase through powers of
a linear factor. For this specified family the target-retention cost
already fails, so no data-band estimate is needed to rule out its
simultaneous thresholds. This does not prove that its data response is
large or that general polynomial modulation cannot work. In particular
the proof requires tau>0, kappa>0 and D>0 fixed; it gives no positive
rate uniform as tau or kappa tends to zero, D tends to zero, or any
parameter varies with n. The zero-tilt case is not inferred from (2).

The result is a contrast to audited C997e's unmodulated leakage and
C997b's atomic normalization stop, not a new assumption excluding all
packets. It narrows a candidate construction for the one-sided point
bridge. General multipliers, the point inequality, selected/both-sign
transfer, C997a(8), the original assay, reconstruction, signed recovery,
infinite-zero complements, regulator uniformity, L993 and L984(H) all
remain open. No RH-equivalent positivity or infinite-zero interchange
is used. This finite-input obstruction is not an RH candidate.

## Mathlib

Full matching coverage for this exact normalized Laguerre response and
its polynomial-packet bound has not been checked and is unknown. No
formal theorem is asserted. Cauchy's integral theorem, elementary
exponential inequalities and finite-measure integration are standard
supporting tools; their formal availability alone would not supply
the analytic amplitude input or this complete-response specialization.
