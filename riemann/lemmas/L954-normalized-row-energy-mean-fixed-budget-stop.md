# Lemma 954: normalized row-energy means and a fixed-budget enclosure stop

## Hypotheses

Use L019's actual positive theta kernel K and L058's domination.
Use exactly L938(5)–(10), including all34 integer coefficients c_alpha,
twelve labelled factors per row, their factorials, and the retained
M_0^12 normalization. At lambda=0 put

    M_j = integral_0^infinity u^j K(u)du,
    A_k = M_(2k)/(2k)!, B_k = M_(2k+2)/(2k)!, 0<=k<=6,
    V_plus = sum_(c_alpha>0) c_alpha h_alpha,
    V_minus = sum_(c_alpha<0) (-c_alpha) h_alpha,
    m_s = integral V_s(E)dE, b_s = integral E V_s(E)dE,
    mu_s(dE) = V_s(E)dE/m_s, s in {plus,minus}.

Numerical statements assume precisely L037's directed Decimal basic
operations and correctly rounded nearest exponential widened by its
adjacent values. All three contexts have precision100. Invalid
operations, overflow, underflow, subnormal arithmetic and divisors
containing zero are rejected. The Decimal implementation is not
independently verified. Integer and rational operations are exact.
No mean inequality, stochastic order, determinant sign, contact,
positive semidefiniteness, zero-location or RH premise is assumed.

## Conclusion

Both mu_s are probability measures on [0,infinity) with finite first
moments and strictly positive finite normalizers. Their exact masses
and first moments are the following finite positive sums:

    T_alpha = product_(k=0)^6 A_k^alpha_k,
    U_alpha = sum_(k:alpha_k>0) alpha_k B_k A_k^(alpha_k-1)
                                  product_(j!=k) A_j^alpha_j,
    m_plus/minus = sum_(+/-c_alpha>0) |c_alpha| T_alpha,
    b_plus/minus = sum_(+/-c_alpha>0) |c_alpha| U_alpha.             (1)

In particular the proposed increasing-convex order mu_minus <=icx
mu_plus necessarily requires

    delta := b_plus/m_plus - b_minus/m_minus >= 0.                 (2)

The one prescribed full-theta calculation, using64 equal panels on
[0,2], theta indices1..4, midpoint Taylor remainder order8 and
precision100, produces a complete enclosing interval I_delta with

    -8.574*10^-7 < inf I_delta < 0 < sup I_delta < 8.576*10^-7,
    width(I_delta)>1.714*10^-6.                                   (3)

Its full endpoints are in `scripts/heat/normalized-row-energy-mean-109.json`.
Thus neither sign branch of the mean test is certified. This fixed
budget ends inconclusively without refinement. The interval containing
zero does not prove that the exact delta is zero, negative or positive.
It neither refutes nor establishes the proposed order or an H2 sign.

For every full moment M_0,M_2,...,M_14 the omitted positive contribution
is below2.114*10^-22; the full quadrature error is also paid. Both
normalizers satisfy

    6.33069*10^-25 < m_s < 6.33070*10^-25.                         (4)

This is a local specialization and numerical-method budget failure,
not a mathematical discovery beyond the sources assessed. There is
no actual-Xi all-degree mixed-positivity or RH conclusion.

## Proof

### Labelled-factor moments and applicability of the necessary test

L938 defines f_k(x)=x^(k-1/2)K(sqrt(x))/(2(2k)!) for x>0,
and h_alpha as the convolution of twelve labelled such factors.
Substitution x=u^2 gives

    integral f_k(x)dx = A_k,
    integral x f_k(x)dx = B_k.                                   (5)

All these integrals are strictly positive by L019 and finite by L058.
The energy power changes the numerator moment to M_(2k+2); its
denominator remains (2k)!, not (2k+2)!.

Choose labelled indices k_1,...,k_12 with multiplicities alpha.
Tonelli for nonnegative functions gives

    integral h_alpha(E)dE = product_(i=1)^12 A_(k_i),
    integral E h_alpha(E)dE
       = sum_(i=1)^12 B_(k_i) product_(j!=i) A_(k_j).              (6)

For example, in the second formula E is the sum of the twelve
nonnegative factor energies, and linearity splits that sum before
integrating. Grouping equal labels in (6) gives (1). No permutation
or multinomial coefficient is introduced. There are rows of each
sign (e.g.64 and-120), so each m_s is a finite nonempty sum of
strictly positive products. The same argument proves finite b_s.
Thus the stated normalization defines integrable probability laws.
No A_0 factor is cancelled from the original densities; all twelve
factors and L938's M_0^12 convention are retained.

Import the definition and scalar stop-loss characterization of
increasing-convex order from Lasse Leskela and Matti Vihola,
*Conditional convex orders and measurable martingale couplings*,
Bernoulli23(4A)(2017),2784–2807,
[arXiv:1404.0999v3](https://arxiv.org/pdf/1404.0999v3),30 October2015,
Sections1.1/2.1 and Proposition2.3 in Section2.2, printed pp.1,4,5.
These passages were inspected in the prior assessment. The scalar
result applies to integrable probability laws, as just proved.
The nonnegative increasing convex test phi(E)=max(E,0) equals E
on both supports. Its order inequality is exactly (2). Equivalently,
this is the zero-threshold case of the cited stop-loss criterion.
No equal-mean assumption or coupling theorem is imported or reproved.
Every other threshold remains unpaid. A mean pass alone would not
establish mass comparison, exponential-test applicability, H2 signs
or any of the independent global gaps.

### Complete full-theta tails through M14

For k=0,2,...,14 and u>=0, u^k<=exp(14u). On[0,1] use u^k<=1;
on[1,infinity) use k log u<=14u. Put X=exp(2u). Each positive theta
summand satisfies, by3<pi<4 and dropping its negative term,

    0<K_n(u)<=128 n^4 exp(9u/2)exp(-3n^2 X).                     (7)

For integer n>=1, n^4<=16^(n-1) and
n^2>=1+3(n-1), the latter difference being(n-1)(n-2)>=0.
Consequently, since X>=1 and16exp(-9)<1/2,

    sum_(n>=1) n^4 exp(-3n^2 X) <=2exp(-3X).

The full moment integrand is at most256exp(37u/2-3X).
Under du=dX/(2X), its residual power is X^(33/4)<=X^9.
Since exp(4)>50, the spatial tail u>2 is therefore at most

    E_space =128 exp(-150) sum_(j=0)^9
                         [9!/(9-j)!]50^(9-j)/3^(j+1).            (8)

This is nine integrations by parts in integral_50^infinity X^9
exp(-3X)dX, after enlarging the domain from X>exp(4).

For omitted theta indices n>=5, integrate(7) times exp(14u) over
all u>=0, not only[0,2]. The resulting upper bound is

    64 sum_(n>=5) n^4 integral_1^infinity X^9 exp(-3n^2 X)dX.

For X>=1, -3n^2 X<=1-3n^2-X. Enlarge the remaining integral to
[0,infinity) to obtain9!. Write n=5+j. Then
n^4<=625*16^j and n^2>=25+11j, since j(j-1)>=0.
As16exp(-33)<1/2, this proves the complete bound

    E_theta=64*9!*625*2 exp(-74)=29,030,400,000 exp(-74).          (9)

The complement of the retained rectangle u<=2,n<=4 is covered by
(8)+(9). Any overlap double-counts positive mass harmlessly. Thus
each full M_k receives[0,E_space+E_theta]. This explicitly extends
the method through M14; L917's M12 constant is not assumed to do so.

The finite positive series through degree7 at4 exceeds50; the one
through degree4 at9 exceeds32. They justify exp(4)>50 and both
geometric ratios. The producer verifies these inequalities exactly.
Its outward tail intervals give

    E_space<6.359*10^-49, E_theta<2.114*10^-22,
    E_space+E_theta<2.114*10^-22.                                 (10)

The rational checker also encloses each needed exponential without
the Decimal exponential: for x in{74,150}, put
P=sum_(j=0)^1000 x^j/j!. The positive remainder is at most
(x^1001/1001!)/(1-x/1002), because all subsequent ratios are at
most x/1002<1. Reciprocating the resulting bounds on exp(x)
encloses exp(-x). Both complete rational intervals are saved in
the checker certificate and lie inside the producer's tail intervals.

### Fixed finite integration and row arithmetic

Use the inspected unchanged interval/jet primitives in
`scripts/hankel/certify_hankel.py` under L037's contract. The three
contexts are set to100 digits before any evaluation. Pi uses L037's
96-term rational Machin enclosure. Each spatial panel is
[2p/64,(2p+2)/64], with midpoint(2p+1)/64 and h=1/64,
for p=0,...,63. These cover the entire[0,2], including endpoints.

The finite kernel jet is exactly
sum_(n=1)^4 exp(u/2)(8v^2-12v)exp(-v), v=pi n^2 exp(2u).
For u^k its normalized derivative jet has coefficient
binom(k,j)u^(k-j) for j<=k and zero otherwise, truncated only
above derivative order8. This remains valid for k=10,12,14.
L036's product/exponential recurrences enclose all coefficients.
At the midpoint they give a_j; on the full panel the eighth
coefficient encloses f^(8)(u)/8!. The finite integrand is C^8.
Thus L036 gives the complete enclosure

    2 sum_(j=0,2,4,6) a_j h^(j+1)/(j+1)+[-R,R],
    R=(2h^9/9) max absolute endpoint of the eighth coefficient.    (11)

Sum all64 enclosures and add[0,(E_space+E_theta)_upper]. All
operations are directed outward; no moment midpoint is substituted.
Every full moment has a positive lower endpoint. For orientation,

    8.987750630*10^-6 < M14 <8.987761156*10^-6.

The summed quadrature remainder upper bounds, conservatively rounded
outward, are:

|Moment order|Quadrature remainder upper bound|
|---:|---:|
|0|6.566*10^-11|
|2|3.533*10^-11|
|4|2.167*10^-11|
|6|1.441*10^-11|
|8|1.027*10^-11|
|10|7.784*10^-12|
|12|6.240*10^-12|
|14|5.263*10^-12|

The complete unrounded eight moment intervals, all512 panel
integrals, midpoint even coefficients, eighth coefficients, error
intervals, finite totals and tails are retained in the certificate.
These bounds justify the full moments, rather than a sampled kernel
or truncated-theta approximation.

Evaluate(1) using nonnegative row products before any probability
division. All34 canonical coefficients and exponents are parsed
without substitution; every row is checked to have12 factors and
weighted degree12. Each summand in U_alpha uses B_k with the original
factorial(2k)!, preserving the size-bias factor. Summing separately
by coefficient sign and then dividing gives(3)–(4). As an enclosing
consistency check, also evaluate

    (b_plus*m_minus-b_minus*m_plus)/(m_plus*m_minus).

Its interval overlaps the directly subtracted mean interval; overlap
alone is not sign evidence and is not used to narrow(3). All divisors
are strictly positive. Both means lie between1.44815057 and1.44815144.
The common tail upper bound is much smaller than the saved spatial
Taylor error bounds; no assertion is made that changing one error
source would suffice. The stopping rule prohibits refinement here.

### Complete evidence, replay and limits

Run from the notebook:

```text
python3 scripts/heat/normalized-row-energy-mean-109.py
python3 scripts/heat/check-normalized-row-energy-mean-109.py
```

The producer writes `scripts/heat/normalized-row-energy-mean-109.json`.
The exact-rational checker writes
`scripts/heat/check-normalized-row-energy-mean-109.json`.
Both completed without failures or exceptional arithmetic. The
checker verifies input hashes, the exact partition and fixed budget,
all512 saved panel integrations/remainder operations, all8 full
moment sums, both complete rational tails and all34 canonical rows.
It independently expands each first moment into twelve labelled-factor
replacements (408 terms total), checking multiplicities and shifted
moment factorials against the grouped computation. It replays the
masses, first moments, final divisions and both delta expressions
with exact rational endpoint arithmetic, and verifies the numerical
thresholds(3),(4),(10). The complete relevant moments, normalizers,
means, tails, exceptional flags and failed-sign result were inspected.

This replay does not independently reimplement the derivative jets,
the Decimal exponential or the interval library. Their inclusion
rests on the inspected formulas, L036/L037 and the stated library
contracts. A later independent conceptual/code audit is still absent.
The current canonical result is the reproducible conditional enclosure
and its failure to certify the necessary sign, not an independent
audit or a claim of exact-law incompatibility.

C938a's density-ratio obstruction and the L916 score-curvature,
L918 origin, L943 field and L949/L953 compact/tail stops keep their
original scopes. None implies the exact normalized energy mean sign.
Full normalized order, independent mass comparison and exponential
comparison would all still be required for the proposed d=2 use;
other degrees, initialization, contacts, realization and global
continuation remain unresolved. The fixed mean enclosure route is
parked without a parameter, precision or representation campaign.

## Mathlib

Full matching coverage and specialized supporting coverage have not
been checked; availability is unknown, not asserted absent. The
finite Decimal certificate is not Lean-formalized. The standard
Tonelli theorem and imported increasing-convex-order criterion are
used only with the hypotheses verified above.
