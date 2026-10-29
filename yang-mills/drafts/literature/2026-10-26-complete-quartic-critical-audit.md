# Complete quartic asymptotic: completed critical-audit coverage

TARGET: Critically audit L283–L285's complete quartic N^2 asymptotic, including differentiated local covariance, all-anchor boundary control and Wilson coefficients.
CHECKED: 2026-10-26
DECISION: EXPLORE
SEARCH_EVIDENCE: On 2026-10-26 compared full L283–L285, the relevant L003/L279/L280/L281/L282 passages, histories 496–500, selected quartic draft passages and ATTEMPTS/047–049. Reused the exact-target and stronger-result searches in the ready quartic and density assessments below; the scoped comparison found pending derivations, not an existing independent quartic audit. No repeated broad discovery search or novelty inference.
SOURCE_EVIDENCE: Reopened Benzi–Razouk, ETNA 28 (2007), section 3.5, printed pp. 24–25, graph-power argument, Theorem 3.4 and full proof including diagonal and normal-matrix cases; reused the precisely versioned Luescher–Weisz, Dowker, Lawler–Limic, Michta–Slade, bulk and quotient readings identified below.
COMPARISON: Known polynomial locality and scalar relative kernels support tools for a direct audit. Neither the analytic matrix-function theorem nor the inspected bulk one-loop results supply the weighted differentiated covariance, uniform all-anchor quartic limit or Wilson constants. No matching complete theorem is imported; the explicit local estimates must be checked independently.
GAP: Audit L283(5)–(19), L284(7)–(18) and L285(5)–(20): uniform spectral/column errors, all boundary paths, separated first derivatives on both time halves, complete summation, raw-edge Fourier phases, color/source factors and the final assembly. This review verifies source scope only.
REASON: Approve exactly the unchanged critical-audit target for one later RESEARCH / REPRODUCTION invocation. Its written proof uses explicit finite estimates and adequately covered tools, with no essential inaccessible source. EXPLORE does not accept those estimates or certify novelty.
LITERATURE_REASON: Separate approval of the newly registered audit was required; its differentiated internal covariance and full half-domain error sum had not been explicitly compared with the saved polynomial and scalar source coverage. The focused reopening tests that scope, rather than refreshing adequate discovery searches for quota.
SCOPE: Exactly TARGET for SU(2), even N>=2, a=8/N, fixed relative cube, every boundary-contained pin, boundary-fixed gauges, all normal links and colors, L002's exact product bump through L282 and L280's real source domain; ambient all-link L279 jets on L280's own slice. Includes essential L281/L282 source-field and tail inputs; no cubic compensation, uniform higher remainder or continuum assertion.
COVERED_TARGET: Critically audit L283–L285's complete quartic N^2 asymptotic, including differentiated local covariance, all-anchor boundary control and Wilson coefficients.

## Completed comparison and approval — step 501

The main gap remains construction of the required interacting continuum
theory with nonzero physical sector and finite positive mass for every
compact simple group. The nearer perturbative gap includes the complete
cubic compensation and a mesh-uniform higher remainder. The intermediate
target here is an independent audit of the claimed complete quartic
asymptotic. If valid, it quantifies the compensation still needed from
the cubic family when compared with L282's complete density. No sign of
the combined quartic/density coefficient is required or presumed.

Essential input IDs are L003 L279 L280 L281 L282 L283 L284 L285;
L002 enters through the exact bump in L282. The controlling target
version in `foundations/01-target-and-scope.md` is reused; this audit
does not select a new route or change that target. No other notebook is
read or used. Full and supporting Mathlib coverage remains **not checked**.

### Primary source scope

M. Benzi and N. Razouk, *Decay bounds and O(n) algorithms for
approximating functions of sparse matrices*, ETNA **28** (2007),
16–39, [published PDF](https://etna.ricam.oeaw.ac.at/vol.28.2007-2008/pp16-39.dir/pp16-39.pdf),
section 3.5, pp. 24–25, Theorem 3.4, was reopened with its entire
proof. It assumes diagonalizability, spectrum in a continuum F, and
analyticity on an enclosing domain; the bound includes the eigenvector
condition number. The proof combines polynomial approximation and
graph propagation, treats diagonal entries separately, and notes that
normal matrices permit a unitary eigenbasis. This covers polynomial
locality. It supplies no uniform inverse bound at the notebook's
closing spectral gap, nor an estimate for a product with the source
diagonal and incidence matrices. L285's column-energy claims remain
independent audit obligations; the theorem is not their justification.

Reuse [the quartic assessment](2026-10-26-quartic-response-quadratic-asymptotic.md):
Luescher–Weisz, *Coordinate space methods for the evaluation of Feynman
diagrams in lattice field theories*, hep-lat/9502017v2, 23 February
1995, sections 1, 2.1–2.2, pp. 1–4, and Appendix A.1–A.2,
pp. 18–21, treats the infinite scalar lattice propagator, including
both auxiliary-integral proof cases. Its Fourier convention can be
compared with the notebook's normalized Brillouin measure. It does
not establish a finite relative-box quartic limit or its anisotropic
edge-offset table. The explicit Wilson contractions therefore require
checking, not a reproof of the known scalar expansion. The same review's
Adams–Lee 0709.0781v3, section II (7)–(15), Appendix A (A1)–(A11),
and Luescher–Weisz hep-lat/9504006v1 sections 4.1–4.3 and 7,
with retained measure vertices (5.10)–(5.11), concern different
momentum-integral or complete-functional hypotheses. They do not import
the isolated quartic coefficient or a cancellation on this slice.

Reuse [the density-kernel assessment](2026-10-25-density-response-separated-kernel-asymptotic.md)
and [its audit coverage](2026-10-25-density-negative-asymptotic-critical-audit.md).
Dowker, 1207.2096v2, sections 7–8, (29)–(37), pp. 10–13,
covers the scalar interval conventions, including shifted Neumann edges
and their constant mode. It supports L003's tensor-mode framework;
it does not give L284's edge-to-plaquette normalization or L285's
uniform first-derivative bound on a time half. Those are explicit local
specializations to audit. Lawler–Limic (2010), Theorem 4.3.1 and
Proposition 4.6.2(a), concerns transient scalar walks and exit subtraction;
Michta–Slade, ALEA **19** (2022), Theorem 1.3(ii), retains d>2q
for the massless case. The excluded bare d=4,q=2 import remains excluded.
Neither is needed to assume the written finite spectral estimates.

Reuse [the quotient audit coverage](2026-10-25-local-quotient-critical-audit.md)
and the recorded separate L279/L280 audits for the fixed-mesh formula,
local chart and source normalization. Kirwin 0810.1700v2 Theorem 2.1
does not give a mesh-uniform remainder. The present audit does not
differentiate such a remainder or transport nonlinear forest jets.
No new source-dependent claim about the full interacting coefficient
is approved here. Uninspected references in the reused assessments
remain leads, not premises. No essential source access blocker was found.

### Exact later audit obligations

1. For L283 sections 1–2, check the relative spectra and all endpoint
   eigenvector bounds, the low-eigenvalue shell count and the order of
   limits in (6). Check both positive error matrices, their entry
   estimates and the conversion to a norm bound only after contraction
   with the local Wilson tensor. Verify every fixed-polynomial boundary
   layer, including intersecting faces, and the use of strong physical
   source-field convergence and the complete external tail in section 4.
   L281's audited tail and L282's audited fields may be used with their
   exact hypotheses; they are not automatic substitutes for a different
   operator or source domain.
2. For L284 section 1, check C_12 adjoint signs and each mode's actual
   grid, including zero edge indices and both normal endpoints. Audit
   the claimed physical kernel a^-3 GC_12^*, time recurrence and uniform
   summable first-derivative tails. For sections 2–3, check weighted row
   sums, support-edge rows, fixed-degree path locality, order of limits,
   shifted Riemann sums, beta_*=a_*/3, both insertion traces and time
   reflection. The numerical kernel certificate is not a proof of these
   assertions.
3. For L285 section 1, check the column norms in (6) using
   C_12^*C_12<=L as a quadratic-form inequality, without commuting those
   matrices. Audit the product subtraction and its uniformity in every
   anchor and mesh. For each fixed polynomial degree, verify that paths
   encountering any face have zero source weight, including pinned slots
   and corners. Verify the infinite-symbol domination, finite-offset
   convergence and the successive limits used in (9).
4. For L285 sections 2–3, audit separation on the two entire time halves,
   not only on compact neighborhoods of the sources. Check source and
   edge derivatives in all variables needed for uniform Riemann sums,
   time endpoints, pinned tangential slots, every orientation and the
   zero-time layer. Verify the remote O(a^2) factor and the full claimed
   normalized error bound C a^2 N^2(delta_N+rho_N), with constants
   independent of all anchors. No boundary or internal region may be
   discarded by a bulk-only argument.
5. Independently check L279's SU(2) generator and quartic conventions,
   L283's 35-word contraction (12)–(13), its raw-edge Fourier table
   (14)–(16), and L285's different anisotropic table (15)–(20). Isotropic
   and differentiated covariances must not be interchanged. Check all
   phases, reflected orientations, internal versus external color sums,
   source-order multiplicities, factors 1/4 and 1/24, physical powers of
   a, and the final four-term assembly against L280(20). The exact finite
   contraction certificates test only their supplied finite algebra;
   they do not establish Fourier identities or analytic errors.

These are checks to perform, not estimates proved by this review. The
ordinary spectral theorem, Cauchy–Schwarz, dominated convergence, finite
trace identities and uniform Riemann integration are standard named
inputs. Their general theories need no reproof; the precise finite-domain
applications and the Wilson algebra do require independent verification.
No unread finite-element, bulk renormalization or matrix-decay theorem
is hidden in the approved audit scope.

### Duplicates, failures and decision test

The scoped comparison of histories 496–500 and the three quartic work
notes found the existing derivations and audit requests, not a completed
critical audit. The source searches recorded in the reused quartic and
density assessments cover the same exact response and stronger scalar,
bulk and finite-volume tools; their limits have not changed. They are
reused rather than repeated. No inference of novelty follows from them.

ATTEMPTS/047 retains the uncontrolled integration-by-parts residual;
048 retains the insufficient global absolute norm; 049 excludes generic
gauge identities as a sufficient mechanism using a nonlocal comparison
phase. Auditing the claimed Wilson-specific local estimates tests a
different mechanism. It neither erases those stops nor reopens them
without new evidence. No exhausted source blocker requires recovery here.

Approve exactly TARGET for the next mathematical critical audit,
classified REPRODUCTION under EXPLORE. Accept the complete quartic
asymptotic only if every essential analytic and normalization claim
survives. A specific failure must identify the equation, its failed
hypothesis or estimate and its effect on the assembly, preserving the
original argument. A replacement mechanism outside this scope receives
REVIEW_REQUIRED before dependent research. Do not accept a bulk constant
with an unestimated error, infer validity from certificates, or reject
the actual asymptotic merely because a general source theorem is
inapplicable. Either audit outcome leaves cubic compensation, uniform
higher errors and the continuum/infrared Yang–Mills target unresolved.

This approval is made in a separate literature-only invocation after
the derivations. Outcome EXPLORATION / LITERATURE / NOVELTY_UNCHECKED;
zero mathematical exploration attempts are spent. No lemma, mathematical
script, DAG or PROOF change, and no mathematical acceptance, occurs.

## Original registration — retained, gate superseded above

Exact hypotheses: SU(2), even N>=2, a=8/N, fixed relative cube,
boundary-contained pins, boundary-fixed gauges, every normal link,
three colors, L002's exact product bump as recorded in L282, and
L280's real source domain. Use ambient all-link L279 jets evaluated on
L280's own slice. Essential inputs: L003 L279 L280 L281 L282 L283
L284 L285; L281 enters through the earlier subfamily estimates.

Reuse `2026-10-26-quartic-response-quadratic-asymptotic.md` and the
recorded separate L280/L282 audits where their hypotheses coincide.
No new external theorem is required by the written L285 proof. The
next literature-only turn should establish the exact coverage and
audit scope, including any source needed to challenge its assumptions,
before a later mathematical critical audit. Do not repeat source
browsing merely because this is a new filename. No novel theorem or
audit conclusion is derived in this registration. Mathlib not checked.

The audit should test the full uniform error before accepting the bulk
constant. In particular C_12^*C_12<=L must be used as a quadratic-form
inequality without an unjustified commutation, paths near every face
must have zero source weight, and one remote covariance must give
O(a^2) at every plaquette on its assigned time half. Check the
anisotropic H_12 symbol and every relevant raw-edge phase independently.
The finite rational certificate verifies only the stated covariance
table's Wilson contraction, not those Fourier identities or analytic
estimates. L283/L284's upstream local and separated estimates also
remain part of the audit, rather than being silently certified by L285.

A pass accepts the complete quartic asymptotic under its exact
hypotheses, with any necessary corrections made explicit. A failure
must identify the precise unsupported estimate or coefficient and
preserve the original derivation. Neither outcome by itself determines
the complete cubic/quartic/density coefficient, a uniform higher
remainder, continuum construction or positive physical mass.
