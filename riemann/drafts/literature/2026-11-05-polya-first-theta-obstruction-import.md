# Pólya finite-theta obstruction: narrow applicability nomination

TARGET: Import Pólya's finite-theta-truncation obstruction for the exact n=1 reference, checking L019's scalar normalization against the source and reconciling L234 without duplicating its endpoint proof.
CHECKED: 2026-11-05
DECISION: IMPORT
SEARCH_EVIDENCE: Reuse step571's exact first-summand/finite-truncation search and duplicate check in 2026-11-05-first-theta-summand-relative-minor-scope.md; L234 already contains the endpoint and first-associated-spectrum obstruction, so no new endpoint calculation or lemma is requested.
SOURCE_EVIDENCE: G. Pólya, Acta Math.48 (1926),305–317, DOI10.1007/BF02565336, (3) p.305, Section4 HilfssatzI/proof pp.315–316 and the immediately following finite-sum application p.316; original primary PDF and translation were inspected in step571.
COMPARISON: The source explicitly treats finite sums of full theta summands, including the single full term, rather than only the leading exponential or a cosh-modified kernel. A nonzero scalar and half-line/even-Fourier convention match remains to be checked locally; no reproof is needed.
GAP: Record the exact local applicability and citation in existing L234. This does not establish the sign of any specified reference or actual coefficient minor, a uniform perturbation radius, or mixed positivity.
REASON: Close a source-applicability gap for a failed reference premise using the known result, preserving the stronger local endpoint evidence and avoiding a duplicate lemma. This nomination awaits separate next-turn approval; the obstruction source review itself is complete.
SCOPE: Known theorem import only; no new endpoint derivative/asymptotic calculation, root search, determinant computation, lemma identifier or extension to a modified kernel. No new literature search is needed under these hypotheses.

The main gap remains actual-Xi all-degree mixed positivity. The intermediate
task closes the exact all-real-reference obstruction, permitting later
research to avoid relying on that failed premise. It is local source
integration, not progress beyond known mathematics or an RH disproof.

Use [Pólya's original PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/5376-11511_2007_Article_BF02565336.pdf),
Section4, pp.315–316. HilfssatzI assumes an analytic, real-valued F on the
nonnegative axis with u^2 F^(j)(u)->0 for every fixed j>=0 and F not even.
Its cosine transform is eventually nonzero on the real axis. The following
paragraph states explicitly that a finite sum of (3)'s full theta summands
has an entire transform with infinitely many zeros, only finitely many
real. Import that finite-sum assertion as stated. Its brief Hadamard
invocation is a citation input, not an independently audited derivation.
Use the exact finite-sum paragraph, not the modified-kernel real-zero
theorem or the ambiguous older word “imaginär.”

Essential inputs are L019's kernel formula, L021's moment convention,
L776's reference normalization and the existing L234 proof. Read only
needed ranges. Check that the proposed n=1 half-line transform and L234's
even-Fourier transform each differ from the source object by a nonzero
constant. Preserve L234's N-dependent onsets and its infinite-kernel
cancellation qualifications. Add a precise source qualification there;
do not reproduce its proof or create another reference-sign lemma.
No DAG edge or PROOF assembly change is anticipated for a citation-only
closure; assess any actual mathematical change on its merits.

Accept only if the exact full summand and transform conventions match.
On a mismatch, record it and abandon this import instead of silently
substituting a different kernel. Do not infer any particular negative
coefficient minor, the failure of every restricted-order reference
comparison, or a conclusion about actual Xi. Signed compensation,
usable order dependence and mixed/edge transfer remain unresolved.

The completed review is
`2026-11-05-first-theta-summand-relative-minor-scope.md`.
L234's endpoint obstruction and L808's distinct two-node reference stop
are retained as scoped evidence; L811/L813 provide no sign premise for
this import. Full matching Mathlib coverage is unchecked. No cross-notebook
input is proposed. Routine normalization/citation audit is standard/high;
this known-result closure is not a creative central mechanism.
