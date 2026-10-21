# All smaller auxiliary subfields — completed source review

TARGET: Assess whether all subfields of MN of degree less than 36 can jointly support a generalized norm relation for L96.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched generalized norm relations for PGL(2,11) and the S3 fiber product, and GAP exhaustive subgroup methods; inspected primary GAP documentation and pinned implementation plus Hulpke's survey; compared L055, ATTEMPTS/022 and the ready Etienne assessments.
SOURCE_EVIDENCE: Reuse Etienne arXiv:2411.13124v2 Proposition 2.7 pp.12-15 and full orbital-map coverage; newly read GAP Reference Manual 39.19-3,5,6 and 39.20-10/39.21-1, GAP v4.15.1 lib/grplatt.gi LowIndexSubgroups's complete finite-group method, and Hulpke arXiv:2012.01595v1 Sections 3.2,4,4.1 printed pp.8-9,15-17.
COMPARISON: Known unconditional criteria and an exact bounded-index enumeration procedure cover the enlarged test; neither the sources nor L055 decide its actual subgroup list or map-image rank.
GAP: Execute and certify complete index-at-most-35 subgroup coverage for the audited group and all rational equivariant maps to its 36-dimensional target; backend availability and the actual result remain unverified.
REASON: The essential source scope is now covered for a separate finite calculation; this is local source progress, without a new relation, obstruction or branch exclusion.
SCOPE: All fixed fields (MN)^J with [G:J]<36, all conjugate embeddings and arbitrary auxiliary multiplicities; relation existence only, with no class/unit or descent calculation.
LITERATURE_REASON: The saved REVIEW_REQUIRED target enlarges the auxiliary set beyond the audited pair; exhaustive bounded-index subgroup coverage was the essential unread interface.

The main gap remains unconditional emptiness of L032's 96a1 branch.
The proposed intermediate target tests the feasibility of reducing its
degree-36 arithmetic to smaller fields within this particular overfield.
It does not reopen the failed pair. Preserve ATTEMPTS/018-022, especially
the distinction between a sufficient Minkowski cutoff and necessary
complexity, and the GRH qualifications of the inspected algorithms.

Inputs: L051's L96=K96F and degree 36; L055's audited splitting fields
M of m and N of h, with G=Gal(MN/Q) the sign fiber product of
PGL2(F11) and S3, of order 3960. H is the stabilizer of one pair in
P1(F11) times {0,1,2}. The future mathematical question concerns all
subgroups J with [G:J]<36 and their fixed fields, including all conjugate
embeddings and arbitrary multiplicities. No claim about the answer,
irreducibility of the missing 22-dimensional space, a complete subgroup
list or existence of useful new auxiliary fields is made here.

The completed comparison below covers the criterion and an exact
finite-group enumeration procedure. Continue to the separately approved
calculation only with complete subgroup coverage and all maps, or an
equivalent complete constituent test. A negative answer would
park smaller auxiliaries in this overfield only; a positive answer would
identify concrete fields for later unconditional arithmetic review.
Neither outcome alone certifies class groups or excludes an integer
branch. Unconditional auxiliary completeness, integral saturation and
transfer, torsion lifts, support/norm maps, descent compatibility and
full-disk disjointness remain unresolved. No GRH, new theorem, calculation
or cross-notebook input is introduced. Mathlib coverage is not checked.

## Newly inspected primary enumeration coverage

The [GAP Reference Manual, Chapter 39](https://gap-system.github.io/gap/doc/ref/chap39_mj.html),
accessed 2026-10-11, Section 39.19-6 specifies that
`LowIndexSubgroups(G,index)` returns representatives of every subgroup
conjugacy class with index at most the supplied bound. For non-finitely-
presented inputs it iterates maximal subgroups. Section 39.19-5 supplies
the complete maximal-class interface; 39.19-3 supplies all subgroup classes
as an alternative. Thus the appropriate documented bound here is 35,
not 36. The degree bound is strict; G itself, corresponding to Q, is
included. No solvability restriction is stated for this operation.

Version-specific evidence is the complete finite-group method in
[GAP v4.15.1, lib/grplatt.gi, lines 2979-2994](https://github.com/gap-system/gap/blob/v4.15.1/lib/grplatt.gi#L2979-L2994),
read through the [raw primary file](https://raw.githubusercontent.com/gap-system/gap/v4.15.1/lib/grplatt.gi).
Its input filters are finite group and positive integer. It starts with G,
requests maximal-class representatives, filters their indices, merges
G-conjugates, and continues until its frontier is empty; the method also
has an explicit half-bound frontier cutoff. This is inspected source
coverage, not an executed or independently certified list for our group.
Any later reproduction must retain the complete frontier and justify its
stopping criterion, not assume an arbitrary depth suffices.

Alexander Hulpke, *Calculating Subgroups with GAP*,
[arXiv:2012.01595v1](https://arxiv.org/pdf/2012.01595v1), December 2, 2020,
Section 4 and Section 4.1, printed pp.15-17, describe maximal-subgroup
enumeration and bounded-index iteration with conjugacy fusion. The
inspected cases include affine actions arising from the solvable radical,
nonabelian chief factors, and the simple-group base case. Database methods
require actual isomorphisms to the input group. Section 3.2, pp.8-9,
describes the alternative cyclic-extension algorithm, including its
complete perfect-subgroup initialization and normalizer-extension step.
No timing bound in this survey is used to predict our calculation's cost.

The manual's Section 39.21-1 explicitly warns that a filtered
`LatticeByCyclicExtension` may lose wanted subgroups when their construction
passes through discarded subgroups. Do not use the small-index predicate
as an upward-construction filter. Its perfect seeds also cannot be omitted
without the stated solvability implication. Section 39.20-10 requires
PerfGrp for its perfect-subgroup interface and reports an error for
insufficient catalogue coverage. A backend error or partial lattice leaves
the target unresolved; it is not a negative result.

`command -v gap` and `command -v sage` found neither executable on this
turn's PATH. No software was installed or run. This runtime limitation
does not block the source assessment, but the later mathematical step
must establish its actual execution method. A different enumeration
implementation requires a completeness argument under this assessed
finite-group scope; an unreviewed classification shortcut does not suffice.

## Criterion reuse and the remaining specialization

Reuse the full primary theorem/proof assessment in
`drafts/literature/2026-10-11-ninety-six-two-auxiliary-generalized-relation.md`
and its independent interface review in
`drafts/literature/2026-10-11-ninety-six-two-auxiliary-obstruction-audit.md`.
Etienne, *Computing class groups by induction with generalised norm
relations*, [arXiv:2411.13124v2](https://arxiv.org/pdf/2411.13124v2),
April 23, 2025, Proposition 2.7, pp.12-15, applies to a finite group,
a target subgroup H, and a finite set of nontrivial auxiliary subgroups.
It equates generalized relation existence with a surjection from
arbitrary copies of their rational permutation modules and with complete
simple-constituent invariant coverage. The assessed field interface
allows a finite Galois overfield; normality of L96 is unnecessary.
Lemma 1.1, Proposition 1.3 and the assessed compositum/orbital-map
correspondence supply all maps, rather than one selected field trace.

Our input is precisely L055's audited group acting on all 36 pairs and
their stabilizer H. All qualifying J are nontrivial under this index
bound, and the finite subgroup set fits the theorem's scope. Subgroup
conjugacy representatives are permitted only with the full equivariant
map criterion: conjugate permutation modules are isomorphic. This
does not license deleting unequal compositum maps. No source asserts
that the missing 22-dimensional space is simple; no such assertion is
needed or approved as an assumption.

The later certificate must identify G and H against L055, record the
execution/backend version, subgroup generators and indices, and evidence
for completeness of the bounded list. For every representative it must
retain every orbital incidence map on (G/H) times (G/J), and exact
rational image-rank evidence, or a fully justified equivalent constituent
test. Report actual rank against required rank 36 and every failure.
Rank 36 with complete coverage gives an algebraic feasibility result;
rank below 36 with complete coverage parks precisely these smaller
fields in MN. Without completeness either conclusion remains unfinished.
The previous rank 14 is a control for the old pair, not the new answer.

Only the field/group specialization and exact enumeration remain to be
reproduced. No reproof of the general relation theorem is justified.
A positive result would identify auxiliary fixed fields by explicit
subgroups; usable polynomial models and unconditional arithmetic would
still need separate assessment. Preserve the GRH qualifications and
independent global gaps in the nonnormal-certification assessment.

## Search record, duplicates and unread leads

Queries used: `site.gap-system.org ConjugacyClassesSubgroups LatticeSubgroups
non solvable group all subgroups`; `generalised norm relations Etienne
2411.13124 subfields smaller degree algorithm`; `PGL(2,11) S3 fiber product
generalized norm relation permutation module`; `Alexander Hulpke Computing
subgroups non-soluble groups 2013 pdf`; `"PGL" "11" "generalised norm"`.
The searches produced no inspected theorem deciding this particular
group/target/bound. This is not evidence of novelty or nonexistence.

The source comparison differs from ATTEMPTS/020-021's failed normality
premises and ATTEMPTS/022's audited pair-specific stop. None is removed
or reopened. Etienne's Algorithm 5.4 was located but concerns optimization
of classical relations in subquotients; it is not an exhaustive subgroup
implementation or an answer to this generalized relation test.
Hulpke's references to Cannon-Holt-Slattery-Steel, *Computing subgroups
of bounded index in a finite group*, J. Symbolic Comput. 40 (2005),
1013-1022, and Bray-Holt-Roney-Dougal's classical-group maximal-subgroup
book were not read and are not imported here. A search hit titled
*PGL(2,11) and PSL(2,11)* was also unread. Exact-field subgroup or
constituent classifications from these leads remain outside this approval.

This completes one literature-only comparison. No enumeration, new lemma,
mathematical script or relation calculation was performed. The ready
continuation is recorded separately for next-turn approval.
