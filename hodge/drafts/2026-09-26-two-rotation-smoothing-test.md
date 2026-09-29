# Two-rotation union: saved calculation

## Gap, target and continuation test

The saved SPECIALIZE assessment in `drafts/literature/2026-09-26-current-target.md` applies unchanged. The target is the embedded first-order smoothing test for the reduced union of the images of (g_0,g_0 sigma) and (g_0,g_0 sigma^2), in the same deformation of S in both factors. A fourth RM lifting direction could supply a new representative of a non-scalar RM class; higher-order lifting, algebraization and the general Hodge conjecture would still be open. The required kernel dimension is four, against three attained by the earlier representatives. Stop this union if every lift recovers a lift of C; continue only for an actual transverse lift or a concrete surviving cancellation channel.

The whole overview and DAG, the prior assessment, and the relevant local/global correspondence proofs have been read. The earlier diagonal, fibre-component and sheaf failures are preserved. They do not compute this union. The existing uncommitted literature notes and histories are retained.

## Reasoning saved before the full calculation

Put theta_j=zeta^j+zeta^(-j). On the finite base chart, the j-th image has conic equation Q_j=t^2+s^2-theta_j*t*s-a*(4-theta_j^2)=0, with the same elliptic coordinates in both factors. For j=1,2, its intersection pulls back on the first normalization to v^2=a*zeta^(-3) or v^2=a*zeta. These give four complete smooth elliptic fibres under the very-general assumptions. Over infinity the images are the graphs of f,f^(-1) and f^2,f^(-2); their only mutual intersections should be the three fixed points already computed in L008.

A possible global obstruction mechanism uses the third conic Q_3 only as a test locus, without adding it to the representative. At each of the two critical values of P_a there are three distinct critical points. The three unordered pairs among them appear as intersections of different Q_j's. The union includes the Q_1/Q_2 pair but has a single smooth graph branch at the Q_1/Q_3 and Q_2/Q_3 pairs. A lifted single branch is locally a graph of an isomorphism of smooth elliptic fibres, so the first variations of their j-invariants must agree at these critical points. If those two equalities connect all three points, they force equality also on the Q_1/Q_2 pair.

Near a double curve, J_0(t)-J_0(s) is a unit times the product of the two transverse base-branch equations. A lifted union must lie in J_A(t)=J_A(s): prove this first on complete smooth fibres where its four sheets separate, then use flatness and reducedness to extend the identity. The local smoothing coefficient is therefore proportional to the difference of the first variations of J at the two critical points. The preceding equalities would force it to vanish. This needs a proof covering whole fibres and all allowed embedded lifts, not an assumption that a lift preserves the original cover construction.

If the coefficients vanish, factor the first-order node equation to recover both component lifts away from the three points at infinity. Then L008's Hartogs property for N_C extends the C lift over those points; no flatness assertion for a residual ideal at a four-branch point is needed. The reverse inclusion must separately check flatness of the union along the Dickson family, including the four-plane arrangements at infinity.

These were proof obligations at the initial checkpoint. The correspondence action also needs its multiplicity-one check: the second image should act as U^2-2 id, so the reduced union acts as U^2+U-2 id, rather than U+U^2.

## Global compatibility calculation saved

Choose c with c^2=a. For each sign e, write p_k=e*c*theta_k (k=1,2,3); all three are simple critical points of P_a with value 2*e*c^7. The pairs {1,2}, {1,3}, {2,3} belong respectively to conic pairs {Q_1,Q_3}, {Q_2,Q_3}, {Q_1,Q_2}. Thus the first two pairs are smooth loci of the tested union. Its double curves are the ordered pairs (p_2,p_3),(p_3,p_2) for both signs.

Write J_0=R composed with P_a and J_A=J_0+epsilon*dJ for the j-map of the lifted NS-fixed elliptic fibration. Require R'(2*e*c^7) nonzero, an open condition at very general parameters. The identity J_A(t)=J_A(s) on an arbitrary embedded lift follows on the dense open where the four sheets of its finite first projection are disjoint graphs. Each graph maps complete elliptic fibres to fibres, since a holomorphic function on a complete connected fibre is constant, including the epsilon coefficient. The maps reduce to isomorphisms, so their j-invariants agree. A-flatness and reducedness of Y extend the identity from that dense open.

At a smooth point over either of the first two critical pairs, a section of the smooth first-order lift exists. Since J_0' vanishes at both base values, evaluation forces dJ(p_1)=dJ(p_2) and dJ(p_1)=dJ(p_3). At a double curve set r=Q_1,s_0=Q_2. Then J_0(t)-J_0(s)=h*r*s_0 with h(p_2,p_3)=R'(2*e*c^7)*(p_2-p_3)*Q_3(p_2,p_3) nonzero. In a lifted ideal (z-epsilon*alpha,r*s_0-epsilon*beta), its smoothing residue is

    beta|D = -(dJ(p_2)-dJ(p_3))/h(p_2,p_3) = 0.

The reversed ordered pair has the same normalized residue because both numerator and h change sign. Thus the four local smoothing lines have zero residues for every global embedded lift. When beta|D=0, write beta=r*b+s_0*a and factor the second equation as (r-epsilon*a)*(s_0-epsilon*b). The component lifts glue uniquely off infinity; L008 extends the resulting lift of C across the three isolated points. This gives the necessary inclusion in V_D. The reverse inclusion uses constant node models along the four finite curves and relative finite-group linearization of the four graph planes at infinity.

The written lemma must retain these arguments, check the finite incidence identities exactly, and state that the global compatibility calculation is a specialization beyond the matches established by the prior bounded literature search, not certified originality. Schuett--Shioda, *Elliptic Surfaces*, section 2.6 and Theorem 2.4, p. 5, were read at https://arxiv.org/pdf/0907.0298#page=5 to check the supporting j-invariant formula and invariance. The same short-Weierstrass scaling proof works over the dual numbers. No converse from equal j-invariants to an isomorphism is used.

## Mathlib

Coverage: **not checked**. The existing assessment supplies the named embedded and double-crossing theory; its full-union calculation remains the target here.

## Completed result

[L014](../lemmas/L014-two-rotation-union-retains-cubic-obstruction.md) completes the saved calculation and both kernel inclusions. All four smoothing residues vanish for every embedded lift; recovery of C includes the isolated points at infinity. The kernel has dimension three, short of four required. The step is NEGATIVE for this representative, with no claimed resolution or extension of the known cycle span. The exact algebra is checked by scripts/cubic-deformation/check_two_rotation_union.py; the global geometric arguments are in the lemma.
