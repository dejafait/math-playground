# Exact polyhedral sign/equality test — source scope approved

TARGET: Test exact polyhedral feasibility of L084's selected equalities with all 85 original plane-domain rows and 45 moment signs.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 307 read canonical L084 and L085 through the affine multiplier construction, foundations/10's equality and polyhedral coverage, the saved step-306 lift/reverse record, ATTEMPTS/052–053,060–068 and the equality-audit assessment. Primary-source searches for rational LP feasibility, Farkas/basic feasible solutions and exact simplex/Phase I found standard certificate and algorithm coverage; no checked source contains a verdict for this finite subsystem.
SOURCE_EVIDENCE: Reinspected Goemans Lecture 3 (19 September 2001), Theorems 1 and 3 and projection proof pp.1–2; MIT 6.854 (2020) Notes 11, Introduction, Linear Equalities and Basic Feasible Solutions; Goemans An Introduction to Linear Programming (October 1994), The Simplex Method pp.7–8; Nannicini–Nasrabadi MIT 15.053 Recitation 3 solutions (Spring 2013), Problem 3.A–B pp.4–6. Reuse Ye October 2017 Theorem 1.11 p.13 and Section 1.5.1 pp.23–24 via foundations/10; exact primary links and qualifications below.
COMPARISON: General rational LP methods cover the sign/equality subsystem once its affine identity is retained. L085 establishes constant selected cross vectors and affine selected Schur slacks; step 306 records the complete 48-to-21 equality lift and reverse. Unlike the stopped joint conic targets, this test drops all 53 other modes and permits exact rational Phase I. No inspected source supplies the finite feasibility verdict, which still requires original/raw certificate verification.
GAP: No essential source coverage remains missing for this narrowly scoped test. The affine coefficients, exact lift, 85 original domain rows, 45 signs and 28 original/raw equalities must be reconstructed and verified in the later calculation; feasibility here leaves the 53 remaining modes undecided.
REASON: The changed scope has now been separately compared with known rational LP alternatives and a bounded exact method. Approve one later RESEARCH / REPRODUCTION attempt on this subsystem; no calculation, feasibility conclusion or new lemma is claimed in this source review.
LITERATURE_REASON: Changed target drops the 53 remaining PSD modes and replaces the stopped floating conic proposal with exact rational polyhedral certification over the entire original plane; the proposed certificate method and limits need separate scope approval.
SCOPE: Exactly TARGET, with all three original plane parameters free, the saved complete affine equality elimination, all 85 domain rows and 45 moment signs; one bounded rational Phase I attempt as specified below, with no point scans, variable caps or conic solve.

Essential inputs: reviewed L084/L085, L076,L078,L082,L083 and the saved
step-306 affine lift/reverse identities; ancestral L021,L053,L073,L075
and foundations/04,09,10,12 retain all qualifications. Keep original rho,
p8, pairs, dictionary, seven-column RREF/completion, 90 weighted kernel
equations, all 500 types/3000 presentations, 36 forced and 45 free moments,
the full anchor and all original/raw coordinate conversions. No changed
pair/base/column domain, variable caps, point scan or new conic run.

Prospective discrimination: either a rational assignment satisfies every
domain row, sign and selected original/raw equality, or a correctly
oriented rational Farkas combination gives a strict whole-domain
contradiction. Mere solver failure, resource exhaustion or a numerical
dual would leave this subsystem undecided and must be saved honestly.
The bounded exact method is specified below. Rational LP certificate
existence is distinguished from obtaining a certificate within its budget.
Any feasible witness parks sign-only exclusion but leaves the 53 PSD
modes, other anchors, global consistency and RS realization unresolved.
Any exclusion concerns this fixed pair/base/family only. Both outcomes
could inform the next joint-feasibility decision, without changing the
955–957 boundary by themselves. The main gap remains arbitrary-center
67/68-agreement safety. Mathlib matching coverage is not checked.

## Primary theorem comparison and inspected cases

Michel X. Goemans, *Advanced Algorithms*, Lecture 3, 19 September 2001,
scribes Abhinav Kumar and Nodari Sitchinava, distributed in MIT OCW 2008,
[primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/b23096080e3d2142c3c8337bdcd9d3c7_lect9_19.pdf),
Theorems 1 and 3, printed pp.1–2 (PDF pp.2–3): for finite real data,
exactly one of Ax=b,x>=0 and A^T*y>=0,b^T*y<0 holds; the free-variable
inequality version is Ax<=b versus y>=0,A^T*y=0,b^T*y<0. Reinspected
the complete projection proof through its strict-sign conclusion and
the variant's statement. No Slater or full-dimensionality assumption
occurs. OCR corrupts several signs and the final definition of y; use
the preceding definition y=p-b and the nonnegative-variable argument,
as already recorded in foundations/10. No unrelated duality claim is
needed. This alternative supplies no verdict for our particular rows.

MIT 6.854, 2020 compilation, [Notes 11](https://courses.csail.mit.edu/6.854/20/Notes/n11-lp.html),
sections Introduction, Linear Equalities, Basic Feasible Solutions:
reinspected free-variable splitting, slack conversion, Cramer's-rule
rational representation and the full movement-to-a-basic-solution
argument, including degeneracy and the canonical-form lineality caveat.
Apply the basic-solution assertion only after standard-form conversion.
Rational data give rational feasible certificates, and likewise rational
Farkas certificates after normalizing a strict negative pairing to -1
and converting that feasibility problem to standard form. This is a
specialization of the inspected results, not a new rationality theorem.
Do not import that page's informal compactness or general geometry claims.

For a concrete algorithm, Goemans, *An Introduction to Linear Programming*,
October 1994, [MIT primary notes](https://ocw.mit.edu/courses/6-854j-advanced-algorithms-fall-2008/908fe54d659623efadda2d033b895caf_notes_lp.pdf),
The Simplex Method, printed pp.7–8 (PDF pp.8–9): read the reduced-cost
formula, improvement step, exact ratio restriction, optimality test and
degenerate-pivot discussion. The minimal-index rule is attributed to
Bland (1977); its noncycling statement is recorded without importing an
unread original proof or a polynomial pivot bound. The proposed run is
bounded independently of any eventual-termination result.

Giacomo Nannicini and Ebrahim Nasrabadi, MIT 15.053, Spring 2013,
*Recitation 3 solutions*, [primary worked notes](https://ocw.mit.edu/courses/15-053-optimization-methods-in-management-science-spring-2013/05885823def0372adb5eae09c7f5490d_MIT15_053S13_rec03sol.pdf),
Problem 3.A–B, printed/PDF pp.4–6: read surplus/artificial initialization,
the sum-of-artificials Phase I objective and both pivots to the zero
objective. This is a worked algorithm example, not a general termination
theorem. General certificate correctness comes from Farkas and exact
substitution, not this example or a solver's status.

Search queries included `site.math.uwaterloo.ca qsopt_ex exact rational
linear programming feasibility certificate`, `site.csail.mit.edu linear
programming feasibility rational Farkas basic feasible solution`, and
`site.mit.edu simplex phase I artificial variables minimize sum initial
feasible basis lecture pdf`. QSopt_ex and Applegate et al.'s exact-simplex
paper are unread implementation leads only; no installation or dependency
on them is approved. MIT 6.251 Fall 2009 Recitation 4 opened with unusable
text encoding; it supplies no theorem evidence and is unnecessary given
the readable sources above. A failed retrieval is not a source blocker
for this target. No originality inference follows from these searches.

## Why this particular subsystem is covered

L084 writes quadratic right sides before simplification. That notation
alone would not justify an LP or linear Farkas certificate. L085's proof,
"Constancy and multiplier", establishes that each selected cross vector
is constant on t78=s, so its selected slack ell_i is affine in the three
plane parameters and the 45 moments. The step-306 working record saves
the vanishing six quadratic coefficients and the complete affine lift
and reverse. This review imports those existing facts conditionally; it
does not calculate coefficients or strengthen L084/L085. The later run
must stop if reconstruction fails to recover that affine contract.

In the saved reduced coordinates the 21 real variables are the three
plane parameters and 18 equality-free coordinates. Pulling the domain
and sign rows through the existing lift gives the same equality locus,
not a selected slice. Standard-form conversion may split free variables;
it must not silently require those coordinates to be nonnegative.
Singular equalities and a lower-dimensional feasible set are permitted.
No compactness, strict positivity, original-coordinate vertex or rational
SDP feasibility assumption is needed. Original moments use the positive
diagonal conversion p8/V_rq, so their signs are unchanged.

## Approved bounded exact attempt and certificate acceptance

Before any pivot, save all rational original affine rows, row order,
coordinate conversions and the complete saved lift/reverse maps. Verify
their identities, every selected affine coefficient and all six absent
quadratic coefficients. Form exactly the pulled-back 85 domain and 45
moment-sign inequalities on the 21 free coordinates. Keep every row,
including zero or duplicate rows. Convert to rational standard form
using free-variable splitting and slacks, recording every conversion.

Run one exact rational Phase I tableau: orient each standard equality
to nonnegative right side, add one nonnegative artificial variable per
row, initialize with those artificial columns, and minimize their sum.
Use the smallest indexed nonbasic variable with strictly negative
reduced cost; use the exact minimum-ratio test and break ties by the
smallest indexed leaving basic variable. Keep fixed column numbering.
Stop at zero artificial objective, at an exactly verified positive
Phase I optimum, or after 10000 pivots or 300 seconds, whichever occurs
first. These are computational limits, not variable/domain caps. Save
the current tableau, basis and transformation before lengthy work and
at interruption. No warm-start point scan, second run, rounding scheme,
floating conic iteration or alternate weight search is included.

A zero artificial objective is accepted only after lifting the rational
point and checking all 85 domain rows, all 45 signs, all 28 selected
original equalities and their raw-moment forms exactly. Preserve the
kernel/dictionary/anchor contracts listed above. A positive objective
is accepted as exclusion only with an extracted rational separator
checked against the complete original affine inequality system, with
the 28 equalities represented by both orientations (or explicitly free
equality multipliers): nonnegative inequality weights, cancellation of
all 48 original variable coefficients and a strictly negative weighted
right side. Track conversion, elimination and row-sign multipliers all
the way back; a reduced-only certificate or an unverified optimum does
not suffice. Zero pairing is not a contradiction. A budget stop, failed
identity, exceptional pivot or failed original check leaves the subsystem
undecided, with full evidence preserved. Do not treat the pivot limit
as a mathematical infeasibility proof.

These finite checks specialize standard methods because the sources do
not contain this exact matrix. No general theorem needs reproof. A
passing sign/equality witness parks sign-only exclusion; a strict lifted
separator rules out only this fixed family. Neither outcome alone
resolves the 53 other PSD modes, scalar upper rows, other anchors, global
consistency, actual-label restrictions, RS realization or arbitrary-center
safety. The 955–957 bracket stays unchanged.

## Duplicate and failure comparison

ATTEMPTS/052–053 concern a different 24-row fixed-point system: equality
compatibility there coexists with a remaining-mode obstruction. L084 and
ATTEMPTS/066 stop equality-only exclusion here but do not test moment
signs. ATTEMPTS/060–065 preserve individual points and fixed-weight
family tests; none decides all signs plus selected equalities over this
entire plane. ATTEMPTS/067–068 preserve the two stopped joint conic
prescriptions. Their failed candidates and negative individual residuals
are not Farkas certificates and neither imply infeasibility nor supply
a feasible point of this subsystem. This exact LP test is a materially
different necessary-subsystem calculation, not another conic run.

Full matching Mathlib coverage for the combined rational polyhedral
certificate and notebook specialization: not checked. Supporting Farkas,
simplex and rational elimination coverage: not checked. Unknown coverage
is not evidence of absence. This source-only step edits no lemma,
mathematical script, DAG or mathematical argument in PROOF.md.
