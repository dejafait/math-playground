# Small-background full-Jacobian sign — source comparison969

TARGET: Review source coverage for the conjectured implication Re W_t(r,s)>=0 on every C466s survivor when H_0 is real, the strict C466u buffer holds, and M_1 sqrt(a^2+b^2)+M_2 T_0<=1/100, including degree-at-most-two H as a possible counterexample class.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Step969 searched quantitative residual-phase/Hessian bounds, logarithmic-zero counterexamples, positive-real Jacobians, and Lagrangian-angle preservation; inspected the primary statements and proof cases below and reused reviews947/954. No matching all-survivor theorem or certified counterexample meeting the proposed smallness condition was found in this bounded search; no novelty inference.
SOURCE_EVIDENCE: Reused TNV2017 Section2.2/AppendixB and LY2021 IV.A–IV.B from reviews947/954; newly inspected TNV2017 Section4.2(45)–(49), Alexandru et al. arXiv:1604.00956v1 SectionsII–III(5)–(20), Cristoforetti et al. arXiv:1403.5637v2 SectionsII–VI(4)–(17), Behrndt arXiv:0812.4256v3 Section3(2), Definition5.1 and Propositions5.4–5.5 with proofs, and Bloch arXiv:1808.00882v1 SectionIII(4)–(9), SectionIV pp6–7. Direct citations and scope qualifications below.
COMPARISON: Exact variational/orthonormal-frame phase identities retain the full tangent geometry; the exact Gaussian calculation concerns quadratic total action with critical-point tangent initialization. Mean-curvature angle evolution has a different velocity. The logarithmic Gaussian example uses a different initial cycle and modified flow; Bloch's quartic example has no logarithmic divisor. None supplies or refutes the stated 1/100 implication. C466s/u still give modulus/current rather than sign.
GAP: Uniform control of the full fixed-time weighted determinant near first collision remains unproved. No inspected source gives a gradient/Hessian-background-only half-plane estimate for this initial plane; no admissible low-degree negative point was certified. Essential local-flow sources are accessible, so a bounded polynomial obstruction attempt has sufficient source coverage, without claiming coverage of its conclusion.
REASON: Complete the changed sign target's essential comparison without deriving new mathematics. Park imports based on Gaussian approximation, action phase alone, or a different geometric flow; nominate one polynomial counterexample test for separate approval in assessment969. A failure of a phase bound would not itself be a counterexample.
LITERATURE_REASON: The proposed 1/100 full-weight sign condition and all-survivor quantifier were outside the ready modulus/current assessments; this review reads the essential residual-phase and angle-theorem cases, rather than repeating those earlier approvals.
SCOPE: Exactly C466s's unit flat raw flow in a bounded bidisk, initial (ir,s), real H_0, bounded holomorphic gradient/Hessian, first lifetime and fixed-physical-time full complex Jacobian; add T_0>0, M_1 T_0<min{R-a,L-b}, and the displayed smallness condition. No regular collision trace, symmetry of H, positive determinant or actual-Xi realization is assumed.

## Original nomination968, preserved; its source review is completed below

The following nomination's REVIEW_REQUIRED and proposed next-turn language
records the invocation-start state. The completed decision and next target
are specified in the fields above and the comparison below.

## Exact prospective discriminator, not an established result

Use C466s's W_t=-q(t)^2 exp(-H(X(t))) det_C J_t/i on
survivors, with J_t=[partial_r X,partial_s X] at fixed t.
The universal proposed conclusion is Re W_t(r,s)>=0 for every
0<=t<=T_0 with t<tau(r,s), r!=0, (r,s) in I. The bound
M_1 sqrt(a^2+b^2)+M_2 T_0<=1/100 is a proposed sufficient
condition, not a proved estimate, optimal constant or necessity claim.
The universal quantifier includes arbitrarily small r and times
arbitrarily close to collision; no extra lower bound on |q| is allowed.

The literature review must search the exact implication and stronger
quantitative residual-phase or Lagrangian-angle results, and compare
known logarithmic-flow counterexamples. Retain the full signed complex
Jacobian, not its modulus or just the phase of exp(-S). Reuse already
inspected local-flow, variational and volume machinery. Read only new
primary hypotheses/proof cases essential to this sign question; do not
repeat inaccessible retrievals or a general thimble survey.

If no exact import or obstruction is found, a later separately approved
bounded test may seek an admissible polynomial H of total degree at
most two satisfying all the bounds and one surviving point with
Re W_t<0. Such a point would refute this universal sufficient condition,
not actual-Xi positivity or the possibility of a different contour.
Numerical phase sampling or failure of an angle estimate is insufficient:
any counterexample needs a complete exact or rigorous interval
certificate, including survival and fixed-time parameter derivatives.
Conversely, a positive outcome requires the uniform sign theorem for
the stated H class; favorable polynomial examples do not establish it.
No calculation, polynomial fitting or proof attempt is authorized by
this REVIEW_REQUIRED nomination.

## Relevance and alternatives considered

The main gap is still L030-L032/C032a actual-Xi all-degree
algebraic-square positivity. A local full-weight half-plane sign would
be a possible additional ingredient for signed integration on flow
patches, alongside the audited current identity. Paying actual-H
smallness, phase alignment between patches, all orders, global
homology/endpoints and density-to-Xi transfer would remain separate.
This prospective use is conditional; the local result would not be a
positivity theorem for Xi.

Three possible continuations were compared, without attempting them:

1. Restart C466u through arbitrary time: changed initial surfaces and
   outer-grazing shadows are unpaid; C466t forbids simply dropping the
   buffer. This would still leave the sign untouched, so it is parked.
2. Enclose the third actual determinant at x=B'(1): C466p already
   imports the strict sign with explicit external certificate
   qualifications. Reproving that same conclusion is not selected.
3. Test the prescribed flow's full weighted sign under a quantitative
   small-background condition: this is independently falsifiable and
   addresses a missing sign premise. Select its source comparison.

Preserve C466k/stop927, stops932/941/947/948/959/961 and attempt966.
In particular stop948 does not prohibit every phase question: this is
a sufficient half-plane inequality for a specified dynamics, not a
claim that every admissible contour has a smooth divided phase.
C466s supplies the formulation; C466u supplies only the downstream
local current tool; C466t and C466k are contrasts, not sign inputs.
C466p is only the duplication comparison. No cross-notebook input is
used and no Mathlib match for this sign statement has been checked.

The exact next task is literature_comparison, standard/high. There is
not yet a justified proof_attempt/creative on the central actual-Xi
gap: the smallness and global assembly implications have not been
paid, and exact sign coverage is missing. Do not relabel this local
candidate as a central breakthrough to satisfy scheduling. After the
source review, select proof purpose from the actual remaining work;
any new ready mathematical continuation needs separate approval.

## Completed bounded source comparison — step969, 14 November 2026

No sign estimate, coefficient fit, flow solution or counterexample was
derived in this literature-only step. The target in TARGET is preserved.
The result is source coverage for a later test, not mathematical progress
beyond the inspected sources or a claim of exhaustive literature coverage.

### Exact phase identities and the Gaussian restriction

Alexandru, Basar, Bedaque, Ridgway and Warrington,
[*Fast Estimator of jacobians in Monte Carlo Integration on Lefschetz
Thimbles*, Phys. Rev. D93 (2016) 094514](https://doi.org/10.1103/PhysRevD.93.094514),
[arXiv:1604.00956v1, 4 April 2016](https://arxiv.org/html/1604.00956),
SectionsII–III, (5)–(20): read the tangent initialization, variational
equation and complete Gaussian calculation (11)–(16). The initial frame
comes from positive Takagi directions at a nondegenerate critical point.
For quadratic total action the determinant is a positive exponential
times the initial frame determinant, (15). The trace exponential in (17)
is instead an estimator: (19) omits conjugation of J and (20) retains
reweighting. No uniform phase-error bound is stated in these passages.
In our target, degree-two background H does not make the total
logarithmic action quadratic, and diag(i,1) is prescribed independently
of a critical-point frame. Thus the exact Gaussian case is not an import
of the proposed implication; an estimator cannot certify its sign.

Cristoforetti, Di Renzo, Eruzzi, Mukherjee, Schmidt, Scorzato and Torrero,
[*An efficient method to compute the residual phase on a Lefschetz
thimble*, Phys. Rev. D89 (2014) 114505](https://doi.org/10.1103/PhysRevD.89.114505),
[arXiv:1403.5637v2, 14 June 2014](https://arxiv.org/html/1403.5637),
SectionsII–VI, (4)–(17): read the nondegenerate-saddle assumption,
orthogonality preservation, continuous orthogonalization and the complete
trace derivation before (16). The residual phase is det U for an
orthonormal complex tangent frame; its logarithm contains an integral
of the full real Hessian projected through the evolving tangent frame.
The source's J denotes the ambient complex structure, not our parameter
Jacobian, and its H is the real Hessian of the full action. SectionVI
initializes the phase at the saddle limit, approximated at a finite
cutoff; (17) uses an infinite stochastic-sample limit. Neither the
reported average-phase evidence nor this identity is a pointwise
half-plane bound from our background M_1,M_2. Applying the frame method
to the prescribed initial plane and controlling collision uniformly
would require additional mathematics; it is not performed here.

### Angle preservation uses a different evolution

Behrndt, [*Generalized Lagrangian mean curvature flow in Kähler manifolds
that are almost Einstein*, arXiv:0812.4256v3, 7 April 2010](https://arxiv.org/pdf/0812.4256v3),
Section3, (2), printed pp4–5, Definition5.1 and Propositions5.4–5.5,
printed pp10–12: read the smooth nonvanishing holomorphic-volume-form
hypothesis, the definition K=H_mean-n(grad psi)^perp, and both proposition
proofs. For that geometric flow the angle satisfies
theta_t=Delta theta+n dpsi(grad theta). The key proof uses the identity
K=J grad theta. The source's compact existence theorem is Theorem3.6,
printed p8; the angle identity is a statement on a smooth existing flow.
Our raw ambient conjugated-gradient velocity has not been identified
with K, even up to tangential reparametrization. Its punctured survivor
domain also has no supplied angle boundary control at collisions.
Consequently a maximum-principle sign import is not justified. This
comparison does not assert that the two velocities can never agree in
a special example, and makes no new non-equivalence theorem.

### Known adverse examples do not certify this target's failure

Reuse TNV2017's local flow and Jacobian coverage from reviews947/954.
Newly read [TNV2017 v2 Section4.2, (45)–(49)](https://arxiv.org/html/1706.03822v2#S4.SS2):
the model has quadratic regular action and a polynomial determinant;
the displayed case has multiplicity p=2. It is a relevant low-degree
logarithmic lead. Its initial cycle is the real axis with a shifted
divisor, and its numerical flow has the damping factor (49). The
discussion distinguishes saddle phases and residual phase. It neither
asserts our 1/100 bound nor certifies a surviving negative point for
the initial (ir,s) plane with unit raw dynamics. No coordinate rotation,
parameter rescaling or limiting metric argument is silently used to
turn that example into a counterexample here.

Bloch, [*Anatomy of a strong residual sign problem on the thimbles*,
Phys. Rev. D98 (2018) 114502](https://doi.org/10.1103/PhysRevD.98.114502),
[arXiv:1808.00882v1, 2 August 2018](https://arxiv.org/pdf/1808.00882),
SectionIII, (4)–(9), printed p3, and SectionIV discussion of Figures7–8,
printed pp6–7: read the action, arc-length Jacobian decomposition and
the cancellation mechanism. The example's action is
S(z)=z^2/(2 sigma^2)+a z^4/(2 sigma^4)-iz-log N. The plotted negative
real contributions involve the sum of the constant action phase and
the tangent phase. The action has no logarithmic divisor, the curves
are saddle thimbles, and the evidence is numerical rather than an
interval certificate for our data. A small quartic coefficient in that
model is not our gradient/Hessian smallness hypothesis. This is a
warning against unrestricted residual-phase optimism, not a rigorous
counterexample to the nominated condition.

### Search, duplicate checks and decision

Queries included `"holomorphic gradient flow" "residual phase" bound
Hessian`, `"holomorphic gradient flow" logarithmic singularity Jacobian
phase counterexample`, `Lefschetz thimble Lagrangian angle small
perturbation logarithmic zeros positive real Jacobian`, `"holomorphic
gradient flow" "small" "phase" determinant`, `"holomorphic gradient
flow" "phase" "bound"`, `"Lagrangian angle" "holomorphic" "gradient
flow"`, `"holomorphic gradient flow" "positive real" Jacobian`,
`"logarithmic" "thimble" "residual sign" counterexample`, and
`"residual phase" "Hessian" "bound" thimble`. Additional exact
logarithmic/small-flow and q^2/Jacobian searches returned no matching
statement; unrelated gradient-flow results were not used as evidence.
The Behrndt primary paper was followed from the angle search, and the
2014 residual-phase paper from TNV's explicit reference. The 2014 and
2016 arXiv abstract records confirm the cited versions. The failed
Bloch HTML retrieval was replaced by the accessible v1 PDF; it is not
a persistent source blocker. The 2016 PDF has an anomalous internal
date; equation claims above use its rendered v1 HTML and arXiv record.

The one-site fermion paper found by search, the separate lead
arXiv:1412.2802, and broader sign-problem reviews remain unread;
no theorem or conclusion is attributed to them. No exact target match
was located in the sources actually
inspected. This is sufficient bounded discovery for EXPLORE, not an
assertion of novelty or literature-wide absence. Further browsing on
this same ready scope needs a changed essential hypothesis or lead.

Locally read C466s's hypotheses/conclusion and source convention,
C466u's exact strict buffer, and C466k's product-contour hypotheses and
conclusions. Read stops947/948/959/961/968 in full and reused the
relevant primary-source comparisons in reviews947/954. The product
obstruction, generic free-coordinate phase rectification, unsupported
collision smoothness screen, modulus-to-current gap and outer-grazing
defect keep their original scopes. They neither prove nor refute the
new sufficient sign condition. No stopped-current audit or known third
determinant is repeated. No cross-notebook input is used.

The remaining mathematical discriminator is one admissible negative
point or a uniform all-survivor theorem; a failed envelope, favorable
examples or numerically sampled phase are insufficient. Select the
bounded degree-at-most-two counterexample test in
[assessment969](2026-11-14-small-background-polynomial-sign-test-969.md).
It is newly nominated and requires separate approval next turn. No
existence of such a polynomial or of a sign-preserving neighborhood
is asserted. Matching Mathlib coverage was not checked; no formal
absence or verification is claimed.
