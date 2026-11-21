# Lower-power first-mode allowance — nomination1632

TARGET: Review source coverage for Kawano v1's lower-power first-mode allowance T_low(p)<=2 L^(3/2)/r on C048c's full sector, where T_low is the normalized finite horizontal integral defined in the assessment.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step1633 searched exact title/low-order and Kawano/Mellin/lower-power/B_low terms, searched specific local Mellin records, inspected L799's differing hypotheses and reused the global-import stop. No independent matching theorem was located; no novelty inference. Full evidence: 2026-11-19-mellin-lower-power-source-notes-1633.md.
SOURCE_EVIDENCE: Kawano Preprints.org202611.0383v1, posted4November2026, DOI10.20944/preprints202611.0383.v1, https://www.preprints.org/manuscript/202611.0383/v1 , Section5.2(28)/Lemma5.1(i)/reflection; AppendixA.2(A3); AppendixB local definitions, Gaussian normalization and B_low/B_modes; AppendixC domain, width, absorbed curvature and lower-power allowance preceding origin cases. Essential cases directly read19November2026; DLMF7.7.6 coverage reused from source-notes1630.
COMPARISON: B_low is a local absolute Gaussian allowance for the negative first-mode factor in the same h_p,g normalization; AppendixC supplies width1/(3L) and threshold2L^(3/2)/r on the saved sector. T_low is an operational definition, not a printed source symbol. C048c(3),(9)-(19) verifies relevant local premises but excludes this correction; L799's rotated-contour bound cannot transfer automatically.
GAP: Coverage suffices for separate reproduction, which must write out finite-integral majorization, exact correction factor, Gaussian normalization and effective constant on the full unbounded sector. AppendixB's finite-band width/cell data are not imported. No T_low inequality is proved here.
REASON: Previously unread essential proof structure and source scope now match the proposed local allowance. A separate SPECIALIZE continuation1633 preserves the mathematical target and requires next-turn approval before research; this completed literature comparison derives no estimate.

## Exact prospective observable

Use C048c's p, r=|p|, L=log r>=12, Re p>=-r/(4L), principal
w=W_0(2p/pi), u_0=w/2, d=1/(3L),
h_p(u)=2p Log u-pi exp(2u), g(u)=8pi^2 exp(9u/2)/u,
K(s)=g(u_0+s)/g(u_0), and A_0=4p(1+w)/w^2.
Set, with real s and the same principal Gaussian branch,

    T_low(p) = |integral_(-d)^d K(s) [-3/(2pi exp(2(u_0+s)))]
                   exp(h_p(u_0+s)-h_p(u_0)) ds|
                   / |sqrt(pi/A_0)|.

This specifies the n=1 lower-power correction identified in the cached
full normalized factor (A3). It is a prospective target definition,
not a new estimate. Review1633 confirms that it operationalizes the
source's local absolute allowance; the source does not name this
integral. The candidate threshold is the source-recorded 2L^(3/2)/r.
Keep its scale; do not silently replace it with a full-path or rotated
amplitude estimate. Source matching must resolve any scope difference.

## Relevance, test and limits

The main gap remains L030-L032/C032a actual-Xi all-degree algebraic-square
positivity. A verified lower-power allowance could pay another finite
local term in a future full actual-theta Mellin remainder. Independent
higher theta modes, horizontal tails, assembly, inversion, zero counts
and sufficient mixed signs remain unpaid. No RH candidate follows.

Continue to a separate reproduction only after matching the observable,
width, domain, normalization, reflection and proof cases, checking the
specific L799 and global-import failure comparison already recorded
in source-notes1627/1630. If the primary bound concerns another scope,
record the mismatch and refine the target before mathematical work.
Failure of a sufficient absolute bound would not itself refute T_low.
No new lemma or mathematical script was written in this review.

LITERATURE_REASON: The target changed from the audited Gaussian pair to the separate lower-power first-mode contribution; its essential primary scope and cases were unread at invocation. Step1633 supplied that missing coverage without new derivation.

Potential local inputs for later reproduction: C048c's audited branch,
geometry, curvature and normalization; C048a's actual-kernel normalization
only as needed. C048d does not bound this correction. Full matching
Mathlib coverage has not been checked. No novelty claim is made.

## Completed review1633

The complete inspected cases, scope qualifications and bounded search
are in `2026-11-19-mellin-lower-power-source-notes-1633.md`.
The local absolute allowance matches the saved prospective observable;
the effective constant is still a reproduction target, not an import.
The separate continuation is
`2026-11-19-mellin-lower-power-first-mode-reproduction-1633.md`.
Its new ready assessment receives separate next-turn approval before
mathematics. No lemma, mathematical script, DAG or PROOF changed.
