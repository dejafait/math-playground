# C744z: The exact neutral shared-middle residual and comparison stops

## Hypotheses

Let ell=log(3)/2. Use C744r's unconditional Hermitian pairing H,
linear in its first argument, d(f)=H(f,f), and the original space N
of complex C_c^infinity(0,ell) profiles with both integrals against
exp(x/2) and exp(-x/2) zero. Extend all profiles by zero. Write
tau_a f(x)=f(x-a). Only offsets 0,7ell,14ell are considered.

Use L742(8)-(12), L744(6),(8), C744v's complete response extension,
and the audited C744y two-profile inequality. The single-cell floor
in L742 Section1 is d(f)>=c_*||f||_2^2 on N, c_*=8.9*10^-18.
Its L741/Zhu source-computation qualification is inherited: that
source certificate was not locally replayed. No conditional-on-RH
conclusion of L742 is used. C744y retains its IEEE754/Decimal and
analytic-input contracts. No H2 existence or strict slack is assumed.

The standard form inputs are Gerald Teschl, *Mathematical Methods in
Quantum Mechanics*, author-hosted GSM99 PDF, Section2.3,
Theorem2.13/proof, printed pp71-72, and Theorem2.18/proof, printed
p77, [author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
The version inspected in assessment541/comparison542 has317 PDF pages.
The first represents a densely defined closed semibounded Hermitian
form by a self-adjoint operator; the second supplies the lower-bound
and resolvent estimates. The associated spectral calculus is used
for the inverse square root. These results are imported, not reproved.
The bounded-block comparison is Dritschel and Rovnyak,
*The Operator Fejer-Riesz Theorem*, arXiv:0903.3639v1, AppendixA,
LemmaA.1, printed pp28-29,
[pinned PDF](https://arxiv.org/pdf/0903.3639v1). Its LemmaA.2 is not
used to infer positivity from an assumed positive whole block.

C744v's analytic response identity is the already assessed
specialization of Hongmin Li, paper45 displayed v2, 9 November2026,
Lemma3.1/(2.1)-(3.4),
[source](https://rstation.ai/problems/riemann_hypothesis/papers/45).
It is not rederived here. The new applicability work is the exact
neutral core/restriction and the actual separation14 block; the
general Schur theorem is not a new result. Decimal scalar bounds
use the audited interval implementation and contract of C744v.
The finite diagnostic below has no verified arithmetic contract.

## Conclusion

There is a closed coercive neutral single-cell form with domain
V0=V intersect ker(C), where V is C744v's logarithmic cosine form
domain and C is the two-moment map. N is a form core. Let A0 be its
representing operator on H0=ker(C) in L2(0,ell), and P0 the L2
orthogonal projection onto H0. Then A0>=c_*I and A0^-1 is bounded.
It is the inverse of the restricted form, not a projected inverse
of an unrestricted form.

Let T be C744v's complete separation7 operator. The exact
separation14 operator U is

    (Uf)(x)=sum_(n in P14) [Lambda(n)/sqrt(n)] f(x+14ell-log(n))
                + integral_0^ell K14(x,y)f(y)dy,
    P14={prime powers n: 3^13<n^2<3^15},
    K14(x,y)=sum_(j>=1) exp[-(2j+1/2)(14ell+x-y)].       (1)

Zero-extension indicators are included in every translation.
There are334 active prime powers, including n=2187 with exactly
zero delay. It contributes (log3)/sqrt(2187) times the identity.
No prime, continuous tail or complex cross product is omitted.

Set K=P0 T|H0, J=P0 U|H0, E=A0^-1/2 and

    R=E K E, V14=E J E.                                (2)

C744y implies ||R||<=1. For f,g,h in V0 and x=A0^1/2 f,
y=A0^1/2 g, z=A0^1/2 h, the exact three-cell extension is

    ||y-Rx-R*z||^2 + <(I-R*R)x,x> + <(I-RR*)z,z>
                      -2 Re<(V14+R^2)x,z>.             (3)

Thus nonnegativity on all original smooth neutral triples is
equivalent to nonnegativity of the bounded endpoint block

    S3=[[I-R*R, -(V14+R^2)*],
        [-(V14+R^2), I-RR*]] on H0 direct-sum H0.        (4)

Both diagonal entries in (4) are nonnegative; its full sign is
**unproved**. Formula (4) retains the actual remote operator and
the induced coupling. It supplies no compatible propagation law.

Section10's separate quantitative specialization gives the actual
bound ||R||^2<.998001 under the inherited contracts. This is strict
contraction, but misses the requested3/4 threshold for excluding the
fixed defect windows. Neither window emptiness nor nonemptiness is
proved. This new specialization is not independently audited.

The rigorous scalar calculation gives ||U||<=u14<29.813203120,
with u14>29.813203119. For the512-mode raw L2 row comparison,
the diagonal lower bound is h512>6.1442765416 and the proposed
uniform floor h512-4.71-u14 lies in (-28.379,-28.378). The scalar
comparison itself is indefinite, already on endpoint coordinates
(1,0,1); this stops that sufficient certificate. It does not show
that the actual neutral form has a negative direction.

The unverified512-mode neutral diagnostic has endpoint residual
minimum about.019327887 and both residual diagonal minima about
.15033647. Its middle inverse is finite, all omitted covariance is
unpaid, and its approximate moment projection is not a certificate.
These numbers do not prove even the exact finite sign here.

The separate step544 attempt in Section6 also stops one signed
comparison: subtracting the unit prime-density model and bounding its
primitive by a constant-centered L1 first-derivative Young estimate
cannot improve the raw remote bound on the512-mode complement. Even
the optimal integration constant has coefficient at least.03200576,
where improvement requires less than.01072864. This is a comparison
obstruction, not a lower bound on the actual remote operator or a
negative smooth triple. The full residual (4) is still unsigned.

Section7 gives a different, signed covariance obstruction. Keeping
both exact endpoint energies and the actual remote pairing, but
replacing only the middle energy D+S by D, gives a comparison value
in (-.531418,-.530619) on an exactly neutral16-mode triple. Restoring
the positive middle response gives an actual triple value in
(.771368,.772279). Thus the diagonal-only middle comparison fails;
the actual residual (4) remains unsigned. No inverse or tiny c_*
bound is needed for this obstruction.

Section8 retains the first32 positive middle-response squares in each
parity, but this fixed comparison still has an exactly neutral512-mode
value in (-.000528,-.000170). The same original triple has positive
energy in (.093538,.094207). Thus this prefix does not pay the complete
middle debt. This does not exclude larger prefixes or determine(4).

These are local REPRODUCTION/specializations under the pre-existing
EXPLORE assessment541. The useful local
input is the fully specified restricted residual and its domain,
not a sign theorem beyond the checked sources. This derivation is
not independently audited as a whole. Section9 separately upholds
only the fixed-prefix Section8 obstruction and its needed core/entry
arguments under the stated contracts. RH, other separations, C744q's
strict margin, H2 slack/existence, non-neutral coverage and assembly
remain unresolved.

## Proof

### 1. The neutral core and its actual restricted inverse

Let e_n be C744v's normalized cosine basis, D e_n=h(n*pi/ell)e_n,
and S its bounded positive response. The closed form a=D+S has
domain

    V={f: sum_(n>=0)(1+log(2+n))|<f,e_n>|^2<infinity}.

Its shifted form norm is equivalent to the displayed weighted
norm, by C744v and L744(8). It agrees with d on N; no moment
penalty remains there. The map C:L2->C^2 is bounded. Consequently
V0=V intersect ker(C) is closed in V. We verify its dense core,
rather than assuming an operator domain equals a form domain.

First C_c^infinity(0,ell) is dense in V. Finite cosine sums are
dense by truncation of the defining positive series. For a fixed
such smooth sum p, let chi_delta be a smooth cutoff equal to1
except within distance2delta of the endpoints, zero within
distance delta, with |chi_delta'|<=constant/delta. Put
r_delta=(1-chi_delta)p. Then

    ||r_delta||_2^2=O_p(delta),
    ||r_delta'||_2^2=O_p(delta^-1).

Cosine Parseval and integration by parts against the sine basis
give sum n^2|<r_delta,e_n>|^2=(ell/pi)^2||r_delta'||_2^2.
There is no boundary term since the sine functions vanish at both
endpoints. For n<=delta^-1 the weight is O(log(1/delta)); for
n>delta^-1 its ratio to n^2 is O(delta^2 log(1/delta)). These
statements follow directly from monotonicity of
(1+log(2+t))/t^2 for t>=1. Splitting the coefficient sum therefore
gives ||r_delta||_V^2=O_p(delta log(1/delta))->0. Hence
chi_delta p approximates p in V.

Next choose real nonnegative nonzero smooth bumps b1,b2 supported
in disjoint subintervals, the first strictly to the left of the
second. The ratio C_+(bi)/C_-(bi) is the weighted average of e^x
with positive weight e^(-x/2)bi(x). The two ratios lie in disjoint
intervals, so the2 by2 matrix M with columns Cbi is invertible.
If p_j in C_c^infinity converges in V to f in V0, set

    q_j=p_j-(b1,b2)M^-1 Cp_j.

Then Cq_j=0 exactly, and q_j->f in V because Cp_j->Cf=0
and the correction functions are fixed in V. Thus N is a form
core of V0. The same construction, using ordinary L2 smooth
density, proves that the L2 closure of N is H0=ker(C).

The uniform L742 Section1 bound passes to V0 by form continuity:
a(f,f)>=c_*||f||_2^2. This uses its expressly retained source
qualification, not an RH premise. The restriction a0 is densely
defined on H0, closed (closed subspace of the shifted form Hilbert
space) and uniformly coercive. Teschl Theorems2.13/2.18 therefore
give the unique self-adjoint A0>=c_*I. Spectral calculus gives
bounded A0^-1 and E=A0^-1/2, with E mapping H0 bijectively onto
V0 and A0^1/2 inverse to that map. We never replace A0^-1 by
P0 A^-1 P0 for an unrestricted A.

### 2. The complete actual remote pairing

Polarize L742's unconditional formula on f and tau_(14ell)h.
The scalar local term has disjoint supports. Both pole products
factor through the two moments of f,h, hence vanish exactly.
The continuous separated contribution is

    - integral integral [k(14ell+x-y)/2] f(y)conj(h(x))dy dx.

Expand k(t)/2=sum_(j>=0)exp[-(2j+1/2)t]. Since
14ell+x-y>=13ell>0 on the closed square, the series is absolutely
uniformly convergent. Thus all interchanges hold for L2 profiles
by their finite-interval L1 norms. Its j=0 product vanishes by
neutrality; the entire j>=1 series is K14.

For a prime-power delay log n, only the forward causal pairing
can meet the two supports; its contribution is

    -[Lambda(n)/sqrt(n)] integral f(x+14ell-log n)conj(h(x))dx.

The reversed causal direction contributes zero. Its overlap is
nonzero precisely when |14ell-log n|<ell. Equivalently
3^13<n^2<3^15. Boundary equality would give only zero-length
overlap (and is impossible here for integer n). This proves
H(f,tau_(14ell)h)=-<Uf,h>, with coefficient Lambda(n)/sqrt(n),
not twice that coefficient. The same separation7 identity is
C744v/y's audited input. Translation invariance and polarization
now give the whole three-cell energy

    d(f)+d(g)+d(h)-2 Re[<Kf,g>+<Kg,h>+<Jf,h>].          (5)

Every operator here is bounded on L2 except the displayed local
closed forms. The prime sum is finite; the continuous operator
is bounded by the row argument below. Equation (5) therefore
extends continuously to V0 cubed. Original compact smooth triples
and their whole-window generator domains remain those of L742;
no larger-window generator-domain equality is asserted for V0.

### 3. Spend the middle energy once

In unscaled coordinates put b=Kf+K*h. For fixed endpoints,

    a0(g,g)-2 Re<b,g>
       =||A0^1/2(g-A0^-1 b)||^2-<A0^-1 b,b>.           (6)

This is legitimate: b is in H0, A0^-1b is in Dom(A0), and all
terms are actual form pairings. In particular no inverse is taken
of the unproved positive triple block. Both diagonal losses and
the induced cross product in <A0^-1b,b> must be retained.

Equivalently set f=Ex,g=Ey,h=Ez. Equation (5) becomes

    ||x||^2+||y||^2+||z||^2
       -2 Re[<Rx,y>+<Ry,z>+<V14 x,z>].                 (7)

Square completion in y gives (3), since
<Rx,R*z>=<R^2x,z>. Thus the two defects are I-R*R and I-RR*,
and the remote-plus-induced block is V14+R^2 with its actual
adjoint on the opposite side. This covers arbitrary complex and
independent profiles. Replacing V14 by R^2, changing its sign,
or deleting either defect would change the problem.

C744y and the core result extend the two-cell inequality to V0
squared. In energy coordinates it says
||x||^2+||y||^2-2Re<Rx,y>>=0 for every x,y in H0.
Taking y=Rx proves ||R||<=1, hence both displayed defects are
nonnegative. This alone does not prove (4), exactly as the
bounded-block factorization criterion requires its whole cross
term to be paid. For any x,z, the minimizing y=Rx+R*z is allowed
in H0. Density of N cubed and continuity of (5) prove both
directions of the claimed equivalence with the original smooth
triple sign. This is a local reduction, not proof of its sign.

### 4. Complete scalar evidence and the failed sufficient comparison

For the arithmetic part of U put

    r14(x)=sum_(n in P14) [Lambda(n)/sqrt(n)]
                               1_(0,ell)(x+14ell-log n).

The column sum is r14(ell-y). Weighted Cauchy--Schwarz as in
C744v gives prime-operator norm at most ess sup r14. The full
continuous row/column norm is at most

    kappa14=sum_(j>=1)exp[-13ell(2j+1/2)]/(2j+1/2)
       <=3^(-65/4)/[(5/2)(1-3^-13)]<7.061*10^-9.       (8)

The notation kappa14 in the certificate denotes the last upper
bound. The prime enumeration uses integer tests 3^13<n^2<3^15
and complete trial division through sqrt(n). For each active
power all row events -delta and ell-delta in the cell are enclosed
with directed Decimal arithmetic. The exactly zero delay at2187
is handled symbolically; it has no interior event and is present
in every row. There are335 endpoints including0,ell and334 open
row intervals. All consecutive event intervals are disjoint;
every active-set membership on every row is checked by interval
inequalities. Summing the complete row sets gives

    29.81320311275997 < ess sup r14 <29.81320311275999,
    29.81320311982055 <u14<29.81320311982056.             (9)

Here u14 is the row maximum plus the bound (8), not a lower bound
on the actual operator norm. C744v's n>=512 diagonal estimate is

    h512=log(512/(2ell))-2ell^2/(9*512^2)
          in (6.14427654163698,6.14427654163699).        (10)

For three complementary components, D contributes at least h512
times their total squared norm; S and the original comparison's
moment penalties are nonnegative. Using ||T||<4.71 and ||U||<=u14
therefore gives the scalar norm comparison matrix

    G=[[h512,-4.71,-u14],[-4.71,h512,-4.71],
                                      [-u14,-4.71,h512]].

Its row floor is h512-4.71-u14 in (-28.379,-28.378), and its
Rayleigh quotient at (1,0,1) is h512-u14<-23.6689. Thus even
this whole scalar comparison matrix is indefinite; optimizing its
middle entry cannot repair it. This comparison pays all operators
by their L2 norm envelopes and loses their actual signed neutral
cancellations. Its failure is not a negative direction of (5),
not an estimate from below on ||U||, and not a failure of RH.
It rules out transferring C744y's particular coarse512-mode
complement-floor method without an additional cancellation bound.

### 5. What the finite diagnostic does and does not test

The script reads, without changing, C744w's audited512-mode head
archive. It checks its SHA256 against the step541 audit. It forms
all334 remote shifts using C744w's antiderivative formulas and
includes j=1,...,7 of the remote continuous kernel. The latter's
remaining positive kernel is bounded analytically by (8) starting
at j=8, but its rounding and the new finite entries are not enclosed.
The exact2187 shift is its scalar identity matrix.

A numerical QR of the two moment rows proposes a510-dimensional
neutral basis. In that basis the penalized head agrees with the
unpenalized energy only up to the moment residual, about2.65*10^-18;
this is explicitly not exact neutrality. The script computes the
finite energy inverse square root and constructs all of (4), with
no omitted finite cross products. Its least direction has endpoint
diagonal energy about1, eliminated-middle debt about.7316238335,
and actual-remote contribution about-.2490482794, leaving about
.0193278871. All matrices and the direction are saved, not just
an eigenvalue preview. New floating eigenvalues remain diagnostic.

There is also an analytic reason that a positive finite test cannot
close this target. For an exact finite neutral subspace W of V0,
the restricted middle debt satisfies

    sup_(g in W) [2Re<b,g>-a0(g,g)]
       <=sup_(g in V0) [2Re<b,g>-a0(g,g)]
        =<A0^-1b,b>.                                  (11)

The first supremum is the finite Galerkin inverse correction.
Consequently the finite minimized residual is an upper comparison
to the actual residual on the same endpoints, not a lower one.
Equality requires the full minimizer to lie in W. The entire
omitted middle correction, all endpoint complements, and their
mixed covariance remain unpaid. No profile is promoted to an
exact neutral smooth witness, and no H2 budget conclusion follows.

Reproduce this bounded attempt from the notebook with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/shared-middle-543.py

Full scalar certificate:
`scripts/separation-seven/shared-middle-scalar-certificate-543.json`.
Full diagnostic summary:
`scripts/separation-seven/shared-middle-diagnostic-543.json`.
All diagnostic matrices:
`scripts/separation-seven/shared-middle-diagnostic-matrices-543.npz`.
The initial zero-delay event-assertion failure and its correction
are recorded in the scalar certificate. Subsequent scalar checks
all passed. No original archive, previous failure, source
assessment or supervisor state was changed.

### 6. Signed density subtraction: a first-derivative comparison stop

This is one additional RESEARCH / REPRODUCTION / proof_attempt,
12 November2026, step544, under the unchanged prior EXPLORE
assessment541. It uses the actual operator (1), the same geometry,
the same cosine cutoff512 and the original neutral class. The
question is whether signed density cancellation can improve the
unpaid remote complementary estimate in (4). General integration
by parts, the integral triangle inequality (Minkowski), and cosine
Parseval are standard inputs; their applicability is given below.
No new source sign theorem, PNT estimate, H2 budget or RH premise
is introduced. The unchanged source qualifications above apply.

Write a=14ell and J14 for the prime part of U. On [-ell,ell] let

    nu=sum_(n in P14) [Lambda(n)/sqrt(n)] delta_(a-log n),
    rho(t)=exp((a-t)/2),
    F(t)=nu([-ell,t])-integral_(-ell)^t rho(s)ds,
    b(c)=integral_(-ell)^ell |F(t)-c|dt.                (12)

The density scale in this test is exactly1; optimization of that
scale or an x-dependent primitive is not being claimed. For each
x in (0,ell), the interval (x-ell,x+ell) contains the entire support
of an original profile f. Therefore

    integral_(-ell)^ell rho(t) f(x+t)dt
      =exp((a+x)/2) integral_0^ell exp(-y/2)f(y)dy=0.

This is exact neutrality, not an approximation to the prime measure.
The finite signed measure nu-rho(t)dt has primitive F of bounded
variation. Stieltjes integration by parts, using f(x-ell)=f(x+ell)=0,
gives for any constant c (real or complex)

    (J14 f)(x)=-integral_(-ell)^ell (F(t)-c)f'(x+t)dt,
    ||J14 f||_2 <= b(c)||f'||_2.                       (13)

To justify the norm bound, extend f' by zero and first bound the
L2 norm on the whole real line by the integral triangle inequality;
each translated derivative has the same L2 norm. Restriction to the
cell only decreases that norm. All integrals converge since F is
bounded on a finite interval and f is smooth and compactly supported.
For h in the same class, integration by parts in x, with the zero
extensions and no endpoint terms, also moves the derivative to h.
Consequently the complete remote pairing has the valid sufficient
majorant

    |<Uf,h>| <= min{r14 ||f||_2||h||_2,
                    b(c) min{||f'||_2||h||_2,
                              ||f||_2||h'||_2}}
                  +kappa14 ||f||_2||h||_2,            (14)

where r14 is the prime row maximum in (9) and kappa14 is the
whole continuous-kernel upper bound (8). The latter kernel has
not been dropped. Formula (14) holds for complex independent
profiles. It is only an absolute majorant of one component of
(4); it does not pay or delete the induced middle covariance.

There is an obstruction even to improving this particular majorant.
The334 distinct atoms lie strictly inside (-ell,ell), so they leave
335 open gaps of positive lengths L_j with sum_j L_j=2ell. On each
gap F is continuously decreasing with -F'(t)=rho(t)>=rho_min,
where rho_min=exp(13ell/2)=3^(13/4). For a gap (u,v) and t in its
left half, the triangle inequality gives, for EVERY constant c,

    |F(t)-c|+|F(u+v-t)-c|
       >=F(t)-F(u+v-t)>=rho_min (u+v-2t).

Integrating over that half-gap yields rho_min (v-u)^2/4.
Summing the gaps, and applying Cauchy--Schwarz to their lengths,
proves the all-constants bound

    b(c)>=rho_min sum_j L_j^2/4
         >=rho_min ell^2/335=:b_lower.                 (15)

Thus even choosing a different optimal constant for each test pair
cannot evade (15). No numerical minimization or assumption about
the locations of F's median is used.

Let Q be the same cosine complement n>=512. For any f in
C_c^infinity(0,ell) with Qf=f, sine Parseval and integration by
parts against sin(n*pi*x/ell) give

    ||f'||_2^2=sum_(n>=512)(n*pi/ell)^2 |<f,e_n>|^2,
    ||f'||_2 >= (512*pi/ell)||f||_2.                  (16)

The sine boundary values vanish, so there is no missing trace term.
This also holds after imposing the two neutral moments; those are
additional linear constraints, not a frequency or derivative upper
bound. The smooth space Q intersect N is infinite-dimensional: imposing
the512 cosine coefficients and two moments gives only514 linear
constraints on C_c^infinity(0,ell). This is a genuine subspace test.
We do not assume that P or Q preserves neutrality; arbitrary projected
pieces would require their moment terms to be restored. Failure to
improve the uniform majorant already on this neutral subspace suffices
to reject the proposed uniform complementary payment. For nonzero
f,h in Q intersect N, (15)-(16) force the derivative
branch of (14) to be at least

    b_lower (512*pi/ell)||f||_2||h||_2
      >89.49627167 ||f||_2||h||_2,

using only pi>3. In contrast, r14<30. Hence the minimum in (14)
always selects the original prime row branch on this complement.
Even the best constant-centered primitive does not improve the
remote complementary bound at all. A necessary (and insufficient)
coefficient threshold for improvement would be

    b(c)<r14 ell/(512*pi)<30ell/1536<.01072864,

whereas (15) gives b(c)>.03200576. Adding the positive kappa14
charge changes neither this comparison nor its failure. The raw
scalar block in Section4 is therefore left unpaid by this method;
both actual endpoint defects and all induced covariance remain
required. This conclusion concerns this sufficient majorant, not
the norm or sign of the actual signed operator. The actual pairings
can be much smaller. It does not exclude signed matrix estimates,
frequency-localized payment, low-to-high covariance estimates, or
cancellation between the actual and induced blocks in (4).

The directed-Decimal certificate independently enumerates all334
prime powers by exact primality and integer cutoff tests. It
cross-checks that list against the original step543 certificate
without changing it. It encloses every primitive jump and gap.
For a jump at a-log(n), the continuous mass used is exactly
2[3^(15/4)-sqrt(n)]; the limiting values at both cell endpoints
are included. The monotonicity between jumps justifies computing
the primitive extrema from these values. In addition to the simple
load-bearing bound (15), the certificate records the stronger gap
bound >.05145786 and a valid midrange-choice upper bound <.740239.
Neither bound is an assertion of the exact optimized coefficient.
The simpler bound alone already rejects the comparison.

Reproduce from the active notebook:

    python3 scripts/separation-seven/density-primitive-stop-544.py

Full certificate: `scripts/separation-seven/density-primitive-stop-544.json`.
All enumeration and interval assertions pass, with no failed run.
The script prints the actual lower bound, necessary threshold,
failure count and artifact path. The interpretation requires the
complete analytic argument (12)-(16), not a numerical preview.
This new comparison obstruction remains independently unaudited.
It is a local specialization, not a claim of new general mathematics
or of progress beyond the standard source methods.

### 7. Signed logarithmic covariance: the middle response cannot be discarded

This is the bounded step545 research attempt,12 November2026, under
the unchanged approved assessment541/comparison542. It tests a
materially different sufficient comparison from Sections4 and6:
retain signed mode products and both full endpoint energies, but
pay the eliminated middle using only its logarithmic diagonal.
The exact target remains (4). The known method and response identity
are imported from the sources in the Hypotheses; this section is
their local specialization, not a new general Schur theorem.

Write a(f)=<Df,f>+<Sf,f> on V0, and define on V0 cubed

    Q_D(f,g,h)=a(f)+a(h)+<Dg,g>
            -2 Re[<Tf,g>+<Tg,h>+<Uf,h>].              (17)

All pairings use the actual complete operators (1),(5). Since
S>=0, the actual triple energy is exactly

    Q_actual(f,g,h)=Q_D(f,g,h)+<Sg,g>.                 (18)

Thus Q_D>=0 on all neutral triples would suffice. A negative Q_D
only stops this sufficient comparison; it is not a negative actual
triple. Neither of the endpoint response forms has been discarded.
No moment penalty has been added or spent on the neutral profiles.

Here is a fully specified obstruction. Use the cosine basis e_n,
k_n=n*pi/ell and normalization nu_n from C744v Section3. For each
integer2<=n<=15 let p=n mod2 and

    r_n= sqrt(2)*(1/4)/(1/4+k_n^2),             p=0,
    r_n= (1/4+k_1^2)/(1/4+k_n^2),              p=1.    (19)

Specify the following free coefficients by their exact integer
numerators with common denominator2^30. All unlisted coefficients
above15 vanish; the two low coefficients are fixed by (20).

| n | f numerator | g numerator |
|---|---:|---:|
|2|-663346670|-2110590631|
|3|533331766|0|
|4|164165448|-264410890|
|5|-88458226|0|
|6|176787232|-276887860|
|7|184734098|0|
|8|-306743621|-677439980|
|9|-247733884|0|
|10|347656722|485951745|
|11|3818045|0|
|12|-65652459|72428290|
|13|-195071970|0|
|14|84842579|207301287|
|15|-48880280|0|

For u=f,g set

    u_p=-sum_(2<=n<=15, n mod2=p) r_n u_n,  p=0,1;
    h_n=(-1)^n f_n.                                  (20)

These define exact real functions; only their interval enclosures
are numerical. To verify both moments, direct integration gives

    integral_0^ell e^(x/2)e_n(x)dx
       =nu_n(1/2)[(-1)^n e^(ell/2)-1]/(1/4+k_n^2),
    integral_0^ell e^(-x/2)e_n(x)dx
       =nu_n(-1/2)[(-1)^n e^(-ell/2)-1]/(1/4+k_n^2).

Within either parity, the ratio of either moment at n to that at
p is exactly r_n. The low moment at p is nonzero. Equation(20)
therefore kills each parity's two moments, hence both moments of
f,g. Reflection F u(x)=u(ell-x) multiplies coefficient n by(-1)^n,
exchanges the two moments up to nonzero constants, and preserves
V0. Thus h=Ff is also exactly neutral and g=Fg. These finite cosine
functions belong to V0, although they are not compactly supported
in the open cell and are not claimed to lie in the causal generator
domain.

Reflection commutes with D and S, the latter by its same-parity
response formula. For a truncated translation L_delta, changing
variables in the finite integral gives F L_delta F=L_delta^*.
For the complete separated continuous kernel the same identity
follows by replacing (x,y) by(ell-x,ell-y); its argument changes
from s ell+x-y to s ell+y-x. Consequently FTF=T* and FUF=U*.
In particular a(h)=a(f) and <Tg,h>=<Tf,g> for these real profiles.
Both separation7 pairings are nevertheless evaluated separately
in the certificate. Reflection is a device for selecting this
test triple, not a claim that arbitrary profiles have one parity
or that one sector proves (4).

**Complete scalar enclosures.** The new verification uses directed
60-digit Decimal intervals with the elementary-function contract
of C744v/w. It does not use the floating locator or an eigensolver
as a mathematical premise. Machin's identity with80 terms in
each alternating arctangent series encloses pi; logarithms and
square roots are enclosed by the inherited adjacent-Decimal rule.
All absolute values and sign changes of Decimal endpoints use
exact copy_abs/copy_negate, without default-context rounding.

For d_n=h(k_n), use C744w(12): put y=k_n/2, a=64.25, and evaluate

    (1/2)log(a^2+y^2)-a/[2(a^2+y^2)]-log(pi)
                  -sum_(j=0)^63 (j+1/4)/[(j+1/4)^2+y^2]

with absolute error at most sqrt(2)/[6(a^2+y^2)]. This is the
previously assessed digamma recurrence and sector remainder,
including n=0; no differentiated or new asymptotic is assumed.

The full positive response is evaluated in its square form, with
alpha_n=sqrt(2)nu_n, eta_p=(-1)^p, c_j=2j+1/2:

    <Su,u>=sum_(p=0,1) sum_(j>=0)(1-eta_p 3^(-j-1/4))
         [sum_(n mod2=p) alpha_n c_j u_n/(c_j^2+k_n^2)]^2. (21)

Sum j<1024 directly. Put C=2048.5 and add the leading remainder
sum_p(sum_(n mod2=p)alpha_n u_n)^2/(2C). By C744v(10), the absolute
error of this tail replacement is at most

    [C^-2+2k_15^2(1/(6C^3)+C^-4)
          +3^(-1024-1/4)(1/(2C)+C^-2)]
                      *sum_p(sum_(n mod2=p)|alpha_n u_n|)^2. (22)

This follows from the cited entrywise tail estimate by multiplying
by |u_n u_m| and summing, with no omission of opposite-sign products.
All prefix products in(21) keep their signs before squaring. Both
<Sf,f> and <Sg,g> are enclosed with(21)-(22); the latter is retained
separately to distinguish the comparison from the actual form.

Every prime power is enumerated by exact integer factorization and
3^(s-1)<n^2<3^(s+1), for s=7,14; the upper enumeration endpoint4000
satisfies4000^2>3^15. The counts are16 and334. At s=14, n=2187 is
represented as the exact zero translation, including its full
scalar identity coefficient. For all other delays delta=s ell-log n,
the intervals certify its strict sign. For output index i and input
index j, the unnormalized translation integral is

    [-eta_i eta_j k_i sin(k_i delta)+k_j sin(k_j delta)]
                     /(k_i^2-k_j^2),   delta>0, i!=j;
    [k_i sin(k_i delta)-eta_i eta_j k_j sin(k_j delta)]
                     /(k_i^2-k_j^2),   delta<0, i!=j.

For i=j>0 it is
(ell-|delta|)cos(k_i delta)/2-sign(delta)sin(k_i delta)/(2k_i),
and for i=j=0 it is ell-|delta|. Multiply by nu_i nu_j.
These are C744w's exact finite-interval antiderivatives with their
zero-extension overlaps. Sines and cosines are reduced by an
integer multiple of pi/2; every reduced interval has absolute
value<.786. The degree31 sine and degree30 cosine Taylor
polynomials have absolute errors bounded by |r|^33/33! and
|r|^32/32!, respectively. Thus every entry and every signed
contribution is enclosed, rather than replacing a sum by the sum
of absolute operator norms.

For the remaining continuous operator, sum j=1,...,7 exactly in
its rank-one separated form, using exp(-ell c_j)=3^(-j-1/4).
For each pairing (u,v), the entire j>=8 remainder has absolute
value at most

    [3^(-8-1/4)]^(s-1)
        /[(33/2)(1-3^(-(s-1)))] *||u||_2||v||_2.     (23)

Indeed a row or column integral is at most
sum_(j>=8)exp[-(s-1)ell c_j]/c_j; bound1/c_j by2/33
and sum the geometric series. This is precisely the complete
tail method of(8), starting at j=8. The j=0 separated term
vanishes by the exact moments already verified, whereas the
single-cell j=0 term in(21) is retained. No continuous term,
prime power, signed product or moment error is left unpaid.

The resulting outward decimal displays are

    a(f)+a(h)-2<Uf,h> in (3.321932,3.322217),
    <Dg,g>-2[<Tf,g>+<Tg,h>] in (-3.853351,-3.852835),
    Q_D(f,g,h) in (-.531418,-.530619),
    <Sg,g> in (1.302786,1.302899),
    Q_actual(f,g,h) in (.771368,.772279).              (24)

Full intervals, exact free numerators, all coefficients, all
diagonal entries, all350 prime contributions, response remainders,
continuous remainders and checks are saved in
`scripts/separation-seven/signed-diagonal-stop-545.json`.
Reproduce from the active notebook:

    python3 scripts/separation-seven/signed-diagonal-stop-545.py

Seven final checks pass, with no remaining failed assertion. The
earlier draft's context-rounding defect in Decimal absolute values
and negation is retained in
`scripts/separation-seven/signed-diagonal-development-545.json`;
that artifact is explicitly not a certificate. The final evidence
was regenerated after the fix. The finite floating locator and its
full matrices remain separately labeled uncertified in
`scripts/separation-seven/signed-diagonal-locator-545.json` and
`scripts/separation-seven/signed-diagonal-locator-545.npz`.

To interpret this as a covariance obstruction, for the fixed f,h put
b=P0(Tf+T*h). The complete diagonal-middle variational debt obeys

    sup_(v in V0)[2Re<b,v>-<Dv,v>]
         >=2Re<b,g>-<Dg,g> >3.852835,                 (25)

whereas the entire available endpoint energy minus the actual remote
coupling is<3.322217. This disproves the sufficient payment even
if the complete supremum were infinite. There is no need to assume
positivity of the neutral D restriction, identify its inverse,
or replace an infinite inverse by a finite one. Any legitimate
diagonal-middle square completion must include this particular
variational test and therefore cannot fix the deficit by adding
more middle modes. The previous raw row and derivative stops do
not imply(25); it retains the signed operator and exact neutrality.

Finally, the core proof in Section1 supplies compact smooth neutral
approximations in the logarithmic form norm. All terms in(17),(18)
are continuous in that norm, since T,U,S are bounded and D is the
diagonal form. Hence sufficiently close such triples still have
Q_D<0 and Q_actual>0. This justifies the obstruction on the
original smooth neutral class without asserting a uniform H2 budget
or treating the cosine vectors as original generator-domain vectors.
The obstruction itself does not use c_*, C744y's contraction, or
an unreplayed middle inverse. Its response-identity input and the
new interval proof retain their stated analytic qualifications.

Abandon the diagonal-only middle-energy comparison, even with its
signed full covariance. At least some of the actual positive middle
response must be paid into the comparison. No assertion is made that
a finite response prefix suffices, or that the full residual(4)
has either sign. This new local specialization is independently
unaudited; all RH, other-separation, strict H2, C744q margin,
non-neutral and global assembly gaps remain.

### 8. A fixed positive response prefix still leaves an unpaid direction

This is step546,12 November2026, one research attempt under unchanged
assessment541/comparison542. It implements exactly the continuation
prescribed after Section7: retain j=0,...,31 of(21) in each parity.
Write S_32 for this bounded positive finite-rank response. On V0 cubed,

    Q_32(f,g,h)=a(f)+a(h)+<Dg,g>+<S_32 g,g>
           -2 Re[<Tf,g>+<Tg,h>+<Uf,h>],
    Q_actual=Q_32+<(S-S_32)g,g>.                       (26)

Since S-S_32>=0, nonnegativity of Q_32 everywhere would be a sufficient
comparison. Nothing allows replacing its middle inverse by a finite
inverse. Instead we exhibit one negative variational value; no inverse,
coercivity constant c_*, eigenvalue accuracy or RH premise is needed.
Both endpoint forms remain complete, and U is the actual operator(1).

**Exact neutral data.** Let N=512. Use(19)-(20) for2<=n<=511, with
free coefficients f_n=F_n/2^40 and g_n=G_n/2^40. The complete integer
arrays F_n,G_n, in increasing n, are specified by the keys
`f_free_numerators`, `g_free_numerators` of
`scripts/separation-seven/response-prefix-direction-546.json`.
Its SHA256 is
`f39d45d9754d0415f5180e2cb5803d8152bfbaba3eb34130b4bf4b91b81da013`.
These finite exact data are part of this certificate, not approximate
coefficients. Set all higher coefficients to zero. All odd G_n are
zero, so g=Fg for reflection F; set h=Ff. The two low coefficients
are defined by(20), not rounded to dyadics. The explicit moment
identities in Section7 prove f,g,h in V0 with both moments exactly
zero. The same reflection calculation gives a(h)=a(f). The real
triple suffices to refute a comparison asserted for all complex triples.

`response-prefix-locator-546.py` used the previous finite matrices to
select these data. Its tests at8,16,32,64,128 and512 modes and both
reflection sectors, all saved in the matching JSON/NPZ files, are
uncertified diagnostics only. They are not positivity results at the
smaller sizes, proofs of exact moment vanishing, or inverse estimates.
The certificate below treats the chosen integers as arbitrary exact
input and uses none of the locator's eigenvalues or inverses.

**Complete head forms.** Reuse the audited C744w matrix M0 representing
the512-mode compression of D+S+256C*C. On the present exactly neutral
vectors it equals the complete a. Its stored binary64 entries have
the analytic and elementary error ledger C744w(12)-(15), including
the entire response tail. Hash comparison with the step541 audit
pins the archive and both imported arithmetic implementations; this
does not assert an independent replay of them in the present turn.

For clarity, the exact directional head error used here is stated
explicitly. Put r_n=sqrt(2)/[6(64.25^2+k_n^2/4)], C=131072.5 and

    t_n=C^-2+2k_n^2[1/(6C^3)+C^-4],
    E_nn=r_n+2nu_n^2 t_n,
    E_nm=nu_n nu_m(k_n r_n+k_m r_m)/|k_n^2-k_m^2|
          for n!=m of the same parity,
    E_nm=0 for opposite parities.

For any finite real vector u the error is at most

    epsilon_A(u)=10^-7 (sum|u_n|)^2
                       +sum_(n,m) E_nm |u_n u_m|.     (27)

This is the entrywise bound already proved in C744w, multiplied by
the actual coefficient magnitudes and summed; it is not an operator
norm inferred from a sampled eigenvalue. The elementary10^-7 includes
the moment penalty and the D entry's roundoff, as clarified by its
audit. Opposite-parity penalty entries are retained before exact
neutrality cancels their true quadratic form. Head symmetrization
preserves the symmetric entrywise bounds. Directed evaluation gives
epsilon_A(f)<.000078795 and epsilon_A(g)<.000162865. Both full endpoint
energies are paid with(27); the second head evaluation bounds a(g)
only to distinguish the original form from the comparison.

For Dg in(26), use the same exact digamma recurrence and the same
DLMF5.11.2/5.11(ii) sector remainder as C744w(12), now with shift256:
put y=k_n/2 and b=256.25, and enclose h(k_n) by

    (1/2)log(b^2+y^2)-b/[2(b^2+y^2)]-log(pi)
            -sum_(j=0)^255 (j+1/4)/[(j+1/4)^2+y^2]

with error sqrt(2)/[6(b^2+y^2)]. The recurrence is exact and
Re(b+iy)>0 gives the identical sector multiplier2sqrt(2). Only the
shift is changed to narrow this scalar enclosure; no new asymptotic
or differentiated remainder is imported. The64 squares defining
<S_32 g,g> are evaluated directly by(21), keeping all signs inside
each squared projection and retaining the single-cell j=0 terms.
No response tail is asserted small in this middle comparison: the
entire S-S_32 is deliberately discarded and recorded separately.

Both separation7 pairings use the audited Mc+Mg archive. Each exact
Mc,Mg entry has elementary error10^-7, already including its continuous
tail, and their binary addition costs less10^-8. Thus each pairing
<Tu,v> is enclosed about its exact stored-matrix scalar product by

    2.1*10^-7 (sum|u_n|)(sum|v_n|).                    (28)

Both actual pairings are evaluated separately. Their respective errors
are less.000002656; neither is replaced by its absolute operator norm.

**Actual remote pairing and its complete error.** Rebuild the334
remote prime translations by(1) and Section7's exact cosine
antiderivatives. The integer test3^13<n^2<3^15 and exact prime-power
factorization certify completeness;4000^2>3^15. The n=2187 term is
the exact identity translation, multiplied by its enclosed weight.
Every other delay has its strict sign verified by a directed interval.
All weights and delays are enclosed with60-digit Decimal arithmetic;
conversion to binary64 has absolute error<10^-16 for each. The
complete weight sum is in(52.2014392229,52.2014392230), hence<60.

Here is the arithmetic specialization for this new remote matrix,
under C744w's explicit IEEE754 contract. All used modes n<512 and
|delta|<ell are within the range of its sin/cos estimate(14). Constants
ell,pi and normalization have the same relative rounding controls;
Machin's formula supplies pi. The implementation uses the same degree
21/20 Taylor polynomials after quadrant reduction, with every reduced
argument's magnitude<.786. Thus sine/cosine errors are bounded by
10^-14(1+k_n). For unequal indices,

    (n^2+m^2)/|n^2-m^2|<1024,
    [k_n(1+k_n)+k_m(1+k_m)]/|k_n^2-k_m^2|<1025.

The normalization nu_n nu_m<4, so the contribution of trigonometric
errors is<4.1*10^-11 per unweighted translation entry. The denominator
relative error is<10^-11 by C744w's integer-gap argument. The absolute
normalized exact numerator divided by the denominator is bounded by
4/|k_n-k_m|<.7, so its denominator contribution is<7.1*10^-12.
Product, normalization and numerator arithmetic contribute<10^-12:
each is a bounded number of binary operations, with the same
4/|k_n-k_m| bound controlling subtraction, and unit roundoff2^-53.
The diagonal formula has trigonometric error<4*ell*3.1*10^-11/2
plus its smaller sine-over-frequency error and elementary rounding;
the zero mode is evaluated directly. In all cases the deliberately
loose bound10^-9 covers one normalized unweighted translation entry.

Multiplying by all positive weights therefore contributes<6*10^-8.
There are334 weight-conversion errors, each<10^-16; their entries have
magnitude at most1+10^-9 since a truncated translation is a contraction.
The334-term accumulation has gamma_334<4*10^-14, with total absolute
sum<61. Product rounding and conversion add less10^-11 in total.
Consequently the complete stored remote prime matrix Uhat has error
less10^-7 per entry. Its signed scalar product is evaluated with
directed Decimal arithmetic after exact conversion of its binary64
entries; a floating dot product supplies no certification here.

The whole remaining continuous operator is paid, without needing a
finite continuous approximation. The row/column estimate of Section2
gives

    ||K14||<=kappa14
      =1/[3^16*3^(1/4)*(5/2)*(1-3^-13)]<7.061*10^-9.

Thus the complete actual pairing <Uf,h> is enclosed about
<Uhat f,h> with error

    10^-7 (sum|f_n|)(sum|h_n|)+kappa14||f||_2||h||_2.  (29)

This encloses the actual continuous contribution in either sign;
it does not replace U by a fitted covariance or delete that term.
The j=0 separated response vanishes by the exact moments, as in(1).
The full new prime matrix is saved in
`scripts/separation-seven/response-prefix-remote-546.npz`.

**Certificate and implication.** All remaining operations use directed
60-digit Decimal intervals. Basic operations, correctly rounded
ln/sqrt with adjacent-Decimal widening, exact endpoint negation/absolute
value and the Machin interval are the same contracts as Section7.
No default-context rounded unary operation is used. Every scalar
product of a stored matrix is accumulated outward, not passed through
an unverified BLAS reduction. The resulting outward displays are

    a(f)+a(h)-2<Uf,h> in (2.7017288,2.7020494),
    <Dg,g>+<S_32 g,g>-2[<Tf,g>+<Tg,h>]
                                      in (-2.7022561,-2.7022202),
    Q_32(f,g,h) in (-.000528,-.000170),
    <(S-S_32)g,g> in (.0940515,.0943919),
    Q_actual(f,g,h) in (.093538,.094207).              (30)

The full intervals, exact input integers, interval coefficients,
all512 diagonal enclosures,64 response terms,350-prime coverage
(16 through the pinned audited input and334 explicitly here),
head/error contributions, remote data and nine passing checks are in
`scripts/separation-seven/response-prefix-stop-546.json`. Reproduce:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/response-prefix-stop-546.py

For fixed f,h, (30) also says the full variational debt for D+S_32
is at least2.7022202, while the available endpoint energy after the
actual remote pairing is less2.7020494. Adding further middle
variational modes cannot repair this inequality for the fixed
comparison. This conclusion needs no existence of a restricted
inverse: the displayed finite g is already an admissible test.

Section1's neutral core proof transfers both strict signs to some
compact smooth neutral triples, since D is continuous in its form
norm and S,S_32,T,U are bounded. It asserts no explicit H2 budget.
The result stops this fixed32-square comparison, not every larger
prefix and not the actual residual(4). Repeated prefix enlargement
is not justified by this obstruction alone. Preserve all earlier
stops, and independently audit this new narrow-margin certificate
before choosing another response/infinite-covariance development.
The result was an unaudited local REPRODUCTION/specialization at
step546; Section9 records its later independent audit. It is not a
new source theorem, negative original
smooth witness, or RH disproof. All other-separation, C744q, strict
H2, non-neutral and global assembly gaps remain.

### 9. Separate conceptual audit of Section8 — 12 November2026, step548

**Result and scope.** The fixed32-response obstruction(26)-(30) is
upheld, conditional on the imported analytic response identity and
the stated IEEE754/Decimal execution contracts. The audit uses the
pre-existing SPECIALIZE assessment546/comparison547 and is
REPRODUCTION: newly checked local evidence, not an inequality beyond
the construction or checked sources. It does not audit the inverse
completion(2)-(4), Sections4/6/7's other stops, or prove a sign for
the full three-cell residual. No c_* value, restricted inverse,
C744y's positive two-cell inequality, H2 existence or RH assumption
enters this variational test.

**Exact moments, forms and signs.** The complete direction JSON has
the Section8 hash and exactly510 integer free coefficients per
profile, with denominator2^40. Equation(19) is the ratio of the
two explicitly integrated exponential moments within each parity:
nu_n/nu_0=sqrt(2) for even n>=2, and nu_n/nu_1=1 for odd n>=3.
Consequently(20), extended to511, annihilates both moments exactly.
All odd middle coefficients vanish. Reflection sends each e_n to
(-1)^n e_n, so h=Ff and g=Fg are exact identities, not approximate
projections. D is diagonal; S has only same-parity entries by(21).
Thus a(h)=a(f) exactly, even though stored matrix entries need not
satisfy a symbolic reflection identity. The head scalar error(27)
encloses a(f); using it twice pays both endpoints. The exact
256C*C term vanishes on these vectors; its stored rounding error
is still charged in10^-7. No positive penalty is spent twice.

For the separated kernel, polarizing the unconditional L742(9)
gives H(f,tau_s h)=-<T_s f,h>. Only the forward delay can overlap;
its coefficient is Lambda(n)/sqrt(n), with factor2 appearing only
when assembling the real off-diagonal energy. The geometric
continuous expansion is absolutely uniform on the separated
square. Its j=0 product vanishes by the exact moments. This checks
the orientation and normalization of both T pairings and U in(26),
including its negative sign in the energy. The cosine
antiderivatives in C744w Section3 integrate over the actual overlap
for each sign of delta. The zero delay is the identity, including
the constant mode. Both signed T products and the signed U product
are evaluated separately. All64 prefix squares retain the signed
projection before squaring, including j=0; S-S_32 is positive by
the imported full response identity, not by a numerical truncation.

The complete head entry allowances in(27) are C744w(12)-(15), whose
separate534 audit is reused. Both the head archive and its two
arithmetic implementations match that audit's hashes, as well as
the541 pins. Diagonal and unequal-index analytic errors are charged
by the appropriate separate formulas; the equal-index case never
uses a divided difference. Both response tails and the combined
elementary head/penalty allowance remain included. The Dg recurrence
with256 shifts is exact on Re(z)>0. DLMF5.11.2/5.11(ii), n=1,
gives the omitted-term bound (1/12)|z|^-2 sec^3(arg(z)/2)
<=sqrt(2)/(6|z|^2), also at k_0=0. Thus it encloses all512
diagonal values without a derivative-remainder assumption. The two
entry errors and the charged addition roundoff of Mc+Mg give(28).

**Complete remote ledger.** Independent sieve/exponent enumeration
agrees with every one of the334 trial-division records. The strict
integer test3^13<n^2<3^15 and4000^2>3^15 cover the entire possible
range. The only zero delay is2187=3^7; every other delay has a
certified strict sign and satisfies |delta|<ell. Each weight and
delay conversion error is below10^-16. Their entire weight sum is
less52.202<60. None of these are sampled-coverage assertions.

Here n<=511, k_n<2923, nu_n nu_m<4. C744w's range-reduction
proof applies unchanged, with every reduced argument below.786;
the complete replay maximum is less.785396. The degree21/20
Taylor remainders and input/reduction arithmetic give the stated
10^-14(1+k_n) sine/cosine allowance. For unequal indices the
integer gap(n-m)(n+m) gives both ratios<1024 and<1025 in Section8.
Multiplying by normalization gives trigonometric error<4.1e-11.
The exact normalized numerator divided by its denominator has
magnitude<=4/|k_n-k_m|<.7. Denominator relative error<1e-11
therefore costs<7.1e-12; the bounded products, normalizations and
numerator subtraction cost<1e-12 with unit roundoff2^-53.
There is no division by an uncontrolled small difference. For
n=m>0, the cosine term costs at most
4ell(3.1e-11)/2, the sine term at most
2e-14(1+1/k_n), and the overlap-length/input arithmetic is smaller
than1e-12. The zero mode and identity case are direct. Each case
is safely below the uniform10^-9 unweighted-entry allowance.

A truncated translation is an L2 contraction, so each normalized
exact matrix entry has modulus<=1. All334 rounded entries therefore
have modulus<=1+10^-9. Weighted entry errors total<60e-9.
Weight conversion contributes<334e-16(1+10^-9), and multiplication
plus334-term summation contributes less10^-11, since gamma_334
<4e-14 and the absolute weighted sum is<61. Their combined bound
is strictly below10^-7. The proof covers every matrix entry; the
262144-entry bit-for-bit replay is an additional execution check,
not a substitute for this analytic bound.

The whole continuous operator, rather than just a finite prefix,
is charged in(29). Integrating each positive exponential over a row
or column bounds its norm by
sum_(j>=1)exp[-13ell(2j+1/2)]/(2j+1/2), at most
3^(-65/4)/[(5/2)(1-3^-13)]<7.061e-9.
This checks the normalization and both sides of the Schur bound.
Multiplication by ||f||_2||h||_2 pays its contribution in either sign.

**Full arithmetic evidence and runtime.** The independent audit is

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/response-prefix-audit-548.py

It preserves the original artifacts and writes complete evidence to
`scripts/separation-seven/response-prefix-audit-548.json`, plus
`response-prefix-replay-548.json` and
`response-prefix-remote-replay-548.npz` in that directory.
The complete546 generator was replayed at90 Decimal digits. All2871
scalar checks pass: ordinary enclosures nest, and the three purely
upper-error allowances are dominated by their original upper bounds.
For five scalar products, a separate integer accumulation converts
every stored binary64 matrix entry to an exact dyadic rational and
the90-digit coefficient intervals to rational points with rigorous
uncertainty. All five resulting rational enclosures lie inside the
original60-digit centers. This includes1310720 matrix entries across
the five products, without relying on any floating dot reduction.
The exact rational sums, denominators, uncertainty bounds, six
moment-consistency checks and all334 coverage records are saved.
Numerical moment intervals only check consistency: the identities
above, not small residuals, prove neutrality.

An initial audit incorrectly required two-sided nesting of the three
allowances formed from sums of coefficient absolute upper endpoints.
Increasing precision lowers those upper endpoints, so an allowance's
new lower endpoint can fall below its old lower endpoint. Only its
upper endpoint is used by inflate. The saved
`response-prefix-audit-first-pass-548.py/json` retain all three failed
checks; the corrected audit checks nonnegativity and upper domination.
This was an audit-check error, not a defect in546's sign enclosure.
There is also a harmless raw Decimal unary minus in546's overlap
assertion; that assertion is independently checked with exact endpoint
negation in548. All enclosure operations use exact endpoint negation
and absolute value, explicit directed contexts and widened ln/sqrt.
The wording in Section8 about default-context operations applies to
the enclosure calculation, not this auxiliary support assertion.

The observed runtime is Python3.15.2, NumPy2.5.4, arm64, with binary
radix2,53 significand bits and fegetround()==0. This identifies the
runtime and its current rounding mode; it does not formally prove
the IEEE754/Decimal implementation contracts. Those qualifications
remain explicit. No library trigonometric or eigensolver accuracy
is imported. All original input hashes remained unchanged.

The full audit retains the strict outward bounds

    Q_32 in (-.000528,-.000170),
    Q_actual in (.093538,.094207).

Equivalently this fixed middle test demands more than2.7022202,
while both endpoints after the complete remote pairing supply less
than2.7020494. The discarded response remains in
(.0940515,.0943919). Thus the negative comparison and positive
actual form are separately certified, with all errors charged.

**Smooth transfer.** Section1's cutoff proof uses the cosine H1
identity with zero sine boundary terms; it does not assert that the
cosine vectors belong to the causal generator's operator domain.
Splitting frequencies at delta^-1 gives the stated
O(delta log(1/delta)) squared form-norm error. The moment map is
L2-continuous, and the two fixed separated positive bumps have
distinct ratios C_+/C_-, so their correction matrix is invertible.
The correction tends to zero in V and enforces both moments exactly.
Hence N is dense in V0 independently of any coercive constant.
For each of f,g,h choose these approximants. Reflection may be
preserved by h_j=Ff_j and symmetrizing g_j; it preserves V and the
neutral subspace. D is continuous as a form on V, and S,S_32,T,U
are bounded on L2. Both real quadratic values therefore converge
simultaneously to their displayed strict signs. Some sufficiently
close compact smooth neutral triple retains both signs. No numerical
approximation threshold, prescribed H2 norm or budget is asserted.

This closes only the Section8 audit. The actual full residual,
other separations, C744q's strict margin, H2 slack/existence,
non-neutral directions and global assembly remain open.

### 10. Full-certificate norm extraction — 13 November2026, step705

**Scope and inputs.** Keep the Hypotheses, the actual restricted
A0,E,K,R of(2), and C744y unchanged. This is REPRODUCTION under the
pre-existing SPECIALIZE assessment704: an application of the imported
closed-form and bounded-block tools, not a new general theorem.
Teschl Theorems2.13/2.18 and spectral calculus, cited above, supply
the restricted energy coordinates. Dritschel--Rovnyak LemmaA.1,
cited above, supplies the bounded-block context. Only the following
quantitative metric conversion is derived here. No outside source,
original certificate factor, response, cutoff or penalty is changed.

On the full penalized two-component form domain put
A=D+S+256 C*C, B=[[A,-T*],[-T,A]], and Gamma=diag(A,A).
Use P2,Q2,F=Q2 B P2,M=P2 B P2 as in C744y(4)-(5).
Its full certificate, including the high-output covariance, gives

    Q2 B Q2>=tau I, M-F*F/tau>=delta I,
    tau=143/100, delta=13999/500000=.027998.             (31)

Indeed F*F=F_<*F_<+G*G, G*G<=U, and C744y(22) pays
M-F_<*F_</tau-U/tau. Thus(31) keeps all mixed products.
The finite factor and entry bounds in C744y(20)/Section5 give

    ||F_<||<3.162+eF,
    eF<.000000181+3sqrt(65024*512)*10^-7
       <.001731181.

The product block has no extra sqrt2 factor: its repeated diagonal
norm and off-diagonal norm are bounded by the sum of the three
single-block factor norms, as in C744y. Since the finite and high
output ranges are orthogonal, and ||Z||^2=256,

    ||F||^2 <= ||F_<||^2+||G||^2
      < (3.163731181)^2+256/5000+1/125000
      =10.060402985631654761 < 10.061=:s.               (32)

This pays the entire high covariance, not a finite-section norm.
For p=P2 u and q=Q2 u, square completion in(31) yields

    b(u,u)>=delta||p||^2+tau||q+Fp/tau||^2.

For 0<m<tau, subtracting m(||p||^2+||q||^2) from
the right side gives exactly

    (tau-m)||q+Fp/(tau-m)||^2+(delta-m)||p||^2
                           -m||Fp||^2/[tau(tau-m)].

Consequently b>=m I on the full form domain whenever

    (delta-m)tau(tau-m)-m s>=0.                        (33)

The left side divided by tau(tau-m) is strictly decreasing
on(0,tau). Its unique zero in(0,delta) is bracketed by exact
rational arithmetic as

    .004716385 < m_opt < .004716386.

At m=.004716385 the left side of(33) is exactly
15172162647/4000000000000000000>0; at .004716386 it is
-208485190393/25000000000000000000<0. Set m=.004716385.

**Energy metric, projections and both mixed blocks.** C744v's full
||T||<4.71=:t implies, as form inequalities,

    Gamma=B+[[0,T*],[T,0]] <= B+t I <= (1+t/m)B.

Thus B>=eta Gamma, eta=m/(m+t). No upper bound on the
unbounded A is assumed. Restrict to exactly neutral f,g in V0:
both penalties vanish, and <Tf,g>=<P0 Tf,g>=<Kf,g>.
Now substitute f=Ex,g=Ey using the actual E of(2), whose range
is V0. This is not a projected unrestricted inverse. We obtain
for arbitrary independent complex x,y in H0

    2Re<Rx,y><=(1-eta)(||x||^2+||y||^2).

For x!=0 and Rx!=0 choose y=||x||Rx/||Rx||; the zero cases
are immediate. Hence ||R||<=1-eta, with the exact result

    ||R|| <= 942000000/942943277,
    ||R||^2 <= 887364000000000000/889142023639498729
             < .998001.                              (34)

Both adjoint orientations and all neutral projections are retained.
In particular the two defects exceed .001999 I, but this falls
short of the1/4 floor needed to exclude the fixed windows.

**Decision and limits.** Even replacing m in this scalar comparison
by its optimal zero cannot reach ||R||^2<3/4: the lower endpoint
of the resulting scalar *upper-bound values*, obtained from
m=.004716386, has square
5546025000000000000/5557137650104225249>3/4. This is not a
lower bound on the actual norm. The test therefore stops this
scalarized extraction; it does not show that all uses of the
unchanged directional certificate fail. No conclusion about actual
window nonemptiness, localized coupling or the full S3 sign follows.
No tau, cutoff, allocation or certificate was tuned after a miss.

Reproduce the new scalar arithmetic and inherited artifact-identity
checks with

    python3 scripts/separation-seven/defect-window-norm-705.py

The full exact rational ledger,17 checks, seven original artifact
hashes, required3/4 threshold and empty arithmetic-failures list
are in `scripts/separation-seven/defect-window-norm-705.json`.
All relevant exact values and checks were inspected. This is not
another replay of C744y's upstream proof. Its analytic and
IEEE754/Decimal qualifications and the restricted-core setup remain;
the original c_* source certificate remains unreplayed. This is
local progress within assessed standard methods, not a claim of
mathematical novelty or an RH candidate.

## Mathlib

Full matching coverage for this neutral three-cell residual and
its form-core specialization is not checked. Standard Hilbert
space, spectral calculus and positivity facts are mathematical
inputs here; no Lean theorem name or formal verification is
claimed. The scalar certificate and finite diagnostic have the
distinct scopes stated above. This is not absence evidence.
The full signed-density comparison (12)-(16) and its coefficient
obstruction have not been checked in Mathlib; no Lean verification
is claimed for the standard integral inequalities or this application.
The exact-neutral signed covariance obstruction(17)-(25) and this
Decimal certificate have not been checked in Mathlib. The finite
cosine formulas and standard form continuity are supporting mathematics,
not a matching formal theorem or evidence of absence from Mathlib.
The fixed-prefix comparison(26)-(30), its exact data and arithmetic
ledger have not been checked in Mathlib; no matching formal theorem
or formal verification of the numerical runtime is claimed.
Section10's full quantitative norm specialization is not checked
in Mathlib; supporting form order and spectral calculus are not
asserted to be a matching theorem. Unknown coverage is not absence.
