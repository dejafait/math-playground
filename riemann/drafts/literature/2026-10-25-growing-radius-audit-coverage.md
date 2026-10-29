# Growing-radius component — completed source-scope approval

TARGET: Critically audit the growing-radius Stirling, amplitude and complementary-arc bounds in bramble_trace v4 Section 4.2 for fixed c_0>1/2 and c_0<=2p/log(t/(2pi))<=log(t/(2pi))^2, including the Xi gauge.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the initial-sign, L463 application and Section 4.3 assessments; searched the named October 24 theta assessment, local foundations and relevant masking/count failure records. Targeted external queries returned the same manuscript with a stale v2 preview; its primary page was read as v4. No inspected stronger substitute supplies an independent audit of these estimates.
SOURCE_EVIDENCE: bramble_trace, Generalized Laguerre positivity at growing orders, paper 41, displayed v4, 24 October 2026 07:18 UTC, definitions (1)-(2), (8)-(18), full Section 4.2 (18a)-(18b) and Section 4.4; NIST DLMF 5.11.1-5.11.2 and 5.11(ii), 25.2.1, 25.2.6-25.2.7 and 25.2.11; Titchmarsh-Heath-Brown (1986), (1.1.4), p. 3, Theorem 3.5 and its proof, pp. 49-50, and Section 5.1 (5.1.1)-(5.1.5), pp. 95-96. Source qualifications and inspection limits below.
COMPARISON: The source already claims the exact growing-disk estimates for every fixed A>0, hence states the A=2 target. L464 independently checks only the product tail. L463 checks application of a stronger conditional theorem, while its source estimates remain unaudited. Classical sector Stirling, absolute Dirichlet convergence, near-one bounds and convexity cover the ingredients, not their full growing-domain assembly.
GAP: No essential source blocker remains for this exact audit. Uniform branches, all error constants and derivatives, arc geometry, the near-one transition, the Cauchy normalization and the Xi gauge still require mathematical verification; source coverage is not a correctness verdict.
REASON: Approve one bounded REPRODUCTION audit of this previously unaudited component. Reproof is justified to check load-bearing uniform estimates rather than claim a new sign theorem. The unchanged target is ready for a later research invocation, with no derivation in this literature-only turn.
SCOPE: Exactly the saved TARGET, with fixed c_0>1/2, A=2, ell=log(t/(2pi)), R=ell^2, n=2p and t tending to positive infinity; local analytic Hardy branches and the actual entire Xi, central zeros allowed, no external fixed zero-free premise. Section 4.5 and endpoint or effective-onset claims are excluded.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED nomination and the Section 4.3 assessment exclude this distinct growing-radius analytic audit; exact essential Stirling, near-one and convexity source coverage was missing. Reuse prior theorem comparisons and resolve only that missing scope.

## Original nomination and present decision

The main gap is still initial actual-Xi signs at unbounded heights,
effective bounded-height overlap and global mixed positivity. This
intermediate target would check the analytic component that bridges
an unconditional proportional-logarithmic order range to L464's
logarithm-squared tail. It would not imply initial signs or RH.

Scope retained after review: t tends to infinity, p is an integer,
n=2p, ell=log(t/(2pi)), and c=n/ell lies in [c_0,ell^2], with
fixed c_0>1/2. Recover the definitions and exact branches in source
(8)-(18), rather than importing constants from fixed-radius estimates.
Determine coverage for the uniform gamma derivatives, zeta estimates
on all needed complex arcs, the positive amplitude, and the Xi gauge.
Section 4.5's fixed-half-plane improvement is outside this target.

Available local context is L018 and L464; L463 supplies the import
context only. No external strict Re(s)>7/8 theorem is needed for
this unconditional Section 4.2 audit. The nomination originally left
essential analytic inputs unidentified; the comparison below resolves
that source gate only. No mathematical audit verdict is given here.
Full matching Mathlib coverage remains unchecked.

The approval test was exact primary-source coverage and a bounded
audit plan for every uniform estimate. That test passes, so retain the
unchanged target under SPECIALIZE for REPRODUCTION. The later audit
should continue only if all bounds hold with constants independent of
t and the allowed order. A failed branch, transition, gauge cancellation
or uniform error bound requires recording the precise failure or
narrowing the conclusion, not treating the source statement as proof.

## Primary texts and precise source cases

The [primary manuscript](https://rstation.ai/problems/riemann_hypothesis/papers/41)
still displays v4, 24 October 2026 07:18 UTC, accessed 25 October.
Read definitions (1)-(2), the full shifted identity and fixed-radius
argument (8)-(18), all of Section 4.2, and the Section 4.4 overlap.
The search result preview instead displayed v2; it supplies no v4
coverage. The author/platform identification is retained, without a
claim of journal verification. The closing participant note expressly
distinguishes numerical controls from verification of uniform estimates.

The source uses gamma(z)=pi^(-z/2)Gamma(z/2), s=1/2+it,
X_y=gamma(s+y)gamma(1-s+y)/(gamma(s-y)gamma(1-s-y)),
H_y=X_y^(-1/2), with H_0=1. Its identity (9) is
P_t(y)=H_y^(-1)zeta(s+y)zeta(1-s+y), P_t(-y)=P_t(y).
Equation (12) defines E_t(y)=exp(-ell*y)P_t(y).
These definitions and the local Hardy branch must be retained exactly;
the notebook coefficient index is p, whereas n in this source is 2p.

For fixed A>0 and R=ell^A, Section 4.2 claims on |y|<=2R that
the analytic logarithm of H_y^(-1), anchored at zero, differs from
ell*y by O_A(R^2/t), with first derivative O_A(R/t), in (18a).
For fixed beta with c_0*cos(beta)>1/2, (18b) claims a positive
height-independent lower bound for E_t(c), a bound for c*|E_t'(y)|,
and relative angular Lipschitz control on the positive saddle arc
and segments to c. These are the exact claims to audit, not estimates
established by this review.

The complementary-arc paragraph splits u=Re(y)>=0 at u=1/2.
It invokes convexity in the lower portion and near-one/absolute
convergence bounds above it, retaining exp(ell*u). The claimed fixed
exponent gap is min(c_0-1/2,c_0*(1-cos(beta)))>0.
The Cauchy normalization costs O(sqrt(n)), not an arbitrary constant
depending on a growing c. The gauge paragraph claims
(log b)''(z)=O(t^(-2)) on |z-t|<=2R and a symmetric ratio
1+O_A(R^2/t^2), with corresponding derivative control. Its final
relative error is O_(c_0,A)(ell^(-1/2)). The A=2 case alone is
approved here. Section 4.4 states the overlap with the product tail;
no new assembly or effective overlap was proved in this review.

## Classical coverage and applicability limits

1. [NIST DLMF 5.11](https://dlmf.nist.gov/5.11), equations 5.11.1
   and 5.11.2 and section (ii), gives log-Gamma and digamma expansions
   in a closed sector |arg z|<=pi-delta, with complex remainder
   bounds. Read the sector/branch conditions and remainder cases.
   This is the correct source for growing real parts; 5.11.9 explicitly
   assumes bounded real parts and is insufficient by itself. Its
   application must place all four half-arguments in fixed sectors,
   keep them away from poles, and use compatible analytic logarithms.
   Higher derivatives may use Cauchy's standard derivative estimates
   on larger sector disks; differentiating an unspecified real big-O
   is not authorized. Existing foundations already record this tool.
2. [DLMF 25.2](https://dlmf.nist.gov/25.2), equations 25.2.1 and
   25.2.11, gives the Dirichlet series and Euler product for Re(s)>1.
   Titchmarsh, second edition revised by D. R. Heath-Brown (Oxford,
   1986), [equation (1.1.4), printed p. 3](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=6),
   gives the reciprocal Mobius series in that same domain, with its
   absolute-convergence justification. Its primary passage was read.
   DLMF 25.2.6-25.2.7, also read, explicitly states the differentiated
   Dirichlet series in Re(s)>1. These cover source ingredients for the
   lower amplitude and bounded factors; their uniform bounds and
   derivative decay as Re(y) grows are application checks, not a
   theorem about Re(s)<=1.
3. [Titchmarsh, Theorem 3.5 and proof, pp. 49-50](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=29)
   gives zeta(s)=O(log t) uniformly for
   1-A/log(t)<=Re(s)<=2, t>t_0, fixed A>0. The theorem and its
   Euler-summation proof through the N=[t] estimate were read, along
   with the following derivative remark. This supplies the near-one
   transition, not reciprocal control on that strip. Source heights
   are t+/-Im(y), so comparability and both signs must be checked;
   conjugation is available for the negative sign. Farther to the
   right use the convergent series, rather than extend this theorem
   to an unbounded real-part interval without justification.
4. [Titchmarsh, Section 5.1, pp. 95-96](https://sites.math.rutgers.edu/~zeilberg/EM18/TitchmarshZeta.pdf#page=52),
   (5.1.1)-(5.1.5), gives finite-order growth, the growth-exponent
   convexity discussion and the classical exponent (1-sigma)/2
   on 0<sigma<1 with any fixed positive exponent loss. This passage
   and its functional-equation and boundary cases were read in text;
   screenshot requests supplied no additional readable evidence.
   Reuse its existing assessment in the October 5 source review.
   The named Phragmen-Lindelof convexity principle is the supporting
   theorem; uniformity in sigma on the required fixed strip and
   shifted heights must be written out in the audit. Nothing here
   imports Lindelof's hypothesis, which the book separately labels.

These inputs do not require RH, a new zero-free region, negative
moments, or an approximate functional equation with growing shifts.
The exact assembled analytic estimate is already claimed by paper 41;
an independent reproduction is justified because it remains a
load-bearing unaudited source component, not because of novelty.

## Duplicate/failure check and bounded audit plan

Reused the [initial-sign comparison](2026-10-25-initial-laguerre-sign-coverage.md),
[L463 application coverage](2026-10-25-l463-import-audit-coverage.md)
and [product-component coverage](2026-10-25-local-factor-coefficient-audit-coverage.md).
Read L018's full statement/proof and L464's hypotheses/conclusion;
neither contains these growing-radius analytic bounds. The October 24
whole-plane theta assessment compares v3's fixed pointwise range and
different moving theta bands; it is not an independent proof of v4
Section 4.2. No cross-notebook theorem is used.

The September 23 first-sign masking and September 27 count/gap
failure records were read for their exact scope. Their canonical
countermodels L251/L354, plus the prior assessment's L257/L260
qualifications, stop generic sufficiency claims, not this actual-Xi
component audit. L462's fixed-anchor small-tail stop is unchanged.
No historical stop is treated as a global ban and no old route is
reopened. Initial signs, the endpoint, effective height overlap and
global mixed positivity remain missing even if this audit passes.

The later audit has one coherent bounded test: reproduce only the
A=2 component with every constant uniform in the saved range.
Check (8)-(9)'s branch/identity on the enlarged disks, then (18a)'s
complete analytic errors; (18b)'s arc-segment geometry, inverse lower
bound and derivative; the whole complementary arc including the
near-one transition and factorial normalization; and (17)-(18)'s
gauge and derivative cancellation on the growing domain. Retain
positive normalization even at central Xi zeros. Use L018 for the
completion; L464 is downstream context for a possible later overlap,
and L463 is source-import context only. Independent full-source and
external-zero-free audits remain excluded. Store a successful audit
with full proof, hypotheses and Mathlib qualification in a later
canonical lemma; this turn writes no lemma or mathematical script.

Queries actually made on 25 October 2026:
- "Generalized Laguerre positivity at growing orders" "Stirling"
- Riemann zeta convexity bound uniform 1/2 1 Titchmarsh theorem 5.1
- "Generalized Laguerre positivity at growing orders" "growing"
- "Laguerre" "Xi" "growing orders" saddle Stirling

Other returned surveys, growth databases and author-profile results
are unimported leads. They add no needed coverage, so no larger
passages or reference chains were pursued. No exhaustive search or
novelty finding is claimed. Full matching and supporting Mathlib
coverage were not checked; unknown availability is not absence.

Outcome: EXPLORATION, LITERATURE, REPRODUCTION: new source-scope
comparison, with no new mathematical theorem or audit verdict. The
unchanged Next action is now ready under SPECIALIZE; a separate
research invocation, subject to the supervisor's approval, performs it.
