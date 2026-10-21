# Lemma 426: actual-height phase average of the covariance-free bulk

## Hypotheses

Use L425's exact comparison observable B_H^0 on [H,2H], with real
H tending to infinity, ell=log H and E=H^(-1) integral_[H,2H].
Retain L423's fixed k=13,14 mixture, mass w, normalization g_H=g0/N_H,
and actual physical matrix J(t), including response derivatives and
curvature. Use precisely L419's ordered two-stage coordinate rule,
with its equality cases and complementary rotations. Denote the
ordered output of this rule on a real symmetric matrix M by
(U_1(M),U_2(M),U_3(M)). No arbitrary Schur--Horn representative is used.

Let K be L423's positive definite matrix and P its positive square root:

    K=[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]], P=K^(1/2).

Write g0(t)=gfrak(|zeta(5/2+it)|^2), where the fixed polynomial is

    gfrak(s)=alpha[1-theta_13+theta_13 s^13/C_13]
             +(1-alpha)[1-theta_14+theta_14 s^14/C_14].       (1)

Here C_j, theta_j and alpha are exactly L423 (3)--(7), including
alpha=(B_14-T)/(B_14-B_13); none is fitted or depends on H.
For a circle point eta=C+iS define

    J_*(eta)=[[C^2/16,-CS/4,C^2/4+S^2/2],
              [-CS/4,-C^2,CS],
              [C^2/4+S^2/2,CS,C^2]],
    u_i(eta)=U_i(P J_*(eta) P).

Thus u_i uses the same coordinate/pair orders and both equality rules
as the finite-H construction. Set

    Q(a,b,d)=exp(-a^2-b^2)[b^2(1-2a^2)+ad(1-2b^2)].

Let Omega be the countable product of unit circles indexed by primes,
with product normalized Haar probability mu. For omega in Omega put
omega(n)=product_p omega_p^(v_p(n)), and define the full response

    Zcal(omega)=sum_(n>=1) n^(-5/2) omega(n).

No assumption on critical-strip zeros, critical-line phase laws,
phase independence or RH is made.

## Conclusion

The following finite, fully specified integral is the limit:

    I=integral_Omega integral_0^(2pi)
        (1/3) sum_(i=1)^3
          Q(sqrt(3 gfrak(|Zcal(omega)|^2)) P u_i(exp(i theta)))
                  dtheta/(2pi) dmu(omega),

    B_H^0=I+o(1).                                             (2)

The response in this integral is multiplicative: composite-integer
coordinates are products of the prime coordinates. The uniform angle
and prime Haar law in (2) are conclusions of actual-height averaging.
The prescribed branch choices, including ties, specify the test
everywhere; the tie fibers have limiting measure zero.

L424 and audited L425 consequently give, for the unchanged complete
L423 law,

    E_nu Q(X/sqrt(ell))=I+o(1).                               (3)

No value, sign or nonzero lower bound for I is proved. In particular
this does not reject or realize L423, establish a transport defect,
evaluate actual clipping, supply L413's full-error regulator margin,
or change a positivity/zero-exclusion range or RH status. The separate
step-186 critical audit below validates this reduction under its stated
inputs, without evaluating I.

## Proof

This is RESEARCH / REPRODUCTION / proof_attempt under the prior
SPECIALIZE assessment
`drafts/literature/2026-10-17-covariance-free-bulk-phase-averaging.md`.
We import its standard convergence and oscillatory-integral theorems;
only the exact finite-H observable specialization is proved here.
No new general equidistribution theorem or originality is claimed.

### Standard inputs and their precise domains

Import E. Kowalski, *Arithmetic Randonnee: An introduction to
probabilistic number theory*, manuscript January 19, 2021,
[Example B.6.2(1)--(2), p. 145, and Theorem B.6.3, p. 146](https://metaphor.ethz.ch/x/2021/fs/401-3109-65L/probabilistic-number-theory-fs-2021.pdf):
the continuous characters of a product of circles are exactly finite
products of integer powers of its coordinates;
on a compact abelian group, vanishing expectations of every nontrivial
continuous character characterize convergence to Haar. Its B.6.5(2)
and Example B.6.6(2), pp. 146--147, cover continuous linear orbits.
Proposition 3.2.5/Lemma 3.2.6, pp. 42--43, and the Re(s)>1 proof of
Theorem 3.2.1, pp. 43--44, supply the prime-character/Euler-log setting.
Their symmetric interval is not substituted for our dyadic interval;
the character estimates below check that change and the extra carrier.

Import T. Tao, *Lecture Notes 8 for 247B*, Winter 2007,
[Lemma 2.3 and (4), pp. 4--5](https://www.math.ucla.edu/~tao/247b.1.07w/notes8.pdf):
on an interval J, a smooth real phase with |psi'|>=b>0 and
|psi''|<=C has integral at frequency lambda>0 bounded by
O(lambda^(-1)(b^(-1)+C|J|b^(-2))). This bound includes both
endpoint terms and does not require monotonicity of psi'. We use
lambda=1 and verify both derivative bounds.

Import P. Morters and Y. Peres, *Brownian Motion*, draft May 25, 2008,
[Appendix Section 1, Theorem 1.6(v), pp. 331--333](https://www.stat.berkeley.edu/users/aldous/205B/bmbook.pdf):
weak convergence of laws on a metric space gives convergence of
expectations for any bounded measurable test whose discontinuity set
has zero limiting law. The compact countable product used below is
metrizable. We apply this theorem to one fixed test, after removing
all H-dependent observable errors; it is not applied directly to a
changing family of selectors. These inputs were read in the prior
assessment and are reused without reproof.

### Full response as a continuous, nonvanishing function

Each omega(n) is continuous on Omega. The response series is uniformly
absolutely convergent by sum n^(-5/2)=zeta(5/2), so Zcal is continuous.
The full Euler logarithm is uniformly absolutely convergent as well:

    Lcal(omega)=sum_p sum_(a>=1) omega_p^a/(a p^(5a/2)),
    sum_p sum_(a>=1) 1/(a p^(5a/2))=log zeta(5/2).

Exponentiating finite Euler products and then taking their uniform
limits gives Zcal=exp(Lcal). The identification with the Dirichlet
series follows from absolute convergence and unique factorization;
its uniform product/series tails are bounded by the corresponding
untwisted positive tails. In particular, with M=zeta(5/2),

    M^(-1)<=|Zcal(omega)|<=M                            (4)

for every omega, not just almost surely. Thus Zcal/|Zcal| is a
continuous circle-valued function. No global real argument on Omega
is selected. The polynomial gfrak is bounded above and below by
positive constants on the compact interval [M^(-2),M^2], since
0<alpha,theta_13,theta_14<1. This also verifies the fixed state-ball
bound needed for Q throughout this proof.

On the actual path omega_p=p^(-it), this full series is exactly
Z(t)=zeta(5/2+it). L368 (5)--(6) also gives the ordinary derivative
bound |Z'(t)|<=sum_n (log n)n^(-5/2)<infinity and the same uniform
positive lower bound. These justify the bounded Z'/Z used in the
actual combined-phase comparison below; no derivative of a tail
error is implicit there.

### Every joint character on the actual height interval

Use L369's actual carrier

    R(t)=exp(i phi(t)),
    phi'(t)=log(t/(2pi))/2+O(t^-2), phi''(t)=O(t^-1).

This is the phase of (t^2+1/4)Gamma(1/4+it/2)pi^(-1/4-it/2),
not the phase after multiplying by L368's polynomial b. All b and
response derivative effects remain in the physical matrix comparison
below. The displayed separate derivative estimates are L369 (6);
no derivative of an uncontrolled asymptotic error is taken.

Let mu_H be the law on G=S^1 times Omega of

    (R(t),(p^(-it))_p), t uniform on [H,2H].

The continuous characters of this compact product have the form

    chi_(m,n)(r,omega)=r^m product_p omega_p^(n_p),

where m is an integer and only finitely many integers n_p are nonzero.
This is exactly the imported product-character classification of
Kowalski Example B.6.2(1)--(2), including the countable product here;
it is not an assumption that finite-prime tests alone suffice.
Set a=sum_p n_p log p, a fixed real number. Along the actual heights,

    chi_(m,n)=exp(i[m phi(t)-a t]).

If m=0 and some n_p is nonzero, a!=0 by unique factorization
applied to product p^(n_p)=1. Exact integration yields

    |E chi_(0,n)|<=2/(H |a|) ->0.

If m!=0, the phase psi=m phi-a t has, for each fixed (m,n),

    |psi'|>=|m| log H/4, |psi''|<=C_m/H

on every sufficiently high [H,2H]. Apply Tao's quoted sharp-interval
bound with b=|m| log H/4, C=C_m/H and |J|=H. After dividing by H,

    |E chi_(m,n)|=O_(m,n)(1/(H log H)) ->0.             (5)

Negative m is allowed since the bound uses |psi'|. Both sharp
endpoints are included. No estimate uniform over a growing set of
characters, no prime/combined-phase independence, and no monotonicity
of arg(RZ) is presumed in (5). The trivial character has mean one.
Kowalski's Weyl criterion therefore gives

    mu_H -> m_circle times mu                            (6)

weakly on G as real H tends to infinity. Equivalently, it applies
along every sequence H tending to infinity, which gives the same
real-parameter limit. This is the asserted joint law, before any
discontinuous test is introduced.

### Fixed test and its complete discontinuity set bound

For (r,omega) in G set

    eta(r,omega)=r Zcal(omega)/|Zcal(omega)|,
    F(r,omega)=(1/3) sum_i
       Q(sqrt(3 gfrak(|Zcal(omega)|^2)) P u_i(eta(r,omega))).

The coordinate construction is Borel, including ties, so F is Borel.
Its states lie in the fixed ball from (4), hence F is bounded.
We must check continuity off a null set, rather than infer it from
Borel dependence or the existence part of Schur--Horn.

For a real symmetric matrix N put D_i(N)=N_ii-tr(N)/3. L425 proves
for the exact P and J_* above that

    F_i(theta)=D_i(P J_*(exp(i theta)) P)
               =A_i cos^2(theta)+B_i sin^2(theta),

and each F_i is nonzero as a function. More explicitly, with
d=1/(6sqrt(5)) and D^2=81/80+2d, its sin^2 coefficients are

    B_1=-(159/80+d)/(36D^2), B_2=1/36,
    B_3=(39/40-d)/(36D^2),

all nonzero. Thus the union T of their zero sets modulo 2pi is
finite. Away from T every original diagonal gap is strict. L425's
analysis of the prescribed first rotation proves continuity there.
For the second rotation the unused original coordinate k has gap
D_k; the other complementary coordinate has gap -D_k because
the complementary trace is twice the trace average. Thus that stage
is also strict and continuous away from T. A vanishing off-diagonal
does not cause a singular rotation root on these strict branches.
This rules out an unaccounted complementary discontinuity locus.
The fixed pair orders cannot change within a strict gap-sign region.

Since Zcal, eta and gfrak are continuous, F is continuous outside

    A={(r,omega): eta(r,omega) in exp(i T)}.

For each fixed omega, the fiber of A in r is a rotation of a finite
set, so its circle Haar measure is zero. A is measurable (indeed
closed), and Fubini gives (m_circle times mu)(A)=0. This concerns
the combined phase, not a tie condition in r alone. Apply the quoted
Morters--Peres theorem to (6) and the fixed F to obtain

    E F(R(t),(p^(-it))_p) -> integral_G F.               (7)

For each fixed omega, the change of variable
r -> r Zcal(omega)/|Zcal(omega)| preserves circle Haar measure.
Fubini is allowed by boundedness. It turns integral_G F into exactly
I in (2), without selecting a real argument of Zcal or changing any
branch rule. Only the phase coordinate is integrated out; the full
multiplicative response modulus remains in gfrak.

### Comparison with the exact finite-H observable

Let u_i^0(t) be L425's exact selected basis for S_0 J S_0, where
S_0=sqrt(ell g_H)P. Positive scalar invariance of both stages of
L419's rule, including equality, gives the exact identity

    u_i^0(t)=U_i(P J(t) P),
    V_i^0(t)=sqrt(3 g_H(t)) P u_i^0(t).                 (8)

From L423, 0<=w<=1, E(1-w)=O(ell^-5/2), and
N_H=1+O(H^-1+ell^-5/2). Since g0 is uniformly bounded above and
below, sup_t |g_H-g0|=O(H^-1+ell^-5/2). On the fixed state ball
Q has bounded first derivatives, and sqrt is Lipschitz on this
positive scalar range. We may therefore remove w and replace g_H
by g0 in the observable while retaining u_i^0, with total error
O(H^-1+ell^-5/2). This uses E(1-w), never pointwise smallness of
1-w or a derivative bound on w.

It remains to replace this exact-J selector by the leading selector.
The complete physical expansion L390 (4)--(5), checked in L425 (3), is

    J(t)=c^2 rho(t)^2 J_*(exp(i theta(t)))+O(ell^-1),
    c=1/(4pi), rho=|zeta(5/2+it)|,
    exp(i theta(t))=R(t) zeta(5/2+it)/rho(t).           (9)

The error is uniform in operator norm and retains all ordinary
response derivatives and curvature, including at real projection
zeros. The annulus (4) applies to actual heights too. A smooth lift
theta exists on the eventual real ray; it is used only for the
actual-height exceptional-set estimate, not on the prime torus.

Fix delta>0 and set
E_delta={theta mod 2pi: min_i |F_i(theta)|<=delta}, with length
epsilon_delta ->0 as delta decreases to zero. L425 (7)--(8), using
theta'=phi'+Im(Z'/Z)=log(t/(2pi))/2+O(1), proves

    E 1_(theta(t) in E_delta)<=C epsilon_delta

for all sufficiently large H, with C independent of delta. This
is an actual-height estimate using the full response, not (6) applied
prematurely to an H-dependent function.

Off this set, all gaps of c^2 rho^2 P J_* P are at least
c^2 M^(-2)delta in absolute value. The bounded-matrix error in
PJP from (9) tends uniformly to zero, so the gap signs agree for
large H depending on delta. The two-stage compact-branch continuity
proved in L425 gives

    max_i |u_i^0(t)-u_i(exp(i theta(t)))|=o_delta(1)

uniformly there. Positive scalar invariance removes c^2 rho^2
without any amplitude approximation. All states stay in the same
fixed ball, including the exceptional fibers. Boundedness and uniform
continuity of Q now give, with constants independent of delta,

    |B_H^0-E F(R(t),(p^(-it))_p)|
          <=o_delta(1)+C_Q epsilon_delta
                        +O(H^-1+ell^-5/2).             (10)

First take limsup as real H tends to infinity at fixed delta, then
let delta decrease to zero. This proves that (10) tends to zero.
Together with (7) and its Haar change of variable it proves (2).
Every equality fiber has been bounded, not redefined; no shrinking
tie tolerance has been inserted before its uniformity was checked.
No response truncation or infinite-Fourier/height interchange is used.

Finally audited L425 gives B_H-B_H^0=o(1), and L424 gives
E_nu Q(X/sqrt(ell))=B_H+O(ell^-1) with the original high and
intermediate components and bounded translation retained. This
proves (3). The constant I is still unevaluated; even I=0 would
establish only passage of this one necessary transport test, not
global trajectory realization. A nonzero I would need its own
rigorous evaluation before any incompatibility claim. Neither case
alone repairs the independent actual-theta or regulator gaps.

### Separate critical audit — 2026-10-17, step 186

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-17-bulk-phase-averaging-critical-audit.md`.
The audit found no mathematical defect in (2)--(10). The product-character
reference above is made explicit using the already inspected source;
its classification is imported rather than reproved. This is a local
reliability result, not an integral evaluation or a discovery beyond the
sources checked. L425's separate audit is reused for its branch and
covariance comparisons, with the new applications checked below.

**The whole compact group and both character cases.** Enumerate the
primes as p_j. The usual circle distance on the carrier, plus the sum
of 2^(-j) times the bounded circle distances on prime coordinates,
metrizes G with its compact product topology. Thus its Borel probability
laws have the metric-space setting required by the quoted weak-convergence
theorem. Kowalski's product classification applies to every continuous
character, including arbitrary negative integer exponents. For m=0,
a=0 would imply equality of the two integers formed from the positive
and negative prime exponents. Unique factorization makes all exponents
zero. Otherwise direct sharp integration costs at most 2/|a| before
division by H. For m nonzero, L369 (6) is for precisely R=Q/A,
and gives on [H,2H]

    psi'=m log(t/(2pi))/2-a+O_m(H^-2),
    psi''=O_m(H^-1).

For each fixed character the first has magnitude at least
|m| log H/4 eventually. Tao's two-derivative bound is therefore
O_(m,n)((log H)^(-1)+(log H)^(-2)) before normalization.
The second summand comes from |J| sup|psi''|/b^2; it is not
discarded on an unsupported monotonicity claim. This proves (5),
with both endpoints and either sign of m. The trivial character has
mean exactly one. Weyl applies along every sequence of real H tending
to infinity, which suffices for (6). No simultaneous growing-character
estimate or independence assumption has entered.

**Full response and the fixed test.** On Omega the absolute majorants
for the series and Euler logarithm are respectively M and log M.
Finite Euler expansion, unique factorization and these convergent
majorants identify exp(Lcal) with the full multiplicative series.
In particular Re Lcal>=-log M gives the lower bound in (4), even
on exceptional prime configurations. The same function restricted to
the actual path is exactly zeta(5/2+it). This validates the continuous
circle-valued quotient used in eta; no global real phase is required.

L423's coefficients in (1) are fixed: both theta_j are in (0,1),
and alpha=(B_14-T)/(B_14-B_13) is in (0,1). The strict bounds
R_13,R_14>S>C_1 and B_13<T<B_14 used here are the audited inputs
of L423, not fitted values. Hence gfrak has a fixed positive minimum
and finite maximum on [M^-2,M^2]. Since P is fixed and each selected
vector has unit length, all arguments of Q lie in one compact ball.
Q need not be globally bounded on R^3: boundedness of this composed
test, and of the finite-H comparison states, is what is used.

The literal rule is Borel at all first-stage and complementary
equalities. On a strict first-stage low/high pair its positive root
has denominator M_jj-tau>0 and radicand
M_ij^2+(M_jj-tau)(tau-M_ii)>0. On a gap-bounded compact set both
are uniformly separated from zero. In the prescribed complement
(rotated companion,e_k), the gaps are (-D_k,D_k); so neither second
stage equality can occur when the original three gaps are nonzero.
The low/high order is fixed by the sign of D_k. Both labeled rotations
are continuous on each such sign region, even if an off-diagonal
entry vanishes. No eigenvector continuity or free basis change is used.

The explicit P in L425 has no mixing between coordinate 2 and the
outer block. Thus each diagonal gap of P J_* P has only cos^2 and
sin^2 terms. At theta=pi/2 the trace is -1/12, and subtraction of
its mean gives exactly the three B_i displayed above. Their nonzero
values ensure a finite zero set for each gap, regardless of root
multiplicity. All possible discontinuities of F are consequently
inside the closed combined-phase set A. For each omega its carrier
fiber is a rotation of that finite set, so Fubini makes A product-Haar
null. Morters--Peres now applies to the one fixed bounded Borel F.
The following fiberwise Haar rotation produces the stated I while
leaving gfrak(|Zcal|^2) and every branch choice intact. It does not
replace composite phases by independent coordinates.

**Physical comparison, normalization and sequential limits.** The
leading response triple from L390 is (ca,-ch/2,-ca/4), with each
complete derivative error O(1/L). Substituting it in the exact
quadratic form gives diagonal coefficients C^2/16,-C^2,C^2 and
cross coefficients -CS/2,C^2/2+S^2,2CS after division by c^2 rho^2.
These are precisely the entries of J_* after halving cross terms.
Polynomial dependence on bounded response coordinates bounds the
operator error by O(1/L); exact curvature contributes
O(1/(t^2 L^2)). Thus (9) holds uniformly, including projection zeros,
with L=log(2+t)>=ell. This verifies that the carrier is Q/A and
that b and response derivatives have not been lost.

Since S_0=sqrt(ell g_H)P, its matrix S_0 J S_0 is the positive
scalar ell g_H times PJP. Both selection stages, including equality
rules, are invariant under that scalar: the trace comparisons scale
and the root's numerator and denominator scale equally. This proves
(8), with V_i^0 normalized by sqrt(ell), not sqrt(L(t)). L423 gives
E(1-w)=O(ell^-5/2) and N_H=1+O(H^-1+ell^-5/2). Bounded g0 and
N_H bounded away from zero give the asserted uniform g_H-g0 error.
On the fixed positive scalar range the square-root map is Lipschitz,
and Q has bounded derivatives on the state ball. Removing w costs
at most a fixed bound for |Q| times E(1-w); no pointwise estimate
of 1-w or independence from the basis is required.

For each fixed delta>0, all good leading gaps have magnitude at
least c^2 M^-2 delta. The operator error just checked preserves
their signs eventually and bounds the exact gaps below by half this
quantity. L425's compact-branch moduli then apply to both labeled
stages. Their constants may depend on delta; no uniform rate in
delta is asserted. On bad heights L368's full |Z'| and lower |Z|
bounds give theta'=phi'+Im(Z'/Z), bounded above and below by fixed
positive multiples of ell. The periodic-set change of variable in
L425 (8) therefore bounds bad-height probability by C epsilon_delta,
with C independent of delta. The bound for Q on the whole state
ball is also independent of delta. Taking limsup in H first, then
delta decreasing to zero, proves (10) tends to zero. Equality fibers
are bounded in this estimate, not silently assigned new vectors.

Finally audited L425 deletes the entire covariance correction only
at the observable level, with o(1) error. Audited L424 retains the
high and intermediate components and the paired bounded translation,
giving B_H+O(ell^-1) at exactly X/sqrt(ell). These are sequential
comparisons of the same complete L423 law, so they prove (3) without
asserting that the comparison states still meet its moment constraints.
The integral's value and sign remain unknown. The step-175 numerical
screen is not evidence for either, and was not rerun. No actual
realization, clipping result, regulator margin or RH consequence is
established by this audit.

### Bounded enclosure, inconclusive — 2026-10-17, step 188

Under the same hypotheses and the additional implementation contract of
correct Python integer, Fraction and `isqrt` execution, the finite range
calculation gives

    -301/1000 <= I <= 207/1000.                            (11)

This interval contains zero. It supplies no value, sign, nonvanishing,
transport incompatibility or RH conclusion. It is a REPRODUCTION /
calculation under the unchanged prior SPECIALIZE assessment
`drafts/literature/2026-10-17-bulk-haar-integral-enclosure.md`.
The earlier step-186 audit concerns (2)--(10), not this new computation.

The standard imported method is S. M. Rump, *Verification methods:
Rigorous results using floating-point arithmetic*, Acta Numerica **19**
(2010), 287--449, corrected author PDF,
[Section 5.5, (5.16)--(5.17), internal pp. 27--28](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf):
the inclusion property for successive valid interval operations. Here
integer fixed-point endpoints implement that property directly, rather
than relying on a new general integration theorem. Finite probability
cell ranges bound their integral by monotonicity. The arithmetic details
below justify the particular elementary-function callbacks and domain
cover; these details are necessary for this implementation.

**Exact coefficients and the entire response.** Read the audited bounds
in `scripts/discriminant/response-modulus-second-moment-certificate.json`.
Evaluate the literal formulas for theta_13, theta_14 and alpha from
L423 (3)--(7) by outward interval operations. Every divisor has a
strictly positive lower endpoint; all three parameters lie in (0,1).
The source's Euler tails are inherited, not independently recertified.
The full coefficient endpoints and the resulting intervals are copied
into the new certificate. Repeated occurrences may overestimate, but
the exact same coefficients always lie in the evaluated ranges.

Use prime coordinates 2,3,5, with q_p=p^(-5/2). Their squared-modulus
head is product_(p=2,3,5)(1-2q_p cos(t_p)+q_p^2)^(-1).
The omitted Euler logarithm has absolute value at most the positive
constant t bounded by

    t <= sum_(7<=p<=200) q_p/(1-q_p)
       + [2/(3*200^(3/2))]/[1-201^(-5/2)] < 1.           (12)

The finite sum is over every prime in that interval. For each prime,
sum_(a>=1) q_p^a/a <= q_p/(1-q_p); for larger primes, enlarge to
all integers above 200, use the decreasing-integrand bound for
sum n^(-5/2), and bound each denominator by 1-201^(-5/2).
Thus (12) retains every omitted prime and prime power, uniformly over
all of their phases. If t_+ is the computed upper endpoint, the
omitted squared-modulus factor lies in

    [(1-t_+)^2, (1-t_+)^(-2)],

since exp(-t_+)>=1-t_+ and exp(t_+)<=1/(1-t_+).
Multiply the head range by this full interval before evaluating the
degree-13/14 mixture, square roots and Q. No small-tail linearization
or replacement of composite coordinates by independent phases occurs.

**Cells and both branch stages.** The modulus depends on each retained
prime angle only through its cosine. Reflection therefore permits four
equal intervals on [0,pi] for each, each of probability 1/4. Independently
partition the selector angle into 512 equal intervals on [0,2pi].
There are exactly 4^3*512=32768 product cells, each of mass 1/32768;
shared endpoints have measure zero. This use of an independent selector
angle is precisely the change of variables already proved in (2).

On an angle interval enclose P J_* P, its mean diagonal tau and all
three original gaps. If every gap has a strict sign, retain the literal
lexicographic low/high pair and L419's positive rotation root, with its
ordered companion and unused coordinate. For numerical stability the
same root can be written low/(sqrt(off^2+high*low)+off) when off>=0.
The complementary restriction is computed with all entries retained,
but its gaps are enclosed using L425's exact identity (-D_k,D_k),
where k is the unused original coordinate. Its positive root and
coordinate order are then evaluated in exactly the same way. This
identity, rather than a fresh interval trace subtraction, is essential
to reduce dependency. Intersecting vector coordinates with [-1,1] and
coordinates of P u with [-sqrt(K_jj),sqrt(K_jj)] is legitimate because
the actual selected vectors are unit vectors. All these intersections
are checked nonempty.

Any uncertified branch or denominator receives the full state range,
including both equality conventions. For an actual selected state
sqrt(3g)P u, |d|<=sqrt(3g/80), so

    |Q| <= (1+sqrt(3g/80))/2.                            (13)

Indeed for x>=0, |1-2x|exp(-x)<=1,
x exp(-x)<=1/2 and sqrt(x)exp(-x)<=1/2. Differentiation locates
the respective interior extrema at 3/2, 1 and 1/2; their bounds follow
from exp(3/2)>2 and exp(1)>2, with the endpoints included.
Apply these to a^2,b^2 in Q. Thus no positive-width tie cell is dropped.
On certified cells evaluate all three Q ranges and average them,
intersecting each with (13). The full response tail and all coefficient
uncertainty remain inside every such range, including (13).

**Elementary enclosures and aggregation.** Every endpoint is an integer
multiple of 10^(-24). Addition and subtraction are exact at that scale;
products use floor/ceiling of the four endpoint products, division uses
the positive reciprocal interval, and square root uses floor/ceiling
integer square roots of the scaled endpoints. Squares use their true
interval range, including zero if appropriate. L037's proved Machin
identity and alternating arctangent remainder give a rational pi
interval using 48 terms. Sin/cos are evaluated at an enclosed rational
midpoint using 48 Taylor updates; for arguments in [0,7] their error
is bounded by 7^97/97!, enlarged by the argument radius using the
unit derivative bound. The sine polynomial has one extra term; its
remainder is smaller than this bound. All angle arguments are checked
to lie in [0,7].

For exp(-x), x>=0, reduce the endpoint argument by an exact power
of two to at most 1/8, use the degree-18 exponential Taylor polynomial
with error at most 1/(8^19*19!), then square the resulting nonnegative
interval the required number of times. Monotonicity supplies the
endpoints for interval x. Each operation rounds outward; no binary
floating input, numerical comparison or post-hoc decimal wrapping
is part of the proof. The general known inclusion method is thereby
specialized to the complete observable.

Reproduction command:

    python3 scripts/discriminant/enclose_bulk_haar_integral.py

The complete certificate is
`scripts/discriminant/bulk-haar-integral-enclosure-188.json`.
It stores every product-cell range, every selector-vector interval or
fallback reason, all coefficient bounds, response ranges and tails.
Its exact aggregate is

    [-150389321869866202429577/500000000000000000000000,
       103133517733522630906603/500000000000000000000000].

These endpoints imply (11). All 32768 distinct cell records were checked for
coverage, ordered finite endpoints and exact rational aggregation
inside this outward aggregate. All certificate checks pass. Its
reported failure is the unmet target: this aggregate contains zero.

There are 24 uncertified selector intervals, of total mass 3/64.
Their full contribution is enclosed symmetrically by
941365329859063440501/31250000000000000000000, approximately
0.030124. The other 31232 product cells have strict-stage ranges whose
total width is approximately 0.446799. These are joint observable
budgets, retaining the full log-tail bound (approximately 0.015136),
coefficient ranges and cell variation. They are not additive estimates
attributing the same interval width separately to each source.
The achieved full width is approximately 0.507046, against the required
zero-excluding interval. Stop this uniform capped mesh; finer or adaptive
methods have not been shown either sufficient or impossible. No source
claim, proof of nonvanishing or new general mathematical result is made.

### Adaptive enclosure, still inconclusive — 2026-10-17, step 189

Under the same hypotheses and integer/Fraction/`isqrt` implementation
contract as (11), one adaptive refinement proves the stronger bound

    -223/1000 <= I <= 138/1000.                            (14)

This is a local quantitative improvement, not a sign or nonvanishing
result. It is RESEARCH / REPRODUCTION / calculation under the unchanged
prior SPECIALIZE assessment
`drafts/literature/2026-10-17-bulk-haar-integral-enclosure.md`.
The method imports precisely the interval inclusion principle cited
above; no new general integration theorem is asserted. The difference
from the known method is its finite specialization to this integral.

**Inputs and finite partition proof.** Retain every exact coefficient,
the same prime coordinates 2,3,5, the complete tail (12), the state bound
(13), and both literal branch stages. Read, without changing, the full
step-188 certificate. Its coefficient records must agree exactly with
the output of `source_coefficients`; its tail factor must agree with
the displayed factor constructed from its full log-tail interval.
Check all 32768 initial records for ordered endpoints and distinct
valid Cartesian indices. These records exhaust the initial grid by
cardinality. Sum their exact endpoint contributions as Fractions and
check that this sum lies inside the earlier outward aggregate. The
initial response and selector caches are those already justified above.
No earlier sampling certificate is used.

Represent a cell by four pairs (a_j,n_j), j=0,1,2,3. The first three
denote the normalized prime-angle intervals [a_j/n_j,(a_j+1)/n_j]
in [0,pi], and the last denotes the normalized selector-angle interval
in [0,2pi]. Its exact probability is m=1/product_j n_j. Bisecting
coordinate j replaces (a_j,n_j) by (2a_j,2n_j) and (2a_j+1,2n_j).
Their interiors are disjoint and their union is the parent. All shared
boundaries have zero product measure. Consequently any finite sequence
of these replacements preserves a complete probability-one partition;
this is the only integration argument needed beyond inclusion and
monotonicity.

On each new response cell recompute the three finite Euler factors
with interval cosines, multiply by the unchanged full tail factor,
and evaluate the exact fixed polynomial gfrak with its coefficient
intervals. Every g lower endpoint is checked positive. On each new
selector cell use the existing `selector(a_3,n_3)` callback: its original
and complementary branches, exact gaps (-D_k,D_k), square roots,
coordinate intersections and fallback are precisely those justified
for (11)--(13). A failed branch certificate again uses the complete
state bound; no tie neighborhood is omitted. Average the three Q
ranges when both stages are certified. If R is the parent range and
R_child is this new direct range, use R intersect R_child. Both contain
the integrand on the child, so the intersection remains valid even
when their interval dependencies differ. Every intersection is checked
nonempty. Thus coefficient uncertainty and the entire omitted response
remain inside all retained ranges, rather than being added as an
unjustified small final error.

**Bounded adaptive choice and complete evidence.** The work note
`drafts/2026-10-17-bulk-haar-adaptive-enclosure-189.md` declared a cap
of 65536 final cells and 262144 candidate-child evaluations, and a
material-narrowing threshold of at most 3/4 of the initial exact width.
Select a cell with greatest exact m times range width. Compare its
four coordinate bisections (eight child evaluations), choose the one
with least summed child width, and prefer the larger coordinate index
on a tie. The selector is therefore preferred on an exact tie. These
choices affect efficiency only; the partition and inclusion proof
applies to any of them. Every priority and comparison uses rational
or integer arithmetic, with no sampled integrand values.

There are 32768 chosen bisections and exactly 262144 candidate-child
evaluations. Counts by prime-2, prime-3, prime-5 and selector coordinate
are respectively 13120, 10676, 3992 and 4980. The resulting 65536
leaf records, every chosen split and parent/child range, and all cached
response and selector intervals are saved. Replay every chosen split
from the original grid and check that the terminal keys and ranges
equal the saved leaves, their masses sum to one, and exact rational
endpoint sums equal the maintained aggregate. All these checks pass.
The certificate also checks that both declared caps were respected.
Correct execution of the stated arithmetic remains an explicit
contract; neither this replay nor a structure checker is formal
verification of the interval implementation.

Reproduction command:

    python3 scripts/discriminant/enclose_bulk_haar_adaptive.py

Full certificate:
`scripts/discriminant/bulk-haar-adaptive-enclosure-189.json`.
The exact resulting interval is

    [-58230540666534131227229282207/262144000000000000000000000000,
      35987133774012347045611265993/262144000000000000000000000000].

Direct rational comparison gives (14). Its exact width is

    471088372202732391364202741/1310720000000000000000000000,

and its ratio to the initial exact width is

    11777209305068309784105068525/16614872816247690580431891918
      < 71/100 < 3/4.

Thus the declared material-narrowing test passes. The achieved width
is approximately 0.359412, a reduction of about 29.1 percent. Leaves
with an unresolved selector have total probability 141/8192; their
aggregate is exactly the symmetric interval with radius

    342152213572390465982353763/32768000000000000000000000000.

Their width is approximately 0.0208833. The strict leaves contribute
approximately 0.338529 in width. As before these are joint observable
budgets including the same full log-tail (approximately 0.015136),
coefficient uncertainty and cell variation; they are not independent
error allocations. All exact `/integral`, `/checks`, strict and
unresolved contribution fields, and `/failures` were inspected. The
recorded failure is substantive: the final interval contains zero.
No nonzero value, sign, law incompatibility, actual realization,
clipping estimate, regulator margin, positivity or RH conclusion
follows. The old uniform-mesh and sampling stops remain valid for
their respective implementations. This finite narrowing does not
establish that further refinement will exclude zero.

### Resumed adaptive enclosure and stop — 2026-10-17, step 190

Under precisely the same hypotheses and integer/Fraction/`isqrt`
implementation contract as (11)--(14), resuming the saved partition gives

    -194/1000 <= I <= 114/1000.                            (15)

This narrower local enclosure still contains zero. The completed task is
RESEARCH / REPRODUCTION / calculation under the unchanged prior SPECIALIZE
assessment `drafts/literature/2026-10-17-bulk-haar-integral-enclosure.md`.
It imports the same standard interval inclusion principle of Rump,
Section 5.5, (5.16)--(5.17), cited above; no new integration theorem,
novelty, nonvanishing or sign is asserted. Its substantive route outcome
is NEGATIVE: it misses the predeclared material-narrowing test.

**Source verification and resumed inclusion proof.** The script reads
the complete step-189 certificate, checks its SHA-256 link to step 188,
and compares both coefficient records with `source_coefficients`.
It checks that the full logarithmic tail and squared-modulus factor
are unchanged, including the factor formula following (12). The original
32768 distinct valid grid indices exhaust the probability-one Cartesian
partition. Their exact sum is checked against both step 188's outward
aggregate and step 189's initial exact aggregate. Every one of step 189's
32768 splits is replayed, checking its parent range, dyadic children,
mass identity and nested child ranges. The resulting keys and ranges
must equal all 65536 saved leaves; their exact masses sum to one and
endpoint sums equal the saved final interval. This verifies the starting
partition and aggregation, while inheriting the earlier arithmetic
callback proof and coefficient-tail contract rather than claiming a new
independent verification of them.

From those leaves use exactly the four-coordinate bisection and parent
intersection procedure justified for (14). New response cells use all
three Euler factors and the entire factor (12); selector cells use both
literal ordered stages, exact gaps (-D_k,D_k), positive denominators and
the complete fallback (13). All coefficient uncertainty remains inside
every range. A parent range and a direct child range both contain the
integrand on the child, so their checked nonempty intersection does too.
Dyadic children partition their parent up to null boundaries, with half
its mass. Induction therefore proves full domain coverage and validity
of all terminal range integrals. Priority by exact mass times width,
comparison of the four candidate bisections and the same tie convention
affect efficiency only, not this inclusion argument.

The work note `drafts/2026-10-17-bulk-haar-resumed-enclosure-190.md`
declared caps of 131072 final leaves and 524288 additional candidate-child
evaluations, and required zero exclusion or width at most 3/4 of the
step-189 width. The script performs 65536 further bisections and exactly
524288 candidate-child evaluations, meeting both caps. Coordinate split
counts are 27794, 16664, 8700 and 12378. It replays every new split from
the verified starting partition, compares every final key and range,
and recomputes mass one and both endpoint sums exactly. All checks pass.
This is a finite arithmetic certificate under the stated execution
contract, not a formal verification of the implementation.

Reproduction command:

    python3 scripts/discriminant/enclose_bulk_haar_resume.py

Full certificate: `scripts/discriminant/bulk-haar-resumed-enclosure-190.json`.
Its exact interval, inspected in full, is

    [-101217211031374483466663453041/524288000000000000000000000000,
      119123797085335438353523839137/1048576000000000000000000000000].

Rational comparison gives (15). The exact width is

    321558219148084405286850745219/1048576000000000000000000000000,

and its ratio to the step-189 width is

    321558219148084405286850745219/376870697762185913091362192800,
    85/100 < ratio < 86/100, hence ratio > 3/4.

The width is approximately 0.306662, a reduction of about 14.7 percent.
The strict-cell contribution is exactly

    [-96380781956261200142651681933/524288000000000000000000000000,
      109450938935108871705500296921/1048576000000000000000000000000],

of width approximately 0.288212. Unresolved-selector leaves have mass
4039/262144 and symmetric contribution of radius

    1209107268778320831002942777/131072000000000000000000000000,

of width approximately 0.0184495. These contributions sum exactly to the
full interval. They include the unchanged full log-tail of approximately
0.015136, coefficient uncertainty and cell variation jointly; no separate
coefficient or tail floor has been measured. Complete relevant aggregate,
checks and failure fields were inspected, not inferred from previews.
Both substantive failures remain: zero is contained and the 3/4 width
threshold fails. Stop further direct adaptive subdivision of this
implementation. This measured failure is not a lower bound on all
possible integration methods or a proof that I vanishes. The sampling
and uniform-mesh stops remain intact. No law incompatibility, actual
realization, clipping, regulator margin, positivity or RH result follows.

### Angular polynomial envelopes and failed expectation test — 2026-10-17, step 192

This RESEARCH / REPRODUCTION / calculation uses the unchanged prior
SPECIALIZE assessment
`drafts/literature/2026-10-17-bulk-haar-angular-polynomial-envelopes.md`.
It constructs uniform degree-32 polynomial envelopes for the same A(g)
and evaluates certified intervals for their full prime-Haar expectations.
The resulting enclosure is only

    -2625/1000 < I < 2616/1000.                            (16)

It contains zero and is weaker than (15), which remains the retained
bound. The predeclared width test fails. This stops this interpolation,
angular-range and independent-moment-interval implementation; it is not
a lower bound on the best polynomial error, a proof of I=0, or a stop
on every polynomial or angular method. There is no new RH conclusion.

**Entire continuation and uniform remainder.** Write v=P u=(x,y,z).
For real g>=0 direct substitution in Q gives

    Q(sqrt(3g)v)=exp(-t g)(b g+c g^2),
    t=3(x^2+y^2), b=3(y^2+xz),
    c=-18y^2(x^2+xz).                                    (17)

The right side defines an entire function of complex g without any
square-root choice. The selector and these coefficients depend only
on angle, never on g. Unit length of u and the diagonal of K give

    0<=t<=13/4,
    |b|<=1/4+3/sqrt(80),
    |c|<=(3/2)(1+1/sqrt(80)).                            (18)

On every compact complex g set, the exponential series in (17),
including multiplication by its degree-two polynomial, converges
uniformly in angle and state by (18). Its bounded measurable
coefficients are integrable. Termwise integration of that uniformly
absolutely convergent power series proves that A has an entire
continuation. This also supplies the domination needed for derivatives;
no angle derivative across a selector tie is taken. This elementary
specialization is necessary because analyticity of an ordinary fit
would not justify the interpolation theorem.

Use the exact rational endpoints a,b_g of `/g_full_range` in
`scripts/discriminant/bulk-haar-integral-enclosure-188.json`, displayed
in the prior assessment. Let m=(a+b_g)/2 and h=(b_g-a)/2. On the
Bernstein ellipse with parameter rho>1 in the coordinate (g-m)/h,
put r=(rho+rho^-1)/2. Then

    |g|<=G=m+hr, Re(g)>=q=m-hr.

For any state whose t,|b|,|c| are enclosed by t in [t_-,t_+], B,C,
a valid whole-ellipse modulus bound is

    M=(B G+C G^2) exp(max(0,-q)t_+).                     (19)

When q>=0 the exponential is bounded by one since t>=0. When q<0
the expression in (19) follows from |exp(-tg)|=exp(-t Re g).
All tested ellipses and their interiors therefore satisfy the analytic
and modulus hypotheses, not just boundary sampling hypotheses.

Import L. N. Trefethen, *Approximation Theory and Approximation Practice*
(SIAM, 2013), Theorems 8.1--8.2, using the inspected
[author Chapter 8 source](https://raw.githubusercontent.com/chebfun/ATAP/master/chap8.m):
Theorem 8.1 bounds Chebyshev coefficients by 2M rho^-k, and
Theorem 8.2 bounds the interpolation error by the doubled coefficient
tail. The source's endpoint-node convention is not silently changed.
Here N=d+1 and the nodes are theta_k=(2k+1)pi/(2N). For every integer
l>=N, reducing l modulo 2N and reflecting about N shows that its
node cosine vector is either zero (residue N) or plus/minus that of
some T_j, 0<=j<N: cos((2Nq+l)theta_k)=(-1)^q cos(l theta_k), and
cos((2N-j)theta_k)=-cos(j theta_k). Therefore the root-node
interpolant of T_l has norm at most one. Both T_l and its interpolant
are bounded by one on [-1,1]. Summing the uniformly convergent
Chebyshev series gives an error at most
2 sum_(l>=N) 2M rho^-l=4M rho^-d/(rho-1).
This finite-node aliasing specialization is needed for the different
node convention; the analytic coefficient theorem is imported, not
reproved. Apply this bound to each state function (17).
The interpolating nodes depend on d, not
rho; consequently the best of the finitely tested rho bounds may be
chosen separately for each angular cell and state, then integrated.
Linearity of interpolation in its node values makes the integral of
these interpolants exactly the interpolant p_d of A. The triangle
inequality thus gives a uniform real bound

    p_d(g)-R_d <= A(g) <= p_d(g)+R_d, a<=g<=b_g.          (20)

**Every angular branch and numerical obligation.** First partition
the angle into 1024 equal cells. Both literal L419 rotations are
enclosed by the existing selector callback, using L425's exact
complementary gaps (-D_k,D_k), including all denominator/radicand
checks. Split each of the 28 unresolved cells into 16 children.
This leaves 1444 terminal cells, with exact masses 1/1024 or 1/16384;
they partition the circle up to null endpoints. There are still 28
unresolved terminal cells. Every such cell uses (18) for all three
states in the remainder calculation and the full bound (13) at
interpolation nodes. No finite neighborhood of a tie is omitted and
no equality state is reassigned.

Test rho=101/100,...,180/100 at d=8,16,32. All modulus exponentials
are bounded by the outward integer arithmetic and `exp_negative`
routine already justified for (11)--(13); positive exponentials use
reciprocals of strictly positive enclosures. The exact rational radii
and all cell/state bounds are retained in
`scripts/discriminant/bulk-haar-polynomial-preflight-192.json`.
For d=32 the statewise radius is less than 362/10000, with strict-cell
radius about .0281061 and unresolved-cell radius about .00806216.
The complete radius is about .03616825. Degrees 8 and 16 have
symmetric widths about 1579.59 and 113.250 under these same budgets,
so only degree 32 passes the remainder preflight. These are chosen
certified upper error budgets, not measured lower approximation errors.
The preserved initial uniform partition certificate is
`scripts/discriminant/bulk-haar-polynomial-preflight-192-initial.json`.

Use the exact ideal nodes x_k=cos((2k+1)pi/66), k=0,...,32, enclosed
by L037's rational pi and the existing uniform trig remainder.
At g_k=m+h x_k integrate the complete angular range callbacks,
retaining their exact masses and all fallback contributions. The
node intervals enclose the values at the ideal nodes despite numerical
node uncertainty; rounded nodes are not substituted in the theorem.
If a_j are the Chebyshev coefficients of p_32, they are

    a_0=(1/33) sum_k A(g_k),
    a_j=(2/33) sum_k A(g_k) cos(j(2k+1)pi/66), j>=1.

For completeness the finite cosine interpolation identity follows
from sum_k cos(l(2k+1)pi/66)=0 for 1<=l<=65 and the product-to-sum
formula: the constant column has squared norm 33, every other column
has squared norm 33/2, and distinct columns are orthogonal. Thus this
formula is the unique degree-32 interpolant, not a least-squares fit.
All signed operations are outward interval operations. The full node
and coefficient intervals are in
`scripts/discriminant/bulk-haar-polynomial-nodes-192.json`.

**Full fixed Euler expectations and cancellation.** For each fixed
integer j>=1, absolute multiplication of the uniformly convergent
Dirichlet series for Zcal^j and its conjugate is justified by
sum_n d_j(n)n^-5/2=zeta(5/2)^j<infinity. Prime-Haar character
orthogonality keeps exactly equal integers. Thus

    E_mu |Zcal|^(2j)=C_j,
    C_j=product_p sum_(e>=0) binom(j+e-1,e)^2 p^-5e.

This imports L419/L422's fixed-moment construction, equivalently the
absolutely convergent Euler-product theorem in
[DLMF 27.4.1--27.4.2](https://dlmf.nist.gov/27.4); the character
application above checks its specialization. No critical-line
high-moment hypothesis is used. Expanding T_j((gfrak(W)-m)/h) as
a finite polynomial in W requires orders only through 448. The
complete required list has 371 orders including zero. Its interval
coefficients retain the original source uncertainty in alpha, theta,
C_13,C_14; none is fitted or treated as exact decimal data.

Recompute L422 (9)--(10) through p=200, using local terms through an
exponent e<=1024 with next ratio
((j+e)/(e+1))^2 p^-5<1. Bound each local omitted tail by its first
term over 1-ratio. Stop only when that bound is at most 10^-110
times the retained local lower sum. The largest exponent needed is
325. For every omitted prime range verify both
1-j^2/201^5>0 and r_C(j)<1 before using the product upper bound
1/(1-r_C(j)). All 17020 local factors and all global tails are saved.
This is an extension of the numerical orders, not a reproof of the
Euler theorem or reuse of L422's insufficient old numerical list.

Signed monomial expectations use outward 160-place integer intervals.
Independently |T_j((gfrak(W)-m)/h)|<=1, so intersect each raw interval
with [-1,1]; this retains both valid enclosures. The complete record
`scripts/discriminant/bulk-haar-polynomial-expectation-192.json`
retains each polynomial, moment, raw and intersected expectation,
signed coefficient product and final sum. Adding [-R_32,R_32]
gives (16), with computed endpoints approximately -2.6243456401 and
2.6159529272 and width about 5.2402985673. The required width is
3/4 of the exact step-190 width, approximately .2299963611.
Both zero exclusion and the width test fail; intersection with (15)
therefore retains the old bound without improvement.

**Diagnosis and limits.** Every saved node interval, and every
Chebyshev coefficient interval, contains zero. Hence this independent
coefficient enclosure already permits the zero polynomial, regardless
of how accurately its expectation is evaluated. Node interval widths
range from about .0124194 to .171431. Also 27 of the 32 nonconstant
raw moment intervals cover the whole [-1,1] before the independent
Chebyshev bound is imposed. This is a measured conditioning failure
of the chosen interval evaluation, not a lower bound on true moments,
true node error, coefficient-source uncertainty alone, or the best
attainable expectation width. Raising working precision alone does
not remove the retained angular range or prime-tail intervals.

Complete relevant records were processed with exact rational comparisons
for the partition, all node/coefficient zero inclusions, every saved
local ratio and global-tail formula, and the final failure fields.
The summary is `scripts/discriminant/bulk-haar-polynomial-verification-192.json`.
All checks pass under the stated arithmetic contract. Counting the
eight preliminary selector probes, both 1024-cell preflights, the
1472-callback refined preflight, the 1444 selector replays and 47652
node/cell evaluations gives 52624 angular callback boxes, below
65536. Degree, prime, exponent and precision caps all hold. The
scripts are not formally verified and no separate critical proof
audit is claimed.

Reproduction commands (the preflight writes the refined certificate):

    python3 scripts/discriminant/preflight_bulk_haar_polynomial.py
    python3 scripts/discriminant/certify_bulk_haar_polynomial.py
    python3 scripts/discriminant/verify_bulk_haar_polynomial.py

The stronger retained enclosure (15), I's undecided sign, actual
clipping, realization, L413's full-error regulator margin and the
global mixed-positivity gap are unchanged. Further repetition of this
same independent-coefficient/moment-box implementation is stopped.

## Mathlib

Full matching coverage for this prescribed-basis actual-height limit
has not been checked. The compact-group Weyl criterion, absolutely
convergent Euler logarithm, sharp nonstationary bound and null-
discontinuity test theorem are imported by the precise references
above. Supporting integration, product-Haar and continuity results
would not alone cover the exact physical comparison and two-stage
selection. Unknown Mathlib coverage is not evidence of absence;
no Lean verification is claimed.
The full matching enclosure specializations (11)--(15) are also not checked
in Mathlib; the finite certificate uses the explicit integer contract above.
Full matching coverage for the prescribed angular envelopes and Euler
expectation calculation (16)--(20) has not been checked. Standard
polynomial, integration and Haar results alone would not certify the
recorded selector or its numerical error budgets.
