# 2026-10-03 — Saved square-twist calculation and map audit

This preserves the initial reasoning on the exact SPECIALIZE target in
[the prior assessment](literature/2026-10-02-cubic-rm-polarization-comparison.md).
It is an informal working note, not a complete Hodge-conjecture candidate.
The pending arguments below were completed in
[L037](../lemmas/L037-square-twist-kuga-satake-comparison.md), which is the
canonical full proof, including the alternative tensor convention.

In E=Q[U]/(U^3+U^2-2U-1), put b=U^2+U-1. Exact polynomial
reduction gives b^2=2 id+U and b^{-1}=U^2-1. Therefore the
specified a is a nonzero square and totally positive. The known
square-twist criterion applies: b:(T,q_a) to (T,q) is a Hodge
isometry, with compatible Kuga--Satake embeddings satisfying
I kappa_a=kappa b for an algebraic abelian cohomology isomorphism I.

The return-map audit must use the actual cup product q on S.
For an ample class on B=A^2, define the geometric q-adjoint
d of kappa using transpose and forward Lefschetz. The proposed
normalization is s=d kappa and r=s^{-1}d, retaining s as a
Hodge endomorphism rather than assuming it scalar. If kappa
is algebraic and s is nonzero, its inverse is an algebraic
polynomial in s on T, so r is algebraic. The comparison then
has r I kappa_a=b. A separate proof of the nonzero pairing and
the equivalence of modified-cycle algebraicity with algebraicity
of U is needed before treating this as a completed result.

The plausible downstream use is realization of U=b^2-2 id.
The discriminating test is whether kappa_a has any independent
cycle supply. Algebraicity of an abelian isogeny alone supplies
no map from S to B_a. The ordinary kappa remains unresolved too.
The achieved family span and the missing RM direction are unchanged.
