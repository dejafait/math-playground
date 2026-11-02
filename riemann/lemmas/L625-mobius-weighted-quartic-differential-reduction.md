# Lemma 625: weighted quartic reduction and the unresolved amplifier cost

## Hypotheses

Use L622's actual functions and parameter conventions:

    A(t)=(t^2+1/4) pi^(-1/4)|Gamma(1/4+it/2)|/2,
    Z(t)=-Xi(t)/A(t),
    W(t)=(Xi'(t)^2-Xi(t)Xi''(t))/A(t)^2,
    L=log T, T<=X<=2T, v(t)=w((t-X)/T),
    w in C_c^infinity((0,1)), w>=0, integral w=1.

Take T sufficiently large, and keep the raw amplifier from L624
Section 5:

    N=floor(T^(1/100)), m_N^2=sum_(n<=N) mu(n)^2/n,
    a_n=mu(n)/(sqrt(n) m_N),
    M(t)=sum_(n<=N) a_n n^(-it),
    U(t)=c0 Z(t)+c1 Z'(t)/L, c0,c1 real, c0^2+c1^2=1.

Every height derivative below holds T,X,N,m_N,c0,c1,L fixed.
In particular no derivative changes the cutoff. Set rho=v|M|^2,
f=Z, b=c1/L and a=log A. Integrals are over the real line with
compact support in [X,X+T]; the identities need f only on that
interval. L471 (7) gives W=f'^2-ff''-a''f^2, including at zeros.

For the quantitative absolute bounds, use L619's audited H=T
complex-shift and fourth-moment application (delta=1/26,
sigma=1/88), and L471's completion-curvature bound. The named
arithmetic input is C. P. Hughes and M. P. Young, *The twisted
fourth moment of the Riemann zeta function*, J. reine angew. Math.
641 (2010), 203–236, [arXiv:0709.2345v2, Theorem 1.1/(11)–(17),
printed pp. 3–5](https://arxiv.org/pdf/0709.2345v2#page=3), including
the complete-sum holomorphy remark on p. 5. L619's source application
is reused; its arithmetic/holomorphy manuscript proofs are not
independently audited here. L622's complete transfer is also retained
with its unaudited qualification. No source asymptotic for a tapered
mollifier, no RH, no zero-spacing assumption and no relative
amplifier-derivative estimate is imposed.

## Conclusion

The following identity is exact:

    I_c := integral rho W U^2 = B_c+R_c-C_c,               (1)
    B_c = integral rho [(2c0 f f'+b f'^2)^2
                                      +(b^2/3) f'^4],
    R_c = integral rho' H_c,
    H_c = c0^2 f^3 f'+c0 b f^2 f'^2+(b^2/3)f f'^3,
    C_c = integral rho a'' f^2 U^2.

Thus B_c>=0 for every common real observer. Every generated
amplifier and weight derivative is retained in

    rho'=v'|M|^2+2v Re(M' conjugate(M)),
    M'=sum_(n<=N) (-i log n) a_n n^(-it).                 (2)

Writing R_c=R_c^w+R_c^M according to (2), the available uniform
absolute bounds are

    |R_c^w|/(T L^6) <= C_w N/(T L),
    |C_c|/(T L^6) <= C_w N/(T^2 L^2).                   (3)

The first bound is o(T^(-17/80)/L^4); the second is at most
C_w T^(-199/100)/L^2. These statements concern absolute costs,
not their ratios to B_c. They do not dispose of R_c^M.

The first uncontrolled relative cost is explicit already at c=(1,0).
Set

    P=integral v |M|^2 f^2 f'^2,
    D=integral v |M'|^2 f^4,
    S=integral v' |M|^2 f^3 f'.

Then

    I_(1,0) >= 4P-2 sqrt(PD)-|S|-|C_(1,0)|.             (4)

Let E_w(T)=C_w[T^(-17/80)/L^4+T^(-199/100)/L^2] denote
L622's full absolute transfer bound, with its appropriate constant.
For P>0 the sufficient scalar test for I_(1,0)/(T L^6)>E_w(T) is

    4-2 sqrt(D/P)
       > [|S|+|C_(1,0)|+T L^6 E_w(T)]/P.                (5)

In particular this particular lower-bound test needs D/P<4;
that inequality alone would still be insufficient without a margin
and a quantitative size for P. Failure of (5) would not imply a
negative integral. The only bounds established here are

    0<=P<=C_w N T L^6,
    0<=D<=C_w N (log N)^2 T L^4
                         <=C_w N T L^6/10000.           (6)

No lower bound for P, upper bound for D/P, uniform positive margin,
negative witness or actual-Xi sign conclusion is obtained. This is
a known-calculus reduction for the approved bounded test, not a new
arithmetic theorem or progress beyond the sources checked. Its
canonical calculation has not had a separate critical audit.

The second bounded attempt in Section 5 extracts both correlated
moments from L622's complete source expression, with the derivative
coefficient norm included in its error. It also gives the linear
sufficient test (13). No uniform lower bound for that complete
expression is obtained; this refinement ends inconclusively too.

## Proof

### 1. All observer derivatives and the positive bulk

The elementary inputs are integration by parts for continuously
differentiable functions on a compact interval and the product rule.
Their explicit application is needed to determine every coefficient
and cost for this observable; no moment theorem is reproved. Smooth
compact support makes all boundary products below vanish. Expanding
U^2, denote the three unnormalized observer entries by

    J00=integral rho (f'^2-ff'') f^2,
    J01=integral rho (f'^2-ff'') f f',
    J11=integral rho (f'^2-ff'') f'^2.

The three product identities are

    (f^3 f')'=3 f^2 f'^2+f^3 f'',
    (f^2 f'^2)'=2f f'^3+2 f^2 f' f'',
    (f f'^3)'=f'^4+3f f'^2 f''.

Multiply each by rho and integrate. They give, respectively,

    J00=4 integral rho f^2 f'^2+integral rho' f^3 f',
    J01=2 integral rho f f'^3+(1/2)integral rho' f^2 f'^2,
    J11=(4/3)integral rho f'^4+(1/3)integral rho' f f'^3.

Consequently c0^2 J00+2c0 b J01+b^2 J11 has derivative cost
R_c and bulk

    integral rho [4c0^2 f^2 f'^2+4c0 b f f'^3
                                             +(4b^2/3)f'^4].

This is exactly B_c in (1). Thus the f'' terms generated by the
derivative observer were included before the integrations, rather
than treating U as a constant. L471's zero-safe identity subtracts
precisely C_c, proving (1).

For completeness the bulk quadratic 4x^2+4xy+(4/3)y^2,
with x=c0 f f', y=b f'^2, satisfies

    4x^2+4xy+(4/3)y^2-(x^2+y^2)/4
        =(15/4)(x+8y/15)^2+y^2/60 >=0.

Hence the bulk is positive semidefinite uniformly in the observer,
but a quantitative integrated lower bound does not follow just from
this pointwise algebra. Zeros of f or M cause no division or exception.

### 2. Weight derivatives and the alternate second-derivative form

The finite sum M is smooth and differentiates term by term, giving
(2). If the c0^2 cost is integrated once more, its exact alternate
form is

    c0^2 integral rho' f^3 f'=-(c0^2/4)integral rho'' f^4,
    rho''=v''|M|^2+4v' Re(M' conjugate(M))
                    +2v[|M'|^2+Re(M'' conjugate(M))],
    M''=-sum_(n<=N)(log n)^2 a_n n^(-it).                (7)

Here v'=T^(-1)w'((t-X)/T) and
v''=T^(-2)w''((t-X)/T). Formula (7) is equivalent to the
first-derivative form; it does not allow either |M'|^2 or the M''
term to be dropped or assigned a combined sign. The proof uses
neither M'/M nor derivatives of a fractional power of w.

### 3. Absolute window and completion costs

The n=1 term gives m_N>=1 and the coefficient norm is exactly 1.
Finite Cauchy--Schwarz therefore gives

    |M|^2<=N,  |M'|^2<=N (log N)^2.                     (8)

Choose once a nonnegative smooth bump eta compactly supported in
(0,1) and dominating |w'|. Such a bump exists since the support
of w' is compact in that interval; multiplying a bump equal to 1
near that support by a fixed large constant suffices. Rescale eta
by its integral when applying L619. Its H=T complex-shift bound,
followed by the fixed Cauchy derivative in each of four distinct
variables, gives, uniformly in X,

    integral eta((t-X)/T) |f|^4 <= C_w T L^4,
    integral eta((t-X)/T) |f'/L|^4 <= C_w T L^4.          (9)

Indeed L619's normalized integral Fcal is bounded on the fixed
complex polydisc; partial_1 partial_2 partial_3 partial_4 Fcal(0)
is exactly the second integral divided by T L^4. The derivative
has fixed unit-circle Cauchy cost. The same statements hold with
eta replaced by w. Nonnegativity permits Holder to bound all the
mixed absolute fourth products of f and f'/L by C_w T L^4.
This is a specialization of the audited local germ, with the same
named source imports, not an amplifier-weight source application.

Each of the three monomials in H_c is L times a mixed fourth
product of f and f'/L, with uniformly bounded observer coefficients.
Equations (8)-(9) and |v'|<=eta((t-X)/T)/T give
|R_c^w|<=C_w N L^5. This proves the first bound in (3), and

    [N/(T L)]/[T^(-17/80)/L^4]
       <= T^(-311/400) L^3 -> 0.

For the completion use |a''|<=C/T^2 from L471 and the audited
L619 bound integral v f^2 U^2<=C_w T L^4. Equation (8) gives
|C_c|<=C_w N L^4/T, proving the second part of (3).
No lower bound for w, M, f, U or B_c is used. Different occurrences
of C_w can denote different finite constants; no effective onset
or finite-height certification is inferred.

### 4. The first scalar cost and the stopping decision

At c=(1,0), (1)-(2) read exactly

    I_(1,0)=4P+S+2 Re integral v M' conjugate(M) f^3 f'
                                                   -C_(1,0).

Cauchy--Schwarz in the measure v(t)dt, applied to the absolute
factors |M f f'| and |M' f^2|, bounds the middle amplifier term
in absolute value by 2 sqrt(PD). This proves (4); dividing it by
P>0 yields the sufficient test (5), without claiming necessity for
the actual sign. The definitions and (8)-(9), now using w, imply
(6) by Holder. Finally log N<=L/100 gives its last inequality.

These absolute upper bounds have no positive lower counterpart for
P. Comparing two upper bounds does not compare D/P. The coefficient
inequality sum |(-i log n)a_n|^2<=(log N)^2 is an unweighted
coefficient estimate; it cannot simply be substituted as a relative
norm estimate in the varying measure v Z^4 dt. Likewise it supplies
no comparison between Z^4 and Z^2 Z'^2 correlated with this M.
No such implication is asserted or assumed for the actual amplifier.

The bounded physical test stops at this first uncontrolled cost.
It neither rules out an arithmetic estimate of P,D nor rules out
cancellation in the signed amplifier term. A later continuation
would have to estimate these actual correlated moments, with checked
coefficient rescaling and uniform error, before attempting the full
common-observer bound. It must also treat the other observer entries.
The earlier row/freezing/raw-boundary failures are not reopened.
Pointwise initial signs and all-degree mixed positivity remain open.

### 5. Correlated-moment refinement and the linear sufficient test

Retain the hypotheses and the full H_hk(b) of L622 Section 1. In
particular H_hk includes all six permutations, the exact analytic
Hardy phase inside the integral, and the factor 1/sqrt(hk). For any
fixed complex vector x of length N, define

    F_x(b)=integral v |M_x|^2 product_(j=1)^4 f(t+b_j/L) dt/(T L^4),
    M_x(t)=sum_(n<=N) x_n n^(-it),
    H_x(b)=sum_(m,n<=N) x_m conjugate(x_n)
                           H_(m/g,n/g)(b),  g=gcd(m,n).

The vector is held fixed in b. L622 (9)-(11), before its signed
extraction, supplies one finite C_w such that

    sup_(|b_j|<=2) |F_x(b)-H_x(b)| <= ||x||_2^2 eta_T,
    eta_T=C_w T^(-17/80)/L^4.                            (10)

This statement retains L622's unaudited application and named-source
qualifications. Its extension from unit x is justified by homogeneity:
both expressions are multiplied by ||x||_2^2 on replacing a unit
vector by x. For x=0 both vanish. More directly, its absolute error
sum is bounded by

    (sum |x_n| n^(7/8))^2 <= ||x||_2^2 N^(11/4).

There is no moment theorem for a varying weight |M_x|^2 being assumed:
this is the finite sum of admissible twists. Each error is holomorphic
on the stated polydisc by L622 Section 3. Consequently its mixed
derivative partial_1 partial_2 at zero costs at most the right side
of (10), by the unit-circle Cauchy formula; both factorials are 1.
Real parts below refer only to the final values of the complete
holomorphic functions, not to individual pole terms.

For the actual raw vector a put

    d_n=(log n/L)a_n,
    sigma_T^2=||d||_2^2
      =sum_(n<=N) mu(n)^2 (log n)^2/(n m_N^2 L^2)
      <= (log N/L)^2 <= 1/10000,
    p=Re (partial_1 partial_2 H_a)(0),
    q=Re H_d(0).

Here d is a new coefficient vector for evaluating a moment, not a
change of the amplifier in the signed integral. The exact identity
M'=-i L M_d and differentiation of two distinct Hardy factors give

    |P/(T L^6)-p| <= eta_T,
    |D/(T L^6)-q| <= sigma_T^2 eta_T.                    (11)

For the first equality the two height derivatives each contribute
L^(-1) before setting b=0. For the second, |M'|^2=L^2 |M_d|^2;
this L^2 cancels the difference between the fourth-moment and the
sixth-log normalization. Thus no additional L^2 belongs on the
normalized error in (11). If d=0 the second moment and its error
are exactly zero. The curvature cost is not part of either of
these two Hardy moments; it is retained separately as C_(1,0).

Write F=4p-q and r_T=(|S|+|C_(1,0)|)/(T L^6). Then (11) gives

    |(4P-D)/(T L^6)-F| <= (4+sigma_T^2) eta_T.           (12)

For nonnegative P,D, the elementary square
(sqrt(2P)-sqrt(D/2))^2>=0 proves
2sqrt(PD)<=2P+D/2. Applying this to (4) proves, without division
by P or any pointwise function,

    I_(1,0)/(T L^6)
      >= (F-(4+sigma_T^2)eta_T)/2-r_T.

In particular, a sufficient condition for the required scalar margin
I_(1,0)/(T L^6)>E_w(T) is

    F > (4+sigma_T^2)eta_T+2r_T+2E_w(T).                (13)

This is sufficient, not necessary. It is a slightly stronger test
than retaining the exact square root in (5). A positive lower bound
for 4P-D would automatically imply P>0 and D/P<4, so (13) avoids
requiring two separate relative asymptotics. It does not establish
such a bound. All constants in (10)-(13) remain existential.

For a fully upper-bounded right side one can use (3), namely

    r_T <= C_w [N/(T L)+N/(T^2 L^2)],

along with L622's complete E_w(T). The first term is o(eta_T)
at this length, by the exponent comparison already proved in
Section 3. The second term has the retained completion scale.
Thus the new derivative coefficient rescaling does not destroy
the available source-error precision. It also gives no smallness
for q relative to p: (10) is an error estimate, not a bound on the
main term H_d. The assertion ||d||<=||a||/100 cannot be inserted
as a contraction in the different, correlated moment norm.

The attempted comparison now has a precise missing quantity:
the complete F=Re{(4 partial_1 partial_2 H_a-H_d)(0)}, uniformly
in X as N grows. Nonnegativity of the actual P and D gives only
p>=-eta_T and q>=-sigma_T^2 eta_T. These two lower bounds give
no positive lower bound for 4p-q. The old absolute estimates (6)
likewise provide no lower bound for it. Replacing H_a or H_d by
its zero-shift arithmetic Gram approximation would require the
unproved growing-index comparison stopped in L623/L624; it is
not a consequence of (10). No prefix, boundary term, isolated
permutation or height phase was discarded in obtaining (11)-(13).

This second mathematical attempt therefore ends as EXPLORATION,
not as a negative sign, a counterexample to (13), a new arithmetic
estimate or an impossibility theorem. It has isolated the full
linear correlated comparison and its error, but has not evaluated
it with a uniform signed bound. The direct absolute-derivative
cost refinement is parked after two inconclusive attempts. It
requires materially new quantitative input before reopening;
repeating (10)-(13) does not supply it. Other observers and the
pointwise and all-degree gaps remain unresolved.

## Mathlib

Full matching coverage for this weighted quartic identity, its
Möbius specialization and the imported shifted fourth-moment input
was not checked and is unknown. The proof uses standard integration
by parts, product rules, Holder, Cauchy's integral formula and
Cauchy--Schwarz; no exact Mathlib
declaration is claimed. This informal calculation is not a Lean
formalization, and the conditional arithmetic imports remain separate.
