# Corollary 997b: exponential normalization cost for a Chebyshev slope family

## Hypotheses

Use L997's exact K_(n+2), a_n(c;eta), z_0(c) and phi(c), with
A=7/4, B=9/4, r=2 and eta_0=3/4+i. All four quartet points have
multiplicity one and are hypothetical finite inputs, not actual zeta
zeros. Keep every endpoint and K's constant subtraction.

For each integer n>=20 set k=2n, h=1/(4n) and

    c_j=A+j*h, 0<=j<=k,
    R=exp(1/32), d=R*exp(i/4)*cos(1/16),
    e=i*R*exp(i/4)*sin(1/16),
    v_l=d+e*cos((2l-1)*pi/(2k)), 1<=l<=k,
    P_n(X)=product_(l=1)^k (X-v_l)/(1-v_l)
          =sum_(j=0)^k p_(n,j)*X^j.                            (18)

These are explicitly defined Chebyshev-node roots on the chord joining
R*exp(3i/16) to R*exp(5i/16). Their imaginary parts are positive, so
the denominators in (18) do not vanish and P_n(1)=1. No minimax theorem
or bound on a curved spectral arc is assumed.

Define finite complex measures on the CLOSED slope interval by

    nu_tilde_n=sum_(j=0)^k p_(n,j)
                  *exp(-i*n*(phi(c_j)-c_j/2))*delta_(c_j),
    V_n=||nu_tilde_n||_TV=sum_j |p_(n,j)|,
    J_n=integral_A^B z_0(c)^n*a_n(c;eta_0)dnu_tilde_n(c).       (19)

The atoms are distinct, including both endpoints, and their phase
factors have modulus one. The allowed family in this corollary consists
only of scalar multiples of these particular nu_tilde_n. It does not
include arbitrary atomic or arbitrary finite Borel measures.

## Conclusion

For every integer n>=20,

    |J_n|<=64*(n+2)*exp(-3n/16)*V_n.                           (20)

If J_n=0, no scalar multiple has selected value one. If J_n!=0, the
unique scalar normalization nu_n=nu_tilde_n/J_n satisfies

    ||nu_n||_TV>=exp(3n/16)/(64*(n+2)).                        (21)

Thus this degree-proportional Chebyshev atomic construction cannot meet
review312's simultaneous requirements. Indeed (21) contradicts any TV
allowance C_epsilon*exp(epsilon*n) with 0<epsilon<3/16 along unbounded
degrees for which normalization exists. No estimate for the competing
response is needed for this necessary-condition failure.

This is a local informative NEGATIVE / REPRODUCTION in step316 under
the pre-invocation EXPLORE review312. It is a standard coefficient-bound
specialization, not an imported theorem about this family, a certified
originality claim, or an all-measure obstruction. The independent step317
replay below verifies (20)-(21). Review312's general assay remains undecided;
actual reconstruction, signed forcing, infinite-zero complements,
regulator uniformity, L993 and L984(H) remain unpaid. No RH candidate.

## Proof

### Source tools, proposal and exact polynomial realization

Import the Laguerre generating function
[NIST DLMF18.12.13](https://dlmf.nist.gov/18.12.E13) through L994(6),
and the real-positive bound
[DLMF18.14.8](https://dlmf.nist.gov/18.14.E8) through L994(7):

    L_(n+1)^(2)(t)=[w^(n+1)] (1-w)^(-3)*exp(-t*p(w)),
    p(w)=w/(1-w),
    |K_(n+2)(t)|<=2*(n+2)*exp(t/2), t>=0.                    (22)

These are the inspected, unchanged contracts reused in review312 and
review291. Cauchy's coefficient formula may be evaluated on |w|=1/2:
the generating function is holomorphic for |w|<1, so the particular
radius 1/4 in L994 is not a restriction on this finite coefficient.
No Laguerre asymptotic or single oscillatory branch is substituted.
The Chebyshev-node product (18) is a definition; no general Chebyshev
extremal theorem is reproved or used to assert operator smallness.

The proposal has a specific spectral motivation. At w=i,
p(i)=-1/2+i/2. For alpha_0=eta_0-1=-1/4+i,

    exp((alpha_0-p(i)-1/4-i/2)/4)=1.

For alpha=-1/8+i*gamma, the corresponding values are

    X_gamma=R*exp(i*(gamma-1)/4), A<=gamma<=B.                 (23)

Their endpoints are precisely those of the chord used in (18).
This only motivates the trial: the full contour and the curved arc
are not replaced by that chord or by the reference point w=i.
In particular P_n(1)=1 is not the actual selected normalization.

L997(7) and the phase in (19) give the EXACT identity

    z_0(c_j)^n*exp(-i*n*(phi(c_j)-c_j/2))
                      =exp(-n*c_j/4-i*n*c_j/2).              (24)

For any complex N, putting X=exp(h*N) gives finite-sum identities

    sum_j p_(n,j)*exp(c_j*N)=exp(A*N)*P_n(X),
    sum_j c_j*p_(n,j)*exp(c_j*N)
                 =exp(A*N)*[A*P_n(X)+h*X*P_n'(X)].           (25)

They follow by expanding the displayed polynomial and its derivative.
They remain exact under finite integrals and coefficient extraction.

### Root bounds and the selected contour

Every root v_l is a convex combination of the endpoints in (23).
Using exp(x)<=1/(1-x) for 0<=x<1, |exp(i*t)-1|<=|t|, and
cos(t)>=1-t^2/2, obtain

    |v_l-1|<=1/31+5/16=171/496,
    Re(v_l)>=cos(5/16)>=487/512,
    |1+v_l|>=999/512=:D.                                    (26)

For the middle inequality, R>=1 and cos(5/16)>0; the same
lower bound holds on the whole chord. The positive imaginary parts
already gave P_n(1)=1, and (26) also excludes a root at -1. Moreover

    |P_n(-1)|<=sum_j |p_(n,j)|=V_n.                          (27)

For sigma=+1 or -1, set alpha_sigma=-1/4+sigma*i. On |w|=1/2,
p(w) lies on the circle of center 1/3 and radius 2/3, as follows
directly from |p(w)|=|1+p(w)|/2. For 0<=u<=2 let

    lambda=alpha_sigma-p(w), t=c*(n+u),
    N=(n+u)*lambda-n/4-i*n/2,
    s=1+u/n, Y=h*N=s*lambda/4-1/16-i/8, X=exp(Y).

Here 1<=s<=11/10 because n>=20. The Y circle has center
-7s/48-1/16+i*(sigma*s/4-1/8) and radius s/6. Hence, for both
signs and every point of the full w contour,

    Re(Y)<=s/48-1/16<=-19/480<0,
    |Y|<=3/16+9s/16<=129/160.                               (28)

The second estimate uses the sum of absolute real and imaginary
parts of the center, plus the radius; it does not assume Y is real.
Since exp(Y)-1=Y*integral_0^1 exp(t*Y)dt and Re(Y)<=0,
|X-1|<=|Y| and |X|<=1. Combining (26)-(28) gives, for EVERY root,

    |X-v_l|/|1+v_l|
       <=(129/160+171/496)/(999/512)
        =30448/51615<3/5=:q.                               (29)

The product in (18) and its derivative therefore satisfy

    |P_n(X)|<=q^k*|P_n(-1)|,
    |P_n'(X)|<=k*q^(k-1)*|P_n(-1)|/D.                       (30)

The derivative bound expands the derivative as a sum of k products
with one omitted factor. It does not divide by X-v_l and remains
valid when X equals a root. Since h*k=1/2, A=7/4 and |X|<=1,

    |A*P_n(X)+h*X*P_n'(X)|
      <=q^(k-1)*|P_n(-1)|*(21/20+256/999)
       <2*q^(k-1)*V_n.                                    (31)

Also Re(lambda)<=1/12 on this circle, so

    exp(A*Re(N))<=exp(-7n/24+7/24).                         (32)

### Full selected response, including the remaining quartet terms

L997(5) rewrites the response using the SAME K_(n+2) as the difference
of the upper short interval [cn,c(n+2)] and the lower interval [n,n+2].
Split only for estimation, keeping the equality and all its terms:

* upper intervals for the two points 3/4+i and 3/4-i, first the
  Laguerre part L_(n+1)^(2)/(n+1), then its constant -1/(n+1);
* upper intervals for the two reflected points 1/4+i and 1/4-i,
  retaining their full K;
* lower intervals for all four points, retaining their full K.

For the first part, use t=c_j*(n+u), dt=c_j*du, 0<=u<=2, (22),
(24) and (25). Apart from the original outer sign, its exact expression is

    1/(n+1)*[w^(n+1)] (1-w)^(-3)
      *sum_(sigma=+1,-1) integral_0^2
            exp(A*N)*[A*P_n(exp(h*N))
                         +h*exp(h*N)*P_n'(exp(h*N))]du.       (33)

All sums are finite and all u and w integrations are compact with
continuous integrands; these interchanges require no limiting argument.
On |w|=1/2, Cauchy gives coefficient factor 2^(n+1), and
|(1-w)^(-3)|<=8. Apply (31)-(32), sum the TWO signs, and integrate
over the interval of length two. The bound is

    128*2^n/(n+1)*q^(2n-1)*exp(-7n/24+7/24)*V_n
      <=320/(n+1)*(18/25)^n*exp(-7n/24)*V_n.                 (34)

For the last inequality use exp(7/24)<=24/17, so the constant
128*q^(-1)*exp(7/24) is at most 5120/17<320. The entire generating
function in (33), rather than an asymptotic saddle contribution,
is bounded. Both Laguerre oscillatory branches are consequently covered.

The upper reflected points have Re(omega-1)=-3/4. From (22), their
combined bound, including (24) and all atoms in absolute value, is

    18*(n+2)*exp(-7n/8)*V_n.                               (35)

Indeed each interval has length 2c, and the normalized integrand is
at most 2*(n+2)*exp(-cn/4-t/4); t>=cn and c<=9/4.
For the upper right-pair CONSTANT branch, the same reasoning with
|K_constant|=1/(n+1) and Re(omega-1)=-1/4 gives

    9/(n+1)*exp(-7n/8)*V_n.                                (36)

Finally all four lower intervals, each of length two, are bounded
using Re(omega-1)+1/2<=1/4 and c>=7/4:

    16*exp(1/2)*(n+2)*exp(-3n/16)*V_n.                      (37)

This bound includes both reflected lower terms and the -1 in their K.
Thus the lower interval has not been silently canceled by the weights.

Adding (34)-(37), using exp(1/2)<=2, 18/25<1,
7/24>3/16 and 7/8>3/16, and dividing the remaining prefactor by
n+2 gives, for n>=20,

    320/((n+1)*(n+2))+32+18+9/((n+1)*(n+2))
      <=50+329/(21*22)=3347/66<64.

This proves (20). If J_n!=0, scalar normalization multiplies TV
by 1/|J_n|, proving (21). Exponential growth divided by a fixed
polynomial exceeds C_epsilon*exp(epsilon*n) for every fixed
epsilon<3/16 and every finite C_epsilon eventually. If J_n=0 for
arbitrarily large n, that separately prevents eventual-all-n
normalization; otherwise (21) applies eventually. This completes
the subclass stop.

### Exact arithmetic check and qualifications

The elementary rational comparisons in (26)-(31), (34) and the final
constant were replayed with Python Fraction arithmetic:

    python3 scripts/adaptive-slope/primal-chebyshev-316.py

The complete certificate is scripts/adaptive-slope/primal-chebyshev-316.json.
Every check passes. It checks constants, not the analytic proof or an
infinite family of numerical kernel samples. The all-n argument is above.
That certificate alone is not an independent verification or a competing
response lower bound. Other degrees, root placements, weights and
arbitrary complex measures remain outside this conclusion.

### Independent proof audit — step317, 10 November 2026

This audit rederives the load-bearing inequalities from L997's exact
definitions and L994(6)-(7), rather than interpreting the rational
certificate as an analytic proof. It verifies the existing subclass
bound, with no stronger conclusion and no new all-measure argument.
The ready review312 EXPLORE assessment is reused on its unchanged scope.

**Operator and applicability.** L997(7) gives
z_0(c)=exp(-c/4+i*(phi(c)-c)), so the phase cancellation in (24)
has the stated sign and modulus for every atom, including A and B.
Since h*k=1/2 and h>0, the atoms are distinct and their TV is exactly
the coefficient l1 norm. Every v_l is on the stated upper-half-plane
chord. Thus 1-v_l is nonzero and the polynomial is defined. The
generating function in (22) uses degree n+1 and denominator n+1,
exactly as required by m=n+2. Its Cauchy circle lies strictly inside
the disk of analyticity. The real Laguerre bound applies to every t
in the upper and lower intervals: alpha=2>=0 and t>=0. Explicitly,
the bound after subtraction is

    |K_m(t)|<= [m*(m+1)/2+1]/(m-1)*exp(t/2)
             <=2*m*exp(t/2), m>=2,

because the last comparison is equivalent to
(3*m+1)*(m-2)>=0. Hence the -1 costs in (35),(37) are included;
(36) treats the upper right -1 separately.

**Uniform contour estimate.** The equation |p|=|1+p|/2 is
equivalent to |p-1/3|=2/3. Substituting either sigma into Y gives
the displayed center and radius. The triangle bound before maximizing s is

    |Y|<=7*s/48+1/16+|sigma*s/4-1/8|+s/6
         <=3/16+9*s/16, 1<=s<=11/10.

For sigma=+1 the constant in the last expression can even be replaced
by -1/16; the weaker common bound covers both signs. The real-part
bound is s/48-1/16. These verify (28) uniformly in u,n and on the
whole circle. Convexity of the chord, R<=32/31 and
cos(5/16)>=1-(5/16)^2/2 give (26). Therefore

    (|X-1|+|1-v_l|)/|1+v_l|
       <=30448/51615<3/5

for every root simultaneously. In the product for P_n, the ratio
to |P_n(-1)| cancels every |1-v_l| denominator. For P_n', omit
one numerator factor in each differentiated product and bound the
corresponding |1+v_l| below by D. This proves both (30) without
dividing by X-v_l. Finally |P_n(-1)|<=V_n is the triangle
inequality, not a putative upper bound on V_n. This direction is
essential to the lower normalization cost.

**Complete quartet accounting.** Substituting t=c_j*(n+u) in
each upper interval produces the Jacobian c_j. The finite identity
sum c_j*p_(n,j)*exp(c_j*N)=exp(A*N)*(A*P_n+h*X*P_n')
therefore gives exactly (33), with both sigma signs. The Cauchy,
generating-factor, sign-count, u-length and derivative constants are
respectively 2^(n+1),8,2,2,2; their product is 128*2^n.
The exponent maximum is A*(-n/6+1/6)=-7*n/24+7/24.
This independently recovers (34), including q^(2n-1), not q^(2n).
For the reflected upper pair the full normalized integrand is at
most 2*(n+2)*exp(-c*n/4-t/4). Two intervals of length 2c
give the prefactor 8c<=18 and exponent -c*n/2<=-7*n/8.
The upper right constant pair similarly gives 4c/(n+1)<=9/(n+1).
For all four lower intervals t<=n+2 and c>=7/4 give exponent
-7*n/16+(n+2)/4=-3*n/16+1/2 and prefactor
4*2*2*(n+2)=16*(n+2). Thus (35)-(37) cover every remaining
term of the exact interval difference, irrespective of its outer sign.
Only finite sums and compact integrals are exchanged.

**Constants and all-degree conclusion.** Replayed
scripts/adaptive-slope/primal-chebyshev-316.py and inspected every
entry of its /checks certificate, not a preview. In particular the
derivative prefactor is 26099/19980<2, the upper coefficient constant
is at most 5120/17<320, and the final normalized constant is
3347/66<64. The decay comparisons hold for all n>=20, since
2*q^2=18/25<1, 7/24>3/16 and 7/8>3/16. No finite sampling
is used to extrapolate in n. If J_n=0 for unbounded n, eventual
normalization is impossible. Otherwise it is eventually nonzero,
and homogeneity of complex-measure TV gives V_n/|J_n| and (21).
For example the permitted choice epsilon=3/32 would require
exp(3*n/32)/(64*(n+2)) bounded, which is false. This verifies
failure of the required every-epsilon quantifier. It says nothing
about other slope measures or their competing leakage.

Audit result: PASS for (20)-(21), with no correction to the bound.
The direct mathematical inputs remain L994 and L997; C997a is not
a premise. The result remains a known-tool specialization and a
stop for this prescribed family only. No claim about actual zeros,
signed forcing, infinite-zero complements or L984(H) is obtained.

## Mathlib

Full matching coverage of this exact Chebyshev atomic family and its
normalization-cost bound is unchecked and unknown. Polynomial products,
Cauchy coefficient estimates and finite complex measures are supporting
mathematics; their precise Mathlib theorem names were not checked here.
No absence claim or formal verification is asserted.
