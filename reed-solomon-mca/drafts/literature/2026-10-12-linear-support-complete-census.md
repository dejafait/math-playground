# Complete linear-support census — completed source-access review

TARGET: Reproduce a complete census of linear 16_4 support families from the published sixteen-vertex cubic-graph census, retaining duals and marked tau-zero triangles.
CHECKED: 2026-10-12
DECISION: SOURCE_BLOCKED
SEARCH_EVIDENCE: Exact companion-title/author and configuration-graph/isomorphism queries, the published graph-file URL, author PDFs, Aalto's primary dataset mirror and nauty documentation were checked; file access and load-bearing theorem/proof passages remained unavailable. See the bounded access record below.
SOURCE_EVIDENCE: Read Aalto's creator-maintained dataset description, graph6 convention and class-count table, lines 20–28; reused the previously inspected Zenodo v1 description. Neither the 4,207-row file nor its generation/completeness evidence nor a full graph-to-four-support correspondence was inspected.
COMPARISON: The primary description advertises complete cubic-graph coverage and an appended automorphism order, but gives no inspected algorithmic completeness proof or four-block/duality/marked-triangle theorem. L072/L079 and positive-only rank samples do not supply these missing inputs.
GAP: Actual graph data and essential generation evidence, the complete leave-graph/complement-decomposition correspondence and point-preserving versus dual/marked scope remain unverified; no complete census invocation is approved.
REASON: Park dependent graph-census work after this bounded source-access review; preserve the exact reproduction target and use an independently testable local proof-audit target requiring separate scope approval.
LITERATURE_REASON: The complete cubic-graph dataset and source-to-support reduction are new essential leads; ready affine-plane moment coverage does not approve a census of all support families.

The main gap is exclusion of arbitrary sixteen-count equality families.
This intermediate target concerns only sixteen distinct four-subsets of
sixteen labels, degree four everywhere, with pair intersections at most one.
The optional marked triangle is L072's three blocks, equivalently the
prescribed L057 tau-zero support pattern. No reduction from all equality
families to this class is assumed. Essential context IDs: L010, L072, L079;
these supply equality constraints, one abstract family and its audited
fixed-H exclusion, respectively, not census completeness.

The exact external candidate input is Betten–Betten–Heinlein–Östergård,
*Dataset for On the regular linear spaces up to order 16*,
[Zenodo 7890664](https://zenodo.org/records/7890664), v1, 31 August 2023,
DOI 10.5281/zenodo.7890664. Its file `graph_16_3.txt.gz` is 36.3 kB,
published MD5 `ca9ed2b489cf157f42f3bb70eba1841d`; rows use graph6 plus
an automorphism-group order. The description says all cubic graphs on
sixteen vertices, not merely connected graphs. Verify this scope and the
generation evidence. No download, decoding or mathematical program was
performed. Other large files in that dataset are unnecessary to this target.

Proposed test: assess complete enumeration of four-block decompositions of
complements of the published graphs, followed by point-preserving incidence
isomorphism rejection. The leave-graph correspondence is a proposed proof
obligation, not a result derived here. Distinct dual configurations must not
be silently merged by uncolored Levi-graph equivalence. If triangle markings
are used to reduce later work, coverage of all markings needs a precise
convention. The reported nineteen configurations is a comparison lead;
its original duality convention is unread and cannot serve as a stopping
condition or completeness oracle.

Downstream use: a verified complete incidence list could select one concrete
non-L072 type and a necessary uniform moment obstruction, or establish the
actual finite scope of the linear branch. It would not itself exclude any
RS pencil. Every H-labeling, nonzero-weight condition, original finite chart,
moment compatibility, nonlinear-support extraction and challenge-definition
qualification remains unresolved.

Continue only if the graph source is inspectable and sufficient for a complete
case set, and the intended correspondence and isomorphism conventions are
covered. If these fail, record the failure and choose a different independently
testable target; no positive-only samples or an assumed nineteen-case list.
Reproduction of known combinatorial mathematics would be justified by the
essential implementation and explicit marked/duality scope required locally,
not a novelty claim. ATTEMPTS/020, /027 and /028 remain preserved.

Reuse the [completed broader comparison](2026-10-12-linear-four-support-structure.md)
for the already-inspected inapplicable real-pseudoline obstruction and access
failures. Do not repeat its searches without a specific new source lead.
Mathlib coverage of the census/correspondence is not checked. No cross-notebook
input is proposed. This assessment does not approve a mathematical invocation.

## Completed review: evidence actually inspected

The inspected primary mirror is the creators' Aalto research-portal record,
[*Dataset for On the regular linear spaces up to order 16*](https://research.aalto.fi/en/datasets/dataset-for-on-the-regular-linear-spaces-up-to-order-16/),
dated 31 August 2023, accessed 12 October 2026. Read its Description,
graph-file format and count table, web lines 20–28. Its all-graphs claim
has no stated connectedness restriction; the table gives 4,207 in the
sixteen-vertex degree-three column. This confirms the published claim,
not the file's contents or independent completeness. The mirror links
the concept DOI 10.5281/zenodo.7890663; the pinned version remains
10.5281/zenodo.7890664, not a changed dataset version. Graph rows append
an automorphism-group order to graph6. Configuration files in this dataset
have other parameters and do not provide the required 16_4 support list.

No essential mathematical theorem is imported. The proposed correspondence
and the point-preserving, dual-retaining and marked-triangle conventions
in the original proposal above remain proof/scope obligations, not results
proved during a literature turn. In particular, a graph representative
alone is not a representative of every decomposition of its complement.
A future implementation would have to document complete decomposition
coverage and rejection conventions before its output could be used.
An original classification's nineteen total is still no stopping oracle.

## Bounded access and search record

New exact queries included `"On the Regular Linear Spaces up to Order 16"
cubic configurations`, the exact title excluding dataset mirrors, `"regular
linear spaces" Heinlein arxiv`, `"Betten" "Heinlein" "linear spaces"
paper`, `"regular linear spaces" "clique" Betten`, `"Regular Linear
Spaces" "isomorphic" "configuration graph"`, `"cubic graphs" "4207"
McKay`, and targeted betten5.pdf construction/isomorphism/duality queries.
The companion paper itself was not located in inspectable form. Unrelated
linear-space hits and cubic-graph applications were screened as leads;
they were not imported as completeness evidence.

The precise published data URL
`https://zenodo.org/records/7890664/files/graph_16_3.txt.gz?download=1`
returned no inspectable data in the web reader. A single scoped curl
failed DNS for zenodo.org (exit 6). The alternate web connector reported
HTTP 429 for the record. No file was saved, decoded or checksum-verified;
the published MD5 above is not a computed checksum. No graph census,
format-validation program or mathematical script was run.

The newly found exact configuration-graph lead is Betten–Betten,
[*The Proper Linear Spaces on 17 Points*](https://www.math.colostate.edu/~betten/pub/betten15.pdf),
Discrete Appl. Math. 95 (1999), 83–108, introduction, manuscript p. 3.
Search extraction describes completion by two-point lines and calls the
resulting regular graph the configuration graph. The PDF returned 29 pages
but zero text lines; screenshot access failed. This is an unread lead,
not a primary theorem assessment or a justification of the required
four-block-decomposition specialization. Likewise betten5.pdf still
returned fourteen pages but no text, and its indexed count/algorithm
extracts were not promoted to full source coverage.

McKay–Piperno's [nauty and Traces User's Guide 2.9](https://users.cecs.anu.edu.au/~bdm/nauty/nug29.pdf)
initially exposed PDF metadata but targeted extraction, subsequent access
and screenshots failed. McKay's graph-data page also timed out. Thus
neither generator hypotheses/completeness nor colored canonical-label
conventions were read sufficiently to approve an implementation. Installing
or running a generator would be mathematics/implementation, not an access
review, and was not attempted. No essential proof case was replaced by a
search snippet. Access tests ended once these independent leads remained
uninspectable; no further retry loop is recommended.

## Decision and independent continuation

Outcome: EXPLORATION, source coverage incomplete. This changes the proposed
census gate to SOURCE_BLOCKED; it supplies no theorem, classification,
new support family or mathematical negative result. The frozen-model
interval is still 11/q–16/q. It spends zero mathematical exploration
turns and does not reset the existing exploration count.

Park both this data-dependent reproduction and the original unread-table
route. Retain the independently testable L064 two-row compatibility bound
as the proposed next proof-audit target: it could become a checked input
for a future simultaneous triangle argument without a census. The supplied
overview and scoped history identify L064 as unaudited; a narrow check
also found L068's audit already completed in history/158, so that alternative
was screened out as a duplicate. The old triangle-count assessment is ready
for its own unchanged target, but does not explicitly cover the newly
specified L064 audit. The new audit assessment is therefore REVIEW_REQUIRED
for separate approval, not silently ready coverage.

Preserve ATTEMPTS/020, /027, /028 and /025. The last stops formal common-root
conditions and unstructured label samples; checking L064's existing uniform
proof does not reopen that mechanism. A correct two-row bound still would
not bound the number of different supports at one weight point. Arbitrary
linear/nonlinear extraction, moment exclusion and challenge qualifications
remain independent unresolved gaps. No lemma, DAG row, PROOF.md passage
or mathematical script changed in this step.
