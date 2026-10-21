# Mixed zero/one blocks — approved fixed-assignment diagnostic

TARGET: Test L022's unchanged assignment against both full (0,1) Schrijver blocks for A(1024,10,68), with exact PSD or negative-quadratic certificates.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-instance, standard terminology and stronger-result searches in 2026-10-05-triple-distance-sdp-certificate.md; scoped searches and reads of L022/L023, their working records, history/042–045 and ATTEMPTS/012–013 found no completed mixed-(0,1) diagnostic.
SOURCE_EVIDENCE: Directly inspected Schrijver's eight-page author manuscript III.A (55)–(58), pp. 6–7, and III.B (60)–(65), p. 7; directly corroborated complete index ranges and both affine PSD families in Kim–Toan arXiv:1212.3467v1 III.B (32)–(35), printed p. 9; canonical source input remains foundations/04.
COMPARISON: The known tensor decomposition supplies this distinct mixed block; L022 tests (33,33), (34,34) and selected (0,0) entries, and L023 tests full (0,0) only. Neither canonical result evaluates (0,1). No inspected source gives this assignment's mixed signs or a finite-instance threshold certificate.
GAP: Evaluate the two full mixed matrices exactly for the unchanged prescribed assignment and independently certify their signs; possible exclusion of this extension and full-SDP feasibility remain unknown.
REASON: Essential mixed-index source coverage and duplicate comparison are now complete; the remaining step is finite reproduction of known constraints, without a new general theorem or optimization.
SCOPE: Only (block k,block l)=(0,1), n=1024, w=68, v=956, d=10, L022's pair values and its prescribed extension formula; both full matrices on indices 1,...,68. No additional blocks, assignment tuning, full scalar feasibility or SDP solve.
LITERATURE_REASON: The saved target changes the tensor component from (0,0) to (0,1), outside prior approved scope; this separate review checks essential complete-index and normalization coverage.

## Source scope and qualifications

Alexander Schrijver, *New code upper bounds from the Terwilliger algebra
and semidefinite programming*, IEEE Trans. Inform. Theory 51 (2005),
2859–2866, DOI 10.1109/TIT.2005.851748,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
III.A (55)–(58), gives W_k={k,...,w-k}, V_l={l,...,v-l}
and deletion to their intersection. Its (58) uses positive diagonal
rescaling; III.B (64) gives the unscaled beta-product PSD tests.
The (60)–(63) construction retains repeated words and actual multinomial
orbits. Preserve foundations/04's unused printed (61) prefactor
qualification rather than reconstructing it. The mixed component is a
different tensor label, not a principal submatrix obtained merely by
deleting index zero from the (0,0) matrices. This does not predict its sign
on the restricted fixed assignment or prove independence within that ansatz.

Hyun Kwang Kim and Phan Thanh Toan,
[Improved Semidefinite Programming Bound on Sizes of Codes](https://arxiv.org/pdf/1212.3467v1),
v1, 14 December 2012, III.B (32)–(35), printed p. 9, independently
states both families with entries summing beta_(ij,k)^(t,w)
beta_(ij,l)^(s,v) times respectively y_(ij)^(t,s) and
p_(i+j-t-s)-y_(ij)^(t,s). For (0,1), the intersection is
{0,...,68} intersect {1,...,955}={1,...,68}.
Both source statements apply to binary constant-weight codes;
10 is even and 0<10<136<=1024. The existing L001/L021 support
interpretation, uniformly in m and allowing extra agreements, is reused.
No source theorem is reproved. Mathlib matching coverage remains not checked.

The prior assessment's four-word and enhanced inequalities remain stronger
unimported comparisons; their unread details are not approved here. Exact
instance searches previously found no matching certificate, without proving
absence or novelty. One screenshot request for Kim–Toan p. 8 timed out;
the essential p. 9 text and formulas were accessible. There is no essential
source blocker and no claimed local PDF checksum.

## Bounded test and decision

Main gap: arbitrary-center safety at 68 agreements, with safety at 67
agreements independent. Intermediate target: decide the signs of these
two fixed mixed matrices. Downstream use: a negative rational quadratic
would expose a missing constraint excluding this particular above-threshold
extension and inform a later strengthened support-bound attempt. It would
not give an upper certificate or exclude every extension.

Essential inputs are L001, C001a, L021, L022, L023 and foundations/04;
C001a retains C012a/L019. Preserve L022's assignment branches in order:
forbidden distances, repeated words, then p_i p_j p_h/p_68 with
h=i+j-t-s. Use the actual admissible orbit ranges recorded in L023;
retain original indices and distinct t-s orbit identities. Reconstruct
source coefficients and verify overlaps with the existing extension.
The new matrices may use old orbit values with different coefficients;
nonduplication is a constraint change, not a claim of new variables.

Save both full matrices before sign testing. A successful negative result
requires an exact rational vector and a fully reconstructed negative
quadratic value, not a negative elimination pivot alone. PSD requires a
complete exact invertible congruence to a nonnegative diagonal, including
zero residual rows. An independent verifier must reconstruct every entry
and check every load-bearing identity and sign; previews and numerical
eigenvalues are insufficient. Preserve full certificates under
scripts/finite-support/ in the future research turn.

Continue only on a verified exclusion with a concrete constraint-based
follow-up. If both pass, park this mixed diagnostic and reassess repeated
fixed-assignment block tests before choosing any further block. A resource
failure is unfinished work, not a sign result. No optimization, tuning or
additional constraint family is approved. L022's selected-batch stop and
L023's full-zero stop remain intact; the unchanged objective is above T.
Full scalar/SDP feasibility, actual packing or RS list realization,
interleaving sharpness, ABF equivalence and the 955–957 bracket remain
unresolved. This review is EXPLORATION with NOVELTY_UNCHECKED, approving
a subsequent REPRODUCTION calculation; no matrices or new lemmas were derived.
