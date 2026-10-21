# Supported Kummer containment — completed source comparison

TARGET: Determine whether the full two-descent Kummer image of E0(K) lies in L074's W_S, retaining all primes above 2 and 11.
CHECKED: 2026-10-15
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the Simon support-theorem records in the ordinary-unit and eleven-adic assessments; compared the scoped TARGET/COVERED_TARGET fields and ATTEMPTS/032–033; searched the full paper title with prime ideals/1.4 and Simon Proposition 1.4 Disc elliptic, then inspected the primary theorem and complete proof.
SOURCE_EVIDENCE: Denis Simon, Computing the rank of elliptic curves over number fields, LMS J. Comput. Math. 5 (2002), 7–17, published 17 April 2002, Sections 1.1–1.2, Propositions 1.1–1.4 and Remark 1.5, printed pp.8–9; primary publisher PDF and exact read scope below. L069 supplies the saved integral irreducible model and its discriminant; L074 supplies the supported-space definitions.
COMPARISON: Simon Proposition 1.4 already controls the full global Kummer image with a potentially smaller exceptional support, while Propositions 1.1–1.2 supply the origin and norm clauses. The fixed-model application is within that theorem's scope; neither a new support theorem nor a local split-algebra extension is needed. L074 alone supplies no such containment.
GAP: A later application must explicitly match the fixed generator/model, compare the theorem's support with all primes above 2 and 11 using L069's saved discriminant, and translate its square-norm conclusion into L074's W_S. This review does not execute that application or compute any dimension.
REASON: Essential primary coverage is adequate for a later KNOWN_IMPORTED application of the existing theorem; no reproof or new mathematics is justified for the containment target.
LITERATURE_REASON: At invocation the required conclusion changed from an abstract supported norm-kernel quotient to full elliptic Kummer containment; the necessary support theorem had not been assessed for this exact target.
SCOPE: Exactly TARGET for L033's entire K, L069's fixed theta and monic irreducible cubic, and L074's maximal-ring support above 2 and 11; full global points including O and coordinate denominators. Only a KNOWN_IMPORTED applicability argument is approved, without deleting support or computing units, classes, local intersections or rank.

The main gap is primitive integer emptiness in the ordered (3,4,11)
branch and the remaining Beal signatures. This intermediate target would
connect the actual global point classes to L074's supported ambient
space, a prerequisite for using its class quotient in a filtered rank
bound. It need not decide either class group or a rank.

Essential inputs: L033's entire K and curve E0; L069's entire D/K,
fixed generator theta and cubic model; L074's definitions of S_F, W_S
and V_S. L073 and ATTEMPTS/033 are a warning against removing eleven,
not a presumed globally realized odd class. ATTEMPTS/032 still excludes
the unfiltered rank shortcut. No cross-notebook input is proposed.

The preceding audit saved this assessment as REVIEW_REQUIRED without
approving or proving containment. This separate literature turn completes
the source comparison and approves only the later matching import. No
containment application, new lemma or mathematical script is supplied here.

The later mathematical continuation test is a proof covering every
outside-support maximal prime and every global point class, with the
same cubic generator. Continue if the exact containment is justified;
otherwise identify a failing hypothesis or class and revise the support
only after separate assessment. This does not reopen the failed demand
for evenness at eleven.

Unresolved assumptions: full Kummer containment itself, complete S-unit
and actual S-class data, global realization of odd local classes,
simultaneous local filtering, rank, subgroup indices/cosets and primitive
integer lifting. No complete candidate exists. Matching and supporting
Mathlib coverage are not checked; no absence or novelty is inferred.

## Primary theorem and complete relevant proof scope

Denis Simon, *Computing the rank of elliptic curves over number fields*,
LMS J. Comput. Math. **5** (2002), 7–17,
[DOI](https://doi.org/10.1112/S1461157000000668),
[publisher PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8FAFF26D93D01A154C51CF897E4BE6CD/S1461157000000668a.pdf/computing_the_rank_of_elliptic_curves_over_number_fields.pdf).
Read printed pp.8–9 (PDF pages 2–3), including the full Proposition 1.4
proof, rather than relying on search excerpts. The paper was received
29 March 2000, revised 27 February 2002 and published 17 April 2002;
search-engine crawl dates are not mathematical source versions.

The setting is a number field k and y²=P(x), with P monic, integral
and irreducible cubic; L=k(theta). Proposition 1.1 sends O to 1 and
finite points to [x−theta], with kernel 2E(k). Proposition 1.2 gives
square norm. Proposition 1.4 puts the image in L(T,2) with square norm,
where T includes infinite places and primes P of L satisfying BOTH
P divides P'(theta) and p² divides disc(P), for p below P in k.
Here L(T,2) means even valuations outside T, without sign restrictions.

The support proof covers negative valuations first, nonnegative odd
valuations away from the derivative second, and the remaining
discriminant-valuation-one case last. All three cases were inspected.
The negative case uses integrality and the monic cubic equation; the
last case uses the relative prime factorization and the square norm.
The later application may cite these cases directly, without reproducing
the stronger last-case argument. This is coverage for all points, not
an integral-coordinate theorem. No class-number, normality or GRH
hypothesis is stated.

## Fixed-model comparison and boundaries of the import

The existing L069 proof gives the origin-preserving K-isomorphism
X=4x, Y=8y+4 from L033's E0 to Y²=g(X), with
g=X³−4X²−160X−1264, the same theta as L074, and the saved identity
disc(g)=−256·11^5. It also proves g irreducible over the entire K and
E0(K)[2]={O}. These are prior canonical inputs, not computations or
derivations in this review. They supply the exact model interface to
check in the later application. The support comparison should use this
polynomial discriminant in O_K, rather than an assumed maximal-order
discriminant or the discriminant of K. All primes above the retained
rational primes remain allowed, regardless of their ramification.

The full global map has no finite zero evaluation under this existing
irreducibility input; O is explicitly included by Proposition 1.1.
Local exceptional two-torsion evaluations in split completions must
not be silently used as global finite-point exceptions. For the present
global target the cited irreducible theorem suffices; there is no need
to extend its statement to split local algebras. Coordinate denominators
are within Proposition 1.4's read proof. The later write-up should
import the theorem and give only the model/support/space identification.
A general reproof would duplicate existing coverage without closing a
different gap.

The norm-square target has no extra archimedean positivity requirement.
Simon includes infinite places in T, whereas L074 places no valuation
or sign condition there; the finite support conventions must simply be
matched. A larger permitted finite support weakens the valuation
condition. This source comparison authorizes that applicability check,
not an assertion that the smallest possible support has been computed.

## Reuse, duplicate and failure checks

The exact support theorem and all its proof cases had already been read
for `drafts/literature/2026-10-15-even-valuation-unit-exhaustion.md` and
`drafts/literature/2026-10-15-eleven-adic-even-valuation-containment.md`.
Those records are reused; their targets did not approve this particular
global supported application. L069 uses Propositions 1.1–1.2 and counts
ordinary units; L074 handles an ambient quotient. Neither is a duplicate
proof of the present containment application. No additional Milne,
Stacks or BPT search was needed for this target.

The bounded searches above located the same Simon theorem; unrelated
quadratic-parametrization results bearing the same proposition number
were not mathematical inputs. A search also surfaced Michael Stoll's
separate EllipticCurves Lean repository with a claimed supported descent
result. Its declarations and proof were not inspected, and it is not
asserted to be Mathlib coverage or an essential source. Full matching
and supporting Mathlib coverage remains not checked. No novelty claim
is inferred from this search.

ATTEMPTS/032 still rules out the unfiltered dimension shortcut; placing
point classes in a supported ambient space alone will not repair it.
ATTEMPTS/033 still rules out universal local evenness at eleven. The
current import retains eleven and does not assert global realization of
that odd local class. No historical stop is broadened into a ban on
filtered descent, and no cross-notebook theorem was read.

The continuation passes only if the later cited application covers every
global class at every outside-support maximal prime with the same model.
A mismatch requires correction or renewed assessment, rather than
silently enlarging support. Even success leaves supported unit/class
arithmetic, simultaneous filtering, rank, indices/cosets, all other
classes and primitive integer lifting unresolved. This is local notebook
progress in source coverage, not progress beyond Simon's theorem and
not a complete candidate for Beal.
