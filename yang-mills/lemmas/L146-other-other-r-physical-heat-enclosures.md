# L146 — Complete signed R physical heat enclosures

## Hypotheses

Import L145(1)--(3),(11)'s established physical form, identity
K_(i,R)=g_G B_(i,R), complete omission and finite tensor. Keep SU(2),
both actual L010 probes i=3,6, the straight direction-1 lower-rooted
forest, all-face relative fixed links on D=(-4,4)^4 and tau=1/16.
Bare small-coupling coefficients are taken at each fixed mesh before
refinement. This evaluates an established continuum functional; it
takes no new mesh limit and inserts no outside factor 3.

Import L132's full symmetric Q_i rows and mode/probe estimates,
L133's certified moment extensions and L082's saved 644-node positive
time rule and 62468 heat entries, with their exact input hashes.
Retain L141's scalar interval (-61/1000,-43/1000). Both displacement
sectors, all relative zero indices, both inverse weights and both
constant prefixes p_0=(x_1+4)/sqrt(8) remain. No upper primitive or
additional x_1+4 weight from the different G form is used.

Numerical inclusion uses L039's qualified IEEE binary64 addition,
multiplication/FMA model, no overflow and local underflow allowance
10^-290. Source moment/time qualifications remain. This is informal
computer-assisted inclusion, not independent processor or BLAS
verification. L144's checked time-rule/arithmetic specialization is
reused with the R amplitude from L145, not its G amplitude or values.

## Conclusion

The complete physical forms and coefficients have strict enclosures:

| Probe | B_(i,R) lower | B_(i,R) upper | K_(i,R) lower | K_(i,R) upper |
| --- | ---: | ---: | ---: | ---: |
| 3 | 1228.1260684 | 1228.1260686 | -74.916 | -52.809 |
| 6 | 451.5469823 | 451.5469825 | -27.545 | -19.416 |

Both actual R coefficients are negative under the stated arithmetic
model. Each physical interval includes retained spatial/time and
arithmetic uncertainty and the complete omitted spectrum. Against
the saved retained centers, total errors are respectively below
3.173*10^-8 and 1.061*10^-8, both below the requested threshold 1.

All 241347 spatial entries in 26 matrices pass full integer replay
and dyadic containment. The complete signed tensor has 192 matched
terms (48 triplet, 144 shear) and 83 coordinate features; its audit
has zero failures. This is local REPRODUCTION of standard inclusion
methods, not an originality claim beyond the sources checked.
L124 adds R positively before its single outside factor 3. No complete
compensation comparison is performed here. The triplet transverse-H
sign, finer powers/logarithm, other response jets, finite matching,
interacting error <=c_box/2, continuum axioms, reflection positivity,
infrared control and finite positive mass remain unresolved. There is
no candidate Yang--Mills solution.

## Proof

### 1. Match the exact R tensor and every spatial row

Let ordinary component-alpha modes have an edge cosine in coordinate
alpha and vertex sines elsewhere. The edge basis includes index zero;
the vertex basis begins at one. Each transverse lift component a=2,3,4
has two rows: its direct component-a mode and its negative component-1
row with axial prefix p_n and transverse derivative in direction a.
Pair both rows with both rows of that same output component, using
weight (f,r,f',r), where r=rho and f=x rho. The result is exactly
12 signed component-block rows of M_R. There is no additional axial
weight. This expands L145's sum of three squared lift components,
without assuming parity cancellation of its physical prefix.

Import all 48 Q_3 and 192 Q_6 rows from L132. Exact matching checks
their components, rational coefficients and four spatial keys against
L133's full saved Q rows. In Tr(M_R F Q_i F), a row M(alpha,beta)
pairs with Q(beta,alpha). Expanding all such pairs gives 48 and 144
signed products. Each coordinate contributes

    H_alpha(s) [M_j .* Q_j^T] H_beta(t)^T,                 (1)

where H is the corresponding one-coordinate heat vector and .* is
entrywise multiplication. The coefficient of each product is the
product of its two signed rational row coefficients. Thus only Q_j
is transposed; no optional symmetry factor is inserted. Multiplying
the four factors in (1) and integrating both times gives L145(11).
The two F factors are exp(-lambda/16)/lambda, independently retained.

For spatial integration expand each mode/prefix product g into
x^h exp(i n pi x/8) with its exact shifted phase. At n=0 the ordinary
edge is 1/sqrt(8) and the prefix is (x+4)/sqrt(8). Use L133(2)'s exact
integration-by-parts identities, differentiating the entire product:

    integral r g = sum c_(n,h) F_h(n),
    integral f g = sum c_(n,h) F_(h+1)(n),
    integral r' g = -integral r g',
    integral f' g = -integral f g',
    integral f'' g = integral f g''.

Compact support removes every endpoint term. In transverse coordinates
and in Q_i the mode product has degree zero; the required moments have
h<=1 and |n|<=192. For the axial R weight f, two positive indices
also need only h=1 through frequency 192. A zero prefix raises degree
once but removes one oscillating index, so h<=2 and |n|<=96. Two zero
prefixes give x(x+4)^2/8, requiring h<=3 only at frequency zero.
This proves coverage in L082's original domain, contained also in
L133's imported table. No new Fourier moment evaluation is required.

The symbolic containing-support check runs over every entry before
evaluation. Its complete required-domain maxima are h=0,1:192;
h=2:96; h=3:0, with no missing moment. Exact outward integer Fourier
and IBP arithmetic then encloses all 241347 entries in 26 matrices.
Every integer interval is converted to a dyadic midpoint-radius pair
only after exact rational containment. Full replay recomputes every
entry, checks the saved integer record and archive arrays and verifies
containment again. All tests pass; the largest spatial radius is
0x1.32cb9092f9a43p-27 <8.929*10^-9. The replay is corroboration within
the same program, not an independently implemented proof.

### 2. R-specific error for both complete time integrals

The retained eigenvalues obey 27/64<lambda<96^2<2^14. Import the
standard Gauss--Legendre remainder theorem as specialized in L082(4)
and L144(3): for the exact 28-point shifted-time rule on the initial
panel and all 22 dyadic panels through 256,

    |lambda B(lambda)-1|<=epsilon_t,
    epsilon_t=C_28[1+22(57!)]+exp(-108),
    C_28=(28!)^4/[57(56!)^3].

The scalar exponential is entire, the first panel has lambda*2^-14<1,
and the omitted time interval uses lambda>27/64. Hence the hypotheses
are exactly the previously checked ones. The product relative error
of the two inverse weights is <=2epsilon_t+epsilon_t^2.

L145 bounds each normalized physical mode pair by C_R=160380;
L132 gives |q_i(A_k,A_l)|<=N_i, with N_3=6050 and N_6=1640736.
The complete one-label heat sum is bounded by A=4*12^4=82944.
Therefore the absolute full pair series is <=C_R N_i A^2, and the
containing rational time allowance is

    T_i=C_R N_i A^2(2 epsilon_hat+epsilon_hat^2),            (2)

where epsilon_hat replaces exp(-108) by L082's certified rational
upper bound. This applies to a signed trace without positivity of
its physical integrand. Exact arithmetic gives T_6<1.362*10^-9;
the actual T_3 is approximately 5.021*10^-12. G's polynomial mode
weight and its different amplitude are not assigned to this form.

### 3. Retained arithmetic inclusion and exact endpoints

Import L039's outward midpoint-radius add/product/dot rules. For
uncertain inputs (A,a),(B,b), the product uncertainty is bounded by
|A|b+a|B|+ab plus separately bounded rounding. The dot rule specializes
N. J. Higham, *Accuracy and Stability of Numerical Algorithms*, 2nd ed.,
SIAM (2002), Lemma 3.1: nextafter(10^-12,+infinity) exceeds
(2n+2)u/[1-(2n+2)u], u=2^-53, for n<=276. All coordinate dots have
inner dimension <=97. Both time dots are blocked to <=160 nodes,
so the same bound applies throughout. Nonnegative bound operations
round upward with the stated local underflow allowance. All centers
and radii are finite and every radius is nonnegative.

Induction through spatial multiplication, the two coordinate dots,
the four coordinate products, signed coefficient multiplication,
both time dots and signed summation encloses the exact-rule tensor.
The 15801 finite/radius checks verify the operation domains; the
arithmetic argument, not these checks alone, justifies inclusion.
The saved centers and retained spatial/arithmetic radii are

    c_3=0x1.3308118163170p+10, r_3=0x1.106f2b421b7fap-25,
    c_6=0x1.c38c070932058p+8,  r_6=0x1.3d8483719322ap-27.    (3)

Use L145's complete omission, with its sharper probe-specific form,

    S_i=C_R N_i *2717908992/20^27.                        (4)

This is <5.329*10^-15 for either probe. Combining (2)--(4) gives
|B_(i,R)-c_i|<=r_i+T_i+S_i. Exact rational comparisons establish
the physical columns and total-error bounds in the conclusion.
Only now multiply by L141's strict scalar interval. Minimum and
maximum of its four endpoint products with the full B interval give
the R columns. Both physical lower endpoints are positive and both
scalar endpoints negative, proving the stated R signs.

### 4. Complete certificates, reproduction and limitations

Commands from the active notebook, using PYTHONDONTWRITEBYTECODE=1
and OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=VECLIB_MAXIMUM_THREADS=1:

    python3 scripts/combined-ward-response/enclose_r_spatial.py
    python3 scripts/combined-ward-response/enclose_r_spatial.py --audit
    python3 scripts/combined-ward-response/enclose_r_heat_form.py
    python3 scripts/combined-ward-response/enclose_r_heat_form.py --audit
    python3 scripts/combined-ward-response/check_r_heat_endpoints.py

Full integer entries are in
scripts/combined-ward-response/r-spatial-integer-entries.jsonl.gz;
the spatial certificate, arrays and complete replay audit use the
corresponding r-spatial-enclosure filenames. The complete signed
records, exact errors/endpoints, input hashes and source qualifications
are in scripts/combined-ward-response/r-heat-enclosure-certificate.json.
Its audit checks all 192 records and 83 features against the complete
symbolic expansion, exact dyadic aggregation, (2),(4), and all four
scalar endpoint products. It has zero failures. Exact readable
comparisons and required-domain maxima are in
scripts/combined-ward-response/r-heat-endpoint-check.json, also with
zero failures. Complete relevant results and failure fields were
inspected; previews are not used to verify omitted records.

A variable-shadowing error was found in the initial spatial certificate
writer before it completed. That run was interrupted; its partial
output and integer entries remain under r-spatial-interrupted filenames
and certify nothing. The corrected complete run and replay pass.
No independently verified processor conformance or independent BLAS
tensor recomputation is claimed. Inclusion retains the inherited IEEE
model. Standard moment/time machinery is imported rather than reproved;
the necessary application here is the different complete R tensor.
No value for the full selected-group compensation or interacting
response follows merely from these two negative coefficients.

## Mathlib

Full matching signed R heat-enclosure theorem: **not checked**.
Supporting finite tensor traces, Laplace transforms, Gauss--Legendre
remainder/positivity, Fourier IBP, Gaussian heat sums and roundoff
inclusion: **not checked**. Unknown availability is not absence.
No Mathlib theorem is assumed as a numerical input. The named standard
Gauss--Legendre theorem and precise Higham citation are applied within
their checked hypotheses; no general Ward or flow-finiteness theorem
is reproved or assigned to this isolated coefficient.
