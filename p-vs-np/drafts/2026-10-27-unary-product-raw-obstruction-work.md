# Step 527 — unary products: raw versus right-closed test

The prior EXPLORE assessment is
`literature/2026-10-26-unary-product-sparse-quotient.md`, supplied at startup.
This is one mathematical attempt on its unchanged target. Existing notebook
changes are retained. No source refresh, cut table, row search or finite-job
receiver is needed for the following exact test.

Main gap: unrestricted uniform P versus NP. Intermediate target: the
linear-support/linear-intermediate-size scalar chain for independent unary
FG/GF products. Possible use: the unary sector of the fourth comparison;
mixed-letter Dcomm, binding, full costs and general availability remain open.
Continue a raw-first quotient only if its boundary and both raw transition
equations are consistent on every allowed input. A single allowed pair with
different raw marked-constant coefficients rejects that proposal, but not
closed-only chains.

## Reasoning saved before final verification

Take F to be one x edge and G one scalar-one edge, both with two distinct
roots. The exact three-connector product recipe has six vertices, five
edges and five singleton entries in each order, so the denominator is 32.
In recipe numbering (source 0, sink 1, first copy 2,3, second copy 4,5),
the common path is 0,2,3,4,5,1. Its FG labels are 1,x,1,1,1; its GF
labels are 1,1,1,x,1. With a diagnostic symbol c marking scalar edges,
the words are c x c^3 and c^3 x c. Scalar one is still not a letter of
the original polynomial alphabet.

Raw equations for A -> B are eta_A X=eta_B, E_A0 X=X E_B0,
E_Ax X=X E_Bx and theta_A=X theta_B. Known simulation soundness applies
over F₂ to the auxiliary alphabet {c,x}, so every arrow and every zigzag
preserves each marked-constant word coefficient. The coefficient of
c x c^3 is 1 for FG and 0 for GF. This looks like a complete obstruction
to any raw-first chain, independent of its size; verify all recipe indices
and the right-closed boundary/transition values before canonizing it.

For right closure, preliminary exact rows are alpha_FG=e0+e2 and
alpha_GF=e0+e2+e3+e4; beta=e1. M_FG has only row 2, equal to
e3+e4+e5+e1; M_GF has only row 4, equal to e5+e1. Both series are x,
with empty coefficient zero and M_x^2=0. These are finite matrices, not
an epsilon-free occurrence graph or a claim of a general sparse bound.

The scoped duplicate/failure check read L112's hypotheses and cancellation
stage, L110 §§2–4 and product recipe in §21, L111's source conventions and
§§4,7, L035's hypotheses and central formula, and searched the step-524–526
notes/assessments and Attempt 047. Their raw/closed warning was explicit;
no such endpoint obstruction was already established in those passages.
L112's quadratic cut failure is independent and remains preserved.

## Completed result

The exact check is complete in
[L113](../lemmas/L113-unary-product-raw-simulation-obstruction.md), including
all finite matrices, every right-closed coefficient case and a
constant-free operand subfamily. The outcome is NEGATIVE for the
raw-first proposal, not for closed-only chains. The preserved preliminary
reasoning above is superseded by that canonical proof. The unchanged
assessment remains available for the still-open closed-only part of its
original target; no new assessment or mathematics is approved in this note.
