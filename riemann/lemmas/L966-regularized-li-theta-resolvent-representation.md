# Lemma 966: a complete theta representation of the regularized Li form

## Hypotheses

Use the actual Xi function, the positive theta kernel K of L019-L020,
and the paired nodes beta_j=alpha_j^(-2) of L024, with multiplicities.
Thus sum_j |beta_j|<infinity, and L026 gives |beta_j|<1/16 and
Re(beta_j)>0. No RH, simplicity, positive Stieltjes measure or negative
Li coefficient is assumed. Fix an integer n>=1 and set

    p=floor((n-1)/2),  b=1/4,  eta=1/(64*9^n),  h=1/eta,
    v_i=binom(n,2i+1)/4^i                  (0<=i<=p),
    P_n(z)=sum_{i=0}^p (-1)^i v_i z^i,
    a_n(z)=P_n(z)(1+z/4)^(-n/2).

The branch in a_n is exactly L964(5), with value n at zero. Define

    Q_eta(n)=sum_j beta_j^2 a_n(beta_j)^2/(beta_j+eta).       (1)

Squares are algebraic throughout. These are the prescribed eta and
observable of the assessed target; the negative-margin hypothesis and
epsilon-dependent choice of eta in L964 are not assumed here.

## Conclusion

There are the following finite positive rational coefficients. For
0<=s<=2p and 0<=r<=n-1 define

    w_s=sum_{i+j=s, 0<=i,j<=p} v_i v_j,
    D_r=sum_{s=0}^{min(2p,n-1-r)}
            w_s binom(n-1-s,r) b^(n-1-s-r),
    d_k=h sum_{r=0}^{n-k} D_r/(h-b)^(n-k-r+1)   (1<=k<=n). (2)

For real x>=0 put

    H_r(x,u)=sum_{l=r}^infinity
                l!/(l-r)! * x^(l-r) u^(2l)/(2l)!,
    I_r(x)=int_0^infinity K(u) H_r(x,u) du,   F(x)=I_0(x).  (3)

Every I_r is finite and strictly positive. The series includes its
usual continuous value at x=0. In particular H_0(x,u)=cosh(sqrt(x)u),
F(x)=Xi(i sqrt(x)), and I_r=F^(r).

Let M_k be the finite set of tuples m=(m_1,...,m_k) of nonnegative
integers with sum_{r=1}^k r*m_r=k. Write ell=sum_r m_r and define

    T_m(x)=(ell-1)!/(product_r m_r!)
            * product_{r=1}^k (I_r(x)/(r! I_0(x)))^m_r.

Then the exact, absolutely convergent theta representation is

    Q_eta(n)=N_n-R_n,                                      (4)
    N_n=sum_{k=1}^n k*d_k sum_{m in M_k, ell odd} T_m(b),
    R_n=d_1 I_1(h)/I_0(h)
          +sum_{k=1}^n k*d_k sum_{m in M_k, ell even} T_m(b).

Both N_n and R_n are strictly positive, explicitly specified finite
combinations of the actual theta integrals. Every product in (4)
is an absolutely convergent multiple integral. The complete signed
remainder is -R_n; no term or zero tail is omitted.

No inequality R_n<=N_n is proved. This lemma is a representation input,
written in step165 and independently conceptually audited in step166
on 10 November 2026, with its statement and formulas unchanged. It is
not a positivity theorem or an RH candidate.

## Proof

### Rational reduction and all coefficient signs

Set t=1/z. Squaring the prescribed analytic branch gives the ordinary
rational function a_n(z)^2=P_n(z)^2/(1+z/4)^n. At every node none of
these denominators vanishes. Straight substitution gives

    z^2 a_n(z)^2/(z+eta)
      =h B_n(t)/((t+h)(t+b)^n),
    B_n(t)=t^(n-1)P_n(1/t)^2
          =sum_{s=0}^{2p} (-1)^s w_s t^(n-1-s).             (5)

Since 2p<=n-1, B_n is a polynomial of degree n-1, with leading
coefficient w_0=n^2. There is no pole at t=0 hidden in this expression.
The rational function in (5) is O(t^-2) at infinity. Its only possible
poles are -h, simple, and -b, of order at most n; they are distinct
because h=64*9^n>b.

The binomial theorem applied to B_n(-b+y) gives exactly

    B_n(-b+y)=sum_{r=0}^{n-1} (-1)^(n-1-r) D_r y^r.         (6)

Every D_r is positive: all summands in (2) are nonnegative, and its
s=0 term is n^2 binom(n-1,r)b^(n-1-r)>0. Near y=0, expand
(h-b+y)^(-1)=sum_{j>=0}(-1)^j y^j/(h-b)^(j+1), valid for
|y|<h-b. The coefficient of (t+b)^(-k) in the principal part of
(5) is therefore

    h sum_{r+j=n-k} (-1)^(n-1-r+j)D_r/(h-b)^(j+1)
       =(-1)^(k-1)d_k.                                    (7)

This proves the claimed positivity of every d_k and gives a finite
recipe for every pole order, without a symbolic root choice. Let A be
the remaining coefficient of (t+h)^(-1). Partial fractions have no
polynomial part. Comparing coefficients of t^(-1) at infinity in (5)
gives A+d_1=0, since k>=2 terms contribute no such coefficient. Hence
the full rational identity is

    h B_n(t)/((t+h)(t+b)^n)
      =-d_1/(t+h)+sum_{k=1}^n (-1)^(k-1)d_k/(t+b)^k.       (8)

For completeness, the principal parts in (7) together with the true
residue at -h exhaust all poles. Subtracting them leaves a rational
function without poles that vanishes at infinity, hence the zero
polynomial. This proves the partial-fraction assertion used to compare
the t^(-1) coefficients. In particular the leading cancellation in (8)
is exact; the original summand remains O(beta^2) as beta tends to zero.

### Resolvents, local logarithms and complete sums

L024 gives the entire paired product

    F(x)/F(0)=product_j (1+x beta_j).                         (9)

Here F is entire in x by the even entire expansion of Xi (or (3)),
so the notation involving sqrt does not introduce a branch. For x>=0,
|1+x beta_j|>=1. The kth resolvent is thus absolutely summable:

    sum_j |(alpha_j^2+x)^(-k)|
      <=sum_j |beta_j|^k
      <=(1/16)^(k-1) sum_j |beta_j|<infinity.               (10)

These statements do not replace alpha_j by its real part or ordinate.
For complex y with |y-x|<1, the denominator satisfies
|1+y beta_j|>=1-|beta_j|>15/16. Consequently every fixed-order
derivative series is locally uniformly dominated by a constant times
sum_j |beta_j|. The product is locally uniform by L024; F(x)>0 by
the actual theta integral, so a local analytic logarithm exists near
each evaluation point. Product differentiation is therefore licensed
by NIST DLMF 1.10.23-24, version 1.2.8, with all its factors nonzero
on these neighborhoods. Its finite higher derivatives give

    (log F)^(k)(x)
      =(-1)^(k-1)(k-1)! sum_j (alpha_j^2+x)^(-k),           (11)
    Q_eta(n)=sum_{k=1}^n d_k/(k-1)! * (log F)^(k)(b)
               -d_1 F'(h)/F(h).                           (12)

The original sum (1) is also absolute: on |beta|<1/16 the rational
a_n(beta)^2 is uniformly bounded for fixed n, and
|beta+eta|>=eta. Thus its terms are bounded by a fixed multiple of
|beta|^2. Equation (8) may be summed term by term using (10); it never
separates an infinite sum of constants. Multiplicity is preserved
at every step because (9)-(11) use exactly L024's indexed paired
multiset. Conjugation preserves that beta multiset, and the rational
coefficients are real, so the absolute sum is real as well. No
global logarithm through any zero is used.

### Positive theta derivatives and finite chain differentiation

The power series for H_0(z,u) is entire in z and satisfies
|H_0(z,u)|<=exp(sqrt(|z|)u) for u>=0. Cauchy's derivative bound on
unit circles gives, for |z|<=M and each fixed r,

    |partial_z^r H_0(z,u)|<=r! exp(sqrt(M+1)u).             (13)

L019 bounds K by C exp(9u/2-pi exp(2u)), so the right side times K
is integrable for every finite M,r. The analytic integral theorem
and M-test, DLMF 1.10.18-19, therefore justify differentiation under
the actual integral to every fixed order. Differentiating the entire
series gives (3). At x>=0,u>0 all its terms are nonnegative and its
l=r term is positive, hence I_r(x)>0. This proves simultaneously
convergence, positivity and F^(r)=I_r at b and h. Although h grows
rapidly with n, it is finite for every n under consideration; no
uniform-in-n majorant or limiting interchange is asserted.

Apply the finite Faà di Bruno formula, DLMF 1.4.13, to log(F(x))
on its positive real domain and local analytic neighborhood. Its
outer derivatives are (log)^(ell)(F)=(-1)^(ell-1)(ell-1)!/F^ell.
The hypotheses were checked above. Thus

    (log F)^(k)(x)=k! sum_{m in M_k} (-1)^(ell-1) T_m(x).   (14)

Inserting (14) into (12) proves (4), including the coefficient k*d_k.
The terms with odd ell have positive sign, the terms with even ell
have negative sign, and the h-resolvent has its displayed negative
sign. Every T_m(x)>0. The k=1 term of N_n and the h-term of R_n
are strictly positive, so both totals are positive even when n=1.

Explicitly, enumerate ell variables u_{r,j}, 1<=j<=m_r. Then

    product_r I_r(x)^m_r
      =int_{(0,infinity)^ell}
           product_{r,j} K(u_{r,j}) H_r(x,u_{r,j}) du.

Each factor is nonnegative and integrable by (13), and its product
integral is finite, bounded by the product of the corresponding
one-variable integrals. Tonelli followed by finiteness gives absolute
Fubini. The denominators in T_m are strictly positive finite numbers;
all remaining sums are finite. This verifies every multiple integral
in (4), including products with repeated derivative orders.

### The exact unpaid inequality and the n=1 boundary case

The sign question in this representation is the following explicit
inequality in actual theta integrals. Put

    E_{k,m}=k*d_k*(ell-1)!/
                (product_r m_r! * product_r (r!)^m_r),
    J_m=I_0(b)^(n-ell) product_r I_r(b)^m_r.

Since ell<=k<=n, all exponents in J_m are nonnegative integers.
Multiplying (4) by the positive number I_0(b)^n I_0(h) gives

    Q_eta(n) I_0(b)^n I_0(h)
      = I_0(h) sum_{k,m: ell odd} E_{k,m} J_m
        -I_0(h) sum_{k,m: ell even} E_{k,m} J_m
        -d_1 I_1(h) I_0(b)^n.                              (15)

Thus a concrete sufficient and necessary condition for this Q_eta(n)
to be nonnegative is

    I_0(h) sum_{k,m: ell even} E_{k,m} J_m
       +d_1 I_1(h) I_0(b)^n
       <= I_0(h) sum_{k,m: ell odd} E_{k,m} J_m.            (16)

Each side is a finite sum of positive integrals with exactly n+1
variables after expanding the products. Its coefficients are (2),
not unknown zero data or positive/negative parts of Q. This makes
(16) an independently estimable theta-moment comparison, rather than
the tautology Q=max(Q,0)-max(-Q,0). Nevertheless it is an exact
reformulation of this one sign, not an established bound. Positivity
of K signs neither (15) nor (16); the even-block and h terms remain
fully unpaid. L242's signed G' formula is consistent with this issue
and does not provide the missing integrated inequality.

For n=1, p=0, D_0=1 and d_1=h/(h-b). There is only m_1=1, and no
even-block term. Equations (4) and (12) reduce to

    Q_eta(1)=h/(h-b) * (I_1(b)/I_0(b)-I_1(h)/I_0(h)).       (17)

No monotonicity of F'/F was assumed to obtain this case. It verifies
that the distant-point term cannot be dropped even at the first index.

### Verification, comparison and scope

The standard inputs are the product/integral differentiation theorems
at [DLMF 1.10.18-24](https://dlmf.nist.gov/1.10) and the finite chain
formula [DLMF 1.4.13](https://dlmf.nist.gov/1.4.E13), version 1.2.8,
as inspected in the prior assessment. They are imported, not reproved.
The specialization needed here is (5)-(8), its explicit positive
coefficients, the actual-node convergence checks, and the complete
partition (4). The bounded prior search found no inspected theorem
giving this exact Q_eta formula; it does not establish originality.
L242 is a lower-derivative comparison, not a positivity input.

Run `python3 scripts/li-theta/regularized-resolvent-check-165.py` for
exact rational, denominator-cleared checks of (8) for n=1,...,12.
The full certificate is `scripts/li-theta/regularized-resolvent-check-165.json`.
All polynomial residuals are zero and all d_k are strictly positive.
These finite algebra checks are supplementary diagnostics; the
all-n argument and integral convergence are the proof above. No
theta truncation or numerical sign calculation is used.

This does not establish actual mixed positivity, a negative Li margin,
an off-line zero or RH. It also does not assert that signs at only
the prescribed eta(n) imply all Li or mixed signs: L964's conditional
margin transfer chooses eta using that supplied margin. Broader
parameter coverage and the unpaid inequality are separate questions.
The local progress is a convergent representation and a specified
remainder, not a sign advance beyond the sources checked.

### Independent conceptual audit, step166

The audit accepts (1)-(17) under exactly the stated hypotheses. It
reuses the pre-existing source assessment and checks the complete
proof against L019-L020, L024, L026 and the exact definition in L964.
No mathematical correction or new external input was needed.

The main algebraic checks were as follows. Substitution in (1) gives
the factor h and exponent n-1 in (5), including when n is even and
B_n has a zero at t=0. The inequality 2p<=n-1 excludes a negative
exponent in B_n for either parity. In (7), substituting j=n-k-r
gives exponent 2n-1-k-2r, congruent to k-1 modulo 2. This checks
all principal-part signs, not just the highest and lowest orders.
The coefficient of 1/t is zero in (5), so the residue -d_1 at -h
is essential. In the beta variable the resulting cancellation leaves
order beta^2, while each separated resolvent is itself summable by
L024. The n=1 formula (17) retains that same subtraction.

For the analytic checks, write alpha=a+ic. L026 gives a^2>16 and
c^2<1/4, hence |beta|<1/16 and
Re(beta)=(a^2-c^2)/(a^2+c^2)^2>0. At each real x>=0, the disk
|y-x|<1 satisfies |1+y beta|>15/16. The absolute kth logarithmic
derivative sum on this disk is bounded by

    (k-1)! (16/15)^k (1/16)^(k-1) sum_j |beta_j|.

The product M-test and these derivative bounds justify the local
logarithmic identities with every multiplicity and with no global
zero-free assumption. Conjugate nodes and the absolute sum justify
reality; no ordinate replacement or modulus square occurs.

For (13), the unit-circle Cauchy bound is valid for the entire power
series H_0, including at x=0. For each finite M, its product with K
is bounded by a constant times

    exp((9/2+sqrt(M+1))*u-pi*exp(2u)),

which is integrable at infinity and bounded near zero. This licenses
each fixed derivative and each finite product at b and h. The argument
does not require a majorant uniform in n. The positive l=r term of
H_r and positivity of K give strict I_r>0; in particular no denominator
in (4), (14) or (15) can vanish.

The finite chain-rule normalization was checked separately: T_m uses
I_r/(r! I_0), the derivative in (14) contributes k!, and division by
(k-1)! in (12) leaves k*d_k. All signs are exhausted by ell parity
and the negative h term. The k=1 term makes N_n>0, and the h term
makes R_n>0 even at n=1. Since ell<=k<=n, clearing denominators
in (15) really gives n+1 integrable factors in every term; it does
not introduce a negative power of I_0 into a purported product
integral. Absolute Fubini follows from the finite one-variable bounds.

Run `python3 scripts/li-theta/regularized-representation-audit-166.py`.
It reproduces all full step165 cases without rewriting that evidence,
and checks the Bell coefficients independently via the formal identity
f*(log f)'=f' for f=1+sum_r a_r z^r with independent indeterminates a_r.
Rational polynomial and residue residuals are exactly zero for n=1,...,12;
all D_r,d_k are positive. Formal-log polynomial residuals are exactly
zero through order eight. Full coefficients and residuals are saved in
`scripts/li-theta/regularized-representation-audit-166.json`.
These finite checks supplement the general arguments above; they prove
neither the all-n analytic statement by themselves nor any theta sign.

This audit establishes reliability of the local representation only.
Equation (16) remains the unpaid comparison; L242's both-sign kernel
and L044/L046's generic logarithm/variance obstructions remain in force.
No actual negative Li coefficient is supplied. In particular L964's
margin-dependent regularization is not replaced by the prescribed eta
here, and an implication from just these Q_eta(n) signs to all mixed
signs remains unproved. The DAG's direct inputs remain unchanged.

## Mathlib

Full matching coverage has not been checked and is unknown. No Mathlib
theorem is imported. General product, analytic-integral or chain-rule
support alone would not certify this rational specialization, the
paired-zero normalization or the unpaid inequality. Reference portal:
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).

