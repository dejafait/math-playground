# Endpoint square-root prime-cutoff test — 2026-09-24

The gap is the endpoint arithmetic sign at the coupled heights r=2n,
a_n=sqrt(4π²exp(4r)−25), within the unresolved initial logarithmic
Laguerre range. The proposed intermediate target is a controlled limit
of r S_r[ω_(r,b)] for fixed b>0, with ω_(r,b)(p)=−1 through
y=exp(b sqrt(r)) and +1 above y. A negative constant for a fixed b
would justify testing a smaller set of prime constraints than L336's
logarithmic-product cutoff. A positive limit for every b would stop
this transition mechanism. The negative margin must exceed
E_r=(1+r)²exp(−r/256); even a successful phase test would leave both
return on the coupled height scale and transfer to a_n unproved.

Redundancy review: read GOAL.md, PROGRESS.md, the entire PROOF.md
overview and global DAG, and inspected the existing tracked and
untracked changes. L335 gives the full Liouville negative asymptotic;
L336 gives an excessive return certificate after a sqrt(r log r)
cutoff; L337 gives a positive completion at y=r. None treats fixed
log(y)/sqrt(r). L304's failed high-height freezing does not preclude
retaining this explicit finite product on its natural Mellin scale.
The historical September 21 admission rule is superseded by GOAL.md;
its evidence and all unfinished work remain intact. Zero consecutive
unresolved exploration turns precede this test.

Unfinished reasoning saved before the limit and bounds are proved:
put L=sqrt(r), u=α+it with fixed α>0, and use the admissible Mellin
line z=1/2+u/L. Its normalized kernel should tend to
sqrt(2/π)exp(2u²) dt. Relative to the Liouville series
F_λ(s)=ζ(2s)/ζ(s), the +1 completion has a tail Euler product whose
squared logarithm should tend to 4 J_b(u), where
J_b(u)=∫_b^∞ exp(−u x) dx/x. Since L F_λ(1+u/L)→ζ(2)u,
the proposed limit is ζ(2)² sqrt(2/π)∫ exp(2u²)u² exp(4J_b(u))dt.
Mertens' third theorem may suffice for the required prime-tail limit,
without a prime-number-theorem error estimate. The comparison with
the full Liouville limit −ζ(2)²/4 should be bounded by
ζ(2)² exp(2α²)(α²+1/4)[exp(4J_b(α))−1]. An absolute logarithmic
Euler-product bound may extend this comparison uniformly to every
unit-phase completion above y. Uniform contour tails, the moving
prime cutoff, all interchanges, an explicit b, and the interior sum
remain to be checked. No limit or sign is claimed at this saved
checkpoint.

Result: [L338](../lemmas/L338-endpoint-square-root-prime-cutoff.md)
proves the proposed scaling limit, with an absolutely convergent
Gaussian-contour formula for C_b. The shifted line also gives the
stronger uniform comparison over every unit-phase completion above y:
limsup sup |r S_r[ω]+ζ(2)²/4| is at most
ζ(2)² exp(2α²)(α²+1/4)[exp(4J_b(α))−1], and likewise for T_r.
At α=1/2, b=6 this is strictly less than ζ(2)²/14. Both sums are
therefore at most −ζ(2)²/(8r), uniformly over those completions,
for all sufficiently large r. No numerical starting r is claimed.

The prime-tail limit uses only the checked standard Mertens main
term, Stieltjes integration with cutoff atoms retained, and an
absolutely summable higher-prime-power error. A local Liouville zero
at s=1 supplies the factor u²; uniform tail-product bounds and
Gaussian decay justify the limits and the supremum over completions.
The interior cutoff costs o(1/r). The signed Gaussian second moment,
not a positive measure, supplies the negative sign.

Assessment: ADVANCE; zero consecutive unresolved exploration turns.
The sufficient exact cutoff is reduced from log y=8 sqrt(r log r)
to log y=6 sqrt(r), and the margin exceeds E_r. This achieves the
intermediate target and a stronger robustness statement about
unfixed primes. It does not give a neighborhood for the fixed prime
phases or any return time, place a negative value at a_n, or change
a Laguerre sign or zero-exclusion range. There is no RH candidate.
Continue by quantifying perturbations of the fixed phases through
the paired Euler product: this tests whether the exact assignment
has a useful neighborhood before any different recurrence argument.
The stopped product-bump certificate is not reopened. The sole
current action is in PROGRESS.md.

Verification: reviewed the absolute Euler products and logarithms,
Mertens-to-prime-tail passage, moving-line normalization, compact
limits and uniform complementary tails, analytic versus modulus
squares, completion-independent bound and discrete interior error.
The exact checker `python3 scripts/laguerre/check_endpoint_sqrt_prime_cutoff.py`
passes 112 paired Euler-log coefficient identities and bounds and
five rational margin comparisons. These supplement the informal
proof; they do not numerically certify an asymptotic or return.
Only scalar inversion, the discrete cutoff and Liouville inputs
are new direct DAG edges. Full Mathlib coverage is not checked;
the supporting name and direct link are preserved. The Mertens
reference supports its standard input only, not the full new result.
All pre-existing changes and unfinished work are preserved.
