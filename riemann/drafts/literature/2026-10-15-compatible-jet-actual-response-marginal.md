# Prescribed actual response and uniform height: completed source comparison

TARGET: Test whether L416's full moment list permits joint-sign avoidance when the height marginal is uniform on [H,2H] and all response coordinates and jets equal their actual values at that height.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 150 compared L414/L415/L416, their scoped October-15 failure records and step-138/142/146 coverage; searched prescribed-marginal/support-constrained moments, Young measures, purification and exact Hardy/discriminant terminology. Inspected the primary selection/purification statements and proof cases below; no inspected theorem decides this particular feasibility question and no novelty is inferred.
SOURCE_EVIDENCE: Read Jaskiewicz--Nowak arXiv:1712.07577v1 as delivered, Section 2, Theorem 1, hypotheses, Lemma 1 and proof, PDF pp. 2--4; Aumann, J. Math. Anal. Appl. 12 (1965), Theorems 1--4, Proposition 2.1 and relevant proofs, pp. 1--8. Reuse the existing exact moment and weak-duality coverage in steps 138/142/146; finite atomic replacement alone does not preserve the marginal.
COMPARISON: Purification retains a prescribed atomless base measure and finitely many integrable signed observables of an existing supported kernel; measurable selection does not supply prescribed moment values. L416's fixed-height, freely chosen response construction is outside the strengthened scope. No source licenses converting its atoms into the actual response graph without a new feasibility argument.
GAP: Construct one measurable conditional critical-jet law over the exact actual height/response graph satisfying the complete list, or exhibit a pointwise separator with an integrated gap surviving all allowed errors; neither alternative is established here.
REASON: Essential coverage now supports one bounded mathematical feasibility attempt. The new work is the prescribed-response construction or robust obstruction, not a reproof of selection, purification or the existing zeta moments; no such mathematics was performed in this literature-only step.
LITERATURE_REASON: The uniform height law and exact response graph were explicitly excluded from earlier ready assessments; this turn assesses that changed coupling and reuses the existing moment sources.
SCOPE: L416's existing moment list and qualitative bounds, with t uniform on [H,2H] and (a,h,v_0,v_1,v_2) fixed to the actual response at t; only the critical triple remains conditional model data. No critical first moments, finer even-second-moment coefficients, single global critical function or regulator conclusion.

The proposal below is retained as the step-149 startup record. Its pending
source language is superseded by the completed step-150 comparison below;
its target, thresholds and limitations are unchanged.

## Relevance and discriminating test

The main gap is actual negative-Bcal clipping and L413's full-error,
regulator-scale margin toward global mixed positivity. The intermediate
target fixes the complete response to its actual height with the actual
uniform height law. This changes a physical coupling rather than increasing
a finite scalar moment list. Its downstream use is to determine whether
this response information distinguishes the desired joint sign from L416's
relaxed obstruction.

After separate approval, the test is either a law meeting every constraint
and avoiding the joint sign, or an error-robust consequence excluding all
such laws. Failure of one conditional ansatz is not separation. Preserve
L416 regardless: its hypotheses allow the freedoms now removed. If no
justified implementation emerges, record that limitation without assuming
actual critical-jet realization or repeating the stopped unchanged-list
implication or the step-99 blocked signed-clipping source search.

## Inputs and obligations for the separate review

Reuse L416 and audited L414/L415 for the exact list and scales; L389 and
the step-146 Bui--Hall coverage for the six ordinary-jet second moments;
L369 for the first Bcal mean; and L410's constants. Retain the
L367/L368/L370/L390/L393/L401/L405/L409 physical-response, curvature and
mixed-moment scopes. Actual response coordinates mean those in L414's
auxiliary actual-height pushforward; response jets mean the exact ordinary
envelope jets with divisors applied after differentiation. The review must
identify their precise local formulas before calculation.

Search precise terminology for prescribed-marginal/support-constrained
moment feasibility and conditional laws. Compare any inspected theorem
against the noncompact critical variables, fixed bounds, signed coordinates
and asymptotic errors here. A general moment theorem or conditional atomic
replacement is not an existence proof. Reuse adequate primary statements;
retrieve only essential new hypotheses and proof cases. Do not infer novelty
from absent search matches.

Preserve all six second-moment tolerances, both first means, cubic tolerance,
all 23 quartic coefficients, both absolute power-three bounds, exact
curvature, response lower bound and one set of constants/onset for all
sufficiently large real H. Measurability and marginal compatibility cannot
be replaced by finite atomic support at arbitrary heights.

Actual critical/global realization, actual clipping, regulator margin,
common-zero upper counts and global positivity remain unresolved even if
a stronger relaxed law exists. This proposal asserts no new mathematics,
source approval or RH consequence. Full matching Mathlib coverage has not
been checked.

## Completed comparison — 2026-10-15, step 150

LITERATURE / NOVELTY_UNCHECKED / literature_comparison; outcome
EXPLORATION. This supplies source coverage and a precise later test,
not a feasible law, separating inequality or new zeta result. No lemma
or mathematical script was modified or run. PROOF.md and DAG.md have
no mathematical change to record.

### Exact prescribed graph and retained information

Use the actual functions and conventions already defined in L366 (1),
L368 (3), L369 (4), L390 and L401. For t in [H,2H], put

    s=1/4+it/2, p=t^2+1/4,
    Q=p Gamma(s) pi^(-s), A=|Q|, R=Q/A,
    Z=zeta(5/2+it), b=-s(s+1/2)/pi,
    a(t)=Re(RZ), h(t)=Im(RZ), G(t)=Re(QbZ),
    v_j(t)=(G/A)^(j)(t)/(T(t)^2 L(t)^j), j=0,1,2,
    T(t)=1+t, L(t)=log(2+t).

These are imported local definitions, not new formulas proved here.
The j derivatives in v_j are taken BEFORE division by T^2 L^j;
in particular this is not the derivative of G/(A T^2). Convert v_j to
V_j with L414's exact product rule, retaining alpha=A'/A and
q=(log A)''. The free conditional coordinates remain X=(x,y,z).
All P_j, ell_F, Ccal, Bcal, Delta and omega are exactly L414's
polynomials evaluated at this same t and this actual response.
No independent replacement of R, b, Z or their derivatives is allowed.

The desired law is expressed as dt/H times a measurable probability
kernel nu_(H,t)(dX). Its support must lie in L414's pointwise bounds
and {Delta<=0 or Bcal>=0}, with the above response fixed. This is a
specification of the saved problem, not an asserted existence result.
One can also work directly with a measurable conditional finite mixture;
its weights must sum to one for almost every t. No atomic replacement
of the height variable is permitted. Altering a conditional critical
triple does not assert that it is the jet of one global function.

Retain L414's (1), L415's first Bcal constraint, and L416's (1),
with L410's exact constants and the full L401 matrix. In particular:

- Four even raw second moments have O(1) errors; the two odd entries
  have errors O(H^(-2/3)ell^(-1)) and O(H^(-2/3)ell^(-3)).
- E Delta=-a_* ell+o(ell), and E Bcal=-zeta(3)/(4pi)
  +O(1/ell+H^(-1/2)ell^2), where ell=log H.
- E(Delta Bcal)=beta_* ell^2+o(ell^2); preserve the square moment,
  Delta Bcal^2 and all 21 matrix entries at their stated quartic scales.
- Retain E|Bcal|^3=O(ell^(9/4)), E U^(3/2)=O(ell^(9/4)) and
  E U^2=O(ell^4), as well as all pointwise envelopes, response errors,
  annulus and strict Ccal lower bound.

The exact first-mean equalities in L416's construction are stronger
achieved properties, not additional required constraints. Do not add
critical first moments or specified coefficients inside the even O(1)
errors. Every constant and one onset must work for all sufficiently
large real H, not just a selected sequence. An enlarged qualitative
bound constant may be fixed once, as permitted by L414; it may not grow
with H. The actual response itself cannot be calibrated or enlarged.

### Inspected primary theorems and qualifications

Anna Jaskiewicz and Andrzej S. Nowak, *On a generalization of the
Dvoretzky--Wald--Wolfowitz theorem with an application to a robust
optimization problem*, [arXiv:1712.07577v1](https://arxiv.org/pdf/1712.07577v1),
Section 2, Theorem 1, pp. 2--4. The delivered PDF carries the v1/20
December 2017 arXiv header and a June 23, 2021 title-page date; this
assessment identifies the delivered text, without resolving that metadata
difference. Hypotheses: complete atomless probability space, Polish
action space, nonempty measurable-graph allowable-action correspondence,
finite measurable real observables absolutely integrable under a given
supported kernel, and no atoms relative to the conditioning sigma-field.
The conclusion is a measurable pure selection preserving the conditional
expectations. Lemma 1 and the proof first place each kernel barycenter
in the ordinary convex hull, measurably select a Caratheodory mixture,
then use an atomless partition. Read all these cases; import without
reproof. For this target use only the trivial conditioning sigma-field
on the completed uniform-height space, not conditioning on the entire
height sigma-field. Thus the result can preserve finite unconditional
moments of an already feasible kernel while retaining the base measure;
it does not manufacture that kernel or its moment values.

Robert J. Aumann, *Integrals of set-valued functions*, J. Math. Anal.
Appl. 12 (1965), 1--12,
[DOI 10.1016/0022-247X(65)90049-1](https://doi.org/10.1016/0022-247X(65)90049-1),
[primary PDF](https://econweb.ucsd.edu/~rstarr/201/Aumann%20Journal%20of%20Mathematical%20Analysis%20and%20Applications%201965.pdf).
Read definitions and Theorems 1--4, pp. 1--2, Proposition 2.1 and
Theorem 2's proof, p. 3, Theorem 3's proof/counterexamples, pp. 4--7,
and Theorem 4/Proposition 4.1's proof, pp. 7--8. The integral is convex;
nonempty Borel graphs with an integrable bound admit integrable
selections. Convexification preserves the integral under the stated
nonnegativity hypothesis, also with an integrable one-sided bound;
closed integrably bounded values give compactness. These qualifications
matter for signed observables: no unrestricted unbounded signed
convexification or closure claim is imported. A measurable selection
alone does not meet specified moments. Fixed-H bounded envelopes can
support an application, but cannot supply uniform-in-H moment errors.
No reproof or application yielding new feasibility is made here.

For a later purification application the allowable actions are the
critical triples in the prescribed support. Verify its graph and
nonempty fibers and absolute integrability for the proposed kernel.
The finite observable list can be the 35 nonconstant coordinates in
L416's full list: Delta, Delta^2, Delta Bcal, Delta Bcal^2, |Bcal|^3,
the 21 Delta omega_i omega_j, U^2, U^(3/2), Bcal and the six second
moments. Its integrals, not merely formal leading terms, are what a
purification theorem preserves. The constant coordinate is redundant
for a probability kernel. No theorem here supplies conditional moment
values at each height; those are not constraints of the saved target.

### Reused coverage, duplicate/failure checks and unused leads

Reuse the precise primary inputs in the step-138 assessment
`2026-10-15-jet-supported-moment-feasibility-review.md`, step-142
`2026-10-15-compatible-jet-first-linear-mean.md`, and step-146
`2026-10-15-compatible-jet-second-moment-scope.md`. The last assessment
covers Bui--Hall, arXiv:2304.05178v1, Introduction equation (1) and its
odd-order companion; L416 already supplies the sharp weighted
specialization. No changed zeta-moment hypotheses require a fresh
extraction. Earlier coverage behind L389/L390/L393/L401/L405/L409
continues to cover the same unconditional integrated moments.
These sources do not give conditional independence or conditional
critical-jet moments given the response; neither is needed to state
the present feasibility problem and neither may be assumed in solving it.

Bayer--Teichmann Corollary 2 remains a conditional finite-coordinate
replacement theorem. The existing step-138 assessment explicitly
excludes preservation of a continuum of marginal constraints; do not
reuse its global 29-atom conclusion here. Bertsimas--Popescu weak-duality
coverage remains usable for a proposed pointwise inequality; do not
assume an attained separator, interiority or strong duality. No new
primary reading of these unchanged inputs was needed.

Searches included `moment problem prescribed marginal measures support
constraints conditional distributions purification Dvoretzky Wald
Wolfowitz`, `generalized moment problem fixed marginal conditional
Tchakaloff theorem Young measures`, and `fixed marginal moment problem
support restrictions Aumann expectation selection theorem feasibility`.
Exact zeta/discriminant and prescribed-marginal queries did not identify
an inspected matching feasibility theorem. This is a bounded search,
not a novelty certificate. The initial general zeta query returned
Curran--Heycock arXiv:2403.00902, already covered locally; it was not
reassessed. Marginal-moment optimal-transport relaxations and martingale
Tchakaloff variants were search leads only, not imported statements.

Feinberg--Piunovskiy, Theory Probab. Appl. 50 (2006), 463--466,
Theorems 1--2, was a relevant lead. Search indexing exposed pages
463--464, but direct CiteSeer retrieval returned 403 and the author
site timed out. That is not a fully inspected source. The accessible
Jaskiewicz--Nowak primary theorem provides the needed scope; there is
no essential source blocker and no repeated access work is proposed.
The distinct strongly-equivalent paper, Theory Probab. Appl. 54 (2010),
300--307, concerns a different preservation requirement and is not used.

L414/L415/L416 and their October-15 ATTEMPTS records were checked at
the exact scopes. Their rare components move height to H and replace
response jets; their bulk calibrations choose a response amplitude.
They are not duplicates of a law preserving this prescribed graph.
L410's scalar obstruction, L412's failed frozen-height pairing and
L413's scale/full-error obstruction remain intact. Step 99's blocked
actual signed-clipping search is not reopened: this is an abstract
conditional feasibility question with no claimed actual critical law.

### Ready bounded test and stopping rule

DECISION SPECIALIZE authorizes the exact TARGET for one later research
attempt. Seek one explicitly measurable conditional construction, with
all its moments checked simultaneously, or a pointwise inequality on
the full allowed fibers whose integrated gap survives every tolerance.
Sources cover the framework and existing moments; the new prescribed-
response feasibility or separation argument must be written and audited
as new local work, with no originality claim beyond this search.
A failed conditional rare/bulk ansatz is only failure of that ansatz.
It is not a separating theorem or an obstruction to every conditional law.

Continue if the proposed construction has a concrete way to retain the
height mass and exact response and to meet the tiny odd-moment errors
alongside the first/cubic/quartic requirements. Abandon that implementation
if it uses response-amplitude freedom, changes the height marginal,
loses fixed constants, or requires an unproved conditional moment or
actual-phase distribution. Record the failed constraint precisely.
No mathematical test of these possibilities was performed this turn.

Plausible downstream use: decide whether this actual-response coupling
adds useful joint-sign information beyond L416's stopped list. Even a
successful stronger obstruction would leave actual critical/global
realization, actual negative-Bcal clipping, L413's regulator-scale/full-
error margin, actual common-zero upper counts and global mixed positivity
unresolved. STATUS remains IN_PROGRESS. Full matching Mathlib coverage
of the conditional feasibility target and selection results was not
checked; unknown coverage is not claimed absence.
