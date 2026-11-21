# C750n: The fixed sine64 negative-symbol loss certificate fails

## Hypotheses

Use precisely C750m's complex H=L2((-b,b)), zero extension, Fourier
convention, fixed b=log(101)/2, all35 coefficients c_n=2Lambda(n)/sqrt(n),
joint symbol Psi=m-p, A, T=2pi exp(A+2), beta=2-1/T, P=P64 and Q=I-P.
In particular m(t)=Re psi(1/4+it/2)-log pi and
p(t)=sum_(2<=n<101)c_n cos(t log n). The projection is unchanged.
Let c(x)=cosh(x/2), s(x)=sinh(x/2), and define on ALL of H

    w(t)=(beta-Psi(t))_+, |t|<=T,
    <N_- f,f>=integral_(-T)^T w(t)|F_f(t)|^2 dt/(2pi)
                   +2|<f,s>|^2.                         (1)

The accepted C750m complex normalization/domain audit and L744(8)'s
scalar digamma bounds are inputs. Reuse the ready source assessment
1164, completed1165, at its exact COVERED_TARGET; this is its one
fixed complementary-witness test, not a new support/cutoff/head test.

## Conclusion

For the unit vector phi=phi_115 in the UNCHANGED QH,

    <N_- phi,phi> >27/10>2>beta,
    ||Q N_- Q|| >27/10.                                 (2)

Thus the sufficient condition ||Q N_- Q||<beta cannot hold at these
fixed parameters. This is a local informative negative result from a
source-supported specialization (RESEARCH/REPRODUCTION), not a novelty
claim or a disproof of RH. It does NOT establish a negative direction
for R, E, QRQ or the actual-Xi form. Coupling, retained-head positivity,
all-support signs and Xi transfer remain unresolved.

The finite arithmetic certificate is part of the proof below. The separate
audit1168 in Section5 accepts its implementation and interpretation.

## Proof

### 1. Bounded object and the proposed sufficient order comparison

C750m Sections1-2 show that Psi is continuous, real and even on the
finite interval [-T,T]. Hence w is bounded and nonnegative. With zero
extension and Plancherel, (1)'s integral is a bounded positive form
on H, of norm at most ||w||_infinity. Its pole has norm2||s||^2.
It therefore defines a bounded positive self-adjoint N_-. Its kernel,
if needed, is the complete expression

    n(x,y)=integral_(-T)^T w(t)exp(it(x-y))dt/(2pi)+2s(x)s(y).

Fubini is justified by finite T, bounded w and finite spatial support;
this is the same kernel construction as C750m, with a bounded new
symbol. No nonlinear operation on a compressed operator is used.
The standard source for bounded Borel symbol order is Teschl,
*Mathematical Methods in Quantum Mechanics*, GSM99, author version
12February2009, Theorem3.1/(3.20)-(3.21), printed pp90-91,
https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf .
The source hypotheses hold on the full Fourier space before zero
extension/compression; compression preserves its quadratic inequality.

Indeed h=Psi-beta satisfies h>=-w pointwise. C750m(2),(7) give,
including both complex pole components,

    R(f)>=beta||f||^2-<N_- f,f>+2|<f,c>|^2
          >=beta||f||^2-<N_- f,f>, f in H.              (3)

Together with the accepted E>=R on V, a norm below beta would supply
a complementary lower resource. Conversely, failure of that norm
condition is only failure of this sufficient resource: (3) is not an
upper bound on R. N_- is not the spectral negative part of K or R.

### 2. Fixed witness and a retained positive frequency interval

Put L=log101, alpha=115pi/L. Then

    phi(x)=b^(-1/2)sin(115pi(x+b)/(2b))
          =-b^(-1/2)cos(alpha x).

It is real even, has norm1, and is orthogonal to phi_1,...,phi_64.
Thus Qphi=phi, and <phi,s>=0 EXACTLY by parity. The odd pole is
retained in (1) and evaluates to zero for this particular witness.
The witness is also in V, since its endpoint-zero extension is H1;
no domain assertion about arbitrary members of H is required.

Write sinc(u)=sin(u)/u, with its continuous value1 at0, and

    G(t)=sinc(bt-115pi/2)+sinc(bt+115pi/2).

Direct integration of the cosine, equivalently C750m(13), gives
F_phi(t)=-sqrt(b)G(t). In particular |F_phi(t)|^2=bG(t)^2.
The removable singularity near alpha is handled by sinc's series,
never by division by t-alpha.

C750m Section3 proves T>100000 and 2<b<5/2. Consequently
beta>beta0:=199999/100000 and [77,79] is inside [0,T]. L744(8)
gives, throughout this interval,

    m(t)<=log(t/(2pi))+2/t^2.

Define the REAL scalar function, retaining all35 terms jointly,

    v(t)=beta0-log(t/(2pi))-2/t^2+p(t).

Then w(t)>=(v(t))_+. Since the original w and |F_phi|^2 are even,
and the entire omitted part of (1)'s integral is nonnegative,

    <N_- phi,phi>
      >= integral_77^79 (v(t))_+ bG(t)^2 dt/pi.           (4)

This lower bound uses no asserted frequency cutoff of F_phi, no
approximation of the full comb by A inside the clip, and no omitted
negative term. No estimate on the rest of [-T,T] is needed for (4).

### 3. Certified lower rectangles for the whole retained interval

Here and below every interval endpoint is a rational. The executable
certificate is `scripts/sine64/negative_loss_witness_1166.py`; its
complete output is `scripts/sine64/negative-loss-witness-1166.json`.
It uses only Python integer arithmetic and Fraction; no floating-point
elementary function or external numerical library enters the bounds.

Use2000 adjacent cells of width h=1/1000, midpoints
t_k=77+(2k+1)/2000, k=0,...,1999. Their union is exactly [77,79].
Certified coefficient intervals give

    D:=1+sum c_n log(n)<109.                             (5)

For77<=t<=79, |-1/t+4/t^3|<1; hence |v'(t)|<=D<109.
By Cauchy--Schwarz applied to the Fourier integral and ||phi||=1,

    |G'(t)|=|F_phi'(t)|/sqrt(b)
             <=sqrt((integral_(-b)^b x^2 dx)/b)
             =sqrt(2/3)b<3.                             (6)

For each k the certificate computes intervals V_k containing v(t_k)
and Z_k containing G(t_k), and an interval B containing b. Put

    a_k=max{0, inf V_k-109/2000},
    d_k=max{0, dist(0,Z_k)-3/2000}.

Equations(5)-(6), the Lipschitz property of absolute value and
positive part, and |t-t_k|<=1/2000 show on the ENTIRE cell that
(v(t))_+>=a_k and |G(t)|>=d_k. Thus (4) is bounded below by

    sum_(k=0)^1999 h*(inf B)*a_k*d_k^2/(sup Pi),          (7)

where Pi is the certified interval for pi. No quadrature convergence
assumption or omitted mesh error is used: these are lower rectangles.
Every summand is nonnegative. The program rounds the summands and
their finite sum outwards once more, so its resulting lower endpoint
is at most (7). All2000 cells and all35 prime powers are recorded.

### 4. Enclosure primitives and exact finite evidence

The common grid is S=10^40. An interval is stored as two integer
endpoints divided by S. Addition, subtraction and multiplication use
the exact endpoint extrema, rounded down/up by integer floor/ceiling;
division uses all four endpoint ratios and asserts that its denominator
does not contain zero. Square root uses isqrt of the endpoint times S,
with ceiling adjustment at the upper endpoint. These rules enclose
the corresponding real operations, including when factors have mixed
signs; dependency can enlarge intervals but cannot invalidate them.

The complete elementary-function bounds are as follows.

* Machin's identity pi=16atan(1/5)-4atan(1/239), with40 and12 terms
  respectively of sum_(k>=0)(-1)^k/((2k+1)n^(2k+1)). Each omitted
  alternating tail is bounded in absolute value by the next term.
* For log(x), range reduction by exact powers of2 puts x in [1,2];
  assertions check those interval endpoints. With q=(x-1)/(x+1),
  use50 terms of 2sum_(k>=0)q^(2k+1)/(2k+1). The positive tail is
  at most 2(1/3)^101/[101(1-1/9)]. The same formula gives log2.
* For sin/cos, reduction by an integer multiple of the enclosed2pi
  preserves the exact function. The reduced interval is ASSERTED
  to lie in [-4,4]. Twenty-six terms are evaluated by interval Horner
  arithmetic. The sin remainder is <=4^53/53! and the cos remainder
  <=4^52/52!, by Taylor's theorem including the intervening zero
  coefficient. For sinc on [-4,4], use26 terms
  sum_(k=0)^25(-1)^k u^(2k)/(2k+1)! with remainder <=4^52/53!;
  this follows by integrating the corresponding cos Taylor bound
  in sinc(u)=integral_0^1 cos(ru)dr.

The code uses sinc's direct polynomial for bt-115pi/2, whose interval
is checked inside [-4,4] in every cell. It uses the reduced sine and
division for bt+115pi/2, with denominator checked away from zero.
These cover the complete G, rather than just its resonant term.
All range-reduction choices are integer operations and their domains
are verified. The true inputs are inside the intervals, so a tail
bound on their stated real domain remains valid despite any outward
extension in subsequent interval arithmetic.

Reproduction command:

    python3 scripts/sine64/negative_loss_witness_1166.py

The full finite certificate checks that there are exactly35 terms,
b<5/2, A<34, D<109, exact cell coverage, and that the resulting lower
endpoint exceeds27/10. All checks pass; no failures. The exact final
lower endpoint is

    27170280682740257375754196114320989666474 / 10^40
       > 27/10.

It is recorded in the certificate's `complete_lower_integral`; its
comparison with27/10 is an integer comparison, not a decimal preview.
The separate `scripts/sine64/verify_negative_loss_assembly_1166.py`
checks ALL2000 cell reductions, midpoint coverage, lower products and
the exact complete sum from the recorded primitive intervals. Its full
certificate is `scripts/sine64/negative-loss-assembly-verification-1166.json`.
This is an assembly check; it does not independently certify the
elementary-function enclosure implementation. Together with (4)-(7)
and the enclosure justification above, this proves the first inequality in
(2). Bounded self-adjointness, Qphi=phi and ||phi||=1 give
||QN_-Q||>=<QN_-Qphi,phi>=<N_-phi,phi>, proving the norm claim.

Only this loss certificate is stopped. Positive symbol energy and
the even pole discarded by (3) may compensate the loss; the witness
does not show that R or E is negative. No head assembly, retuning,
spectral-floor assumption, all-support inference or RH premise is used.

### 5. Independent full enclosure and interpretation audit1168

This separate audit uses the unchanged SPECIALIZE assessment1166,
approved1167. It accepts (2), without increasing the bound or claiming
a discovery beyond the source-supported local specialization. The
original1166 proof and its evidence are preserved. The following verifies
the analytic primitives as well as the complete finite assembly.

**Real branch and elementary sources.** Put a=atan(1/5), d=atan(1/239)
on their principal real branches. Integration of 1/(1+x^2) gives
5/26<a<1/5 and 0<d<1/239. Thus

    0<4*(5/26)-1/239 < 4a-d <4/5<1<pi/2.

The elementary pi>2 suffices for the last inequality. Rational tangent
addition gives tan(2a)=5/12, tan(4a)=120/119, and

    tan(4a-d)=(120/119-1/239)/(1+120/(119*239))=1.

All intermediate denominators are nonzero; 0<4a<4/5<pi/2. Uniqueness
of the tangent on (-pi/2,pi/2) gives 4a-d=pi/4, proving the exact
Machin identity used by BOTH implementations. No multivalued addition
identity selects a branch implicitly. The series inputs1/5 and1/239
are real in (0,1), so the alternating remainder is bounded by the
first omitted term, with index equal to the stated term count.
Supporting primary formulas are NIST DLMF v1.2.8,
[4.24.3](https://dlmf.nist.gov/4.24.E3) and
[4.24.15](https://dlmf.nist.gov/4.24.E15); the range argument above
supplies the branch qualification left open by the latter formula.

The odd-power logarithm formula is DLMF
[4.6.4](https://dlmf.nist.gov/4.6.E4). After the exact positive power-of-two
reduction, every actual argument is in [1,2], so q is in [0,1/3].
For any count N the omitted positive tail is bounded by
2*(1/3)^(2N+1)/((2N+1)*(1-1/9)). This is the geometric majorant
obtained by replacing each omitted denominator by2N+1. The generator
uses N=50; its last included exponent99 and first omitted exponent101
are correct. The independent audit uses N=90 and exponent181.
Interval extension of q can only enlarge the finite polynomial
enclosure; the remainder concerns the true q in the verified domain.

DLMF [4.19.1](https://dlmf.nist.gov/4.19.E1) and
[4.19.2](https://dlmf.nist.gov/4.19.E2), with real Taylor's theorem,
justify the trigonometric bounds. The original sine polynomial has
degree51, and adjoining its zero degree52 coefficient gives the
remainder |r|^53/53!. The cosine polynomial has degree50, and its
zero degree51 coefficient gives |r|^52/52!. For sinc, integrate that
cosine remainder in sinc(u)=integral_0^1 cos(ru)dr, giving
|u|^52/53!, valid also at u=0. Hence all three original bounds on
[-4,4] are correct. An arbitrary chosen integer k is sufficient for
sin(x)=sin(x-2k*pi), and likewise for cosine: it need not be the
nearest integer. The code encloses the resulting argument and checks
its domain in every invocation. The nonresonant sinc denominator is
checked away from zero; the resonant sinc uses no division by u.
These are applicability/remainder checks for standard identities,
not reproving the cited functional calculus or digamma theorem.

**All integer primitives.** At a positive grid scale S, floor(a/S)
and -floor(-a/S) give the correct directed product bounds; exact
extrema of the four endpoint products cover every mixed-sign case.
For division the four endpoint ratios give the extrema when the
denominator interval excludes zero. Python floor division and
-((-a)//b) are respectively floor(a/b) and ceil(a/b), including
negative b. Addition/negation are exact on the grid. The constructor
applies floor/ceiling to each exact rational endpoint. For square
root, isqrt(lo*S)/S is below sqrt(lo/S), and adding one to the upper
integer root exactly when hi*S is not square bounds sqrt(hi/S)
above. Each operation therefore encloses the corresponding real
operation. All zero exclusions and range assertions pass in the
complete rerun; no float or rounded elementary library value enters.

For an independent verification, rather than trusting rerun identity,
`scripts/sine64/audit_negative_loss_enclosures_1168.py` recomputes
all coefficient, parameter and midpoint enclosures on the grid10^-70,
without importing the generator. It uses65/20 arctangent terms,
monotone endpoint logs with90 terms, direct50-term trigonometric
recurrences rather than Horner evaluation, and integer roots of n*10^140
for sqrt(n). Its arbitrary reduction gives |r|<=7, asserted at every
call. Sine has last degree99 and zero degree100, cosine last degree98
and zero degree99; Taylor remainders are7^101/101! and7^100/100!.
Integrating the latter gives the sinc remainder7^100/101!.
The same exact directed interval rules verified above apply on this
different grid. Monotonicity of the real logarithm justifies enclosing
an input interval using the lower endpoint's lower log and upper
endpoint's upper log, after exact rational range reduction.

The audit separately factors every integer2,...,100 by its smallest
divisor and tests whether only that prime divides it. This reproduces
the entire35-term list, not merely its length. Every recomputed c_n,
log(n), pi,L,b,A,D,beta0 interval is contained in its saved1166 interval.
For EVERY one of the2000 consecutive midpoint records the recomputed
v and G intervals are contained in the original V_k and Z_k, by exact
integer cross-multiplication of both endpoints. Full values and all
per-cell tests are saved in
`scripts/sine64/negative-loss-enclosure-audit-1168.json`. Its nine
global checks pass, with no failed term or cell; domain failures
would raise an assertion and prevent completion. This independently
certifies the transcendental enclosures, not just decimal agreement.

**Witness, constants and all rectangles.** In the normalized Dirichlet
sine basis, index115 exceeds64 and odd-index reflection gives exactly
-cos(alpha*x)/sqrt(b). Orthogonality and its norm1 follow by integrating
the Dirichlet sines on a length2b interval. It is real even, so the
full odd pole vanishes on this witness, whereas the even pole is not
given a negative sign or dropped from an asserted upper estimate.
Its zero-endpoint extension has an L2 weak derivative; Plancherel and
log(2+|t|)<=C*(1+t^2) prove its membership in V. Direct integration
gives F=-sqrt(b)*G including BOTH sinc terms. Evenness of the full
comb and gamma symbol and of |F|^2 gives exactly the factor b/pi
in (4). C750m's T>100000 yields beta>beta0 and covers [77,79].
L744(8) is used in the upper direction for m, hence in the lower
direction for beta-Psi; monotonicity of positive part preserves it.

On [77,79], |-1/t+4/t^3|<1, and each c_n and log(n) is positive.
Thus D<109 implies the displayed bound on |v'|. For the other
Lipschitz bound, differentiating the finite Fourier integral and
Cauchy--Schwarz give |G'|<=sqrt(2/3)*b. Since b<5/2 its square is
less than25/6<9, proving |G'|<3. The cell half-width1/2000 therefore
pays109/2000 and3/2000, respectively. Distance to zero of Z_k bounds
|G(t_k)| below, including the case when Z_k crosses zero. The clip
and absolute value are1-Lipschitz, so each lower rectangle is valid
on its whole closed cell; shared endpoints have measure zero.

The rerun of `negative_loss_witness_1166.py` passes all six checks.
The independent exact assembly program1166 checks each actual index,
midpoint, clipped lower value, absolute lower value and rounded lower
product, then sums all2000 lower endpoints exactly. Its six global
checks pass. The full check/failure objects of all three certificates
and the complete final lower endpoint were inspected. The exact
lower numerator remains27170280682740257375754196114320989666474
at scale10^40. Subtracting27*10^39 leaves the positive integer
170280682740257375754196114320989666474. Thus the strict >27/10
comparison is certified, with every retained cell and both sinc terms
accounted for; no preview or floating approximation is evidence here.

**Order and scope.** Finite T, continuity of Psi, Plancherel and
bounded odd moment give bounded positive self-adjoint N_- on the
full complex H. Pointwise h>=-(-h)_+ on the uncompressed Fourier
space gives (3) after compression; the even pole adds a nonnegative
term. For unit Qphi=phi, the operator norm is at least its expectation,
which is >27/10>beta. This is precisely failure of the proposed norm
certificate. It is not a spectral negative part calculation, a
negative direction for R/E, or all-support/Xi positivity. C750m and
L744 are the only direct local mathematical inputs, so DAG edges are
unchanged. PROOF.md is unchanged because the mathematical argument and
bound have not changed; the current audit status is recorded here and
in PROGRESS.md.

Reproduction commands (run in this order):

    python3 scripts/sine64/negative_loss_witness_1166.py
    python3 scripts/sine64/verify_negative_loss_assembly_1166.py
    python3 scripts/sine64/audit_negative_loss_enclosures_1168.py

## Mathlib

Full matching coverage for this fixed clipped-symbol compression and
its certificate is not checked. Plancherel, bounded-functional-calculus
order, Hilbert-Schmidt kernels, Taylor remainders and integer interval
arithmetic are standard supporting inputs, not an identified matching
Mathlib theorem. No Lean verification is claimed. The source-scope
assessment is1164/1165 and the separate approved audit scope is1166/1167;
audit1168 verifies the local specialization without a Lean claim.
