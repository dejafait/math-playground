# Lemma 445: fixed-height regularity of the complete conditional x-second

## Hypotheses

Use exactly L443's complete conditional law on its eventual real-H ray,
including L438's high and two signed intermediate components, original
L429 cutoff j(H), all probability losses, translation m and constant
covariance correction A_H. The L441/L443 subsequent covariance changes
have zero 11 entry. Fix a sufficiently large real H and put
ell=log H, I=[H,2H], L(t)=log(2+t), T(t)=1+t.

The exact actual functions are those of L366/L417:
F=F_0, G, the positive envelope A,
X0=(f,f'/L,f''/L^2), f=F/A, and
v_j=(G/A)^(j)/(T^2 L^j), j=0,1,2. Derivatives precede division.
Use L419's curvature e=(log A)''/L^2 and exact forms

    ell_F(X;t)=y^2-xz-e x^2,
    C=v_1^2-v_0 v_2-e v_0^2,
    b=(-v_2-2e v_0,2v_1,-v_0), B=b^T X,
    D=B^2-4C ell_F=X^T J X.

Keep the precise L421 positive-direction tie rule and final reversal,
and the L437 negative direction. All their proved denominator margins
hold after a common onset. No temporal regularity of individual selected
bulk atoms, inter-H consistency, actual sine limit, or realization is
assumed. Parameters defined by height integrals are held fixed as t varies.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-complete-x-second-weak-regularity.md`.
This is a REPRODUCTION by branch algebra and known one-dimensional
calculus; it claims no new general regularity theorem or originality.

## Conclusion

For every sufficiently large real H, the specified complete raw density

    q_H(t)=integral x^2 dnu_(H,t)(X)

is Lipschitz on [H,2H], with a finite constant allowed to depend on H.
In particular it is locally absolutely continuous on (H,2H). This
holds for its actual pointwise definition, including all zero, max,
projection-tie and calibration-zero conventions; no exceptional-point
replacement is needed. Its weak derivative is locally integrable and
has no singular part.

The separate step-279 critical audit below validates this result. It closes only the
singular-variation obstruction for this unchanged entry. It supplies no
derivative bound uniform in H, mean compatibility, positive covariance
repair, other occupation identity or actual/global realization. It
does not alter L444's audited lower bound on bounded zero-11 repairs,
evaluate actual clipping, establish capped nondegeneracy or L413's
full-error margin, or address global mixed positivity or RH.

## Proof

### Fixed-height smooth inputs and the calculus used

L366 (1) writes F(t)=2 xi_c(1/2+it) and
G(t)=-(t^2+1/4) Re[xi_c(5/2+it)/(5/2+it)], where xi_c is entire.
Thus both are smooth real functions on an open neighborhood of I.
The same lemma defines
A=(t^2+1/4)|Gamma(1/4+it/2)| pi^(-1/4).
The gamma function has no pole or zero on this line, so A is smooth
and strictly positive. Hence X0,v,e,C,b,J are smooth, by their exact
formulas above, with no division by a critical-line zeta value.

For the negative direction L437 uses a+ih=R zeta(5/2+it),
R=Q/A and Q=(t^2+1/4)Gamma(1/4+it/2)pi^(-1/4-it/2).
These functions are smooth too. The scalar d_H, matrix A_H,
calibration vector a_H, normalizations N_H,W_H and finite integer
j(H) are constants in this proof, even if not smooth in H.
By L440 (16), L438's calibration

    F_H(theta)=beta W_3(theta)+a_H^T(1,cos theta_2,P(theta)),
    theta(t)=(t log 2,t log 3,t log 5),

is smooth in t: W_3 is smooth on its torus and P is one fixed finite
trigonometric polynomial. Define F_+=(F_H(theta(t)))_+ and
F_-=(F_H(theta(t)))_-. Both are Lipschitz on I.

Here and below a smooth function on a neighborhood of I is Lipschitz
on I by its bounded first derivative and the mean-value theorem.
For completeness the nonsmooth operations needed satisfy

    ||a|-|b||<=|a-b|,
    |max(a,b)-max(c,d)|<=max(|a-c|,|b-d|).

Positive/negative parts therefore preserve Lipschitz regularity.
Products of bounded Lipschitz functions are Lipschitz, since
|fg(t)-fg(s)|<=||f||_infinity |g(t)-g(s)|
+||g||_infinity |f(t)-f(s)|. Reciprocation does so when the absolute
denominator is at least delta>0, by
|1/a-1/b|<=|a-b|/delta^2. These elementary inequalities are given to
check the specific branch operations, not to reprove a general
Sobolev theorem. Bounds here are at fixed H.

### The high component, including rho0=0 and the scale boundary

Write u=|X0|^2, x0=(X0)_1, and

    V=max(ell^6,sqrt(2) u)=r^2.

This is an everywhere positive Lipschitz function, including the exact
boundary between L421's two scale choices. For u>0 that lemma gives
p=(rho0/r)^4 and Y=s r X0/rho0, s in {1,-1}. Consequently

    p=u^2/V^2,
    pYY^T=(u/V) X0 X0^T,
    pY_1^2=u x0^2/V.                                  (1)

At u=0 the right sides vanish and equal exactly the prescribed p=0,
Y=0 convention. They are Lipschitz on all of I, since u,X0 are smooth
and V>=ell^6>0. The possibly discontinuous reversal s cancels from
the whole raw second matrix and from p. No assertion about the first
moment pY or the regularity of Y is required: its height integral,
used later in d_H, is a fixed parameter.

### The positive intermediate: both selections and their tie values

To avoid confusion with the signed labels of L438, call L421's two
unoriented positive candidates

    c_1=(2/3,1/3,2/3), c_2=(2/3,-1/3,2/3).

They satisfy exactly, not just at leading response order,

    (c_i)_1^2=4/9,
    ell_F(c_i;t)=E_*(t):=-1/3-4e(t)/9, i=1,2.

Set M=max(|b^T c_1|,|b^T c_2|). It is Lipschitz, and L421's
uniform projection bound gives M>=b1>0 on the eventual ray.
The prescribed rule chooses the larger absolute projection (c_1 at
equality), then reverses the chosen vector to make B positive.
Thus the resulting L438 direction n_+ satisfies at every t

    B(n_+;t)=M,
    D(n_+;t)=M^2-4C E_*,
    h_+=(M^2-4C E_*)M,
    (n_+)_1^2=4/9.                                    (2)

These identities include equality of opposite-signed projections as
well as equality of same-signed projections. The selected projection
is never zero because M>=b1. Both its reversal and its c_1/c_2 tie
choice disappear from (2). L421 supplies h_+>=h_min>0; alternatively
E_*<=-1/4 and C>=C_min give it directly together with M>=b1.
It follows that h_+ and 1/h_+ are Lipschitz on I, even where n_+
itself changes discontinuously.

Using R_mid=ell^(3/2), L438 (10) consequently gives the pointwise
Lipschitz expressions

    k_+=ell^(-5/2) F_+/h_+,
    k_+(Z_+)_1^2=sqrt(ell) (4/9) F_+/h_+.            (3)

At a zero of F_H these formulas equal the specified zero mass and
zero raw second contribution. In particular regularity of k_+,
which also enters the remaining bulk mass, has been checked separately
from regularity of its raw second contribution.

### The negative intermediate and all remaining terms

The exact negative direction of L437 is n_-=U/|U|, where

    U=(a+h,(a-h)/2,-(a+h)/4),
    |U|^2>=(a^2+h^2)/2>=zeta(5/2)^(-2)/2>0.

Thus n_- is smooth on I, with no response-projection division or tie.
Its exact h_-=-D(n_-;t)B(n_-;t) is smooth and bounded below by
L437's strictly positive h_-min. Hence

    k_-=ell^(-5/2) F_-/h_-,
    k_-(Z_-)_1^2=sqrt(ell) F_- (n_-)_1^2/h_-          (4)

are Lipschitz, including every zero of F_H.
Equations (1), (3), (4) imply that the full remaining probability

    w=1-u^2/V^2-ell^(-5/2)(F_+/h_++F_-/h_-)           (5)

is Lipschitz. L438 gives w>=1/4 and W_H=E_H w>0.
The original stage j(H) is finite, and L429 defines

    P_j(t)=product_(p<=p_j)(1-1/p)/|1-p^(-1/2-it)|^2.

Each denominator is at least (1-p^(-1/2))^2>0, so P_j is smooth
on I. N_H=E_H(wP_j)>0 is constant in t, and g_H=P_j/N_H is smooth.
No derivative of the stepwise cutoff in H is taken.

Retain the complete L438 (14) definitions

    d_H=(-b0-J_R)/W_H,
    m=d_H b/|b|^2,
    A_H=-(Q+E_H[wmm^T])/W_H.

The rare integrals J_R,Q are finite by L438 (9)--(12).
They can involve nonsmooth signed first moments without affecting
their status as constants in t. L419 gives |b|>=b_min>0, so m is
smooth. In particular m_1^2=d_H^2 b_1^2/|b|^4 is smooth, while
(A_H)_11 is a finite constant. Neither contribution is dropped.

The later L441/L443 fields have zero 11 entry. L443 (1), with
K_11=1, therefore gives the following single exact formula for the
complete raw density at every t in I:

    q_H=u x0^2/V
        +sqrt(ell)[(4/9)F_+/h_++F_- (n_-)_1^2/h_-]
        +w[ell P_j/N_H+(A_H)_11+d_H^2 b_1^2/|b|^4].   (6)

Every factor in (6) is bounded and Lipschitz on I by the preceding
arguments. Thus q_H is Lipschitz on I. This formula explicitly
retains the high contribution, both signed masses, the mass loss in
w, the normalization, the full constant covariance correction and the
translation. It bypasses both bulk atom/basis selection stages using
their exact raw covariance, as permitted by L443 (1).

### Absolute continuity and the representative distinction

If C_H is a Lipschitz constant furnished by (6), every finite disjoint
collection of intervals (a_i,b_i) in I satisfies

    sum_i |q_H(b_i)-q_H(a_i)|<=C_H sum_i(b_i-a_i).

This proves absolute continuity directly by its definition (with the
constant-function case immediate). Import the standard integral/weak
derivative characterization from J. K. Hunter, *Notes on Partial
Differential Equations*, revision 2014-06-18,
[Theorems 3.60, 3.62--3.63, printed pp. 77--80](https://math.ucdavis.edu/~hunter/pdes/pde_notes.pdf).
For an AC function on a compact interval its a.e. derivative is
integrable and reconstructs the function, and integration by parts
identifies that derivative with its distributional derivative on the
interior. These hypotheses now hold on I, hence also on every compact
subinterval of (H,2H). There is no jump or singular-continuous part.
No general characterization is reproved here; the explicit interval
inequality only verifies its law-specific hypothesis.

Crucially (1)--(6) were pointwise identities across every branch, so
the specified q_H itself is the AC representative. Possible jumps of
selected atoms, or values assigned at their ties, have not been ignored
by an a.e. argument. No uniform bound on C_H has been established.
In particular fixed-H Lipschitz regularity is consistent with L444's
required correction norms growing at least as sqrt(log H). The
all-temporal covariance feasibility question is not decided.

### Separate critical audit — 2026-10-20, step 279

The unchanged prior SPECIALIZE assessment is
`drafts/literature/2026-10-20-complete-x-second-regularity-audit.md`.
This audit independently compares (1)--(6) with the original law
definitions; it does not assume those identities as extra hypotheses.
It reuses the inspected Hunter calculus statements with their
representative qualifications. The result is a REPRODUCTION and local
critical validation, not a new general theorem or a novelty claim.

**Actual inputs and fixed parameters.** L366 (1) gives exactly the F,G
formulas used above and its hypotheses give Q and A=|Q|. On a neighborhood
of the fixed positive compact interval the entire completion, the
nonzero gamma factor and the divisor 5/2+it are smooth and have no
singularities. Thus forming f=F/A and then its derivatives, as prescribed
in L417, gives the claimed smooth X0 and v. The exact L419 coefficient
formulas then give smooth e,b,C,J. No asymptotic response is substituted
in these definitions. The negative direction uses the same smooth
R=Q/A and right-line zeta value. L440 (16) checks smoothness of W_3
on the whole torus, including the locations of its rational poles,
and of the finite polynomial P. L438 (6) makes a_H a parameter
depending only on H; its sign-split calibration is therefore Lipschitz
in t even at calibration zeros. L429's thresholds tend to infinity,
so j(H) is finite at every fixed H. Neither it nor any defining height
integral is differentiated in this argument.

**High branches.** Independently squaring L421's scale gives
r^2=max(ell^6,sqrt(2)|X0|^2)=V. For u>0 its probability and atom give
p=u^2/V^2 and pYY^T=(u/V)X0X0^T, without dependence on its sign
choice. At u=0 both expressions are exactly zero and equal L421's
assigned p=0,Y=0 values. At sqrt(2)u=ell^6 both scale definitions
agree. V>=ell^6>0 therefore establishes Lipschitz regularity of
the mass as well as the whole raw second matrix. The sign-dependent
first moment is used only in the finite constant J_R; no temporal
regularity of that first moment is asserted or required.

**Positive branches.** Substitution of each of L421's original unit
candidates gives y^2-xz=1/9-4/9=-1/3 and x^2=4/9.
Their exact ell_F values are consequently identical E_*.
After the prescribed larger-absolute-projection choice and sign
reversal, B equals M and D equals M^2-4CE_* at every point.
The exact lower bound M>=b1>0 excludes a selected zero projection.
At a tie, including opposite signs of the candidate projections,
both expressions and x^2 agree. Thus h_+ in (2) is indeed the
selected exact DB, not merely a continuous substitute for it.
Since E_*<=-1/4 and C>=Cmin eventually,
h_+>=(b1^2+Cmin)b1>0. The operations maximum, absolute value,
products and reciprocation are therefore valid on the whole compact
interval. Multiplying the probability
ell^2 F_+/(ell^(9/2)h_+) by the atom's x-square
ell^3(4/9) checks both powers in (3), separately from the mass.

**Negative branches and probabilities.** From L437 (3),
|U|^2=(17/16)(a+h)^2+(1/4)(a-h)^2
is at least ((a+h)^2+(a-h)^2)/4=(a^2+h^2)/2.
The recorded right-line lower bound makes this strictly positive;
the square root and normalization therefore preserve smoothness.
L437 (4) supplies the positive exact h_- margin, with the curvature
and response errors already retained. Its probability and raw
x-second are precisely (4), with the same ell powers as the positive
component and the unreversed direction U/|U|. Both masses vanish
exactly when F_H=0. This validates (5) at all calibration and
projection boundaries, not only almost everywhere. L438 (12)
supplies w>=1/4. Every finite Poisson factor has positive denominator,
so N_H=E_H(wP_j)>0, and W_H=E_H w>=1/4. Their reciprocals introduce
no fixed-H singularity.

**Complete bulk entry and representative.** L438 (14), rather than
L419's earlier two-entry correction, defines the constant A_H here.
Its Q includes all three rare components and its w includes all
their probability loss. The bound |b|>=b_min gives a smooth
m=d_H b/|b|^2; its first coordinate squared is exactly the last
term in (6). L443 (1), (6), (16) keep these data and alter only
off-diagonal centered covariance entries. For every selected
orthonormal basis, including L419's equality branches, the paired
atoms m+/-sqrt(3)S u_i have mean m and raw second
mm^T+sum_i S u_i u_i^T S=mm^T+S^2.
Thus no basis choice changes entry 11. Since K_11=1, their
weighted contribution is exactly
w[ell P_j/N_H+(A_H)_11+m_1^2], proving (6) for the specified
pointwise law. The paired cross terms cancel before any regularity
claim; no bulk atom is differentiated.

All factors of (6) are bounded Lipschitz functions at fixed H.
The explicit product and reciprocal inequalities in the proof therefore
give a finite Lipschitz constant on the closed interval. Hunter's
Theorems 3.60 and 3.62--3.63 apply to this AC function itself,
so its distributional derivative on the interior is its integrable
a.e. derivative. Pointwise branch agreement, not the source's
existence of an a.e. representative alone, supplies the representative
claim. There is no hidden jump, singular-continuous derivative,
division by an actual critical zero, or interchange of H and t limits.

The audit passes without changing a coefficient, hypothesis, proof
argument or direct mathematical input. The singular-variation
obstruction for this unchanged entry is closed. Fixed-H regularity
does not give uniform derivative bounds, exact integrated cross-moment
compatibility or a positive covariance repair. In particular L444's
bounded-repair obstruction, L443's finite compatibility and all stated
global limitations remain unchanged.

## Mathlib

Full matching coverage of this selected-law regularity statement has
not been checked. No absence claim is made. The proof uses elementary
real-function Lipschitz calculus and Hunter's precisely cited AC/weak
derivative characterization; no Mathlib theorem name or formalization
of the conditional law is asserted.
