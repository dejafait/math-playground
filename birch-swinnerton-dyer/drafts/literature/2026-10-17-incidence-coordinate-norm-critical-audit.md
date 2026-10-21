# Fixed coordinate norms — separate critical-audit scope approved

TARGET: Critically audit L075's full incidence coordinate-norm certificates, including both determinant methods, all coefficient transports and original-file preservation.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact-statement, stronger-result and algorithm searches in 2026-10-17-incidence-coordinate-norm-certificate.md and the general incidence assessment; compared complete L075, L074 hypotheses/conclusion, histories/271--273, saved construction design, relevant producer/verifier/I/O ranges and ATTEMPTS/035/036/039. Direct primary retrievals and passages read this turn are recorded below; no renewed discovery search or novelty claim.
SOURCE_EVIDENCE: Reopened Stacks Lemma 31.18.6 (0BD2), complete statement/proof; Bär arXiv:2008.04247v3, PDF dated 2021-08-06, Section 2.1 printed pp.3--4 equations (1)--(6), with Section 2 setup and Section 2.2 implementation comparison; Schaefer--Stoll author long version 2001-06-13, printed p.19 incidence proof, Proposition 7.10 and following multiplication-matrix paragraph. Reuse construction assessment's inspected standing hypotheses and generic Mathlib norm/Laplace statements.
COMPARISON: Known finite-free norms and both determinant algorithms cover the entire commutative Q-algebra B, including possible zero divisors. Audited L074 supplies the global rank-seven basis and projection pullbacks. Those theorems justify reviewing the fixed assembly; none certifies its coefficients, code, complete records or preservation. Construction replay is not a separate critical audit.
GAP: Essential source coverage is sufficient for the exact audit. Full fresh replay, complete evidence agreement, critical review of both implementations and all transports, and preservation checks remain undone; this assessment does not declare L075 audited.
REASON: The invocation-start REVIEW_REQUIRED scope is now compared with ready sources and the completed construction. One bounded RESEARCH / REPRODUCTION / proof_audit is justified, with isolated output, complete certificate checks and unchanged upstream mathematics.
LITERATURE_REASON: The separate critical-audit target was outside the prior construction-only scope. Reuse adequate discovery coverage; reopen only load-bearing ring/convention passages and determine exact audit obligations and caps.
SCOPE: Exact TARGET only; L075's short X,Y at seven for L067's conductor-389 model, L074's whole I/B, both V components, all rational transports, both determinant methods and scalar controls, complete records, qualified rejections and preservation. No arbitrary-input/power-class norm, descent arithmetic, field-factor selection, L069, stopped columns or new general theorem.

## Relevance, inputs and source reuse

The main gap remains rank E(Q)=m(E) for arbitrary E/Q with m(E)>=2.
The intermediate target is reliability of L075's two full coordinate norms.
Its plausible downstream use is a checked incidence-norm component toward
L066's conditional descent enclosure. Two fixed norms alone provide neither
arbitrary power-class norms nor a Selmer certificate.

L075 is the canonical statement and proof under review. Accept audited L074
and its accepted L067/L070/L071/L072/L073 inputs, including the specified
all-fiber geometric identification. Use complete incidence-269, successful
incidence-audit-271 and coordinate-norm-273 evidence. Do not rerun earlier
constructions or assume B or I is a field. No cross-notebook input is used.

Reuse `2026-10-17-incidence-coordinate-norm-certificate.md` and
`2026-10-16-conductor389-seven-incidence-maps.md` in this directory for the
unchanged exact-statement searches, stronger general construction and
implementation comparison. Their queries, versions and unread leads remain
as recorded. No additional discovery search is necessary for this audit.
Direct retrieval this turn used the three primary URLs below, finding
Proposition 7.10 and reading its incidence and matrix paragraphs, Bär's
relevant derivation and the full Stacks proof. Unrelated surrounding passages
returned by retrieval are not new inputs.

## Primary hypotheses and audit consequences

[Stacks Lemma 31.18.6, tag 0BD2](https://stacks.math.columbia.edu/tag/0BD2)
assumes a finite locally free morphism of constant degree d>=1. Its proof
defines the norm as the determinant of multiplication, checks basis
independence and arbitrary base change, and checks the vanishing property
after passage to a residue field. That last step does not impose fieldness
on the original base. L074's global B-basis (1,X,...,X^6) supplies d=7.
Computing a norm does not require a unit; a later power-class application
must establish its own unit and compatibility premises. The audit must
retain all B coefficients and the rank-seven scalar convention.

Christian Bär,
[*The Faddeev-LeVerrier algorithm and the Pfaffian*](https://arxiv.org/pdf/2008.04247v3#page=3),
arXiv:2008.04247v3 (revision 2021-08-05, PDF dated 2021-08-06),
Section 2.1, printed pp.3--4, equations (1)--(6), assumes a commutative
Q-algebra R and A in Mat(n,R). It gives N_1=Id,
c_k=-tr(A N_k)/k and N_(k+1)=A N_k+c_k Id;
det(t Id-A) has coefficients c_0=1,...,c_n, with
c_n=(-1)^n det(A). The terminal N_(n+1)=0 is an additional check.
The adjugate identity and formal Jacobi formula give the derivation without
inverting a matrix entry. Set R=B and n=7; division by 1,...,7 is permitted.
Section 2.2's NumPy example is not an exact-arithmetic certificate.
The audit must check every recurrence record and determinant comparison,
rather than infer the determinant solely from the terminal zero matrix.

Schaefer--Stoll, *How to do a p-descent on an elliptic curve*, Trans. AMS
356 (2004), 1209--1231, DOI 10.1090/S0002-9947-03-03366-X,
[author long version dated 13 June 2001](https://www.mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf#page=19),
printed p.19, Proposition 7.10 and adjacent proof/matrix paragraphs identify
point pullback followed by norm along the line projection. The following
paragraph computes it by a multiplication matrix. Reuse the inspected
standing odd-prime/number-field hypotheses: Q and seven qualify. The source's
incidence D is our I, not our direction D. L074 supplies the exact projections;
L072's inverse ordinary-functional indexing and Cartier convention persist.
No full residual-image hypothesis or cohomology/descent conclusion is imported
by computing these two norms. The p=3 example remains outside this audit.

For ordered Laplace expansion reuse the construction assessment's inspected
[Matrix.det_succ_row_zero and Matrix.det_fin_zero](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html#Matrix.det_succ_row_zero),
valid over a commutative ring. Review inherited row/column order, cofactor
signs, empty-minor value and zero-branch handling. No general reproof is needed.
Reuse [Algebra.norm_eq_matrix_det](https://leanprover-community.github.io/mathlib4_docs/Mathlib/RingTheory/Norm/Defs.html#Algebra.norm_eq_matrix_det)
and Algebra.norm_algebraMap_of_basis for generic norm/scalar coverage.
These generic statements do not formalize this fixed certificate. Full
matching Mathlib coverage for its algebras, transports and replay remains
not checked, not claimed absent.

## One bounded later audit

Before execution, save the unfinished design and inventory. Read the complete
producer, verifier and I/O/wrapper code and L075's entire proof. The present
limited code reads establish output routing and scope only; they do not verify
the implementation or certificates. JSON previews this turn prove no arithmetic.

Inventory every path in the existing 404-file originals inventory and every
file in coordinate-norm-273; match the retained prior 379-file inventory and
incidence-268/269 originals. Preserve all failed evidence and ATTEMPTS/035--039.
Use a new unoccupied `scripts/seven-torsion/coordinate-norm-audit-275/`
(or a fresh unoccupied equivalent if needed). Never run the exclusive-create
writer in the original directory. Copy verifier and I/O module byte-for-byte
to the fresh sibling directory, with required original input certificates;
record source/copy hashes. Keep upstream paths directed to the originals.
A copied construction report is input provenance, not a new build. Use a
fresh audit wrapper covering the whole stage; do not run the producer.

One fresh complete verifier execution must reconstruct B,I,y_f, both operators,
all source-coordinate changes and point transports without importing producer
arithmetic. Compare all 4704 rational matrix slots, all 96 norm slots, both
entire 48-column point bases/transports, all line inclusions and all
flatten/unflatten basis round trips against the originals. Keep all zeros,
both V components and all direction embeddings.

Inspect and compare complete fresh/saved N_k, A N_k, traces, c_k, N_(k+1),
all characteristic coefficients and full terminal matrices for X,Y and both
scalar controls. Compare every mathematical payload in fresh/original verifier
outputs; exclude only timing/path/report metadata where appropriate and list
exclusions explicitly. Check L075's entire norm table against all coefficients,
including claimed zeros. Success flags or selected coefficients do not suffice.

Independently check every saved ordered Laplace minor using the imported
cofactor formula and the verifier's separate full B arithmetic, including the
empty-minor convention and every nonzero branch needed from the root. Require
the retained key set to cover every computed reachable minor and leave no
unchecked records. This is certificate verification of the known expansion,
not a new determinant algorithm or theorem. Compare the full root norm with
the fresh Faddeev result, saved Laplace norm and norm table. Retain all scalar
control coefficients too.

Retain all three fixtures and reproduce exactly their named conditions.
The changed matrix coefficient, changed norm coefficient and missing odd-V
block retain L075's limited rejection scopes. Do not call them full malformed
replays or describe basis loss as a geometric sign selector. No additional
rejection family is required merely to increase counts.

Allow exactly one new audit arithmetic stage, including fresh verification,
all comparisons, Laplace-certificate and rejection checks: <=180 seconds
internally, <=181 seconds external watchdog, and <=134217728 bytes for the
entire new directory including input copies, reports and logs. Enforce the
total stage limit rather than giving each child/check a fresh budget. No
retry, cap extension or retrospective subdivision. Save complete certificates;
print actual/required bounds, failures and paths. Verify all original hashes.

Continue toward accepting this fixed assembly only if source hypotheses,
code conventions, every complete comparison and original hashes pass within
those bounds. Stop at the first mismatch, missing essential case or cap,
preserving failed evidence and the exact unresolved obligation. An uncovered
replacement requires separate REVIEW_REQUIRED coverage.

## Duplicates, stops and limits

Histories/272--273 distinguish source approval and construction replay from
the still pending separate audit. History/271 audited L074 only. This is a
distinct reliability check, not a new construction or novelty claim.
ATTEMPTS/035 and /036 stop different column presentations; ATTEMPTS/039
preserves a parser failure. None is reopened by auditing the completed
rank-seven representation. Existing stops remain evidence, not a global ban.

Arbitrary-input norms and power-class compatibility, descent functions,
complete global units/classes, local identifications/bounds, Selmer containment,
other L026 premises, successful localization, rational membership,
divisible-Sha removal and arbitrary-curve comparison remain unresolved.
This literature-only step establishes source/scope readiness using known
results; it derives no new result, executes no audit arithmetic and changes
no lemma, mathematical script, PROOF.md or DAG.md. L075's construction outcome
remains intact; its separate critical audit awaits execution.
