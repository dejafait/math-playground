# Lemma 626: a uniform dyadic signed operator margin

## Hypotheses

Use the actual Xi, A, Z, W, nonnegative fixed
w in C_c^infinity((0,1)) with integral 1, L=log T,
T<=X<=2T, N=floor(T^(1/100)), common real unit observer
c=(c0,c1), U_c, and exact Hermitian matrix K_c(T,X) of L622.
Let

    J_T=floor(log N/log 2),
    I_T={2^j: 0<=j<=J_T},
    K_c^dyad=(K_c(2^j,2^k))_(0<=j,k<=J_T).

All coefficient vectors below are arbitrary complex vectors; they
may depend on T,X,c. The observer is common to every frequency.
Retain L622's full six-term collision sum, exact analytic Hardy
phase, both twist orientations and original pair multiplicities.
Use its audited transfer (1) and the audited H=T case of L619.
From L623 only Section 1's p=2 autocorrelation is used, with its
normalization verified below; its full Gram argument is not assumed.

The arithmetic and complete-sum holomorphy inputs remain named
imports: C. P. Hughes and M. P. Young, *The twisted fourth moment
of the Riemann zeta function*, J. reine angew. Math. 641 (2010),
203–236, [arXiv:0709.2345v2, Theorem 1.1/(13)–(17), printed
pp. 4–5 and the following holomorphy remark; Lemma 6.9/(139)–(155),
pp. 22–24](https://arxiv.org/pdf/0709.2345v2#page=4).
Their manuscript proofs are not audited here. No RH, zero-free
improvement, simplicity, spacing or pointwise sign is assumed.

## Conclusion

Put

    rho=2^(-1/2),
    r(e)=rho^e(1+e/3),
    G_J(j,k)=r(|j-k|),  0<=j,k<=J,
    B(c)=(28c0^2+c1^2)/(840 pi^2),
    gamma=1/[12(1+rho)^4],
    m_*=1/[10080 pi^2(1+rho)^4].

There is C_w, independent of T,X,c and J_T, such that for all
sufficiently large T the Euclidean operator norm satisfies

    ||K_c^dyad-B(c)G_(J_T)|| <= C_w/L.                  (1)

In particular, uniformly in X and the common real unit observer,

    lambda_min(K_c^dyad) >= B(c)gamma-C_w/L,
    lambda_min(K_c^dyad) >= m_*/2                       (2)

beyond one onset. For every unit vector a supported on I_T, set
M(t)=sum_(n in I_T) a_n n^(-it). Enlarging that onset if needed,

    integral w((t-X)/T) W(t)|M(t)|^2 U_c(t)^2 dt
                         /(T L^6) >= m_*/4 > 0.        (3)

The constants in (2)–(3) are explicit positive margins, but the
onset and error constant are existential. This is a specialization
of the imported moment theorem and finite Toeplitz bounds, with a
newly supplied local comparison proof; no priority claim or new
arithmetic theorem is asserted. It excludes this dyadic averaged
witness family. Cross-prime interactions, pointwise initial signs
at unbounded heights and all-degree mixed positivity remain open.
The separate conceptual application audit of 1 November 2026 below
validates (1)–(3) under the named imports. It does not audit the
source manuscripts or establish an all-prime or pointwise sign.

## Proof

### 1. Uniform absolute deformation of the dyadic local factor

Write q=(alpha,beta,gamma0,delta) here, using gamma0 to distinguish
the shift from the constant gamma in the conclusion. For e>=0 set

    D(q)=sum_(u>=0) sigma_(alpha,beta)(2^u)
                       sigma_(gamma0,delta)(2^u) 2^(-u),
    N_e^h(q)=sum_(u>=0) sigma_(alpha,beta)(2^u)
                       sigma_(gamma0,delta)(2^(u+e)) 2^(-u),
    N_e^k(q)=sum_(u>=0) sigma_(alpha,beta)(2^(u+e))
                       sigma_(gamma0,delta)(2^u) 2^(-u).

These are precisely L622's source factors for (h,k)=(2^e,1)
and (1,2^e): B_e^h=N_e^h/D and B_e^k=N_e^k/D. At e=0
both quotients are 1. At zero shifts, the geometric-series sums give

    D(0)=sum_(u>=0)(u+1)^2 2^(-u)=12,
    N_e^h(0)=N_e^k(0)=12+4e,
    b_e:=B_e^h(0)=B_e^k(0)=1+e/3.                      (4)

We need a bound with explicit e-dependence, rather than a fixed-e
Taylor error. Suppose max_i |q_i|<=6/L and set eta=6 log(2)/L.
In either numerator, each of the (u+1)(u+e+1) summands before
the factor 2^(-u) is exp(z), with |z|<=eta(2u+e).
The identity exp(z)-1=z integral_0^1 exp(sz) ds gives

    |N_e^h(q)-N_e^h(0)|, |N_e^k(q)-N_e^k(0)|
      <= eta exp(eta e) sum_(u>=0)
          (2u+e)(u+1)(u+e+1) 2^(-u) exp(2eta u).      (5)

For L>=24, 2^(-u)exp(2eta u)<=2^(-u/2). Also
u+e+1<=(u+1)(e+1) and 2u+e<=2(u+1)(e+1). Thus, with
the fixed finite constant S_3=sum_(u>=0)(u+1)^3 2^(-u/2),

    |N_e^h(q)-N_e^h(0)|, |N_e^k(q)-N_e^k(0)|
          <= 2 eta S_3 (e+1)^2 exp(eta e),
    |D(q)-12| <= 2 eta S_3.                            (6)

The same bounds provide locally uniform convergence of the defining
series; differentiation or finite divisor expansion does not require
an unproved interchange. For sufficiently large L, |D(q)|>=6
throughout this closed shift domain. The quotient identity and
N_e(0)<=12(e+1) now give, for either orientation,

    |B_e(q)-b_e|
      <= |N_e(q)-N_e(0)|/6+N_e(0)|D(q)-12|/72
      <= C (e+1)^2 exp(eta e)/L.                       (7)

For the allowed exponents, 2^e<=N implies
e log 2<=L/100, hence exp(eta e)<=exp(6/100).
All six source permutations preserve max_i |q_i|, so (7) yields

    |B_e(q^pi)-b_e| <= C (e+1)^2/L                     (8)

for every one of them and both orientations, with one constant.
The same convergence/nonvanishing argument with 7 in place of 6
gives holomorphy on a neighborhood of the domains used next.
Uniform relative o(1) in e is neither asserted nor needed.

### 2. Complete-sum comparison, exact phase and signed extraction

Keep L622's definitions q(b)=(ib1,ib2,-ib3,-ib4)/L, Phi(t,b),
S_hk(t;q), H_hk(b), Q and V_c. Work first on the separated torus

    |b1|=3, |b2|=4, |b3|=5, |b4|=6.

Every polar linear form in a zeta numerator is, up to sign,
i(b_j-b_k)/L. Its numerator difference has modulus at least 1
and at most 12. The Laurent expansion at the simple pole therefore
bounds each of the four zeta factors by C L. The reciprocal zeta
factor near 2 is bounded. Each unswapped or swapped J(q^pi) in
L622 (3) is consequently O(L^4) on this torus. The six exponential
weights are bounded, since log(t/(2pi))/L is bounded for T<=t<=3T.

Subtract b_e times the complete untwisted sum before passing to
collisions. Formula (8) gives, for either (h,k)=(2^e,1) or (1,2^e),

    |S_hk(t;q(b))-b_e S_11(t;q(b))|
                       <= C L^4 (e+1)^2/L.             (9)

L622 (8), on this fixed enlarged shift domain, bounds the exact
Phi uniformly. Since integral w((t-X)/T) dt=T and sqrt(hk)=2^(e/2),
the holomorphic difference

    E_hk(b)=H_hk(b)-rho^e b_e H_11(b)

has torus bound

    |E_hk(b)| <= C_w rho^e(e+1)^2/L.                   (10)

No phase has been frozen: the same exact Phi multiplies both sides
of the subtraction. The two complete main sums are holomorphic
on a neighborhood of the enclosed polydisc, by L622's imported
complete-sum holomorphy; Section 1 excludes additional local-factor
poles. The reciprocal zeta denominators are near 2 and nonzero.
The compact t integration preserves holomorphy. Successive maximum
principles therefore extend (10) to |b_j|<=2, including all collisions.
Only complete holomorphic differences are evaluated or differentiated
there; the estimates for singular summands were confined to the torus.

Cauchy's formula on the four unit circles gives total Q cost 3:
the two second-derivative factorials cancel their coefficients 1/2.
The V_c cost is (|c0|+|c1|)^2<=2. Thus, with J_hk(c) as in L622,

    |J_hk(c)-r(e)J_11(c)|
                      <= C_w rho^e(e+1)^2/L.           (11)

This controls every term of Q V_c, including the mixed c0 c1
terms. The estimate is uniform in c,X and the entire allowed chain.
At e=0 the difference is exactly zero.

### 3. Summation in the original coefficient norm

Set beta_c=Re J_11(c). For m=2^j,n=2^k, gcd reduction gives
precisely the two orientations used in (11), with e=|j-k|.
L622 (5)'s transposition and conjugation consequently give

    |(K_c^dyad-beta_c G_(J_T))_(j,k)|
                      <= C_w rho^|j-k|(|j-k|+1)^2/L.  (12)

All original pairs are present. In each row there are at most two
entries of a given positive exponent difference, regardless of J_T.
In particular the row sums of absolute errors are at most

    (C_w/L)[1+2 sum_(e>=1)(e+1)^2 rho^e] <= C'_w/L.    (13)

This is a convergent numerical series independent of T. If E denotes
the Hermitian error matrix in (12), then for any complex vector a,

    |a^* E a| <= sum_(j,k)|E_jk||a_j||a_k|
      <= (1/2) sum_(j,k)|E_jk|(|a_j|^2+|a_k|^2)
      <= (C'_w/L)||a||_2^2.

The last inequality uses |E_jk|=|E_kj|. The Hermitian Rayleigh
characterization therefore gives ||E||<=C'_w/L. This argument
does not multiply an entrywise error by the chain length.

### 4. Reference normalization and finite-section spectral bounds

For clarity verify the p=2 specialization of L623 Section 1, since
no audit of that entire lemma is being claimed. Put v_u=(u+1)rho^u
for u>=0. These coefficients are absolutely summable, and (4) gives

    sum_(u>=0) v_u v_(u+e)=rho^e(12+4e)=12 r(e).

Consequently the absolutely convergent two-sided Fourier series
with coefficients r(|e|) has the real symbol

    f(theta)=(1/12)|sum_(u>=0) v_u exp(iu theta)|^2
            =1/[12|1-rho exp(i theta)|^4].             (14)

The multiplication of series is legitimate by absolute convergence;
the generating function is sum_(u>=0)(u+1)z^u=(1-z)^(-2),
|z|<1. Thus every finite G_J is exactly the Hermitian Toeplitz
section of this single fixed symbol, and

    gamma=1/[12(1+rho)^4] <= f(theta)
                       <= Gamma=1/[12(1-rho)^4].       (15)

Apply Robert M. Gray, *Toeplitz and Circulant Matrices: A review*,
[author-hosted draft, Lemma 4.1/(4.11)–(4.16), printed pp. 41–43;
Section 4.1/(4.3)–(4.8), pp. 38–40](https://ee.stanford.edu/~gray/toeplitz.pdf).
Its finite Hermitian section bounds apply because the coefficients
are absolutely summable, the symbol is real and bounded, and (14)
is the exact coefficient normalization. They give

    gamma I <= G_J <= Gamma I                          (16)

for every J, including J=0. The Hermitian Rayleigh characterization
used here and in Section 3 is Gray Lemma 2.1/(2.2)–(2.7), printed
pp. 12–13. These spectral results are imported, not reproved.
The published counterpart is *Foundations and Trends in Communications
and Information Theory* 2(3) (2006), 155–239,
[DOI 10.1561/0100000006](https://doi.org/10.1561/0100000006);
the page numbers above refer to the inspected author draft.

### 5. Scalar margin and transfer to the actual-Xi integral

Use the H=T case of L619 with delta=1/26 and sigma=1/88, already
audited in that scope. Its relative error is uniformly O_w(1/L),
since T^(3+sigma)/T^(13/4)=T^(-21/88) and its curvature error
also tends to zero faster than 1/L. Since B(c) is bounded above
and below for real unit c, it follows that

    integral w_XT W U_c^2 dt/(T L^6)=B(c)+O_w(1/L).

Apply L622 (1) to the unit coefficient at n=1. Its matrix value
is exactly beta_c, so

    beta_c=B(c)+O_w(1/L).                              (17)

Here L622's absolute transfer error

    epsilon_T=C_w[T^(-17/80)/L^4+T^(-199/100)/L^2]       (18)

is O_w(1/L) as well. Combining (13), (16) and (17) yields

    ||K_c^dyad-B(c)G_(J_T)||
      <= C'_w/L+|beta_c-B(c)| Gamma <= C''_w/L,

which is (1). In particular B(c)>=1/(840 pi^2), and
(16) gives B(c)gamma>=m_*. Choose one onset so C''_w/L<=m_*/2.
Rayleigh's bound proves both inequalities in (2).

Extend a dyadic coefficient vector by zero to all n<=N. Its
Euclidean norm is unchanged, and its quadratic form is precisely
that of K_c^dyad. L622 (1) applies with the same error (18),
uniformly in all coefficients and the common observer. Choose
the onset also so epsilon_T<=m_*/4. This gives (3), with every
Xi completion and curvature cost already included in L622.
No zero of Xi was divided out; central real multiplicities require
no extra hypothesis.

The reference comparison succeeds because the absolute errors in
(12) are summable. It does not contradict L623's relative local-factor
freezing counterexample, which persists at e comparable to L.
It also makes no inference from a failed row-dominance test: (13)
is used for the error around a positive Toeplitz reference, not
for dominance of K_c itself. This proof contains no numerical
eigenvalue evidence, effective height claim or RH resolution.

### Separate conceptual application audit — 1 November 2026

The unchanged dyadic target was replayed against L622 (1)/(3)–(12),
L619's already audited H=T application and L623 Section 1 only.
No conclusion or exponent required correction. The following checks
make explicit the growing-index and analytic-domain obligations.

For either orientation, a summand in N_e has (u+1)(u+e+1)
divisor choices and a total of 2u+e prime exponents. Hence the
complex exponential bound (5) applies to each summand, with no
positivity assumption on the shifts. The inequalities preceding
(6) give the stated cubic summable majorant when L>=24.
For D use the same calculation with e=0. Enlarging to |q_i|<=7/L
and increasing the onset gives geometric domination and |D|>=6
on an open neighborhood of every required closed domain. The
growing exponent appears only in the explicit factors (e+1)^2
and exp(6e log(2)/L)<=exp(6/100). A fixed-e Taylor estimate was
not substituted for (7), nor was uniform relative freezing used.

To check all six singular summands on the torus, index each source
permutation by its two positive-height labels S. In L622 (3) these
are respectively {1,2}, {3,4}, {2,3}, {2,4}, {1,3}, {1,4}.
The four numerator arguments are then
1+i(b_j-b_k)/L for j in S, k outside S, up to a reordering.
Distinct radii 3,4,5,6 ensure 1<=|b_j-b_k|<=12.
Thus every numerator is O(L) by the Laurent expansion on this
fixed annulus in the scaled variable. The denominator has argument
2+O(1/L), remains in Re(s)>1, and its reciprocal is bounded.
All swap exponentials are bounded uniformly for t in [T,3T].
Each permuted local factor obeys (8), including the two twist
orientations. This verifies (9) for the complete difference.

The exact phase estimate extends to |b_j|<=7: the complex segments
t+s b_j/L stay in the same gamma sectors of L622 Section 2, and
their lengths are bounded by 7/L. Its constants change only by a
fixed factor. Complete-sum holomorphy is used on the entire enclosed
polydisc, not inferred from a torus bound. Together with the local
nonvanishing check above and the compact integration, the named
holomorphy import permits successive maximum principles and
Cauchy extraction. No pole term is evaluated alone at a collision.
No approximation of Phi is made in this comparison.

For Q the mixed derivative costs 1 and the two repeated derivatives
cost (1/2)2!=1 each. For V_c the four costs are c0^2,
|c0 c1|, |c0 c1|, c1^2. Their sum is at most 2 for a real
unit observer; thus all twelve terms of Q V_c cost at most 6.
The coefficients and observer are held fixed during differentiation.
This proves the full mixed-observer estimate (11), not merely the
two diagonal-observer cases.

In (5) of L622 the two oriented errors average after conjugation.
Their common reference becomes r(e) Re J_11; its e=0 error is
exactly zero. Every original dyadic pair survives gcd reduction,
and any row has at most two pairs with a given e>0. The convergent
series in (13) therefore controls the Hermitian operator norm
without a factor J_T or N. This is a bound on the error about a
positive reference, so the earlier diagonal-dominance stop is
irrelevant to this estimate and remains valid.

Independently checking the reference normalization gives
sum (u+1)^2/2^u=12 and sum (u+1)/2^u=4; the Fourier coefficient
of |(1-rho exp(i theta))^(-2)|^2 at distance e is consequently
rho^e(12+4e). Its division by 12 produces exactly G_J, including
unit diagonal. Absolute summability justifies this coefficient
calculation. Gray's finite-section bounds thus give precisely
gamma and Gamma in (15), uniformly for every J, without invoking
an asymptotic spectral-distribution theorem.

For the scalar input, delta=1/26 admits sigma=1/88, since
1/88<min(1/4,13delta/4)=1/8. The L619 error at H=T is
1/L+T^(-21/88)/L^4 with completion cost
O_w((1+e(T,T))/(T^2 L^2)); its coefficient margin is exactly
(c0^2/30+c1^2/840)/pi^2. The unit coefficient at n=1 in L622
has value Re J_11, even though the full length is N. This verifies
(17) without transferring a frozen-phase error through an amplifier.
Multiplying |beta_c-B(c)| by the uniform Gamma costs O_w(1/L),
so (1) follows in the original coefficient norm.

Finally B(c)gamma>=m_* and epsilon_T in (18) tends to zero.
One onset, independent of X,c,a, can impose both C''_w/L<=m_*/2
and epsilon_T<=m_*/4. Zero-extension of a dyadic vector preserves
its norm, proving the actual-Xi bound (3). The audit uses the
zero-safe completion of L622; it divides neither by Xi nor Z.
This validates the restricted averaged conclusion, with no effective
onset, source-manuscript audit, cross-prime comparison or RH claim.

## Mathlib

Full matching coverage for this dyadic signed comparison and its
actual-Xi consequence has not been checked and is unknown. The
named arithmetic/holomorphy imports are unchanged. Gray's finite
Hermitian Toeplitz theorem supplies the spectral step; the required
normalization, summability, analytic domains, coefficient norm and
signed derivative costs are established explicitly above. No Lean
certificate or numerical spectrum is claimed. The separate informal
application audit above does not change the unknown Mathlib coverage.
