# Endpoint aggregate phase-budget test — 2026-09-24

Gap and target: the arithmetic sign at the prescribed endpoint heights
a_n and the low Laguerre indices required by the global witness argument
remain unresolved. Test the concrete budget from the checkpoint:

L=sqrt(r), y=exp(6L), σ=1+1/(2L), q_p=p^(−σ),
B_r(θ)=Σ_(p≤y)(1−cos θ_p)(log p)q_p(1+q_p)/(1−q_p)^3≤L/32,
ω(p)=−exp(iθ_p).

The proposed intermediate result is uniform negativity of both endpoint
arithmetic sums, with margin at least ζ(2)²/(8r), under this aggregate
condition and every larger-prime completion. A larger sufficient region
could support a different recurrence test after the full-box obstruction.
Its size, visits on the coupled interval and transfer to a_n would remain
unproved. Continue if the normalized Gaussian comparison error is below
1/8 and the full contour tails vanish uniformly; otherwise identify the
failed bound or a completion that prevents the claimed sign.

Redundancy review: read GOAL.md, PROGRESS.md, the whole PROOF.md and
the global DAG before loading detailed proofs; inspected existing changes.
L339 treats a coordinatewise tolerance of 1/10. L340 obstructs its
absolute Fourier return certificate and L341 disproves uniform full-box
return at length exp(2r); neither treats the proposed larger budget set.
The search found no existing aggregate stability theorem. L337's positive
completion fixing only primes through r remains relevant and is not
replaced by an assumption that small-prime agreement suffices. This step
changes the sufficient phase region, not the stopped box-return estimate.
The superseded September 21 admission condition is not applied; its
mathematical evidence and all unfinished work are preserved.

Unfinished reasoning saved before writing the proof: for every real θ,
|1−exp(imθ)|≤m|1−exp(iθ)|, so
1−cos(mθ)≤m²(1−cos θ). The paired Euler logarithm then has
|(log H_r)'(σ+iv)|≤2B_r(θ)≤L/16. After normalization at the
positive real value h_r=H_r(σ), the near-contour variation is exactly
the one bounded in L339. Its old r^(1/200) global bound used small
individual angles and cannot simply be reused. A separate unrestricted
factor bound gives |H_r(σ+iv)|≤ζ(σ)^4≤(1+2L)^4, while h_r≥1;
this polynomial cost should be absorbed by L338's exponential far-tail
decay. Check every phase-uniform limit, the strict Gaussian margin,
the omitted-index transfer and genuine enlargement beyond the box.
Zero consecutive unresolved exploration turns precede this test.

Result: [L342](../lemmas/L342-endpoint-aggregate-phase-budget.md) proves
the proposed aggregate criterion. The chord inequality bounds the paired
logarithmic derivative by 2B_r≤L/16. At the real normalization point
1≤h_r≤(1+2sqrt(r))^4, and this unrestricted polynomial bound suffices
on the far contour. The resulting normalized limiting error is at most
Aβ, where A=ζ(2)² and β=412505/3437154<1/8. Thus both real sums
are eventually at most −A h_r/(8r)≤−A/(8r), uniformly over every
budget-admissible assignment and larger-prime completion. This meets
the tested threshold and dominates E_r=(1+r)²exp(−r/256).

The criterion strictly enlarges the old box: its budget there is at
most (3/100+o(1))L<L/32. It also permits arbitrary phases on every
prime p≤r if r<p≤exp(6sqrt(r)) retains the exact Liouville phase.
Their total budget is at most 24(log r)(1+log r)=o(sqrt(r)),
so this is a growing set of unrestricted coordinates. In particular
the new condition is not another statement of the stopped box target.

Assessment: ADVANCE; zero consecutive unresolved exploration turns.
This supplies a relevant conditional arithmetic input and justifies
assessing the larger region, rather than repeating either stopped
full-box return argument. Its Haar measure and recurrence on the
exp(2r) scale remain unknown here; inclusion of a small box does not
transfer that box's covering deficit to a superset. No visit at a_n,
Laguerre sign, zero-exclusion extension or RH candidate is obtained.
The main global mixed-positivity and low-index gaps remain unresolved.
The reason for the following direction is to test whether the enlarged
region is still too small for uniform return before investing in a
return certificate. The sole concrete current action is in PROGRESS.md.

Verification: reviewed the arbitrary-angle chord inequality, the factor
of two in the derivative, analytic logarithm branches, positive real
normalization, global polynomial bound, common Gaussian domination,
phase-uniform supremum and tail estimates, strict margin and genuine
set enlargement. The existing command
`python3 scripts/laguerre/check_endpoint_phase_neighborhood.py` passes
60 exact paired-log coefficient identities and ten rational checks.
These supplement the proof, without certifying an asymptotic or a return
time numerically. No new computational experiment or test script is
needed. The four mathematical inputs in the new DAG row are used in the
proof; the older positive completion and geometric failure are contrasts.
Full Mathlib coverage is not checked; inherited supporting names, direct
links and source qualifications are preserved. The overview records the
larger conditional region; all pre-existing changes remain in place.
