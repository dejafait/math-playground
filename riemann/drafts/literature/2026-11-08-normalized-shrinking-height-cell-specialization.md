# Normalized shrinking height-cell loss — specialization nomination

TARGET: Establish an explicit squared-height width delta(R,eta)>0 for L902's own-normalized parity minorant with 0<=S_m(y,x)-B_m^{a,b}(x)<=eta uniformly in m>=0, a<=y<=b and |x|<=R, using cosh-weighted stability without a Fourier sign margin.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse step129's exact target, weighted-normalization, stronger-result and scoped duplicate searches recorded in 2026-11-08-normalized-shrinking-height-cell-loss.md; no matching completed application located, with no novelty claim.
SOURCE_EVIDENCE: Sprungk https://arxiv.org/pdf/1906.07120v3#page=10 Theorem8 printed p10, setup p3, normalization proof pp7-9 and AppendixA before (13) p24; van Hemert https://raw.githubusercontent.com/LeonardSEO/certified-riemann-xi-positivity/main/paper/main.tex Sections8-11, particularly lines695-711. Reuse L899's scalar DLMF application and L902's assessed ordering input. Full source comparison and qualifications are in the linked step129 review.
COMPARISON: General normalization stability is known. L899 controls the unweighted law and L900 an oscillatory transform; neither directly supplies this unbounded coefficient observer. The primary Xi manuscript gives fixed-degree refinement, not the proposed explicit uniform-degree width. Only the weighted reference/normalizer and parity application remain to specialize.
GAP: Establish the cosh-weighted original-normalization estimate, all-degree absolute-series domination and explicit finite constant/width, including zero heights; no bound is proved by this nomination. Independent signs and global all-degree mixed positivity remain open.
REASON: One bounded established-method application is independently testable and may price adaptive cells without assuming their signs. New ready coverage receives separate next-turn approval before research; no lemma, script or mathematical derivation is included here.
SCOPE: Actual Phi=k/2, p=u+v, q=u-v and A_(2j),m_(2j) of L898; retained L902/L309/L037 contracts; every R>0, eta>0, integer m>=0 and 0<=a<=y<=b<=1/2. Constants may be explicit finite theta integrals; no numerical optimization, sign hypothesis or frequency-uniform positive width.

The exact quantities are the already nominated section and minorant:

    S_m(y,x) = sum_(j=0)^(2m+1) (-1)^j m_(2j)(y) x^(2j)/(2j)!,
    B_m^{a,b}(x) = 1
      + sum_(1<=j<=2m+1, j even) m_(2j)(b) x^(2j)/(2j)!
      - sum_(1<=j<=2m+1, j odd)  m_(2j)(a) x^(2j)/(2j)!.

All moments use their own A_0 normalization. Seek delta(R,eta)>0
so b²-a²<=delta implies the TARGET inequality. This is an unproved
target, not an imported theorem or an assertion of positivity of B_m.

[The completed source review](2026-11-08-normalized-shrinking-height-cell-loss.md)
contains exact primary hypotheses, inspected proof cases, queries,
version qualifications, duplicate comparisons and the application plan.
Import the general theorem there; do not reprove it or theta curvature.
Apply it, if justified, to a reference proportional to cosh(Rq)W_(1/2)
with L899's existing nonnegative potentials. Prove the changed reference
hypotheses, all weighted moment finiteness and essential infima; control
the weighted masses and recover the original A_0 normalization explicitly.
Then test uniformity for every finite parity section with a justified
absolute cosh-series majorant. Any different method needs its own scope
comparison; the general stability theorem itself is not new mathematics.
No candidate constant or width has yet been calculated.

Essential inputs: L019/L898 positivity and polynomial-exponential decay,
L899's scalar potential bound and positive mass floor, and audited L902
under retained L309/L037 arithmetic contracts. L900, L312 and the
fixed-cross-endpoint stop are comparisons, not new proof premises.
No cross-notebook input or new source blocker is needed. Full matching
Mathlib coverage is unchecked, not absent.

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
Potential downstream use is a computable absolute price for adaptive
height cells; positive reference/section margins, growing-frequency
coverage and higher forms remain unpaid. Do not choose a mesh from an
assumed margin. Keep R fixed in each assertion.

Pass only if one application yields a rigorously finite explicit constant
and positive squared-height width with the exact uniform quantifiers,
zero endpoints and no sign assumption. Otherwise preserve the failed
hypothesis, narrow or park the application, and do not substitute another
fixed-width radius scan. This is ordinary specialization/calculation,
not a new central creative mechanism or an RH candidate.
