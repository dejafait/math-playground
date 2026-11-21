# Variable-quartic single-factor count nomination1478

TARGET: Determine whether Z_c((1+D+tD^2)(R(y)(y^2+by+c)))<=2 for every monic real quartic R with four real roots counted with multiplicity, every real b,c with c>b^2/4 and every 1/4<=t<=5/18; import a matching theorem or give an exact counterexample or a uniform proof.
CHECKED: 2026-11-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1479 searched quadratic constant-coefficient differential count, bounded-degree CZDS, Walsh partial counts and finite-free convolution terminology; primary statements and relevant proof cases were inspected. No matching theorem or exact counterexample was verified; bounded queries and comparisons are below.
SOURCE_EVIDENCE: Reuse assessment1468/review1469 and assessment1464/review1465; newly inspect Craven--Csordas1982, Pacific J.Math.102(1),15--31, multiplicity convention p.16, Theorem2.3/proof opening pp.18--19, Theorems3.1/3.3 and Corollary3.4/proof pp.25--26, https://msp.org/pjm/1982/102-1/pjm-v102-n1-p03-s.pdf; Marcus--Spielman--Srivastava, arXiv:1504.00350v2 (3 July2019), Definition1.1/equation(1), Theorems1.2--1.3, discussion p.6 and Theorem1.11, pp.2--3,6--8, https://arxiv.org/pdf/1504.00350v2.
COMPARISON: The all-real-symbol count law applies at the repeated-real-symbol endpoint only; its symbol hypothesis fails in the remaining interval, by the roots already displayed in C020p. Walsh and the finite-free preservation/maximum-root results require both complete inputs real-rooted; they do not count roots for R times a positive irreducible quadratic. No general-spacing reduction follows from C020p/r/s/t.
GAP: A uniform single-factor degree-six count bound for arbitrary real-rooted quartic R, including repeated roots, or an exact counterexample remains unestablished. No new polynomial identity, counterexample, root count or proof was derived in this literature turn.
REASON: The changed-scope theorem comparison is complete enough for one bounded uniform structural attempt on the exact unchanged TARGET. No essential source is blocked for that attempt; EXPLORE is not a novelty claim, theorem or approval of a general-symbol/composition/Xi extension.
SCOPE: One quadratic differential factor, one degree-six input with a positive quadratic factor, root counts including multiplicities; no product, degree sweep, sector change or actual-Xi application.
LITERATURE_REASON: The proposed claim replaces fixed-spacing inputs by every real-rooted quartic, including all repeated-root limits, and quantifies over real coefficients. Existing source coverage did not compare this exact uniform count statement to known finite-degree complex-zero-decreasing theorems.

At nomination1478 this was a proposal for a separate review, not
permission to derive the statement during the completed audit. Review the exact finite-degree
count law first, reusing the ready primary preservation and all-degree
count comparisons in assessment1468/review1469. Search for the uniform
single-quadratic statement and stronger known finite-degree count laws;
a rephrased preservation theorem alone does not answer the question.
An adequate source should be imported with exact hypotheses; a
specialization should identify only the missing difference. An exact
counterexample must have a certified t in [1/4,5/18],
a real-rooted quartic and a strictly positive quadratic factor, with
multiplicity-aware counts. It need not meet the older rational or
nonnegative-coefficient restrictions unless that further consequence
is proved separately.

The downstream use is precise: a uniform positive answer would exclude
a single quadratic operator for every real sextic with exactly one
nonreal pair, because such a sextic factors over the reals into a
real-rooted quartic and a monic irreducible quadratic after dividing
by its leading coefficient. An exact negative answer would refute this
uniform single-factor shortcut, not RH. General allowed degree-six
symbols and compositions would still require separate treatment even
with a positive answer. No reduction to this operator class is assumed.

Essential local context is C020t/audit1478, C020p's Walsh interface,
C020r/s/audit1476 and the fixed-family stop1477. C020p's remaining
proof and C020o/q remain unaudited. The direct-moment, variation,
inverse-positivity, finite-grid and expanded-coefficient stops remain
in force at their recorded scopes; no exploration budget is reset.

Continuation test: accept a matching known theorem only after checking
its degree range, operator normalization, nonreal-count conclusion and
all multiplicity/endpoint cases. If there is no match after a bounded
comparison, record the exact gap and approve at most one uniform
structural attempt; do not collect further fixed-spacing examples.
A theorem whose hypotheses exclude our nonreal symbol, or a finite
preservation statement without the count bound, is insufficient.
Persistent source blockage requires parking this target rather than
repeating access attempts. This proposed route is independently
testable but is not yet a central creative mechanism.

The main RH gap remains L030--L032/C032a actual-Xi all-degree positivity
and the unpaid exceptional-root deficit. Actual-factor applicability,
a paid actual-data loss mechanism, all degrees, signs, initialization
and overlap remain absent. Those missing applicability inputs prevent
a justified central creative nomination here; this finite prerequisite
must not be presented as one. Full matching Mathlib coverage is unchecked.

## Completed source review — 18 November 2026, step1479

Outcome EXPLORATION; classification NOVELTY_UNCHECKED. The gate is now
EXPLORE for the unchanged TARGET, not an answer to it. The earlier
nomination and audited exclusions are preserved. No lemma, mathematical
script, PROOF paragraph or DAG row changed.

### Primary theorem comparison

Craven--Csordas, *On the number of real roots of polynomials*, Pacific
J. Math. **102**(1) (1982), 15--31,
[primary PDF](https://msp.org/pjm/1982/102-1/pjm-v102-n1-p03-s.pdf):
p.16 includes multiplicities. Theorem2.3, pp.18--19, assumes real-rooted
h and arbitrary real f. Its induction factors h into real linear
factors; zero constant coefficient is handled by removing a power
and differentiating f. Theorems3.1/3.3, pp.25--26, require negative/
nonpositive real symbol roots; 3.1 also assumes deg f<=deg h.
Corollary3.4/proof, p.26, gives the Hermite--Poulain count law in the
nonzero-constant case relevant here, without simplicity. A zero-constant
real-count claim would need degree-loss qualification and is not
imported. The proof counts branches intersecting x=1, retaining the
real-symbol premise. C020p already displays our symbol roots: the
endpoint has real roots, the interior does not. Replacing this symbol
by T(y^6) does not meet that premise. No new specialization is proved;
Pinkus's qualified all-degree count interface is reused from1464.

Marcus--Spielman--Srivastava, *Finite free convolutions of polynomials*,
[arXiv:1504.00350v2](https://arxiv.org/pdf/1504.00350v2), submitted version
3 July2019 (PDF title date4 July2019), Definition1.1/equation(1), p.2,
uses the derivative convolution normalized by 1/d!. This matches the
Walsh interface already justified in C020p, not a different coefficient
map. Theorem1.3, p.3, assumes both degree-d inputs real-rooted and
concludes real-rootedness and an extreme-root upper bound. It does
not require simple roots. The discussion p.6 and Theorem1.11, pp.7--8,
also keep real-rooted inputs. Theorem1.2, p.3, is an expected
characteristic-polynomial identity for complex normal matrices;
it makes no partial-count assertion. These statements do not accept
R(y)(y^2+by+c) as a real-rooted degree-six input. We import no new
matrix argument or conclusion about expectations. This PDF is the
inspected preprint; equality with a published version is not asserted.

Reuse rather than reprove assessment1468/review1469's Walsh,
all-degree CZDS, iteration, diagonal counterexample and positivity
comparisons. Their scope exclusions persist. In particular neither
an eventual-iteration theorem nor positivity of an inverse settles
a single-step partial count. The exact original1961/published2022
retrievals remain parked, and are not prerequisites for this finite
attempt. No claim about their unread contents is made.

### Bounded search, local overlap and evidence limits

Queries included `quadratic differential operator finite degree complex
zero decreasing sextic real rooted polynomial`; `Craven Csordas complex
zero decreasing differential operator finite degree n quadratic`;
`"finite degree" "complex zero decreasing" constant coefficients`;
`"quadratic" "complex zero decreasing" operator`; `"finite"
"convolution" "nonreal zeros"`; `"Walsh convolution" "number"
"nonreal"`; `"finite free" "non-real" roots`; `"differential operator"
"quadratic" "nonreal zeros" polynomial count`; and `"complex zero
decreasing" "bounded degree"`. Exact-title searches located the two
primary PDFs. Search snippets were discovery aids. No matching count
law or exact counterexample was verified; this is neither an exhaustive
bibliography nor a claim that the question is open or original.

The PMC copy of the finite-free article displayed a browser challenge;
the accessible arXiv primary version supplied the inspected statements.
Screenshot calls on the1982 scan produced no inspectable image; the
relevant statement/proof text was accessible. No OCR-obscured numerical
threshold is used. Sector-reduction, finite-difference and derivative
localization hits were not newly read or imported. The previously
assessed sector-reduction distinction is reused from source-notes1461.
Full matching Mathlib coverage is unchecked.

Local reads were C020p's hypotheses and Walsh interface, assessment1468,
review1469, assessment1464's completed source section, source-notes1461's
relevant comparisons, audit1478 history and fixed-family stop1477.
A narrow search of November17--18 sector/quartic assessments and
November18 sextic history/stops found no already ready universal-quartic
count assessment. No sibling proof or checkpoint was read. Existing
uncommitted and unfinished work was preserved.

### One approved continuation and stopping test

One subsequent mathematical turn may attempt the exact TARGET using
arbitrary ordered real quartic roots and all real b,c satisfying
c>b^2/4. A uniform sign/collision argument must handle arbitrary
spacings, all quartic multiplicities and both closed t endpoints;
there is no approved extremal reduction. An exact counterexample must
certify every hypothesis and more than two nonreal output roots with
multiplicity. It need not satisfy the older nonnegative/rational
coefficient class. A failed search is inconclusive. An accepted uniform
proof would exclude the single-factor shortcut; an accepted counterexample
would refute this uniform law only. All new arguments still need a
separate critical audit.

Do not collect additional fixed spacings, inverse-positivity examples,
expanded-coefficient grids or an unapproved degree sweep. If the uniform
attempt supplies neither an informative obstruction nor a viable
uniform argument, save its partial reasoning and reassess before any
repeat. No known theorem is to be reproved; only the unprovided partial
count is at issue. C020p's unrelated proof and C020o/q remain unaudited.
Actual-Xi correspondence, paid exceptional loss, arbitrary compositions,
all degrees, signs, initialization and overlap remain independent gaps.
No central creative nomination is justified by this finite prerequisite:
the actual-data applicability and independently testable paid-loss
mechanism are still absent. This next attempt is development.
