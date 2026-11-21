# Lemma 738: an admissible strictly log-concave kernel with a positive Fourier minimum

## Hypotheses

Fix delta=10^(-8), and, for real u, define

    h(u)=1+cos(10u)/100,
    phi(u)=exp(-u^2-delta u^4) h(u),
    F(z)=integral_R phi(u) exp(izu)du.

“Admissible” has exactly the meaning of George Csordas,
[*Fourier transforms of positive definite kernels and the Riemann xi-function*,
arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
Definition 1.2, printed p.2: smooth, positive, even, strictly decreasing
on the positive half-line, and, for some epsilon>0, every derivative
is O(exp(-|u|^(2+epsilon))) as u tends to positive infinity.

The only imported transform evaluation is the Gaussian row (a>0) in
[NIST DLMF, Table 1.14.1](https://dlmf.nist.gov/1.14.T1), with the
normalization in [1.14.1](https://dlmf.nist.gov/1.14.E1).
No local lemma, zero-location hypothesis, simplicity, or RH is assumed.

## Conclusion

The fixed kernel phi is admissible with epsilon=1, and satisfies

    (log phi)''(u) <= -98/99-12 delta u^2 < 0   (u in R).

Its full-line Fourier transform F is real and even on R, entire on C,
and has the following strict signed margins:

    F(t)   > sqrt(pi)/20000   (6<=t<=7),
    F''(t) > sqrt(pi)/10000   (6<=t<=7),
    F'(6)  < -sqrt(pi)/20000,
    F'(7)  > sqrt(pi)/4000.

Consequently there is a unique t_* in (6,7) with F'(t_*)=0.
It is a positive strict local minimum, and

    F'(t_*)^2-F(t_*)F''(t_*) < -pi/200000000 < 0.

Thus positivity, strict log-concavity, all the above admissibility
conditions, and the restriction to a nonzero real critical value do
not imply the first Fourier Laguerre sign. This is a generic obstruction,
not a theorem about actual Xi or its theta kernel. No order-one,
zero-strip, modularity, realization, or higher-degree conclusion is made.
This fixed example is not claimed to be original. Its analytic proof and
exact scalar bounds passed the independent audit of 4 November 2026,
step 265, described below; no actual-Xi consequence was audited or claimed.

## Proof

**Global shape and all derivative tails.** We have 99/100<=h<=101/100,
so phi is positive, smooth and even. Since h''(u)=-cos(10u),

    (log h)'' = h''/h-(h'/h)^2 <= |h''|/h <= 100/99.

Adding the curvature of -u^2-delta u^4 gives the asserted upper bound.
Evenness gives (log phi)'(0)=0. Integrating the strict negative curvature
from 0 to u>0 proves (log phi)'(u)<0, hence phi'(u)<0.

For every integer j>=0, repeated differentiation expresses phi^(j) as
a finite sum of polynomials in u times exp(-u^2-delta u^4), multiplied
by 1, sin(10u), or cos(10u). Thus some finite C_j,d_j satisfy

    |phi^(j)(u)| <= C_j (1+|u|)^(d_j) exp(-u^2-delta u^4).

The polynomial factor times exp(-u^2-delta u^4+|u|^3) is bounded
on R: its logarithm tends to minus infinity at either end, because
delta>0. Hence |phi^(j)(u)|<=C'_j exp(-|u|^3) for every real u.
The same epsilon=1 works for every j, as required. Constants may
depend on j and the fixed delta; no uniformity as delta tends to zero
is used.

**Fourier evaluation and a uniform perturbation estimate.** For each
compact set of z, put A=1+sup|Im z|. On a neighborhood of that compact
set every differentiated integrand is
bounded by

    (101/100)|u|^j exp(A|u|-u^2-delta u^4),

an integrable function. Differentiation under the integral therefore
makes F entire, with F^(j)(z)=integral_R (iu)^j phi(u)exp(izu)du.
Evenness and conjugation show that F and its real derivatives are real
on R, and F is even.

Let phi_0(u)=exp(-u^2)h(u), and let G be its full-line Fourier transform.
Multiplying the DLMF normalized Gaussian row at a=1 by sqrt(2 pi)
gives integral_R exp(-u^2)exp(itu)du=sqrt(pi)exp(-t^2/4).
The exact identity cos(10u)=(exp(10iu)+exp(-10iu))/2 then gives

    G(t)/sqrt(pi) = q(t)+[q(t-10)+q(t+10)]/200,
    q(x)=exp(-x^2/4).

The same dominated differentiation argument applies to G. It is not
being asserted that F itself has this Gaussian formula. For real t,
1-exp(-v)<=v (v>=0) and h<=101/100 give, for j=0,1,2,

    |F^(j)(t)-G^(j)(t)|
      <= (101/100)delta integral_R |u|^(j+4)exp(-u^2)du.       (1)

The bound is uniform on the whole real axis. All integrals are absolute;
no oscillatory remainder or numerical sampling is used.

For completeness, set I_m=integral_R |u|^m exp(-u^2)du.
The imported Gaussian value at zero gives I_0=sqrt(pi), while direct
integration on the two half-lines gives I_1=1. For m>1, integration
by parts on (0,infinity) has boundary term u^(m-1)exp(-u^2), which
vanishes both at zero and at infinity. Doubling that half-line integral
gives I_m=(m-1)I_(m-2)/2.
Consequently I_4=3sqrt(pi)/4, I_5=2, I_6=15sqrt(pi)/8.
Thus (1), divided by sqrt(pi), gives the respective error bounds

    E_0=(303/400)delta,
    E_1=101 delta/(50 sqrt(pi)),
    E_2=(303/160)delta.

Each is strictly less than eta=1/10000000, using sqrt(pi)>1.
These are bounds for the actual damped transform, including its
first and second derivatives, rather than a formal damping expansion.

**Elementary exponential bounds.** The positive exponential series gives
e>1+1+1/2+1/6=8/3>5/2. Its sum through degree four is 65/24.
The tail starting at degree five is at most
(1/120)sum_(k>=0)(1/6)^k=1/100. Thus

    5/2<e<65/24+1/100<11/4<3.

In particular e^5<(11/4)^5=161051/1024<200,
e^9<3^9=19683, and e^10>(5/2)^10=9765625/1024>9000.
All exponential comparisons below follow from these rational bounds.

**Uniform value and curvature margins.** For 6<=t<=7, the shifted
argument t-10 lies in [-4,-3]. All three terms of G are positive, so

    G(t)/sqrt(pi) >= exp(-4)/200 > 1/16200.

Also q''(x)=(x^2/4-1/2)q(x). At the three arguments t, t-10, t+10,
we have |x|>=3, so all curvature terms are positive. Retaining only
the t-10 term, whose quadratic factor is at least 7/4, gives

    G''(t)/sqrt(pi) >= 7exp(-4)/800 > 7/64800.

Subtracting the errors bounded by eta proves the claimed interval
margins, since the exact rational comparisons are

    1/16200-eta > 1/20000,
    7/64800-eta > 1/10000.

**The two derivative endpoints.** Since q'(x)=-x q(x)/2, we have

    G'(6)/sqrt(pi) = -3exp(-9)+exp(-4)/100-exp(-64)/25
                   < exp(-9)[-3+e^5/100]
                   < -exp(-9) < -1/19683.

Therefore F'(6)/sqrt(pi)<-1/19683+eta<-1/20000.
At the other endpoint the exact expression is

    G'(7)/sqrt(pi)
      = exp(-9/4)[3/400-(7/2)exp(-10)-(17/400)exp(-70)].

Here exp(-70)<exp(-10)<1/9000, so the bracket is greater than

    3/400-(7/2+17/400)/9000 = 25583/3600000 > 7/1000.

Also exp(-9/4)>exp(-3)>1/27. Thus
G'(7)/sqrt(pi)>7/27000, and
F'(7)/sqrt(pi)>7/27000-eta>1/4000.
All four final rational comparisons have strict slack; none depends
on a decimal approximation of e or pi.

**Critical point and sign.** F' is continuous, changes sign between
6 and 7, and is strictly increasing throughout that interval because
F''>sqrt(pi)/10000 there. The intermediate value theorem gives a
unique t_* in (6,7) with F'(t_*)=0. The strict curvature makes it a
strict local minimum. The two interval margins give
F(t_*)F''(t_*)>pi/(20000*10000), proving the stated negative sign.
Csordas's equation (1.1), printed p.1, uses one half of the full-line
transform, hence the half-line cosine transform F/2 for this even
kernel. This scaling preserves stationarity and all sign conclusions,
and scales the Laguerre expression by 1/4. In contrast, Theorem 3.7
and Remark 3.8(a), printed p.8, explicitly use the full-line transform,
which agrees with F here. No uniform convention across that paper is
assumed, and no Laguerre positivity theorem is being imported from it.

No inference from this example to actual Xi has been made. The only
role of L050 and L607 in selecting this test was comparison with their
different conclusions; neither result is used in this proof.

**Independent audit, 4 November 2026, step 265.** The approved fixed
scope was checked against the source hypotheses recorded above; no
parameters or family were changed. The proof survives. More explicitly:

1. Repeated differentiation of exp(-u^2-delta u^4) produces a polynomial
   of degree at most 3j at derivative order j: the induction step is
   P -> P'-(2u+4delta u^3)P. Leibniz's rule and the bounded derivatives
   of h give the displayed polynomial majorant. For each fixed j,
   -delta |u|^4+|u|^3-u^2+d_j log(1+|u|) tends to minus infinity.
   This verifies a single epsilon=1 for all orders, with order-dependent
   constants as permitted in Definition 1.2. Positivity of h makes
   log differentiation legitimate everywhere; -2+100/99=-98/99,
   so integrating from zero proves strict decrease globally.
2. The neighborhood majorant for every derivative is integrable at
   both ends because delta>0. Holomorphic differentiation is therefore
   justified locally throughout C, not only along R. For phi_0 the
   Gaussian factor also dominates exp(A|u|) times every fixed power.
   DLMF's sqrt(2pi) normalization and both shifts give exactly G above.
   The two Csordas conventions are distinguished in the corrected
   paragraph; the earlier broad wording did not affect the inequalities.
3. The error estimate uses the absolute value of the full difference
   of the kernels and |exp(itu)|=1 for real t. It is uniform in t for
   each of j=0,1,2. The integration-by-parts endpoint check yields all
   three moments exactly. Dividing by sqrt(pi) gives E_0,E_1,E_2 as
   stated; replacing 1/sqrt(pi) by 1 only enlarges the j=1 error.
   The undamped Gaussian is a comparison kernel, not an asserted
   admissible kernel satisfying the super-Gaussian requirement.
4. For the uniform lower bounds all omitted value and curvature terms
   are nonnegative: the three absolute arguments are at least 3 and
   x^2/4-1/2>=7/4. The endpoint expansions have respectively the
   discarded negative term -exp(-64)/25 and the factored exponent
   differences 10 and 70. Both inequality directions, the positive
   endpoint-7 bracket, and the exponential-series bounds hold.
   After subtracting/adding eta, the strict slack over the four
   required normalized margins is, in displayed conclusion order,

       9419/810000000,
       6419/810000000,
       138817/196830000000,
       2473/270000000.

   For F'(6), slack means the required upper bound minus the actual
   upper bound. These are rational proof bounds, not measured values.
5. Continuity and strictly positive curvature supply exactly one zero
   of F' inside (6,7); positive value and curvature there imply the
   strict negative Laguerre expression with the stated denominator.
   No assertion of global uniqueness of critical points is made.

The supplementary replay command is
`python3 scripts/critical-minimum/fixed-rational-margins-263.py`.
All twelve exact comparisons passed with no failures. The complete
load-bearing `checks` array in
`scripts/critical-minimum/fixed-rational-margins-263.json` was inspected
using `python3 ../scripts/loop/inspect_json.py` with `--pointer /checks
--full`; each actual/required value and strict slack was checked against
this proof. The replay supplies arithmetic only; the analytic audit is
the argument above. This confirms a generic obstruction, not progress
beyond the sources checked or an RH counterexample.

## Mathlib

Full matching coverage for this fixed modulated-kernel counterexample
has not been checked; no absence is claimed. Supporting Gaussian,
integral-differentiation and intermediate-value results may exist, but
no particular Mathlib theorem is imported here. The analytic proof
above supplies every required specialization and perturbation bound.
