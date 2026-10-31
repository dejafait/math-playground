# Lemma 511: individual compensation without a conserved joint allocation

## Hypotheses

Set h=11/16 and r=5/4. For c in {h,-h}, real x, define

    K_c(x)=2((x-c)^2-1)/((x-c)^2+1)^2.

For x!=+/-r put

    F_c(x)=K_c(x)+1/(x+r)^2+1/(x-r)^2,
    H(x)=K_h(x)+K_{-h}(x)+1/(x+r)^2+1/(x-r)^2.

An allowed allocation has four nonnegative real constants
alpha_h, alpha_{-h}, beta_h, beta_{-h}, with

    alpha_h+alpha_{-h}<=1,   beta_h+beta_{-h}<=1.

Each pair displacement and each real-zero budget is one. These are
finite rational functions; no actual-Xi geometry, fractional zero
multiplicities or infinite assembly is assumed.

## Conclusion

On the entire domain x!=+/-r, both F_c(x)>0 and H(x)>0.
Nevertheless no allowed allocation makes both functions

    K_c(x)+alpha_c/(x+r)^2+beta_c/(x-r)^2

nonnegative throughout this domain. Thus individual compensation with
the full budgets and positive aggregate do not imply conserved joint
allocation, even in this symmetric block. Unlike L510's example, neither
pair has an individual full-budget deficit. This is a finite first-sign
obstruction, not an RH result. Its fixed-example proof passed the
independent critical audit described below.

## Proof

### Common denominators and full-domain signs

Put A(x)=(x-h)^2+1, B(x)=(x+h)^2+1 and M(x)=x^2-25/16.
Since A,B>=1 and M!=0 on the domain, the denominators below are
strictly positive. Direct addition gives

    A(x)^2 M(x)^2 F_h(x)=P(x),
    A(x)^2 B(x)^2 M(x)^2 H(x)=Q(x^2),                 (1)

where the coefficient vectors in increasing powers are

    P: (2203225/524288, -158675/8192, 905329/32768,
        -4147/512, 703/128, -33/4, 4),
    Q: (121268016025/34359738368, -43179459359/2147483648,
        424168615/4194304, -25679/8192, -195/64, 6).

For explicit verification of every coefficient in (1), expand

    P=2((x-h)^2-1)M^2+2(x^2+r^2)A^2,
    Q(x^2)=2((x-h)^2-1)B^2 M^2
           +2((x+h)^2-1)A^2 M^2+2(x^2+r^2)A^2 B^2. (2)

The second polynomial in x is even, yielding precisely the Q above.

Here is an exact positivity certificate with all intervals and tails.
For a degree-n polynomial p and rational l<u, write
p(l+(u-l)t)=sum_{i=0}^n a_i t^i and define

    b_k=sum_{i=0}^k a_i binom(k,i)/binom(n,i).

Then the polynomial identity

    p(l+(u-l)t)=sum_{k=0}^n b_k binom(n,k)t^k(1-t)^(n-k) (3)

follows by substituting the b_k and using
binom(n,k)binom(k,i)/binom(n,i)=binom(n-i,k-i).
The inner binomial sum is (t+(1-t))^(n-i)=1, leaving a_i t^i.
On 0<=t<=1 the basis terms in (3) are nonnegative and their sum
is one. Thus p>=min b_k>0 if all b_k>0, including both endpoints.
This elementary identity is provided to justify the certificate; no
positivity theorem or numerical minimization is being assumed.

For P the following rows give all b_k multiplied by 7864320:

| Interval | Scaled Bernstein coefficients, increasing k |
| --- | --- |
| [-2,0] | 6496927095, 1697519735, 731787191, 384678711, 192541431, 83824375, 33048375 |
| [0,1/2] | 33048375, 20354375, 11281691, 5432211, 2587791, 2372335, 4405395 |
| [1/2,1] | 4405395, 6438455, 10720031, 16869675, 24502587, 33383215, 44070375 |
| [1,2] | 44070375, 65444695, 94045143, 134342247, 203516423, 352101815, 716087415 |

These are obtained by the displayed formula from P, with n=6; all
are strictly positive. For z>=0, the power coefficient vectors of
524288 P(2+z) and 524288 P(-2-z), respectively, are

    (47739161, 145594240, 215400208, 181318656,
     85454848, 20840448, 2097152),
    (433128473, 959881472, 958418704, 535841792,
     171962368, 29491200, 2097152).

All coefficients, including both constants, are positive. These tails
and the four closed intervals cover every real x. Hence P(x)>0
everywhere, and (1) proves F_h>0 throughout its punctured domain.
Reflection gives F_{-h}(x)=F_h(-x), so the second individual assertion
holds without an additional hypothesis.

For Q, n=5, the following rows give all b_k multiplied by 171798691840:

| Interval | Scaled Bernstein coefficients, increasing k |
| --- | --- |
| [0,1/2] | 606340080125, 260904405253, 349817392141, 866347445013, 1797219853853, 3154829049125 |
| [1/2,1] | 3154829049125, 4512438244397, 6296784226101, 8520261424701, 11220933411141, 14494745151565 |
| [1,2] | 14494745151565, 21042368632413, 29882551129197, 41782852371069, 58436934410381, 83495353773725 |
| [2,4] | 83495353773725, 133612192500413, 217346380523229, 363902370054909, 633794924896029, 1151834469268285 |

All are strictly positive. The power coefficient vector of
34359738368 Q(4+z) is

    (230366893853657, 259019772186128, 124073494765568,
     31202606055424, 4018478776320, 206158430208).

Again every coefficient is positive, so these intervals and this tail
prove Q(y)>0 for all y>=0. Since y=x^2 covers that half-line, (1)
proves H>0 on the entire domain, not just the numerical search window.

At x=+/-r, each F_c and H has its corresponding positive inverse-square
pole and all other summands bounded. These points remain excluded.
Direct leading-term comparison gives x^2 F_c(x)->4 and x^2 H(x)->6
as |x|->infinity. No uniform positive constant lower bound is claimed.

### Joint-budget contradiction in the original four variables

Take s=9/32, which avoids both poles, and put

    a=1/(s+r)^2=1024/2401,
    b=1/(s-r)^2=1024/961,
    k=K_h(s)=K_{-h}(-s)=-1751040/1423249.

Then 0<a<b and

    k+b=-225342464/1367742289<0.                       (4)

If both allocated functions were nonnegative, their evaluations at
s for c=h and -s for c=-h would give

    0<=k+a alpha_h+b beta_h,
    0<=k+b alpha_{-h}+a beta_{-h}.

Adding, increasing the a coefficients to b using nonnegativity, and
then using both original budgets gives

    0<=2k+a(alpha_h+beta_{-h})+b(beta_h+alpha_{-h})
      <=2k+b(alpha_h+alpha_{-h}+beta_h+beta_{-h})
      <=2(k+b)<0,

a contradiction. No symmetric allocation or reduction of the four
variables has been assumed. Both pair groups are essential to this
contradiction: either pair alone is feasible with its full budgets,
as proved on the entire domain above.

For explicit finite-linear replay, let v=(alpha_h,alpha_{-h},beta_h,
beta_{-h}). The eight rows of Mv<=d, including all nonnegativity
constraints, are

    M=((-a,0,-b,0), (0,-b,0,-a),
       (1,1,0,0), (0,0,1,1),
       (-1,0,0,0), (0,-1,0,0), (0,0,-1,0), (0,0,0,-1)),
    d=(k,k,1,1,0,0,0,0).

The exact multiplier vector is

    lambda=(1,1,b,b,b-a,0,0,b-a)>=0.

One has M^T lambda=0 and
d^T lambda=2(k+b)=-450684928/1367742289<0. Thus summing the
inequalities gives the same contradiction. This is the finite-linear
alternative of Boyd and Vandenberghe, *Convex Optimization*, Cambridge
UP, 2004 (corrected seventh printing 2009), Section 5.8.3, pp. 261–263,
[primary text](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf#page=275).
Only the elementary certificate direction is used; no assertion of
finite completeness for a semi-infinite system or closedness is needed.

### Evidence, provenance and limitations

The unchanged prior EXPLORE assessment is
`drafts/literature/2026-10-30-genuine-shared-budget-competition.md`.
It covers exactly this fixed-h bounded test and the added individual
requirement. The inspected signed identities, zero-count theorems and
finite alternatives did not supply this example or force a decomposition.
That comparison does not certify originality. L509 and L510 are
contrasts, not mathematical inputs to this standalone proof.

Run from the notebook:

    python3 scripts/signed-allocation/genuine_shared_budget.py

The complete rational polynomials, all Bernstein coefficients, tail
coefficients, original matrix and exact multipliers are saved to
`scripts/signed-allocation/genuine-shared-budget-certificate.json`.
The first required candidate r=5/4 succeeded: one of at most eight
candidates and two of at most 32 added pair rows were used. A numerical
diagnostic sampled 60001 x in [-3,3], omitting poles and zero, only to
nominate s=9/32; those samples are not the sign proof or linear rows.
No other r candidate was tested. The script records no failures; all
load-bearing polynomial/dual evidence was inspected in full. The
separate independent critical audit is recorded next.

### Independent critical audit, 30 October 2026

The ready audit scope is
`drafts/literature/2026-10-30-l511-critical-audit-coverage.md`.
Run the independent replay from the notebook:

    python3 scripts/signed-allocation/l511_independent_audit.py

It uses only Python's standard-library exact rational arithmetic and
does not import or execute the original generator. It reconstructs
P and the even numerator Q(x^2) directly from (2), composes polynomials
by Horner evaluation, and obtains the interval coefficients by inverting
the triangular Bernstein-to-power expansion. It compares every numerator,
every interval endpoint and coefficient, and all three tail coefficient
vectors with both the displayed proof and the original certificate.
It also reconstructs the eight original rows from the two evaluation
definitions, checks all four column cancellations, nonnegative
multipliers and the strictly negative dual value. All 79 exact checks
pass, with no failures. The complete independent evidence is
`scripts/signed-allocation/l511-independent-audit.json`.

The minimum certified interval bounds are 474467/1572864 for P and
260904405253/171798691840 for Q. These are numerator bounds on the
listed compact intervals, not uniform positive bounds for F_c or H.
The translated tail coefficients have positive constants and
nonnegative higher coefficients, so the closed intervals and tails
give the entire real domain for P and the entire nonnegative domain
for Q. Formula (3) includes both endpoints because its basis sums to
one there as well. A,B>=1 and M^2>0 away from the two excluded poles
justify division in (1); reflection preserves the excluded set and
gives the other individual sign. At each excluded pole the singular
inverse square has coefficient one, while the other terms stay bounded.
The denominator degrees and leading coefficients give the stated
limits 4 and 6 at both infinities.

The linear certificate is only a necessary finite subsystem of the
all-real allocation conditions: nonnegativity everywhere implies its
two evaluation rows. Its nonnegative weighted sum has zero left side
and negative right side, which proves infeasibility without any
semi-infinite completeness assumption. Removing either pair group
leaves that pair feasible with alpha=beta=1 by the full-domain F_c
proof; hence this contradiction needs joint conservation.
No polynomial symmetry is imposed on allocations. This audits the
standalone example, not an external manuscript or an actual-Xi bridge.

This establishes a relevant finite obstruction beyond the one-pair
deficit in L510, with no claimed progress beyond the sources checked
on RH itself. Actual-Xi geometry, unmatched-pair mass, convergent
assembly and higher-order signs remain unresolved. It does not refute
collective signed positivity or rule out other allocation mechanisms.

## Mathlib

Full matching theorem and supporting-identity coverage are unchecked;
no absence claim is made. The proof uses rational polynomial identities,
the binomial theorem, elementary positivity and a finite linear dual.
