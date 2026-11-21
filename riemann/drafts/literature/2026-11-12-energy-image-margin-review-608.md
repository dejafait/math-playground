# Exact energy-image finite margin: nomination608 and source comparison609

TARGET: Certify a positive normalized margin for the compression of C744z(4) to W_512 direct-sum W_512, where W_512=A0^(1/2)H_512, using C999l's fixed free-coordinate bound and the full finite energy metric.
CHECKED: 2026-11-12
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step609 searched generalized symmetric-definite eigenproblems, Rayleigh quotients and closed-form square-root calculus; read the primary sources below and C744v Section3, C744z Sections1-3, C999l Sections1-2/6-7, C999r hypotheses/conclusion, audit561 and stops537/598/600/603. Reuse607 for the unchanged restricted-form calculus; no novelty inference.
SOURCE_EVIDENCE: Teschl GSM99 version12February2009, Theorem2.13/proof pp71-72, Lemma2.14/proof pp72-73, Theorems3.1/3.2 pp90-92 including (3.18),(3.24)-(3.27), and Theorem3.7 p96 (reuse607); Anderson et al., LAPACK Users Guide third edition (1999), Computational Routines, Generalized Symmetric Definite Eigenproblems/Table2.13, https://netlib.org/lapack/lug/node54.html, and Section4.10, https://netlib.org/lapack/lug/node98.html plus node99.html. Read complex Hermitian type1 reduction and exact eigendecomposition; distinguish approximate numerical error guidance.
COMPARISON: Standard generalized Hermitian spectral normalization covers the finite metric comparison once the exact energy-image identification and a certified full-metric upper bound are supplied. C999l(3) defines the complete finite metric and Sections2/6-7 retain its entry and arithmetic controls; .000999 bounds only the numerator in free coordinates. Neither source imports this notebook-specific normalized margin or transfers C999r to W_512.
GAP: Establish the exact restricted energy-coordinate identification, obtain a certified numerical upper bound for C999l(3) using its complete matrix and allowances, and then certify a positive normalized margin. These are the approved local specialization, still unproved here. Changed-projection tail control and all global sign gaps remain separate.
REASON: Separate literature-only step609 completes comparison for the changed projection nominated608. SPECIALIZE permits the unchanged TARGET under its retained contracts; general form and matrix results are cited rather than reproved. No new lemma, bound, mathematical script or source-contract validation is supplied by this approval.
SCOPE: Fixed N=512, ell=log(3)/2, H_512=H0 intersect span(e0,...,e511), exact restricted A0, W_512=A0^(1/2)H_512, both independent complex endpoints, complete S3=C744z(4), and C999l's unchanged .000999 coefficient margin and inherited analytic/arithmetic/core/c_* contracts. No finite inverse square root, new scalar floor, parameter tuning, or transfer of the band margin is authorized.

Main gap: L030-L032/C032a actual-Xi positivity. This proposal addresses
the separate missing finite normalized margin, not the infinite sign.
The candidate change is to choose a subspace adapted to the energy
coordinates of an already certified finite endpoint family. It is a
standard-method normalization question, not a claimed creative mechanism.

Essential local inputs: C744z Sections1-3; C999l(1)-(3), its complete
energy metric and audit561; C744v's full D+S form; C999r's distinction
between exact H_N compression and free-coordinate margins. C999q is
only a contrast: its band positivity does not certify the joint family.
No cross-notebook input. Exact source/certificate ranges beyond these
definitions should be located in the separate source review, not loaded
for orientation or taken as verified from a preview.

Bounded test after source approval: obtain a strictly positive explicit
margin on exactly W_512 direct-sum W_512, using the full finite metric
and every inherited entry/response error, or identify the precise missing
comparison or certificate. Retain the full restricted middle minimization
and remote-plus-induced products of C744z(4). Merely observing that
finite-dimensional norms are equivalent does not certify a numerical
margin. General spectral or matrix theorems should be cited, not reproved.

Plausible downstream use: a genuine normalized finite margin could be
paired with a separately justified complement estimate for this new
subspace. The latter is not supplied by C999r, and neither finite signs
nor a changed projection settle the mixed or infinite endpoint blocks.
The ineffective allowance in C999r remains true and is not retuned.
Original source/core verification, C744q, H2, non-neutral coverage and
global actual-Xi assembly remain unresolved. Full Mathlib match unchecked.

The paragraphs above preserve nomination608 and its original bounded test.
The separate review609 below supersedes their pending source status.
No proof, numerical margin or sign was established by either literature entry.


## Separate source comparison609 — 12 November2026

LITERATURE_REASON: The exact energy-image projection was REVIEW_REQUIRED at invocation start; coverage606/607 did not compare its finite energy metric. This essential changed scope justifies this literature turn despite the recent literature balance.

The main gap remains actual-Xi positivity in L030-L032/C032a. The
intermediate target is exactly TARGET above. A normalized finite margin
could support a later comparison with its infinite complement, once that
new complement and its mixed blocks are independently controlled. This
review approves only the finite specialization, with no sign calculation.

### Primary sources and essential cases actually read

[Teschl, Mathematical Methods in Quantum Mechanics, GSM99 author PDF,
version12February2009](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf):
Theorem2.13 assumes a densely defined closed semibounded Hermitian form;
its proof shifts the lower bound and constructs the self-adjoint
representative from a bounded inverse. Lemma2.14 equates the norms of a
bounded Hermitian form and its representing operator. Theorems3.1/3.2,
(3.18) and (3.25)-(3.27) give spectral norm identities and the domain of
an unbounded Borel function via integrability and bounded truncations;
(3.24) treats finite Hermitian matrices. Reuse607 for Theorem3.7 and the
positive spectral support. These support exact square-root coordinates,
not a square root of a finite operator substituted for A0. The inner
product convention must be translated consistently.

[Anderson et al., LAPACK Users Guide, third edition, SIAM1999,
Computational Routines, Generalized Symmetric Definite Eigenproblems, Table2.13](https://netlib.org/lapack/lug/node54.html):
for complex Hermitian matrices with positive definite metric, type1
reduces the generalized eigenproblem by Cholesky congruence; adjoints
replace transposes. [Section4.10](https://netlib.org/lapack/lug/node98.html)
gives an exact metric-orthonormal eigenbasis and diagonal form. This
covers the generalized Rayleigh comparison without assuming that the
target block is already positive. Its numerical error bounds are called
approximate; [the further-details page](https://netlib.org/lapack/lug/node99.html)
retains dimension factors and metric conditioning. Those routines and
bounds alone are not rigorous local certificates. The existing audited
arithmetic ledgers, rather than an unchecked computed eigenvalue, must
supply any numerical upper metric bound.

Queries used: `site.netlib.org lapack generalized symmetric definite
eigenproblems Rayleigh quotient positive definite B` and
`site.mat.univie.ac.at gerald schroe pdf quadratic form square root theorem`.
Search hits beyond the primary pages above are unread leads and are not
inputs. No independent source for a notebook-specific numerical margin
was located; this is not evidence of novelty. A new general theorem or
reproof is unnecessary. Full matching Mathlib coverage is unchecked.

### Exact local scope and approved specialization obligations

C999l(1) parametrizes exactly H_512 using510 free complex coefficients.
Its equation(3) defines A=Z*LZ with L=D+S+256C*C. The penalty vanishes
on the exact neutral image; the single-cell form includes the whole S,
not a fixed response prefix. C744z Section1 supplies the restricted A0
under the inherited core/c_* qualification. Section3 identifies the full
middle minimization with its bounded endpoint block. These are existing
inputs to be specialized, not new conclusions of this review.

For the next attempt:

- Justify the map from C999l's exact neutral endpoint family into exactly
  W_512, using the restricted square root and its actual form domain.
  Identify the endpoint norm through the complete finite metric A in(3).
  Do not assume H_512 is invariant under A0 or its square root.
- Bound that metric from above using the complete saved head and C999l's
  certified allowances. Section2(6) supplies eta_A; the reconstructed
  factor for 6.19^2 I-(Mhat Zhat)*Mhat Zhat supplies one possible bound.
  Sections2/6 also give exact-neutral conversion control and conservative
  matrix/basis norm bounds. Using a coarser audited upper bound is allowed;
  changing the floor, basis, family, predictor or allocation is not.
- Apply the cited finite Hermitian comparison to the unchanged .000999
  free-coordinate lower bound. Give an explicit positive normalized
  constant with complete rounding/conversion allowances, or identify the
  exact missing numerical certificate. No optimal margin is required.
- Keep the actual U and every induced middle product. A finite metric
  normalization does not license replacing the original restricted inverse
  or replacing full products by products of their compressions.

The selected certificate values `/stored_frobenius_ledger` and
`/finite/head_form_error` in
`scripts/separation-seven/neutral-head-covariance-559.json` were inspected
in full with the shared inspector, solely to locate metric evidence.
Their previews, and the root previews of559/561, were not treated as a
new verification. The existing canonical proof and audit561 supply the
qualified numerical input; this turn did not replay matrix operations
or derive a normalized bound. No new certificate is needed for source
approval itself. A later attempt must expose every value it actually
uses and preserve the inherited arithmetic conditions.

### Duplicates, failure scope and bounded decision

Audit561 already validates the fixed free-coordinate lower bound; do
not reproduce that certificate as a new finding. C999r concerns the
orthogonal projection onto H_512 in normalized L2 coordinates. Its
exact remainder, including its ineffective allowance, says nothing
by itself about the changed projection onto W_512. C999q's separate
band sign is not a joint-family certificate. No band result is imported.

The precise scoped histories537/598/600/603 were read. Stop537 is the
uniform-tail sufficient comparison;598 and600 fail joint-family
isotropic/entry-radius certificates;603 is a saved trial-map verification
allowance stop. This fixed512-family metric specialization neither
repairs those comparisons nor returns to their parameter loops. The
older diagonal-only/fixed-prefix stops remain mathematical obstructions
to their own comparisons, not a ban on the complete existing metric.

Continue with exactly TARGET: certify a strictly positive normalized
margin on W_512 direct-sum W_512, or isolate a precise missing comparison
or certificate. Merely invoking equivalence of finite-dimensional norms
fails this test. Do not append a tail claim or an enlarged-family test.
All inherited source/core/c_*, analytic/arithmetic assumptions, C744q,
H2, non-neutral coverage and global assembly remain unresolved.

DECISION is SPECIALIZE for this exact target; the local applicability
argument and numerical normalization remain future mathematics. This
step is EXPLORATION / REPRODUCTION, not a mathematical advance or
progress beyond the cited methods. No justified creative central sign
mechanism emerged: the unbounded endpoint/complement comparison remains
unpaid, and the source review did not supply a new mechanism for it.
