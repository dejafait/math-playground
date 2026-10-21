# Global triple moments — bounded principal-matrix trial

TARGET: Test whether L022's above-threshold pair assignment has a global degree-three extension with all L020-incidence triples set to zero, satisfying augmented pair PSD and every anchor-containing three-index conditioned principal matrix.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the completed unrestricted-global-triple comparison, including its five external queries and scoped failure/duplicate checks; the changed trial is not a completed L023 scalar or block diagnostic.
SOURCE_EVIDENCE: Polak https://arxiv.org/pdf/1703.05171v1 Section 1.1 (1)–(3), Proposition 1.1 and complete proof, p. 2; Brouwer–Polak https://arxiv.org/pdf/1709.02195v1 Section 2 (1), p. 2, freshly rechecked; foundations/12 records qualifications. Reuse foundations/09: https://arxiv.org/pdf/1709.09011v2 Section 3, p. 10, and https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf Sections 11.2 and Theorem 2.7.1(i). L022–L023 supply trial inputs only.
COMPARISON: Known conditioned PSD matrices cover this finite principal-submatrix test. L021 bounds pair-only strength, while L022–L023 give an above-threshold trial whose changed incidence-zero entries have not been checked. L030 and L051–L052 decide different local or fixed-pair models.
GAP: Check one complete rational trial, including its global constant coordinate, every retained conditioned principal matrix, Boolean repetitions, all pair/triple zeros and the strict integer threshold; full conditioned PSD and a uniform useful bound remain open.
REASON: A globally defined symmetric trial permits finite orbit verification without imposing symmetry on arbitrary labeled points; this is a known-method specialization with a discriminating exact outcome, not an approved full SDP solve.
SCOPE: Exactly the trial below; augmented global pair PSD, scalar moment nonnegativity and all conditioned principal matrices with indices {A,A union {B},A union {C}}. No anchor-free three-index matrices, full conditioned matrices, complement matrices, scalar Frechet additions or degree-four moments are included.

Separate source approval completed in step 168; the exact TARGET and
SPECIALIZE scope are unchanged. No mathematical attempt or trial
verification occurred in either literature turn. The main gap is arbitrary-center
68-agreement safety; 67-agreement safety remains independently open.

## Proposed diagnostic and downstream use

Let V be all 68-subsets of H and N=binomial(1024,68). Take U from L021
and the exact p_i and lambda=p_68 from L022. Use L023's formula on all
actual ordered triple orbits, without assuming PSD after modification.
Propose rho=(U+1)/(2N), x(empty)=1, x({A})=rho and
x({A,B})=rho*p_(68-|A intersection B|) for distinct A,B. On Boolean
repetitions use the lower-order coordinate, not a new variable.

For distinct A,B,C propose x({A,B,C})=rho times the L023 formula,
except set it to zero whenever the three supports have exactly L020's
incidence sizes: a 61-point common core, three pair-only two-sets and
three private points on each support. This extra-zero prescription is a
trial choice, including determinant-zero/realizable triples; it is not
imposed on every list or every feasible point. All actual forbidden
nonsingular triples must be included, with exact matching verified in
research. A failed trial is evidence about this prescription only; a
different prescription or broader model requires source review.

The proposed batch is the free-pair relaxation of the known global
order-three program retaining its empty-conditioned matrix, all scalar
nonnegative moments, pair zeros and actual L020 forbidden-triple zeros,
and precisely the anchor-containing principal matrices named in SCOPE.
The fixed p_i above are a trial for this free-pair batch, not constraints
on arbitrary lists. Research must justify the indicator specialization
and dropped-matrix relaxation using the primary source; neither has
been established as a new local theorem in this review.

Its downstream use is an economical strength test before attempting a
global labeled dual. An exact feasible trial with singleton objective
at least T=floor(65537^28/2^128)+1 stops this batch as a sufficient
certificate below T and motivates larger conditioned matrices. A failed
matrix identifies an incompatibility of this trial, not the free-pair
optimum. Either outcome leaves the 955–957 bracket unchanged.

## Complete evidence and finite bound

Build the global augmented matrix x(I union J) for empty/singleton
indices. Check all 69 Johnson spectral coordinates and the constant
Schur condition using foundations/09. The trial's normalization is an
assertion to verify, not a result of this review. For every A,B,C check
the matrix indexed by {A,A union {B},A union {C}}, removing duplicate
indices. All entries use the same global moments and Boolean repeats.
PSD needs all principal minors or an exact congruence, allowing zero
pivots and their off-diagonal obligations; a determinant alone is not
sufficient. Check scalar nonnegativity and every required zero as well.

The trial depends on incidence/intersection sizes. Verification may
enumerate the actual (i,j,t,s) domain in foundations/04 and L023, proving
that the incidence-zero translation and the enumeration are exhaustive.
This verifies a chosen invariant function directly on labeled sets; it
never averages away labeled constraints. Retain every repeated-word
case and actual orbit. L023's 1500625-orbit enumeration is a reference
scale, not certification of the changed matrices. Stop generation if
more than 2000000 ordered orbit records are needed; this planning cap
is a resource stop only.

Save full rational coefficients, failed matrices and complete PSD
evidence under scripts/finite-support/ during research. Print actual
and required counts/bounds, failures and certificate paths. Inspect
complete load-bearing values with the shared JSON inspector; a preview
or approximate eigenvalue is not proof. No mathematical script was
written or run in the literature step.

Continue only from an exact failed matrix or a fully checked feasible
trial. At-least-T feasibility stops this specified batch as a sufficient
upper certificate; it proves no full order-three feasibility, measure,
packing or RS list. Failure stops only this witness. Arithmetic or
reconstruction failure is unfinished work. A trial below T is inconclusive
for the batch optimum. Larger conditioned matrices need separate review.

Essential inputs are L001, C001a, L020, L021, L022, L023 and
foundations/04,09,12. Unresolved assumptions are global pair
normalization/PSD, exact orbit matching and complete retained-matrix
PSD. Larger conditioned matrices, label-preserving reduction, a useful
uniform upper bound and common-center realizability are not asserted.
Mathlib full matching and supporting coverage are not checked. The
calculation is REPRODUCTION of assessed methods, with no originality
claim.

## Separate approval and direct-source recovery (step 168)

LITERATURE_REASON: The supervisor requires direct source URLs in this ready assessment; this bounded recheck repairs that omission for the unchanged target.

On 11 October 2026, reopened the two immutable primary PDFs linked in
SOURCE_EVIDENCE. Read Polak's Section 1.1 definitions, equations (1)–(3),
all of Proposition 1.1's indicator proof and diagonal-nonnegativity
explanation on printed p. 2, and Section 1.2's constraint-preserving
averaging on p. 3. The displayed proposition's A(n,d) endpoint is
qualified by its proof's A(n,d,w) endpoint; no unrestricted-code bound
is imported. Read Brouwer–Polak Section 2 through equation (1), the
Johnson order-two comparison and the nonnegative-block explanation on
p. 2. These passages agree with foundations/12; no new theorem is
derived or hierarchy reproved.

The spectrum and Schur coverage in foundations/09 is reused without
fresh browsing or changed hypotheses. Its direct primary URLs are now
visible in SOURCE_EVIDENCE. The exact trial's full applicability and
PSD still require research; this approval is source coverage only.
Scoped searches of ATTEMPTS/013–015 and 033–034 confirm that the retained
stops concern unchanged old blocks/scalars or different fixed pairs,
not the changed incidence-zero trial. The earlier external discovery
and full duplicate comparison are reused, with no novelty claim.

This is STALLED as mathematical progress: direct-link repair and
separate approval supply no new bound, feasibility witness or obstruction.
The saved test is ready for one REPRODUCTION calculation turn. Its
continuation/abandonment rules and unresolved assumptions above remain
in force; no lemma or mathematical script was changed.
