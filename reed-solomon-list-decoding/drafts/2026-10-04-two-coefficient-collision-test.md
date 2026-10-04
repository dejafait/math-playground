# Two-coefficient collision test: working calculation

The saved SPECIALIZE assessment is
`drafts/literature/2026-10-04-two-leading-coefficient-fibers.md`.
This is one mathematical attempt on its unchanged target, with no new
literature work or use of the unread optional moment-count leads.

The gap is the unsafe-grid comparison at A=k+2 on the fixed proper
order-1024 subgroup in F_65537 inside F_{65537^28}. A single coefficient
class exceeding 65537^28/2^128 would exclude another grid radius for
every interleaving width. A missed lower certificate leaves that rate
unresolved; it cannot establish safety.

For S of cardinality s=k+2, write e1(S)=sum(S) and
e2(S)=sum_{x<y in S}xy, with the second sum over unordered pairs.
The common pivot is X^(k+2)-b X^(k+1)+c X^k. Matching e1=b,e2=c
cancels the three leading terms of its difference from the root product.
The candidate has degree less than k and exactly S as its agreements.
Conversely, s agreements force that monic degree-s difference to be the
root product; the other rows must vanish. This reproduces the cited
scalar coefficient dictionary with the extension and column metric checks.

There are Q^2 coefficient pairs in the source field, Q=65537. The
collision lower certificate is ceil(binomial(1024,k+2)/Q^2), whereas
the safety threshold retains the ambient q=Q^28. Preliminary exact
integer comparisons gave the following floor base-two exponents of the
certificate: 986,796,525,316 at k=512,256,128,64 respectively. The
first three exceed the threshold, which is between 2^320 and 2^321;
the fourth does not. No maximizing pair, actual largest joint-fiber
count or full-code upper bound has been computed.

The full center-list proof and symbolic threshold comparison are now in
[L013](../lemmas/L013-two-leading-coefficient-fibers.md). Independent
small-domain interpolation and exact arithmetic passed, with output in
`scripts/coefficient-fibers/two-coefficient-results.json`. The known
collision mechanism warrants REPRODUCTION, not a novelty claim. The
rate-1/16 bare averaging failure is preserved separately; no uniform
joint-fiber upper bound has been attempted in this step.
