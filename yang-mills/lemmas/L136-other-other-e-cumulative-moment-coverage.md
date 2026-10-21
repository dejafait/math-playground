# L136 — Retained cumulative-weight moments include the upper axial tail

## Hypotheses

Use L008's exact even smooth cutoff rho, with 0<=rho<=1, rho=1 on
[-5/2,5/2] and support in [-3,3]. Set omega=pi/8 and

    R(x)=integral_(-4)^x rho(t)dt, M=integral rho=F_0(0),
    F_h(n)=integral_(-3)^3 x^h rho(x) exp(i n omega x)dx,
    J_h(n)=integral_(-4)^4 x^h R(x) exp(i n omega x)dx.

The physical application is precisely L134(9)--(10)'s two E heat forms
for both actual probes i=3,6, the straight direction-1 forest and the
relative fixed-link box (-4,4)^4, at flow time 1/16. Keep both probe
sectors and every direct/prefix pairing. Here J_h is a one-dimensional
moment, distinct from the earlier companion functional J_i.

Import L082 proof sections 1--2's certified pi and F moment intervals
from exactly `scripts/combined-ward-response/continuum-first-pair-enclosure-certificate.json`.
In particular its h=0,1 table covers |n|<=192, and its h=2,3 table
covers |n|<=96. These are the proved L037 saved-table intervals and
the enclosed exact-rule extensions, not regenerated approximate values.
L132 proof section 2 and L134 proof section 4 give the actual axial
mode/prefix factors. No accuracy of an R table is assumed.

## Conclusion

For n!=0 put xi=n omega. Elementary integration by parts gives

    J_h(n)=sum_(j=0)^h [(-1)^j h!/(h-j)! (i xi)^(-j-1)]
                            [4^(h-j) i^n M-F_(h-j)(n)],       (1)
    J_h(0)=[4^(h+1)M-F_(h+1)(0)]/(h+1).                     (2)

These identities hold for all integers h>=0, n, independently of the
certified frequency range. They retain R(4)=M. The complete moment
domain needed for the R-weighted axial products at cutoff K=96 is
contained in the following 579-element set:

    h=0: |n|<=192; h=1: |n|<=96; h=2: n=0.                 (3)

All these J moments have outward integer enclosures. Every real and
imaginary component interval has width strictly below 6.92e-12,
against the chosen threshold 1e-9. Only 580 already certified F
moments are imported. All 37,249 possible direct/prefix product
positions satisfy (3); this is integration coverage, not a numerical
evaluation of those spatial matrices or of a heat trace.

The constant-prefix upper tail is explicitly positive:

    integral_3^4 R(x) p_0(x)^2 dx=169M/24,
    845/24 < 169M/24 < 169/4,
    38.8407 < 169M/24 < 38.8408.                            (4)

Its complete length-eight integral is

    integral_(-4)^4 R(x)p_0(x)^2 dx=56M/3-F_2(0)/2.        (5)

Thus the upper tail cannot be dropped even in this retained spatial
entry. Equation (4) is not a contribution or lower bound for the
signed actual W_i or E functional: the transverse coefficients and
probe trace are still required. This supplies L134's missing retained
R-integration input only. U_i,W_i, K_(i,E), ax,-Q,G,R and the complete
K_(i,oo)+4 gamma D_i comparison remain unevaluated here. No finer
remainder, logarithm, interacting bound, continuum construction,
reflection positivity or finite positive physical mass follows.

## Proof

### 1. Exact moments with the upper endpoint retained

R is smooth, R'=rho, R(-4)=0 and R(4)=M. For n!=0 define

    P_(h,n)(x)=exp(i xi x) sum_(j=0)^h
                              (-1)^j h! x^(h-j)/[(h-j)!(i xi)^(j+1)].

Differentiate the entire finite sum. The derivative of each monomial
cancels the exponential derivative of the next term, leaving exactly
P'_(h,n)=x^h exp(i xi x). Integration by parts on [-4,4] therefore
gives J_h(n)=M P_(h,n)(4)-integral rho P_(h,n). Since
exp(i xi*4)=exp(i n pi/2)=i^n, this is (1). For n=0 the primitive
x^(h+1)/(h+1) gives (2). No boundary term is discarded because rho
is compact: R itself is constant, generally nonzero, above 3.
All integrations are of smooth functions on a compact interval.

This is a direct specialization of the standard integration-by-parts
theorem to the imported weights. Its derivation is written out because
the nonzero upper endpoint changes the result; it does not reprove
the rho quadrature theorem or invoke a new ultraviolet estimate.

### 2. Full product scope, including the constant prefix

For a transverse direct lift input the axial row is

    v_n(x)=sin(n omega(x+4))/2, 1<=n<=96.

For a component-1 prefix input the axial rows are p_n=v_n/(n omega)
for n>=1 and p_0=(x+4)/sqrt(8). These are exactly L132/L134's rows.
The R-weight occurs only in L134's W_2,W_4. In those physical matrices
there is no extra ell=x+4 factor, no axial derivative, and no other
axial coefficient. All transverse derivatives are in transverse row
factors. Both U_i's compact axial f and W_3's compact axial f remain
covered by the existing rho integration-by-parts machinery; they do
not introduce R moments.

Each nonzero axial row is a sum of exponentials with frequencies ±n
and polynomial degree zero, using the exact shift phase i^(±n).
Two such rows need only J_0 at |n|<=192. One p_0 row and one nonzero
row need J_0,J_1 at |n|<=96. Two p_0 rows have frequency zero and
polynomial degree two. This proves (3) for every pairing and every
mode, including off-diagonal products. Scalars 1/(n omega), norm
factors and transverse derivatives do not enlarge that axial scope.

Equations (1)--(2) need F_0 for |n|<=192, F_1 for |n|<=96 and
F_2(0),F_3(0). The union has 385+193+2=580 elements and lies
entirely within L082's certified table. Thus no new quadrature or
unread essential source is needed. In particular the degree-2
nonzero-frequency extension from L133 is not needed for these R rows.
The program checks the frequency/degree union at every one of
96^2+2*96*97+97^2=37,249 direct/prefix positions. It includes possible
terms even when exact cancellation could reduce their scope.

### 3. Outward interval evaluation and complete replay

Use L037's outward fixed-point arithmetic at scale S=10^180, with
integer endpoint addition, multiplication and signed nonzero division.
Import the exact 580 source records and the certified pi interval.
Set the mass imaginary part to zero using exact evenness, after
checking that its imported interval contains zero. All reciprocal
denominators n omega are separated from zero. The phase i^n has
exact integer real/imaginary components. Complex products use
(a+ib)(c+id)=(ac-bd)+i(ad+bc) with outward real operations.
Substitution into the finite identities (1)--(2) then encloses each
exact moment by induction; correlations between repeated inputs may
widen intervals but do not invalidate inclusion.

The certificate saves every imported record and all 579 resulting
complex intervals, source/script hashes, the complete product-scope
unions and the exact rational widths. The largest component width,
at h=1,n=-1, is <6.92e-12 by exact fraction comparison. No claimed
precision is inferred from a binary64 preview. The audit regenerates
and compares every record and every product-scope union. It also
checks all 576 nonzero-frequency moments against the separate
recurrence obtained by differentiating x^h exp(i xi x):

    i xi J_h(n)=4^h i^n M-F_h(n)-h J_(h-1)(n),            (6)

with the last term absent at h=0. Every pair of enclosures intersects;
all negative-frequency conjugacy checks pass. These checks support
the inclusion implementation; equations (1)--(3) provide its proof.
No new BLAS or machine-trigonometric assumption is used. The imported
rho intervals retain the source certification's qualifications.

Reproduce from the active notebook:

    python3 scripts/combined-ward-response/enclose_e_cumulative_moments.py
    python3 scripts/combined-ward-response/enclose_e_cumulative_moments.py --audit

Full evidence is saved in
`scripts/combined-ward-response/e-cumulative-moments-certificate.json`
and `scripts/combined-ward-response/e-cumulative-moments-audit.json`.
All records replay, all bounds pass and there are no failures.

### 4. Constant-prefix and upper-tail checks

Evenness of rho gives F_1(0)=F_3(0)=0. Hence (2) gives
J_0(0)=4M, J_1(0)=8M-F_2(0)/2, and J_2(0)=64M/3. Expanding
p_0^2=(x^2+8x+16)/8 proves (5), including both prefix endpoints.
On [3,4], R=M, and direct integration gives

    integral_3^4 M(x+4)^2/8 dx=M(8^3-7^3)/24=169M/24.

The cutoff equals one on an interval of length 5 and is strictly
between zero and one on the transition intervals, so 5<M<6. This
proves the rational inequalities in (4). The imported M enclosure,
multiplied outward by 169/24, lies strictly between 38.8407 and
38.8408 by exact endpoint comparison. The expanded and simplified
whole-prefix intervals also intersect. The saved complete upper-tail
interval was inspected. An omitted upper tail would therefore change
this particular spatial entry by a strictly positive amount; this
does not assert a sign after the actual heat/probe contraction.

## Mathlib

Full matching retained R-moment/physical-mode coverage theorem: **not checked**.
Supporting integration by parts, polynomial-exponential primitives,
finite sums, interval arithmetic and trigonometric identities: **not checked**.
Unknown availability is not absence. This is local reproduction of
standard calculus and certified-interval methods, with no novelty claim.
