# Simultaneous simple-G contact — completed bounded source comparison

TARGET: Test whether a C2 local radial graph with real nonnegative full L847 density and J(p)!=0 can meet two distinct simple zeros of G at once.
CHECKED: 2026-11-06
DECISION: EXPLORE
SEARCH_EVIDENCE: Completed bounded exact/stronger-result searches for simultaneous contacts, vanishing holomorphic forms, normal-crossing normal forms and positive totally real pullbacks; searched the named local contact assessments and failures. No inspected matching full-form radial-graph theorem was found. Queries and read scope below; no novelty inference.
SOURCE_EVIDENCE: Inspected Szawlowski J.Singularities4(2012)104-113 DOI10.5427/jsing.2012.4f Theorem1.1 p104, definitions p105, Lemma3.1 both directions pp108-109 and Section3 existence conclusion p110 https://journalofsing.org/volume4/szawlowski.pdf ; reuse inspected Lebl CA v1.10 Theorem2.4.7 pp49-50 and Corollary3.2.12 pp67-68 https://www.jirka.org/ca/ca.pdf , Lebl SCV v4.4 Theorem1.2.1/proof pp20-21 https://www.jirka.org/scv/scv.pdf , and Chaperon 9January2007 Section1 Corollary1 p2 https://webusers.imj-prg.fr/~marc.chaperon/Chaperon_Cauchy_Kowalevski.pdf .
COMPARISON: The inspected function-germ normal form does not supply a positive radial surface or preserve its angular data automatically. The analytic tools remain applicable as tools, but L855/L859's single-G inverse assumes G(eta)!=0 and cannot be imported at this pair. Reused special-Lagrangian coverage assumes a nonvanishing form on a divisor complement. No cited result decides full-density feasibility with J(p)!=0 in all coordinate ranks.
GAP: Test exact full-form feasibility or a scoped C2 obstruction at two distinct nonzero simple G zeros, retaining both factors, J(p)!=0, all coordinate ranks and the original angular orientation. Any new joint coordinates, tangent-product restrictions and actual germ remain to be justified in research.
REASON: The changed target now has adequate bounded comparison and supporting source coverage for one local model/first-order obstruction attempt. No essential source blocker remains for that attempt; no matching theorem can simply be imported. This decision is coverage, not a derived contact result.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED nomination changes the divisor configuration from one vanishing G factor to two; the accepted single-G assessments explicitly exclude it. This turn completes that missing comparison and does no mathematical attempt.
SCOPE: Exactly TARGET for actual L847 G,R,C,F, C2 real u on an open angular neighborhood, original orientation, zeta eta!=0, zeta!=eta, G(zeta)=G(eta)=0 and G'(zeta)G'(eta)!=0. Both coordinate ranks one and two are allowed. Covers one exact local model or first-order obstruction test, not a prescribed collar, forced contact, global torus, all-degree transfer or an actual selected zero pair.

## Original nomination: bounded target and relevance

Retain L847's actual G,R,C,F and the full identity
q_u=F(Phi_u)det(I-iDu). Explicitly hypothesize zeta eta!=0,
zeta!=eta, G(zeta)=G(eta)=0 and G'(zeta)G'(eta)!=0. Use real
angular lifts p=(arg zeta,arg eta) and C2 real u on an open
neighborhood of p with Phi_u(p)=(zeta,eta). The test asks for real
nonnegative q throughout that neighborhood and J(p)!=0. It must
allow either coordinate rank one or two; no transversality or
isolated pulled-back zero may be silently imposed.

The bounded discriminator, after source coverage is approved, is one
exact full-form local construction with its stated pair conditions,
or a rigorously scoped C2 obstruction. A formal jet, omission of a G
factor, J(p)=0 example, or an obstruction only for an unannounced
transverse subclass is insufficient. Any pair-dependent criterion
must remain conditional. No calculation toward this test was carried
out while preparing this nomination.

The new issue is interaction between two odd vanishing factors, rather
than the single even factor audited in L859. The known inverse loses
its nonzero derivative here. Source comparison should therefore check
normal-crossing divisors of holomorphic volume forms and positive
totally real surfaces, including exact hypotheses and proof cases,
before deciding whether a coordinate or obstruction method applies.
These are search directions, not imported theorems or a proposed proof.

Plausible downstream use is to delimit simultaneous contacts that a
later collar-extension argument would have to handle. L858 supplies
motivation for retaining J!=0 in its global conditional setting; its
conclusion is not assumed to force the proposed local pair. L847 is
the essential form input. L855 and audited L859 are comparisons only;
separately unaudited C858b is not a premise. Actual selected zeros,
contact forcing, prescribed gluing and all-degree Xi positivity remain
unresolved. The main gap remains L030-L032/C032a.

Keep the free-germ/boundary and full-phase two-period stops. This is
neither automatic patching nor a renamed period test. A simultaneous
local result would still supply no global extension. No justified
central creative mechanism has yet been obtained from the local
models; do not label this source nomination or routine specialization
as creative merely to satisfy routing priority. No cross-notebook
input or Mathlib coverage claim is made.

## Completed comparison — 6 November 2026

This is LITERATURE / NOVELTY_UNCHECKED, outcome EXPLORATION. The
comparison is new local documentation, not a new mathematical input
or a discovery beyond the sources. No contact construction, exclusion,
normalization of the actual form, or tangent classification was derived.
The exact TARGET is retained for a separate approved research turn.

### Local duplicates and failures

Read L847's full form, radial pullback and scope; L855's hypotheses,
conclusion and joint-coordinate proof (3)-(5); and L859's hypotheses,
conclusion and reused-coordinate portion (1)-(4). Searched simultaneous,
two-odd-factor and normal-crossing terminology in the 6 November contact
assessments, related failures and contact histories. Reused the completed
odd-contact, even-single-contact and primitive-monomial source comparisons.
No matching simultaneous-contact result appeared in these specific paths.

L847 excludes globally separated product contours, not every local
coupled surface. L855 permits central J=0; L859 assumes one even zero
and the other G factor nonzero. The odd-contact assessment assumes
exactly one vanishing factor. None settles this target. C858b is not
an input. Read the free-germ/boundary, full-phase two-period and
primitive-source-parking ATTEMPTS records. Their respective stops
concern prescribed matching, compatible full phase periods, and an
old process repair; preserve them without turning them into a ban
on this changed local test. No exhausted mechanism is reopened.

### Primary theorem and essential cases

Adrian Szawlowski, *A volume-preserving normal form for a reduced
normal crossing function germ*, J. Singularities 4 (2012), 104-113,
[Theorem 1.1, p104](https://journalofsing.org/volume4/szawlowski.pdf#page=1):
if a holomorphic germ f at zero is right equivalent to the product
of the n coordinates, there are holomorphic automorphisms Phi and
Psi with det D Phi identically one and f composed with Phi equal
to Psi of that product, with Psi invertible.
Read the definition p105 and Lemma 3.1's two directions pp108-109:
quasihomogeneous rescaling exchanges function and volume normalization;
the reverse direction solves a coefficient equation with nonzero
constant term. Read the existence conclusion p110, which invokes
Lemma 3.2 and Françoise's path method. That referenced proof and
Section 4's uniqueness proof were not inspected or imported. The
theorem concerns a function with a nonvanishing ambient volume form,
not an oriented radial surface through its zero set. Applying it to
the actual coefficient would require checking right equivalence
and transporting angular and Jacobian conditions. This review does
neither; a direct first-order test needs no path-method input.

Reuse the primary analytic statements already inspected in the
single-contact assessments: Lebl CA v1.10 (5 November 2026),
Theorem 2.4.7 and its first-nonzero-Taylor-coefficient factorization
proof pp49-50; Corollary 3.2.12 and segment-primitive proof pp67-68;
Lebl SCV v4.4 (31 May 2026), Theorem 1.2.1 and proof pp20-21;
Chaperon (9 January 2007), Section 1 Corollary 1 and real/complex
justification p2. G is entire and G(0)>0 by L847, so the zero
factorization input applies separately at each hypothesized zero.
The primitive requires a star-like plane domain; the joint power
series requires a polydisc within the holomorphic domain; every
inverse requires its own invertible derivative. These are standard
tools, not a theorem removing either divisor or guaranteeing the
angular orientation. No reproof of them is warranted.

Reuse the odd-contact assessment's first-order differentiation
coverage and its C2 warning: J is only C1, and a high-order Taylor
extremum theorem cannot be used without its extra derivatives.
Reuse the even-contact assessment's inspected Auroux Definition 2.1
and Proposition 2.2 comparison (author manuscript Section 2.2 pp4-5):
the nonvanishing-form, divisor-complement and Lagrangian hypotheses
do not supply the present contact. Forstneric's complex-point index
models likewise do not specify this full density. No fresh review
of those unchanged results is needed.

### Search scope and one permitted discriminator

Queries actually run included:

- `holomorphic volume form zeros normal crossing special totally real submanifold local positive`
- `singular holomorphic volume form normal crossing real submanifolds constant phase`
- `"holomorphic" "volume forms" "normal crossing" normal form zeros`
- `"vanishing" "holomorphic" "volume form" "totally real"`
- `"normal crossing" "special Lagrangian" local divisor`
- `"holomorphic volume form" "zeros" "normal form"`
- `"totally real" "vanishing" "form" "positive" divisor`
- `"normal crossing" "volume-preserving" Szawlowski theorem`
- `"nonnegative" "pullback" "holomorphic" "zeros"`
- `"normal crossing" "positive" "totally real"`
- `"vanishing holomorphic" "Lagrangian" forms`
- `"radial graph" "holomorphic" "nonnegative"`
- `"normal crossing" "nonnegative" "pullback"`
- `"holomorphic" "volume form" "zero divisor" "local" "surface"`

Inspected the journal's own landing page, theorem and selected proof
passages before the larger Section 3 range. Search hits on torus
fibrations, log-symplectic forms, divisor smoothings and algebraic
positivity were not read as theorems or imported; they supply no
evidence for this exact sign condition. The bounded search does not
establish originality or exhaust the literature.

One later attempt may use the full L847 identity and first-order
restrictions in arbitrary real angular directions to test the two
simple factors together, then either give a rigorously scoped
obstruction or test an exact analytic model. Treat rank-one and
rank-two coordinate maps explicitly; do not assume separate zero
curves, transversality, an isolated pulled-back zero, or an inverse
whose determinant vanishes here. A quadratic jet alone establishes
neither feasibility nor a full obstruction unless the logical
implication for all allowed ranks is proved. An exact construction
must keep both factors on one common open neighborhood and check
the actual angular orientation and J(p)!=0 there as required.

Continue if an exact germ meets these checks, or if an obstruction
has an explicit valid scope and changes the local feasibility
decision. Abandon a proposed normalization or leading-term test
when it needs the other G factor nonzero, extra smoothness, an
unannounced rank restriction, or loses the full sign. Preserve its
failure rather than generalizing it. Pair-dependent conclusions
must remain conditional; contact forcing and global gluing stay open.

This EXPLORE coverage is ready for separate next-turn approval,
not permission to derive mathematics during this review. The
suggested research classification is POTENTIALLY_NEW solely in the
bounded-search sense. No justified central creative mechanism is
ready: this local test lacks contact forcing, prescribed gluing and
all-degree transfer. It is not labeled creative to satisfy a schedule.
Full matching Mathlib coverage is not checked. No cross-notebook
input, lemma, DAG, PROOF or mathematical script changed in this turn.
