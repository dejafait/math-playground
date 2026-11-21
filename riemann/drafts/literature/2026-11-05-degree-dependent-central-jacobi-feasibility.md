# Degree-dependent central Jacobi feasibility — completed source review

TARGET: Assess whether the exact central quotient constraints q_0,q_1,q_2 of L791 admit positive parameters depending on d with A_d>B_d+d-1 and C_d>D_d+d-1 for arbitrarily large degrees, using primary matching and Jacobi/convolution results and distinguishing sufficient-regime failure from model nonexistence.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step597 reused the fixed-degree matching and fixed-model classification assessments, searched the exact quotient terminology and prescribed coefficient-ratio/degree-dependent Jacobi variants, and inspected the primary cases below. No matching central unbounded-degree feasibility theorem was located in this bounded search; this is not an originality claim.
SOURCE_EVIDENCE: Holland https://arxiv.org/html/2608.08682v1 (49)–(57),(66)–(74), Lemma6.2/full proof and Lemma7.3's Jacobi identity; Martinez-Finkelshtein–Morales–Perales https://arxiv.org/pdf/2309.10970v3 pp.11,15–16,33–34, Propositions2.7(iii)/2.17, Theorem3.1/full proof, Proposition4.15(ii)/(R2); https://dlmf.nist.gov/18.5.E7, https://dlmf.nist.gov/18.3#T1, https://dlmf.nist.gov/18.2#vi. Reused step474's full root-regime comparison; additional leads and access limits are identified below.
COMPARISON: Known conditional matching and per-degree root theorems cover the construction's interpretation, not the central feasibility quantifiers. L817 fixes a tuple before varying degree and cannot decide freely degree-dependent tuples. Broader continuous and discrete sufficient root regimes prevent any strict-Jacobi stop from being a global model-nonexistence claim.
GAP: Prove or refute unbounded-degree feasibility of the three exact central quotient equations with four free positive parameters in the specified strict Jacobi regime, including both numerator pairings. No feasibility conclusion, finite degree cap, root-separation rate or signed residual estimate is established here.
REASON: Source coverage is sufficient for one bounded algebraic specialization using the existing actual-data enclosures. Cite matching/orthogonality/convolution results; only the central feasibility difference needs an attempt, not a reproof of those results or a new degree sweep.
LITERATURE_REASON: The tuple and D may now vary with degree while the exact central data remain fixed; this changes the quantifiers beyond the ready fixed-tuple assessment and beyond Holland's large-shift existence theorem.
SCOPE: Completed literature-only source gate. The following nomination is retained for its scope and stopping test; the next mathematical target is specified separately in 2026-11-05-degree-dependent-central-jacobi-test.md. No calculation, lemma or mathematical script is produced in this review.

Essential inputs for a later mathematical attempt would be L791's exact
q constraints and audited data provenance, with L018/L021/L776/L778
normalization/analytic/evaluator/software contracts retained. L817 is
the fixed-family contrast. C792a/b and L793 are contrasts about universal
preservation and relative root tolerance, not existence premises.
No cross-notebook input is requested.

The potential downstream use is a degree-dependent positive-rooted
reference to which a genuinely model-specific signed perturbation might
later be compared. Matching indices0..4 alone supplies neither signed
residual control nor root separation. Those remain independent gaps.

The future bounded test, only after source approval, is exact feasibility
or an obligatory obstruction to arbitrarily large d in this specified
sufficient Jacobi regime. If the constraints impose a finite degree cap,
park this regime only, without claiming all reference models impossible.
If feasibility survives or coverage supplies only sufficient statements,
record that precise limitation; do not infer simplicity or signed transfer.
No feasibility conclusion is derived in this nomination.

Prior scope available for reuse:
`2026-11-05-shift-zero-jacobi-matching-feasibility.md`, exact-system and
root-hypotheses sections;
`2026-11-05-fixed-matched-model-all-degree-scope.md`, p=q classification
and fixed-versus-degree-dependent qualification. Reuse their primary
citations; review only the changed assumptions and essential gaps.
Full matching Mathlib coverage remains unchecked.

## Completed comparison — step597, 5 November 2026

Main gap: actual-Xi all-degree mixed positivity. This intermediate
question asks whether a particular sufficient reference regime remains
available as degree grows, before paying for separation and signed
transfer. A negative answer stops that regime only. A positive answer
would not resolve either independent gap. The changed question is not
a repetition of the fixed-tuple or universal-preserver tests.

### Exact scope retained from L791

At shift zero retain gamma(j)=8*4^j*j!*a_j,
R_j=gamma(j)/gamma(0), and q_k=R_(k+1)^2/(R_k R_(k+2)).
L791's full stated conservative enclosures are

    1.07484394250019421126346157158 < q_0 < 1.07484394250019421126346157162,
    1.06274366627144916855311401273 < q_1 < 1.06274366627144916855311401285,
    1.05430333113463476927545484495 < q_2 < 1.05430333113463476927545484516.

The actual q values are fixed and correlated. These are inherited
certified inputs, not newly evaluated numbers; retain L018/L021/L776/L778
and L791's completion, analytic-error, evaluator and software contracts.
No script or certificate was replayed in this source review. Interval
independence may be used only conservatively, and rounded centers may
not replace the exact data. The original parameter box is not imposed
on the new unknowns and D=B_J/2 is not imposed.

For each proposed integer d>=1 the question uses positive A_d,B_d,C_d,D_d
and the same equations, for k=0,1,2,

    q_k=(A_d+k)(B_d+k+1)(C_d+k)(D_d+k+1)
        /[(A_d+k+1)(B_d+k)(C_d+k+1)(D_d+k)].

The strict regime is A_d>B_d+d-1 and C_d>D_d+d-1. The model is
Holland (69), with its positive scale D_d/(A_d C_d). Its numerator
parameters may be paired with (B_d,D_d) in either order; a claim about
all admissible tuples must cover both. Arbitrarily large degrees allow
different tuples at different degrees, rather than one tuple good for
every degree. No simplicity, separation or actual-Xi signs are assumed.

### Primary statements and applicability boundary

Jonathan Holland, *A new hyperbolicity wedge and a joint semicircle limit
for Jensen polynomials of Riemann's xi-function*,
[arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1), 9 August 2026:
(49),(52),(66)–(69), Lemma6.2 and its complete quotient-induction proof
give conditional matching through R_4. The proof uses positivity,
initial values and the three equations; D=B_J/2 in (51) is the chosen
existence construction, not a premise used in that induction. Thus a
free-D solution may use the cited identity, but its existence is unpaid.
Lemma6.1 and (53)–(57) apply only eventually in the shift; their
contraction construction does not import a central solution. Reused
step473/474 for that proof's scope; no full manuscript audit.

The Jacobi identity in Lemma7.3 sets alpha=V-1, beta=U-V-d.
[DLMF18.5.7](https://dlmf.nist.gov/18.5.E7),
[Table18.3.1](https://dlmf.nist.gov/18.3#T1) and
[18.2(vi)](https://dlmf.nist.gov/18.2#vi) supply the representation,
alpha,beta>-1 orthogonality conditions and simple interior zeros.
Here d is polynomial degree, not the source's coefficient shift.
The nominated strict inequalities are precisely the classical
conditions already identified in step474, now with variable d.
Holland's additional localization assumptions (57) are stronger and
are not imposed merely to ask this root-regime feasibility question.

A. Martinez-Finkelshtein, R. Morales and D. Perales,
*Real roots of hypergeometric polynomials via finite free convolution*,
[arXiv:2309.10970v3](https://arxiv.org/pdf/2309.10970v3),
2 May 2024, printed pp.11,15–16,33–34: Proposition2.7(iii) preserves
nonnegative roots; Proposition2.17 preserves logarithmic mesh of
positive-rooted factors; Theorem3.1 concatenates parameter lists.
Reaccessed their statements, the full mesh/coefficient proofs and
the relevant factorization cases. Positive denominator Pochhammer
normalization is nonzero; variable dilation is positive. Multiplicity
is not excluded by preservation alone. No uniform separation rate is
imported. The PDF is pinned; the HTML has an inconsistent 2026 date.

Proposition4.15(ii) gives a larger continuous positive-root region:
B_d,D_d>0, A_d>B_d+d-2, C_d>D_d+d-2, with parameter permutations.
The following (R2) also permits positive integer paired differences
1,...,d-1; Remark4.1/(60) exhibits repeated roots in a discrete case.
These are sufficient results, not a complete classification. They
must remain outside any claimed nonexistence conclusion for the
stricter nominated region. Reuse step474 for Table2 and Theorem4.7;
no extension of those theorems is derived here.

### New leads and bounded-search limits

Queries included `Jacobi matching quotient Jensen Holland degree
dependent`, `Jacobi coefficient ratios prescribed parameters matching
polynomial`, `Holland Jacobi central matching xi`, `Jacobi quotient
invariants parameters`, and `hypergeometric prescribed coefficient
ratios real zeros parameters`. Searches did not locate a direct
central feasibility theorem. Irrelevant hits were not theorem evidence.

A search index led to J. Savva, *A Two-Thirds Hyperbolicity Wedge for
Jensen Polynomials of Riemann's Xi-Function*, v1.1,
[DOI10.5281/zenodo.22293642](https://doi.org/10.5281/zenodo.22293642).
The preprint record could not be opened. The
[author's account](https://www.beyond-plausible.com/a-two-thirds-hyperbolicity-wedge-for-jensen-polynomials-of-riemanns-xi-function/),
5 September 2026, Sections3–4, was inspected: its stated theorem
requires n^2 log(n+2)>=K d^3, K>0, and its free-D construction matches
indices0..5 for large n. This author-stated candidate is not imported
or proof-audited. It supplies no central feasibility statement in those
inspected sections; a better large-shift exponent is not this target.

Other indexed leads were M. Sarnowski, Papers134Z/134AA,
[DOI10.5281/zenodo.22023893](https://doi.org/10.5281/zenodo.22023893) and
[DOI10.5281/zenodo.22025447](https://doi.org/10.5281/zenodo.22025447).
Both records failed to open. Their primary theorem statements/proofs
remain unread; secondary Padé-spine descriptions are not accepted
theorem evidence. No claim about their exact coverage or correctness
is made. These optional broader-matching leads are not essential
premises for the narrow algebraic feasibility test: its equations and
sufficient-regime interpretation already have accessible primary
coverage, and it will claim no originality or exhaustive literature
classification. Access failure does not supply a mathematical stop.

### Duplicates, continuation and limits

Narrow local search/read covered L791/L817 and the step474/594
assessments, plus the statements of C792a/b and L793. L791 gives one
finite model outside the nominated classical regime; its direct root
brackets remain intact. L817 excludes that fixed tuple across all
degrees, without excluding changing tuples. C792a/b concern universal
or same-mesh residual preservation. L793 is a sufficient tolerance
conditional on model roots and separation. None decides the present
free-parameter feasibility problem or pays its later signed error.
No cross-notebook result was read.

The source gate is SPECIALIZE for one algebraic feasibility attempt,
specified in [the calculation assessment](2026-11-05-degree-dependent-central-jacobi-test.md).
Use the exact equations and full input intervals to seek either
unbounded-degree admissible solutions or a necessary finite degree
cap. A finite scan, a failed numerical solver, or failure of one
pairing is inconclusive. An obstruction may use a subset of the three
equations if it is proved necessary for every proposed solution.
No such inequality, elimination, numerical cap or solution is derived
or approved as a mathematical conclusion in this literature turn.
One bounded argument is justified; inconclusive work must preserve its
remaining subproblem rather than silently change the root regime.

Full matching Mathlib coverage remains unchecked. Standard results are
to be cited; no reproof is justified. No lemmas, mathematical scripts,
PROOF.md or DAG.md were changed. There is no new mathematical advance
beyond the inspected sources. A central creative signed mechanism
remains unready because existence, quantitative separation and signed
payment are still independent unpaid claims.
