# Truncated microscopic density: completed source review

TARGET: Assess whether actual-height truncated microscopic density differences admit a lower bound c T log T with cap (log T)^4, for L477's fixed cutoff.
CHECKED: 2026-10-31
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Completed bounded sharp-polynomial fourth-moment, truncated absolute-shift and microscopic-difference searches; compared the prior microscopic-density, weighted-cubic and Laplace-saturation assessments and L481/L482/L572 stops. No matching positive capped lower-bound theorem was identified; no novelty or falsity is inferred.
SOURCE_EVIDENCE: Newly inspected Montgomery--Vaughan, Hilbert's Inequality (1974), Theorem 2/Corollaries 2--3 pp. 74--75 and Section 4 p. 82; reread Curran 2303.10123v2 Lemma 2.3's exact unconditional O(N) mean-square statement. Reuse previously inspected Kovaleva/Curran shifted-zeta theorem limitations. Exact links, extraction qualifications and proposed use below.
COMPARISON: The sharp finite-polynomial mean square supports a separate unweighted cap-loss test without a Haar or full-zeta replacement. It supplies no positive absolute-difference lower bound. L481's complete-residual concentration and L482's global approximation obstruction do not decide this different observable; L572 stops its rank certificate only.
GAP: No inspected theorem or concrete covered signed mechanism supplies the required c T log T capped lower bound. The proposed O(T) cap-loss estimate remains unproved and is nominated separately; even success would leave the uncapped lower bound and full-residual comparison open.
REASON: Park direct import of the capped lower bound because theorem scope is missing, not because sources are inaccessible or the bound is disproved. Prepare one independent known-tool cap-loss specialization to test whether this cap is actually a new obstacle; no dependent lower-bound research is approved.
LITERATURE_REASON: The explicit cap changes the observable to a truncated actual-height density functional; its essential source hypotheses and overlap with prior saturation failures have not been assessed.
SCOPE: Source comparison only; fixed real T tending to infinity, M=floor(sqrt(T/(2 pi))), h=1/log T, J=[T+h,2T-h], A_M(t)=sum_(n<=M)n^(-1/2-it), F_M=|A_M|^2. No moving cutoff, Haar limit, independent phases, RH or full-residual transfer is authorized.

## Completed comparison and bounded continuation

The main gap is actual-Xi all-degree positivity and unbounded-height
initial signs. C481a is now canonical and its full proof was inspected:
the missing density premise would give a full-scale ratio norm, while
the chirped residual comparison, defect thresholds and negative mass
remain independent. The present target fixes a cap but does not itself
specify a new source of positive mass. Continue a lower-bound attempt
only with an applicable sharp-polynomial theorem or a covered bounded
test supplying that mass. Neither was identified in this review.

### Newly inspected primary input

Montgomery--Vaughan, *Hilbert's Inequality*, J. London Math. Soc. (2)
8 (1974), 73--82, DOI 10.1112/jlms/s2-8.1.73,
[author-hosted original](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf).
Read Theorem 2 and Corollaries 2--3, pp. 74--75, and Section 4,
p. 82. Corollary 3 assumes sum n|a_n|^2 finite and gives the
Dirichlet-series mean square with absolute O(sum n|a_n|^2) error.
Finite sequences satisfy its summability hypothesis. The proof expands
the square, applies the Hilbert bounds to the two endpoint bilinear
forms, and uses logarithmic frequency separation. The general Hilbert
inequality is imported; its full proof is not audited here. PDF formula
OCR is incomplete, so the exact finite form is checked independently
in the following readable primary statement. Screenshot requests
returned no inspectable image; shell download failed DNS. These are
extraction qualifications, not an essential source blocker.

Curran, *Correlations of the Riemann zeta function*,
[arXiv:2303.10123v2, Lemma 2.3](https://arxiv.org/html/2303.10123v2#S2),
states, for arbitrary complex a_n,

    integral_T^(2T)|sum_(n<=N)a_n n^(-it)|^2 dt
       =(T+O(N)) sum_(n<=N)|a_n|^2.

This lemma is unconditional; the RH assumption in his main shifted-zeta
upper bound is not needed for it. Its arbitrary coefficients permit
translations by phases. A proposed application must retain the actual
length of the squared sharp polynomial, not the original M. This is
an upper mean-square tool, not a positive density-difference theorem.
No disjoint-prime splitting lemma is invoked. No new specialization is
performed here.

### Reuse, overlap and search limits

Reuse `2026-10-31-microscopic-density-second-difference.md` for the
already inspected full-zeta product and RH-dependent bounds. No new
reading of those unchanged theorem proofs was needed. Read C481a in
full, L477's hypotheses/conclusion, L481's hypotheses/conclusion and
mean-square/finite-coefficient sections, L482's precise scope, L572's
statement/grouping, and its ATTEMPTS record. Reused the weighted-cubic
and Laplace-saturation comparisons for their actual-height versus
fixed-length Haar and residual-weighted exceptional-set limitations.
None is an obstruction to an unweighted upper cap-loss estimate.

Searches included `Dirichlet polynomial fourth moment partial sum zeta
sqrt T Montgomery Vaughan mean value truncated moments`, `Dirichlet
polynomial mean value theorem T sum coefficients O sum n coefficients
Montgomery Vaughan`, `Dirichlet polynomial truncated absolute shift
density`, and `microscopic Dirichlet polynomials absolute difference
lower bound`. Stronger twisted-fourth-moment and large-value results
surfaced as unread leads; none is used. Searches did not identify a
matching capped lower bound, not even a theorem covering its absolute
sharp-polynomial observable. This is not a claim of originality.

The weaker logarithm-losing estimate recorded in L481 should not be
silently used where the sharp error is essential. The newly verified
statement motivates a bounded test: determine whether the mass removed
by this cap is O(T), with the full finite fourth moment, translated
intervals and floor cutoff retained. This is an upper-tail question,
not another attempt to infer a lower bound from L481's stopped moment
ratio. Its proposed proof and exact hypotheses are nominated in
`2026-10-31-density-cap-loss-specialization.md`; no cap-loss inequality
or equivalence of capped/uncapped conjectures is proved this turn.

If the cap-loss test succeeds, the cap is not the missing lower-mass
mechanism at scale T log T; return to that central missing mechanism
before further density research. If only an O(T log T) loss is obtained,
it is insufficient for that conclusion. A creative lower-bound attempt
is currently blocked by the absence of a concrete covered source of
positive mass, not by historical stops on all density methods.
Full and supporting Mathlib coverage remain unchecked. No cross-notebook
input, lemma edit, mathematical script or new mathematical derivation.

## Original nomination, preserved; pending-review language superseded

The proposed mathematical test, not an established result, is the existence
of absolute c>0 and T_0 such that for every real T>=T_0,

    integral_J min(|F_M(t+h)-2F_M(t)+F_M(t-h)|,(log T)^4)dt
        >=c T log T.

This specifies the cap rather than asking generally for a joint-density
law. Its purpose is to test a route that retains difference mass while
limiting large peaks, instead of inferring an L1 bound from the stopped
second/fourth-moment certificate. A bound on a specified unbounded
sequence must be labeled separately. No claim is made that this stronger
test is true, necessary for RH, or equivalent to the untruncated target.
A positive result could supply C481a's missing premise; transfer from the
ratio component to the complete residual remains independent.

Review actual-height shifted sharp-polynomial results, quantitative
truncated/size-biased density arguments, and the already recorded
saturation and Haar-transfer failures. Retrieve exact hypotheses and
essential proof cases of any proposed input. Do not reuse a full-zeta
product moment as a sharp-cutoff absolute-difference theorem. Record
which results are actually inspected, and distinguish unread leads.

Continue only if the comparison identifies an applicable theorem or a
concrete independently testable truncation/tail mechanism with adequate
inputs at this cap and required scale. Park this cap if concentration
obstructs it, or if it merely repackages an exhausted certificate without
new information; preserve the weaker untruncated question. Missing
coverage authorizes no new lemma or mathematical script. This nomination
does not approve its own mathematics or claim novelty. Full matching and
supporting Mathlib coverage are unchecked. No cross-notebook input.
