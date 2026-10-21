# Five-support actual-label diagnostic — source comparison

TARGET: Determine realizability for every m>=1 of the prescribed five 68-supports with a 59-point common core and consecutive subgroup pair overlaps.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Scoped local five-support/59-core/quartic/K5/five-way search found only the proposed continuation; external exact-support, five-intersection and consecutive-power queries found no matching inspected result. Higher-order searches led to the generic GM-MDS comparison below; failed searches do not establish novelty.
SOURCE_EVIDENCE: Rechecked AGL arXiv:2304.09445v3 Definition 2.5/Lemma 2.7 and complete proof, printed pp. 7–8, Theorem 2.9, p. 9; ST arXiv:1911.01502v1 Lemma 4.3 statement/full proof, pp. 11–12, and Section 5 characteristic-two assumption; inspected generalized GM-MDS arXiv:2310.12888v3 Definition 1.3/Theorems 1.4–1.5 and Section 2 genericity definition. Reused the saved BGM v4 theorem comparison; precise links below.
COMPARISON: The signed matrix works over arbitrary finite fields with arbitrary message count; its inspected lemma supplies scalar necessity, not a five-distinct-tuple converse. Common-root division is a known proof step. Generic/random higher-order guarantees do not settle prescribed subgroup points; L031 covers four messages only.
GAP: Justify the fixed five-support specialization, all ten distinctions, extension-field and tuple-width qualifications, compatible center and exact finite evidence. No rank or realizability conclusion has been obtained.
REASON: Essential coverage of the changed five-message scope is now adequate for one finite specialization attempt; importing known equality tools avoids reproof of generic full-rank results. No exact-match theorem or originality claim is asserted.
SCOPE: Only the five fixed supports defined below in the existing rate-1/16 instance; no auxiliary-coordinate replacement, general five-support classification, extremal cap, or RS-list threshold conclusion.

## Exact proposed configuration

Use the fixed E=F_65537, F=F_(65537^28), H=<h>, h=19139,
k=64 and m>=1 from C001a and L031. Let
C={h^20,...,h^78}. Order the ten pairs ij with 1<=i<j<=5
lexicographically, numbering them r=0,...,9, and set
U_ij={h^(2r),h^(2r+1)}. Let W_i={h^(78+i)}, i=1,...,5.
The prescribed support S_i is C union W_i union the four incident U_ij.
The later work must verify the disjointness and all support sizes, rather
than silently importing a four-support configuration.

Realizability asks for five pairwise distinct polynomial m-tuples over
F, with every row of degree strictly less than 64, and one center
Y:H -> F^m agreeing with tuple i on all of S_i. Extra agreements are
allowed. Neither descent of arbitrary given tuples nor a scalar
projection preserving all distinctions may be assumed.

## Relevance and discriminating test

The main gap is arbitrary-center 67/68 safety. The candidate intermediate
target tests a simultaneous five-message restriction on actual subgroup
labels. A rigorously forbidden configuration could supply a further
necessary constraint for a later support-family bound; a realization
would show that this proposed exclusion must be abandoned. Neither
outcome alone establishes a useful uniform cap. Quantitative exploitation,
cross-core consistency and the 184665717 cap benchmark remain independent
unresolved tasks; no such result is assumed.

This changes the number of messages, common core and actual-label
compatibility question. It does not try another coordinate substitution
in the stopped auxiliary cubic families. Retain ATTEMPTS/019–021,023–025.
The historical stops remain evidence, not a global ban on additional
support constraints. This source review approves the method and scope
only; no new criterion, matrix, determinant, mathematical computation
or realization proof is derived in this turn.

## Inspected primary statements and proof cases

Alrabiah, Guruswami and Li, *Randomly punctured Reed–Solomon codes
achieve list-decoding capacity over linear-sized fields*,
[arXiv:2304.09445v3](https://arxiv.org/pdf/2304.09445v3), 26 July 2023:
Definition 2.5, printed p. 7, assigns signed Vandermonde rows to a
hypergraph over any prime-power field, omitting the last message block.
Lemma 2.7, p. 8, assumes distinct scalar RS codewords and their agreement
hypergraph at the evaluation vector. Its complete proof uses coefficient
differences from the last message as a nonzero specialized kernel vector.
This is the imported equality framework; deleting constraints for extra
agreements must be justified in the specialization. Theorem 2.9, p. 9,
assumes a k-weakly-partition-connected hypergraph with at least two
vertices and gives full column rank over F_q(X_1,...,X_n). Its rational
function field conclusion is not a rank certificate at h's prescribed
powers. No partition-connectivity computation or generic-rank reproof
is needed for the approved finite test. Neither statement supplies the
required converse or preservation of every tuple distinction.

Shangguan and Tamo, *Combinatorial list-decoding of Reed–Solomon codes
beyond the Johnson radius*,
[arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1), 4 November 2019:
Lemma 4.3, printed pp. 11–12, assumes failure of scalar list-two decoding
at radius (2/3)(1-R) and concludes vanishing of a member of its specified
determinant-polynomial family. The full proof first selects suitable
three-way overlaps, then divides message differences by the product of
common roots, retaining strict reduced degree, vanishing on residual
overlaps and the cycle identity. Only this common-root proof step is
relevant here; its list-radius conclusion is not a five-support result.
The opening of Section 5, p. 12, assumes q a power of two, as does Lemma
5.4's t-message kernel statement. The retained four-support assessment
already excludes importing its unsigned cycle construction at
characteristic 65537. Use the signed AGL framework instead.

*Generalized GM-MDS: Polynomial Codes are Higher Order MDS*,
[arXiv:2310.12888v3](https://arxiv.org/html/2310.12888v3): inspected
Definition 1.3, Theorems 1.4–1.5 and the Section 2 definition of generic
polynomial codes. The polynomial coordinates are linearly independent;
evaluation variables are algebraically independent over the base field.
The theorems give higher-order MDS for generic polynomial codes and
their duals. They do not assert the property at every finite-field
specialization. No proof or result about this fixed subgroup is imported.
Only these passages were inspected; the remaining proof is unread and
unnecessary for this exclusion of direct applicability.

Reuse the earlier BGM comparison in
[2026-09-26-current-target.md](2026-09-26-current-target.md), “New primary
readings”: Brakensiek–Gopi–Makam,
[arXiv:2206.05256v4](https://arxiv.org/html/2206.05256v4), 28 August 2024,
Theorem 1.13, Corollary 1.15, Theorem 1.16 and Proposition 4.5.
The saved inspected notes distinguish dual higher-order-MDS equivalence
from generic/random RS guarantees. This unchanged qualification is
reused without new primary retrieval. No fixed-subgroup MDS hypothesis
is established or assumed here.

## Search, duplicates and recorded stops

Queries actually issued were:

- `Reed Solomon higher order MDS fixed evaluation points signed intersection five codewords realizability`
- `"Reed Solomon" "19139" five supports`
- `"Reed-Solomon" "five" "intersection matrix"`
- `"Reed-Solomon" "consecutive powers" "higher order"`
- `"Reed-Solomon" "five" "common" "supports" realizability`
- `"Reed-Solomon" "59" "68" "agreement"`

The exact searches yielded no matching primary theorem; generic
higher-order results led to the inspected comparison above. Irrelevant
coding-implementation hits were not used. This is bounded source
coverage, not a claim that no stronger theorem exists.

Read C001a's instance/list qualifications and L031's framework,
necessity, extension-rank argument and six-subspace converse; reuse its
source assessment. L033 is the recorded three-message comparison,
not a five-message premise. The scoped local search found no completed
duplicate of this fixed test. Read ATTEMPTS/019–021: L028–L030 stop
strengthening precisely the old local edge system, without supplying a
common RS center. Read ATTEMPTS/023 and 025: L032/L039 stop their
auxiliary cubic avoidance families and do not test actual subgroup
labels. ATTEMPTS/024 records L035's sharp neighborhood count, not a
five-support theorem. These stops are preserved; none alone decides
the proposed actual-label compatibility test.

## Approved attempt and stopping test

The exact TARGET is ready for one research turn under SPECIALIZE,
normally classified REPRODUCTION of the inspected equality framework.
Justify why common-root removal and signed constraints apply to the
specified five messages, while keeping all distinctions. Establish
necessity row by row for arbitrary ambient-field tuples; do not presume
that their coefficients descend or that one projection distinguishes
every pair. Any scalar sufficiency argument must separately justify
simultaneous distinctions and compatibility of the single center.
The finite-union technique in L031 is supporting methodology whose
five-message applicability must be proved, not an imported conclusion.
Singularity alone is insufficient.

Before using finite arithmetic, verify the exact generator order, every
point, disjointness, support size, complete pair intersections and
absence of unintended shared points. Save the complete signed system,
exact elimination and every needed distinction check. A realization
requires explicit strict-degree messages, all pairwise differences and
the center's agreements; a prohibition requires a rigorous obstruction
for all m, not failure of a scalar search. Inspect complete load-bearing
certificate values, not previews. Do not vary the prescribed labels or
start a general five-support search within this approval.

A certified prohibition permits proposing a separately assessed
counting use; a certified realization abandons this fixed exclusion.
An inconclusive system or unresolved distinctness argument is recorded
as unfinished, with no cap or safety claim. Relevant full Mathlib
coverage and supporting theorem names remain **not checked**; absence
is not inferred. No reproof of generic/random list-decoding results is
authorized or necessary.

Essential continuation inputs: C001a for the instance and strict list
model, L031 for the inspected four-support framework and subgroup
generator. L033 is comparison, while L039 motivates leaving auxiliary
avoidance and is not a proof premise. ABF equivalence, 67/68 safety,
uniform family caps and common-center realization of large families
remain unresolved. The existence or failure of this particular
five-message realization is the only proposed mathematical test.
