# 2026-10-04 — Cubic/cofactor upper test and estimate stop

Completed exactly the saved upper-test subtarget under its prior
SPECIALIZE coverage, without further literature work. The gap was the
degree-67 family's effective upper comparison at 66 agreements. The
test was a certified cap at most 65537^28/2^128, which would exclude
this family as an unsafe witness; missing that comparison would leave
the family and arbitrary-center maximum unresolved. L015's dictionary
was reused, and the earlier degree-66 stop and averaging failures were
preserved.

[L016](../lemmas/L016-cubic-cofactor-sieve-cap-and-limitation.md)
retains the residual-factor Fourier sum, eliminates linear phases and
applies the imported monomial estimate and weighted sieve in each
remaining phase degree. Its upper cap is between 320297 and 320298
times threshold; the rational refinement is between 294741 and 294742.
This establishes no large list. L001's older support cap is stronger,
between 1050 and 1051 times threshold, and also inconclusive. This step
does not improve the existing list upper bound. The exact cofactor norm
also
shows that the constant cubic sieve cap followed by absolute summation
cannot certify the threshold even with exact cofactor magnitudes. The
allowance lower bound is about 35496 times threshold, not an actual
error or list lower bound. Stop that calculation and preserve it in
[ATTEMPTS/006](../ATTEMPTS/006-cubic-cofactor-constant-weight-upper.md).

Outcome: NEGATIVE, new evidence changing the estimate decision;
STEP_KIND: RESEARCH; classification: REPRODUCTION. This specializes
known scalar character/sieve tools and elementary orthogonality. No
progress beyond the checked literature, completed candidate, safety or
unsafety claim is made. Exploration turns used remain 0/3; the negative
test is not an exploratory or stalled repeat. The degree-67 dictionary
remains useful, but the family's maximum is unknown. The rate-1/16
bound t_star<=958 and the other rate bounds 509,765,893 are unchanged.

The next direction tests correlated cycle/cofactor error rather than
the stopped constant-weight absolute sum. This requires a new input
outside the prior scope, which excluded new character estimates. Save
[REVIEW_REQUIRED coverage](../drafts/literature/2026-10-04-correlated-cubic-cofactor-error.md)
for that exact next target; the next turn reviews sources before more
mathematics. The ABF26 and other persistent source blockers stay parked.
This is a proposed bounded mechanism, not an assumed completion route.

The [exact certificate](../scripts/coefficient-fibers/cubic-cofactor-upper-results.json)
passed. It checks all finite inequalities with integers and rationals.
On an order-8 subgroup of F_17 it checks the signed three-moment sieve,
factorial normalization and cofactor convolution against direct counts.
An exact cyclotomic calculation over all 4624 cubic parameter vectors
checks the cofactor norm identity. No large-domain fibers are enumerated.
An initial script assertion had the characteristic divisibility test
reversed; it was corrected before the successful certificate run.

The overview records the estimate failure and leaves the main gap open.
The ID-only DAG adds only L016's genuine mathematical use of L015.
All preexisting notebook and neighboring changes were preserved.

Validation: the shared documentation checker passed with 18 nodes and
17 edges; `git diff --check -- .` passed. Exact ready coverage for the
completed target, the next REVIEW_REQUIRED target match, unique step
fields and the mathematical certificate passed. The checkpoint has 14
lines and the overview 100. Structural validation does not prove the
mathematics or settle the missing lists.
