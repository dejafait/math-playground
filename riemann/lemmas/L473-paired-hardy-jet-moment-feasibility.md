# Lemma 473: paired Hardy-jet moments still permit positive clipped mass

## Hypotheses

Let H>1, ell=log H, and I={(r,j): r=0,1; j=0,1,2}, in that order.
All derivatives are ordinary height derivatives; ell is held fixed.
For the actual Hardy function put

    Y_(r,j)(t)=Z^(j)(t+r/ell)/ell^j,  H<=t<=2H,
    S_ab(H)=H^(-1) integral_H^(2H) Y_a(t)Y_b(t) dt,
    F_m(H)=H^(-1) integral_H^(2H) product_a Y_a(t)^m_a dt,
                                           m in N^6, |m|=4.       (1)

For an abstract state v=(x_0,y_0,z_0,x_1,y_1,z_1) define
Q(v)=(x_0 z_0-y_0^2)_+. The required data are all 21 unordered second
and all 126 fourth entries, with exactly these tolerances:

    E V_a V_b=S_ab(H)+O(1), except for the four pairs below;
    E V_(r,0)V_(r,1)=O(H^(-2/3)ell^(-1)), r=0,1;
    E V_(r,1)V_(r,2)=O(H^(-2/3)ell^(-3)), r=0,1;
    E product_a V_a^m_a=F_m(H)+O_m(ell^3), |m|=4.                 (2)

All constants must be uniform on one eventual ray of real H. Their
numerical values are not prescribed. There are no first/cubic constraints,
exact lower fourth coefficients, independence assumptions on the two
actual jets, sample-path constraints or global analytic realization.
No RH, simplicity or zero-free-region premise is used. The arithmetic
moment inputs are imported below; Bui--Hall Proposition 3 has an omitted
proof that is not independently audited here.

## Conclusion

For every sufficiently large real H there is a positive probability law
nu_H on R^6 satisfying (2), supported in |v|<=ell^2, with

    E_nu_H V V^T=ell K,
    E_nu_H Q=ell/144+O(1)>=ell/288.                              (3)

The fixed real symmetric positive definite matrix K is given explicitly
by (6) below. In particular all four tight odd second entries are exactly
zero. All displayed observables are absolutely integrable. The onset is
existential; no numerical atoms or effective height are asserted.

Thus this full two-height second/fourth system does not force E Q=o(ell)
or exclude the nominated ell/288 threshold. This extends the one-height
obstruction L472 using its established bulk, not a new arithmetic moment
theorem. It gives no lower bound on the actual Hardy clipped mean or
negative Xi mass, and no individual-height or higher mixed signs. The
separate application audit in Section 8 verifies the stated construction
without correction; the arithmetic source proofs remain imported.

## Proof

### 1. Imported sources and the complete second specialization

Import Sandro Bettin, *The second moment of the Riemann zeta function with
unbounded shifts*, Int. J. Number Theory 6 (2010), 1933--1944,
[DOI 10.1142/S1793042110003861](https://doi.org/10.1142/S1793042110003861),
[arXiv:1111.0925v1, Theorem 1, p. 2](https://arxiv.org/pdf/1111.0925v1#page=2).
For complex a,b with real parts O(1/log T), c=a-b, its primitive is the
integral of

    zeta(1+c)+zeta(1-c)chi(1/2+a+it)chi(1/2-b-it),                (4)

with error O((sqrt(T)+sqrt(|Im a|)+sqrt(|Im b|))log^2 T).
Coincident shifts mean the limit of the entire bracket, not of its two
singular terms separately. Only |a|,|b|<=C/ell is used. The same fixed
shifts apply to every primitive endpoint U in [H,2H]. The uniform error
there is O(sqrt(H)ell^2), and subtracting the primitive at H retains it.

Also import H. M. Bui and R. R. Hall, *On the derivatives of Hardy's
function Z(t)*, Bull. Lond. Math. Soc. 55 (2023), 2304--2323,
[DOI 10.1112/blms.12859](https://doi.org/10.1112/blms.12859),
[arXiv:2304.05178v1](https://arxiv.org/html/2304.05178v1), specifically
Introduction (1) and its preceding odd-order bound, (6)--(7), Proposition
3 in Section 4.2, and the Cauchy/Hardy conversions in Sections 5 and 7.
The published moment theorems are inputs, not reproof targets. The prior
assessment covers the fixed complex neighborhoods used here. The primary
statements and conversion passages were checked again for this application;
this is not a new discovery review or a full audit of either source.

Write the ordinary phase as Z(w)=exp(i theta(w))zeta(1/2+iw).
The gamma quotient in Bui--Hall's definition provides a holomorphic phase
branch for w=t+z/ell, t in [H,2H], z in any fixed bounded complex set.
Uniform Stirling for these gamma arguments gives

    theta'(t)=lambda_t/2+O(H^(-2)), lambda_t=log(t/(2pi)),
    theta''(t+z/ell)=O(H^(-1)).

These are the phase estimates behind the cited (6)--(7); the complex
extension is away from gamma poles and follows from the same uniform
Stirling expansion, not from differentiating a real-variable error.

For fixed bounded complex r,s set a=ir/ell, b=is/ell, c=i(r-s)/ell and
g(t)=exp(i(theta(t+r/ell)-theta(t+s/ell))). The functional equation gives
the exact identities

    Z(t+r/ell)Z(t+s/ell)
      =g(t)zeta(1/2+a+it)zeta(1/2-b-it),
    chi(1/2+a+it)chi(1/2-b-it)=g(t)^(-2).

Here g=O(1) and g'=O(1/(H ell)), uniformly on the complex sets.
Integration by parts against the primitive error in Bettin therefore
costs O(sqrt(H)ell^2)(sup|g|+integral_H^(2H)|g'|)=O(sqrt(H)ell^2).
It remains to integrate g zeta(1+c)+g^(-1)zeta(1-c).

The phase estimates give
g=exp(c lambda_t/2)(1+O(|c|/(H ell))). The factor |c| is retained:
the phase difference vanishes when r=s. Thus the two pole terms combine,
uniformly also at c=0, into

    2 sinh(c lambda_t/2)/c+O(1).

For example write zeta(1+c)=1/c+h(c), h holomorphic and bounded near
zero, and combine (g-g^(-1))/c before taking a limit. The error in g
then has no singularity. Since lambda_t=ell+O(1), division by H and
integration yield, uniformly on the fixed complex sets,

    H^(-1) integral_H^(2H) Z(t+r/ell)Z(t+s/ell) dt
      =ell G(r-s)+O(1),
    G(d)=integral_(-1/2)^(1/2) exp(i d u) du
        =2 sin(d/2)/d, G(0)=1.                                  (5)

The divided analytic error H^(-1/2)ell^2 is O(1). Both sides of (5)
are holomorphic in r,s. Cauchy differentiation on fixed-radius scaled
circles preserves the O(1) error for j,k<=2; differentiation under the
compact t integral is valid by local holomorphy and compact bounds.
Since d/dr Z(t+r/ell)=Z'(t+r/ell)/ell, all entries in (1) satisfy

    S_((r,j),(s,k))(H)=ell K_((r,j),(s,k))+O(1),
    K_((r,j),(s,k))
      =integral_(-1/2)^(1/2) (iu)^j(-iu)^k exp(i(r-s)u) du.         (6)

This single exact integral specifies all 21 entries, including all nine
cross entries; no independence or numerical fit enters. It is real by
conjugation and u -> -u, and symmetric on interchanging the indices.
Each diagonal 3 by 3 block is

    K_0=[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]].                 (7)

For the four same-height odd entries the stronger Bui--Hall primitive
bound integral_0^T Z^(j)Z^(k)=O(T^(1/3)) for j+k odd applies directly
at the two endpoints H+r/ell and 2H+r/ell. Dividing their difference
by H ell^(j+k) gives exactly the errors in (2). Its even formula (1)
also verifies (7). No generic O(1) replaces the four tighter bounds.

### 2. Complete fourth specialization, including mixed allocations

Choose four independent scaled shifts r_1,...,r_4 in fixed bounded
complex neighborhoods of {0,1}. In Proposition 3 put

    alpha_1=ir_1/ell, alpha_2=ir_2/ell,
    beta_1=-ir_3/ell, beta_2=-ir_4/ell.

All four Hardy factors equal that zeta product times the phase

    g_4(t)=exp(i(theta(t+r_1/ell)+theta(t+r_2/ell)
                   -theta(t+r_3/ell)-theta(t+r_4/ell)))
          =exp(i(r_1+r_2-r_3-r_4)/2)+O(ell^(-1)).

The error is uniform also for complex shifts. Its product with the
zeta integrand has integral O(H ell^3): Holder bounds the integral of
the absolute product by the product of four fourth-norms, each bounded
by O(H ell^4) to the one-fourth power. To check those bounds directly
from the same Proposition 3, for a single positive-height shift a use
alpha_1=alpha_2=a, beta_1=beta_2=conjugate(a); the integrand is then
|zeta(1/2+a+it)|^4. Its main integral is bounded on the fixed scaled
shift set and its error is O(H ell^3). Negative-height factors follow
by conjugation. This auxiliary estimate is pointwise in the parameters;
it need not be holomorphic to bound the holomorphic product error.

With u in [0,1]^4 define

    A=1/2+(u_1-u_2)u_3-u_1,
    B=1/2+(u_2-u_1)u_3-u_2,
    C=1/2+(u_1-u_2)u_4-u_1,
    D=1/2+(u_2-u_1)u_4-u_2.

Substitution in the source's full integral, including its factor
1/(2 zeta(2))=3/pi^2, consequently gives

    H^(-1) integral_H^(2H) product_(l=1)^4 Z(t+r_l/ell) dt
      =ell^4 J(r_1,r_2,r_3,r_4)+O(ell^3),
    J(r)=3/pi^2 integral_[0,1]^4 (u_1-u_2)^2
                   exp(i(r_1 A+r_2 B-r_3 C-r_4 D)) du.             (8)

Every factor has its own shift variable even if its eventual coordinate
repeats. Both sides are holomorphic on the fixed neighborhoods, with
the uniform error just proved. Cauchy differentiation of each r_l to
order j_l<=2 therefore proves, for every list of four coordinates
(r_l,j_l) representing the multi-index m,

    F_m(H)=ell^4 q_m+O_m(ell^3),
    q_m=3/pi^2 integral_[0,1]^4 (u_1-u_2)^2
          (iA)^j_1 (iB)^j_2 (-iC)^j_3 (-iD)^j_4
                   exp(i(r_1 A+r_2 B-r_3 C-r_4 D)) du.             (9)

Formula (9) specifies all binomial(9,4)=126 coefficients, without
omitting three-versus-one or four-versus-zero height allocations.
No factorial is inserted: each derivative acts on its own factor
before coincident shifts are evaluated. Different occurrence orderings
give the same coefficient because they evaluate the same F_m and have
O(ell^3) errors as H -> infinity. The coefficients are real by the same
argument. For a single common r, A+B=C+D removes the exponential and
(9) agrees with the one-height coefficients used in L472. At distinct
heights no odd-total-order vanishing is assumed.

The finite index sets allow all source constants and onsets to be
maximized. Statements (6), the four direct odd bounds and (9) verify the
equivalence of the reference-integral constraints (2) with the assessed
leading-coefficient system. In particular |Y|^4 is a finite sum of
covered fourth monomials, so

    H^(-1) integral_H^(2H) |Y(t)|^4 dt=O(ell^4).                  (10)

### 3. The leading second matrix is strictly positive definite

For real coefficients c_(r,j), (6) gives the exact nonnegative expression

    c^T K c=integral_(-1/2)^(1/2)
                |sum_(r=0)^1 sum_(j=0)^2 c_(r,j)(iu)^j e^(iru)|^2 du.

If this is zero, the continuous integrand vanishes on the interval.
Its inner entire function is P_0(iu)+e^(iu)P_1(iu), where
P_r(z)=sum_j c_(r,j)z^j. The identity theorem makes it zero for all
complex u. At u=iv, v -> +infinity, this says
P_0(-v)=-e^(-v)P_1(-v). A nonzero polynomial cannot tend to zero on
that ray, so P_0=0, and then P_1=0. Thus c=0. Consequently K is
positive definite with some fixed lambda=min eigenvalue(K)>0.
No numerical lower bound for lambda is required. Its possible smallness
affects the existential onset, not the asymptotic order or positivity.

### 4. Extend the L472 bulk while preserving its clipped marginal

Use the twelve-state centered vector B_0 from L472 Section 4:
B_0=(epsilon,v,k epsilon), where epsilon is uniform on {+1,-1},
k equals 1/12 with probability 1/6 and -7/60 with probability 5/6,
and v equals 0 with probability 1/2 and +/-1/sqrt(6) with probability
1/4 each; these three model variables are independent. L472 proves

    E B_0=0, E B_0 B_0^T=K_0, E Q(B_0)=1/144.                  (11)

Here Q(B_0) means the three-coordinate clipped form. This imported
finite-law calculation is reused, not asserted for actual Hardy jets.
Write K=[[K_0,D_0],[D_0^T,K_0]]. Its Schur complement

    S=K_0-D_0^T K_0^(-1)D_0

is positive definite: for nonzero z, evaluate the positive quadratic
form of K at (-K_0^(-1)D_0 z,z). Let e be an independent vector of
three independent uniform signs, so E e=0 and E ee^T=I_3. Set

    B_1=D_0^T K_0^(-1)B_0+S^(1/2)e, B=(B_0,B_1).               (12)

All square roots denote real symmetric positive square roots, supplied
by finite-dimensional spectral diagonalization. Independence and
centering give E B_0 B_1^T=D_0 and
E B_1 B_1^T=D_0^T K_0^(-1)D_0+S=K_0. Hence

    E B=0, E BB^T=K, E Q(B)=1/144.                              (13)

The vector B has at most 96 states and a fixed finite norm bound M_0.
Neither that bound nor any construction variable depends on H.

### 5. Retain every actual fourth moment in a rare component

For Y(t) != 0 put n(t)=Y(t)/|Y(t)| in S^5, choosing any fixed unit
vector when Y(t)=0. Define a positive Borel measure mu_H on S^5 by

    integral f(n) dmu_H(n)
      =(H ell^4)^(-1) integral_H^(2H) |Y(t)|^4 f(n(t)) dt.

The zero-radius convention receives weight zero; compact-interval
continuity ensures finiteness. By (10) its mass W_H<=W_* for a fixed
finite W_*>0 beyond one onset. Let eta_H be the pushforward of
ell^(-4)mu_H under n -> ell^2 n. Its unnormalized contributions are

    p_H=eta_H(R^6)=W_H ell^(-4),
    R_H=integral vv^T deta_H=integral nn^T dmu_H,
    0<=R_H, ||R_H||<=trace(R_H)=W_H<=W_*,
    integral v^m deta_H=ell^4 integral n^m dmu_H=F_m(H), |m|=4,
    0<=integral Q(v) deta_H=integral Q(n) dmu_H<=W_*/2.             (14)

The inequality for Q uses (n_x0 n_z0-n_y0^2)_+<=
(n_x0^2+n_z0^2)/2<=1/2. The radius, mass, second and fourth factors
in (14) follow directly from homogeneity. No reflection is performed:
all cross quartics and odd leading coefficients are retained exactly.

### 6. Correct the bulk covariance without losing the clipped bound

Put w_H=1-p_H. On an eventual ray w_H>=1/2. Define

    E_H=ell^(-1)K^(-1/2)R_H K^(-1/2),
    A_H=K^(1/2)(I-E_H)^(1/2)K^(-1/2).                           (15)

Since 0<=E_H and ||E_H||<=W_*/(ell lambda), it is at most I/2 for
large H. Spectral diagonalization and 0<=1-sqrt(1-x)<=x for
0<=x<=1/2 show

    A_H K A_H^T=K-R_H/ell,
    ||A_H-I||<=C_A/ell,
    C_A=||K^(1/2)|| ||K^(-1/2)|| W_*/lambda.                     (16)

Give the law of sqrt(ell/w_H) A_H B total mass w_H, and add eta_H.
This defines a positive probability law nu_H; its second matrix is
exactly

    w_H(ell/w_H)A_H K A_H^T+R_H=ell K.                         (17)

Thus all cross second entries and both diagonal blocks are corrected
at once, including the four exactly zero odd entries in (7). An O(1)
odd error has not been absorbed into the power-saving tolerances.
Equations (6)--(7) and the direct odd bounds now prove every second
requirement in (2).

For each homogeneous degree-four monomial M, the bulk contribution is

    (ell^2/w_H) E M(A_H B)=O_M(ell^2),                           (18)

since w_H>=1/2, ||A_H||<=2 eventually and |B|<=M_0. Combined with
the exact rare fourth equality in (14), this proves the stronger
E V^m=F_m(H)+O_m(ell^2), hence every one of the required O_m(ell^3)
bounds. It also retains (9), including its vanishing coefficients.

To check the clipped statistic quantitatively, let J_0 be the real
symmetric six by six matrix with entries (x_0,z_0),(z_0,x_0) equal
to 1/2, the (y_0,y_0) entry equal to -1, and all others zero.
Then Q(v)=(v^T J_0 v)_+ and ||J_0||=1. The positive-part map is
1-Lipschitz, so for real u,v

    |Q(u)-Q(v)|<=(|u|+|v|)|u-v|.

Apply this to u=A_H B,v=B and use E|B|^2=trace K. For ||A_H||<=2,

    |E Q(A_H B)-1/144|<=3 C_A trace(K)/ell=C_Q/ell.               (19)

Mass and degree-two homogeneity cancel w_H exactly in the bulk:

    E_nu_H Q=ell E Q(A_H B)+integral Q deta_H
            =ell/144+O(1),
    E_nu_H Q>=ell/144-C_Q>=ell/288 when ell>=288 C_Q.              (20)

This proves the requested numerical coefficient, not merely an
unspecified positive lower bound. One common onset can enforce all
source estimates, ell>=1, ell^4>=2W_*, ell>=2W_*/lambda,
ell>=C_A, ell>=288 C_Q, and 2 sqrt(2ell) M_0<=ell^2. The last
inequality bounds the bulk support by ell^2; the rare support already
has that radius. Compact support proves absolute integrability of
all 21 second, 126 fourth and clipped observables. No subsequence,
limit-law convergence or numerical eigenvalue certificate is used.

### 7. Scope of the negative test

The exact leading kernel is nonsingular even though the two scaled
heights are close. This permits an O(1) correction to second moments
inside an order-ell positive matrix, while fourth moments live at
order ell^4 and the new bulk contributes only order ell^2. The method
therefore settles the approved feasibility test at its stated errors.

The construction uses actual quartic data only to obtain a positive
spherical measure; it changes radii and adds a different bulk. It is
not the actual joint Hardy law, does not preserve any unrequested
moments, and need not arise from a function of height. The current
ordinary-moment pair-division and frozen-jet failures are not reopened.
L471 is downstream motivation only: its actual clipped-mass estimate
still requires information not forced by (2). This lemma uses L472's
bulk as a mathematical input; the older rare/bulk precedents are not
additional premises. It is an established-mechanism specialization;
the prior bounded comparison found no full matching theorem, which
does not establish originality.

### 8. Separate critical application audit, 28 October 2026

This audit replays the application under the previously saved SPECIALIZE
assessment `drafts/literature/2026-10-28-l473-critical-audit-coverage.md`.
The theorem and its errors pass without repair. This is verification
of the existing obstruction, not a new moment theorem or a stronger
obstruction. L472 Sections 4/7 were read in full for the bulk input.

**Weighted second primitive and coincidence.** Bettin v1 Theorem 1,
p. 2, and its small-shift completion, pp. 9--10, were checked at the
primary PDF cited in Section 1. Fix the scaled complex parameters on
a bounded open set containing slightly larger closed circles than
those used for Cauchy differentiation. With ell fixed, every endpoint
U in [H,2H] has log U=ell+O(1), so the same shifts satisfy the theorem
with one constant. If E(U) is the difference of its two primitives,
then sup_U |E(U)|<=C sqrt(H)ell^2. The weighted error is exactly

    g(2H)E(2H)-g(H)E(H)-integral_H^(2H) g'(t)E(t) dt.

Thus the derivative bound on g, not any derivative of E, gives the
stated O(sqrt(H)ell^2) error. The functional-equation factors are
g^(-2), so the weighted main bracket has signs g and g^(-1) as in
Section 1; reversing the Hardy phase would give a different kernel.

For completeness, the analytic phase is obtained by logarithms of the
nonvanishing gamma factors on these neighborhoods. Its derivative is

    theta'(w)=-log(pi)/2
      +(psi(1/4+iw/2)+psi(1/4-iw/2))/4,

where psi=Gamma'/Gamma. Uniform complex Stirling in the two sectors
gives the real-center theta'(t) and complex theta'' bounds used in
Section 1. Integrating theta' along the segment between t+s/ell and
t+r/ell yields an error O(|r-s|/(H ell^2)); in particular it vanishes
on r=s. Consequently g-exp(c lambda_t/2) is divisible holomorphically
by c, and its quotient is O(1/(H ell)). With h(c)=zeta(1+c)-1/c,
the complete weighted bracket is

    (g-g^(-1))/c+g h(c)+g^(-1)h(-c).

The first term has a removable singularity and the other two are
uniformly bounded. This proves the required O(1) error through c=0,
without estimating either zeta pole separately. Replacing lambda_t
by ell costs O(1), since the derivative with respect to lambda of
2 sinh(c lambda/2)/c is cosh(c lambda/2)=O(1) on this set.

The error in (5) is holomorphic and uniformly O(1) on these larger
sets. For scaled circle radius rho>0, Cauchy's derivative bound is
j! k! rho^(-j-k) times that supremum. All j,k<=2 are fixed, so no
power of ell is lost. The same argument for four independent shift
variables preserves O(ell^3) in (8) through total derivative order
eight. Differentiating an occurrence variable j times produces the
normalized derivative ell^(-j)Z^(j), with no factorial in the moment.

**Fourth phases and full coverage.** Bui--Hall v1 Proposition 3,
Introduction (1) and preceding odd bound, and Sections 5/7 were
checked at the primary HTML cited in Section 1. The proposition has
four independent complex shifts, uniform O(H ell^3) error and an
explicitly omitted proof. It is not restricted to two squared values.
Substitution gives coefficients of r_1,r_2,r_3,r_4 in its exponent
plus the Hardy phase respectively iA,iB,-iC,-iD. This checks both
reflection signs, and 1/(2 zeta(2))=3/pi^2 checks the normalization.

Replacing the Hardy phase costs O(ell^(-1)) times the absolute
zeta-product integral. For each complex a, the auxiliary substitution
alpha_1=alpha_2=a, beta_1=beta_2=conjugate(a) gives exactly an absolute
fourth power, bounded by O(H ell^4). Holder therefore bounds the
absolute product by O(H ell^4). Conjugation is used only for this
bound; the difference to which Cauchy is applied is holomorphic.
Thus this step has O(H ell^3) error even on the complex circles.

Every unordered second pair is an entry of (6): twelve entries in the
two diagonal blocks and nine cross entries. Every fourth multi-index
has a list of four occurrences, each differentiated independently in
(8), so (9) covers all 126 entries. Repeated occurrences do not bring
multinomial factors. Reordering a list leaves the reference integral
unchanged; dividing the two resulting asymptotics by ell^4 and taking
H to infinity proves equality of their fixed coefficients. It also
proves reality, and does not assume odd-total-order vanishing across
different centers. In the same-height blocks, the two odd pairs use
the direct primitive estimate at H+r/ell and 2H+r/ell. Their errors
are exactly O(H^(-2/3)ell^(-1)) and O(H^(-2/3)ell^(-3)). They are
never replaced by the generic O(1) error.

**Strict positivity and the finite bulk.** The Gram functions in (6)
are (iu)^j exp(iru). A zero real quadratic form forces their entire
linear combination to vanish on the whole complex plane. Along u=iv
the polynomial at r=0 tends to zero because the other term has the
factor exp(-v); therefore both polynomials vanish. This proves strict
positive definiteness, not just a semidefinite numerical fit. The
fixed separation one in scaled variables is essential to that proof;
no uniform eigenvalue claim for shrinking separation is made.

L472's twelve states have E k=-1/12, E k^2=1/80 and E v^2=1/12.
The only positive clipped event is k=1/12,v=0, of probability 1/12,
giving E Q=1/144. The Schur extension preserves these first three
coordinates exactly. Its cross second block is D_0, since
E[B_0(D_0^T K_0^(-1)B_0)^T]=D_0; its other block is K_0 by the
Schur identity. Independent signs contribute zero cross terms and
second matrix I_3. Thus (13) and the finite, H-independent M_0 hold.

**Rare part, matrix correction and simultaneous bounds.** Expand
|Y|^4 as sum_a Y_a^4+2 sum_(a<b)Y_a^2Y_b^2. These covered entries
give one W_* on an eventual ray. The zero-radius convention has zero
weight. A homogeneous degree-d observable under the rare pushforward
receives multiplier ell^(2d-4); hence its mass is O(ell^(-4)), second
matrix is R_H, and every fourth contribution is exactly F_m(H).
The unnormalized clipped contribution is between zero and W_*/2.

The correction does not require R_H to commute with K. In fact
K^(-1/2) K K^(-1/2)=I reduces A_H K A_H^T to
K^(1/2)(I-E_H)K^(1/2)=K-R_H/ell. For ell>=2W_*/lambda,
the real square root exists with spectrum in [1/sqrt(2),1], and
the stated norm estimate follows. Positivity of K also implies
positivity of the corrected second matrix. The mixture has total
mass w_H+p_H=1, and its second matrix is precisely ell K, not an
entrywise approximation. All four odd entries are consequently zero.

For each quartic, the added bulk is bounded in absolute value by
(ell^2/w_H)(2M_0)^4=O(ell^2), within its allowed O(ell^3) error,
even when the leading quartic coefficient vanishes. For the clipped
form, the Lipschitz estimate in (19) gives a total bulk error at most
C_Q after multiplication by ell. The rare contribution is nonnegative
and at most W_*/2. Thus

    ell/144-C_Q <= E Q <= ell/144+C_Q+W_*/2.

The common onset in Section 6 includes ell>=288 C_Q, which gives
E Q>=ell/288; it also gives w_H>=1/2, ||A_H||<=2 and the stated
support bound. Each condition is eventually monotone in ell, and the
finitely many source constants are uniform on the same ray of real H.
No small eigenvalue approximation, subsequence or numerical evidence
is used to substitute for any of these inequalities.

**Verdict and limits.** All 21 second and 126 fourth requirements,
positivity of the law, support and the exact clipped coefficient pass.
The sole local mathematical input is L472's bulk, so the existing
L473 DAG row is correct. L471 is downstream motivation only. The
law is not identified with the actual Hardy law and has no asserted
height-process realization. First/cubic constraints, actual clipped
mass, individual-height signs and RH remain unresolved. The imported
arithmetic proofs are not independently audited, and no new formal
coverage claim is made.

## Mathlib

Full matching coverage of the shifted arithmetic inputs, six-coordinate
feasibility statement and clipped statistic has not been checked.
No matching Mathlib theorem is asserted. The exact source citations
are given in Section 1; their applicability, finite-dimensional matrix
arguments and all probability/error calculations are written out above.
Unknown formal coverage is not evidence of absence. The omitted proof
of Bui--Hall Proposition 3 remains an import qualification; Section 8
audits this application's analytic and finite-law steps only.
