# L062 — Fixed joint witness fails its minimum real guard

## Hypotheses

Use L055's 25 intact indexed triples, with tails 2 at indices 0–23
and tail 166504412 at index 24. Fix precisely L060's chronology

```text
8 1 2 3 4 5 6 12 0 9 10 11 7 13 14 15 16 17 18 19 20 21 22 23 24
```

Write J_j,H_j,a_j for the triple at chronological position j, so
J_0=1230,H_0=5849,a_0=2. The counts remain K=397573379,
L=232565518,N=630138897. Test exactly L051 (1)–(4) at r=25,
as restated in L055, allowing only cyclic relabeling with each triple
attached to its input junction. In particular a required own-index guard
is 4J_j log2 <= log(s_j)+log(11/4). All logarithms are natural.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-12-joint-witness-permuted-real-guards.md`.
No real feasibility, integrality, actual parity/exact-tail or primitive
integer-orbit realization is assumed.

## Conclusion

The unique affine cyclic root for this fixed order fails the required
J guard at its unique smallest designated junction. More precisely,
at chronological position 0 (original index 8),

\[
18000000000<n_0<s_0<20000000000,\qquad n_j=s_j-23/11,
\]
\[
4J_0\log2>3280,
\qquad \log s_0+\log(11/4)<26.
\tag{1}
\]

Thus no cyclic relabeling makes this order satisfy the complete retained
25-word real system. This removes the specific order surviving the two
prime diagnostics from that system; it does not exclude every order or
allocation. L060/L061's modular cancellations and L055's literal-order
real witness remain valid. The restricted actual-cycle exclusion remains
through 24. Universal entry, unrestricted cycles, divergence and eventual
descent remain unresolved. The separate critical audit below found no
defect within this fixed-order scope.

This is local REPRODUCTION of the assessed affine/logarithm machinery,
not a claim of progress beyond the general results inspected or of a
new general rational-cycle theorem.

## Proof

### Exact root and coordinate specialization

Import the formal affine construction from Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta Arith.
78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The prior assessment inspected its statement and relevant proof cases.
The word is nonempty, with length N and K odd letters. Only its formal
affine composition and fixed point are used, without a parity-realization
claim or a reproof of the general coding result.

L055's separately audited bound on the count-dependent linear form
survives this intact permutation:

\[
\lambda_-:=10584/10^{14}<\Lambda=N\log2-K\log3
 <10585/10^{14}=: \lambda_+<1.
\tag{2}
\]

For the present chronology define

\[
c_j=3^{3J_j+H_j}/2^{4J_j+H_j+a_j},\qquad
\eta_j=23/11-(12/11)(16/27)^{J_j}
                   -(16/27)^{J_j}(2/3)^{H_j},
\]
\[
C_j=\prod_{t<j}c_t,\quad C_0=1,\quad
B=\sum_{j=0}^{24}\eta_j/C_j,\quad
n_0=\frac{B}{2^N/3^K-1},\quad
n_j=C_j\left(n_0+\sum_{t<j}\eta_t/C_t\right),\quad s_j=n_j+23/11.
\tag{3}
\]

These are finite exact rational expressions; large powers are factored,
not truncated. Since J_j,H_j>0, 0<eta_j<23/11. Equation (2) makes
the root denominator positive. The prefix formula gives
n_{j+1}=c_j(n_j+eta_j). Substituting s_j=n_j+23/11 yields exactly
L051 (4), including both affine corrections. The intact counts give
C_25=3^K/2^N=exp(-Lambda), and hence
n_25=C_25(n_0+B)=n_0. The large final tail is included here.
Since C_25 is strictly below 1, this composition has exactly one fixed
point. Thus (3) is the only tuple satisfying all these endpoints and
closure in this chronology, regardless of the guard tests.

### Order-dependent root bounds and unique minimum

For j<24 the actual tail is 2. Consequently

\[
c_j\ge(27/16)^2(3/2)^3/4=19683/8192>2.
\]

The positive recurrence therefore gives n_0<n_1<...<n_24.
In particular position 0 is the unique smallest designated junction;
this makes no assertion about every intermediate parity phase.

The new first triple has J_0=1230>=8 and H_0=5849>=40. Both
27/16 and 3/2 exceed 1, so its c_0 dominates the smaller baseline
(J,H,a)=(8,40,2). Both subtracted terms defining eta decrease when
J or H increases. Exact baseline comparisons therefore give

\[
c_0\ge3^{64}/2^{74}>10^8,\qquad
\eta_0\ge
\frac{7122556955297586891012225981605}
     {3433683820292512484657849089281}>2.
\]

This is a new applicability argument for the permuted first row, rather
than an assumption that literal-order bounds carry over. For 1<=j<=24,
C_j>10^8 2^{j-1}. Summing the finite positive series and comparing
with its infinite geometric majorant proves

\[
2<B<\frac{23}{11}\left(1+\frac2{10^8}\right)
=\frac{1150000023}{550000000}=:B_+.
\tag{4}
\]

For 0<x<1 the exponential series gives x<exp(x)-1<x/(1-x),
as already justified and audited in L055. With (2)–(4) this gives

\[
n_0>\frac{2(1-\lambda_+)}{\lambda_+}
=\frac{39999999995766}{2117}>18000000000,
\]
\[
s_0<\frac{B_+}{\lambda_-}+\frac{23}{11}
=\frac{95833335260143}{4851}<20000000000.
\tag{5}
\]

Thus all junctions exceed 540/11, although the J guard will fail.

### Certified violated guard and cyclic relabeling

Positive exponential-series terms suffice for the needed coarse bounds:

\[
\exp(24)>\sum_{k=0}^{40}\frac{24^k}{k!}
=\frac{202750314819830504045671593478515759301}
       {7661655986496068058455078125}>20000000000,
\]
\[
\exp(2)>1+2+2^2/2!=5>11/4.
\]

Hence (5) implies log s_0<24 and log(11/4)<2. For log2, use the
positive-real odd-power expansion already assessed in L055 and
[NIST DLMF 4.6.4](https://dlmf.nist.gov/4.6.E4), with x=(2-1)/(2+1)=1/3.
All omitted terms are positive, so

\[
\log2>2(1/3+1/81)=56/81>2/3.
\]

Since J_0=1230, these inequalities prove (1): the left side of its
required non-strict J guard exceeds 4*1230*(2/3)=3280, while its
right side is below 24+2=26. There is strict separation exceeding
3254, not a rounding uncertainty or a failed sufficient test for a
potentially true guard. One false necessary guard is enough to reject
the complete system; no claim about the remaining guards is needed.

Any cyclic rotation of (3) satisfies the correspondingly rotated
endpoint equations. Their product multiplier remains exp(-Lambda)<1,
so each rotated endpoint system also has a unique cyclic solution.
It must be that rotated tuple. Its smallest designated junction is
still the same point, still paired with the intact row 8. Relabeling
that point as s_0 thus retains the failed guard. No admissible cyclic
relabeling repairs this order, and no new order is tested.

### Evidence and qualifications

Run `python3 scripts/postspell-word-count/test_joint_witness_real_guards.py`.
The complete certificate is
`scripts/postspell-word-count/joint-witness-real-guard-certificate.json`.
It contains all 25 intact chronological rows and prefix exponents, the
exact factored definitions, all 41 exponential summands, full comparison
operands and margins, and the explicit failed necessary guard. All 14
rational supporting checks and 12 integer/count checks pass. The full
rows, comparison operands/margins, integer checks and root-bound fractions
were inspected; pass flags alone are not the argument. Equation (2) is
an imported audited mathematical input, not a fresh cancellation check.
Symbolic closure and positivity are proved above, not by a numerical
orbit tolerance or expansion of the enormous rational root.

The inherited published computational, continued-fraction and
Rhin/Crandall qualifications for the motivating actual-cycle bounds
remain as recorded in L051/L055; this step neither reverifies them nor
applies integer-cycle theorems to arbitrary reals. No integrality,
actual parity/exact-tail or primitive realization is established.
The modular results are retained as diagnostics with a different scope.

### Independent critical audit — 2026-10-12

The separate approved audit compared the whole statement with L051
(1)–(4), L055's literal allocation and audited Lambda interval, and
L060's exact chronology. No defect was found. This verifies the existing
one-order exclusion, without extending it to other orders or adding a
new theorem beyond the assessed affine/logarithm specialization.

The coordinate identity was checked algebraically, before using bounds:

\[
c_j\eta_j=\frac{23}{11}c_j-
 2^{-a_j}\left(\frac{12}{11}(3/2)^{H_j}+1\right).
\]

Hence n_{j+1}=c_j(n_j+eta_j), after adding 23/11, is exactly L051 (4).
If T_j=sum_{t<j}eta_t/C_t, then
C_{j+1}=c_j C_j and T_{j+1}-T_j=eta_j/C_j verify every prefix in
(3). The recomputed totals give C_25=exp(-Lambda), including the full
tail 166504412. Positivity of eta_j, B and exp(Lambda)-1 proves
positivity of the unique root and all its prefixes. The closing equation
is equivalent to n_0=B/(exp(Lambda)-1); it is not an approximate closure
test. The affine slope is strictly between zero and one, so there is
exactly one real fixed point, even before positivity restrictions.

For C_j with 1<=j<=24 only multipliers c_0,...,c_{j-1} occur, and
all their tails are actually 2. The first triple dominates (8,40,2);
both of eta's subtracted terms decrease as J or H increases (the first
is constant in H). Thus the exact baseline bounds in the proof apply
to this order. The final multiplier c_24 is never treated as a growing
tail-2 multiplier. From c_0>10^8 and c_j>2 for 1<=j<24,
C_j>10^8*2^(j-1), while 0<eta_j<23/11 for every j, including 24.
This gives precisely 2<B<B_+. Strict growth n_0<...<n_24 then
identifies the unique minimum among the 25 designated inputs; n_25 is
the repeated closing input, not a second designated occurrence.

For 0<x<1, the positive exponential series satisfies
x<exp(x)-1<sum_{k>=1}x^k=x/(1-x). The strict upper bound follows
because 1/k!<1 for k>=2. Substitution of the outward Lambda interval
therefore gives (5) in the stated directions, including the +23/11
shift only in s_0. The independently recomputed 41-term exponential
sum exceeds 20 billion, so log s_0<24. Similarly exp(2)>5>11/4,
and the first two positive terms for log2 give log2>56/81>2/3.
These prove the strict inequalities LHS>3280 and RHS<26 for the
same own-index guard. Its required sign is non-strict <=; the strict
separation rules it out. No seed or remaining guard needs to be true
for this contradiction to a necessary subsystem condition.

For any cyclic rotation, rotating this tuple supplies a solution of
the rotated endpoints. Their affine product slope is the same
exp(-Lambda)<1, so their unique solution must be that rotated tuple.
The smallest junction and its outgoing intact row 8 remain paired.
This proves cyclic invariance of the failure, without asserting that
arbitrary permutations have the same B, root or guard values.

The independent verifier is
`python3 scripts/postspell-word-count/audit_joint_witness_real_guards.py`.
It does not import or execute the original generator. It reads L055's
literal table and the written L060/L062 orders, recomputes every row
and prefix exponent, all 12 integer checks, and every operand, strict
margin and flag of all 14 original rational comparisons. It recomputes
all 41 exponential summands by recurrence, rather than factorial
evaluation, and matches the complete sum and the written root fractions.
The original certificate is preserved and its SHA-256 is recorded.

As a separate check on the reused count-dependent input it evaluates
log2 and log3 directly, with x=1/3 and x=1/2 respectively, using 96
unrounded rational terms. For either x, the exact lower sum is
2 sum_{j=0}^{95} x^(2j+1)/(2j+1), and the integral remainder is

\[
2\int_0^x\frac{u^{192}}{1-u^2}\,du
\le \frac{2x^{193}}{193(1-x^2)}.
\]

This is the assessed positive-real logarithm expansion with its
geometric remainder; no numerical logarithm or new source theorem is
used. Opposite endpoints enclose N log2-K log3. The resulting complete
rational interval lies strictly inside (10584/10^14,10585/10^14),
independently confirming the imported interval after the count check.

The full separate evidence is
`scripts/postspell-word-count/joint-witness-real-guard-audit-certificate.json`:
216 exact audit comparisons, zero failures, with complete series terms,
remainder bounds, Lambda endpoints, rows, prefixes and comparison operands.
The complete relevant original fields and the independently generated
Lambda interval, root fractions and all original comparison operands
were inspected; the conclusion does not rely solely on success flags.
Symbolic positivity, closure, minimum and rotation uniqueness are proved
above, rather than inferred from a finite floating-point orbit.

No direct mathematical input changed: L051 supplies the system, L055
the allocation and count-dependent Lambda input, and L060 the order.
L061 remains motivation only. The inherited published qualifications,
unchecked full Mathlib coverage and all realization/universal gaps
remain unchanged. In particular this audit neither invokes integer-cycle
theorems on arbitrary real junctions nor creates a Collatz candidate.

## Mathlib

Full matching coverage and external Lean builds were not checked.
Unknown coverage is not evidence of absence. The rational certificate
supports this written finite specialization; it is not a Lean theorem
or an integer Collatz-cycle certificate.
