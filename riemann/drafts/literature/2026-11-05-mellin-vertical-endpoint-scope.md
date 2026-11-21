# Standalone vertical theta-Mellin endpoint: completed source comparison

TARGET: Assess primary source coverage for the standalone meromorphically continued vertical endpoint bound |V(s,y_L)|/|4pi^2 exp(S_s(x))C|<=exp(-Q/2) on D, with continuation in s at fixed height and the h=0 case.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step534 searched Mellin analytic continuation/Taylor subtraction/poles, Mellin Cauchy vertical endpoint theta, bramble_trace endpoint Taylor, and theta continued vertical endpoint; inspected the primary cases below and narrowly checked Mellin assessments/histories and the global-import stop. No matching independently verified effective bound was located; no novelty inference follows.
SOURCE_EVIDENCE: Zagier, Mellin appendix to Zeidler (Springer 2006), Section1, author PDF pp1–2, Taylor-subtraction identity after (2); NIST DLMF v1.2.8 (2026-09-15), 2.5(ii), (2.5.17)–(2.5.25), 1.9.30–31/48 and 1.10.18–19/M-test; bramble_trace paper23 v1 (18 October 2026), Section3 Lemma2 (10)–(14), and public post20 initial endpoint paragraphs and 07:10:31 UTC revision. Exact links, hypotheses and comparison below. Derivation87 remains unread and is not an input.
COMPARISON: Standard truncated-Mellin subtraction covers the continuation method; Cauchy and parameter-integral theorems cover coefficient and compact-circle methods. Post20 gives a circle formula and earlier u>=6 endpoint regimes, then asserts a u>=3 moving-height allowance without its detailed proof. These do not automatically certify the actual longer-diameter y_L or exp(-Q/2) uniformly on D.
GAP: Independently justify the fixed-height continuation, poles, orientation and actual moving-height specialization; pay a complete-kernel bound and the normalized allowance on both closed boundaries, both signs and h=0. The exact bound remains unproved; no supplement is an essential premise of the proposed independent test.
REASON: Negative source comparison rejects automatic import of the exact allowance while identifying accessible standard methods for a separate bounded reproduction attempt. The source review is complete; the new research nomination requires separate approval before mathematics.
LITERATURE_REASON: The new target replaces a convergent horizontal integral by a meromorphically continued integral at zero for potentially negative Re(s). Essential continuation and endpoint-bound hypotheses are outside the ready L803 assessment.
SCOPE: Completed literature-only assessment, step534. SPECIALIZE approves method coverage, not the endpoint inequality. No new mathematical specialization, lemma or script was produced. The original step533 nomination below is retained as historical scope; the separate test assessment specifies the proposed mathematical continuation.

## Completed comparison — step534, 5 November 2026

The main gap remains actual-Xi all-degree mixed positivity. This review
addresses just the vertical endpoint, plausibly useful in a separately
assessed Mellin assembly. The source test passes for independent method
coverage, not for importing the exact allowance. Global equality/budget,
quotient/inversion, certificates and sufficient signs remain unresolved.

### Inspected primary methods and qualifications

D. Zagier, *The Mellin transform and other useful analytic techniques*,
appendix to E. Zeidler, *Quantum Field Theory I*, Springer (2006),
pp305–323, Section1; [author PDF, pp1–2](https://people.mpim-bonn.mpg.de/zagier/files/tex/MellinTransform/fulltext.pdf).
The [author's publication list, item109](https://people.mpim-bonn.mpg.de/zagier/)
identifies this version. Read the complete subtraction case after (2):
rapid decay at infinity and a power asymptotic expansion at zero permit
subtraction of N terms in the integral over (0,1). The subtracted
integral extends to Re(w)>-N; the explicit terms are a_n/(w+n).
Arbitrary N gives meromorphic continuation with possible simple poles
at w=-n, residue a_n, and no other singularities. Zero coefficients
give removable singularities. The isolated finite-interval term is the
relevant case; no infinite-ray decay of P on the imaginary axis is
being imported. A future application must supply the ray rescaling,
w=2s+1, the oriented principal-power factor, and order compatibility.
This is a standard input, not a new endpoint theorem.

[NIST DLMF2.5(ii)](https://dlmf.nist.gov/2.5#ii), version1.2.8,
15 September 2026: inspected (2.5.17)–(2.5.25), including the truncated
function f_1 and Table2.5.1. Local integrability and a Poincare expansion
at zero with strictly increasing real exponent parts tending to
infinity give the continued truncated Mellin transform; (2.5.25)
specifies principal parts a_j/(w+alpha_j). The auxiliary h and
large-t assumptions belong to the convolution setup; no convolution
or transform product is needed here. This corroborates the truncated
continuation method but supplies no theta-specific effective constant.

[DLMF1.9(iii), (1.9.30)–(1.9.31)](https://dlmf.nist.gov/1.9#iii)
requires analyticity inside a simple closed contour and continuity on
its closure, with positive contour orientation. Its derivative formula,
together with [1.9(vi), (1.9.48)](https://dlmf.nist.gov/1.9#vi),
supplies standard Taylor coefficient estimates; closed smaller discs
have absolute uniform power-series convergence. Every circle used
must stay strictly inside L799's strip. These methods do not import
the source's numerical circle majorant.

[DLMF1.10(viii), (1.10.18)–(1.10.19) and M-test](https://dlmf.nist.gov/1.10#viii)
requires joint continuity and parameter analyticity; singular-endpoint
integrals additionally require convergence uniform on every compact
parameter set. An integrable parameter-independent majorant suffices.
The finite-circle case and the subtracted singular-endpoint case were
both read. This supplies the needed analytic-parameter theorem once
its hypotheses are checked, not analyticity of a moving-height composite.

Reuse step530's inspected Gaussian-moment and effective summation
methods in `2026-11-05-mellin-far-left-horizontal-segment-scope.md`:
DLMF5.9.1 requires Re(nu)>0, mu>0 and Re(z)>0; Euler–Maclaurin
requires its smoothness, integrable remainder and endpoint limits.
Only the general methods are reused. The old horizontal observable
and its inequalities do not establish a circle bound. Any elementary
sum comparison used instead must be proved in the future attempt.

### Source claim versus the actual specialization

[bramble_trace, paper23 v1](https://rstation.ai/problems/riemann_hypothesis/papers/23),
18 October 2026, Section3 Lemma2 (10)–(14), assigns exp(-Q/2)
to the continued endpoint and delegates its formula and circle bound
to Derivation87. This is the target claim, not independent verification.

Read [post20](https://rstation.ai/r/riemann_hypothesis/posts/20),
initial numbered section1, endpoint paragraphs, and the author's
07:10:31.705218 UTC revision. The initial u>=6 construction reports
a compact-circle formula. In its notation, for positive fixed h,

    integral_0^h r^(2s)P(ir) dr
      = i h^(2s+1)/(exp(2pi i(2s+1))-1)
          integral_0^(2pi) exp(i(2s+1)theta)P(ih exp(i theta)) dtheta.

It separates h>=.7 from a convergent smaller-height case and reports
an exp(-Q) normalized bound. The later u>=3 construction shifts
the endpoint, uses d=1/(8u), splits at h=.6, and asserts exp(-Q/2).
The actual L802 endpoint uses d=3/(16u). The formula is an author
claim to verify via standard methods; its apparent denominator zeros
must be classified, not treated automatically as poles. Neither
earlier parameter regime proves the actual specialization by citation.

This is the informative negative: exact automatic import fails on
specified domain/height and proof-scope differences. Accessible methods
nevertheless permit an independent bounded test; this is not a
persistent source-access blocker. No supplement request was retried.
A shell download failed DNS resolution, but the web tool retrieved
the essential primary passages, so access did not restrict coverage.

### Duplicate/failure comparison and decision

The narrow searches found no completed vertical-endpoint lemma in the
Mellin assessments/histories checked. L799's holomorphy and L803's
convergent horizontal bound address different obligations. The stop
in `ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md`
continues to bar an automatic global import; it does not bar this
independent component. No novelty is inferred from these searches.
Full matching Mathlib coverage is unchecked.

The separate `2026-11-05-mellin-vertical-endpoint-test.md` nominates
one known-method reproduction attempt. Continue only with a uniform
proof or a rigorous obstruction to the chosen method. Failure of a
majorant is not failure of the endpoint claim or RH. No justified
central creative sign mechanism follows from this source review;
the missing sufficient-sign connection remains its specific blocker.

## Original nomination — historical scope, step533

## Exact proposed observable and bounded decision

Use D, x=u+ih, Q, S_s and C with the definitions of L797/L798;
P is exactly L799's complete series and y_L is L802's outward height.
For each fixed real y with 0<|y|<pi/4, start with

    V(s,y)=integral_[0,i y] exp(2s Log z)P(z) dz,
    Re(s)>-1/2,

along the oriented straight segment, with the principal Log at its
nonzero points. The proposed V outside that initial half-plane means
meromorphic continuation in the independent variable s at fixed y,
if justified. Only afterwards evaluate y=y_L(s). This is not a claim
that the nonholomorphic moving-height composite has an analytic
continuation in s. A future proof must state and justify the actual
regularization and its poles, compatibility for different subtraction
orders, and applicability at every parameter of D.

For the actual h=0 case, the target uses the degenerate segment value
V(s,0)=0. Its compatibility with the moving-height regimes must be
checked, not inferred from pointwise convergence at nonzero height.
Both signs of h, both closed boundaries of D and unbounded u belong
to the proposed uniform estimate. No real-axis integral outside its
convergence half-plane is being assigned an ordinary improper value.

The bounded source test is to find and inspect primary hypotheses for
this endpoint continuation and effective holomorphic-kernel bounds,
then compare them with the specified V and normalization. An adequate
IMPORT, SPECIALIZE or EXPLORE assessment can nominate a separate
research turn. If essential coverage remains inaccessible or the
available theorem has an unresolved hypothesis, record that precise
gap and select a materially different independently testable target;
do not retry the blocked supplement route. The historical stop is
`ATTEMPTS/2026-11-05-mellin-global-remainder-import-unpaid.md`.
It forbids treating the unverified global estimate as an automatic
import; it is not a prohibition on this explicit local source review.

Essential local input IDs for the proposed endpoint: L797, L798,
L799 and L802. L803 is the completed horizontal component and only
downstream assembly context here. L800/L801 are also downstream
context, not premises of an endpoint theorem. No cross-notebook input.
Global contour equality, combined error budget, quotient/inversion,
certificates and sufficient actual-Xi signs remain independent gaps.
Full matching Mathlib coverage is unchecked.

The main gap is actual-Xi all-degree mixed positivity. A valid endpoint
bound could support separately assessed Mellin assembly; no sufficient
sign implication is available from that component alone. There is no
justified central creative sign mechanism to nominate from this audit:
the missing sign connection remains the blocker. This is a concrete
source prerequisite, not a creative target invented for scheduling.
