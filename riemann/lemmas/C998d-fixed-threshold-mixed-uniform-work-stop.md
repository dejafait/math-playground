# C998d: A fixed-threshold mixed prescription fails the uniform work test

## Hypotheses

Keep C998a's six exact frozen parity densities, a=log(3)/4, all modes
0..255, exact neutral completion and pinned652 archive. Retain its
analytic-response/arithmetic/source-to-Xi/whole-core/unreplayed c_*
qualifications. No inverse, residual-norm or signed comparison is assumed.
The point-input contract is |t-T*2^-1024|<=2^-1024 and
a*2^-80<=t<=a, certified by the caller. Write s=t/a and

    z0=n*pi*s/2,   z1=n*pi*(1+s)/2,   1<=n<=255.

Test the following EXPLICIT prescriptions, not all mixed algorithms.
The threshold H is64,128 or256; fractional precision P is256,512 or1024.
Branch on the represented argument y: use convergent series for y<H,
and finite auxiliary f,g expansions otherwise. At each small first
argument compute Si(y), C(y)=Ci(y)-gamma-log(y), sin(y),cos(y) together
with N terms and the two unconditional updates

    A_0=y, B_0=1,
    A_(j+1)=round[-A_j*y^2/((2j+2)(2j+3))],
    B_(j+1)=round[-B_j*y^2/((2j+1)(2j+2))],    j=0,...,N-2.  (1)

Each update forms an integer product and a division (or a shift if
applicable). No tabulated whole-function values, mode pruning, cached
query answers, argument-reduction replacement of these recurrences,
or coefficient-weighted error reallocation is part of this prescription.
All modes are shared across the six outputs. N may depend on the mode
and an argument bin, but must be at most1024. The scalar mode transform
needs the first argument's sine and cosine as well as both primitives.

The small-branch TRUNCATION policy is an absolute geometric tail
certificate for every primitive, with allowance epsilon=2^-80. In
particular its cosine certificate includes the first omitted term

    T_N(y)=y^(2N)/(2N)!,                              (2)

and therefore requires T_N(y)<=epsilon. For example the usual bound
T_N/(1-D_N) with D_N=y^2/((2N+1)(2N+2))<1 has this necessary condition.
This is a policy for certifying truncation, not a necessary condition
for the actual signed series remainder or for whole-density accuracy.
Rounding, input, constants and assembly require separate allowances.

For the witness interval 1/2<=s<=513/1024 require |y-z0|<1/8 for each
first argument. This is a deliberately weak design requirement, not an
implemented argument-error theorem. Any eventual point evaluator must
justify its actual argument errors; failure to do so does not rescue
this prescription. Conditional on this requirement the cost obstruction
below is independent of how that accuracy is obtained.

The work test is setup plus the WORST CASE over lists of11174 admissible
query codes, with ceiling100000000 integer addition/subtraction,
multiplication, division, shift or comparison operations on registers
of at most16384 bits. It is the uniform service test specified in
assessment661. It is not a lower bound for one particular nonrepeating
outer quadrature-node list, which has not been evaluated. The prescribed
service does not reuse a previous query answer. Setup and every remaining
calculation have nonnegative cost. If a register cap fails, the proposed
algorithm already fails the stated test independently of the count.

Invocation-start SPECIALIZE assessment661 licenses this REPRODUCTION.
Import the standard series from NIST DLMF, version1.2.8,15September2026,
[6.6.5-6](https://dlmf.nist.gov/6.6); definitions/branches are
[6.2.9,11-13](https://dlmf.nist.gov/6.2#ii). The absolute geometric-tail
method is Johansson, *Computing hypergeometric functions rigorously*,
[arXiv:1606.06977v2](https://arxiv.org/pdf/1606.06977v2), Section4.1,
Theorem1 and its scalar proof, with ratio strictly below1. These general
results are not reproved. Only positive real arguments occur.
The ready large branch is DLMF[6.2.19-20](https://dlmf.nist.gov/6.2#E19)
and [6.12.5-8, final remainder paragraph](https://dlmf.nist.gov/6.12#ii):
finite f,g expansions have first-omitted-term magnitude bounds for
|arg z|<=pi/4 and the omitted term's sign on the positive axis. Their
applicability and the gamma setup sources are recorded661, but no large
branch value, error or work property is needed in this early cost proof.

## Conclusion

All three threshold choices, at every allowed P, fail this uniform work
test, conditional on the stated argument accuracy. The mandatory small
first-argument updates for modes41..81 alone require at least

    9840 operations/query,
    109952160 operations for the worst-case11174-query service. (3)

The latter exceeds the ceiling by9952160, before setup, all other modes,
second arguments, gamma/log/pi, trigonometric assembly and output sums.
STOP these prescriptions before a batch. This is an informative local
cost obstruction, not a lower bound for all mixed algorithms or for the
actual as-yet-uncomputed outer-node list. In particular a cheaper uniform
primitive tolerance, changed summation/argument reduction, joint
coefficient error allocation or direct residual integration is not ruled
out. No repeated retuning is licensed by this result.

No whole-density2^-53 error theorem, Euler-constant enclosure, mixed
normalization/rounding proof, complete register upper bound, point value,
residual norm, inverse pairing, signed S3 result or RH conclusion is
established. The cost stop makes completion of those errors unnecessary
for these prescribed service algorithms. This result has not received a
separate critical audit.

## Proof

### 1. Applicability and simultaneous small branches

C998a(4),(6) gives each density as the appropriate parity part of a
finite cosine sum, with exact neutral coefficients. For a nonzero mode,
substitute u=t+r in its integral over0<=r<=a and use the cosine addition
formula. The resulting integral is

    cos(z0)[Ci(z1)-Ci(z0)]+sin(z0)[Si(z1)-Si(z0)].       (4)

Both arguments are positive, and the zero mode is separately
log((a+t)/t). This checks which first-argument functions (1) computes;
it does not use C998c's unaudited numerical error conclusion. Inserting
Ci=gamma+log+C on both small arguments gives that file's gamma-free
form. Inserting different representations on mixed branches would
require the gamma, log and pi/2 bridge; it is NOT omitted from a claimed
successful evaluator here. We stop before constructing that evaluator.
The C998a parity and exact completion do not alter (4)'s scalar arguments.

For every n=41,...,81 and every s in[1/2,513/1024], the standard strict
bounds3<pi<22/7 and |y-z0|<1/8 give

    y > 3n/4-1/8 >=245/8 >30,
    y < (n/2)(22/7)(513/1024)+1/8
      <=(81/2)(22/7)(513/1024)+1/8 <64.              (5)

The final rational comparison is performed exactly in the certificate
for EVERY one of these41 modes. All nine threshold/precision pairs
therefore take the small branch for their first arguments simultaneously,
throughout this interval. It is not a sum of incompatible branch maxima
or a conclusion drawn from a sample. The free coefficients of all41
modes are nonzero in each frozen column, checked exactly against the
complete654 dyadics; nonetheless the recurrence count uses the explicit
unpruned policy, rather than an assumed lower bound for all mode methods.

The interval is contained in[2^-80,1]. Every true t=a*s in it admits an
integer T at absolute distance at most2^-1025 from t, so the input-code
contract is nonempty. There are vastly more than11174 such codes: its
t-width is a/1024>1/4096, hence over2^1012 grid intervals. The witness
can therefore supply distinct requests as well as repeated requests.
This establishes a worst-case-service witness, without identifying any
of the future outer quadrature nodes with these requests.

### 2. A necessary order for this tail policy

For fixed z>0, the ratios

    T_(N+1)(z)/T_N(z)=z^2/((2N+1)(2N+2))

strictly decrease with N. Thus the finite sequence T_0,...,T_60 first
increases and then decreases, with either part possibly empty. Its
minimum is one of its endpoints. At z=30, T_0=1 and exact integer
comparison gives

    2^80 *30^120 >120!,
    T_60(30)>2^-80.                                  (6)

Consequently T_N(30)>2^-80 for ALL0<=N<=60. Each T_N is nondecreasing
in positive z; for N=0 it is constant. Hence none of these N satisfies
the necessary tail-policy condition (2) when y>30. The certificate
additionally checks every one of the61 comparisons and stores every
full rational term and excess over2^-80, not decimal estimates.

Every first argument in (5) therefore requires N>=61. This does not
claim the actual alternating remainder exceeds the tolerance or that
such a tolerance is necessary for any full density. It proves failure
of the declared absolute-tail policy at smaller orders, which is the
only order fact used in the cost count.

### 3. Work lower bound and stopping boundary

For N>=61, (1) performs at least60 updates for A and60 for B. Each
specified update has a multiplication and a division/shift, so at
least240 charged operations occur for each of the41 first arguments.
This gives41*240=9840 per request throughout the witness interval.
This is already shared work across all six densities; it is not
multiplied by the number of columns or parities. Table lookup, branch
comparisons and all function accumulators are omitted only to make
the lower bound smaller. Their costs cannot offset it.

Taking11174 admissible requests in this interval proves(3), and
109952160>100000000 stops each tested uniform-service prescription.
This is a genuine LOWER bound for its explicit required operations,
not a loose upper bound mistaken for infeasibility. No claim is made
that every possible query list attains it. Neither register feasibility
nor a complete upper cost bound is inferred from counting operations.
If the register condition or the weaker argument-accuracy requirement
cannot be implemented, that is an additional failure, not missing
evidence needed for this conditional exclusion.

The planning command is

    python3 scripts/separation-seven/mixed-finite-cosine-work-662.py

It saves the complete certificate
`scripts/separation-seven/mixed-finite-cosine-work-662.json`:114 checks,
no failures. It pins the652 archive and654/655/660 certificates, reads
all relevant frozen dyadics, checks all41 argument intervals and all61
excluded orders, and records all nine threshold/precision cases.
The symbolic reasoning above remains essential; a passing script alone
does not prove applicability or the operation interpretation. No point
or norm batch is run. Prior652/657/660 stops and unfinished work remain.
All independent outer/node/forcing/scalar/projection/norm-width,
higher/mixed-endpoint,C744q/H2, non-neutral and global gaps remain open.

## Mathlib

Full matching coverage of this frozen-data conditional algorithm/work
statement has not been checked. No absence or formal-verification claim
is made. The primary numerical series/tail theorems are cited above;
the local exact inequalities and recurrence counts are supplied in full.
