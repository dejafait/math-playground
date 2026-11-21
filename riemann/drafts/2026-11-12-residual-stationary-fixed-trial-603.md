# One residual-stationary fixed trial603 — inconclusive implementation stop

Invocation-start gate: assessment601, separately approved602, SPECIALIZE.
The exact approved target is its TARGET. Preserve stops598/600. This is
one REPRODUCTION calculation, not a global optimization theorem.

Main gap: L030-L032/C032a actual-Xi positivity. The intermediate target
is the joint2044 .000999 comparison for one exact-neutral finite middle
map. It could pay finite head/band cross terms. Higher endpoints, C744q,
H2, neutral-core/c_* verification, non-neutral coverage and global
assembly remain independent.

## Finite-surrogate derivation and saved-trial interpretation

Use exact neutral Z and the unchanged operators/reference from C999q(2).
For constructing a proposal ONLY, put bars over the saved real dyadic
centers: A=Z^t M Z, P=[TZ,T*Z], B=Z^t P, V=LZ restricted to
outputs0:65535. In this paragraph these letters denote the finite center
data, not certified exact analytic operators. Let W be the finite block
weight: a symmetric saved dyadic approximate inverse for the reference
head, and the directed saved diagonal majorants on512:65535. This is a
fully specified finite surrogate; the actual R inverse is verified later.

For a real map Y the surrogate is

    Fbar(Y)=E0-B^tY-Y^tB+Y^tAY-(P-VY)^tW(P-VY)
           =E0-P^tWP-D^tY-Y^tD+Y^tCY,
    C=A-V^tWV, D=B-V^tWP.

For each real endpoint vector x, differentiating x^tFbar(Y)x in direction
Delta gives 2(Delta x)^t(CY-D)x, since C is symmetric. The trace over
all endpoint basis vectors therefore has derivative
2 trace(Delta^t(CY-D)); its stationary equation is CY=D. Equivalently
CY=D makes the derivative of the entire matrix vanish. No sign of C,
attainment, concavity, uniqueness, or optimum is asserted. The finite
matrix products and single unregularized linear solve are numerical
proposals for this equation; no accuracy of that solve is needed for a
fixed-witness application. A failed/singular proposal ends the attempt.

Save the returned binary64 Y once: its entries are exact dyadics. The
trial in the analytic comparison is g=Z_exact Yx; neither physical
coefficients nor the moment completion are rounded. C999q(2) applies
to every such finite neutral strong trial. In particular there is no
unknown-Galerkin correction and no transfer of old predictor norms.

## Bounded decision and verification obligations

Recompute all norms, full signed trial energy, actual Dg, both T
orientations, rational head action, every finite residual row, six tail
functionals and entire n>=65536 remainder. Reuse C999q Sections2/4/5
only for formulas and source contracts, never their numerical totals.
Verify the entire2044-square Hermitian lower matrix at .000999, paying
all coordinate/Gram/assembly/factor errors. Complex endpoint vectors
remain independent. A fully paid success needs a later critical audit.
Failure of a sufficient certificate is inconclusive and ends this single
trial without regularization, pseudoinverse, parameter sweep or tuning.
An actual enclosed violating direction would reject only the saved map.

This partial record is saved before the lengthy calculation. Full matching
Mathlib coverage is unchecked. Inherited analytic-response, IEEE754 and
directed Decimal, whole-neutral-core and unreplayed c_* assumptions stay
in force. No cross-notebook mathematical input is used.

## Completed attempt and exact limitations

Outcome EXPLORATION / RESEARCH / REPRODUCTION. This is a new bounded test,
not a route-changing mathematical negative or a new established input.
The original partial record above is preserved. No new lemma or argument
in PROOF/DAG is asserted. Standard quadratic differentiation is the
specialization covered by Boyd--Vandenberghe--Nobel, EE364a *Convex
functions*, slides3.9-3.10 and *Unconstrained minimization*, slides9.2-9.3,
as inspected in source notes601. No optimizer theorem is invoked; its
additional hypotheses were deliberately not used. General inverse order
and strong-trial applicability remain precisely those cited in C999q
Hypotheses and Proof Section1, especially (2), without reproof.

The source `scripts/separation-seven/residual-stationary-fixed-trial-603.py`
made exactly one unregularized1022-by2044 solve after accumulating every
raw output0:65535. It saved its free coordinates once, in
`scripts/separation-seven/residual-stationary-fixed-trial-proposal-603.npz`.
Its SHA256 is
`f61fc5dddfad8bceb77000939596570c2c3496b8f15a6327891a17f38d3e5a7a`.
The proposal includes all free coordinates, finite surrogate coefficient
matrices, weights and complete row partition; the JSON records the digest
of every generated raw row. No solver residual is promoted to a proof.

The verifier recomputed the exact-neutral coordinate intervals and new
norm factors. It then stopped at its prescribed head-action error budget:

    ||Y|| < 1.315101,
    ||Y||_F < 11.760592, ||Z_center Y||_F < 11.761085,
    ||rho_head,center||_F < 7.491115,
    ||X_head,proposal||_F < 1.535745,
    e_head = ||rho_head,center||_F
               (||rho_head,center-H_center X||_F
                + 1e-8 ||X||_F + 1e-6)/.239999 + 1e-6
           < .000032692462,
    prescribed gate: e_head < .00001.

The selected complete80-digit value is in `/bounds/head_inverse_matrix_nuclear_error`
of `scripts/separation-seven/residual-stationary-head-stop-replay-603.json`.
Its lower interval endpoint also exceeds .00003269246198. These endpoints
enclose the computed UPPER error estimate; they do not lower-bound the
actual head error. Thus exceeding this gate does not establish failure
of the desired .000999 comparison. In particular it is an overly tight
implementation allowance inherited from598, not a necessary mathematical
threshold. No improvement of the allowance or tuning of the saved trial
was attempted after this stop.

The head replay preserves the first-pass script, JSON, factors, log and
single saved proposal. It recomputes only the stopped head calculation
and checks its full supporting arithmetic, rather than resuming the
remaining outputs. Full factor reconstruction errors are <1.085e-8 for
the new predictor norm and <1.157e-8 for the reference head, each below
the1e-6 allowance. The predictor's1e-6 norm inflation is separately
checked to pay both the factor error and new Gram rounding. The actual
head inverse error follows from H>=.239999I and its complete equation
residual, not accuracy of the library solve. H_center assembly, row-map,
head-equation and head-product matrix/nuclear arithmetic budgets all pass;
the full values, required allowances and input hashes are saved in the
replay JSON/NPZ. The nuclear product budget uses sqrt(2044) times the
Frobenius product error, so the matrix allowance also controls trace.
Its interval-arithmetic replay has no failures.

This covers the numerical head center and its inverse action, not yet
the analytic error of the full residual or a uniform trial-energy bound.
Outputs1024:65535 were computed for SELECTING the candidate only; their
independent residual covariance/analytic verification was not executed.
The six infinite-output functionals, suffix debt and final2044-square
comparison were not evaluated. The unexecuted code is not evidence.
No finite signed comparison, actual violating direction, complete
infinite-output certificate, or joint .000999 floor was established.

Reproduction, from the notebook (the first command intentionally refuses
to overwrite an existing saved proposal; use an isolated copy of its
pinned inputs for a fresh first-pass reproduction):

    OPENBLAS_NUM_THREADS=4 python3 scripts/separation-seven/residual-stationary-fixed-trial-603.py
    OPENBLAS_NUM_THREADS=4 python3 scripts/separation-seven/residual-stationary-head-stop-replay-603.py

First-pass JSON/NPZ/log have basename `residual-stationary-fixed-trial-603`;
the replay has basename `residual-stationary-head-stop-replay-603`.
Complete selected proposal, bounds, arithmetic and factor values were
inspected using the shared JSON inspector with `--full`; previews were
not used as sign evidence. Input hashes are preserved and checked.

## Route decision

Park this bounded fixed-map calculation without tuning, preserving598,
600 and this implementation stop. A fresh more permissive arithmetic
allowance would not itself be new mathematical evidence or establish the
uniform target. The repeated finite-comparison certificates have not
closed the finite mixed gap; this turn does not prove their infeasibility.

A materially different next question is source coverage for a quantitative
high-endpoint finite-section reduction of the complete normalized
C744z(4) operator. This addresses a still independent unbounded-endpoint
gap, instead of another optimizer or enclosure variation. It is a
REVIEW_REQUIRED nomination only: no compactness, rate, new inequality or
finite-to-infinite implication is proved here. A qualitative theorem
without a usable remainder is insufficient. Known source gates and the
need for actual signed finite-head control remain. No justified central
creative mechanism is ready; the new analytic scope needs sources first.
