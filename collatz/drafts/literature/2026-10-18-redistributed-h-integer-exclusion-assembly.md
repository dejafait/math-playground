# Proposed changed-table integer-exclusion assembly

TARGET: Assemble L078, L079 and L080 to exclude all-integral unshifted junctions for the redistributed-H table over every cyclic order and the full tail-allocation simplex.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused step 294 affine/divisibility searches and steps 306/308 coverage; compared L078 hypotheses/formula/normalization, C077a complete tests, L079 statement/test and audit passages, L080 statement/coordinate and audit passages, L055 explicit table, the C074a assembly precedent and Attempts 026–031. No fresh external query or calculation.
SOURCE_EVIDENCE: Reused inspected Halbeisen–Hungerbuehler (1997), section 2 equations (2)–(4), Lemma 2 pp. 228–229 and printed induction cases, recorded in the L078 and step 306 assessments; no changed primary hypothesis or essential unread source was found.
COMPARISON: L078 already supplies the conditional all-integral exclusion; L079 certifies every independent O/S/C test for exactly the changed table and L080 certifies nondivisibility for exactly its two candidate parameters at the same normalized unshifted row-0 cut. C074a concerns the original table and is only an assembly precedent.
GAP: Coverage is ready for a separate mathematical application matching all L078 premises; this review proves no assembled exclusion, survivor feasibility or actual-word transfer.
REASON: Approve exactly TARGET for one later RESEARCH/REPRODUCTION assembly using audited conclusions, without reproof of affine/divisibility machinery, new modular calculations or an actual-word consequence.

The original proposal below is preserved; its pending-review wording is superseded by the completed comparison appended below.

Main gap: universal eventual descent. The intermediate target is exactly
TARGET. Its plausible downstream use is a later, separately scoped application
to actual closed words. This proposal performs neither assembly nor that
application. Reuse the ready primary Halbeisen–Hungerbuehler affine coverage
and existing criterion assessments; inspect new sources only if an essential
hypothesis is uncovered.

Essential inputs: audited L078, L079, L080; L055 only for the explicit pair
table. Keep r=25, B=9250245, tau=2, H_0=39, H_24=32670622 and every
other pair unchanged. Allocations are integers b_i>=0 with sum B, outgoing
tails a_i=2+18b_i, and every cyclic order retains its row/input pairing.
L079's endpoint/domain/own-input J hypotheses and all independent data tests
must match L078 without adding H/seed, minimum or primitive-count premises.
After normalization at indexed row 0 the only candidate allocations have
b_i=0 for i<=22, b_23=t, b_24=B-t, t in {0,1}. L080's audited arithmetic
is at precisely the unshifted row-0 cut. Its two modulo-25 pairs are (16,5)
and (7,5); no old-table residues or shifted-integrality premise may substitute.

Continuation test: approve scope only when every required theorem hypothesis
has ready coverage; the later assembly must match all independent tests and
both candidates and preserve the normalized coordinate. A mismatch stops or
narrows the assembly rather than assuming a missing test. Feasibility of the
real survivors, actual-word transfer, other tables, entry, divergence and
universal descent remain unresolved. Both original witnesses and Attempts
026–031 remain valid. No new lemma, computation or novelty is claimed here.

## Step 310 completed source-scope comparison — 2026-10-18

SCOPE: Exactly TARGET; r=25, B=9250245, tau=2, L055 indexed pairs with only H_0=39 and H_24=32670622, every integer allocation b_i>=0 summing to B, attached tails a_i=2+18b_i and every cyclic order; endpoint/domain/non-strict own-input J hypotheses only.
LITERATURE_REASON: The new table-level assembly was REVIEW_REQUIRED; the ready criterion and arithmetic assessments did not approve this exact conjunction. Reuse their adequate primary coverage without repeating external discovery.

The main gap remains universal eventual descent. The intermediate target
is the saved table-level exclusion. Its plausible downstream use is a
separately scoped actual-word application. Neither implication is proved
in this literature-only comparison. No mathematical script or lemma is
written, and no numerical certificate is rerun or independently audited.

### Primary coverage reused

Halbeisen–Hungerbuehler, *Optimal bounds for the length of rational Collatz
cycles*, Acta Arithmetica 78 (1997), 227–239, DOI 10.4064/aa-78-3-227-239,
[section 2 equations (2)–(4), Lemma 2, pp. 228–229](https://math.ch/norbert.hungerbuehler/publications/Optimal_bounds_for_the_length_of_rational_Collatz_cycles.pdf),
is the precise affine/fixed-point input. The prior assessments
`2026-10-17-variable-table-survivor-divisibility.md` and
`2026-10-18-redistributed-h-survivor-mod25.md` record inspection of the
chronological concatenation convention, nonempty-word formula and unique
fixed point for nonzero denominator, the length-one and appended-zero
induction cases and the printed analogous appended-one case. Those
statements and proof cases are reused, not newly retrieved. Only formal
composition is needed; no parity-realization converse, primitive-period
restriction or rotation-gcd theorem is imported. L078 already specializes
the formula and proves the unshifted coordinate identity. Reproving it
would add no needed coverage. Its positive-Lambda hypothesis supplies the
positive nonzero denominator, and its positive integral offsets supply
the nonzero numerator qualifications.

The step 306 assessment also records pinned Mathlib PadicVal.Basic
support for prime/nonzero valuation cancellation. L080 already includes
the needed nondivisibility conclusion, so this assembly needs no fresh
valuation theorem or cancellation proof. Full matching Mathlib coverage
for the changed-table assembly remains unchecked; no absence or formal
verification claim follows. The existing MathPrize target check is reused;
no current prize or adjudication claim is made.

### Exact statement comparison and later application obligations

Read C077a's complete O/S/C hypotheses and endpoint/domain/J subsystem.
L078 retains every one of those tests, with independent certificate
constants; support tests are mandatory here because B>0 and the full
cutoff boundary package is mandatory because tau=2<=B. L079's conclusion
explicitly certifies all tests. Its canonical O, S and C passages and
step 305 audit cover the positive-Lambda enclosure, minimum cap, all
negative tail-2 offsets and order margins; residual support cap, every
early tail-20 offset and next-input margin; both eta bounds, uniform-domain
inequality, every incoming-prefix lower bound, complete inverse-prefix
sum, boundary cap and strict final J margin. The changed row-0 multiplier
and changed final H are explicitly retained. Equal total H alone is
never used to transfer a prefix or numerator.

L055's complete 25-pair table was read only as the explicit data source.
L079 keeps its increasing integer J entries and replaces precisely the
two specified H entries, still at least 3. Its audited conclusion has
exactly the full integer allocation budget and arbitrary cyclic orders
required by L078. The later proof must state the same real lower domain
s_k>=540/11, every exact cyclic endpoint including closure and every
non-strict own-input J guard, keeping each outgoing row with its pair,
allocation and input. No H guard, seed, given minimum location or
primitive/count-ray premise is needed or authorized as a substitute.

L078's arithmetic hypothesis ranges over all integers 0<=t<=B with
t<tau. L079's audited necessary reduction and L080's explicit hypotheses
cover precisely t=0,1 with b_i=0 for i<=22, b_23=t and b_24=B-t.
L080 uses L078's definitions of Phi(t) and Delta, with K=397573379,
N=630138897, all chronological weights and the closing tails. Its audited
conclusion states Delta does not divide either numerator; the recorded
pairs modulo 25 are (16,5) and (7,5). The later assembly may cite that
conclusion directly. No new residue reduction, primality test or modulus
search is necessary. The modulus 25 itself is not asserted to divide
Delta; L080 supplies nondivisibility, rather than an invalid choice of
25 as the divisor in L078's optional sufficient-certificate formulation.

The coordinate to retain is x_0-23/11=s_z-23/11, where z is the position
of indexed row 0 after cyclic normalization. L078 and L079 already keep
both cyclic cuts and every own-input guard. The later application must
explicitly match that tested coordinate to the all-unshifted-integral
premise; it must not assume z=0, shifted integrality, a minimum at row 0
or individual nonintegrality at every junction. L080's test-root identity
requires no survivor guard feasibility.

### Duplicates, failures and decision

The exact original-table C074a assembly assessment was compared as a
precedent, not imported for the changed table. L078 is the general
conditional mechanism; L079 and L080 deliberately leave its table-level
conjunction pending. This is a local application of known machinery and
audited inputs, with no originality claim. The reused step 294 searches
and steps 306/308 comparisons remain adequate; no changed source scope
requires new browsing. Unread peripheral search leads remain unimported.

Attempts 026–031 were inspected. The original rational witness blocks
exclusion from its unchanged real subsystem; the prime-five and joint-prime
stops concern particular old-table orders and cancellations. None licenses
new-table residues or establishes survivor feasibility. The guard failure
of the old joint witness is likewise order-specific. Preserve all stops,
both original rational witnesses and unfinished work. This assembly
reuses the already audited changed-table tests and two arithmetic results;
it does not reopen any exhausted arithmetic diagnostic.

Decision: SPECIALIZE for one later RESEARCH/REPRODUCTION assembly, after
the supervisor's separate next-turn approval of this changed assessment.
Continue only if every independent L078 test, both candidates and the
normalized unshifted coordinate match exactly. Any omitted certificate,
additional candidate or coordinate mismatch stops or narrows the
application. No further factor, modulus or feasibility search is covered.
Actual-word transfer, real survivor feasibility, other tables, universal
entry, arbitrary cycles, divergence and eventual descent remain unresolved.

Outcome: LITERATURE / EXPLORATION / NOVELTY_UNCHECKED. This is new exact
scope comparison and readiness evidence, not a mathematical advance or
an assembled exclusion. Mathematical exploration usage remains zero.
