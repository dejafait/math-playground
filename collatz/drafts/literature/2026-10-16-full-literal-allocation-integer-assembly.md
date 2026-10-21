# Full literal allocation integer exclusion — proposed assembly review

TARGET: Assemble L073 and C068a to exclude all-integral unshifted junctions for every literal allocation a_i=2+18b_i with integers b_i>=0 and sum b_i=9250245 under the endpoint/domain/J hypotheses.
CHECKED: 2026-10-16
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 254 exact-budget/prescribed-word discovery and ready last-pair assembly/audit assessments; inspected L073 and C068a statements, C068a complete proof/audit, L051 definitions, L055 complete table, L068 statement and L056/L066 coordinate passages; checked Attempts 026–031. No fresh external search.
SOURCE_EVIDENCE: Reused inspected Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2, pp. 228–229 and essential induction cases, plus supporting pinned Mathlib valuation coverage; audited L073 and C068a provide the local conclusions.
COMPARISON: L073 covers positive early support in the exact integer simplex; C068a covers the full closed literal last-pair interval with the same endpoints, domain, own-input J guards and unshifted coordinate. Existing fixed-support/all-order exclusions overlap proper subfamilies.
GAP: No essential source or hypothesis coverage is missing for this exact assembly; the canonical exhaustive case assembly and explicit parameter identification remain for a separate research turn.
REASON: Approve exactly TARGET for one later RESEARCH/REPRODUCTION assembly using existing local inputs, with no new affine theorem, residue computation or actual-word consequence.

Scope proposed for review: keep all 25 L055 indexed pairs in literal
order, integers b_i>=0 with sum b_i=9250245, a_i=2+18b_i, real
s_i>=540/11, every L051 exact cyclic endpoint including s_25=s_0,
and every own-input non-strict J guard. The intended condition to exclude
is integrality of all n_i=s_i-23/11. No H guard, seed, chosen minimum,
parity/exact-valuation realization, actual-word application or primitive
count premise is available. Both positive rational witnesses must remain
valid and distinct from an all-integral tuple.

Essential prospective inputs are L051's definitions, L055's indexed
pairs, audited L073 and C068a. Read C068a's exact statement and audit
and only necessary portions of its L068/L056/L066 inputs. Confirm the
full closed parameter interval, both endpoint allocations, all shifts,
and whether any qualification prevents the proposed implication. The
local DAG remains the sole mathematical dependency index; this proposal
adds no node or edge. Reuse ready literature coverage wherever its
hypotheses match, and inspect any essential missing coverage separately.

The main gap remains universal eventual descent. This target could turn
the literal early-support restriction into an integer exclusion for the
full fixed-pair literal tail budget. Nonliteral orders, other indexed
pairs, actual-word transfer and universal descent would remain separate.
Continue only if the exact scopes cover every admitted allocation and
the unshifted integrality implication matches; otherwise record the
specific uncovered premise and revise the target before research.
No assembly is derived or approved here. Full Mathlib coverage is unchecked.

## Separate source-scope approval — step 258, 2026-10-16

LITERATURE_REASON: The saved full-simplex integer assembly is REVIEW_REQUIRED; its one-time family and coordinate comparison is essential. Reuse adequate primary coverage without further browsing.
SCOPE: Exactly TARGET; the complete L055 indexed pairs in literal order, integer nonnegative allocation with the stated total, all L051 cyclic endpoints, lower domain and own-input non-strict J guards. No other L051 hypotheses are imported.

The preceding proposal is retained as provenance. Its pending-approval
wording is superseded by this source comparison. This turn writes no
mathematical assembly and makes no new exclusion claim.

### Primary coverage and qualifications

Reuse [step 254's exact-simplex assessment](2026-10-16-arbitrary-tail-literal-early-support.md),
[the ready last-pair assembly assessment](2026-10-14-uniform-last-pair-integer-assembly.md)
and [its separate audit assessment](2026-10-14-literal-family-integer-exclusion-audit.md).
These record actual primary readings, rather than search snippets:
Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2 equations (2)–(4), Lemma 2, pp. 228–229](https://www.math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf).
The inspected proof cases were length one and appended zero; the printed
appended-one case is stated analogous. Only chronological formal affine
composition and the fixed-point formula for a nonempty binary word with
nonzero denominator are relevant. Later maps act on the left. The local
inputs retain N=630138897, K=397573379 and audited positive Lambda,
which supply the denominator qualification. No rational parity conclusion,
integer-itinerary sufficiency or general coding reproof is needed.

Discovery queries reused from step 254 include `Collatz prescribed parity
word redistribution even exponents cyclic affine intermediate lower bounds`,
`Collatz "9250245"`, and `Collatz rational cycles prefix domination Halbeisen
Hungerbuhler even exponents`. The earlier last-pair assessment also records
changed-tail and exact-count queries. These searches were not rerun.
The inspected scalar-prefix ordering and rotation-extremum results do not
enforce all own-input guards. Unread 2021/SSRN leads and the nonessential
blocked high-cycle lead remain unimported; no essential source is blocked.
No novelty or literature-wide absence claim follows.

The ready assessments record supporting `padicValRat.defn`,
`padicValInt_dvd_iff` and `Rat.num_or_den_zero_padicVal` in
[Mathlib PadicVal.Basic, commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean),
with prime, nonzero and reduced-pair coprimality qualifications. The proposed
assembly invokes C068a's existing nonintegrality conclusion, needing no new
valuation theorem. Full matching Mathlib coverage is unchecked.

### Exact statement comparison and remaining assembly obligation

L073's Hypotheses use the same full literal indexed table, nonnegative
integer allocation, total 9250245, shifted domain and every endpoint and
own-input non-strict J guard as TARGET. Its extra premise is positive
early support through row 22. Its separate audit is recorded in the
canonical file and step 257. No minimum, H/seed or realization premise
appears. Its conclusion is a necessary-subsystem exclusion only.

C068a was read through its proof and complete separate critical audit.
Its last-pair parameter is an integer in the closed interval
0<=t<=9250245, with tails 2+18t and 166504412-18t and all earlier
tails 2. Its endpoints, domain and J guards are identical to those in
TARGET; its integer condition is all n_i=s_i-23/11 integral, never
shifted integrality. The later assembly must explicitly identify its
parameter and both tails from the remaining allocation and check both
closed endpoints. This is an assembly obligation, not a new guard test.
It must invoke L073 only when its positive-support premise holds, and
C068a only after matching its entire family. No reordering is authorized.

C068a's audited L068 input classifies every integer parameter, including
final tail 2. Its proof identifies the two surviving roots by endpoint
uniqueness before importing L056 and L066. Those coordinate passages were
read: the roots are unshifted n_0=Phi/Delta; the old-tail and changed-tail
numerators are distinct. L056 gives Phi=4, Delta=0 modulo 5; L066 gives
Phi=21, Delta=5 modulo 25. L066's audit expressly needs no H guard,
seed, parity or integer-cycle bound; L065 only identifies its tuple.
These arithmetic results are imported, not recomputed. All-integral
junctions include the cut tested by C068a. The assembly must not claim
each individual junction nonintegral or silently add actual-word premises.

### Duplicates, failures and continuation test

C063a/C067a already cover all intact orders separately at the two survivor
allocations. C068a covers the last-pair family, and L073 provides the new
local early-support restriction. L064/L070/L072 cover proper restricted
supports; they do not replace the full-simplex assembly. The planned work
organizes existing audited results and claims no new general arithmetic.
Attempts 026–031 were read: the rational witnesses refute real-system
exclusion, while modular cancellations and one rejected permuted witness
stop specified order diagnostics. This proposed integer assembly preserves
all of them and reopens none of those routes.

The main gap is universal eventual descent. The intermediate target is
exactly TARGET; its plausible downstream use is a separately assessed
actual-word application for this fixed-pair literal tail budget. Nonliteral
orders, other indexed pairs, entry, divergence and universal descent remain
independent unresolved gaps. No cross-notebook input is used.

Approve one separate RESEARCH/REPRODUCTION assembly. Essential immediate
inputs are L073 and C068a; retain L051 definitions and L055 indexed table,
and C068a's audited L068/L056/L066 qualifications. Continue only if the
exhaustive allocation split, exact last-pair parameter, both tail identities,
all closing equations and unshifted all-integral implication can be written
without added premises. A mismatch requires recording the precise missing
hypothesis and abandoning this assembly scope pending review. No new
calculation or source extraction is needed. A completed assembly still
requires a later critical review before broader use.
