# Endpoint fixed phase-neighborhood test — 2026-09-24

The gap is the arithmetic sign at the coupled endpoint heights r=2n,
a_n=sqrt(4π²exp(4r)−25), within the missing initial logarithmic
Laguerre range. The intermediate target is a quantitative neighborhood
of the Liouville prime phases through y=exp(6 sqrt(r)) that preserves
a negative margin of order 1/r uniformly over every larger-prime
completion. Such a neighborhood could support a different effective
return argument. The test is whether its integrated perturbation stays
below the negative margin A/(4r), A=ζ(2)², with a surviving fixed
multiple of 1/r greater than E_r=(1+r)²exp(−r/256). Return on the
coupled height scale and transfer to the prescribed a_n would remain
separate unresolved steps.

Redundancy review: read GOAL.md, PROGRESS.md, the whole PROOF.md
overview and global DAG, and inspected the existing changes. L335
supplies Liouville negativity, L336 uses absolute coefficient mass
to obtain a shrinking tolerance and an excessive return certificate,
L337 rules out constraining only primes through r, and L338 controls
arbitrary completions after a square-root exponential prime cutoff.
None proves a fixed angular neighborhood at that cutoff. The stopped
return certificate is not reopened merely by changing the tolerance.
GOAL.md supersedes the historical September 21 admission condition;
all prior mathematical evidence and unfinished work are preserved.
Zero consecutive unresolved exploration turns precede this test.

Unfinished reasoning saved before the uniform proof: write
ω(p)=−exp(iθ_p) for p≤y and pair the Euler factors at the same
complex argument s. Relative to F_λ(s)² their finite product is

H_r(s)=∏_(p≤y)(1+p^(−s))²/
                    [(1+exp(iθ_p)p^(−s))(1+exp(−iθ_p)p^(−s))].

The logarithm has coefficients
2(−1)^(m+1)(1−cos(mθ_p))p^(−ms)/m, hence a quadratic phase loss.
Bounding H_r−1 directly would still accumulate log log y. Instead
normalize by h_r=H_r(σ)≥1 at σ=1+1/(2sqrt(r)). The vertical
logarithmic variation should be bounded by
ε² |v| Σ_(p≤y)log p·p^(−σ)(1+p^(−σ))/(1−p^(−σ))³.
Mertens' reciprocal-prime asymptotic from L338 should make this sum
at most (6+o(1))sqrt(r). Thus a fixed ε=1/10 would bound the
normalized product on v=t/sqrt(r) by exp(|t|/16), eventually.
The remaining Euler product has logarithm at most 4B_r with
lim 4B_r=4J_6(1/2)<1/15. Test the resulting Gaussian error using
|t|≤(1+t²)/2 and the exact zeroth and second Gaussian moments.
The far contour still needs a global polynomial bound, since an
exponential in |v| cannot be integrated against its algebraic tail.
All uniformities, the positive normalization and interior-sum error
remain to be checked. No fixed tolerance is claimed at this checkpoint.

Result: [L339](../lemmas/L339-endpoint-fixed-phase-neighborhood.md)
proves that |θ_p|≤1/10 for every p≤exp(6 sqrt(r)) forces both
endpoint sums to be at most −ζ(2)²/(8r), eventually, uniformly
over every larger-prime assignment. The positive normalizing factor
is at least one and at most C r^(1/200). The normalized comparison
with the Liouville sum has limiting absolute error at most
A·412505/3437154<A/8 after multiplying by r. This proves the
stronger negative margin −A h_r/(8r), without any numerical
starting r or convergence assumption on the varying phases.

The proof uses Mertens' reciprocal-prime asymptotic already proved
in L338 to show Σ_(p≤y)(log p)/p=log y+o(log y). Pairing eliminates
the linear phase error; normalization removes the accumulated size
of the finite product. Its scaled vertical logarithmic variation
is at most |t|/16. For the far contour a separate polynomial bound
is used, since an exponential bound in |v| would not be integrable
against the algebraic kernel tail. Uniform Gaussian domination,
the unconstrained prime tail and the omitted discrete indices are
all controlled before passing to the limit or taking suprema.

Assessment: ADVANCE; zero consecutive unresolved exploration turns.
The fixed phase tolerance improves on the shrinking tolerance in
L336 and meets the required negative 1/r margin above E_r. It
does not give a return estimate, a value at a_n, a Laguerre sign or
a larger exclusion interval. The endpoint arithmetic margin and
main low-index gap remain unresolved; there is no RH candidate.
The subsequent return test will retain individual Fourier weights
in the reciprocal-frequency discrepancy instead of L336's worst
frequency replacement. Its required error is below the product
bump's constant-term surplus on length exp(2r). This is a specific
changed estimate to test, with no assertion that the growing phase
dimension permits it; L336's stopped certificate is not reinstated.
The sole current action is in PROGRESS.md.

Verification: reviewed logarithm branches, conjugate pairing,
positive normalization, the partial-summation remainder, uniform
near and far contour bounds, the strict Gaussian budget, interior
transfer and all three direct mathematical DAG inputs. The exact
check `python3 scripts/laguerre/check_endpoint_phase_neighborhood.py`
passes 60 paired-log coefficient identities and ten rational checks.
They supplement the informal proof and are not a numerical
asymptotic or recurrence certificate. Full Mathlib coverage is not
checked; inherited supporting names, links and source qualifications
are retained. The structure check passes with 342 nodes and 772
edges, and `git diff --check` passes. All pre-existing changes and
unfinished work remain.
