# Fixed-c quadratic input audit — working record

STEP_ID: 2026-10-31-family003-l554-quadratic-audit-01

The approved target is the four-term evaluation for c=p or pq, with
distinct good primary primes outside fixed S containing the primes above
6. Reuse the saved SPECIALIZE assessment. Main gap: actual-Xi all-degree
positivity. Downstream use: discharge only L554's quadratic input in its
coprime reciprocity step. Continue only if the character, measure, branch,
normalized limit and four-class table all match; otherwise record the
failed factor/limit and restrict or repair the application.

Read the complete pinned source proof at lines 772–859 and its use at
899–927, plus conventions 557–566. Relevant local L554 proof and prior
audit notes retain this input explicitly; no completed duplicate was
found. L547/L548/L553 conventions and hypotheses were checked narrowly.
Unrelated existing edits are preserved. No cross-notebook input.

Initial checkpoint: the real bilinear pairing is B(z,y)=2 Im(zy)/sqrt(3).
In the basis (1,omega) its Gram matrix is [[0,1],[1,-1]], so the
annihilator is O, with no conjugation. The lattice covolume is sqrt(3)/2
in dx dy and one in dmu. For c=rho exp(i theta), rotate
z=exp(i theta/2)(u+iv), y'=exp(i theta/2)y. Then the Gaussian matrix is
M=[[epsilon,-i k],[-i k,epsilon]], k=4/(sqrt(3)rho), and the real
frequency is (2/sqrt(3))(Im y',Re y'). Its eigenvalues epsilon +/- i k
have positive real part. The determinant branch and inverse computation,
coset means, all replacement errors and finite classes still need to be
written out before a verdict. No uniformity in c is being attempted.

Completed: L555 contains the full proof and precise analytic imports.
The character/measure conversion, positive determinant branch, all coset
means and three normalized replacement errors pass. The errors after
division by I_epsilon are O_c(epsilon^2), O_c(epsilon^2), O_c(epsilon),
respectively. The twelve unit residues form the four asserted classes;
the table and symbolic all-sixteen-pair correction match exactly.
No mathematical script or numerical evidence is needed for these exact
checks. L554 now uses this result only on p and pq, defining its finite
class function separately at the other representatives.

Outcome: ADVANCE / REPRODUCTION, meaning a locally retained source
premise has been verified, not a result beyond the cited manuscript.
No other Gauss identity or all-height positivity input has been proved.
The new cubic Jacobi-sum continuation is explicitly REVIEW_REQUIRED;
no mathematical work on that target was performed. All original
unrelated changes and the former conditional-review record are retained.

Validation: `python3 ../scripts/docs/check_structure.py --problem riemann`
passes (578 nodes, 1457 unique edges, acyclic, complete file coverage,
valid local links, compact overviews). The first check found only an
overview byte excess; the changed summary phrase was shortened, with
all hypotheses and proof retained in L555. Scoped `git diff --check`
also passes. Mathematical edge review: L554 adds L555; L555 uses only
the named standard analytic imports and elementary calculations, with
no dependency on the presentation it supports.
