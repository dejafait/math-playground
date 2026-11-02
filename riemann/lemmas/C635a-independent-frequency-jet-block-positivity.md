# Corollary 635a: positivity for independent frequency/jet coefficients

## Hypotheses

Use the actual Xi normalization and exact source expression of L622,
the full positive definite Gram matrix G_N of L623, and the uniform
common-real-observer conclusions L635 (2) and (2a). Specifically, fix
nonnegative w in C_c^infinity((0,1)) with integral 1, and put

    L=log T, T<=X<=2T, N=floor(T^(1/100)),
    w_XT(t)=w((t-X)/T),
    A(t)=(t^2+1/4) pi^(-1/4)|Gamma(1/4+it/2)|/2,
    Z(t)=-Xi(t)/A(t), W(t)=(Xi'(t)^2-Xi(t)Xi''(t))/A(t)^2,
    u_0(t)=Z(t), u_1(t)=Z'(t)/L.

Let b,d be arbitrary independent complex vectors of length N, and set

    M_b(t)=sum_(n<=N) b_n n^(-it),
    M_d(t)=sum_(n<=N) d_n n^(-it),
    J(b,d)=integral w_XT(t) W(t)
                   |M_b(t)u_0(t)+M_d(t)u_1(t)|^2 dt/(T L^6),
    beta_0=28/(840pi^2), beta_1=1/(840pi^2),
    R(b,d)=beta_0 b^*G_N b+beta_1 d^*G_N d.

The coefficients may depend on T,X but are fixed during shift
differentiation. The normalization ||b||_2^2+||d||_2^2=1 is allowed
but unnecessary by homogeneity. L623 gives G_N>0 without discarding
its infinite convolution tail in any signed expression.

The moment and collision-holomorphy imports remain C. P. Hughes and
M. P. Young, *The twisted fourth moment of the Riemann zeta function*,
J. reine angew. Math. 641 (2010), 203–236,
[arXiv:0709.2345v2, Theorem 1.1/(11)–(17), pp. 3–5 and the p. 5
holomorphy remark](https://arxiv.org/pdf/0709.2345v2#page=3).
L622 checks their exact-phase application and L635 checks its full-Gram
error conversion at the used scope. Their external manuscript proofs
remain named imports. This corollary neither reproves an arithmetic
moment theorem nor assumes pointwise signs, RH, simplicity or spacing.

## Conclusion

There is one existential onset depending on w, independent of X,b,d,
such that

    |J(b,d)-R(b,d)| <= (9/10) R(b,d),
    J(b,d) >= (1/10) R(b,d).                              (1)

In particular J is strictly positive for (b,d)!=(0,0). The complete
Hermitian six-term source block defined below satisfies the same
relative defect bound at the common onset. Its separate error relative
to J is o(1/L)R, uniformly over the independent vectors. Bound (1)
uses L635's already combined actual-Xi reserve, rather than adding
this separate error to 9/10 again.

This is an elementary specialization of the existing local estimate,
not a new arithmetic input or certified progress beyond the assessed
literature. It closes this enlarged negative-average search at
sufficiently large heights under the named imports. No effective onset,
pointwise Xi sign, higher-sign theorem or RH resolution follows. This
corollary's mixed-block identities and uniform relative-error lift
passed the separate conceptual audit in Section 5. External manuscript
proofs remain named imports; the audit establishes no new arithmetic
theorem or improvement of the stated bound.

## Proof

### 1. The actual two mixed channels coincide and are Hermitian

For j=0,1,2 define matrices A_j by

    (A_0)_(m,n)=integral w_XT W u_0^2 (m/n)^(it) dt/(T L^6),
    (A_1)_(m,n)=integral w_XT W u_0 u_1 (m/n)^(it) dt/(T L^6),
    (A_2)_(m,n)=integral w_XT W u_1^2 (m/n)^(it) dt/(T L^6).

These are finite integrals of continuous functions on compact support,
including at real Xi zeros. The scalar factors multiplying (m/n)^(it)
are real. Swapping m,n therefore conjugates every entry, so each A_j
is Hermitian; no sign of W is used. Expanding the absolute square gives

    J(b,d)=b^*A_0 b+b^*A_1 d+d^*A_1 b+d^*A_2 d.         (2)

Both mixed channels contain exactly u_0 u_1. Thus the off-diagonal
blocks are the same Hermitian matrix A_1, including for complex b,d.
This assertion is stronger than knowing scalar contractions against
real observers: for a general block matrix those contractions could
miss an anti-Hermitian part. The actual integral has no such part.

### 2. Complete source block and conjugate orientation

Retain L622's complete H_hk(s), with the exact Hardy phase Phi, all six
source terms, and its factor 1/(T L^4 sqrt(hk)). Here s=(s1,...,s4)
denotes its scaled height shifts, to avoid confusing them with b. Put

    Q=partial_1 partial_2-(partial_1^2+partial_2^2)/2,
    j_0(h,k)=(Q H_hk)(0),
    j_1(h,k)=(Q partial_3 H_hk)(0),
    j_2(h,k)=(Q partial_3 partial_4 H_hk)(0).

In fact (Q partial_4 H_hk)(0)=j_1(h,k). To check this before
symmetrization, the prime-power divisor factors R_hk(alpha,beta,
gamma,delta) in L622 are symmetric within each shift pair. Under
gamma<->delta the first two source terms are fixed, the third and
fourth exchange, and the fifth and sixth exchange, using that pair
symmetry. Phi is also symmetric in s3,s4. Thus H_hk(s) is unchanged
by s3<->s4 away from collisions, and the named complete-sum holomorphy
extends the equality across collisions. Q commutes with this exchange.
This checks both separately differentiated mixed channels; no combined
real-observer coefficient table is used to assume their equality.

For g=gcd(m,n), define the Hermitian matrices

    (K_j)_(m,n)=[j_j(n/g,m/g)+conjugate(j_j(m/g,n/g))]/2,
    K_block = [ K_0  K_1 ] .                             (3)
              [ K_1  K_2 ]

Every original pair (m,n), including all diagonal multiplicities,
is retained. In the expansion with coefficients a_m conjugate(a_n),
the raw entry is j_j(m/g,n/g); its ordinary quadratic matrix is the
transpose. Formula (3) is precisely the Hermitian part of that
transpose. For the mixed bilinear sum, taking the real part replaces
the same raw matrix by its Hermitian part in both blocks, giving
b^*K_1 d+d^*K_1 b. Thus (3) has the correct conjugate orientation.

Linearity of the shift derivatives and the equality just proved give
exactly L622's common-observer matrix:

    K_c=c0^2 K_0+2c0 c1 K_1+c1^2 K_2.                   (4)

No phase, prime-power factor, normalization derivative, divisor tail
or mixed channel has been omitted in this definition.

### 3. A factor-two lift in the full Gram norm

The following elementary argument applies to any Hermitian triple
(D_0,D_1,D_2) with positive definite G and positive beta_0,beta_1.
Suppose, for all complex a and real c0,c1,

    |a^*[c0^2 D_0+2c0 c1 D_1+c1^2 D_2
                  -(beta_0 c0^2+beta_1 c1^2)G]a|
       <= delta (beta_0 c0^2+beta_1 c1^2) a^*G a.       (5)

Using the positive Hermitian square root of G, define

    E=beta_0^(-1) G^(-1/2)D_0 G^(-1/2)-I,
    F=beta_1^(-1) G^(-1/2)D_2 G^(-1/2)-I,
    C=(beta_0 beta_1)^(-1/2)G^(-1/2)D_1 G^(-1/2).

All three matrices are Hermitian. Set a=G^(-1/2)y in (5).
The coordinate observers give ||E||,||F||<=delta. The two observers
c=(beta_0^(-1/2), +/- beta_1^(-1/2)) give

    |y^*(E+F+2C)y|<=2delta ||y||^2,
    |y^*(E+F-2C)y|<=2delta ||y||^2.

Subtract the two quadratic forms and apply the triangle inequality:
|y^*Cy|<=delta ||y||^2. The finite-dimensional Hermitian spectral
theorem now gives ||C||<=delta, also on complex vectors. This is the
step that would fail for an uncontrolled anti-Hermitian mixed block.

For x=sqrt(beta_0)G^(1/2)b and z=sqrt(beta_1)G^(1/2)d,
the joint reference is ||x||^2+||z||^2=R(b,d). Consequently

    |x^*Ex+2 Re(x^*Cz)+z^*Fz|
       <= delta (||x||^2+2||x||||z||+||z||^2)
       <= 2delta (||x||^2+||z||^2).                     (6)

This proves the claimed lift for arbitrary independent complex vectors.
The proof is finite-dimensional and introduces no N-dependent constant.
If (5) is initially given for real unit c, homogeneity gives it for
all real c, including the two observers used above.

### 4. Uniform transfer errors and the positive margin

L635 (2) supplies (5) with D_j=K_j, G=G_N and delta=9/20.
For the exact integral, (2) gives the common contraction

    I_c(a)=a^*(c0^2 A_0+2c0 c1 A_1+c1^2 A_2)a.

L635 (2a) supplies the same (5) with D_j=A_j and delta=9/20,
uniformly in X,a,c beyond one common onset. Equation (6) therefore
proves both the source-block bound and (1), since 2delta=9/10<1.
The two coordinate and two sum/difference observers all lie inside
the homogeneous scope of that estimate. No onset is chosen separately
for b,d, an eigenvector, or a small Gram direction.

For explicit accounting of the source-to-actual-block error, write

    epsilon_T=C_w[T^(-17/80)/L^4+T^(-199/100)/L^2],
    gamma_N=1/[2N^4(N+1)(1+log N)^2].

L622 (1) and homogeneity bound the common error by
epsilon_T(c0^2+c1^2)||a||_2^2. L623 (2) gives

    gamma_N >= T^(-1/20)/[4(1+L/100)^2],
    |I_c(a)-a^*K_c a|
       <= e_T (beta_0 c0^2+beta_1 c1^2)a^*G_N a,
    e_T=epsilon_T/(beta_1 gamma_N)
       <=3360pi^2 C_w(1+L/100)^2
             [T^(-13/80)/L^4+T^(-97/50)/L^2]=o(1/L).   (7)

Apply the same proof (coordinate and sum/difference observers) to
the Hermitian error triple A_j-K_j with zero reference. It gives

    |J(b,d)-(b,d)^*K_block(b,d)|<=2e_T R(b,d).           (8)

This includes L622's differentiated moment error and the exact
completion curvature W=Z'^2-ZZ''-(log A)''Z^2. It charges the
absolute error even in small full-Gram directions. No independent
bilinear moment hypothesis or absolute-error reinterpretation is used.

L635 (2a) already combines the regular-zeta/phase relative error,
the full arithmetic row remainder and (7) in a single reserve. Its
arithmetic defect is eventually <=2/5, and its entire additional
relative cost is eventually <=1/20, at a uniform onset. The lift
doubles their total: 2(2/5+1/20)=9/10. Thus (8) is explanatory
error accounting, not a second charge added after this reserve.
Positive definiteness of G_N now makes R>0 for a nonzero pair.
This completes the proof without a new moment calculation or screen.

### 5. Independent mixed-block and reserve audit, 1 November 2026

The audit verifies (1)–(8) at exactly the stated scope. The local
inputs are L622 (1) and its complete phase-weighted expression,
L623 (1)–(2), and L635 (2)/(2a), including Section 5's combined
reserve. No assertion from an unrelated part of those lemmas or
an audit of the imported moment manuscripts is included.

**Both orientations before scalar contraction.** On the real support
A>0 and Xi is real, so W,u_0,u_1 are real and continuous, including
at multiple zeros. In the ordinary b^*A d convention the product
conjugate(M_b) M_d has coefficient conjugate(b_m)d_n(m/n)^(it).
Its weight is W u_0 u_1 in both mixed terms. Thus (2) has the
displayed orientation and a Hermitian A_1 without a sign assumption.

For the source, sigma_(u,v) is symmetric in u,v. This makes every
incremented numerator and denominator in L622's R_hk symmetric
within either pair, for both h and k orientations. Number the six
summands of L622 (3) in their displayed order. Under gamma<->delta
their permutation is

    1->1, 2->2, 3->4, 4->3, 5->6, 6->5.

For example the image R_hk(-delta,beta,-alpha,gamma) of the third
term equals the fourth term's R_hk(-delta,beta,gamma,-alpha)
by its second-pair symmetry; the exponential factors agree too.
The second term is fixed by first-pair symmetry. The exact Phi
has two identical negative-phase roles for s3,s4. Therefore the
complete H_hk is invariant under their exchange before Q is
applied. This is an identity off the collision sets, extended to
their holomorphic values by the named complete-sum import. It is
not differentiation of an individual singular summand. The powers
of L agree: Q contributes L^(-2) to 1/(T L^4), and each observer
derivative contributes precisely the 1/L in u_1.

To check symmetrization explicitly, let (T_j)_(m,n)=j_j(n/g,m/g).
The raw mixed contribution is b^*T_1 d+d^*T_1 b. Its real part is

    b^*(T_1+T_1^*)d/2+d^*(T_1+T_1^*)b/2.

This is (3), since K_1=(T_1+T_1^*)/2. Diagonal blocks obey the
same Hermitian-part convention. No raw-source Hermiticity is
required; equality of the two raw mixed channels is what permits
this formula. All gcd pairs, including m=n, are still present.

**Homogeneous observers and the block norm.** L635 is uniform over
complex a and real unit c. Both sides of its estimate are quadratic
in each, so normalization extends it to all a,c, with zero vectors
handled directly. The four observers used in Section 3 are the two
coordinate directions and (beta_0^(-1/2),+/-beta_1^(-1/2)); their
Euclidean normalizations have the same common onset. After the
G_N^(-1/2) change of variables, subtracting the plus and minus
quadratic forms isolates 4y^*Cy. Each form has bound
2delta||y||^2, hence |y^*Cy|<=delta||y||^2. Hermiticity is essential
to obtain the complex operator norm. Together with the coordinate
bounds and 2||x||||z||<=||x||^2+||z||^2 this gives exactly 2delta,
with no eigenvector-dependent onset or dimension factor.

**Small Gram directions and the single reserve.** L623's full Gram
identity converges by finite-prime square summability. Its inverse
convolution uses ||V_N||<=2sqrt(N)(1+log N) and
C_N>=2/[N^3(N+1)], giving the stated gamma_N. Only nonnegative
squares are dropped for this lower bound; no signed tail is dropped.
The bounds N<=T^(1/100), N+1<=2T^(1/100) give (7). In particular
17/80-1/20=13/80 and 199/100-1/20=97/50. Since beta_1 is the
smaller positive reference coefficient, division by beta_1 gamma_N
is valid for every real observer and every complex coefficient
direction. The two resulting terms decay faster than 1/L.

For the error triple use E=beta_0^(-1)G_N^(-1/2)(A_0-K_0)G_N^(-1/2)
and F=beta_1^(-1)G_N^(-1/2)(A_2-K_2)G_N^(-1/2), with no subtraction
of I; define C from A_1-K_1. The same four-observer argument with
delta=e_T proves (8), so the zero-reference version is justified.
L635 Section 5 chooses one onset for arithmetic defect <=2/5 and
one for the entire remaining relative cost <=1/20, covering both
source and actual integrals simultaneously. Their maximum is
uniform in X,c,a and hence in b,d. Applying the lift to that combined
bound costs 2(2/5+1/20)=9/10. Adding (8) afterwards would charge
the actual-Xi transfer twice and is unnecessary.

No correction to a constant, hypothesis, identity or DAG input was
needed. This independent verification closes the pending audit of
the detector stop only. It supplies neither an effective onset nor
pointwise signs, a higher-jet conclusion or an RH candidate. No
finite numerical check is used as a substitute for uniformity.

## Mathlib

Full matching coverage of this Xi application and block estimate has
not been checked and is unknown. The finite-dimensional Hermitian
spectral theorem is used only to turn Hermitian quadratic bounds into
operator-norm bounds; the particular factor-two argument is proved
above. No Mathlib theorem identifier or Lean certificate is asserted.
The imported analytic inputs retain L622/L635's stated qualifications.
