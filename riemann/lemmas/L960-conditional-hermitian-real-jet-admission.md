# Lemma 960: conditional Hermitian admission of the physical real jet

## Hypotheses

Use the source convention

    Phi(v)=sum_(n>=1) (2pi^2 n^4 exp(9v)-3pi n^2 exp(5v))
                         exp(-pi n^2 exp(4v)),
    H_t(z)=integral_0^infinity exp(tv^2) Phi(v) cos(zv) dv.

Fix real t,x with

    98/625 <= t <= 1/5,
    X=6000000185827 <= x <= W_g=120000000000000,
    N=floor(sqrt(x/(4pi)+t/16)).

At a wall x=4pi(j^2-t/16), take N=j. In all local analytic
definitions and spatial derivatives below, N and t are fixed at their
centre values. Every integer n<=N and every prime dividing such an
integer is included.

Define, with conjugation-compatible analytic logarithm branches on a
neighbourhood of the centre,

    M_0(s)=sqrt(2pi)/16 * s(s-1) pi^(-s/2)
                       exp(((s-1)/2) Log(s/2)-s/2),
    alpha(s)=1/(2s)+1/(s-1)+(1/2) Log(s/(2pi)),
    M_t(s)=M_0(s) exp(t alpha(s)^2/4),
    s_+(z)=(1+iz)/2,             s_-(z)=(1-iz)/2,
    w_+(z)=s_+(z)+t alpha(s_+(z))/2,
    w_-(z)=s_-(z)+t alpha(s_-(z))/2,
    A_+(z)=sum_(n<=N) exp(t log(n)^2/4-w_+(z) log n),
    A_-(z)=sum_(n<=N) exp(t log(n)^2/4-w_-(z) log n).

Let mathcal_L_+,mathcal_L_- be the corresponding analytic logarithms
of M_t(s_+),M_t(s_-), and put

    J=(mathcal_L_++mathcal_L_-)/2,
    Theta=(mathcal_L_+-mathcal_L_-)/(2i),
    G=exp(J),                   P=exp(i Theta),
    u=H_t/G,                    V=PA_++P^(-1)A_-,
    r=u-V.

Assume these functions are holomorphic on a neighbourhood of the
centre; G,Theta,u,V,r are real-type, G(x)>0, and the minus and plus
coordinates are conjugate on the local real interval. These are local
analytic hypotheses, also required at an exact index wall. Real-type
means f(conj(z))=conj(f(z)) on a conjugation-invariant neighbourhood.
In particular r(x),r'(x),Theta(x),Theta'(x) are real and |P(x)|=1.

At the centre set w=w_+(x)=sigma+i tau, ell=4Theta'(x), and

    a_n=exp(t log(n)^2/4-sigma log n).

A unit multiplicative character means freely chosen chi(p) of modulus
one for each prime p<=N, extended completely multiplicatively. Set

    A_chi=sum_(n<=N) a_n chi(n),
    L_chi=sum_(n<=N) a_n log(n) chi(n),
    B_chi=ell A_chi+4i w_+'(x)L_chi,
    S_chi=ell A_chi-2L_chi.

Assume the following bounds for this same complete support and centre:

    |r(x)| < 101/10^8,           |r'(x)| < 71/10^7,
    |B_chi-S_chi| < 1/250000000000       for every unit character,
    M_32=sum_(n<=N) a_n |log(n/32)| < 81/4,
    ell-log N > 13,             0 < ell-2log32 < 25.

Finally assume the complete polynomial

    mathcal_F(z)=sum_(n<=N) a_n product_(p|n) z_p^(v_p(n))

has no zero on the closed unit polydisc, and |mathcal_F|>=1/790 on
its distinguished torus. These are model hypotheses, not assertions
about simplicity of H_t. Only the moment premise is independently
certified below; the remaining analytic bounds and these stability and
modulus premises stay assumptions.

## Conclusion

At the physical character chi(n)=n^(-i tau), abbreviate A=A_chi,
B=B_chi,S=S_chi, and set

    A_true=A+r/(2P),            B_true=B-2i r'/P.

Then, with all quantities evaluated at the centre,

    u=2 Re(P A_true),           u'=-Im(P B_true)/2,
    Re(conj(A_true) B_true)
      >107199260708819659/312050000000000000000000 >3/10^7.

Consequently (H_t(x),H_t'(x)) is not (0,0). Every zero at a centre
where the hypotheses hold is simple; this excludes every finite
spatial multiplicity >=2 there, not just multiplicity two.

The notebook normalization is F(lambda,z)=8H_(4lambda)(2z).
Thus the same conditional exclusion applies to (F,F_z) at
(lambda,z)=(t/4,x/2). It supplies no unconditional exclusion,
continuation to zero time, or all-degree mixed positivity for Xi.

## Proof

### Source, purpose and local convention

This is a checked reproduction of Michel Planat and Dale James Raymond,
*Certified Collision Exclusion and an Unconditional Upper Bound
Lambda<0.156821 for the de Bruijn–Newman Constant*,
[arXiv:2611.06245v1, 4 November 2026](https://arxiv.org/html/2611.06245v1#S3),
Corollary 3.2, Section 3.7 equations (19)–(20), Section 3.8 equation
(21), and Lemma 3.4 with the subsequent quadratic reserve calculation.
Theorem 3.1 supplies the source's asserted remainder/companion bounds;
Theorem 3.3 asserts its moment bound. They remain explicit hypotheses
here. No global theorem or certificate archive is imported as verified.

The prior assessment is
`drafts/literature/2026-11-10-conditional-hermitian-real-jet-admission-133.md`.
Repeating the source's conditional reasoning is justified by this
audit's specific tests: physical carrier differentiation, complete
support, wall conventions, and the small paid reserve in an unrefereed
claim. It is not claimed as new mathematics beyond that source.

L019 gives K(u)=4Phi(u/2). Substitution u=2v in L058's absolutely
convergent integral therefore gives

    F(lambda,z)=8 integral_0^infinity exp(4lambda v^2)Phi(v)cos(2zv)dv
               =8H_(4lambda)(2z),
    F_z(lambda,z)=16H'_(4lambda)(2z).

L058's compact domination justifies the substitution and derivative.
These nonzero constants preserve simultaneous vanishing and spatial
multiplicity. L059/L060 and L617 explain collision relevance only;
their splitting/potential statements are not premises of the admission
argument, and no regularization or event-atom assertion is invoked.

### The carrier derivative and lifted coordinates

At fixed t,N, differentiation of the finite A_+ sum gives
A_+'(x)=-w_+'(x)L_chi at the physical character. This differentiates
both the amplitude and physical phase through w_+, not a character
artificially held constant during spatial differentiation. From
P'=iTheta'P and ell=4Theta',

    B=4Theta'A_+(x)-4iA_+'(x),
    (PA_+)'=iPB/4.

Conjugation of the two local summands gives V=2Re(PA_+) on the real
interval. Differentiating there yields V'=-Im(PB)/2. Since r and r'
are real, adding the corrections gives precisely

    2Re(PA_true)=V+r=u,
    -Im(PB_true)/2=-Im(PB-2i r')/2=V'+r'=u'.

The correction is also compatible with the derivative companion. Put
A_tilde(z)=A_+(z)+r(z)/(2P(z)). At the centre,

    A_tilde'=A_+'+r'/(2P)-iTheta'r/(2P),
    4Theta'A_tilde-4iA_tilde'
       =B+2Theta'r/P-2i r'/P-2Theta'r/P
       =B-2i r'/P.

Thus no uncharged Theta'r term is dropped. For completeness,
(log M_t)'(s)=alpha(s)+t alpha(s)alpha'(s)/2, so the actual branch
definition gives Theta'(x)=Re(alpha+t alpha alpha'/2)/2.
There is no replacement of this derivative by a leading asymptotic.

### Weighted support from full polydisc stability

We check Lemma 3.4's argument, including possible degree cancellation.
Fix a unit character. For positive integers k choose positive integers
m_p(k) with m_p(k)/k tending to log p for each of the finitely many
primes p<=N, for example ceil(k log p). Substitute
z_p=chi(p)z^(m_p(k)) in mathcal_F, obtaining f_k(z). For |z|<=1
all substituted coordinates lie in the closed polydisc, so f_k has no
zero there. Moreover f_k(0)=a_1=1 and f_k(1)=A_chi is nonzero.

Write d_k=deg f_k. If d_k=0 its logarithmic derivative is zero.
Otherwise factor over its d_k roots rho, counted with multiplicity.
Each |rho|>1 and

    Re(1/(1-rho))=1/2+(1-|rho|^2)/(2|1-rho|^2)<1/2.

The logarithmic derivative formula at 1 consequently gives, in both
degree cases,

    Re(f_k'(1)/f_k(1)) <= d_k/2 <= D_k/2,
    D_k=max_(n<=N) sum_(p|n) v_p(n)m_p(k).

Cancellation of leading coefficients can only reduce d_k; it cannot
invalidate this upper bound. Since N is fixed and the support finite,

    f_k'(1)/(k f_k(1)) -> L_chi/A_chi,
    D_k/k -> max_(n<=N) log n=log N.

Taking this finite limit and multiplying by |A_chi|^2 proves

    Re(conj(A_chi)L_chi) <= (log N)|A_chi|^2/2.

Every prime variable and every natural-support term is accounted for;
stability of a smaller prime head alone would not license the argument.

### Complete scalar error payment

Write R=|A|>=1/790. The weighted inequality and ell-log N>13 give

    Re(conj(A)S) >= (ell-log N)R^2 > 13R^2.

Writing L_32=L_chi-(log32)A gives |L_32|<=M_32<81/4 and
S=(ell-2log32)A-2L_32. Hence |S|<25R+81/2. Define

    p=101/200000000,
    q=142/10000000+1/250000000000.

Since |P|=1, a=A_true-A and b=B_true-S satisfy |a|<p and |b|<q.
Expanding all four products, without assuming any signs of their
arguments, yields

    Re(conj(A+a)(S+b))
       >= Re(conj(A)S)-|a||S|-|A||b|-|a||b|
       > Q(R),
    Q(R)=13R^2-(25p+q)R-(81/2)p-pq.

In particular the constant cross term pq has been paid. Exact arithmetic
gives

    Q(1/790)=107199260708819659/312050000000000000000000,
    Q(1/790)-3/10^7=13584260708819659/312050000000000000000000>0,
    Q'(1/790)=649470206171/19750000000000>0,
    Q''=26.

Therefore Q is increasing on the entire required interval R>=1/790,
and the stated strict reserve follows even when the torus modulus
equals its allowed lower endpoint. Reproduction command:

    python3 scripts/heat/hermitian-admission-reserve-134.py

The exact certificate is `scripts/heat/hermitian-admission-reserve-134.json`.
Its seven checks pass; it records every separate error charge. This is
an arithmetic verification of the displayed conditional inequality,
not evidence for the analytic estimates or stable-polynomial premise.

### Simultaneous vanishing and closed walls

If u=u'=0, then PA_true is purely imaginary and PB_true is real.
Their Hermitian product has zero real part. As |P|=1 this is exactly
Re(conj(A_true)B_true)=0, contradicting the strict reserve. Also
H_t=Gu and H_t'=G'u+Gu'. Since G(x)>0, simultaneous vanishing of
(H_t,H_t') is equivalent to simultaneous vanishing of (u,u').

At an exact wall the right index N=j is used throughout the finite
sum, polynomial, moment and remainder. That local remainder is
r_N=H_t/G-(PA_(+,N)+P^(-1)A_(-,N)), an analytic function for the
frozen N. The assumed bound on r_N' is for this function on a full
neighbourhood, not a one-sided derivative of a moving-index formula.
Every preceding equality is consequently valid at the wall itself.
No agreement of the auxiliary coordinates chosen at adjacent centres
is needed for this pointwise implication. Deriving uniform bounds on
r_N' through support crossings, or transporting model stability
between centres, remains separate work; pointwise conditional validity
does not establish those premises.

This concludes only the cited admission implication. Finite-height
initialization, stationary boundary, source recovery across changing
support, the infinite exterior, global continuation, zero time and
the L030–L032/C032a signs remain unresolved. The positive reserve
does not imply a positive lower bound for H_t alone. No candidate
solution of RH is produced.

### Partial independent audit of the moment premise (step136)

This subsection checks the analytic reduction of Planat–Raymond v1,
Theorem 3.3, Section 3.8.1, using the exact rectangle and complete
support in the hypotheses above. At step136 it did **not** discharge
M_32<81/4: the directed numerical inequalities had not been replayed.
The step140 specialization and complete rational replay below now supply
this finite input; the original Arb branch remains unexecuted.
The prior coverage is
`drafts/literature/2026-11-10-centred-moment-independent-audit-135.md`.
An independent reconstruction is justified by the source's unrefereed
computer-assisted status; this is reproduction, not a novelty claim.

Write a=98/625, T=1/5, C=690988, H=3100000, K=128,
kappa=log32 and W=120000000000000. At s=(1+ix)/2,

    Re(1/(2s)+1/(s-1))=-1/(1+x^2),
    Re((1/2)Log(s/(2pi)))=(1/2)log(sqrt(1+x^2)/(4pi)).

Consequently sigma=1/2+t*c(x), where c=c_pol in the source, and

    c'(x)=x/(4(1+x^2))+x/(1+x^2)^2>0  (x>0).

Assume first the two unverified wall inequalities

    X/(4pi)+a/16>C^2,
    (H+1)^2>W/(4pi)+T/16.

Monotonicity of the square root gives C<=N<=H throughout the closed
rectangle. In particular at an exact wall the floor selects N=j,
with no excluded equality case. Starting at C, the exact recurrence
e_(j+1)=min(H,floor(101*e_j/100)) terminates at H and yields 151
adjacent closed leaves [L,U]. The integer certificate named below
verifies these endpoints and their strict ordering; adjacency covers
every integer from C through H, with shared endpoints allowed.

On such a leaf use x_L=X for L=C, otherwise
x_L=4pi(L^2-T/16). For N>=L the definition of the floor implies
x>=4pi(N^2-t/16)>=4pi(L^2-T/16), including equality. The first leaf
uses the original x>=X instead. Suppose the still-unverified leaf
gates give x_L>=X and log U<4c(x_L). For 1<=n<=N<=U put u=log n.
Then u>=0 and u(u/4-c(x))<=0. Thus, since t>=a and c(x)>=c(x_L),

    t*u^2/4-(1/2+t*c(x))*u
       <= a*u^2/4-(1/2+a*c(x))*u
       <= a*u^2/4-sigma_L*u,   sigma_L=1/2+a*c(x_L).

At n=1 both exponents are zero. Multiplication by |log(n/32)|
preserves the comparison, and at n=32 that factor is exactly zero.
No term of the natural support has been removed.

For v>=K let f(v)=(log v-kappa)exp(a*log(v)^2/4-sigma_L*log v).
It is positive since K>32. With u=log v, direct differentiation gives

    f'(v)=exp(a*u^2/4-sigma_L*u)/v * g(u),
    g(u)=1+(u-kappa)(a*u/2-sigma_L),   g''(u)=a>0.

If the two unverified endpoint gates g(log K)<0 and g(log U)<0
hold, convexity places g below its negative endpoint chord on the
whole closed interval. Hence f strictly decreases there. Since
N>=C>K, integrating on each [n-1,n] gives

    sum_(n=K+1)^N f(n) < integral_K^N f(v)dv <= integral_K^U f(v)dv.

Together with the complete K-term prefix, this bounds the entire
moment by the displayed prefix plus integral. Extending the positive
envelope from N to U is legitimate; no physical coefficient beyond
N is asserted to belong to the actual polynomial.

The antiderivative can be checked without numerical evidence. Put
B=sigma_L-1, E(u)=exp(a*u^2/4-B*u), and define

    A(u)=sqrt(pi/a)*exp(-B^2/a)*erfi((a*u/2-B)/sqrt(a)),
    erfi(z)=(2/sqrt(pi))*integral_0^z exp(q^2)dq.

The fundamental theorem of calculus and the chain rule give
A'(u)=E(u): the prefactors multiply to one and
(a*u/2-B)^2/a-B^2/a=a*u^2/4-B*u. Let
I=A(log U)-A(log K). Substituting v=exp u yields

    integral_K^U f(v)dv = integral_(log K)^(log U) (u-kappa)E(u)du,
    E'(u)=(a*u/2-B)E(u),
    J=integral_(log K)^(log U) u*E(u)du
      =2/a*(E(log U)-E(log K)+B*I),
    integral_K^U f(v)dv = J-kappa*I.

This verifies the source's signs, scaling and B convention. No
quadrature or unsigned replacement of the integral is used. The
remaining obligations are directed enclosures for both walls and
every leaf gate, including the complete prefix plus this exact
integral being strictly less than 81/4 on every leaf. The auxiliary
I>0 and tail>0 gates also need execution, even though the integrands
are analytically positive.

The independent reconstruction and its full current certificate are
`scripts/centred-moment/independent_audit_136.py` and
`scripts/centred-moment/independent-audit-136.json`. Reproduction:

    python3 scripts/centred-moment/independent_audit_136.py --bits 192

Its actual step136 run checks the exact 151-leaf cover and all 914
gate names, but only five exact global gates execute: the other
909 gates remain unexecuted because importing flint fails. Installing
python-flint 0.9.0 in an isolated Python 3.12 environment also failed
DNS; narrow local wheel/cache checks found no package. Therefore no
Arb enclosure, numerical maximum, moment bound or source-byte hash was
certified by step136. The unexecuted Arb branch is saved for continuation, not
validated code. It is intended to compare each leaf and the maximum
of outward upper endpoints, avoiding midpoint ordering. A working
Arb runtime is still essential to executing that original branch; the
independent rational method below removes that dependency for this bound.

### Rational finite-error specialization (step140)

This is REPRODUCTION under the unchanged step138 SPECIALIZE assessment,
separately reviewed in step139. The script is
`scripts/centred-moment/rational_replay_140.py`; its certificate is
`scripts/centred-moment/rational-replay-140.json`. The standard inputs are
Daumas–Lester–Munoz, *Verified Real Number Calculations: A Library for
Interval Arithmetic*, [arXiv:0708.3721v1](https://arxiv.org/html/0708.3721),
Section III, Propositions9/10/12;
[NIST DLMF 3.1(ii–iii)](https://dlmf.nist.gov/3.1#ii) for outward operations;
[DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4),
[4.2.19](https://dlmf.nist.gov/4.2.E19),
[4.24.3](https://dlmf.nist.gov/4.24.E3) for elementary series; and
[DLMF 3.5.6–8](https://dlmf.nist.gov/3.5#ii), citing Davis–Rabinowitz,
*Methods of Numerical Integration*,1984,pp.57–58, for composite Simpson.
These license methods, not an unchecked Python port. Independent
specialization is justified by the source's unrefereed numerical status.
The finite-error and implementation correspondence are as follows.

**Included operations.** Write Q=2^256. Stored integers (l,h) represent
[l/Q,h/Q]. Rational p/d, d>0, is enclosed by floor(pQ/d),ceil(pQ/d),
using exact integers. Addition and negation use exact endpoints.
Multiplication takes the minimum/maximum of all four endpoint integer
products and rounds after division by Q. Bilinearity on a rectangle
proves inclusion for every sign. Reciprocal reverses endpoints and is
allowed only if zero is excluded, using exact rational reciprocals before
rounding. Division is included multiplication by this reciprocal; negative
endpoint denominators are normalized by Fraction. Powers use repeated
included multiplication. For sqrt on [l/Q,h/Q], l>=0, integer endpoints
are floor(sqrt(lQ)) and ceil(sqrt(hQ)); integer `isqrt` and a final exact
square comparison give them. No floating input or overflow-limited
integer arithmetic is used. These observations prove inclusion after
every operation, rather than assuming an aggregate machine-error bound.

**Finite elementary series.** For exact rational x>0 write x=2^k m,
1<=m<2, by exact comparisons. Permit m=2 separately to compute log2.
For z=(m-1)/(m+1), 0<=z<=1/3, the cited series and geometric comparison
of its positive omitted terms give

    log m=2 sum_(j=0)^99 z^(2j+1)/(2j+1)+R,
    0<=R<=2z^201/(201(1-z^2)).

Every omitted denominator is >=201, and 1-z^2>=8/9. The script initializes
term=z and multiplies by z^2 after each of100 summands; the terminal term
encloses z^201. It takes the lower partial-sum endpoint and the upper
endpoint after adding the remainder. Adding k times the independently
enclosed log2 is included even for k<0. Monotonicity extends this to
positive interval inputs. In particular log1=0 exactly.

For exact x>=0 choose x=2^r t, 0<=t<=1/8, by repeated halving. The cited
factorial series gives

    exp t=sum_(j=0)^79 t^j/j!+R,
    0<=R<=(t^80/80!)/(1-t/81).

Successive omitted-term ratios are <=t/81 and the divisor is
>=647/648>0. The script's included term recurrence encloses each term,
finite sum and remainder. The lower sum endpoint is positive since its
constant is1. Repeated squaring encloses exp x. For x<0 reciprocate the
positive enclosure of exp(-x); monotonicity handles interval inputs.

Pi uses the named Machin identity pi=16atan(1/5)-4atan(1/239).
By the cited atan series and the alternating-series remainder theorem,
each value lies between its exact rational m-term sum and that sum plus
the next signed term; m=120 and40 respectively. Included subtraction
reverses the second atan's endpoints as required. No decimal pi is used.

**Variable endpoints and Simpson error.** Let l=log K, h=log U,
w=h-l>0, q(u)=a*u^2/4-B*u and E=exp q with the leaf's exact parameters.
Set u(s)=l+ws for s in[0,1]. The transformed integrands are wE(u(s))
and w(u(s)-kappa)E(u(s)); both are C^infinity on this closed interval.
All uncertain parameter and endpoint enclosures are propagated by
inclusion; no independence of their errors is required. Put d=a/2 and
r(u)=a*u/2-B. Product differentiation, starting with E'=rE and
E''=(r^2+d)E, gives

    E'''=(r^3+3dr)E,
    E''''=(r^4+6dr^2+3d^2)E,
    ((u-kappa)E)''''=
        ((u-kappa)(r^4+6dr^2+3d^2)+4(r^3+3dr))E.

Enclose u on [lower(l),upper(h)]. Let R bound |r| and M bound |u-kappa|
on that interval. Since q''=a/2>0, the maximum on the exact integration
interval is at an endpoint. Thus the maximum of upper interval
evaluations of exp(q(l)) and exp(q(h)) supplies Emax. Nonnegative bounds
for the two fourth derivatives in u are

    A_I=Emax*(R^4+6dR^2+3d^2),
    A_tail=Emax*(M*(R^4+6dR^2+3d^2)+4*(R^3+3dR)).

All bound expressions are themselves rounded outward; their upper
endpoints apply uniformly to every exact parameter choice. The chain
rule multiplies the fourth derivatives in s by w^5. Composite Simpson
on[0,1] with even m=4096 therefore has errors at most

    w^5*A_I/(180m^4),   w^5*A_tail/(180m^4).

The script subtracts/adds each error's upper endpoint from/to the
quadrature's lower/upper endpoints. This charges uncertain endpoints,
rounding and quadrature error together. Both I>0 and tail>0 are tested
from the resulting closed intervals. No erfi cancellation is evaluated.

To avoid separate exponentials at600000 nodes, put delta=w/m and
u_i=l+i*delta. Expanding q's quadratic gives the exact recurrences

    E_0=exp(q(l)),
    rho_0=exp(r(l)*delta+a*delta^2/4),
    eta=exp(a*delta^2/2),
    E_(i+1)=E_i*rho_i,   rho_(i+1)=rho_i*eta.

Interval induction encloses every node even with correlated parameters.
Simpson's weights are1 at endpoints,4 at odd indices and2 at interior
even indices; multiply their included sum by w/(3m). The certificate
retains a direct final endpoint exponential and the recurrence endpoint.
Their overlap is an implementation check, not the proof of the induction.

**Gate semantics.** All eight global and six-per-leaf original gates
are retained, giving914. Both natural-index walls use strict margins.
The first x_L=X position gate accepts its exact equality; later position
gates use positive margins. The log32 gate takes the minimum of the two
margins log32-3 and7/2-log32. The integral gate takes the minimum of the
separate I and tail enclosures, both also saved. For a strict margin,
positive lower endpoint passes; nonpositive upper endpoint is definite
failure; spanning zero is inconclusive. Neither missing nor inconclusive
gates pass. The prefix includes n=1 through128, with the n=32 summand
exactly zero and the two remaining absolute-log cases checked positive.
No new arithmetic/error check replaces an original gate.

A uniform moment conclusion requires all151 closed leaves, all914 gates
and the maximum of every outward upper endpoint <81/4. Partial runs keep
the completed-leaf maximum separate and the uniform bound unset. The
certificate saves exact constants, endpoints, errors, individual leaf
bounds, failures and the maximum if complete. The inclusion proof above
is informal and does not claim formal verification of the Python port.
Full Mathlib coverage is unchecked; all independent analytic, stability,
global and zero-time premises remain open.

**Executed result and qualifications (step140).** The initial 256-bit,
4096-subinterval run completed in about21 seconds. All914 original gates
passed, with zero failed, inconclusive or unpaid gates; all151 closed
leaves were included. The maximum outward upper endpoint occurs on leaf1,
[L,U]=[690988,697897], and equals

    2340604918293025570185271056201132701237504700764076737479746791105994795136734
    /2^256 < 20213859/1000000 <81/4.

The preceding reduction and the included series/quadrature calculations
therefore reproduce the complete-support bound, throughout the exact
rectangle and at both wall conventions,

    M_32 <20213859/1000000 <81/4.

This is a local reproduction of Planat–Raymond v1 Theorem3.3, not progress
beyond its stated conclusion. It discharges only this scalar moment
premise of the conditional admission argument; its other hypotheses are
not established. The redundant explicit moment hypothesis in the initial
conditional statement is retained to preserve the original implication.

Reproduction and complete stored-evidence inspection commands:

    python3 scripts/centred-moment/rational_replay_140.py --seconds 55
    python3 scripts/centred-moment/inspect_certificate_140.py

The second command reads every stored leaf, original margin, error charge
and recurrence-endpoint comparison with exact integer arithmetic, checks
the entire endpoint recurrence, verifies prefix+tail and all cap comparisons,
and recomputes the maximum over all151 upper endpoints. Its report is
`scripts/centred-moment/rational-inspection-140.json`, with evaluator and
certificate SHA256 values. It passed. This checks complete recorded
evidence, not just a preview or the evaluator's PASS string; it does not
independently recompute transcendental values or formally verify Python.
The full maximum-leaf certificate (including both derivative errors),
constants, both wall margins and arithmetic checks were also inspected.
The independent conceptual audit below now checks the
correlated-endpoint recurrence and finite error specialization.

An initial version of this inspection helper guessed the unnecessary
stronger display bound20.2137 and failed that assertion. Its full report
is preserved as `scripts/centred-moment/rational-inspection-first-140.json`.
The helper now computes a display ceiling by exact integer arithmetic;
none of the original914 inequalities, quadrature values, error bounds or
main replay certificate changed. This helper failure is not a failure of
the required81/4 inequality and is not suppressed.

### Independent conceptual audit of the moment certificate (step142)

**Scope and conclusion.** Under the exact rectangle, complete support and
right-index convention of the step136 reduction, the step140 proof and
its entire stored certificate survive this audit. Thus the moment premise
is discharged locally with the same bound M_32<20213859/1000000<81/4.
This is a checked reproduction of Planat–Raymond v1 Theorem3.3, not a new
result beyond that source and not verification of any other hypothesis
of this lemma. The approved assessment is
`drafts/literature/2026-11-10-centred-moment-rational-audit-140.md`.
It reuses the precise standard-input citations in step140; no new
theorem or changed domain is imported.

**Original implementation scrutiny.** All integer endpoint operations in
`rational_replay_140.py` were read against the proof. For an interval
[l/Q,h/Q] not containing zero, 1/y decreases on its entire positive or
negative branch, so its endpoint bounds are Q/h and Q/l. The exact
Fraction conversion and subsequent rounding therefore handle negative
divisors as well as positive ones. The four-product multiplication rule
also covers intervals crossing zero; repeated multiplication need not be
sharp to retain inclusion. The square-root endpoints satisfy the exact
squared inequalities by `isqrt`, including zero and perfect squares.

The logarithm loop sums precisely powers1,3,...,199 and exits with
power201. Its remainder denominator201 and factor1-z^2 are correct.
Range reduction handles both signs of the integer exponent of2; the
interval endpoint extension uses monotonicity only on positive inputs.
The exponential loop retains degrees0,...,79, then computes degree80;
the ratio of successive omitted terms is at most t/81. All these
divisors are positive in their stated reduced domains. Directed rounding
of z or t may widen those intervals, but still encloses each exact
series/remainder expression; the code forbids any divisor spanning zero.
The constant term ensures a positive exponential enclosure before
reciprocation. Machin's two even truncation counts give a lower partial
sum and upper next-term sum; subtraction of the second atan reverses its
endpoints. Neither the original self-checks nor overlapping final
exponentials are being used to prove these facts.

**Dependence and quadrature.** Fix one exact tuple (a,B,kappa,l,h)
inside its computed intervals, and put delta=(h-l)/4096. For this same
tuple at every node, the displayed E and rho recurrences are exact
quadratic identities. Interval induction includes the tuple's values
regardless of dependencies between l, h, B and their intermediate
expressions. Reusing a wider interval cannot remove that exact tuple.
The interval for u contains the entire exact closed integration interval;
R and M are actual upper bounds for the two absolute values on it.
Convexity applies to the exact q, so its endpoint upper evaluations
bound exp(q) throughout, even when those endpoints are uncertain.
Differentiating E and (u-kappa)E four times gives exactly the two
displayed derivative polynomials. After the affine substitution, the
outside width and four derivatives contribute width^5, not width^4.
The even4096 mesh and real smooth integrands satisfy the cited Simpson
hypotheses. Adding and subtracting each error's upper endpoint therefore
encloses the exact integral uniformly. No independence, unsigned
cancellation, ignored endpoint interval or uncharged derivative is used.

The analytic reduction was also checked: c'(x)>0 on the rectangle;
the lower/upper natural walls imply C<=N<=H even at equality; the first
leaf uses x_L=X exactly; and subsequent leaves use the consequence of
N>=L with t<=T. The exponent comparison uses t>=a only after proving
u(u/4-c(x))<=0. The complete prefix retains n=1 and all terms through128,
with n=32 exactly zero. The convex g's two negative endpoints imply a
strictly decreasing positive tail, so the sum-to-integral comparison is
valid on every included closed leaf. None of these statements assumes
the moment bound or any stability hypothesis of the conditional consumer.

**Independent discriminating computation.** The standalone auditor
`scripts/centred-moment/audit_certificate_142.py` imports neither original
evaluator nor acceptance helper. It rebuilds every prefix coefficient, gate,
quadrature node, derivative bound and charged error using320-bit dyadic
intervals and longer versions of the same elementary series. It compares
them to all151 original leaf records; the retained theorem bound is the
original256-bit bound, not a proposed stronger estimate or new method.
Its log truncation has120 terms and tail
2z^241/(241(1-z^2)); its exp truncation has degrees0,...,95 and tail
(t^96/96!)/(1-t/97). The geometric arguments above apply unchanged.
Machin uses160 and48 terms with the same alternating remainder proof.

For a different implementation of the same node identities, the auditor
uses separate even and odd sequences. At u_i=l+i*delta it initializes
each parity's exponential directly and uses

    E_(i+2)=E_i R_i,
    R_i=exp(2delta*(a*u_i/2-B)+a*delta^2),
    R_(i+2)=R_i exp(2a*delta^2).

Expanding q(u_i+2delta)-q(u_i) verifies the first ratio; incrementing
u_i by2delta verifies the second. These identities and inclusion prove
both parity inductions, including the final even endpoint. Their weights
give the same complete Simpson rule. Thus this check does not merely
repeat the original one-step loop or trust its saved terminal overlap.

All320-bit interval recomputations are contained in their corresponding
stored256-bit enclosures, except the two precision-dependent singleton
upper bounds R and M, for which the appropriate comparison is that the
stored upper bound dominates the recomputed one. Every original error
charge and prefix-plus-tail sum also passes an exact endpoint identity
check. All914 original gate names and their positive margins/exact
predicates pass. The entire151-leaf recurrence, each original cap
comparison and the maximum over all original upper endpoints were
recomputed. The certificate contains all128 prefix terms for each leaf,
the full quadrature/error records, exact checks, source/script hashes and
an empty failure list. It reports32050 passing checks and maximum leaf1.

Reproduction, writing a separate certificate and preserving step140:

    python3 scripts/centred-moment/audit_certificate_142.py

Full evidence: `scripts/centred-moment/conceptual-audit-142.json`.
All records were processed, not inferred from a preview; both wall
margins, the maximal leaf's complete values/errors and the final leaf
margin were also inspected in full. The original maximum remains the
exact numerator over2^256 displayed in step140, strictly below
20213859/1000000; the required threshold is81/4. No original evaluator,
certificate or first failed display-helper report was overwritten.

This is an informal mathematical/code audit with an independent
implementation check, not a formally verified Python runtime. The
analytic remainder and derivative, companion and phase/support,
complete-polydisc stability/modulus, initialization/recovery, seams,
exterior, zero-time and all-degree mixed-positivity obligations remain
open. The original Arb branch remains parked. The scalar replay/audit
task is now complete; further repetition requires new contrary evidence.

## Mathlib

Full matching coverage and supporting theorem names have not been
checked; availability is unknown. This audit uses elementary complex
polynomial factorization, finite differentiation, a finite limit and
rational inequalities. No Mathlib formalization or certificate replay
of the upstream analytic hypotheses is claimed. Full Mathlib coverage
of the partial moment reduction, erfi evaluation and finite certificate
is likewise not checked.
