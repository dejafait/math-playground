# Independent audit of the exact Hermite product-kernel obstruction

TARGET: Audit L794's denominator minimality, symmetric theta integral identity and integer one-outlier witness without inferring a sign for the integral.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step497 approves reuse of the unchanged Newton/Hermite and finite-integral coverage in 2026-11-05-central-hermite-product-kernel-test.md and its completed parent 2026-11-05-central-hermite-theta-gram.md; L766 is a different Toeplitz representation, not a matching result or input. No new search or originality claim.
SOURCE_EVIDENCE: Nathanson arXiv:1911.01745v2 pp.1–4, Newton-sum definitions, Lemmas1–2/Theorem1 and both root cases; Forrester arXiv:1806.10411v1 Sections2.2–2.3/(1.7), complete finite permutation proof, as previously inspected. L019/L021 give positive K and all finite moments; L018/L776 fix actual-Xi normalization. L794 and product-kernel-496.json are the new local proof and certificate to audit, not independent source confirmation.
COMPARISON: Known central degree-six hyperbolicity is separate from this particular kernel's pointwise sign. The only audit specialization is the finite formal coefficient map, denominator clearing and polarization, plus exact rational arithmetic and continuity; no stronger analytic theorem is needed.
GAP: L794's written proof and certificate have not received a separate independent audit. Check especially cancellation/minimality, the permutation factorial, absolute integrability, integer-vector coefficients and open distinct-variable witness. No integrated sign follows from a negative region.
REASON: A useful exact mechanism stop must be checked before reuse. This audit has existing source coverage and tests the new certificate rather than reproducing known qualitative hyperbolicity or assuming real roots.
SCOPE: Separate literature-only approval completed in step497; the unchanged exact TARGET is ready for the next research invocation. Audit only this fixed degree-six construction, N=10, w=(-152988,4638,113,0,0,0), t=4 and its t>=4 bound. No alternate kernel, degree sweep, actual-root premise or theta compensation is approved.

The reusable source links and exact applicability are recorded in the
parent assessment, not replaced by this nomination. Primary sources are
[Nathanson v2](https://arxiv.org/pdf/1911.01745v2) and
[Forrester v1, permutation proof](https://arxiv.org/html/1806.10411v1#S2.SS2).
Newton identities are polynomial identities for arbitrary monic
polynomials; the real-root branch of Hermite's criterion must not enter
the audit. Forrester supplies a finite-expansion precedent, not a Gram
factor. The local proof derives its own monomial integral identity by
absolute Fubini using actual moments.

Essential mathematical inputs are L018/L019/L021/L776. Check L794's
formal expansion and the complete selected certificate values; a JSON
preview or execution success alone does not validate a proof. The first
five Newton sums suffice for the sign witness, while the denominator
minimality proof must cover s_10. Continuation test: either confirm every
claim at these exact hypotheses or record and repair a concrete defect.
Do not extend this audit into another construction. Degree-uniform signs,
integrated compensation and RH remain unresolved. Full matching Mathlib
coverage is unchecked. This is an ordinary finite proof audit, not a
creative mechanism or a candidate-RH audit.


## Completed source-scope approval (step497)

LITERATURE_REASON: The supervisor requires separate approval of the newly
nominated audit assessment. Reuse the parent discovery search; inspect
only the essential cited statements and proof cases to settle audit scope.
No changed mathematical target or repeated discovery search is needed.

Reopened Nathanson v2 HTML, power-sum definitions and Theorem 1 with both
proof cases and Lemmas 1–2. Roots count with multiplicity; the matrix is
(s_(i+j)) with zero-based indices. Its real-root direction uses real
squares; the converse uses conjugate-pair interpolation. Neither direction
is an admissible premise for the proposed kernel audit. Citation precision:
Lemmas 1–2 are interpolation lemmas, not explicit Newton recurrences.
Newton's identities are the standard named algebraic input; Nathanson's
opening paragraph cites Zeilberger, Discrete Mathematics 49 (1984), 319.
That reference was not opened, and is an unread lead, not extra coverage.
The explicit local recurrence remains an object of the approved audit.

Reopened Forrester v1 (1.7), Sections 2.2–2.3 and their complete finite
permutation argument. The determinant formula uses two given function
families and an N! factor. It supplies no matching functions or positivity
for L794. The audit must justify its own symmetric monomial identity and
absolute Fubini; it must not transplant the determinant factorial into the
permutation average. Individual function integrability alone is inadequate
on an unbounded domain without the requisite product integrability.

Read L019/L021's finite positive moment statements and proofs and only
L776's defining coefficient convention. Those are the local analytic
inputs; no conditional Fredholm conclusion is imported. Compared L794's
hypotheses/conclusion with the exact prescribed construction and its
recorded ATTEMPTS stop. This is scope comparison only: denominator
minimality, coefficients, witness, continuity argument and certificate
contents have not been audited in this turn. L766's different Toeplitz
obstruction and known degree-six hyperbolicity remain contrasts, not
inputs or substitutes for the fixed-kernel check.

DECISION remains SPECIALIZE. No missing essential source prevents the
finite audit. This approval does not establish new mathematics or certify
originality; full matching Mathlib coverage remains unchecked. Accept
only confirmation of every fixed claim or a concrete defect/repair, with
no change of kernel or family and no inference about the integral's sign.
The mathematical exploration budget and prior stop evidence are unchanged.
