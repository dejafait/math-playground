# Proposed critical audit of the marked-octic factorization

TARGET: Critically audit L115's complete rational factorization certificate and identification of the entire octic algebra as one degree-eight field.
CHECKED: 2026-10-22
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the unchanged construction assessment's exact-instance and standard-method searches; compared L115's full claims and imported criterion with that coverage, L114's input/interface, history/400–401 and ATTEMPTS/050–051. No new exact-instance search is needed for verification of the same certificate.
SOURCE_EVIDENCE: Reuse drafts/literature/2026-10-22-marked-octic-rational-factorization.md: Milne, Fields and Galois Theory v5.10 (September 2022), 1.8 pp.10–11, Propositions 1.13–1.14 p.12, Remark 1.18 p.14, Proposition 4.20/Corollaries 4.21–4.22 pp.53–54 and Exercise 4-8 p.60; statements and supporting proof cases already inspected there, not newly fetched here.
COMPARISON: Every method used by L115 is within the prior Gauss/reduction, Bezout and finite-field criterion coverage; the required difference is independent instance verification, including the entire quotient and multiplicity. LLL and the unread Rabin original are unnecessary; two passing implementations are not a critical audit.
GAP: Source approval is complete; independent verification of the actual coefficients, Frobenius/division evidence, Bezout identity, theorem hypotheses and entire-field conclusion remains for the mathematical audit.
REASON: This separate literature turn establishes that the existing inspected criteria suffice for the unchanged audit target; SPECIALIZE permits a later REPRODUCTION audit, without a general reproof or any claim of novelty.
LITERATURE_REASON: The startup gate requires a separate comparison for the newly proposed critical audit; reuse existing essential sources and close that scope review without repeating browsing.
SCOPE: Exactly TARGET for unchanged L114–L115 and their full selected-prime certificates; independent exact verification and whole-algebra interpretation only, excluding larger prime searches, maximal orders, class/unit computations and point methods.

The main gap is marked rational-point control and eventual primitive
integer exclusion. This audit's intermediate target is reliability of
the sole-degree-eight-field input before later supported-class arithmetic.
Essential inputs are L114–L115, audited L113's unchanged G, and both full
factorization certificates with their scripts. No cross-notebook input
is used. Retain L109 marking and L110–L111 transport for interpretation;
there is no new point transport in L115.

The later mathematical audit should reconstruct all nine coefficients,
positive content and monic scalar, trial-certify 19 and both nonzero
leading residues, independently recompute every selected Frobenius
residue and the Bezout identity, and check the exact degree-eight
irreducibility criterion. Inspect the complete relevant trace when
verifying its claimed completeness, and distinguish failed modular tests
from rational reducibility. Check why a single primitive irreducible
factor yields the entire quotient field with no lost component or
multiplicity. Do not infer maximality of the polynomial order.

Pass only if every selected residue, product/scalar, gcd witness and
theorem hypothesis agrees; otherwise correct or park the unsupported
claim. Preserve startup work, ATTEMPTS/050–051, unfinished L108 and all
earlier recorded failures. No larger prime search is needed for this
audit. Class/unit data, full local images, point completeness, root
recovery, remaining factors, both L095 systems and minus-eleven stay
unresolved. The completed comparison below finds no essential additional source
coverage for this unchanged audit; no source-level novelty is claimed.

## Completed source comparison, not a mathematical audit

The construction assessment is reusable: neither G, the base field nor
the finite-field criterion has changed. Its primary reference is J. S.
Milne, *Fields and Galois Theory*, v5.10, September 2022,
[author PDF](https://www.jmilne.org/math/CourseNotes/FT.pdf). The earlier
assessment records the inspected statements and relevant proofs; this
turn reads and reuses that evidence, rather than claiming a fresh fetch.

The audit must check monicity after multiplication by a nonzero residue
scalar, degree preservation at the selected prime, and the primitive
integral input needed by Gauss. Exercise 4-8 applies to monic degree n
polynomials over F_p: it requires X^(p^n)=X modulo the polynomial and
a coprimality certificate for X^(p^(n/r))−X for every prime divisor r
of n. No irreducibility assumption on the input is a premise of this
test. The Frobenius/factor results cited above cover its use, and 1.8
covers an exact Bezout witness. L115's claimed degree is eight, so the
later audit must verify that its selected proper-index check is precisely
the one prescribed by this criterion. No listed residue or identity has
been recomputed in this literature turn.

The product/content and multiplicity claims must be checked independently
of finite-field irreducibility. The whole-algebra interpretation uses
the standard polynomial quotient-field theorem: over a field, the ideal
generated by a nonconstant irreducible polynomial is maximal, and its
quotient has dimension the polynomial degree. Checking the equality of
the two principal ideals under a nonzero rational scalar is essential;
a chosen root alone would not certify the entire algebra. This is an
elementary applicability check within the assessed factorization scope,
not a new number-field result or an assumption about its integer ring.

L114 supplies the unchanged octic/interface and support containment. It
does not require an extra field-discriminant or order-maximality theorem
for this audit. Its real-place convention and rational infinity images
remain intact. L109–L113 transport and marking are context, not new
calculations requested here. L095's different octic and its Eisenstein
argument supply no input about this one. The reviewed rank failures are
independent of certification; they are preserved, not reopened.

The independent audit should inspect all selected-prime division witnesses
and the complete relevant Euclidean evidence whenever it verifies the
certificate's completeness claim. Earlier unsuccessful prime tests need
not be rerun to establish the selected certificate; any assertion about
the search history must be checked against the full relevant records or
explicitly left unverified. No enlarged search is authorized. If a
load-bearing equality or hypothesis fails, correct or park that claim
before using it for supported-class arithmetic.

Full matching Mathlib coverage remains not checked; no absence is inferred.
This approval adds source readiness only. It neither certifies L115 nor
establishes a new mathematical result beyond the sources checked.
