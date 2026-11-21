# One-sided prime-degree average — bounded specialization nomination

TARGET: Test whether every-epsilon upper bounds for A_n(X_n) imply RH by a positive-coefficient correction of the ordinary Li partial-sum germ, verifying cutoff errors, multiplicities and positive-axis regularity.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step236's completed comparison in 2026-11-10-prime-laguerre-one-sided-average-review-235.md, including exact Li/Cesaro/partial-sum searches, L976's distinct-germ obstruction and step235's two-sided stop. No exact moving-cutoff theorem was inspected; no novelty claim.
SOURCE_EVIDENCE: Lagarias AIF57(2007) Thm2.4/(2.20)-(2.23), pp1702-1703 and proof https://www.numdam.org/item/10.5802/aif.2311.pdf#page=15 ; Voros arXiv1403.4558v2 (31)-(32), p10 and Section3.4, p12 https://arxiv.org/pdf/1403.4558v2#page=10 ; Flajolet-Sedgewick Complex Asymptotics (8May2004) ThmIV.3(i)-(ii) and full proof, printed pp15-16 https://algo.inria.fr/flajolet/Publications/ch4567.pdf#page=23 ; reuse review233/L980 arithmetic split/smooth trend and review207 local analytic tools.
COMPARISON: Known individual Li growth/radius criteria and the generic boundary theorem supply standard tools, not the cumulative/moving-cutoff implication or arithmetic payment. Only their bounded specialization is proposed; no source theorem is reproved.
GAP: Establish the partial-sum germ and sign direction, check the needed L982 step235 error independently, retain finite-prefix terms and arbitrary zero orders, and verify a correction's signs, finite radius and same-germ positive-axis regularity. Arithmetic payment remains open and outside this test.
REASON: Step237 separately checked the nominated source contracts and repaired direct-URL provenance; this SPECIALIZE assessment is ready for exactly the saved test, without approving its unresolved mathematics or repeating two-sided inverse recovery.
SCOPE: Actual Lambda and L981/L982's complete P_k, integers n>=2, X_n=exp(10000*(n+1)^4), A_n(X)=(n-1)^(-1)*sum_(k=2)^n P_k(X); premise: for every epsilon>0 there is finite C_epsilon>=0 with A_n(X_n)<=C_epsilon*exp(epsilon*n) for all n>=2. No lower bound, RH, simple zeros, uniform n/X limit exchange or independent prime estimate is assumed.

The central gap is actual-Xi positivity and L966/L968 signed forcing.
Success would specify a sufficient one-sided arithmetic threshold,
not establish it. The application is REPRODUCTION, not a creative
central mechanism or an advance beyond the inspected source methods.
The desired conclusion is RH, not a proof of L966's separate Q_n
signs; L968's sufficient regularized sign premise is not assumed.

Use L981/L982 to relate the proposed average to fixed-index S_f,
verifying only the cutoff estimate needed. The step235 application
is unaudited. L980's audited split and smooth trend fix signs and
normalization. Investigate the ordinary generating function of
unnormalized partial sums of ordinary lambda_k, k=2 through n,
using justified operations on the germ in Voros(32). Do not substitute
Keiper's lambda_k/k or L976's translated logarithm. L018 supplies
actual zeros and symmetries; L968 supplies audited individual-criterion
normalization, not a criterion for averages.

The discriminating test is whether, conditional on an interior mapped
zero, the cumulative germ and a correction meet every Pringsheim
hypothesis while remaining regular at the positive radius point.
Check nonremovability for arbitrary positive zero orders and the
correction's analyticity beyond that radius. Keep all prefixes, pole
compensation and every-epsilon quantifiers. Do not interchange an
infinite degree sum and the arithmetic cutoff limit without proof.
Import Pringsheim precisely; justify only the specialization and
needed analytic identities.

Continue if these obligations yield a complete implication or a
specific informative obstruction; abandon this application if a
load-bearing hypothesis fails. After a successful criterion, stop
criterion-only reformulation absent a distinct independently testable
payment mechanism with its own coverage. Historical stops remain
scoped. No mathematical script is needed. Full matching Mathlib
coverage is unchecked/unknown. This is a source nomination, not a
proved input; source approval was completed separately in step237.

## Separate source approval and provenance repair — step237

On 10 November 2026 all three direct primary PDFs above were opened.
The exact saved TARGET and SCOPE are unchanged. Reused review235's
searches and local duplicate/failure comparison rather than running
another discovery search. This is a process repair, not new source
coverage or a mathematical advance.

Rechecked Lagarias Theorem 2.4 and its full proof, printed pp1702-1703:
the hypotheses concern irreducible cuspidal unitary automorphic
representations, and the one-sided criterion concerns individual
coefficients. Its published coordinate-description inconsistency
remains excluded as recorded in review235; no new zeta specialization
or average criterion is inferred here.

Rechecked Voros (31)-(32), printed p10, and the Section3.4 radius
statement, printed p12. These supply the ordinary Li normalization
and the logarithmic germ used in the proposed test, not its cumulative
observable. No saddle argument is needed or imported.

Rechecked Flajolet-Sedgewick Theorem IV.3 and both proof cases,
printed pp15-16 (PDF pages23-24): finite Taylor radius is essential;
part(ii) additionally requires nonnegative coefficients. The proof
uses Cauchy estimates in part(i), and recentering with nonnegative
double sums in part(ii). Import the named theorem, without reproof.
The future application must establish these hypotheses for its own
corrected germ; the source does not establish them for A_n.

No new implication, cutoff estimate or lemma is proved. The remaining
obligations listed above are exactly the approved bounded research
test. Full matching Mathlib coverage remains unchecked/unknown.
