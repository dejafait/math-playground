# Lemma 917: complete low-time twelfth-moment enclosures and an inconclusive H2 budget

## Hypotheses

Use the actual positive theta kernel K of L019 and the jointly entire
L058 family F(lambda,z)=integral_0^infinity exp(lambda*u^2)K(u)cos(zu)du.
Write M_k(lambda)=integral_0^infinity u^k exp(lambda*u^2)K(u)du.
Assume exactly L037's arithmetic contracts: outward directed basic
Decimal operations; correctly rounded nearest exponential widened by
adjacent representable values; rejection of zero-containing divisors,
invalid operations, overflow, underflow and subnormal arithmetic.
All three contexts use precision 100. Library correctness is assumed,
not independently verified. There are no all-real-zero hypotheses.

For real lambda define S_n by the local logarithm germ

    log(F(lambda,z)/M_0(lambda))=-sum_(n>=1) S_n(lambda)z^(2n)/n.

Use L874's real symmetric H2=(S_(i+j+2))_(0<=i,j<=2). The coefficient
convention is local; no product over deformed zeros is asserted.

## Conclusion

For every lambda in the closed band [0,1/20], each of M_0,M_2,...,M_12
is enclosed by its complete saved interval on any containing parameter
panel p, 0<=p<=255, in `scripts/heat/low-time-h2-uniform-195.json`.
The panels are [p/5120,(p+1)/5120]. In particular M_0>0.49712.
The nonnegative contribution discarded by retaining u<=2 and n<=4
is uniformly less than 4.389*10^(-23) for every one of those moments.

Let Delta_j be the j-th leading principal minor of H2. The certificate
gives, uniformly on the full closed band,

    Delta_1=S_2>3.714*10^(-5),
    9.7*10^(-16)<Delta_2<7.026*10^(-15),
    -7.013*10^(-27)<Delta_3<6.585*10^(-27).

Every one of the 256 saved enclosures of Delta_3 contains zero; none
has a negative upper endpoint or a positive lower endpoint. Thus this
fixed-budget computation **does not decide H2 positive definiteness**.
The required criterion was Delta_j>0 for all three j on every panel.
The first two signs reproduce the already audited L914 conclusion;
no new discovery is claimed for them. No actual contact, negative
actual determinant, failure of positivity, or RH conclusion follows.

The separate step197 proof/code audit below accepts this conditional
enclosure and the higher-moment tail extension. The original
exact-rational replay alone checked finite algebra and evidence;
the later audit also checks analytic inclusion and reproduces every
finite quadrature record. Decimal-library correctness remains assumed.

## Proof

### Local coefficients through degree twelve

L058 gives joint analyticity and M_0>0 for real lambda. Near any such
parameter, g=F/M_0 has value 1 at zero and a normalized local analytic
logarithm. In t=z^2 put

    e_n=M_(2n)/((2n)!M_0), e_0=1,
    q_n=(-1)^n e_n,
    g(t)=sum_(n=0)^6 q_n t^n+O(t^7).

All derivatives used in this finite expansion are justified by L058's
compact domination. Writing ell=log g=-sum S_n t^n/n, the exact identity
g'=ell'g gives

    S_n=-n q_n-sum_(k=1)^(n-1) S_k q_(n-k), 1<=n<=6.

Let a=e_1,b=e_2,c=e_3,d=e_4,e=e_5,f=e_6. Successive substitution gives

    S_1=a,
    S_2=a^2-2b,
    S_3=a^3-3ab+3c,
    S_4=a^4-4a^2b+2b^2+4ac-4d,
    S_5=a^5-5a^3b+5ab^2+5a^2c-5bc-5ad+5e,
    S_6=a^6-6a^4b+9a^2b^2-2b^3+6a^3c-12abc+3c^2
          -6a^2d+6bd+6ae-6f.

These are elementary Newton/logarithm identities, reproduced solely
to fix signs and permit an independent implementation; no novelty is
claimed. The rational checker separately forms log(1+h) modulo t^7
as sum_(r=1)^6 (-1)^(r+1)h^r/r in six independent formal variables,
where h=sum_(n=1)^6 (-1)^n e_n t^n. It compares -n times each log
coefficient with the displayed polynomial. All six complete symbolic
residuals are empty, and the derived polynomials are saved in its
`formal_algebra` record. This computation checks finite identities;
it does not presume any S_n sign.

### Complete positive-tilt tails through twelve

For k=0,2,...,12, u^k<=exp(12u) on u>=0: on [0,1] use u^k<=1,
and on [1,infinity) use k log u<=12u. Put X=exp(2u) and beta=119/40.
The exponential series gives X>=2u^2. Hence lambda u^2<=X/40 and
also <=n^2 X/40 for 0<=lambda<=1/20 and n>=1.
Dropping the negative part of each positive K_n and using pi<4 gives
K_n<=128 n^4 exp(9u/2)exp(-pi n^2 X).
For X>=1, n^4<=16^(n-1), n^2>=1+3(n-1) and pi>3 yield
sum n^4 exp(-pi n^2 X)<=2exp(-pi X), because 16exp(-9)<1/2.
Thus the full integrand is bounded by
256 exp(33u/2)exp(-beta X). Under du=dX/(2X), the residual power is
X^(29/4)<=X^8. Since exp(4)>50, its spatial tail after u=2 is at most

    E_space=128 exp(-50beta)
      *sum_(j=0)^8 [8!/(8-j)!]50^(8-j)/beta^(j+1).

This is integration by parts eight times for integral_50^infinity
X^8 exp(-beta X)dX, enlarging the actual lower endpoint exp(4).

For omitted theta terms n>=5, integrate their bounds over all u>=0.
The termwise tilt inequality leaves exp(-beta n^2 X), so their total
is at most 64 sum_(n>=5) n^4 integral_1^infinity X^8 exp(-beta n^2 X)dX.
For X>=1, exp(-beta n^2 X)<=exp(1-beta n^2)exp(-X), and the integral
of X^8 exp(-X) on [0,infinity) is 8!=40320. Write n=5+j; n^4<=625*16^j
and n^2>=25+11j. Since 16exp(-11beta)<1/2, a valid uniform bound is

    E_theta=3,225,600,000 exp(1-25beta).

The nonnegative discarded contribution to each moment is bounded by
E_space+E_theta. This covers the spatial tail and every omitted theta
term without relying on L914's smaller constants; any double counting
only enlarges the error. The two exponential inequalities above follow
from positive exponential series (as in L914); numeric constants will
be enclosed outward in the certificate.


### Uniform finite integration and interval evaluation

The producer `scripts/heat/low-time-h2-uniform-195.py` imports the
unchanged interval/jet primitives in `scripts/hankel/certify_hankel.py`.
L037 supplies inclusion of the operations and the 96-term rational
Machin enclosure of pi. Precision is set to 100 in all three contexts;
the complete final trap/flag record is saved in `arithmetic`.

On each of the 256 full closed lambda intervals, use 64 spatial panels
[(2i)/64,(2i+2)/64], center (2i+1)/64 and half-width h=1/64.
The finite integrand is

    u^k exp(lambda*u^2) sum_(n=1)^4 K_n(u), k=0,2,...,12.

With v=pi*n^2 exp(2u), the kernel jet computes
exp(u/2)*(8v^2-12v)*exp(-v), precisely L019's K_n.
The normalized jet of u^k has coefficient binom(k,j)u^(k-j)
for j<=k and zero otherwise. This includes all spatial derivatives
needed when k=10,12; the spatial derivative order remains eight.
The exponent lambda*u^2 has normalized coefficients lambda*u^2,
2lambda*u, lambda and then zeros. L036's product and exponential
recurrences therefore enclose all required normalized derivatives.

Midpoint jets use the spatial center and the whole parameter interval.
Eighth-derivative jets use the whole closed spatial and parameter
rectangle. The finite integrands are C^8 there. For each fixed lambda
in the panel, L036 supplies

    integral_(center-h)^(center+h) f(u)du
      in 2 sum_(j=0,2,4,6) f_j h^(j+1)/(j+1)+[-R,R],
    R=2h^9/9 * sup |f^(8)|/8!.

The largest absolute endpoint of the full-rectangle eighth coefficient
encloses this supremum. All operations, including remainder sums, are
outward. Add [0,E_space+E_theta] to every summed finite moment. The
complement of n<=4,u<=2 is covered by the complete tails just proved;
positivity of K_n makes the discarded contribution nonnegative.
Thus interval induction proves containment of every full moment for
every lambda in every panel, including both endpoints. The complete
seven moment intervals and seven quadrature remainder bounds per
panel are retained, not merely midpoint samples.

All moment lower endpoints are strictly positive; hence normalization
by M_0 is safe. Evaluate the displayed six coefficient polynomials
using enclosing arithmetic. Write A=S_2,B=S_3,C=S_4,D=S_5,E=S_6.
The minors are evaluated as

    Delta_1=A, Delta_2=AC-B^2,
    Delta_3=A(CE-D^2)-B(BE-DC)+C(BD-C^2).

The producer also evaluates the equivalent expanded determinant
ACE+2BCD-AD^2-EB^2-C^3 and requires the two enclosures to overlap.
The sign attempt uses the cofactor expression; the expanded expression
is a consistency check. Both remain enclosing even when they contain
zero. No narrowed point value is substituted.

Sylvester's criterion (real symmetric form) requires all three leading
minors to be strictly positive for positive definiteness. Although
the first two are certified, the third is unresolved on every panel.
The bounded-attempt stopping rule is therefore met without refining
panels, enlarging the theta core, changing the band, or sweeping a
parameter. This is failure of this certificate to pay the sign
threshold, not a theorem that H2 fails to be positive definite.

### Complete evidence and exact-rational replay

Run, from this notebook,

```text
python3 scripts/heat/low-time-h2-uniform-195.py
python3 scripts/heat/low-time-h2-uniform-195-check.py
```

The full producer output `scripts/heat/low-time-h2-uniform-195.json`
contains all 256 panel, moment, remainder, normalized-coefficient,
S_1,...,S_6, determinant-cofactor/term, minor and failure records.
It has 0 certified H2 panels, 256 failed sign panels, and no exceptional
arithmetic. Each failure is exactly minor 3. The quoted rational
thresholds above conservatively enclose the complete global extrema;
the sign summaries and their endpoints were inspected.

The checker output `scripts/heat/low-time-h2-uniform-195-check.json`
has status passed, 256 checked panels and an empty replay-failure list.
Using Fraction endpoint arithmetic, it checks every exact parameter
endpoint and every saved moment/remainder record, independently derives
the coefficient polynomials by finite-log extraction, replays all
normalizations, polynomials, cofactors, terms and minor enclosures,
and verifies their containment in the Decimal records. It recomputes
all sign counts, extrema and the complete failed-panel list. It verifies
the stated context precision, rounding modes, traps and flags. These
checks address cancellation-sensitive arithmetic using exact rationals;
they neither reimplement finite quadrature nor verify Decimal.exp.

For each negative exponential in the tail constants the checker also
uses rational positive-series enclosure independently of Decimal.exp.
For x>=0 let P=sum_(j=0)^1000 x^j/j!. The positive remainder is at most
(x^1001/1001!)/(1-x/1002), since subsequent ratios are at most x/1002<1
for both x=50beta and x=25beta-1. Thus reciprocating the two positive
bounds encloses exp(-x). The resulting exact rational spatial, theta
and total bounds are saved in full in `tails`; they lie inside the
producer's outward intervals. They prove the bound 4.389*10^(-23).
The full spatial upper endpoint is below 4.447*10^(-50), and the theta
upper endpoint below 4.388*10^(-23). Tail uncertainty has been paid;
there is no unpaid positive-tilt tail assumption.

A concrete width diagnostic on panel 0 is S_6 enclosed between
-8.828*10^(-14) and 1.201*10^(-13). Its third-minor enclosure is
between -6.508*10^(-27) and 6.104*10^(-27). The full endpoints in the
certificate, rather than these outward decimal abbreviations, were
used in all checks. Moment-to-logarithm interval propagation has already
lost a sign at this coefficient. For comparison the panel-0 M_12
interval has width between 1.776*10^(-9) and 1.777*10^(-9), its spatial
Taylor error upper bound is below 6.241*10^(-12), and its discarded
tail bound is below 4.389*10^(-23). These quantify where the stored
width occurs; they do not prove that eliminating one error source
would suffice, or that a refined method would succeed. No such
refinement was run. The result concerns only finite coefficients
of the actual family, not an arbitrary moment model.

### Independent proof/code audit, 9 November 2026 (step197)

The stated conditional enclosures and fixed-budget failure pass the
audit. No mathematical correction, new sign theorem or refinement is
made. The previously unreviewed extension is now accepted locally,
subject to exactly the arithmetic hypotheses above. The audit reuses
the SPECIALIZE assessment
`drafts/literature/2026-11-09-l917-twelfth-moment-enclosure-audit.md`;
the existing source comparison does not supply an H2 sign theorem.

**Analytic tails.** Each K_n is positive since v=pi n^2 exp(2u)>3/2.
Dropping its negative term gives the stated 128 n^4 bound, using
pi<4. The inequality exp(2u)>=2u^2 is valid on u>=0 by the positive
quadratic exponential-series term. Thus both uses of the tilt bound
are valid, including lambda=0 and lambda=1/20. For every order used,
u^k<=exp(12u) follows on [0,1] directly and on [1,infinity) from
log u<=u. No derivative or signed quantity is estimated by positivity
here: these bounds concern only positive moment tails.

For the spatial tail, n^4<=16^(n-1) follows inductively from
((n+1)/n)^4<=16. Also n^2>=1+3(n-1), since the difference is
(n-1)(n-2)>=0 for integer n>=1. The resulting geometric ratio is
16 exp(-3pi X)<=16 exp(-9)<1/2. Factoring out exp(lambda u^2)
therefore gives 256 exp(33u/2-beta X), with beta=3-1/40.
Changing variable gives the coefficient 128 and power X^(29/4),
which is at most X^8 on X>=1. Enlarging the domain from X>=exp(4)
to X>=50 is legitimate. Eight integrations by parts give exactly
the nine terms in E_space, including its final constant term.

For theta indices n>=5, absorbing the tilt separately into each
n^2 exponential gives coefficient 64 after the same change of
variable. For X>=1,
-beta n^2 X<=(1-beta n^2)-X, since beta n^2>=1.
The enlarged gamma integral is 8!. For n=5+j, n^4<=625*16^j
and n^2>=25+11j: the latter difference is j(j-1)>=0 for integer
j>=0. Summing the ratio 16 exp(-11beta)<1/2 gives exactly
64*40320*625*2=3,225,600,000. Thus E_theta covers even the
omitted terms below u=2. Adding the full spatial tail double-counts
some positive mass, which is harmless. All seven moments receive a
valid common upper bound on the entire closed parameter band.

The audit script supplies exact rational witnesses for every numerical
premise: the degree-seven positive partial sum at 4 exceeds 50;
the degree-four positive partial sum at 9 exceeds 32; and 11beta>9.
The second witness implies both geometric ratios are below 1/2.
The inspected rational exponential checker has positive terms and
subsequent ratios at most x/1002<1 for both required x. Its next-term
geometric bound and reciprocal interval therefore enclose each
exponential with the correct orientation. All three exact rational
tail enclosures lie inside the saved outward intervals, and the
complete tail sum is below 4.389e-23. This is not an appeal to the
Decimal exponential for the analytic tail threshold.

**Finite integration and arithmetic.** The complete base primitives
were inspected. Exact Decimal construction preserves integer inputs;
addition, the four endpoint products, reciprocal division and rational
conversion use the named directed contexts. Sign reversal and magnitude
use exact copy operations. All invoked powers use repeated interval
multiplication for nonnegative integer exponents. No Context.power
rounding property is assumed. Endpoint exponentials use the nearest
context followed by its adjacent neighbors. All three contexts are
set to 100 digits before evaluation and retain the required traps.
The final saved exceptional flags are all false. These checks validate
the implementation against L037's contracts; they do not verify the
Decimal library itself.

The product and exponential jet loops implement L036's normalized
recurrences through index eight. For k=10 and k=12, the binomial
power jet retains all coefficients through eight; coefficients of
higher derivative order are unnecessary for this quadrature. The
kernel jet is exactly exp(u/2)(8v^2-12v)exp(-v) summed over n=1,...,4.
The separate tilt jet has precisely the three nonzero exponent
coefficients stated above. At each fixed point of the full rectangle,
interval induction therefore includes the true normalized eighth
derivative, despite dependencies between repeated occurrences of u
or lambda. Taking the larger absolute endpoint bounds its magnitude.
Midpoint jets retain the entire lambda interval. The integration
weights 2h^(j+1)/(j+1), j=0,2,4,6, and remainder weight 2h^9/9
are exactly those of L036. The symmetric remainder uses its outward
upper endpoint, and adding [0,tail_upper] has the correct sign.

All 64 spatial intervals have exact endpoints 2i/64,(2i+2)/64
and centers (2i+1)/64. They cover [0,2] with matching endpoints.
Likewise the saved lambda endpoints are exactly p/5120,(p+1)/5120
for all 256 panels, so there is no omitted endpoint or parameter.
The coefficient evaluation uses strictly positive saved mass lower
bounds; every division is consequently legitimate.

**Log algebra and complete evidence.** The identity g'=ell'g gives
S_n=-n q_n-sum_(k=1)^(n-1) S_k q_(n-k) with the displayed signs.
The independent finite-log extraction was inspected and replayed in
six formal variables. Its six complete residual polynomials vanish,
including the S5 and S6 extensions. The inherited Fraction interval
helper implements exact endpoint addition, multiplication, reciprocal
division and integer multiplication powers. It is used only with
positive mass denominators and nonnegative powers. Replaying every
panel checks all seven moment/remainder records, all six normalized
coefficients and S polynomials, all determinant cofactors and signed
terms, both determinant expressions, sign counts, failure indices
and exact extrema against the printed rational thresholds. The
determinant formulas agree algebraically with the symmetric matrix
having rows (A,B,C), (B,C,D), (C,D,E). Overlap of their intervals is
only a consistency check; enclosure follows from arithmetic inclusion.

Run the separately written finite-integration replay with

```text
python3 scripts/heat/low-time-h2-audit-197.py
python3 scripts/heat/low-time-h2-uniform-195-check.py
```

The first script changes the loop order and reconstructs all seven
integrals and errors on every panel, using the inspected original
preparation and shared interval/jet primitives. Its full certificate
`scripts/heat/low-time-h2-audit-197.json` records exact equality to
all 1,792 moment intervals and all 1,792 remainder intervals, with
zero failures. It also checks the saved pi/tail records, spatial and
parameter partitions and final arithmetic record. Input hashes and
the replay's Python version are saved. This is a complete reproduction
with an independently inspected inclusion argument, not an independent
interval library, jet implementation or verification of the original
runtime's historical Python version. The original producer certificate
was not overwritten or refined. The rational replay passes on all
256 panels and verifies the complete failed-panel list, all quoted
thresholds and panel-zero width diagnostics; its tail bounds and formal
polynomials remain saved in full in the existing checker certificate.

Every panel has positive first and second leading minors and a
zero-containing third-minor enclosure. The global third-minor
endpoints are approximately -7.0124514150e-27 and 6.5842009247e-27;
the checker compares their full rational endpoint values, not these
abbreviations, with the bounds in the Conclusion. In particular the
required strictly positive third lower endpoint is not attained on
any panel. Sylvester's criterion consequently cannot conclude positive
definiteness from these intervals. Nothing here proves exact-law
negativity, equality, a contact, or an obstruction to another method.
The fixed-budget route remains stopped; the exact H2 sign and the
main all-degree mixed-positivity gap remain unresolved.

## Mathlib

Full matching coverage and supporting specialized coverage have not
been checked. Availability is unknown, not asserted absent. The finite
Decimal computation is not formalized in Lean. L036/L037 retain their
stated inclusion and library qualifications. Sylvester's criterion is
a standard named linear-algebra input; there is no positive-definiteness
conclusion here requiring its unresolved third hypothesis. Reference:
https://leanprover-community.github.io/mathlib4_docs/.
