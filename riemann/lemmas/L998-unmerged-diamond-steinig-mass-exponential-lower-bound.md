# Lemma 998: the unmerged Diamond–Steinig mass has positive exponential rate

## Hypotheses

Let n>=1 be an integer. Let K_n consist of nonnegative integer vectors
k=(k_1,...,k_(2n)) satisfying sum_j j*k_j=2n and
1<=r=sum_j k_j<=n. Set

    c(k)=(-1)^(r-1)*(r-1)!/prod_j k_j!,
    w(k)=prod_j (j!)^(-k_j).

Let H_n consist of ORDERED pairs (k',k'') of nonnegative integer
vectors of length n, each with weighted sum n. Their positive
lengths r',r'' must satisfy r'+r''<=n. Define c and w on these
vectors by the same formulas, and put

    M_n=2n*sum_(k in K_n) |c(k)*w(k)|
          +n^2*sum_((k',k'') in H_n)
                    |c(k')*c(k'')*w(k')*w(k'')|.              (1)

In particular H_1 is empty. Absolute values are taken BEFORE any
collection of equal convolution factors, including across the two
families. No arithmetic factor norms or correlation estimates are
assumed, and n is exactly the order nu, without rescaling.

## Conclusion

For every integer m>=1,

    M_(3m)>=2*(9/4)^m / binom(3m+2,2).                       (2)

Consequently, with natural logarithms,

    0 < log(9/4)/3
      <=limsup_(n->infinity) log(max(1,M_n))/n
      <=log(2).                                            (3)

Thus the subexponential assertion in review295 is false. This stops
automatic subexponential coefficient overhead for this UNMERGED
termwise representation at order nu=n. It neither bounds the norm
after signed collection nor disproves a signed arithmetic estimate,
Selberg methods generally, or RH. It does not pay L984(H).

## Proof

### Source import and scope

Import the finite coefficient definitions and the upper bound

    M_n<=(n+2)*2^(n-1)                                     (4)

from O. Ramaré, *On Bombieri's asymptotic sieve*, author preprint
dated 28 October 2009, Section 2, (12)-(18), Lemma 4, printed
pp8-9, and Lemma 7 with its proof using Lemmas 5-6, printed
pp10-11: [primary preprint](https://ramare-olivier.github.io/Maths/V12BombieriSieve.pdf).
The pre-invocation SPECIALIZE assessment is
drafts/literature/2026-11-10-diamond-steinig-coefficient-test-review-295.md.
It inspected these statements and proofs. Only their finite
coefficient specialization is used; no asymptotic sieve theorem,
distribution hypothesis, or growing-order prime estimate is imported.
The source's Lambda^(t) is Lambda(log)^(t-1)/(t-1)!, not
mu*(log)^t. No general arithmetic identity or source bound is reproved.

The new local calculation is just the lower bound (2), using the
standard multinomial theorem. The finite maximization argument is
given to verify the balanced coefficient in this specialization.
No originality beyond the checked sources is asserted.

### An admissible single coefficient

Take n=3m and set k_1=k_2=k_3=m, with every other component zero.
Its weighted sum is (1+2+3)*m=6m=2n and its length is 3m=n,
so it belongs to K_n, including the allowed length boundary.
Its exact contribution to the first sum in (1), including 2n, is

    6m*(3m-1)!/(m!)^3 * (1!*2!*3!)^(-m)
       =2*(3m)!/(m!)^3 *12^(-m).                            (5)

All other terms in BOTH sums of (1) are nonnegative. Thus (5) is
a lower bound for the full prescribed mass, without changing its
second family, ordering convention, signs, or factorial weights.

### A uniform lower bound for the balanced multinomial coefficient

For nonnegative integers a,b,c with a+b+c=3m, define
T(a,b,c)=(3m)!/(a!*b!*c!). If a>=b+2, moving one unit from a to b
multiplies T by a/(b+1)>1. A maximizer over this finite set therefore
has every two coordinates differing by at most one. Since their sum
is divisible by three, its coordinates must all equal m. Hence

    T(a,b,c)<=T(m,m,m).

There are sum_(a=0)^(3m) (3m-a+1)=binom(3m+2,2) such triples.
By the multinomial theorem their T values sum to
(1+1+1)^(3m)=27^m. Therefore

    (3m)!/(m!)^3 >=27^m/binom(3m+2,2).                      (6)

Substitution into (5) proves (2), since 27/12=9/4.

### Growth-rate test and its limits

Because max(1,M_(3m))>=M_(3m)>0, (2) gives

    log(max(1,M_(3m)))/(3m)
       >=log(9/4)/3
          +(log(2)-log(binom(3m+2,2)))/(3m).

The final term tends to zero: the binomial coefficient is a positive
quadratic polynomial in m. Taking the limsup along n=3m gives the
lower bound for the full limsup in (3). This is strictly positive
because 9/4>1. Equation (4), whose right side is >=1 for all n>=1,
gives the upper bound log(2) after taking logarithms and dividing by n.
No exact asymptotic or existence of a limit is claimed or needed.

In particular, if 0<epsilon<log(9/4)/3, (2) rules out any finite
C_epsilon with M_n<=C_epsilon*exp(epsilon*n) for every n. It does
not rule out arithmetic factors supplying a compensating exponential
saving, unequal termwise estimates, or cancellations retained before
absolute values. Actual factor norms, signed correlations, the exact
Laguerre reconstruction, prime powers, endpoints, compensation,
complements and regulator/infinite-zero control remain unpaid.
This finite coefficient argument uses no local lemma as a mathematical
input; L984 is downstream motivation only.

Step296, 10 November 2026: RESEARCH / REPRODUCTION / NEGATIVE under
the prior SPECIALIZE review295. This is a local quantitative
specialization of an inspected known identity, not a new prime
estimate, a certified novelty claim, or an RH candidate. The complete
proof above is the certificate; no mathematical script or finite
numerical preview is needed to decide the asymptotic test.

## Mathlib

Full matching coverage for (1)-(3) is unchecked and unknown. The
multinomial theorem and elementary factorial arithmetic are standard
supporting mathematics; no matching formal theorem name has been
verified. No absence claim is made.
