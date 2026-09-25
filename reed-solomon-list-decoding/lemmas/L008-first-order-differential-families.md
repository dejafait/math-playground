# L008 — First-order differential families and agreement loss at zeros

## Hypotheses

Let F be a finite field of characteristic p and cardinality q. Fix
a,b in F[X], with a nonzero, and write L(P)=aP'+bP, where the first
Hasse derivative P' is the ordinary formal derivative. All m>=1 rows
use this same homogeneous operator; the right sides c_1,...,c_m may
differ. Let x_1,...,x_n be distinct elements of F and 1<=k<=n.

For a received word y in (F^m)^n, count tuples of degree-less-than-k
polynomials satisfying L(P_j)=c_j and agreeing with y in at least A
columns, where k<=A<=n. Denote this number by M. Agreement means
simultaneous column agreement in the
[pinned model](../foundations/02-pinned-list-model.md).
No hypothesis puts the full RS list in this differential solution set.

## Conclusion

If there is no such polynomial solution tuple before agreement
filtering, M=0. If the homogeneous kernel in degree less than k is
zero, M<=1. In every other case choose one solution tuple P_0 with
degrees less than k. There is a unique monic polynomial g of minimal
degree d in the nonzero full homogeneous kernel, and

\[
 \ker L=gF[X^p],\qquad
 \{P:\deg P_j<k,\ L(P_j)=c_j\}
 =P_0+g\{(H_1(X^p),\ldots,H_m(X^p)):\deg H_j\le h\},
 \quad h=\left\lfloor\frac{k-1-d}{p}\right\rfloor. \tag{1}
\]

Here d<k. Every irreducible factor of g has multiplicity less than p,
and its squarefree radical divides a. Consequently

\[
 d\le(p-1)\deg a,
 \qquad e:=|\{i:g(x_i)=0\}|\le\min(d,|\{i:a(x_i)=0\}|). \tag{2}
\]

Let z be the number of these e columns at which P_0 equals y, and put
N=n-e and A_0=A-z. All candidates have the same values at the e
deleted columns. On the other columns, subtract P_0 and divide every
row by the nonzero g(x_i). The filtered family is exactly the degree-
at-most-h interleaved RS list on the distinct points x_i^p, requiring
A_0 agreements. In particular A_0>=1; if A_0>N then M=0. Otherwise,
when A_0^2>Nh,

\[
 M\le J_g(y,A):=
 \left\lfloor\frac{N(A_0-h)}{A_0^2-Nh}\right\rfloor. \tag{3}
\]

There is no exponent m. A bound uniform in y is obtained by replacing
A_0 with A-e in (3), provided (A-e)^2>(n-e)h. If a has no zeros on the
evaluation domain, then e=0: (3) is at least as strong as the L007
bound for the unmodified message degree k-1, whenever that bound's
denominator is positive. For general a, the columns cannot be kept
without accounting for their fixed agreement.

Here is one uniform sufficient slack, without any degree restriction
on a,b beyond the preceding hypotheses. For fixed 0<R=k/n<1 and
0<=gamma<=1-R, set

\[
 A=k+\lceil\gamma n\rceil,\qquad
 s=\sqrt{1-1/p},\qquad
 \Gamma_p(R)=\frac{1-R}{2}(1-s). \tag{4}
\]

If gamma>=Gamma_p(R), every such affine family has M<=pn. If
gamma>Gamma_p(R), the stronger constant bound

\[
 M\le\max\left\{1,\frac{1}{\gamma^2-\Gamma_p(R)^2}\right\} \tag{5}
\]

also holds. This is a sufficient cutoff, not an optimized cutoff for
each rate or equation. For pinned smooth domains p is odd, so the
single choice gamma>=(1-R)(1-sqrt(2/3))/2 gives M<=3n for every
admissible characteristic in this first-order setting.

At A=k, a uniform constant independent of n cannot be obtained merely
by extending L007 to all a,b: for any distinct evaluation domain there
is an equation with exactly n-k+1 nearby solutions in one family.
The example is proved below, and attains (3) with h=0. In particular
the full code has B_m((n-k)/n)>=n-k+1, so this radius is unsafe on
any instance with epsilon* q<n-k+1.

For a family bound B above, the required contribution M<=epsilon* q
still needs B<=epsilon* q. For example q>=epsilon*^(-1)pn suffices
in (4), while q>=3 epsilon*^(-1)n suffices at the stated common slack
for odd characteristics. A union of T controlled families yields only T B without
further information. No such cover of a general interpolant, bound on
T, or sharp boundary for the original code is asserted.

## Proof

**The rational constants and polynomial generator.** Suppose the full
homogeneous kernel is nonzero, and choose a monic g of least degree
in it. For any other nonzero homogeneous solution U, the identities
aU'=-bU and ag'=-bg imply

\[
 (U/g)'=(U'g-Ug')/g^2=0,
\]

since a is nonzero in the field F(X). Write U/g=u/v as a fraction
of coprime nonzero polynomials. Differentiation gives u'v=uv'. Thus
u divides u' and v divides v', by coprimality. A nonzero derivative
has smaller degree than its polynomial, so u'=v'=0. Coefficientwise
differentiation now shows that u,v belong to F[X^p]: precisely the
exponents divisible by p can have nonzero coefficients.

From Uv=gu and coprimality, v divides g. If v were nonconstant,
g=v w and v'=0 would give 0=L(g)=vL(w). This would produce a nonzero
homogeneous solution w of smaller degree, a contradiction. Hence v
is constant and U/g belongs to F[X^p]. Conversely, the product rule
gives L(gH(X^p))=H(X^p)L(g)=0. This proves the kernel assertion.
Two monic solutions of the least degree differ by a nonzero constant
factor by that assertion, and their normalization makes them equal.

Any nonzero H(X^p) has degree p deg H. The exact degree formula
deg(gH(X^p))=d+p deg H proves the homogeneous cutoff. Subtracting
P_0 proves (1); translating within the vector space of polynomials
of degree less than k introduces no additional solutions. If the
truncated homogeneous kernel is zero, each inhomogeneous row has at
most one solution, proving the earlier singleton case.

**Zeros of the generator.** A nonconstant factor v in F[X^p] cannot
divide g, by the same minimal-degree argument. In particular, no
irreducible factor phi can occur with multiplicity at least p, since
phi^p belongs to F[X^p]. Write g=phi^j w with 1<=j<p and phi not
dividing w. Finite fields are perfect: Frobenius is injective, hence
surjective on F. Thus an irreducible nonconstant phi has phi' nonzero;
otherwise coefficientwise pth roots would express phi as a pth power
of a nonconstant polynomial. Irreducibility and the degree drop imply
gcd(phi,phi')=1. Therefore

\[
 g'=\phi^{j-1}(j\phi'w+\phi w')
\]

has phi-adic multiplicity exactly j-1. The equation ag'=-bg makes
phi^j divide ag', forcing phi to divide a. Applying this to every
irreducible factor proves rad(g)|a and the degree bound (2). Each
evaluation root is such a factor X-x_i. This proves the remaining
assertions in (2), including when g is constant.

**Shortening and counting.** At a zero of g every candidate has value
P_0, so exactly z of those columns agree with y for every candidate.
At each remaining column, (1) gives the equivalent conditions

\[
 H_j(x_i^p)=\frac{y_{i,j}-P_{0,j}(x_i)}{g(x_i)}
 \quad\hbox{for every row }j.
\]

Frobenius sends distinct elements to distinct elements. Also
N=n-e>=k-d>=1 and h<k-d<=N. Thus the shortened polynomial evaluation
is injective. As A>=k and z<=e<=d<k, A_0>=1. If A_0>N, agreement
is impossible. Otherwise apply L007 on the N remaining original
points, with message cutoff k-d, zero affine translate, and the
displayed transformed center. Its derivative-kernel family is
exactly the H_j(X^p) family in (1); its count proves (3).

For fixed N,h, the real function
f(t)=N(t-h)/(t^2-Nh) is nonincreasing for sqrt(Nh)<t<=N. Indeed its
derivative has the sign of

\[
 -t^2+2ht-Nh=-((t-h)^2+h(N-h))\le0.
\]

As A_0>=A-e, replacing A_0 with A-e therefore preserves an upper
bound whenever the latter denominator is positive. When e=0, the
remaining h is at most floor((k-1)/p). For fixed A,N the derivative
of N(A-h)/(A^2-Nh) with respect to h is
NA(N-A)/(A^2-Nh)^2>=0. This proves the zero-free comparison with L007.

**A uniform sufficient slack.** The singleton and empty cases already
satisfy (4)--(5), so consider d<k. Put c=1-R and u=(k-e)/n>0; then
N/n=c+u. The degree bound d>=e and the exact degree cutoff imply

\[
 h\le\frac{k-1-e}{p}=\frac{nu-1}{p}.
\]

Using A-e>=n(u+gamma) gives

\[
 (A-e)^2-Nh
 \ge n^2\left((u+\gamma)^2-\frac{(c+u)u}{p}\right)+\frac Np.
 \tag{6}
\]

Write Gamma=Gamma_p(R). As s^2=1-1/p and c/p=2Gamma(1+s), the
bracket in (6) is exactly

\[
 (su-\Gamma)^2+(\gamma-\Gamma)(2u+\gamma+\Gamma). \tag{7}
\]

For gamma>=Gamma this is nonnegative, so (A-e)^2-Nh>=N/p>0,
including equality in the limiting slack. Formula (3), or its
uniform version, gives M<=p(A_0-h)<=pN<=pn whenever M is nonzero.
If gamma>Gamma, (7) is at least gamma^2-Gamma^2>0. The numerator
N(A_0-h) is at most n^2, so (3) gives the constant bound in (5).
The maximum with 1 also covers a trivial homogeneous kernel. Since
p is odd on pinned smooth domains by L007, one can instead use
h<=(k-1-e)/3 throughout (6)--(7). The same argument with 3 in place
of p then gives M<=3n at gamma>=Gamma_3(R). This proves a bound
independent of the varying characteristic at that common slack;
it does not treat p as fixed while making a uniform field claim.

**An attained loss from fixed zero columns.** Select k-1 evaluation
points and put g=product_i(X-x_i) over those points. For k=1 the
empty product is 1. Take a=g, b=-g', and every c_j=0. This g is a
nonzero homogeneous solution. It is squarefree, so it has no
nonconstant divisor in F[X^p]: over the perfect field F every such
divisor is a pth power. By the kernel assertion already proved, a
monic minimal generator must divide g with quotient in F[X^p]; the
quotient must be constant. Thus g is the generator, d=e=k-1, and
h=0. All degree-less-than-k solutions are the tuples lambda g for
lambda in F^m.

There are N=n-k+1 remaining columns. Since q>=n and m>=1, choose N
distinct vectors lambda_i in F^m. Set the received column equal to
zero on the roots of g, and to g(x_i)lambda_i at each remaining
column. Each tuple lambda_i g agrees at the k-1 fixed zero columns
and at exactly its one remaining assigned column. Every other
lambda g agrees only at the fixed zero columns. The filtered list
at A=k therefore has exactly N candidates, which equals (3).
For example, n=16,k=8 in characteristic 3 gives nine candidates,
whereas the fixed derivative fiber in L007 has at most three. A
smooth domain of size 16 exists in F_81, as recorded in L007.

This example refutes only transfer of that constant bound to all
first-order equations. It is also a lower bound for the full RS list,
to be compared with epsilon* q for the specified instance. It does
not determine the sharp boundary or disprove the challenge. It shows
why the fixed columns must be counted.

The exact checks under `scripts/first-order-families/` compare finite
polynomial kernels and affine fibers, shortened agreement counts,
the uniform slack inequality, and the attained example. They test
the stated finite instances; the proof above is the general argument.

## Mathlib

Full first-order classification with the shortened agreement bound:
**not checked** in Mathlib. Supporting rational-function derivative
constants, finite-field perfection, polynomial factor multiplicities,
and polynomial module results: **not checked** in this step. The
needed elementary arguments are supplied above, and the agreement
estimate is the already proved L007 count. No matching library theorem
or novelty claim for the differential-kernel classification is asserted.
