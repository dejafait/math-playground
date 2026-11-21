# Lemma 690: complete full-circle charge for a common displacement

## Hypotheses

Use exactly L666's family and conventions. In particular

    q>=1 integer, n=12q+3, M=4q+1=n/3, h=27/(10n),
    x=-d=-5/4, R=11/8, U=R^2=121/64, t_j=j/n (0<=j<n).

Specialize the permitted independent displacements to one common real
number alpha, |alpha|<=1/8:

    Z={x} union {x+i*h*(m+1/2+alpha): -2q<=m<2q}.

All original residues are one. The same poles are used at every angle.
Keep the entire product, including j=0, and the denominator angle 1/u:

    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    T_M(v)=sum_(0<=k<M) v^k,
    G(u,zeta)=R^(-1) sum_(a in Z) W_a(u)*T_M(a*zeta/R),
    D=mean_u sum_(a in Z) |W_a(u)|^2/(U-|a|^2),
    m(u)=mean_zeta log|G(u,zeta)|, A_n=mean_u m(u).

Both circle means are normalized. D is the original squared-residue
diagonal. Use L657's exact K,Q,m_0,Z_n,P_n, with all numerator roots,
multiplicities, cancellations and denominator factors retained. Z_n
here is the angular zero charge, not the pole set Z.

## Conclusion

This is an admissible one-parameter subfamily of L666. Uniformly in
alpha and both unit-circle variables, for every n in this sequence,

    |G(u,zeta)-R^(-1)T_M(x*zeta/R)|
                                  <=n^2*exp(22-n/500).       (1)

Set epsilon_n=64*n^2*exp(22-n/500). For n>=30000 in the sequence,
epsilon_n<1 and

    sup_u |m(u)+log R| <= epsilon_n,
    |m_0+Z_n-P_n+log R|=|A_n+log R|<=epsilon_n -> 0.          (2)

In particular, the complete weighted angular compensation is

    Z_n-P_n=-m_0-log R+O(epsilon_n)
           =-log M+O(1),                                  (3)

with constants uniform in alpha and n>=30000. The first O term has
absolute value at most epsilon_n. No subset of roots is substituted
for the charge in (2)--(3).

Writing sigma^2=137/5000 and

    C=8+2log R-log(3*sigma^2),

the exact full-circle test has a positive margin for the same n>=30000:

    2(m_0+Z_n-P_n)-log D+n/16
                         >=(261/10000)*n-log n-C.           (4)

Thus the rate-1/16 full-circle bound holds on this subfamily, with
an absolute constant and onset. This rules out a common-displacement
countersequence to that bound. It does not control independently
varying e_m, establish the full-cube bound, or resolve H/support,
actual-Xi realization or signs. L663's different integer-lattice
countersequence and all prior norm/clearing/Taylor stops are preserved.

This is a family-specific specialization and a new local extraction
from inspected contour evidence, not a reproof of Jensen or a claimed
new general theorem. Section 7's separate conceptual audit accepts
this restricted specialization. The interval replay below reuses L663's
previously audited backend, not an independent arithmetic backend.

## Proof

### 1. Scope, literature inputs and admissibility

The invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-spatially-averaged-angular-zero-charge.md`
covers the exact full-circle target and testing a tractable L666
subfamily. L663's old census and the recorded full-circle, relaxed
angular propagation, clearing and Taylor failures were compared first.
The common shift is inside the approved cube; no symmetry is required,
and alpha may depend on n. A prescribed subfamily result is only a
partial answer to the uniform target.

Use L657's exact clearing, nonzero-slice and integrability conclusions
to identify A_n with m_0+Z_n-P_n. Its primary logarithmic inputs are
F. Brunault and W. Zudilin, *Many Variations of Mahler Measures*, ISBN
9781108794459, [Proposition 1.4, pp.6--7](https://assets.cambridge.org/97811087/94459/excerpt/9781108794459_excerpt.pdf),
including boundary roots, and Z. Issa and M. Lalin, *A generalization
of a theorem of Boyd and Lawton*, [arXiv:1203.5379v1, Remark 3.8 and
Theorem 4.1/proof, printed p.7](https://arxiv.org/pdf/1203.5379v1), s=1.
These known theorems are imported, not reproved or strengthened.

The finite-contour input, already inspected for L663, is the residue
theorem with the simple-pole rule and the contour absolute-value bound:
J. H. Mathews and R. W. Howell, *Complex Analysis*, online edition,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
and [Section 6.2, Theorems 6.2.18--6.2.19](https://complexanalysis.org/web/sec_contour-integrals.html).
The altered kernel, moving contour, explicit anchor and new pointwise
extraction below are necessary because L663's stated integer-lattice
result does not apply to L666's census. The source manuscripts are not
independently audited here.

Admissibility follows from L666, or directly: nonanchor heights are
distinct, have distance at least 3h/8 from zero, and absolute value
at most h*(2q-3/8)<9/20. Hence there are exactly M unit residues,
the anchor is included, and

    |a|^2<(5/4)^2+(9/20)^2=353/200<(273/200)^2.

This verifies L657's hypotheses and the positive denominators in D.

### 2. Uniform extraction from the complete L663 contour evidence

Use the fixed, positively oriented rectangle Gamma in the complex
y-plane given by |Re y|<=Y=9/20 and -b<=Im y<=c, where
b=2/25, c=1/8. Put lambda=20*pi/27. For u=exp(i theta) and
a=x-v+i*s with y=s+i*v on Gamma, define precisely as in L663

    f(t,u,a)=log|(x-t*u)/(a-t*u)|
                  +log|(U*u-t*a)/(U*u-t*x)|,
    beta(a)=(1/3)log max(1,|a|/R),
    F(theta,s,v)=integral_0^1 f(t,u,x-v+i*s)dt
                         -lambda*(-v)_+ +beta(x-v+i*s),
    B(theta)=max_((s,v) in Gamma) F(theta,s,v).

These expressions are finite: e=d+v is between e_0=117/100 and R,
and |a|<=sqrt(R^2+Y^2)<29/20<U. L663 Sections 3--5 and its
Section 7 audit establish the following specific inputs, which are
unchanged functions of the fixed rectangle and not of its old census:

- |partial_t f|<16, |partial_t^2 f|<70, and
  |partial_theta^2 f|<100 throughout the rectangle and 0<=t<=1.
- On the fixed vertical sides, the derivative of integral f with
  respect to e is <=-3/10 for d<=e<=R and >=-9/4 for e_0<=e<=d.
  With beta and the kernel decay included, the side maximum is at e=d.
- The four complete edge upper bounds at theta_k=k*pi/512,
  0<=k<=512, are recorded in the original certificate's
  `angular_rows`. Each includes its 128-cell t quadrature error
  70/(12*128^2); the upper edge includes its spatial cost, and the
  lower edge includes the kernel decay. No edge or spatial term is
  dropped.

The new step is a pointwise, rather than averaged, use of these rows.
For fixed (s,v), F(theta,s,v)+50*theta^2 is convex. Therefore the
maximum B(theta)+50*theta^2 is convex too. On any interval of length
delta, subtraction of this quadratic gives

    B(theta)<=chord_B(theta)
                  +50*(theta-left)*(right-theta)
              <=max(B(left),B(right))+100*delta^2/8.       (5)

This is valid even where the maximizing edge changes. Conjugation
with s replaced by -s makes B even, so [0,pi] covers the full circle.
Using all 513 row maxima and delta=pi/512 yields the exact bound

    B(theta) <= -1319516391354837085/590295810358705651712
             < -1/500,                                  (6)

uniformly in theta. The angular error is the pointwise /8 error in
(5), not L663's integrated /12 error. Section 6 below records the
complete replay and exact strict comparison. In particular (6) is
not an inference from a sampled maximum or from a negative average.

### 3. The changed kernel and every pole of the moving rectangle

Set Y_n=2q*h=Y-27/(20n) and let Gamma_n be the positively oriented
boundary of [-Y_n,Y_n]+i[-b,c]. The half-shifted kernel is

    K_alpha,n(y)=-i*lambda*n
                      /(exp(i*lambda*n*y-2*pi*i*alpha)+1).  (7)

The only zeros of its denominator are real and occur at
y=h*(m+1/2+alpha). At each zero the derivative of the denominator
is -i*lambda*n, so every residue is one. In -Y_n<y<Y_n these
are exactly -2q<=m<2q. Since |alpha|<=1/8, each extreme pole
and each first excluded pole has distance at least 3h/8 from the
corresponding vertical boundary. There is no pole at the anchor or
on any boundary. The fixed old boundary Y would not be valid at
alpha=0; the moving boundary is essential.

For y in the entire closed rectangle, a=x+i*y has Re a<=-e_0<-1
and |a|<29/20<U. Thus W_a(u) is holomorphic on a neighborhood of
that rectangle: a=t_j*u is impossible and its fixed denominators
U-t_j*x/u are nonzero. Its numerator factors are also nonzero there.
The polynomial T_M(a*zeta/R) introduces no pole. The residue theorem
therefore gives, for every pair of unit-circle variables, the exact
identity with the extra anchor separated:

    G(u,zeta)=R^(-1)T_M(x*zeta/R)
      +(1/(2*pi*i*R)) integral_(Gamma_n)
          W_(x+i*y)(u)*K_alpha,n(y)*T_M((x+i*y)*zeta/R)dy. (8)

All M spatial moments occur in this identity.

On either horizontal edge, the reverse triangle inequality bounds
the denominator of (7) below by |1-exp(-lambda*n*v)|.
Since n>=15 and lambda*5*b>log 2 (as verified in L663), both edges
obey

    |K_alpha,n(s+i*v)|
             <=2*lambda*n*exp(-lambda*n*(-v)_+).          (9)

On a vertical edge lambda*n*s=+/-4*pi*q. The denominator there
is 1+r*exp(-2*pi*i*alpha), where r=exp(-lambda*n*v)>0.
Its squared modulus is 1+r^2+2r*cos(2*pi*alpha)>=max(1,r^2),
because |alpha|<=1/8 implies cos(2*pi*alpha)>=0. This proves
(9) on the entire vertical edges too, even without its factor 2.
No symmetry of the displaced pole set is used.

### 4. Paying for the moving sides and the full spatial polynomial

Let B_n(theta) be the same maximum of F, now over Gamma_n. Its
horizontal edges are subsets of the old horizontal edges. To compare
a moving side with its old side, hold v fixed and move s over the
distance Delta_n=Y-Y_n=27/(20n). Throughout that path, the two
logarithms involving a give the ordinate derivative bound

    |partial_s f|<=1/(e_0-1)+1/(U-29/20).

The beta term is Lipschitz with constant at most 1/(3e_0): on its
positive part its derivative has modulus |s|/(3|a|^2)<=1/(3e_0),
and on its zero part the derivative is zero. Continuity at the
transition retains this Lipschitz bound. The kernel decay is
independent of s. Thus

    |F(theta,s,v)-F(theta,s',v)|
      <=[100/17+320/141+100/351]*|s-s'|<10*|s-s'|,
    B_n(theta)<=B(theta)+27/(2n)<=-1/500+27/(2n).          (10)

The exact finite product satisfies

    log|W_a(u)|=sum_(0<=j<n) f(j/n,u,a)
                         <=n*integral_0^1 f(t,u,a)dt+8,   (11)

by the derivative bound 16 and the left-sum error. This includes
the j=0 factor x/a. On the entire contour, including |a|>R on
parts of the upper edge, the complete spatial polynomial obeys

    |T_M(a*zeta/R)|<=M*max(1,|a|/R)^(M-1)
                                   <=M*exp(n*beta(a)).   (12)

The contour length is at most 221/100. Equations (8)--(12) give

    |G-R^(-1)T_M(x*zeta/R)|
      <=[(221/100)*lambda/(3*pi*R)]
                             *n^2*exp(8+27/2-n/500).

The prefactor is 1768/4455<1 and 8+27/2=43/2<22. This proves
(1), with constants independent of alpha, n, u and zeta. It uses
the exact signed sum before the absolute contour bound, and the
bound is on the complete polynomial, not a selected coefficient.

### 5. Anchor comparison, complete charge and original D

Let A_M(zeta)=R^(-1)T_M(x*zeta/R), and put r=d/R=10/11. On
|zeta|=1 the geometric identity gives

    |A_M(zeta)|>=(1-r^M)/(R*(1+r))>=8/231>1/32.          (13)

All zeros of T_M(x*zeta/R) have modulus 11/10>1, and its constant
coefficient is one. The imported complete root formula therefore
gives mean_zeta log|A_M(zeta)|=-log R. This retains its degree
and leading factor; it is not a constant-coefficient substitution
for the unrelated full polynomial G.

The function n^2*exp(22-n/500) decreases for real n>1000.
At n=30000 it is 30000^2*exp(-38), which is strictly less than

    30000^2/2^38=3515625/1073741824<1/64,

using exp(1)>2. Thus (1) and (13) give |G/A_M-1|<1/2 uniformly
for every permitted n>=30000. In particular there are no torus
zeros at those n. For |z-1|<=delta<=1/2, the real bounds
1-delta<=|z|<=1+delta give |log|z||<=2delta. Applying this with
delta=32*n^2*exp(22-n/500) proves

    |log|G(u,zeta)|-log|A_M(zeta)||<=epsilon_n.

Integration first in zeta and then in u proves (2). L657's exact
identity identifies this full two-circle mean with m_0+Z_n-P_n.
Its nonzero slices and absolute logarithmic integrability are already
applicable at every permitted n; no zero/pole is removed in passing
to the large-n nonvanishing comparison. In particular cancellations
with Q still contribute to Z_n exactly as in L657.

L657 also bounds m_0-log M above and below by absolute constants.
Subtracting m_0+log R from (2) proves both assertions of (3), with
uniform constants. This is control of the complete weighted charge,
not just its sign or an unweighted number of zeros.

Finally L661's audited general envelope, with kappa=91/5000 and
sigma^2=137/5000, applies to this admissible unit-residue family:

    D<=sigma^(-2)*exp(2*kappa*n+6)*M.

Together with A_n>=-log R-1 and M=n/3, it implies

    2A_n-log D+n/16
      >=(1/16-2*kappa)*n-log n
                                 -[8+2log R-log(3*sigma^2)].

Since 1/16-2*kappa=261/10000, this is (4). Its positive linear
term supplies the full-circle criterion after a uniform onset. It
does not imply anything about the missing independent-displacement
perturbation: such perturbations have no common kernel (7), and an
absolute O(1/n) node motion is not a relative error bound for this
signed sum.

### 6. Complete certificate and verification limits

Run from the notebook:

    python3 scripts/one-sided-hankel/common-displacement-full-circle-94.py

The full new evidence is
`scripts/one-sided-hankel/common-displacement-full-circle-certificate-94.json`.
The script reuses the exact 2^-72 outward interval backend in
`scripts/one-sided-hankel/full-circle-root-compensation.py` and reads
the original certificate without changing it. L663 Section 7 already
audited that backend and replayed all its derivative computations.

For this extraction, every one of the original 8192 derivative terminal
intervals and all four complete, disjoint grid covers are inspected
against the stated thresholds; every global bound is replayed.
All 513 four-edge angular interval rows are recomputed and agree
exactly with the originals. Every edge maximum is retained, the entire
angle cover is checked, and the new pointwise chord error is charged.
Integer arithmetic gives precisely (6) and a strictly positive margin
below -1/500. These computations use no floating-point premise.

The same certificate checks the exact ordinate Lipschitz bound,
rectangle radius, moving-side and Riemann-sum costs, contour prefactor,
anchor modulus, uniform onset and the original-D rate margin. It
passes with an empty failure list. Full new angular rows, exact
comparisons, inspected derivative extrema, paths and source hashes
are saved. The initial diagnostic
`scripts/one-sided-hankel/half-shifted-full-circle-screen-94.json`
is preserved but is not a premise of the proof.

This is complete relevant terminal/coverage inspection and an angular
replay using the inherited backend. It is not an independent interval
implementation or a source-manuscript audit. The separate critical
review is in Section 7; neither step proves the whole independent cube.

### 7. Conceptual audit — 3 November 2026, step 96

The audit accepts (1)--(4), with (4)'s inherited n>=30000 range now
explicit in its statement. No bound or mathematical dependency changes.
It uses the invocation-start SPECIALIZE assessment
`drafts/literature/2026-11-03-common-displacement-full-circle-audit.md`.
This establishes a checked local input, not a new theorem beyond the
sources or an independent source-manuscript audit. The full-cube and
Xi gaps in the conclusion remain open.

**Census and analytic domain.** The identity lambda*n*h=2*pi places
all kernel zeros at real y=h*(m+1/2+alpha). The denominator derivative
at each is -i*lambda*n, giving residue one with the positive contour
orientation. The moving boundaries have ordinates +/-2q*h. The closest
included and excluded poles have distances h*(1/2+/-alpha)>=3h/8;
this covers both endpoints of the alpha interval and q=1. No integer
m makes m+1/2+alpha zero, so the anchor is absent from the kernel
census and must be added as in (8). There are 4q nonanchor poles and
one anchor, hence exactly M unit residues. In contrast, the old fixed
side has lambda*n*Y=(4q+1)*pi and would meet a pole at alpha=0.

On and inside the moving rectangle Re(a)<=-117/100<-1 and
|a|<=sqrt(R^2+Y^2)<29/20<U. Thus a=t_j*u and U*u=t_j*a
are both impossible. The fixed anchor factors are also nonzero.
W_(x+i*y) is holomorphic on a neighborhood of the closed rectangle;
T_M is polynomial. The only singularities in (8) are the enumerated
simple kernel poles. This verifies the hypotheses of the cited finite
residue theorem and ML bound. On the horizontal edges the denominator
clearance follows from exp(lambda*n*b)>2 and c>b; the inherited
global certificate checks even n>=5. On the moving sides its squared
modulus is 1+r^2+2r*cos(2*pi*alpha)>=max(1,r^2). Consequently (9)
has the correct decay sign on the lower edge and no omitted side cost.
No reflection symmetry of the shifted pole set is used.

**Pointwise continuum bound and moving sides.** The inherited fixed
rectangle estimates in L663 are independent of its pole census.
Their two vertical sides, lower edge, and upper spatial correction
are exactly the four columns replayed here. For each fixed boundary
point, F+50*theta^2 is convex; its compact maximum is convex as well.
The chord error is therefore 50*(theta-left)*(right-theta), bounded
by 100*delta^2/8 pointwise. Substituting upper bounds at both endpoints
preserves this inequality. Evenness uses the fixed rectangle's
(theta,s)->(-theta,-s) symmetry, not any symmetry of alpha. This is
why all 513 rows on [0,pi] control every angle in (6); a negative
average alone would not do so.

For either moving side, integrate the absolute s derivative on the
straight path to the corresponding fixed side. Throughout that path
the two a-dependent logarithms have derivative bound
100/17+320/141, and beta has Lipschitz constant 100/351, including
its kink. Their sum is 2366080/280449<10. The displacement is
27/(20n), so the loss in n*F is at most 27/2, uniformly in n.
Horizontal edges only shorten. The left-sum error is at most 8 and
includes t_0=0, whose exact factor is x/a. On every edge
|T_M|<=M*max(1,|a|/R)^(M-1)<=M*exp(n*beta), even where
|a|>R. With perimeter at most 221/100 the exact prefactor is
1768/4455<1 and total constant exponent is 43/2<22. Thus no
angular, spatial, j=0 or contour-motion factor is missing from (1).

**Anchor, integrability, and complete charge.** Since r=10/11<1,
|A_M|>=(1-r^M)/(R*(1+r))>=8/231>1/32. Its M-1 roots are
the nontrivial Mth roots of unity divided by x/R, all of modulus
11/10. Its constant coefficient is 1/R. The cited full root formula
therefore gives mean log|A_M|=-log R; the roots and leading factor
have not been dropped. The error E(n)=n^2*exp(22-n/500) has
logarithmic derivative 2/n-1/500<0 for n>1000. At n=30000,
E(n)<3515625/1073741824<1/64, hence epsilon_n=64E(n)<1
uniformly thereafter. The ratio satisfies |G/A_M-1|<=32E(n)<1/2,
and both sides of the real logarithm estimate give error <=64E(n).
No torus zero or logarithmic branch problem occurs in this comparison.

The audit also checked the L657 inputs actually used here: the exact
K/Q with every j=0 factor, Q's exterior and interior roots, nonzero
spatial and angular slices, Re c_0(0)>0, exceptional finite spatial
slices at u=0, and absolute logarithmic integrability. The imported
polynomial theorem supplies integrability for each finite n, without
a degree-uniform constant. Fubini then identifies A_n with the full
m_0+Z_n-P_n. Cancelled poles remain counted in both K and Q; angular
boundary roots have zero charge and integrable logarithms. L657's
two fixed m_0-log M bounds apply uniformly to the present family.
Thus (2)--(3) concern all weighted numerator zeros, not a subset or
an unweighted census. L657's unrelated local-arc estimates are not
promoted by this audit.

**Original diagonal and uniform range.** L661's general envelope
has no symmetry or spacing assumption. The current family satisfies
its radius hypothesis; U-r_*^2=137/5000 and sum r_a^2=M=n/3.
Combining that envelope with A_n>=-log R-1 gives exactly
1/16-2*(91/5000)=261/10000 and the stated constant C in (4).
This uses an upper bound for the actual D in the correct direction;
no surrogate diagonal or anchor-only replacement occurs. All constants
and the comparison onset are independent of alpha; alpha may vary with n.
Only the admissible subsequence n=12q+3 is claimed.

**Complete replay and limits.** Reproduction commands from the notebook:

    python3 scripts/one-sided-hankel/common-displacement-full-circle-94.py --output scripts/one-sided-hankel/common-displacement-full-circle-audit-96.json
    python3 scripts/one-sided-hankel/common-displacement-full-circle-audit-96.py

The first command recomputed every four-edge angular row and all global
interval constants. All 513 rows agree exactly with the originals.
It inspected all 8192 inherited derivative terminal intervals, their
thresholds, and all four complete disjoint covers. The second command
linked every terminal record to L663's prior full derivative replay,
checked source/backend hashes and all angular records, and independently
checked the rational /8 chord aggregation using the upper pi endpoint.
Both failure lists are empty. The exact uniform bound is (6), with
margin below -1/500 equal to

    17365596329678222697/73786976294838206464000 > 0.

The separate complete artifacts are
`scripts/one-sided-hankel/common-displacement-full-circle-audit-96.json`
and `scripts/one-sided-hankel/common-displacement-full-circle-audit-checks-96.json`.
The original certificate is preserved and the new replay is identical.
This step read the relevant inherited arithmetic implementation and
reused its previously audited outward rounding. It did not recompute
the derivative integrals anew or implement an independent interval
backend. Complete evidence was processed rather than inferred from
previews. The standard source results and the unchanged Mathlib
qualifications below remain the limits of this informal audit.

## Mathlib

Full matching coverage for this moving half-shift contour and its
complete two-variable charge is not checked. Reuse only the supporting
univariate coverage recorded in L657:
[Mathlib.Analysis.Polynomial.MahlerMeasure](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Polynomial/MahlerMeasure.html),
including `Polynomial.logMahlerMeasure_eq_log_leadingCoeff_add_sum_log_roots`,
`Polynomial.intervalIntegrable_mahlerMeasure` and
`Polynomial.mahlerMeasure_mul`. These are not a formalization of (1)--(4).
No new Mathlib search or absence claim is made. The cited analytic
theorems, their stated qualifications and the explicit finite bounds
above are the informal inputs.
