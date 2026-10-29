# Step 544 — basis-independent residual weight filtration

One bounded mathematical attempt under the unchanged, supplied EXPLORE
assessment `drafts/literature/2026-10-28-residual-relation-generators.md`.
No literature refresh, cross-notebook input, or change of target is needed.
All pre-existing unfinished work is preserved.

Main gap: ordinary uniform P versus NP remains unresolved. The immediate
target is the assessed full original-coordinate relation basis with O(N)
expanded support, an O(N) acyclic singleton realization and both boundaries.
A necessary support obstruction could stop that particular common-source
route to the unary fourth comparison, while leaving general scalar chains,
general operands, actual reception and all unrestricted complexity claims open.

Inputs inspected: L125 hypotheses/§§1–2,6–7; L124 §3; L122 hypotheses/§2;
L110 §4; Attempt 058 and history 543. Reuse the recorded primary target
audit and literature comparisons. The exact relation core is
`(r,(b+r)P_N; b,rP_N)`, with six disjoint unit directions and one paired
final direction. P_N is the binary Pascal translation matrix; N=2^k.
The original endpoints and S=16N+20 are fixed.

Bounded discriminant: enumerate every original-coordinate relation of
weight at most four at N=16 by enumerating coordinate subsets, not the
entire 2^32 core. Check residual equality directly, record every passing
row and compute complete threshold-span ranks. The predicted core rank
at weight four is 16 (full rank 23 after the seven disjoint directions).
A different rank rejects that prediction. Agreement alone proves no
asymptotic lower bound. Only then test a uniform tensor/weight inequality;
do not repeat the stopped balanced-basis optimization.

Unresolved at this checkpoint: a uniform all-basis rank bound, sparse
shift coordinates and literal realization, all other reception/resource
gaps, and P versus NP. No calculation outcome or new theorem is asserted
in this saved setup.

## Finite discriminant and candidate uniform argument

The completed direct subset enumeration at N=16 checks all 1,091,059
subsets of the 72 original coordinates of size at most four. Core ranks
are `[0,0,1,6,16]`; full ranks are `[0,6,8,13,23]`. The prediction passes.
All passing rows and rank witnesses are saved in
`scripts/batched-incidence/output-544/weight-filtration.json`.
This alone is only a finite result; independent replay is still pending.

Candidate uniform mechanism, saved before its detailed check: identify
the index j with its binary subset of k variables. Pascal multiplication
is simultaneous substitution x_i -> 1+x_i in a multilinear polynomial.
For a nonzero multilinear f of total degree d, try to prove
`s(f) s(f(1+x)) >= 2^d`, where s counts nonzero monomials. The induction
splits f=f0+x_k f1. Write a=s(f0), b=s(f1), c=s(f0*),
e=s((f0+f1)*), h=s(f1*); then c<=e+h. If deg(f0)=d, use
`(a+b)(e+h)>=ac`. Otherwise deg(f1)=d-1. If deg(f0)=d-1,
use `(a+b)(e+h)>=ac+bh`; if deg(f0)<d-1, use
`(a+b)e>=s(f0+f1)e` and `(a+b)h>=bh`. Each case appears to give
the required 2^d from the induction hypothesis. Zero polynomials and
d=0 must be handled explicitly.

For a core row `(r,(b+r)P;b,rP)` of weight W, the proposed inequality
would imply `W>=2*2^(deg(r)/2)` and `W>=2*2^(deg(b)/2)` separately,
using `s(bP)<=s((b+r)P)+s(rP)` in the second case. Thus every nonzero
parameter coefficient j forces W>=2*(sqrt(2))^popcount(j). An invertible
parameter matrix for any full relation basis has a nonzero determinant
term selecting each parameter column once. Summing the selected row
bounds, and charging the six free unit parameters and paired final
parameter, would give total support at least
`8+4*(1+sqrt(2))^k`. This is superlinear relative to S=16*2^k+20.
These are candidate deductions at this checkpoint, pending the full
induction, coordinate correspondence and arbitrary-basis argument.

## Completed attempt

The full induction and arbitrary-basis argument are now canonical in
[L126](../lemmas/L126-dyadic-full-relation-basis-support-obstruction.md).
They establish the lower bound `8+4*(1+sqrt(2))^k` for all generators
spanning the full original E_N. This changes the route decision from
stopping one balanced basis to stopping that whole full-relation target.
It does not obstruct smaller invariant subspaces or general chains.

The independent syndrome-join replay receives every original-coordinate
N=16 relation of weight at most four, with core rank 16 and full rank 23.
It also checks every one of the 65,809 nonzero multilinear polynomials
in zero through four variables against the support-product inequality.
Every row and product check is retained in
`scripts/batched-incidence/output-544/audit.json`; there are no finite
failures. The all-k conclusion uses the proof, not this finite check.

One RESEARCH / NEGATIVE / POTENTIALLY_NEW attempt is complete. This is a
new local obstruction relative to the recorded restricted stops, not
certified progress beyond all literature. Attempt 059 preserves its
scope. A new REVIEW_REQUIRED continuation requests separate source-gate
approval and conceptual audit of the argument; no second mathematical
attempt or source review occurs in this turn. All prior work is retained.
