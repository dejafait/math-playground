# Overlap/disjoint quadratic-fiber restriction — approved critical audit scope

TARGET: Critically audit L047's overlap/disjoint quadratic-fiber restriction, including its uses of L045–L046 and the full-weight union-six consequence.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the completed simultaneous-recovery searches and recurrence/MDS assessments; two narrow coupling queries on 2026-10-08 found no inspected matching import; read L045–L047 in full, L043's gates and relevant L010 kernel/count passages, and ATTEMPTS/022.
SOURCE_EVIDENCE: Freshly inspected Hall, Notes on Coding Theory, section 5.1 definition, Theorem 5.1.1 and full proof, printed pp. 63–64; reused inspected Chojecki v9.2 DR2 and DR6–DRC, source lines 2785–2935, and Marquez-Corbella–Pellikaan (2016) section 5 through the saved primary extracts identified below.
COMPARISON: Primary coverage supplies arbitrary-field MDS distance and fixed-support full-moment membership, not L047's simultaneous quadratic coupling; the completed counting review gives no matching bound, and neither L043's audit nor reading L045–L046 certifies their use here.
GAP: Independently audit the conditional fiber restriction and union-six consequence with essential L045–L046 cases; eleven, both twelve profiles, universal extraction, other patterns and ABF26 identification remain unresolved.
REASON: The changed audit scope has adequate ingredient coverage and no identified matching theorem import; approve one bounded POTENTIALLY_NEW proof audit on the exact TARGET without certifying its claims or originality.
SCOPE: Exact TARGET only: F=F_(97^20), H order sixteen in F_97, k=8, pinned cell, gated tau=1 pattern (2,2,3), arbitrary extension-field weights and distinct original finite parameters, L043 (4)–(7) before weight gate (9), an actual B-disjoint witness for L047's coupling, and full weights and both universal finite-lift gates only where explicitly required.
LITERATURE_REASON: The target changes from constructing a simultaneous-count restriction to critically auditing L047 and its essential unaudited L045–L046 uses; this separate review checks coverage for that previously unapproved audit target.

## Gap, intermediate target and decision test

The main local gap remains the uniform eleven-candidate bound and, more
broadly, exclusion or realization of L010's arbitrary sixteen-error
equality. The intermediate target is the exact TARGET above: a separate
audit of L047 including its essential unaudited input uses. A sound
conditional extraction could route a genuine disjoint/overlap configuration
to the union-six branch. It would not supply a disjoint candidate, exclude
the small-intersection alternative or certify L040's candidate bound.

Coverage continuation test: all essential theorem hypotheses must fit
the unchanged local domain, with the simultaneous claims left for direct
audit. That test is met by the existing ingredient assessments and the
scope comparison below; no essential new source is missing. Mathematical
continuation test for the next turn: check every load-bearing identity and
case under the stated gates, then retain the restriction only if no defect
is found or a defect is repaired explicitly. If a load-bearing assertion
fails under these hypotheses, record it and stop downstream use of that
assertion; do not narrow to rational weights to conceal the failure.

## Precise primary coverage and applicability

J. I. Hall, *Notes on Coding Theory*, undated 13-page
[author-hosted GRS chapter](https://users.math.msu.edu/users/halljo/classes/codenotes/GRS.pdf),
section 5.1 definition, Theorem 5.1.1 and complete proof, printed
pp. 63–64, freshly inspected 2026-10-08. Over a field, distinct evaluation
points and nonzero multipliers give a dimension-k GRS code of distance
n-k+1 for positive k. The proof treats injective evaluation and its root
bound, with an explicit root-product attaining the distance. Here n=16,
k=8, H distinct and unit multipliers satisfy the hypotheses over F.
Reuse this citation for distance nine; it imposes no prime-field condition
on words. This is the already recorded specialization, not a new lemma.

Przemek Chojecki, *Shortening Bounds for Reed–Solomon MCA*,
[live author TeX v9.2](https://raw.githubusercontent.com/przchojecki/rs-mca/main/RS_MCA_Paving_v9.2.tex),
dated July 17, 2026, source lines 2785–2935, exact anchors
`drc:lem-locator-recurrence` (DR2) and `drc:thm-exact-compiler`
(DR6–DRC). Reuse the inspected full-hypothesis/proof-case extracts in
`2026-10-08-nine-union-fourth-support-incidence.md`, “Primary recurrence
input and applicability”, and
`2026-10-08-nine-union-fourth-support-critical-audit-scope.md`,
“Primary source comparison and applicability”. No fresh author-source
retrieval is claimed; the mutable file is not certified identical to
ePrint 2026/1463.

Those inspected results use distinct weighted Vandermonde columns with
nonzero multipliers, redundancy R and support size t<R. DR2 identifies
support-span membership by the R-t recurrences; its annihilator proof
uses support-polynomial multiples and MDS rank. The compiler handles
nonzero projected directions by proportionality and a pivot, and zero
directions by the empty/common intersection cases. Here the saved
substitution is R=8,t=4,a=12, with shifted moments and nonzero multipliers
x. Arbitrary syndrome coefficients over F are allowed. Quotient-zero
systems still require L043's actual shared-column lift; the source does
not certify recovered weights or a simultaneous count. No decoder or
recurrence reproof is needed in the audit.

I. Marquez-Corbella and R. Pellikaan, *A characterization of MDS codes
that have an error correcting pair*, FFAA 40 (2016), 224–245,
[DOI 10.1016/j.ffa.2016.04.004](https://doi.org/10.1016/j.ffa.2016.04.004),
[accepted manuscript dated 2016-02-29](https://pure.tue.nl/ws/files/93073933/16_02_29_ECP_MDS.pdf),
section 5, Definitions 5.1–5.2, Lemma 5.3 and following unnumbered
single-coordinate GRS shortening formula, printed pp. 7–8. Reuse the
inspected extract in `2026-10-07-six-coordinate-triple-equality-obstruction.md`,
“Primary shortening input”. L041's already audited shortening retains
distinct finite labels, positive dimensions and nonzero difference
multipliers. It is an upstream local input, not a new shortening argument
or a source for the fiber restriction. No broader characterization
theorem is being imported.

## Duplicates, discovery and recorded failures

Reuse `2026-10-08-nine-union-simultaneous-recovery-count.md` in full:
its inspected Guruswami–Kopparty Theorem 14/Claims 15–16 require structured
disjoint blocks; its Goyal–Guruswami–Sun–Wootters Theorem 3.27(1) requires
an established design inequality, and Theorem 5.6 uses random evaluation
points. These are not imports for fixed H or the relaxed systems. The
fixed-label L016 count and L043's individual-support audit do not cover
L047's simultaneous assertions. No stronger matching conclusion was
established by that bounded discovery.

Two fresh scope-specific queries were issued:
`"Reed-Solomon" "quadratic" "disjoint" "mutual correlated agreement"`
and `"Shortening Bounds for Reed" "fiber"`. Returned metadata included
an author-repository overview and broader proximity/decoding papers;
these hits were not inspected theorem coverage and supply no premise.
No exact coupling theorem was established by these queries. Failed
searches do not establish novelty. ABF26, Jo26 and the saved nonessential
campaign/ePrint blockers remain parked; none is needed to audit this
model-only conditional argument.

ATTEMPTS/022 was read in full: isolated cubic degrees only reproduce
coordinate capacities and permit both twelve profiles. The proposed
audit examines simultaneous equations rather than reopening that stop.
The earlier incidence-only and sampling stops compared in the completed
counting assessment remain preserved. No cross-notebook result is used.

## Ready bounded audit and qualifications

Use L010 and L041 with audited L042–L043; critically check the uses of
unaudited L045–L046 within L047. L044 is not an essential input and L040
must not be used to turn conditional extraction into a profile exclusion.
L046 supplies distinct outside triples and the opposite-singleton-tag
restriction on repeated pairs; its h/d application is load-bearing.
L045 supplies only the stated twelve-profile application and its weight
and coordinate multiplicities. Reading their proofs here supplies scope
comparison, not separate correctness certification.

The audit must check the all-eight-moment lift with zero recovered
weights, disjoint factorization, descent of ell alone, cancellation
identities, the intersection-three obstruction, and both degrees of ell.
Retain the constant case, possible double roots, nonzero polynomial and
denominator arguments, uniqueness of eta/c, and distinct-parameter
counting even with multiple witnesses. Check L046's coincident outside
triple cases and two-tag cancellation before using its pair restriction.
Then check the full-weight affine-word consequence, five h-root
contradiction, L045's lower-weight exclusion and the two separate
universal finite-lift gates. Do not assume rational rho or original chart,
an actual disjoint witness outside L047's conditional hypothesis, or any
global equality outside the explicit L045 equality application.

Approve one POTENTIALLY_NEW proof audit on the unchanged TARGET. This
classification preserves the prior bounded-search status; it is not a
novelty certification. The completed literature turn derives no new
mathematics, runs no mathematical script, modifies no lemma, and makes
no audit verdict. Exact Mathlib coverage and supporting declarations
remain not checked; no absence or formalization claim is made.
