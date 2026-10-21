# Direct PVT location after the local interfaces — completed source review

TARGET: Assess direct import of PVT Theorem 7.8 for L019's representation at 7 using L020–L023, retaining both coefficient embeddings and the exceptional-algebra hypothesis without reopening the blocked independent type-to-level proof.
CHECKED: 2026-10-05
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the earlier modular-location, local-lift and local-line assessments; narrowly checked L019–L023 and the recorded type-to-level failure. Queries "Pacetti" "Villagra" "7.8" conductor erratum and "2512.17845" revision supplied no inspected replacement theorem; the primary arXiv version page identifies v1 of 19 December 2025.
SOURCE_EVIDENCE: Read PVT arXiv:2512.17845v1 Section 7.2 setup, Theorem 7.8(i)–(ii) and its whole proof, https://arxiv.org/html/2512.17845v1#S7.SS2; inspected Corollary 3.6/Remark 3.7, Corollary 3.11/Remark 3.12, Lemma 3.13 and proof, Proposition 3.14, Lemma 7.3 and proof, Proposition 7.4 and proof, and Remark 7.5; reused Theorem 2.4(1), Remark 2.2 and Section 7.1's geometric identification.
COMPARISON: The exact theorem matches L019's primitive signed solution and geometric plus component; L020 supplies its irreducibility premise for either coefficient embedding. L021 closes the earlier cyclotomic-restriction objection, and L022 plus L023's audited local portion cover the local lift/line interfaces. Exact conductor and automorphic level are imported from PVT, not inferred from L019's bounds or L023's blocked conclusion.
GAP: No additional minimal-type or conductor hypothesis is imposed by this direct theorem application. The cited preprint's conductor computations and level-lowering conclusion remain imported source inputs, not independent notebook verifications; exceptional-algebra applicability, packet exhaustion and uniform signature emptiness remain open.
REASON: Complete theorem-level matching now supports a later KNOWN_IMPORTED application; reopening the blocked independent type-to-level audit would duplicate a stronger accessible result and is unnecessary for this bounded target.
LITERATURE_REASON: L021, L022 and L023's local-line audit change the essential inputs since the earlier direct-import comparison; coverage of the exact-level clauses under these inputs has not been approved.
SCOPE: Direct citation of PVT Theorem 7.8 for the conditional fixed-signature geometric representation at 7, with both coefficient embeddings and all source level cases. No independent conductor/level reproof, packet computation, archive retry or global algebra classification.

## Relevance and completed test

Essential input IDs are L019, L020, L021, L022 and L023's audited local portion. Retain the isomorphism Q[T]/(15T^7-35T^6+21T^5-X^5/Z^7) with Q[T]/(T^7-483T^2+3955T-3945), signed nonzero primitive X^5+Y^3=Z^7, geometric covariant Tate normalization and both coefficient embeddings. The algebra assumption, irreducible-packet exhaustion and uniform residual-signature emptiness remain unresolved. L023's type-to-level passage remains parked and is not a premise of this comparison.

The main gap is uniform emptiness of the residual Beal signatures. The intermediate target is conditional exact-level modular location at 7. Its downstream use is a precisely specified ambient Hilbert space for an irreducible-sector exclusion. Location leaves both packet exhaustion and global algebra applicability unresolved and does not meet the zero-solution threshold.

The continuation test was complete source-backed hypothesis coverage, including the characteristic-7 endpoint and both coefficient embeddings; an essential uncovered minimal-type premise would have parked the import. The test passes for direct citation of the theorem. It does not pass for independent reconstruction of its proof. The earlier restriction objection is now covered by L021; the historical type-to-level source blocker remains preserved.

## Primary theorem and essential cases

[Ariel Pacetti and Lucas Villagra Torcomian, *On the generalized Fermat equation of signature (5,p,3)*, arXiv:2512.17845v1, submitted 19 December 2025, Section 7.2, Theorem 7.8 and proof](https://arxiv.org/html/2512.17845v1#S7.SS2), works over K=Q(sqrt(5)) with a primitive solution a^5+b^p+c^3=0 and the plus representation specialized at -a^5/c^3. The paper's Section 1.3 allows primes p>=7 after treating the smaller exponents; 7.8 adds no exclusion of 7. Its premise is irreducibility of the residual representation at a coefficient prime over p. It states an isomorphism with the residual representation of a parallel-weight-two Hilbert newform of trivial character at exact level (3)^e3(sqrt(5))^e5, with a prime of the newform coefficient field over p.

With a0=a*5^(-v5(a)) and c0=c*3^(-v3(c)), its clauses are:

- e3=2 if 3 divides ab; if 3 divides c and either sign of 2*c0^3 is congruent to a^5 modulo 9; or if 3 does not divide abc and 4*c^3 is congruent to a^5 modulo 9. Otherwise e3=3.
- e5=2 if 5 divides bc; if 5 divides a and c^3/a0^5 is congruent to one of 6,12,28 modulo 25; or if 5 does not divide abc and c^3/a is congruent to one of 6,8,17,19 modulo 25. Otherwise e5=3. The denominators in their respective clauses are units. In particular the third clause really has denominator a, not a^5; preserve the source's notation in a later import.

The whole proof first invokes Theorem 2.4 and BCDF25 Theorem 3.13 for modularity/trivial character, then BD14 for parallel weight two and level equal to the prime-to-p residual conductor. It invokes Theorem 2.1 for support at 3 and sqrt(5). The e3 cases use Corollary 3.6 and Remark 3.7, with Lemma 7.3 removing the possible quadratic twist. The 3-divides-a case uses potentially good reduction from Proposition 7.4/Remark 7.5. For e5, the 5-divides-bc cases use Corollary 3.11/Remark 3.12 and the 5-divides-a case uses Proposition 7.4. The remaining congruence cases use Lemma 3.13's finite mod-25 irreducibility criterion and a cited source script. The tables, twist tests and finite computation are imported as parts of this stated theorem; their programs are not independently rerun or used as local certificates here.

These are substantive distinctions. Corollary 3.6 and Proposition 3.14 alone permit exponents 0 or 1 in some rows, so L019's upper bounds alone do not imply the exact four levels. Remark 3.8 warns that residual congruence does not generally determine the local type. Theorem 7.8's proof supplies the family-specific qualifications; a direct citation imports them. It has no extra hypothesis requiring the applicant to manufacture a minimal lift at 3 or 5. A later derivation from BD alone would still need the parked conductor and compatibility work and is outside this approval.

## Matching the notebook inputs

L019 has already justified (a,b,c)=(X,-Z,Y), p=7, t=-X^5/Y^3 and the geometric covariant weight-two Tate normalization. The coordinates are signed, primitive and nonzero; no positivity, odd-b or divisibility assumption is added by 7.8. Its K is both the base field F and the degree-two coefficient field of the geometric component. L020 gives absolute irreducibility under the displayed algebra assumption through each residue-field embedding of F_49. There is no coefficient-field-degree-one or F_7-valued premise in 7.8. A later import must specify the characteristic-zero/residual coefficient identifications separately for each embedding; the resulting form, prime or identification need not be the same. Nor does the theorem restrict the newform coefficient field to K.

The source's shortcut from irreducibility to absolute irreducibility need not be reconstructed: L020 supplies the stronger property directly. L021 supplies restriction irreducibility for the BD interface exposed by the earlier review. L022 supplies the actual crystalline lift with cyclotomic determinant at the base prime over 7. L023's audited local portion covers the required ordinary and nonzero-monodromy lines; it uses the actual local modules and saturated reduction, not local semisimplification. These remove the earlier uncovered interfaces. They are existing inputs and are not rederived in this literature turn. The source normalization is fixed by Remark 2.2 and the geometric identification already checked in L019; an additional Tate or quadratic twist is not approved.

## Duplicates, failures and source limits

The earlier direct-import assessment withheld approval because L019–L020 lacked the restriction assertion; L021 is the materially changed input. The post-restriction review then isolated the local lift, now supplied by L022, and the line audit, now completed in L023. The source-blocked independent type-to-level audit remains blocked, with the same Carayol/newvector retrieval evidence. It is neither used nor retried. No sibling notebook, archive, packet computation or original descent was read.

The source's Theorem A excludes p=7 from its elimination range. Its large-prime conclusions and the column counting forms whose coefficient field is K do not exhaust the forms at 7. The four-level location alone does not reduce the entire irreducible sector to L016's six displayed comparison polynomials. No claim of a new result beyond the checked literature or a signature solution is made.

This completes one source comparison. The ready mathematical continuation is recorded separately in `drafts/literature/2026-10-05-mixed-seventh-pvt-exact-level-citation.md` and receives the supervisor's separate next-turn approval. No lemma, DAG or mathematical script was changed.

## Mathlib

Full direct-import specialization, Hilbert newforms, level lowering and conductor coverage: **not checked**. PVT is the named mathematical input, not a Mathlib matching theorem or formal verification.
