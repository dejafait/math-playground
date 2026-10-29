# Distinct-line cubic localization attempt — 2026-10-26

Approved target: Determine the N^2 leading asymptotic of L280(20)'s complete cubic response on the same relative box and compare it with L285(4).

Use the unchanged prior EXPLORE assessment
`drafts/literature/2026-10-26-complete-cubic-quadratic-asymptotic.md`.
The main gap is the interacting continuum theory with nonzero sector
and finite positive mass. This step tests the last cubic group
D_{3,N}=B(T,T;G_-,G_+,G)/2. Its controlled leading coefficient could
complete the comparison with L290(3); no cancellation is presumed.
The separate audits of L286–L290, subleading control, uniform higher
remainder and continuum/infrared construction remain open.

Local checks: L280(18)–(20), L284's separated kernel, L285's local
covariance approximation, L287–L290, and ATTEMPTS/047–049. The latter
stop generic rearrangements or inadequate global norms, not the present
Wilson-specific separated-source test. No new external theorem is used.

## Saved unfinished reasoning

For independent Gaussian fields y_-,y_+,x with covariances G_-,G_+,G
(each with three independent colors), the exact group is
one half E[T[y_-,y_+,x]^2]. Split its local tensor by the time of each
plaquette anchor into two halves. On each half the opposite source is
at fixed physical distance. A possible first test is to extend L290's
separated nuclear estimates to the complete time half, including its
spatial faces and normal links, then use G_pm<=F G in each bilinear
quadratic-polynomial estimate. This could control the whole positive
square, including pairs of vertices on opposite halves, at O(N^2).

The sharper test requires a uniform finite-range approximation of the
remaining two-line bilinear operator after the remote source is exposed.
The differentiated covariance is GC_12^*hC_12G, so L288's independent
positive-covariance splitting does not apply to its polynomial
approximation without proof. A local-entry estimate alone is insufficient.
Even a halfwise O(N^2) bound leaves the cross-half covariance and the
leading coefficient unresolved. Do not infer a limit from it.

Continue to a limit only if the complete approximation error tends to
zero after N^-2 normalization and all cross-half terms are estimated.
Otherwise preserve the proved bound and identify the exact remaining
uniform estimate; an unestimated tail is not an asymptotic result.

## Refined mechanism saved before assembly

The source-factor approximation avoids the missing positive splitting:
y_h=L^-1 C_12^* W_h xi_h, y_{h,m}=h_m(L)C_12^*W_h xi_h on the
same source noise. Set x_m=Lh_m(L)x on the original independent
G-Gaussian x. Each residual covariance is dominated by F times (or
without F for x) L288's R_{N,m}, while the retained covariances are
dominated by F times (or without F) its positive finite-range hat G.
Independence between source noise and x survives; independence between
each retained field and its residual is unnecessary.

Expand the internal-curl bilinear difference into six terms. The Schur
bound with residual edge diagonal O(M^-1), residual curl diagonal
O(M^-2), retained operator norm O(M), and curl norm O(1) gives squared
operator error O(M^-1), M=m+1. The remote half source map has squared
Hilbert–Schmidt norm O(N^2), and its half-restricted curl has squared
Hilbert–Schmidt norm O(1), by L285's full-half separated series. These
suggest a complete normalized error O(M^-1/2)+o_N(1).

For fixed m, each retained near-source field is supported within fixed
lattice distance of its source. The two half amplitudes have zero cross
expectation once N is large, because x_m has finite covariance range.
The same finite ranges permit freezing the local source weight and the
remote field. The prospective color-block row sum on directions 1,2 is
beta_m=8 integral sin(q_1)^2 lambda h_m(lambda)^4(d_1^2+d_2^2).
Its proposed limit is beta=8 integral sin(q_1)^2(d_1^2+d_2^2)/lambda^3.
Using L289's I_1=Z_0/2-1/16 and integrating the derivative of
sin(q_1)d_2^2/lambda^2 gives beta=(22Z_0-3)/6. With two halves and
the original factor 1/2, this would give (22Z_0-3)J_f/128, exactly
the required compensation. These are saved proof obligations, not a
claim that the incomplete calculation already establishes the limit.

## Completed result and limits

[L291](../lemmas/L291-cubic-distinct-line-quadratic-asymptotic.md)
contains the full proof. Whole-half Hilbert–Schmidt estimates suffice;
the initially proposed nuclear estimate is unnecessary. The complete
remote-curl error is O(N sqrt(log(eN))+log(eN)). The source-factor
approximation has normalized error O((m+1)^-1/2), uniformly in N,
without a false independence assumption for retained/residual fields.
The finite-range cross-half expectation is exactly zero at fixed m
for sufficiently fine meshes. All internal colors and the original
factor 1/2 are retained in the bulk and source-trace calculation.

The final distinct-line limit is (22Z_0-3)J_f/128. With L290(3),
this proves kappa_a=o(N^2), under the inherited input qualifications.
No logarithmic rate, uniform higher remainder, interacting lower bound
or continuum/mass construction follows. No mathematical script or new
external theorem was needed. The proof and L286–L290 still require
separate critical audits. This is local progress within the ready
target, not certified novelty or a complete-solution candidate.
