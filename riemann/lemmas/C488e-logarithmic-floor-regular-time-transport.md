# Corollary 488e: logarithmic-floor regular-time transport

## Hypotheses

Use the actual theta heat family H_t in C488a, with
H_0(z)=xi((1+iz)/2)/8. Fix real a and R>=200. Write its zero
copies as z_j=x_j+i y_j, counting multiplicity, and set

    s(x)=sqrt(x^2+R^2), L(x)=log(2+s(x)),
    w(x)=exp(-sqrt(1+((x-a)/R)^2)),
    eta(x)=1/(1000L(x)), p(x)=w(x)eta(x),
    A_j(t)=1_(y_j!=0)[w(x_j)|y_j|+p(x_j)], A(t)=sum_j A_j(t).

Let 0<t<=1/5 be a regular time: H_t has no multiple zero.
Use the paired velocity law, actual strip and all-copy global count
of C488a, the positive-time confinement of L488, and the audited
nearby real-partner payment of C488d. No RH, positive lower nonreal
height, uniform separation, restriction on a, or finite-head parameter
relation is assumed. Derivatives keep a and R fixed.

## Conclusion

The contributing sum is finite and differentiable at this time, and

    A'(t) <= sum_(j:y_j!=0)
              26(|x_j|+R)log(32(|x_j|+R)) A_j(t)/R^2
           <= sum_(j:y_j!=0)
              40(|x_j|+R)log(32(|x_j|+R)) A_j(t)/R^2.       (1)

This is a quantitative specialization of C488a's known transport
mechanism, with a different floor and widened a,R domain. The full
changed-floor inequality is not stated in the checked sources; no
novelty claim is made. The separate conceptual audit2121 below passes
with the stated hypotheses and accepted source inputs.
It proves no collision passage, integrated estimate, time-zero
passage, initial-mass bound, all-height reality or actual-Xi
all-degree mixed positivity.

## Proof

### Imported results, domains and regularity

The prior SPECIALIZE assessment is
`drafts/literature/2026-11-21-log-floor-full-transport-review-2118.md`.
The source mechanism is bramble_trace, *An unsigned strip bound for
the de Bruijn--Newman constant*, rStation paper186, v1,
20 November2026, [Appendix B, (B.1)-(B.5)](https://rstation.ai/problems/riemann_hypothesis/papers/186).
Its original floor and parameter restrictions differ from ours.
Replaying the pair bookkeeping is necessary to verify the changed
weight and full-domain constants, rather than copying its rate20.

Import D. H. J. Polymath, *Effective approximation of heat flow
evolution of the Riemann xi function, and a new upper bound for the
de Bruijn--Newman constant*, Research in the Mathematical Sciences
6 (2019), article31, [arXiv1904.12438v2, Proposition3.1(i)/(28),
Theorems1.5(i)-(ii),3.2](https://arxiv.org/html/1904.12438v2),
in the normalizations already checked in L488 and C488a. At a simple
selected zero,

    z_j'=2 sum_(k!=j)' 1/(z_j-z_k),                         (2)

where opposite zeros z_k,-z_k are paired. The source allows other
zeros to be complex or repeated. Its strip input is N. C. de Bruijn,
*The roots of trigonometric integrals*, Duke Math. J.17 (1950),
197-226, Theorem13, as restated in Polymath Theorem3.2. Together with
the initial strip this gives |y_k|<=1 for 0<=t<=1/5.

C488a(4), independently of its finite-head parameters, gives

    #{k:|x_k|<=u} <= N(u):=(u+20)log(4u+40), u>=0.          (3)

It counts all copies at every 0<=t<=1/5. This also makes the vertical
reciprocal tails absolutely convergent and justifies the opposite-paired
product underlying (2). We import (3), not a new local-count theorem.
C488d supplies the changed-floor nearby mixed count payment below.

Choose a compact positive-time neighborhood of t inside (0,1/2).
L488 applies to it in coordinates lambda=t/4 and
F(lambda,z)=8H_(4lambda)(2z). All nonreal or multiple zeros there
are confined to one compact rectangle. Enlarge this rectangle slightly,
with boundary free of H_t zeros. Joint entirety (L058) and Rouche's
theorem keep its zero count constant locally. At the regular slice
all its finitely many zeros are simple, so they have local analytic
branches; its real branches stay real by conjugation and uniqueness.
Its nonreal branches remain nonreal on a sufficiently small common
neighborhood. The exterior stays real by the uniform confinement.
Thus locally A is a fixed finite sum of smooth terms. At t=1/5 the
same neighborhood can straddle the endpoint, since L488's source range
extends to H-times below1/2. Counts and the coefficient estimates below
are used only at the stated slice. There is no differentiation at a
collision or interchange of a derivative with an infinite trace.

### Changed derivatives and segment comparisons

The unchanged weight satisfies

    |w'|<=w/R, |w''|<=w/R^2.                               (4)

Indeed for v=(x-a)/R,
R^2 w''/w=v^2/(1+v^2)-(1+v^2)^(-3/2), whose absolute value is at
most1. Also

    L'=x/[s(2+s)],
    L''=R^2/[s^3(2+s)]-x^2/[s^2(2+s)^2].

Each term in L'' is nonnegative and at most1/R^2, because s>=R
and |x|<=s. Hence |L'|<=1/R and |L''|<=1/R^2. C488d's elementary
comparison gives L>=log202>5, including R=200. Differentiating eta,

    |eta'|/eta<=1/(5R),
    |eta''|/eta=|2(L'/L)^2-L''/L|<=7/(25R^2).

The product p=w eta therefore satisfies

    |p'|<=6p/(5R),
    |p''|<= [1+2/5+7/25]p/R^2
           =42p/(25R^2)<=2p/R^2.                          (5)

Integrate |(log w)'|<=1/R and |(log p)'|<=6/(5R).
On a segment of length at most R, w is at most3 times its value at
either endpoint, and p is at most4 times its value at either endpoint.
For exact scalar margins, C488a proves e<11/4<3, while the exponential
series gives exp(1/5)<sum_(n>=0)(1/5)^n=5/4. Consequently
exp(6/5)<55/16<4. These constants are independent of a and x.

### Nearby nonreal and real partners

Partition interactions by the closed nearby condition |x_j-x_k|<=R.
First exclude each nonreal zero's own conjugate, reserving it below.
For an unordered pair of nonreal zeros put

    d=x_j-x_k, b=y_j-y_k, D=d^2+b^2,
    Y_j=|y_j|, h_j=w_j Y_j, w_j=w(x_j), p_j=p(x_j).

The height contribution, after removing its factor2/D, is exactly

    d(w'_j Y_j-w'_k Y_k)
       -b(w_j sgn(y_j)-w_k sgn(y_k)).                      (6)

For equal signs sigma, it becomes

    [d(w'_j+w'_k)/2-(w_j-w_k)] sigma b
       +(d/2)(w'_j-w'_k)(Y_j+Y_k).

Let M_w=sup_segment |w''|. Integrating the first bracket as the
trapezoid error for w' bounds it by M_w d^2/4: the kernel is
u-d/2 on a segment of length |d|, with absolute integral d^2/4.
The second coefficient is bounded by M_w d^2/2. Since
|b|<=Y_j+Y_k and d^2/D<=1, restoring2/D bounds the pair by
(3/2)M_w(Y_j+Y_k). By (4) and the segment comparison this is at most

    (9/2)(h_j+h_k)/R^2.                                   (7)

For opposite signs the vertical numerator in (6) is
-(w_j+w_k)(Y_j+Y_k), and the horizontal numerator is at most
(|d|/R)(h_j+h_k). Their sum is nonpositive for |d|<=R.
For a real partner k only j contributes to height; its numerator
is d w'_j Y_j-w_jY_j, also nonpositive in that range.

The count contribution for an unordered nonreal pair is
2d(p'_j-p'_k)/D. With M_p=sup_segment |p''|, it is bounded above by
2M_p d^2/D<=2M_p. By (5) and the factor4 segment comparison,

    2M_p <=16min(p_j,p_k)/R^2<=8(p_j+p_k)/R^2.              (8)

All these estimates hold at d=0 as well; D>0 for distinct simple
zeros. Combining (7)-(8), each nearby nonreal pair other than own
conjugates costs at most8(A_j+A_k)/R^2. Each j has at most N(m_j)
nearby copies, where m_j=|x_j|+R, so their total is at most

    sum_(j:y_j!=0) 8N(m_j)A_j/R^2.                         (9)

The own-conjugate term in (2) is -i/y_j. Its height loss is
-w_j/Y_j per copy, and it has zero horizontal and count contribution.
C488d(1) bounds the sum of all nearby real-partner count contributions
at j by (3/25)w_j/Y_j. Their sum with the reserved loss is nonpositive.
No conjugate loss has been used in (7)-(9), and no positive minimum
Y_j was required. All nearby copies, including equality at |d|=R,
have now been paid for.

### Distant vertical and opposite-paired horizontal sums

For fixed j with y_j=y>0, combine each distant conjugate pair at
heights b,-b and common abscissa. Its vertical reciprocal kernels sum to

    2y(d^2+y^2-b^2)/[(d^2+(y-b)^2)(d^2+(y+b)^2)]>=0,

because |d|>R>=200 and |b|<=1. Vertical velocity has the opposite
sign, so its contribution to height is nonpositive. A distant real
copy has that sign individually. Conjugation gives the lower-half-plane
case. The distant set is conjugation invariant. Absolute convergence
of the vertical sum follows from (3) and the bounded strip.

For the horizontal reciprocal sum at j write m=|x_j|+R. The finite
portion with |x_k|<=2m and |d|>R has absolute value at most N(2m)/R.
When |x_k|>2m, both members of every opposite pair are distant and

    (1/2)[1/(z_j-z_k)+1/(z_j+z_k)]
       =z_j/(z_j^2-z_k^2),
    |z_j/(z_j^2-z_k^2)|<=4m/(3|x_k|^2),                   (10)

since |z_j|<=|x_j|+1<=m and |z_k|>=|x_k|>2m. This is an average
per copy; multiplying it by the all-copy count introduces no extra
factor2. In shells 2^(k+1)m<|x_l|<=2^(k+2)m, k>=0, (3) gives

    N(2^(k+2)m)<=5*2^k m log(32*2^k m).

The paired shell sum in (10) is consequently at most
(5/3)2^(-k)log(32*2^k m). Its sum is

    (10/3)[log(32m)+log2]<=5log(32m).                      (11)

The last inequality uses 32m>=4. This also proves convergence in
the prescribed opposite-paired order. No absolute convergence of
unpaired horizontal reciprocals is asserted. The cutoff |x_k|<=2m
and symmetric shell boundaries never split an opposite pair.

The horizontal multiplier in A_j' is 2(w'_jY_j+p'_j). By (4)-(5),
its absolute value is at most (12/5)A_j/R. Thus all distant horizontal
costs are bounded by

    sum_(j:y_j!=0)
       [(12/5)N(2m_j)+12Rlog(32m_j)] A_j/R^2.              (12)

Only the finite contributing sum over j is taken here. Equations
(10)-(11) handle each infinite exterior velocity sum before this
finite sum, so neither rearrangement nor differentiation requires an
unproved infinite-sum interchange.

### Full-domain coefficient

Combine (9), the paid mixed/own-conjugate terms, the nonpositive distant
vertical terms and (12). For every m>=R>=200,

    8N(m)+(12/5)N(2m)+12Rlog(32m)
       <=[(64/5)m+208+12R]log(32m)
       <=(646/25)m log(32m)<26m log(32m).                  (13)

Indeed 4m+40<=32m and 8m+40<=32m permit replacing both count
logarithms by log(32m); their constant coefficients are
8*20+(12/5)*20=208. Finally R<=m and
208<=208m/200=(26/25)m. This proves (13) throughout the unbounded
domain, including m=R=200. All A_j are nonnegative. Summing gives
the first inequality in (1), and 26<40 gives the second. If there
are no nonreal zeros the finite sum is locally zero by the regularity
argument, and the same conclusion holds.

The achieved sufficient coefficient646/25 is strictly below the
required40. This is an analytic budget, not sampled evidence for zero
locations. It supplies only the regular-time derivative inequality;
none of the omitted global or time-passage obligations follows from it.

### Independent conceptual audit — 21 November2026, step2121

The exact rate40 target passes under the unchanged SPECIALIZE
assessment cited above. This is a local verification of the quantitative
reproduction, not a new transport mechanism or an advance beyond the
checked source mechanisms. No load-bearing defect, altered hypothesis,
new mathematical input or changed dependency was found. The stronger
sufficient coefficient646/25 in (13) is retained.

**Applicability and differentiation.** The count proof in C488a(4)
uses only the actual H_t kernel, 0<=t<=1/5, and an arbitrary window
radius u>=0. It uses none of that corollary's V,X,U,a,R restrictions.
Its closed-window all-copy count, paired velocity law and strip can
therefore be used here. C488d's audited (1) has exactly the present
w,p, all real a, R>=200 and closed nearby cutoff. Its local count
input is carried by C488d; no new count or onset is being inferred.

For the local finite-trace argument, take 0<tau<t<T<1/2, allowing
t=1/5, and apply L488 on [tau/4,T/4] in F coordinates. Conversion
F(lambda,z)=8H_(4lambda)(2z) preserves multiplicity. Choose a larger
rectangle whose boundary is zero-free at the slice t. Compactness of
that boundary and joint holomorphy give a common time neighborhood
with no boundary zero. The finitely many simple interior zeros each
have disjoint implicit-function neighborhoods; Rouche's count excludes
additional interior zeros. Shrinking the time neighborhood makes all
these branches simple, the real ones real, and the nonreal ones
nonreal. Uniform confinement makes every exterior zero real there.
Thus A locally is exactly a fixed finite sum, even if there are no
nonreal zeros. The derivative at1/5 is the ordinary two-sided one;
only its value at1/5 uses the count and coefficient estimates. No
uniform simplicity assertion over an uncontrolled infinite set is
needed, and no infinite trace has been differentiated.

**Derivatives and nearby bookkeeping.** Directly,

    (log p)'=w'/w-L'/L,
    p''/p=w''/w-2(w'/w)(L'/L)+2(L'/L)^2-L''/L.

The two nonnegative quantities whose difference is L'' are each
<=1/R^2; this gives |L''|<=1/R^2, rather than their sum. With L>5,
the last display gives 1+2/5+2/25+1/5=42/25 as the coefficient
of1/R^2. Integrating the log derivatives gives precisely the factors
e<3 and exp(6/5)<4 for w and p, independent of the center a.
For d>0 the bracket in the equal-sign case of (6) is

    integral_0^d (u-d/2)w''(x_k+u) du;

its absolute kernel integral is d^2/4. Swapping endpoints covers
d<0, and d=0 contributes zero. The bound(7) follows with no lower
bound on D or on the nonreal heights. For the count term,
2sup_segment|p''|<=16min(p_j,p_k)/R^2<=8(p_j+p_k)/R^2.
The opposite-sign vertical term dominates the possible horizontal
height cost because (w_j+w_k)(Y_j+Y_k)>=h_j+h_k and |d|/R<=1.
The mixed height numerator is also nonpositive. These checks cover
every nearby class, including equality at the cutoff.

The unordered own-conjugate pair gives -2w_j/Y_j; its two per-copy
losses are exactly -w_j/Y_j, each paying C488d's respective real
partners. It is absent from(9), so there is no second use of that
loss. Summing the other unordered pair bounds by endpoints gives
8 sum_j degree(j)A_j/R^2, with degree(j)<=N(m_j); there is no
additional factor2. The nearby/distant division is made after taking
the derivative of the full trace at the fixed slice. No derivative
of a time-dependent cutoff or boundary-crossing term is asserted.

**Tail ordering and full-domain margin.** Conjugation preserves the
distant set, so the displayed vertical kernel pairs exhaust its
nonreal copies; real copies are handled individually. The bounded
strip and count(3) make this vertical sum absolutely convergent.
Removing finitely many nearby terms from the prescribed horizontal
sum is legitimate. For |x_k|>2m, both opposite copies are distant
since |x_k|-|x_j|>2m-|x_j|>R. Each symmetric shell contains whole
opposite pairs. The modulus of each pair sum is at most twice the
bound in(10), and the number of pairs is half the all-copy count.
Thus a shell costs at most (5/3)2^(-k)log(32*2^k m), as stated.
Indeed 20<=2^k m and40<=16*2^k m prove its bound on N for every
k>=0,m>=200. The identities sum2^(-k)=sum k2^(-k)=2 give(11),
including convergence; no unpaired absolute summation is used.

Finally the horizontal derivative multiplier is
2(w'_jY_j+p'_j), bounded by(12/5)A_j/R. The exact total coefficient
before division by R^2 is therefore bounded by

    [8m+160+(24/5)m+48+12R]log(32m)
      <=[64/5+26/25+12]m log(32m)
      =(646/25)m log(32m).

Here208/m<=26/25 and R/m<=1 include m=R=200. The margins to26
and40 are respectively4/25 and354/25, both strictly positive.
This closes the full unbounded parameter range analytically, not by
sampling. Multiplicity is included in the imported counts; the audit
does not extend the derivative assertion to multiple-zero times.
Collisions, integration, time zero, initial mass, all-height overlap
and L030-L032/C032a remain outside the conclusion. Full matching
Mathlib coverage remains unchecked. No mathematical script was needed.

## Mathlib

Full matching coverage has not been checked; no absence claim is made.
No Mathlib declaration is used for the actual-family count, confinement
or velocity theorems. Supporting operations are real differentiation,
finite sums, geometric series, elementary logarithm comparisons and the
holomorphic implicit-function/Rouche arguments stated above.
