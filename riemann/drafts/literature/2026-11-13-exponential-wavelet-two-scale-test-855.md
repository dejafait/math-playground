# Fixed exponential-moment two-scale complete-Weil test — source approval856

TARGET: Test strict half-contraction of the complete Weil pairing between the two compact exponential-spline detail spaces at T=log(3)/16 and T=log(3)/32 inside (0,4log(3)), using roots (-1/2,-1/2,1/2,1/2), no zeros and free filter Q_i=1.
CHECKED: 2026-11-13
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused assessment854's exact Weil/wavelet searches and local IMS/modulus/Schur/neutral-coordinate failure comparison; step856 found an equation-bearing indexed version of the published primary PDF, followed its Riesz/reproduction references, and checked fixed-window positivity overlap. Exact queries, inspected cases and unused leads are below; no matching half-contraction was identified and no novelty inference follows.
SOURCE_EVIDENCE: Read Khalidov-Unser2006 SectionsIII.A/IV.A-B/V.A-B pp1259-1262, (3)-(9), compact G formula, Proposition2 and Property2 proof; cross-checked2005 Sections2-4. Read Unser-Blu2005 PartI Theorem1 real-root case and III.C2/Proposition2 including its proof; checked PartII Theorem1 prose. Reuse assessment804's complete Schur/Rump coverage; paper60/v1 Theorem1.1 does not cover this larger window or half threshold.
COMPARISON: The compact exponential-moment construction and finite Hermitian block methods are known. Their fixed full-Q specialization and quantitative strict half-contraction remain unproved; L2 orthogonality supplies neither Weil orthogonality nor positive Q metrics. A successful test would be local progress, without certified originality or a global positivity conclusion.
GAP: The later attempt must verify source-unit conversion, exact support/lattice enumeration and moments, H2/smooth-core applicability, independent complete finite spans and every full-Q entry/error; then certify positive diagonal metrics and beta<1/2 or a rejecting pair. No block value or sign is established here.
REASON: Separate literature-only approval856 resolves nomination855's essential construction coverage and authorizes one unchanged fixed-target RESEARCH/REPRODUCTION attempt. No new lemma, mathematical script, numerical result or half-contraction theorem was produced.
SCOPE: Only the stated two scales, real roots, empty zero vector, Q_i=1, source origin0, every strictly interior closed-support translate and complete Q; no parameter/threshold sweep, dual substitution, moment correction, ambient infinite-dimensional assertion or frozen-family reopening.
LITERATURE_REASON: At invocation start nomination855 was REVIEW_REQUIRED: equation-level compact-side/moment coverage was essential and unread. This turn supplies that missing evidence; ready Schur, scalar verification and failure assessments are reused without another general search.

## Original nomination855; pending-language preserved historically

Put L=4log(3), I=(0,L), T_0=log(3)/16 and T_1=T_0/2.
At each T use the compact B-spline-type generator of the source's
orthogonal difference V_T minus V_(2T), with the specified four roots,
empty zero vector, Q_i=1 and source-normalized scaling functions.
The detail lattice has step2T. Fix its origin0 and retain every
translate whose entire closed support is contained in I. Let U_0,U_1
be their full complex finite spans. These definitions await exact
source verification; no basis or moment specialization is proved here.

Let H be the Hermitian polarization, linear in its first argument,
of L744(6)'s original complete Q on I. Retain zero extensions,
dt/(2*pi), the actual digamma symbol, both poles and every von Mangoldt
term 2<=n<81; n=81 has zero overlap. Poles may vanish only after exact
moments are established. Do not substitute an arithmetic norm or a
differential energy for Q.

The one proposed test is positive definiteness of Q on both U_j and

    beta = sup_{0 != u in U_0, 0 != v in U_1}
           |H(u,v)| / sqrt(Q(u) Q(v)) < 1/2.

The supremum is over whole spaces, with all signed terms combined
before the modulus. The half budget reserves room for other levels;
it is a screen, not a sufficient infinite-scale theorem. A later
approved attempt must justify the finite Gram/block reduction and all
analytic/roundoff remainders. No diagonal positivity, beta value or
automatic form extension is asserted. If the specified compact side
lacks the required exact moments, stop this nomination without
switching to the dual, truncating tails or adding moment corrections.

A certified pair with beta-ratio>=1/2 stops this strict estimate.
Failure to certify a diagonal metric or the threshold is inconclusive
and ends this one test without retuning. Only a rigorous negative Q
value would challenge positivity; failure of the stronger screening
estimate is not such a value.

Plausible use: a paid finite interscale interaction could inform a
multiresolution assembly beyond L750's corrected IMS rule. Coarse
space, same-scale long-range correlations, other levels, non-neutral
directions, arbitrary-window uniformity and Xi mixed positivity remain
independent. Compare any known finite-window positivity before
approving a reproduction; a covered sign must be cited, not rediscovered.

L744 supplies the normalization and smooth-domain calculation;
L741 supplies supported logarithmic-form definitions, not positivity
at this different length. Piecewise spline form applicability requires
its own check. L750/L752/C998z, L742/L743, C759d and assessment558
are safeguards/contrasts, not sign inputs. Assessment854 records exact
sources, readable versus missing proof cases and duplicates/failures.
Do not repeat ready Schur or ground-state searches. Resolve the missing
construction scope through a readable primary equation-level source,
then approve this exact test as known-machinery specialization or park
it with a specific hypothesis obstruction. Previews are not coverage.

Mathlib matching coverage is not checked. No lemma, mathematical script,
calculation or same-turn approval accompanies this nomination. A future
finite numerical specialization is calculation/standard/high; changed
coordinates alone do not merit creative routing.

## Separate source approval856 — 13 November2026

The current fields and this section supersede the original nomination's
pending gate. The exact TARGET is unchanged. This is one literature-only
review, completed as EXPLORATION: construction coverage became usable,
but no new Weil estimate, diagonal positivity or mathematical certificate
was established. Approve one REPRODUCTION attempt, including its necessary
applicability checks, rather than a reproof of the cited basis theorems.

### Primary statements and essential proof cases actually inspected

Khalidov–Unser, *From Differential Equations to the Construction of New
Wavelet-Like Bases*, IEEE TSP54(4),1256–1267, April2006,
[published author PDF](https://bigwww.epfl.ch/publications/khalidov0601.pdf),
DOI10.1109/TSP.2006.870544: the web index offers an equation-bearing
representation of this same PDF. It resolved the earlier missing-formula
blocker; direct extracted text and screenshot markers did not. Read
III.A p1259, IV.A–B pp1260–1262 and V.A–B p1262. The relevant source
formulas, with T=2^i and c_i the scaling B-spline's L2 norm, are

    phi_i = beta_T / ||beta_T||_2,
    a_i[k] = <phi_i, phi_i(.-Tk)>,
    H_i(z) = 2(c_i/c_(i+1)) product_l ((1+exp(T alpha_l)z^(-1))/2),
    G_i(z) = -z Q_i(z^2) H_i^*(-z^(-1)) A_i(-z),
    psi_(i+1)(x) = sum_k g_i[k] phi_i(x-Tk).

These are source formulas, not a newly derived filter. A_i is the
z-transform of the source autocorrelation sequence; star on a Laurent
filter conjugates coefficients. Use (3) for beta_T, (4) for A_i,
(6) and the following displayed refinement formula for H_i, and
(9) and the displayed formula immediately before Proposition2 for G_i.
The source's detail generator for V_T minus V_(2T) is psi_(i+1),
whose translate lattice is 2T, not T. Preserve the leading factor -z
and the causal scaling-function origin; shifting a generator changes
the prescribed finite selection even if it preserves an infinite basis.

Proposition2 requires the free filter bounded and nonzero on the unit
circle. Its proof compares detail autocorrelations with the three
scaling autocorrelations and the squared free-filter modulus. Read the
whole proof; the indexed intermediate display loses some modulus/square
symbols. It is not an implementation formula or a numerical certificate.
The readable theorem statement and the construction's orthogonality
equation are sufficient theorem inputs, independently cross-checked in
the2005 primary conference paper, Sections2–4 ppIV626–627,
[author PDF](https://bigwww.epfl.ch/publications/khalidov0501.pdf).
The compact branch uses phi and G; the dual branch uses the dual phi
and formula(10), generally with infinite support. IV.B p1262 explicitly
distinguishes these branches and states regularity C^(N-M-2).

Property2 p1262 states exponential-polynomial annihilation for psi_i
with complex conjugation, all real shifts and degrees below each root's
multiplicity. Its proof uses Property1's coarse exponential reproduction,
orthogonality to the coarse space, and shift invariance of the null
space. The displayed psi in that argument is the orthogonal-complement
generator of(9); the label “analysis” alone does not select a dual.
For the compact branch reproduction is locally finite on its support:
the exponentially growing null functions are not being asserted to
belong to L2(R). Do not infer exponential integrability of a noncompact
dual from exponential decay without a rate. No dual is used here.

Followed the relevant cited source: Unser–Blu, *Cardinal Exponential
Splines: Part I—Theory and Filtering Algorithms*, IEEE TSP53(4),
1425–1438, April2005,
[author PDF](https://bigwww.epfl.ch/publications/unser0503.pdf),
III.C, Theorem1, pp1430–1432, and III.C2/Proposition2 pp1430–1431.
The Riesz obstruction concerns distinct purely imaginary root aliases;
the proof's nonzero-real-part case has no such Fourier zeros. Repeated
roots are allowed. The reproduction proof includes repeated-root
exponential polynomials. Proposition2 requires a nonzero exponentially
weighted zeroth convolution moment, weighted absolute integrability and
a summable reproduction majorant. Its proof uses a triangular moment
matrix and Fubini under those conditions; these hypotheses must not be
silently dropped. Its compact real exponential factors fall within the
stated B-spline case. Also inspected Unser, *Part II—Think Analog, Act
Digital*, IEEE TSP53(4),1439–1449,
[author PDF](https://bigwww.epfl.ch/publications/unser0504.pdf),
III.D Theorem1 pp1442–1443 and the four proof cases in prose. The empty
zero vector needs no general rational-extension reproof.

### Applicability scope approved for the later attempt

The target has N=4, M=0, real nonzero roots with multiplicity two and
constant free filter1. These satisfy the inspected source restrictions;
there is no imaginary-alias or unit-circle free-filter obstruction.
Real coefficients remove a conjugation ambiguity in matching the two
pole moments. The later attempt must give the precise conversion from
the source's unit dyadic ladder to base spacing T_0, with roots scaled
in the source coordinate and restored in x. It must use the physical
roots in(3), source normalization and the stated origin; it may not
substitute dilates of a single fixed wavelet for scale-dependent ones.

This authorizes an explicit finite specialization, not a new analytic
claim in this review. Check exact moments from the cited construction
and fixed filter, actual closed supports, all allowed lattice indices
and finite-span independence before evaluating. Retain the full complex
spans. Source C2 regularity and piecewise exponential-polynomial form
provide the appropriate regularity input; the attempt must verify zero
extensions in H2 and passage from compact smooth approximants to the
actual Q formula. For this step reuse Plancherel, standard Sobolev
mollification, L744(8)'s logarithmic symbol bound, finite bounded delays
and finite-interval pole functionals. No extension of L741's positivity
or closed-domain conclusion to this longer interval is authorized.
This is an applicability obligation using covered tools, not an unread
essential domain theorem or assumed positivity.

Read L744's hypotheses and complete smooth formula(6), and L741's
definitions and scope. Keep the actual digamma symbol, dt/(2*pi),
zero extensions and every active von Mangoldt delay. Only exact matching
moments justify eliminating the pole block. The finite Gram/block
reduction and rigorous matrix residual method are covered by the
unchanged ready assessment804, including Andrews–Connes–La Gatta
2611.13129v1 Lemma8.16 and Rump2010 Section10.8/Lemma10.12.
The later attempt must prove the specialization and enclose integration,
infinite archimedean remainders and arithmetic/roundoff errors. An L2
Gram matrix is not a Q metric. The “complete blocks” here include every
direction of the specified finite spaces; they are not all directions
of the ambient form domain. Neither positive definiteness nor a beta
value is an imported premise.

### Stronger results, duplicate/failure screen and source limits

Reuse assessment854's comparison of L750/L752's signed IMS defect,
C998z's unrestricted modulus obstruction, L742's conditional translated
cell nonsummability, C759d's shifted-Schur stop and the two-moment
coordinate warning in assessment557/558. Those mechanisms supply no
signed estimate here; no historical stop is promoted to a global ban.
Ready Schur coverage is used only as finite block machinery, without
importing a positive complement or source numerical arrays.

For overlap, reuse assessment804's theorem comparison and inspect
bramble_trace, *Full-source Schur certificates for Weil positivity at
support radius two*, [paper60/v1](https://rstation.ai/problems/riemann_hypothesis/papers/60),
26 October2026, Theorem1.1/(1.1), (2.1), and its domain/certificate
qualifications. Its endpoint is radius2 for arbitrary complex tests;
this target's centered radius is2log3>2. It supplies neither positivity
on this whole window nor the stricter cross-block threshold. No source
computation was replayed. Positivity for single short-support translates
would likewise not certify the full within-scale metric.

New queries: `"khalidov0601" "pdf"`; `"From Differential Equations to
the Construction" full text`; `"Weil" "positivity" "log" "81"
quadratic form`; `"Weil" "wavelet" "half" positivity`; `"Unser"
"Blu" "Cardinal exponential splines" "Part II" Theorem 1 Riesz`;
the exact PartI URL with `"Theorem 1"` and `"Proposition 2"`;
`"Weil" "positivity" "radius" "2" "log" wavelet`; and
`"Weil" "half-contraction"`. No inspected primary theorem supplies
this fixed half bound. Unrelated and unverified RH claims in results
are not theorem inputs. The distinct primary preprint path
`https://bigwww.epfl.ch/preprints/khalidov0501p.pdf` returned502 and
remains unread. A repeated local download failed DNS; no more download
retry is needed because the published equation-bearing source is now
readable. Screenshot responses without pixels were not evidence.
Matching Mathlib coverage remains not checked, not absent.

### Decision and bounded continuation

Proceed once at the unchanged TARGET, using SPECIALIZE/REPRODUCTION.
Require verified complete positive diagonal Q metrics and an upper
enclosure beta<1/2. A certified pair ratio at least1/2 rejects the strict
estimate, without refuting positivity or RH. Unresolved metrics,
overlapping bounds or incomplete error control are inconclusive and
end this attempt without retuning. A failure of the exact compact
moments ends this nomination, without dual substitution or corrections.
No generic theorem is to be reproved merely to generate a result.

Other levels, coarse/non-neutral components, long-range correlations,
arbitrary-window uniformity and actual-Xi mixed positivity remain open.
No justified creative central proof is ready: there is still no paid
scale-uniform signed mechanism. This fixed test is calculation/standard/
high. The current review spends no mathematical exploration attempt and
does not reset earlier stop evidence or budgets.
