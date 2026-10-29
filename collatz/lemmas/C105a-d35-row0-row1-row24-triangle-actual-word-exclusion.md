# C105a — d35 row0/row1/row24 triangle actual-word exclusion

## Hypotheses

Let T(n)=n/2 for even positive integers and T(n)=(3n+1)/2 for
odd positive integers. Letters O and E specify actual input parities
for T. Use the 25 indexed pairs (J_i,H_i) in the literal order of
L055's table, changing only H_0=40 to 5 and H_24=32670621 to
32670656. No witness, minimum, seed or other assertion of L055
is assumed.

Let B=9250245 and let m,u be integers satisfying m>=1, u>=1
and m+u<=B. Define

\[
b_0=m,\quad b_1=u,\quad b_{24}=B-m-u,\quad
b_2=\cdots=b_{23}=0,\qquad a_i=2+18b_i,
\]
\[
W_i=(OOEO)^{J_i}O^{H_i}E^{a_i},\qquad
D_i=4J_i+H_i+a_i,\qquad q_i=\sum_{j<i}D_j,\qquad N=q_{25}.
\]

Suppose W_0...W_24 is actual at a positive odd integer n_0>1
and T^N(n_0)=n_0. Put n_i=T^{q_i}(n_0), 0<=i<=25.
Require each junction n_i, 0<=i<25, to be positive odd and
congruent to 20 modulo 27, and each final even tail to be exact.
Thus n_25=n_0. Repeated periods and coincident junction values
are allowed. No minimum, seed, first-return, primitive-period or
relative-height premise is imposed. All logarithms are natural.

## Conclusion

No such closed actual concatenation exists for any integer pair
m,u>=1 with m+u<=9250245. The entire closing-tail2 edge m+u=B
and the point m=u=1 are included.

This is local RESEARCH/REPRODUCTION under the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-26-l105-triangle-actual-word-transfer.md`.
It specializes occurrencewise necessities to audited L105; it claims
no progress beyond the sources checked. The separate critical audit
on 2026-10-26 retained this restricted transfer without mathematical
repair; its verification is recorded below. This is not a complete
Collatz candidate.

## Proof

Assume such a concatenation exists and fix its given m,u and original
chronological indexing. The full table has J_i>=8. After exactly the
two H replacements, H_0=5 and H_i>=72 for i>0. Thus J_i>=2 and
H_i>=3 for every row. The parameter triangle makes all b_i
nonnegative integers, so every a_i is an integer at least 2 and
congruent to 2 modulo 18. All local parameter hypotheses of L041
hold with r=25.

Every D_i is positive. The intervals [q_i,q_{i+1}) partition the
actual concatenation, and W_i is actual at n_i with output n_{i+1}.
This includes i=24, whose output n_25=n_0 is odd. Use L041's
proof section "Each occurrence's own prefix and the transfer to the
next" and its corresponding audit only for their finite occurrencewise
necessities. Those necessities apply to each input with its own exact
tail and odd output, without a size ordering or upper-tail assumption.
L041's minimizing relabeling, seed, represented-length conclusion and
global cycle estimates are not used.

Set kappa=23/11 and s_i=n_i+kappa for 0<=i<=25. To check the
lower domain explicitly, write n_i=20+27k with k an integer.
Positivity gives k>=0, and oddness forces k odd, hence k>=1.
Consequently

\[
s_i\ge47+23/11=540/11>0\quad(0\le i<25),\qquad
s_{25}=s_0.
\tag{1}
\]

At each occurrence define y_i=T^{4J_i}(n_i) and
z_i=T^{4J_i+H_i}(n_i). L041's finite identities give

\[
y_i+1=(27/16)^{J_i}s_i-12/11,
\qquad
z_i=(27/16)^{J_i}(3/2)^{H_i}s_i
          -(12/11)(3/2)^{H_i}-1,
\qquad n_{i+1}=z_i/2^{a_i}.
\tag{2}
\]

Put G_i=(27/16)^{J_i}(3/2)^{H_i} and
Q_i=(12/11)(3/2)^{H_i}+1. Adding kappa to the last equality
in (2) yields exactly

\[
s_{i+1}=2^{-a_i}(G_i s_i-Q_i)+\kappa
\quad(0\le i<25).
\tag{3}
\]

Thus both subtractions remain inside the actual row's tail division
and kappa remains outside. Equation (3) holds at every chronological
endpoint, including row24-to-row0. No endpoint is replaced by a
composed upper bound, and no tail is replaced by a total-tail value.

L041 also gives at this same occurrence

\[
4J_i\log2\le\log s_i+\log(11/4),\qquad
2^{H_i}\le y_i+1<(27/16)^{J_i}s_i.
\tag{4}
\]

The arbitrary-tail case in that proof uses
2^{H_i}(2^{a_i}n_{i+1}+1)=3^{H_i}(y_i+1), with a_i>=2,
H_i>=3 and odd output. These hypotheses hold for every assigned
tail here; it is not an E^2-only assertion. All terms in the second
chain of (4) are positive. Taking logarithms, using their strict
monotonicity and product rule, gives

\[
H_i\log2<\log s_i+J_i\log(27/16).
\tag{5}
\]

The strict upper comparison comes from the positive subtraction
12/11 in (2). Therefore (5) remains strict even when
2^{H_i}=y_i+1. The first guard in (4) remains non-strict.
Both guards use row i's own input s_i and its own J_i,H_i.

Apply audited L105 to the single tuple (s_0,...,s_25). Its indexed
table has exactly our J_i,H_i, including H_0=5,H_24=32670656.
Its parameters are these same integers m,u>=1 with m+u<=B;
the allocations b_0=m,b_1=u,b_24=B-m-u and all other b_i=0,
and hence every a_i=2+18b_i, agree without alteration. Equation
(1) supplies its lower domain and closure; (3) supplies every one
of its 25 endpoints. The first inequality in (4) and (5) supply
its non-strict J and strict H guards, respectively, at the required
inputs. These are all L105's hypotheses. Its exclusion of such
a real tuple is a contradiction.

This matching is uniform over the entire integer triangle. At
m=u=1, the changed tails are a_0=a_1=20 and a_24=166504376.
On the entire edge m+u=B, a_24=2 and the last actual occurrence
still ends at n_0 with equation (3) and both own-input guards.
This includes both edge vertices (m,u)=(1,B-1),(B-1,1).
All tails on rows2,...,23 are 2 throughout, and their endpoint
equations and guards have also been retained. There is no upper-tail
premise in L041's finite necessities or L105. Repeated periods and
coincident junction values leave the intervals [q_i,q_{i+1}) as
distinct chronological occurrences; they do not remove any equation
or guard. No rotation, minimization, seed or primitive-period reduction
is needed.

### Sources, overlap and qualifications

The direct mathematical inputs are L041's finite occurrencewise
necessities, L055's complete literal table only and audited L105.
L104's denominator enclosure and the cut2 estimate remain internal
inputs of L105, with their existing qualifications. This transfer
does not need a new affine bound, logarithmic enclosure or certificate
replay. It matches hypotheses rather than reproving general finite
coding or fixed-point results.

The precise upstream finite-affine reference inspected in the reused
assessment is Halbeisen–Hungerbuehler, *Optimal bounds for the length
of rational Collatz cycles*, Acta Arithmetica 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp.228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Only finite actual-word identities are used through L041; actuality
is an explicit hypothesis. No integrality-to-actuality converse or
general coding reproof is used, and no fresh source retrieval is
claimed. The displayed substitution and logarithm step justify the
particular domain, endpoint and guard matching needed here.

The prior scoped duplicate comparison found C103b in b_0=0 and
C104b in b_1=0; neither supplies this positive-row0/positive-row1
triangle transfer. They are comparisons, not mathematical inputs.
Attempt032's failed fixed sufficient support mechanism supplies no
premise and is not reopened. Both d0 witnesses and unfinished work
remain preserved. This proves no support/order exhaustion, language
entry, arbitrary-cycle exclusion, divergence result or universal
descent. Endpoint-only feasibility is never treated as integer
realization.

### Separate critical audit — 2026-10-26

This RESEARCH/REPRODUCTION proof audit uses the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-26-c105a-triangle-actual-word-critical-audit.md`.
It found no mismatch and retains the statement and proof without
mathematical repair. The following checks establish the transfer as a
verified local input; they are not a new general theorem or formal
verification. Audited L105 is imported, not numerically recertified.

**Parameters and literal data.** All25 rows of L055's table were checked:
their J values are at least8; H1=72 is the smallest H away from row0
after the replacements H0=5,H24=32670656. Thus every J>=2,H>=3
required by L041 holds. The same two replacements, the same indices
and B=9250245 occur in L105. For every integer m,u>=1,m+u<=B,
all budgets are nonnegative integers, with exactly b0=m,b1=u,
b24=B-m-u and rows2 through23 zero. Consequently every a=2+18b
is at least2 and is 2 modulo18. Neither L055's original H values
at the changed rows nor its witness, minimum or seed is imported.

**One tuple and every endpoint.** Each D_i>0, so the time intervals
[q_i,q_(i+1)) partition the given actual word into all25 occurrences.
The hypotheses provide an odd output at every endpoint, including
n25=n0. The residue calculation n_i=20+27k>0 forces k>=0,
and odd n_i forces odd k, hence k>=1. Thus for the single original
tuple s_i=n_i+23/11 one has s_i>=540/11 and s25=s0.
L041's finite affine identities apply to each of these occurrences.
Its displayed z_i is G_i*s_i-(12/11)*(3/2)^H_i-1. Actual E^a_i
then divides this entire expression by 2^a_i; adding 23/11 produces
exactly L105(1), with Q_i=(12/11)*(3/2)^H_i+1. This checks both
subtractions, the outside shift and all25 indexed equations. The last
equation has input s24 and output s0; closure is not inferred from an
approximation or a different tuple.

**Own-input guards and arbitrary tails.** The imported finite argument
was checked directly in L041's occurrencewise proof and audit, with
L031's arbitrary-tail qualification. At an arbitrary occurrence write
y=T^(4J)(n_i). Its identity

\[
2^H(2^a n_{i+1}+1)=3^H(y+1)
\]

has odd 2^a*n_(i+1)+1 because a>=2. Hence v_2(y+1)=H and
y+1=2^H*v for a positive odd integer v. Since H>=3,
11y+23=4(11*2^(H-2)*v+3) has valuation exactly2. The finite
identity 16^J(11y+23)=27^J(11n_i+23) therefore gives
v_2(11n_i+23)=4J+2. Positivity implies
2^(4J+2)<=11n_i+23=11s_i. Taking logarithms yields precisely
4J*log2<=log s_i+log(11/4), without changing its non-strict sign.
Also 2^H<=y+1=(27/16)^J*s_i-12/11<(27/16)^J*s_i.
All terms are positive; strict monotonicity of log gives
H*log2<log s_i+J*log(27/16). The positive subtraction 12/11
preserves strictness even if the first inequality is equality.
These are L105(2) at the same original input s_i. No 3-adic guard,
two-word closure converse, E^2-only transport, minimum relabeling,
global cycle estimate or upper bound on a enters this check. This
is verification of the cited finite argument, not a new coding reproof.

**Full domain and contradiction.** The preceding checks use only the
stated inequalities m,u>=1,m+u<=B; they do not infer uniformity from
samples. At m=u=1 the tails are (a0,a1,a24)=(20,20,166504376).
On the whole edge m+u=B the closing tail is exactly2; at its vertices
(1,B-1),(B-1,1) the other two tails are respectively
(20,166504394),(166504394,20). All remain within L041's arbitrary-tail
scope. Rows2 through23 always have tail2. Coincident junction values
or repeated periods never identify distinct time intervals, and all
equations and guards continue to be imposed. No primitive-period or
first-return hypothesis is introduced.

This exhausts L105's premises: literal data and budget domain, lower
domains, closure, all endpoint equations and both own-input guard
families. In particular the same s2 must satisfy L105's audited
s2<10^21 and its necessary J2=28 lower bound
s2>=(4/11)*2^112>10^21. The contradiction excludes exactly the
claimed actual-word triangle. L105's denominator and analytic estimate,
with L104 internal, remain established inputs; no certificate replay
or fresh primary-source retrieval is claimed in this transfer audit.

The direct inputs remain L041, L055 and L105, so no DAG edge changes.
The existing precise finite-affine citation and its source qualifications
above are retained. The scoped duplicate/failure check used histories498,
500 and501, the triangle working records and Attempt032. C103b and
C104b cover different supports and are not premises here. Both d0
witnesses and unfinished work remain intact. The audit supplies no
support/order exhaustion, entry argument, unrestricted cycle exclusion,
divergence result or universal descent. It never treats endpoint
feasibility as actual integer realization.

## Mathlib

Full matching coverage for this restricted actual-word exclusion
has not been checked. Exact declarations for its supporting finite
affine identities, valuations and logarithmic rules have not been
checked in this step. No matching theorem, absence claim, checked
Lean build or external formal verification is asserted.
