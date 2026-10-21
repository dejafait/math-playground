# Triple-distance semidefinite certificate — source review

TARGET: Test whether the Schrijver triple-distance semidefinite bound for A(1024,10,68) certifies B_m(956/1024)<=65537^28/2^128, using an exact certificate.
CHECKED: 2026-10-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched Schrijver constant-weight/Terwilliger SDP, the exact A(1024,10,68) string, large-parameter implementations and stronger constant-weight bounds; scoped local searches found L021's pair-LP stop and L020's failed universal exclusion, with no earlier SDP test. No matching finite-instance certificate was found; this is not an absence or novelty claim.
SOURCE_EVIDENCE: Read Schrijver 2005 author manuscript equation (7), Proposition 5/Theorem 1 and Section III.A–B (52)–(67), pp. 2,5–7; cross-checked Kim–Toan arXiv:1212.3467v1 III.B (31)–(35), pp. 8–9, III.C.2 (40), p. 10; read Polak arXiv:1703.05171v1 Introduction, 1.1 definitions (1)–(3), Proposition 1.1/proof, pp. 1–2.
COMPARISON: The standard constant-weight SDP applies to the existing selected-support dictionary, with objective including the diagonal 1; its two PSD families and triple-orbit parameter t-s add joint constraints beyond L021. No inspected theorem or table supplies the value for (1024,10,68); four-word bounds are stronger but substantially larger and are not part of this test.
GAP: Implement and verify a bounded selected-block certificate test; effective finite-instance improvement and exact PSD feasibility are unknown. Failure of a selected-block relaxation is not failure of the full Schrijver SDP or evidence of actual unsafety.
REASON: Essential theorem coverage is now available; the remaining work is finite specialization of a known method, not a new general SDP theorem or another basic-LP optimization.
SCOPE: Parameters (1024,10,68), existing uniform-in-m support selection, exact rational coefficients and certificates; first test only the explicitly selected blocks and scalar orbit constraints below, retaining all basic pair-LP inequalities. No full-scale SDP solve or enhanced four-word/RS determinant constraints is authorized by this assessment.

Main gap: arbitrary-center safety at 68 agreements. Proposed intermediate
target: an exact feasible upper certificate using standard joint-distance
semidefinite constraints, rather than another pair-distance LP. Downstream
use would be the same uniform-in-m support selection from L001/C001a.
No improved bound, feasible matrix, or applicability is assumed.

Essential continuation inputs are L001, C001a and L021; C001a retains
C012a/L019. C001b and L020 are comparison evidence, not additional SDP
constraints. Preserve C001b's nested-floor stop and L020's degeneracies.
Extra agreements are allowed; scalar/tuple equality, an exponent m,
determinant-density transfer and an actual packing of LP-optimal size are
not assumed. Safety at 67 agreements, sharpness and ABF equivalence remain
unresolved independently.

## Imported source and applicability

The full cited input, hypotheses, formulas and source qualifications are
in [the source note](../../foundations/04-constant-weight-triple-sdp-source.md).
Schrijver, IEEE Trans. Inform. Theory 51 (2005), 2859–2866,
[author manuscript](https://homepages.cwi.nl/~lex/files/codes.pdf),
Section III.B (64)–(67), is the actual constant-weight bound; Theorem 1
alone is a block diagonalization, not the complete code-size theorem.
The binary unrestricted-code SDP is not substituted for it.

Reuse L021's proved support dictionary: selecting 68 agreement columns
per candidate gives distinct weight-68 incidence vectors of length 1024
with distance >=10. Extra agreements remain allowed. Here v=956 and
10<136<=1024, checking also Kim–Toan's even-distance convention.
The binary code is the support family, not the received-word alphabet.
Any valid upper certificate applies to the whole tuple list without m
in the exponent. The objective is 1+sum a_i, where
a_i=binom(68,i)binom(956,i)p_i, i=5,...,68; p_0=1 and p_1,...,p_4=0.
Kim–Toan (40), rather than an assumed conversion, supplies this dictionary.
No new support theorem is derived in this literature step.

The source uses k for a block index; it is unrelated to RS dimension 64.
Triple-orbit normalization requires both multinomials nonzero. Permuting
pair distances must preserve t-s. Both PSD families are essential to the
full SDP. Keep the source note's qualifications about impossible indices
and the unused printed complement prefactor; no source identity is silently
repaired. The inspected block statements, corroborated independently in
Kim–Toan, suffice for the planned specialization.

## Bounded first certificate test

The complete source has O(w^4) variables, not the O(n^3) unrestricted-code
variable count. Polynomial complexity alone does not make this instance
a one-step computation. The first research invocation should construct
a relaxation using the following fixed batch, then test it once:

- Both source PSD families for (block k,block l)=(33,33), with their full
  index set {33,34,35}, and (34,34), with index set {34}.
- Both principal submatrices of the (0,0) blocks on indices {0,5,6,68}.
- All 68 basic Delsarte pair inequalities from L021, all pair variables,
  and the source's normalization, nonnegativity, upper/lower orbit
  inequalities, permutation equalities and distance zeros on the triple
  orbits touched by this batch (including their permutation closure).

This specifies selected necessary constraints, not a claim to have computed
the full SDP. Dropping other constraints must be explicitly justified in
the research write-up as a relaxation. Do not set omitted triple variables
to zero or assume that a partial feasible witness extends to all blocks.
Check the exact coefficient dictionaries and source indices before solving.
Use a finite construction cap of 20000 retained orbit variables and 200000
scalar rows after symmetry reduction; exceedance parks this batch as a
resource limitation, without a mathematical impossibility claim. These
caps are planning limits, not computed counts. No enumeration was run here.

Numerical discovery, if available locally, is only a way to find witnesses.
A valid upper certificate must supply rational nonnegative scalar
multipliers and rational PSD dual matrices, an exact coefficient identity
bounding the objective on every retained variable, and
2^128 U<=65537^28 (or the valid integer-floor comparison).
An exact congruence/LDL certificate must handle singular PSD matrices,
including zero pivots and their off-diagonal obligations; approximate
eigenvalues or determinants alone do not prove PSD. Independent arithmetic
verification must inspect every identity, sign and PSD factor in full.

Alternatively, an exact feasible rational primal assignment with objective
above threshold rules out a sufficient upper certificate from this batch.
It need not be an actual code, an RS list, or feasible for the omitted
Schrijver constraints. L021's pair witness is comparison evidence, not an
assumed feasible triple lift. Preserve full certificates under
scripts/finite-support/ in the future research turn, printing actual and
required bounds, failures and paths. No script or lemma was written now.

Continue this batch if an exact upper certificate decides index 956 or a
verified improvement supplies a concrete discriminating next block test.
Stop it as a threshold certificate if an exactly feasible primal objective
exceeds threshold; report only that batch's limitation. A solver failure
is unfinished work, and any broader block batch needs its own approved
scope. No conclusion on the full SDP follows from this bounded failure.
67-agreement safety, the RS determinant-density transfer, sharpness and
ABF equivalence remain independent gaps. Full matching Mathlib coverage:
not checked.

## Stronger known comparisons and source access

Sven C. Polak, [Semidefinite programming bounds for constant weight codes](https://arxiv.org/pdf/1703.05171v1),
v1, 15 March 2017, Introduction and Section 1.1, pp. 1–2,
defines A_4 and B_4 using at most four words, with PSD moment matrices
indexed by small subcodes. Proposition 1.1's code-indicator proof establishes
the upper-bound mechanism; its printed final A(n,d) omits w, whereas its
proof explicitly concerns the constant-weight code. No unrestricted-code
conclusion is imported from that typographical omission. The introduction
states these bounds sharpen Schrijver, and 1.1 warns that the reduced
programs remain large. Four-word block formulas and later proof cases
were not read and are not approved inputs. Kim–Toan's later enhanced
inequalities and quadruple SDP implementations remain separate leads.

Actual searches included `Schrijver new code upper bounds Terwilliger
algebra constant weight codes semidefinite 2005 pdf`, `"A(1024,10,68)"`,
and `Schrijver constant weight semidefinite bound large n fixed w
implementation exact certificate`. Results and small-parameter tables
supplied no certificate at the target parameters; no novelty is inferred.
Local comparison reused the ready Delsarte assessment and read
ATTEMPTS/010–011 and the extremal-transfer assessment. L020's antipodal
triples prohibit a universal pattern exclusion, but do not prohibit the
standard coding SDP. Its determinant adds no constraint in this test.

Primary PDFs and essential proof cases were accessible through the web
reader. Shell downloads failed at DNS resolution; no local PDF snapshot
or checksum is claimed. This is not missing theorem coverage: the actual
read passages and formulas are recorded above. The existing saved target
is now assessed for a REPRODUCTION research step within the stated batch;
no finite certificate, new extremal result or complete solution is claimed.
