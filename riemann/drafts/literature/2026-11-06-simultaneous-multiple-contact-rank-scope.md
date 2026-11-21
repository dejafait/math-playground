# Simultaneous multiple contacts — completed necessary-condition source comparison

TARGET: Determine the necessary multiplicity and real-rank possibilities at a simultaneous contact of two distinct nonzero finite-order G zeros with q>=0 and J(p)!=0, and whether they preserve L861's regular-value sign balance.
CHECKED: 2026-11-06
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Bounded searches for nonnegative binary forms, products of complex linear forms and multiple vanishing-volume-form contacts; inspected two primary binary-factorization passages and an alternate univariate source, and compared the named local results/stops. Queries, actual reads and unread leads below; no novelty inference.
SOURCE_EVIDENCE: Read Blekherman-Sinn-Smith-Velasco, Notices AMS68(2021)734-747, Section3 binary-form paragraph p742 https://ggsmith.ca/Papers/notices.pdf#page=9 ; Michalek, Algebraic Varieties, 17April2018, Example7 p4 https://www.math.uni-konstanz.de/~michalek/april17.pdf#page=4 ; Semmes, Functional Analysis2, Section107 p111 https://math.rice.edu/~semmes/fun2.pdf#page=111 . Reuse inspected Lebl factorization/first-order sources and Teschl2004 Theorem2.4 with exact qualifications below.
COMPARISON: Known binary-form factorization covers conjugation and real-root parity for a real nonnegative homogeneous polynomial, not the full radial contact. L860 covers two simple factors, L859 one even factor with the other nonzero, and L861 regular preimages under its simple-pair restriction. No inspected theorem automatically transfers these conclusions to simultaneous arbitrary multiplicities.
GAP: Justify the tangent-product reduction using finite holomorphic factorization and first-order surface information, apply known binary-factor constraints to every coordinate-rank combination, and distinguish regular-value orientation from singular preimages. The necessary classification and its L861 specialization remain unperformed.
REASON: Essential changed-scope comparison is now sufficient for one bounded specialization; import the standard factorization/degree tools without reproof. Remaining work is the actual-form applicability and rank calculation, not an exact-germ existence theorem. This newly ready continuation requires separate next-turn source approval before mathematics.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target replaces simultaneous simple factors by arbitrary fixed finite positive multiplicities; existing ready assessments did not compare the required homogeneous-product/rank cases. This turn supplies that essential missing coverage only.
SCOPE: Actual L847 G,R,C,F and original angular orientation; one conditional pair zeta!=eta with zeta eta!=0, multiplicities m,n>=1 fixed finite, a real C2 local angular graph through that pair, real q>=0 on an open neighborhood and J(p)!=0. Seek necessary tangent/rank conditions only; no exact germ existence, finite contact set, prescribed data, global symmetry, periodic extension, actual multiple zeros or RH is assumed.

## Original nomination and bounded continuation

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. L861 supplies a restricted global incidence constraint;
its regular-value use depends on L860's simple-pair rank conclusion.
A necessary-condition classification could determine precisely which
parts of that constraint survive without a simplicity assumption, or
show why such an extension fails. It would not settle the other global
or sign gaps. Existence of an actual multiple-zero pair is conditional,
and is not to be asserted or sought as a prerequisite of this test.

The next invocation must first review the exact target, standard
terminology, stronger results and counterexamples. Reuse the inspected
factorization and degree evidence where its hypotheses really apply.
First-order expansions may be candidate tools; no order-m+n Taylor
theorem for a merely C2 surface is authorized. Distinguish a necessary
algebraic tangent from a realizable full-neighborhood germ, and a
regular coordinate value from a singular one. An exact model or a
global degree theorem at singular values would be a different target.

Essential local inputs for the future comparison are L847's full
form, L860's all-rank simple-pair converse, and L861's use of regular
coordinate preimages. L859 is a scope contrast; it cannot be silently
applied with its nonvanishing second factor removed. The relevant
prior assessments are `2026-11-06-simultaneous-simple-g-contact-scope.md`,
`2026-11-06-even-single-contact-feasibility-scope.md` and
`2026-11-06-individual-divisor-contact-incidence.md`.

Continue only if the reviewed target can decide which multiplicity
and rank cases retain the regular-value orientation mechanism, or
identify a specific exceptional case preventing it. Stop if it merely
repeats the simple-pair proof without deciding any additional case,
requires an unproved high-regularity assumption, or substitutes free
formal tangents for exact local feasibility. Useful necessary
conditions may leave existence and all global issues unresolved.

This differs from the stopped count-only contradiction, the automatic
two unweighted moments and the parked singular real-flux lift. It
addresses a stated hypothesis gap, not a renamed completion mechanism.
Their original stop evidence is preserved. No new central creative
mechanism has been justified by the repeated audit; do not describe
this local classification as a creative solution of the main gap.
Full matching Mathlib coverage is not checked. The original nomination
made no source approval; the completed comparison below changes that
source decision only. No cross-notebook input is used.


## Completed comparison — 6 November 2026

LITERATURE / NOVELTY_UNCHECKED / EXPLORATION. This is a fresh source
comparison, not a contact classification, theorem import into the proof,
new obstruction or new lemma. The exact TARGET and conditional SCOPE
are unchanged. No mathematical scripts, lemma, DAG or PROOF changes
are needed. This review does not spend the mathematical exploration
budget or reset an exhausted mechanism.

### Primary statements and essential proof cases

Blekherman, Sinn, Smith and Velasco, *Sums of Squares: A Real Projective
Story*, Notices AMS **68** (May 2021), 734–747, Section 3, printed p742,
[binary-form paragraph](https://ggsmith.ca/Papers/notices.pdf#page=9).
For a nonnegative real binary form of even degree, their argument
separates real-root factors from conjugate nonreal-root factors; real
roots have even multiplicity. It yields a sum of two squares. Read the
whole paragraph, including dehomogenization and the conjugate-product
identity. These are polynomial hypotheses, not conclusions about a
surface. A future application must first establish a nonzero real
homogeneous polynomial and account for projective root directions;
a single affine chart cannot silently omit a direction at infinity.
The stronger sum-of-squares conclusion does not realize a radial germ.
The former Queen's PDF URL redirected to the author's homepage; the
current author PDF supplied the text. Its screenshot timed out, so no
image inspection is claimed.

Mateusz Michalek, *Algebraic Varieties*, lecture notes dated 17 April
2018, [Example 7, printed p4](https://www.math.uni-konstanz.de/~michalek/april17.pdf#page=4).
The FTA-based binary factorization is unique up to scalar factors and
ordering. For real coefficients, conjugation preserves the multiset
of projective linear factors. Read the complete example's real/complex
field cases and conjugate-divisibility argument. Extraction loses some
conjugation bars; the explicit conjugation-invariance prose is the
evidence, not a claimed page-image inspection. Multiplicities
belong to that multiset; scalar normalization must be tracked rather
than reading a chosen complex factor as literally real. Import this
standard algebra, not a new factorization proof. It imposes no angular
or Jacobian condition on a contact.

Stephen Semmes, *An Introduction to Some Aspects of Functional Analysis,
2: Bounded Linear Operators*, undated accessed PDF, [Section 107,
printed p111](https://math.rice.edu/~semmes/fun2.pdf#page=111), equations
(107.1)–(107.4). Read the real-root parity, FTA product and alternative
minimum/induction proof. It is an independent univariate check of the
parity input. Operator consequences and later sections are not inputs.
It does not replace the binary/projective hypothesis check.

Reuse Lebl CA v1.10 Theorem 2.4.7, factorization proof/remark pp49–50,
and Lebl Basic Analysis I v6.3 Definition 4.1.1 p155, as inspected in
`2026-11-06-odd-divisor-contact-scope.md`. G is entire and G(0)>0 by
L847, so finite zero factorization is applicable at each hypothesized
zero separately. First-order curve differentiation and continuity of
the remaining coefficient are the available tools. J is only C1 for
C2 u. Do not invoke an order-m+n Taylor theorem for the full density.
No joint inverse or exact local normalization is needed for the
necessary-condition test, and none is approved by these sources.

Reuse Teschl, *Nonlinear Functional Analysis*, 23 June 2004,
[Theorem 2.4 and Sections 2.2–2.3, pp13–22](https://www.math.chalmers.se/Math/Grundutb/GU/MMA120/A14/lecture%20notes/Teschl%20G.%20Nonlinear%20functional%20analysis%20%28lecture%20notes%2C%20web%20draft%2C%202004%29%2874s%29.pdf),
with Theorems 2.1–2.2/2.11 and the local-sign/negative-determinant proof
cases already inspected in `2026-11-06-individual-divisor-contact-incidence.md`.
The signed derivative formula requires a regular value of a C1 map on
a bounded open domain, continuous closure data and boundary avoidance.
Its more general degree existence does not license summing Jacobian
signs at singular preimages. Any future global comparison must retain
ALL preimages, L861's finite entire-contact census, admissible cuts
and its other hypotheses. This local target does not assume that census
or infer it. No new singular-value degree formula is required or imported.

### Local overlap, search and stronger-result comparison

Read L847(1)–(4), L860's hypotheses/conclusion and complete first-order
necessity section (16)–(17), L861's hypotheses, degree application and
angular-fiber argument, and L859's hypotheses/conclusion. Reused the
three nominated assessments and the odd-contact differentiation review.
Searched multiplicity, rank and homogeneous/binary terms in these
specific contact assessments and the L861 audit histories. No matching
simultaneous-multiplicity classification was found there. This is a
local duplicate check, not a notebook-wide novelty claim.

Read the individual-divisor count-only, periodic-two-moment weight-gap
and divisor-real-flux ATTEMPTS records. Their conditional census,
uncontrolled covariance and unresolved exact real contraction remain
stops for those mechanisms. Necessary higher-multiplicity restrictions
would clarify a hypothesis of L861, not invalidate those stops or solve
the parked lift. L859 cannot drop its nonvanishing second factor.

Queries actually issued included:

- `nonnegative binary forms real linear factors even multiplicity complex conjugate factors theorem`
- `"complex" "linear forms" "product" "real" "nonnegative" polynomial`
- `positive totally real submanifold vanishing holomorphic volume form multiple divisor multiplicity`
- `"nonnegative binary" "factors" "even multiplicity"`
- `"homogeneous" "product" "linear" "nonnegative" "conjugate" binary form`
- `"binary form" "two" "linear factors" "nonnegative"`
- `"holomorphic volume form" "multiplicity" "totally real"`
- `"nonnegative" "product of powers" "linear forms"`

The prior simultaneous-simple review's Szawlowski Theorem 1.1 assumes
right equivalence to a reduced coordinate product. It does not supply
a theorem for arbitrary multiplicities or the real radial sign and is
not imported here. Reused Auroux divisor-complement/nonvanishing-form
coverage likewise does not settle this contact. Search hits on matrix
positivity, Waring length, SOS denominators, special Lagrangians and
unrelated vanishing theorems are unread leads, not supporting results.
The primary polynomial passages above suffice for the bounded necessary
calculation; no essential access blocker remains. No failed search
establishes originality. Full matching Mathlib coverage is not checked.

### Approved specialization boundary and discriminator

After separate source approval, perform exactly TARGET. Keep m,n fixed
positive finite integers and the distinct nonzero actual-G pair
conditional. Check the full nonvanishing coefficient at the center,
original orientation and J(p)!=0 before applying polynomial inputs.
Use first-order directions only; verify any tangent-product reduction
rather than assuming its order or a high-regularity surface. Treat the
four rank-one/rank-two combinations explicitly and justify any exclusion
of rank zero from the radial angular formula. Import known factorization;
the remaining graph-specific restrictions need their own calculation.

Then determine which established necessary cases permit L861's regular
coordinate sign mechanism. Mark singular cases as outside its regular
signed-Jacobian formula, not as impossible contacts. Do not assert exact
feasibility from a permissible tangent, perturb while assuming positivity
survives, construct a global graph, or carry over four/eight bounds before
checking every hypothesis. A classification of necessary cases is enough;
existence of any new case is outside this scope.

Continue if additional multiplicity/rank cases are decided or an explicit
exception limits the regular-value argument. Abandon if only m=n=1 is
replayed, an extra smoothness assumption is needed, or formal tangents
are substituted for exact feasibility. Main-gap relevance remains a
restricted contact input for future global assembly; actual zero data,
contact forcing, global extension and all-degree Xi signs stay unresolved.
The proposed next research classification is REPRODUCTION under SPECIALIZE,
not creative work or a claim of discovery beyond the inspected sources.
