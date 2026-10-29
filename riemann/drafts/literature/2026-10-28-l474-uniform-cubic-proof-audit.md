# L474: uniform cubic application audit

TARGET: Critically audit L474's uniform cubic small-displacement pair-mass bound, replaying multiplicity suppression, gamma normalization, combined pole cancellation and clipped endpoints with common C,T_0 for all 0<epsilon<=1.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed exact/stronger-result and failure comparison in 2026-10-28-l474-critical-audit-coverage.md and its named prior assessments; no new target, theorem discovery or novelty claim.
SOURCE_EVIDENCE: Broughan II (2017), Theorem 3.3 proof (1),(4), pp. 26--27, https://api.pageplace.de/preview/DT0400.9781108195430_A31720577/preview-9781108195430_A31720577.pdf#page=48; Bettin arXiv:1111.0925v1 Theorem 1 p. 2/small-shift proof pp. 9--10, https://arxiv.org/pdf/1111.0925v1#page=2; DLMF 5.11.2/5.11(ii), https://dlmf.nist.gov/5.11; L018, L465 Sections 1--2 and L471 definitions. Precise inspected scope and limitations are in the completed comparison.
COMPARISON: Sources cover the supporting tools with the required multiplicities and bounded microscopic shifts; L474's summed quotient bound is an application requiring independent replay, not a quoted source theorem.
GAP: Verify or repair L474 (1)--(12), especially the y-anchored chi remainder, one-pair division, uniform cluster suppression and TL^2 disk-area cost; no verdict on these application claims is yet established.
REASON: The new partial bound needs a separate conceptual audit before extension. This ready assessment awaits next-turn approval and does not itself audit the proof.
SCOPE: Exact L474 (1), with no RH, simplicity, separation, lower displacement bound, zero-count input or external half-plane premise; the complementary sector and full L471 little-o target are excluded.

Import the cited tools with their exact hypotheses. Replay all of L474,
not merely the listed critical equations, checking its complete local
normalizations and domains against the named inputs. Keep full proof
and any repair in its canonical lemma file. Distinguish an application
audit from an independent audit of Bettin's arithmetic proof or the
unused infinite-factorization theorem. Unknown Mathlib coverage is
unchanged.

Pass requires the same absolute C,T_0 for all real T>=T_0 and every
0<epsilon<=1. Test repeated roots after removing just one pair, an
unremoved real central zero, arbitrarily close centers, empty sectors,
singleton clipped windows and both dyadic endpoints. A lost logarithm,
epsilon-dependent constant or hidden occupancy hypothesis requires
explicit repair or narrowing. Preserve old reasoning and failure
evidence. A passing audit alone adds no complementary mass saving,
individual sign or RH conclusion.

Essential input IDs: L474, L018, L465, L471. L471's ordinary-moment
stop and L473's finite-law stop are contrasts only, not mathematical
premises. No cross-notebook input. A changed target outside this scope
requires REVIEW_REQUIRED rather than immediate research.
