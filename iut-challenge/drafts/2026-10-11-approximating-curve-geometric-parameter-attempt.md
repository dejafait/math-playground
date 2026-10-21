# Approximating curve geometric parameter — working attempt

Approved target: determine whether strengthening L046's fixed precision
retains split multiplicative reduction over Q_3 and v_3(q_0)=30,
alongside L045–L047. Coverage is the pre-existing SPECIALIZE assessment
`drafts/literature/2026-10-11-approximating-curve-geometric-tate-parameter.md`.

Essential inputs: L044's f=x^3+x^2/4-b_2(q)x-b_3(q), q=3^30,
and L046's arbitrary fixed sufficient precision; downstream apply
L045 and L047 to the same reselected curve, retaining Omega,H,N.
The main gap remains original finite B>=A.

Working calculation to complete: choose M>=max(M_tors,31).
The integral invariant polynomials preserve Delta modulo 3^M;
v_3(Delta(f))=30. For y^2=x^3+c x^2+d x+e,
c4=16c^2-48d is a unit when c=1 modulo 3. The residue equation
is y^2=x^3+x^2, with node at (0,0) and tangent cone
(y-x)(y+x). Complete the unit-c4 minimality argument and apply
the inspected Tate theorem and integral j-series. This note records
unfinished reasoning; it is not a verified lemma or complete solution.

Continue only if all model, valuation and same-curve checks pass.
No q_0=3^30, sufficient initial data, other-place conditions,
native/input/action, pilot transport or essentiality bridge is assumed.
ATTEMPTS/027 and the other-packet stops remain intact.

Completed this bounded attempt in
[L048](../lemmas/L048-approximating-curve-retains-split-tate-valuation.md).
The sufficient threshold and all declared tests pass in the written
known-method specialization. The canonical proof awaits a separate
critical audit; the working note above is preserved as the initial
unfinished checkpoint. No mathematical script was needed.
