# Proposed reanchored principal test for the fixed released-zero witness

TARGET: Test whether L056's fixed shell witness satisfies every reanchored three-index conditioned principal matrix on its represented triples.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 185 compared foundations/09,12, L053 and L056 entry definitions, ATTEMPTS/035–038 and the approved free-triple assessment; searched constant weight codes fixed triple moments reanchored principal matrices Polak semidefinite 1024 68. No inspected source gives a verdict for these fixed coefficients.
SOURCE_EVIDENCE: Reused foundations/09,12 and freshly inspected Polak arXiv:1703.05171v1 Section 1.1 (1)–(3), Proposition 1.1 and complete proof, p. 2; Brouwer–Haemers author preprint Theorem 2.7.1(i), p. 36 and Lemma 2.9.1 with proof, p. 37. L053 supplies existing three-index and Boolean normalizations.
COMPARISON: L056 verifies its anchor and represented unordered-orbit equality; it explicitly omits PSD when a different support is the anchor of a principal matrix. L053 checks such small matrices for a different triple assignment, so it does not decide this target.
GAP: Evaluate the unchanged L056 triple coefficients in the existing L053 three-index normalization at every represented orbit and each of its three anchors, retaining Boolean repetitions; neither feasibility nor failure is established here.
REASON: Known union-matrix and nonsingular-leading-block Schur tools cover the necessary tests, but do not decide this fixed assignment; exact application is needed without reproving these tools.
SCOPE: Only L056 represented triple orbits at fixed L053 rho,p_i, all three singleton anchors and Boolean repetitions; unchanged 21 coefficients, forbidden-distance zeros and no optimization, off-shell completion or actual-label constraints.
LITERATURE_REASON: The changed other-anchor PSD scope was omitted by the shell-only assessment; this separate approval resolves that essential source-scope question.

Main gap: 68-agreement arbitrary-center safety remains unresolved,
independently of 67-agreement safety. This independently testable target
asks whether the now audited shell witness survives necessary small
principal matrices at the other anchors. Its plausible use is to decide
whether this specific shell optimizer is worth extending to larger
coupled matrices, or requires changing before such work.

Essential inputs: L053's fixed rho,p_i and union-index convention;
L054's eight-region dictionary; L056's exact d_rq and represented
unordered-orbit consistency, including its step-184 critical audit.
Use the unchanged 21 coefficients. For each represented distinct triple
and each support D chosen as anchor, retain just the union indices
{D}, {D,E}, {D,F}, with pair and triple entries fixed by those inputs.
Retain the repeated-pair case by Boolean normalization. No coefficient
optimization, new zero prescription or other moment assignment is in
this proposed target. It differs from repeating L056's same anchored
shell: when r+q differs from five, the other anchors have one neighbor
outside their distance-five shell.

Source coverage is now approved for a subsequent research turn to inspect all such exact small matrices.
A failed principal minor stops this fixed witness as a global extension
candidate, requiring changed coefficients; it does not exclude every
shell-feasible assignment. If every matrix passes, park only this
necessary test and retain the unresolved larger cross-shell PSD and
global extension conditions. Preserve ATTEMPTS/035–038 and the audited
shell optimum. No test of these additional matrices was performed in
step 184 or this literature turn. Approval covers only the stated fixed-witness test.

Other-anchor full PSD, cross-shell consistency, actual-label zeros,
the full SDP value, useful uniform bounds, representing measures and
common-center RS realization remain unproved. No outcome alone changes
the 955–957 boundary. Full matching Mathlib coverage is not checked.


## Source comparison completed in step 185

Polak, *Semidefinite Programming Bounds for Constant-Weight Codes*,
IEEE Trans. Inform. Theory 65 (2019), 28–38,
DOI 10.1109/TIT.2018.2854800, inspected
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Section 1.1 (1)–(3), Proposition 1.1 and complete proof,
printed p. 2, provides union matrices for every conditioning family.
At order three, singleton conditioning admits the three proposed indices.
The indicator proof gives necessary PSD for constant-weight codes;
its displayed A(n,d) endpoint must retain the A(n,d,w) qualification
from the proof. The following paragraph includes nonnegative
lower-cardinality diagonals. These requirements concern all anchors,
not just anchors with two distance-five neighbors. This imports the
known constraint; it supplies no feasibility verdict for L056.

Brouwer–Haemers, *Spectra of Graphs*, Springer (2012),
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Theorem 2.7.1(i), printed p. 36, gives the invertible triangular
Schur congruence. Lemma 2.9.1 and complete proof, p. 37, identify PSD
with nonnegative quadratic forms/eigenvalues. Real symmetry and
nonsingularity of the leading block are required; the existing L053
normalization has positive leading entry one. No lower-block inverse
or positive-definiteness assumption on that block is allowed. Zero
pivots must remain included. These source facts are imported, not reproved.

Reuse L053's canonical normalized matrix and Boolean cases in its
“Orbit scope and Boolean coordinates” and “Complete retained principal
PSD” sections. For distinct triples, substitute the L056 triple moment
and the appropriate unchanged pair moments; changing anchors does not
change the unordered triple coordinate. L056's full-region consistency
already justifies that coordinate on represented orbits. The later test
must explicitly permute full regions and regenerate pair distances,
including an anchor with a neighbor outside its distance-five shell.
No new formula or determinant sign has been established in this review.
Repeated supports use lower-order moments and duplicate-index removal
as in L053, rather than the distinct-triple recipe. Test all represented
relations, including forbidden-distance zero cases, not only the 21
free coefficients. Exact principal minors or a complete exact Schur
certificate must cover singular cases.

The targeted query above returned the primary Polak paper and related
constant-weight SDP sources, not an exact fixed-coefficient answer.
The new work is therefore a finite specialization of known tools, with
REPRODUCTION appropriate; a search miss establishes no novelty. Reuse
of the inspected primary inputs is sufficient: no essential unread
source was identified. The stronger full programs do not themselves
answer whether this partial assignment passes the selected tests.

ATTEMPTS/035 concerns L053's different triple recipe; /036 excludes its
full shell; /037 retains an extra incidence zero; /038 stops shell-only
exclusion after releasing that zero. None records this other-anchor
verdict. The approved free-triple scope in
`drafts/literature/2026-10-12-free-triple-five-shell-feasibility.md`
already explains small principals outside a shell, but retains a
trial-zero hypothesis absent here. Its theorem coverage is reused,
not its mathematical conclusion or that hypothesis.

Continuation test: any negative principal minor rejects only L056's
fixed assignment as a global PSD extension candidate. A complete pass
justifies considering larger coupled matrices, while leaving all
unrepresented triples and full other-anchor matrices unverified.
Even a pass supplies no labeled feasible point: L056 released the
entire incidence zero and has not checked the actual-label nonfaces.
There is no uniform bound, representing measure, RS realization or
improvement to the 955–957 bracket. Full matching Mathlib coverage
remains not checked, as in the canonical inputs.
