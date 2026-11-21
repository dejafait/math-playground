# Corollary C030v: a finite conjugate-rate basis evolution bound

## Hypotheses

Fix integers m>=1, n>=max(4,2m) and 2<=d<=floor(n/2). Fix positive
real a_1,...,a_m,r and real b_1,...,b_m. The actual n rates are

    (q_1,...,q_n)=(a_1+i*b_1,a_1-i*b_1,...,
                   a_m+i*b_m,a_m-i*b_m,r,...,r).

Put A=sum_l |b_l|, M=sum_l b_l^2 and q_max=max_(1<=j<=n) Re(q_j).
When n=2m there are no r entries, so r does not enter q_max. All rates
are fixed throughout time differentiation. Assume

    0<s<=t, t*A<=1/4,
    (n-2*d+1)/2 >= sqrt((d-1)*(n-d+1)).                  (H)

Use exactly C030r's d-by-d real coefficient matrix C_b(x): its rows
are the signed-orthogonal polynomials Q_0,...,Q_(d-1) in increasing
monomial order, with positive leading coefficients and signed norms
(-1)^i for the derivative functional of f_b=e_(q_1)*...*e_(q_n), where
e_q(y)=q*exp(-q*y) for y>0 and zero otherwise. Let C_0(x) be the same
construction after setting all b_l=0 and retaining all real rates.
The norm is the Euclidean operator norm in these coefficient coordinates.
Repeated rates, zero phases, every real-part contrast, n=2m, s=t and
the closed phase boundary t*A=1/4 are included.

## Conclusion

The approved finite evolution estimate holds with the absolute constant
C=37/4:

    ||C_b(t)*C_b(s)^(-1)||_2
       <= exp(q_max*(t-s)/2 + (37/4)*M*(t^2-s^2)).       (1)

The constant is independent of m,n,d and all real rates and contrasts.
No sharpness is asserted. This is a source-based specialization under
assessment1238/review1239, completed in attempt1240. Independent
conceptual audit1242 under SPECIALIZE assessment1240/review1241 passes
(1) with unchanged hypotheses and constant; its checks are below.
Classification REPRODUCTION credits the known
real-reference theorem and matrix-norm method; no originality or RH
candidate is claimed. The result is finite and restricted by (H) and
the phase window. It does not assert an s=0 estimate, global signed
smoothing, actual-Xi realization or all-degree mixed positivity.

## Proof

### Imported real-reference and matrix-norm results

S. Sra, *On some positivity properties of the Riemann Xi function*,
[arXiv2611.02944v1, 2 November 2026](https://arxiv.org/pdf/2611.02944v1),
Theorem C.8/(C.15)-(C.17), printed pp26-27, and the proof of Theorem C.9,
(C.18)-(C.23), printed pp27-29, give the real-reference estimate used
here. In the source's basis dimension m, renamed d here, it assumes
positive real rates 0<q_j<=Q, n>=2d, and the degree inequality (H).
For its lower-bidiagonal moving-basis generator K_0(x), (C.23) gives

    lambda_max((K_0(x)+K_0(x)^T)/2)<=Q/2, x>0.          (2)

The subsequent proof evolves C_0(t)*C_0(t-u)^(-1) on the right and
uses the row-vector energy identity and Gronwall. We import (2), with
the same coefficient normalization as C030r, rather than reprove its
real-rate estimates. The reference list here is
(a_1,a_1,...,a_m,a_m,r,...,r), whose maximum is precisely q_max.
It consists of n positive real rates; repeats are permitted by the
cited result. Thus Q=q_max, n>=2d and (H) verify all the hypotheses
for (2). This application does not extend (2) analytically to complex
rates. The source's support-boundary and global conclusions are unused.

N. J. Higham, [*What Is the Logarithmic Norm?*, 18 January 2022](https://nhigham.com/2022/01/18/what-is-the-logarithmic-norm/),
Lemma 2 and Theorem 6, state, for the same finite subordinate norm,

    |mu_2(U)-mu_2(V)|<=||U-V||_2,
    mu_2(U)=lambda_max((U+U*)/2).                        (3)

These are standard matrix facts, imported by citation. The necessary
specialization is the quantitative comparison of the present generators
and the ensuing time-dependent energy argument. No autonomous
matrix-exponential formula is applied to a nonautonomous system.

### Dimension-independent generator comparison

For s<=x<=t, C030r supplies real, invertible, smooth C_b(x), C_0(x)
and the equations C_b'=K_b*C_b, C_0'=K_0*C_0. Both generators are lower
bidiagonal. Write E_i(x) for C030q's difference of adjacent orbital
responses. C030r(6)-(7) give exactly

    (K_b-K_0)_(ii)=E_i(x)/2,                   0<=i<d,
    (K_b-K_0)_(i,i-1)=beta_(i,b)(x)-beta_(i,0)(x),
                                               1<=i<d. (4)

Every x in this interval has x*A<=1/4. C030q(2) and C030t(1a) therefore
imply, uniformly in all these indices,

    |(K_b-K_0)_(ii)| <= (9/2)*x*M,
    |(K_b-K_0)_(i,i-1)| <= 14*x*M.                     (5)

C030t's unconditioned conclusion already incorporates C030u's
real-reference comparison with c=1. There is no extra monotonicity
assumption here. When M=0 both differences vanish, so the weak form
of (5) remains valid. Each response retains its own normalizer; no
common positive law for the derivative functional is introduced.

Let D be the diagonal part of K_b-K_0 and S its subdiagonal part.
For a column vector z in C^d,

    ||D*z||_2^2 <= (max_i |D_(ii)|)^2*||z||_2^2,
    ||S*z||_2^2 = sum_(i=1)^(d-1) |S_(i,i-1)|^2*|z_(i-1)|^2
                <= (max_(1<=i<d) |S_(i,i-1)|)^2*||z||_2^2.

Thus the two operator norms are bounded by the respective maxima,
without a dimension factor. The triangle inequality and (5) give

    ||K_b(x)-K_0(x)||_2 <= (37/2)*x*M.                  (6)

This compares the generators in their identified row-index coordinates;
it does not compare C_b and C_0 by conjugation or bound either inverse.
Combining (2), (3) and (6), with the real transpose equal to the adjoint,
now gives

    mu_2(K_b(x)) <= q_max/2 + (37/2)*x*M.               (7)

### Correctly ordered nonautonomous evolution

Fix t and put h=t-s. For 0<=u<=h define

    R(u)=C_b(t)*C_b(t-u)^(-1).

C030r's smoothness and invertibility on [s,t] justify the inverse
derivative. Indeed, with x=t-u and C=C_b(x),

    d/du (C_b(t-u)^(-1))
       =C^(-1)*C_b'(x)*C^(-1)=C^(-1)*K_b(x).

Consequently

    R'(u)=R(u)*K_b(t-u),       R(0)=I_d.                (8)

The generator is on the right; no matrices at different times are
commuted. For any initial real row vector w_0 set w(u)=w_0*R(u).
Equation (8), the Euclidean energy identity and (7) yield

    d/du ||w(u)||_2^2
       =w(u)*(K_b(t-u)+K_b(t-u)^T)*w(u)^T
       <= 2*(q_max/2+(37/2)*(t-u)*M)*||w(u)||_2^2.      (9)

All coefficients are continuous on this compact interval because
s>0. Multiplication by the scalar integrating factor, or equivalently
Gronwall's inequality, gives

    ||w(h)||_2 <= exp(integral_0^h [q_max/2+(37/2)*(t-u)*M]du)
                    *||w_0||_2.

The supremum over unit row vectors equals the Euclidean operator norm
of R(h): the norm of the transpose equals that of the matrix. Real
vectors suffice since R(h) is real. Finally,

    integral_0^(t-s) [q_max/2+(37/2)*(t-u)*M]du
       =q_max*(t-s)/2+(37/4)*M*(t^2-s^2).

Since R(h)=C_b(t)*C_b(s)^(-1), this proves (1).

### Boundary and scope checks

If s=t, R(0)=I_d and both sides of (1) equal one. If M=0, all phases
vanish, C_b=C_0 and the phase term is zero, recovering the cited real
bound. Repeated rates require no limiting argument: all imported local
interfaces and the real-reference estimate allow them. The case n=2m
uses no r entry anywhere in (2) or (7). Every real contrast is allowed
in C030q and C030t and remains unrestricted here.

At t*A=1/4 the determinant floor is still strict; C030r establishes
smoothness on an open neighborhood of each such endpoint. Thus (8)-(9)
are legitimate at the closed boundary, and their bounds are needed
only on [s,t]. No passage to s=0, uniform onset, uniform positive beta
floor, or uniform inverse-basis norm is used. The derivative functional
remains signed. The remaining actual-Xi supply, degree/time selection,
signed-complement payment, theta signing, graph realization and all-degree
positivity gaps are not addressed by (1).

### Independent conceptual audit1242

17 November 2026. This audit checks the complete local assembly against
the established C030q/r/t interfaces and the precise real-reference and
logarithmic-norm imports above. Coverage1238/review1239 is reused; the
external source theorems and the previously audited input proofs are
not independently reproved. No change of hypothesis, normalization,
constant or mathematical argument is needed. The result remains a
source-based finite specialization, not a new source theorem or an RH
candidate.

First check the normalization that determines the generator. In C030r
the monic signed norm is h_i=(-1)^i*D_(i+1)/D_i, so the positive leading
coefficient of Q_i is ell_i=sqrt(D_i/D_(i+1)). Differentiating its signed
orthogonality includes both moving-polynomial terms on the diagonal;
it gives K_ii=-alpha_i/2. For j=i-1, division by (-1)^(i-1) gives
K_(i,i-1)=ell_(i-1)/ell_i>0. Thus C030v uses exactly C030r's row
normalization, not a positive Gram normalization or the transposed
system. In the difference of the two diagonals, C030r(6) gives
alpha_(i,b)-alpha_(i,0)=-E_i. Therefore (4) has the positive sign and
factor E_i/2, including i=0. The largest orbital rank needed is d,
which is available because d<=floor(n/2).

C030q gives |E_i|<=9*x*M. C030t's full conclusion (1a), together with
its separate M=0 case, gives the weak bound 14*x*M for every required
subdiagonal. Its condition (H) is already discharged by C030u for the
identical fixed real list, with c=1; it is not C030v's degree condition
(H), and neither is silently dropped. No input from the pending C030s
or parked joint-moment argument is used. All reference rate-product
normalizations are those of C030r; no extra scale factor multiplies
either part of (4).

The real-reference import is applied only to positive real rates. Its
dimension is d, distinct from the number m of conjugate pairs; n>=2d
and its exact additional degree inequality are explicit here. Setting
the phases to zero preserves every actual real entry and its maximum
q_max. In particular an unused r when n=2m never enters that maximum.
The source's positive-leading-coefficient, alternating-sign basis is
the one just checked, so (2) applies to this K_0 in the same Euclidean
coordinates. Repeated positive rates are within the inspected source
statement. No complex-rate or signed-variance version of (2) is used.

For the norm step, each column of S has at most one nonzero entry and
those entries occupy distinct rows. Consequently the displayed formula
for ||S*z||_2^2 includes no cross terms; its bound is the maximum entry,
not a sum over rows. The diagonal part has the same maximum-entry norm
property. The triangle inequality yields (9/2+14)*x*M=(37/2)*x*M,
independently of d. Both matrices act on the identified polynomial-row
index space, so the subordinate-norm perturbation theorem applies
directly. There is no unbounded change-of-basis similarity hidden in
(6), and no inverse-basis norm is needed to obtain (7).

For the evolution, differentiating the inverse first gives
(d/dx)C^(-1)=-C^(-1)*C'*C^(-1). Substituting x=t-u and C'=K*C
therefore gives (d/du)C_b(t-u)^(-1)=C_b(t-u)^(-1)*K_b(t-u),
with the two minus signs cancelling. Hence (8) evolves on the right.
For w=w_0*R, differentiation of w*w^T gives exactly w*(K+K^T)*w^T.
The signed functional never serves as a norm in this argument: this
is the positive Euclidean row energy. Its scalar bound integrates to
2 times the exponent in (1) for the squared norm, and taking the
nonnegative square root removes that factor 2. Explicitly,
integral_0^(t-s)(t-u)du=(t^2-s^2)/2, giving 37/4. Maximizing over real
unit rows yields ||R^T||_2=||R||_2. It also controls complex vectors:
for real R and z=x+i*y, ||R*z||_2^2=||R*x||_2^2+||R*y||_2^2.
No time-ordered product is replaced by an ordinary exponential.

For every point of [s,t], C030q's strict floor and C030r's determinant
identity give real, nonzero pivots. At the closed phase endpoint the
finitely many pivots remain nonzero on a common open neighborhood;
the same positive-square-root branch is smooth there. Thus the inverse
derivative and continuous coefficients used by Gronwall are valid on
the whole compact interval. Only the estimates inside the phase window
are used. The lower endpoint s>0 is essential and is retained.

If s=t, the interval has length zero and (1) is equality. If M=0,
every b_l=0 and K_b=K_0, so (1) reduces to the imported real bound.
Partial zero phases and repeated rates introduce no divided difference
or singular denominator. At n=2m the constructions simply omit r;
all remaining restrictions, including n>=4 and the degree inequality,
still apply. Arbitrary fixed real-rate contrasts are already covered
by both coefficient inputs and the reference theorem. These checks
also cover t*A=1/4 without a one-sided derivative convention.

Full matching Mathlib coverage remains unchecked. This audit establishes no s=0
limit, global signed-convolution statement, actual-Xi supply or
all-degree positivity. Those require separate hypotheses and work.

## Mathlib

Full matching coverage for this conjugate-rate finite-basis estimate
has not been checked. No absence claim is made. The source-level inputs
are the precisely cited real-generator bound and logarithmic-norm facts;
the additional finite matrix calculation and nonautonomous energy
argument are written above. No Lean theorem or numerical certificate
is asserted to verify (1).
