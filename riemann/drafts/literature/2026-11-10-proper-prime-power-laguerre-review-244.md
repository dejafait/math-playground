# Proper prime powers at the common cutoff — specialization nomination

TARGET: Bound the absolute proper-prime-power contribution R_n(X) by C*n*(1+log(X)^2) for all n>=2 and real X>=2, and specialize to X_n=exp(10000*(n+1)^4) without changing the compensator.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step244 searched exact Laguerre/prime-power bound combinations and DLMF18.14.8; a scoped exact-term search in lemmas and the 10 November assessments found no matching local result. L981/L982 and the step224/233/235/240/243 stops retain all powers and do not bound this isolated component. No novelty inference.
SOURCE_EVIDENCE: Inspected live NIST DLMF18.14.8, its full x>=0, alpha>=0 hypotheses, integer degree and value at0, and attribution to Koornwinder1977 Remark4.1; https://dlmf.nist.gov/18.14.E8 . Reuse L981/L982's definitions and full real endpoints, and review241's finite degree-average convention. Koornwinder's original proof was not inspected and is not separately needed beyond the precise DLMF citation.
COMPARISON: A global polynomial bound covers every nonnegative prime-power logarithm and every degree in the average, unlike the compact bulk asymptotic of L985. The source does not itself state this growing-degree arithmetic sum. Only a positive-sum specialization using elementary geometric sums and integral comparison remains; no prime cancellation theorem is required or proposed.
GAP: Verify the complete proper-power sum, uniform constant, degree normalization, all exponents a>=2, real cutoff endpoints and the polynomial-in-n specialization. The contribution of primes, continuum compensator and L984(H) remain unpaid.
REASON: Isolating sparse proper powers is independently testable and could remove one full component of the actual common-cutoff arithmetic head; it does not reopen centered Vaughan cancellation. Import the global inequality without reproof and derive only the arithmetic specialization. This newly written ready assessment requires separate approval next turn before research.
SCOPE: Integers n>=2, actual primes p and all integers a>=2, real X>=2, full endpoints p^a<=X, K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u). No RH, simplicity, PNT estimate, large-n asymptotic, prime-only replacement before payment, or change to the continuum integral.

## Exact proposed observable and threshold

Define the target, without asserting its bound:

    R_n(X)=sum_(p prime,a>=2,p^a<=X)
                        (log p)*|K_n(a*log p)|/p^a.

Seek an absolute finite C independent of n and X for the TARGET
bound, and its every-epsilon subexponential consequence at L981's
X_n. This finite positive observable majorizes the absolute value of
the proper-power contribution to the degree-averaged Mangoldt sum.
No continuum density is assigned to proper powers and the original
compensator must be kept exactly. The prime-only remainder, if this
specialization succeeds, is still an unbounded signed observable.

## Imported contract and permitted specialization

[NIST DLMF18.14.8](https://dlmf.nist.gov/18.14.E8), live page inspected
10 November2026, states for every integer d>=0, alpha>=0 and x>=0:

    exp(-x/2)*|L_d^(alpha)(x)| <= L_d^(alpha)(0)
                                             = (alpha+1)_d/d!.

The displayed theorem and its full parameter range were inspected,
not merely a search snippet. DLMF attributes its proof to
T.H. Koornwinder, *The addition formula for Laguerre polynomials*,
SIAM J. Math. Anal.8 (1977),535-540, Remark4.1. Import DLMF's
stated result; no general reproof is justified. alpha=1 and each
d=k-1 in the defining finite average are within the stated range.
This is a global bound, so it has no turning-point or large-argument
gap at the remote cutoff.

The nominated calculation must retain a=2 separately from a>=3,
use only positive majorants, and justify any extension to infinite
positive sums by monotonicity and convergence. Elementary geometric
series and one-variable integral comparison suffice as tools; no
unread prime-distribution estimate is essential. The requested bound,
its constants and its cutoff consequence are not proved in this
literature turn. If an unexpectedly divergent exponent sum or a
nonpolynomial cutoff loss remains, record the exact obstruction and
stop rather than discard powers informally.

## Relevance, stopping scope and classification

The main gap remains actual-Xi positivity and L984's unpaid signed
bound. The plausible use is a rigorously paid proper-power removal
in that same finite arithmetic average, covering its entire range
rather than just the bulk B_n. This does not sign primes or control
the continuum contribution. It does not contradict any recorded
stop: L985 addresses dense uncentered derivative envelopes; step235
addresses automatic average payment; step233 refutes a lobe rule.

Continue only if the proposed uniform majorant and its cutoff
specialization are proved with full endpoints. Do not claim novelty,
an RH result, or start a second mechanism. Expected classification:
REPRODUCTION, a standard specialization. Creative routing remains
unjustified because no new gain for the dense signed prime residual
has been identified. Matching Mathlib coverage is unchecked and
unknown; neither formalization nor absence is claimed.
