# Corollary919r: fixed two-region signs and one-removal decrease

## Hypotheses

Use the actual K of L019 and Xi of L058, with
Xi(z)=integral_0^infinity K(t)cos(zt)dt. Set X=[14,29/2] and

    I_x(u)=integral_0^infinity K(t+u)cos(xt)dt,
    J_x(u)=(I_x(u)-I_x(0))/u, u>0,
    J_x(0)=integral_0^infinity K'(t)cos(xt)dt.

The finite certificate assumes correct CPython integer/Fraction arithmetic
and libmpdec directed basic operations, representable neighbors and
correctly rounded HALF_EVEN exp. These are C919f's explicit contracts,
not an independent verification of the backend. Actual runtime:
CPython3.15.2, libmpdec4.0.1, precision80. Only Inexact and Rounded flags
were set. All constants displayed as terminating decimals are rationals.

For the residual-kernel conclusion additionally fix any actual root
14<x<29/2, Xi(x)=0, and use C919m's smooth even positive kernel G_x.
Multiplicity is unrestricted. No root census, simplicity, first-zero,
RH, or all-degree positivity hypothesis is used. C919n is context only.

## Conclusion

Subject to the arithmetic contracts, on the complete closed boxes,

    J_x(u)>23/100, x in X, 0<=u<=1/16,
    I_x(u)>9/10^9, x in X, 1/16<=u<=1.                    (1)

In particular both exceed the fixed preregistered thresholds 1/100 and
1/10^12, respectively. The J definition is a continuous extension of
the divided cosine integral, including u=0, with cancellation before
error estimation. For every root specified above,

    G_x'(0)=0,     G_x'(u)<0 for every u>0.                (2)

Thus the even G_x is strictly decreasing on [0,infinity). This is a
source-covered REPRODUCTION specialization. Separate conceptual audit2253
below accepts the proof and complete certificate under the stated
arithmetic contracts. Arbitrary-removal shape
preservation, an all-degree bridge, and RH remain unresolved.

## Proof

### Imported results, and the specialization required here

Use the fundamental theorem of calculus, Strang--Herman, *Calculus
Volume1*, Section5.3, Theorems5.4-5.5:
https://openstax.org/books/calculus-volume-1/pages/5-3-the-fundamental-theorem-of-calculus .
Use differentiation under an integral with continuous integrand and
parameter derivative and integrable parameter-independent majorants:
K. Conrad, *Differentiating under the integral sign*, Theorem12.3,
printed p16, author-hosted30-page version inspected21November2026,
https://kconrad.math.uconn.edu/blurbs/analysis/diffunderint.pdf .
Conrad refers out for its proof. Dominated convergence, signed Fubini
under absolute integrability, and Tonelli for nonnegative majorants
are the standard named theorems, as stated in T. Tao, *245B notes0*,
1January2009, Theorem3(4)-(5), Theorem4(1)-(2):
https://terrytao.wordpress.com/2009/01/01/245b-notes-0-a-quick-review-of-measure-and-integration-theory/ .
The notes omit these general proofs; no independent reproof is claimed.

For composite Simpson use a real C4 integrand on [a,b], positive even M,
and the bound (b-a)^5 sup|f''''|/(180 M^4). Source: NIST DLMF3.5(ii),
(3.5.6)-(3.5.8), citing Davis--Rabinowitz(1984), pp57-58,
https://dlmf.nist.gov/3.5.ii . For real Taylor with Lagrange remainder
use Strang--Herman, *Calculus Volume2*, Section6.3, Theorem6.7:
https://openstax.org/books/calculus-volume-2/pages/6-3-taylor-and-maclaurin-series .
Only smooth real intervals are used. These tools were covered by
assessment2249 before this invocation. Neither sign in (1) is supplied
by those general theorems; effective constants and closed-box coverage
are the specialization proved below.

C919m imports G. Csordas, *Fourier transforms of positive definite
kernels and the Riemann xi-function*, arXiv:1309.0055v2,21February2014,
Theorem4.1 and (4.2), printed p10, https://arxiv.org/pdf/1309.0055v2 .
With K(u)=4 Phi(u/2), K is smooth and even, positive, strictly decreasing
for u>0, and each derivative has decay of every exponential rate.
The Wintner/Spira original proofs remain unread; the precise named
restatement, not an independent recertification, is the input.
C919m supplies G_x'=-x^2 I_x, its exact entire quotient and its root
boundary condition. C919o's analytic-exterior proof supplies I_x(u)>0
for all x>0,u>=1, including1, using its proved K''>0 on that ray and
Tuck's strictly decreasing-amplitude sine-transform theorem. The exact
source is E.O. Tuck, *On positivity of Fourier transforms*, Bull.
Austral. Math. Soc.74(2006),133-138, pp133-134,(1)-(4):
https://doi.org/10.1017/S0004972700047511 . No compact signs or derivative
constants in this file are inferred from that exterior assertion.

### Endpoint and differentiability, without dividing independent errors

For every m and B>0 the imported derivative decay and continuity give
|K^(m)(s)|<=D_m(B)exp(-Bs), s>=0. Hence for t>=0, u in [0,1],
and r in [0,1], |K^(m)(t+ru)|<=D_m(B)exp(-Bt). Polynomial factors
in t remain integrable. This verifies all qualitative domination for
the u and x differentiations used below. Finite sums are smooth.
The infinite derivative series are legitimate on compact s intervals:
each differentiated summand is a polynomial in n times exp(-c n^2),
for c>0, and those majorants are summable. Quantitative tails follow
in the next subsection.

FTC gives exactly, for u>0,

    (K(t+u)-K(t))/u = integral_0^1 K'(t+ru)dr.             (3)

The preceding integrable majorant, also on the finite r interval,
permits signed Fubini. It identifies J with both the nominated divided
integral and integral_0^1 integral_0^infinity K'(t+ru)cos(xt)dt dr.
Dominated convergence as u decreases to zero proves the stated J_x(0)
and continuity, uniformly with respect to x in the compact X.
Interior differentiation uses the cited theorem; the continuous
one-sided derivatives at u=0 follow from the same FTC and dominated
convergence argument. Thus no open negative-u neighborhood is assumed
when applying a parameter theorem at the boundary. Real x derivatives
are valid in an open neighborhood of X.

Define S_x(u)=integral_0^infinity K(t+u)sin(xt)dt. Integration by
parts, justified by derivative integrability and vanishing infinity
endpoints, gives

    I_x'(u)=-K(u)+x S_x(u),
    S_x'(u)=-x I_x(u),
    I_x''(u)+x^2 I_x(u)=-K'(u).                          (4)

At t=0 the cosine boundary is -K(u), and the sine boundary is zero.
These identities hold also for nonroots in the fixed parameter box.

### Complete derivative/index/spatial bounds

Write v=pi*n^2 exp(2s) and

    K_n^(m)(s)=exp(s/2-v)P_m(v),
    P_0(v)=8v^2-12v,
    P_(m+1)(v)=(1/2-2v)P_m(v)+2v P_m'(v).              (5)

This follows by finite differentiation; the program constructs exact
rational coefficients p_mk through m=17. P_2=32v^4-224v^3+330v^2-75v
also agrees with the exterior input. Put

    A_m=sum_k |p_mk|(4k)^k, with the k=0 factor equal to1.

For k>0 the maximum of v^k exp(-v/4) is (4k/e)^k, and for k=0
the bound is1. Therefore each summand has absolute value at most
A_m exp(s/2-3v/4). For n>=5, using pi>3, exp(2s)>=1+2s,
n^2>=25+10(n-5), and exp(-45/2)<1/2, the geometric sum gives

    sum_(n>=5)|K_n^(m)(s)|
       <= 2 A_m exp(-225/4)exp(-112s), s>=0.             (6)

The coefficient of s before the last relaxation is 1/2-(9/2)n^2
<=-112. Summability is absolute, so this is also a uniform bound for
the derivative series. It applies pointwise at every Taylor center.
With a translation u>=0, its complete t^j integral bound is

    B_index(m,j)=2 A_m exp(-225/4) j!/112^(j+1).         (7)

For all n>=1, n^2>=1+3(n-1) bounds the corresponding geometric sum by
2 exp(-(9/4)exp(2s)); its ratio is at most exp(-27/4)<1/2.
For s>=4, s/2<=exp(2s)/4 and
exp(2s)>=exp(8)(1+2(s-4))>256(1+2(s-4)), since exp(1)>2.
Consequently

    sum_(n>=1)|K_n^(m)(s)|
       <=2 A_m exp(-512)exp(-1024(s-4)), s>=4.          (8)

For the whole spatial tail t>=4, translation s=t+u only decreases
this envelope. Its t^j integral bound is

    B_space(m,j)=2 A_m exp(-512)
        *sum_(k=0)^j binom(j,k)4^(j-k) k!/1024^(k+1).  (9)

The elementary exponential moment integrals follow by repeated
integration by parts with vanishing endpoints. Equations(6)-(9) hold
for every m=0,...,17 and every required j, with every theta index
included. They are new specialized bounds, not automatic reuse of
C919f's undifferentiated constants.

For the finite n<=4 sum on each closed cell [l,r] of [0,5], let
v_lo<=pi*n^2 exp(2l), v_hi>=pi*n^2 exp(2r). A whole-cell bound is

    E_m(l,r)=sum_(n=1)^4 exp(r/2-v_lo)
                              sum_k |p_mk|v_hi^k.      (10)

All operations are rounded upward. The1280 cells have width1/256.
Sum E_17/256 over [0,4], and add (7),(9) at m=17,j=0 to obtain
M17>=integral_0^infinity |K^(17)(s)|ds. Likewise sum r^9 E_0/256
and add the m=0,j=9 tails for M9>=integral t^9 K(t)dt. The full saved
bounds imply

    M17<9.691e24,     M9<0.000133370.                    (11)

The M17 omitted-index contribution is less than8.803e15, not zero;
it remains included despite the very loose high-derivative bound.
For all u>=0, positivity and decrease of K give
integral t^9 K(t+u)dt<=M9. Also
|I_x^(17)(u)|<=integral_0^infinity |K^(17)(t+u)|dt<=M17.
These provide complete remainders rather than compact-only bounds.

### One fixed quadrature and all parameter errors

The precomputation plan is saved in
`drafts/calculations/2026-11-21-two-region-work-2251.md`.
Run from the notebook:

    python3 scripts/real-zero-origin/two_region_2251.py

No settings were tuned. Use t in [0,4], n<=4, M=16384 Simpson panels,
precision80, c=57/4, x radius1/4 and x Taylor degree8. The u centers
are 0 and (2i+1)/32, i=1,...,15. At each center a, evaluate both
coefficient families

    C_j(a)=integral t^j K(t+a)cos(ct+j*pi/2)dt/j!,
    S_j(a)=integral t^j K(t+a)sin(ct+j*pi/2)dt/j!,
    j=0,...,8.                                         (12)

The integrals here and below have endpoints0,infinity. Their x Taylor
remainders on X have magnitude at most M9*(1/4)^9/9!, by the translated
M9 bound. This is less than1.403e-15 for each family at every center.

For Simpson errors, on a finite spatial cell use (10) for E_0,...,E_4.
For P_j(t)=t^j/j! and a t upper endpoint b, put

    P_js=b^(j-s)/(j-s)! for s<=j, else0,
    D_jk=sum_(s=0)^k binom(k,s)P_js E_(k-s),
    B_j4=sum_(k=0)^4 binom(4,k)D_jk c^(4-k).            (13)

Leibniz twice and the sine/cosine derivative bounds give the full fourth
derivative estimate B_j4. For center a use every spatial cell between
a and a+4, with b=r-a. All these endpoints lie on the 1/256 mesh.
Take the maximum of (13) over those1024 cells, multiply by
4^5/(180 M^4), and add
[B_index(0,j)+B_space(0,j)]/j!. These errors are charged on both sides
of each signed coefficient, with no cancellation assumption for omitted
regions. All144 error records, both288 quadrature/enclosure records,
and all cell bounds are retained in the certificates.

For each exact closed x cell [14+k/64,14+(k+1)/64], k=0,...,31,
interval Horner in x-c using (12), enlarged by its complete ninth
remainder, gives I_x(a) and S_x(a). Use (4) to construct interval
coefficients a_k containing I_x^(k)(a)/k! through degree16:

    a_0=I_x(a),  a_1=-K(a)+x S_x(a),
    a_(k+2)=[-K^(k+1)(a)/k! - x^2 a_k]/[(k+1)(k+2)],
    k=0,...,14.                                       (14)

The pointwise K jets in (14) use the exact rational polynomials (5),
signed interval Horner, the n<=4 sum, and (6) for the entire omitted
index tail at the center. Dependence discarded in interval operations
only widens enclosures. There is no assumption of cancellation in
these high derivatives or of Xi(x)=0 at a nonroot.

At a=0, subtract the exact constant term symbolically and divide
the Taylor polynomial by u, so

    J_x(u)=sum_(k=1)^16 a_k u^(k-1)+R_J,
    |R_J|<=M17*(1/16)^16/17! <1.477e-9.                 (15)

For u>0 this is Taylor's theorem for I with its remainder divided by u;
the sharper pointwise error is M17*u^16/17!, finite and vanishing at
zero. Continuity already proved extends (15) to zero. In particular
the independent error in a_0 is never divided by u.

On each [i/16,(i+1)/16], i=1,...,15, centered at a=(2i+1)/32,

    I_x(u)=sum_(k=0)^16 a_k (u-a)^k+R_I,
    |R_I|<=M17*(1/32)^17/17! <7.043e-16.                (16)

Each of the16 parent u intervals, including [0,1/16] for J, is covered
by32 equal closed subcells of width1/512. Interval Horner and the
appropriate complete remainder cover every value on all16384 x/u
cells. Both exterior faces, the split1/16, u=0 and u=1 are included.

### Arithmetic, actual margins, and inspection

The evaluator copies C919f's directed interval-operation definitions
and C919n's corresponding implementations. Signed products use the
needed endpoint products; positive division reverses denominator
endpoints. Exp on [A,B] uses the lower neighbor of correctly rounded
nearest exp(A) and upper neighbor of nearest exp(B). This uses the
explicit HALF_EVEN contract, not directed exp. Its documentation is
https://docs.python.org/3/library/decimal.html#decimal.Decimal.exp .
All exceptional signals other than Inexact and Rounded are trapped.

Machin pi uses80 exact Fraction atan terms at1/5 and25 at1/239, with
the next alternating term as error. Its branch identity and proof of
3<pi<22/7, pi^2<10 are the reviewed C919f constant construction; they
are reused, not newly asserted from an approximation. The script
checks those exact inequalities. The mesh angle d=c*4/M is below0.004.
Real sine/cosine Taylor polynomials of degree31, with d^32/32!
remainders, enclose the step pair. Addition-formula interval rotations
starting at(1,0) enclose all16385 node pairs; their widening is retained.
There is no builtin approximate trigonometric evaluation. Exact dyadic
nodes and shifted nodes are checked against Fraction. Positive finite
kernel factors 4v(2v-3) are checked before positive multiplication.
Moment recurrence multiplies by t/(j+1), and phase cycling uses
(cos,-sin,-cos,sin) or (sin,cos,-sin,-cos). Simpson weights are exactly
1,4,2,...,4,1, with factor4/(3M). Thus signed phase and factorial
normalizations in (12) are accounted for explicitly.

The preflight is `scripts/real-zero-origin/two_region_preflight_2251.json`,
saved before the first signed quadrature. Full coefficients, parameter
jets, closed cells, constants, hashes, flags and failures are in
`scripts/real-zero-origin/two_region_2251.json`. The262160-node pass
completed in about90seconds, with no unexpected signals and no failed
cell. The hulls of all saved enclosures are contained in

    J in [0.23259130360,0.27796018330],
    I in [9.82459613e-9,0.03315459710].                  (17)

These displayed rational endpoints are rounded outward from the full
80-digit records. The actual lower endpoints begin0.2325913036094438394
and9.824596137136438634e-9; hence (1) follows. The required lower bounds
were1/100 and1e-12, not the observed margins. All complete remainders
and derivative17/moment9 records were inspected at full precision.

Internal complete-record inspection is rerunnable as

    python3 scripts/real-zero-origin/inspect_two_region_2251.py

It consumes every1280 spatial record,288 coefficient enclosure,
512 parameter-jet record and16384 closed-cell enclosure. Its97255
checks pass with zero failures: exact Fraction polynomial recurrences,
compact-sum and remainder inclusions, all coefficient error inflations,
every parameter Horner/ODE coefficient inclusion, complete closed-cell
coverage and final positive margins, runtime counts and artifact hashes.
The summary is `scripts/real-zero-origin/two_region_inspection_2251.json`.
This does not independently recompute exponential bounds or replay the
quadrature nodes. Their validity follows from the explicit formulas,
reviewable evaluator and backend contracts. The inspection is not a
formal verification or the separate conceptual audit.

### Root conversion and both joins

By definition and L058, I_x(u)=Xi(x)+u J_x(u) for u>0. At any actual
root in the open bracket this becomes I_x(u)=u J_x(u)>0 on(0,1/16].
The second box supplies I_x(u)>0 on[1/16,1]. These refer to the same
continuous integral and both include their common face. C919o supplies
I_x(u)>0 on[1,infinity), also including the join. Consequently C919m's
exact derivative identity gives G_x'(u)=-x^2 I_x(u)<0 for every u>0.
At zero the root supplies G_x'(0)=-x^2 Xi(x)=0; C919m pays its smooth
even extension. For0<=a<b the integral of the continuous negative
derivative on(a,b) is strictly negative, proving strict decrease.
No simplicity is needed in the zero condition or in these identities.

### Scope and known traps

The result concerns a single removed real pair in one fixed bracket.
The two parameter boxes are stronger nonroot assertions; applying the
root condition occurs only in the last subsection. It is not assumed
at sampled frequencies. All infinite regions and used derivatives are
bounded, including the cancellation-sensitive endpoint. Positivity of
an integrand is not used to infer positivity of its cosine transform.
This provides a useful shape property of the actual first residual,
but neither shape preservation after a second removal nor positivity
of all algebraic mixed determinants follows. The generic-model stops
and approval-loop stops2238/2241/2243/2246/2248 remain intact. No complete
RH candidate, proof or disproof is asserted, and no novelty beyond the
checked sources is certified.

### Separate conceptual audit2253 — 21 November2026

**Decision and scope.** Accept (1)-(2), retaining precisely the arithmetic
contracts, actual-root premise and source qualifications above. No error
was found and no box, split, cutoff, degree, mesh or threshold was changed.
This validates the existing finite specialization; it is not a theorem
beyond the sources checked or an RH candidate. The audit used the prior
SPECIALIZE2251 coverage, separately approved2252, and reused source
notes2249. No optional original source was silently treated as inspected.

**Complete analytic bounds.** Differentiating exp(s/2-v)P(v), with
v'=2v, gives exactly (5); all18 polynomials were independently reconstructed
over the rationals. The envelope uses v^k exp(-v/4)<=(4k)^k, with a
separate k=0 value1. For n>=5, its exponent is bounded above by
-9n^2/4+(1/2-9n^2/2)s. The two inequalities n^2>=25+10(n-5) and
1/2-9n^2/2<=-112 give the complete geometric bound (6), including its
factor2. Integration of t^j exp(-112t) gives (7); u>=0 only decreases
the bound. For all n>=1, the ratio bound from n^2>=1+3(n-1) gives
2 exp(s/2-(9/4)exp(2s)). On s>=4, s/2<=exp(2s)/4 and
exp(2s)>256(1+2(s-4)) give (8), hence the full binomial integral (9).
Adding the entire index and entire spatial tails double counts a
nonnegative overlap, which is harmless. No differentiated tail is dropped.

The finite-cell exponential in (10) uses r/2-v_lo, and its polynomial
uses v_hi. These bounds apply throughout each closed cell, not merely
at its endpoints. Integrating the first1024 cells and both tails pays
M17 and M9. In particular the order17 omitted-index term exceeds
8.802e15; treating it as zero would be invalid. Positivity and decrease
of the actual K, imported via C919m's cited theta theorem, pay the
translated ninth moment. Absolute derivative integration after the
change of variable s=t+u pays the translated seventeenth derivative.
The audited full bounds retain M9<0.000133370 and M17<9.691e24.

**Differentiation, normalization and zero.** The uniform majorants
D_m(B)exp(-Bt), also after multiplication by each required t power,
justify differentiation and signed Fubini. FTC first forms (3) before
any errors are taken; dominated convergence gives J at zero. This is
a one-sided endpoint argument, not an unproved open-neighborhood
application. Both integrations by parts in (4) have vanishing infinity
terms; their lower terms are respectively -K(u) and zero. Differentiating
that ODE k times and dividing by (k+2)! gives exactly (14), including
K^(k+1)/k!, not an unnormalized derivative. Orders0,...,15 of K suffice
for the degree16 polynomial. The full derivative17 remainder is separate.

Every x coefficient in (12) has its j! denominator and phase j*pi/2;
the ninth remainder has 9!, and the spatial remainder has17!. At zero
the *exact* constant I_x(0) cancels. Its enclosure is retained when
forming higher ODE coefficients but is never divided by u. The
pointwise divided remainder is M17*u^16/17!, which tends to zero.
Thus (15) applies at zero by the already established continuity.
The remaining spatial centers have radius1/32 and use (16). All
Taylor segments stay on the nonnegative half-line where the estimates
hold. No root condition is used in either box computation.

**Independent arithmetic implementation and full consumption.** Run:

    python3 scripts/real-zero-origin/audit_two_region_2253.py
    python3 scripts/real-zero-origin/reinspect_two_region_2253.py

The first program independently implements interval operations at
precision110 with the same stated backend contracts. It reconstructs
the original exact Machin bounds and encloses pi more narrowly using
100 and35 terms. It recomputes all23040 finite derivative-cell bounds,
256 signed kernel jets with full index tails, both integrated tail
families and all144 coefficient-error records. Its fourth-derivative
bound uses the single multinomial Leibniz sum over a+b+c=4,
4!/(a!b!c!)*t^(j-a)/(j-a)!*E_b*(57/4)^c, with a<=j. This independently
checks every whole-interval maximum used in (13). All reconstructed
bounds are no greater than their saved2251 upper bounds.

The new node pass uses exact rational step-trigonometric Taylor sums,
full degree31 remainders and interval rotations. It evaluates the kernel
as exp(s/2)*(8v^2-12v)*exp(-v) and moments as exact t^j/j!, independently
of the original evaluator's factorizations and moment recurrence.
All262160 nodes are included. Every one of its288 signed quadrature
intervals is contained in the corresponding saved2251 interval, and
the same holds after adding the complete coefficient errors. Higher
precision is solely a verification of the original enclosures, not a
replacement sign pass with altered mathematical settings.

The independently implemented layer passes27220 checks, zero failures.
Full recomputed bounds, jets, quadratures, signals, hashes and runtime
are saved in `scripts/real-zero-origin/two_region_audit_2253.json`.
It uses CPython3.15.2/libmpdec4.0.1; only Inexact and Rounded flags occur.
All other signals are trapped, including underflow, subnormal and
float conversion. Exp enclosures use neighbors of HALF_EVEN results;
correctly directed exp is never assumed. The pi branch justification
and elementary trig identities remain the C919f inputs stated above.

The second program is an explicitly labeled copy of the already
inspected exact-rational checker with a separate output path, not a
second independent implementation. It consumes the complete2251
records and repeats all97255 inclusions, with zero failures, in
`scripts/real-zero-origin/two_region_exact_cells_2253.json`. It checks
the512 parameter jets, all16384 closed cells, complete coefficient
inflations, error propagation and hashes. The first program supplies
the exponential/envelope/quadrature layers this checker alone omits.
Its exact index checks establish that the32 x cells cover [14,29/2],
the32 origin cells cover [0,1/16], and the15*32 remaining spatial
cells cover [1/16,1], with all shared faces included. The original
lower hulls still exceed23/100 and9/10^9, hence also the preregistered
1/100 and1/10^12. Full relevant records were consumed; a positive
preview was not used as verification. Neither implementation verifies
the common integer/Decimal backend or constitutes formal verification.

**Root-qualified assembly.** C919m's substitution t=u+v gives precisely
G_x'=-x^2 I_x with this K and this cosine normalization. At an actual
root, L058 gives I_x(0)=Xi(x)=0, hence I_x(u)=u J_x(u)>0 on(0,1/16].
The two closed certificates agree as statements about the same integral
at1/16. C919o's exterior proof uses K''>0 on the full ray u>=1,
so -K'(u+t) is positive strictly decreasing and integrable. Its sine
theorem applies for every x>0, including the join u=1; it supplies
the remaining ray without a compact-gap assumption. At zero the exact
root gives G_x'(0)=0; C919m already supplies the smooth even extension.
Integration of the strictly negative continuous derivative on any
nontrivial interval proves the asserted strict decrease. No simplicity,
first-root identification, numerical near-zero or additional zero
census is used. Repeated-removal shape and all-degree positivity remain
independent gaps. The DAG's existing inputs are sufficient and unchanged.

## Mathlib

Full matching theorem and supporting coverage were not checked in this
step; availability is unknown. A generic integration or Taylor theorem
would support the cited tools and would not establish the specialized
theta signs or the numerical backend. Documentation reference:
https://leanprover-community.github.io/mathlib4_docs/ .
