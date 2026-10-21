# Proposed free-triple shell feasibility assessment

TARGET: Test whether free triple moments on L054's full distance-five shell can satisfy full anchored PSD and every three-index anchored PSD constraint, with L053's fixed pairs and the same forbidden-distance and full-incidence zeros.
CHECKED: 2026-10-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 176 checked the exact parameter and fixed-distance-distribution/free-triple terminology, compared primary Polak and Schrijver formulations, and read ATTEMPTS/035,036 plus L053/L054's definitions and entry dictionaries; queries and limits are recorded below. No inspected source supplies a verdict for this slice.
SOURCE_EVIDENCE: Freshly inspected Polak arXiv:1703.05171v1 Section 1.1 (1)–(3), Proposition 1.1 and its complete proof, p. 2, and Section 1.2 averaging, p. 3; Brouwer–Polak arXiv:1709.02195v1 Section 2 (1)–(3), pp. 2–3; Schrijver author manuscript III.A (57)–(59) and III.B (60)–(67), pp. 6–7. Reuse foundations/04,09,12 for exact orbit, full product-spectrum and Schur inputs.
COMPARISON: Known union matrices and constraint-preserving averaging cover the proposed finite necessary PSD slice; Schrijver's full two-family block program and Polak's higher-order programs impose further conditions. None supplies feasibility/infeasibility for L053's prescribed pairs with the full-incidence trial zeros. L054 excludes only its fixed product formula.
GAP: Apply the known tools to one consistent global unordered triple assignment: full distance-five anchored PSD at every anchor, and every L053 three-index anchored principal matrix at all three anchor choices. Verify any orbit reduction for this restricted invariant slice, then seek exact feasibility or infeasibility; no verdict or reduction certificate is established in this review.
REASON: Essential comparison for the changed variables and all-anchor scope is complete. Approve one bounded mathematical test of this slice using known methods; its result cannot be imported, and no hierarchy or spectral theorem needs reproof.
SCOPE: Free nonnegative real triple moments globally on the 68-subset universe; L053 singletons/pairs fixed, Boolean repetitions and forbidden-distance/full-incidence zeros retained; all distance-five shells and all anchor-containing three-index principal tests, with no other PSD or scalar conditions added.

Main gap: arbitrary-center safety at 68 agreements; 67 agreements remain
independently unresolved. The intermediate target is feasibility of a
specified finite necessary slice with free triple values, not a uniform
RS bound. A feasible certificate would show that this shell permits a
repair of the failed product assignment; infeasibility would exclude the
whole stated restricted class. Either result would decide whether this
particular slice can discriminate among these pairs and trial zeros.
Neither conclusion by itself proves safety or an unsafe list.

Essential inputs: audited L053 and L054; foundations/04,09,12. The full
incidence zero, including realizable L020 triples, remains a chosen trial
restriction. It cannot be promoted to a necessary zero for every list.
Boolean repetitions must keep lower-order moments; distinguish full-shell
PSD from the three anchored principal matrices of each unordered triple.
Free values must define consistent unordered triple moments. The research
scope and the legitimacy of any symmetry restriction must first be fixed
by source comparison, not inferred from L054's particular invariant trial.
Do not infer feasibility of untested shells or an extension to all moments.

Continuation test for the source review: approve only a precisely delimited
finite feasibility question with inspected essential source coverage, or
identify the exact missing source/hypothesis. Research would require an
exact feasible assignment or exact infeasibility certificate, not numerical
solver status. No free-triple derivation, optimization, candidate or verdict
was performed in step 175. General pair choices, representing measures,
a uniform bound below T=floor(65537^28/2^128)+1, cross-core consistency and
RS realization remain unresolved. Mathlib coverage is not checked.

LITERATURE_REASON: Releasing the fixed product formula and requiring consistency at every anchor changed the assessed scope; this separate literature turn completed the essential applicability and known-result comparison before calculation.

## Completed source review — step 176

The preceding proposal is preserved as the startup target and historical
qualification. Its missing-coverage wording describes the state before
this review. The fields above now approve the same exact TARGET; this
turn performs source comparison only. No free-triple candidate, equation
elimination, optimization, PSD calculation or new lemma was produced.

**Primary statements and essential cases inspected.** Sven C. Polak,
*Semidefinite Programming Bounds for Constant-Weight Codes*, IEEE Trans.
Inform. Theory 65 (2019), 28–38, DOI 10.1109/TIT.2018.2854800;
[arXiv:1703.05171v1](https://arxiv.org/pdf/1703.05171v1), 15 March 2017,
Section 1.1 (1)–(3), Proposition 1.1 and proof, printed p. 2, specifies
union-indexed PSD matrices on the weight-w universe. Its indicator proof
establishes the constant-weight bound despite the displayed A(n,d)
endpoint; retain foundations/12's qualification. The nonnegativity
paragraph following the proof retains lower-cardinality diagonals.
Section 1.2, p. 3, permits averaging because each group image satisfies
the constraints, not just because the ordinary universe is symmetric.
Its Table 2, p. 3, supplies small-parameter higher-order bounds, not this
fixed-pair slice at (1024,10,68).

Andries E. Brouwer and Sven C. Polak, *Uniqueness of codes using
semidefinite programming*,
[arXiv:1709.02195v1](https://arxiv.org/pdf/1709.02195v1), 7 September 2017,
Section 2 (1), printed p. 2, explicitly has nonnegative coordinates.
The following averaging discussion and (2)–(3), pp. 2–3, describe orbit
variables, affine PSD coefficient matrices and exact primal/dual
identities. They do not certify a numerical solver output for our slice;
their optimal-code uniqueness conclusions are not used.

Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE Trans. Inform. Theory 51 (2005),
2859–2866, DOI 10.1109/TIT.2005.851748;
[eight-page author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.A (57)–(59), printed pp. 6–7, includes the complete extension/reset
proof for the equal-weight block restriction. III.B (60)–(67), p. 7,
uses free triple coefficients, both included/excluded-anchor PSD
families and extra scalar inequalities. Its permutation condition (65)
preserves t-s, as explained using symmetric differences after (65);
three pair distances alone do not identify a triple orbit. This stronger
program is a comparison, not an equivalent formulation of our weaker
retained slice. The qualified prefactor in (61) remains unused.

**Reused spectral coverage.** The exact inspected statements, hypotheses
and proof cases in foundations/09 are reused without another search:
Brouwer–Cioaba–Ihringer–McGinnis,
[arXiv:1709.09011v2](https://arxiv.org/pdf/1709.09011v2), Sections 1.2, 3
and 3.4, pp. 3,10,12; Brouwer–Haemers, *Spectra of Graphs*,
[author preprint](https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf),
Sections 1.4.7 and 11.2, pp. 19,162–163, and Theorem 2.7.1(i), p. 36.
Both factors (68,5) and (956,5) meet the Johnson n>=2d hypothesis.
Coverage includes every factor eigenspace, identity relations, the
constant projector and singular lower blocks with a positive leading
scalar. Changing coefficients does not change those theorem hypotheses.
Research must verify the new entries and all spectral signs; no spectrum
of free coefficients is derived here.

## Exact approved finite question and specialization obligations

Keep L053's x(empty), singleton rho and all distinct-pair rho*p_i values,
including its augmented pair PSD certificate. Seek a single nonnegative
real function on unordered support families of size at most three. For
distinct triples, retain the prescribed pair-forbidden zeros and the
entire L020 incidence zero (common 61, pair-only two each, private three
each); free every other triple value. Boolean unions with repetitions
have their fixed lower-order values. The objective stays M=(U+1)/2;
this is a feasibility question at fixed pairs, not maximization.

For each A, require the entire union matrix indexed by {A} and {A,B}
for every B at half-distance five to A to be PSD. Also require every
L053 principal matrix indexed by {A},{A,B},{A,C}, with duplicate indices
removed, for all A,B,C. For a distinct unordered triple the same value
must be used at all three choices of anchor. Matrices involving B,C
outside a particular distance-five shell still belong to the principal
batch. A shell-only solution with no global continuation is insufficient.
Conversely an infeasibility verdict cannot silently fix off-shell free
coordinates to the old product formula.

Import the source union-matrix definition rather than redeveloping the
hierarchy. L053 and L054 already justify the support and shell indices.
Research must verify that the chosen free-coordinate representation uses
those definitions and lower-order entries exactly. Do not add full
conditioned matrices outside the distance-five shells, anchor-free
three-index tests, complement matrices, Frechet inequalities or
four-support moments. Such additions would test a different target.

The full-incidence restriction is set-incidence based, whereas L020's
nonsingularity-only restriction depends on actual subgroup labels. This
difference is essential when applying Polak's constraint-preserving
averaging argument. The approved research includes explicitly checking
that the fixed coordinates, both kinds of zeros and the complete families
of retained matrices are preserved by coordinate permutations, and that
unordered support permutations are represented consistently. Only after
that check may an infeasibility proof use an invariant reduction for this
restricted slice. An invariant feasible witness may instead be checked
directly on all relevant entries. Neither option licenses averaging the
general labeled RS program. Use foundations/04's actual orbit ranges
and the full support-permutation identification; no distance-only
identification or independent per-anchor variable is preapproved.

L054 already identifies its shell with J(68,5) x J(956,5), all 36 product
relations, Boolean diagonal p_5, anchor row p_5 and the single incidence
override (r,q)=(2,3). Those are reusable dictionaries. The old nonzero
product coefficients are released here. Necessary finite specialization
and exact verification justify research; reproof of any imported spectral
or hierarchy theorem does not.

## Search, duplicates, decision and limits

Queries on 12 October 2026: `constant weight code SDP fixed distance
distribution triple variables Schrijver A3 Polak`; `constant weight codes
three point semidefinite programming Johnson scheme prescribed distance
distribution feasibility`; `"A(1024,10,68)" semidefinite`; `"Schrijver"
"fixed" "distance distribution" semidefinite constant weight`; and
`"constant weight" "triple" "prescribed" semidefinite feasibility`.
The exact-parameter search returned no matching result. Broader searches
returned the primary formulations inspected above, strengthened/split
SDP leads and unrelated hits. The split-Terwilliger and other search-only
leads remain unread and are not theorem evidence or an essential input
for this finite slice. No failed search establishes novelty.

Read L053's hypotheses, trial definition, Boolean/orbit discussion and
principal-PSD proof, and L054's hypotheses and full entry dictionary.
Reuse their separately audited conclusions. ATTEMPTS/035 stops precisely
the small-principal batch as a threshold certificate; ATTEMPTS/036 stops
precisely the fixed product formula for full-shell feasibility. The prior
fixed-shell and unrestricted-small-principal assessments do not approve
free coefficients. The source comparison now fills that scope gap, but
does not alter either mathematical stop. L051/L052's different prescribed
pairs and L023/L024's unchanged block formulas are not substituted here.

Continuation test: perform one bounded search for an exact feasible
global assignment or an exact infeasibility proof for this slice, with
complete unordered-orbit consistency, all anchor choices and all shell
modes checked. Numerical candidates may guide certificate construction;
solver status or a spectral preview alone is not a verdict. If neither
certificate is obtained, save the unresolved constraints and report
EXPLORATION honestly; if a candidate fails, preserve the exact offending
constraint. A verdict decides whether this restricted slice can repair
L054's failure at the prescribed pairs. Neither verdict gives a uniform
bound, an unsafe RS list or a boundary improvement. Retain the 955–957
bracket, independent 67-agreement gap, arbitrary pair choices, untested
shells, representing measures and common-center realization as open.
Full matching Mathlib coverage remains not checked.
