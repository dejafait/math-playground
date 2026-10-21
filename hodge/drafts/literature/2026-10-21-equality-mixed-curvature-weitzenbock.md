# Equality kernel — differential mixed-curvature source comparison

TARGET: Assess a global Weitzenböck identity for the mixed curvature of L071's equality kernel, retaining all pure-curvature commutator terms, for a sign obstruction beyond L131/L142.
CHECKED: 2026-10-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact mixed-curvature/product Yang–Mills searches and broader coefficient-valued Bochner searches located Oliveira–Waldron arXiv:1812.10866v2; scoped drafts/literature and ATTEMPTS searches found the distinct normal-moduli, charge-splitting and fixed-quartic stops, but no completed product-projection/sign calculation for this target.
SOURCE_EVIDENCE: Read Oliveira–Waldron v2 (8 February 2019), section 4 opening and section 4.1 equations (4.1)–(4.13), PDF pp. 10–12; complete Proposition 4.1 statement and projection/integration proof, pp. 12–13; section 4.3 through (4.17), pp. 13–14. Reuse the earlier source comparisons and ready invariant-module assessment specified below.
COMPARISON: The general two-form formula retains every coupling and supports a finite product specialization; neither compatibility preservation nor Kähler trace-sector cancellation asserts mixed-curvature vanishing. No applicable sign conclusion was imported or calculated.
GAP: The mixed product projection, full Riemann-term reduction, and sign and zero locus of the pure/mixed commutator contraction are uncomputed; global parallelness, vanishing and F exclusion remain unproved.
REASON: Essential formula coverage is accessible, supporting one separately approvable mathematical specialization rather than further general browsing; the known identity is an input, not a new obstruction.
LITERATURE_REASON: The saved REVIEW_REQUIRED target lacked essential coverage of the coefficient-valued curvature identity and projection proof beyond the earlier moduli-curvature, charge and quartic assessments.
SCOPE: Only L071's hypothetical equality F, identical marked K3 factors/common metric, actual SU(2) connection, and the full mixed projection of the cited formula; the finite test allows every simultaneous-quaternionic su(2)-valued two-form, including arbitrary pure ASD blocks. No changed functional optimization, new metric, Green estimate or global curvature realization is covered.
COVERED_TARGET: Derive the product projection of Oliveira–Waldron (4.6) and test the sign and zero locus of its full mixed-block energy coupling on simultaneous-quaternionic su(2) curvature.

## Relevance and bounded outcome

The main gap is algebraic realization of every primitive rational Hodge
class, already unresolved on arbitrary fourfolds. The intermediate target
is readiness for one differential necessary-condition test on the equality
kernel. A vanishing-forcing identity could conflict with its nonzero mixed
action; parallelness alone would require a further argument. F existence,
reconstruction, transverse transport, other representatives and the
universal target remain independent gaps.

This review supplies an inspected general identity and a precise future
test, not a sign result. Outcome EXPLORATION / LITERATURE / REPRODUCTION:
source readiness improved, with no mathematical advance beyond the sources
and no kernel exclusion. The proposed calculation has not been executed.
Its newly covered continuation receives separate next-turn approval.
The initial REVIEW_REQUIRED registration is superseded by this comparison.

## Primary input and conventions

Gonçalo Oliveira and Alex Waldron, *Yang-Mills flow on special-holonomy
manifolds*, Advances in Mathematics **376** (2021), 107418,
[arXiv:1812.10866v2](https://arxiv.org/pdf/1812.10866v2#page=10),
8 February 2019. Equation numbers/pages refer to v2, whose section 4.4
correction is recorded on arXiv; the input here is section 4.1.

For a smooth metric connection A, denote its curvature by R_A and the
coupled derivative by nabla. The source uses
Delta_A=d_A^*d_A+d_A d_A^*. Its general two-form identity (4.6), p. 11,
in a normal orthonormal frame, is

\[
\begin{aligned}
(\Delta_A\omega)_{ij}
={}&(\nabla^*\nabla\omega)_{ij}
 -[(R_A)_{ik},\omega_{kj}]+[(R_A)_{jk},\omega_{ki}]\\
 &+R^g_{ik\ell k}\omega_{\ell j}
  +R^g_{ik\ell j}\omega_{k\ell}
  -R^g_{jk\ell k}\omega_{\ell i}
  -R^g_{jk\ell i}\omega_{k\ell}.
\end{aligned}
\]

Repeated indices are summed; R^g is the source's Riemann tensor.
Equations (4.7)–(4.9) fix its contracted bracket, symmetric on two
adjoint-valued two-forms; (4.11) gives the intrinsic version.
Proposition 4.1 projects evolution, retains cross terms and integrates
a norm estimate to preserve an initially zero component. Section 4.3's
cancellation treats the Kähler trace sector. Equations (4.13), (4.15)
are norm estimates, not the sign assertion sought here.

## Applicability and obligations for specialization

L131 supplies the actual conditional SU(2) connection, not just a
topological SU(2) structure. Its underlying real metric bundle fits
so(E); the connection and bracket preserve su(2), so the identity
restricts to these coefficients. A positive rescaling of the invariant
coefficient pairing does not change the proposed sign. The product is
smooth, compact and without boundary; reducible factor restrictions
cause no inverse-Laplacian or regular-moduli hypothesis here.

The retained exact data are integral c_1(F)=0 and
ch_2(F)=-14e_1-21e_2-tau_D, with the full tensor and identical metric
of L071. L095's mixed derivative is nonzero and ASD-complex harmonic.
It does NOT supply Delta_A K=0 for the mixed curvature two-form K.
A future application must put omega=R_A in (4.6) before projection.

For that attempt name the form-leg blocks P=(R_A)_{11}, K=(R_A)_{12},
Q=(R_A)_{22}. Split every summed index over both factors, checking
P/P, P/K, P/Q, K/K, K/Q and Q/Q cases instead of presupposing which
survive. Keep both commutators and all four Riemann summands until the
product connection and Ricci-flatness justify any reduction. Ricci-flatness
is no reason to delete bundle commutators. Check commutation of the
rough Laplacian with the parallel form-leg projection separately from
any claim about d_A. Compact integration must keep the real pairing,
source signs and multiplicities. These are proposed obligations, not
new derivations or an asserted product identity. The general formula
needs citation, not reproof; only this specialization is proposed.

The source's Kähler trace-sector result cannot simply be assigned to
this different projection: no inspected theorem makes that transfer.
Likewise compatibility preservation starts from zero, whereas the
hypothetical equality kernel has a prescribed nonzero mixed action.

## Finite test and continuation or abandonment

Reuse the adequate invariant-module coverage in
[the quartic feasibility assessment](2026-10-20-mixed-calibration-quartic-feasibility.md),
its Fowdar (2.6) input and full real thirty-variable domain su(2) tensor W
on H direct sum H. Reuse only that domain; the stopped quartic bound
is not reopened. The new expression is the full mixed-block energy
coupling from (4.6), retaining both independent pure ASD blocks. It is
not L142's characteristic-square density or fixed Psi functional.
No expression, sample or sign is calculated in this source turn.

The concrete test is: derive and integrate the correct projection,
then determine whether its coupling has the vanishing-forcing sign
on the entire domain, and determine its zero locus. A positive result
requires an exact all-values argument, including commuting coefficients
and K=0. An exact admissible wrong-sign tuple parks this universal
Bochner sign mechanism; it need not be realized by a global F and
would not exclude F by itself. An unevaluated norm or Green estimate
also parks this bounded mechanism. Fixed factor charges cannot replace
pointwise curvature bounds or determine correlated density products.

If only semidefiniteness survives, distinguish K=0 from nabla K=0:
parallelness alone is no contradiction supplied here. A further holonomy
argument would need assessment. Passing the test constructs neither
a kernel nor a cycle. Essential continuation inputs are L071, L095,
L131, the displayed primary identity and the reused invariant module;
F existence, integration of pointwise data, reconstruction, transport
and universal primitive Hodge realization remain unresolved.

## Duplicates, failures and source limits

Read L071's hypotheses/conclusion, L095 through its harmonicity proof,
L131's connection/charge passage and ATTEMPTS/082. Reuse
[the normal-curvature review](2026-10-14-equality-stable-normal-curvature-test.md)
for uncontrolled moduli Green/bracket data and
[the splitting review](2026-10-19-equality-connection-product-splitting.md)
for null-charge/zero-horizontal-curvature premises. Those assessments
remain adequate for their unchanged scopes. This new test concerns
coefficient curvature on the product, rather than moduli Riemann
curvature, the failed null-charge criterion or quartic optimization.

Queries: `Yang Mills curvature Weitzenbock formula product manifold
mixed curvature Bourguignon Lawson Simons`; `Yang Mills connections
Bochner formula curvature two form Ricci commutator equation`;
`"Yang-Mills flow on special-holonomy manifolds" Weitzenbock`;
`"Yang-Mills" "product" "mixed curvature" Weitzenbock`;
`"Stability and isolation phenomena for Yang-Mills fields" pdf`.
Bourguignon–Lawson was an additional lead only: its primary theorems
were not inspected and supply no premise or exclusion. Oliveira–Waldron's
PDF supplied all essential passages despite intermittent HTML failures.
No essential source blocker remains for the finite test. The search
was bounded and establishes no novelty or exhaustive noncoverage claim.

Mathlib matching coverage is not checked; unknown is not absence.
No lemma, mathematical script, DAG or main argument was changed.
