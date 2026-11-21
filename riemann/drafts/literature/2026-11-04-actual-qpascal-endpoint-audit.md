# Actual q-Pascal endpoint obstruction — proposed critical audit

TARGET: Critically audit L765's actual-coefficient endpoint limit and full error-norm obstruction on k=1024r, including finite-value remainder amplification and exact diagonal normalization.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the unchanged source/overlap search in drafts/literature/2026-11-04-actual-toeplitz-qpascal-endpoint.md and step385's three-mechanism discovery; the audit introduces no new coefficient sequence, parameter regime, model or proposed sign theorem.
SOURCE_EVIDENCE: Direct primary URLs https://arxiv.org/html/2007.13582v2#S1 (definition(1.2), Theorem1.4/(1.8), K=2) and https://arxiv.org/html/2607.16795v1#S4 plus https://arxiv.org/html/2607.16795v1#S5 and https://arxiv.org/html/2607.16795v1#S6 (Lemma4.1/proof, (6), Lemma6.1/proof, normalization/factorization); retrieved and inspected again on 2026-11-04 for this approval.
COMPARISON: The source already gives the comparison and warns of its tail limitation; L765 supplies a quantitative actual-entry specialization. The continuation checks that specialization and its qualifications, without reproving the saddle theorem or claiming new positivity.
GAP: Independent critical review of L765's centering signs, factorial normalization, amplified integer errors, uniform limit, rational lower bound and exact F_00 remains undone; the entire manuscript and its certificates are outside scope.
REASON: Step387 supplies the missing direct source URLs and approves the unchanged audit scope after primary-interface review; L765 remains unaudited. This literature-only approval authorizes the separate mathematical audit next turn.
SCOPE: Exactly L765 on integer k=1024r, r->infinity, with the original F and actual a_n; no other rays, redesigned comparisons, minor signs or new mechanism.

Reuse primary theorem hypotheses and the precise references in the endpoint
assessment and L765. The K=2 asymptotic is a finite-value statement at
positive integers; no derivative of its error is available. Audit that
its O(log(n)^2/n^2) logarithmic remainder survives O(r^2) amplification
after division by r. Differentiate only the explicitly displayed G.

Check the gamma_n/(8*4^n*n!) normalization, the two directions of the
rho diagonal congruence, cancellation of A and c_d, and triangular first
row extraction. Confirm eventual 0<q<1 before whitening. The audit must
check the full analytic proof of the endpoint limit, not decimal samples.

Accept only if the claimed positive constant and resulting norm divergence
follow; repair a concrete error if possible and report any failed bound.
A passing audit stops only the unmodified sufficient criterion on this ray.
It provides no effective finite threshold and no minor or RH sign result.
Inputs are L018/L021 and the two cited primary theorem interfaces; L763
is merely a normalization contrast, not a mathematical dependency.
Mathlib matching coverage remains unchecked.

## Source approval — step387

LITERATURE_REASON: Supervisor recovery identified missing direct source URLs;
this review repairs provenance for the saved audit, without expanding its target.

Inspected [O'Sullivan v2](https://arxiv.org/html/2007.13582v2#S1),
(1.2), Theorem1.4 and (1.8): fixed-order integer coefficient asymptotics,
with an error constant depending only on K. At K=2 the relative remainder
is O(log(n)^2/n^2). No differentiated remainder or effective onset is
provided by this interface; both remain excluded from the audit's premises.

Inspected [Michałowski v1](https://arxiv.org/html/2607.16795v1),
(2), Lemma4.1 and its full Newton-elimination proof, (6), Lemma6.1 and
its full homotopy proof, Section6 assembly, and Remark8.2. The finite
factorization assumes r>=2 and 0<q<1. The inertia criterion assumes an
invertible S, a signature J, a symmetric perturbation and whitened norm<1.
Section6 displays the cancellation used by L765. Its rho normalization
prose must still be checked independently in the audit. The tail theorem
and Taylor-series estimates are not imported outside their stated regime.

Reuse the existing endpoint overlap assessment and recorded
[route stop](../../ATTEMPTS/2026-11-04-actual-qpascal-endpoint-norm-stop.md);
no duplicate calculation is warranted. No new mathematics, lemma edits or
certificate checks were performed. Mathlib matching coverage remains unchecked.
The exact audit target is ready as SPECIALIZE; this approval does not certify
L765 or change its mathematical stop evidence.
