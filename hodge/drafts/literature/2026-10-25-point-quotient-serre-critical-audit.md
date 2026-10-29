# Point-quotient Serre comparison — critical-audit source approval

TARGET: Critically audit L168's quotient adjoint, finite-point orthogonality and trace weights in L164's bracket coordinates.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 558 reused step 556's bounded theorem searches, searched the named L109/L111/L116/L164/L165 proof conventions and ATTEMPTS/092–094, and followed 48.27.4's primary evaluation reference to Stacks 20.50.7 (0FPC); no novelty claim or repeated broad discovery search.
SOURCE_EVIDENCE: Live Stacks HTML read 2026-10-25: 48.27.1–4 (0FVU), 48.20.12 (0AX4), 4.24.9 including proof and equation 4.24.9.1 (0DV0), 48.12.6 including adjunction explanation (0G81), 57.11.2 including finite-length proof (0G23), and 20.50.7 (0FPC); reuse remaining primary coverage in 2026-10-25-point-supported-quotient-serre-form.md.
COMPARISON: The inspected framework covers shifted dual-first evaluation, actual cup/trace adjunction and finite trace composition under the retained smooth proper and finite-support hypotheses; it supplies no ready theorem certifying L168's particular inverse-gamma and bracket-coordinate calculation. A separate audit of that specialization is now covered.
GAP: Check L168 (5)–(10) against the actual arrows and local conventions, including inverse direction, shift sign, Koszul orientation, both coordinate factors and common-scalar scaling; all remain mathematical audit obligations, not conclusions of this review.
REASON: Separate source approval of the new critical-audit target, with the evaluation convention explicitly inspected; no missing essential theorem was identified for the symbolic-trace scope. Numerical analytic residues and actual quartic calculations remain outside approval.
SCOPE: Exact TARGET only, with L168's full conditional hypotheses, general s,t, reduced finite W and symbolic tau_z; allows checking or repairing the stated specialization, not a new exclusion or quartic computation.

The main gap remains primitive realization and F existence. The audit
would test whether the new access to the point form is sound before any
dependent attempt to evaluate the actual quartic. It need not decide
that quartic or any other independent gap.

Retain L168's entire conditional family through L109,L111,L116,L164,L165,
including L071 and L108/L115. L167 supplies the possible downstream use,
not a premise of L168. Preserve the actual alpha,j,a,r,gamma, full reduced
finite W with DW=W^dagger[-2], top derived base change theta_z and fixed
h_0. The hypothetical F, markings, metric, forms, integral c_1=0 and
full character 2-14e_1-21e_2-tau_D+62P remain as stated canonically.
There is no cross-notebook input. General s,t are allowed; the formal
endpoint s=800,t=48 is not needed to audit this form.

The key comparisons proposed for a later audit are L168 (5)–(8) and
(9)–(10): a Lambda=gamma[-2], r Lambda=0, pullback adjoint
gamma^{-1}[-2], the positive even-shift global evaluation, and the
resolution comparison defining epsilon_{x,y}. In the bracket coordinate
ell_z, verify the two factors 2 kappa/bar(s_0) and that rescaling the
relative trace scales the form once. The evaluation functional tau_z
is deliberately retained; no analytic residue value has been derived.

Continuation test: approve the audit only if the existing primary
coverage accounts for these precise maps and conventions; otherwise name
the essential missing theorem before dependent work. The audit itself
should preserve a valid formula, repair a real sign/normalization error,
or identify a concrete unsupported inference. Even a valid formula leaves
the actual section quadrics, complementary operation, quartic minimum
square length and F existence unresolved. ATTEMPTS/092–094 stay intact.
Full matching Mathlib coverage remains unchecked.

## Completed source comparison (step 558)

LITERATURE_REASON: The invocation-start target was a new REVIEW_REQUIRED
critical audit; separate coverage approval was required despite ready
coverage for the preceding derivation. The new primary lead is the
evaluation convention referenced by 48.27.4, not a reason to repeat
discovery on the already assessed local-form target.

The following are source statements and audit obligations, not a proof
audit or a new derivation. Sources are live HTML as read 2026-10-25;
stable tag IDs fix the cited results, with no commit version asserted.

- [Stacks 48.27.1(5),(7), 48.27.2–4, 0FVU](https://stacks.math.columbia.edu/tag/0FVU):
  proper schemes over a field have functorial duality compatible with
  shifts and triangles; bounded coherent inputs give perfect pairings.
  The smooth case identifies the dualizing complex with the shifted
  canonical bundle. The remarks describe composition followed by trace;
  48.27.4 identifies cup/evaluation with that pairing for perfect inputs.
  Read the statements, adjunction proof of (5), remarks and proof of
  48.27.4. Smooth projective B and X, their fixed canonical forms, and
  perfect C and point sheaves fit these hypotheses. This permits checking
  L168 (7)–(8); it does not decide the notebook's signs automatically.
- [Stacks 20.50.7, 0FPC](https://stacks.math.columbia.edu/tag/0FPC):
  for a perfect complex on a ringed space, evaluation has order dual
  tensor original, and coevaluation corresponds to the identity.
  Read the entire example. This is the explicit convention referenced
  by 48.27.4. It does not tabulate L109's component matrices or resolve
  L168's shifts; those must be compared in the later audit.
- [Stacks 48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81):
  a pairing into the relative dualizing complex inducing a duality
  isomorphism, with pseudo-coherent second input, induces the pushed
  forward duality through relative cup and trace. Read its statement
  and adjunction explanation. Here p is smooth proper of relative
  dimension two and V is locally free and trace-self-dual; reuse 0BRT
  from the ready assessment for its relative dualizing complex.
  The audit must retain this actual adjoint, rather than choose a form.
- [Stacks 57.11.2, 0G23](https://stacks.math.columbia.edu/tag/0G23):
  read the full proof for a finite-length module over a regular local
  ring, identifying its derived dual with its Matlis dual shifted by
  minus the dimension. The local rings at the split points have
  dimension two. This covers the dual's degree, not a choice of its
  generator or any numerical residue. Reduced length one is L111's
  hypothesis, not a consequence imported from this source.
- [Stacks 48.20.12, 0AX4](https://stacks.math.columbia.edu/tag/0AX4):
  finite morphisms between finite-type schemes over a Noetherian
  dualizing base have the displayed derived-Hom trace, evaluation at 1,
  when the dualizing complexes are normalized over that common base.
  Read the entire remark. The points, Z and B lie over Spec C, so the
  scope permits comparing their trace maps. This is not flat finite
  algebra trace and does not impose a numerical value on tau_z.
- [Stacks 4.24.9, 0DV0](https://stacks.math.columbia.edu/tag/0DV0):
  read the statement and proof of composition of adjoints and counits,
  especially equation 4.24.9.1. Reuse the finite-adjoint identifications
  from the prior assessment when applying it to the composite point,
  surface and field maps. Coherent trace normalization is covered;
  independently rescaling point traces is not authorized.

The prior ready assessment supplies inspected 0A9X/0B6M/0AX2 and
the relative-duality hypotheses. It is reused within exactly that scope,
not treated as a proof of L168. The new evaluation-source inspection
and explicit comparison resolve this proposal's source gate only.
No further essential source is needed for the stated symbolic formula;
an analytic residue/Jacobian normalization would be a changed target.

Local overlap check: read L168 in full, L109's explicit dual-complex
sign passage, L111's actual orthogonal Koszul summand, L116's actual
adjoint/retraction construction, L165's base-first sign comparison,
and L164's h_0/commutator normalization passage. These already contain
the relevant component conventions; the next step should audit them,
not add a duplicate local-form lemma or reprove general duality.
L168's explicit resolution comparison is a family-coordinate
specialization, so checking it is necessary even with the known
theorems imported. No new matrix identity was proved in this review.

ATTEMPTS/092–094 were read completely. They leave the section-image
pairing, complementary operation and polynomial compatibility open.
Nothing in this source approval supplies those data, contradicts their
stop evidence or proves an exclusion. The main Hodge gap is unchanged.

Decision: retain the exact TARGET and approve one subsequent critical
proof audit under SPECIALIZE, classified REPRODUCTION. Check (5)–(10)
completely, including the empty split-set case, and preserve a valid
formula or repair a specific error with its dependencies recorded.
If an essential theorem outside this scope appears, stop the dependent
audit and identify it. No actual quartic computation, lower square
length or F existence claim is approved. Mathlib matching coverage
remains unchecked. No lemmas or mathematical scripts were modified.
