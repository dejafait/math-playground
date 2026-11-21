# Centered companion terminal-three test nomination1523

TARGET: Test a uniform positive degree-linear lower bound for K_d(D) from the last three principal coordinates of C028d's centered companion, using its exact coefficients and arbitrary positive diagonal D.
CHECKED: 2026-11-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Review1523 completed assessment1522's bounded matrix/scaling comparison and narrowed the nominated at-most-four-coordinate test to three coordinates; exact queries and local overlap/failure checks are in drafts/literature/2026-11-18-centered-companion-source-notes-1523.md. The finite optimized cost was not derived or evaluated during that literature review.
SOURCE_EVIDENCE: Schmeisser2002 Lemma1 pp211-212 https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf ; Higham2021 identity(*) https://nhigham.com/2021/03/23/what-is-a-companion-matrix/ ; Watrous2018 Section1.1(1.168),(1.175),(1.179)-(1.181),pp32-34 https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf . Direct sources reopened and essential statements checked in recovery1524; prior detailed scope is in source-notes1523. De Teran-Dopico-Perez2014 Section7 https://gauss.uc3m.es/fdopico/papers/laa2013-bounds-fiedler.pdf remains an inspected whole-matrix norm contrast, not a K_d input.
COMPARISON: Known matrix majorization and norm contraction supply the height interface and compression; C028d and C028a fix the actual coefficients and strict central-moment signs. The remaining difference is finite coefficient extraction and an unrestricted positive-ratio optimization, not a reproof of those theorems or an extension of C028a/c's reference families.
GAP: Decide whether this three-coordinate compression alone forces K_d(D)>=c*d for a d-independent c>0 in every sufficiently large degree and for every positive diagonal D. No block formula, c, onset or countersequence is established in this assessment.
REASON: A bounded known-method calculation could stop a distinct candidate majorant or expose its surviving scaling regime; source coverage is adequate. This newly written ready nomination requires separate next-turn approval and does not authorize its own mathematical invocation in review1523.
SCOPE: Exactly the real centered Q_d and binomial coefficient formula of C028d, integer d>=3, last three coordinate indices d-2,d-1,d, positive diagonal D with arbitrary d-dependent entries; use C028a's established central cubic combination and S_2,S_3>0. No RH, real/simple roots, bounded condition number, irreducibility or positive symmetrizer is assumed.

## Object, input use and exact limits

Use assessment1522's proposed companion A_d with subdiagonal1 and
last-column entries -c_(d,d-j+1). Set B=D A_d D^(-1) and
K_d(D)=||(B-B*)/(2i)||_1, with the Schatten trace norm. Form the
Hermitian imaginary part after scaling. Use the coordinate inclusion
E:C^3->C^d onto d-2,d-1,d and inspect E*((B-B*)/(2i))E.
All other coordinates must be retained when interpreting the full cost;
they may be omitted only for the cited compression lower comparison.

C028d supplies the exact centered coefficient formula and c_(d,1)=0,
c_(d,2)=-binom(d,2)S_2. C028a supplies the existing actual central cubic
combination and its strict sign. Extracting the needed centered entries,
with all factorials, is deferred to the calculation. C028b supplies the
H_d=o(d) criterion; audited C028g supplies its limiting functional;
neither supplies the desired upper bound. C028a/c's failed budgets and
degree-stop1514/1515 are contrasts only. No inherited evaluator is
necessary unless the calculation actually introduces numerical constants;
prefer a symbolic threshold from the established strict signs.

The bounded test seeks one uniform c>0 and an onset, allowed to depend
on the fixed actual coefficients, covering every positive D and all
sufficiently large integer degrees. Stop this majorant if that floor is
proved. If the compression instead admits cost/d->0, preserve the exact
positive-ratio countersequence and abandon this block as an obstruction;
the full K_d may still be large. An unresolved optimization remains
unresolved, without a parameter sweep, a fourth-coordinate extension or
a changed matrix family during this single target. Any such new target
needs its own source-scope decision.

Plausible use: an o(d) full cost would pay the height criterion, whereas
the proposed floor would eliminate that payment mechanism efficiently.
Neither a cost floor nor a large numerical cost forces any nonreal root
or refutes RH. This is calculation, standard/high, a reproduction or
specialization of known matrix methods. It is not a justified creative
central mechanism. Full matching Mathlib coverage is unchecked.

## Separate approval and URL repair1524

On 2026-11-18 the separate literature recovery reopened the three
load-bearing URLs above. Schmeisser Section3 definitions and Lemma1
(printed pp211-212) cover arbitrary square complex matrices; no
orthogonal-polynomial premise is attached to that lemma. Watrous
(1.175) covers compatible rectangular operators and every p in [1,infinity];
(1.165)-(1.168) and (1.179)-(1.181) specify the norms used. Higham's
opening identity(*) explicitly includes the alternative companion
placements. These checks confirm the previously recorded scope;
no source supplies the actual terminal-block optimization.

The TARGET and SCOPE remain unchanged. SPECIALIZE is approved for the
next invocation's single finite calculation, with C028d and C028a as
its exact local coefficient inputs. No new mathematics was performed
in recovery1524. This repairs the missing direct URLs in the assessment
itself rather than changing the route or claiming another source advance.
Full matching Mathlib coverage remains unchecked.
