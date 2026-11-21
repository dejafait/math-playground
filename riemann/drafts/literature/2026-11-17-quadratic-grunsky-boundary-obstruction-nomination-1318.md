# Fixed quadratic branch: boundary-obstruction nomination1318 — source review1319

TARGET: Test whether C031c's fixed-u=400 local branch has a pole or a critical point in |z|<1 for every sufficiently small positive tau, using only first variations at the unit-circle boundary and the fixed1307 boxes; if neither is certified, leave whole-disk univalence undecided.
CHECKED: 2026-11-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1319 read C031c, pertinent C031a/C031b/C030z ranges, assessment1316 and Grunsky-named failure/source records; searched simple polynomial-root perturbation and rational-map univalence terminology. Inspected de Oliveira Section3 Theorem2 and Ahlfors Chapter2 Section1.4/Chapter4 Section3.3. Exact searches and limits below; no branch calculation or originality claim.
SOURCE_EVIDENCE: de Oliveira, Real Anal. Exchange39(1)(2013/2014),207–218, arXiv1212.2066v1 Section2 differentiability/mean-value statements and Section3 Theorem2 with proof, https://arxiv.org/html/1212.2066v1 ; Ahlfors, Complex Analysis, 3rd ed.(1979), Chapter2 Section1.4 p30 equation(11), Chapter4 Section3.3 Theorem11/proof pp131–133, https://people.math.gatech.edu/~mccuan/courses/6321/lars-ahlfors-complex-analysis-third-edition-mcgraw-hill-science_engineering_math-1979.pdf . Reuse1316 for the existing coefficient branch and1314 for the meromorphic-univalence caveat.
COMPARISON: Classical C1 IFT covers local continuation and implicit differentiation of simple complex roots after a verified real two-coordinate specialization. Ahlfors covers reduced rational poles and the necessary nonzero derivative for holomorphic injectivity. These tools do not locate this branch’s roots or determine their radial signs. Linear stops1307/1311 do not decide the quadratic-defect branch; absence of an inward first variation cannot prove whole-disk univalence.
GAP: For the fixed C031c branch, identify candidate boundary roots and verify simplicity, real-IFT hypotheses, strict inward squared-modulus variation and noncancellation using fixed1307 boxes. These instance-specific checks have not been performed. Multiple/zero/tangential cases remain inconclusive within this first-order scope; no global sufficiency or effective radius is covered.
REASON: Essential analytic source coverage is now adequate for one bounded specialization after separate approval. No essential source blocker remains. Known theorems should be imported, with only root/normalization/sign hypothesis checks proved in the mathematical turn; no reproof of IFT or local mapping theory is needed.
SCOPE: Exactly the saved TARGET for C031c at u=400, its inherited tangent and fixed1307 actual boxes. First-order continuation of simple boundary roots only, poles distinguished from removable factors and critical points from derivative-numerator artifacts. Real C1 regularity suffices; no analytic tau dependence, monic fixed-degree normalization, higher-order expansion, weight/degree sweep, new quadrature, whole-disk sufficiency or all-branch classification.

## Original nomination1318 (historical, before review1319)

LITERATURE_REASON: Changed conclusion and hypotheses: certify an open-disk analytic obstruction for the new rational-map branch, rather than existence of solutions of six finite equations. Root persistence, possible rational cancellations and univalent-map necessity require coverage outside assessment1316.

The main gap remains actual-Xi all-degree positivity. A strict pole or
critical-point obstruction would park this particular realization; absence
of such an obstruction would merely retain it for a separately justified
global test. First-order radial displacement must have a strict sign:
tangential/zero displacement is inconclusive, not permission for a
higher-order expansion under this scope. Preserve the local branch result
even if analytic admissibility fails. Do not infer a global family stop
or RH conclusion from a fixed-u branch obstruction.

Continuation inputs: C031a,C031b,C031c and C030z's fixed1307 boxes,
with L025,L027 and inherited L019,L021,L036,L037,L917 contracts.
The local branch is qualitative, with no effective tau radius or
uniform radius over input boxes. Whole-disk holomorphy/univalence,
larger blocks, singular branches, actual identification and initialization
remain open. No RH or cross-notebook premise.

Before calculation, review primary theorem hypotheses, rational-map
exception cases and relevant Grunsky-named local failures. Reuse known
IFT coverage only where it actually applies. No pole, derivative zero,
first variation or sign is computed or asserted here. Full matching
Mathlib coverage remains unchecked. The next routing is standard theorem
comparison; this bounded obstruction test is not a creative whole-disk
construction. No independently specified sufficient analytic construction
is yet ready to justify such a creative nomination.

## Completed literature-only review1319 — 17 November2026

The exact target above is retained. The main gap is actual-Xi all-degree
positivity in L030–L032/C032a. This is a necessary analytic-admissibility
test of one finite realization, with a possible downstream use in a
separately proved Grunsky positivity transfer. It cannot establish that
transfer. No boundary root, first variation, radial sign, new lemma or
mathematical script was computed in this source review.

### Inspected sources and applicability

O. R. B. de Oliveira, *The Implicit and the Inverse Function Theorems:
Easy Proofs*, Real Anal. Exchange39(1)(2013/2014),207–218,
[arXiv1212.2066v1,10 December2012](https://arxiv.org/html/1212.2066v1),
Section3 Theorem2: a C1 map on a real open product neighborhood, a base
zero and invertible dependent derivative give a unique local C1 graph,
with derivative minus the inverse dependent derivative times the
independent derivative. Read the theorem and full proof: local
injectivity, derivative normalization, scalar elimination/induction,
chain-rule formula and uniqueness. Section2 defines differentiability
with an o(norm) remainder and states the real mean-value theorem.
Reuse1316's earlier extraction. For a candidate complex root, use real
and imaginary parts as the two dependent variables; the future check
must verify that Jacobian is invertible. This avoids assuming analytic
parameter dependence or a constant polynomial degree. For a radial
sign, apply ordinary differentiation to the squared modulus, then
justify the strict one-sided sign using that remainder definition or
the mean-value theorem. No root Jacobian or radial derivative for this
family is evaluated here. Multiple roots do not meet the simple-root
method's hypotheses.

L. V. Ahlfors, *Complex Analysis*,3rd ed.,McGraw-Hill,1979,
[Chapter2 Section1.4,p30,(11); Chapter4 Section3.3,Theorem11,
pp131–133](https://people.math.gatech.edu/~mccuan/courses/6321/lars-ahlfors-complex-analysis-third-edition-mcgraw-hill-science_engineering_math-1979.pdf).
Read the reduced-rational-function discussion, quotient derivative,
local-mapping statement and its proof/converse. Denominator zeros
represent poles after common factors are removed. The quotient
formula applies off denominator zeros; its unreduced derivative
expression may contain cancellations. For an analytic function whose
value difference has a zero of order n, the local mapping theorem
counts n nearby preimages. Its proof uses the argument principle on
a small zero-free boundary and excludes other nearby derivative zeros.
The converse on p133 forces n=1 for local injectivity, hence a nonzero
derivative. An interior derivative zero of a holomorphic map therefore
obstructs injectivity. This is a necessary condition; its converse is
not global injectivity. The future specialization must distinguish an
actual pole from a removable point, and a derivative zero from a point
where the quotient is undefined. A boundary obstruction must enter
the open disk: a zero remaining on its boundary does not suffice.

The existing assessment1314 inspected Ponnusamy–Wirths1704.08184v1,
Theorem1/proof/Remark1. Reuse its caveat: a sufficient criterion for
meromorphic univalence can allow a pole. The current goal is the
holomorphic disk class needed by the intended signing argument.
A certified pole stops that realization only, without any assertion
about meromorphic univalence or a changed normalization.

### Bounded mathematical specialization authorized by this coverage

Use only C031c's existing branch and tangent. At the mathematical turn,
form the denominator and the quotient derivative exactly from C031a's
stated rational map, using Ahlfors(11); check potential cancellations
before interpreting a zero. Locate the relevant roots at tau=0 and
verify simplicity individually. For each candidate simple boundary root,
verify the real C1 IFT hypotheses on an open neighborhood of zero and
apply its derivative formula. Use C031c's known first tangent; do not
compute its higher derivatives or solve the nonlinear branch again.

Compute only first derivatives of squared root moduli at zero, and
bound them with the unchanged fixed1307 boxes. A certified strictly
negative value, together with the verified pole/critical-point status,
may establish the nominated obstruction for every sufficiently small
positive tau. The mathematical write-up must explicitly justify the
strict eventual sign, denominator nonvanishing at a critical point,
and persistence of any required noncancellation. Existence intervals
may depend on the fixed actual tuple; no effective or box-uniform tau
radius is promised. If no strict obstruction is certified, including because a relevant root
is multiple, a radial derivative is zero/tangential, or a sign is not
certified by the fixed boxes, record the exact limitation and stop this
first-order test. Do not expand to
higher order, sweep parameters or infer branch nonexistence. A strict
outward motion of all inspected roots would still leave whole-disk
univalence undecided, since this test supplies no global sufficiency.

### Search, overlap and limits

Local searches were confined to Grunsky-named assessments/attempts and
the named1318/1311 histories, using pole, univalence, critical point,
boundary, simple root and radial terminology. Read C031c completely,
C031a's map/full-equation statement, C031b's tangent/actual bounds,
C030z's pertinent fixed1307 input context, and stops1307/1311.
Assessment1316 already covers coefficient existence. The stops concern
a different linear prescription, not this quadratic-defect branch.
No completed first-variation obstruction for C031c was found in the
bounded local comparison. This is not evidence of novelty.

External queries: `Ahlfors complex analysis one to one analytic function
derivative nonzero theorem pdf`; `simple root polynomial parameter
implicit function derivative root perturbation C1 theorem`; `Grunsky
rational function poles critical points unit disk univalence criterion`;
`"polynomial roots" "implicit function theorem" "complex" parameter
derivative`; `"rational functions" "univalence" "critical points"
"unit disk"`; `"Grunsky" "quadratic defect" "branch" "pole"`.
Search-only leads included a Paris-Saclay text Proposition14.3.2.1
on monic simple roots, Ian Tice's complex-analysis notes, and *Dimer
models and conformal structures*. Their theorem/proof passages were
not inspected and none is imported. The direct real IFT needs no monic
normalization, which is useful because polynomial degree may drop at
the base. There is no reason to delay this fixed test for those leads.
Ahlfors text was retrieved through the university-hosted PDF, including
all essential proof cases; two page-render timeouts did not block the
complete textual statements/proof. Search snippets are not evidence
for any mathematical conclusion.

Mathlib: reuse1315/1316's supporting implicit-function tools and links.
Full matching complex-root, rational-cancellation, injective-derivative
and Grunsky/actual-Xi branch coverage remains unchecked here; no
absence claim or Lean verification. This source review introduces no
canonical mathematical result to register in the DAG. A future canonical
proof must state all hypotheses, precise citations and these limits.

Continuation inputs: C031a,C031b,C031c,C030z fixed1307 boxes; actual
constants from L025 with L027 positivity, retaining L019,L021,L036,
L037,L917 and1307 inclusion/arithmetic contracts. L030–L032/C032a give
intended use, not an established positivity premise. Other regular,
singular/non-C1/fractional-power/zero/diverging-weight branches, larger
blocks, identification and initialization remain open. No RH or
cross-notebook input. Import the classical inputs; the future check is
REPRODUCTION specialization, not creative mathematics. No independent
sufficient whole-disk construction is specified, so there is no justified
creative target to nominate in this turn. Ready coverage is newly saved
and requires a separate approval before the calculation.
