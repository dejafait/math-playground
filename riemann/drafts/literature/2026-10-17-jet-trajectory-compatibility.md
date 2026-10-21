# Differential-compatibility test: finite-interval source coverage

TARGET: Test whether L423's law violates a leading-order integration-by-parts constraint required of C^2 jet trajectories with x=f, y=f'/L and z=f''/L^2.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 174 searched occupation/Liouville and higher-derivative holonomic constraints, then exact Hardy/zeta-jet occupation terminology; inspected the primary 2008 finite-interval identity and 2023 nonlinear test class/integrability proof. Scoped local comparisons found prior second-moment integration by parts, but no completed nonlinear trajectory separator for L423; no novelty inference follows.
SOURCE_EVIDENCE: Lasserre--Henrion--Prieur--Trelat, SIAM J. Control Optim. 47 (2008), 1643--1666, author manuscript dated 2008-01-30, Sections 2.1--2.3, (2.7),(2.10)--(2.12), manuscript pp. 3--5, and Theorem 2.3(iii), p. 6; Henrion--Korda--Kruzik--Rios-Zertuche, manuscript dated 2023-03-04, Definitions 2.4/2.7, (6)--(8), pp. 3--4, Theorem 3.1 statement, p. 5, and Lemma B.1 with complete proof, pp. 17--18. Primary links and precise scope are below.
COMPARISON: The finite-interval source supplies necessary transport identities with boundary terms; it does not decide the normalized nonautonomous L423 defect. Work directly at each H with a bounded smooth nonlinear state test, retaining the moving L and endpoint terms, instead of importing an unproved weak-limit passage. The preserved second moments already cover the uncut quadratic diagnostic.
GAP: Specialize the cited identity to the ordinary normalized two-coordinate state, bound its complete sharp-endpoint/scaling budget, and test the single Gaussian-damped quadratic test specified below on all L423 components. No specialized identity, vanishing budget, defect, or incompatibility is proved in this literature turn.
REASON: Essential source coverage is now available for one bounded REPRODUCTION attempt. The change from a proposed weak-limit argument to a finite-H identity avoids an unnecessary unproved limit hypothesis; source necessity alone neither rejects the counterlaw nor realizes it by a trajectory.
LITERATURE_REASON: The changed differential target was outside the ready integrated-moment assessments; this turn inspected its essential transport identity and nonlinear integrability cases, completing coverage for a finite-H test without an assumed weak limit.
SCOPE: L423's complete conditional law on sharp [H,2H], actual full response and curvature, fixed k=13,14 mixture and every stated moment tolerance/envelope; real H tending to infinity. Necessary leading-order constraints for real C^2 functions, not equality of a non-Dirac conditional kernel with a deterministic graph at every t. No RH, actual zeta realization or new signed/clipped estimate is assumed.
COVERED_TARGET: Test whether L423's law violates a leading-order integration-by-parts constraint required of C^2 jet trajectories with x=f, y=f'/L and z=f''/L^2.

The main gap remains global mixed positivity; actual capped nondegeneracy,
negative-Bcal clipping and L413's full regulator-error margin remain
unproved. The intermediate target is one necessary differential test,
not construction of a global function or a sufficient sign theorem.
Its plausible downstream use is identifying an actual-jet restriction
that limits the moment-law concentration mechanism. Rejection of this
specific law would not invalidate its selected-information obstruction,
prove a lower bound for actual critical data, or exclude other laws.

Essential inputs for the later comparison are L423 (complete mixture and
support), L421 (high/intermediate components), and L419 (bulk). L405 and
L406 fix the actual ordinary jets and full response conventions. L420's
stopped magnitude certificate and L413's regulator obstruction remain
contrasts, not premises for a new sign claim. The exact derivatives are
taken before division by L=log(2+t); a trajectory constraint must retain
the derivative of L and any explicit time dependence of the test.

Before mathematics, inspect primary statements for integration-by-parts
constraints on occupation measures or weak limits of ordinary derivative
jets. Compare their regularity, growth, integrability, endpoint treatment
and sufficiency/necessity qualifications with this nonautonomous,
height-dependent law. Determine which compactly supported smooth tests,
and which H-dependent rescalings, have controlled errors under the
stated envelopes. A named chain rule alone does not settle passage to
an asymptotic law or its quantitative defect. No formula or new theorem
application is proved in this proposal.

Continue only with a concretely specified necessary test and a defect
threshold exceeding its full endpoint/approximation budget. Retain the
whole law: discarding the high/intermediate components, ignoring the
moving response, comparing incompatible scales or adding unsupported
uniform integrability would not be a separator. Non-Dirac conditional
support by itself is not an obstruction to an asymptotic occupation law.
If all tested constraints are already consequences of the preserved
moments, or if the defect is within the error budget, stop this test
without claiming either realization or incompatibility. Full matching
Mathlib coverage is not checked. Approval and any mathematics belong
to separate later turns.

## Completed source comparison — 2026-10-17, step 174

The preceding proposal is preserved as the pre-review record. This section
supersedes its missing-source status only. No mathematical attempt, lemma,
script or trajectory-realization claim is added in this turn. The main gap,
downstream purpose and independent clipping/regulator gaps stated above
are unchanged.

### Search and local duplicate/failure comparison

Queries actually submitted were: `occupation measures differential
constraints Liouville equation C1 test functions boundary measures optimal
control Lasserre Henrion Korda`; `holonomic measures higher order
derivatives jets integration by parts Young measures necessary conditions`;
the two primary paper titles; `"occupation measures" "higher order"
"derivatives" constraints`; `"holonomic measures" "compact support"
"closed"`; `"Young measures" "uniform integrability" "continuous" Ball
fundamental theorem pdf`; `"Hardy" "occupation measure" derivatives zeta`;
`"zeta" "jet" "integration by parts" distribution`; and `"occupation
measures" "normalized derivatives" "integration by parts"`. The last
three returned no inspected matching zeta-specific separator. Unrelated
hits, including a claimed RH preprint, are not theorem evidence.

The scoped local search used the October-15/16 compatibility assessments
and relevant ATTEMPTS, then the L423 audit assessment and step-172 audit.
The second-moment scope assessment already imports Bui--Hall's parity
formulas and their integration-by-parts provenance. L423 preserves those
six moments exactly. Thus the undamped quadratic comparison alone is not
a new restriction. The full L423 construction through its component and
moment verification, L421's high/intermediate definitions and bounds,
L419's bulk hypotheses and covariance convention, and L405's exact jet
definition were read for applicability. No prior nonlinear trajectory test
was found in these selected records. This bounded comparison says nothing
about novelty outside the sources checked.

L420's magnitude-certificate stop and L413's regulator obstruction remain
in force at their recorded scope. Neither addresses ordinary-derivative
compatibility. Conversely, rejecting L423 by an additional differential
constraint would leave its selected-information obstruction intact.

### Inspected primary statements and essential cases

1. J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat,
   *Nonlinear optimal control via occupation measures and LMI-relaxations*,
   SIAM J. Control Optim. 47 (2008), 1643--1666,
   [DOI 10.1137/070685051](https://doi.org/10.1137/070685051),
   [author manuscript, dated January 30, 2008](https://homepages.laas.fr/henrion/Papers/ocp.pdf).
   Read Sections 2.1--2.3, manuscript pp. 3--5: smooth dynamics,
   bounded measurable controls, compact state/control sets, C^1 tests,
   occupation and terminal measures. Equation (2.12), p. 5, states

       integral (partial_t g + grad_state g . dynamics) dmu
           = g(T,state(T)) - g(0,state(0)).

   This is the required finite-interval necessary identity. Its derivation
   from the trajectory and definitions was inspected. Theorem 2.3(iii),
   p. 6, requires convex velocity images and a convex reduced cost for its
   no-gap conclusion; that conclusion is not imported. The fixed-compact
   weak continuity in Remark 2.1 is not a theorem for expanding normalized
   jet supports.

2. D. Henrion, M. Korda, M. Kruzik and R. Rios-Zertuche,
   *Occupation measure relaxations in variational problems: the role of
   convexity*,
   [March 4, 2023 primary manuscript](https://optimization-online.org/wp-content/uploads/2023/03/convexcov-1.pdf),
   [arXiv record 2303.02434](https://arxiv.org/abs/2303.02434).
   Read Definitions 2.4/2.7 and (6)--(8), printed pp. 3--4.
   Nonlinear tests are additional to affine ones; finite-p measures require
   interior and boundary p-moments. Their F_p class bounds the test and
   time derivative by c(1+|state|^p), and its state derivative by
   c(1+|state|^(p-1)). Lemma B.1 and its complete proof, pp. 17--18,
   justify integrability by Holder for finite p and compact support for
   p=infinity. This is integrability, not uniform integrability or
   convergence for an H-dependent family. Theorem 3.1's inspected
   convexity/affinity hypotheses do not justify realization here.

The relevant formulas were read in the primary PDF text. The first PDF's
optional screenshot failed with a restricted-fetch error; its complete
load-bearing identity and surrounding hypotheses were accessible as text.
This is not a source blocker. Young-measure lectures and holonomic-measure
notes returned by discovery remain unread leads; no weak-limit theorem
from them is imported. No larger passage or no-gap proof is essential for
the finite-interval necessary test selected here.

### Exact later specialization and bounded test

Keep the saved TARGET unchanged. For the later attempt, use the two state
coordinates (x,y) and control z from L405, with ell=log H fixed on each
interval and L(t)=log(2+t). Derive their exact nonautonomous dynamics from
ordinary differentiation before any asymptotic replacement. Apply the
source identity at each finite H. C^2 trajectories have bounded jets on
each compact interval, so the source can be used with an H-dependent
compact box; no uniform box or weak-limit conclusion is licensed. The
L423 states also have bounded support at each fixed H, as recorded in
L421. This is a source-scope comparison, not a claim that they solve the
dynamics.

The single proposed test is

    a=x/sqrt(ell), b=y/sqrt(ell),
    psi(a,b)=a b exp(-a^2-b^2),
    g_H(t,x,y)=psi(x/sqrt(ell),y/sqrt(ell))/L(t).

It is a bounded smooth alternative to a compact cutoff; the cited C^1
finite-box test class permits it without polynomial approximation. The
later proof must verify every derivative bound it uses. Compute the exact
transport expression, keeping derivatives of 1/L and of y=f'/L. Keep both
sharp endpoints. Do not differentiate the third jet, drop a response
derivative, freeze L at ell without an error bound, or assert stationarity
of a limiting law. No C^3 hypothesis is intended.

Evaluate the resulting finite-H normalized defect for the whole L423 law,
including high, intermediate and six-state bulk, the exact covariance
correction, bounded translation and fixed mixed weight. The Gaussian test
changes the observable, not the law or its constraints. Its intended use
is to test a nonlinear restriction absent from the selected moments.
The existing exact second matrix supplies the starting integrability
input; any approximation or passage under the integral still needs its
own bound. The fourth-moment rare mass cannot simply be declared absent
from this different statistic.

The continuation threshold is a nonvanishing order-one normalized defect
along some unbounded sequence, against a proved o(1) complete transport
budget. An explicit defect exceeding the exact finite-H budget on such
heights is equally acceptable. Neither this threshold nor its anticipated
vanishing budget is verified here. If the defect vanishes at the available
precision, follows from the retained constraints, or cannot be separated
from its full error, stop this one diagnostic; do not infer realization
or silently enlarge the test family. A quantitative smaller-scale test
would require its own assessment.

No reproof of either source theorem is needed. Only the normalized
dynamics, endpoint estimates and complete-law defect are local work.
Classify that later attempt REPRODUCTION unless a separately reviewed
target changes its scope. Full matching Mathlib coverage for the
occupation-measure specialization is not checked and is not asserted
absent. Newly completed source coverage receives the supervisor's separate
approval before mathematical invocation.
