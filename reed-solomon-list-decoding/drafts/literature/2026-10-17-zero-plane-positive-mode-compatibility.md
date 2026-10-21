# Positive-weight mode equalities on the necessary zero plane — approved scope

TARGET: Derive the exact signed compatibility conditions for L082's 28 positive-weight mode equalities on L083's zero plane, retaining L076's original domain.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 295 searched exact linear-system compatibility, left-nullspace solvability, polynomial right-side systems and zero-dual facial reduction; compared L070, ATTEMPTS/052–053 and 060–065, and the ready consistency and L083-audit assessments. Freshly inspected Garloff–Popova–Smith's primary preprint Sections 1–2.2 and Section 3.1 Theorem 1; no matching finite-system verdict was found, with no novelty inference.
SOURCE_EVIDENCE: Reuse foundations/10's inspected Ye October 2017 Section 2.3 opening p.42, Theorem 1.11 p.13 and Section 1.5.1 pp.23–24, and the L083-audit assessment's inspected Schrijver, Sano, Polak and Goemans passages. Fresh Garloff–Popova–Smith comparison: author-hosted 18-page preprint, Section 1 (1)–(2), Section 2.2 (3)–(4), and complete Section 3.1 Theorem 1 plus ensuing qualification, pp.5–6. Exact references and access limits below.
COMPARISON: Scalar complementarity and the equality alternative already cover the general method, including signed variables and arbitrary real right sides evaluated at fixed parameters; no new parametric solvability theorem is needed. Neither source supplies this 28-by-45 matrix's full left nullspace or compatibility on the original domain. Interval enclosure and free-entry completion results do not replace that finite calculation; L070's 24-row fixed-point pass is different.
GAP: Compute only the original 28-row system's exact left-nullspace compatibility on t78=s, with all three remaining parameters and all 85 domain inequalities retained; its rank, compatibility polynomials, domain intersection and solution parametrization remain uncomputed.
REASON: Separate source review now covers the proposed finite specialization without re-proving the general theorems; only the exact saved target is ready for a later research turn.
SCOPE: Equality-only compatibility for L082's unchanged 28 positive-weight rows, 45 signed scaled moments and L076's whole original domain restricted by L083's t78=s; no extra separator, sign assumption, remaining-inequality search or changed base/pairs.

The main gap remains arbitrary-center safety at 67/68 agreements. The
proposed intermediate target is a complete original-coordinate description
of when the 28 positive-weight mode equations can hold on the necessary
plane. Its potential use is either an obstruction to completion or a
sound equality reduction before testing the remaining mode inequalities.
No rank, compatibility equation, automatic consistency or feasible point
for this new system is asserted here.

The approved later bounded test must keep the
45 original scaled real free variables and substitute only t78=s into
the already audited 81 bound quadratics. The original 85 domain rows
remain inequalities in the other three parameters; do not replace them
by only endpoint conditions or a new parametrized subfamily. Determine
the exact compatibility conditions of the 28 selected equations using
all their original rows, with a complete rational certificate. Do not
search for a different separator, add nonnegative-moment assumptions or
infer the remaining inequalities from this equality calculation.

Continuation/abandonment test: a nontrivial compatibility condition is
useful only if its relationship to the original domain is explicit.
If every compatibility condition is already forced by L083's aggregate
identity, park equality-only exclusion and retain the reduction solely
as an input to a separately assessed remaining-inequality test. An
inconclusive reduction must record the actual unresolved conditions;
it is not an infeasibility certificate. This full-plane test is distinct
from another isolated-column optimization. Independent gaps remain:
nonnegative entries, the other mode inequalities, scalar upper rows,
other anchors, global consistency, other pair/base choices and RS
realization.

Essential inputs: L021,L053,L073,L075,L076,L078,L079,L081,L082,L083 and
foundations/09,10 with foundations/04,12 qualifications. Use the complete
step-290,292,294 certificates and their canonical upstream recipes.
Preserve original rho,p8,pairs, the seven-column RREF/completion, all
500 types/3000 presentations, 36 forced/45 free moments, 90 weighted
kernel equations, singular/empty ranges and the full anchor. Ancestral
PSD, uniqueness and whole-kernel contracts remain qualified imports.
Retain all fixed-point rejections and ATTEMPTS/060–065. General matching
and supporting Mathlib coverage is not checked; unknown is not absence.

Step 294 proposed this continuation without approving it. Step 295
supplies the separate literature approval. No new lemma, equality-system
calculation, rank or compatibility result is claimed by this review.

## Precise imports, comparison and access

Reuse Yinyu Ye, *Conic Linear Programming*, December 2004, revised
October 2017, [Stanford monograph](https://web.stanford.edu/class/msande310/sdpmain.pdf):
Section 2.3 opening, printed p.42 (PDF p.55), gives scalar nonnegative
zero-product complementarity. It needs neither Slater nor optimality.
Theorem 1.11, printed p.13 (PDF p.26), states that Ax=b is solvable
exactly when no y has A^T y=0 and b^T y=1; the source states it without
proof. Section 1.5.1, printed pp.23–24 (PDF pp.36–37), describes pivoting
and back substitution. These previously inspected passages are canonical
in foundations/10 and were also assessed for L070. Their hypotheses do
not constrain the right side to be parameter-independent. Apply the
alternative separately at each real parameter value, using one complete
exact rational row reduction of the constant coefficient matrix. No
general theorem needs reproof. The later finite calculation must supply
and verify the complete left-nullspace certificate and all original-row
substitutions; the single already known weighted dependence cannot be
assumed to exhaust that space.

Fresh Ye access returned PDF metadata/text initially, but targeted text
and all four selected-page screenshots failed or timed out. No fresh
page inspection is claimed. The adequate recorded inspection is reused;
this nonessential access failure does not invalidate that coverage or
require another access-only turn.

Freshly read Jürgen Garloff, Evgenija D. Popova and Andrew P. Smith,
*Solving Linear Systems with Polynomial Parameter Dependency with
Application to the Verified Solution of Problems in Structural Mechanics*,
[author-hosted preprint](https://www.math.bas.bg/~epopova/papers/13-GarloffEtAl-preprint.pdf),
18 pages, retrieved 2026-10-17 (no dated version asserted): Section 1,
pp.1–2, (1)–(2), Section 2.2, pp.3–4, (3)–(4), and Section 3.1,
pp.5–6, complete Theorem 1 and ensuing regularity qualification. Its
systems are square over a parameter box. Under its interval
Gauss–Seidel inclusion hypotheses it proves regularity and encloses
the unique solution for every parameter value. It is not an exact
compatibility theorem for this rectangular 28-by-45 system. Section 2.2
also explicitly warns that replacing dependent parameters by independent
interval entries enlarges the solution set. No enclosure calculation,
regularity premise or interval replacement is imported. Its statement is
given without a proof there, with references to inclusion theory; those
references remain unread and are unnecessary for the rejected application.

Reused upstream coverage remains exactly the ready L083 critical-audit
assessment: Schrijver, DOI 10.1109/TIT.2005.851748, Proposition 5
(44)–(47), Theorem 1 (51), III.A (52)–(59), III.B (64); Sano,
DOI 10.1007/s44146-026-00231-y, Section 2, Corollary 2.2, Theorem 2.6
and Lemma 2.7; Polak arXiv:1703.05171v1 Sections 1.1–1.2; Goemans,
19 September 2001 MIT Lecture 3, Theorems 1 and 3, pp.1–2.
These supply the existing mixed-layer, singular-range, moment and signed
separation contracts with all foundations/04,09,10,12 qualifications.
Their inspected proof cases are reused, not freshly checked. In
particular keep both rectangular orientations, the coherent positive
congruence, the full anchor, and the singular/empty old-layer cases.
No representing measure or new labeled symmetry is assumed.

Reuse foundations/10's Grone–Johnson–Sá–Wolkowicz, LAA 58 (1984),
109–124, Proposition 2 and Theorem 7 comparison: unrestricted free-entry
completion and chordality do not impose this shared moment dictionary.
No chordality premise has been established here. Broader facial-reduction
search leads and general parametric algorithms were not imported; they
do not supply the desired finite coefficients. Search snippets are leads,
not theorem evidence. Full matching and supporting Mathlib coverage
remains not checked; unknown is not absence.

## Exact research contract and stopping test

Retain L082/L083's orientation A_mode*z<=b(t). Select the rows by the
strictly positive entries of the unchanged canonical weight vector, not
by a new optimizer or a guessed rectangular index set. The forthcoming
calculation must reconstruct all 28 original rows, their 45-column
order and positive scaling, the bound quadratics and original/raw moment
translations. Preserve the family-wide range identities and full-key
checks as imported inputs with their existing qualifications; this source
review does not audit their certificates again.

Substitute only the exact s from L083 into t78. Keep t56,t63,t69 free
and keep every original domain row. Use exact constant-matrix elimination
to obtain all compatibility conditions, with an invertible row-operation
certificate and exhaustive original-row residuals. In the later report,
state explicitly whether the resulting conditions are identities on the
plane or further restrictions, and describe their intersection with the
original domain only as far as rigorously established. A numerical rank,
a few sampled points, or the existing aggregate dependence is insufficient.
No rank, automatic consistency or nonempty equality locus is predicted.

This equality calculation may be useful without deciding the remaining
constraints. If it adds no restriction beyond the plane, stop equality-only
exclusion and preserve the exact reduction for a separately assessed
remaining-inequality target. If a further condition appears, continue only
with its certified relationship to the full domain; an unresolved domain
intersection is not infeasibility. Do not infer nonnegative moments,
other-anchor PSD, global consistency, RS realization or a boundary change.

Search queries used: “linear equations compatibility left nullspace
polynomial right hand side exact Gaussian elimination”; “semidefinite
programming zero dual certificate positive weights equality facial
reduction”; “\"left nullspace\" \"solvable\" site:edu linear”;
“\"parametric\" \"linear systems\" \"polynomial\" \"right-hand\" compatibility”;
and “\"Reed\" \"Schrijver\" \"zero\" \"completion\" \"positive\"”.
No matching specialized result was identified; this does not establish
novelty. Local searches compared the named assessments, L070, L082,
L083 and ATTEMPTS/052–053,060–065. In particular L071's later rejection
of L070's fixed equality-consistent point shows why equality consistency
must not be promoted to completion. L083's old fixed-weight stop remains.

Step 295 is LITERATURE / REPRODUCTION, outcome EXPLORATION: new scope
comparison completed, with no mathematical advance or source-level
discovery. The target is now ready; no essential source blocker remains.
Mathematical exploration usage stays 0/3. No lemma, mathematical script,
PROOF.md or DAG.md was changed.
