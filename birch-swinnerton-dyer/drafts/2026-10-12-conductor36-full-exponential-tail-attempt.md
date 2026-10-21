# Fixed full-exponential tail planning — work in progress

Approved target: Implement and independently replay full-exponential-tail planning on L054's fixed 98 points and uncombined absolute occurrence weights, testing all 72 normalized two-sided tail widths <=2^-38 with cutoff <=4860 and total distinct terms <=1000000.

The unchanged SPECIALIZE assessment is
`drafts/literature/2026-10-12-conductor36-full-exponential-tail.md`.
Main gap: arbitrary analytic-order-at-least-two rank equality. This attempt
tests a finite tail plan for the conductor-36 relative table; a pass permits
later finite sums, but leaves arithmetic errors, division, integer isolation,
relations and separate audits unresolved. CM excludes L027.

Inputs: L038's saved N=36 presentation; audited L049 identities;
L050 E=[0,0,0,0,1]; audited L051 positive total period and real attenuation;
L053 representatives and L054 fixed coupled solution and absolute occurrences.
L052's integer 24 is downstream only. Structural N=36, L053 and L054
instance critical audits remain pending. No cross-notebook input.

Reuse Wuthrich arXiv:1608.06423v2 equation (2), Lemma 4 and proof,
pp.6--7, without reproof. At every saved rational height enclose
q=exp(-2*pi*y) by audited Machin/Taylor arithmetic; bound
B_H=q^(H+1)/(1-q). First test H=4860 everywhere (minimality is not sought).
Save all Taylor operations, positive power operations, both source-majorant
endpoints and every original uncombined generator occurrence. Independently
replay the source plan, period, brackets, powers and all 72 widths.

Continue only when all upper widths pass, max H<=4860 and sum H<=1000000,
with zero replay failures. A lower source-majorant width above threshold
stops this bound convention on the fixed geometry, not true analytic error.
Straddling intervals are inconclusive and require rational refinement.
Preserve ATTEMPTS/025--028 and all input bytes. No new sums or table here.

Completed as BSD-182. Canonical proof and all qualifications are in
[L055](../lemmas/L055-conductor36-full-exponential-tail-feasibility.md).
The uniform H=4860 plan passes: 476280 terms, all 72 upper widths <=2^-60,
and zero independent replay failures. Every one of 16 q brackets, 2560
Taylor steps, 336 power multiplications, 98 primitive rows and 1316
uncombined occurrences was replayed. This is local finite progress using
known sources, not a new tail theorem or BSD candidate. The separate
assembly audit is pending; the new continuation has REVIEW_REQUIRED
coverage and must receive its own approval turn. No original inputs or
old failure artifacts were changed.
