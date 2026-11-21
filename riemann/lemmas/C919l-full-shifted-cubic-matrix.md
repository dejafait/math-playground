# Corollary 919l: full shifted cubic matrix at time zero

## Hypotheses

Use the actual Xi of L018, opposite-class representatives alpha_j
with every zero order as in L024, beta_j=alpha_j^(-2), L025's real
absolutely convergent S_m, and L030's algebraic form

    Q(q)=sum_j beta_j^2 q(beta_j)^2.

Use accepted C919f at time zero and L058's F(0,z)=Xi(z), retaining
C919f's correct CPython integer/Fraction and Decimal/libmpdec contracts,
including correctly rounded HALF_EVEN exp. Use accepted C919k's
count-certified occurrence in(100,200], under its Bellotti-Wong input.
Correct CPython integer/Fraction arithmetic is also assumed for the
new finite exact certificate; Decimal below is explanatory display only.

Import David J. Platt, *Isolating some non-trivial zeros of zeta*,
Mathematics of Computation86(307)(2017),2449-2467,
DOI10.1090/mcom/3198, Theorem5.1, accepted manuscript printed p8
(PDF p9), with Sections4.1-4.2/5, pp6-8:
https://research-information.bris.ac.uk/ws/portalfiles/portal/78836669/platt_zeta_submitted.pdf.
This gives critical-line location and simplicity of all nontrivial
zeros with |Im rho|<=30610046000. Only complete reality through1000
and the zero-ordinate implication are used. Simplicity is unnecessary.
Import L467's complete multiplicity-counted closed-unit-shell bound
18log(n+2), under Chiara Bellotti and Peng-Jie Wong, *Improved estimates
for the argument and zero-counting function of the Riemann zeta-function*,
arXiv:2412.15470v2(7July2025), Theorem1.1 p1/Section5 pp23-24:
https://arxiv.org/pdf/2412.15470v2.
These published/source computations and the accepted C919f computation
are imported, not rerun or fully source-audited here.

No RH, ordered zero census, uniqueness in a box, global simplicity,
exterior reality, positive-time product or cross-notebook input is assumed.

## Conclusion

For every integer r>=4 the real symmetric matrix

    H_(3,r)=(S_(2r+i+j+2))_(0<=i,j<=3)

is positive definite. Equivalently, Q(X^r p)>0 for every nonzero real
polynomial p of degree at most3. With D=diag(1,200,40000,8000000)
and k=r-4>=0, the stronger bound proved below is

    lambda_min(D H_(3,4+k) D)
       >=200^(-4k)*(h4-t4*(1/625)^k)
       >=200^(-4k)*(h4-t4)>0,
    h4=1/B,
    B=55044853395654549140820213578367951043403504391013321572165680339806783432529630521310214442670151084252781180078812111551
      /12001875781096364510863055158897268634103072275607649796489216000000000000,
    C=1+1/25000000+1/625000000000000+1/15625000000000000000000,
    t4=18*C*(1000^(-19)+1000^(-18)/18).

For orientation only, h4 is approximately2.18038109663561e-49,
t4 approximately1.01800004072000e-54 and h4/t4 approximately214182.81.
The proof uses exact rational inequalities, not these displays.
This is a local known-method specialization, classified REPRODUCTION,
accepted by the separate step2224 conceptual audit under the stated
source and arithmetic assumptions. It extends the accepted single cubic
ray to every cubic coefficient vector after the shift; it establishes
no result beyond the checked general methods, removes no shift and
provides no arbitrary-degree or RH conclusion. It is not an RH candidate.

## Proof

### Representatives, complete real head and four selected occurrences

L018 sends rho=sigma+i gamma to alpha=gamma+i(1/2-sigma), injectively
and preserving orders. If gamma=0, Platt's symmetric theorem forces
sigma=1/2, so alpha=0, excluded by L024. Hence choose the unique
representative Re(alpha)>0 of every opposite class, keeping orders.
This is exactly the positive-ordinate zeta multiset. In particular a
nonreal conjugate pair of Xi zeros with positive real parts contributes
two occurrences, not one; neither is the other's opposite.

Let the finite head contain every occurrence with0<gamma<=1000,
including the upper endpoint. It is finite by L467, and Platt applies
since1000<30610046000, making every head alpha positive real. Thus
every head beta is positive real. C919f and L058 give one real zero
x_j in each of (14,29/2),(41/2,43/2),(49/2,51/2). Accepted C919k
gives N(200)-N(100)>=14, hence at least one real head occurrence
x_4 in(100,200]. Select one. All four classes are distinct. No count
or simplicity beyond existence is needed for the selected occurrences.
Use their closed enclosures for a bound valid at every endpoint:

    ell=(14,41/2,49/2,100), u=(29/2,43/2,51/2,200).

For any head or exterior alpha define

    w(alpha)=(alpha^(-2),200alpha^(-4),40000alpha^(-6),
              8000000alpha^(-8))^T.

L025/L030, applied entrywise to this fixed dimension, give the
absolutely convergent identity in ordinary transpose convention

    D H_(3,r) D=sum_j beta_j^(2r) w(alpha_j)w(alpha_j)^T. (1)

The head terms in(1) are real positive semidefinite, including all
unselected occurrences and all multiplicities.

### One weighted inverse enclosure on the entire four-node box

Import Walter Gautschi, *Norm Estimates for Inverses of Vandermonde
Matrices*, Numerische Mathematik23(1975),337-347, Section3(3.1)-(3.4),
printed p339 and Section4(4.1)-(4.1'), p340:
https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/051.pdf.
For distinct nodes, row j of the inverse of the matrix with columns
(1,y_j,...,y_j^(n-1))^T consists of the coefficients of the j-th
Lagrange polynomial in increasing degree order. Use its general
finite-n formula at n=4; its proof is not repeated. The specialization
below is necessary because neither this source nor C919e supplies
the four-node shifted weights, broad fourth interval or constants.

Put y_j=200/x_j^2 and let V have columns(1,y_j,y_j^2,y_j^3)^T.
Their transformed enclosures [a_j,b_j] are exactly

    [800/841,50/49], [800/1849,800/1681],
    [800/2601,800/2401], [1/200,1/50].

For j<l, g_jl=a_j-b_l has the six positive values

    g_12=672000/1413721, g_13=1248000/2019241,
    g_14=39159/42050, g_23=441600/4439449,
    g_24=38151/92450, g_34=37399/130050.

Write g_lj=g_jl. Thus y_1>y_2>y_3>y_4>0 throughout the closed
box; all pairwise separations have paid positive lower bounds.
At r=4 let U have columns beta_j^4 w(x_j). Exactly,

    U_j=x_j^(-10)*(1,y_j,y_j^2,y_j^3)^T,
    U=V diag((y_j/200)^5),
    U^(-1)=200^5 diag(y_j^(-5)) V^(-1).              (2)

This includes the onset weights inside the inverse enclosure.
For J_j={1,2,3,4}\{j}, the cited formula makes inverse entry(j,m),
with0<=m<=3 indexing polynomial degree, equal to

    200^5*(-1)^(3-m)*e_(3-m)((y_l)_(l in J_j))
      /[y_j^5*prod_(l in J_j)(y_j-y_l)].            (3)

Here e_d is the elementary symmetric polynomial of degree d in
three variables, with e_0=1. All its coefficients are nonnegative.
Consequently the following SINGLE rational enclosure holds uniformly:

    |(U^(-1))_(j,m)|<=M_jm,
    M_jm=200^5*e_(3-m)((b_l)_(l in J_j))
                  /[a_j^5*prod_(l in J_j)g_jl],
    ||U^(-1)||_F^2<=sum_(j=1)^4 sum_(m=0)^3 M_jm^2=B. (4)

Every numerator uses upper endpoints and every positive denominator
uses lower endpoints. They need not attain their extrema simultaneously;
these inequalities hold at each point of the full box. There is no
subdivision, sampling, parameter search or determinant-only bound.
The denominator sign in(3) is(-1)^(j-1), so the row signs are
(-,+,-,+),(+,-,+,-),(-,+,-,+),(+,-,+,-); the certificate retains
all16 full signed entry enclosures as well as their magnitudes.

For the finite real matrix implication import Stephen Boyd and Lieven
Vandenberghe, *Convex Optimization*(2004), corrected seventh printing2009,
A.1.1 pp633-634, A.1.5 p636, A.5.2 pp646-647, A.5.4 pp648-649,
and Section2.2.5 pp34-35:
https://web.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf.
Only finite real SVD, Euclidean/Frobenius norms, matrix order and
congruence are used. In particular ||U^-1||_2<=||U^-1||_F and
lambda_min(U U^T)=||U^-1||_2^(-2)>=1/B=h4.
At onset the selected contribution in(1) is exactly U U^T. Keeping
every other nonnegative head occurrence gives head_4>=h4 I.

### Complete complex exterior in the same scaling

For any real c in R^4 and every exterior occurrence gamma>1000,
complex Cauchy-Schwarz and |alpha|>=gamma imply

    |beta^8 (c^T w(alpha))^2|
       <=||c||_2^2 |alpha|^(-20)
             *sum_(i=0)^3 200^(2i)|alpha|^(-4i)
       <=||c||_2^2 C gamma^(-20).                  (5)

This bounds the error in an algebraic square; it does not change(1)
to a Hermitian Gram identity. Each component of the prescribed D
has been retained, including the cubic component.

Partition all gamma>1000 into half-open unit shells(n,n+1], integer
n>=1000. L467 bounds their complete counts by the closed-shell count
18log(n+2). Integer upper endpoints are retained; extra lower endpoints
in this upper bound only overcount. Both conjugate occurrences and
every zero order are charged. For n>=1000, log(n+2)<=n since
n+2<=2n, log2<1 and log n<=n-1. The decreasing integral bound gives

    sum_exterior |beta^8(c^T w(alpha))^2|
       <=18*C*||c||_2^2*sum_(n>=1000)n^(-19)
       <=18*C*||c||_2^2*(1000^(-19)+1000^(-18)/18)
        =t4||c||_2^2.                              (6)

Indeed n^(-19)<=integral_(n-1)^n x^(-19)dx for n>=1001,
and the integral from1000 to infinity is1000^(-18)/18. This is
a summable bound for every shell, with no unpaid intermediate or
infinite remainder. By L025 the matrix in(1) is real symmetric;
the head is real, hence the complete exterior E_4 is real symmetric.
Absolute convergence from L030 permits subtraction and the bound(6),
so E_4>=-t4 I. No individual exterior reality or sign is presumed.

### Exact rational comparison and all larger integer shifts

Run from the notebook:

    python3 scripts/h2-head/full_cubic_matrix_2222.py

Full exact evidence is in `scripts/h2-head/full_cubic_matrix_2222.json`.
It retains all eight spatial/transformed endpoint pairs, all six gaps,
all inverse numerator/denominator operands and16 signed inclusions,
four row squares, their sum B, every exterior component, the full
shell budget, actual/required margin, shift factors and all failures.
The complete load-bearing values were inspected, not inferred from
previews. All seven checks pass and the failure list is empty.
Evaluating(4) gives exactly the B in the conclusion. For reduced
h4=N_h/D_h and t4=N_t/D_t, the positive integer comparison is

    N_h*D_t-N_t*D_h
    =93764216761198174281344544452200837799669889049801000628997883582430374015085823167246414103850576511443829196156122445818289206448969333345398160220541>0.

Both denominators are positive, so h4>t4>0 exactly. Thus at onset
D H_(3,4) D>=head_4+E_4>=(h4-t4)I>0.

For any integer k=r-4>=0, each selected real x_j<=200 contributes
its onset rank-one matrix times beta_j^(2k)=x_j^(-4k)>=200^(-4k).
Every other real head occurrence stays nonnegative. Therefore the
complete head at r is at least200^(-4k)h4 I. Each exterior summand
in(5) gains |alpha|^(-4k)<=1000^(-4k), so the same COMPLETE
summable majorant bounds the exterior at r by1000^(-4k)t4 I in
absolute quadratic form. This proves, for every real c,

    c^T D H_(3,4+k) D c
       >=[200^(-4k)h4-1000^(-4k)t4]||c||_2^2
        =200^(-4k)*[h4-t4*(1/625)^k]||c||_2^2>0

when c is nonzero. This is for arbitrary k, not a finite sample.
Invertible positive diagonal D transfers positive definiteness to
H_(3,r). Finally L030 gives c^T H_(3,r)c=Q(X^r p) for
p(X)=sum_(i=0)^3 c_i X^i, proving the conclusion.

The bound decays with k; no shift-independent positive lower bound,
unshifted matrix sign, arbitrary-degree sign or RH assertion follows.
All source computations and arithmetic contracts remain qualifications.
The separate audit below accepts the normalization, occurrences,
all16 inverse bounds, the complete tail and the every-r comparison.

### Independent conceptual audit, 21 November2026 (step2224)

The invocation-start SPECIALIZE assessment2222, separately approved2223,
covers this exact audit. The proof and generator2222 were read in full,
with the essential local proofs and the accepted C919f/k qualifications.
Primary source coverage and the C030b/L057/2146/2061 overlap distinctions
are reused from notes2221/2216. This audit accepts the stated result
without changing any parameter, mathematical claim or dependency. It
is local verification of a known-method specialization, not a new
general result beyond the checked sources.

**Complete occurrences and endpoints.** The L018 coordinate map is
injective and preserves orders. The symmetric Platt input includes
zero ordinate: a zero there would have sigma=1/2, contrary to L024's
Xi(0)!=0. Hence choosing Re(alpha)>0 loses no opposite class. An
off-line quadruple gives two conjugate representatives at positive
real part, each counted with its full order; they are not opposites.
Thus N's positive-ordinate convention matches (1), with no factor two.
The complete head uses0<gamma<=1000, a subset of the imported verified
range. Its reality, not an ordered census or simplicity, makes every
retained head term nonnegative. C919f includes time zero and L058
identifies that transform with Xi. The three open sign brackets and
C919k's count N(200)-N(100)>=14 supply four distinct classes. The
fourth occurrence may be at200 but not100. All four lie in the closed
boxes used for enclosure; no interior endpoint margin is assumed.

**Normalization and uniform inverse bound.** Entry(i,j) of (1) is
200^(i+j) sum beta^(2r+i+j+2), with zero-based i,j. At r=4 each
selected column is beta^4 w=x^(-10)(1,y,y^2,y^3)^T. Thus (2) has
the fifth power, and its inverse scales ROW j of V^-1 by200^5/y_j^5.
The cited Lagrange coefficient convention applies to columns of V:
its row polynomial evaluated on column l is delta_jl. No transpose
of that coefficient matrix or unweighted inverse is substituted.

The six strictly positive lower separations establish distinctness
over the whole closed product box. All numerator magnitudes in (3)
are elementary symmetric polynomials in positive nodes; bounding
each node above and each denominator magnitude below is valid even
when the separate extremes cannot occur simultaneously. The denominator
has j-1 negative difference factors, giving exactly the four recorded
alternating sign rows. The resulting B is an upper bound on the
Frobenius norm SQUARED of U^-1. The cited finite real singular-value
identity therefore gives lambda_min(U U^T)>=1/B, with no missing
square, dimension factor or change to an infinity norm. All remaining
head occurrences can be added in real positive-semidefinite order.

**Independent complete arithmetic.** Run from the notebook:

    python3 scripts/h2-head/full_cubic_matrix_audit_2224.py

The full certificate is `scripts/h2-head/full_cubic_matrix_audit_2224.json`.
It neither imports nor executes the original generator. Instead, exact
signed interval polynomial multiplication constructs prod_(l!=j)(t-y_l)
over all four node boxes. The signed denominator interval encloses
y_j^5 prod_(l!=j)(y_j-y_l)/200^5 and excludes zero. Reciprocal interval
multiplication therefore encloses each actual inverse entry. Interval
operations allow repeated-variable correlations to be discarded only
by enlarging enclosures. All16 resulting intervals are contained in
the original signed enclosures; their maximum absolute endpoints
reproduce the original M_jm. This proves full-box inclusion, not a
sampled inverse check. Squaring and summing reproduces every row bound
and B. The tail is independently assembled as C*1018/1000^19.

All126 saved rational operands are compared, including the endpoints,
six gaps, all inverse operands and signed endpoints, four row squares,
full exterior components, margin and shift factors. A recursive field
check confirms that no rational operand is omitted. All200 audit
checks pass, including the seven reconstructed original Boolean
claims; both failure lists are empty. Original generator/certificate
hashes are retained and both files remain unchanged. Complete interval
rows, bounds and checks were inspected using selected full JSON fields.
The exact positive cross product displayed above is reproduced. Thus
h4>t4>0, with explanatory ratio214182.810355635177; the rounded ratio
is not used to prove the strict sign. The backend trust is unchanged.

**Complete algebraic exterior and every shift.** For real c, the
complex Euclidean inequality bounds |c^T w|^2 by||c||^2 sum|w_i|^2.
Multiplication by|beta|^8 gives exponent20 and all four components
of C exactly as in (5). This estimates the modulus of an algebraic
square; it does not identify the form with a Hermitian square. Every
gamma>1000 is assigned to exactly one shell(n,n+1], n>=1000. The
closed-shell bound only overcounts, including integer endpoints and
every order. The n=1000 term plus the decreasing integral pays the
entire infinite sum. L025/L030 make the full matrix real symmetric
and absolutely convergent; subtracting its real head makes the entire
exterior real. Its quadratic form is therefore bounded below by minus
the absolute budget. No individual exterior zero is assumed real.

For arbitrary integer k>=0, only the FOUR SELECTED head terms are
compared with200^(-4k) times their onset terms. Their heights are at
most200 and their rank-one matrices are real positive semidefinite.
Other head occurrences, some above200, are retained as nonnegative;
the argument never incorrectly scales the entire onset head by the
selected-height bound. Every exterior term gains at most1000^(-4k)
in modulus. Multiplying the complete summable majorant is valid for
each k and gives the stated factor(200/1000)^(4k)=(1/625)^k. No limit
interchange, finite sample of shifts or k-independent positive margin
is used. Real invertible congruence by D then transfers the strict
matrix sign, and L030's index shift identifies Q(X^r p).

The audit verifies all frozen obligations without retuning. The result
pays every cubic coefficient vector after r>=4, including cross terms,
but supplies neither arbitrary-degree positivity nor shift removal.
C030b's finite total-degree overlap does not cover every r. Source
computations, C919f's Decimal/libmpdec correctly rounded HALF_EVEN exp
contract, and correct CPython integer/Fraction arithmetic remain inputs;
none is independently implementation-verified here. No RH candidate
or formal Lean verification is asserted.

## Mathlib

Full matching theorem not checked; no absence claim. The source
assessment2221 covers the imported general finite-matrix methods,
not a formal proof of this actual-Xi arithmetic specialization.
