# Triple-support rank diagnostic — scoped specialization for separate approval

TARGET: Establish and test an exact realizability criterion for three selected 68-agreement supports with a 61-point common core and two points in each pair-only overlap on C001a's instance, for every m>=1.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed RS-support source discovery; additionally searched three/common/intersection-matrix supports, quadratic agreement-support realizability and Shangguan 3-wise intersections. No matching local diagnostic was found; no novelty inference is made.
SOURCE_EVIDENCE: Inspected Shangguan–Tamo arXiv:1911.01502v1, Definition 4.1, Lemma 4.2 and the common-root division in Lemma 4.3; the exact source statement and remaining specialization appear below.
COMPARISON: The source supplies the scalar difference-kernel dictionary and common-root reduction; a fixed-subgroup test still must verify tuple applicability, pairwise distinctness, a converse center construction and actual specialized ranks.
GAP: Prove the exact selected-support criterion and test nonvanishing/degeneracy on the prescribed subgroup; no global packing or threshold conclusion follows without a separate counting argument.
REASON: This small configuration tests algebraic realizability beyond pairwise packing while avoiding a generic-domain assumption; no new criterion has been derived in the approval turn.

## Exact scope and input qualifications

Use C001a's n=1024, k=64, E=F_65537, F=F_(65537^28), H<=E^*
of order 1024, with all m>=1. Fix three subsets S_i of H of size 68 whose
triple intersection has size 61 and each pair-only intersection has size 2.
“Realizable” means that some received array and three pairwise distinct
degree-less-than-64 polynomial tuples agree on every column of the respective
S_i. Extra agreements are permitted. The problem concerns selected supports,
as used in C001b, rather than exact agreement sets. No fixed center, zero-row
restriction or descent of arbitrary messages to E may be assumed.

## Imported scalar input and specialization still required

Shangguan–Tamo,
[arXiv:1911.01502v1](https://arxiv.org/pdf/1911.01502v1), printed pp. 10–12,
Definition 4.1: for s>=1 the three-way matrix has first block row
[I_s I_s I_s] and diagonal Vandermonde blocks on the three pair intersections.
Its specialized kernel consists of degree-less-than-s polynomials summing
to zero and vanishing on the respective overlaps. Lemma 4.2: when the triple
intersection is empty, the pair-overlap sum is 2s, s is at most the source's
ambient message dimension, and each pair overlap has size at most s, its
determinant is a nonzero polynomial of total degree
s(s-1), each variable of degree at most s-1. This is symbolic nonvanishing.
Lemma 4.3's proof divides pairwise differences by the common-root product,
reducing degree by the common-core size.

Import this dictionary, not a new proof of the symbolic theorem. The
necessary local work is to justify the common-core reduction for simultaneous
tuples, obtain a criterion at the actual E-valued evaluation points, check
pairwise distinctness rather than merely a nonzero vector, and prove or
refute sufficiency by constructing one compatible center. Rank over E versus
F, and possible additional agreements, must be handled explicitly. These
are proposed proof obligations, not conclusions established in this review.
The source's global two-list theorem is not invoked at the 956-error radius.

## Discriminating test and downstream use

Test actual specialized rank on six distinct subgroup points representing
the pair-only overlaps. A claimed universal nonvanishing criterion must
survive subgroup symmetries, including antipodal pairs. Save full points,
matrices, ranks and any kernel; numerical sampling cannot prove universality.
An admissible singular case must pass distinct-message and common-center
tests before being called realizable. One bounded symbolic criterion and
finite diagnostic suffice for the next step; do not exhaust all subsets.

A forbidden configuration could enter an extremal support-family estimate
stronger than C001b. A realizable degeneracy would delimit such an estimate.
That counting step and the required factor exceeding 2.763 remain independent
unresolved gaps. Inputs are L001, C001a, C001b and the cited scalar dictionary;
C001a already retains C012a/L019 and the ambient threshold. No full list
maximum, scalar/tuple worst-case equality or ABF equivalence is assumed.

Mathlib matching coverage: not checked. This new ready continuation receives
separate approval on the next invocation before mathematical work; proposed
research classification is REPRODUCTION. No calculation or new lemma was
performed while writing this source assessment.
