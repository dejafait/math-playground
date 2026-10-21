# Separate audit of the fixed seven-torsion algebra: source coverage

TARGET: Critically audit L067's full 7-torsion algebra, coordinate maps and complete finite replay for y^2+y=x^3+x^2-2x.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the completed construction assessment and its exact-model, division-polynomial and finite-field searches; compared the full L067 proof with the audit obligations, L030's model arithmetic, history/238--239 and ATTEMPTS/034. Reopened the primary sources below; no new discovery search or claim of novelty.
SOURCE_EVIDENCE: Sutherland, MIT 18.783 Fall 2023 Lecture 5, Sections 5.5--5.6, pp. 9--14, Lemmas 5.20/5.22/5.24 and Theorems 5.21/5.25; Schaefer--Stoll, author long version 2001-06-13, Section 5 step 2, printed p. 9; Lenstra, Factorization of Polynomials, Section 5 Test 2, printed p. 181, reused from the inspected construction assessment (fresh page retrieval failed).
COMPARISON: The imported kernel, separating-function and irreducibility criteria cover the proposed fixed audit; exact coefficient identities, faithful inverse maps and complete finite witnesses still require independent instance scrutiny. No new general theorem or recurrence reproof is needed.
GAP: Source coverage is ready, but the separate mathematical audit and fresh complete replay have not been performed; production reports alone do not certify that audit. No downstream descent arithmetic is covered by this approval.
REASON: The changed audit target required separate comparison; its essential hypotheses and proof cases are covered by the prior inspected results, with the instance obligations specified below.
SCOPE: Only the exact TARGET, including complete original evidence replay, distinct exact arithmetic cross-checks and bounded altered-evidence checks preserving original bytes; excludes new torsion production, enlarged search caps, descent functions, units/classes, local bounds and Selmer conclusions.
LITERATURE_REASON: Audit-specific coverage was REVIEW_REQUIRED at invocation start; compare full-kernel identification, faithful coordinate transport and complete irreducibility evidence with the previously inspected construction sources before mathematical audit.

## Primary coverage and specialization

[Sutherland, Lecture 5](https://math.mit.edu/classes/18.783/2023/LectureNotes5.pdf),
Fall 2023, pp. 9--14, covers the short-Weierstrass division polynomials,
multiplication coordinates, degrees and absence of cancellation.
Theorem 5.25 supplies degree and separability. Reopened Theorem 5.21,
Lemma 5.24's adjacent-multiple contradiction and Theorem 5.25's proof;
reuse the previously inspected parity and recurrence proof cases.
Characteristic zero meets the restrictions. The audit must verify the
origin-preserving change and its inverse before applying these inputs.
The source theorem, rather than a new reproof, supplies the general
kernel interpretation; every fixed recurrence coefficient and the
squarefree/disjointness witnesses remain audit obligations. The printed
proof of Theorem 5.25 contains a degree-bound typo relative to Corollary
5.23; use the latter's explicit degree statement, not that printed bound.

[Schaefer--Stoll, long version](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
13 June 2001, Section 5 step 2, printed p. 9 (PDF page 9), was reopened.
It requires the chosen function to be defined at every point of the
chosen finite Galois set and to separate them. Its characteristic product
presents the function algebra, with rational irreducible factors giving
orbit fields. The suggestion of a y-coordinate does not assert separation
for this curve. Thus the audit must retain both coordinates and verify the
whole power matrix and both inverse products, rather than infer separation
from the source's suggestion. This is only the algebra step; the source's
later units/classes and cohomology/local-image steps are independent.

[Lenstra, Factorization of Polynomials](https://infoscience.epfl.ch/server/api/core/bitstreams/3154505c-23e7-4fd4-be73-e8c8b9c85951/content),
Section 5, Test 2 (Rabin), printed p. 181, is reused from the complete
inspection recorded in the construction assessment. Its degree-n test
requires the full q^n power congruence and coprimality for every prime
divisor of n. For the claimed degree 48, the saved tests at indices 16
and 24 must be checked along with the complete chain through 48, not
sampled powers. Retain primehood, degree preservation, invertible
coefficient denominators, primitive integer polynomial and the
Gauss-lemma passage. Fresh initial PDF extraction returned metadata,
but follow-up text and screenshot retrieval failed at the signed redirect.
This does not erase the prior inspected coverage or establish a theorem
from an unread search result; no new source claim depends on that refresh.

## Exact audit obligations and decision test

The essential local inputs are L067, L030's exact nonsingular model and
all original scripts/seven-torsion/ evidence. No cross-notebook input or
L026 premise enters. The prior assessment is
[the construction coverage](2026-10-15-conductor389-full-seven-torsion-algebra.md).
The full L067 proof was read to compare obligations, without executing or
certifying its arithmetic in this literature-only turn.

1. Check both coordinate substitutions, every recurrence coefficient,
   degrees, both rational Bezout identities and the two-coordinate basis.
   Check the imported kernel theorem's applicability to the entire nonzero
   torsion set, including the exclusion of O and absence of canceled points.
2. Reconstruct every saved power and both full matrix inverse products;
   retain all coefficient slots through degree 48. Verify annihilation,
   both coordinate transports, defining equations and every generator
   product. A characteristic polynomial or resultant alone is insufficient.
3. Replay the complete primitive-integer and modular witnesses, all
   Frobenius powers and both full modular Bezout identities. Verify the
   single-factor identity/maps as well as rational irreducibility; no
   software factorization label or residual-surjectivity premise suffices.
4. Read and run the independent verifier on the complete original input,
   then add a distinct exact arithmetic check of a load-bearing identity
   or irreducibility criterion. Recheck intended corrupted-coefficient and
   missing-map failures using copies and fresh reports. Preserve original
   bytes, including producer-draft-v0.json; its degree-47 padding defect
   stays explicitly excluded. Rejection tests supplement complete replay.

Pass only if full kernel, basis, inverse-coordinate and field
identification all survive exact scrutiny. On failure, isolate the
unsupported assertion and preserve valid partial evidence; do not enlarge
the production caps or silently repair and approve new mathematics here.
The audit is known-method REPRODUCTION under SPECIALIZE, not a new result.
No mathematical calculation was performed in this source comparison.

History/239 records production rather than a prior completed critical
audit; this is not duplicate audit work. ATTEMPTS/034 parks repeated
conditional-interface work, not this independently checkable arithmetic
input. ATTEMPTS/021/032/033 and the capped zero remain unchanged.
A successful audit could certify L066's global algebra component only.
Functions, embeddings/local factors, complete units/classes, local upper
bounds and full Selmer-space containment remain absent. L026 residual
nonvanishing is unverified; divisible Sha, successful localization,
rational membership and arbitrary-curve complex-order comparison remain
unresolved. The main rank-equality gap is unchanged.

Mathlib: matching kernel, coordinate-algebra and finite-certificate
coverage was not checked; no absence claim is made. Precise mathematical
citations and the fixed proof remain canonical in L067; this assessment
changes readiness only, not the argument or its pending-audit status.
