# Cyclic kernel restriction — audit source coverage

TARGET: Critically audit L088's cyclic-family rank-two and one-dimensional-kernel restrictions.
CHECKED: 2026-10-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused step 220's documented exact-ruler and fixed-evaluation exterior-kernel searches; read full L088, the relevant L010/L027/L087 proof ranges and ATTEMPTS/020,029,031 for this separate audit-scope comparison; no fresh external search.
SOURCE_EVIDENCE: Conrad Exterior Powers Theorem 4.2, Theorems 5.1/5.4 and Corollary 5.9 as inspected in step 220, plus L010's Vandermonde independence, L027's full-exterior quotient equivalence and audited L087's cyclic incidence, cover the audit's external machinery.
COMPARISON: The known machinery supports checking L088, not importing its conclusion; the new cyclic incidence, alternating-image and common-factor arguments remain local proof obligations, with no plane-family conclusion or actual-error hypothesis available.
GAP: Independent critical checking of L088 remains; even a passing audit leaves rank 27 versus 28, realization, arbitrary-family coverage and the challenge qualifications unresolved.
REASON: Essential coverage is ready for exactly the stated separate proof audit; no essential unread source or matching imported cyclic-kernel theorem was identified, and correctness and originality are not certified here.
SCOPE: Full canonical L088 under its fixed F/H and arbitrary bijection hypotheses, using only the stated portions of L010/L027/L087 and the inspected exterior machinery; no rank search or new realization claim.

## Proposed scope, not a completed assessment

Read the full canonical L088 and its essential inputs L010's
eight-column independence, L027's quotient interpretation and L087's
cyclic incidence. Reuse the ready source comparison
`drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`;
its approval was for the mathematical attempt, not this new audit.
Do not import a plane restriction or a different family's rank proof.

The new proof's load-bearing cases are: the alternating-image reduction
without ambient nondegeneracy; connectivity with all zero projections
retained; the eight-row disjoint-containing-block certificate and its
coverage of every pair; the translated triangle count with up to four
zero projections; complementary quotient images for disjoint blocks;
and the two-independent-tensors argument including the common factor
proportional to the exceptional column. Check signs only to the extent
needed by contraction rank and the quotient equivalence, retaining the
unshifted moment convention throughout. Check the rational-kernel
corollary separately from any claim about an original affine chart.

Passing this audit would validate only the stated restriction. Uniform
zero kernel, existence of any rank-27 labeling, full-weight realizability,
the global sixteen-count exclusion and challenge qualifications all
remain unresolved. No actual-error hypothesis may be used to remove
kernel vectors in this audit. No numerical sample or source snippet
can replace the uniform proof. Matching Mathlib coverage is not checked.

Approval criterion for the separate source turn: existing primary
exterior-algebra coverage and local proofs suffice for this exact scope,
or identify a specific essential unread result before dependent work.
Do not repeat generic-MDS browsing or reopen stopped rank sampling.

## Completed source comparison — step 222

The proposal above is retained as the audit specification. This separate
literature-only turn approves its scope, without executing the critical
audit or endorsing L088's proof. The exact TARGET is unchanged.
LITERATURE_REASON: The newly written L088 audit scope required separate
approval; this comparison reuses ready coverage instead of repeating
external searches on the already covered mathematical attempt.

The main gap is exclusion of sixteen actual errors, with the certified
model's interval still 11/q–16/q. The intermediate target is a critical
audit of the rank-two and at-most-one-dimensional restriction in L088.
A passing audit would make that restriction usable in a later uniform
rank-28 obstruction or independently certified rank-27 test. Neither
test, nor an actual-error applicability argument, is undertaken here.

Reuse the full theorem-level comparison and source version notes in
`drafts/literature/2026-10-14-cyclic-family-alternating-kernel.md`.
In particular Keith Conrad, *Exterior Powers*, undated author-hosted
47-page PDF, inspected October 14, 2026, Theorem 4.2 (printed pp. 11–12),
Theorem 5.1 (pp. 15–16), Theorem 5.4 (p. 17) and Corollary 5.9 (p. 18),
[primary source](https://kconrad.math.uconn.edu/blurbs/linmultialg/extmod.pdf),
provide bases, induced maps/composition, preservation of isomorphisms
and surjections, and preservation of injections over fields. L088 uses
finite-dimensional vector spaces over F_(97^20), so these hypotheses
match. Their inspected proof coverage is retained from step 220; no
new retrieval or reproof is necessary. They do not prove the common
kernel restriction, the alternating-image reduction or cyclic incidence.
The latter are precisely written local arguments to audit, rather than
missing assertions assigned to an unread external theorem.

Read the complete canonical L088 to identify those obligations. Read
L010's hypotheses and proof opening (eight shifted moment columns form
a Vandermonde matrix times a nonzero diagonal), L027's polynomial-
constraint/quotient-map section and its audited pairing convention,
and L087's hypotheses, conclusion and analytic incidence proof. These
are narrower inputs than the full equality or family-exclusion results.
The independence statement is independent of L010's bad-event and
locator assumptions: its determinant argument uses only distinct
nonzero labels. The scalar change from (h,...,h^8) to (1,...,h^7)
preserves each column span. L027 supplies the quotient interpretation
on the entire exterior square, not its other family's residual basis
or rank conclusion. L087 supplies incidence only. Its comparison to
L072 and supplementary finite certificate are not needed to audit
the explicitly written cyclic incidence cases in L088. No additional
transitive proof load is essential for this restricted input use.

The reused source comparison already rejects generic/selectable-
evaluation GM-MDS results as a theorem about every fixed H-labeling.
L027/L029's other support patterns are not duplicates of L088, and
L073–L079's plane restrictions remain unavailable. No novelty inference
is made from the absence of an inspected matching theorem. Full Mathlib
coverage is not checked; it is not an audit prerequisite.

Read the three recorded failures in full. ATTEMPTS/020 stops positive
rank sampling, ATTEMPTS/029 excludes anchors for one saved assignment,
and ATTEMPTS/031 stops abstract uniqueness. None supplies a defect in,
or a ban on auditing, L088's independently specified analytic restriction.
No census, sample sweep or cross-notebook input is proposed.

Continuation/abandonment test: independently check every displayed
incidence row and its pair coverage, all zero-projection branches,
the alternating-image reduction, the exceptional common factor, and
the rational-kernel corollary under the exact hypotheses. Pass only
if every essential implication is justified; otherwise record the
first exact defect and which conclusion it affects, preserving the
rest of the work. Passing validates only L088's restriction. It cannot
close rank 27, infer a rational original chart or create full errors.
This source review derived no new lemma, modified no lemma or
mathematical script, and used zero mathematical exploration turns.
