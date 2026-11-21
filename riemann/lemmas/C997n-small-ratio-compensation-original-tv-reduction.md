# Corollary 997n: small-ratio compensation has a charged original-TV error

## Hypotheses

Use C997c(1)'s complete response, with integer n>=2,

    K_(n+2)(t)=(L_(n+1)^(2)(t)-1)/(n+1),
    g_n(t)=K_(n+2)(t)*exp(-t/2)*cosh(3t/8),
    H_n^+(z;mu)=-2*integral_I exp(-cn/4)*[
        integral_(cn)^(c(n+2)) g_n(t)*exp(izt)dt
        -integral_n^(n+2) g_n(t)*exp(izt)dt]dmu(c).

Here I=[7/4,9/4], J=[15/8,17/8], delta=1/8, z_star=1+i/8,
and phi is C997e's real phase

    phi(c)=arccos(1-c/2)+sqrt(c*(4-c))/2.

Fix A>=A_0>=16 before n, with C997e's existential A_0, and take
exactly C997m(1)'s parameters theta=1 and lambda=A/128. Write

    r_n=floor(lambda*n), E_r(u)=sum_(j=0)^r u^j/j!,
    Q_r(u)=exp(-u)*E_r(u), b_n(x)=(1-64*x^2)^n,
    w_n(x)=b_n(x)*Q_(r_n)(An*x^2),
    M_n=integral_(-delta)^delta w_n(x)dx,
    N_n=integral_(-delta)^delta b_n(x)dx,
    dmu_n(c)=1_J(c)*w_n(c-2)*exp(in(phi(c)-c))dc/M_n,
    dnu_n(c)=1_J(c)*b_n(c-2)*exp(in(phi(c)-c))dc/N_n.       (1)

The comparison nu_n is an auxiliary pure endpoint measure, not an
assertion that the finite exponential equals the full exponential.
These are finite hypothetical slope measures, not zeta-zero data.

## Conclusion

Both measures have original total variation one. For every n>=2,

    0<=b_n(x)-w_n(x)<=exp(-n/16), |x|<=delta,
    0<=N_n-M_n<=exp(-n/16)/4,
    N_n>=1/(8*sqrt(2*n)),
    ||mu_n-nu_n||_TV<=4*sqrt(2*n)*exp(-n/16).             (2)

There is a finite constant C, independent of n and of the real
observation point gamma in the CLOSED J, such that for all sufficiently
large n,

    sup_(gamma in J)|H_n^+(gamma;mu_n)-H_n^+(gamma;nu_n)|
                                <=C*n^(-1)*exp(13*n/64),
    |H_n^+(z_star;mu_n)-H_n^+(z_star;nu_n)|
                                <=C*n^(-1)*exp(-n/16).   (3)

Thus the complete-response correction has upper logarithmic rate
at most 13/64 on the data band. This bound GROWS; it is neither band
suppression nor leakage. In particular, if a separate argument supplies
some rho>13/64 and an unbounded integer subsequence on which

    |H_n^+(2;nu_n)|>=exp(rho*n),                          (4)

then the same subsequence eventually has
|H_n^+(2;mu_n)|>=exp(rho*n)/2, ruling out uniform exponential
suppression for this parameter subfamily. Hypothesis (4) is UNPROVED.

C997m(2) already supplies nonzero target retention for mu_n, with
H_n^+(z_star;mu_n)=n^(-3/2)*(B_star+o(1)). Equation (3) transfers
that same asymptotic to nu_n. No new target normalization is needed.

Step350, 11 November 2026: RESEARCH / REPRODUCTION, outcome ADVANCE
under the unchanged pre-invocation EXPLORE assessment345. This is a
local error estimate using a standard exponential-tail bound, not a
claim of original mathematics beyond the sources checked. The separate
audit in step357 below accepts (1)-(9) with their original hypotheses
and bounds. No data lower bound, family-wide stop or RH candidate is
established.

## Proof

### Known inputs and the necessary specialization

Import the exact nonnegative-integer finite-exponential identities from
NIST DLMF version1.2.8 (15 September 2026),
[8.4.7-11](https://dlmf.nist.gov/8.4#E7), together with the entire
exponential series [1.10.2](https://dlmf.nist.gov/1.10#E2).
For integer r>=0 and real u>=0 they imply 0<Q_r(u)<=1 and exactly

    1-Q_r(u)=exp(-u)*sum_(j=r+1)^infinity u^j/j!.          (5)

Every series term here is nonnegative and the series converges
absolutely. This is also the normalized lower incomplete gamma from
[8.2.1](https://dlmf.nist.gov/8.2#E1), with positive integer shape r+1.
No large-order incomplete-gamma asymptotic or complex replacement is
used. The elementary exponential-tail specialization below is written
out to fix the constants and the floor; no general tail theorem is
being proposed or reproved as new mathematics.

Use C997e(4),(15)-(16)'s exact analytic Laguerre amplitudes, based on
M. Vanlessen, *Strong asymptotics of Laguerre-type orthogonal polynomials
and applications in random matrix theory*,
[math/0504604v2](https://arxiv.org/pdf/math/0504604v2), Theorem2.4(b),
Proposition3.31, Theorem3.32 and Proposition5.1/(5.5)-(5.6).
The real-interval specialization and normalization have already been
proved and audited in C997e. Only their bounded values on the real J
are needed here; no enlarged complex domain is imported. C997c(5)
pays the complete lower interval in original variation. C997m supplies
the existing packet definition and target asymptotic. The new local
work is charging (5), the endpoint weight and normalization against
the COMPLETE response, including uniformity in the closed band.

### Exact correction on the real slope interval

Put k=r_n+1>lambda*n and v=64*x^2 in [0,1]. Then
u=An*x^2=2*lambda*n*v. When v<=1/8, we have u<=lambda*n/4<k/4.
For u>=0, (5) and 4^j>=4^k for j>=k give

    1-Q_(r_n)(u)
       <=4^(-k)*exp(-u)*sum_(j=k)^infinity (4*u)^j/j!
       <=4^(-k)*exp(3*u)
       <=exp(-k*(log(4)-3/4))
       <=exp(-k/2)<=exp(-n/16).                          (6)

For the penultimate inequality, log(4)>5/4. For example the identity
1/t-(4/3-4*t/9)=(2*t-3)^2/(9*t) gives
log(2)>integral_1^2(4/3-4*t/9)dt=2/3, hence log(4)>4/3.
For the last inequality lambda=A/128>=1/8 and k>lambda*n.
This checks the floor without replacing it by a real index.

When v>=1/8, use 0<=1-Q_(r_n)(u)<=1 and
(1-v)^n<=exp(-n*v)<=exp(-n/8); at v=1 the left side is zero.
Combining this with (6) and b_n<=1 proves the first inequality of (2).
Integration over an interval of length 1/4 proves its second inequality.
No contour deformation, cutoff limit or discarded correction is involved.

The interval |x|<=1/(8*sqrt(2*n)) lies in [-delta,delta]. On it,
Bernoulli's inequality gives

    b_n(x)>=(1-1/(2*n))^n>=1/2.

Its length is 1/(4*sqrt(2*n)), proving the lower bound for N_n in (2).
Both M_n and N_n are strictly positive because their continuous
nonnegative integrands are positive in the interior. The real phase
has modulus one, so both original total variations are exactly one.

Let D_n=N_n-M_n>=0. The exact density decomposition

    w_n/M_n-b_n/N_n
       =(w_n-b_n)/N_n+w_n*(1/M_n-1/N_n)

and w_n<=b_n give

    ||mu_n-nu_n||_TV<=D_n/N_n+M_n*(1/M_n-1/N_n)
                         =2*D_n/N_n.

The bounds just proved give the final inequality of (2). In particular
there is no uncharged change of norm or normalization factor.

### Complete-response bound on the real band and at the target

We establish the needed operator estimate for any finite complex measure
eta supported on J, with V=||eta||_TV. The positive-beta upper Laguerre
term in the exact response, after t=c(n+u), is

    -n^(-3/2)*integral_J c*exp(n*c*(1/8+i*z))*[
       integral_0^2 exp(c*u*(3/8+i*z))*
        (exp(-in*phi(c))*B_(-,n)(c,u)
         +exp(in*phi(c))*B_(+,n)(c,u))du]deta(c).         (7)

This follows from C997e(4): the coefficient -2 cancels cosh's 1/2,
and the exponential factors are exp(-cn/4)*exp(t/2)*
exp((-1/8+iz)*t). Both exact amplitudes B are uniformly bounded
for real c in J and u in [0,2]. Since phi is real there, both
oscillatory factors have modulus one. For real gamma in the closed J,
the absolute c,u factors in (7) are bounded by a fixed constant times
exp(n*c/8)<=exp(17*n/64). For z_star=1+i/8 the n-dependent real
exponent is zero and the u factor is exp(c*u/4), again bounded.
Consequently the absolute value of (7) is at most

    C*n^(-3/2)*exp(17*n/64)*V,  z=gamma in J,
    C*n^(-3/2)*V,                         z=z_star.     (8)

These are genuine uniform real-band bounds, including its endpoints;
they do not require analytic continuation of an error symbol.

For completeness, the reflected-beta upper Laguerre term has, after
the real Laguerre bound in C997e, exponential factor at most
exp(-cn/4-3*t/8). The entire K subtraction, with both beta signs, has
factor at most exp(-cn/4-t/8). Here t>=cn and interval lengths are
2c<=9/2, so these terms are bounded by C*(n+2)*exp(-n/16)*V.
C997c(5) bounds the COMPLETE lower interval by
8*exp(3/4)*(n+2)*exp(-n/16)*V. At z_star the extra exp(-t/8)
only improves each bound. Thus all omitted terms together are at most

    C*(n+2)*exp(-n/16)*V.                                (9)

Both slope endpoints, both Laguerre branches, both beta terms, both
short intervals and K's -1 are now accounted for. All integrations are
over compact sets against finite variation, so the substitutions and
finite-integral interchanges are justified as in C997c(4)-(6).

For all sufficiently large n, (9) is absorbed in the corresponding
bound (8), since n^(5/2)*exp(-n/16) tends to zero. Apply the resulting
linear operator bounds to eta=mu_n-nu_n and use (2). This yields (3),
with data exponent 17/64-1/16=13/64 and factor n^(-3/2)*sqrt(n)=n^(-1).
In particular the response remainder is paid in the ORIGINAL
variation of the difference measure, without a second division by M_n.

If the independent hypothesis (4) holds, the triangle inequality and
(3) give, along that subsequence,

    |H_n^+(2;mu_n)|>=exp(rho*n)-C*n^(-1)*exp(13*n/64).

Since rho>13/64, the second term is eventually at most half the first.
This proves the stated conditional implication only. The target transfer
follows from (3) because n^(3/2)*n^(-1)*exp(-n/16) tends to zero and
C997m's B_star is nonzero.

### What remains unresolved

This calculation charges the finite-exponential correction without
assuming complex compensation. It does NOT establish (4). The natural
pure-endpoint stationary-point proposal at theta=1 has a fixed complex
displacement; C997e's stated existential amplitude neighborhood does
not, by itself, certify a contour through that point. C997m's
large-theta argument arranged containment by sending its saddle toward
zero. Here theta is fixed at 1, and increasing A cannot move the
comparison packet's saddle. Neither containment nor its failure is
inferred. Exact amplitude control on a sufficient contour, leading
nonvanishing, both endpoint charges and other-branch dominance remain
to be justified before any data leakage claim.

C997i's degree<=n stop does not apply: the actual polynomial degree
is 2*(n+r_n)>=2*n>n. C997m's strong-taper leakage theorem also does
not apply to theta=1,lambda=A/128. No stopped result has been reopened
by relabeling its hypotheses. C997m's target retention remains valid.

The point bridge, selected/both-sign transfer, C997a(8), original assay
and reconstruction, signed recovery, complementary zeros, regulators,
L993, L984(H) and L030-L032/C032a actual-Xi positivity remain unpaid.
No cross-notebook input, numerical certificate or complete RH candidate
is used or produced.

### Independent correction audit — step357, 11 November 2026

RESEARCH / REPRODUCTION under the unchanged SPECIALIZE assessment
`drafts/literature/2026-11-11-small-ratio-correction-audit-review-355.md`,
separately approved in step356. The audit accepts (1)-(9). It verifies
the written specialization of the cited inputs; it supplies neither a
stronger bound nor an originality claim. A and lambda=A/128 are fixed
before n; the asymptotic operator estimates have an existential onset.

**Indices and real tail.** At theta=1, floor(theta*n)=n exactly.
Since A>=16, lambda>=1/8 and r_n>=0. Thus k=r_n+1 is a positive
integer with k>lambda*n, including when lambda*n is an integer.
For v=64*x^2<=1/8, u=2*lambda*n*v<k/4. In (5), multiplying each
term of index j>=k by 4^j/4^k only increases it. Completing that
nonnegative sum to exp(4u) proves the first two inequalities of (6).
Then 3u<=3k/4 and log(4)>4/3>5/4 give

    4^(-k)*exp(3u)<=exp(-k*(log(4)-3/4))
                        <=exp(-k/2)<=exp(-n/16).

The displayed integral identity proving log(2)>2/3 is valid on [1,2]
and strict after integration, since its nonnegative square vanishes
only at 3/2. In the complementary range v>=1/8 the endpoint factor
alone is at most exp(-n/8); at v=1 it is zero. These two cases cover
the whole closed interval without assumptions on complex Q_r.
The exponential/gamma source hypotheses are exactly integer r_n>=0
and real u>=0, so their previously inspected scope suffices.

**Original normalization.** The central interval used for N_n has
length 1/(4*sqrt(2*n)) and lies in [-1/8,1/8]. There 64*x^2<=1/(2*n)
and Bernoulli gives b_n>=1-n/(2*n)=1/2. Hence its claimed lower
bound holds for every n>=2. Q_r is strictly positive for finite u,
and b_n is positive in the interior, so M_n,N_n>0. The common phase
has modulus one on real J; the variations of the two normalized
measures are exactly one, regardless of their complex total masses.
The integral of b_n-w_n is D_n<=exp(-n/16)/4. In the exact density
decomposition the second summand has integral of its absolute value
M_n*(1/M_n-1/N_n)=D_n/N_n. The first has integral D_n/N_n as well.
Their triangle inequality gives

    ||mu_n-nu_n||_TV<=2*D_n/N_n
                       <=4*sqrt(2*n)*exp(-n/16).

No lower bound for M_n, or extra division by M_n, is required here.

**Exact leading term and closed-band uniformity.** Expand cosh and
K=L/(n+1)-1/(n+1) before taking absolute values. In the upper
positive-beta Laguerre term, -2 times the cosh coefficient 1/2 is
-1. C997e(4) and t=c(n+u), dt=c du, give precisely (7), since

    -cn/4+t/2-t/8+izt
        =nc*(1/8+iz)+cu*(3/8+iz).

C997e(15)-(16) retain both branches exactly. Their bounded values
on real c in the compact J and real u in [0,2] suffice; no continuation
of a real O term or enlarged-lens theorem enters this calculation.
For real gamma, |exp(i*gamma*t)|=1 and both exp(+/-in*phi(c)) have
modulus one. The largest nc/8 is 17n/64 at the closed right endpoint;
the u factor has modulus at most exp((3/8)*(17/8)*2). At z_star,
1/8+Re(iz_star)=0 and 3/8+Re(iz_star)=1/4. Thus (8) holds for
arbitrary finite complex eta of variation V, uniformly at both real
band endpoints as well as in its interior.

**Every remaining response term.** L997(4), including K's -1,
implies |L_(n+1)^(2)(t)/(n+1)|<=C*(n+2)*exp(t/2) for t>=0.
The reflected-beta upper Laguerre term therefore has factor
exp(-cn/4-3t/8)<=exp(-5cn/8). The entire constant-subtraction term,
with both beta signs, is bounded using cosh(3t/8)<=exp(3t/8)
by 2*exp(-cn/4-t/8)/(n+1)<=2*exp(-3cn/8)/(n+1). Their lengths are
2c<=17/4<9/2; c>=15/8 gives decay stronger than exp(-n/16).
C997c(5) pays the complete lower interval, both beta signs and the
constant subtraction together, in V. Its coarser I-based exp(-n/16)
bound is valid for eta supported on J subset I. At z_star the factor
exp(-t/8) only improves all three estimates. This proves (9) without
discarding an endpoint, branch, interval or constant. Compact Borel
integrands against dt*d|eta|(c) are absolutely integrable for each n,
as in C997c(4)-(6), justifying the substitutions and finite Fubini use.

Finally (n+2)*n^(3/2)*exp(-n/16)->0, so (9) is absorbed into (8),
also at z_star. Applying the resulting bounds to eta=mu_n-nu_n
gives n^(-3/2)*sqrt(n)=n^(-1) and
17/64-1/16=13/64, exactly (3). The reverse triangle inequality
proves only the implication conditional on (4) with rho>13/64.
At the target, n^(3/2) times the correction bound is
O(sqrt(n)*exp(-n/16))=o(1), which transfers the already audited
C997m(2) limit and its same nonzero B_star. No data lower rate or
dominance of a data branch has been proved in this audit.

The direct local mathematical inputs remain C997c, C997e and C997m;
their underlying L997 bound is used through C997c/e. No DAG edge
changes. The fixed-domain concern above records the situation at
step350; C997o's later audited domain does not enter this real-interval
audit or by itself settle the data-rate calculation. Nonvanishing,
endpoint and other-branch errors for that calculation, and all listed
actual-Xi/forcing/transfer gaps, remain unresolved.

## Mathlib

Full matching coverage for this weighted correction and complete-response
specialization has not been checked and is unknown. The cited exact
exponential/gamma identities, Bernoulli's inequality and finite-measure
integration are standard informal inputs. No absence claim, matching
Mathlib theorem name or Lean verification is asserted.
