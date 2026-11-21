# Normalized-width rounding source work1828

Completed literature-only source comparison. The saved target is the single dyadic
rounding of C033z's normalized coefficient before eight exact Newton steps,
with error<=2^-60, cost<=322 including clamps, and an explicit iterate
denominator bound independent of the input denominator. No grid, cost or
denominator formula is proved here.

Main gap remains L030-L032/C032a actual-Xi all-degree positivity; this
bounded arithmetic input could help later C033w interpolation and evaluation,
but conditioning, weights, TV<=2, observations, signed-height cancellation
and realization remain independent.

Local comparison read: C033z hypotheses/operation model,1802(14)-(17),
1810's explicitly charged comparison-bisection rounding, and1825's exact
normalization/Newton theorem/error/ledger;1823/1825 literature assessments
and ATTEMPTS/2026-11-19-unrounded-gmp-execution-budget-1823.md. The1810
mechanism is a local precedent, not an approved width-rounding theorem.
Preserve1823's15/780 profiles,0/8 scalars and six replayed1823b profiles.

Review test: inspect primary rounding/input-perturbation hypotheses and
rational representation results; distinguish rounded iterative algorithms
from a once-rounded coefficient with exact subsequent operations. Approve
only a separately testable specialization with every conversion charged;
otherwise name the missing source or mismatched hypothesis. This source
review cannot establish the simultaneous numerical contract.

## Discovery and reuse

Queries included `"reciprocal square root" "Newton" "rounding" error
analysis coefficient`, `"rational" "Newton" "denominator growth" square
root`, `"one" "input rounding" "Newton" "inverse square root"`,
`"rational Newton" "dyadic" square root denominator`, the title of the
Korzilius-Schoenmakers paper, and primary bisection/GMP-manual searches.
Scoped local searches covered the width/direct-positive-real assessments,
width/GMP histories and direct-positive-real/GMP failure records. The
relevant changed-algorithm exclusions and1810 precedent were read in full
where used; no earlier once-rounded width certificate was found there.
This is a bounded comparison, not a claim of originality.

LITERATURE_REASON:1823/1825/1827 cover exact coefficients only;1810 covers
Ihat accumulation only. The saved target changes a coefficient and asks
for denominator control. Reused1809's already inspected Johansson
arXiv1611.02831v1, Sections3.1.1-3.2 and5-5.1, pp5-8 derivative-enclosure
principles; no repeat search for generic interval arithmetic was needed.

## Inspected primary statements and relevant cases

1. Brent-Zimmermann, *Modern Computer Arithmetic*, v0.5.9,7 October2010,
   [Lemma3.14, printed p112, PDF page128](https://members.loria.fr/PZimmermann/mca/mca-cup-0.5.9.pdf#page=128).
   Reused1823/1825's assessment and reinspected the complete statement
   and Taylor proof. For positive a,x, rho=a^(-1/2), the update
   x'=x+(x/2)(1-a*x^2) satisfies
   0<=rho-x'<=(3*x^3/(2*theta^4))*(rho-x)^2,
   with theta between x and rho. It is exact arithmetic. Positivity and
   the normalized interval still need verification for the converted
   coefficient. The adjacent integer Algorithm3.9/Lemma3.15 is not
   imported; its exclusions are already documented in1823/1825.

2. [*The Bisection Method*, WPI MA3257 Spring2023 lecture23](https://users.wpi.edu/~bgu/sp23/ma3257/lecture_notes/MA3257_L23.pdf),
   pp1-2: read the algorithm, theorem and entire interval-halving proof.
   For continuous f on[A,B] with f(A)f(B)<0, its nth midpoint p_n
   approximates a root p with |p_n-p|<=(B-A)/2^n; the initial midpoint
   is p_1. The algorithm terminates at an exact midpoint root. This is
   the standard bisection theorem, not a theorem granting free conversion
   or dyadic membership. Later use for comparison with a coefficient
   must justify its linear sign test, endpoints/equality handling and
   indexing convention; no rounding precision was selected here.

3. Korzilius and Schoenmakers, [*Divisions and Square Roots with Tight
   Error Analysis from Newton-Raphson Iteration in Secure Fixed-Point
   Arithmetic*](https://www.mdpi.com/2410-387X/7/3/43),
   *Cryptography*7(3)(2023),43, DOI10.3390/cryptography7030043,
   publisher HTML,12 September2023. Read Sections5.1-5.3,
   Algorithm5, Theorems4-5 and their displayed proof cases, Remark6.
   Theorem4 reports error<2.71*2^-f on b in[0.5,2), with seed(9),
   iteration count(12) and fixed-point rounding within each iteration.
   Its proof separates zero,1-3 and>=4 iterations, invoking A5/A6 and
   numerical bounds; those auxiliary proofs/certificates were not audited.
   Theorem5 instead requires positive a in Q_(2f,f), Algorithm5 and
   f/2<=n<=f-2; its reported bound is
   (2^((f-1)/2-n)*2.71+1/2)*2^-f. Its cases distinguish scaling errors.
   Equation(13)/Remark6 omits higher-order coefficient terms. Neither
   theorem is imported: the domains, seed, internal rounding and cost
   model differ. No source-wide correctness is asserted.

4. [GNU MP6.3.0 manual, Chapter6, *Rational Number Functions*](https://gmplib.org/manual/Rational-Number-Functions):
   read the full canonical-form contract. Arithmetic assumes canonical
   operands and canonicalizes outputs; the denominator is positive and
   coprime to the numerator, and zero is0/1. Assignment need not
   canonicalize. This fixes the meaning of reduced denominator only;
   it supplies no bound on this Newton sequence or its running time.
   Reduction does not replace the required explicit expression-by-expression
   denominator accounting. No GMP operation is added to the allowed model.

## Access qualifications and noninputs

The author-hosted MCA source and publisher HTML were accessible. The
initial TU/e PDF request returned403; the inspected MDPI original supplied
the relevant material, so it is not an essential blocker. The FNC bisection
URL was inaccessible; WPI's primary lecture supplied the theorem/proof.
A Stanford slide's endpoint-sign typo is not used as a theorem. GMP's
extensionless URL intermittently failed; its .html redirect returned the
full22-line Chapter6 contract. Hardware inverse-root, Borges2112.14321 and
other search leads are unread/noninputs. No cross-notebook theorem is used.

## Completion and remaining local obligations

SPECIALIZE: source coverage suffices for a bounded costed specialization;
the simultaneous error/count/denominator result is not in the inspected
sources. No new lemma, numerical experiment or mathematical script was
created. This is source-scope progress only (EXPLORATION/REPRODUCTION),
not an RH advance or a newly proved numerical input. Full matching Mathlib
coverage was not checked and is not inferred absent.

The changed continuation in assessment1827 requires separate approval next
turn. Its later test must include all constant construction, normalization,
conversion comparisons and arithmetic, eight exact steps, rescaling and
clamps; positive closed-range containment, exact equality branches, full
coefficient/input error and every iterate's denominator bound. Original
input comparison cost in bits remains unrestricted. The existing record
of source/divisor/law qualifications and all unrounded execution stops
remains in force. No central signed-height/actual-Xi mechanism is supplied
by this numerical scope, so a creative nomination remains unjustified.

## Recovery1829: direct URL repair (2026-11-19)

The assessment's SOURCE_EVIDENCE now contains the direct primary URLs
already recorded above, plus the versioned Johansson URL reused from1809.
The exact construction target and SPECIALIZE comparison are unchanged.
This is the separate continuation approval requested in1828. No additional
discovery search, lemma, calculation or mathematical script was needed.

The MCA PDF, WPI PDF and MDPI HTML resolved again. MCA Lemma3.14's full
statement and Taylor proof were located at printed p112/PDF page128;
WPI's theorem remains on p2 and MDPI Theorem4 retains its fixed-point
seed/domain/iteration hypotheses. Neither fixed-point result becomes an
import. Both extensionless and .html GMP manual URLs returned502 in this
recovery; the previously inspected1828 contract is reused with that access
qualification. This transient failure is not missing essential coverage.
Johansson is reused without retrieval. The repair supplies no numerical
contract or new evidence about RH; it is honestly STALLED mathematically.
The next attempt must pass all three original thresholds simultaneously
and preserve all local and source qualifications listed above.
