# Lemma 572: the complete ratio coefficient certificate is too small

## Hypotheses

Use the exact ratio polynomial in L481, with L477's fixed cutoff:

    X=sqrt(T/(2pi)), M=floor X, T<=t<=2T,
    U_T(t)=sum_(n,m<=M) log(n/m)^2/sqrt(nm) exp(it log(m/n)).

All pairs are ordered. T tends to infinity through arbitrary real values.
There is no RH, zero-simplicity, spacing, independent-phase or chirped
cancellation assumption. Every nonzero frequency is retained, both
positive and negative. The diagonal is zero, not a zero-frequency term.

Import Jaming--Saba, *From Ingham to Nazarov's inequality: a survey on
some trigonometric inequalities*, arXiv:2311.17714v1, 29 November 2023,
Theorem 4.2, equation (4.4), Section 4.2, printed pp. 38--48
([primary version](https://arxiv.org/html/2311.17714v1)). In precisely
the normalization recorded in the prior source assessment, there are
absolute c_*,delta_*>0 such that, if 0<delta<delta_*,
lambda_(k+1)-lambda_k>=1 and the complex a_k are arbitrary, then

    sum_(k=0)^N |a_k|/(k+1)
      <= c_* delta^(-15/2)
         integral_(-(1+delta)/2)^((1+delta)/2)
          |sum_(k=0)^N a_k exp(2pi i lambda_k y)|dy.       (1)

This theorem and its constants are imported, not reproved. The prior
assessment inspected its hypotheses and essential proof cases; no
independent source-proof audit or effective numerical value of c_* or
delta_* is claimed. All asymptotic constants below are fixed positive
constants, and all onsets are existential.

## Conclusion

Let R_M be the increasing list of reduced ratios a/b with 1<=a,b<=M,
gcd(a,b)=1, a!=b. If j(r) is the one-based ascending rank, set

    b_r=log(r)^2 H_floor(M/max(a,b))/sqrt(ab),
    S_M=sum_(r in R_M) b_r/j(r),
    g_M=min_(r<s in R_M) log(s/r), H=T g_M/(2pi).

Here H_q=sum_(d=1)^q 1/d. For M>=5 the minimum gap is exactly

    g_M=log((M-1)^2/(M(M-2))).                           (2)

Writing alpha=X-M in [0,1), uniformly as M tends to infinity,

    H-1=2(1+alpha)/M+O(M^(-2)),
    S_M is comparable to M^(-1/2)(log M)^3.              (3)

In particular delta=H-1 lies in (0,delta_*) eventually. The full
interval application of (1) gives integral_T^(2T)|U_T(t)|dt>=B(T),
where this particular coefficient certificate satisfies

    B(T)=(2pi/(c_* g_M))(H-1)^(15/2) S_M,
    B(T) is comparable to M^(-6)(log M)^3
                 and to T^(-3)(log T)^3.                (4)

Consequently B(T)/(T(log T)^3) is comparable to T^(-4) and tends to
zero at every sufficiently large real height, hence on every unbounded
sequence. Restricting the interval, translating its center, or using a
smaller admissible common gap in (1) cannot increase this certificate.

This stops only this complete-spectrum, ascending-rank implementation
of (1). It is not an upper bound for the actual integral|U_T|, a failure
of a full-scale ratio norm bound, a chirped separation estimate, a
negative-mass bound or an RH statement. L477's two defect thresholds
remain open. This is a local known-tool specialization; it is not
claimed as a discovery beyond the sources checked.

## Proof

### 1. Exact grouping and logarithmic minimum gap

For m=da,n=db with (a,b)=1, m/n=a/b and

    log(n/m)^2/sqrt(nm)=log(a/b)^2/(d sqrt(ab)).

Summing 1<=d<=floor(M/max(a,b)) proves the stated b_r and the exact
identity U_T(t)=sum_(r in R_M)b_r exp(it log r). All b_r are positive.
There is no factor two: reciprocal ratios are separate terms, with
equal coefficients. The terms with n=m have zero coefficient.

For distinct fractions a/b<c/d in this list let k=bc-ad>=1. Their
logarithmic separation is log(1+k/(ad)). We show ad/k<=M(M-2) for
M>=5. If k>=2 then ad/k<=M^2/2<=M(M-2). If k=1 and ad>M(M-2),
both a,d belong to {M-1,M}; otherwise ad<=M(M-2).

If a=d=M then bc=ad+1>M^2 is impossible. If one of a,d is M and
the other is M-1, then bc=M(M-1)+1>(M-1)^2, so one of b,c must
be M. This is impossible because bc is then divisible by M whereas
M(M-1)+1 is not. If a=d=M-1, then bc=(M-1)^2+1>(M-1)^2, so
again one of b,c must be M. The proposed product is congruent to
2 modulo M, also impossible for M>=5. These exhaust the cases.
Thus every separation is at least log(1+1/(M(M-2))). The reduced
fractions (M-2)/(M-1)<(M-1)/M attain this separation and neither
is 1. This proves (2), including both frequency signs and the hole
where the zero frequency would otherwise lie.

Since g_M=-log(1-1/(M-1)^2), the real logarithm's Taylor estimate gives

    g_M=1/(M-1)^2+O(M^(-4)).

Using T/(2pi)=(M+alpha)^2 proves the first formula in (3), with error
uniform for 0<=alpha<1. Moreover H>(M/(M-1))^2>1 exactly, because
-log(1-u)>u for 0<u<1. Hence H-1 is comparable to 1/M, not a
fixed positive margin. Its upper bound eventually ensures H-1<delta_*.

### 2. Lower bound for the complete rank sum

The first J=M-floor(M/2) ratios are

    1/M, 1/(M-1), ..., 1/(floor(M/2)+1).

Indeed each lies below 2/M, and any reduced fraction with numerator
at least 2 is at least 2/M. For these denominators b>M/2 one has
H_floor(M/b)=1, so b_(1/b)=log(b)^2/sqrt(b), bounded below by
c(log M)^2/sqrt(M) for M>=5. Their exact ranks are 1,...,J.
Since sum_(j<=J)1/j>=log(J+1)>=c log M, this proves

    S_M>=c M^(-1/2)(log M)^3.                           (5)

The remaining coefficients are not removed from an L1 inequality;
their positivity only permits a lower bound on the numerical sum S_M.

### 3. Rank counting and the upper bound

For 4/M<=r<=1/2 and M sufficiently large, put A=floor(rM/2).
Count coprime pairs with 1<=a<=A and ceil(M/2)<=b<=M. Each reduced
ratio a/b<=2a/M<=r is in R_M, and no two such pairs give the same
ratio. For a<=A<=M/4 the denominator interval contains at least
floor(M/(2a)) complete blocks of a consecutive integers. Each block
has phi(a) integers coprime to a, giving at least

    (M/(2a)-1)phi(a)>=M phi(a)/(4a)

denominators. The elementary product formula and finite union bound
give phi(a)/a=product_(p|a)(1-1/p)>=1-sum_(p|a)1/p, including a=1.
Consequently

    sum_(a<=A)phi(a)/a
      >= A-sum_(p<=A) floor(A/p)/p
      >= A(1-sum_(n=2)^infinity n^(-2)) >= A/4.         (6)

For the last inequality use
sum_(n=2)^infinity n^(-2)<=1/4+integral_2^infinity x^(-2)dx=3/4.
As A>=rM/4 when rM>=4, the number of ratios <=r, hence its rank
when r belongs to R_M, is at least M^2 r/64. Counting at r=1/2
also shows that every ratio >1/2 has rank at least M^2/128.
All these counts are for the complete spectrum, with no artificial
zero coefficient or restriction to a frequency sign.

Split S_M into r<4/M, 4/M<=r<=1/2 and r>1/2, taking M>=16.
For the first part, a/b<4/M implies a<4, b>M/4, and
H_floor(M/b)<=H_4. Also |log r|<=log M. Thus every coefficient
in that part is at most C(log M)^2/sqrt M. The total number of
ratios is <=M^2, so its rank-weighted sum is at most

    C M^(-1/2)(log M)^2 (1+2 log M).                     (7)

For the middle part, (6) and r=a/b give the pointwise bound

    b_r/j(r)<=C M^(-2) log(b/a)^2 H_floor(M/b)
                                 sqrt(b)/a^(3/2).

First use log(b/a)^2<=(log M)^2 on the original range a<=b<=M.
Then drop coprimality and enlarge the remaining nonnegative sum to
all 1<=a,b<=M, using

    sum_(a>=1)a^(-3/2)<=3,
    sum_(b<=M)sqrt(b) H_floor(M/b)
       =sum_(d<=M) (1/d) sum_(b<=M/d)sqrt(b)
       <=M^(3/2) sum_(d>=1)d^(-5/2)<=C M^(3/2).

Its total contribution is therefore at most
C M^(-1/2)(log M)^2, smaller than (7).

For the last part the rank bound M^2/128 applies. The sum of all
grouped coefficients equals the sum of all original nonnegative
coefficients. With S_j=sum_(n<=M)n^(-1/2)log(M/n)^j for j=0,2,
the inequality (x-y)^2<=2x^2+2y^2 gives

    sum_(r in R_M)b_r<=4 S_0 S_2<=C M.                  (8)

Here S_0<=2sqrt M; for S_2 partition the integers into
M/2^(h+1)<n<=M/2^h. The h-th contribution is at most
2sqrt M 2^(-h/2)((h+1)log 2)^2. The convergent infinite sum
bounds all finite blocks, including n=1 and every floor endpoint,
so S_2<=C sqrt M. Thus the r>1/2 contribution is O(1/M).
Combining (5)--(8) proves the second formula in (3). The coprime
count is proved here because a bound on the total unweighted mass
alone would not evaluate the ascending-rank source certificate.

### 4. Translation, normalization, Jacobian and interval losses

Set t_c=3T/2, y=g_M(t-t_c)/(2pi), lambda_r=log(r)/g_M and
a_r=b_r exp(it_c log r). Then successive lambda_r have gap >=1,
|a_r|=b_r, and the actual interval maps exactly onto [-H/2,H/2].
The Jacobian is dt=(2pi/g_M)dy. Apply (1) with delta=H-1, which
is in its required open range for all sufficiently large M. This
gives exactly (4)'s inequality and certificate formula. There is
no assumed bound for the chirped product sum and no Haar averaging.

Since g_M is comparable to M^(-2), (3) gives

    g_M^(-1)(H-1)^(15/2) S_M
       comparable to M^(2-15/2-1/2)(log M)^3
       =M^(-6)(log M)^3.

The relation T=2pi(M+alpha)^2 proves all comparisons in (4) and
the ratio T^(-4) to the required full scale. Both upper and lower
comparisons concern B(T), whose c_* is fixed, not the true norm.

For completeness, using a smaller common gap g'<=g_M and a subinterval
of length h<=T admits only 0<delta<=h g'/(2pi)-1. The coefficient
sum is still S_M, since translations change only coefficient phases.
For fixed g', its certificate increases with delta, so the full
interval and delta=Tg'/(2pi)-1 are best. Writing H'=Tg'/(2pi)>1,
this value is (T/c_*) S_M (H'-1)^(15/2)/H'. The function
(H'-1)^p/H' is strictly increasing for H'>1 when p=15/2, since
its derivative has the sign of (p-1)H'+1. It is maximized by
g'=g_M. The permitted deltas all remain below delta_* eventually.
If H'<=1 the source theorem is inadmissible, not improved. Reflection
reverses reciprocal ratios with equal coefficients and yields the
same S_M. No deletion, shifted rank, new dual or extension of (1)
is considered. This completes the certificate test.

### 5. First independent arithmetic and hypothesis audit, 31 October 2026

The audit accepts (2)--(4), including their uniformity over all sufficiently
large real T. No conclusion or power is repaired. This is independent
verification of the local specialization, conditional on the cited source
theorem as stated; it is not an independent audit of its manuscript proof.
L481 supplies exactly the ordered U polynomial used here. L477 supplies
the same fixed M and the full residual U+Re(e^(2i theta)V). Nothing in
this audit transfers a ratio-only certificate to that full residual.

Grouping preserves every multiplicity: a reduced a/b determines exactly
m=da,n=db with 1<=d<=floor(M/max(a,b)). The reciprocal ratios are
distinct frequencies with equal positive coefficients. All and only the
diagonal pairs have zero weight. Thus grouping introduces neither a
zero-frequency coefficient nor a factor two.

For any distinct ratios, k=bc-ad is a positive integer. The k>=2 case
has ad/k<=M^2/2<=M(M-2) for M>=5. In the remaining k=1 case,
ad>M(M-2) forces both factors into {M-1,M}. The products M^2,
M(M-1), and (M-1)^2 are the full list, with the middle product covering
both orderings. Respectively bc=ad+1 is too large, or forces b=M or
c=M and has residue 1 or 2 modulo M. The latter residues cannot be
zero for M>=5. The consecutive reduced fractions in Section 1 attain
the resulting bound, without using the excluded unit ratio. Therefore
the exact minimum is valid on the complete spectrum, not merely within
one selected block.

There are also direct uniform excess-length bounds. Put u=1/(M-1)^2.
The inequalities u<-log(1-u)<=u/(1-u), together with
M<=X<M+1, give

    (2M-1)/(M-1)^2 < H-1
          < (4M+1)/(M(M-2)).                              (9)

The lower inequality is strict even when X=M. Hence 0<H-1<delta_*
eventually, with no integer-cutoff exception. Expanding
(1+alpha/M)^2/(1-1/M)^2 and using
g_M=(M-1)^(-2)+O(M^(-4)) yields precisely
2(1+alpha)/M+O(M^(-2)), uniformly for 0<=alpha<1. No fixed
positive excess length can replace this shrinking quantity.

For the rank lower bound, numerator-one fractions with b>M/2 are
exactly the fractions below 2/M: every numerator at least two gives
a/b>=2/M, and the remaining numerator-one denominators are at most
M/2. Their ranks are consequently M-b+1, including odd M and all
endpoints. Their coefficients are at least
log(M/2)^2/sqrt(M); the harmonic rank sum supplies the third logarithm.
This is a lower bound on S_M with all other frequencies still
present in the source inequality.

For the upper bound, the interval [ceil(M/2),M] contains at least
floor(M/(2a)) disjoint complete blocks of a consecutive integers.
Every block has exactly phi(a) coprime residues; for a=1 this is one.
Since a<=A<=M/4, floor(M/(2a))>=M/(4a). Distinct coprime pairs
in the counted rectangle represent distinct fractions <=r<=1/2 and
never the excluded unit fraction. The union bound in (6) includes the
empty prime set at a=1 and, after summing, gives

    count(r)>= (M/4) sum_(a<=A)phi(a)/a
             >=MA/16>=M^2 r/64.

Here A=floor(rM/2)>=rM/4 holds for the full closed range rM>=4.
At r=1/2 this also certifies the stated rank bound for every larger
ratio, including all ratios above one.

The three upper sums exhaust the spectrum with disjoint boundaries.
For r<4/M, a<4 and b>M/4, so the uniform coefficient bound with
H_4 and the harmonic sum through at most M^2 ranks applies. For
4/M<=r<=1/2, first bound the squared logarithm on a<=b<=M;
only then enlarge the remaining positive sum. The bounds
sum a^(-3/2)<=3 and sum d^(-5/2)<=5/3 give an upper bound
320 M^(-1/2)(log M)^2 for this part. Every floor is retained by
the finite identity for sum sqrt(b) H_floor(M/b) in Section 3.
For r>1/2 the rank is at least M^2/128 and the whole coefficient
mass is at most 4 S_0 S_2=O(M). The half-open dyadic blocks used
there contain every integer exactly once, including n=1 and powers
of two; extending their positive majorants to an infinite convergent
series is an upper estimate, not an infinite-series identity. Thus
this last contribution is O(M^(-1)). These bounds and the first
rank block prove both sides of the complete S_M comparison.

Finally the actual interval maps onto [-H/2,H/2] with Jacobian
2pi/g_M. The finite real frequencies lambda_r may have both signs:
the imported ascending-rank theorem has no sign restriction, and its
arbitrary complex coefficients allow the exact translation phases.
Its open delta range follows from (9). The power check is
M^2 M^(-15/2) M^(-1/2)=M^(-6); since T=2pi(M+alpha)^2,
this is T^(-3), and division by T(log T)^3 gives T^(-4).
For any 0<g'<=g_M and h<=T, admissibility requires H'>1;
all possible excess lengths are at most H'-1<=H-1<delta_*.
The positive derivative of (H'-1)^(15/2)/H' proves the claimed
optimization without crossing the theorem's open endpoint. Reversing
frequencies leaves S_M unchanged because reciprocal coefficients
are equal. These checks validate only B(T); no inequality reverses
the source's lower bound into an upper bound for the true norm.

## Mathlib

Full matching coverage for this grouped-ratio certificate has not
been checked. Supporting finite grouping, harmonic sums, totient
product formula, logarithm estimates and change of variables have
not been matched to specific Mathlib declarations. Unknown coverage
does not assert absence. The only non-elementary imported inequality
is the precisely cited Jaming--Saba Theorem 4.2/(4.4); the elementary
rank and gap calculations are supplied to justify its specialization.
The local L477/L481 definitions and defect relevance retain their
own cited analytic qualifications. No new source theorem, numerical
certificate, RH candidate or all-height sign claim is asserted.
