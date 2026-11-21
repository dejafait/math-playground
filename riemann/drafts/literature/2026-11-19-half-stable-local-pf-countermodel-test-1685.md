# Half-stable countermodel test: prepared continuation1685

TARGET: Test whether the half-stable density p(x)=exp(-1/(4x))/(2 sqrt(pi) x^(3/2)) for x>0, extended by zero, is a countermodel to self-decomposable local-PF propagation by proving its fixed-order local differential determinant asymptotics and exhibiting a negative global 2-by-2 translation minor.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1685 searched self-decomposable/local PF, stable additive translation kernels, half-stable total positivity and Wronskian terms; no exact all-fixed-order local statement found in the inspected sources. Reuse source-notes1685 and the unchanged C466a/audit882 coverage. No novelty claim.
SOURCE_EVIDENCE: Simon, Positive stable densities and the bell-shape, arXiv:1302.0956v1, Introduction p2 and Section3.2 pp9-10, https://arxiv.org/pdf/1302.0956v1 ; Sra2611.02944v1 LemmaC.1/proof p20, LemmaC.16/proof pp37-38, PropositionC.25/complete proof pp44-45, https://arxiv.cnoctave.top/pdf/2611.02944 ; canonical C466a full saddlepoint/local-domain proof and precise citations reused. Schoenberg characterization is comparison only, not essential to the explicit negative-minor test.
COMPARISON: The positive law, smooth endpoint behavior, inverse-gamma identity, drift-free self-decomposability and global TP2 failure are source-covered. Sra/C466a supply a fixed-order saddle/Fourier/determinant method and interval transfer, not the local determinant conclusion for this density. Only this explicit missing specialization and an exact negative-minor witness are to be calculated.
GAP: Verify normalization against X_(1/2)=1/(4 Gamma_(1/2)); establish a positive leading differential determinant for every fixed k on a whole interval next to zero, and give a rigorous negative 2-by-2 ordered translation minor. Finite sampling, bell-shape or a pointwise Gaussian limit alone do not establish the local hypothesis.
REASON: A complete countermodel would reject a proposed generic bridge to actual-Xi global PF while preserving actual-Xi extra structure as an independent question. Known-method specialization is justified to check the exact stronger local hypothesis absent from the inspected theorem statements; no reproof of standard stable-law theory is needed.
SCOPE: Newly written ready assessment; separate approval next turn is required before mathematics. One analytic/symbolic calculation, no parameter sweep, no new zero-free estimate and no assumption of actual-Xi realization. Suitable classification REPRODUCTION for this standard-method specialization, not creative or a new general PF theorem.

## Mathematical contract for the later attempt

The input is the single explicit p in TARGET, not a sequence of laws
depending on the verified order. Import the stable probability law and
self-decomposability from Simon at the exact passages above. Check the
elementary inverse-gamma change of variable and zero extension. The
new all-fixed-order local conclusion must still be proved.

Use the convention

    D_k(p;x)=(-1)^(k(k-1)/2) det[p^(i+j)(x)]_(0<=i,j<k).

For the saddlepoint route let B be minus the logarithm of the known
Laplace transform and define x_s=B'(s), v_s=-B''(s). The required
fixed-k test is positivity, for example by proving

    D_k(p;x_s)/(p(x_s)^k v_s^(-k(k-1)/2) product_(j=0)^(k-1) j!) -> 1.

This is a proposed threshold, not a result of review1685. Verify the
whole derivative limit under Fourier inversion and that x_s covers
a whole interval next to zero. Alternatively compute the explicit
derivative determinant's leading coefficient with all cancellations
controlled. No finite check in k suffices. Sra LemmaC.16 is applicable
only after all D_j through the fixed m have a common positive interval;
the two increasing tuples must have all cross differences inside it.
The local-domain proof and determinant signs in C466a are reusable
method inputs, not a claim that C466a applies directly to this p.

For failure of global PF, import Simon's TP2-failure statement, but
also produce one exact negative 2-by-2 translation minor as a
checkable witness for the proposed normalization. Do not use a plot,
numerical inversion or the entire-reciprocal obstruction as a substitute.

Continue only if every premise of nomination1684 is met by this SAME
density. If a local determinant has a nonpositive leading term or the
proposed transfer fails, save that finding and abandon this particular
construction pending a materially new input; it would not establish
the generic propagation theorem. Do not add stronger hypotheses to
nomination1684 in order to avoid a countermodel.

Even success would not decide RH, C028g's S_F, or propagation with
actual-Xi additional assumptions such as its entire reciprocal and
global log-concavity. No source claims those extra assumptions for p.
Full matching Mathlib coverage is unchecked. No cross-notebook input.
