# Corollary 609a: the selected first-period allocation is positive

## Hypotheses

Use exactly L609's full-line density p=k/Z, k(u)=4 Phi(u/2),
Z=integral_R k, and its functions h, tau=h/p, q=-tau', J_a and
the complete four-term K_x(a,b). In particular

\[
G_x(a)=q(a)J_a(x)^2+
2p(a)\int_0^a[\tau(b)-\tau(a)]p(b)K_x(a,b)\,db.
\]

No auxiliary density, kernel term, limiting floor or normalization
is changed. L605 supplies smoothness and positivity through a=0;
L019 gives the positive theta series, differentiated using L016.
For the spatial tail use only L564's complete envelope
k(u)=2 Phi_R(u)<=20000 exp(-u^2) for u>=0. Retain all imported
theta/source-proof qualifications from L609 and L605. No source
theorem asserting a sign of this integral is assumed.

The numerical method is imported from Fredrik Johansson,
*Numerical integration in arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1](https://arxiv.org/pdf/1802.07942v1),
Section 2 algorithm step 2 and Section 2.1, printed pp.2--4:
a box on the entire real input encloses its integral after multiplication
by the interval length. No complex-analytic quadrature is used.
Reuse the geometric-tail machinery assessed in Johansson,
*Numerical Evaluation of Elliptic Functions, Elliptic Integrals and
Modular Forms*, [arXiv:1806.06725v1](https://arxiv.org/pdf/1806.06725v1),
Section 1.2, p.4, Section 1.4.2 (1.18)--(1.20), pp.12--13;
L609 gives the explicit theta specialization below. Midpoint acceleration
uses the standard named real Taylor theorem with bounded second derivative.
Arithmetic guarantees are imported from the Python Software Foundation,
*Python Library Reference*, [CPython v3.15.0 decimal documentation](https://raw.githubusercontent.com/python/cpython/v3.15.0/Doc/library/decimal.rst),
named entries Decimal, Context, Rounding modes, copy_abs, copy_negate,
exp, next_minus and next_plus. Their implementation is not independently
verified here. This specializes known numerical methods, without
reproving or claiming a new general method.

## Conclusion

At the sole approved frequency x=11, writing A=2pi/11,

\[
\boxed{\quad
\int_0^A G_{11}(a)\,da
\in[0.0001633789,\;0.0002004819]\subset(0,\infty).
\quad}                                                     \tag{1}
\]

This rejects the proposed negative witness on the first complete
outer period. It signs no other group or frequency, their sum with
the floor, the total first Xi form, or any higher form. L609's
negative fixed-a witness is unchanged. A positive integral is
compatible with its negative integrand value. This is a new local
calculation relative to the checked sources, without certified
originality or formal machine verification. The independent local
proof and implementation audit below passes; imported source proofs
and the Decimal backend retain their stated qualifications.

## Proof

**Exact reduction retaining the triangle.** All notation in this
paragraph is unnormalized. Put

\[
\begin{aligned}
H(u)&=\int_u^\infty v k(v)\,dv,&
S(a)&=\int_0^a k(b)\cos(xb)\,db,\\
T(a)&=\int_0^a H(b)\cos(xb)\,db,&
U(a)&=\int_0^a bH(b)\sin(xb)\,db,\\
V(a)&=\int_0^a bk(b)\sin(xb)\,db.&
\end{aligned}
\]

L609's exact normalization cancellation gives

\[
Z^2G_x(a)=4\left(a+\frac{H(a)k'(a)}{k(a)^2}\right)S(a)^2
+2\int_0^a[k(a)H(b)-H(a)k(b)]K_x(a,b)\,db.       \tag{2}
\]

Its complete kernel is
K_x(a,b)=2[(cos(xa)+xa sin(xa))cos(xb)-xb cos(xa)sin(xb)].
Set C=cos(xa) and E=C+xa sin(xa). Distributing both products in
the integral in (2), with their original signs, gives

\[
Z^2G_x(a)=4\left(a+\frac{H(a)k'(a)}{k(a)^2}\right)S(a)^2
+4\{E[k(a)T(a)-H(a)S(a)]
          -xC[k(a)U(a)-H(a)V(a)]\}.                         \tag{3}
\]

Every integral is over a compact b interval and its continuous
integrand is bounded. Thus this is ordinary finite linearity, with
no infinite interchange or sign assumption. It retains every point
0<=b<=a, including the moving upper limit. L605 gives k(0)>0
and smoothness of k and H. The four primitives vanish at zero;
(3) is continuous there with value zero. No division by a, S, or
k(b) is used. The only nonconstant divisor is k(a)^2.

**Uniform imported bounds and arithmetic.** The unchanged L609
implementation `scripts/theta-allocation/certify.py` supplies directed
interval operations at precision 45, exact sign copying, an
adjacent-number widening of correctly rounded nearest exp, Machin pi,
and theta/derivative enclosures on 0<=u<=8. Explicitly it sums n=1,...,5
in e^(u/2) sum e^(-v_n) P_j(v_n), v_n=pi n^2 e^(2u), where

\[
P_0=8v^2-12v,\quad
P_1=-16v^3+60v^2-30v,\quad
P_2=32v^4-224v^3+330v^2-75v.
\]

The complete omitted tails on that domain are
[0,T_0] for k and [-T_j,T_j] for derivatives j=1,2, with
T_j=2 C_j 144^(j+2) exp(-104) and (C_0,C_1,C_2)=(20,106,661).
L609 proves the decreasing-term/geometric domination for all n>=6.
The evaluated upper allowances here are respectively less than
5.652e-40, 4.314e-37 and 3.874e-34. The complete spatial allowances
in the actual u coordinate, from the envelope above, are

\[
0<=H(8)<=10000e^{-64},\qquad
0<=\int_8^\infty k<=1250e^{-64}.                            \tag{4}
\]

These are bounds on all omitted terms, not a first-term approximation.
Both sides of Z are counted using evenness. Machin's pi enclosure
is used directly to form an interval for A; its width is never
replaced by a decimal midpoint. Every arithmetic input is an integer
or exact decimal string. Basic operations use explicit FLOOR/CEILING
contexts, exp is widened at both endpoints, and squares handle all
three sign cases. The original core and singleton certificates are
preserved, not rerun or overwritten.

**Variable tail endpoint.** For each actual A in its enclosure, use
u=A+(8-A)s, 0<=s<=1, and M=4096 equal s cells. Their actual common
width is (8-A)/M. Endpoints and midpoints are evaluated as convex
combinations of A and 8, enclosing the true points while keeping
every kernel argument in [0,8]. On a real cell of width w and
midpoint m, the midpoint Taylor error for f is at most
w^3 sup|f''|/24: the linear Taylor term integrates to zero and
the quadratic remainder integrates to that value. Take
f=uk, f''=2k'+uk'' for H, and f=k, f''=k'' for mass. The midpoint
values, derivative supremum and width are all intervals enclosing
their actual values. Summing the outward midpoint contributions
and adding (4) encloses H(A) and integral_A^infinity k uniformly
for the true endpoint. No analyticity hypothesis or requested
numerical tolerance replaces this derivative proof.

**Outer cells and whole-cell H.** Put N=65536, r_i=i/N and
u_i=A r_i. For each fixed actual A these are an exact partition
of [0,A] with actual width d=A/N; the change a=A r has Jacobian A.
Use the whole input box
[lower(A i/N),upper(A(i+1)/N)] and the interval for d in all products.
Thus endpoint uncertainty is included in the points and Jacobian;
there is no missing irrational-endpoint sliver. Boxes may overlap,
but the underlying true parameter cells partition the domain.

On each cell the complete series encloses k,k'. Every such k box
has positive lower endpoint. Descend from the H(A) enclosure.
If H(u_(i+1)) is in [L,U] and the whole-cell positive integral
d*uk is enclosed by [v_-,v_+], then for every a in the true cell,

\[
H(a)\in[L,U+v_+],\qquad
H(u_i)\in[L,U]+[v_-,v_+].                                  \tag{5}
\]

This follows from 0<=integral_a^u_(i+1) uk<=v_+; it proves the
descending induction at every cell, not just at sampled points.

**All moving primitives and outer integration.** For each of the
four primitive integrands f, let P_i enclose integral_0^u_i f and
F_i enclose f on the entire cell, using (5) wherever H occurs.
For all a in that cell,

\[
P(a)\in P_i+[0,d_{hi}]F_i,\qquad
P_{i+1}\in P_i+dF_i.                                      \tag{6}
\]

Indeed the partial interval length lies in [0,d_hi]. The real-box
rule gives its signed integral in that length times F_i, whether
F_i is positive, negative or straddles zero. The full-cell update
uses the true d enclosed by d. Starting all four primitives at zero,
(6) encloses their values for every a; it therefore includes the
entire b=a boundary triangle. It does not keep only rectangles
strictly below that boundary.

For sin and cos, use L609's Taylor routine only for the first
midpoint angle and the step angle. Both have magnitude less than
0.000096<5. Propagate midpoint enclosures by simultaneous angle
addition with the two old intervals; the recurrence includes all
rounding/endpoint uncertainty. The global derivative bounds 1
give whole-cell sine/cosine enclosures after adding radius
(x*d/2)_hi. Direct Taylor evaluation at 2pi is not used. No periodic
reset discards accumulated interval errors.

Insert (5), (6), the complete k,k' and trigonometric boxes into (3).
Whole-cell interval inclusion gives its value everywhere in that
outer cell. Summing d times those boxes encloses integral_0^A Z^2G.
Dependency between the same A or other shared quantities can only
widen interval products. Finally enclose
Z=2(integral_0^A k+integral_A^infinity k), certify Z>0 numerically
and divide by Z^2 once. This is the full original normalization.

**The single finite computation and complete evidence.** The caps
above, precision 45, five terms and cutoff 8 were saved before the
run in `drafts/2026-11-01-theta-first-period-calculation-working.md`.
There was one run, no adaptive restart, new frequency or later period.
Reproduction command (the executable refuses to overwrite an existing
certificate; preserve it elsewhere before a later authorized replay):

```text
python3 scripts/theta-allocation/first_period.py
python3 scripts/theta-allocation/check_first_period.py
```

The complete primary output is
`scripts/theta-allocation/first-period-certificate.json`. It stores
all 65536 head cells and 4096 tail cells, their whole-input boxes,
primitive bounds, layer/remainder bounds and tail error contributions.
There are exactly 4096 order-zero, 65536 order-one and 4096 order-two
kernel calls: 73728 total, within the declared cap. Every constructed
interval is finite and ordered. All kernel arguments lie in [0,8].
The minimum numerical head-k lower endpoint exceeds 0.04629929,
and Z>0.99417759, so both mathematical divisions are separated from
zero throughout. There are 303312 recorded division operations;
all denominators miss zero. Only two direct sincos calls are made;
the maximum whole-cell trigonometric radius is <0.000047937.

Runtime is CPython 3.15.0, C Decimal, decimal specification 1.70,
libmpdec 4.0.1. All contexts have precision 45, Emin=-999999999,
Emax=999999999 and clamp=0. Only Inexact and Rounded are set;
InvalidOperation, FloatOperation, DivisionByZero, Overflow, Underflow,
Subnormal and Clamped are false in all contexts, including the
inherited pi/tail construction. A version-attribute deprecation
warning affects telemetry only. Source hashes identify the unchanged
core and exact first-period executable.

The following rational-decimal bounds widen the complete inspected
certificate outwards:

| Quantity | Lower | Upper |
|---|---:|---:|
| A | 0.5711986642890533160841169787780914334903942 | 0.5711986642890533160841169787780914334903947 |
| H(A) | 0.00168380237 | 0.00168390179 |
| Z | 0.99417759 | 0.99430515 |
| Integrated layer, multiplied by Z^2 | 0.00022957472 | 0.00023155389 |
| Integrated remainder, multiplied by Z^2 | -0.00006805134 | -0.00003339983 |
| Z^2 integral G | 0.00016152339 | 0.00019815405 |
| integral G | 0.0001633789 | 0.0002004819 |

The actual final lower endpoint is
0.000163378930234523122445938516309768044535219018;
the upper endpoint is
0.000200481817541327521991840904188829422802237864.
The negative-witness test required upper<0; instead lower>0.
This proves (1), with precisely the opposite sign to that proposal.

The complete propagated normalized radius is
0.000018551443653402199772951193939530689133509423.
Before normalization, layer and remainder radii are respectively
<9.896e-7 and <0.000017326; their sum is
<0.000018316 and bounds the raw radius. These are propagated
component bounds, not unpaid errors to add again. The tail midpoint
radius allowances are <4.971e-8 for H(A), <9.702e-8 for one-sided
mass; spatial allowances are <1.604e-24 and <2.005e-25. Maximum
whole-cell primitive radii for S,T,U,V are respectively
<0.000044054, <0.000002649, <5.300e-7 and <0.000009358.
All series, spatial, midpoint, whole-cell, prefix, outer, endpoint
and rounding uncertainties are included in the final interval.

The exact-rational certificate check in
`scripts/theta-allocation/first-period-certificate-check.json` checks
every saved head/tail cell against the parameter endpoints, every
positive head-k bound, all saved tail/head aggregate sums, Z and
the final normalization, plus error radius, counts, flags and source
hashes. It uses exact Fractions on the saved decimal endpoints,
without rerunning numerical quadrature. This verifies domain/sum
coverage and serialization consistency; it does not independently
recompute the theta, exp or trigonometric enclosures. The complete
load-bearing aggregate, arithmetic, cap, runtime and telemetry
objects, and selected full endpoint-cell records, were inspected
with the shared JSON inspector. The per-cell inclusion proof above
and complete all-cell checks, rather than a floating preview,
justify using the aggregate bounds. The later independent audit below
also checks the cell enclosures and their use. No imported
library/source-proof audit or RH conclusion is claimed.

**Independent complete-enclosure audit, 1 November 2026.** The ready
assessment `drafts/literature/2026-11-01-c609a-independent-enclosure-audit.md`
was reused unchanged. This is REPRODUCTION / proof_audit of the existing
result, not a new sign discovery or a stronger positivity assertion.
The prior fixed-a and first-period stops remain distinct.

1. **Algebra, coordinates and origin.** Substituting h=H/Z and p=k/Z
   gives tau=H/k, q=a+Hk'/k^2 and J_a=2S/Z. Expanding the original
   cosine pair gives 2C cos(xb); expanding its sine pair gives
   2xa sin(xa)cos(xb)-2xb C sin(xb). Consequently its integral against
   k(a)H(b)-H(a)k(b) is exactly the remainder in (3), with both factors
   4 and its minus sign. Finite linearity is legitimate on the compact
   triangle because all functions are continuous. At a=0 the four
   primitives vanish, k(0)>0, and H,k are smooth by L605, so no singular
   boundary term or divided zero is hidden. L019 gives k=2 Phi_R in the
   actual u coordinate. L564's complete Gaussian envelope therefore
   gives precisely (4), with both one-sided masses doubled for Z.

2. **Inclusion through every moving boundary.** For each true A,
   u_i=Ai/N partition [0,A], and the affine tail cells partition [A,8].
   Their width intervals include their actual Jacobians. The saved
   numerical boxes enclose every such endpoint and midpoint, and lie
   in [0,8]. Overlap of boxes cannot remove part of those true domains.
   Positivity of uk makes (5) an induction from H(A) through every
   head cell. For a signed integrand f in F_i, its partial integral
   of actual length l satisfies l*lower(F_i)<=integral f<=l*upper(F_i).
   Since 0<=l<=d_hi, (6) encloses it on either sign and across zero.
   The full-cell update starts the next prefix correctly. Thus all
   four primitives include b=a, rather than omitting boundary cells.
   The tail midpoint uses the actual width cubed and exactly
   (uk)''=2k'+uk'', or k'' for mass; its d^3/24 error applies uniformly
   to every true A. No derivative of A or analyticity is assumed.

3. **Complete analytic bounds and arithmetic.** The differentiated
   theta operator is P -> (1/2-2v)P+2vP', giving precisely the three
   displayed polynomials. For n>=6 and 0<=u<=8, exp(u/2)<=exp(4),
   v>=pi n^2>108, v^m exp(-v) decreases for m<=4, and successive
   majorants have ratio <=(7/6)^8 exp(-39)<1/2. The first majorant
   is bounded using 108<36pi<144, yielding all three stated tails.
   The order-zero tail is nonnegative; the derivative tails require
   both signs. L016 justifies termwise derivatives. Directed sums,
   four-corner products, zero-separated reciprocals and the three
   square sign cases enclose real interval extensions. Exact sign
   copying avoids default-context negation. Correct nearest-even exp
   is widened by adjacent representable numbers at both endpoints;
   directed exp is not assumed. Machin's alternating series encloses
   pi, and the degree-99 Taylor remainder bounds both direct trig
   calls. Simultaneous angle addition uses the old sine and cosine;
   adding the global Lipschitz radius covers the entire cell, including
   the last cell. There is no periodic reset or discarded uncertainty.

4. **Independent implementation and all-cell evidence.** Run
   `python3 scripts/theta-allocation/audit_first_period.py` with no
   existing audit output; it preserves the original certificate and
   refuses to overwrite its own report. This separately coded
   55-digit interval implementation imports neither `certify.py` nor
   `first_period.py`. It independently encloses pi with 150 arctangent
   terms and uses the displayed polynomials. On exactly the original
   mesh it checks inclusion in every saved theta value/derivative,
   tail error/contribution, head trig box, descending H box, signed
   primitive prefix, q, layer, remainder and raw integrand. It also
   checks all sums, both masses, normalization, reported radii, original
   source hashes, and preservation of the original certificate bytes.
   Higher precision tests the saved 45-digit enclosures; no new mesh,
   frequency, period, adaptive refinement or sign search is introduced.

   The full report is
   `scripts/theta-allocation/first-period-independent-audit.json`:
   `INDEPENDENT_ALL_CELL_INCLUSION_AUDIT_PASS`, no failures. Its
   complete category counts certify 4096 tail cells, 65536 head cells
   and each of the four 65536-cell primitive inductions, with 73728
   independent kernel evaluations. All 303616 audit divisions have
   zero-separated denominators; their smallest magnitude exceeds
   0.0021436243445167175923226681955798443181005527. The saved head
   k lower bound and Z lower bound remain those stated above. Audit
   contexts have precision 55, Emin=-999999999, Emax=999999999,
   clamp=0, and FLOOR/CEILING/HALF_EVEN rounding. CPython 3.15.0,
   C Decimal 1.70 and libmpdec 4.0.1 are recorded. Only Inexact and
   Rounded occur in both original and audit contexts; all exceptional
   flags are false. Full counts, flags, telemetry and the complete
   error budget were inspected, not a sampled or floating preview.

The final interval and normalized radius are unchanged. In particular
the positive lower endpoint is greater than the required threshold
zero, validating rejection of the selected negative witness. No
mathematical or executable correction was needed. Independence is
limited to the local derivation checks and separately written
implementation: both numerical programs use the same imported Decimal
backend and named analytic inputs. Their source proofs, backend
conformance and formal verification are not established by this audit.

## Mathlib

Full matching-result and supporting interval/Decimal coverage have
not been checked. L016 retains its supporting theta references;
they do not formalize this grouped integral. No absence or formal
verification claim is made. The imported named numerical/analytic
inputs and the explicit domain specialization above are the stated
basis of this computer-assisted local result.
