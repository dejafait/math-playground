# Zero-extracted signed inverse — source comparison

TARGET: Assess whether zero-extracted contour estimates for L975's complete binomial inverse provide a cancellation-sensitive remainder bound, retaining multiplicities and off-line contributions without RH.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step213 searched Li finite-zero contour remainders, incomplete Li coefficients and Lagarias theorem corrections; narrowly screened local literature/attempts/history/foundations for incomplete Li, 0404394 and the exact theorem, and reused steps171/186/203/212. No novelty claim. Prior nomination evidence: Nomination only: narrow searches of November10 literature/attempt records and L960-L975 for deflation, Darboux, zero clusters and singularity subtraction found a Darboux reference in the prescribed-eta assessment; the exact new target has not received an external theorem or comprehensive duplicate comparison. Reused the inspected bn inverse and signed-forcing source-limit records; no novelty inference.
SOURCE_EVIDENCE: Step213 read Lagarias AIF57(5)(2007), Definitions4.3/(4.5), Lemma4.4/(4.6)-(4.8), Theorem1.1/(1.17), and Theorem6.1/(6.1)-(6.14), pp.1693-1694,1708-1709,1721-1726; cross-checked arXiv math/0404394v4 Section6 in full. Read Coffey0912.2390v1 (1.1)-(1.3), Proposition1/(2.1), and Voros math/0506326v2 Section3/(14) through both RH cases. No signed residual estimate is imported. Earlier nomination context: Reused L975's He-Jejjala-Minic arXiv0903.4321v2 equation(3.4), Coffey arXiv0912.2390v1 equations(1.1)-(1.3), and L968's Lagarias AIF57(5)(2007) Theorem2.4(2)/(2.21) citations as leads and normalization context. No source passage for zero-extracted contour remainder estimates was inspected in step212. Existing exact inverse and Pringsheim coverage do not approve this different target.
COMPARISON: Lagarias states an unconditional growing-height extraction with O(sqrt(n) log n) residual, beyond a bare zero-sum identity; however its printed residue sign and horizontal proof need an independent audit before local import. Coffey supplies representations, and Voros distinguishes conditional asymptotic cases; neither pays L968 unconditionally. L975/L976 remain unchanged.
GAP: No certified cancellation-sensitive remainder is available from this review. Audit the sign, zeta pole normalization and horizontal estimate of the inspected Lagarias theorem before any application; even a valid polynomial residual leaves its growing incomplete-zero contribution unsigned.
REASON: Completed the required changed-target source review. Primary proof passages identify a concrete audit rather than an inaccessible source or an assumed cancellation estimate. No repair, new lemma or mathematical script was produced. The original nomination below is preserved as history, not current approval.
SCOPE: Source comparison only, with finite conjugation/reflection-invariant zero multisets, full multiplicities, ordinary Li normalization and the actual residual germ. Do not assume removed zeros are on the line, omit remaining zeros, or infer an all-n sign from a finite set.

## Main gap and bounded downstream test

The main gap remains L030-L032/C032a positivity and L966's complete
signed forcing. L968's downstream threshold is a lower bound
lambda_n >= -K_epsilon exp(epsilon n) for every epsilon>0 and all n,
with K_epsilon independent of n. L975's inverse is a usable identity;
the coefficientwise way of paying that threshold has failed in L976.

The proposed intermediate source target is an exact finite-zero
extraction inside a coefficient contour, together with a bound for
the remaining signed contribution. No such formula or bound is derived
here. Keep the finite-cluster contribution intact until after the
complete transform. The motivation is to test cancellation that the
termwise lower envelope discarded; no favorable sign is assumed.

Read primary statements and the sign/contour-determining proof cases
before larger extracts. Begin with the accessible Li-coefficient
sources already cited in L975/L968 and their relevant references.
Check exact statements, stronger results and local duplicates, including
the recorded Darboux and Voros comparisons, before nominating a proof.
Do not retry the parked Coffey 2007 retrieval without new access.

Continue only if the review identifies a precise available estimate
or an independently testable residual mechanism beyond the known
zero-sum identity. Record its dependence on n, the extracted set,
contour clearance and all remaining zero contributions, and compare
its achieved rate with the every-epsilon threshold above. A weaker
intermediate estimate is useful only with a stated downstream role.
If extraction merely restates the Li zero sum, hides RH in a contour
deformation or pays the residual only with the rejected coefficient
envelope, stop this candidate with that specific overlap or defect.
An inaccessible optional source does not justify renewed retrieval
loops; distinguish it from an essential missing theorem.

## Three mechanisms compared for the continuation decision

1. Termwise geometric correction of the actual b_m coefficients:
   L976 now passes its audit, so the every-delta payment is closed.
   Preserve the canonical stop in ATTEMPTS/2026-11-10-bn-every-delta-envelope-stop-210.md.
2. Direct theta-Laguerre cancellation import from Coffey 2007:
   the primary-source blocker in the step203 assessment and step204
   attempt record persists. No new access is available; keep it parked.
3. Finite zero extraction with a signed contour residual:
   selected for a new source comparison, independently of the blocked
   article and without paying a termwise coefficient envelope. Its
   possible overlap with known Li asymptotics remains unresolved.

This is a nomination, not another mathematical exploration or an
approval of previously uncovered mathematics. No justified creative
proof attempt is ready: an independent signed residual estimate has
not been identified. If this review supplies one, specify a bounded
test and its obstruction before recommending creative routing; do not
label standard contour algebra creative merely to satisfy scheduling.

Essential local context for the review is L975/L976 and the audited
Li threshold in L968; L018/L024/L026 provide zero correspondence,
summability and localization if actually used by a source application.
L966 identifies the independent main sign gap. No cross-notebook
input is proposed. Full matching Mathlib coverage remains unknown.


## Completed source review — step213, 10 November 2026

### Primary statements and scope

J. C. Lagarias, *Li coefficients for automorphic L-functions*,
Ann. Inst. Fourier **57**(5) (2007), 1689-1740,
[Theorem6.1, (6.1)-(6.14), pp.1721-1726](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=34),
states S_f(n,pi)=lambda_n(sqrt(n),pi-dual)+O(sqrt(n)log n),
unconditionally, with constant depending on pi. The incomplete sum
retains multiplicities and all zeros with |Im rho|<=T, including
off-line ones. Its extracted set grows with n; it is not an arbitrary
fixed deflation set. The proof chooses a pole-avoiding rectangle with
-3<sigma_0<-2, sigma_1=2sqrt(n), T in [sqrt(n),sqrt(n)+1], and compares
the endpoint sum with cutoff sqrt(n). Theorem1.1/(1.17), p.1694,
places that sum with a minus sign in the full-coefficient formula.
Definitions4.3/(4.5) and Lemma4.4, pp.1708-1709, include the zeta pole
subtraction and delta=1. The statement's hypotheses include the trivial
GL(1) representation, whose completion is 2xi; reuse L968's normalization.

The complete Section6 was also inspected in
[arXiv:math/0404394v4, 4 May2005](https://arxiv.org/html/math/0404394v4#S6).
Its equations are numbered (6.106)-(6.119); the published numbering is
canonical. Both versions require checking the transition from the
kernel and negative logarithmic derivative to the residue sum, and
from the horizontal bounds to the asserted geometric decrease. This
review records suspect passages, not a corrected theorem or disproof.

### Independent known comparisons

Coffey, [0912.2390v1, (1.1)-(1.3) and Proposition1/(2.1), pp.2-5](https://arxiv.org/pdf/0912.2390v1#page=2),
supplies the ordinary-Li and b_m zero representations. This is identity
coverage, not an estimate for an extracted residual after the complete
inverse. L975 already checks the branch/interior inverse; do not
repeat that calculation or enlarge its domain. L976's coefficient
lower-envelope obstruction is preserved.

Voros, [math/0506326v2, Section3/(14), pp.4-5](https://arxiv.org/pdf/math/0506326v2#page=4),
distinguishes RH-false pole contributions, allowing multiplicities,
from the RH-true saddle calculation. Its infinite expression is an
asymptotic expansion, not an absolute finite-n zero sum. It supplies no
unconditional lower bound for the residual germ. Reuse step171 and
step186's detailed conditional-scope comparison. These sources do not
license removal of unknown off-line poles from a deformation.

### Load-bearing audit questions, left unproved

The precise next assessment names one bounded audit of Lagarias's
published theorem. Check the residue sign for the printed integrand
k_n(s)(-L'/L)(s+1), including multiplicity, normalization by 2pi*i,
functional reflection and the zeta pole at s=0. Compare the actual
result with (6.5)-(6.7), Definition4.3 and Lemma4.4, rather than changing
the Li convention to make signs agree. In particular, the general
coefficient definition and the separate zeta remark (4.12)-(4.13) must
not be interchanged without checking their signs.

Separately, the horizontal argument after (6.12) asserts geometric
decrease, following a kernel-ratio upper bound e and a Dirichlet-series
factor 2 per unit step. That passage, including the shift s+1, requires
replay; its conclusion is not imported from the printed assertion.
The printed zero-clearance wording and the transient O(sqrt(n)) claim
also require distinction from the final O(sqrt(n)log n) bound. A
failure of a displayed majorant alone would not disprove the integral
estimate or RH. No asymptotic envelope, counterexample or repair is
proved in this literature step.

The claimed residual rate would be polynomial, whereas L968 requires
a lower bound for the **whole** lambda_n at every positive exponential
rate. The source keeps a signed growing zero contribution explicit.
A favorable residual rate cannot pay that contribution by itself.
Thus neither a fixed certified zero list nor the stated truncation
theorem resolves the main sign gap. No effective constants or
independence from arbitrary extracted sets have been established here.

### Search, access and duplicate limits

Queries included `Li coefficients finite zeros remainder contour
Lagarias Voros asymptotic RH false`, `Coffey 0912.2390 Li coefficients
b n zeros`, `Lagarias Li coefficients sign Theorem 6.1`, exact-title
`erratum`/`correction sign`, and exact `(6.12)` variants excluding
researchai.dev and researchgate.net. Primary arXiv metadata confirms
v4 as the latest posted version, with a historical remainder-correction
comment; that comment is not a new correction to the inspected version.
No inspected primary erratum was found. This is a bounded search, not
proof that no correction exists. Search results included external AI
research discussions; none was loaded or used as theorem evidence.

The notebook duplicate screen found step171/172's criterion use and
step186's Voros comparison, but no prior local application or audit of
the growing-height Theorem6.1. Existing ready assessments cover their
unchanged targets and are reused. The parked Coffey2007 source was not
retried. PDF screenshots returned text placeholders; they supplied no
visual verification. Shell PDF retrieval failed DNS and saved no source
certificate. Primary PDF text and the complete arXiv HTML Section6
supply the passages listed above; no access blocker remains for the
bounded audit. Full matching Mathlib coverage is unexamined/unknown.

Outcome: NEGATIVE, LITERATURE, NOVELTY_UNCHECKED. The useful new source
comparison changes routing: do not import the proposed polynomial
residual automatically; audit its exact load-bearing claims first.
This does not declare the published theorem false, prove a new
obstruction, or advance RH. No creative central proof target is yet
justified because a reliable signed residual estimate remains missing.
