# Signed core Type I/II source comparison2101

One literature-only step on review2100's exact target. The main gap is
L030-L032/C032a actual-Xi all-degree algebraic mixed positivity. The
intermediate target remains the full signed core energy
O_(h,epsilon)(X^(1/2+epsilon)), for every epsilon>0 and all sufficiently
large real X. A successful upper would supply quantitative arithmetic
control for C034r's detector, but would not itself prove subpower energy,
the required cumulative upper, or mixed positivity.

## Exact local object and source reuse

Read C034r's hypotheses, conclusions and relevant Fourier/operator proof;
C034u's complete signed square and primitive reduction; C034v's full
cap/operator interface; C034w's Fourier formula and audited tail. In
C034w(7), write W(u)=Xi(u-i/4) times the Fourier transform of Jh. Its
P_X(u) retains the factor (n/X)^(1/4), the positive Fourier phase,
mu(n), and log(X/n)n^(-1/2), on precisely X/2<n<=X. C034w's
Plancherel formula identifies the core with the integral over
|u|<=4 log X of |W(u)P_X(u)|^2/(2pi). This is an existing formula,
not a new specialization. The target is integrated energy, not a
pointwise assertion at u=0. Failure to estimate that single point
alone would not disprove an integrated estimate; a neighborhood or
an appropriate averaged theorem must be addressed.

Reused source-notes2096's fixed-form-correlation, different-state Gram
and Cotlar comparisons, and source-notes2093's Mertens/Abel coverage.
Read stops2076/2077/2079/2084/2087/2089 and localization-stop2100.
The local pole survives only in its stated local scope; the complete
diagonal transform remains uncontinued at its proposed boundary.
Neither is a global impossibility result for the present upper.
Read the October21 overlap assessment and external-input register:
the registered strict fixed half-planes do not supply this signed norm
estimate, and nonvanishing alone is not a reciprocal-series bound.
No cross-notebook input was used.

## Primary finite identity actually retrieved

H. A. Helfgott and L. Thompson, *Summing mu(n): a faster elementary
algorithm*, Research in Number Theory **9** (2023), article6,
[publisher Section2, (2.1) and following displayed identity](https://doi.org/10.1007/s40993-022-00408-8).
Read the complete identity paragraph and its comparison with Vaughan's
identity. For integer K>=1, integer n>=1 and real z>=n^(1/K), it states

    mu(n) = sum_(j=1)^K (-1)^(j-1) binom(K,j)
            sum_(m_1...m_j r_1...r_(j-1)=n; all m_i<=z)
            mu(m_1)...mu(m_j).

The r_i are unrestricted positive integers. The authors explicitly
correct the extra r_K in Iwaniec--Kowalski, *Analytic Number Theory*
(2004), (13.38). Their K=2 formula retains 2mu(n)1_(n<=z); it is
not an identity consisting only of its convolution term. The Main
Theorem, also read, concerns computational running time, not a bound
on the size of M(x). No algorithmic exponent is an analytic saving.
No reproof or application of this identity is performed in this turn.

## Analytic comparison and essential cases read

Ben Green and Terence Tao, *Quadratic uniformity of the Mobius function*,
[arXiv:math/0606087v2](https://arxiv.org/html/math/0606087v2),
22 September2007, Sections3-5. Read Section3's multiplicative versus
nonmultiplicative distinction, Proposition3.2, Lemma4.1 and its full
proof, Proposition4.2 and both proof cases, and (1.3).

Lemma4.1 assumes positive integer U,V,N with UV<=N and gives exact
Type I/II sums on N<n<=2N. Its coefficients are
a_d=sum_(bc=d,b<=U,c<=V)mu(b)mu(c) and
b_d=sum_(c|d,c>V)mu(c). Type I has d<=UV; Type II has
V<d<=2N/U and max(U,N/d)<w<=2N/d. Proposition4.2, for bounded f
and correlation at least delta, permits either a large Type I average
or a large four-point multiplicative rectangle average. The Type II
range is V/2<=D<=4N/U and N/4<=DW<=4N. Its proof removes arithmetic
coefficients by Cauchy--Schwarz and removes the hyperbolic cutoff
before the rectangle test. Section3 expressly separates multiplicative
phases, requiring arithmetic information, from this harmonic method.
Davenport's (1.3) saves arbitrary fixed logarithmic powers for linear
additive phases, not a fixed power of N. The auxiliary cutoff/divisor
lemmas are cited by the source, not independently audited here.

K. Matomaki, X. Shao, T. Tao and J. Teravainen,
*Higher uniformity of arithmetic functions in short intervals I.
All intervals*, Forum of Mathematics, Pi **11** (2023), e29,
[publisher article, DOI10.1017/fmp.2023.28](https://www.cambridge.org/core/journals/forum-of-mathematics-pi/article/higher-uniformity-of-arithmetic-functions-in-short-intervals-i-all-intervals/6DF08E2A3EFABB2DD0DA6CDA38649B18).
Read Theorem1.1(i), Lemma2.16 with its full displayed-identity proof,
and Definition4.1. Theorem1.1(i) assumes X>=3,
X^(5/8+epsilon)<=H<=X^(1-epsilon), a filtered nilmanifold of fixed
degree/dimension and complexity <=delta^(-1), and Lipschitz norm
<=delta^(-1). Its maximal Mobius correlation is bounded by
C delta^(-O(1)) H log^(-A)X, for each fixed A>0. Lemma2.16 describes
dyadic convolution factors and short Mobius factors; Definition4.1
requires second moments for both Type II coefficient sequences and
a fourth moment for the second. This is not a theorem for arbitrary
vector weights. No nilsequence realization of the present logarithmic
phase, power-saving consequence, or dyadic reconstruction is imported.
The later inverse theorems and their proofs were not audited.

## Comparison with the required threshold

The finite identity covers exact arithmetic coefficients but supplies
no cancellation estimate. The Green--Tao inverse theorem is a
dichotomy; a large rectangle is an allowed conclusion, not an upper
bound. Its unrestricted bounded-f formulation does not assert a
power saving for the actual P_X. The newer theorem above supplies
stronger phase classes and shorter intervals, but still only fixed
logarithmic savings with explicit geometric hypotheses. Those classes
cannot be silently replaced by n^(iu) with a moving window and a
frequency integral. A formal Taylor approximation with unbounded
degree or uncontrolled Lipschitz constants would not check them.

The target would require an energy improvement from C034w's available
unsigned O_h(X) envelope to O_(h,epsilon)(X^(1/2+epsilon)). Even an
X times arbitrarily high *fixed* inverse-logarithmic power does not
state that exponent. This is a strength comparison, not a new estimate
obtained by applying the sources. No conclusion is drawn about all
possible refinements of Type I/II methods.

All small/short/long factor ranges and the original strict/inclusive
window must survive an actual application. None of the retrieved
theorems supplies their signed recombination at the requested power.
Triangle or Cauchy--Schwarz bounds for a finite decomposition may be
legitimate, but their accumulated losses must be paid; identities do
not pay them. The complete quadratic square still includes every
cross term. Deleting these terms, assuming they are favorable, or
substituting a bound uniform in freely chosen coefficients would
change the problem. No calculation of the actual rectangle phase,
new bound, or obstruction theorem is asserted here.

## Bounded decision and separate continuation

Park the **direct theorem-import** route: exact identity coverage is
now available, but the retrieved analytic theorems do not establish the
power or the actual-state hypotheses. No essential access blocker
remains for this comparison. Further searches merely for another
finite identity are unjustified. Reopening requires a new signed
estimate or an inspected theorem with the missing power/uniformity.

A separate, finite diagnostic is nominated in review2101. It tests
whether frequency averaging with this actual W can support the
coefficient-blind balanced-block estimate one might use after
Cauchy--Schwarz. It is not an estimate for Mobius coefficients or a
weakening offered in place of the target. In contrast to the
unrestricted operator norm and different Riesz state in2096, it
fixes h, the theta kernel and the logarithmic band, and restricts
both factors to a balanced rectangle. A positive-power obstruction
there would identify a specific loss that any signed mechanism must
avoid. No outcome of that diagnostic is proved in this literature turn.
There is not yet a justified creative signed mechanism; the source
gap is a missing arithmetic estimate, not missing identity algebra.

## Search and verification limits

Queries included `Heath Brown identity Mobius function Type I Type II
sums identity mu n K 1982`, `Mobius exponential sums Davenport bound
Type I Type II small frequency uniform theorem`, `Mobius n^{it} Type II
bound`, and `Mobius logarithmic Heath-Brown sums bilinear`. Followed
the exact Mobius-identity result to its publisher, then the primary
Green--Tao text and the newer publisher theorem. The original1982
Heath-Brown article and Iwaniec--Kowalski's full chapter were not read;
they are references through the inspected sources, not separately
verified inputs. Nonprimary search hits were locators only. The
recent almost-all-intervals sequel is an unread lead, not coverage for
every real X. No novelty is inferred from these bounded searches.

Targeted duplicate searches used C034 proofs and November21
gamma/Mobius literature and attempt paths. They found no inspected
actual-fixed-state balanced-rectangle diagnostic; this is not an
exhaustive novelty search. Full matching Mathlib coverage is unchecked.
No lemmas or mathematical scripts were written; no mathematical
exploration budget, supervisor state or routing counters were changed.
