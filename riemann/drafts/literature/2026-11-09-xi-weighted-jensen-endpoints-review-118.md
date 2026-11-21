# Actual-Xi weighted-displacement source review

TARGET: Review unconditional weighted horizontal zero-displacement estimates for actual Xi as a possible source of unbounded Jensen-disk-free real endpoints, with exact constants, interval losses and applicability.
CHECKED: 2026-11-09
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step119 searched horizontal distances, Jensen disks, Selberg density and mollified second moments; reused the November1 charged-block comparison and October11 Young coverage, then inspected the primary passages below. No matching endpoint theorem was located in this bounded search; no novelty inference.
SOURCE_EVIDENCE: Simonic arXiv:1910.08274v2 Theorem1 pp1–2, Section4.2 pp29–30 and Section4.5 pp33–34; Young, Arch.Math.95(2010),539–548, definitions/Theorems1–2 pp539–541, Lemma3/(3.1)–(3.3) p541 and zero-shift extension pp544–545; Najnudel–Nikeghbali arXiv:2609.15862v1 Theorem1.1 p1 and Lemma8.4/proof p21. Exact versions, links and limits below; Kim's unchanged coverage is reused.
COMPARISON: Explicit density and the newer horizontal-moment lemma give O(T) without a sufficient small coefficient. Young supplies an unconditional exact mollified moment with numerical main-term formula, a distinct input for a later Littlewood/endpoint specialization. None of these statements is itself a Jensen-endpoint theorem.
GAP: Prove the transfer for a different mollifier, including boundary arguments, zero multiplicities, smoothing losses, critical-line logarithms and padded closed intervals. The proposed coefficient and endpoint conclusion remain unproved locally; actual-Xi critical counts and mixed signs remain open.
REASON: Source discovery changes the decision from unspecified O(T) density to a concrete known-moment specialization. Park density-only direct import; prepare one separately approved mathematical transfer test without deriving it in this literature turn.
SCOPE: Unconditional results for actual zeta zeros and Xi's real-axis coordinate; distinguish all zeros from nonreal conjugate pairs and horizontal displacement in the zeta plane from imaginary displacement in the Xi plane. Review sources only until an exact mathematical target has separate ready coverage.

## Original registration (historical; completed review below)

Main gap remains L030–L032/C032a actual-Xi all-degree mixed positivity.
The intermediate question is whether published weighted-displacement
control actually pays Kim's endpoint premise. Such control would make
his conditional critical-count interface usable at unbounded heights;
it would still leave critical-zero estimates, global transfer and mixed
signs unresolved. No such control is claimed here.

Start with the canonical audited L956 and the completed Kim source
assessment `2026-11-09-xi-first-derivative-critical-count-scope-114.md`.
Search exact weighted-horizontal-displacement terminology, stronger
distribution results and endpoint obstructions. Inspect primary theorem
hypotheses and the necessary proof cases before deciding whether any
bound is adequate. Record the actual and required thresholds, including
any strict inequality, without treating an unspecified O(T) bound or a
zero-density statement as an endpoint certificate. If a proposed source
uses the October2026 zero-free input, first read the baseline assessment
and external-input register required by GOAL.md; do not reconstruct it.

Continue only if inspected theorems give a concrete, independently
testable quantitative target or a cited endpoint theorem. If they give
only insufficient bounds, record that mismatch and park this mechanism;
do not repeat the strip countermodel or a source-approval loop. An
access blocker must be recorded explicitly and dependent mathematics
parked. No new mathematics is performed in registering this question.
No Mathlib matching theorem is identified; coverage remains unknown.

LITERATURE_REASON: The next target adds an actual-Xi quantitative
weighted-displacement hypothesis outside the ready L956 audit scope;
its essential primary theorem coverage has not been obtained. A
literature-only turn is required before any dependent calculation.

## Completed bounded comparison — step119

Main gap: L030–L032/C032a actual-Xi all-degree mixed positivity. The
intermediate question is the exact TARGET, with possible downstream use
in Kim's conditional count theorem. Continue only for an inspected
small-coefficient input or a concrete separately testable specialization;
an unspecified O(T) estimate parks direct import. Critical-count
estimates, global transfer and mixed signs remain independent gaps.

Read L956's countercertificate, L018's zero correspondence, step114's
Kim passages and the November1 charged-block assessment/failure.
L612's abstract positive-linear-measure obstruction concerns a sublinear
union target; it does not settle actual endpoints or a strict coefficient
threshold. October11's complete-mollified-mean audit assessment already
inspected Young for a different observable. Reuse it without importing
Wronskian/modified-response claims. Scoped Kim/mollifier records yielded
no duplicate of this endpoint specialization.

### Inspected primary statements

Aleksander Simonic, *Explicit zero density estimate for the Riemann
zeta-function near the critical line*,
[arXiv:1910.08274v2](https://arxiv.org/pdf/1910.08274v2),
29 November2019, Theorem1 pp1–2: for T>=H0=3.0610046*10^10 and
1/2<=sigma<=0.831,

    N(sigma,2T)-N(sigma,T)
      <=10395.2 T^(1-(sigma-1/2)/4) log T
        +1.104 log²T+0.173 log T log log T+0.51 log T.

N uses beta>sigma and 0<gamma<=T. Section4.2 states Littlewood's
rectangle identity for f holomorphic near the closed rectangle, with no
boundary zeros: it retains both vertical log integrals and both horizontal
argument integrals. Its product application retains nonnegative zero
orders and multiplicities. Read that section and Section4.5's microscopic
and continuity cases. At sigma=1/2, (74) has leading coefficient
2e²/pi+alpha(T0), with alpha defined there, and logarithmic remainders.
This coefficient already exceeds the desired 1/2 dyadic displacement
threshold. The improved high-onset density constant5.357 in (5) is not
itself a sufficient first-moment bound. An upper bound missing a threshold
is no lower bound on Xi's actual union.

Joseph Najnudel and Ashkan Nikeghbali, *Cauchy laws for zeta logarithmic
derivatives and stationary Stieltjes transforms*,
[arXiv:2609.15862v1](https://arxiv.org/pdf/2609.15862v1),
14 September2026, Theorem1.1 p1 and Lemma8.4 with complete proof p21:
for each fixed q>0,

    sum_{0<gamma<=2T, beta>1/2} m(rho)(beta-1/2)^q
      <<_q T(log T)^(1-q).

Its exponential tail has unspecified absolute constants c,C>0. At q=1
this is O(T). Theorem1.1 assumes H(T)=o(T) for its actual logarithmic-
derivative transfer; its unconditional projected Cauchy limit does not
remove that hypothesis. The full Cauchy theorem proof is not imported.

Matthew P. Young, *A short proof of Levinson's theorem*, Arch.Math.
**95**(2010),539–548, DOI
[10.1007/s00013-010-0199-9](https://doi.org/10.1007/s00013-010-0199-9),
[published PDF](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf).
Compared published statements with
[arXiv:1002.4403v1](https://arxiv.org/pdf/1002.4403v1).
Definitions pp539–540: L=log S, M=S^theta, 0<theta<1/2, real polynomial
P with P(0)=0,P(1)=1; sigma0=1/2-R/L and

    psi(s)=sum_{h<=M} mu(h) h^(-s-1/2+sigma0)
                  P(log(M/h)/log M).

For smooth w with 0<=w<=1, support in [S/4,2S], and
w^(j)<<_j(S/log S)^(-j), Lemma3 p541, (3.1)–(3.3), states

    I(alpha,beta)=integral_R w(t) zeta(1/2+alpha+it)
                    zeta(1/2+beta-it)|psi(sigma0+it)|² dt
                =c(alpha,beta) integral_R w(t)dt+O(S/log S),
    c(alpha,beta)=1+(1/theta) partial_x partial_y [
       M^(-beta*x-alpha*y) integral_0^1 integral_0^1
       S^(-v*(alpha+beta))P(x+u)P(y+u) du dv ]_{x=y=0},

uniformly for complex alpha,beta=O(1/log S). Section2 explains smooth
upper/lower envelopes for sharp half-dyadic intervals, losing O(S/log S)
in mass. Section5's end, pp544–545, explicitly extends the error to
alpha+beta=0 by holomorphy/maximum modulus after combining the two
diagonals. Thus Lemma3 covers zero shifts; its separate singular Lemma6
terms must not be evaluated there. These statements, smoothing and that
extension were read. Reuse October11's remaining proof-case coverage;
there is no reason to reprove Young's arithmetic theorem here.

### Applicability test still to do

L018 uses z=gamma+i(1/2-beta). One right-off-line zeta zero represents
one Xi nonreal conjugate pair with equal multiplicity. Kim's disk cuts
the real axis in [gamma-d,gamma+d], d=beta-1/2. The proposed target is

    W_T=sum_{T-1<=gamma<=2T+1, beta>1/2} m(rho)d <= T/4

eventually. Compare against the strict coverage budget 2W_T<T. These
are requested thresholds, not established estimates. The later proof
must justify all intersecting disks, conjugate-pair factors and padding.
Coincident intervals may be overcounted; source multiplicities cannot be
dropped. Critical-line zeros supply no nonreal Jensen disk.

The concrete lead is Young's lemma at theta=1/4, P(u)=u and zero shifts,
followed by Littlewood for zeta times that linear mollifier. The candidate
coefficient to test is log(5)/(4pi), including padding and every boundary
loss; it is not derived here. Do not take an unproved R-to-zero limit of
Theorem1, apply Simonic's optimized-mollifier argument estimates to a
different mollifier, discard mollifier zeros, or assume critical-line log
integrability. Positive-height rectangles avoid the pole at1; boundary
zeros still need a justified limit. Standard Jensen/argument-principle
tools are available; their applicability/error bounds for this F remain
the substantive specialization, rather than missing source statements.

Continue only if that later attempt proves a strict budget with all errors
o(T) and the closed-disk conclusion. Otherwise name the failed transfer
step and park the specialization. Endpoints alone supply neither critical
counts nor actual-Xi mixed signs, and do not resolve RH.

### Search/access qualifications and outcome

Queries included `Riemann zeta sum beta minus 1/2 zeros Selberg explicit
bound Jensen disks`, `Jensen discs xi zeta`, `sum of distances zeros
critical line unconditional`, `zeta Littlewood mollifier 1/2 Selberg
moment`, and Young's exact title. The September2026 result is a relevant
new lead, not evidence of a new endpoint theorem. Located the Dong–
Wattanawanichkul–Zaharescu derivative-polynomial article; its HTML omits
essential formulas and flags a corrigendum. Neither it nor its unread
correction is imported. Conrey AIM PDF links returned404 and are unused;
Young's published PDF is accessible. Simonic screenshots failed; actual
equation text and prior complete primary reading supplied the evidence.
No essential access blocker remains for the nominated transfer. Full
or supporting Mathlib endpoint coverage is not checked/unknown.

Outcome: ADVANCE / LITERATURE / NOVELTY_UNCHECKED: local source coverage
advances through an inspected known moment input, without a new
mathematical result or endpoint certificate. The separate continuation
assessment records exactly one specialization for next-turn approval.
No lemma, mathematical script, DAG or PROOF changes were made.
