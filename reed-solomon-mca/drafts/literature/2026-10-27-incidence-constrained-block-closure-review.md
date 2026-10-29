# Incidence-constrained block closure — completed source comparison

TARGET: Assess an incidence-constrained exterior-block closure mechanism for the fixed-S/J twelve-row gap, using L167 rows 2 and 3 as a bounded pilot.
CHECKED: 2026-10-28
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 532 searched finite closure/semilattice enumeration, realizable-polymatroid flats, block-closure packing and Reed–Solomon/MCA combinations; compared L109/L125/L151/L153/L154/L162/L167/L168 and ATTEMPTS/041,043,048,055. Exact queries, inspected passages and bounded duplicate search are below; no novelty inferred.
SOURCE_EVIDENCE: Borchmann, CLA 2012 pp. 9–20, sections 2–4, Theorems 1–2 and Lemmas 1–3, https://ceur-ws.org/Vol-972/paper1.pdf ; Crowley–Simpson–Wang, Algebraic Combinatorics 8(5) (2025), section 2.1/Example 2.2 pp. 1289–1290, https://connorgs.net/assets/papers/combinatorial_flats_and_schubert_varieties_of_subspace_arrangements.pdf ; checked matching preliminaries in arXiv:2410.10552v4 (2026-10-07). Reuse the capacity/enumeration and arbitrary-field exterior coverage identified below.
COMPARISON: Finite closure enumeration and representable-polymatroid closure are known; the missing coupling is an upper bound of eleven selected supports in every deficient block closure containing this numerical pair. L151 excludes a different pair with actual coding gates; L153 supplies equal two-row ranks; L154 specifies an unsolved gated formula; L168 excludes one completion only. No inspected theorem or located local implementation supplies the proposed bound.
GAP: A later attempt must justify a complete cover of deficient completions and a sound incidence-capacity certificate on that cover, or preserve a twelve-support deficient witness or unresolved frontier. Closure membership does not force support selection, and a current closure's capacity does not bound its larger deficient descendants.
REASON: Essential method coverage now permits a bounded test of a distinct rank-growth/capacity mechanism. This literature turn establishes no new rank, closure identity, capacity bound or lemma. The separately saved proposed ready continuation requires approval next turn.
LITERATURE_REASON: Gate-required first comparison of the changed complete-block closure mechanism; earlier fixed-stack audits and two-row census coverage do not cover its closure/capacity coupling.
SCOPE: Literature comparison and proposed pilot only: original L109 S/J, all 756 supports and whole six-row blocks over F_97, fixed L167 rows 2 and 3, integer degrees at most four and pairwise intersections at most one; all ranks below 21 and all extension-field kernels retained. No genericity, pair symmetry, matroid exchange or coding converse is approved.

## Completed comparison — step 532

The main local gap is uniform twelve-row exclusion. The intermediate
target is a certificate bounding the size of a linear degree-four support
selection inside every deficient complete-block closure containing the
pilot pair by eleven. A successful pilot could support a later all-pair
test under C152a; it supplies no transport between numerical pairs.
Representation, coding gates and challenge identification remain separate.

### Primary statements and essential proof cases inspected

D. Borchmann, *A Generalized Next-Closure Algorithm — Enumerating
Semilattice Elements from a Generating Set*, CLA 2012, pp. 9–20,
[primary PDF](https://ceur-ws.org/Vol-972/paper1.pdf): section 2 p. 10
requires a finite ground set and an extensive, monotone, idempotent
operator; Theorem 1 gives the next closed set in lectic order.
Section 3 pp. 11–13 assumes an associative, commutative, idempotent join
and a finite ordered generating set. Read Lemmas 1–3 and Theorem 2's
proof: the three index-order cases establish the order; the successor
proof uses existence, the lower comparison and the maximal admissible
index. Section 4 p. 14 includes the bottom closure in the generating set.
This supplies enumeration, not constrained pruning or a small state count.
The cited Ganter original/reprint was traced as a reference, not read;
Borchmann's own generalized theorem and complete proof suffice here.

C. Crowley, C. Simpson and B. Wang, *Combinatorial flats and Schubert
varieties of subspace arrangements*, Algebraic Combinatorics 8(5)
(2025), 1285–1312, DOI 10.5802/alco.447,
[author-hosted published PDF](https://connorgs.net/assets/papers/combinatorial_flats_and_schubert_varieties_of_subspace_arrangements.pdf):
section 2.1 pp. 1289–1290 defines rank, flats and closure. Example 2.2
gives projection ranks and the equivalent intersection-of-kernels
realization; read both constructions. These linear-algebra preliminaries
allow an arbitrary field. Ordinary flats differ from the paper's expanded
combinatorial flats. The latter's Schubert geometry requires characteristic
zero and is not imported. The same relevant preliminaries were checked
in [arXiv:2410.10552v4](https://arxiv.org/html/2410.10552v4), dated
2026-10-07; its revised Theorem 3.20 is unused. The publisher PDF returned
403, resolved by the author's published copy, so no essential blocker remains.

Kastner–Shaw–Winz, *Tropical Compactification via Ganter's Algorithm*,
DCG 73 (2025), 264–292,
[section 2.2 and implementation discussion](https://link.springer.com/article/10.1007/s00454-023-00581-2),
provide an inspected implementation lead for generic closure enumeration
in polymake. Their tropical closure is not the present block closure;
no implementation, complexity improvement or geometric theorem is imported.

Reuse the inspected Eppstein–Loffler–Strash maximal-clique proof and
SCIP 8.0.4 capacity/conflict definitions recorded with direct URLs in
`2026-10-26-l163-forty-support-compatibility-review.md`. Its warning
against checking only maximal cliques under degree constraints applies.
Reuse exact nonnegative-weight/weak-duality coverage in
`2026-10-26-full-four-row-capacity-dual-review.md`, citing Boyd–Vandenberghe
sections 5.1.3/5.2.1–5.2.3 pp. 216,224–227 and the author PDF there.
It covers an exhibited rational capacity bound, not a realizable mask
or an integral packing theorem. No new source extraction is claimed for
these unchanged tools. L109's audited necessary direction and arbitrary-field
exterior coverage remain adequate; no general theorem needs reproof.

### Local duplicates, hypotheses and failures

Read L109 through the recovery/converse boundary, the hypotheses,
conclusions and necessary-input uses of L125/L151/L153/L154/L162,
L151's actual-row assembly, L167's full support table and L168's fixed-stack
statement. The pilot is literally

    row 2: I={8,12}, K={70,75}; row 3: I={18,22}, K={79,85}.

Neither is L125/L151's pair. Their conclusions need actual rows, not
just a rank-deficient support family; importing them as capacity exclusions
on arbitrary closures would change hypotheses. L153's complete census
does not identify equal kernels. L154's finite-field formula has all
coding gates but proves no emptiness. L162 prevents an unconditional
four-row-finiteness shortcut. L168 cannot exclude other completions of
its first two rows by symmetry or rank extrapolation.

ATTEMPTS/041 preserves deficient later-row stacks; /043 preserves
decomposable four-row survivors passing selected gates; /048 stops rank-only
pair stratification; /055 stops completion-sensitive marked extraction.
The proposed test adds complete-block closure and incidence capacity
jointly, without assuming any of those false implications. A filename/content
search for NextClosure, block closure, closure operator, polymatroid and
rank growth in `scripts/seven-coordinate/`, `scripts/l167-twelve-row-exterior/`
and `drafts/literature/` found only this intake, not an implementation.
This bounded search is not a claim about all software or all literature.

Three candidate mechanisms were compared: whole-block closure plus
capacity is the selected new coupling; greedy exchange on support labels
has no assessed matroid hypotheses; geometric plane stratification is
already the L155–L165 route and is not a new closure pilot. In particular,
individual covectors must not replace whole blocks as selectable supports.

### Search record and continuation boundary

Queries: `Ganter Next Closure algorithm closure operator closed sets lectic
order paper pdf`; `linear polymatroid subspace arrangement rank function
closure enumeration blocks subspaces`; `"Reed Solomon" "block" "closure"
"matroid" agreement`; `"subspace arrangements" "degree" "packing" closure
rank`; `"polymatroid" "closure" "capacity" enumeration`; `"Reed-Solomon"
"subspace arrangement" "rank"`; `"subspace" "block" "closure" "set packing"`;
`"mutual correlated agreement" "matroid"`. Searches returned the primary
methods above and unrelated channel-capacity/secondary challenge pages;
the latter were not used as theorem evidence. The bounded search found
no adequate matching twelve-row theorem; this does not establish novelty.

The next proposed assessment is
`2026-10-28-block-closure-capacity-pilot-review.md`. It asks for a
rank-growth/capacity invariant and a complete-cover justification before
any large enumeration. Capacity inside one current closure cannot prune
larger closures without that justification. A closure mask may contain
conflicting supports, which remain optional selections. Merging equal
spans may not merge different selected histories or residual capacities
without a proved domination rule. Rank twenty is not the only deficient
case. No extension-field samples or nonlinear realization are substituted.

Continue on an exact certificate covering all deficient completions with
capacity at most eleven. A twelve-support linear degree-four deficient
family stops this exterior-only version; it is not a coding witness.
Uncontrolled closure growth or an unfinished cover ends the bounded
attempt with its entire unresolved frontier saved. A proposed 10,000-state
cap limits exploration, not the theorem's quantifiers. Full matching
Mathlib coverage for the combined mechanism is not checked; the cited
closure results are supporting inputs, not this missing bound.

## Retained invocation-start proposal, before the comparison above

Keep the original characteristic-97 S/J and all L109 maps. The pilot
starts with precisely L167 rows 2 and 3, which are disjoint as numerical
supports. Compare an approach that branches on the span of complete
six-row blocks, closes each branch under blocks already in that span,
and bounds admissible added rows using pairwise linearity and integer
coordinate degrees at most four. The proposed output is a reproducible
closure/pruning rule with a finite pilot stopping criterion, not another
two-row rank census. A subsequent assessed attempt must retain every
rank-deficient branch and state whether it tests only the exterior
relaxation or actual decomposable/weight/chart feasibility.

Potential downstream use: if the pilot admits rigorous capacity bounds
below twelve for all its deficient closures, test whether those bounds
can later extend to all disjoint pairs extracted by C152a. A pilot is
not a universal proof, and no transfer between numeric pairs is assumed.
If closure growth cannot be bounded, or a degree-feasible deficient
family survives, preserve that evidence and stop this version rather
than infer a nonlinear realization or repeat rank-only extrapolation.

Before approval, compare canonical L125/L151 fixed-pair exclusions,
L153's rank-twelve census, L154's certificate contract, L162's infinite
four-row locus and ATTEMPTS/041,043,048,055. Retrieve primary theorem
hypotheses for any closure/capacity theorem actually used. Avoid broad
source scans or another census under the name of literature. The next
review must decide whether this is distinct and useful, bound the pilot,
and identify any pre-existing implementation; otherwise park it.

No new mathematical assertion is derived here. This intake needs a
separate literature approval turn. If a genuinely new central proof
mechanism is then justified, recommend proof_attempt/creative with
deep_research/max and a precise bounded test; algorithm-only replay
should instead receive its actual calculation/implementation route.
