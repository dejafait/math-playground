# L045 — Fixed retained-transfer scalar cutoff at seventeen words

## Hypotheses

Use the shortcut map T(t)=t/2 at even positive integers and
T(t)=(3t+1)/2 at odd positive integers. Let r>=3 be an integer and
let J_i>=2,H_i>=3,a_i>=0 be integers, with a_i congruent to 2 modulo
18, for 0<=i<r. Put W_i=(OOEO)^{J_i}O^{H_i}E^{a_i} and
D_i=4J_i+H_i+a_i. Assume W_0...W_(r-1) is actual at a positive
odd n_0>1, returns to n_0, and its junction occurrences n_i are
positive odd integers congruent to 20 modulo 27. Every final tail
is exact. Independent tails, repeated periods and coincident states
are allowed. Define

\[
K=\sum_i(3J_i+H_i),\quad L=\sum_i(J_i+a_i),\quad N=K+L.
\]

These are input-time counts. No least-root, first-return, primitive
representation or global-minimum assumption is imposed. Logarithms
are natural. The published general cycle inputs retain the qualifications
specified below.

## Conclusion

No such closed concatenation exists for **3<=r<=17**, subject to the
published inputs. This extends the restricted thirteen-word exclusion;
it supplies no unrestricted word-count bound or universal descent.

For every r>=3 the fixed forward transfer h_(i+1)+1<2(h_i+1),
with the existing seed and prefix/length estimates, gives

\[
K<U_r(N):=\frac{15}{4}(2^r-1)
       \left(\frac{133}{10}\log N+9+\log r\right),             \tag{1}
\]
\[
N<A_r\log N+B_r,\quad
A_r=\frac{399}{5}(2^r-1),\quad
B_r=(54+6\log r)(2^r-1)+\frac{69r}{1034}.                     \tag{2}
\]

Seventeen is maximal for the **specified assembled scalar system**:
integer parameters and the displayed exact total-word counts;
positive integer d,K_0,L_0 with K=dK_0,L=dL_0,K_0>225640000;
(1), (2), N<(8/5)K+69r/1034; and

\[
e^{-6.125581}K^{-133/10}<\Lambda:=N\log2-K\log3<23r/517.
                                                               \tag{3}
\]

An integer scalar tuple satisfies all these conditions at r=18.
This system omits individual junction heights, individual valuation
bounds, exact input parities and affine integer closure. Its feasibility
is neither a word realization nor a cycle. No optimality among those
omitted conditions or other transfer mechanisms is claimed. The separate
critical audit below found no defect within these qualifications; this is
not a complete Collatz candidate.

## Proof

### Inputs and applicability

L041 proves the all-r occurrence partition and seed, own-word prefix
bound and length conversion. It also gives the upper/lower linear-form
estimates in (3). Its primitive reduction counts repeated input times:
the least return period p divides N, say N=dp, and K=dK_0,L=dL_0.
Both primitive counts are positive since each representation has odd
and even inputs. Each junction is at least 47, so its closed orbit is
nontrivial and never enters the invariant shortcut cycle {1,2}.

The precise general inputs imported there are Christian Hercher,
*There are no Collatz m-Cycles with m <= 91*, JIS 26 (2023),
Article 23.3.5, [Theorem 16 and proof, printed pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
and John Simons and Benne de Weger, *Theoretical and computational
bounds for m-cycles of the 3n+1-problem*, Acta Arith. 117 (2005),
51–70, [Lemma 12, printed p. 61; period conventions p. 52](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
The represented linear form and reciprocal mass scale by d. L041
justifies both estimates without substituting r for the full cyclic
local-minimum count. Its Rhin and published computation qualifications
remain imports. Hercher's inspected June 2026 correction does not
amend Theorem 16; amended Theorem 21 is not used.

Import from Simons–de Weger the same paper's
[Corollary 2 and complete proof, printed p. 53](https://www.impan.pl/shop/en/publication/transaction/download/product/82263):
the primitive nontrivial cycle has K_0>M=225640000 odd inputs.
No fixed-m hypothesis restricts this corollary. The primitive orbit
meets its conventions after rotation to any even-to-odd transition;
these transitions count the full cyclic minima, not just the r
designated word boundaries. Its proof imports x_min>301*2^50 from
distributed [Ro] computations with a Roosendaal personal-communication
footnote, and continued-fraction denominators 225644606 and 397573379.
Original certificates and Crandall's proof are not locally verified.

All these applicability checks are the established L041/L043 bridge.
No general cycle theorem is reproved. L043 also supplies the elementary
e<3 and certified log2/log3 enclosures used for the scalar witness.

### Fixed-transfer assembly for every r

Cyclically relabel occurrences to choose n_0=min_i n_i, resolving
ties arbitrarily, and put h_i=log(n_i+23/11)>0, P_i=4J_i+H_i.
L041 (6), (7), (11) give

\[
h_0<\frac{133}{10}\log N+8+\log r,\quad
P_i<\frac{15}{4}h_i+3,\quad
N<\frac85K+\frac{69r}{1034}.                              \tag{4}
\]

L044's transfer proof (3)–(6) is wordwise: it uses precisely L041's
own-index valuation bounds, h_i>0 and a_i>=2. It does not use thirteen
in those lines. In particular, with delta=log3/log2 and c_J=log(11/4),
its positive-coefficient substitution gives at every index

\[
h_{i+1}<\frac{3\delta^2}{4}h_i
 +\frac{\delta(3\delta-4)}4c_J
 <\frac{48}{25}h_i+\frac{32}{75}<2h_i+1.                    \tag{5}
\]

The shifts are already accounted for by L041's exact endpoint and
s_(i+1)<G_i s_i. Thus (5) retains both offsets, independent exact
tails and each occurrence's own parameters. Applying this existing
finite-word implication at r occurrences is the specialization here;
L044's thirteen-word conclusion is not assumed to cover all r.

Induction from j=0 to r-1 gives
h_j+1<=2^j(h_0+1), with equality permitted at j=0. Since
P_j<(15/4)(h_j+1), and K=sum(P_j-J_j)<sum P_j,

\[
K<\frac{15}{4}\sum_{j=0}^{r-1}(h_j+1)
 \le\frac{15}{4}(2^r-1)(h_0+1)<U_r(N).
\]

This traverses indexed occurrences even if state values coincide.
Substitution in the last inequality of (4) gives (2), because
(8/5)(15/4)=6. Every tail remains in N through that conversion.

### Exclusion on the entire real length ray through r=17

Put C=3M/2=338460000. Since 3^2>2^3, positivity of Lambda and
primitive scaling imply

\[
N>K\frac{\log3}{\log2}>\frac32K\ge\frac32K_0>C.            \tag{6}
\]

A_r and B_r are positive and strictly increasing for integer r>=3.
For real t>=C>1 and 3<=r<=17 their right sides in (2) are at
most the r=17 right side. The elementary exponential-series estimates
already used in L044 give e>163/60>27/10. Therefore

\[
27^3=19683>17000,\qquad
27^{20}=42391158275216203514294433201
 >C10^{20}=33846000000000000000000000000
\]

prove log17<3 and log C<20. With R_17=131071,

\[
A_{17}=52297329/5<C,
\]
\[
A_{17}\log C+B_{17}
 <1668\cdot131071+1173/1034=226059727725/1034<C,
\]
\[
C-226059727725/1034=123907912275/1034>119833000>0.           \tag{7}
\]

For F(t)=t-A_17 log t-B_17, F'(t)=1-A_17/t>0 on every
real t>=C, and (7) gives F(C)>0. Consequently (6) implies
F(N)>0, contradicting (2) for any 3<=r<=17. This is an
all-real contradiction, not a finite screen of lengths or parameters.

### Simultaneous scalar feasibility at r=18

Set every J_i=2, and set

\[
H_0=225639842,\quad a_0=131990870=2+18\cdot7332826,
\qquad H_i=3,\quad a_i=2\quad(1<=i<=17).
\]

Their sums are sum J_i=36, sum H_i=225639893 and
sum a_i=131990904. Thus

\[
K=225640001,\quad L=131990940,\quad N=357630941.
\]

Take d=1,K_0=K,L_0=L. All integer guards, counts and scaling hold,
and K_0>M. This choice of d does not assert a primitive orbit.
L043's proved e<3, together with N>3^17=129140163, gives log N>17.
Also log18>0. Exact rational comparisons give

\[
K<1848894579/8
 =\frac{15}{4}(2^{18}-1)\left(\frac{133}{10}\cdot17+9\right)
 <U_{18}(N),                                               \tag{8}
\]
\[
N<955878500448/2585
 =(2^{18}-1)\left(\frac{399}{5}\cdot17+54\right)+1242/1034
 <A_{18}\log N+B_{18}.                                    \tag{9}
\]

The separate conversion constraint holds too, since
N<8K/5<8K/5+1242/1034. No upper bound on a single tail is
added to the retained system.

For these same K,N, L043's exact logarithm enclosures give

\[
\frac12<\frac{40739498685267}{78125000000000}<\Lambda
 <\frac{2607328207492559}{5000000000000000}
 <\frac{53}{100}<\frac{414}{517}.                          \tag{10}
\]

The upper cap is now 23r/517=414/517. The lower bound in (3)
also holds: c=6.125581>0 and K>1 imply
e^(-c)K^(-133/10)<1/K<1/2<Lambda. Hence all retained scalar
constraints hold simultaneously at eighteen. Neither the huge H_0
nor the huge a_0 is claimed to satisfy omitted individual heights or
actual parity conditions.

For independent reproducibility of the arithmetic, the certificate
reevaluates L043's positive series
S_m(t)=2 sum_{j=0}^{m-1}x^(2j+1)/(2j+1), x=(t-1)/(t+1), at
t=2,3,m=64. Its proved strict enclosure is
S_m(t)<log t<S_m(t)+2x^(2m+1)/((2m+1)(1-x^2)). The saved complete
rational endpoints lie strictly inside the decimal brackets
(6931471805599453,6931471805599454)/10^16 for log2 and
(10986122886681096,10986122886681097)/10^16 for log3.
Multiplying with positive N,K and reversing the log3 endpoint
selection gives exactly (10). The established analytic enclosure is
reused; reevaluation checks transcription and the changed cap.

Reproduction command:
`python3 scripts/postspell-word-count/certify_retained_range.py`.
All 99 exact checks pass, with complete actual/required bounds in
`scripts/postspell-word-count/retained-range-certificate.json`.
The first provisional allocation failed a_0's congruence; its complete
failed certificate remains in
`scripts/postspell-word-count/retained-range-initial-certificate.json`.
Only the corrected allocation above is a witness. Exact checks support
the analytic argument and do not establish orbit realizability.

Thus seventeen is the maximal initial cutoff for the stated assembled
scalar system. This does not say every count greater than eighteen is
feasible or that (5) cannot be strengthened with additional information.
Stop this fixed comparison at its certified first failure. Attempt 019
and history 069 retain their different failures; neither is reopened.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-09-retained-transfer-word-count-range.md`;
the working record is `drafts/2026-10-10-retained-transfer-range-calculation.md`.
This is REPRODUCTION: local quantitative assembly of known inputs, with
no claim of originality or progress beyond the checked general sources.
Universal entry, unrestricted counts/cycles, divergence and eventual
descent remain unresolved. Published computation inputs, Rhin/Crandall
originals and external Lean coverage are not upgraded by this calculation.

### Separate critical audit — 2026-10-10

The separate audit used the prior SPECIALIZE assessment
`drafts/literature/2026-10-10-retained-transfer-range-audit.md`.
**Verdict: no defect found in the stated exclusion or scalar maximality.**
This verifies the existing local specialization; it gives no stronger
range, new theorem beyond the checked sources or complete Collatz proof.

L041's hypotheses match every actual word here. Its half-open input
intervals partition all N times, including a junction only at its outgoing
word. The finite-word reciprocal estimate therefore sums with multiplicity
even at coincident states. Positivity, n_i>=47 and closure exclude {1,2}.
The least return period divides N: writing N=dp+u, 0<=u<p, periodicity
gives T^u(n_0)=n_0, hence u=0. Thus K=dK_0,L=dL_0 and the reciprocal
mass scale together. The cited primitive estimates give the represented
upper bound and lower bound: d exp(-c)K_0^(-133/10) is at least
exp(-c)(dK_0)^(-133/10). No source minimum count has been replaced by r.
The precise Hercher Theorem 16 and Simons–de Weger Lemma 12 and
Corollary 2 citations above, with their published qualifications, suffice;
their general theorems and underlying computations are not reproved.

For the seed, combining the lower linear form with
Lambda<(23r/11)/b, b=min n_i, gives b<(23r/11)exp(c)K^(133/10).
Since 23/(11b)<1/20, c<25/4 and log(23/11)<1, L041's shift costs
less than 73/10<8, exactly as required in (4). The selection is of a
designated occurrence, not a global orbit minimum; ties cause no issue.
The seed's log r remains present throughout the assembly.

The own-index valuation bridge was checked: the exact final tail implies
v_2(y+1)=H, whence v_2(11y+23)=2 for H>=3, and the affine OOEO
identity gives v_2(11n_i+23)=4J_i+2. These yield the two logarithmic
bounds used by L044 at that same index. Its substitution coefficients
log2, delta-1 and 3delta-4 are positive. The coefficient of h_i after
both substitutions is delta+delta(3delta-4)/4=3delta^2/4.
Using delta<8/5 and 0<c_J<4/3 gives the constants 48/25 and 32/75;
the residual difference to 2h_i+1 is (2/25)h_i+43/75>0.
The exact endpoint includes both -(12/11)(3/2)^H and -1.
With a_i>=2 and G_i s_i>=540/11, its shifted upper bound is
s_(i+1)<G_i s_i/4+23/11<G_i s_i. Thus no tail cap, omitted offset
or unproved height-ratio assumption enters (5).

The resulting implication is wordwise, so using it at arbitrary r
does not import L044's thirteen-word conclusion outside its hypotheses.
The induction starts with equality at index zero and visits all r time
occurrences. The geometric sum is 2^r-1, and P_i<(15/4)(h_i+1)
because 3<15/4. Summing K=sum(P_i-J_i)<sum P_i proves (1).
The length identity and Lambda<23r/517 give
N<(8/5)K+69r/1034 using log3/log2<8/5 and log2>2/3.
Thus every tail remains in N and multiplication by (8/5)(15/4)=6
gives exactly (2).

The primitive threshold and positive Lambda give N>(3/2)K>C,
without identifying K with N or K_0. For r>=3, both positive
factors of (54+6log r)(2^r-1) increase, as do A_r and the remaining
term of B_r. Since log t>0 for t>=C, r=17 dominates every required
right side. Independently summing the exponential series through degree
five gives 163/60>27/10. The exact powers in (7) prove log17<3
and log C<20. Exact recomputation gives A_17=52297329/5<C,
the conservative RHS 226059727725/1034<C, and positive margin
123907912275/1034>119833000. The derivative 1-A_17/t is positive
on every real t>=C. These checks verify the entire real-ray
contradiction; checking a finite set of lengths would not suffice.

All eighteen J,H,a entries were inspected and independently checked for
integrality, guards and tail congruences. Their sums are precisely
36,225639893,131990904, giving K=225640001,L=131990940,N=357630941.
The independently checked d,K_0,L_0 are positive integers and satisfy
both scaling equations and K_0>M. The generator's use of d*K in its
scaling check is valid for this particular d=1,K_0=K witness; the
independent verifier instead checks d*K_0 and d*L_0 explicitly.
The aggregate lower RHS values in (8)–(9) and the stronger N<8K/5
comparison were recomputed. Since e<3, N>3^17 and log18>0, they
strictly imply all three retained aggregate inequalities simultaneously.

For each t=2,3, integrating the finite geometric identity for
2/(1-x^2), x=(t-1)/(t+1) in (0,1), gives the positive log-series
remainder. Every omitted denominator is at least 129, and later ones
are strictly larger. Hence its strict upper bound is
2x^129/(129(1-x^2)), as used by the generator. Independent Horner
evaluation of sum_(j=0)^63 (x^2)^j/(2j+1), multiplied by 2x,
and addition of this remainder reproduced all four complete rational
endpoints exactly. Their strict decimal-bracket comparisons passed.
Positive N,K require the lower log2 and upper log3 endpoints for the
lower Lambda bound, with the opposite choices for its upper bound.
These give exactly the two fractions in (10), so
1/2<Lambda<53/100<414/517. Finally c>0, K>1 and 133/10>1 give
exp(-c)K^(-133/10)<1/K<1/2. Both linear-form restrictions therefore
hold for this same tuple, rather than for separate witnesses.

The complete generator and all 99 original actual/required comparisons
were inspected. Independent verification:
`python3 scripts/postspell-word-count/audit_retained_range.py`.
All 336 exact checks passed, including the 99 original comparison
replays and their saved flags. Full actual/required evidence and input
hashes are in `scripts/postspell-word-count/retained-range-audit-certificate.json`.
The verifier neither imports nor executes the generator and preserves
both original certificates byte for byte. It confirms the initial
a_0=131990860 has residue 10 modulo 18 instead of 2. That failed
allocation is preserved and supports no feasibility claim; the corrected
a_0=131990870 has the required residue 2.

The analytic proof, not a finite computation, establishes the range
exclusion. The feasible scalar tuple establishes the first failure only
for the explicitly retained system. Individual height compatibility,
parity, integer closure and existence of a primitive orbit are not
asserted. Attempt 021's stop remains; Attempts 019 and history 069 are
not reopened. L041, L043 and L044 remain the direct inputs already
recorded in DAG.md. No argument or dependency changed, so PROOF.md and
DAG.md are unchanged; this canonical verdict supersedes the overview's
pending-audit wording for L045. Published computation certificates,
Rhin/Crandall originals, external Lean and matching Mathlib coverage
remain unchecked. Universal entry, unrestricted counts/cycles,
divergence and eventual descent remain unresolved.

## Mathlib

Full matching theorem: **not checked**. Exact supporting declarations
for logarithm bounds, geometric sums, monotonicity and count arithmetic:
**not checked**. No absence claim or formal verification is made.
