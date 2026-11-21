# Corollary C030m: bounded two-level infinitesimal orbital phase response

## Hypotheses

Let n>=2 be finite, a,r,x>0, and b real. For j=0,...,n let P_j be
an orthogonal projection of rank j on C^n. All unitary integrals use
probability Haar measure on U(n). Define

    D_b=diag(a+i*b,a-i*b,r,...,r),
    Z_(j,b)(x)=integral exp(-x tr(D_b V P_j V*))dV,
    G_(j,b)(x)=-Z'_(j,b)(x)/Z_(j,b)(x),
    E_(k,b)(x)=(G_(k+1,b)-G_(k,b))
                  -(G_(k+1,0)-G_(k,0)),   0<=k<n.

The prime in G differentiates x while a,r,b are fixed. The quotient
uses the positive real branch near b=0, justified below. Each rank has
its own partition function; no common normalizer is assumed. When n=2
the background r has no entries and is immaterial. Repeated rates,
a=r, and both adjacent endpoint ranks are included.

## Conclusion

For every parameter choice above the limit exists and

    |lim_(b->0) E_(k,b)(x)/(x*b^2)| <= 2/3.             (1)

More precisely, put u=x(a-r), Q=V P_j V*, S=Q_11+Q_22 and
T=Q_11-Q_22. Write E_(j,u) for expectation under Haar measure tilted
by exp(-u*S), divided by its own positive integral, and set

    m_j(u)=E_(j,u) T^2,
    R_j(u)=m_j(u)+(u/2)m_j'(u).

Then

    lim_(b->0) E_(k,b)(x)/(x*b^2)=R_(k+1)(u)-R_k(u),
    |R_j(u)|<=1/3,       R_0(u)=R_n(u)=0.               (2)

In particular the adjacent endpoint cases have bound 1/3. The uniform
constant 2/3 in (1) is not claimed sharp. The n=2 case attains absolute
response 1/3.

This is the restricted intermediate result of research step1206;
independent conceptual audit1208 retains (1)-(2), with no strengthening
of their scope or constants. Assessment1204's checked
sources supplied no matching response estimate, which does not establish
originality. The conclusion is only a bound on the infinitesimal
coefficient. No uniform finite-b remainder, arbitrary background
spectrum, sum over conjugate pairs, actual-Xi transfer, all-degree
positivity or RH conclusion is asserted.

## Proof

### Local branch, separate normalizers and differentiation

An orthogonal projection satisfies 0<=Q_ii<=1, so 0<=S<=2 and |T|<=1.
Directly,

    tr(D_b Q)=r*j+(a-r)S+i*b*T.

Swapping coordinates 1 and 2 preserves the Haar law of Q and S, while
negating T. Thus, separately for every j,

    Z_(j,b)/Z_(j,0)=E_(j,u) cos(x*b*T).                 (3)

The denominator Z_(j,0)=exp(-x*r*j) integral exp(-u*S)dV is strictly
positive. If |x*b|<pi/2, the right side of (3) is at least cos(|x*b|)>0.
This proves the needed local positive branch without assuming any
dimension-uniform consequence of bare analyticity. Only its local use
is needed for (1).

On compact sets of complex x,b, the integrand and every fixed derivative
are bounded by a constant, since S,T are bounded and a,r,n are fixed.
Differentiation under the finite Haar integral is therefore valid.
Around any fixed real x>0,b=0, the positive ratio (3) has a nonvanishing
complex neighborhood and a local analytic logarithm. Evenness in b and
the cosine expansion give, with H_j and its x derivative bounded on a
possibly smaller neighborhood,

    log(Z_(j,b)/Z_(j,0))
      = -(x^2*b^2/2)m_j(x(a-r)) + b^4 H_j(x,b).

Taking minus the x derivative at fixed a,r,b proves

    G_(j,b)-G_(j,0)
      = x*b^2 [m_j(u)+(u/2)m_j'(u)] + O(b^4).           (4)

All remainders here are local at fixed parameters; no supremum over
parameters is interchanged with this expansion. For completeness,
ordinary quotient differentiation gives

    m_j'(u)=-Cov_(j,u)(S,T^2).

Subtracting (4) for the two independently normalized ranks proves the
limit formula in (2). It remains to bound R_j uniformly in real u,n,j.
The bound |T|<=1 by itself would not control u*m_j'(u).

### Averaging inside the two-dimensional corner

Let ell<=h be the eigenvalues of the leading two-by-two corner of Q.
They lie in [0,1]. Conjugation by diag(W,I_(n-2)), W in U(2), preserves
the Haar law of Q and the tilt exp(-u*S). Averaging over this additional
independent W is therefore legitimate. For a fixed corner with
eigenvalues ell,h, its diagonal difference after conjugation is

    (h-ell)(2p-1),

where p is uniform on [0,1]. One elementary justification is that a
Haar unit vector in C^2 is a normalized pair of independent standard
complex Gaussians: their squared magnitudes are independent unit
exponentials, and the change of variables (z_1,z_2)=(s*p,s*(1-p)) has
density s*exp(-s) on s>0, 0<p<1. Integrating s makes p uniform.
Consequently the average square of the diagonal difference is
(h-ell)^2 integral_0^1 (2p-1)^2 dp=(h-ell)^2/3. It follows that

    m_j(u)=(1/3) E_(j,u)(h-ell)^2,   0<=m_j(u)<=1/3.   (5)

This identity uses block invariance, not an identification of the laws
at different ranks. At j=0,n the corner is scalar and m_j is identically
zero. For n=2,j=1 its eigenvalues are 0,1 and m_1 is identically 1/3.
These cases already satisfy (2). Also u=0 gives R_j(0)=m_j(0), bounded
by (5). Below take n>=3, 1<=j<n and u!=0.

### The real tilted corner comparison used from C030l

C030l proves the following auxiliary statement in its orbital-law,
finite-mesh and continuum-limit argument: for weakly increasing real
top rows lambda<=mu coordinatewise, the full corner-eigenvalue arrays
of V diag(lambda)V* and V diag(mu)V*, tilted respectively by the same
field exp(sum_(s<n)c_s S_s) and normalized separately, are ordered in
expectations of continuous increasing functions of the array. Here S_s
is the sum of eigenvalues of the leading s-by-s corner. The fields c_s
are arbitrary real numbers, and repeated top eigenvalues are included
by the Haar continuity argument proved there.

That is the real positive-law input used here. C030l's source is
Suvrit Sra, *On some positivity properties of the Riemann Xi function*,
[author v3, 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Lemma C.7 and Theorem C.8, printed pp25-27. Its uniform orbital-law
input for strict top rows is G. Olshanski, *Projections of Orbital
Measures, Gelfand-Tsetlin Polytopes, and Splines*, J. Lie Theory 23
(2013), 1011-1022,
[Corollary 3.2, p1017](https://www.heldermann-verlag.de/jlt/jlt23/olshla2e.pdf).
We use C030l's established comparison including its repeated-row
extension; no general HCIZ formula, corner theorem or complex
stochastic order is reproved or assumed.

Fix epsilon in {-1,1}, and for t>0 consider Y=t V P_j V*, with its
own probability law tilted by exp(-epsilon*tr(Y_[2])). The notation
Y_[2] means its leading two-by-two corner. This is precisely the
fixed field c_2=-epsilon, all other c_s=0. Let ell_t<=h_t be the two
corner eigenvalues under that law, and set

    N_j^epsilon(t)=E_t^epsilon (h_t-ell_t)^2.

Its top row is lambda(t)=(0^(n-j),t^j). For eta>0,

    lambda(t) <= lambda(t+eta) <= lambda(t)+eta*(1,...,1).

Translation of every top eigenvalue by eta translates every corner
eigenvalue by eta. The tilted weight is multiplied by the constant
exp(-2*epsilon*eta), which cancels against that translated law's own
normalizer. Thus C030l's comparison gives the two stochastic orders

    law_t <= law_(t+eta) <= translation_eta(law_t).      (6)

In particular, for each of the two corner eigenvalues,

    0<=E_(t+eta) ell_(t+eta)-E_t ell_t<=eta,
    0<=E_(t+eta) h_(t+eta)-E_t h_t<=eta.               (7)

These are comparisons of normalized expectations. They do not assert
that the partition functions at t,t+eta are equal.

### A bounded change of the squared corner gap

Write U=t+eta. On the triangle 0<=ell<=h<=U, both functions

    F_U(ell,h)=(h-ell)^2+2U*ell,
    H_U(ell,h)=-(h-ell)^2+2U*h

are increasing in both coordinates. Indeed their respective partial
derivatives are (2U-2(h-ell),2(h-ell)) and
(2(h-ell),2U-2(h-ell)), all nonnegative. Here is an explicit global
extension, also checked in audit1208. Set c_U(v)=min(U,max(0,v)),
L=c_U(ell), H=c_U(h), and d=(H-L)_+. Use

    F_tilde(ell,h)=d^2+2U*L,
    H_tilde(ell,h)=-d^2+2U*H.

On 0<=L<=H<=U the derivative pairs are the ones just displayed.
On 0<=H<=L<=U they are (2U,0) and (0,2U), respectively.
The two pieces agree continuously at H=L, and clipping is increasing
in each coordinate. Thus both extensions are continuous and increasing
on all of R^2, and agree with F_U,H_U on the triangular supports.
Viewed as functions of the full array, they are constant in every
other coordinate, so they are legitimate tests in C030l's comparison.

Apply the first order in (6) to F_U and H_U. With Delta denoting the
expectation at t+eta minus that at t, this gives

    -2U Delta E ell <= N_j^epsilon(t+eta)-N_j^epsilon(t)
                         <= 2U Delta E h.

Using (7) yields the uniform, dimension-free inequality

    |N_j^epsilon(t+eta)-N_j^epsilon(t)| <= 2(t+eta)*eta. (8)

Writing everything back in the fixed Haar variable Q shows that N is
smooth: it is t^2 times the quotient of integrals of the bounded
continuous function (h(Q)-ell(Q))^2 with weight exp(-epsilon*t*S).
The weight is smooth and its denominator positive. Divide (8) by eta
and let eta decrease to zero to obtain

    |(N_j^epsilon)'(t)|<=2t.                           (9)

For u=epsilon*t, (5) gives

    N_j^epsilon(t)=3t^2 m_j(epsilon*t),
    (N_j^epsilon)'(t)/(6t)
       =m_j(u)+(u/2)m_j'(u)=R_j(u).

Thus (9) proves |R_j(u)|<=1/3 for both signs of u. Together with the
previously treated zero contrast, n=2, and endpoint ranks, this proves
(2) in full. The triangle inequality for R_(k+1)-R_k proves (1).

### Exact endpoint check and scope

For n=2,j=1 the Haar calculation above gives

    Z_(1,b)(x)=exp(-a*x) sin(x*b)/(x*b),
    G_(1,b)-G_(1,0)=1/x-b*cot(x*b)=x*b^2/3+O(b^4),

with the removable value at b=0. The rank-zero and rank-two responses
vanish, so the two adjacent normalized limits are 1/3 and -1/3.
This checks the normalization, derivative sign and limiting coefficient.

The argument controls only the quadratic phase coefficient. Positivity
of the local quotient in (3) does not bound its finite-phase logarithmic
derivative. The compact Taylor argument did not supply a parameter-uniform
fourth-order remainder. With unequal background rates the scaled real
tilt is no longer just the fixed S_2 field used in (6), and no such
extension is claimed here. The finite real-reference requirements in
C030l and all actual-Xi signing/realization gaps remain unpaid.

### Independent conceptual audit1208 (17 November 2026)

Verdict: (1)-(2) pass the specified audit, relative to C030l's proved
real comparison and its precisely cited strict-row orbital-law input.
No numerical evidence, stronger finite-phase estimate or new theorem
is used in this verdict. The following are the load-bearing checks.

The analytic expansion is in a neighborhood of each fixed real x>0,
b=0. The positive lower bound in (3) makes the local logarithm
legitimate. Compact Haar domination applies to the mixed x,b
derivatives, so differentiating b^4 H_j leaves O(b^4) at fixed rates.
In particular du/dx=a-r is included in (4). Each rank has its own
positive normalization throughout; the only comparison between ranks
in the bound is the final triangle inequality. Block U(2) conjugation
preserves S as well as the law, so its uniform-orientation second
moment may be averaged before or after the normalized tilt.

The full array comparison needed in (6), rather than just C030l's
scalar conclusion, was checked in that canonical proof. Its discrete
conditional CDF calculation uses positive but separately normalized
weights for every real field. Its decreasing-coordinate argument
gives irreducibility; stationary marginal limits precede mesh limits.
The imported Lebesgue orbital law is used only for strict rows.
Simultaneously ordered strict rational approximants and bounded Haar
continuity, with denominators bounded away from zero on a fixed
compact top-row set, then cover the repeated projection rows here.
Thus no ambient density is assigned to a collapsed polytope.

For n>=3, c_2=-epsilon is an available proper-corner field and is
fixed while t varies; n=2 was treated directly. For epsilon=-1
the positive weight grows with S_2, which C030l permits. Under
translation by eta*I every proper corner shifts by eta*I_s;
its S_2 increases by 2eta. The factor exp(-2*epsilon*eta) cancels
within the translated law. This proves its exact translated
probability distribution and (7), without equating any two different
partition functions or claiming an almost-sure coupling.

The global tests made explicit above require no monotonicity of the
squared gap itself. Their two expectation inequalities, combined
with 0<=Delta E ell,Delta E h<=eta, imply both sides of (8).
Smoothness of N follows from its fixed-Haar integral representation;
no derivative of individual eigenvalue paths or differentiation of a
stochastic coupling is required. Its right finite difference therefore
converges to its ordinary derivative. Differentiating
N=3t^2 m_j(epsilon*t) gives N'=6t R_j(epsilon*t), including the
negative-contrast chain-rule sign. This validates (9) and the constant.

At a=r no division by u occurs: R_j(0)=m_j(0). At j=0,n the
response vanishes exactly. At n=2 the sine quotient independently
checks the derivative sign, normalization and adjacent responses
+1/3 and -1/3. These cases complete the claimed parameter range.
Only the infinitesimal coefficient is retained; the uniform constant
does not authorize an exchange of a parameter supremum with b->0.

## Mathlib

Full matching coverage of (1), of the auxiliary tilted corner comparison,
and of its orbital-law input is unchecked; no absence claim is made.
Haar invariance, differentiation of bounded parameter integrals and
elementary monotone-function estimates support this proof, but matching
Mathlib theorem names were not checked or formalized in this step.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
