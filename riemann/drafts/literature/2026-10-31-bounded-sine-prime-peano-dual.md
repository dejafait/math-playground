# Bounded sine prime probe: completed source comparison

TARGET: Assess source coverage for a bounded sine of L574's prime-block probe as a Peano dual for L477's complete residual.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed the bounded exact-weight, weighted-prime-moment, truncated-exponential and twisted-second-moment searches below; checked L482/L319 and the constructive-linear-dual stop. No matching theorem for both proposed bounds was identified; no novelty inference.
SOURCE_EVIDENCE: Reuse L574/C481a/C574a and the density-Peano stationary-tool assessment. Inspected Curran 2303.10123v2 Lemmas 2.2--2.5; Fazzari 1912.08127v2 Theorem 1.1, Propositions 1.1/1.2, Lemma 2.1 and Section 3.1; Bettin--Chandee--Radziwill author PDF Theorem 1, pp. 1--2; Gonek Invent. Math. 75 (1984), Lemmas 1--3 and proof cases, pp. 129--130, with Banks 2405.11084v1 Lemma 2.8 for readable endpoint notation; DLMF 4.19.1. Precise hypotheses, imports and limits below.
COMPARISON: Finite mean square and endpoint-uniform logarithmic stationary phase support a bounded first-order Taylor budget test. Full-zeta distribution/twisted-moment results do not supply the finite-density sine moment or complete chirp leakage. Stationary main terms survive; none may be discarded. L482 does not apply to this weighted approximation problem.
GAP: Establish or fail the first-order sine truncation's two actual weighted remainder budgets, grouped coefficient lengths/norms, complete chirp stationary sum and endpoints, and the signed Peano transfer; compare with the unchanged a T log T and (a/2)T(log T)^3 thresholds. No desired bound is imported or derived.
REASON: Essential primary scope is available for one independently testable finite implementation, with failure allowed. EXPLORE approves a hypothesis-and-loss calculation, not cancellation or a result; the supervisor separately approves the changed ready continuation next turn.
LITERATURE_REASON: The changed sine amplitude needs density-weighted nonlinear remainder and mixed-prime endpoint coverage absent from the ready quotient assessment; this turn reads those essential comparisons rather than repeating the old source search.
SCOPE: Arbitrary sufficiently large real T, fixed M=floor(sqrt(T/(2pi))), h=1/log T, J=[T+h,2T-h], complete L477 residual and L574's entire prime block T^(1/16)<p<=T^(1/8). No moving cutoff, independent phases, Haar replacement, quotient decorrelation, discarded stationary terms or assumed approximation error.
COVERED_TARGET: Test the first-order Taylor implementation of the bounded sine prime Peano dual, retaining both weighted remainders and all complete-chirp stationary terms.

## Original nomination, preserved; review status superseded above

The following was an uncovered proposal, not a result.
The main gap remains actual-Xi positivity. A full-scale residual lower
bound would obstruct the selected little-o fixed-square defect route;
it would not settle either negative-mass or Xi-sign questions.

Keep precisely L574's P_T(t)=-Re sum_(T^(1/16)<p<=T^(1/8))p^(-1/2-it).
For a fixed positive epsilon independent of T, propose

    b_epsilon(t)=sin(epsilon P_T(t)),
    psi_epsilon(x)=-h^(-2) integral_J (h-|x-t|)_+ b_epsilon(t)dt.

The mathematical target to be assessed, not derived here, asks whether
some absolute epsilon,a>0 admit both eventual bounds

    integral_J D_h(t)b_epsilon(t)dt >= a T log T,
    |integral_T^(2T) V_T(x)psi_epsilon(x)dx|
                                    <=(a/2)T(log T)^3.

A source comparison must separately assess the signed moment and the
complete chirp pairing. L574's result for P_T or D_h/Q_T cannot be
substituted for either bound. Finite prime-polynomial expansion is a
proposed technique: its truncation error must be controlled against the
actual densities and chirp, with product lengths, repeated primes and
every stationary/boundary contribution retained. An ordinary unweighted
Taylor approximation, linear-frequency theorem or formal diagonal is
not adequate coverage. No finite truncation degree or useful remainder
estimate has been selected or proved in this nomination.

Essential inputs to a future attempt are L477, C481a, L574 and C574a's
verified transfer interface and derivative stop. Before approving a
calculation, compare L482's global polynomial-saturation obstruction,
the constructive-linear-dual source stop, and L319's stationary
involution stop in their exact hypotheses. A bounded sine is a changed
multiplier, not an exemption from any applicable obstruction. The
existing quotient source review need not be repeated.

Continue only if primary statements and essential proof cases give a
concrete finite test for both losses, or an EXPLORE assessment identifies
the exact remaining calculable difference without assuming cancellation.
If the expansion cost or stationary main terms are already obstructed,
park this nomination and select an independent target. The question
whether the combined bounds hold is open; no novelty is asserted.
Source proofs and full/supporting Mathlib coverage remain unchecked.
No cross-notebook mathematical input is proposed.

## Completed comparison, 31 October 2026

This literature-only turn retains both displayed target bounds. It
does not prove the signed sine moment, the smoothing transfer for this
amplitude, or a chirp estimate. No lemma or mathematical script changed.
The intermediate target remains a concrete bounded dual for the complete
residual. Its downstream use is an obstruction to the fixed-square
little-o defect route; actual-Xi positivity, both defect thresholds and
negative-mass saving remain independent gaps.

### Primary theorem scope

**Finite moments.** Michael J. Curran, *Correlations of the Riemann
zeta function*, arXiv:2303.10123v2 (15 May 2024),
[Section 2, Lemmas 2.2--2.5](https://arxiv.org/html/2303.10123v2#S2).
Lemma 2.3 allows arbitrary finite complex coefficients and error
O(N sum|a_n|^2), as already imported and interval-translated in L574.
Lemma 2.5 bounds the 2r-th prime-polynomial moment by
O(T r! (sum|a_p|^2)^r), assuming N^r<=T/log T and r natural.
It is unweighted. Lemma 2.4 requires disjoint prime supports;
the density polynomial does not meet that splitting hypothesis.
Lemma 2.2's truncated exponential comparison requires its specified
good set and parameters. Neither result controls a discarded bad set
against the present densities or chirp. Use Lemma 2.3 after grouping;
do not substitute prime-only moments for weighted ones. These are
supporting imports, not matching sine theorems; source proofs unaudited.

**Weighted distribution comparison.** Alessandro Fazzari,
*A weighted central limit theorem for log|zeta(1/2+it)|*,
[arXiv:1912.08127v2](https://arxiv.org/html/1912.08127v2),
Theorem 1.1, Propositions 1.1/1.2, Lemma 2.1 and Section 3.1.
The log-zeta approximation and main CLT assume RH. Proposition 1.2's
prime-polynomial moment statement is unconditional, uses full
|zeta|^2 dt, and has x=T^(epsilon/k), epsilon=1/log log log T,
fixed integer k, and centering by sum_(p<=x)1/p. Lemma 2.1 assumes
a(n),b(m)<<n^delta,m^delta for every delta>0 and length exponents
theta+2sigma<1, again with a full-zeta factor. Section 3.1 expands
mixed prime moments using that interface. These hypotheses and weights
do not match the fixed block or shifted finite densities here.
No CLT, RH-dependent approximation, or independence is imported.
The remainder of its combinatorial proof was not audited or imported.

**Stronger twisted moments.** Sandro Bettin, Vorrapan Chandee and
Maksym Radziwill, *The mean square of the product of the Riemann
zeta-function with Dirichlet polynomials*,
[author PDF, Theorem 1, pp. 1--2](https://www.math.mcgill.ca/radziwill/BCR.pdf#page=2),
identified by [arXiv:1411.7764v1](https://arxiv.org/abs/1411.7764v1).
For A(s)=sum_(n<=N)a_n n^(-s), a_n<<n^delta for every delta>0,
N=T^theta and theta<17/33, the theorem evaluates
integral |zeta A|^2 phi(t/T)dt for smooth phi supported in [1,2].
Its error is O(T^(3/20+delta)N^(33/20)+T^(1/3+delta)).
The gcd/lcm main term is retained by the source. This stronger length
range does not replace full zeta by the sharp finite polynomial,
remove smoothing, or produce the proposed bounded multiplier.
No specialization or source-proof audit is made here.

**Endpoint-uniform logarithmic saddle.** S. M. Gonek, *Mean values
of the Riemann zeta-function and its derivatives*, Inventiones
Mathematicae 75 (1984), 123--141,
[Lemmas 1--3, pp. 129--130](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=7).
Lemma 2, for fixed sigma, large A, A<B<=2A and r>0, states

    integral_A^B exp(it log(t/(r e))) (t/(2pi))^(sigma-1/2) dt
      =(2pi)^(1-sigma) r^sigma exp(-ir+i pi/4) 1_(A,B](r)
           +O(A^(sigma-1/2)
                +A^(sigma+1/2)/(|A-r|+sqrt(A))
                +B^(sigma+1/2)/(|B-r|+sqrt(B))).

Read Lemma 1's central quadratic change, Lemma 2's endpoint windows,
interior saddle plus outer integrals, and nonstationary outside cases.
The endpoint windows use a second-derivative bound; the outer pieces
use integration by parts. Lemma 3 adds fixed nonnegative log powers.
These calculus lemmas assume no RH. They retain the saddle main term
and do not assert arithmetic cancellation. Import the stated result;
no reproof or independent audit of its supporting references is needed
for this bounded test.

For readable endpoint notation also inspected William Banks,
*Shifting the ordinates of zeros of the Riemann zeta function*,
[arXiv:2405.11084v1, Lemma 2.8](https://arxiv.org/html/2405.11084v1#S2.SS4).
The fetched text labels the submission 17 May 2024 and carries an
internal date 24 August 2026. Its conjugate-phase formula has
10a>=b>a>=10, sigma in [1/10,10], m in {0,1}, indicator a<u<=b,
and error

    O((a^(sigma-1/2)
        +a^(sigma+1/2)/(|a-u|+sqrt(a))
        +b^(sigma+1/2)/(|b-u|+sqrt(b))) (log a)^m).

The result explicitly cites Gonek Lemmas 2/3. Only this unconditional
auxiliary formula is relevant; Banks's RH-dependent main theorems
are not imported. Equality at an endpoint is absorbed by the stated
error, not an omitted case. The endpoint formula is a tool for finite
modes, not a theorem about the sine's complete correlation.

**Finite sine approximation.** [NIST DLMF 4.19.1](https://dlmf.nist.gov/4.19.E1)
states the sine series. For the proposed first-order implementation use
the standard named Taylor theorem with Lagrange remainder for real
arguments, with the sine's second-degree Taylor polynomial at zero
equal to z and |sin'''|<=1: |sin z-z|<=|z|^3/6. This is a scalar
tool only, not an integrated error estimate or permission to exchange
an infinite expansion with either weighted integral.

Reuse `2026-10-31-density-peano-dual-chirp-pairing.md` for the already
inspected McKee--Sun--Ye Theorems 1.1/1.2 and Blomer--Khan--Young
Lemma 8.1/Proposition 8.2. Those tools have their recorded derivative,
support and endpoint restrictions. Their comparison is unchanged;
the new logarithmic formula supplies explicit near-endpoint cases
after a justified phase reduction. Full matching and supporting
Mathlib coverage remain unchecked for all proposed specializations.

### Exact remaining test and boundaries of approval

The one covered mathematical attempt is the COVERED_TARGET above.
Start with the fixed first-order approximation epsilon P_T to the
same bounded sine amplitude; do not change the prime block or let
epsilon depend on T. The complete proposed bounds remain

    integral_J D_h sin(epsilon P_T) >= a T log T,
    |integral_[T,2T] V_T psi_epsilon| <= (a/2)T(log T)^3

for some fixed epsilon,a>0 and every sufficiently large real T.
The first linear density moment is L574's established input, not a
new result to reprove. The sine remainder must be paid against |D_h|
or its actual positive majorant Q_T, using proved weighted moments.
The chirp remainder must separately be paid against its actual Peano
convolution pairing; an unweighted remainder bound does not pay it.
No moment bound for either cost is established by this assessment.

For every finite prime monomial retain both conjugate frequency signs,
all repeated primes, equal integer products and the n=m zero
coefficient. Specify actual product supports, coefficient norms and
finite mean-square errors before asserting an admissible length.
L574's existing quadratic norm bound does not imply all needed higher
weighted moments. An unspecified O(T(log T)^3) leakage constant does
not meet the fixed fraction required above.

For the complete linear chirp term, use finite Fubini with the triangular
kernel, retaining both strips and any new integration limits. Check the
sign and h^(-2) normalization of the weighted Peano transfer for the new
amplitude. C574a proves it for g=D_h/Q_T, not for an arbitrary b by
assertion. The same compact-integrability calculus interface is available
to justify the specialization; it is not a new general Peano theorem.

Use the logarithmic saddle formula only after explicitly identifying
each mode's phase and positive saddle parameter, the actual endpoints,
the correct 2pi convention and conjugation. A reduction of exact theta
to a logarithmic phase must bound its full error from an established
analytic input; L477's phase derivative estimates alone must not be
silently replaced by an unrecorded phase expansion. Alternatively check
the exact-theta hypotheses of the reused finite weighted tools and pay
all endpoint terms. Bound every interior, exterior and endpoint mode,
and sum errors over the entire ordered block. The source's oscillatory
main term is an obligation, not a small error. Any rational-frequency
coincidences and endpoint proximity must remain in that sum.

Continue this implementation only if both complete budgets are proved
with compatible fixed epsilon,a and constants independent of large
real T. An informative failure is a proved loss exceeding its allowed
share, or an evaluated surviving stationary contribution that blocks
the proposed leakage test. Preserve such evidence and park this
first-order implementation. Do not respond by assuming cancellation,
discarding mass, increasing Taylor degree without a new covered target,
or repeating the generic derivative/linear-dual searches. Failure would
not refute the bounded sine inequality, the full-residual lower bound,
or RH. This review asserts neither success nor impossibility.

### Duplicate and failure comparison; search record

L482's Markov obstruction assumes uniform polynomial approximation
on the full interval [0,B_T] and its particular formal product budget.
The present finite weighted Taylor test does not impose that uniform
approximation hypothesis. L482 expressly leaves actual-height weighted
approximation and nonpolynomial tests open. Its proof was inspected;
it is not a universal degree ban.

L319's reciprocal stationary transform preserves the unsigned ratio
form and returns it after a second transform. It supplies no sign for
the new correlation. Its proof and endpoint conventions were inspected;
there is no proposal to repeat that involution as a signing argument.
The constructive-linear-dual assessment's missing curved-phase pairing
is also preserved. None of those source constructions supplies this
sine multiplier or its complete chirp bound.

C574a's generic quotient-variation budgets fail their explicit
threshold and remain parked. This test changes the amplitude and
uses finite prime modes; it does not claim a better bound for that
quotient. L481's global interpolation, L482's envelope and L572's
rank-certificate failures remain intact. No discovered exact duplicate
or stronger matching theorem was established by the bounded search.

Queries included `"Dirichlet polynomial" "characteristic function"
primes weighted`, `"twisted second moment" "Riemann Siegel"
stationary phase Dirichlet polynomial`, `"sin" "prime sum" "zeta"
moments Taylor`, `"Curran" "2303.10123" "Lemma 2.5"`, `twisted
second moment zeta Dirichlet polynomial Bettin Chandee Radziwill
theorem`, `prime sums weighted central limit theorem zeta
characteristic function sine`, `"prime sums" "characteristic
functions" "zeta"`, `"weighted central limit" "zeta" Fazzari prime`,
`"Gonek" "Lemma" "stationary" "integral" zeta`, and the exact
Gonek title. Noisy characteristic-function terminology, snippets,
secondary summaries and unrelated hits were not mathematical evidence.
Followed the primary weighted-moment and saddle references above.
No broad scalar-dual retrieval was repeated and no failed search is
evidence of novelty. The original Gonek source was accessible through
web retrieval; a local-shell download failed DNS and was not used.

The sources inspected suffice for a finite hypothesis-and-loss test;
the remaining gap is mathematical estimation, not persistent source
access. EXPLORE is the appropriate limited decision. It does not certify
originality, approve a solution, or derive previously uncovered
mathematics. Newly changed coverage is submitted for the supervisor's
separate next-turn approval. After that gate, the default continuation
is the one mathematical calculation specified above, without another
literature search unless an essential hypothesis actually changes.
