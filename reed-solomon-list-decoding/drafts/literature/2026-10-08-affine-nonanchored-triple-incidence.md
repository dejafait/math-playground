# Fixed affine family — nonanchored triple coverage review

TARGET: Determine whether L035's fixed affine family contains a nonanchored triple with empty triple intersection and all three pair intersections of size three.
CHECKED: 2026-10-08
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches for affine triple intersections, transversal-design three-block configurations, doubly constant-weight configurations and exact 10696/191 terms found no inspected matching theorem; scoped L033–L035, affine drafts/history and ATTEMPTS/019–021,023–024 checks found no completed local triple diagnostic. No novelty inference follows.
SOURCE_EVIDENCE: Reuse inspected AGL arXiv:2304.09445v3 (https://arxiv.org/pdf/2304.09445v3), Definition 2.5/Lemma 2.7 and full proof, printed pp. 7–8; ST arXiv:1911.01502v1 (https://arxiv.org/pdf/1911.01502v1), Definition 4.1/kernel equivalence and Lemmas 4.2/4.3, PDF pp. 9–11; AVZ June 24, 2000 manuscript (https://publications.lib.chalmers.se/records/fulltext/local_14986.pdf), definition (5), Theorems 8/32/36, printed pp. 3/6/16/17. Their primary coverage and qualifications are saved in the reused assessments identified below.
COMPARISON: Signed RS kernels concern actual evaluation labels, and ordinary shortening bounds cardinality; neither decides this prescribed mixed head/tail triple incidence. L035 handles only distinguished-block triples, L033 supplies a labeled rank criterion after incidence is given, and L036 handles a different four-neighbor pattern.
GAP: Exhibit and directly verify a complete triple witness, or rigorously exclude every triple in the unchanged 56-slope family; no witness, exclusion or mathematical computation is supplied by this review.
REASON: Essential coverage is sufficient for one bounded exact-set diagnostic, with no new RS theorem to reprove; optional hash-family leads are not essential premises. Newly completed coverage receives separate supervisor approval before research.
LITERATURE_REASON: The startup REVIEW_REQUIRED gate concerns a changed nonanchored three-neighbor clause outside the earlier anchored and quadruple scopes; this is its first exact comparison.
SCOPE: Only three distinct neighbors in L035's exact lexicographic 56-slope family over auxiliary F_191 on {0,...,4}, all intercepts and all outside bijections; no slope change, actual-label rank theorem, full-family cap or RS realization.

## Intended applicability and discriminating test

The main gap is arbitrary-center 67/68-agreement safety; the 955–957
bracket is unchanged. The proposed intermediate target concerns L034's
triple clause among three neighbors, which L035's anchored argument
leaves open. If incidence is absent, that particular clause would be
vacuous under all outside bijections. If a complete incidence witness
exists, whole-pattern avoidance for this triple type must be abandoned;
actual-label L033 ranks would require a further, separately reviewed test.
Neither outcome supplies a whole-family cap or an unsafe RS list.

Essential prospective inputs: L035, L033, L034; L036 distinguishes the
already-audited four-neighbor result, and C001a supplies the unchanged
boundary. Preserve ATTEMPTS/019–021,023–024. This review completes coverage for this exact target, subject to separate
supervisor approval before research. No mathematical derivation or script
for it was performed in the audit or this literature turn. Unknown Mathlib coverage
is not evidence of absence. Full admissibility including a distinguished
block, cross-core consistency, realization and ABF equivalence remain open.


## Reused primary coverage and applicability

The primary statements and essential proof cases are already inspected in
[the three-overlap review](2026-10-07-sixty-core-three-overlap-criterion.md)
and [the direct-source affine review](2026-10-08-affine-four-neighbor-incidence-test.md).
Those reviews were read for this comparison; the primary PDFs were not
newly retrieved this turn. This is reuse, not a claim of a fresh source audit.

Alrabiah–Guruswami–Li, *Randomly punctured Reed–Solomon codes achieve
list-decoding capacity over linear-sized fields*, v3, 26 July 2023,
Definition 2.5 defines signed Vandermonde rows over a finite field.
Lemma 2.7 assumes distinct scalar RS codewords and their agreement
hypergraph; its proof uses a nonzero coefficient-difference kernel.
Neither the statement nor proof excludes an abstract set-incidence
pattern in this auxiliary family. Symbolic or randomly evaluated rank
results do not transfer to fixed subgroup labels.

Shangguan–Tamo, *Combinatorial list-decoding of Reed–Solomon codes beyond
the Johnson radius*, v1, 4 November 2019, Definition 4.1 gives the
three-polynomial difference-kernel dictionary for degree less than s.
Lemma 4.3 divides by common roots. Lemma 4.2 additionally needs even
total overlap and the matching square-matrix degree; the nine overlap
points of L033 do not meet that hypothesis. L033 already contains the
needed local rectangular criterion, so no reproof or new specialization
of that dictionary is needed for this incidence-only target. Its rank-two
realizations prohibit treating every incidence occurrence as forbidden.

Agrell–Vardy–Zeger, *Upper Bounds for Constant-Weight Codes*, June 24,
2000 manuscript, definition (5), Theorems 8/32/36, covers exact
head/tail weights, positive-weight shortening with floors, deletion of
a zero-weight head and the disjoint-support base. L035 already applies
these at weights three/five and distance ten. A cardinality maximum
10696 does not determine which three-block intersections occur.
There is no reason to reprove that bound in this attempt.

The high-girth source comparison in
[the sixty-core review](2026-10-07-sixty-core-extremal-transfer.md) was
also read. Glock–Joos–Kim–Kühn–Lichev, *Conflict-free hypergraph matchings*,
arXiv:2205.05564v1, Theorems 1.1/1.6 and Section 9, gives existence for
sufficiently large ground sets with specified sparse conflicts. Such an
existence theorem does not certify this particular family or its fixed
slope attachment. No asymptotic theorem or unspecified cutoff is used.
This rejection needs no new parameter calculation.

## Local duplicate and failure comparison

Read L035's exact construction, pair proof and anchored proof, L033's
hypotheses, criterion and necessity/converse proof, and L034's full
admissibility clauses. The triple target is exactly clause (2) of L034
among three neighbors; the distinguished block is not one of them.
Neither L035's anchored proof nor the completed L036 audit answers it.
L034 requires actual overlap cubics of rank two, rather than abstract
incidence absence. Thus presence refutes only this sufficient avoidance
mechanism; it does not refute L035 or establish inadmissibility.

ATTEMPTS/024 stops smaller caps in the old anchored graph only.
ATTEMPTS/019–021 stop the older 61-core restrictions and their local
moment strengthenings. ATTEMPTS/023 records a four-block witness in a
different shortened cubic construction; it warns against omitting valid
coordinate reuse, but cannot supply this affine triple witness. These
records were read and remain unchanged. Searches of the specific affine
working notes and history/083–091 found the nonanchored question recorded
as unresolved. No completed local result was found, and no claim of
originality follows.

## Bounded search and optional leads

Search queries this turn were `"affine" "triple intersections" "constant
weight" codes`, `"transversal design" "three blocks" "pairwise"
intersections affine`, `"10696" "191" code affine`, `"affine" "empty
triple intersection" packing`, `"doubly constant-weight"
"configurations"`, `"linear hash families" "forbidden configurations"`,
and `"affine lines" "triangle" "transversal designs"`. Exact-number
hits were irrelevant; the other hits supplied no inspected matching
statement. Snippets are discovery evidence only, not theorem evidence.

Colbourn–Ling, *Linear hash families and forbidden configurations*,
Designs, Codes and Cryptography 52 (2009), 25–55,
DOI 10.1007/s10623-008-9266-7, remains an unread optional lead, as does
Dinitz–Ling–Stinson, *Perfect hash families from transversal designs*,
Australasian Journal of Combinatorics 37 (2007), 233–242. The previously
recorded access issue for the latter is preserved in the affine
four-pattern review; no access attempt was repeated. No theorem or
hypothesis is inferred from search extracts. Neither is an essential
input to direct intersections of the explicit finite sets; dependent
hash-theorem imports remain parked.

## Exact approved scope and evidence requirements

Use the abstract ordered head {0,...,7}, its 56 lexicographic triples T,
slopes s_T=0,...,55 in F_191, and blocks
B_(T,b)=T union {(x,s_T*x+b):x in {0,...,4}}, for all b in F_191.
Head points and ordered tail pairs are disjoint types. The spare tail
point belongs to no constructed block. This restates L035's family,
without choosing a triple or proving any reduction.

The later attempt must test three distinct blocks from this unchanged
family. Require the full triple intersection to be empty, all three
full pair intersections to have size three, and each full private part
to have size two. Check complete points, not only coordinate indices;
retain equal head classes and intercepts until a proved reduction
justifies excluding them. Any common-translation normalization needs
an explicit completeness argument for triples. Do not import the K4
reduction or the anchored disjoint-head case as triple coverage.

A witness certificate must save all three (T,s_T,b) keys, all 24 block
entries, all three pair intersections, the triple intersection, all
private parts and every exact check. A complete exclusion needs a proof
of coverage of every head/intercept case and complete load-bearing
evidence; a bounded search miss is only EXPLORATION. Scripts, if used
in the later research step, must write full evidence to disk and print
the result, required sizes, failures and paths. No script or new lemma
was written or run this turn.

Continue on rigorous absence only with the conclusion that this triple
incidence clause is vacuous for this family under outside bijections.
Abandon whole-pattern avoidance for this clause on one verified full
witness. A later actual-label rank test would be a changed target needing
its own assessment. No auxiliary-field embedding, rank invariance under
bijections, admissibility of an adjoined distinguished block, family cap,
cross-core consistency or RS realization is assumed. Full matching
Mathlib coverage has not been checked; this is not evidence of absence.
The 955–957 bracket and independent unresolved assumptions are unchanged.
