# Imaginary-shift lead after the fixed differential stop — nomination2032

TARGET: Review the Meixner-Pollaczek imaginary-shift difference equation and zero-count theorems for finite-difference operators against C029m's full tilted family, and nominate one bounded coefficient-identity test only if exact hypotheses and recorded stops permit it.
CHECKED: 2026-11-20
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step2033 checked imaginary-shift/difference-equation, exceptional-zero and inverse-Pollaczek terminology; reused discovery2029 and the recorded metric/residue/affine/differential stops. No inspected source establishes the actual inverse-family half-plane count; failed searches imply neither novelty nor absence.
SOURCE_EVIDENCE: DLMF18.22.16-18 (https://dlmf.nist.gov/18.22#ii); Katkova-Tyaglov-Vishnyakova1608.03924v2 Proposition1.1 and Theorem2.2/proof pp2,4-5; their1901.06398v1 Theorem1.10 pp5,19-21; de Bruijn1950 Lemma2/full proof p215 and Theorem9a p203 (https://repository.tudelft.nl/file/File_524a4d3c-0858-4c55-b425-8c8ce1fb89da). Exact scope and access qualifications below.
COMPARISON: The basis equation has degree-dependent eigenvalues, not one eigenvalue for the weighted sum. Forward preservers do not pay the input zero premise. The known polynomial real-part lemma permits a distinct fixed-operator inverse/half-plane screen, without claiming that screen passes or giving an eventual family bound.
GAP: Exact inverse coefficients, degree and the multiplicity-counted threshold below Im(t)=-2 remain uncomputed. Uniformity in N, singular/boundary cases, initialization and the qualified convergence/upstream[9] bridge remain open.
REASON: Primary coverage supports one known-method inverse screen using the fixed Pollaczek operator, rather than another root count of T_6 or a repetition of the parked differential range. The new screen needs separate approval before mathematics.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target had no imaginary-shift coverage; newly inspected primary statements and the exceptional-zero proof are essential to assessing this different operator.
SCOPE: Completed literature-only step2033. No inverse computed, coefficient identity verified for U_6, root count obtained, lemma added or mathematical script changed. The separately nominated finite screen is a specialization, not a creative uniform-family claim.

## Completed source comparison2033

The main gap remains L030-L032/C032a actual-Xi all-degree mixed
positivity. C029m offers only a conditional alternative: an eventual
uniform Hermite negative index at most one. The intermediate source
target was a fixed imaginary-shift coefficient identity with a
plausible route to that bound. Continue only if the source controls
the actual full sum through a checkable input condition; abandon an
automatic basis-to-sum or forward-to-inverse inference.

### Exact equation and its scope

[NIST DLMF18.22.16-18](https://dlmf.nist.gov/18.22#ii), inspected
20 November2026, states, for P_n=P_n^(lambda)(x;phi),

    A(x)P_n(x+i)-(A(x)+C(x))P_n(x)+C(x)P_n(x-i)
      +2n sin(phi)P_n(x)=0,
    A(x)=exp(i phi)(x+i lambda),
    C(x)=exp(-i phi)(x-i lambda).

C029m uses lambda=3/4, phi=pi/2 and x=t/2, hence shifts in t
are +/-2i. These parameters meet the standard positive-lambda,
0<phi<pi restrictions. The relation concerns polynomials, so its
real-x identity extends polynomially; no complex-shift limit is
needed. Its n-dependent scalar cannot be pulled out of the full
weighted sum. The proposed inverse below is to be checked using
this equation, not assumed from preservation. No new difference
equation is proved here.

### Preservation is conditional; an exceptional-zero input is available

Olga Katkova, Mikhail Tyaglov and Anna Vishnyakova,
*Linear finite difference operators preserving Laguerre-Polya class*,
[arXiv:1608.03924v2](https://arxiv.org/pdf/1608.03924v2),
3 September2016: Proposition1.1, p2, treats nonzero polynomial
coefficients multiplying shifts of a real-rooted input. Theorem2.2,
pp4-5, treats meromorphic M and f in the Laguerre-Polya class:
f(z+i)+M(z)f(z-i) has real zeros only, or vanishes identically,
when M is strictly contractive above and expansive below, or is a
constant of modulus one. Reused the October7 complete proof coverage;
rechecked the displayed hypotheses and product-modulus sufficiency
cases, including zero-free exponential/Gaussian inputs. These are
forward statements. They provide no actual-family inverse root count.

The same authors, *Hermite-Poulain theorems for linear finite difference
operators*, [arXiv:1901.06398v1](https://arxiv.org/pdf/1901.06398v1),
18 January2019, Theorem1.10, p5, classifies constant-coefficient
shift operators preserving a prescribed strip: perpendicular step,
symmetric stencil and unit-circle generating roots. The proof begins
on p19. Inspected its necessity setup, not the entire proof or its
additional simplicity assertion. It does not directly cover the
variable-coefficient Pollaczek operator. Its p25 complex-zero-decreasing
remark is a lead, not the imported theorem used for this nomination.

N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math.
J.17(3) (1950),197-226, DOI10.1215/S0012-7094-50-01720-0,
[publisher scan via TU Delft](https://repository.tudelft.nl/file/File_524a4d3c-0858-4c55-b425-8c8ce1fb89da),
Lemma2, p215: for real polynomials U,V, if W=U+iV has n zeros
in the open lower half-plane, U has at most n nonreal conjugate
pairs. Read its complete proof: remove common real factors; the
case deg(W)<2n is trivial; otherwise the argument change supplies
real zeros, with separate treatment when the leading real part
vanishes. Counts include algebraic multiplicity. The zero real-part
case cannot be used as a nonzero output.

Also inspected Theorem9a and its short reduction to Lemma2, p203:
the real entire input has order<2, exactly 2k zeros outside a closed
strip of half-width Delta, shift lambda>=Delta>=0, and a nonzero
conjugate coefficient pair. Its shifted sum has at most 2k nonreal
zeros. The following p204 warning rejects the analogous fixed-strip
count when the shift is too small. No entire-function specialization
of that theorem is needed for the proposed polynomial screen.

The p215 polynomial lemma is the relevant broader input. A later
application must identify the real part and count the input zeros;
it cannot replace that count by an LP assertion or an unsigned
norm bound. No reproof of this standard theorem is justified.

### Bounded nomination, not an application performed here

Nominate the fixed operator

    B h(t)=(3/4-it/2)h(t+2i)+(3/4+it/2)h(t-2i).

For C029n's full U_6, the proposed test is to solve B h=U_6 in real
polynomials of degree at most six, verify every coefficient, and
certify whether h has at most one zero below Im(t)=-2, counting
algebraic multiplicity. No coefficient, inverse or root was computed.
The source basis equation suggests a fixed inverse filter, not a
common eigenvalue assertion. Its normalization, degree and existence
must be verified in the mathematical step.

Prospective use: a later application of Lemma2 would examine
W(t)=(3/4+it/2)h(t-2i) and verify its real part is U_6/2.
The half-plane count and the prefactor's zeros are explicit
application obligations, not established conclusions of this review.
An eventual uniform version for the inverse full family could feed
C029m; a finite pass cannot establish it. The shift and coefficients
are fixed by the source equation before root information, unlike
fitting a quadratic or a phase to the numerator.

The separate assessment
`2026-11-20-pollaczek-shift-inverse-halfplane-screen-2033.md`
specifies the full threshold and allowed certification. Reject this
baseline on a certified threshold failure; unresolved boundary
enclosures are inconclusive. A pass licenses no degree campaign or
uniform extrapolation. Repeating the test would require materially
new family structure. A genuinely creative central attempt remains
unjustified until such a uniform coefficient/half-plane mechanism
is identified; routine inversion is not relabeled creative.

### Search, reuse and limitations

Queries included `Meixner Pollaczek imaginary shift difference operator
nonreal zeros decreasing theorem finite difference`, `Meixner Pollaczek
difference equation DLMF18.22`, `Katkova Tyaglov Vishnyakova finite
difference operators strip nonreal zeros decreasing polynomials`,
`Meixner-Pollaczek zero decreasing difference`, and exact Pollaczek
combinations with `Hermite-Biehler`, `nonreal difference Kuznetsov`
and `inverse zero difference operator`. No inspected source supplies
the proposed actual inverse's half-plane bound; novelty is unassessed.
Recent Meixner/Sturm-Liouville and representation-theory search hits
remain unread and are not essential inputs to this finite screen.

Reused discovery2029, fixed-reference discovery2026, the October30
actual-theta coefficient/weight mismatch, and the November5 Pólya
shift-residual scope stop. Targeted local searches found no matching
fixed inverse-Pollaczek screen. The latter historical stop concerns
reference-to-forced-function transfer, not this polynomial identity.
C029m/n/s were read in full; C029l's Rouché source coverage was reused.
Kuznetsov's (9) and Propositions4.1-4.2 were checked at their exact
source passages; neither substitutes the auxiliary coefficients for
the full beta family. No older failed route was erased or reopened.

The TU Eindhoven de Bruijn scan exposed only cover-page OCR; the
TU Delft copy supplied the complete relevant primary text. Local
curl retrieval failed DNS; browser primary-text access succeeded.
Screenshot requests supplied no inspectable image to this interface,
so no visual-scan audit is claimed. The clearly parsed p215 statement
and full proof suffice for the polynomial specialization; no ambiguous
product-formula inequalities in the 2016 paper are imported.

Outcome EXPLORATION: one bounded source review prepares a distinct
known-method screen; no actual-family estimate or mathematical advance
beyond the inspected sources. No lemma, mathematical script, PROOF,
DAG, shared infrastructure or supervisor state changed. No calculation
budget was spent or reset. Mathlib coverage for the full application
and supporting half-plane theorem is unchecked; no absence claim.

Essential continuation inputs: C029m exact family/conditional context,
C029n U_6 and unchanged rational enclosures, DLMF18.22.16-18,
de Bruijn Lemma2, and the standard Rouché theorem covered in C029l.
C029s is stop evidence only. Uniformity, actual-degree/singular cases,
initialization and qualified weighted convergence/upstream[9] remain
unresolved. No cross-notebook theorem input is used.

## Original nomination2032, preserved

This is an uncovered source-review target, not a ready mathematical
continuation. No difference equation, coefficient law, zero-count
inequality or new lemma was derived in audit2032. The next turn is
literature-only. Retrieve primary theorem hypotheses and essential
proof cases before larger passages. Reuse discovery2029 and its
referenced local stops rather than repeating those searches.

Main gap: actual-Xi all-degree mixed positivity in L030-L032/C032a;
the prospective downstream alternative is C029m's eventual uniform
full-family index bound. The concrete source test is whether an
imaginary-shift operator theorem has an exact coefficient-identity
test on this full family that is independent of the parked mechanisms.
Do not treat a basis-polynomial difference equation as an identity
for a weighted sum with varying eigenvalues. Do not substitute an
auxiliary expansion or discard odd coefficients.

Continue to a separately nominated bounded mathematical target only
if the operator, coefficient identity and source hypotheses can be
stated exactly and a plausible uniform downstream use is identified.
Otherwise record a specific source or hypothesis obstruction and
park this lead. No new degree/precision campaign or generic
preservation assertion is approved. A later creative attempt would
need that concrete mechanism and a decisive bounded test; none is
invented here to satisfy scheduling balance.

Essential local context: C029m for the exact full-family definition
and its conditional bridge; C029n for finite normalization; audited
C029s for the fixed differential stop. Discovery2029 and its named
local stops are comparison evidence, not new mathematical premises.
Eventual uniformity, actual-degree/singular cases, initialization,
preimage/root control and qualified weighted convergence/upstream[9]
remain open. No cross-notebook input. Mathlib coverage unchecked.
No readiness or source-coverage claim is made by this nomination.
