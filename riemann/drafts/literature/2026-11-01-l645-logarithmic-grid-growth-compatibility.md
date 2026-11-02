# L645 logarithmic-grid growth compatibility — source assessment

TARGET: Determine whether unconditional completion and zeta-derivative growth bounds force L645's inequality (7) to fail for every sufficiently high simple zero with fixed displacement delta in (0,1/2).
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Checked L018/L258/L645, the producing Pick assessment, its independent audit/history and the fixed-reserve stop; searched zeta derivative convexity, vertical-strip Stirling and quantitative Xi/Pick growth terminology. Read the primary statements and the derivative proof paragraph identified below; no exact matching height-compatibility theorem was located in the inspected sources, without any claim of novelty.
SOURCE_EVIDENCE: S. M. Gonek, Invent. Math. 75 (1984), 123–141, Section 2, equation (20), p.127 and its complete following Cauchy-estimate paragraph; NIST DLMF 1.2.8 (2026-09-15), 5.11.9 with bounded-real-part uniformity, 5.11.1–3 and complex remainder paragraph, 27.4.3/5 with absolute-convergence condition, and 25.2.6/8 with their domains. L018/L645 supply the unchanged completion, circle maximum and exact strict threshold.
COMPARISON: Classical unconditional derivative convexity, uniform Stirling and reciprocal-series bounds cover the analytic inputs; none of the read sources compares this exact H_rho with L645 (7). L258 remains a different growth-priced detector; C644a obstructs a fixed norm reserve, not this comparison. The remaining work is a standard specialization, not a new sign mechanism.
GAP: In a separate mathematical turn, obtain a justified lower bound for the exact H_rho from the covered inputs, compare its exponent with the exact lambda_delta, and handle constants and floor(log gamma); no incompatibility or onset has yet been proved.
REASON: The previously missing primary growth coverage is now supplied. SPECIALIZE licenses only the stated fixed-delta quantitative comparison after the supervisor's separate approval; import the standard estimates and justify their application rather than reprove convexity. The completed L645 audit remains accepted.
SCOPE: The exact TARGET with fixed delta in (0,1/2), simple stipulated rho and unchanged L645 disk/nodes is covered for a separate research step using the inputs below. No hypothetical zero existence, derivative lower bound, multiple-zero extension, optimized disk, delta tending to zero or actual matrix signs are covered.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED gate lacked essential primary derivative-growth and safe-half-plane lower-bound coverage; the interpolation audit did not assess those changed hypotheses. This single source turn fills that gap.

## Exact proposed test and relevance

For each fixed delta in (0,1/2), condition on a simple zero
rho=1/2+delta+i gamma of the completed xi, gamma>=e^5. Retain all of
L645's definitions: s_*=2+i gamma, a=3/2, d=a-delta,
R_delta=a-delta/2, M_rho, H_rho, A_delta, q_delta and lambda_delta.
The proposed question is whether there is an onset T_delta such that
every such zero with gamma>=T_delta fails L645 (7). No such onset or
failure is asserted here. The strict comparison to test is exactly

    H_rho < A_delta^(-1) exp(lambda_delta floor(log gamma)).

The main gap remains actual-Xi positivity at unbounded heights. The
downstream purpose of this test is to decide whether L645's present
sufficient bound can connect those logarithmic-size matrices to
exclusion of a putative simple zero. A proved incompatibility would
limit this quantitative implementation, not the every-grid detector,
the possibility of a smaller witness, matrix positivity, or RH.

## Proposed implementation and bounded continuation test

The original source nomination called for exact detector overlap,
uniform vertical-strip Stirling, safe-half-plane zeta lower bounds and
an unconditional upper bound for |zeta'|. The completed source review
below covers these inputs. An upper bound for the derivative is the
prospective input for a lower bound on the ratio; no lower bound for
the derivative is authorized or assumed.

After separate approval, continue to a mathematical comparison with the
exact required exponential in floor(log gamma). If that comparison
does not discriminate, retain an inconclusive gap; source availability
alone does not prove incompatibility.
Do not replace the target by merely showing H_rho finite, repeating
the audited threshold, or trying again to obtain a fixed norm reserve.
If this test fails to discriminate, preserve its evidence and select
a materially different signed mechanism rather than prolonging it.

L018 and L645 are the essential local mathematical inputs for the
proposed continuation; L258 and C644a are overlap and contrast only.
Independent actual positivity, arbitrary small-delta uniformity, zero
multiplicities and all-degree mixed positivity remain unresolved.
No cross-notebook input is proposed. Matching Mathlib coverage for
these new growth estimates has not been checked; no absence is claimed.

No new central creative sign mechanism is nominated: the screened
arithmetic and collision routes still lack a specific signed relation
or collision-valid functional. This concrete compatibility test must
be assessed as a standard theorem application, not relabeled creative.

## Completed source review — 1 November 2026

This is a literature-only assessment. No bound for H_rho, estimate of
lambda_delta, incompatibility conclusion, onset, lemma or mathematical
script is derived here. The standard estimates below are source inputs;
their assembly is the unchanged research target.

### Primary derivative input and its relevant proof case

S. M. Gonek, *Mean values of the Riemann zeta-function and its
derivatives*, Inventiones Mathematicae **75** (1984), 123–141,
[author-hosted published PDF](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf),
Section 2, equation (20), printed p.127 (PDF page 5): for each fixed
nonnegative derivative order nu and epsilon>0, the critical-strip case is

    |zeta^(nu)(sigma+it)| << |t|^((1-sigma)/2+epsilon),
    0 <= sigma <= 1, |t| >= 1/2.

Only fixed sigma=beta in (1/2,1) and nu=1 are needed; allow the
implicit constant to depend on beta, epsilon and nu. The adjoining
cases concern sigma<0 and sigma>1 and are not required. Read the
complete following proof paragraph: the source applies Cauchy's
analytic derivative estimate on a small disk to the nu=0 bound,
referencing Titchmarsh [9], pp.81–82. The preceding selected-height
log-derivative estimates (16)/(18) and RH-dependent introduction
corollaries are different statements: equation (20) has neither
restriction. Import (20), not a derivative of a real-variable error.
Titchmarsh's cited pages were not separately inspected in this turn.

### Gamma and safe-half-plane inputs

NIST DLMF, version **1.2.8**, release **2026-09-15**, accessed
1 November 2026:

- [5.11.9](https://dlmf.nist.gov/5.11.E9) states
  |Gamma(x+iy)| ~ sqrt(2pi)|y|^(x-1/2)exp(-pi|y|/2) as
  y tends to either infinity, uniformly for bounded real x.
  Read that uniformity sentence, the sector conditions preceding
  [5.11.1–3](https://dlmf.nist.gov/5.11#i), and the complex remainder
  paragraph in [5.11(ii)](https://dlmf.nist.gov/5.11#ii).
  This matches the existing gamma input in foundations/notation-and-inputs.md.
  Bounded real parts and fixed imaginary shifts fit this scope.
  No zeta or zero-location assumption enters.
- [27.4.3 and 27.4.5](https://dlmf.nist.gov/27.4) give the zeta
  Euler product and 1/zeta(s)=sum mu(n)n^(-s), Re(s)>1.
  Read the absolute-convergence proviso preceding these examples.
  The prospective safe-line lower estimate is an absolute-value
  specialization of that reciprocal identity; write it out in the
  research proof. [25.2.6](https://dlmf.nist.gov/25.2.E6) gives the
  absolutely convergent zeta derivative series on the same half-plane
  if anchor control is needed. These are not critical-strip series.
- [25.2.8](https://dlmf.nist.gov/25.2.E8), Re(s)>0 and positive
  integer N, supplies the finite Euler summation formula with its
  integral remainder. This is a fallback source, not an already
  differentiated estimate or a necessary extra research target.

### Exact specialization still required

Retain L018's entire completion and L645's full circle maximum, not
an uncompleted zeta maximum. In a later proof, justify any use of an
interior safe-line value to bound that maximum, and differentiate the
completion at the stipulated zero while retaining every prefactor.
Check which terms vanish because zeta(rho)=0 and where simplicity is
needed. Account for common gamma decay and bounded shifts before
comparing the remaining powers; none is cancelled by assertion here.

Gonek's fixed-beta estimate is uniform in height and needs no
lower estimate for zeta'(rho). The covered asymptotic question allows
an onset depending on delta; it does not demand numerical constants
or any uniform limit as delta tends to zero. One still has to bound
the exact algebraic q_delta/lambda_delta over the stated delta range
well enough for the comparison. This is elementary specialization of
the already defined constants, not a source theorem being assumed.
Retain strict inequality and integer rounding in (7).

Continue only if the assembled lower estimate and verified lambda
bound decide eventual compatibility or its failure. Otherwise report
the remaining exponent or constant gap and stop this test. Failure
of (7) would limit this sufficient threshold only; it would not prove
PSD, exclude smaller witnesses, refute L645 or decide RH.

### Search, overlap and limits

Queries included `Riemann zeta derivative bound sigma greater 1/2 t
convexity derivative uniform strip`, `site:dlmf.nist.gov 5.11.9 gamma
vertical strip`, `site:dlmf.nist.gov zeta Euler Maclaurin 25.2`,
`"xi" "Pick matrix" "growth" pole detection`, and `"zeta" "Pick"
"logarithmic" matrix`. Search snippets were leads only. Gonek's
published equation and proof paragraph and the DLMF statements above
were actually read. No exact detector-height theorem emerged from
this bounded search; no absence or novelty claim follows.

The previously recorded external qualitative Pick material was reused
only through the producing assessment. A new search hit titled
*Pick Kernel Triadic Positivity* was not inspected or imported; it
does not replace a theorem-level growth comparison. Other search
leads on derivative moments, conditional logarithmic derivatives and
extreme values were not imported. A PMC extreme-values page returned
a browser challenge. A shell download of Gonek failed DNS, but the
web reader supplied the relevant published text, so essential source
coverage is not blocked. No claim relies on an unavailable screenshot.

L258 and the fixed-reserve stop were checked as overlap and contrast;
neither resolves this exact test. Mathlib matching coverage for the
new growth inputs was not checked; no absence is claimed. The local
input IDs for the continuation are L018 and L645 only. No
cross-notebook mathematical input or new DAG edge is proposed.
