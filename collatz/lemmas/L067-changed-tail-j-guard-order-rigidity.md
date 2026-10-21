# L067 — Changed-tail J-guard order rigidity

## Hypotheses

Use the complete indexed J_i,H_i table of L055, with the tails specified
by L065: a_23=20, a_24=166504394, and a_i=2 otherwise. Let pi permute
{0,...,23}, with pi(24)=24. At chronological position k use the intact
outgoing triple (J_pi(k),H_pi(k),a_pi(k)). Require real junctions
s_k>=540/11, s_25=s_0, every exact endpoint L051 (4), and the own-input
non-strict guards

\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4),\qquad 0\le k\le24.
\tag{1}
\]

All logarithms are natural. No H guard, seed, integer, parity, residue,
exact valuation or primitive-orbit realization is assumed. The fixed
totals are K=397573379 and N=630138897. Tails stay attached to their
original J,H rows; no further redistribution is permitted.

## Conclusion

This necessary subsystem has a solution if and only if pi is the identity.
For every allowed order the endpoints alone have a unique real solution,
which is positive and obeys, with n_k=s_k-23/11,

\[
18\cdot10^9<n_0<s_0<20\cdot10^9,
\qquad n_0<n_1<\cdots<n_{24}.
\tag{2}
\]

Thus s_0 is its unique smallest designated junction and every s_k lies
in the required domain. Every nonidentity order strictly violates (1)
at its first displaced row, with left-minus-right margin exceeding
779441541677/50000000000>15.58.

This is a local RESEARCH/REPRODUCTION specialization under the prior
SPECIALIZE assessment `drafts/literature/2026-10-13-changed-tail-order-rigidity.md`.
It extends a fixed-allocation result locally; no originality beyond the
inspected sources is claimed. The separate critical audit below found no defect. L066
is a possible downstream input, not a premise or an integer exclusion
assembled here. Other allocations, unrestricted cycles, entry, divergence
and universal eventual descent remain unresolved.

## Proof

### Formal affine root and changed-tail uniformity

For each position define

\[
c_k=3^{3J_{\pi(k)}+H_{\pi(k)}}/
       2^{4J_{\pi(k)}+H_{\pi(k)}+a_{\pi(k)}},
\]
\[
\eta_k=23/11-(12/11)(16/27)^{J_{\pi(k)}}
                  -(16/27)^{J_{\pi(k)}}(2/3)^{H_{\pi(k)}},
\quad C_k=\prod_{t<k}c_t,\quad C_0=1.
\]

The standard affine composition and fixed-point input is
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational
Collatz cycles*, Acta Arith. 78 (1997), 227–239,
DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment inspected the theorem and essential induction cases.
The formal word is nonempty, with N letters and K odd letters; only
affine composition is imported, without integer realization. The changed
finite estimates below justify the specialization, rather than reprove
general coding or invoke a scalar extremality theorem for input guards.

Indeed, for every actual tail,

\[
c_k\eta_k=\frac{23}{11}c_k-
2^{-a_{\pi(k)}}\left(\frac{12}{11}(3/2)^{H_{\pi(k)}}+1\right).
\]

Subtracting 23/11 from L051 (4) therefore gives exactly
n_(k+1)=c_k(n_k+eta_k). Dividing by C_(k+1)=c_k C_k and summing yields

\[
B=\sum_{k=0}^{24}\eta_k/C_k,\qquad
n_k=C_k\left(n_0+\sum_{t<k}\eta_t/C_t\right).
\tag{3}
\]

The changed tails still sum to 166504460. L055's unchanged J,H totals
give sum(3J+H)=K and sum(4J+H+a)=N. Consequently C_25=3^K/2^N.
The audited count-dependent L055 enclosure remains applicable:

\[
\lambda_-:=10584/10^{14}<\Lambda=N\log2-K\log3
 <10585/10^{14}=: \lambda_+<1.
\tag{4}
\]

In particular 0<C_25=exp(-Lambda)<1. The closing equation is uniquely
solved by

\[
n_0=B/(\exp\Lambda-1)=B/(2^N/3^K-1).
\tag{5}
\]

These are finite exact factored rational expressions. Every eta_k is
strictly between 0 and 23/11, since its two positive subtractions have
sum strictly below 12/11+1. Thus B,n_0 and all prefixes in (3) are
positive. This proves uniqueness before any guard is imposed, and retains
the changed closing tail in C_25.

Here is the new multiplier check needed for all orders. Every eligible
tail-2 row has J>=8,H>=40, so its multiplier is at least
b:=3^64/2^74>10^8 by L055's exact baseline comparison. For the tail-20
row 23, its actual parameters have J_23>=8 and H_23>=80. Monotonicity
in J,H, since 27/16>1 and 3/2>1, gives

\[
c(23)\ge3^{104}/2^{132}
=b\,3^{40}/2^{58}>b>10^8,
\tag{6}
\]

where the strict integer comparison is
3^40=12157665459056928801>288230376151711744=2^58.
Thus every first-24 multiplier exceeds 10^8, in particular exceeds 2,
regardless of the position of row 23. No growth assertion is made about
the final row 24. Every eligible first row also has eta>=eta(8,40)>2,
because both subtractions decrease with J and the second decreases with H.
The exact baseline is

\[
\eta(8,40)=
7122556955297586891012225981605/
3433683820292512484657849089281>2.
\]

For 1<=k<=24, C_k>10^8*2^(k-1), uniformly over every suffix.
Only first-24 multipliers appear in these denominators; eta_24 is
included in B but c_24 appears only in closure. Hence the finite
geometric majorant gives

\[
2<B<B_+:=(23/11)(1+2/10^8)=1150000023/550000000.
\tag{7}
\]

For 0<x<1, the positive exponential series gives
x<exp(x)-1<x/(1-x), with the strict upper bound from 1/k!<=1
and strict inequality for k=2. Combining (4), (5), (7) gives

\[
n_0>2(1-\lambda_+)/\lambda_+
=39999999995766/2117>18\cdot10^9,
\]
\[
s_0<B_+/\lambda_-+23/11
=95833335260143/4851<20\cdot10^9.
\tag{8}
\]

The positive recurrence with c_k>2 for k<24 proves (2), including
the unique designated minimum and s_k>18*10^9>540/11. The audited
L062 comparison sum_(t=0)^40 24^t/t!>20*10^9 proves log s_0<24.
Also exp(2)>1+2+2=5>11/4 proves log(11/4)<2. No permuted domain
or minimum is assumed, and no old order-dependent root value is used.

### Unchanged prefixes and complete first-displacement coverage

Let pi be nonidentity and k its first displaced position. Then
0<=k<=22: if positions 0,...,22 were fixed, row 23 would be forced.
Every row below k has already been used, so j=pi(k)>k. The preceding
literal prefix contains only rows below k, hence no tail-20 row 23.
Its outgoing edges therefore have exactly the tail-2 shifted formula

\[
s_{t+1}=c_t s_t+81/44-(3/11)(3/2)^{H_t}<c_t s_t,
\quad t<k.
\tag{9}
\]

The additive term is negative: H_t>=40>=5 and
(3/11)(3/2)^5=729/352>648/352=81/44.
Both endpoints are positive, so logarithms preserve (9). With the
nonnegative literal prefix totals

\[
A_k=\sum_{i<k}(3J_i+H_i),\qquad
D_k=\sum_{i<k}(4J_i+H_i+2),
\]

induction from log s_0<24 gives

\[
\log s_k<24+A_k\log3-D_k\log2.
\tag{10}
\]

The initial bound is uniform in the permuted suffix. Row j's own tail
does not affect the guard at its input s_k, and row 23's tail has not
entered the unchanged prefix. This is why changing the tails preserves
the first-displacement operands, although it did require a new root bound.

Set S=10^12, ell=693147180559 and u=1098612288669.
L055 (6) supplies strict log2>ell/S and log3<u/S. For each eligible
0<=k<j<=23 put

\[
m_{k,j}=4J_j\ell-26S-A_k u+D_k\ell.
\tag{11}
\]

These are exactly the finite integer expressions in L063 (7), with
unchanged J,H and unchanged literal prefix tails. Its audited 23-entry
weakest-margin table therefore applies as a finite arithmetic input,
not as an application of L063's differently scoped all-order theorem.
It gives every m_(k,k+1)>0. Since the J sequence is strictly increasing,
m_(k,j)>=m_(k,k+1) for every j>k. The least among all 276 pairs is
m_(0,1)=15588830833540, giving m_(0,1)/S=779441541677/50000000000.
The new certificate also recomputes every pair and every weakest operand.

Using (10), the outward log bounds and log(11/4)<2 gives

\[
\log s_k+\log(11/4)
<26+(A_k u-D_k\ell)/S
<4J_j\ell/S<4J_j\log2.
\tag{12}
\]

The middle inequality is precisely m_(k,j)>0. Thus the true
left-minus-right margin of (1) is strictly greater than m_(k,j)/S,
with the stated global bound. The input s_k stays paired with outgoing
row j. These 276 first-displacement pairs cover every nonidentity one
of the 24! orders; no suffix enumeration or probabilistic premise is used.

For the identity order, audited L064 at j=23 supplies exact closure,
domain and every one of the 25 strict J guards for exactly these tails,
including row 24's guard. That theorem's literal scope matches here;
L065's additional H/seed result is not needed. This proves the equivalence.
Cyclic relabeling, if performed, must rotate each outgoing row together
with its input. The unique solution then rotates too; putting row 24
last restores this normalization and the same own-input verdict.

### Certificate and qualifications

Run `python3 scripts/postspell-word-count/certify_changed_tail_order_rigidity.py`.
The complete certificate is
`scripts/postspell-word-count/changed-tail-order-rigidity-certificate.json`.
It stores all 25 actual attached triples, totals, prefix exponents,
276 full guard operands and margins, 23 weakest cases, exact root-bound
fractions, 41 exponential terms, 15 rational comparisons and 8 integer
checks. There are zero failures. All supporting rational operands and
the complete weakest-case operands/margins were inspected; monotonicity
in J supplies the written full-pair proof. A preview or success flag
is not the verification. Imported log/Lambda and literal-existence
results retain their canonical qualifications; no floating-point
calculation, huge-power expansion or approximate closure is required.

This step uses established affine/logarithm machinery and L063's exact
finite comparisons with their changed-tail applicability proved above.
It does not reopen prime diagnostics in Attempts 027–030 or the single
real-order failure in Attempt 031. Both positive rational witnesses
remain valid. The result concerns one fixed necessary subsystem; it
does not imply integer/parity/residue/exact-valuation or primitive
realization and applies no integer-cycle theorem to arbitrary reals.
No Collatz candidate is claimed. The separate critical audit is recorded below.

### Independent critical audit — 2026-10-14

The separate approved RESEARCH/REPRODUCTION audit found no defect in
the full statement, including the uniform bounds, domain, minimum and
cyclic relabeling. It reused the unchanged SPECIALIZE assessment
`drafts/literature/2026-10-13-changed-tail-order-rigidity-critical-audit.md`.
This verifies the local input; it claims neither mathematics beyond the
inspected sources nor a downstream integer exclusion.

The coordinate identity was checked directly against L051 (4).
Writing G=(27/16)^J(3/2)^H, one has
G(16/27)^J=(3/2)^H and G(16/27)^J(2/3)^H=1.
Thus c eta=(23/11)c-2^(-a)((12/11)(3/2)^H+1)
for either ordinary or changed tails. Subtracting 23/11 from the
endpoint gives n_(k+1)=c_k(n_k+eta_k), with eta independent of a.
Division by C_(k+1) and finite telescoping proves (3). Recomputed
totals give sum a=166504460, K=397573379 and N=630138897,
including a_24=166504394. Therefore C_25=exp(-Lambda) is strictly
between zero and one. The cyclic equation has exactly one real root;
positivity of every eta makes that root and all its prefixes positive.
Neither closure nor uniqueness is inferred from numerical iteration.

For every eligible tail-2 row, J>=8,H>=40 imply c>=3^64/2^74.
The exceptional tail-20 row has J>=8,H>=80, so its c is at least
3^104/2^132; its ratio to the former baseline is 3^40/2^58>1.
These exact bounds cover row 23 even when it is the first row.
The monotonicity of eta in J,H gives eta>=eta(8,40)>2 for every
possible first row as well. Hence c_k>10^8 for all k<24, which
implies the weaker C_k>10^8*2^(k-1) used in (7).
All denominators C_1,...,C_24 in B contain only these growing
multipliers. The final eta is included in B; the final multiplier is
excluded from these denominators but retained in C_25 and closure.
This proves the geometric bound uniformly over every suffix.

For 0<x<1, the strict series inequalities
x<exp(x)-1<x/(1-x) have the required direction. Substituting the
upper Lambda endpoint for the lower root bound and the lower endpoint
for the upper root bound yields precisely the two fractions in (8).
They respectively exceed 18 billion and lie below 20 billion after the
specified shift. The positive recurrence with c_k>2 proves the strict
growth of n_0,...,n_24. Thus the minimum is unique among designated
inputs and every logarithm is in its required domain before guards are
used. The independently recomputed 41-term exp(24) sum agrees with
L062 and exceeds 20 billion. No growth of the closing edge or minimum
over intermediate parity phases is assumed.

For a nonidentity order, its first displacement satisfies k<=22 and
j=pi(k)>k: all smaller row labels have already been consumed, and a
permutation cannot have exactly its final position displaced. Its entire
literal prefix has indices less than k and therefore omits row 23.
Every such prefix edge has tail 2 and negative shifted additive term,
since (3/11)(3/2)^5=729/352>81/44. Positivity permits taking
logarithms. This proves (10) using a uniform initial bound, although
the actual initial root depends on the suffix. Row j's tail affects
its output, not the guard at its input. Nonnegative A_k,D_k justify
the outward substitutions in (11)–(12). Increasing J_j makes j=k+1
weakest at each k. All 276 pair operands and all 23 weakest margins
were independently recomputed and matched to the original certificate
and L063's complete written table. Their minimum is exactly
779441541677/50000000000>15.58. The true left-minus-right margin
is strictly larger, so the rejection contradicts the non-strict guard.
The first-displacement partition, not enumeration of 24! orders,
supplies full coverage. L063's old-tail theorem is not applied.

L064's audited j=23 existence has exactly the tails and endpoint/J
conditions used here. Its unique cyclic root therefore coincides with
(5). As an additional arithmetic check, all 25 literal lower J margins
were recomputed with a_23=20; every value matches L064's displayed
list, including the closing row's numerator 8286876116986. The least
is 402427610954 at i=19. No H or seed result is needed. A cyclic
rotation must rotate endpoints and outgoing rows together. The rotated
tuple then satisfies the rotated equations, whose unchanged product
multiplier differs from one, so uniqueness identifies it. Putting the
unique row 24 last restores precisely the normalization of this theorem
and preserves each own-input guard and the designated minimum.

The independent verifier is
`python3 scripts/postspell-word-count/audit_changed_tail_order_rigidity.py`.
It imports or executes no generator. It parses the canonical L055 table,
independently sums each prefix, compares complete saved records rather
than pass flags, and checks all 15 supporting rational comparisons,
8 integer assertions, 41 factorial-based exponential terms, root
fractions, every pair and every literal J margin. The unrounded
128-term logarithm enclosure is

\[
P(x)=2\sum_{m=0}^{127}\frac{x^{2m+1}}{2m+1},\qquad
R(x)=\frac{2x^{257}}{257(1-x^2)},\qquad
P(x)<\log\frac{1+x}{1-x}<P(x)+R(x).
\]

The assessed integrated geometric remainder justifies these strict
bounds for 0<x<=1/2. The verifier uses x=1/3,1/2,7/15 for
log2, log3 and log(11/4), respectively, and binary reduction by 2^34
for log(18 billion). Opposite endpoints give an independent interval
for N log2-K log3 strictly inside (lambda_-,lambda_+), retaining
the cancellation. They also certify every grid bound needed for the
literal guard calculation. Terms, remainders and endpoints are all saved.

The full certificate is
`scripts/postspell-word-count/changed-tail-order-rigidity-audit-certificate.json`:
381 exact checks, zero failures, complete operands and the original
certificate's SHA-256. Full supporting comparisons, Lambda endpoints,
root fractions, the minimum rejection and the final literal margin were
inspected. The written argument above supplies the all-order quantifiers;
the certificate supplements it and makes no integer-cycle assertion.

The direct mathematical inputs remain L051, L055, L062, L063's finite
table and L064. L065 names the explicitly repeated tail allocation;
its H/seed theorem is not used. L066 remains downstream only. DAG.md
and the main argument do not change; the overview's historical pending
label is superseded by this canonical audit. Both rational witnesses,
Attempts 027–031, source qualifications and unchecked full Mathlib
coverage remain intact. Every universal Collatz gap remains unresolved.

## Mathlib

Full matching coverage and Lean builds were not checked. Supporting
real-logarithm/exponential declarations do not constitute a formalization
of this changed-tail all-order statement. Unknown availability is not
evidence of absence. The exact rational certificate supplements the
informal proof and is not an integer-cycle or Lean certificate.
