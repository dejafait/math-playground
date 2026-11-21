# Count-only coarse-overlap obstruction — completed source assessment

TARGET: Test whether the product, simple-ordering and upper-count premises used in L836 force its exact coarse overlap expression to be negative at k=6002 and m=9000000000000, or admit an all-real genus-zero countermodel with a nearly colliding selected pair.
CHECKED: 2026-11-07
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Compared L836/L835, L834's verified-count passage, L467's count hypotheses, the ready product/envelope/indexed-test assessments and step659/667/runtime stops; searched prescribed canonical zeros, count versus spacing and the exact 6002 overlap terminology. Read Heittokangas–Laine Section2 and Example2.4, DLMF's product M-test and Bellotti–Wong Theorem1.1. No matching exact coarse-expression countermodel was located; no novelty inference.
SOURCE_EVIDENCE: Heittokangas–Laine, Acta Math. Univ. Comenianae LXXIV(2) (2005), 287–307, Section2/(2.1), Definition2.1/Lemma2.2 p.289 and Example2.4 pp.291–292, https://emis.de/ft/28373 ; NIST DLMF Section1.10(ix), M-test (1.10.20)–(1.10.21) and following alternative hypothesis, https://dlmf.nist.gov/1.10.ix ; Bellotti–Wong arXiv:2412.15470v2 (7 July2025), Theorem1.1 p.1, https://arxiv.org/pdf/2412.15470v2 ; reuse Katkova and Platt–Trudgian passages assessed in L836/L834.
COMPARISON: Known canonical-product theory supplies prescribed-zero existence subject to summability, and the inspected positive-real genus-zero example has no q-separation for any q>=0. Neither that example nor the actual-zeta count theorem verifies the proposed model's exact inclusive count, prescribed H total or H_m sign. The target is a standard-method specialization with these additional obligations, not new product or spacing theory.
GAP: Construct a complete strictly ordered positive sequence meeting N(t)<=U(t) for every t>=e and N(H)=12363153437138, prove reciprocal-square summability and the required product properties, and certify the sign of the exact unrounded H_m. No such model or sign is established by this source review.
REASON: Essential coverage is sufficient for one bounded abstract close-pair test without indexed zeta data; only the specified count-admissibility and scalar-margin specialization remains. This approves the unchanged target for a later mathematical turn, without deriving or validating it here.
LITERATURE_REASON: Invocation-start REVIEW_REQUIRED changes actual-Xi hypotheses to an abstract count/product class; prescribed-zero and spacing coverage was essential and missing from the earlier actual-function audits.
SCOPE: One bounded test of the class and exact expression below, with k=6002, J=6003, m=9000000000000 and the stated H and count; no actual-Xi counterexample, additional count constraints, parameter sweep, sign theorem or numerical-zero setup.

## Completed comparison — 7 November 2026, step103

This is a literature-only step. The main gap, downstream purpose and
exact proposed mathematical test below are unchanged. The earlier
nomination's statements about missing review describe its startup state;
the completed fields above supersede them. No construction is proved.

### Inspected source hypotheses and comparison

Heittokangas and Laine, *Solutions of f''+A(z)f=0 with prescribed
sequences of zeros*, [primary journal PDF](https://emis.de/ft/28373),
Section2 p.289, give the finite-genus canonical product (2.1) with
exactly its prescribed zeros. Distinctness and quantitative separation
are different hypotheses: Definition2.1 requires a positive infimum of
the weighted derivative magnitudes; Lemma2.2 expresses that requirement
through the product excluding a selected zero. Example2.4, pp.291–292,
gives an increasing positive-real sequence of genus zero whose canonical
product is not q-separated for any q>=0. Read the complete example,
including its derivative-ratio estimate and order-zero conclusion.
This is an inspected known obstruction to importing separation from
genus alone. Its count is not the prescribed notebook count, and its
derivative conclusion is not a sign calculation for H_m. The example's
referenced Bank Corollary1 was not independently read; no extra Bank
theorem or ODE realization is needed or imported here.

The [NIST DLMF Section1.10(ix) M-test](https://dlmf.nist.gov/1.10.ix)
states uniform analytic product convergence under a summable uniform
bound on logarithms, and explicitly also permits a summable bound on
the factors' increments. Zeros can occur only at factor zeros. This
is the relevant genus-zero convergence input, subject to the later
sequence's summability verification on each disk and its local
multiplicity check. The separately displayed exponential-factor
Weierstrass product (1.10.22) is not the requested genus-zero product.
No general convergence theorem needs reproof. DLMF was inspected as an
official authored reference, not as a novelty search or Mathlib claim.

Fresh inspection of [Bellotti–Wong v2](https://arxiv.org/pdf/2412.15470v2),
Theorem1.1, printed p.1, confirms the two-sided error bound, its first
triple of constants 0.10076, 0.24460, 8.08344, the domain T>=e and
upper-inclusive positive-height count. Reuse L467's previously reviewed
multiplicity/endpoints and Section5 cases; this is not a full-manuscript
audit. L836(9) already records its weaker upper envelope U with
b=0.34536, d=8.08344. The nominated abstract class requires only that
U bound, not the sharper first expression or the lower bound. The
source's zeta theorem does not assert a theorem for arbitrary products;
the inequality is a separately imposed model hypothesis.

Reuse the ready Katkova product assessment without repeating its proof.
L834's inspected Platt–Trudgian passage fixes the origin of H and
N(H)=12363153437138. For an abstract model the same integer is an
imposed total, not evidence that its ordinates are zeta ordinates.
No individual verified zeta locations are inputs. L018/L021/L776 remain
actual-function context, not automatic theorems about a replacement
function. The test concerns the scalar expression defined from L836;
it must not silently claim that every actual-Xi hypothesis of L835/L836
has transferred to the model.

### Discovery, duplicates and bounded decision

Queries included `canonical product prescribed zeros arbitrarily close
zeros counting function genus zero`; `"canonical product" "counting
function" "separation" zeros`; `"zero spacing" "counting function"
entire functions`; `"6002" "canonical product" "overlap"`; and
`"genus zero" "upper" "counting function" "close"`. These led to the
inspected primary example and official convergence statement. Other
general growth/spacing search hits were leads only; no stronger theorem
is imported from a snippet. No exact local-expression result was found
in this bounded search, which cannot establish originality.

The clustered-pole assessment already handles interpolation with
coalescing nodes; it does not prove a lower gap or this count-constrained
countermodel. The residual-envelope and indexed-test assessments cover
actual-function formulas and algorithmic indexed inputs. Step659's
unpaid hybrid determinant ratio and step667's unpaid signed residual
comparison are distinct stops. The FLINT setup and LMFDB access blockers
remain parked; this abstract test uses neither service. No repeat
symbolic audit or duplicate indexed-data attempt is approved.

The bounded plan is one selected close pair together with a fully
specified finite ordered packet and infinite positive tail. No choice
of these objects is established in this review. Every height regime,
including e, each jump, H and the unbounded tail, must meet U; an
asymptotic count or an endpoint-only check is insufficient. The later
proof must retain exact R,q,a,s,V,B and every term of H_m. It must also
justify all logarithm domains and any positivity used to bound B.
Summability alone does not verify the count or the scalar threshold.

Continue only on a fully admissible model with H_m>=0, preferably a
strict certified margin, or a proved uniform H_m<0 under every stated
premise. A close-pair limit without an admissible complete sequence,
or a failed candidate, is inconclusive. A countermodel stops only this
count-only sufficiency claim; actual overlap, sharper finite-product
bounds, arithmetic correlation and all-degree signs remain independent.
This routine specialization is not a central creative mechanism.
The missing input for such a mechanism is still an independently
payable actual-theta signed-compensation estimate. Full matching
Mathlib coverage is unchecked; no cross-notebook input is used.

## Exact proposed test and its relevance

The main gap remains L030–L032/C032a all-degree mixed positivity.
The intermediate question concerns only whether the scalar ingredients
of the fixed-shift envelope can bypass unavailable indexed endpoint
data. A countermodel would delimit that proposed replacement; it would
neither disprove actual overlap nor refute actual minor positivity.
A valid uniform bound would instead justify investigating that replacement.

For the proposed test fix k=6002, J=k+1, m=9000000000000 and
H=3,000,175,332,800. The candidate class consists of strictly increasing
positive ordinates gamma_j tending to infinity, with gamma_J>4,
sum_j gamma_j^(-2)<infinity, and exactly 12,363,153,437,138 ordinates
at or below H. Require the inclusive count to satisfy L836(9)'s upper
bound N(t)<=U(t) for every real t>=e, with its exact constants. Require
the normalized real genus-zero product
F(z)=prod_j(1-z/(4 gamma_j^2)), compactly convergent. All its zeros
are simple positive real numbers. This is an explicitly abstract class;
it does not assume the actual theta coefficients or an actual zeta zero.
L836 uses this upper bound, rather than the unused lower half of the
source's two-sided estimate, in its residual-envelope argument.

Use the exact definitions of T,R,q,a,s,V and B in L836, with
s=(1+q)/2. The expression to test, with no interval inflation, is

\[
\mathcal H_m=\mathcal B(s)+2\log k+(2k-2)\log(1+q)
 +k\log2-2k\log(1-q)+(m+k+2)\log s.
\]

It is precisely the unrounded coarse expression from L836(15) at
r=m+1, not an arbitrarily chosen large C_+. A proposed obstruction
must supply a fully admissible product with H_m>=0 (preferably a
strict margin), verifying the count inequality for all heights, the
finite-height total, convergence and the complete positive tail. A
formal limit q->1 alone does not establish existence in this class.
If these premises instead exclude such close pairs, identify the exact
quantitative separation and check whether it pays the strict H_m<0
threshold. Do not infer a mathematical miss from absent numerical data.

Essential local inputs are L836's scalar formula and L835's explanation
of its sufficient sign threshold, with L834/L832/L467 providing the
actual-function comparison. C832a's already audited finite-PF order is
context, not a premise that forces this absolute majorant to succeed.
The next source review should reuse adequate citations and inspect only
missing theorem hypotheses/cases for this changed target. No general
spacing or product theorem should be reproved merely to claim novelty.
Full matching Mathlib coverage is unchecked. No cross-notebook input.

The earlier step659/667 stops, the FLINT setup failure and the LMFDB
access failure remain intact. This nomination does not reopen the
failed transports or approve another L836 audit. A countermodel would
stop only the deduction from the listed abstract premises. An actual-Xi
estimate using additional arithmetic correlations would remain separate.
Source coverage must be decided before mathematical work; this turn
neither derives nor approves the proposed construction.
