# Parameterized dual-kernel certificate — source comparison completed

TARGET: Assess source and implementation coverage for a parameterized full-relative dual-kernel certificate with supplied exact conductor and good-prime traces and an independent dimension-one stopping witness.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the ready L029/L037/L038 assessments; searched the fixed and general-relative programs and ATTEMPTS/023--024; queried official Sage documentation for rational right kernels and dual modular-symbol eigenvectors, then read the exact method contracts and cases below.
SOURCE_EVIDENCE: L029's complete proof and L037's complete argument/audit retain the inspected primary integration, real-duality, anemic-algebra and boundary inputs; L030 retains a complete fixed rank/nullvector certificate. Newly inspected Cremona corrected second edition Section 2.7 pp.25--26 and SageMath 10.8 right_kernel_matrix, dual_eigenvector and matrix_rational_echelon_form_multimodular documentation supply the implementation comparison.
COMPARISON: Standard algorithms already compute rational kernels and dual Hecke eigenvectors; L029 already proves full-relative sufficiency and L030 already checks an independent minor/nullvector witness. The new work is parameterized evidence production and arithmetic-input binding, not new linear algebra, multiplicity or nonvanishing mathematics.
GAP: No parameterized arithmetic-bound dual-kernel producer/checker is present in the scoped programs; implement and independently replay the full finite witness, preserving supplied arithmetic hypotheses and reporting larger kernels as inconclusive.
REASON: Essential coverage is adequate for the bounded implementation below; citations do not emit its matrices, rank witness or input binding. This review derives no new result and executes no mathematical script.
LITERATURE_REASON: Changed executable object: the ready structural implementation assessment explicitly excludes eigenlines, and the fixed dual-kernel checker hardcodes conductor 389 and a_2=-2.
SCOPE: Finite supplied good-prime set P, L029's exact minimal non-CM E/Q and conductor/newform hypotheses, independently certified entire relative presentation and operators; bounded mandatory arithmetic replay at conductor 389 with P={2}, a_2=-2. No prime cutoff, general software correctness or runtime theorem.
COVERED_TARGET: Implement a parameterized full-relative dual-kernel certificate and independent rank/nullvector checker, replaying the supplied conductor-389 input with P={2} and a_2=-2.

## Relevance and retained inputs

Main gap: rank E(Q)=m(E) for arbitrary m(E)>=2. The intermediate target
is an executable full-relative rational dual line, usable as the line
input of L028/L036 independently of q. The threshold is a nonzero exact
nullvector together with independently checked rank d-1 on the entire
relative dual. A larger kernel is inconclusive. Failure of input binding,
operator coverage or either rank inequality requires repair before use.

Essential inputs are L029's column/dual and reflection conventions,
L030's supplied independent arithmetic and fixed evidence, L037's
conditional eventual-attainment theorem, and L038's full structural
certificate contract. This review does not reprove their theorems.
L037 supplies eventual attainment only when the exact-conductor hypotheses
hold and every requested construction and exact check finishes; its
existence argument is not an instance's stopping witness. The approved
implementation is finite supplied-P production, not an unbounded search.

Reuse assessments `2026-10-07-relative-hecke-line-certification.md`,
`2026-10-08-good-prime-relative-line-termination.md`,
`2026-10-07-concrete-relative-t2-certificate.md`,
`2026-10-09-general-relative-certificate-implementation.md` and
`2026-10-10-general-relative-implementation-critical-audit.md` in this
directory. Their mathematical scopes are unchanged. Read L029's whole
proof, L037's full argument and audit, L030's arithmetic and both rank
witness passages, and L038's hypotheses and completed executable audit.
No certificate arithmetic was reverified here.

## Primary source comparison

All new retrievals below were made on 2026-10-10. These are inspected
documentation contracts, not library executions or source-code audits.

1. [Cremona, *Algorithms for Modular Elliptic Curves*, corrected second
   edition (1997), Chapter 2, Section 2.7, printed pp.25--26](https://johncremona.github.io/book/fulltext/chapter2.pdf#page=19).
   Read the opening column-action, dual-row and transpose-eigenvector
   discussion and the following oldclass qualification. This already
   computes projection by a dual vector up to scale, but its ambient
   space is absolute H^+(N). It does not alone identify the whole relative
   line or give a good-prime cutoff. Retain L029's relative adjointness
   and nonvanishing argument rather than copying an absolute eigenline.

2. [SageMath 10.8, matrix2.right_kernel_matrix](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix2.html#sage.matrix.matrix2.Matrix.right_kernel_matrix).
   Read input/output, the field-only pivot option, rational rectangular
   examples with exact zero-product checks, and the zero-row/zero-column
   cases. Rows of the returned matrix form an independent spanning set
   for the right kernel; its transpose is used in multiplication.
   The nearby right_kernel documentation distinguishes kernel(), which
   means left kernel. This supplies an existing exact-computation option,
   not independent rank evidence. Use Q, explicit dimensions and L029's
   right-kernel convention; no inexact tolerance is approved. Availability
   was not tested, and Sage need not become an executable dependency.

3. [SageMath 10.8, HeckeModule_free_module.dual_eigenvector](https://doc.sagemath.org/html/en/reference/hecke/sage/modular/hecke/module.html#sage.modular.hecke.module.HeckeModule_free_module.dual_eigenvector).
   Read the simple-input warning, lift option, transpose-action output,
   cached/randomized qualification, dot-product interpretation and
   level-14 simple-factor example. This is a known stronger algorithmic
   precedent for an ambient dual functional. It requires a simple input
   space already identified; it does not certify that our supplied
   simultaneous full-relative kernel has dimension one or bind arithmetic
   eigenvalues to a particular E. No software sign label replaces J.

4. [SageMath 10.8, matrix_rational_echelon_form_multimodular](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/misc.html#sage.matrix.misc.matrix_rational_echelon_form_multimodular).
   Read proof input, echelon/pivot output and algorithm steps 0--5,
   including denominator clearing, rational reconstruction and the final
   height inequality; inspect the rectangular rational examples. Exact
   rational elimination is established software functionality. The
   continuation does not need this particular multimodular algorithm or
   its reconstruction proof: retain the already covered reversible
   rational-row replay and independent minor/nullvector contract instead.
   No probabilistic rank claim or library-output trust is authorized.

Queries: `site.doc.sagemath.org matrix rational right_kernel_matrix echelon
pivots algorithm` and `site.doc.sagemath.org modular symbols dual eigenvector
eigenvalues sign`. The first query's site spelling did not restrict its
results reliably; only the official pages listed above were used.
Search snippets, numerical modular-symbol pages, unrelated results and
unopened linked implementation source code are not theorem evidence.
No claim of novelty follows from this search. Full matching and supporting
Mathlib coverage remain not checked; unknown availability is not absence.

The canonical citations for relative mathematics remain in L029/L037/L038:
Stein online v0.1 General Modular Symbols Proposition 1.38, Theorem 1.42,
Remark 1.41 and equations (11)--(12)/Remark 1.43; Cremona Sections
2.1.2--2.1.3 and 2.4; Stein Theorem 9.4 with its Gamma_0 paragraph and
Ribet--Stein January 12, 2017 Proposition 9.4.3 with Remark 9.4.5;
Cremona Proposition 2.2.3 and the named Hasse and Dirichlet theorems.
Their previously inspected hypotheses and essential proof cases are
reused, not replaced by Sage manuals. No reproof of those inputs is needed.

## Local duplicates, failures and evidence contract

Scoped reads of `scripts/relative-t2/build_certificate.py`'s
reduce_rational and dual-output sections, the verifier's arithmetic and
rank replay, and the audit's independent minor/nullvector section find a
complete *fixed* precedent. L030 records rank 64 at d=65, corroborated by
a selected integer minor nonzero modulo 101 and an exact nullvector.
These are prior results, not newly checked numbers. The fixed verifier
hardcodes the model and a_2 and enforces threshold success, so it cannot
serve unchanged as a generic inconclusive-result checker.

The general-relative programs accept finite good P and already preserve
matrix shapes and independently reconstruct the lattice/operators. Their
audited N=1/N=15 runs carry no arithmetic traces or eigenline. Extending
their evidence schema is therefore distinct from repeating an old audit.
Preserve every fixed/general certificate and report. ATTEMPTS/023--024
stop repeating conditional calibration audits as production; they do
not ban this concrete producer. Uniform twist-source blockers remain
parked. No cross-notebook input is used.

The covered implementation must satisfy the following existing contracts:

- Accept externally supplied model identity, exact conductor, finite good
  P and integer traces, with explicit provenance for minimality, non-CM
  and conductor/newform association. Bind them to the structural input
  and reports. Reject prime/level/operator mismatches, duplicate or missing
  trace entries, malformed dimensions and unsupported arithmetic claims.
  A hash binds bytes, not arithmetic truth. Generic output is conditional
  on supplied arithmetic certification; it does not certify an arbitrary
  conductor or minimal model by repeating input fields. At the mandatory
  fixed replay, reuse L030's independently justified arithmetic evidence.
- Independently validate the complete relative structural evidence under
  L038, or reuse an entire previously verified input with explicit content
  binding and a check of its applicable schema/conventions. A builder's
  claim of success or operator hash alone is insufficient. An adapter for
  the audited fixed L030 schema may be used without pretending it is the
  general-relative schema. Retain all integral-generator coordinates.
- Reconstruct every block of L029's B from the checked column matrices
  and matching traces. Keep the entire relative domain, transpose and
  geometric J sign. Save exact reversible rational elimination, all
  pivots/zero rows and a full kernel basis, with explicit matrix shapes,
  strict rational parsing and operation/index checks before list iteration.
- At dimension one save and independently check nonzero v and every
  entry of Bv, plus a selected (d-1)-square minor from independently
  reconstructed B. Check its determinant exactly, or use L030's existing
  integer-minor/modular-witness method with verified prime and permissible
  denominator handling. A vanished modular minor is not a zero rational
  determinant certificate; permit exact determinant fallback. Keep d=1's
  empty-minor convention from L029. Do not infer rank from v alone.
- Compute every integral-generator functional value using the checked
  coordinates and v, and check all saturated relations. No normalized
  period, q or denominator C is supplied by those values. A valid kernel
  of larger dimension must be recorded as INCONCLUSIVE with its actual
  rank/nullity, not as a failed theorem or a certified integration line.
  Nullity zero, d=0 or contradictory arithmetic cannot activate L029;
  preserve the diagnostic result without producing a line.
- The independent checker must not import the kernel builder or trust its
  failure list. Persist complete witnesses and success/failure reports;
  print actual/required ranks and dimensions, failures and artifact paths.
  Include bounded corruption checks for input binding, transpose/sign,
  missing blocks, zero/wrong nullvectors and malformed/nonzero-minor claims.
  Synthetic shape or larger-kernel fixtures are checker tests, not elliptic
  arithmetic instances. The mandatory substantive replay is the supplied
  conductor-389 case; an additional universal execution theorem or
  arbitrary-curve run is outside this one-step scope.

No new lemma, certificate, mathematical calculation or script is produced
by this review. The approved next research turn is SPECIALIZE /
REPRODUCTION, with ACTUAL_TASK_TYPE implementation. Continue on complete independent replay
of the mandatory input and its stopping evidence; repair missing evidence
before downstream use. If this bounded implementation cannot meet its
contract, save the precise obstruction and choose a discriminating repair
or a materially different test, not another conditional audit.

Independent q, normalized coefficient production, rational membership,
divisible Sha and general complex-order comparison remain unresolved.
STATUS remains IN_PROGRESS and there is no BSD candidate.
