# Lemma 662: the signed endpoint pair prevents half-turn census suppression

## Hypotheses

Retain L649's definitions with n>=5, x=-d=-5/4, R=11/8,
U=R^2=121/64, eta=1/100 and the full grid t_j=j/n, 0<=j<n:

    B_u(a)=product_j R*(a-t_j*u)/(U-t_j*a/u),
    W_a(u)=B_u(x)/B_u(a),
    c_k(u)=R^(-1) sum_a r_a W_a(u)(a/R)^k,
    G(u,zeta)=sum_(0<=k<M)c_k(u)zeta^k,
    D=sum_a r_a^2 mean_u |W_a(u)|^2/(U-|a|^2),
    H=max_u mean_zeta log|G(u,zeta)|.

Circle measures and arc means are normalized, and logarithms are natural.
The denominator angle is conjugated on |u|=1. Specialize to L661's
common pole census, fixed before u varies:

    n=6q+3>=1210,       M=2q+1=n/3,
    A_j=1/(d-t_j),      b_j=t_j/(U-d*t_j),
    phi_n(y)=sum_j [atan(A_j*y)+atan(b_j*y)] for real y,
    phi_n(y_l)=pi*l,    -q<=l<=q,
    phi_n(Y_n)=pi*n/6,  a_l=x+i*y_l,   r_(a_l)=1.       (1)

L661 proves that these are distinct admissible poles, include x,
have |a_l|<=R-eta, and satisfy 0<Y_n<27/100. Use its analytic
phi_n on |Im y|<1/4, rational function S_n=exp(2i phi_n), kernel
K_n=2i phi_n'/(S_n-1), and positively oriented rectangle Gamma_n
with Re y=+/-Y_n and Im y=+/-h, h=1/8. Set

    w_n(y)=W_(x+i*y)(1),  rho_0=81/6250,
    kappa=91/5000,       sigma^2=137/5000.

No spacing or symmetry is imposed on L649's general family; (1) is
a particular family with those additional properties. It is the only
family to which the conclusions below apply.

## Conclusion

There are absolute positive constants c,C and one existential onset
such that, along (1),

    max(|c_0(1)|,|c_1(1)|)>=c*|w_n(Y_n)|
                              >=c*exp(-rho_0*n),        (2)
    H>=-rho_0*n-log n-C.                                (3)

For a maximizing angle in H, take the centered connected arc I_n of
normalized measure n^(-2), as in L658. Then

    log mu(I_n)+2 mean_(I_n x T) log|G|-log D+n/16
                         >=9*n/50000-5log n-C.          (4)

In particular this census satisfies the proposed paid-arc criterion
with C=0 beyond an existential onset. Its signed response cannot be
an all-arcs countersequence to that criterion. The conclusion does not
follow from L661's positive absolute contour cost: both endpoint phases,
the rest of the signed contour and the full spatial root cost are
controlled below. No effective onset or sharp asymptotic for H or D
is claimed.

The uniform criterion for arbitrary integer support, L651's uniform
joint response, Xi realization, matching upper bounds and all-degree
signs remain open. The conceptual audit in section 7 validates this
special-family result, including the inherited inputs actually used;
it does not audit every conclusion of those input lemmas or their source
manuscripts. It is not an RH candidate or a claim of originality beyond
the sources checked.

## Proof

### 1. Scope and known inputs

Reuse the unchanged EXPLORE assessment
`drafts/literature/2026-11-02-localized-logarithmic-joint-moment.md`.
The target is still its exact paid-arc comparison. L649 supplies the
definitions, L661 supplies the census and full finite-contour identity,
its endpoint amplitude bound and its improved diagonal envelope, and
L658 supplies finiteness of H and its angular localization. L651 is
downstream motivation, not an established response bound.

Import the standard residue theorem and simple-pole rule as in L661:
R. W. Howell and J. H. Mathews, *Complex Analysis*,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
Import the complete one-root logarithmic integral, including boundary
roots, from F. Brunault and W. Zudilin, *Many Variations of Mahler
Measures*, ISBN 9781108794459,
[Proposition 1.4, publisher excerpt pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf).
These are reused source inputs, not freshly audited manuscripts.

The proof specializes the assessed contour and root formulas. It does
not reprove Jensen, a quadrature theorem or a general norm inequality.
The short residue computation in section 4 verifies the complex
multiplier and its nonvanishing for the actual endpoint limit; it is
the familiar Euler beta/reflection value, not a new transform theorem.
Its branch and decay checks are included because a modulus-only
evaluation would not establish the endpoint pairing.

L661's absolute-cost stop and L660's monomial phase stop were checked
as contrasts; neither proves a signed coefficient bound. The fractional
and finite-screen failures recorded in the reused assessment are also
not counterexamples for this census. No new source blocker or stronger
source theorem is assumed here.

### 2. Bounds on the entire rectangle

Write A_j^+=1/(d+t_j), b_j^+=t_j/(U+d*t_j). Directly from the full
product, including t_0=0,

    w_n(y)=product_j (1-i*b_j^+*y)/(1-i*A_j^+*y).        (5)

For 0<=t<=1, 0<=b^+<A^+<=4/5. Their difference decreases in t.
At t=1/4,1/2,3/4,1 it equals, respectively,

    26/47>11/20,   60/161>37/100,
    85/362>23/100, 76/603>1/8.

The left n-point sum for a decreasing function is at least its
integral, and the four-cell right sum bounds that integral from below.
Consequently

    sum_j(A_j^+-b_j^+)>n*(51/160)>3n/10.               (6)

Put y=r+i*s with |r|<=27/100, |s|<=1/8, and set

    f(c)=c*(1+c*s)/[(1+c*s)^2+c^2*r^2].

For 0<=c<=4/5, differentiation gives

    f'(c)=[(1+c*s)^2-c^2*r^2]
                          /[(1+c*s)^2+c^2*r^2]^2>2/5. (7)

Indeed the numerator is at least 47709/62500>3/4, whereas the
denominator is at most 6168688681/3906250000<15/8. Also f(c)>=0
and f(A_j^+)<=A_j^+/(1+A_j^+*s)<=8/9<1. Applying (6)--(7) to
the logarithmic derivative of (5) gives the uniform real inequalities

    -n <= d/ds log|w_n(r+i*s)| <= -3n/25.             (8)

All factors are nonzero in this rectangle, so these derivatives and
their integrals are legitimate. For real r, (5) gives |w_n(r)|<=1.
In particular, for 0<=s<=h,

    |w_n(r+i*s)/w_n(r)|<=exp(-3n*s/25),
    |w_n(r-i*s)/w_n(r)|<=exp(n*s).                     (9)

For the phase product, take A in [4/5,4] and s>=0. Its A-factor
satisfies

    log |(1+i*A*(r+i*s))/(1-i*A*(r+i*s))|
      = (1/2)log[1-4*A*s/((1+A*s)^2+A^2*r^2)]
      <=-2*A*s/((1+A*s)^2+A^2*r^2)<=-6s/5.            (10)

To verify the last bound, the function
A/[(1+A/8)^2+(27*A/100)^2] has derivative of the sign of
1-A^2*(1/64+729/10000); its minimum on [4/5,4] is therefore at
an endpoint. The endpoint values are 50000/78541 and 10000/8541,
both greater than 3/5. Every b_j-factor has modulus at most one
above the real axis. Reflection in that axis reverses the modulus
of every factor. Thus, throughout the rectangle,

    |S_n(r+i*s)|<=exp(-6n*s/5),
    |S_n(r-i*s)|>=exp(6n*s/5),       0<=s<=h.          (11)

The partial-fraction formula for phi_n' in L661 also gives
|phi_n'|<11n here. For example, the A_j terms are bounded by
A_j/(1-A_j*h)<=8, and the b_j terms by b_j/(1-b_j*h)<8/3.
The same rational formulas give uniform O(n) second derivatives
on this closed rectangle; all their factor denominators have modulus
at least 1/2. Likewise (log w_n)''=O(n), with a local logarithm or
direct logarithmic derivatives of (5). Constants do not depend on n.

There is no small denominator in K_n at the real crossing of the
right edge. There S_n(Y_n)=-1. If |s|<=1/(100n), then
|phi_n(Y_n+i*s)-phi_n(Y_n)|<=11/100. Hence

    |S_n(Y_n+i*s)+1|<=exp(11/50)-1<=11/39<1,
    |S_n(Y_n+i*s)-1|>1.                               (12)

For larger |s|, (11) bounds the denominator by 1-exp(-6n*s/5)
above and exp(6n*|s|/5)-1 below. Combining this with (12) yields
one absolute C such that, on the full right edge,

    |K_n(Y_n+i*s)|<=C*n,                    s>=0,
    |K_n(Y_n+i*s)|<=C*n*exp(-6n*|s|/5),     s<=0.      (13)

In the small lower segment the last estimate follows after increasing
C by exp(6/500). Away from it, the factor 1-exp(-6/500) is bounded
away from zero. These estimates hold at s=0 as well.

On the upper horizontal edge, (9),(11) give
|w_n K_n|<=C*n*exp(-3n/200). On the lower edge they give
|w_n K_n|<=C*n*exp(-n/40). Multiplication by 1 or (x+i*y)/R
changes only C, since those factors are uniformly bounded here.
The horizontal lengths are uniformly bounded. Their combined
contribution to each of the first two coefficient integrals is
therefore

    O(n*exp(-3n/200))=o(|w_n(Y_n)|).                  (14)

For the equality on the right use L661's actual endpoint bound
|w_n(Y_n)|>=exp(-rho_0*n-1) and
3/200-rho_0=51/25000>0. No horizontal term is simply discarded.

### 3. Limit of the signed right endpoint integral

Define the continuous limiting phase on [0,27/100] by

    F(y)=integral_0^1 [atan(y/(d-t))
                              +atan(t*y/(U-d*t))] dt.

Its integrand and derivatives are continuous on this compact set,
and the full left Riemann sums phi_n(y)/n converge uniformly to F.
F is strictly increasing, F(0)=0, and L661's integral bound gives
F(27/100)>pi/6. There is a unique Y in (0,27/100) with F(Y)=pi/6,
and uniform convergence and strict monotonicity give Y_n->Y.

Put

    v_n=phi_n'(Y_n)/n -> v=F'(Y)>0,
    p_n=w_n'(Y_n)/(n*w_n(Y_n)) -> p,
    p=i integral_0^1 [A^+(t)/(1-i*A^+(t)*Y)
                           -b^+(t)/(1-i*b^+(t)*Y)] dt.

These convergences follow from the corresponding continuous integrands
on the same compact set. Write B=Im p. Equation (8), evaluated at
s=0, gives 3/25<=B<=1. Differentiating the upper bound (11) at
s=0, where log|S_n|=0, gives 2v_n>=6/5, hence 2v>=6/5.
In particular

    0<Re z<1,                z=(-i*p)/(2v).           (15)

For k=0,1 let the right edge be traversed upwards and set

    J_(k,n)=integral_right w_n(y) K_n(y) ((x+i*y)/R)^k dy.

Rescale y=Y_n+i*t/n. For fixed real t the O(n) second-derivative
bounds in section 2 give

    w_n(Y_n+i*t/n)/w_n(Y_n) -> exp(i*p*t),
    S_n(Y_n+i*t/n) -> -exp(-2v*t),
    K_n(Y_n+i*t/n)/n -> -2i*v/(1+exp(-2v*t)).         (16)

For the first line integrate the logarithmic derivative along the
short vertical segment; its exponent is i*p_n*t+O(t^2/n). This
does not choose an inconsistent logarithm of w_n(Y_n). The second
line uses the exact S_n(Y_n)=-1, not a limiting phase at Y.

The change of variable supplies dy=i*dt/n. For 0<=t<=nh,
(9),(13) bound the absolute normalized integrand by C exp(-3t/25).
For -nh<=t<=0 they bound it by C exp(-|t|/5). These same integrable
majorants work for k=1, because its extra factor is uniformly bounded.
Extend the integrands by zero outside [-nh,nh]. Dominated convergence
now proves, with a complex error tending to zero,

    J_(0,n)/w_n(Y_n) -> J,
    J_(1,n)/w_n(Y_n) -> ((x+i*Y)/R)*J,
    J=2v integral_(-infinity)^infinity
                              exp(i*p*t)/(1+exp(-2v*t)) dt. (17)

Equivalently J_(k,n)=w_n(Y_n)[((x+i*Y_n)/R)^k J+o(1)] for k=0,1.
The estimates control the entire vertical edges, not just finite
rescaled intervals, and include the lower edge of the local kernel.

### 4. The multiplier is nonzero and the endpoint pair is invertible

With z as in (15), the positive real substitution r=exp(2v*t) gives

    J=integral_0^infinity r^(-z)/(1+r) dr
                             =pi/sin(pi*z) != 0.      (18)

Here r^(-z)=exp(-z*log r) uses the real logarithm. For completeness,
the residue evaluation needed in (18) follows by integrating
f(w)=exp((1-z)*w)/(1+exp w) on the rectangle with real part +/-T
and imaginary part between 0 and 2pi. Its sole interior pole is
i*pi, with residue exp(-i*pi*z). The vertical integrals tend to
zero because 0<Re z<1. The upper integral, in the reverse direction,
is -exp(-2pi*i*z) times the lower one. Consequently
(1-exp(-2pi*i*z))*J=2pi*i*exp(-i*pi*z), proving (18).
There are no boundary poles and sin(pi*z)!=0 in this open strip.
This retains the complex multiplier; positivity of an absolute
integral is not being used to infer nonvanishing.

The symmetry of the actual products gives

    w_n(-conjugate(y))=conjugate(w_n(y)),
    K_n(-conjugate(y))=-conjugate(K_n(y)),
    x+i*(-conjugate(y))=conjugate(x+i*y).

Since the left edge is traversed downwards, its kth integral is
-conjugate(J_(k,n)). This sign includes both the kernel reflection
and the contour orientation. Extracting coefficients k=0,1 from
L661's full polynomial contour identity and using (14) therefore gives

    c_k(1)=(1/(pi*R)) Im J_(k,n)+o(|w_n(Y_n)|).        (19)

The coefficients are real, also directly from the symmetric census.
Set V_n=J*w_n(Y_n). Equations (17),(19) say

    c_0(1)=Im V_n/(pi*R)+o(|w_n(Y_n)|),
    c_1(1)=[x*Im V_n+Y_n*Re V_n]/(pi*R^2)
                                      +o(|w_n(Y_n)|). (20)

The real matrix in (20) has nonzero determinant proportional to Y_n.
Here Y_n->Y>0, so its inverse is uniformly bounded beyond one onset.
Explicitly the first row determines Im V_n, and the second gives
Y_n*Re V_n=pi*R^2*c_1-x*pi*R*c_0+o(|w_n(Y_n)|).
Thus |V_n|<=C max(|c_0|,|c_1|)+o(|w_n(Y_n)|). Since
|V_n|=|J|*|w_n(Y_n)| and J!=0, the errors can be absorbed.
This proves the first bound in (2). L661's endpoint bound proves
the second after changing c. No convergence of the endpoint phase
or noncancellation of either coefficient separately is assumed.

### 5. Full spatial root cost and the exact diagonal comparison

For a nonzero polynomial P of actual degree d_P and leading
coefficient gamma, the imported root integral gives

    exp(mean log|P|)=|gamma| product_alpha max(1,|alpha|).

Its constant coefficient has modulus at most this quantity. For
d_P>=1, its first coefficient is a sum of d_P products of d_P-1
roots times gamma, so its modulus is at most d_P times this same
quantity. For d_P=0 the first coefficient is zero. This elementary
specialization keeps every root, including zero and boundary roots,
and makes no integrality or zero-free assumption. Applying it to
the complete G(1,.) of degree at most M-1 gives

    max(|c_0(1)|,|c_1(1)|)
                         <=M*exp(mean_zeta log|G(1,zeta)|).

Together with (2) and M=n/3 this proves (3). It pays only a
logarithmic cost for the first coefficient; it does not apply a
degree-exponential generic norm comparison or truncate G to two terms.

L658 gives an arc of measure n^(-2) with paid logarithmic expression
at least 2H-2log n-32pi^2/9. L661's bound on the actual census
diagonal, with its original unit residues, is

    D<=n*exp(2*kappa*n+6)/(3*sigma^2).

Combining these in the correct directions gives

    log mu(I_n)+2 mean_(I_n x T)log|G|-log D+n/16
       >=(1/16-2*kappa-2*rho_0)*n-5log n-C
       =9*n/50000-5log n-C.

This is (4), and its right side tends to positive infinity. The
two logarithmic costs from (3), two from localization, and one from
the diagonal are all retained. The tiny positive rate is not used
to claim an effective numerical onset.

### 6. Verification and limitations

The exact rational inequalities in section 2 and the final exponent
comparison are checked by

    python3 scripts/one-sided-hankel/signed-phase-endpoint-bounds.py

The complete output is
`scripts/one-sided-hankel/signed-phase-endpoint-bounds.json`.
All 15 checks, their actual and required rational bounds, and the
complete rate comparison were inspected. The failures list is empty.
This is not an independent verification of dominated convergence,
the contour orientation, the cited inputs or L661's analytic proof.
No numerical integral or finite screen is a premise. The asymptotic
proof establishes existence of an onset, not a computable value here.

The result closes this particular census as a possible counterexample
to the paid criterion; it does not promote symmetry, phase spacing,
unit residues or these endpoint formulas to general admissible support.

### 7. Independent conceptual audit — 2 November 2026

The audit accepts (2)--(4) with their stated existential onset and
special census hypotheses. No mathematical correction or stronger
conclusion is required. This is validation of the existing argument,
not another discovery or a numerical proof of the contour limit.

**Inherited admissibility, contour and diagonal.** In L661, strict
increase of the real phase and its rational lower integral bound give
Y_n<27/100; n=6q+3 makes the endpoint phase exactly pi*(q+1/2).
The factors in S with positive parameters have modulus strictly below
one in the upper half-plane and above one in the lower half-plane. Thus the only
kernel poles in the rectangle are the simple real nodes, each with
residue one. The inequality Re(x+i*y)<=-9/8 excludes every possible
pole x+i*y=t_j*u of W there. This checks the full finite contour used
in (19), without dropping an alias or assuming an infinite census.

The single-factor quadratic used for L661's diagonal has leading
coefficient L*D_0-t^2*N_0>0; its discriminant condition is exactly
the quartic (7) of that lemma. This was checked against the factor
formula in L659, including the conjugation used only in a modulus
identity. Each rational majorant therefore applies to every real
vertical displacement. The holomorphic function T_a(w) has no pole
for |w|<=1, so the maximum modulus extension to smaller radii is
legitimate. At t_0=0 its modulus is |x/a|<=1. Counting at most
n/128+1 grid points in each remaining radial bin and keeping all
original squared residues proves the asserted diagonal envelope.
For this census sum r_a^2=n/3, not (n/3)^2. Independently integrating
the decreasing function (d+t)^(-2) gives the endpoint lower bound
exp(-81n/6250-729/31250), which is stronger than the bound used here.

**Moving edges and the complex limit.** The derivative in (7) has
the displayed numerator; A^+-b^+ is decreasing since its derivative
is -1/(d+t)^2-U/(U+d*t)^2. Consequently (8)--(9) hold on the full
rectangle. For the phase factors the squared denominator in (10)
is positive, and 4*A*s divided by it is less than one, since
1-A*s>=1/2. The endpoint minimum calculation therefore proves (11)
on the whole edge, not only at s=0. The split at |s|=1/(100n)
gives (13) with constants independent of n; its small central segment
uses the exact phase -1, and the other segments use modulus gaps.

After division by w_n(Y_n), the complete right-edge integrands have
majorants C exp(-3t/25) for t>=0 and C exp(-|t|/5) for t<=0.
These bounds include their dy factor and K_n/n. Extension by zero
outside [-n/8,n/8] supplies a single integrable majorant on R.
Uniform Riemann-sum convergence on the compact real interval gives
Y_n->Y>0 and the limits of both logarithmic derivatives. The uniform
second-derivative bounds justify the local Taylor expansions on each
fixed t interval. Dominated convergence in (17) thus controls the
entire moving edge. The horizontal contribution divided by the
endpoint amplitude is O(n exp(-51n/25000)), hence tends to zero.

For z=-i*p/(2v), Re z=Im p/(2v)>0 and Re z<=5/6<1; the upper
bound uses Im p<=1 and 2v>=6/5. The integral in (18) converges at
both ends. In its auxiliary rectangle the only pole is i*pi, the
residue is exp(-i*pi*z), and the upper horizontal multiplier is
-exp(-2pi*i*z). These signs give pi/sin(pi*z), which cannot vanish.
No convergence of the oscillating phase w_n(Y_n)/|w_n(Y_n)| is needed.

**Reflected edge and recovery of both components.** Parameterize the
right edge by y=Y_n+i*s with s increasing. Reflection y->-conjugate(y)
traverses the left edge upwards, whereas the positive contour traverses
it downwards. Together with K(-conjugate(y))=-conjugate(K(y)), this
gives the left integral -conjugate(J_(k,n)). Thus (19) has the stated
sign and factor 1/(pi*R). On writing V_n=A_n+i*B_n, the leading real
matrix from (A_n,B_n) to (c_0,c_1) is

    [[0, 1/(pi*R)], [Y_n/(pi*R^2), x/(pi*R^2)]].

Its determinant is -Y_n/(pi^2*R^3), bounded away from zero eventually.
Both errors are o(|w_n(Y_n)|); inversion and |V_n|=|J|*|w_n(Y_n)|
therefore give a fixed positive lower constant in (2). Individual
coefficient zeros and endpoint phase oscillations do not affect it.

**All roots, integrability and localization.** The coefficient estimate
in section 5 follows from the full factorization of G(1,.), even at
degree drops: each first-coefficient root product is bounded by the
product of all max(1,|alpha|), with at most M-1 summands. It does not
replace G by its first two terms. For L658's localization, the rational
clearing and slice arguments in L657 were checked: spatial nonvanishing
uses N<=M and Lagrange interpolation; angular nonvanishing uses the
unique exterior pole a/t_j, whose nonzero coefficient is
r_a*H_M(a*zeta/R)/R. The named polynomial logarithmic-integrability
input thus applies to the nonzero full numerator. Subtracting the
bounded denominator logarithm justifies all Fubini steps.

L658's disk change of variables has Jacobian P_s, and its numerator
constants obey |A|^2-|B|^2=(1-s^2)(1-|gamma|^2)>=0, including boundary
roots. Hence every numerator root is charged with (log s)/2. Every
denominator reflected root has modulus <4/5 and costs at most 4(1-s).
Upper semicontinuity gives a maximizing angle, and nonnegativity of
H-m on the entire circle justifies restricting its Poisson integral
to the centered arc. With h=pi/n^2, s=1-h and d_ang<=n^2/3, this
proves the exact loss 16pi^2/9, with normalized arc length n^(-2).
This validates the whole localization input needed here; it does not
assume that a diagonal-maximizing angle also maximizes m.

The final subtraction uses an upper bound on D and lower bounds on
H and the arc mean. The linear rate is exactly
1/16-2*(91/5000)-2*(81/6250)=9/50000; the logarithmic loss is 5log n.
All constants are absolute for this one census and all sufficiently
large n in the indicated congruence class. The number 1210 establishes
admissibility only; it is not the onset of the asymptotic signed bound.

**Arithmetic replay and remaining scope.** The existing replay program
was read and rerun: all 128 quartic identities, 581 full-cover cells,
2905 strictly positive Bernstein coefficients and 128 arctangent rows
passed. Its exact rate is 13916666837251/768000000000000<91/5000;
its phase lower bound is 33735471548097/64000000000000>11/21.
The 15 L662 rational checks were also read and rerun. Complete selected
summary/comparison values, all 15 actual/required checks and both empty
failure lists were inspected from the certificates named above; the
large certificate was checked in full by the replay, not by a preview.
These computations verify arithmetic only. The analytic conclusions
come from the preceding audit. Source manuscript proofs, other claims
in L657/L659/L661, general support, Xi transfer and all-degree signs
are outside this audit. The standard cited inputs and recorded Mathlib
qualifications remain unchanged.

## Mathlib

The reused assessment inspected the supporting univariate
[MahlerMeasure module](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure`, and
`Polynomial.norm_coeff_le_choose_mul_mahlerMeasure`. The finite analytic
logarithmic mean here is for a nonzero polynomial; Lean's totalized
logarithm at zero does not replace that hypothesis. Full matching
coverage for the signed moving-contour limit, complex multiplier,
endpoint-pair estimate and paid-arc comparison has not been checked.
The rational check is not a Lean formalization; unknown coverage is
not evidence of absence.
