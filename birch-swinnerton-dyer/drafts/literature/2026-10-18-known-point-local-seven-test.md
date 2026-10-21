# Known rational point — fixed local-seven source assessment

TARGET: Test whether P=(0,0) is nonzero in E(Q_7)/7E(Q_7) for y^2+y=x^3+x^2-2x by a certified formal-group computation of [13]P.
CHECKED: 2026-10-18
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Local L034/L062/L065, localization/descent assessments, histories 219/237 and ATTEMPTS/033/034/042 contain no matching finite value; external exact-curve/point/logarithm and seven-divisibility searches found Silverman's general theory, Sage's exact-model logarithm examples and Wuthrich's exact-curve approximation-lattice study, but no inspected certificate of this fixed seven-adic quotient value; queries and read scope below.
SOURCE_EVIDENCE: Silverman, The Arithmetic of Elliptic Curves, second edition (2009), III Group Law Algorithm 2.3 pp.53–54, VII Proposition 2.1 pp.188–190, VII Proposition 2.2 p.191, IV Theorem 6.4 p.132 with Lemma 6.3(b) p.131; relevant statements/proof cases and author errata dated 2022-10-13 inspected. Sage ell_point.padic_elliptic_logarithm method/precision note/exact-model examples and Wuthrich (2006), Section 3 pp.3–5, inspected for overlap.
COMPARISON: These known results cover the reduction kernel, formal parameter, logarithm radius and exact group law; the remaining work is the fixed exact arithmetic certificate and explicit full-group applicability argument. Sage's displayed P=(0,0) value is at three, its seven examples are logarithm ratios for another point, and Wuthrich's plots do not supply the requested value. No mathematical novelty is claimed.
GAP: No [13]P coordinates, parameter valuation or nonzero quotient class have been produced here. The next research step must certify the full scalar chain and specialize the imported reduction/formal-group results, including possible division points in the entire local group; every L026 premise and D=D_div remain independent downstream obligations.
REASON: Previously missing essential coverage is now inspected, including the convergence erratum and full reduction-group issue; one exact known-method specialization is justified without repeating descent-interface audits or continuing the order-correction chain.
SCOPE: Only the displayed minimal curve, prime seven, supplied point P, W=[13]P and the depth-one quotient; exact group-law replay, projective/reduction checks and numerator/denominator valuations. No second point, changed prime/depth, larger search, quotient-exponent production, full descent certificate or BSD conclusion.
LITERATURE_REASON: The prior REVIEW_REQUIRED proposal lacked primary formal-group/reduction coverage and exact-target comparison; the ready finite Kummer interface alone did not cover these hypotheses.

## Relevance, historical proposal and bounded decision

The main gap remains rank E(Q)=m(E) for arbitrary analytic order at least
two. This target could produce an actual nonzero local Kummer value from
an already supplied rational point, independently of global order,
unit/class and descent computations. It cannot increase the already
known rational rank of this curve or produce rational directions for
arbitrary curves. Successful local data would be one input for a later
conditional application of L062, not that application itself.

Step 305 proposed exactly this target with REVIEW_REQUIRED. Its scope,
threshold and stop rule are preserved; step 306 supplies source comparison
only. No scalar multiplication, valuation test or new mathematical result
has been derived in this literature turn. The former pending-source
language is superseded by this assessment, not by a claimed computation.

Continue with one exact computation of W=[13]P, seeking W distinct from O,
reduction O and v_7(-x(W)/y(W))=1, after the explicit full-group
specialization. Stop this fixed test if a needed hypothesis fails, the
threshold is not met, or the exact chain cannot be certified. Preserve
the actual result; do not switch points or increase depth in that step.
A failed witness does not select L061's k=2 branch or imply rank zero.

## Discovery and duplicate comparison

Queries issued on 2026-10-18 included:

- `Silverman Arithmetic Elliptic Curves VII Proposition 2.1 formal group IV Theorem 6.4 logarithm pdf`;
- `"389a1" "7" "saturation"`, `"389" "formal" "13" elliptic point logarithm`;
- `"389a1" "padic_logarithm" "7"`, `"389a1" "13*P"`, `"389a1" "non-divisible" "7"`;
- `"389a1" "formal" "logarithm"`, `"389a1" "local" "7" "divisible"`, and `"x^3+x^2-2*x" "13" "7" elliptic`.

Read primary results below rather than adopting search snippets. The
search returned unrelated purported BSD resolutions and informal software
experiments; none was inspected as a theorem input. Failure to find a
matching certificate does not establish novelty or absence elsewhere.

The [Sage reference method](https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/ell_point.html#sage.schemes.elliptic_curves.ell_point.EllipticCurvePoint_number_field.padic_elliptic_logarithm)
was read through its algorithm, precision qualification and displayed
examples (HTML lines 3565–3629 at inspection). It uses the formal logarithm
at -x/y after multiplying into the formal group. On the exact coefficient
vector [0,1,1,-2,0], it displays P=(0,0)'s logarithm at three, not seven.
The subsequent multi-prime examples give ratios on (-11/9,28/27), not an
absolute logarithm for the present P. Its stated absolute-precision
qualification reinforces using an exact rational coordinate/valuation
certificate here. No Sage command was run or value extrapolated.

Christian Wuthrich, [*On p-adic elliptic logarithms and p-adic approximation
lattices*, author text dated 26 April 2006](https://www.maths.nottingham.ac.uk/plp/pmzcw/download/logs.pdf),
Section 3, printed pp.3–5, treats the exact model and point pair, explicitly
gives a formal-subgroup basis at three, and plots approximation-lattice
minima for several primes including seven. Those quantities and plots
are not this fixed point's depth-one value. Only that comparison scope,
the introduction's conjectural status, and the beginning of Section 4's
formal-logarithm setup were read; the paper's later lattice theorems are
not inputs and no stronger uninspected conclusion is assumed.

Locally, L034 already imports the published rational basis from Cremona,
*Algorithms for Modular Elliptic Curves*, corrected second edition,
Table 2 p.257, row 389A1, with its computational qualifications. L030 and
L033 supply the exact minimal model, good ordinary seven and complete
reduction count 13. Reuse those established inputs rather than rerun
source discovery for them. The relevant full L062 argument and its
separate audit retain the same-depth Kummer conventions. Histories 219
and 237 confirm the interface/upper-enclosure audits are complete.
ATTEMPTS/033, /034 and /042 record respectively the absent ordinary value
from scalar transfer, repeated interfaces without arithmetic data, and
repeated changed-order approval. An actual value on a supplied rational
point is independently testable and does not reopen those stopped tests.

## Primary coverage, hypotheses and relevant proof cases

Use Joseph H. Silverman, *The Arithmetic of Elliptic Curves*, second
edition, GTM 106, Springer (2009), DOI 10.1007/978-0-387-09494-6.
The [author's edition page](https://www.math.brown.edu/johsilve/AECHome.html)
identifies the edition. The actual primary text was read in the
[ENS-hosted book PDF](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf),
with the following printed-page and PDF-page locators. A direct shell
download failed DNS resolution; the web reader supplied the needed
complete statements and relevant proof text, so this is not a source
blocker. Screenshot calls did not expose usable page images; rely on
the inspected text, not an assertion of image inspection.

1. **Reduction.** [VII Proposition 2.1, pp.188–190](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=204)
   (PDF pages 204–206) gives the exact reduction sequence from E_1(K)
   through E_0(K) onto the nonsingular special-fiber points. The chapter
   assumes a complete discretely valued field, normalized valuation,
   valuation ring R and perfect field/residue field; the equation is
   minimal integral. Read the definitions, Hensel-surjectivity argument,
   the distinct-reduction case, tangent lemma and coincident-reduction
   case. The source leaves other group-law cases as exercises; import
   the named proposition rather than claim a new complete reproof. Its
   good-reduction paragraph identifies E_0(K) with all of E(K).

2. **Parameter.** [VII Proposition 2.2, p.191](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=207)
   (PDF page 207), including its complete proof, identifies the formal
   group on the maximal ideal with E_1(K) for a minimal equation. Its
   inverse parameter is t=-x/y; zero corresponds to O. The proof uses
   w(t)=t^3 times a unit, and for a nonidentity point in the kernel gives
   3v(x)=2v(y)=-6r with integer r>=1. Thus projective reduction and the
   stated coordinate chart must be checked; -x/y is undefined at the
   original affine P=(0,0), which is outside this formal parameter chart.

3. **Logarithm.** [IV Theorem 6.4, p.132](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=150)
   (PDF page 150), both parts and proof, applies to a formal group over
   the valuation ring of a characteristic-zero complete discretely
   valued field. For integer r>v(p)/(p-1), it supplies an additive
   logarithm isomorphism on the r-th maximal-ideal power. Read also
   Lemma 6.3(b), p.131, and its strict leading-term estimate, which
   provides valuation preservation in this radius. At K=Q_7 the
   normalization is v_7(7)=1, so r=1 and r=2 are both in that radius.
   These are the precise source hypotheses needed for the proposed
   first/second-filtration test. No truncated logarithm evaluation or
   unproved claim of convergence on an arbitrary ramified field is needed.

4. **Exact group law.** [III Group Law Algorithm 2.3, pp.53–54](https://www.math.ens.psl.eu/~benoist/refs/Silverman.pdf#page=71)
   (PDF pages 71–72), all branches, supplies the general Weierstrass
   negation, inverse-pair, chord and tangent formulas and the resulting
   coordinates. Read also their preceding line-intersection derivation.
   The later certificate must retain a_2=1 and a_3=1, record whether an
   input is O, handle inverse pairs and doubling separately, and justify
   every rational denominator used. A nonsingular on-curve output alone
   does not certify the claimed scalar multiple.

The author's [errata dated 13 October 2022](https://www.math.brown.edu/johsilve/AEC/AECErrata.pdf)
were checked at entries for pp.130–133 and pp.185–191 (errata PDF pages
15 and 21), with searches for pp.54 and 132. The errata correct Example
IV.6.1.1's p>=2 to p>=3 and Lemma IV.6.3(a)'s unrestricted assertion of
convergence in R: in general convergence is in its fraction field, with
an additional integrality threshold. Do not import the erroneous wording.
The inspected part (b) and Theorem 6.4 use their strict radius, satisfied
here. The reduction-section corrections restore missing special-fiber
notation and point to an alternative proof; they do not change the
sequence used. The errata explicitly omit errors fixed in the 2015
second printing; no blanket claim of an exhaustive errata audit is made.

## Approved specialization and certificate boundary

The next research step may import the named results without reproving
the general formal-group or reduction theorems. Its remaining elementary
specialization must explicitly explain all three passages:

- why multiplication by 13 puts the supplied point in E_1(Q_7), using
  L033's complete reduction order, and why multiplying by 13 preserves
  zero/nonzero in the quotient killed by seven;
- why a seven-division point in E(Q_7) of a point in E_1(Q_7) must itself
  reduce to O, using that multiplication by seven is invertible on the
  complete reduction group of order 13;
- how the imported logarithm isomorphisms at the first and second
  filtrations identify the seven-multiple subgroup of E_1(Q_7), and
  hence justify the proposed valuation-one success threshold.

These are approved applicability obligations for the separate mathematical
attempt, not a new proved lemma in this source review. The known inputs
cover them without any unassessed arithmetic mechanism. The exact rational
scalar chain and full independent group-law replay remain necessary:
no inspected theorem supplies W's coordinates or its valuation. A short
binary scalar chain and a distinct sequential-addition replay are suitable
finite certificates, with every intermediate curve identity and exceptional
branch retained; the proof may use another completely specified fixed chain.
Reduced numerator/denominator seven-valuations and projective reduction
must be saved in full and summarized against the required value one.

Only after a successful test may a canonical lemma state the local point
conclusion with its full applicability proof. A later use of e=0,n=1 in
L062 still requires every L026 premise and independently established
D=D_div. The known rational point would supply a global Kummer class
with classical local conditions, but neither the L026 package, removal
of the finite quotient, nor a second strict rational direction is assumed
or produced by this assessment. No global descent representative or
faithful degree-48 power-class evaluation is needed for this point test.

## Mathlib

Full matching local test, formal-group logarithm/radius and supporting
Weierstrass/reduction coverage: not checked. No absence is inferred.
The analytic theorem and group-law algorithm will remain precise imports;
only the finite instance and the specified applicability argument need
reproduction. A successful result would be known-method specialization,
not a discovery beyond the inspected sources.
