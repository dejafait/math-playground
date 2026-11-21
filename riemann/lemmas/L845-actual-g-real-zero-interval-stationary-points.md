# Lemma 845: actual-G stationary points on separated real-zero intervals

## Hypotheses

Use the actual completion of L018, so Xi(t)=xi(1/2+it) is entire,
even and real on the real axis. Use L775's entire function

\[
 G(z)=\frac18\xi\left(\frac12+\frac{\sqrt z}{2}\right)
\]

and its unique finite positive radius R_k satisfying
R_k G'(R_k)/G(R_k)=k, with G(R_k)>0. The square-root notation defines
an entire function by evenness. Fix any integer r>=2 and put k=r-1.
Keep precisely the angular density of L844:

\[
 H_r(\boldsymbol\zeta)=
 \prod_{j=1}^{r}\left[e^{-ik\zeta_j}
       \frac{G(R_ke^{i\zeta_j})}{G(R_k)}\right]
 \prod_{i<j}4\sin^2\frac{\zeta_i-\zeta_j}{2}.
 \tag{1}
\]

Stationarity means that all r complex partial derivatives of this
specified function vanish and H_r is nonzero. No RH, simplicity of
all real zeros, Hessian condition or coefficient-minor sign is assumed.

## Conclusion

For every r>=2 there are r compact intervals I_j=[a_j,b_j] with
0<a_1<b_1<a_2<b_2<...<a_r<b_r, each bounded by consecutive distinct
positive real zeros of Xi, and points t_j in (a_j,b_j), such that

\[
 z_j=-4t_j^2,\qquad
 \zeta_j=\pi-i\log\frac{4t_j^2}{R_k}
 \tag{2}
\]

give a nonzero stationary point of (1). In fact the construction works
for any r intervals satisfying those conditions. Endpoints may have
arbitrary multiplicities.

This is a specialization of the cited real-zero and extremum theorems,
not a new general variational theorem. No uniqueness, Hessian
nonsingularity, effective location, uniform spacing, contour
participation, saddle contribution, signed remainder or mixed-minor
positivity is concluded. These points have Re(zeta_j)=pi and are outside
the collar excluded in L844. L775's absolute-complement obstruction and
the automatic-contour source stop remain intact. The separate audit
below accepts this scoped construction; it is not an RH candidate.

## Proof

### Imported inputs and selection of intervals

J. B. Conrey, *More than two fifths of the zeros of the Riemann zeta
function are on the critical line*, J. reine angew. Math. **399**
(1989), 1–26,
[Theorem 1, p.4, with count (11), p.3](https://www.maths.dur.ac.uk/users/herbert.gangl/morethan2_5.PDF#page=4),
unconditionally supplies infinitely many distinct simple zeros on the
critical line with positive ordinate. Only infinitely many distinct
positive ordinates are used. By L018's multiplicity-preserving zero
correspondence, Xi therefore has infinitely many distinct positive real
zeros. This does not say that every real zero is simple or that every
zero is real. Conrey's theorem is imported, not reproved.

Xi is not identically zero: L018 gives Xi(i/2)=xi(0)=1/2. Its zeros
are isolated by the identity/isolated-zero theorem, Jiří Lebl,
*Guide to Cultivating Complex Analysis*, v1.10, 5 November 2026,
[Theorem 2.4.7, p.49](https://www.jirka.org/ca/ca.pdf#page=49).
Consequently every compact real interval contains only finitely many
zeros: an infinite subset would have an accumulation point in the
domain C. In particular positive zeros cannot accumulate at zero.
They can thus be listed, without multiplicity, in increasing order
gamma_1<gamma_2<..., tending to infinity. Choose

\[
 I_j=[\gamma_{2j-1},\gamma_{2j}],\qquad 1\le j\le r.
 \tag{3}
\]

The endpoints in each pair are consecutive distinct positive real
zeros. Adjacent chosen intervals have strictly positive separation
gamma_(2j+1)-gamma_(2j). This proves existence of the prescribed boxes
for every finite r; it uses no height estimate or simplicity assumption.
The argument below applies equally to any ordered intervals with the
stated properties.

### Exact real restriction and all boundary faces

Put m=r(r-1)/2. On (C\{0})^r define the holomorphic function

\[
 F_r(\mathbf z)=(-1)^m\frac{R_k^{kr}}{G(R_k)^r}
     \prod_{i<j}(z_i-z_j)^2
     \prod_j G(z_j)z_j^{-(k+r-1)}.
 \tag{4}
\]

L844 (4), equivalently the exact identity
4 sin^2((zeta_i-zeta_j)/2)=-(z_i-z_j)^2/(z_i z_j), states that
H_r(zeta)=F_r(R_k exp(i zeta_1),...,R_k exp(i zeta_r)).
Integer k ensures e^(-ik zeta_j)=(R_k/z_j)^k. No integration measure
has been changed, and no Jacobian is multiplied into (4).

For real t, evenness gives G(-4t^2)=Xi(t)/8, with no branch ambiguity.
Since k+r-1=2(r-1), direct substitution in (4) gives

\[
 f_r(\mathbf t):=F_r(-4t_1^2,...,-4t_r^2)
 =(-1)^m C_r
   \frac{\displaystyle\prod_j\Xi(t_j)
          \prod_{i<j}(t_i^2-t_j^2)^2}
        {\displaystyle\prod_j t_j^{4(r-1)}},
 \qquad
 C_r=\frac{R_k^{r(r-1)}}{8^r4^{r(r-1)}G(R_k)^r}>0.
 \tag{5}
\]

For the constant, each squared difference contributes 16, each G
contributes 1/8, and the denominators together contribute
4^(-2r(r-1)); since 16^m=4^(r(r-1)), the net power is
4^(-r(r-1)). In particular no denominator exponent or normalization
has been dropped.

Let Q=I_1 x ... x I_r. All t_j are bounded below by a positive
number, so (5) is real and continuous on Q and differentiable on an
open real neighborhood of Q. On every boundary face at least one
t_j is an endpoint and Xi(t_j)=0. All other factors stay finite, so
f_r=0 on the entire boundary, including intersections of faces.

In the interior, no Xi(t_j) vanishes because the endpoints are
consecutive real zeros. Separation and positivity of the intervals
imply t_i^2!=t_j^2. Thus every interior value of f_r is nonzero.
Moreover Xi has one constant sign on each (a_j,b_j), by continuity
and the intermediate value theorem. Equation (5) therefore has one
constant sign epsilon in {1,-1} throughout the interior. The function
h=epsilon f_r is positive there and zero on the boundary. This is a
real sign adjustment by a constant; no modulus is differentiated.

### Interior extremum and transfer to every complex partial

The real continuous function h attains a maximum on the nonempty
compact box Q by Lebl, *Basic Analysis I*, v6.3, 15 May 2026,
[Theorem 7.5.6, p.290](https://www.jirka.org/ra/realanal.pdf#page=290).
The value at the tuple of interval midpoints is strictly positive.
Thus a maximizer t* has h(t*)>0 and cannot lie on the boundary, where
h=0. In particular every t_j* is in (a_j,b_j) and f_r(t*)!=0.

Fix j and hold the other coordinates equal to their values at t*.
The resulting differentiable function of t_j has an interior local
maximum at t_j*. Fermat's theorem in Lebl, *Basic Analysis I*,
[Lemma 4.2.2, pp.162–163](https://www.jirka.org/ra/realanal.pdf#page=162),
therefore gives partial_(t_j) h(t*)=0. Since epsilon is a nonzero
constant, partial_(t_j) f_r(t*)=0 for every j.

For completeness the coordinate domains meet the analytic hypotheses:
F_r is holomorphic on (C\{0})^r, and the map w_j -> -4w_j^2 is
holomorphic and nonzero on a sufficiently small complex neighborhood
of each positive t_j*. For a holomorphic function, its derivative
along the real direction equals its complex derivative, as stated in
Lebl, *Guide to Cultivating Complex Analysis*,
[Proposition 2.1.4, p.28](https://www.jirka.org/ca/ca.pdf#page=28).
Applying this in the jth coordinate and the chain rule (Lebl,
*Basic Analysis II*, v6.3,
[Theorem 8.3.7, p.38](https://www.jirka.org/ra/realanal2.pdf#page=38))
gives exactly

\[
 0=\partial_{t_j} f_r(\mathbf t^*)
   =-8t_j^*\,\partial_{z_j}F_r(\mathbf z^*),
 \qquad z_j^*=-4(t_j^*)^2.
 \tag{6}
\]

Every multiplier -8t_j* is nonzero, so all complex partials of F_r
vanish. The lifts in (2) satisfy R_k exp(i zeta_j*)=z_j*, because
i zeta_j*=i pi+log(4(t_j*)^2/R_k). A final chain-rule application to
the exact identity following (4) gives

\[
 \partial_{\zeta_j}H_r(\boldsymbol\zeta^*)
   =i z_j^*\partial_{z_j}F_r(\mathbf z^*)=0,
 \qquad
 H_r(\boldsymbol\zeta^*)=f_r(\mathbf t^*)\ne0.
 \tag{7}
\]

This proves the required complex stationarity of the original density
for every r>=2. Nothing in this argument controls a second derivative
or constructs an integration cycle. No sum, limit or contour is
interchanged, and off-line zeros are permitted throughout.

### Independent audit, 6 November 2026

The invocation-start SPECIALIZE coverage in
`drafts/literature/2026-11-06-actual-g-real-zero-interval-audit.md`
was reused. This audit accepts the construction as a local
specialization of the cited inputs; no strengthened conclusion or
progress beyond those sources is claimed.

For the zero selection, Conrey supplies a simple subset with infinitely
many distinct positive ordinates. The enumeration in (3) is instead
of **all** distinct positive real Xi zeros. Since Xi is nonzero and
entire, its zeros have no finite accumulation point, including at
zero. Therefore this enumeration has a first element, each element
has a successor, and the enumeration is unbounded. In particular
there are no omitted real zeros inside each chosen interval. The
strict gap between gamma_(2j) and gamma_(2j+1) guarantees separation
of the closed intervals themselves. The proof never infers that
their endpoints belong to Conrey's simple subset. L018 supplies the
completion correspondence and Xi(i/2)=1/2 used for nonidentity.

Independently checking the exact restriction, each of the m pairs
in (4) contributes 16(t_i^2-t_j^2)^2. For each coordinate,
z_j^(-(k+r-1))=(-4t_j^2)^(-2(r-1)) is positive and contributes
4^(-2(r-1))t_j^(-4(r-1)). The r G factors contribute 8^(-r).
Thus the full constant is

\[
 (-1)^m\frac{R_k^{r(r-1)}}{G(R_k)^r}
       16^m\,8^{-r}\,4^{-2r(r-1)}=(-1)^m C_r,
\]

as asserted in (5). In particular the parity of m, which can change
with r, is retained. R_k and G(R_k) are finite and strictly positive
by L775's scalar-radius proof. No sector asymptotic or growing-r
estimate from L844 is needed for this step; only its exact coordinate
identity is used.

Every t_j stays in a positive compact interval. Hence denominator
factors cannot diverge, even at intersections of boundary faces.
Every boundary point has at least one vanishing Xi factor, so all
faces and intersections have value zero. Every interior Xi factor
is real and nonzero, all squared differences are positive, and all
denominators are positive. The sign epsilon therefore is one constant
on the entire product interior. Multiplication by epsilon is a real
constant operation before applying Fermat, not taking a modulus.
The midpoint tuple has strictly positive h, whereas the boundary
has h=0. Compact attainment consequently gives an interior maximum
for every finite r, with no spacing lower bound or onset required.

Finally hold the other r-1 coordinates fixed. Holomorphy of F_r in
that one variable on C minus zero and the map w -> -4w^2 imply that
the derivative of the real restriction equals its complex derivative
times -8t_j. This uses the cited one-variable complex derivative fact
and the finite-dimensional chain rule on a neighborhood avoiding
zero, not a claim that an arbitrary real modulus extremum is complex
stationarity. Each -8t_j is nonzero. The lift has
exp(i[pi-i log(4t_j^2/R_k)])=-4t_j^2/R_k, and its angular derivative
multiplier i z_j is also nonzero. Thus each of the r original complex
partials vanishes at the same nonzero point. No real direction is
substituted for a missing complex derivative condition.

The direct mathematical input IDs remain L018/L775/L844; their DAG
row needs no change. This audit supplies no Hessian nonsingularity,
contour participation, Jacobian phase, signed-error estimate or minor
positivity. L775's complement stop, L844's collar exclusion and the
automatic-contour source stop retain their scopes. Mathlib matching
and supporting coverage remain unchecked.

## Mathlib

Full matching coverage and supporting theorem names were not checked.
Availability is unknown, not asserted absent. The proof uses the exact
external theorems cited above and the local actual-G interface; no
formal verification or numerical certificate is claimed.
