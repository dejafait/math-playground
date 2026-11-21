# Lemma 937: the fixed L936 degree-eleven score correction is infeasible

## Hypotheses

Use the exact algebraic witness of L936, including its single common
mass, its accepted real root alpha, and its normalized real vector c.
In particular the raw values m_j, indexed by the power u^(2j), are

    m0=.497123021571, m1=.022972233662, m2=.002962906960,
    m3=.000599311666, m4=.000160971754, m5=alpha,
    m6=.000020475993,
    .0000530387415958154365906397391693872935932598188 < alpha
      < .00005303874159581543659063973916938729359325981881.

Alpha is an exact root of L936's specified quadratic, not the midpoint
of this bracket. Put y_j=m_j/m0, y0=1, and retain L936's y7, although
the polynomial below does not use it. The vector c is exactly the one
in L936, so c2^2>0. Use the full positive kernel K of L019 and fix
lambda0=1/10240. Define by finite formal coefficient extraction

    g_w(z)=sum_(j=0)^6 (-1)^j y_j z^(2j)/(2j)!,
    b_n=sum_(i+j=n-2) c_i c_j,                0<=i,j<=2,
    R_w(u)=-sum_(n=2)^6 n b_n [z^(2n)] cos(zu)/g_w(z).

This is L874's finite prescription evaluated on algebraic data. It
does not assert that g_w is the actual characteristic-function germ.
Choose any eight real constants (a0,...,a5,alpha0,beta0) in [-16,16]^8,
independent of u, and set

    P(u)=c2^2 sum_(j=0)^5 a_j u^(2j+1),
    W(u)=u(K'/K)(u)R_w(u)+P'(u)+(2lambda0 u+K'/K)P(u)
                              +alpha0 R_w(u)+beta0 uR_w'(u).

## Conclusion

There is no such constant tuple with W(u)>=0 for every u>=0.
In fact the nine points and positive rational weights below satisfy,
uniformly over the entire coefficient box,

    sum_i w_i W(u_i)/c2^2 < -1.05419147312*10^(-14) < -10^(-15).

This excludes the fixed degree-eleven sufficient certificate on this
single member of the relaxation. It does not exclude coefficients
outside the box, other multiplier classes, or a certificate restricted
to genuinely realized contacts. No actual score expectation, contact
sign, failure of Xi positivity, or RH counterexample follows.
The independent step45 proof/code audit below accepts this fixed
finite obstruction, with the same scope qualifications.

## Proof

### Exact normalization and the linear residual

Write c=c2*(p,r,1). L936 supplies

    q_j=(-1)^j y_j/(2j)!,
    S_n=-n q_n-sum_(k=1)^(n-1) S_k q_(n-k),
    Delta=S2*S4-S3^2>0,
    p=(S3*S5-S4^2)/Delta,
    r=(S3*S4-S2*S5)/Delta.

Put v=(p,r,1), bbar_n=sum_(i+j=n-2)v_i v_j, and define

    d0=1,  d_n=-sum_(j=1)^n q_j d_(n-j),
    Rbar(u)=R_w(u)/c2^2=sum_(j=0)^6 rho_j u^(2j),
    rho_j=-sum_(n=max(2,j))^6 n bbar_n d_(n-j)(-1)^j/(2j)!.

These finite recurrences are the formal inverse of g_w, whose constant
term is one. In particular rho6=-6/12!; no approximate null vector is
used. The full interval for alpha is propagated through every operation.
L936 justifies Delta>0 and the exact choice of c; the present arithmetic
also keeps every denominator away from zero. No root uniqueness or
new moment-realization theorem is needed.

Let h(u)=K'(u)/K(u) and define

    f(u)=u h(u)Rbar(u),
    B_j(u)=(2j+1)u^(2j)+(u/5120+h(u))u^(2j+1), 0<=j<=5,
    B_6(u)=Rbar(u),       B_7(u)=u Rbar'(u).

Direct differentiation, using 2lambda0=1/5120, gives exactly

    W(u)/c2^2=f(u)+sum_(j=0)^5 a_j B_j(u)
                         +alpha0 B_6(u)+beta0 B_7(u).       (1)

The scale c2^2 is positive, so it does not change the required sign.
All values at u=0 are polynomial evaluations; B_0(0)=1.

### The positive combination and its certified bounds

Take w_i=N_i/10^45, with the following exact integer numerators.
Their positivity is immediate; their sum need not equal one.

| u_i | N_i |
| --- | --- |
| 0 | 342629551549331167928578595198237452234451029 |
| 19/100 | 426557058813327609702413571732323783259929594 |
| 39/200 | 56912904027720194510092583061216678730988358 |
| 19/50 | 122205527368671115281979946784999547871670448 |
| 77/200 | 33758257961239763697121188149130759718426132 |
| 57/100 | 5573293822800309123450863218672228205428839 |
| 23/40 | 12001199277408839756363251855419549979105596 |
| 31/40 | 232732544813000000000000000000000000000000 |
| 39/50 | 129474634688000000000000000000000000000000 |

The exact-rational enclosures justified below yield

    -1.05818188426e-14 <= sum_i w_i f(u_i) <= -1.05818188425e-14.

For C_j=sum_i w_i B_j(u_i), complete outward rational bounds imply:

| j | lower bound for C_j | upper bound for C_j |
| --- | --- | --- |
| 0 | 1.10905264742e-44 | 1.10905264743e-44 |
| 1 | 2.03924960631e-45 | 2.03924960632e-45 |
| 2 | 3.80713857992e-46 | 3.80713857993e-46 |
| 3 | 4.64782200551e-47 | 4.64782200552e-47 |
| 4 | -9.67949205045e-48 | -9.67949205044e-48 |
| 5 | -1.14878796515e-47 | -1.14878796514e-47 |
| 6 | 1.35732291792e-18 | 1.35732291793e-18 |
| 7 | -1.13668403629e-18 | -1.13668403628e-18 |

In particular C_6 and C_7 are not set to zero. For any coefficient
tuple in the stated box, (1) gives

    sum_i w_i W(u_i)/c2^2
      <= sum_i w_i f(u_i)+16 sum_(j=0)^7 |C_j|.

The exact interval computation gives the box allowance at most
3.99041112674e-17 and the combined upper bound strictly below
-1.05419147312e-14. Already the two displayed coarser bounds imply
a negative upper bound. If W were nonnegative on the half-line, its
positive weighted sum at these nine points would be nonnegative,
a contradiction. This argument excludes every coefficient tuple,
not just a tested optimizer output. No sign proof between the points
or on the infinite u-tail is required for this infeasibility direction.

### Complete theta score, including every omitted summand

For each selected u put v=pi exp(2u). L019 and L874 give, with locally
uniformly convergent differentiated series,

    K_n(u)=4vn^2(2vn^2-3)exp(u/2-vn^2),
    A_n=K_n/K_1=n^2(2vn^2-3)/(2v-3) exp(-(n^2-1)v),
    s_n=K_n'/K_n=9/2+6/(2vn^2-3)-2vn^2,
    h(u)=(s_1+sum_(n>=2) A_n s_n)/(1+sum_(n>=2) A_n).

The rational v bounds verify 3<v<16 at all nine points. Thus, for
n>=1, A_n<=2n^4 exp(-3(n^2-1)) and |s_n|<39n^2: indeed
2v/(2v-3)<=2 and 9/2+6/(2vn^2-3)+2vn^2<=13/2+32n^2.
For n=9+k, k>=0 integer,

    n<=9(10/9)^k,       n^2-1>=80+19k.

Since e>2 and (10/9)^m/2^57<1/2 for m=4,6, geometric summation gives

    0<=sum_(n>=9) A_n < E_A=4*9^4/2^240,
    |sum_(n>=9) A_n s_n| < E_B=156*9^6/2^240.              (2)

The elementary e>2 follows from its positive power series. Both
geometric-ratio comparisons are checked exactly. The script encloses
the terms n=1,...,8, adds [0,E_A] to their denominator, adds
[-E_B,E_B] to their numerator, and divides by the positive denominator.
Thus every h used in (1) encloses the full theta score. In particular
the score enclosure at zero contains zero; symmetry is not needed to
replace it by an unproved exact value. These are complete pointwise
series bounds, not a finite-theta substitution.

### Reproducible arithmetic and the scope of imported tools

Reproduce the certificate with

    python3 scripts/heat/l936-score-correction-certificate-43.py

All full intervals, score terms, polynomial coefficients, weights,
row values, weighted sums and checks are saved in
`scripts/heat/l936-score-correction-certificate-43.json`.
The proof uses exact Python integer/Fraction arithmetic, with rational
interval endpoints rounded outward to multiples of 10^(-80) after
each operation. Addition uses the endpoint sums, multiplication the
four endpoint products, and division the reciprocal interval after
rejecting any zero-containing divisor. Floor/ceiling are exact integer
operations. Induction therefore proves enclosure for each finite
expression, without relying on floating-point or Decimal exp.

For pi, import L037's rational Machin identity and alternating-series
remainder only: 96 terms for arctan(1/5) and arctan(1/239) enclose pi
through 16 arctan(1/5)-4 arctan(1/239). The Decimal-library contracts
of L037's separate moment certificate are not used here. For exp(x),
x>=0, divide the whole input interval by 2 repeatedly until its upper
endpoint is <=1. On [0,1], compute sum_(j=0)^90 x^j/j! by interval
recurrence and add [0,2/91!]. This remainder is valid because the
first omitted term is <=1/91!, and every subsequent ratio is <=1/92.
Repeated interval squaring recovers exp(x). A negative exponential
in A_n is obtained by the reciprocal of this positive enclosure.
The specializations and finite arithmetic are written out to verify
the full score and the coefficient-box margin, not to claim new
arctangent, exponential or interval-arithmetic theorems.

The 26 checks pass with zero failures. The complete rational response
coefficient bounds, root interval, positive weights, tail constants,
checks and weighted separation record were inspected, not merely
previews. The outward decimal summaries above are themselves checked
to contain the exact rational enclosures. In the production run there
are 7211 interval divisions; all divisors avoid zero. Ordinary Python
integer/Fraction correctness remains a computation trust assumption;
the producing run alone is neither a Lean formalization nor an
independent replay. The separate replay is recorded below.

The fixed weights were nominated by a floating finite-point screen,
then constructed by a rational seven-equation midpoint system for
the six B_0,...,B_5 columns and a normalization, fixing the last two
weights at .000232732544813 and .000129474634688. They were rounded
down to multiples of 10^(-45). Neither the midpoint equations nor the
screen is used as an exact cancellation claim: the complete residual
of every rounded weight and column is charged in 16 sum |C_j|.
The certificate script reads no diagnostic file.

The screening script's first pass exhausted its simplex iteration
budget. Its preserved record is
`scripts/heat/l936-score-correction-screen-43-first-pass.json`.
An initial exact construction tried to annihilate all eight midpoint
columns; its weight at u=57/100 was negative, so it was invalid despite
its negative residual. Its full script and certificate are preserved
as `scripts/heat/l936-score-correction-certificate-43-first-pass.py`
and `.json`. The final positive construction keeps the same nine
points, witness, parameter and coefficient class, and pays the two
small response-column residuals instead. No degree/box enlargement
or suppressed failure is involved.

The motivating general identity is known: Ley and Swan, *Stein's
density approach and information inequalities*, ECP18 (2013), paper7,
Definition2.1/Theorem2.2, pp.2-3,
https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/2578/2199.pdf .
It applies to a positive differentiable normalized density with a
differentiable test product vanishing at both endpoints, with absolute
integrability in the local application. Its hypotheses and proof
direction were already inspected in the reused source assessment.
No expectation identity is invoked in the present finite-point
contradiction, so no boundary-integral specialization or reproof is
needed here. In particular, E_actual R_w=0 and E_actual[uR_w']=0
are not assumed for this algebraic witness. Fantuzzi et al.,
arXiv:1512.05599v2, Section4 (4.2)-(4.10)/Proposition3, pp.8-9,
https://arxiv.org/pdf/1512.05599v2 , is only the previously inspected
auxiliary-function comparison; no polynomial-SOS completeness theorem
or stationary theta diffusion is imported.

The approved EXPLORE assessment is
`drafts/literature/2026-11-09-l936-score-correction-pilot-42.md`.
This is a new local obstruction relative to that bounded comparison,
not certified originality of a general theorem. L936's finite Phi>0
obstruction and the earlier empty-domain pilot remain unchanged.
Actual realization, a genuine contact sign, uniform extension,
initialization/tangency, other degrees/panels and global continuation
remain unresolved.

### Independent proof/code audit, 9 November 2026 (step45)

The unchanged conclusion is accepted under the prior EXPLORE assessment
`drafts/literature/2026-11-09-l937-score-separation-audit-43.md`.
This is independent reproduction and local validation of L937, not a
new sign theorem or a result beyond the sources checked. No coefficient,
weight, witness, degree, box, parameter or multiplier class was changed.
The actual-law identities of L874 are not applied to the relaxed witness.

Reproduce the independent certificate with

    python3 scripts/heat/l937-independent-score-audit-45.py

Full evidence is in `scripts/heat/l937-independent-score-audit-45.json`.
The replay reads the producer certificate for comparisons but never
imports or executes its code, solves its midpoint weight system or reads
its optimizer output. It uses the nine published integer weights directly.
Every weight is strictly positive; the minimum is exactly
2023041167/15625000000000. It also verifies the preserved rejected
construction's negative weight at u=57/100 and its recorded failure,
and that the first screen explicitly claims no mathematical conclusion.
Those failed constructions supply no separation evidence.

The real root and its exact normalized vector are imported from the
audited L936. The replay additionally substitutes both exact bracket
endpoints into its integer-scaled quadratic and verifies opposite signs.
The scale is positive, so this is consistent with L936's IVT root.
All subsequent enclosures hold on the entire bracket, not its midpoint.
It independently forms the truncated log(1+h) from powers h^k, k<=6,
and forms (1+h)^(-1) by the finite geometric expansion, modulo t^7,
where t=z^2 and h has exact constant zero. These finite identities follow
from the ordinary formal series since h has positive order. Thus the
S_n and inverse coefficients use a different construction from the
producer's recurrences. Elimination in the leading two null equations
computes (p,r). Delta and the elimination pivot are positive, all
actually used divisors exclude zero, and c2^2=1/(1+p^2+r^2)>0.
The cosine convolution then recovers all seven response coefficients,
including rho6=-6/12!. Horner evaluation in u^2 independently evaluates
Rbar and u Rbar'. The coefficient prescription uses only the finite
algebraic data; it assumes neither actual realization nor expectation
cancellations for this witness.

The arithmetic grid is 2^(-380), with exact Fraction floor/ceiling
after each operation. Enclosure follows by the same endpoint inequalities
stated in the producing proof, with no transcendental library contract.
The replay uses 100 alternating arctangent terms in L037's rational
Machin identity, rather than 96. For exp(-x), x>=0, halve until the
whole interval lies in [0,1/2]. The even Taylor partial sum through
order 160 is an upper bound, and subtracting
2^(-161)/161! bounds its alternating remainder below. The term magnitudes
decrease on this interval. Interval evaluation encloses the partial sum
for every possible input, and repeated squaring recovers exp(-x).
The reciprocal gives exp(2u) only after checking its divisor is positive.
This independent enclosure avoids the producer's positive exponential
series and its very large intermediate positive exponentials.

For v=pi exp(2u), the replay verifies 3<v<16 separately at every point.
It sums the differentiated kernel directly: after division by the common
positive factor exp(u/2-v), its n-th mass and derivative are

    4v n^2 (2v n^2-3) exp(-(n^2-1)v),
    (60v^2 n^4-30v n^2-16v^3 n^6) exp(-(n^2-1)v).

These follow from L019 by differentiation and agree with L874's full
kernel derivative. Dividing both head sums by 4v(2v-3) normalizes to
the producer's relative mass convention. The analytic tail argument (2)
is valid: 2v/(2v-3)<2, |s_n|<39n^2, n<=9(10/9)^k and
n^2-1>=80+19k for n=9+k, integer k>=0. The last inequality uses
k(k-1)>=0; the first follows by induction. Both geometric ratios are
strictly below 1/2, as verified rationally. Thus the same E_A,E_B
cover every n>=9 term. Adding [0,E_A] to the relative denominator
and [-E_B,E_B] to the relative numerator gives the full score, with
positive denominator at all nine points. In particular the enclosure
at zero contains zero without substituting a symmetry claim.

The replay verifies all eight published two-sided column bounds,
the published weighted-offset bounds, and every positive-weight row
against the independently enclosed full score. Each of the eight
allowances is 16 times the larger absolute column endpoint; none is
set to zero. In exact rational comparisons it finds

    sum_i w_i f(u_i) in [-1.05818188426e-14,-1.05818188425e-14],
    16 sum_j |C_j| <= 3.99041112674e-17,
    whole-box upper bound < -1.05419147312e-14 < -1e-15.

The last bound is checked using the full independent rational sum,
not the rounded summaries. Complete root-sign values, all response,
normalization and inverse intervals, all nine weights and full scores,
tail constants, all eight column intervals and individual allowances,
and the exact final upper bound were inspected. Comparisons with the
producer include every finite head mass, head numerator/denominator,
score, row, offset and weighted column. Their enclosures overlap; this
is corroboration, not a claim that one expression-dependent interval
contains the other. The independent enclosures and strict inequalities
establish the conclusion without relying on producer success flags.
The replay reports 263 checks, zero failures and 13672 interval divisions;
its division guard rejects every zero-containing divisor. Python integer
and Fraction correctness remain trusted; this is not a formal proof.

The normalization and linear residual (1) agree exactly with the stated
P and 2lambda0=1/5120. Positivity of the weights therefore contradicts
pointwise W>=0 uniformly over the fixed box, as asserted. No tail sign
for W between or beyond the points is necessary for this direction.
The general density-operator citations above are unchanged: no new
integration-by-parts or stationary-diffusion theorem is imported or
reproved. Actual contact realization, actual signs, other multiplier
classes, initialization/tangency, other panels/degrees and global
continuation remain unresolved. The DAG's direct inputs are unchanged.

## Mathlib

Full matching and supporting specialized coverage were not checked;
unknown availability is not absence. The finite linear inequality,
formal inverse recurrence and series bounds here are not formalized.
