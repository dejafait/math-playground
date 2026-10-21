# Global pair-marginal extension — source comparison completed

TARGET: Test exact feasibility of the global 68-support pair-moment extension with L030's prescribed entries at intersections 61–68, retaining the augmented constant row and nonnegative pair entries.
CHECKED: 2026-10-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Inspected the named local inputs and ATTEMPTS/011,019,021; searched Johnson spectral, prescribed distance-distribution, constant-weight moment-extension and exact 2571353 packing terms; no inspected source supplies the requested fixed-slice witness or exclusion.
SOURCE_EVIDENCE: foundations/09-global-pair-johnson-source.md records Polak v1 Sections 1.1–1.3 (https://arxiv.org/pdf/1703.05171v1), Brouwer–Polak v1 Section 2 equation (1) (https://arxiv.org/pdf/1709.02195v1), Brouwer–Cioaba–Ihringer–McGinnis v2 Sections 1.2/3 (https://arxiv.org/pdf/1709.09011v2), and Brouwer–Haemers preprint Section 11.2 and Theorem 2.7.1(i) (https://homepages.cwi.nl/~aeb/math/ipm/ipm.pdf), with inspected hypotheses, normalization and singular-case qualifications.
COMPARISON: The global pair-only cone is the known order-two constant-weight/Delsarte framework with additional fixed moments; L021's optimized value and L030's separate local distributions do not settle this affine slice.
GAP: Apply the imported spectral and Schur-complement criteria and provide either a complete exact rational global pair certificate or an exact infeasibility certificate for this prescribed assignment only.
REASON: Essential changed-universe coverage is now present; the remaining finite slice test is a known-method specialization, with no global representation, RS-list or novelty conclusion licensed.
SCOPE: The exact rho, diagonal, overlap-61/62/63 moments and overlap-64–67 zeros below; all 68-subsets of a 1024-set; free nonnegative overlap-0–60 moments; one augmented constant/singleton PSD matrix; all Johnson eigenspaces and exact rational feasibility or infeasibility certificates.

## Fixed diagnostic preserved from the reviewed target

The completed literature task was: Assess source coverage for a global
68-support pair-moment extension with L030's prescribed entries at
intersections 61–68. Only source comparison was performed. The ready
TARGET above is the concrete subsequent test; its newly changed
assessment receives separate supervisor approval before invocation.

Use L027 and L030, with the fixed 1024-point domain H and all 68-subsets S.
Keep rho=137^3/binomial(963,7), d=(2442832,125664,2856) and
N_i=binomial(7,i)binomial(956,7-i). Seek a permutation-invariant
symmetric real matrix F with singleton vector f_S=rho, diagonal
F_SS=rho, augmented matrix [[1,f^t],[f,F]] PSD and nonnegative pair
entries. For distinct S,T prescribe

- F_ST=rho*d_i/N_i if |S intersect T|=61+i, for i=0,1,2;
- F_ST=0 if |S intersect T|>=64;
- entries for |S intersect T|<=60 are free, subject to the stated constraints.

These requirements define the preserved fixed test, not an assertion
that a global extension exists. Actual labeled triple constraints and
higher-order global moments are outside this pair-only test.

Potential downstream use: exact infeasibility could detect an obstruction
to these prescribed local moments having global pair consistency. Exact
feasibility would park only this pair-consistency diagnostic. Neither
outcome alone bounds all RS lists, proves a representing distribution,
or closes 68/67-agreement safety. The original all-core local-cap stop
remains valid regardless of this test's result.

## Source applicability and necessary distinctions

Precise imported inputs, theorem/page references, versions and Mathlib
qualifications are in [foundations/09](../../foundations/09-global-pair-johnson-source.md).
Reuse the inspected [Delsarte assessment](2026-10-05-delsarte-support-certificate.md)
for L021's coefficient normalization and foundations/08 for the
indicator-moment formalism; neither requires refreshing its old scope.

Here n=1024 and w=68 satisfy n>=2w. The source's minimum Hamming
distance is 10, whereas its moment order is 2; neither is the RS
dimension 64 or interleaving width m. Distance i means intersection
68-i. Thus source relations 5,6,7 are the fixed overlap-63,62,61
coordinates; relations 1–4 are zero and relations 8–68 are free.
The source valencies are global counts binomial(68,i)binomial(956,i).
They must not be confused with L030's local N_i, which remain in the
prescribed entries. The inspected eigenvalue formula divided by its
global valency is exactly L021's q_(j,i); no sign or transpose change
is inferred from a snippet.

At source moment order two, D=empty gives precisely the constant and
singleton matrix. For |D|=1 or 2 its indexing rule gives a scalar
moment matrix. Consequently pair nonnegativity is part of the source
program, rather than a consequence assumed from the unconditioned
PSD matrix alone. The Boolean diagonal identifies x({S,S}) with
x({S}). No third/fourth moments or conditioned higher-order matrices
are imported. The source's indicator proof explains necessity for
actual packings; it does not assert that feasible pair moments have
a representing measure.

L027 restricts a support family to supports containing C and then
deletes C. This is restriction of indicators, not conditioning a
probability law on an event involving C. L030's f,F therefore prescribe
the principal entries of a hypothetical global moment matrix directly,
with no extra probability factor. When two full supports contain a
61-core, their residual intersection is their full intersection minus
61. The same fixed entry is prescribed by every common 61-core.
This checks consistency of the *specification* on overlaps; PSD and
existence remain untested. Matching pair restrictions would still
leave all cross-core higher moments unresolved.

The pair diagnostic omits actual determinant labels. Its fixed entries,
diagonal and zero pattern are invariant under all permutations of the
1024 underlying positions. The inspected averaging argument therefore
applies to this diagnostic without changing the fixed entries. It is
not licensed for a labeled triple-constrained global model or used to
turn an arbitrary RS list into a list with these prescribed moments.
The chosen constant singleton rho is an extra hypothesis of this
slice: no existing result forces every list to have it.

The future implementation must apply the source's common spectral
decomposition to every eigenspace and the Schur-complement criterion
with leading block [1]. In particular it must check the constant
eigenspace of F-rho^2 J, rather than merely check F PSD or the 68
nonconstant Delsarte inequalities. Singular eigenspaces are allowed;
no strict-PD assumption, lower-block inverse or division by a zero
eigenvalue is approved. The specific reduced system and its exact
feasibility are to be justified in the research turn, not asserted
as a new result of this source review.

## Duplicate, failure and search evidence

Read L021's statement and complete finite LP proof; L027's
hypotheses, conclusion and selected-support restriction; L030's
hypotheses, conclusion and complete pair-moment computation.
Narrow duplicate checks of the shared-moment assessments and
ATTEMPTS/011,019,021 found no completed global fixed-slice test.
L021's unrestricted optimum cannot be substituted for a fixed
distance subvector. ATTEMPTS/011's LP stop is retained: this task
tests compatibility of a specified witness, not renewed optimization
of the old upper certificate. ATTEMPTS/019–021 retain their local-cap
obstructions irrespective of the new diagnostic's outcome.

External queries on 7 October 2026 included:

- `Johnson scheme adjacency eigenvalues Eberlein polynomial constant weight Delsarte semidefinite theta matrix`
- `Polak semidefinite programming bounds constant weight codes A2 Delsarte 1703.05171`
- `Delsarte thesis 1973 algebraic approach association schemes coding theory Theorem 4.6 pdf`
- `Schrijver Delsarte bound theta prime Johnson scheme positive semidefinite augmented matrix`
- `"smallest eigenvalues" "Johnson" "Brouwer" arxiv 2018`
- `"Johnson scheme" "prescribed" "distance distribution" positive semidefinite`
- `"constant weight codes" "moment" "extension" "Delsarte"`
- `"2571353" "packing" "137"`

The readable primary passages actually inspected are those in
foundations/09. The strongest relevant inspected conclusion is the
standard Johnson spectral/moment framework and the order-two
Delsarte comparison, not existence or nonexistence for this slice.
Source tables and asymptotic bounds were not applied. Delsarte's
restricted original thesis, Karloff's original theorem, de Laat's
thesis returned by search and other search-only leads were not read
and are not essential inputs. The guessed CWI Delsarte URL, old
Eindhoven book URL and PMC browser-check failure were bypassed by
the inspected arXiv and author-hosted sources. There is no essential
remaining access blocker. Failed searches do not establish novelty.

## Bounded subsequent test and decision rule

Essential mathematical inputs are L027, L030 and L021. The main gap
remains arbitrary-center safety at 68/67 agreements. The intermediate
target is exactly this fixed global pair extension; its plausible use
is to test a compatibility requirement absent from the local model.

Import the scheme and Schur-complement theorems, verifying only the
needed finite specialization. Reproving either standard theory is
unnecessary. A solver may discover a witness, but the subsequent
research turn must save full exact rational data and check every
fixed coordinate, nonnegative free coordinate, spectral inequality
and augmented constant-coordinate condition. An infeasibility claim
needs a complete exact dual/Farkas certificate or a proved obstruction,
not a solver status. Compare any reported objective with the ambient
threshold 65537^28/2^128 without treating the slice as a list bound.

Feasibility parks this pair-only diagnostic. Infeasibility excludes
only this fixed assignment and may motivate a separately assessed
different marginal target. Neither establishes a representing
distribution, rules out other local moment choices, improves the
local exact-cap stop, proves unsafety/safety, settles the earlier full
SDP or resolves ABF equivalence. Reconstruction failure is unresolved
work, not mathematical exhaustion. No calculation, lemma, mathematical
script or complete-solution candidate was produced in this review.
