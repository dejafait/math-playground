# Large repeated-message fiber — completed source comparison

TARGET: Test whether a single quadratic message attained at more than 272 auxiliary points forces full-sheet constancy in the pinned L030 model over E or F.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the prior narrow duplicate search and external exact/terminology searches for quadratic-message equality fibers, finite-plane stopping sets, blocking numbers and line percolation; no inspected theorem matches the saved target. Queries, inspected statements and unread leads are distinguished below; failed searches imply no novelty claim.
SOURCE_EVIDENCE: Read Conrad, Counting Roots of Polynomials, Theorem 1 and Lemma 2 with complete proofs, pp. 1–2; Brouwer–Schrijver, JCTA 24 (1978), unnamed theorem and complete proof, pp. 251–252; Gerbner et al., arXiv:1608.00531v1, model pp. 2–4 and Propositions 12–13 with every proof case, p. 10. Direct links and versions below.
COMPARISON: The root theorem covers nonzero univariate differences over either coefficient field; the blocking theorem requires meeting every auxiliary hyperplane, and projective line percolation uses all lines and a different update rule. Neither supplies the 272 implication under the pinned hypotheses. This is equality-fiber propagation, not the stopped auxiliary-line rank or translation test.
GAP: Essential bounded source comparison is complete; the entire large-fiber implication remains unproved. A separate mathematical attempt must justify every propagation/counting step or produce a permitted complete counterassignment. No matching theorem or certified sharp cutoff was found in the inspected sources.
REASON: Permit one bounded attempt on the unchanged target using the named root theorem as a standard input. A positive result could isolate the high-multiplicity regime without settling the small-fiber, retention or RS-transfer gaps; the source review itself proves no propagation statement.
SCOPE: Exactly TARGET: q=137,T={16,64,70,102,112,118,121}, arbitrary permitted C,sigma, K=E or F and every full-sheet equation of L138; repetitions and extra incidences retained, no coefficient translation action, injectivity or coefficient-span restriction. Any weaker span-three-only conclusion must be labeled as such. No reopening of ATTEMPTS/109–114 is approved.

## Relevance and bounded test

The main gap remains arbitrary-center 67/68 safety, with bracket 955–957.
Inputs are L030's label setup and the restated full-sheet hypotheses of
L138, not L138's unproved translation inclusion. For a message g, the
proposed fiber is exactly {P in F_137^2 : g_P=g}. It is not the image of
one auxiliary line. The number 272 is a proposed research cutoff, not
a proved cap, a sharpness assertion or a citation.

The bounded comparison below supplies an EXPLORE assessment, not a
correctness decision. Standard root counting should be imported by
citation; there is no reason to reprove it. The missing implication
is specific to the full-sheet equations and arbitrary labels. No
additional general incidence-source browsing is needed for this target.

After approval, the bounded mathematical test would be either a complete
proof with all label and extension-field qualifications, or a permitted
full-sheet counterassignment with this large fiber. A partial patch is
not a counterexample. Stop an inconclusive attempt after recording the
precise missing propagation implication. A positive result would isolate
the small-fiber regime, not force such a large fiber to exist and not
repair the inadequate general incidence threshold. No new calculation
budget is spent in preparing this gate; prior stops are preserved.

There is no cross-notebook input. This completes the separate source
comparison requested by the invocation-start REVIEW_REQUIRED gate;
no mathematical attempt, lemma edit or mathematical script occurred.

LITERATURE_REASON: The saved target lacked external theorem-level comparison at invocation start. This review fills that coverage rather than repeating the ready module or general-incidence assessments.

## Exact hypotheses retained

Use L030's labeling setup as restated in L138: E=F_65537,
F=F_(65537^28), H=<19139> of order 1024, an arbitrary 61-subset C
of H, and a bijection sigma from (T times F_137) disjoint union four
dummies onto H minus C. All x_(t,y)=sigma(t,y) are distinct. Over
K=E or F there is a quadratic g_P for every P=(u,v) in F_137^2,
with g_P(x_(t,y))=d_(t,y) whenever u+tv=y. No polynomial dependence
of the coefficients on u,v is assumed. In particular a multivariate
degree bound in the auxiliary coordinates is unavailable. The two
fields of indices and values must not be identified.

## Search record and prior failures

In addition to the supplied duplicate search, searched the cone and
characteristic-rank assessments, coefficient-closure assessment and
span-three working record for blocking/percolation, equal-message,
272/274 and large-fiber claims; no match was returned. Read the full
short failure records ATTEMPTS/109–113 and the relevant L138 hypotheses.
The one-point rank-two patch in ATTEMPTS/110 is incomplete, and the
small equality classes of ATTEMPTS/111 are not a large-fiber test.
ATTEMPTS/112's search is exhausted; ATTEMPTS/113 leaves translation
membership unresolved. The completed general-incidence comparison
is reused for ATTEMPTS/114; its bounds are not being recalculated.

External queries included `"affine plane" "bootstrap percolation"`,
`"finite plane" "stopping sets" Reed Solomon`,
`"nets" "stopping sets" "Latin" codes`,
`"Brouwer" "Schrijver" "blocking number" pdf`,
`"line percolation" "finite projective planes"`,
`"quadratic" "equal" "messages" "affine plane"`,
`"seven directions" "percolation"`,
`"partial net" "closure" "percolation"`,
`"272" "137" "propagation" polynomial`, and
`"large fibre" "polynomial" "agreement"` (2026-10-29).
Root-bound searches located the author-hosted proof below and the
Stacks Project Fields §9.17, tag 09HW, whose introductory root-bound
statement was inspected. Irrelevant search hits were not treated as
evidence. The search is bounded, not exhaustive.

## Primary inputs and comparisons

**Polynomial roots.** Keith Conrad, *Counting Roots of Polynomials*,
[author-hosted two-page note](https://kconrad.math.uconn.edu/blurbs/ringtheory/countroots.pdf),
undated version retrieved 2026-10-29, Theorem 1 and Lemma 2, pp. 1–2.
The theorem bounds the distinct roots of a nonconstant degree-d
polynomial over any field by d. Read the factor lemma and induction,
including the no-root case and the removal of a chosen linear factor.
For later use, check the zero difference separately; a nonzero constant
also needs its elementary zero-root case. The source applies to both
K fields directly. It places no bound on the number of auxiliary points
carrying the zero difference. Any conversion from labels to auxiliary
propagation remains an obligation of the later attempt, not a theorem
imported here. No reproof is justified.

**Affine blocking.** A. E. Brouwer and A. Schrijver, *The Blocking
Number of an Affine Space*, J. Combin. Theory Ser. A 24 (1978),
251–253, DOI 10.1016/0097-3165(78)90013-4,
[primary journal scan](https://ir.cwi.nl/pub/9858/9858D.pdf), unnamed
theorem p. 251, proof pp. 251–252. Its minimum for a set intersecting
every hyperplane of AG(k,q) is k(q−1)+1; for k=2,q=137 this is 273.
Read the upper construction and lower polynomial argument, including
the nonzero value at the origin after coordinate reduction. This
requires meeting all hyperplanes. A lower bound on a blocking set
does not say that every set of that size is blocking. The full-sheet
hypotheses do not assert that the equality fiber blocks all affine
lines. The numerical proximity to 272 therefore supplies no import.
No blocking premise or converse is proved here.

**Line percolation.** D. Gerbner, B. Keszegh, G. Mészáros, B. Patkós
and M. Vizer, *Line Percolation in Finite Projective Planes*,
[arXiv:1608.00531v1](https://arxiv.org/pdf/1608.00531v1), retrieved
2026-10-29 (v1 identifier; PDF title dated November 7, 2018).
Read the update definition pp. 2–3, projective incidence/duality
and Propositions 2–4 pp. 4–5, and Propositions 12–13 with proofs
p. 10. A line becomes entirely infected after r of its points are
infected. For all projective lines Proposition 13 gives maximum
nonpercolating size q(r−1)+1 when r<q/2+2 (275 at q=137,r=3).
Its proof distinguishes zero, one, and at least two infected lines
through infected points; Proposition 12 also uses an uninfected point.
The notebook has seven affine parallel classes and quadratic
evaluation constraints, not the stated update rule. Neither dualizing
nor deleting lines automatically transfers this extremal theorem.
This source does not establish the target cutoff.

## Unread leads and scope decision

Brouwer–Schrijver's introduction reports Jamison's stronger coset-cover
theorem and cites *Covering finite fields with cosets of subspaces*,
JCTA 22 (1977), 253–266. That original paper was not read and is not
an imported input. Its reported covering hypothesis is not supplied
by a fiber cardinality premise. Xia–Hu, *On the Stopping Sets of
Finite Plane LDPC Codes* (2007), was seen only at the publisher's
abstract; no theorem-level claim from it is used. Ordinary stopping-set
terminology alone does not identify the quadratic full-sheet system.
Neither lead is essential to the bounded attempt approved here.
If a future argument actually requires either theorem or a changed
propagation model, its coverage must be separately assessed.

EXPLORE records no adequate match in this bounded comparison, not
novelty. The proposed mathematical mechanism is direct propagation
from an equality class using all seven classes; it must not silently
assume translation invariance, faithful nets, auxiliary degree bounds,
or a full projective-plane update. Accept only a complete proof under
the stated hypotheses, or a fully verified full-sheet counterassignment
with a fiber larger than 272. Otherwise save the precise missing
implication and stop this bounded attempt. A combinatorial patch alone
cannot refute the implication. Mathlib matching and supporting coverage
was not checked in this review. The exact RS target, 955–957 bracket,
and all independent unresolved assumptions are unchanged.
