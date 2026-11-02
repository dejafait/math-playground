# Normalized microscopic density contrast: completed source review

TARGET: Assess source coverage for a denominator-weighted microscopic contrast lower bound c T log T with C481a's fixed cutoff.
CHECKED: 2026-10-31
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded searches for the exact normalized sharp-polynomial contrast, triangular-discrimination duals, shifted lower bounds and prime-block bounded probes; checked the density, saturation and grouped-certificate records listed below. No matching theorem was identified; no novelty or falsity is inferred.
SOURCE_EVIDENCE: Read Reid--Williamson JMLR 12 (2011), Table 2 p. 760 and Appendix F (83) pp. 796--797; Curran 2405.08725v1 Theorem 1.1, Propositions 1.2--1.4 and proof outline; checked Curran 2303.10123v2 Lemma 2.3 and adjacent splitting hypotheses; read Villarino math/0504289v3 Theorems 2--4/6 and Section 2.3 proof. Precise sources and limitations below; reuse prior finite mean-square coverage.
COMPARISON: Generic divergence duality supplies no arithmetic separation, and Curran's general shifted lower theorem assumes RH and concerns full zeta. The unconditional finite mean-square interface and classical Mertens second theorem support a concrete prime-block quadratic-dual test of this exact contrast, without Haar transfer or a global fourth-moment denominator; none of its required estimates is established here.
GAP: The normalized c T log T bound remains open. Proposed prime-probe signed correlation, denominator-weighted second moment, boundary-strip errors and finite-measure dual comparison all require proof; no source theorem settles their combination.
REASON: Park direct theorem import; nominate one independently specified prime-block test under a separate ready assessment, requiring separate approval next turn before mathematics. This is bounded source exploration, not a new lower bound or approval of an uncovered derivation.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED covered no source for the nonlinear normalized functional; its essential divergence and shifted-lower-bound hypotheses required inspection.
SCOPE: Real T tending to infinity, L=log T, h=1/L, fixed M=floor(sqrt(T/(2 pi))), J=[T+h,2T-h], F_M=|sum_(n<=M)n^(-1/2-it)|^2 and D_h=F_M(t+h)-2F_M(t)+F_M(t-h). No RH, moving cutoff, independent phases, Haar transfer or full-residual comparison.

## Completed comparison, 31 October 2026

The main gap remains actual-Xi all-degree positivity and initial signs
at unbounded heights. This review retains the exact normalized functional
below. Its plausible downstream use is C481a's missing positive density
mass, followed by its conditional ratio-norm transfer. Full-residual
comparison, both L477 defects, negative-mass saving and all Xi signs
remain independent. L573 removes only the cap-loss obstacle and has
not received a separate critical audit.

### Inspected primary statements and exact scope

Reid--Williamson, *Information, Divergence and Risk for Binary
Experiments*, JMLR 12 (2011), 731--817,
[Table 2, p. 760; Appendix F, (83), pp. 796--797](https://jmlr.csail.mit.edu/papers/volume12/reid11a/reid11a.pdf#page=66).
The table identifies triangular discrimination by f(u)=(u-1)^2/(u+1).
Appendix F gives the convex-conjugate variational representation for
probability measures with densities; it obtains it by substituting the
pointwise conjugate formula, then discusses restriction of the test
class. Read that argument and the bounded variational-distance case.
It gives no positive separation of our two intensities. Our measures
have unequal masses and an additive L in Q_T: probability normalization
and equal-mass affine cancellations cannot be silently imported.
Classical weighted Cauchy--Schwarz is an adequate named supporting
input for a future direct finite-measure quadratic test; its precise
application and integrability checks remain for mathematics.

Curran, *Lower bounds for shifted moments of the Riemann zeta function*,
[arXiv:2405.08725v1, Theorem 1.1](https://arxiv.org/html/2405.08725v1#S1),
14 May 2024: assumes RH, fixed nonnegative exponents beta_k and
|alpha_k|<=T/2, with T sufficiently large in terms of the exponents.
Its lower bound is for products of shifted full-zeta absolute powers.
Read Propositions 1.2--1.4 and the good-set/exceptional-set proof outline:
the latter two propositions retain RH; unconditionally computing the
whole-interval twisted piece does not remove the exceptional-set
obligation. Neither the reciprocal sum denominator nor the sharp
rectangular cutoff is covered. Thus this theorem cannot be imported
unconditionally toward RH. Reuse the earlier Kovaleva/full-zeta
qualifications without reopening unchanged proof passages.

Curran, *Correlations of the Riemann zeta function*,
[arXiv:2303.10123v2, Lemma 2.3](https://arxiv.org/html/2303.10123v2#S2),
gives the unconditional arbitrary-complex-coefficient finite mean square
(T+O(N)) sum |a_n|^2. Reuse its exact statement and Montgomery--Vaughan
coverage from the cap-loss review. Check adjacent Lemma 2.4: its
prime-support splitting requires disjoint prime sets. An all-integer
A_M and the proposed prime probe overlap in prime support, so that
splitting cannot be used. Products must instead be grouped with all
coincidences and their actual lengths; translations need phase factors
and the shortened J interval needs explicit boundary control. Lemma
2.5's unweighted prime moment does not alone control an F_M-weighted
moment. No such weighted estimate is proved in this review.

Classical Mertens second theorem: sum_(p<=x)1/p=log log x+B+O(1/log x).
For an inspected theorem statement and author-written proof, see
[Villarino, *Mertens' Proof of Mertens' Theorem*, math/0504289v3,
Theorem 6, (2.3.4)--(2.3.5), printed p. 7](https://arxiv.org/pdf/math/0504289v3#page=7),
17 May 2005. Read also Theorems 2--4 and Section 2.3's partial-summation
proof, with its bounded weighted-prime remainder explicitly retained
as a named input, not independently audited. It applies to real x>2
and supplies prime reciprocal mass, not a time-correlation theorem.
Import the standard named asymptotic, with no need to reproduce its
proof or use the explicit error constant. Original Rosser--Schoenfeld
PDF access returned a security page; a digitized Mertens PDF returned
404. Neither inaccessible original is used as inspected evidence.
The accessible named-theorem coverage suffices for this proposed use.

### Duplicate and failure comparison

Read C481a and L573 completely; L477's exact hypotheses/conclusion;
L481's concentration statement and finite coefficient interface;
L482 completely; L572's precise statement and its ATTEMPTS record.
Reuse the 31 October microscopic/truncated-density reviews and the
29 October bounded-resonator/weighted-cubic comparisons. The older
fixed-witness clipped-mean review was checked for its actual scope:
it concerns sign-restricted real Hardy jets with fixed small-prime
twists, not the present growing prime block and density contrast.
No jet result or cross-notebook theorem is an input.

Three candidate mechanisms were compared. The unchanged global
second/fourth-moment certificate remains stopped by L481. General
shifted-zeta lower bounds do not cover the target and retain RH. A
short growing prime-block quadratic test has a different signed
correlation and a positive Q_T-weighted norm as its two explicit
obligations; it is selected for a later bounded attempt. This does
not discard the chirped term from any assertion about the full
residual. L482 stops global uniform polynomial saturation with its
stipulated length budget, not every weighted dual. L572 stops its
complete ascending-rank certificate, not the actual ratio norm.

Specific searches included `"Dirichlet polynomial" "triangular
discrimination"`, `"Dirichlet polynomials" "absolute" "small shifts"`,
`zeta normalized intensity shifted moments`, `triangular discrimination
variational representation f divergence`, `Curran shifted moments lower
bounds Riemann zeta function`, `"Dirichlet polynomial" "clipped" primes`,
and `"Dirichlet polynomial" "prime block" "lower bound" "bounded"`.
Several queries returned unrelated results. Generic divergence and
shifted-moment hits were followed to the statements above. Curran's
moment-of-moments paper and Curran--Heycock joint derivative moments
remain unread leads, not theorem inputs. The searches establish no
originality or impossibility claim.

### Concrete continuation and test

Nominate, without proving either estimate, the prime probe

    P_T(t)=-sum_(T^(1/16)<p<=T^(1/8)) cos(t log p)/sqrt(p),

and seek fixed c_1,C_1>0, uniformly at all sufficiently large real T,

    integral_J D_h(t) P_T(t) dt >= c_1 T L,
    integral_J Q_T(t) P_T(t)^2 dt <= C_1 T L.

These are proposed thresholds, not established claims. The intended
method is a direct weighted quadratic-dual comparison for the exact
normalized functional, retaining all prime/product coincidences,
translations, floors and interval ends. P_T itself is an unbounded
finite polynomial; it must not be called a bounded witness. A later
argument must justify how its weighted test controls the normalized
functional and how that functional supplies a bounded density dual.
No clipping estimate or comparison is derived here.

Continue only if both moment obligations and the dual comparison
produce a fixed positive normalized lower scale, or a weaker result
with a precisely stated bottleneck. Abandon this particular probe if
the signed correlation is too small, its weighted cost loses a growing
factor, or the finite-height errors cannot be controlled. No automatic
Haar or independence repair is permitted. The exact attempt and source
scope are in `2026-10-31-prime-block-normalized-contrast-attempt.md`.
It is a newly written ready continuation requiring separate supervisor
approval next turn; this literature-only turn performs no mathematics.
Full matching and supporting Mathlib coverage remain unchecked.

## Original nomination, preserved; pending-review language superseded

The specific proposed test, not a proved estimate, is whether absolute
c,T_0>0 exist such that for every real T>=T_0,

    integral_J D_h(t)^2/Q_T(t) dt >= c T log T,
    Q_T(t)=F_M(t+h)+2F_M(t)+F_M(t-h)+log T.

The denominator is everywhere positive. The intended downstream use is
a normalized bounded dual witness for the actual-height absolute
density difference. Its precise comparison and a lower bound require
review before mathematical work. No normalized lower bound or new
comparison is derived in the nominating turn. L573 controls only cap
loss; it supplies no positive mass for this test.

Search the exact functional and standard terminology such as triangular
discrimination, normalized shifted intensity contrast and bounded dual
tests for sharp Dirichlet polynomials. Inspect primary hypotheses and
essential proof cases of any applicable theorem. Reuse the earlier
shifted-zeta qualifications; do not substitute a full-zeta product
moment for a sharp-cutoff nonlinear absolute functional. Check the
local density reviews and L481/L482/L572 failures before proposing a
method. A claimed difference from those failures must be mathematical,
not merely a renamed route. No novelty follows from an unsuccessful
search.

Essential local inputs are C481a and L573; L477 fixes the surrounding
residual problem. L481/L482/L572 are contrasts unless an actual use is
justified. No cross-notebook input. Mathlib coverage remains unchecked.

Continue only if source comparison identifies an applicable theorem or
a concrete covered bounded test of this exact lower scale. Otherwise
park this mechanism with the precise obstruction or missing hypothesis.
An independently justified subsequent creative attempt would test this
one normalized functional; its decisive evidence must be a rigorous
positive lower scale or an informative obstruction. The central
importance is C481a's still-missing positive mass. Full-residual
transfer, both defects, negative-mass saving and all Xi signs remain
independent unresolved steps.
