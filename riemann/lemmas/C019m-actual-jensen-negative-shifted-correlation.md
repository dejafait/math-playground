# C019m — Full-band square and negative actual-Jensen correlation

## Hypotheses

Use the actual xi and polynomial conventions of C019j, the finite real
sum S_d and heat family of C019k, and the elementary functions of C019l.
Thus d tends to infinity through positive integers,
\[
 d=\frac{T}{2\pi}\left(\log\frac{T}{2\pi}-1\right),\quad T>2\pi e,
 \qquad X=\frac{T}{\sqrt{2d}},\quad q=\log X,
 \quad B=(\sqrt2-1)X,\quad h=\frac{3\pi}{q}.
\]
Write J=[X,sqrt(2)X], D=[X,sqrt(2)X-h]. For Y in J define
\[
 r(Y)=T^2/Y^2,\quad
 P(Y)=\frac{(-1)^d A_d(-r(Y))}{N_d^{\rm norm}(r(Y))},\qquad
 N_d^{\rm norm}(r)=\frac{(d!/d^d)r^d e^d m(T/\sqrt r)}{\sqrt{2\pi d}}.
                                                               \tag{1}
\]
Here A_d is C019j's rescaled reciprocal Jensen polynomial and m is
its strictly positive gamma modulus. N_d^norm denotes C019j's positive
normalization, never C019k's floor. In each S_d argument use exactly
\[
 t_d(Y)=Y^2/(2d),\qquad
 N_d(Y)=\left\lfloor\sqrt{Y/(2\pi)+Y^2/(32d)}\right\rfloor.
\]
Both factors at Y and Y+h retain their own time, floor and normalization.
There is no RH, nonvanishing, simple-zero or heat real-zero hypothesis.

## Conclusion

For absolute constants and all sufficiently large d,
\[
 \int_J |S_d(Y)|^2\,dY=O(Xq),                                \tag{2}
\]
and
\[
 \left|\int_D\{P(Y)P(Y+h)-S_d(Y)S_d(Y+h)\}\,dY\right|
        =O(X/\sqrt q)=o(Bq).                                \tag{3}
\]
With exactly C019l's constant K from its (1),
\[
 \int_D P(Y)P(Y+h)\,dY=Bq K+O(X\log q),\qquad
 K\leq-\frac{2}{3\pi}.                                      \tag{4}
\]
In particular, beyond one common existential onset,
\[
 \int_D P(Y)P(Y+h)\,dY\leq-\frac{Bq}{3\pi}.                  \tag{5}
\]
These are local specializations of assessed classical methods and
existing notebook comparisons. No originality determination, effective
onset, quantitative ordered sign samples, root count or RH conclusion
is asserted. The separate conceptual audit1385 below retains (2)--(5)
without changing their hypotheses, constants or error orders.

## Proof

### Reused inputs and exact full-band entry domains

The specialization gate is assessment
`drafts/literature/2026-11-17-jensen-correlation-transfer-second-moment-1381.md`
(review1382, SPECIALIZE). It covers the square and product payment;
neither was already stated by the inspected source theorems. We import
the following classical estimates, not reprove them: H. Kösters,
*On the Occurrence of the Sine Kernel in Connection with the Shifted
Moments of the Riemann zeta function*, arXiv:0803.1141v2,
5 September 2008, [Appendix A, Lemmas A.2 and A.3](https://arxiv.org/html/0803.1141v2#A).
A.2 bounds |integral exp(iF)| by 8/sqrt(epsilon) for a real twice
differentiable F with either F''>=epsilon>0 throughout or
F''<=-epsilon throughout. A.3 states
\[
 \sum_{1\leq m<n\leq M}
 \frac1{\sqrt{mn}\log(n/m)}=O(M\log M).
                                                               \tag{6}
\]
These are Titchmarsh, *The Theory of the Riemann Zeta-function*,
second edition, Lemmas 4.4 and 7.2. Integral Cauchy--Schwarz will be
used below on finite intervals with square-integrable factors.

Use C019l (4)--(12) on the whole closed J, not its nonzero-shift
correlation conclusion with h replaced by zero. For clarity the exact
elementary data are
\[
 \ell(Y)=\log(Y/(2\pi)),\quad v_n(Y)=\ell(Y)/2-\log n,
 \quad\vartheta(Y)=Y\ell(Y)/2-Y/2-\pi/8,
\]
\[
 a_n(Y)=n^{-1/2}\exp\left\{\frac{t_d(Y)}4
                     (v_n(Y)^2-\pi^2/16)\right\},\quad
 f_n(Y)=\vartheta(Y)-Y\log n+\frac{\pi t_d(Y)}8v_n(Y),
\]
\[
 V(Y)=2\sum_{n\leq N_d(Y)}a_n(Y)\cos f_n(Y).
                                                               \tag{7}
\]
With M=N_d(sqrt(2)X)=O(sqrt X), those results give, uniformly for
Y in J and every n<=M even before its entry,
\[
 S_d(Y)=-V(Y)+O(X^{-3/4}),\quad |S_d(Y)|+|V(Y)|=O(X^{1/4}),
                                                               \tag{8}
\]
\[
 |a_n|\leq C/\sqrt n,\quad |a_n'|\leq C/(X\sqrt n),\quad
 f_n''=1/(2Y)+O(q/d),\quad d\asymp X^2q^2.
                                                               \tag{9}
\]
These bounds have no nonzero-shift premise. They include all floor
thresholds. The reduction error in the square is paid directly:
\[
 \left|\int_J(S_d^2-V^2)\right|
 \leq\int_J|S_d+V|(|S_d|+|V|)=O(\sqrt X).                    \tag{10}
\]

Put U_d(Y)=Y/(2pi)+Y^2/(32d), and let r_k>0 solve U_d(r_k)=k^2.
Since U_d is strictly increasing, k<=N_d(Y) is exactly Y>=r_k.
Consequently the unshifted pair domain is the actual interval
\[
 J_{mn}=[\max(X,r_m,r_n),\sqrt2X],\quad 1\leq m,n\leq M,
                                                               \tag{11}
\]
interpreted as empty if its left endpoint exceeds its right endpoint.
Singleton intervals contribute zero. No endpoint or floor is replaced
by an asymptotic cutoff. On J_{mn} set A_{mn}=a_ma_n. Equation (9)
gives
\[
 \sup|A_{mn}|+\int_{J_{mn}}|A_{mn}'|
       \leq C/\sqrt{mn}.                                    \tag{12}
\]
The functions being differentiated here are smooth on all of J; the
floor only determines integration domains and is never differentiated.

### Both channels of the square

The finite cosine product formula gives exactly
\[
 \int_J V^2
 =2\sum_{m,n\leq M}\int_{J_{mn}} A_{mn}(Y)
       \{\cos(f_m-f_n)+\cos(f_m+f_n)\}\,dY.                  \tag{13}
\]
For the entire sum channel, (9) implies
\[
 (f_m+f_n)''=1/Y+O(q/d)\geq1/(4X)                            \tag{14}
\]
at one sufficiently large onset, uniformly in all indices and all
Y in J. Indeed 1/Y>=1/(sqrt(2)X) and Xq/d tends to zero.
The cited second-derivative estimate bounds the unweighted integral
on every subinterval of J_{mn} by C sqrt X. Integrating against
its primitive and using (12) bounds the weighted complex integral,
and therefore its real part, by C sqrt X/sqrt(mn). Summation costs
\[
 C\sqrt X\left(\sum_{n\leq M}n^{-1/2}\right)^2
       \leq C\sqrt X M=O(X).                               \tag{15}
\]
This includes the equal indices and possible stationary first
derivatives at entry; no first-derivative test was used in this channel.

For unequal indices in the difference channel put eta=log(n/m)!=0
and c_0=pi/8. Differentiating the explicit (7), or using C019l (11),
gives the exact identities
\[
 (f_m-f_n)'=(1+c_0Y/d)\eta,\qquad
 (f_m-f_n)''=c_0\eta/d.                                    \tag{16}
\]
In particular the first derivative has modulus at least |eta|.
Integration by parts, for F=f_m-f_n, reads
\[
 \int_{J_{mn}} A_{mn}e^{iF}
 =\left[\frac{A_{mn}e^{iF}}{iF'}\right]_{\partial J_{mn}}
   -\int_{J_{mn}}e^{iF}
       \left(\frac{A_{mn}'}{iF'}-
                         \frac{A_{mn}F''}{i(F')^2}\right).
\]
The two endpoint terms and the A' integral cost
C/(sqrt(mn)|eta|). The remaining integral costs at most
CX/(d sqrt(mn)|eta|), by (12)/(16). Thus the full bound is
C/(sqrt(mn)|eta|), since X/d is eventually bounded. Applying (6)
to both orders m<n and n<m makes all unequal-index difference
terms together O(M log M)=O(sqrt X log X). This explicitly handles
their entry endpoints; no derivative monotonicity assumption is hidden.

For the equal-index difference terms the cosine is exactly 1 and
the integrand is a_n(Y)^2<=C/n. Their sum is bounded by
\[
 2\int_J\sum_{n\leq N_d(Y)}a_n(Y)^2\,dY
 \leq C B(1+\log M)=O(Xq).                                 \tag{17}
\]
Combining (10), (13), (15)--(17) gives
\[
 \int_J S_d^2
 \leq C\{Xq+X+\sqrt X\log X+\sqrt X\}=O(Xq),                \tag{18}
\]
which proves (2) on the complete band. S_d is a finite sum of smooth
terms on finitely many entry intervals, so these are ordinary finite
integrals; all functions used are square-integrable.

### Every normalized product error

For Y in J the argument r(Y)=T^2/Y^2 is in [d,2d]. C019j (1)
therefore applies to (1) with exactly its positive normalization and
heat time Y^2/(2d). Combining it with C019k (3) gives
\[
 E(Y):=P(Y)-S_d(Y),\qquad
 \sup_J|E|\leq\epsilon_d=C_1/\log d+C_2X^{-1/4}=O(q^{-1}).    \tag{19}
\]
To verify the last rate without an unstated relation between scales,
C019l (4) gives log d=L+log(L-1) and
q=L/2-(log(L-1))/2+log(sqrt(2)pi), so log d is comparable to q.
Also qX^{-1/4} tends to zero. These hold at a common onset.

For Y in D, both Y and Y+h belong to J because 0<h<B eventually.
By change of variable and nonnegativity, (2) bounds each of
integral_D |S_d(Y)|^2 and integral_D |S_d(Y+h)|^2 by CXq.
Expand the product difference exactly as
\[
 E(Y)S_d(Y+h)+S_d(Y)E(Y+h)+E(Y)E(Y+h).                       \tag{20}
\]
Using integral Cauchy--Schwarz separately for both cross terms yields
\[
 \left|\int_D\{P(Y)P(Y+h)-S_d(Y)S_d(Y+h)\}\,dY\right|
 \leq2\epsilon_d\sqrt{|D|}\sqrt{CXq}+|D|\epsilon_d^2
 \leq C X(\epsilon_d\sqrt q+\epsilon_d^2)
 =O(X/\sqrt q).                                             \tag{21}
\]
All three terms of (20) are paid; in particular no pointwise
envelope replaces the needed square estimate. Equation (21) divided
by Bq is O(q^(-3/2)), proving the required little-o in (3).

### Negative margin and one common onset

Now use C019l (2), with its actual nonzero shift h=3pi/q, to obtain
\[
 \int_D P(Y)P(Y+h)
 =Bq K+O(X\log q)+O(X/\sqrt q).
\]
Since q tends to infinity, the last term is absorbed into O(X log q).
This proves (4). The ratio of its absolute error to Bq is at most
C log q/((sqrt(2)-1)q), which tends to zero. Choose an integer onset
so this is at most 1/(3pi). Then K<=-2/(3pi) proves (5).
Equivalently, (21) is smaller than any fixed positive portion of
C019l's Bq negative margin eventually, meeting the proposed test.

All thresholds used are finitely many absolute eventual conditions:
the onsets of C019j, C019k and C019l; q>1, 0<h<B;
the lower bound (14); X/d bounded; comparability of log d and q;
qX^(-1/4) bounded; and the final margin inequality. Their maximum
is one integer d_0 independent of Y and all indices. No effective
value for d_0 is asserted. All normalizations are positive and no
division by xi, zeta or a possibly zero reference value was used.

### Independent conceptual audit1385 — 17 November 2026

The audit retains (2)--(5). It uses the prior SPECIALIZE coverage in
`drafts/literature/2026-11-17-jensen-correlation-transfer-audit-1383.md`,
completed by review1384, and the already audited local inputs. The
following verification concerns the new square and normalized transfer;
it does not reopen C019l's coefficient calculation or import a general
moving-weight moment theorem.

**Real functions and closed domains.** C019k defines S_d as a real part,
so S_d^2=|S_d|^2. The polynomial coefficients in C019j are real, and
N_d^norm is strictly positive, so P is also real. Since Y>0,
r(X)=2d, r(sqrt(2)X)=d, and r is decreasing. Further,
T/sqrt(r(Y))=Y exactly. Thus C019j (1) applies with precisely the
gamma modulus m(Y), polynomial A_d, parity (-1)^d and heat time
Y^2/(2d) in (1). Conjugation makes C019k's lower-half-plane modulus
equal to C019j's upper-half-plane modulus. No possibly zero xi or
reference value is a denominator.

For each finite d, U_d'(Y)=1/(2*pi)+Y/(16d)>0 on the positive
axis; its unique positive root r_k of U_d(r_k)=k^2 gives
k<=floor(sqrt(U_d(Y))) if and only if r_k<=Y, including equality.
Therefore every term of (13) has exactly (11) as its domain. M is
finite. Empty intervals have no terms, and singleton intervals have
zero integral. Extending a_n and f_n to all of J before entry is
legitimate by C019l (8), (11)--(12); no floor is differentiated.

**Square and both channels.** The finite identity
4*cos(u)*cos(v)=2*cos(u-v)+2*cos(u+v) gives the factor 2 in
(13), with both ordered pairs retained. C019l's whole-band bounds give
sup|A_mn|<=C/sqrt(m*n) and |A_mn'|<=C/(X*sqrt(m*n));
integration over an interval of length at most B proves (12).
They also give the integrable pointwise bound
|S_d^2-V^2|<=C*X^(-1/2), proving (10) over length B=O(X).
This estimate does not require continuity across a source entry.

For F=f_m+f_n, its exact smooth second derivative is
1/Y+O(q/d), with one absolute error constant for all pairs. Since
X*q/d tends to zero and 1/Y>=1/(sqrt(2)*X), F''>=1/(4X)
throughout J beyond one onset. Kösters v2 A.2, with this positive
lower bound, applies to every subinterval of every J_mn. If
H(y)=integral_a^y exp(iF(r)) dr, then sup|H|<=C*sqrt(X), and
integration by parts in integral A_mn*H' gives a bound
C*sqrt(X)*(sup|A_mn|+integral|A_mn'|). This verifies (15),
including m=n and stationary first derivatives: sum n^(-1/2)
is at most 2*sqrt(M), so the entire channel is O(sqrt(X)*M)=O(X).

For F=f_m-f_n with m!=n, t'=Y/d and v_m-v_n=log(n/m)
give exactly F'=(1+pi*Y/(8d))*eta and F''=pi*eta/(8d).
Consequently |F'|>=|eta| for either sign of eta. The endpoint
and amplitude-variation terms of (16)'s integration by parts are
O(1/(sqrt(m*n)*|eta|)). Its remaining term is bounded by
sup|A_mn|*length(J_mn)*pi/(8*d*|eta|), hence by
C*X/(d*sqrt(m*n)*|eta|). This proves the claimed bound uniformly
without assuming monotonicity of a first derivative. Kösters v2 A.3
pays the m<n sum and its swapped copy. Equal-index difference terms
have phase zero and cost at most C*B*sum_{n<=M}1/n=O(Xq).
Thus every term of (13), including all entry endpoints, is paid.
Finally sqrt(X)*log(X)=O(X) and sqrt(X)=O(X), yielding (18).

**Every normalized product term.** C019j (1) and C019k (3) are
absolute errors after division by the same m(Y), so their triangle
inequality gives (19) directly on the whole closed J. The exact
identities log(d)=L+log(L-1) and
q=L/2-log(L-1)/2+log(sqrt(2)*pi) imply log(d)/q tends to 2.
Also q*X^(-1/4) tends to zero. Hence one absolute constant bounds
epsilon_d*q for all sufficiently large integers d.

Once 0<h<B, D is a nonempty finite interval and D+h is contained
in J, as is D itself. Substitution Z=Y+h proves
integral_D |S_d(Y+h)|^2=integral_{D+h}|S_d(Z)|^2<=C*Xq;
nonnegativity gives the same bound on D. All factors are square
integrable: S_d is bounded and piecewise smooth with finitely many
entries, and P is smooth on J with a positive smooth normalization.
For each of the two distinct cross terms, integral Cauchy--Schwarz
therefore gives epsilon_d*sqrt(|D|)*sqrt(C*Xq). The error-error
term is at most |D|*epsilon_d^2. These are exactly the three terms
of (20), not merely one symmetric representative. Since |D|<=B,
their sum is O(X/sqrt(q))+O(X/q^2)=O(X/sqrt(q)). Dividing by
Bq=(sqrt(2)-1)*Xq gives O(q^(-3/2)), verifying (3).

**Margin and simultaneous onset.** C019l (2) uses the identical
D, nonzero h, S_d and K, with both moving times and floors. Its
O(X*log(q)) error absorbs (21). The combined absolute error divided
by Bq tends to zero, so it is at most 1/(3*pi) eventually.
Together with K<=-2/(3*pi), this proves (5) with its stated constant.
All index dependence above was removed before choosing thresholds:
M<=C*sqrt(X), |v_n|<=Cq and the amplitude/phase constants hold
uniformly on J. The finitely many input onsets and conditions
q>1, h<B, X*q/d sufficiently small, X/d bounded,
log(d)/q bounded above and below, q*X^(-1/4) bounded, and the
last error ratio are each eventual consequences of the exact scales.
Their finite maximum is one integer d_0, independent of Y,m,n.
It is existential; no numerical onset is certified.

No defect in (1)--(21) was found. This audit verifies a local
specialization/reproduction, not a stronger estimate or a newly cited
source theorem. No finite numerical test, RH-equivalent positivity,
unpaid infinite interchange or zero-free premise enters. The integrated
negative mean supplies neither a separated-sample count nor a solution
to any of the independent root-count and global gaps below.

### Qualifications and remaining gap

The proof establishes the exact assessed transfer, with both channels,
all pair entries, both actual times and floors, and every normalized
error product retained. The source estimates are imported by precise
citation. The specialization is needed because ordinary fixed-weight
moments do not supply these moving coefficients or entry intervals.
It does not reprove the classical oscillatory estimates or C019l's
already audited signed-correlation calculation.

The conclusion is an integrated sign result. It supplies no quantitative
distribution of ordered disjoint sign samples, margins at such samples,
c*sqrt(d) additional roots, or separation from the existing bulk count.
Those independent gaps, every-degree Jensen hyperbolicity, and actual-Xi
all-degree positivity remain unresolved. Stops1345/1355/559 and parked
direct (A) retain their previous scope. This is not an RH candidate.

## Mathlib

Full matching coverage is not checked. No Mathlib theorem identifier
for (2)--(5) is asserted. Finite-sum identities and integral
Cauchy--Schwarz would only support parts of the proof. The load-bearing
oscillatory inputs are Kösters v2 A.2--A.3 with the hypotheses verified
above; the actual-Jensen comparisons are the stated local inputs.
