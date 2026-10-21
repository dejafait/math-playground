# Source coverage for the five-probe obstruction audit

TARGET: Critically audit L086's five-probe reciprocity obstruction, including omitted places, all witness pairings and the distinction between envelope failure and global independence.
CHECKED: 2026-10-17
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the exact reciprocity searches and inspected primary coverage in 2026-10-17-primitive-eleven-global-comparison.md; narrowly compared L086 with L069/L073/L074/L077/L084/L085 and ATTEMPTS/038. No fresh external discovery search or source download was needed for this audit.
SOURCE_EVIDENCE: J.S. Milne, Class Field Theory v4.03 (6 August 2020), III Theorem 4.4 pp.113–114, V Theorem 5.3(a)/Example 5.4 p.179, VIII 5.8 pp.246–247, 5.10 p.247 and archimedean cases p.248; precise previously inspected statements and proof cases are reused from the prior assessment.
COMPARISON: These general theorems cover quadratic symbols and their global product, but do not certify L086's field-specific support, local ordering, valuation table or envelope inclusion; those are exactly the remaining mathematical audit.
GAP: Source coverage is ready for a separate critical audit of the existing proof; no correctness approval, global realization, independence, new dimension bound or integer exclusion is established in this source turn.
REASON: The new audit target required separate approval; its hypotheses and proof obligations fit the already inspected reciprocity coverage without a changed theorem or essential unread source.
LITERATURE_REASON: The saved Next action was REVIEW_REQUIRED; compare its finite audit obligations with existing coverage once, then return to mathematics.
SCOPE: Audit the existing fixed five-probe L086 only, retaining the exact T, all local factors and its outside-envelope witness; no probe enlargement or new sufficient certificate.

## Reused primary results and their scope

The primary source is Milne's [Class Field Theory, v4.03](https://www.jmilne.org/math/CourseNotes/CFTc.pdf).
The prior assessment records inspection of the local norm-criterion proof,
the odd-residue formula proof and the archimedean cases, as well as the
numbered statements above. This turn reuses that evidence; it does not
claim a new reading of the PDF. The prior search terminology included
Hilbert reciprocity, number-field product formula, local norms and
localization of Selmer conditions. Its exact-family comparisons and
GRH qualification of FNS remain applicable. No search failure is
interpreted as novelty or absence of a stronger theorem.

III.4.4 supplies bilinearity and the norm criterion over local fields
containing the relevant roots of unity. V.5.3(a)/Example 5.4 supplies
the product over all places for two nonzero global elements. VIII.5.8
supplies the residue calculation used at odd residue characteristic;
VIII.5.10 and p.248 retain global and infinite-place scope. L086 uses
n=2, characteristic-zero completions and a number field D, so no
missing roots-of-unity premise calls for a new source. The Q2 formula
on p.248 does not cover J and is not approved for use there. Identity
arguments must instead use the general bilinearity statement.

## Audit obligations compared with existing canonical interfaces

- L074, Hypotheses, defines W_S using even valuations outside ALL primes
  over 2 and 11, allowing negative valuations, and element-square norm.
  L077, supported generation and transport paragraphs, supplies actual
  maximal-ring probe ideals and integrality of both probes and inverses
  over Z[1/22]. Check their use in L086 for arbitrary W_S representatives,
  including non-unit and class-group contributions. The odd-place theorem
  has the required scope; its application still needs mathematical review.
- L069's real-algebra paragraph identifies R times C at each real base
  place. Check L086's extension from this algebra identity to arbitrary
  norm-square representatives, rather than assuming its unit statement
  already proves that extension. The real/complex symbol cases are covered.
- L073 and L085 fix both rational Q11 times M factors and all three L
  factors with the same theta. L077's exact prime identities supply the
  proposed valuation table. Check every entry, the normalized M valuation,
  and transport to BOTH rational base places; a citation alone does not
  verify this field-specific arithmetic.
- L084's definition imposes the two rational full-local conditions and
  the primitive dyadic subgroup, without the ramified eleven-adic full
  Kummer condition. Check the precise envelope inclusion using that T.
  L082 supplies its dyadic subgroup; L085 supplies the ordered J11.
  Check all witness norms and all five products, retaining identity
  factors in C, J and each copy of L. No unknown xi symbol is needed for
  the stated identity-dyadic witness; this is not authorization to omit
  an essential pairing if the actual proof uses one.
- Check that an outside tuple in a necessary envelope is used only to
  refute the sufficient containment certificate. No inspected theorem
  turns it into a global T-class or proves independence of the filter.

These comparisons specify the audit; they do not perform or approve its
mathematical conclusions. No lemma, proof overview, DAG or mathematical
script is changed in this literature-only step. Full matching and
supporting Mathlib coverage remain not checked; unknown is not absent.

## Duplicates, stopped routes and bounded continuation

ATTEMPTS/038 and history/280 already record failure of this fixed
sufficient test, not failure of reciprocity generally. The prior
assessment compared the affine failures and parked class backend;
none is reopened. This is a verification target, not another attempt
to evaluate or enlarge the envelope. No additional source is essential
for the stated finite audit, and no new source blocker was found.

Essential input IDs: L069, L073, L074, L077, L082, L084, L085, L086.
Continue with the exact TARGET under this SPECIALIZE assessment,
classified REPRODUCTION. Accept L086 only if every omitted place,
local norm, witness symbol and logical implication checks independently.
If any check fails, isolate and correct the specific defect and preserve
the stopped-route evidence; do not infer global independence or expand
the test. Actual loc_11(T), class-kernel values, full units, rank and
integer lifting remain unresolved. No cross-notebook input is used.
