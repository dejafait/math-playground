# Corollary 919e: conditional fixed-box three-node Gram margin

## Hypotheses

Let x_1,x_2,x_3 be hypothetical real numbers satisfying exactly

    14 <= x_1 <= 29/2,
    41/2 <= x_2 <= 43/2,
    49/2 <= x_3 <= 51/2.

Put

    w(x)=(x^(-2),200*x^(-4),40000*x^(-6))^T,
    W=[w(x_1) w(x_2) w(x_3)],
    G=W W^T=sum_(j=1)^3 w(x_j)w(x_j)^T.

All matrices here are real. The transpose is the ordinary transpose.
There is no parameter, heat-flow premise, actual zero placement,
initial simplicity, multiplicity count or Decimal arithmetic contract.
In particular the intervals are hypotheses, not certified zero brackets.

## Conclusion

Uniformly over this entire closed box,

    lambda_min(G) >= 1/B > 1/700000000 > 1/2000000000,

where the exact inverse Frobenius square enclosure is

    B=9038116652331572962135737621217329139050385873
      /13463243595254160685006848000000000000.

The decimal 1/B approximately 1.48960719508e-9 is explanatory only;
the conclusion uses rational inequalities. This is a quantitative
specialization of published finite-matrix methods, not a new general
theorem or progress beyond the sources checked. It supplies a candidate
selected contribution at C919c's threshold only if actual placement and
the sign of the rest of the rectangular head are separately justified.
No actual H2 sign, all-degree sign or RH conclusion follows here.
The independent step2164 audit accepts this conditional calculation
with exactly these hypotheses and constants.

## Proof

### Imported finite-matrix facts and exact normalization

Import the explicit inverse Vandermonde formula from Walter Gautschi,
*Norm Estimates for Inverses of Vandermonde Matrices*, Numerische
Mathematik 23 (1975), 337-347, Section 3, printed p.339,
(3.1)-(3.4), with Section 4, p.340, (4.1)-(4.1'):
https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/051.pdf.
For the matrix whose j-th column is (1,y_j,...,y_j^(n-1))^T at
distinct nodes, row j of its inverse consists of the coefficients
of the j-th Lagrange basis polynomial in increasing degree order.
Use only this formula, not an identification of the infinity and
Euclidean norms. Its proof was inspected in the step2161 assessment;
it is not reproved here.

For the finite real matrix norm and SVD implications import Stephen
Boyd and Lieven Vandenberghe, *Convex Optimization*, Cambridge
University Press (2004), corrected seventh printing (2009),
Appendix A, A.1.1 (A.1)-(A.2), pp.633-634; A.1.5, p.636;
A.5.4 (A.12), pp.648-649:
https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf.
These give the Frobenius and induced Euclidean norm conventions,
the bound ||M||_2<=||M||_F, transpose invariance of the Euclidean
norm, and, for invertible W, lambda_min(W W^T)=||W^(-1)||_2^(-2).
Only their finite real full-rank cases are used. No infinite operator,
determinant-only eigenvalue estimate or interpolation error is used.

Set y_j=200/x_j^2. Monotonicity on the positive x axis gives

    y_1 in [a_1,b_1]=[800/841,50/49],
    y_2 in [a_2,b_2]=[800/1849,800/1681],
    y_3 in [a_3,b_3]=[800/2601,800/2401].

Let V have columns (1,y_j,y_j^2)^T. Directly from the weights,

    w(x_j)=(y_j,y_j^2,y_j^3)^T/200,
    W=(1/200) V diag(y_1,y_2,y_3).

All diagonal entries are positive. Below the nodes are proved distinct,
so the cited formula applies and

    W^(-1)=200 diag(1/y_1,1/y_2,1/y_3) V^(-1).

For {j,k,l}={1,2,3}, the j-th inverse row is therefore exactly

    200/(y_j*(y_j-y_k)*(y_j-y_l))
            * (y_k*y_l, -(y_k+y_l), 1).                  (1)

This tracks both the column convention and the extra y_j weight.
The argument is a specialization of the imported formula; the source
does not supply these weighted entries or the following constants.

### One enclosure on the full box

For j<k put g_jk=a_j-b_k. Exact subtraction gives

    g_12=672000/1413721 > 0,
    g_13=1248000/2019241 > 0,
    g_23=441600/4439449 > 0.

Thus y_1>y_2>y_3>0 everywhere, including every endpoint, and
|y_j-y_k|>=g_min(j,k),max(j,k). Write g_kj=g_jk when k>j.
For each row put d_j=a_j*g_jk*g_jl, a strictly positive number.
Equation (1), positivity of the nodes and the triangle inequality give
the following single entrywise magnitude enclosure:

    (|W^(-1)_(j,1)|,|W^(-1)_(j,2)|,|W^(-1)_(j,3)|)
       <= (200*b_k*b_l,200*(b_k+b_l),200)/d_j.            (2)

There is no subdivision or tuning, and no claim that incompatible
endpoint maxima can be simultaneously attained: independent upper
bounds are sufficient for (2). The exact d_j are

    d_1=95846400000000/342965014892143,
    d_2=33914880000000/1657798153602703,
    d_3=48988160000000/2590687739642401.

Evaluating (2) gives the matrix of positive magnitude upper bounds

    [ 594823321/5241600,
      93387261397/161280000,
      342965014892143/479232000000 ],

    [ 4833230768521/1454100480,
      62831999990773/4748083200,
      1657798153602703/169574400000 ],

    [ 52871178360049/10293637120,
      26065490931504157/1646981939200,
      2590687739642401/244940800000 ].

Rows are displayed on separate lines; these are not interval samples.
The inverse sign pattern from (1) is (+,-,+),(-,+,-),(+,-,+).
Hence each positive sign entry is in [0,U], and each negative sign
entry in [-U,0], for its displayed magnitude upper bound U.
The certificate records all nine full signed inclusions as well.

The sums of squares of the three rows of (2) are, respectively,

    3227226392249942642329850416667
      /3751167393792000000000000,
    317712030479081613005065059830715047
      /1127684376499322880000000000,
    65901247445416384478623542187414481061
      /169534344253187031040000000000.

Their exact sum is B as displayed in the conclusion. Consequently
||W^(-1)||_F^2<=B. To make the strict comparison independently
checkable, write B=N/D with the displayed positive denominator D.
The integer cross product at the simpler reporting cap is

    700000000*D-N
      =386153864346339517369055978782670860949614127 > 0.

Thus B<700000000<2000000000. The cited SVD/norm implication now gives

    lambda_min(G)=1/||W^(-1)||_2^2
                 >=1/||W^(-1)||_F^2>=1/B
                 >1/700000000>1/2000000000.

The original threshold comparison also has the positive cross product

    2000000000*D-N
      =17888370538176748407877958378782670860949614127.

This proves the stated uniform bound. It does not use rounded
eigenvalues, a positive determinant as a quantitative substitute,
or any assertion that the nodes arise from zeros.

### Reproduction and limitations

Run from the active notebook:

    python3 scripts/h2-head/fixed_box_gram_2162.py

The full exact certificate is
`scripts/h2-head/fixed_box_gram_2162.json`. It retains every original
endpoint, transformed endpoint, separation, positive denominator,
numerator upper bound, inverse-entry enclosure, row square, total norm
bound, threshold, strict difference, integer comparison and failure.
Python Fraction integer arithmetic supplies every inclusion operand;
floats occur only in the printed explanatory decimal. The relevant
full certificate rows, all transformed endpoints, all separations and
both comparisons were inspected in this step, not accepted from a
bounded preview. All recorded failures are empty.

This result passes the single frozen-box test under the unchanged
step2161 SPECIALIZE assessment and is classified REPRODUCTION.
C919c motivates the threshold but is not a mathematical premise of
this self-contained real matrix inequality. C919d's qualitative
reality does not place three distinct opposite classes in these boxes.
An actual-family application still needs that independent placement,
with initial multiplicities and zero time covered, and a justification
for retaining the remaining head terms. The actual boundary premises
would retain their inherited arithmetic contracts. The earlier
outer-only, inner-evaluator and L917/L920/L922 stops are unchanged.
No claim about higher-degree positivity or a global implication is made.

### Independent arithmetic and normalization audit, 21 November 2026 (step2164)

**Verdict.** Accepted on the entire stated closed box. No mathematical
formula, rational constant, hypothesis or dependency needed correction.
This is the first independent audit of the saved specialization, not
a stronger bound or a new theorem beyond the checked sources. The
unchanged ready step2162 audit assessment supplies SPECIALIZE coverage;
the completed audit is classified REPRODUCTION.

**Orientation and full-box validity.** With the source's column
convention, multiplying V on the right by diag(y)/200 scales its
columns. Inversion therefore places 200 diag(1/y) on the left of
V inverse, so the factor in (1) is 200/y_j, not a common row factor
200 alone. Monotonicity of 200/x^2 at positive x verifies all six
transformed endpoints. Each of the three exact gaps is strictly
positive, including endpoints; this verifies both invertibility
and the denominator signs +,-,+. Products and sums in the numerator
are positive, giving the displayed signed pattern. Taking each
numerator upper bound and denominator lower bound separately is valid
at every point of the box. No simultaneous-extremum premise, vertex
sampling or interval subdivision is required.

**Independent exact arithmetic.** The audit script uses q_j=1/x_j^2
instead of y_j and the alternative factorization

    W=diag(1,200,40000) V(q) diag(q).

Thus the absolute inverse-row numerator bounds in q coordinates are

    (q_k^+ q_l^+, (q_k^++q_l^+)/200, 1/40000),

divided by q_j^- times the two positive q-gap lower bounds. This
tracks the scaling independently of the original generator. Conversion
back to y gives every saved denominator, numerator, all nine magnitude
bounds and all nine signed enclosures exactly. The three row squares,
their sum B, reciprocal, strict threshold difference, and both integer
cross products agree exactly as well. Every displayed endpoint, gap,
denominator, magnitude bound, row square and B in this proof was checked
against those reconstructed rationals; both displayed cross products
also agree. All 55 recorded checks pass, with no recorded failures.

Run from the active notebook:

    python3 scripts/h2-head/fixed_box_gram_audit_2164.py

Its full evidence is `scripts/h2-head/fixed_box_gram_audit_2164.json`.
The script reads every field of the original arithmetic certificate
without importing its generator or changing either original artifact.
The relevant original certificate fields and complete audit check and
scalar records were inspected; acceptance does not rest on previews
or on the printed PASS label. The analytic interval argument above,
together with exact operands, is what establishes uniformity.

**Norm direction and limits.** For real invertible W, the imported
finite-dimensional norm/SVD facts give
lambda_min(W W^T)=1/||W inverse||_2^2. Since
||W inverse||_2^2<=||W inverse||_F^2<=B and B>0, taking reciprocals
gives the claimed lower bound. The two strictly positive cross
products establish the strict comparisons without rounded eigenvalues.
There is no use of Gautschi's infinity norm as a Euclidean norm.

C919c's weights and threshold match the audited ones, but neither
C919c nor C919d is a mathematical premise of this real-matrix
inequality. The result only supplies a candidate selected head
contribution. This audit supplies no actual three-class placement,
does not certify the imported propagation argument in C919d, and
does not strengthen any inherited Decimal contract. In an actual
application, positivity of all unselected head terms must be justified
from paid actual-family inputs, rather than inferred from this bound.
Initial multiplicities and zero time cannot be omitted. The parked
confinement and earlier evaluator/moment stops remain unchanged;
all-degree and global positivity remain open.

## Mathlib

Full matching coverage of this weighted rational box inequality has
not been checked. The imported sources provide the mathematical
finite-matrix facts; no matching Mathlib theorem is asserted. Unknown
coverage is not evidence of absence. The exact certificate is a
reproducible informal arithmetic check, not a formal Lean verification.
