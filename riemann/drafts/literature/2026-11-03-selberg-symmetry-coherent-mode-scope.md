# Selberg symmetry: completed arithmetic discrimination source review

TARGET: Assess whether the unconditional Selberg symmetry formula and its proved remainder exclude L733's coherent power mode or supply a coercive estimate for L732's drift-removed prefix energy.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact Selberg symmetry/error formula, improved/refined remainders, fixed-power modes and local duplicates; inspected the primary statements and relevant error arguments listed below, L732, L733 and the recorded prime-variance transfer stop. Found an overlapping conditional power-mode manuscript; no exhaustive coverage or novelty claim.
SOURCE_EVIDENCE: Selberg 1949 (2.8)–(2.13), printed pp. 309–310, with Section 2 proof text; Tenenbaum Bordeaux 2000 first lecture (2)–(6), printed pp. 2–4, and (9)–(14), pp. 5–6; Granville–Soundararajan 2014 author draft Theorem 1.1.2 and full proof, p. 10; CSM_RH Paper 64 v0.1 Sections 1–4, with seed qualification. Precise links and read limits below.
COMPARISON: The inspected unconditional discrepancy relation retains O(x); neither its statement nor its inspected contraction argument gives L732's drift-optimized squared prefix bound. The overlapping sharper mode estimate is seed-dependent and is not imported. Compatibility of L733's power with the weaker fixed-actual-kernel O(x) relation is a distinct bounded specialization to test, not proved in this literature turn.
GAP: No coercive quadratic estimate, projected remainder bound, actual-family anchor, complementary-tail control or Xi sign is supplied. No assertion that F satisfies the self-consistent arithmetic identity or that every stronger Selberg formulation is ineffective is made.
REASON: Park direct import of a prefix upper bound; the source comparison identifies the exact O(x) constraint and an overlap qualification, permitting one separately approved elementary kernel diagnostic before abandoning that coarse constraint as a discriminator.
SCOPE: Completed literature-only review; unconditional named formulas may be cited within their exact arithmetic scope. No model computation, new lemma or mathematical script was derived. The proposed follow-up has its own assessment and requires separate next-turn approval.

## Original question and bounded source test

L733 establishes a limitation for a numerical increment envelope in
the class of general profiles. Selberg's symmetry formula is a named
arithmetic relation to inspect independently. Retrieve a primary
statement, its exact remainder and the proof cases needed for any
claimed uniformity or specialization; do not rely on model memory.
Search the active notebook for this specific relation before reading
further local proofs. Do not treat the absence of an Euler product
or prime support for F as a quantitative prefix bound.

The prospective downstream use was a paid additional constraint on
long-range discrepancy, potentially supplying information lost in the
increment envelope. No coercivity, favorable sign, remainder size or
substitution of F into an arithmetic theorem is assumed. Distinguish
the actual von Mangoldt convolution from a proposed continuous model
and from a linearized discrepancy relation. If a new model calculation
is needed, nominate it for a separately approved research turn.

Continue only if inspected unconditional hypotheses identify a
specific usable term with a remainder on the required scale, or a
concrete separately testable implication. If the source leaves the
prefix term unpaid, requires an RH-strength estimate, or excludes F
only by definition, record that limitation and park this mechanism.
Do not infer an upper estimate from an identity or an absolute bound.
Preserve the existing envelope-only and actual-prefix source stops.

Essential local IDs for the future comparison: L733 and L732; L729
only if its actual arithmetic identities are explicitly used. Actual
arithmetic covariance, scalar anchors, complementary tails and Xi
mixed positivity remain open. Before proposing a zero-free improvement
or reopening a parked estimate, read the October baseline and external
input register required by GOAL.md. No such improvement is proposed here.

LITERATURE_REASON: Changed essential input: the exact Selberg symmetry
formula and its unconditional remainder were not covered by the reused
increment-variance assessment. This review prepares a different
arithmetic mechanism; it does not repeat browsing for the audited target.

Creative work is not yet justified: exact source strength and a paid
coercive term are missing. If the source comparison supplies a concrete
central-gap mechanism, nominate its bounded proof attempt with the
required creative routing and escalation; otherwise do not invent one.
Mathlib matching coverage is not checked; availability is unknown.

## Exact source statements and read evidence

All formulas here concern the ordinary von Mangoldt function, with
Lambda(1)=0, psi(x)=sum_(n<=x)Lambda(n), real x tending to infinity,
and absolute implied constants. No RH or October zero-free input is
assumed. They are source transcriptions, not new local lemmas.

1. Selberg, “An Elementary Proof of the Prime-Number Theorem,”
   *Annals of Mathematics* 50(2) (1949), 305–313,
   [primary scan](https://www.math.lsu.edu/~mahlburg/teaching/handouts/2014-7230/Selberg-ElemPNT1949.pdf),
   DOI 10.2307/1969455. This scan has a cover: printed 309–310 are PDF
   indices 5–6. Read the Section 2 proof text, especially (2.4)–(2.9),
   and (2.12)–(2.13). Equation (2.8) states

       sum_(p<=x)(log p)^2 + sum_(pq<=x)log p log q
         =2x log x+O(x).

   The pair sum is ordered. Equations (2.9) and (2.12) use theta,
   not psi; (2.12) has R_theta=theta-x and prime kernel log p.
   The proof's divisor/Mobius estimates and prime-power error retain
   O(x); the two-prime iteration (2.13) has O(x log log x).
   The Wolf-hosted scan lacked readable text, and screenshot calls
   returned text placeholders rather than inspectable images; no
   claim of visual verification is made. Ambiguous OCR is resolved
   for the needed psi statement by the readable source below.

2. Tenenbaum, *Trois conferences sur la theorie analytique et
   probabiliste des nombres*, Bordeaux, 7–9 December 2000, first
   lecture “Convolutions et equations fonctionnelles : sur la preuve
   elementaire de Daboussi,”
   [author PDF](https://tenenb.perso.math.cnrs.fr/PPP/JER.pdf),
   (2)–(6), printed pp. 2–4 (PDF indices 3–5). Read the supporting
   Lambda_2 convolution and O(x) error calculation, and the conversion
   to the following exact formulation, (6):

       R(x)log x + sum_(n<=x)Lambda(n)R(x/n)=O(x),
       R(x)=psi(x)-x.

   Equation (2) supplies sum Lambda(n)/n=log x+O(1).
   Replacing log n by log x also costs O(x). Read (9)–(14) and the
   concluding contraction discussion, pp. 5–6: these estimate absolute
   discrepancy and conclude R=o(x). They do not state the weighted
   squared prefix or an optimized-complex-drift estimate. In (8)–(12)
   log_2 denotes iterated logarithm, not a square. No differentiation
   of an error term or uniform short-interval refinement is imported.

3. Granville–Soundararajan, *Multiplicative number theory: The pretentious
   approach*, 2014 author draft, Section 1.1.6, Theorem 1.1.2, printed
   p. 10 (PDF index 14),
   [author PDF](https://dms.umontreal.ca/~andrew/PDF/Book.To1.4.pdf).
   Read the complete proof. It identifies
   Lambda_2=Lambda log+Lambda*Lambda=mu*(log)^2. A divisor-function
   comparison gives a summatory error O(x^(2/3+epsilon)), choosing
   fixed 0<epsilon<1/3; summing
   against mu by absolute values yields O(x), not that smaller power.
   The prime-power removal is separately retained. This checks a
   modern derivation's remainder bookkeeping; it supplies no signed
   Mobius cancellation or L732 norm bound. This is a mutable working
   draft, not a claim about a pinned published edition.

## Duplicates, stronger leads and nonimports

The notebook-scoped phrase search covered foundations, literature
assessments, ATTEMPTS, history and lemma text. It found no earlier
assessment of this arithmetic symmetry equation. The October 29
Selberg review concerns a differentiated logarithmic-derivative
approximation and cannot be reused as coverage for it. The inspected
prime-variance assessment and its transfer stop already leave cumulative
covariance, the single drift and actual-family tails unpaid; they remain
in force. L732 supplies a necessary lower obstruction, not an upper
estimate. L733 already supplies the general-profile energy asymptotic;
it need not be reproved in a follow-up.

A search found *CSM_RH Paper 64 — Selberg-Symmetry Boundary Saturation,
Sparse Integer Pseudo-Primes, and the Ordinary-Arithmetic Residual*,
v0.1, 2026-09-09,
[primary manuscript](https://unboundedaxiom.org/p/lm-003939/).
Inspected Sections 1–4, especially Theorem 3.1 and its preceding
calculation. It studies R_rho(y)=y^rho, 0<Re rho<1, under a PESC
seed, and asserts a convolution main term x/(1-rho) with a sharper
power-sized error. Its phrase about a PNT power bound does not specify
enough exponent comparison for an unconditional use of that error.
The proposed weaker O(x) test below therefore imports neither this
asymptotic nor the seed. Its method-barrier label is the manuscript's
claim, not a local certificate. The sparse-model and progression sections
are outside this assessment. This overlap prevents a novelty claim for
the power-mode idea, while leaving an elementary hypothesis check useful.

Queries included “Selberg 1949 elementary proof prime number theorem
symmetry formula pdf,” “Selberg symmetry formula error term remainder
unconditional improved remainder,” “Selberg symmetry formula refined,”
the exact R(x)log x formula, and Selberg/Euler-constant variants. No
inspected stronger unconditional remainder theorem supplied the requested
prefix estimate. This is a bounded search result, not a claim that no
sharper expansion or useful refinement exists. Search snippets suggesting
refined constants are not theorem inputs. Tatuzawa–Iseki's 1951 paper and
Selberg's elementary-methods/limitations article remain unread leads;
the former PDF request failed, and neither is needed for the O(x) test.
No result is inferred from their titles or bibliographic records.

## Applicability decision and bounded continuation

The source mismatch is substantive: the equation acts linearly on the
*actual* discrepancy with the actual arithmetic kernel, whereas L732
asks for a quadratic norm after one complex scalar projection. The
sources checked do not pay the pairing with the equation's remainder,
any drift term introduced by that projection, or the physical tail.
PNT contraction and a signed identity are not themselves such a bound.
This is a comparison of inspected statements, not a proof that Selberg
methods cannot work.

Nor may one replace Lambda by dF, declare F to be psi, or call a
fixed-kernel test a self-consistent arithmetic model. The original
source question therefore has two separate answers: no prefix bound
is ready to import; exclusion of the declared power by the *coarse*
O(x) equation needs one explicit test. That test is nominated in
`2026-11-04-selberg-operator-power-diagnostic.md`, with the actual kernel
held fixed and no seed. It has not been calculated here.

No zero-free improvement or reopening of an October arithmetic estimate
is proposed; the baseline/register is not reloaded. If a later target
does propose one, GOAL.md's mandatory comparison applies. A protected
creative attempt remains unjustified at present: no quantitatively
controlled projected residual or paid coercive term has been identified.
The follow-up is a reproduction/specialization diagnostic, not creative
central-gap development. After that one test, park the coarse relation
unless a materially stronger residual input is supplied.

Mathlib: full matching symmetry or prefix-transfer coverage not checked;
availability unknown. Metamath's named `selberg` assertion was inspected
as an independent statement check; it is not Mathlib coverage and its
entire formal proof was not replayed. No new standard input is installed
in the proof assembly by this literature-only turn.
