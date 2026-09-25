# L009 — Riccati divisors and the obstruction to unfiltered counts

## Hypotheses

Let F be a finite field of odd characteristic p, and let a,b,c,d be
polynomials over F with a,b nonzero. For an integer k>=1, let

\[
 \mathcal S_k=\{P\in F[X]:\deg P<k,\quad
                 aP'+bP^2+cP+d=0\}.
 \tag{1}
\]

The zero polynomial is allowed, and P' is the ordinary formal derivative.
This is a set of polynomial solutions before agreement filtering. No
hypothesis places a full RS list inside it. When comparing to a code,
use distinct evaluation points and the simultaneous column convention in
the [pinned model](../foundations/02-pinned-list-model.md).

## Conclusion

If S_k contains two distinct elements, fix P_0,P_1 and set

\[
 D=P_1-P_0,\qquad C_0=2bP_0+c,\qquad
 \mathcal L(V)=aV'-C_0V.
\]

If the polynomial homogeneous kernel of L is zero, S_k has exactly
these two elements. Otherwise let g be its minimal monic generator,
as in L008, and put

\[
 \phi=Dg,\qquad W=D^2g,\qquad r=\phi'.
 \tag{2}
\]

Then a r=-bW, so r is nonzero. All solutions other than P_0 are in
bijection with the following admissible monic divisors T of W. Define

\[
 M=\frac{T'}r,\qquad N=T-\phi M.
 \tag{3}
\]

Require M to be a polynomial in F[X^p], require N to be nonzero, and
require the monic gcd of M,N to be 1. The condition N in F[X^p] then
holds automatically. Finally require

\[
 P_T=P_0+D-\frac WT M
 \quad\hbox{to have degree less than }k.
 \tag{4}
\]

There is no requirement to take a pth root of a coefficient. These
conditions are a complete polynomiality and degree test on the
rational parameter; they retain factors with multiplicity divisible by p.
If W is a nonzero constant times product_i pi_i^(e_i), with distinct
monic irreducibles pi_i, then, in this nonzero-kernel case,

\[
 |\mathcal S_k|\le\tau_F(W):=\prod_i(e_i+1)
 \le 2^{\deg W}
 \le 2^{2(k-1)+(p-1)\deg a}.
 \tag{5}
\]

The cases with fewer than two solutions need no parametrization.
Thus max(2,2^(2(k-1)+(p-1)deg a)) is a uniform bound on the entire
set in (1). It is independent of |F|, but is generally exponential
in the relevant degrees, even when p is fixed.

There is no replacement of this unfiltered bound by a polynomial in
k and deg a uniform over fields of a fixed odd characteristic. More
precisely, fix p and s>=2, set Q=p^s, and let F contain E=F_Q. The
single equation

\[
 A P'+P^2+P=0,\qquad A=X^Q-X
 \tag{6}
\]

has at least p^(floor(s/2) ceil(s/2)) distinct polynomial solutions
of degree less than Q. For every F_p-subspace V of E, one such solution is

\[
 H_V=\prod_{v\in V}(X-v),\qquad
 P_V=A\frac{H_V'}{H_V},\qquad
 \deg P_V=Q-|V|.
 \tag{7}
\]

The number in (6) exceeds every fixed power of Q as s grows.
These degree bounds can also be realized with the power-of-two message
dimensions and smooth domains of any of the four pinned rates, after
choosing a suitable finite extension field. This does **not** assert
that these solutions agree with a single received word in k or more
columns. It is an obstruction to counting all solutions before imposing
agreement, not a large-list witness or a disproof of the prize target.

For any unfiltered bound B used independently in m rows, B^m<=epsilon* q
would still be needed to certify that family's contribution by this
method. An exponential sufficient field condition does not follow from
the source's weaker existence proviso. Neither (5) nor (7) determines
the sharp list boundary or a controlled cover for a general interpolant.

## Proof

**Reciprocal differences and the rational kernel.** Subtract the equation
for P_0 from that for P=P_0+U. The resulting identity is

\[
 aU'+C_0U+bU^2=0.
 \tag{8}
\]

For nonzero U, setting V=1/U in F(X) gives

\[
 aV'-C_0V=b.
 \tag{9}
\]

Conversely, every rational solution V of (9) is nonzero, since b is
nonzero. Its reciprocal satisfies (8). In particular V_1=1/D is a
particular solution of (9).

Any rational homogeneous solution h=u/v can be multiplied by v^p to
produce the polynomial homogeneous solution u v^(p-1): the derivative
of v^p is zero, and the product rule applies to L. Thus a zero
polynomial kernel implies a zero rational kernel. Equation (9) then
has only V_1, and the only original solutions are P_0 and P_1.

In the other case, L008 gives a minimal monic polynomial g with
L(g)=0 and deg g<=(p-1)deg a. Every rational homogeneous solution h
has (h/g)'=0. The rational-constants argument proved in L008 says
precisely that a reduced fraction with derivative zero has numerator
and denominator in F[X^p]. Consequently the rational homogeneous
kernel is g F(X^p), and all solutions of (9) have the unique form

\[
 V=\frac1D+gH,\qquad H\in F(X^p).
 \tag{10}
\]

Applying (8) to D and L(g)=0 to g gives

\[
 a(Dg)'=(-C_0D-bD^2)g+D(C_0g)=-bD^2g.
 \tag{11}
\]

Since a,b,D,g are nonzero, (11) proves that r is nonzero.

**The exact pole-cancellation condition.** Write H=M/N as a reduced
polynomial fraction with M,N in F[X^p] and N nonzero. If H=0, use
M=0,N=1. Such a reduced representation exists by the same
rational-constants argument, not just by formally naming a constant
field. Put T=N+phi M. Equation (10) reads

\[
 V=\frac{T}{DN},\qquad U=\frac{DN}{T}.
 \tag{12}
\]

Here T cannot vanish. Indeed its derivative is r M; if T=0, then
M=0 because r is nonzero, and T=N would contradict N nonzero.
Also gcd(T,M)=gcd(N,M)=1. The identity

\[
 DN=D T-WM
 \tag{13}
\]

now gives the equivalence

\[
 U\in F[X]\quad\Longleftrightarrow\quad T\mid DN
 \quad\Longleftrightarrow\quad T\mid W.
 \tag{14}
\]

For the forward direction in the last equivalence, T divides WM by
(13), so coprimality with M forces T to divide W. The reverse
direction follows directly from (13). Polynomial divisibility is over
F, so (14) also rules out finite poles whose roots lie only in an
extension. It is stronger than testing denominators at evaluation
points. A polynomial U may still have a pole at infinity; its permitted
order is imposed by the degree condition in (4).

Scale M,N,T by the inverse of the leading coefficient of T so that
T is monic. This leaves H and U unchanged and preserves coprimality.
Since M'=N'=0, differentiation forces T'=rM, which is exactly (3).
Thus each monic divisor T determines at most one solution. Conversely,
suppose T is a monic divisor satisfying the stated tests. The condition
M in F[X^p] implies M'=0, and (3) then implies

\[
 N'=T'-rM-\phi M'=0.
\]

Coefficientwise differentiation implies N in F[X^p]. The fraction
H=M/N belongs to F(X^p), so (10) solves (9). Equations (12)--(14)
give the polynomial U=D-(W/T)M, nonzero because D,N,T are nonzero.
Its reciprocal satisfies (9), so P_T satisfies (1). The degree test
is precisely the remaining condition for membership in S_k.

Finally, two admissible divisors yielding the same P give the same
U,V,H. Two reduced polynomial representations of H differ by a
nonzero scalar, including the case H=0. Their corresponding monic T
must therefore coincide. This proves the asserted bijection.

**Counting and the field comparison.** There are exactly tau_F(W)
monic divisors, by unique factorization in F[X]. The monic associate
T=phi/lc(phi) is one of them, since phi divides W. In (3) this gives
M=1/lc(phi) and N=0, so it is not admissible. Adding P_0 to all
admissible divisors therefore still leaves at most tau_F(W) solutions.
For each positive integer e, e+1<=2^e. Also every nonconstant
irreducible has degree at least one. Hence

\[
 \tau_F(W)\le 2^{\sum_i e_i}\le 2^{\deg W}.
\]

The identity deg W=2 deg D+deg g, the bound deg D<=k-1, and L008's
bound on g complete (5). This bound counts all solutions, so taking
its mth power bounds all tuples with rows in this set, before any
simultaneous agreement restriction. It does not put a full code list
inside the set. Even when that containment holds, this method still
requires B^m<=epsilon* q for the original given field.

**A superpolynomial family in fixed characteristic.** Every element of
E=F_Q is a root of A=X^Q-X, and A'=-1. Thus A is the product of the
distinct factors X-v over v in E. In particular H_V divides A.

We verify that H_V is a linearized polynomial, meaning a sum of
monomials c_i X^(p^i). For V={0}, H_V=X. Inductively suppose this
holds for a subspace V and choose u outside V. A linearized polynomial
is additive and F_p-linear, by the Frobenius identity. Thus

\[
 H_{V+F_pu}(X)=\prod_{j\in F_p}H_V(X-ju)
 =H_V(X)^p-H_V(u)^{p-1}H_V(X).
 \tag{15}
\]

The product identity follows from product_j(Z-j)=Z^p-Z and scaling;
H_V(u) is nonzero since u is not a root. Formula (15) is again
linearized. Its coefficient of X is the old nonzero coefficient
multiplied by -H_V(u)^(p-1), so induction also proves H_V' is a
nonzero constant. In particular H_V''=0.

Consequently P_V in (7) is a nonzero polynomial of degree Q-|V|.
Calculating first in the rational function field gives

\[
 A P_V'-A'P_V+P_V^2
   =A^2\frac{H_V''}{H_V}=0.
 \tag{16}
\]

Since A'=-1, this is exactly (6), now an identity of polynomials.
The zeros of P_V in E are precisely E minus V: A/H_V has those
simple roots and H_V' is a nonzero constant. Distinct subspaces
therefore yield distinct polynomials.

To count enough subspaces, put t=floor(s/2) and write the vector
space E over F_p as U direct-sum Z with dimensions t and s-t. The
graphs of all linear maps U -> Z are distinct t-dimensional subspaces.
There are p^(t(s-t)) such maps, by their (s-t)-by-t matrices.
All resulting P_V have degree Q-p^t<Q. For fixed p,
t(s-t)>= (s^2-1)/4, whereas the base-p logarithm of any fixed
polynomial bound C Q^j is log_p C+j s. This proves the claimed
superpolynomial growth, with no numerical extrapolation.

For compatibility of the degree examples with the pinned parameters,
choose the least power of two k>=Q and let n=ell k for any
ell in {2,4,8,16}. Then Q<=k<2Q, so deg P_V<k, deg a=Q=O(n),
and n is a power of two. Because p is odd, choose an extension
F=F_(p^u) with u divisible by both s and the multiplicative order of
p modulo n. The standard finite-field existence and subfield theorem
places E in F; cyclicity of F's multiplicative group supplies a
subgroup of order n. This is a pinned smooth evaluation domain.
Multiplying u further can ensure epsilon* |F|>=1 for any fixed
positive epsilon*. No comparison of the filtered list with epsilon* |F|
is inferred from this extension construction. The number of raw
solutions remains superpolynomial in n because n is within a fixed
factor of Q.

The equation (6) has first derivative order one, total degree two in
the dependent variables, and X-degree O(n). The obstruction therefore
already occurs in the simple nonlinear class tested here. It rules
out a polynomial bound on all its polynomial solutions. It does not
rule out a useful geometric overcover with subsequent agreement
filtering, a weighted agreement count, or a different general-interpolant
argument. It supplies no lower bound for a list around one center.

`python3 scripts/riccati-families/verify.py` checks the classification
against exhaustive small solution sets, and checks (7) on explicit
subspaces in F_9 and F_81. Its finite results are retained in
`scripts/riccati-families/results.json`; the arguments above prove the
general statements.

## Mathlib

Full divisor parametrization and superpolynomial unfiltered family:
**not checked** in Mathlib. Supporting rational derivative constants,
polynomial factor counts, finite-field subfields and cyclicity, and
linearized polynomials: **not checked** in this step. L008 supplies
the rational-constants and minimal-generator arguments used here;
the special subspace identities and count are proved above. The
finite-field existence and subfield theorem and cyclicity of finite
field multiplicative groups are standard named supporting results,
not matches for the full statement. No matching library theorem or
novelty claim for the Riccati substitution is asserted.
