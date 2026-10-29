# L166 — The complementary Yoneda test leaves a global extension operation

## Hypotheses

Retain L071's identical marked projective K3 factors, original common
metric and ordered triple, and L116's entire conditional family, including
its L108/L109/L111/L115 inputs. The hypothetical locally free rank-two
product-polystable F on X=S_1 x B has integral c_1(F)=0 and
ch(F)=2-14e_1-21e_2-tau_D+62P, with the full prescribed mixed tensor.
Let V=End_0(F), C=Rp_*V, M=R^1p_*V and W=R^2p_*V. Retain the full
finite-point W, possibly empty Z, and unknown t=h^0(B,M).

Use L116's actual j:M[-1] -> C and trace-adjoint r:C -> M[-1],
with rj=id. Set H=H^0(B,M), K=H^1(B,M), j_1=H^1(j), i=H^2(j)
and R=H^2(r). Use L165's normalized fourfold Serre form Q and its
nondegenerate restriction S on K, so Q(x,iw)=S(Rx,w).
All coefficients and forms are complex; these pairings are bilinear,
not Hermitian. Fix the same canonical trivializations and trace scalar.

Use the actual derived cup followed by the coefficient commutator
mu:C tensor^L C -> C. On Dolbeault forms it is
[alpha,beta]=alpha beta-(-1)^(deg(alpha)deg(beta)) beta alpha.
No integrability, bracket-compatible splitting, pure-relative global
representatives, value of the bracket, or existence of F is assumed.

## Conclusion

The actual complementary operation is represented by

    kappa = r mu (j tensor j)
       in Hom_D(B)((Sym^2 M)[-2], M[-1])
        = Ext^1_B(Sym^2 M,M).

Here and below the notation denotes the factor through Sym^2 M,
with uv the image of u tensor v, without a factor 1/2. Evaluation on
global sections satisfies

    kappa(u v) = R[j_1u,j_1v] in H^1(B,M).                 (1)

For closed actual Dolbeault representatives alpha,beta,gamma of
j_1u,j_1v,iw, respectively, their degrees are 1,1,2 and

    S(kappa(u v),w)
      = Tr_X(alpha beta gamma + beta alpha gamma)
      = Tr_X(alpha[beta,gamma]).                          (2)

Tr_X denotes matrix trace, product with the fixed holomorphic volume
form, integration and the common normalization of Q. Cyclicity does
not cancel the two terms: in the second expression the bracket has
degrees 1 and 2. Equations (1)--(2) leave an undetermined actual global
operation. No zero or nonzero value for it is established. Its restriction
as an Ext^1 morphism at every stalk is zero, which does not establish
its global vanishing or the vanishing of its evaluation on H.

This is an EXPLORATION / REPRODUCTION record of the bounded test, not
a new exclusion or an informative counterexample. It parks the proposed
vanishing proof by cyclicity alone. It neither invalidates a possible
geometric vanishing theorem nor constructs a compatible bracket or F.
No cardinality bound, transport or primitive Hodge realization follows.

## Proof

**Imported operations.** Reuse the prior SPECIALIZE assessment
`drafts/literature/2026-10-25-adjoint-complementary-yoneda-component.md`.
Derived cups and compatibility with composite pushforward are imported
from [Stacks 20.31.1, 0FKU](https://stacks.math.columbia.edu/tag/0FKU)
and [20.31.7, 0FP6](https://stacks.math.columbia.edu/tag/0FP6).
The actual trace adjunction is the one already specialized in L116/L165
from [48.12.6, 0G81](https://stacks.math.columbia.edu/tag/0G81) and
[48.27.1(5),(7), Remarks 2--3 and Lemma 4, 0FVU](https://stacks.math.columbia.edu/tag/0FVU).
Here V and M are locally free, C is perfect, p is smooth proper, and
B and X are smooth projective with the fixed canonical trivializations.
These hypotheses do not require W to be locally free.

Import cyclic trace from Bandiera--Manetti--Meazzini, *Formality conjecture
for minimal surfaces of Kodaira dimension 0*, Compositio Math. 157
(2021), 215--235, DOI 10.1112/S0010437X20007605,
[arXiv:1907.10690v2, Definition 3.6/Example 3.7, pp. 7--8,
and Section 5 through (5.1), p. 14](https://arxiv.org/pdf/1907.10690v2).
Example 3.7 covers locally free F on a smooth projective n-fold with
holomorphic volume form, hence n=4 here. Restrict the trace construction
to the actual commutator-closed coefficient V. Its perfect trace pairing
is checked in L165; no trace-free formality statement is imported.
Theorem 3.8's n<=2 hypothesis is not applicable. Retain the recorded
intermediate-line [h,g] versus final [g,h] discrepancy: use the final
invariant identity, with the explicit sign verification below. The
general trace and duality theorems are imported, not reproved.

**Placement of the surviving operation.** Local freeness of M identifies
M[-1] tensor^L M[-1] with (M tensor M)[-2]. The derived interchange of
the two degree-one inputs is minus the ordinary interchange on M tensor M.
Antisymmetry of mu therefore makes mu(j tensor j) symmetric on M tensor M.
Over C it factors through the ordinary Sym^2 M. Composing with the
specific r gives the displayed kappa; shifting both source and target
by two identifies its group with Hom_D(B)(Sym^2 M,M[1]), namely Ext^1.
No replacement of r by the projection of a chosen splitting occurs.

For u,v in H, their product is a class map O_B -> Sym^2 M. Precompose
kappa, after shifting by two, with this map. The resulting O_B -> M[1]
is a class in H^1(B,M). Functoriality of derived cup and global sections
identifies it with the bracket of the images of u,v followed by R.
This proves (1), including on the diagonal: the bracket there is twice
the Yoneda square, and no polarization factor has been removed.

At a stalk the source Sym^2 M is a finite free module, so Ext^1 from
it is zero. Globally, local freeness instead identifies the Ext group
with H^1(B,(Sym^2 M)^vee tensor M); this follows by applying global
sections to the derived sheaf Hom, which is the stated vector bundle
in degree zero. The vanishing of the sheaf higher Exts does not kill
this H^1. No value or nonvanishing of that H^1 is asserted here.
In particular the sheaf-Hom argument used for fj=b[-1] in L116 has
equal shifts and does not apply to kappa, whose shifts differ by one.

**Full global pairing and signs.** By (1) and L165's actual adjoint
identity, the left side of (2) is Q([j_1u,j_1v],iw). Locally free V
has a Dolbeault resolution; choose closed representatives of these
actual cohomology classes. They need not have pure fibre degree.
The definition of the graded bracket gives the first trace expression
in (2), since (-1)^(1*1)=-1. In its second term, moving beta from
the first position to the last crosses degrees 1+2 and yields

    Tr_X(beta alpha gamma) = -Tr_X(alpha gamma beta).

Thus the sum is Tr_X(alpha(beta gamma-gamma beta)), precisely the
second expression of (2), since (-1)^(1*2)=+1. This also directly
checks the cited invariant identity at these degrees. Canonical forms
have even degrees and introduce no extra interchange sign. Trace and
integration kill exact changes of representatives by differential
compatibility (equivalently Stokes on compact X with closed volume
form), so the expression depends only on the actual cohomology classes.

All displayed products have total Dolbeault degree four after the
outer pairing. The bracket [beta,gamma] has degree three, not a degree
that forces it to vanish on X. Tr(V)=0 does not say that the trace
of a product of three V-valued forms is zero. Nor does rj=id say
anything about r mu (j tensor j). Moving the bracket back by cyclicity
recovers the same expression, without a negative of itself. Hence this
calculation gives no cancellation.

Nondegeneracy of S makes evaluation against every w in the full K
sufficient to detect kappa(u v), but supplies none of those values.
Neither the tangent summand alone nor an arbitrary matrix pairing can
replace that full test. Fibrewise degree arguments cannot eliminate
the global Ext^1 operation just identified. If t=0 its section domain
is zero. If Z is empty, W disappears but K and the Ext^1 test remain;
there is no inferred vanishing in that case. The stated stopping test
is met only in its unresolved-operation branch: save the actual
operation and park this cyclicity-only route. Actual point-section
pairings, integrability, F existence and global realization are still
independent unresolved issues. A separate critical audit of this
reduction has not been performed.

## Mathlib

Full matching coverage for the actual global complementary Yoneda
operation is not checked; no absence is claimed. The general derived
cup, duality and cyclic-trace sources are cited precisely above.
The shift and graded-sign specialization is informal, not machine
verified. No numerical calculation or formal certificate is used.
