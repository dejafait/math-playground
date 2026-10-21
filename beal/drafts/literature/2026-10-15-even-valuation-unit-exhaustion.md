# Even-valuation norm-square classes — completed source review

TARGET: Derive an exact ideal-class criterion for ordinary units to exhaust the norm-square classes in L069's D*/D*² with even valuation at every finite prime.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched ideal-square/virtual-unit exact sequences, number-field Selmer groups, norm and class-group compatibility, and odd-degree unit norms; inspected Simon, Lemmermeyer, Milne and BPT primary passages. Scoped duplicate checks covered L069, ATTEMPTS/032 and the prior bare-unit, global-eleven and rational-cubic assessments; no existing local result proves this exact criterion.
SOURCE_EVIDENCE: Simon 2002 Sections 1.1–1.2, Propositions 1.1–1.4 pp.8–9; Lemmermeyer arXiv:1108.5674v1 Sections 2.1–2.2 pp.2–3 and Section 3 p.4; Milne ANT v3.08 (July 19, 2020) Proposition 4.1 with complete proof pp.68–69; BPT arXiv:2001.02263v3 Lemma 2.13, Lemma 2.14 proof and Remark 2.15 pp.12–13. Exact sources and qualifications below.
COMPARISON: Known ideal-square exact sequences and relative norm compatibility supply the general machinery; the target still needs an explicit norm-kernel specialization to L069's cubic extension, retaining or rigorously eliminating the norm-lifting obstruction. None of the inspected theorems computes these fields' class groups or proves unit exhaustion for them.
GAP: Write the compatible norm diagram and identify exactly which ordinary two-torsion ideal classes admit square-norm lifts; prove both directions of the exhaustion criterion, separating square norm from exact norm one. No such field-specific criterion is derived in this review.
REASON: Essential coverage is now sufficient for one separate mathematical specialization. Cite the general results and prove only the compatibility/kernel application; do not reprove general descent theory or infer class-group values.
LITERATURE_REASON: The saved target changes from an explicit unit audit to non-unit coverage; the previously unread ideal-square sequence and its relative norm compatibility were essential.
SCOPE: Exactly TARGET with L033's entire K and E0 and L069's entire cubic field D and unit norm kernel V; no class-group calculation, full Kummer containment, Selmer dimension, rank bound or integer exclusion is approved.

## Relevance and proposed test

The main gap is zero positive primitive integer solutions for every residual
Beal signature; even the ordered (3,4,11) branch is unresolved. The
intermediate target identifies the possible non-unit contribution to one
even-valuation norm-square upper space. Its downstream use is to specify
what certified class information would be required before L071's verified
unit exclusion could contribute to a full descent bound. It need not
resolve the independent local, point or integer-lifting gaps.

Continue if the next attempt gives a necessary and sufficient ideal-class
criterion, with all representative choices and norm-lifting obstructions
controlled. If a class-norm kernel alone is insufficient, retain the
additional obstruction explicitly. An assertion of unit exhaustion without
certified class information, or of full Kummer containment without separate
local justification, fails the test. No numerical or lemma-count threshold
is relevant. A conditional criterion is useful even if its class inputs
remain uncomputed; it is not a claim of exhaustion.

## Inspected known inputs

Denis Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[primary publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf).
Read Sections 1.1–1.2, printed pp.8–9, including the entire proof of
Proposition 1.4. Proposition 1.3 splits the finite square-class group into
S-units and S-class two-torsion. Taking S to consist of the infinite places
matches the ordinary-unit question; the splitting is not stated to commute
with relative norms. Proposition 1.4 allows exceptional finite support for
the actual Kummer image. Its proof treats negative valuations, primes away
from the derivative, and discriminant valuation one separately. Thus it
does not certify even valuations everywhere for this notebook's image.
L069 already justifies the integral irreducible cubic interface; this
review does not repeat or extend that proof.

Franz Lemmermeyer, *Selmer Groups and Quadratic Reciprocity*,
Abh. Math. Sem. Univ. Hamburg **76** (2006), 279–293;
locators refer to [arXiv:1108.5674v1, August 29, 2011](https://arxiv.org/pdf/1108.5674v1),
not presumed journal pagination. Sections 2.1–2.2, manuscript pp.2–3,
define Sel(F) by principal fractional ideals that are squares and give

    1 -> O_F*/O_F*² -> Sel(F) -> Cl(F)[2] -> 1,

with map [alpha] to [a] when (alpha)=a². These are ordinary class groups,
with no positivity condition or omitted dyadic primes. Section 3 p.4 uses
a snake-lemma diagram for additional conditions and states Proposition 3.1
for odd class number. The source's Sel(F) is a number-field group, not
an elliptic Selmer group. Its unconditioned sequence is the needed imported
input; its odd-class-number hypothesis is not known for D. The relative
norm-kernel application is left for the next turn.

J.S. Milne, [*Algebraic Number Theory*, v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANTc.pdf),
Chapter 4, printed pp.68–69, definition preceding Proposition 4.1 and
entire proof of that proposition. For a Dedekind domain A and its integral
closure B in a finite separable extension L/K, relative ideal norm sends
P to p raised to the residue degree. Proposition 4.1(a) gives the norm
of an extended ideal; (c) identifies the norm of a principal ideal with
the ideal of its element norm. Its proof covers the Galois case and then
passes to a Galois overfield and cancels in the torsion-free ideal group.
Hence the nonnormal cubic case is included. A future application to
fractional ideals must explicitly pass through inverses or denominator
clearing. This theorem supplies compatibility, not a class-norm-kernel
calculation for K or D.

Barrera Salazar–Pacetti–Tornaría, *On 2-Selmer groups and quadratic twists
of elliptic curves*, [arXiv:2001.02263v3, September 17, 2020](https://arxiv.org/pdf/2001.02263v3).
Read Lemma 2.13 and the relevant kernel argument p.12, complete Lemma 2.14
proof and Remark 2.15 p.13. Lemma 2.14 uses scalar units in degree three
to obtain surjectivity of norm on unit square classes. Remark 2.15
explicitly discusses lifting an ideal-square relation with norm a square
up to a unit, and uses extra positivity/class hypotheses in its setting.
Those hypotheses cannot be silently transferred here. This is a useful
warning against replacing square-norm lifting by ideal-class norm
vanishing without proof. The general global Selmer bounds in that section
are not imported. Prior L070 coverage is reused only for motivation;
its rational dyadic theorem does not settle global non-unit coverage.

## Bounded comparison, duplication and continuation

Queries included `number field units Cl 2 exact sequence square classes
Selmer`, `Barrera Pacetti Tornaria 2001.02263 class group units exact
sequence norm`, `Lemmermeyer Selmer groups quadratic reciprocity pdf`,
`norm Selmer groups class groups odd degree units exact sequence`, and
primary-domain ideal-norm searches. Search snippets and third-party mirrors
were discovery leads only; the theorem evidence above was read directly
in the primary PDFs. No failed search is evidence of novelty.

The existing bare-unit assessments already mention Simon Proposition 1.3;
this review reuses that input and fills its relative norm comparison.
The global-eleven assessments concern K(S,5) and unrestricted primes over
five; their Sharifi cohomological sequence assumes S includes primes over
n. It is not substituted for the present all-finite-even n=2 group.
L069 counts units only, L070 is local, and audited L071 supplies one actual
unit exclusion. None duplicates this exact non-unit coverage target.
ATTEMPTS/032 still bars the unfiltered rank shortcut; this target does
not reopen it or enlarge the exhausted bounded searches.

The next research attempt may specialize the two cited ideal-square
sequences to F=D and F=K, use Milne to check the relative norm diagram,
and track the induced lifting obstruction. The degree-three scalar/unit
argument of L069 and the inspected Lemma 2.14 is available for determining
whether an obstruction survives, but its effect on the full sequence must
be proved. Do not assume the abstract splitting in Simon is norm-compatible.
Keep norm-square classes distinct from representatives of exact norm one.
A short diagram/application proof is justified to make this difference
checkable, rather than as a new general theorem.

Essential notebook inputs are L033's K/E0 and L069's D/V; L070 and audited
L071 provide downstream motivation only. No cross-notebook input occurs.
Actual ordinary class groups, class norm maps, all-finite-even containment
of the full Kummer image, finite-local filtering, rank, subgroup indices,
cosets and primitive integer lifting remain unresolved. A criterion on the
stated space must be labeled as such even if containment remains unknown.
Mathlib matching/supporting coverage: not checked; no absence is asserted.

Outcome: source coverage advances from REVIEW_REQUIRED to SPECIALIZE.
This approves a later specialization, not a new lemma or a mathematical
criterion in this literature-only turn. PROOF.md and DAG.md need no change.
