# Parameterized relative certificate — implementation coverage approved

TARGET: Implement L038's parameterized relative lattice and reflection/T_2 certificate, with independent full replay at N=1 and N=15.
CHECKED: 2026-10-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed arbitrary-level primary-source assessment; scoped comparison of scripts/relative-t2/{build_certificate,verify_certificate,audit_certificate}.py found only fixed conductor-389 evidence. Inspected SageMath 10.8 P1List and transformation-output smith_form documentation for composite lookup/lifts and empty-matrix coverage.
SOURCE_EVIDENCE: Audited L038 and drafts/2026-10-08-general-relative-construction-source-notes.md retain Stein equation (3.2.1), Propositions 3.10--3.11, Theorem 3.13, Section 3.4.1; Cremona corrected second edition Propositions 2.2.1--2.2.2; Sergeraert arXiv:2411.02422v1 Sections 2,3.1,4,6--7/Theorem 1. Newly inspected SageMath 10.8 P1List index/normalize_with_scalar/lift_to_sl2z and smith_form transformation, singular, rectangular and empty cases.
COMPARISON: Known mathematics and existing software already cover projective cosets, lifts and exact normal forms; the local fixed programs do not supply composite orbit completeness, the level-one empty quotient or a parameterized independent full replay. This is certified implementation of known algorithms, not a new theorem or novelty claim.
GAP: Produce actual complete finite witnesses at N=1 and N=15 under L038's contract, retaining dimensions, all reversible transformations, every oriented path, full saturated-kernel descent and reconstruction; no instance has been run in this review.
REASON: Separate implementation comparison now covers the previously excluded executable evidence requirements; citation alone cannot supply these local certificates. Approval is confined to structural construction/replay, without arithmetic eigenvalues, an eigenline, q, periods or a BSD comparison.
SCOPE: Positive N, weight two, trivial character, finite supplied good-prime set P; mandatory instances N=1 and N=15 with P={2}; no practical runtime or complexity claim.

## Source comparison and qualifications

This literature-only step reuses the inspected theorem domains and proof cases
in the source notes cited above. Stein's integral relative presentation is
modulo all torsion, includes elliptic-point relations and permits composite
positive levels. Both path-reduction cases and the good-prime endpoint sum
were previously inspected. Cremona's composite coset/lift discussion is the
appropriate source; rational absolute homology alone is insufficient.
Sergeraert supplies arbitrary-rank rectangular finite normal forms, with the
coefficient-growth warning retained. Manin's original injectivity passage
and the original Kannan--Bachem paper remain unread; they are not added
premises. Import the precise cited results rather than reprove them.

New implementation-source comparison:

- [SageMath 10.8 P1List](https://doc.sagemath.org/html/en/reference/modsym/sage/modular/modsym/p1list.html): read the composite-level example, index input gcd(u,v,N)=1, normalize_with_scalar output convention, and lift_to_sl2z input/output. These provide existing general lookup/lift facilities, but not this notebook's full orbit certificate. A returned normalizing scalar needs its unit and congruence checks; the checker must independently reconstruct the primitive-pair orbits. No Sage level-one behavior is presumed.
- [SageMath 10.8 integer-matrix smith_form](https://doc.sagemath.org/html/en/reference/matrices/sage/matrix/matrix_integer_dense.html#sage.matrix.matrix_integer_dense.Matrix_integer_dense.smith_form): read transformation=True, S=U*A*V, singular and nonsquare examples, and all three empty matrix shapes. This is an available implementation option, not a correctness substitute for complete transformation/inverse replay. Invariant-only elementary_divisors cannot recover integral generator coordinates. A custom reversible diagonal equivalence is also allowed by L038; divisibility ordering is unnecessary. Library availability was not tested.

These official manuals were accessed 2026-10-10. No source-code internals,
new topological proof, new termination proof or numerical instance result
is claimed. Direct manual URLs, not snippets, were read. Local searches
covered the three fixed programs, construction assessments, history/105--109
and ATTEMPTS/022--024. No matching completed parameterized implementation
was found in those scoped paths; this is not a global novelty search.
Mathlib full matching and supporting coverage remain not checked.

## Executable differences and approved evidence contract

The builder's build() fixes a Weierstrass model and sets N from its prime
discriminant. Its representatives and index() use the prime-level list and
invert every nonzero first coordinate. The verifier independently repeats
that restriction. The supplementary audit fixes (s,r,d)=(390,325,65).
Those restrictions must not be propagated to the general structural input.
Preserve all conductor-389 programs and artifacts; create separate outputs
under scripts/general-relative/ rather than overwrite their certificates.

Use audited L038 as the mathematical contract, with L029 fixing geometric
reflection and column-convention good-prime endpoint maps. L037 is the
plausible downstream line-termination use, not a computational premise.
No elliptic curve or newform is attached to the two structural levels.

The builder/checker must accept explicit positive N and finite good P,
reject invalid inputs, and record inputs and explicit matrix dimensions.
A zero-row matrix must retain its column dimension; list transpose or zip
must never silently erase it. Do not invoke the fixed eigenline/RREF stage
or enforce a dimension-one output at these levels.

Require the following full evidence, already justified in L038:

1. At N>1 reconstruct every primitive residue pair and every unit orbit,
   with representative-assignment/unit witnesses and one coprime SL2 lift
   per orbit. At N=1 use L038's single identity lift. Check every lookup
   used by relations or segments through h*g_i^(-1) in Gamma_0(N).
2. Reconstruct all 2s relation rows, including repeated-index multiplicity,
   from actual right actions of L038's S and R_3. Record/check the chosen
   convention explicitly; do not mix the fixed builder's alternative
   three-cycle labels with the new certificate schema.
3. Replay every elementary row/column operation, with strict integer types,
   bounds and valid elementary-operation conditions. Check the complete
   diagonal identity, nonzero pivots and zero tail. Retain/check both
   unimodular transforms and inverse products, either explicitly or via
   complete reversible logs. Replay the row inverses too; the fixed
   verifier's column-inverse replay alone is not the whole new contract.
4. Check all L038 coordinates, saturation basis and quotient section,
   removed torsion order, Pi*Q=Id, Pi*K=0, Pi*A^t=0 and the full integral
   decomposition of Id_s. Retain all s integral-generator coordinates,
   including empty coordinates at d=0. Use L038's already audited N=1
   relations (2),(3) and d=0 as the structural expectation; do not invent
   or assert an uncomputed dimension or torsion value at N=15.
5. Replay every original generator path and every reflected/good-prime
   path, all endpoints, chain adjacency, orientations, segment determinants,
   coset/gamma witnesses and raw sums. Infinity chains are empty; negative
   fractions use reduced positive denominators. The checker need not share
   the builder's continued-fraction routine: segment geometry and complete
   telescoping are essential. Check all ell+1 terms, never isolated descent.
6. Recompute each full operator image, test every source relation and every
   saturated-kernel column, and check B_O=Y_O*Q and B_O*Pi=Y_O on every
   generator. Optional involution/commutation checks do not replace these.
   N=1's 0-by-0 operators still require all raw path/normal-form checks.

A separate checker must not import the builder or trust its failure list.
Strict shapes and complete required-domain reconstruction must precede
any zip-based comparison. Persist full certificates and checker reports,
including failures even on an interrupted/failed replay where possible.
Print bounded actual/required counts, dimensions, removed torsion, failure
counts and artifact paths. Do not run the old large fixed-level replay
merely to reestablish unchanged evidence.

## Relevance and continuation test

The main gap remains rank E(Q)=m(E) for arbitrary m(E)>=2. The intermediate
target is executable evidence for the full relative lattice and operators,
which could feed L037/L029 line production independently of q. Continue
only on complete zero-failure independent replay at both mandatory levels.
Missing orbits, residual torsion, wrong orientation, matrix shape loss or
failed full descent require specific repair before downstream use; repeated
failure requires reassessing that implementation mechanism. This review
supplies coverage approval, not successful replay or a universal software
correctness proof. No new lemma or mathematical script was written.

ATTEMPTS/022--024 stop repeated conditional audits as production; they do
not ban this instance-production target. Uniform twist sources remain
parked. Exact conductor/minimal-model/newform and arithmetic eigenvalues
remain separate later premises, as do independent q, normalized denominator
and coefficient production, rational membership, divisible Sha and general
complex-order comparison. No BSD candidate exists.
