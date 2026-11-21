# Interior slope packets for an exact-range point obstruction — source assessment

TARGET: Assess source coverage for an exact-range counterexample to C997c's point inequality using n-dependent interior slope packets with TV=1, |H_n^+(1+i/8)|>=exp(-o(n)), and sup_[15/8,17/8]|H_n^+|<=exp(-sigma*n) for some fixed sigma>0 along an unbounded integer subsequence.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step326 searched exact-range Laguerre localization, Gaussian packets, uniform bulk errors and analytic stationary phase; reused review291's primary Vanlessen assessment and reviews312/318/320/322. No inspected theorem decides the specified packet thresholds; no novelty inference. Queries and unread leads are recorded below.
SOURCE_EVIDENCE: Hitrik–Sjostrand arXiv1508.00649v1 Section2.3, Theorems2.3.1/2.3.3, Lemma2.3.2 and the latter theorem's complete proof, printed pp37-40; DLMF18.12.13,7.7.3,7.12.1 with domains/error qualifications. Reuse review291's inspected Vanlessen Theorem2.4(b), analytic error matrix and bulk proof; C997c(1),(4)-(6), audit322 and L997(4) fix the exact range.
COMPARISON: Known analytic saddle tools supply exponential remainders relative to a paid complex-domain amplitude norm, whereas fixed-order bulk errors do not supply exponential response accuracy. No source realizes the requested TV-normalized slope packets or excludes them. Arbitrary Hardy extremizers and unrelated Laguerre-function packets are insufficient.
GAP: Construct an admissible n-dependent density and prove its complete target lower bound and uniform data upper bound, including analytic-domain norm costs, both Laguerre branches, cutoff/contour boundaries, both short intervals, both beta contributions and K's -1. No rate margin, realization or counterexample is established by this assessment.
REASON: Accessible primary method coverage is adequate for one bounded exact-contour packet test, without importing its desired outcome. Missing packet-specific inequalities are the research target, not an inaccessible theorem premise. No essential source blocker remains; this completed literature-only comparison is EXPLORATION/NOVELTY_UNCHECKED.
LITERATURE_REASON: The n-dependent interior density and exponentially small complete response fall outside the paid Hardy certificate and fixed-bump assessments; analytic localization and its amplitude/cutoff hypotheses require source comparison.
SCOPE: Exactly the finite complex absolutely continuous slope measures, fixed compact interior J, original TV and three asymptotic thresholds specified below. Approves one attempt after the separate next-turn approval; no new mathematics was derived during this review. It does not approve arbitrary Fourier-density realization or n-dependent uses of nonuniform O symbols.
COVERED_TARGET: Test whether n-dependent interior slope packets give an exact-range counterexample to C997c's point inequality, with TV=1, |H_n^+(1+i/8)|>=exp(-o(n)), and sup_[15/8,17/8]|H_n^+|<=exp(-sigma*n) for fixed sigma>0 along an unbounded integer subsequence.

## Exact target and bounded test

Keep the complete C997c(1) integral, n>=2, I=[7/4,9/4],
E=[15/8,17/8], and z_star=1+i/8. The proposed obstruction would use
integers n_j tending to infinity and finite complex measures mu_j with
absolutely continuous, n_j-dependent densities supported in one fixed
compact subinterval J of (7/4,9/4). Require

    ||mu_j||_TV=1,
    |H_(n_j)^+(z_star;mu_j)|>=exp(-a_j), a_j>=0, a_j/n_j -> 0,
    sup_(gamma in E)|H_(n_j)^+(gamma;mu_j)|<=exp(-sigma*n_j),
    sigma>0 fixed.

These are desired thresholds, not asserted estimates. The possibility
of a complex phase matched to an interior Laguerre saddle and an
n-dependent localized amplitude is only a candidate mechanism. No
formula, existence claim or optimization is supplied in step325.
The review must assess whether available primary results justify this
mechanism, exclude it, or leave a sharply bounded research test. Retain
both short intervals, both beta contributions and K's -1, including
original-TV normalization and uniformity in the CLOSED data interval.

Read primary theorem hypotheses and load-bearing cases for the exact
oscillatory regime before longer source passages. Compare potential
uniform asymptotic errors with the exponential data threshold; an
algebraic remainder cannot silently replace an exponentially small
complete response. Arbitrary positive-frequency densities or Hardy
extremizers are insufficient without a proved realization by the stated
mu_j. The old fixed-bump and Chebyshev stops remain evidence, not a
global prohibition on this materially different n-dependent family.

Continue only if coverage supports a concrete construction or an
independently testable obstruction for this packet class. Abandon or
refine the packet class if the source hypotheses cannot control the
complete response at the required scales; do not infer all-measure
impossibility from that failure. No source blocker is currently claimed.

## Relevance and limitations

Main gap: L030-L032/C032a actual-Xi positivity and L966/L968 signed
forcing, with L984(H) unpaid. A valid packet obstruction would settle
whether this particular one-sided point bridge can serve the later
selected-response route. It would refute neither RH nor every possible
bridge from C997c's local branch recovery. It is a proposed exact-range
test, not an excuse to repeat the failed scalar Hardy conversion.

Essential inputs for the source comparison are C997c(1),(4)-(6),
its audit322, L997(4) and C997d's scoped failure; C997a(1)-(2) specify
the later selected-response context, not an assumed identity. Selected
normalization, both-sign transfer, original assay feasibility, actual
reconstruction, signed recovery, infinite-zero complements, regulator
uniformity, L993 and L984(H) remain unresolved. No cross-notebook input.
Matching Mathlib coverage is unchecked. The original step325 nomination
contained no new lemma, proof, source approval, mathematical script or
RH candidate. The separate step326 source assessment follows.

## Completed source comparison — step326, 10 November 2026

One literature-only step completed the unchanged TARGET. The desired
thresholds above remain unproved. No lemma, mathematical script, packet
formula, asymptotic specialization or numerical experiment was produced.
The COVERED_TARGET is a future bounded attempt; this newly ready
continuation receives separate supervisor approval next turn.

### Primary contracts inspected

**Analytic localization.** M. Hitrik and J. Sjostrand,
[*Two minicourses on analytic microlocal analysis*,
arXiv:1508.00649v1, 4 August 2015](https://arxiv.org/pdf/1508.00649v1),
Section2.3, printed pp37-40 (PDF pp37-40). Read Theorems2.3.1/2.3.3,
Lemma2.3.2 and the complete proof of Theorem2.3.3. Theorem2.3.1 gives
a factorial remainder for a Gaussian integral with holomorphic amplitude.
Theorem2.3.3 assumes 0 in V compactly contained in U, holomorphic phi,
phi(0)=phi'(0)=0, nonsingular phi''(0), Re(phi)>=0 on V intersect R^d,
strict positivity on its boundary, and no other critical point there.
For sufficiently large C, truncation at k<=1/(C*h) has remainder

    |R(h)| <= epsilon^(-1)*exp(-epsilon/h)*sup_U|u|, 0<h<=1,

for holomorphic u. Its proof pays cutoff terms near the strictly positive
boundary, deforms the contour to obtain quadratic decay, uses holomorphic
Morse coordinates and reduces to the Gaussian theorem. These are
imported tools, not a packet theorem. Domain/amplitude costs and uniformity
for our n-dependent family and closed E remain to be proved. A compact
cutoff is not a globally holomorphic amplitude; its errors need payment.

**Exact kernel rather than an exponential claim from a bulk O symbol.**
[DLMF18.12.13](https://dlmf.nist.gov/18.12.E13), inspected with |w|<1,
gives the Laguerre generating function. Alpha=2 and degree n+1 are
already specialized in L997(4), including the subtraction (1-w)^(-1).
Reuse that exact identity and named Cauchy coefficient/contour and
finite-measure Fubini theorems. A later deformation must avoid w=1 and
justify every parameter interchange and endpoint; no contour is supplied
or asserted admissible here.

Reuse [review291](2026-11-10-continuous-slope-phase-projection-review-291.md)
for M. Vanlessen,
[*Strong asymptotics of Laguerre-type orthogonal polynomials and
applications in random matrix theory*, math/0504604v2](https://arxiv.org/pdf/math/0504604v2),
Theorem2.4(b)/(2.13), Remarks2.3/2.5, Proposition3.31/Theorem3.32,
Proposition5.1 and Section5.2, printed pp5-7,32-34,39. Its previously
inspected contract covers alpha>-1, polynomial Q with positive leading
coefficient, complex bulk domains, both branches and an analytic error
matrix. Q(x)=x, alpha=2 and degree n+1 remain the same specialization.
The n-dependent slope amplitude and complete-response exponential error
are outside that assessment's established conclusions. The present turn
opened the source's version/abstract only, and does not claim a new full
read of its proof. The earlier adequate theorem assessment is reused.

**Gaussian models and tails.**
[DLMF7.7.3](https://dlmf.nist.gov/7.7.E3) gives the half-line Gaussian
integral with complex linear phase, Re(a)>0, including its Dawson term.
[DLMF7.12.1 and following qualifications](https://dlmf.nist.gov/7.12#i)
give erfc expansions for |arg(z)|<=3*pi/4-delta. In |arg(z)|<=pi/4
the remainder is bounded by the first neglected term; on the positive
axis it has that term's sign. These are optional exact-model/tail tools,
not formulas for a truncated nonlinear packet. Any full-line replacement,
complex contour or cutoff must be paid in the original response.

**Alternative source deliberately not imported.** Dunster–Gil–Segura,
[arXiv:1705.01190v1](https://arxiv.org/pdf/1705.01190v1), opening cases
pp1-3 and Section2 basic domains/remainders pp5-6 were inspected. Case1a
requires alpha comparable to the large parameter, so its displayed
remainder cannot be applied to our fixed alpha=2 by ignoring hypotheses.
Case2 admits a broader alpha range but was not fully inspected. It is an
unused lead, not essential coverage; its numerical error tables are not
an exponential remainder certificate for this assay.

### Scope comparison and the bounded research test

Search found no directly matching construction or all-measure obstruction.
The retrieved Gaussian-beam/optical Laguerre results are not theorem
evidence for this slope-measure range. Epperson's *Hermite and Laguerre
wave packet expansions*, Studia Mathematica126(1997),199-217,
[publisher abstract](https://www.impan.pl/en/publishing-house/journals-and-series/studia-mathematica/all/126/33/110046/hermite-and-laguerre-wave-packet-expansions),
describes finite combinations of Laguerre functions and their decay.
Its full theorem text could not be fetched and is an unread lead; neither
exact-range realization nor an exclusion follows from its abstract.

The exact generating identity and analytic contour tools suffice to
test a proposed interior analytic/Gaussian localization with explicitly
paid cutoff costs. They do not guarantee that any such packet passes.
The attempt must start with a genuine density in c on one fixed compact
J inside I. Arbitrarily prescribing h_U(t) or a Hardy extremizer is not
allowed. Its TV normalization, not a demodulated transform norm, must be
used at every stage. A leading saddle term must have a proved nonzero
coefficient or a justified unbounded subsequence avoiding cancellation.

At the data band E, bounds must hold uniformly up to BOTH endpoints.
A moving phase or contour needs uniform separation, holomorphy and
amplitude bounds; a fixed-phase theorem supplies no automatic uniform
constant for such a family. Any growth of the complex-domain norm in
the displayed theorem must be charged against its exponential remainder.
An analytic error matrix may be kept inside an exact contour argument
only after proving the requisite domain and norm bounds. Integrating an
absolute algebraic bulk error is not an exponential response estimate.
Keeping the exact coefficient representation is an available alternative,
not a representation or contour already established in this turn.

Retain both oscillatory Laguerre branches, both terms of cosh, K's -1 and
both short intervals. C997c(5) already provides a complete lower-band TV
bound; cite it with its hypotheses if used. No new improved bound for
the lower band or the complex target is derived here. The central test
is simultaneous target retention at exp(-o(n)) and absolute data decay
with one fixed sigma>0. Insufficient contour margins stop the chosen
certificate, not all measures or the underlying point inequality.

The materially new mechanism is an n-dependent primal localization in
the original slope variable. L997's fixed bump has an audited endpoint
leak; C997b's prescribed Chebyshev atoms have an audited normalization
cost; trial318's whole-boundary transfer and C997d's Hardy scalar
conversion miss their rate requirements. None covers this density
family. Existing stops293/316, audit317 and trials314/315/318 are
preserved. This assessment does not reopen their certificates or reset
an exploration budget. Selected-response normalization remains separate
because of C997a(8), even if this one-sided point test succeeds.

### Search, access and decision record

Queries included `Laguerre polynomials uniform asymptotic expansions
large n fixed alpha oscillatory region exponential error steepest descent`,
`Laguerre functions wave packets analytic localization exponential
stationary phase compact support`, `"Laguerre" "Gaussian wave packets"
exponential`, `"Laguerre" "analytic stationary phase"`,
`"analytic stationary phase" "exponentially" theorem pdf Sjostrand`,
`Hitrik Sjostrand Two minicourses analytic microlocal analysis pdf theorem
2.3.4`, and `Epperson Hermite Laguerre wave packet expansions 1998 pdf`.
The primary PDF's relevant theorem is 2.3.3, not the searched 2.3.4;
Epperson's publisher identifies 1997, correcting the search metadata.
Source text, not a search snippet, supplies the imported contracts.

Hitrik–Sjostrand v1 was fully accessible in the relevant section. The
original Sjostrand Astérisque95 PDF exceeded the web tool's size limit;
it is not needed in addition to the inspected same-author theorem and
proof. Epperson's EU-DML/publisher downloads returned403; this unused
lead is not a persistent essential source blocker. Some DLMF TeX query
URLs failed; the displayed equations and their qualifications were read
successfully. No API key, cross-notebook input or shared edit was used.

EXPLORE: approve a single future exact-range packet attempt after the
separate approval of this newly written ready continuation. Continue on
the three rigorously simultaneous thresholds, or a concrete partial
representation with a new discriminating bound. Preserve an incomplete
construction if a contour/amplitude/cancellation margin is unpaid.
Abandon or refine the particular packet class on a proved incompatible
threshold; a failed upper estimate alone is inconclusive. This review
establishes source readiness only, not a mathematical advance or an RH
candidate. Mathlib full matching coverage remains unchecked and unknown.
