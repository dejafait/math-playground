# General relative construction — proposed known-source specialization

TARGET: Write a cited finite construction argument for L037's complete torsion-free relative presentation and geometric-reflection/good-prime operators at arbitrary exact conductor N.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed arbitrary-level source comparison in drafts/literature/2026-10-08-general-relative-operator-construction.md; its theorem domains and searches cover precisely this assembly, beyond the fixed conductor-389/T_2 assessment.
SOURCE_EVIDENCE: Stein 2007 equation (3.2.1), Propositions 3.10--3.11, Theorem 3.13 and Section 3.4.1 https://wstein.org/books/modform/stein-modform.pdf; reflection equations (11)--(12), Remark 1.43 https://wstein.org/books/modform/modform/modular_symbols.html; Cremona corrected second edition Propositions 2.2.1--2.2.2 https://johncremona.github.io/book/fulltext/chapter2.pdf; Sergeraert arXiv:2411.02422v1 Sections 2, 3.1, 4, 6--7 and Theorem 1 https://arxiv.org/html/2411.02422v1; Sage transformation-output specification https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_integer_dense.html#sage.matrix.matrix_integer_dense.Matrix_integer_dense.smith_form; inspected domains and access qualifications in drafts/2026-10-08-general-relative-construction-source-notes.md.
COMPARISON: Known results give full integral relative symbols modulo torsion and finite exact algorithms at every positive N and requested good prime; the notebook lacks their general certified-construction assembly, while L030 verifies only a fixed instance and L037 grants construction termination.
GAP: State and justify complete coset/lift generation, all relation saturation and integral-generator coordinates, finite endpoint reduction and complete reflection/good-prime matrix witnesses, retaining elliptic-point torsion and all finite descent checks.
REASON: A known-source specialization can remove the granted finishing-construction premise without reproving topology, multiplicity or Smith normal form; citations alone do not specify the notebook's full evidence contract.

SCOPE: One proof_attempt giving a finite construction argument, not an implementation or instance computation; N is a supplied positive exact conductor, E and f satisfy L029, and independently certified a_ell(E) are supplied as needed. Any finite set of primes ell not dividing N is covered. No arithmetic conductor computation, finite Hecke cutoff, complexity bound, period scale, q or BSD conclusion.

This ready continuation was saved in a literature-only turn; it receives
the supervisor's separate next-turn approval. No mathematical assembly
has been performed here. Essential input IDs are L029 and audited L037;
L030 is a comparison only, not a premise for arbitrary N.

Import Stein's complete presentation modulo torsion and integral relative
homology identification by precise citation. Retain all cosets and both
relation types; certify the full torsion-free quotient by a general
rectangular/arbitrary-rank integer normal-form theorem with unimodular
witnesses. Coprime integer lifts at composite N need their own finite
construction explanation. Import the path-reduction and operator results;
use every endpoint, complete relations and every integral-generator value.
The geometric reflection must have L029's sign. Do not reprove source
theorems or infer a lattice from rational dimensions.

Continuation test: succeed only if each finite construction is justified
to finish and its complete evidence is independently checkable on the
full relative integral quotient; any missing generator, residual torsion,
unjustified lift or operator-descent failure prevents discharging L037's
premise. State any surviving qualification instead of declaring coverage
to be an actual certificate. Combine with L037 only under unchanged
exact-conductor/newform/arithmetic assumptions; no new cutoff is sought.

The plausible downstream use is producing L029's relative integration line
by L037's eventual dimension-one test, independent of q. Independent q,
normalized denominator and nonzero coefficient certificates, rational
membership, divisible Sha and complex-order comparison remain unresolved.
Preserve ATTEMPTS/022--024 and parked twist sources. This is reproduction
of known mathematics, not a new discovery or BSD candidate. Mathlib full
matching coverage was not checked.

## 2026-10-08 direct-source recovery

The direct primary URLs above were reopened successfully in this recovery
turn. Reused the completed source comparison; no new theorem coverage or
mathematical assembly is claimed. The saved TARGET, SPECIALIZE decision,
scope and continuation test are unchanged. Cremona's coset propositions,
Sergeraert's finite-diagonalization statement and Sage's transformation
contract were located again to identify the cited passages. Stein's PDF
and online reflection chapter remain accessible. Manin's omitted original
proof and the original Kannan--Bachem source remain unread as recorded;
neither becomes a new premise. The existing notes retain the rectangular
qualification and full-torsion requirement. This correction repairs the
assessment's missing direct URLs and permits a separate supervisor gate
check; it does not discharge L037's construction assumption.
