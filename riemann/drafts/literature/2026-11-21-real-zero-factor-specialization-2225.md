# One real-zero factor: standard specialization nominated2225

TARGET: Construct, for an arbitrary actual zero x in (14,29/2), the decaying even inverse cosine kernel of Xi(z)/(1-z^2/x^2) using the inspected ODE and sine-transform results, and prove or refute strict positivity on u>=0 with complete origin, tail and removable-pole checks.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review2225 searched exact real-zero Fourier division, positive-definite/characteristic-function factor removal, Schwartz division and stronger preservation results; compared the nominated nonreal records, review576 and discovery1117. Queries and limits are in drafts/literature/2026-11-21-real-zero-factor-source-notes-2225.md; no exact combined theorem was located and no novelty is claimed.
SOURCE_EVIDENCE: Tuck2006 pp133-135 (1)-(4), https://doi.org/10.1017/S0004972700047511; DLMF1.13(iii) (1.13.8)-(1.13.10), https://dlmf.nist.gov/1.13.iii; Tao2009 Section3 Exercise30 and inversion(11), https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/; Csordas arXiv:1309.0055v2 Theorem4.1 (4.2), p10, https://arxiv.org/pdf/1309.0055v2. These direct sources were reopened in recovery2226; theorem/proof ranges were checked as recorded below. Original Wintner1935/Spira1971 proofs remain unread; retain source notes2225 access qualifications.
COMPARISON: Ordinary variation of parameters, actual-theta strict decrease and decreasing-amplitude sine positivity cover the general tools. The exact quotient-kernel construction, boundary compatibility, two transform integrations, decay and complex extension still require one local specialization; no general-method reproof or claim beyond the inspected sources is justified.
GAP: Establish the full inverse-kernel identity and pointwise sign under only the actual selected-root hypothesis, or identify the exact failed origin/tail condition. Residual monotonicity, repeated removal and any all-degree mixed-positivity bridge are outside this target and remain open.
REASON: A bounded known-method mathematical application is justified; no quotient formula or new sign theorem was derived during source review. This newly written continuation requires separate approval before research invocation. A successful specialization is REPRODUCTION, not a creative advance or RH proof.
SCOPE: One actual root with possible multiplicity; Xi(x)=0,14<x<29/2; no first-zero assertion, simplicity, zero census, Laguerre-Polya premise or iteration closure. One complete analytic construction/sign test only; no parameter sweep, finite-head enlargement or numerical positivity surrogate.

## Mathematical purpose and full obligations

The main gap is L030-L032/C032a actual-Xi all-degree mixed positivity.
A nonnegative inverse kernel after one removal could supply an actual
shape input for later preservation tests. Positivity alone would leave
independent degree-uniform and iteration gaps; the original positive
theta kernel itself already fails to settle RH.

Use L018/L019/L024/L058 and accepted C919f. In particular C919f supplies
only existence of an unspecified real root in the bracket at lambda=0,
under its CPython/Fraction/Decimal/libmpdec HALF_EVEN exp contracts.
No certificate replay is needed for this source-covered application;
retain those qualifications if existence is used. Removing one factor
at each of +/-x is allowed even at a multiple zero. Remaining zeros,
real or nonreal, are unrestricted. No cross-notebook input.

Import the known theta monotonicity theorem by its exact source
statement and cite it in the eventual canonical lemma; do not spend
the turn reproving that classical result. The source normalization is
K(u)=4 Phi(u/2). Import the standard sine-transform result and variation
of parameters, deriving only their combined actual-kernel application.
The representation and sign are targets, not established premises.

The application must select the decaying solution and control any
homogeneous ambiguity; justify differentiating the relevant convergent
integrals; check the origin condition from the actual zero rather than
imposing it independently; justify smooth even extension and both
transform integrations with every endpoint term. Establish an exact
identity on real frequencies and its permitted extension to complex
z, including removable poles at +/-x. All required weighted integrals
and tails must be controlled, not inferred from a numerical plot.
If uniqueness or smoothness is asserted, supply the appropriate source
hypotheses and applicability reasoning. Do not assume strict decrease
or positivity of the new residual in order to prove its sign.

Continue if the exact quotient identity and a complete pointwise
positivity proof survive. If a nonzero boundary term, nondecaying mode
or uncontrolled signed tail remains, record the specific obstruction
and stop this one test. Do not repair it by presupposing the desired
sign or iterability. Full matching Mathlib coverage is unchecked;
state that honestly in a later canonical lemma.

## Routing qualification

This is established-route analytic development, classified REPRODUCTION
if completed. No justified creative central mechanism is ready: the
sources provide no preservation law for subsequent removals or bridge
to all-degree positivity. Those would require materially new input and
a separately assessed target. Approval of this nomination is deferred;
no lemma or mathematical script was written in literature step2225.

## Separate source approval2226 (2026-11-21)

LITERATURE_REASON: The supervisor reports missing direct source URLs in
the ready assessment. This is a bounded citation repair and separate
approval of the unchanged target, not another discovery search.

Direct publisher PDF for Tuck:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D232B9DEB4819E4D2FF17E8162B8B066/S0004972700047511a.pdf/on_positivity_of_fourier_transforms.pdf
Reopened pp133–135, including the convergence assumptions and the
positive/negative half-period proof on p134. Its parsed display (4)
remains incomplete; the complete parallel argument in Csordas Remark3.11,
p9, was reopened. The contemplated bounded, integrable, strictly
decreasing amplitude is within this classical tool's scope; verifying
its use in the quotient remains mathematical work.

Reopened Csordas v2 p10, (4.2) and all five parts of Theorem4.1:
positivity, strip analyticity, evenness, derivative decay and strict
decrease. Attribution is precise: parts (i)–(iv) to Polya, part (v) to
Wintner, with Spira also cited. Thus the whole package should not be
attributed solely to Wintner. This uses the inspected complete classical
restatement; it does not claim inspection of the original proofs.

Reopened DLMF1.13(iii), (1.13.8)–(1.13.10), including analytic forcing
and coefficients and homogeneous ambiguity. Reopened Tao Section3,
Exercise30 in full and Remark31: L1 function and derivative, with the
fundamental-theorem/absolute-continuity hypothesis. Inversion(11) remains
covered by the existing inspected source record2225 and is not a new
claim of this repair. No boundary condition at infinity or quotient
positivity is supplied by these general identities.

DECISION remains SPECIALIZE. The existing exact target is approved for
one subsequent REPRODUCTION attempt; no new target or expanded scope is
introduced. Existing nonduplicate and failure comparisons in source
notes2225 are reused unchanged. No new mathematics, lemma or mathematical
script was written. This repairs the reported source-link issue without
claiming mathematical progress, novelty or independent proof certification.
