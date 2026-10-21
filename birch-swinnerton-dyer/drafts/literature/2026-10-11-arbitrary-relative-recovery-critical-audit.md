# Arbitrary-relative recovery — completed separate audit coverage

TARGET: Critically audit L049's arbitrary-relative exact recovery, checking cusp matrices and orientation, certified shrinking Fourier/AGM enclosures, both total-period factors and integer isolation including zero.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the unchanged construction assessment's exact-statement/stronger-result searches; read full L049, L048's statement and audit qualifications, ATTEMPTS/022--024 and history/163; reopened only the primary transport, cusp-equivalence, Fourier-tail and real-period passages needed for this audit.
SOURCE_EVIDENCE: Inspected Wuthrich arXiv:1608.06423v2, version 2017-03-23, primitive (2), Lemma 4 with full proof pp.6--7 and Section 5.1 (11)/matrix construction pp.11--12; Cremona corrected second edition (1997), Proposition 2.2.3 with full proof pp.16--17, (2.4.1) with adjointness pp.18--19, total-period convention p.30, (2.9.1)/arbitrary-cusp remark pp.31--32, Section 3.7 both real-root cases pp.97--98; DLMF 19.8.1--19.8.5.
COMPARISON: Known analytic identities cover L049's unchanged curve/cusp/period scope, but do not directly certify its finite-function error schedule or combined integer isolation. SPECIALIZE authorizes a separate critical check of this known-algorithm assembly, including two source sign pressure points, without a new method or executable instance claim.
GAP: L049's matrix multiplication, reduced-cusp cases, orientation, complete shrinking finite errors, period factors and zero-inclusive isolation have not passed their separate mathematical audit.
REASON: Essential audit coverage is now available by reusing the construction review and comparing its precise imports with the complete L049 proof; source approval does not establish the assembly's correctness.
LITERATURE_REASON: The newly proposed critical-audit action was REVIEW_REQUIRED; compare its exact sign, finite-error and termination scope separately while reusing adequate construction coverage.
SCOPE: Full L049 under its unchanged global minimal E/Q, exact conductor/associated newform with computable finite coefficient segments and supplied complete integral generating paths; CM, additive reduction, nonunitary cusps, zeros and both real-component cases; audited L048 is the sole local mathematical input.

## Initial proposal retained

The following proposal predates the completed review below; its approval
instructions and REVIEW_REQUIRED status are historical.

The sole proposed Next action is TARGET. Its independent audit should
check the entire canonical statement and proof of L049, with L048 as its
only local mathematical input. Preserve the source qualifications in
L048. The supplied exact minimal curve, conductor/newform with computable
finite coefficient segments, and complete finite integral generating
paths remain explicit hypotheses. No cross-notebook input is proposed.

Reuse the construction assessment's primary statements and complete
proof cases wherever adequate. Check whether any exact audit claim needs
unread essential coverage; do not repeat broad searches or certify
generic software. Specific pressure points are reduced cusp cancellation,
the sign of the transporting matrix congruence, the orientation of (6),
the rational Fourier-tail bound (8), finite-function error allocation,
one-real-root positivity even when d<0, both component factors, the
fixed-iteration/refined-precision AGM schedule, and integer existence
versus uniqueness, including zero. These are proposed checks, not new
theorems or completed reviews.

Continue to mathematical audit only after separate IMPORT, SPECIALIZE
or EXPLORE coverage for this exact action is recorded. If a missing input
or orientation/error defect is found, name it precisely and repair or
narrow the assembly. Passing an audit would make a theoretical recovery
input available; it would produce no executable instance, coefficient
nonvanishing, rational point certificate or complex-order comparison.

## Completed comparison — 2026-10-11, BSD-164

The main gap remains rank E(Q)=m(E) for arbitrary m(E)>=2. The single
intermediate target is TARGET. A successful audit would make L049's
theoretical normalization recovery available for later production of
L027 inputs. It would neither produce those inputs nor ensure a nonzero
coefficient. This literature turn establishes source coverage only.

### Primary passages and applicability

Reuse the exact-statement and stronger-result searches recorded in
`2026-10-11-arbitrary-relative-exact-recovery.md`; no changed mathematical
hypothesis requires a new broad search. Its Sage comparison excludes
using conditional software normalization as an unconditional theorem.
The published Wuthrich version remains an unread lead; v2 suffices here.

[Wuthrich v2](https://arxiv.org/pdf/1608.06423v2), printed pp.6--7,
Lemma 4 assumes positive height and positive requested error. Its complete
proof gives the geometric-series tail exp(-2*pi*H*y)/(exp(2*pi*y)-1)
using |a_n|<=n. Section 5.1, (11), printed pp.11--12, applies to
Gamma_0(N)-equivalent reduced cusps and any interior tau. Neither
analytic identity uses Manin constant one; the paper's global practical
normalization does. Its matrix paragraph's extracted display reads
c=c_0+t*m*m', whereas L049 (3) uses a negative t term. Section 5.2
also has the previously recorded closing-sign concern. These are source
comparison pressure points, not established corrections. Recompute the
matrix entry and oriented primitive difference in the mathematical audit,
using Cremona's criterion and Hecke identity rather than treating either
printed sign as authoritative. The retrieved PDF title page says
24 March 2017; its arXiv version stamp is 23 March 2017. Earlier title-page
date descriptions are not relied on.

[Cremona Chapter 2](https://johncremona.github.io/book/fulltext/chapter2.pdf),
Proposition 2.2.3, pp.16--17, includes all three equivalence criteria and
the constructive congruence proof for reduced cusp fractions. Read every
implication, including the final solvability criterion. Equation (2.4.1)
and its integration-adjointness proof, pp.18--19, require a good prime
and retain all ell+1 terms. Equation (2.9.1) and its arbitrary-cusp
remark, pp.31--32, cover a good prime 1 modulo N. The p.30 convention
retains the two total-period factors. Its optimal-form period
identification is not an input for an arbitrary target equation.

[Cremona Chapter 3](https://johncremona.github.io/book/fulltext/chapter3.pdf),
Section 3.7, pp.97--98, gives periods for the supplied Weierstrass
equation. Equation (3.7.1) uses ordered real roots and positive square
roots when the discriminant is positive. The negative-discriminant
paragraph instead uses z=s+it, s>0, and lambda_1=pi/AGM(|z|,s).
Both full real-root cases were inspected. Their floating-point root
algorithm is not an outward-enclosure certificate. L049's algebraic
branch choice and target minimal differential must be checked separately.

[DLMF 19.8(i)](https://dlmf.nist.gov/19.8.i), equations
19.8.1--19.8.5, assumes positive initial AGM inputs and gives iteration,
common-limit convergence and integral identities. It supplies no
rounded-arithmetic precision schedule. Sturm isolation, Dirichlet's
theorem, Machin's identity and Taylor's remainder theorem remain standard
named inputs, as in the unchanged construction coverage.

### Difference that the separate audit must check

Known identities are imported, not reproved. Limited sign verification
is justified by the two extracted source displays and L049's fixed
orientation. The remaining difference is its combined exact-arithmetic
assembly. In particular, no inspected source directly certifies L049's
rational tail majorant, complex Taylor budget, finite interval-polynomial
width, aggregate signed-generator budget, fixed-iteration AGM refinement,
positive period division or zero-inclusive scaled-integer stopping test.
These are explicitly covered audit tasks, not results of this review.

Check the full canonical L049 statement and proof, not just selected
formulae: finite eligible-prime search; cancellation of ell in reduced
Hecke cusps, including numerator zero; arbitrary Bezout choices and matrix
entry; all transport terms and orientation; the full tail and finite
function errors; both positive AGM inputs including d<0; the minimal
differential and both component factors; inner and outer refinement
termination; signed interval division; integer existence from L048 before
uniqueness; zero and empty-generator conventions; final integral extension.
Do not assume a presentation or arithmetic implementation has been audited.

L048 supplies a fixed clearing integer, not merely a denominator size
bound. Retain its audited hypotheses and its qualified named Kenku and
Manin inputs. Its source originals remain unread as already recorded;
this unchanged audit does not reopen them or assert a new verification.
No cross-notebook input is used. Full matching Mathlib coverage and
supporting formal algorithms remain not checked, with no absence claim.

ATTEMPTS/022--024 and history/163 were read. Those stops prohibit repeated
conditional verification as input production; they do not duplicate the
first separate audit of L049's different recovery assembly. The blocked
uniform twist-source route stays parked. Preserve all unfinished work.

### Decision and discriminating test

SPECIALIZE approves exactly TARGET/SCOPE for one subsequent mathematical
audit, classified REPRODUCTION. Continue only if each load-bearing step
survives its exact source hypotheses and explicit error/termination
checks. Repair or narrow on a concrete unsupported matrix, orientation,
branch, period factor or error claim; do not infer failure from a historical
stop, or correctness from documentation validation. No further literature
is essential unless the audit discovers a changed hypothesis or new
load-bearing input. This turn neither audits L049 nor derives new results.

A passing audit would still grant exact conductor/newform arithmetic and
complete integral paths. Executable certificates, practical bounds,
coefficient nonvanishing, rational directions, Sha defects and complex
order comparison remain unresolved. This is local source-coverage progress,
not progress beyond the checked numerical-modular-symbol methods or a BSD
candidate.
