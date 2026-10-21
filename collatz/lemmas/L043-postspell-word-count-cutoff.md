# L043 — Fixed-comparison exclusion through twelve postspell words

## Hypotheses

Use the shortcut map T(t)=t/2 at even positive integers and
T(t)=(3t+1)/2 at odd positive integers. Let r>=3 be an integer.
For 0<=i<r let J_i>=2, H_i>=3 and a_i>=0 be integers, with
a_i congruent to 2 modulo 18. Put

\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad
N=\sum_i(4J_i+H_i+a_i).
\]

Assume the concatenation is actual at a positive odd integer n_0>1,
closes at n_0 after N steps, and every junction occurrence is a
positive odd integer 20 modulo 27. Each final even tail is exact.
Independent tails, repeated periods and coincident junction values
are allowed. No least-root, primitive-representation, tail cap,
global-minimum or junction-height-ratio assumption is imposed.
All logarithms are natural.

## Conclusion

There is no such concatenation with **3<=r<=12**.

The upper endpoint 12 is maximal for the following explicitly retained
scalar comparison: L041's fixed inequality N<A(r)log N+B(r), the
integer word-count restrictions

\[
K=\sum_i(3J_i+H_i),\quad L=\sum_i(J_i+a_i),\quad N=K+L,
\]

primitive scaling K=dK_0,L=dL_0 with positive integers d,K_0,L_0,
the imported bound K_0>225640000, and L041's estimate

\[
0<N\log2-K\log3<23r/517.                         \tag{1}
\]

A scalar tuple satisfying all these restrictions exists at r=13.
It is not asserted to be an actual word, an affine closed root or a
positive cycle. Maximality here concerns this initial range for this
specified comparison, not every intermediate estimate in L041 or
other cycle bounds. The separate critical audit below found no defect
within the stated scope and imported qualifications. Universal entry, unrestricted word counts, other
cycles, divergence and eventual descent remain open.

## Proof

### Known inputs and applicability

L041 supplies A(r)=(399/5)Q_r and
B(r)=(264/5+6log r)Q_r+69r/1034, where
Q_r=sum_{j=0}^{r-1}(23/8)^j. Its audited all-r argument gives both
the length inequality and (1), counting all input occurrences and
retaining every independent tail.

Import John Simons and Benne de Weger, *Theoretical and computational
bounds for m-cycles of the 3n+1-problem*, Acta Arithmetica 117 (2005),
51–70, [Corollary 2 and complete proof, printed p. 53; shortcut-map
and period conventions, sections 1.1–1.3, pp. 51–53](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
For a positive nontrivial shortcut cycle its odd count exceeds
225640000. Apply this to the primitive cycle, not to a count of
word boundaries or total steps.

For completeness, L041's period reduction is independent of r. If p
is the least positive return time to n_0, periodicity and division
N=dp+s, 0<=s<p, give T^s(n_0)=n_0. Minimality forces s=0 and
d>=1. The parity list repeats d times, so K=dK_0 and L=dL_0.
Each a_i>=2, hence K>=9r and L>=4r; thus K_0,L_0 are positive.
The junction n_0>=47 makes the closed orbit nontrivial, since {1,2}
is invariant. Both primitive parities occur. Rotating to an E-to-O
transition starts at a strict local minimum: its predecessor is 2u
and its successor is (3u+1)/2, both greater than its odd state u.
Every even state has a smaller successor and every odd state preceded
by an odd state has a smaller predecessor. Thus these transitions
are precisely the full cyclic minima. The source applies at this
actual minimum count, without setting it equal to r. This is the
same applicability bridge audited in L042; its three-word exclusion
is a comparator rather than an additional mathematical input here.

The source proof uses Lemma 1, the published height input
x_min>301*2^50 and continued-fraction denominators 225644606 and
397573379. The height input is attributed to distributed [Ro]
computations, with a Roosendaal personal-communication footnote.
These remain precise published imports; the original certificates
and Crandall's proof are not independently certified. L041's
Hercher Theorem 16, Simons–de Weger Lemma 12 and Rhin qualifications
also remain unchanged. No general cycle theorem is reproved.

Write M=225640000 and C=3M/2=338460000. Since 3^2>2^3,
log3/log2>3/2. Positivity in (1) and Corollary 2 give

\[
N>K\frac{\log3}{\log2}>\frac32K
   \ge\frac32K_0>C.                                  \tag{2}
\]

This uses more than K<N; dropping the positive linear form would
discard a useful established restriction.

### Uniform exclusion for the initial range

For r>=3, Q_r,A(r),B(r) are strictly increasing and positive.
In particular, for 3<=r<=12 and any t>1,

\[
t-A(r)\log t-B(r)\ge t-A(12)\log t-B(12).             \tag{3}
\]

The positive exponential series gives e>163/60>27/10. Therefore
e^3>(27/10)^3=19683/1000>12, so log12<3. Also the exact integers

\[
27^{20}=42391158275216203514294433201
 >33846000000000000000000000000=C10^{20}
\]

give e^20>C, hence log C<20. It follows that

\[
A(12)\log C+B(12)
 <\frac{8334}{5}Q_{12}+\frac{828}{1034}.               \tag{4}
\]

Here 8334=399*20+264+6*3*5. The exact geometric sum and differences
are

\[
Q_{12}=\frac{1460970380836239}{8589934592},\quad
A(12)=\frac{582927181953659361}{42949672960}<C,
\]
\[
C-\frac{8334}{5}Q_{12}-\frac{828}{1034}
 =\frac{610323442974809006259}{11102490460160}
 >54971760>0.                                        \tag{5}
\]

For real t>=C, F(t)=t-A(12)log t-B(12) has derivative
F'(t)=1-A(12)/t>0. Equations (4)–(5) give F(C)>0, so (2)
forces F(N)>0. Equation (3) then contradicts L041's strict
length inequality for every 3<=r<=12. This is an all-real
monotonicity argument, not a finite length screen.

### Scalar feasibility at thirteen words

Set r=13 and take the integer parameters

\[
J_0=4,\ H_0=225639881,\ a_0=131990888;
\qquad J_i=2,\ H_i=3,\ a_i=2\quad(1<=i<=12).
\]

All lower bounds hold and a_0=2+18*7332827. Their sums are
sum J_i=28, sum H_i=225639917 and sum a_i=131990912. Thus

\[
K=225640001,\quad L=131990940,\quad N=357630941.
\]

Take d=1,K_0=K,L_0=L. All primitive scaling and lower-count
restrictions hold, including K_0>M and N>=13r.

To check the transcendental signs rigorously, for x=(t-1)/(t+1)
and t>1 let

\[
S_m(t)=2\sum_{j=0}^{m-1}\frac{x^{2j+1}}{2j+1},\qquad
E_m(t)=\frac{2x^{2m+1}}{(2m+1)(1-x^2)}.
\]

Integrating the geometric series for 2/(1-x^2), or its finite
remainder, gives S_m(t)<log t<S_m(t)+E_m(t). The upper bound
holds because every omitted denominator is at least 2m+1,
strictly greater for later terms. These are explicit rational
bounds at t=2,3. With m=64, exact rational comparisons certify

\[
\frac{6931471805599453}{10^{16}}<\log2
 <\frac{6931471805599454}{10^{16}},
\]
\[
\frac{10986122886681096}{10^{16}}<\log3
 <\frac{10986122886681097}{10^{16}}.
\]

The complete rational bounds and all cross-multiplication checks
are stored in `scripts/postspell-word-count/cutoff-certificate.json`;
the explicit finite-series computation is reproducible by
`python3 scripts/postspell-word-count/certify_cutoff.py`.
No floating-point estimate is used in this certificate. Substituting
the displayed rational bounds with the correct signs gives

\[
\frac12<\frac{40739498685267}{78125000000000}
 <N\log2-K\log3
 <\frac{2607328207492559}{5000000000000000}
 <\frac{53}{100}<\frac{299}{517}=\frac{23r}{517}.       \tag{6}
\]

The length inequality is also satisfied. The factorial-series
bound k!>=2^(k-1) for k>=2, strict for k>=3, gives
e=2+sum_{k>=2}1/k!<3. Since N>3^17=129140163,
log N>17. Finally

\[
A(13)=\frac{13407352604005382967}{343597383680},\qquad
17A(13)-N=\frac{105043938617475067559}{343597383680}>0.
\]

Consequently N<17A(13)<A(13)log N+B(13), since B(13)>0.
All retained scalar restrictions are simultaneously feasible at 13.
Even L041's imported positive lower linear-form estimate would not
reject this tuple: e^(-6.125581)K^(-133/10)<1/K<1/2, whereas
(6) gives a larger positive linear form. No wordwise height or
parity realizability claim follows from these totals.

Because the initial range through 12 is excluded and count 13 is
feasible for precisely these scalar restrictions, 12 is its maximal
initial-range cutoff. This does not prove the existence of a cycle
at 13 or prevent other inequalities from excluding that count.

### Relevance and qualifications

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-08-postspell-word-count-cutoff.md`.
This is REPRODUCTION: known general estimates are imported, and only
their elementary fixed-input optimization is supplied. No novelty
or advance beyond the checked source mathematics is claimed.
The working record is `drafts/2026-10-08-postspell-word-count-calculation.md`.
All 23 exact certificate checks passed, with no failures. The proof
of monotonicity supplies the infinite-length argument that a finite
certificate alone would not give.

Attempt 019's guard-only failure and history 069's full-minimum-count
mismatch are preserved. This calculation uses neither a guard-only
contradiction nor a substitution of r for the full minimum count.
It assumes actual closure only for the exclusion. The scalar tuple
tests the limit of the specified necessary conditions and has no
closure converse. Repeated periods and coincident junction values
are counted by occurrences throughout. Universal entry, arbitrary
counts, other cycles, divergence and eventual descent remain unresolved.
No external Lean build is certified. The separate critical audit is
recorded below.

### Separate critical audit — 2026-10-08

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-08-word-count-cutoff-audit.md`.
Verdict: **no defect found within the stated hypotheses, explicitly
retained scalar restrictions and published input qualifications**.
This REPRODUCTION audit establishes no stronger exclusion, mathematical
repair or new theorem beyond the checked sources. It checks the full
proof above against L041, the audited applicability comparator L042,
and the published Corollary 2 and conventions precisely cited above.
The prior assessment's inspected primary passages are reused; no
new source or stronger odd-count threshold is introduced.

The hypotheses match L041 at every integer r>=3, including all actual
parities, closure, exact independent tails and odd residue-20 junctions.
The half-open word intervals count 3J_i+H_i odd and J_i+a_i even
inputs, retaining occurrences at coincident states. The congruence gives
a_i>=2. Nontriviality follows from n_0>=47 and the invariance of {1,2}:
a closed orbit through n_0 cannot ever enter that invariant cycle.
The least positive return p divides N by division with remainder,
without requiring p to end at a designated word boundary. Repeating
its parity list gives K=dK_0,L=dL_0 with d>=1 and both primitive
counts positive. Rotation to an E-to-O transition supplies the source's
local-minimum convention. Such transitions, rather than designated
junctions, count all cyclic minima; nothing sets that number to r.
Thus the imported Corollary 2 really gives K_0>M=225640000.

L041 supplies strict positivity of Lambda=Nlog2-Klog3 at represented
counts. Since log2>0 and 3^2>2^3, N>(3/2)K>=(3/2)K_0>C.
Both strict inequalities needed at the threshold survive primitive
scaling. At 3<=r<=12, each Q_r increases, the positive factor
264/5+6log r increases, and 69r/1034 increases. Hence A(r),B(r)
increase. Multiplication by log t preserves this ordering for t>=C>1.
The comparison with r=12 therefore covers all the stated counts.

The exponential partial sum through degree five is 163/60, strictly
below e and above 27/10. Its third and twentieth powers justify
log12<3 and log C<20. The exact Q_12,A(12), conservative right
side and margin in (4)–(5) were recomputed using the closed geometric
sum (8/15)((23/8)^12-1), independently of the generator's sum of
powers. The margin is exactly the displayed fraction and exceeds
54971760; the required margin is merely positive. Also A(12)<C.
Consequently F(C)>0 and F'(t)=1-A(12)/t>0 for every real t>=C.
Thus F(N)>0 contradicts N<A(r)log N+B(r). This proves an unbounded
real-length exclusion, not just an integer search up to a finite cap.

For r=13, all thirteen entries of J,H,a were checked as integers
with the stated lower bounds; every tail is 2 modulo 18. Their sums
are exactly 28,225639917,131990912, yielding the displayed K,L,N.
The proposed d=1,K_0=K,L_0=L satisfy positivity, scaling and the
strict imported threshold. This verifies only the specified scalar
conditions: setting d=1 does not assert a primitive parity realization.

For the logarithms, put x=(t-1)/(t+1) in (0,1). Integrating the
finite geometric identity for 2/(1-x^2) gives the displayed positive
series remainder. Each omitted denominator is at least 129 when m=64,
and all after the first exceed 129. The strictly positive tail is
therefore strictly below 2x^129/(129(1-x^2)). This proves the analytic
enclosures; exact computation only evaluates their rational endpoints.
All four complete saved endpoints were independently recomputed by
Horner evaluation of sum_{j=0}^{63}(x^2)^j/(2j+1), followed by
multiplication by 2x and addition of that remainder bound. They agree
exactly with the certificate. Their strict comparisons with the four
displayed decimal rationals also hold by rational arithmetic.

Both N and K are positive. The lower bound for Nlog2-Klog3 must
therefore use the lower log2 bound and the upper log3 bound; the
upper bound uses the opposite endpoints. These signed calculations
give exactly the two fractions in (6). They prove
1/2<Lambda<53/100<299/517, so both positivity and the strict
upper cap hold simultaneously. For the length comparison, k!>=2^(k-1)
for k>=2, strict for k>=3, implies e<3. With N>3^17 this gives
log N>17. The independent geometric calculation gives exactly
17A(13)-N=105043938617475067559/343597383680>305718098>0.
Since B(13)>0, the retained length inequality follows strictly.
Finally c=6.125581>0 and K>1 imply
e^(-c)K^(-133/10)<K^(-1)<1/2<Lambda, verifying the optional
lower-linear-form observation without estimating an exponential.

Reproduction command:
`python3 scripts/postspell-word-count/audit_cutoff.py`.
All **62 independent exact checks passed**, with no failures; complete
actual values, comparison relations and required bounds are in
`scripts/postspell-word-count/audit-certificate.json`.
The verifier reads the existing certificate, does not import the
generator, and leaves its original certificate unchanged. Its arithmetic
checks supplement the analytic and applicability arguments above;
passing flags alone would not prove either of those arguments.

The exclusion through 12 and simultaneous scalar feasibility at 13
justify exactly the claimed maximal initial range. They do not say
that every larger count is feasible, or that any scalar feasible tuple
is an actual orbit. L041's finer per-word height/valuation constraints
and exact affine closure are omitted from this retained system, so
their possible further exclusions remain open. Repetitions and coincident
junctions are retained, and no junction is a presumed global minimum.
Attempt 019 and history 069 remain valid obstructions to their different
mechanisms. No direct mathematical input beyond L041 has been added,
so the DAG and mathematical assembly in PROOF.md are unchanged; this
audit supersedes the overview's pending-audit wording. The published
height computations, Rhin/Crandall originals, external Lean builds and
exact Mathlib coverage remain unchecked. Universal entry, unrestricted
counts, arbitrary cycles, divergence and eventual descent remain open.

## Mathlib

Full matching theorem: **not checked**. Supporting real logarithms,
finite geometric sums, exponential-series bounds, monotonicity and
period/count arithmetic: **not checked** for exact declarations.
No matching theorem, absence from Mathlib or formal verification is
asserted.
