# Full-energy corrected localization: completed source comparison

TARGET: Assess source coverage for the two-window exact-moment-corrected IMS defect of the full Weil form at total length 8log3, with the fixed overlapping partition and six-mode neutral test specified in the nomination.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step314 checked the nominated statement, nonlocal IMS, logarithmic-Laplacian localization, exact moment correction and full Weil partition terminology; reused the October30 signed-localization comparison and November4 joint-energy/neutral-Rayleigh stops. Primary statements and essential proof cases below were inspected; no full matching theorem was located and no novelty is inferred.
SOURCE_EVIDENCE: Frank--Lieb--Seiringer math/0610593v2 Lemmas3.1/3.5 pp.8-9/12 and h_s definition p.5; Chen--Weth 1710.03416v4 Theorem1.1 p.2 and proof pp.6-7; DLMF5.9.12/5.9.16 and Re(z)>0 qualification; Kuberwastaken/riemann T1-ARCHITECTURE.md, main retrieved 2026-11-04, core/dipole and Assembly no-go sections. Reuse audited L744(6), L749 cutoff and L743(9)-(10), within their stated scopes.
COMPARISON: Standard IMS covers a fractional Hardy form and retains a signed overlap; the logarithmic-Laplacian theorem has symbol 2log|xi|, not the full digamma/prime/pole form. Existing moment right inverses cover different bumps. The external partition proposal reports numerical and envelope failures, not a theorem excluding this fixed corrected complete-form defect. No citation settles its sign.
GAP: The nominated H_j inverses, smooth translated supports, exact local/global moments, complete defect formula and certified sign on the exact six-mode kernel remain unproved. Full-class control, smaller-window positivity and uniform iteration remain independent gaps. No new mathematical result, matrix or sign was derived during this source review.
REASON: Essential source comparison is now sufficient for one bounded test of this precise difference from known identities; permit EXPLORE for the covered continuation only. Do not reprove fractional IMS or replace the complete symbol by a high-frequency approximation. The exact signed defect, rather than a generic identity or absolute envelope, must be the discriminating output.
SCOPE: Only the fixed definitions in the preserved nomination below, exact smooth zero extensions and both moments, total length 8log3 and local length 6log3, complete L744(6) including every in-window prime power and its pole normalization. No L742 conditional conclusion, arbitrary window enlargement, universal defect sign or positivity seed is approved.

LITERATURE_REASON: The invocation-start decision was REVIEW_REQUIRED for this exact new localization/correction scope; this is its first essential primary comparison, not a refresh of a ready target for balance purposes.
COVERED_TARGET: Derive and rigorously screen the full signed two-window exact-moment-corrected IMS defect on the nominated six-mode neutral space at total length 8log3, with the fixed partition and correction bumps.

## Completed comparison, 4 November 2026, step314

This is a literature-only assessment. The following nomination is
preserved as the exact future test; its references to step313 and a
pending gate describe its original status. This completed comparison
supersedes that gate status only for COVERED_TARGET. It proves none of
the proposed definitions' mathematical obligations or signs. A separate
next-turn approval of this newly completed assessment remains available
to the supervisor; no dependent research is performed in this turn.

### Inspected primary statements and proof cases

[Frank, Lieb and Seiringer, *Hardy--Lieb--Thirring inequalities for
fractional Schroedinger operators*, math/0610593v2,
27 October 2006](https://arxiv.org/pdf/math/0610593v2), Lemma3.5, p.12,
assumes 0<s<min(1,d/2), Lipschitz multipliers with squared sum one,
and a compact smooth input. It states h_s[u]=sum_j h_s[chi_j u]-(u,Lu),
where L has kernel a_(s,d)|x-y|^(-d-2s) sum_j(chi_j(x)-chi_j(y))^2.
Here h_s is the fractional Hardy form defined on p.5. Read the entire
statement and reduction to Lemma3.1, pp.8-9, including its Plancherel
and constant-evaluation proof. The bounded error retains a bilinear
pairing; the theorem grants no favorable sign for sign-changing u.
Neither s=0 nor the present signed digamma/atomic form is in its
hypotheses. It is a comparison input only: no fractional reproof,
s=0 differentiation, or universal signed-kernel extension is needed.
This reuses the October30 assessment's conclusion within its scope.

[Chen and Weth, *The Dirichlet Problem for the Logarithmic Laplacian*,
1710.03416v4, 1 September 2018](https://arxiv.org/pdf/1710.03416v4),
Theorem1.1, p.2, assumes u in C_c^beta(R^N), beta>0. Its operator
has symbol 2log|xi|, with a renormalized near-diagonal difference
integral, an exterior integral and the explicit scalar rho_N. It
also gives Lp convergence of the fractional difference quotient for
1<p<=infinity. Read the proof pp.6-7: the exterior support estimate,
local Holder domination, differentiated normalization, large-radius
limit and L2 Fourier passage. The prospective smooth tests meet its
regularity scope, but the multiplier differs from L744(6). This is
no theorem about moment-corrected Weil localization. Do not obtain a
digamma defect by dropping its low-frequency difference or by an
unjustified s=0 limit of the fractional IMS formula.

[NIST DLMF, Section5.9(ii), (5.9.12) and (5.9.16)](https://dlmf.nist.gov/5.9#ii),
live version accessed 4 November 2026, states for Re z>0 the scalar
integral representations of psi(z) and psi(z)+gamma; (5.9.12) keeps
the two cancellation terms together at zero. Substitution at
z=1/4+i xi/2 meets that half-plane hypothesis. This is a precise
known scalar input, not a new localization theorem. Any prospective
Fourier/kernel interchange still needs smooth-test domination at zero
and infinity. Reuse L744(6) for the complete normalization; no reproof
of digamma representation or replacement by log|xi| is justified.
The future defect can instead be evaluated directly from that existing
smooth-form identity, with rigorous Fourier-tail bounds.

### Exact and stronger-statement searches; overlap and failures

Web searches on 4 November 2026 used:

- `"logarithmic Laplacian" "localization" IMS`
- `"Weil" "quadratic form" "localization" partition unity`
- `fractional laplacian IMS localization formula Frank Lieb Seiringer lemma`
- `"logarithmic Laplacian" Chen Weth integral representation 2019`
- `"Hardy-Lieb-Thirring" "localization" "3.1"`
- `"Weil" "IMS" localization` and `"logarithmic Laplacian" "IMS"`
- `"Weil quadratic form" "partition" "localization"`
- `"Weil" "moment" "localization" positivity`
- `"IMS" "moment constraints"`
- `"localization" "digamma" "quadratic form"`
- `"exact moment" "localization" "Weil"`
- `"moment correction" "IMS"`
- `"Weil form" "partition of unity"`
- `"digamma" "IMS" localization`

Some exact searches returned unrelated Chern--Weil/index-theory or
nonmathematical IMS material. These are not evidence of novelty.
The 2025/2026 logarithmic-manifold, extension and fractional-logarithmic
papers, CIRM localization slides, secondary tutorials and search-only
platform hits are unread leads, not imported theorems. No such lead is
needed to define or directly test the fixed smooth energy already
available locally; no essential source-access blocker remains.

A particularly close primary research note is
[Kuberwastaken/riemann, T1-ARCHITECTURE.md](https://raw.githubusercontent.com/Kuberwastaken/riemann/main/experiments/weil_positivity/T1-ARCHITECTURE.md),
heading date 23 July 2026, unpinned main branch retrieved 4 November
2026. Read Lemma1's proof, the core/dipole decomposition and numerical
v1/v2 sections, and Assembly no-go analysis/Honest status. It studies
real tests on [-L,L], especially the one-prime regime, sharp spatial
blocks and archimedean-relative prime transfer. It reports failure of
block-norm screens and asserts a shrinking-transition IMS cost that
outgrows its gain. Those reports are not independently certified here;
an upper error estimate alone does not establish impossibility of
all spatial mechanisms. It contains no theorem on the present fixed
broad overlap, specified exact bump correction and complete six-mode
signed defect. Its displayed Certified Result1 uses an approximate moment nullspace
and retains poles; that result cannot establish our exact neutrality.
Do not import its global route ban, positivity claims or numerical
values. Its scope overlap strengthens the requirement to keep every
signed component and test the actual defect rather than an envelope.

Locally, reuse the complete October30 comparison in
[the weighted-localization assessment](2026-10-30-weil-nullvector-weighted-localization-coverage.md)
and its [scope stop](../../ATTEMPTS/2026-10-30-weil-nullvector-multiplier-source-stop.md).
That target was a nullvector-specific BV translation-slope estimate;
a generic static identity did not give its required S<=P-H bound.
The present finite-space defect is not a new proof of that inequality
or a renamed nullvector multiplier test. It has no nullvector premise,
no singular-multiplier limit and a fixed sign screen of its own.

The November4
[joint-energy source comparison](2026-11-04-joint-energy-mechanism-nomination.md)
excludes importing a differently normalized prime/pole core or a Schur
factorization with unpaid positive complement. The
[carrier-span scope stop](../../ATTEMPTS/2026-11-04-carrier-span-general-sign-scope-limit.md)
leaves arbitrary signed complements open. The
[neutral-prime-only stop](../../ATTEMPTS/2026-11-04-neutral-prime-only-rayleigh-saving-stop.md)
and audited L743 exclude moment-only unweighted arithmetic saving.
L749 excludes direct A>=W_b/2, not a complete-energy defect. These
are retained obstructions, not a global ban on the present target.

### Moment-correction comparison and permissible future work

L743(9)-(10), whose full matrix argument and exact correction were
read, supplies a ready right inverse for the two exponential moments
using a common cutoff times e^(+/-s/2). That is not the H_j matrix
in this nomination: its columns are two separated translated bumps.
Do not import G's positive definiteness as H_j's invertibility.
Elementary two-by-two linear algebra is the known mechanism; the
fixed columns' determinant, conditioning for any enclosure, translated
weights and complete correction-energy cost remain application
obligations for the covered attempt. No replacement bumps are approved.
L749 supplies the smooth eta/theta and cutoff-sine technique only.
No new right-inverse theorem, rank assertion, neutral basis or defect
formula has been established in this review.

DECISION EXPLORE authorizes one future mathematical screen of exactly
the preserved nomination. Standard source results above are cited
inputs or comparisons; the new signed defect is not covered by them.
A local proof of that defect's complete formula is necessary because
neither a fractional identity nor a prime-free multiplier covers it.
The execution must first justify inverses, smooth supports, moment
cancellation and translation conventions, retaining poles until exact
cancellation is proved. It must include the entire digamma multiplier,
all in-window prime powers, boundary-delay convention and full errors.
A negative vector requires exact neutrality and a strict certified
upper bound below zero. A claimed nonnegative trial form requires the
complete restricted Hermitian form with its exact constraint space;
pairwise tests or numerical eigenvalues are insufficient. An unresolved
enclosure remains inconclusive and must be saved without automatic
enlargement. If implementation is lengthy, save partial reasoning first.

The test and downstream limits in the nomination remain unchanged:
negative Delta abandons only this literal propagation rule; a finite
pass leaves full-class estimates, initialization and uniform iteration
open. Full matching Mathlib coverage was not checked; supporting
matrix/Fourier facts do not establish it. A later result may be labeled
POTENTIALLY_NEW only in the bounded-search sense, never as certified
originality or a solution of RH. No lemma, mathematical script,
PROOF.md argument or DAG edge changed in this literature turn.

## Nomination, not a mathematical result

The completed step313 work is solely the L749 audit. The following is
a proposed future test, with no defect calculation or source approval.
It prepares a possible central creative attempt rather than relabeling
the completed routine audit. A source comparison may find it covered,
obstructed or unsuitable and should route accordingly.

Put L0=4log3 and T=2L0. Use theta as defined in L749, and propose

    alpha(x)=(pi/2)*theta((x-3L0/4)/(L0/2)),
    rho_1(x)=cos(alpha(x)),  rho_2(x)=sin(alpha(x)),
    I_1=(0,3L0/2),  I_2=(L0/2,2L0).

These are proposed localization data, not an asserted propagation
inequality. Let ell=3L0/2 and a_1=0, a_2=L0/2. Fix the correction
bumps by the same flat function eta used in L749:

    beta_(j,k)(x)=eta(1-((x-a_j-k*ell/3)/(ell/12))^2),
       j=1,2, k=1,2,
    H_j(sigma,k)=integral_(I_j) exp(sigma*x/2)beta_(j,k)(x)dx,
       sigma=+1,-1,
    d_j(g)(sigma)=integral_(I_j) exp(sigma*x/2)g(x)dx.

The proposed correction is
C_j g=g-sum_k beta_(j,k)(H_j^(-1)d_j(g))_k.
Existence of these inverses and all exact support/moment assertions
are future proof obligations, not conclusions established here.
No floating-point nullspace or approximate neutrality is admissible.

For an exactly globally neutral smooth f on (0,T), the proposed
quantity to derive and test is

    Delta(f)=E_T(f)-E_(I_1)(C_1(rho_1 f))
                      -E_(I_2)(C_2(rho_2 f)),

where each E is the complete smooth Weil energy of L744 (6), on
the translated interval when appropriate. Retain its pole term until
both exact moments are justified, its entire digamma multiplier, and
all arithmetic delays: n<exp(T)=6561 for the total interval and
n<exp(ell)=729 for each smaller interval. Those cutoffs are simply
the definitions of the proposed forms, not a truncation of an infinite
form. The later comparison must check boundary delays and the precise
convention and cannot use L742 conditionally.

Bound the first mathematical screen, if later approved, to the six
functions obtained from L749's cutoff-sines by replacing its length
by T and its cutoff parameter by T/40. Use the exact common kernel
of the two exponential-moment functionals. No matrix, rank claim or
sign of this proposed trial form has been computed in step313.
The future attempt must first justify every definition, then derive
the signed localization and correction terms and certify their full
errors on this fixed trial space. A preview or pairwise estimate
does not certify the collective form.

## Relevance and discriminating test

The central gap is positivity on unrestricted support. A nonnegative
localization defect on a full class would transfer smaller-window
positivity to a larger interval, provided smaller-window positivity,
moment correction and uniform iteration were proved. Those are
independent unresolved steps. A six-mode pass alone establishes none
of them; it is only an initial test of the proposed mechanism.

The bounded decisive negative evidence would be one rigorously
exact-neutral trial vector with Delta<0: that abandons this literal
nonnegative-defect propagation rule. A certified nonnegative trial
matrix permits reassessment of the full-class defect, not a universal
sign claim or automatic family enlargement. An unresolved enclosure
is inconclusive and must be saved. Any continuation requires a new
input, informative obstruction or refined mechanism rather than
renaming the test.

This differs from the stopped direct A>=W_b/2 payment: it never
substitutes W_b for available complete energy. It differs from the
recorded generic Schur route because its actual signed localization
and finite-rank correction defects are the quantities to be tested,
not presumed controlled. The prime-only supremum obstruction remains
relevant: no moment-only arithmetic saving is assumed. The future
source review must search duplicates and known nonlocal IMS failures,
read exact primary hypotheses and reuse adequate local assessments.

If source coverage approves an uncovered central attempt, its purpose
would be proof_attempt/creative, deep_research/max: the precise
obstruction is the signed coupling cost of support localization after
exact moment correction. The bounded defect test above is required
before any support-propagation inference. The next turn itself is
literature_comparison at standard/high because essential coverage is
missing. No creative attempt, theorem, script or source approval is
claimed by this nomination.
