# Source assessment: complete conditional x-second regularity

TARGET: Determine whether L443's complete conditional x-second density is locally absolutely continuous in t on (H,2H) for every sufficiently large real H, retaining the high component, both intermediate selection rules, mass loss and translation.
CHECKED: 2026-10-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 276 reused the all-temporal and L440 calculus assessments; searched one-dimensional piecewise smooth gluing/weak derivatives and conditional second moments/measurable selection/absolute continuity; inspected Hunter's primary statements and Bell's proof, then compared the exact L419/L421/L429/L437/L438/L440/L443/L444 interfaces and the recorded bounded-repair failure. No matching law-specific theorem was found; no novelty inference follows.
SOURCE_EVIDENCE: Hunter, Notes on Partial Differential Equations, revision 2014-06-18, Examples 3.4--3.5, 3.58--3.61 and Theorems 3.53, 3.60, 3.62--3.63, printed pp. 48--49, 77--80; Jordan Bell, Sobolev spaces in one dimension and absolutely continuous functions (2015-10-21), Sections 2--3, Lemmas 2--3 and proof preceding Theorem 4; reuse Tao, An Introduction to Measure Theory (2011), Theorem 1.6.40 and previously inspected exercise scope.
COMPARISON: Standard sources cover integrable weak derivatives, absolutely continuous representatives and finite-interval calculus. They do not decide equality of the actual selected branch expressions, the high-kernel scale boundary, or cancellation in the complete raw 11 entry. This is a fixed-H specialization of known calculus, not a new general regularity theorem.
GAP: A later proof must check the complete density from L443 (1) with L438 (9)--(14), L421 (2)--(3), L437 (3)--(4), retaining mass loss and translation; neither individual atom jumps nor almost-everywhere classical derivatives decide the target.
REASON: Essential source coverage is now adequate for this exact bounded regularity test; branch algebra and any resulting conclusion are deferred to a separate mathematical turn. No larger repair or realization construction is approved.
SCOPE: Precisely L443's unchanged complete raw 11 entry at each fixed sufficiently large real H and original L429 stage; local absolute continuity and the distinction between the specified density and an almost-everywhere representative, without uniform derivative bounds or regularity of selected bulk atoms.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED and its complete-density branch scope had not been compared with the ready occupation and calculus sources. This is the required separate comparison, not additional browsing of a ready target.

The main gap remains global mixed positivity. L444's audited lower
bound stops bounded zero-11 repairs of the all-temporal identity.
This continuation tests a different obstruction: singular temporal
variation of the fixed x-second density would prevent an identity
with a locally integrable cross entry regardless of its size.
Absence of that obstruction would not construct a correction or
establish any other occupation identity.

Essential local inputs are L419's exact response forms and translation
interface, L421's high kernel and positive-direction rule, L438's
signed intermediate masses and full constant covariance correction,
L440's response regularity, L443's unchanged 11 entry, and audited
L444's necessary identity and size-only conclusion. L429 supplies the
original finite smooth product at fixed H. Read only the specific
formulas needed after comparing the already inspected source scopes.
No cross-notebook input is proposed.

The discriminating test for later research is an exhaustive regularity
check of the complete raw density across every relevant branch
boundary, including high-kernel scale changes and intermediate ties.
Continue only with source-approved treatment of those actual formulas.
A genuine singular defect must survive in the complete sum; a jump
in a selected atom or a large derivative of one term is insufficient.
If local absolute continuity holds, record that this obstruction is
absent and stop this target without inferring bounded derivatives,
exact mean compatibility or feasibility of a larger repair.

No growing covariance construction is proposed. Such feasibility,
actual/global realization, actual clipping, capped nondegeneracy,
L413's full-error margin and global mixed positivity remain open.
There is no actual sine-limit, independence, growing-character
uniformity or inter-H consistency assumption. Full matching Mathlib
coverage has not been checked.


## Inspected sources and their limits — step 276

[Hunter, author-hosted notes](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf),
revision 18 June 2014: Theorems 3.60 and 3.63 characterize absolute
continuity by integral reconstruction and an integrable weak derivative;
3.62 supplies integration by parts. Theorem 3.53 covers the stronger
bounded-derivative case. These statements concern representatives up to
a.e. equality. Examples 3.4--3.5 and 3.58--3.61 distinguish jumps,
singular continuous variation, and genuine absolute continuity. The
appendix supplies a proof outline rather than a full proof of every
characterization. Its hypotheses must be established on compact
subintervals; pointwise a.e. differentiation alone is insufficient.

[Bell, author's note](https://jordanbell.info/LaTeX/mathematics/sobolev1d/),
dated 21 October 2015, Sections 2--3: Lemma 2 proves the zero-distributional-
derivative constant assertion using zero-integral test primitives and
local integrability. Lemma 3 proves the weak derivative of an indefinite
integral by Fubini. The argument before Theorem 4 constructs an AC
representative for H1(R); the final theorem adds a Holder estimate using
L2. Its displayed theorem is not a W1,1 theorem on arbitrary intervals.
The inspected proof supports the representative distinction; Hunter is
the exact integrable-derivative citation. Brezis Lemma 8.1 and Leoni
Theorem 7.13 are references in Bell, not independently inspected inputs.

Reuse Tao's endpoint AC fundamental theorem and the qualified
exercise-level product/Lipschitz calculus coverage from
`drafts/literature/2026-10-19-prime-two-quadratic-occupation-audit.md`.
A finite branch gluing argument, if needed, is an elementary application
of that theorem which the later proof must write, not an imported
law-specific assertion. No reproof of the general characterization is
needed. No Mathlib lookup was needed for this source comparison; full
matching coverage remains unchecked, not asserted absent.

## Exact local comparison and approved obligations

The inspected formulas are L443 (1), L438 (6), (9)--(15), (19),
L421's high-kernel definition and positive-direction selection, L437's
negative direction (3)--(4), L429's finite product definition and
L440 (13). L419 supplies the exact response and translation interface.
Only their formula ranges were needed; bulk atom construction is not
a regularity theorem for the density.

At fixed H, the original stage j(H), calibration coefficients, integrated
matrix correction and normalization are parameters. The stepwise cutoff
in H is not a branch in the temporal variable t. The later proof must
justify the temporal smoothness it uses for the exact response, critical
input and signed calibration from their definitions; the older bounds
and mere continuity statements cannot substitute for this check.

The raw matrix formula to use is exactly L443 (1): R plus
w(Sigma^0+mm^T), with the later off-diagonal changes leaving entry 11
unchanged. Retain R, w=1-p-k_+-k_-, g_H=P_j/N_H, A_H and mm^T.
For the high component inspect rho0=0, the max defining r, and sign
reversal in Y at the level of its mass and raw second matrix. For the
positive intermediate inspect both candidate projections, their equality
branches and final reversal; for the negative intermediate inspect U/|U|
and its denominator bound. Retain both signed parts of F_H and their
h_+ and h_- denominators. The later proof must decide which selected
quantities actually enter entry 11 and w, rather than assuming that a
sign disappears from all terms because it disappears from a square.
No branch matching or cancellation is proved in this source turn.

Continue if these exact expressions can be shown to reconstruct an AC
function on every compact subinterval, or if a genuine defect of the
complete density can be isolated. Any representative issue must be
reported separately: changing finitely many tie values is distinct from
a persistent one-sided jump or singular distributional derivative.
Abandon this obstruction if complete local AC holds, without inferring
uniform derivative bounds, exact mean compatibility, positive covariance
feasibility or a correction satisfying all temporal tests.

The duplicate/failure check found no saved complete-density regularity
proof. L444's audited size obstruction and its ATTEMPTS record expressly
leave regularity open; L440 controls angular averaging through ties,
not temporal AC of this raw entry. The earlier Gaussian/core-tail stops
address different observables. None is reopened or weakened here.
The approved continuation uses known calculus with law-specific algebra;
classify a successful mathematical specialization as REPRODUCTION,
without claiming originality or progress beyond the inspected sources.
