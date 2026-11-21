# Compact gamma midpoint: source comparison1612

18 November2026. Literature-only step; no derivative estimate, new
lemma, mathematical script or quadrature evaluation is performed.

## Primary statements and proof cases inspected

Erik Talvila and Matthew Wiersma, *Simple derivation of basic quadrature
formulas*, [arXiv:1202.0249v1](https://arxiv.org/pdf/1202.0249v1),
1 February2012 (manuscript dated21 December2011), Section1, printed p.2,
equation(1.1) and the following composite formula; Section4, printed
p.8, complete midpoint proof and composite-rule paragraph. For
f in C^2([a,b]), n equal panels and their midpoints y_i, the source gives

    |integral_a^b f-(b-a)/n*sum_i f(y_i)|
        <=(b-a)^3*||f''||_infinity/(24*n^2).

Its proof integrates f'' against a continuous piecewise quadratic,
separately on the two half-panels, twice by parts. The polynomial and
its first derivative vanish at the outer endpoints; the derivative
jump at the midpoint supplies the node value. The final paragraph
sums this construction over the panels. Its later observation about
possibly singular endpoint functions supplies no bounded-second-
derivative guarantee and is not used here. No reproof is needed.

Douglas N. Arnold, *A Concise Introduction to Numerical Analysis*,
[author's notes](https://www-users.cse.umn.edu/~arnold/597.00-01/nabook.pdf),
copyright1999-2001, Chapter2 Section2, printed pp.58-59 (PDF pp.64-65),
Peano-kernel derivation and equations(2.3)-(2.5). The composite error is
integral f''(t)K(t)dt. On a panel [l,r], K(t)=(t-l)^2/2 to its midpoint
and (r-t)^2/2 thereafter. It is nonnegative, with panel integral
(r-l)^3/24; equation(2.5) gives the composite sup-norm estimate.
The proof uses Taylor's integral remainder and interchange with finite
evaluation functionals. This integral identity, rather than a single
real mean-value point, applies componentwise to complex f. Taking
the modulus under the integral preserves the same sup-norm constant.
This is source applicability, not a claim about C033a's derivatives.
The preceding scalar Taylor/Lagrange discussion on p.57 is unnecessary;
in particular, no choice of a continuously varying Lagrange point is
imported. The source is preliminary course notes, not a later edition.

OpenStax, *Calculus Volume2*, Section3.6,
[Theorem3.5, equation(3.12)](https://openstax.org/books/calculus-volume-2/pages/3-6-numerical-integration),
live page inspected18 November2026, independently states the same
midpoint bound under a bounded second derivative; it explicitly omits
the proof. It is corroboration, not the proof source or a complex
mean-value theorem. NIST DLMF3.5(i), equations3.5.1-3 and their C^2
hypotheses, concern trapezoidal rules and do not directly cover the
prescribed midpoint sum. No periodic or infinite-line exponential
convergence statement there is imported for this compact nonperiodic
family.

## Scope of the approved specialization

C033a(4) specifies I_(sigma,w)(v) on[0,16] with I(0)=w^2/4;
critical audit1611, equation(14), supplies its nonsingular A/B expression.
The new work must establish C^2 regularity including the right endpoint
derivatives at0 and a common bound on |partial_v^2 I| over the entire
closed set. Continuity alone is insufficient. Product/quotient rules
and differentiation of the compact A,B integrals are the proposed
elementary means; no such family estimate is proved in this review.

Once those hypotheses are paid, the cited remainder theorem is the
generic input. The exact finite rule, with exact function values, stays
at4096 equal panels. Test the resulting allowance against1/16, keeping
the symbolic factor16^3/(24*4096^2); no successful bound, simplified
derivative threshold or numerical feasibility is asserted here.
Panelwise derivative bounds with the cited kernel may also estimate
this same fixed sum, but do not authorize refinement or a changed rule.

The complete complex modulus must be bounded: no sign of I, reality
of w, common complex mean-value point or sampled maximum is allowed.
The task does not require a new quadrature theorem. Its difference
from the sources is the explicit uniform application to this family,
including its removable origin. The downstream component use retains
C032z's normalization, divisor multiplicities, no-ordinate-zero,
strip/counting qualifications and C032j/m/q's additional finite-zero,
heat and fixed-v1 qualifications for probability use. This review does
not verify their external source data.

## Duplicate and obstruction comparison

Targeted local reads: C033a and C032z's displayed hypotheses/formulas;
L036 in full; L953's hypotheses, fixed rule and analytic error;
assessments1608/1609 and source-notes1608's quadrature exclusions;
the recorded stops1576/1581/1586; dictionary assessment1570's exact
target. A scoped filename/text search of18 November gamma, spectral
and variation notes found no completed version of this uniform compact
midpoint bound. This is a bounded duplicate check, not a novelty claim.

L036 integrates a real C^8 Taylor polynomial through degree6, with an
eighth-derivative allowance: its rule is not the midpoint-value-only
sum. L953 concerns a different actual residual and weighted
Gauss-Chebyshev rule; its zero-containing result cannot estimate this
gamma component. Stop1576 is about C032w's expanding-disk bounds;
stop1586 is about literal separate digamma-series allowances, and
stop1581 lacks certified divisor coordinates for that finite evaluator.
None proves this compact rule infeasible or supplies its bound.
The present component does not itself pay their other missing inputs.

## Bounded external search and limits

Queries executed18 November2026:

- `site.dlmf.nist.gov 3.5 midpoint rule error remainder`
- `midpoint quadrature Peano kernel complex valued function remainder second derivative`
- `"exp(-sigma" "cosh" "midpoint" gamma quadrature`
- `"digamma" "midpoint rule" error bound complex`

The first two located the generic remainder sources above; the latter
two returned no inspected full match to this parameter family. This
does not establish originality. Stronger/changed-rule leads include
corrected trapezoidal formulas and analytic Gaussian quadrature;
they change the finite rule and are outside this fixed benchmark.
Talvila-Wiersma's bounded C^2 theorem is sufficient as the generic
remainder input; no stronger theorem is essential for attempting the
stated test. The endpoint-singular observation is not permission to
ignore origin regularity or to change norms without proof.

The Victoria University repository lead *Midpoint Type Rules from an
Inequalities Point of View* returned an access-denied page at
`https://vuir.vu.edu.au/17275/1/MidIneqAnasRep.pdf`; it was not read or
relied upon. This is nonessential because the primary proof above is
accessible. Search snippets and unrelated digamma leads are not inputs.
The two PDF proof pages were also requested as screenshots; the
load-bearing statements and proof cases were inspected in full text.

Full matching Mathlib coverage remains unchecked/unknown. No new
Mathlib-absence claim is made. No generic theorem is being reproved;
future canonical work should cite the sources and prove only the
family-specific hypotheses and effective estimate.

## Decision and continuation test

SPECIALIZE: essential generic remainder coverage is ready. Continue
with precisely the saved fixed-domain test. Record a rigorous common
allowance and compare it with1/16; an allowance at least1/16 makes
this proof attempt inconclusive, not the actual quadrature error
large. Preserve the result without automatically increasing panels,
shrinking the parameter set or launching a dictionary optimizer.
No local derivative bound has been derived and approved in this turn.
The analytic tail is already separately audited in C033a; it is not
part of this compact error. Node arithmetic, pole/prime/O evaluation,
coefficient amplification and the actual residual<1/2 are independent
unpaid obligations. Signed upper control, unsmoothed Xi realization
and actual-Xi all-degree positivity remain open.

## Recovery1613 — direct source URL field

18 November2026. The supervisor reported that the ready assessment
needed a direct source URL. The primary links above were in these
notes but absent from the assessment's SOURCE_EVIDENCE field. That
field now includes both exact PDF URLs. Direct opens succeeded;
Talvila-Wiersma Section1 p.2 and the complete Section4 p.8 midpoint
proof, and Arnold Chapter2 Section2 pp.58-59 through equations(2.3)-(2.5),
were rechecked. The integral-kernel argument, rather than Arnold's
preceding scalar mean-value discussion, remains the applicability
input for complex tests. Screenshot requests returned no usable
images in this session; the complete relevant text was inspected.
No new theorem, stronger estimate, changed hypothesis or source
blocker emerged. Reuse the prior duplicate/failure comparison above;
no broad search was repeated and no novelty inference is made.

This is a STALLED process repair with no mathematical advance and no
new source-readiness claim. The fixed target and SPECIALIZE scope
are preserved for the next invocation's gate. No lemmas or scripts
were written; Mathlib coverage remains unknown. The next task must
pay the full-domain C^2 and derivative obligations before invoking
the existing generic remainder, retaining all inherited qualifications.
