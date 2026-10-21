# Lemma 408: positive fixed-head signed cubic leading coefficient

## Hypotheses

Use the actual functions, ordinary jets, constants and finite response
heads in L407. In particular c=1/(4pi), ell=log H,

    I_N(H)=integral_[H,2H] d_N(t) B0_N(t) dt.

N is a fixed positive integer independent of the real parameter H tending
to infinity. Use L407's audited sharp arithmetic reduction (9), with all
coefficients specified by its (4), both S and T terms, delta=11/20,
and its O_N(H^(71/120)) remainder. No RH, phase independence, growing
head, full-response, clipping or nonzero-value hypothesis is assumed.

## Conclusion

For u>=1 define the positive rational number

    A_u=u^(-2) sum_(a=1)^u gcd(a,u).

For each triple m,n,k put u=mn/gcd(mn,k), the numerator of mn/k
in lowest terms. Then

    I_N(H)=beta_N H(log H)^2+o_N(H(log H)^2),              (1)
    beta_N=(17 c^3/20160)
                    sum_(m,n,k<=N) (mn)^(-2) k^(-3) A_u>0. (2)

Every rational twist and exact analytic weight contributes to this
coefficient or to a proved smaller remainder. All zero-carrier
resonances are retained; their total is O_N(H), below this scale.
In particular beta_1=17/(1290240 pi^3).

This is local REPRODUCTION: specialization of the assessed finite
Hurwitz/Mellin inputs and audited L407, followed by exact finite signed
algebra. No originality beyond the inspected sources is asserted.
The separate step-115 critical audit below validates the fixed-N
coefficient and its analytic error. This result does not exchange
the H and N limits, evaluate the complete signed physical statistic or
a clipped statistic, or establish a total pencil margin, common-zero
upper count, global mixed positivity, zero-exclusion range or RH.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-14-fixed-head-cubic-leading-coefficient.md`.
Its exact target and fixed-N scope match this calculation. L407's
step-111 audit and the saved step-112 source comparison are reused.
The checked recent cubic records contain no evaluation of (1).
L394/L399/L400 are different-weight failures, not premises. The
excluded unproved cubic theorem is not used. We do not reprove a
Voronoi functional equation or use the inconsistent expanded polar
factor identified in the assessment.

### 1. Combined ordinary-jet pole for every rational twist

For fixed coprime positive integers u,v and p=(p1,p2,p3), with
0<=pi<=2, put d=p1+p2+p3. Let C_p(j) be L407 (8), including its
sign (-1)^d. Define on Re s>1

    D_p(s)=sum_(j>=1) C_p(j) exp(-2pi i vj/u) j^(-s),
    Z_a(s)=sum_(n>=1,n=a mod u) n^(-s)
           =u^(-s) zeta(s,a/u), 1<=a<=u.

Import A. Fazzari, *A Voronoi summation formula for the shifted triple
divisor function*, arXiv:2306.15553v1 (27 June 2023),
[(3.5), p. 10](https://arxiv.org/html/2306.15553v1#S3),
the finite three-progression identity. Its numerator here is -v and
modulus u; (-v,u)=1. Its progression classes include a=u and all
nonunits. Differentiating the three independent shifts on the absolutely
convergent right half-plane gives exactly

    D_p(s)=sum_(a,b,c=1)^u exp(-2pi i vabc/u)
                              Z_a^(p1)(s) Z_b^(p2)(s) Z_c^(p3)(s). (3)

This differentiation is of a locally uniformly absolutely convergent
series, not of an asymptotic error. Equal derivative orders need no
multinomial factor: each of the three ordered factors is differentiated
once to its assigned order. Equation (3) also follows by expanding
the three progression series, so no separate-pole expansion at unequal
shifts is needed.

[DLMF 25.11(i)](https://dlmf.nist.gov/25.11#i) supplies the sole
Hurwitz pole and residue one. Thus, near s=1,

    Z_a^(p)(s)=(-1)^p p!/[u(s-1)^(p+1)]+an analytic function.

Taking the product in (3) proves

    D_p(s)=A_u (-1)^d (p1! p2! p3!) (s-1)^(-d-3)
                                      +O((s-1)^(-d-2)).          (4)

All lower Laurent terms are retained in the O term; the order statement
is local for these fixed parameters. To verify the coefficient, sum
the third residue class first:

    u^(-3) sum_(a,b,c=1)^u exp(-2pi i vabc/u)
       =u^(-2) #{(a,b):1<=a,b<=u, u divides ab}
       =u^(-2) sum_(a=1)^u gcd(a,u)=A_u.

The first equality uses finite character orthogonality and (v,u)=1.
For a fixed a the congruence has exactly gcd(a,u) solutions b among
these u classes. In particular A_u is real, strictly positive and
independent of v, and A_1=1. No class was removed before orthogonality.
This evaluates the combined coalesced pole directly.

### 2. Smooth Mellin calculation and absolute sharp transfer

Fix psi in C_c^infinity((0,infinity)) and let
psi_hat(s)=integral_0^infinity psi(x)x^(s-1)dx.
Import Mellin inversion [DLMF 2.5.2](https://dlmf.nist.gov/2.5.E2);
here the compact smooth support makes the transform entire and
rapidly decreasing on every fixed vertical strip. More explicitly,
the substitution x=exp(y) and repeated integration by parts give
|psi_hat(sigma+it)|<=C_(psi,B)(1+|t|)^(-B), uniformly for
1/2<=sigma<=2 and every B. Absolute convergence at Re s=2 permits
the series/integral interchange, giving

    sum_j C_p(j) exp(-2pi i vj/u) psi(j/X)
                 =(1/(2pi i)) integral_(2) D_p(s) X^s psi_hat(s)ds. (5)

The needed growth bound comes from
[DLMF 25.11.5](https://dlmf.nist.gov/25.11.E5), Apostol (1976),
(25), p. 269: its hypotheses are a>0, Re s>0, s!=1 and integer
cutoff >=0. Use cutoff zero and a=a_class/u in (0,1]. The fractional
part in its integral is bounded by one, so for real part bounded
below by 3/8 and |Im s|>=2 its integral is O(1+|s|); the finite
term and the term with denominator s-1 are also polynomially bounded.
On the enlarged closed strip 3/8<=Re s<=17/8 this gives
O_u(1+|Im s|) for |Im s|>=15/8, by the same integral bound.
Cauchy disks of radius 1/8 about points with 1/2<=Re s<=2
and |Im s|>=2 stay in that strip and avoid the pole. Thus the
same bound holds for
the first two s derivatives. Multiplication in the finite sum (3)
gives D_p(s)=O_(u,p)((1+|Im s|)^3) on 1/2<=Re s<=2 away
from a fixed neighborhood of s=1. Finite portions off that pole
are bounded by meromorphy.

Shift (5) to Re s=1/2. The only crossed pole is s=1. With B>5,
the horizontal integrals at heights +/-T are
O_(u,p,psi)(X^2 T^(3-B)) for each fixed X>=1 and tend to zero;
the new vertical integral is absolutely O_(u,p,psi)(X^(1/2)).
Expanding X^s= X exp((s-1)log X) in the residue, (4) gives

    sum_j C_p(j) exp(-2pi i vj/u) psi(j/X)
      = A_u m_p X(log X)^(d+2) integral psi
        +O_(u,p,psi)(X(log X)^(d+1)+X^(1/2)),            (6)
    m_p=(-1)^d p1! p2! p3!/(d+2)!.

The lower poles and derivatives of psi_hat give powers at most d+1;
there is no differentiation of (6) with respect to shifts. This proof
uses only the finite continuation, not the full source Voronoi theorem.

For completeness, transfer (6) to the actual interval X<j<=2X
using an absolute boundary bound. Fix 0<epsilon<1/4. Choose a real
smooth psi_epsilon between zero and one, supported in (1,2), equal
to one on [1+epsilon,2-epsilon], with integral 1+O(epsilon).
Choose a nonnegative smooth boundary majorant chi_epsilon which is
at least one on [1,1+epsilon] union [2-epsilon,2], supported in
[1-epsilon,1+2epsilon] union [2-2epsilon,2+epsilon], and has
integral O(epsilon). These functions are fixed before X grows.

Apply (6) with u=v=1 and p=(0,0,0) to chi_epsilon. Its coefficients
are the unsigned d_3(j), and A_1 m_p=1/2. Hence

    sum_(j in boundary bands) d_3(j)
       <= O(epsilon) X(log X)^2+o_epsilon(X(log X)^2).   (7)

For X<j<=2X the bound |C_p(j)|<=d_3(j)(log j)^d from L407
and log j<=log X+log 2 imply that replacing the indicator by
psi_epsilon costs in absolute value at most
O_p(epsilon)X(log X)^(d+2)+o_epsilon(X(log X)^(d+2)).
This covers j=X or j=2X when either is an integer: the majorant
includes those points, while the original indicator keeps its exact
left-open/right-closed convention. The same bound covers complex
additive phases, since their absolute value is one.

Equation (6), followed first by X tending to infinity and then by
epsilon tending to zero, now proves the sharp statement

    sum_(X<j<=2X) C_p(j) exp(-2pi i vj/u)
       =A_u m_p X(log X)^(d+2)+o_(u,p)(X(log X)^(d+2)).  (8)

Formally, the limsup of the normalized difference is O(epsilon)
for every epsilon, so it is zero. No vanishing-width uniformity or
short-interval theorem is asserted. The signed sum was never bracketed
by positive main terms; positivity was used only for its absolute
unsigned boundary mass.

### 3. Uniform leading analytic weights

Use the exact formulas for D0,D1,D2 and P1 in L407 (4).
For tau=t-i delta, H<=t<=2H, L(tau)=ell+O(1).
The sector-qualified digamma expansion
[DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2), already underlying
L391's polygamma bounds, applies to z_+=1/4+i tau/2 and
z_-=1/4-i tau/2. Both have magnitude comparable to H and lie in
fixed sectors |arg z|<=pi-eta with eta>0. It gives
Psi(z)=Log z+O(1/|z|). Since z_+ z_-=tau^2/4+1/16,
the sum of their principal logarithms equals
2Log tau-2log 2+O(H^(-2)); their arguments sum near zero,
so no branch multiple is introduced. Therefore

    Omega(tau)=ell/2+O(1), Omega'(tau)=O(H^(-1)).       (9)

The derivative estimate is the separately controlled L391 bound,
not a differentiation of the O(1) term. All estimates are uniform on
this closed shifted segment. In terms of the formal variables
X=h0, Y=h1/ell, Z=h2/ell^2, the coefficient limits are

    D0 -> X, D1 -> i(Y+X/2), D2 -> -Z-Y-X/4.

For each nu with sum nu_i=3 and d=nu1+2nu2, let a_nu be the
coefficient of X^nu0 Y^nu1 Z^nu2 in P1 after this substitution.
The exact monomial description in L407 says
w_(1,nu) is a finite sum of Omega^b (Omega')^k/L^m with
m=d+b+2k. For k=0, (9) and L=ell+O(1) give the limiting constant
times ell^(-d), with error O(ell^(-d-1)). For k>=1, the term is
O(H^(-k) ell^(-d-2k)), which is smaller than that error.
Consequently every coefficient, including those whose limit is zero,
satisfies

    w_(1,nu)(t-i delta)=a_nu ell^(-d)+O(ell^(-d-1)).    (10)

The finite expansion thus keeps every Omega' contribution until it is
bounded. Its discarded terms do not assume that a_nu is nonzero.
For a fixed twist, L407's complete divisor bound gives
sum_(X<j<=2X)|C_p(j)|=O_(r,p)(H ell^(d+2)), with
X=rH/(2pi). This follows also from its elementary bound on
sum_(j<=2X)d_3(j). Substituting (10) into S in L407 (9)
therefore costs O_(r,nu)(H ell), uniformly at all sample points.
There is no inference from bounded variation alone.

### 4. Complete signed assembly

The substitution above gives J_plus=-X-2Y-Z, J_minus=-Z and

    P1=-(X+2Y+Z)(Y^2+3YZ/2+3Z^2/4-XZ/4)
      = X^2 Z/4-X Y^2-X Y Z-X Z^2/2
                              -2Y^3-4Y^2 Z-3Y Z^2-3Z^3/4. (11)

This uses L407's full P1=M_D J_plus+J_plus^2 J_minus/4;
both parts survive. In particular the missing X^3 and X^2Y
monomials have zero leading weights, not omitted exact coefficients.
Their (10) errors are already covered. For any monomial choose
p with nu_l entries equal to l as in L407. Equations (8) and (10),
with X=rH/(2pi), imply

    S_(r,nu,w_(1,nu))
      = H ell^2 sqrt(r) A_u a_nu m_p+o_(r,nu)(H ell^2). (12)

Indeed 2pi r^(-1/2) X=H sqrt(r) and
log X=ell+log(r/(2pi)); the latter change costs O_(r,nu)(H ell).
The sharp little-o remainder in (8), times ell^(-d), is of the
required size. The real projection in L407 leaves this coefficient
unchanged: A_u, a_nu and m_p are real.

The eight nonzero contributions a_nu m_p in the order displayed
in (11) are exactly

    1/48, -1/24, 1/60, -1/360,
                           1/60, -1/90, 1/420, -1/6720.

Their sum is 17/20160. This can also be checked by the simplex
monomial formula integral_(v_i>=0,sum v_i=1) product v_i^pi
=product pi!/(d+2)!, with the (-1)^d signs retained; the pole
calculation above establishes the same factors without needing this
alternative interpretation.

For the other carrier, every r=mnk is a fixed positive integer.
L407 keeps the exact resonance

    T_(r,nu,w_(0,nu))
               =r^(-1/2) C_p(r) integral_[H,2H] w_(0,nu)(t-i delta)dt.

Its audited bound |w_(0,nu)|<=C ell^(-d), with d>=0,
gives O_(r,nu)(H ell^(-d))=O_(r,nu)(H). Thus no resonance can
contribute to the ell^2 coefficient; none is assumed zero. The finite
sum of these terms is O_N(H). The audited source and connector
remainder O_N(H^(71/120)) is also o_N(H ell^2).

Finally sum (12) over all nu and all m,n,k<=N in L407 (9).
There are finitely many terms before H grows, so every little-o
can be summed without a uniform-in-N assertion. The complete coefficient
is

    c^3 (17/20160) sum_(m,n,k<=N) (mnk)^(-5/2) sqrt(mn/k) A_u,

which is (2), since the weight equals (mn)^(-2)k^(-3).
Every summand is positive and the triple (1,1,1) is present, proving
beta_N>0. This completes (1).

### Verification and qualifications

Reproduction command:

    python3 scripts/discriminant/check_cubic_leading_coefficient.py

The full finite algebra certificate is
`scripts/discriminant/cubic-leading-coefficient-certificate.json`.
Its complete /P1, /polar_terms, /factorization_residual and /tests
were inspected using the scoped JSON inspector with --full. All seven
checks pass, the factorization residual is empty and the eight signed
contributions sum to 17/20160. The finite residue-count checks for
u=1,...,40 support the implementation only; the orthogonality/gcd
argument proves the formula for every u. Analytic bounds in the
certificate are references to the written proof, not numerical evidence.

The achieved remainder is o_N(H(log H)^2), at the required fixed-N
scale. The weight replacement has the stronger O_N(H log H) bound;
the sharp transfer has only the sequential-width little-o established
above. No rate uniform in the endpoint width or in N is claimed.
L406 is downstream context only: it cannot supply the missing
full-response tail passage. Clipping, regulator choice, total L367
margin/remainder, actual common-zero upper counts and global mixed
positivity remain unresolved. There is no RH candidate.

### Separate critical audit — step 115

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-14-fixed-head-cubic-leading-coefficient-audit.md`.
This independent proof audit reuses the already audited L407 (4), (8),
(9) and L391 ordinary-jet/polygamma bounds. It validates (1)--(2) for
each fixed positive integer N, with the qualifications stated above.
No new cubic-moment theorem or expanded unequal-shift polar factor is
imported. The following are the load-bearing checks.

**Combined poles and all residue classes.** Differentiating the exact
progression series gives Z_a^(p) with leading coefficient
(-1)^p p!/u. Its remainder is analytic; multiplying the three factors
therefore leaves all other pole orders at most d+2. Summation over
c=1,...,u gives u if u divides ab and zero otherwise, because (v,u)=1.
For each a there are gcd(a,u) admissible b, including zero and nonunit
classes. Thus the highest coefficient is exactly (4), rather than an
assumed sum of separated coalescing residues. The factor (d+2)! in
m_p comes from the residue expansion of exp((s-1)log X). Repeated
derivative orders introduce no extra permutation factor.

**Growth, contours and absolute sharp endpoints.** The continuation
integral has bounded fractional part and absolute integral at most
C_u/sigma on the enlarged strip just specified; multiplying by s
gives O_u(1+|Im s|). All first/second derivative disks remain there,
so the finite triple product has cubic polynomial growth. The compact
smooth Mellin transform decays faster than any fixed power. This
justifies absolute inversion, vanishing horizontals (X fixed first),
the O(X^(1/2)) new vertical integral, and the sole crossed pole.
Each lower Laurent coefficient or transform derivative loses at least
one logarithmic power in (6).

For fixed epsilon, the unsigned u=v=1, p=(0,0,0) formula bounds the
entire boundary mass by C epsilon X(log X)^2+o_epsilon(X(log X)^2).
Multiplication by (log(2X))^d bounds every signed coefficient and
every modulus-one phase. The majorant includes both integer endpoints.
The smooth-main-term discrepancy has the same C epsilon leading
bound, with C independent of epsilon. Taking X to infinity before
epsilon to zero proves (8); neither a signed sandwich nor uniform
shrinking-width control is needed.

**Branches and every analytic weight.** On tau=t-11i/20 the gamma
arguments are z_+=21/40+it/2 and z_-=-1/40-it/2. For large t they
both lie in |arg z|<=3pi/4. Their principal arguments sum near zero,
so Log z_++Log z_-=2Log tau-2log 2+O(H^(-2)), with no branch
multiple. The negative real part of z_- does not violate this sector
hypothesis. The separately bounded polygamma derivative, rather than
a differentiated O term, gives Omega'=O(H^(-1)). Every exact weight
has m=d+b+2k; k=0 yields a_nu ell^(-d) with error O(ell^(-d-1)),
and every k>=1 term is smaller. This applies also to the two zero
leading coefficients. Absolute coefficient mass on the interval is
O_(r,nu)(H ell^(d+2)), so (10) costs O_(r,nu)(H ell).

**Complete signed normalization.** Substitution into both summands of
P1 gives J_plus=-X-2Y-Z and J_minus=-Z, and exactly the eight terms
in (11). The reproduction command was rerun: all seven tests pass.
The full /P1, /polar_terms, /factorization_residual, /tests and
/residue_count_checks were inspected, not previews. The eight polar
moments and signed contributions agree with the written factorial
formula and sum to 17/20160; the factorization residual is empty.
These exact checks verify finite algebra only. The argument above,
not the forty finite modulus checks, proves A_u for every u.

L407's prefactor 2pi r^(-1/2) and X=rH/(2pi) give H sqrt(r).
All leading weights and residues are real, so the final real projection
preserves them. Multiplication by (mnk)^(-5/2) gives exactly
(mn)^(-2)k^(-3). Every zero-carrier resonance remains O_(r,nu)(H),
and the inherited connector/source error is O_N(H^(71/120)). The
remaining sharp and weight errors are respectively o_N(H ell^2) and
O_N(H ell). Thus all errors meet the required o_N(H ell^2) threshold.
There are finitely many twists before H grows; no N-uniform rate or
full-response limit was inferred. In particular beta_1 equals
17/(1290240 pi^3)>0. This audit establishes a local specialization of
the cited tools, not progress beyond the literature or a solution of RH.

## Mathlib

Full matching coverage of this weighted fixed-rational-twist ordinary-jet
asymptotic is not checked. The needed standard analytic inputs are
precisely cited above; the remaining finite residue algebra, specialization
and endpoint estimates are proved here. Unknown Mathlib coverage is not
evidence of absence. The Python certificate is exact finite arithmetic,
not a Mathlib formalization or a verifier of the analytic proof.
