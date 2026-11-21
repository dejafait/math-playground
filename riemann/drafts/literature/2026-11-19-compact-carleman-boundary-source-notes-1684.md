# Compact Carleman boundary comparison1684

Literature-only completed record, 2026-11-19. Exact target is the unchanged
TARGET in nomination1683. No mathematical result or lemma is being proved.

## Preserved findings before further extraction

Read C028b's actual normalization/criterion and C028g's hypotheses,
summability and origin-exclusion contracts; C028d's finite signed-log
statement and C028f's uniform-tail statement; source-notes1507 and
stop1602's unpaid-sign warning. No existing work is discarded.

Located B. Ya. Levin, *Lectures on Entire Functions*, AMS Translations
of Mathematical Monographs 150 (1996), Section 24.1, pp.187--188,
equations (1)--(2), boundary discussion and Remark 1:
https://lib.ysu.am/disciplines_bk/fdf9c65b4685d7860d18d2bae6895160.pdf .
Read the finite semi-annulus hypotheses, Green-formula derivation,
zero/pole contributions, inner-arc remainder, real-boundary indentation
instruction and origin limit. The extracted preliminary Green equation
has inconsistent factors compared with the final formula: do not use
that intermediate OCR as a certificate. PDF screenshots timed out;
the final formula is also being compared with another primary text.

Levin's final zero weight is exactly the weight in TARGET; this is
classical accounting, with no theta-specific nonpositive boundary bound.
The remainder includes a radial derivative and cannot be dropped merely
because the inner disk is zero free. Detailed source comparison and
the route decision are recorded below. The two YSU text extractions agree
on the final formulas. Screenshot retrieval failed on both mirrors, and
shell retrieval failed at DNS; these failures do not prevent reading the
final statement. No visual verification of the printed scan is claimed.

## Primary formula and essential cases

**Levin**, cited above, Section 24.1, equations (1)--(2), pp.187--188;
[second text-accessible mirror](https://lib.ysu.am/open_books/417657.pdf).
For nonzero meromorphic f near the closed upper semi-annulus
rho<=|z|<=R, initially with no boundary zeros/poles, set u=log|f|.
The final formula is

    sum_a (1/|a|-|a|/R^2) sin(arg a)
      -sum_b (1/|b|-|b|/R^2) sin(arg b)
      = B_f(rho,R)+O_f(R)+A_f(rho,R),
    B_f(rho,R)=(1/(2pi)) integral_rho^R
                   (t^(-2)-R^(-2)) log|f(t)f(-t)| dt,
    O_f(R)=(1/(pi R)) integral_0^pi u(R exp(i theta)) sin(theta) dtheta,
    A_f(rho,R)=-(1/(2pi)) integral_0^pi
        [(rho^(-2)+R^(-2))u(rho exp(i theta))
          +(rho^(-1)-rho/R^2) partial_rho u(rho exp(i theta))]
               rho sin(theta) dtheta.

Here a,b are interior upper-half-plane zeros,poles with multiplicities.
The proof removes small disks and applies Green's formula with
v=-Im(1/z+z/R^2); zero/pole logarithmic singularities supply the sums.
Levin then treats real-boundary zeros/poles by small semicircle
exclusions and limits. Their multiplicities are unrestricted.
Circular boundary limits are mentioned, but not needed here: both radii
are chosen zero free. Remark 1 gives, for f(0)=1,
lim_(rho->0) A_f(rho,R)=Im f'(0)/2, at fixed R. Fixed rho gives
A_f(rho,R)=O(1) as R grows; this is not a nonpositive bound.

**A. A. Goldberg and I. V. Ostrovskii**, *Value Distribution of
Meromorphic Functions*, English AMS text (2008), Chapter 1 Section 3,
Theorems 3.1--3.2, equations (3.1)--(3.2), pp.10--11,
[accessible text](https://citeseerx.ist.psu.edu/document?doi=4d027fb513dcadf933b62d5c9ca2b70cc1179600&repid=rep1&type=pdf).
Read both statements and the complete relevant proof through the
derivation of Theorem 3.1. Equation (3.1) independently confirms the
two outer/real coefficients above; its Q(R,R0;f) is the inner remainder.
Theorem 3.2 writes that remainder as a Green boundary integral and
handles singular inner-circle points by changing R0 before limiting.
This is supporting coverage, not an independently useful sign estimate.
The source's OCR drops 'meromorphic' from one statement; its surrounding
theorem/proof supplies the intended meromorphic setting. Actual F is
entire, so no weak-boundary meromorphy extension is required.

The search also found Yang et al., *A note on the number of zeros of
polynomials*, Ann. Polon. Math.100.1 (2011), p.27 Lemma1,
https://www.impan.pl/shop/en/publication/transaction/download/product/84981 .
Read Lemma1 and its immediate use. Its half-disk display omits the
f(0)=1 normalization required by the origin-integral version. It is
not used to remove the inner term or bypass real-axis singularities;
Levin's fully stated annular formula suffices. No source correction
theorem is claimed or reproved here.

## Applicability and the failed sign discriminator

C028g supplies the actual entire F with F(0)=1, real positive
coefficients and a zero-free origin disk. Choose rho=r within that
disk and R>r avoiding all zeros on its circle. Thus there are no poles,
both circular boundaries are nonsingular, and only real-axis zeros need
the source's indentation convention. Its zero weight matches TARGET:
(1/|w|-|w|/R^2)sin(arg w)=Im(w)(|w|^(-2)-R^(-2)).
This is an applicability comparison of a known formula, not a new
Carleman theorem or new lemma. No general reproof is justified.

The needed inequality is for the COMPLETE functional B_F+O_F+A_F.
None of the three cited Carleman statements asserts it is nonpositive.
Zero-free inner disk does not delete A_F at fixed r. The fixed-R
origin limit in Levin's Remark 1 has zero derivative contribution
when f=F, since F'(0) is real; that specialization still does not
sign the real-boundary and outer-arc terms. No simultaneous r,R limit
or global actual-F logarithmic identity is established in this turn.
Local real zeros are logarithmic singularities, not permissible finite
values of log|F|, and no simplicity assumption removes them.

C028d concerns the full signed integral of a finite centered polynomial;
its negative exterior term does not sign the different weighted actual-F
boundary functional. C028f's summable escaping-root allowance and
C028g's finite S_F leave compact mass unpaid. An unsigned majorant,
finite-degree root census, or an order estimate cannot be called the
missing sign. Stops1507/1602 remain in force at their original scopes.

The theta-specific search located **Michel Planat**, *A Theta-Kernel
Reformulation of Riemann-Xi Growth and the Obstruction to Blockwise
Positivity*, Symmetry18(8)1283 (2026),
https://doi.org/10.3390/sym18081283 . Read Theorems1--3, their displayed
proofs and the orientation discussion in Sections2--3.3. Its claimed
global growth positivity is explicitly RH-equivalent; its exact coupled
theta identity does not assert the complete Carleman boundary inequality.
We do not import its global sign as a premise or audit its later
blockwise obstruction theorem here. Its later correlated-grouping ideas
are unread leads, not ready mechanisms or evidence of impossibility.

Also inspected **Suvrit Sra**, *On some positivity properties of the
Riemann Xi function*, author-hosted riem-xi-v3.pdf, accessed2026-11-19,
https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf : normalization(1.2),
Theorems1.1--1.3 and PropositionC.25's statement in SectionC.17,
printed pp.1--3,44--45. Its h is notebook F, while its F is normalized
Xi: keep the two conventions separate. The stated positive reciprocal
laws, finite PF order and fixed-order positivity near the one-sided
boundary do not assert our annular budget. Theorem1.3 has a finite-height
zero hypothesis. These are statement-level comparisons only: the
essential source proofs of the reciprocal-law and local-PF assertions
are NOT assessed here and none is imported as a new notebook theorem.

## Search record and decision

Queries: `Carleman formula upper half disk log modulus real zeros annulus
formula holomorphic`; `Riemann xi theta function Carleman formula
logarithm boundary positivity`; `Lectures on Entire Functions Carleman
188 pdf`; `Riemann Carleman log xi formula zeros`; `Carleman theta
boundary Riemann`; `Carleman xi boundary logarithm Riemann nonpositive`.
Retrieved passages above, rather than snippets, support this comparison.
Unrelated PDE Carleman estimates, analytic-continuation formulas named
Carleman, and unreviewed RH claims are not theorem inputs.

Outcome NEGATIVE: the exact classical identity and its unpaid signed
remainder defeat the nominated identity-plus-automatic-sign continuation.
This is new source-scope evidence for this nomination, not a mathematical
counterexample, global no-go theorem, discovery beyond the sources or
proof of RH. Park the route until an independent actual-theta signed
estimate is supplied; do not schedule a bare-identity lemma/audit chain.
PROOF and DAG are unchanged. Full matching Mathlib coverage is unchecked.

A different prospective source question concerns whether self-decomposability
and local PF positivity at every fixed order can force global PF positivity.
Sra's statements motivate it, but no such bridge is assumed. The earlier
finite-PF adjacency stops L837/L838/L840 and reciprocal-transform scope
stop651 have different hypotheses and must be compared, not declared
irrelevant. Nomination1684 records exactly this missing coverage; no
countermodel, propagation theorem or creative proof attempt is approved
or performed here.
