# Six-pair finite-cosine boundary closure test675

TARGET: Test a finite-interval integration-by-parts closure for C998g's K_0 cosine matrix on mode pairs (0,0),(0,2),(2,2),(2,4),(1,1),(1,3), retaining every finite-end and axis term and proving the singular cutoff limit; stop at the first unclosed two-variable correction.
CHECKED: 2026-11-12
DECISION: EXPLORE
SEARCH_EVIDENCE: Separate literature step675 completed assessment674's exact finite-cosine displacement search and compared the existing point/Duffy/hierarchy stops. No matching finite-cell closure/evaluator theorem was identified in the inspected primary sources; this permits a bounded proof test, not a novelty assertion. Full query/read evidence is in2026-11-12-finite-cosine-displacement-source-notes-675.md.
SOURCE_EVIDENCE: https://arxiv.org/pdf/1004.1988v1 Section2/(4)-(5),Remark2.1,Remark3.1 and3.3/Algorithm3; https://arxiv.org/pdf/0712.1013v1 Theorem2.1 and proof(2.3)-(2.5),Lemma2.2/proof; https://arxiv.org/pdf/1005.0667v1 Theorem3.6/proof and5.2; Tracy--Widom https://www.math.ucdavis.edu/~tracy/selectedPapers/1990s/CV49.pdf (1.2)-(1.4),IIA/B,(2.8),IID through(2.32), with OCR qualifications in source-notes675. Reuse658's Si/Ci definitions/branches only if needed and670/655's absolute-integration coverage; C998g/audit674 supplies the exact local kernel, not a displacement theorem.
COMPARISON: General structured-matrix results do not compute the generators or missing coincident-frequency data. Compact-support half-line commutation is inapplicable directly. Finite-interval kernel commutators retain endpoint corrections and do not automatically survive cosine compression. Ordinary integration by parts on a verified smooth positive-cutoff domain is an available tool; the finite-cell limit and closure are the explicit unproved application, not a general theorem to reproduce.
GAP: Determine whether all six selected entries reduce exactly to explicit endpoint data and convergent one-variable integrals, including independent diagonal formulas. No relation, rank bound, uniform arbitrary-mode closure, stable finite arithmetic or affordable evaluator has been established. If the proposed integration-by-parts scheme leaves a two-variable singular correction, preserve it as the obstruction rather than relabel it as evaluated.
REASON: This tests the first missing analytic input independently of inaccessible GKO/partial-reconstruction leads and before any expensive assembly. The original1e-10/20000000 service remains the later standard; passing six cases only supports considering a general relation. Newly ready coverage awaits separate next-turn approval; no proof is attempted675.
SCOPE: One analytic proof attempt on the six specified pairs, a=ell/2,ell=log(3)/2, modes n*pi/ell with C998a's normalizations/parity map. The frozen652 witness, neutral0/1 modes and coefficients stay unchanged. No quadrature batch, precision/degree choice, truncation, parameter sweep,256-mode assembly, low-rank assertion or quantitative work/error certificate is licensed.

Main gap: actual-Xi positivity in L030-L032/C032a and the signed S3
remote-plus-induced comparison. A closed square-matrix representation
could eventually pay one term in a full residual-Gram ledger. This
six-pair test alone pays neither the square service nor an RH sign.

Begin with the audited integral representation of K_tau in C998e(6),
as upheld in C998g Section1. Specify positive cutoffs before using
derivatives or boundary traces. Check the finite smooth hypotheses on
that restricted domain, retain all resulting boundary/corner expressions,
and only then consider removal of cutoffs. The previously proved absolute
integrability of the original product does not justify differentiated
interchanges or separate divergent boundary limits. Keep singular terms
combined when required and prove each claimed limiting cancellation.

The chosen pairs test zero, diagonal and distinct same-parity frequencies
in both blocks. A denominator that vanishes at n=m must be handled by
an independent exact formula or a proved limiting identity. K_tau(s,s)
is a spatial-diagonal formula, not the required frequency-diagonal
matrix entry. No claim that multiplication or differentiation has a
closed finite cosine matrix is an allowed premise.

Continuation test: all six exact reductions and limits must close into
explicit endpoint data and convergent one-variable integrals, with the
parity/normalization convention checked. An unreduced one-variable
integral is allowed at this analytic stage, provided its definition and
convergence are proved; it is not a paid numerical oracle. Abandon this
scheme at the first unavoidable two-variable singular correction,
unjustified limit or missing diagonal datum. Preserve the expression
and explain why the inspected tools do not close it. Six passes would
justify a later general-closure target, not prove arbitrary-mode closure
or feasibility. Do not tune parameters or expand the test after failure.

Closure must use shared, explicitly specified one-variable moments of
boundary/kernel data. The original Fubini representation as an integral
of two Carleman outputs is already known and does not pass this test.
Neither renaming that product as a moment nor recursing on unknown
mode-pair entries counts as closure. The proposed data must be defined
independently of both such outputs and the unknown Galerkin entries.

Essential inputs: C998g/audit674 and the prior672/674 evidence, reused
without a new arithmetic audit; C998a/audit655 for the modes/parities;
C998e(6)-(8) only in its audited scope; C999q exact Z for the eventual
frozen contraction. The archive
`scripts/separation-seven/frozen-reference-proposal-652.npz` stays pinned
to SHA256
`2b770a8a689a972ae487b9dd718e2e6d47b6769a5530e7fec244a102c5c317c6`.
The analytic six-pair test does not require loading its arrays or replaying
certificates unless it actually makes a new data-dependent claim.

C998f/audit669's diagonal setup is separate. C999/audit650 and
C999y/audit642 are downstream; C744v/w/z,C999k,C999z/audit646 original
analytic/arithmetic/source-to-Xi/whole-core/c_* contracts remain
unreplayed. A-square,both mixed terms,moments/projection,actual entries,
full100million work,residual/inverse debt,signs,higher/mixed endpoints,
C744q/H2,non-neutral/global assembly remain open. Mathlib full matching
coverage is unchecked; no cross-notebook result is used.

This is development using established calculus/structured-operator
methods at a computational subgap. It is not a justified creative
central signed-S3 mechanism. Future classification may be
POTENTIALLY_NEW only in the limited sense that this bounded search
found no matching closure result; no originality is certified.
