# Corollary 488c: effective off-axis comparison and the constant100 local count

## Hypotheses

Use the actual H_t normalization and CLOSED-window multiplicity count of
C488b, with the actual theta family of L058 and the normalization already
verified in C488a:

    H_0(z)=xi((1+iz)/2)/8,
    N_t(x,r)=#{z:H_t(z)=0, |Re z-x|<=r}.

All complex zero copies are counted. No RH, simplicity, lower nonreal
ordinate or all-height reality is assumed. Use the source inputs stated
below, with their branches and all-real-sigma domains. Let

    B_t(z)=M_t((1-iz)/2),  M_t(s)=exp(t alpha(s)^2/4)M_0(s),
    alpha(s)=1/(2s)+1/(s-1)+(1/2)Log(s/(2pi)),
    M_0(s)=(s(s-1)/16)pi^(-s/2)sqrt(2pi)
           exp((s/2-1/2)Log(s/2)-s/2).

The principal logarithms define these functions off (-infinity,1].

## Conclusion

For x>=29399, 3<=y<=4 and 0<=t<=1/5,

    |H_t(x+iy)/B_t(x+iy)-1| < 9/10 < 99/100.              (1)

Consequently, for every 0<=t<=1/5 and |x|>=2r>=400,

    N_t(x,r) <= 100 r log(2+|x|).                          (2)

The independent conceptual audit2115 verifies the numerical target,
including C488b's counting reduction. It is a quantitative
specialization of Polymath's known local-count mechanism, not a claimed
new order of magnitude or a resolution of RH. Transport improvements,
uniform overlap at t=0, all-height reality and mixed signs remain open.

## Proof

### Imported inputs and why a numerical specialization is needed

Import D. H. J. Polymath, *Effective approximation of heat flow evolution
of the Riemann xi function, and a new upper bound for the de Bruijn--Newman
constant*, Research in the Mathematical Sciences 6 (2019), article31,
[arXiv1904.12438v2, 4August2019, Section4 (39), (41),
Lemma5.1(v), Propositions6.1-6.2, (43)-(44), (48)-(58), and
Proposition9.1(ii)](https://arxiv.org/html/1904.12438v2).
The cited statements and the relevant Gaussian/remainder proof cases
were inspected. The Arias de Reyna estimates are imported in the precise
form of Proposition6.2, not claimed independently reproved here.

Proposition9.1(ii) gives a qualitative comparison with an unspecified
onset. Proposition6.3 and Theorem1.3 as stated restrict sigma or y;
their final numerical constants are NOT applied outside those domains.
Instead, Proposition6.1 allows every real sigma, and Proposition6.2
allows every real integration variable u. We integrate its bounds
directly on the needed band. This difference, and the resulting
numerical onset, are what require the argument below. It uses the
correct t/2 times alpha in Proposition6.1, not the stronger coefficient
printed in the informal Section9 real-part estimate.

Here are the exact usable imports. Write f*(s)=conjugate(f(conjugate(s))).
The source's Riemann--Siegel decomposition (39), for nonimaginary z,
every integer N>=0 and t>0, is

    H_t(z)=sum_(n=1)^N [r_t,n((1+iz)/2)+r_t,n*((1-iz)/2)]
           +R_t,N((1+iz)/2)+R_t,N*((1-iz)/2).             (3)

The r and R are the source's Gaussian evolutions of the gamma-times-
Dirichlet summand (37) and contour remainder (38). Proposition6.1 gives,
for sigma real, T>10, n>=1 and 0<t<=1/2,

    r_t,n(s)=M_t(s) exp((t/4)log^2 n)n^(-s-(t/2)alpha(s))(1+e_n),
    |e_n|<=exp([(t^2/8)|alpha(s)-log n|^2+t/4+1/6]
                    /(T-3.33))-1,  s=sigma+iT.          (4)

Conjugation gives the same estimate for r_t,n* at sigma-iT. The source
also gives |alpha'(s)|<=1/[2(Im s-3)] for Im s>3. Its Stirling input
has logarithmic gamma error at most 1/[12(|w|-0.33)] when |Im w|>=1.

For T'>0 put a=sqrt(T'/(2pi)), N=floor(a), p=1-2(a-N).
Proposition6.2 expands the contour factor in R_0,N(u+iT') as
(-1)^(N-1)U a^(-u)[sum_(k=0)^K C_k(p,u)/a^k+RS_K(u+iT')],
where |U|=1, |C_0(p)|<=1/2, and C_0 is independent of u.
The removable cases p=+-1/2 are included. For k>=1 its bounds are

    |C_k(p,u)| <= sqrt(2)/(2pi) 9^u Gamma(k/2)/2^k          (u>0),
    |C_k(p,u)| <= 2^(1/2-u)/(4pi^2)
                  Gamma(k/2)/[((3-2log2)pi)^(k/2)]        (u<=0),
    |RS_K| <= (1/7)2^(3u/2)Gamma((K+1)/2)(1.1/a)^(K+1)  (u>=0),
    |RS_K| <= (1/2)(9/10)^ceil(-u)
                   Gamma((K+1)/2)(1.1/a)^(K+1)           (u<0, K+u>=2).
                                                               (5)

These are source conclusions with hypotheses retained, not numerical
experiments. At u=0 either use the nonpositive coefficient bound or
its limiting positive bound; the latter is also a larger bound.

### Common parameter bounds

First take 0<t<=1/5. Set

    T=x/2, T'=T+pi*t/8, b=sqrt(T/(2pi)), a=sqrt(b^2+t/16),
    N=floor(a), sigma+=(1+y)/2, sigma-=(1-y)/2,
    s+=sigma+-iT, s-=sigma-+iT.

Thus T>=29399/2>14000, b>48, and -3/2<=sigma-<=-1,
2<=sigma+<=5/2. The inequality b>48 follows from pi<22/7.
Furthermore

    a/b<=1001/1000, a<sqrt(T), a<b^2,
    (a/b)^((y+1)/2)<3/2.                                  (6)

For example (a/b)^2<=1+1/184320<(1001/1000)^2; the last
claim follows by increasing the exponent to3. These bounds cover
every jump of floor(a), including a integer.

We use only elementary scalar estimates: 3<pi<22/7, pi^2<10,
8/3<e<3, log14000<10, log2<7/10 and log9<11/5.
The last two follow by lower Taylor sums for exp(7/10) and exp(11/5);
log14000<10 follows from (8/3)^10>14000. Every numerical inequality
below has slack; the exact rational checks are recorded at the end.

For real u in [-3/2,5/2], integrate the source alpha' bound from iT:

    |alpha(u+iT)-(log b+i*pi/4)| <= 3/(T-3)=:eta,
    |alpha(u+iT)| < log b+1.                              (7)

Indeed alpha(iT) differs from log b+i*pi/4 by at most3/(2T),
and the horizontal segment contributes at most(5/2)/[2(T-3)].
Also Re alpha(sigma++iT)>=log b, since both rational real parts
in alpha are positive there.

### Two finite sums and their errors

In the first main sum normalized by B_t, the n=1 term is1.
For n<=N we have log n<=2log b by (6), so

    exp((t/4)log^2 n-(t/2)Re alpha(s+)log n)<=1.

Its n>=2 terms therefore have total modulus less than2/3: indeed
sum_(n=2)^infinity n^(-2) is at most
1/4+1/9+1/16+1/25+integral_5^infinity v^(-2)dv
=2389/3600<2/3. The whole sum has absolute-term mass below5/3.

Let gamma=M_t(s-)/M_t(s+). Since (log M_t)'=alpha(1+(t/2)alpha'),
(7) gives throughout the horizontal segment between sigma-+iT and
sigma++iT

    Re (log M_t)' >= log b-h,
    h=[3+(log b+1)/20]/(T-3) < 1/1000.

To check the last uniform inequality, use log b<log T/2 and the
decrease of log T/(T-3) for T>=14000; the upper bound is at most
(33/10)/13997. Integration over length y<=4, and conjugation, give

    |gamma|<=exp(4h)b^(-y)<2b^(-y).                        (8)

For the second main sum, (7) and log n<=2log b bound its heat weight
by exp(t eta log n/2). Its exponent is at most
3log T/[20(T-3)]<1/1000, again uniformly, so this factor is<2.
Consequently its normalized absolute-term mass is less than

    4 b^(-y)sum_(n=1)^N n^((y-1)/2)
    <=4 b^(-y)a^((y+1)/2)
    <6 b^((1-y)/2)<=6/b<1/8.                              (9)

For both sums, |alpha(sigma+-iT)-log n| and
|alpha(sigma-+iT)-log n| are at most2log T, by (6)-(7).
The exponent in (4) is therefore bounded by

    [log^2 T/50+1/4]/(T-4)
    <= (9/4)/13996 < 1/6000.                              (10)

Here log^2 T/(T-4) decreases for T>=14000: its logarithmic derivative
is 2/(T log T)-1/(T-4)<0. The constant term decreases as well.
The elementary bound exp(v)<=1/(1-v) for 0<=v<1 now makes every
relative error in (4) less than1/1000. Their total normalized
contribution is below (5/3+1/8)/1000<1/500.

### A remainder estimate on the larger sigma interval

We prove, for every -3/2<=sigma<=5/2,

    |R_t,N(sigma+iT)| < 40 |M_0(iT')|.                    (11)

Use (41) with beta=pi*i/4. Both imaginary parts T and T' are positive,
so its contour condition holds; the Gaussian integral is absolutely
convergent by the source's sub-Gaussian growth justification. With
u=sigma+sqrt(t)v, its phase factor has modulus1 and its outside factor
has modulus exp(t*pi^2/64).

Taylor's theorem for the fixed holomorphic log M_0 along the horizontal
segment at height T', the alpha' bound, and the gamma Stirling error
give, for every real u, a bound on the gamma-prefactor times a^(-u):

    |prefactor(u+iT')| a^(-u)/|M_0(iT')|
       <= exp[u^2/(4(T'-3))+3|u|/(2T')+1/(6(T'-0.66))]
       <= exp[(u^2+1)/(T-3)].                             (12)

The prefactor is s(s-1)pi^(-s/2)Gamma(s/2)/16 from (38).
For the second line use 6|u|<=3u^2+3 and T'>=T. Specifically the
preceding exponent is at most [u^2+6|u|+2/3]/[4(T-3)], hence at
most (u^2+11/12)/(T-3). This retains the full Stirling error; it
does not copy the smaller intermediate constant in the printed6.3
proof. No bounded-u restriction is made here.

For u>=0 choose K=1 in (5). Since sqrt(2)Gamma(1/2)/(4pi)<1/4
and (1.1)^2/7<1/5, the nonleading coefficient and remainder mass E(u)
is bounded by

    E(u)<=9^u/(4a)+2^(3u/2)/(5a^2)
         <=9^u/[4(a-1)].                                 (13)

For u<0 put v=-u>0 and choose K=ceil(v)+2. Then K+u>=2, so (5)
applies, and K+1<=v+4. Its nonleading mass is at most

    2^(v-1)sum_(k=1)^(K+1) Gamma(k/2)(1.1/a)^k.

For integer k>=1, Gamma(k/2)<=2exp(k^2/8). For even k this follows
from (k/2-1)!<=(k/2)^(k/2) and log w<=w/2; for odd k use the
half-integer product and sqrt(pi)<2, with k=1 separately.
Since log a>3 and log(1.1)<1/10, each summand is at most

    (2/a)exp[k^2/8-29k/10+3]
       <=(2/a)exp(v^2/4+1/4),  1<=k<=v+4.

The last assertion follows by convexity in k: at1 the exponent is
9/40, and at v+4 it is v^2/8-19v/10-33/5, both no larger than
v^2/4+1/4. Thus, using v+4<=4exp(v/4) and log2<7/10,

    E(u)<=(v+4)/a exp(v^2/4+v log2+1/4)
         <=(16/a)exp(v^2/2).                              (14)

For the last step, the maximum of 19v/20-v^2/4 is361/400;
adding1/4 gives461/400<6/5, and exp(6/5)<4. The coefficient
bound used in the first line follows directly from (5), since
sqrt(2)/(4pi^2)<1/2 and ((3-2log2)pi)^(-1/2)<1<1.1.
This handles the entire negative Gaussian tail, including arbitrarily
large K. It uses neither an omitted tail nor a finite sample of u.

Let expectation E_sigma refer to U with density
(pi*t)^(-1/2)exp(-(U-sigma)^2/t), and put q=1/(T-3)<1/10000.
Equations (5), (12)-(14) imply

    |R_t,N(sigma+iT)|/|M_0(iT')|
      <=exp(t*pi^2/64+q) [ (1/2)E_sigma exp(qU^2)
         +1/[4(a-1)] E_sigma exp(qU^2+U log9)
         +(16/a)E_sigma exp((q+1/2)U^2) ].               (15)

Extending each nonnegative integral to the whole real line gives this
upper bound. Each is integrable since t(q+1/2)<1. The exact Gaussian
formula, obtained by completing the square, is

    E_sigma exp(dU^2+cU)
      = exp(c sigma+t c^2/4)(1-td)^(-1/2)
        exp[d(sigma+tc/2)^2/(1-td)],  td<1.              (16)

Uniformly for |sigma|<=5/2 and t<=1/5 the three expectations in (15)
are, respectively, <2, <486, and <90. Here are details of all three:

* For d=q, (1-tq)^(-1/2)<1001/1000. Both q sigma^2/(1-tq)
  and q(sigma+t log9/2)^2/(1-tq) are <1/1000; in the second
  bound use |sigma+t log9/2|<=68/25. Hence the product of this
  square-root factor and either exponential is <1001/999.
* Taking c=0 proves the first bound. Taking c=log9 gives
  exp(c sigma)<=9^(5/2)=243 and t c^2/4<121/500.
  Since exp(121/500)<=500/379 and
  (1001/999)(500/379)<2, this proves the second.
* For d=q+1/2<=5001/10000, the square-root factor is<10/9,
  and d sigma^2/(1-td)<7/2. Thus the third expectation is
  <(10/9)exp(7/2)<(10/9)e^4<90.

Finally exp(t*pi^2/64+q)<exp(1/30)<=30/29. The bracket in (15)
is less than

    1+486/(4*47)+(16/48)*90 <34.

Multiplication by30/29 gives <36<40, proving (11). The changeable
integer K was used only in pointwise upper bounds of an already
defined integrable remainder; no infinite Riemann--Siegel expansion
was interchanged with the Gaussian integral.

### Normalizing the remainders and assembling the count

For v>=T, Im alpha(iv)=pi/4-1/(2v)-v/(1+v^2)>0. Hence
log|M_0(iv)| decreases with v and |M_0(iT')|<=|M_0(iT)|.
For 0<=u<=sigma+, the explicit alpha gives
Re alpha(u+iT)>=log b-1/T^2. Integrating in u yields

    |M_0(iT')/M_0(s+)|<=exp((5/2)/T^2)b^(-sigma+).

At s+, Re alpha>=log b>3 and |Im alpha|<1 by (7), so
Re(alpha^2)>0 and |M_t(s+)|>=|M_0(s+)|. Therefore

    |M_0(iT')/B_t(x+iy)|<2 b^(-sigma+)<=2/b^2.           (17)

The two remainders in (3) have real parts sigma- and sigma+ at
positive imaginary height T, after conjugating the starred one.
Equations (11) and (17) bound their combined normalized modulus by
160/b^2<160/48^2=5/72. Combining this with (9)-(10) and the first
sum gives the fully uniform estimate

    |H_t/B_t-1| < 2/3+1/8+1/500+5/72
                =971/1125 <9/10.                        (18)

By L058 and the normalization in C488a, H_t converges locally
uniformly to H_0 as t decreases to0. B_t also converges locally
uniformly to its nonzero B_0 on this band. The limiting ratio is
therefore at most971/1125, still strictly below9/10. This proves
(1) on the closed time interval; no continuity of a sharp count is
assumed.

Apply C488b with A=29399 and delta=99/100, whose additional
comparison hypothesis is now supplied by (1). Its positive-kernel
argument covers the closed window when |x|>148r, and its even
global-count bound covers 2r<=|x|<=148r. Both retain multiplicity
and t=0. This proves (2); the conceptual audit below also checks that
reduction. Neither conclusion asserts that
the counted zeros are real.

### Verification and limitations

`python3 scripts/heat/local_count_off_axis_2114.py` writes the exact
rational scalar checks to `scripts/heat/local-count-off-axis-2114.json`.
The checks support the scalar comparisons in (6)-(18); they do not
validate imported analytic theorems, the Gaussian representation, or
the C488b counting reduction. No sampled H_t values or floating-point
underflow is used. The separate conceptual audit below passes. The sharp
count is a local input, not an RH candidate.

### Conceptual audit — 21 November2026, step2115

The full numerical domain passes. The imports, all-real-u bounds,
Gaussian integration, normalization and C488b's counting reduction were
checked independently of the scalar script. The cited source was
inspected at (39), (41), Lemma5.1(v), (43), Propositions6.1-6.2 and
(48)-(58), including the negative-real-part case and K restriction.
This audit uses the existing ready assessment; it does not assign
numerical constants to Proposition9.1's qualitative onset or extend
Proposition6.3 beyond its stated sigma interval.

In (3) the dominant n=1 term is the starred summand at s+.
The principal branches obey M_t*(s)=M_t(s), so its approximation
has leading factor B_t exactly. Conjugation also transfers (4) to
the lower half-plane. For the reflected factor only its modulus is
compared along the horizontal segment at height +T. Thus (8) requires
no erroneous identification of the two complex phases. The factor
t/2 multiplying alpha is retained throughout both finite sums.

The elementary Gamma estimate in (14) can be checked without an
asymptotic formula: put w=k/2. For even k, (w-1)!<=w^w, and for
odd k>=3 the half-integer product is at most2w^(w-1/2)<=2w^w.
Since log w<=w/2 for w>0, these are at most2exp(k^2/8);
k=1 follows from sqrt(pi)<2. Extracting one factor a^(-1) leaves
exp(k^2/8-29k/10+3), since log a>3 and log(1.1)<1/10.
Its convexity in k bounds it by its two endpoint values on
[1,v+4], exactly as used above. The final maximum
max_(v>=0)(19v/20-v^2/4)=361/400 pays the entire negative tail.
There is no truncation in v. K=ceil(v)+2 is a measurable positive
integer with K-v>=2, and K+1<=v+4. Changing K in these pointwise
upper bounds does not change the remainder function being integrated.

At u=0 the nonpositive coefficient estimate in (5) directly gives
|C_1|<1/4, so (13) includes that endpoint without assuming continuity
in sigma. All p values, including the removable singularities and
the floor jumps at integral a, are covered by the source bounds.
For (12), a holomorphic logarithm of M_0 exists in the upper
half-plane. Its Taylor remainder is at most u^2/[4(T'-3)] for
every real u. Stirling's error applies because |Im(s/2)|=T'/2>1,
even when u is arbitrarily negative. The linear error at iT' and
the retained Stirling term give the displayed full exponent in (12).

Completing the square gives (16) with U of variance t/2, not t.
The largest quadratic coefficient used is q+1/2<5001/10000,
so 1-t(q+1/2)>44999/50000>0 throughout the time domain. The
three expectations are consequently genuine integrals over the full
line. Their bounds2,486,90 give bracket3157/94<34 and total
<1020/29<36<40. This verifies (11) without an unproved dominated
interchange. The Gaussian representation itself is the cited (41),
whose shifted height T'>0 keeps the contour in the allowed half-plane.

The vertical derivative of log|M_0(iv)| is -Im alpha(iv)<0 for
v>=T. Horizontally, Re alpha(u+iT)>=log b-1/T^2 for
0<=u<=sigma+, while Re(alpha(s+)^2)>0. These signs verify both
normalizations in (17); each remainder costs less than80/b^2.
The resulting error bound971/1125 is strictly below9/10 and99/100.
At t=0 its non-strict limiting bound is still below those thresholds.
C488b's audited positive-kernel argument then supplies the count on
the entire closed domain, including multiplicities and negative x.

The existing scalar script was replayed and all33 checks passed; the
complete /checks value in its certificate was inspected using the
shared JSON inspector. Those checks establish only the stated rational
comparisons. The analytic arguments above supply the remaining audit.
The dependency review found no need to change the DAG. This verifies
a quantitative local specialization,
not a new counting order, transport theorem, or sign input for RH.

## Mathlib

Full matching coverage is not checked; no absence claim is made.
No Mathlib declaration is used to verify the effective heat remainder
or numerical onset. Standard supporting tools are the Gaussian integral,
Taylor's theorem for a holomorphic logarithm, dominated convergence,
and C488b's Cauchy/Hadamard/Tonelli reduction.
