# C020f — Source-dual detuning test and its limited obstruction

## Hypotheses

Use C020e's exact integer-d scales, coefficients, own heat times, witness
prime pairs, floors and translated indicators. In particular X tends to
infinity, q=log X, B=(sqrt(2)-1)X, L=floor(X^(1/1000)), R=L^4,
K=ceil(X^3), J=[X,sqrt(2)X], and lambda=vr/(ns). No selected-slice
estimate from C019y or C020a/b, actual-P contract or RH assumption is
used. Every constant below is uniform beyond an absolute integer onset.

The real phase below leaves **all** complex heat factors in the
amplitude. A critical point of this phase is not a critical point of
the argument of the entire complex integrand.

## Conclusion

For l=1,...,K, the k=-l integral in C020e has phase
\[
 \Phi_l(Z,y)=Z\log(Z/(2\pi))-Z-\pi/4-Z\log(\lambda y)+2\pi l y.
 \tag{1}
\]
Its source critical point and the phase restricted to that point are
\[
 y_l(Z)=Z/(2\pi l),\qquad
 \Phi_l(Z,y_l(Z))=Z\delta_l-\pi/4,\qquad
 \delta_l=\log\frac{lns}{vr}.
 \tag{2}
\]
Joint stationarity is exactly lns=vr, subject to the true domain.
The Hessian of (1) has determinant zero, even away from resonance.
These are exact identities, not a stationary-phase asymptotic.

There are explicit unequal-product tuples for **every** witness v,
with n=1, s=7, r in {4,5,6}, and 7l-vr in {1,-1}, such that
\[
 4<y_l(Z)<45<N(Z)\quad(Z\in J),\qquad
 4< X|\delta_l|<26.
 \tag{3}
\]
Their four-taper coefficients are nonzero eventually. Hence an
unequal integer product does not supply a height oscillation parameter
tending to infinity, even at strictly interior source critical points.
Nevertheless the **entire contribution of this particular family**,
including both translated amplitudes, is O(B)=o(Bq^2).

The full unequal-product layer with 0<|delta_l|<=100/X remains unpaid.
The explicit expression (6) below retains it with both boundaries; the
available absolute estimate established here is only
\[
 |\mathcal E_{\rm near}|\le C X^{3/2}R(1+\log R)^2.
 \tag{4}
\]
This envelope, divided by Bq^2, has scale X^(1/2)R and does not tend
to zero. It is **not** a lower bound. Neither a nonzero main term nor
failure of the desired total o(Bq^2) remainder is proved. The test
stops only deletion of all unequal products on the ground that they
are uniformly rapidly nonstationary in height.

## Proof

### 1. Check the inherited expression at its load-bearing uses

C020c (5) has kappa=m lambda. Its second exterior source phase is
m^(ih) exp(-ih log(m lambda))=lambda^(-ih). Conjugating that entire
term inside the real part therefore gives C020e's lambda^(ih) factor
and the same f_Z(m) as in its first term. The domains remain D0 and
D1 separately; no equality of complex channels or domains is used.

C020e's y-derivatives follow by writing
A=-1/2-iZ-t(u-log y)/2-i pi t/8. Then f'=f A/y and
f''=f(A^2-A+t/2)/y^2. C019's audited scales imply Q_Z(N)<=CX^2.
At integer endpoints the 1/k boundary terms of the Fourier integrals
cancel between k and -k; the remaining pair is bounded by
Q_Z(N)/(2 pi^2 k^2). Thus the imported symmetric finite-Poisson
identity and C020e's outer coefficient mass
O(X^(3/4)R(1+log R)^2) give a tail O(X^(15/4)R(1+log R)^2/K).
At K=ceil(X^3) this is O(X^(377/500)q^2)=o(B).

This checks the conjugation, phase convention and truncation needed
here. The imported identity is J.-H. Evertse, *The functional equation
for the Riemann zeta function*, Chapter 9, Section 9.1, Theorem 9.2,
printed p.128, with Theorem 9.1's endpoint proof, pp.125--127,
https://pub.math.leidenuniv.nl/~evertsejh/ant13-9.pdf (undated
author-hosted file, inspected in review1422). It applies to f holomorphic
near [1,N], integers 1<N; C020e verifies that hypothesis and treats
N=0,1 separately. We reuse it, rather than reprove it. This scoped
check does not certify other estimates in C019y's numerator.

### 2. Stationarity and an explicit nonresonant family

Differentiate (1):
\[
 \Phi_Z=\log\frac{Z}{2\pi\lambda y},\qquad
 \Phi_y=-Z/y+2\pi l,\qquad
 \nabla^2\Phi=\begin{pmatrix}1/Z&-1/y\\-1/y&Z/y^2\end{pmatrix}.
 \tag{5}
\]
Its determinant is zero. Substituting y=Z/(2 pi l) gives (2),
including the constant -pi/4. For l=lambda, each portion of that
curve lying in the source domain is stationary; this is not an
isolated nondegenerate two-variable critical point. The source second
derivative is positive, so one-variable source stationary phase is
not excluded. For k>=0 the source derivative -Z/y-2 pi k is negative;
their integrals and endpoints are retained, not set to zero.

Eventually p,b>7, so v is invertible modulo 7. Let a in {1,...,6}
be its inverse, and put r=max(a,7-a), s=7, n=1. Then r is 4,5 or 6.
Choose sigma in {1,-1} so vr is congruent to sigma modulo 7, and set
l=(vr-sigma)/7. This is a positive integer <=K eventually, and
7l-vr=-sigma, never zero. Since X/100<=v<=X/25,
\[
 \frac{X}{175}-1<l<\frac{6X}{175}+1.
\]
Consequently y_l is between limits 175/(12 pi)>4 and
175 sqrt(2)/(2 pi)<40, uniformly in Z in J. The relaxed bounds in
(3) follow beyond one onset, since N(X) tends to infinity.
The n=1 entry condition holds on both respective translated bands.

Here delta_l=log(1-sigma/(vr)). The elementary bound
log(1+z)=z+O(z^2), uniform for |z|<=1/2, gives
X|delta_l|=X/(vr)+O(1/X). Since 25/6<=X/(vr)<=25, (3) follows.
Thus the height phase varies by at most 26 sqrt(2) on the whole band,
independently of X. No asymptotically growing oscillation parameter
can be inferred from the inequality lns!=vr alone.

For fixed j, as L tends to infinity and h tends to zero, the finite
four-factor coefficient c_j tends to the j-th coefficient of zeta^(-2).
This follows term by term from its definition, entirely in Re(s)>1.
The local Euler factor is (1-z)^2; hence the limits for j=4,5,6,7
are 1,-2,4,-2 respectively. All coefficients used in this family are
nonzero eventually. This does not assert that the sum of the two
translated amplitudes is bounded below or has a fixed sign.

### 3. Retain the precise unpaid layer and every complement

Define the finite source integral, with its heat factor unchanged,
\[
 I_l(Z)=\int_1^{N(Z)} y^{-1/2}E_y(Z)
                              e^{-iZ\log y+2\pi i l y}\,dy.
\]
Write Omega exactly as C020e (1). The unpaid layer is
\[
 \mathcal E_{\rm near}=2\operatorname{Re}
 \sum_{n,v,r,s}\frac{c_r\overline{c_s}}{\sqrt{nvrs}}
 \sum_{\substack{1\le l\le K\\0<|\log(lns/(vr))|\le100/X}}
 \int_J e^{2i\theta(Z)}\lambda^{-iZ}\Omega_{nvrs}(Z)I_l(Z)\,dZ.
 \tag{6}
\]
All n<=N*, all r,s<=R and every original witness v are included.
No gcd, sign or coefficient restriction is inserted. Both n-entry
indicators and both translated bands stay in Omega; the exact floor
N(Z) is retained in I_l. The heat factors are not frozen at a saddle.

To describe exactly what is left, partition C020e's finite expression
into its half-lattice endpoints, its k=0,...,K modes, and its negative
modes. Partition the latter into delta_l=0, (6), and |delta_l|>100/X.
These disjoint pieces, plus C020e's o(B) tail, equal M. No piece is
discarded, and the delta_l=0 piece has not been evaluated as a main
term. This bookkeeping isolates an unpaid expression; by itself it
is not progress toward the required asymptotic.

### 4. Quantitative limits of pointwise bounds

For a dyadic source interval y in [Y,2Y] intersected with [1,N(Z)],
the real source phase has second derivative Z/y^2>=cX/Y^2.
The standard integral second-derivative estimate gives a primitive
bounded by CY/sqrt(X). The precise known input is Kösters,
*On the Occurrence of the Sine Kernel in Connection with the Shifted
Moments of the Riemann zeta function*, arXiv:0803.1141v2, Appendix A,
Lemma A.2 (=Titchmarsh, second edition, Lemma 4.4),
https://arxiv.org/html/0803.1141v2#A, inspected in review1410 and
already used by C019/C020c. Its real C2 phase has a second derivative
of constant sign and magnitude at least epsilon. Those hypotheses
hold here, including on clipped dyadic intervals, uniformly in l.

For g(y)=y^(-1/2)E_y(Z), the exact derivative is
g'=g[-1/2-t(u-log y)/2-i pi t/8]/y. C019's scales give
|g|<=CY^(-1/2) and integral |g'|<=CY^(-1/2) on each dyadic piece.
Partial summation therefore bounds that piece of I_l by
CY^(1/2)/sqrt(X). Summing the geometric series through N*=O(sqrt(X))
gives |I_l(Z)|<=CX^(-1/4), with no assumption about saddle location.

For each tuple the number of positive integers with
|log(l/lambda)|<=100/X is at most C(1+lambda/X). Indeed the enclosing
interval has length 2 lambda sinh(100/X)<=C lambda/X for X>=100.
Using |c_j|<=tau(j), C019's coefficient bound, and the elementary
witness comparison with integer pairs gives
\[
 \sum_{n,v,r,s}\frac{|c_rc_s|}{\sqrt{nvrs}}
       (1+\lambda/X)
 \le C\{X^{3/4}R(1+\log R)^2
                +X^{1/2}R^{3/2}(1+\log R)\}
 \le C X^{3/4}R(1+\log R)^2.
 \tag{7}
\]
For the second summand, use sum n^(-3/2)<=C,
sum_v sqrt(v)<=CX^(3/2),
sum_r |c_r|sqrt(r)<=CR^(3/2)(1+log R), and
sum_s |c_s|s^(-3/2)<=C. The last bound follows from
sum tau(s)s^(-3/2)=(sum a^(-3/2))^2<infinity. Finally
R^(1/2)<=X^(1/500) makes the second summand no larger than the first
beyond one onset. Since |Omega|<=C, multiplying (7) by |J| and
CX^(-1/4) proves (4). Its failure to reach o(Bq^2) is only failure
of this absolute estimate, not evidence of the size of the signed sum.

For the particular family in Section 2, l>=X/175-1. On [1,80],
the same second-derivative/variation argument gives O(X^(-1/2)).
On [80,N(Z)] the phase derivative satisfies
2 pi l-Z/y >=(2 pi/175-sqrt(2)/80)X-2 pi>=cX>0 eventually.
It is increasing. Integration by parts gives O(X^(-1)): the boundary
term is O(X^(-1)); integral |g'|<=C; and
integral phi''/(phi')^2<=1/phi'(80)<=C/X bounds the remaining term.
Thus |I_l|<=CX^(-1/2). This holds separately at every floor value.
There is one tuple per v, all c_r,c_s are bounded for these fixed
indices, and sum_v v^(-1/2)<=CX^(1/2). Its complete outer integral
is therefore at most C X * X^(-1/2) * X^(1/2)=CX=O(B).
No distribution theorem for primes or cancellation is needed for
this upper bound. In particular this explicit family is not a
counterexample to the proposed total remainder.

### 5. Decision and qualifications

The inspected Kıral--Petrow--Young uniform stationary-phase theorem
concerns smooth dyadically supported inert weights; see *Oscillatory
integrals with uniformity in parameters*, JTNB 31(1) (2019),
Definition 2.1, Main Theorem (3.1)--(3.2), pp.147--149, and
Lemma 3.1, p.150, https://www.numdam.org/item/10.5802/jtnb.1072.pdf .
It does not pay the present sharp boundaries or the signed outer sum.
The calculation above shows concretely why the unequal-product
condition also cannot provide a growing nonstationary height
parameter for all retained interior tuples. No invalid application
of that theorem has been used to obtain a bound here.

This bounded test has not produced the required signed main term.
Expression (6), the other retained modes, the two half-lattice
endpoints and both translated source boundaries remain. C019y's
O(G,J), UA, denominator, E_P and actual-P contracts are separate
obligations. Stops1417/1419 retain their original scopes. Neither
the fixed witness nor source Poisson in general is refuted; actual-Xi
all-degree positivity and RH remain open. This is standard calculus
and pointwise-bound development under assessment1424, not a claimed
advance beyond the checked literature. Independent audit is pending.

## Mathlib

Full matching coverage of this moving-heat, sharp-floor signed sum
has not been checked. No absence or formal verification is claimed.
The finite Poisson and second-derivative inputs are the precisely
cited standard results above; the joint-phase calculation and all
specialization bounds are written out here.
