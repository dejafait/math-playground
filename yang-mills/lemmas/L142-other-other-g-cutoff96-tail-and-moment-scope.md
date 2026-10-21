# L142 — Complete G omission at cutoff 96 and certified moment scope

## Hypotheses

Use precisely L140(1),(3),(14)'s established G functional, physical form
B_(i,G), and finite tensor, with SU(2), both actual L010 probes i=3,6,
the straight lower-rooted direction-1 forest, relative fixed-link box
D=(-4,4)^4, flow time 1/16, and the bare small-coupling coefficient
at each fixed mesh before refinement. This step takes no new mesh limit.
Retain all permitted component zero indices, the upper primitive's
cosine and endpoint constant, the lower constant prefix, both physical
inverse weights, both probe displacement sectors and both shear
polarizations. The rectangular cutoff retains every mode coordinate
at most K=96 for both labels.

Import L140 proof section 3's amplitude bound C_G |k| with C_G=280665,
its coefficient bounds N_3=6050, N_6=1640736, and its scalar bound
|g_G|<1/4. Import the relative mode heat weights and Gaussian-tail
method from L081 and L132. For retained spatial scope, import L132
proof section 2's full probe rows and L082/L133's exact compact Fourier
moments F_h(n)=integral_(-3)^3 x^h rho(x) exp(i n pi x/8) dx.
L082 supplies 1156 intervals and L133 supplies the 192 additional
signed degree-2 intervals, giving the containing domain

    h=0,1,2: |n|<=192; h=3: |n|<=96.                    (1)

These are the specific saved certified tables identified below,
with their original quadrature/input qualifications. Scope coverage
alone does not enclose new spatial matrices, time integrals or tensor
arithmetic. It does not transfer L133's numerical values to G.

## Conclusion

For both probes, the complete spectral omission in L140's physical
heat form satisfies

    |B_(3,G)-B_(3,G)^[96]| < 7518846951/(3200000000000000000000000)
                          < 2.350e-15,
    |B_(6,G)-B_(6,G)^[96]| < 3186064791063/(5000000000000000000000000)
                          < 6.373e-13.                         (2)

Thus both are below the requested 1e-9. Multiplication by |g_G|<1/4
gives corresponding G coefficient errors below 5.875e-16 and
1.594e-13. These bounds cover the full omitted spectrum and retain
the polynomial |k| amplitude without weakening either heat exponent.

Every one-dimensional moment required by the full retained G tensor
and both probe matrices lies in (1). An exhaustive containing-support
check covers 24 signed G component rows, 48 triplet and 192 shear probe
rows, and all 259682 entries in their 28 distinct spatial matrices.
Their required moment union is exactly the 1348 keys in (1), with no
missing moment or failed matrix. The support sets can overestimate
true nonzero terms; no coefficient cancellation is assumed.

No retained heat integral, B_(i,G) value, actual G sign, complete cubic
compensation, finer power/logarithm or interacting estimate follows.
The R evaluation, triplet transverse-H sign, other response jets,
finite matching, interacting error <=c_box/2, continuum axioms,
reflection positivity, infrared control and finite positive mass remain
unresolved. This is local standard-method reproduction, without a
claim of originality or a Yang--Mills candidate.

## Proof

### 1. Sum the polynomial amplitude with the full heat decay

Set c=9/1024. Since lambda_k/16=pi^2 |k|^2/1024>c |k|^2,
L140's complete physical pair has the absolute majorant

    C_G N_i |k| exp[-c(|k|^2+|l|^2)].                         (3)

This is used for the entire omitted union. Allowing every nonnegative
coordinate in all four one-form components only increases the sums.
Define S0=sum_(n>=0)exp(-c n^2), S1=sum_(n>=0)n exp(-c n^2).
The decreasing Gaussian and pi<4 give

    S0<=1+integral_0^infinity exp(-c x^2)dx
       =1+16 sqrt(pi)/3<35/3<12.

For n>=1 and n-1<=x<=n, both x+1>=n and
exp(-c x^2)>=exp(-c n^2). Hence, without claiming that the
first-moment integrand is decreasing,

    S1<=integral_0^infinity (x+1)exp(-c x^2)dx
       =512/9+16 sqrt(pi)/3<608/9<68.                         (4)

For an omitted coordinate n>K, the same cell argument and the usual
Gaussian tail (integrate x/K in place of 1) give

    sum_(n>K)exp(-c n^2)<=t0 exp(-cK^2),
    sum_(n>K)n exp(-c n^2)<=t1 exp(-cK^2),
    t0=1/(2cK), t1=1/(2c)+t0.                               (5)

The second inequality integrates (x+1) on [K,infinity), so it includes
all high frequencies even though n exp(-c n^2) is not globally
monotone. At K=96, cK^2=81, t0=16/27 and t1=1552/27.

Let A and B denote the full single-label majorant sums with weights
1 and sum_j k_j respectively; |k|<=sum_j k_j. Four components and
four coordinates give

    A<=4*12^4=82944,
    B<=16*68*12^3=1880064.                                  (6)

For their rectangular complements, union over the omitted coordinate
gives

    A_tail<=16*t0*12^3 exp(-81)=16384 exp(-81),
    B_tail<=16*(t1*12^3+3*t0*68*12^2)exp(-81)
          =1867776 exp(-81).                                (7)

In the second line the omitted coordinate supplies the first moment
t1, or one of the other three coordinates supplies S1 while that
omitted coordinate supplies t0. This includes every corner; union
overcounts are harmless. The omitted pair union is contained in
{k omitted} union {l omitted}, with the polynomial weight only on k.
Consequently its complete weight is at most

    B_tail*A+B*A_tail
      <=(1867776*82944+1880064*16384)exp(-81)
       =185723781120 exp(-81).                              (8)

The positive Taylor polynomial through degree 8 gives
exp(3)>sum_(j=0)^8 3^j/j!=89641/4480>20. Thus
exp(-81)<20^-27. Multiply (8) by C_G N_i from (3). Exact rational
reduction gives precisely (2); all decimal comparisons are rational
inequalities. Multiplication by L140's strict scalar bound proves the
G errors. This sharpens L140's omitted-mode bound by keeping its
original heat decay; it does not change its functional or mode region.

### 2. Cover the new physical rows without dropping the upper endpoint

For a transverse input component alpha, L140 gives h by replacing its
axial sine with

    j_n(x)=[cos(n omega(x+4))-(-1)^n]/(2 n omega),
    omega=pi/8, n>=1.                                      (9)

Its output alpha is the sum of -partial_b^2 rows over transverse
b!=alpha; its output a!=alpha is the partial_a partial_alpha row.
The input component 1 gives zero h exactly. There are 12 such signed
component rows: six diagonal second-derivative rows and six mixed
first-derivative rows. Each is paired with the complete direct and
negative-prefix rows of L_F, giving 24 signed G matrix terms. Its
weight is ell u_1=(ell f) tensor r tensor f' tensor r. No optional
symmetrization factor or outside factor 3 is introduced.

Represent row products by containing polynomial-exponential supports
(n,h) for x^h exp(i n omega x). An ordinary positive-frequency mode
or its nonzero first/second derivative has degree zero and frequencies
±n; a zero E mode is constant and its derivatives are zero. A nonzero
lower prefix has degree zero and frequencies ±m. Its zero mode is
p_0=(x+4)/sqrt(8), of degrees 0 and 1 at frequency zero. Formula (9)
has degree zero and frequencies ±n AND zero: the latter retains its
endpoint constant. The exact shift phases i^(±n) and the real endpoint
coefficient do not change these containing supports.

In the axial G row multiply by ell*f=(x+4)x rho. With a direct
right row, or with a nonzero prefix, the required degree is at most
2 and |frequency|<=n+m<=192; the endpoint-constant piece also
requires the right frequency m. With p_0 the degree is at most 3,
and the only frequencies are 0 and ±n, with |n|<=96. This proves
(1) for all axial G factors, including every upper endpoint term.

In the transverse directions all G row factors and derivatives have
polynomial degree zero, including constant E modes. Their product
frequencies have absolute value at most 192. Weights r and f' reduce
to F_0 and F_1 by the compact integration-by-parts identity

    integral f' g=-integral x rho g'.                        (10)

All boundary terms vanish because rho and its derivatives have compact
support in [-3,3], inside the length-eight box. Differentiating a mode
exponential changes only its coefficient, so no higher degree is
introduced by (10). The right forest gradient derivatives and the
left transverse second derivatives are all retained.

For Q_3 and Q_6 import the complete curvature rows and symmetric
polarizations of L132/L133. Their 48 and 192 signed terms include
both displacement sectors. Each row is an ordinary mode or derivative,
without prefixes, so its product has degree zero and frequency at
most 192. The displacement derivative factors r,r',f,f',f'' reduce
by the complete IBP identities to F_0,F_1 at those frequencies.
In particular both derivatives in an f'' weight are applied to the
whole row product; the polynomial-degree bound remains one.

The required domain (1) is therefore covered by L082's saved moments
(h=0,1 through 192, h=2,3 through 96) plus precisely L133's 192
additional signed F_2(n) intervals at 97<=|n|<=192. The cutoff rho,
moment definition and frequencies are unchanged. L133 proof section 2
already justified the new degree-2 moments using L082's exact-rule
bound E_2<6.3e-13 and L037's specific saved rule; this scope use
requires no new quadrature theorem or regenerated numerical table.
L136's different cumulative R moments are not inputs for these compact
rho rows. Neither the two physical inverse weights in L140(14) nor
the Laplace heat integration changes the spatial moment domain.

### 3. Complete certificate and limitations of its audit

From the active notebook run

    python3 scripts/combined-ward-response/check_g_cutoff96_coverage.py
    python3 scripts/combined-ward-response/check_g_cutoff96_coverage.py --audit

The full certificate is
`scripts/combined-ward-response/g-cutoff96-coverage-certificate.json`;
the replay is
`scripts/combined-ward-response/g-cutoff96-coverage-audit.json`.
The program records the entire rational omission calculation, both
probe bounds, all component row templates, every required signed
moment with an entry witness for each matrix, all failures, and hashes
of the specific L082/L133 input certificates. It checks all retained
entry indices, not a sampled or low-frequency subset. Each symbolic
support is a containing union, so cancellations cannot introduce an
unlisted moment. This does not assert that every possible support
coefficient is nonzero in the mathematical expression.

All 28 matrices and 259682 entries pass; the 1348 required keys match
the supplied containing domain. The full tail record, summary and
empty failure list were inspected, and replay of the complete record
passes. The first audit found a tuple/list serialization mismatch in
the record comparison, with no mathematical bound or coverage failure.
That failed record is preserved as
`scripts/combined-ward-response/g-cutoff96-coverage-first-audit.json`.
Normalizing the generated record to its JSON schema repairs the
comparison; the final replay has zero failures. This is a same-program
replay supporting the analytic proof, not independent formal verification.

Importing the table enclosures establishes available numerical inputs
for a later G evaluation. It does not establish midpoint-radius matrix
inclusion, retained double-time error, arithmetic inclusion or a signed
G interval. The scalar enclosure and original continuum limit remain
separate established inputs; their conclusions are not strengthened
into a physical sign or compensation by this coverage check.

## Mathlib

Full matching G cutoff-96 omission and retained moment-scope theorem:
**not checked**. Supporting polynomial-exponential differentiation,
compact integration by parts, finite tensor traces, Gaussian tails,
positive Taylor bounds and summable union majorants: **not checked**.
Unknown availability is not evidence of absence.
