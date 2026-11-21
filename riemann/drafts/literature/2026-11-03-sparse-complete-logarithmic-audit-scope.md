# Source scope for the sparse complete-mean audit

TARGET: Audit L692's complete logarithmic-mean and angular zero-charge bounds for at most 2*floor(n/40000) independent shifts, checking moment normalization, annihilation degree, uniform baseline error, coefficient costs and straight-path quantifiers.
CHECKED: 2026-11-03
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 97's ready independent-shift homotopy discovery assessment; searched the exact local L657/L666/L686/L690-L692 source and failure references. Targeted inspection of the cited publisher excerpt located the matching standard coefficient estimate in Lemma 1.6; no redundant general discovery search was needed.
SOURCE_EVIDENCE: Brunault--Zudilin, Many Variations of Mahler Measures, ISBN 9781108794459, publisher excerpt, Proposition 1.4 and its three complex-analytic proof cases p.6, Proposition 1.5 p.7, Lemma 1.6 and full proof p.8, inspected 2026-11-03. Reused step 97's inspected integrability coverage and L657's exact finite charge identities; L690 (1)-(2) remains the audited local baseline.
COMPARISON: L692 (13)'s coefficient-to-Mahler inequality is covered by Lemma 1.6, not new mathematics. The normalized finite annihilator, baseline error, support fraction, onset and complete-charge specialization are family-specific claims still requiring audit. L686's norm result and L691's two-half bound do not imply them.
GAP: Verify those finite applicability and arithmetic steps, including actual degree and exceptional slices; no essential source is blocked. Full-cube control, H/support, actual-Xi realization and signs remain unresolved.
REASON: Separate source-only approval completes the saved REVIEW_REQUIRED gate. SPECIALIZE authorizes exactly the saved audit, not acceptance of L692 or a new mechanism. The new precise coefficient citation changes the source comparison and should replace an unnecessary general reproof during the audit.
LITERATURE_REASON: The invocation-start scope required separate approval for the newly proposed L692 audit; this turn resolves that exact gate and identifies a directly matching coefficient theorem, reusing adequate earlier discovery.
SCOPE: L692's n=12q+3, n>=10^6, M=n/3, original unit residues, fixed anchor x=-5/4, R=11/8, one independent displacement vector |e_m|<=1/8 at every angle, at most 2L changed indices with 1<=L<=n/40000, and its full straight path. Preserve all spatial moments, j=0 factor, denominator angle 1/u and complete L657 charges. No source-manuscript audit or full-cube extension is approved.

## Primary input and applicability

F. Brunault and W. Zudilin, *Many Variations of Mahler Measures*,
[publisher excerpt, printed pp.6–8](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
retrieved 3 November 2026. Proposition 1.4 includes every complex root;
its boundary case uses an indentation error tending to zero. Proposition
1.5 is the nonzero complex-polynomial root-mean formula, retaining the
actual leading coefficient and multiplicities. Lemma 1.6 states
|a_k|<=binom(d,k) M(P) for a complex polynomial of degree d and
0<=k<=d. Its full proof uses Viete's expansion and the root product.
No integrality, root simplicity or circle-zero exclusion is required.
These are imported known results; their general proofs need no reproof.

The later audit must apply the coefficient theorem at the actual spatial
degree, handle coefficients above that degree as zero, and justify the
replacement by the nominal M-1 binomial bound. Constant nonzero slices
must remain included. This is a finite specialization, not a theorem
on continuity uniform in growing degree.

Reuse [step 97's assessment](2026-11-03-independent-shift-mahler-homotopy.md)
for its inspected Issa--Lalin arXiv:1203.5379v1 Remark 3.8/Theorem 4.1,
printed p.7, s=1, logarithmic-integrability input. This source was not
freshly retrieved here. L657 supplies the specialized nonzero slices,
absolute product-log integrability, complete K/Q identity and m_0 bounds;
the later audit must check L666 meets those finite hypotheses. L690
(1)-(2) supplies the uniform undisplaced error. No annular limiting
argument, singular-log differentiation or root-motion theorem is needed
by the displayed L692 proof.

## Exact pending audit and decision test

Check L692's p in the normalized coordinate a/R; the functional is
sum p_k*c_k, with no implicit coefficient conjugation. Check padding
with unchanged indices and repeated factors, exact old/new cancellation,
available degree 4L<=(M-1)/2, coefficient extraction from the full
uniform L690 error, and every separation/factorial/binomial cost.
Check both n>=10^6 and the restricted sequence n=12q+3.

For integration, retain torus zeros, all denominator factors and canceled
numerator factors, actual angular degrees, multiplicities and the finite
center-zero exceptional spatial slices. Check that the same constants
hold for every t in [0,1], rather than inferring a path bound by
logarithmic differentiation. Replay all thirteen exact records in
`scripts/one-sided-hankel/sparse-complete-logarithmic-101.json` during
the research audit only; no replay was performed in this literature turn.

Accept only if these checks validate the stated sparse-support complete
mean and charge bounds. On failure preserve the derivation and identify,
repair or withdraw the precise affected claim. No full-cube or RH
conclusion is within the acceptance test.

## Duplicate and failure comparison

Read L692's full argument and remaining-obstruction section for scope,
L690's exact (1)-(2), L657's hypotheses and complete-charge statements,
and L666's exact census. L686's sparse norm claim uses a different
observation quantity. Its single-anchor stop is recorded in
`ATTEMPTS/2026-11-03-exact-spatial-single-anchor-limit.md`: the displayed
full-support lower certificate becomes negative, not an upper bound on
the response. L691 controls two moved halves via a different analytic
mechanism. Neither is used as a theorem premise in L692.

L692's own full-support annihilator degree obstruction and remaining
coefficient costs remain recorded limitations. This audit cannot remove
them. A validated sparse bound could support L690's base/L661's diagonal
comparison on that subfamily; arbitrary support, realization and Xi
positivity remain independent gaps.

Mathlib: reuse L692's supporting univariate root-mean names. Full
matching coverage for the family-specific theorem is unchecked; this
turn makes no absence claim or formalization claim. No lemma, script,
DAG or proof-overview change was made, and no mathematical result was
derived or audited in this source-review step.
