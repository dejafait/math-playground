# Sector-restricted quartic differential count: nomination1464

TARGET: Test whether q(D) can preserve real-rootedness of every real quartic yet increase Z_c from two to four on a monic rational quartic with nonnegative coefficients, when q is rational, q(0)=1, deg q<=4, its coefficients are nonnegative and all its zeros satisfy Re z<0 and |Im z|<=-Re z/3.
CHECKED: 2026-11-18
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1465 searched differential/sector/complex-zero-decreasing operators, quartic Hermite--Poulain counts, constant-coefficient finite-degree count laws and Obreschkoff spellings; exact queries and narrow duplicate checks appear below. No matching restricted count theorem was verified; this is not a novelty claim.
SOURCE_EVIDENCE: Craven--Csordas1983, Illinois J.Math.27(2),244--278, Theorems3.3--3.4/proof and Corollary3.8/proof, pp.257--261, primary scan https://scispace.com/pdf/location-of-zeros-part-i-real-polynomials-and-entire-z3v2jd50yw.pdf; Craven--Csordas2004 manuscript p.2/(1.2), p.21/Theorem3.26, https://www.dcce.ibilce.unesp.br/~dimitrov/ProfRusev/czdssurvey.pdf; Pinkus, Some Remarks on Zero-Increasing Transformations, author manuscript pp.1,3--4,12, https://pinkus.net.technion.ac.il/files/2021/02/stl.pdf. Reuse source-notes1461 and audit1464 as qualified below.
COMPARISON: Sector preservation and the all-real-symbol Hermite--Poulain count theorem do not decide the requested nonreal-symbol finite test. The triangular converse inspected in Pinkus requires every polynomial in all degrees. C020m and coefficient-diagonal examples do not meet this target's exact restrictions. No inspected theorem supplies the desired restricted count inequality or its failure.
GAP: One exact rational quartic witness meeting every saved restriction, or an impossibility proof for the whole stated class, remains unestablished. Certify universal preservation through the reused Walsh interface, not a finite sample of real-rooted inputs; certify sector membership, coefficients and multiplicity-aware input/output counts separately.
REASON: The changed-hypothesis source comparison is complete enough for one bounded algebraic test using accessible Walsh and standard exact root counting, without relying on a guessed sector threshold or blocked original source. This approves the unchanged TARGET for mathematics next turn, not a new result or an automatic count theorem.
SCOPE: D=d/dx; Z_c counts multiplicities; q is rational, q(0)=1, deg q<=4, all coefficients nonnegative, and all zeros satisfy Re z<0 and |Im z|<=-Re z/3; p is monic rational of degree exactly four with nonnegative coefficients. Universal preservation includes repeated-root real quartics with arbitrary nonzero real leading coefficient. Only one bounded witness/impossibility attempt is approved; no degree sweep, actual-symbol approximation or sector-theorem reproof. Matching Mathlib coverage unchecked.
LITERATURE_REASON: The added nonnegative coefficients and explicit left-hand sector are absent from C020m's approved generic test; their effect on a nonreal-count inequality requires a separate theorem comparison before mathematics.

The nomination below is preserved as the pre-review record. Its pending
language is superseded by completed review1465 at the end of this file;
the TARGET has not changed.

Main gap: L030--L032/C032a actual-Xi all-degree positivity, with an
unbounded actual unshifted Jensen exceptional-root deficit. This finite
prerequisite could distinguish a genuinely geometric root-count input
from mere hyperbolicity preservation. It cannot improve the actual
deficit by itself, even if an impossibility theorem is found.

A future mathematical acceptance test would be an exact rational witness
meeting every restriction, or a theorem proving impossibility with
multiplicities. An unsuccessful search is inconclusive. A witness would
stop only this narrower automatic-contraction implication. A positive
count theorem would still need an actual factorization, its precise
coefficient/operator correspondence and a paid exceptional-divisor
count, followed by the remaining degree/height, signs, initialization
and overlap arguments. None of these premises is supplied here.

C020m is contrast evidence, not a premise asserting this sector class
is a preserver. C019j describes actual normalization downstream only;
L018/L021 and C019t supply no sign or restricted count law. No
cross-notebook result is used. The sector threshold must be compared
with a primary statement rather than guessed from OCR or a remembered
Obreschkoff theorem. The original1961/published2022 retrieval stays
parked; seek accessible exact interfaces and independent finite tests.
If a source remains persistently blocked, record that limitation and
park dependent work rather than repeat access attempts.

This is a routine finite algebraic prerequisite, not a protected creative
attempt. No central creative mechanism is ready: actual signed data,
a restricted loss law and actual-factor applicability remain unpaid.
The new gate does not reset old moment/variation exploration budgets.
Full matching Mathlib coverage remains unchecked.

## Completed source comparison — 18 November 2026, step1465

This is a literature-only EXPLORATION, not a counterexample, impossibility
proof or advance on the actual Jensen deficit. No coefficients were
constructed, no mathematical scripts ran, and no lemma was changed.

### Inspected source interfaces

Craven--Csordas1983: Theorem3.3 and remarks(1),(3), pp.257--258,
give circular-region convolution localization and preservation,
including closed half-planes. Reuse C020m/audit1464's exact operator
normalization and repeated-root qualification. Theorem3.4,
pp.258--259, assumes nonnegative factorial coefficients and concerns
real-rooted inputs of degree at most n. Its proof uses Walsh for positive
coefficients, positive perturbations/Hurwitz for zero coefficients,
and the monomial test for the converse. Corollary3.8, pp.260--261,
assumes nonnegative factorial coefficients and all symbol zeros in a
specified double sector; its proof imports Obreschkoff p.273 and uses
Theorem3.4. Its conclusion is preservation, not a count bound on a
nonhyperbolic input. No exact numerical sector specialization is needed
or imported here: parsed formulas are damaged and image calls yielded
no inspectable image. Candidate preservation must instead be certified
with the already checked Walsh interface.

Craven--Csordas2004, manuscript p.2, (1.2), explicitly counts
nonreal zeros with multiplicity and records contraction for q(D) when
q has only real zeros. Theorem3.26, manuscript p.21, assumes an LP
symbol with at least one real zero, a finite-nonreal-zero input and
the stated genus/Gaussian restrictions; its conclusion is eventual
reality after sufficiently many iterates. Neither conclusion covers
the single-step nonreal-symbol question. The latter theorem is quoted
there from [23, Theorem3.3]; that original proof was not newly audited.

The triangular-operator lead at manuscript p.3 was followed to Allan
Pinkus, *Some Remarks on Zero-Increasing Transformations*, author
manuscript, Approximation Theory X proceedings draft (title-page
copyright2001), pp.1,3--4,12. Page1 defines multiplicity counting.
The named Hermite--Poulain theorem on pp.3--4 assumes a polynomial
symbol with all real zeros and nonzero constant coefficient. Its proof
factors into first-order real operators and invokes Rolle, including
the extra end interval; nonzero constant coefficient prevents degree
loss. Page12's converse assumes a triangular operator with a constant
nonzero diagonal and the count inequality for every polynomial in all
degrees. It therefore cannot decide a fixed-quartic test. The joint
Carnicer--Peña--Pinkus2002 journal article returned403; its proof is
unread and is not imported. The coauthor's explicit all-degree scope
suffices to exclude this lead as a decision of the present target;
the blocked article is not an essential input to the finite test.

### Bounded discovery and duplicate checks

Queries included `"differential operators" "sector" "complex zero
decreasing"`, `"nonreal zeros" "quartic" "differential" operator`,
`"differential" "nonreal zeros" "sector" Obreschkoff polynomial`,
`"constant coefficient" "finite degree" "complex zero" decreasing`,
`"q(D)" "nonnegative" "nonreal"`, `"quartic" "Hermite-Poulain"
count`, `"Obrechkoff" "differential" "sector"`, and `Carnicer Peña
Pinkus lower triangular matrices nonreal zeros polynomials
transformations`. Searches also compared nonreal-symbol/sector counts
and composition-theorem terminology. Search hits were used to locate
the primary passages above, not as substitutes for theorem statements.
No exact restricted count theorem or matching rational witness was
verified. Uninspected general sector-preserver and matrix-real-rootedness
hits are leads only; no claim of present-day open status follows.

Local comparisons used source-notes1459's corrected CZDS discussion,
source-notes1461's Kim--Kim and sector-reducing-operator distinctions,
assessment1461, C020m/audit1464, and the generic stop1463. November5's
quartic finite-free and additive-degree assessments concern inverse
factors or compatibility and do not establish this count law. No
sibling notebook or original1961/published2022 retrieval was used.
No known result has been relabeled as a discovery.

### Acceptance and continuation boundary

The approved attempt must supply either a fully certified rational
witness or a proof covering the entire saved class. Walsh supplies the
preservation interface already justified in C020m; Sturm's theorem,
with squarefree decomposition and multiplicities retained, supplies
standard exact root counting. Explicit factors and rational sign bounds
may also certify individual candidates. A certificate must show all
sector and coefficient restrictions, preservation for every real-rooted
quartic, and actual/required counts (2,4). Sampling hyperbolic inputs,
floating-point roots, or failing to find a witness does not settle the
question. No theorem proving count contraction is assumed.

This is a finite prerequisite, not a central creative mechanism. A
witness would stop only this restricted automatic implication; an
impossibility theorem would still leave actual-factor correspondence,
exceptional-divisor counts and unbounded-degree control unpaid, as
well as signs, initialization and overlap. The lack of an independent
actual-data loss law blocks a justified creative central nomination.
The original target and exploration histories are preserved. Once this
gate is accepted, proceed to its exact mathematical test; further
literature requires a specific new essential hypothesis or source.
