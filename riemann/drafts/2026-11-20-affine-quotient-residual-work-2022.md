# Affine-quotient residual attempt2022 — working record

Approved target: the exact N=6,7 residual test in assessment2020,
separately approved in step2021. Main gap: L030–L032/C032a actual-Xi
mixed positivity; the relevant downstream sufficient premise is C029m's
eventual uniform index bound. No convergence premise is used here.

Reuse C029n's normalization and fixed rational enclosures, C029o's
kernel order, and C029p's audited degree-six baseline. Comparison2020
and approval2021 already cover the exact family, quotient interface and
scoped failures; no new source review is needed. Existing work is retained.

Before sign inspection, write U_6=sum b_i t^i and U_7=sum c_i t^i.
With l=b_6, m=b_5, L=c_7, M=c_6, use the common denominator
D=l^2, Q(t)=(Ll)t+(Ml-Lm). The proposed quotient is q=Q/D;
check degree seven and l!=0, then check DU_7=QU_6+R, deg R<6.
Construct the rectangular matrix H by Q Phi_6=H^t Phi_7, so E=H/D.
Store the exact residual as (D^2 B_7-H B_6 H^t)/D^2. No polynomial
normalization, spectral fit, degree increase or input refinement occurs.

The verification will check both kernel identities and the embedding
coefficient identity. Enclose the quotient from the individual leading
coefficients using only separated interval reciprocals, then enclose the
entries of B_7-E B_6 E^t. Avoid expanding its high-degree numerator for
interval evaluation: C029o records why such expansion can overestimate.
The complete exact numerator is still retained for algebraic checking.

Test exactly e_i and e_i+/-e_j in descending Phi_7 coordinates, 49
directions. A negative upper bound rejects this PSD ansatz only at this
pair. No witness is inconclusive. All-degree signs, initialization,
singular cases, alternative embeddings and upstream[9]/qualified
compact convergence remain unpaid. Save full certificates under
scripts/pollaczek/; no root counts or unrelated calculations.

State: construction planned; no sign result asserted yet. Any completed
result will be canonical in its lemma, with this note retained as the
pre-computation checkpoint.

Completion2022: the attempt produced a certified e_2 negative direction.
The full proof is canonical in C029q and the full certificate is
scripts/pollaczek/tilted-affine-quotient-residual-2022.json. The fixed
pair test stops; this checkpoint's pre-computation reasoning is retained.
