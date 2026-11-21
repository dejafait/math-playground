# Sector-sextic partial-count nomination1468

TARGET: Test whether a rational q(D), q(0)=1 and deg q<=6, with nonnegative coefficients and all zeros satisfying Re z<0 and |Im z|<=-Re z/3, can preserve real-rootedness of every real sextic yet send a monic rational sextic with nonnegative coefficients and exactly two nonreal roots to one with exactly four; give an exact witness or prove impossibility.
CHECKED: 2026-11-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1469 searched sextic/finite-degree differential count, Walsh convolution/nonreal counts and sector/CZDS terminology; inspected primary passages and reused assessment1464/review1465. No exact restricted count theorem or matching witness was verified; queries and scope comparison are below, without a novelty claim.
SOURCE_EVIDENCE: Craven--Csordas1983, Illinois J.Math.27(2),244--278, Theorem3.3/remarks(1),(3), Theorem3.4/proof, Corollary3.8/proof, pp.257--261, https://scispace.com/pdf/location-of-zeros-part-i-real-polynomials-and-entire-z3v2jd50yw.pdf; Craven--Csordas2004 survey (1.2)/Theorem3.26, pp.2,21, https://www.dcce.ibilce.unesp.br/~dimitrov/ProfRusev/czdssurvey.pdf; Pinkus pp.3--4,12, https://pinkus.net.technion.ac.il/files/2021/02/stl.pdf; Borcea--Guterman--Shapiro, Preserving positive polynomials and beyond, author manuscript pp.8--9,12--13, Proposition3.7/Remark3.9/Proposition3.10 and TheoremC/Lemma5.1/proof, https://staff.math.su.se/shapiro/Articles/PositivPreserv.pdf (arXiv:0801.1749v2 record dated2008-01-22; byte identity not asserted).
COMPARISON: Walsh supplies a finite-degree preservation certificate, not the partial-count inequality. The all-real-symbol count theorem and all-degree triangular converse do not decide this finite nonreal-symbol class. C020n excludes a root-free quartic output only; C020m and the inspected diagonal counterexamples lack the saved restrictions. The positivity criterion inspected in review1469 does not count roots of an output retaining real zeros.
GAP: One exact sextic (2,4) witness satisfying every restriction, or impossibility for the entire saved class, remains unestablished. No sextic coefficients, inverse, root counts or certificate have been computed or derived. Actual-Xi applicability remains independently absent.
REASON: Completed changed-degree source comparison supports one bounded mathematical attempt on the unchanged TARGET using accessible preservation and exact-count interfaces. No essential source is blocked for that attempt. This approves exploration next turn, not a theorem, novelty certification, degree sweep or automatic actual-Xi transfer.
SCOPE: One fixed V_6 test with counts (2,4), counting multiplicities. Universal preservation includes every real-rooted sextic with repeated roots and arbitrary nonzero leading coefficient. No degree sweep, sector widening, actual-symbol estimate or unbounded-degree claim is approved.
LITERATURE_REASON: Changing the degree from four to six introduces a partial-count case with real roots in the output; assessment1466 covers only C020n's V_4 audit. The exact new implication needs source coverage even though the sector is unchanged.

The original nomination paragraphs below are retained as historical context;
their pending status is superseded by completed review1469 at the end.
Preserve the exact proposed
mathematical TARGET while reviewing it; do not derive and approve it in
the source-review turn. The original1961/published2022 retrieval stays
parked. Accessible finite-degree convolution and count results should
be compared first; a failed search is not evidence of novelty.

The main gap remains L030--L032/C032a actual-Xi all-degree positivity
and the unpaid unshifted Jensen exceptional-root deficit. C020n and its
complete certificate1466/audit1468 are the essential finite comparison.
C020m/audit1464 is a contrast, not an input asserting sector preservation.
The actual coefficient normalization is C019j, with L018/L021 downstream;
none supplies an actual-factor/operator correspondence or a paid
exceptional-divisor estimate. Those assumptions, unbounded-degree
control, signs, initialization and overlap would remain unresolved even
after a successful finite test. No cross-notebook input is proposed.

After source approval, a useful bounded test would either certify every
restriction of an exact witness, including universal preservation and
multiplicity-aware counts, or prove impossibility for the entire stated
class. An inconclusive search is not a stop theorem. A witness would
abandon this partial-count shortcut while retaining C020n; impossibility
would justify considering its precise mechanism, not a degree sweep or
an automatic actual-Xi transfer. The source review should instead import
an exact known answer if one covers the target.

This is an established finite-operator prerequisite, not a protected
creative attempt. A central creative nomination is still blocked by the
absence of a justified actual-factor correspondence and an independently
testable actual-divisor loss mechanism. Merely increasing degree does
not supply either. All previous moment/variation exploration usage and
generic/source stops remain. Full matching Mathlib coverage is unchecked.

## Completed source comparison — 18 November 2026, step1469

This literature-only step is EXPLORATION. It changes the source gate from
REVIEW_REQUIRED to EXPLORE for the exact TARGET, without a mathematical
claim about sextics. The main gap, intermediate use and acceptance test
remain those in the nomination. No lemma or mathematical script changed.

### Inspected statements and their limits

Reuse assessment1464/review1465's primary comparisons. The1983 primary
scan was reopened at Theorem3.3 and its remarks, pp.257--258, then at
Theorem3.4 and its proof, pp.258--259, and Corollary3.8/proof,
pp.260--261. Walsh assumes two polynomials of degree n and a circular
region containing all zeros of one; its convolution zeros lie in the
union of translates by the other's zeros. Closed half-planes are allowed;
the real-rooted consequence has no simplicity assumption. This supplies
the preservation interface for the nominated degree, but no bound on
partial nonreal counts. Theorem3.4 assumes nonnegative factorial
coefficients; its proof covers zero coefficients by perturbation/Hurwitz
and uses a monomial for the converse. Corollary3.8 concerns sufficiently
narrow double-sector symbols and concludes preservation. Its numerical
sector formula remains OCR-damaged and is not imported or specialized.
Universal preservation stays explicit and must be certified independently.

The2004 survey's Theorem3.26, p.21, was reopened: both entire factors
have genus0/1 after removal of nonnegative Gaussian exponents, whose
product is zero; the symbol is in LP with a real zero, and the input
has finitely many nonreal zeros. The conclusion concerns sufficiently
many iterates. Reuse its (1.2) all-real-symbol count law and Pinkus's
named Hermite--Poulain theorem, pp.3--4. Pinkus p.12 was reopened to
check the triangular converse: the count hypothesis ranges over every
polynomial in every degree. None covers a nonreal symbol on sextics
in a single step. The survey's cited original iteration proof was not
newly inspected and is not an essential input.

Borcea--Guterman--Shapiro's author manuscript, pp.8--9, gives diagonal
counterexamples in Proposition3.7; Remark3.9 and Proposition3.10 reject
an inverse-positivity/CZDS equivalence. Their operator class differs from
constant-coefficient q(D), so they do not settle our restricted test.
On pp.12--13, equation(9), TheoremC and Lemma5.1/proof treat real
constant coefficients through even degree k=2l. The nonnegativity
branch uses the Hankel matrix ((i+j)! alpha_(i+j)) for 0<=i,j<=l and
positive semidefiniteness. The inspected proof uses evaluation at zero,
translation and a cited moment criterion (Widder, The Laplace Transform,
1941, Theorem11, p.133; that original was not read). This is a
nonnegativity interface, not a partial-count theorem. Neither its strict
positivity equivalence nor a new moment specialization is imported.

### Bounded discovery and local overlap

Queries actually issued included `"complex zero decreasing" "finite"
"differential"`, `"convolution" "number of nonreal zeros" polynomials`,
`"sector" "differential operators" "nonreal zeros"`, `"sextic"
"complex zero" differential`, `"finite" "complex zero decreasing"
"convolution"`, `"Walsh convolution" "real zeros" number`,
`"differential" "sextic" "nonreal" zeros`, `"finite degree"
"zero-increasing" differential`, `"Walsh convolution" "nonreal"`,
and `"sector" "complex-zero-decreasing" polynomial`. The positivity
paper was located by its exact title and authors. Its arXiv version
record was read separately; the inspected text is the author-hosted PDF.
Search results were discovery aids, not theorem evidence. No verified
exact sextic answer emerged; this does not establish novelty or open status.

Local checks used the saved assessment1464 and the canonical C020n
proof through its scope discussion; C020m/audit1464's generic failure
is reused as contrast. Narrow searches in November17--18 assessments
and November18 sector attempt records found no ready assessment for
this exact partial-count target. No sibling notebook was read. Existing
moment/variation exhaustion and original1961/published2022 source stops
remain; neither blocked retrieval was retried. Sector-reducing and
finite-difference search hits are unread leads, not imported results;
no statement about their present-day open problems is adopted.

### Approved attempt and stopping boundary

One mathematical attempt may now construct an exact rational witness
or prove impossibility for the entire nominated class. A witness must
check rationality, q(0)=1, degrees, coefficient signs and every sector
zero, and certify preservation of every real-rooted sextic, including
repeated roots and arbitrary nonzero leading coefficient. Use the
degree-n Walsh theorem with the factorial normalization checked, not
sampled inputs or an unread sector threshold. Multiplicity-aware exact
counts must be (2,4); use standard Sturm theory with repeated factors
retained, or exact factorization/sign arguments. Failed search is
inconclusive. No reproof of the imported preservation theorem is needed.

A witness stops only this partial-count shortcut; impossibility would
retain a finite prerequisite. Actual-factor correspondence, paid
exceptional-divisor loss, unbounded-degree control, signs, initialization
and overlap remain independent gaps. No central creative target is
justified by this extension alone: an independently testable actual-data
loss mechanism and its applicability are absent. The next task is
established-route development, not creative routing. Full matching
Mathlib coverage is unchecked; this source review adds no theorem.
