# Lemma 991: no bounded fixed-coordinate recursion for the exact endpoint filter

## Hypotheses

Use L990's exact real polynomials

    K_m(u)=[L_(m-1)^(2)(u)-1]/(m-1), m>=2,
    a_n=(K_n(n),K_(n+1)(n),K_(n+2)(n)),
    b_n=(K_n(2n),K_(n+1)(2n),K_(n+2)(2n)),
    c_n=(a_n cross b_n)/||a_n cross b_n||_1.

Fix an integer N beyond the existential cofinite-definition onset
of C990a. Define (Tx)_n=sum_(j=0)^2 c_(n,j)*x_(n+j) for n>=N.
The orientation and the two constant subtractions are exactly those
of L990. No coefficient is assumed nonzero individually, and no
singular index is removed from the definition of T.

Use the audited normalized row estimate and integer phase-orbit
equidistribution proved in L990. No RH, arithmetic realization,
Diophantine rate, effective onset or uniform normalization near
phase collisions is assumed.

## Conclusion

For each j in {0,1,2}, each M>0 and each sign s in {-1,1}, there
are arbitrarily large integer indices n>=N such that

    s*c_(n,j)>0,
    |c_(n,k(j))|>1/4,
    |c_(n,k(j))/c_(n,j)|>M,                     (1)

where k(0)=1, k(1)=0 and k(2)=1. In particular, each coordinate
has liminf absolute value zero even when restricted to its nonzero
indices. There is no uniformly bounded recursion obtained by solving
every row through any one fixed coordinate.

More specifically, at every n with c_(n,2)!=0 the exact homogeneous
row has the companion representation

    (x_(n+1),x_(n+2))^t = A_n (x_n,x_(n+1))^t,
    A_n=[[0,1],[-c_(n,0)/c_(n,2),-c_(n,1)/c_(n,2)]]. (2)

On the indices where (2) is defined, sup_(n>=N) ||A_n||_infinity
is infinite. The analogous backward representation using c_(n,0)
and middle-coordinate elimination using c_(n,1) also have unbounded
coefficient ratios. This conclusion already holds away from
degeneracy of the leading cross product.

This does not assert that an individual coefficient ever vanishes
exactly. Nor does it prove or refute

    x in E and Tx in S  ==>  x in S,

where E is the real sequences bounded by C*exp(A*n) for some finite
C,A>=0, and S is the sequences bounded by C_epsilon*exp(epsilon*n)
for every epsilon>0. No homogeneous solution, product growth rate,
inverse estimate, actual-prime bound or RH implication is obtained.

Step270, 10 November 2026: a scoped negative result under the prior
EXPLORE assessment review267. POTENTIALLY_NEW means only that the
recorded comparison did not establish coverage of this exact
operator; it is not a claim of originality. The proof below is not
yet independently critically audited.

## Proof

### Reused input and its domain

Write, exactly as in L990,

    phi_n=n*(sqrt(3)/2+pi/3)-13*pi/12,
    psi_n=n*(1+pi/2)-pi,
    v(phi)=(cos(phi),cos(phi+pi/3),cos(phi+2*pi/3)),
    w(psi)=(cos(psi),-sin(psi),-cos(psi)),
    h(phi,psi)=v(phi) cross w(psi),
    g(phi,psi)=h(phi,psi)/||h(phi,psi)||_1, when h!=0.

For every fixed eta>0, L990's formula (6) gives

    ||c_n-g(phi_n,psi_n)||_1 <= C/(n*eta)             (3)

for all sufficiently large n with ||h(phi_n,psi_n)||_1>=eta.
The bound applies to the exact polynomials, including their -1
terms. L990 also proves that on each fixed residue class modulo12
the phase pair is equidistributed on the two-dimensional torus;
in particular every nonempty open phase rectangle is visited at
arbitrarily large integer indices.

These are local inputs, not asymptotic or equidistribution theorems
being reproved here. L990 imports its bulk input from Gil–Segura–Temme,
*Asymptotic approximations to the nodes and weights of Gauss–Hermite
and Gauss–Laguerre quadratures*, arXiv1709.09656v1, section3.3,
[equations81–87](https://arxiv.org/html/1709.09656v1#S3.SS3), with
fixed alpha=2 and compact scaled argument [1/9,1/2]. Its orbit
argument applies the Weyl criterion in T. Tao, *Higher Order Fourier
Analysis*, 5June2012 manuscript, Proposition1.1.2, Exercise1.1.5 and
Proposition1.1.5, [printed pp5–7](https://terrytao.wordpress.com/wp-content/uploads/2012/12/gsm-142-tao7-higher-book-05june2012.pdf#page=13),
after checking every integer resonance using Lindemann–Weierstrass.
Only their already verified specializations in L990 are needed here.

### Three regular phase points

Set phi_*=-pi/3. Then cos(phi_*)=1/2 and
cos(phi_*+pi/3)=1. L990's cross-product identity becomes

    h(phi_*,psi)=(-cos(psi)+sin(psi)/2,
                  cos(psi),
                 -sin(psi)/2-cos(psi)).              (4)

Put t=arctan(2), so 0<t<pi/2, cos(t)=1/sqrt(5) and
sin(t)=2/sqrt(5). Formula (4) gives

    h(phi_*, t)=(0,1,-2)/sqrt(5),
    h(phi_*, pi/2)=(1/2,0,-1/2),
    h(phi_*,-t)=(-2,1,0)/sqrt(5).                    (5)

The corresponding g values are (0,1/3,-2/3), (1/2,0,-1/2),
and (-2/3,1/3,0). In order j=0,1,2 these points have g_j=0
and g_(k(j)) respectively 1/3,1/2,1/3, all strictly above1/4.
They have nonzero h, with l1 norms respectively 3/sqrt(5),1,
and 3/sqrt(5).

At these respective points the derivatives with respect to psi of
h_j(phi_*,psi) are

    sin(t)+cos(t)/2=sqrt(5)/2,
    -sin(pi/2)=-1,
    -cos(-t)/2+sin(-t)=-sqrt(5)/2.                   (6)

Thus each selected numerator changes sign at its point. The positive
normalizing denominator is continuous and bounded away from zero
in a neighborhood. It follows that g_j takes arbitrarily small
nonzero values of either sign there, while g_(k(j)) stays above1/4.
No derivative of the l1 norm, which need not be differentiable at
these points, is required for this conclusion.

### Passage to exact coefficients at integer indices

Fix j, M and s. By (5)–(6) and continuity, choose a nearby point
q with h(q)!=0, s*g_j(q)>0, |g_(k(j))(q)|>1/4, and

    |g_(k(j))(q)|>2*M*|g_j(q)|.

Choose a sufficiently small closed phase rectangle R around q,
with nonempty interior, on which h is nonzero, s*g_j is strictly
positive, and both strict inequalities

    |g_(k(j))|>1/4,
    |g_(k(j))|-M*|g_j|>0

hold with positive margins. Such an R exists by continuity and the
strict inequalities at q. Compactness gives eta=min_R ||h||_1>0
and positive minima for these margins and for s*g_j.

There are arbitrarily large n with (phi_n,psi_n) in the interior
of R. For all sufficiently large such n, (3)'s error is smaller
than half the sign and first-inequality margins, and smaller than
the last margin divided by 2*(1+M). The triangle inequality then
gives s*c_(n,j)>0, |c_(n,k(j))|>1/4, and

    |c_(n,k(j))|-M*|c_(n,j)|>0.

This proves (1) at exact integer indices with a nonzero denominator.
The rectangle and onset may depend on M,s,j; only arbitrarily large
visits after each fixed onset are asserted. No shrinking-target rate
or interchange of M and n is used. As ||c_n||_1=1, (1) also gives
|c_(n,j)|<1/M, proving the stated liminf by letting M increase.

For j=2, the induced infinity norm in (2) is

    max(1,(|c_(n,0)|+|c_(n,1)|)/|c_(n,2)|),

which exceeds M on the nonzero indices just obtained. The j=0 and
j=1 cases prove the remaining elimination claims in the same way.
They concern solving a row by division through the stated coordinate;
they do not exclude changing coordinates, time-dependent norms,
finite-block arguments or direct control of matrix products.

### Why this stops only the tested construction

The proposed forward homogeneous construction requires more than
cofinite definition: each forward pivot used must be nonzero, and
its products must produce a sequence of finite positive exponential
growth. C990a proves only vector nonvanishing. The bounded-matrix
shortcut to the second obligation is now false by (1)–(2), even on
regular phase neighborhoods and even restricting to nonzero pivots.
This strengthens a missing applicability hypothesis into a proved
failure for that specific representation.

Unbounded one-step norms do not determine the growth of a product
on a solution. Large factors might cancel, and a solution might align
with directions they do not amplify. Exact zero pivots, if any, also
impose relations that cannot be handled by (2). The full implicit
equations at those indices remain part of the target. Consequently
the current homogeneous construction is incomplete, and neither a
positive-rate witness nor stability follows. Nonzero subexponential
forcing and arbitrary initial values remain necessary in any positive
answer to the original implication. Arithmetic identification, shifted
boundaries, all prime powers, both complements and L984(H) are still
independent unresolved steps toward the main RH gap.

## Mathlib

Full matching coverage of this exact moving coefficient operator and
its fixed-pivot obstruction has not been checked. The input asymptotic
and equidistribution specializations are the audited local L990
results, with their primary citations above. Finite vector algebra,
continuity and compactness support the proof but are not a checked
matching Mathlib theorem. No formalization or absence claim is made.
