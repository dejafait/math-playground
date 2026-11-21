# Lemma 687: discarding a linear block exhausts the small-circle polynomial dual budget

## Hypotheses

Use L666's exact independently displaced family. Thus q>=1 is an
integer, n=12q+3, M=4q+1=n/3, x=-d=-5/4, R=11/8, U=R^2,
h=27/(10n), t_j=j/n for 0<=j<n, and

    Z={x} union {x+i*h*(m+1/2+e_m): -2q<=m<2q},
    e_m real, |e_m|<=1/8,
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    F(u,z)=sum_(a in Z) W_a(u)/(R-a*z),
    V=max_(|u|=|zeta|=1) |F(u,r*zeta)|,
    D=mean_(|u|=1) sum_(a in Z) |W_a(u)|^2/(U-|a|^2),
    r=1/32, A=R/r=44.

The mean is normalized. Every original residue is one, the complete
product includes j=0 and the denominator angle 1/u, and the same
displacement vector serves every angular and spatial observation.

For a nonzero complex polynomial p(v)=sum_(k=0)^N p_k*v^k set

    C_r(p)=sum_(k=0)^N |p_k|*A^k,
    J(u,p)=|sum_(a in Z) W_a(u)*p(a)|/[R*C_r(p)].

For an integer 1<=K<=M let P_K consist of every such polynomial
vanishing at at least K distinct nodes of Z, and define

    B_K=sup_(|u|=1, p in P_K) J(u,p).

There is no bound on N, no prescribed retained block, and no symmetry
or sign condition on p. Extra factors, repeated zeros, and choices of
p and of its discarded nodes depending on u or on the displacement
vector are permitted. C_r is specifically the displayed coefficient
norm about v=0; other observation costs are not identified with it.

## Conclusion

Each J(u,p) is a valid lower certificate for V. Uniformly over the
entire displacement cube and all polynomials in the indicated class,

    0 <= B_K <= V,
    B_K <= [n/(3R)]*exp(91*n/5000+3)*48^(-K).          (1)

If K>=n/90, then the certified lower value satisfies

    B_K/[n*exp(-n/48)*sqrt(D)]
                   < 5*exp(-79*n/30000) -> 0.          (2)

Consequently this coefficient-norm polynomial dual, when it discards
at least ceil(n/90) nodes, cannot establish the approved uniform lower
bound with any fixed c>0 and onset. This holds even after optimizing
the full signed angular response and every additional polynomial
factor. It is an upper bound for this certified lower value, not an
upper bound for V or an admissible countersequence to the norm target.

This method-specific negative result is unaudited. It does not stop
polynomials discarding fewer nodes, filters retaining all nodes,
rational duals, other observation norms, joint signed estimates, or
the full-H route. L686's sparse-support result remains intact. L683's
transfer audit, H/support, actual-Xi realization and all-degree signs
remain separate. No RH candidate or certified originality is claimed.

## Proof

### 1. Scope, standard input, and the local comparison

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-inner-spatial-rational-response.md`.
The intermediate test is a combined-block certificate for exactly its
joint norm target. L666 supplies the exact admissibility and geometry;
only the audited envelope (3) from L661 is used for the angular weights.

The sole analytic import is the standard maximum modulus principle:
a function holomorphic on a neighborhood of a closed disk has modulus
at every interior point at most its boundary maximum. Below it is
applied to an explicit polynomial after removable zeros are canceled.
The moment extraction is a finite linear combination of coefficients
of a uniformly convergent geometric series; its normalization is
proved directly. No general rational coercivity or new sampling
theorem is asserted or reproved.

The local comparisons checked L650's conclusion, L670/L671's exact
certificates, L686 and its recorded single-anchor limitation. L650
uses a different projected norm and an exponentially close two-node
example; it expressly allows its joint combination to escape that
individual-dual stop. L670/L671 concern angular polynomial clearing
and Mahler transfers. L686 extracts one anchor from a finite replacement
response and subtracts an undisplaced remainder. Here arbitrary
retained blocks and extra polynomial factors are allowed, and there is
no undisplaced-error subtraction. These earlier stops are comparisons,
not mathematical premises of (1)--(2). The reviewed rational norm
inequalities do not give the original-D lower bound sought here.

This is an explicit specialization of elementary disk zero removal,
not a new maximum principle. Its new local content is the uniform cost
and threshold for this family and certificate; the bounded literature
comparison does not establish originality.

### 2. The exact coefficient cost yields a lower certificate

Fix |u|=1 and a displacement vector. L666 gives |a|<R for every
a in Z. Thus F(u,r*zeta) is holomorphic on a neighborhood of the
closed unit disk and, uniformly for |zeta|<=1, has the series

    F(u,r*zeta)=sum_(k>=0) f_k(u)*zeta^k,
    f_k(u)=R^(-1)*A^(-k)*sum_a W_a(u)*a^k.             (3)

Indeed |r*a/R|<r<1, and there are finitely many a. Termwise
integration on the unit circle is therefore justified, and elementary
Fourier orthogonality gives

    f_k(u)=mean_theta F(u,r*exp(i*theta))*exp(-i*k*theta),
    |f_k(u)|<=max_(|zeta|=1)|F(u,r*zeta)|<=V.

Using the finite degree of p, equation (3) now gives the exact identity

    sum_a W_a(u)*p(a)=R*sum_(k=0)^N p_k*A^k*f_k(u).

The triangle inequality bounds its modulus by R*C_r(p)*V.
Since C_r(p)>0 for p!=0, J(u,p)<=V. Taking a supremum proves
the first line of (1). No assertion that the coefficients f_k can
be separately maximized with a common phase is needed.

### 3. Every discarded node has a uniform disk cost

Choose any K distinct zeros b_1,...,b_K of p in Z. Set

    beta_b(v)=A*(v-b)/(A^2-conjugate(b)*v).

Its denominator is nonzero for |v|<=A, since |b|<R<A.
On |v|=A, direct expansion gives
|A*(v-b)|=|A^2-conjugate(b)*v|, so |beta_b(v)|=1.
The function

    H_p(v)=p(v)/product_(j=1)^K beta_(b_j)(v)
          =[p(v)/product_j(v-b_j)]
                         *product_j(A^2-conjugate(b_j)*v)/A^K

is a polynomial. Distinctness of the b_j and their being zeros of p
justify the division, even if p has larger multiplicities or degree.
On |v|=A it satisfies |H_p(v)|=|p(v)|<=C_r(p). The maximum
modulus principle therefore gives, for each a in Z,

    |p(a)| <= C_r(p)*product_j |beta_(b_j)(a)|.          (4)

For a equal to a discarded node both sides have the required zero;
the canceled-polynomial identity justifies (4) there as well.

L666 gives Re(a)=x and |Im(a)|<9/20. Hence, for any a,b in Z,

    |a-b|<9/10,       |a|,|b|<R,
    |beta_b(a)| <= A*|a-b|/(A^2-|a|*|b|)
                < [(44)*(9/10)]/[1936-121/64]
                 =12672/618915 < 1/48.                (5)

The last comparison is the integer inequality
48*12672=608256<618915. In particular (4) implies

    |p(a)| <= C_r(p)*48^(-K)                           (6)

at every retained node, and it remains true at the discarded nodes.
This bound does not assume a block shape or positive values of p(a).
Extra polynomial factors cannot evade (6), since they were retained
in H_p and in the full boundary cost C_r(p).

### 4. The angular maximum cannot recover this cost

L661's audited envelope (3), applicable by L666's admissibility, is

    |W_a(u)|<=exp(91*n/5000+3)

for every node and every |u|=1. Apply it and (6) to the exact signed
sum defining J. There are M=n/3 original unit-residue terms, so

    J(u,p) <= [M/R]*exp(91*n/5000+3)*48^(-K).

This proves the second line of (1) after taking the supremum over
u,p. The triangle inequality here is an upper bound on a certificate,
not an attempted lower bound on the actual signed response. It thus
retains the validity of the obstruction regardless of cancellation.

The anchor W_x=1 contributes exactly 1/(U-d^2)=64/21 to D;
all other diagonal summands are nonnegative. Consequently

    B_K/[n*exp(-n/48)*sqrt(D)]
      <= [exp(3)*sqrt(21)/33]
                       *exp((91/5000+1/48)*n)*48^(-K). (7)

For completeness, log 48>15/4 can be established without numerical
rounding. The exponential series gives

    exp(1)<=5/2+(1/6)*sum_(j>=0)4^(-j)=49/18<11/4,
    exp(1/4)>5/4,
    exp(15/4)=exp(1)^4/exp(1/4)<14641/320<48.

For K>=n/90 this yields K*log48>n/24. The exponent in (7) is
therefore strictly less than

    (91/5000+1/48-1/24)*n = -79*n/30000.

Also exp(3)<27 and sqrt(21)<5, so exp(3)*sqrt(21)/33<5.
This proves (2), uniformly in all displacement vectors and polynomial
choices, without any asymptotic approximation to W or D.

The direction of the conclusion matters: B_K<=V and a small upper
bound for B_K say nothing about an upper bound for V. The general
joint norm target and the downstream gaps thus remain unresolved.
No numerical experiment or mathematical script is a proof premise.

## Mathlib

Full matching coverage of this family-specific polynomial-dual
obstruction has not been checked. The supporting mathematics consists
of the standard maximum modulus principle, polynomial factorization
at distinct roots, geometric-series coefficient extraction, and
elementary exponential estimates. L661 retains its audited-envelope
and source qualifications; L666 supplies the stated family geometry.
No matching named Lean theorem or formal verification is claimed.
Unknown coverage is not evidence of absence.
