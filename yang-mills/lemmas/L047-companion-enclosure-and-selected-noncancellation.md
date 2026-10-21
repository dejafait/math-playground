# L047 — The two selected upper-face action classes do not cancel

## Hypotheses

Keep L046's exact SU(2) box, bare coupling, two original Wilson-flow
probes, tau=1/16, lower-rooted straight forest, compressed forms Q_i^0,
and functionals A_i,B_i,J_i,I_i. Take the small-coupling coefficient
at fixed mesh before a=8/N tends to zero. L046 imports the complete
selected companion limit and its normalization from L045. L039's
one-internal-pair functional I_i retains its unrestricted second mode
index: the companion's axial compression is not applied to I_i.

Use exactly L037's 898 hexadecimal Fourier transforms for h=0,1,
|n|<=224, with their established complex errors <6e-12 and <9e-12.
The calculation uses L039's stated IEEE binary64 arithmetic model:
correctly rounded addition/product or FMA, arbitrary summation order,
no overflow, and underflow covered by its additive 1e-290 allowance.
Integer interval input arithmetic does not assume accuracy of machine
pi, exponentials, trigonometric evaluations or Gauss root proposals.
This is an informal computer-assisted enclosure, not formal verification
of the processor or BLAS implementation.

## Conclusion

The exact continuum traces of L046 have enclosures

\[
\begin{array}{c|cc}
 &A_i&B_i\\\hline
3&(148.83170,148.83172)&(111.03741,111.03743)\\
6&(-147.77981,-147.77978)&(-32.21998,-32.21996).
\end{array}                                                     \tag{1}
\]

Using the exact 0<c_*<=1/4, without a numerical value of c_*, gives

\[
2381.30<J_3<5046.21,\qquad -3137.76<J_6<-2364.47.              \tag{2}
\]

Consequently the combined a^-2 coefficients of **only** L030/L039's
upper-face one-internal-action-pair class and L045/L046's complete
selected companion satisfy

\[
\begin{split}
-19379.50&<J_3-48I_3<-16688.19,\\
-164110.08&<J_6-48I_6<-163241.27.                             \tag{3}
\end{split}
\]

Both are strictly negative. This establishes selected noncancellation,
not a coefficient of the complete Ward response. Other plaquettes,
the cubic-action pair, coordinate measure, insertion/observable/flow
jets and L019's nonlinear forest compensation remain unevaluated as a
complete group. Neither subleading powers/logarithms nor finite matching,
an interacting error <=c_box/2, continuum fields, full reflection
positivity, infrared control or finite physical mass is established.

## Proof

### 1. Retain the actual weak forms

Use L046(3)–(4), with both arguments in the transverse Dirichlet
space. Write its coefficient Phi as a product of x rho(x), rho(x),
x rho(x) in directions 2,3,4. An equivalent four-dimensional weak
entry uses Psi_24 and two normalized axial zero cosines; their product
is 1/8 and their coefficient integral is exactly kappa. For a monomial
write the coefficient derivative and argument derivatives as d,a,b,
with its rational coefficient v. Restrict both argument components to
1 and their axial derivatives to zero. The resulting Q_3,Q_6 have total
derivative degree four. The scalar S has the two weak terms
d=(0,3,0,1) and (0,1,0,3), coefficients +1,-1 and a=b=0. These are
the derivatives of the full potential, including every transition.

For each product Q_i S or Q_i Q_3, multiply the finite weak expansions
and collect identical coordinate products exactly over the rationals.
There are respectively 4,3,16,16 collected products for (A_3,B_3,A_6,B_6).
Sorting the two weak features in a coordinate merely uses commutativity
of their scalar product. No approximate zero is dropped. In a coordinate
with positive modes k,l, normalized sine waves have amplitudes
sign(p)/(4i), p=+/-k, and shifted phase i^p. Moving d coefficient
derivatives onto the two waves therefore yields the real weak entry

\[
 W_h(d,a,b;k,l)=\frac{\omega^{d+a+b}}{16}
 \sum_{p=\pm k,\ q=\pm l}
 \operatorname{sign}(p)\operatorname{sign}(q)
 p^a q^b(p+q)^d
 \operatorname{Re}\{i^{p+q+a+b-d-2}F_h(p+q)\},                \tag{4}
\]

where omega=pi/8 and F_h(n)=integral x^h rho(x)exp(i omega n x)dx.
For the axial zero modes, W_0(0,0,0;0,0)=F_0(0)/8=kappa;
a positive derivative there gives zero. Exact reflection parity makes
(4) zero when h+d+a+b+k+l+2 is odd. This uses the symmetry of the
exact rho, not a near-zero entry of its approximate table. The remaining
entries are enclosed using the actual table with its complex errors:
each real and imaginary component lies within the respective error.
The four-wave formula (4) then follows by real interval arithmetic,
so cancellation between waves is enclosed rather than presumed exact.

### 2. Full omitted-mode bound

Here both transverse index triples have positive entries. Set
R²=|k|²+|l|². The four-dimensional potential has L1 norm <=2916,
and each normalized wave's absolute amplitude sum is <=1/2, including
the axial constants. Moving coefficient derivatives off the potential
as in L033 gives, for degree-four weak operators,

\[
 |T_{kl}|\le(2916/256)2^{-4}R^4\Omega(T),\qquad
 \Omega(T)=\sum|v|2^{|d|}.                                  \tag{5}
\]

The restrictions cannot increase L033's conservative bounds
Omega(Q_3)<=192 and Omega(Q_6)<=768. The two scalar terms give
Omega(S)=32, and the second Q_3 factor is <=192. Both inverse
eigenvalues are <64/27 and tau omega²>c=9/1024. Thus the absolute
product summand, for either A_i or B_i, is bounded by

\[
 K_i R^8e^{-cR^2},\quad
 K_i=(2916/256)^2 2^{-8}(64/27)^2\Omega(Q_i)\,192.
                                                                  \tag{6}
\]

These constants are strictly below L033's 11584512 and 46338048.
Since R>=1, R^8<=R^10. Add a seventh index equal to zero, then
enlarge its domain to all nonnegative integers. The omitted six-index
cube is dominated by L033's omitted seven-index cube. Therefore its
explicit bound applies to each of the two traces separately:

\[
 \text{tail}_i\le C_i7^4(7T_{10}S_0^6+42S_{10}T_0S_0^5),     \tag{7}
\]

at M=112. Import L033's complete rational upper bounds
S_0<=9.95308720484, S_10<=5.32283164890e12,
T_0<=2.10711391688e-49 and T_10<=7.25796325172e-29.
Exact substitution gives tails <1.38e-11 and <5.50e-11.
The certificate recomputes (6)–(7). This covers every omitted mode,
not only the modes observed in a refinement run.

### 3. Time-rule error with the actual coefficient uncertainty

Each inverse-linear heat weight has the exact representation
e^(-tau lambda)/lambda=integral_tau^infinity e^(-s lambda)ds.
Use L039's positive 12-point Gauss rule on the shifted initial panel
[0,2^-14] and its 22 doubling panels through endpoint 256, independently
for both times. Both retained eigenvalues are >27/64 and less than
3*112²/4<12544, so L039's applicability hypotheses hold.
Import the standard Gauss–Legendre quadrature remainder theorem and
L039's uniform specialization for the linear inverse weight:

\[
 |\lambda\widehat B(\lambda)-1|\le\epsilon_B,
 \quad\epsilon_B=C_{12}[1+22(25)!]+H,
 \quad C_{12}=\frac{(12!)^4}{25((24)!)^3},
 \quad H=\Big(\sum_{j=0}^{160}108^j/j!\Big)^{-1}.             \tag{8}
\]

Only its inverse-linear case is needed; the squared-inverse weight
in I_i is not substituted here. Its proof is not repeated. The product
relative error is <=2epsilon_B+epsilon_B².

For each collected product, the absolute initial tensor separates into
four coordinate sums of e^[-tau omega²(k²+l²)]|W_1 W_2|. Enclose
each W using (4), including L037's coefficient errors, and enclose each
of those nonnegative sums upward. Multiply the four bounds, multiply
by the absolute rational collected coefficient, and sum. Call the
result P. Since the true weak entries belong to these intervals, P
bounds the absolute expansion with the **exact** coefficients.
Integrating the spectral-gap envelope in both shifted times gives
the complete absolute inverse-weight bound P(64/27)². Hence the entire
time-rule error is at most

\[
 E_{\rm time}=P(64/27)^2(2\epsilon_B+\epsilon_B^2).            \tag{9}
\]

Coefficient uncertainty is propagated inside the signed finite rule
as well; (9) does not replace that propagation. This avoids the stopped
scalar/global-moment error propagation of ATTEMPTS/016.

### 4. Certified inputs and complete signed tensor arithmetic

The implementation is `scripts/combined-ward-response/check_companion_enclosure.py`.
It imports L039's integer interval primitives and exact-rule constructor
without changing them. At scale 10^80, floor/ceiling endpoint arithmetic
encloses all rational operations. Machin's identity with alternating
arctangent remainders encloses pi. Integer square bounds enclose 1/sqrt(8).
The 12 disjoint sign-changing Legendre root brackets have width <=1e-50;
degree 12 identifies all roots. The usual derivative formula encloses
their positive Gauss weights. Alternating Taylor bounds at an argument
<=1/8 followed by interval squaring enclose every heat entry. The
table is never regenerated. Equation (4)'s integral entries use only
these enclosures and the specified hexadecimal transforms/errors.

For two intervals represented by floating centers/radii (c,r),(d,t),
the product's propagated radius includes |c|t+r|d|+rt; a sum includes
r+t. Rounded center products/sums add 1e-15 times the absolute result
and 1e-290, with upward nextafter operations. For a dot product of
inner dimension n<=276, use gamma_n=(2n+2)/(2^53-(2n+2))<G,
where G is the upward binary64 enclosure of 1e-12. A nonnegative dot
upper bound is nextafter((a dot b)/(1-G),+infinity)+1e-290, propagated
upward. The signed dot radius is the sum of the corresponding upward
dots of |c| with t, r with |d|, and r with t, plus G times the upward
dot of |c| with |d| and the additive allowance. The implementation
checks the inequalities for G and the rounded denominator and rejects
nonfinite arithmetic. These are L039's stated forward-error bounds.

For each coordinate feature, enclose the signed matrix
E W_1 W_2 E^T for all 276 time nodes in both directions. Multiply
the four coordinate matrices entrywise, apply the exact rational
coefficient interval, and add over all collected products. Finally
contract with the two positive inverse-linear time weight vectors.
This retains every mode at cutoff 112 and all transition coefficients.
The saved radii include coefficient, root, heat, weight and tensor
arithmetic errors. Add (9) and (7) to the final arithmetic radius.

The full certificate is
`scripts/combined-ward-response/companion-enclosure-certificate.json`;
all 38 coordinate feature enclosures are saved in four archives
`scripts/combined-ward-response/companion-enclosure-axis<j>.npz`, j=0,1,2,3.
The complete relevant error upper bounds are

\[
\begin{array}{c|rr}
 & A_i & B_i\\\hline
3&2.822\,10^{-6}&1.574\,10^{-6}\\
6&7.761\,10^{-6}&2.865\,10^{-6}.
\end{array}                                                    \tag{10}
\]

These are enclosure errors, unlike L046's preceding diagnostic
refinement differences. Their exact rational sums and dyadic centers
are saved in each `/final` record. The exact computed intervals are
contained strictly in the displayed rational decimal intervals (1).

The reproduction commands, from this notebook, are

```sh
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_companion_enclosure.py
OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/audit_companion_enclosure.py
```

The audit at `scripts/combined-ward-response/companion-enclosure-audit.json`
checks the complete expected coordinate-feature coverage, source and
archive hashes, 12 root brackets, 276 mapped rule records, 31301 heat
intervals, 928258 saved weak-entry occurrences and all 2894688 coordinate
tensor entries. It recomputes every signed contraction, the four exact
rational final error budgets and both separations. All four errors are
<1e-5, and there are no failed budgets. This is an all-record aggregate
audit, not an independent reconstruction of each primitive interval or
verification of BLAS. The primitive interval induction and stated
arithmetic model above remain the mathematical justification.

### 5. Separate the selected classes

L046 gives J_i=16A_i+96c_*B_i with 0<c_*<=1/4. From (1), B_3>0
and B_6<0, so respectively

\[
16A_3<J_3\le16A_3+24B_3,\qquad
16A_6+24B_6\le J_6<16A_6.
\]

Substituting the rational endpoints of (1) gives (2).
L039 supplies 21734.4<48I_3<21760.8 and
160876.8<48I_6<160972.32. Subtraction gives (3).
The limits already proved in L030 and L045, imported by L046,
identify (3) with the sum of these two selected classes' scaled
limits. No interchange with positive coupling or claim about an
uncomputed compensation is used.

Reuse the unchanged SPECIALIZE assessment
`drafts/literature/2026-09-26-current-target.md`. The primary general
flow input remains Luescher–Weisz, *Perturbative analysis of the
gradient flow in non-abelian gauge theories*,
[arXiv:1101.0963v2](https://arxiv.org/pdf/1101.0963v2), sections
7.1–7.4, (7.1)–(7.8), and 8.2, under ordinary four-dimensional
renormalization on R^4. It does not compute these fixed-box traces
and is not reproved. This local standard-method specialization repairs
the diagnostic's missing verification; it makes no originality claim.

## Mathlib

Coverage of the full fixed-box companion enclosure and selected
noncancellation: **not checked**. Coverage of supporting spectral
heat expansions, Fourier integration by parts, Gaussian quadrature,
interval arithmetic and floating dot bounds: **not checked**.
No full matching theorem or direct Mathlib link is asserted; unknown
coverage is not evidence of absence.
