# Global transition hypotheses for L489 — completed source comparison

TARGET: Review source coverage for using the de Bruijn–Newman transition theorem and Polymath's Lambda<=0.22 bound to discharge L489's transition hypotheses under failure of RH.
CHECKED: 2026-10-30
DECISION: IMPORT
SEARCH_EVIDENCE: Exact Newman 1976 title/theorem searches and narrow L058/L062/L488/L489, positive-transition assessment and endpoint-failure checks; inspected the original paper's definitions and Theorem 3/proof, using the exact modern primary restatement where scan extraction corrupts inequality glyphs. No novelty claim follows.
SOURCE_EVIDENCE: C. M. Newman, Proc. AMS 61 (1976), 245–251, Theorem 3 p.247, definitions (1.1)–(1.4) pp.245–246, https://sites.math.northwestern.edu/~auffing/papers/Newman.pdf ; D. H. J. Polymath, arXiv:1904.12438v2 (4 August 2019), introduction (1)–(4), paragraph after (4), Theorems 1.1–1.2, Sections 8.1–8.2 and the numerical-method context in 8.4, https://arxiv.org/html/1904.12438v2 .
COMPARISON: The named threshold theorem and unconditional upper bound supply the global source statements needed by the proposed application; source time 0.22 is strictly below 1/2. L488 already supplies the exact t=4lambda normalization. Neither source states theta-specific exclusion of a finite collision.
GAP: No essential theorem-statement coverage gap remains for this import. The explicit local application to both L489 assumptions is deferred to a separately approved research turn; original source proofs and numerical certificates remain independently unaudited.
REASON: This replaces an uncovered global threshold premise by precise known source statements, making a bounded applicability step available without reopening tail or endpoint-energy proofs. It is local source progress, not new mathematics beyond the sources checked.
SCOPE: Completed literature-only review. Import the named global theorem and Theorem 1.1 as stated, not a locally verified numerical certificate; no lemma or mathematical script is changed. The separate continuation assessment specifies the pending specialization.
LITERATURE_REASON: The exact target changes from L488's local replay to global transition existence and a strict upper time bound; essential theorem-to-hypothesis coverage is not supplied by the unchanged audit assessment.

## Exact known statements and inspection limits

Newman's *Fourier Transforms with Only Real Zeros*, DOI
[10.1090/S0002-9939-1976-0434982-5](https://doi.org/10.1090/S0002-9939-1976-0434982-5),
uses the negative Gaussian exponent exp(-b u^2). Theorem 3 on p.247
gives the finite transition for that specific xi family. Its short proof
uses Theorems 1–2 and the theta density's faster-than-quartic decay.
The classification proof of Theorem 2 was not audited. The original
scan's inequality glyphs in the theorem are corrupted in extracted text;
the closed endpoint is accepted from Polymath's exact primary restatement,
not inferred from that OCR or search snippets. Screenshot calls supplied
no inspectable image through this tool; shell retrieval failed DNS and
the AMS mirror returned 403. These do not block the accessible primary
restatement. No original-scan inequality is newly certified here.

In [Polymath v2](https://arxiv.org/html/1904.12438v2), the paragraph after
(4) states a finite real Lambda with all zeros of H_t real **if and only
if t>=Lambda**. It also identifies RH with Lambda<=0. Theorem 1.1
states Lambda<=0.22 unconditionally. Section 10's conditional improvements
are separate. Sections 8.1–8.2 implement Theorem 1.2 using verified finite
zeta heights, a final-time asymptotic region and an intermediate-time
barrier. These numerical verifications are accepted by citation, not
replayed; Section 8.4's mesh/derivative discussion was inspected only to
identify that obligation. No infinite RH assumption or simplicity premise
is attached to Theorem 1.1 or the threshold statement.

Theorem 1.2's complete three hypotheses and conclusion were read; its
conditional criterion must not be substituted for the unconditional
Theorem 1.1 without its verifications. Its proof and the full Section 8
computation are outside this review. The known threshold theorem is used
by citation rather than reproved. Exact full matching Mathlib coverage is
unchecked; this is not evidence of absence.

## Applicability comparison and bounded continuation

The gap towards RH remains exclusion of positive-time finite real
collisions (or another proof of actual-Xi all-degree signs). The intermediate
target is to discharge L489's two existence assumptions under failure
of RH and then use its already audited conditional conclusion. Its
downstream value is a finite collision obstruction in place of an
unactivated conditional statement; it does not exclude that obstruction.

Essential inputs are L018/L058 and the qualified, locally audited
L488/L489. L488's existing identity is F(lambda,z)=8 H_(4lambda)(2z);
the spatial substitution preserves reality and multiplicity. The source
bound 0.22<1/2 has the required strict margin for the open local range.
The closed threshold statement covers the side of all-real slices;
its strict complement covers nonreal slices. Writing their exact local
quantifiers, including an increasing incoming sequence and a common
positive-time interval, is the pending applicability task, not a new
theorem established in this literature turn. No endpoint simplicity or
Lambda>=0 theorem is needed as an added premise.

Continue only if that application verifies both L489 assumptions at one
lambda_* in (0,1/8) without assuming RH, simplicity or uniform control
as lambda tends to zero. Otherwise record the exact failed implication
and stop the import. No lemma or PROOF.md claim is added here. See
[the separate continuation](2026-10-30-global-transition-specialization.md),
which requires its separate approval before mathematical invocation.

Duplicate/failure check: L058 is local and L062 assumes initial global
reality plus a boundary exhaustion; neither supplies global threshold
existence. L489 leaves precisely these transition assumptions conditional.
Its compactness argument and L488's replay are already audited and are not
repeated. The parked endpoint inverse-gap source application and L487's
generic energy obstruction are not being reopened or bypassed.

## Recovery comparison

Three different gaps were considered after completing the audit.
First, theta-specific finite-collision exclusion remains central, but
no new sign or arithmetic estimate currently separates a proposed test
from the generic shape and L487 energy obstructions. A creative label
would not be justified. Second, direct positive-endpoint inverse-gap
integrability retains the recorded lower-endpoint Hamiltonian loss and
unread CSV proof; no new input justifies reopening that source route.
Third, the selected global transition question uses named threshold
theorems to address the existence hypotheses left conditional in L489.
It is independently testable and does not require either blocked
mechanism. Local splitting is already covered by L059/L060 and is not
another proposed result. This nomination neither resolves RH nor
establishes a new collision mechanism.
