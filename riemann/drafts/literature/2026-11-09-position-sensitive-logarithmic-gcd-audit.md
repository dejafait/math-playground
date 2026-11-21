# Separate audit nomination for the position-sensitive logarithmic gcd bound

TARGET: Independently audit L925's bound F_(log N)(c)>=-C_* Q(c), checking the same-index weighted Hermitian rows, transpose orientation, factor two, similarity versus quadratic forms, kappa, complex vectors and every real cutoff.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the unchanged exact-form searches and theorem comparisons in the November9 position-sensitive-coercivity, row-sum and critical-coercivity assessments; step232 narrowly checked the logarithmic-gcd notes, histories and preserved dyadic-pilot stop. No new browsing or originality claim.
SOURCE_EVIDENCE: Step233 directly confirmed Leitner CO-MAT2 WS2013/14 Section1.1.1 Theorem1.1.3 printed p2 (sixth PDF page) and preceding similarity statement, and Bindel CS6210 2025-11-03 Hermitian spectral/Rayleigh sections and weighted-average argument; reuse Tao Notes1 Section2 Theorem13 eq(22) through audited L924 (4)-(7). Exact URLs and inspection details below.
COMPARISON: The target audits the same finite arithmetic inequality authorized before step232. Existing source coverage includes the full matrix-theorem hypotheses and L924's scalar input; no new coefficient threshold, analytic theorem or source interface is proposed.
GAP: L925 now contains a complete specialization, but its weighted transpose and same-index combination have no separate audit yet. This nomination does not certify that proof or establish conditioning, moments, realization or signs.
REASON: Step233 separately approves the unchanged exact audit target after primary-source confirmation and reuse of the prior comparisons. The mathematical audit is not performed; next turn defaults to the saved finite audit.
SCOPE: All N>=2, arbitrary finite complex c, natural logarithms, the unchanged full F_A and Q, both cross terms, kappa, c=0, finite inversion, and all real/empty cutoffs. No new source is essential unless the audit uncovers a changed hypothesis.

## Reused evidence and exact audit boundary

The invocation-start ready assessment is
drafts/literature/2026-11-09-logarithmic-gcd-position-sensitive-coercivity.md.
It records the exact searches, duplicates, prior failures and complete
relevant primary-source inspections. Reuse it unchanged; this nomination
does not perform another literature campaign or infer novelty.

The imported matrix statements are Leitner,
[Theorem1.1.3 and preceding similarity statement](https://www.csc.univie.ac.at/files/Numerik_WS13-14/Lecture_Notes2.pdf),
WS2013/14, printed p2 (PDF p6), and Bindel,
[Hermitian eigenvalue basics / Variational approaches](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-11-03.html),
3 November2025. The scalar input is Tao,
[Section2 Theorem13, equation(22)](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/),
23 November2014, with its all-real-cutoff specialization already proved
and audited in L924. Their statements are imported, not reproved.
The earlier gcd-spectrum and logarithmic-gcd-kernel scope comparisons
remain unchanged. No unread lead is a premise.

Audit the canonical proof in
lemmas/L925-position-sensitive-logarithmic-gcd-lower-bound.md.
Essential local inputs are L737 (5)-(11)/step261 and L924 (4)-(7)/step230.
Only their finite identities and scalar bounds are used; no Hardy,
height, bump, moment or multiplier-length premise is imported.

Check H=K+K*, its zero diagonal and entrywise nonnegativity; recompute
the outgoing and incoming weights at a fixed d. Verify that the latter
is exactly log d, that the former retains log(N/d)+C_*, and that the
same d is used before taking any global bound. Check the diagonal
similarity orientation D^(-1)HD and that the Rayleigh theorem is applied
to H, not to its generally non-Hermitian similar matrix. Retain the
factor two from the full complex cross term and kappa until its
nonnegativity is used. Include the zero column, empty rows, c=0 and
finite inversion; do not upgrade Q>0 into a uniform condition number.

Continue if the proof yields the one absolute C_*=M+3 log2+2 for every
N and c. Otherwise identify the failing equality, theorem hypothesis
or bound and repair or withdraw only the unsupported claim. Finite
positive trial quotients are not audit evidence. The parked pilot is
not reopened. Full matching Mathlib coverage remains unchecked.

This is proof_audit/routine_audit, standard/high: a finite application
of inspected named theorems, with precise orientation and factor checks.
It is neither a creative central mechanism nor a candidate RH audit.
Conditioning, moments, actual-theta contact flux, realization and signed
transfer remain independent gaps. No cross-notebook input is proposed.

## Separate source approval — step233, 9 November 2026

LITERATURE_REASON: The invocation explicitly requires a separate approval
of step232's newly written audit assessment. This is a narrow source-scope
confirmation, not another search for a stronger theorem.

Reused the position-sensitive-coercivity assessment's exact searches,
stronger-result comparisons and inspected-versus-unread distinctions,
the row-sum review's Mertens coverage, and the critical-bound audit
assessment's source-access repair. Read L925's hypotheses/conclusion
to match the contract, step230/232 histories and the preserved step226
pilot failure. No expanded search, certificate replay or originality
claim is needed for this unchanged target. Positive pilot quotients
remain irrelevant to an all-vector lower bound.

Reopened both linked primary matrix sources. Leitner's printed p2
(sixth PDF page, zero-based page5) states similarity invariance and
Theorem1.1.3 for arbitrary finite complex square matrices. Read its
complete maximal-component proof, including the nonzero component
and closed-disk conclusion. No Hermitian or irreducibility hypothesis
is imposed. Bindel's Symmetric eigenvalue basics and Variational
approaches state the Hermitian hypothesis, unitary decomposition and
complete Rayleigh weighted-average argument for complex nonzero
vectors; repeated eigenvalues are allowed. Only these passages are
imported, not the later generalized or interlacing results. Their
hypotheses agree with the proposed audit's source contract.

The arithmetic applicability is still the next mathematical task.
Similarity supplies spectral invariance, not invariance of Euclidean
quadratic forms; the audit must use Rayleigh on the original Hermitian
matrix. Verify the actual weights, factor two, common absolute constant,
kappa, complex vectors, zero vector, finite inversion and all real/empty
cutoffs in L925 using L737 and audited L924. No such calculation or
independent proof verification was performed here.

SPECIALIZE is now separately approved for exactly TARGET, with no
changed threshold or new lemma input. Continue only if the full replay
supports one C_* for every N,c; otherwise isolate and repair or withdraw
the precise unsupported claim. Conditioning, moment errors, realization,
signed transfer and actual-Xi mixed positivity remain open. Full matching
Mathlib coverage remains unchecked. No cross-notebook input.

Outcome: LITERATURE / STALLED / NOVELTY_UNCHECKED. This approval
confirms existing coverage without mathematical progress or an
exploration/recovery-counter reset. No lemma, script, DAG or PROOF
change. A new central creative target remains unjustified without a
concrete actual-theta/signed-realization input; the essential pending
audit is not relabeled creative.
