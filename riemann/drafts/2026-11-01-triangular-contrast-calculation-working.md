# Full triangular contrast — working record

Approved target and assessment: `drafts/literature/2026-11-01-charged-block-triangular-contrast.md`, EXPLORE before invocation. Main gap: actual-Xi signs at unbounded heights. Inputs: corrected L612's finite lattice and the cited BGST triangular transform; C464c/L018 provide interpretation only. No actual-zeta pair theorem is applied to the artificial multisets.

The exact weight admits the elementary integral
`4/(4-u^2)=int_R exp(-2|v|) exp(u v) dv` for `|Re u|<2`.
Write `A=log(2T)` and `t_A(y)=A^(-1)(1-|y|/A)_+`.
The imported triangular transform gives `F(u)=int t_A(y) exp(u y)dy`.
Thus `Phi(u)=int q_A(x) exp(u x)dx`, with
`q_A=t_A * exp(-2|.|)`, a nonnegative density of mass one.
All pair differences have real part in `{0,+2/L,-2/L}`, strictly inside the convergence strip.

Finite expansion, retaining both signs and collapsed multiplicity two, gives
`Delta_T=4 int q_A(x) sinh^2(x/L) |sum_(j=0)^n exp(i j h x)|^2 dx`.
This proves reality/nonnegativity and retains every cross pair.

Potential sufficient bound: split at `B=3L/2`, which is below the first nonzero Dirichlet peak `pi L/2` and above `A`. In the central region the zero of `sinh(x/L)` cancels the zero of `sin(2x/L)` in the geometric-sum denominator, yielding an absolute bound independent of n and T. In the tails use the finite bound `|sum|<=n+1` and the exact convolution tail
`q_A(x)=exp(-2|x|) sinh^2(A)/A^2` for `|x|>=A`.
This should give `Delta_T=O(T)`, hence `o(T sqrt(log T))`, sufficient to park this contrast. This is partial reasoning until constants, endpoints and integrability are checked in the canonical proof. No numerical preview or script is needed.

Remaining tasks in this step: verify the complete bound and source applicability, write the canonical result if sound, preserve the source-scale limitation, then checkpoint with a separate audit continuation. No charge-union result, Xi realization or initial sign is established by this calculation.

Completion: the candidate bound was checked algebraically and written in canonical L613. The central contribution is at most `4 sinh^2(3/2)/sin^2(3)`. Both tails together are at most `(e^3/3)T`, since `kappa=2-2/L>3/2`, `N^2/A^2<=T^2/4`, `sinh^2 A<=T^2` and `exp(-kappa B)=e^3 T^(-3)`. Thus the full contrast is little-o of the source error scale, an informative negative diagnostic. Independent audit remains pending; no asymptotic equality or actual-Xi conclusion is claimed. The preceding working reasoning is preserved rather than substituted for the canonical proof.
