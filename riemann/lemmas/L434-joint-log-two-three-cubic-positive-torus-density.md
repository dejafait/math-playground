# Lemma 434: the joint fixed log-2/log-3 cubic data have a positive torus density

## Hypotheses

Use the actual complete physical Delta and Bcal and the ordinary jets,
response, phase and normalizations in L406--L409. Put c=1/(4pi),
kappa=17c^3/20160, ell=log H, E_H=H^(-1) integral_[H,2H], and
let beta>0 be L409's complete cubic coefficient. Each v=(j,k) in Z^2
is fixed before taking the real-H limit. Every response head N is
fixed in its inner height limit. No RH, actual sine limit, growing
frequency uniformity, conditional law, clipping or margin is assumed.

Write num(r) for the reduced numerator of a positive rational r and
A_u=u^(-2) sum_(b=1)^u gcd(b,u). The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-joint-two-prime-cubic-density-attempt.md`.
Its fixed-positive-rational and lattice-measure coverage is reused.

## Conclusion

For every separately fixed v=(j,k), set a=2^j3^k. Then

    E_H[Delta Bcal cos(t log a)]=g_v ell^2+o_v(ell^2),       (1)
    g_v=(kappa/2) sum_(m,n,q>=1) (mn)^(-2)q^(-3)
         [sqrt(a) A_num(a mn/q)+a^(-1/2) A_num(mn/(a q))].  (2)

These sums converge absolutely. Put c_v=g_v/beta. The whole sequence
(c_v)_(v in Z^2) is absolutely summable, c_0=1 and c_(-v)=c_v.
Define, for p=2,3,

    b_p(d)=1 (d<=0),
    b_p(d)=p^(-d)(1+(1-1/p)d) (d>=1),
    B_p(j)=sum_(s,r>=0)(s+1)p^(-2s-3r)b_p(s-r+j),
    Q_p(u)=p^7(p-1)^2 u^3 /
                 [(u-1)(u-p)^2(p^2u-1)^2(p^3-u)].          (3)

With normalized Haar measure h=dtheta dphi/(2pi)^2, the continuous
probability density

    W(theta,phi)=Re[Q_2(sqrt(2)e^(i theta))
                     Q_3(sqrt(3)e^(i phi))]/[B_2(0)B_3(0)] (4)

has Fourier coefficients c_v under the convention integral e^(-iv.x).
It obeys, on the entire torus,

    W(theta,phi)>1/194400>0.                               (5)

Its log-2 marginal is exactly L433's density. It is the unique finite
centrally symmetric measure with all the specified cosine moments;
uniqueness among arbitrary nonsymmetric measures is not asserted.
Every finite difference matrix (c_(v_a-v_b)) for distinct lattice
indices is positive definite.

This stops the joint two-prime cosine family as a positive-measure
obstruction. The separate step-234 critical audit below validates the
stated scope. It constructs no
law meeting other selected constraints and evaluates no actual sine
coefficient or clipped statistic. Actual/global realization, capped
nondegeneracy, L413's full-error regulator margin and global mixed
positivity remain unresolved. This is a local REPRODUCTION of assessed
analytic and harmonic-analysis tools with an arithmetic specialization,
not a claim of originality beyond the sources checked or an RH result.

## Proof

The saved step-230 comparison supplies the focused duplicate/failure
check and the inspected primary hypotheses. L433 settles a marginal
only; L427/L428/L430's narrower stops and the harmonic-four stop are
preserved. No increase of a finite-minor cutoff is used. The changed
obligations are the fixed-pair physical passage, joint bilateral
summability and sign of the product's real part.

### 1. Every fixed pair, including opposite-sign indices

Fix v and write a=A/B with coprime positive integers A,B. Multiplying
L407's exact real carrier expansion by cos(t log a) inserts the two
characters a^(it),a^(-it), each with coefficient 1/2. For
alpha=(mnq)^(-5/2), the single-carrier twists become r=a0 mn/q and
the zero-carrier twists r=a0 mnq, a0 in {a,a^(-1)}. The characters
enter r^(s-1/2) on the contour; they are not differentiated as slow
weights. At v=0 the two identical terms have combined weight one.
All ordinary-jet coefficients and their signed sum are unchanged.

At fixed N, L408 (12) applies separately to every positive rational
r=u/w in lowest terms. For a monomial of total derivative order D<=6,
its leading coefficient is sqrt(r) A_u a_nu m_nu, where
m_nu=(-1)^D product_i d_i!/(D+2)! and sum_nu a_nu m_nu=17/20160.
The arithmetic input is Fazzari, *A Voronoi summation formula for the
shifted triple divisor function*, arXiv:2306.15553v1,
[(3.5)](https://arxiv.org/html/2306.15553v1#S3), and the residue-one
Hurwitz pole and continuation in [DLMF 25.11(i)](https://dlmf.nist.gov/25.11#i)
and [25.11.5](https://dlmf.nist.gov/25.11.E5). The additive numerator
is -w and modulus u, with gcd(w,u)=1; every residue class is retained.
The finite residue sum is u^(-3) sum_(b,d,e=1)^u exp(-2pi i wbde/u)
=A_u: summing over e forces u|bd, with gcd(b,u) admissible d's.
Positive progression parameters and the small shift disks are exactly
those in L408. Its smooth-first absolute endpoint passage, not direct
use of a Schwartz formula on an indicator, supplies the sharp interval.
Multiplying alpha sqrt(r) gives sqrt(a0)(mn)^(-2)q^(-3), so the
finite-head leading coefficient is exactly the head of (2).

Here is the complete passage for the changed rational characters.
Use the audited L409/L430 bounds with sigma=21/20, delta=11/20,
eta=1/100. On the shifted height rectangle tau=t-i z, 0<=z<=delta,
the response series converge normally on a neighborhood because all
powers z lie inside (-3/2,3/2). Each fixed a0 merely contributes a0^z.
The two sharp connectors for an individual twist are bounded by

    C(1+r^delta)H^(71/120) (single carrier),
    C(1+r^delta)H^(1/2)   (zero carrier).                  (6)

These are L407/L409's fixed-strip Cauchy specialization of Bourgain,
JAMS 30 (2017), [arXiv:1408.5794v2, Theorem 5/(0.5), p. 2](https://arxiv.org/pdf/1408.5794v2#page=2).
The primary frequency input is Milinovich--Ng, *Lower bounds for moments
of zeta'(rho)*, [Lemma 6.1, p. 9](https://home.olemiss.edu/~mbmilino/Lower_Bounds.pdf#page=9),
for positive kernel argument x and abscissa in a fixed compact subset
of (0,2], including its full endpoint-transition denominator. Its saddle,
endpoint and exterior cases use Gonek, Invent. Math. 75 (1984),
[section 3, Lemma 2, p. 130](https://www.sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf#page=8).
The inspected source coverage and local estimates are reused, not reproved.

Specifically, set x=l/r>0 and subtract the primitives at H and V,
H<=V<=2H. Integrating against each exact weight uses
|w|<=C ell^(-D), |w'|<=C ell^(-D)/H. The weighted single-carrier
error, including both endpoints and nearest saddles, is at most

    C[H^(11/20)r^(11/20)
      +H^(1/100)r^(-49/100)(1+log_+r)^D
      +H^(51/100)ell r^(51/100)(1+log_+r)^D].              (7)

The absolute arithmetic main sum is at most
C H sqrt(r)ell^2(1+log_+r)^(D+2). For r=a0 mn/q,
alpha r^z=a0^z m^(-5/2+z)n^(-5/2+z)q^(-5/2-z).
All exponents z in (6)--(7) lie strictly inside (-3/2,3/2).
The logarithms are bounded by C_v(1+log m+log n). Consequently
all response sums of these errors are o_v(H ell^2), uniformly for
subsets of response tuples, and the main sums have majorant

    C_v H ell^2 (mn)^(-2)q^(-3)(1+log m+log n)^8.           (8)

For zero carrier use the common grid h Z, h=1/(AB); every r=a0 mnq
is at least h. The resonance l=r is integral exactly when B divides
mnq for a0=A/B, or A divides mnq for a0=B/A. At every such resonance
retain r^(-1/2) C_nu(r) integral_[H,2H] w_(0,nu)(t-i delta)dt.
The bound |C_nu(l)|<=C l^(1/100)log(2l)^D shows its complete
response sum is O_v(H), including r=1. Off resonance the primitive is
bounded by

    2r^delta sum_(l!=r)|C_nu(l)|l^(-21/20)/|log(r/l)|.     (9)

Outside (r/2,2r) this is O(r^delta). Inside, use
|log(r/l)|>=|r-l|/(2r). Nonzero distances are at least h; the first
unit distance band costs O(1/h), and the remaining unit bands have
bounded occupancy and harmonic sum O(log(2+r)). This includes h<=r<1.
Thus (9) is O_v(r^(11/20)+r^(51/100)log(2+r)^(D+1)).
Both powers are summable against alpha for r=a0 mnq. Exact weight
variation is O(ell^(-D)), so the nonresonant sum is O_v(1).
Together with (6), the whole zero carrier is O_v(H). No denominator
grid resonance, endpoint saddle or response tail is omitted.

The tail epsilon_N of the summable series in (8) tends to zero.
The foregoing estimates applied to its cube complement give

    limsup_(H->infinity)
     |E_H[(d B0-d_N B0_N)cos(t log a)]|/ell^2<=C_v epsilon_N. (10)

Also 0<A_u<=1, so (2) converges absolutely at fixed v. Given a
tolerance, choose N to control (10) and the coefficient tail, then H
large at that fixed v,N. This proves (1) for d B0. L406's absolute
physical error O(ell^(5/4)) survives bounded cosine multiplication
and proves (1) for Delta Bcal, with full response derivatives and
curvature. An integrated signed tail has not been multiplied by cosine.
There is no uniform-in-v claim or summation of physical asymptotics.

### 2. Two valuations and the joint absolute majorant

L431's Chinese-remainder proof gives multiplicativity of A_u. For
p prime and e>=1, the residue classes of p-valuation d<e number
(p-1)p^(e-d-1); the zero class contributes p^e to the gcd sum.
Thus A_(p^e)=p^(-e)(1+(1-1/p)e), also valid at e=0.
This elementary changed local factor is needed at p=3.

Let T_6 be the sum in L409 restricted to m,n,q each coprime to 6.
It is positive and finite, between 1 and zeta(2)^2 zeta(3).
Unique valuations at 2 and 3 and nonnegative Tonelli summation give

    g_(j,k)=(kappa T_6/2)
       [2^(j/2)3^(k/2)B_2(j)B_3(k)
         +2^(-j/2)3^(-k/2)B_2(-j)B_3(-k)],
    beta=kappa T_6 B_2(0)B_3(0).                          (11)

The factor s+1 in (3) counts the ordered valuations of m,n. The
coprime-to-6 reduced numerator is unchanged by either character,
even when those remaining indices share factors. Thus T_6 is exactly
the same in both terms and beta. This proves (11) for all integer
j,k, including mixed signs; it is not a product of symmetrized moments.

For each p=2,3 and 1<R<p, nonnegative Tonelli and the bijection
d=s-r+j establish

    sum_(j in Z)B_p(j)R^j
      =[sum_(d in Z)b_p(d)R^d]
                      /[(1-p^(-2)/R)^2(1-R/p^3)]<infinity. (12)

The negative d tail requires R>1, and the positive tail requires
R<p. The other two geometric sums converge on this annulus. This
is a joint majorant over j,s,r before any rearrangement. For complex
u on that annulus, absolute convergence and the differentiated
geometric series give

    sum_d b_p(d)u^d
      =u/(u-1)+u/(p-u)+(p-1)u/(p-u)^2
      =(p-1)^2u/[(u-1)(u-p)^2].                          (13)

Multiplying the two geometric factors in (12) gives Q_p in (3).
Inner and outer radii supply local uniform convergence. At R=sqrt(p)
these sums are finite and positive. Applying (11) and reindexing its
second summand by (j,k)->(-j,-k) now gives the genuinely joint bound

    sum_(j,k in Z)c_(j,k)
       =Q_2(sqrt(2))Q_3(sqrt(3))/[B_2(0)B_3(0)]<infinity. (14)

Here c_v>0, so this is absolute summability. Tonelli justifies the
product in (14). The uniform Fourier series sum_v c_v e^(iv.x)
therefore equals the half-sum of the product Q_2 Q_3 and its complex
conjugate, precisely (4). Central reflection conjugates both factors
simultaneously. Individual coordinate reflection need not preserve W.

For normalization, c_0=1 follows directly from (11), and uniform
absolute convergence permits integration of the Fourier series.
Thus integral W dh=1 before using any sign. Integrating only phi
retains k=0 and cancels B_3(0) in (11), giving exactly L433's
prime-2 coefficient sequence and hence its continuous density.
This also checks the audited marginal without inferring joint positivity.

### 3. Entire-torus sign, retaining the mixed imaginary term

For p=2,3 set u=sqrt(p)e^(it), X=Re u, Y=Im u, and define

    A_p=p+1-2X, B_p^*=p^3+p^(-2)-2X,
    C_p=p^3+1-(p^2+1)X, D_p=(p^2-1)Y.

All A_p and B_p^* are strictly positive on their circles: A_p is
at least (sqrt(p)-1)^2, and p^3+p^(-2)>2sqrt(p), since it is
the sum of distinct positive numbers with product p. The following
identities use u conjugate(u)=p:

    (u-1)(u-p)=-u A_p,
    (p^2u-1)(p^3-u)=p^2 u B_p^*,
    (u-p)(p^2u-1)=u(-C_p+iD_p),
    C_p^2+D_p^2=p^2 A_p B_p^*.

Substitution into (3), with only nonzero denominators, gives

    Q_p(u)=p^3(p-1)^2(C_p+iD_p)/[A_p^2(B_p^*)^2].          (15)

In particular C_2=9-5sqrt(2)cos t>0 and
C_3=28-10sqrt(3)cos t>0, since 81>50 and 784>300.
Write Q_p=R_p(1+i r_p), where R_p=Re Q_p>0 and r_p=D_p/C_p.
To bound r_p globally, for a>b>0 and x in [-1,1] use the identity

    (a-bx)^2-(a^2-b^2)(1-x^2)=(ax-b)^2>=0.

It yields |d sin t/(a-b cos t)|^2<=d^2/(a^2-b^2), including
all endpoints. Equality occurs at cos t=b/a. Here it gives

    |r_2|^2<=18/31, |r_3|^2<=48/121,
    |r_2 r_3|^2<=864/3751<1/4.                            (16)

Consequently Re(Q_2 Q_3)=R_2 R_3(1-r_2 r_3)>R_2 R_3/2
on the entire torus. This explicitly controls the mixed imaginary
term, whose omission would give the wrong density.

For an explicit bound let w_p=R_p/B_p(0). L433 gives w_2>8/6075.
Since b_3<=1, B_3(0)<=1/[(1-1/9)^2(1-1/27)]=2187/1664<2.
Using sqrt(3)<7/4 gives C_3>10, 0<A_3<8 and 0<B_3^*<32.
Thus (15) gives

    w_3>108*10/(2*8^2*32^2)=135/16384>1/128.

Equations (4) and (16) prove W>w_2 w_3/2>1/194400, which
exceeds the required threshold zero. No truncation or sampled sign
enters this bound. For completeness the constant terms can be evaluated
by d=s-r as in L431: with delta_p=1-p^(-5), z=p^(-3),
a_p=1-1/p and S_i=sum_(d>=0)d^i z^d (S_0=1/(1-z)),

    B_p(0)=[S_0+(delta_p+a_p)S_1+delta_p a_p S_2
                                  +z/(1-z)]/delta_p^2,
    B_2(0)=571520/329623, B_3(0)=152029305/128665108.        (17)

The d>=0 weight is p^(-2d)(1+delta_p d)/delta_p^2;
the negative d=-h weight is p^(-3h)/delta_p^2. Multiplying by
b_p(d) and summing these convergent geometric derivatives proves
(17). The sign bound uses only the stated upper bound for B_3(0).

### 4. Measure scope and finite matrices

Import the lattice Bochner theorem and uniqueness in Peter Major,
*Multiple Wiener--Ito Integrals, with applications to limit theorems*,
author text dated July 13, 2013, section 3.1, original-form theorem
on [printed p. 22, PDF p. 30](https://renyi.hu/~major/articles/lecture0.pdf#page=30)
(the preceding Proposition 3C and proof are on printed pp. 20--21).
The named theorem identifies positive-definite functions on Z^2 with
unique finite positive torus measures; the lattice case needs no
Euclidean origin-continuity assumption. We use finite-measure Fourier
uniqueness on the compact torus and do not reprove the theorem.

We have constructed the finite positive measure W dh, with mass one
and all Fourier coefficients c_v. If a finite positive measure has
these cosine moments, average it with its pushforward under x->-x.
This preserves the cosines and forces every mixed sine moment to zero.
Its Fourier coefficients are consequently c_v for every lattice v.
The cited uniqueness forces its central symmetrization to be W dh.
Conversely W dh supplies such a measure. No actual physical sine
asymptotic or separate coordinate symmetry has been assumed.

For distinct lattice indices v_a and a nonzero finite complex vector z,
Fourier integration and orthogonality give

    sum_(a,b) conjugate(z_a)c_(v_a-v_b)z_b
      = integral W(x)|sum_a z_a e^(iv_a.x)|^2 dh
      >=(1/194400)sum_a|z_a|^2>0.

Thus every finite difference matrix is positive definite as a
consequence of the full density. A new intermediate mass and the
other selected-law tolerances are not consequences of this statement.
No assertion about actual/global realization, actual clipping, regulator
margins or RH follows.

### Exact finite verification

Run `python3 scripts/discriminant/joint_two_prime_cubic_density.py`.
It writes `scripts/discriminant/joint_two_prime_cubic_density_certificate.json`.
Exact rational Laurent arithmetic checks (13), the full complex identity
(15), and its modulus identity for each prime by u conjugate(u)=p.
All six complete residual polynomials are zero. It also checks (17),
the audited prime-2 constant, both squared phase maxima, their product
and the complete rational lower-bound comparisons. All 19 checks pass,
failures=[]. The complete local polynomial records, checks, failures
and actual/required bound were inspected through the JSON inspector.
This is finite algebra corroboration; sections 1--2 prove the physical
limits and infinite interchanges. The separate audit below checks both.

### Separate critical audit — 2026-10-18, step 234

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-18-joint-two-prime-density-critical-audit.md`.
The inspected primary statements and cases in that assessment and the
separate L406--L409/L430/L433 audits are reused. No general moment,
stationary-phase or lattice-measure theorem is reproved. The audit finds
no defect in (1)--(5) or in their quantifiers. It validates a local
known-tool specialization, not a new source theorem or an RH input
asserting the missing mixed positivity.

**Fixed rational characters and the complete physical passage.** Fix
(j,k) and reduce a=A/B before either limit. On the real line
Re(V)cos(t log a)=Re(V a^(it)+V a^(-it))/2. Applying this identity
to L407's exact two carrier patterns gives precisely the four twists
in section 1; a=1 has total weight one. On the shifted contour the
characters continue holomorphically inside r^(s-1/2). They are not
absorbed into a slowly varying coefficient. Thus L407's exact ordinary
jets, including Omega', and their weight derivative bounds are retained.

For r=u/w reduced, the additive phase is exp(-2pi i wl/u).
All residue classes are included, gcd(w,u)=1, and summing the third
class gives u when u divides the product of the first two classes.
There are gcd(b,u) admissible second classes for each b. The leading
coefficient is therefore A_u, including u=1, with no dependence on w.
L408's unsigned absolute boundary majorant handles both sharp endpoints
for these complex phases. Its signed factorial contributions, over
20160, are 420,-840,336,-56,336,-224,48,-3, summing to 17.
Multiplication by alpha sqrt(r)/2 gives exactly (2); the leading
coefficient is real, so the outer real projection adds no further half.
The two zero-leading monomial weights still have their O(ell^(-D-1))
errors from L408. No uniformity in u,w or (j,k) is needed at fixed N.

For the full passage, all response series converge normally on a
neighborhood of the height rectangle. Each fixed a0 contributes only
a bounded a0^z on that rectangle. At z=11/20,-49/100,51/100,
the single-carrier response exponents -5/2+z,-5/2+z,-5/2-z
are all below -1; every fixed logarithmic factor is summable.
The kernel bound is uniform for x=l/r>0. Its two nearest lattice
points cover exact endpoint saddles, including tiny rH. Subtracting
the H and V primitives and integrating against the exact weight
costs |w(2H-i delta)|+integral |w'|. Hence (7) retains both
endpoints and all weight variation. Both sharp connector sums in (6)
converge, with largest height exponent 71/120<1. These bounds hold
for every cube complement, with constants independent of N.

For zero carrier r=A mnq/B is integral exactly when B divides mnq;
for r=B mnq/A it is integral exactly when A divides mnq. Both
statements use gcd(A,B)=1. At l=r the right-line amplitude is
r^(21/20-1/2)r^(-21/20)=r^(-1/2), giving the complete O_v(H)
resonance sum. At r=1 the undifferentiated coefficient is retained;
positive derivative powers give log 1=0. Off resonance, integer l
and r in h Z, h=1/(AB), have nonzero distance at least h. In
r/2<l<2r the nearest unit distance band costs O(1/h); all later
bands have bounded occupancy and harmonic total O(log(2+r)).
Combining r^(11/20), l^(1/100-21/20) and the factor 2r gives
r^(51/100), as in (9). Outside this band the denominator is at
least log 2. The small range h<=r<1 is covered by the same
fixed-v constants. Both powers, and their logarithms, are summable
against alpha for the product pattern. Weight variation preserves
this O_v(1) bound, independently of the O_v(H) resonances.

The absolute single-carrier main sum has the summable majorant (8).
Its cube-complement mass tends to zero. These frequency estimates,
rather than multiplication of an integrated signed error by cosine,
prove (10). Choose N to control that tail and the positive coefficient
tail (using A_u<=1), then H large at this N,v. L406's absolute
physical replacement costs O(ell^(5/4)) after bounded cosine
multiplication. It contains full response derivatives and curvature.
This proves (1) for every separately fixed lattice index, with no
exchange of a height limit and an infinite character sum.

**Joint resummation and the probability measure.** The Chinese
remainder factorization of A_u applies to the reduced numerator, even
when the remaining indices have common factors. At each p the sum
s of the two numerator valuations has s+1 ordered decompositions,
and the denominator valuation is r. Nonnegative Tonelli gives (11)
with the same positive T_6 in both characters and in beta. For each
1<R<p the change d=s-r+j in the full positive sum gives (12):
the factors are (1-p^(-2)/R)^(-2) and (1-R/p^3)^(-1).
The negative d tail requires R>1; the positive d tail requires R<p.
Thus a genuine joint absolute majorant precedes the complex geometric
identities. Inner and outer radii give local uniform convergence;
(13) and both geometric factors give exactly (3), including p^7 u^3.

At R=sqrt(p), the joint product of the two finite positive majorants
proves (14). For complex arguments its two terms are conjugated by
simultaneous inversion of both angles. Their half-sum is Re(Q_2 Q_3),
which retains the mixed imaginary term. It is not Re(Q_2)Re(Q_3).
The constant coefficient is one directly from (11), before signing W.
Uniform absolute convergence licenses integration. Integrating phi
retains k=0 and cancels B_3(0), giving exactly L433's whole marginal,
not merely a finite prefix. No actual sine limit is used or inferred.

**Full complex sign and exact evidence.** All circle denominators are
nonzero: A_p>0 and B_p^*>0, and the corresponding polynomial roots
lie off |u|=sqrt(p). Substitution conjugate(u)=p/u verifies each
of the four circle identities; in particular the remaining factor is
-C_p+iD_p, so inversion gives the plus sign in C_p+iD_p in (15).
The inequality (ax-b)^2>=0 gives the squared phase bounds at every
angle, including endpoints. They are 18/31 and 48/121, whose product
864/3751 is strictly below 1/4. Therefore the adverse term r_2 r_3
is strictly below 1/2 and Re(Q_2 Q_3)>R_2 R_3/2 globally.
The inherited w_2>8/6075 and the complete p=3 bounds give
w_3>135/16384>1/128. This proves the strict bound 1/194400
against the required threshold zero, with no sampled sign argument.
The constant-term formula (17) also follows by separately summing
d>=0 and d<0; it agrees with the saved rational values.

Read the complete algebra program, replayed it, and inspected /checks,
/failures, /local/2, /local/3, /density_bound and
/joint_phase_product_squared in full through the JSON inspector.
Both local records include all Laurent numerator and denominator
coefficients on both sides, all six zero residual polynomials, both
B_p(0) values, their positive majorants and both phase-ratio squares.
All 19/19 checks pass, failures=[], with the stated actual/required
bounds. Empty residual dictionaries represent identically zero
polynomials after exact Fraction arithmetic. The program's cleared
identities do not establish nonvanishing denominators, convergence or
physical limits; those are checked separately above.

The constructed positive measure has mass one and all Fourier
coefficients c_v. For any competing finite positive measure with the
cosine data, central symmetrization kills sin(j theta+k phi) for
every lattice pair; the cited lattice uniqueness theorem then applies.
Coordinatewise symmetry and uniqueness without symmetrization do not
follow. Orthogonality of distinct lattice characters and the global
lower bound give the strict finite-matrix inequality exactly as stated.

No direct input, coefficient, hypothesis or argument has changed, so
the canonical DAG and PROOF.md assembly are unchanged. The audited
compatibility stop supplies no new law, clipping estimate, capped
nondegeneracy, actual/global realization or full-error regulator margin.
The main RH gap remains open. Independent validation is the local
advance; no novelty beyond the checked tools is claimed.

## Mathlib

Full matching coverage for the physical joint cubic, bilateral rational
density, or this specialization has not been checked. The precise
primary inputs and audited local analytic interfaces above are the
mathematical references. Unknown Mathlib availability is not absence,
and the exact algebra certificate is not a Lean formalization.
