# L076 — Variable-table sufficient early-support criterion

## Hypotheses

Let r>=3 and B>=0 be integers. Fix integer pairs with
2<=J_0<...<J_(r-1) and H_i>=3. All logarithms are natural. Set

\[
K=\sum_i(3J_i+H_i),\quad
N=\sum_i(4J_i+H_i)+2r+18B,\quad
\Lambda=N\log2-K\log3,\quad
E=\frac{23(r-1)}{4\cdot2^{4J_1}-23}.
\tag{1}
\]

For B>0 require the following sufficient tests, all depending only on
the table, budget and chosen rational certificate constants. Choose
rationals lambda,U,T,ell,u,v such that

\[
E<\lambda\le\Lambda,\qquad
R:=\frac{23}{11(\lambda-E)}+\frac{23}{11}\le U\le e^T,
\quad 0<\ell\le\log2,\quad \log3\le u,\quad\log(11/4)\le v.
\tag{2}
\]

Define G_i=(27/16)^{J_i}(3/2)^{H_i} and
Q_i=(12/11)(3/2)^{H_i}+1. For every 0<=i<=r-3 require

\[
Q_i>\frac{23}{11}2^{20}.
\tag{3}
\]

For 0<=k<=r-2 put

\[
A_k=\sum_{i<k}(3J_i+H_i),\qquad
D_k=\sum_{i<k}(4J_i+H_i+2),\qquad A_0=D_0=0.
\]

For each 0<=j<=r-3 require the rational margin test

\[
M_j=(D_{j+1}+18+4J_{j+1})\ell-T-v-A_{j+1}u>0.
\tag{4}
\]

Analytic comparisons in (2) must be certified inequalities, not decimal
approximations. Outward logarithm intervals and a positive partial sum
for exp(T) can certify them when applicable. Conditions (3)–(4) are
finite rational tests. They impose no condition on unknown junctions
or the unknown support. For B=0 no tests (2)–(4) are required.

Let b_i>=0 be integers summing to B, and set a_i=2+18b_i. Suppose
real s_0,...,s_r obey s_r=s_0, s_i>=540/11 and, in literal order,

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+23/11,\qquad
4J_i\log2\le\log s_i+\log(11/4)\quad(0\le i<r).
\tag{5}
\]

These are precisely the endpoint/domain/non-strict own-input J parts of
L051, with every endpoint including closure retained. No H guard, seed,
minimum-location, integer-junction, parity, residue, exact-valuation,
actual-word, primitive-count or count-ray premise is assumed.

## Conclusion

Every such tuple has b_0=...=b_(r-3)=0. For B>0, any hypothetical first
early recipient j would violate its next input's J guard with
left-minus-right margin strictly greater than M_j>0.

The tests recover all 23 audited L073 benchmark cases, each with margin
>9.32, without prescribing the later allocation. This is a sufficient
criterion only: failure of a test implies neither feasibility nor the
existence of early support. B=0 says only that every allocation entry
vanishes; it asserts no feasible tuple. No new table, integer exclusion,
arbitrary-order conclusion or universal eventual-descent theorem is
established. The separate critical audit below found no defect within
these hypotheses and sufficient tests.

This is local REPRODUCTION within the prior SPECIALIZE assessment
`drafts/literature/2026-10-17-variable-table-early-support-criterion.md`.
It makes L073's mechanism portable through explicit data tests; no
originality beyond inspected sources is asserted. L075 motivates a later
order reduction for tables passing both sets of tests, but is not an
input to this proof or an assembled consequence here.

## Proof

### Standard inputs and the changed scope

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
provides formal finite-word affine composition. The table and allocation
give a prescribed finite word of length N with K odd letters; only its
formal affine algebra is relevant, not realization. The prior assessment
inspected the needed induction cases. No general coding theorem is
reproved. The coordinate substitution and estimates below justify the
variable-table specialization of the retained L051 endpoints.

Use [DLMF 4.5.1](https://dlmf.nist.gov/4.5.E1), in particular
log(1+x)<x for x>0, and monotonicity of log/exp on positive real
arguments. Benchmark enclosures are imported from audited L055, L064
and L073. Their analytic certification uses
[DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4) and
[DLMF 4.2.19](https://dlmf.nist.gov/4.2.E19); no new analytic theorem
or fixed-table numerical property is asserted for other tables.

### A guard-conditioned bound on input zero

First suppose B>0 and the tests hold. Put n_i=s_i-23/11>=47 and

\[
\eta_i=\frac{23}{11}-\frac{12}{11}(16/27)^{J_i}
                       -(16/27)^{J_i}(2/3)^{H_i},\quad
c_i=2^{-a_i}G_i.
\]

The powers (16/27)^{J_i} and (2/3)^{H_i} both lie in (0,1), so
the sum of the subtracted terms is strictly between zero and 12/11+1=23/11. Hence
0<eta_i<23/11. Subtracting 23/11 in (5), and using
G_i eta_i=(23/11)G_i-Q_i, gives exactly
n_(i+1)=c_i(n_i+eta_i). The allocation sum implies
prod c_i=3^K/2^N. Multiplication of all r positive ratios, including
closure, therefore gives

\[
\Lambda=\sum_{i=0}^{r-1}\log(1+\eta_i/n_i).
\tag{6}
\]

For each i>=1 the own-input J guard and increasing J give

\[
n_i\ge\frac{4\cdot2^{4J_i}-23}{11}
       \ge\frac{4\cdot2^{4J_1}-23}{11}>0.
\]

Applying log(1+x)<x and eta_i<23/11 separately to those r-1
summands shows their sum is strictly below E. The remaining summand
is strictly below 23/(11n_0). Thus

\[
\lambda\le\Lambda<\frac{23}{11n_0}+E,
\quad 0<\lambda-E<\frac{23}{11n_0},
\quad s_0<R\le U\le e^T.
\tag{7}
\]

Every inversion uses a positive quantity. In particular log s_0<T.
No minimum is selected. Arbitrary later tails occur in (6) through their
full budget and every endpoint; none is assumed to increase its input.

### First-recipient comparison and every boundary case

If early support is nonempty, choose its least index j in [0,r-3].
Integrality and nonnegativity give b_j>=1 and b_i=0 for all i<j.
Consequently a_j>=20, and all preceding tails equal 2.

At every actual input the pre-tail bracket is positive:
G_i s_i-Q_i=G_i(n_i+eta_i)>0. The map
F_(i,a)(s)=2^{-a}(G_i s-Q_i)+23/11 is therefore decreasing in a
at that input. Condition (3) says the affine offset
23/11-2^(-20)Q_i is strictly negative for every early row; it also
implies 23/11-Q_i/4<0. Thus the actual preceding edges give

\[
s_{i+1}<(G_i/4)s_i\quad(i<j),\qquad
s_{j+1}=F_{j,a_j}(s_j)\le F_{j,20}(s_j)<2^{-20}G_j s_j.
\]

All multiplying factors and actual junctions are positive. Combining
these inequalities with (7) yields

\[
\log s_{j+1}
 <T+\sum_{i=0}^{j}(\log G_i-2\log2)-18\log2
 =T+A_{j+1}\log3-(D_{j+1}+18)\log2.
\tag{8}
\]

When j=0 the preceding product is empty and equals 1; the last
strict comparison still proves (8). When j=r-3 the next input is
r-2, whose J guard is among (5); every preceding compared row still
lies in the tested range of (3). The case r=3 has only j=0 and is
covered by the same argument. No comparison is needed on either of
the last two rows. The comparison value at tail 20 need not define a
new trajectory: all inequalities were applied at actual inputs.

Subtracting the next guard's left side from (8), and using certified
upper bounds for log3 and log(11/4) and the lower bound for log2,
gives

\[
\log s_{j+1}+\log(11/4)-4J_{j+1}\log2
 <T+A_{j+1}u-(D_{j+1}+18+4J_{j+1})\ell+v=-M_j<0.
\]

The coefficient A_(j+1) is positive and the coefficient negating log2
is positive, so each enclosure has the stated direction. This contradicts
the non-strict own-input guard. Every nonzero early support has one such
first index, proving the conclusion for all allocations at once.
If B=0, a sum of nonnegative b_i equal to zero forces each b_i=0
directly, without (2)–(4) or any feasibility assumption.

### Complete fixed-table benchmark

Use exactly L055's 25 indexed pairs and B=9250245. Their sums give
K=397573379 and N=630138897 independently of allocation. Select

\[
\lambda=10584/10^{14},\quad U=20\cdot10^9,\quad T=24,
\quad\ell=693147180559/10^{12},
\quad u=1098612288669/10^{12},\quad v=1011600911679/10^{12}.
\]

L055 certifies lambda<Lambda, and L064 certifies all three logarithm
bounds. Here J_1=15 and r-1=24, so (1) is exactly L073's residual
bound E=552/4611686018427387881. Its audited comparisons give

\[
\lambda-E=
\frac{6101253702379434166563}{57646075230342348512500000000000}>0,
\quad R=
\frac{1325859730438202850942226985830949}{67113790726173775832193}
 <20\cdot10^9.
\]

The positive exponential partial sum through degree 40 is

\[
\sum_{k=0}^{40}\frac{24^k}{k!}=
\frac{202750314819830504045671593478515759301}
     {7661655986496068058455078125}>20\cdot10^9,
\]

so U<exp(T). Every early H_i>=40, and L073's exact comparison

\[
\frac{23}{11}2^{20}=\frac{24117248}{11}
 <\frac{36472999400827762787}{3023656976384}
 =\frac{12}{11}(3/2)^{40}+1
\]

proves (3) at every required row by monotonicity in integer H. This
uses the benchmark's verified H bound, not H>=3 alone.

For each j, -10^12 M_j equals exactly the L073/L064 upper-margin
integer U_j: expand A_(j+1) and D_(j+1), or use
A_+=3T_+-4E_- and B_+=T_+-E_- in L073's formula. Thus all 23
published margins are retained, not merely a weaker worst-case test.
Their minimum is M_4=9322534135606/10^12>9.32; at the boundary
recipients M_0=10035584058473/10^12 and
M_22=11258799181634/10^12. The benchmark therefore meets every
test on the complete literal simplex. L055's audited rational witness
has zero early support and proves this instance is not vacuous; its
nonintegrality and the other recorded rational witness are unchanged.

`python3 scripts/postspell-word-count/certify_variable_table_early_support.py`
recomputes the finite specialization. The full evidence is
`scripts/postspell-word-count/variable-table-early-support-certificate.json`.
It retains the table, complete rational operands, prefix counts and all
23 margins, comparing them individually with L064. These checks verify
the specialization of the data tests; the preceding argument, not a
finite search, proves their universal conditional implication. The source
Lambda and logarithm enclosures are reused rather than reproved.
All 52 exact rational checks and eight integer checks pass. Their complete
operands, every prefix/margin record and all integer checks were inspected;
there are no failures. This is construction-time verification; the
separate critical audit follows.

### Independent critical audit — 2026-10-17

The prior SPECIALIZE assessment
`drafts/literature/2026-10-17-variable-table-early-support-critical-audit.md`
approved this exact RESEARCH/REPRODUCTION audit. No defect was found.
The audit verifies the quantified criterion and its existing benchmark,
without a new-table application, an order assembly or an integer exclusion.
The cited affine and positive-real analytic inputs above are reused;
their applicability does not require an integer orbit. L051 contributes
only its endpoint/domain/J definitions, and L055/L064/L073 contribute
only the identified benchmark data and comparisons.

For arbitrary admitted tables, J_1>=3 makes the denominator in E positive.
Subtracting the shift in (5) gives n_(i+1)=c_i(n_i+eta_i), because
c_i eta_i=(23/11)c_i-2^(-a_i)Q_i. The bounds 0<eta_i<23/11
hold for every J_i>=2,H_i>=3 and do not involve the allocation.
Every n_i>=47 is positive, so cancellation of the full cyclic product
is legitimate. Its logarithm is (6) with precisely
N=sum(4J_i+H_i)+2r+18B; the closing tail is included. No
minimum is needed. Each i>=1 guard gives the lower bound used above,
since exponentiating yields s_i>=(4/11)2^(4J_i). Thus all r-1
nonzero-index contributions have sum strictly below E. In particular,
even when lambda=Lambda or R=U=exp(T), strictness in
Lambda<23/(11n_0)+E gives s_0<R and log s_0<T. The positive
residual lambda-E is essential for this inversion; the tests state it
explicitly rather than infer it from feasibility.

For a first early recipient j, every earlier b_i is zero and b_j>=1.
The sign of G_i s_i-Q_i is checked at the actual input before replacing
a_j by 20. Condition (3) guarantees negative offsets for both comparison
tails 20 and 2 on every row needed in the prefix. It asserts no sign
for arbitrary larger tails. The comparison value at tail 20 is at least
the actual positive s_(j+1), so taking logarithms after the positive
multiplier bound is legitimate. The accumulated exponents are exactly
A_(j+1) and D_(j+1)+18, giving (8). Their signs justify every outward
logarithm replacement in (4). A strictly positive M_j makes the next
guard's left-minus-right difference strictly positive, contradicting its
non-strict required sign. This covers all support patterns by their least
early index, without enumerating allocations. At j=0 the prefix is empty;
at j=r-3 all compared rows are still tested and the next input is r-2.
For r=3 these are the same case. Neither of the final two rows needs an
offset comparison. For B=0 nonnegativity alone proves the support
conclusion, with no analytic tests and no existence assertion.

The independent program
`python3 scripts/postspell-word-count/audit_variable_table_early_support.py`
does not import or execute the construction certifier. It separately
transcribes all 25 pairs, checks them against L055 and the original
certificate, and recomputes all totals and parameter bounds. For each
t=2,3,11/4, it uses x=(t-1)/(t+1) and the assessed DLMF 4.6.4
positive-real specialization to enclose log t strictly between

\[
P_{128}=2\sum_{m=0}^{127}\frac{x^{2m+1}}{2m+1}
\quad\hbox{and}\quad
P_{128}+\frac{2x^{257}}{257(1-x^2)}.
\]

Here 0<x<=1/2. The positive tail of the series is bounded above by
replacing its denominators by 257 and summing the geometric series;
later denominators are strictly larger, so the upper bound is strict.
This independently verifies all six L064 logarithm grid ends and both
L055 Lambda bounds, with opposite log interval ends in the cancellation
N log2-K log3. The residual, root cap, 41-term exponential sum and
smallest-H offset comparison are recomputed as exact fractions and
agree with the displayed operands above. Monotonicity in H then covers
every required early offset, without constructing enormous powers.

For each j=0,...,22, direct prefix sums reconstruct A_(j+1),
D_(j+1) and the complete integer numerator 10^12 M_j. These agree
individually with the negatives of all 23 published L064 numerators.
This also checks the expansion of L073's formula, rather than assuming
the formula's asserted equality. The unrounded logarithm intervals give
an independent rejection lower bound strictly larger than each M_j.
All 52 original rational records (operands, differences, relations and
verdicts), all eight integer checks and all 23 prefix/margin records
are reconstructed exactly. The minimum remains at j=4, with
M_4=9322534135606/10^12>9.32; both boundary values match those above.

The full evidence is
`scripts/postspell-word-count/variable-table-early-support-audit-certificate.json`.
All 130 independent checks pass, with no failures. The certificate keeps
the original certificate's SHA-256, every unrounded logarithm term and
remainder, full Lambda interval, exponential terms, every reconstructed
comparison and every independently bounded margin. Complete selected
Lambda, rational-check, prefix/margin, integer-check and summary values
were inspected. The original certificate is unchanged. Numerical checks
verify the benchmark; the symbolic argument supplies all-table conditional
coverage and the r=3/B=0 cases. The direct mathematical inputs and
argument are unchanged, so no DAG or overview change is needed.

Both no-early-support rational witnesses and Attempts 026–031 remain
valid. A failed sufficient test establishes neither feasibility nor early
support. The criterion supplies no new-table last-pair arithmetic, combined
order consequence, unrestricted cycle exclusion or universal descent.

## Mathlib

Full matching coverage is unchecked; no absence claim is made. Standard
logarithm and affine facts are supporting inputs, not a formalization of
this table criterion. The finite certificate is exact rational arithmetic,
not a Lean proof or evidence of an actual Collatz cycle.
