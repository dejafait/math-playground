# L137 — Full E heat-form enclosures and opposite probe signs

## Hypotheses

Import L134(1)--(4),(9)--(10)'s established E functional, exact finite
trace and complete spectral bounds, L135(1)'s universal scalar bounds,
and L136's certified cumulative moments. The setting is SU(2), both
actual L010 probes i=3,6, the straight lower-rooted direction-1 forest,
relative all-face fixed links on D=(-4,4)^4, and flow time 1/16.
These are bare fixed-mesh small-coupling coefficients before refinement;
this lemma evaluates an established continuum functional and takes no
additional mesh limit. Retain both full displacement sectors, all direct
and prefix rows, the constant axial edge mode and R through x_1=4.
There is no outside color/group factor 3 in K_(i,E).

Use L008's full symmetric probe polarization, L132 proof section 2's
curvature and lift rows, L082 proof sections 1--4's exact saved moment
and positive time/heat inputs, and L037's integer interval inclusion.
L133 supplies the qualified tensor enclosure method, not numerical
values of these different physical forms. Keep L039's IEEE binary64
rounded addition/multiplication/FMA model, arbitrary summation order,
no overflow and local underflow allowance 10^-290. This is an informal
computer-assisted inclusion under that model, not a processor or BLAS
verification. No diagnostic approximation or source snippet is a premise.

## Conclusion

The full L134 physical heat forms have strict enclosures

| Probe i | U_i | W_i |
| --- | --- | --- |
| 3 | (1228.1,1228.2) | (22889.0,22889.1) |
| 6 | (451.5,451.6) | (-6151.3,-6151.2) |

For each form, the total error from its saved exact dyadic retained
center is less than 3.09e-7, compared with the proposed threshold 1.
The error includes spatial moment/matrix inclusion, both time integrals,
input/tensor arithmetic, and the complete omitted mode spectrum.
Combining the finer saved intervals with L135 gives

    -5184 < K_(3,E) < -4342,
       471 < K_(6,E) < 702.                              (1)

Thus E is negative for the triplet and positive for the shear. These
are signs of one term of L124's assembly only. ax,-Q,G,R and the
triplet transverse-H sign remain unevaluated or unresolved; (1) assigns
no sign to K_(i,oo)+4 gamma D_i and proves no compensation with L084.
Other jets, finer powers/logarithm, finite matching, interacting error
<=c_box/2, continuum fields/axioms, reflection positivity, infrared
control and finite positive mass remain open. No candidate exists.
This is local RESEARCH / REPRODUCTION progress by standard certified
integration methods, with no claim of mathematical originality.

## Proof

### 1. Assemble precisely the finite E tensors

Set K=96. For each transverse output component a=2,3,4, the lift row
is the direct component-a mode minus the component-1 prefix row with
its transverse direction-a derivative, as in L134 proof section 4.
Form M_U by pairing that row with itself with weight u_1, and M_W by
pairing it with itself with the respective weight W_a. With r=rho,
f=x rho, and R'=rho, these weights are exactly

    u_1=(f,r,fp,r),
    W_2=(R,fp,r,fp), W_3=-(f,r,fp,r), W_4=-(R,fp,r,fp),

where fp denotes f' and tuples mean tensor products. No ell=x_1+4
is inserted into M. The constant prefix itself still contains x_1+4.
All four direct/prefix pairings are retained for each a; each physical
matrix has 12 signed component terms. Q_3,Q_6 use the full L008
probe with L132's circulation rows: Q_3 pairs each plane curl with
itself with w_mu+w_nu, while Q_6 pairs the two curvature rows with
s_mu nu and half in each polarization order. Their 48 and 192 terms
are identical, coefficient and one-dimensional key by key, to L133's
already established full-probe tensors. There is no probe-sector swap
or symmetry deletion.

L134(10) now gives each retained form as Tr(M F Q_i F), with
F_kk=exp(-lambda_k/16)/lambda_k. Match opposing component blocks and
expand their four-coordinate tensor products. For each form there are
48 signed products for i=3 and 144 for i=6, totaling 384. The union
has 30 spatial matrix keys and 108 coordinate features. These counts
are checked against the complete symbolic term lists; every coincident
or off-diagonal exterior mode pair within the rectangular domain stays.
No extra factor 2, 3 or 6 occurs in this trace.

### 2. Enclose every spatial entry, including the upper tail

Expand the relative row functions in polynomial exponentials with
omega=pi/8 and exact shift phases i^n. Import exactly L082's 1156
F_h(n) intervals: h=0,1 through |n|=192, h=2,3 through |n|=96.
For compact weights use L082(2)'s identities

    integral rho g=sum c_(n,h)F_h(n),
    integral f g=sum c_(n,h)F_(h+1)(n),
    integral rho' g=-integral rho g',
    integral f' g=-integral f g',
    integral f'' g=integral f g''.

Every derivative acts on the entire mode/prefix product. Compactness
of rho,f and their derivatives removes these endpoint terms. For R,
use directly L136's J_h(n)=integral_(-4)^4 x^h R exp(i n omega x),
including its nonzero upper endpoint. The saved 579 J records are
replayed from the exact F inputs and pi interval before use. No new
quadrature or regenerated approximate moments enter the calculation.

In transverse coordinates the mode products have degree zero and
|n|<=192; compact f shifts the degree by at most one. In the axial
coordinate a physical row with no zero prefix has degree zero,
one zero prefix has degree one and |n|<=96, and two zero prefixes
have degree two at n=0. Compact f therefore needs at most F_3(0)
in the last case and F_2 through |n|<=96 in the middle case. The
probe has no prefixes. Differentiating row products does not increase
degree. Thus all compact moments are covered without L133's extended
nonzero degree-2 table. For R the corresponding necessary degrees and
frequencies are exactly within L136(3). Assertions check coverage at
every nonzero coefficient of every entry, never dropping a small term.

Integer interval addition, multiplication and division at scale 10^180
include every coefficient and moment. All denominators are positive
nonzero frequencies or norm constants. Each real entry's imaginary
interval contains zero; retain the real enclosure. Convert to a dyadic
midpoint-radius pair only after checking exact endpoint containment.
The separate audit recomputes all 278596 entries of all 30 matrices
and checks every dyadic containment.

Three constant-prefix identities are checked independently of mode
symbol differentiation, using p_0=(x+4)/sqrt(8) and F_h=F_h(0):

    integral R p_0^2=56F_0/3-F_2/2,
    integral f p_0^2=(F_3+8F_2+16F_1)/8,
    integral f' p_0^2=-(F_2+4F_1)/4.

The first imports L136(5), which retains the positive tail above 3.
The second follows by polynomial expansion. The third follows by
compact integration by parts: -(1/4)integral x rho(x)(x+4).
They check a load-bearing zero-mode case, not the signed heat-form
value by themselves.

### 3. Both inverse weights and the complete time error

Insert exp(-lambda/16)/lambda=integral_(1/16)^infinity exp(-t lambda)dt
on both sides of Q. Import L082's 644 certified positive nodes and
weights and all 62468 heat entries, with their exact saved center/radius
arrays and hashes. The eigenvalues of every retained relative mode
satisfy 27/64<lambda<K^2<2^14. Consequently L082(4)'s positive
28-point rule on its initial and 22 dyadic panels gives

    |lambda B(lambda)-1|<=epsilon_t,
    epsilon_t=C_28[1+22(57!)]+exp(-108),
    C_28=(28!)^4/[57(56!)^3].

These are the hypotheses of the imported Gauss remainder argument for
the scalar exponential; different physical weights do not change it.
The full omitted time interval is included in exp(-108). Applying the
relative estimate to the product of both inverse weights costs at most
2epsilon_t+epsilon_t^2. L134's exact normalized physical amplitude
bounds C_U=160380,C_W=13783770 and L132's full-probe norm bounds
N_3=6050,N_6=1640736, together with the complete one-label heat sum
<=4*12^4, therefore give the exact rational time-error allowance

    T_(i,s)=C_s N_i(4*12^4)^2(2epsilon_t+epsilon_t^2).

This estimate applies to the absolute complete mode series even for a
signed form. Its largest value, T_(6,W), is below 1.171e-7. Numerical
spatial uncertainty is propagated separately, not inserted as a presumed
exact matrix norm into this bound.

### 4. Qualified arithmetic inclusion and all-record audit

Use L039's midpoint-radius addition, elementwise multiplication and dot
inclusion operations. Their dot bound specializes N. J. Higham,
*Accuracy and Stability of Numerical Algorithms*, 2nd ed., SIAM (2002),
Lemma 3.1: G=nextafter(10^-12,+infinity) exceeds
(2n+2)u/[1-(2n+2)u] for n<=276 and u=2^-53. Nonnegative bound
operations round upward, and each propagation stage adds 10^-290.
Coordinate feature dots have inner dimension <=97; split the 644-node
time sums into blocks of at most 160, so every dot satisfies the bound.
All centers/radii are finite, radii nonnegative, and every imported
heat/weight array is identical to its certified source array.

For each coordinate feature multiply the physical spatial matrix by
the transpose of the probe matrix entrywise, then dot with the left
and right heat matrices. Multiply the four coordinate features, multiply
the enclosed signed rational coefficient, integrate against both time
weight vectors, and add every component term. Induction through those
operations encloses the exact spatial/time-rule trace. The radii retain
spatial input uncertainty, cancellations only in the centers, and every
signed product. The largest retained spatial/arithmetic radius is below
3.032e-7, for W_3; this is distinct from the largest total error W_6.
Here the subscripts 3,6 on W denote the probe, not a displacement weight.

Add L134's complete spectral allowance

    S_(i,s)=C_s N_i*2(4*12^4)(16*12^3)*512/(9*96)/20^27.

The positive Taylor series proves e^3>20, so this rational allowance
bounds the exact omitted modes. The largest S_(i,s) is below 4.580e-13.
For each saved dyadic center c and radius r compare r+T+S in exact
rational arithmetic with 3.09e-7 and compare c±(r+T+S) with the table
endpoints. Every comparison passes. The audit also checks complete
384-term coverage, all rational coefficients and exact dyadic interval
aggregation, all 108 feature keys, inherited time-array identity and
all source hashes. The strict endpoint comparisons are also recorded in
scripts/combined-ward-response/e-heat-endpoint-check.json.
It does not recompute the BLAS tensor independently;
its inclusion depends on the stated arithmetic induction and model.

Full certificate, factor archive and audit are respectively
scripts/combined-ward-response/e-heat-enclosure-certificate.json,
scripts/combined-ward-response/e-heat-enclosure-factors.npz, and
scripts/combined-ward-response/e-heat-enclosure-audit.json.
Reproduce from the active notebook:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/enclose_e_heat_forms.py
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/audit_e_heat_enclosure.py

### 5. Propagate both scalar signs without a signed-form assumption

For each probe take the saved full fine interval [l_s,h_s] for s=U,W
and L135's scalar intervals [b_s,t_s], where
(b_U,t_U)=(-903/1000,-871/1000) and
(b_W,t_W)=(-178/1000,-143/1000). Each product lies between the
minimum and maximum of l_s b_s,l_s t_s,h_s b_s,h_s t_s. Add those
endpoints for U and W, as required by L134(2). This gives containing
fine intervals approximately (-5183.244,-4342.828) and
(471.886,701.631); these displays are previews of exact rational
endpoints. The audit separately verifies the strict rational containments
in (1), which establish the signs. In particular the shear's negative
W term times negative alpha is retained and competes with beta U;
no heat-form positivity was assumed in propagation.

## Mathlib

Full matching physical E enclosure theorem: **not checked**. Supporting
finite traces/tensor products, integration by parts, finite Fourier sums,
Gauss quadrature, Laplace transforms and interval arithmetic: **not checked**.
Unknown availability is not absence. The imported standard arithmetic
method is precisely cited above; no reproof of the source results or
claim of progress beyond the checked sources is made.
