# Continuum positive-output moment specialization: continuation1547

TARGET: Specialize C032k's moment criterion to C032q's continuum law: for every mass-one finite real signed eta on [1,2] with nu_eta nonnegative, prove that J_eta identically zero is equivalent to one finite positive exponential moment and implies every positive exponential moment, using only the output law for moment integrals.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1547 completes assessment1546's changed continuum comparison; queries, duplicate checks and source qualifications are recorded in drafts/literature/2026-11-18-continuum-moment-source-notes-1547.md. C032k covers the finite case, while C032m/p/q supply continuum analytic and measure interfaces. No novelty or feasible-measure conclusion is inferred.
SOURCE_EVIDENCE: Boyer2015 Definition2.1/Lemma2.2 and complete proof/p6 https://maths.jbboyer.fr/documents/articles/renewal.pdf ; Mimica2015 Laplace transform Definition1.1/Remark1.2/p5, Proposition1.4(i)-(ii) and relevant proofs/pp6-7 https://web.math.pmf.unizg.hr/~amimica/lt.pdf . Reuse C032k Section2/audit1302 and C032m/q's checked entire/parity and bounded Laplace identities, with the named identity theorem, Cauchy estimates and monotone convergence theorem.
COMPARISON: The imported tools concern a positive output measure, irrespective of its mixing representation. Only their applicability and C032k's existing even-entire/moment-series argument require specialization. Boyer alone is forward-only; Mimica supplies the positive-s derivative and zero-limit inputs. No reproof of a general analytic theorem is justified.
GAP: Establish the proposed local conditional equivalence with both directions and all inherited qualifications; verify even-lift descent in the s variable and retain positivity at every moment limit. The statement is unproved for the continuum in this literature turn.
REASON: This bounded interface can interpret the audited cone criterion independently of deciding feasibility. Source coverage is sufficient, so after separate approval the next substantive work should be mathematics, with no additional source search under unchanged hypotheses.
SCOPE: C032j/k/m/p/q; W=[1,2], X=[0,infinity), real finite signed Borel eta with eta(W)=1 and arbitrary finite variation; atoms and singular parts allowed; nu_eta>=0 and full complex J_eta. All inherited fixed-v1/divisor/multiplicity/counting/finite-zero/heat-positivity qualifications remain. No density, zero-atom exclusion or moment is assumed in advance.

This ready continuation was written during literature-only turn1547 and
requires separate next-turn approval. It is not executed or proved here.
Classification for the future specialization is REPRODUCTION. The
general mathematics is known; no novelty is claimed for the interface.

Reuse C032q's signed law, its mass and bounded positive-real Laplace
identification; do not reconstruct the kernel or re-audit its cone proof.
Reuse C032m's entire F_eta and its exact full-complex parity identity.
Compare the two directions with C032k Section2. Boyer's transform uses
exp(-zy), so the direct Laplace variable is z=s; an opposite convention
requires an explicit reflected definition. Do not copy an unexplained
minus sign. Entire descent from w to s must be justified, rather than
assumed from an entire lift before evenness is known.

For the converse, the imported derivative and right-limit tools apply
to the finite positive law nu_eta, including a possible atom at zero.
The future argument must spell out the entire Taylor convergence and
the positivity-dependent series passage just as C032k does. No
unbounded-test identity through eta is available from C032q. In
particular no expression subtracting infinite component moments is
admissible. No new mathematical script is needed for this target.

Continue only if both directions follow from these exact interfaces
without a new uniform tail estimate or growing-test width interchange.
If a missing premise is found, record it and qualify or abandon that
implication rather than infer it from analytic continuation alone.
This test does not construct eta, decide cone membership, supersede
finite stop1302, reopen stops1534/1536/1538, or transfer any law to Xi.
Full matching Mathlib coverage remains unknown. No new central creative
mechanism is justified: no concrete inequality or representation
deciding the actual cone or Xi signs has emerged from this comparison.
