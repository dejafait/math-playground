# Uniform point weights — critical-audit source gate

TARGET: Critically audit L169's Ext-generator sign, global base-trace scalar and cancellation proving uniform point weights under L111 and L168.
CHECKED: 2026-10-26
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 560's exact normalization searches and primary-source discovery; compared L169 in full, L111 (3)–(9), L168 finite-trace and (10) passages, prior audit coverage and ATTEMPTS/092–094; followed the exact Appendix C and regular-section references live on 2026-10-26, without a repeated broad search.
SOURCE_EVIDENCE: Nayak–Sastry author PDFs dated 2019-05-29: I C.1, C.2.1–C.2.7, C.5.3–C.5.4 with proof, Theorem 5.3.8 with proof and Remark 5.3.9; II (4.1.2),(4.1.5), Proposition 5.3.1 with proof, Remark 5.3.3 and Theorem 5.4.2 with proof. Reuse step 560 and step 558 finite/global duality coverage.
COMPARISON: The primary construction fixes unsigned transpose, the injective-resolution comparison, shifted fundamental local isomorphism, fraction convention and regular-section trace. Together with the existing actual-family formulas it covers a separate audit, but does not certify L169's component comparison or cancellation.
GAP: Mathematical audit remains: check the claimed tensor/internal-Hom comparison on the injective-resolution diagram, even shift, global trace identification and actual KS/common-kappa substitution in L169 (1)–(13); no essential source gap identified within this exact scope.
REASON: Separate theorem-level comparison now approves the saved critical-audit target as SPECIALIZE for a later REPRODUCTION audit; this is source readiness only, with no new sign calculation, proof certification or exclusion.

The current main gap is still primitive realization and existence of F.
L169 is a conditional normalization result, not a candidate solution or
an exclusion. Its downstream use is an actual section-quartic test with
one common coefficient in the fixed bracket coordinates.

Retain the full conditional family of L168 and L111, including L071,
L108/L109/L115/L116/L164/L165 through their retained hypotheses:
identical marked K3 factors, original common metric/triple/forms and
actual connection; hypothetical locally free rank-two product-polystable
F with integral c_1=0 and full character
2-14e_1-21e_2-tau_D+62P; actual alpha,j,a,r,gamma, reduced finite
W with DW=W^dagger[-2], theta_z, h_0, fixed base trace and one common
relative kappa. General s,t; empty and singleton Z remain valid. No
cross-notebook input, F existence, numerical delta_B, actual section
values, genericity or integrability is assumed. L167 is downstream
context only.

Check whether I's unsigned transpose complex is related to the
internal-Hom complex by components (1,-I,-1) under the specified
resolution arrows, and whether C.2.7's even shift really gives
phi(1/(x wedge y))=-epsilon_{x,y}. Compare the Ext-to-local-cohomology
map with C.5.4 and the square/round fraction convention. Then verify
that L168's fixed finite evaluation comes from the same global
chi_B and that chi_B/(nu_B sigma_B) is one constant delta_B. Finally
compare L111 (5)–(9) with L168's relative kappa, retaining the factor
-8, endpoint h_0 normalization and L168 (10)'s factor 4. Do not
re-audit unrelated upstream claims or recalculate section quartics.

Continuation/abandonment test: approve the audit only if these exact
orientation, trace and actual-family inputs are adequately covered.
The later audit should preserve or correct L169 with complete sign
and scalar evidence. If only a common convention sign needs repair,
distinguish that from failure of point-independence; if a pointwise
factor survives, preserve L168's symbolic formula and name the gap.
Neither result excludes F. No new lemma or mathematical script is
authorized by this REVIEW_REQUIRED record. Full matching Mathlib
coverage remains unchecked.

## Completed source comparison — step 562

LITERATURE_REASON: The invocation-start critical-audit target was
REVIEW_REQUIRED. This turn resolves that separate source gate by
comparing its precise obligations with the already identified sources;
it does not reopen source discovery for the preceding ready target.
The proposal above describes the audit still to be performed.

Primary copies were opened through web PDF text on 2026-10-26.
Printed page numbers are used; no screenshot or unread lead is evidence.

In Nayak–Sastry I, [author PDF](https://www.cmi.ac.in/~pramath/mypapers/fub1.pdf),
C.1 (p.55) defines tensor-ordered homology Koszul complexes and
unsigned-transpose cohomology complexes. C.2.1–C.2.7 (pp.56–57)
construct the comparison using an injective resolution and the
inclusion of annihilated elements by evaluation at one; the determinant
identification has factor (-1)^r and the final isomorphism uses M[r].
C.5.3–C.5.4 (pp.63–64), including the diagram chase, compare fraction
conventions and the Ext-to-local-cohomology map. Theorem 5.3.8
(pp.14–16) and Remark 5.3.9 identify finite trace and restriction to
an open neighbourhood; Proposition 5.4.4 (p.17) is reused from step
560. These require the stated regular/quasi-regular immersion and
finite-flat-over-base hypotheses. They specify the comparison that
must be audited, rather than asserting L169's chosen components.

In II, [author PDF](https://www.cmi.ac.in/~pramath/mypapers/fub2.pdf),
(4.1.2),(4.1.5) (pp.21–22) compare Verdier, abstract and proper
traces. Proposition 5.3.1 and its completion proof (p.26), Remark
5.3.3 (pp.26–27), and Theorem 5.4.2 with proof (p.27) specify the
regular-section residue and coefficient evaluation, for a smooth
separated map and a closed section. The completion/power-series
proof inputs already read in step 560 are reused, not newly certified.

Applicability is unchanged from the prior assessment: B is a smooth
projective complex surface, z a reduced C-point, and x,y regular
parameters on a suitable smooth affine neighbourhood. The point is
finite flat over Spec C, not over B. Open/support comparison relates
this to the proper base trace. Thus the source hypotheses match the
local input without imposing ordinary middle base change. The global
comparison of dualizing trivializations is a short application still
to be checked in the audit, not a new theorem supplied here.

The remaining obligations are local mathematical checks: identify the
claimed (1,-I,-1) map with C.2.3 through its augmentation/injective
comparison, retain C.2.7's shift, and compare the resulting finite
functional with the same chi_B used in L168. Then check L111's actual
(5)–(9) and L168's two coordinate factors and common relative scalar.
The source does not mention this F, h_0, lambda or bracket. Its theorem
cannot be cited as a proof of their cancellation. Reproof of general
duality or residue normalization is unnecessary; checking the explicit
specialization is necessary. No component identity is derived here.

Duplicate/failure comparison: L168's prior audit stops at symbolic
tau_z; L169 introduces the residue normalization beyond that scope.
ATTEMPTS/092–094 still leave actual section images and complementary
operations undetermined. Equal coefficients, even if audited, would
not reopen their failed vanishing tests or prove a quartic exclusion.
The fixed forms/connection and conditional character in the proposal
remain essential; no existence, section values or genericity is added.

Decision: approve exactly TARGET for one separate proof audit, classified
REPRODUCTION under SPECIALIZE. Preserve or correct L169 only after
checking its full sign/scalar evidence. A surviving point factor requires
retaining L168's symbolic weights; a common sign correction must be
separated from loss of uniformity. Empty/singleton support is retained.
Full matching Mathlib coverage is unchecked. No lemmas, mathematical
scripts, PROOF.md or DAG.md were changed; no progress beyond known
source mathematics or correctness certification is claimed.
