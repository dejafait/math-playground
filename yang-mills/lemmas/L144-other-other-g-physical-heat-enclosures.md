# L144 — Complete signed G physical heat enclosures

## Hypotheses

Import L140(1),(3),(14)'s established physical form and identity
K_(i,G)=g_G B_(i,G), L141(1)'s scalar enclosure, L142(2)'s complete
cutoff-96 omission and polynomial heat sums, and L143's complete
certified spatial factors. The scope is SU(2), both actual L010 probes
i=3,6, straight direction-1 lower-rooted forest, all-face relative
fixed links on D=(-4,4)^4, and flow time 1/16. Bare small-coupling
coefficients are taken at fixed mesh before refinement. This evaluates
an established continuum functional and takes no new mesh limit.

Retain both displacement sectors and shear polarizations, every allowed
component zero index, the upper primitive's cosine and endpoint constant,
the lower constant prefix p_0, and both inverse weights. The exact cutoff
keeps every coordinate of both mode labels at most 96. Import L132's
full symmetric probe rows and bounds N_3=6050, N_6=1640736; L143's Q
rows match L133's full saved rows, whose values are not imported.

Use exactly L082's certified 644 positive time nodes/weights and 62468
heat entries, with their enclosing pairs and source hashes. Numerical
tensor inclusion uses L039's explicitly qualified IEEE binary64
addition, multiplication or FMA model, no overflow and a local 10^-290
underflow allowance. Source spatial/moment qualifications remain.
No independent processor-conformance or BLAS-verification claim is made.

## Conclusion

The complete physical forms obey the strict bounds

| Probe | B_(i,G) lower | B_(i,G) upper | K_(i,G) lower | K_(i,G) upper |
| --- | ---: | ---: | ---: | ---: |
| 3 | 2408.3740053 | 2408.3740056 | -146.92 | -103.56 |
| 6 | 5174.7326818 | 5174.7326826 | -315.66 | -222.51 |

In particular both actual G coefficients are strictly negative. Each
physical interval includes spatial uncertainty, both time integrals,
input/tensor arithmetic and the full omitted spectrum. Relative to the
saved retained center, the complete errors are respectively below
8.164e-8 and 3.44e-7, both below the requested threshold 1. No outside
factor 3 or extra color/polarization factor has been applied.

All 360 matched signed terms (72 triplet, 288 shear), 106 coordinate
features and exact interval aggregations pass the complete audit with
zero failures. This is local reproduction of standard inclusion methods
for the assessed comparison, without a claim of originality beyond the
sources checked. It determines one selected coefficient only. R, the
triplet transverse-H sign, full compensation, finer powers/logarithm,
other response jets, finite matching, interacting error <=c_box/2,
continuum axioms, reflection positivity, infrared control and finite
positive mass remain unresolved. No Yang--Mills candidate is supplied.

## Proof

### 1. Complete finite signed tensor

Use L140's exact M_G and symmetric Q_i. Its 24 signed G component
rows are the six diagonal negative-second-derivative and six mixed-
first-derivative J_T rows, each paired with both direct and negative-
prefix L_F rows. The component-1 J_T input is zero, but the component-1
right input, including its constant prefix, is retained. The upper row
is exactly j_n=[cos(n pi(x_1+4)/8)-(-1)^n]/(2 n pi/8), n>=1.
L143 certifies every spatial entry, including that endpoint constant.

Q_3 and Q_6 have 48 and 192 rows from the full L132 probe definition.
In Tr(M_G F Q_i F), a row M(alpha,beta) pairs with Q(beta,alpha).
Every such pair is retained once, with its signed rational coefficient.
Expanding this rule gives 72 and 288 products respectively. Each product
contains four one-coordinate factors with the order

    Tr[M_j E_beta(t) Q_j E_alpha(s)].                         (1)

For a component alpha, coordinate j uses the edge-cosine E basis
when j=alpha and the vertex-sine V basis otherwise. E includes index
zero; V starts at one. The exact scalar expansion of (1) is

    H_alpha(s) [M_j .* Q_j^T] H_beta(t)^T,                   (2)

where H lists the corresponding one-dimensional heat weights, and .*
is entrywise multiplication. Thus only Q_j is transposed in the
spatial product. Multiply the four coordinate expressions, multiply
the enclosed rational coefficient and integrate against both positive
time-weight vectors. The full expansion uses 106 distinct coordinate
features. Matching each component, coefficient and spatial key to
L142/L143 fixes the exact finite tensor; there is no optional extra
factor 2 from symmetric polarization. L140(14) already contains both
inverse weights exp(-lambda/16)/lambda.

### 2. G-specific complete time error

For every retained relative one-form mode,

    27/64 < lambda <= 4(96 pi/8)^2 < 96^2 < 2^14.

The positive lower bound follows from the three positive vertex indices;
the upper bound uses pi<4. Import L082(4)'s Gauss--Legendre remainder
theorem and its specialization to the entire scalar exponential: the
28-point rule on [0,2^-14] and all 22 dyadic panels through 256 has

    |lambda B(lambda)-1| <= epsilon_t,
    epsilon_t=C_28[1+22(57!)]+exp(-108),
    C_28=(28!)^4/[57(56!)^3].                              (3)

Here B(lambda) is the exact shifted-time rule, before the final-time
factor exp(-lambda/16). Its hypotheses are unchanged: lambda*2^-14<1
on the first panel; each dyadic normalized remainder is bounded by
C_28 (lambda b)^57 exp(-lambda b)<=C_28 57!, and the omitted infinite
time interval contributes at most exp(-256*27/64)=exp(-108). Thus (3)
controls both inverse weights without changing either heat exponent.
The product relative error is at most 2epsilon_t+epsilon_t^2.

Unlike a constant-amplitude physical form, L140 proves the normalized
G pair bound C_G |k|, C_G=280665. With c=9/1024, L142 gives the
complete single-label estimates

    sum_k exp(-c|k|^2) <= A=4*12^4=82944,
    sum_k |k| exp(-c|k|^2) <= B=16*68*12^3=1880064.        (4)

These sums allow all nonnegative indices in each component, so they
contain the actual relative-mode domain. The second uses |k|<=sum k_j,
S0<12 and S1<68 from L142, rather than dropping the polynomial weight.
L132's probe bound N_i and lambda/16>c|k|^2 therefore bound the
absolute complete signed pair series by C_G N_i A B. Applying (3)
to that series proves the exact spatial trace's time-error allowance

    T_i=C_G N_i A B (2epsilon_hat+epsilon_hat^2),
    epsilon_hat=C_28[1+22(57!)]+e_hat_108,                 (5)

where e_hat_108 is L082's saved rational integer-interval upper bound
for exp(-108). In particular epsilon_hat>=epsilon_t, so (5) is a
containing rational allowance, not a claim that exp(-108) is rational.

No positivity of the signed physical form is assumed. Formula (5)
controls both infinite time integrals and their corner; it uses exact
physical amplitudes, with numerical spatial uncertainties handled
separately. Certified integer evaluation of exp(-108) and exact
rational arithmetic give T_6<5.401e-8; T_3 is approximately 1.9915e-10.
No L133 constant-amplitude prefactor is assigned to G.

### 3. Qualified arithmetic inclusion

Import L143's dyadic enclosing pairs and L082's heat/weight pairs by
their exact hashes. Use L039's outward midpoint-radius add, multiply
and dot rules. For uncertain inputs (A,a),(B,b), the product uncertainty
is bounded by |A|b+a|B|+ab, with the separately bounded rounding error.
The dot estimate specializes N. J. Higham, *Accuracy and Stability of
Numerical Algorithms*, 2nd ed., SIAM (2002), Lemma 3.1: with u=2^-53,
G=nextafter(10^-12,+infinity) exceeds
(2n+2)u/[1-(2n+2)u] for n<=276. This permits ordinary multiplication/
addition or FMA and any summation order within that operation count.
Nonnegative bound operations round upward and include 10^-290 locally.

Coordinate feature inner dimensions are at most 97. The 644-by-644
time tensor is integrated in blocks of at most 160 nodes on each side;
both time dots are consequently within the same dimension hypothesis.
All centers/radii are checked finite and every radius nonnegative
throughout assembly; overflow is excluded. Induction through (2), four
coordinate products, signed coefficient multiplication, both time dots
and signed aggregation encloses the exact spatial/time-rule tensor.
Cancellation is retained in centers and is never assumed in radii.
The 29478 finite/radius checks confirm the required numerical domains;
the analytic operation bounds, rather than those checks alone, justify
inclusion under the stated IEEE model.

The final retained centers and radii, as exact dyadic rationals, are

    c_3=0x1.2d0bf7da4a523p+11, r_3=0x1.5dc74ae9b6fc1p-24,
    c_6=0x1.436bb910fec93p+12, r_6=0x1.36ed5f761d692p-22.   (6)

Both r_i<2.896e-7. These radii include spatial and all retained-rule
input/arithmetic errors; they are distinct from the analytic time error.

### 4. Omitted spectrum, scalar multiplication and exact endpoints

L142's complete omitted-spectrum bound is

    S_i=C_G N_i *185723781120/20^27,                       (7)

with S_3<2.350e-15 and S_6<6.373e-13. Its polynomial mode weight,
both omitted-label sets and all zero indices are retained. Combining
(5)--(7) gives

    |B_(i,G)-c_i| <= r_i+T_i+S_i.                         (8)

Every comparison in the conclusion is performed with exact rational
arithmetic: (6) is dyadic, (5) uses a containing integer exp(-108)
interval, and (7) is rational. The bounds in the B columns strictly
contain c_i plus/minus (8). The exact total errors are below 8.164e-8
and 3.44e-7 respectively. Refinement or a sampled time integral is not
a premise for these intervals.

Only now use L141's strict scalar interval
(-61/1000,-43/1000). Taking the minimum and maximum of all four products
of that interval's endpoints with the complete B interval endpoints
contains K_(i,G)=g_G B_(i,G). Exact comparisons put those products
strictly inside the stated G columns. Since both B lower endpoints
are positive and both scalar endpoints negative, both G signs are
negative. The scalar interval's width accounts for the much larger
coefficient uncertainty; it is not a tensor-integration failure.

### 5. Complete evidence and limitations

Reproduce from the active notebook:

    PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/enclose_g_heat_form.py
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/enclose_g_heat_form.py --audit
    PYTHONDONTWRITEBYTECODE=1 python3 scripts/combined-ward-response/check_g_heat_endpoints.py

The full certificate is
scripts/combined-ward-response/g-heat-enclosure-certificate.json.
It records every source/script/archive hash, all original rows, every
signed term and coefficient, all feature keys, (5),(7), exact endpoints,
scalar products, finite-check count and failures. The audit in
scripts/combined-ward-response/g-heat-enclosure-audit.json checks all
360 records and 106 features against the full symbolic expansion,
exact dyadic sum containment, both time/omission allowances and all
four scalar endpoint products. It has zero failures. The selected
exact readable comparisons and (6) are in
scripts/combined-ward-response/g-heat-endpoint-check.json; its complete
rows and the full audit results/summary/failure fields were inspected.
No preview is used as verification of an omitted tensor record.

L143's complete spatial replay is imported. The current audit does not
independently recompute the BLAS tensor or establish processor
conformance; inclusion rests on the stated operation-by-operation
arithmetic argument and model. The interrupted first run reached the
triplet aggregation but accessed a nonexistent tail-certificate field.
Its traceback is preserved in
scripts/combined-ward-response/g-heat-first-run-failure.txt. Reading
the correct tail/probes field repairs the lookup. The interrupted run
certifies no value; the final complete run and audit have no failures.

L124 adds G with a plus sign before its single outside factor 3.
The negative signs above do not evaluate R, resolve the triplet
transverse-H sign or prove K_(i,oo)=-4 gamma D_i. L104's limit is
imported and no general Ward/flow theorem is reproved or used to
assign an isolated coefficient. The outcome is a relevant local
standard-method reproduction, not mathematical progress beyond the
sources checked or a construction of the target theory.

## Mathlib

Full matching signed G heat-enclosure theorem: **not checked**.
Supporting finite tensor traces, Laplace transforms, Gauss--Legendre
remainder/positivity, polynomial Gaussian sums and interval/roundoff
inclusion: **not checked**. Unknown availability is not evidence of
absence. No Mathlib result is assumed as a numerical input; the named
standard theorem and precise Higham citation above are used within
their checked hypotheses.
