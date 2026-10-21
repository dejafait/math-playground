# Full scalar extension diagnostic — source scope approved

TARGET: Test L022's unchanged extension against all Schrijver scalar orbit constraints for A(1024,10,68), with an exact exhaustive certificate.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-instance, standard-terminology and stronger-bound searches recorded in 2026-10-05-triple-distance-sdp-certificate.md; scoped reads of L022–L024, selected/full-zero implementation ranges, ATTEMPTS/012–014 and the corresponding working records found touched-closure scalar checks but no completed full scalar audit.
SOURCE_EVIDENCE: Directly read Schrijver 2005 author manuscript III.B (60), (62)–(67) and the explanation following (65), printed p. 7; corroborated normalization, impossible-orbit convention, complete scalar conditions and hypotheses in Kim–Toan arXiv:1212.3467v1 III.A Remark 11 and III.B (31)–(35), printed pp. 8–9. Canonical imported statement remains foundations/04.
COMPARISON: The known scalar conditions apply to all actual triple orbits. L022 checks only the closure touched by three selected blocks and pair variables; L023/L024 reconstruct additional matrices but explicitly leave additional scalar rows unchecked. No inspected result supplies full scalar feasibility for this assignment or the finite-instance threshold.
GAP: Exhaustively evaluate the unchanged assignment on every actual ordered orbit, independently check scope and all signs/equalities, and verify agreement with the old certificates; no scalar calculation or new mathematical claim is completed by this assessment.
REASON: Essential full-orbit source coverage and duplicate comparison are complete; the next step is finite reproduction of known necessary constraints, without reproof, optimization or additional PSD blocks.
SCOPE: Only n=1024, w=68, v=956, d=10, unchanged L022 pair values and L023/L024 extension; all actual ordered scalar orbits including repeated words and forbidden distances. No assignment tuning, enhanced Kim–Toan inequalities, PSD-block calculation or SDP solve.
LITERATURE_REASON: Full scalar orbit feasibility is an essential unassessed target after the fixed-extension zero and mixed PSD diagnostics pass; its scope differs from the selected touched closure.

## Primary statement and qualifications

Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE Trans. Inform. Theory 51 (2005),
2859–2866, DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.B (65), printed p. 7, supplies normalization, the three scalar
slacks, distance-permutation equalities preserving t-s, and forbidden
nonzero distances. The explanation following (65) derives the inequalities
from averaged indicator matrices and the equalities from triple counts.
The triple normalization is (62)–(63); repeated words belong to C^3.
No local reproof is required.

Hyun Kwang Kim and Phan Thanh Toan,
[Improved Semidefinite Programming Bound on Sizes of Codes](https://arxiv.org/pdf/1212.3467v1),
v1, 14 December 2012, III.B (31) and conditions (i)–(iv) following
(35), printed pp. 8–9, corroborate these conditions. The paragraph
following (31) explicitly sets coefficients of impossible multinomial
orbits to zero. Such indices are not additional scalar variables; retain
the actual-orbit interpretation and unused Schrijver (61) prefactor
qualification in foundations/04. Remark 11 permits even d>=4 and
d<2w<=n. Here 10 is even and 4<=10<136<=1024, with v=956.
No linearity or RS-alphabet hypothesis enters this binary-code statement.

The stronger-result comparison and searches in the earlier SDP assessment
remain adequate: the target is a fixed assignment diagnostic, not a new
code-size theorem. Enhanced inequalities and four-word bounds are outside
scope; their full implementation formulas remain unread leads. No novelty
or source absence is inferred. Mathlib full matching coverage remains
not checked. Primary PDF text was accessible; no local PDF checksum is
claimed. There is no essential source blocker.

## Exact scope and duplicate check

Use the already recorded L023 orbit ranges, for every ordered i,j in
{0,...,68}, retaining the original (i,j,t,s), h=i+j-t-s and u=t-s.
The future generator must enumerate those ranges in full; its independent
auditor must use nonnegative parts of both source multinomials, rather
than trusting the generator's range or a stored success flag.

For each actual orbit check the source slacks y, p_i-y and
1+y-p_i-p_j, normalization p_0=1, all prescribed forbidden-distance
zeros, and all source permutation equalities. Retain the branch order:
forbidden first, repeated second, product third. Reconstruct p_i from
L022's specified L021 witness and require lambda=p_68>0. Repeated words
include pair variables and the all-zero orbit; do not apply the product
branch to them or suppress zero-distance cases.

The selected generator's BATCH is (33,33) on {33,34,35}, (34,34) on
{34}, and (0,0) on {0,5,6,68}. Its touched set adds all pair classes,
then takes canonical keys (sorted(i,j,h),u) and their permutation closure.
L022's 7093 classes and 30856 actual closure indices are the prior scalar
scope, not a full-domain count. Its 68805 scalar rows include reduced
repetitions. L023's full zero matrices cover actual orbits but sum their
weighted values; neither those sums nor L024's mixed signs check the
individual scalar slacks. The previous stops therefore remain intact.

Distance-only identification is not approved as a variable reduction.
For source equalities retain keys (sorted(i,j,h),u); if using their closure,
independently verify all source permutations and original indices.
The preferred audit simply checks every ordered actual orbit. Caching
identical rational evaluations is allowed because the prescribed formula
already depends only on the three distances, but it must never erase
orbit coverage or impose equalities absent from the source. A compressed
certificate must retain lossless source ranges and the exact value/slack
records needed for every row, with independently regenerated coverage,
counts and mappings. A digest, preview, sample or extrema alone is not
an exhaustive proof. Verify every overlapping old value and scalar row;
report newly covered rows separately from repetitions.

## Bounded continuation and decision test

Main gap: arbitrary-center safety at 68 agreements. Intermediate target:
decide full scalar feasibility of this one unchanged extension. Plausible
downstream use: a verified violation exposes a necessary constraint missing
from the selected batch and could guide a later strengthened support-bound
attempt. It excludes only this extension, not all completions or assignments.

Essential inputs: L022, L023, L024 and foundations/04; retain
L001/C001a/L021 and C001a's C012a/L019 threshold context. The objective
remains M=(U+1)/2, above 1.383T even after the existing floor comparison,
with T=65537^28/2^128. Do not retune any pair or triple value. This review
approves one exhaustive scalar diagnostic only.

Save full exact evidence under scripts/finite-support/ before interpretation.
An independent verifier must reconstruct all pair values, assignments,
admissible orbits and required permutations, and check every rational sign
or equality. A violation requires its actual original orbit, exact slack
(or equality residual) and independently reconstructed value. If all rows
pass, certify complete coverage and park scalar exclusion; do not repeat
this assignment's diagnostics without a new mechanism. A resource failure
is unfinished work, not either mathematical outcome. Print outcomes,
actual/required threshold comparison, failures and certificate paths.

Full SDP feasibility, actual packing or RS-list realization, scalar/tuple
equality, an exponent m, sharpness, 67-agreement safety and ABF equivalence
remain independent unresolved assumptions or gaps. No general upper bound
or new lemma is approved here. This literature step is EXPLORATION with
NOVELTY_UNCHECKED; the approved next research classification is REPRODUCTION.
