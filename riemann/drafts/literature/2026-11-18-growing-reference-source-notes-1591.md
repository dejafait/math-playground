# Growing-degree Laguerre source review1591

Literature-only review of assessment1590's exact TARGET. No coefficient
matching, residual estimate, new lemma or mathematical script is derived.
Main gap: L030-L032/C032a all-degree positivity; C028b's H_d=o(d)
payment remains missing. A positive reference must bound the unchanged
actual polynomial, without assuming its real roots.

## Working checkpoint

Read C028a/C028c hypotheses and imported interfaces, source-notes1503,
the relevant source-notes1587 comparison, assessment1496 and the precise
Hermite1497/penultimate1504 stop records. Supplied overview/DAG and
assessment1590 were used directly. Primary NIST DLMF Tables18.3.1,
18.9.1 and (18.5.12), including parameter notes, have been inspected.
A search found Holland2608.08682v1, a potentially relevant Laguerre
matching lead; its exact hypotheses and comparison are being inspected
before any ready continuation is nominated. Pan-Zeng2020 opening
formulas provide a primary-paper normalization cross-check.

No matching feasibility, cost floor, o(d^2) bound or RH advance was
claimed at this checkpoint. The completed source comparison follows.

## Inspected formula sources and applicability

NIST Digital Library of Mathematical Functions, version1.2.8, released
2026-09-15 (version verified at https://dlmf.nist.gov/), retrieved
2026-11-18. The Laguerre row of [Table18.3.1](https://dlmf.nist.gov/18.3#T1)
specifies interval (0,infinity), weight z^alpha exp(-z), alpha>-1,
standard squared norm Gamma(n+alpha+1)/n!, leading coefficient
(-1)^n/n!, and next-to-leading coefficient ratio -n(n+alpha).
These are standard-polynomial norms, not monic norms. Its orthogonality
definitions are read with the table, not inferred from a search snippet.
Use a probability normalization and an affine pushforward for the
prospective reference. Checking the resulting monic norms, including
every scale factor, is explicitly left to the separately approved test.
Each fixed d has finite real parameters; uniform bounds in d are not
hypotheses of this exact formula input. Reflection requires pushforward
of the positive measure, with the absolute Jacobian if a density is used.

[DLMF (18.5.12)](https://dlmf.nist.gov/18.5#E12) supplies the finite sum

    L_n^(alpha)(z)=sum_(ell=0)^n
      (alpha+ell+1)_(n-ell)*(-z)^ell/((n-ell)! ell!).

The parameter note in Section18.5(iii) retains alpha>-1 for Laguerre
orthogonality. Algebraic polynomial definitions outside this range do
not supply the stipulated positive reference. This exact finite formula
is sufficient for a five-coefficient calculation without asymptotics.

[DLMF (18.9.1)/Table18.9.1](https://dlmf.nist.gov/18.9#T1) gives
p_(n+1)=(A_n z+B_n)p_n-C_n p_(n-1), with Laguerre entries
A_n=-1/(n+1), B_n=(2n+alpha+1)/(n+1), C_n=(n+alpha)/(n+1),
and initial p_0=1, p_1=A_0 z+B_0. The table cites Szego1975 (5.1.10).
Szego's book proof was not newly read or needed for importing the
explicit DLMF identities. No fixed-alpha asymptotic is used; an
asymptotic with fixed alpha would not by itself cover alpha_d.

Qiongqiong Pan and Jiang Zeng, *Combinatorics of (q,y)-Laguerre
polynomials and their moments*, Seminaire Lotharingien de Combinatoire
81 (2020), B81e, [p1 (1.1)-(1.4)](https://www.mat.univie.ac.at/~slc/wpapers/s81panzeng.pdf).
Read the complete opening formulas. Their monic ell_n=(-1)^n n! L_n
satisfies

    ell_(n+1)=(z-(2n+alpha+1))*ell_n-n(n+alpha)*ell_(n-1).

Equation(1.2) supplies its finite coefficients; (1.4) gives the normalized
Gamma-weight functional. This is a normalization cross-check, not an
import of the paper's deformed-family combinatorics or its integer-alpha
claims. The full real range and norms are supplied by NIST above.

Reuse Schmeisser, Mathematica Balkanica16(2002),203-217,
[Theorem1/Corollary1 pp205-207](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
with definitions pp203-204 and complete relevant proof pp211-214 already
assessed in C028a/source-notes1493/1503. The weight here is positive,
has infinite support and all moments for each alpha>-1; its real affine
pushforward retains these hypotheses. Thus the known interface is
applicable once the proposed monic scaling is checked. No bounded
Jacobi/Favard theorem is needed for this unbounded-support explicit
measure. The source does not estimate its actual expansion cost.

## Relevant recent comparison: inspected, not an automatic import

Jonathan Holland, *A new hyperbolicity wedge and a joint semicircle
limit for Jensen polynomials of Riemann's xi-function*,
[arXiv:2608.08682v1](https://arxiv.org/html/2608.08682v1), inspected
Theorem1.1, Section2 (1)-(5), Section3 (10)-(13), Lemma4.3 with
its complete proof (30)-(33), and Lemma5.1's statement. Lemma4.3
matches normalized ascending coefficients gamma(n+j)/gamma(n)
with S^j/(B)_j and proves a positive third-coefficient defect for
sufficiently large derivative index n. Theorem1.1 requires
n^3 log^2(n+2)>=K d^5, K>0. These hypotheses leave n=0 uncovered.
The present target instead matches descending coefficients of the
unchanged reciprocal P_d using an affine Laguerre polynomial.
Neither the source's coefficient coordinates nor its large-n estimate
can be silently identified with this target. No Schmeisser norm bound
for this affine family is stated in the inspected material. This is a
scope comparison, not a proof audit or import of the global wedge
theorem. Its saddle dependencies and full global proof were not read.

The search result that led here was a third-party discussion at
https://zeta.teal-sea.com/read/hunts/jensen_wedge/RESULTS.html .
It was used only to identify the primary source, not as mathematical
evidence. No third-party claimed extensions or numerical fits are inputs.

## Duplicate and failure comparison

C028a and stop1497 exclude their matched Gaussian statistic. C028c
and stop1504 exclude a Hermite prefix with a specified terminal change;
their statements do not quantify over the present varying bulk.
C028h/i's audited diagonal and one-shear matrix floors remain intact.
Source-notes1503's terminal-diagonal redundancy and source-notes1587's
unpaid barycentric alternative remain relevant cautions. No existing
same-family residual test was found in the narrowly searched November18
actual-Jensen/reference assessments and these canonical statements.
This is a bounded duplicate check, not a notebook-wide novelty claim.
No zero-free region or reciprocal continuation is proposed; no October
analytic-envelope input or cross-notebook theorem is required.

## Search record and decision

Queries: `"Schmeisser" "Laguerre" imaginary parts zeros`;
`Laguerre orthogonal reference polynomial prescribed leading coefficients
imaginary parts zeros Schmeisser`; `"Jensen polynomials" "Laguerre"
"Schmeisser"`; `"Laguerre" "prescribed" "leading coefficients" polynomial`;
`"Laguerre" "imaginary parts" "orthogonal expansion"`;
`"Laguerre" "matching" "three" "coefficients" Jensen`;
`"Holland" "2608.08682" Laguerre`. Queries also returned complex-parameter
Laguerre root bounds, exceptional/deformed families, and Laguerre-type
inequalities; snippets and abstracts were not treated as matching
theorems. They are unread leads rather than essential assumed inputs.

DECISION: SPECIALIZE for the newly nominated finite test in assessment1591.
Import the source formulas and height theorem; justify affine conventions
and investigate only the actual matching/residual difference. No general
theorem reproof is justified. Adequate essential source coverage exists
for that finite calculation; no source access blocker remains. Exact
matching and costs are not settled by the inspected sources. Full matching
Mathlib coverage is unknown/not checked, and no absence is claimed.

Outcome EXPLORATION: new source coverage and a scoped near-overlap
comparison, without a mathematical result or novelty certification.
The nominated continuation needs separate approval next turn. It is
calculation/REPRODUCTION: a changed bulk reference is independently
testable, but no justified full-cost upper-payment mechanism is ready
to label proof_attempt/creative. An o(d^2) retained cost would pay only
a necessary diagnostic; the omitted sum remains unresolved. No lemma,
mathematical script, PROOF or DAG was edited in this review.
