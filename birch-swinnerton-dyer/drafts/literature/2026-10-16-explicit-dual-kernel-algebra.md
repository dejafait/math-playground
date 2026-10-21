# Explicit dual-kernel algebra — primary algorithm comparison

TARGET: Construct and independently verify the full nonzero dual-kernel algebra of L071 over L070's degree-eight direction field.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched dual isogeny kernel polynomial resultant image torsion Kohel algorithm; Shumow thesis 2009 dual isogeny algorithm kernel polynomial; isogeny kernel polynomial image resultant minimal polynomial push forward; and Bostan Morain Salvy Schost fastElkies prime algorithm pdf 2008. Compared L070/L071/L072, their quotient/duality assessments and ATTEMPTS/035--036. Inspected the primary theorem/proof and version-pinned algorithm cases below; no novelty is inferred.
SOURCE_EVIDENCE: Bostan--Morain--Salvy--Schost arXiv:cs/0609020v1, PDF dated 1 February 2008, Theorem 2 p.2, sections 2.4--2.5 pp.5--6 and 4.1--4.3 pp.8--13, including Proposition 4.1 proof and fastElkies' correctness argument; Sage 10.7 ell_curve_isogeny.py dual() lines 3000--3071 and compute_isogeny_bmss() lines 3119--3188, weierstrass_morphism.py baseWI lines 32--40 and 158--203; Stacks 00UB/00UC. Reuse Sutherland duality, Velu quotient and Stacks 03QR coverage in the cited local assessments.
COMPARISON: Primary normalized-isogeny reconstruction covers characteristic-zero degree-seven computation without a known kernel polynomial or generator, after transporting the dual's differential scaling to a normalized codomain. L071/L072 supply existence and the abstract family; exact whole-field coefficients, both-coordinate presentation and independent certificates remain unproduced. This is known-algorithm reproduction.
GAP: Produce and independently check the exact kernel cubic, both signs through the target curve equation, actual dual identification, etaleness and dimension six over D; this review establishes no coefficient or fixed-instance identity.
REASON: Previously essential algorithm coverage is now inspected. The bounded separate RESEARCH / REPRODUCTION construction below is supported, subject to the supervisor's separate approval of this newly ready assessment; no new lemma or mathematical script is written here.
LITERATURE_REASON: The invocation-start target was REVIEW_REQUIRED and earlier assessments explicitly excluded explicit dual-kernel computation; BMSS reconstruction fills that essential source scope.
SCOPE: Only the exact TARGET on the fixed conductor-389 curve at seven, full degree-eight D and raw short models; normalization applicability, known-algorithm construction and independent replay are covered. No selected embedding, rational generator, root-of-unity trivialization, field-factor claim, incidence/norm, functions or descent arithmetic.

## Intended use and discriminating test

The main gap is unchanged: arbitrary analytic order at least two does
not yet give rational rank equality. An explicit algebra for the already
identified affine-line family could support later L066 descent data;
it cannot supply their arithmetic completeness or remove divisible Sha.

Essential inputs are audited L067/L068/L070/L071/L072, including the
full direction polynomial and relative cubic, mixed inverse, both
coordinate transports and quotient-254 maps. No L069 or partial column
evidence is permitted. The literature comparison must retain all eight
embeddings and both signs of all nonzero dual-kernel points, and explain
how a full algebra of dimension six over D (48 over Q), exact kernel
identification and finite etaleness would be independently certified.
A degree count or a kernel computed at one embedding is insufficient.
No field-factor decomposition or polynomial shape is presumed here.

Continue only with a primary-source-supported method and an explicit
bounded test distinguishing the actual dual kernel from unrelated
seven-torsion on the target. An inaccessible essential source or a
method that only recreates the stopped full-column presentations is
grounds to park that method and choose an independently testable one.
ATTEMPTS/035--036 retain their original cost evidence and limits; this
proposal does not resume or extend those runs.

Functions, incidence/norm, complete global units/classes, local
identifications and bounds, Selmer containment, other L026 premises,
successful localization, rational membership and arbitrary-curve
comparison remain unresolved. Full matching Mathlib coverage for the
proposed computation has not been checked. This review fills source
coverage only. The initial REVIEW_REQUIRED proposal's target and exclusions
are retained; no unfinished computation or historical stop is discarded.

## Primary theorem and algorithm coverage

[Bostan--Morain--Salvy--Schost](https://arxiv.org/pdf/cs/0609020),
*Fast algorithms for computing isogenies between elliptic curves*,
Theorem 2(2), gives normalized degree-l reconstruction over a field of
characteristic zero without knowing the kernel-coordinate sum. The
inspected version is arXiv v1 (header 6 September 2006), with PDF title
date 1 February 2008; use its printed numbering. Journal metadata:
*Mathematics of Computation* 77 (2008), 1755--1778,
DOI 10.1090/S0025-5718-08-02066-8. The publisher text was not compared.
Read the theorem hypotheses, Proposition 4.1 and its full paired-point
proof, sections 2.4--2.5's nonlinear series and rational reconstruction,
and all fastElkies' steps and correctness argument in section 4.3.
The general schedule uses S modulo x^(8l-4), followed by rational
reconstruction; the odd-degree paragraph permits reduced precision.
Characteristic zero makes all required integer divisions legitimate.
The method works algebraically over its base field. Its field-operation
complexity is not a rational bit-size or wall-clock bound. No general
reproof is needed.

The author URL `https://www.lix.polytechnique.fr/~morain/jcomp.pdf`
returned HTTP 403 and an attempted Bostan-hosted PDF failed. The complete
relevant arXiv text was accessible, so no essential source remains blocked.
Search snippets and secondary answers are not theorem inputs.

[Sage 10.7 implementation](https://raw.githubusercontent.com/sagemath/sage/10.7/src/sage/schemes/elliptic_curves/ell_curve_isogeny.py),
`dual()` lines 3000--3071, handles characteristic not dividing the degree
by normalized reconstruction, then isomorphisms with combined scaling
equal to the degree. Its target model change has parameter u/d, where
u is the original scaling factor. `compute_isogeny_bmss()` lines
3119--3188 implements fastElkies', rational reconstruction, square-root
extraction and monic normalization. The complete relevant branches were
read. This is algorithm evidence, not a fixed-instance certificate.
The implementation uses the shorter odd-degree schedule; the attempt
may instead use the conservative general schedule from the paper.

[Sage 10.7 Weierstrass conventions](https://raw.githubusercontent.com/sagemath/sage/10.7/src/sage/schemes/elliptic_curves/weierstrass_morphism.py),
`baseWI` lines 32--40 and 158--203, specify coordinate direction,
inverse powers and transformed coefficients. Applying this convention
and checking its differential on the fixed raw models is a research
obligation. Do not reconstruct a normalized map directly back to the
unchanged source model and call it the actual dual.

[Sage's Stark documentation](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_curve_isogeny.html#sage.schemes.elliptic_curves.ell_curve_isogeny.compute_isogeny_stark)
warns of an error in the published Stark pseudocode and refers to Moody
(2009). Shumow section 3.3.2 pp.60--62 was inspected as comparison,
not selected. Moody's correction and Stark's original were not read.
BMSS section 4.3 is the selected method, so neither is essential; this
assessment does not approve uncorrected Stark pseudocode or treating
its squared denominator as a kernel cubic. The prior quotient-formula
qualifications in the reused assessment remain.

The push-subgroup search led to EPSV2023 and Sage's newer subgroup
interface. Their full theorem hypotheses and algorithm were not read;
they are unread alternatives, not approved characteristic-zero fallbacks.
No resultant algorithm is imported from an excerpt.

[Stacks Definition 10.144.1](https://stacks.math.columbia.edu/tag/00UB)
and [Lemma 10.144.2](https://stacks.math.columbia.edu/tag/00UC) give
the monic-polynomial/invertible-derivative standard-etale criterion and
its etaleness/base-change statements. The lemma omits the proofs of
those parts; this is an explicit standard-theorem import, not a claim
to have read an omitted proof. Reused L072/Stacks 03QR handles the
finite geometric family after exact equivariant identification.

## Specialization and discriminating verification requirements

These are obligations for the separate construction, not a derived
lemma, calculated polynomial or verified instance. Use audited
L067/L068/L070/L071/L072 and `scripts/seven-torsion/quotient-254/quotient.json`.
Reuse the precise source qualifications in
`drafts/literature/2026-10-16-quotient-affine-line-dual-kernel.md`
and `drafts/literature/2026-10-16-conductor389-direction-quotient-construction.md`.
The source short model is Y^2=X^3-3024X+46224. L071 supplies scalar one,
separability and nonsingularity over all of D. L072 supplies existence
of the base-field dual. No cross-notebook input is used. No matching
fixed explicit presentation exists in the checked local results; the
earlier homology dual-kernel work addresses a different object.

1. Apply the cited dual normalization with l=7 and L071's scalar one.
   Write and exactly check the model change, inverse and differential
   before reconstructing a normalized isogeny. Use BMSS fastElkies'
   without a supplied kernel sum. Record all series precisions and
   rational-reconstruction degree bounds. The conservative general
   schedule suffices; any shorter schedule must match the inspected
   odd-degree case. Perform every operation in D=Q[Z]/h.
2. Retain the full reduced denominator and monic square-root candidate
   k(T). Require exact squaring, degree three, numerator coprimality,
   squarefreeness and unit witnesses for constant divisions. Transport
   both maps back through the checked isomorphism, retaining the actual
   raw-model dual with differential scalar seven.
3. Independently check both coordinate curve identities, differential,
   exact degree seven and extension/kernel behavior at every finite
   kernel point and O, using the reused quotient coverage. Verify both
   dual-composition identities against [7] in both full function fields
   and coordinates. Build [7] from the already assessed division-
   polynomial/group-law inputs independently of producer reconstruction.
   Keep complete polynomial residuals modulo h. Samples, target
   seven-torsion membership, counts or a software degree label are
   insufficient. The reused dual uniqueness theorem identifies the map;
   no new general duality proof is requested.
4. Establish the full nonzero algebra with both target coordinates,
   proposed as D[T,V]/(k(T),V^2-(T^3+a'T+b')). This is a presentation
   to verify, not assumed completeness. Supply Bezout/inverse witnesses
   for k'(T) and T^3+a'T+b' modulo k. Retain V as a quadratic algebra
   element, without selecting a square root. Check the full six-element
   D-basis, 48-element Q-basis, multiplication and finite etaleness.
   Account for O exclusion in every fiber through the projective kernel
   proof and L072. Explain why the exact D-identities give the result
   in all eight embeddings, rather than checking one selected root.
   No field-factor decomposition, fieldness or new Q-power basis is
   required or presumed.
5. Preserve L072's inverse ordinary-functional indexing and Cartier
   cyclotomic conventions. Use raw target coordinates; do not replace
   the dual kernel by the original kernel or trivialize mu_7. The
   presentation itself gives neither incidence maps nor a rational point.

Use one whole production stage and one independent replay stage, each
capped at 180 seconds with an external watchdog, with at most 128 MiB
of new certificate data. Timers cover all new arithmetic in their stage.
Do not split a failed stage retrospectively or extend either stopped
column run. Small isogeny degree motivates this bounded test; coefficient
growth over D can still cause failure. Save full exact certificates,
actual/required bounds, failures and paths; print compact summaries.
Inspect complete load-bearing evidence before claiming success. The
verifier must not import producer arithmetic. Preserve upstream bytes
and use bounded rejection cases for wrong normalization, a lost sign
and a changed late coefficient.

Continue only if all exact identities, actual dual identification and
full-family etaleness tests pass within these bounds. Stop on the first
cap or failed identity and preserve the precise obstruction. Neither
ATTEMPTS/035 nor /036 is resumed. Successful production still requires
a later separate critical audit. An unassessed algorithm change needs
fresh review. Full matching Mathlib coverage remains not checked.
This literature-only turn changes no mathematical argument in PROOF.md
or the DAG and produces no instance beyond the imported sources.
