# Lemma 806: exact scope of the theta Gaussian derivative-sign premise

## Hypotheses

Use L019/L021's theta kernel K and moments

\[
 m_j=\int_0^\infty u^{2j}K(u)\,du,\qquad
 d\mu(u)=K(u)\,du/m_0,
\]

and let nu be the pushforward of mu under v=u^2, as in L795.
For integers n>=1 and d>=0, and real x>=0, put

\[
 A_d=\frac{d!}{(1/2)_d}>0,\qquad
 f_{d,x}(v)=A_d L_d^{(-1/2)}(vx/4).
\]

The Laguerre convention and rising factorial are those of L795.
Let v_1,...,v_n and w_1,...,w_n be the nodes and weights of
the n-node Gaussian rule for nu. Write

\[
 q_n(v)=\prod_{i=1}^n(v-v_i),\quad
 h_n=\int q_n(v)^2\,d\nu(v),\quad
 Q_{n,d}(x)=\sum_{i=1}^n w_i f_{d,x}(v_i),\quad
 E_{n,d}(x)=P_d(x)-Q_{n,d}(x).
\]

Here P_d is exactly L795's normalized theta average. Gaussian
orthogonality concerns the variable v and the measure nu, not P_d.

## Conclusion

The rule exists, its nodes are distinct and strictly positive, its
weights are strictly positive, and 0<h_n<infinity. For x>0 the
whole-support classification of the ordinary derivative is:

1. If 0<=d<2n, then partial_v^(2n) f_{d,x}=0 identically and
   E_{n,d}(x)=0 by polynomial exactness.
2. If d=2n, the derivative is the positive constant A_d(x/4)^(2n),
   and the actual error is strictly positive:

   \[
   E_{n,2n}(x)=\frac{A_{2n}(x/4)^{2n}}{(2n)!}\,h_n>0.       \tag{1}
   \]

3. If d>2n, put k=d-2n. The derivative has exactly k simple
   positive zeros and changes sign at every one. It takes both
   signs on sets of positive nu measure. Thus it has neither a
   nonnegative nor a nonpositive whole-support sign, even after
   deleting a nu-null set. This statement does not determine the
   sign or nonvanishing of E_{n,d}(x).

There are no nonzero constant-negative-sign cases. At x=0, for
every n,d, f_{d,0}=1, its derivative is zero, and E_{n,d}(0)=0.
At the support endpoint v=0 the derivative in cases 2 and 3 is
strictly positive; no endpoint exception removes the sign changes.
The case d=0 is included in case 1.

Consequently, among degrees beyond the Gaussian exactness guarantee,
the only whole-support derivative-sign regime is d=2n, and its error
has the same positive direction
at every x>0. This premise alone supplies no alternating comparison
directions at positive root barriers. Above this threshold the premise
fails; below it the rule is exact. Neither fact excludes another
actual-weighted error argument, an exact-reference approach, or
hyperbolicity of P_d. In particular case 3 is not a claim that accidental
quadrature equality at a particular x is impossible.

## Proof

**Imported inputs and unbounded-support applicability.** L021 gives
0<m_j<infinity for every j>=0, and hence

\[
 \int v^j\,d\nu(v)=m_j/m_0<\infty.
\]

L019 and L795 show that each nonempty open subinterval of
(0,infinity) has positive nu measure. A nonzero real polynomial
has a nonzero value at some positive point, and continuity gives an
interval on which its square has a positive lower bound. Its squared
nu norm is therefore strictly positive; finiteness follows from
the finite moments. This verifies the positive-definite polynomial
inner product, with infinite support and no truncation.

Import Walter Gautschi, *Orthogonal Polynomials: Computation and
Approximation*, Oxford University Press, first edition (2004),
Theorems 1.6, 1.19, 1.45 and 1.46, pp.1-3, 7 and 21-23,
[book scan](https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf).
These results give the n-node Gaussian rule, distinct interior nodes,
positive weights, and exactness for every polynomial of degree at
most 2n-1 for this positive measure, including unbounded support.
See also NIST DLMF [3.5(v)](https://dlmf.nist.gov/3.5#v),
[3.5.18](https://dlmf.nist.gov/3.5.E18) and
[3.5.20_1](https://dlmf.nist.gov/3.5.E20_1).
The verified hypotheses apply for every fixed n, not just n=2.
In particular h_n is finite and strictly positive, and exactness
on constants gives sum_i w_i=1.

Every polynomial used below is absolutely nu integrable: its
absolute value is bounded by the finite sum of the absolute values
of its coefficients times v^j on v>=0. This includes f, its
derivatives, q_n^2, and any polynomial of degree at most 2n-1
arising below or as a Hermite interpolant. L795 therefore identifies
the integral of f with P_d without an infinite interchange.

The standard Gaussian/Hermite derivative remainder is Gautschi,
Theorem 1.48 and its corollary, pp.23-24, (1.4.10)-(1.4.16),
and DLMF [3.5.19](https://dlmf.nist.gov/3.5.E19)-
[3.5.20](https://dlmf.nist.gov/3.5.E20). Its derivative-sign premise
is the object of this test. We do not assert an extension to arbitrary
smooth nonintegrable functions on an infinite interval or need a
choice of its unspecified derivative-evaluation point. Polynomial
exactness alone will justify (1).

**Derivative and zero specialization.** Import the Laguerre identity

\[
 \frac{d}{dz}L_j^{(\alpha)}(z)=-L_{j-1}^{(\alpha+1)}(z),
 \qquad j\ge1,
\]

from NIST DLMF [18.9.23](https://dlmf.nist.gov/18.9.E23),
citing Szego (1975), (5.1.14). Iterating only while the degree is
positive, and including each chain-rule factor x/4, gives for d>=2n

\[
 \partial_v^{2n} f_{d,x}(v)
 =A_d(-1)^{2n}(x/4)^{2n}
       L_{d-2n}^{(2n-1/2)}(vx/4)
 =A_d(x/4)^{2n}L_k^{(2n-1/2)}(vx/4).                  \tag{2}
\]

For d<2n, differentiation exhausts a polynomial of degree d
(degree zero when x=0), so the derivative is zero instead; no
negative-index Laguerre polynomial is invoked. For d=2n,
L_0^(2n-1/2)=1 proves the positive-constant assertion.

For d>2n, k>=1 and the shifted parameter alpha=2n-1/2>-1.
Import the Laguerre orthogonality and zero theorem from DLMF
[Table 18.3.1](https://dlmf.nist.gov/18.3.T1) and
[18.2(vi)](https://dlmf.nist.gov/18.2#vi): for alpha>-1 the
weight z^alpha exp(-z) on (0,infinity) gives k simple positive
zeros of L_k^(alpha). This Laguerre weight is used solely for the
zero theorem, not as a replacement for nu. If the zeros are
z_1<...<z_k, equation (2) has precisely the zeros v_j=4z_j/x.
Their simplicity and the positive factor in (2) give a sign change
at each v_j.

The constant-term formula, DLMF
[18.5.12](https://dlmf.nist.gov/18.5.E12), gives
L_k^(alpha)(0)=(alpha+1)_k/k!>0. Thus the derivative is positive
at v=0 and on the first interval (0,v_1), negative immediately
after v_1, and alternates on subsequent intervals. Both the
positive and negative intervals have positive nu measure by the
full-support check. This proves the classification including the
almost-everywhere qualification, without making a claim about
the zero set or sign of the integral defining E.

**Exactness and the one constant-sign frontier.** For d<2n the
degree in v is at most 2n-1, so the imported exactness gives E=0.
For d=2n and x>0, put C=A_{2n}(x/4)^(2n)>0. Equation (2)
shows that f has leading v coefficient c=C/(2n)!. Since q_n is
monic, r(v)=f(v)-c q_n(v)^2 has degree at most 2n-1. Exactness
applied to r and q_n(v_i)=0 give

\[
 \int f\,d\nu-\sum_i w_i f(v_i)
 =c\int q_n^2\,d\nu=c h_n.
\]

All integrals are finite as checked above. This is just the
polynomial specialization of the cited Gaussian remainder, proved
by exactness to avoid any unnecessary infinite-interval mean-value
step. It proves (1), including strictness. At x=0, L795's normalized
constant term makes f identically 1, and constant exactness proves
the remaining degeneracy.

Finally, a positive error gives P_d>=Q_{n,d} at every positive
x on the frontier; it transfers positivity where Q is positive
but by itself gives no negative upper bound where Q is negative.
There is no second sign direction as x varies. Quantitative margins,
reference hyperbolicity, actual signed cancellation above the
frontier, and transfer to all-degree mixed positivity are not
established. This parks only the whole-support derivative-sign-only
mechanism, not Gaussian quadrature or RH. The classification is a
conventional specialization of the cited results, with no claim of
progress beyond those sources.

### Independent audit — 5 November 2026, step566

The complete statement and proof were replayed under the separately
approved classification-audit scope, using L019/L021/L795 and the
previously inspected primary sources. No mathematical defect or extra
hypothesis was found. This is validation of a conventional
specialization, not a new result beyond the cited theorems.

**Actual law and Gaussian applicability.** The inverse image of an
interval (a,b) with 0<=a<b<infinity under u↦u^2 contains the
nonempty interval (sqrt(a),sqrt(b)). L019's continuous positive K
makes its mu measure positive. The pushforward therefore has support
[0,infinity); it has no atom at 0. L021 gives total mass one after
normalization and every finite raw v moment. For any nonzero real
polynomial p, choose a positive point avoiding its finitely many
zeros and a smaller bounded interval on which |p|>=epsilon>0.
This proves integral p^2 dnu>0, while the moment bounds prove
finiteness. Thus the exact hypotheses of Gautschi Theorems 1.6,
1.19, 1.45 and 1.46 hold for each n, with no bounded-support or
moment-determinacy assumption. The source's node-location theorem
places the n distinct nodes in (0,infinity), and its weight theorem
gives positive weights. Applying the same norm check to monic q_n
proves 0<h_n<infinity. Polynomial exactness suffices throughout.

**Normalization and frontier coefficient, independently cross-checked.**
L795's finite expansion, before integration, is

\[
 f_{d,x}(v)=\sum_{j=0}^d(-1)^j\binom dj
                      \frac{j!}{(2j)!}v^j x^j.
\]

For d=2n and x>0 its leading coefficient is

\[
 c=\frac{(2n)!}{(4n)!}x^{2n}
   =\frac{A_{2n}(x/4)^{2n}}{(2n)!}>0.
\]

Here (1/2)_(2n)=(4n)!/[4^(2n)(2n)!]; thus the factorial in (1)
and every power of 4 agree by an independent coefficient calculation.
Subtracting c q_n^2 leaves degree at most 2n-1, agrees with f at
every node, and is absolutely integrable. Exactness gives E=c h_n,
including strict positivity. No smooth-function mean-value remainder
on an infinite interval is used or inferred.

**Exhaustive derivative and endpoint replay.** At x>0 the integrand
has degree exactly d. If d<2n, its 2n-th derivative is zero and
its integral is exact. If d>=2n, the successive source derivative
identities apply only to degrees d,d-1,...,d-2n+1, all positive.
They contribute 2n factors -x/4, ending at degree k=d-2n and
parameter alpha=-1/2+2n>-1. For k=0 this gives precisely the
positive constant in the conclusion. For k>=1, the source zero
theorem gives exactly k simple roots in (0,infinity); scaling by
4/x preserves simplicity and location. The value at zero is
A_d(x/4)^(2n)(2n+1/2)_k/k!>0. Consequently the first positive
interval and the interval immediately after the first root have
opposite signs and positive nu measure, including when k=1.
Deleting a null set cannot remove either sign. These facts concern
the derivative, and do not sign its quadrature error.

When x=0 the finite expansion is identically 1 for every d, so
constant exactness gives E=0 and the derivative vanishes. The d=0
case has the same behavior for every x. The v=0 positivity statement
for d>=2n is specifically for x>0, as in the classification; it
does not override the x=0 degeneracy. All statements cover n=1
without alteration. No negative-index Laguerre function, dropped
theta tail, numerical enclosure or interchange of infinite sums is
needed. The restriction to a derivative-sign-only mechanism survives;
no reference-root, actual higher-error-sign or mixed-positivity claim
has been added. Direct mathematical inputs remain unchanged.

**Completion of the preserved audit, step566-finalized.** The unfinished
working record and this audit were present before this invocation's
edits. Their checks were replayed against the complete L019/L021/L795
proofs and the saved primary-source hypothesis/proof-case assessments
from steps539, 543 and 544. In particular the independent coefficient
calculation above and the positive-measure intervals verify the strict
frontier and the almost-everywhere claim, respectively. All cases pass;
the earlier draft is preserved, and this completion claims validation
only, not another mathematical discovery or a new sign mechanism.

## Mathlib

Full matching coverage has not been checked. Availability in Mathlib
of the exact theta-measure Gaussian specialization, the iterated
Laguerre derivative and this regime classification is unknown. No
formal verification or absence claim is made. The citations above
are the mathematical inputs; all parameter, scaling, support,
integrability and degeneracy checks needed here are explicit.
