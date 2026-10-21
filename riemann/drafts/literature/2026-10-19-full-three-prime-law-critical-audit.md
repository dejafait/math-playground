# Source coverage: critical audit of the full three-prime law

TARGET: Critically audit L438's full three-prime signed law, including finite-height Gram calibration and preservation of every L437 constraint.
CHECKED: 2026-10-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 250 read all of L438, reused step 248's exact-target discovery and primary readings and step 246/247's L437 coverage/audit, and compared scoped L419/L429/L431/L435/L436 interfaces and the recorded antipodal/radial/clipping failures. No completed duplicate L438 audit was identified in these records; no fresh external search or novelty inference.
SOURCE_EVIDENCE: Reuse Kowalski January 19 2021 manuscript B.6.3/B.6.5(2)/B.6.6(2), printed pp. 146--147, continuous-character proof; Carlen--Lieb 0904.0734v2 pp. 1--2, Horn theorem after (1.1), proof through (1.2); finite Poisson and actual-moment coverage through the unchanged audited local interfaces. Precise hypotheses, links and applicability are compared below; no fresh primary retrieval is claimed.
COMPARISON: The fixed-test averaging and real symmetric matrix hypotheses remain inside prior coverage. Neither source supplies a moving Gram calibration, nonnegative supported probabilities, Borel matrix choices or preservation of old errors; L438's explicit argument and the unchanged local interfaces must be independently audited for these claims.
GAP: Separate mathematical audit of L438 (5)--(20), including Gram conditioning, the correction orientation and exact three averages, uniform boundedness, simultaneous fixed-character limits, Borel family and every original L437 constraint; none is certified by this source comparison.
REASON: Essential coverage is adequate for one later RESEARCH proof_audit of exactly TARGET under SPECIALIZE. This literature-only step approves the audit scope, preserves step 249 and neither verifies nor modifies its construction.
LITERATURE_REASON: The next task concerns the newly written L438 proof, beyond the existing L437 audit scope; reuse ready sources and inspect only any changed applicability obligation.
SCOPE: L438's full stated selected-law result and its direct inputs only; no additional primes, actual sine limits, growing-character uniformity, global realization, actual clipping or regulator conclusion.

## Original proposal, retained for scope

The following proposal records the pending state before step 250. Its
pending source-comparison statements are superseded by the completed
comparison below; its mathematical target and tests remain unchanged.

The main RH gap remains global mixed positivity. This proposed audit
would check whether the full three-prime cubic family still fails to
force the favorable joint sign in the selected relaxation. It is not
an invitation to enlarge the character set after a successful check.

Essential mathematical inputs are L435's exact continuous density and
g_v coefficients, L436's fixed P,I, L437's two supported directions
and audited finite projection, L431's old tolerances, L429's unchanged
all-real-H cutoff, and L419/L421's Borel matrix/high interfaces.
The prior comparison is
`2026-10-19-full-three-prime-signed-law-feasibility.md`; the previous
finite-law audit coverage is
`2026-10-19-signed-intermediate-counterlaw-critical-audit.md`.

Reuse the primary continuous-time compact-group theorem at
[Kowalski, printed pp. 146--147](https://metaphor.ethz.ch/x/2021/fs/401-3109-65L/probabilistic-number-theory-fs-2021.pdf#page=150)
and the real constant-diagonal theorem at
[Carlen--Lieb, pp. 1--2](https://arxiv.org/pdf/0904.0734v2).
The prior assessment records which hypotheses and proof cases were
inspected; no fresh primary retrieval is claimed here. General signed
moment representation is not an input. Full matching Mathlib coverage
is unchecked, not absent.

After source scope is separately approved, the critical mathematical
test is L438 (5)--(8): positive definiteness at fixed P, eventual
invertibility uniformly on all real H, the orientation of the Gram
correction, its exact three averages and uniform convergence to the
full density. Qualitative convergence alone must not be substituted
for an O(1/log H) rate. The exact calibration is intended to avoid
that rate requirement; its validity remains to be independently checked.

Then audit (9)--(20): nonnegative probabilities on exact supported
directions, complete mass and covariance recomputation, unchanged
Poisson limits, Borel dependence, strict translated bulk support, both
tiny odd tolerances, every old moment and envelope, and the cap for
one family independent of lambda and the subsequently tested character.
Inspect the signed conditional bulk cubic bound separately from an
absolute cubic bound. Huge fixed P constants may change the onset but
cannot be treated as uniform in P or allowed to grow with H.

Continue only if all original remainders and constraints survive; a
failure should be localized and repaired within scope or recorded as a
limitation of L438. Actual/global realization, actual clipping, capped
nondegeneracy, L413's full-error regulator margin and mixed positivity
remain unresolved even if the audit succeeds. No audit is completed or
approved by writing this proposal, and no mathematical result from
step 249 is rejected because its next assessment is new.

## Completed source-scope comparison — 2026-10-19, step 250

LITERATURE / NOVELTY_UNCHECKED / literature_comparison; outcome
EXPLORATION. This resolves coverage for the separate audit, not the
correctness of L438. No lemma, mathematical script, DAG or argument in
PROOF.md is changed. Mathematical exploration usage stays 0 of 3;
this review neither spends nor resets that budget.

### Known inputs and exact scope

Reuse the primary readings and discovery recorded in
`2026-10-19-full-three-prime-signed-law-feasibility.md` (step 248),
`2026-10-19-signed-intermediate-counterlaw-critical-audit.md`
(step 246), and their named earlier assessments. Read L438 in full
to identify its source uses, L437's separate step-247 audit, L431's
hypotheses/conclusion, L429's all-real-height cutoff (10), L419's
explicit matrix branches, and L435/L436's coefficient/density and
fixed-witness interfaces. This is an applicability comparison; the
algebra and estimates in L438 remain for the next research audit.

E. Kowalski, *Arithmetic Randonnee: An introduction to probabilistic
number theory*, January 19, 2021 manuscript,
[B.6.3, B.6.5(2), B.6.6(2), printed pp. 146--147](https://metaphor.ethz.ch/x/2021/fs/401-3109-65L/probabilistic-number-theory-fs-2021.pdf#page=150),
is reused with the continuous-character proof inspected in step 248.
B.6.3 tests convergence on a compact abelian group by its continuous
characters; B.6.5(2) concerns continuous linear time and Haar measure
on the orbit closure; B.6.6(2) identifies the full torus under rational
independence of the velocities. It provides qualitative convergence
for fixed continuous tests, with no rate for a general continuous
density and no theorem for a moving test family.

L438 requests precisely fixed continuous tests of three prime angles
before introducing its correction: the entries of phi phi^T, f phi,
and each separately fixed f C_v. The required independence and the
conversion of the source's [0,X] averages to [H,2H] are explicitly
addressed in L438 (4) and must be checked there. This adds no gamma
coordinate, discontinuous test, physical sine theorem or growing
character. In particular the old O(ell) cubic errors cannot follow
from qualitative averaging alone. The proposed finite-height identity
(7), rather than an unread effective equidistribution theorem, is the
claimed remedy. A separate audit of its conditioning, orientation,
uniform convergence and parameter continuity is therefore essential.

Eric A. Carlen and Elliott H. Lieb, *Short proofs of theorems of Horn
and Mirsky on diagonals and eigenvalues of matrices*,
[arXiv:0904.0734v2](https://arxiv.org/pdf/0904.0734v2), May 13, 2009,
pp. 1--2, Horn theorem after (1.1), proof through (1.2), is reused
with its previously inspected two-dimensional rotation and inductive
deletion/embedding cases. Its finite real majorization statement
supplies real orthogonal realization. L438 proposes the same constant
trace-average application to a real symmetric matrix as L437. It
requires no covariance upper bound, no H-independent spectrum and
no new theorem for a growing covariance. Positivity of Sigma, the
negative trace margin, translation estimates and Borel dependence
are separate local obligations. L419's explicit deterministic equality
and strict branches, rather than Schur--Horn by itself, are the cited
implementation. Reproving general Schur--Horn would not settle those
obligations.

C. Aistleitner, I. Berkes and K. Seip, *GCD sums from Poisson integrals
and systems of dilated functions*, JEMS 17 (2015),
[pp. 1523, 1527, identity preceding Lemma 1/(23)](https://ems.press/content/serial-article-files/32047?nt=1),
is reused through L429 at the already inspected finite-product scope:
normalized Haar measure and radii in (0,1). L438 retains L429's cutoff
and response-only tests, not a new moving-product theorem. Its changed
lost mass, N_H and normalized measure require the perturbation check
(12)--(13). Bounded full-response tails and every fixed-prime limit
remain inputs from the same local interface.

L435 supplies the continuous signed density and every separately fixed
g_v, using its audited fixed-positive-rational moment interface. L436
supplies the single fixed P,I, and L437 supplies the two exact-response
directions and finite projection. L438 requests no additional actual
zeta moment, jet order, rational-twist uniformity or source statement
about a conditional critical law. The Young, Hughes--Young, Bui--Hall
and absolute-envelope inputs already assessed through L431/L437 stay
at their original scopes. Preservation of every tolerance remains an
explicit audit task, not a fresh application licensed by terminology.

General signed moment representation, Richter representation and
purification are not inputs. Step 248's inspected Schmudgen theorem
does not supply positive conditional probabilities or this prescribed
marginal. Its unread matricial-moment lead remains nonessential and
unread. No additional essential source gap was identified. Full matching
Mathlib coverage of the resulting family and source statements remains
unchecked, not absent.

### Nonduplication, failures and the bounded audit

L437's completed audit expressly excludes the full character family;
it does not verify L438's moving correction. Step 248 covers discovery
for that exact enlarged construction, while step 249 is the construction
awaiting review. These records supply no duplicate completed audit.
No new search is needed merely because the task is now an audit.
The October-16 antipodal/sign-only and capped-radial failures concern
different critical-state restrictions; their original obstructions stay
recorded. The step-243 actual-clipping source blocker is not reopened.
L436 still obstructs a positive scalar calibration; it neither rules
out two supported cubic orientations nor verifies their probabilities.
L428's uniform-bulk-density stop and all narrower law separations also
retain their scopes. No other notebook was read.

The next audit must first check L438 (5)--(8), using L437's fixed
projection and L435/L436's exact Haar averages. It must retain fixed-P
conditioning on the entire real-H ray, the sign of the residual and
Gram inverse, the exact three finite-height averages, uniform boundedness
and convergence, and the Borel construction. An o(1) calibration error
cannot replace the exact identity when proving the old O(ell) errors.

Then check (9)--(20) against L437's full constraint list: nonnegative
fiber masses, both response-uniform directions, unchanged high kernel,
complete normalization/mean/covariance recomputation, positive covariance,
strict translated bulk support and all Borel branches; exact even and
tiny odd seconds and first-B mean; first-D, W^2 and each fixed-prime
second limit; all 23 quartics, both third envelopes, fourth envelope
and fixed physical bounds. Distinguish the signed conditional bulk
cubic estimate from an absolute cubic bound. Check all three original
cubic remainders as well as the weaker new fixed-character limits.
Finally check the absolute cap for the same family independent of
lambda and of the subsequently tested character. No P-dependent
constant may silently become uniform in P or grow with H.

Continue only if every original constraint survives that mathematical
audit. A concrete defect should be repaired within this scope or
localized as a limitation, rather than hidden by a weaker asymptotic.
A successful audit would validate the limitation of this full three-prime
diagnostic in the selected relaxation. It would not justify automatic
enlargement to further primes or resolve actual/global realization,
actual clipping, capped nondegeneracy, L413's full-error regulator
margin or global mixed positivity. No RH range or main argument changes
in this literature-only step.
