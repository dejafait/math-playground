# Fixed-index compensated prime-Laguerre identification — source assessment

TARGET: Identify the fixed-n limit of P_n(X) with S_f(n) using Lagarias's compensated eta moments, retaining the pole compensation and full prime-power endpoints.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step228 reused review223's bounded arithmetic-Li/Laguerre search and exclusions and review224's polynomial/endpoint coverage. Narrow searches in the 10 November Li/Laguerre assessments, histories and attempts found this nomination and L981, not a completed combined identification. Reopened only primary moment/normalization passages and DLMF18.5.12; no repeated blocked extraction or general bibliography search.
SOURCE_EVIDENCE: Lagarias, Ann. Inst. Fourier57(5)(2007),1689-1740, DOI10.5802/aif.2311, Definition4.3/(4.5), Lemma4.4/(4.8), pp1708-1709, and unnumbered eta-moment display immediately after(4.13), p1709: published PDF text and arXiv math/0404394v4 Section4 inspected. DLMF18.5.12 and source note inspected. L977/L980 definitions and L981 definition/input contract read; review223/224 reused. Original1999 convergence proof remains unread.
COMPARISON: The unconditional fixed-index moment has the pole subtraction and (-1)^j/j! normalization needed for comparison with the finite Laguerre series. Definition4.3 and(4.8) match the local nonalternating convention; conflicting(4.13) is excluded. Integer full-term cutoffs are covered. Only finite algebra, compensator integration and a fixed-degree integer-to-real endpoint estimate remain to be written; no assembled identity is proved here.
GAP: Prove the exact combined fixed-n identification, including lower integration endpoint1, coefficient/factorial bookkeeping and arbitrary real cutoffs. No essential source coverage is missing for this specialization. This review proves neither that identity nor an n-uniform limit interchange or signed arithmetic bound.
REASON: Essential primary statement coverage now permits routine specialization by precise citation rather than reproof of the moment theorem. This clears the normalization source gate locally; it establishes no mathematical input or cancellation mechanism.
LITERATURE_REASON: The new exact fixed-n identification lies outside review224's tail-only scope and review223 explicitly withheld certification of the combined formula. Reuse its inspected primary moment statement before any additional retrieval; assess only the missing applicability.
SCOPE: Actual von Mangoldt prime powers, each fixed integer n>=2, real X tending to infinity, and L977/L980's ordinary nonalternating eta convention. No RH, simplicity, n-uniform limit exchange, arithmetic sign, or Li positivity is assumed.

The original step227 nomination below is preserved as historical scope;
its source gate is completed by step228 below. Compare
the exact statement against the already inspected Lagarias fixed-index
moment citation and L981's endpoint contract. Import the primary
statement if sufficient, with a precise citation, rather than require
recovery of the inaccessible original proof. Identify any essential
uncovered case before retrieving a different source. Do not use the
conflicting alternating remark (4.13), the retracted Dirichlet cutoff
paper, or the parked Coffey extraction route.

Proposed mathematical inputs to examine are L981, the defining eta/S_f
conventions in L977/L980, the primary moment statement and DLMF18.5.12.
This is a nomination, not an established argument. Decide whether only
finite-sum specialization and real-endpoint applicability remain;
no such derivation is performed here.

Continue only if compensation and signs match the exact P_n definition
and intended S_f. An unresolved additive constant, sign, or endpoint
issue blocks use until repaired. Even successful identification leaves
the n-uniform bound S_f(n)<=C_epsilon*exp(epsilon*n), for every epsilon>0,
unproved. This is an interface specialization, not a creative sign
mechanism or progress beyond checked sources. Full matching Mathlib
coverage is unchecked and unknown.

## Completed source gate — step228, 10 November2026

The main gap remains actual-Xi positivity in L030-L032/C032a and
sufficient signed Li forcing through L966/L968. The intermediate
target is exactly TARGET above. A successful identification would
allow later work to use L981 with an identified normalization; it
would not bound the signed retained statistic. Continue only if
all constants, signs and endpoints match; otherwise block that use.
Fixed-n success cannot pay the n-uniform signed threshold.

### Precise primary input

[Lagarias, published p1709](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=22),
unnumbered display immediately after(4.13), states for each fixed
integer j>=0:

    eta_j=(-1)^j/j! * lim_(N->infinity)
      [sum_(m=1)^N Lambda(m)*(log m)^j/m
       -(log N)^(j+1)/(j+1)].

N is integer, with its last term included fully. Lambda is the
actual von Mangoldt function. The Laurent definition(4.12) agrees
with Definition4.3/(4.5);(4.8) has the local nonalternating binomial
convention. No RH or rate uniform in j is asserted in this moment
statement. The inconsistent alternating(4.13) is excluded, as in L977.
The [arXiv v4 Section4 display](https://arxiv.org/html/math/0404394v4#S4)
was also read to confirm the formula; its automatic equation numbers
differ from the publication. PDF screenshots returned textual image
placeholders, so no visual inspection is claimed.

Review223 records the original Bombieri-Lagarias1999 access failure.
Its proof remains unread and was not requested again. The precise
published fixed-moment statement above suffices as an external input;
no original theorem number or independent proof verification is
invented. Import that statement rather than reprove it.

### What remains a specialization

[DLMF18.5.12](https://dlmf.nist.gov/18.5.E12) gives the global finite
Laguerre series for nonnegative integer degree. Its note cites Szego,
*Orthogonal Polynomials*, fourth edition1975,(5.3.3); the book proof
was not read independently. Degree n-1 and parameter1 are in scope.
L981 records that finite series with the logarithmic argument used
in P_n. There is no restricted oscillatory interval or infinite
polynomial expansion in this input.

For fixed n only finitely many fixed moments are required. The next
mathematical step must write their assembly, integrate the compensation
from1 with its correct constant, and check every sign/factorial.
For real cutoffs it must compare X with its integer floor: preserve
the entire finite prime-power sum and estimate the compensator on
the remaining interval at fixed degree. These elementary tasks are
covered for specialization, but are not carried out in this review.
No half-weight rule, contour formula, uniform-in-n exchange or new
prime estimate is needed for this particular endpoint extension.
No inspected theorem directly states the entire local real-endpoint
formula, hence SPECIALIZE rather than IMPORT.

L981 supplies the audited tail contract only. L977/L980 supply the
eta/S_f definitions here; their zero-contour and residual proofs
need not become inputs to a finite polynomial assembly. The future
canonical proof must distinguish definitions from mathematical input
uses and record actual dependencies in DAG. No edge is added here.

### Reuse, exclusions and routing

Reuse [review223](2026-11-10-compensated-prime-laguerre-head-review-223.md)
and [review224](2026-11-10-prime-laguerre-cauchy-tail-review-224.md).
Their exact-title, arithmetic Li/Laguerre and cutoff searches cover
the broader source setting. This narrower normalization target needs
no new general search. Local queries used fixed-n identification,
compensated moments and eta moments in the 10 November assessments
and specific Li/Laguerre histories/attempts. No completed matching
identification was found in that scope; no novelty is inferred.

The [step224 direct-import stop](../../ATTEMPTS/2026-11-10-compensated-prime-laguerre-direct-import-limit-224.md)
concerns missing uniform signed payment, not this independently
testable fixed-index interface. Preserve it, the retracted Dirichlet
cutoff exclusion, parked Coffey route and L975/L976/L977 obstruction
scopes. No failed extraction or exhausted mathematical route is retried.

The unpaid downstream threshold is S_f(n)<=C_epsilon*exp(epsilon*n)
for every epsilon>0, with constants independent of n, together with
the exact connections specified in the canonical route. Fixed moments
and L981's absolute tail do not supply that threshold. No independent
creative signed-cancellation mechanism is ready from these inputs;
that blocks creative nomination, not this routine reproduction.
Full matching Mathlib coverage remains unchecked/unknown; no absence
claim or formalization is made.

The unchanged TARGET is ready for a REPRODUCTION mathematical step
after separate next-turn supervisor approval. Step228 is a literature
comparison only: no combined formula, endpoint estimate or other new
result was derived; no lemma, mathematical script, DAG or PROOF
argument was changed.
