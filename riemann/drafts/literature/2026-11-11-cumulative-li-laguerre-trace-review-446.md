# Cumulative Li-test arithmetic trace: completed source comparison

TARGET: Assess a Christoffel–Darboux reduction of the cumulative Li-test autocorrelation for a separately estimable signed prime remainder toward L984, retaining the ordinary unweighted degrees 2 through n and all cutoff, pole and archimedean terms.
CHECKED: 2026-11-11
DECISION: IMPORT
SEARCH_EVIDENCE: Step447 searched Li/cumulative Laguerre/Christoffel–Darboux/Weil quadratic prime sums and autocorrelation; read the precise NIST kernel and normalization, Suzuki's individual identity and Lagarias's published Appendix A cutoff warning. Reused reviews231/235/445 and their scoped failures; no matching signed cumulative estimate was inspected and no novelty/nonexistence inference is made.
SOURCE_EVIDENCE: NIST DLMF18.2(i),(iii),(v), equations18.2.5,18.2.12–13 and Table18.3.1 Laguerre row, live 11Nov2026, https://dlmf.nist.gov/18.2#v and https://dlmf.nist.gov/18.3 ; cited proof reference Szego1975 Thm3.2.2/(3.2.4) not separately read. Suzuki arXiv2301.05779v2,p1/(1.1)–(1.4),p2 qualification and Section4.1; Lagarias AIF57(2007),AppendixA/(A.3)–(A.7),pp1735–1738, https://www.numdam.org/item/10.5802/aif.2311.pdf , inspected source statements and cutoff cases; details below.
COMPARISON: The classical kernel has reciprocal squared-norm weights; Laguerre alpha1 norms are Gamma(d+2)/d!, not a common degree-independent normalization. Suzuki's ordinary Li observable uses the unnormalized g_k. Lagarias explicitly requires regularized covariance rather than a separately finite trace on Li tests. Neither kernel positivity nor these identities supplies a signed unweighted cumulative arithmetic estimate.
GAP: L984's every-epsilon/all-n lower bound for c_n remains unpaid. No matching finite signed comparison with a controlled degree/cutoff error was found. A weight conversion, multiplicative autocorrelation reduction, pole cancellation or arithmetic estimate has not been derived in this literature step.
REASON: Import the inspected theorem scopes only and park this direct Christoffel–Darboux payment route: it fails the stated continuation test. This is new source-scope evidence, not a new mathematical obstruction theorem or a ban on other estimates. The next nomination uses a different local-operator source lead.
LITERATURE_REASON: The proposed cumulative quadratic autocorrelation and its exact classical-kernel weighting are outside the assessed linear-average and individual-negative-direction scopes. Essential primary coverage is missing, so the next step is literature-only despite the balance target.
SCOPE: Completed literature-only comparison, classified KNOWN_IMPORTED. IMPORT covers source scope and its qualifications only; it does not authorize a new convolution identity, kernel specialization, signed estimate, mathematical script or numerical diagnostic. The original nomination below is historical and is superseded by the completed comparison.

## Original nomination

The main gap remains actual-Xi positivity L030–L032/C032a, arithmetic
forcing L966/L968 and L984(H). Essential local inputs are L018's
completion and L984's ordinary c_n=sum_(k=2)^n lambda_k with its
every-epsilon/all-n lower threshold. The cited individual g_k identity
is a source input; its cumulative arithmetic use has not been justified.
No density, innerness, positive spectrum, off-line zero or signed
arithmetic error is assumed. No cross-notebook result is needed.

Retrieve the exact classical theorem, coefficient weights and Laguerre
normalization before loading a longer source proof. Distinguish an
orthogonality-weighted kernel from the unweighted sum of ordinary Li
tests; a changed weighting or divided Li sequence does not match the
target. Retain degree1 subtraction, endpoint values, multiplicities,
multiplicative convolution, and all pole/archimedean/prime contributions.
Fixed-degree cutoff convergence is not a uniform growing-degree budget.

Plausible downstream use: a signed remainder or comparison on the actual
arithmetic side could provide a bounded test of one component of L984's
unpaid upper bound. All-n control and independent actual-Xi forcing
would remain unresolved. No complete route to RH is claimed.

Continue only if the source comparison identifies that component, its
exact hypotheses and a concrete finite inequality with all errors and
a decisive threshold for a later attempt. Park an identity-only,
wrong-weight, uncontrolled-cutoff or RH-assuming completion. If no such
test emerges, do not cycle through more kernel identities; select an
independently testable mechanism. The blocked nonprimary blog in
review231 is neither a premise nor a source-access task to repeat.

No justified creative attempt is yet ready: the arithmetic signed
comparison is undefined and its source scope unread. If coverage
exposes one, nominate proof_attempt/creative only with a bounded test
and precise central-gap escalation, in a separately approved assessment.
Full matching Mathlib coverage remains unknown.

## Completed comparison — step447, 11 November 2026

The main gap remains actual-Xi positivity L030–L032/C032a and the
independent forcing/arithmetic inputs L966/L968 and L984(H). The
reviewed intermediate target was an independently estimable signed
component of the cumulative Li autocorrelation. Its potential use
was L984's lower envelope, not just a finite sign or an identity.
The continuation test in the nomination is not met.

### Exact classical source contract

Inspected [DLMF18.2(i),(iii),(v)](https://dlmf.nist.gov/18.2#v):
positive orthogonality measure with finite moments, squared norms
h_d, leading coefficients k_d, and the finite identity18.2.12

    K_N(u,v)=sum_(d=0)^N p_d(u)p_d(v)/h_d
      =k_N/(h_N*k_(N+1))
        *[p_(N+1)(u)p_N(v)-p_N(u)p_(N+1)(v)]/(u-v), u!=v.

Equation18.2.13 gives its confluent derivative form at u=v. No
positivity for an arbitrary signed functional follows from either
identity. The displayed proof reference is Szego, Orthogonal
Polynomials, fourth edition1975, Theorem3.2.2 and (3.2.4); that book
proof was not separately inspected and is not reported as audited.
The finite classical formula is imported from the inspected NIST
statement, without reproof or a new specialization.

[Table18.3.1](https://dlmf.nist.gov/18.3#T1) gives, for degree d,
Laguerre weight exp(-u)u^alpha on (0,infinity), alpha>-1,
h_d=Gamma(d+alpha+1)/d!, k_d=(-1)^d/d!. Alpha1 is admissible,
but its h_d varies with d. Thus the source's inverse-norm-weighted
kernel is not the proposed unweighted Li-family kernel. This is a
comparison of source conventions, not a proof that converting weights
is impossible. We do not perform that conversion or assert that it
preserves a signed arithmetic inequality. Live DLMF was inspected
11Nov2026; no historical snapshot is claimed. Its .tex endpoint was
unsupported by the browser; the HTML rendered the complete formulas
and Laguerre row, so no essential source blocker remains here.

### Li normalization and the essential cutoff case

Reuse [Suzuki2301.05779v2](https://arxiv.org/pdf/2301.05779v2),
14June2023, p1/(1.1)–(1.4) and p2: ordinary lambda_k, multiplicities
and symmetric height summation, real g_k with value k/2 at1, and
the unconditional identity W(g_k *_mult g_k^*)=2lambda_k.
Here g_k^*(x)=x^(-1)overline(g_k(1/x)); this is multiplicative
convolution, not the pointwise product in a polynomial kernel.
Degrees2 through n and the omitted degree1 must be retained in
any later use. Section4.1, pp12–13, discusses the unresolved
unconditional relation to the model-space functions; it supplies
no quantitative arithmetic trace bound. Review445 already covers
the individual identity; it is not a new local result in this step.

Newly inspected [Lagarias2007, AppendixA](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=48),
printed pp1735–1738/PDF48–51, distinguishes the trace functional
T[f]=fhat(0)-W[f]+fhat(1), its place contributions, and the covariance
form W[f]=-sum_v W_v(f)+W_0(f)+W_1(f). The latter accommodates
singular Li tests only with coordinated cutoffs at1/T and T. The
paragraphs after(A.7) expressly retain divergent pole and prime
contributions whose cancellation defines the extended functional.
The final page identifies P_k(log x)=L_(k-1)^(1)(-log x), supporting
the Laguerre convention without relying on the unread blog.

This is inspection of the published statements and their essential
singular-test qualification, not an audit of Bombieri–Lagarias1999's
regularization proof. We use only the abstract endpoint labels
W_j=fhat(j); the web transcription of the integral displays beside
those labels is not used for a formula-sensitive specialization.
No assertion that individual endpoint terms are finite is imported.
Nor do we extrapolate the warning into a new theorem about the
specific cumulative autocorrelation: its compensated finite formula
and uniform error remain to be established. No cancellation, sign
or estimate is silently supplied by calling the observable a trace.

### Search boundaries, failures and decision

Queries executed: `Li coefficients cumulative Laguerre Christoffel
Darboux Weil quadratic form prime sums`; `"Li coefficients"
"Christoffel" "Darboux"`; `"Li" "Laguerre" "covariance" cumulative`;
`"Li coefficients" "autocorrelation" prime`. Searches re-exposed
review231's blocked kenan.works lead. Its search excerpt mentions a
weighted square of the linear arithmetic residual, which is a
different observable; that excerpt is not primary theorem evidence.
The page was not retried, its proof remains unread, and no statement
from it is imported. Other nonprimary/model-written RH pages were
not used. A failed search establishes neither novelty nor absence.

Reused review231's lobe/variance/recurrence comparison and step235's
automatic-average stop. These do not ban independently paid signed
estimates. Review445 parks conditional negative-direction import;
review444 parks norm equality. L018's normalization and L984's
hypotheses/conclusion fix the actual observable. No detailed proof
of an unrelated node, cross-notebook theorem, mathematical script
or new mathematical lemma was used. Full Mathlib matching remains
unchecked and unknown.

Outcome NEGATIVE / LITERATURE / KNOWN_IMPORTED: the newly inspected
weights and singular-test case prevent the proposed direct source
import under available hypotheses. There is no claimed advance
beyond the sources, unconditional arithmetic bound or RH candidate.
Park identity-only kernel continuations. Reopening requires a
specified matching weighted-to-unweighted signed comparison and
complete compensated degree/cutoff budget, not another kernel identity.

For a different source mechanism, AppendixA cites Burnol's local
operator treatment, arXiv:math/9810169v2, 22Nov1998. That paper is an
UNREAD lead, not an imported estimate. A separate nomination asks
whether it can supply an actual lower estimate on L752's already
fixed finite neutral space. Canonical L740/L741/L744/L752 and the
L746–L750 conclusion/stop passages were consulted only to scope
that nomination, not to perform it: complete energy is already
identified; high-frequency floors and identity/localization stops
are not a finite-space sign certificate. L752's old implementation
remains parked. Its reviewed finite space is not a new unrestricted
positivity premise. No justified creative attempt is ready until
an independent signed estimate and applicability mechanism exist.
