# L049 — Twenty-word exact-transfer scalar obstruction

## Hypotheses

Let T(t)=t/2 for even positive integers and T(t)=(3t+1)/2 for odd
positive integers. O and E specify actual input parities. For 0<=i<20
let J_i>=2,H_i>=3,a_i>=0 be integers, with a_i congruent to 2 modulo
18. Set W_i=(OOEO)^{J_i}O^{H_i}E^{a_i}, D_i=4J_i+H_i+a_i and
N=sum_i D_i. Assume W_0...W_19 is actual at a positive odd integer
n_0>1, T^N(n_0)=n_0, and each junction occurrence
n_i=T^(D_0+...+D_(i-1))(n_0) is positive, odd and 20 modulo 27.
Set n_20=n_0. Every final even tail is exact. Independent tails,
repeated periods and coincident junctions are allowed. No least-root,
first-return, global-minimum, primitive-representation or relative-height
assumption is made. These are exactly L041's hypotheses at r=20.
All logarithms are natural. Retain the published qualifications below.

For the scalar obstruction only, N is a test length; it is not asserted
to arise from words satisfying these hypotheses.

## Conclusion

Define delta=log3/log2, c_J=log(11/4), q=3 delta^2/4 and
b=delta(3 delta-4)c_J/4. For x>1 put

\[
S(x)=\sum_{j=0}^{19}x^j,\qquad
U(x)=\sum_{j=0}^{19}\sum_{k=0}^{j-1}x^k
     =\frac{S(x)-20}{x-1}.
\]

Any actual closed concatenation in the hypotheses necessarily satisfies

\[
N<R(N):=\frac{399}{5}S(q)\log N
       +6(8+\log20)S(q)+6bU(q)+96+\frac{1380}{1034}.
                                                        \tag{1}
\]

The source count threshold requires N>C=338460000. However, the scalar
length N_*=370000000 satisfies

\[
545558861<R(N_*)<632443324,\qquad
N_*>C,\qquad N_* > (8/5)225640000.                    \tag{2}
\]

Thus (1) does not exclude the required entire real count ray at twenty
words. Stop this fixed scalar comparison. No simultaneous height
assignment, parameter counts, primitive counts, parity realization,
integer closure or actual cycle is established by N_*. This is neither
a Collatz counterexample nor an optimality claim for other estimates.
The separate critical audit below found no defect within the stated
hypotheses and published qualifications. Universal entry, unrestricted
counts/cycles, divergence and eventual descent remain unresolved.

## Proof

### Applicability of the unchanged inputs

L041 gives K=sum_i(3J_i+H_i), L=sum_i(J_i+a_i), N=K+L, and
primitive scaling K=dK_0,L=dL_0 with integer d>=1. The junctions are
at least 47 and a_i>=2, so this is a nontrivial positive integer
cycle, outside the invariant shortcut cycle {1,2}. Counts refer to
input times, including repetitions, rather than distinct state values.
Cyclically relabel so that n_0=min_i n_i, resolving ties by any one
occurrence. This does not identify n_0 with the global orbit minimum.
Set s_i=n_i+23/11, h_i=log s_i>0 and P_i=4J_i+H_i. L041 (6), (7)
and (11), specialized only in their count, give

\[
h_0<(133/10)\log N+8+\log20,\quad
P_i<(15/4)h_i+3,\quad N<(8/5)K+1380/1034.           \tag{3}
\]

L044 (5) is a wordwise implication before its thirteen-word assembly:

\[
h_{i+1}<q h_i+b.                                    \tag{4}
\]

Its hypotheses are supplied at each occurrence by L041's own-index
bounds 4J_i log2<=h_i+c_J and
H_i log2<h_i+J_i log(27/16). The endpoint keeps both shifts:
s_(i+1)=2^(-a_i)[G_i s_i-(12/11)(3/2)^{H_i}-1]+23/11,
where G_i=(27/16)^{J_i}(3/2)^{H_i}. L046's applicability passage
checks that s_i>=540/11 and a_i>=2 give
s_(i+1)<G_i s_i/4+23/11<G_i s_i, independently of the word count.
The substitutions in L044 (4)–(5) have positive multipliers
delta-1 and log(27/16). Thus (4) applies here without importing a
thirteen-, eighteen- or nineteen-word conclusion at twenty words.
Neither the seed nor the numerical prefix bound is sharpened.

The precise source imports behind (3) are Christian Hercher,
*There are no Collatz m-Cycles with m <= 91*, JIS 26 (2023),
Article 23.3.5,
[Theorem 16 and complete proof, printed pp. 10–11](https://cs.uwaterloo.ca/journals/JIS/VOL26/Hercher/hercher5.pdf),
and John Simons and Benne de Weger, *Theoretical and computational
bounds for m-cycles of the 3n+1-problem*, Acta Arith. 117 (2005), 51–70,
[period conventions p. 52; Lemma 12 and complete proof p. 61](https://www.impan.pl/shop/en/publication/transaction/download/product/82263).
L041 supplies their positive-cycle applicability and represented-period
scaling. The inspected June 2026 Hercher correction leaves Theorem 16
unchanged; amended Theorem 21 is not used. No general cycle theorem
or transcendence estimate is reproved here.

Import Simons–de Weger's same published version,
[Corollary 2 and complete proof, printed p. 53](https://www.impan.pl/shop/en/publication/transaction/download/product/82263):
the primitive nontrivial positive cycle has K_0>M=225640000.
The established positive linear form N log2-K log3 and
delta>3/2 (from 3^2>2^3) give

\[
N>\delta K>(3/2)K\ge(3/2)K_0>C.                    \tag{5}
\]

The full local-minimum count is not set to twenty selected junctions.
These imports are reused from the approved source assessment rather
than independently recertified.

### Twenty occurrences, including the additive sum

Here q>1 and b>0. Induction along the nineteen edges i=0,...,18
in (4) gives, for 0<=j<=19,

\[
h_j\le q^j h_0+b\sum_{k=0}^{j-1}q^k.
\]

The j=0 case is equality; the other cases follow by multiplying the
previous bound by q>0 and adding b. Thus every one of the twenty
outgoing word inputs is covered, including coincident junctions at
different times. Summation yields
sum_j h_j<=S(q)h_0+bU(q). To check the geometric identity, the power
q^k occurs in U exactly 19-k times for 0<=k<=18; equivalently each
inner sum is (q^j-1)/(q-1). Hence (q-1)U=S-20.

Since K=sum_i(P_i-J_i)<sum_i P_i, (3) gives

\[
K<(15/4)[S(q)h_0+bU(q)]+60.
\]

Multiplying by 8/5 and substituting the unchanged seed in (3) gives
(1), including the constant 96 and every additive transfer contribution.
All final tails remain in N through the cycle identity used for (3).
The closing edge is omitted only from this necessary upper estimate;
closure is still essential for the cycle inputs. L048 supplies this
assembly pattern and the logarithm enclosure method, not a theorem
about twenty words.

### Certified scalar obstruction with both terms retained

The finite-integral logarithm enclosure proved in L048 is as follows.
For t>1, x=(t-1)/(t+1) and a positive integer m,

\[
0<\log t-2\sum_{k=0}^{m-1}\frac{x^{2k+1}}{2k+1}
 <\frac{2x^{2m+1}}{(2m+1)(1-x^2)}.
\]

It follows by integrating the finite geometric identity for
1/(1-u^2) over 0<=u<=x; the remainder bound is strict on 0<u<x.
No infinite-sum interchange is involved. Recomputing at m=12 for
t=2,3,11/4 certifies log2>6931/10000, log3<10987/10000 and
1<c_J<41/40. Also 3^12=531441>524288=2^19 gives
delta>19/12, while 10987/6931<793/500 gives delta<793/500.
All factors of b are positive and increasing on this interval. Thus

\[
q>361/192>47/25=:q_-,\qquad
q<1886547/1000000<189/100=:q_+,
\]
\[
19/64=:b_-<b<12322427/40000000<31/100=:b_+.         \tag{6}
\]

For the remaining logarithms, the positive exponential series gives
e>sum_(k=0)^5 1/k!=163/60=:e_-.
For k>=5 the successive terms have ratio at most 1/6. Consequently

\[
e<\sum_{k=0}^4 1/k!+\frac{1/5!}{1-1/6}
 =1631/600=:e_+<11/4.
\]

The strict tail bound holds because ratios after the first tail term
eventually are strictly less than 1/6. Exact rational comparisons give
e_+^2<20<e_-^3 and (11/4)^19<N_*<e_-^20. Monotonicity of the
logarithm therefore proves

\[
2<\log20<3,\qquad 19<\log N_*<20.                  \tag{7}
\]

S and U have nonnegative coefficients and are positive for x>1.
Combining (6)–(7), keeping the bU contribution in both directions,
gives the rational enclosures

\[
R(N_*)>R_-:=\frac{399}{5}\,19S(q_-)+60S(q_-)
                  +6b_-U(q_-)+\frac{50322}{517},
\]
\[
R(N_*)<R_+:=\frac{399}{5}\,20S(q_+)+66S(q_+)
                  +6b_+U(q_+)+\frac{50322}{517}.
\]

Here 50322/517=96+1380/1034 is the unchanged length-conversion
constant. Exact finite sums evaluate to

\[
R_-=
\frac{8208849805725950449780513904578248446781}
     {15046680346131324768066406250000}>545558861,
\]
\[
R_+=
\frac{4087164980535842164012945831433931304241435352501}
     {6462500000000000000000000000000000000000}<632443324.
\]

Since N_*=370000000>338460000 and
(8/5)M=361024000<N_*, (2) follows. In particular N_*<R(N_*),
so it satisfies precisely the tested scalar inequality on the required
ray. One certified survivor suffices to refute exclusion of that whole
ray by (1). This does not certify any of the other conditions omitted
by the scalar comparison and is not a witness to the actual hypotheses.

### Evidence, decision and qualifications

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-10-twenty-exact-transfer-comparison.md`.
This is REPRODUCTION: a finite specialization of established inputs,
without an originality claim. The changed occurrence count requires
its own assembly and certified arithmetic; no general source theorem
needs reproof. Local progress is an informative negative result for
this particular comparison, not progress beyond the checked general
cycle literature or a resolution of the main target.

Run `python3 scripts/postspell-word-count/certify_twenty_exact_transfer.py`.
All 29 exact checks pass, with no failures; complete operands, rational
logarithm enclosures, finite sums, exponential guards and RHS bounds are
in `scripts/postspell-word-count/twenty-exact-transfer-certificate.json`.
The generator also independently iterates homogeneous and additive
responses through nineteen edges to check the twenty-occurrence sums.
All load-bearing enclosures and comparisons were inspected in full.
The written proof supplies applicability and strict inequality directions;
finite arithmetic checks alone do not verify a mathematical argument.
The separate critical audit is recorded below.

Stop the unchanged twenty-word scalar comparison. No larger count,
new seed, prefix sharpening, tail cap, mass bound or cycle threshold
was tested. L048's nineteen-word exclusion and the weaker-comparison
stops in L047 and Attempts 021/022 remain valid. Other retained
information could change a later independently covered target; this
stop is not a ban on other methods.

Published qualifications remain: height x_min>301*2^50, distributed
[Ro] computations and Roosendaal communication, continued-fraction
denominators 225644606 and 397573379, and Rhin/Crandall original-proof
qualifications. Their original certificates and proofs, and external
Lean builds, are not independently certified here. The source inputs
are not assertions about arbitrary real cycles. Universal entry,
unrestricted counts/cycles, divergence and descent remain unresolved.

### Separate critical audit — 2026-10-10

The pre-invocation SPECIALIZE assessment is
`drafts/literature/2026-10-10-twenty-exact-transfer-obstruction-audit.md`.
Verdict: **no defect found within the stated actual-word hypotheses and
published qualifications**. This REPRODUCTION audit supplies verification,
not a stronger theorem, repaired error or discovery beyond the inspected
sources. The complete proof and generator, relevant L041 proof and prior
audit, L044 (3)–(5), L046's applicability passage and L048's enclosure
proof were inspected. The precise primary imports above and their ready
coverage are reused; original computation and transcendence certificates
are not independently recertified.

Each outgoing word has 3J_i+H_i odd and J_i+a_i even input times.
The half-open word intervals partition all N occurrences; repeated state
values are not identified. For the least return time p, write N=dp+t
with 0<=t<p. Closure gives T^t(n_0)=n_0, forcing t=0. Consequently
K=dK_0, L=dL_0 and the full reciprocal mass scales by d>=1. Since
n_0>=47 and {1,2} is invariant, the primitive cycle is nontrivial.
Hercher's cited Theorem 16 therefore gives 0<Lambda<S_mass/3 at
represented counts. The primitive application of the cited Lemma 12
gives Lambda>exp(-6.125581)d^(143/10)K^(-133/10), sufficient for
the represented lower bound. The cited Corollary 2 gives K_0>M.
With delta>3/2 this yields exactly N>C. No full minimum count is
identified with twenty, and no source theorem is applied to real heights.

L041's single-word mass bound gives S_mass<(69/11)sum_i 1/n_i.
At the smallest designated junction this implies
n_0<(460/11)exp(6.125581)K^(133/10). The shift from log n_0 to
h_0 costs less than 23/517<1/20, and
6.125581+log(23/11)+1/20<25/4+1+1/20<8. Thus the seed in (3)
has precisely log20. Also Lambda<460/517, so log2>2/3 and
delta<8/5 give N<(8/5)K+1380/1034. Every tail remains in N.
Cyclic relabeling selects only the smallest designated junction and
retains ties and repeated representations.

At each own occurrence put y=T^(4J_i)(n_i). Actuality gives
2^H_i(2^a_i n_(i+1)+1)=3^H_i(y+1), hence v_2(y+1)=H_i.
Writing y+1=2^H_i u with positive odd u and using H_i>=3 yields
v_2(11y+23)=2. The exact B^J identity then gives
v_2(11n_i+23)=4J_i+2. These establish the two own-index logarithmic
bounds quoted above. The numerical estimates log2>2/3, log27<4 and
0<c_J<4/3 give the unchanged prefix bound P_i<(15/4)h_i+3.

The exact shifted endpoint keeps -(12/11)(3/2)^H_i-1 inside the
factor 2^(-a_i) and +23/11 outside. Positivity, a_i>=2 and
G_i s_i>=540/11 imply s_(i+1)<G_i s_i/4+23/11<G_i s_i.
With alpha=log(27/16)>0, multiplying the H_i bound by delta-1>0
gives log G_i<(delta-1)h_i+delta J_i alpha. Substituting the J_i
bound with its positive multiplier gives coefficient
 delta+delta(3delta-4)/4=3delta^2/4
and additive term b. Thus (4) applies independently of the count.
No small-junction parameter is used at another index and no tail cap
or relative-height hypothesis enters.

Nineteen forward edges cover h_0,...,h_19. The initial induction case
is equality; later cases are strict and can safely be weakened to <=.
In the additive double sum, q^k occurs exactly 19-k times for
0<=k<=18. Hence (q-1)U=S-20 and both responses are fully included.
Summing P_i gives K<(15/4)(S h_0+bU)+60. Multiplication by 8/5
gives the height factor 6 and constant 96, and substitution of the
seed gives 6*(133/10)=399/5. This verifies every term of (1).
The closing edge is omitted only from this necessary upper estimate;
closure remains indispensable in the cycle source bridge.

For the enclosure method, integrate the finite identity
1/(1-u^2)=sum_(k=0)^(m-1)u^(2k)+u^(2m)/(1-u^2).
The substitution x=(t-1)/(t+1) identifies the integral with log t/2.
The remainder is positive and strictly less than
2x^(2m+1)/((2m+1)(1-x^2)), since 1-u^2>1-x^2 for 0<u<x.
All three full m=12 rational enclosures were recomputed independently.
The power comparison 3^12>2^19 gives delta>19/12; the logarithm
enclosures give delta<793/500 and 1<c_J<41/40. Since delta and
3delta-4 are positive and increasing here, both bounds for b have
the stated directions. They yield exactly (6), including q_->1.

For e, the partial sum through k=5 is a strict lower bound. Starting
with 1/5!, the subsequent ratios are at most 1/6 and become strictly
smaller, so the geometric tail gives the strict upper bound 1631/600.
The four full rational power comparisons in (7) were checked. They
establish the strict bounds on log20 and log N_* without floating-point
rounding. Positive coefficients of S and U preserve both enclosure
directions. Independent Horner evaluation of S and of the multiplicity
polynomial U, followed by assembly from the seed and prefix count,
reproduces both displayed rational RHS values and the constant 50322/517.
The lower value exceeds N_* by more than 175558861. In particular an
upper enclosure alone was not used to claim survival.

Run `python3 scripts/postspell-word-count/audit_twenty_exact_transfer.py`.
All 85 exact checks pass, with no failures, in
`scripts/postspell-word-count/twenty-exact-transfer-audit-certificate.json`.
The regenerated 29-check certificate is byte-identical on the audit rerun.
The independent script recomputes logarithm enclosures by a power
recurrence, evaluates S and U by their coefficient polynomials, checks
assembly constants and RHS values, and cross-multiplies every original
comparison without trusting its stored pass flag. The complete original
comparisons, logarithm values, sums and RHS endpoints were inspected.
The written argument supplies strictness and applicability; arithmetic
checks alone do not validate imported source computations.

One surviving scalar length disproves only exclusion of the full count
ray by (1). Neither N_*>C nor N_*>(8/5)M assigns K_0,K,L,d,
parameters, simultaneous heights, parities or closure. Attempt 023's
stop therefore stands, and L048 and the weaker-comparison stops remain
unaffected. No argument or direct mathematical input changed; PROOF.md
and DAG.md stay unchanged. This canonical verdict supersedes their
historical pending-audit wording for L049. Universal entry, unrestricted
counts/cycles, divergence and eventual descent remain unresolved, with
all source and Mathlib qualifications retained.

## Mathlib

Full matching coverage of this twenty-word scalar obstruction and its
imported cycle inputs is **not checked**. Supporting logarithms, finite
geometric sums and exponential-series inequalities have no checked
matching declarations here. Unknown availability is not absence; no
formal verification is claimed.
