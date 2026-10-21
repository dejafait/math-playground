# L154 — The complete quartic residual has a nonzero cubic coefficient

## Hypotheses

Keep L152 and L153's exact SU(2) quartic residual, all three colors,
both signed insertion subtractions, direction-1 straight lower-rooted
forest, all-face relative box D=(-4,4)^4, a=8/N through admitted even
meshes, actual L010 probes i=3,6 and tau=1/16. The bare small-coupling
coefficient is taken at fixed mesh before refinement. Use exactly
L008's compact divergence-free displacement, including both sectors
and their transition region. Retain every heat mode and the constant
axial prefix. This evaluates L152's already-established limit; it
does not prove a new interchange of mesh and coupling limits.

Import L132(1)'s full physical forms P_(i,D),P_(i,X),P_(i,A),P_(i,C)
and L145(1)'s B_(i,R), with their stated absolute convergence.
Numerical premises are L133's complete physical intervals and L146's
complete B_R intervals, with the inherited L039 IEEE binary64
addition/multiplication/FMA, no-overflow and underflow qualifications.
Those heat enclosures are informal computer-assisted inclusions,
not formally verified processor or BLAS results. The new Green
inclusions and endpoint arithmetic below use integers and rationals
only. No sampled or finite-mode diagnostic is a numerical premise.

## Conclusion

Write X=G000-G110 and Y=G110-G111 exactly as in L153(2). Then

\[
\begin{split}
\Lambda_i={}&(-17/2+45X-15Y/2)P_{i,D}
 +(5-39X+9Y/2)P_{i,A}\\
 &+(3/4-3X-3Y/2)P_{i,X}
 +(-6+30X+15Y)P_{i,C}
 +(14-72X+6Y)B_{i,R}.                         \tag{1}
\end{split}
\]

Under the imported heat arithmetic qualifications, the full coefficients
have the strict enclosures

\[
 \boxed{-49200<\Lambda_3<-43073,\qquad
          20982<\Lambda_6<21570.}                       \tag{2}
\]

Thus neither complete quartic residual covariance has a vanishing
a^3-scaled limit. These are coefficients of precisely
kappa_0(f_(i,0),r_2) in L011(6), with no extra outside factor 3.
The complete residual here means this one quartic polynomial, not
the complete order-g^2 Ward response. Other response jets may still
compensate it. No finer remainder, logarithm, interacting error bound,
forest-independent coefficient, continuum theory or mass gap follows.

## Proof

### 1. Match the two exterior-kernel conventions

Let f_k be L008's ordinary normalized real relative one-form modes,
lambda_k their eigenvalues, A_k=f_k/sqrt(lambda_k), and V_k their
transverse forest lifts. L008(8) implies that the covariance-normalized
entries used in L152(6) are exactly

    b_(i,kl)=q_i(A_k,A_l).

Indeed R=d Delta_1^(-1/2), so its bilinear form is the polarization
of q_i evaluated on these A_k. L152(5)'s ell_k is exactly V_k in
L145's hypotheses. Consequently, for one color, the kernel in L153 is

\[
 H_{i,\mu\eta}(x,y)=\sum_{k,l}c_{i;kl}V_{k,\mu}(x)V_{l,\eta}(y),
 \quad c_{i;kl}=e^{-(\lambda_k+\lambda_l)/16}q_i(A_k,A_l). \tag{3}
\]

These are also exactly L132 and L145's coefficients. There is one
covariance normalization in b and one in each V; no inverse eigenvalue
or heat factor is added or removed. The symmetry c_(i;kl)=c_(i;lk)
gives H(x,y)=H(y,x)^T. All components below are transverse.

For h and j as defined in L153(1), put
C_r=sum_(k,l)c_(i;kl) sum_a V_(k,a)(curl_T V_l)_(ra).
The gradient part of the forest lift has zero transverse curl; hence
this is L132's exact curl convention, with
(curl_T V_l)_(ra)=partial_r V_(l,a)-partial_a V_(l,r).
Differentiating (3) and using coefficient symmetry gives pointwise

\[
 \partial_r\operatorname{tr}h=2\sum_a j_{aa;r},\qquad
 C_r=\sum_a j_{aa;r}-\sum_a j_{ra;a},\qquad
 \partial_k h_{rk}=j_{rk;k}+j_{kr;k}.                    \tag{4}
\]

For the second identity, exchange the two heat labels in both terms
of the curl expression; no divergence-free property of V is assumed.
The diagonal terms cancel in C_r, whose curl diagonal is zero.
All differentiations and integrations below can first be performed at
a rectangular mode cutoff. L152's uniformly convergent differentiated
heat sum and L132/L145's absolute bounds justify passage to all modes.

### 2. Reduce all six forms jointly

Set d=x_1+4. L132's forms in kernel notation are

\[
\begin{aligned}
 P_{i,D}&=\int_D d(\operatorname{div}_T u)\operatorname{tr}h,&
 P_{i,A}&=\int_D d\sum_r(\partial_r u_r)h_{rr},\\
 P_{i,X}&=2\int_D d\sum_{r,k}(\partial_k u_r)h_{rk},&
 P_{i,C}&=\int_D d\sum_r u_r C_r,\\
 B_{i,R}&=\int_D u_1\operatorname{tr}h.
\end{aligned}                                                     \tag{5}
\]

Since div u=0 and u has compact support, integration by parts in
the axial coordinate in T_A gives

    T_A=-(1/2) integral (d partial_1 u_1+u_1)tr h
       =(P_D-B_R)/2;                 T_B=B_R.

The u_1 term differentiates d and must remain. Transverse integration
by parts, where partial_r d=0, gives

    T_C=-P_A/2,                     T_D=(P_A-P_D)/2.

Equation (4) gives, with all unequal pairs ordered as in L153,

    T_E=(P_A-P_D)/2-P_C,             T_E+T_F=P_A-P_X/2.

For the first identity, integrate sum_r u_r sum_a j_(aa;r), obtaining
-P_D/2, subtract the full curl form P_C, and subtract the diagonal
sum integral d u_r j_(rr;r)=T_C=-P_A/2. This last subtraction
implements exactly L153's unequal-index T_E.
For the second, integrate sum_(r!=k)u_r partial_k h_(rk), then note
that the missing diagonal derivative contributes 2T_C=-P_A.
More explicitly its value is

    T_E+T_F=-integral d sum_(r!=k)(partial_k u_r)h_(rk)
           =-P_X/2+P_A.                                  \tag{6}

The diagonal correction in (6) is essential. The last form is therefore
T_F=(P_D+P_A-P_X)/2+P_C. Substituting all six identities in L153(4)
gives (1). In particular the P_A coefficient is
(D-C+E+F)/2, not (D-C)/2. The coefficient-check routine below
reconstructs all 15 constant/X/Y entries by exact rational matrix
multiplication from L153's table and these six identities.

### 3. Bound both complete Green differences

Reflection in each angle annihilates all sine numerators in L153(2).
Put x=2-2cos(theta_2), y=2-2cos(theta_3), k=x+y, on [0,pi]^2.
Integrating the third transverse angle first gives

\[
\begin{aligned}
 X&=\int_{[0,\pi]^2}
 {k/2-xy/4\over\sqrt{k(k+4)}}\,{d\theta_2d\theta_3\over\pi^2},\\
 Y&=\int_{[0,\pi]^2}{(1-x/2)(1-y/2)\over2}
       \left(1-\sqrt{k/(k+4)}\right)
                       {d\theta_2d\theta_3\over\pi^2}.       \tag{7}
\end{aligned}
\]

For k>0, the identity used here is

    (1/pi) integral_0^pi 1/(k+2-2cos t) dt = 1/sqrt(k(k+4)).

The substitution z=tan(t/2) changes the left side into
(2/pi) integral_0^infinity dz/[k+(k+4)z^2], proving it directly.
Also the average of (1-cos t)/(k+2-2cos t) is
(1/2)[1-k/sqrt(k(k+4))]. The original three-angle Green integrals
are absolutely integrable: lambda is comparable to |theta|^2 near
zero in dimension three. Thus reflection and Fubini are legitimate.
Set the X integrand to zero and Y to 1/2 at k=0; these are their
continuous limiting values. No angular cell is discarded.

For full-cell inclusion divide each angle interval into N=256 equal
pieces. Each square has exact normalized area 1/N^2. Since
2-2cos(theta) is increasing on [0,pi], certified endpoint intervals
enclose x and y throughout each square. On every noncorner square
k has strictly positive lower bound, so ordinary outward interval
evaluation encloses the first formula in (7). Its numerator is
nonnegative because it is 1-(1-x/2)(1-y/2), with x,y in [0,4].
Clipping its lower interval endpoint to zero is therefore justified.
On the sole origin square use the explicit inequality

    0 <= (k/2-xy/4)/sqrt(k(k+4)) <= sqrt(k)/4.

Indeed the numerator lies between zero and k/2 and sqrt(k+4)>=2.
This bound also controls k=0. The Y expression in (7) has no
singular denominator; direct interval evaluation applies to all
squares, including the origin square. In particular its signed
cosine factors are retained even where either is negative.

The script `scripts/combined-ward-response/enclose_quartic_residual_coefficient.py`
uses fixed-point integer intervals with scale 10^30. Its reused I
arithmetic rounds division/product bounds outward with integer floor
and ceiling, and sqrt bounds with integer square roots. The endpoints
of pi use Machin's identity pi=16 atan(1/5)-4 atan(1/239), with
alternating rational-series bounds after 60 and 20 terms. Cosines are
enclosed by terms through degree 94 of their Taylor series plus
remainder bound 4^96/96!, since 0<=theta<=pi<4. Interval evaluation
includes the uncertainty in theta itself. The endpoint x values 0
and 4 are exact. Summing all 65,536 cell intervals with exact weight
1/65,536 gives complete bounds approximately

    X in [0.1937423718,0.2013759097],
    Y in [0.01036845135,0.01285796811].

These printed decimal previews are not premises; all exact rational
endpoints, nodal enclosures, cell inclusions and summed integer totals
are saved in `scripts/combined-ward-response/quartic-residual-coefficient-certificate.json`.
The corner allowance is included in those bounds, not an omitted-mode
or asymptotic estimate. No floating arithmetic enters this inclusion.

### 4. Retain heat errors and perform exact endpoint recombination

Import precisely these full-spectrum intervals, with the qualifications
in the hypotheses:

| i | P_D | P_A | P_X | P_C | B_R |
| --- | --- | --- | --- | --- | --- |
| 3 | (2359.1,2359.2) | (19170.0,19170.1) | (29198.8,29198.9) | (1024.8,1024.9) | (1228.1260684,1228.1260686) |
| 6 | (703.6,703.7) | (-4195.9,-4195.8) | (69177.0,69177.1) | (3218.2,3218.3) | (451.5469823,451.5469825) |

The first four columns are L133's conclusion; the last is L146's.
They include retained spatial/time and arithmetic errors and the entire
omitted heat spectrum. There is no new retained heat quadrature.
Equation (3) proves applicability of those intervals here; L146's
scalar g_G or its R coefficient is not multiplied into B_R.

The expression (1) is affine in X and Y for each fixed heat vector.
Its extrema over the enclosing rectangle and five heat intervals
occur at endpoints: first evaluate each of the four X/Y corners,
then minimize/maximize each coefficient times its heat interval.
This proves a containing interval even though the actual scalars
and heat forms need not vary independently. The script performs
each endpoint product and sum as Fraction arithmetic, saving all
four sets of coefficients and lower/upper sums for each probe.
The resulting containing intervals are approximately

    Lambda_3 in [-49198.00552,-43073.73897],
    Lambda_6 in [20982.50568,21569.84534].

Exact rational comparisons against the wider strict bounds (2) pass.
The full-cell and exact-coefficient replay records are in
`scripts/combined-ward-response/quartic-residual-coefficient-audit.json`.
Reproduce from the active notebook with

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/enclose_quartic_residual_coefficient.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/enclose_quartic_residual_coefficient.py --audit

The replay checks every stored cell and all load-bearing exact
endpoints; it is same-program verification rather than an independent
implementation. Required zero failures and zero exclusion hold for
both probes. A preliminary transformation missed the unequal-index
diagonal correction in both E and F. Its invalid coefficient bounds
are preserved, explicitly marked as failed, in
`scripts/combined-ward-response/quartic-residual-incomplete-heat-transform-first-run.json`;
they are not used. The corrected transformation is the complete one
proved above. L152 supplies the mesh limit, so (2) proves the claimed
nonvanishing of exactly the approved quartic response.

### 5. Independent critical audit of this evaluation

The subsequent critical audit checks this evaluation conditional on the
established L152 limit and L153 finite contraction. It does not reprove
those asymptotic or word-enumeration inputs. Direct comparison with
L008(8),(11), L152(5),(6), L132(1) and L145(1) confirms (3)--(5).
The first derivative of H acts on its first slot; exchange of the heat
labels, rather than symmetry of that derivative in component indices,
gives (4). Applying compact-support integration by parts separately to
the trace, diagonal and off-diagonal sums recovers every identity (6).
In particular no transverse divergence constraint is imposed on V.
L011(6) assigns this covariance coefficient +1, and L153's Pauli
contraction has already supplied all three colors and the connected
factor twelve. Neither a new factor 3 nor g_G belongs in (1).

The independent program
`scripts/combined-ward-response/audit_quartic_residual_independent.py`
imports no production module. It uses exact Fraction operations and
dyadic square-root bounds at denominator D_*=2^140: for rational z>=0,
set n=floor(sqrt(floor(z D_*^2))). Then

    (n/D_*)^2 <= z < ((n+1)/D_*)^2.

These inequalities are explicitly checked for every endpoint, so the
square-root enclosure is independent of the fixed-point implementation
used in section 3. Products and positive-denominator quotients use all
four rational endpoint combinations. Machin's identity is enclosed
with 64 and 24 alternating-series terms. At each angular node a
degree-96 cosine polynomial has error <=4^98/98!: apply Taylor's
theorem through degree 97, whose coefficient of degree 97 is zero.
The dyadic angle bounds lie in [0,4), and cosine monotonicity on
[0,pi] encloses each interior node. The two endpoint x values are
set to 0 and 4 exactly. All 257 independently obtained x intervals
lie inside the saved node intervals.

Using those validated saved nodes, the program applies (7) on every
cell with rational intervals and the independent square-root bounds.
It uses the explicit sqrt(k)/4 bound on the sole origin cell and keeps
both signed cosine factors in Y. All 65,536 resulting intervals are
contained in the corresponding saved cell intervals. The ordered
cell indices exhaust the 256 by 256 grid exactly once, and exact
integer sums reproduce both saved Green bounds. Thus this is complete
cell inclusion, not sampling of the integrands or of the certificate.

For each probe it then enumerates all 2^7=128 endpoints of X,Y and
the five heat intervals, evaluates the six T forms from section 2,
and inserts L153's original A,...,F coefficients directly. This does
not use the production coefficient matrix or its endpoint routine.
The expression is affine in each of its seven variables separately,
so the full rectangle lies between the minimum and maximum of these
128 values. The extrema reproduce section 4's exact rational bounds
for both probes and lie strictly inside (2).

All ten imported heat intervals are matched to the complete L133/L146
certificates: each exact dyadic center plus/minus the sum of its saved
retained radius, time allowance and full spectral allowance lies
strictly inside the displayed imported interval. All relevant saved
source hashes match. This checks transcription, total-error assembly
and applicability; it does not independently recompute the retained
heat tensors or discharge their IEEE premises. Their standard
arithmetic theorem is Higham, *Accuracy and Stability of Numerical
Algorithms*, second edition (2002), Lemma 3.1, with the operation
counts and underflow qualifications specified in L133 and L146.
No new floating-point theorem or new heat quadrature is asserted.

Reproduce the independent audit with

    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/audit_quartic_residual_independent.py

The full rational node/cell/vertex records and all ten heat endpoint
checks are in
`scripts/combined-ward-response/quartic-residual-independent-audit.json`.
Actual failures: 0; required failures: 0. The independently verified
scalar inclusions and recombination retain exactly (2), conditional on
the stated imported heat and upstream mathematical premises. This is
an independent arithmetic implementation, not formal verification of
Python, hardware, BLAS or the entire chain of earlier lemmas. The
failed preliminary transform remains excluded and preserved.

## Mathlib

Full matching result: not checked; unknown is not absence. The exact
source assessment remains the unchanged approved quartic residual
EXPLORE assessment. Existing heat inclusions are reused within their
precise scopes rather than reproved. No originality is certified.
