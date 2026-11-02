# Lemma 637: Hardy-translate inverse cost and the absolute-error budget

## Hypotheses

Use the actual zero-safe Hardy function and Xi gauge of L622:

    A(t)=(t^2+1/4) pi^(-1/4)|Gamma(1/4+it/2)|/2,
    Z(t)=-Xi(t)/A(t),
    W(t)=(Xi'(t)^2-Xi(t)Xi''(t))/A(t)^2.

Fix w>=0 in C_c^infinity((0,1)), with integral 1, and u0 in (0,1)
with w0=w(u0)>0. Let T tend to infinity, L=log T, T<=X<=2T,
a=X+u0*T, and w_XT(t)=w((t-X)/T). The inner product is
<f,q>_T=integral w_XT f conjugate(q) dt, linear in its first slot.
Fix exactly the bump

    psi(x)=exp(-1/(1-4x^2)) for |x|<1/2, and 0 otherwise,
    P=||psi||_(L2(dx)),
    g_(T,X)(t)=psi(L(t-a))/||psi(L(.-a))||_T.

For an arbitrary finite complex atomic measure on [-1,1], write

    mu=sum_(j=1)^m c_j delta_(s_j),
    U_mu(t)=sum_j c_j Z(t+s_j/L),
    C=||mu||_TV=sum_j |c_j|.

The s_j are distinct; coincident atoms can first be combined. Both their
number and their coefficients may depend on T,X. There is no amplifier,
no normalization of the Hardy atoms and no bound on the number of atoms.

The named analytic imports are:

- The real-axis Riemann--Siegel formula, Titchmarsh, revised by
  Heath-Brown, The Theory of the Riemann Zeta-Function, 2nd ed. (1986),
  Section 4.17, (4.17.4), p. 89; stated with normalization and cutoff in
  [DLMF 25.10.1--3](https://dlmf.nist.gov/25.10#E3) and independently in
  [C. Hughes, July 2017 LMS notes, Theorem 2.2, pp. 18--19](https://personal.maths.manchester.ac.uk/jm/wiki/uploads/LMS/Hughes-lectures.pdf#page=20).
  For all sufficiently large positive real v, including cutoff crossings,

      Z(v)=2 sum_(n<=floor(sqrt(v/(2pi)))) n^(-1/2)
                        cos(theta(v)-v log n)+O(v^(-1/4)).       (1)

  Only this undifferentiated real-axis remainder is used. The lecture
  proof sketch is not imported as a proof. Theta is the smooth analytic
  Hardy phase fixed in L622, compatible with the classical formula.
- Sector gamma/digamma estimates, in the specialization proved in L465
  Sections 1--2 and 5 and L622 Sections 2--4. In particular, on positive
  intervals comparable to T,

      theta'(a)=1/2 log(a/(2pi))+O(1/T),
      theta''(v)=O(1/T),    (log A)''(v)=O(1/T^2).        (2)

  The first identity follows by inserting L465 (4) into the derivative
  of L622's paired analytic gamma logarithm; the conjugate logarithms
  have sum 2 log(|1/2+ia|/(2pi)). These bounds use no logarithm of Z.
- Hughes--Young, The twisted fourth moment of the Riemann zeta function,
  J. reine angew. Math. 641 (2010), 203--236,
  [arXiv:0709.2345v2, Theorem 1.1, (11)--(17), pp. 3--5](https://arxiv.org/pdf/0709.2345v2#page=3),
  including its complete-sum holomorphy remark. L622 Sections 1--4 give
  the exact-phase/complex-weight/Cauchy application used below. The source
  manuscript and the holomorphy theorem it cites remain named imports.
- Fourier inversion and the Plancherel theorem, with angular convention
  f_hat(xi)=integral f(x) exp(-i*x*xi) dx and inverse factor 1/(2pi).

The weak atomic-duality principle is reproduced below only to preserve
the present unnormalized dictionary, complex coefficients and tolerance.
For its standard source context see Bodmann--Flinth--Kutyniok,
[Compressed Sensing for Analog Signals, arXiv:1803.04218v1, Definition 2
and Proposition 1 with proof, pp. 6--8](https://arxiv.org/pdf/1803.04218v1#page=6).
We do not invoke their normalized RKHS setup, attainment or strong duality.
The ready source comparison for this exact target is
drafts/literature/2026-11-01-hardy-translate-dual-test-scope.md.

## Conclusion

There are constants b,D,c>0 and an onset, depending only on the fixed
w,u0,psi and fixed auxiliary smooth cutoffs, such that uniformly for
T<=X<=2T a real q_(T,X) satisfies

    ||q_(T,X)||_T<=2,
    Re <g_(T,X),q_(T,X)>_T -(1/4)||q_(T,X)||_T >= b,
    sup_(|s|<=1) |<Z(.+s/L),q_(T,X)>_T|
                                  <= D T^(-1/4)/sqrt(L).       (3)

Consequently every finite approximant with ||U_mu-g_(T,X)||_T<=1/4
satisfies

    C >= c T^(1/4) sqrt(L).                                  (4)

This remains a valid lower bound on the infimum if there are no such
approximants, when that infimum is +infinity. No density is asserted.

Retain the exact six-term moment main expression M_(T,X)(mu) defined
in Section 4 below. There is a constant K_w>0 independent of m, the
coefficients, atom locations, T and X, such that

    | integral w_XT W |U_mu|^2 dt - M_(T,X)(mu) |
       <= K_w C^2 [T^(19/25) L^2 + T^(-1) L^4].                (5)

Let B_T(C)=C^2[T^(19/25)L^2+T^(-1)L^4], the scale of this sufficient
absolute-error envelope. Every approximant in (4) obeys

    B_T(C)/(T L^6) >= c^2 T^(13/50)/L^3 -> infinity.           (6)

Thus this envelope cannot certify error o(T L^6) for any such
approximant. It does NOT follow that the actual remainder is large:
(5) is an upper bound, and (6) only diagnoses using that bound.
Cancellation-sensitive estimates, a different dictionary and the actual
smaller signed signal scale are not decided here. L2 approximation alone
does not give signed |W|-weighted approximation or observer positivity.

This is a local inverse-cost estimate and a specialization of the imported
moment theorem, not a claimed result beyond all known literature. The
bounded prior search found no matching cost theorem; originality is not
certified. The separate conceptual audit below passed on 1 November 2026
under the named imports, with no changed bound or hypothesis. RH, pointwise
initial signs, all-degree mixed positivity and effective height thresholds
remain open.

## Proof

### 1. Filter, safe weight division and overlap

Choose a real even smooth chi with 0<=chi<=1, chi=1 on [-3/4,3/4]
and support contained in [-1,1]. Set

    h=F^(-1)[(1-chi) psi_hat].

Then h is real, even and Schwartz, h_hat vanishes on [-3/4,3/4], and
||h||_2<=P. Plancherel, |psi_hat|<=||psi||_1, and the length-one
support of psi give

    integral psi h
      = P^2 -(1/(2pi)) integral chi |psi_hat|^2
      >= P^2 -||psi||_1^2/pi
      >= (1-1/pi) P^2.                                      (7)

Fix delta>0 so that [u0-2delta,u0+2delta] is contained in (0,1) and
w>=w0/2 there. Choose eta in C_c^infinity((-delta,delta)), real,
0<=eta<=1, equal to 1 on [-delta/2,delta/2]. Put

    J_T=integral psi(x)^2 w(u0+x/(TL)) dx,
    q_(T,X)(t)=sqrt(L*w0)/P * eta((t-a)/T) h(L(t-a))/w_XT(t)
               on |t-a|<delta*T,
    q_(T,X)(t)=0 elsewhere.                                 (8)

Division occurs only where w_XT>=w0/2. The compact support of eta
makes extension by zero harmless; no inverse weight near a zero of w
is used. The bump norm is sqrt(J_T/L), with J_T->w0 P^2>0.
Changing variables x=L(t-a) gives

    ||q_(T,X)||_T^2
       = (w0/P^2) integral eta(x/(TL))^2 |h(x)|^2
                                      /w(u0+x/(TL)) dx
       -> ||h||_2^2/P^2 <=1,                                (9)

where the integrand is defined as zero off the cutoff support.
It is dominated by 2|h|^2/P^2. For large T, eta=1 throughout the
support of psi in this variable, so

    <g_(T,X),q_(T,X)>_T
       = sqrt(w0)/(P sqrt(J_T)) integral psi h
       -> (integral psi h)/P^2 >=1-1/pi.                    (10)

These expressions do not depend on X. Their limiting difference after
subtracting one quarter of the norm is at least

    d=3/4-1/pi>0.

Consequently (9)--(10) prove the first two parts of (3), with b=d/2,
after one onset uniform in X. No numerical overlap computation is used.

### 2. Uniform correlations, including the moving cutoff

For |s|<=1, (8) gives the exact pairing

    <Z(.+s/L),q_(T,X)>_T
       = sqrt(w0)/(P sqrt(L)) integral eta(x/(TL)) h(x)
                                      Z(a+(x+s)/L) dx.       (11)

On this cutoff support v=a+(x+s)/L lies in [T/2,4T] for large T.
Write N_y=floor(sqrt(y/(2pi))) and N0=N_a. The elementary floor bound
and the derivative of the square root imply

    |N_v-N0| <= 1+C |v-a|/sqrt(T)
              =1+C |x+s|/(L sqrt(T)).                       (12)

Every index between these cutoffs is comparable to sqrt(T), so its
coefficient n^(-1/2) is O(T^(-1/4)). Comparing (1) with its sum cut at
N0 therefore gives, uniformly even when a or v is a cutoff crossing,

    Z(v)=2 sum_(n<=N0) n^(-1/2) cos(theta(v)-v log n)
             + O(T^(-1/4)[1+|x+s|/(L sqrt(T))]).             (13)

The extra 1 in (12) is retained. No differentiability of (1)'s remainder
or of its integer cutoff is asserted.

Set lambda_n=(theta'(a)-log n)/L and phi_n=theta(a)-a log n.
By (2) and N0<=sqrt(a/(2pi)), for n<=N0,

    -C/(TL) <= lambda_n <= 1/2+O(1/L).

Thus |lambda_n|<=3/4 for all these n, beyond an X-uniform onset.
Taylor's theorem and (2), on the entire segment between a and v, give

    theta(v)-v log n
        =phi_n+lambda_n(x+s)+R(x,s),
    |R(x,s)| <= C (x+s)^2/(T L^2).                         (14)

Use |cos(y+r)-cos(y)|<=|r| for real y,r. Since
sum_(n<=N0) n^(-1/2)=O(T^(1/4)), the total error from (14), after
integration against |eta h|, is at most

    C T^(-3/4)L^(-2) integral |h(x)|(|x|+1)^2 dx.           (15)

This is valid even where the pointwise Taylor error is not small.
The integral of the error in (13) is at most

    C T^(-1/4) [||h||_1+(||x h||_1+||h||_1)/(L sqrt(T))].  (16)

The remaining linearized sums vanish with eta replaced by 1: both
orientations exp(+-i lambda_n x) pair to zero against h, by its Fourier
gap. For any integer M>=1, the error from restoring eta is bounded by

    C T^(1/4) integral_(|x|>=delta*TL/2) |h(x)| dx
      <= C_M T^(1/4)(TL)^(-M).                             (17)

For example M=2 suffices. All moments and tail constants in (15)--(17)
are finite because h is a fixed Schwartz function. Combining them bounds
the integral in (11) by O(T^(-1/4)), uniformly in X,s. This proves the
last part of (3). It uses a local linearization plus charged errors,
not a global Paley--Wiener or exact-bandlimitation claim for Z.

### 3. Finite complex weak duality

If ||U_mu-g_(T,X)||_T<=1/4, Cauchy--Schwarz and (3) give

    b <= Re <g_(T,X),q>_T -(1/4)||q||_T
       <= Re <U_mu,q>_T
       <= sum_j |c_j| |<Z(.+s_j/L),q>_T|
       <= C D T^(-1/4)/sqrt(L).

This proves (4) with c=b/D (enlarge D to be positive if necessary).
Only a finite sum is involved; arbitrary complex phases are covered by
absolute pairings. No infimum attainment or atom-count hypothesis occurs.

### 4. Complete moment main term and finite-atomic error

Here is the exact main expression retained in (5). For
q=(alpha,beta,gamma,delta), put

    R(q)=zeta(1+alpha+gamma) zeta(1+alpha+delta)
         zeta(1+beta+gamma) zeta(1+beta+delta)
         /zeta(2+alpha+beta+gamma+delta).

For ell=log(t/(2pi)), let S(t;q) be the complete sum

    R(alpha,beta,gamma,delta)
    +exp(-ell(alpha+beta+gamma+delta)) R(-gamma,-delta,-alpha,-beta)
    +exp(-ell(alpha+gamma)) R(-gamma,beta,-alpha,delta)
    +exp(-ell(alpha+delta)) R(-delta,beta,gamma,-alpha)
    +exp(-ell(beta+gamma)) R(alpha,-gamma,-beta,delta)
    +exp(-ell(beta+delta)) R(alpha,-delta,gamma,-beta).       (18)

At collisions this means its complete holomorphic continuation, never
the separate pole terms. There are no prime-power twist factors because
h=k=1. For b=(b1,b2,b3,b4), define

    q(b)=(i*b1,i*b2,-i*b3,-i*b4)/L,
    Phi(t,b)=exp(i[theta(t+b1/L)+theta(t+b2/L)
                         -theta(t+b3/L)-theta(t+b4/L)]),
    H(b)=1/(T L^4) integral w_XT(t) Phi(t,b) S(t;q(b)) dt,
    Q=partial_1 partial_2 -(partial_1^2+partial_2^2)/2,
    M_(T,X)(mu)=T L^6 Re sum_(j,k) c_j conjugate(c_k)
                                         (Q H)(0,0,s_j,s_k). (19)

All six terms and the exact phase are retained. In particular, no
phase freezing, leading logarithmic approximation or positive-kernel
substitution is hidden in (19).

L622 Sections 1--3 apply on a neighborhood of a fixed closed polydisc,
say |b_r|<=2, with h=k=1, T0=T and epsilon=1/100. The coprimality and
twist-size hypotheses are automatic; all physical shifts are O(1/L).
The weight has support in [T,3T] and all required derivative bounds.
Its complex phase extension is legitimate: L622 (7)--(8) give uniformly
bounded Phi with partial_t^j Phi=O_j(T^(-j)); splitting into four fixed
nonnegative weights supplies the source's positivity hypothesis.
Consequently the exact identity of Hardy and zeta products gives

    F(b):=integral w_XT(t) product_(r=1)^4 Z(t+b_r/L) dt
          = T L^4 H(b) + E(b),
    sup_(|b_r|<=2) |E(b)| <= C_w T^(19/25).                (20)

The exponent is 3/4+1/100. Both sides defining E are holomorphic;
the actual integral is over compact support and the complete source sum
is holomorphic by the named import. The nonholomorphic decomposition of
the weight is used only to bound E, not to differentiate its components.
There is no amplifier or coefficient norm factor in (20).

At b=(0,0,s_j,s_k), Cauchy's formula on unit circles in b1,b2
costs at most 1+1+1=3 for Q: the 2! factors cancel the halves.
The bounds are uniform also when s_j=s_k or either equals zero.
Direct differentiation of the actual product yields

    L^2 (Q F)(0,0,s_j,s_k)
      =integral w_XT (Z'^2-ZZ'') Z(t+s_j/L) Z(t+s_k/L) dt.

Multiply by c_j conjugate(c_k), sum every pair and take real parts.
The actual sum is real and equals the integral with |U_mu|^2.
The total error, before the curvature term, is therefore at most

    C_w T^(19/25)L^2 sum_(j,k)|c_j||c_k|
      =C_w C^2 T^(19/25)L^2.                              (21)

This calculation preserves all conjugate orientations and needs no
reality assumption on the coefficients. Constants are independent of m.

For completeness, the absolute shifted fourth moments needed for curvature
are uniform for |s|<=1:

    integral w_XT(t) |Z(t+s/L)|^4 dt <= C_w T L^4.          (22)

To see this without assuming X+s/L stays in [T,2T], substitute
v=t+s/L. Choose one fixed nonnegative w_plus in C_c^infinity((0,1))
dominating all w(u-e) for |e|<=e0, with e0>0 sufficiently small;
such a majorant exists since supp(w) is compact inside (0,1).
For large T, |s/(TL)|<=e0. Apply L622 Section 4's unshifted absolute
fourth-moment bound to w_plus, normalized to integral one and then
rescaled. This proves (22) with X unchanged and one fixed constant.

Weighted Holder with four fourth powers now gives, for every j,k,

    integral w_XT |Z(t)|^2 |Z(t+s_j/L)| |Z(t+s_k/L)| dt
       <= C_w T L^4.                                      (23)

The product identity in L622 Section 4 is valid at all real zeros:

    W=Z'^2-ZZ''-(log A)'' Z^2.

Using (2), expanding the finite sum and applying (23), its full omitted
curvature contribution has absolute value at most

    C T^(-2) sum_(j,k)|c_j||c_k| * C_w T L^4
      <= C_w C^2 T^(-1)L^4.                               (24)

Equations (21) and (24) prove (5). No other term was discarded. This
extends L622's coefficient accounting to arbitrary finite Hardy atoms;
it does not import a fixed two-vector Euclidean bound for that family.

### 5. What the envelope comparison does and does not show

From (4), C^2>=c^2 T^(1/2)L. The first term of B_T(C) therefore gives

    B_T(C)/(T L^6)
      >= c^2 T^(1/2+19/25-1) L^(1+2-6)
       = c^2 T^(13/50)/L^3,

which tends to infinity. Equivalently, making this particular bound
o(T L^6) would require C=o(T^(3/25)L^2), whereas the necessary cost is
at least c T^(1/4)sqrt(L); their ratio grows like T^(13/100)/L^(3/2).
The second term is nonnegative and cannot rescue this envelope.

The implication stops at the performance of the sufficient absolute
estimate. An upper bound larger than a signal says nothing by itself
about the magnitude or sign of the true error. This proof neither
prohibits approximation nor rules out a substantially sharper error
estimate exploiting coefficient cancellation. Moreover no negative
Xi interval of the stipulated width was assumed or constructed.

### Separate conceptual audit — 1 November 2026

The approved scope was the complete proof above, including its uniformity
in X and every finite complex measure. L465 Sections 1--2 and 5 and L622
Sections 1--4, including the latter's recorded conceptual audit, were
checked as the local analytic inputs. The existing source assessment was
reused. The Riemann--Siegel and Hughes--Young theorems and the latter's
complete-sum holomorphy remain named imports; their manuscript proofs
are not independently certified here. The following replay establishes
the stated local conclusions without strengthening them.

For (7), the Fourier loss is at most
2||psi||_1^2/(2pi)<=P^2/pi, since chi is supported on an interval of
length two and psi on one of length one. The multiplier 1-chi lies in
[0,1], giving ||h||_2<=P. In (9), after the change of variables the
integrand is zero outside eta's support and bounded by 2|h|^2/P^2
there. Hence dominated convergence applies even though h is not compactly
supported. The limit and J_T contain no X. With epsilon>0 small enough,
the overlap is at least 1-1/pi-epsilon and the norm at most 1+epsilon;
their tolerance difference is at least d-5epsilon/4>=d/2>0. This also
gives the norm bound 2 after one uniform onset. The local inverse weight
does not require w to be positive on its entire support.

For (13), both v and a lie in [T/2,4T], and every changed index between
N_v and N_a is comparable to sqrt(T), even if a is exactly a cutoff
height. The floor difference has an unavoidable additive one, retained
in (12). Integration therefore bounds the cutoff plus Riemann--Siegel
error by O(T^(-1/4)+T^(-3/4)/L). The gamma phase derivative gives
lambda_n>=-O(1/(TL)) and lambda_n<=1/2+O(1/L), uniformly in a.
Both signed frequencies are in the zero band of h_hat. The quadratic
phase error contributes O(T^(-3/4)/L^2), and the removed spatial tail
contributes O(T^(1/4)(TL)^(-2)). Each is bounded by O(T^(-1/4))
for large T. No small pointwise phase error, differentiated integer
cutoff, or differentiated Riemann--Siegel remainder is required. After
the exact prefactor in (11), this gives (3) for the entire continuum
|s|<=1. Finite complex weak duality then gives (4), also when the
approximation set is empty.

For (18)--(20), the six tuples and their exponential factors agree
term by term with L622's h=k=1 specialization. Multiplying the product
of the two positive-height and two negative-height zeta factors by Phi
gives exactly the four analytic Hardy factors. For clarity about open
domains, the same sector argument works for |b_r|<3 and uniformly on
its closed smaller polydiscs. There the analytic gauge is nonzero and
the compact t integral is holomorphic. The argument of the denominator
zeta factor has real part greater than one at large T, while the numerator
poles cancel only in the imported complete sum. The exact phase is
bounded and its jth t derivative is O_j(T^(-j)). Thus the four
nonnegative weight decompositions in L622 have uniform bounds on, for
example, |b_r|<=5/2. With h=k=1, T0=T and epsilon=1/100, the source
gives the raw O_w(T^(19/25)) bound on this whole closed polydisc.
The decomposition supplies bounds only; E is holomorphic as the
difference of the actual integral and the full main expression.

At each (0,0,s_j,s_k), the unit circles in b1,b2 lie strictly inside
that domain. Cauchy costs 1 for partial_1 partial_2 and 2!/2=1
for each pure second derivative, so |QE|<=3 sup|E| there. Q acting
on the actual product contributes precisely L^(-2)(Z'^2-ZZ'');
the other two Hardy factors are untouched. They are real on these
real shifts. Consequently every c_j conjugate(c_k) orientation
is retained, their actual sum is |U_mu|^2, and taking the real part
does not enlarge the error. Summing absolute errors uses exactly
sum_(j,k)|c_j||c_k|=C^2, with no constant depending on m or on
separation of the atoms. Coincident evaluation shifts cause no pole.

For curvature, let K=supp(w) be compact inside (0,1). Choose e0>0
and a fixed smooth cutoff equal to one on K+[-e0,e0], supported in
(0,1), and multiply it by ||w||_infinity. This constructs the asserted
w_plus dominating w(u-e) for every |e|<=e0. After v=t+s/L,
w_XT(t)=w((v-X)/T-s/(TL)), so the bound (22) uses the same X,
not X+s/L. Normalize w_plus for L622's fourth-moment input and
then multiply back by its fixed positive integral. Weighted Holder
uses the four exponents 4,4,4,4 for Z,Z,Z_j,Z_k and proves (23).
Direct differentiation of Xi=-AZ gives
W=Z'^2-ZZ''-(log A)''Z^2 without division by Z. L465's paired-gamma
cancellation includes the polynomial prefactor of A and gives the
needed O(T^(-2)) curvature bound on the whole support. This proves
(24), including at zeros of every multiplicity.

Finally, the powers in the comparison are
1/2+19/25-1=13/50 and 1+2-6=-3. Making this envelope o(T L^6)
requires C=o(T^(3/25)L^2); at such a cost its curvature component
is also o(T L^6). The necessary lower cost violates the first
requirement by a ratio tending to infinity. This verifies only the
failure of using the displayed absolute envelope for that purpose.
Neither (5) nor this audit supplies a lower bound on the true error,
the sign of M, approximation density, or signed weighted control.

All constants remain independent of atom count, locations, coefficients
and X. No statement, hypothesis or exponent required correction.
This is independent verification of an existing local estimate and
source specialization, not a new localization mechanism or a result
claimed beyond the checked literature. Effective constants, actual-Xi
pointwise signs and all-degree mixed positivity remain unresolved.

## Mathlib

Full matching coverage of the inverse-cost estimate, Riemann--Siegel
specialization or complete finite-atomic shifted-moment transfer was not
checked; availability is unknown. Fourier inversion/Plancherel, finite
complex sums, Holder, Cauchy--Schwarz and holomorphic Cauchy estimates
are supporting mathematics, not an identified full matching theorem.
No formal verification or numerical certificate is claimed.
