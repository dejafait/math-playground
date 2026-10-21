# Coverage: fixed-prime signed cubic coefficient comparison

TARGET: Compare the sharp cos(t log 2)-weighted signed cubic of the actual critical jets with L429's unchanged complete counterlaw at scale (log H)^2.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step 213's completed focused discovery, local duplicate/failure searches and source comparison in drafts/literature/2026-10-18-prime-twisted-cubic-counterlaw-comparison.md; no matching full-statistic theorem or completed comparison was established, and no novelty is claimed.
SOURCE_EVIDENCE: Milinovich--Ng author-hosted 19-page Lower_Bounds.pdf, Lemma 6.1 p. 9, https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9 ; Gonek (1984), section 3, Lemma 2 p. 130, https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8 ; Sourmelidis--Steuding--Suriajaya 2007.14008v2 section 3 between (35)--(36), https://arxiv.org/html/2007.14008v2#S3 ; Fazzari 2306.15553v1 (3.5), https://arxiv.org/html/2306.15553v1#S3 ; DLMF 25.11(i)/25.11.5. Exact hypotheses and inspected proof cases are recorded in the completed comparison; reuse audited L406--L409 and L429 at their stated scopes.
COMPARISON: Fixed rational-frequency kernels and finite shifted Hurwitz inputs cover the two fixed cosine characters; they do not state the actual weighted coefficient or its difference from the complete law. The bounded change in frequencies, sharp endpoints, complete tails and full law corrections require a local specialization, without a new general moment theorem.
GAP: Determine or obstruct the actual-versus-law leading coefficient difference with total o((log H)^2) averaged error; its existence, value, sign and any separation remain unproved. All physical/global realization, clipping, capped nondegeneracy, regulator-margin and mixed-positivity gaps remain open.
REASON: One bounded mathematical coefficient comparison has adequate essential source coverage. This ready continuation was written during literature step 213 and requires separate supervisor approval before invocation; no calculation was performed under it.
SCOPE: Fixed prime 2, real cosine, sharp [H,2H], all sufficiently large real H, complete actual response and precisely the unchanged complete L429 law. No growing prime, conditional actual law, effective Poisson cutoff rate or law redesign.

The main gap remains global mixed positivity. This intermediate target
could identify sign-sensitive arithmetic information absent from this
particular selected-information counterlaw. A separation would reject
only adding this observable to that law; equality would reject this
leading-scale diagnostic. Neither outcome establishes actual clipping
or the full-error regulator margin. The source comparison and precise
citations are in the completed step-213 assessment above; no general
third-moment theorem or new source discovery is needed for this target.

Essential local inputs are L406, L407, L408, L409, L419, L421 and
audited L429. Read their needed proofs normally. L423 supplies the
inherited full correction interface; its old fixed mixture is not the
law under test. L427 and L428 are contrasts with narrower stopped
scopes. C426c and the parked core/tail calculation are unused.

Compare the actual sharp average of Delta Bcal cos(t log 2) with
E_nu[DB cos(t log 2)], using the same dt/H marginal and ell=log H.
Do not infer either coefficient from the unweighted beta, the fixed-prime
x-second limits or Young's quadratic theorem. The permitted proof work
is the changed local specialization of already imported tools:

1. Retain L406's absolute physical transfer and every L407 carrier and
   ordinary-jet term. Encode both cosine characters as rational twists,
   rather than as slowly varying weights. The single-carrier parameters
   are 2mn/k and mn/(2k); the zero-carrier parameters are 2mnk and mnk/2.
   Keep all signs, amplitudes, exact analytic weights and real projections.
2. At fixed head, specialize the arbitrary reduced-rational Hurwitz/pole
   calculation, with all nonunit/zero residue classes and absolute sharp
   boundary estimates. Do not substitute a sharp indicator into a
   Schwartz theorem or differentiate an asymptotic error.
3. Establish complete response passage from L409's frequency-level
   majorants for both characters, including both connectors and endpoint
   transitions. Treat integer resonances and nonresonant terms for the
   denominator-two zero-carrier grid explicitly. Take H first at every
   fixed head before removing that head. Bounded cosine does not
   automatically transfer an already integrated signed-tail estimate.
4. Retain every component of the complete law. Check the high bound,
   intermediate calibration and conditional signed-bulk identity, with
   bounded mean, full A_H matrix, normalizing mass and cutoff. Do not
   replace the law by its centered covariance or assume an actual
   conditional distribution. Keep all error terms below this scale.

Continue if a nonzero coefficient difference is rigorously separated
from the total remainder; an exact equality is also an informative
negative result for this diagnostic. If the coefficients cannot be
separated by the available estimates, record the actual unresolved
bound. Abandon the proposed certificate if any essential tail, sharp
endpoint, resonance or correction cannot be controlled; that is not
an impossibility theorem for the observable. Stop for separate review
if a changed theorem, weight, law or mechanism becomes essential.

No coefficient or limit is asserted in this coverage file. Unresolved
assumptions include the entire weighted comparison, actual critical
function realization, cross-H consistency, actual clipping and capped
nondegeneracy, L413's regulator margin and global mixed positivity.
Full matching Mathlib coverage is unchecked, without an absence claim.
There is no cross-notebook input. Mathematical exploration usage remains
0 of 3 before the proposed attempt.
