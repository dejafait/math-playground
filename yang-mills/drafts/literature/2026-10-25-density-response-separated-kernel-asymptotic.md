# Complete density response — separated-kernel source assessment

TARGET: Determine the leading mesh scale of Tr(D G_{-+}) in L280(20) from the exact separated-support relative kernels, testing whether N^{-2} Tr(D G_{-+}) converges to a finite nonzero limit while retaining both density determinants and every normal link.
CHECKED: 2026-10-25
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded searches on 2026-10-25 for finite-domain lattice Green convergence, relative Dirichlet/Neumann kernels, composed Toeplitz traces and boundary Faddeev–Popov densities found scalar inputs and scope exclusions, not a theorem for this complete trace; reused the local quotient/transverse reviews and checked the distinct forest-Haar target and ATTEMPTS/048–049.
SOURCE_EVIDENCE: Reused prior precise interval/scalar coverage; inspected Dowker 1207.2096v2 sections 7–8 (29)–(37), pp. 10–13, and section 14 p. 22; Lawler–Limic (2010) Theorem 4.3.1 pp. 81–82 and Proposition 4.6.2(a) p. 97 with its transient proof; Ginovyan–Sahakyan 1405.3568v1 definitions (1)–(9), Theorems 1–3 p. 6 and proofs of 1–2 pp. 8–9; Michta–Slade ALEA 19 (2022), Theorem 1.3(ii) p. 962, (1.4), Lemma 2.1 and section 4 pp. 972–974 including Lemmas 4.1–4.2. Exact applicability limits follow.
COMPARISON: Exact scalar interval kernels and full-space scalar asymptotics cover tools for a direct finite-domain test, not its composed relative trace. The massless inverse-square full-space theorem excludes dimension four; Toeplitz hypotheses do not cover the boundary-dependent matrix. No inspected theorem supplies the N^2 scale, limit or sign.
GAP: Uniform summation with coincident density anchors, all faces and normal endpoints, complete projected kernels and both determinant terms remains unproved; separation of the two sources alone does not verify those summation hypotheses. The proposed normalization and nonvanishing are tests, not premises.
REASON: Approve one direct exploratory attempt on the unchanged finite-domain target using L003 L279 L280 and the inspected scalar tools; no inaccessible source is essential to that attempt. A bulk replacement, derivative-limit interchange or boundary error must be justified mathematically before use. No new lemma or calculation is supplied by this review.
LITERATURE_REASON: The newly registered density-only asymptotic lies outside the ready full-coefficient growth assessment; its composed-kernel and boundary scope required separate approval. This completes that approval without repeating the stopped mechanisms.
SCOPE: Exactly TARGET for SU(2), even N>=2, a=8/N, fixed cube, L003's real f_*, all boundary-contained pins, boundary-fixed gauge transformations, every variable normal link and L280's complete density; no forest transfer, translation-invariant substitution or asserted continuum limit.

## Original proposal (retained; gate superseded below)

Essential inputs are L003's relative quadratic law and modes, L279's
exact reflected-pair interpretation, and L280(16)–(20), including both
determinant terms in D. Keep SU(2), even N, a=8/N, the fixed cube,
real nonnegative f_*, all boundary-contained pins, boundary-fixed gauge
transformations and every variable normal link. No translation-invariant
replacement, scalar-only matching or nonlinear transport is allowed.

This is a materially different proposed mechanism: use actual spatial
separation and position-space kernels to diagnose a fixed signed density
family. It neither repeats the global norm bound of ATTEMPTS/048 nor
uses gauge identities as a cancellation theorem, stopped in ATTEMPTS/049.
No leading scale, sign, convergence or nonvanishing is being assumed.
If a nonzero N^2 term were established, it would identify a quantitative
term that the action and insertion families must cancel in the full
logarithmic target; it would not refute that target. A vanishing rescaled
limit alone would not prove the density response logarithmic.

The registration required comparison of exact statements and proof cases
for relative lattice Green kernels and the required composed traces,
reusing adequate prior boundary comparisons, and checks for duplicates
and failures before approval. It permitted only an explicit finite-domain
summation test with all density terms present. A bulk kernel preview or
an unspecified boundary error is inadequate. The proposed normalization
remains uncertain; it must not be silently asserted or changed.

The preceding proposal was registered with REVIEW_REQUIRED before this
invocation. The completed comparison below supersedes that gate status;
the target, its hypotheses and its uncertainty are preserved. This
literature turn spends no mathematical exploration turn.

## Completed comparison: primary statements and essential cases

J. S. Dowker, *Heat-kernels on the discrete circle and interval*,
[1207.2096v2, 31 August 2012](https://arxiv.org/pdf/1207.2096v2),
sections 7–8, printed pp. 10–13, (29)–(37), gives the scalar kernels:
Dirichlet endpoints 0,p with p-1 interior values; Neumann free indices
1,...,p with mirrors at 1/2,p+1/2 and a constant mode. The image/mode
equivalence retains the half-integer shift. These cases match the
interval conventions already justified in L003, taking p=N and shifting
the edge index by one. Section 14, p. 22, allows Cartesian products but
explicitly leaves the continuum limit untreated. Reuse these identities
by citation, without reproof; they do not state the required trace limit.

G. F. Lawler and V. Limic, *Random Walk: A Modern Introduction*
(Cambridge, 2010), [author-hosted 289-page PDF](https://www.math.uchicago.edu/~lawler/srwbook.pdf),
Theorem 4.3.1, pp. 81–82, covers symmetric finite-range irreducible
walks in transient dimensions, with leading inverse-power Green term
and O(|x|^-d) error. Its simple-walk and bipartite passages are explicit.
Proposition 4.6.2(a), p. 97, subtracts the exit Green expectation for
any lattice subset; its proof splits visits at the exit time. These
are scalar whole-space and killed-domain statements. The walk/resolvent
normalization must be matched to the unscaled incidence before use;
the three-dimensional normalization in older notebook applications
cannot be copied into this four-dimensional problem. Neither statement
estimates the projected relative composed trace or removes its boundary
term. Earlier full proof-case coverage is reused, not rederived.

M. S. Ginovyan and A. A. Sahakyan, *On the trace approximations of
products of Toeplitz matrices*, Stat. Probab. Lett. **83** (2013),
753–760, [1405.3568v1, 14 May 2014](https://arxiv.org/pdf/1405.3568v1),
(1)–(9), pp. 2–3, treats scalar Toeplitz matrices generated by integrable
real even symbols on [-pi,pi]. Theorem 1, p. 6, assumes a Holder bound
of exponent gamma in (0,1] for the four-symbol correlation at zero and
gives error O(n^(-gamma+epsilon)) in the normalized trace of
[T_n(f)T_n(g)]^2. Theorem 2 assumes f in Lip(p,gamma), g in
Lip(q,gamma), with 1/p+1/q<=1/2; Theorem 3 treats differentiated
power-singular symbols with alpha_1+alpha_2<1/2. The proofs of 1–2,
pp. 8–9, use scalar Dirichlet-kernel integration and Holder's inequality.
No verified identification makes the finite relative matrices with
spatially varying sources a member of this class. This theorem is
therefore a scope comparison, not an import for the target.

E. Michta and G. Slade, *Asymptotic behaviour of the lattice Green
function*, ALEA **19** (2022), 957–981,
[published primary PDF](https://alea.impa.br/articles/v19/19-38.pdf),
DOI 10.30757/ALEA.v19-38, (1.4) and Theorem 1.3(ii), p. 962,
concerns the q-th power of the whole-space normalized nearest-neighbor
resolvent. For d>=1, q>0, fixed nonzero integer x and source mass s/n,
it gives n^(d-2q) C_(s/n)^(q)(nx) tending to the continuum kernel.
The massless case s=0 requires d>2q. Section 4, pp. 972–974,
(4.5)–(4.19) and Lemmas 4.1–4.2, proves dominated convergence using
separate short/long-time bounds; coordinates equal to zero are treated,
but x itself stays nonzero. Consequently d=4,q=1 is within its scalar
massless scope, whereas d=4,q=2 is not. Here the source's mass symbol
is unrelated to notebook mesh a. This supplies no termwise replacement
for L280(23)'s finite B Delta^-2 B* or uniform coincident-anchor trace
limit. Keep the finite gap and differences together; no divergence of
our finite projected expression is inferred.

The last comparison is a new relevant lead; the earlier three reuse
the notebook's ready scalar/trace assessments with the exact target
boundary checked. These references authorize scalar imports with their
hypotheses, not a reproof of known kernel identities. Any actual import
or new specialization used in research must be stated in its canonical
lemma with the surviving qualifications. No theorem here resolves the
complete density asymptotic or establishes originality of that question.

## Duplicates, prior failures and search record

Read L003's hypotheses and relative modes, L280's hypotheses, density
proof and complete section 7 before source comparison. Essential input
IDs are L003 L279 L280. The exact D, source inverse derivatives and
finite Hodge decomposition are already recorded in L280(16)–(23);
extracting them again would be duplicate work. Scoped searches of
the two transverse work notes and histories 489–491 found the existing
norm bound and this proposed handoff, not a completed asymptotic.

Reuse `2026-10-23-co-closed-response-rate-critical-audit.md` for the
scalar interval conventions, `2026-10-17-first-pair-quantitative-rate-critical-audit.md`
for the transient/killed Green cases, and
`2026-10-18-h-static-trace-column-rate-critical-audit.md` for the
Toeplitz exclusion. Their other lemma conclusions are not inputs here.
`2026-10-12-coordinate-haar-cubic-scale.md` concerns L018's different
forest Ward response: its measure vertex does not equal the present
complete quotient density. Its isolated-density invariance warning is
retained; this target makes no slice-independent claim.

ATTEMPTS/048 records only an insufficient O(N^2 sqrt(log(eN))) upper
estimate. It is not a reason to posit an N^2 asymptotic. ATTEMPTS/049's
nonlocal invariant comparison blocks gauge identities as a growth
theorem, not this Wilson-specific separated-kernel test. The prior
forest integration-by-parts stop remains in ATTEMPTS/047. None of
these results supplies a lower bound for the actual density response.
The transverse review's bulk renormalization, continuum half-space and
slab exclusions are reused unchanged. The old inaccessible 1986
boundary-ghost lead stays parked; its result is not needed or assumed.

New bounded queries included:

- `"lattice" "Green function" "bounded domain" "derivatives" convergence`
- `"discrete" "Green function" "Neumann" "Dirichlet" "asymptotics" rectangle`
- `"discrete Green function" "convergence" "derivatives" lattice domain`
- `"Faddeev-Popov" "finite lattice" "boundary" "determinant" perturbation`
- `"Heat-kernels on the discrete circle and interval" Dowker`
- `"trace approximations" "products of Toeplitz" Ginovyan Sahakyan`
- `Michta Slade Asymptotic behaviour lattice Green function arxiv`

Search snippets and secondary pages served only as discovery aids.
Immersed-boundary, planar discrete-complex-analysis, massive-propagator
and generic ghost-vertex hits were not inspected theorem inputs.
Michta–Slade's references to polyharmonic and torus work remain unread
leads. No essential access blocker remains for the proposed direct
finite-dimensional attempt. This is a bounded search, not a novelty
certification or an assertion that no stronger theorem exists.

## Approved bounded attempt and stopping test

Continue with exactly TARGET after the supervisor's separate approval
of this newly ready assessment. Use the actual finite matrices and
L003's modes to test the entire density trace. Keep the all-link Haar,
diagonal P and J_ef J_fe contributions of L280(16), their three colors,
and both source orders in (18). The test must identify all internal
summation anchors and treat diagonal/near-diagonal positions, separated
source supports, boundary layers, face intersections and both normal
endpoint signs. Source separation alone is not a uniform envelope for
every internal line. A bulk computation may serve as a comparison only
after its finite-domain error is controlled at the tested scale.

Seek a justified asymptotic or bound that discriminates the proposed
N^-2 normalization. A finite nonzero limiting expression, a proved zero
limit with honest remaining scale uncertainty, or a precise obstruction
to the necessary uniform summation would decide how to continue. Any
claimed nonvanishing requires an analytic argument or a certified bound;
finite-mesh numerical values alone do not establish it. If the scale
fails, record the evidence and propose a precise alternative for review;
do not silently replace TARGET or assume the desired normalization.
Stop a mechanism that merely repeats the global norm bound, replaces
the relative covariance by scalar Dirichlet components, deletes normal
edges or invokes gauge invariance as a cancellation theorem.

This intermediate result could quantify necessary compensation in
L280(20). It would not establish cancellation with the action/insertion
families, uniform higher errors, a physical trajectory, composite mixing,
continuum axioms/positivity, a nonzero sector or finite positive mass.
Mathlib coverage of the full asymptotic and the supporting kernel
theorems is not checked; unknown availability is not absence.
