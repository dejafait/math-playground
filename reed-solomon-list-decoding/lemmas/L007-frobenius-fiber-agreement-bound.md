# L007 — Agreement bounds inside a Frobenius fiber

## Hypotheses

Let F be a finite field of characteristic p and cardinality q. Let
x_1,...,x_n be distinct elements of F, with 1<=k<=n and m>=1. Use
simultaneous column agreement and closed balls as in the
[pinned model](../foundations/02-pinned-list-model.md). Put

\[
 h=\left\lfloor\frac{k-1}{p}\right\rfloor,\qquad
 \mathcal K_{p,k}=\{P\in F[X]:\deg P<k,\ P^{[1]}=0\}.
\]

Here the first Hasse derivative is the ordinary formal derivative, and
the zero polynomial is included. Fix a tuple P_0 of m polynomials of
degree less than k. For a received word y in (F^m)^n and an integer
1<=A<=n, let M(y,A;P_0) be the number of tuples in the affine family

\[
 P_0+\mathcal K_{p,k}^{\,m}
\]

whose evaluations agree with y in at least A columns. Evaluation is
injective in the degree range, so this also counts distinct codewords.
The hypotheses do not say that the full RS list lies in this family.

## Conclusion

The family is exactly

\[
 P_0+\{(H_1(X^p),\ldots,H_m(X^p)):\deg H_j\le h\}.
 \tag{1}
\]

After subtracting the evaluations of P_0 from the center, its filtered
list is an interleaved RS list of degree at most h on the distinct
points x_i^p. In particular, whenever A^2>nh,

\[
 M(y,A;P_0)\le J(n,k,p,A):=
 \left\lfloor\frac{n(A-h)}{A^2-nh}\right\rfloor.
 \tag{2}
\]

There is no exponent m in this bound. It applies, in particular, to
any nonempty fiber of a prescribed first derivative in each row.
The exact integer condition is A>=floor(sqrt(nh))+1.

For k=Rn integral, fixed p and R, and 0<=gamma<=1-R, set
A=k+ceil(gamma n), a=R+gamma, and eta=a^2-R/p. Then:

- If eta>0, (2) gives M<=1/eta, independently of n, q, and m.
- If eta=0, its denominator remains positive and M<=pn.
- If eta<0, the denominator is nonpositive for all sufficiently large
  such n. The displayed second-moment inequality then supplies no upper
  bound. This is not evidence of a large list or a failure of other
  agreement-counting arguments.

Thus this estimate gives a polynomial bound at fixed parameters for
gamma>=max(0,sqrt(R/p)-R), including equality. A strictly positive eta
gives a constant bound.

For the pinned smooth domains, n>=16 is a power of two and n divides
q-1, so p is odd. Write R=1/s for s in {2,4,8,16}. At A=k and p>s,
the stronger integer form is

\[
 M(y,k;P_0)\le
 \left\lceil\frac{s(p-1)}{p-s}\right\rceil-1.
 \tag{3}
\]

Its largest value over the indicated prime characteristics is:

| Rate | Characteristics covered at A=k | Uniform upper bound | Remaining admissible primes below s |
| --- | --- | --- | --- |
| 1/2 | p>=3 | 3 | none |
| 1/4 | p>=5 | 15 | 3 |
| 1/8 | p>=11 | 26 | 3, 5, 7 |
| 1/16 | p>=17 | 255 | 3, 5, 7, 11, 13 |

For each remaining prime the slack cutoff is exactly the sufficient
value gamma_c=1/sqrt(sp)-1/s for this asymptotic estimate. The largest
cutoff, over admissible primes, is attained at p=3: it is
1/sqrt(12)-1/4, 1/sqrt(24)-1/8, and 1/sqrt(48)-1/16 for the last three
rates, respectively. Finite n must still be tested with A^2>nh; some
smaller finite instances already satisfy it below the limiting cutoff.

For 0<epsilon<1, the explicit sufficient condition

\[
 q\ge\epsilon^{-1}J(n,k,p,A) \tag{4}
\]

makes this family's contribution at most epsilon q. It does not bound
the full RS list unless a separate argument puts that list in this
family. A union of T such families would only give T J by summation;
no polynomial bound on T is asserted. Neither (4) nor a bound for one
family locates the sharp boundary of the original code.

## Proof

**Kernel and reduction.** Write P=sum_j b_j X^j. Its first derivative
is sum_{j>=1} j b_j X^(j-1). Distinct monomials have distinct exponents,
so this derivative vanishes exactly when b_j=0 for every j not divisible
by p. The surviving coefficients give uniquely
P(X)=H(X^p), with deg H<=floor((k-1)/p)=h. This proves (1).
Subtracting P_0 translates the received word and preserves agreement
column by column. No transformation of the values by a pth root is
being made: H(X^p) at x_i is literally H(x_i^p).

If u^p=v^p in a field of characteristic p, then (u-v)^p=0, so u=v.
Thus the new evaluation points are distinct. A nonzero polynomial of
degree at most h has at most h distinct roots: factoring X-a for each
successive distinct root proves this by degree comparison. As h<n,
evaluation on the new points is injective. The same root argument in
degree less than k proves injectivity for the original tuples.

For two distinct tuples H and H', choose a row in which they differ.
Every column of simultaneous agreement is a root of that row's
nonzero difference, whose degree is at most h. The tuples therefore
agree in at most h columns, regardless of m. Addition of P_0 does not
change these pairwise agreement sets. Also, two tuples with the same
prescribed derivatives differ by an element of the displayed kernel
in every row; a nonempty derivative fiber is exactly such a translate.

**Second-moment count.** Fix y, and put M=M(y,A;P_0). If M=0 there is
nothing to prove. Otherwise, for each candidate choose exactly A of its
agreeing columns. The intersection of two chosen sets has size at most
h by the preceding root argument. Let l_i be the number of chosen sets
containing column i. Counting incidences and ordered pairs gives

\[
 \sum_i l_i=MA,\qquad
 \sum_i l_i(l_i-1)\le M(M-1)h.
\]

Cauchy--Schwarz, or expansion of
sum_i(l_i-MA/n)^2>=0, yields

\[
 \frac{M^2A^2}{n}\le\sum_i l_i^2
 \le MA+M(M-1)h.
\]

Multiply by n and divide by M>0 to obtain

\[
 M(A^2-nh)\le n(A-h). \tag{5}
\]

If A^2>nh, then A>h: otherwise A^2<=h^2<=nh, since h<n.
The denominator and numerator in (2) are consequently positive.
Division and integrality prove (2). The integer cutoff follows directly
by squaring nonnegative integers. This is the elementary Johnson
second-moment argument, proved here rather than imported as a black
box. Its application uses common column agreement, so separate row
list bounds and their mth powers are unnecessary.

**Slack and rounding.** The exact floor gives

\[
 h\le\frac{Rn-1}{p},\qquad
 h\ge\frac{Rn}{p}-1,
\]

where the second inequality follows from
h+1=ceil(k/p)>=k/p. Also a n<=A<=a n+1 and A<=n. Hence

\[
 A^2-nh\ge\eta n^2+\frac np. \tag{6}
\]

For eta>0, use n(A-h)<=n^2 in (2) to get M<=1/eta.
For eta=0, (6) is still positive and (2) gives
M<=p(A-h)<=pn. This retains the helpful floor correction at the
limiting Johnson threshold.

Conversely the other rounding bounds imply

\[
 A^2-nh\le\eta n^2+(2a+1)n+1. \tag{7}
\]

If eta<0 and p,R,gamma are fixed, the right side is negative for all
sufficiently large n. Since A>=k>h, the right side of (5) stays positive
while its left side is nonpositive. Inequality (5) then imposes no upper
bound on M. This explains the scope of the failed test without
claiming that any actual list is large. In particular, at exact finite
denominator zero, finer arguments could still help.

**Smooth domains and the four rates.** If the domain is aH with a!=0
and H a subgroup of F^* of size n, Lagrange's theorem gives n|(q-1).
Even n is incompatible with characteristic two. Moreover Frobenius
maps H injectively into H, hence bijectively since H is finite. It maps
aH onto a^p H, another smooth domain of the same size. The reduction
therefore preserves the pinned domain class, though its message degree
is the smaller h, not the original k-1.

At rate 1/s, take A=k=n/s. For p>s, the inequality h<k/p implies
k^2>nh. For real z<k^2/n, put f(z)=n(k-z)/(k^2-nz).
On this interval its derivative is
n k(n-k)/(k^2-nz)^2, strictly positive because k<n.
Consequently

\[
 \frac{n(k-h)}{k^2-nh}
 < \frac{n(k-k/p)}{k^2-nk/p}
 =\frac{s(p-1)}{p-s}.
\]

An integer strictly below the last expression is at most its ceiling
minus one, proving (3). For fixed s>1 the expression decreases with
p, since its derivative is s(1-s)/(p-s)^2<0. The least primes above
s=2,4,8,16 are 3,5,11,17. Substitution gives respectively
4,16,80/3,256 before the strict integer rounding, and thus
3,15,26,255 afterward. The remaining primes and slack values in the
table now follow from eta=(1/s+gamma)^2-1/(sp). No pinned case has
p=s, since s is an even power of two and p is odd.

**Threshold comparison and checks.** Equation (4) follows by multiplying
through (2). The count covers only a fixed affine family. Counting
all fibers without controlling their number could introduce a power
of q and lose the required comparison with epsilon q. This is why
the family estimate is not a full small-characteristic extension of
the interpolation/cover argument.

As a finite test, take p=3, n=16, k=4, so h=1. A smooth domain exists
in F_81 since its cyclic multiplicative group has order 80 and hence
a subgroup of order 16. At A=4, A^2-nh=0, so (5) alone gives no upper
bound. At A=5 the denominator is 9, and (2) gives floor(64/9)=7.
Neither calculation asserts an exact list size. If h=0, (2) reduces
to floor(n/A), correctly counting distinct constant tuples by their
disjoint agreement sets. At A=n it gives 1, as injectivity requires.

The arithmetic check `python3 scripts/frobenius-filter/verify.py`
reproduces the rate table and tests the strict integer bound, exact
cutoff, and equality-slack rounding over its stated finite grid.
Its output is `scripts/frobenius-filter/results.json`. These checks
test arithmetic and edge cases, not the theorem for all parameters or
the sharp list size of any code; the proof above is symbolic.

## Mathlib

Full Frobenius-fiber agreement statement: **not checked** in Mathlib.
Supporting formal-derivative kernels, Frobenius injectivity, the
polynomial root bound, Cauchy--Schwarz, and finite-field multiplicative
groups: **not checked** in this step. The proof supplies the needed
arguments and uses the standard Lagrange theorem and cyclicity of the
multiplicative group of a finite field for the smooth-domain discussion.
No matching Mathlib theorem, novelty claim for the Johnson count, or
small-characteristic theorem for general differential equations is
asserted.
