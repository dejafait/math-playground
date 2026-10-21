# Audit coverage for the forced-cross covariance obstruction

TARGET: Critically audit L448's endpoint-layer obstruction to the derivative-forced bulk xy covariance, including its uniform old-density modulus and positive-measure real-H and temporal quantifiers.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 290 compared all of L448 with the ready forced-cross assessment, relevant L366/L391/L445/L446 passages, L447's cutoff/mean/support bounds, step 288 and the fixed-data stop; reused the recorded matrix/occupation discovery queries and freshly read the DLMF derivative formula, gamma recurrence and sector-qualified psi expansion with complex remainder conditions.
SOURCE_EVIDENCE: Reuse Boyd--Vandenberghe Appendix A.5.5 pp. 650--651 (A.13)--(A.14), Hunter Definition 3.1 pp. 47--48 and Theorems 3.60, 3.62--3.63 pp. 79--80, Bell Section 1 Theorem 1/uniqueness, and Bourgain arXiv:1408.5794v2 Theorem 5 (0.5) p. 2 via the assessments below; freshly inspect NIST DLMF 1.9.30--31, 5.5.1, 5.11.1--2 and the complex remainder paragraph in 5.11(ii), accessed 2026-10-20.
COMPARISON: The known matrix and AC results cover the necessary interfaces, and Cauchy's formula covers every fixed derivative order; none certifies L448's quantitative branch bounds, exact response polynomial, fixed-data subtraction or nested positive-measure conclusions. These require a separate mathematical audit rather than a new general theorem or reproof of the imported inputs.
GAP: Source coverage is ready; correctness of L448 (1)--(12), uniformity in the original stages and both positive-measure quantifiers remains unverified until the later critical audit.
REASON: The newly proposed audit needed a separate scope comparison, especially because L391 states its derivative application only through order two. This step approves coverage, not the obstruction's proof.
SCOPE: L448's stated fixed-data obstruction only, with L447's original width H^-10, rare components, bulk mean and y-second data; no changed-data construction or global realization.
COVERED_TARGET: Critically audit L448's endpoint-layer obstruction to the derivative-forced bulk xy covariance, including its uniform old-density modulus and positive-measure real-H and temporal quantifiers.
LITERATURE_REASON: Separate approval of the saved REVIEW_REQUIRED critical-audit target; the fixed third derivative and gamma-phase specialization were not explicitly covered in its pending audit record.

## Gap, intermediate target and decision test

Global mixed positivity remains the main RH gap. The intermediate target
is validation or correction of L448, not another extension of the law.
A validated obstruction would justify keeping this fixed-data route
stopped before considering changed densities, widths or y-second data.
Continue to that scoped stop only if the complete old-density modulus,
centered PSD budget and AC endpoint comparison hold uniformly on the
original ray and give both claimed positive-measure conclusions. A
failed load-bearing estimate requires narrowing or correcting L448;
source approval alone is no evidence that the theorem is true.

## Reused primary coverage and duplicate/failure comparison

Use the full inspected source record in
`drafts/literature/2026-10-20-endpoint-repair-forced-cross-feasibility.md`.
Boyd and Vandenberghe, *Convex Optimization* (2004, corrected seventh
printing 2009), Appendix A.5.5, pp. 650--651, gives the block PSD
criterion, including its singular range condition. The later audit must
apply it to the centered bulk block after subtracting both the complete
rare cross entry and bulk translation. It is not a completion theorem.

Use `drafts/literature/2026-10-20-complete-x-second-integrated-xy-compatibility.md`
for Hunter, *Notes on Partial Differential Equations*, revision
2014-06-18, Definition 3.1/uniqueness pp. 47--48 and Theorems 3.60,
3.62--3.63 pp. 79--80; Bell, *Sobolev spaces in one dimension and
absolutely continuous functions* (2015-10-21), Section 1, Theorem 1
and subsequent uniqueness paragraph. Their weak-derivative uniqueness
and AC endpoint integration require the specified continuous
representative, local integrability and the positive smooth weight L.
L446 supplies that interface; L447 supplies the changed Lipschitz q.
No converse realization theorem is used.

For the scalar zeta input reuse
`drafts/literature/2026-10-10-signed-k1-projection-audit.md` and
`drafts/literature/2026-10-20-endpoint-repair-critical-audit.md`.
Bourgain, *Decoupling, exponential sums and the Riemann zeta function*,
JAMS 30 (2017), 205--224, arXiv:1408.5794v2, Theorem 5 (0.5), p. 2,
gives the unconditional critical-line exponent 13/84+epsilon for
fixed epsilon>0. The audited L391 scalar strip/disk argument, including
the reflected half-disk and extended endpoint heights, is the local
input for a later third-order Cauchy specialization. Bourgain itself
is not a derivative theorem. Reproof is neither needed nor authorized.

L444's bounded zero-11 failure and L446's unchanged-density endpoint
failure have different hypotheses. L447 already repairs the scalar
endpoint identity and finite block. L445 supplies only fixed-H
regularity; it does not supply the asserted uniform modulus. L448 is
the new fixed-data obstruction awaiting audit, not an independently
verified duplicate. The exact stop is preserved in
`ATTEMPTS/2026-10-20-endpoint-repair-fixed-data-forced-cross.md`.
The earlier discovery queries are recorded in the forced-cross
assessment; no new novelty search or originality claim is made.

## Fresh analytic source inspection

[NIST DLMF 1.9.30--31](https://dlmf.nist.gov/1.9.E31) states Cauchy's
formula for every positive integer derivative order on a positively
oriented simple closed contour, with continuity on its closure and
analyticity inside. This covers fixed order three; the later audit
must still verify L391's scalar disk bound and uniform constants.

[DLMF 5.5.1](https://dlmf.nist.gov/5.5.E1) gives gamma recurrence.
[DLMF 5.11.1--2 and 5.11(ii)](https://dlmf.nist.gov/5.11) give log-gamma
and psi expansions in sectors separated from the negative real axis,
with complex remainder bounds. These cover the proposed local analytic
tools, subject to checking pole-free disks and branches. They do not
state L448's response polynomial or its normalized third-order bounds.
These current online primary passages were read on 2026-10-20; no
unread source is essential to this audit. No new specialization is
proved in this literature turn.

## Bounded audit obligations and limits

The later mathematical audit must check L448's exact completion and
response signs, derivative order and normalization; all max/zero/tie
branches via L445's scalar formulas; and bounds for probabilities,
translation, normalizations and the finite Poisson product with H and
stage held fixed. In particular, check uniformity, not merely fixed-H
Lipschitz regularity. Verify the complete rare/mean subtraction before
the PSD test, the old-density cancellation budget, either active
endpoint and AC integration over its entire layer. The real-H sets
must retain L446's positive measure at arbitrarily late original
stages. Temporal failure must have positive measure after deleting
nondifferentiability null sets, not merely occur at an endpoint.

Essential local inputs remain L366, L391, L438, L443, L445, L446 and
L447. No mathematical result was added or certified here. Full matching
Mathlib coverage of L448 remains unchecked as its canonical file says;
unknown availability is not absence. Changed data, remaining temporal
and mean identities, inter-H consistency, actual/global realization,
actual clipping, capped nondegeneracy, L413's full-error margin and
global mixed positivity remain unresolved. There is no RH candidate.
