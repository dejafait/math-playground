# Fixed CM directional theorem import — source approval repaired

TARGET: Import the fixed CM characteristic-order upper bound from Balakrishnan--Muller--Stein Theorem 1.6 and equation (1.3) for y^2=x^3+1 at p=7, matching L002's X and L057's primitive normalization.
CHECKED: 2026-10-14
DECISION: IMPORT
SEARCH_EVIDENCE: The separate universal CM source review found this direct published directional statement; local duplicate checks found only L004's non-CM import and L057's analytic input. See drafts/sources/2026-10-14-cm-ordinary-bound-source-notes.md.
SOURCE_EVIDENCE: BMS publisher offprint https://wstein.org/papers/mcom3029.pdf#page=4 (DOI 10.1090/mcom/3029), Theorem 1.6/equation (1.3), p.986, and Sections 2.1--2.3 pp.987--993; direct URL and load-bearing passages rechecked on 2026-10-14. Details: drafts/sources/2026-10-14-cm-ordinary-bound-source-notes.md. Kato original proof not newly read.
COMPARISON: The published order inequality includes elliptic curves without a CM exclusion. Audited L057 records the fixed optimal model, differential scale one, total period, trivial branch and good ordinary seven required to identify the source series; foundations/03 and L002 supply X. Only applicability and a precise known-theorem import are needed.
GAP: The fixed canonical import and subsequent critical audit remain unwritten. No universal Rubin specialization, reverse divisibility, integral main-conjecture equality, non-CM height converse, coefficient corollary or BSD conclusion is covered.
REASON: Use the source's explicit one-sided order theorem rather than deriving an unassessed CM-field specialization; a reproof of Kato, Rubin or measure construction is unnecessary and unauthorized.
SCOPE: Only E:y^2=x^3+1, p=7, classical cyclotomic Selmer dual X, audited L057 primitive series with gamma satisfying kappa(gamma)=8 and unchanged total-period/orientation qualifications; IMPORT permits KNOWN_IMPORTED only.

Main gap: arbitrary rank/complex-order equality above analytic rank one.
Intermediate target: the fixed CM upper bound already stated in the
published source. Downstream use: permit a later arithmetic use of a
certified coefficient together with independently proved rational lower
bounds. The L058 coefficient alone gives no rank-two witness.

Essential input IDs: L002 and L057, with L028/L050/L052/L056 qualifications
inherited through the latter; foundations/03 defines X. L004 and
foundations/05 are contrasts, not CM inputs. L058 may be mentioned as a
fixed test, but no new coefficient consequence is part of this target.
No cross-notebook result is used. Matching Mathlib coverage is not checked.

Continuation test: the canonical import must identify the classical X,
source order inequality and exact primitive normalization, explicitly
retain power-of-p qualifications, and make no stronger arithmetic claim.
If a needed source hypothesis or period/local-condition identification
fails, stop the import and record that mismatch. No new character descent,
isogeny comparison, extra Euler factor or conjectural equality is allowed.
The fixed curve's optimality and scale are already justified in L057;
this review does not prove them again. No mathematical derivation occurs
here. The separate literature approval and direct-URL repair are complete; the unchanged fixed target is ready for the next research invocation.

## Separate approval record — 2026-10-14

The recovery request concerned the missing direct URL in SOURCE_EVIDENCE.
Reopened the linked publisher offprint and inspected printed p.986,
including the theorem and Selmer definition, plus the period and measure
passages on pp.988 and 990--993. Compared these with foundations/03
and L057’s existing applicability and orientation passages. The prior
IMPORT scope is unchanged. This is a citation/process repair, not a new
theorem application or additional mathematical advance. No reproof is
needed; Kato’s proof is used through the published BMS statement.
