# Permuted last-pair feasibility — step 223 working record

Approved target: Test whether the endpoint/domain/J subsystem admits any cyclic ordering of L068's intact triples for an integer 2<=t<=9250245.

Reuse the saved SPECIALIZE assessment
`drafts/literature/2026-10-14-last-pair-permuted-j-feasibility.md`.
The main gap is universal eventual descent. A uniform rejection here
could later exclude a larger restricted actual-word family; a rational
survivor would stop this necessary-subsystem exclusion. Neither outcome
settles other allocations, entry, unrestricted cycles or divergence.

Initial reasoning saved before calculation: use n=s-23/11>=47 and
the exact own-row recurrence n_next=c(n+eta), 0<eta<23/11. Multiplying
all 25 endpoints gives Lambda=sum log(1+eta/n). If m=min n, then
Lambda<575/(11m), so m<575/(11 lambda_minus). This bounds the minimum
without assuming that either changed-tail row grows. Rotate the full
tuple to this minimum, retaining all endpoints and outgoing rows.
Seek log(s_min)<27. For a first displaced row k, j>k; the preceding
literal rows have indices <k<=23, hence tails 2. Their shifted offsets
are negative, so the existing prefix estimate remains valid with 27
in place of 24. Test all 300 pairs 0<=k<j<=24 using a guard RHS
constant 29 rather than 26. If every margin is positive, the minimum
rotation is literal and L068 rejects t>=2 at row 24. This is only a
conditional plan until the finite margins and exact minimum bound pass.

Stop this sufficient comparison if any required margin or minimum bound
fails. No finite unsuccessful permutation search would establish exclusion.
Inputs: L051 endpoints/J guards, L055 complete table and audited log/count
enclosures, L063 first-displacement method, L068 exact literal rejection.
L067's fixed-tail root bound is not an input for the varying tails.
Attempts 027–031 remain untouched; their prime diagnostics are not resumed.

## Completed bounded attempt

The planned comparison succeeds. Canonical proof:
[L069](../lemmas/L069-permuted-last-pair-j-infeasibility.md).
The exact minimum upper bound is 7187500000030429/14553<500000000000;
the 41-term exp(27) lower sum exceeds that integer. Every one of 300
first-displacement margins is positive, with minimum
629441541677/50000000000>12.58. All five rational and eight table checks
pass in `scripts/postspell-word-count/permuted-last-pair-certificate.json`.
The complete 24 weakest-case operands/margins and all supporting checks
were inspected, not just previews. Strictly increasing J covers every
remaining pair, and the written rotation argument covers every order.

The minimum rotation must be literal; audited L068 then rejects the
whole specified integer interval. No search for individual survivors or
unapproved arithmetic mechanism was needed. This is local ADVANCE through
REPRODUCTION/specialization, without an originality claim beyond checked
sources. The proof still needs separate critical audit. It supplies neither
an assembled actual-word exclusion nor universal descent. No failed probe
was suppressed; all required comparisons passed on the first execution.

Documentation validation: the first scoped check flagged the overview's
100-line cap after adding the result. The new overview/trap prose was
joined to the existing paragraphs without removing mathematical content;
the final `python3 ../scripts/docs/check_structure.py --problem collatz`
passes (74 nodes, 154 unique edges). The canonical 24-row margin table
matches the complete certificate exactly. The next action matches its
REVIEW_REQUIRED assessment TARGET. Direct mathematical inputs were checked
against the four L069 DAG entries; no downstream actual-word input is used.
