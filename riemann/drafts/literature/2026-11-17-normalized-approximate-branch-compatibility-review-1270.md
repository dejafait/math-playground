# Normalized approximate branch compatibility — reviewed1271

TARGET: Review whether C032e's fixed full-theta branch pair admits normalized approximate compatibility in L2(0,infinity)^2, with delta=inf_{||G_+f||_2=1}||G_-f-cG_+f||_2 over complex compact smooth f.
CHECKED: 2026-11-17
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact theta/Volterra normalized-range searches and broader Hankel relative-bound/factorization searches found supporting operator theorems but no inspected theorem deciding this infimum; named local branch/Green reviews, stops and history1270 were compared. Queries, primary reading and limits appear below; no novelty claim.
SOURCE_EVIDENCE: Reused C032e/review1266 conventions and exact-uniqueness coverage; inspected Douglas1966 Theorem1/proof pp413-414, Guiver2025 Section1 and Theorem2.3(1)/proof, Bhuia2024 Section1.1 and Theorem7(3)/proof pp1777-1778, Lissy17Feb2026 Theorems1.1-1.2/Goal1.4 and Theorem2.1 statement, and Freedman2606.29555v1 C.1 normal-equation/limiting-transport passages.
COMPARISON: Exact injectivity, compactness and closure inclusion do not supply the requested relative bound or a unit-plus sequence. Douglas supplies an exact-range/majorization criterion conditional on bounded Hilbert-space realizations; Hankel factorization additionally needs a justified Hardy representation. The source's finite fits and Hardy truncations do not decide this two-component theta threshold.
GAP: Decide delta=0 versus delta>0 for the stated compact complex class and unweighted two-component output norm; verify output integrability, any auxiliary operator domains and compact-core transfer before using a theorem. Actual source norm, completed transport and Xi positivity remain separate.
REASON: Essential source comparison now supports one bounded mathematical attempt at the unchanged quantitative question; no matching theta conclusion can be imported from the inspected results. Apply named theorems only after checking their hypotheses, without reproving them or replacing the requested normalization by an input norm.
SCOPE: Fixed omega=1/4,z=i,c and full Psi of C032e; complex compact smooth f with no common support restriction or input-norm bound; same f in both sigma components and both signs; unweighted Y=L2((0,infinity),C2). Only output-domain checks, a justified auxiliary Hankel/range reduction and the zero-versus-positive threshold are covered; no uniform parameter theorem, source-metric identification or positivity bridge.
COVERED_TARGET: Attempt to decide whether delta=0 or delta>0 for C032e's fixed full-theta branch pair in unweighted L2(0,infinity)^2 over complex compact smooth f with ||G_+f||_2=1, verifying operator domains and retaining both components.
LITERATURE_REASON: The change from exact compact injectivity to normalized approximate compatibility required this operator-range/stability comparison; repeating Fourier uniqueness would not cover it. The covered attempt now has ready sources and needs no further routine literature turn.

## Completed source comparison — step1271

This is one LITERATURE turn, outcome EXPLORATION, classification
NOVELTY_UNCHECKED. It establishes source readiness for the covered
attempt, not a value or sign for delta, a new lemma, or progress beyond
the sources checked. No mathematical calculation or script was run.
The original nomination below preserves the exact diagnostic and its
downstream limitations; this completed assessment supersedes its
pending-source wording.

The main gap is L030-L032/C032a actual-Xi all-degree positivity.
The intermediate target is the unchanged normalized compatibility
threshold. Its plausible use is to distinguish a stable obstruction
from possible approximate common-profile compatibility before a
closure-based transport is pursued. Continue only with a uniform
positive lower bound or a controlled compact sequence having unit
plus-output norm and defect tending to zero. If the proposed range
reduction fails, record the precise failed hypothesis and stop that
reduction; do not substitute exact injectivity or finite-grid evidence.

### Primary comparisons and qualifications

1. **Douglas.** R. G. Douglas, *On majorization, factorization, and
range inclusion of operators on Hilbert space*, Proc. Amer. Math.
Soc. **17** (1966), 413-415, Theorem 1 and proof pp.413-414,
[primary scan](https://home.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf),
DOI [10.1090/S0002-9939-1966-0203464-1](https://doi.org/10.1090/S0002-9939-1966-0203464-1).
For bounded A,B on a real or complex Hilbert space, the equivalent
conditions are ran A contained in ran B, AA* <= lambda^2 BB* for
some finite lambda>=0, and A=BC for bounded C. Read all three
implications, including the closed-graph construction and extension
from ran B*. This is actual range inclusion, without taking closures;
closed range is not a hypothesis. The original AMS endpoint returned
403; the complete original scan was accessible. Review1264 had already
used this theorem for a different norm inference. Here it is reused
as a conditional relative-bound tool, not a theta-specific result.
Choosing adjoints, domains and any direct-sum realization is work for
the subsequent attempt. No automatic factorization constant or
positive delta is imported.

2. **Integral Hankel domains.** Chris Guiver, *Regularity and
Compactness Properties of Integral Hankel Operators and Their Singular
Vectors*, Complex Anal. Oper. Theory **19**, article 6 (2025),
[Section 1, (1.2a), Theorem 2.3(1) and its proof](https://link.springer.com/article/10.1007/s11785-024-01627-w).
For a Hilbert value space U and Bochner-integrable h with values in
compact operators almost everywhere, the sum-kernel map
Gamma v(t)=integral h(t+s)v(s)ds is compact on Lq(R+,U),
1<=q<infinity. The proof's finite-dimensional case is cited to its
reference [8], Appendix 1 p.895; its general case uses norm
approximation by tensor kernels. That reference was not independently
read. The additional Sobolev clauses were inspected as context, not
imported. An auxiliary change of input variable may expose such
sum-kernels, but the original denominator Psi(s) cannot be ignored:
domain equivalence and preservation of the compact test class must
be justified. Compactness in an auxiliary input norm gives no
comparison between the two required output norms. No domain or
compactness theorem for the nominated pair is established this turn.

3. **Stronger structured range result.** Sudip Ranjan Bhuia,
*Factorization of Hankel operators, range inclusion of Toeplitz and
Hankel operators on the vector-valued Hardy space*, C. R. Math.
**362** (2024), 1773-1778,
[Section 1.1, Theorem 7(3) and complete case-(3) proof](https://www.numdam.org/item/10.5802/crmath.680.pdf).
For bounded operator-valued circle symbols Phi1,Phi2 on a separable
complex value space, ran H_Phi1 contained in ran H_Phi2 is
equivalent to H_Phi1=H_Phi2 T_Omega with bounded analytic Omega.
The proof uses Douglas and a shift-intertwining lifting, then an
analytic Toeplitz multiplier. This is stronger structure after range
inclusion, not a theorem declaring inclusion for arbitrary kernels.
No unitary identification of the nominated rectangular pair, its
adjoints and these Hardy operators is currently established. Thus
this result is a comparison rather than an imported answer; neither
the scalar nor separate-component version may replace the joint test.

4. **Closure versus norm control.** Pierre Lissy, *Hybrid range
inclusions: a generalization of Douglas' theorem, with an application
to control theory*, author version dated 17 February 2026,
[Section 1.1, Theorems 1.1-1.2, pp.1-2](https://cermics.gitlab.enpc.fr/lissy/Publi/Douglas-Lemma.pdf).
For bounded A:H1->H3 and B:H2->H3 between Hilbert spaces over the
same field, Theorem 1.2 equates closure inclusion of their ranges
with ker B* contained in ker A*, allowing approximation of each
fixed Ah1 without a bound on the approximating input. This contrasts
with the quantitative criterion in Theorem 1.1. Also inspected
Goal 1.4 and Theorem 2.1's statement: the mixed problem fixes a first
output exactly while approximating a second with the same input.
That has different quantifiers from a unit-norm first output whose
direction may vary. The full mixed-theorem proof was not read and
the theorem is not used. No conclusion about the nominated infimum
follows from merely citing either closure or mixed controllability.

5. **Original model and numerical overlap.** Reused review1266's
full-theta conventions; newly checked the
[Freedman2606.29555v1 Appendix C.1](https://arxiv.org/html/2606.29555v1#A3.SS1)
limiting-transport and continuous/coupled normal-equation passages.
The Hardy truncation is a strong approximation on the Hardy side;
the corresponding Volterra map is still requested. The displayed
continuous features and finite inverse/coupled fits supply no theorem
for the present normalized infimum over all complex compact inputs.
No reported residual or claimed normalized-model certificate is
imported as a bound in the fixed unweighted output space. This is
the specific source overlap, not a claim that all possible
approximation theorems in that manuscript have been ruled out.

### Bounded searches, duplicates and failures

Queries actually used included `Douglas range inclusion 1966
factorization pdf`, `Hankel operators relative boundedness range
inclusion approximate null sequence integral kernel`, `theta kernel
Hankel range density`, `2606.29555 approximate range L2 branch`,
`theta Hankel approximate range operator`, and `G_sigma Xi 2606.29555
normalized compatibility`. Exact-statement searches returned no
inspected matching theorem. The broader results above were inspected
at theorem level; a failed search is not evidence of novelty.
Yafaev's quasi-diagonalization, Hankel restriction/localization papers
and other search hits were not inspected as theorem inputs and are
unread leads, not missing premises for this bounded range attempt.
The accessible primary comparisons suffice for a mathematical test;
there is no essential source-access blocker to carry forward.

Scoped local searches compared the November17 branch/Green reviews
and ATTEMPTS records, C032e's hypotheses/bounds and history1270.
Read review1266's feature/uniqueness/overlap comparison and the two
named stops, plus review1264's Douglas scope. No reviewed local result
settles the normalized threshold. C032e excludes compact exact
solutions; it expressly leaves quantitative approximation open.
The Green-mass stop concerns a different unidentified minimizing
map and remains parked. The new range test does not revive that
representation or infer failure of actual-theta positivity from C032d.

### Ready attempt and stopping boundary

First verify that the compact test profiles belong to the specified
Y, using existing full-theta bounds. If auxiliary bounded operators
are introduced, identify their input Hilbert space and compact core
explicitly; division or multiplication by Psi may not be treated as
a bounded global isometry. Check norm-continuity and compact-core
transfer before applying Douglas. Then test a relative output bound
or its failure, retaining one common input and both sigma outputs.
This is proposed specialization work, not a reduction proved or
approved as correct here. Cite the existing operator theorem when
applicable; do not reprove it. A failed domain/core argument is an
unfinished attempt, and compactness or adjoint-kernel information
alone does not meet the continuation threshold.

The covered attempt is proof_attempt/development, not creative:
it develops a known range mechanism for this fixed diagnostic.
No justified new central-sign construction has emerged; the missing
independent positive representation and actual-Xi bridge remain the
blocker to a protected creative target. Do not relabel this routine
operator specialization to satisfy scheduling preferences.
Mathlib coverage of the full pair problem and supporting operator
results is not checked; no absence or Lean verification is claimed.
No cross-notebook input, new lemma, mathematical script, PROOF or DAG
change is needed. Literature uses zero mathematical exploration turns
and claims no reset of supervisor counters.

## Original nomination1270 — preserved

## Precise proposed test

Keep omega=1/4, z=i, c=Xi(3i/4)/Xi(5i/4), the full
Psi(s)=K(s/2)/2 and G_{sigma,tau} from C032e (1)-(2). For
tau in {-,+}, write

\[
 \mathbf G_\tau f=(G_{-1,\tau}f,G_{+1,\tau}f),\qquad
 Y=L^2((0,\infty),du;\mathbb C^2),
\]

with the unweighted direct-sum norm
\(\|v\|_Y^2=\int_0^\infty(|v_{-1}(u)|^2+|v_{+1}(u)|^2)\,du\).
The nominated quantity is

\[
 \delta=\inf\left\{
 \|\mathbf G_-f-c\mathbf G_+f\|_Y:
 f\in C_c^\infty((0,\infty);\mathbb C),\quad
 \|\mathbf G_+f\|_Y=1
 \right\}.
\]

The task is the zero-versus-positive question, not the exact numerical
value. The two branch components use the same f. Arbitrary complex
cancellation is retained. No fixed support interval, bound on an input
norm, identification with a source trace norm, or restriction to
nonnegative f is implicit. These hypotheses must not be silently
changed to obtain coercivity. Output-domain applicability must be
checked before using a primary operator theorem. The displayed norm
is an explicit diagnostic; its relation to the completed source metric
is still unresolved.

The decisive evidence in a later approved attempt would be either a
proved uniform lower bound delta>0 or a rigorously controlled sequence
with unit plus-profile norm and defect tending to zero. A finite fit,
injectivity alone, or an unnormalized small output is insufficient.
The latter could result from scaling all outputs to zero and would
not meet this test. No such bound or sequence is asserted here.

## Relevance, source work and limits

Main gap: L030-L032/C032a actual-Xi positivity in every degree.
This range test would distinguish a stable obstruction from possible
approximate compatibility of the prescribed pair, which matters before
investing in a closure-based common-profile bridge. Even a zero defect
infimum would leave convergence in the actual source norm, a common
isometry, other evaluation points, uniform parameters, signing,
graph realization and initialization open. It is not itself a central
positivity mechanism or an RH candidate.

The compact exact route is closed by C032e's accepted audit1270.
This proposed approximation question has a different, independently
testable threshold. It does not need the missing Green minimizing-map
representation; no Green mass calculation is reopened. The precise
stops in ATTEMPTS/2026-11-17-compact-exact-branch-transport-stop-1268.md
and ATTEMPTS/2026-11-17-theta-green-positive-kernel-source-limit-1266.md
remain evidence, not global bans on different profile classes.

Before approval, search the exact and stronger normalized range
statements, standard analytic Hankel/operator-pencil terminology and
known stability obstructions. Compare the named local branch/Green
assessments and their recorded failures first. Retrieve primary
theorem hypotheses and essential proof cases for any proposed range,
closed-range or approximate-nullspace result. Reuse review1266's
feature conventions; do not repeat its discovery searches as though
they covered this norm question. No source numerical fit is proof.
Import a matching result with only the required applicability argument;
if coverage is missing, retain REVIEW_REQUIRED or document a bounded
EXPLORE gap before a separate mathematical turn.

Essential local inputs for the future test are C032e,L016,L018-L020;
the existing primary feature comparison is in review1266. The original
source is Freedman, *Finite-core Volterra reductions for a Weyl-positive
Riemann phase kernel*, arXiv:2606.29555v1, Appendix C.1,
https://arxiv.org/html/2606.29555v1#A3.SS1. This is a previously recorded
lead, not a newly inspected approximation theorem. Full Mathlib
coverage is unknown. No cross-notebook input is proposed.

Route next to literature_comparison, standard/high. No justified
creative central-sign construction follows from the accepted audit;
an independent positive representation and actual-Xi bridge are still
missing. This bounded range nomination is not labeled creative to
meet scheduling preferences. Its source gate must be completed before
any calculation or new lemma.
