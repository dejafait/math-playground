# Actual unshifted Jensen hyperbolicity — bounded mechanism discovery

TARGET: Discover at most three mechanisms for actual unshifted Jensen hyperbolicity beyond fixed-Gaussian prescribed grids, compare their primary theorems and recorded failures, and nominate one bounded actual-coefficient test.
CHECKED: 2026-11-04
DECISION: EXPLORE
SEARCH_EVIDENCE: Step385 compared exactly three mechanisms: shifted/prescribed-primitive transfer, finite-free/Appell representation, and coefficient Toeplitz comparison. Reused step379/381 coverage; exact source identifiers, q-Pascal, finite-free, Appell and coefficient-Toeplitz searches in local assessments/failures found no earlier exact selected test. External queries and inspected passages are recorded below; no novelty inference.
SOURCE_EVIDENCE: Reused O'Sullivan 2007.13582v2 product/large-shift and step379 primitive comparisons; inspected Campbell 2412.20488v3 Sections1.4,2.1, Theorems2.1/2.3 and their proofs in4.2/4.3; Katkova math/0505174v1 pp.4–9, TheoremsASWE/C/2/3/D and fixed-order reduction; Michałowski 2607.16795v1 Theorem1.1, Sections4–6 with full relevant proofs, Remarks8.1–8.3; O'Sullivan Theorem1.4/(1.8), Section7/(7.3)–(7.14) coefficient application.
COMPARISON: Shift descent still lacks prescribed actual signs; Campbell assumes LP or real-rooted inputs. Coefficient Toeplitz comparison is distinct from L763/L764, but its stated k>=10^18 r^3 theorem leaves bounded k/r untouched. Its exact q-Pascal error matrix and O'Sullivan's arbitrary-fixed-order actual coefficient asymptotic support a bounded applicability test, not an import of signs.
GAP: No all-degree actual hyperbolicity or signed minor estimate is obtained. The selected question is whether the unchanged sufficient norm<1 comparison survives along k=1024r; the actual endpoint log defect, error amplification and eventual q range remain uncalculated.
REASON: The source search yields one independently testable actual-coefficient continuation with a decisive threshold. Test that mechanism before investing in stronger signed comparison; do not repeat the stopped Hermite grid or assert an independently justified creative cancellation estimate.
SCOPE: Completed literature-only discovery and one later calculation nomination; no new mathematical derivation, lemma, numerical search or mathematical script. The separate q-Pascal endpoint assessment must receive continuation approval before mathematical work.
LITERATURE_REASON: The supplied REVIEW_REQUIRED target lacked essential new-mechanism coverage; unchanged primitive/product/large-shift coverage was reused and only the newly relevant primary interfaces were inspected.

## Exact object and relevance

Use the actual K and moments from L019/L021 and the factorial normalization
in L763:

    Theta(z)=sum_(j>=0) M_(2j) z^j/(2j)!,
    g_d^*(Theta;X)=sum_(j=0)^d binom(d,j) gamma_j X^(d-j),
    gamma_j=j! M_(2j)/(2j)!.

The gap is all-degree actual hyperbolicity, an interface to the main RH
gap through the already assessed Jensen/product criteria. A proposed
intermediate estimate may address only part of that gap, but must name
the remaining independent assumptions. Do not use actual hyperbolicity,
RH-equivalent positivity or the desired signs as available inputs.

L763 and audited L764 are exclusions of specific sufficient tests, not
global prohibitions. Their full mathematical stop evidence is preserved
in their canonical files and the existing ATTEMPTS records. The new
search must compare a candidate's mechanism with those stops and relevant
notebook-local failures before recommending it. Renaming a grid, checking
more degrees or extending the same residue hierarchy is not an independent
test. No cross-notebook theorem is needed or nominated.

## Required bounded output and gate

Search precise candidate statements and standard terminology, and read
primary theorem hypotheses and the essential proof cases. Reuse existing
assessments where applicable. Compare at most three distinct mechanisms;
do not undertake a general survey or derive any new mathematics. The
output should nominate one explicit actual-coefficient statement, its
essential input IDs, its plausible use for the central gap, and a finite
or symbolic test with a decisive failure condition. A known import or an
informative obstruction is acceptable; novelty is not required.

Continue to a mathematical attempt only after source coverage supports
that exact statement and its bounded test. If a proposed mechanism merely
renames the target-equivalent sign condition, reject that candidate with
the specific missing estimate. Preserve any informative source blocker
and prefer an independently testable alternative. A creative nomination
is justified only by a concrete new mechanism and bounded test, not by
the elapsed number of turns. Until then theorem comparison is the actual
task until coverage is ready. The completed review below supplies one
separately assessed continuation, which awaits its own approval; no
mathematical result is asserted. Mathlib coverage remains unchecked.

## Completed bounded discovery — step385

Main gap: all-degree hyperbolicity of the actual unshifted family, or
equivalently the still-unproved actual-Xi positivity interface. This
review establishes no signs. It nominates an applicability test of one
different sufficient comparison, not a new equivalent criterion.

Exactly three mechanisms were compared:

1. **Shift descent by prescribed primitives.** Reuse
   `2026-11-04-theta-jensen-prescribed-primitive-margin.md` (step379),
   including Pereira v2 Lemmas1.1–1.2, Dimitrov–Kostov Theorem1 and
   O'Sullivan v2 Theorems1.3/3.5/8.1. A selectable primitive constant
   is not the prescribed gamma_n. Input root reality, signed critical
   values, repeated-root compatibility and descent initialization
   remain missing. Finite verified unshifted degrees and large-shift
   estimates do not cover every unshifted degree. No changed input
   warrants reopening this transfer. L763/L764 remain narrower stops.

2. **Finite-free/Appell representation.** Andrew Campbell,
   [arXiv:2412.20488v3, 18 December 2025](https://arxiv.org/html/2412.20488v3),
   Section1.4/(1.22)–(1.26), Theorems2.1/2.3, proofs4.2/4.3.
   Theorem2.1 assumes an LP product with real nonzero x_j,
   sum x_j^(-2)<infinity, real c,sigma and f(0)=1. Theorem2.3 starts
   with monic real-rooted p_d, convergent first moments, second
   moments Theta(d), and convergence of the weighted rescaled root
   measures to the stated real-root LP measure. Its conclusion is
   fixed-degree derivative convergence. The proofs use the real-root
   measures and reciprocal real x_j; their positivity is not recovered
   from arbitrary formal coefficients. Normalizing f=Theta/gamma_0
   gives the actual Appell family algebraically, but does not establish
   the LP hypothesis. Reject automatic transfer or a free-ID measure
   asserted solely from formal cumulants. No independent realization
   of those measures is provided. The publisher's DOI10.4171/DM/1071
   confirms the 2026 publication; theorem numbering here refers to v3.

3. **Actual coefficient Toeplitz comparison.** Olga Katkova,
   [arXiv:math/0505174v1](https://arxiv.org/pdf/math/0505174), printed
   pp.4–9, TheoremC, Theorems2/3 and the consecutive-minor reduction,
   distinguishes PF_infinity from fixed-order eventual positivity.
   Theorem3's multiplier parameter depends on the order; it is not one
   all-order certificate. The PDF bears the v1 identifier and a later
   title-page date; citations identify the inspected version/pages.
   Wojciech Michałowski,
   [arXiv:2607.16795v1, 18 July 2026](https://arxiv.org/html/2607.16795v1),
   Theorem1.1 states D_(r,k)>0 for integers r>=2, k>=10^18 r^3.
   Sections4–6 use an exact q-Pascal factorization and a sufficient
   norm<1 perturbation test; all relevant finite-algebra, nonlinear
   majorant and inertia proof cases were read. Remark8.2 explicitly
   leaves k=O(r) outside the method's proved range. The full analytic
   GateA and ancillary certificates were not audited or replayed;
   no certified constant is imported as a local result. Coefficient
   Toeplitz positivity differs from a continuous kernel's PF order and
   from the earlier fixed-Gaussian Jensen tests.

Select mechanism3's exact comparison, with its norm threshold unchanged.
The actual scalar endpoint defect along k=1024r is a finite-expression
asymptotic question before any matrix-size experiment. Its source scope
and discriminating test are in
`2026-11-04-actual-toeplitz-qpascal-endpoint.md`. The arbitrary-fixed-order
actual gamma asymptotic of O'Sullivan Theorem1.4 is available for this
purpose; Section7/(7.3)–(7.14), including the exponential theta-tail
case and Stirling conversion, was inspected. An asymptotic remainder
must be controlled at its integer arguments, never differentiated.
No value or sign of the proposed limit has been calculated here.

This nomination is a known-method specialization, routed calculation,
not a creative all-degree proof. A protected creative nomination is
currently blocked by the absence of an independently justified signed
cancellation or realization estimate. The precise norm test can decide
whether further investment in this unchanged model is warranted.

## Search and overlap record

Queries included `Jensen polynomials Riemann xi function unshifted
hyperbolicity sufficient condition total positivity Turan O Sullivan`,
`finite free convolution Jensen polynomials Appell sequences real
rootedness cumulants`, `Riemann xi function total positivity coefficients
Toeplitz Schoenberg frequency sequence`, `Riemann Katkova multiply
positive coefficients`, and exact 2607.16795/q-Pascal/1024 and
xi/Toeplitz/quadratic-perturbation queries. Hutchinson/ratio searches
yielded no inspected candidate and were not pursued as a fourth
mechanism. Search snippets and unrelated hits supply no theorem.

Local searches covered the active notebook's literature, ATTEMPTS and
foundations for exact source IDs, finite free, Appell, q-Pascal,
signature whitening and coefficient Toeplitz terms. The prime-power
circle-measure Toeplitz tests concern different coefficient sequences;
no theorem was transferred from them. The step379 primitive assessment,
step381 Hermite-grid assessment, L019/L021/L028, L763 and the L764
ATTEMPTS summary were read or reused; L764's completed audit was not
repeated. L560's reciprocal-density shape countermodel is a contrast,
not a coefficient-PF obstruction. No sibling notebook was read.

Mathlib: not checked for the new Toeplitz/finite-free interfaces;
unknown availability is not evidence of absence. No mathematical
script, lemma, DAG edge or PROOF argument changes in this review.
