# L504 residual on the normalized rectangle-positive class: source comparison

TARGET: Review source coverage for E_a(f)<=C_R a M(f) on L504's H_a, uniformly in T and f, using the rectangle positivity constraint.
CHECKED: 2026-10-30
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused parent Poisson/evaluation coverage and local failures; fresh exact-class, positive-real-part, constrained-duality and boundary-multiplier searches below found no matching quantitative theorem. This does not establish novelty.
SOURCE_EVIDENCE: Freshly read Goberna--Volle, arXiv:2106.14573v1, Example 1.2, Lemma 2.1, Propositions 2.1/3.1/3.2 and Remark 3.1, printed pp. 3--9, including relevant proofs; reused the parent Brevig et al. v2 pp. 12--15 and ABR second edition pp. 119--120 comparisons with their exact scope.
COMPARISON: No inspected theorem supplies the constrained uniform upper bound. Evaluation duality is unconstrained; positive Poisson representation cannot cross the signed gap; general infinite-program duality needs qualifications and supplies no O_R(a) estimate or quantitative measure certificate here. L504's full-space obstruction is not a positive-class counterexample.
GAP: The one-sided E_a<=C_R a M estimate on genuine H_a remains open. A bounded two-height positive-multiplier certificate test is specified separately; failure of that family would not refute this estimate or the weaker Q bound.
REASON: Essential comparison is complete for an elementary explicit-certificate test, with no persistent source blocker. A new nomination exploits positivity above b rather than repeating the stopped b-level residual. No theorem, construction, counterexample or originality is established in this literature turn.
SCOPE: Source comparison for the exact displayed bound. The separately saved two-height test requires approval on a later invocation; no separation equivalence, arbitrary-measure closure, L503 audit, detector-cost theorem or arithmetic transfer is covered.
LITERATURE_REASON: The supplied next assessment was REVIEW_REQUIRED: the changed one-sided normalized positive class lay outside the prior full-space audit and required essential constrained-duality coverage.

## Exact retained hypotheses and essential input

Use the definitions and audited identities of L504. Fix R>0; let
L=log T, a=log L/pi, b=a/4, B=L/(4pi), lambda=pi/(2a), and
K(x)=1-(sin(pi x)/(pi x))^2 with K(0)=0. The real vector space V_R
consists of even entire f, real on R, whose inverse Fourier data are
in C_c^infinity with support in [-R,R] in the 2pi convention. There
is no uniform Fourier-derivative bound. H_a imposes

    Re f(x+iy)>=1 for |x|<=a and b<|y|<B.

The lower normalization 1 is retained; H_a is not closed under sign
reversal or arbitrary positive rescaling. With M(f)=integral |f(x)|K(x)dx,
Q_a and the positive boundary measure mu_a exactly as in L504, consider

    E_a(f)=Q_a(f)+integral Re f dmu_a <= C_R a M(f)

for all f in H_a at every sufficiently large real T. The constant and
onset may depend on fixed R but not on f or T. No sign in the gap or
outside the rectangle may be added. L504 is the sole essential local
input; its audited Q_a<=E_a would turn this bound into the proposed
conditional gap estimate. L503's downstream detector-cost use remains
prospective and unaudited; no conclusion of L503 is needed for this review.

## Bounded comparison and routing test

Inspect applicable primary results on one-sided boundary estimates with
continuum harmonic positivity constraints, and compare any constrained
Paley--Wiener dual formulation with the exact weight and moving geometry.
Reuse the parent source evidence rather than repeat its general searches.
An unconstrained absolute norm or a formal residual is insufficient.

The discriminating future mathematical test would be the stated uniform
upper bound or genuine H_a functions with E_a(f)/(a M(f)) unbounded;
neither is asserted or approved here. In particular, the sign-indefinite
V_R tests in L504 cannot settle this target. A refutation of this stronger
residual bound would still not by itself refute the weaker bound for Q_a.
Do not reopen the stopped full-space estimate under a different name.

## Completed bounded review, 2026-10-30

The local check read L504's hypotheses, identities and full-space proof,
its clipped-certificate failure record, and the relevant parts of
`2026-10-30-signed-gap-flux-conditional-bound.md` and
`2026-10-30-signed-rectangle-absolute-cost-review.md` in this directory.
These retain the known failures; no positive-class counterexample or
two-height certificate was found in those scoped records. The narrow
L503 norm-conversion paragraph was also inspected as supporting context;
no L503 conclusion is imported or audited here. No cross-notebook input.

Fresh queries included `bandlimited entire functions positive real part
rectangle integral inequality one sided`, `Paley Wiener space positivity
constraints complex domain convex duality harmonic function inequality`,
`"entire functions" "positive real part" rectangle inequality`,
`"Paley-Wiener" "cone" "positive" duality extremal`,
`"semi-infinite" "duality" "Slater" measure compact constraints norm`,
`"positive harmonic" rectangle boundary negative part estimates`,
`"bandlimited" "rectangle" "positive" "real part"`,
`"Poisson" "positive" "Paley-Wiener" extremal duality`,
`"positive real part" "exponential type" inequality rectangle weighted`,
`"Paley-Wiener" "positive" "Lagrange" constraints`,
`"strip Poisson" "positive" "extremal" entire`, and
`"entire functions" "rectangle" "one-sided" inequality`.
An approximation-oriented query also tested `Runge approximation entire
functions exponential type real axis small positive rectangle`.
No exact match was identified. Search snippets are discovery only.

### Fresh primary comparison: infinite constraints

M. A. Goberna and M. Volle, *Duality for convex infinite optimization
on linear spaces*, [arXiv:2106.14573v1, 28 June 2021](https://arxiv.org/pdf/2106.14573v1),
Example 1.2, Lemma 2.1, Propositions 2.1/3.1/3.2 and Remark 3.1,
printed pp. 3--9. The setting is a real linear space with proper convex
objective and constraints. The conic dual uses finite-support nonnegative
multipliers. Its corrected limiting formula ranges over finite subsets;
Example 1.2 shows a duality gap for the all-constraint relaxation formula.
The sup-dual uses h=sup_t f_t. Proposition 3.2 assumes one point satisfying
f_t<=-alpha for every t, with alpha>0, and gives attained sup-duality and
the relaxation limit. Read the product-topology argument, finite-subset
formula proof, scalar value-function proof and strong-Slater case.

This is a comparison, not an application: no qualification, multiplier
attainment, or uniform quantitative bound for our H_a has been verified.
In particular it cannot turn sampled constraints or a formal dual into
the required continuum certificate. A v3 URL failed (404); the sole
posted v1 was then accessed. No source blocker remains for an explicit
certificate calculation, which need not assert strong duality.

### Reuse and unread leads

Reuse the parent review's inspected Brevig et al. Theorem 3.10 endpoint
warning and ABR Theorem 6.13(a)/Corollary 6.15 domain restriction, as
summarized above. Their limitations persist under the present constraints;
no repeat source audit or reproof is needed. General Runge approximation,
real-axis sign extremals, finite-dimensional semi-infinite optimization
and positive harmonic boundary-asymptotic leads did not identify an
applicable quantitative theorem in the retrieved records. Their full
theorems were not inspected or imported. None is an essential premise of
the nominated explicit kernel test. Search failure is not nonexistence
of a relevant theorem, and EXPLORE is not certified novelty.

### Bounded continuation and stop

The next nomination is
`drafts/literature/2026-10-30-l504-two-height-positive-multiplier-test.md`.
It asks for one test of an explicit two-height family, adding positivity
information at 2b to the stopped b-level residual. It is an established
duality-route development, not a newly justified central creative mechanism.
The source comparison is adequate for that explicit computation without
assuming a duality equivalence; a different target needs new coverage.

Continue only on a uniform O_R(a) weighted functional bound or a rigorous
uniform obstruction for the entire nominated coefficient family. Stop
that family after one bounded attempt without such evidence. A failed
certificate is not a positive-class counterexample. Actual-Xi signs,
negative zero contributions, moving-test errors and height transfer
remain independent. Full Mathlib coverage is unchecked. No mathematics,
lemma or mathematical script was produced in this review.
