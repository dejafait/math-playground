# Lemma 990: signed endpoint-null response on defined integer indices

## Hypotheses

For integers n>=2 and j=0,1,2 use the exact real polynomials

    K_(n+j)(u)=[L_(n+j-1)^(2)(u)-1]/(n+j-1).

Set a_n=(K_n(n),K_(n+1)(n),K_(n+2)(n)),
b_n=(K_n(2n),K_(n+1)(2n),K_(n+2)(2n)), d_n=a_n cross b_n,
with this orientation, and D={n>=2:d_n!=0}. Only for n in D define

    c_n=d_n/||d_n||_1,
    F_n(u)=sum_(j=0)^2 c_(n,j)*K_(n+j)(u),  n<=u<=2n.

Fix tau=10^13 and Q={3/4+i*tau,3/4-i*tau,1/4-i*tau,1/4+i*tau},
each with weight1. For n in D put

    Z_n=-Re sum_(q in Q) integral_n^(2n) exp((q-1)*u)*F_n(u)du.

These are finite integrals. Q is synthetic; its members are not
asserted to be zeta zeros. No RH, zero simplicity, arithmetic transfer,
growing height, eventual definition or phase independence is assumed.

## Conclusion

The exact constraints F_n(n)=F_n(2n)=0 and ||c_n||_1=1 hold on D.
There is an infinite set of integer indices in D on which

    Z_n >= c*exp(n/2)*n^(-3/2),                         (1)

for a fixed c>0. At every sufficiently large index in D,
|Z_n|<=C*exp(n/2)*n^(-3/2). Consequently

    limsup_(n->infinity, n in D)
           log(1+max(Z_n,0))/n = 1/2.                 (2)

The set D is not proved cofinite within this lemma. The subsequent
C990a establishes eventual definition, critically audited in step265.
Step267 critically audits the signed-response argument below and
accepts (1)-(2) and the uniform upper bound on D. Together these two
audited results complete review259's synthetic diagnostic. Normalized asymptotic errors
are controlled on the positive subsequence; no uniform lower bound
for the leading cross product at all integer indices is asserted.
If d_n=0 at a sufficiently large integer, then b_n=lambda_n*a_n
with |lambda_n| comparable to exp(n/2), and exactly

    L_n^2(n)=2-2/lambda_n, L_n^2(2n)=lambda_n-1.        (3a)

Thus both middle-degree endpoint values must be exponentially small
relative to their respective bulk amplitudes. This necessary
condition is not proved impossible here.

Step261, 10 November2026: REPRODUCTION, a local specialization of
the approved sources. This is partial progress in the synthetic
viability question, not a result beyond the sources checked, payment
of B_n or L984(H), an RH candidate, or a separate critical audit.

## Proof

### Imported tools and their common-interval specialization

L985 supplies the exact connection, from
[DLMF18.18.18](https://dlmf.nist.gov/18.18.E18) with alpha=1,
beta=2: the connection coefficients (1)_k/k! are1; remove the
degree-zero term. Its Vaughan estimates are not used. L987 is a
benchmark for the proof method, not an input about this new interval.

Import A. Gil, J. Segura and N. M. Temme, *Asymptotic approximations
to the nodes and weights of Gauss–Hermite and Gauss–Laguerre
quadratures*, [arXiv1709.09656v1, 27September2017, section3.3,
equations81–87](https://arxiv.org/html/1709.09656v1#S3.SS3), and
[DLMF10.17.1–3](https://dlmf.nist.gov/10.17#i) with fixed Bessel
orders2,3 and positive real arguments. GST's fixed-alpha uniform
Poincare expansion is used on a compact positive bulk interval.
The source convention and its conversion are explicit below; no
second-order coefficient, differentiated remainder, numerical error
table or assumed expansion of individual zeros is used. This is the
first-order source contract approved in review265/source-notes262.
The former DLMF coefficient presentation and its recorded discrepancy
are preserved there and in history/2026-11-10-endpoint-null-signed-audit-267.md.

For m=n+j put

    nu_m=4m+2, t=u/nu_m,
    xi(t)=[sqrt(t-t^2)+arcsin(sqrt(t))]/2,
    D_0(t)=4*t^(5/4)*(1-t)^(1/4),
    A_m(u)=sqrt(2/(pi*nu_m))/[(m-1)*D_0(t)],
    Phi_m(u)=nu_m*xi(t)-5*pi/4.

For n>=2, j=0,1,2 and n<=u<=2n, t is in J=[1/9,1/2].
Indeed its smallest possible value is n/(4n+10)>=1/9.
GST's degree is m-1, its parameter is v_m=2m+1=nu_m/2,
rho=t, and zeta=xi(t)^2. At alpha=2 its prefactor satisfies
chi(zeta)/(4*zeta)=sqrt(xi(t))/D_0(t). Thus its exact representation is

    L_(m-1)^(2)(u)=exp(u/2)*sqrt(xi(t))/D_0(t)
      *[J_2(nu_m*xi(t))*A_G-J_3(nu_m*xi(t))*B_G/xi(t)],
    A_G=1+O(v_m^-2), B_G=O(v_m^-1).

These are uniform absolute bounds on J, with delta=1/2. On J,
xi is positive and bounded away from zero, and the displayed
t-dependent prefactors are bounded. Fixed-order Bessel asymptotics give
J_2(nu_m*xi)=sqrt(2/(pi*nu_m*xi))*cos(Phi_m)+O(n^-3/2)
and J_3(nu_m*xi)=O(n^-1/2). The B_G term is O(n^-3/2),
and (A_G-1)*J_2 is smaller. Divide by m-1, retaining the
exact constant subtraction. This proves, uniformly in all three degrees,

    K_m(u)=exp(u/2)*A_m(u)*cos(Phi_m(u))-1/(m-1)+E_m(u),
    |E_m(u)|<=C_B*exp(u/2)*n^(-5/2).                  (3)

The source first gives this beyond a fixed onset; finitely many
earlier compact intervals can be included by enlarging C_B. This
is an additive bound, including at cosine zeros. Differentiating
only the displayed smooth amplitude and phase gives

    |A_m|<=C_A*n^(-3/2), |A_m'|<=C_A'*n^(-5/2),
    p_m=Phi_m'=sqrt(nu_m-u)/(2*sqrt(u)),
    p_m'=-nu_m/[4*u^(3/2)*sqrt(nu_m-u)], |p_m'|<=C_p/n. (4)

All constants are finite maxima on J: 1/D_0 and its derivative
are bounded; 4n<=nu_m<=9n and nu_m-u>=2n give the last bound.
No derivative of E_m is taken.

### Endpoint rows and controlled normalization

Let

    kappa_1=sqrt(3)/2+pi/3, kappa_2=1+pi/2,
    phi_n=n*kappa_1-13*pi/12, psi_n=n*kappa_2-pi,
    v(phi)=(cos(phi),cos(phi+pi/3),cos(phi+2*pi/3)),
    w(psi)=(cos(psi),-sin(psi),-cos(psi)),
    h(phi,psi)=v(phi) cross w(psi),
    S(psi)=(sin(psi),cos(psi),-sin(psi)).

For r=1,2 and bounded delta=4j+2, Taylor's theorem, with u=rn,
applied to nu*xi(rn/nu) at nu=4n gives

    (4n+delta)*xi(rn/(4n+delta))
      =4n*xi(r/4)+delta*[xi(r/4)-(r/4)*xi'(r/4)]+O(1/n).

The second derivative is t^2*xi''(t)/nu=O(1/n) on J.
The bracket is arcsin(sqrt(r/4))/2, equal to pi/12 or pi/8.
Therefore the phases at n are phi_n+j*pi/3+O(1/n), and at
2n they are psi_n+j*pi/2+O(1/n). Similarly, bounded derivatives
of 1/D_0 give

    A_(n+j)(rn)=a_r*n^(-3/2)+O(n^(-5/2)),
    a_r=1/[sqrt(2*pi)*D_0(r/4)]>0,
    a_2=1/(2*sqrt(pi)).

In (3), the constant corrections divided by
exp(rn/2)*n^(-3/2) are O(sqrt(n)*exp(-rn/2))=O(1/n).
Consequently there are positive row scales
A_n^*=a_1*exp(n/2)*n^(-3/2), B_n^*=a_2*exp(n)*n^(-3/2),
such that

    a_n/A_n^*=v(phi_n)+O_1(1/n),
    b_n/B_n^*=w(psi_n)+O_1(1/n),
    d_n/(A_n^* B_n^*)=h(phi_n,psi_n)+O_1(1/n).         (5)

Here O_1 is in the l1 norm, with a uniform constant; boundedness
of the two leading rows proves the cross-product error estimate.
For any fixed eta>0, on indices with ||h(phi_n,psi_n)||_1>=eta,
(5) proves d_n!=0 eventually and

    c_n=h(phi_n,psi_n)/||h(phi_n,psi_n)||_1+O_1(1/(n*eta)). (6)

To justify division: if x=h+e and ||e||_1<=eta/2, then
||x||_1>=eta/2 and
||x/||x||_1-h/||h||_1||_1<=4*||e||_1/eta.
Positive row scales preserve the prescribed orientation.
Exact cross-product orthogonality, not (5), proves both endpoint
constraints and the exact normalization for every n in D.

Write C=cos(phi), D_1=cos(phi+pi/3), E=cos(psi), T=sin(psi).
Then v=(C,D_1,D_1-C), w=(E,-T,-E), and direct multiplication gives

    h=(-D_1*E+(D_1-C)*T, D_1*E, -C*T-D_1*E),
    h dot S(psi)=D_1.                                (7)

In particular h(-pi/3,0)=(-1,1,-1). The leading cross product
can vanish: (7) implies h=0 precisely when D_1=0 and T=0
(if D_1=0 then C!=0). Thus (6) cannot simply be asserted with
one positive eta for all integers.

### Finite transform with all corrections and quartet terms

For a=1/4 or -1/4 define z_a=a-1/2+i*tau and

    I_(a,m)=integral_n^(2n) exp(z_a*u)*K_m(u)du,
    g_(a,sigma,m)(u)=a+i*(tau+sigma*p_m(u)), sigma=+1,-1,
    H_(a,m)=[exp(2n*z_a)-exp(n*z_a)]/[(m-1)*z_a],
    T_a(n)=integral_n^(2n) exp(a*u)du.

For n in D the four original terms give exactly

    Z_n=-2*Re sum_(j=0)^2 c_(n,j)*(I_(1/4,n+j)+I_(-1/4,n+j)). (8)

Expand the cosine in (3). Since |g|>=1/4, finite integration by
parts, as in [DLMF2.3.4-6](https://dlmf.nist.gov/2.3#i), gives

    I_(a,m)=1/2*sum_(sigma=+1,-1)
       [exp(a*u+i*(tau*u+sigma*Phi_m(u)))*A_m(u)/g_(a,sigma,m)(u)]_n^(2n)
       -H_(a,m)+R_(a,m),
    |R_(a,m)|<=C_R*n^(-5/2)*T_a(n).                   (9)

For completeness the remaining integrand from this finite identity
is minus the same exponential times (A_m/g)'. By (4),
|(A_m/g)'|<=4|A_m'|+16|A_m||p_m'|<=C*n^(-5/2).
Integrating this bound and (3)'s E_m proves (9), without an
oscillatory estimate on E_m or a fixed-amplitude uniformity assumption.

The full -1 correction is H_(a,m), before any bounding. Uniformly
over j it satisfies |H_(1/4,m)|<=8*n^(-1)*exp(-n/4) and
|H_(-1/4,m)|<=(8/3)*n^(-1)*exp(-3n/4).
Also T_(1/4)=4*(exp(n/2)-exp(n/4)) and
T_(-1/4)=4*(exp(-n/4)-exp(-n/2)). In the weighted sum all these
estimates remain valid because ||c_n||_1=1. The lower a=1/4
endpoint is O(exp(n/4)*n^(-3/2)); the entire a=-1/4 pair is
O(exp(-n/4)*n^(-3/2)). Neither pair nor endpoint is omitted in (9).

At 2n, (4) and the endpoint expansions give
p_(n+j)(2n)=1/2+O(1/n) and
A_(n+j)(2n)=a_2*n^(-3/2)+O(n^(-5/2)). Replacing only these
explicit endpoint quantities and phases in (9) costs
O(exp(n/2)*n^(-5/2)), uniformly on every defined index. In fact
|1/g-1/(1/4+i*(tau+sigma/2))|<=16*|p_m(2n)-1/2|.
The smaller pieces above are absorbable at this scale. Hence, with

    U_n=sum_(j=0)^2 c_(n,j)*exp(i*(psi_n+j*pi/2)),
    s_n=c_n dot S(psi_n),
    G=(1/4+i*tau)^2+1/4,

we obtain

    Z_n=-a_2*exp(n/2)*n^(-3/2)
       *Re(exp(2*i*tau*n)*(U_n/(1/4+i*(tau+1/2))
                          +conj(U_n)/(1/4+i*(tau-1/2))))
       +O(exp(n/2)*n^(-5/2)).                         (10)

Exact c_n dot b_n=0 and (5) imply Re(U_n)=c_n dot w(psi_n)=O(1/n),
uniformly even near a small nonzero d_n, since ||c_n||_1=1.
Thus U_n=i*s_n+O(1/n), and elementary subtraction gives

    i/(1/4+i*(tau+1/2))-i/(1/4+i*(tau-1/2))=1/G.

Equation (10) reduces to the useful signed formula

    Z_n=a_2*exp(n/2)*n^(-3/2)
             *[-s_n*Re(exp(2*i*tau*n)/G)+O(1/n)].      (11)

This error is uniform on D, with fixed tau; no small determinant
has been divided out. Since |s_n|<=1, (11) proves the upper bound.
For ||h||_1>=eta, (6)-(7) also give

    s_n=cos(phi_n+pi/3)/||h(phi_n,psi_n)||_1+O(1/(n*eta)). (12)

### An integer positive subsequence with the actual phase relation

Import Lindemann-Weierstrass as stated in L. Fukshansky,
*Geometric Number Theory*, undated author notes,
[Theorem6.2.1, printed p138](https://www1.claremontmckenna.edu/pages/faculty/lenny/papers/GNT_lecture_notes.pdf#page=142):
exponentials of distinct algebraic numbers are linearly independent
over the algebraic numbers. It implies that pi is transcendental:
if pi were algebraic, the distinct algebraic exponents0,i*pi and
coefficients1,1 would contradict exp(0)+exp(i*pi)=0.

On a fixed residue class n=12k+r, the phase pair (phi_n,psi_n)
has increments (6*sqrt(3),12) modulo2*pi. For a nonzero integer
character (h1,h2), resonance would mean

    6*h1*sqrt(3)+12*h2=2*pi*l

for an integer l. If l!=0 this makes pi algebraic; if l=0,
irrationality of sqrt(3) forces h1=h2=0. Thus no nonzero character
resonates. Apply the Weyl criterion and linear-sequence result in
T. Tao, *Higher Order Fourier Analysis*,
[5June2012 manuscript, Proposition1.1.2, Exercise1.1.5 and
Proposition1.1.5, printed pp5-7](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf#page=13).
The phase pair is equidistributed on the two-dimensional torus
on each residue class, hence visits every nonempty open rectangle
infinitely often. We have verified the independence it needs.

There is an essential dependence with the quartet phase, which we
retain: since tau=10^13 is an even integer,

    exp(2*i*tau*psi_n)=exp(2*i*tau*n).

Indeed their quotient is exp(i*pi*tau*n-2*i*pi*tau)=1.
On ||h||_1>0 define the continuous real function

    J(phi,psi)=-cos(phi+pi/3)/||h(phi,psi)||_1
                               *Re(exp(2*i*tau*psi)/G).

At (phi,psi)=(-pi/3,0), ||h||_1=3, and

    J(-pi/3,0)=-Re(1/G)/3>0,
    Re(1/G)=(5/16-tau^2)/[(5/16-tau^2)^2+tau^2/4]<0.

By continuity there is a fixed open rectangle around that point
on which ||h||_1>1 and J>delta:=J(-pi/3,0)/2>0.
It can be very small at this fixed large tau; only its positive
size matters. Equidistribution supplies infinitely many integer
indices there. For all sufficiently large such n, (5)-(6) give
n in D, and (11)-(12) give

    Z_n>=a_2*(delta/2)*exp(n/2)*n^(-3/2).

The fixed additive O(1/n) has been made smaller than delta/2;
no effective onset or growing-tau uniformity is asserted. This
proves (1). The upper bound and this infinite subsequence prove (2).

### Exact reduction of the outstanding definition obligation

Write p_k(u)=L_k^2(u). The finite polynomial identity

    (n+1)*p_(n+1)(u)=(2n+3-u)*p_n(u)-(n+2)*p_(n-1)(u)

can be checked from p_k(u)=sum_(r=0)^k (-1)^r*binom(k+2,k-r)*u^r/r!.
Indeed coefficient comparison reduces it to

    (n+1)*binom(n+3,n+1-r)
      =(2n+3)*binom(n+2,n-r)+r*binom(n+2,n+1-r)
                                      -(n+2)*binom(n+1,n-1-r),

which follows by inserting the factorials, with out-of-range
binomial coefficients zero. This is finite algebra used to track
the prescribed constant shifts, not a new general recurrence result.
Substitution of p_(n+j-1)=(n+j-1)*K_(n+j)+1 gives exactly

    R(u) dot (K_n(u),K_(n+1)(u),K_(n+2)(u))=-u,
    R(u)=((n-1)*(n+2),-n*(2n+3-u),(n+1)^2).           (13)

The two leading rows v,w never vanish: if cos(phi)=0 its shifted
cosine by pi/3 is nonzero, and ||w||_2^2=1+cos(psi)^2>=1.
Their norms therefore have positive minima and finite maxima on
their compact phase circles. By (5), a_n and b_n are nonzero for
all sufficiently large n, with norms comparable respectively to
exp(n/2)*n^(-3/2) and exp(n)*n^(-3/2).

If d_n=0 at such an index, write b_n=lambda_n*a_n with lambda_n
real and nonzero. The norm ratio gives |lambda_n| comparable to
exp(n/2). Since R(2n)-R(n)=(0,n^2,0), applying (13) at both
endpoints gives

    lambda_n*(-n+n^2*K_(n+1)(n))=-2n.

Using n*K_(n+1)(n)=p_n(n)-1 and then the middle component of
b_n=lambda_n*a_n proves (3a). The bulk amplitude of p_n at rn
is exp(rn/2)*sqrt(2/(pi*(4n+6)))/D_0(rn/(4n+6)), comparable
to exp(rn/2)*n^(-1/2). Both ratios in (3a) to these amplitudes
are consequently O(sqrt(n)*exp(-n/2)). This exact necessary
condition may support a later nonvanishing proof; first-order
phase errors alone have not excluded it.

### Independent signed-response audit — step267, 10 November2026

REPRODUCTION under the pre-existing SPECIALIZE assessment review265.
The audit accepts (1), (2), and the uniform upper bound on D. It
does not rely on C990a for the subsequence proof or add a dependency
from this lemma to that corollary. The following checks specify the
load-bearing bounds; no numerical diagnostic or script is required.

The source normalization is nu_m=2v_m=4m+2, not 4m+6: the
polynomial degree here is m-1. GST81–84 and A_0=1 were rechecked
on the common compact J. The replacement above uses only the
already approved first-order GST contract. The disputed explicit
correction is unnecessary at this error scale. All three degrees
obey the same additive error, including at cosine zeros.

For the finite transform (9), if
V=exp(a*u+i*(tau*u+sigma*Phi_m)), then V'=g*V.
Consequently integral V*A=[V*A/g]-integral V*(A/g)'
is an exact finite identity. The bounds |g|>=1/4 and
|(A/g)'|<=4*C_A'*n^(-5/2)+16*C_A*C_p*n^(-5/2)
give its uniform remainder. The other remainder is bounded by
integral exp((a-1/2)u)*|E_m(u)|du
<=C_B*n^(-5/2)*T_a(n). No derivative of E_m occurs.
The constant subtraction is exactly -H_(a,m). Its two displayed
bounds follow from |z_(1/4)|>=1/4, |z_(-1/4)|>=3/4 and
1/(m-1)<=2/n. The conjugate pairs yield the factor -2 in (8);
the reflected pair, lower endpoint and constants all fit the
O(exp(n/2)*n^(-5/2)) error for sufficiently large n. This
checks every quartet term and endpoint without a cancellation premise.

Equation (5) and exact c_n dot b_n=0 give
|Re(U_n)|<=||c_n||_1*||b_n/B_n^*-w||_infinity=O(1/n).
This argument is uniform on D, including ill-conditioned indices.
The resolvent subtraction has the positive sign +1/G; the negative
sign of (11) comes from the definition of Z_n. Equation (7) and
the positive row scales fix s_n's sign on the selected neighborhood.
The leading amplitudes and phase constants were checked directly:
4*xi(1/4)=kappa_1, 4*xi(1/2)=kappa_2,
2*(pi/12)-5*pi/4=-13*pi/12,
2*(pi/8)-5*pi/4=-pi, and a_2=1/(2*sqrt(pi)).

On n=12k+r, every nonzero integer character is nonresonant:
6*h1*sqrt(3)+12*h2=2*pi*l with l!=0 would make pi algebraic;
with l=0, irrationality of sqrt(3) forces h1=h2=0. These are
both possible rational-relation cases. The cited Lindemann–Weierstrass
application uses the distinct hypothetical algebraic exponents0,i*pi
and nonzero algebraic coefficients1,1. Tao's torus criterion then
applies. The third phase is not independent: exp(2*i*tau*psi_n)
=exp(2*i*tau*n) because the specified tau is an even integer.

Put A_tau=tau^2-5/16>0. The exact positive witness value is

    J_0=J(-pi/3,0)=A_tau/[3*(A_tau^2+tau^2/4)]>0.

Choose the fixed open rectangle from the proof, with ||h||_1>1
and J>delta=J_0/2. Uniform (11) and (12) supply a finite
C_tau such that, on its sufficiently large integer visits,

    |Z_n/(a_2*exp(n/2)*n^(-3/2))-J(phi_n,psi_n)|<=C_tau/n.

Require n>=2*C_tau/delta as well as the bulk/normalization
onsets. Then the required leading margin is delta/2 and
c=a_2*delta/2>0. Equidistribution supplies infinitely many
visits after this finite threshold. This pays the fixed tau=10^13
comparison without asserting an effective onset. Globally |s_n|<=1
in (11), proving the upper bound on D without uniform conditioning.
Taking logarithms along the positive subsequence and in the absolute
upper bound gives exactly rate1/2, not merely a positive rate.

### Remaining obligation and scope

This proof establishes controlled spectral sensitivity on infinitely
many defined indices with the prescribed orientation. Cofinite
definition is supplied separately by audited C990a; no global
conditioning estimate is inferred near the phase collisions in (7).

A separate second-order nonvanishing attempt and its unresolved
coefficient diagnostic are preserved in
`drafts/2026-11-10-endpoint-null-filter-working-261.md` and
`scripts/endpoint-null-filter/phase-check-261.json` (reproduce with
`python3 scripts/endpoint-null-filter/phase-check-261.py`). Neither
is an input to this first-order proof. Their finite numerical output
does not verify or refute an asymptotic source theorem.

Actual-zero realization, other-zero cancellation, the F_n arithmetic
compensator with every prime power, transfer to the original B_n,
both complements and L984(H) remain unresolved. No infinite zero
sum, contour exchange, numerical implication of RH, or assumed
target-equivalent positivity occurs here.

## Mathlib

Full matching Mathlib coverage of this normalized moving filter and
its signed defined-subsequence response has not been checked. The
external analytical and equidistribution inputs are cited precisely
above. Supporting finite algebra does not establish formal coverage
of the full result; unknown availability is not absence.
