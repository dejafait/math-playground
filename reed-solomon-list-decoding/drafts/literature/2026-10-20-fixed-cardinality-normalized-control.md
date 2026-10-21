# Fixed-cardinality normalized control — proposed bounded specialization

TARGET: Specialize the fixed-cardinality triple contractions at N=floor(65537^28/2^128)+1 and test all 64 nonzero-distance rows on the objective-matched singleton mixture of L022/L023.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed 2026-10-20-fixed-cardinality-triple-marginals.md assessment and its targeted cardinality/Lasserre/coding searches; compare ATTEMPTS/033,034,080 and L001,L021,L022,L023,L097. No inspected source supplies this particular normalized-control verdict.
SOURCE_EVIDENCE: Reinspected Raghavendra–Tan https://arxiv.org/pdf/1110.1064v1 Section 3, Definitions 3.1,3.3 p. 7, conditional-cardinality display p. 8 and qualification p. 9; Schrijver https://homepages.cwi.nl/~lex/files/codes.pdf III.B (60),(62)–(66), p. 7; Kim–Toan https://arxiv.org/pdf/1212.3467v1 (31)–(35), pp. 8–9; Polak https://arxiv.org/pdf/1703.05171v1 Proposition 1.1 full indicator proof p. 2 and Section 1.2 p. 3. Reuse foundations/04,12,13 and companion review for prior search coverage and qualifications; foundations/11 is contrast only.
COMPARISON: Known conditioned cardinality marginals and normalized triple counts cover the general tools. Their repeated-index/orbit specialization and this one exact residual test remain to be carried out; no full-matching finite-instance result or novelty claim is asserted.
GAP: Prove necessity for actual exact-N selected-support codes, match the source normalization and all repeated terms, prove the control has objective N and preserves inherited constraints, and obtain complete exact residuals for distances 5–68. A failure rejects this control only.
REASON: Separate literature approval on 2026-10-20 repaired direct-source coverage and confirmed applicability for the unchanged bounded target. One normalization-controlled test can distinguish additional cardinality consistency from objective mismatch; all specialization and witness verdicts remain future research.
SCOPE: Only the frozen control, all 64 contraction rows and the inherited controls specified below; no optimization, parameter search, altered witness, L097 support enlargement or L053–L096 contract.

## Exact prescribed control, not a result of this review

Use n=1024,w=68,v=956,d=10, T=65537^28/2^128 and N=floor(T)+1.
Let z denote the entire original-orbit L022/L023 formula, not just
L097's selected support, and let M=(U+1)/2 be its source objective,
with U from L021. Let e be the normalized singleton-code assignment:
its all-repeated orbit is 1 and all other actual orbits are zero.
For this subsequent test prescribe

    alpha=(N-1)/(M-1),   z_control=alpha*z+(1-alpha)*e.

This is a chosen diagnostic definition. No new identity, feasibility,
objective computation, contraction or nonredundancy verdict is proved
here. Verify alpha in [0,1], every endpoint value, all repetitions and
the exact source objective before using the control. This is convex
normalization of a relaxed assignment; do not call it thinning a code
or constructing an exact-N measure. Do not use a hypergeometric formula
with the possibly nonintegral M.

## One coherent mathematical attempt after this source approval

Use L001/L021's support argument to justify reducing any hypothetical
larger list to exactly N distinct selected 68-supports, uniformly in m.
Specialize foundations/13's conditioned cardinality requirement to
the unconditioned Boolean moments, without dividing by a possibly zero
pair probability. Then translate using the complete ordered-triple
counts and multinomial normalization of foundations/04. Keep terms
where the third support equals either earlier support, all forbidden
distances, impossible-orbit exclusions and the original t-s symmetry.
Give the coefficients and the necessity argument explicitly; do not
assume that absence of a row in the old batch proves independence.

Test all 64 rows for pair half-distance i=5,...,68, as well as the
normalization and distance-zero controls. The i=0 objective identity
cannot count as the discriminating result. Use exact rational arithmetic
and save every relevant coefficient/residual, actual counts, failures
and paths. Independently reconstruct row coefficients by counting
third supports relative to a fixed ordered pair, as a check against
the source multinomial construction. Small complete cases may check
the repetition convention but cannot replace the full exact evidence.

First establish inherited feasibility at the same control: all original
scalar/pair rows and source symmetries, L097's unchanged 166 matrices
and L023's full two zero-index matrices. Use the frozen endpoint
certificates and the cited convexity of affine PSD constraints rather
than solving or enlarging the stopped batch. Any failed endpoint or
normalization check must be reported; it invalidates the intended
nonredundancy comparison. No old block is independently optimized.

Continue this mechanism only if a nonzero-distance contraction fails
after the exact-N objective and inherited controls pass, thereby
establishing a concrete extra necessary condition against this slice.
That would be a known-method consistency obstruction, not a uniform
bound, packing or RS conclusion. If all rows pass, redundancy is found,
or the control comparison is invalid, park this specific diagnostic
without changing alpha, endpoints or constraints. A future uniform
fixed-cardinality infeasibility target would need its own assessment.

Essential inputs: L001,L021,L022,L023,L097 and foundations/04,12,13;
foundations/11 is a contrast only, not a thinning premise. The separate
67-agreement question, other moments, labeled restrictions, RS
realization, qualified ABF comparison and the 955–957 boundary remain
unresolved. Full matching Mathlib coverage is not checked. The method
is known; a successful specialization should be classified REPRODUCTION.

## Separate source approval, step 359

This is a literature-only process repair, not a new mathematical result.
The target, control and stopping test above are unchanged. Reused the
companion assessment's searches and inspected ATTEMPTS/033,034,080;
they stop different prescriptions or the old selected support, not this
objective-matched cardinality diagnostic. No further discovery search
is needed for the unchanged hypotheses.

Direct primary PDFs above were readable through web text on 2026-10-20.
Raghavendra–Tan's Section 3 requires consistent local distributions and
matching vector inner products; its conditional cardinality display
applies to assignments on at most one fewer variable than the marginal
order. The following paragraph warns that a global representing
distribution need not exist. The conditional expression does not settle
zero-probability assignments: the future homogeneous specialization
must handle these without division. Its Boolean variables here index
68-subsets; they are not evaluation positions. No rounding theorem is used.

Schrijver (62)–(63) and Kim–Toan (31) count ordered triples in C cubed,
including repetitions, with both multinomial factors; the latter sets
impossible-orbit entries to zero. Their affine PSD families and source
objective fix the normalization to retain. Schrijver's qualified (61)
prefactor remains unused. Polak's complete Proposition 1.1 indicator
proof gives the constant-weight code input despite its printed A(n,d)
conclusion; Section 1.2 explicitly uses convexity for invariant averaging.
This does not authorize averaging labeled RS restrictions.

No inspected theorem supplies the 64-row finite-instance verdict.
SPECIALIZE authorizes only the stated conversion and frozen-control
test, classified REPRODUCTION if performed. Inherited endpoint
feasibility and exact objective remain mandatory checks, not findings
of this approval. No contraction, numerical test, lemma or mathematical
script was produced. Full matching Mathlib coverage remains not checked.
