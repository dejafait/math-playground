# Fixed defect-window scalar norm threshold: stop705

The approved704 target asked whether unchanged C744y full evidence,
converted to C744z's actual restricted energy metric, yields
||R||^2<3/4. [C744z Section10](../lemmas/C744z-neutral-shared-middle-completion.md)
contains the complete specialization, inherited qualifications and
exact rational bound. It gives strict contraction ||R||^2<.998001,
but does not reach3/4. The full certificate is
`scripts/separation-seven/defect-window-norm-705.json`; all17 exact
checks pass and all seven inherited artifact hashes remain unchanged.

WHY IT FAILS: Scalarizing the full head/tail coupling to ||F||^2<10.061
and the cross operator to ||T||<4.71 yields only the full L2 floor
m=.004716385. Its relative energy conversion has norm upper bound
4.71/(4.71+m). The exact limiting root of this fixed scalar comparison
also gives a squared upper-bound value greater than3/4, so rounding
refinement cannot settle window vacuity by this comparison. This is
not an actual norm lower bound, a negative direction, a nonempty-window
certificate or a global ban on extracting more directional information
from C744y. No tau, cutoff, penalty or allocation was retuned.

Stop this scalar extraction. An independently testable exact-neutral
finite trial-pair lower bound could instead settle nonvacuity; its
coverage is REVIEW_REQUIRED in the new705 assessment. The complete
signed S3, higher/mixed endpoints, H2 and Xi transfer remain open.
