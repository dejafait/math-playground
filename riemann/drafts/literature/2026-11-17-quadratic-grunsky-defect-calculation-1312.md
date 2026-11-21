# Fixed quadratic Grunsky defect: calculation assessment1312

TARGET: Test the six full quadratic-defect equations delta_mn/m-sum_(k>=1) k*c_km(f_b)*c_kn(f_b)=tau*d_m*d_n*S_(m+n), 1<=m,n<=3, for f_b(z)=z/(1+sum_(j=1)^5 b_j*z^(j+1)), real b_j, tau>0, d_1=1 and d_2,d_3>0, by exact Faber support reduction and one necessary compatibility test using the fixed1307 actual-Xi boxes, retaining all branches and explicitly separating formal feasibility from certified unit-disk univalence.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Completed source review1312 in nomination1311 checks this exact fixed family, full quadratic construction, local linear stops and inverse-realization near-match; its scoped local and external queries are reused. No inspected theorem solves these six actual-Xi equations; no novelty claim.
SOURCE_EVIDENCE: Direct primary URLs https://arxiv.org/html/hep-th/0305005v2 ; https://arxiv.org/html/1606.00553v2 ; https://arxiv.org/html/1704.08184v1 ; Teo hep-th/0305005v2 Sections2.1-2.2 recurrence,(2.3)-(2.4),(2.8)-(2.12), formal extension; Beckermann-Stylianopoulos arXiv1606.00553v2(1.1)-(1.4), Lemma2.2 and proof(2.6)-(2.9); Ponnusamy-Wirths arXiv1704.08184v1 Theorem1/proof(2)-(4)/Remark1; ready1303/1310 coefficient/contraction and1308 exact-sign-method assessments. Full primary links and qualifications in completed review1312.
COMPARISON: Classical Faber identities supply exact column extraction and quadratic contraction supplies a conditional analytic sign; neither realizes the actual block. Linear prescriptions C030y/C030z differ from these equations. Any finite formal compatibility or obstruction must be established in the later calculation, with no assumed positive Hankel input.
GAP: Produce and verify the complete polynomial reduction and one decided necessary test, or save a precise unresolved condition. A formal solution supplies no holomorphic unit-disk realization; every larger block and all-degree signs remain separate.
REASON: One bounded calculation can expose a necessary obstruction or retain a concrete finite mechanism without analytic assumptions. It uses known identities with justified specialization, not a reproof or a ready creative construction. Direct-URL recovery1313 preserves the reviewed target and mathematical scope; supervisor approval remains separate from calculation.
SCOPE: Exactly five real Laurent coefficients, six symmetric equations for the first three indices, fixed1307 outer boxes and their inherited contracts. No extra constant coefficient, oddness assumption, higher degree, rescaling, new quadrature, interval refinement or parameter sweep. A necessary-condition test may fail to decide the family; record that honestly.

## Authorized specialization after separate approval

Use the symmetric negative mixed-log convention of C030y/C030z. Import
Teo's Faber recurrence and composition identity, then prove the exact
support bounds for each of the three selected columns of this finite
Laurent reciprocal map before multiplying columns. Extract all required
coefficients, including those beyond mixed total degree six. Provide
the full sum in every entry; neither a 3-by-3 Grunsky section nor the
old nine mixed entries alone are a justified replacement. There is
no need to reprove the general Faber or Grunsky theorems.

Derive the six equations, preserving tau>0 and all three positive
weights (d1 fixed to one). Select one explicit algebraic necessary
condition from this exact system and test it against the existing
actual S2-S6 boxes or rigorous signs. Keep zero/division, equality,
common-root and unbounded branches relevant to any conclusion. Reuse
1308's exact-real-algebraic coverage only with certified parameter
guards; rational boxes are not an exact sign oracle for transcendental
constants. A floating residual, dimension count or small sample cannot
establish either existence or universal exclusion. No global solver
runtime is promised. Save a complete unresolved condition if the
fixed evidence does not decide it; do not add a sweep to force a result.

Any compatible formal witness must satisfy the full exact equations
and strict parameter hypotheses for the actual data, not merely for
some point in the outer boxes. Analytic use additionally requires a
holomorphic univalent f_b on the whole unit disk. The primary sufficient
test in Ponnusamy-Wirths Theorem1 uses the strict disk inequality in
review1312; poles must be excluded separately. Failure of that sufficient
test is inconclusive. No standalone new univalence construction or
changed analytic method is covered by this finite calculation target.
The optional Gram interpretation in Beckermann-Stylianopoulos also
requires its domain and zero-area-boundary hypotheses; contraction
itself does not require importing that stronger interpretation.

Main gap and use: L030-L032/C032a require all actual mixed-form signs.
A finite analytically certified match could supply one finite input;
formal compatibility only retains the proposal for a later realization
question. A branch-complete necessary obstruction stops this exact
family, not RH or general Grunsky methods. An informative undecided
condition may be retained without calling it positivity or existence.
No altered equations, increased Laurent degree or repetition of1311
is authorized. The generic positive-matrix factorization route would
assume the missing actual sign and does not meet this target.

Continuation inputs: L025,L030,L032,C032a,C030y,C030z,L019,L021,L027,
L036,L037,L917, and the fixed1307 certificates named in C030z. Retain
the conditional arithmetic contracts, all higher-degree, initialization,
singular-block and realization gaps. No cross-notebook input or RH
premise. Full matching Mathlib coverage is unchecked.

Scripts, if needed, must save exact support/coefficient provenance,
equations, branch guards and complete verification evidence under
scripts/grunsky/, and print only conclusions, actual/required bounds,
failures and artifact paths. No mathematical script was written in
this source turn. Route: calculation, standard/high. Classify classical
identity replay as REPRODUCTION; a decided scoped result absent from
the assessed sources may be POTENTIALLY_NEW, with no originality claim.


## Direct-source traceability repair1313 — 17 November 2026

LITERATURE_REASON: Supervisor recovery requires a direct source URL in the ready assessment; this bounded verification repairs that omission without changing the target or expanding its coverage.

All three versioned primary HTML URLs in SOURCE_EVIDENCE were opened
successfully. Reused the completed comparison in nomination1311; no
new discovery search or mathematical calculation was performed.

- [Teo, v2](https://arxiv.org/html/hep-th/0305005v2), Section2.2,
  (2.3)-(2.4), was checked for the symmetric negative-log convention
  and degree-n Faber composition identity. The reciprocal definitions
  (2.8)-(2.12) remain the cited identification input. These identities
  do not themselves establish the specialized full support or feasibility.
- [Beckermann–Stylianopoulos, v2](https://arxiv.org/html/1606.00553v2),
  Lemma2.2, (2.6)-(2.9), was checked with the exterior conformal-map
  setup. Its proof takes analytic level curves to the boundary using
  zero planar boundary measure and summable column products. This
  is conditional Gram overlap, not an inverse-realization result.
- [Ponnusamy–Wirths, v1](https://arxiv.org/html/1704.08184v1), Theorem1,
  proof(2)-(4), Remark1, was checked: normalized meromorphic functions
  satisfying the strict disk inequality are univalent, but a simple
  pole is allowed. Holomorphic realization still needs pole exclusion;
  failure of the sufficient criterion remains inconclusive.

DECISION remains SPECIALIZE. The precise finite calculation is unchanged;
no new lemma, equation, support bound, feasibility result or sign is claimed.
The previous review's duplicate and failure comparison is reused unchanged.
Full matching Mathlib coverage remains unchecked. This is a process repair,
not progress beyond the inspected sources or toward an RH resolution.
