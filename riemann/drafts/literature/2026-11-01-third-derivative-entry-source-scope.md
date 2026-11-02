# Third-derivative entering-block estimate — completed source comparison

TARGET: Assess the explicit third-derivative exponential-sum theorem and its proof cases for C499d's whole moving-cutoff block, retaining Abel weights and both charges, and specify one bounded test of the strict r0 budget.
CHECKED: 2026-11-01
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready uniform-resonant/Abel assessment and searched the named heat, entry-literature and November 1 failure/history paths for third-derivative duplicates. External exact-title/number searches led to Arias de Reyna v1; compared HPY v1 Lemmas 2.4–2.6 and newly read its Section 6. Exact queries and inspected scope are below; no novelty inference follows.
SOURCE_EVIDENCE: Arias de Reyna arXiv:2407.02094v1, Sections 3–5: complete Lemma 6/Theorem 7 proofs, Lemmas 8–10, Theorem 11 (15)–(17), complete proof including Claims 1–3, and Remarks 12–14; PDF pp.5–14, theorem pp.10–13. HPY arXiv:2207.02366v1 Lemmas 2.4–2.6 and complete Section 6; reuse prior complete Sections 4–5 coverage. No source audit or numerical application is claimed.
COMPARISON: The explicit d=3 theorem and its finite-parameter differencing proof have effective constants and no first-derivative resonance exclusion. The earlier positive-curvature split is unnecessary only if the new derivative hypotheses are proved. The optimized constants may be too coarse; a source-supported finite-parameter screen is specified, without claiming a saving. HPY's logarithmic specialization is not silently transferred to the quadratically modified phase or arbitrary translated intervals.
GAP: Actual-phase derivative/sign/range specialization, the bounded prefix calculation, Abel reconstruction and the strict r0 comparison remain unperformed. No uniform exclusion, actual lower bound on the increment, complexity guarantee or central sign theorem is established.
REASON: Source coverage now supports exactly one capped known-method calculation with a different derivative/differencing estimator, after separate supervisor approval of this changed assessment. Preserve the quadratic and capped-spatial stops; do not rerun either estimator.
LITERATURE_REASON: The d>=3 proof and its effective prefix interface were expressly outside the earlier ready quadratic scope. This changed input needs coverage before calculation; it is not extra literature on an unchanged ready target.
SCOPE: Exact C499d interval, t=.16836, X=6000284561421.5, n=691004, N=691260, Y=4*pi*(N^2-t/16), canonical q(x), actual phase, L495 resultant, all Euler channels, L494 full epsilon_1 and both charges. Source-supported specialization only; no cross-notebook input. Mathlib coverage unchecked.
COVERED_TARGET: Test C499d's whole moving-cutoff interval using Arias de Reyna's d=3 theorem and finite single-difference prefix bounds, with Abel weights and both charges, under a fixed 2^25-operation cap, requiring total cost<r0.

## Completed review — 1 November 2026

This review is literature-only, with outcome EXPLORATION: new actionable
source scope, no mathematical estimate or advance beyond inspected sources.
The original nomination below records the starting scope; its pending
language is historical. The SPECIALIZE decision covers only the exact
COVERED_TARGET above. Newly written coverage needs a separate approval
next turn before a research invocation. No calculation is performed here.

### Primary theorem and essential proof cases

J. Arias de Reyna, *Explicit van der Corput's d-th derivative estimate*,
[arXiv:2407.02094v1, 2 July 2024, Sections 3–5](https://arxiv.org/html/2407.02094v1#S5),
Theorem 11, (15)–(16), PDF pp.10–11, assumes a real C^d phase on
(b,b+L], integer d>=3, floor(L)>d, and
0<lambda<=f^(d)<=Lambda throughout. With D=2^d it bounds

    |L^(-1) sum_(b<j<=b+L) e(f(j))|
      <= max{A_d*(Lambda/(lambda*L))^(2/D),
             B_d*(Lambda^2/lambda)^(1/(D-2)),
             C_d*(lambda*L^d)^(-2/D)},
    e(v)=exp(2*pi*i*v),
    A=2*(1+sqrt(1+3*pi/8))/sqrt(pi), B=2+2*sqrt(2),
    A_d=B*sqrt(2)*(d-2)^(2/D),
    B_d=B*((81/8)*(2/3)^(2*d)*2^(D/4)*A^2/B^2)^(1/(D-2)),
    C_d=B*(A*D/B)^(4/D)*(d-2)^(2*(d-2)/D).

For d=3, Table 1 lists upper bounds 6.829, 4.971, 10.389.
Use exact formulas, not rounded entries as equalities or lower bounds.
No separation of f' from integers is assumed. Theorem 11 is an
unweighted bound; source Proposition 15 concerns a different long-block
zeta-sum supremum and supplies no short-block weighted numerical result.

The full proof, pp.11–13, was inspected: difference domains and integral
derivatives; residual lengths at least d-2; Lemma 5; Claims 1–3's small
parameter, integer rounding and minimization cases; final constant
comparisons. Lemmas 8–9 and Theorem 7's induction were read. This is
scope extraction, not an independent correctness audit or a reproof.

Before optimization, [Theorem 7, (8), PDF pp.7–8](https://arxiv.org/html/2407.02094v1#S4)
provides, for any real phase and natural H<=L, the single-difference
interface

    |E(f)| <= B*max{H^(-1/2), B^(-1/2)*T_1^(1/2)},
    E(f)=L^(-1)*sum_(b<j<=b+L) e(f(j)),
    T_1=(L*H)^(-1)*sum_(a=1)^(H-1)
               |sum_(b<j<=b+L-a) e(f(j+a)-f(j))|.

It retains a finite parameter that Theorem 11 eliminates. Its actual
shift lengths and endpoint convention must be preserved. The source's
Lemma 5, already covered by the ready assessment, applies to each
difference only after its positive lower/upper second derivatives and
length>=1 are verified. The integral formula (6) and Theorem 11's proof
give that interface; they do not verify our actual-phase bounds.
Using the max/absolute version above avoids relying on a signed
correlation as though it were nonnegative. No new differencing inequality
is proposed, and no attempt to improve the author's constants is covered.

Theorem 11 does not cover integer lengths 0–3. Empty sums and absolute
finite bounds cover those lengths. For the finite-parameter test H=1
has an empty shift sum; H<=L ensures each nonempty shifted length
L-a>=1. Negative derivatives require an explicit conjugation application
in the research step. A lower bound of zero, an uncovered sign change
or a failed domain check must never be passed to Lemma 5.

### Stronger logarithmic comparison and its scope qualification

Hiary–Patel–Yang, *An improved explicit estimate for zeta(1/2+it)*,
[arXiv:2207.02366v1, 6 July 2022, Lemmas 2.4–2.6 and Section 6](https://arxiv.org/html/2207.02366v1#S6),
has a more tailored third-derivative estimate. Its phase is
f(v)=T*log(r*K+v)/(2*pi), with positive integers r,K,
K>=K0>1, T>0, and W=pi*(r+1)^3*K^3/T,
lambda=(r+1)^3/r^3. For positive integer length<=K and eta>0,
Lemma 2.6's squared bound is

    (K/W^(1/3)+eta)*(alpha*K+beta*W^(2/3)),
    mu=(lambda^(2/3)/2)*(1+1/((1-1/K0)*lambda^(1/3))),
    alpha=1/eta+eta*mu/(3*W^(1/3))+mu/(3*W^(2/3))
                      +32*mu*sqrt(eta+W^(-1/3))/(15*sqrt(pi)),
    beta=32/(3*sqrt(pi*eta))+(2-4/pi)*W^(-1/3).

Newly read Section 6 keeps the differencing parameter's ceiling and
the boundary constant 2-4/pi; its dependence on Lemma 2.5's full
resonant/endpoint proof is covered by the prior assessment. The statement
mentions every integer starting N, but the supporting derivative and
Lemma 2.5 proof ranges are tied to the displayed rK block. No unrestricted
translation is imported here. Applying it to a different start or to
C499d's modified phase would require additional justification. We do
not assert the source theorem false, or infer that all sharper estimates
fail. This review uses the general Arias interface for the bounded test;
HPY supplies a qualified comparison, not a second calculation target.

The older incorrect Kusmin–Landau constant is not used. Yang's 2024
JMAA article (Arias reference [15]) and the general-phase tests mentioned
in HPY remain optional unread leads, not assessed coverage or essential
inputs for the single finite test below. No novelty claim is made.

### One bounded mathematical test, after approval

Keep the exact C499d n,N,X,Y,t and its closed-domain/canonical-floor
conventions. Use its actual reduced phase f_x from Section 1 or its
conjugate; establish every derivative hypothesis before invocation.
First screen the d=3 theorem using its exact constants on all needed
prefix lengths 4–256, retaining trivial caps. This screen may show
that the optimized theorem is too coarse. Do not drop an unfavorable
term from its maximum or present an upper bound as a true-cost lower bound.

For the one finite-parameter variant use a single rigorously justified
derivative range uniform in x in [X,Y] and in the j-domain (n,N].
For every prefix length L=1,...,256 and H=1,...,L, bound every shifted
sum in T_1 by the cited Lemma 5 or its finite absolute cap. Obtain the
shift derivative ranges from the cited integral representation with
all arguments inside (n,n+L]; derive the actual derivative formulas
only in that later research step. The unshifted short prefixes retain
their absolute caps. Minimize the cited upper bounds over this finite
H list, then retain a uniform all-prefix cap for Abel weighting.
Store complete operands and rows; no spatial sample stands for [X,Y].

This uses one global derivative enclosure, not a search over new
spatial partitions. The already proved floor-cell partition in C499d
handles x=X, entry equalities and Y; the prefix range covers every
q(x). No larger block, adjacent endpoint, altered prime set or spatial
Taylor replay is included. Permit at most 2^25 scalar enclosure
operations cumulatively, including one precision refinement only if
enclosure width prevents a decision. Record exhaustion honestly; no
complexity guarantee is inferred from a theorem. Retain full certificates
on disk and print only bounds, thresholds, failures and paths.

C499d Sections 3–4 supply the already justified positive decreasing
heat/logarithmic weights, full finite resultant reconstruction, old-model
reserve and independently uniform two-charge envelopes. Apply the new
prefix caps to those weights via the ready Abel interface; prove any
changed cap or charge before using it. Keep the actual nu, ell, Euler
product, all squarefree channels, conjugate terms, both saddle
corrections and the full epsilon_1 entering-pair/Cauchy allowance.
No derivative of q, unsigned replacement of the resultant, endpoint
interpolation, fall credit or assumed phase separation is allowed.

The single decisive comparison is B_unif+U_s,unif+U_r,unif<r0 on
the entire interval. A certified success provides a qualified finite
positive-time exclusion input only. Adequate-precision failure or the
fixed cap parks this specified third-derivative/difference envelope;
precision, H-range or spatial sweep expansion is not its continuation.
It leaves all-height signs, later intervals/times, H1, zero time and
the imported manuscript audits open. A useful negative would identify
which source bound or Abel/resultant cost prevents this sufficient test.

### Reuse, duplicate check, provenance and Mathlib

Read C499d in full, C499c Sections 1–4, L494/L496/L499's exact
hypotheses/interfaces and L495's definitions/charges. Reuse the ready
uniform-resonant assessment for Abel, complete Lemmas 4–5 and the
already inspected HPY endpoint cases. Both named ATTEMPTS records
were read in full: the quadratic/absolute-tail stop and capped spatial
signed-enclosure failure. They remain estimator-specific stops, not
global bans. Narrow searches in named heat, entry-literature and November
1 history/failure paths found the nomination and the excluded Theorem 11
lead, not a completed third-derivative entry certificate. Older fixed-
frequency arithmetic derivative notes concern a different target and
were not loaded as mathematical inputs. No cross-notebook read occurred.

External queries: `"2407.02094" "third" derivative` and
`"Explicit van der Corput" "Theorem 11"`; then the primary HTML,
PDF and arXiv version record were opened directly. The record lists
v1 dated 2 July 2024; theorem formulas and the essential proof cases
were read as primary content, not inferred from search results.
The HPY primary comparison followed the already named ready assessment.
Source access succeeded; no persistent source blocker is present.

Full matching Mathlib coverage of these effective tests and this
weighted heat application is unchecked. No absence claim or formalization
is inferred. This is a routine finite specialization, not a new creative
central-gap mechanism. Independent actual-kernel/all-height transfer
data is still missing; that blocks justified creative routing here.

## Original nomination — retained historical scope

Essential canonical inputs for a later attempt are L494/L495/L496/L499
and C499c/C499d with their retained saddle/base-phase manuscript
qualifications. The read C499d statement and reduced-phase setup fix
f_x(u)=-a_x log u-u(u-1)/2 and the exact integer-phase equivalence;
do not replace the actual complex resultant by an unsigned primitive sum.
No derivative of the floor q is permitted. No new derivative formula
or estimate has been derived in this nomination.

The main gap is still all-height actual-Xi signs and collision exclusion.
A successful intermediate bound could extend one qualified finite
spatial comparison at one positive time. Later intervals, other times,
H1, zero time and manuscript audits remain independent. This finite
known-method target is not a creative central-gap mechanism.

Reuse C499d's canonical bounds: its sufficient total is between
.00072254689054510978 and .00072254689054510979, while
r0<.000422493815870544. These compare upper-bound formulas and do not
lower-bound the true increment. The separate capped spatial enclosure
stopped at cutoff 691087 before N=691260; its ledger check was not an
independent mathematical audit. Preserve both ATTEMPTS records.

Continuation test: source approval requires a completely explicit
finite prefix procedure with all missing short/resonant cases charged,
valid variation/Abel control and a fixed finite partition/resource plan
that can test B_unif+U_s,unif+U_r,unif<r0 over the entire prescribed
interval. A theorem with unusable implicit constants, uncovered endpoint
cases or no genuinely changed estimator does not pass. Park this proposal
if coverage or the bounded plan fails; do not run a larger spatial sweep
or infer success from isolated phase samples. The next source review may
reject this lead without producing a lemma or a calculation.
