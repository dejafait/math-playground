# Aggregate cut lower bound: proposed critical-audit scope

TARGET: Critically audit L100's exact coefficient-cut lower bound for S_n, including parity cancellation, affine constants and the original-Q comparison.
CHECKED: 2026-10-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Reused the exact-S_n searches in drafts/literature/2026-10-20-renaming-aggregate-seed-compression.md; inspected full L100 and L033, L099 §3/step-388 recurrence and ledger passages, Attempts 020/032/033 and history/390; no additional search was needed for unchanged hypotheses.
SOURCE_EVIDENCE: Reused step-389 primary-source evidence: Nisan STOC 1991 §2 Definition 1 and §3 Theorem 1/both proof directions, PDF pp.4–5; Raz–Shpilka author manuscript Definition 1/Lemma 2 Steps 1–5, printed pp.4–6; read L033's full audited F2 constant-closure specialization. No primary source was reopened.
COMPARISON: Existing coverage suffices for one audit of exact S_n: Nisan supports the rank mechanism, L033 supports F2 affine constants, and L099 supplies the received recurrence/Q ledger. Growing alphabet, unequal cuts, lowest-component formula and exact rank are explicit local audit obligations, not imported theorems.
GAP: Perform the independent all-size critical audit of L100; this approval establishes neither its coefficient formula nor exact rank nor original-N lower bound. Complete-certificate cancellation and unrestricted SAT remain unresolved.
REASON: Separate scope comparison found no essential uncovered source hypothesis; approve the unchanged saved audit target using ready evidence, with no new mathematics or correctness verdict.

SCOPE: Exactly the TARGET, free F₂ algebra on the 2n named generators, explicit acyclic affine-edge ABPs with arbitrary endpoints/parallel edges, and unchanged original Q of L099; audit only, with no full-certificate or alternative-witness lower bound.
LITERATURE_REASON: The supervisor requires separate approval of the newly selected completed-proof audit; reuse the ready exact-S_n source assessment rather than repeat discovery or browse unchanged hypotheses.

## Scope approval — step 391, 2026-10-20

This literature-only comparison approves one subsequent critical audit.
The previous assessment's discovery and inspected primary passages remain
adequate because the exact aggregate, field, receiving graphs and original
input parameter have not changed. Reading L100 here identifies what must
be audited; it does not verify its derivations. No lemma, mathematical
script, new theorem specialization or audit verdict is produced.

Nisan, *Lower Bounds for Non-Commutative Computation (Extended Abstract)*,
STOC 1991, pp.410–418, §3 Theorem 1, PDF p.5
([primary mirror](https://www.csa.iisc.ac.in/~chandan/courses/arithmetic_circuits/notes/noncomm.pdf),
[DOI](https://doi.org/10.1145/103418.103462)), uses real coefficients and
homogeneous consecutive-layer linear ABPs. Its lower direction factors
coefficient matrices through a layer. It does not directly state the
F₂/affine-DAG theorem or the aggregate's rank. L033 supplies the audited
local field/model treatment; the next audit must check its claimed
finite-alphabet and unequal-cut application in L100, without deriving
and approving that application in this gate turn.

Raz–Shpilka, *Deterministic Polynomial Identity Testing in Non Commutative
Models*, author-hosted 16-page manuscript, Definition 1/Lemma 2, printed
pp.4–6 ([primary manuscript](https://www.cs.tau.ac.il/~shpilka/publications/RazShpilka_PIT.pdf)),
provides degree-copy and scalar-edge normalization for formula inputs
with zero constant term. Its formula runtime is not an arbitrary-circuit
conversion and is unnecessary for L100's claimed original-N factorization.
No additional normalization upper bound or factorization theorem is
needed for this audit. The prior factorization lead therefore creates
no essential unread source dependency.

Duplicate/failure comparison: Attempt 020 concerns a universal degree-only
conversion; Attempt 032 concerns literal whole-seed copying. Attempt 033
records L100's stronger isolated-output stop, explicitly pending audit.
None is independent verification of L100. L099 step 388 already audits
its recurrence and original-Q family, but explicitly does not establish
aggregate rank. The earlier exact-S_n assessment records no inspected
full-statement match, which does not certify novelty. No new external
queries or cross-notebook reads were made.

The approved subsequent audit must verify L100's exclusion of all
lower degrees, every term in the homogeneous recurrence, word/suffix
injectivity, n=1, both directions of the exact-rank statement, and the
factorization through the original N vertices. In particular a constant
run at the cut must not be counted twice, and no homogeneous-normalization
size loss may be used to claim an original-N bound. Check all full
encoding assumptions and comparison with the original Q, without
substituting a witness-dependent size parameter.

Essential mathematical inputs are L099's audited recurrence/original-Q
family and L033's audited constant-closure method; L097/L087 enter via
L099's received extraction and dictionary ledger. The finite checks
in scripts/renaming-aggregate/lowest-cut-certificate.json are optional
support, not the all-size proof. Existing source passages suffice unless
a precise uncovered condition is found. This note approves no new
lemma, script or theorem specialization.

The independent limitations remain: set later Z_i=0 before B and take
the output before b; the complete K_n(B)=p. Full-certificate cancellation,
alternative witnesses, occurrence normalization, exact fg transfer,
short-proof availability, M-only bounds, universal W2 and unrestricted
SAT are not assumed settled. Mathlib matching coverage is not checked.

Continue if the all-size coefficient and original-vertex arguments survive
independent checking; repair a localized defect explicitly. If parity,
suffix injectivity, constant-run placement or the original-Q comparison
fails essentially, narrow or withdraw the corresponding L100 claim and
preserve the failure evidence. Do not reopen exact-output compression
merely by recounting contexts. A successful audit would make the isolated
compression stop reliable for route selection, while leaving all listed
independent gaps open. Mathematical EXPLORATION usage remains zero.
