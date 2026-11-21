# Fixed-collar actual quartic attempt1925

Approved exact target: Test actual degree-four cubic/quartic matching on B=[-1/4,1/4]x[3/4,5/4] by one interval range/Krawczyk evaluation per affine orientation, using unchanged L917/L037 moment boxes and no site or radius sweep.

Research/calculation, REPRODUCTION under unchanged SPECIALIZE assessment1924.
Main gap: L030-L032/C032a actual-Xi all-degree positivity and C028b's
unpaid H_d=o(d). A finite match could remove two degree-four residuals;
it would leave other degrees and uniform full costs unresolved.

Read full source-notes1924 and relevant canonical construction and
coefficient conventions C028a/d/h/q/t, L917's containment and audit197,
L037, and the audited point producer/checker. Complete selected raw
panel0 endpoints I_0,I_2,I_4,I_6,I_8 inspected with the JSON inspector.
Only the already assessed moment/Newton construction and Rump13.3
will be specialized. Actual roots are formal, with empirical division4;
reference moments have no factorial conversion. Both orientations share
the unchanged actual intervals. No source refinement or solver is allowed.

Plan: collect the finite Cramer polynomials and derivatives exactly;
recompute the point Jacobian and its rational midpoint inverse; make one
natural interval evaluation on the prescribed collar. Record every
division. Strict Krawczyk containment would prove a conditional solution;
range exclusion of both signs would exclude only this collar. An unpaid
divisor or failed sufficient test is inconclusive and ends the attempt.

## Completed finite calculation, inconclusive

Producer: `scripts/heat/two-site-actual-collar-1925.py`; full evidence:
`scripts/heat/two-site-actual-collar-1925.json`. Independent replay:
`scripts/heat/two-site-actual-collar-check-1925.py` and its JSON.
The calculation made one whole-collar Cramer evaluation, shared by both
orientations because the Gram divisor is independent of orientation.
It stopped before dividing by its zero-containing determinant interval.
No residual range or Krawczyk inclusion was evaluated on the collar.
No subsequent representation, subdivision, radius or source refinement
was tried. Point derivatives and their midpoint inverse were recomputed.

The full determinant interval is

    [-438269648433368794543018463498687592783409986321/10^50,
      332483056580617137275351700964754866217649303471/(5*10^49)].

Thus it lies strictly inside [-4383/10^6,6650/10^6] but contains0.
Required: exclude0 before division (a positive lower bound suffices).
Actual determinant positivity follows from the positive Gram measure;
this natural polynomial enclosure fails to retain that positivity.
It is not a counterexample or nonmatching certificate. Both orientations
are explicitly recorded as `inconclusive_unpaid_collar_divisor`.

The independent check passes19,685 checks on all6,530 expression nodes,
the15 complete determinant/derivative polynomials, result copies,
input provenance and both exact midpoint inverses, with no failures.
It uses dual permutation expansion instead of the producer's Laplace
expansion followed by differentiation. This checks finite arithmetic
and symbolic collection, not Decimal correctness or a nonlinear solution.

## Canonical record

Full finite coefficient identities, affine/Newton equivalence, source
citations, hypotheses, complete failed enclosure and arithmetic inclusion
argument are canonical in C028u, with Mathlib coverage explicitly unchecked.
This draft retains only the attempt's working state and continuation.
C028u records a reproduction and enclosure limit, not matching or a new
mathematical discovery. PROOF is unchanged; DAG adds only C028u's direct
input IDs. L917/L037 containment and Decimal-library correctness remain
assumed. All-degree signs, outside-collar matching and uniform full costs
remain unresolved.

Continuation nomination: a positive two-atom Uvarov kernel update could
avoid cancellation in the same Gram determinant. Its exact source scope
and usable full-collar derivatives must be assessed separately before
any changed calculation. This is a proposed representation change,
not an approved refinement or a central creative mechanism.
