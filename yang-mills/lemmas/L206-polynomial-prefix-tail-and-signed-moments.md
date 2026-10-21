# L206 — Exact polynomial prefix tails and their signed transition moments

## Hypotheses

Use L205's complete setting and definitions, including both actual L010
probes, all relative faces, normal end rows, constant own-direction
modes, full heat sums and both residual subtractions. In particular
epsilon=N^(-7/4), Z=p(Delta+epsilon I) is L205's degree-d polynomial,
d=O(N^(7/8)log N), and X=2ZAZ is its polynomial covariance matrix.
No prefix, coefficient or projection is regularized here. L205 gives
X=PXP, Q_3=Q[X]+O(N^(23/8)) and G_i=-Q[X]+o(N^3).

Let I contain the row and column support of A, let E_I insert these
source indices, and put

    A_I=E_I^T A E_I, Z_I=Z E_I, F=Phi Z_I,
    W=Z_I-D F/2.                                      (1)

The columns of E_I are standard coordinate vectors, not a spectral
cutoff. Source indices are compactly interior by L205. For sufficiently
large N every d-step path from I is interior. The endpoint sum q,
incidence D, and lower prefix Phi retain their original pinned domains.

On the infinite component-1 grid write the translation-invariant kernel
of p(Delta_infinity+epsilon I) as k(r,z), r in Z and z in Z^3.
Here r is the axial difference of link tails. Put

    k_T(z)=sum_r k(r,z),
    ell(t,z)=sum_(r<=t-1) k(r,z)-1_(t>0) k_T(z).       (2)

These sums are finite; no uniform absolute kernel estimate is assumed.

## Conclusion

For a component-1 source h=(1;j,z_h) in I, every interior vertex
(s,z) has the exact prefix value

    F_((s,z),h)=1_(j<s<N) k_T(z-z_h)
                              +ell(s-j,z-z_h).        (3)

For a source in any other component its entire F column is zero.
All boundary vertex values in (3) are separately set to zero. The
first term is a long plateau up to the upper pin; it is not a local
error. The transition satisfies

    ell(t,z)=0 unless 1-d<=t<=d and |z|_1<=d,
    ell(t,z)=-ell(1-t,z),
    sum_t ell(t,z)=0,                                 (4)
    sum_t (t-1/2)ell(t,z)
                   =[p'(Delta_(T,infinity)+epsilon I)]_(z,0), (5)
    k_T(z)=[p(Delta_(T,infinity)+epsilon I)]_(z,0).     (6)

Delta_(T,infinity) is the three-dimensional nearest-neighbor scalar
Laplacian. The prime in (5) is the derivative of the same polynomial p;
it is not a derivative of a limiting inverse.

Both covariance-side prefixes in the third-placement trace can now be
evaluated with (3). More precisely, its four covariance blocks are

    K_VH=V X H^T=2q F A_I W^T,
    K_VV=V X V^T=2q F A_I F^T q^T,
    K_HH=H X H^T=2W A_I W^T,
    K_HV=H X V^T=2W A_I F^T q^T.                      (7)

In L187(7) replace its M covariance blocks by (7), retaining its
original HP, VP, alpha=Vn_k and Hn_k factors and full heat weights.
This is exactly Q[X], with its original signs and normalization.
The remaining projection-side prefixes have the separate exact forms

    VP=q(Phi-G_0 D^T),
    HP=P-D(Phi-G_0 D^T)/2,
    G_0=(D^T D)^(-1).                                 (8)

Thus neither a prefix crossing a projection nor a boundary correction
is discarded. Formula (3) expands each F in (7) into plateau and
transition terms, including both cross terms when F occurs twice.

For a scalar coefficient c twice continuously differentiable on the
physical axial interval containing the transition, set x_j=-4+a(j+1/2).
For each fixed transverse offset z, one further exact estimate is

    sum_t c(-4+a(j+t)) ell(t,z)
      =a c'(x_j)[p'(Delta_(T,infinity)+epsilon I)]_(z,0)+R,
    |R|<=a^2 ||c''||_infinity/2
                      sum_t (t-1/2)^2 |ell(t,z)|.     (9)

This is a conditional coefficient test, not an error bound for Q[X].
The growing polynomial's absolute second moment, its p' insertion,
the plateau terms and their remaining pinned Green contractions have
no cubic-scale estimate here. In particular (4) cannot be applied
across an upper jump or to a rough projection kernel by declaring it
smooth. No cubic limit, coefficient, vanishing or compensation follows.
This is local algebraic progress with standard polynomial methods,
not a claim of progress beyond the checked sources. All independent
interacting, continuum and infrared gaps remain.

## Proof

### 1. Evaluate the prefix before taking any limit

L205's finite-path comparison applies to every column Z E_I, before
any coefficient replacement. Delta is componentwise, so a column with
source component other than 1 has no axial link entries. Phi sums only
component 1, proving its zero assertion. For component 1, L026(2)'s
prefix at an interior vertex is sum_(r=0)^(s-1) of its axial links.
Every nonzero entry of the column lies away from physical faces, so
the sum can be extended to all axial indices below s. Translation
invariance of the infinite polynomial gives

    F_((s,z),h)=sum_(v<=s-j-1) k(v,z-z_h).

Subtract and add 1_(s>j) k_T to obtain (3). L205 supplies finite
propagation: k(r,z)=0 if |r|+|z|_1>d. The cumulative sum is zero
when t<=-d and equals k_T when t>=d+1. This proves the support in
(4). Its transverse support follows from the same range bound.

Phi has only interior vertex rows. Equation (3) must therefore be
extended by zero, rather than by its plateau, at s=N. Applying D or q
after this extension retains the entire upper pinned jump. Compact
source support and d=o(N) ensure the transition never reaches a face;
they do not shorten the plateau.

### 2. Exact signed moments, including their lattice midpoint

Axial reflection commutes with Delta_infinity and fixes a point source.
Therefore k(-r,z)=k(r,z) for every z, also for a polynomial with signed
coefficients. Reflecting the finite sum in (2) gives

    sum_(r<=t-1) k(r,z)+sum_(r<=-t) k(r,z)=k_T(z).

For integer t, 1_(t>0)+1_(1-t>0)=1. Subtracting the step functions
proves ell(t,z)+ell(1-t,z)=0. Since the support is finite and invariant
under t -> 1-t, its zeroth moment is zero.

For each fixed z, directly differencing (2) yields

    ell(t+1,z)-ell(t,z)=k(t,z)-1_(t=0)k_T(z).         (10)

Multiply by t^2 and sum over all integers. Shifting the finite sum
on the left gives sum_t(-2t+1)ell(t,z). Its zeroth moment vanishes,
and the delta term on the right has t^2=0. Hence

    sum_t (t-1/2)ell(t,z)=-1/2 sum_r r^2 k(r,z).      (11)

To evaluate both kernel moments, use finite Fourier polynomials,
which require no convergence or singular-integral interchange. At
axial angle theta and transverse angle xi the symbol is

    p(epsilon+2-2cos(theta)+lambda_T(xi)),
    lambda_T(xi)=sum_(mu=2)^4 (2-2cos(xi_mu)).

Setting theta=0 proves (6). Taking two theta derivatives at zero
gives 2p'(epsilon+lambda_T(xi)). On the kernel side that derivative
is -sum_r r^2 k(r,z), after transverse Fourier inversion. Equation
(11) proves (5). The half-integer midpoint in (5) is fixed by the
actual link-to-vertex prefix and has not been replaced by a vertex
midpoint. These calculations hold for each finite degree and mass;
they assume no uniform derivative approximation to a resolvent.

### 3. Substitute both legs without changing the signed trace

Since A=E_I A_I E_I^T, X=2Z_I A_I Z_I^T. Direct multiplication
gives VZ_I=qF and HZ_I=Z_I-D F/2=W, proving all four formulas (7).
L187(7) is linear in its symmetric covariance M. Its algebraic proof
therefore applies with X=X^T=PXP, retaining every one of its four
terms. Their exterior n_k=S e_k and y=e_l do not change. Multiplying
by a^2 and summing the complete d_(i;kl) gives exactly L205(1)'s
Q[X]. There is no approximation in this substitution. L205's uniform
error remains O(N^(23/8)), and L202's original joint group still has
the minus sign G_i=-Q[X]+o(N^3).

For (8), use the actual pinned identity Phi D=I from L196. Substitution
in P=I-DG_0D^T gives Phi P=Phi-G_0D^T. The definitions of V and H
then prove (8), in their stated order. No multiplier is commuted with
P or G_0. In particular the compact covariance source indices in
(1) do not restrict the rows or sources of the remaining Green matrix.

### 4. What the signed moment does and does not control

Taylor's theorem at x_j writes

    c(-4+a(j+t))=c(x_j)+a(t-1/2)c'(x_j)+r_t,
    |r_t|<=a^2(t-1/2)^2 ||c''||_infinity/2.

Multiply by ell and sum. Its constant term is exactly zero by (4),
its linear term is (5), and the absolute remainder proves (9).
The transition is interior, so no upper boundary value has entered
this Taylor argument. The long plateau has deliberately not been
included in that remainder.

This is a possible replacement for an absolute coefficient-freezing
argument: the signed zeroth transition moment vanishes even at the
growing degree. It is not yet such a trace argument. Both original
prefix placements, coefficients at distinct output levels, finite
projection corrections, insertion subtractions, faces, constant modes
and heat sums remain in (7)--(8). Bounding a^3 times their actual
remainder, or identifying their cumulative coefficient, is still
necessary. Small d/N alone remains insufficient by L205's stated
O(N^(7/2)) absolute count. All checks here are analytic finite sums;
no numerical diagnostic or mathematical script is used.

## Mathlib

Full matching actual-probe prefix reduction and cubic limit: **not
checked**. Supporting polynomial functional calculus, finite Fourier
polynomials, finite-sum shifts and Taylor's theorem: **not checked**;
unknown coverage is not evidence of absence. L026 supplies the exact
pinned lower prefix, L187 the full signed four-term contraction,
L196 the pinned projection identity, L202 the joint-group reduction,
and L205 the polynomial comparison and finite propagation. The finite
sum calculation is needed to keep the lattice midpoint, long upper
plateau and signed moments of this varying-degree polynomial; no
general flow or renormalization theorem is reproved. Reuse the unchanged
[approved assessment](../drafts/literature/2026-10-14-joint-cubic-probe-jet-scale.md)
within its exact joint-group target. No further literature claim or
originality assertion is made.
