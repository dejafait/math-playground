# Lemma 442: the repaired law fails the remaining y-squared occupation test

## Hypotheses

Use exactly L441's repaired complete conditional law, including its
unchanged rare components, recentered covariance perturbation, actual
response, uniform height marginal and original L429 cutoff. All limits
are through real H on its eventual ray. Write ell=log H, L(t)=log(2+t),
omega=log 2, E_H=H^(-1) integral_[H,2H], and e(t)=eta(t/H), with
eta(u)=(u-1)^2(2-u)^2 on [1,2], zero elsewhere, as in L440.
For an ordinary trajectory use x=f, y=f'/L, z=f''/L^2 with real f in
C^2([H,2H]). No consistency of the conditional laws at different H,
atom continuity, actual sine limit or trajectory realization is assumed.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-repaired-law-remaining-quadratic-occupation.md`.
The full raw-second interface of L438, the signed angular estimates of
L440, the exact perturbation of L441 and K from L419 are the local inputs.

## Conclusion

The complete transport polynomials for e sin(omega t)xy/L and
e sin(omega t)y^2/L are respectively

    T_xy=[e' sin(omega t)/L+omega e cos(omega t)/L
                         -2e sin(omega t)L'/L^2]xy
                                      +e sin(omega t)(y^2+xz),       (1)
    T_yy=[e' sin(omega t)/L+omega e cos(omega t)/L
                         -3e sin(omega t)L'/L^2]y^2
                                      +2e sin(omega t)yz.            (2)

Every stated trajectory has E_H T_xy=E_H T_yy=0 exactly. For L441's
unchanged complete law, with conditional expectation included in E_nu,

    E_nu T_xy=o(1),
    E_nu T_yy=omega/(360 sqrt(2))+o(1)>0 eventually.                 (3)

Thus its x-squared repair does not satisfy this additional necessary
y-squared identity. The xy result asserts only asymptotic cancellation,
not exact finite-H compatibility. This is a local REPRODUCTION of the
assessed occupation and averaging tools; no originality is asserted.
The separate step-267 critical audit below validates this scope. It changes no
selected-moment conclusion of L441 or L438, and supplies no new law,
actual clipping value, capped nondegeneracy, regulator margin, global
mixed positivity, zero-exclusion range or RH consequence.

## Proof

### Necessary identity and complete matrix

Import the necessary C^1 finite-interval occupation identity from
J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat, *Nonlinear optimal
control via occupation measures and LMI-relaxations*, SIAM J. Control
Optim. 47 (2008), 1643--1666, DOI 10.1137/070685051,
[arXiv:math/0703377v1](https://arxiv.org/pdf/math/0703377v1),
Sections 2.1--2.3, (2.7), (2.10)--(2.12), pp. 3--5.
As in L424/L440, at each fixed H a continuous C^2 trajectory fits
finite compact state/control boxes, with control z continuous. Both
tests are C^1, including the cutoff extension. L424 gives
x'=Ly and y'=Lz-(L'/L)y. Substitution gives (1)--(2), retaining the
extra y normalization derivatives. Both test endpoint values vanish.
The imported identity therefore gives the exact trajectory assertions;
only this explicit specialization is calculated, not the general theorem.
H, the cutoff and every law parameter are held fixed in differentiation.

Let q_ij(t) denote the complete repaired conditional raw seconds. In
the notation of L438/L441 their exact matrix is

    q=R+w[ell g_H K+A_H+mm^T+(d(t)-bar_d_H)V],
    R=pYY^T+sum_(s=+,-) k_s Z_s Z_s^T,
    V=e1 e2^T+e2 e1^T.                                           (4)

L419 gives K22=1/12, K13=-1/12, K12=K23=0. The preserved bounds are

    E_H q=ell K, E_H tr R=O(sqrt(ell)), ||A_H||=O(sqrt(ell)),
    m=O(1), |d-bar_d_H|=O(1), E_H(1-w)=O(ell^(-5/2)),
    E_H(wg_H)=1, E_H[p|Y|^2]=O(ell^(-2)).                         (5)

Constants are independent of H and its cutoff stage. Positivity of R
and bounded m imply, entrywise,

    E_H|q_ij-ell wg_H K_ij|=O(sqrt(ell)).                        (6)

The perturbation V has zero entries 22,13,23. For slow terms in (1)
and (2), use E_H q22=ell/12 and
E_H|q12|<=sqrt((E_H q11)(E_H q22))=ell/sqrt(12).
Since ||e'||=O(1/H), L>=ell and L'<=1/H, all e' and L' terms
have total absolute integral O(1/H). The cosine xy term is O(ell^(-1/2))
by (6) and K12=0. Also ell/L=1+O(1/ell). Consequently

    E_nu T_xy=E_H[e sin(omega t)(q22+q13)]+O(ell^(-1/2)+H^(-1)), (7)
    E_nu T_yy=(omega/12)E_H[e cos(omega t)wg_H]
                      +2E_H[e sin(omega t)q23]
                      +O(ell^(-1/2)+H^(-1)).                   (8)

No rare, translation or constant-covariance entry has been removed
from the two remaining signed integrals.

### A quantitative sine bound for the intermediate amplitudes

Set theta(t)=(t log 2,t log 3,t log 5), Z=zeta(5/2+it), rho=|Z|.
Write F_H for L438 (6), and F_s=(F_H)_+ or (F_H)_-. These are real,
centrally even functions of theta, with a uniform supremum and torus
Lipschitz constant. Indeed L435's rational W_3 is smooth on its compact
torus and centrally even; L436's fixed P is centrally even. L438's
bounded coefficient vector a_H multiplies (1,cos(theta_2),P).
Taking either part preserves evenness and the Lipschitz bound. Neither
coordinatewise symmetry nor a convergence rate for a_H is needed.

We need the following quantitative specialization, for r=2 or 3 and
U_H=F_+,F_-, or the constant 1:

    E_H[e sin(omega t) U_H(theta(t)) rho(t)^(-r)]
                  =O(ell^(-3/4)log ell)+O(ell^(-2))
                     +H^(-1) exp(O(ell^(3/4)))=o(ell^(-1/2)).    (9)

Here is a complete finite-frequency estimate; qualitative Haar
convergence alone would not suffice after multiplication by sqrt(ell).
Convolve U_H on each of its three circles with the normalized Fejer
kernel of order M=ceil(ell^(3/4)). The kernel convention is that of
L436: K_M(theta)=(M+1)^(-1)|sum_(j=0)^M exp(ij theta)|^2.
This gives a real centrally even polynomial U_H,M, of degree at most
M in each coordinate, with

    ||U_H-U_H,M||_infinity<=C log(M+2)/(M+1),
    sum_v |hat U_H,M(v)|<=C(2M+1)^3.                           (10)

To verify the needed rate directly, K_M(theta)<=min(M+1,
C/((M+1)theta^2)) for 0<|theta|<=pi, by its finite geometric sum.
Its normalized first distance moment is at most C log(M+2)/(M+1),
by splitting at 1/(M+1). The Lipschitz estimate for the product
convolution follows by summing the three coordinate distances.
Each Fourier coefficient is bounded by the unchanged supremum, giving
the second bound. These elementary estimates supplement the imported
kernel formula specifically to obtain this moving accuracy.

For a=r/2, use the Euler-log branch on Re s>1 to write

    zeta(s)^(-a)=sum_(n>=1) b_a(n)n^(-s), b_a(n) real,
    sum_(n>=1)|b_a(n)|n^(-3/2)<infinity.                       (11)

For precision, expand each (1-p^(-s))^a by its binomial series.
Its absolute local sum at sigma=3/2 is 1+O_a(p^(-3/2)); hence their
product converges absolutely. Unique factorization supplies (11) and
its Euler-log branch. This justifies the fractional power without
assuming a critical-line Euler product. If N=ceil(ell^2), truncation
to n<=N on sigma=5/2 has uniform error O(1/N), since the discarded
n^(-5/2) is at most N^(-1)n^(-3/2). Thus

    rho^(-r)=|sum_(n<=N)b_a(n)n^(-5/2-it)|^2+O(1/N),             (12)

uniformly in height, with bounded absolute Fourier mass. Equality
before truncation follows because the real part of the Euler logarithm
is log|Z|. Multiplying (12) by U_H,M gives a finite real even
exponential polynomial in t. All frequencies are logarithms of positive
rationals with numerator and denominator at most 30^M N.
After multiplication by sin(omega t) this bound is at most
D=2*30^M N. Its constant coefficient is zero: the polynomial before
that multiplication has equal real coefficients at u and -u, including
every rational-frequency collision. For any remaining frequency,
unique factorization and the elementary integer separation estimate
give |u|>=1/D. Integration by parts gives

    |E_H[e exp(iut)]|<=C/(H|u|).

The whole finite sum therefore costs at most C D(2M+1)^3/H.
The errors in (10) and (12) cost O(log M/M+1/N); all other factors
have bounded supremum. Since log D=O(M+log ell)=o(ell), these are
exactly the bounds in (9). The constants use only uniform norms of
U_H; the statement holds for its actual H-dependent coefficients.
This auxiliary truncation does not alter any probability, cutoff,
threshold or law. It asserts no actual critical-function sine moment.

### Both new intermediate raw entries

Use L440's actual angle alpha=varphi+arg Z, c=1/(4pi), and

    A(alpha)=|cos alpha|/2+|sin alpha|/3,
    v(alpha)^2=(21+13 sin(2alpha))/16.

L440 proves alpha'=ell/2+O(1), |alpha''|<=C, and its estimate (14):
a bounded zero-circle-mean angular function g, against any uniformly
bounded Lipschitz amplitude with uniformly bounded a.e. derivative,
has height mean O(1/ell). Its tie-neighborhood bound (15) is O(1/ell).
Also F_s(theta(t)), rho^(-r), and their products with e sin(omega t)
have those uniform Lipschitz bounds. We use this proved deterministic
phase estimate, never independence of prime and response angles.

For s=+,- the exact intermediate raw entry is

    k_s (Z_s)_i(Z_s)_j=sqrt(ell)F_s(theta(t))(n_s)_i(n_s)_j/h_s. (13)

For y^2+xz its leading angular functions are

    G_+(alpha)=5/[9c^3 A(alpha)(A(alpha)^2+1/3)],
    G_-(alpha)=-4v(alpha)sin(2alpha)/c^3.                      (14)

To check them, the positive direction before whole-vector reversal is
(2/3,sigma/3,2/3), so n2^2+n1n3=5/9, independent of sigma.
Its selected leading h is c^3 rho^3 A(A^2+1/3). The negative direction
is proportional to (a+h,(a-h)/2,-(a+h)/4), with a=rho cos alpha,
h=rho sin alpha. Its norm is rho v, its n2^2+n1n3 equals
-sin(2alpha)/(2v^2), and its leading h is c^3 rho^3/(8v^3).
These give (14). Uniform exact denominators and coefficient errors
from L440 imply for each sign

    (n2^2+n1n3)/h_s=rho^(-3)G_s(alpha)+error,
    |error|<=C/ell+C 1_{|sin(2alpha)|<=C0/ell}.                (15)

For the negative direction the indicator is unnecessary. For the
positive direction it includes all projection-selection ties, exactly
as in L440 (19). Let mu_s be the circle mean of G_s. Apply L440's
zero-mean estimate to G_s-mu_s, and its tie bound to (15). The full
weighted intermediate contribution to q22+q13 is therefore

    sqrt(ell) sum_s mu_s E_H[e sin(omega t)F_s rho^(-3)]
                                           +O(ell^(-1/2))=o(1),    (16)

by (9). No assertion that mu_s vanishes is made or needed; retaining
these means is essential.

For yz the positive direction has n3=n1 exactly, and the negative
direction has n3=-n1/4 exactly. Thus each yz raw entry is respectively
the same as, or -1/4 times, its own xy raw entry. L440 (17)--(19)
already controls each signed xy intermediate separately. Its complete
e sin(omega t)-weighted mean is O(ell^(-1/2)) for each sign, hence
so is the sum of the yz intermediate means. The rare directions and
masses are unchanged in L441, so this reuse is exact.

### High states, covariance and translation

The high contributions to both remaining signed integrals are
O(ell^(-2)), using (5) and |y^2+xz|+|yz|<=C|X|^2.
The Poisson part of q22+q13 vanishes pointwise since K22+K13=0;
that of q23 vanishes because K23=0. The added covariance perturbation
also vanishes in all these entries. For either constant A combination,

    |E_H[e sin(omega t)w A_ij]|
        <=C sqrt(ell)[H^(-1)+E_H(1-w)]
        =O(sqrt(ell)/H+ell^(-2)).                          (17)

This keeps the complete constant covariance, including rare-state
recentering, rather than assuming weighted cancellation from exact
integrated seconds.

Finally put d_H=(-b0-J_R)/W_H as in L438, bounded and constant in t.
L440's uniform leading b and lower bound on |b| give, with
D0(alpha)=(17/16)cos(alpha)^2+sin(alpha)^2,

    m2^2+m1m3=d_H^2 rho^(-2)G_m(alpha)+O(1/ell),
    G_m(alpha)=[sin(alpha)^2-cos(alpha)^2/4]/[c^2 D0(alpha)^2]. (18)

The function is smooth and bounded. Subtract its circle mean and use
the same angular estimate. The remaining mean times
E_H[e sin(omega t)rho^(-2)] is o(1) by (9), with U_H=1.
Replacing w by 1 costs O(E_H(1-w)). Thus the entire translated
contribution to q22+q13 is o(1). For yz, the same leading b gives
m2m3=-4m1m2+O(1/ell). L440 (21) bounds its weighted xy mean by
O(1/ell), proving that its yz mean is O(1/ell) too. L441 keeps m
unchanged. These estimates account for every term of (4).

### Assembly and scale

Equations (16)--(18) and the high estimates prove

    E_H[e sin(omega t)(q22+q13)]=o(1),
    E_H[e sin(omega t)q23]=o(1).                            (19)

The most delicate xy error from (16) is
O(ell^(-1/4)log ell)+H^(-1)exp(O(ell^(3/4))), which does vanish
at the required scale one. In (8) use L440 (8)--(12), its audited
moving-height finite-Poisson calculation under the unchanged cutoff:

    E_H[e cos(omega t)wg_H]=1/(30 sqrt(2))+o(1).             (20)

The imported finite Poisson character identity there is C. Aistleitner,
I. Berkes and K. Seip, *GCD sums from Poisson integrals and systems
of dilated functions*, JEMS 17 (2015), 1517--1546, DOI 10.4171/JEMS/537,
[Section 3, p. 1527, identity before Lemma 1 and (23)](https://ems.press/content/serial-article-files/32047?nt=1).
Its finite radii are p^(-1/2)<1; L440's direct Fourier estimate, not
the Haar identity alone, proves (20) for the moving cutoff and e.
The normalization and rare mass loss in (20) are those of the same
law, unchanged by L441. Substitution of (19)--(20) in (7)--(8) proves
(3), with one eventual onset and no added cutoff condition.

The result separates just this unchanged law from one more necessary
occupation identity. Neither its vanishing x-squared and xy residuals
nor this failure settles existence of a different supported law or
any of the independent clipping, regulator and RH positivity gaps.

### Separate critical audit — 2026-10-20, step 267

This RESEARCH / REPRODUCTION audit uses the pre-existing SPECIALIZE
assessment `drafts/literature/2026-10-20-remaining-quadratic-residual-critical-audit.md`.
It checks both complete residuals on the same real-H ray. No law,
cutoff, coefficient, hypothesis or error threshold needs repair.

**Ordinary dynamics and the complete matrix.** Holding H fixed,
(xy)'=L(y^2+xz)-(L'/L)xy and
(y^2)'=2Lyz-2(L'/L)y^2. Differentiating the common factor
e sin(omega t)/L gives precisely the additional normalization
derivative in each of (1)--(2). Only x and y are differentiated;
f in C^2 suffices, with z continuous. The zero extension of eta is
C^1 and vanishes at both interval endpoints. The cited occupation
identity therefore applies in a finite compact state/control box for
each H, without a common box as H grows or derivatives of any atoms.

L438's centered bulk has covariance ell g_H K+A_H and mean zero;
translation adds mm^T. L441 changes only the centered covariance by
(d-bar_d_H)V and preserves every rare component and m. This proves
the exact matrix (4). The positive semidefinite rare matrix satisfies
|R_ij|<=(R_ii+R_jj)/2, so its complete absolute entry budget is
O(sqrt(ell)). The bounded translation and perturbation, and the full
constant A_H, give (6). The exact integrated second matrix is still
ell K. In particular E_H|q12|<=ell/sqrt(12) and E_H q22=ell/12;
these bounds justify the slow terms without conditional cancellation.
For the cosine term of (1), K12=0 and (6) give O(ell^(-1/2)).
For (2), positivity and mass one of wg_H dt/H justify replacing
ell/L by one at cost O(1/ell). Thus (7)--(8) retain all raw entries.

**Quantitative sine estimate and all collisions.** The rational
functions Q_p in L435 have real coefficients and no pole on
|u|=sqrt(p). Conjugating all three coordinates conjugates their
product, so taking its real part proves central evenness and uniform
smoothness. L436's symmetrized fixed kernel P is centrally even.
L438's a_H is real and bounded on the eventual ray. Thus both signed
parts of F_H have uniform Lipschitz and supremum bounds; their bounds
may depend on this one fixed P, not on H or the Poisson stage.

The imported one-circle rate is Lee Lorch, *On Approximation by Fejer
Means to Periodic Functions Satisfying a Lipschitz Condition*, Canadian
Mathematical Bulletin 5 (1962), 21--27, DOI 10.4153/CMB-1962-004-3,
[equations (1)--(5), pp. 21--22, alpha=1 proof p. 23](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/3882561682569E0A63092BDD44372FC0/S000843950005102Xa.pdf/div-class-title-on-approximation-by-fejer-means-to-periodic-functions-satisfying-a-lipschitz-condition-div.pdf).
The needed order log(M)/M is known. The elementary kernel bound in
(10) checks only its normalization, uniform Lipschitz constant and
three-coordinate use, not a new approximation theorem. Product
convolution has mass one, preserves central evenness and the supremum
bound, and incurs at most the sum of the three distance moments.
Each of its (2M+1)^3 Fourier coefficients is bounded by that same
supremum. Real central evenness implies that these coefficients are
real and equal at v and -v; coordinatewise evenness is unnecessary.

For (11), use the binomial expansion with |z|<1 from NIST DLMF,
version 1.2.8, [4.6.7](https://dlmf.nist.gov/4.6#E7), with the local
logarithm in [4.6.1](https://dlmf.nist.gov/4.6#E1), and the Euler
product only on Re(s)>1 in [25.2.11](https://dlmf.nist.gov/25.2#E11).
For a=1 or 3/2, the absolute binomial sum excluding its constant
term is O_a(x), uniformly for 0<=x<=2^(-3/2)<1: divide its
absolutely convergent power series by x and bound it on this compact
interval. Summing x=p^(-3/2) proves convergence of the absolute
product. Unique factorization gives real coefficients b_a(n) with
C_a=sum |b_a(n)|n^(-3/2)<infinity. Absolute convergence also
identifies the product with exp(-a Log_E zeta(s)), where Log_E is
the Euler logarithm tending to zero as Re(s) tends to infinity.
Its real part is log|zeta(s)|. This fixes the fractional branch and
establishes the untruncated modulus identity, without using a
principal logarithm of the possibly rotating value of zeta.

The tail on Re(s)=5/2 is at most C_a/N. Both the full series and
its truncation have absolute norm at most C_a, so their squared
moduli differ by O(1/N), proving (12). The truncated squared
modulus has coefficients b_a(n)b_a(m)/(nm)^(5/2), real and paired
under n<->m, and absolute coefficient mass at most C_a^2. Multiplying
by the finite torus polynomial preserves paired real coefficients
at opposite frequencies even after grouping every equal rational
ratio. The additional sine therefore has exactly zero constant
coefficient: the contributions at frequencies omega and -omega
cancel. No approximate independence or limiting sine moment enters.

Every resulting numerator and denominator is at most
D=2*30^M N. Reduction cannot increase them. A nonzero log(n/m)
has absolute value at least 1/max(n,m)>=1/D. The full absolute
coefficient mass is O((2M+1)^3), and the endpoint integration-by-parts
bound is C/(H|u|). This proves the complete finite bound
C D(2M+1)^3/H. The truncation errors cost O(log(M+2)/(M+1)+1/N)
because the other factors have uniformly bounded suprema. With the
specified M and N, define

    epsilon_H=ell^(-3/4)log(ell+2)+ell^(-2)
                              +H^(-1)exp(C ell^(3/4)).

One fixed C bounds (9) by O(epsilon_H), and
sqrt(ell) epsilon_H->0. These are auxiliary approximations of the
existing observables; neither changes the cutoff j(H) or the law.

**Angular means, ties and translation.** The response lower bound
and absolutely convergent right-line derivatives through order two
give L440's alpha'>=ell/4 and |alpha''|<=C. Its audited absolutely
continuous primitive argument applies to every bounded measurable
zero-mean angular function here. The amplitudes e sin(omega t),
F_s(theta(t)) and rho^(-r) and their products are uniformly Lipschitz
in t; a_H and d_H are held fixed. No H derivative is needed.

For the positive intermediate vector, n2^2+n1n3=5/9 before or
after whole-vector reversal. Dividing by its leading h gives G_+
in (14). For the negative vector U,

    U2^2+U1 U3=((a-h)^2-(a+h)^2)/4=-ah,
    |U|^2=rho^2(21+13 sin(2alpha))/16.

Dividing first by |U|^2 and then by h_-,0 gives exactly G_- in
(14), with its minus sign and factor 4. The leading denominators
are uniformly positive. Exact response/curvature errors are O(1/ell)
on unit vectors. A changed positive selection can occur only in
|sin(2alpha)|<=C0/ell; both quotients remain bounded there and
L440's indicator estimate gives total height measure O(1/ell).
Thus (15) holds with all ties retained. Subtracting each actual
circle mean mu_s costs O(1/ell) by the angular primitive estimate;
the unsubtracted mean costs O(epsilon_H) by (9). After the exact
sqrt(ell) factor in (13), the complete error is
O(ell^(-1/2)+sqrt(ell) epsilon_H)=o(1). No vanishing assertion
about either mu_s is required. The exact relations n3=n1 and
n3=-n1/4 separately reduce the two yz entries to L440's audited
xy estimates, hence give O(ell^(-1/2)) for their sum.

The leading b=c rho(cos(alpha)/4,-sin(alpha),-cos(alpha)) has
|b|^2=c^2 rho^2 D0, with D0>=1. Substitution into
m=d_H b/|b|^2 gives the numerator sin(alpha)^2-cos(alpha)^2/4
and denominator c^2 D0^2 in (18). The lower bound on |b| controls
the O(1/ell) error uniformly, without differentiating its remainder.
Subtracting the mean of G_m gives O(1/ell); retaining that mean
gives O(epsilon_H), using r=2 and U_H=1 in (9). Inserting w
costs O(ell^(-5/2)). The leading relation m2m3=-4m1m2 has a
uniform O(1/ell) error, so L440 controls the other translated entry.

**Complete error and positive constant.** High raw seconds cost
O(ell^(-2)). The Poisson terms in q22+q13 and q23 vanish pointwise
by the exact K entries, and V has zero entries 22, 13 and 23.
Each complete constant-covariance entry is O(sqrt(ell)); its fixed
sine average is O(1/H), and inserting w costs O(ell^(-5/2)).
This verifies (17) with no conditional cancellation assumption.
Consequently all non-Poisson errors in the two residuals are bounded
by a fixed multiple of

    ell^(-1/2)+sqrt(ell) epsilon_H+sqrt(ell)/H+ell^(-2),

which tends to zero. L440's separate audit proves (20) under the
original M_j<=ell^(1/8) cutoff, retaining its full Fourier tail and
normalization N_H->1. It contributes only o(1), not multiplied by
sqrt(ell). Since K22=1/12 and integral eta=1/30, its coefficient
in (8) is exactly omega/(12*30*sqrt(2)). Thus both assertions (3)
are validated, including the strictly positive y-squared limit.

This is validation of a local known-tool specialization, not progress
beyond those sources or proof of an RH sign. The separation applies
to this representative only. Exact finite-H cancellation, other laws,
other occupation tests, actual/global realization, clipping and the
full-error regulator margin remain unresolved. No argument or direct
mathematical input changed, so the existing DAG row remains correct.

## Mathlib

Full matching coverage of the law-specific residuals, occupation
specialization and quantitative moving signed average has not been
checked. No claim of absence is made. The finite calculus, matrix
identities and series estimates above are informal proofs, not Lean
certificates; structural documentation validation is not a proof audit.
