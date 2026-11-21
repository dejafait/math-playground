# Direct index recurrence — completed source comparison

TARGET: Review source and recorded-failure coverage for a direct recurrence in n for L966's prescribed Q_eta(n), retaining eta(n)=1/(64*9^n) and the full h charge, and select one bounded induction-or-obstruction test.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step192 searched Li/Keiper recurrences, Chebyshev zero sums, regularized Li recurrences and resolvent monotonicity; read Xiao's exact recurrence and RH-conditional bound, Maslanka's computational recurrence, and the scoped local failures listed below. No inspected source pays the prescribed moving-eta error; search failure establishes no novelty or nonexistence.
SOURCE_EVIDENCE: Xiao arXiv:2006.13103v1, Theorems2.1/3.2, (3.7)-(3.10), pp2-4, Corollary3.3 with complete proof and Conjecture3.4 pp4-5; Maslanka arXiv:math/0402168v5, (3.5)-(3.12), pp5-6; DLMF18.9.1/Table18.9.1 including T_n initial values; L964(7),(9)-(13), L966 complete, L968 proof and scope, L970 statement/audit status. Earlier Cauchy and Li-normalization coverage reused.
COMPARISON: Published Li recurrences give identities with signed forcing or computational formulas; Xiao's small second-difference bound assumes RH and his convexity assertion is a conjecture. None is a sign-propagating recurrence for Q_eta(n) with changing eta. Existing actual-theta heat recurrence and pointwise/angular payment stops do not settle a quantitative moving-eta estimate.
GAP: Pay the changing-eta error independently before attempting scalar sign induction; fixed-eta signed forcing, initialization at all required indices and sufficient induction margins remain open. No prescribed-Q recurrence or error bound is established in this turn.
REASON: Essential source comparison is complete. Select one bounded moving-eta loss test at fixed polynomial index using existing geometry/Cauchy inputs, rather than import RH-conditional convexity or repeat the stopped angular/heat mechanisms. Its separate ready assessment is newly written and requires separate next-turn approval.
LITERATURE_REASON: The startup recurrence target was REVIEW_REQUIRED; earlier ready assessments cover representation, detection and prefix audits, not propagation across eta_n and eta_(n+1).
SCOPE: Completed literature-only source comparison. SPECIALIZE covers only the tools for the nominated moving-eta component test in the separate assessment; no full induction, positivity theorem, new recurrence derivation, lemma or mathematical script is approved here.

The original nomination below is retained as historical scope. Its
source comparison is now completed by step192, recorded after it.

Essential starting inputs are L966's complete Q_eta(n), L964's relation
to Li signs, and L968's downstream implication; L970's n=2 certificate
is at most a proposed base input and requires its own audit status to
be checked. These latter proofs were not loaded in step191 merely to
prepare this nomination. Eta changes with n: an identity only for fixed
eta, an omitted h term, or an unsigned remainder does not establish
sign propagation for the prescribed sequence.

The plausible downstream use is an induction with positive initial
values and a fully paid signed error, which would bypass the failed
angular-prefix allocation. Neither such an induction nor its required
coefficients are asserted. A useful source turn should select one
finite algebraic recurrence/obstruction test with an explicit success
criterion, or explain why known obstructions rule this mechanism out.
No lemma, script, altered radius/onset, new finite-Q certificate,
RH assumption, zero data or cross-notebook input is authorized by
the original nomination. All-index positivity remains unresolved.

## Completed comparison — step192, 10 November 2026

The main gap is L966(16), R_n<=N_n for every index; L968 makes that
condition sufficient for RH but supplies no sign. The intermediate
target selected here pays just the change of regularization parameter,
with a proposed uniform loss threshold A/8 for one fixed reciprocal
mass bound A. This could make one error in a later index recurrence
manageable. It leaves the recurrence's fixed-parameter signed forcing
and adequate induction margins wholly unresolved. No such loss bound
has been derived, tested or accepted in this source turn.

### Primary recurrence evidence and exact limitations

H. Xiao, *Recurrence relations of Li coefficients*,
[arXiv:2006.13103v1, 23 June 2020](https://arxiv.org/pdf/2006.13103v1),
Theorem3.2/(3.10), p4, states for ordinary Li coefficients and n>=3

    lambda_n=2 lambda_(n-1)-lambda_(n-2)
              -sum_rho rho^(-2)(1-1/rho)^(n-2).

Read its derivation (3.1)-(3.10), pp2-4: reflection pairs actual zeros,
and the Chebyshev argument retains rho(1-rho), rather than ordinates.
Theorem2.1, p2, is a first-difference identity with another unsigned
zero sum. Corollary3.3, pp4-5, bounds the absolute second difference
by 2+gamma-log(4pi) **under RH**; its complete proof uses
|1-1/rho|=1. Conjecture3.4, p5, asserts strict convexity rather than
proving it. None signs the recurrence forcing unconditionally or
handles changing eta. Use the theorem's explicit zero-sum normalization;
the introductory Keiper generating series uses a different normalization.
No source convergence shortcut replaces the local absolute-sum checks.

K. Maslanka, *Effective method of computing Li's coefficients and
their properties*, [arXiv:math/0402168v5, 2 June 2004](https://arxiv.org/pdf/math/0402168v5),
(3.5)-(3.12), pp5-6, gives power-series recurrences for auxiliary
coefficients and a finite binomial expression for the oscillatory Li
part. Its gamma_n are Laurent coefficients in the convention (3.5),
not the unscaled Stieltjes constants; (3.8) divides by m*gamma_0.
Read the coefficient-extraction setup and both subsequent conversion
formulas. These are computational identities, with signed terms and
additional input coefficients, not an all-index positive recurrence
or a bound for this regularized observable. No numerical table or
asymptotic fit from this paper is used as a theorem.

[NIST DLMF18.9.1 and Table18.9.1](https://dlmf.nist.gov/18.9.i)
give T_0=1, T_1=x and T_(n+1)=2xT_n-T_(n-1) for n>=1;
the table retains A_0=1 rather than 2. The displayed real-variable
identity extends to complex arguments as a polynomial identity, but
its negative preceding-order coefficient supplies no positivity.
This is a standard imported identity; no reproof is needed. The
regularization and summation specialization would be separate work.

### Reused coverage, duplicates and failure screen

Reuse the already adequate analytic-tool coverage in
[step164](2026-11-10-regularized-li-theta-representation-review-163.md)
and Li normalization/actual-complex-node cautions in
[step159](2026-11-10-li-negative-margin-mixed-transfer-review-158.md).
The latter's inspected Mazhouda-Smajlovic result forbids replacing
actual nodes by ordinates without the RH-equivalent hypothesis.
L964(7),(9)-(13) already gives the paired identity, analytic disk bounds
and a one-sided comparison to lambda_n at a single eta. L968 applies
that comparison to the prescribed family. Neither is a comparison
between two eta values at fixed polynomial index. Do not subtract
one-sided inequalities to obtain a new one-sided bound.

L966's full proof retains the distant-h subtraction and absolute
convergence at each finite n. Its positive coefficients and positive
theta moments sign neither its logarithmic combination nor its n-step.
L040 is an existing signed Newton recurrence; deriving it again would
duplicate work. L044/L046 were read in full: ordinary moment Gram
positivity and termwise log-concavity do not remove logarithmic/variance
corrections. Their model conclusions are not actual-Xi counterexamples.

The recorded L967 boundary-spreading stop and L971 complete-prefix stop
were read in ATTEMPTS/2026-11-10-li-theta-boundary-spreading-stop-168.md
and ATTEMPTS/2026-11-10-complete-bell-reflected-prefix-stop-189.md.
Do not repeat their payment rules or shift their onset. Reuse the
step140 theta-heat recurrence comparison and its stop record: L874's
contact equation has an unpaid top coefficient and theta response;
Jacobi heat uses another parameter. This nomination concerns movement
of the regularizing denominator at a fixed polynomial index, not
another heat-contact or angular-prefix propagation argument.

L970's statement explicitly records its independent step186 audit.
It is an available n=2 base candidate, contrary to the stale overview
label, but is not needed for the selected parameter-loss estimate.
No new finite-Q sign or audit was performed. No PROOF/DAG edit is
needed because the mathematical argument has not changed.

### Bounded test selected, without deriving its outcome

Use the exact proposed test and hypotheses in
[the moving-eta assessment](2026-11-10-prescribed-q-moving-eta-loss-review-192.md).
Hold a_n fixed and compare Q at eta_n and eta_(n+1); retain every
node/multiplicity and both resolvent charges if that representation
is used. Seek a uniform lower bound -A/8 on the entire difference.
This is an induction-component test, not a proposed sign recurrence.
It is useful even if independent signed-forcing gaps remain.

Continue only with the complete bound, or a rigorous obstruction
showing the selected threshold fails. An n-dependent exponential loss,
omitted charge, assumed Stieltjes law or fixed-eta identity does not
meet the threshold. A finite sign check cannot certify the uniform
claim. Success would pay only parameter movement; accumulation of
losses still needs an independently proved induction margin.

### Search and access record

Queries used included `Li coefficients recurrence relation xi coefficients
Li 1997 criterion recurrence`, `Keiper Li coefficients recurrence
Chebyshev regularized resolvent positivity`, `Li coefficients regularized
eta Chebyshev recurrence positivity`, `"Q_eta" "Li" recurrence`,
`"Li coefficients" "regularization" "recurrence"`, and
`"Li coefficients" "resolvent" eta monotonicity`. Narrow local searches
used Li/recurrence, resolvent identity, Xiao/2006.13103 and Chebyshev
within relevant literature and attempt records. No exact matching
theorem was inspected; this is not a novelty claim.

Connon arXiv:0902.1691 was screened at its introduction and selected
Section3 search passages only; its long Stieltjes recurrence is an
unused lead, not theorem evidence. Coffey's previously inaccessible
theta-Laguerre paper remains parked; the bounded parameter comparison
does not depend on it. DLMF TeX endpoints failed, but the complete
displayed recurrence/table was accessible and read. There is no
essential source blocker for the selected test. No external unreviewed
RH claim, API key, cross-notebook input or new mathematical script is
used. Full matching Mathlib coverage is unchecked and unknown.

Outcome: EXPLORATION, LITERATURE, NOVELTY_UNCHECKED. Source coverage
now selects an independently testable component; no new mathematical
result or progress beyond the inspected sources is claimed. The newly
written continuation receives a separate approval next turn.
