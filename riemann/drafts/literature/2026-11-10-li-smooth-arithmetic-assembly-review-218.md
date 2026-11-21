# Smooth-model and ordinary-Li assembly — completed source comparison

TARGET: Assess the smooth-model/arithmetic matching needed to combine L978 and L979 into S_f(n)+lambda_n(sqrt(n))=O(sqrt(n) log n) with the weak finite cutoff.
CHECKED: 2026-11-10
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused reviews214/216 and the Li source/failure comparisons212/213/158; screened the local November10 Li/tail records for a completed assembly. Searched exact Li/Arias/truncated-zero, Lagarias/erratum and Li/smooth/tail terminology; no additional matching primary theorem was inspected.
SOURCE_EVIDENCE: Rechecked Arias de Reyna author version31Jan2011 Thm1 and complete proof pp.4-5, normalization p.1 footnote/(6) p.2; Lagarias AIF57(2007), (1.1)-(1.5) p.1690, Definition4.3/Lemma4.4 and proof pp.1708-1709, Thm5.1/(5.1)-(5.4) pp.1712-1713, (6.1) p.1721; v4 HTML cross-check confirms ordinary normalization and GL(1) inclusion.
COMPARISON: The published smooth J1 estimate and unconditional archimedean trend display the same constant; the exact arithmetic identity includes delta=1. These known inputs support a bounded assembly specialization after L978/L979, not import of the defective Section6 proof or of an unconditional whole-Li asymptotic.
GAP: The corrected residual is still unproved locally. Required work is smooth-integral normalization, the lower smooth interval, radial-to-height paired summation, exact head/tail splitting and error assembly with weak endpoints; finite-head signs remain independent.
REASON: Essential source scope is adequate for the stated standard calculation. Import the inspected smooth estimate and arithmetic identity, proving only their specified cutoff/convergence specialization. This literature-only step derives no new bound or assembly.
SCOPE: Fixed actual zeta; integer n>=2; ordinary undivided Li coefficients and L977 eta convention; all multiplicities; weak head |Im rho|<=sqrt(n), complementary tail strictly above; no RH, simplicity, zero-table or finite-head sign assumption.
LITERATURE_REASON: The incoming REVIEW_REQUIRED assembly extends beyond L979; its essential smooth-integral normalization and ordinary-Li/cutoff comparison had not been approved. Reuse prior counting/integration coverage without refreshing it.

## Completed comparison, step219, 10 November 2026

The main gap is actual-Xi all-degree positivity (L030-L032/C032a),
with the signed forcing in L966 also unpaid. A corrected residual
would separate a controlled tail from the actual growing finite head;
that head still needs independent lower control before L968 can apply.

### Primary source evidence

J. Arias de Reyna, *Asymptotics of Keiper-Li Coefficients*,
[author version, 31 January 2011, Thm1/proof pp.4-5](https://personal.us.es/arias/56-2RHB.pdf#page=4),
uses a positive nondecreasing sequence with multiplicity and
N(t)=t*log(t/(2*pi*e))/(2*pi)+O(log t). Its proof defines

    J1(m)=2/(pi*m)*integral_0^infinity
              sin^2(m*arctan(1/(2*t)))*log(t/(2*pi)) dt
          =(log m+EulerGamma-1-log(2*pi))/2+O(log m/m).

Read both endpoint cases in its g(y)/y^2 remainder, the extended
integrals and constants on p.5. This is the smooth part alone.
The theorem's l2 conclusion concerns the counting-error part; its
RH corollary is not used. The p.1 footnote and (6), p.2, distinguish
divided Keiper coefficients from ordinary Li coefficients. The
next calculation must match J1 to L979's K_n, retaining the factor n.

J. C. Lagarias, *Li coefficients for automorphic L-functions*,
AIF **57**(5) (2007), 1689-1740, DOI10.5802/aif.2311,
[Definition4.3 and Lemma4.4, pp.1708-1709](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=21),
states lambda_n=S_infty(n)-S_f(n)+1 for the self-dual trivial GL(1)
case. Use (4.5)/(4.8), not the inconsistent separate remark (4.13).
[Thm5.1, (5.1)-(5.4), pp.1712-1713](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=25)
is unconditional, with N=Q=1, kappa=0, K=0 and
C1=(EulerGamma-1-log(2*pi))/2, and an O(1) archimedean remainder.
[Equations(1.1)-(1.5), p.1690](https://www.numdam.org/item/10.5802/aif.2311.pdf#page=3)
use ordinary coefficients and radial star summation with orders;
(6.1), p.1721, uses the weak height cutoff. These are different
exhaustions: the next proof must justify their agreement after pairing.
The completion 2*xi and GL(1) inclusion are explicit on p.1697;
reuse L964/L968's normalization justification. No Section6 bound is
imported. Published numbering is canonical; v4 has different numbers.

### Applicability, missing specialization and bounded test

The proposed local inputs have been inspected: L018 preserves zero
orders and conjugation, L013 excludes real nontrivial zeros, and L978
gives absolute conjugate-paired tail convergence as well as displacement.
Together they provide the existing setting for reconciling the radial
source sum with a height sum. This reconciliation must be written,
not asserted for the unpaired conditionally convergent series. Do not
replace the finite head by real-ordinate model terms.

L979 already establishes the excluded-lower-atom Stieltjes identity
and absolute integrability on (sqrt(n),infinity). Reuse its counting
and NBV coverage from review216. A smooth Lebesgue integral has no
cutoff atom; the actual counting function does. All zeros at the
cutoff must remain in the head with their complete orders. No
zero-avoiding height perturbation or half-weight convention is needed.

The precise remaining elementary obligations are to normalize the
displayed J1 integral to K_n; control its removed interval (0,sqrt(n))
using L979's global bound 0<=K_n<=4 and local integrability of log t;
check convergence at 0 and infinity; then combine the sourced
archimedean/arithmetic identities with L978/L979 and a justified exact
head/tail split. These are tasks for the next mathematical attempt,
not estimates established here. Source constants agree literally;
no new identity is needed to define S_f or its delta term. Any
finite initial asymptotic range must be included in one fixed-zeta
constant. No effective numerical remainder constant is promised.

Continue if these tools produce the requested O(sqrt(n)*log n)
uniformly for n>=2 without an RH-dependent equality. Stop this
specialization if a non-summable rearrangement, a missing smooth
constant or an unsigned-to-signed inference is required; record the
actual failed identity. Success supplies no signs for the actual head
and does not close L968's whole-coefficient lower-bound threshold.

### Duplicates, failures and limits

Reviews214/216 and step218's history nominate this assembly but do
not prove it. L977's contour sign/majorant stop, L976's coefficient
envelope stop and the parked Coffey2007 access route remain intact.
Review158's inspected ordinate-only/RH-equivalence warning is reused.
The source J1 estimate already covers the smooth work; reproducing
its full proof is unnecessary. Only the listed normalization and
cutoff differences justify further local calculation.

Queries were `"Li coefficients" "Arias" "truncated" zeros`,
`"Lagarias" "Li coefficients" "erratum"`, and
`"Li coefficients" "smooth" "sqrt" "tail"`. Returned author
bibliographies supplied no inspected correction; no absence claim
follows. Other AI notebooks, snippets and unrelated results were
not theorem evidence. Both primary PDFs were accessible as text;
screenshots returned placeholders, so no visual verification is claimed.
No essential source blocker remains. Mathlib coverage of the full
assembly is unchecked/unknown; no formal theorem is imported.

Outcome: EXPLORATION, LITERATURE, NOVELTY_UNCHECKED. The useful result
is completed source comparison and a precisely bounded specialization,
not a mathematical advance beyond the sources checked. No lemma,
mathematical script, DAG edge or PROOF argument is changed. A separate
ready continuation is recorded in review219 for next-turn approval.
Creative finite-head work still lacks an independently testable new
sign mechanism in these inputs; ordinary assembly is not creative.

## Original nomination from step218 (superseded coverage status)

The following text is preserved as the pre-review nomination. Its
pending-coverage statements describe that earlier stage.

Use actual zeta, n>=2, all multiplicities, no RH or simplicity, and
lambda_n(T)=sum_(rho: |Im(rho)|<=T)[1-(1-1/rho)^n]. Retain the actual
finite head; do not replace its terms by their real-ordinate model.
S_f is the ordinary eta convention in L977, from Lagarias (4.5)/(4.8).
The intended eventual mathematical target is the corrected residual
displayed in TARGET, not the unsigned or wrong-sign contour formula.
L018, L977, L978 and L979 are essential local context; L968 supplies
only the downstream whole-Li lower-bound benchmark.

First compare the already inspected sources and the narrow local Li
failure records. Retrieve only the precise additional hypotheses or
cases needed for the matching. Review214's model theorem is normalized
by n and concerns real ordinates; its later RH corollary is not an
unconditional actual-zero identity. Its smooth integral and Lagarias's
unconditional archimedean trend may be sufficient tools, but this
nomination does not establish that claim. L977's Section6 contour stop,
L976's envelope stop and the parked Coffey2007 route remain intact.

Approve IMPORT or SPECIALIZE only if the constants, ordinary-Li
identity and weak-cutoff cases are actually covered by inspected
source statements/proofs. If there is a missing essential identity or
an RH-dependent substitution, record that obstruction instead of
repairing it by assumption. No new estimate or assembly is derived in
this nomination. Even a successful residual will leave the actual
growing finite head unsigned, so it would not meet L968's threshold.

No independently testable creative finite-head sign mechanism is
justified by the present source inputs. This concrete normalization
comparison is the next unresolved task; do not label it creative or
reopen the failed horizontal majorant merely to change route names.
Mathlib coverage of the proposed assembly remains unchecked.
