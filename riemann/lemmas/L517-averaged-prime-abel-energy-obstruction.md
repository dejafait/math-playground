# L517 — Averaged finite-prime Abel test and energy-bound obstruction

## Hypotheses

Use the complete real form b, multiplier m, finite prime cutoff,
translations T_s, dilations U_r, H, P and S_r of L516, with
0<a<A<infinity and zero extension from I_a=(-a,a). Write

    N=floor(exp(2A)), ell_n=log(n),
    w_n=Lambda(n)/sqrt(n), w_1=0, W(j)=sum_(n<=j)w_n.

All prime powers with n<=N are retained, including equality atoms.
The full-Weil identification remains the qualified external input
specified in L516. The logarithmic form domain is its smooth-core
domain, with whole-line reference form

    q_G(f)=(1/(2pi)) integral (1/2)log(1+xi^2)|hat f(xi)|^2 dxi.

For the averaged identity, u is a real normalized eigenvector as in
L516; no sign, simplicity or gap is required. The smooth-test
obstruction instead uses real C_c^infinity(I_a) functions, and requires
a>log(2)/2. These tests are expressly **not eigenvectors**. A positive
Rayleigh quotient b(f,f) is not an eigenvalue equation.

This is the bounded test authorized by the pre-existing EXPLORE gate
`drafts/literature/2026-10-30-weil-averaged-prime-remainder-coverage.md`.
The finite Abel identity is imported, not reproved. Its application
and the packet calculation investigate the proposed signed estimate;
POTENTIALLY_NEW is not a certification of originality. This local
derivation has not received a separate critical audit.

## Conclusion

For 0<epsilon<h<log(A/a), put

    d_n(t;u)=<u,(T_(ell_n exp(-t))+T_(-ell_n exp(-t))
                         -T_ell_n-T_(-ell_n))U_(exp(t))u>/(exp(t)-1),
    F_n(epsilon,h;u)=(1/h) integral_epsilon^h d_n(t;u)dt,
    R_(epsilon,h)(u)=(1/h) integral_epsilon^h S_(exp(t))(u)dt.

The following is an exact proper-integral identity:

    R_(epsilon,h)=W(N)F_N
                    -sum_(n=1)^(N-1)W(n)(F_(n+1)-F_n).       (1)

For N=1 both sides are zero. On the eigenvector, the complete
right side, taken as a whole, has the successive limits

    R_h(u)=lim_(epsilon->0+) R_(epsilon,h)(u),
    lim_(h->0+)R_h(u)=S(u).                                  (2)

No individual improper integral of d_n is asserted. Thus the required
bound on limsup R_h is exactly L516 (6), with its unchanged uniform-K
requirement; (1) does not establish it.

Here is a concrete obstruction to closing (1) by signs or a form-energy
bound valid on smooth tests. For such tests define the smooth limit

    S_sm(f)=-2 sum_(n<=N) w_n ell_n C_f'(ell_n),
    C_f(s)=integral_R f(x)f(x+s)dx.                           (3)

It is also lim_(h->0+)R_h(f), with the same finite expressions.
There are real even normalized smooth tests y_j^+ and y_j^-, supported
strictly inside I_a, and k_j^+,k_j^-->infinity, such that

    S_sm(y_j^+)= k_j^+ (log(2))^2/sqrt(2),
    S_sm(y_j^-)=-k_j^- (log(2))^2/sqrt(2).                    (4)

Only the n=2 atom contributes, including at finite sufficiently small
h. The F_2 limits have opposite signs. If N>=3, the Abel increment
F_3-F_2 has either sign despite W(2)>0; if N=2, the endpoint W(2)F_2
has either sign.

More strongly, for **every** real normalized f_0 in C_c^infinity(I_a),
there are real normalized smooth f_j^+ and f_j^- with

    f_j^+/- -> f_0 in the logarithmic form norm and in L-infinity,
    b(f_j^+/-,f_j^+/-) -> b(f_0,f_0),
    H(f_j^+/-)-P(f_j^+/-)+S_sm(f_j^+/-) -> +/-infinity.        (5)

If 0<b(f_0,f_0)<lambda_0, all sufficiently late tests also have
Rayleigh quotients in (0,lambda_0). Hence no fixed finite K can give

    H(f)-P(f)+S_sm(f)<=K b(f,f)                              (6)

for all normalized smooth tests in that positive-energy band, even
in an arbitrarily small form-norm neighborhood of f_0. This statement
is conditional on the band containing such an f_0. An actual positive
eigenvector with eigenvalue in its interior supplies a smooth seed by
form-core approximation, but does not turn the constructed tests into
eigenvectors.

This refutes a universal sign/energy closure of the averaging-Abel
implementation. It does not refute L516 (6) on the exact eigenbranch,
prove that such a branch exists, or imply anything about off-line zeros.
An eigen-equation-specific signed input could still succeed. No bound
on G f_j in L-infinity, common spectral gap or uniform dilation rate
is claimed or used.

## Proof

### Proper finite Abel summation and the aggregate limit

Translations and dilations are strongly continuous on L2. Since each
is unitary and ||u||_2=1, d_n is continuous for t>0 and

    |d_n(t;u)|<=4/(exp(t)-1).

It is therefore integrable on [epsilon,h]. A finite sum can be
interchanged with this proper integral. Apply Giuseppe Molteni,
[*Analytic Number Theory*, Spring 2026, revision 9.0](https://sites.unimi.it/molteni/didattica/matematica/analytic_number_theory/appunti-AnNTh.pdf),
Section 1.2, printed p.6 (PDF page 12), Proposition 1.3, with the
finite sequences g(n)=w_n and f(n)=F_n(epsilon,h;u). Its partial sums
are exactly W(n), with full right-closed prime-power weights. This
gives (1). No C1 interpolation, prime-density approximation or
half-weight convention is involved.

L516 proves that the entire function S_(exp(t))(u) tends to the
finite S(u) as t decreases to zero. It is continuous for t>0, being
a finite sum of continuous functions. Extend the complete function
at t=0 by S(u). It is bounded on every [0,h], so its proper integrals
have the first limit in (2). For the second,

    |R_h(u)-S(u)|<=sup_(0<=t<=h)|S_(exp(t))(u)-S(u)| ->0.

The value at t=0 in this display means the continuous extension.
This passes to epsilon=0 only after the signed combination in (1)
has been formed. Individual F_n may have no improper limit under
the eigenvector hypotheses. The fixed-u conclusion supplies no
uniform rate as a or u varies.

### Smooth limit, with the dilation term accounted for

For smooth compact f, differentiation of all translations and U_r f
is legitimate in L2 near r=1. The difference of translation operators
in the numerator of d_n is zero at r=1. Therefore its product with
the derivative of U_r f contributes zero. Differentiating just the
two varying translations gives

    lim_(t->0+)d_n(t;f)
      =-ell_n C_f'(ell_n)+ell_n C_f'(-ell_n)
      =-2ell_n C_f'(ell_n),                                  (7)

since the real autocorrelation is even. There are finitely many n,
so individual averaging and summation of these smooth limits are
valid and give (3). This step makes no regularity assertion about
the eigenvectors of L516.

### An exact one-atom packet test

Set ell=log(2) and choose

    0<delta<min(a-ell/2, ell/2, (log(3)-ell)/2).

Let phi be a real even member of C_c^infinity((-delta,delta)) with
integral phi^2=1, and define

    v(x)=phi(x+ell/2)+phi(x-ell/2),
    y_k(x)=v(x)cos(kx), b_*=ell/2+delta<a.

The two packets have disjoint supports. The support of y_k lies in
[-b_*,b_*], with 2b_*<log(3). For every n>=3, C_yk(s) vanishes
on a neighborhood of ell_n. The finite-r assertion also holds:
the scaled pairing can overlap only if ell_n<=b_*(1+r), and the
unscaled pairing only if ell_n<=b_*(1+1/r). Taking r>1 sufficiently
close to one makes both impossible for every n>=3 simultaneously.
If these n exceed N they are simply outside the fixed finite sum;
none of its atoms has been dropped. The n=1 difference is zero.

For k ell=2pi j +/- pi/2, let k=k_j^+/-; take j>=1. Then

    ||y_k||_2^2
      =integral phi(z)^2[cos^2(k(z-ell/2))+cos^2(k(z+ell/2))]dz
      =integral phi(z)^2[1+cos(2kz)cos(kell)]dz=1.             (8)

Only the left packet and its translate to the right packet overlap
in C_yk(ell). Differentiating that overlap gives

    C_yk'(ell)
      =integral phi(z)phi'(z)cos(k(z-ell/2))cos(k(z+ell/2))dz
       -k integral phi(z)^2 cos(k(z-ell/2))sin(k(z+ell/2))dz.

In the first integral, the product of cosines is
[cos(kell)+cos(2kz)]/2. Its constant term integrates to zero;
integration by parts makes the other term
(k/2) integral phi(z)^2 sin(2kz)dz. In the second integral,
cos(alpha)sin(beta)=[sin(alpha+beta)+sin(beta-alpha)]/2.
The sin(2kz) terms cancel exactly, leaving

    C_yk'(ell)=-(k/2)sin(kell).                              (9)

Equations (3), (8) and (9), with w_2=ell/sqrt(2), prove (4).
They also prove the asserted sign failure for the Abel increments.
For example the successive average limits of F_2 equal
ell k sin(kell), while those of every F_n with n>=3 are zero.
The signs persist for sufficiently small averaging windows for
each fixed test; no common window across k is asserted.

### Energy-small perturbations retain the obstruction

Fix f_0 as in (5), choose either packet sequence, and put

    eta_k=k^(-1/4),
    z_k=f_0+eta_k y_k, f_k=z_k/||z_k||_2.

First the packet logarithmic energy is O(log(2+k)). Indeed

    hat y_k(xi)=[hat v(xi-k)+hat v(xi+k)]/2,
    (1/2)log(1+xi^2)<=log(1+|xi|),
    log(1+|eta+/-k|)<=log(1+k)+log(1+|eta|).

The inequality |alpha+beta|^2<=2|alpha|^2+2|beta|^2 and a change
of variables bound q_G(y_k) by a constant times log(2+k) plus
integral log(1+|eta|)|hat v(eta)|^2 deta. This last integral is
finite: repeated integration by parts makes the Fourier transform
of the fixed smooth compact v decay faster than any fixed inverse
power. Consequently

    ||eta_k y_k||_(q_G+L2)^2=O(k^(-1/2)log(2+k))->0.

Also ||eta_k y_k||_infinity<=2||phi||_infinity k^(-1/4)->0.
Since ||f_0||_2=||y_k||_2=1, ||z_k||_2->1; normalizing preserves
both convergences in (5). By L516's realization, b is q_G plus
a bounded L2 bilinear form (the scalar and finite signed-measure
convolution). Thus form-norm convergence implies convergence of
b(f_k,f_k) to b(f_0,f_0), including its sign when the limit is
strictly positive.

Next expand the quadratic expression (3):

    S_sm(z_k)=S_sm(f_0)+eta_k E_k+eta_k^2 S_sm(y_k).           (10)

For each fixed shift, E_k consists of integrals of f_0 times a
translated derivative of y_k, and of y_k times a translated
derivative of f_0. In the former move the derivative onto f_0
by integration by parts. Each resulting integral is an oscillatory
integral of a fixed smooth compact amplitude at frequency k,
possibly multiplied by a phase of modulus one. Repeated integration
by parts shows |E_k|=O_M(k^(-M)) for every integer M>=1. Constants
may depend on f_0, phi, a, A and the fixed finite shift list, which
suffices. No infinite sum of such estimates is taken.

Using (4) in (10) and ||z_k||_2^2->1 gives

    S_sm(f_k)/sqrt(k) -> +/-(log(2))^2/sqrt(2).               (11)

Finally L516 establishes bounded p(xi)=xi m'(xi). Plancherel and
||f_k||_2=1 give |H(f_k)|<=||p||_infinity. For the pole derivative,

    |P(f_k)|<=2a max_(|s|<=2a)|2cosh(s/2)+s sinh(s/2)|,

by ||f_k||_1^2<=2a. These bounds preserve both signs of divergence
in (11), proving (5). They retain the signed pole in the desired
comparison, rather than silently omitting it.

If the seed energy lies in (0,lambda_0), convergence of its energy
puts the tests in the same band eventually. Their positive-diverging
left side in (6) contradicts (6) for every fixed K. If an actual
normalized eigenvector has eigenvalue in this open band, the stated
smooth-core form density and continuity of b give normalized smooth
seeds with energies arbitrarily close to that eigenvalue. This is
only an existence argument for seeds. No small eigen-equation residual
or trace conclusion for the constructed f_k is deduced.

### Decision and limits

The exact finite Abel transform and averaging preserve the signed
quantity. Its coefficients W(n)>=0 do not impose the needed sign
on its increments. The packet test disproves that sign, and (5)
disproves a closure based only on logarithmic form energy and small
positive Rayleigh quotients. Even L-infinity closeness to a seed
does not repair that closure.

All packet tests vanish near the endpoints, so their boundary traces
are zero. L516's flux identity (5) cannot be applied to them because
they do not satisfy the eigen-equation. The divergence here is not
a violation of that identity. No estimate on the exact positive
simple eigenbranch has been disproved; it still needs a genuinely
eigenvector-specific signed cancellation. This bounded attempt parks
the averaging-Abel implementation in the absence of such a new input,
not all Weil-form approaches. The source realization, source collar
and support laws, multiple branches and Xi transfer remain unresolved
at their previously stated levels.

## Mathlib

Full matching coverage of this averaged-prime obstruction has not
been checked. Finite Abel summation is imported from the precise
source above. Other ingredients are finite sums, Plancherel, smooth
integration by parts, and L516's qualified logarithmic-form model
and bounded multiplier p. No Mathlib declaration or Lean proof was
inspected; unknown coverage is not evidence of absence. The generic
packet method is not claimed as novel, and no separate critical
audit of this local result has yet been performed.
