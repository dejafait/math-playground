# Signed nested-radius attempt — step 151

The invocation-start EXPLORE assessment is
`drafts/literature/2026-11-03-gevrey-inner-disk-complete-charge-scope.md`.
Its unchanged target is: Assess whether one fixed L703 profile has
Z_n^(1/2)(e)>=P_n^(1/2)-o(n), using complete L657 angular charges
inside |u|<1/2.

This is one mathematical attempt. The main gap is actual-Xi all-degree
mixed positivity. The intermediate charge could pay the missing inner
numerator contribution to logarithmic compensation; the outer annulus,
complete mean, H/support and Xi realization remain independent gaps.
All profile choices precede n. No head/path Fourier gap, residue sign,
root simplicity or effective onset is assumed.

Inputs inspected: L657's complete K,Q and divisor/integrability proof;
L666's exact family and rational continuation; L703's fixed-profile
statement and source interface; L704's full positive-point contour,
uniform spatial transfer, boundary and signed Poisson comparison.
L700/L701's statements retain their extra reflected-profile hypotheses;
L702 and the C703a ATTEMPTS record preserve their distinct stops.
The source comparison is reused, not rerun. Existing changes remain.

Bounded test: write the signed difference between a fixed inner radius
and 1/2 with complete cancelled divisors and spatial means, then test
whether a genuine annular comparison controls its missing linear term.
Continue with a quantified reduction of the deficit or an informative
same-profile obstruction. Mere monotonicity of numerator charge,
generic degree accounting, a rescaled L704 one-point bound or an
optimization of its constant does not pass the test.

Initial checkpoint: for each radius r<d, the exterior A factors of Q
have constant angular logarithmic mean. Thus the entire signed change
is the change of the complete numerator mean minus the known C_x pole
charge. Standard Jensen accounts for this exactly, but its nonnegative
numerator increment has no automatic lower bound matching the pole
increment. The attempted comparison must supply that extra information;
the identity itself is not progress.

## Concrete comparison under test

Test the anchor comparison K_0=Q*T_M(x*zeta/R)/R on the full
circles r0=1/4 and r1=1/2. If the remainder were strictly smaller
there for the required spatial slices, Rouche could compare complete
counts; radial integration would still be needed for weighted charge.
The comparison is a proposed sufficient mechanism, not an assumption.

At u=-r, write W_r(y)=W_(x+i*y)(-r). Its limiting logarithmic
modulus Phi_r(y) has derivative

    integral_0^1 [y/((d-U*r/t)^2+y^2)
                         -y/((d-t*r)^2+y^2)]dt.

For r=1/4 and 1/2, a symmetric subinterval in v=d-U*r/t gives
Phi'_r(y)>1/6 for 0<y<=Y=9/20. Thus both endpoint bands grow
exponentially at these negative-real boundary points. The actual
Gevrey shifts tend to zero at the endpoints; no approximation to the
infinite Picard solution is needed. A discrete endpoint expansion
should retain BOTH conjugate endpoint amplitudes and all spatial
moments. Their limiting spatial resolvents are linearly independent,
so cancellation of a scalar value cannot erase the whole polynomial.

The intended discriminating conclusion is failure of uniform anchor
Rouche dominance for this SAME fixed profile, with a full spatial
logarithmic lower bound. This would stop only that sufficient annular
comparison. It would not refute the charge target, prove a deficit,
or supply a lower angular mean. The detailed endpoint domination,
uniform errors and spatial logarithmic step are being checked next.

## Completion

The full proof is canonical in
`lemmas/L705-inner-annulus-anchor-comparison-obstruction.md`.
For both proposed radii its actual signed nonanchor sum has full
spatial logarithmic mean n*Phi_r(9/20)+O(log n), with Phi_r(9/20)>3/40.
The anchor mean is -log R. This disproves uniform anchor dominance
on each comparison contour for the same actual fixed profile. It
does not prove an actual charge deficit or improve L704's payment.

The exact endpoint coordinates, uniform logarithmic Riemann errors,
separate positive/negative tails, phase cancellation and spatial
Poisson bound are written out. No script or numerical Picard profile
is an input. The rational derivative margins exceed 1/6 explicitly.
The negative outcome is a local specialization, classified REPRODUCTION;
it remains unaudited. The new audit nomination is REVIEW_REQUIRED,
with source approval deferred to a separate turn. Existing work,
the aggregate target and earlier scoped failures are preserved.
