# Fixed time-one pairing attempt849

IN_PROGRESS working record, saved before calculation. Assessment847
(completed source review848), SPECIALIZE, covers the exact startup Next
action. This is a REPRODUCTION calculation, not a new sign mechanism.

Main gap: actual-Xi all-degree mixed positivity, L030-L032/C032a.
Intermediate target: one enclosure of C759i's B_1 at t=1, in the
prescribed W=span{v,(1-x^2)P_0,...,(1-x^2)P_508}, even indices.
A strictly negative upper endpoint would exclude time-one cone
preservation; it would not decide the ground state, parity or Xi transfer.
A zero-crossing enclosure or unpaid complete defect ends this fixed test.
No time, pair or space sweep is permitted.

Reused inputs: C759a(1),(5)-(6), C759h Proof1-2 (floor -10,
operator domain and complete action), C759i's exact quartics, and
Jacob-Zwart Lemma10.1.2 as read in assessment847/848. C759k supplies
the exact rho normalization; its unsigned resolvent conclusion is not
a sign theorem. Stop823's triangle residual and stops829/831/838/843
remain preserved. No fresh source search is needed for this scope.

Plan: assemble one finite evolution, keep its defining data, and evaluate
its combined complete defect. Numerical assembly and samples are only
diagnostics unless every quadrature, tail, time and arithmetic error is
paid. Preserve any such failure explicitly; no sampled sign is proof.

## Completed attempt849: uncertified and inconclusive

One fixed256-dimensional approximate Galerkin evolution was constructed;
no space, time, pair or support sweep was performed. The full executable
and complete numerical records are
`scripts/spectral-triples/even-time-one-pair-849.py`, its `.json` record,
and its `.npz` exact-candidate data. Run with
`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 scripts/spectral-triples/even-time-one-pair-849.py`.
The rerun after adding finite-data integrity assertions reproduces the
same candidate and diagnostic numbers; it is not a second attempt.

The binary64 entries in `eigenvalues` and `modal_coefficients` are
interpreted as exact dyadic real numbers, rather than certified
eigenvalues/eigenvectors. With basis ordered v followed by the255
specified polynomials, column j defines f_j and the associated entry
defines lambda_j. The candidate is exactly

    w(t) = v + sum_j (exp(-lambda_j t)-1) f_j.

Thus w(0)=v identically, even though the floating eigendecomposition does
not give an exact modal reconstruction. This finite analytic path stays
in W. C759h Proof2 supplies domain membership; finite linearity supplies
continuity of its complete action. No operator-core or invariance claim
is needed. The method uses the defect identity imported in assessment847,
with A_e>=-10I, and has zero initial error. The exact prospective error
bound and all unpaid certification fields are saved in the JSON record.
This records applicability to a candidate, not a new error theorem.

Assembly uses the polynomial harmonic-number representation of the
singular archimedean term, a finite-part quartic integral, the smooth
remainder kernel, all ten masked translations for n=2,3,4,5,7, and the
even pole action2c<c,.>. That last action represents both poles.
The computation does not use a mismatched r(|x|) in place of rho.
The physical-action representations, finite-part evaluation and all
floating quadratures are diagnostic here; they have not been certified
as approximations to C759h(2). In particular there is no claim that
a spatial sample contains the multiplier's full Fourier tail.

The single candidate gives sampled <u,w(1)>=-0.0018642353578662493.
The combined defect w'+A_e w was sampled BEFORE taking its spatial norm,
on1536 independent spatial Gauss nodes and64 time nodes. With the
proved floor's exponential weight, its sampled scalar error radius is
2.136074339567056. These are not enclosures, lower bounds, or evidence
that every rigorous bound must fail. Even their apparent comparison
misses the negative-center margin by over three orders of magnitude.
No negative trial center has been rigorously enclosed. No full spatial
or Fourier-tail bound, validated time integral, or arithmetic enclosure
was obtained. The record deliberately sets `B1_enclosure` and
`full_defect_bound` to null, rather than presenting sampled endpoints as
a certificate. The fixed test ends under its unpaid-defect stop rule.

There is an additional diagnostic warning: the computed mass minimum
is8.220962687381295e-12, and the unsymmetrized stiffness discrepancy is
4.0732693422825164e-5. Its approximate lowest Ritz value
-0.012686315476673324 consequently gives no sign information about
the full form or spectrum. Symmetrization does not pay these errors.
The raw matrices are preserved in the NPZ, and the exact candidate is
well defined regardless of these assembly defects.

Outcome: EXPLORATION, RESEARCH/REPRODUCTION, actual task calculation.
This is one mathematical exploration attempt and no certified advance
or informative mathematical negative. No new lemma is justified.
PROOF and DAG are unchanged because the assembled mathematical argument
is unchanged. Stops823/829/831/838/843 remain in force with their scopes.
The main gap, sign/simplicity, parity and Xi realization remain open.

## Separate next nomination

No refinement or rescue of B_1 is nominated. A different scalar target
is the complete Rayleigh quotient of the single stored mode f_0. Its
definition is column0 of the exact dyadic modal array, independent of
whether the matrix eigenvalue is accurate. A direct full-form enclosure
can test the apparent negative Ritz indication without evolving any
semigroup, estimating a ground state or assuming a positive resolvent.
The conditional downstream use is either a genuine local negative-form
candidate requiring critical review and exact RH-criterion qualifications,
or evidence that this matrix root is an assembly artifact. Neither
alternative is asserted. The local goal still requires a rigorous actual
off-line zero certificate for a disproof; a sampled negative matrix root
provides none.

The narrow duplicate/failure search in C759*, November13 even-family
assessments and even-family stops found that generic pole-free secular
and pointwise kernel tests were already parked in assessments821/838.
Those do not reopen here. Constant-trial/form coverage in C759a does not
certify this nearly cancelling quartic-polynomial vector. No claim of
novelty follows from the search. The new target has REVIEW_REQUIRED
coverage in `drafts/literature/2026-11-13-frozen-even-mode-form-review-849.md`.
No mathematics on it was derived or approved in this turn.

A justified creative central-gap mechanism is still unavailable: neither
this one pairing nor the ill-conditioned matrix supplies sign, isolation,
parity or actual-Xi transfer. A concrete scalar form check should settle
the new numerical indication before it is used to motivate such a claim.
