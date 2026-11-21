# Actual-H spatial cofactor test: source coverage

TARGET: Test whether one retained real zero can dominate the cofactor-weighted tail in the actual reciprocal-density Volterra first-contact forcing at arbitrary fixed order m, beyond the cited finite PF range, without assuming complete monotonicity or higher-order PF signs.
CHECKED: 2026-11-14
DECISION: EXPLORE
SEARCH_EVIDENCE: Comparison884 completed exact Volterra/determinant/PF/self-decomposable/cofactor searches and the local L874/L611/U12 duplicate screen in assessment883. No inspected theorem supplies this signed forcing bound; no novelty claim. Low-order actual-density positivity is already covered by Sra v3.
SOURCE_EVIDENCE: Direct primary text https://hub.valency.io/works/W_pr5z5huy_v1 (Lemma2.2, Proposition2.3, Lemma2.4/AppendixB); author v3 https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf ; official differentiation https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ContDiff/Convolution.html ; assessment883 records inspected Steutel--van Harn V.2.11/V.2.16 equation(2.23), singular-kernel case III.10.4; Sra Hub v1 Lemma2.2/full proof, Proposition2.3 and AppendixB endpoint/regularity proof; author v3 Theorems1.2/3.4/C.9 and SectionC.8; official Mathlib compact-support convolution derivative statements. Reuse882/C466a for boundary initialization and Wronskian transfers, and the November6 heat-contact assessment for determinant/contact cautions.
COMPARISON: Known tools cover the scalar Volterra law, smooth-factor differentiation and determinant algebra, not a cofactor-weighted actual-H tail inequality. Sra's finite-factor signed smoothing requires a factor budget growing with m; its global finite PF result must not be reproduced as a new sign. This test seeks a distinct spatial forcing mechanism, not another scalar monotonicity proof.
GAP: The exact contact forcing, its retained-zero contribution and a relative signed-tail estimate are unproved. Generic positivity of H does not sign a cofactor integral. No global continuation, multiple-contact barrier, all-order PF conclusion or L030 transfer is established.
REASON: C466a gives independent boundary data, and the inspected retained-zero source mechanism offers a concrete sign-payment test outside finite-factor smoothing and the parked logarithmic heat flux. One symbolic forcing calculation can expose a paid inequality or an informative obstruction; the bounded test is not yet performed.
SCOPE: One arbitrary-order symbolic contact reduction and one retained-zero domination test, with actual H and the cited low-zero/counting inputs. Do not expand a matrix of order k*+1, recertify known finite PF orders, invert transforms numerically, or derive an increasing-order saddle estimate. Source-link recovery885 reviews and approves this unchanged bounded scope for a later research invocation; no calculation is performed in the recovery turn.

## Inputs, observable and bounded purpose

Use C466a's actual theta_1, h, B and Theta=theta_1/c_0, with
L018/L024 conventions. The destination remains L030-L032/C032a.
Their global all-degree algebraic-square sign is not an input.
Let

    D_j(p;x)=(-1)^(j(j-1)/2) det[p^(a+b)(x)]_(0<=a,b<j).

For a fixed symbolic integer m, C466a initializes all D_j,1<=j<=m,
on a possibly m-dependent boundary interval. Seek a hypothetical
first loss at x_*>0 with D_m(p;x_*)=0 and D_j(p;x_*)>0 for j<m,
and D_m positive immediately to the left. This is a conditional test;
it does not assert a contact exists. Simultaneous lower-order losses
are excluded from this test and remain a separate gap.

The test must be meaningful for arbitrary m above k*=1810540931075,
the global finite PF range stated in Sra's author v3 Theorem1.2.
This is a symbolic index restriction, not a request to construct or
numerically certify a matrix of that size. No claim of a new PF3
conclusion, nor any optimization of that finite bound, is proposed.

Use the source equation x p=H*p and Jacobi's cofactor formula to
identify the exact signed contact forcing, including normalization
and all endpoint terms. This line describes the calculation to do;
no differentiated recurrence or forcing identity is claimed here.
The singular H must remain under an integrable convolution with a
localized smooth density factor. Check the cutoff and derivative
domination explicitly. C466a's cited zero extension is smooth; the
official Mathlib hypotheses and source citations are in assessment883.

The proposed new ingredient is to keep the complete conjugate-pair
tail inside that signed forcing and compare its possibly negative
contribution with one retained real-zero contribution. For the
available scalar comparison, use Sra Hub v1 Lemma2.2 at U=100,
q=gamma_1^2 in(196,225), K_U=e^(-qt)+H_>U and
epsilon_U=U^4e^(-U); that lemma bounds K_U and -K_U' below by
(1-epsilon_U) times the corresponding retained term for all t>0.
Its full proof was inspected in884. It does not contain a bound for
the new cofactor weight; finding whether that extension can hold is
the entire mathematical test. Preserve the counting, strip and
finite-zero hypotheses recorded in C466a; no tail zeros are assumed
real and no complete monotonicity of H is available.

## Continue or abandon

Continue only if the exact forcing yields a strictly inward contact
sign D_m'(x_*)>0, or an independently proved local barrier that
excludes a crossing, using paid actual-H estimates. A merely
nonnegative derivative at one point cannot exclude a tangential
crossing. A useful reduction may instead identify one concrete unpaid
weighted-tail inequality and its actual required threshold; retain it
without claiming preservation.

Abandon this retained-zero domination mechanism if the calculation
requires an uncontrolled cofactor-weight ratio, complete monotonicity,
already-global PF signs, or a degree-growing verified-zero supply
that simply reinstates the cited finite-factor budget. Report an
obstruction only within the hypotheses actually tested. A substituted
kernel or free-jet model is not an actual-Xi counterexample. Do not
repeat formal contact manipulation after a stop without a new input.

If this test succeeds, a separately justified treatment of other
contacts and compact-interval continuation could extend each fixed
boundary order. Iterating over orders and the Schoenberg/RH interface
would still need a complete assembly. Order-uniform boundary data
are not assumed. This is a plausible downstream use, not a proof.

L874's heat/logarithmic-moment missing coefficient, L611's double-zero
Fourier sign and the fixed-U12 stops are preserved as contrasts.
Reuse the contact warning in
`2026-11-06-reciprocal-hankel-heat-contact.md`, including its inspected
Nagumo-hypothesis comparison; no closed autonomous matrix flow or
maximum principle is an input. Full matching Mathlib Volterra/PF
coverage is unchecked; the inspected convolution theorems are support
only. No cross-notebook mathematical input is used.

Recommended mathematical routing after approval: proof_attempt/creative,
deep_research/max. The precise obstruction is the unbounded-order
cofactor-weighted tail sign left unpaid by scalar H monotonicity and
finite-factor PF smoothing. The decisive bounded evidence is an exact
forcing plus a strict/barrier inequality, or a demonstrated failure of
that proposed domination under the actual retained-zero estimates.


## Source-link recovery885 (14 November 2026)

This is a traceability repair and separate literature approval of the
unchanged TARGET, not new mathematical evidence or a second discovery
search. Reuse assessment883's exact-statement searches, duplicate screen
and inspected source hypotheses. LITERATURE_REASON: the supervisor
requires direct source URLs in the ready assessment; the target and
assumptions have not changed.

Primary locators, with access distinguished from inherited inspection:

- Sra, *On some positivity properties of the Riemann Xi function*,
  [Hub v1, 29 October 2026](https://hub.valency.io/works/W_pr5z5huy_v1):
  Lemma 2.2 and its proof for retained-zero bounds; Proposition 2.3 and
  its proof for the Bernstein representation and integrability; Lemma 2.4
  and Appendix B for smooth zero extension. The Hub text was accessible
  in885; the full proofs were inspected in884/882 and are reused.
  The scalar estimates have no signed cofactor-weight hypothesis or
  conclusion. They do not themselves pay the proposed weighted bound.
- Steutel--van Harn (2004), Chapter V Theorems 2.11/2.16,
  equation (2.23), and Chapter III Theorem 10.4:
  [book PDF](https://www.nzdr.ru/data/media/biblio/kolxoz/M/MV/Steutel%20F.%2C%20van%20Harn%20K.%20Infinite%20divisibility%20of%20probability%20distributions%20on%20real%20line%20%28Dekker%2C%202004%29%28ISBN%200824707249%29%28546s%29_MV_.pdf).
  Reuse883's inspection of the positive self-decomposable law with left
  endpoint zero, its canonical density k=H and the singular-kernel case.
  The PDF timed out through the web tool in885; no fresh book inspection
  is claimed. This does not erase the prior inspected evidence.
- Sra, [author v3, 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
  Theorem 1.2 pp2-3, Theorem 3.4 p10, Theorem C.9 pp27-28,
  Section C.8 p29, Proposition A.1 pp16-17: reuse883's inspected
  finite-factor assumptions and overlap comparison. This PDF was
  inaccessible through the web tool in885. Its stated finite range is
  retained as source overlap, not an independently audited import and
  not an arbitrary-order preservation theorem. Do not substitute Hub v1
  theorem numbering for this version.
- [Official Mathlib convolution documentation](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/ContDiff/Convolution.html#HasCompactSupport.hasDerivAt_convolution_right):
  hasDerivAt_convolution_right and contDiff_convolution_right.
  Statements inspected in885 retain local integrability, a compactly
  supported smooth factor, and invariant measure hypotheses. The
  previously inspected source revision is
  [26573066084e6e2aa8526ea358bc43b66d96f970](https://github.com/leanprover-community/mathlib4/blob/26573066084e6e2aa8526ea358bc43b66d96f970/Mathlib/Analysis/Calculus/ContDiff/Convolution.lean).
  These are supporting differentiation results only; localization,
  endpoint terms and the contact inequality must still be proved.

Decision remains EXPLORE. The prior coverage suffices for one later
symbolic forcing and retained-zero domination attempt under the stated
scope. No new theorem is approved as true. No essential new source is
awaited for that attempt, and no further literature turn is nominated.
Preserve C466a normalization and external zero/counting hypotheses,
L874/L611/U12 stops, simultaneous-contact and continuation gaps.
