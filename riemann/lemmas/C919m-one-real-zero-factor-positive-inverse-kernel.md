# Corollary 919m: a positive inverse kernel after one real-zero factor

## Hypotheses

Use the actual entire function Xi of L018 and the theta kernel K of
L019, in L058's normalization

    Xi(z) = integral_0^infinity K(u) cos(zu) du.

Fix an arbitrary real x with 14<x<29/2 and Xi(x)=0. No assertion that
x is the first zero, simple, or the only zero in this interval is made.
Evenness gives Xi(-x)=0 with the same multiplicity. All other zeros
are unrestricted.

Existence of at least one such x follows from the accepted C919f at
lambda=0 and continuity in L058. That existence input retains C919f's
correct CPython integer/Fraction arithmetic and libmpdec directed basic
operations, representable-neighbor and correctly rounded HALF_EVEN exp
contracts (recorded runtime CPython3.15.2/libmpdec4.0.1, precision80).
Those contracts have not been independently recertified here. The
analytic assertion below for a given actual x does not use numerical
approximation, an identification of x, or a simplicity hypothesis.

Import the classical theta shape theorem and the ordinary decreasing-
amplitude sine-transform theorem as cited precisely in the proof.

## Conclusion

For u>=0 set

    G_x(u) = x integral_u^infinity K(t) sin(x(t-u)) dt.            (1)

Its even extension to the real line is smooth and strictly positive
at every real u, including u=0. For every nonnegative integer m,p
and every B>=0,

    integral_0^infinity (1+u)^p exp(Bu) |G_x^(m)(u)| du < infinity,
    exp(Bu) G_x^(m)(u) -> 0 as u -> infinity.                   (2)

It is the unique decaying twice continuously differentiable solution
on the positive half-line of

    G_x'' + x^2 G_x = x^2 K.                                  (3)

It satisfies G_x'(0)=0 and has the exact entire cosine transform

    Q_x(z) := integral_0^infinity G_x(u) cos(zu) du
            = Xi(z)/(1-z^2/x^2),                              (4)

where both apparent poles are removable. Their values are

    Q_x(x) = Q_x(-x) = -x Xi'(x)/2.                            (5)

Thus one factor is removed at each of +/-x, including when the zero
has multiplicity greater than one. On the real frequency axis Q_x is
integrable and the inverse formula is, for every real u,

    G_x(u) = (2/pi) integral_0^infinity Q_x(y) cos(yu) dy.       (6)

This is a source-covered REPRODUCTION specialization, not a claim of
new general mathematics or a complete RH argument. In particular,
strict decrease of G_x, repeated-removal closure and the all-degree
mixed-positivity bridge are not conclusions. The separate conceptual
audit2229 below accepts this specialization with the stated qualifications.

## Proof

### Imported tools and normalization

G. Csordas, *Fourier transforms of positive definite kernels and the
Riemann xi-function*, arXiv:1309.0055v2 (21 February 2014), equation
(4.2) and Theorem4.1, printed p10, gives the classical kernel

    Phi(t) = sum_{n>=1} (2*pi^2*n^4*exp(9t)
                         - 3*pi*n^2*exp(5t))
                        * exp(-pi*n^2*exp(4t)).

The theorem supplies positivity, evenness, analyticity in a strip
about the real axis, decay of every derivative stronger than every
fixed exponential at positive infinity, and strict decrease for t>0.
Parts(i)-(iv) are attributed there to Polya and part(v) to Wintner,
with Spira also cited. The exact complete restatement was inspected
in source reviews2225/2226; the original Wintner and Spira proofs
remain unread. The input is that named classical theorem, not an
independent recertification of those proofs.

Direct source: https://arxiv.org/pdf/1309.0055v2 .
Original monotonicity reference: A. Wintner, *A Note on the Riemann
xi-Function*, J. London Math. Soc.10 (1935),82-83,
https://doi.org/10.1112/jlms/s1-10.1.82 .

Termwise substitution in the displayed definition and L019 gives
K(u)=4 Phi(u/2). Consequently K is even and smooth, positive, strictly
decreasing on [0,infinity), and for every m>=0 and B>0 there is a
finite D_m(B) with

    |K^(m)(u)| <= D_m(B) exp(-Bu), u>=0.                       (7)

Continuity on compact intervals and the cited derivative decay justify
the global constants in (7). Strict decrease includes the endpoint
zero: K'<0 on (0,infinity) implies K(b)<K(a) whenever 0<=a<b.
This imports theta monotonicity; it does not reprove it.

The sine-transform input is the bounded, continuous, integrable case
of the decreasing-amplitude result in E.O. Tuck, *On positivity of
Fourier transforms*, Bull. Austral. Math. Soc.74 (2006),133-138,
pp133-134, equations(1)-(4) and the half-period comparison proof:
if f is positive, strictly decreasing and integrable on [0,infinity),
then integral_0^infinity f(v) sin(av)dv>0 for every a>0. The same
half-period proof is completely readable in Csordas, Remark3.11,
printed p9. These are pointwise sine-transform results; the unrelated
positive-definiteness assertions in that paper are not imported.

Tuck's direct publisher PDF:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/D232B9DEB4819E4D2FF17E8162B8B066/S0004972700047511a.pdf/on_positivity_of_fourier_transforms.pdf .

Variation of parameters and homogeneous ambiguity are the standard
identities DLMF1.13(iii), (1.13.8)-(1.13.10),
https://dlmf.nist.gov/1.13.iii . Their analytic-coefficient/forcing
hypotheses hold for the constant-coefficient equation(3) and the
analytic K. The boundary selection and all endpoint checks below
are the necessary specialization, not consequences assumed from
the general ODE formula.

For Fourier differentiation/inversion use T. Tao, *245C, Notes2:
The Fourier transform*, 6 April 2009, Section3, Exercise30 with its
absolute-continuity and L1 derivative hypotheses, Remark31, and
inversion formula(11) and its proof:
https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/ .
We verify those hypotheses and the cosine/angular-frequency constants
below. No reproof of any of these general tools is needed.

### Decaying solution and complete tails

K is integrable, so (1) converges absolutely. To differentiate it on
any compact u interval, use the Leibniz rule for the lower endpoint
and dominate each derivative of its trigonometric factor by a fixed
power of x times K(t). This is an integrable majorant independent of
u on that interval. The endpoint sine is zero. Therefore

    G_x'(u) = -x^2 integral_u^infinity K(t)cos(x(t-u))dt,
    G_x''(u) = x^2 K(u) - x^2 G_x(u).                         (8)

These derivatives are continuous up to zero. The smoothness of K and
the second equation bootstrap G_x to C^infinity on [0,infinity), with

    G_x^(m+2) = x^2 (K^(m) - G_x^(m)), m>=0.                 (9)

For B>0 let M_B=integral_0^infinity exp(Bt)K(t)dt. It is finite by
(7) at rate B+1. The complete tail, without any finite truncation,
satisfies

    T(u):=integral_u^infinity K(t)dt <= M_B exp(-Bu),
    |G_x(u)| <= x T(u),   |G_x'(u)| <= x^2 T(u).              (10)

For fixed B set C_0(B)=x M_B, C_1(B)=x^2 M_B and recursively
C_{m+2}(B)=x^2(D_m(B)+C_m(B)). Equations(7),(9),(10) give
|G_x^(m)(u)|<=C_m(B)exp(-Bu) for every m. In particular, applying
this at rate B+1 gives the full weighted-integral bound

    integral_0^infinity (1+u)^p exp(Bu)|G_x^(m)(u)|du
      <= C_m(B+1) sum_{j=0}^p binom(p,j) j! < infinity.      (11)

The same stronger rate makes every endpoint limit in (2) zero.
Thus the signed integrals have complete absolute tails, and their
derivatives, polynomial weights and all fixed complex frequencies
are controlled. Constants may depend on x,m,p,B; no uniformity in an
unbounded zero index or in the number of removals is asserted.

Any two decaying C^2 solutions of (3) differ, by the homogeneous ODE
identity, by A cos(xu)+B sin(xu). Taking respectively u=2*pi*n/x
and u=(pi/2+2*pi*n)/x as n tends to infinity forces A=B=0.
This removes all homogeneous ambiguity within the asserted decaying
class; no real-pole distributional inverse is used.

### Origin compatibility and the even extension

The first equation of (8), the actual-root hypothesis and L058 give

    G_x'(0) = -x^2 integral_0^infinity K(t)cos(xt)dt
            = -x^2 Xi(x) = 0.                               (12)

This is the required origin condition obtained from the root, rather
than an extra boundary premise. All odd derivatives of the even
smooth K vanish at zero. Starting with (12), formula(9) with odd m
shows inductively that every odd derivative of G_x at zero vanishes.
Consequently G_x(|u|) has matching one-sided derivatives of all orders
at zero and is C^infinity on the real line. It solves (3) there with
the even K. In particular its second derivative has no singular mass
at the origin. The half-line weighted bounds also hold on the whole
line with exp(B|u|).

### Strict positivity

In (1) put t=u+v. For each fixed u>=0 the amplitude f_u(v)=K(u+v)
is bounded, continuous, strictly positive, strictly decreasing and
integrable on [0,infinity). These are exactly the hypotheses of the
imported sine-transform result. Since x>0,

    G_x(u)=x integral_0^infinity f_u(v)sin(xv)dv>0.            (13)

The application includes u=0, and evenness gives positivity for u<0.
There is no unsigned replacement of the oscillatory integral and no
assumption about the sign or monotonicity of G_x' in this argument.
The root hypothesis is used for origin compatibility, not for the
sine theorem. Strict positivity is pointwise; no positive uniform
lower bound over the half-line is claimed, since G_x tends to zero.

### Exact transform, complex extension and removable poles

For |z|<=R, each z derivative of G_x(u)cos(zu) is bounded by
u^n exp(Ru)|G_x(u)|, which is integrable by (11). Truncated integrals
are entire and converge locally uniformly. The usual dominated
differentiation/Weierstrass theorem therefore makes Q_x entire and
gives all its z derivatives by differentiating the integrand. The
same bounds apply to G_x' and G_x'', so both integrations by parts
below are legitimate for complex z. Explicitly,

    integral_0^infinity G_x''(u)cos(zu)du
      = [G_x'(u)cos(zu)]_0^infinity
        + z integral_0^infinity G_x'(u)sin(zu)du
      = -G_x'(0) + z[G_x(u)sin(zu)]_0^infinity
        - z^2 Q_x(z)
      = -z^2 Q_x(z).                                        (14)

The first bracket at infinity and the second bracket at infinity
vanish by (2) with B>|Im z|. The first bracket at zero is (12),
and the second is zero because sin(0)=0. Combining (3),(14) and the
actual transform in L058 yields

    (x^2-z^2)Q_x(z)=x^2 Xi(z), z in C.                       (15)

This proves (4) away from +/-x and proves that the entire integral
is its extension across both points. Alternatively, L018's entire
even Xi and Xi(x)=0 show directly that the denominator's two simple
zeros cancel. Expanding at x gives (5); expanding at -x and using
Xi'(-x)=-Xi'(x) gives the same value. If the order at x is m>=1,
division reduces it to m-1; the same holds at -x. For m>1 both
values in (5) are zero. No simplicity assumption or branch choice
was hidden in the cancellation.

For completeness the actual inverse formula has no normalization
or integrability gap. On real y, |Q_x(y)|<=||G_x||_{L1(0,infinity)};
by (14), for y!=0,

    |Q_x(y)| <= ||G_x''||_{L1(0,infinity)}/y^2.               (16)

Thus Q_x is in L1(R). The even full-line function f(u)=G_x(|u|)
is continuous and in L1 with its first two derivatives; its smoothness
ensures the local absolute-continuity conditions. In Tao's convention
its Fourier transform is hat f(eta)=2 Q_x(2*pi*eta), which is also
integrable by (16). Fourier inversion at every continuity point,
followed by y=2*pi*eta and evenness, gives exactly (6).
It also gives uniqueness of this continuous L1 inverse kernel.

### Scope and known traps

The preceding calculations discharge the origin, infinity, transform
and pole conditions of the single approved test. They supply an actual
positive residual kernel, not just a formal ODE solution or numerical
positivity evidence. L024's paired product is compatible with this
interpretation but is not needed as a mathematical input here: entire
division and the explicit transform identity already suffice.

The proof does not show that the residual is decreasing, that another
removal preserves positivity, or that any of L030-L032/C032a's
algebraic mixed signs follow. It supplies no all-degree assertion and
does not eliminate any possible nonreal zeros. The old nonreal-
deflation normalization stop and the mixed-determinant adjacent-lobe
failure concern different unpaid conditions; neither is contradicted
or silently imported. The original positive theta kernel already
demonstrates why kernel positivity alone cannot close this notebook's
RH gap. No finite-zero census, product-sign assumption or RH-equivalent
positivity was used. QED.

### Separate conceptual audit, 21 November 2026 (step2229)

This audit uses the prior SPECIALIZE assessment2227 and its separate
approval2228. It is REPRODUCTION: first critical acceptance of this
source-covered local assembly, not a new general theorem. The complete
proof above and the actual uses of L018, L019, L058 and accepted C919f
were checked. The source record2225/2226 is reused; there is no claim
of new external inspection or recertification of Wintner/Spira or the
arithmetic backend. No numerical positivity surrogate is used.

**Source hypotheses and scaling.** Substitution into the displayed
Phi series gives coefficients 8*pi^2 and -12*pi and exponents 9u/2,
5u/2 and 2u, exactly L019. Thus K^(m)(u)=4*2^(-m)Phi^(m)(u/2).
The named theta theorem supplies every derivative's decay, not merely
the first two derivatives proved in L019. Its smooth even extension
also supplies every odd origin derivative. Choosing a stronger source
decay rate and bounding the remaining compact interval gives each
D_m(B). For any 0<=a<b, integrating K'<0 on (a,b) proves strict
decrease, including a=0. Hence for every fixed u>=0 the translated
amplitude in (13) is continuous, bounded, integrable, positive and
strictly decreasing. Tuck's strict sine theorem applies at x>0, also
when u=0. No convexity of K, positivity of a cosine transform, or
monotonicity of the residual is supplied by that theorem or assumed.

**Differentiation, every tail and uniqueness.** In the first derivative
the endpoint term vanishes; differentiating the cosine integral gives
G_x''=x^2 K-x^3 integral_u^infinity K(t)sin(x(t-u))dt, which is (8).
Local domination by K and its fixed multiples legitimizes these two
steps. Smoothness and recurrence (9) then give all higher derivatives;
an unjustified infinite sequence of integral differentiations is not
needed. Positivity of K makes (10) an absolute tail bound. The recursion
for C_m(B) has both parity base cases and covers every m. At rate B+1,
integration of (1+u)^p exp(-u) gives exactly the finite factorial sum
in (11), while the endpoint bound is C_m(B+1)exp(-u). This covers
B=0, every finite p,m, and every compact complex-frequency set. All
tails extend to infinity. Homogeneous solutions at real x>0 are the
two trigonometric modes; the two sequences stated in the proof kill
their coefficients using only decay of the solution itself. No decay
of its derivative is silently added to the uniqueness hypothesis.

**The origin and transform.** Equation (12) uses L058 at lambda=0
and the actual zero, with no approximation. Induction in (9) for
m=1,3,5,... kills all subsequent odd derivatives at zero. The matching
one-sided derivatives therefore give a smooth even extension, with
no jump in the first derivative and hence no origin delta term in
the second derivative. For each fixed complex z, the rate
B>|Im z| controls both infinity endpoint expressions in the two
integrations by parts. The remaining origin term is -G_x'(0)=0;
the sine endpoint is zero. The surviving term is -z^2 Q_x, so (15)
has the asserted sign and numerator x^2 Xi. The locally uniform
weighted bounds also prove entire dependence, independently of pole
cancellation. No contour passage, conditionally convergent integral,
product expansion or positivity of a mixed form is involved.

**Both poles, multiplicity and inverse constants.** The denominator's
derivatives at x and -x are -2/x and 2/x respectively. Therefore the
two extension values are -x Xi'(x)/2 and x Xi'(-x)/2, equal by oddness
of Xi'. Each denominator zero has order one: any multiplicity m>=1
in Xi is reduced exactly to m-1. In particular m>1 gives extension
value zero, not a residual pole. For real y, the L1 bounds on G_x
and G_x'' give (16); combining the bounded estimate on |y|<=1 with
the y^(-2) estimate outside proves Q_x is in L1(R). The smooth even
extension f and its derivatives meet the absolute-continuity and L1
hypotheses of the imported Fourier tools. In Tao's convention,

    hat f(eta)=2 Q_x(2*pi*eta),
    f(u)=(1/pi) integral_R Q_x(y)exp(i*y*u)dy
        =(2/pi) integral_0^infinity Q_x(y)cos(y*u)dy.

Absolute convergence permits the variable change and symmetry, and
continuity makes inversion valid at every u, including zero. This
also proves uniqueness in the continuous L1 inverse class claimed.

**Acceptance and limits.** Every conclusion (1)-(6) follows under the
stated hypotheses. No mathematical repair or new input was required.
For a given actual root the analytic proof is independent of its
numerical location inside the bracket; C919f is used only to guarantee
existence of at least one such root and retains its backend contracts.
No first-zero assertion, simplicity, census or uniformity in repeated
removals was used. The direct mathematical inputs remain L018, L019,
L058 and C919f; L024 remains context only. Residual strict decrease,
iteration, and the actual-Xi all-degree mixed-positivity bridge are
unproved. This accepts a qualified partial input, not an RH candidate.

## Mathlib

Coverage of this full quotient-kernel statement is not checked; no
matching theorem or absence claim is asserted. The classical sources
above are the mathematical inputs. Standard ODE, dominated-integral
and Fourier support in Mathlib, if any, is not by itself a full match,
and no particular Mathlib declaration has been verified this turn.
Reference documentation: https://leanprover-community.github.io/mathlib4_docs/ .
