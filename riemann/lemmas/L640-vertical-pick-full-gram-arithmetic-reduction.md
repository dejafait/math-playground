# Lemma 640: vertical Pick full-Gram arithmetic reduction

## Hypotheses

Use the completed xi function of L018 and its s-logarithmic derivative
F(s)=xi'(s)/xi(s). All logarithms of positive numbers are natural.
Let T>=e^5, N=floor(log T), T<=X<=2T, and 0<=j,k<N. Put

    t_j=j/N,  s_j=2+i(X+t_j),  ell_X=log(X/(2*pi)),
    C_jk=1/(3+i(t_j-t_k)),
    K_jk=(F(s_j)+conjugate(F(s_k))) C_jk,
    D=diag(t_0,...,t_(N-1)).

All vector spaces are complex. Norms without a subscript are Euclidean
spectral operator norms; the Frobenius norm is denoted by ||.||_F.
After the strict definiteness of C is established below, define

    A=C^(-1/2) D C^(1/2),
    E_N(v)=exp(-iv A),
    Q_(N,X)=sum_(n>=2) Lambda(n) n^(-2-iX) E_N(log n),
    W_(T,X)=(Q_(N,X)+Q_(N,X)^*)/ell_X,
    R_(T,X)=C^(-1/2) K C^(-1/2)/ell_X-I.

Lambda is the von Mangoldt function. The star denotes conjugate
transpose. This is the full C of the approved vertical-block diagnostic.

## Conclusion

C is strictly positive definite, all quotients and series above exist,
and the following statements hold.

1. The displacement identity gives the exact finite-dimensional bound

       ||A||_F^2 = sum_(j=0)^(N-1) (j/N)^2 + (9/2)N(N-1),
       ||A|| <= 3N.                                             (1)

2. For every v>=0,

       ||E_N(v)|| <= min(exp(3v/2), exp(3*pi*N)).                  (2)

   For every integer Y>=2 the full arithmetic tail satisfies

       ||Q_(N,X)-sum_(2<=n<=Y) Lambda(n)n^(-2-iX)E_N(log n)||
           <= exp(3*pi*N)(log Y+1)/Y.                            (3)

3. Gamma and both rational completion terms obey the coefficient-uniform
   estimate in the full Gram norm

       ||R_(T,X)+W_(T,X)||
           <= 18N/(X ell_X) <= 36/T.                            (4)

4. There is a unitary U, depending only on N, such that

       U^*[(2+iX)I+iA]U = H_(N,X),
       H_jj=2+i(X+j/N),  H_jk=3 (j<k),  H_jk=0 (j>k).

   Thus, for q(s)=-zeta'(s)/zeta(s),

       U^*Q_(N,X)U=q(H_(N,X)),
       (H_(N,X)+H_(N,X)^*)/2=(1/2)I+(3/2)1 1^*.               (17)

   The analytic matrix function q(H) is defined on neighborhoods of
   its eigenvalues, all of real part 2. It does not assert that q is
   holomorphic throughout the numerical range of H.

5. Set Y=ceil(T^12) and define the exact, finite matrix sum

       P_(T,X)=sum_(2<=n<=Y) Lambda(n)n^(-H_(N,X)),
       V_(T,X)=(P_(T,X)+P_(T,X)^*)/ell_X,
       n^(-H)=exp(-(log n)H).

   Then the complete omitted arithmetic tail satisfies

       ||U^*W_(T,X)U-V_(T,X)||
          <=50 T^(-(12-3*pi)) <=50 T^(-5/2),
       ||U^*R_(T,X)U+V_(T,X)||<=37/T.                          (18)

6. Let S be the upper shift, S_(j,j+1)=1, and put D=diag(j/N).
   Define g_d(v), for 0<=d<N and v>=0, by the power series at z=0

       G_v(z)=exp(3iN[log(1-exp(-iv/N)z)-log(1-z)])
             =sum_(d>=0) g_d(v)z^d.                            (19)

   Both logarithms are the analytic branches with value zero at z=0.
   Evaluation at S uses only the first N coefficients. Then

       exp(-vH)=exp(-(2+iX)v) exp(-ivD) G_v(S),
       g_0(v)=1,
       d g_d(v)=3iN sum_(m=1)^d (1-exp(-imv/N))g_(d-m)(v).      (20)

   In these unitary triangular coordinates, for a unit vector x define

       p_x(v)=sum_(d=0)^(N-1) g_d(v)
                    sum_(j=0)^(N-1-d) conjugate(x_j)x_(j+d)
                                           exp(-ijv/N).

   The exact signed norm test is

       ||W_(T,X)||=(2/ell_X) sup_(||x||=1)
          |Re sum_(n>=2) Lambda(n)n^(-2-iX)p_x(log n)|.          (21)

   The series converges absolutely for fixed N, uniformly in X and
   unit x. Truncation at any integer Y>=2 changes the scalar sum
   inside Re by at most exp(3*pi*N)(log Y+1)/Y. Its infinite tail
   and the completion error are therefore still charged by (18)
   when Y=ceil(T^12). Formula (21) is a reduction, not a bound on
   the supremum.

7. Let I be any consecutive block of m Schur coordinates, 1<=m<=N,
   and let Pi_I be its orthogonal coordinate projection. Then

       ||Pi_I U^*R_(T,X)U Pi_I||
          <= 9(3m+1)4^m/(32 ell_X)+36/T.                       (22)

   In particular, if m=m(T) satisfies m4^m=o(log T), these compressed
   norms tend uniformly to zero for every allowed X and block I.
   Hence a unit vector supported on such a block cannot be an
   asymptotic obstruction witness: its normalized K-Rayleigh quotient
   tends to one, rather than zero. This includes every fixed block size.
   Arbitrary sparse supports with large gaps are not covered. For
   m=N the bound is inconclusive and proves no full norm margin.

Consequently the existence of an eventual fixed margin below one for
||R_(T,X)||, uniformly in T<=X<=2T, is equivalent to the existence of
such a margin for ||W_(T,X)|| (the margin and onset may change).
Likewise their norms differ by at most 36/T. The same fixed-margin
equivalence holds for V, by (18). No bound below one or asymptotic lower
witness for any of these norms is proved here.

This is an unaudited local reduction of the approved diagnostic. It
removes Gram invertibility and archimedean normalization as unresolved
inputs and controls the entire arithmetic tail for any stated cutoff.
The signed arithmetic norm, positive interpolation conclusion, arbitrary
configurations, critical-boundary transfer and initial signs remain open.
There is no RH candidate. No originality is inferred from the source search.
The original reduction (1)--(4) was inherited as unfinished work;
this completed attempt checks that proof and adds (17)--(18). These are
local finite-dimensional reductions, not a new positivity theorem or
a resolution of the signed norm test. A second bounded attempt adds
(19)--(22), retaining every arithmetic phase in scalar generating
coordinates and excluding short consecutive-coordinate witnesses,
but still obtains neither a fixed full norm margin nor an asymptotic
obstruction. A separate critical audit remains outstanding.

## Proof

### Full Gram and the displacement calculation

For a in C^N set p_a(u)=sum_j a_j exp(i t_j u). Direct integration gives

    a^* C a = integral_0^infinity exp(-3u)|p_a(u)|^2 du.          (5)

Thus C is Hermitian and nonnegative. If (5) is zero, continuity implies
p_a(u)=0 for u>=0. Its first N derivatives at zero vanish. The resulting
Vandermonde system at the distinct numbers i t_j forces every a_j=0.
This proves strict definiteness, including existence of the positive
Hermitian square roots used above.

Let 1 denote the all-ones column and b=C^(-1/2)1. The entrywise identity
(3+i(t_j-t_k))C_jk=1 implies

    3C+i(DC-CD)=1 1^*,
    i(A-A^*)=b b^*-3I.                                         (6)

Similarity to D gives tr(A-A^*)=0, so ||b||^2=3N. Hence

    ||A-A^*||_F^2
       =tr((b b^*-3I)^2)=9N(N-1).                              (7)

Expanding the left side also gives

    ||A-A^*||_F^2
       =2 tr(A^*A)-2 Re tr(A^2).

Since tr(A^2)=sum_j t_j^2 is real, (7) proves the exact expression
in (1). The inequalities sum_j t_j^2<=N and
N+(9/2)N(N-1)<=9N^2 for N>=1 prove its stated norm bound.
No smallest-eigenvalue estimate or diagonal surrogate for C is used.

### Exact translations and the full arithmetic series

The adjoint of E_N(v) is

    E_N(v)^*=C^(1/2) diag(exp(i v t_j)) C^(-1/2).

Use x=C^(1/2)a in its norm ratio. Multiplying a_j by exp(i v t_j)
replaces p_a(u) by p_a(u+v), and (5) therefore gives

    ||E_N(v)||^2
      =sup_(a!=0) integral_0^infinity exp(-3u)|p_a(u+v)|^2 du
                    / integral_0^infinity exp(-3u)|p_a(u)|^2 du
      <= exp(3v),                                               (8)

because the numerator is exp(3v) times the denominator's integral
restricted to u>=v. Each frequency j/N has period 2*pi*N.
For r=v modulo 2*pi*N in [0,2*pi*N), E_N(v)=E_N(r).
Applying (8) at r proves the second bound in (2).

For fixed N, (2), Lambda(n)<=log n, and sum_(n>=2)log n/n^2<infinity
prove absolute convergence in matrix norm, uniformly in the real phase X.
For integer Y>=2, log u/u^2 is decreasing on [Y,infinity), so

    sum_(n>Y) Lambda(n)/n^2
       <= integral_Y^infinity log u/u^2 du=(log Y+1)/Y.

This proves (3), with every omitted prime power charged. These estimates
are convergence/tail estimates, not a bound of the required size on Q.

### Completion and a uniform analytic matrix estimate

L018 gives the completion and nonvanishing at every s_j. Logarithmic
differentiation there yields

    F(s)=a(s)+zeta'(s)/zeta(s),
    a(s)=1/s+1/(s-1)-(1/2)log pi+(1/2)psi(s/2).                 (9)

In particular the pole-factor contribution is +1/(s-1), and the
digamma chain factor is 1/2. The standard absolutely convergent identity

    -zeta'(s)/zeta(s)=sum_(n>=2) Lambda(n)n^(-s),  Re(s)>1,

is imported from NIST DLMF, equation
[27.4.12](https://dlmf.nist.gov/27.4.E12). Applying it to the N samples,
and using the matrix-norm convergence just proved, gives

    C^(-1/2) diag(F(s_j)) C^(1/2)=a(B)-Q_(N,X),
    B=(2+iX)I+iA,                                               (10)

where a(B) is the analytic matrix function, equivalently the similarity
of diag(a(s_j)). No continuation of the arithmetic series outside its
absolute-convergence half-plane is used.

For clarity prove the archimedean bound for any integer N>=1 and
X>=12(N+1). The closed disk |s-(2+iX)|<=X/2 lies in Im(s)>0,
satisfies |s|>=X/2 and |arg s|<=2*pi/3. To see the last claim, the disk
center has argument at most pi/2 and the angle subtended by its radius
is at most arcsin(1/2)=pi/6. There are no rational or digamma poles
on this disk, and the principal logarithm is analytic there.

DLMF [5.11.2](https://dlmf.nist.gov/5.11.E2) and the complex remainder
statement in [5.11(ii)](https://dlmf.nist.gov/5.11#ii), terminated before
the B_2 term, give

    psi(z)=log z-1/(2z)+r(z),
    |r(z)| <= sec^3(arg(z)/2)/(12|z|^2).

At z=s/2 on the disk, |z|>=X/4 and sec(arg(z)/2)<=2. Thus (9) becomes

    a(s)=(1/2)log(s/(2*pi))+1/(2s)+1/(s-1)+h(s),
    |h(s)| <= 16/(3X^2).                                       (11)

This uses a fixed sector and one fixed truncation order; no differentiated
asymptotic remainder is assumed. Both DLMF statements are the inputs
covered in the prior assessment; their formulas and sector remainder
were rechecked for this applicability calculation on 1 November 2026.

Set H_X=(1/2)ell_X+i*pi/4 and q=(2+3N)/X<=1/2.
Since ||A||<=3N, the matrix logarithm power series about iX yields

    ||(1/2)log(B/(2*pi))-H_X I||
      <= (1/2)sum_(m>=1) q^m/m <= q.                            (12)

The branch is correct because the disk |s-iX|<X lies in the upper
half-plane and log(s/(2*pi))=log(iX/(2*pi))+log(s/(iX)) there.
The inverse Neumann series similarly give

    ||(1/2)B^(-1)||<=1/X,
    ||(B-I)^(-1)||<=2/X.                                       (13)

Apply the scalar Cauchy coefficient estimate to the analytic h at
s_0=2+iX with radius X/2. Substitution of iA into its convergent Taylor
series, using 2||A||/X<=1/2, gives

    ||h(B)|| <= (16/(3X^2))/(1-2||A||/X)
               <=32/(3X^2).                                   (14)

This also justifies the analytic functional calculus in these estimates:
each power series converges in operator norm and agrees with the scalar
values after similarity to the diagonal sample matrix. It does not
assert that the values of h alone control a nonnormal matrix function.

Equations (11)--(14) imply, since X>=12(N+1)>=24,

    ||a(B)-H_X I||
      <= (3N+5)/X+32/(3X^2)
      <= (3N+6)/X <=9N/X.                                      (15)

### Assembly and exact limitation

Writing M=C^(-1/2)diag(F(s_j))C^(1/2), the definition of K gives

    C^(-1/2) K C^(-1/2)=M+M^*.

Therefore (10), H_X+conjugate(H_X)=ell_X, and (15) give

    R_(T,X)=-W_(T,X)+Z_(T,X),
    ||Z_(T,X)||<=18N/(X ell_X).                                (16)

For T>=e^5, T>=12(log T+1)>=12(N+1): this holds at e^5 and
T/(log T+1) is increasing for T>1. Also log(2*pi)<5/2, so

    ell_X>=log T-log(2*pi)> (1/2)log T,
    N/ell_X<=2.

Together with X>=T this proves (4). The reverse triangle inequality
implies | ||R_(T,X)||-||W_(T,X)|| |<=36/T. Taking suprema over the
unchanged interval proves the fixed-margin equivalence: any margin eta
for one norm becomes at least eta/2 for the other once 36/T<=eta/2.

The first bound in (2) would replace the arithmetic absolute sum by
sum Lambda(n)n^(-1/2); it supplies no summable majorant. The periodic
bound gives a finite but exponentially growing upper bound in N. Neither
is a lower bound on the actual signed norm. Thus this attempt proves
neither the required margin nor its asymptotic obstruction. No positivity
criterion is assumed, and there are no numerical or independent-phase
inputs. The elementary Gram, displacement and analytic estimates were
proved to track the dimension and adjoints in this exact full norm;
they are not a reproof of the Nevanlinna--Pick theorem.

### Exact orthonormal triangular coordinates

Apply the standard complex Schur triangularization theorem to A, ordering
its distinct eigenvalues as t_0,...,t_(N-1). This is possible by choosing
an eigenvector for the first desired eigenvalue and inducting on the
remaining compression. Let S=U_0^* A U_0 be the resulting upper triangular
matrix and c=U_0^*b. Equation (6) becomes

    i(S-S^*)=cc^*-3I.

Its diagonal, since S_jj=t_j is real, gives |c_j|^2=3 for every j.
Conjugate S further by the diagonal unitary with entries c_j/sqrt(3).
The new vector c has every entry sqrt(3), and the diagonal t_j is
unchanged. For j<k the lower entry S_kj is zero, so the (j,k) entry of
the identity gives i S_jk=3, or S_jk=-3i. Combining the two unitaries
gives a single U depending only on A, hence only on N. Multiplying S
by i and adding (2+iX)I gives exactly H in (17).

The equality U^*Q U=q(H) follows either by similarity of scalar values
at the distinct s_j, or directly by the absolutely norm-convergent
series already proved. Indeed

    n^(-H)=n^(-2-iX) U^*E_N(log n)U.

The diagonal of the Hermitian part of H is 2, and each off-diagonal
entry is 3/2. This proves the last identity in (17). For N>=2 its least
eigenvalue is exactly 1/2, attained on the orthogonal complement of 1.
Consequently scalar information only on Re(s)=2 cannot be transferred
by an assertion that the numerical range of H stays in Re(s)>1.
Nothing here supplies a bound for q on Re(s)=1/2 or assumes its
nonvanishing denominator there.

### Complete finite tail and the inconclusive signed test

By (3), unitary invariance, and the triangle inequality for the Hermitian
part, the error replacing U^*W U by V is at most

    2 exp(3*pi*N)(log Y+1)/(Y ell_X).

Here exp(3*pi*N)<=T^(3*pi), Y>=T^12, and
log Y<=12 log T+log 2, since ceil(T^12)<=2T^12. Using
ell_X>(1/2)log T and log T>=5 bounds the displayed error by

    [48+4(log 2+1)/log T] T^(-(12-3*pi))
       <=50 T^(-(12-3*pi)) <=50 T^(-5/2).

The coefficient bound follows already from log 2<1, and the exponent
bound follows from pi<22/7, which gives 12-3*pi>18/7>5/2.
Combining this with (4) proves the second inequality of (18): for
T>=e^5, 50 T^(-3/2)<1, so 36/T+50 T^(-5/2)<=37/T.
Every prime power beyond Y is included in this estimate. No phase
cancellation, numerical spectrum or truncation-as-identity is used.

This new coordinate test reaches an exact finite signed operator with
an error tending uniformly to zero. It does not control that operator:
the sufficient inequality would be ||V_(T,X)||<=1-delta uniformly for
all sufficiently large T and T<=X<=2T, with fixed delta>0. An asymptotic
countersequence with limsup norm at least one would instead obstruct
every such margin. Neither is obtained. The shift upper bounds in (2),
even though the full tail can now be charged explicitly, do not decide
the signed interaction among the retained summands. The fact that the
numerical range touches the critical line is a precise limitation of a
safe-half-plane multiplier estimate, not an obstruction to the target
norm and not a negative eigenvalue of K.

### Signed scalar generating coordinates: second bounded attempt

Write J=S+S^2+...+S^(N-1)=S(I-S)^(-1), so that
H=(2+iX)I+iD+3J. The nilpotence S^N=0 makes every power series
substitution below a finite polynomial. In particular, the branch
convention in (19) introduces no ambiguity at the matrix argument S.
The entrywise diagonal conjugation gives

    exp(ivD) S exp(-ivD)=exp(-iv/N)S.

Set r=exp(-iv/N). Differentiating (19) with respect to v, first for
|z|<1 and then substituting the nilpotent S, gives

    dG_v(S)/dv=-3 rS(I-rS)^(-1)G_v(S),  G_0(S)=I.

All these polynomials in S commute. Thus

    Y(v)=exp(-ivD)G_v(S)

satisfies Y(0)=I and Y'(v)=-(iD+3J)Y(v). For example, the second
term in its derivative is -3JY because
exp(-ivD)rS(I-rS)^(-1)=J exp(-ivD). Multiplying by
exp(-(2+iX)v) proves the exponential identity in (20): alternatively,
differentiate exp(vH)exp(-(2+iX)v)Y(v) to see it is the constant I.
No approximate confluent replacement of the distinct nodes is made.

Expanding the logarithms in (19) at zero gives

    log G_v(z)=3iN sum_(m>=1)(1-r^m)z^m/m.

Taking its z derivative and comparing the coefficient of z^(d-1)
in G_v'(z)=G_v(z)(log G_v)'(z) proves the recurrence in (20).
It includes g_0=1 and g_1=3iN(1-exp(-iv/N)); the derivative
of g_1 at v=0 is -3, agreeing with the strict first upper entry
of -H. At v=2*pi*N all g_d for d>=1 vanish and exp(-ivD)=I,
also agreeing with the exact period in (2).

The (j,j+d) entry of exp(-ivD)G_v(S) is
exp(-ijv/N)g_d(v). Therefore

    x^*q(H)x=sum_(n>=2) Lambda(n)n^(-2-iX)p_x(log n).

This equality and the interchange of finite coordinate sums with the
arithmetic series follow from the norm convergence already established
in (2)--(3). More explicitly,

    |p_x(v)| <= ||exp(-ivD)G_v(S)||
              =||E_N(v)|| <=min(exp(3v/2),exp(3*pi*N))

for every unit x. This proves the stated scalar tail bound uniformly
over all such x and over X. Taking the real part and using the
Rayleigh characterization of the norm of a Hermitian matrix proves
(21), with the factor 2 and the absolute value both required.

This test has preserved the complete signed arithmetic but has not
bounded it. A fixed margin would require a single delta>0 with the
absolute real scalar sum in (21) at most (1-delta)ell_X/2 for
every unit x and every X in the allowed intervals, beyond one onset.
An obstruction would require a sequence of unit vectors and allowed
T,X for which twice that absolute real sum divided by ell_X has
limsup at least one. Neither has been obtained. Inserting the displayed
absolute bound for p_x simply returns the earlier inconclusive
majorant. Replacing g_d by its fixed-d, large-N approximation would
not control the required indices d<N and is not performed.

### A bounded witness test: short consecutive coordinate blocks fail

There is a coefficient-sensitive bound stronger than (2) when only a
short consecutive block of coordinates is tested. For v>=0 let P_0(v)=1
and, for d>=1, set

    P_d(v)=sum_(k=1)^d binom(d-1,k-1)(3v)^k/k!.

These are the nonnegative coefficients of exp(3vz/(1-z)). Differentiating
this generating function with respect to z gives

    d P_d(v)=3v sum_(r=1)^d r P_(d-r)(v).

Since |1-exp(-irv/N)|<=rv/N, recurrence (20) and induction on d
give |g_d(v)|<=P_d(v). This estimate is exact for all v>=0 and
d<N, not an interchange of fixed-d and growing-d limits.

For every integer k>=0, monotonicity of log x and x<=n+1 on
[n,n+1], n>=2, give

    (log n)^(k+1)/n^2
       <= (9/4) integral_n^(n+1) (log x)^(k+1)/x^2 dx.

Summing and substituting u=log x bounds the sum by
(9/4) integral_0^infinity u^(k+1)exp(-u)du=(9/4)(k+1)!;
the last equality follows by repeated integration by parts. Therefore
Lambda(n)<=log n and the exact entries in (20) imply

    |q(H)_(j,j+d)|<=b_d,
    b_0=9/4,
    b_d=(9/4)sum_(k=1)^d binom(d-1,k-1)3^k(k+1)
       =(27/16)(3d+5)4^(d-1),  d>=1.

The finite binomial sum is evaluated by differentiating (1+x)^(d-1)
once and setting x=3, including d=1 directly. All estimates are uniform
in N, X and j whenever j+d<N; they price the entire infinite arithmetic
sum, not a short-prime approximation.

The Hermitian compression of q(H)+q(H)^* to a consecutive m-block has
diagonal absolute values at most 2b_0 and two possible off-diagonal
entries of size at most b_d at each distance d. Its maximum absolute
row sum, and hence its spectral norm, is at most

    2 sum_(d=0)^(m-1)b_d = (9/32)(3m+1)4^m.

The equality follows by summing the geometric series and its derivative;
it gives 9/2 at m=1 as required. For completeness, the row-sum bound
for a Hermitian matrix M also follows from
|x^*Mx|<=sum_(j,k)|M_jk|(|x_j|^2+|x_k|^2)/2.
Divide by ell_X and apply (4) in the unitary coordinates to obtain
(22). As ell_X>(1/2)log T, its right side tends uniformly to zero
when m4^m=o(log T). For a unit vector supported in I, the normalized
K-Rayleigh quotient is 1+x^*U^*R Ux, proving the stated witness exclusion.

This bounded lower-witness test fails for the stated blocks. It does
not exclude vectors spread over the full N-dimensional space, nor does
it control correlations between widely separated coordinates. Inserting
m=N into (22) gives an upper bound growing at least as a positive
power of T, and provides neither a margin nor a lower obstruction.
The full signed norm question is still open. No numerical spectrum or
new zero-statistics input is used in this exclusion.

## Mathlib

Full matching coverage is not checked; no absence claim is made. The
proof uses finite-dimensional Hermitian linear algebra, the named Schur
triangularization theorem, the Vandermonde
determinant, Cauchy's coefficient estimate, matrix power series and the
named DLMF inputs. No specific Mathlib theorem for their assembled
dimension-uniform specialization has been identified. General reference:
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
