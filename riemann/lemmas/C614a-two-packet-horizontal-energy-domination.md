# Corollary 614a: domination for the complete bounded two-packet family

## Hypotheses

Use exactly the family in L614: 0<a<=4, 0<=u,v<=2, m,n in {1,2},
with m copies of each of -a/2+iu and -a/2-iu and n copies of each of
a/2+iv and a/2-iv. Coincident labels keep their combined multiplicity.
All pair sums are ordered and retain products of multiplicities. Define

    K(z)=sin(pi*z)/(pi*z), K(0)=1,
    E=sum_(z,s in Z) K(z-s)^2,
    M=sum_(z,s in Z; Re z=Re s) 1=4m^2+4n^2.

The pairwise square is algebraic. There is no zero-spacing limit in the
claim: a is positive. No zeta realization, thin-box, simplicity or
minimum-spacing hypothesis is imposed.

The proof includes a finite directed-rounding certificate, using the
usual IEEE-754 binary64 model for Python's elementary arithmetic and
`math.nextafter`. It does not trust numerical library sin, cos, sinh or
exp evaluations. The separate 2026-11-01 invocation audited the
implementation, certificate and used L614 reductions, including a second
arithmetic implementation described below. This is a notebook proof/code
audit, not an external review or formal verification of either runtime.

## Conclusion

For this complete bounded family,

    E >= M.                                                   (1)

This settles only the stipulated two-packet test. It establishes no
general finite-multiset inequality, equal-ordinate zeta count, removal
of actual-zeta weights, charge conversion or Xi sign. In particular,
it is not a candidate proof of RH. Coverage beyond the recorded sources
is unestablished; no improvement of a cited zeta theorem is claimed.

## Proof

### Reduction and known inputs

L614 (1)--(2) cover aligned multiplicities/depths, equal multiplicities,
equal depths and a<=1/2. Exchanging packets therefore leaves only

    m=1, n=2, 1/2<=a<=4, 0<=v<=u<=2.                        (2)

Including the already settled endpoints in (2) causes no loss. Retain
L614's notation

    H(b)=(sinh(pi*b)/(pi*b))^2, H(0)=1,
    F(a,b)=Re K(a+ib)^2,
    w(t)=1-|t| on [-1,1],
    A(t)=cosh(2pi*u*t), B(t)=cosh(2pi*v*t), c(t)=cos(2pi*a*t).

Its exact full-multiplicity formula is

    E-M=2(H(2u)-1)+8(H(2v)-1)
           +8[F(a,u-v)+F(a,u+v)].                           (3)

The only non-elementary source interface is already imported in L614:
the triangular Fourier pair from Baluyot--Goldston--Suriajaya--
Turnage-Butterbaugh, *Pair Correlation of Zeros of the Riemann Zeta
Function I*, [arXiv:2501.14545v3](https://arxiv.org/html/2501.14545v3),
(4.1), and the complete finite-energy norm identity assessed in
Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann
zeta function are simple and on the critical line*,
[arXiv:2609.02882v1](https://arxiv.org/html/2609.02882v1), Proposition
2.1, (2.4), (2.10)--(2.21). L614 gives their precise specialization.
Neither source is assumed to assert (1); their norm identity is not
reproved here. All expansions below are finite or on a compact interval.

### Small depths: 0<=u<=1/20

L614 (8) makes E nondecreasing in v on [0,u], because
cosh(2pi*u)<=cosh(pi/10)<2. To verify the last strict bound, pi^2<10
and (2k)!>=2^k give

    cosh(pi/10) <= 1/(1-pi^2/200) < 20/19 < 2.

It suffices to take v=0. At u=0, (3) is 16K(a)^2>=0. Assume u>0
and put f(a)=K(a)^2. The triangular Fourier pair and Taylor's theorem
for cosh, whose fourth derivative is cosh, give

    F(a,u) >= f(a)-(u^2/2)f''(a)-R,
    0<=R <= (2pi*u)^4 cosh(2pi*u)/360.                     (4)

Indeed, int w(t)t^4 dt=1/15, and the absolute fourth-order remainder
is at most (2pi*u*t)^4 cosh(2pi*u)/24. Differentiation of f under
this compact integral is justified by continuous bounded derivatives.
Also H(2u)-1>=4pi^2*u^2/3, by the positive power series of sinh.
Consequently (3) gives

    E-M >= 16f(a)+u^2(8pi^2/3-8f''(a))-16R.              (5)

The remainder satisfies the uniform bound

    16R/u^2 <= (32/45)pi^4*u^2*cosh(2pi*u)
              < (32/45)*(100/400)*(20/19)=32/171.         (6)

For 1/2<=a<=4/5, concavity of sine on [pi/2,pi] gives
sin(pi*a)>=2(1-a). Hence f(a)>=1/(4pi^2)>1/40. The same Fourier
pair gives |f''(a)|<=4pi^2 int w(t)t^2 dt=2pi^2/3. Equations
(5)--(6) therefore yield

    E-M > 2/5-(80/3+32/171)/400 > 3/10.                   (7)

For a>=4/5 write s=sin(pi*a), c=cos(pi*a). Since u^2<=1/400,
16f/u^2>=6400f, and direct differentiation gives

    6400f-8f''
      = [6400/(pi^2*a^2)+16/a^2-48/(pi^2*a^4)]s^2
          +64sc/(pi*a^3)-16c^2/a^2.

The coefficient of s^2 is at least 6325/(pi^2*a^2), because
48/a^2<=75. Completing the square, and using c^2<=1, proves

    6400f-8f'' >= -1024/(6325a^4)-16/a^2
                 >= -100/253-25.                         (8)

With pi>157/50, (5)--(6) now imply

    (E-M)/u^2 > (8/3)(157/50)^2-25-100/253-32/171
                > 7/10.                                 (9)

Thus the entire small-depth region, including its zero-depth limit,
is covered analytically. This argument uses no grid near the exact
equalities at u=v=0 and integer a.

### Large depths: 1/2<=u<=2

L614 (5),(7) give

    E = 4 int w[(A-2B)^2+4AB(1+c)]
      >=16 int w AB(1+c).

Here B>=1, A>=cosh(pi*t) and 1+c>=0. Thus, for every 0<=v<=u,

    E-M >=16[H(1/2)+F(a,1/2)]-20.                        (10)

The certificate described below covers a in [1/2,4] by 256 closed
intervals with endpoints 1/2+7k/512, 0<=k<=256. On every interval
it encloses the right side of (10) strictly above 3. Its smallest
stored lower endpoint is 3.0598574763299626. This proves (1) throughout
this region independently of v. It is a bound on a complete integral;
no signed pair contribution was deleted.

### Remaining compact region and its certificate

It remains to cover u in [3/64,1/2]. This overlaps the analytic region
because 3/64<1/20. Write v=r*u, 0<=r<=1; since u>0 this covers every
allowed v. The root box is

    (a,u,r) in [1/2,4] x [3/64,1/2] x [0,1].              (11)

`scripts/aggregate-energy/certify_two_packet.py` encloses (3) on each
box and accepts a box only when its lower endpoint is strictly positive.
For exact elementary evaluation it uses

    Re K(a+ib) = [a sin(pi*a)cosh(pi*b)+b cos(pi*a)sinh(pi*b)]
                   /[pi(a^2+b^2)],
    Im K(a+ib) = [a cos(pi*a)sinh(pi*b)-b sin(pi*a)cosh(pi*b)]
                   /[pi(a^2+b^2)],
    F(a,b)=(Re K(a+ib))^2-(Im K(a+ib))^2.                 (12)

The denominator is positive because a>=1/2. In particular, no algebraic
square has been replaced by a modulus square. It evaluates b=u(1-r)
and b=u(1+r), retaining their full ranges, and uses the monotonicity
of H on [0,infinity), proved directly by its positive power series.

The saved certificate is `scripts/aggregate-energy/two-packet-cover.json`.
The complete partition contains 8,553 accepted leaves and 8,552 binary
splits (17,105 evaluated boxes). Every split and leaf is recorded with
its address and exact binary64 endpoints. The script traverses the
entire recorded tree from (11), verifies that each split joins at a
shared interior endpoint, checks that each resulting leaf has exactly
its recorded box, and checks that every stored node was used. It
reports zero uncovered boxes and zero failures. All 8,553 lower
endpoints exceed the exact rational 1/100000; the minimum stored value
is 0.00001517610561320437. These are interval bounds on whole boxes,
not evaluations at selected parameter values.

The rounding and elementary-function enclosures are as follows.

1. After each binary64 addition, subtraction, multiplication or
   reciprocal, the code moves the relevant endpoint one representable
   value outward with `nextafter`. Products use all four endpoint
   products; squares use their correct range, including zero when
   crossed. Divisions have denominators bounded away from zero.
   The recorded runtime has radix 2, 53 mantissa bits and rounding
   mode 1 (nearest). This is a computer-assisted proof in that standard
   arithmetic model, not a formal verification of Python or hardware.
2. Pi is enclosed using the named Machin identity
   pi=16 arctan(1/5)-4 arctan(1/239). Exact `Fraction` arithmetic
   sums 48 and 12 terms, respectively, of the alternating arctangent
   series and includes the next-term remainder. Both rational endpoints
   are saved. Conversion to floating endpoints is rounded outward and
   checked against those exact rationals.
3. Trigonometric endpoint arguments pi*a are reduced modulo 2pi to
   [-pi,pi]. The dyadic endpoints and integer reductions used here are
   exact. Thirty Taylor terms give sine through degree 59 and cosine
   through degree 58. The alternating tails are bounded by
   (22/7)^60/60!<10^(-50); the code adds the wider interval with
   endpoints +/-10^(-49). It also includes every integer/half-integer
   extremum when enclosing cosine/sine on an a interval.
4. To enclose exp(x), 0<=x<=32, the code sums through degree 24
   for y=x/32. The tail is at most 3/25!<10^(-24), since 0<=y<=1
   and e<3. Adding that positive tail interval and squaring five times
   encloses exp(x). Hyperbolic functions use exp and its reciprocal.
   H(0)=1 is treated exactly. For 0<b<1/64, sinh(pi*b)/(pi*b)
   instead uses ten positive terms, through degree 18. Since pi*b<1/16,
   its tail is at most 2/(16^20*21!)<10^(-40), which is added before
   squaring. Larger b use the exponential enclosure. No unbounded
   division at b=0 is performed.

All interval operations account for their own rounding. Rational
checks of the Taylor remainder thresholds and of (7),(9) are included
in the certificate's verification record. All complete leaves and all
256 large-depth cells are tested against the stated rational floors.
The full partition check and computation, rather than a bounded JSON
preview, are the evidence for exhaustion of (11).

Reproduction from the active notebook:

    python3 scripts/aggregate-energy/certify_two_packet.py

The first direct three-dimensional attempt with u<=2 reached its
300,000-box work cap without covering the whole region. Its complete
partial certificate is preserved as
`scripts/aggregate-energy/two-packet-cover-first-incomplete.json`.
That run neither proves the theorem nor refutes it. The reduction
(10), followed by the completed smaller cover, is the proof used here.
The earlier floating diagnostic in L614 is also not a proof input.

Combining (7),(9), the complete cover of (11), (10) and L614's other
cases proves (1), including packet exchange, all allowed multiplicities
and coincident labels. No generalization is inferred from this
bounded-family success.

### Separate proof, code and full-certificate audit, 2026-11-01

The audit checked L614's finite specialization of the assessed Fourier
and norm identities, ordered multiplicities and formulas (1)--(8).
It checked (4) by retaining the sign of cos(2pi*a*t) and bounding the
absolute Taylor remainder, (5)--(9) by exact rational arithmetic and
completion of the square, and (10) by the nonnegative multiplier
1+cos(2pi*a*t). All endpoint cases are included: a=1/2,4,
u=0,1/20,3/64,1/2,2, v=0,u, and either packet exchange. There is
no substitution of |K|^2 for the algebraic square K^2. The complete
source assessment is reused unchanged; no new zeta theorem is imported.

The binary64 code audit checked its interval operations, nonnegative
clamps, positive denominators, exact dyadic argument reductions,
trigonometric extrema, alternating tails, exponential tail and scaling,
and small-argument sinh tail. The exponential tail bound follows from
sum_(j>=0) y^j/(25+j)! <= e^y/25! for 0<=y<=1. For sinh(x)/x
with x<1/16, the successive omitted terms have ratio less than 1/2,
so the stated twice-first-term tail suffices. The trig tails start
after degrees 59 and 58, where their alternating terms decrease.
The true reduced arguments have absolute value <=pi even if their
interval enclosures extend slightly beyond it. Each Taylor polynomial
is enclosed on the full interval; its error is bounded at the true
argument. Exact rational checks certify every displayed tail threshold.

Run the independent checker from the active notebook:

    python3 scripts/aggregate-energy/audit_two_packet.py

It preserves the original certificate, checks its generating-script
hash, reconstructs the entire tree from (11), verifies every split and
leaf box, excludes duplicate/unused nodes and replays both endpoints
of every binary64 bound exactly. It checks all 256 large-depth grid
intervals and their joins. This is full evidence, not a JSON preview.

The checker also evaluates every box in a separately written 50-digit
Decimal interval implementation using ROUND_FLOOR/ROUND_CEILING for
each arithmetic operation. Negation is exact, and multiplication uses
all four endpoint products. Its Machin enclosures use 80 and 24
arctangent terms. It uses 50 trig terms and tail 10^(-100), verified
by (22/7)^100/100!<10^(-100). For exp(x), 0<=x<=16, it uses
y=x/16, terms through degree 50, tail 3/51!<10^(-65), then four
squarings. Its independent H evaluator uses the positive series for
sinh(x)/x through degree 98 throughout 0<=b<=1; here x=pi*b<4,
and the omitted terms have ratio <1/2, giving tail
2*4^100/101!<10^(-90). It then squares the enclosure. Monotonicity
of H and exp justifies endpoint range evaluation. Trig range extrema
are included explicitly. No library sin, cos, sinh or exp is used.

The complete second certificate is
`scripts/aggregate-energy/two-packet-audit.json`. It contains every
compact leaf and large-depth interval with its independent bounds,
exact constants, input and script hashes, runtime and failure fields.
All 8,553 compact leaves and 8,552 splits were used, with zero failures.
The second compact minimum is
0.000015176148530208569449635185843931990874617242661>1/100000;
the large-depth minimum is
3.059857476348987076412124005015021567676574356849>3.
All original binary64 bounds replayed exactly, including their smaller
minima recorded above. The small-depth coefficient is exactly
19194583/27039375>7/10 and the small-spacing lower bound is
1423/4275>3/10. Thus the full bounded verdict passes this audit under
the explicitly stated arithmetic models. Original certificate metadata
still says audit pending because that original evidence is preserved.
This audit does not establish general-family domination, actual-zeta
weights, charge conversion, Xi signs, source novelty or formal correctness.

## Mathlib

Full matching coverage for the two-packet inequality and this certificate
is not checked. Supporting results for real hyperbolic functions,
finite sums, Taylor bounds and interval arithmetic have not been checked
for this particular specialization. Unknown coverage is not evidence
of absence. No Lean or independently verified interval-library proof
is claimed.
