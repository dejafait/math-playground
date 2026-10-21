# Alternative product plane maximum — critical audit source scope approved

TARGET: Critically audit L072's attained positive maximum for L071's unchanged product pairing on the full scalar-admissible zero plane.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L072's full statement/proof, L071's hypotheses and conclusion, ATTEMPTS/054, history/248 and the ready calculation and L071-audit assessments; searched the exact L072 and implementation-failure records. Reused the existing primary-source assessment rather than repeating its external searches.
SOURCE_EVIDENCE: Reuse drafts/literature/2026-10-16-alternative-product-dual-zero-plane.md and foundations/04,09,10,12: Schrijver Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64)–(65); Sano Corollary 2.2, Theorem 2.6 and Lemma 2.7; Polak v1 Sections 1.1–1.2; Boyd–Vandenberghe author slides 4.18 and 5.19–5.20. Read the local source records' hypotheses and singular/unequal-layer qualifications; no primary source was newly retrieved this turn.
COMPARISON: The audit stays within the previously assessed real finite matrix and polyhedral quadratic scope. Singular PSD Hessians are allowed; L072 claims a global square identity and an explicit feasible attaining point, so no strict concavity, compactness, Slater converse or attainment theorem is needed. Those instance-specific claims and the two implementation corrections remain unverified by this review.
GAP: Independently verify L072's exact square, full scalar domain, original ranges/normalization/cancellations and attained point, including both preserved initial failures. Sources cover the tools but do not certify these coefficients or the finite maximum.
REASON: The newly proposed audit scope is now compared with adequate reusable coverage; no changed theorem hypothesis or essential unread source prevents the later critical audit.
LITERATURE_REASON: The supervisor requires separate approval of this newly proposed critical-audit continuation; the review checks rank-one curvature, attainment and correction scope against ready coverage without redoing the completed calculation.
SCOPE: Exactly L072's full scalar-admissible w=w_star plane and L071's unchanged product weights, original rho,p7,pairs through p13, L065 RREF, 36 v-scaled variables, 28 forced entries, unordered presentations, 64 singular ranges and full anchor correction. Critical audit and repairs within this statement only; no new dual or simultaneous-completion search.

## Relevance and bounded audit

The main gap remains arbitrary-center safety at 67/68 agreements, with
955–957 the unchanged grid bracket. The intermediate target is to retain
or concretely correct L072's finite maximum statement. If retained, it
justifies parking strict exclusion of this plane by these exact weights
and directs later work toward a separately assessed completion or other
dual. It does not establish that such a continuation is feasible.

Essential inputs are L061,L062,L065,L067,L068,L069,L071,L072 and
foundations/04,09,10,12. Their ancestral results are imported inputs,
not independently reverified in this literature turn. Continue if the
complete independent audit retains the exact polynomial identity, the
actual feasible attaining point and the original matrix translation.
A failed identity, range, domain row or lookup correction requires a
specific repair or rejection of that claim; successful prior scripts
alone do not settle the audit. No research calculation was run here.

## Precise reusable source coverage

Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE TIT 51 (2005), 2859–2866,
DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Proposition 5 (44)–(47), Theorem 1 (51), III.A (52)–(59), III.B
(64)–(65), printed pp.5–7. The assessed tensor decomposition includes
unequal layers and positive binomial rescaling. Factors 68 and 956 and
layers 0,5,6,7 are in range. The old source record's displayed application
mentions layers through 6; the ready plane assessment explicitly covers
7 as well. No theorem change is involved. The actual finite dictionary,
signed rectangular normalization and source-to-mode translation remain
audit obligations, including repeated words and forbidden entries.

Takashi Sano, *Moore-Penrose inverse, generalized Schur complement and
inertia*, version of record 27 February 2026,
[Section 2](https://link.springer.com/article/10.1007/s44146-026-00231-y),
Corollary 2.2, Theorem 2.6 and Lemma 2.7. For finite Hermitian
[A,B;B*,C], positivity is equivalent to C PSD, ker(C) contained in
ker(B), and A-B C^dagger B* PSD. The prior assessment inspected both
the square-root necessity and triangular-congruence sufficiency cases.
Finite-dimensional ranges are closed; inverse action on the range is
covered. All real symmetric blocks here qualify, conditional on checking
every original range and the actual orbit-weight normalization. A
varying cross vector does not license dropping singular cases.

Sven C. Polak, *Semidefinite Programming Bounds for Constant-Weight
Codes*, [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1),
15 March 2017, Section 1.1 (1)–(3), Proposition 1.1 and indicator
proof, p.2; Section 1.2, p.3. Reuse foundations/12's constant-weight
qualification at n=1024,d=10,w=68. Averaging is available only when
it preserves this ordinary unlabeled slice. This is not an assertion
of a representing measure, labeled symmetry or RS realization.

Stephen Boyd and Lieven Vandenberghe, with Parth Nobel, *Convex
Optimization*, revised 402-page
[author slides](https://web.stanford.edu/~boyd/cvxbook/bv_cvxslides.pdf),
PDF pp.53–54,97–98,105,174–175; slide 4.18 and slides 5.19–5.20.
The ready assessment inspected convexity and the complete KKT sufficiency
argument: singular PSD Hessians and boundary points are allowed, without
Slater for sufficiency. L072 instead claims the stronger directly
checkable identity Phi=V-alpha*(v-v_dagger)^2, alpha>0, for every real
(u,v). The later audit must verify it, rather than assuming curvature
from the source. With an actually feasible point attaining V, the claimed
maximum needs neither boundedness of the domain nor a KKT converse.
The inaccessible book PDF remains an unread nonessential lead; the
inspected slides already cover the optimization hypotheses.

These are known tools imported by citation, not general results needing
reproof. Their finite specialization is the reason for SPECIALIZE rather
than IMPORT. No source checked supplies this prescribed maximum; no
novelty follows. Full matching and supporting Mathlib coverage remains
not checked, which is not evidence of absence.

## Duplicates, failures and complete audit obligations

The inspected records distinguish L067's immutable-column exclusion,
L068's old-weight zero, L069's scalar pass, and L071's different-weight
fixed-point exclusion from L072's plane maximum. ATTEMPTS/054 stops only
the unchanged alternative weights. No completed separate L072 critical
audit appears in the inspected step-248 records. This is an audit of
existing work, not a new lemma or a repeated exclusion calculation.

The audit must preserve positive rho,p7, original RREF coordinates and
exact w_star; reconstruct all 270 types/1620 presentations and every
forced entry; and check all 64 singular ranges, the weighted energy,
full transported anchor term and every original/raw cancellation on all
36 free variables. Independently establish the quadratic coefficients,
null u direction, exact square and maximum interval before accepting
attainment. Check the attaining point against all 49 nonnegativity rows,
1530 column rows through p13, 2178 unchanged rows and 49 original
weighted kernel residuals. Newly untested seven/seven scalar upper rows
are outside this claimed domain and cannot be silently inferred.

Inspect the complete relevant evidence in both final certificates and
the preserved initial reports named in L072. The false strict-concavity
expectation must be reconciled with rank-one curvature. The 268 initial
lookup-check failures require checking which presentations lie outside
the retained layers, and that every available prescribed lookup and
all unordered full-key identifications are still tested. An unavailable
lookup cannot excuse disagreement with an available one. This review
approves that investigation without accepting either implementation fix.

A positive pairing disproves strict exclusion by these weights only.
It supplies neither simultaneous PSD completion at the maximizer nor
an obstruction there, no global consistency or measure, and no RS list
or sharp safety bound. Those independent gaps remain unresolved.
