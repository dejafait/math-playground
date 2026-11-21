# Centered theta-power derivative — working attempt 427

This is unfinished reasoning for the single target in assessment426,
not an established sign or a new lemma. The supplied gate approves a
mathematical attempt now; no new source review or mathematical script
is being run. Prior work and the numerical-backend stop are preserved.

Main gap: actual-Xi all-degree positivity L030-L032/C032a, with forcing
and L984(H) unpaid. Intermediate target: G_w>0 on
[1,3/2] x [40,45]. A positive bound would pay only a parameter factor
in a prospective decreasing-w collision argument. The test succeeds
only with a uniform positive margin or a rigorously nonpositive value;
otherwise retain the signed remainder and park unrefined repetition.

Inputs: L018/L019 for normalization, and Lagarias--Rains,
*On a Two-Variable Zeta Function for Number Fields*,
arXiv:math/0104176v5, Theorem 2.1, equation (2.9), pp. 8--9;
Theorem 4.4 and Lemmas 4.5--4.7, pp. 21--24.
https://arxiv.org/pdf/math/0104176v5
The entire-family theorem and source estimates are imported, not
reproved. Assessment425 contains the prior primary-source inspection
and the relevant heat/affine failures. No cross-notebook input.

Let T(x)=theta(exp(2x)), B(x)=log T(x), Q=t^2+w^2/4 and
H(w,x)=exp(wx/2)(T(x)^w-1)/w, for x>=0. Direct substitution in
(2.9), including BOTH rational terms and the completion, gives

    G(w,t)=1/2-Q integral_0^infinity H(w,x) cos(tx) dx.

The working centered derivative is therefore

    G_w=-integral_0^infinity [(w/2)H+Q H_w] cos(tx) dx,
    H_w=exp(wx/2)[x(T^w-1)/(2w)
                       +(w B T^w-(T^w-1))/w^2].

This records the moving center and the logarithm. H and H_w are
positive on x>=0 (the latter also at x=0), but their cosine transforms
are unsigned. Positivity is not being asserted for G_w.

Planned bounded analytic comparison: remove the rational cancellation
by integrating twice and inspect the resulting centered kernel and
its endpoint terms. Establish explicit tail domination before any
signed inference. No root search, numerical sign or quadrature is
authorized by this attempt's scope. The sign, event curvature,
event existence/nondegeneracy, all heights and transport remain open.

Full matching Mathlib coverage is unchecked and unknown.

## Completion of the bounded attempt

The supporting identities and all effective estimates are now canonical
in [C999f](../lemmas/C999f-centered-theta-power-derivative-endpoint-comparison.md).
The original unfinished notes above are retained as the checkpoint,
not a second proof. No mathematical script or numerical sign was used.

The remaining finite quantity is

    J(w,t)=integral_0^2 F(w,t,x) cos(tx) dx.

C999f gives G_w=-J+E, |E|<10^(-61), uniformly on the original box.
A uniform J<=-delta with delta>10^(-61) would pay a positive margin.
A single rigorously bounded J>=10^(-61) would suffice for a
nonpositive value. Neither estimate was obtained. The full unsigned
enclosure is only (-68,68).

Removing the rational cancellation produces an even smooth kernel M
with M(w,0)<-1/40. This is a kernel value, not a transform sign.
Every endpoint term in any finite even-order integration by parts
vanishes. The remaining absolute remainder gives no signed margin,
irrespective of its size. Thus the specific endpoint/absolute-remainder
comparison is parked. The approved sign statement itself remains open.

Outcome: EXPLORATION, one mathematical attempt; no RH advance or
certified failure of G_w>0. A future contour-displaced signed comparison
is a different mechanism requiring source review, including the
previously recorded normalization qualification. No contour is moved
or approved in this turn.
