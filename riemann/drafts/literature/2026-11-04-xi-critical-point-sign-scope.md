# Actual-Xi critical-point sign: completed source comparison

TARGET: Assess primary-source coverage for a theta-specific proof of -Xi(t)Xi''(t)>=0 at every real t with Xi'(t)=0 and Xi(t)!=0, testing whether the critical-point constraint yields a sign mechanism beyond kernel positivity and log-concavity.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the exact-extrema, constrained Fourier/Laguerre and kernel-shape comparisons below; checked L049/L050/L607 as additional local obstruction evidence. No matching unconditional all-height critical-point theorem or independent theta residual estimate was located in this bounded search; no novelty or nonexistence claim follows.
SOURCE_EVIDENCE: Read Kobayashi revised 29 March 2016 author PDF, Theorem 1.1/(14)-(18) and approximation-dependent Theorem 2.1 passages; Bombieri official description, printed p.113; Csordas arXiv:1309.0055v2, Definition 1.2, Propositions 2.2-2.3, Theorems 3.5/3.7 with proof cases, Example 3.12 and Open Problem 4.7; Sra author v3 (2 November 2026), Theorem 1.3, Lemmas 4.1-4.2 and complete relevant proof, pp.3/10-12. Precise links and qualifications below.
COMPARISON: Kobayashi's matching critical-value formula assumes RH; the inspected Sra v3 retains the bounded-height premise already covered locally. Associated-kernel admissibility still does not give a Fourier sign. Bombieri's strict-extrema assertion is not a supplied proof or an equivalence for the saved weak stationary inequality.
GAP: No independently controlled theta-specific signed residual using Xi'(t)=0 was obtained from the inspected sources. The actual-Xi inequality, degenerate cases and its relation to stronger sign criteria remain unresolved.
REASON: Park citation-only and shape-only implementations of the actual-Xi target. Prepare one separately assessed finite-interval countertest of the generic constrained inference; do not derive a theta identity or a new sign theorem in this literature turn.
SCOPE: The actual entire Xi of L018, real t, Xi'(t)=0, Xi(t)!=0, and the exact theta kernel of L019/L020. No RH, simplicity, all-real critical points, positivity of an associated kernel, or missing sign is assumed.
LITERATURE_REASON: The critical-point constraint and theta-specific sign mechanism lie outside the ready short-Dirichlet-polynomial moment scope; essential exact-target and stronger-result coverage is missing.

## Purpose and bounded test

The main gap is actual-Xi all-degree mixed positivity. The proposed
intermediate input controls the first Laguerre sign only where Xi has
a nonzero real critical value. It could constrain adverse local extrema
and provide actual-function signed information for a later local-margin
argument. Transfer to other centers and all higher/mixed signs would
remain unpaid; even global first-sign positivity alone is insufficient,
as the masking example L251 records.

The candidate mechanism is to use the exact critical-point constraint
inside the theta cosine-transform calculation, retaining every
oscillatory residual and boundary term, instead of requesting a global
autocorrelation factorization or another small exterior-tail estimate.
No such identity has been obtained. This is a discovery question, not
an approved proof_attempt/creative. The blocker to that routing is the
absence of both primary-source coverage and a specific independently
controlled residual; a mere restatement of the desired sign is not a
mechanism.

Use at most three primary source chains: first actual-Xi real extrema
and critical values; second constrained Laguerre/Turan inequalities for
Fourier transforms; third, only if necessary, exact theta identities
that address the resulting signed term. Check whether a stronger known
theorem already supplies the claim, and inspect its actual hypotheses
and relevant proof cases before nominating a calculation. Search and
compare the exact claim and standard terminology without presuming
novelty or treating an RH-conditional statement as unconditional.

Continue only by (i) importing a matching unconditional theorem with
precise scope, or (ii) recording an explicit theta-specific identity
and a bounded residual inequality whose success or failure would decide
one named intermediate input. If the sources supply only kernel
positivity/log-concavity, count/gap data, or a conclusion assumed as a
premise, park that implementation. A hypothetical countermodel must
match its stated generic hypotheses and would refute only that generic
inference, not the actual-Xi claim or RH. An inconclusive search is
EXPLORATION; it does not refresh an exhausted calculation budget.

## Existing evidence to preserve and reuse

The following are comparisons in mathematical prose, not new premises
for the proposed inequality. L047/L048 establish recorded actual-kernel
log-concavity; the older positive-kernel inference fails in
ATTEMPTS/2026-09-09-positive-theta-kernel-inference.md. L251 warns
against identifying first-sign positivity with RH. L354's count/gap
counterexample prevents substituting aggregate zero information for a
signed estimate. L727's local product and
ATTEMPTS/2026-11-03-l727-tail-only-signing-stop.md leave the actual
polynomial margin unpaid; the new question must not repeat that tail.

Reuse the relevant source evidence in
drafts/literature/2026-10-25-initial-laguerre-sign-coverage.md and
drafts/literature/2026-10-31-theta-heat-autocorrelation-scope.md. The
latter is a different full associated-kernel decomposition question;
its EXPLORE decision is not automatically coverage of this constraint.
The essential defining inputs for a later attempt would be L018,
L019 and L020, with any additional theorem justified separately.
No zero-free region, reciprocal continuation or parked arithmetic
estimate is being reopened. No cross-notebook input is proposed.

Full matching Mathlib coverage is unchecked. No new lemma, proof,
mathematical script or ready continuation was produced by this nomination.

## Completed review — step 262, 4 November 2026

The preceding purpose and stopping test are retained from the entry
nomination. This section completes its source review. The main gap is
still actual-Xi all-degree mixed positivity. The reviewed intermediate
target is the weak first sign at *every* nonzero real critical value;
an adverse-extremum exclusion could inform local signed margins, while
other centers, degeneracies and higher signs would still require work.

### Primary-source comparison

Hisashi Kobayashi, [*Local Extrema of the Xi(t) Function and the Riemann
Hypothesis*, revised 29 March 2016](https://hp.hisashikobayashi.com/wp-content/uploads/2016/04/Riemann-Hypothesis-No-6-Revised-March-29.pdf),
Theorem 1.1 and (14)-(18), printed pp.2-3: the real-zero product and
negative curvature ratio at critical points are derived **under RH**.
This is no unconditional sign import. Theorem 2.1, pp.9-10, is an
asymptotic converse claim, not a proof of the requested sign; its
discussion uses (11)'s approximation and the asserted displacement
(37). No uniform remainder audit or converse import was performed.

Enrico Bombieri, [*The Riemann Hypothesis*, official description,
in *The Millennium Prize Problems* (2006)](https://www.claymath.org/library/monographs/MPPc.pdf),
Section 3, printed p.113 (PDF page 106), asserts the strict local-extrema
equivalence without a proof there. It supplies no mechanism for proving
the signs. The saved weak inequality allows zero curvature and excludes
zero critical values; no equivalence between these formulations is
asserted or used. A generic converse would in any event conflict with
L251's documented scope. This comparison does not adjudicate the
actual-Xi equivalence assertion.

George Csordas, [*Fourier transforms of positive definite kernels and
the Riemann xi-function*, arXiv:1309.0055v2, 21 February 2014](https://arxiv.org/pdf/1309.0055v2),
Definition 1.2, pp.2-3, specifies positivity, smoothness, evenness,
strict decrease and super-Gaussian derivative decay. Propositions
2.2-2.3 require zero exclusion or a controlled remaining factor.
Theorems 3.5/3.7, pp.6-8, give admissibility and a sign interface, not
the desired sign; both intervals in 3.5's proof and the coefficient
argument were inspected. Example 3.12, p.9, has Gaussian decay and a
positive first sign despite nonreal zeros. It is not the proposed
admissible critical-minimum obstruction. Open Problem 4.7, p.12, is
historical context, not proof of present nonexistence. Reuse the
recorded Proposition 3.10 corrections and half-wave failure screen in
[the cumulative-defect review](2026-10-31-associated-theta-cumulative-upper-defect-review.md);
that criterion supplies no independent constrained upper bound.

Suvrit Sra, [*On some positivity properties of the Riemann Xi function*,
author v3, 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Theorem 1.3, p.3, still assumes RH through height T>1/2 and concludes
all-order nonnegativity only for |x|<=T-1/2, strictly unless the central
zero multiplicity exceeds the index. Read Lemmas 4.1-4.2 and the proof,
pp.10-12: real factors, conjugate pairs, Gaussian prefactor, compact
product limits and central multiplicities are all retained. This does
not remove the height restriction by imposing Xi'(x)=0. The latest
version therefore does not change L466's applicable scope. Its other
reciprocal-law/PF results were not audited or imported.

### Search record and limits

Three source chains: real extrema (Kobayashi/Bombieri); constrained
Laguerre/Fourier signs (Csordas/Sra); generic kernel-shape obstructions
and standard transform inputs for a bounded countertest. Queries used:

- `Riemann Xi function extrema stationary points positive maxima negative minima theorem`;
- `Riemann Xi critical points Laguerre inequality Csordas local extrema`;
- `Riemann Xi "critical points" "inequality" theta`;
- `Fourier transform "stationary points" "Laguerre" kernel`;
- `"Fourier" "critical points" "log-concave" Laguerre`;
- `"Riemann" "stationary" "kernel" "constraint"`;
- `"Fourier" "log-concave" "local minimum" kernel`;
- `"admissible kernel" "local minimum"`;
- `"logarithmically concave" "kernel" "Laguerre" counterexample Gaussian`.

Search snippets and unreviewed RH-proof claims were discovery leads
only. An initial standalone Clay URL failed; the official collected
volume succeeded. No essential source blocker remains for this screen.
The supplemental Schubr lead and Gaussian input are qualified in the
separate continuation assessment, not imported as actual-Xi results.

Local duplicate checks newly included L049/L050: their nonreal zeros
do not themselves certify an adverse real critical value. L607 proves
a negative first sign at a specified center, without a stationary-point
claim; L560 uses a reciprocal density, a different object. None is
silently strengthened. L047/L048, L251, L354 and the original tail-only
stop retain their recorded qualifications.

Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. This is a new
bounded comparison with a concrete continuation, not a new theorem
or evidence against RH. Park the actual-theta signing implementation
until an independent residual mechanism exists. No justified creative
attempt at that central gap is ready; its blocker is mathematical,
not a need to repeat this search. The separate
[modulated-kernel test](2026-11-04-critical-point-modulated-kernel-test.md)
requires next-turn approval before execution. No proof, lemma,
mathematical script, assembly or DAG was changed.
