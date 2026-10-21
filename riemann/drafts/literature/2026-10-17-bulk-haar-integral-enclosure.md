# Source assessment: certified enclosure of the prescribed bulk limit

TARGET: Determine whether L426's fixed limiting integral I is nonzero by a rigorous enclosure retaining the exact mixture, multiplicative response and both prescribed branch stages.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 187 searched validated integration with discontinuous selectors, random Euler products with interval arithmetic, and Schur--Horn Gaussian integration; inspected Johansson arXiv:1802.07942v1 Section 2 and Rump Acta Numerica 19 Sections 5.5, 6 and 7.1; checked L424's step-175 screen, its ATTEMPTS stop, L425's ties and L422/L423's exact coefficient/tail construction. No inspected source evaluates this particular integral; failed searches establish no novelty.
SOURCE_EVIDENCE: Johansson, Numerical integration in arbitrary-precision ball arithmetic, arXiv:1802.07942v1 (22 February 2018), Section 2 pp. 2--3, direct-box step 2, analyticity-tested Gaussian step 3 and Section 3.2 p. 6; Rump, Verification methods: Rigorous results using floating-point arithmetic, Acta Numerica 19 (2010), 287--449, corrected author PDF Sections 5.5 (5.16)--(5.17), pp. 27--28, Section 6 pp. 29--30 and Section 7.1 p. 33; reuse the Kowalski Euler-log assessment through audited L426, without a new value-distribution theorem.
COMPARISON: Standard interval inclusion and validated finite-interval integration cover enclosure machinery, not the value of I. L426 already supplies the exact product law and full uniform response majorants; L425 supplies the prescribed branch domains. Their quantitative enclosure with L423's exact coefficients is the remaining specialization; no new general integration or equidistribution theorem is needed.
GAP: Produce a total enclosure with exact coefficient intervals, all multiplicative-response tails, finite-cell integration error and both selector stages included. Neither useful numerical width nor exclusion of zero is established by this review; dimension and interval dependency may defeat the bounded implementation.
REASON: The enclosure target required essential integration coverage beyond qualitative averaging; this separate literature-only review now permits one bounded mathematical attempt using standard inclusion methods. Do not infer a sign or efficient convergence from the method approval.
SCOPE: Only the exact TARGET for L426's I at sigma=5/2 and unchanged k=13,14 mixture, using finite-prime or multiplicative Dirichlet truncation with a uniform full tail, certified cell ranges, and explicit treatment of both ordered branch stages. Optional analytic quadrature requires certified complex domains; it is unnecessary for direct range integration. No alternate basis, fitted coefficient, free composite phase, or growing-height sign assertion.
COVERED_TARGET: Determine whether L426's fixed limiting integral I is nonzero by a rigorous enclosure retaining the exact mixture, multiplicative response and both prescribed branch stages.

LITERATURE_REASON: The changed observable is a certified value of the fixed limiting integral, whereas the ready preceding assessments cover qualitative averaging and its critical audit only. The required interval-integration source was previously unread.

## Intended input and relevance

The main RH gap is global mixed positivity. The intermediate target is
a certified nonzero value, of either sign, for the one specified integral
in L426. L424, audited L425 and audited L426 show its prospective use:
a nonzero I would distinguish the complete L423 law from trajectory
occupation laws agreeing on this observable up to o(1). It would not
invalidate L423's selected-moment obstruction, evaluate actual clipping,
or supply the quantitative full-error regulator margin in L413.

Essential inputs are L426's exact integral and full-response annulus,
L423's exact alpha/theta_j/C_j coefficients, L419's prescribed ordered
two-stage rule, L425's finite diagonal-tie set and branch controls,
and L424's exact Q and trajectory bound. L368/L369/L390 enter through
the audited actual-height reduction, not as an extra independence
assumption. Keep the existing numerical failure in
`ATTEMPTS/2026-10-17-gaussian-jet-trajectory-diagnostic.md`.

## Primary sources actually inspected — step 187

1. Fredrik Johansson, *Numerical integration in arbitrary-precision ball
   arithmetic*, [arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942),
   22 February 2018. Read Section 2, pp. 2--3, including the complete
   four-step algorithm and tolerance qualifications, and the manual-tail
   restriction in Section 3.2, p. 6. The callback must enclose the function
   over its whole argument box. With its regularity flag set, it must
   additionally certify analyticity or return a nonfinite result. The
   Gaussian bound assumes analyticity and a modulus bound on an enclosing
   complex ellipse. Step 2 instead integrates a whole-segment range bound;
   step 4 bisects. Evaluation limits may leave a wide valid enclosure:
   requested tolerance is not an achieved error bound. Infinite intervals
   and omitted tails require separate manual bounds.

   Applicability: direct range integration does not demand continuity at
   L419's ties. Gaussian acceleration is optional and cannot cross an
   uncertified selector branch or square-root cut. This univariate
   algorithm is not cited as an automatic high-dimensional product-law
   solver; any nested use must enclose all outer parameters. A floating
   inner integral is not an interval callback.

2. Siegfried M. Rump, *Verification methods: Rigorous results using
   floating-point arithmetic*, Acta Numerica **19** (2010), 287--449,
   DOI [10.1017/S096249291000005X](https://doi.org/10.1017/S096249291000005X),
   [corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
   accessed 17 October 2026. Page references here use its internal
   numbering: Section 5.5, pp. 27--28, inclusion property (5.16) and
   inclusion principle (5.17); Section 6, pp. 29--30, dependency failure
   and interval Newton Theorem 6.2 with its proof; Section 7.1, p. 33,
   exact input conversion. Successive valid interval operations enclose
   an arithmetic expression on a box, with division excluding zero.
   Repeated variables can produce severe overestimation. Ordinary decimal
   or transcendental floating inputs wrapped afterward need not contain
   their intended exact values. Theorem 6.2 assumes a differentiable
   scalar function and a derivative enclosure excluding zero.

   Applicability: import inclusion, with validated elementary functions,
   for cell ranges. Ties need explicit case treatment, not ordinary
   floating comparisons. Root certification is optional; Theorem 6.2
   cannot be invoked at a possible multiple tie without its derivative
   condition. Covering unresolved tie neighborhoods is allowed instead.

These are inspected primary sources, not search snippets. The FLINT/Arb
documentation URLs returned internal access errors, and direct shell
downloads failed DNS; the accessible full primary paper supplies the
needed algorithm hypotheses. No claim of a checked current software API
or locally available interval package is made. Software availability is
an implementation question, not a persistent essential-source blocker.
No package installation, source computation or mathematical script was
performed in this review.

## Exact local comparison and recorded failure

The initial search strings were `Johansson numerical integration arbitrary
precision rigorous error bounds Petras algorithm 2018`, `validated
multivariate integration interval arithmetic discontinuous functions
subpavings rigorous integral enclosure`, and `random Euler product
distribution log absolute zeta sigma greater than one characteristic
function Bohr Jessen`. Follow-ups included `rigorous integration Schur
Horn Gaussian`, `random Euler product interval arithmetic`, and
`validated integration discontinuous interval Johansson`. Bohr--Jessen
distribution/density leads and general multivariate interval-integration
abstracts were not read as theorems and are not inputs. A density formula
would still need certified integration against this selector; it is not
essential once the exact Haar product in L426 is available.

The scoped local check found no enclosure of I. L424's numerical screen
uses midpoint phases and approximate coefficients; its sampled phase
means change sign across covariance scales. It has no full-distribution
enclosure or quadrature remainder. The corresponding ATTEMPTS stop stays
valid. L425 and L426 subsequently repair the qualitative covariance,
branch-null-set and height-limit obligations; they do not repair that
screen's arithmetic or sign certification. This is the concrete new
reason to test the fixed integral, without repeating the old sampling.

Reuse the existing assessment
`drafts/literature/2026-10-17-covariance-free-bulk-phase-averaging.md`
only for its inspected Kowalski Euler-log and Haar inputs. L426's
full-response series and Euler logarithm have uniform positive absolute
majorants at sigma=5/2; no new random-Euler-product limit theorem or
critical-line independence assertion is required. L425 supplies the
explicit P and three diagonal-gap functions, their finite zero sets,
and continuity of both prescribed stages on strict gap regions.
Its qualitative vanishing-neighborhood statement is not a numerical
bound for a chosen neighborhood.

For coefficient coverage, read L423 (3)--(7) and L422 (8)--(12), including
the complete local geometric and omitted-prime tails. They define exact
C_j, S, T, B_j, theta_j and alpha and justify rational enclosure/refinement.
No certificate was rerun or freshly verified. Their presently saved
coefficient intervals need not be narrow enough for this new test. The
needed difference is an enclosure of the nonlinear Q observable with
these exact constants; replacing alpha by a fitted value changes I.

## Approved boundary and discriminating test

One bounded mathematical attempt may specialize interval inclusion and
finite-measure integral monotonicity/Fubini to L426's already established
product probability law. This paragraph specifies proof obligations for
that future attempt, not a derived enclosure or a convergence theorem.

- Enclose the exact coefficient constants, P and normalization constants
  from exact inputs. Reuse L422/L423's certified tails or refine them
  with their documented contracts. Preserve the definition of alpha.
- Truncate the response by a finite prime product, or a Dirichlet sum
  whose composite phases are computed from the same prime coordinates.
  Enclose every omitted prime/prime-power or integer tail uniformly
  using L426's absolute majorants, with an explicit finite bound.
  Propagate that full range through modulus, the degree-14 mixture and
  Q; a small response tail alone is not the final observable error.
- Partition prime angles and the independent angle in normalized
  coordinates with certified cell masses. On strict cells certify the
  literal first low/high pair and the complementary second-stage order,
  square roots and positive denominators. Retain the original coordinate
  and pair order. No arbitrary Schur--Horn basis may replace this one.
- For unresolved angle cells, include all possible prescribed outputs
  via a proved state/range bound and their complete measure. L426 places
  these branch tests in the independent angle, rather than in composite
  response phases. Neither counting grid hits nor deleting a measure-zero
  tie alone bounds a positive-width cell. The exact equality convention
  must remain covered. Finite tie neighborhoods can be enclosed without
  proving that every root is simple.
- Aggregate cell range enclosures with outward arithmetic, including
  complete domain coverage and any unresolved cell budget. If using
  analytic quadrature on strict subcells, prove its complex analyticity
  and uniform parameter hypotheses there. It is acceptable to use only
  direct cell ranges and avoid that extra obligation.

The discriminating threshold remains a final interval [a,b] for the
full exact I with a>0 or b<0. Record the actual interval, tail/cell/branch/
coefficient budgets and any failed checks in a disk certificate, without
claiming success from a preview. An interval containing zero is
inconclusive, unless a separate exact identity establishes vanishing.
Begin with a bounded feasibility enclosure and a declared cell/work cap;
do not promise that increasing dimension or precision will obtain the
needed width. If deterministic tails, branch cells or dependency exhaust
that cap without a useful narrowing, record the obstruction and stop
that implementation. More unvalidated samples are not the continuation.

The method's general ingredients are known; the numerical specialization
remains undone. No originality or nonzero defect is established in this
LITERATURE turn. No lemma or mathematical script was changed. Actual
critical-function realization, capped nondegeneracy, negative-Bcal
clipping, L413's full-error regulator margin and global mixed positivity
remain unresolved and are not premises. Full matching Mathlib coverage
for this enclosure specialization is not checked; unknown availability
is not evidence of absence.
