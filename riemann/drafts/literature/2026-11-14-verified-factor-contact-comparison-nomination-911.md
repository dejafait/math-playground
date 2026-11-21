# Verified-factor contact comparison: completed source review912

TARGET: Assess whether one-factor deconvolution r_lambda=p+lambda^{-1}p' at the verified rates lambda in C466b's M_100 yields an actual-density determinant comparison implying (22), without global PF or a degree-growing verified-factor budget.
CHECKED: 2026-11-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review912 searched signed/formal Christoffel Hankel determinants, Darboux functional perturbations, exponential deconvolution and reciprocal-Xi terminology; inspected the primary statements and relevant cases below and reused assessments884/888/889/898/899. No matching arbitrary-order actual contact inequality was located; no novelty inference.
SOURCE_EVIDENCE: Sra arXiv:2611.02944v1, Theorem C.20 and full proof pp41-42, Theorem3.4 p10 and Theorem C.9 statement/proof pp27-29; Krattenthaler arXiv:2101.04225v5, Theorem1 p2, Section2.2 pp6-7, Proposition5/proof pp13-14, Lemma6/proof pp14-15 and Section6 pp18-20; Bueno--Marcellan author preprint dated23August2006, Definition pp1-2, Lemma2.1/Remark2.2 pp6-7, Lemma3.1/Proposition3.2/Theorem3.3 and shifted extension pp10-13. Version distinctions and precise limits below.
COMPARISON: The verified-factor residual law is covered by Sra C.20; signed Christoffel/Darboux formulas provide algebraic relations subject to nonsingularity/pivot hypotheses, not the parity-dependent actual estimate in C466b(22). Sra's determinant smoothing still requires n>=2m and its additional factor-budget inequality. None of these statements supplies the requested fixed-factor arbitrary-order comparison.
GAP: The actual signed endpoint budget (22) remains unproved. The narrow proposed identification of each one-factor residual with p+lambda^{-1}p', including its endpoint regularity and multiplicity bookkeeping, still needs a written applicability audit; no transformed higher-order signs follow from scalar residual positivity.
REASON: Park automatic determinant-sign import. Source coverage is complete for a separate, bounded known-result admissibility audit nominated in assessment912; do not repeat finite integration by parts or invoke a global-PF assumption. SPECIALIZE covers only that identified difference, not a new sign mechanism or an approval of (22).
SCOPE: Source review only for the finite multiset M_100 and arbitrary finite m>=2 under C466b's actual-density and hypothetical-contact conventions; preserve multiplicities and deletion of exactly one first-zero occurrence.
LITERATURE_REASON: Changed target from finite endpoint integration by parts to actual verified-factor deconvolution and signed determinant transport; the primary comparison and any all-order sign input are uncovered.

## Completed review912, 14 November 2026

This is a literature-only NEGATIVE source comparison, KNOWN_IMPORTED.
The new evidence closes the proposed automatic Christoffel/Darboux sign
import and identifies an explicit primary residual-law theorem. It is
local progress in source scope, not a new mathematical discovery, a
counterexample to actual F_100>=0, or a proof that factor methods cannot
help. No new transform identity, contact inequality or lemma was derived.
The preceding LITERATURE_REASON records the invocation-start coverage gap;
the inspected evidence below resolves access for the narrower admissibility
question. The original nomination retained below is provenance only.

### Primary sources and exact applicability limits

Suvrit Sra, *On some positivity properties of the Riemann Xi function*,
[arXiv:2611.02944v1](https://arxiv.org/pdf/2611.02944v1), submitted
2 November 2026, 53-page version: Theorem C.20, pp41-42, extracts the
finite multiset of verified exponential factors with one anchor occurrence
retained. It requires 100<=U<=U_PT and an anchor satisfying
2<=gamma_*^2<=U^2/4-1/4. Repetitions count with multiplicity.
The independent residual is positive and self-decomposable, with smooth
positive density on (0,infinity). Its transform is P_U/h.
Read the full proof, including positivity/decrease of the retained kernel,
transform multiplication, and the finite-removal regularity argument.
Theorem3.4 p10 and Theorem C.9 pp27-29 require n>=2m and
(n-2m+1)/2>=sqrt((m-1)(n-m+1)); n>=8m suffices, alongside the
weighted signed-error threshold <1. Read the moving-frame bound and
support-boundary/inertia cases. These are not a fixed-factor all-order
contact comparison. No independent audit of the full manuscript or finite
certificates is claimed.

For local applicability, C466b's M_100 is the multiset in C.20 when the
anchor is precisely the one first-zero occurrence already retained there.
C466a uses the probability density p=c_0 Theta, matching the normalized
S_1 law. Extracting *all* M_100 factors and removing a *single* chosen
factor are different operations: the latter requires putting back the
other factors, with their multiplicities. Connecting that residual law
to the proposed derivative expression remains a mathematical task, not
a theorem proved in this review. The inspected theorem asserts no
arbitrary-order sign for the residual's derivative determinants.

Christian Krattenthaler, *Hankel determinants of linear combinations of
moments of orthogonal polynomials, II*,
[arXiv:2101.04225v5](https://arxiv.org/pdf/2101.04225v5),
10 September 2021: Theorem1, p2, assumes monic orthogonal polynomials
over a characteristic-zero field with every squared norm nonzero. Its
formula (1.1) expresses a polynomially modified Hankel determinant as
a determinant of polynomial evaluations divided by a Vandermonde and
the original Hankel determinant. Section2.2 pp6-7 gives the classical
Christoffel relation. Proposition5 and proof pp13-14 handle repeated
modification nodes by confluent derivatives; this is not permission to
divide by a vanishing base determinant. Read Lemma6's triangular
basis-change proof pp14-15 and Section6's Heine/Vandermonde proof
pp18-20: they supply identities, not a signed inequality. The
positive-measure interpretation in Section2.3 has an extra positivity
hypothesis.

At C466b's contact the size-m base determinant is zero. Thus the quoted
full quasi-definite theorem cannot simply be applied there. Lower-size
minors remain nonzero; a finite truncated or cleared-denominator identity
may still be possible. This comparison does not rule those out. Neither
form signs the endpoint pairing in (22). Assessment889 and C466c already
exclude substituting a positive raw-moment/root theorem for these signed
derivative data; no new root or determinant result is asserted here.

M. I. Bueno and F. Marcellan, *Darboux transformation and perturbation
of linear functionals*,
[author primary preprint](https://web.math.ucsb.edu/~mbueno/papers/darbouxLAA.pdf),
32 pages, bearing 23 August 2006: quasi-definiteness is defined on
pp1-2 by nonsingularity of every leading moment block. Lemma2.1 and
Remark2.2 pp6-7 identify nonzero polynomial evaluations as the no-pivot
LU condition. Read the finite boundary correction in Lemma3.1 p10,
Proposition3.2 and proof pp10-12, Theorem3.3 p12, and shifted extension
pp12-13. The infinite theorem assumes quasi-definiteness and nonzero
evaluations throughout; it transfers Jacobi matrices. It asserts no
order relation between the required signed contact determinants.
The finite version retains a boundary correction, and no simple UL
swap may suppress it. The published article is
[Linear Algebra Appl.384(2004),215-242, DOI10.1016/j.laa.2004.02.004](https://doi.org/10.1016/j.laa.2004.02.004);
the theorem locators above refer to the inspected author preprint,
whose displayed date differs from publication. No numbering equivalence
with the published pagination is assumed.

### Search, duplicates and access

Executed queries included `"Hankel determinants" "Christoffel" "linear
functional" sign`, `"Polya frequency" "deconvolution" exponential`,
`Krattenthaler "Hankel determinants" "linear combinations" II arxiv`,
`Christoffel transformation quasi definite functional determinant nonzero
singular Hankel Darboux arxiv`, `"exponential" "deconvolution" "total
positivity" density`, and `"Hankel" "first contact" "Christoffel"`.
Search snippets, abstracts, statistical deconvolution hits and unrelated
results were discovery only. The 2021 associated-polynomial and matrix
biorthogonal transformation papers remain unread leads; no conclusion
depends on their hypotheses. No exact matching source was found in this
bounded search, which establishes no originality or impossibility.

Read C466b's complete relevant reduction and (15)-(22), C466a's source
hypotheses and source-scope text, C466c's finite-jet result and C466e's
stated generic contact contrast. Reused assessments884/888/889 and the
cumulative assessment898/completion899. Narrow reciprocal/contact-path
search found assessment903: its Mobius source blocker concerns another
mechanism and does not block C.20. No sibling notebook was read.
The generic countermodels do not refute this actual-density target.

The author-v3 PDF and Hub v1 direct requests failed in this review;
the accessible arXiv v1 above removes the essential source-access gap
for the stated factor theorem. Do not equate version numbering or use
uninspected claims from another version. Krattenthaler's v2 HTML was
unavailable; the v5 PDF was accessible. PDF screenshot requests produced
no visible page images; all reported reads use the readable extracted
theorem/proof text, not an image preview. Mathlib coverage of the full
matching factor/contact comparison remains unchecked; the prior compact
convolution differentiation coverage is supporting only.

### Decision and continuation

The main gap remains L030-L032/C032a. A paid finite-head sign would
help C466b(7), while first-zero signed mass, full tail, strict forcing,
simultaneous contacts, propagation and Xi transfer would remain open.
The discriminating source test fails for automatic determinant signs:
the inspected identities and factor theorem supply no actual estimate
reaching (22). Preserve this scoped stop; additional algebra alone is
not a reason to reopen it.

One independently checkable prerequisite is now source-covered: audit
the proposed one-factor density identification against C.20 and the
actual smooth p. Assessment912 specifies that bounded known-result
application. Positivity of that residual alone is expressly insufficient
for the reviewed determinant target; do not report it as payment of (22).
It can supply a legitimate input for a later actual-specific mechanism.
The new assessment requires separate next-turn approval before research.

No justified creative sign mechanism is ready: a noncircular coercive
estimate for the transformed signed derivative pairing is still absent.
This is the blocker to creative routing, not a global ban on factor
methods. Reopening the sign route requires a new actual estimate with
a test against (22), not global PF, an assumed transformed PF sign,
a real-root premise or a factor budget growing with m.

## Original nomination (preserved)

## Concrete proposed test, not a result

C466b(22) is the exact remaining finite-head budget. Investigate one
verified real-zero factor at a time, with lambda in its M_100, by
comparing primary results on the transform (1+s/lambda)/h(s) and the
proposed function r_lambda=p+lambda^{-1}p'. Their precise functional
identification, positivity, smoothness and transform hypotheses must
be justified before use; they are not new conclusions of this
nomination. No higher-order PF sign for r_lambda is assumed.

Seek a contact comparison for derivative Hankel determinants under
this single-factor operation, including signed Christoffel/Darboux
transformations if relevant, and compare its actual hypotheses with
the endpoint data in C466b. Positive raw moment theorems cannot simply
be substituted for the signed derivative functional. The intended
downstream use is to control the surviving finite-head remainder,
not to reproduce already cited finite-order PF smoothing.

The discriminating source test is whether the comparison supplies an
independently checkable actual-density estimate that reaches (22).
Stop this candidate if it only requires the same unproved PF_m sign
for r_lambda, assumes real-rooted P or global PF, restates (22), or
uses a number of verified factors growing with m. Positivity of a
single transformed density alone is not the requested determinant
comparison. Do not approve mathematics merely because an algebraic
transformation formula exists.

The existing assessment884 explicitly records the order-dependent
finite-factor limitation. Assessment889/C466c distinguishes signed
derivative jets from positive raw moments. Assessments888/898 park
automatic variation/cumulative imports; C466d/e refute universal
scalar/contact arguments within their stated generic scopes. Reuse
these comparisons and assess the actual factor operation rather than
repeating those routes. No generic model replaces the actual density.

Essential input IDs for a later attempt would be C466a and C466b,
with L018's inherited completion convention. C466c-e are contrasts,
and C466g is boundary motivation only. The source counting, verified
low-zero and multiplicity qualifications remain external inputs.
Actual contacts, transformed-density admissibility at all chosen
rates, transformed higher-order signs, the endpoint budget, signed
first-zero mass, full tail, strict forcing, simultaneous contacts,
propagation and L030 transfer are not established here.

Creative discovery was considered because this comparison could use
actual factor structure absent from a bare scalar envelope. It is
only a source-review candidate: no sufficiently justified new sign
mechanism is yet available for proof_attempt/creative routing. A
future creative nomination would need a precise noncircular estimate
and bounded test after this coverage decision. Mathlib coverage of
the exact proposed comparison is unchecked. No theorem, proof or
mathematical script for this changed target was produced in step911.
