# C750b: A nine-phase positive functional excludes the eight-delay completion

## Hypotheses

Put T=4log(3). Use C750a's complete scalar symbol

\[
 w(t)=\Re\psi(1/4+it/2)-\log\pi
       -2\sum_{2\le n<81}\frac{\Lambda(n)}{\sqrt n}\cos(t\log n),
 \qquad h(t)=(t^2+1/4)^2w(t).
\]

Here psi is the digamma function and Lambda is the von Mangoldt
function. All 31 prime powers below 81 are included. Consider exactly

\[
 H_b(t)=h(t)+\sum_{k=1}^{8}b_k\cos(kTt),\qquad b\in\mathbb R^8.
                                                        \tag{1}
\]

There is no additional constant, change of window or delay, omitted
prime power, RH assumption or positivity premise. The prescribed h
and H_b are scalar functions: this result does not assume or establish
a primitive-range theorem or a representation of the supported Weil
form by H_b.

For the numerical part use the digamma recurrence
[DLMF 5.5.2](https://dlmf.nist.gov/5.5.E2), expansion
[5.11.2](https://dlmf.nist.gov/5.11.E2), and the complex digamma
remainder in [5.11(ii)](https://dlmf.nist.gov/5.11#ii), in the source
version already inspected in assessments861/866. Exact Python integer
arithmetic implements the rational enclosures below; no binary64
transcendental function or floating-point sign decision is used.

## Conclusion

Let t_j=2*pi*j/(9*T), -4<=j<=4, and define the finite positive
functional

\[
 \mathcal L(g)=\frac19\sum_{j=-4}^{4}g(t_j).
\]

Its mass is one, and

\[
 \mathcal L(\cos(kT\,\cdot))=0\quad(1\le k\le8),\qquad
 \mathcal L(h)<-\frac{49}{50}<0.                         \tag{2}
\]

Consequently every b in R^8 has H_b(t_j)<0 at at least one of these
nine points. In particular no b makes H_b nonnegative on the real line.
The full mean enclosure is

\[
 -0.989434654360<\mathcal L(h)<-0.989433156292.
                                                        \tag{3}
\]

This is a local, known-method specialization (REPRODUCTION), not a
claim of progress beyond the inspected sources or a disproof of RH.
It rejects this sufficient scalar family. Neither negative neutral
Weil energy nor failure of a more general completion follows. The
independent rational audit869 below accepts this fixed-family conclusion.

## Proof

### Exact positive functional and its annihilation

Set zeta=exp(2*pi*i/9). For 1<=k<=8, zeta^k is not 1, including
k=3 and k=6. The finite geometric identity gives

\[
 \sum_{j=-4}^{4}\zeta^{kj}
   =\zeta^{-4k}\frac{1-\zeta^{9k}}{1-\zeta^k}=0.
\]

Taking real parts and dividing by nine proves every cancellation in
(2) exactly. The numerical enclosures of T and pi never define the
points or replace this identity by approximate cosine moments.
As an additional integer check, the certificate reduces each polynomial
sum_(j=-4)^4 X^(kj mod 9) modulo Phi_9(X)=X^6+X^3+1. For k=3,6
the quotient is 3; for the other six k it is 1+X+X^2; all remainders
are zero.

This is the finite-support weak-duality specialization of
Basu--Martin--Ryan, *On the sufficiency of finite support duals in
semi-infinite linear programming*, author PDF dated 9 April 2014,
Section 1, pp.2-3 ([primary source](https://www.ams.jhu.edu/~abasu9/papers/finite-support.pdf)).
Only the following elementary applicability argument is needed. If
(1) were nonnegative everywhere, positivity of the nine weights would
give 0<=L(H_b)=L(h)+sum b_k L(cos(kT dot))=L(h). The strict negative
value proved below contradicts this. No compactness, strong duality,
attainment, boundedness of b or exhaustive alternative is invoked.

### Complete scalar evaluation with an explicit remainder

Conjugation of the gamma integral on Re(z)>0, and then of its
derivative, gives psi(conjugate z)=conjugate psi(z) there. Hence w
and h are even and only t_0,...,t_4 need evaluation. For each such t
write y=t/2, a=1025/4 and Z=a+iy. The imported formulas give

\[
 \begin{split}
 m(t)&:=\Re\psi(1/4+it/2)-\log\pi\\
 &=\tfrac12\log(a^2+y^2)-\frac{a}{2(a^2+y^2)}-\log\pi
   -\sum_{r=0}^{255}\frac{r+1/4}{(r+1/4)^2+y^2}
   +\epsilon(t),\\
 |\epsilon(t)|&\le
 \frac{\sec^3(\arg Z/2)}{12|Z|^2}
 <\frac{1}{4(a^2+y^2)}.                                \tag{4}
 \end{split}
\]

Indeed Re(Z)>0, so |arg Z|<pi/2 and sec^3(arg Z/2)/12
<=sqrt(2)/6<1/4. Every recurrence denominator is positive, including
at t=0. Thus (4) is a finite formula with an enclosing error, not an
uncertified asymptotic evaluation. The same source specialization was
used in C750a; its old numerical output is not an input here.

The new exact-integer program is
`scripts/good-frequency/exterior-delay-certificate-867.py`.
It represents [l/2^128,u/2^128] by the two integers l,u. Addition and
negation are exact; multiplication takes the minimum and maximum of
the four integer products and rounds the resulting division by 2^128
outward using integer floor and ceiling. For a strictly positive
denominator [l,u]/2^128 its reciprocal is enclosed by

    [floor(2^256/u), ceil(2^256/l)] / 2^128.

Negative denominators are handled by changing both signs; intervals
meeting zero are rejected. Squares use zero as their lower bound
when the interval crosses zero. Square roots use integer square roots
of l*2^128 and u*2^128, rounding the upper one upward and checking the
two squared endpoints. These operations enclose the corresponding
real ranges by construction and involve no finite-machine overflow.

The elementary-function enclosures are as follows; these details
justify this implementation of the known formulas, not a reproof of
general special-function theory.

* Binary scaling reduces each positive logarithm endpoint x to
  2^e r with 1<=r<=2. For v=(r-1)/(r+1), use
  log r=2 sum_(j=0)^79 v^(2j+1)/(2j+1) plus a remainder of modulus
  at most 2|v|^161/[161(1-|v|^2)]. The checked interval bound
  |v|<=1/2 makes this less than 2^-160. The same series encloses
  log2. The scalar logarithm is increasing, so lower and upper input
  endpoints suffice. Exact scaling uses integer bit lengths.
* Machin's identity pi=16 atan(1/5)-4 atan(1/239) is evaluated with
  64 alternating terms for each arctangent. Its identity follows by
  the tangent addition formula with the angle in (0,pi/2). For the
  checked |x|<=1/4, the omitted tail is at most |x|^129/129<2^-256.
* Cosine is evaluated through degree 64. Viewing this as the
  degree-65 Taylor polynomial (the odd coefficient is zero), its
  real remainder is at most |x|^66/66!. Every complete argument
  t_j log(n) lies in [-4,4]; the program checks this and the exact
  integer inequality 4^66*2^150<66!. Therefore 2^-150 encloses
  the Taylor remainder. No argument reduction is needed.

Each remainder is enlarged outward to the dyadic grid before use.
Rounding intervals may be wider than the analytic remainders; they
are never replaced by them. The certificate records all series domain
bounds. All139 log-base calls satisfy their domain, both arctangent
calls satisfy |x|<=1/4, and all155 cosine calls satisfy |x|<2.777<4.

Integer trial division and repeated integer powers give exactly

    2,3,4,5,7,8,9,11,13,16,17,19,23,25,27,29,31,32,
    37,41,43,47,49,53,59,61,64,67,71,73,79.

For n=p^r the program encloses log(p)/sqrt(n), log(n), and the whole
term 2log(p)cos(t_j log(n))/sqrt(n). It subtracts the sum of all31
such terms from (4), and then multiplies by the enclosing nonnegative
factor (t_j^2+1/4)^2. The full artifact
`scripts/good-frequency/exterior-delay-certificate-867.json` records
all weights, all155 arithmetic terms, all1280 recurrence terms, their
sums, errors, final values and exact annihilation data. Its common
dyadic denominator makes every stored endpoint an exact rational.
The shorter summary is for inspection, not a replacement certificate.

The following deliberately widened rational enclosures follow; their
finite decimal endpoints denote exact rationals. The five final values,
the full exact annihilation records and the strict mean comparison were
inspected. The program's source and enclosure reasoning above determine
the finite certificate; raw intermediate decimals are not used as a
substitute for that reasoning.

| j | enclosure of t_j | lower bound for h(t_j) | upper bound for h(t_j) |
|---|---|---:|---:|
| 0 | 0 | -2.254364 | -2.254363 |
| 1 | (0.158866714854, 0.158866714855) | -2.407616 | -2.407614 |
| 2 | (0.317733429708, 0.317733429709) | -2.526847 | -2.526845 |
| 3 | (0.476600144563, 0.476600144564) | -1.390252 | -1.390249 |
| 4 | (0.635466859417, 0.635466859418) | 2.999439 | 2.999443 |

In particular, using weight1/9 at zero and weight2/9 at each positive
node, the table alone gives

\[
 \mathcal L(h)
 <\frac{-2254363+2(-2407614-2526845-1390249+2999443)}{9000000}
 =-\frac{8904893}{9000000}<-\frac{49}{50}.
\]

The tighter dyadic accumulation gives (3). This proves (2) and hence
the asserted obstruction for every real coefficient vector b.

Reproduce from the active notebook directory:

```sh
python3 scripts/good-frequency/exterior-delay-certificate-867.py
python3 ../scripts/loop/inspect_json.py scripts/good-frequency/exterior-delay-certificate-867.json --pointer /result --full
```

The initial bounded proposal, retained as
`scripts/good-frequency/exterior-delay-proposal-867.json`, was expressly
nonrigorous. Its first, unshifted nine-phase proposal succeeded, so no
period translations were tried. None of its approximate values enters
the proof. The exact certificate has an empty failure list. It requires
no real-line tail estimate because a finite positive functional already
contradicts the necessary pointwise inequalities.

### Scope of the stop

The nine-point measure is not asserted to have the form
|F_u(t)|^2 dt for a compactly supported smooth primitive u. Therefore
its negative value supplies no negative supported quadratic form.
No primitive-surjectivity, endpoint-trace or exterior-annihilation
identity is needed for this scalar obstruction, and none has been
quietly established here. The previously audited coarse-screen stop
C750a remains separate. More general representatives, complete neutral
positivity, non-neutral directions, global assembly and actual-Xi
mixed positivity remain unresolved.

### Independent rational audit — 14 November 2026, step869

The invocation-start SPECIALIZE assessment867, separately approved868,
covers exactly this audit. The full proof, complete certificate and its
producer were read, with C750a's symbol and L744(6)-(8) for normalization
and scope. The known scalar and finite weak-duality inputs above suffice;
no new theorem about primitive ranges or positive forms is imported.

The geometric identity is valid for all eight k: zeta^k!=1 even when
k=3,6. The nine indices form a complete residue system modulo9. An
independent integer multiplication, rather than the producer's polynomial
division, checks that the phase polynomial is Phi9 times3 for k=3,6
and Phi9 times(1+X+X^2) otherwise. Its real part therefore vanishes
exactly. Positivity of the weights and their total mass1 imply that a
negative mean forces a negative node for every unrestricted b. No
approximate cancellation or bound on b enters this inference.

The nonmutating audit is `scripts/good-frequency/audit-869.py`, with
full evidence `scripts/good-frequency/audit-869.json`. It does not import
or execute the producer. It parses every dyadic endpoint as a Fraction,
performs rational endpoint operations, and rounds outward to the dyadic
grid using exact floor/ceiling. All original128-bit records match
exactly, including every stored decimal enclosure, all31 weights and
logarithms, all155 angles/cosines/signed complete terms, all1280
recurrence terms, five sums/factors/values, constants, domains and mean.
Independent factorization classifies each integer2,...,80, yielding
precisely the31 listed prime powers, each with Lambda(p^r)=log p. The
coefficient2, subtraction from the archimedean part, and positive square
factor are retained in every node calculation. The published five-row
table and its exact rational comparison also pass.

This complete rational reconstruction alone would still share the
producer's evaluation scheme. A second enclosing calculation uses
192-bit Fraction intervals, direct powers for the series rather than
their running-term recurrences,100 logarithm terms,80 arctangent terms,
cosine through degree80, and the digamma shift512 (Re Z=2049/4).
For |v|<=1/2, the logarithm tail is bounded by
2(1/2)^201/[201(1-1/4)]<2^-200. For |x|<=1/4 the alternating
arctangent tail is at most (1/4)^161/161<2^-320. The degree81 Taylor
remainder for cosine is at most4^82/82!<2^-220. Each radius is itself
rounded upward before widening, so a radius below the grid spacing
is not silently discarded. Exact endpoint squaring checks sqrt bounds;
reciprocals exclude zero, and logarithm scaling is selected by rational
comparisons. These are alternate implementations of the same cited
analytic formulas, not independent special-function theory or formal
verification.

For both digamma shifts every recurrence denominator is strictly
positive. The shifted argument is in the open right half-plane, where
the imported complex remainder gives sec^3(arg Z/2)/(12|Z|^2).
Since sec^3(arg Z/2)/12<=sqrt(2)/6<1/4, the implemented bound
1/(4|Z|^2) applies also at t=0. The recurrence has a minus sign;
Re log Z=log(|Z|^2)/2 and Re(1/Z)=Re Z/|Z|^2. Conjugation makes
h even, justifying exactly the multiplicities1,2,2,2,2 and division9.
No real-axis-only digamma remainder or omitted prime-power tail is used.

All3920 audit checks pass, with no failure. Each alternate final-value
interval, and its mean interval, is strictly contained in the corresponding
original interval. In particular the complete original mean upper endpoint
is exactly

    -336686656333279602935731856070137307396 / 2^128,

which is strictly less than-49/50, with margin greater than9/1000.
The original two-sided enclosure (3) and fixed-family conclusion (2)
are accepted without changing their bounds. The audit certificate stores
all checks, the original artifact hash and the alternate exact endpoints;
it does not treat a JSON preview or sampled central value as proof.

Reproduce with `python3 scripts/good-frequency/audit-869.py`. Its output
reports pass/fail, actual and required bounds and the evidence path.
The full matching Mathlib theorem and a formal verification remain
unchecked. This is REPRODUCTION/local verification of an existing
obstruction, not a new discovery beyond the inspected sources. The
finite point measure has no asserted smooth Fourier-square realization;
the supported neutral form and all global RH gaps remain open.

## Mathlib

Full matching theorem and formal verification of this exact-integer
certificate: not checked. The finite geometric identity and rational
interval arithmetic are standard supporting mathematics; their
availability would not by itself constitute the present complete
symbol certificate. No absence claim or formal-proof claim is made.
