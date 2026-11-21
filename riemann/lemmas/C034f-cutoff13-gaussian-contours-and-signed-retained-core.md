# Corollary C034f: cutoff13 Gaussian contours with a signed retained core

## Hypotheses

Use C034d's functions and all its qualifications. Explicitly,

    G_sigma(v)=(4*pi*sigma)^(-1/2)*exp(-v^2/(4*sigma)),
    p(v)=(1/2)*sum_rho[G_sigma(v-z_rho)+G_sigma(v+z_rho)],
    z_rho=gamma_rho-i*delta_rho,
    Q_j(v)=4*j*(3*v^2+j)/(v^2*(v^2+j)^2), j=1,2,
    d_j=int_0^infinity (p(x)-p(0))*Q_j(x) dx,
    e_j=int_0^infinity (p''(x)-p''(0))*Q_j(x) dx,
    C=d_1*e_2-d_2*e_1,
    K(z,w)=[Q_1(z)Q_2''(w)+Q_1(w)Q_2''(z)
                      -Q_2(z)Q_1''(w)-Q_2(w)Q_1''(z)]/2.

Primes here are spatial complex derivatives. The nonempty actual
positive-ordinate divisor includes every multiplicity and conjugate,
gamma>14, |delta|<1/2 and N(T)=O(T log(T+2)). Sigma is Gaussian
half-variance in [1,2]; all estimates below are uniform on I=[1/2,3].
Retain the excluded ordinate zero, verified zeros through100, retained
real zero in (14,15), reciprocal-square tail, heat positivity and
separate fixed-j errors, both fixed-v1 source qualifications, zero
drift/killing, and C033w's probability interpretation through C034b.
Their source-wide/finite-zero validity is not independently verified.
Only the explicit divisor assumptions, C032n's Gaussian estimates,
C034d's real identities and audited C034e's product-strip sign enter
the contour argument. No RH, positive real profile or global Sobolev
membership is assumed.

## Conclusion

Set a=13. Index BOTH translates by nu=(rho,epsilon), epsilon in {+1,-1},
without altering multiplicities, and define

    c_nu=epsilon*gamma_rho, b_nu=-epsilon*delta_rho,
    eta_nu(x)=x+i*b_nu,                  x>=a,
    xi_nu(u)=a+i*b_nu*u,                 0<=u<=1,
    h_nu(x)=G_sigma(x-c_nu)>0,
    v_nu(u)=i*b_nu*G_sigma(a-c_nu+i*b_nu*(u-1)).

For F=Q_1,Q_2,Q_1'',Q_2'', define

    H[F]=(1/2)*sum_nu int_a^infinity h_nu(x)*F(eta_nu(x)) dx,
    V[F]=(1/2)*sum_nu int_0^1 v_nu(u)*F(xi_nu(u)) du.

Then, with absolutely convergent sums and integrals,

    int_a^infinity p(x)*F(x) dx = H[F]+V[F].                 (47)

In particular no connector at a is dropped. The signed finite-side
factor i*b_nu is part of V, including when b_nu<0 or b_nu=0.
Define the following four TWO-VARIABLE expressions independently:

    B_HH=(1/4)*sum_(nu,mu) int_a^infinity int_a^infinity
       h_nu(x)*h_mu(y)*K(eta_nu(x),eta_mu(y)) dy dx,
    B_HV=(1/4)*sum_(nu,mu) int_a^infinity int_0^1
       h_nu(x)*v_mu(u)*K(eta_nu(x),xi_mu(u)) du dx,
    B_VH=(1/4)*sum_(nu,mu) int_0^1 int_a^infinity
       v_nu(u)*h_mu(y)*K(xi_nu(u),eta_mu(y)) dy du,
    B_VV=(1/4)*sum_(nu,mu) int_0^1 int_0^1
       v_nu(u)*v_mu(t)*K(xi_nu(u),xi_mu(t)) dt du.           (48)

Every ordered divisor pair, diagonal pair and sign combination is
present. Each expression is uniformly absolutely convergent on I and
real. Moreover B_HH<0 at every width. The sign does not require mu to
be the conjugate of nu. Although B_HV=B_VH by symmetry, both are kept
in the formula to exhibit all side combinations.

Here are the exact remaining origin and cutoff terms:

    U_j=int_a^infinity p Q_j, W_j=int_a^infinity p Q_j'',
    alpha_j=int_0^a (p-p(0))*Q_j-p(0)*int_a^infinity Q_j,
    beta_j=int_0^a (p''-p''(0))*Q_j-p''(0)*int_a^infinity Q_j
                               -p'(a)*Q_j(a)+p(a)*Q_j'(a),
    R_a=U_1*beta_2-U_2*beta_1+alpha_1*W_2-alpha_2*W_1
                                      +alpha_1*beta_2-alpha_2*beta_1.

All these quantities and their expanded independent divisor products
are uniformly absolutely convergent. At the singular origin, an
individual divisor member retains its even pair of translates; this
does not assert separate integrability of the two origin-subtracted
single translates. The resulting identity is

    C = B_HH+B_HV+B_VH+B_VV+R_a,                          (49)
    C < Omega_sigma:=B_HV+B_VH+B_VV+R_a.                  (50)

This is the partial result of attempt1855, passing independent
conceptual audit1857 below. It constructs the approved signed core and full
residual; it does NOT bound Omega_sigma by S4^3/5, where
S4=sum_rho gamma_rho^(-4). Such a bound would suffice for C034c(20),
but is stronger than needed because it discards the negative core.
No final-prefix sign, ECT, conditioning, exact weights, TV<=2,
full observation matching, signed-height cancellation or actual-Xi
realization is concluded. This is not a complete RH candidate.

## Proof

### Imported tools and target-specific work

Reuse the pre-invocation EXPLORE assessment1854 and its source review
`drafts/literature/2026-11-20-laplace-retained-core-source-notes-1854.md`.
The exact standard inputs are Friedrich Haslinger, *Complex Analysis*,
Section2.2, Theorem2.5/Corollary2.6, printed pp45-48,
[primary notes](https://www.mat.univie.ac.at/~has/scriptneu.pdf), for
zero integrals around finite closed paths in a convex holomorphy
domain; and John K. Hunter, *Measure Theory*, Section5.6,
[Theorem5.18/Example5.19, p61](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch5.pdf),
for complex Fubini and absolute double series. For limits use Hunter,
Section4.5, Theorem4.24 and Section4.6's complex-valued extension,
[pp49-50](https://www.math.ucdavis.edu/~hunter/measure_theory/measure_notes_ch4.pdf).
The statements and available relevant proof cases were inspected in
the saved review; the general theorems are imported, not reproved.

Counting measure on the divisor and Lebesgue measure on the real
side parameters are sigma-finite. The integrands below are measurable,
indeed continuous in their real variables. The estimates supplied
below verify absolute integrability and a single width-independent
dominator before those theorems are applied. The specialization is
the member-dependent contours, their simultaneous divisor limits,
the signed weights and exact origin/cutoff bookkeeping. No known
general contour theorem supplies these checks or a residual sign.
C034d's real identity and C034e's audited sign are reused without
reproving their algebra. No claim of originality follows from the
saved search's failure to locate this precise representation.

### Finite rectangles, with both orientations

Fix nu, M>a and one of the four rational F. Write
g_nu(z)=G_sigma(z-c_nu-i*b_nu). Its product with F is holomorphic
on the convex open half-plane Re z>12: all poles of F lie at
0 or +/-i*sqrt(j). The whole rectangle with vertices a,M,M+i*b_nu,
a+i*b_nu lies in that open set. Cauchy's theorem applies without
an exceptional point, pole crossing or origin regularization.

Parameterize the lower and far vertical paths upward by their signed
heights, so the same formula includes negative b_nu. If b_nu=0,
both connectors are zero and the identity is tautological. In general,

    int_a^M g_nu(x)*F(x) dx
      = int_a^M h_nu(x)*F(eta_nu(x)) dx
           + int_0^1 v_nu(u)*F(xi_nu(u)) du
           - int_0^1 v_(nu,M)(u)*F(M+i*b_nu*u) du,        (51)
    v_(nu,M)(u)=i*b_nu*G_sigma(M-c_nu+i*b_nu*(u-1)).

Indeed the closed path a->M->M+i*b_nu->a+i*b_nu->a
has integral real+far-horizontal-lower=0. On its horizontal side
g_nu(x+i*b_nu)=G_sigma(x-c_nu), exactly, with no phase factor.
This argument treats negative-center translates c_nu<0 as well as
positive-center translates; neither is discarded.

For fixed complex w on another such contour, K(z,w) is holomorphic
in z on the same half-plane, and conversely in w. Thus (51) may be
applied successively in both variables of a finite divisor sum.
Calling the horizontal, lower and far functionals H,V,F_far, this
finite expansion is

    HH+HV+VH+VV-HF_far-F_farH-VF_far-F_farV+F_farF_far. (52)

There are nine terms, including both signs of the far connectors.
No cancellation or sign is used to justify a term's limit.

### Uniform majorants for all sides and independent pairs

For z=x+i*t, x>=a, |t|<=1/2, put r=j/|z|^2<=2/169<1/80.
Then |z^2+j|>=(1-r)|z|^2>(19/20)|z|^2. In particular the
denominators are bounded away from zero on these paths. The explicit
Q_j and C034d(34)'s rational expression for Q_j'' give

    |Q_j(z)| <= 8*(13/4)*(20/19)^2*x^-4 <32*x^-4,
    |Q_j''(z)| <=48*11*(20/19)^4*x^-6 <800*x^-6.        (53)

Here 3+r<13/4 and 10+5r+4r^2+r^3<11. The displayed integer
bounds follow respectively from 10400<32*361 and
84480000<800*130321. Thus, for independent z=x+i*t,w=y+i*s
in the strip,

    |K(z,w)|<=25600*(x^-4*y^-6+x^-6*y^-4).            (54)

For sigma in I and real q with |q|<=1/2, the exact Gaussian formula
gives

    |G_sigma(X+i*q)|
      <=(2*pi)^(-1/2)*exp(1/8)*exp(-X^2/12)
      <=2*exp(-X^2/24).                               (55)

The imaginary differences on every vertical side in (51) are
b_nu*(u-1), of modulus at most1/2. The real path has imaginary
difference -b_nu, and the shifted horizontal has difference zero.
Consequently (55) controls every one of these cases uniformly in
nu, b_nu and sigma, not just each fixed translated Gaussian.

Use exactly C032n's envelope

    P(x)=sum_rho[exp(-(x-gamma_rho)^2/24)
                        +exp(-(x+gamma_rho)^2/24)].

C032n(9) proves int_1^infinity P(x)*x^-2 dx<infinity, and
its counting argument for (13) gives
P(x)=O((x+1)log(x+2)), x>=1. The latter argument is an absolute
sum estimate: at gamma<=2x+2 bound each exponential by1; beyond
that cutoff use exp(-gamma^2/96), whose divisor sum is finite.
It does not rely on cancellation in p. Also P(a)<infinity.

For m=4,6 define the width-independent numbers

    H_m=2*int_a^infinity P(x)*x^-m dx <infinity,
    V_m=a^-m*P(a)<infinity,
    F_m(M)=M^-m*P(M)=O(M^(1-m)*log(M+2))->0.           (56)

Before the factors1/2 in the definitions of H,V are taken, H_m
bounds the sum of the absolute horizontal weights integrated against
x^-m. V_m bounds the analogous lower connector sum, since
|i*b_nu|<=1/2 in (55). F_m(M) bounds the corresponding far-side
sum. Real paths have the same majorant as H_m. These bounds also
hold for any finite divisor truncation and for finite horizontals.
They are sums of explicit pointwise nonnegative Gaussian majorants,
not merely independent bounds for the final signed integrals.

For X,Y in {H,V,F_far}, the absolute sum of the corresponding
two-variable K integral, INCLUDING its factor1/4, is at most

    6400*(X_4*Y_6+X_6*Y_4),                           (57)

where X_m,Y_m mean (56). This is a direct consequence of (54),
Tonelli on its nonnegative product majorant, and (55). It treats
every independent nu,mu; no conjugate restriction, diagonal deletion,
matched imaginary shift or member-dependent cancellation is used.
It also proves absolute convergence of each product of the four
one-variable rational integrals in (47).

In particular the four terms of (48) are uniformly absolutely
summable and integrable. Every term of (52) containing a far side
tends uniformly to zero after the FULL divisor summation: its bound
contains F_4(M)=O(M^-3 log M) or F_6(M)=O(M^-5 log M), while
the other factor is bounded or tends to zero. This explicitly covers
centers with gamma near M, where memberwise Gaussian decay is not
a uniform argument. The double-far term is also bounded by (57).

For a formal limiting order, first truncate at gamma<=N, retaining
all multiplicities, both translates and conjugates. Apply (51)-(52)
to finite sums and finite paths. At fixed M, the compact Gaussian
majorants and (57) permit N->infinity by complex dominated
convergence and Fubini. Then let M->infinity: horizontal truncations
have the common integrable majorants H_m, the lower sides are fixed,
and the summed far sides vanish by (56)-(57). The same real-path
majorants identify the limit of the original integrals. This proves
(47), all four absolute expressions (48), and

    int_a^infinity int_a^infinity p(x)*p(y)*K(x,y) dy dx
                           =B_HH+B_HV+B_VH+B_VV.       (58)

Uniformity on I follows from the same fixed majorants and vanishing
far-side bounds. Continuity in sigma, including at widths1 and2,
also follows by dominated convergence. No derivative of an inequality
or nonabsolute divisor rearrangement has entered.

### Reality and the retained sign

The divisor involution rho->bar(rho) fixes gamma and negates delta,
with every multiplicity retained. On nu=(rho,epsilon), it fixes
c_nu and replaces b_nu by -b_nu. Thus h_nu is unchanged,
eta_nu and xi_nu are conjugated, and v_nu is conjugated as well:
the conjugate of i*b_nu is -i*b_nu. Every Q_j and its derivatives
have real coefficients. Absolute convergence therefore permits this
involution in the one-variable sums and simultaneously in the two
independent indices of (48). Each sum equals its complex conjugate.
This proves its reality; it does not reduce the pair sum to conjugate
pairs. Symmetry of K and Fubini give B_HV=B_VH.

For B_HH, both kernel arguments have real part at least13 and
imaginary part of modulus at most1/2. C034e(36) applies to those
arguments independently and gives Re K<0. The two h weights are
positive real numbers, so every real part of a horizontal-horizontal
integrand is strictly negative. Absolute convergence permits taking
real parts under the integrals and the complete pair sum. At least
one nu,mu pair exists; its integral over any fixed nondegenerate
compact rectangle in [13,infinity)^2 is strictly negative by
continuity. All other real contributions are nonpositive. Therefore
the real number B_HH is strictly negative. This reasoning also covers
b_nu=0 and either sign of each b; it assumes no positivity of p(x).
No analogous sign follows for a connector's complex weight v_nu.

### Exact origin terms and the relocation from cutoff1

C034d already proves d_j=int(p-p(0))Q_j and
e_j=int(p''-p''(0))Q_j as ordinary absolutely convergent integrals.
Split them at a. Integrate p''Q_j by parts twice only on [a,M];
the far pairing p'(M)Q_j(M)-p(M)Q_j'(M) tends to zero by
C032n(13) and rational decay. The resulting formulas are exactly

    d_j=U_j+alpha_j, e_j=W_j+beta_j.                    (59)

The lower pairing is -p'(a)Q_j(a)+p(a)Q_j'(a), with the signs
in the conclusion. The constants -p(0)int_a^infinity Q_j and
-p''(0)int_a^infinity Q_j remain, as do the subtracted integrals
over [0,a]. Near zero, evenness gives p-p(0)=O(x^2) and
p''-p''(0)=O(x^2), with summable memberwise derivative majorants
from C032n(8). Since Q_j=O(x^-2), these origin integrals converge
absolutely before divisor summation. On [1,a] compact Gaussian
majorants apply; origin values and traces at a also have absolutely
summable member bounds. The tails in (59) have (56)'s majorants.
All products of these finite absolute sums converge, including every
independent origin, trace and tail cross term in R_a.

There is no integral of pQ_j'' through zero in this proof. C034d's
quadratic subtraction V(x)=p(x)-p(0)-p''(0)*x^2/2 was essential
for its alternate transfer through zero; here the equivalent original
subtraction p''-p''(0) is retained throughout [0,a]. No divergent
origin term has been separated, assigned a finite part or deformed.

To make the relation to C034d's ORIGINAL bulk explicit, distinguish
its cutoff1 quantities by superscript (1) and put

    L_j=int_1^a p Q_j, M_j=int_1^a p Q_j'',
    J_a=L_1*W_2-L_2*W_1+U_1*M_2-U_2*M_1
                                      +L_1*M_2-L_2*M_1.

Then U_j^(1)=U_j+L_j, W_j^(1)=W_j+M_j. Direct subtraction of
the definitions gives alpha_j=alpha_j^(1)+L_j. Integrating by
parts on [1,a], with BOTH finite endpoint pairings, similarly gives
beta_j=beta_j^(1)+M_j. All these are convergent compact-interval
identities. Expanding their products proves

    B_1:=int_1^infinity int_1^infinity p(x)*p(y)*K(x,y) dy dx
          = B_HH+B_HV+B_VH+B_VV+J_a,
    R_a=R_1+J_a.                                      (60)

Thus the entire cutoff1-to13 relocation, including both mixed
rectangles and the [1,13]^2 square, is retained. Finally (59)
gives C=U_1W_2-U_2W_1+R_a. Symmetry and absolute Fubini identify
U_1W_2-U_2W_1 with the left side of (58), proving (49)-(50).

### Achieved result and remaining threshold

The representation succeeds at the stated test: all Gaussian weights
in B_HH are nonnegative, C034e signs its full independent product
strip, every side has an absolute majorant, the far-side sums vanish
uniformly, and (60) retains the origin/cutoff accounting. This removes
the need to assume a positive spatial profile when signing that core.

The residual Omega_sigma in (50) has no proved sign or upper bound
at S4^3/5. Constants (53)-(57) prove integrability and limits only;
they are not a payment of the curvature budget. A later quantitative
comparison must be separately assessed and must preserve all three
connector terms and R_a, or exploit their exact combination with the
negative core. Stops1847/1843/1839 and the older recorded evidence
remain valid for their respective mechanisms. This specialization
does not itself reopen closure by the old real identity alone.

### Conceptual audit1857 — 20 November 2026

The exact statements (47)-(60) pass under the unchanged EXPLORE
assessment1855, separately approved1856. This validates the existing
representation and its limited strict inequality; it adds no residual
estimate or new theorem beyond that representation. The standard
Cauchy, complex Fubini and dominated-convergence inputs cited above
are reused with their recorded source qualifications. No new source,
finite-zero validation or global operator-domain premise is used.

**Finite contours and normalization.** For either sign of b, integrate
g_nu F along a to M, M to M+i*b, M+i*b to a+i*b, and a+i*b to a.
The four integrals are respectively real, far, minus horizontal, and
minus near. Their sum is zero because the whole rectangle is in
Re z>12, while every rational pole has real part zero. Thus real =
horizontal + near - far, even when the traversal is clockwise.
For b=0 both vertical integrals vanish. The identity
g_nu(x+i*b)=G_sigma(x-c_nu) leaves no complex phase, for c_nu of
either sign. The near weight is precisely i*b times the stated
Gaussian, with the same signed i*b on the far side. Replacing b by
|b| would be incorrect.

Applying this finite identity successively to each variable of K
gives (H+V-F_far) in each variable. It produces exactly the nine
terms in (52), with four negative mixed far terms and one positive
double-far term. The divisor convention contributes (1/2)^2=1/4;
the separate symmetrization factor1/2 is already in K. Neither
diagonal pairs nor negative-center translates disappear. Fixed
second-variable arguments also lie in the pole-free half-plane,
so the successive Cauchy applications have the required holomorphy.

**Absolute independent-pair bounds.** For j<=2 and |z|>=x>=13,
r=j/|z|^2<=2/169<1/80 and |z^2+j|>(19/20)|z|^2.
The numerator in Q_j is at most 4j(3+r)|z|^2. Factoring |z|^6
from the numerator in C034d(34) bounds the numerator polynomial
there by 10+5r+4r^2+r^3<11. Consequently (53) reduces to

    26*(20/19)^2<32, 528*(20/19)^4<800.

Their integer comparisons are exactly the two displayed in (53).
Taking absolute values of all four terms of K, without cancellation,
then yields (54). The Gaussian modulus is

    (4*pi*sigma)^(-1/2)*exp(-X^2/(4*sigma)+q^2/(4*sigma)),

which gives (55) for sigma in [1/2,3] and |q|<=1/2. The actual
imaginary differences on real, horizontal and vertical paths are
-b, 0 and b(u-1), respectively; all meet that bound.

Before the factor1/2, horizontal absolute densities summed over nu
are bounded pointwise by 2P(x), and near/far connector absolute
densities are bounded pointwise by P(a) and P(M). Multiplication by
the real-coordinate powers gives exactly H_m,V_m,F_m in (56).
C032n(9) gives integrability, and its counting proof of (13) bounds
P(M) itself, not merely the possibly cancelling profile p(M).
Tonelli on these nonnegative densities gives (57) for two independent
indices and side parameters. It also bounds each unsymmetrized
rational product separately, as required for complex Fubini.

In particular the five far-containing bounds can be written

    |HF_far|,|F_farH| <=6400*(H_4 F_6+H_6 F_4),
    |VF_far|,|F_farV| <=6400*(V_4 F_6+V_6 F_4),
    |F_farF_far|     <=12800*F_4 F_6.

Here absolute values denote the corresponding absolute pair integrals
after summing the full divisor. The first four bounds are
O(M^-3 log(M+2)); the last is O(M^-8 log^2(M+2)). They vanish
uniformly in width and include arbitrarily many centers near M.
At fixed M the Gaussian compact dominators permit passage from finite
divisors to the whole divisor. Subsequently the horizontal truncations
converge by the fixed integrable product dominators, the near sides
are fixed, and the above far bounds vanish. These are exactly the
two limiting steps used in (47) and (58); no memberwise far limit is
substituted for a summed limit. The same majorants give continuity
in sigma, including the endpoints1 and2.

**Reality and strict core sign.** The involution (c,b)->(c,-b)
conjugates eta and xi and also v: the latter uses both
conjugate(i*b)=-i*b and the real coefficients of the Gaussian.
Applying this involution independently to the two summed indices
conjugates each entire expression in (48), proving that it is real.
It is a bijection of all ordered pairs, not a restriction to pairs
of conjugate members. Symmetry gives B_HV=B_VH by absolute Fubini.

Both arguments of every HH kernel satisfy C034e's independent closed
product-strip hypotheses. Its real part is strictly negative and
both multiplying Gaussians are strictly positive. Choose any one
ordered pair in the nonempty divisor and a compact rectangle of
positive area inside [13,infinity)^2. Continuity gives a strictly
negative integral for that pair there, while the real parts of all
remaining contributions are nonpositive. Absolute convergence then
proves B_HH<0, without a uniform negative constant or a sign for p.
This checks the sole strict sign needed to deduce (50) from (49).

**Origin grouping and both cutoff endpoints.** For this check use
the complex even member

    t_rho(x)=[G_sigma(x-z_rho)+G_sigma(x+z_rho)]/2.

Conjugation makes sum t_rho equal the real p. By C032n(8) and the
counting hypothesis, for k=2,4 the constants

    M_k=sum_rho sup_(sigma in I, 0<=x<=1)|t_rho^(k)(x)|

are finite. Evenness gives t_rho'(0)=t_rho'''(0)=0. Taylor's integral
remainders therefore yield

    sum_rho |t_rho(x)-t_rho(0)|<=M_2*x^2/2,
    sum_rho |t_rho''(x)-t_rho''(0)|<=M_4*x^2/2.

These are the required summable majorants against Q_j=O(x^-2).
On [1,13] compact derivative bounds apply; origin values and cutoff
traces have summable bounds as well. This verifies the intended
absolute expansion of alpha and beta over rho. Splitting an even
member into separately integrated origin-subtracted single translates
would lose this x^2 estimate and is neither needed nor asserted.
Away from zero the individual nu-indexed translates remain separately
integrable, exactly as used in (47)-(48). Products of the finite
absolute linear sums cover every independent origin/trace/tail pair.

Define E_j(x)=p'(x)Q_j(x)-p(x)Q_j'(x). On [a,M], twice integrating
by parts gives

    int_a^M p'' Q_j=E_j(M)-E_j(a)+int_a^M p Q_j''.

C032n(13) and rational decay imply E_j(M)->0 uniformly; its two
terms have bounds O(M^-3 log M) and O(M^-4 log M). Splitting the
original subtracted integrals at a now gives exactly (59), including
-p(0)int_a^infinity Q_j, -p''(0)int_a^infinity Q_j and -E_j(a).
No origin value or divergent integral is discarded.

For relocation from1 to a, direct subtraction gives
alpha_j-alpha_j^(1)=L_j. For beta the difference is

    beta_j-beta_j^(1)=int_1^a p'' Q_j-E_j(a)+E_j(1)=M_j.

Thus both finite endpoint pairings cancel in exactly the way claimed.
Using U^(1)=U+L and W^(1)=W+M, subtraction of the two bulk
determinants gives precisely

    L_1 W_2-L_2 W_1+U_1 M_2-U_2 M_1+L_1 M_2-L_2 M_1=J_a.

The common determinant C equals B_1+R_1 and equals B_a+R_a.
Since B_1-B_a=J_a, it follows that R_a=R_1+J_a, with the plus
sign in (60). Substitution of (58) proves (49). This completes the
audit of every displayed correction and limit without changing a
formula or adding a mathematical dependency.

The audited identity supplies no estimate of Omega_sigma at S4^3/5,
nor of its combination with the negative core. No claim of C034c(20),
final-prefix nonvanishing, conditioning, full observations or actual-Xi
positivity follows. Stops1839/1843/1847 and older limitations remain.
Full matching Mathlib coverage and all inherited external-source
qualifications remain outside this conceptual verdict.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is used or claimed absent. General Cauchy, product integration and
dominated-convergence support may exist; no matching formal theorem
for these member-dependent half-line contours, full divisor limits,
cutoff corrections and retained sign has been verified. Conceptual
audit1857 validates the qualified analytic representation, not a formal
Mathlib theorem; all inherited source qualifications remain in force.
