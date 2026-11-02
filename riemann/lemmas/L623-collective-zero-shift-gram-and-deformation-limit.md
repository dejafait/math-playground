# Lemma 623: full zero-shift arithmetic Gram bound and its deformation limit

## Hypotheses

Let N>=1 be an integer. For each prime p and integer e>=0 put

    r_p(e)=p^(-e/2)(1+e(p-1)/(p+1)),
    G_N(m,n)=product_p r_p(|v_p(m)-v_p(n)|),  1<=m,n<=N.

Every product defining an entry is finite. This is precisely the
zero-shift arithmetic kernel B_hk(0)/sqrt(hk) in L622 (14), with
h=m/gcd(m,n), k=n/gcd(m,n). In particular every original pair and
its gcd multiplicity is retained, including all N diagonal entries.
The coefficients a_n are arbitrary complex numbers.

For the application only, use the complete matrix K_c(T,X), common
real unit observer c, fixed nonnegative smooth w, normalization,
N=floor(T^(1/100)), L=log T, and T<=X<=2T of L622. That lemma's
transfer remains a conditional, not separately audited input. Its
Hughes--Young and complete-sum holomorphy inputs retain their stated
qualifications. No zero-free hypothesis, RH, zero simplicity, signed
spectral bound or uniform growing-index leading expansion is assumed.

The arithmetic factor is taken from C. P. Hughes and M. P. Young,
*The twisted fourth moment of the Riemann zeta function*, J. reine
angew. Math. 641 (2010), 203–236,
[arXiv:0709.2345v2, (13)–(14) and Theorem 1.1, printed pp. 3–4;
Lemma 6.9/(139)–(155), pp. 22–24](https://arxiv.org/pdf/0709.2345v2#page=3).
The previously completed source comparison is reused. The elementary
autocorrelation and inverse-convolution computations below supply
the missing coefficient-uniform bound for this particular reference
kernel; they do not reprove the imported moment theorem or assert
that its six signed terms have this Gram representation.

## Conclusion

Let P_N be the finite set of primes <=N and S_N the positive integers
all of whose prime divisors belong to P_N, including 1. Write d for
the divisor-counting function, and define

    C_N=product_(p<=N) (1-1/p)^3/(1+1/p),
    b_r=sum_(n<=N, n|r) a_n d(r/n)/sqrt(r/n),  r in S_N.

There is an exact full-matrix Gram identity

    a^*G_N a = C_N sum_(r in S_N)|b_r|^2.                (1)

In particular, with

    gamma_N=1/[2 N^4(N+1)(1+log N)^2],

one has, for every complex a,

    a^*G_N a >= gamma_N sum_(n<=N)|a_n|^2.               (2)

The bound is deliberately coarse but uniform. At the approved length,
the reference signed form B(c)G_N, where

    B(c)=(28 c0^2+c1^2)/(840 pi^2),

has a lower bound at least

    T^(-1/20)/[3360 pi^2(1+L/100)^2].                  (3)

This exceeds the complete L622 transfer error asymptotically. It is
only a bound for the reference form, not for K_c. The required
comparison of K_c with that reference is unproved.

In fact the tempting uniform arithmetic-factor freezing is false.
Fix 0<tau<=1, take e=floor(L/(100 log 2)), h=2^e<=N, and
q_T=(0,0,tau/L,tau/L). In the source convention of L622,

    B_(h,1)(q_T)/B_(h,1)(0) --> exp(-tau/100),
    B_(1,h)(q_T)/B_(1,h)(0) --> 1.                       (4)

Thus replacing each shifted arithmetic factor by its zero-shift
value with a uniform relative o(1), in particular O(1/L), is
invalid on the allowed family. Formula (4) concerns analytic local
factors, not individual singular terms at shift collisions. It does
not determine the six-term signed sum or give a negative direction.

The full signed spectrum and actual-Xi sign remain unresolved.
These are elementary local consequences of the inspected arithmetic
factor and standard convolution identities, not a new moment theorem,
a claim of originality, or an RH candidate. This lemma has not yet
received a separate critical audit.

## Proof

### 1. Prime-power autocorrelation, with its normalization

Put x=1/p. The absolutely convergent sums, obtained by differentiating
the geometric series inside |x|<1, are

    D_p=sum_(j>=0)(j+1)^2 x^j=(1+x)/(1-x)^3,
    sum_(j>=0)(j+1)x^j=1/(1-x)^2.

For e>=0 it follows exactly that

    p^(-e/2) sum_(j>=0)(j+1)(j+e+1)p^(-j)
      =p^(-e/2)[D_p+e/(1-1/p)^2]=D_p r_p(e).           (5)

Consider, on the nonnegative integer exponents, the vector
v_i(j)=0 for j<i and v_i(j)=(j-i+1)p^(-(j-i)/2) for j>=i.
If i<=k, putting j=k+u in its scalar product with v_k gives
exactly the left side of (5) with e=k-i. Hence the normalized
scalar product is r_p(|i-k|). This argument includes e=0 and all
prime powers, not merely squarefree twists.

### 2. The full Gram map

For n<=N define a vector on S_N by

    v_n(r)=1_(n|r) d(r/n)/sqrt(r/n).

Multiplicativity and the finite number of primes give

    ||v_n||_2^2=product_(p<=N)D_p=C_N^(-1)<infinity.

The equality holds even when n contains a high prime power: shifting
the lower exponent of summation does not change the norm. The product
of (5) over P_N gives

    <v_m,v_n>=C_N^(-1)G_N(m,n).

One may factor these sums because their terms are nonnegative and
there are finitely many primes; all values are finite. For complex
linear combinations, there are only N vectors. Cauchy--Schwarz gives
absolute convergence of every scalar product, so expanding the finite
quadratic form through the square-sum is justified. Its components
are exactly b_r. This proves (1), without a finite-support or numerical
approximation to the infinite Gram sum.

### 3. A uniform lower bound from finite inverse convolution

Define the multiplicative function eta by

    eta(1)=1, eta(p)=-2, eta(p^2)=1, eta(p^j)=0 for j>=3.

It is mu*mu, but only the displayed values are needed. The local
identity (1-z)^2 sum_(j>=0)(j+1)z^j=1 shows that
d(k)/sqrt(k) and eta(k)/sqrt(k) are inverse Dirichlet-convolution
kernels. For each r<=N the finite divisor sums therefore give

    a_r=sum_(k|r) eta(k)b_(r/k)/sqrt(k).                 (6)

No infinite inversion or interchange is used here. Let U_N be the
lower triangular matrix mapping a to (b_1,...,b_N); its entries are
d(r/n)/sqrt(r/n) when n|r and zero otherwise. Let V_N=U_N^(-1),
whose entries are given by (6). Both have diagonal entries 1.

For k<=N the map sending b_j to the coordinate r=kj, when kj<=N,
and to zero elsewhere has Euclidean operator norm at most 1. The
triangle inequality applied to the sum of these maps in (6) yields

    ||V_N|| <= H_N := sum_(k<=N)|eta(k)|/sqrt(k).

Prime by prime, |eta(k)|<=d(k). Also, for every real y>=1,
sum_(j<=y) j^(-1/2)<=2sqrt(y), by integral comparison. Consequently

    H_N <= sum_(uv<=N)1/sqrt(uv)
        <= 2sqrt(N) sum_(u<=N)1/u
        <= 2sqrt(N)(1+log N).                           (7)

It follows from (1), discarding only nonnegative tail squares, that

    a^*G_N a >= C_N ||U_N a||^2
             >= (C_N/H_N^2)||a||^2.                    (8)

For each integer j>=2 the factor (1-1/j)^3/(1+1/j) lies in (0,1).
Adding the composite integers to the finite product can only decrease
it. The two resulting products telescope, giving

    C_N >= product_(j=2)^N (1-1/j)^3/(1+1/j)
         =2/[N^3(N+1)].                                (9)

Empty products make (9) valid at N=1 as well. Combining (7)–(9)
proves (2). This deliberately elementary bound avoids any additional
prime-distribution or Mertens-theorem input; optimal conditioning is
not required to compare the reference scale with the transfer error.

### 4. Actual versus required bounds, and the remaining comparison

For T>1, N<=T^(1/100), N+1<=2T^(1/100) and log N<=L/100.
Thus

    gamma_N >= T^(-1/20)/[4(1+L/100)^2].                 (10)

Since B(c)>=1/(840 pi^2) for the common real unit c, (3) follows.
Denote the error bound in L622 (1) by

    epsilon_T=C_w[T^(-17/80)/L^4+T^(-199/100)/L^2].

The ratio to the reference lower bound is at most

    3360 pi^2 C_w (1+L/100)^2
      [T^(-13/80)/L^4+T^(-97/50)/L^2] --> 0.            (11)

The power differences are 17/80-1/20=13/80 and
199/100-1/20=97/50. This comparison is uniform in c and X and
has the same existential-constant qualification as L622.

Here is exactly what (11) does not prove. Write

    R_c(T,X)=K_c(T,X)-B(c)G_N.

No upper bound small enough for ||R_c|| or for its negative
quadratic part has been established. For example, the inequality

    |a^*R_c a| <= (B(c)/2) a^*G_N a  for all a           (12)

would suffice, but is not an assumption or conclusion of this lemma.
L622's O_(h,k,w)(1/L) fixed-entry expansions cannot be summed with
a uniform constant when N grows. Even a hypothetical entrywise
O(1/L) bound would give only O(N/L) by absolute coefficient summation,
which is larger than the certified lower-bound scale in (3). This
last observation is a limitation of that proposed error estimate;
it is not a lower bound on the actual error or an impossibility
theorem for a sharper, correlated comparison.

There is an exact finite-coordinate way to state a possible subsequent
test without freezing the shifts. By (8),

    V_N^*G_N V_N >= C_N I.

For the still exact K_c a lower bound

    V_N^*K_c(T,X)V_N >= (B(c)/2) C_N I                  (13)

would also suffice. It implies K_c>=(B(c)/2)gamma_N I in the
original coordinates. L622's transfer, evaluated on a=V_N b,
has absolute error <=epsilon_T H_N^2 ||b||^2; this follows by
homogeneity from the unit-coefficient statement. Relative to C_N
it is at most epsilon_T/gamma_N, which tends to zero by (11).
Thus the finite change of coordinates itself does not exhaust the
transfer budget. Inequality (13), including all shifted factors and
the exact Hardy phase, remains wholly unproved. It is a concrete
comparison criterion, not another result about the signed spectrum.

### 5. Growing prime powers prevent uniform freezing of local factors

The source's h-side factor increments the (gamma,delta) divisor
function. At q=(0,0,s,s), use

    sigma_(0,0)(p^j)=j+1,
    sigma_(s,s)(p^j)=(j+1)p^(-js).

For s>=0 put x=p^(-1-s), so |x|<1. Applying the sums in Section 1
to the defining numerator and denominator gives the exact formulas

    B_(p^e,1)(0,0,s,s)=p^(-es)[1+e(1-x)/(1+x)],
    B_(1,p^e)(0,0,s,s)=1+e(1-x)/(1+x).                  (14)

For the second orientation it is the unshifted first divisor
function that is incremented, explaining the absent p^(-es).
Both equal 1+e(p-1)/(p+1) at s=0. These are direct evaluations of
convergent local series with nonzero denominator. Repeated shifts
cause no singularity in these factors, and no individual zeta-pole
term of the six-term sum has been assigned a value at collision.

Now choose p=2, s=tau/L and e=floor(L/(100 log 2)). For large T,
e>=1 and 2^e<=floor(T^(1/100))=N. One has

    e log 2/L --> 1/100,
    x=2^(-1-tau/L) --> 1/2,
    [1+e(1-x)/(1+x)]/[1+e/3] --> 1.

The two limits in (4) follow. These shifts are inside L622's bounded
complex b domain: b=(0,0,i tau,i tau) gives q(b)=q_T. Thus for
every fixed tau>0 the first relative error tends to
1-exp(-tau/100)>0. A uniform relative o(1) replacement of these
arithmetic factors is actually contradicted, not merely unproved.

The obstruction is restricted. After multiplication by 1/sqrt(hk),
large-ratio entries can be small; the six terms can cancel; and
the signed differential extraction is not the same as evaluating
this factor. Therefore (4) proves no negative eigenvalue, gives no
lower bound for ||R_c||, and does not refute (12) or (13). It stops
the attempt to justify a full Gram comparison by uniformly freezing
each local factor. Exact shifted correlations would need separate
control. The phase in K_c was never discarded.

## Mathlib

Full matching coverage for this arithmetic Gram kernel, its stated
uniform lower bound, the shifted-factor comparison, and L622's signed
transfer has not been checked and is unknown. Geometric-series
identities, finite Dirichlet convolution, Hilbert-space Gram positivity
and the triangle inequality are proved explicitly here as informal
mathematics; no Lean certificate or finite numerical spectrum is
claimed. The full infinite Gram sum and its convergence are justified
in the proof rather than inferred from a preview or numerical test.
