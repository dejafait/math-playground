# Lemma 930: coupled pole integral, regular residual, and parameter-norm floor

## Hypotheses

Use L928's fixed nonnegative w in C_c^infinity((0,1)), integral w=1,
L=log T, N=floor(T^(1/5)), T<=X<=2T, and exact real Hardy phase.
Write <f> for T^(-1) integral w_XT(t)f(t)dt. This is a probability
average supported in [T,3T]. All assertions are eventually uniform in
X and in arbitrary moving complex coefficient pairs c_-,c_+.
Put ell_t=log(t/(2*pi)) and retain exactly

    epsilon_t=theta(t+1/L)-theta(t-1/L)-ell_t/L.

L928 gives epsilon_t=O(1/(T L)), its exact main form, and the charged
moment error. Use only L737's finite divisor identities and norm bound,
which apply to every finite N, rather than its shorter-length analytic
projection theorem. The needed source tools have prior coverage in
drafts/literature/2026-11-09-joint-pole-integral-residual-test-12.md,
with the primary reads recorded in the associated step12 comparison:

* Carl de Boor, *Divided Differences*, Surveys in Approximation Theory
  1 (2005), 46–69, [arXiv:math/0502036v1, Section 9, pp. 63–64,
  the two-node derivative integral immediately before (52)](https://arxiv.org/pdf/math/0502036v1).
  For a scalar function holomorphic near the segment from x to y,
  its first divided difference is integral_0^1 f'((1-s)x+s*y)ds.
  Apply this named identity entrywise to the finite entire family below;
  no general calculus reproof or positivity inference is needed.
* Mika Mattila, *On the eigenvalues of combined meet and join matrices*,
  Linear Algebra Appl. 466 (2015), 1–20,
  [arXiv:1403.5907v2, Section 2, Proposition 2.5, p. 6](https://arxiv.org/pdf/1403.5907v2).
  The complex incidence factorization applies to the divisor lattice,
  the factor-closed prefix [1,N], and f(d)=d^(1+z). It uses transpose,
  not adjoint, and does not assert positivity for complex z.
* Rajendra Bhatia, *Positive Definite Matrices* (2007),
  [Propositions 1.3.1–1.3.2 and Theorem 1.3.3, pp. 13–14](https://assets.press.princeton.edu/chapters/s8445.pdf).
  Only the nonsingular finite block criterion, using both positive
  diagonal metrics and their inverse square roots, is used.
* [NIST DLMF 25.2(i), 25.2.4](https://dlmf.nist.gov/25.2#E4):
  zeta has its residue-one simple pole at 1 and its Laurent regular
  part there. Set g(z)=zeta(1+z)-1/z, with g(0)=gamma, and
  C_g=max_(|z|<=1/2)|g(z)|<infinity. The removable value is included.

All positive-base powers use real logarithms. Matrix norms are Euclidean
operator norms; * denotes adjoint and superscript T denotes transpose.
Positive square roots are used for the energy matrices. No RH, sign
assumption, zero-free region, or limit of a shifted-moment remainder
through a zero-sum shift is used. L929 provides notation and a contrasting
stopped estimate; its unaudited claims are not assumed. The required
coordinates are verified below directly from L737 and L928.

## Conclusion

There is an exact entire-family first-divided-difference representation
for the nominated combined pole part, with both endpoints, the complete
energy metrics, the original time weight, and the Hardy phase retained.
The regular-zeta residual is uniformly small in those full metrics:

    sin(1)-C/L <= ||B_pole|| <= 15 exp(2)+C/L,
    0 <= ||R_reg|| <= C_reg/L.                              (1)

Finite bounds with specified quantities, rather than just the asymptotic
constants in (1), are given in (12)–(13). In particular, entrywise small
regular zeta coefficients have been promoted to a uniform operator bound
at the growing length N; this is not assumed from their scalar size.

However, the selected estimate that integrates the pointwise operator
norms of the combined derivative has certificate J satisfying

    ||B_pole|| <= J,
    J >= <ell_t>/sqrt(a_- a_+)=1+O(1/L).                    (2)

Thus even exact pointwise norms in this estimate, with any nonnegative
upper charge for R_reg added, cannot certify <=1-eta for fixed eta>0.
The loss occurs at taking norms under the interpolation integral, after
the pole endpoints have already been combined. It is distinct from
L929's separate-modulus pole-summand majorant.

This stops only that parameter-norm estimate. The true norm sum
||B_pole||+||R_reg||, a sufficient weaker margin, L928(11), joint
projection, signed transfer and actual-Xi mixed positivity remain open.
The positive lower endpoint in (1) is one test direction, not the norm.
The upper endpoint exceeds one and proves no contraction. This is an
informative local negative test using imported tools, not a new moment
theorem or an RH candidate. The checked sources did not supply this
exact diagnostic; no certified originality is claimed. Written
9 November 2026, step13; the separate step15 conceptual audit below
validates these scoped conclusions without correction.

## Proof

### 1. Exact coordinates and the entire endpoint family

Let phi be Euler's totient and use L737's real matrices and scalar
function

    G_(d,n)=1_(d|n) sqrt(phi(d)/n),
    K_(d,n)=1_(d|n,n>d) Lambda(n/d) sqrt(phi(d)/phi(n)),
    kappa(d)=sum_(p|d) log p/(p-1).

G is upper triangular with nonzero diagonal. Set r=log N,
D=diag(log d), and A=G diag(log n)G^(-1). L737's finite identity
for C_d gives

    A=D+K,  ||K||<=2r,  0<=kappa(d)<=log d<=r.             (3)

Indeed the coefficient logarithm is log n=log d+log(n/d), and the
second summand is exactly L737's C_d operator. The last scalar bound
uses 1/(p-1)<=1 and product_(p|d)p<=d. These applications hold at
the present N, independently of L737's shorter analytic cutoff.

Put D_s=diag(n^(i*s/L)), y_s=G D_s c_s, and define

    a_s=<log((t+s/L)/(2*pi))+2*gamma>,
    H_s=a_s I+2 diag(kappa)-K-K^T,
    lambda_s=a_s-4r,  d_H=sqrt(lambda_- lambda_+).           (4)

L737's exact finite form makes the two diagonal main energies in
L928 equal to T y_s^* H_s y_s. Since H_s>=lambda_s I,
a_s=L+O(1), and r<=L/5, both lambda_s are positive eventually,
uniformly in X. In fact lambda_s=L/5+O(1). The full H_s, including
their logarithmic cross terms, are retained in every normalization.
Also e_1^*H_s e_1=a_s; e_1 need not be an eigenvector.

For any complex z,v set

    j(z,d)=J_(1+z)(d)/phi(d),
    J_(1+z)(d)=sum_(b|d) mu(b)(d/b)^(1+z),
    Q(z)=diag(j(z,d)),
    M(v)=G diag(n^(-v))G^(-1)=exp(-v A),
    h=2i/L,
    F_t(z)=exp(z ell_t/2) M(z/2+i/L)^T Q(z) M(z/2+i/L).
                                                               (5)

For each fixed T,t,N this is an entire matrix function: all scalar
constituents are finite sums or exponentials. It is holomorphic on a
neighborhood of the whole segment [-h,h], including its midpoint.
The incidence theorem with f(d)=d^(1+z) gives exactly

    (G^T Q(z) G)_(m,n)=gcd(m,n)^(1+z)/sqrt(m*n).

Consequently, for the already fixed y_- and y_+,

    y_-^* F_t(z) y_+
      =sum_(m,n) c_(+,m) conjugate(c_(-,n)) q_mn
                   exp(z H_t(m,n)/2),                     (6)

where q_mn and H_t(m,n) are exactly L928(1). To check the rotations,
each side supplies n^(i/L) or m^(i/L) from D_-^* and D_+;
these cancel the factor (m*n)^(-i/L) in (5). The remaining factors
are exp(z ell_t/2), gcd(m,n)^z and (m*n)^(-z/2), as in (6).
No nonunitary coordinate transformation has been treated as unitary.

In particular, with

    W_+=M(h)^T Q(h) M(h),  W_-=Q(-h),
    I_±=<exp(i epsilon_t) exp(±i ell_t/L)>,
    V=zeta(1+h) I_+ W_+ + zeta(1-h) I_- W_-,
    B=H_-^(-1/2) V H_+^(-1/2),                            (7)

the endpoints are F_t(h)=exp(i ell_t/L)W_+ and
F_t(-h)=exp(-i ell_t/L)W_-. They agree with L929(6),(8), now checked
against L928 independently. The transpose in W_+ is essential: (6)
is a bilinear spatial factorization before the fixed conjugation of
the minus coefficients, not a positive Hermitian Gram factorization.
The cross main form is exactly T y_-^* V y_+. Since the two changes
of coefficients are invertible and H_s are positive definite, the
supremum relative to the two full energies is ||B||, as in the cited
nonsingular block criterion.

Replace only the two scalar zeta poles by 1/h and -1/h, respectively.
Then the nominated matrices are exactly

    V_pole=<exp(i epsilon_t) [F_t(h)-F_t(-h)]/h>,
    B_pole=H_-^(-1/2) V_pole H_+^(-1/2),
    R_reg=H_-^(-1/2)
       [g(h) I_+ W_+ + g(-h) I_- W_-] H_+^(-1/2),
    B=B_pole+R_reg.                                        (8)

The entire-family first-difference identity from de Boor gives

    [F_t(h)-F_t(-h)]/h=integral_(-1)^1 F_t'(s h) ds.        (9)

The denominator in the standard divided difference is 2h: changing
from [0,1] to [-1,1] gives precisely (9), with no extra factor two.
The exact weight and exp(i epsilon_t) multiply this identity before
time integration. Only finite matrices and compact t,s integrals
occur, so differentiation and these integrations commute entrywise.
No integration by parts or omitted boundary term is involved.

### 2. Uniform finite bounds and the full regular residual

The following estimates are supplied for this growing finite family,
because scalar pole removal alone would not control its metric norm.
For real u, f(u)=M(iu)b satisfies f'=-i(D+K)f. The real diagonal D
contributes zero to d||f||^2/du, while the other contribution has
absolute value <=2||K|| ||f||^2. Multiplication by exp(-2||K||u)
for u>=0, and the same argument with u replaced by -u, therefore give

    ||M(iu)||<=exp(2r|u|).                                 (10)

This elementary differential estimate is applied to the specific finite
matrix (3); it does not assert that M is unitary. There is no dimension
factor or condition number of G in (10).

For imaginary z=iu, the finite Euler product gives

    j(iu,d)=d^(iu) product_(p|d)
                      (1-p^(-1)exp(-iu log p))/(1-p^(-1)).

Each factor has modulus <=exp(|u|log p/(p-1)), by
|1-exp(-iv)|<=|v|. Thus ||Q(iu)||<=exp(r|u|). The factors never
vanish on this line. Their logarithmic derivative is

    j'(iu,d)/j(iu,d)=log d+sum_(p|d) log p/(p^(1+iu)-1),

so ||Q'(iu)||<=2r exp(r|u|), since |p^(1+iu)-1|>=p-1.
For d=1 the derivative is zero and the same bounds hold.

On z=s h, -1<=s<=1, put v=z/2+i/L=i(s+1)/L. Direct
differentiation of (5), using M'(v)=-A M(v), gives

    F_t'(z)=exp(z ell_t/2) M(v)^T
      [(ell_t/2)Q(z)+Q'(z)-(A^T Q(z)+Q(z)A)/2] M(v).
                                                               (11)

The scalar exponential has modulus one. Also ||A||<=3r from (3),
|Im z|<=2/L, |Im v|<=2/L, and transpose preserves the Euclidean
operator norm. Equations (10)–(11) imply

    ||F_t'(s h)|| <= (ell_t/2+5r) exp(10r/L),
    ||W_+||<=exp(10r/L),  ||W_-||<=exp(2r/L).

Here ell_t>0 eventually on the support. Both inverse square roots
in (8) have product of norms <=1/d_H. Since |I_±|<=1 exactly,
and |g(±h)|<=C_g for L>=4, (8) yields the full metric bound

    ||R_reg|| <= C_g [exp(10r/L)+exp(2r/L)]/d_H.             (12)

The complete time weight and Hardy phase enter I_±; bounding their
modulus by one is justified by the probability average and the reality
of epsilon_t. No entrywise-to-operator estimate is being inferred.
As d_H=L/5+O(1) and r<=L/5, (12) is at most
5 C_g [exp(2)+exp(2/5)]/L+O(L^(-2)). This proves the residual
bound in (1) with a uniform constant C_reg.

Applying the triangle inequality to (9) gives the explicit certificate

    J=< integral_(-1)^1
          ||H_-^(-1/2) F_t'(s h) H_+^(-1/2)|| ds >,
    ||B_pole||<=J<= [<ell_t>+10r] exp(10r/L)/d_H
                         <=15 exp(2)+O(1/L).               (13)

The exact phase in (8) is still present in the operator identity;
its modulus is one in this estimate. The constant in (13) is deliberately
not called a contraction. Even replacing this crude upper bound by
the exact integrand norms cannot give the fixed gap, as follows.

### 3. The floor at the parameter-norm step

Set u_s=H_s^(1/2)e_1/sqrt(a_s), for s=-1,+1. These are unit
vectors by (4). Because G e_1=G^(-1)e_1=e_1 and j(z,1)=1,
M(v)e_1=e_1. Therefore the exact entire-family scalar entry is

    e_1^*F_t(z)e_1=exp(z ell_t/2),
    e_1^*F_t'(z)e_1=(ell_t/2)exp(z ell_t/2).

The cancellation of both positive square roots gives, at every point
z=s h of the interpolation segment,

    |u_-^* H_-^(-1/2)F_t'(s h)H_+^(-1/2)u_+|
        =ell_t/(2 sqrt(a_- a_+)).                          (14)

This is a lower bound for the integrand norm in (13), including when
e_1 is not an eigenvector of either full energy matrix. Integrating
over s and taking the time average proves (2).

Explicitly, if b=<ell_t>=L+O(1), then
a_s=b+2*gamma+<log(1+s/(t L))>=b+2*gamma+O(1/(T L)).
Consequently b/sqrt(a_-a_+)=1+O(1/L), uniformly in X. There is
one C such that every certificate obtained by majorizing the pointwise
norms in (13) is >=1-C/L. Adding any nonnegative upper bound on the
residual cannot lower this certificate. For each fixed eta>0 it is
therefore >1-eta at one uniform sufficiently-large-T onset. This
precludes the required fixed-gap conclusion from this specific estimate.

For comparison, taking the s integral before its scalar modulus yields

    u_-^* B_pole u_+
       =<exp(i epsilon_t) L sin(ell_t/L)>/sqrt(a_-a_+)
       =sin(1)+O(1/L).                                     (15)

The second equality uses ell_t/L=1+O(1/L),
epsilon_t=O(1/(T L)), and sqrt(a_-a_+)=L+O(1), uniformly on the
whole support. This proves the lower bound in (1). Equations (14)–(15)
show where a limiting loss of 1-sin(1) occurs on the same direction:
at integrating derivative norms instead of preserving cancellation
between interpolation parameters. Neither (14) nor (15) is an upper
bound for the true operator on all moving coefficient pairs.

### 4. Required threshold and scope of the stop

The achieved residual is O(1/L), whereas L928's charged arithmetic
error relative to its diagonal coefficient scale is O(T^(-9/80)/L).
The residual is therefore controlled but cannot be omitted. The present
pole bound leaves no proven positive margin after either charge.
To use a weaker margin by this split, an upper bound
||B_pole||<=1-delta(T) would still need a proved positive remainder
eta(T)=delta(T)-an_upper_bound_for_||R_reg||; that remainder must
dominate the stated O(T^(-9/80)/L) arithmetic error. No such delta
or eta is obtained here. The floor (2) alone also does not rule out
all sufficient vanishing margins: its O(1/L) term has no decisive sign
or sharp upper-certificate value. No weaker-margin impossibility is
claimed.

The selected parameter-norm estimate is stopped. Reopening it requires
a materially different estimate that retains cancellation across the
interpolation variable, or a new input; more Schur weights or parameter
samples cannot remove (14). This does not prohibit another treatment
of the exact integral (9). L929's termwise-modulus stop, the older joint
coercivity and step226 stops retain their own scopes. The regular
residual bound (12) is validated by the separate audit below. No joint
projection statement is inferred, no source
moment theorem has been strengthened, and no signed realization or
Xi-sign premise has been supplied.

### Separate conceptual audit — 9 November 2026, step15

This audit uses the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-09-pole-integral-residual-audit-13.md`.
It reuses the inspected primary statements cited in the hypotheses,
L737 Sections 2–3 and its step261 audit, and L928(1)–(5),(11) and
its step8 audit. The finite calculations below were checked directly;
no source contraction, numerical evidence, or L929 theorem is assumed.

**Coordinates and both endpoints.** For any coefficient vector c,
put b_n=c_n/sqrt(n). The d-th component of G diag(log n)c is
sqrt(phi(d)) times sum_(d|n)b_n log n. Splitting log n into
log d+log(n/d), L737's finite C_d identity gives (D+K)Gc.
Invertibility of G therefore gives exactly A=D+K, for this finite N.
No shorter analytic length hypothesis is used. L737's full form yields
H_s in (4), with both K and K^T and the positive 2*kappa term.
For complex y, the cross contribution has absolute value at most
2||K|| ||y||^2<=4r||y||^2. Thus H_s>=lambda_s I. Since
r=L/5+O(T^(-1/5)) and a_s=L+O(1), both lambda_s=L/5+O(1),
uniformly in X. This proves a common onset for both positive metrics.

The incidence specialization is valid on the divisor-closed prefix:
sum_(d|gcd(m,n)) J_(1+z)(d)=gcd(m,n)^(1+z), with real logarithms
of the integer bases. If E(v)=diag(n^(-v)), then M(v)G=GE(v)
and G^T M(v)^T=E(v)G^T. The factor contributed on either coefficient
index by D_-^* or D_+ and E(v) is n^(i/L-v)=n^(-z/2).
This checks (6) for every complex z and arbitrary complex vectors,
including the orientation of the minus-vector conjugation. At z=h,
v=h; at z=-h, v=0. These are exactly W_+ and W_- in (7).
The zeta pole at -h is -1/h, so their coupled pole difference has
the sign in (8). The family is entire even though the uncancelled
zeta expression is not holomorphic at zero. The cited first-difference
identity on the segment from -h to h, followed by z=s*h, gives (9)
with denominator h and interval length two. The exact real phase
and probability weight are retained before averaging.

**Uniform bounds, transpose and the residual.** For either sigma=+1
or -1, f(u)=exp(-i*sigma*u*A)b, u>=0, satisfies
|d||f||^2/du|<=2||K|| ||f||^2: the real diagonal D contributes zero.
Integration gives ||M(i*sigma*u)||<=exp(||K||u)<=exp(2r*u).
This verifies (10) for both signs, without a condition number of G.
For imaginary z, every Euler factor has modulus at most
1+|Im z|log p/(p-1), hence the product bound exp(r|Im z|).
Its logarithmic derivative has the plus sign in the displayed formula
above (11), and |p^(1+z)-1|>=p-1. Thus the derivative bound is
2r exp(r|Im z|), also for d=1. There is no zero denominator on
this segment. These estimates use kappa(d)<=log d, not positivity
of a complex Jordan factor.

Since dM(z/2+i/L)/dz=-A M(z/2+i/L)/2, differentiating the two
matrix factors puts A^T on the left of Q and A on its right inside
the bracket in (11). A commutes with M because M=exp(-vA).
Complex transpose has the same Euclidean operator norm as the original
matrix; this assertion does not replace the transpose by the adjoint.
The three bracket bounds add to ell_t/2+2r+3r. The two M factors
contribute exp(8r/L) and Q or its derivative contributes exp(2r/L).
This checks the exponent 10r/L and the factor ell_t/2+5r.
The two endpoints give respectively exp(10r/L) and exp(2r/L).

Both metric square roots are those of the complete H_s; their inverse
norm product is at most 1/d_H. The scalar regular part g is holomorphic
on the closed disk used in the proof, by the cited zeta pole statement,
and |h|<=1/2 for L>=4. Since |I_+|,|I_-|<=1, (12) follows with
one N-independent constant C_g. The asymptotic d_H=L/5+O(1)
makes its upper bound 5*C_g*(exp(2)+exp(2/5))/L+O(L^(-2)),
uniformly in X. In (13), integration over an interval of length two
gives <ell_t>+10r=3L+O(1); division by d_H yields
15 exp(2)+O(1/L). All estimates are operator estimates before testing
vectors, so they cover arbitrary T,X-dependent complex coefficient pairs.
Only finite sums and compact integrals have been differentiated or
interchanged; no limit of a source moment remainder is involved.

**Certificate floor and its precise limitation.** The first columns of
G and G^(-1) are e_1. Hence M(v)e_1=e_1, and the transpose gives
e_1^*M(v)^T=e_1^* because e_1 is real. Also Q(z)e_1=e_1.
This proves the scalar entry and its derivative used in (14).
The real positive quantities a_s equal e_1^*H_s e_1, so the vectors
u_s=H_s^(1/2)e_1/sqrt(a_s) are unit vectors even when e_1 is
not an eigenvector. Multiplication cancels both square roots in the
scalar pairing exactly. Its modulus on the entire segment is therefore
ell_t/(2sqrt(a_-a_+)), with no phase or metric approximation.
The pointwise norm is at least this modulus. Integrating first in s
and then against the probability weight gives (2).

For b=<ell_t>, one has b=L+O(1) and
a_s=b+2*gamma+<log(1+s/(tL))>=b+2*gamma+O(1/(TL)).
These bounds are uniform since T<=t<=3T on the support. They imply
one constant C with J>=1-C/L. For every fixed eta>0 the floor is
strictly greater than 1-eta at a common sufficiently large onset.
Thus any pointwise-norm majorant, even using the exact norms and then
adding a nonnegative residual charge, cannot prove that fixed gap.

Integrating the scalar derivative before taking its modulus instead
gives exactly L*sin(ell_t/L); the phase remains exp(i*epsilon_t).
Since ell_t/L=1+O(1/L), epsilon_t=O(1/(TL)), and
sqrt(a_-a_+)=L+O(1), the normalized scalar entry is
sin(1)+O(1/L). Its modulus gives the lower bound in (1), not an upper
bound for the full operator. The floor in (2) therefore cannot be
transferred to ||B_pole||, or to ||B_pole+R_reg||. It also excludes
no particular sufficient shrinking margin by itself. A margin after
paying the full regular residual must still absorb L928's relative
arithmetic error O(T^(-9/80)/L), as explained in Section 4.

**Audit result.** Equations (1)–(15) and the scoped stop pass without
correction. The retained full-metric O(1/L) residual is now a checked
informal input under the named imports; the audit is REPRODUCTION,
not a discovery beyond those sources. The e_1 certificate floor is
validated only for the specified estimate. The actual joint gap,
joint projection, signed realization/transfer and L030–L032/C032a
remain unresolved. No new direct mathematical input or DAG edge is
introduced. L925 is not used and L929 remains independently unaudited.

## Mathlib

Full matching coverage for this finite coupled family, its metric
residual bound and the parameter-norm obstruction has not been checked
and is unknown. Matrix exponentials, finite divisor convolutions,
positive square roots, first divided differences and norm inequalities
are supporting topics, not a checked matching theorem. The named source
tools above are imports; the step15 audit is an informal mathematical
check, not formal verification. Full matching Mathlib coverage remains
unknown after the audit.
