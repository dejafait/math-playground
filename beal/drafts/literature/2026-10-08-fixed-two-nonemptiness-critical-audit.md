# Fixed-two nonemptiness — critical audit coverage

TARGET: Critically audit L039's complete B_2 identification and its inference that I_pow and I_fiber are nonempty.
CHECKED: 2026-10-08
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L039's actual proof scope with the fixed-one and fixed-two assessments, foundation 17, L033-L036 and L038; searched the targeted calculation draft, history/098-099 and ATTEMPTS/008-011 for duplicates and stops. Existing primary coverage suffices for this audit; no fresh external search or certificate verification was performed.
SOURCE_EVIDENCE: Reused previously inspected Milne ANT v3.08 Theorem 7.33 and Remark 7.36, Corollary 7.42 and Remark 7.43, Proposition 7.50 with proof; FNS final author manuscript June 10, 2019 Section 7.2, Table 5 and equation (7.4); Clark ANT II Theorem 1.79 and Schaefer-Stoll Section 5 as qualified below.
COMPARISON: Standard lifting and unramified classification cover the proposed factor pairing; existing audited map/descent inputs and L036 cover transport and common witnesses. The explicit coefficient and finite-field certificates still require an independent arithmetic and applicability audit, not a reproof of general theory.
GAP: No essential theorem coverage is missing for this exact audit. Coordinate completeness, every certificate identity, residue irreducibility, complete product pairing and the nonemptiness inference remain mathematically unaudited.
REASON: The saved target now has matched source coverage; a separate research turn can audit L039 without widening to varying-scalar images or global emptiness.
SCOPE: Exactly L039's existing complete B_2 identification and restricted-image nonemptiness, including all direct inputs and full relevant certificate values; no new scalar tests, class lists, strictness decision or global exclusion.
LITERATURE_REASON: The supervisor requires separate approval of the newly written L039 audit target; this comparison checks coverage for its complete-algebra and common-witness inference, reusing ready primary assessments.

Inputs for the proposed continuation: L033's f and connecting map; L034's
full map and exceptional coordinates; L035's exact sets; L036's primitive
common-scalar construction; L038's complete A identification; L039 and
scripts/full-fiber-at-two/factor-certificate.json. No cross-notebook input.
This assessment approves the scope of a subsequent mathematical
audit. Review must retain every factor and distinguish local witnesses
from global integer solutions. Neither strictness nor global emptiness is
an audit premise or conclusion. This literature step checks source adequacy,
not the certificate or correctness of L039.

## Source comparison and qualifications

Reuse [the fixed-one assessment](2026-10-08-full-fiber-at-one-local-algebra.md)
for the primary statements and relevant proof cases actually inspected, and
[the fixed-two assessment](2026-10-08-full-fiber-at-two-local-algebra.md)
for the unchanged scalar-specific search scope. Neither is claimed newly
retrieved. The explicit B_2 result is local work already in L039, not a new
discovery in this review; failed searches do not establish originality.

J. S. Milne, [Algebraic Number Theory v3.08, July 19, 2020](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
Theorem 7.33 and Remark 7.36, printed pp.121-123, lift monic pairwise
coprime residue factors over a complete DVR. Corollary 7.42 and Remark
7.43, p.124, give degree ef. Proposition 7.50 and proof, pp.127-128,
classify unramified extensions by residue extensions under the stated
perfect-field hypotheses. The audit must check monicity, integrality,
coprimality, irreducibility and residue degree before applying these
results to Z5 and Q5. Equal degree alone would not identify ramified
fields. L039 proposes only unramified factors, so Clark's Krasner and
separable-algebra stability theorems need not supply a precision cutoff.
The finite-field Frobenius factor-degree criterion used in L039 is the
standard factorization of X^(5^n)-X into all monic irreducibles whose
degrees divide n. Its explicit remainders and Bezout witnesses, including
the degree-eleven primality case, are audit objects, not verified here.

Freitas-Naskrecki-Stoll, *The generalized Fermat equation with exponents
2, 3, n*, Compositio Math. 156 (2020), 77-113,
[June 10, 2019 final author manuscript](https://www.mathe2.uni-bayreuth.de/stoll/papers/genfermat-final.pdf),
Section 7.2, printed pp.25-28, Table 5 and equation (7.4), provides the
field and modular-map data. L034's prior independent audit records
coefficient and exceptional-coordinate checks. Lemma 7.6 concerns specified
Q2 domains and excludes 54a1 in its statement; it cannot decide this Q5
fiber. Neither GRH-dependent Selmer dimensions nor the full classification
is an input. Compare the certificate's complete source coefficients to
these existing inputs rather than assuming elimination preserves points.

Pete L. Clark, [Algebraic Number Theory II](https://plclark.github.io/PeteLClark/Expositions/8410FULLL.pdf),
161-page version retrieved 2026-10-08, revision date unidentified,
Theorem 1.79, printed p.58, supplies the strict Hensel-Newton inequality
for integral polynomials over complete valued fields. Foundation 17 and
L036 already specialize it to unit cube and eleventh roots; the audit
must retain one common c and primitive integral coordinates. Schaefer-Stoll,
*How to do a p-descent on an elliptic curve*, Trans. AMS 356 (2004),
1209-1231, [June 13, 2001 long manuscript](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf),
Section 5, pp.8-10, with the Section 9 isogeny pairing, is reused through
L033's audited connecting-map normalization over every completion. L035's
definitions permit all whole-fiber isomorphisms and a scalar witness
shared across factors. No new descent theorem or reproof is needed.

## Relevance, stopping test and remaining gaps

Main gap: global emptiness for every residual signature, including five
surviving twists for ordered (3,4,11). Intermediate target: critical
verification of this single local nonemptiness input. Its plausible use
is a reliable nonempty baseline for future I_pow versus I_fiber comparison;
it cannot alone exclude integers. ATTEMPTS/008-010's global arithmetic,
constant-norm and unrestricted-baseline failures remain intact.
ATTEMPTS/011 rejects j=1 only; L038 does not certify B_2. History/099
records a calculation, not an independent audit of it, so this is not a
duplicate completed review.

Continue if exact reconstruction accounts for every geometric point,
every residue factor and witness checks, both dimensions total twelve,
and the full pairing and common-witness inference follow with their
hypotheses. Repair a concrete defect or withhold the affected conclusion
if any check fails; do not convert incomplete evidence into emptiness.
Inspect complete load-bearing certificate values next turn, without
sampling or precision guesses. Image strictness, global intersections,
the five twist exclusions and infinitely many signatures remain unresolved.
Full matching and supporting Mathlib coverage is not checked; unknown
coverage is not evidence of absence.
