# Ramified dyadic integral-affine disk stage

Approved target and gate: the exact full-image action in PROGRESS.md, using
unchanged drafts/literature/2026-10-16-ramified-dyadic-two-descent-image.md.
This is a bounded stage of that target, not a changed target or new source review.

Before implementation: use L078's entire maximal ring and labels. On the
original E0 model, each x in O_H has two points: modulo pi, x^3-x^2=0,
and y^2+y has the two simple roots 0,1. The cubic Kummer value is
4x-theta. Its J-valuation is 44, because v_J(4x)>=66 and v_J(theta)=44.
Normalize by rho^44, a square. A change x by pi^15 O_H changes the
normalized unit by valuation >=66+45-44=67, beyond the square threshold 66.
Thus all 2^15 disks can be realized and labeled exactly with L078.

Compute exact integral coefficients of A=4/rho^44 and B=-theta/rho^44
before finite reduction; verify rho^44*A=4 and rho^44*B=-theta exactly.
Enumerate representatives sum b_i pi^i, 0<=i<15. Save every disk, its
label and full normal-form reconstruction. Compare collisions in the
fixed 34-bit basis. Required complete-image size is 2048, but matching it
will not substitute for the pending chart/exceptional coverage.

Continuation test: certify arithmetic and every integral disk, or save
an exact blocker. Do not infer global unit independence or a rank bound.
The global gap is primitive integer emptiness; a full local test could
support further supported-unit filtering. Class contributions and actual
global directions remain unresolved. Parked searches 034–036 stay parked.

## Completed stage

Canonical [L079](../lemmas/L079-ramified-dyadic-integral-affine-image.md)
contains the proof and citations. All 32768 integral disks were realized
and labeled, with 2048 distinct labels of rank eleven. The exact
normalized input was formed before reduction, preserving precision 99;
disk constancy has valuation bound 67>66. The construction certificate
passes 15/15 checks and the full-record replay passes 8/8, with no
failures. Both complete check fields and the original independent label
witnesses were inspected; replay checked every disk reconstruction,
input, mask and collision rather than a bounded preview.

Realized inequivalent classes plus the cited BPT image-size theorem
prove abstract full-image equality and membership. The stricter requested
LocalImage disk certificate still needs reciprocal and exceptional chart
coverage. No chart run is inferred from that cardinality argument.
The next action remains the same covered target, with affine work
reused; no new assessment, global restriction rank or class value is
claimed. Independent critical audits of L078 and L079 remain pending.
