# Source comparison: a self-consistent generalized-prime diagnostic

TARGET: Assess whether a discrete Beurling generalized-prime system can have psi_P(x)=x-x^b+o(x^b) for some fixed 1/2<b<7/8 and its own Selberg discrepancy relation with O(x) remainder, distinguishing continuous models and ordinary primes.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reviewed two primary source chains: Broucke–Vindas arXiv:2102.08478v2 and Revesz arXiv:2202.01837v3; searched power-error constructions, prescribed real zeros, generalized Selberg symmetry and discrepancy terminology. Scoped duplicate searches found no prior inspection of these constructions. Queries and exact read ranges appear below; no exhaustive absence or novelty claim.
SOURCE_EVIDENCE: Broucke–Vindas Theorem 1.2, printed p. 2, continuous-measure proof case in Section 2 pp. 4–6, and Section 3 definitions and prime-power conversion pp. 9–10; Revesz Section 1 definitions (1)–(7), Section 7 (48)–(51) and theta/psi conversion, and Theorem 8 pp. 21–22. Versioned primary links and qualifications below.
COMPARISON: Theorem 1.2 supplies actual discrete primes approximating an admissible prime-counting template, unlike L734's independently fixed kernel. It does not itself state the exact coefficient-1 psi asymptotic or displayed O(x) discrepancy relation. Revesz's prescribed-zero formula has coefficient 1/rho, not 1, and is not silently substituted for this target.
GAP: A later specialization must verify template hypotheses, weighted prime-count conversion, finite prime-power tails and a same-system O(x) convolution estimate at real endpoints. No such specialization is proved here. Ordinary integer density, the full increment envelope, prefix transfer and Xi positivity remain outside coverage.
REASON: Essential source access is resolved by a precise discrete construction theorem; a bounded reproduction specialization can now test arithmetic self-consistency. Reproving the random discretization is unnecessary. No generalized Selberg remainder theorem or ordinary-prime transfer is imported.
SCOPE: Completed literature-only comparison; the original coefficient-1 target is preserved. The newly prepared b=3/4 continuation has its own exact-target assessment and requires separate next-turn approval. No new mathematical result, lemma or script is written this turn.
LITERATURE_REASON: At invocation the target changed from an independently fixed ordinary kernel to a self-generated generalized arithmetic system, with essential primary construction and remainder coverage missing; this review supplies construction coverage and isolates the mathematical specialization.

## Completed comparison — step 250

The missing coverage is no longer a source blocker. The decision is to
specialize a known discretization theorem, not to claim a new existence
theorem or to assert that the diagnostic has already been constructed.
The main gap remains unconditional actual-Xi mixed positivity. The
intermediate diagnostic asks whether multiplicative self-consistency
alone rules out a coherent power error in a larger arithmetic category.
Its downstream use is to identify a need for additional ordinary-integer
information, if the diagnostic succeeds. It does not transfer a norm or
a sign to Xi.

### Primary construction input and read limits

F. Broucke and J. Vindas, *A new generalized prime random approximation
procedure and some of its applications*, Math. Z. 307 (2024), Article 62;
inspected version [arXiv:2102.08478v2, 17 June 2024](https://arxiv.org/pdf/2102.08478v2),
Theorem 1.2, printed p. 2. The [HTML text](https://arxiv.org/html/2102.08478v2)
was used for legible formulas and the versioned PDF for pagination.

Its hypotheses on F on [1,infinity) are: nondecreasing, right-continuous,
F(1)=0, F tending to infinity, and F(x)<<x/log x. Its conclusion is a
discrete generalized-prime sequence with |pi_P(x)-F(x)|<=2 for every
x>=1 and the simultaneous estimate, for every real t and x>=1,

    |sum_(p_j<=x) p_j^(-it)-integral_1^x u^(-it)dF(u)|
      << sqrt(x)+sqrt(x log(|t|+1)/log(x+1)).

If F is continuous the primes can be strictly increasing and the
counting error is <=1. This is an existence theorem, not an explicit
numerical prime certificate. No ordinary-prime hypothesis or Axiom A
for the associated integers is imposed by this theorem.

Read the relevant continuous-measure proof case, Section 2 pp. 4–6:
unit-mass F-intervals, independent prime choices, the counting-error
bound, summable exceptional events, and extension from interval
endpoints/integer frequencies to all real x and t. The separate
atomic-template construction is unnecessary for the proposed continuous
template and was not used. Read Section 3 pp. 9–10 through the
prime-power conversion in the proof of Theorem 3.1. That theorem's
special li template is a useful comparison, not our power template;
its N and M bounds are not automatically available here. The later
Perron proof and Section 4 were not needed or imported.

### Arithmetic conventions and the exact remainder sought

The same paper, Section 3 p. 9 and (3.1), uses generalized integers
with multiplicity and Pi_P(x)=sum_(j,k:p_j^k<=x)1/k. For an explicit
free-semigroup formulation, inspected Sz. Gy. Revesz,
*Oscillation of the remainder term in the prime number theorem of
Beurling, caused by a given zeta-zero*,
[arXiv:2202.01837v3, 15 September 2022](https://arxiv.org/pdf/2202.01837v3),
Section 1, (1)–(7), printed pp. 1–3.

Use one formal generator for each prime index j. Distinct exponent
vectors are distinct generalized integers g, even when their real
norms |g|=product p_j^(a_j) coincide. Sums count those formal elements
separately. The unit has norm 1 and Lambda_P(1)=0; Lambda_P(g)=log p_j
if g is the formal power of generator j, and is zero otherwise. Thus

    psi_P(x)=sum_(|g|<=x)Lambda_P(g)
            =sum_(j,k>=1:p_j^k<=x)log p_j.

The convolution meant in the saved target is the multiplicative one:
(f*h)(g)=sum_(de=g)f(d)h(e), with formal factorization in this free
semigroup. In particular, the requested discrepancy expression is

    R_P(x)log x+sum_(|g|<=x)Lambda_P(g)R_P(x/|g|)=O(x),
    R_P(x)=psi_P(x)-x.

This specifies the target, not a proved equation. Both R_P and
Lambda_P must belong to the constructed system, for all sufficiently
large real x, with all atoms at equality included. The sum must not
be replaced by the ordinary integer Lambda sum of L734. The requested
O(x) statement is only this coarse discrepancy relation; it does not
include an unspecified sharper Selberg identity or N_P(x)=floor(x).

### Stronger-looking comparison and its coefficient qualification

Read Revesz Section 7's construction setup, Theorems 6–7, (48)–(51),
and the following theta and psi conversion (pp. 16–17), then Theorem 8
(pp. 21–22). The theorem permits a finite conjugation-symmetric multiset
S in r<Re rho<1, including real points. In its r=1/2 case it states
discrete existence with

    psi_P(x)-x=-sum_(rho in S)x^rho/rho+O(sqrt(x)),

and Axiom A for the generalized integers with every exponent 1/2+epsilon
in (1/2,1). This supplies a source comparison for prescribed real-power
terms, but the coefficient is reciprocal rho with integer multiplicity.
It is not the coefficient 1 required here. No noninteger zero
multiplicity or rescaling of psi is licensed. The full N-estimate
proof and the r>1/2 case are not being imported or independently
audited. The proof's prime-power cutoff shorthand is not adopted:
the continuation must retain the actual first prime p_1>1.

The construction input we select is therefore Broucke–Vindas Theorem
1.2, whose template flexibility avoids importing a differently
normalized prescribed-zero statement. No meromorphic continuation
through s=b, prescribed zero, integer-count error exponent or functional
equation is part of our proposed diagnostic.

### Search, duplicates, and continuation test

Queries included: “Beurling generalized primes psi x x beta Selberg
symmetry formula remainder”; “discrete Beurling primes prescribed zeros”;
“Beurling primes prescribed zeros real zero beta Broucke Debruyne Vindas
discretization”; “Beurling primes Selberg symmetry”; and exact
generalized-prime discrepancy/power-error variants. These found the two
chains above. Search hits on the elementary Selberg lecture archive,
Mertens theorems, short-interval zero density, and the 2025 prescribed
contour paper remain unread leads, not evidence for this exact target.
Beurling–Selberg approximation and Nyman–Beurling results concern other
questions. No inference of novelty is made from unmatched searches.

Scoped searches in drafts/literature, foundations and ATTEMPTS for both
arXiv IDs, Broucke/Vindas and generalized-prime discretization found no
previous primary comparison. Reviewed the earlier prime-variance
assessment's uninspected leads, the Selberg symmetry assessment's
ordinary-kernel qualification, L734's canonical proof/audit and its
coarse-discrimination stop. Existing failure evidence remains intact.
The Tenenbaum assessment is reused as an ordinary-prime comparison;
its theorem is not applied to the new category.

Continue only to a separately approved specialization at b=3/4. A
candidate prime-counting template is nominated in the continuation
assessment; its admissibility and all mathematical consequences remain
proof obligations. Success requires the exact coefficient-1 asymptotic
and the displayed same-system bound, including prime powers and real
endpoints. Failure of template hypotheses, an uncontrolled power tail
or a convolution estimate requiring unproved integer regularity stops
that specialization. No full increment envelope or prefix transfer is
authorized by a successful diagnostic.

Mathlib coverage for this discrete existence theorem and the proposed
specialization is not checked; availability is unknown. There is no
new canonical lemma this turn because source review is the authorized
task. The source theorem must receive its precise citation in any
later canonical specialization; its random construction should not be
reproved without a new need.

## Preserved nomination and prior selection (superseded by review above)

The main gap is unconditional actual-Xi mixed positivity, with actual
upper prefix norms, anchors and complementary residuals still unpaid.
The completed step was only the approved L734 proof audit. The following
comparison selects future work and derives no mathematics on it.

1. **Further coarse fixed-kernel control:** park it. The audited L734
   proves compatibility of exactly the tested O(x) inequality with
   L733's growing prefix. Its canonical stop remains in
   `ATTEMPTS/2026-11-04-coarse-selberg-power-discrimination-stop.md`.
   A different smooth power would not repair self-consistency.
2. **Growing local Hardy derivative realization:** do not reopen the
   specified dictionary. The recorded L639 audit and
   `ATTEMPTS/2026-11-01-growing-hardy-jet-localization-stop.md` give
   projection o(1) through the stated degree range. No new dictionary
   or source input has been supplied here. This is a different sign
   mechanism, but its recorded failure remains in force.
3. **Self-generated generalized arithmetic:** select only this source
   question. It imposes the missing multiplicative consistency in a
   deliberately broader arithmetic category. It is not another test
   of an arbitrary smooth profile against the ordinary fixed kernel.
   If primary sources exhibit the specified common system, that could
   show that this added condition still needs information specific to
   ordinary integer primes. If they do not, do not infer impossibility.

The prior Selberg comparison explicitly distinguishes fixed-kernel
compatibility from self-consistency. The prime-variance comparison,
near its final search paragraph, records generalized-prime hits as
uninspected leads. The Nyman--Beurling approximation assessments do
not cover Beurling generalized prime systems. These observations are
local duplicate checks, not evidence of mathematical novelty.

## Bounded next review and discriminating test

Search the exact power-error construction, its stronger known variants,
and generalized Selberg symmetry/remainder terminology. Inspect primary
theorem statements and the essential discrete-construction and convolution
proof cases before larger extracts. Begin with at most three directly
relevant primary constructions or source chains. A title, abstract,
continuous example or ordinary-prime citation is not coverage.

The source review must say precisely what counts as a discrete prime
multiset, how repeated factorizations are counted, how psi_P and the
convolution sum are defined, and whether the asserted asymptotic and
O(x) remainder hold for that same system at all sufficiently large real
x. If normalization or the remainder differs, preserve the exact
statement and identify the difference; do not silently alter this target.
The b-range is part of the proposed diagnostic, not a claimed zero-free
region or an imported ordinary-zeta theorem.

Continue to a separately gated mathematical specialization only if a
precisely cited construction and remainder provide adequate coverage,
or a bounded search isolates a concrete additional difference worth
testing. Otherwise record the missing condition or source obstruction
and park that dependent target; do not repeatedly retrieve blocked
sources. No conclusion about ordinary primes follows from a generalized
countermodel. L733's increment envelope and the transfer to a growing
discrete prefix would remain separate obligations even after existence.

L733 and L734 are diagnostic background, not assumptions about a new
arithmetic system. Their results cannot be transferred by renaming F.
The proposed downstream use is to discriminate structural hypotheses,
not to establish an actual-family norm or Xi sign. Matching Mathlib
coverage for the new target is unchecked, with availability unknown.

No controlled actual projected remainder or paid coercive term has been
identified, so a central creative proof attempt is not yet justified.
Next routing is standard/high literature_comparison. Any eventual
creative nomination needs its own exact claim, bounded test and source
gate; this REVIEW_REQUIRED nomination supplies none of those approvals.
