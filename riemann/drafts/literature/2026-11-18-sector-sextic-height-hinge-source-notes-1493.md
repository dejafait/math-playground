# Hinge-sum source review1493

This is a literature-only step on the exact nomination1492 TARGET.
No hinge-sum inequality, root computation, new lemma or script is being
derived. The supplied nomination and checkpoint are the startup record.

Main gap: actual-Xi all-degree positivity and unpaid unbounded unshifted
Jensen exceptional-root loss. Proposed intermediate quantity is
H_a(p)=sum_r max(|Im r|-a,0), counting multiplicities, for the fixed
T=1+D+5D^2/18 on all real monic sextics and all a>=0. Its prospective
use is a continuous exceptional-root budget; realization, payment and
unbounded-degree transfer are independent unresolved requirements.

Continue only with an inspected matching theorem, an informative source
obstruction, or a separately gated bounded test after adequate comparison.
Do not infer weighted contraction from C020w's count result, C020x's
(4,6) witness or Walsh localization. C020o's inverse-positivity failure
and ATTEMPTS/2026-11-18-sector-sextic-discriminant-coefficient-stop-1473.md
remain in force and do not themselves decide this statistic.

Primary source versions and passages inspected:

- Julius Borcea, *Spectral order and isotonic differential operators of
  Laguerre–Pólya type*, Ark. Mat. 44 (2006), 211–240,
  DOI 10.1007/s11512-006-0017-6.
  https://archive.ymsc.tsinghua.edu.cn/pacm_download/116/7891-11512_2006_Article_17.pdf
  Published introduction/definitions; Theorem 2 and Corollary 1 in
  arXiv:math/0404336v2 (21 January 2006), §§1–1.2:
  https://arxiv.org/html/math/0404336v2
- Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
  a Polynomial*, Mathematica Balkanica 16 (2002), 203–217.
  https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf
  Definitions pp.203–204; Theorem 1, (2.1)–(2.2), pp.205–206;
  Lemmas 1–5 and the complete Theorem 1 proof, pp.211–214.
- Marcus–Spielman–Srivastava, *Finite free convolutions of polynomials*,
  arXiv:1504.00350v2 (3 July 2019).
  https://arxiv.org/html/1504.00350
  Definition 1.1, Theorems 1.2–1.3, and Theorem 2.10 with its complete
  coefficientwise proof in §2.2.1.
- Borcea–Brändén, *Hyperbolicity preservers and majorization*,
  C. R. Math. Acad. Sci. Paris 348 (2010), 843–846,
  DOI 10.1016/j.crma.2010.07.006:
  https://www.numdam.org/item/10.1016/j.crma.2010.07.006.pdf
  Definitions, Theorem 1, Lemma 6 and its two hyperbolicity cases,
  and the pinching completion pp.843–846 were read.
- Borcea, *Convexity properties of twisted root maps*,
  arXiv:math/0312321v4 (13 July 2005), introduction defining A'
  and §4.2 Conjecture 1 with the surrounding comparison:
  https://arxiv.org/html/math/0312321v4
  Published as Rocky Mountain J. Math. 38 (2008), 809–834;
  theorem numbering here refers to the inspected arXiv version.
- Rajesh Pereira, *Matrix-theoretical derivations of some results of
  Borcea–Shapiro on hyperbolic polynomials*, C. R. Math. Acad. Sci.
  Paris 341 (2005), 651–653, DOI 10.1016/j.crma.2005.10.002:
  https://www.numdam.org/item/10.1016/j.crma.2005.10.002.pdf
  D_alpha definition p.651; Proposition 2, Theorem 6 and matrix
  realization p.652; Theorem 10, proof and Lemma 11 p.653.
- Adam W. Marcus, *Polynomial convolutions and (finite) free probability*,
  arXiv:2108.07054v1 (16 August 2021), Lemma 5.7,
  §5.2 Corollary 5.12 and Theorem 5.15 with its proof:
  https://arxiv.org/html/2108.07054v1

Initial searches: `polynomial differential operator imaginary parts zeros
majorization convolution real rooted`; `Walsh convolution imaginary parts
zeros weak majorization`; `polynomial zeros "imaginary parts"
"majorization" convolution`; `"Walsh" "majorization" zeros complex`;
`"convolution" "complex" "majorization" Borcea Shapiro zeros`.

Follow-up queries used the exact titles, `"Hyperbolicity preservers and
majorization" pdf`, `"imaginary parts" "zeros" "contraction" polynomial
differential`, `"polynomial" "imaginary parts" "Obrechkoff"`,
`"finite" "convolution" "majorization" "complex roots"`,
`"Borcea" "Conjecture 1" "imaginary" majorization`,
`"Pereira" "convolution" "majorization" imaginary`, and
`"complex" "finite free" "majorization" polynomial`,
`polynomial "5/18" "zeros" "differential"`,
`polynomial "hinge" "imaginary parts" contraction`, and
`"1+D+5" "18" polynomial roots`. The latter exact-coefficient/hinge
queries returned no verified matching result.
Only the primary passages above support the comparison. Search snippets,
aggregators and bibliographic leads are not theorem evidence. A mistaken
open of arXiv:1001.0382 was unrelated and is not used.

## Theorem-level comparison

**Pereira.** For every nonconstant complex polynomial p and real alpha,
Theorem 10 states Im Z(D_alpha p) majorized by Im Z(p), where
D_alpha=(1-alpha D)exp(alpha D). The source explicitly permits replacing
D_alpha p by p-alpha p'. Roots include multiplicities. Proposition 2
characterizes majorization by sums of every convex function on an interval.
Theorem 6 uses a rank-one perturbation; Theorem 10 uses its Hermitian
imaginary part and Lemma 11. The proof displays the opposite alpha
sign to the preceding realization; both signs are covered by its
all-real-alpha statement. No proof is reconstructed. C020x records
nonreal symbol roots for q; no representation by covered real
first-order operations has been verified. This is a comparison input,
not approval of the quadratic inequality.

**Schmeisser.** Theorem 1 assumes a monic orthogonal basis for a positive
real measure with all moments and an expansion p=sum a_nu P_nu of degree n.
Put kappa=Im(a_(n-1)/a_n),
I(p)^2=kappa^2+sum_(nu=0)^(n-2)(gamma_nu/gamma_(n-1))|a_nu/a_n|^2,
gamma_nu=||P_nu||^2, and c=-t*kappa, 0<=t<=1/2. For nondecreasing
convex phi on [0,infinity) with phi(0)=0, its (2.2) bounds the sum of
phi(|Im z_j-c|), k>=2, by
phi((I+|kappa+2c|)/2)+phi((I-|kappa+2c|)/2)+(k-2)phi(|c|).
The proof uses a companion matrix's imaginary-part singular values.
The comparison vector depends on coefficients, not the original roots
of another polynomial; it gives no stated H_a(Tf)<=H_a(f).

**Borcea2006.** Theorem 2 says that for P,Q in the monic real-rooted
degree-n space, Q majorized by P implies Q-lambda Q' majorized by
P-lambda P' for real lambda. Corollary 1 extends to normalized
Laguerre–Pólya differential operators, still with real-rooted inputs.
This is isotonicity between two real root vectors; it does not cover
the proposed comparison for arbitrary real sextics with complex roots.

**Borcea–Brändén2010.** Theorem 1 characterizes linear maps on real
degree-at-most-n polynomials preserving majorization *of hyperbolic
inputs*. Its nondegenerate case requires T(H_n) contained in some H_m.
Lemma 6 starts with real-rooted r of degree n-2 and real s,t, and studies
T(r(z)((z+s)^2-t^2)). Its proof uses hyperbolicity in both cases of its
third coordinate, a real symmetric matrix pencil and real pinches.
These are not a theorem about imaginary root vectors of nonreal inputs.
Finite-degree real-rooted preservation alone therefore is not a stated
substitute for the requested hinge conclusion.

**Borcea2005.** Conjecture 1 in §4.2 asserts an alternative: for T in
the all-degree, root-average-preserving monoid A', either real parts
expand in majorization or imaginary parts contract. A disjunction
does not assert its second branch, and membership of the present
finite-degree operator in A' is not supplied. Pereira resolves the
relevant real first-order case. No current open/closed status for the
entire general conjecture is asserted from this historical manuscript.

**Marcus–Spielman–Srivastava.** Theorem 1.2 represents the finite additive
convolution as E_Q chi_(A+QBQ*) for complex normal A,B and Haar-unitary Q.
Theorem 2.10 proves the coefficient identity; it does not identify roots
of this expectation with averaged eigenvalues. Theorem 1.3 requires
both polynomial inputs real rooted. No passage inspected supplies the
needed comparison of imaginary heights after polynomial averaging.
The saved Walsh normalization in C020x is reused, not reproved.

**Marcus2021.** Lemma 5.7 assumes real symmetric A,B with A diagonal
and supplies a real rotation placing the pair in finite free position
with constant diagonal for the rotated B. Corollary 5.12 assumes
real-rooted polynomial inputs and zero root sum for the second one.
Theorem 5.15 studies dilation of the second input; its proof again
invokes this real symmetric realization and additive compounds.
The printed theorem line does not repeat real-rootedness, but that
proof and Lemma 5.7 require it. Its wording cannot license complex-input
imaginary-part majorization. No correction or independent reproof is
attempted here.

## Local overlap and decision

Read C020x's hypotheses, conclusion and Walsh applicability passage
(lines1–66), C020o's hypotheses/conclusion, and the complete recorded
coefficient-test failure1473. The sector-scoped keyword search also
looked for imaginary-height majorization and twisted-root terminology in
sector assessments, histories and attempts. It found no earlier exact
hinge-sum assessment beyond nomination1492; this is not a global novelty
audit. C020w/audit1488's accepted scope is reused from the supplied
checkpoint and assessment1486, not re-audited. No sibling notebook read.

The exact universal inequality is neither established nor refuted by
these inspected statements. Outcome: EXPLORATION, not a mathematical
advance or a counterexample. Decision: EXPLORE for one bounded test;
no essential source is blocked for that test. No new result, root
calculation, lemma or mathematical script was produced.

The separate continuation tests the fixed C020x sextic at only
s in {1/4,1/2,1,2,4}, defining f_s(x)=s^6 f(x/s), keeping q fixed.
Use only a in {0,1/8,1/4,1/2,1,2,4,8}, at most forty pairs in total,
seeking a rigorous strictly positive lower bound
for H_a(Tf_s)-H_a(f_s). Approximate roots may nominate a candidate but
only complete root enclosures/counts and certified sum bounds accept it.
An uncertified candidate, no violation, or inconclusive enclosures remain
bounded evidence only; they do not establish the universal inequality.
Stop after these five inputs and eight thresholds, preserve failures, and require a new
discriminating idea before extending the search. This nomination is not
executed here and needs separate next-turn approval.

The target is an intermediate generic budget, not a central creative
actual-Xi mechanism. Payment, actual-factor realization and all-degree
control are missing; no creative routing is justified solely by the
discovery cadence. Full matching Mathlib coverage was not checked;
absence is not claimed. No reproof is needed or authorized this turn.
