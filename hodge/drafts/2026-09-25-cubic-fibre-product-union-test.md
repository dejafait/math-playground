# 2026-09-25 — Testing the cubic support after adding a fibre product

## Gap, intermediate target, and decision test

The near-term gap is an algebraic representative of the cubic RM generator that extends in the fourth NS-fixed RM tangent direction. Test the reduced union Y = C union B with B = F_+ x F_+, using the smooth elliptic fibre and intersection calculation of L009. Its added divisor-product class acts as zero on T(S), so an algebraic extension followed by subtraction of that class could extend U. A first-order lift would only justify investigating higher-order lifting and algebraization; arbitrary K3 self-products, fourfolds, and higher codimensions would remain unresolved.

The required first-order threshold is a four-dimensional obstruction kernel on V_RM, against the three-dimensional V_D already available. The discriminating test is whether the local curve-smoothing parameter survives as a global embedded lift, or whether any lift still extracts a lift of C. No positive outcome is assumed.

## Prior evidence and preserved work

Read the shared rules and prompt, local goal and checkpoint, whole overview and DAG, existing changes, L006–L009, and the last two failed support tests. Existing changes and inactive branches are retained. Unlike the diagonal, B does not project dominantly to S, so L009's meromorphic-vector-field argument does not directly apply. Its different normal bundle and double curve are the new mechanism tested here. This is one focused lifting test, not a continuation of the stopped identity-branch calculation.

## Reasoning saved before the global test

The finite-chart formulas suggest C meets B exactly in D = Delta_{F_+}. Both projections of C are etale there. With the local involution coordinates from L009, take r = u_2-u_1, s = u_2+u_1, and z = w_2-w_1. Then I_C = (s,z), I_B = (s,r), and I_Y = (s,rz). Thus the union has a local smoothing rz = epsilon beta, but B's first-order normal displacement would have at most a simple pole along D.

For B = E x E, its normal bundle in S x S is O_B direct sum O_B. The difference map d:B -> E identifies D with d^{-1}(0); connected fibres give H^0(B,O_B(D)) = H^0(E,O_E(0)) = C by genus-one Riemann–Roch. Consequently no meromorphic normal section can have a genuine simple pole along D. The tentative conclusion is that the B branch extends to a global embedded first-order product of moving fibres, forcing the local smoothing residue to vanish. A residual-ideal calculation should then extract a flat lift of C along D; away from D, including C's three points at infinity, the union is already C.

Outstanding checks: construct a reference B_A in every NS-fixed S_A; justify the global normal section relative to it; prove scheme-theoretic containment of the extended B branch; verify flatness of the extracted residual and the reverse kernel inclusion along the Dickson family. The distinction between simple poles and higher allowed poles must be retained. No outcome is asserted at this checkpoint.

## Completed assessment

[L010](../lemmas/L010-fibre-product-union-retains-cubic-obstruction.md) completes the test. An NS-fixed deformation lifts the elliptic pencil and hence a reference B_A. Relative to this reference, any lifted B branch has normal displacement in H^0(B,N_B(D)). The elliptic difference map and genus-one Riemann–Roch make this exactly H^0(B,N_B), so the local smoothing residue vanishes. The extended branch is a product of independently moving fibres and is contained scheme-theoretically in the lifted union. Its residual has the explicit flat local ideal (s-epsilon r a_0,z-epsilon b_0). Away from B, including C's three points at infinity, the union already supplies a C lift. Conversely the Dickson family has a flat union with its moving smooth fibre product.

The kernel is therefore V_D: dimension three against the four required RM tangent dimensions. This supplies new global evidence about a representative to which the preceding diagonal argument did not apply. Outcome: NEGATIVE; exploration turns used are 0 after this informative result. The attained span remains 21 only for the existing family; no complete candidate for the universal target exists. The stopped representative is recorded in [Attempt 007](../ATTEMPTS/007-adding-fibre-product-to-cubic-support.md).

The primary rational formulation was rechecked in [Deligne, section 1, p. 2](https://www.claymath.org/wp-content/uploads/2022/06/hodge.pdf#page=2). [Stacks Project, Lemma 53.5.2, tag 0BS6](https://stacks.math.columbia.edu/tag/0BS6), was checked as support for the elliptic section count, not as a citation for the full obstruction theorem. The needed local ideal, pole, and colon identities are proved symbolically in L010; no numerical test is used as evidence for the global conclusion.

## A precisely specified untested change of mechanism

The obstruction proved here uses a reduced B branch on B minus D. A nonreduced added component removes that premise. To specify a test without asserting it works, let theta=zeta+zeta^{-1} and let R_theta be the base correspondence in P^1 x P^1 whose finite equation is

\[
t_1^2+t_2^2-\theta t_1t_2=a(4-\theta^2).
\]

It is smooth at b=(t_+,t_+). Let xi be the length-two subscheme of R_theta supported at b, with local algebra O_{R_theta,b}/m_b^2, and define B_2=(pi x pi)^{-1}(xi). Near D the base correspondence is s=0, xi has ideal (s,r^2), and C union B_2 has ideal (s,r^2 z). Its fundamental cycle is [C]+2[B], so its transcendental action is still U. This scheme is globally defined, rather than an unspecified doubled cycle. Whether its first-order obstruction vanishes is untested; the presence of multiplicity alone proves neither smoothing nor a transverse lift. No claim about allowable pole order for this nonreduced scheme has been made.

## Mathlib

Coverage of the full lifting statement: **not checked**. No Mathlib match or absence is claimed. The directly linked Stacks theorem supports only the genus-one section calculation.
