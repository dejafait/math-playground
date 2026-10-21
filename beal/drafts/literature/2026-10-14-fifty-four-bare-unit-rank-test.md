# Bare norm-square ambient rank diagnostic

TARGET: Test whether the unfiltered norm-square 2-descent ambient space for E0 over L033's K can supply a rank upper bound below twelve, retaining its full unit contribution and rational 2-torsion without class-group assumptions.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact descent/class-bound search, duplicate checks and primary comparison in drafts/literature/2026-10-14-fifty-four-coarse-unconditional-rank.md; this is its delimited bare-unit subtarget.
SOURCE_EVIDENCE: Directly reaccessed Simon 2002 Section 1.1–1.2 p.8 at https://doi.org/10.1112/S1461157000000668 and Barrera Salazar–Pacetti–Tornaría arXiv:2001.02263v3 Section 1 p.3, Hypotheses 2.1 p.8, archimedean notation p.11 and Lemma 2.14 with entire proof pp.12–13 at https://arxiv.org/pdf/2001.02263v3; explicit primary PDF links and scope below.
COMPARISON: Standard unit-square dimensions and the cubic norm allow a diagnostic before class-group certification; applicability to E0/K, including split algebra and torsion correction, remains to check.
GAP: No ambient dimension or unit lower bound is derived here; split components and rational 2-torsion cannot be silently omitted.
REASON: Decide whether omitting all local image conditions is viable before costly global arithmetic.
SCOPE: Only the unfiltered ambient-size diagnostic and necessary model, unit-norm, real-sign and torsion checks; no class enumeration, local-image computation, actual rank determination or branch exclusion.

Essential input is L033's E0, E1, degree-twelve K and dual maps.
FNS Table 5 is conditional comparison only. L068 and the prior stops
are routing evidence, not rank premises. No cross-notebook input.

The main gap is positive primitive integer emptiness. The intermediate
test could identify whether any coarse rank certificate must include
local conditions, avoiding an expensive inadequate upper-space
calculation. Other-class coverage, generators/index, coset bounds and
primitive integer lifting remain independent gaps.

Identify the entire étale two-torsion algebra from a verified integral
cubic model. Retain every component and archimedean type. Apply the
named Dirichlet unit theorem and check the norm on unit square
classes, including roots of unity and scalar units from K. Verify
their injection into D*/D*². Do not assume total reality, cubic
irreducibility, odd narrow class number, maximal polynomial order,
class triviality or GRH.

Compare the resulting unit-subspace lower bound on the unfiltered
norm-kernel ambient dimension, after subtracting the ACTUAL rational
2-torsion dimension, with required upper-bound value eleven.
This is a size test for a proposed upper space, never a lower bound
on Mordell–Weil rank. All unit classes must be retained, rather than
only found units. Necessary local conditions may remove some of
them, but are outside this unfiltered diagnostic.

Continue only if the diagnostic leaves the strict threshold feasible
and missing class contributions can be bounded concretely. Otherwise
park this simplification; do not declare all 2-descent or Chabauty
exhausted. No numerical bound or rank conclusion is approved as
already established.

The field-case unit count is known in Lemma 2.14. Any component
bookkeeping must be justified from the named unit theorem; importing
the field formula outside its hypotheses is forbidden. This limited
applicability difference is the only proposed rederivation.
Mathlib matching/supporting coverage: not checked. This source-only repair preserves the exact target; mathematical application remains for a separate turn.


## Direct primary-source repair (2026-10-14)

Denis Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf).
Printed p.8, Section 1.1 assumes an integral monic irreducible cubic;
Propositions 1.1–1.2 give the Kummer injection and square-norm containment.
Section 1.2 recalls Dirichlet's S-unit theorem, including roots of unity,
and Proposition 1.3 separates unit squares from S-class two-torsion.
These are inspected statements, not evidence that our cubic is irreducible
or that its class contribution vanishes.

Barrera Salazar–Pacetti–Tornaría, *On 2-Selmer groups and quadratic twists
of elliptic curves*, [v3, September 17, 2020](https://arxiv.org/pdf/2001.02263v3).
Section 1 p.3 states the norm-square Kummer description for a monic
squarefree cubic, allowing an étale algebra. Hypotheses 2.1 p.8 then
assume odd narrow class number, no rational two-torsion and the finite-place
condition; that section's algebra is a field. On p.11, a,b,c count,
respectively, real places with algebra R×C, real places with R³, and complex
places. Lemma 2.14 pp.12–13 counts norm-square unit classes as
2^(a+2b+2c). Its entire proof uses norm surjectivity on unit square classes
from scalar units in odd degree and Dirichlet counts for the base and
cubic field. This field formula is an inspected input, not a computation
for L033's K or permission to omit split factors. The broader section
hypotheses are not asserted for K; the future diagnostic must justify
which elementary proof ingredients apply without them.

No new search was needed for the unchanged target: the coarse assessment's
recorded searches and duplicate/failure checks remain applicable, including
history/212 and ATTEMPTS/029–031. This turn repaired direct source evidence;
it neither derived the component extension nor calculated the ambient
size. SPECIALIZE remains limited to the previously stated diagnostic.
The source test passes because the essential unit theorem and norm proof
are accessible. The mathematical continuation/abandonment test above is
unchanged; no new result or novelty claim follows from this repair.
