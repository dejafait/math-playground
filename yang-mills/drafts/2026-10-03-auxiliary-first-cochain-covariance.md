# Auxiliary-first relative-cochain covariance — working record

## Preflight and test

Read the shared GOAL.md and PROMPT.md, the local goal, checkpoint, whole overview and DAG, the unchanged SPECIALIZE assessment in drafts/literature/2026-10-03-auxiliary-boundary-gaussian-matching.md, L003 and L012, and the preceding failed-domain record. The exact saved action is a COVERED_TARGET of that assessment. There were no pre-existing local changes; unrelated notebook edits are preserved. Reuse the assessment for one RESEARCH / REPRODUCTION step without further literature retrieval.

The intermediate gap is an explicitly defined auxiliary integral reproducing the existing relative Hodge Gaussian. This could supply a legitimate regulated starting representation before separately testing boundary Ward identities. It does not address L011's interacting forest-measure replacement, physical-boundary subtraction or O(1) remainder. Finite matching and the required interacting reflected error <= c_box/2 remain open, as do limiting fields, full reflection positivity, infrared removal and finite positive mass.

The discriminating test is exact equality of the normalized curvature law at each fixed mesh, with b, c and bar c on interior vertices and all relative connection links retained. A changed quadratic form, extra boundary restriction or undefined normalization stops this prescription. L003 already proves the cochain decomposition, nondegeneracy, modes and reflected coefficients; rederive none of those. The only missing specialization is the auxiliary-first Fourier integral and determinant normalization. L012's unrestricted strong Neumann-domain shortcut stays stopped.

## Reasoning saved before completion

Write D = d on relative zero-cochains, E = d on relative one-cochains, and delta = D*. All degrees use L003's inner product a^4 times the cell sum. L003 gives ED = 0, ker E = im D, positive L0 = D*D, and positive L1 = E*E + DD*. Use orthonormal coordinates for Lebesgue and Berezin integration so that no powers of a are hidden.

For each colour, the proposed integrand is

\[
\exp[-\|EA\|^2/2-\|b\|^2/2+i(b,\delta A)
      -(\bar c,L_0c)].
\]

First perform the finite Grassmann integral with convention giving det L0, and the real b integral at fixed A. The normalized Gaussian Fourier identity gives exp[-||delta A||^2/2]. Only then integrate A. If this is correct, the resulting A density is exactly L003's Hodge density; det L0 is nonzero, independent of A and cancels on normalization. The three colour copies factor.

The original joint A,b integrand is not absolutely integrable: its modulus has no decay in im D. Thus changing the integration order or claiming an ordinary joint probability law requires extra justification. The intended b-first prescription is an iterated integral. No pointwise equation b = i delta A is imposed, and no strong partial_n A_n condition is added to the connection integration variables.

The remaining completion checks are the exact normalization and characteristic covariance formula, all boundary-cell interpretations, and an independent finite-complex consistency check. This saved calculation is provisional until those checks and the full proof are recorded.

## Completed result and verification

The full proof is recorded in L013. The auxiliary-first prescription has positive finite normalization and exactly L003's normalized connection law, hence its entire Gaussian curvature law. The ghost determinant is positive and cancels. Orthogonal-coordinate normalization gives the raw point covariance a^-4 d L1^-1 d*. Relative normal links are retained, and every face and intersection is treated by the unchanged cochain complex. No strong normal connection constraint, joint positive auxiliary measure or integration-order interchange is used.

The b-first Fourier transform supplies the gauge-fixing quadratic form. Before that transform the modulus is constant along the nonzero space im D, so the joint A,b integral fails absolute integrability. This explains why covariance equality alone cannot authorize the later auxiliary/ghost Ward change of variables. No such Ward calculation is performed in this step.

Outcome: ADVANCE, RESEARCH / REPRODUCTION. This is a relevant local regulator identification using known Gaussian machinery and the established L003 law; it makes no claim beyond the checked literature. It leaves the required interacting reflected error <= c_box/2, the physical-boundary remainder and all remaining construction and mass requirements unresolved. There is no complete candidate proof or disproof.

An independent exact rational calculation on the complete even N=2 relative complex (one interior vertex, eight links, twenty-four faces) verifies ED = 0, det L0 = 1/2, vanishing curvature contribution from the longitudinal covariance, and equality of all 576 raw curvature covariance entries with the gauge slice obtained by pinning one boundary-root forest edge. It retains the a^-4 factor. The calculation is stored, without changing the existing incidence checker, in scripts/auxiliary-cochains/check.py. Reproduce it from the notebook directory with:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/auxiliary-cochains/check.py
```

The next target changes the observable class to auxiliary/ghost polynomials and requires a justified integration-by-parts prescription. Its separate REVIEW_REQUIRED assessment is drafts/literature/2026-10-03-auxiliary-brst-ward-identity.md. The original SPECIALIZE assessment is unchanged; its covariance target is completed. The current status and exact next action appear only in PROGRESS.md.

Validation: the stored exact check passed. The documentation checker with --problem yang-mills passed with 13 nodes and 22 unique edges. Read-only literature validation accepted the captured prior SPECIALIZE target, unchanged assessment, RESEARCH / REPRODUCTION completion and exact REVIEW_REQUIRED next target. All 26 pre-existing lemma, script and assessment hashes were preserved, and the local whitespace diff check passed. The full proof was checked against the determinant orientation, Fourier sign, point-versus-operator covariance normalization, absence of scalar zero modes, complete relative cell space and the absolute-convergence qualification. No further mathematical target was attempted.
