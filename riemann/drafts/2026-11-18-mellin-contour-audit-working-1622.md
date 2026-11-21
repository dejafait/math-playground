# Mellin contour audit1622: unfinished checkpoint

Completion pointer: the reasoning below was saved before completion.
The finished proof and its exact qualifications are canonical in
`lemmas/C048a-mellin-fixed-height-contour-continuation.md`. No outstanding
claim in this early checkpoint supersedes that result.

18 November 2026. One RESEARCH / proof_audit / conceptual_audit under
the unchanged SPECIALIZE assessment1621. No saddle-error estimate is
being tested. Main gap: actual-Xi all-degree algebraic-square positivity.

Primary source inspected: Kawano, Preprints.org202611.0383v1,
(4)-(5), (25), and Lemma5.1's first two proof paragraphs. DLMF4.13.1
and the principal-branch domain supply the standard Lambert input.
L016/L019/L048 supply real kernel normalization/evenness. L804's
fixed-ray proof and completed audit538 were found during the duplicate
check: its Taylor continuation is reusable method evidence, but its
s coordinate, outward height and saddle map differ. No L804 endpoint
bound or L797 saddle estimate is imported into this test.

Proposed branch test: for fixed r>=exp(12), continue W_0 along
z=(2r/pi)exp(i theta), 0<=theta<=pi/2+arcsin(1/(4 log r)).
Rule out first exits of U>0, 0<V<pi/2 by modulus on U=0 and by
the argument at V=pi/2. This avoids an uncontrolled asymptotic.
The proof is still to be written and checked.

Remaining audit: complex compact normal convergence of the full theta
series; real evenness extended by identity theorem; exact small arc
and far-vertical limits at fixed height; locally normal meromorphic
origin series with residues c_n and comparison to (25); y=0 and
reflection; open neighborhoods of closed-sector points. Only after
these checks may the contour prerequisite be marked validated.

Success supports a later separately assessed exterior-remainder step.
It does not validate its quantitative budget, finite zero count,
inverse density, coefficient-to-mixed-sign bridge, or RH. A branch or
uncanceled endpoint failure stops this source step. No numerical
script, certificate, cross-notebook input or shared-state edit.
