# Fixed-size shifted zero-moment Hankel: source gate2197

TARGET: Review known eventual-positivity results for the actual shifted zero-moment matrix H_(2,r)=(S_(2r+i+j+2))_(0<=i,j<=2), and decide whether three verified distinct real nodes and a complete absolute tail bound support an explicit finite r_0 with H_(2,r) positive definite for every integer r>=r_0; preserve the unshifted and all-degree gaps.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2198 searched shifted Hankel/zero-power-sum/eventual positivity and meromorphic dominant-pole terminology; inspected primary zero-verification and Vandermonde statements; reused ready finite-matrix and counting assessments; checked L056/L057, C919e/f/g and recorded finite-extrapolation/strip-sign failures. No exact effective shifted actual-Xi theorem was located; this is not evidence of novelty.
SOURCE_EVIDENCE: Platt2017 accepted manuscript Theorem5.1 and Sections4.1-4.2/5, pp6-8; Platt-Trudgian2004.09765v1 Theorem1/Section2, p2; Gautschi1975 Section3(3.1)-(3.4), p339 and Section4(4.1), p340; Bellotti-Wong2412.15470v2 Theorem1.1, p1, with ready Section5/count audit reused; audited C919e/f and L467, with L018/L024/L025/L030 and L058 normalization read.
COMPARISON: Known inputs cover a quantitative head-tail specialization, not its result. C919e/f already supply a qualified three-box head margin at zero time; Platt supplies reality of every additional node through cutoff100. Keep that entire real middle as a nonnegative head instead of requiring an unavailable exact first-three census. C919g already supplies qualified unshifted H2; the new issue is all large shifts, not another unshifted certificate.
GAP: No explicit r_0 or complete shifted tail comparison has been proved. The later fixed-r_0=4 test must bound the whole exterior by L467, track the shifted head weights and prove the comparison for every larger integer. Arithmetic qualifications remain; unshifted all-degree, larger-degree uniformity and RH remain open.
REASON: Reuse established placement, matrix margin and shell counts rather than reprove zeros, quadrature or general asymptotics. One bounded known-method calculation is justified; a fixed-size sign family is not a central creative bridge or progress beyond the inspected methods.
SCOPE: Completed literature-only review2198. The precise later specialization is nominated separately in 2026-11-21-shifted-zero-hankel-tail-test-2198.md for next-turn approval. No lemma, mathematical script, new inequality or shifted positivity result is produced here.
LITERATURE_REASON: This changed zero-power target lacks essential theorem-level coverage; reuse matching coefficient/heat/finite-height assessments after checking their exact scopes.

## Original nomination (historical; completed review below supersedes readiness)

Main gap: L030-L032/C032a actual-Xi all-degree algebraic mixed positivity.
Use beta_j=alpha_j^(-2), S_k=sum_j beta_j^k with L024/L025's exact
conventions and algebraic squares. H_(2,r) is proposed, not asserted
positive; r is a nonnegative integer. The prospective polynomial tests
are restricted to X^r p(X), deg p<=2, leaving arbitrary polynomials
and removal of the shift unresolved.

Essential prospective inputs: L018/L024/L025/L030. A real head requires
a precise cited zero-verification result retaining distinctness,
multiplicities and the complete omitted set. No positive/real residual
nodes, RH, global simplicity or new interchange may be assumed. Three
decimal zero values, an asymptotic without an onset, and sampled positive
matrices do not meet the target.

Continue only if an inspected theorem covers the target or a precise
quantitative specialization has a finite head margin and complete tail
comparison at a stated shift. Reject a duplicate, an unpaid finite
threshold or a restricted sign with no benefit beyond ready coverage.
Check known failures before nominating calculation. No creative attempt
is justified yet. Mathlib matching is unchecked; no cross-notebook input.

## Completed source review2198, 21 November 2026

The exact question in TARGET was reviewed, without deriving a dominance
lemma or calculating a threshold. The main gap is unchanged. The useful
intermediate conclusion would concern only q(X)=X^r p(X), deg p<=2.
No control of arbitrary polynomials follows from an onset depending on
the fixed degree. In particular no shift-removal inference is supplied.

### Actual nodes and primary inputs

L018, L024, L025 and L030 were read in full. Their alpha coordinate is
gamma+i(1/2-Re rho); beta=alpha^(-2), with one occurrence per opposite
pair and multiplicity retained. S_k uses these beta, not ordinates of
unverified zeros. Algebraic squares and ordinary transposes remain.
L058 identifies F(0,z)=Xi(z), so the audited endpoint result C919f at
lambda=0 is in exactly this coordinate. No deformed-family Hadamard
theorem or positive-time propagation is needed for the proposed test.

David J. Platt, *Isolating some non-trivial zeros of zeta*, Mathematics
of Computation86(307) (2017), 2449-2467, DOI10.1090/mcom/3198,
[accepted manuscript](https://research-information.bris.ac.uk/ws/portalfiles/portal/78836669/platt_zeta_submitted.pdf),
Theorem5.1, printed p8 (PDF p9), certifies simplicity and critical-line
location for every nontrivial zero with |Im rho|<=3.0610046*10^10.
Read the theorem, its preceding 103800788359-zero report, and the
completeness/isolation passages in Sections4.1-4.2, pp6-7. The latter
use Turing counting and rigorous evaluations on both sides of each
proposed sign change. Import this published computational theorem;
do not reproduce its computation or presume individual brackets from
the theorem alone. Its symmetric statement also treats height zero;
L024 separately excludes Xi(0)=0. Simplicity is stronger than needed.

Platt and Trudgian, *The Riemann hypothesis is true up to 3 times
10^12*, Bulletin of the London Mathematical Society53 (2021),792-797,
DOI10.1112/blms.12460,
[arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1), Theorem1 and
Section2, printed p2, were inspected for comparison. Their certified
larger window is not high-precision individual isolation; Section2
explicitly says that refinement was omitted. The smaller Platt theorem
already suffices for cutoff100; do not require either new zero data or
an improved zero-free region. The October quasi-RH input is unnecessary
for this target; no parked analytic envelope is being reopened.

C919f's audited statement provides at least one real zero in each of
(14,29/2), (41/2,43/2), (49/2,51/2), including lambda=0, under its
explicit CPython integer/Fraction and Decimal/libmpdec contracts.
The recorded step2169 conceptual audit accepts exactly those signs.
Reuse that result and its ready comparison2168; no evaluator or artifact
replay was performed here. Existence in disjoint boxes is enough for
distinct opposite classes. It is not an exact census of the first three.

C919e's audited closed-box conclusion gives the selected scaled Gram
margin 1/B>1/700000000 for w(x)=(x^(-2),200*x^(-4),40000*x^(-6)).
Read its hypotheses, constants and inverse normalization; reuse the
step2164 audit. Walter Gautschi, *Norm Estimates for Inverses of
Vandermonde Matrices*, Numerische Mathematik23 (1975),337-347,
[author scan](https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/051.pdf),
Section3 (3.1)-(3.4), p339, and Section4 (4.1), p340, were reopened:
nodes must be distinct, inverse rows are Lagrange coefficients, and
the displayed norm is the infinity norm. The proof and positive-ray
equality case were inspected. There is no reason to rederive C919e.

Reuse the finite real SVD/norm, Gram positivity and matrix-order
coverage in comparison2161 and comparison2170: Boyd-Vandenberghe,
*Convex Optimization* (2004), corrected seventh printing2009,
A.1.1 pp633-634, A.1.5 p636, A.5.2 pp646-647, A.5.4 pp648-649,
Sections2.2.5 pp34-35 and8.3.1 p406
[author PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).
Fresh PDF requests timed out; the exact unchanged inspected coverage
is reused, not inferred from an inaccessible page. For a complex
exterior use the ordinary Cauchy-Schwarz inequality on real coefficient
vectors; its algebraic summands need not be positive Gram matrices.

L467's full shell proof and relevant audit passages were read. It gives
18 log(v+2) for every closed positive-height unit shell, counting all
zeros with multiplicity, including both endpoints. Its primary input is
Bellotti-Wong, *Improved estimates for the argument and zero-counting
function of the Riemann zeta-function*,
[2412.15470v2](https://arxiv.org/pdf/2412.15470v2), 7July2025,
Theorem1.1 p1, reopened here. Reuse the exact Section5 pp23-24 and
endpoint/multiplicity coverage in the October25 assessment and L467's
audit. This supplies a complete count input; it is not yet the required
shifted norm bound. No source count or analytic estimate is reproved.

### Overlap, failures and quantitative scope

L056 proves strict Gram positivity for an entirely real comparison
spectrum; it cannot supply signs for Xi's complete complex tail.
L057 and ATTEMPTS/2026-09-09-finite-hankel-extrapolation.md rule out
the generic finite-to-all-degree inference. The separate strip-to-Hankel
failure warns against replacing algebraic squares by modulus squares.
Neither stop prohibits a qualified fixed-degree actual head-tail test.

C919g, including its step2173 audit, already establishes qualified
unshifted H2 over a closed heat band by a signed rectangular exterior.
Thus a new r=0 H2 proof would be overlap, not the intended contribution.
The proposed all-r>=r_0 family uses different polynomial tests and an
absolute exterior estimate. It must not reuse C919g's signed exterior
bound after inserting unbounded powers. The finite-height Laguerre
result L466 and boundary-density minors C466a are different forms;
their statements do not imply these shifted logarithmic moments.
The earlier all-fixed-shift Toeplitz source blocker concerns growing
matrix size, coefficient minors and tied packets, not this fixed-size
zero-power matrix; it need not be reopened.

A head consisting of exactly three occurrences would require a
complete first-three census and separator not imported here. The
source-covered alternative keeps every opposite class with positive
ordinate <=100 as a finite real head, selecting three occurrences
only to pay its margin. The future proof must retain all unselected
real occurrences as nonnegative terms. The entire complement has
ordinate >100 and is estimated absolutely, without assuming RH,
positive residual nodes, an exact low-zero census or global simplicity.
This is a specification for a later specialization, not a derived
inequality or established shifted matrix sign.

No primary theorem inspected directly supplies an effective r_0 for
this normalization. Searches also produced classical Hadamard/qd
meromorphic-pole asymptotics leads (Henrici Section7.5 and
Golub-Meurant), but their full theorems were not retrieved and are not
inputs. They cannot supply an explicit error or onset from a snippet.
LMFDB's source/completeness/reliability pages were read: they describe
Platt's complete list and +/-2^(-102) precision. The four-value endpoint
was inaccessible; no decimal values or raw data were imported. Existing
C919f removes that data dependency, so it is not a persistent blocker.
Other search hits asserting stronger RH criteria or resolutions were
not inspected or used. No absence-of-literature or novelty claim follows.

Queries actually used include `Riemann zeta zeros power sums Hankel
determinants eventual positivity shifted moments`, `Hankel determinants
zeta zeros dominant poles asymptotic positivity`, `"Hankel" "zeros"
"power sums" Riemann positivity`, `"Hankel determinants" "meromorphic"
"poles" Hadamard`, and `Hankel determinants power sums zeros
"eventually" positive`. Narrow local searches compared these with
finite-height, coefficient/Toeplitz, heat-flow and H2 source records.

### Decision and stopping test

Prepare one later known-method test at the fixed proposed onset r_0=4,
cutoff100 and existing scale D, with no cutoff/onset sweep. This integer
is a test specification, not a computed bound or theorem. Establish a
complete absolute tail budget and compare it with the shifted selected
head margin, then justify every larger r. An unmatched endpoint, missing
occurrence, failed threshold or absent monotonic comparison ends this
one certificate without tuning. Success would give a restricted family
of signs only. Full Mathlib matching remains unchecked.

Outcome: EXPLORATION / LITERATURE / NOVELTY_UNCHECKED. Coverage and
overlap are clarified, but no new mathematical advance or negative
certificate is claimed. The next assessment is new and needs separate
approval next turn. A central creative route remains unjustified:
finite-degree large-shift dominance supplies no shift-removal or
degree-uniform mechanism. PROOF and DAG are unchanged.
