# Boundary-contained degree-three support action — working record

## Scope and test

Reuse the unchanged ready SPECIALIZE assessment in
[the prior review](literature/2026-10-03-cubic-rm-boundary-support-action.md).
The main gap is an independent non-scalar cubic-RM correspondence,
with a transverse use still required; the universal Hodge target
is farther away. This step only screens actual stable maps whose
entire weighted-support image is in the collision locus.

The intermediate target is regular factorization of that support
map through the (2,1)-stratum normalization, followed by the
actual positive weighted-action calculation. The discriminating
test is coverage of nondominant images and triple collisions,
with no extra leading-cycle term from punctual lift data.
A scalar bound stops this particular supply. Failure of one
of those checks keeps the mechanism open, rather than refuting
the Hodge conjecture.

L038's fixed-point recipe is already stopped. L039 supplies
the actual family quotient and weighted action; L040 supplies
its all-stratum identification with Hilbert--Chow. Neither
states the proposed bound. The totally real isometry input
is already cited for general K3 surfaces in foundations/07;
L004's quartic hypothesis should not be silently dropped.

## Checkpoint before completing the argument

The imported normalization is nu:S x S -> Delta, (x,y) -> 2x+y,
where Delta is the reduced collision locus. Each geometric
cycle in Delta has exactly one such ordered pair, including
3x. Normality of S alone does not authorize a nondominant
normalization lift. Examine the finite pullback, its dominant
reduced component, and its degree over S before invoking the
finite-birational theorem.

After a regular lift (a,b), the proposed leading cycle is
2 Gamma_a + Gamma_b. Check generic multiplicities separately
for a != b and a=b. Finiteness over the parameter surface
must exclude dimension-two contributions over smaller subsets.
Then compare the cycle with L039's Mukai sign, rather than
using only a pointwise CH_0 identity.

For each regular self-map, verify preservation of T by the
projection formula. A nondominant map kills the holomorphic
two-form; a dominant map is an automorphism by the imported
regular-map result. Only after these checks apply the cited
irreducibility and totally real isometry restrictions.

No completed scalarity result or new lemma is claimed at this
checkpoint. The saved scalar supply has one transcendental
direction against three required by E. Span 21 on the Dickson
family and three attained RM directions against four required
are unchanged.

## Completed test

The full argument is [L041](../lemmas/L041-boundary-contained-sheaf-maps-are-scalar.md).
The finite pullback has a reduced generic fibre Spec C(S):
its geometric fibre has one point and finite extensions are
separable in characteristic zero. Its unique dominant reduced
component is finite and birational over S, hence is S. This
justifies descent without assuming dominance onto the stratum.
It treats all smaller images and the entirely triple case.

The two generic-length cases give the actual leading cycle
2 Gamma_a + Gamma_b. Finite support excludes any additional
dimension-two component over a proper subset. Thus L039's
positive weighted action is exactly 2a^*+b^*. The projection
formula verifies preservation of T; the cited holomorphic-line
detection and regular-self-map results give component actions
zero or +id or -id. The action is scalar, with coefficient
between -3 and 3, without claiming every coefficient has a
stable lift. Punctual lift data contributes no extra action.

The discriminating test passes and stops the boundary-contained
supply: its span is at most one against three required by E.
This is an informative negative reproduction of known tools,
not progress beyond the checked literature or a Hodge disproof.
No non-scalar class or transverse surface is supplied. The
general primitive fourfold and higher-dimensional gaps remain.
The proposed generically distinct dihedral-plus-diagonal recipe
is only named for a separate source review; it is not tested here.
