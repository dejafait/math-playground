# Lemma 642: constrained vertical trace and its uniform distant tail

## Hypotheses

Use L641's actual-Xi zero-pair identity, rational space H_N, boundary
norm dx/(2pi), concentration space E_N and grid. In particular

    T>=e^5, N=floor(log T), T<=X<=2T, c=X+1/2,
    a=3/2, u_j=j/N-1/2, Q_N(z)=product_(j<N)(z-u_j+ia),
    H_N={P/Q_N: deg P<N}, I=[-1,1].

E_N is the eigenspace of the boundary concentration operator with
eigenvalues at least 1-N^(-1/2). It depends on N, not X. For each X,
let U_X be its intersection with the kernels of evaluations at every
w=zeta-c with |Re w|<=1, where zeta ranges over actual Xi zeros.
All occurrences and both conjugates are retained. Repeated occurrences
give repeated value constraints, not derivative constraints. L018 gives
|Im zeta|<1/2 and conjugation symmetry with multiplicities. Use L467's
closed unit-shell count, including its stated source-audit qualifications.
Neither RH nor simplicity nor a positive complex-zero measure is assumed.

The finite generalized inverse is imported from R. Penrose,
*A generalized inverse for matrices*, Proc. Cambridge Philos. Soc.
**51** (1955), 406--413, Theorem 1 and proof, pp.406--407, and the
following lemma on p.408
([primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/5F4516D6B9989BB6563A4B267CC7D615/S0305004100030401a.pdf/div-class-title-a-generalized-inverse-for-matrices-div.pdf)).
These sources and the finite model-space and zero-count inputs were
already assessed before this attempt. The projection specialization
below is standard finite linear algebra. The purpose of the rational
estimate is to supply a uniform growing-family tail, which fixed-N
convergence in L641 does not itself supply. L641 remains separately
unaudited; this lemma does not certify all of that input.

## Conclusion

Choose any orthonormal basis f_1,...,f_d of E_N and write f(z) for its
row of values. Form the matrix D with one row f(w) for each local
zero occurrence. With D^dagger its Moore--Penrose inverse, put

    Pi=I_d-D^dagger D,
    k_U(z,v)=f(z) Pi f(v)^*,   r_X=tr Pi=d-rank D.             (1)

Pi is exactly the orthogonal projection onto the coefficient space of
U_X. Empty, dependent and repeated constraint rows are allowed. The
full signed exterior trace on U_X is

    tau_X=sum_(zeta: |Re(zeta)-c|>1)
                    k_U(zeta-c, conjugate(zeta)-c).          (2)

This is an absolutely convergent real sum. It is the trace of L641's
zero-pair Hermitian form compressed to U_X, before division by ell_X.
All local terms vanish. In particular its summands are mixed evaluations,
not nonnegative diagonal values.

For z=x+iy, |y|<=1/2, |x|>=1, set b=|x|-1/2 and

    q(b,y)=[b^2+(a+|y|)^2]/[b^2+(a-|y|)^2].

Uniformly for every X and its actual constraint matrix,

    |k_U(z,conjugate(z))|
      <=3N q(b,y)^((N-1)/2)/[b^2+(a-|y|)^2]
      <=3N exp(3N/[2(b^2+1)])/(b^2+1).                     (3)

There is an absolute constant C_Xi such that for every
R>=max(2,sqrt(N)),

    sum_(zeta: |Re(zeta)-c|>=R)
          |k_U(zeta-c,conjugate(zeta)-c)|
      <= C_Xi N [log(c+R+4)+1]/R.                           (4)

The constant is independent of T,N,X,R, the evaluation rank and the
chosen basis. The proof gives C_Xi=144 e^6 A_0, with A_0 a fixed
all-height shell constant defined below. Thus R=sqrt(N) gives O(N^(3/2))
uniformly in X in [T,2T]. At L641's favorable heights, r_X>=kappa N-o(N),
so this distant tail divided by ell_X r_X is O(N^(-1/2)). Consequently

    tau_X = sum_(1<|Re(zeta)-c|<sqrt(N))
                     k_U(zeta-c,conjugate(zeta)-c)
                +O(N^(3/2)).                               (5)

No little-o estimate or actual-zero obstruction is established for
the remaining annulus in (5). The result therefore does not settle
the approved full-trace target. It supplies a partial tail estimate,
not a fixed norm reserve, positive/negative eigenvalue or RH result.
It is locally proved here and separately unaudited.

## Proof

### Projection in E_N, including rank deficiency

Represent h in E_N as h(z)=f(z)alpha with alpha a column. Orthonormality
gives ||h||=||alpha||, and the local constraints are exactly D alpha=0.
All evaluations are finite: their imaginary parts have absolute value
at most 1/2, whereas the poles lie at imaginary part -3/2. The local
multiset is finite by the strip bound and compact finiteness of zeros.

Penrose's identities imply that D^dagger D is self-adjoint and
idempotent. Also D(I-D^dagger D)=0. If D alpha=0 then
(I-D^dagger D)alpha=alpha. Thus Pi is the orthogonal projection onto
ker D, and rank-nullity proves the formula for r_X. If there are no
rows, set D^dagger D=0, giving Pi=I_d. No independent-row inverse or
condition-number assertion has been substituted for this projection.

Choose an isometry W from C^(r_X) onto ker D. Its columns give an
orthonormal basis h_l(z)=(f(z)W)_l of U_X. Since WW^*=Pi,

    sum_l h_l(z) conjugate(h_l(v))=f(z)Pi f(v)^*=k_U(z,v).     (6)

In particular this kernel is basis independent. A projection onto the
evaluation nullspace in H_N followed by a projection onto E_N would
not in general equal (1); that unproved replacement is not used.

### Uniform mixed-evaluation bound

L641 verifies the orthonormal basis of the full H_N

    e_j(z)=sqrt(3)/(z-u_j+ia)
                    product_(k<j)(z-u_k-ia)/(z-u_k+ia).

For any subspace U of H_N, orthogonal projection of the evaluation
vector and Cauchy--Schwarz give

    |k_U(z,v)|<=sqrt(k_U(z,z) k_U(v,v))
                <=sqrt(k_H(z,z) k_H(v,v)).                  (7)

This bounds the trace kernel directly; it does not multiply a
single-vector bound by dim U. It applies in particular to the actual
U_X, whatever the constraint rank.

Suppose first y>=0. Put d_j=x-u_j, so |d_j|>=b. At x+iy every
factor in the product defining e_j has modulus at most one. At x-iy
the squared modulus of its k-th factor is

    [d_k^2+(a+y)^2]/[d_k^2+(a-y)^2] <= q(b,y).

The last inequality follows because the ratio is
1+4ay/[d_k^2+(a-y)^2]. Both prefactors have squared modulus at most
3/[b^2+(a-y)^2]. Hence

    k_H(x+iy,x+iy)<=3N/[b^2+(a-y)^2],
    k_H(x-iy,x-iy)<=3N q(b,y)^(N-1)/[b^2+(a-y)^2].           (8)

For y<0 interchange the two evaluations. Combining (7)--(8) proves
the first inequality in (3), also at y=0. Since a=3/2, |y|<=1/2,

    log q(b,y)<=6|y|/[b^2+(a-|y|)^2],
    b^2+(a-|y|)^2>=b^2+1,

the second inequality follows. These estimates keep both members of
each conjugate pair; they assert no positivity of its contribution.

### The entire distant tail, with both ordinate signs and endpoints

Let M_0 be the number of Xi zeros on Re zeta=0, counted with
multiplicity. It is finite: all such zeros lie in the compact segment
|Im zeta|<=1/2 and Xi is a nonzero entire function. No absence of these
zeros is required for this proof. L467 and the even symmetry of L018
give, for every real v,

    #{zeta: v<=Re zeta<=v+1} <= A_0 log(|v|+3),
    A_0=36+M_0/log 2.                                      (9)

For v>=0 use the positive-height shell count plus M_0 if v=0; for
v<=-1 reflect the interval and do the same. For -1<v<0 split it at
zero; each nonzero half is bounded by the count in a reflected copy
of [0,1], at most 18 log 2. Adding M_0 proves (9), since
log(|v|+3)>=log 2. All these are upper bounds with closed endpoints,
so overcounting endpoints causes no loss of coverage.

Write s=|Re(zeta)-c|. For s>=R>=max(2,sqrt(N)), b=s-1/2>=s/2.
Equation (3) gives

    |k_U(zeta-c,conjugate(zeta)-c)|<=12 e^6 N/s^2,            (10)

because b^2+1>=s^2/4 and 3N/[2(b^2+1)]<=6N/s^2<=6.
Let m=floor R>=R/2. The shell k<=s<=k+1 is contained in
the two closed intervals [c+k,c+k+1] and [c-k-1,c-k]. By (9) its
count is at most 2A_0 log(c+k+4). We may include extra points in
the first shell when R is not an integer. Thus the tail in (4) is
at most

    24 e^6 A_0 N sum_(k>=m) log(c+k+4)/k^2.                 (11)

For k>=m>=1,

    log(c+k+4)<=log(c+m+4)+log(k/m),
    sum_(k>=m) 1/k^2<=2/m,
    sum_(k>=m) log(k/m)/k^2<=3/m.                           (12)

The first follows from c+k+4<=(c+m+4)k/m. For the last, use
log t<=sqrt(t) for t>=1 and
sum_(k>=m) k^(-3/2)<=3/sqrt(m), obtained by a first term plus
the integral from m to infinity. The elementary logarithm inequality
follows by minimizing sqrt(t)-log t at t=4, where it is positive.
Combining (11)--(12), m>=R/2 and m<=R gives the upper bound

    48 e^6 A_0 N [2 log(c+R+4)+3]/R
       <=144 e^6 A_0 N [log(c+R+4)+1]/R,

as asserted. This proves an absolute bound for the full infinite tail,
including arbitrarily negative ordinates. No numerical truncation,
positive-zero-only sum or hidden fixed-N constant is used.

For fixed N,X the complement of this tail contains only finitely many
zeros. The same bound (7) applies to a one-dimensional subspace spanned
by any unit h, so all of its paired sums converge absolutely as well.
We may therefore sum L641's zero-pair identity over the finite
orthonormal basis of U_X and interchange these sums. Equation (6)
gives (2). Every local contribution vanishes by D Pi=0. Conjugation
of a summand exchanges zeta with its conjugate, preserving its
multiplicity and the exterior set; hence (2) is real and its operator
is Hermitian. This also justifies the complete-tail passage, rather
than inferring it from a formal projection identity.

For R=sqrt(N), log(c+R+4)=O(log T)=O(N), uniformly in X. L641 gives
r_X>=kappa N-O(sqrt(N)log N) at its count-selected heights, with
kappa>0; also ell_X=log(X/(2pi)) is asymptotic to N uniformly on
[T,2T]. Equation (4) now proves (5) and the normalized O(N^(-1/2))
tail claim. Constants may be large, but are independent of the growing
parameters and of the actual constraint matrices.

### What remains quantitatively unproved

An explicit version of the near-annulus cost follows from the first
inequality in (3). For |x|>=1 set

    g(y)=(1/2) log{[1/4+(3/2+y)^2]/[1/4+(3/2-y)^2]},
                  0<=y<=1/2.

The ratio q decreases as b increases, and its value increases with y
on this range (the derivative of g is a sum of positive terms).
Consequently

    |k_U(x+iy,x-iy)|
       <=3N exp(N g(|y|))/[(|x|-1/2)^2+1],
    g(0)=0, g(1/2)=(1/2)log(17/5)>0.                       (13)

Applying only (9) to 1<|x|<sqrt(N) bounds its absolute sum by
O(N log(c+sqrt(N)+4) exp(N g(1/2))). Indeed, for the shell k>=1
the denominator is at least k^2/4, and sum_(k>=1) k^(-2) is finite.
This is an upper envelope of size O(N^2 exp(N g(1/2))), not o(N^2).
Even putting y=0 in this particular envelope yields merely O(N^2).
Failure of the upper envelope is not a lower bound or a counterexample
for the actual trace, and (13) does not assert that any actual zero
attains its worst case.

The constraints have been respected in (1)--(5), but contraction (7)
has discarded their finer cancellation in the near annulus. No bound
on D^dagger, conditional cancellation of the projection correction,
or simultaneous favorable-height theorem is asserted. Neither L641's
unconstrained test pair nor its boundary leakage fills this gap.

If the full unnormalized trace were o(ell_X r_X) with r_X>0, finite
Hermitian spectral theory would give a unit vector with exactly the
average Rayleigh quotient tau_X/(ell_X r_X): take equal squared
coefficients in an orthonormal eigenbasis of the compressed form.
L641 transfers that quotient to the full normalized C,K diagnostic.
This conditional use does not place an eigenvalue near zero and
does not assert a negative eigenvalue. The prerequisite full-trace
bound has not been obtained here.

## Mathlib

Full matching coverage is not checked; unknown availability is not
absence. Finite orthogonal projections, Hermitian spectral theory,
matrix generalized inverses and convergent nonnegative-series estimates
are supporting mathematics. No formalization of this growing-grid,
actual-zero tail specialization is claimed.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
