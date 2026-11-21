# Fixed-interval weighted-cubic flux test — source gate repaired at step221

TARGET: Test whether a fixed full-theta density minorization on x in [1/16,1/4] pays the shifted monic-cubic norm deficit in L874's S7 flux at every full-degree d=2 contact on 0<lambda<=1/20, retaining all three null rows and stopping at the first unpaid estimate.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed exact/stronger-result and duplicate/failure search in 2026-11-09-d2-flux-weighted-cubic-norm-review.md, step220; the fixed-interval candidate lies within its weighted-norm scope. No novelty conclusion.
SOURCE_EVIDENCE: Gautschi2004 Theorem1.24 pp8-9 https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf ; Gallier2019 Proposition2.2/Proposition4.2/Theorem4.3 https://www.cis.upenn.edu/~jean/schur-comp.pdf ; DLMF18.3 Table18.3.1 https://dlmf.nist.gov/18.3#T1 ; rechecked accessible statements and relevant cases at step221. Reuse step220 Boyd-Vandenberghe AppendixA.5.5 pp650-651 https://stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf and Laurent2010 Lemma4.2 pp54-55 https://homepages.cwi.nl/~monique/files/moment-ima-update-new.pdf ; Gaussian coverage reused, no new theorem needed.
COMPARISON: Minimum-norm and block-matrix identities are known. No inspected result pays the actual-theta contact-conditioned flux deficit. A fixed density lower bound is a new candidate quantitative input, distinct from strict generic PSD, the stopped J test and determinant-box refinement.
GAP: The exact norm/flux reduction, density floor and domination test have not been derived or evaluated. No mathematical result or sufficient sign is approved as already proved.
REASON: Step221 separately reviewed the saved nomination and repaired its missing direct source URLs. Essential standard tools remain covered; approve only the unchanged bounded mathematical test, with its theta-specific claims wholly unproved.
SCOPE: Only the exact TARGET and fixed interval. Use L019/L058/L874 as essential inputs; L043 is ordinary-Gram overlap, L917 may supply only an existing full-band normalizing-mass upper bound, and L918/L921 are contrasts. No actual contact, representing measure for H2, extra shifted logarithmic rows, positive lower bound for abs(c2), new moment evaluator, determinant boxes, new panels, residual class, interval tuning or sweep is authorized.

The main gap is L030-L032/C032a all-degree mixed positivity. The
intermediate aim is an independently paid finite-contact boundary
direction. Initialization, equality/tangency, all other degrees and
global continuation still need separate work even if this test passes.

Use the actual normalized positive theta law, x=u^2 and its weighted
measure x dmu_lambda. Retain real unit c=(c0,c1,c2), c2!=0, H2 PSD
and every equation H2*c=0. c0/c1 may vanish; no uniform bound away
from c2=0 is assumed. No contact is asserted to exist. The interval is
fixed at [1/16,1/4]; it is a test choice, not an optimized bound.

In the later attempt first expose, with exact signs and normalization,
the missing seventh x-moment in L874's flux and the corresponding
shifted cubic norm deficit after all null rows are used. Cite the
general Schur-minimization and monic-extremal theorems; justify the
actual raw-block invertibility or retain their singular range case.
Do not reprove those general results. Polynomial moments are finite
by L058. The positivity of H2 is a distinct logarithmic premise.

The proposed independently paid input is one coefficient-independent
norm floor: minorize the actual weighted density on this fixed
interval using L019's positive first summand and a proved upper bound
for the full normalizing mass; apply the cited monic Legendre minimum
after checking the change of variable. Do not replace the full theta
law by its first term or a truncated normalized probability. The floor
must hold for all monic cubics, not a convenient trial polynomial.
No density constant, square-completion formula or deficit sign was
calculated in step220.

The decisive test is whether this single floor pays the entire exact
contact deficit uniformly under the stated actual-family premises.
Record actual and required bounds. A rigorous admissible witness can
refute a specified enlarged sufficient relaxation only; it is not an
actual-theta contact or a counterexample to the flux. If the first
comparison cannot be paid, stop and retain the partial reasoning.
Do not change the interval, add data or launch an optimization. An
unpaid comparison is EXPLORATION unless it yields a new informative
obstruction; merely completing another reformulation is no advance.

The creative purpose is the independent theta-density coercivity
versus the logarithmic null-row deficit, not an original Schur or
Legendre theorem. No source reviewed supplies that domination.
Preserve all earlier local stops. No cross-notebook input. Full
matching Mathlib coverage for this contact mechanism is unchecked.

## Step221 — separate source approval and recovery repair

LITERATURE_REASON: Supervisor flagged missing direct source URLs in this ready assessment; this bounded source-access and citation repair is the required exception to immediate mathematics. No new search or mathematical scope is claimed.

On 9 November 2026, reopened the directly linked Gautschi book,
Gallier author PDF (24 August 2019), and DLMF table. Retrieved
Gautschi Theorem1.24 and its complete orthogonal-expansion proof,
Gallier Proposition4.2's singular range/positive-subspace cases and
Theorem4.3's statement, and both Legendre rows of Table18.3.1.
Gautschi printed pp.8-9 correspond to PDF pages19-20. Gallier's
Proposition4.2 starts on printed p.9 and continues on pp.10-12;
Theorem4.3 is on printed p.12. These locators remove the earlier
ambiguous p.9 shorthand. The remaining standard hypotheses and
proof cases are reused from step220, not newly assessed mathematics.

The norm minimum presupposes a positive measure with infinite support
and finite moments. Application to the actual weighted law still needs
local justification using L019/L058. Gallier requires a real symmetric
block and, in a singular PSD case, the range condition
(I-AA^dagger)B=0; an inverse cannot be presumed from logarithmic H2.
DLMF supplies weight-one Legendre data on (-1,1) and (0,1), not a
theta density bound. No source pays the S7 deficit. No general theorem
needs reproof; the future attempt must justify the change of variable,
normalization, raw-block treatment and contact-specific algebra.

Reuse step220's exact/stronger-result searches, duplicate L043 and
failure comparisons unchanged. This repair establishes no new lemma,
no theta constant and no new mathematical evidence: STALLED as a
research outcome. The assessment remains EXPLORE for exactly TARGET;
no additional approval turn is mathematically needed before that test.
Keep the fixed interval, all three null rows, c2!=0 without a uniform
lower bound, and every stopping qualification above. Full matching
Mathlib coverage remains unchecked. PROOF and DAG are unchanged.
