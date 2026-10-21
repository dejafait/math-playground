# Lemma 444: all temporal x-second tests exclude a bounded covariance repair

## Hypotheses

Use precisely the complete L443 family on its eventual real-H ray.
Write ell=log H, L(t)=log(2+t), I_H=(H,2H), and E_H for H^(-1)
integration over [H,2H]. Keep the high and both intermediate components,
their probabilities, w, m, g_H, actual response, and original L429
cutoff unchanged. Let q^0 be L443's complete conditional raw second
matrix, including its L441 and L443 covariance fields.

An allowed further change is a symmetric Borel bulk covariance field
F(t), with F11=0. Its change to the complete raw matrix is
exactly w F. In the proposed application it must also have
E_H[w F]=0 entrywise, retain the selected constraints and L443's
three exact identities, and have a norm bounded independently of H.
The obstruction below does not need these additional restrictions.

Use L435's smooth signed density W_3, negative on a nonempty open
three-torus set, and L438's calibration
f_H(theta)=beta W_3(theta)+a_H^T(1,cos theta_2,P(theta)),
where a_H tends to zero and P is fixed. The rare components are exactly
those of L438. Use L440's audited response-angle and complete moment
interfaces. There is no trajectory-realization, independence, actual
critical-function sine-limit or inter-H consistency assumption.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-all-temporal-x-second-occupation.md`.
This is a local REPRODUCTION using its covered occupation, weak-balance
and averaging tools. No originality beyond the checked sources is claimed.

## Conclusion

There are fixed c_0>0, C_0<infinity and a full eventual real-H ray,
and temporal tests a_H^test in C_c^1(I_H), such that

    ||L a_H^test||_infinity+||(a_H^test)'||_infinity<=C_0,
    R_H:=E_H[(a_H^test)' q^0_11+2L a_H^test q^0_12]
                                                   >=c_0 sqrt(ell). (1)

Consequently every field F satisfying (F)11=0 and the x-squared
occupation identity for all temporal tests must obey

    E_H[w |F12|]>=c_0 sqrt(ell)/(2 C_0),
    ||F||_(L-infinity,op)>=c_0 sqrt(ell)/(2 C_0).           (2)

The first assertion assumes the tested entries are integrable; the
second applies whenever the norm is finite. Thus no uniformly bounded
field can solve the approved target, even before exact recentering,
support, the other finite identities and the selected tolerances are
imposed. This rules out the specified bounded extension of L443.
It does not rule out corrections growing with H, changing the rare
components or x-second density, or other laws.

The separate step-275 critical audit validates this local obstruction. It preserves
L443's finite-block compatibility and all previous selected-law results.
It supplies no actual clipping value, capped nondegeneracy, actual/global
realization, L413 full-error regulator margin, global mixed positivity,
new zeta sign or zero-exclusion range, or RH conclusion.

## Proof

### The necessary weak equation and its source scope

Import the necessary finite-interval occupation identity from
J. B. Lasserre, D. Henrion, C. Prieur and E. Trelat, *Nonlinear optimal
control via occupation measures and LMI-relaxations*, SIAM J. Control
Optim. 47 (2008), 1643--1666, DOI 10.1137/070685051,
[math/0703377v1](https://arxiv.org/pdf/math/0703377v1),
Sections 2.2--2.3, (2.7), (2.10)--(2.12), printed pp. 4--5.
For fixed H the ordinary C^2 trajectory has x'=Ly and fits finite
compact state/control boxes. The test phi(t,x)=a(t)x^2 is C^1 with
zero temporal endpoints for a in C_c^1(I_H). Its necessary identity is

    E_H[a' q11+2L a q12]=0.                              (3)

This uses no converse representation theorem. For the permitted change,
q11=q^0_11 and q12=q^0_12+w F12, exactly, so (3) becomes

    E_H[a' q^0_11+2L a(q^0_12+w F12)]=0.                 (4)

In distribution notation it requires
(q^0_11)'=2L(q^0_12+w F12). The weak-derivative interpretation is
John K. Hunter, *Notes on Partial Differential Equations*, revision
2014-06-18, [Definition 3.1, pp. 47--49; Theorems 3.53,
3.60--3.63, pp. 77--80](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf).
For fixed H, bounded F makes the right side bounded, since the
complete law is bounded on that compact interval. The cited
one-dimensional result would then give a Lipschitz representative.
We do not presume or need this regularity: (4) itself will force (2).
The norm comparison at the end is the elementary integration bound
covered by Hunter, *Measure Theory* (2011),
[Section 7.5, Proposition 7.13, pp. 84--85](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes.pdf).
No converse duality theorem or general theorem is reproved.

### A compact temporal test on the negative-calibration region

Set f=beta W_3. L435's explicit negative point and continuity give
delta>0 and a fixed nonzero smooth torus function psi with

    0<=psi<=1, supp psi contained in {f<-2delta}.          (5)

One can take a smooth nonnegative bump in a small coordinate ball
about that point. Its closed support is inside that open set.
L438 gives ||f_H-f||_infinity->0 and uniformly bounded first torus
derivatives. Thus f_H<=-delta on supp psi for every sufficiently
large real H. Both psi and its derivatives vanish outside supp psi.
On this support the positive intermediate probability is exactly zero,
and f_H,-=-f_H>=delta. The negative part f_H,- is uniformly Lipschitz
on the whole torus, with constants independent of H.

Let eta(u)=(u-5/4)^2(7/4-u)^2 for 5/4<=u<=7/4, and zero elsewhere.
It is C^1, nonnegative, nonzero, and compactly supported in (1,2).
Set e(t)=eta(t/H), theta(t)=(t log 2,t log 3,t log 5).
Use L440's actual smooth response angle and modulus

    Z=zeta(5/2+it)=rho exp(i chi), alpha=varphi+chi,
    0<rho_min<=rho<=rho_max, |rho'|<=C,
    alpha'=ell/2+O(1), |alpha''|<=C.                      (6)

The phase chi is the Euler-log phase on Re s=5/2. These bounds hold
uniformly on the interval with its fixed H. Put

    G(alpha)=-cos(2alpha),
    a_H^test(t)=e(t) psi(theta(t)) G(alpha(t))/L(t).        (7)

This is genuinely in C_c^1(I_H), rather than merely zero at the
endpoints. Its norm and derivative satisfy the first inequality of (1).
Writing B(t)=e(t)psi(theta(t)), its exact derivative is

    (a_H^test)'=B alpha' G'/L+(B'/L-B L'/L^2)G,
    = (1/2)B G'+O(1/ell),                              (8)

uniformly, since B,B' are uniformly bounded, L=ell+O(1),
and L'<=1/H. All slow terms in (8) are included in its error.
No probability, atom, law coefficient or cutoff is differentiated.

### The negative intermediate defect has a positive angular mean

L438 and L440 give the exact intermediate raw entries

    q^mid_ij=sqrt(ell) sum_(s=+,-)
                      f_H,s(theta(t)) (n_s)_i(n_s)_j/h_s. (9)

On the support of a_H^test or its derivative the plus term vanishes
by (5). For the minus direction, L440's explicit formulas are

    n_-=(cos alpha+sin alpha,
           (cos alpha-sin alpha)/2,
           -(cos alpha+sin alpha)/4)/v(alpha),
    v(alpha)^2=(21+13 sin(2alpha))/16,
    h_-,0=c^3 rho^3/(8v^3), c=1/(4pi).

The exact h_- differs from h_-,0 by O(1/ell); both are uniformly
bounded below by a positive constant. This is L440's coefficient
comparison, including the exact response and curvature errors.
The displayed numerator of n_- is exact, and rho cancels in its
normalization. In particular, uniformly in alpha and t,

    (n_-)_1^2/h_-=rho^(-3) U(alpha)+O(1/ell),
    (n_-)_1(n_-)_2/h_-=rho^(-3) V(alpha)+O(1/ell),
    U=8v(1+sin(2alpha))/c^3,
    V=4v cos(2alpha)/c^3.                               (10)

There are no selection ties in this negative direction. The positive
direction's potentially nonsmooth ties have been excluded only from
the test support, not removed from the law.

Let A(t)=e(t)psi(theta(t))f_H,-(theta(t))rho(t)^(-3).
It and its almost-everywhere derivative are bounded uniformly in H,
by (5)--(6) and L440's uniform Lipschitz bound on f_H,-.
Using (8)--(10), the complete tested intermediate contribution is

    R_mid=sqrt(ell) E_H[A(t) J(alpha(t))]+O(ell^(-1/2)),
    J=(1/2)G' U+2G V.                                 (11)

The error includes both coefficient errors and every slow derivative
in (8); bounded f_H,- makes their integrated costs uniform.

For normalized circle mean <.>, periodic integration by parts gives

    <J>=<G(2V-U'/2)>=:kappa.

Indeed v'=13 cos(2alpha)/(16v), and exact cancellation of the other
terms gives

    2V-U'/2=-13 cos(2alpha)(1+sin(2alpha))/(4c^3 v),
    kappa=13/(4c^3)
       <cos^2(2alpha)(1+sin(2alpha))/v(alpha)> >0.        (12)

The integrand is continuous, nonnegative and positive on an open set.
For an explicit lower bound, on |sin(2alpha)|<=1/2 it is at least
(3/8)sqrt(8/17), and this set has normalized measure 1/3.
Thus kappa>=13 sqrt(8/17)/(32c^3)>0.

Apply L440 (14) to the fixed bounded zero-mean angular function
J-kappa and the uniformly Lipschitz amplitude A. All its hypotheses
are exactly (6) and the bounds just stated; its absolutely continuous
integration-by-parts proof includes both endpoints. It gives

    R_mid=kappa sqrt(ell) E_H A+O(ell^(-1/2)).           (13)

This is deterministic fast-phase averaging, not independence.
Furthermore

    E_H A>=delta rho_max^(-3) E_H[e psi(theta(t))].

The last average tends to
(integral_1^2 eta(u)du)<psi>, which is strictly positive.
The source for the fixed continuous torus average is E. Kowalski,
*Arithmetic Randonnee: An introduction to probabilistic number theory*,
2021-01-19 manuscript,
[B.6.3, B.6.5(2), B.6.6(2), printed pp. 146--147](https://metaphor.ethz.ch/x/2021/fs/401-3109-65L/probabilistic-number-theory-fs-2021.pdf#page=150),
as specialized in L438. Its orbit is the full torus because unique
prime factorization makes each nonzero integer character frequency
nonzero. To check the additional slow weight, approximate eta uniformly
by fixed step functions. On a fixed interval [aH,bH], the normalized
psi integral tends to (b-a)<psi>, by subtracting the source's
[0,bH] and [0,aH] averages. The uniform approximation error is at
most ||psi||_infinity times the approximation error. Let that error
tend to zero after H. This justifies the weight without a moving-test
equidistribution assertion. Therefore some fixed a_0>0 satisfies

    E_H A>=a_0                                        (14)

on a full eventual real-H ray.

### Every other term of the complete raw matrix is lower order

Combine L438's complete matrix with L443's bounded repairs. Denote
their sum of covariance fields by B_old(t); it is uniformly bounded
and has zero 11 entry. Let R_hi=pYY^T and R_mid be the two exact
intermediate raw matrices in (9). In this paragraph R_mid denotes
that matrix only, not the scalar in (11). Exactly,

    q^0=R_hi+R_mid+w[ell g_H K+A_H+mm^T+B_old].

Here K11=1, K12=0, A_H is constant in t, ||A_H||=O(sqrt(ell)),
|m|=O(1), E_H(1-w)=O(ell^(-5/2)),
E_H[p|Y|^2]=O(ell^(-2)), and
g_H=P_j/N_H with N_H=1+o(1) and sup g_H<=2ell^(1/8).
These are complete-law bounds, not statements about the leading bulk
alone.

Replacing w by 1 only in the bracket changes its 11 entry in L1
height mean by at most

    C E_H(1-w)(ell^(9/8)+sqrt(ell)+1)
                                  =O(ell^(-11/8)),     (15)

and its 12 entry by O(ell^(-2)). In view of (7)--(8) these costs
are also negligible in the tested residual. The rare matrix itself
has not been approximated in this replacement.

The high term costs O(ell^(-2)) by its complete absolute second bound
and the bounded coefficients (a_H^test)' and 2L a_H^test.
The translated matrix mm^T and B_old cost O(1) by their uniform
bounds. The constant A11 term is exactly zero because integral a'=0.
For the A12 term, G has zero circle mean, so L440 (14) with the
uniformly Lipschitz amplitude e psi gives

    |2A12 E_H[L a_H^test]|
          =O(sqrt(ell)/ell)=O(ell^(-1/2)).              (16)

It remains to bound the entire Poisson contribution in the 11 entry.
No high-frequency averaging of an uncontrolled moving amplitude is
used. L429's exact finite product and L440's unchanged-cutoff bounds
give, with y=p_j and M_j its supremum,

    P_j=product_(p<=y)(1-1/p)/|1-p^(-1/2-it)|^2,
    M_j<=ell^(1/8), y<=ell^(1/4).

For r=p^(-1/2), direct differentiation of its positive denominator
gives

    |(log P_j)'|
       <=sum_(p<=y) 2r log p/(1-r)^2 <=C y log y.

The last estimate uses r<=2^(-1/2), at most y primes, and
log p<=log y; it does not need a prime-number theorem. The denominator
bound is uniform, so

    ||g_H'||_infinity<=C ell^(3/8)log ell.                (17)

H and its cutoff stage are fixed in this derivative; N_H is a
constant in t. The product is finite and smooth, regardless of
discontinuities of the law across different H. The compact support
of a_H^test permits the exact integration by parts

    |E_H[(a_H^test)' ell g_H]|
       =|ell E_H[a_H^test g_H']|
       <=C ell^(3/8)log ell=o(sqrt(ell)).                (18)

Thus the complete Poisson part, including every retained prime under
the original cutoff, is lower order. Its mass-loss term was already
included in (15); no derivative of w or of an actual critical jet
was needed. The finite Poisson inputs used here are those imported in
L429 from Aistleitner--Berkes--Seip, *GCD sums from Poisson integrals
and systems of dilated functions*, JEMS 17 (2015), 1517--1546,
[Section 3, p. 1527, identity preceding Lemma 1 and (23)](https://ems.press/content/serial-article-files/32047?nt=1).
Only the displayed finite-product derivative estimate is additional
local work; no infinite critical-line Euler product is invoked.

Combining (13)--(18) yields the complete residual estimate

    R_H=kappa sqrt(ell) E_H A
                  +O(ell^(3/8)log ell+1).              (19)

By (14) and ell^(-1/8)log ell->0, this proves (1), for example with
c_0=kappa a_0/2 after one later onset. All constants precede H and
its stage; no rate for a_H->0 or new cutoff threshold is required.

### Universal bounded-field obstruction and qualifications

If (4) holds for every test, it holds for (7), hence

    R_H=-2E_H[L a_H^test w F12].

The integration bound and (1) imply

    c_0 sqrt(ell)<=2C_0 E_H[w |F12|].

Since 0<=w<=1 and |F12|<=||F||op, this gives both bounds (2).
It applies to every possible field with zero 11 entry, regardless
of the values of its other entries or any dependence on H.
Exact w-weighted recentering, supported covariance realization and
retaining the other finite identities can only restrict this class
further; none can evade the inequality. This is why failure of the
particular finite sine ansatz is not the conclusion being used.

The proven lower bound is of order sqrt(log H), against the requested
O(1) bound. It is not a proof that a correction of that growing size
exists. Nor does it require or establish the weak regularity of the
fixed q11. The construction uses an admissible H-dependent temporal
test at each H, as allowed by the universal quantifier in the target.
All rare, translation, constant calibration and old repair terms were
included in (19). L443's three exact fixed identities remain valid,
and no contradiction to any actual trajectory is asserted.

### Separate critical audit — 2026-10-20, step 275

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment
`drafts/literature/2026-10-20-all-temporal-bounded-repair-critical-audit.md`.
The complete proof passes within its stated scope. No coefficient,
hypothesis, cutoff, mathematical argument or direct input needs repair.
The general source results above are imported in their assessed scopes;
this audit checks their application to the complete law, not those
general theorems afresh.

**Localization and admissible test.** L435's exact negative point has
positive real local factors and real multiplier
(48-41sqrt(2))/75<-47/375. Its rational denominators stay off the
three circles, so f=beta W_3 is smooth and strictly negative on an
open set. Choose the closed support in (5) strictly inside that set.
L438's uniform convergence, not a convergence rate, gives the single
eventual negative margin there. At a point outside supp psi there is
a neighborhood on which psi is zero, so its derivative is zero too.
Thus both terms of the exact derivative in (8) exclude the plus
intermediate, including the term containing the prime-phase derivative
of psi. No positive-direction selection tie is silently differentiated.

The zero extension of eta has matching zero value and derivative at
5/4 and 7/4. The test is C1 with support in [5H/4,7H/4] strictly
inside (H,2H). The smooth nonvanishing right-line response and its
Euler-log phase justify its remaining factors. L440 gives
alpha'/L=1/2+O(1/ell), uniformly in the fixed interval, and bounded
alpha''. The derivative B' includes the fixed prime velocities and
eta'/H, so the slow remainder in (8) is indeed O(1/ell). The norm
constant is independent of H and the stage. The necessary identity
requires only x'=Ly; no derivative of the conditional law is used.

**Angular sign and positive slow mass.** Directly squaring the exact
negative-direction numerator gives v^2=(21+13sin(2alpha))/16,
with 1/2<=v^2<=17/8. Its first square and first cross entry are
(1+sin(2alpha))/v^2 and cos(2alpha)/(2v^2). Dividing by the
uniformly positive h_-,0 gives exactly U and V in (10).
The uniform O(1/ell) error in h_- transfers to the reciprocal,
since both exact and leading denominators have fixed lower bounds.
Together with (8) this costs O(ell^(-1/2)) after the full
sqrt(ell) intermediate scale is included.

Differentiating v^2 gives v'=13cos(2alpha)/(16v).
In U'/2 the term 8v cos(2alpha)/c^3 cancels 2V exactly.
The remainder has the negative sign in (12); multiplication by
G=-cos(2alpha) makes its circle integral positive. On
|sin(2alpha)|<=1/2, cos^2(2alpha)>=3/4,
1+sin(2alpha)>=1/2 and 1/v>=sqrt(8/17).
This set occupies one third of the circle, confirming the explicit
kappa lower bound in (12). The integral has no endpoint term because
U and G are periodic.

The amplitude A is uniformly Lipschitz: f_H has uniformly bounded
torus derivatives, its negative part is Lipschitz, the prime velocities
are fixed, and rho is bounded below with bounded derivative.
L440 (14) therefore applies to J-kappa and gives an error O(1/ell)
before multiplication by sqrt(ell). This does not assume independent
prime and response phases. For the lower bound on E_H A, only psi
needs torus averaging: f_H,- >=delta on its support and
rho^(-3)>=rho_max^(-3) suffice. Unique factorization verifies every
nonzero character frequency required by the cited continuous-time
criterion. Subtracting initial-interval averages gives the limit on
each fixed [aH,bH]; uniform step approximation of eta then proves
the positive weighted limit on the entire real-H ray. There is no
moving-frequency theorem or subsequence selection.

**Full matrix and error scale.** L438 (14) and L443's exact
raw-matrix interface give the displayed q^0, including the old
L441 field and L443's additional field in B_old. Both are bounded,
have zero 11 entry, and change no rare component or translation.
The constant matrix A_H is held fixed in t. The following absolute
budgets account for all terms except the signed intermediate main
term already evaluated:

| Term in the tested residual | Bound |
| --- | --- |
| Removing w from the 11 bulk bracket | O(ell^(-11/8)) |
| Removing w from the 12 bulk bracket | O(ell^(-2)) |
| Complete high raw matrix | O(ell^(-2)) |
| Translation mm^T and both old repair fields | O(1) |
| Constant A11 after removing w | Exactly zero |
| Constant A12 after removing w | O(ell^(-1/2)) |
| Complete finite Poisson term after removing w | O(ell^(3/8)log ell) |

For the first two rows multiply E_H(1-w)=O(ell^(-5/2))
by the respective bracket bounds O(ell^(9/8)) and O(sqrt(ell)).
The latter uses K12=0; the former uses K11=1.
The tested coefficients a' and 2La are uniformly bounded.
The high estimate controls every needed entry by p|Y|^2.
Translation and old fields need only their uniform value bounds.
The A11 integral is zero by compact support. For A12 apply
L440 (14) to the zero-mean G with amplitude e psi, obtaining
O(1/ell), and then use |A12|=O(sqrt(ell)).
No derivative of w, m, any selected atom or A_H is required.

For the last row the original L429 threshold log B_j>=M_j^8
gives M_j<=ell^(1/8). L440's geometric-series comparison gives
M_j>=sum_(n<=p_j)n^(-1/2)>=sqrt(p_j), hence p_j<=ell^(1/4).
For one positive Poisson denominator its derivative has magnitude
at most 2p^(-1/2)log p, and its value is at least
(1-p^(-1/2))^2. Summing the logarithmic derivatives over at most
p_j primes bounds |(log P_j)'| by C p_j log p_j.
Since N_H>=1/2 is constant in t, this proves (17) with one
stage-independent constant. Exact integration by parts against the
compactly supported test bounds the term by
ell ||a||_infinity ||g_H'||_infinity, giving (18).
The threshold list is unchanged. The earlier mass-loss row accounts
for the difference between w g_H and g_H.

Consequently the complete residual is (19), with positive slow mass
bounded below independently of H. Dividing its error by sqrt(ell)
gives O(ell^(-1/8)log ell+ell^(-1/2))->0.
All onsets can be replaced by their maximum on one real-H ray;
cutoff discontinuities in H are irrelevant because only t is
differentiated. This verifies (1) with c_0=kappa a_0/2.

**Universal conclusion and its limits.** For every admissible field
with finite tested integrals, F11=0 leaves the entire a' term fixed
and changes the residual by exactly 2E_H[La w F12].
The integration bound then yields (2). If the weighted absolute
integral is infinite its lower bound is automatic; if the essential
operator norm is finite, E_H[w|F12|] is at most that norm because
the interval measure is normalized and 0<=w<=1.
Thus the conclusion is not restricted to the sine-field ansatz,
recentering or any values of the other matrix entries. It contradicts
a uniform O(1) bound even without support or preservation constraints.
It neither asserts existence at the lower-bound scale nor settles
local absolute continuity of the fixed q11. The all-test quantifier
permits a different compact temporal test for each H.
L443's finite identities, all selected-law statements and every
independent clipping, realization, regulator and RH gap remain intact.

## Mathlib

Full matching coverage of this constrained-law obstruction and its
uniform fast-phase estimates has not been checked. Unknown coverage
is not absence. The necessary occupation identity, weak-derivative
interpretation, integration norm bound, fixed torus averaging and
finite Poisson inputs are cited precisely above; their local
specializations are justified in the proof. No Lean or numerical
certificate is claimed. The separate step-275 audit validates the local
specialization without asserting additional Mathlib coverage.
