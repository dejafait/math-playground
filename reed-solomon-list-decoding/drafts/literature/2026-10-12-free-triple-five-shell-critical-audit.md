# Proposed critical audit of the free-triple shell exclusion

TARGET: Critically audit L055's free-triple shell exclusion, checking invariant averaging, every dual coefficient and the exact Schur contradiction without assuming RS safety.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 178 compared the exact critical-audit target with the inspected construction assessment, foundations/04,09,12, L055 and ATTEMPTS/035,036,037; reused step 176 primary searches and source inspections because the universe, fixed pairs, full-incidence zeros and spectral hypotheses are unchanged. No fresh general discovery or arithmetic audit was performed.
SOURCE_EVIDENCE: Reuse Polak [arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1) Section 1.1 (1)–(3), Proposition 1.1 and complete proof, p. 2, Section 1.2, p. 3; Brouwer–Polak [arXiv:1709.02195v1](https://arxiv.org/pdf/1709.02195v1) Section 2 (1)–(3), pp. 2–3; Schrijver [author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf) III.A (51)–(59), pp. 6–7; Brouwer–Haemers [author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf) Theorem 2.7.1(i), p. 36, Sections 1.4.7,11.2, pp. 19,162–163; Brouwer–Cioaba–Ihringer–McGinnis [arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2) Sections 1.2,3,3.4, pp. 3,10,12. All five direct primary PDFs retrieved in step 179; exact inspected cases and qualifications remain in foundations/04,09,12 and the construction assessment.
COMPARISON: Known sources cover the union-matrix definition, constraint-preserving finite averaging, simultaneous Johnson factor decomposition, tensor eigenvectors and positive-leading-block Schur congruence. They do not provide this fixed-pair/full-incidence finite verdict; L055 is the canonical local result and its independent critical verification remains pending.
GAP: No essential source gap remains for the saved audit. Research must independently check constraint preservation, Boolean normalization and p_5 positivity, all 36 relations and 20 free columns, every nonnegative dual weight and coefficient identity, and the strict constant Schur contradiction; arithmetic reconstruction is not yet a critical manuscript audit.
REASON: Approve exactly the saved critical-audit target by SPECIALIZE: all imported methods have adequate unchanged primary coverage, while the finite applicability and certificate-to-global-slice implication require independent local verification. No reproof of the hierarchy or spectral theorems is needed.

SCOPE: Critical review only of L055 as stated, with L053 fixed pairs, free unordered triple moments, forbidden-distance and entire incidence trial zeros, all anchors and no RS-safety conclusion.

## Original proposal (before step 178 approval)

The following proposal is preserved; its pending-approval language describes the startup state, superseded by the completed review below.

Essential inputs are L053,L054,L055 and foundations/04,09,12. Read only
the relevant source/theorem cases if the construction assessment is
insufficient for the critical-audit scope; reuse adequate coverage without
repeating general discovery. Compare ATTEMPTS/035,036,037 to delimit the
changed stop. No new theorem, script or reproof is authorized by this
REVIEW_REQUIRED proposal.

After approval, audit L055 independently from its exact hypotheses and
explicit 11-weight dual, reconstruct every one of the 20 columns and both
constant bounds, and inspect all essential certificates. Do not infer a
general packing bound or RS safety from a slice that zeros realizable
incidences. A full audit must also connect finite reconstruction to all
noninvariant feasible assignments by the stated symmetry argument.

Remaining assumptions and limitations: the entire incidence zero is a
trial restriction; other pairs and removing that zero are untested;
representing measures, uniform bounds below T, common-center realization
and safety at 67/68 agreements remain open. The 955–957 bracket is retained.
Full matching Mathlib coverage is not checked.

## Completed source comparison — step 178

LITERATURE_REASON: The newly proposed critical-audit target required separate approval of its load-bearing source scope; the unchanged construction coverage is reused rather than repeating browsing.

The main gap remains arbitrary-center safety at 68 agreements, with the
67-agreement gap independent. The intermediate target is a critical audit
of L055's exclusion of the fixed-pair/full-incidence free-triple slice.
Its downstream use is to establish whether that restricted repair is
rigorously parked and which hypotheses a different repair must change.
It cannot certify the general SDP optimum or RS safety.

**Source coverage and applicability obligations.** The precise primary
citations above are imports, not proposed reproofs. The construction
assessment [step 176](2026-10-12-free-triple-five-shell-feasibility.md)
records the actual searches, theorem passages and essential proof cases;
[foundations/12](../../foundations/12-global-degree-three-moment-source.md)
preserves Polak's constant-weight endpoint qualification and the
Brouwer–Polak nonnegative formulation and affine coefficient identities.
Union matrices concern real moment coordinates on the weight-68 universe,
with order three unrelated to interleaving. The audit need not import a
representing measure or the stronger full hierarchy to test the retained
necessary shell matrices.

Polak Section 1.2 permits averaging only when the group preserves the
constraints. L055's restriction uses region sizes rather than actual
subgroup-label determinants. The audit must check every fixed coordinate,
zero family and retained matrix under point permutations before invoking
this import. The primary coverage is sufficient for this check, but the
check itself is research for the next turn. An ordinary symmetric code
universe alone would not justify averaging a labeled RS feasible point.
Unordered triples must remain globally consistent; independent shell
variables may be used only as a relaxation in an exclusion argument.

[Foundations/09](../../foundations/09-global-pair-johnson-source.md)
records the full Johnson formulas and multiplicities, simultaneous
idempotents, tensor spectrum and the complete Schur triangular congruence.
The fixed factors remain J(68,5) and J(956,5), within n>=2d. Identity
relations use identity matrices; no loopless graph assumption is imposed
on the diagonal. All six factor indices and all 36 product modes remain
in scope. Schur congruence requires a positive leading block, not an
invertible shell, so singular lower blocks are allowed. L055's additional
normalization by p_5 requires independently verifying p_5>0 from L053's
fixed pairs; the audit must distinguish its normalized D-p_5 J from
L054's differently normalized C-p_5^2 J. No new spectral theorem or
source hypothesis arises from freeing the coefficients.

Schrijver's III.A tensor block theorem supplies the existing independent
beta-formula cross-check. [Foundations/04](../../foundations/04-constant-weight-triple-sdp-source.md)
retains actual-orbit ranges, Boolean repetitions, the t-s permutation
qualification and the unused suspect complement prefactor. The audit
must not import complement PSD or the stronger scalar program, and need
not resolve that unused prefactor. The finite nonnegative weighted sum
is to be checked directly through all 20 columns; no optimization
strong-duality theorem or numerical solver-status conclusion is required.
The optional primal sharpness certificate is not essential to exclusion.

**Duplicates and stops.** ATTEMPTS/035 records L053's small-principal
nonexclusion; ATTEMPTS/036 records L054's fixed-product exclusion;
ATTEMPTS/037 records L055's stronger free-triple restricted exclusion.
The construction assessment already searched the exact parameter and
prescribed-distance/free-triple terminology; no inspected theorem gave
this slice's verdict. Those searches are adequate for an audit of that
unchanged result; search failure is not evidence of novelty. No duplicate
new lemma is proposed. L055's 1318-check report is existing local evidence,
not a completed critical audit, and was not rerun or certified in this
literature turn.

**Continuation and abandonment test.** Approve one separate proof-audit
turn at the exact TARGET. Essential inputs are L053,L054,L055 and
foundations/04,09,12; inspect complete relevant rational certificate
values rather than previews. Retain the exclusion only after verifying
all 20 free columns, the 11 displayed nonzero dual weights (and zero
weights elsewhere), all 35 nonconstant inequalities, diagonal and
anchor normalization, exact required/upper row sums, and the passage from
arbitrary feasible assignments through constraint-preserving averaging
to the shell contradiction. If any identity, sign, normalization or
invariance step fails, record the precise defect and repair or withdraw
the affected implication; do not reject earlier small-principal results
or infer an RS counterexample. No such verification was performed here.

The entire incidence zero includes realizable triples and remains a trial
restriction. Off-shell moments are free and unused. Other pairs,
removing that zero, representing measures, full SDP bounds, common-center
RS realization and both safety gaps remain unresolved. The 955–957
bracket is unchanged. Full matching Mathlib coverage remains not checked.

## Direct-source repair — step 179

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs in this ready assessment; verify and attach the existing primary URLs without widening the audit target or repeating discovery.

All five primary URLs in SOURCE_EVIDENCE resolved to PDFs on 12 October
2026: Polak (15 pages), Brouwer–Polak (12), Schrijver (8), the
Brouwer–Haemers author preprint (253), and the Johnson eigenvalue paper
v2 (30). These are the same source versions cited by the construction
assessment and foundations/04,09,12. The repair also located Polak's
Section 1.1 definitions and complete Proposition 1.1 proof, Schrijver's
(59), Brouwer–Haemers Theorem 2.7.1(i), and the Johnson paper's Section
1.2 hypothesis n>=2d. Searches for the literal strings “averaging” in
Polak and “2 Semidefinite” in Brouwer–Polak did not match the extracted
text; no source gap is inferred from those failed text locators. Their
previously inspected cases are reused, rather than claiming a fresh
complete theorem review. No inaccessible source remains for this repair.

The main gap is still arbitrary-center safety at 68 agreements, with
67-agreement safety independently open. The unchanged intermediate target
is the L055 critical audit, whose downstream use is to validate the stop
on the fixed-pair/full-incidence repair. Retain that exclusion only if
invariant averaging, every dual coefficient and the exact Schur conflict
pass independent review; otherwise record the precise defect. The exact
continuation, essential inputs L053,L054,L055 and foundations/04,09,12,
complete certificates, and unresolved trial-zero/other-pair qualifications
above remain unchanged. ATTEMPTS/035,036,037 remain the recorded stops;
no duplicate lemma, new reproof or mathematical calculation is proposed.

This is a STALLED process repair, not new mathematical or theorem-comparison
progress. SPECIALIZE remains the existing source decision for the exact
TARGET. No critical audit was performed; full matching Mathlib coverage
remains not checked. The source URLs repair the reported readiness defect
without approving previously uncovered mathematics.
