# Step 538 — dyadic scalar-incidence attempt (working checkpoint)

The supplied startup overview/DAG and unchanged ready EXPLORE assessment
`drafts/literature/2026-10-27-batched-incidence-zigzag.md` were read before
this RESEARCH / proof_attempt. Its exact TARGET remains the sole target.
Existing notebook changes and unfinished work are preserved. No external
source refresh, cross-notebook input or supervisor-state edit is needed.

Main gap: ordinary uniform P versus NP. Intermediate target: a fixed-length
acyclic scalar incidence chain between the original wrapped F_rG/GF_r,
with support plus twice-counted intermediate size <=C*S for a universal C.
A positive result would supply one unary-sector input to the fourth
comparison, leaving general F, mixed letters, actual reception, complete
resource bounds and availability unresolved.

Read L110 §4 and §21's product recipe, L115's complete construction and
ledger, L118 §5's path residual basis, L117 §§3–4, L119 §§4–5 and L120
§§1–4. Checked Attempts 053–054, histories 536–537 and their working notes.
Targeted searches found the suggested dyadic scalar-sum mechanism, but no
already supplied construction for it. Reuse the precise source imports
and limitations in the ready assessment; do not reprove qualitative
simulation or claim novelty from this local search.

One bounded mechanism: replace the full placement grid by an acyclic
network of two-coordinate sums ordered by binary scale. The path test is
r=N=2^k. The conversion between the N monomials z^(j+1) and the N suffix
residuals z(1+z)^j has the binary subset matrix already forced in L118.
Try to share these conversion relations inside one retained auxiliary,
with ordinary output-dead projections permitted and no elementary reverse
companion. A factored matrix is not a free scalar map; all retained gates,
edges, incidences and graph repetitions must be charged.

Continue only on complete oriented boundary/transition equations and a
universal linear ledger, or a precise unfinished map with a discriminating
test. Stop the literal template on a failed necessary equation or forced
superlinear retained count. Test the path family first; a decisive failure
there suffices to stop before the cancellation cases, whose existing
ordinary projections are not invalidated. No missing arrow is itself an
impossibility argument. At this checkpoint no new result is established.

## Literal template selected before replay

Let N=2^k. Use base states b_j, 0<=j<N, with parallel 1/x edges
b_j->b_(j-1) for j>0 and exit b_0. Their full raw suffixes are
(1+z)^j. Initially a_(0,j)=b_j. For each binary scale t=0,...,k-1,
reuse a_(t,j) when bit t of j is zero; otherwise allocate ONE sum vertex
v_(t,j) with two constant edges to a_(t,j) and a_(t,j-2^t), and set
a_(t+1,j)=v_(t,j). There are no identity-copy vertices. Add probes p_j
with one x edge to a_(k,j). D_N has source p_(N-1), exit b_0;
the candidate accepting intermediate is Q_N=Prod(F_N,D_N).

This is a single acyclic singleton graph, with two-coordinate sums and
maximum alias sharing of unchanged registers; no placement grid is used.
It retains every changed dyadic register as a vertex of the final graph.
There is no claim that a general scalar chain must retain such registers.
The first necessary test is its graph charge, before attempting missing
maps. The expected full suffix of a_(t,j) is
z^(j mod 2^t)*(1+z)^(j-(j mod 2^t)); consequently each probe has
right-closed residual z^(j+1), and Q_N has the correct accepted polynomial.
These series facts alone do not prove any accepting simulation arrow.

Provisional obstruction: at a newly allocated v_(t,j), let
l=j mod 2^(t+1), H=j-l. Its raw suffix z^l*(1+z)^H has l>=2^t>0.
Its orders at zero/one recover l,H, hence j and t. Thus the kN/2
changed registers are pairwise distinct nonzero raw suffixes; they cannot
be represented by the same graph vertex while preserving their named
values. The N base values are distinct from them (order at zero zero).
Even optimistic value-preserving vertex sharing therefore leaves at least
N+kN/2 vertices, whose twice-counted charge divided by S=16N+20 diverges.
Constant-only gate states have ZERO right-closed residual; do not substitute
their raw suffixes into an unproved scalar map. The probes supply the first
letter explicitly. Full proof and exact replay are still pending here.

## Completed decision

Canonical proof: `lemmas/L121-retained-dyadic-sum-incidence-obstruction.md`.
Outcome NEGATIVE; classification REPRODUCTION; actual task proof_attempt.
This is a local specialization and route change, not an originality claim.

The full proposed first map keeps the F prefix/boundaries and maps h_j to
p_(N-j-1) for j<N, h_N to b_0. Its initial and final equations pass.
The transition equation fails exactly in rows h_0,...,h_(N-2); in the last
of those rows it requires e_p0=e_v(0,1)+e_b1. These are distinct coordinates.
The scalar series agreement does not repair this failure. All remaining
row cases are checked in the canonical proof; no second map is assumed.

The retained changed gates have distinct full raw suffixes, and the literal
Q_N has 2g(Q_N)=26N+5kN+10. Even arbitrary equal-value vertex sharing
leaves at least N+kN/2 vertices. Against S=16N+20 this forces an unbounded
ratio at least (k+2)/36. Thus repairing the map alone cannot rescue this
retained-register template. General scalar recoding remains outside the
claim. The mandatory path failure stops the attempt before the cancellation
tests; L120's previously checked projections are unaffected.

`scripts/batched-incidence/check_dyadic_sums.py` completed six exact cases
N=1,...,32 by powers of two. Full graphs, all coefficients, all stages,
all gate values and both sides of every equation are saved in
`scripts/batched-incidence/output-538/dyadic-sums.json`, including every
failed coordinate. There were no unexpected verification failures.
Selected --full inspections covered the complete N=2 original/auxiliary
graphs and arrow, all N=8 stages/gates and arrow products, the N=32 ledger,
symbolic thresholds and the complete verification-failure list. Finite
checks do not replace the symbolic proof.

Stop retaining a vertex for every partial dyadic sum (Attempt 055). A
materially different candidate should connect only endpoint placements
using sparse scalar relations and a shared explicit letter-delay spine,
instead of retaining all intermediate changes of basis. No such graph
or maps are established. The exact continuation remains solely in
PROGRESS.md under the unchanged ready target. All prior unfinished work,
independent gaps and receiver/cap/history stops are preserved.
