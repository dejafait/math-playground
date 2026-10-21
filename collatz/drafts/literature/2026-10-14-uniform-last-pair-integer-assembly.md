# Literal last-pair family — proposed integer-exclusion assembly

TARGET: Assemble L068 with L056 and L066 to exclude all-integral cyclic junctions for the literal last-pair family 0<=t<=9250245 under its own-input J guards.
CHECKED: 2026-10-14
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused focused prescribed-parity/redistribution and changed-tail integrality searches in ready assessments; inspected L051 coordinates, L055's complete table, L064 root definition, L068 statement/root/audit, L056/L066 statements/coordinate proofs/audits, C063a/C067a scope, Attempts 027–031 and history 213; the narrow exact-family search found only this proposal and its preceding checkpoint.
SOURCE_EVIDENCE: Reused inspected Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 and essential induction cases pp. 228–229, plus pinned Mathlib valuation coverage in the ready changed-tail assessments; audited local inputs supply the allocation-specific conclusions.
COMPARISON: L068 classifies the exact endpoint/J family; L056 and L066 identify the two surviving literal unshifted roots and prove nonintegrality; C063a/C067a already give stronger all-order exclusions separately for these survivors, but neither states the parameter-family conjunction.
GAP: No essential source or hypothesis coverage is missing; remaining work is a canonical case assembly with explicit root identification, not a new residue evaluation or general theorem.
REASON: Separate scope comparison approves exactly TARGET for a later RESEARCH/REPRODUCTION attempt; no family exclusion is derived in this literature turn.
LITERATURE_REASON: The saved REVIEW_REQUIRED conjunction requires its one-time exact-tail and unshifted-coordinate comparison beyond the preceding classification audit; primary coverage is reused.
SCOPE: Literal L055 J,H order; integer 0<=t<=9250245; stated two tails; all cyclic endpoints, s_i>=540/11 and non-strict own-input J guards; all n_i=s_i-23/11 integral is the condition to exclude, with no additional realization premises.

The main gap is universal eventual descent. The proposed intermediate
target would combine the verified necessary-subsystem classification
with fixed-root arithmetic information. Its downstream use would be a
uniform literal-family integrality obstruction, potentially available
for a separately assessed actual-word application. Other tail allocations,
orders, entry, divergence and universal descent would remain unresolved.

Use exactly L055's indexed J,H table, the literal order, a_23=2+18t,
a_24=166504412-18t and every other tail 2 for integers in the stated
interval. Impose every cyclic endpoint, s_i>=540/11 and the own-input
J guards from L068. The proposed integer condition concerns all
n_i=s_i-23/11, not integrality of shifted s_i. The target adds no
minimum, H/seed, parity, residue, exact valuation or primitive premise,
and makes no arbitrary-order or actual-word conclusion.

Essential inputs for the separate review are L068's audited classification,
L055's literal table, L051's coordinate/guard definitions, audited L056's
literal nonintegrality statement, L064's exact t=1 tuple and audited
L066's changed-tail coordinate match and nonintegrality statement. Read
only those relevant ranges. Reuse the ready affine/prime diagnostic
assessments when their hypotheses match; do not re-run prior computations
or assume fixed-allocation order-rigidity results apply to changing tails.

Compare with C063a/C067a's described fixed-allocation scope before any
duplicate assembly claim, and retain the known real witnesses and earlier
prime-diagnostic stops. A citation may cover some or all of this proposed
conjunction; do not presume novelty. No new primary-source search or
complete applicability review for this target is claimed in this file.
Full matching Mathlib coverage is unchecked, with no absence claim.

Continuation test: approve a precise import or specialization only if
the existing inputs jointly cover every permitted t with the same
unshifted coordinates and outgoing-row pairing. Otherwise identify the
specific uncovered hypothesis or parameter set and leave the target
unapproved. No integer exclusion is derived during the preceding audit.

## Separate source/scope approval — 2026-10-14

The proposal above is retained as provenance. This section approves the
exact TARGET for one later proof attempt. It writes no assembly, changes
no lemma and runs no mathematical calculation.

### Primary coverage reused

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI
10.4064/aa-78-3-227-239,
[section 2 equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
provides chronological affine composition and its fixed-point formula.
The ready `2026-10-14-uniform-last-pair-tail-redistribution.md` and
`2026-10-13-survivor-prime-five-diagnostic.md` assessments record the
primary nonempty binary-word statement, one-letter case, appended-zero
induction and printed analogous appended-one case. Later maps act on
the left; the fixed-point denominator must be nonzero. Only formal affine
identities are relevant. Rational-parity conclusions and integer-itinerary
sufficiency are unused. The audited inputs retain N letters, K odd letters
and positive Lambda, checking these hypotheses. No coding reproof or
new modular computation is needed.

The reused queries are `Collatz rational cycle prescribed parity sequence
redistribution even steps cyclic fixed point Halbeisen Hungerbuhler`,
`Collatz cycle tail exponents parameter affine fixed point guard
inequalities`, `Collatz "166504394" "397573379"`, and `Collatz rational
cycles changed parity word numerator denominator prime cancellation
Halbeisen Hungerbuhler`. The ready assessments distinguish inspected
primary results from unread generalization papers, repositories and
informal leads. No novelty or literature-wide absence follows. Lemma 4's
prefix-domination comparison orders scalar numerators, rather than all
own-input guards; it is unused here. No essential source is blocked and
no fresh external search was necessary for this conjunction.

The inspected ready `2026-10-14-changed-tail-integer-exclusion-assembly.md`
assessment records supporting
[Mathlib PadicVal.Basic, commit 2da3ab0a20dc0c66f56a557e37df39f7d36cb953](https://github.com/leanprover-community/mathlib4/blob/2da3ab0a20dc0c66f56a557e37df39f7d36cb953/Mathlib/NumberTheory/Padics/PadicVal/Basic.lean),
including `padicValRat.defn`, `padicValInt_dvd_iff` and
`Rat.num_or_den_zero_padicVal`, with prime/nonzero and coprimality
qualifications. The assembly can simply invoke audited nonintegrality;
it needs no new valuation proof. Full matching Mathlib coverage of the
family conjunction is unchecked; no formal verification is claimed.

### Exact local applicability

L055's complete table was inspected, including rows 23 and 24. L051 (4)
is identical to L068 (1), and the J part of L051 (3) is L068 (2), with
h_i=log s_i. This does not import L051's minimum, seed, H guard, count-ray
or primitive hypotheses: L068 explicitly isolates the weaker subsystem.
Its audited conclusion covers every integer in the closed interval,
including both extreme tails, and states that exactly t=0,1 pass the
guards. Endpoint uniqueness is established before guards.

At t=0 the tails match L056 exactly: first-24 tails 2, final tail
166504412. L056's coordinate proof identifies L055's unique unshifted
root as Phi/Delta, testing n_0 rather than s_0 or B. Its audit retains
complete residues Phi=4 and Delta=0 modulo 5. Formal affine identities
require no actual itinerary.

At t=1 the tails match L064's j=23 case and L066 exactly: a_23=20,
a_24=166504394, others 2. L064 (3) supplies its unique endpoint root;
L066's coordinate proof and audit identify that same root as
n_0=s_0-23/11=Phi/Delta. Its audited residues are 21 and 5 modulo 25.
The L066 audit explicitly needs no H guard, seed, parity or integer-cycle
bound. Referencing L065 identifies the tuple rather than adding its
full-system premises.

These are comparisons of existing statements, not the family proof.
The later assembly must invoke uniqueness at each surviving parameter
before applying its fixed-root result. It must use integrality of n_0
implied by the all-junction condition, without asserting that every
individual junction is nonintegral. Direct assembly inputs can be L068,
L056 and L066; the table and L064 root definition are already retained
through them. No arbitrary-order or actual-word consequence is approved.

### Overlap, failures and continuation test

C063a already excludes every intact order of the t=0 allocation;
C067a does the same for t=1. Their identity-order cases overlap this
proposal, but neither classifies other parameter values. The later
result would organize audited local conclusions, not discover new
arithmetic. Attempts 027–030 stop diagnostics for different orders of
the old allocation, and Attempt 031 rejects one by a J guard. Those
routes remain stopped; no new order or prime diagnostic is proposed.
Both rational witnesses remain valid. Other allocations, orders, actual
realization, unrestricted cycles and universal eventual descent remain
unresolved.

The coverage threshold is satisfied for exactly the saved target. Continue
with its canonical assembly only. If writing reveals a tail, endpoint,
coordinate or uniqueness mismatch, stop and record the precise discrepancy
without changing hypotheses. A completed proof will still need a separate
critical review. No mathematical family exclusion is asserted this turn.
