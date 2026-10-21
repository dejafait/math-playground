# Lemma 435: the joint log-2/log-3/log-5 cubic cosine data obstruct a positive measure

## Hypotheses

Use the complete actual physical Delta and Bcal, ordinary critical jets,
response and normalization of L406--L409. Write c=1/(4pi),
kappa=17c^3/20160, beta>0 for L409's cubic coefficient,
ell=log H and E_H=H^(-1) integral_[H,2H]. Every v=(j,k,l) in Z^3
is fixed before H tends to infinity through real values. Response
heads N are fixed in their inner height limits. No RH, physical sine
limit, growing-character uniformity, clipping, conditional law,
nonnegative physical product or regulator margin is assumed.

Write num(r) for the reduced numerator of a positive rational r and
A_u=u^(-2) sum_(b=1)^u gcd(b,u). Reuse the audited fixed-rational
interfaces of L434, the multiplicativity in L431 and the prior
SPECIALIZE assessment
`drafts/literature/2026-10-18-three-prime-cubic-density-review.md`.

## Conclusion

For every separately fixed v, put a=2^j 3^k 5^l. Then

    E_H[Delta Bcal cos(t log a)]=g_v ell^2+o_v(ell^2),       (1)
    g_v=(kappa/2) sum_(m,n,q>=1) (mn)^(-2)q^(-3)
          [sqrt(a) A_num(a mn/q)+a^(-1/2) A_num(mn/(a q))]. (2)

The series converge absolutely. The real sequence c_v=g_v/beta is
absolutely summable on Z^3, c_0=1 and c_(-v)=c_v. For p=2,3,5 define

    b_p(d)=1 (d<=0),
    b_p(d)=p^(-d)(1+(1-1/p)d) (d>=1),
    B_p(j)=sum_(s,r>=0)(s+1)p^(-2s-3r)b_p(s-r+j),
    Q_p(u)=p^7(p-1)^2 u^3 /
                   [(u-1)(u-p)^2(p^2u-1)^2(p^3-u)].        (3)

The continuous centrally symmetric signed density, with normalized
Haar measure dh=dtheta dphi dpsi/(2pi)^3, is

    W(theta,phi,psi)=Re[Q_2(sqrt(2)e^(i theta))
                          Q_3(sqrt(3)e^(i phi))
                          Q_5(sqrt(5)e^(i psi))]
                       /[B_2(0)B_3(0)B_5(0)].             (4)

It has integral one and Fourier coefficients c_v. Its log-2/log-3
marginal is exactly L434's positive density. Nevertheless, at the point
specified by

    sqrt(2)e^(i theta_*)=1+i,
    sqrt(3)e^(i phi_*)=1+i sqrt(2),
    sqrt(5)e^(i psi_*)=1+2i,                              (5)

it is strictly negative, hence negative on an open neighborhood.
Consequently no finite positive torus measure has all cosine moments
c_v. This excludes even nonsymmetric measures, through their central
symmetrization. It does not assert an actual physical sine limit or
coordinatewise symmetry.

This is a local REPRODUCTION specialization of assessed analytic and
compact-group tools, with an exact arithmetic sign test; originality
beyond the sources checked is not asserted. The separate step-238
critical audit below validates this scope. The obstruction concerns this entire added character
family only. No actual/global realization, actual clipping, capped
nondegeneracy, full-error regulator margin, extended zeta zero-exclusion
range or RH conclusion is obtained.

## Proof

The prior assessment records the exact known-result comparison,
primary hypotheses and the focused duplicate/failure search. The
positive single- and two-prime results do not sign a three-factor
real part. The earlier narrower law-separation and core/tail stops
remain intact. The new test is the full complex product, rather than
an enlarged finite Toeplitz section.

### 1. Complete physical coefficients at every fixed triple

Fix v and write a=A/B in lowest terms. Its only new prime is 5;
what the analytic argument requires is simply a fixed positive rational.
The fixed-rational proof and separate audit in L434 section 1 apply
with exactly this A,B. The following checks specify that application
rather than asserting a new general moment theorem.

On the real segment multiply L407's exact carrier expansion by
(a^(it)+a^(-it))/2. Single-carrier frequencies are
r=a0 mn/q and zero-carrier frequencies r=a0 mnq, where
a0=a or a^(-1); alpha=(mnq)^(-5/2). Opposite-sign lattice triples
are included because A,B are reduced after forming the whole a.
Continue each character as part of r^(s-1/2); it is not a slow weight
and is never differentiated as one. L407's ordinary-jet signed
coefficients, including phase derivatives, are unchanged.

For each fixed N,r=u/w, gcd(u,w)=1, L408's combined Hurwitz-pole
calculation gives the leading factor sqrt(r) A_u and signed monomial
sum 17/20160. The precise imported input is Fazzari,
*A Voronoi summation formula for the shifted triple divisor function*,
arXiv:2306.15553v1, [(3.5)](https://arxiv.org/html/2306.15553v1#S3),
with additive numerator -w and modulus u and all progression classes.
[DLMF 25.11(i)](https://dlmf.nist.gov/25.11#i) supplies the
residue-one Hurwitz pole; [25.11.5](https://dlmf.nist.gov/25.11.E5)
supplies continuation for positive progression parameter, Re s>0
away from the pole and integer cutoff. Here every parameter b/u
is positive. The finite residue sum is

    u^(-3) sum_(b,d,e=1)^u exp(-2pi i wbde/u)
       =u^(-2) sum_(b=1)^u gcd(b,u)=A_u.

Coprimality permits the sum over e to impose u|bd. L408's
smooth-first absolute endpoint transfer supplies the sharp interval;
a Schwartz-weight formula is not applied directly to an indicator.
Multiplication by alpha sqrt(r) and the character half gives the
finite head of (2). The leading coefficient is real; the real
projection introduces no further half. At a=1 the two halves add.

For completeness, the response-uniform bounds from the audited
fixed-rational interface retain the changed character constants.
Use sigma=21/20, delta=11/20 and eta=1/100. The two connectors cost
C(1+r^delta)H^(71/120) for single carrier and
C(1+r^delta)H^(1/2) for zero carrier. These are L407/L409's
fixed-strip Cauchy specialization of Bourgain,
[arXiv:1408.5794v2, Theorem 5/(0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2).
The positive-frequency kernel is Milinovich--Ng, *Lower bounds for
moments of zeta'(rho)*,
[Lemma 6.1, p. 9](https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9),
for x>0 and abscissa in a fixed compact subset of (0,2], retaining
its complete endpoint-transition error. Its relevant saddle, endpoint
and exterior cases are Gonek, Invent. Math. 75 (1984),
[section 3, Lemma 2, p. 130](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8).
Their inspected primary hypotheses and audited applications are reused.

For total derivative order D<=6, the weighted single-carrier error is

    C[H^(11/20)r^(11/20)
      +H^(1/100)r^(-49/100)(1+log_+r)^D
      +H^(51/100)ell r^(51/100)(1+log_+r)^D].             (6)

This subtracts both H and V primitives, H<=V<=2H, before integration
against the exact weights |w|<=C ell^(-D),
|w'|<=C ell^(-D)/H. Both endpoints and nearest saddles remain.
For r=a0 mn/q and z in these powers or the connector power,

    alpha r^z=a0^z m^(-5/2+z)n^(-5/2+z)q^(-5/2-z).

Every z lies strictly in (-3/2,3/2), so all response sums,
including logarithms, converge. The same open bounds prove normal
convergence on a neighborhood of the shifted rectangle. A fixed a0
only changes constants. The absolute main-sum majorant is

    C_v H ell^2 (mn)^(-2)q^(-3)(1+log m+log n)^8.          (7)

For zero carrier every r lies in h Z, h=1/(AB), and r>=h.
The integer resonances are precisely B|mnq for a0=A/B and
A|mnq for a0=B/A. Retain their r^(-1/2)C_nu(r) weighted
integrals, including r=1. Since
|C_nu(d)|<=C d^(1/100)log(2d)^D, the full resonance sum is O_v(H).
Off resonance, the primitive bound is

    2r^(11/20) sum_(d!=r)|C_nu(d)|d^(-21/20)/|log(r/d)|.

Outside (r/2,2r) it is O(r^(11/20)). Inside use
|log(r/d)|>=|r-d|/(2r), nonzero distance at least h, a
nearest-unit-band cost O(1/h), and harmonic later bands. The result is
O_v(r^(11/20)+r^(51/100)log(2+r)^(D+1)), including h<=r<1.
Both powers are summable against alpha when r=a0 mnq. Weight
variation preserves this O_v(1) nonresonant sum; both connectors
also sum. Thus the complete zero carrier remains O_v(H).

Applied to cube complements, (6)--(7) prove an absolute normalized
signed-tail bound C_v epsilon_N+o_v(1), epsilon_N->0, without
multiplying an already integrated signed error by cosine. The
coefficient tails in (2) also vanish because 0<A_u<=1. Choose N
first for those tails, then H large at that fixed N,v. Finally L406's
absolute physical error O(ell^(5/4)) survives bounded cosine
multiplication and is o(ell^2). This proves (1)--(2) with complete
response derivatives and curvature. No height limit is summed over
characters, and no growing-triple uniformity is used.

### 2. Three valuations, convergence, normalization and marginal

For e>=1 the prime-p residue classes with valuation d<e number
(p-1)p^(e-d-1), and the zero residue contributes p^e to the gcd sum.
Thus A_(p^e)=p^(-e)(1+(1-1/p)e), also valid at e=0. L431's
Chinese-remainder multiplicativity applies to these factors, including
p=5. Let T_30 be L409's sum restricted to m,n,q each coprime to 30.
It is positive and finite, 1<=T_30<=zeta(2)^2 zeta(3).
Unique valuations and nonnegative Tonelli give, with P={2,3,5} and
v_2=j,v_3=k,v_5=l,

    g_v=(kappa T_30/2)
       [product_(p in P) p^(v_p/2)B_p(v_p)
        +product_(p in P) p^(-v_p/2)B_p(-v_p)],
    beta=kappa T_30 product_(p in P)B_p(0).               (8)

The count s+1 records the ordered m,n valuations. The remaining
coprime-to-30 reduced numerator is unchanged by either a or a^(-1),
regardless of shared factors among the remaining indices. Hence the
same T_30 occurs in both terms and beta. This is a product before
central symmetrization, not a product of symmetric marginal moments.

For each of these primes and 1<R<p, the nonnegative change of
variables d=s-r+j in the entire triple sum gives

    sum_(j in Z)B_p(j)R^j
      =[sum_(d in Z)b_p(d)R^d]
                  /[(1-p^(-2)/R)^2(1-R/p^3)]<infinity.   (9)

The negative d tail requires R>1 and positive d tail R<p;
both other geometric sums converge there, also for p=5. This is an
absolute majorant before rearrangement. Differentiated geometric
series then give, locally uniformly on 1<|u|<p,

    sum_d b_p(d)u^d
       =u/(u-1)+u/(p-u)+(p-1)u/(p-u)^2
       =(p-1)^2u/[(u-1)(u-p)^2].                        (10)

Together with the factors in (9) this is Q_p in (3).
All c_v are positive, and (8)--(9), at R=sqrt(p), imply the joint
three-index bound

    sum_(v in Z^3)|c_v|
      =product_(p in P) Q_p(sqrt(p))/B_p(0)<infinity.      (11)

Thus uniform absolute Fourier summation identifies their continuous
signed density as the half-sum of the complex product and its conjugate,
which is exactly (4). Reflection of all three coordinates together
conjugates the product; reflecting a single coordinate need not preserve
it. Since c_0=1 in (8), integration yields mass one without assuming
any sign. Integrating psi keeps v_5=0 and cancels B_5(0), recovering
L434's whole joint density. These operations concern coefficient
series, not an exchange with the physical height limits.

### 3. Full complex sign at an exact point

For u=sqrt(p)e^(it), X=Re u and Y=Im u, set

    A_p=p+1-2X, J_p=p^3+p^(-2)-2X,
    C_p=p^3+1-(p^2+1)X, D_p=(p^2-1)Y.

A_p>0 since its minimum is (sqrt(p)-1)^2. Also J_p>0:
p^3 and p^(-2) are distinct positive numbers of product p,
so their sum exceeds 2sqrt(p). The rational denominator roots
1,p,p^(-2),p^3 all lie off |u|=sqrt(p). The circle identities
proved algebraically in L434 hold for every p here:

    (u-1)(u-p)=-u A_p,
    (p^2u-1)(p^3-u)=p^2u J_p,
    (u-p)(p^2u-1)=u(-C_p+iD_p),
    C_p^2+D_p^2=p^2 A_p J_p.

Consequently the exact full complex value is

    Q_p(u)=p^3(p-1)^2(C_p+iD_p)/(A_p^2 J_p^2).           (12)

This also justifies its new p=5 specialization. For p=2,3,5,
C_p>0 on the entire circle: the three required squared comparisons
are 9^2>5^2*2, 28^2>10^2*3, and 126^2>26^2*5.
Write R_p=Re Q_p>0 and r_p=D_p/C_p. Unlike the two-factor
case, the three-factor real multiplier is

    Re(product_p Q_p)=(product_p R_p)
                         (1-r_2 r_3-r_2 r_5-r_3 r_5).    (13)

At (5), X=1 for all three primes and Y=1,sqrt(2),2.
Thus (C_2,C_3,C_5)=(4,18,100) and

    (r_2,r_3,r_5)=(3/4,4sqrt(2)/9,12/25),
    1-r_2r_3-r_2r_5-r_3r_5
       =1-9/25-41sqrt(2)/75=(48-41sqrt(2))/75.

The rational bounds 7/5<sqrt(2)<10/7 follow by squaring positive
numbers. Therefore the multiplier lies strictly between -74/525
and -47/375, in particular below zero by more than 47/375.
Every R_p/B_p(0) is strictly positive and finite, so W at (5) is
strictly negative. Its continuity, already proved by (11), gives an
open neighborhood with negative W. This is not a sampled sign claim.

### 4. Positive measures, symmetry and the scope of the obstruction

Import the lattice Bochner theorem and compact-torus Fourier uniqueness
from Peter Major, *Multiple Wiener--Ito Integrals, with applications to
limit theorems*, author text dated July 13, 2013, section 3.1,
original-form theorem on
[printed p. 22, PDF p. 30](https://renyi.hu/~major/articles/lecture0.pdf#page=30).
It applies to functions on Z^nu for any finite nu, here nu=3;
Euclidean origin continuity is not a lattice hypothesis. Finite
signed/complex measure Fourier uniqueness is used in its usual compact
torus form. No new Bochner or multivariate factorization proof is needed.

If a finite positive measure mu had all cosine moments c_v,
its mass would be c_0=1. Average mu with its pushforward under
x->-x. The result mu_s is finite positive, has the same cosine
moments and zero sin(v.x) moments for every v. Hence all its
Fourier coefficients equal c_v. Finite-measure uniqueness forces
mu_s=W dh, which contradicts the negative mass of an open subset
where W<0. Thus no such mu exists, with or without initial symmetry.
The signed measure W dh itself is the unique centrally symmetric
finite signed measure with these cosine moments. No uniqueness for
arbitrary nonsymmetric signed measures or actual sine asymptotic is
asserted.

This is an obstruction to a nonnegative mass with exactly the full
normalized coefficient family. It neither rejects L431's selected
finite calibration nor claims that every modified law must fail its
original constraints. No law construction or finite trigonometric
witness is supplied. No actual clipped statistic, physical visit,
regulator margin or RH statement is inferred.

### Exact finite evidence

Run `python3 scripts/discriminant/three_prime_cubic_density.py`.
It writes `scripts/discriminant/three_prime_cubic_density_certificate.json`.
Exact Fraction Laurent arithmetic checks (10), (12) and the modulus
identity at each p=2,3,5: all nine residual polynomials are identically
zero. It evaluates B_p(0) by the geometric constant-term formula of
L434 (17); in particular B_5(0)=603597109375/581483140832.
It checks the exact pair-product multiplier in Q(sqrt(2)), its strict
rational bounds, the point's positive real factors and p=5's global
C comparison. All 19 checks pass, failures=[]. Complete /checks,
/local, /negative_point and /failures were inspected with the shared
JSON inspector. The exact normalized density upper bound is

    W(theta_*,phi_*,psi_*)
       < -2845531063062452632131264/92613754219265544503359375 < 0.

The required threshold is zero. The explicit normalized bound is
corroboration: the proof needs only (12)--(13), the rational sqrt(2)
bounds and positivity of B_p(0). Cleared finite identities alone
would not establish convergence, nonzero denominators or physical
transfer; those are justified separately above and checked in the
independent critical audit below.

### Separate critical audit — 2026-10-18, step 238

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-18-three-prime-density-critical-audit.md`.
It reuses the inspected primary hypotheses and the audited L434
fixed-rational interface, checking its application here. No general
moment or measure theorem is reproved. The audit finds no defect in
(1)--(13), including their fixed-character and sequential-limit scope.
This validates a local known-tool specialization, not a new theorem
beyond the checked sources or the missing RH positivity assertion.

**Physical transfer.** Fix the entire triple before reducing a=A/B.
Mixed signs create no new analytic hypothesis: both A/B and B/A are
fixed positive rationals. The identity Re(V)cos(t log a)=
Re(V a^(it)+V a^(-it))/2 applies to each exact carrier in L407.
Holomorphic continuation includes the character in r^(s-1/2),
preserving the exact ordinary-jet coefficients and their slow-weight
derivative estimates. In particular no extra log a derivative term
or extra half from the outer real projection is introduced.

For r=u/w reduced, coprimality makes the third finite residue sum
vanish unless u divides the product of the other two classes. All
classes, including zero and nonunits, remain. The coefficient is A_u,
also at u=1. L408's eight signed factorial contributions, in units
of 1/20160, are 420,-840,336,-56,336,-224,48,-3; they sum to 17.
The exact leading weights with zero coefficients retain their lower
order errors. Multiplication by alpha sqrt(r)/2 yields precisely
(2), and at a=1 the two identical halves restore L409's beta.
L408's absolute smooth-first endpoint comparison is unchanged for
these modulus-one additive phases, so both sharp endpoints are covered.

For single carrier the response power exponents are
-5/2+z,-5/2+z,-5/2-z. At z=11/20,-49/100,51/100 they are
all strictly below -1, as are the connector exponents. Fixed
logarithmic factors do not spoil summability. A small neighborhood
of the contour rectangle retains this strict inequality, justifying
normal convergence before contour integration. The complete kernel
estimate includes the nearest saddles and both H,V endpoints;
integration against the exact weight costs at most C ell^(-D).
The largest connector height exponent is 71/120<1. These errors
are o_v(H ell^2), uniformly for subsets of response tuples.

For zero carrier the common grid h Z with h=1/(AB) includes both
characters and every integer. Resonance occurs exactly under B|mnq
or A|mnq, respectively; its amplitude is r^(-1/2)C_nu(r),
not r^(11/20)C_nu(r). Its response sum is O_v(H), including r=1.
For nonresonant terms in r/2<d<2r, the first distance band costs
O(1/h) and the remaining bands give a harmonic sum. The resulting
power is 11/20+1+1/100-21/20=51/100. Outside this range the
logarithmic denominator is at least log 2. The fixed lower bound
r>=h covers the small-r cases. Both resulting powers are summable
against alpha for the product pattern, giving O_v(1) after weight
variation, besides the resonances and connectors.

The absolute main-sum bound (7) has a vanishing cube-complement
tail. Thus choose N to control that tail and the coefficient tail
in (2), then H large for this fixed N,v. This is not multiplication
of an integrated signed error by a cosine. L406 supplies precisely
the absolute physical error needed for that final multiplication,
O(ell^(5/4))=o(ell^2), with complete response derivatives and
curvature. No infinite character sum is interchanged with H->infinity.

**Joint density and normalization.** The prime-power gcd formula
follows by counting every valuation class and the zero class. CRT
then separates all three valuations from the same coprime-to-30
reduced numerator, even when the remaining indices share factors.
Nonnegative Tonelli gives (8); s+1 counts ordered numerator valuations.
The unchanged positive factor T_30 cancels from c_v. In (9) the
bijective substitution j=d-s+r produces factors
(1-p^(-2)/R)^(-2) and (1-R/p^3)^(-1). Both tails of b_p(d)R^d
converge for 1<R<p, including p=5. Hence this is an absolute
majorant preceding the complex identity, and inner/outer radii give
local uniform convergence. Substitution R=sqrt(p) proves the full
joint bound (11), rather than only separate convergence in each index.

Consequently W=sum_v c_v exp(i v.x) uniformly and absolutely.
Since c_(-v)=c_v, either Fourier sign convention gives coefficients
c_v. The constant coefficient is one before any sign claim. Integrating
psi retains l=0, cancels B_5(0) and gives exactly the audited L434
density. Central reflection conjugates all factors together; replacing
the real part of the product by a product of real parts is invalid.

**Complete sign and finite evidence.** The denominator roots lie
strictly off each circle, and A_p,J_p are positive by the stated
strict inequalities. The four circle identities therefore license
division and give the plus sign in C_p+iD_p in (12). Each C_p is
positive on its circle by the three squared comparisons in section 3.
The selected points have exactly modulus sqrt(p), and their ratios
are 3/4,4sqrt(2)/9,12/25. Expanding the full three-factor product
retains all three negative pair products; the triple imaginary term
has zero real part. The multiplier is (48-41sqrt(2))/75, with
strict bounds -74/525 and -47/375. Multiplication by the positive
real factors preserves both inequalities.

Read the complete algebra script, replayed it and inspected /checks,
/failures, /negative_point and each of /local/2, /local/3, /local/5
in full through the shared JSON inspector. All 19 checks pass with
no failures. The records include all numerator and denominator
coefficients and all nine identically zero Laurent residuals.
The B_p(0) formula was checked separately by splitting d=s-r at
zero: its weights are p^(-2d)(1+(1-p^(-5))d)/(1-p^(-5))^2
for d>=0 and p^(-3h)/(1-p^(-5))^2 for d=-h<0. Multiplying
by b_p(d) and summing gives the formula used by the script and the
stated p=5 value. Thus its normalization is justified by convergent
sums, not inferred from the cleared residuals. The exact density
upper bound printed above is strictly below the required zero threshold.

**Measure obstruction and limits.** Continuity and W(x_*)<0 give
a smaller open neighborhood on which W<=W(x_*)/2<0; its Haar
measure is positive. A hypothetical positive measure with the cosine
data has mass one. Central symmetrization preserves those data and
annihilates every sine character, giving all Fourier coefficients c_v.
The imported finite-measure uniqueness theorem on the compact torus
then identifies it with W dh, contradicting that neighborhood's
negative mass. Initial symmetry and actual physical sine limits are
unnecessary. Uniqueness is asserted only after central symmetrization.

The audit changes no direct mathematical input or argument, so DAG.md
and the PROOF.md assembly are unchanged. It validates this full-family
compatibility obstruction; no finite trigonometric witness or new law
was constructed. L431's selected finite calibration and the positive
L434 marginal remain intact. Actual/global realization, actual clipping,
capped nondegeneracy, L413's full-error regulator margin and global
mixed positivity remain unresolved.

## Mathlib

Full matching coverage for the physical three-prime cubic, the signed
torus density or this specialization has not been checked. The precise
primary references and audited analytic interfaces above are the
mathematical inputs. Unknown Mathlib availability is not absence.
The finite certificate is exact rational corroboration, not a Lean proof.
