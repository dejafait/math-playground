# Lemma 588: constant-offset periodic bulk misses the clipped threshold

## Hypotheses

Use L586's exact spectral matrices A(u), interval I=[-1/2,1/2],
function space E, matrix K=integral_I A(u) du, and finite cone C_I.
For h(s)=a+b cos(omega s), suppose

    0<b<a,   0<omega<=1/2,   K-C(h) in C_I.                 (1)

Here C(h) averages the outer product of the six ordinary lag-one
jets over one full period, exactly as in L586. Cone membership in
(1) is weaker than the proposed strict-interior condition. Amplitudes
already include any nonnegative conic weight assigned to this whole
path. No probability normalization, fourth-moment completion, Hardy
realization or RH premise is assumed.

## Conclusion

Writing brackets for uniform phase average, every path in (1) satisfies

    a^2 <= 4194/19649 < 2/9,
    <(h h''-(h')^2)_+> <= 2097/628768 < 1/288.              (2)

The gap in the second inequality is 97/707364. Thus no member of this
family can meet the approved joint strict-remainder and 1/288 test.
The estimate is uniform through the frequency endpoint and all limiting
amplitude/frequency regimes. This stops only this surrogate family,
not general stationary paths or actual-Hardy/Xi signs. It is a local
calculation under the saved EXPLORE assessment, not a certified novelty
claim. The separate conceptual audit in Section 4 passes, including an
independent complete-tail certificate. This verifies the stated local
obstruction, not a new inequality beyond the previously recorded result.

## Proof

### 1. Exact covariance and a necessary dual inequality

The constant/cosine cross terms average to zero. L586 (3)--(4),
including its exceptional zero-frequency normalization, therefore gives

    C(h)=a^2 A(0)+(b^2/2)A(omega).                         (3)

In particular this identity includes all nine lag-one cross entries,
not only the same-height derivative block. For every f in E with
f>=0 on I, the definition of the finite evaluation cone implies

    integral_I f(u) du-a^2 f(0)-(b^2/2)f(omega)>=0.        (4)

Indeed represent K-C(h) as a finite nonnegative sum of A(u_i),
and apply L586's functional L_M; the result is sum_i w_i f(u_i).
This uses the actual function-space cone, not an ambient PSD test.
The moment-cone interior criterion imported in L586 (Blekherman--Fialkow,
*The core variety and representing measures in the truncated moment
problem*, arXiv:1804.04276v1, Proposition 2.1/Corollary 2.2, pp.5--6)
is not needed for this necessary inequality; no general theorem is
being reproved. No maximal-atom sufficiency claim is used.

### 2. An explicit nonnegative entry function

The following eight functions belong to E, as is immediate by choosing
the same-lag or cross-lag entries in L586 (3):

    1, u^2, u^4, cos u, u^2 cos u, u^4 cos u, u sin u, u^3 sin u.

For example same-lag (j,k)=(0,0),(1,1),(2,2) give the first
three. Cross-lag (0,0),(1,1),(2,2) give the three cosine terms;
(0,1),(1,2) give the sine terms up to signs. Thus all coefficient
choices below are in the exact space, with its relations respected.

Put

    q(u)=1-36u^2+(1584/5)u^4-(27456/35)u^6.

Let g be the linear combination of the displayed eight basis functions,
in that order, with coefficients

    20406931943878657,
    -24477043814885880/7,
    2123114775919056/35,
    -20406931943878656,
    8870803683860448/7,
    -106482224695968/35,
    -7974003096078624,
    3405467682859968/35.

Despite their large size these are exact rationals; floating evaluation
of g is not used. The even Taylor coefficients of g and q^2 agree
at degrees 0,2,...,14 (the coefficient at degree 14 is zero).
Their odd coefficients vanish identically. The following exact bound
is certified below:

    sup_(u in I) |g(u)-q(u)^2| < 11/5000 < 1/400.          (5)

Consequently f=g+1/400 is strictly positive on I, f belongs to E,
and f(0)=401/400. Direct polynomial integration gives

    integral_I q(u)^2 du=256/1225,
    integral_I f(u) du <=256/1225+1/200.                   (6)

The second bound follows from (5) and the length-one interval, without
any oscillatory cancellation estimate for the large coefficients.

For the elementary analytic input use NIST, *Digital Library of
Mathematical Functions*, v1.2.8 (15 September 2026),
[equations 4.19.1--2](https://dlmf.nist.gov/4.19), the entire sine and
cosine Maclaurin series. Their specialization to these shifted terms
and the uniform tail bound are justified below; no general theorem is
reproved. For completeness here is the full finite rational specification
and tail justification for (5). For each basis member u^s cos u or
u^s sin u let d_(t,s)(n) be its Taylor coefficient: it is zero unless
k=n-s>=0 has the appropriate parity, and otherwise is
(-1)^floor(k/2)/k!. For a polynomial basis member u^s use
d_(poly,s)(n)=1 if n=s and zero otherwise. Let c_(t,s) be the eight
coefficients above and p_n the coefficient of q^2. Define

    E_50=sum_(n=16,18,...,50)
            |sum_(t,s) c_(t,s)d_(t,s)(n)-p_n|/2^n
         +(4/3)sum_(t!=poly,s) |c_(t,s)d_(t,s)(52)|/2^52.

The first sum bounds all included terms on |u|<=1/2. Beyond degree
50, each individual trig series has first omitted exponent 52;
its consecutive absolute terms have ratio
|u|^2/((k+1)(k+2))<=1/4. Thus the factor 4/3 bounds its entire
tail, including endpoints. All series converge absolutely. There is
no infinite numerical truncation assumption. Exact rational arithmetic
gives

    E_50=
    53765584323603286414215018684766367271819623359194798028350610463719655842783
    /25082513548667626541684295307238193041433991623155113914197688188928000000000000
    <11/5000.

The degree matching, integral in (6), this rational comparison and
the final bounds are reproduced by

    python3 scripts/offset-periodic/zero_atom_certificate.py

The complete certificate is
`scripts/offset-periodic/zero_atom_certificate.json`. The script uses
only Python integer/Fraction arithmetic, explicitly generates every
coefficient in the finite sums and asserts each required inequality.
Its rational uniform-error value was inspected in full. The optional
early decimal grid diagnostics in the working note are not inputs.

### 3. Uniform clipping bound

Since f(omega)>=0, (4)--(6) give

    a^2 <= (256/1225+1/200)/(401/400)=4194/19649<2/9.       (7)

Let theta=omega s, r=b/a in (0,1), and t=-cos theta. Ordinary
differentiation gives the exact identity

    h h''-(h')^2=-omega^2(ab cos theta+b^2),
    (h h''-(h')^2)_+=omega^2 a^2 r(t-r)_+.

For t<=0 the rightmost positive part is zero. For t>0, if t<=r
it is zero, and otherwise r(t-r)<=t^2/4, since
(r-t/2)^2>=0. Hence r(t-r)_+<= (t_+)^2/4 at every phase.
The uniform-circle average of (-cos theta)_+^2 is 1/4 (half
the integral of cos^2). Therefore

    <(h h''-(h')^2)_+> <=omega^2 a^2/16
      <=a^2/64 <=4194/(19649*64)=2097/628768.

Finally 1/288-2097/628768=97/707364>0, proving (2).
This argument controls all parameters in (1) uniformly, so no
unexamined boundary regime can rescue the family. It neither constructs
a residual nor assumes its existence outside the stated hypothesis.

### 4. Independent conceptual audit, 31 October 2026

The audit reuses the approved source comparison in
`drafts/literature/2026-10-31-l588-critical-audit-scope.md`.
It verifies only this lemma, importing L586's definitions and direct
functional identification; L586's general interior and cubature
theorems, L585's carrier and L473's arithmetic results are not additional
premises of the obstruction.

To check every entry, write c=cos u and s=sin u in the following
two blocks. In increasing derivative order 0,1,2, the same-lag block
of A(u) is

    S(u)=[ 1    0   -u^2 ]
         [ 0   u^2    0  ]
         [-u^2  0    u^4 ],

and the block with first lag 0 and second lag 1 is

    B(u)=[ c     -u s    -u^2 c ]
         [ u s    u^2 c  -u^3 s ]
         [-u^2 c  u^3 s   u^4 c ].

The other cross block is B(u)^T. These follow by taking the real
part of i^j(-i)^k u^(j+k)e^(-iu), and verify all nine cross
entries and the signs used to select the eight functions. In
particular the test is in the actual E even if its coordinates
satisfy linear relations. At zero, A(0)=e e^T for
e=(1,0,0,1,0,0). At positive frequency the six coordinates of the
oscillating part of h are b Re(v(omega)e^(i theta)). The normalized
phase average of their product is (b^2/2)Re(v v^*); its average
against a e is zero. Thus (3) holds entrywise. The paired frequencies
are one evaluation fibre since A is even; they are not counted twice.
Applying an entry linear combination to the finite nonnegative
representation of K-C(h) proves (4) directly, with no PSD sufficiency,
closure, optimizer or interior assumption.

An independent script starts from the printed q and eight coefficients,
without importing the original script or solving its fitting system.
At radius R=1/2, the scaled cosine/sine coefficients start respectively
at t_0=1 and t_1=R and obey

    t_(k+2)=-t_k/[4(k+1)(k+2)].

For shift s, multiply by R^s and move the index by s. This computes
each coefficient times R^n directly, independently of the original
factorial/Gaussian-elimination implementation. The resulting nonzero
coefficients of q^2, and of g through degree 14, are

    n:    0    2       4          6             8
    p_n:  1   -72   9648/5   -853248/35   27447552/175
    n:       10                12             14
    p_n: -86980608/175    753831936/1225         0.

All odd coefficients vanish. Direct integration is the finite identity
sum_(n=0,2,...,12) p_n/((n+1)2^n)=256/1225, verifying (6).
The independent computation reproduces every one of the original
certificate's sixteen fields, including every term defining E_50 and
its full printed rational value; it does not rely on its PASS label.

As a separate complete-tail check, retain only degrees through 28.
For the five shifted trigonometric terms the first omitted total
degree is 30. Their unshifted exponents are respectively 30,28,26,29,27.
Every subsequent absolute-term ratio on the closed interval is at
most 1/[4*27*28]=1/3024. Hence the entire remaining tail of each
term is bounded by 3024/3023 times its absolute degree-30 contribution.
Using the same coefficient notation as in Section 2, this yields

    E_28=sum_(n=16,18,...,28) |sum c_(t,s)d_(t,s)(n)|/2^n
         +(3024/3023)sum_(t!=poly,s)|c_(t,s)d_(t,s)(30)|/2^30
        =11625308796299635084201636747882303
         /5423394334107898910473778626560000000
        <11/5000<1/400.

There are no polynomial terms past degree 12 in q^2. The full finite
sum, five tail terms, exact E_28, all degree matches and the original
E_50 terms were inspected; the full evidence is
`scripts/offset-periodic/audit_zero_atom_certificate.json`. This is a
second proof of the required uniform approximation inequality with a
different truncation and recurrence computation. In particular
f>=1/400-E_28>0 on the whole closed interval, and f(0)=401/400.
Reproduce it with

    python3 scripts/offset-periodic/audit_zero_atom_certificate.py

Finally, the phase inequality in Section 3 has three exhaustive cases:
t<=0, 0<t<=r, and t>r. In the last case
r(t-r)=t^2/4-(r-t/2)^2, while in the first two cases the clipped
quantity is zero. Its mean bound uses the exact uniform-circle integral
of (t_+)^2, namely 1/4, and the endpoint omega^2<=1/4. Exact arithmetic
confirms both ratios in (2) and the positive gap 97/707364. The cases
t=r and omega=1/2 are included. The bounds are uniform as a tends to
zero, b/a tends to either endpoint, and omega decreases to zero.
At each omega>0 the complete-period change of variable is exact; no
limit interchange or positive-frequency covariance formula at omega=0
is used. The frequency-zero path is outside (1). No limiting regime
or strict-interior loophole invalidates this necessary-cone stop.

Audit verdict: the claimed obstruction passes, with no mathematical
repair or new hypotheses. The broader periodic clipping problem,
probability/fourth-moment assembly and actual-Hardy/Xi transfer remain
unresolved. The added certificate is local verification, not evidence
of originality or of RH.

## Mathlib

Full matching coverage for this covariance/clipped-threshold obstruction
has not been checked. Supporting elementary trigonometric, series and
polynomial-integration facts are not asserted to constitute a matching
formal theorem. L586's cited moment-space results remain imported with
their stated qualifications. The finite certificate is informal
computer-assisted evidence with exact arithmetic, not a Lean proof.
