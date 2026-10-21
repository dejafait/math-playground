# Approximating curve's geometric Tate parameter — completed source comparison

TARGET: Determine whether strengthening L046's fixed congruence precision ensures split multiplicative reduction over Q_3 with geometric Tate parameter q_0 satisfying v_3(q_0)=30, while retaining L045–L047.
CHECKED: 2026-10-11
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused the inspected L041/L042 Tate coverage and L044–L047 approximation/adjunction/image assessments; searched the relevant October 11 assessments and histories 138–154 for duplicates; external searches for coefficient-local reduction constancy and characteristic-3 minimal/split criteria located Milne, Cremona and Schrettner's primary passages recorded below.
SOURCE_EVIDENCE: Read Milne EC2 (2021) II.2 Theorem 2.4 and invariant formulas pp.52–53, II.3 pp.58–61 and III.3 (23)–(26) pp.102–103; Cremona second edition (1997) III.1 (3.1.2)–(3.1.3) pp.62–63 and III.2 Tate's Algorithm pp.65–67, including the p=3 and multiplicative branches, with the 2003-09-26 errata; Kedlaya fall-2004 Theorems 1–2 pp.2–4; Schrettner arXiv:2508.12329v1 Theorem 1.1 and introduction's minimal-model qualification.
COMPARISON: Known invariant, minimal-model, nodal/split and Tate criteria cover the proposed mechanism at residue characteristic 3; the actual original-cubic congruence specialization and simultaneous reselection remain to be proved. Finite-module constancy alone is insufficient, and the broader regular-model constancy theorem does not replace the minimality check.
GAP: In a separate research turn choose a sufficient finite precision, verify discriminant valuation, unit c4, local minimality and rational distinct tangents for L044's original cubic, identify its unique geometric parameter and valuation, then retain L046 and apply L045/L047 to the same reselected curve.
REASON: Missing essential source coverage is now supplied; the unchanged target is ready for a bounded known-method specialization, without deriving its congruence threshold or new result in this literature-only turn.
SCOPE: Exactly TARGET for L044's monic Z_3 cubic, integer congruence approximants, absolute valuation v_3(3)=1 and a precision fixed before L046's selection. Allows invariant congruences, unit-c4 minimality, characteristic-3 split-node/Tate tests and same-curve retention only; no q_0=3^30 or sufficient initial theta data.
LITERATURE_REASON: The startup gate required first source comparison for reduction type and geometric parameter, outside the ready finite-torsion and restricted-image assessments; unchanged external inputs are reused.

## Preserved proposal (source-status claims superseded below)

The main gap remains finite B>=A. The intermediate question asks
whether approximation can retain a specified bad-place geometric
parameter condition alongside the audited torsion and image properties.
A positive answer could supply one more initial-data prerequisite;
it would not supply sufficient initial data or a numerical comparison.

Use L046's original monic cubic neighborhood of L044's f, not an
assumed integral equivalence with the scaled short model. The proposed
q_0 is the changed curve's geometric Tate parameter, with v_3(3)=1;
do not impose q_0=3^30. A stronger fixed precision would be chosen
before selecting E_0, then L045 and L047 applied to that same choice.
Neither the present arbitrary E_0's satisfying this target nor the
success of such strengthening is asserted.

Essential inputs are L044's local equation, L046's fixed-precision
quantification and L045/L047's same-curve conclusions, retaining
L042's E_q, Omega,H,N through them. Review narrowly the existing Tate
coverage associated with L041/L042 before retrieving missing primary
results. Check split versus nonsplit reduction, minimality and model
hypotheses at residue characteristic 3. Distinguish coefficient
closeness, isomorphic torsion modules and isomorphic curves. The
geometric parameter, not a pilot root, is intended. Compare known
results and previous stops before approving a derivation.

Continue only if inspected criteria supply a finite precision condition
compatible with L046 and imply both split multiplicative reduction
and the exact requested valuation. Otherwise identify the missing
hypothesis or obstructing case; finite-module agreement alone is not
proof. No such precision threshold or new lemma is derived here.

ATTEMPTS/027 still excludes the exact Tate curve; this question
concerns a different curve. ATTEMPTS/022,025,026 are preserved.
Conditions at other places, sufficient initial data, native/input/action,
pilot transport, essentiality and original finite B>=A remain open.
Full matching Mathlib coverage is unchecked. This proposal requires
a separate literature turn before mathematical work.

## Completed comparison — 2026-10-11

### Primary criteria actually inspected

[J.S. Milne, *Elliptic Curves*, second edition (2021)](https://www.jmilne.org/math/Books/EC2.pdf),
II.2, pp.52–53, defines the general integral Weierstrass invariants,
including c4=b2^2-24b4, the polynomial discriminant and j=c4^3/Delta;
Theorem 2.4 gives nonsingularity and pointed coordinate changes.
II.3, pp.58–61, treats nodes, rational tangents and multiplicative
reduction for a minimal equation. Its general-Weierstrass node
criterion allows arbitrary characteristic; the simplified short-form
square test excludes 2 and 3. The section explicitly extends to Q_p
and finite extensions. III.3, pp.102–103, (23)–(26), gives the standard
integral Tate coefficients, discriminant product and j-series, and
identifies the split-node curves over Q_p. These passages supply
criteria, not an already-proved neighborhood for our cubic.

[J.E. Cremona, *Algorithms for Modular Elliptic Curves*, second
edition (1997), Chapter III](https://johncremona.github.io/book/fulltext/chapter3.pdf),
III.1, pp.62–63, (3.1.2)–(3.1.3), states the invariant laws
u^4 c4'=c4 and u^12 Delta'=Delta. III.2, pp.65–67, accepts an
integral equation without assuming it minimal. Read the initial
coordinate adjustment, especially the separate p=3 branch, and
lines 18–22: when p does not divide c4 the algorithm exits with
type I_n, n=ord_p(Delta), and tests roots of
X^2+a1 X-a2 in the adjusted residue equation. This is the branch
needed here; later additive cases are not inputs. The supporting
unit-c4 minimality test uses the invariant transformation laws and
integrality, without running the remaining algorithm. Milne's
minimal-equation and rational-tangent criteria still need to be
applied to the actual cubic.

The [author's edition page](https://johncremona.github.io/book/)
identifies the second edition, published 15 May 1997.
Checked its [errata, last updated 26 September 2003](https://johncremona.github.io/book/errata.pdf):
the p.64 residue-interval sign correction does not alter the cited
invariant laws or p.66–67 multiplicative branch. No uninspected
Silverman or original Tate proof is claimed read.

[K.S. Kedlaya, *Introduction: the Tate curve*, fall 2004](https://kskedlaya.org/18.727/tate-curve.pdf),
Theorem 2, p.4, assumes a finite extension K/Q_p and |j(E)|>1.
It gives a unique nonzero q in K with |q|<1 defining the geometric
Tate isomorphism; this isomorphism is over K exactly in the split
multiplicative case. Read its proof discussion: part (a) uses series
inversion and part (b) cites Silverman V.5.3. Reuse the named Tate
theorem, without reproof. Theorem 1 and its p.3–4 discussion give
the discriminant/j-series and defer uniformization surjectivity to
Silverman. Use Milne's standard coefficient normalization, preserving
the earlier assessment's warning about Kedlaya's displayed a4 formula.
The valuation comparison must use that integral j-series, with
v_3(3)=1; a pilot root or valuation normalized in H or N is a
different quantity.

### Stronger-result comparison and discovery record

Queries included `elliptic curve split multiplicative reduction
integral Weierstrass tangent lines c4 unit minimal residue
characteristic 3`, `elliptic curve p-adic local constancy reduction
type Tate parameter j valuation coefficient approximation`, and
`Tate algorithm c4 unit minimal equation pdf Tate 1975 182`.
Only the primary passages above are proposed inputs. Search snippets,
encyclopedia and software-manual hits are not mathematical evidence.

Inspected [Jakab Schrettner, *Local constancy of reduction type and
related invariants for curves in p-adic families*, arXiv:2508.12329v1,
17 August 2025](https://arxiv.org/html/2508.12329v1), Theorem 1.1:
over an excellent discrete valuation ring, field characteristic
different from 2, sufficiently close same-degree separable
hyperelliptic equations admit regular models with the same special
fibre. The introduction expressly declines a corresponding
minimal-regular-model assertion. Its discussion points to Tate's
algorithm for elliptic local constancy. This inspected theorem is
not imported as proof of our exact split reduction/parameter target;
its full proof is unread. The paper's DDMM22/Faraggi–Nowell references
and the newly surfaced journal version are unread, unnecessary leads.
The directly inspected elliptic criteria already cover this target.
No originality is inferred from the scoped duplicate search.

### Applicability and approved bounded continuation

The main gap is original finite B>=A. The intermediate target remains
the exact TARGET above. A positive specialization would close one
selected-place geometric prerequisite, with the already retained
finite torsion and restricted large image; it would not provide a
numerical comparison or sufficient initial data.

The research turn may specialize the cited inputs as follows. Use
L044's actual monic cubic, written as a general Weierstrass equation;
check its invariants with their integral polynomial formulas. Choose
precision sufficient to preserve the discriminant's exact valuation
and the necessary reduction data. Establish local minimality using
the unit-c4 criterion with its integral-model hypotheses. Check
distinct rational tangents in the characteristic-3 residue model,
using the applicable general criterion or the inspected p=3 branch.
Then apply Tate Theorem 2 and the standard integral j-series to test
the geometric parameter's requested valuation. No threshold, cubic
invariant value, tangent computation or new implication is proved
in this literature turn.

Apply these tests before selecting E_0. L046 explicitly allows any
fixed sufficient precision; its quadratic coefficient representative
is chosen after that precision, and its full-rank two-parameter
count does not require uniformity as precision varies. The research
must justify strengthening the original monic neighborhood and
retaining the full local 210-module. Apply L045 and L047 to this
same reselected E_0. The scaled short equation is a pointed Q_3
isomorphism but has not been asserted to be a minimal integral
reduction model, so it cannot replace the original cubic in the
reduction test. No reproof of torsion constancy, sieve bounds or
Tate uniformization is authorized or needed. The identified extra
work is the model-specific congruence/minimality specialization;
REPRODUCTION is its appropriate classification.

Continue if a finite precision yields both split multiplicative
reduction and exactly v_3(q_0)=30 while preserving the cited same-curve
inputs. Otherwise isolate the failing model hypothesis or congruence
test and stop that implication; torsion-module agreement alone cannot
rescue it. Essential local results are L044, L046 and the downstream
L045/L047, retaining L042's Omega,H,N. L041 is source orientation and
L043/ATTEMPTS/027 are contrasts, not premises for this specialization.
The narrowed searches found no completed duplicate of this target.
Other-packet stops ATTEMPTS/022,025,026 remain preserved. No
cross-notebook theorem is used.

The changed curve's exact q_0 is unestablished and q_0=3^30 is not
assumed. Conditions at other places, field-of-moduli/full initial
data, native/input/action, marked pilot transport, essentiality and
finite B>=A remain unresolved. Full matching Mathlib coverage is
unchecked, with no absence claim. This source comparison creates no
lemma or mathematical script and changes no proof argument or DAG.
The newly ready assessment is for a separate subsequent invocation;
it is not a correctness certificate for the proposed result.
