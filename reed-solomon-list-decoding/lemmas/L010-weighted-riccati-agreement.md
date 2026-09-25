# L010 — Weighted agreement for Riccati solutions

## Hypotheses

Let F be a finite field of odd characteristic p and cardinality q. Fix
distinct evaluation points x_1,...,x_n, integers 1<=k<=A<=n and m>=1,
a nonzero polynomial a, and polynomials b_j,c_j,d_j for 1<=j<=m, with
b_j nonzero. Count degree-less-than-k tuples satisfying

\[
 aP_j'+b_jP_j^2+c_jP_j+d_j=0 \quad(1\le j\le m)
 \tag{1}
\]

and agreeing with a fixed received word y in at least A simultaneous
columns. Denote their number by M. Derivatives are ordinary formal
derivatives; zero polynomials are allowed. Use the closed column-Hamming
convention in the [pinned model](../foundations/02-pinned-list-model.md).
The hypotheses do not put the entire RS list in (1).

Set

\[
 D=k-1,\quad e=|\{i:a(x_i)=0\}|,\quad N=n-e,\quad
 V=n+(p-1)e,\quad W_A=pA-(p-1)\max(0,A-N).
 \tag{2}
\]

## Conclusion

If p A^2>V D, then

\[
 M\le J:=\left\lfloor
       \frac{V(W_A-D)}{pA^2-VD}\right\rfloor.
 \tag{3}
\]

There is no exponent m. Equivalently, the positivity condition is

\[
 A^2>(k-1)\left(e+\frac{n-e}{p}\right).
 \tag{4}
\]

At e=n, (3) is exactly the ordinary pairwise root bound
floor(n(A-D)/(A^2-nD)). At e=0 one can strengthen it, by integer
rounding of the pair budget, to

\[
 M\le\left\lfloor\frac{n(A-h)}{A^2-nh}\right\rfloor,
 \qquad h=\lfloor D/p\rfloor,\quad A^2>nh.
 \tag{5}
\]

The estimate (5) recovers the L007 count for this nonlinear solution
set without asserting that it is a single derivative fiber.

For a rate R=k/n and 0<=gamma<=1-R, put A=k+ceil(gamma n). If
e<=rho n with 0<=rho<=1, define

\[
 \lambda=\rho+(1-\rho)/p,\qquad
 \eta=(R+\gamma)^2-R\lambda.
 \tag{6}
\]

If eta>=0, then (3) applies and M<=pn, including eta=0. If eta>0,
the constant bound M<=p lambda/eta also holds. Thus the limiting
sufficient slack is max(0,sqrt(R lambda)-R), with equality allowed.
At zero slack a sufficient condition is

\[
 \rho\le\frac{pR-1}{p-1},
 \tag{7}
\]

when the right side is nonnegative. For example:

| Rate R | Characteristic p | Sufficient e/n at A=k |
| --- | --- | --- |
| 1/2 | 3 | at most 1/4 |
| 1/4 | 5 | at most 1/16 |
| 1/8 | 11 | at most 3/80 |
| 1/16 | 17 | at most 1/256 |

Strict inequality in (7) gives the constant case of (6). These are
sufficient conditions, not sharp boundaries. Weights 3 in place of p
are valid in every odd characteristic; all the bounds and conditions
(2)--(4), (6)--(7) with that replacement therefore hold uniformly over
odd characteristics, giving M<=3n when their eta is nonnegative.

The raw-solution obstruction in L009 has a concrete filtered resolution
on an infinite subsequence. Set p=3, let s>=3 be odd, Q=3^s, k the least
power of two at least Q, and n=2k. Over any finite extension containing
F_Q and a multiplicative subgroup H of order n, take H as the evaluation
domain. For all m rows use

\[
 (X^Q-X)P_j'+P_j^2+P_j=0.
 \tag{8}
\]

Then e=2 and every received word has at most four solution tuples
agreeing in at least k columns. In contrast, L009 supplies at least
3^((s^2-1)/4) unfiltered scalar solutions of degree less than k for
this same equation. The four-candidate bound applies to all polynomial
solutions of (8) in the degree cutoff, not merely that constructed subset.

To make a bound J here meet the target for this family's contribution,
one still needs J<=epsilon* q for the given field. For example,
q>=epsilon*^(-1)pn suffices in the nonnegative-eta case, and
q>=4 epsilon*^(-1) suffices for (8). The source's existence proviso does
not imply those stronger conditions. No control of e for a general
interpolant, cover by equations of the form (1), or sharp full-code
boundary is asserted. A nonpositive denominator is not a large-list
witness. The improvement can disappear when a vanishes on the domain.

## Proof

**Multiplicity of a pairwise difference.** If P_j and Q_j are solutions
of the same row equation, their difference U=P_j-Q_j satisfies

\[
 aU'+(b_j(P_j+Q_j)+c_j)U=0.
 \tag{9}
\]

Suppose U is nonzero and x is one of its roots with a(x) nonzero. Write
U=(X-x)^t v with t>=1 and v(x) nonzero. If p does not divide t, then

\[
 U'=(X-x)^{t-1}(t v+(X-x)v')
\]

has order exactly t-1 at x. Multiplication by a preserves this order.
The second summand of (9) has order at least t, or is zero. They
cannot sum to zero, a contradiction. Thus p divides t, and t>=p.
At an evaluation root where a vanishes, the order is at least one.

Give column i weight w_i=p when a(x_i) is nonzero and weight 1 otherwise.
Two distinct tuples differ in at least one row. In such a row, their
nonzero difference has degree at most D, and every column of simultaneous
agreement is a root. The product of its distinct linear root factors
with their multiplicities divides that difference. Degree comparison
therefore gives

\[
 \sum_{i:\,P(x_i)=Q(x_i)}w_i\le D.
 \tag{10}
\]

This step needs no common homogeneous kernel for the different pairs.

**Weighted incidence count.** There is nothing to prove when M=0.
Otherwise choose exactly A agreeing columns for each candidate and
let l_i be the number of chosen sets containing i. Then sum_i l_i=MA.
For a chosen set of size A at least max(0,A-N) points are exceptional,
so its weight is at most W_A. Consequently

\[
 \sum_i w_i l_i\le M W_A,\qquad
 \sum_i w_i l_i(l_i-1)\le M(M-1)D.
 \tag{11}
\]

The second inequality counts ordered pairs and uses (10). Applying
Cauchy--Schwarz to sqrt(w_i) l_i and 1/sqrt(w_i) gives

\[
 (MA)^2\le\left(\sum_i w_i l_i^2\right)
                 \left(\sum_i1/w_i\right),\qquad
 \sum_i1/w_i=e+N/p=V/p.
 \tag{12}
\]

Combining (11)--(12), multiplying by V, and dividing by M>0 yields

\[
 M(pA^2-VD)\le V(W_A-D).
 \tag{13}
\]

Since W_A>=A>=k>D, the right side is positive. Dividing when the
coefficient on the left is positive and taking the integer floor proves
(3). This counts tuples directly, so m never enters the inequality.
Degree less than k<=n also ensures distinct tuples give distinct
evaluation words, by the polynomial root bound in a differing row.

For e=n, V=pn and W_A=A, giving the asserted ordinary bound. For e=0,
each pair agrees in at most h=floor(D/p) columns by (10). In the same
calculation replace its pair budget D by ph and use V=n, W_A=pA.
Canceling p yields (5). This also covers k=1 and h=0 without division
by zero in a positive-denominator case.

**Slack, integer correction, and uniform characteristic.** From e<=rho n
we have V<=p lambda n. Since D=Rn-1 and A>=(R+gamma)n,

\[
 pA^2-VD
 =pA^2-VRn+V
 \ge p n^2\eta+V.
 \tag{14}
\]

When eta>=0 this is at least V>0. Formula (3) gives
M<=W_A-D<=pn. When eta>0 its numerator is at most
V W_A<=p^2 lambda n^2, proving M<=p lambda/eta. This proves (6)--(7)
and retains the positive correction at equality. The table substitutes
the displayed rates and primes in (7).

The multiplicity at a regular root is at least p>=3. Giving such roots
weight 3 preserves (10), and every subsequent counting step uses only
the chosen weights. Repeating it with 3 proves the stated uniform
odd-characteristic bounds. This does not change the derivative's actual
characteristic or claim divisibility of multiplicities by 3 for p>3.

**Filtering the earlier obstruction on a smooth domain.** The standard
finite-field subfield theorem identifies the roots of X^Q-X with F_Q.
Its roots in H are H intersect F_Q^*. In the cyclic group F^*,
subgroups of orders n and Q-1 have an intersection of order gcd(n,Q-1).
Indeed, if g generates F^* of order q-1, those two subgroups are generated
by g^((q-1)/n) and g^((q-1)/(Q-1)); their intersection is generated by
the power with exponent the least common multiple of those exponents.
Its order is gcd(n,Q-1). Thus e=gcd(n,3^s-1).

For odd s, 3^s is 3 modulo 4, so 3^s-1 has exactly one factor of 2.
As n is a power of two, e=2. Also s>=3 implies Q>=27, k>=32, and
n>=64. At A=k=n/2, N=n-2>=A, so W_A=3n/2 and V=n+4. Formula (3)
becomes

\[
 M\le\left\lfloor
      \frac{(n+4)(n+1)}{n^2/4-n+4}
      \right\rfloor\le4.
 \tag{15}
\]

The denominator is positive for n>=64. The ratio is less than 5
because five times its denominator minus its numerator is
n^2/4-10n+16=n(n/4-10)+16>0 at those n. Integrality proves the last
inequality. L009's subspace construction gives the stated number of
unfiltered solutions, with degree less than Q<=k. It also supplies
compatible fields: take an extension degree divisible by s and the
multiplicative order of 3 modulo n. Thus the comparison is for actual
equations and pinned smooth-domain parameters, not only a formal
coefficient pattern. It does not prove that every nearby RS codeword
satisfies (8), nor does it change a specified instance's field.

The general multiplicity and counting proofs above are symbolic.
`python3 scripts/weighted-riccati/verify.py` supplies additional exact
finite checks, including enumeration of centers up to their agreement
patterns, simultaneous two-row agreement, an attained regular-root
multiplicity p, and the numerical constants in (15). Its output is
retained in `scripts/weighted-riccati/results.json`; it is not a check
of the full prize boundary.

## Mathlib

Full weighted Riccati agreement statement and its smooth-domain
specialization: **not checked** in Mathlib. Supporting formal derivatives,
root multiplicities, weighted Cauchy--Schwarz, polynomial root bounds,
finite-field subfields, and cyclic subgroup intersections: **not checked**
in this step. The finite-field subfield theorem and cyclicity of the
multiplicative group of a finite field are standard named supporting
results, not matches for the full statement. The other arguments are
supplied above; L009 supplies the unfiltered subspace construction used
in the comparison. No full matching library theorem or novelty claim for
the incidence method is asserted.
