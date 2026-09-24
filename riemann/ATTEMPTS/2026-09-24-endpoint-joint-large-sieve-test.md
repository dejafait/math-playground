# Endpoint joint large-sieve test — 2026-09-24

Gap and target: test D_N=o(1) on L344's actual coupled pairs using
a joint sampling operator for L332's reciprocal-series coefficients.
Such a bound could give positive endpoint margins for a density-one
subset of these pairs; exceptional pairs, the lower Laguerre indices,
and global mixed positivity would still require separate arguments.
Continue if the joint bound and the moving-weight and truncation
costs tend to zero. Stop the specified certificate if even its optimal
sampling constant has a lower budget incompatible with that target.

Redundancy review: read GOAL.md, PROGRESS.md, the whole PROOF.md and
the global DAG before the detailed proofs, and inspected the existing
tracked and untracked work. L333 controls continuous averages;
L344 and L345 stop separate-frequency derivative certificates in
the sample and stationary-dual variables. The repository search
found no joint large-sieve test for these reciprocal coefficients.
The present test uses the exact joint operator, rather than another
derivative estimate. The September 21 admission rule is superseded
by GOAL.md, while its mathematical evidence is retained. Existing
changes and identifiers are preserved.

Unfinished reasoning saved before completing the proof: truncate
the reciprocal indices m,n at Q and group all equal ratios. The
recorded divisor majorant gives a uniform absolute tail
O(N^4 Q^(-1/(8N))) for 2N<=r<4N, but also a lower bound on that
same budget of order r(Q+1)^(-1/r). Thus a short cutoff does not
certify a small remainder. For a long cutoff the reduced ratios
p/Q with p near Q/2 form a cluster of at least order Q exp(-8N)
distinct frequencies within the reciprocal of the actual sample
span. Modulating constant coefficients at the first sample makes
this entire cluster coherent at every sampled height. The optimal
unweighted squared sampling norm should therefore be at least
order |I| Q exp(-8N) on every subinterval I, despite the large
sample gaps. L332's nonzero constant coefficient should give a
uniform order-1/N lower bound for the truncated coefficient norm.
Exact vector Abel summation should preserve that lower budget.
The quantifiers, diagonal tail, common-frequency support and
partition comparison still need checking. These are certificate
claims, not lower bounds on D_N. No RH candidate; zero consecutive
unresolved exploration turns preceded this test.

Completed assessment — 2026-09-24: NEGATIVE.
[L346](../lemmas/L346-endpoint-joint-large-sieve-cutoff-obstruction.md)
proves the exact cutoff tradeoff, including the vector Abel bound
and arbitrary interval partitions with independent cutoffs. The
recorded positive divisor-tail budget is at least cN when
Q<exp(16N). For Q>=exp(16N), a cluster near −log 2 forces the
optimal squared joint sampling norm to be at least
c|I|Q exp(−8N). The fully grouped nonzero coefficient satisfies
b_r(2,1)=((log 2)/2−5(log 2)^2/48)/r+O(r^(-2)), and truncating
it changes it by O(Q^(-3/4)). Thus the moving-vector certificate
is at least c min(N^2,exp(8N)/N^2), tending to infinity instead
of the required o(1). A legitimate cutoff (N+1)^(64N) makes the
tail O(N^(-4)) and leaves the actual coefficient norm O(1/N);
the operator constant, rather than that norm or convergence,
then obstructs the test. The completed proof uses a nonzero
coefficient, improving on the saved diagonal-only observation.

WHY IT FAILS: the [canonical proof](../lemmas/L346-endpoint-joint-large-sieve-cutoff-obstruction.md)
shows that the unweighted operator must control arbitrary vectors
on many very close rational frequencies whose actual coefficients
are small. The necessary operator norm therefore loses information
that the arithmetic coefficient vector contains. The actual sample
spacings and all retained ratio collisions are respected; the
cluster lies away from zero and the constant frequency is treated
exactly. The short-cutoff obstruction concerns the stated absolute
majorant, not the true signed tail. Stop this combination of full
support, unweighted norm, divisor-tail bound and absolute vector
Abel summation. This does not stop coefficient-weighted sampling,
adapted support or a better signed-tail estimate, and supplies no
lower bound on D_N or actual endpoint sign.

The coefficient-weighted alternative has a specific unresolved
target. For nonzero reduced frequencies put
w_N(ν)=max_(N<=n<2N)|b_(2n)(ν)|, omit zero weights, and define
x_n(ν)=b_(2n)(ν)/sqrt(w_N(ν)),
G_N(n,m)=Σ_ν w_N(ν)exp(i(a_n−a_m)ω_ν),
V_N=||x_(2N−1)||_2+Σ_(n=N)^(2N−2)||x_n−x_(n+1)||_2.
These sums are well defined by L332's absolute convergence and
the finite number of n values. The target ||G_N||op V_N²=o(N)
would make the corresponding exact vector-Abel bound small; the
constant-frequency contribution is already O(1/N) in normalized
sample norm. No estimate meeting this target has been obtained
or tested here. It is materially different because the frequency
weights enter the Gram matrix itself, and no long rectangular
cutoff is needed merely to define it. Exceptional pairs and the
global low-index signs would remain even if this target succeeds.

The main gap and all established sign/exclusion ranges are
unchanged. STATUS remains IN_PROGRESS; no RH candidate and zero
consecutive unresolved exploration turns. Verification reviews
the exact tail support, frequency-cluster construction, grouped
nonzero coefficient, uniform diagonal-free norm comparison and
the full partitioned moving-vector budget. Full Mathlib coverage
is not checked; L346 retains the previously recorded supporting
names and direct links. Prior unfinished work is preserved.
