# Marked elliptic quotient — completed three-descent review

TARGET: Assess whether explicit three-descent on L112's elliptic model can certify rank E(Q) <= 1 without the stopped quartic traversal or unavailable class-group backend.
CHECKED: 2026-10-25
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Checked L112/L127, L128/L129 model/conclusion ranges, ATTEMPTS/050–054, the explicit-two-descent review and the older five-adic Schaefer–Stoll assessment; searched general/class-group-free three-descent, rational three-isogenies and both exact cubic coefficient pairs. No inspected matching rank certificate or class-group-free complete ternary-cubic enumeration was found; no absence or novelty claim.
SOURCE_EVIDENCE: Inspected Schaefer–Stoll's June 13, 2001 long version, Proposition 4.6 and Lemma 4.5 proof, Section 5 pp.8–10, Section 9 pp.21–23 and Section 11.1 pp.29–30; Cremona et al. (2015) published offprint, exact sequence p.895, Theorems 2.2/2.4 and proofs pp.900–901, and Section 4 p.905 including its generic-action assumption; Cremona corrected second edition III.3.8 p.99, rational-kernel discussion and three-division formula.
COMPARISON: General prime descent still needs complete class/unit input and local images; producing plane cubics does not eliminate these prerequisites. Rational three-isogeny descent uses smaller kernel algebras but its existence is untested on L112. A complete rational-root eligibility test is independently executable; no upper rank or complete three-descent instance plan is supplied.
GAP: Park the general full-Selmer implementation pending independently certified global arithmetic. Test rational-three-isogeny eligibility separately; even a positive test leaves its quadratic class/unit data, both isogeny directions, local completeness and sharp rank threshold unresolved.
REASON: Inspected prerequisites rule out treating general three-descent as an immediate backend bypass; known rational-kernel theory identifies a distinct bounded structural test, separately assessed for next-turn approval, without deriving its answer here.
LITERATURE_REASON: The saved target was REVIEW_REQUIRED; binary-quartic and local five-adic coverage did not cover full three-descent, its global prerequisites or this model's isogeny eligibility.
SCOPE: Source comparison for unchanged TARGET, with general dependent execution parked. Only the separately assessed rational-three-isogeny eligibility test is a proposed mathematical continuation; no Selmer, class-group, ternary-cubic enumeration or upper-rank calculation is approved here.

## Exact scope, relevance and route decision

The intended elliptic model is precisely L112's

    E': y²=x³−2874960x+1739350800,

with its proven lower rank one. An upper bound at most one could
determine the elliptic summand in L127. L129 supplies only the latest
fixed-sieve workload obstruction, not a general impossibility theorem.
ATTEMPTS/050–054 and unfinished L108 remain preserved.

This completed turn was literature-only. No three-descent calculation,
lemma, mathematical script or new instance theorem was produced.
No rational three-isogeny, torsion dimension, Galois image, class value,
Selmer size, finite precision or rank upper bound is assumed.

The original continuation test is not met for general full descent:
the source algorithms retain the kind of certified global arithmetic
missing in ATTEMPTS/052. Their fields and 3-primary groups need not be
the same as that attempt's octic and 2-primary group. This is a shared
execution prerequisite, not an identification of those data or a proof
that manual certificates are impossible. Park dependent execution
without reprobes or larger quartic caps. An upper bound above one
would not refute exact rank one.

The independently testable structural continuation is specified in
`drafts/literature/2026-10-25-marked-elliptic-three-isogeny-eligibility.md`.
It checks applicability of the smaller-field branch before any global
arithmetic. Its answer is reserved for a later approved research turn.

Essential inputs: L112, L127, L128, L129; the explicit-two-descent
assessment and ATTEMPTS/050–054. Unresolved assumptions include all
three-descent source coverage and instance feasibility, elliptic upper
rank, genus-two rank, marked lifts, degree-nine recovery, both L095
systems, minus-eleven and other signatures. Mathlib coverage is not
checked. This review adds source coverage and changes routing, with
no new mathematical conclusion or change to the Beal argument.

## Primary theorem comparison

**General Selmer computation.** J.E. Cremona, T.A. Fisher, C. O'Neil,
D. Simon and M. Stoll, *Explicit n-descent on elliptic curves III.
Algorithms*, Math. Comp. **84** (2015), 895–922,
[DOI](https://doi.org/10.1090/S0025-5718-2014-02858-5),
[published author offprint](https://johncremona.github.io/papers/mcom2858.pdf).
Theorem 2.4, p.901, assumes a number field, an elliptic curve, a prime,
bad-prime information and class/unit data in fields of nonzero p-torsion
points. Its proof constructs the global unramified group and
cohomological image, then intersects complete local images at p and
Tamagawa primes. Theorem 2.2 and proof, p.900, use pair-of-torsion fields
instead. Neither theorem supplies those groups. The exact sequence on
p.895 bounds rank using Selmer dimension with rational p-torsion
allowed; no Sha-vanishing assumption is needed for an upper bound.

L112 supplies the number-field/elliptic hypotheses for p=3, but none
of the missing instance arithmetic. Section 4, p.905, assumes mod-three
Galois surjectivity for its displayed tower; its footnote mentions
other implemented cases. That generic assumption is unverified here.
Converting Selmer elements to ternary cubics does not certify a search.

**Arithmetic and special branch.** E.F. Schaefer and M. Stoll,
*How to do a p-descent on an elliptic curve*, Trans. AMS **356** (2004),
1209–1231, [DOI](https://doi.org/10.1090/S0002-9947-03-03366-X).
Locators here refer to the inspected
[long manuscript dated June 13, 2001](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
not journal pagination. Proposition 4.6, p.7, and its Lemma 4.5 proof
retain p-adic and p-divisible-Tamagawa places. Section 5, pp.8–10,
requires global/local injectivity and the cohomological image; its
S-unit/S-class exact sequence retains both contributions. Local spanning
needs a certified quotient size, including the formal-group factor at p.
Section 9, pp.21–23, assumes an actual rational degree-p isogeny and
uses kernel algebras of degree p−1; equation (9.1) and Lemma 9.1 keep
the dual direction and correction terms. This supports a cheaper
eligibility test, not a rank certificate from one isogeny alone.
Section 11.1, pp.29–30, explicitly assumes GRH for its generic example's
class computation. That example is not an unconditional certificate.

**Exact eligibility criterion.** J.E. Cremona, *Algorithms for Modular
Elliptic Curves*, second edition, CUP 1997,
[corrected online Chapter III](https://johncremona.github.io/book/fulltext/chapter3.pdf),
Section 3.8, printed p.99. For a nonsingular short model y²=x³+ax+b
over Q, rational subgroups of order three correspond to rational roots
of 3x⁴+6ax²+12bx−a². The text distinguishes a rational subgroup from
pointwise rational kernel points and gives isogenous coefficients from
a root. L112 is such a model. These formulas are imported; no
substitution or root determination was done this turn.

## Search record, overlap and limits

Queries included `explicit 3 descent elliptic curves number field class
groups units Schaefer Stoll 3 Selmer algorithm`, `Cremona Fisher O Neil
Simon Stoll explicit n descent III algorithms 3 descent class group`,
`elliptic rational 3 isogeny division polynomial rational root criterion
theorem pdf`, `"3-descent" "without" "class" elliptic`, and
`"three-descent" "ternary" "enumeration"`. Exact-instance queries used
`"2874960" "1739350800" elliptic`, `"179685" "27177356" elliptic`,
and `"3-descent" "2874960"`. No inspected result supplied the desired
exact-instance rank bound; failed searches do not establish novelty.

The older five-adic norm-slice assessment covers Section 5 on L033's
different curve/local predicate, not L112's global arithmetic.
L128/L129 stop their fixed quartic traversals; ATTEMPTS/050 is a
bounded genus-two lower-rank detector and ATTEMPTS/051 excludes rank
zero. None decides this structural eligibility test. All stopped
evidence and unfinished L108 are preserved.

Search results also exposed historical Magma manuals, modern
3-isogeny/class-group bounds and a capitulation-discriminant lead;
they were not used as inspected theorem inputs. Milne's newer book
and Robert's algorithm notes timed out; they are unnecessary because
Cremona supplies the exact criterion. The 2011 n-descent-III preprint
was identified, but the comparison uses the published 2015 version.
No comprehensive-coverage or method-impossibility claim is made.
