# Nakamura–Suzuki: completed Li-input source comparison

TARGET: Source-assess arXiv:2306.08317 for an unconditional input to L984's cumulative Li lower bound, checking exact hypotheses against the recorded positivity and signed-generator stops.
CHECKED: 2026-11-11
DECISION: IMPORT
SEARCH_EVIDENCE: Step444 searched exact arXiv ID with Li and exact title, retrieved the primary PDF and HTML, and checked the author's publication list; narrowly compared review420, the screw-function screen and the causal-realization stop. No separate local assessment of this exact paper was found. No novelty inference.
SOURCE_EVIDENCE: Nakamura–Suzuki, On infinitely divisible distributions related to the Riemann hypothesis, arXiv:2306.08317v1 (wrapper14June2023, PDF internal16June2023), (1.1),(1.5)–(1.7), Theorems1.1–1.2 p2, Lemmas2.1–2.2 and complete Section2 proofs pp3–4, Appendix3 pp4–5; https://arxiv.org/pdf/2306.08317v1 . Publication metadata confirmed on Suzuki's author page: Statistics & Probability Letters201(2023),109889; published text not separately inspected.
COMPARISON: Import only the cited source-scope facts: the positive probability conclusion is RH equivalent, the explicit positive Levy measure assumes RH, and the unconditional transform retains Im(z)>1/2. The latter overlaps Suzuki's already assessed g=-Psi representation, not an independent signed Li estimate.
GAP: No inspected theorem supplies c_n>=-D_epsilon exp(epsilon n) for every epsilon>0 and all n>=2, or an independently paid signed transfer to that observable. L984(H), actual-Xi signs and forcing remain open.
REASON: Newly inspected exact hypotheses reject this nominated direct input and park it; this is informative source evidence, not a mathematical impossibility theorem. Reusing the identities or assuming the positive measure would not pay the missing bound.
LITERATURE_REASON: At invocation this exact source was unread and REVIEW_REQUIRED; its theorem-level scope was essential missing coverage. Ready Pringsheim/quartic assessments were reused rather than refreshed.
SCOPE: Completed source comparison only. IMPORT covers the quoted theorem hypotheses and overlap decision, not a new lemma, source reproof, signed specialization, transform-domain extension, or proof audit. The distinct Li norm-defect nomination requires a separate review.

## Original nomination retained; completed comparison below supersedes unread labels

The main gap is actual-Xi positivity L030–L032/C032a, with forcing
L966/L968 and the unpaid L984(H) arithmetic estimate. This nomination
focuses on a possible actual-zeta input to the existing sufficient
cumulative bound, not another model or an assertion that the paper
addresses that bound. C984a is contrast only: weak radial continuation
does not suffice under its retained properties.

The intermediate target is an inspected unconditional theorem with
an explicit quantitative conclusion that could control the negative
part of c_n=sum_(k=2)^n lambda_k. L984's required threshold is:
for every epsilon>0, some finite D_epsilon>=0 gives
c_n>=-D_epsilon*exp(epsilon*n) for all integers n>=2.
A partial independently paid input is useful even if other ranges
or signed transfers remain unresolved. No such input is known here.

First verify the paper's identity and primary theorem statements,
then read essential proof cases only where they affect applicability.
Compare its exact objects and quantifiers with review420's completed
divisibility comparison. If it uses screw functions, compare only the
relevant passages of 2026-11-01-screw-function-signed-remainder-screen.md
and the matching Suzuki causal-energy assessments; those records were
located, not substantively reviewed in this nomination. Reuse adequate
coverage rather than infer that a different paper evades an old stop.
Do not resurrect the persistent boundary/evaluator route by relabeling it.

Continue only if the inspected result identifies an independently
checkable actual-zeta input and a bounded quantitative transfer test.
Park this lead if its useful conclusion assumes RH-equivalent
positivity, lacks a cost for the signed transfer, concerns an unrelated
observable, or its essential source remains inaccessible. Record exact
scope evidence rather than an impossibility theorem. Do not turn a
formal identity into an approved mathematical attempt in the same turn.

Potential inputs for later mathematics are L984's exact ordinary-Li
normalization and cumulative germ and L018's completion; the paper's
additional inputs remain unknown. C984a and the prior stops are
comparisons, not premises. All actual arithmetic, signs, forcing and
the capped E_n bridge stay unresolved. No cross-notebook input is
proposed, and matching Mathlib coverage is unknown.

No justified creative central attempt is ready: this unread lead has
not furnished an independent sign/domain/arithmetic mechanism. If its
review justifies one, nominate a precise bounded creative test with
NEXT_ESCALATION and obtain the required separate approval. Otherwise
choose a materially different independently testable target; neither
this source nomination nor repeating the quartic renews an exhausted
mathematical mechanism's budget.

## Completed source comparison — step444, 11 November 2026

The required intermediate input was an unconditional signed estimate for
L984's ordinary-Li cumulative coefficients, with every-epsilon root rate
at most1. Its downstream use is L984's sufficient criterion; actual-Xi
positivity and the other forcing/bridge gaps remain independent. The
discriminator was an independently checkable quantitative transfer,
not merely another equivalent sign criterion. The direct-import test
fails on the inspected source's exact hypotheses.

### Primary statements and essential cases

The controlling text is [Nakamura–Suzuki, arXiv2306.08317v1](https://arxiv.org/pdf/2306.08317v1).
The [wrapper](https://arxiv.org/abs/2306.08317) lists one version,
14June2023; the PDF says16June2023. Its experimental HTML instead
says24August2026; no later theorem version is inferred from that anomaly.
[Suzuki's publication list](https://www.math.titech.ac.jp/top/~msuzuki/index.html)
identifies the journal article as *Statistics & Probability Letters*
201(2023),109889. The journal text was not independently inspected.

Equation(1.1) uses the same factor1/2 completion as L018. Equation(1.5)
defines the even real function g_zeta from all von Mangoldt prime powers,
pole terms and the archimedean correction; there is no finite verified-zero
subtraction. Theorem1.1,p2, states exactly RH iff exp(g_zeta) is the
characteristic function of an infinitely divisible probability measure
on the real line. Theorem1.2,p2, explicitly assumes RH before declaring

    nu_zeta = sum_gamma m_gamma/gamma^2 delta_(-gamma)

its positive Levy measure, with triplet(0,0,nu_zeta), giving a compound
Poisson law. Here gamma ranges over distinct zeros of xi(1/2-iz) and
m_gamma is the full multiplicity. Reality of gamma is a hypothesis in
that positive-measure use; complex gamma are not real-line atoms.

The unconditional identity(1.7) and Lemma2.1,p3, retain all complex
gamma and give compact-real-t absolute/uniform convergence of

    g_zeta(t)=sum_gamma m_gamma*(exp(-i*gamma*t)-1)/gamma^2.

Lemma2.2,(2.2),pp3–4, gives only for Im(z)>1/2

    integral_0^infinity g_zeta(t)*exp(i*z*t) dt
        = z^(-2)*(xi'/xi)(1/2-i*z).

Read the complete Section2 proof cases: the forward case invokes real
zeros and the Levy integrability conditions; the transform case uses
Hadamard factorization and the central logarithmic derivative; the
converse extracts g_zeta<=0 from the probability assumption and invokes
Widder, *The Laplace Transform*(1941), ChapterII,Theorem5b, plus
nonvanishing of xi on the positive real axis. Widder was not newly
imported or independently audited here. This is a source-scope review,
not a proof audit of every displayed termwise identity or interchange.
Appendix3,pp4–5, was read to its conclusion: its prime-series transform
retains Re(s)>1, equivalently Im(z)>1/2; it does not supply a larger
unconditional convergence domain. No source reproof or repaired
auxiliary identity is offered.

### Overlap, comparison and decision

Reused the inspected Suzuki2206.03682v4 coverage in
[the screw-function screen](2026-11-01-screw-function-signed-remainder-screen.md):
Theorem1.1's unconditional representation, g=-Psi normalization and
Theorem1.7's global sign criterion. The source itself identifies that
Suzuki representation as its input. The finite-window coercivity and
verified-zero remainder questions are not solved by Theorem1.2's
RH-conditional measure. The screen's separate inaccessible scalar-tail
lead remains parked; no access retry was made.

Review420's Nakamura1504.03438 completed-ratio and signed-generator
limits concern a different probability object. The new source does
not evade those payment requirements by proving its own probability
premise unconditionally. Review421 already parks the reciprocal-theta
reconstruction-to-Li import. The causal-realization assessment and
its realization-only sign-gap attempt were checked narrowly: domain
identification and finite-window boundedness do not provide total
zero-loss signed control. None is a premise for a new result here.

The source has no stated cumulative-Li coefficient bound matching
L984's ordinary normalization, degree1 subtraction and all-n quantifiers.
Neither compact-t convergence nor the already assessed transform domain
is such a bound. Park this direct input absent a new independent signed
estimate. This conclusion rejects an import, not all probabilistic or
screw-function research. Outcome NEGATIVE, LITERATURE, KNOWN_IMPORTED:
new source-scope evidence changes the decision, with no progress beyond
the sources' mathematics and no new local theorem.

The next distinct lead is the author's explicitly listed *Li coefficients
as norms of functions in a model space*, arXiv2301.05779. Its theorem
text remains unread. A narrow exact-ID/title search of local literature,
foundations and attempts found no matching assessment; this establishes
no novelty. Nominate only its norm-defect applicability question in
[review444](2026-11-11-suzuki-li-norm-defect-review-444.md), with
REVIEW_REQUIRED. A genuinely new central mechanism cannot yet be
approved: the existence and independently estimable signed part of that
representation are unknown. C999i was found already audited in step441;
its stale overview qualifier is no reason to repeat it. No lemma, script,
DAG or PROOF change, cross-notebook import or mathematical exploration
budget reset occurred. Full matching Mathlib coverage is not checked.
