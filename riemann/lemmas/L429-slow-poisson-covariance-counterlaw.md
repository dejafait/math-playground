# Lemma 429: a slowly growing Poisson weight preserves the counterlaw

## Hypotheses

Use exactly the integrated-moment relaxation of L423: the full actual
response on [H,2H], height marginal dt/H, ell=log H, exact polynomials
B(X;t)=b(t)^T X and D(X;t)=X^T J(t)X, and its original selected
tolerances. These include both first means, six raw critical seconds,
the signed cubic, all 23 quartic coefficients, both absolute third-power
envelopes, the fourth-power envelope, and the qualitative fixed physical
jet bounds. Retain its added requirement E_nu[W^2 x^2]=T ell+o(ell),
where W=|zeta(5/2+it)|^2 and T is L422's exact coefficient.

Retain L421's high and intermediate kernels without modification,
including their combined raw second matrix Q, first B integral J_R,
first D integral D_R, and remaining fiber mass w. Use L419's exact
response bounds and Borel six-state construction, and L423's full
mean and matrix correction formulas. The constants in the qualitative
envelopes can be chosen once, independently of H; they are not separately
prescribed smaller constants. No conditional actual critical moments or
consistency of different H laws is imposed.

Let p_j be the j-th prime. The only replacement weight permitted here is

    P_j(t)=product_(p<=p_j) (1-1/p)/|1-p^(-1/2-it)|^2,
    g_H(t)=P_j(t)/N_H, N_H=E_H[w P_j],
    E_H=H^(-1) integral_[H,2H],

with j=j(H) tending to infinity sufficiently slowly. Write
q_H(t)=integral x^2 dnu_(H,t)(X) for the complete raw x-second density,
including its mean and all three law components. L389 identifies the
actual f^2 with |zeta(1/2+it)|^2 without dividing by zeta.

## Conclusion

There is a stepwise cutoff j(H) tending to infinity on an eventual
real-H ray for which this replacement gives a measurable family
satisfying every stated constraint. In addition, for each fixed prime p,

    E_H[(q_H-f^2)p^(-it)]=o(ell).                       (1)

The six raw seconds and the first B mean are exact:
E_nu XX^T=ell K and E_nu B=-b0, with K and b0 as in L423.
The family avoids {D>0,B<0}, and for every fixed lambda>0,

    E_nu[|DB| min(1,|X|/(lambda ell^2))]
       =O(ell)+O_lambda(ell^(3/2))+O_lambda(ell^(1/4))
       =o(ell^2).                                      (2)

The family and its constraint onset do not depend on lambda. The onset
in (1) may depend on p, and the cap onset may depend on lambda. No
effective cutoff rate or uniform estimate over growing primes is claimed.
The added W^2 mean has its original o(ell) tolerance; L423's stronger
O(sqrt(ell)) error for its fixed mixture is not asserted here.

This extends a selected-information counterlaw, not the actual critical
function. It is a local specialization not supplied by the sources
checked; the separate step-212 critical audit below validates its stated
scope. The original POTENTIALLY_NEW label does not certify originality.
Actual clipping, global realization, the full-error
regulator margin and global mixed positivity remain unresolved. This is
neither a candidate proof nor a disproof of RH.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-growing-prime-poisson-law-feasibility.md`.
Its source comparison is reused. Only the changed-weight limits and
simultaneous law estimates are proved here. L422's single-power and
L427's unchanged-mixture separations, and L428's uniformly bounded
density obstruction, are historical contrasts, not premises of feasibility.

### Finite-product inputs and complete response coefficients

Import C. Aistleitner, I. Berkes and K. Seip, *GCD sums from Poisson
integrals and systems of dilated functions*, JEMS 17 (2015), 1517--1546,
DOI 10.4171/JEMS/537, [section 3, p. 1527, identity preceding Lemma 1
and equation (23)](https://ems.press/content/serial-article-files/32047?nt=1).
For a finite polydisc with radii r_p in (0,1) and normalized Haar measure,
the Poisson kernel has integral one and character integral
product r_p^|e_p|. Set r_p=p^(-1/2); all source hypotheses hold for
each finite stage. No infinite critical Euler product is taken.

Define

    M_j=product_(p<=p_j) (1+p^(-1/2))/(1-p^(-1/2)).

The pointwise one-circle extrema and multiplication give

    M_j^(-1)<=P_j(t)<=M_j.                            (3)

Each finite product has an absolutely convergent Fourier series:
the one-circle sum of absolute coefficients is (1+r_p)/(1-r_p),
so the product's sum is M_j. Unique factorization implies that no
nonzero integer combination of distinct prime logarithms vanishes.
For fixed nonzero u, the sharp average of exp(iut) is at most
2/(H|u|). Applying this to a finite Fourier head and then its absolute
tail gives the continuous-height character average. In particular,

    E_H P_j -> 1,
    E_H[P_j p_i^(-it)] -> p_i^(-1/2)  (i<=j).          (4)

This is the elementary character specialization of the fixed compact
group averaging covered in the assessment, not a growing-twist theorem.

For positive integers m,n let

    k_j(m,n)=0 if v_p(m)!=v_p(n) for some p>p_j;
    k_j(m,n)=product_(p<=p_j) p^(-|v_p(m)-v_p(n)|/2)
                 otherwise.

The same character calculation, adjoining the finitely many outside
primes in m,n, gives
E_H[P_j(m/n)^(-it)] -> k_j(m,n). The signs of the exponents do
not matter because the Poisson coefficients are real and symmetric.
One has 0<=k_j<=1 and, for each fixed pair, eventually

    k_j(m,n)=gcd(m,n)/sqrt(mn).                        (5)

Expand the complete absolutely convergent response series, with
Z=zeta(5/2+it), Z^2=sum d_2(n)n^(-5/2-it). At fixed j this gives

    E_H[P_j W] -> S_j
       :=sum_(m,n>=1) (mn)^(-5/2) k_j(m,n),
    E_H[P_j W^2] -> T_j
       :=sum_(m,n>=1) d_2(m)d_2(n)(mn)^(-5/2) k_j(m,n). (6)

For completeness the tail control does not need a growing supremum
times a fixed response tail. For r=1,2 put
V_r=Z^r and V_r,N=sum_(n<=N)d_r(n)n^(-5/2-it), where d_1=1.
Let delta_r,N=sum_(n>N)d_r(n)n^(-5/2), which tends to zero.
Uniformly on the full prime torus or at actual heights,

    ||V_r-V_r,N||_infinity<=delta_r,N,
    || |V_r|^2-|V_r,N|^2 ||_infinity
          <=2 zeta(5/2)^r delta_r,N.                  (7)

The finite Poisson measure, extended by Haar measure for any extra
primes, is positive with total mass one. Thus (7) bounds its coefficient
tail independently of j. On the height interval it bounds the weighted
tail by the same constant times E_H P_j; this is at most 2 eventually
at each fixed j by (4). This proves the full fixed-stage limits (6).
The majorants (mn)^(-5/2) and d_2(m)d_2(n)(mn)^(-5/2) are summable.
Equation (5) and dominated convergence then yield

    S_j -> S=sum gcd(m,n)/(m^3 n^3)
             =zeta(5)zeta(3)^2/zeta(6),
    T_j -> T=sum d_2(m)d_2(n)gcd(m,n)/(m^3 n^3).       (8)

These are exactly L381's (14)--(15)/L419's S and L422's T.
The evaluation of S groups m=da,n=db with (a,b)=1, all absolutely;
L381 supplies this evaluation. No new actual zeta moment is inferred
from the artificial Poisson measure.

The other full response input is the gamma harmonic. In L419 notation
R=exp(i phi), a+ih=RZ, and

    E_H[P_j R^2 Z^2] -> 0                             (9)

at each fixed j. Indeed P_j Z^2 has an absolutely convergent series
of fixed real frequencies. For a finite head the phase 2phi(t)+ut
has derivative log(t/(2pi))+u+O(t^-2), at least (log H)/2 eventually,
and second derivative O(1/H). The sharp integration-by-parts formula
has endpoint bound O(1/log H) and integral bound O(1/log^2 H);
division by H makes each term vanish. The uniform absolute tail
then tends to zero, proving (9). These are exactly L419's phase
hypotheses; no conditional phase independence is used. Full response
truncation could also be made before this argument: its error is at
most delta_2,N E_H P_j, independently of the gamma factor of modulus
one. This retains all response terms.

### One slow cutoff on every sufficiently large real height

Choose eps_j=1/(j+4). The limits (4), (6), (9) imply the existence
of a finite threshold B_j beyond which, for every real H, all of

    |E_H P_j-1|, |E_H(P_j W)-S_j|,
    |E_H(P_j W^2)-T_j|, |E_H(P_j R^2 Z^2)|,
    max_(1<=i<=j)|E_H(P_j p_i^(-it))-p_i^(-1/2)|

are at most eps_j. Increase these thresholds, if necessary, to have
B_(j+1)>=2 B_j, log B_j>=M_j^8, and B_1 beyond the common
eventual onset for the unchanged inputs below. Define j(H) to be the
largest j with B_j<=H. The thresholds tend to infinity, so this is
finite for every H>=B_1, Borel, and tends to infinity. It gives (3)
with M_j<=ell^(1/8) and simultaneously

    E_H P_j=1+o(1), E_H(P_j W)=S+o(1),
    E_H(P_j W^2)=T+o(1), E_H(P_j R^2 Z^2)=o(1),
    E_H(P_j p^(-it))=p^(-1/2)+o(1) for each fixed p. (10)

Every estimate holds across the entire interval [B_j,B_(j+1)),
including its left endpoint. No subsequence or unproved convergence
rate is substituted for an eventual real-height limit. The thresholds
depend only on finite-stage tests, not on lambda. There is no need to
include an increasing-twist actual zeta theorem in their selection.

L421 gives w in [1/4,1], E_H(1-w)=O(ell^(-5/2)),
Q>=0, ||Q||=O(sqrt(ell)), J_R=O(ell^-1), and
D_R=O(sqrt(ell)). The constants are independent of j because these
components are unchanged. By (3) and our cutoff,

    0<=E_H[(1-w)P_j]<=C ell^(-19/8).

Consequently N_H=E_H(wP_j)=1+o(1), eventually 1/2<=N_H<=2, and

    (1/2)ell^(-1/8)<=g_H<=2ell^(1/8),
    E_H(wg_H)=1.                                    (11)

For every uniformly bounded response expression F(t), including all
the tests in (10), the exact difference is

    E_H(wg_H F)-E_H(P_j F)
       =(N_H^-1-1)E_H(wP_j F)-E_H((1-w)P_j F)=o(1). (12)

Here |E_H(wP_j F)|<=N_H||F||_infinity; the last term is
O(||F||_infinity ell^(-19/8)). There is no pointwise assumption
that the high probability p(t) tends to zero.

The moving-weight response tail is now controlled exactly: by (7)
and E_H(wg_H)=1, replacing W^r by |V_r,N|^2 in a normalized weighted
mean costs at most 2 zeta(5/2)^r delta_r,N for every eventual H.
Replacing Z^2 in the gamma mean costs at most delta_2,N.
Thus no moving test or uncontrolled product supremum is hidden in
(10)--(12); the small supremum factor was used only for the explicitly
bounded rare-mass loss.

### Covariance, trace and translated support

Use the unchanged exact L423 formulas, with W_H=E_H w:

    d_H=(-b0-J_R)/W_H, m(t)=d_H b(t)/|b(t)|^2,
    A_H=-(Q+E_H[w m m^T])/W_H,
    Sigma(t)=ell g_H(t)K+A_H.                         (13)

L419 gives bounded J,b, |b|>=b_min>0, K positive definite and
tr(JK)<=-delta_0<0 uniformly. Hence m is uniformly bounded and
||A_H||<=C_A sqrt(ell), with constants independent of j,H. The
entire symmetric A_H is retained, including both odd entries.
Writing kappa_0=lambda_min(K)>0 and J_* a bound for ||J||,
(11) gives

    lambda_min(Sigma)>=(kappa_0/2)ell^(7/8)-C_A ell^(1/2),
    ||Sigma||<=2||K||ell^(9/8)+C_A ell^(1/2),
    tr(J Sigma)<=-(delta_0/2)ell^(7/8)+3J_*C_A ell^(1/2). (14)

Thus Sigma is positive definite and has strictly negative J-trace
with a uniform margin c ell^(7/8), after one fixed onset.

Import the real Schur--Horn theorem as stated in E. A. Carlen and
E. H. Lieb, *Short proofs of theorems of Horn and Mirsky on diagonals
and eigenvalues of matrices*, [arXiv:0904.0734v2, pp. 1--2, Horn's
theorem following (1.1), proof through (1.2)](https://arxiv.org/pdf/0904.0734v2).
The trace-average diagonal is majorized by the eigenvalues of the real
symmetric matrix Sigma^(1/2) J Sigma^(1/2). L419's explicit Borel
two-rotation implementation therefore gives an orthonormal basis u_i
with that diagonal, including repeated-eigenvalue and equality branches.
That algorithm is valid for every positive definite Sigma; it does not
require fixed bounds on g_H.

Let mu_(H,t) assign probability 1/6 to each of

    m +/- sqrt(3) Sigma^(1/2) u_i, i=1,2,3.

The centered law has mean zero, covariance Sigma, symmetry, and each
centered D value is tr(J Sigma). Each centered atom has norm at most
C ell^(9/16). Translating by bounded m changes D by at most
C ell^(9/16)+C. Since 9/16<7/8, (14) implies exact D<0 for all
six translated atoms, uniformly in t and H after one common onset.
Also |X|<=C ell^(9/16) on the bulk. This explicitly compares the
largest translation error with the smallest negative margin.

Define nu_(H,t)=p(t)delta_Y(t)+k(t)delta_Zmid(t)+w(t)mu_(H,t).
The unchanged masses sum to one in each fiber and are nonnegative.
All branch choices and j(H) are Borel. Parameter integrals defining
N_H,m,A_H are Borel after t=Hu, 1<=u<=2; their integrands are locally
bounded on compact eventual H intervals, which meet only finitely many
stages. Thus this is also a jointly measurable family. At a fixed H
the actual jets and every constructed state are bounded on the compact
height interval, giving integrability of every observable used here.

### Exact seconds, both first means and the additional correlations

Equations (11), (13) give exactly

    E_nu XX^T=Q+ell K+W_H A_H+E_H[wmm^T]=ell K,
    E_nu B=J_R+W_H d_H=-b0.                          (15)

This meets all four O(1) even-second tolerances, both much smaller odd
tolerances O(H^(-2/3)ell^-1), O(H^(-2/3)ell^-3), and the full
first-B tolerance O(ell^-1+H^(-1/2)ell^2), with zero errors.

For first D, L419's exact trace estimate is

    tr(JK)=-c^2(a^2/20+h^2/12)+O(1/L), c=1/(4pi),
    a^2=(W+Re(R^2 Z^2))/2, h^2=(W-Re(R^2 Z^2))/2.

Using (10)--(12) and the exact normalized mass, its O(1/L) error
integrates to O(1/ell), and

    E_H[wg_H tr(JK)]=-c^2 S/15+o(1)=-a_*+o(1).

The remaining D terms D_R+E_H[w(tr(J A_H)+m^T Jm)] are
O(sqrt(ell)). Thus E_nu D=-a_* ell+o(ell), its original tolerance.

Let r_H(t) be the sum of the two unchanged rare x-second densities.
It is nonnegative and E_H r_H=Q_11=O(sqrt(ell)). The complete
raw density is

    q_H=r_H+w(ell g_H+A_H,11+m_1^2).                 (16)

Consequently for every bounded test F,

    E_H(q_H F)=ell E_H(wg_H F)+O(||F||_infinity sqrt(ell)), (17)

with a uniform constant. Applying (17) to W^2 proves the complete
added coefficient T ell+o(ell), not just a centered-bulk coefficient.
Applying it to p^(-it) and using (10)--(12) gives
E_H(q_H p^(-it))/ell -> p^(-1/2) for each fixed prime.

For the actual target import audited L428 (6):
E_H(f^2 p^(-it))/ell -> p^(-1/2). Its primary input is
M. P. Young, *A short proof of Levinson's theorem*, Arch. Math. 95
(2010), 539--548, DOI 10.1007/s00013-010-0199-9,
[Lemmas 4--5, (4.1)--(4.5), pp. 542--543](https://www.math.ntnu.no/emner/MA3001/2020v/2022v_MA3004/Young.pdf),
via L381 (7) and L389's identity for f^2. Fixed twists satisfy the
source length condition eventually; both zero-shift diagonals are
combined at their removable singularity. L428's four nonnegative
squares and sharp endpoint bracketing supply the complex sharp limit.
No smoothing inequality for a complex integrand or growing twist is
introduced here. Subtracting these two fixed-p limits proves (1).

### Remaining selected moments, physical envelopes and cap

Centered bulk symmetry gives the exact identity

    E_mu DB=(b^T m)tr(J Sigma)+2m^T J Sigma b
                                +(m^T Jm)(b^T m).

Its absolute value is at most C(||Sigma||+1). More usefully than the
supremum bound, (13) and E_H(wg_H)=1 give

    E_H[w||Sigma||]<=ell||K||+W_H||A_H||=O(ell).

Thus the integrated signed bulk cubic is O(ell). L421's unchanged
high cubic is O(ell), and its intermediate cubic is exactly
beta_* ell^2, giving E_nu DB=beta_* ell^2+O(ell).

Each selected quartic has absolute value at most C|X|^4, uniformly
for the full actual response. The high component preserves its actual
integral exactly by L421 (3), including all signed matrix entries and
zero leading coefficients. The intermediate addition is O(ell^(7/2)).
The bulk norm bound gives an addition O(ell^(9/4)). Both additions
are o(ell^4); therefore all 23 required coefficients survive. The
same calculation gives E_nu |X|^4=O(ell^4). For |X|^3 and |B|^3,
the three component bounds are respectively O(ell), O(ell^2) and
O(ell^(27/16)). Their sum is O(ell^2), within the original
O(ell^(9/4)) absolute third-power envelopes. All these constants
are independent of j and H by the explicit cutoff bound (11).

The actual response annulus, derivative estimates, strict Ccal lower
bound and exact curvature remain unchanged. On the high component
the states have either norm ell^3 or are signed 2^(1/4) multiples of
the actual critical triple, as in L421. The intermediate norm is
ell^(3/2), and the new bulk norm is O(ell^(9/16)). The exact conversion
to physical jets has uniformly bounded coefficients. Since

    sup_(H<=t<=2H) ell^3 L(t)^r/T(t)^(1/2) -> 0 (0<=r<=2),

one fixed set of physical E_r works on all polynomial-size branches;
the other high branch uses one fixed enlargement of the actual bounds.
This verifies the prescribed qualitative envelopes on the whole family,
not separate constants for different prime stages.

The high support avoids {D>0,B<0} by its original orientation, the
intermediate support has B,D>0, and the bulk has exact D<0. For the
absolute capped cubic, L421 bounds the entire high contribution by
O(ell). The intermediate contribution is exactly
beta_* ell^(3/2)/lambda eventually for fixed lambda. On the bulk,
|X|<=C ell^(9/16)<lambda ell^2 eventually, and

    |DB| min(1,|X|/(lambda ell^2))
          <=C |X|^4/(lambda ell^2).

Its integral is O_lambda(ell^(1/4)). This proves (2) without signed
cancellation. The same family works for every fixed lambda because
lambda was absent from every construction and threshold above.

All remaining estimates require only finitely many common eventual
onsets after (11); taking their maximum preserves j(H)->infinity.
The construction supplies the full simultaneous feasibility conclusion.
Its density is not uniformly bounded as required by L428's stopped
route, and no contradiction with that result is asserted. The separate
critical audit below checks this specialization. It supplies no actual
realization or RH sign conclusion.

### Separate critical audit — 2026-10-18, step 212

This RESEARCH / REPRODUCTION / proof_audit uses the pre-existing
SPECIALIZE assessment
`drafts/literature/2026-10-18-growing-poisson-counterlaw-critical-audit.md`.
The conclusion passes in its stated integrated-moment relaxation.
This verifies the existing specialization, not a new source theorem,
originality, actual conditional law or RH consequence. The entire
construction above and the load-bearing input proof ranges were checked.

**Imported inputs and two limit orders.** The cited finite Poisson
identity uses normalized Haar measure and finitely many radii strictly
between zero and one. At r_p=p^(-1/2) it applies exactly. Outside-head
prime characters integrate to zero; inside-head characters have their
stated symmetric coefficients. Unique factorization accounts for all
zero frequencies, giving exactly k_j(m,n), including unreduced ratios.
For each fixed j the Fourier series has finite absolute coefficient
sum M_j, so finite-head averaging followed by its uniform tail proves
(4). In (6), the squared response tails satisfy (7) because both the
full and truncated V_r have modulus at most zeta(5/2)^r. The finite
Poisson measure has mass one, while E_H P_j<=2 eventually at that
fixed j. Thus the head can be removed after the fixed-stage height
limit, with a bound independent of the response head. The positive
double-series majorants in (6) are summable. Each pair's kernel
eventually equals gcd(m,n)/sqrt(mn), so dominated convergence in j
gives the complete S and T of L381 (14)--(15) and L422 (1).
No infinite critical-line Euler product is asserted.

For (9), at fixed j the full P_j Z^2 has an absolutely convergent
frequency expansion. For each finite head, L419's exact phase bounds
give |(2phi+ut)'|>=log H/2 and |(2phi+ut)''|<=C/H eventually.
The sharp integration-by-parts boundary and integral terms are
O_u(1/log H) and O_u(1/log^2 H), before division by H. Their
normalized integrals vanish; the discarded absolute Fourier tail is
uniform in H. This also includes both sharp endpoints and retains
every full-response term. The source hypotheses are fixed frequencies,
not frequencies increasing with H.

**One real-height diagonal and normalization.** Each stage has finitely
many convergent tests. Their definition of a limit supplies one B_j
valid for every real H>=B_j. Recursively enlarging B_j to meet the
doubling and log B_j>=M_j^8 conditions preserves that property.
The largest admitted j is finite, is Borel, tends to infinity, and
satisfies M_j<=ell^(1/8) at every H in its entire stage, including
the left endpoint. The errors eps_j and S_j-S,T_j-T tend to zero.
For a fixed prime, its test appears at every stage beyond its index.
These facts prove (10) without taking an actual increasing-twist limit.

L421 (4)--(6) leave E_H(1-w)=O(ell^(-5/2)) and all rare constants
unchanged. Multiplication by P_j<=ell^(1/8) therefore costs at most
O(ell^(-19/8)); no pointwise rarity is required. Hence N_H=1+o(1)
and (11) follows from both extrema of P_j. The exact difference (12)
is bounded in modulus by

    ||F||_infinity (|1-N_H|+E_H[(1-w)P_j]).

It tends to zero uniformly over tests with a common sup norm.
In particular all response and prime tests used here qualify. After
normalization, the positive measure w g_H dt/H has exactly mass one,
so (7) controls its full response tails independently of H and j.
This is the essential reason a moving supremum does not multiply an
uncontrolled response tail.

**Full correction and every translated atom.** L419 gives the exact
K, bounded J,b, positive lower bound for |b| and tr(JK)<=-delta_0.
L421 gives Q>=0, ||Q||=O(ell^(1/2)), J_R=O(ell^-1) and w>=1/4.
Thus (13) makes m uniformly bounded and ||A_H||=O(ell^(1/2)),
independently of j. Both covariance extremes in (14) follow from
(11); |tr(J A_H)|<=3||J|| ||A_H|| retains every entry.
The smallest covariance and negative trace have order ell^(7/8),
strictly larger than the correction order ell^(1/2). The largest
covariance has order ell^(9/8). For xi_i=sqrt(3) Sigma^(1/2)u_i,
the imported constant-diagonal realization gives

    xi_i^T J xi_i=tr(J Sigma), |xi_i|<=C ell^(9/16),
    D(m +/- xi_i)<=-c ell^(7/8)+C ell^(9/16)+C<0.

All constants and the eventual onset can be fixed for every stage.
The Schur--Horn import applies to any finite real symmetric matrix;
it imposes no uniform upper covariance bound. L419's explicit rotations
also apply here: a strict branch solves
(d_j-tau)eta^2+2e eta-(tau-d_i)=0 with positive denominator and
radicand greater than e^2. Equality branches select coordinate vectors;
the complementary two-dimensional trace is 2tau. These cases exhaust
the construction and are Borel. Unit vectors stay bounded even near
branch changes. Thus neither a continuous eigenbasis nor a measurable
selection theorem is being assumed.

The unchanged rare kernels are Borel with their zero conventions.
After t=Hu, their parameter integrals and those in (13) are Borel;
on compact eventual H intervals all input states are bounded and only
finitely many stages occur. Positive N_H and positive definite Sigma
make all subsequent operations Borel. The final fiber masses are
nonnegative and sum to one. This verifies joint measurability, exact
dt/H marginal and integrability, including across stage jumps.

**Original tolerances and complete correlations.** Integrating the full
raw covariance Sigma+mm^T gives (15), with Q and the entire A_H,
so all six seconds have zero error. In particular no O(sqrt(ell))
error remains in either tiny odd tolerance. The first B mean is also
exact, meeting its O(ell^-1+H^(-1/2)ell^2) allowance. For first D,

    a^2/20+h^2/12=W/15-Re(R^2 Z^2)/60.

Equations (10)--(12) therefore give the coefficient -c^2 S/15=-a_*.
The exact trace remainder contributes O(1) after multiplication by ell,
and D_R, A_H and m contribute O(sqrt(ell)); all are o(ell).
The required error is o(ell), not a bounded remainder.

For the full raw x-second density, K_11=1 and (16) includes both
rare densities, the mean square and A_H,11. Their absolute integrated
contribution is at most Q_11+W_H|A_H,11|+E_H(w m_1^2)=O(sqrt(ell)).
This proves (17) also for complex bounded tests. L422's full T
therefore gives the original W^2 tolerance o(ell). For each fixed p,
L428 (6) is the sharp actual target with either character orientation.
Its four nonnegative squares were checked against L381 (7): fixed
twists meet Young's length hypothesis eventually, both zero-shift
diagonals are retained, and smoothing limits precede polarization.
L389 (3) identifies f^2 with |zeta(1/2+it)|^2 even at zeros.
Consequently (1) follows for the complete q_H with no complex
bracketing or response-conditioned actual moment premise.

**Remaining moments, fixed bounds and cap.** Central symmetry leaves
exactly the three displayed terms in E_mu DB. Integrating their
absolute value costs O(ell), since E_H(w||Sigma||)=O(ell), despite
the larger pointwise covariance. The unchanged intermediate cubic is
exactly beta_* ell^2 and the high cubic is O(ell). Thus the original
signed cubic tolerance is met. The high homogeneity identity preserves
each of the 23 actual quartic integrands, including signed and zero
coefficients. Intermediate and bulk additions are O(ell^(7/2)) and
O(ell^(9/4)), both o(ell^4). The fourth envelope remains O(ell^4).
For both absolute third envelopes the three costs are O(ell),
O(ell^2), O(ell^(27/16)); their sum is O(ell^2), within O(ell^(9/4)).

All response quantities and curvature remain actual. The high branches
have norm ell^3 or are signed 2^(1/4) times the actual triple;
the other branches are smaller powers of ell. The bounded exact
physical conversion and ell^3 L(t)^r/T(t)^(1/2)->0 uniformly for
0<=r<=2 permit one fixed enlargement of qualitative constants.
There is no separately prescribed smaller bound to meet.

Finally the unchanged high and intermediate support and the proved
strict negative bulk support exclude the joint sign. Their absolute
capped cubic contributions are bounded by O(ell),
beta_* ell^(3/2)/lambda eventually, and O_lambda(ell^(1/4)),
respectively. The last uses the full bulk fourth bound divided by
lambda ell^2. Every term is o(ell^2). No construction parameter or
constraint onset uses lambda; only the eventual cap comparison does.
This is a single family for every fixed cap, not uniformity as the
cap parameter shrinks with H.

No defect or missing direct mathematical input was found. The proof
and direct inputs need no change. L428's uniform-density obstruction
and L423's original selected-list validity are preserved. This audit
does not settle actual clipping, capped nondegeneracy, realization by
one critical function, L413's full-error regulator margin or RH.

## Mathlib

Full matching Mathlib coverage for this height-dependent counterlaw has
not been checked. The finite polydisc identity, Young moment input and
real Schur--Horn theorem are imported by their precise citations above.
L419 supplies the additional Borel implementation. No claim of Mathlib
absence or formal verification is made; no numerical certificate is
needed for the qualitative threshold construction.
