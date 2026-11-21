# Normalized shrinking height cells — source comparison

TARGET: Assess primary coverage for an explicit shrinking-height-cell coefficient-loss bound from L902's normalized moments, uniform over Taylor degree and |x|<=R with prescribed absolute error eta, distinguishing it from L899/L900 and assuming no Fourier sign margin.
CHECKED: 2026-11-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step129 searched exact Xi-defect height-cell, normalized cross-endpoint/sinhc moment, weighted total-variation Lipschitz and unbounded-observer stability terminology; inspected the primary sources below and narrowly compared L898-L900/L902 and the recorded fixed-cross-endpoint stop. No matching completed coefficient-loss result was located in that scope; no novelty or exhaustive absence claim.
SOURCE_EVIDENCE: Sprungk arXiv:1906.07120v3 Theorem8 printed p10, setup p3, TV convention p7, normalization proof pp7-9 and AppendixA before (13) p24; van Hemert 20July2026 raw main.tex Sections8-11, especially exact-hierarchy/mixed-limit/obstruction and lines695-711 on refinement. Primary URLs, exact hypotheses, version qualifications and reuse below.
COMPARISON: L899 is unweighted full-L1 control; L900 is oscillatory transform control. Neither directly bounds the growing coefficient observer. Sprungk permits a changed reference probability, but returning from its weighted normalizers to A_0 and bounding all parity sections are unperformed application steps. The manuscript states fixed-degree refinement, not this explicit degree-uniform squared-height rule.
GAP: Prove a finite explicit cosh-weighted normalized-density bound and its uniform parity-section application, including zero heights and every degree, then specify delta(R,eta)>0. No such constant or width is derived here; signed margins and all-degree mixed positivity remain unresolved.
REASON: The source review identifies a precise established-method specialization with accessible inputs and no matching recorded application. The next research scope is nominated separately for approval; this review neither executes the mathematics nor certifies originality.
SCOPE: Actual Phi=k/2 and A_(2j),m_(2j) of L898; L902's retained L309/L037 contracts; 0<=a<=y<=b<=1/2, R>0, eta>0, and every integer m>=0. Constants may be finite explicitly specified theta integrals; no numerical optimality, relative margin or unbounded-frequency positivity is requested.

## Exact proposed estimate, not an established conclusion

For a cell [a,b], use the proposed lower polynomial

    B_m^{a,b}(x) = 1
      + sum_(1<=j<=2m+1, j even) m_(2j)(b) x^(2j)/(2j)!
      - sum_(1<=j<=2m+1, j odd)  m_(2j)(a) x^(2j)/(2j)!,

and L898's exact section

    S_m(y,x) = sum_(j=0)^(2m+1) (-1)^j m_(2j)(y) x^(2j)/(2j)!.

The target is an explicit positive delta(R,eta) such that b²-a²<=delta
implies 0<=S_m(y,x)-B_m^{a,b}(x)<=eta for every displayed m,y,x
with |x|<=R. All coefficients use their own A_0 normalization. This
is the estimate to assess, not mathematics executed in step128.

Potential use: a quantitative price for using ordered coefficients in
adaptive height cells. This would still need an independently proved
positive section/reference margin; absolute error control supplies no
sign. Do not infer any value of a hypothetical margin or select a mesh
by dividing by a margin not yet paid. R is fixed in each assertion;
no uniform positive width as R tends to infinity is proposed.

The new, independently testable issue is shrinking cell loss for the
normalized parity minorant, rather than another fixed-width radius scan
or bounded-observer interpolation. L898's original stop is preserved.
L312 blocks importing conditional cosine monotonicity; it does not
alone decide a nonoscillatory coefficient-loss estimate. L899/L900 must
be compared before deriving anything, to avoid manufacturing a duplicate.

Read primary theorem hypotheses and essential proof cases for weighted
normalization stability or the exact coefficient estimate, using the
existing assessments where their scope matches. Import a matching
bound; specialize only a real uncovered difference. Continue to later
mathematics only if the comparison identifies a precise covered test.
Abandon this nomination as a distinct research task if it is already a
direct recorded result with no needed application, or if its only stated
benefit assumes a missing sign. Do not extend it to oscillatory ordering.
Full matching Mathlib coverage is unchecked.

No central creative mechanism is claimed. No independently justified
signed compensation input is presently available; this is the blocker
to creative routing, rather than a quota-based reason to invent one.

## Completed source review — 8 November 2026, step129

LITERATURE_REASON: The changed all-degree coefficient observable lacks essential coverage in the prior bounded-observer assessment; this review addresses that difference, reusing the scalar and ordering sources already assessed.

The main gap remains L030–L032/C032a actual-Xi all-degree mixed positivity.
This review selects exactly the proposed shrinking-cell absolute loss.
Its downstream use is a quantitative error budget for adaptive coefficient
cells, even before a positive reference margin is available. It does not
select or assume such a margin. This is one source review; no lemma,
mathematical script, constant calculation or new inequality is produced.

### Primary inputs inspected

Björn Sprungk, *On the Local Lipschitz Stability of Bayesian Inverse
Problems*, Inverse Problems 36 (2020), 055015,
[arXiv:1906.07120v3](https://arxiv.org/pdf/1906.07120v3#page=10),
22 January 2020 (title page 23 January), Theorem 8, printed p.10.
For a Borel probability mu on Polish E and real f,g in L1(mu),
essinf_mu f=0, and positive finite Z_h=integral exp(-h) dmu, it states

    d_TV(mu_f,mu_g) <= exp(-[essinf_mu g]_-)/Z_f * ||f-g||_L1(mu),
    dmu_h=exp(-h)dmu/Z_h, [r]_- = min(0,r).

TV is half the density L1 distance (p.7). The statement allows an
arbitrary reference probability, rather than only the original theta
reference. Read setup p.3, the normalization splits on pp.7–9 to which
the TV proof refers, and Appendix A before (13), p.24, which bounds TV
by the likelihood L1 difference divided by its first normalizer.
The normalization proof also controls the raw normalizing-integral difference.

Leonard van Hemert, *Finite Positivity Certificates and a Cross-Endpoint
Obstruction for a Riemann Xi-Defect Kernel*, manuscript title date
20 July 2026, [primary raw source](https://raw.githubusercontent.com/LeonardSEO/certified-riemann-xi-positivity/main/paper/main.tex),
retrieved 8 November 2026, 868 lines; no immutable commit or peer-review
status verified. Read Sections 8–11: exact sections, entire cosine/cosh
series, mixed-limit formula and fixed-endpoint obstruction, including
zero and coincident-endpoint qualifications. Section 11, lines 695–711,
asserts fixed-degree refinement by continuity and distinguishes diagonal
positivity on every compact rectangle as RH-equivalent. It states no
explicit degree-uniform width for the present own-normalized minorant.
Its fixed-cell claim concerns its raw cross-normalized construction;
we do not transfer that stop to a different normalized construction.

Reuse DLMF 4.36.1/4.33.1/25.6.1 as assessed in
[the L899 source comparison](2026-11-08-normalized-xi-defect-interpolation.md),
and Dümbgen–Mösching Theorem 1/Remark 4 as assessed in
[the normalized-moment comparison](2026-11-08-normalized-height-moment-order.md).
The former scalar application is already canonical in L899; L902's
strict order is already audited with retained L309/L037 contracts.
No unchanged theorem needs a new search or general reproof.

### Searches, duplicates and failures

Queries included `"Sprungk" "weighted" "total variation" Lipschitz`,
`"Riemann" "normalized" "cross-endpoint" moments sinhc`,
`"normalized measures" "weighted" "Lipschitz" potentials unbounded expectations`,
`"Xi-defect" "height" "cells"`, and `"sinhc" "moments" "Lipschitz"`.
A Hellinger/expectation query supplied alternative leads, but no theorem
from those leads is imported or required. Secondary search results were
not used as mathematical evidence. Searches found no exact-match theorem;
that fact establishes neither absence nor novelty.

Local reads compared L898's normalization, domination, exact sections
and fixed-endpoint stop; L899's full proof and audit; L900's hypotheses,
conclusion and analytic interface; L902's full proof and qualification;
and L312's conditional-cosine obstruction statement/interface. The
[fixed-cross-endpoint stop](../../ATTEMPTS/2026-11-08-fixed-cross-endpoint-xi-extension-stop.md)
is preserved. Targeted searches of the November8 normalized/frequency
assessments and these canonical files found no completed cosh-weighted
cell-loss estimate. This is a scoped duplicate check, not a claim about
all notebook mathematics. No cross-notebook input was read.

### What the later specialization must establish

The candidate method is to apply the imported stability theorem with a
reference density proportional to cosh(Rq) W_(1/2), retaining L899's
potential Psi_y=log(sinhc(p/2)/sinhc(yp)). This is a proposed application,
not a verified new measure estimate. The later proof must justify its
finite positive mass, potential L1 integrability and essential infimum,
including positive-measure neighborhoods of p=0. It must control its
changed normalizing masses and recover the original A_0 normalization;
ordinary TV between two newly normalized weighted laws is insufficient
on its own. L899's scalar bound and L898's theta domination are available
inputs, but their changed weighted integrability must be checked.

Then combine a justified weighted bound with L902's coefficient order
and a nonnegative absolute-series majorant, checking every finite parity
section and the infinite majorant without an unjustified interchange.
Give an explicit finite theta-integral constant and a positive width
rule depending on R,eta. These are future obligations, not conclusions
of this literature-only step. No reproof of general Bayesian stability
or of theta curvature is justified; only the weighted normalization and
parity application differ from existing local results.

Continue if this bounded application gives the stated absolute loss
uniformly in degree, independently of signs. Abandon or narrow it if a
required uniform estimate fails, is already an exact recorded result,
or needs an unpaid Fourier margin. Do not optimize constants, scan
radii, infer a global sign or treat fixed R as unbounded frequency.
Full matching Mathlib coverage remains unchecked, not absent.

The separate [specialization nomination](2026-11-08-normalized-shrinking-height-cell-specialization.md)
contains the exact next target. It requires next-turn approval. No
independently justified signed compensation supports a central creative
target now; that blocker is retained rather than inventing a mechanism.
