# Lemma 972: uniform loss for moving eta at fixed Li index

## Hypotheses

Use the actual Xi paired nodes beta_j=alpha_j^(-2) of L024, with
all multiplicities, and the zero geometry of L026. Fix a finite real
A>0 with sum_j |beta_j|<=A, independent of the index below. For each
integer n>=1 use L964(5)'s function

    P_n(z)=sum_{k=0}^{floor((n-1)/2)}
               (-1)^k binom(n,2k+1)(z/4)^k,
    a_n(z)=P_n(z)(1+z/4)^(-n/2),                 |z|<4,

with the analytic branch equal to 1 at zero in the power factor.
Thus a_n(0)=n. Set eta_j=1/(64*9^j). For a real u>0 define

    Q_u(n)=sum_j beta_j^2 a_n(beta_j)^2/(beta_j+u).        (1)

This extends L966's defining zero sum to arbitrary positive u;
no extension of its theta partial-fraction formula is assumed.
All squares are algebraic. No negative Li coefficient, RH, positive
Stieltjes law, simplicity, zero data or finite-head assumption is used.

## Conclusion

The sums in (1) are absolute and real. For every integer n>=1,

    Q_{eta_(n+1)}(n)-Q_{eta_n}(n) >= -A/9 > -A/8.        (2)

The index inside a_n is n in both terms. The same A works for all n.
This pays only the fixed-index parameter movement. It proves no
index recurrence, sign propagation, all-n Q positivity or RH.
The local specialization was written in step194 and passed the
independent proof audit in step196 on 10 November 2026. The statement,
constants and original derivation were unchanged by that audit.

## Proof

### Node sector and the analytic remainder

Write alpha=x+i y. L026 gives |x|>4 and |y|<1/2. For z=alpha^(-2),

    |z|=1/(x^2+y^2)<c:=1/16,
    Re z=(x^2-y^2)/(x^2+y^2)^2>0,
    |Im z|/(Re z)=2|xy|/(x^2-y^2).

Putting r=|y|/|x|<1/8 bounds the last ratio by
2r/(1-r^2)<16/63<1. In particular

    Re(z^2)=(Re z)^2-(Im z)^2>0.                         (3)

The strict bound follows because 2r/(1-r^2) is increasing on [0,1),
as its derivative is 2(1+r^2)/(1-r^2)^2>0. This uses the actual complex
nodes; they have not been replaced by real ordinates.

Put H_n(z)=a_n(z)^2. Reuse L964(9)-(10), whose analytic estimates
use only n and the indicated disks, independently of that lemma's
supplied negative-margin hypothesis. Explicitly a_n is analytic on
|z|<4, and on |z|<=1/4 its bound is |a_n(z)|<=3^n. Since H_n(0)=n^2,
the Cauchy coefficient estimate and Taylor expansion yield

    |H_n(z)-n^2|<=C_n |z|,      C_n=8*9^n,   |z|<=1/8. (4)

The standard inputs are the Cauchy formulas
[DLMF 1.9.30](https://dlmf.nist.gov/1.9.E30) and
[1.9.31](https://dlmf.nist.gov/1.9.E31), and the analytic Taylor theorem
[DLMF 1.10.1](https://dlmf.nist.gov/1.10.E1), version 1.2.8, as checked
in the prior assessment. L964 already specializes them: the circle
|z|=1/4 lies strictly inside the analytic domain, its H_n supremum is
at most 9^n, and the geometric remainder is bounded by
9^n*4|z|/(1-4|z|)<=8*9^n |z| for |z|<=1/8. No new analytic theorem
or negative-margin conclusion is being imported.

### Off-diagonal definition, convergence and realness

For every node and every u>0, Re z>0 gives |z+u|>=u and |z+u|>=|z|.
Thus denominators are nonzero. Using |H_n(z)|<=9^n at the nodes,

    sum_j |beta_j^2 H_n(beta_j)/(beta_j+u)|
       <=(9^n/u) sum_j |beta_j|^2
       <=(9^n c/u) A < infinity.                         (5)

This proves (1) at both positive parameter values in (2), including
the off-diagonal one. Conjugation preserves L024's beta multiset with
multiplicity, as verified in L964's paired identity. H_n has real Taylor
coefficients (its branch respects conjugation) and u is real, so
conjugation preserves each absolutely summed multiset of terms. Hence
Q_u(n) is real. No theta identity at an off-diagonal parameter or
limiting interchange in n is needed.

### The signed rational comparison

Fix n arbitrarily. Set s=eta_n, t=eta_(n+1)=s/9, delta=s-t>0 and

    W(z)=z^2/((z+s)(z+t)).

Elementary subtraction in the absolute sums (5) gives

    Q_t(n)-Q_s(n)=delta sum_j W(beta_j) H_n(beta_j).      (6)

The constant part of H_n is favorable. Indeed, multiplication by
the conjugate denominator shows

    Re W(z)=
      (|z|^4+(s+t)|z|^2 Re z+st Re(z^2))
         / |(z+s)(z+t)|^2 > 0                            (7)

at each node, by (3). The s,t product and both denominators are
retained in this identity. Also

    |W(z)|<=1,             |W(z)|<=|z|/s.                (8)

For the second inequality use |z+s|>=s and |z+t|>=|z|;
the first uses |z+s|,|z+t|>=|z|. Therefore the constant-part series
is absolute, since sum_j |W(beta_j)|<=A/s, and by (4) so is the
remaining series, with

    sum_j |W(beta_j)(H_n(beta_j)-n^2)| <= C_n A.          (9)

These bounds justify splitting (6) into its n^2 and remainder terms
and taking real parts. Using realness, (7) and (9),

    Q_t(n)-Q_s(n)
      =delta n^2 sum_j Re W(beta_j)
        +delta Re sum_j W(beta_j)(H_n(beta_j)-n^2)
      >= -delta C_n A.                                  (10)

Finally the exact constants cancel the index growth:

    delta C_n=(8/9)*(1/(64*9^n))*(8*9^n)=1/9.

This proves (2) for each arbitrary n, with the fixed A from the
hypotheses. There is no exchange of an n-limit and a node sum.

### Scope and remaining gap

The prior SPECIALIZE assessment covers this exact parameter-loss
test. Standard Cauchy/Taylor results and L964's bounds are reused;
the local addition is the signed two-denominator comparison (7)-(10).
This is recorded as a reproduction/specialization, with no certified
originality claim. The bounded literature search did not supply the
two-eta bound; failure to find it establishes no novelty.

The proof uses the original complete zero sum, retaining every node
and multiplicity. It does not drop either distant-h term from a
theta resolvent representation: no partial-fraction splitting at b
or at either h was used. It does not replace algebraic squares by
modulus squares, subtract two one-sided bounds, or assume a sign
for H_n(beta). Only its constant n^2 contribution has been signed.

This estimate leaves fixed-eta signed index forcing, recurrence
closure, initialization and margins paying accumulated losses open.
In particular a loss bounded by A/9 at each step need not have a
bounded cumulative sum. L966's R_n<=N_n is still unproved, and L968's
downstream implication still requires its unproved all-n sign premise.
No complete candidate argument for RH is asserted.

### Independent proof audit, step196

The audit replayed the complete argument under the separately approved
SPECIALIZE scope. No defect or mathematical correction was found.
The following checks explain why its conclusion is valid without the
negative-margin premise in L964.

First, for r=|Im alpha|/|Re alpha|<1/8, the ratio controlling the
node sector is 2r/(1-r^2)<16/63<1. Thus both Re beta>0 and
Re(beta^2)>0 hold even at nonreal nodes. Choosing either member of
an alpha sign pair gives the same beta. Conjugating sign pairs
permutes them with equal multiplicities, as in L964's unconditional
paired construction; there is no extra factor two in (1) or (6).

Second, the analytic branch is exp(-(n/2) Log(1+z/4)), with Log
normalized to zero at z=0. It exists on |z|<4, respects conjugation,
and has modulus |1+z/4|^(-n/2). On |z|<=1/4, the sum of the odd
binomial coefficients is 2^(n-1) for every n>=1, including n=1.
Consequently

    |a_n(z)|<=2^(n-1)*(16/15)^(n/2)<=3^n.

The cited Cauchy/Taylor theorems apply to H_n on the entire closed
radius-1/4 circle inside that domain. Every coefficient of positive
degree k is at most 9^n*4^k in modulus, so the complete remainder
is bounded by 9^n*4|z|/(1-4|z|)<=8*9^n|z| on |z|<=1/8.
This verifies precisely the use of L964(9)-(10): these estimates
involve neither lambda_n, epsilon, nor L964's margin-dependent eta.
Zeros of P_n do not require choosing a square root of H_n.

Third, the denominator inequalities follow directly from
|z+u|^2=|z|^2+2u Re z+u^2 for u>0. They prove (5) for every
positive u, so the off-diagonal Q_t(n) is defined by its full node
sum. Its n is unchanged, its numerator has no u dependence, and
subtraction therefore has sign +(s-t) and exactly W as in (6).
No off-diagonal theta identity is imported. All coefficients and
the branch respect conjugation; absolute convergence then proves
realness, retaining every multiplicity and every algebraic square.

Fourth, expanding z^2*conjugate((z+s)(z+t)) gives respectively
|z|^4, (s+t)|z|^2*z and st*z^2. Taking real parts gives exactly
(7). Each term in its numerator is positive at a node. Crucially,
the favorable constant term is not separated as n^2*sum_j 1:
its series is n^2*sum_j W(beta_j), with absolute sum at most
n^2*A/s. The remainder has absolute sum at most C_n*A by (4)
and |W|<=1. Both are finite for each fixed n. Thus every split
and real-part summation in (10) is justified independently of a
uniform-in-n dominating sequence.

Finally, s-t=8/(64*9^(n+1)) and C_n=8*9^n, so their product is
64/(64*9)=1/9. One fixed A bounds the node mass at every n,
giving the stated all-n lower bound and, since A>0, its strict
comparison with -A/8. Neither an n-limit nor a deleted resolvent
charge is used. The direct mathematical inputs remain L024, L026
and the unconditional analytic/symmetry passages of L964; L966
only supplies comparison of conventions, and L968 is downstream.

This establishes an audited local input, classified REPRODUCTION;
it establishes no originality beyond the sources checked. It does
not sign a change of polynomial index. In particular, this audit
does not supply initialization, a signed forcing bound, recurrence
closure or a summable loss budget. The proof of actual all-degree
positivity remains open.

## Mathlib

Full matching coverage has not been checked and remains unknown.
No Mathlib theorem is imported. Supporting analytic or complex-field
results alone would not certify the fixed-index normalization, sector
sign and uniform constant proved here. Reference portal:
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
