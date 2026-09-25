# Radius-dependent certificate multiplicity — 2026-09-25

Read the shared instructions, local target and checkpoint, complete overview,
and DAG before selecting this step. Existing changes are preserved. The
[official statement](https://proximityprize.org/) and
[ePrint metadata](https://eprint.iacr.org/2026/680) were reread; the page remains
preliminary and the paper record still lists the July 6 revision. The unread
paper-to-model correspondence is not assumed. This step uses only the pinned
affine-line support event.

Gap: L003's all-radius union bound discards the size of the original bad
support, so it cannot distinguish smaller radii at the given field size.
Intermediate target: for m >= k+1 coordinates on which b is not a degree-<k
RS restriction, prove that at least binomial(m-1,k) of their (k+1)-subsets
also fail. Then divide the total small-certificate budget by this multiplicity.
Downstream use: a uniform radius-dependent sufficient field-size bound for
the prescribed error, while sharpness, ABF26 correspondence, and endpoint
qualifications remain separate unresolved steps.

Discriminating test: first try induction on the support size, separating the
case where deleting one coordinate leaves a code restriction from the case
where every deletion still fails. Check the bound on finite examples using
direct polynomial membership, and verify that certificate families for
different bad challenges are disjoint. Continue this mechanism if it gives a
strict radius-dependent improvement over L003; abandon the proposed factor
if a counterexample or a missing disjointness implication appears. Compare
the resulting sufficient q with 2^128 times the integer challenge bound,
without treating sufficient safety as a sharp radius.

Redundancy and failure check: L003 proves existence of one small certificate,
not their multiplicity. The previous endpoint and single-field disproof
routes do not establish this count and are not reopened. No prior failed
multiplicity test is recorded. Consecutive exploration turns start at zero.

## Saved unfinished reasoning

For a noncode restriction on S, |S|=m, suppose b agrees with a degree-<k
polynomial p on S minus {i}. Then it disagrees at i. Every (k+1)-subset
containing i fails by uniqueness on its other k coordinates, and every such
subset avoiding i succeeds. This gives exactly binomial(m-1,k) failures.

If every single-coordinate deletion fails and m>k+1, induction supplies at
least binomial(m-2,k) failures on each of the m deletions. Every failing
(k+1)-subset is counted m-k-1 times. Thus their number is at least
m*binomial(m-2,k)/(m-k-1), which exceeds binomial(m-1,k). The base m=k+1
has the whole support as its one failure. This looks like a proof of the
proposed multiplicity, with equality attained by one changed coordinate.

On an original bad support for gamma, b fails and a+gamma*b succeeds, so
each counted subset T has h_T(b) nonzero and forces the same unique value
gamma=-h_T(a)/h_T(b). Different challenges cannot use the same T. With
m=max(k+1,ceil(n*(1-delta))), the tentative bound is
E_C(delta) <= min(1, floor(binomial(n,k+1)/binomial(m-1,k))/q).
The proof and endpoint qualifications still need review; no completed result
is claimed in this saved reasoning.

## Completed assessment

The induction and disjoint-certificate argument succeed. The full proof is
stored in [L004](../lemmas/L004-radius-dependent-certificate-multiplicity.md).
The local factor is sharp exactly when the direction agrees with a codeword
except at one coordinate of the support. The uniform bound is
min(1, K_m/q), where K_m=floor(binomial(n,k+1)/binomial(m-1,k)); it need not
be sharp. The actual error budget is met whenever q >= K_m*2^128.

This improves a concrete parameter regime where L003's all-radius condition
fails: n=256, k=128, q=257^32 has a smooth domain and is certified safe for
all real delta < 90/256, including grid radius 89/256. The next cell has
m=166 and fails this sufficient test; no conclusion of unsafety follows.
The proof retains the original support size through multiplicity without
claiming that each smaller certificate meets the radius threshold.

The independent polynomial-enumeration check passed 111,013 noncode supports
across nine small parameter sets and 31,994 input-pair classes across seven
of them. It checked the factor, its one-coordinate equality case, certificate
disjointness, all integer support cutoffs, and exact field-size comparisons.
It also exposes slack: at q=5, n=5, k=2, cutoff m=4, the computed maximum
bad-challenge count is 2 while K_m=3. This is finite evidence for investigating
the geometry of large-support constraints; no general sharp formula follows
from that enumeration. The current concrete action is only in PROGRESS.md.

Outcome: ADVANCE, a relevant radius-dependent mathematical input for the
pinned model, with exploration turns reset to zero. No complete challenge
candidate is claimed. The sharp error at the given code, source bridge, and
endpoint and field-size qualifications remain unresolved.
