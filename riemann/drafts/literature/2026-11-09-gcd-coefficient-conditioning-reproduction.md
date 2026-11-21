# Finite coefficient-conditioning reproduction

TARGET: Reproduce the source-covered bound Q(c)>=a_epsilon N^(-epsilon)||c||_2^2 for every epsilon>0, uniformly for integers N>=2 and complex c, using L737's finite inversion and a weighted Schur estimate with explicit exponent allocation.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed step235 comparison in drafts/literature/2026-11-09-gcd-coefficient-conditioning-review.md; exact endpoint overlap is recorded there, with primary comparisons and no novelty claim.
SOURCE_EVIDENCE: Direct sources reaccessed 2026-11-09: https://rstation.ai/problems/riemann_hypothesis/papers/41/v3 Section5 Lemma5(27); https://terrytao.wordpress.com/2008/09/23/the-divisor-bound/ (3); https://denisevellachemla.eu/Rosser-Schoenfeld-1962.pdf Theorem15(3.41)-(3.42), pp71-72; https://grafakos.missouri.edu/preprints/multilinear_schur.pdf Section2 classical Schur theorem p2; reuse step235 proof-case assessment and L737 finite(5)-(11).
COMPARISON: This is reproduction of a source-covered finite estimate; the compressed immediate manuscript proof warrants a canonical verification from precisely cited standard inputs. No general theorem needs reproving.
GAP: Canonical verification must retain complex vectors, the squared operator norm, positive weights, cutoff1 and constants depending only on epsilon; no analytic length or positivity assertion follows automatically.
REASON: Conditioning is a concrete remaining obstacle after L925, with all essential sources now available. Write only the finite proof after separate supervisor approval, and classify it REPRODUCTION.
SCOPE: Exact TARGET only; integer natural-prefix indices, unchanged Q normalization, every fixed epsilon>0, no epsilon=0 or shifted parameter claim, no new moment theorem or observer application.

Essential local input is L737's finite factorization and inversion.
L925 is downstream context, not a premise of the inverse estimate.
No RH, simplicity, nonvanishing, signed realization or cross-notebook
theorem is assumed. The intended future use is comparing arithmetic
margins with coefficient-norm moment errors; those errors and all Xi
signs remain unpaid. Full matching Mathlib coverage is unchecked.

The bounded test is a complete finite estimate of both weighted sums
with enough exponent budget for the squared inverse norm and one
constant for every N>=2. If that cannot be justified from the cited
inputs, preserve the failed estimate and report the exact loss.
No new inequality has been derived in preparing this continuation.
This newly written assessment needs the separate approval next turn;
its readiness does not retroactively invoke mathematical work now.

## Direct-source recovery — 9 November 2026

The supervisor reported that ready assessments need a direct source URL.
This assessment formerly delegated all URLs to the earlier comparison.
The SOURCE_EVIDENCE line now supplies the essential URLs directly; the
exact TARGET, SPECIALIZE decision and scope remain unchanged.

Reaccessed the manuscript's full Lemma5 statement and proof, Tao's (3)
and opening proof, the classical Schur statement (a)-(c), and the
Rosser-Schoenfeld statement and Section9 locators. Reuse step235's
completed proof-case reads rather than claiming a new full source audit.
The manuscript explicitly includes shift zero. Its claimed inverse
estimate remains unverified locally; no derivation is performed here.
The scalar source retains its exceptional integer 223092870, with
indices1,2 outside the stated n>=3 range. The Schur source uses a
nonnegative kernel, sigma-finite measures and 1<p<infinity; finite
counting measure with p=2 is the intended later application. Both
weighted inequalities still need verification for the specific inverse.

No source blocker remains for the exact finite reproduction. The
squared norm, exponent allocation, complex coefficients and small
indices remain its mathematical checks. The prior duplicate comparison
and signed dyadic stop are reused unchanged. This is a process repair,
not a new estimate, new literature discovery or reset of any counter.
No lemmas, mathematical scripts, PROOF.md or DAG.md changed in this step.
The repaired assessment is submitted for separate next-turn approval.
