# Approved angular-observable attempt — working checkpoint

STEP_ID: 2026-11-06-nongraph-angular-observable-separation

The invocation-start SPECIALIZE assessment is
`literature/2026-11-06-nongraph-angular-observable-test.md`.
Only its single fixed observable is being tested. Inputs are L855/L856,
with the inherited actual G/full form of L775/L847. Preserve the fixed
pair, finite n>=1, original product, inverse chart B and angle branches.
The requested filling is a compact oriented embedded annulus with the
exact inward collar portions, real nonnegative omega and strictly
positive original angular two-form. Its w projection is unrestricted.

Provisional calculation, not yet an audited result: put
a=(1,0)T^(-1), f=a_1 log((zeta+w)/zeta)+a_2 log(h(w,v)/eta).
Then ell=Im(f) and f(w,Aw)=iw+O(w^2). On the original product use
K(w,z)=integral_eta^z H(w,t) f(w,t) dt and alpha=-w^n K dw;
the intended identity is d alpha=f omega on all B. On a surface where
omega is real, Im(d alpha) pulls back to ell omega. Thus this does not
assume that a surface parameter is holomorphic or that ell omega is
closed on the ambient four-manifold.

For the boundary calculation set u=v-Aw. The primitive expansion about
v=Aw has linear term f(w,Aw)u and remainder O(|u|^2), after subtracting
a holomorphic-in-w term with zero circle integral. On both circles
u=O(r^(n+1)); hence the two integrated remainder scales are
O(r^(2n+4)) and O(r^(3n+3)), with the latter no larger for n>=1.
The leading boundary period should be i M_1, so its imaginary part
divided by M_0 should be 2r+O(r^2). Boundary values of ell should be
Re(w)+O(r^2), so the boundary maximum is at most r+O(r^2).

Remaining checks before claiming a result: primitive and logarithms
throughout unchanged B via the original product; exact induced boundary
signs; explicit fixed constants in the two remainder bounds; compact
extrema on a hypothetical surface even at zeros of omega/w and folds of
w. A strict separation would exclude only these synthetic collars in
this angular-projection class. It supplies no actual exterior data,
global homology/exchange or Xi signs. Stop if any of these checks fails;
do not escalate to higher moments. No mathematical scripts are needed.

Completion: the provisional reasoning above is preserved. The completed
proof and fixed-constant error bounds are now canonical in
[L857](../lemmas/L857-angular-first-moment-excludes-nongraph-annular-fillings.md).
It gives a strict violation of at least r M_0/2 for all sufficiently
small r, including n=1, with primitives on all of unchanged B.
The first independent conceptual audit remains pending. No higher
observable, numerical certificate or global sign claim was introduced.
