# Corollary 988a: complete exact-root lobe formula and absolute high-zero tail

## Hypotheses

Let n>=2 be an integer, Lambda the actual von Mangoldt function
(including all prime powers), and

    K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u)
          =[L_(n-1)^(2)(u)-1]/(n-1).

The equality is L985's exact finite connection; no asymptotic from
that lemma is used. Let I_n consist of the intervals I=[a,b] between
consecutive distinct real roots of K_n for which n<=a<b<=2n.
No simplicity, root-spacing estimate, or nonemptiness is assumed.
For I in I_n put

    A_(n,I)=sum_(exp(a)<m<=exp(b)) Lambda(m)*K_n(log m)/m,
    C_(n,I)=A_(n,I)-integral_a^b K_n(u)du,
    T_(n,I)(s)=integral_a^b exp((s-1)*u)*K_n(u)du,
    V_(n,I)=integral_a^b K_n(u)*exp(-3*u)/(1-exp(-2*u))du.

The left arithmetic endpoint is excluded and the right endpoint has
full weight. Let rho range over all actual nontrivial zeta zeros
0<Re(rho)<1, with analytic multiplicity. No RH, zero simplicity,
rightmost-zero assumption, or bound on a signed low-zero sum is used.

## Conclusion

For each such I the series sum_rho |T_(n,I)(rho)| converges, and

    C_(n,I)=-sum_rho T_(n,I)(rho)-V_(n,I).              (1)

The pole/continuum compensator is exactly the integral from a to b;
V is the retained trivial-zero/archimedean correction. In particular
there is no omitted lower-endpoint constant. For every real H>=e,
with P(n)=n*(n+1)*(n+2)/12,

    sum_(I in I_n) sum_(rho, |Im rho|>H) |T_(n,I)(rho)|
      <=(n-2)*P(n)*exp(n)*(40*log H+80*log 2)/H.       (2)

The cutoff excludes zeros at |Im rho|=H. Consequently

    sum_(I in I_n) sum_(rho, |Im rho|>exp(n)) |T_(n,I)(rho)|
      <=(n-2)*P(n)*(40*n+80*log 2)
      <=(10/3)*(n+2)^5 <100*(n+2)^6.                 (3)

These statements include the empty collection. Step309, 10 November
2026: REPRODUCTION specialization under the pre-existing SPECIALIZE
review308, explicitly approved for mathematics by the invocation.
This is local technical progress using known inputs, not a new prime
estimate beyond the sources checked or an RH candidate. Independent
audit passed in step311, 10 November2026, under the separately approved
SPECIALIZE review309; the replay is recorded below. No positive-lobe
budget or low-zero sign is claimed.

## Proof

### Finite interval estimate before any infinite-series identification

Import audited L988's exact derivative and counting conclusions:

    |K_n'(u)|<=a_n*exp(u/2), a_n=n*(n+1)/6,
    |K_n''(u)|<=b_n*exp(u/2), b_n=n*(n+1)*(n-2)/24,
    sum_(rho, |Im rho|>H) |Im rho|^(-2)
                      <=(40*log H+80*log 2)/H, H>=e. (4)

The derivative bounds hold for every u>=0. They use exact polynomial
differentiation, not differentiation of a bulk asymptotic. Their
precise external inputs are DLMF18.9.23 and18.14.8, and
Hasanalizade-Shen-Wong, *Counting zeros of the Riemann zeta function*,
arXiv2107.06506v1 (14 July2021), Corollary1.2/(1.5), p2; L988 gives
the domain, multiplicity, small-height and shell-bound qualifications.
At n=2, K_2=2-u, a_2=1 and b_2=0. Thus (4) never uses a negative
polynomial degree. The imported zero-count theorem also implies that
each bounded-height multiset is finite; this follows alternatively
from analyticity and isolation, including near the pole at1.

For s with 0<beta=Re(s)<1 and gamma=Im(s)!=0, set z=s-1.
Both K_n(a) and K_n(b) vanish. Two finite integrations by parts give

    T_(n,I)(s)=-[exp(z*u)*K_n'(u)]_a^b/z^2
                    +(1/z^2)*integral_a^b exp(z*u)*K_n''(u)du. (5)

Indeed the first integration has endpoint bracket
[exp(z*u)*K_n(u)/z]_a^b=0; the second leaves exactly the negative
derivative bracket in (5). Both derivative endpoint terms are kept.
Since u>=0 and beta<1,

    |exp(z*u)|*exp(u/2)=exp((beta-1/2)*u)<=exp(u/2).

It follows that

    |z|^2*|T_(n,I)(s)|
      <=a_n*(exp(b/2)+exp(a/2))
                         +2*b_n*(exp(b/2)-exp(a/2))
      <=2*(a_n+b_n)*exp(n)=P(n)*exp(n).              (6)

Here b<=2n, b_n>=0, and the integral of exp(u/2) is
2*(exp(b/2)-exp(a/2)); |z|>=|gamma|. Thus

    |T_(n,I)(s)|<=P(n)*exp(n)/gamma^2.               (7)

Apply (4) to the nonnegative tail using (7). This proves absolute
summability above any H>=e, with the bound in (2) before its factor
counting I. The bounded-height zero multiset is finite, and every T
is a finite integral (indeed an entire function of s), so the whole
zero series is absolutely convergent for fixed n,I. This argument
precedes identification with the arithmetic sum. There is no
interchange of a conditional zero sum with an integral across jumps.

### Admissible test and precise named explicit formula

Import H.L. Montgomery and R.C. Vaughan, *Multiplicative Number
Theory I: Classical Theory*, Cambridge2007, Theorem12.13 (Weil),
(12.20)-(12.22), printed pp410-411, with its gamma-integral
Lemma12.14 and proof, pp414-416. The primary source is
[Section12.2](https://personal.science.psu.edu/rcv4/personal/Publications/MNTI/16.0_pp_397_418_Explicit_formulae.pdf#page=14).
Review288 already inspected its bounded-variation inversion and the
zero/nonzero origin cases of the gamma lemma. In step309 the exact
statement and normalization on pp410-411 were reopened for this
application. Import the general theorem; a new contour proof is
unnecessary. Its constants depending on the test are not used for
the uniform bound (2).

Define on the real line

    F(x)=2*pi*exp(pi*x)*K_n(-2*pi*x),
                       -b/(2*pi)<=x<=-a/(2*pi),
    F(x)=0 otherwise.                               (8)

It is a measurable, continuous, compactly supported function:
the two nonzero-piece endpoint limits are zero by K_n(a)=K_n(b)=0.
It is C^1 on each of finitely many pieces, with bounded derivative
on the compact nonzero piece. Splitting at the two endpoints shows
that F is absolutely continuous on every bounded interval and of
finite total variation on R. Its derivative is zero off the compact
piece, and no endpoint jump gives an atom in dF. Hence both weighted
integrals in (12.20)-(12.21) are finite, for example for the fixed
delta_0=1. No uniform-in-n assertion about those integrals is needed.
Continuity gives the required midpoint value at every point. Since
a>=n>=2, F vanishes in a neighborhood of0. Therefore F(0)=0 and
F(x)+F(-x)=2F(0)+O(|x|), with an identically zero difference near0.
This verifies every test hypothesis of Theorem12.13. It also verifies
the L1, bounded-variation and origin behavior used in Lemma12.14
for the reflected/symmetrized test, so no uninspected smooth-test
replacement is being made at the root endpoints.

With the source's transform convention, substitution u=-2*pi*x
gives, including its Jacobian and orientation,

    Phi(s)=integral_R F(x)*exp(-(s-1/2)*2*pi*x)dx
          =integral_a^b exp((s-1)*u)*K_n(u)du=T_(n,I)(s). (9)

Apply the theorem to the primitive principal character modulo1:
q=1, kappa=0 and E_0=1. There is no evenness requirement on F.
The source's two pole terms are

    Phi(1)=integral_a^b K_n(u)du,
    Phi(0)=integral_a^b exp(-u)*K_n(u)du.             (10)

The local conductor/digamma term is zero because it is multiplied
by F(0). For m>=2, the positive-argument sample F(log(m)/(2*pi))
is zero. The negative sample, divided by 2*pi*sqrt(m), is
K_n(log m)/m on exp(a)<=m<=exp(b), and zero otherwise.
At either endpoint the sample is exactly zero. Thus the prime term
in the theorem is exactly -A_(n,I), including every prime power.
A hypothetical endpoint prime power contributes zero whether given
half weight, full weight, or excluded; this reconciles the source's
midpoint convention with the prescribed (exp(a),exp(b)] convention.

The remaining source gamma integral, by u=2*pi*x, becomes

    G=integral_0^infinity exp(-pi*x)/(1-exp(-4*pi*x))
                              *(2*F(0)-F(x)-F(-x))dx
     =-integral_a^b exp(-u)*K_n(u)/(1-exp(-2*u))du.  (11)

Its integrand is supported away from0, so this integral is absolutely
convergent without a further regularization. Combining (10)-(11),

    Phi(0)+G=-integral_a^b K_n(u)*exp(-3*u)
                                      /(1-exp(-2*u))du=-V_(n,I). (12)

This cancellation retains both pole terms before collecting the
archimedean term. For an equivalent trivial-zero expression,

    V_(n,I)=sum_(j>=1) T_(n,I)(-2*j).               (13)

Indeed the geometric series exp(-3u)/(1-exp(-2u)) equals
sum_(j>=1) exp(-(2*j+1)*u). Since a>0 and K_n is bounded on [a,b],
this expansion converges uniformly there and its absolute-integral
majorant is finite. Thus (13) is an absolutely justified expansion,
not a suppressed correction. No term from u=0 or a lower endpoint
at log1 is present: the support starts at a and vanishes there.

Theorem12.13 now gives initially in its symmetric-height order

    lim_(Y->infinity) sum_(rho, |Im rho|<=Y) T_(n,I)(rho)
           =integral_a^b K_n(u)du-A_(n,I)-V_(n,I).   (14)

The absolute convergence already proved from (4)-(7) identifies this
limit with the unconditionally convergent series in (1). Rearranging
the finite arithmetic terms in (14) proves (1). No n-limit, moving
regulator limit, or passage through an infinite family is used.

### Number of intervals and aggregate constant

K_n has exact degree n-1: its leading coefficient is
(-1)^(n-1)/((n-1)*(n-1)!), unaffected by the subtracted constant.
A nonzero polynomial of degree n-1 has at most n-1 distinct real
roots. If their number is r>=1, the number of adjacent pairs is r-1;
if r=0 it is0. Restricting pairs to [n,2n] cannot increase the count,
so #I_n<=n-2 for every n>=2. In particular I_2 is empty; no lobe or
negative-degree exception has been assumed. Repeated roots cause
no problem since the list uses distinct roots and endpoint vanishing.

For each I, (4)-(7) bound its high-zero tail by
P(n)*exp(n)*(40*log H+80*log2)/H. There are finitely many I, so
summing these nonnegative bounds proves (2), with all multiplicities
and the strict height cutoff exactly as in L988. At H=exp(n),
exp(n) cancels and log H=n. Finally log2<1, n-2<=n+2, and

    P(n)<= (n+2)^3/12,
    40*n+80*log2<=40*(n+2).

These elementary inequalities prove the second inequality in (3).
For n>=2, (10/3)<100*(n+2), proving its final strict inequality.
Thus the actual aggregate upper bound is explicitly below the chosen
100*(n+2)^6 threshold for every admissible n, not just asymptotically
or at sampled degrees.

### Relevance and limit of the result

At fixed n, (1) can now be split at H=exp(n) into a finite low-zero
sum and an absolutely controlled high-zero remainder, together with
the exact V term. The result removes the unpaid leading endpoint
series only for these complete exact-root intervals. It proves
neither a bound for sum_(I in I_n) max(C_(n,I),0), nor low-zero
cancellation, nor the contribution of intervals clipped by n or2n.
Both logarithmic complements and L984(H), and hence L030-L032/C032a
and L966/L968, remain unresolved. It uses no off-line synthetic zero
as an actual zeta input and proves no new zero-free region.

The bounded test is complete. Do not follow it with successively
sharper absolute high-tail estimates: the remaining research needs
signed arithmetic/spectral aggregation or a materially different
mechanism. Stops233/235/243/307 are comparisons, not premises or
global bans. L981/L982 supply contextual conventions only; neither
their quantitative tails nor an unproved part of L984 enters (1)-(3).

### Independent audit, step311

This audit imports the general source contracts already inspected in
review309 and replays the specialization, rather than reproving Weil's
formula or the zero-counting theorem. Its only local mathematical inputs
remain L985's finite connection and audited L988. There is no new premise
about zero locations, lobe signs or the endpoint quantities in L981/L982.

First, DLMF18.18.18 at degree n-1 with alpha=1,beta=2 has all
connection coefficients equal to1. Removing its degree-zero term gives
exactly the displayed K_n, including the -1 and division by n-1.
The leading coefficient is nonzero, including when n=2, so the degree
is n-1. Consequently there are at most n-2 intervals between consecutive
distinct real roots, even before restricting to [n,2n]. When there are
zero or one distinct roots there are no such intervals; when n=2 there
cannot be two. A repeated root is used once in this count and still
annuls the kernel at the endpoint. No positivity or spacing of roots
is being inferred from the Laguerre connection.

For the tail, the derivative constants imported from L988 are
a_n=n(n+1)/6 and b_n=n(n+1)(n-2)/24, both nonnegative for n>=2.
Their source degrees are n-2 with parameter3, and, only for n>=3,
n-3 with parameter4. At n=2 the kernel is 2-u and its second
derivative is zero. Thus the global real-positive-argument bounds
are applicable on every interval under consideration, without any
negative-degree convention or large-n onset. Integration first gives
T=-z^(-1)*integral exp(z*u)K_n'(u)du because both K endpoints
vanish; integrating this integral gives precisely (5), with the
negative derivative bracket and positive second-derivative integral.
The derivative bracket has two terms; neither is assumed to vanish.
For beta<1 and u>=0 the weighted exponential is at most exp(u/2).
The resulting numerator is bounded by

    a_n*(exp(b/2)+exp(a/2))
                  +2*b_n*(exp(b/2)-exp(a/2))
      <=2*(a_n+b_n)*exp(n)=P(n)*exp(n).

The first pair is at most 2*a_n*exp(n), and the difference is
between0 and exp(n). This proves the bound also when beta<1/2;
there is no division by beta-1/2. The denominator satisfies
|z|^2=(beta-1)^2+gamma^2>=gamma^2.

L988's nonnegative shell bound counts the actual zeros with analytic
multiplicity, uses shells (2^j*H,2^(j+1)*H], and includes both signs
of the ordinate. Thus it applies at every real H>=e, even if a zero
lies on a shell boundary. All zeros at |gamma|=H are excluded from
the high tail. The resulting absolute convergence above e, together
with finiteness of the bounded-height zero multiset, proves absolute
convergence of the whole series for fixed n,I before any explicit
formula is invoked. Potential zeros at gamma=0 would belong to that
finite part and need no gamma^(-2) bound. Finiteness near the strip
endpoints follows from analytic continuation at0 and the nonzero
residue at the pole1, as well as isolation on the remaining compact
region; no unproved absence of real zeros is needed here.

For the explicit formula, (8) is continuous at both endpoints because
K_n vanishes there. Extending its smooth interior piece by zero gives
a compactly supported absolutely continuous function with integrable
piecewise derivative and no jump atoms. Hence both exponentially
weighted integrals required in Montgomery-Vaughan Theorem12.13 are
finite for a fixed delta_0=1. Every point has its midpoint value.
Its support is separated from0, so the symmetric origin condition
holds with identically zero difference near0. The reflected and
symmetrized tests in Lemma12.14 likewise vanish there and have L1
bounded variation. These checks cover the original, nonsmooth-at-the-
endpoints test directly; a smoothing limit is unnecessary.

The transformation u=-2*pi*x reverses limits and contributes
dx=-du/(2*pi). Multiplying exp(pi*x) from F by the transform's
exp(-(s-1/2)*2*pi*x) gives exp((s-1)*u). Thus Phi=T with no
remaining 2*pi factor. The principal modulus1 character is primitive,
has q=1,kappa=0,E_0=1, and supplies BOTH Phi(0) and Phi(1).
The term proportional to F(0) is zero. Positive prime samples vanish;
the negative sample divided by 2*pi*sqrt(m) is K_n(log m)/m.
The theorem sums Lambda over all prime powers. At either endpoint
that sample is zero, reconciling midpoint values with the specified
open-left, closed-right arithmetic sum without a residual boundary term.

For x>0 in the gamma integral, only F(-x) can be nonzero.
Its product with exp(-pi*x) is
2*pi*exp(-2*pi*x)*K_n(2*pi*x); the substitution u=2*pi*x
therefore gives exactly the negative integral in (11). In particular,

    exp(-u)-exp(-u)/(1-exp(-2*u))
                       =-exp(-3*u)/(1-exp(-2*u)).

This checks the sign, exponent and normalization of Phi(0)+G=-V.
The remaining pole Phi(1) is the continuum compensator. All these
integrals are ordinary absolutely convergent integrals on [a,b],
with a>=2. The geometric expansion of the correction converges
uniformly and has an absolute-integral majorant there, so (13)
retains exactly the trivial zeros -2,-4,... . No origin constant
or suppressed lower-endpoint term remains. The source formula now
gives (14) in symmetric-height order; the absolute convergence already
proved identifies it with the unrestricted series. This verifies (1)
without differentiating a pointwise psi formula across prime powers.

Finally multiply the per-interval high-tail bound by at most n-2.
At H=exp(n)>=e, the exponential factors cancel exactly. For every
n>=2, use n-2<=n+2, n(n+1)(n+2)<=(n+2)^3 and
40*n+80*log2<=40*(n+2). The resulting bound is
(10/3)*(n+2)^5, strictly less than 100*(n+2)^6 since
10/3<100*(n+2). This is an all-degree comparison, not a sampled
calculation. Empty collections have zero tail and satisfy the same
inequalities. Thus all conclusions (1)-(3) survive unchanged.

This validates a local specialization of named theorems, not an
estimate beyond the sources checked. It pays no signed low-zero or
positive-lobe resource, clipped interval, logarithmic complement or
L984(H). No infinite-degree limit is used. The direct mathematical
inputs in the DAG remain unchanged. Further absolute-tail refinement
is not justified as the next research mechanism.

## Mathlib

Full matching Mathlib coverage of this exact-root, actual-Lambda
explicit formula with the displayed n-uniform aggregate tail is
unchecked and unknown. The general analytic theorem is imported
by the precise citation above; L988 documents its derivative/counting
inputs. Ordinary polynomial calculus and nonnegative series facts
are supporting results, not a claimed full matching formalization.
No absence-of-coverage or checked formalization claim is made.
