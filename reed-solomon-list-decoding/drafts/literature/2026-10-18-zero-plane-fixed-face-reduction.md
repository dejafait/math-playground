# Fixed-face reduction — known-method scope assessed

TARGET: Determine whether L082's positive-weight modes yield a fixed exact face reduction of the full zero-plane joint affine-LMI system.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched semidefinite facial reduction/exposing-vector/kernel-compression terminology and Schur-complement facial reduction; checked local overlap in the step-297 assessment, step-298 model/working record, L082–L084 and ATTEMPTS/060–067. Permenter–Parrilo v3 supplies the finite certificate/reformulation method; no search result establishes the notebook-specific face.
SOURCE_EVIDENCE: Inspected Permenter–Parrilo arXiv:1408.4685v3 Lemmas 1–3, complete proofs of Lemmas 2 and 3, Remark 1, Algorithm 2 and Section 4.1; Section 3.1's nonminimal-face warning. Reuse foundations/10's inspected affine-LMI, weak-duality and singular-Schur coverage; its prior degenerate-certification comparison remains qualified.
COMPARISON: Known face formulas cover restriction by a checked fixed PSD multiplier orthogonal to the affine pencil, with kernel equations retained; neither L082's scalar weights nor L084's equality parametrization identifies that multiplier. No new general facial-reduction theorem is needed, and no local reduction is proved in this review.
GAP: In a later mathematical attempt construct and check one constant rational multiplier from the unchanged canonical tight-mode weights, or exhibit a precise failed identity; then retain all linear face equations and verify the exact original/reduced formulation. Feasibility and minimality remain separate questions.
REASON: Essential primary coverage is now sufficient for one bounded REPRODUCTION attempt on the saved target; coefficientwise trace cancellation, PSD and an exact kernel basis are testable without assuming Slater, feasibility or a rational-existence theorem.
LITERATURE_REASON: The changed target requires fixed-face identification and exact equivalence, which exceeded the earlier weak-duality feasibility assessment; the primary facial-reduction passages were essential and previously unread.
SCOPE: L076's full original 85-row domain with t78=s, all 45 moment signs, L075's unchanged dictionary, all 81 included-anchor modes, full anchor and all singular/empty ranges; one fixed reduction from L082's canonical weights, with no new solve, parameter cap, scalar upper row, other anchor, pair/base choice or global extension.

## Main gap and intended use

Arbitrary-center safety at 67 or 68 agreements is still unresolved; the
finite bracket is 955–957. The intermediate target is exactly TARGET.
A verified equivalent face restriction could make a later joint test
more discriminating. It would establish neither a completion nor a
contradiction, and would not address scalar upper rows, other anchors,
global consistency, alternative moments or RS realization.

## What was searched and read

Queries on 18 October 2026 included:

- `semidefinite facial reduction exposing vector PSD trace zero kernel compression Permenter Parrilo partial facial reduction`
- `facial reduction semidefinite programming feasibility affine slack exposing certificate Waki Muramatsu theorem`
- `"semidefinite" "Schur complement" "facial reduction" "exposing"`
- `"Partial facial reduction" "2018" "171" "1" Permenter Parrilo`

The primary theorem evidence is Frank Permenter and Pablo Parrilo,
*Partial facial reduction: simplified, equivalent SDPs via approximations
of the PSD cone*, [arXiv:1408.4685v3](https://arxiv.org/pdf/1408.4685v3),
submitted 17 May 2017, manuscript dated 19 May 2017. The canonical
statements, precise pages, hypotheses, proof cases and Mathlib qualification
are saved in foundations/10's fixed-face source addition. Read Lemma 1's
face/constraint forms, both proof directions of Lemma 2, the entire
Lemma 3 kernel argument, Remark 1's infeasible-case qualification and
Section 4.1's retained linear equations. This suffices for a checked
partial reduction; later maximum-rank and dual-recovery results are not
imported. No claim of source-level discovery is made.

The author-hosted MIT PDF returned an internal browser error. The
versioned arXiv PDF was readable at the required passages, so there is
no essential source blocker. Search hits for symmetry-reduced DNN
facial reduction, Waki–Muramatsu, Ramana and weak infeasibility remain
unread leads here. No theorem from those hits or search snippets is
used. The MIT repository record was a bibliographic search hit, not
additional inspected proof evidence. Failed search establishes no novelty.

## Source comparison and local evidence limits

The source applies to finite real symmetric pencils and supplies both
a face description and an exact constraint representation. The saved
step-298 model has the required affine form in 48 variables. Its working
record and constructor lines 85–145 describe original blocks, rational
fixed-base congruences and full-plane zero-cross checks. The certificate
schema and complete selected-mode index list were inspected to locate
the future test, without treating a preview as verification of all data.
No full certificate rerun or mathematical identity check was performed.

L082 supplies nonnegative scalar Schur weights with 28 positive entries.
L083 confines a possible completion to t78=s. L084 supplies rank-27
equality compatibility and an 18-dimensional signed completion space.
Those facts do not themselves satisfy a fixed matrix-exposure hypothesis.
In particular, a Schur kernel may depend on the parameters; a scalar
quadratic pairing is not automatically an affine-pencil trace identity.
The exact transport through the original source blocks remains the
mathematical work. A citation cannot supply that computation.

Reuse the earlier Vandenberghe–Boyd and Sano coverage rather than
reprove weak duality or the singular-Schur criterion. The previously
inspected Kolmogorov–Naldi–Zapata v3 certification theorem still needs
unestablished nonemptiness, maximum-rank proximity and valid-column
hypotheses; it is not a substitute for a fixed certificate. Free-entry
chordal completion does not enforce the shared moment dictionary.

The local overlap/failure check retains ATTEMPTS/060–066's fixed-column,
fixed-weight and equality-only stops. ATTEMPTS/067 stops one numerical
run and rounding prescription; it neither decides the full plane nor
forbids a different exact reduction. Step 298 already removes fixed old
base kernels. A multiplier acting only on those discarded directions
would add no reduction. No adequate duplicate fixed-face certificate
was found in the specific local paths checked.

## One bounded mathematical contract and decision test

The next attempt may construct one fixed rational block-diagonal PSD
multiplier using exactly L082's unchanged canonical weights and the
saved original tight-mode blocks. It may calculate the needed inverse
actions and kernel bases exactly. This is a known-method specialization,
classified REPRODUCTION; no originality claim is licensed. Do not run
another conic solve, vary weights, scan points or restrict the domain.

Save the proposed multiplier and check symmetry/PSD exactly. In the
original plane variables check its trace pairing with the constant
coefficient and every one of the 48 variable coefficients, including
all 45 moment coefficients. Preserve positive norms, multiplicities,
original/raw scaling, both rectangular directions and the full anchor.
Any conversion from the scalar weights must be explicit. Check that the
multiplier acts nontrivially after the already saved kernel removals;
its proper-face claim needs more than a nonzero discarded-kernel entry.

If these tests pass, compute an exact full-rank basis for the multiplier's
kernel and an exact complement. Use the source's compressed PSD condition
together with ALL mixed and removed-coordinate zero equations. Check
their pullback to the original affine blocks coefficientwise; preserve
all untouched blocks, domain/sign rows and original equality contracts.
Handle zero-dimensional and empty blocks explicitly. A reduced PSD
condition alone is insufficient. Do not replace the affine pencil by
L084's quadratic parametrization and call the result an affine LMI.

Continue this mechanism only with a nontrivial exact certificate and
an original/reduced equivalence retaining the entire plane-domain system.
Otherwise save the precise failed constancy, PSD, trace, range, rank or
equivalence check and stop this fixed prescription. A failed candidate
need not exclude every fixed face; a formal face restriction need not
be minimal or strictly feasible. Rational certificate existence and
exact Farkas alternatives are not assumed. This attempt ends after
the reduction test, before another feasibility solve.

Essential continuation inputs: L021,L053,L073,L075,L076,L078,L079,L081,
L082,L083,L084; foundations/04,09,10,12; complete step-290/292/294 and
equality certificates; step-298 `zero-plane-joint-feasibility-results.json`
and its verification in scripts/finite-support/. Retain rho,p8, original
pairs, seven RREF/completion, 90 weighted kernel equations, 500 types/
3000 presentations, 36 forced/45 free entries, all 81 modes and canonical
weights. Whole-kernel/base-PSD/uniqueness contracts retain their ancestral
qualifications; L084's critical review remains pending. This source
review does not discharge any critical review or change PROOF.md/DAG.md.
