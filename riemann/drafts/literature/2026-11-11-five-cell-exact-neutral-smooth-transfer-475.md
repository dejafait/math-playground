# Source approval: exact-neutral smooth transfer in the logarithmic form norm

TARGET: Establish form-norm approximation of every exactly cell-neutral even sum of modes0-83 by even cell-interior smooth tests satisfying the original ten five-cell moments exactly.
CHECKED: 2026-11-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step476 searched logarithmic Laplacian smooth density, constrained form cores, finite-codimension dense-subspace complements and moment-preserving Sobolev approximation; checked the named local cutoff/right-inverse results and five-cell stops. Primary passages inspected are listed below; no exact combined theorem was located and no novelty inference is made.
SOURCE_EVIDENCE: Read Suzuki arXiv:2606.09096v3 Section3.2, (3.2)-(3.4) and both frequency cases through its conclusion; reread Li45 displayed v2 Lemma3.1/(2.1); inspected Hofer-Wysocki-Zehnder, JEMS9(2007),841-876, Lemma2.12 p846 with its complete proof; inspected Feulefack-Jarohs, DOI10.1007/s10231-022-01290-y, (2.1), space definitions and Theorem3.1/Remark3.2, PDF pp6/11. Reuse L743(9)-(10), C744c Section2 and C744e's accepted closure audit.
COMPARISON: The inspected cutoff and finite-dimensional complement methods cover the proposed mechanism, not the exact combined conclusion. The general Lipschitz-domain theorem cannot simply be applied to the punctured five-cell union. A finite-vector cutoff specialization and fixed smooth correction are justified work; no new general density theorem or sign computation is needed.
GAP: Still to prove: cutoff convergence at every cell boundary in the full shifted logarithmic form norm; form-norm control of a fixed smooth correction for physical moments; compatibility with even reflection and all ten complex equations. No such specialization or estimate is derived in this literature turn.
REASON: Essential comparison is now complete for exactly TARGET. Approve one REPRODUCTION attempt using the inspected standard methods and accepted local inputs, without retuning any stopped energy comparison or importing a numerical positivity claim.
SCOPE: Only ell=log3/2, a=5ell/2, original complex physical moments, the even modes0-83 and the semibounded zero-extension logarithmic form of L744(6); no positivity, graph-tail, odd-sector or all-window conclusion.
LITERATURE_REASON: The target at invocation was REVIEW_REQUIRED; its internal-boundary, exact-moment and parity hypotheses were outside the prior unconstrained closure assessment. This turn supplies that missing comparison; further literature is not required for the unchanged target.

## Completed source comparison — 11 November 2026, step476

The main gap is L030-L032/C032a actual-Xi positivity. This intermediate
target would connect finite exactly neutral tests to the cell-interior
smooth class in energy norm. It pays a domain issue only; it supplies
no coercivity or global sign. The target is preserved verbatim above.

Exact external queries (search results used as leads, not theorem evidence):
`"logarithmic Laplacian" "density" "smooth"`;
`"dense subspace" "kernel" "finite codimension" approximation constraints`;
`"Sobolev" "preserving moments" "density"`;
`"logarithmic Laplacian" "C_c" "dense" Chen Weth`;
`"Nonlocal operators of small order" density theorem 3.1`;
`"Hofer" "Lemma 2.12" "dense" subspace`.
Forum hits were discovery leads only; the primary passages below,
rather than snippets or model memory, support the comparison.

**Primary sources and their limits.**

- Masatoshi Suzuki, *Weil's quadratic form via the screw function*,
  [arXiv:2606.09096v3, Section3.2](https://arxiv.org/html/2606.09096v3#S3.SS2),
  (3.2)-(3.4), including the subsequent two frequency integrals and
  conclusion: smooth approximation of fixed trigonometric tests in
  the shifted semibounded Weil form norm. Its boundary-error argument
  retains endpoint terms, controls the Fourier transform by both an
  L1 estimate and a uniform variation estimate, and obtains squared
  form error O(epsilon log(1/epsilon)). This is unconstrained outer
  boundary approximation, not a ten-moment or internal-boundary theorem.
  Both low- and high-frequency proof cases were read. Use the genuine
  compact-support cutoff convention already justified in C744c.
- H. Hofer, K. Wysocki and E. Zehnder, *A general Fredholm theory I:
  A splicing-based differential geometry*, J. Eur. Math. Soc.9(2007),
  841-876, [Lemma2.12, p846](https://ems.press/content/serial-article-files/31611).
  Hypotheses: a Banach space F, a closed subspace Y with a finite
  dimensional complement, and a dense linear subspace F_infinity.
  Conclusion: a finite dimensional complement can be chosen inside
  F_infinity. Its full proof uses surjectivity of the dense subspace
  onto the finite dimensional quotient and chooses representatives of
  a quotient basis. This is the abstract complement input, not an
  unconditional theorem about intersecting arbitrary dense sets with
  kernels. Form continuity of the moment map and the applicable dense
  subspace must still be justified locally; parity changes its image.
- P. A. Feulefack and S. Jarohs, *Nonlocal operators of small order*,
  [published article, DOI10.1007/s10231-022-01290-y](https://d-nb.info/1281913596/34),
  Section2 (2.1), space definitions and Section3 Theorem3.1/Remark3.2,
  PDF pp6/11. The stated smooth density concerns regional or
  zero-exterior kernel energy spaces on all Euclidean space or bounded
  open sets with Lipschitz boundary. The ambient kernel is measurable,
  nonnegative and symmetric, with a uniform finite integral against
  min(1,|x-y|^sigma); the small-order setting has sigma<1.
  The logarithmic kernel is explicitly an example. The union of
  touching open cells has two-sided interior punctures, so its
  Lipschitz-boundary hypothesis is not automatically available.
  Neither equivalence with our full form nor the needed puncture
  removal is imported. The full general density proof was not read
  and is not an essential input to the approved finite-vector method.
- Hongmin Li, *Cutoff-free positivity of localized Weil forms through
  the (log11)/2 threshold*,
  [displayed v2, 9 November2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
  (2.1) and Lemma3.1: the arbitrary-window identity on smooth compact
  parity tests matches the local normalization. It does not itself
  assert constrained density. No positivity threshold or source
  computation is imported for this target.

**Local comparison and duplicates.** L744(6)/(8) and C744c Section2
identify the shifted logarithmic Fourier norm and bounded L2
perturbations. C744e's accepted step466 audit gives closure for finite
even sums, but only removes outer endpoints. L743 Section3/(9)-(10)
and its accepted step285 audit item4 supply fixed complex smooth
right inverses cell by cell, with an L2 bound only. C744b(1) fixes the
physical normalization and its reflection calculation exchanges
(j,sigma) with (4-j,-sigma). These are reusable inputs, not a proof
of the combined target. The new work should cite them and supply only
the missing internal-boundary, form-continuity and parity checks.
No whole-domain identification or quantitative uniform rate over
varying windows is required.

C744g's accepted negative half-energy comparison remains intact, as
does ATTEMPTS/2026-11-11-five-cell-minimum-L2-half-energy-stop-473.md.
A smooth exact correction is not an energy-saving correction; this
target makes no such inference. Searches of the named five-cell
assessments found no completed proof of the combined assertion.
L730's separately assessed arithmetic-functional density problem is
not this logarithmic-form problem and supplies no shortcut.

**Approved test and stopping rule.** For exactly the saved finite span,
the next mathematical turn must exhibit genuine cell-interior smooth
approximants with even parity, exact original moments, and convergence
in a positive shift of L744(6). A fixed smooth right inverse needs a
form-norm bound, not merely the recorded L2 estimate. All internal
boundary errors and the complex reflection law must be included.
If a required estimate fails, preserve that obstruction and stop the
target; L2 convergence, small residual moments or formal endpoint
values do not pass. No result of this test is asserted here.

**Mathlib.** A full matching constrained logarithmic-form theorem was
not checked. Supporting finite dimensional continuity facts are not
a substitute for the analytic specialization; no absence or formal
verification claim is made.

This completed review approves a standard specialization, not creative
central-gap work. The creative blocker remains an absent quantitative
mechanism for unrestricted middle/cell correlations or all-window
growth. No exhausted route budget is renewed.

## Original nomination, step475 — historical, superseded by approval above

This is a future nomination, not ready coverage or a proof. The next
turn is literature-only for the exact TARGET. Search the exact assertion,
standard terminology (constrained form cores, finite-codimension density,
smooth approximation preserving moments) and stronger applicable results.
Retrieve primary hypotheses, especially the form norm and availability
of a smooth right inverse, before approving a specialization. Import a
matching theorem rather than creating an unnecessary new lemma.

Essential local inputs for that comparison are L744(6)/(8), C744b's
physical normalization, C744c/e's accepted cutoff/closure proofs and
L743(9)-(10). C744g supplies the motivating exact-neutral finite graph;
its negative half-energy comparison is not a density premise. No other
notebook result, inaccessible supplement or numerical source sign is
required. Full matching Mathlib coverage is unchecked.

Plausible downstream use: justify passage between these finite neutral
tests and the actual cell-interior smooth neutral class in energy norm.
This would remove a domain-transfer gap while leaving unrestricted
middle/cell interactions, distant graph couplings, odd signs and
all-window positivity unresolved. It supplies no sign by itself.

Continuation test: find adequate primary coverage, then require a proof
of exact moment preservation and convergence in a shifted form norm
equivalent to the logarithmic Fourier norm. An L2-only approximation,
small moment residual or discarded internal boundary is insufficient.
If a matching local theorem already contains the whole statement, cite
it and record the overlap; do not reprove it. If hypotheses fail, record
the precise domain obstruction rather than changing the target silently.

This is a possible standard specialization, not a justified creative
central mechanism. The creative blocker remains the absence of a new
quantitative inequality for unrestricted middle/cell correlations or
all-window growth. The finite half-energy,128-response, coarse-box,
L750 localization-defect and distant-review stops remain recorded;
none is asserted to prohibit this separate domain question.
