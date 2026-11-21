# Local odd-multiplicity divisor contacts — completed source comparison

TARGET: Assess whether full-density nonnegativity and L858 exclude off-diagonal contacts where exactly one G(z_j) vanishes to odd multiplicity, retaining nontransverse contacts and the C2 radial class.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded exact/stronger-result searches for nonnegative holomorphic-form pullbacks, odd multiplicity, totally real divisor contacts, and odd-order sign tests found no inspected matching actual-G exclusion theorem; targeted L847/L849/L855/L858 and transverse-divisor/failure records distinguish the common-J-zero germ from this target. Queries and limits below; no novelty inference.
SOURCE_EVIDENCE: Read Lebl CA v1.10 Theorem2.4.7 and factorization proof/remark pp49-50 https://www.jirka.org/ca/ca.pdf ; Lebl Basic Analysis I v6.3 Definition4.1.1 p155, Exercise4.1.14 p161 and Theorem4.3.2 with proof pp172-173 https://www.jirka.org/ra/realanal.pdf ; Zakon Mathematical Analysis I SectionV.6 Theorem2 with both parity proof cases in the primary-text LibreTexts edition https://math.libretexts.org/Bookshelves/Analysis/Mathematical_Analysis_(Zakon)/05:_Differentiation_and_Antidifferentiation/5.06:_Differentials._Taylors_Theorem_and_Taylors_Series .
COMPARISON: Known holomorphic zero factorization and first-order differentiation supply the tools for a bounded specialization. The inspected higher-derivative sign test requires Cn regularity and cannot be directly imported for arbitrary odd multiplicity in this C2 class. L855 allows J=0 at its positive germ; L858 excludes f=J=0 only under its full global hypotheses. No source establishes the requested exclusion as stated.
GAP: Verify the full-density factor and a two-sided leading-term sign test along a suitable angular coordinate using factorization and only first-order surface information; justify a nonzero leading coefficient without rank-two transversality or isolated pulled-back zeros. This actual-form application is reserved for research, not proved here.
REASON: Essential coverage is sufficient for this precise finite-order specialization without stronger smoothness or a new existence theorem. Sources are imported, not reproved; the remaining coordinate, coefficient and sign checks are necessary because neither a holomorphic zero theorem nor a Cn extremum test already handles the C2 pullback.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changed from global phase periods to local odd-contact sign order; its exact nontransverse C2 source comparison was missing. This turn supplies that comparison, not another review of the retired period mechanism.
SCOPE: Exactly TARGET under L847's actual full F and radial angular coordinates, L849's strictly smaller exact collar with inherited L848 qualifications, and accepted L858 for a real C2 periodic exchange-symmetric radial torus with globally real nonnegative q=fJ. At the tested point z_1!=z_2, exactly one G(z_j) has finite odd multiplicity and the other is nonzero. No transversality, simple zeros, isolated pulled-back zero set, RH, or existence of a global torus is assumed. The approved application uses only holomorphic factorization, first-order restrictions, limit algebra and two-sided signs.

## Purpose and scope boundary

The main gap remains L030–L032/C032a actual-Xi all-degree mixed
positivity. The intermediate target is a necessary restriction on
single-coordinate divisor contacts in the global collar-assembly
problem. Its plausible use is to reduce the kinds of contacts a
nonnegative extension would have to accommodate. Even success leaves
even multiplicities, simultaneous G zeros, forced contact, global
assembly, all other signs and all-degree transfer unresolved.

This assessment approves source coverage for a subsequent bounded
mathematical attempt. It proves no parity rule and makes no torus
nonexistence claim. Its invocation-start decision was REVIEW_REQUIRED;
the present SPECIALIZE assessment is newly completed and remains
subject to the supervisor's separate next-turn approval.

## Duplicate and failure comparison

Read L847 hypotheses/conclusion and full pullback (1)–(4), L849's
prescribed data and exact collar conclusion, L855's hypotheses,
conclusion and source boundary, and L858's hypotheses/conclusion and
factorization citation. These are scoped input reads, not new audits
of their proofs or of the inherited software claims.

Searched odd/nontransverse/multiplicity/sign-order terminology in
L847–L858 and the named 6 November contact assessments and failures.
Read the completed transverse-divisor comparison through its primary
sources and the retired full-phase two-period ATTEMPTS record. No
recorded matching odd-contact exclusion was found in those paths.
L855's real-analytic positive germ retains a central J zero. It is a
contrast, not a counterexample under L858's globally qualified
common-zero exclusion. Its free local data also do not match a global
torus with the prescribed collar. C858a is motivation only, not an
input. The retired two-period obstruction remains retired.

## Primary statements and essential proof cases inspected

Jiří Lebl, *Guide to Cultivating Complex Analysis*, version 1.10,
5 November 2026, [Theorem 2.4.7, proof and factorization remark,
pp49–50](https://www.jirka.org/ca/ca.pdf#page=49), assumes an analytic
function on a connected open domain. Unless it is identically zero,
its zeros are isolated. The proof factors the first nonzero power
at a zero, leaving a convergent analytic unit nonzero nearby; it then
uses connectedness for the identity conclusion. Read both cases.
For this target the actual G is entire and G(0)>0 by L847; importing
its finite-zero factorization is justified. The theorem imposes no
surface regularity and makes no sign assertion about a pullback.
Its identity theorem and factorization are known inputs, not new
results or claims about the existence of any particular contact.

Lebl, *Basic Analysis I*, version 6.3, 15 May 2026,
[Definition 4.1.1 p155; Exercise 4.1.14 p161; Theorem 4.3.2 and
proof pp172–173](https://www.jirka.org/ra/realanal.pdf#page=155).
The definition gives the first-order difference quotient; the exercise
states affine approximation with an error divided by distance tending
to zero. Apply the definition componentwise for a complex-valued
curve, not an unproved solution of that exercise. Taylor's theorem
requires n continuous derivatives and an (n+1)st derivative on the
interval interior; its proof iterates the mean value theorem. Read
the hypotheses and proof through the final remainder identity.
This is a regularity comparison, not permission to differentiate the
full density to arbitrary order. A C2 surface gives only a C1 J.
The proposed later application must use first-order curve information
and a continuous remaining coefficient, rather than a Cn density
assumption. No reproof of Taylor's theorem is needed.

Elias Zakon, *Mathematical Analysis I*,
[Section V.6, Definition 1 and Theorem 2 with proof, LibreTexts
primary-text edition](https://math.libretexts.org/Bookshelves/Analysis/Mathematical_Analysis_(Zakon)/05:_Differentiation_and_Antidifferentiation/5.06:_Differentials._Taylors_Theorem_and_Taylors_Series).
Theorem 2 assumes Cn near the point and a first nonzero derivative
of order n. It gives a local extremum for even n of the appropriate
sign and no local extremum for odd n. Read the Lagrange-remainder
argument, coefficient-continuity step and both parity cases. The
odd case compares the two sides of the point. This is the strongest
inspected direct sign-order statement; its Cn hypothesis does not
follow for the full C2-surface density at arbitrary n. The publisher's
trillia.com landing page timed out; the theorem and its complete
relevant proof were available in the attributed textbook edition,
so this is not an essential source blocker. Do not import the theorem
with its differentiability assumptions silently dropped.

## Searches, proposed application, and decision test

External queries actually run:

- `nonnegative pullback holomorphic volume form odd multiplicity zero totally real submanifold`
- `nonnegative smooth function vanishing odd order Taylor theorem sign change`
- `totally real surface holomorphic divisor tangency positive volume form zero odd multiplicity`
- `"nonnegative" "odd" "order" "Taylor" function theorem`
- `"holomorphic" "divisor" "nonnegative" "totally real"`
- `"holomorphic" "odd multiplicity" "nonnegative" pullback`
- `"radial graph" "divisor" "nonnegative" complex`

Broad volume-form, positivity and unrelated entire-function hits did
not supply an applicable theorem and were not used as evidence.
The searches located the inspected textbook sign test. Reuse the
completed transverse-divisor assessment's Forstneric comparison:
complex-point indices and monomial models do not preserve this full
specified nonnegative pullback. No further index source is essential
for the present one-coordinate sign test; other leads remain unread
and unimported. A bounded search is not evidence of originality.

The later attempt may restrict to varying the angular variable of the
vanishing factor while fixing the other angle. It must check the
velocity, the surviving coefficient in the full L847 form, and the
two-sided limiting sign under L858's J-nonvanishing consequence.
This specifies a test, not a derivation or an established asymptotic.
It must work for either coordinate and arbitrary finite odd n while
allowing rank-one/nontransverse contacts and nonisolated zero sets.
Do not replace G by a polynomial or divide by it at its zero.

Continue if this exact restriction yields a nonzero leading term and
a valid two-sided sign contradiction at C2 regularity. Abandon the
proposed coordinate test if it requires rank-two transversality,
extra density derivatives or a nonvanishing assumption not supplied
by the inputs; record the specific failure instead. A counterexample
would have to respect the full hypotheses being tested; L855 alone
does not. There is no approved global-exclusion or gluing calculation.

No lemmas, DAG, PROOF or mathematical scripts were changed in this
literature turn. No new mathematical claim or canonical proof is
asserted. Full matching Mathlib coverage was not checked; the named
standard source tools are supporting inputs, not a matching theorem.
No cross-notebook input is used. This is a routine specialization
nomination, not a genuinely new central creative mechanism. Such a
mechanism is not justified by this bounded local source review.
