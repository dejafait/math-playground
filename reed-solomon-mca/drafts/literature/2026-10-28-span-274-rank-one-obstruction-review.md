# Span 274 — completed gate-aware source comparison

TARGET: Assess whether the saved span-274 kernel can exclude history (0,51,98,177,318) through Plücker decomposability and L109's exact-rank-one row gates over the algebraic closure, without new block-rank tests.
CHECKED: 2026-10-28
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 541 searched the exact history/span strings in notebook lemmas, drafts, ATTEMPTS and history; compared L109/L154/L158/L162–L165 and ATTEMPTS/048–049/052–053; issued the five exact external queries recorded below. No completed named-history locus test was located; no novelty follows.
SOURCE_EVIDENCE: Reuse the October 25 gated-feasibility and October 26 full-locus assessments below, including Gao–Platzer–Clarke CAI 2011 Theorem 4.1/Lemmas 4.1–4.2 https://symbolaris.com/pub/QEfin.pdf ; freshly inspect Stacks Lemma 27.22.1 https://stacks.math.columbia.edu/tag/089T , Lemmas 15.8.4(3)/15.8.7 https://stacks.math.columbia.edu/tag/07ZA and https://stacks.math.columbia.edu/tag/07ZC , and Theorem 10.34.1 https://stacks.math.columbia.edu/tag/00FV , statements and relevant complete proof cases, live 2026-10-28.
COMPARISON: Known arbitrary-field chart, minors, nonzero-atom and Nullstellensatz methods cover a bounded exact specialization to the saved kernel; they do not determine this history's locus. L154's field equations and pair-specific parametrizations are not transferred. Use a complete chart/open cover rather than an unverified saturation shortcut.
GAP: The saved span-274 kernel's actual decomposable exact-rank-one locus is still uncomputed. A later attempt must bind the complete saved kernel and prove either emptiness on every chart/open branch or an exact surviving point/component; no exclusion is supplied by this review.
REASON: Essential method coverage is adequate and no duplicate was found in the scoped search. One bounded specialization is justified, without new block-rank tests, solver guarantees, traversal or a coding converse; the new ready continuation needs separate approval next turn.
LITERATURE_REASON: The incoming target is REVIEW_REQUIRED and changes from rank/incidence domination and finite-field encoding to one algebraic-closure geometric locus; reuse adequate method coverage while resolving that scope change.
SCOPE: Source comparison only for L109's original S/J/maps, node 1006, complete history (0,51,98,177,318), saved span 274, and planes over the algebraic closure of F_97 with all five selected ranks exactly one. No geometric calculation, new lemma, script write, new block-rank test or broader cover is performed.

## Completed comparison — step 541

The main gap remains uniform twelve-row exclusion for an unspecified
pair. The intermediate target is emptiness of the necessary geometric
locus at this one saved five-row history. An empty locus could eliminate
descendants containing this history; a survivor would stop this empty-locus
route, without proving coding feasibility. Other branches, arbitrary
representation and identification with the challenge remain independent
gaps. The frozen radius interval is unchanged.

### Local inputs, duplicates and failures

Read L109's original Q/N definitions, nonzero-wedge reduction, complete
Plücker reconstruction, rank-zero exclusion and recovery qualifications.
Its linear/exterior identities hold over every extension of F_97.
Necessity of exact rank one for actual events uses the stated polynomial
nonpersistence hypotheses; full weights and the original finite chart
are additional gates, deliberately absent from this weaker test.

Read L154's hypothesis/encoding passage and certificate criterion. Its
282-variable finite-field formula solves no instance. Neither its pair
registry nor its X^(97^20)-X equations is an input to the proposed
algebraic-closure test. The useful reusable template is its complete
nonzero-Plücker chart cover and explicit nonzero witnesses.

Read the full L158 locus argument and statement/method ranges of
L162–L165, together with ATTEMPTS/048–049/052–053. These concern other
explicit labels. L158's two-point/empty conclusions, L163's forty-row
mask and L165's full-locus identification do not transfer to this seed.
L162 rules out universal four-row finiteness. Rank-only stratification,
encoding-size repetition and another attempt at unconditional finiteness
remain stopped. The target instead tests an omitted necessary gate on
an existing branch, using its saved complete kernel. This is a local
specialization of an established method, not a new general mechanism.

The exact-string local search matched only the intake, step-540 records
and L170's occurrence comparison. The step-540 history explicitly says
the geometry was not evaluated. No equality-of-span symmetry or L170
completion-transport theorem is needed here. Reused kernel provenance is
the pair-free result record's full independent reconstruction of all 524
saved span kernels, backed by `scripts/pair-free-envelope/verification.json`;
the verifier's complete-kernel/minor checks were inspected as source
provenance, not rerun. A later attempt must inspect the complete selected
node/span records and bind the actual history to that kernel. This turn
does not certify a kernel dimension, coefficient or geometric property.

### Primary inputs and correct scope

Reuse `2026-10-25-twelve-row-gated-feasibility-review.md` for the named
coding/exterior imports and Gao–Platzer–Clarke's conjunction/disjunction
and inverse-witness proof cases. Reuse
`2026-10-26-full-four-row-capacity-dual-review.md` for the already assessed
arbitrary-field geometric methods; no LP result is needed for this test.
The older rank-19 review is a method comparison, not this kernel's result.

Stacks, Lemma 27.22.1, Tag 089T: inspected its chart construction,
base-change argument and covering proof. Its G(k,n) parametrizes
rank-(n-k) quotients, so k=2,n=7 has two-dimensional kernels. The cover
is valid in characteristic 97. L109/L154 already give the explicit
21 nonzero exterior-coordinate charts and reconstruction used here;
no general Grassmannian theorem is reproved.

Stacks, Lemmas 15.8.4(3)/15.8.7, Tags 07ZA/07ZC: inspected the minors
description, presentation base change and residue-field proof. Apply to
finite matrices on the chart rings over F_97. L109 supplies the concrete
four-by-two restriction: vanishing two-by-two minors imposes rank at most
one; all entries zero is the rank-zero branch. Exact rank one requires
retaining the complement of that branch, separately for each selected row.

Stacks, Theorem 10.34.1, Tag 00FV: inspected both contraction cases in
part (1) and the localization proof of part (2). It applies to finite-type
algebras over a field; over the algebraically closed E a proper affine
ideal has an E-valued point. Thus complete chart/open unit-ideal
certificates can decide emptiness. No practical degree or runtime bound,
prescribed-degree descent or F_(97^20)-point follows.

The approved method is the existing normalized-chart/nonzero-atom
template: keep every nonzero exterior pivot; impose all 35 Plücker
equations and all five selected row gates; express each nonzero-entry
disjunction by exhaustive principal opens with inverse witnesses, using
the cited formula-conversion machinery. Omit every field equation.
Do not require a chosen entry, all entries, or all exterior coordinates
to be simultaneously nonzero. Proving the instantiated cover and checking
its generators are obligations of the later attempt, not results here.
An alternative saturation implementation is not approved by analogy:
it must first justify exactly the same open locus and all boundaries.
The complete finite chart/open method needs no new saturation theorem.

No source read identifies these five concrete matrices' common locus.
This is why citation alone does not answer the target and an exact local
specialization is necessary. Full matching Mathlib coverage is not checked;
unknown coverage is not absence. No general theorem reproof is proposed.

### Bounded external search and unread leads

Fresh queries were `"Grassmannian" "saturation" "Plucker" finite field
exact rank one`, `"Reed Solomon" "0,51,98,177,318"`,
`site.stacks.math.columbia.edu "Rabinowitsch"`,
`"Grassmannian" "nonzero" "unit ideal" finite field Plucker`, and
`"mutual correlated agreement" "Plucker"`. Results included general
incidence/saturation and Grassmannian references, not an inspected
matching fixed-history theorem. Search snippets and secondary pages
are not theorem evidence. The fresh primary reads are the Stacks tags
above. Reuse the October 25 stronger coding/subspace-design comparison;
no generic-position or specially constructed-evaluation conclusion is
imported for these fixed labels. Its unread ABF26/ePrint leads remain
unimported; they are still essential to challenge identification, but
not to this conditional model's bounded geometric test.

### Decision and continuation test

Coverage is SPECIALIZE for one exact saved-history test. Continue only
with a complete algebraic-closure emptiness certificate, or preserve an
exact extension-field survivor/proven nonempty component with all five
rank-one gates and stop empty-locus exclusion. A partial chart search,
proper-ideal software flag, numerical sample or timeout is inconclusive.
Do not resume traversal, prune the saved cover, test another history,
or spend new block-rank tests. The 1665 obligations and exhausted cap
remain intact. Detailed bounded scope is in
`2026-10-28-span-274-rank-one-emptiness-test-review.md`, newly ready for
separate supervisor approval; no mathematical invocation occurs here.

Outcome is EXPLORATION / LITERATURE / NOVELTY_UNCHECKED: source coverage
and a discriminating test are recorded, not a new mathematical result.
The mathematical exploration count remains zero. This is calculation
routing because it instantiates known gates; labeling it creative would
overstate the mechanism. A justified new central creative mechanism has
not yet been obtained from this source-only step.

## Invocation-start proposal retained for provenance

Use only the frozen pair-free model, original 756 L109 blocks and saved
span 274. Node 1006 has history (0,51,98,177,318) and a complete saved
candidate set. Its identity, complete history and comparison with node
4851 were checked this step, but no kernel geometry was investigated.
This proposed test does not depend on accepting L170: it uses L109 and
the prior saved span/kernel verification directly. L170 separately
awaits a critical audit.

The eventual bounded question is whether there exists a nonzero
decomposable p in the saved exterior kernel whose reconstructed plane
has rank exactly one under each selected Q_a. Work over the algebraic
closure, not sampled F_97 points. If an exact emptiness certificate is
available, every descendant of this one history fails L109's necessary
gate, without new block-rank tests. If the locus is nonempty, preserve
an exact extension-field witness or component and stop this empty-locus
route; no coding witness or wider descendant exclusion follows. Weight,
locator and chart gates remain additional conditions. No assertion is
made about the dimension, decomposability or components of span 274.

First check narrowly scoped local sources L109, L154, L158 and L162–L165,
their relevant failure records and the exact named history/label set for
duplicates. Reuse adequate prior primary-source coverage where it matches;
inspect primary theorem hypotheses for projective equations, saturation
and extension-field emptiness where essential. Determine whether the
target is already computed, a known specialization or a genuinely
different gap. Do not run a geometric calculation during that review.

This is source-first preparation of a different necessary-gate mechanism,
not an approved creative proof attempt or a claim of novelty. If it is
duplicate or uninformative, record that evidence and choose a materially
different target. The pending approval must fix the exact bounded test
and imports before any subsequent mathematical turn.
