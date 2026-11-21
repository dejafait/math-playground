# C998w: Original-measure residual validation on three support grids

## Hypotheses

Use C998v Section2's explicit positive measure, independently of any
actual-Xi or signed-scalar assumptions:

    J in {256,512,1024}, j=J,...,2J-1,
    t_j=(4j+1)/(2J)-3, nu_J=sum_j [16J/(4j+1)^2] delta_(t_j).

Sections1-8 use S equal to the real polynomials of degree<=34; Section9
explicitly changes S to degree<=28 on the remaining blocks. Let

    j_i=J+floor(i(J-1)/128), i=0,...,128.

All129 indices are distinct original support points. The quadrature
weights u_i are the exact finite decimals in the corresponding
`candidate_weights_decimal` array of the certificates
`scripts/separation-seven/support-grid-nnls-731-k8.json`,
`scripts/separation-seven/support-grid-nnls-731-k9.json`, and
`scripts/separation-seven/support-grid-nnls-731-k10.json`.
The normalized coordinates and masses are exact rationals. Decimal
interval validation assumes correctly directed basic Decimal arithmetic
at100 digits, as in the inherited notebook convention. The80-digit
candidate solve is not an assumption of optimizer correctness.

The invocation-start assessment729, completed source comparison730,
is SPECIALIZE for this support-constrained NNLS test. Import:

- F. Piazzon, A. Sommariva and M. Vianello, *Caratheodory-Tchakaloff
  Subsampling*, Dolomites Research Notes on Approximation10(2017),5-14,
  Proposition1.2, equations(7)-(15), pp6-7/full proof,
  [published primary PDF](https://drna.padovauniversitypress.it/system/files/papers/PiazzonSommarivaVianello_2017_CTS.pdf).
  For an original positive discrete measure of mass M, nonnegative
  weights on its support and an original-measure orthonormal basis of
  S containing constants, with moment residual epsilon, the error is
  at most2(M+epsilon sqrt(M)) E_S(f)+epsilon ||f||_(L2(nu)).
- L.N. Trefethen, *Approximation Theory and Approximation Practice*,
  Chapter8, Theorem8.2/(8.2), following Theorem8.1/proofs,
  [primary book text hosted at ETH](https://people.math.ethz.ch/~hiptmair/Seminars/RAP_22/TRE13.pdf),
  PDF pp56-57: for |f|<=M on the open Bernstein ellipse E_rho,
  rho>1, degree-n Chebyshev projection error<=2M rho^-n/(rho-1).
- C.L. Lawson and R.J. Hanson, *Solving Least Squares Problems*,
  SIAM1995 reprint of1974, companion
  [NNLS.FOR](https://netlib.org/lawson-hanson/all), NNLS unit's
  main/secondary/termination loops. Only its active-set candidate
  mechanism motivates the solver here. Our normal-equation variant
  is not claimed to reproduce that implementation's numerical behavior
  or inherit an all-work bound. Independent validation below is essential.

These sources and scope restrictions were inspected730; no new source
search or general theorem reproof is undertaken731. The finite validation
is needed because floating residuals in Chebyshev or grid-orthonormal
coordinates do not meet the imported proposition's hypotheses.

## Conclusion

For each of the three stated J, precisely35 weights u_i are strictly
positive, the rest are zero, and their original-measure orthonormal
moment residual satisfies

    epsilon_J^2 <3*10^-155, hence epsilon_J<10^-70.       (1)

The prescribed per-block budget is5*10^-19. This establishes only
three finite feasibility instances of the approved129-point grid,
not all64 blocks k=8,...,71, nor affordable preparation or validation.
The61 other blocks and complete work/storage upper bounds remain
unverified. No actual full G approximation, signed scalar, S3, H2,
Xi transfer or RH claim follows. The unsuccessful separator diagnostic
does not certify any obstruction; it is recorded separately from the
successful residual validation.

Work test732 stops the unchanged731 numerical implementation: extending
its repeated35-dimensional inverse construction to the remaining61
blocks costs at least121,951,200 source units>10^8, even if all moments,
NNLS candidates and the first three certificates are supplied for free.
Section4 proves this source-specific bound. It neither invalidates(1)
nor excludes optimized inverses or different residual constructions.

If the SAME residual budget were certified on every k=8,...,71 block,
retaining j<256 exactly and dropping j>=2^72, the imported theorems
would give the zero-inclusive conditional bound

    B^2 sup_(r>=0)|G(r)-Gtilde(r)|
      < 2^37[5^-34+(5*10^-19)(1+5^-34)]
            +2^46/(4*2^72-3)
      <7.245*10^-8 <10^-7, B=2^23.                   (2)

The premise covering all64 blocks is NOT proved. Even that premise
would not pay the required complete work<=10^8 or explicit storage.
This is a partial REPRODUCTION of known methods, not progress beyond
the checked literature and not a replacement for C998v's audited rule.

Section6 certifies a necessary interpolation prerequisite for ALL61
remaining blocks: the SAME R_A from Section5 has a common positive
componentwise radius d with ||I-R_A A_k||_d<897/1000<1. Section7 now
REFUTES the prescribed positive-rule family at k=11: EVERY nonnegative
rule on those SAME35 nodes has original residual>1/1000, whereas the
budget is5e-19. Thus the contraction prerequisite does not imply
positive feasibility. The three rules(1), the conditional implication(2)
and all earlier implementation stops survive. No full-work upper bound
or full G/scalar/sign conclusion is obtained.

Section9 completes the changed-degree feasibility test740: on EVERY
k=11,...,71 block the unchanged35 labels admit29 positive weights and
six zero weights, with original-measure residual<1e-180<5e-19. Combined
with the three earlier rules and the exact prefix, these give a positive
2130-term kernel approximation with B^2 uniform error<7.291e-8<1e-7,
including zero. This is a kernel result only. Section10's audit741
stops the unchanged740 production/replay/export bundle together with
original731 production of the three retained rules: a disjoint
source-work LOWER bound is101,666,571>1e8. The older51,546,118
subtotal was inconclusive. Section11 separately stops the fixed742 single-final-export
prescription at102,628,907 units, even charging no export work. No
peak-byte upper bound or source-independent impossibility follows. The scalar,
density/mixed interactions and signs remain unresolved.

## Proof

### 1. Exact moments and the original-measure residual

Write T_n for Chebyshev polynomials, m_n=integral T_n dnu_J and

    H_ab=(m_(a+b)+m_|a-b|)/2, 0<=a,b<=34,
    r_a=sum_i u_i T_a(t_(j_i))-m_a.

The product formula2T_a T_b=T_(a+b)+T_|a-b| gives H as the
ORIGINAL-measure Gram matrix. All69 moments through degree68 are
generated by exact Fraction sums over ALL J original atoms. The
recurrence T_0=1,T_1=t,T_(n+1)=2tT_n-T_(n-1) is evaluated exactly.
Neither a smooth density nor a candidate-grid moment replaces nu_J.
For a nonzero polynomial of degree<=34, at least one of J>=256
distinct support values is nonzero. Every mass is positive, so H is
positive definite. Its mass m_0<1 since x_j=(j+1/4)/J>1 and
m_0=(1/J)sum x_j^-2<1.

If C changes the Chebyshev basis to any nu_J-orthonormal basis, then
C H C^t=I. The finite square matrix C is invertible; consequently
C^t C=H^-1. The orthonormal residual is C r, and therefore

    epsilon_J^2=r^t H^-1 r.                           (3)

This proves exactly which norm is being certified without treating
the Chebyshev residual as orthonormal or paying for an unnecessary
explicit orthonormal basis. It is finite change-of-basis algebra,
not a replacement residual theorem.

### 2. Outward validation, without trusting the NNLS candidate

The script computes an80-digit approximate inverse R of H. These
finite decimals are regarded as exact rationals, not exact inverses.
It encloses EVERY entry of I-RH using100-digit downward/upward
arithmetic, including the exact rational-to-Decimal input quotients.
Define the saved upper bounds

    e>=||I-RH||_infinity, A>=||R||_infinity,
    z>=||r||_infinity.

All row sums and residual bounds round outward. The original r is
first formed exactly from the finite-decimal weights and rational
original moments; candidate solver residuals are unused in this check.
Every certified e<1/2. With E=I-RH, the convergent Neumann series
gives H^-1=(I-E)^-1 R and

    ||H^-1||_infinity<=A/(1-e),
    epsilon_J^2<=35 z^2 A/(1-e).                       (4)

The second inequality follows from
|r^t H^-1 r|<=||r||_1 ||H^-1 r||_infinity and
||r||_1<=35||r||_infinity. The script encloses the right side of(4)
upward, including a downward denominator1-e. Its upper bounds are,
respectively for J=256,512,1024, less than

    2.872333*10^-155, 2.866627*10^-155, 8.984753*10^-156.

The full unrounded directed bounds, R, all error-entry intervals,
all exact r entries, all69 exact original moments, all129 indices
and weights are in the three certificates. Exact weight sign/count
checks pass, as do all13 validation checks per certificate. Thus(1)
holds. Candidate stationarity, raw residuals or tiny pivots are not
used as mathematical evidence.

Reproduction from the notebook directory:

    python3 scripts/separation-seven/support-grid-nnls-731.py 8
    python3 scripts/separation-seven/support-grid-nnls-731.py 9
    python3 scripts/separation-seven/support-grid-nnls-731.py 10

The solver used35/36/35 outer additions and0/1/0 secondary iterations,
within the fixed387 secondary and774 total caps. It computes raw
Chebyshev least squares, then validates against the original measure.
Its80-digit normal-equation pivot cutoff is10^-60; no precision or
candidate-grid adaptation was made. A preliminary exact separator
candidate had positive original integral in every instance, so its
negative-integral tests failed. The first-block preliminary certificate
is preserved in `scripts/separation-seven/support-grid-nnls-731.json`
and its `support-grid-nnls-first-block-731.json` copy. These false
separator tests are not proofs of impossibility or solver failure.
The initial k=10 JSON serialization hit Python's4300-digit integer
conversion limit; allowing the selected exact values to be serialized
resolved output, without changing the mathematical prescription.

### 3. Conditional zero-inclusive transfer and limits

For f_r(t)=exp[-J(t+3)r], the ellipse rho=5 has
Re(t+3)>3-(5+1/5)/2=2/5. Hence |f_r|<=1 on that open ellipse
for every r>=0, including zero. The cited analytic approximation
theorem gives E_S(f_r)<=5^-34/2, uniformly in r. Also
||f_r||_(L2(nu_J))<=sqrt(m_0). Applying the cited residual proposition
with m_0<1 and nonnegative original-support weights gives

    |integral f_r dnu_J-sum_i u_i f_r(t_(j_i))|
      <=5^-34+epsilon_J(1+5^-34).                    (5)

C998v(3) multiplies this by1/(4J) to recover the original spectral
block. Since J(t_j+3)=2j+1/2, all candidate rates are original rates.
Summing1/(4*2^k) for k>=8 gives1/512; after B^2 transfer this is2^37.
C998v Section1's unchanged decreasing-integral tail bound is
1/(4*2^72-3), valid also at zero. Substituting the prescribed
epsilon_J<=5*10^-19 gives(2), checked as an exact rational comparison
by the script. This is an implication, not certification of its
unverified61 block premises.

No inverse estimate for the original operator or actual-Xi form is
used: R is only a finite polynomial moment-matrix validation device.
The script's favorable Gram arithmetic subtotal, elimination counts
and allocated entry counts do not bound all source work or byte storage.
In particular it does not price Fraction internals, candidate/control
work, the remaining moments, directed validation, h preparation or
the full scalar. At the partial731 checkpoint the shared total cap was
neither passed nor disproved; the later source-specific stop is below.
The retained256 exact atoms are not free in any future ledger.
C998v's bisection stop and100-digit failure remain valid for728's
different implementation. The present three-instance result leaves
the original mathematical gap untouched.

### 4. Mandatory-work test732 for the unchanged numerical loops

Continue exactly the731 candidate-Gram and finite-inverse routines,
replacing direct original-support enumeration by any valid moment
preparation for k=11,...,71. Only this source-preserving continuation
is tested here. The actual731 entry point remains bounded at k<=12;
no large-block rules, moments or errors are computed in this test.
If the candidate or pivot tests fail, the prescription already fails
to construct the required full rule. Conditional on completing every
block, the following loops are mandatory, independently of its data.

The source assigns dim=DEG+1=35, then computes inverse_columns by
calling solve(hd,e_j,list(range(dim))) separately for each j=0,...,34.
There is no shared factorization or multi-right-hand-side solve. For
each call n=len(active)=35. The elimination updates are

    for k in range(n):
        for i in range(k+1,n):
            for j in range(k+1,n+1):
                a[i][j] -= factor*a[k][j]

The upper column endpoint n includes the right-hand side. Partial
pivoting changes matrix entries, not these loop lengths. For fixed k,
there are (34-k)(35-k) updates. Thus a complete call executes

    sum_(k=0)^34 (34-k)(35-k)
      =sum_(m=1)^34 m(m+1)=34*35*36/3=14280

updates, and one inverse executes35*14280=499800 updates.

Use the source-operation convention fixed in C998v Section5: a scalar
arithmetic operation/comparison, explicit binding/store or successful
loop advance costs at least one unit. Count just FOUR distinct units
per update: the multiplication, subtraction, binding the inner-loop
variable j, and its successful loop advance. Do not charge the matrix
entry store, the solve_steps counter, pivot searches, factor divisions,
back substitution, other loop control, inverse-error validation,
moments, candidate generation, reporting, replay or storage. Even if
the three existing certificates are free, the remaining61 inverses
therefore require at least

    61*35*14280*4=121951200>100000000.                 (6)

For all64 inverses this same subtotal is127948800. These are lower
bounds, so excluding the other required tasks cannot restore the cap.
A premature arithmetic exception is a construction failure, not an
escape yielding a successful cheaper full rule.

There is also a conservative arithmetic-only check for preparation of
all64 blocks from scratch. The candidate Gram forms129*130/2=8385
entries, each with35 scalar products and at least34 additions (the
possible addition to the initial zero is omitted). This costs at least
8385*69=578565 arithmetic operations per block. The inverse update
products/subtractions cost another2*499800=999600. Their total is

    64*(578565+999600)=101002560>100000000.            (7)

This check omits all assignments and control. The sharper(6) suffices
even if earlier successful instances may be reused without cost.

Reproduction:

    python3 scripts/separation-seven/support-grid-work-stop-732.py

Its certificate `scripts/separation-seven/support-grid-work-stop-732.json`
binds the complete relevant source excerpts to their SHA256, verifies
the fixed parameters/loop shapes/inverse calls, independently enumerates
the finite update count, and records both lower bounds. All15 static
source/count checks pass. Complete load-bearing source_work,
independent_arithmetic_only and checks values were inspected732;
previews and the earlier favorable subtotal were not used as proof.
The static checks support the displayed source argument; they do not
verify numerical feasibility or prove bounds for a redesigned program.

This is an informative implementation stop within the approved residual
test, not a lower bound for all degree34 grids, positive quadrature,
shared factorizations, parameter-uniform validation, or compiled
implementations. There is no full G rule or actual-error claim for
the untested61 blocks and no byte-storage upper bound. The three finite
rules and the conditional implication(2) survive. The scalar, density,
signed S3, H2 and actual-Xi/global gaps remain unchanged. No progress
beyond the checked general mathematical methods is claimed.

### 5. Fixed-support anchor test734: equal-radius inclusion fails at k=11

This subsection is independent of the repeated-inverse source stop in
Section4. Keep degree34 and the original discrete measures of Section1,
now with the35 k=10 active LABELS in their saved order:

    29,36,21,15,46,55,64,10,74,83,6,92,3,100,107,40,113,1,
    25,118,122,125,0,69,127,51,87,18,128,96,2,8,120,124,104.

For each J=2^k, interpret label i as j_i=J+floor(i(J-1)/128),
t_i=(4j_i+1)/(2J)-3. Let A_k have entries

    (A_k)_(a,i)=T_a(t_i), 0<=a<=34.

These are35 distinct original nodes, so A_k is nonsingular by
polynomial interpolation. Let H_k be the ORIGINAL-measure Gram matrix
in Section1. In this subsection R_A and R_H mean exactly the two
finite-decimal matrices in the `anchor` object of
`scripts/separation-seven/fixed-support-shared-734.json`. They are
generated ONCE at k=10 by the256-digit single augmented eliminations
in `scripts/separation-seven/fixed-support-shared-734.py`. There is
no per-block inverse or NNLS. Numerical inverse accuracy is not
assumed: all entries are exact finite real inputs to validation.

Import S.M. Rump, *Verification methods: Rigorous results using
floating-point arithmetic*, Acta Numerica19(2010),287-449,
DOI10.1017/S096249291000005X,
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
Sections10.3-10.5, Theorems10.2/10.6/10.8 and(10.14), internal
pp52-53/55-59. Assessment732/comparison733 inspected the statements,
proofs and interval-input cases. Theorem10.2 validates an inverse
bound when ||I-RA||<1. Theorem10.6 validates a solution from the
strict inclusion R(b-Ax0)+(I-RA)X subset int(X); Theorem10.8 covers
outward interval inputs. These are known finite-system results, not
new theorems here. A shared chosen preconditioner is allowed; their
criteria need not succeed.

The fixed first prescription saved before calculation in
`drafts/2026-11-13-fixed-support-shared-test-734.md` uses the UNWEIGHTED
infinity norm and equal-radius centered boxes X=[-r,r]^35, r>0.
It fixes anchor k=10, precision256,64 Euler--Maclaurin order,256 log
terms and at most15 candidate residual iterations; no support,
precision, anchor, norm or preconditioner adaptation is allowed734.
Stop at the first failed contraction criterion, after checking both
systems on that instance. This is only one sufficient-certificate
prescription inside the general source-backed family target.

The anchor data pass outward validation:

    ||I-R_A A_10||_infinity <=5.99856e-254,
    ||I-R_H H_10||_infinity <8.913e-180.

For k=11 the shared Gram preconditioner still passes,

    ||I-R_H H_11||_infinity <0.274.

But for E=I-R_A A_11 its row with zero-based index33 satisfies the
EXACT rational comparison

    1.58635 < sum_(j=0)^34 |E_(33,j)| <1.58636.          (8)

In particular ||E||_infinity>1.58635>1. This is not the inference
that an overestimated interval upper bound happened to exceed1.
The selected exact absolute sum, all35 exact error entries and all
outward error-entry intervals are saved in the certificate. The
separate `fixed-support-row-replay-734.py` reconstructs integer
Chebyshev coefficients, evaluates by rational Horner rather than the
constructor's value recurrence, and checks every one of the35 error
entries and(8) exactly. All10 replay checks pass. The full selected
`/blocks/0/exact_failed_row/absolute_sum` and replay checks were
inspected, not accepted from a preview. No solver residual is used.

For completeness, (8) also rules out the prescribed equal-radius
inclusion, for ANY candidate x0 and right side b. Indeed the exact
range of row33 of EX on X=[-r,r]^35 is

    [-r sum_j|E_(33,j)|, r sum_j|E_(33,j)|].

Each coordinate of X can independently attain the sign chosen by
that row, so both endpoints are attained. Adding the fixed residual
R_A(b-A_11 x0) translates this interval and does not change its width.
By(8) its width exceeds2r, the width of row33 of X; it therefore cannot
be contained in the interior of X. Any outward interval extension
contains this exact range and cannot remedy the width obstruction.
This short local calculation identifies which of Rump's sufficient
tests fails; it does not reprove his verification theorems.

Moment evidence and scope: the script encloses all69 original moments
for the anchor and k=11. It extends C998v Section2's finite telescoping
power sums through q=66, using exact Fractions for positive powers and
the Euler--Maclaurin correction/remainder. The logarithm is enclosed
by its256-term series with the same positive explicit tail. Finite
binomial and integer Chebyshev transformations retain all cancellation
in256-digit directed intervals. All69 anchor intervals separately
contain the exact moments of the old k=10 certificate. This reference
check does not replace the original-measure moment formula for k=11.
The inherited correctly directed Decimal arithmetic qualification
remains. The load-bearing obstruction(8) uses only rational nodes and
finite-decimal R_A and is independently exact.

Reproduction from the notebook directory:

    python3 scripts/separation-seven/fixed-support-shared-734.py
    python3 scripts/separation-seven/fixed-support-row-replay-734.py

The test stops at k=11 before candidate weights or residual iterations.
Only two anchor inverses and four35-by35 matrix validations are run;
k=12,...,71 and their moments are not computed. Six constructor checks
and ten independent exact-row replay checks pass. No negative weight,
failure of unequal-radius interval inclusion, ill-posedness or failure
of the fixed support as a quadrature set has been proved.

The preliminary full61-block product-work LOWER bound is62,769,000
source units, below1e8; it is not a cost pass. For each of the
61*2*35^3 scalar terms in the two validation products, the source
charges four directed arithmetic operations, one c binding, two a/b
bindings, one sign comparison, two lo/hi stores, one k binding and
one successful loop advance:12 distinct units. This omits other
control, row norms, moments, anchor construction, candidate iterations,
Fraction/integer internals, output and storage. Their complete upper
ledger and a byte-storage upper bound are not established. No earlier
728/731 coefficient-production cost is declared free; the reference
certificate is an incremental check only. Failed inclusion already
stops this fixed prescription before a complete-cost claim.

The negative result is a local verification-method obstruction, not
progress beyond the checked general methods, and does not invalidate
the three rules in Sections1-3. A distinct componentwise-radius test
could still satisfy Rump10.6 with the SAME preconditioners: (8) does
not exclude |E|d<d for a positive vector d. Such a test was not run734;
it needs a fixed finite prescription, simultaneous coverage of all61
blocks and its own paid work. This is a specific refined mechanism,
not continuity as a substitute for positive margins. Full G/kernel
error, rounded-weight signs/residuals, density/scalar preparation,
remaining9e-7, S3/H2/Xi and global assembly all remain open.

### 6. Common componentwise interpolation contraction735

**Hypotheses and scope.** Use EXACTLY Section5's ordered35 labels,
the original floor indices j_i=J+floor(i(J-1)/128), J=2^k,
k=11,...,71, and A_k=(T_a((4j_i+1)/(2J)-3))_(a,i).
R_A is the exact finite-decimal matrix in the `anchor` /
`interpolation_preconditioner` field of
`scripts/separation-seven/fixed-support-shared-734.json`.
No inverse is recomputed. No original moments, Gram matrices or
weights for new blocks are an input to this subsection. The ready
assessment732/comparison733 explicitly covers this Rump interval-box
specialization; reuse the precise citation in Section5.

Let M be the finite-decimal35-by35 nonnegative matrix in
`/common_absolute_upper_matrix`, and let d be the35 exact finite
decimals in `/prefix_radius_tests/60/trials/2/d`, of
`scripts/separation-seven/fixed-support-componentwise-735.json`.
These field paths define all coefficients completely, without rounding
their printed values. Define ||x||_d=max_i |x_i|/d_i. The result is

    d_i>0, |I-R_A A_k|<=M entrywise for EVERY k=11,...,71,
    q=max_i (M d)_i/d_i <897/1000<1,                  (9)
    hence ||I-R_A A_k||_d<=q for EVERY such k.         (10)

The common q is approximately0.896315812809559; (9), not that preview,
is the exact certified comparison. In particular the centered
homogeneous boxes satisfy (I-R_A A_k)[-d,d] subset int([-d,d]).
This certifies the interpolation contraction prerequisite only;
R_A(b-A_k x0) is not zero in general and no residual-centered solution
box or positive weights are claimed here.

**Fixed finite calculation.** The saved prescription is
`drafts/2026-11-13-fixed-support-componentwise-test-735.md`.
At256 digits, reuse734's directed product routine to enclose EVERY
entry of E_k=I-R_A A_k. In increasing k, accumulate the entrywise
maximum of the absolute upper bounds. For each prefix start d=1;
compute y=M d upward, testing all35 strict y_i<d_i. On failure set
d_i=1+(9/8)y_i upward and repeat, with a fixed15-check cap. No
support/anchor/precision/preconditioner adaptation occurs. All61
prefixes pass: k=11,12 on check2 and k=13,...,71 on check3. Only the
final common M,d are needed for (9); earlier prefix radii are not
silently substituted block by block.

**Independent exact verification.** The separate
`scripts/separation-seven/fixed-support-componentwise-replay-735.py`
does not import either constructor or use its interval arithmetic.
It reads R_A and d as exact rational finite decimals and chooses
common positive denominators L_R,L_d, so R_A=r/L_R, d=s/L_d
with integer r,s. For Q=2J, h_i=4j_i+1-6J, integer Chebyshev
coefficients and homogeneous Horner evaluation produce integers

    a_(a,i)=Q^34 T_a(h_i/Q).

This identity follows directly from integer polynomial evaluation:
a degree-a numerator is multiplied by Q^(34-a). Thus EVERY exact
entry of E_k has numerator

    e_(i,j)=delta_(i,j)L_R Q^34-sum_a r_(i,a)a_(a,j)

and denominator L_R Q^34. Integer cross multiplication checks all
74,725 entries against both saved directed endpoints and M. Exact
positive s_i then gives each weighted row ratio as

    sum_j |e_(i,j)|s_j / (L_R Q^34 s_i).

The replay checks all2,135 ratios<1, saves each exact ratio and a hash
of each complete error matrix. It ALSO independently computes all35
exact (M d)_i/d_i, verifies every final directed y upper bound, and
checks their maximum q<897/1000 by exact cross multiplication. The
complete exact q and all15 replay checks were inspected at their
selected JSON fields; every check passes. Original floor indices,
all61 actual blocks, input hashes, matrix dimensions and d_i>0 are
checked. The exact-integer replay therefore establishes (9) without
assuming correct Decimal rounding for this contraction result.

For any real x, |E_k x|<=M|x|<=||x||_d M d proves (10) and strict
homogeneous inclusion. To specialize the imported Rump Theorem10.2,
put D=diag(d), Atilde=A_k D and Rtilde=D^-1 R_A; then
I-Rtilde Atilde=D^-1 E_k D has ordinary infinity norm<=q<1.
This is the applicability argument for the weighted norm, not a
reproof of the source theorem or a positivity theorem. Rump10.6's
nonhomogeneous residual inclusion and weight signs are still unpaid.

Reproduction from the notebook directory:

    python3 scripts/separation-seven/fixed-support-componentwise-735.py
    python3 scripts/separation-seven/fixed-support-componentwise-replay-735.py

Both write their full same-stem JSON certificates. The constructor's
seven checks and the replay's15 checks pass. No extra original
moments, Gram validation, weights or original-measure residuals are
generated735. The k=11 equal-radius obstruction in Section5 remains
true: changing to a nonconstant radius is essential to this result.

**Cost and limitations.** Executed subtotals are2,615,375 directed
matrix-product terms,221,725 radius-product terms and4,200 radius
updates, with zero new inverse calls. Counting respectively at least
12,5,3 source units gives32,505,725<10^8. This is a mandatory-work
LOWER bound, not a complete upper ledger or cost pass. It omits exact
replay, Fraction/integer internals, other control/output, production of
the734 anchor and731 reference rules, all Gram/moment/weight work and
byte-storage bounds. Even a two-system full-family validation still
needs paid preparation. No full G/kernel approximation, density,
scalar, remaining9e-7, S3/H2/Xi or RH result follows. This is local
known-method REPRODUCTION progress, not a discovery beyond the
inspected verification methods.

### 7. Exact fixed-support residual obstruction736 at k=11

**Hypotheses and conclusion.** Use exactly Section5's35 labels,
now at J=2048, with original measure nu_J, original nodes and S of
degree<=34 as above. For ANY nonnegative real weights u_i on these
35 nodes (zeros allowed), let epsilon be their original-measure
orthonormal moment residual, as in(3). Then

    epsilon>1/1000>5*10^-19.                           (11)

This rules out the prescribed family already at its first new block,
independently of finite precision, inverse construction, candidate
iterations, conditioning or work cap. It does NOT rule out the full
129-point grid, changed or enlarged supports, signed weights, other
compression mechanisms, or RH. This is a finite feasibility negative
within the source-backed SPECIALIZE target, not a new general theorem.

**Bounded numerical stage.** The prescription saved before work in
`drafts/2026-11-13-fixed-support-gram-weights-test-736.md` reuses734's
exact R_A,R_H and735's FINAL common d,M without regenerating735.
At precision256 it encloses the69 original moments and H_11 using
the already justified Section5/C998v Section2 recipe. The same
shared Gram preconditioner passes ||I-R_H H_11||_infinity<0.274.
Fifteen fixed candidate updates x<-x+R_A(b_mid-A_mid x), starting
at zero, produce exact finite-decimal rounded weights x. With the
ORIGINAL interval residual b-Ax, z=R_A(b-Ax), q bounding the saved
||M||_d, and t=(9/8)max_i |z_i|/d_i/(1-q), the directed check

    |z|+M(td)<td

passes in every coordinate. Rump Theorem10.6/(10.14), via the diagonal
scaling already justified in Section6, encloses the exact interpolation
solution in x+[-td,td]. But coordinate30, label2, is negative:

    x_30 approximately -0.00110501335277,
    (td)_30 <3.484*10^-19,
    x_30+(td)_30 <-1/1000.                            (12)

The midpoint preview is not a sign certificate: the directed full
solution box and the independent exact calculation below establish
the sign. The sufficient rounded-residual estimate(4) is
epsilon(x)^2<4.628234*10^-35, above the required upper threshold
2.5*10^-37. This failed UPPER estimate alone does not establish a
genuine residual violation for the signed candidate. Indeed the
coarse Chebyshev lower test does not certify such a violation.
The family calculation stops here; k>=12 are not tested736.

**Exact polynomial certificate, independent of Decimal.** Let i_*=30
(zero-based), with label2 and original index j_*=2079. For real t put

    y=(J/2)(t+3)-1/4,
    p(t)=product_(i!=i_*) (y-j_i)/(j_*-j_i).

All35 j_i are distinct, so p is a well-defined degree34 polynomial.
At an original atom t_j=(4j+1)/(2J)-3, y=j exactly. Consequently
p(t_(j_i))=1 for i=i_* and0 for the other34 prescribed nodes.
Define the ORIGINAL integrals

    I=sum_(j=2048)^4095 [32768/(4j+1)^2] p(t_j),
    N=sum_(j=2048)^4095 [32768/(4j+1)^2] p(t_j)^2.

The exact integer/Fraction calculation in
`scripts/separation-seven/fixed-support-separator-replay-736.py`
certifies

    I<-1/1000, 0<N<1.                                (13)

To specify the finite certificate fully, form the integer polynomial
P(y)=product_(i!=i_*)(y-j_i) and nonzero integer D=P(j_*).
Its35 ascending integer coefficients, D, all35 exact cardinal values,
ALL2048 integer values P(j), and the full exact fractions I,N,I^2/N
are saved in
`scripts/separation-seven/fixed-support-separator-replay-736.json`.
Every P(j) is independently evaluated by integer Horner and the
integer product and the two answers agree on every original atom.
The original positive mass is exactly32768/(4j+1)^2; no moment
enclosure, density limit, inverse or numerical residual is used in
these sums. Exact rational cross multiplication verifies(13) and
I^2/N>10^-6>(5e-19)^2. The exact I also lies inside the numerical
coordinate30 box in(12), a consistency check rather than a premise.
All15 checks, including input binding to the unchanged labels and
all floor indices, pass; the full checks and small rational bounds
were inspected, not inferred from previews. Thus(13) has independent
exact arithmetic verification under Python integer/Fraction semantics.

For completeness the separator implication is finite
Cauchy--Schwarz, the same diagnostic used in731, not an imported
positivity assumption. Write p=sum_a c_a phi_a in ANY original-measure
orthonormal basis of S. Such a basis exists by the positive definiteness
proved in Section1. Then sum c_a^2=N. If Q(f)=sum_i u_i f(t_(j_i)),
the cardinal identities and nonnegativity give Q(p)=u_(i_*)>=0.
Writing e_a=Q(phi_a)-integral phi_a dnu_J, one has

    -I <= Q(p)-I = sum_a c_a e_a <= sqrt(N) epsilon.

Since I<0 and0<N<1, this implies epsilon>=(-I)/sqrt(N)>1/1000,
proving(11). It applies to arbitrary nonnegative weights, not merely
the failed fifteen-step candidate. Numerical inclusion is therefore
unnecessary for the final obstruction. Section1's source residual norm
is exactly the norm in this argument; a raw Chebyshev norm is not
substituted. No extension of a literature theorem is asserted.

Reproduction from the notebook directory:

    python3 scripts/separation-seven/fixed-support-gram-weights-736.py
    python3 scripts/separation-seven/fixed-support-separator-replay-736.py

The numerical constructor has six integrity checks passing, together
with three explicitly FAILED feasibility checks (rounded signs,
exact-solution signs, sufficient residual upper threshold). The exact
replay has15/15 checks passing. Its success certifies the negative
result(11); it does not turn the failed positive-rule test into a pass.

**Accounting and limits.** The numerical execution plus735's recorded
production subtotal is at least33,326,300 source units. This charges
new Gram-product terms at12 units, candidate dot/radius terms at5,
candidate updates at2, interval-vector terms at7, and includes735's
32,505,725 rather than declaring it free. This is ONLY a LOWER bound:
it omits Fraction/integer internals, all moment preparation, reference
and anchor production, exact diagnostic, other control/output and byte
storage. The two full-family product subtotal62,769,000 is also only
a lower bound. Observed output sizes875828 and269162 bytes are file
sizes, not peak-memory bounds. No full construction was completed,
so no cost/storage upper claim is needed to conclude its failure.

Preserve the earlier independent729/732 implementation stops,734's
equal-radius stop,735's contraction prerequisite and Sections1-3's
three positive rules. The new obstruction ends the SAME35-support
family for its stated residual budget. Signed S3, H2, density/mixed
interactions, other entries/endpoints, remaining9e-7 and actual-Xi/global
assembly are still open. This is local checked-method specialization,
not progress beyond the general verification or quadrature sources.

### 8. Every one-label extension fails at the original residual tolerance738

**Hypotheses and conclusion.** Fix J=2048, the original positive measure
nu_J of Section1, S of degree<=34 and the35 ordered labels of Section5.
For EACH unused label l in {0,...,128}, add the original index

    q_l=J+floor(l(J-1)/128).

There are94 choices. For ANY nonnegative real weights on these36
original nodes, including arbitrary zeros, the ORIGINAL-measure
orthonormal residual satisfies

    epsilon>1/10000>5*10^-19.                         (14)

Thus no one common added label can meet the approved residual target
for all k=11,...,71: every choice already fails at k=11. This excludes
approximate positive rules at the stated tolerance, not only exact
moment matching. It does not exclude two added nodes, different base
supports, lower polynomial degrees, the full129-node cone or other
compression mechanisms. There is no full G approximation or S3/H2/Xi
sign conclusion. The conclusion has independent exact arithmetic
validation and does not assume correct Decimal rounding.

**Imported method and precise instance specialization.** Reuse the
invocation-start SPECIALIZE assessment736/comparison737. Stephen Boyd
and Lieven Vandenberghe, *Convex Optimization*, CUP2004, Section4.1.3,
p132 and Section4.2.4, pp142-143,
[author book PDF](https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf),
parametrize a consistent equality system by any particular solution
plus its complete nullspace. The particular solution need not be
nonnegative. No positive-base quadrature extension theorem is used.
The following verifies rank and specializes that general statement;
the exact residual diagnostic is the finite Cauchy--Schwarz argument
already justified in Section7, not a new general positivity theorem.

Let p_i be the degree34 cardinal polynomial at the35 retained nodes,
i=0,...,34 in Section5 order, and set

    w_i=integral p_i dnu_J, v_i=p_i(t_(q_l)).

The square evaluation matrix A is nonsingular by interpolation at35
distinct real nodes. Polynomial interpolation gives A v=a, where a
is the extra Chebyshev evaluation column. Consequently [A a] has
rank35, its kernel is exactly span{(-v,1)}, and ALL exact-matching
weights have the form

    (w-s v,s), s real.

Completeness follows also directly: A u+s a=m implies
u=A^-1 m-s v=w-s v. The identity A w=m follows by integrating each
Chebyshev interpolation formula. Nonnegativity requires s>=0,
s<=w_i/v_i when v_i>0, s>=w_i/v_i when v_i<0, and w_i>=0 when v_i=0.
All35 exact extra-column identities are checked for every label.

The initial finite screen uses Section7's736 containing boxes
[wlo_i,whi_i]. Its OUTER scalar interval has lower endpoint
max(0,max_(v_i<0)whi_i/v_i) and upper endpoint
min_(v_i>0)whi_i/v_i, with the zero constraints checked separately.
It contains every feasible scalar because dividing by a negative
number reverses the inequality. Every one of the94 outer intervals
is empty. No candidate solve or later block is run. This screen alone
would exclude exact matching only; the next independent validation
is essential for(14).

**Exact support-nonnegative duals.** Coordinate30 is Section7's
negative-integral cardinal polynomial. If v_30>=0, use p=p_30. If
v_30<0, choose b attaining the incompatible outer lower constraint
with v_b<0 and a attaining the outer upper constraint with v_a>0,
and use

    c=-v_a/v_b>0, p=p_a+c p_b.

At the extra node p=0. At the35 retained nodes its values are1 at a,
c at b and0 elsewhere. In the first case its retained values are the
cardinal values and its extra value is v_30>=0. Hence p is nonnegative
at ALL36 allowed nodes. The certified boxes select these witnesses;
they are not premises of the exact validation below. In particular
no35-node separator is transferred without checking the new node.

For each label the full certificate specifies the chosen cardinal
coordinates and positive coefficients, all35 exact Chebyshev
coefficients c_r of p, and every exact support value. Put

    I=integral p dnu_J, K=sum_(r=0)^34 |c_r|.

The finite exact computation, independently replayed, verifies for
ALL94 labels

    I<0, K>0, p>=0 on all36 nodes, (-I)/K>1/10000.    (15)

These are rational comparisons, not rounded previews. Since all
original nodes lie in(-1,1), |T_r|<=1 gives |p|<=K there. Section1's
original mass bound0<nu_J(R)<1 implies ||p||_(L2(nu_J))<K.
If phi_r is any original-measure orthonormal basis of S, write
p=sum c'_r phi_r. Its norm is sqrt(sum |c'_r|^2). For any allowed
nonnegative rule Q, Q(p)>=0 and finite Cauchy--Schwarz yields

    -I<=Q(p)-I<=epsilon ||p||_(L2(nu_J))<epsilon K.

Combining with(15) proves(14). This applies to every nonnegative rule
on the support, whether or not it matches any moments exactly.

**Complete finite evidence.** The constructor
`scripts/separation-seven/one-label-extension-738.py` first evaluates
each cardinal p_i at each added original node by exact rational
products. It checks all35 extra-column identities by exact Chebyshev
recurrence, and records all94 scalar intervals, including failures.
For the residual proof it independently recomputes the original
cardinal integrals without interval moments, R_A or any inverse.
With y=(J/2)(t+3)-1/4, form

    P_i(y)=product_(h!=i)(y-j_h), D_i=P_i(j_i)!=0,
    L=lcm_({2048<=j<=4095})(4j+1)^2,
    S_r=sum_(j=2048)^4095 [32768 L/(4j+1)^2] j^r.

If P_i(y)=sum a_(i,r)y^r, then its exact original integral is
sum a_(i,r)S_r/(L D_i). These are finite identities at EVERY original
atom, since y(t_j)=j and the original mass is32768/(4j+1)^2.
All35 coefficient arrays, D_i, all35 exact integrals, L and all35
integer S_r are saved. Exact Chebyshev multiplication separately
produces the cardinal coefficients. Evaluating them at all35 retained
nodes gives the cardinal identities, so uniqueness of degree34
interpolation identifies the two polynomial representations.

The independent
`scripts/separation-seven/one-label-extension-replay-738.py` imports
neither constructor nor Decimal arithmetic. It builds the FULL35-root
integer polynomial and obtains each P_i by synthetic division, checking
zero remainder and equality to the saved integer coefficients. It then
computes every original cardinal integral by DIRECT integer Horner
evaluation on all2048 atoms and weighted summation with denominator L,
rather than using the saved S_r. Every integral agrees exactly. A hash
of each complete2048-value numerator sequence is retained. The replay
also checks all35 Chebyshev cardinal identities, reconstructs all94
dual coefficients and integrals, and verifies ALL3384 support values,
all94 K bounds and all94 comparisons in(15).

Reproduction from the notebook directory:

    python3 scripts/separation-seven/one-label-extension-738.py
    python3 scripts/separation-seven/one-label-extension-replay-738.py

The full same-stem JSON certificates contain the exact evidence.
All17 constructor integrity/result checks and all14 independent replay
checks pass; the full checks and the replay's exact common threshold
were inspected. The smallest computed rational lower bound occurs at
label4 and is approximately0.000102626; only the exact common bound
1/10000 in(15) is needed. The first-pass script/JSON, preserved as
`one-label-extension-first-pass-738`, had three failed positive-rule
checks because NO label survived. Those failures are retained, not
converted into positive feasibility. The final report distinguishes
successful negative certificates from failed construction outcomes.

**Accounting and scope.** No new inverse, NNLS, later original moments,
rounded positive rule or full-family residual certificate is produced.
The abandoned fixed30-update prescription also has a source-specific
conditional full-production lower bound102,692,100>1e8. It charges
735 constructor production, a conservative subset of735 replay,
the three731 inverse loops,61 Gram products and61 fixed30 candidate
dot sequences; all other work is omitted. This secondary implementation
stop is not needed for(14), and is not a lower bound for other algorithms.
No complete work or peak-byte upper bound is claimed. Observed files
are about4.74MB and0.52MB, not memory bounds. The exact residual
obstruction ends this36-node degree34 family independently of cost.
Earlier three-block rules,735 contraction and all earlier stops survive.
This is a local REPRODUCTION/informative negative using checked standard
methods, not a mathematical advance beyond those sources or toward a
proved Xi sign. Density, mixed interactions, other entries/endpoints,
remaining9e-7,S3,H2 and actual-Xi/global assembly remain open.

### 9. Degree28 on the same35 labels: finite feasibility740, cost open

**Hypotheses and sources.** Use exactly Section5's ordered35 labels,
indices j_i=J+floor(i(J-1)/128), and ORIGINAL positive measures nu_J,
now with J=2^k, k=11,...,71 and S=P_28. The weights are the exact
finite-decimal `weights_decimal` arrays of
`scripts/separation-seven/lower-degree-fixed-740.json`. No734/735
matrix, radius, contraction or degree34 separator is an input to
this calculation. The earlier three degree34 rules remain the ones
specified in this lemma's hypotheses. Retain B=2^23 and the unchanged
tail after j=2^72-1. Directed basic Decimal arithmetic at256 digits,
and320 digits in the independent moment regeneration, is an explicit
qualification, not an independently proved property of the runtime.

Invocation-start assessment738/comparison739 approves this exact
SPECIALIZE test. Import Piazzon--Sommariva--Vianello2017,
Proposition1.2/(7)-(15), pp6-7, for arbitrary constant-containing
finite spaces; Trefethen Chapter8, Theorem8.2, projection equation
(8.2), PDF pp56-57, for arbitrary degree; and Rump2010,
Theorems10.2/10.8, Sections10.3-10.5, for square interval-Gram
validation. The primary URLs and precise qualifications are given
above in the Hypotheses and Section5. Trefethen(8.3) is the
INTERPOLANT bound with numerator4M, not the projection bound used
here; the earlier hypothesis citation has been corrected. The
Householder candidate follows the Lawson--Hanson1995 companion
NNLS/H12/G1 mechanisms, including rectangular rank termination and
secondary corrections. It supplies finite numbers only; neither
optimizer correctness nor a complexity theorem is assumed.

**Original moments and rank.** Generate57 Chebyshev moments through
degree56 by C998v Section2's finite recipe, extending its finite
power-sum identities through q=54. Both inverse-power moments use
the63 correction terms, order128 periodic-Bernoulli remainder and
256-term logarithm enclosure already justified there. No smooth
density or original-support enumeration substitutes for nu_J.
The Gram matrix is

    H_ab=(m_(a+b)+m_|a-b|)/2, 0<=a,b<=28.

Every nonzero polynomial of degree<=28 is nonzero at some one of
J>=2048 distinct original atoms; all masses are positive. Thus H
is positive definite. The29-by35 candidate evaluation matrix has
row rank29: any polynomial in its left kernel vanishes at35 distinct
points, hence is zero. No inverse of this rectangular matrix is used.
Section1's finite orthonormal-change-of-basis identity therefore
applies in dimension29: for the ORIGINAL moment residual r,

    epsilon^2=r^t H^-1 r.

**Bounded construction and validation.** The constructor uses one
256-digit incremental Householder NNLS candidate per block, in the
saved label order. It fixes main-loop cap210 and the source's
secondary cap3*35=105. Every block actually takes30 main visits and
29 secondary visits, terminating at row-rank29, with29 strictly
positive output weights and six exact zeros. No degree, support,
precision or optimizer sweep is made. Even a source-translation
error in candidate generation would not imply correctness; the
independent finite checks below are essential.

Generate ONE29-dimensional finite-decimal preconditioner R at k=11
using one elimination with all29 right sides. For every block enclose
every entry of I-RH, and let

    e=max_a sum_b |(I-RH)_ab|, A=||R||_infinity,
    z=max_a |sum_i u_i T_a(t_i)-m_a|.

The same R validates every block, with outward e<149/1000<1.
The imported square-system bound and the residual identity give

    epsilon^2 <=29 z^2 A/(1-e) <10^-360,
    hence epsilon<10^-180<5e-19.                         (15)

Every weight sign is an exact finite-decimal sign. All57 original
moment intervals, R, all841 Gram-error entry intervals per block,
all29 residual intervals, exact rational squared-error bounds,
indices, nodes, candidates and iteration histories are saved in
the constructor certificate. Thus raw Chebyshev residuals, rank
termination or a favorable floating norm are not proof premises.

`scripts/separation-seven/lower-degree-replay-740.py` imports NO
constructor code. It regenerates the57 moments at320 digits using
normalized power sums with h=1/J and endpoints u=1+h/4,v=2+h/4:

    s_q=[v^(q+1)-u^(q+1)
         -sum_(l<q)binom(q+1,l)h^(q-l)s_l]/(q+1).

Here s_q=(1/J)sum x_j^q; this is C998v's exact finite telescoping
identity after normalization. It evaluates the inverse-power
corrections as exact Fractions, the logarithm by an independently
implemented positive interval series, and T_n(2x-3) directly by
integer polynomial recurrence. Every regenerated interval is
contained in its saved original-moment interval. The finite support
and all remainders have the same hypotheses as C998v; no asymptotic
or limiting measure is introduced.

For the Gram and residual replay, saved finite decimals are converted
to exact integers on a common denominator10^600; each conversion is
checked to be exact. The replay checks all61*29^3=1,487,729 product
terms and ALL51,301 saved Gram-error intervals by integer arithmetic,
all1769 residual intervals by exact rational polynomial evaluation,
every sign, row sum and rational bound in(15). All610 block checks
and seven global checks pass, with no failed checks. Its exact
largest squared bound is approximately1.819150080838025e-445;
the proved displayed threshold in(15) is deliberately much looser.
The exact maximum, not its decimal approximation, supplies the
comparison. Full values and per-block checks are in
`scripts/separation-seven/lower-degree-replay-740.json`.

**Complete kernel error.** For every r>=0 use f_r(t)=exp[-J(t+3)r].
The SAME rho=5 ellipse has Re(t+3)>2/5, hence |f_r|<=1. Trefethen
(8.2) at n=28 gives approximation error<=5^-28/2. Since nu_J has
mass<1 and ||f_r||_(L2(nu_J))<1, the imported residual proposition
gives block error<=5^-28+epsilon(1+5^-28). This verifies the changed
degree rather than transferring Section3's degree34 number.

Retain j<256 exactly, use the three old35-node rules for k=8,9,10,
the61 new29-positive-node rules for k=11,...,71, and omit j>=2^72.
Rates remain the original a_j=2j+1/2; original spectral weights are
u_i/(4J)>0. The number of positive exponential terms is

    256+3*35+61*29=2130.

Write eta=5e-19 and b_n=5^-n+eta(1+5^-n). C998v(3) and its
zero-inclusive tail estimate give the EXACT rational upper bound

    B^2 sup_(r>=0)|G(r)-Gtilde(r)|
      <=2^46 [sum_(k=8)^10 b_34/(4*2^k)
                   +sum_(k=11)^71 b_28/(4*2^k)]
           +2^46/(4*2^72-3)
      <7.291e-8<1e-7.                                (16)

The exact-prefix error is zero. The constructor and independent
replay separately check the rational sum in(16); its approximate
early/new/tail contributions are6.012975e-8,9.051104e-9 and
3.725291e-9 respectively. This argument covers r=0 and all r>=0,
without differentiating G, interchanging an uncontrolled series,
or replacing the derivative measure by its atoms. It now establishes
an actual kernel approximation, whereas the degree34 full-block
implication(2) still has false support premises in its stopped family.

**Work/storage limits.** The pricing artifact
`scripts/separation-seven/lower-degree-ledger-740.json` records a
disjoint source-work LOWER subtotal51,546,118:24,472,346 in selected
new constructor loops,19,340,477 in the integer Gram replay, and
7,733,295 in mandatory production of the three earlier rules.
The last number uses Section4's inverse-update and candidate-Gram
counts only; the earlier coefficients are not declared free.
The ledger script states each charged operation and all omissions.
Its subtotal is below1e8 and proves NEITHER affordability NOR a
cost obstruction. Missing costs include moment preparation, integer/
Fraction/Decimal internals, remaining candidate/validation/control,
the exact prefix, allocation, output, replay and the rest of old
production. No complete upper bound has been established.

The five coefficient/replay certificates occupy38,575,203 bytes on
disk, including the three old rules. The new constructor retains
102,602 Gram-error endpoints,6954 moment endpoints and2135 candidate
weights including zeros. These are explicit subinventories and file
sizes, not a peak-entry or peak-working-byte upper bound. A later
full ledger must price the complete production and validation, not
reuse these successful coefficients at zero cost.

Reproduction from the notebook directory:

    python3 scripts/separation-seven/lower-degree-fixed-740.py
    python3 scripts/separation-seven/lower-degree-replay-740.py
    python3 scripts/separation-seven/lower-degree-ledger-740.py

This completes the degree28 finite feasibility/error portion of the
approved target, leaving its complete cost/storage portion unfinished.
No new impossibility, affordable scalar, density quadrature, signed
S3, H2 or actual-Xi result follows. C998r's witness,C999l(1),334
shifts,identity2187,512 modes,full K14,exact P0 and all inherited
analytic-response/neutral-core/IEEE754/Decimal/unreplayed-c_* contracts
remain. This is a local REPRODUCTION advance under checked known
methods, not a mathematical discovery beyond those sources.

### 10. Source-work audit741: unchanged production bundle exceeds the cap

**Hypotheses and conclusion.** Retain Section9's exact numerical
prescription, all61 rules, original moments and independent replay,
and produce the earlier three rules by the unchanged731 routines.
Include740's actual checkpoint exports after each successful block
and its final export. Use C998v Section5's source-work convention:
scalar arithmetic/comparisons, explicit variable bindings/stores and
successful loop advances each cost at least one unit. In this full
ledger an explicitly declared function parameter is a variable binding
when the function is called. This charges the binding, not an additional
call instruction. It is a source-level convention, not elapsed time,
CPU instructions or a lower bound for optimized or compiled code.

For Fraction internals use the actual CPython3.15.2 implementation,
`fractions.py`, whose complete relevant functions, version, source
path and SHA256 are retained in
`scripts/separation-seven/degree28-cost-audit-741.json`. The relevant
functions are `_operator_fallbacks`' forward/reverse wrappers,
`_add`, `_sub`, `_mul` and `_from_coprime_ints`. This is inspection
of an implementation, not an imported complexity theorem. No bound
on integer multiplication or gcd internals is assumed.

Under these hypotheses the unchanged source bundle requires at least

    101,666,571 > 100,000,000                         (17)

units. Thus it fails the complete-work gate. Section9's finite
kernel result survives. This conclusion does not exclude a different
save schedule, different production or exact reproduction of the old
rules, another degree28 implementation, or the scalar itself.

**Disjoint charges.** Start from the51,546,118 LOWER subtotal in
Section9. Its selected constructor arithmetic/stores/loop control,
integer Gram replay and old inverse/candidate-Gram operations remain
charged exactly once. Add only the following excluded work.

1. The740 `save` routine executes `export(report)` before JSON output.
   For every recursive `export(v)` call, count one parameter binding.
   For each dictionary entry count k,x bindings and its successful
   comprehension advance, three units. For each list/tuple entry count
   x and its advance, two units. Ignore type tests, str conversions,
   allocations, JSON formatting, copying and disk writes. For a tree T,
   its count is1+sum(3+count(child)) for a dictionary,
   1+sum(2+count(child)) for a list/tuple, and1 for a leaf.
   Every saved block has count10,935. Original Decimal/Fraction leaves
   become JSON strings without changing container shape, so the final
   certificate suffices to enumerate these trees. All per-block data
   remain unchanged after appending their validation. Block r=1,...,61
   appears in61-r+1 successful-block exports and again in the final
   export, hence63-r times. Disregard the initial empty save, the report
   wrapper and every other report field. This yields

       10,935 sum_(r=1)^61 (63-r) =21,345,120.

   The certificate checks the complete source of `export`, the save
   call/order and the61 block shapes. Recursive and iterative tree
   counts agree; prefix-sum enumeration separately checks multiplicities.

2. For each of61*29^3 constructor Gram terms, the source executes
   `add(value,scale(H[k][j],R[i][k]))`. The signatures `scale(a,c)`
   and `add(a,b)` bind four parameters. The older nine-unit charge
   counted c's local conversion store, the sign comparison, the loop
   binding/advance, four arithmetic operations and the value store;
   it excluded these four parameter bindings. Add5,950,916 units.

3. Charge previously unpriced Fraction operations only in the old
   original Chebyshev table, its moments and original_q, and the NEW
   independent replay's Chebyshev/residual loops. Each relevant operand
   pair is Fraction/Fraction or integer/Fraction; reverse dispatch
   converts the latter to Fraction before the same arithmetic routine.
   There is no skipped zero-weight multiplication in the replay.

   A forward or reverse wrapper binds two parameters. The arithmetic
   routine binds two more. `_from_coprime_ints` binds three parameters,
   binds obj and stores two attributes, six units. In `_mul`, count
   na,da,nb,db and g1,g2 bindings (six), two comparisons and two integer
   products; including those wrapper/helper bindings gives20 even
   without cancellation branches. In the shortest `_add`/`_sub` path,
   count four numerator/denominator bindings, g, the g==1 comparison
   and FOUR integer arithmetic operations in the returned numerator
   and denominator. Together with the same wrapper/helper bindings
   this is20. The other two return paths cost at least26 and28.
   The multiplication paths cost20,24 or28. The certificate enumerates
   all source branches, retaining full function texts. Discard all gcd
   calls, gcd internals, extra conversions and one further unit: use
   the conservative common lower bound19 per Fraction operation.

   The three old blocks have256+512+1024=1792 original atoms. A degree68
   Chebyshev row has67 recurrence steps, each two multiplications and
   one subtraction. All69 moment sums have one Fraction product and
   one addition per atom, including addition to the initial Fraction(0).
   The original_q vector pairs each row with its35 Fraction coefficients,
   again one product and one addition per term. The new independent
   replay has61*35 rows of27 recurrence steps, followed by29 weighted
   residual updates, each one product and one addition. Thus the counts
   of Fraction operations are respectively

       1792*67*3=360192, 1792*69*2=247296,
       1792*35*2=125440, 61*35*27*3=172935,
       61*35*29*2=123830.

   Their sum is1,029,693, giving19,564,167 units. None of these calls
   occurs in the earlier old inverse/candidate-Gram subtotal, new
   constructor subtotal or new integer Gram-replay subtotal. Do not
   count those earlier high-level arithmetic operations again here.

4. The old inverse-update charge deliberately omitted the matrix entry
   store in `a[i][j] -= factor*a[k][j]`. Add one per update for the
   three inverses,3*499800=1,499,400. The old candidate-Gram count
   charged arithmetic only. Its35-term generator binds k and advances
   once per term, adding3*8385*35*2=1,760,850. These stores/advances
   occur outside all exact-Fraction and export work above.

Adding these five extra subtotals to the original gives exactly(17),
an excess1,666,571. All omitted work is nonnegative; in particular
no new-moment, integer-internal, JSON-output, exact-prefix, allocation
or peak-memory upper bound is needed to reject this source bundle.
There is no affordability or storage pass. Conditional on finishing
the specified numerical construction, every listed operation is
required; an earlier failure would not produce a successful cheaper
complete rule.

Reproduce the finite source/count audit, without rerunning or changing
any quadrature coefficients:

    python3 scripts/separation-seven/degree28-cost-audit-741.py

All34 source-binding, source-shape, branch and count checks pass, with
no failed checks. Complete load-bearing `/work`, `/checks` and
`/failures` were inspected, not previews. The first audit-script run
incorrectly required its conservative19-unit bound to equal the source
minimum; the actual minimum is20. Replacing equality by the appropriate
lower-bound test corrected the audit, leaving the conservative19 charge
and all numerical certificates unchanged. Static source checks support
this explicit count; they are not a fresh numerical or analytic proof.
No source-independent quadrature lower bound or RH conclusion follows.

### 11. Fixed742 single-final-export source-work stop743

**Hypotheses, scope and conclusion.** Invocation-start SPECIALIZE741,
completed comparison742, covers this exact bounded source-first test.
Retain Section9's numerical functions,35 labels, degree28 for every
k=11,...,71,256-digit construction,320-digit independent regeneration,
residual/error budgets and all three unchanged731 productions for
k=8,9,10. Replace only the constructor's repeated full-report saves by
742's fixed short metadata checkpoints and one terminal full export.
The actual new source files are
`scripts/separation-seven/single-export-fixed-743.py` and
`scripts/separation-seven/single-export-replay-743.py`.
No numerical production or numerical replay is run743. The unchanged740
certificates supply evidence of the unchanged successful numerical path;
the ledger charges production, rather than treating their data as free.

Use Section10's source-work convention and its actual CPython3.15.2
Fraction implementation. The complete relevant source functions and
runtime/Fraction SHA256 are recorded again in
`scripts/separation-seven/single-export-cost-audit-743.json` and match741.
The seven old741 input hashes,741's own source binding, and the three
old-rule certificate/source bindings pass. This is source inspection
and finite counting, not an imported complexity theorem. No new
analytic theorem or reproof is needed; Section9's precisely cited
quadrature/residual inputs are unchanged.

For THIS prescribed bundle, a disjoint mandatory-work LOWER bound is

    102,628,907 > 100,000,000.                           (18)

Consequently the fixed742 prescription fails the complete-work gate.
Every export, checkpoint and JSON/file operation is assigned ZERO in
this bound. Section10's repeated-export charge is not reused. This
stops an implementation, not positive quadrature, a different algorithm,
the finite kernel result, or RH. There is no complete work upper bound
or peak-working-byte upper bound, and neither is needed for this stop.

**Changed boundary and source identity.** The new constructor preserves
all original functions, including `save` and `export`, exactly as ASTs.
Its complete entrypoint is identical after deleting only `save` and
`checkpoint` calls from the comparison. All original module setup,
constants, numerical definitions, contexts and COUNT initialization
are identical, apart from the allowed new checkpoint path/schedule
and helper. The helper writes exactly the prescribed source hash,
schedule, state, last validated k, three validation booleans when
available, failure labels and COUNT copy. It retains no numerical
arrays or restart state, and does not change report/block numerical
data or Decimal contexts. The former `save` changed only the report's
count snapshot and output; no numerical routine reads that snapshot.

There are four syntactic short-checkpoint sites (initial, candidate
stop, after validation, certificate stop) and exactly one full `save`,
outside the block loop and context after normal completion or either
handled stop. The retained report is exported there in full with the
original `export`, `json.dumps(...,indent=2)` and newline. A hard
interruption leaves only short metadata, with no free resume or
completed certificate. Progress-print data are unchanged. The new
replay text differs only in its description and constructor input path;
its existing `INPUT.with_suffix('.py')` check binds the new constructor.
No terminal743 numerical artifact is fabricated or copied from740.

**Disjoint retained charges.** Reuse Section10's proven components
EXCEPT its21,345,120 repeated-export charge. The retained units are

| Source region | LOWER units |
| --- | ---: |
| Section9 original selected constructor/replay/old-rule loops | 51,546,118 |
| Constructor Gram `scale`/`add` parameter bindings | 5,950,916 |
| Section10 previously unpriced Fraction calls | 19,564,167 |
| Old inverse entry stores | 1,499,400 |
| Old candidate-Gram generator bindings/advances | 1,760,850 |
| Retained subtotal, with all output free | 80,321,451 |

These execute unchanged under the new schedule. Section10 gives their
complete operand cases, source operations and exclusions. Its export
calculation is checked as historical evidence only, never included in
(18). No stop for the changed schedule follows by merely subtracting
exports from the old total: the following additional mandatory work
is essential.

**Previously omitted exact-rational regions.** Charge only add/sub/mul
calls in FOUR further source regions, disjoint from every retained
region. In the constructor, `data` builds35 degree28 Chebyshev columns
per block: each of27 recurrence steps executes two Fraction products
and a Fraction subtraction. In `validate`, each of29 exact residual
sums has35 Fraction products and35 Fraction additions, including the
addition to Fraction(0). No part of this exact residual is a constructor
Gram interval-product term. The corresponding replay support/residual
work was charged in Section10; constructor and replay are different
executions and neither is counted twice.

In constructor `moments`, for p=0,...,54 the power-sum expression is

    (v**(p+1)-u**(p+1)
       -sum_(l<p) comb(p+1,l)*sums[l])/(p+1).

All u,v and sums entries are Fractions. Count one integer/Fraction
product and one Fraction addition per inner term, and the two outer
Fraction subtractions for each p, even p=0. In replay `regenerate`,
the independent normalized recurrence has inner terms

    comb(p+1,l)*h**(p-l)*power_sums[l].

Here h=Fraction(1,J) and p-l>=1. Count TWO Fraction products and
one Fraction addition per inner term, and again the two outer
Fraction subtractions per p. No power, division, conversion, binomial
computation or other source loop/binding is charged in these regions.

All counted operands are Fraction/Fraction or integer/Fraction.
Section10's inspected `_operator_fallbacks`, `_add`, `_sub`, `_mul`
and `_from_coprime_ints` therefore give at least19 units per call:
the complete inspected source-path minima remain20,26,28 for add/sub
and20,24,28 for multiplication. The conservative19 discards a unit.
Do not additionally charge the enclosing high-level Fraction arithmetic
operation, since its internal units already pay that same execution.
No gcd or integer primitive complexity is assumed. Thus:

| New rational source region | Fraction operations | LOWER units |
| --- | ---: | ---: |
| Constructor support Chebyshev | 61*35*27*3=172935 | 3285765 |
| Constructor exact residual | 61*29*35*2=123830 | 2352770 |
| Constructor power sums | 61*(2*1485+110)=187880 | 3569720 |
| Replay power sums | 61*(3*1485+110)=278465 | 5290835 |
| Total | 763110 | 14499090 |

Here1485=sum_(p=0)^54 p. Separate loop-index enumerations in the
certificate agree with each of the four formulas. Bernoulli, inverse
moments, logarithms and most other exact arithmetic remain unpaid.

**Previously omitted instrumentation.** The original selected loop
prices in Section9 count numerical arithmetic, numerical destination
stores, loop bindings and successful advances. They explicitly exclude
the source's counter increments. Charge only the integer addition and
counter-destination store for `COUNT[...] += 1` in the constructor's
gradient, triangular and Gram loops, and `product_terms += 1` in the
replay Gram loop. These are two distinct units per occurrence, not
another price for a numerical accumulator or loop advance. Ignore all
dot/update/rotation counters and all old731 counters.

Every unchanged block's history records(main,secondary,active count)
=(i,i,i) for i=1,...,29, followed by rank termination at main visit30.
The source adds one active column per successful main visit and enters
the secondary loop at least once. With29 secondary visits in29 accepted
main visits, none of those iterations removes a column. Consequently
the gradient has active size p=0,...,28 and the first triangular solve
has size q=1,...,29. The mandatory selected counter occurrences are

    gradient: 61 sum_(p=0)^28 (35-p)(29-p) =681065,
    triangular: 61 sum_(q=1)^29 q(q-1)/2 =247660,
    constructor Gram: 61*29^3 =1487729,
    replay Gram: 61*29^3 =1487729.

Both independent nested-loop counts and the original count snapshots
agree. The Gram terms already received their nine/thirteen-unit
numerical prices, which omit these counter additions/stores. This adds

    2*(681065+247660+1487729+1487729)=7808366.

All three new classes of charges are mutually disjoint: the retained
operations, the four extra Fraction source regions, and the four
selected source counters. Combining them proves(18):

    80321451+14499090+7808366=102628907,
    excess above the cap=2628907.

All omitted work is nonnegative, including the short checkpoints,
single full export, complete JSON/string/file output, allocation,
source binding, exact256 prefix, remaining arithmetic/control and
ledger production. Runtime/internal coverage for a full upper bound
would require further inputs; no such upper claim is made. An earlier
failure does not produce successful rules more cheaply.

Reproduce only the static source/count certificate:

    python3 scripts/separation-seven/single-export-cost-audit-743.py

All75 source, hash, branch, schedule and count checks pass, no failures.
Complete `/work`, `/checks`, `/failures`, `/boundary` and `/runtime`
were inspected. Source AST equality is a boundary check, not numerical
revalidation. The retained rank2130, residual<1e-180 and B^2 error
<7.291e-8 remain Section9's qualified results. No changed coefficient,
affordable kernel preparation, density/mixed scalar, signed S3, H2 or
actual-Xi/global conclusion follows. This is a local REPRODUCTION
obstruction under the assessed standard methods, not a new general
mathematical result beyond the sources checked.

## Mathlib

Full matching coverage of the inexact positive quadrature theorem,
this original-measure residual certificate and the three explicit
finite rules has not been checked. Supporting finite linear algebra
and polynomial identities are not a claim of a full matching theorem.
Unknown coverage does not establish absence.
The source-specific operation count in Section4 has not been checked
in Mathlib and makes no claim of a general complexity theorem.
The particular shared-preconditioner row obstruction and verification
criteria in Section5 have not been checked in Mathlib; no absence
claim or full matching formalization is asserted.
The explicit common weighted contraction and exact-integer replay in
Section6 have not been checked in Mathlib. Supporting matrix or
polynomial identities do not constitute a full matching formalization.
The explicit cardinal-polynomial obstruction, all2048 original-atom
sums and numerical validation in Section7 have not been checked in
Mathlib. Finite-dimensional Cauchy--Schwarz is supporting mathematics;
no full matching formalization or absence claim is asserted.
The complete94-support residual obstruction in Section8, its direct
original-atom integer replay and source-specific work bound have not
been checked in Mathlib. General linear algebra, interpolation and
Cauchy--Schwarz do not constitute a full matching formalization; no
absence claim is made.
Section9's61 explicit degree28 rules, moment/Gram replay, uniform
kernel bound and source-work subinventory have not been checked in
Mathlib. Supporting polynomial, matrix and finite-sum results are not
a full matching formalization; unknown coverage is not absence.
Section10's source-specific work obstruction has not been checked in
Mathlib; it makes no claim about a general quadrature complexity theorem.
Section11's changed-schedule source-work obstruction and its75 finite
checks have not been checked in Mathlib; no matching formalization or
source-independent complexity theorem is claimed.
