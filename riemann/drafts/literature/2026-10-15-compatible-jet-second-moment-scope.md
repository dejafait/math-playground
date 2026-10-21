# Critical-jet second moments: completed source comparison

TARGET: Test whether L415's joint-sign-avoiding relaxation can also match all six critical-jet second-moment asymptotics while retaining every existing constraint.
CHECKED: 2026-10-15
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 146 compared L414/L415, L401's normalization, L389's Hardy identification, the step-138/140/142/144 assessments and the two October-15 compatible-jet failure records; targeted mixed-second-moment, Hardy-derivative-product and support-constrained moment queries found the direct Bui--Hall formula and the unused Das--Pujahari lead below. No inspected theorem decides the enlarged feasibility problem; no novelty is inferred.
SOURCE_EVIDENCE: Freshly read Bui--Hall arXiv:2304.05178v1, 11 April 2023, Introduction p. 1, Hardy definition, odd-order bound and equation (1), including both parity explanations and reference [11], checking PDF text against HTML. Reused precise primary moment/atomic/weak-duality coverage in the step-138 and step-144 assessments. Hall's original publisher pages and the Das--Pujahari public page did not supply complete theorem text and are not independently imported.
COMPARISON: Bui--Hall explicitly covers all fixed ordinary Hardy-derivative pairs needed here, with a sharp cumulative polynomial/error for even order and a separate odd-order bound. L389 identifies f=F/A with a constant-sign Hardy function. The required log(2+t) normalization is a standard partial-summation specialization to document in the mathematical attempt; neither the source nor atomic replacement decides joint feasibility.
GAP: Test one simultaneous law or an error-robust separator with the six sourced degree-two constraints specified below and every L415 constraint, first documenting the imported-moment normalization. No enlarged law or separator is established here.
REASON: Essential primary coverage now suffices for the saved bounded mathematical target. This literature-only step supplies source coverage, without deriving an enlarged-law result or modifying lemmas or mathematical scripts.
LITERATURE_REASON: The proposed extra second-moment matrix changes the hypotheses and lower-order scales. It requires source comparison rather than repetition of the stopped polynomial-to-clipping implication or the step-99 signed-clipping source search.
SCOPE: Exactly L415's local relaxation, both first means, all existing errors, exact curvature and fixed bounds; add the six unweighted raw second moments at the sourced scales below. No uniform height marginal, actual response/global realization, independent phases, finer even-entry coefficients or regulator conclusion.

## Startup proposal retained

The following paragraphs record step 145's proposal. Their pending-source
language is superseded by the completed step-146 comparison below;
their mathematical limitations and stopping evidence remain in force.

The main gap remains actual negative-Bcal clipping and the full regulator
margin toward global mixed positivity. The proposed intermediate target
tests additional lower-order physical covariance information rather than
repeating an implication from the already refuted selected list. Its
plausible downstream use is to distinguish a usable omitted constraint
from continued insufficiency of these finite moments. No claim is made
that a further moment obstruction alone would resolve the main gap.

Use the exact normalized critical triple X=(x,y,z) defined in L414,
with ordinary derivatives and the envelope conversion unchanged. The
six proposed observables are x^2, xy, xz, y^2, yz and z^2, averaged
over the actual sharp dyadic interval. Their leading constants, possible
vanishing leading terms and necessary error scales must be extracted
from inspected primary theorems and compared with existing notebook
results. No values or feasibility claims are supplied here. Check for
duplicates and recorded obstructions in the specifically relevant
Hardy-jet moment records before extending any proof.

The continuation uses L369 and L415, retaining L414's audited
L367/L368/L370/L390/L393/L401/L405/L410 scope. Review must distinguish
ordinary Hardy jets from derivatives of normalized functions, and
unweighted degree-two means from Delta-weighted degree-four means.
The cited atomic theorem is conditional on a feasible integrable law;
it does not supply missing matrix constants or joint feasibility.

Continue only after exact primary coverage supports all six additional
constraints with sharp-interval errors adequate for a bounded joint
feasibility test. Its later mathematical success criterion is one law
meeting the whole enlarged list, or a pointwise separator whose
integrated gap survives every permitted error. Failure of a restricted
bulk-atom ansatz is not a separator. If essential source coverage is
persistently blocked or a test merely repeats the existing mechanism
without discriminating new information, park that dependent test and
choose an independently testable mechanism. Do not derive or approve
the enlarged mathematics during the approval turn.

Actual/global realization, a uniform height marginal, the actual clipped
mean, L413's regulator-scale/full-error margin, common-zero upper counts
and global mixed positivity remain unresolved. L410/L412/L413/L414/L415
and the step-99 signed-clipping source stop are preserved at their exact
scopes; no historical stop is treated as a global ban. Full matching
Mathlib coverage for this changed target is not checked. This file is
the original REVIEW_REQUIRED proposal. The completed comparison follows.

## Completed comparison — 2026-10-15, step 146

This is LITERATURE / NOVELTY_UNCHECKED / literature_comparison work.
The advance is usable source coverage, not a feasible law or new moment
theorem. No lemma or mathematical script was written or run.

### Inspected primary input

H. M. Bui and R. R. Hall, *On the derivatives of Hardy's function Z(t)*,
Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
[DOI 10.1112/blms.12859](https://doi.org/10.1112/blms.12859),
[arXiv:2304.05178v1, Introduction p. 1](https://arxiv.org/pdf/2304.05178v1#page=1),
[equation (1) and preceding display](https://arxiv.org/html/2304.05178v1#S1):
for fixed nonnegative k,l, let J_kl(T)=integral_0^T Z^(k)Z^(l).
For k+l=2s and |k-l|=2d the stated formula is

    J_kl(T)=(-1)^d T Q_(2s+1)(log(T/(2pi)))/(4^s(2s+1))
               +O_(k,l)(T^(3/4)(log T)^(2s+1/2)),

where Q is monic of degree 2s+1. For odd k+l the preceding bound
is J_kl(T)=O_(k,l)(T^(1/3)). The text explains the even case via
Hall [11, Theorem 3] and integration by parts, and the odd case via
integration by parts and fixed-order pointwise bounds. Neither display
assumes RH. Import these precise statements; no reproof is needed.

The underlying reference is R. R. Hall, *The behaviour of the Riemann
zeta-function on the critical line*, Mathematika 46 (1999), 281--313,
[Theorem 3, DOI 10.1112/S0025579300007762](https://doi.org/10.1112/S0025579300007762).
Its Wiley PDF request redirected to an abstract and Cambridge gave an
abstract/access page. That theorem/proof was not independently read.
This is not an essential blocker: the needed mixed statement and both
parity cases are explicit in the inspected Bui--Hall research paper.
No unread Hall proof case or stronger conclusion is imported.

### Exact applicability scope for the later mathematical attempt

Use X_j=f^(j)/L(t)^j, j=0,1,2, with L(t)=log(2+t), as in L401.
L389 (3) proves f=-sigma Z with one constant sigma in {1,-1} on
the connected eventual ray, including at zeros. Thus each product of
two ordinary f derivatives is the corresponding Hardy product. These
are not the physical P_j: L414's alpha,q conversion remains mandatory
for Delta and Bcal.

Extraction of the source coefficients for the six index pairs gives:

| Observable | (j,k) | m=j+k | Coefficient of T(log T)^(m+1) in source |
| --- | --- | --- | --- |
| x^2 | (0,0) | 0 | 1 |
| xy | (0,1) | 1 | odd-order bound; no polynomial main term |
| xz | (0,2) | 2 | -1/12 |
| y^2 | (1,1) | 2 | 1/12 |
| yz | (1,2) | 3 | odd-order bound; no polynomial main term |
| z^2 | (2,2) | 4 | 1/80 |

The approved specialization and feasibility constraints are

    E x^2=ell+O(1),       E xz=-ell/12+O(1),
    E y^2=ell/12+O(1),    E z^2=ell/80+O(1),
    E xy=O(H^(-2/3)ell^(-1)),
    E yz=O(H^(-2/3)ell^(-3)),              ell=log H.

For actual source data E means H^(-1) integral_[H,2H]; the later
feasibility test asks for these same asymptotics on its law. These are
raw second moments, not centered covariances: no first means of x,y,z
are imposed. The odd entries need not vanish exactly. No independently
prescribed O(1) constants or lower polynomial coefficients are added.

This is the specified known-source specialization to justify at the
start of the mathematical attempt, not a new normalized-moment proof
produced in this literature turn. Give the elementary partial-summation
applicability argument with weight L(t)^(-m) and both sharp endpoints
before using the constraints. The cumulative polynomial and power-saving
error cover all four even pairs; retain the odd primitive bound for the
two smaller errors. There is no smooth-to-sharp limit, fast carrier,
response head, growing derivative order or conjectural higher moment.
Finer even-entry errors or additional moments lie outside this approval.

### Reuse, duplicates and unused alternatives

Reuse [step 138](2026-10-15-jet-supported-moment-feasibility-review.md)
and [step 144](2026-10-15-compatible-jet-first-mean-critical-audit.md)
for unchanged first/cubic/quartic inputs, absolute envelopes and
atomic/weak-duality qualifications. Bayer--Teichmann,
arXiv:math/0502473v2, Theorem 1, Corollaries 1--2 and Remarks 1--2,
pp. 2--4, allows finite-coordinate atomic replacement only after an
integrable feasible law exists; six extra coordinates do not remove
that premise. Bertsimas--Popescu, SIAM J. Optim. 15 (2005), Section 2,
Theorems 2.1--2.2, grants neither unproved interiority nor strong duality.
Check any separator pointwise and against every allowed error.

L414/L415 and the two October-15 compatible-jet ATTEMPTS records decide
smaller lists. Their orientation and rare/bulk constructions do not
certify the added constraints. L401's 21 entries are Delta-weighted
quartics, not these unweighted degree-two data. L381's October-8 Young
assessment is a general alternative, but a new shifted-moment calculation
is unnecessary given the direct mixed formula. No duplicate enlarged
feasibility result was found in the specifically searched local records.

M. K. Das and S. Pujahari, *Mean of the product of derivatives of Hardy's
Z-function with Dirichlet polynomial*, J. Number Theory 258 (2024),
334--367, [DOI 10.1016/j.jnt.2023.11.001](https://doi.org/10.1016/j.jnt.2023.11.001),
was located on the publisher page and author's research list. The public
Theorem 3 and Section 4 omit essential displayed formulas in retrieved
text; the full theorem/proof was not inspected. This is an unused lead,
not coverage inferred from an abstract. No further access is needed
before the present ready test.

Queries included `"Hardy" "mixed second moments" derivatives Z(t)`,
`"Mean of the product of derivatives" Hardy`,
`Hall "The behaviour of the Riemann zeta-function on the critical line" pdf`,
`Das Pujahari Hardy derivatives Dirichlet polynomial 2024 arxiv`,
`"Hardy" derivatives "covariance" "moments" sign`, and
`"truncated moment" "prescribed support" "second moments" feasibility`.
No matching enlarged-law theorem was established; snippets and unrelated
results are not mathematical evidence or evidence of novelty.

One simultaneous enlarged law or an error-robust pointwise separator
is the discriminating test. A failure of a restricted bulk-atom ansatz
is not a separator for all laws. Actual/global realization, a uniform
height marginal, actual clipping, the regulator margin, common-zero
upper counts and global mixed positivity remain independent gaps.
Full matching Mathlib coverage is not checked. No feasible law,
separator, canonical lemma, DAG edge or proof-assembly change is made.
