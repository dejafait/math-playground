# L075 — Variable-table sufficient cyclic-order criterion

## Hypotheses

Let r>=3 and B>=0 be integers. Fix integer indexed pairs with
2<=J_0<...<J_(r-1) and H_i>=3. Define the table/budget totals

\[
K=\sum_{i=0}^{r-1}(3J_i+H_i),\qquad
N=\sum_{i=0}^{r-1}(4J_i+H_i)+2r+18B,\qquad
\Lambda=N\log2-K\log3.
\tag{1}
\]

All logarithms are natural. The following are explicit sufficient tests
on the fixed data and rational certificate constants; they do not quantify
over possible junctions, orders or allocations.

Choose rationals lambda,T,ell,u,v satisfying

\[
0<\lambda\le\Lambda,\qquad
U:=\frac{23r}{11\lambda}+\frac{23}{11}\le e^T,
\qquad 0<\ell\le\log2,\quad \log3\le u,\quad
\log(11/4)\le v.
\tag{2}
\]

For each row require the negative tail-2 offset test

\[
d_i:=\frac{81}{44}-\frac3{11}(3/2)^{H_i}<0.
\tag{3}
\]

This is a rational-power test; H_i>=5 suffices. Define the literal
tail-2 prefix totals, including the empty prefix, by

\[
A_k=\sum_{i<k}(3J_i+H_i),\qquad
D_k=\sum_{i<k}(4J_i+H_i+2),\qquad 0\le k\le r-2.
\tag{4}
\]

Require the r-1 rational margins

\[
M_k:=4J_{k+1}\ell-T-v-A_k u+D_k\ell>0
\qquad(0\le k\le r-2).
\tag{5}
\]

Conditions (2) require certified one-variable analytic inequalities;
they are not claims based on floating-point evaluation. Finite outward
logarithm enclosures and a positive exponential-series partial sum can
certify them, as in the benchmark below. Conditions (3)–(5) are then
finite exact rational arithmetic. None asks whether an unknown tuple is
feasible or prescribes its order.

Now let b_i>=0 be any integers with sum b_i=B and put a_i=2+18b_i.
Let pi be any permutation of {0,...,r-1}. Suppose real junctions
s_0,...,s_r satisfy s_r=s_0, s_k>=540/11 and, for every 0<=k<r,

\[
s_{k+1}=2^{-a_{\pi(k)}}(G_{\pi(k)}s_k-Q_{\pi(k)})+23/11,
\quad
G_i=(27/16)^{J_i}(3/2)^{H_i},\quad
Q_i=(12/11)(3/2)^{H_i}+1,
\tag{6}
\]
\[
4J_{\pi(k)}\log2\le\log s_k+\log(11/4).
\tag{7}
\]

Every outgoing row keeps its own pair and allocation under permutation
and rotation. These are only L051's endpoint/domain/non-strict own-input
J conditions, without its H guard, seed, minimum or count-ray conditions.
There is no integer-junction, actual-word, parity, residue, exact-valuation,
primitive-period or realization premise.

## Conclusion

Under tests (2)–(5), every feasible cyclic order is a rotation of
0,...,r-1. More precisely, rotation to any smallest designated junction
makes pi the identity. Any first displaced position k, carrying row j>k,
would fail its own guard with left-minus-right margin strictly greater
than

\[
M_{k,j}:=4J_j\ell-T-v-A_k u+D_k\ell\ge M_k>0.
\tag{8}
\]

The tests have the audited L074 instance as a nonvacuous benchmark, with
exactly its existing constants and minimum margin >12.58, as shown below.
The conclusion is sufficient only: failure of any test proves neither
feasibility nor nonrigidity. Literal-order feasibility, integer exclusion
for other tables, unrestricted cycles and universal eventual descent
remain unresolved. This local specialization is not a complete Collatz
candidate. The separate critical audit below found no defect within these
hypotheses and qualifications.

## Proof

### Standard inputs and purpose of the specialization

The ready SPECIALIZE assessment is
`drafts/literature/2026-10-17-variable-table-cyclic-order-criterion.md`.
The formal affine-word identity is imported from Halbeisen–Hungerbuehler,
*Optimal bounds for the length of rational Collatz cycles*, Acta
Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2, equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
Its finite formal word identity applies to these nonnegative integer row
exponents; (2) gives a positive fixed-point denominator. No integer or
parity realization is imported. The coordinate and product checks below
are the needed variable-table specialization, not a reproof of general
affine coding. The local template is L074, with L051 supplying (6)–(7).
L074 is a method reference, not an imported variable-table premise;
the changed implication is proved below. Neither theorem's additional
fixed-table/count restrictions are assumed here.

The analytic inputs are the positive-real logarithm/product identity,
NIST DLMF [4.5.1](https://dlmf.nist.gov/4.5.E1), its positive-real
logarithm representation [4.2.19](https://dlmf.nist.gov/4.2.E19), and,
for the benchmark certificates, the series in
[4.6.4](https://dlmf.nist.gov/4.6.E4). The prior assessment inspected
their applicable domains. In particular log(1+x)<x for x>0 and
monotonicity apply only to positive arguments here. Scalar affine
ordering theorems are not inputs to simultaneous guard rigidity.

### Every closed allocation has a controlled minimum

Put n_k=s_k-23/11>=47 and

\[
\eta_i=\frac{23}{11}-\frac{12}{11}(16/27)^{J_i}
                    -(16/27)^{J_i}(2/3)^{H_i},\qquad
c_i=2^{-a_i}G_i.
\tag{9}
\]

Both bases in the subtracted powers are in (0,1), and J_i,H_i>0.
The subtracted sum is strictly between zero and 12/11+1=23/11,
so 0<eta_i<23/11. Direct multiplication gives
G_i eta_i=(23/11)G_i-Q_i. Thus every edge in (6), including
closure, is exactly

\[
n_{k+1}=c_{\pi(k)}(n_k+\eta_{\pi(k)}).
\tag{10}
\]

The total allocation gives sum a_i=2r+18B and hence
prod c_i=3^K/2^N=exp(-Lambda), independently of pi and b.
Multiplying all r equations (10) cancels the same positive incoming
and outgoing product, even when junction values repeat. Taking positive
logarithms yields

\[
\Lambda=\sum_{k=0}^{r-1}
 \log(1+\eta_{\pi(k)}/n_k).
\tag{11}
\]

For m=min n_k>=47, each summand is less than eta_(pi(k))/n_k
and this is less than 23/(11m). Consequently

\[
\lambda\le\Lambda<\frac{23r}{11m},\qquad
s_{\min}=m+23/11<U\le e^T,\qquad \log s_{\min}<T.
\tag{12}
\]

No row has been assumed growing or identified in advance with that
minimum. All allocated tails remain in (11), including tails equal to 2.

### Compare arbitrary tails only at actual inputs

At any actual input s>=540/11, let n=s-23/11>=47. Equation (9)
gives G_i s-Q_i=G_i(n+eta_i)>0. Since a_i>=2, replacing its
tail factor at this same input gives

\[
2^{-a_i}(G_i s-Q_i)+23/11
\le\tfrac14(G_i s-Q_i)+23/11
=\tfrac14G_i s+d_i<\tfrac14G_i s.
\tag{13}
\]

The identity for d_i is exactly (3). For H_i>=5 its sign follows
from (3/11)(3/2)^5=729/352>648/352=81/44; the rational-power
condition (3) is what the theorem requires. H_i>=3 by itself is
never substituted for it. No sign is asserted for the actual large-tail
offset. No upper comparison trajectory is required to stay in the
domain; (13) is applied at actual lower-domain junctions only.

### Rotate and reject every possible first displacement

Choose any minimum occurrence q and replace the position-k input by the
old input at (q+k) mod r, carrying its outgoing row and allocation with
it. The old closing edge remains an edge; the new closing edge is the
old edge q-1 to q modulo r. Therefore all endpoints, domain bounds and
own-input guards survive, including both cuts and any repeated values.
Reuse the symbols pi,s for the rotated tuple; now log s_0<T by (12).

If pi is not the identity, its first displaced position k is at most
r-2: agreement through r-2 would force the last row. All indices less
than k have already been used, so j=pi(k)>k. The preceding rows are
exactly 0,...,k-1 in literal order, though their allocated tails may be
arbitrary. Repeated use of (13) at their actual positive inputs gives

\[
\log s_k<T+A_k\log3-D_k\log2
\le T+A_k u-D_k\ell.
\tag{14}
\]

For the empty prefix k=0 the strict inequality comes directly from
(12). For k>0 it follows by induction from log(G_i/4)=
(3J_i+H_i)log3-(4J_i+H_i+2)log2 and positivity. Nonnegative
A_k,D_k justify the last inequality with the displayed directions.
The prefix includes neither the displaced row nor any suffix.

Its displaced row's guard would then have difference

\[
4J_j\log2-(\log s_k+\log(11/4))
>4J_j\ell-T-v-A_k u+D_k\ell=M_{k,j}.
\tag{15}
\]

Since J_j>=J_(k+1) and ell>0, M_(k,j)>=M_k>0 by (5).
This contradicts the non-strict guard (7). Every nonidentity permutation
has such a first displacement, so the minimum rotation is literal.
Undoing the rotation proves the cyclic-order conclusion. The proof
assumes neither an ordering of actual heights nor a preselected minimum
location, and imposes no H/seed or realization condition.

### Nonvacuity: recover precisely the audited L074 benchmark

Take L055's complete 25-row pair table and B=9250245. Its audited
totals give K=397573379, N=630138897. Use

\[
\lambda=10584/10^{14},\quad T=27,\quad
\ell=693147180559/10^{12},\quad
u=1098612288669/10^{12},\quad v=2.
\tag{16}
\]

L055's audited enclosures imply lambda<Lambda, ell<log2 and
log3<u. L069 (6)–(7) gives the complete exact comparisons

\[
U=\frac{7187500000030429}{14553}
 <500000000000
 <\sum_{q=0}^{40}\frac{27^q}{q!}<e^{27}.
\tag{17}
\]

Also log(11/4)<2 since e^2>1+2+2=5>11/4. Every H_i>=40,
so all offset tests (3) hold. The table has strictly increasing J.
The 24 rational tests (5) become exactly the complete weakest-case
integers of L069 (9), divided by S=10^12:

\[
SM_k=4J_{k+1}\,693147180559-29S
       -A_k\,1098612288669+D_k\,693147180559.
\tag{18}
\]

There are no changed operands: D_k uses comparison tails 2 regardless
of allocation. L069's complete table and monotonicity proof certify all
24 entries, and hence all 300 eligible (k,j), with minimum

\[
\min_k M_k=12588830833540/10^{12}
 =629441541677/50000000000>12.58.
\tag{19}
\]

Only L069's exact numerical inequalities are imported, not its narrower
tail assumptions or literal rejection. The final prefix remains
A_23=144318712, D_23=162928789. Thus tests (2)–(5) recover L074
over its entire allocation simplex without new hypotheses. Nonvacuity
is supplied by L055's actual positive rational literal witness, which
satisfies the weaker endpoint/domain/J premises here. This witness
establishes neither integer realization nor feasibility for other tables.

The existing independent benchmark program is
`python3 scripts/postspell-word-count/audit_permuted_last_pair.py`.
It checks the exact logarithm remainders, table/count matching, minimum
bound, all 24 weakest records and all 300 pair operands; its full output
is `scripts/postspell-word-count/permuted-last-pair-audit-certificate.json`.
These finite checks verify the reused benchmark evidence; they do not
verify the new symbolic implication in place of the proof above.

This is local RESEARCH/REPRODUCTION under SPECIALIZE: an explicit
variable-table sufficient test obtained by specializing an audited local
mechanism, not a claim of originality beyond inspected literature.
Attempts 026–031 and both rational witnesses retain their scope. No
other table search, signed-offset extension, literal integer exclusion
or actual-word consequence is included. The separate critical audit below verifies this sufficient implication
and its benchmark without extending its scope.

### Independent critical audit — 2026-10-17, step 281

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-17-variable-table-cyclic-order-critical-audit.md`.
This audit reused the construction assessment's inspected primary theorem
hypotheses and proof cases, and checked Attempts 026–031. No new source,
scalar optimizer, parity converse or stopped prime diagnostic is used.
The verdict is no defect in (1)–(19), including the benchmark. This
validates a local reproduction, not a new mathematical discovery beyond
the sources or an advance on universal eventual descent.

**General implication.** The positive powers in (9) give
0<eta_i<23/11 for every permitted pair, and multiplication verifies
G_i eta_i=(23/11)G_i-Q_i exactly. Thus (10) retains the actual a_i
at every edge. The finite permutation and sum b_i=B give the exponents
K and N in the full product. Since n_k>=47, cancellation of the
incoming and outgoing products is valid, including closure and repeated
junction values; (11) follows with the displayed positive sign of Lambda.
For m=min n_k each term is strictly below 23/(11m). Multiplying
lambda<=Lambda<23r/(11m) by positive m/lambda yields
m<23r/(11lambda). Adding 23/11 and using U<=exp(T) proves the
strict height bound in (12), even if either certified inequality is
an equality. No minimum location or growing-row premise is required.

At each actual input, G_i s-Q_i=G_i(n+eta_i)>0. Hence a_i>=2
allows the first inequality in (13). The tail-2 offset is exactly
23/11-Q_i/4=d_i, and the explicit test d_i<0 supplies strictness.
H_i>=3 alone is insufficient; the proof uses (3). For the benchmark,
H_i>=40 implies H_i>=5 and the written comparison 729/352>648/352.
The actual large-tail offset may be positive and is never discarded.
The positive multiplier G_i/4 propagates bounds only at actual positive
inputs, with no domain assumption on a comparison trajectory.

Rotation to any minimum moves its outgoing indexed row and allocated
tail with it. The old final edge remains one of the rotated edges; the
new final edge is the old q-1 to q edge, with indices modulo r. Thus
all own-input guards and both cuts survive. If the rotated permutation
is not identity, its first displaced position satisfies k<=r-2 and
j=pi(k)>k, since every smaller row was already used. Its prefix consists
exactly of rows i<k, and (13) yields (14) with the tail-2 D_k regardless
of their actual allocations. For k=0 strictness is supplied by (12);
for k=r-2 the prefix ends at row r-3, so no missing final case occurs.
A_k,D_k>=0 give the upper rounding direction in (14). In (15),
J_j>0, ell<=log2 and log(11/4)<=v give a lower guard difference;
strictness remains from (14). Increasing J and ell>0 then give
M_(k,j)>=M_k>0, contradicting precisely the non-strict guard (7).
This covers every permutation, including any rotation from a tied minimum,
without using H/seed, primitive/count-ray or realization assumptions.

**Complete benchmark and existence.** Read L055's full table, factored
root and witness proof and L069's complete numerical comparisons; compare
L074 only as the audited fixed-table method. The table has increasing J,
minimum H=40, sum J=66061058 and sum H=199390205. With B=9250245,
sum a=166504460 gives exactly K=397573379 and N=630138897.
The L055 positive Lambda interval and grid logs therefore apply to every
allocation, not just its witness. The constants (16), the full fraction
U in (17), and the complete positive exponential sum match L069.
All 24 weakest records match (18), including the empty prefix and
A_23=144318712, D_23=162928789. The latter record has scaled operands
85945478764125031844 and 45616708760840061277. The minimum is exactly
12588830833540/10^12>12.58. Monotonicity in J covers every larger j;
the independent program also recomputes all 300 complete pairs.
No restricted-tail assumption or literal rejection from L069 is imported.

Read and reran both existing independent programs:
`python3 scripts/postspell-word-count/audit_permuted_last_pair.py` and
`python3 scripts/postspell-word-count/audit_fixed_count_tail_witness.py`.
They passed 387 and 317 exact checks respectively, with no failures.
Their full evidence remains in
`scripts/postspell-word-count/permuted-last-pair-audit-certificate.json`
and `scripts/postspell-word-count/fixed-count-tail-witness-audit-certificate.json`.
The complete weakest records, Lambda endpoints, exponential total, all
25 witness rows and root-bound fractions were inspected. The programs
recompute complete rational operands, logarithm terms and remainder
bounds rather than trusting flags. For the first program, with
x=(z-1)/(z+1) in (0,1/2], its 160-term lower sum has error bounded
by 2x^321/[321(1-x^2)]; opposite endpoints bound N log2-K log3.
The second checks all rounded terms and an independent 120-term bound.
These are the assessed positive-real series with justified outward
remainders. The first program's L068 boundary check is not used here.

For nonvacuity, L055's exact finite root has a positive denominator,
and its recurrence gives every endpoint and exact closure with the
actual large final tail. Its first 24 multipliers exceed 2, its root
bounds give 18*10^9<n_0<s_0<20*10^9, and the complete own-J margins
are positive (minimum 402427610954/10^12). Its allocation is b_i=0
for i<24 and b_24=9250245, so it satisfies precisely the weaker
L075 endpoint/domain/J premises. No H/seed or primitive hypothesis is
transferred to other tables. Numerical checks verify this benchmark;
the general implication is verified by the preceding symbolic argument.

No premise, conclusion or direct mathematical dependency changed, so
DAG and PROOF remain unchanged. Full matching Mathlib coverage is still
unchecked. Both rational witnesses and recorded failures remain valid.
Failure of a sufficient test still implies neither feasibility nor
nonrigidity; new-table literal allocation and integer analysis, arbitrary
cycles, entry, divergence and universal eventual descent remain unresolved.

## Mathlib

Full matching coverage for this simultaneous cyclic endpoint/own-input
guard criterion is unchecked. Supporting finite-product and positive-real
logarithm results are not a matching theorem. No absence or formalization
claim is inferred from unknown coverage.
