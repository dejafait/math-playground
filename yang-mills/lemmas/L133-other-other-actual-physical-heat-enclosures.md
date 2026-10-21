# L133 — Complete enclosures of the actual transverse-H heat contractions

## Hypotheses

Import L132(1)--(6)'s four real functionals P_(i,D), P_(i,X),
P_(i,A), P_(i,C), exact finite tensors and full omitted-spectrum bounds.
The scope is unchanged: SU(2), the actual L010 probes i=3,6, the
direction-1 straight lower-rooted forest, relative fixed-link box
D=(-4,4)^4, and bare fixed-mesh small-coupling coefficients before
refinement. Both displacement sectors, the transition region, every
relative mode, both physical transverse-H orientations and the constant
axial prefix are retained. The flow time is 1/16. Write tau_p for L132's
antisymmetric scalar tau, to distinguish it from that flow time.

Use L008(1),(6)'s actual symmetric probe polarization. Import L036's
proved degree-200 cutoff residual, L037's precise certified rule and
saved hexadecimal table, and L082 proof sections 1--4's certified
moments and positive 28-point time/heat rule. In particular L082(3)'s
quadrature bound applies for h=2,3 and |n|<=192, although its saved
degree-2/3 table used only |n|<=96. The additional moment evaluations
needed here are enclosed below; they are not assumed accurate.

Retain L039's qualified IEEE binary64 addition/multiplication/FMA model,
arbitrary summation order, no overflow, and underflow allowance 1e-290.
The computation is an informal computer-assisted inclusion under that
model, not a formal processor or BLAS verification. All numerical
premises are the exact certificate inputs and their stated enclosures;
earlier physical-contraction diagnostics are not numerical inputs.

## Conclusion

The full continuum functionals have the following strict enclosures:

| Probe i | P_(i,D) | P_(i,X) | P_(i,A) | P_(i,C) |
| --- | --- | --- | --- | --- |
| 3 | (2359.1,2359.2) | (29198.8,29198.9) | (19170.0,19170.1) | (1024.8,1024.9) |
| 6 | (703.6,703.7) | (69177.0,69177.1) | (-4195.9,-4195.8) | (3218.2,3218.3) |

Each total error against its saved exact dyadic retained center is
less than 1.44e-5, including spatial integration, both time integrals,
input and tensor arithmetic, and the complete omitted mode spectrum.
The largest error is for P_(6,X); the exact errors and centers are in
`scripts/combined-ward-response/physical-h-enclosure-certificate.json`.

Combining the full fine intervals with L132(2),(3) gives

    -3417 < K_(3,tr) < 742,
      7862 < K_(6,tr) < 13095.                         (1)

Thus the actual retained transverse-H coefficient is strictly positive
for the shear probe. The certified interval for the triplet crosses
zero, so its sign is unresolved. There is no outside color/group factor
3 in (1). This evaluates only K_(i,f)+K_(i,V)+K_(i,sc)+K_(i,en).
The five other coefficients E,ax,-Q,G,R in the complete other/other
assembly remain unevaluated. Neither (1) nor a partial group sign
determines K_(i,oo)+4 gamma D_i, cancellation of the mixed cubic group,
finer powers/logarithms, an interacting reflected bound, or the
Yang--Mills target. No candidate solution or novelty claim is made.

## Proof

### 1. Every spatial factor uses covered Fourier moments

Let omega=pi/8 and F_h(n)=integral_(-3)^3 x^h rho(x) exp(i n omega x) dx.
Use the ordinary relative sine/cosine factors, their first derivatives
and prefixes specified in L132 proof section 2. A nonzero-index factor
is a linear combination of exp(±i n omega x) with exact shift phases
i^(±n); the constant edge factor is 1/sqrt(8), and its prefix is
(x+4)/sqrt(8). Consequently every row product g is a finite sum of
x^h exp(i n omega x). Multiplication convolves its indices, and

    (x^h exp(i n omega x))'
       =h x^(h-1)exp(i n omega x)+i n omega x^h exp(i n omega x).

For a physical matrix multiply g by ell=x+4 in the axial coordinate
*before* applying integration by parts. With f=x rho, all endpoint
terms vanish by compact support, and the exact identities are

    integral rho g = sum c_(n,h) F_h(n),
    integral f g = sum c_(n,h) F_(h+1)(n),
    integral rho' g = -integral rho g',
    integral f' g = -integral f g',
    integral f'' g = integral f g''.                  (2)

Here g in (2) includes ell when present. No derivative of a prefix or
of ell is omitted. All compact coefficient factors are exactly r,r',
f,f',f''; second derivatives occur in the actual shear coefficients.

For completeness, check the maximal moment scope by coordinates.
In the three transverse coordinates every row factor has polynomial
degree zero. Their weights therefore need only h=0,1 and |n|<=2K.
The axial probe factors also have polynomial degree zero, and need
only h=0,1 up to 2K. In an axial physical factor the weight is r or f':
the transverse displacement components are u_2,u_3,u_4, whose axial
factors are respectively r,f',r, and only transverse derivatives of
those components occur. Multiplying by ell raises degree by one.
Each zero axial prefix raises it once more; a nonzero prefix is a
sine factor with a constant inverse-frequency coefficient.

With no zero prefixes, (2) needs h<=2 and |n|<=2K. With one zero
prefix, h<=3 and |n|<=K, since only the other axial row oscillates.
With two zero prefixes, the frequency is zero and g=(x+4)^3/8.
The r weight needs h<=3. For the f' weight g' has degree two, so
the extra x in f still needs h<=3, not h=4. Thus the exact necessary
moment domain is contained in

    h=0,1,2: |n|<=192;   h=3: |n|<=96.               (3)

An assertion checks (3) at every nonzero polynomial-exponential
coefficient of all matrix entries; it never suppresses a small term.
The first attempt to use only L082's saved table stopped at h=2,n=-97
in an ell*f' row product. Its full output remains in
`scripts/combined-ward-response/physical-h-enclosure-moment-coverage-failure.txt`.
This is preserved evidence against that insufficient table selection,
not a failure of (2) or a negative probe result.

### 2. Import the covered moments and enclose the additional ones

Import precisely the 1156 moment intervals in L082's
`scripts/combined-ward-response/continuum-first-pair-enclosure-certificate.json`:
h=0,1 through |n|=192, and h=2,3 through |n|=96. L037 supplies
the first two via its saved dyadic table with the full errors 1.565e-13
and 3.333e-13; the other two include L082(3)'s exact-rule allowance.
No newly regenerated approximate table is substituted.

Only h=2, 97<=|n|<=192 remains in (3). L082 proof section 2 proves,
at these same frequencies, the exact 144-point four-panel rule bound

    |F_2(n)-F_2^Q(n)| <= E_2 < 6.3e-13,
    E_2=18[epsilon+(1+epsilon)delta_t]+(125/2)delta_c,
    epsilon=3.48e-14,
    delta_t=2*3^36/(3*4^84),
    delta_c=2*3^179/(3*4^284).                        (4)

This imports L036's checked cutoff polynomial, rather than rebuilding
that approximation. The standard Gauss--Legendre exactness and positive
weights apply: 200+84+2<=287 on a transition panel and 284+2<=287
on a core panel. L082's Cauchy/Chebyshev phase majorants remain valid
because |n omega|<=24pi<76. These are exactly the hypotheses behind
(4); the new spatial weights do not change rho or the rule.

Reuse all 288 certified positive-panel node, weight and rho intervals
from L037. Evenness gives

    F_2^Q(n)=2 sum_positive_nodes weight*x^2*rho(x)*cos(n omega x).

Enclose every cosine with L037's reduced alternating Taylor and
double-angle algorithm at scale 10^180. Sum outward and add E_2
outward. Negative frequencies have the same real value and zero
imaginary part by exact parity. The certificate retains all 192
additional signed moment intervals and the exact rational allowance.
The audit recomputes all of them, with no machine-cosine assumption.

### 3. Spatial matrices, tensor assembly and complete time error

Use (2) with outward integer coefficients and moments. Multiplication,
division and addition use L037's inclusion operations; denominators
are the positive nonzero mode frequencies or norm constants. Every
imaginary interval contains zero for a real row integral. Converting
the real intervals to dyadic midpoint-radius pairs checks exact
containment, so each pair encloses the exact spatial entry.

The expansion of L132(6) has 30 distinct spatial matrices, 36/72/12/48
physical component terms for D/X/A/C, and 48/192 probe component
terms for i=3/6. These counts retain both displacement sectors and
every polarization. Reconstruct them from the displayed displacement,
curvature rows and lift rows; match the symbolic component lists and
matrix keys to L132's existing diagnostic certificate exactly. Only
its algebraic lists are used, never its spatial matrices or values.

There are respectively 144/240/48/144 and 432/864/144/576 matched
signed trace products, totaling 2592. Each matches four coordinate
factors in the precise order Tr[M_j E_beta(t) Q_j E_alpha(s)].
There are 198 distinct such coordinate features. Every component and
mode below 96 is retained, including the zero edge index.

Import exactly L082's 644 certified positive time nodes and weights
and 62,468 heat entries, including their center/radius intervals.
The archive hashes and exact arrays must match. L082(4) applies to
all retained relative eigenvalues, independently of the physical form:

    |lambda B(lambda)-1| <= epsilon_t,
    epsilon_t=C_28[1+22(57!)]+exp(-108),
    C_28=(28!)^4/[57(56!)^3].                         (5)

It covers the initial panel, all 22 dyadic panels and the omitted
time tail. No mesh-dependent cutoff or sampled eigenvalue error is
used. The eigenvalues satisfy 27/64<lambda<K^2<2^14, as required.

L132 proves the complete normalized physical amplitude bounds

    C_D=C_A=20582100, C_X=1395445968, C_C=280665,

the full-displacement probe bounds N_3=6050,N_6=1640736, and the
single-label heat sum <=4*12^4. Multiplying the two inverse-weight
errors in (5), and summing the absolute complete mode series, bounds
the exact spatial trace's time-rule error by

    T_(i,s)=C_s N_i (4*12^4)^2 (2epsilon_t+epsilon_t^2). (6)

Thus the largest time error, T_(6,X), is <1.185e-5. This uses bounds
for the exact physical and probe matrices; numerical matrix errors
are propagated separately. It controls both infinite time integrals
even though the signed integrands need not be positive.

Compute the actual time-rule tensor using L039's outward add, product
and dot rules. The dot bound specializes Higham, *Accuracy and Stability
of Numerical Algorithms*, 2nd ed., SIAM (2002), Lemma 3.1, as specified
in L039 and L082: G>10^-12 covers at most 2n+2 elementary operations
under the stated arithmetic model. Coordinate inner dimensions are
<=97. Split the 644-node integrations into blocks of at most 160,
so every dot is within L039's n<=276 scope. All centers and radii
are finite, with nonnegative radii. Induction through these operations
encloses the exact-rule tensor, with the spatial moment and matrix
uncertainties included. Cancellation is retained in the centers; the
radius propagation never assumes a term's sign or deletes a term.

### 4. Complete spectrum, endpoint comparisons and evidence

Let c_(i,s),r_(i,s) be the exact dyadic retained center/radius saved
after summing all matched products. L132's complete spectral bound
has the exact rational upper bound

    U_(i,s)=C_s N_i *2(4*12^4)(16*12^3)*512/(9*96)/20^27,

because the positive Taylor series gives e^3>20. All U_(i,s)<5e-11.
The total error is r_(i,s)+T_(i,s)+U_(i,s), compared in exact rational
arithmetic with the Conclusion's endpoints and 1.44e-5. The largest
spatial/arithmetic radius is <2.528e-6, again for P_(6,X). Every bound
includes the full omitted spectrum, not just a diagnostic difference.

Finally take all four products with L132(3)'s scalar intervals:
(h_D+tau_p), (h_X-tau_p/2), h_A and (xi+2tau_p). For intervals
[l,h] and [s,t], enclose the product by the minimum and maximum of
ls,lt,hs,ht, then add the four endpoints. The complete fine bounds
are contained in (-3417,742) for i=3 and (7862,13095) for i=6.
These endpoint comparisons are exact rational checks. The triplet
enclosure straddles zero; no claim that its true coefficient changes
sign follows. This proves (1) and the shear positivity only.

Reproduce from the active notebook:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/enclose_physical_h_contractions.py
    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/combined-ward-response/audit_physical_h_enclosure.py

Full certificate, factors and audit are
`scripts/combined-ward-response/physical-h-enclosure-certificate.json`,
`scripts/combined-ward-response/physical-h-enclosure-factors.npz` and
`scripts/combined-ward-response/physical-h-enclosure-audit.json`.
The audit recomputes every added moment and all new integer spatial
entries, checks their exact dyadic containments, all 2592 signed term
indices/coefficients and their exact interval aggregation, inherited
time-array identity, all errors and final endpoint products. It also
checks the three complete constant-prefix identities

    integral ell*p_0^2*r = (F_3(0)+12F_2(0)+48F_1(0)+64F_0(0))/8,
    integral ell*p_0^2*f' = -3(F_3(0)+8F_2(0)+16F_1(0))/8,
    integral ell*p_0^2*r' = -3(F_2(0)+8F_1(0)+16F_0(0))/8.

They follow directly from p_0=(x+4)/sqrt(8) and (2); the middle
identity in particular retains the derivative of ell. The audit
does not independently recompute the full BLAS tensor or verify a
processor. Its inclusion still relies on the arithmetic induction
above and L039's model. This is local reproduction of standard
Fourier/IBP, positive quadrature and interval methods, specialized to
the actual physical forms; no discovery beyond the checked sources
is asserted. No independent construction gap is closed by these values.

## Mathlib

Full matching actual physical heat enclosures: **not checked**.
Supporting integration by parts, finite tensor traces, Gauss--Legendre
quadrature, Fourier moments, interval arithmetic and roundoff bounds:
**not checked**. Unknown coverage is not evidence of absence. These
Python certificates are not a Mathlib formalization.
