# C750l: The fixed middle-indicator response passes prime97/8

## Hypotheses

Use a=9/4, b=log101/2, r=(a/b)log97, w=2a-r,
k=2log97/sqrt97 and the exact conventions of C750i:

    I=(-a,a), I_L=(-a,-a+w), I_R=(a-w,a),
    E=I_L union I_R, M=(-a+w,a-w), m=|M|=2a-2w,
    e=1_E, h=1_M, f_t=e+t h, t real,
    F_f(xi)=integral_R f(x) exp(-i xi x)dx,
    J[f]=(1/(2pi))integral_R log(2+|xi|)|F_f(xi)|² dxi,
    D_a={f in complex L2(R): f=0 a.e. outside I, J[f]<infinity},
    C_f(s)=integral_R f(x+s)conj(f(x))dx,
    (U_b f)(x)=sqrt(a/b)f(ax/b).

Lebesgue measure and zero extensions are understood. Only this fixed
real affine family is tested inside the complex domain; there is no
parity/neutrality premise on a larger class. Assessment1155, approved
separately1156, covers this finite-span calculation, including original
full-frequency J and the unchanged one-eighth allocation.

Computer-assisted statements assume MPFR4.2.2 directed rounding,
Python integer semantics and the ctypes C ABI used by the existing
384-bit backend. Its arithmetic contract is the
[MPFR4.2.2 manual, Section4.4](https://www.mpfr.org/mpfr-4.2.2/mpfr.html#Rounding);
outward decimal conversion uses Section5.4, mpfr_get_str. Earlier
backend/ABI audits remain supporting platform evidence, not formal
verification of MPFR or Python. Separate correctness audit1159 below
confirms the analytic specialization and the complete certificate
under these same platform qualifications.

## Conclusion

Every f_t belongs to D_a and has C_(U_b f_t)(log97)=w>0.
Write its full-J energy matrix in the ordered basis (e,h) as

    [ EE  EM ] ,  J[f_t]=EE+2t EM+t² MM.
    [ EM  MM ]

Complete directed enclosures, weakened outward here, are

    0.29695626 < EE < 0.29704288,
   -0.11841990 < EM < -0.11837759,
    4.26144969 < MM < 4.26187214,
    0.29282701 < 8kw < 0.29282702.

In particular MM>0. Its exact minimizing amplitude t_*=-EM/MM
satisfies

    0.02777596 < t_* < 0.02778865,
    0.00083852 < min_(t real)(J[f_t]-8kw) < 0.00092782.   (1)

Thus every member of this fixed family satisfies the allocation, with
a positive margin. This is new local exclusion evidence for this
family, using known methods; it is not a claim of mathematical novelty
beyond the assessed sources. It supplies neither a uniform lower
bound on arbitrary extensions nor a counterexample to the allocation.
No different middle shape, collar, cap, allocation fraction, phase or
support has been searched. The complete dilation budget,
J-to-baseline comparison and actual-Xi positivity remain unresolved.

## Proof

### Domain, exact correlation and all matrix interactions

C750i gives 0<w<a, r=2a-w>a, r>w and the normalized identity
C_(U_b f)(log97)=C_f(r). Its change of variables cancels a/b against
the dilation Jacobian. Since I intersect (I-r)=I_L and I_L+r=I_R,
only x in I_L contributes to C_f(r) for any supported f. The other
eight ordered pairings between I_L,M,I_R have zero intersection
measure after this shift: x in M or I_R gives x+r outside I,
and x in I_L gives x+r only in I_R. Our f_t equals1 on both
collars, so C_f_t(r)=integral_(I_L)1 dx=w, independently of t.
All boundary points have measure zero.

An interval indicator of length L has Fourier transform
exp(-i xi u)(1-exp(-i xi L))/(i xi) for xi!=0, with removable
value L at0. Its modulus is bounded by min(L,2/|xi|). Therefore
|F_f_t| is bounded near0 and is at most (4+2|t|)/|xi| away
from0. The majorant log(2+|xi|)/xi² is integrable for |xi|>=1.
This proves finite J for each t and for both basis vectors, without
needing a general nonsmooth-boundary domain theorem.

Import C750k's audited full whole-line form, with its restored log2,
rate-two kernel and complex-domain justification:

    J[f]=log2 ||f||²+(1/2)integral_(R x R)
                      |f(x)-f(y)|² j(x-y)dxdy,
    j(z)=(1/pi)integral_0^infinity e^(-2s)/(s²+z²)ds, z!=0. (2)

Its precise primary input is Chen–Song, *Two-sided eigenvalue estimates
for subordinate processes in domains*, JFA226(2005),90–113,
DOI10.1016/j.jfa.2005.05.004,
[Section2(2.5)–(2.7), printed pp94–96](https://rsong.web.illinois.edu/pages/evest.pdf).
The conservative symmetric Cauchy semigroup with independent zero-drift
subordinator of Levy measure e^(-2s)ds/s satisfies its hypotheses.
C750k verifies that measure's integrability, the rate change giving
log((2+|xi|)/2), the additive log2, both exterior orientations and
the extension to complex L2. No extended non-L2 domain or interchange
of killing and subordination is imported. We use this established
identity rather than reprove general form theory. What remains here
is exact finite-interval integration, normalization and certification;
none of the sources supplies these particular matrix entries.

For L>0 and g>=0 define the finite quantities

    A(L)=J[1_(0,L)],
    K_g(u,v)=integral_0^u integral_0^v j(g+x+y)dy dx.

Translation invariance makes A depend only on length. The cross
energy of disjoint real indicators 1_A,1_B is -integral_(A x B)j:
the log2 cross term is zero and expanding the product of differences
in(2) leaves its two negative orientations. Polarization is justified
by Cauchy–Schwarz in the finite-energy difference measure; both
indicators already have finite J. Consequently touching endpoints
cause no undefined cancellation of divergent energies.

There are two collar–middle pairs, each adjacent with lengths w,m,
and one collar–collar pair of gap m and lengths w,w. Hence exactly

    EE=2A(w)-2K_m(w,w),
    EM=-2K_0(w,m),
    MM=A(m).                                           (3)

The cross term in J[e+t h] is 2t EM, not t EM. In particular all
three supported pairs, their orientations and the full frequency
range are retained. C750h's older wide numerical pulse enclosure
and C750j's cap are historical comparisons, not numerical inputs.

### Complete scalar spatial integrals

The two ends of (0,L), including both orientations in(2), give

    A(L)=L log2+2integral_0^L z j(z)dz
                   +2L integral_L^infinity j(z)dz
        =L log2+(1/pi)integral_0^infinity e^(-2s)G_L(s)ds,
    G_L(s)=log(1+(L/s)²)+(2L/s)atan(s/L).               (4)

For example integrate the exterior tail H(x)=integral_x^infinity
j(z)dz over x in(0,L): the contribution is 2integral_0^L H(x)dx.
Nonnegative Tonelli gives 2integral_0^infinity min(L,z)j(z)dz,
which proves the first line. Substituting(2), again by Tonelli,
and integrating z/(s²+z²) and the Cauchy tail proves(4).

For fixed s>0 let

    Phi_s(z)=-(z/s)atan(s/z)-(1/2)log(s²+z²), z>0,
    Phi_s(0)=-log s.

It is continuous at0 and, for z>0,
Phi_s'(z)=-(1/s)atan(s/z), Phi_s''(z)=1/(s²+z²).
Integration on the rectangle, with continuity at a zero endpoint,
therefore gives

    Q_g(s;u,v)=Phi_s(g+u+v)-Phi_s(g+u)-Phi_s(g+v)+Phi_s(g),
    K_g(u,v)=(1/pi)integral_0^infinity e^(-2s)Q_g(s;u,v)ds. (5)

This representation cancels the linear pi*z/(2s) in the usual
primitive analytically before interval evaluation. It avoids
oscillatory Fourier tails without changing J.

All four functions integrated in(4)–(5), including e^(-2s), are
positive and decreasing for s>0. For Q this follows directly from
its positive spatial integral of (s²+(g+x+y)²)^(-1). For G use

    G_L(s)=2[integral_0^L z/(s²+z²)dz
                    +L integral_L^infinity 1/(s²+z²)dz].

The denominators increase with s; the exponential is decreasing.
These observations prove monotonicity on whole panels. Positivity
or monotonicity is not inferred from sampled values.

### Fixed rectangles and both complete omitted ranges

Freeze delta=2^(-24), S=16 and 2048 equal panels on each dyadic
interval [2^q,2^(q+1)], q=-24,...,3. There are57344 panels.
On [s_i,s_(i+1)], with positive decreasing integrand V, use

    (s_(i+1)-s_i)V(s_(i+1))
       <= integral_(s_i)^(s_(i+1)) V(s)ds
       <= (s_(i+1)-s_i)V(s_i).                         (6)

All nodes and widths are exact rational dyadics. No Simpson/Gauss
error theorem, differentiability at s=0 or mesh convergence claim
is needed: the bounds in(6) already cover every finite panel.
The following allowances cover every s outside the mesh.

For 0<s<delta<L, (L/s)>1 and sqrt(1+(L/s)²)<=2L/s,
while atan(s/L)<=s/L. Thus

    integral_0^delta e^(-2s)G_L(s)ds
           <=2delta[log(2L/delta)+2].                 (7)

The certificate's complete endpoints give delta<w<m, so this
applies to both L=w and L=m. For the adjacent pair enlarge the
second interval to infinity and integrate in its coordinate:

    Q_0(s;w,m)
       <=integral_0^w atan(s/x)dx/s
       <=pi/2+log(w/s), 0<s<delta<w.

The second inequality splits x at s, using atan(s/x)<=pi/2
below s and <=s/x above s. Consequently

    integral_0^delta e^(-2s)Q_0(s;w,m)ds
            <=delta[pi/2+log(w/delta)+1].              (8)

For the far pair the spatial denominator is at least m²,
so its small-s integral is at most delta*w²/m².
The lower bound for every omitted range is zero.

For s>=S, log(1+x)<=x and atan<=pi/2 imply
G_L(s)<=L²/S²+pi L/S. The spatial denominators in Q are at
least s², giving Q_0<=wm/S² and Q_m<=w²/S² there. Integrating
e^(-2s) yields the respective upper tail allowances

    e^(-2S)/2 [L²/S²+pi L/S],
    e^(-2S)wm/(2S²),   e^(-2S)w²/(2S²).                (9)

All(7)–(9) precede the common division by pi. Restore L log2
for A(L). These are the entire s tails of the exact spatial
representation, not a frequency cutoff standing in for J.

### Directed certificate and scalar minimization

Run from this notebook:

    python3 scripts/prime-collar/certify_1157.py
    python3 scripts/prime-collar/check_output_1157.py

The full records are
[scripts/prime-collar/certificate-1157.json](../scripts/prime-collar/certificate-1157.json)
and
[scripts/prime-collar/certificate-output-check-1157.json](../scripts/prime-collar/certificate-output-check-1157.json).
The first script uses only the unchanged interval backend in
scripts/pivot-area/certify_1136.py. It records source hashes, MPFR
version4.2.2, precision384, all57345 nodes and all229380 integrand
intervals, cumulative lower/upper sums after each octave, every
small/tail allowance, all three matrix entries, threshold and exact
scalar-minimum enclosures. Basic operations are rounded outward;
products take all endpoint extrema; squares here are of strictly
positive intervals; log/atan/exp are monotone on their arguments.
No trigonometric approximation is used. Outward decimal conversion
is applied again on persistence. Binary64 is console display only.

The second script reads every saved node and checks its exact dyadic
location, positivity and endpoint ordering. Using Python Fraction,
it independently accumulates all four right-lower and left-upper
rectangle sums, including every panel. It then reconstructs the
complete integrals, matrix and decisive minimum from those wider
saved node intervals, the full tail allowances, directed pi/log2
endpoints and geometry. It separately recomputes the minimum from
the printed matrix/threshold endpoints. Both exact-rational routes
give the strict bounds(1). This current-step verification is not
the later independent critical audit of the argument/backend.

The first output-check script incorrectly required sums of outward
decimal node endpoints to lie inside the tighter cumulative MPFR
enclosures. That containment check failed: decimal persistence widens
the node intervals. The failed script and certificate are preserved
as scripts/prime-collar/check_output_1157_initial.py and
scripts/prime-collar/certificate-output-check-1157-initial.json.
The corrected check does not rely on that containment. It uses every
decimal node directly for the independent complete bounds above;
comparison with all28 saved cumulative bounds within1e-90 is only
a diagnostic. The exact full-node proof does not use this tolerance.
No mathematical parameters, original certificate or original
calculation script were changed to repair the check.

The complete matrix, full-kernel integral, small/tail, geometry and
minimum endpoints were inspected. Before division by pi the four
small-s allowances are respectively below

    1.919e-6, 2.482e-6, 9.521e-7, 4.734e-12;

the four large-s allowances are below

    4.903e-17, 5.981e-15, 4.309e-18, 3.841e-20.

No old pulse enclosure is narrowed by rerunning its quadrature.
Equations(3)–(9) supply the matrix bounds in the conclusion from
full original-J spatial integrals with all cross entries retained.
All current-step verification assertions pass.

Since MM>0, ordinary scalar completion of the square gives exactly

    J[f_t]-8kw
      =MM(t+EM/MM)²+EE-EM²/MM-8kw.                    (10)

This uses only a two-dimensional finite Gram form, not an inverse
of the unbounded J operator on arbitrary collar data. Directed
interval evaluation encloses the last three terms in

    [0.0008385279268795933544...,
     0.0009278138391149551443...].

The endpoints displayed with ellipses here are explanatory; the
complete outward decimal endpoints are in the certificate. Exact
rational evaluation using the full saved matrix endpoints separately
proves the weaker strict bounds(1), without using rounded console
values or a preview as evidence. The amplitude enclosure follows
from -EM/MM with its strictly positive denominator.

The preassigned continuation/abandonment test is therefore decided:
the minimum is positive, and this single family closes. There is
no change of middle shape, width, support or allocation fraction
and no new search after the result. The certificate also retains
one non-load-bearing preassigned rational amplitude1/20; it is
positive as expected from(10), not a counterexample. C750h's older
collar-only closure, C750i's whole-line inverse stop, C750j's cap
stop and C750k's exterior-only stop preserve their distinct scopes.
Neither this finite-span exclusion nor a later audit would resolve
the uniform original allocation, complete Weil budget or RH.

### Separate correctness audit1159 — 16 November2026

This audit uses the unchanged SPECIALIZE scope in assessment1157,
separately approved1158. It checks the entire fixed-family assertion,
not a new shape or a uniform extension theorem. The mathematical
inputs remain exactly C750i (geometry/pairing) and C750k (full form).
No new edge or positivity assumption is introduced.

**Analytic checks.** In the correlation, a/b from the two dilation
factors cancels b/a from dx. Since r=2a-w>a, the intersection of
I with I-r is exactly I_L up to endpoints, and I_L+r=I_R. This
checks all nine ordered interval pairings: only left-to-right remains.
The Fourier bounds prove finite energy before polarization. Expanding
the bilinear difference form for disjoint indicators gives -1 for
each of its two opposite orientations, followed by the factor1/2.
Thus its cross entry is -integral_(A x B)j, and the two collar–middle
pairs give EM=-2K_0(w,m); the scalar energy uses 2t EM. The far-pair
gap is m, not r, and its contribution to EE is -2K_m(w,w).

For each fixed s>0, Phi_s(0)=-log s is its actual right limit,
Phi_s'(0+)=-pi/(2s), and Phi_s''(z)=1/(s²+z²) extends continuously
to zero. Twice integrating this derivative on the closed finite
rectangle therefore also justifies(5) when g=0. Its four terms are
not separately integrated down to s=0. The positive spatial-integral
representations in(4)–(5) prove monotonicity for every positive s,
including the touching case; no sampled sign supplies this fact.
Tonelli is used only for nonnegative integrands. Finite energy and
Cauchy–Schwarz justify signed polarization afterwards.

The endpoint allowances are valid on the entire missing ranges.
For(7), G_L(s)<=2log(2L/s)+2 and integrating log(1/s) adds the
second constant in its bracket. For(8), the split at x=s is valid
because delta<w; integrating log(w/s) adds exactly delta. The far
denominator is at least m². For the other tail, s>=S bounds the
denominators by S² and atan by pi/2, while integrating exp(-2s)
contributes exp(-2S)/2. These bounds precede division by pi. The
saved geometry verifies delta<w<m and all overlap conditions.
The log2 diagonal contributions are retained. These checks confirm
that the numerical matrix encloses original full-frequency J.

**Implementation and full evidence.** Run from this notebook:

    python3 scripts/prime-collar/audit_1159.py

The complete audit is
[scripts/prime-collar/certificate-audit-1159.json](../scripts/prime-collar/certificate-audit-1159.json),
and its separately preserved unchanged-grid replay is
[scripts/prime-collar/certificate-1157-replay-1159.json](../scripts/prime-collar/certificate-1157-replay-1159.json).
All41 checks pass. The replay is field-for-field identical to the
original, and all original1157 scripts/certificates, including the
failed output check, retain their hashes. All57345 dyadic nodes,
229380 integrand intervals and28 cumulative blocks are checked.
The audit independently sums every right lower and left upper
rectangle using exact Python Fractions and records the four complete
cumulative bounds after every octave. It restores every small/large
allowance and the log2 term, reconstructs all matrix entries and
the threshold, and evaluates the minimizing amplitude and minimum
with exact rational interval arithmetic. Both this full-node route
and a separate calculation from the saved matrix endpoints verify
all displayed strict bounds, especially(1). Neither uses a tolerance
comparison to establish sign.

The implementation review checks the actual log, exp, atan and sqrt
wrappers against the MPFR4.2.2 contracts: increasing unary functions
use lower/down and upper/up endpoints; multiplication takes all four
extrema; division excludes zero; the specialized square is used only
on positive intervals, including abs(EM). Constants, mesh and widths
are exact integers or dyadics before directed arithmetic. The exact
node formulas implement(4)–(5), with g+w+w=2a for the far pair.
Every computed operation is checked finite by the backend. See the
[MPFR4.2.2 manual, Section5.7](https://www.mpfr.org/mpfr-4.2.2/mpfr.html#Transcendental-Functions)
for the named transcendental contracts; this is an API assumption,
not a reproof of the library.

For decimal persistence, the audit obtains each finite binary endpoint
using384 base-two digits, converts it exactly to a Fraction, and
compares it with the persisted signed decimal/exponent expression.
All573986 checked endpoints are outward. A freshly compiled unchanged
C probe matches MPFR/header version4.2.2, precision384, rounding
constants[3,2], structure/type sizes[32,8,4,8,8] and field offsets
[0,8,16,24]. ctypes argument widths and signatures used by these
operations agree. Unused return values of void functions do not enter
any numerical decision. This checks applicability on the installed
platform; it does not independently implement the transcendental
functions or formally verify MPFR, ctypes, the compiler or Python.

The initial failed containment assertion remains invalid: independently
outward decimal nodes can produce wider sums than the binary sums.
Audit1159 does not assert that containment, rerun it as a passing test,
or use the corrected check's1e-90 diagnostic tolerance. The complete
Fraction reconstruction gives the decisive sign directly. Also,
certify_1157.py has a stale comment calling t=1/20 a point in a
negative witness region. Its actual recorded witness margin is
positive and it is not used for(1); no negative witness was found.
The original script is preserved, with this comment qualified here.

Finally MM>0 and EM<0 are verified before the square/minimization.
Completion(10) therefore has no denominator or complex-square
ambiguity. The strict positive minimum is confirmed for every real t,
conditionally only on the stated platform semantics. This advances
local verification of the existing exclusion, not the numerical
margin or mathematics beyond the previously checked sources. The
fixed-family route remains closed without retuning; arbitrary middle
responses, the complete dilation budget, J-to-baseline comparison and
actual-Xi positivity remain open. PROOF's main argument is unchanged.

## Mathlib

Full matching coverage was not checked. Supporting ingredients are
indicator Fourier transforms, Plancherel/polarization, nonnegative
Tonelli, elementary interval integration, monotone rectangle bounds
and scalar completion of the square. The cited subordinate form is
an imported informal theorem with its local specialization already
justified in C750k. No matching formal matrix certificate, Lean
verification or absence from Mathlib is asserted.
