# Power-order sufficient interface — approved critical-audit coverage

TARGET: Critically audit L058's sufficient power-order certificate interface and exact lattice verification specification.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the extension/fractional-ideal/HNF searches recorded in drafts/literature/2026-10-11-global-eleven-order-extension-certificate.md; compared the full L058 scope and relevant L033/L041 hypotheses with audited L045 coverage and ATTEMPTS/013,025; narrowly reopened the three cited primary sources to check theorem hypotheses and the rectangular HNF case. No novelty search or witness search is claimed.
SOURCE_EVIDENCE: Lynn Extension and Contraction, second operations list item 3; Milne ANT v3.08 (2020), Corollary 3.13 printed p.51, fractional-ideal definitions printed pp.52–53, Example 3.19 and Theorem 3.20 printed p.53, class-group definition printed p.54, Theorem 3.29 and proof printed p.57; official PARI mathnf integer-matrix flags 0,1 and rectangular example. Existing L045 audit coverage is reused for its quotient criterion.
COMPARISON: The inspected general inputs cover the unchanged ring-extension, maximal-ring valuation/class and exact column-module methods; the field-specific prime identification and verification soundness remain mathematical audit obligations. Sources do not certify L058, supply a witness or evaluate u.
GAP: Independently check every local exponent, fractional extension, ordinary-class implication and exact finite lattice certificate in L058; no new essential source gap was identified within this scope.
REASON: Approve reuse for exactly the saved critical audit; its hypotheses and methods fit the prior inspected coverage, while the mathematical correctness of the specialization remains unreviewed.
LITERATURE_REASON: The newly selected critical-audit target required separate coverage approval; focused source confirmation resolves that gate and does not justify another literature turn on unchanged hypotheses.
SCOPE: Exactly TARGET, using L058 and direct inputs L033, L041 and audited L045. No witness search, verifier implementation, class computation, enumeration, equivalence of restricted certificates with u=0 or branch-emptiness inference.

## Primary coverage and qualifications

Reuse the ready [interface assessment](2026-10-11-global-eleven-order-extension-certificate.md)
and [L045 audit coverage](2026-10-10-global-eleven-criterion-critical-audit.md).
Their original searches and source versions remain the evidence for known
results and terminology; no failed search is evidence of novelty.

Ben Lynn, [Extension and Contraction](https://crypto.stanford.edu/pbc/notes/commalg/extcon.html),
live authored notes accessed 2026-10-11, no revision date identified:
read the arbitrary ring-homomorphism definition, warning that extension
need not preserve primality, and product identity in the second operations
list, item 3. These support checking integral product extension. They do
not license contracting a maximal-order identity back to R or assuming
invertibility of arbitrary R-ideals. Fractional denominators remain an
explicit obligation in the later audit.

J.S. Milne, [Algebraic Number Theory](https://www.jmilne.org/math/CourseNotes/ANT.pdf),
v3.08, July 19, 2020: reopened Corollary 3.13 and its localization proof,
fractional-ideal definitions, Example 3.19, Theorem 3.20 and its
integral/fractional factorization proof, the class-group definition,
and Theorem 3.29 with its proof. Printed locators are pp.51–54 and 57;
PDF page indices are one greater. The hypotheses are Dedekind domains
and, in 3.29, finite separable field extension. L033 supplies the fixed
number field; these results concern its maximal integer ring. The
strongest relevant conclusion is fractional ideal factorization and
classes modulo principal ideals, rather than arithmetic of a nonmaximal
power order. No reproof of these standard results is needed.

[PARI official mathnf documentation](https://pari.math.u-bordeaux.fr/dochtml/html/Vectors__matrices__linear_algebra_and_sets.html#mathnf),
live HTML accessed 2026-10-11, no release number identified: reopened the
complete flags 0,1 statement and its rectangular 3-by-4 example. The
input may be nonsquare over a Euclidean ring; the specialization here
is integer matrices. The output columns span the input column module;
flag 1 gives an invertible transformation with M U=[0|H]. Full row rank
makes H square. This supports exact certificate checking after common
rational denominator clearing. It does not establish backend availability,
execution, enumeration completeness or runtime. L058's explicit two-way
integer inclusion alternative also lies within this elementary module
scope. No implementation is approved by this review.

## Boundaries of the separate mathematical audit

The following are obligations, not conclusions independently established
in this literature turn:

- Check L033's exact polynomial and degree-twelve power basis against L058;
  use L041's entire ordered maximal-prime data, including the degree-ten
  place. Audit J at every prime, with the normalized orders and residues,
  rather than use power-order factorization or primality under extension.
- Check denominator-cleared extension for arbitrary fractional A and every
  integer e. Audit the stronger ordinary-class consequence and its passage
  to audited L045; retain all valuations outside S and the claimed explicit
  two-vector consequences. Do not silently replace arbitrary prime-five
  freedom by the principal rational-five factor.
- Check rank, nonzero alpha, k-stability, all product generators, exact
  compression and equality of entire modules. Audit the sizes and
  unimodularity conditions for rectangular HNF certificates, the common
  denominator, and both integer inclusions. Rank, covolume and norm alone
  are insufficient verification. Necessity and sufficiency refer to
  checking supplied lattice data, never to existence of such data.

No additional source is essential to these checks under the saved
hypotheses. A changed target (witness construction, software verification,
class computation or completeness) would require its own assessment.
No independent audit or new mathematical derivation occurred here.

## Relevance, duplication and continuation test

The main gap is unconditional integer emptiness of surviving ordered
(3,4,11) branches and the other residual signatures. The intermediate
target is confidence in L058's sufficient certificate interface. Its
plausible downstream use is checking a future positive identity witness
and its eleven-valuation consequence; it cannot be an absence test.
L058 is the existing canonical result to audit, not a reason to create a
duplicate lemma. ATTEMPTS/013's finite norm search failure and
ATTEMPTS/025's certified-enumeration/backend blocker are preserved;
this audit neither repeats those implementations nor requires them.
The primary target version is reused from the already checked foundation
record cited in the preceding assessment; no change of Beal's target occurs.

Continue with exactly the approved mathematical audit. Its discriminating
test is validation of every implication and verifier condition, or an
explicit defect/correction with the failing hypotheses named. Park the
interface if its soundness needs missing arithmetic, unsupported R-ideal
inversion or a completeness assertion; reassess any newly essential source
before dependent research. Approval here closes a coverage gate only.

Essential inputs: L058, L033's exact field/power basis, L041's complete
ordered eleven places, audited L045's quotient and dichotomy. L044 is the
retained downstream local filter through L045, not a new theorem input.
Unresolved: independent L058 audit; no identity witness or verifier
execution; u, global unit compatibility, other places, global points and
integer-power lifting remain open. No cross-notebook input or GRH premise.
Full matching and supporting Mathlib coverage are not checked; unknown
availability is not absence. Outcome EXPLORATION records completed source
comparison and approval, not mathematical progress beyond known sources.
