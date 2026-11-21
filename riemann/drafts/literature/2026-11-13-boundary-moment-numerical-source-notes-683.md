# Boundary-moment numerical source comparison683

LITERATURE_REASON: Saved assessment682 is REVIEW_REQUIRED: the quantitative moment/error/work target was explicitly excluded by analytic assessments678/680. This is one essential literature-only step, not another identity audit.

## Initial source checkpoint and scope

The supplied overview/DAG preceded reads of C998i Sections1-3 and the
endpoint-data passage, C998g hypotheses/Section1, C998a hypotheses and
parity-map opening, and C999q's exact neutral completion. Reused source
comparisons658/670/675/679/681 and prescription stops660/662. The
notebook-scoped git status exposed substantial pre-existing unfinished
work; none is altered or discarded. No witness or mathematical script
has been loaded or executed. No cross-notebook result is used.

Primary source now retrieved: Johansson, *Numerical integration in
arbitrary-precision ball arithmetic*, arXiv:1802.07942v1,22February2018,
Sections2/2.1 (printed pp2-3). This requires interval evaluations and
explicit analytic-domain checks for quadrature bounds; output precision
and adaptive tolerances do not themselves certify the final contraction.
Endpoint treatment, finite arithmetic and total scalar cost still need
the comparison below. The initial mistyped URL1802.07946 retrieved an
unrelated physics paper; it is not mathematical evidence or an input.

The stable Arb2.23.0 acb_calc API was retrieved. Its bounded-path
requirement and cumulative-error qualification matter. The current
FLINT3.7.0-dev algorithm page advertises October2026 LLM-assisted
documentation revision; it is a lead only, not the basis for importing
error constants or cost claims.

No local specialization, new bound, evaluator, precision, panel schedule
or square entry was derived at this initial checkpoint. The completed
comparison follows. This file records source evidence, not a proof of
the requested numerical service.

## Search and earlier overlap

Queries used combinations of `Johansson Numerical integration arbitrary
precision ball arithmetic 2018 Petras rigorous`, `certified quadrature
logarithmic endpoint singularity oscillatory integrals error bound ball
arithmetic`, `Carleman cosine logarithmic moments rigorous quadrature
finite interval`, `Petras 2002 self validating integration analytic
functions error bounds`, `Johansson computing dilogarithm rigorous ball
arithmetic paper`, and restricted searches of arblib.org and DLMF25.12.
No matching theorem for this complete fixed square service was identified;
this bounded search establishes neither absence nor originality.

The exact reused inclusion/quadrature assessment is
`drafts/literature/2026-11-12-graded-full-residual-norm-review-655.md`,
completed comparison656; there is no separate source-notes656 file.
Read its completed primary-source passages and concise history656.
Reuse its inspected Trefethen19.3 proof and scalar inclusion coverage,
and658's elementary Taylor/rational evaluation coverage. The numerical
service now has independent single-density moments from C998i/audit682,
which those older norm and point-service targets did not have.

Stops652/657/660/662 concern their specified full-action/pointwise
prescriptions; C998g/672 stops its direct tensor contraction. Their
costs do not transfer to this coefficient-moment mechanism. Source
stops673/675 concern hierarchical or displacement imports, not this
quadrature theorem. None is reopened or erased. In particular, this
review does not repeat a Si/Ci uniform-point service at another threshold.

## Primary evidence actually read

**Interior integration and endpoint treatment.** Johansson,
*Numerical integration in arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1),22February2018:
read Sections2/2.1, pp2-4, every algorithm branch and tolerance/evaluation
limit qualification, plus Section3.2 and its notes, pp6-7. Complex-box
evaluation must check analyticity, especially branch cuts. Improper
integrals require manual truncation with separately supplied tail bounds.
The output radius controls accuracy; requested tolerances need not be
achieved. Evaluation counts exclude the cost of a function call, and
benchmark timings omit first-time node setup. These are known tools and
limitations, not a fixed-data error or scalar-work theorem.

Arb2.23.0 [acb_calc API](https://arblib.org/acb_calc.html): read the
callback contract, complete integration/tolerance paragraphs and options
through evaluation/degree/depth limits. A finite result needs bounded
values on a finite path; analytic calls must reject inappropriate boxes.
Working precision is not automatically increased. Cumulative uncertainty
can exceed the input tolerances. No invocation of an adaptive API alone
can pay the requested complete-entry error or total scalar count.

Reuse Trefethen, *Approximation Theory and Approximation Practice*(2013),
Chapter19 Theorem19.3/(19.8), complete proof as inspected655/656/670:
[book PDF](https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf),
PDFpp153-154. For a bounded holomorphic continuation to E_rho, rho>1,
bound M, the(n+1)-point Gauss rule has error at most
(64/15)M*rho^(-2n)/(rho^2-1), n>=1. Affine interval scaling and the
actual point-count convention are essential. No singular-endpoint
extension is imported. No reproof is justified.

**Weight primitives and branches.** NIST DLMF,
[25.12(i)](https://dlmf.nist.gov/25.12#i), inspected equations25.12.1-4
and the principal-branch paragraph. Its defining integral, power series,
Landen relation and inversion formula are precise available citations
(underlying references: Maximon2003,(2.1),p2807 and(3.1),(3.2),(3.4),
p2808). The series applies on the stated unit disk; transformations
have their displayed exclusions and principal logarithms. These supply
tools for identifying and enclosing C998i's D, not a proved local
complex extension or cancellation bound for Q. No weight identity or
endpoint formula is newly derived here.

Read the complete Arb2.23.0
[dilog_zero_taylor.c](https://raw.githubusercontent.com/flintlib/arb/2.23.0/acb_hypgeom/dilog_zero_taylor.c),
especially lines184-222: a magnitude geometric tail is divided by n^2
and explicitly added after the finite sum; a nonfinite tail produces an
indeterminate result. Its precision heuristic is not an accuracy theorem.
Read
[dilog_transform.c](https://raw.githubusercontent.com/flintlib/arb/2.23.0/acb_hypgeom/dilog_transform.c)
branches1-4, lines20-106, against the cited transformation domains.
Branches5-7 were inspected only as unused implementation alternatives;
their continuation dependencies are not approved inputs. These reads are
not an exhaustive verified build. The bounded test may use the cited
series/transformations with explicit interval tails and counted arithmetic;
it must not hide a library's uncounted method-selection or subroutine work.

**Arithmetic and quadrature setup.** Reuse655/656's Johansson,
*Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval Arithmetic*,
[author paper](https://fredrikj.net/math/arbpaper.pdf), Sections3.2,4,5-5.3,
pp6-9: outward error propagation plus rounding preserves inclusion, not
accuracy or stability. Also inspected the pinned
[arXiv:1611.02831v1](https://arxiv.org/pdf/1611.02831v1),9November2016,
Section4, p6, multiplication example: midpoint and radius arithmetic both
have costs. Neither paper supplies this service's primitive ledger.
Reuse658's inspected elementary-function source; a simpler finite
Taylor/rational interval implementation is permitted if its local
truncations and all costs are paid. No optimized library speed is assumed.

Johansson--Mezzarobba, *Fast and rigorous arbitrary-precision computation
of Gauss-Legendre quadrature nodes and weights*,
[arXiv:1802.03948v1](https://arxiv.org/pdf/1802.03948v1),12February2018:
read Section1 equations(1)-(4), Theorem1 and proof sketch, pp1-3;
Section2 through Proposition3 and its full proof, pp3-5;
Section3 opening recurrence(9), p6. Real Legendre roots and the derivative
weight formula give the rule; polynomial evaluation and interval derivative
bounds support enclosure refinement. Theorem1 assumes p~n and gives an
asymptotic bit-operation result, not the current scalar cap; its sketch
is NOT imported as a complete concrete complexity certificate. Petras's
asymptotic starting intervals and later high-order evaluation algorithms
were not inspected here and are not needed if all nodes are explicitly
isolated in disjoint sign brackets and refined with counted interval or
rational polynomial arithmetic. Such brackets/refinement still need to
be supplied. A seed or approximate root alone is not a certified node.

## Stronger singular-rule comparison and unread leads

Okayama--Arakawa--Kamigaki--Yabumoto, *Explicit error bounds of the SE
and DE formulas for integrals with logarithmic and algebraic singularity*,
[arXiv:2411.19755v2](https://arxiv.org/pdf/2411.19755v2),3December2024:
read introduction/domain definitions, Theorems2.3/2.4, equations(2.2)-(2.6),
and their constants, pp4-7. Both need analyticity on the specified image
of a complex strip and a global bound K|z|^(alpha-1)|T-z|^(beta-1)|log z|,
with positive K,alpha,beta,d and their mesh/size restrictions (d<pi for
SE,d<pi/2 for DE). These are quantitative singular quadrature theorems,
but no such domain/bound or finite-arithmetic ledger for Q is established
locally. Their proofs and later revisions were not inspected: these are
comparison statements only, not an imported theorem or approved DE
fallback. A faster nominal convergence rate is not the required scalar
cost. No claim of inapplicability or impossibility is made.

The BEM oscillatory/Filon-Lobatto, Mastroianni--Monegato product-rule,
and Petras2002 search hits remain unread leads. The prior inaccessible
Petras source is not an essential dependency: Trefethen and the inspected
primary arithmetic sources suffice for the selected bounded test.
No persistent source blocker remains. No general oscillatory theorem is
needed when the finite frequencies are retained in a certified complex
bound. Their size must actually be paid; analyticity alone is insufficient.

## Decision for the unchanged target

SPECIALIZE: source coverage is sufficient for one separate REPRODUCTION
attempt using manually bounded endpoint strips, finitely prescribed
interior Gauss panels, enclosed weight primitives and finite arithmetic,
then the exact C998i entry formulas and frozen-column contraction. This
is a method family whose parameters must be fixed by the attempt, not a
claimed feasible prescription or authorization for repeated parameter
sweeps. No source proves this square service verbatim. The difference is
its effective constants, stable local evaluation, contraction and work.

The permitted attempt must discharge all of the following, before a
large evaluation. These are obligations, not new mathematical results:

1. Fix ONE complete endpoint/interior prescription, degrees, precision
   and primitive evaluator. Use C998i's existing real majorants to pay
   every omitted strip for q_n and chi_n, including denominator weights.
   If trimming near a is used to avoid removable-endpoint cancellation,
   pay that strip too; do not evaluate the undefined separated Q/Aj
   expressions at a or assert a complex continuation from a real limit.
2. Prove actual branch-safe holomorphic neighborhoods and explicit bounds
   for each retained panel and every required frequency through255.
   Pay complex oscillatory growth and input uncertainty. If using the
   DLMF primitive identification, justify it from the cited definitions
   and domains; no change of branch or cancellation is assumed.
3. Enclose ALL undotted/dotted moments and endpoint data in C998i(4),
   J and constants. Propagate all errors through(6)-(8), including
   lambda_n*dot H_n, the full W and V brackets at BOTH endpoints,
   all four diagonal residues and separate mode zero. Entry cancellation
   may require guard precision; a small moment error is not the output
   guarantee. Retain nu_n*nu_m/2 and C998g's scoped square coefficient.
4. Enclose the unchanged binary-rational free columns with C999q exact
   neutral completion and normalization, then the complete S_ij for
   both parities and every column product. Common weights/nodes may be
   cached once only with their setup and error propagation accounted for.
   The final tolerance is1e-10 per complete S_ij, not per moment or B_nm.
5. Count every scalar operation under C998g's convention: constants,
   sign-isolated nodes/weights, primitive series/transforms, argument
   reductions, midpoint/radius arithmetic, moment accumulation, endpoint
   products, coefficient completion and final contraction, including
   initialization, comparisons and assignments. Charge complex and
   interval operations by their real primitive work, not as one call.
   All required setup belongs to this service; reserve C998f separately.

Continue only if the full error bound is<=1e-10 and the complete scalar
work bound is<=20000000. A rigorous lower bound already exceeding the
cap may stop the prescription early. An unaffordable sufficient schedule
also stops that schedule, without a universal lower-bound claim. Stop
at the first unpaid error or required setup source. If the pre-batch
test passes, any ensuing computation still needs complete enclosure
evidence and an independent audit; no square has been evaluated here.

The exact saved TARGET and witness pin are retained in assessment682.
C998i/audit682, C998h/audit678, C998a(4)/audit655, C998g Section1/audit674
and C999q exact Z are essential; C998e(6)-(8) is used only in that scoped
audit. The original operator/source contracts remain conditional and
unreplayed as recorded there. A-square, both mixed terms, projection,
full100000000 work, inverse/residual debt, signed S3 and Xi assembly
remain independent gaps. Full matching Mathlib coverage is unchecked.

This review clears an essential source gate, not a mathematical advance
in a bound or sign. It does not justify a creative central S3 mechanism:
the audited square representation supplies no signed coupling comparison.
No lemma, mathematical script, PROOF or DAG change is warranted. The
next action remains exactly the existing quantitative target, rather
than a newly invented continuation requiring another discovery review.
