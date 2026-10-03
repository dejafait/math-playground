# Research history — 2026-10-03

## Complete parity grouping: an infinite-block negative tail

STEP_ID: 2026-10-03-complete-parity-negative-tail-01.
NEGATIVE; RESEARCH; REPRODUCTION. Reused the ready SPECIALIZE
[parity assessment](../drafts/literature/2026-09-27-first-associated-parity-blocks.md)
and completed its boundary cancellation and Fourier-tail test.
Earlier local unfinished source-review changes and all other
notebooks' work were preserved; no additional literature was read.

[L356](../lemmas/L356-complete-parity-blocks-have-opposite-fourier-tails.md)
proves the complete same-parity block has an eventually negative
first-associated spectrum. It controls the infinite half-sums and
their derivatives directly, includes the modular prefactor, zero
mode and odd characteristic phase, and retains the reflected boundary
terms. The opposite block cancels its leading tail. This gives new
evidence stopping the separate complete-parity certificate, while
the full first Laguerre sign remains unproved. The proof specializes
the standard cusp method already used in L234; the inspected sources
did not supply this full parity-block conclusion, and no originality
is claimed.

An exact recurrence check caught a copied derivative error in L234
and L254: the correct polynomial is −16v³+60v²−30v. Both formulas
were repaired in place, preserving their identifiers and conclusions.
For n≥2 its sign is still strictly negative; the full modular sum of
derivatives still vanishes. Their Fourier coefficients only use these
derivative values abstractly, so their sign and tail conclusions
survive. The corrected formula is also used in L356's strictly positive
boundary constant. Searches found the erroneous copies only in these
two prior lemmas; scripts did not contain that formula.

The [failed-certificate record](../ATTEMPTS/2026-10-03-complete-parity-positive-definiteness-test.md)
preserves the stopping reason. PROOF.md records this limitation;
DAG.md adds only the new lemma's direct mathematical inputs. No
Laguerre sign, nonreal-center exclusion range or endpoint margin is
extended, and no RH candidate appears. STATUS remains IN_PROGRESS.
The informative negative result ends the unresolved exploration
streak; zero of three calculation turns are now used.

The next direction tests a different approximation mechanism:
Gaussian index regulation with explicit Poisson zero-mode subtraction,
aiming for weighted whole-line L¹ convergence before any sign transfer.
This directly addresses L235's mass obstruction. Its changed
hypotheses are recorded as
[REVIEW_REQUIRED](../drafts/literature/2026-10-03-gaussian-regulated-modular-zero-mode.md);
the next invocation must screen that target before calculations.
No regulator calculation is part of this step.

The intermediate reasoning was saved before the full proof in
[the calculation checkpoint](../drafts/2026-10-03-parity-boundary-calculation.md).
Validation: `python3 ../scripts/docs/check_structure.py --problem riemann`
passes with 359 nodes and 815 edges. Metadata checks confirm unique
step fields, reuse of the unchanged ready SPECIALIZE assessment, and
exact matching between the sole Next action and its REVIEW_REQUIRED
assessment; PROGRESS.md has 19 lines and PROOF.md has 100. An exact
standard-library rational-polynomial calculation checks the derivative
coefficients (−30,60,−16) and the opposite Fourier coefficients (−4,4).
`git diff --check -- .` passes. Mathematical input review confirms the
new DAG row uses only the scalar theta identity, actual-kernel bounds,
first-associated Fourier identity and smooth full-boundary cancellation.
No numerical sign certificate or Mathlib lookup is required for this
analytic test.
