# Direct actual Jensen height source review1500

Literature-only work on the exact discovery TARGET in assessment1499.
Main gap: L030--L032/C032a actual-Xi all-degree positivity. The proposed
intermediate threshold is sum_j |Im z_j(R_d)|=o(d), with exactly C028a's
unshifted reciprocal polynomial and multiplicities. Its proposed use is
an exceptional-root budget; no upper payment or RH conclusion is assumed.

## Saved working checkpoint (completed below)

Three mechanisms only: direct strip/sector localization; large-shift
Hermite asymptotics; compact Jensen convergence and persistence of a
fixed nonreal zero. Reuse reviews1460/1461 for the first, and
source-notes1493/1496 plus C028a/audit1499 for the prior stops.
Read the relevant definitions in L018/L021/L028, C019j and C032a.
L028 proves degree two only; it is not an all-degree criterion.
Read L763/L764's hypotheses and conclusions as contrasts, without
reopening their different Gaussian-product families.

New primary reading: Craven--Csordas1989 Lemma2.2, pp244--245;
O'Sullivan2007.13582v2 Section3.1, Theorem3.1 and proof sketch,
Corollaries3.2--3.3; Farmer2008.07206v2 Section2 items(1)--(2)
and Section3/(3.1)--(3.2); Griffin et al1910.01227v2 Theorem1.1.
The first two explicitly state J_d(z/d)->F(z) on compact sets.
The reciprocal-coordinate consequences are an unproved continuation
target, not a result established during this source review.

Pending: finish the source/hypothesis comparison, record exact versions
and retrieval qualifications, and nominate one bounded zero-persistence
specialization with separate next-turn approval. No lemma, mathematical
script, DAG or PROOF change is authorized or made.

## Completed comparison: three mechanisms

1. **Direct strip/sector localization.** Reuse source-notes1460/1461's
   inspected primary hypotheses: Kim--Lee arXiv:2105.05386v1,
   12 May2021, Theorems1/3/4 and the final even-function remark;
   Craven--Csordas1983 Theorems3.3--3.4/Corollary3.8; Cardon et al
   arXiv:1802.02641v1 Theorems2.2/2.5. Their derivative thresholds,
   all-zero-sector premises or finite degree ceilings under height
   exclusions do not state the desired unconditional height sum.
   Published Kim--Lee2022 remains parked and unread; no retrieval retry
   was made. Finite verified height is not enlarged to infinity. No
   new zero-free region or strip estimate is proposed, so the October
   zero-free-region baseline is not reopened.

2. **Large-shift Hermite asymptotics.** M.J. Griffin, K. Ono, L. Rolen,
   J. Thorner, Z. Tripp and I. Wagner, *Jensen polynomials for the Riemann
   xi-function*, accepted manuscript for Advances in Mathematics397
   (2022),108186:
   https://uva.theopenscholar.com/files/ken-ono/files/jensenadvmathaccepted.pdf .
   Inspected p1/(1.1)--(1.3)/Theorem1.1 and p2 remarks. Its conclusion
   requires n>=c exp(d), c>0 absolute. The earlier arXiv:1910.01227v2
   Theorem1.1, also inspected, prints n>>exp(8d/9); versions are not
   merged. Either excludes n=0. This is a statement-level applicability
   comparison, not an audit of Sections3--4's coefficient estimates.
   Factorial-normalized gamma matches; a common factor8 in the older
   submitted PDF changes no roots. No inverse differentiation, actual
   primitive constant or unshifted upper bound follows from these
   stated ranges. Reuse the November5 bulk-saddle assessment's Farmer
   comparison without reopening its stopped moving-window estimate.

3. **Compact Jensen convergence and zero persistence.** Selected as a
   diagnostic, not an upper estimate. Thomas Craven and George Csordas,
   *Jensen polynomials and the Turan and Laguerre inequalities*, Pacific
   J.Math.136(2) (1989),241--260,
   https://msp.org/pjm/1989/136-2/pjm-v136-n2-p03-s.pdf , Lemma2.2,
   pp244--245/(2.13)--(2.21), states: for arbitrary entire
   h(z)=sum a_k z^k/k! and fixed p>=0, g_(n,p)(z/n)->h^(p)(z)
   uniformly on compact subsets of C. No LP or real-zero premise.
   Read the statement and the entire proof's text: a finite coefficient
   block and two Cauchy-bounded tails. Some displayed formulas are
   OCR-obscured; screenshot calls yielded no inspectable image and a
   shell download failed DNS. No exact rate or independent audit of
   those formulas is claimed.

   The exact compact-limit formula is independently legible in Cormac
   O'Sullivan, *Zeros of Jensen polynomials and asymptotics for the
   Riemann xi function*, arXiv:2007.13582v2,9 December2020,
   https://arxiv.org/html/2007.13582v2 , Section3.1 Theorem3.1 and its
   complete proof sketch, Corollary3.2 and proof. For real entire
   genus1* functions the criterion equates LP membership with
   hyperbolicity of all Jensen polynomials. The proof sketch explicitly
   states compact convergence; its two directions use Hurwitz and
   real-root-preserving differential operators. Corollary3.2 records
   actual Theta's order1/2. No actual LP membership is assumed.

   David W. Farmer, arXiv:2008.07206v2,9 November2022,
   https://arxiv.org/html/2008.07206v2 , Section2 items(1)--(2) and
   Section3/(3.1)--(3.2), confirms the convention and distinguishes
   even Xi polynomials from ordinary Jensen polynomials of
   xi(1/2+sqrt(z)). The November5 assessment already covered those
   statements for a different moving-window target; that failed scope
   does not supply a height bound. Farmer's title is not an impossibility
   theorem. No numerical examples or general order<2 assertion is used.

   Terence Tao, *Math246A, Notes4: singularities of holomorphic functions*,
   11 October2016,
   https://terrytao.wordpress.com/2016/10/11/math-246a-notes-4-singularities-of-holomorphic-functions/ ,
   Corollary34 and Theorem37 with complete proofs were read. Theorem37
   is Rouche's theorem: holomorphic f,g near a simple closed contour
   and its interior, |g|<|f| on the contour, imply equal zero counts
   for f and f+g inside, including multiplicity. The proof uses the
   zero-free boundary homotopy in Corollary34 and the argument principle.
   No simple-root assumption. Import this theorem without a reproof.

## Applicability and remaining difference

L018/L021 and C028a specify the same actual coefficients as O'Sullivan:
F=Theta/gamma_0, F(0)=1, gamma_j=j!M_(2j)/(2j)!>0.
The polynomials J_d/gamma_0 and R_d/gamma_0 have the same roots as J_d
and R_d respectively. The relevant primary limit fixes p=0 and sends
d to infinity; fixed-degree, increasing-shift limits are different.
No global square-root branch, LP premise or actual nonreal zero is used.

The inspected statements do not display the proposed reciprocal-height
inequality. The remaining specialization must track a fixed zero
neighborhood under inversion, retain multiplicity, and check the factor
d and liminf. A qualitative RH inference needs both directions and the
actual zero correspondence. These checks are reserved for research;
this review does not prove the inequality or RH equivalence. Reproofs
of Jensen convergence, Rouche or the Jensen criterion are unnecessary.
Full matching Mathlib coverage is unchecked; absence is not claimed.

## Searches, duplicates and decision

Queries: `Jensen polynomials reciprocal zeros horizontal strip imaginary
parts unshifted xi large degree`; `Jensen polynomials zeros sector
Obreschkoff Hurwitz convergence entire functions`; `"Jensen polynomials"
"sum" "imaginary" zeros`; `"Jensen polynomial" "imaginary" "height"
reciprocal`; `"Jensen polynomials" "nonreal zero" "convergence"`;
exact Craven--Csordas/Lemma2.2 and Farmer titles; primary-author
Rouche/Hurwitz terms. Search snippets and secondary pages are leads
only. Chasse's thesis, the 2019 restricted-zero convergence paper and
unrelated new preprints were not inspected as additional mechanisms.
Farmer v3 returned404; v2 was actually read. O'Sullivan's legible formula
and the primary theorem statements avoid an essential source blocker.

Scoped duplicate searches: named November18 Jensen/deficit/height
assessments and attempts, C019g/i/j, C028a, L028, November4 primitive
and November5 bulk-saddle assessments. General compact convergence
was already known, but no canonical exact reciprocal-height lower-bound
proof was located. A guessed November4 discovery filename did not exist
and supplied no evidence. This is not an exhaustive novelty claim.
C019i states a real-root count, not a height bound. C028a, L763/L764,
inverse-direction1496 and stop379 retain their limited conclusions.

Outcome EXPLORATION: no direct upper theorem or creative payment
mechanism was identified. The separate nomination is an independently
testable known-method specialization. Continue only after checking the
one-fixed-nonreal-zero linear obstruction, multiplicity and scale;
otherwise isolate the exact failed implication. No global norm or
root-distribution sweep is justified. A proved equivalence would guide
target selection, not prove RH. This source turn spends no mathematical
exploration attempt, resets no counters, and changes no lemma,
mathematical script, PROOF or DAG.
