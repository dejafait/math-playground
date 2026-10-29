# Residual-relation generators — bounded source comparison completed

TARGET: Test whether the dyadic path endpoint relation E_N={(u,v):uR_A=vR_B}, N=2^k, has a generating basis with total scalar support O(N) whose induced shift has an acyclic singleton realization of O(N) occurrences and preserves both accepting boundaries.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 541 searched the joint sparse common-source/residual-basis target, sparse null bases/matrix sparsification, invariant generators and binary Pascal/Sierpinski transformations; actual queries and inspected local failures are in drafts/2026-10-28-residual-relation-source-review-work.md. No exact quantitative match was established; no novelty or nonexistence claim follows.
SOURCE_EVIDENCE: Reused ready scalar simulation/factorization/up-to coverage; inspected Bhaduri arXiv:2109.00732v3 Definitions 3.1/3.3/3.5, Theorems 3.2/3.8 and Proposition 3.7 with proof cases; Gottlieb–Neylon arXiv:1008.1498v1 §§2.2–3.2, Lemmas 2–3/Theorem 4; Coleman–Pothen (1986) Algorithm 2.1/Theorem 2.1 and its proof; Boyar–Find arXiv:1305.3041v1 §6 Theorem 10/Proposition 3 and cancellation discussion. Versions, pages and qualifications are in the source notes.
COMPARISON: Qualitative common sources and semantic kernel relations are known. Sparse null-basis optimization does not control a shift realization or boundaries; the inspected rational/real results cannot be silently imported over F₂. Cancellation-free Sierpinski circuit bounds are not arbitrary-generator support bounds. L122/L123 stop specified lifts, not every basis of E_N.
GAP: Neither an O(N) expanded-support basis together with its O(N) acyclic singleton realization and both boundaries, nor an obstruction to every such basis/realization, is established by the inspected sources. Sparse generators, sparse shift coordinates and sparse occurrence realization remain separate obligations.
REASON: Primary hypotheses and essential proof cases now distinguish known qualitative algebra and sparsification from this exact joint quantitative target sufficiently for one bounded attempt. There is no essential inaccessible premise. Retain the target unchanged; separate next-turn approval precedes research under this newly completed assessment.
LITERATURE_REASON: The new exact target optimizes generator coordinates and the induced shift jointly, outside the prior assessment's incidence-template scope. This turn fills that missing comparison and does not repeat a ready-target review merely for balance.
SCOPE: Original F₂ dyadic endpoints A=Prod(F_N,G_N), B=Prod(G_N,F_N), N=2^k, all original coordinates and right-closed residuals retained; freely chosen row basis of the full E_N, expanded support, induced shift and literal acyclic singleton realization with both initial/final boundary equations. Begin with complete N=4 data; no source supplies an asymptotic bound or an all-basis obstruction.

Step 540 created this as REVIEW_REQUIRED without attempting the new
mathematics. Step 541 completes one LITERATURE / EXPLORATION /
NOVELTY_UNCHECKED comparison. The assessment is now ready for separate
approval; no research under it has occurred. Step 540's negative result
and all earlier work remain intact. Detailed source evidence and queries
are in [the review notes](../2026-10-28-residual-relation-source-review-work.md).

The endpoints remain L110's original wrapped products on L122's dyadic
path family. R_A,R_B mean the full columns of right-closed state
residuals, including zero-residual vertices and the final coordinate.
Rows u,v range over all original endpoint coordinates. The proposed
shift is (u,v)->(uM_A,vM_B); candidate maps must receive both original
initial boundaries and their final functional. A polynomial equality
alone is insufficient. No support bound, shift realization, existence
theorem or obstruction is asserted here.

The comparison distinguishes qualitative finite generation from total expanded scalar support,
cancellation-free restrictions from arbitrary F₂ sums, and sparse matrix
generators from an acyclic singleton occurrence realization. The prior
primary simulation coverage is reused.
Potential linear-circuit or binomial-transform sparsification results are
not assumed facts; the specific inspected comparisons are recorded below.
Search failures do not certify novelty.

After separate approval, the independent initial discriminant is N=4:
an explicit generator matrix, its shift equations and accepting-boundary
coordinates, with all support charged. Finite low-weight generators alone
would not establish a uniform bound. A lower bound for this common-source
generator model would not rule out general mixed-orientation chains.

Require the candidate generator rows to span the full E_N, not just a
paired reachable subspace. Record their two endpoint blocks, all induced
shift-coordinate equations, and the coordinates receiving both original
initial rows and their common final functional. A claimed occurrence
realization must specify the actual 1/x graph, closure, accepting roots
and any extra boundary/auxiliary maps, charging every entry and occurrence.
The displayed generator blocks need not alone be the full maps after
boundary states are added; those additions must be checked and charged.
Do not treat a compressed XOR program or a dense closure oracle as free.

Continue only from complete finite equations and a concrete proposed
uniform mechanism, or an informative lower bound with its exact scope.
A failed equation rejects that proposal; a proved superlinear necessary
support or occurrence count stops its claimed linear construction.
Failure to find a basis at N=4 is an unfinished search unless exhaustively
certified with the quantified realization scope. N=4 success is a
discriminant, not an asymptotic theorem. No numerical threshold or universal
constant has been obtained in this literature turn.

## Source comparison and reuse

Ésik–Maletti's [2010 word-automata manuscript](https://www.informatik.uni-leipzig.de/~maletti/pub/esimal10.pdf),
Definition 3.1/Theorem 4.2, pp.2–3, already gives scalar soundness and a
common source from generators of paired reachable rows. Its three
equations match L110's closed convention. It does not identify that space
with the full E_N or bound our ledger. Existing factorization/splitting
and Bonchi–König–Küpper up-to comparisons are reused from the 26/27-Oct
assessments; no general theorem is reproved.

Bhaduri's [v3 preprint](https://arxiv.org/pdf/2109.00732v3), printed
pp.11–14, covers semantic kernel relations over semirings including F₂,
not sparse presentations. Its quotient/finality arguments do not control
our fixed original coordinates. Gottlieb–Neylon's
[retrieved v1 text](https://arxiv.org/pdf/1008.1498v1), printed pp.4–7,
compares sparse null bases with matrix sparsification over its stated
rational domain; no quantitative shift/boundary conclusion is imported.
Coleman–Pothen's [Theorem 2.1 and proof](https://cedric.cnam.fr/~bentzc/INITREC/Files/DW10.pdf),
pp.529–531, concerns greedy minimum-support null bases, with real-sign
decomposition in the proof. Neither source proves our binary-family
bound or supplies a shift-compatible optimum.

Boyar–Find's [2013 v1 §6](https://arxiv.org/pdf/1305.3041v1), printed
pp.10–14, proves its Sierpinski bound for cancellation-free XOR circuits
and explicitly discusses the cancellation case. The gate-elimination
proof is not an arbitrary F₂ generator argument. No reduction from the
present joint basis/realization problem to that circuit model is supplied
or assumed. Later circuit-covering leads are unread and not used to
assert present-day optimal bounds.

The local duplicate/failure check reads L110 §§4,21; L122 §§2,4–5;
L123 §§1,4–5; Attempts 056/057 and history 540. Earlier fixed-basis,
placement and incidence stops remain comparisons. No checked local
result settles arbitrary residual generators. No cross-notebook input
is used. Full matching Mathlib coverage is not checked; supporting
linear algebra is not a matching quantitative theorem.

This subtarget could isolate the state-coordinate issue behind the unary
fourth comparison. It leaves general r/G, general F, mixed letters,
actual receptions, all full resource costs, certificate availability and
uniform P versus NP unresolved. No source blocker, receiver change,
historical recovery or cross-notebook input is assumed.
