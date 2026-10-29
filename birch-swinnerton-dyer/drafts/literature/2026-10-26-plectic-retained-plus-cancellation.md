# Retained plus component: bounded complete-integral cancellation test

TARGET: Test whether the split-multiplicative same-prime tensor D^{++} of Fornea's r=2 trivial-character class vanishes by deriving a conjugation relation for the complete invariant integral, or isolate the precise surviving arithmetic term.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 512 exact-title searches with same-prime, localization, complex conjugation and symmetric, plus notebook-local duplicate/failure checks, found no inspected theorem for the retained-component cancellation; no originality is inferred.
SOURCE_EVIDENCE: Fornea https://arxiv.org/html/2603.28327v2 (13 April 2026), Definitions 4.3/4.5/4.8/4.17/4.23, equations (54)/(55)/(63)/(68), Theorem 4.13 with proof, Proposition 4.18 with proof, Corollary 4.24 with proof, Theorem 5.3 and its complete Section 5.4 proof inspected in step 512; Fornea-Gehrmann https://arxiv.org/html/2311.03100v2 (2 December 2024), Corollary 2.9 and Section 2.2.5 checked there for projected action scope; both versioned URLs retrieved and key comparison statements reconfirmed in step 513.
COMPARISON: Theorem B determines the minus partial-Frobenius projection for split p, not the retained plus component; Theorem 5.3 controls degree-zero differences, while Theorem 4.13 has an omitted constant-coordinate hypothesis; none states the proposed same-prime cancellation.
GAP: Derive a transformation for the complete invariant integral under global conjugation and local plus projection, without a pointwise pr_A or assumed determinant/Selmer conclusion; no such identity is approved as a premise.
REASON: A concrete actual class and complete integration formula permit an independently falsifiable local test at the strict-class bottleneck; this changes mechanism from importing rationality to testing a retained arithmetic term.
SCOPE: Only the single r=2 split-multiplicative same-prime diagnostic defined below; no full plectic rationality, arbitrary-curve coverage, nonvanishing, finite Sha or Kummer membership is included.

## Approval boundary

Newly saved at the end of literature step 512. Separate literature
recovery step 513 supplies the missing direct primary-source URLs and
retains EXPLORE coverage for this exact target. No research is performed
in this recovery turn; subsequent invocation remains subject to the
supervisor's gate.
No conjugation relation, vanishing result, or scalar norm formula is
established by this assessment. This is adequate bounded-search
coverage, not a theorem certification or a novelty certification.

## Direct-source recovery (step 513)

Retrieved both versioned primary HTML sources on 2026-10-26. Reconfirmed
Fornea's Theorem B, Definition 4.17 and Theorem 5.3 statement, and
Fornea–Gehrmann's Corollary 2.9 with its proof and the opening of
Section 2.2.5. The original complete-proof inspection is reused from
step 512's source notes; this recovery does not claim a fresh complete
proof audit. Theorem B concerns the partial-Frobenius projection, and
Corollary 2.9 concerns the mock invariant. These references therefore
do not turn the retained-component diagnostic into an imported zero
identity. No target, hypothesis, source-scope comparison or mathematical
conclusion has changed. This is a process repair, not new negative
evidence or mathematical progress. Prior duplicate and failure checks,
including ATTEMPTS/058, remain applicable without repeating discovery.

## Hypotheses and exact input

Use the scope and operational formula in
`drafts/source-notes/2026-10-26-plectic-diagonal-localization-coverage.md`.
A/Q is modular, K is imaginary quadratic, p>=5 is inert in K,
cal S={p} is incoherent, and p is split multiplicative for A/Q_p.
The conductor is unramified in K, the inert part is square-free,
the residual image contains SL_2(F_p), and split-conductor exponents
are at most two. Set w=infinity, conductor one, trivial character.
Retain the full Hecke localization and diamond-invariant descent.
The trivial-character factor descends from L_1 to K, not automatically
to Q. Inputs of central relevance are L005's strict-Kummer threshold
and L122's rationality limitation; neither supplies a plectic theorem.

For the rank-two application restrict additionally to
ord_{s=1}L(A/Q,s)=2 and L(A^K/Q,1) nonzero, where A^K is the
quadratic twist. The source construction itself needs neither extra
analytic hypothesis; they identify the desired application family.
Do not assert existence of such K,p for every curve. No assertion of
algebraic rank two, Selmer dimension two or finite Sha is assumed.

Let kappa_0 be the descended class in U tensor H^1(K,V),
U=H_f^1(K_p,V), and define D^{++} exactly as in the source notes.
The two projectors act on separate factors. Fix compatible local and
global embeddings and check restriction/conjugation on cochains;
do not take a determinant, interchange factors, or assume the second
factor is in U. Apply pr_A only to the integrated invariant quantity.

## One bounded attempt and decisive evidence

Try to obtain a c-transformation for that integrated quantity and
combine it with the local plus projection to test D^{++}=0. Track
the full logarithmic kernel, coefficient action, CM sum and descent;
degree-zero differences and constant mass alone are not replacements.
The attempt may end with a specific unevaluated arithmetic residual,
provided its definition and needed vanishing are explicit and do not
merely assume Conjectures 1.9–1.10. No finite-precision zero is proof.

Continue only after a rigorous cancellation or a concrete residual
that enables an independent test. Park this mechanism if its crucial
identity reduces to conjectural determinant rationality, requires an
undefined pointwise arithmetic projection, or yields no discriminating
arithmetic condition within this attempt. Preserve partial reasoning
and the source-scope obstruction before considering a repeat.

Strictness could support a rank lower bound only after independent
nonzero rational Kummer membership and a justified multiplicative-prime
extension of L005. General rank/order equality and refined BSD remain
unresolved even if this local test succeeds. No reproof of the source
construction is planned; only the uncited transformation is in scope.
Mathlib coverage: not checked.
