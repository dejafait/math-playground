# Actual-theta coefficient weight — completed overlap comparison

TARGET: Review whether Romik (3.3)'s exact coefficient multiplier makes the weighted degree-six two-atom outward-flow test distinct from L530 and applicable as an actual-theta discriminator.
CHECKED: 2026-10-30
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the direct-theta discovery, sixth-degree moment-flow assessment and independently audited L530; searched their specific local coefficient/weight/failure passages. External queries for Romik/Pollaczek coefficient hyperbolicity, Meixner-Pollaczek Hausdorff multipliers and Riemann/Pollaczek moment preservation supplied no inspected stronger theorem; primary (3.3) itself resolves the purported changed multiplier.
SOURCE_EVIDENCE: Read Romik arXiv:1902.06330v3 (5 May 2019), https://arxiv.org/html/1902.06330v3 , (1.7)/(1.9), (2.5)-(2.6), (3.1)-(3.7), Theorem 3.1's final convergence argument, Theorem 3.6 with its generating-function/change-of-variable proof, (3.25)-(3.26), and (A.21)-(A.30). Reused the prior reading of Theorem 3.8/Proposition 3.9; no manuscript audit is claimed.
COMPARISON: Equation (3.3) contains a fixed positive integration weight and constant 4sqrt(2), with no degree-dependent coefficient multiplier. Its normalized coefficients are moments in precisely the basis convention used in L530. A two-atom replacement under the original [0,1] domain repeats that family; it does not specify the actual theta measure.
GAP: No distinct weighted finite discriminator is supplied by (3.3). A proved theta-specific restriction, initial hyperbolicity, all-degree control, stability and Xi transfer remain missing. L530 is not transferred to the actual theta measure or to a narrower smooth/open-support subclass.
REASON: Import the precise source identity to correct the proposed changed-hypothesis premise and park this duplicate retest. This is informative source-overlap evidence, not a new lemma, source reproof, or new root-loss certificate.
SCOPE: Completed literature comparison only; IMPORT covers this normalization/overlap decision, not any additional preservation or realization claim.
LITERATURE_REASON: The saved REVIEW_REQUIRED target alleged an essential changed coefficient hypothesis; the primary formula had to be compared before any weighted calculation. That comparison is now complete and does not justify further dependent browsing.

## Original review and decision test (preserved)

Main gap: actual-Xi all-degree mixed positivity. Essential local input:
L530 only for its exact obstruction and hypotheses; L018/L024 and
L030-L032/C032a identify the eventual goal, not a positivity premise.
No cross-notebook or zero-free input is needed.

Reuse `2026-10-30-direct-theta-mixed-positivity-discovery.md`,
`2026-10-30-pollaczek-moment-flow-sixth-degree.md` and the completed
L530 audit. Retrieve only the primary coefficient formula and its
normalization, reflection and integrability hypotheses first. Compare
the actual even coefficients with the unweighted moments in L530,
including the degree-dependent factor; do not silently identify them.
Check exact/stronger weighted preservation results and overlap with
L530 before nominating a calculation. Source formulas should be
imported by precise citation, with only the applicability justification.

Continue to a separate mathematical target only if the exact weighted
family is specified, is distinct from the disproved family after all
admissible reparametrizations, and supports a bounded root-loss or
preservation discriminator with a plausible actual-theta use. Record
whether L530 already transfers by a known theorem. If the same
obstruction covers it, or no independent discriminator is justified,
record that evidence and park this dependent route. A missing source
is not permission to invent the coefficient restriction. Do not infer
initial actual-theta hyperbolicity, or approve and execute previously
uncovered mathematics in this review.

The 10,000-tuple sample is exhausted and remains preserved; no sampling
is nominated. This review does not renew the old exploration budget.
A creative central mechanism is not yet justified: an actual-theta
restriction and initial hyperbolicity are missing. The review tests
whether the precise source weight supplies a distinct intermediate
question before further mathematical work. Mathlib matching is not
checked, not known absent.

## Completed source comparison — 30 October 2026

The intermediate target was to identify a distinct coefficient family,
not to prove a new positivity statement. The decisive source check is
Romik (3.3), in the normalization of (A.21)/(A.27):

    c_(2j) = 4sqrt(2) integral_[1,infinity)
             omega(x)/(x+1)^(3/2) * ((x-1)/(x+1))^(2j) dx.

For the applicability comparison only, put h(x)=((x-1)/(x+1))^2
and let nu be the finite measure with density
4sqrt(2) omega(x)/(x+1)^(3/2) on [1,infinity). Then (3.3) says
exactly c_(2j)=integral h^j dnu. Positivity, the reflection identity
and absolute convergence are supplied by (1.7)/(1.9), (2.5)-(2.6)
and (3.1)-(3.3). The mass is c_0>0; normalization gives the probability
measure mu=h_*(nu/c_0) and moments c_(2j)/c_0. Here 0<=h(x)<1.
This is a definition of the pushforward in the cited integral,
not a new moment representation theorem or a quadrature reduction.

Thus the degree-six truncation, divided by c_0, has exactly the
alternating moment-coefficient form used in the earlier assessment.
There is no extra sequence a_j multiplying these moments. Replacing
mu by an arbitrary two-atom probability measure on the originally
proposed closed [0,1] domain yields the old finite test. Multiplication
by the positive constant c_0 changes no zeros. L530 already obstructs
that general implication, with its original endpoint atoms and precise
hypotheses. No new algebraic calculation is needed or approved here.

Two nearby normalizations do contain degree factors: (A.22) defines
f_n using (3/2)_n/n!, while (3.7) is an inversion integral with
n!/(3/2)_n. Neither is an extra multiplier in (3.3)/(3.4).
The actual density depends on x, not on j. Theorem 3.6's
0<r<1 representation and finite diagonal formula (3.26) do not
introduce a different coefficient multiplier. Import these identities
by the citations above; no reproof of the expansion is justified.

The actual measure is a particular non-atomic measure, not L530's
two-atom witness. The source comparison does not license identifying
their root behavior. In particular the witness atom at 1 is outside
h([1,infinity)); no claim of transfer to open-support, continuous,
smooth, or actual-theta measures is made. If any of these restrictions
is proposed later, it must have an independent relevance test and
coverage; this review approves neither a perturbation argument nor
another sample. Merely weighting before pushing forward is not the
missing theta-specific restriction.

The prior source warning (Proposition 3.9) remains only the previously
qualified non-even example; no stronger certified subclass theorem
was imported. Queries were `"Romik" "Pollaczek" "coefficient"
"hyperbolicity"`, `"Meixner-Pollaczek" "Hausdorff" "multiplier"`,
and `"Riemann" "Pollaczek" "moment" "preservation"`. Search-only
secondary frontier maps and unrelated quadrature/Markov references
were not treated as evidence. No absence or novelty claim follows.
The separate Hahn formula (5.1) was located while checking nearby
degree factors; it concerns a different basis and is not adopted or
assessed as a continuation here. Mathlib matching remains unchecked.

Decision test: a nonconstant coefficient multiplier or a proved
additional restriction was required to justify this weighted retest.
The exact cited formula supplies neither. Park the retest, preserve
L530 and the exhausted sample, and retain the actual-Xi gap. Outcome
NEGATIVE records a corrected source premise and a changed route,
not progress beyond the checked source or a disproof of actual flow.
