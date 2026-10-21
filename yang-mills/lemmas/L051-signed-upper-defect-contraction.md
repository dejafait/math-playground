# L051 — Signed boundary defect contraction and a subleading quartic remainder

## Hypotheses

Keep L049–L050's actual SU(2) forest Gaussian, a=8/N, tau=1/16,
both quadratic probes f=f_(i,0), i=3,6, residual r=r_0, and all upper
edges, including transverse end edges. Limits take the small-coupling
coefficient at fixed mesh first. Use L018's one-color forest matrices
S=Sigma_F, B=B_(i,F), A=A_F. Let J map one-color forest coordinates
to the upper potential u on transverse interior vertices. Extend every
vertex matrix below by zero when an index is a boundary vertex. Set

\[
C=JSJ^T=NG3,\quad U=JSBSJ^T,\quad V=JSASJ^T,
\quad W=JSBSASJ^T,\quad D=I-K.                       \tag{1}
\]

Here D is the one-color noise defect, not an incidence. L050 gives
D=P/N+b_N(Delta_T)(I-P). For symmetric vertex matrices M,H define
the symmetric bilinear functional

\[
\begin{split}
\Phi_D(M,H)=\frac12\sum_{e=(v,v'),\,h=(w,w')}D_{eh}\big[&
M_{vw}H_{v'w'}+H_{vw}M_{v'w'}\\
&-M_{vw'}H_{v'w}-H_{vw'}M_{v'w}\big].                \tag{2}
\end{split}
\]

The sum is over ordered pairs of the entire upper edge set with L049's
orientation. No off-diagonal kernel entry, transverse direction or
boundary row is omitted. W need not be symmetric; W+W^T is symmetric.

## Conclusion

L049's positive quartic defect has the exact signed connected response

\[
\kappa(f,r,Z)=6\Phi_D(C,W+W^T)+6\Phi_D(U,V).          \tag{3}
\]

The first term contains the one internal potential pair C; the second
contains no internal quartic pair. Neither term has a prescribed sign.
For L049's full remainder R=S_(4,nr,top)-q_A, both probes obey

\[
|\kappa(f,r,R)|\le C_i a^{-1},\qquad
a^2\kappa(f,r,R)\longrightarrow0.                  \tag{4}
\]

Thus, with G_i the complete selected nonradial upper quartic plus
top/top cubic-pair group of L049(9),

\[
G_i=-6\Phi_D(C,W+W^T)-6\Phi_D(U,V)
          +\mathcal E(f,r)+\varepsilon_{i,a},
\qquad |\varepsilon_{i,a}|\le C_i a^{-1}.           \tag{5}
\]

This removes R, but only at a^2 scale. It supplies no bound or scaled
limit for either Phi term or for E. In particular it does not prove
compensation of L047, exclude a subleading power or logarithm in R,
evaluate the complete logarithmic response, or improve the required
interacting reflected error <=c_box/2. Other cubic pairs, all other
L011 jets, continuum construction, full reflection positivity and
infrared/mass control remain unresolved.

## Proof

### 1. Contract the nonlocal defect without discarding connected terms

Import the standard finite-dimensional Gaussian quadratic-tilt formula
and Isserlis' theorem, in the same conventions as L018(8) and L025's
connected-pairing proof. For sufficiently small real s,t, the normalized
tilt of the full three-color forest law by exp(sf+tr) is a centered
Gaussian with three independent identical covariance blocks

\[
S(s,t)=(S^{-1}-2sB-2tA)^{-1}.                        \tag{6}
\]

S is positive definite at each fixed mesh, so (6) exists and stays
positive on a neighborhood of zero. Polynomial expectations and their
first two derivatives there are justified by an integrable Gaussian
majorant. Additive constants in f,r cancel from the normalized tilt.
No exponential of the quartic Z is required.

Let C(s,t)=J S(s,t)J^T. Differentiating the inverse matrix, without
commuting its factors, gives at s=t=0

\[
C_s=2U,\quad C_t=2V,\quad C_{st}=4(W+W^T).          \tag{7}
\]

For any one-color vertex covariance M, Isserlis and the three-color
epsilon contraction give

\[
E[(u(v)\times u(v'))\cdot(u(w)\times u(w'))]
=6(M_{vw}M_{v'w'}-M_{vw'}M_{v'w}).                   \tag{8}
\]

Indeed each nonzero epsilon has two different input colors. A pairing
within a cross product has equal input colors and vanishes. The two
cross-edge pairings have opposite signs, each with six nonzero color
assignments. Equation (8) remains true for coincident vertices and
pinned zero rows. Applying it to Z=sum_(e,h) D_(eh) Q_e.Q_h/8 gives

\[
E_{s,t}Z=\tfrac34\Phi_D(C(s,t),C(s,t)).             \tag{9}
\]

D in (9) is the fixed original covariance defect. It is not recomputed
under the tilt. Differentiating the normalized expectation twice gives
the third cumulant kappa(f,r,Z), including all five connected
subtractions. Symmetry and bilinearity of Phi yield

\[
\partial_s\partial_t E_{s,t}Z\big|_0
=\tfrac32[\Phi_D(C,C_{st})+\Phi_D(C_s,C_t)],
\]

which is (3) by (7). This is a contraction of the actual finite forest
polynomial; it does not make Z or either observable independent of
the curvature noise. The correction E in L049 is still required
when this formula is used for the cubic-pair group.

### 2. Bound the entire one-internal-pair part of R

Use L029's local H,L,d coordinates and its one-color internal entries
h,l,e,b,c,f_c (write f_c for its covariance Cov(L,d), to distinguish
it from the probe). Subtracting the quadratic Wick coefficient of
q_A=|[H,L]|^2/8 from L029(3) gives exactly

\[
\begin{split}
Q_{2,R}={}&-\tfrac{f_c}3|H|^2-\tfrac e{12}|L|^2
-\tfrac l{12}|d|^2+\tfrac c3 H\cdot L\\
&+\tfrac b3 H\cdot d
+(\tfrac{f_c}6-\tfrac h3)L\cdot d.                 \tag{10}
\end{split}
\]

This retains internal d pairings. L029(4) gives h,l,|b|<=C N,
e<=1, f_c=l/N and c=b/N, so the six coefficients of (10), in
the order HH,LL,dd,HL,Hd,Ld, have bounds

\[
O(1),\ O(1),\ O(a^{-1}),\ O(1),\ O(a^{-1}),\ O(a^{-1}).
\]

L025's general contraction proof applies by linearity to the quartic
R: its negative one-pair response is -24 Tr(M_R W_i) with M_R the
one-color symmetric matrix of (10). Off-diagonal coefficients are
divided by two, and both W orientations are retained. L029(6)–(7)
bound these entries by respectively a^2,a^4,a^6,a^3,a^4,a^5 times
mesh-independent constants. There are at most 3N(N-1)^2 upper edges.
The absolute-sum bounds for the six types are therefore

| Type | HH | LL | dd | HL | Hd | Ld |
| --- | --- | --- | --- | --- | --- | --- |
| Bound | O(a^-1) | O(a) | O(a^2) | O(1) | O(1) | O(a) |

Consequently the entire one-internal-pair R response is O(a^-1),
with pinned endpoints and all modes included. The improvement is the
removal of q_A's O(N) coefficient of |H|^2; it is not a bound obtained
by ignoring d.

### 3. Retain the signed companion and assemble

The q_A contribution to L040(3) is exactly its first line. Thus the
negative no-internal-pair R response is the sum of the last two lines,
precisely D_(i,a) in L041(1). Import L041(2), which proves
|D_(i,a)|<=C_i a^-1 using its separated Green column and pinned
summation by parts. In particular the u_c v_b term is controlled as
a signed sum; a termwise absolute estimate would not suffice.

L025 proves that these two pairing classes exhaust a connected
quadratic/quadratic/quartic cumulant. Combining the bounds proves
(4). Substitute (3) and (4) into L049(9) to obtain (5), with
epsilon_(i,a)=-kappa(f,r,R). L050 supplies the exact D in (1);
its low-mode limit has not been interchanged with any sum in (2).

### 4. Verification and remaining discriminating test

The finite checks in
`scripts/combined-ward-response/check_signed_upper_defect.py` compare
(3) with direct rational Gaussian moments for color-diagonal quadratic
observables and a nonlocal defect on several edges, including a pinned
end edge. The certificate
`scripts/combined-ward-response/signed-upper-defect-certificate.json`
retains the full inputs, both pairing values and every result. These
are algebra checks, not evaluations of the actual box or scaled limits.
All four exact checks and the empty failures field were inspected.
The two cumulants are 16872/5 and 480; deleting off-diagonal defect
entries changes them by -2793/5 and -474, respectively. Thus these
checks exercise cross-edge entries as well as the connected subtractions.
The arbitrary-mesh bound (4) follows from the analytic estimates above.

Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. This is reproduction
of finite Gaussian methods with a local applicability deduction, not
a new general renormalization result. Its necessary specialization is
the nonlocal physical-boundary kernel and the actual residual/probe
contractions that the inspected sources do not compute.

The next discriminating comparison is still at a^2 scale against
L047: evaluate or bound the two signed Phi terms together with E.
An estimate on low modes of D alone does not do this, because C and V
contain unflowed internal frequencies. R is now subleading at that
scale but is retained for any eventual logarithmic calculation. No
condition on the uncomputed terms is used as a proved premise.

## Mathlib

Coverage of the full specialized signed defect formula and R bound:
**not checked**. Coverage of supporting finite Gaussian tilting,
Isserlis' theorem and cumulant differentiation: **not checked**.
No matching Mathlib theorem is asserted. L018 and L025 fix the imported
finite Gaussian identities, while L029, L040–L041 and L049–L050 supply
the specific lattice polynomials, estimates and kernel. General
flow-renormalization theorems are not reproved or assigned unstated
physical-boundary hypotheses.
