# Endpoint discrete-mean derivative test — 2026-09-24

Gap and target: the endpoint arithmetic margin at the actual pairs
r=2n, a_n=sqrt(4π²exp(8n)−25), remains unproved. Test
D_N=N^(−1)Σ_(N≤n<2N)|R_(2n)(a_n)|²=o(1) using L332's
frequency expansion and fixed-order derivative estimates in n.
Such a bound would give positive endpoint margins for a density-one
subset of these pairs. Exceptional pairs, the lower Laguerre indices
and heights above forty would remain unresolved. Continue this
certificate only if its summed error tends to zero; a nonvanishing
lower bound on the certificate, as distinct from D_N, stops it.

Redundancy review: read GOAL.md, PROGRESS.md, the whole PROOF.md
and the global DAG and inspected the existing changes. L333 handles
continuous height averages, L334 tests their uniform pointwise
conversion, and L343 concerns arbitrary translated returns to a
sufficient phase region. None estimates this discrete coupled mean.
L305 and L329 are precedents for derivative-budget failures in an
arithmetic summation index; the variable here is the Laguerre index
n, with a moving coefficient array. The September 21 admission
condition is superseded by GOAL.md; its evidence is retained.

Unfinished reasoning saved before completing the estimates: use
L333's exactly grouped expansion |R_r(a)|²=Σ g_r(k,l)exp(ia log(k/l)).
Its zero-frequency sum is M_r=C/r²+O(r^(−3)); averaging r=2n
should give C/(8N²)+O(N^(−3)). Its proved inverse-frequency
absolute sum is O((r+1)^17), so frequencies smaller than exp(−2N)
have total coefficient mass O(N^17exp(−2N)). For every other
frequency ω, the dth derivative of ω a(x)/(2π) is asymptotic to
4^d ω exp(4x), uniformly for x≥N at fixed d. The first term in
each standard fixed-order derivative bound is then larger than the
number of summands. To check that this failure is material, use
L334's R_r(0)→−1: the signed nonconstant coefficient sum tends to
one, and removal of the tiny-frequency part should leave absolute
mass at least 1−O(1/N). Check the exact product grouping, the moving
weights in Abel summation, the derivative hypotheses, and the
diagonal/tiny-frequency budgets before recording an obstruction.
No estimate for the actual D_N or its signed remainder is claimed
at this saved checkpoint. Zero consecutive unresolved exploration
turns precede the test.

Result: [L344](../lemmas/L344-endpoint-discrete-mean-derivative-obstruction.md)
retains every equal-frequency collision and proves the exact discrete
expansion with diagonal C/(8N²)+O(N^(−3)). Frequencies of magnitude
below exp(−2N) have absolute mass O(N^17exp(−2N)). The remaining
fully grouped coefficient mass is at least
1−O(1/N)−O(N^17exp(−2N)). Every fixed-order classical or
Heath-Brown derivative certificate on those frequencies is trivial.
The proof retains the moving weights: their absolute Abel budget is
at least their absolute mass, even after arbitrary interval partitions.
The certificate's liminf is therefore at least one, exceeding both
the o(1) target and the fixed threshold 1/4. No lower bound on the
actual mean is proved.

WHY IT FAILS: the [canonical proof](../lemmas/L344-endpoint-discrete-mean-derivative-obstruction.md)
shows that all coefficient mass needed to reconstruct the order-one
value |R_r(0)|² lies, up to a negligible error and the small diagonal,
at frequencies whose derivatives in the sampling index grow
exponentially. Derivative magnitude alone then yields only the
number-of-terms bound. Absolute Abel summation cannot recover the
lost signed information, even with all ratio collisions already
grouped. This stops the specified derivative certificate, not the
discrete mean target, actual phase cancellation or endpoint positivity.

Assessment: NEGATIVE; zero consecutive unresolved exploration turns.
The actual endpoint margin, global mixed positivity and low-index
signs remain unproved, with all sign/exclusion ranges unchanged and
no RH candidate. The next direction retains the sampling phase in a
stationary dual sum, whose longer integer range might expose different
cancellation. The necessary first comparison is a weighted o(N)
partial-sum estimate before reassembling the coefficients. L319's
involution for a different ratio-block phase is relevant caution:
merely transforming twice without a signing estimate would add no
evidence. No transform or bound is assumed here. The sole concrete
current action is in PROGRESS.md.

Verification: checked absolute convergence after full reduction,
the exact constant-frequency term, the dyadic factor 1/8, the
inverse-frequency tail, the actual zero-height value used only for
coefficient mass, the differentiated binomial tail, bounded-A
hypotheses on subintervals, every term of both derivative estimates,
and the finite Abel identity with signed moving weights. The primary
Heath-Brown source was checked for equation (1) and Theorem 1;
Mathlib coverage is not checked, with inherited supporting theorem
names and direct links preserved. These are analytic checks; no
numerical phase sample or asymptotic computation is used. The new
DAG row contains only L333 and L334, whose proved data are the
mathematical inputs. All pre-existing changes are preserved.
