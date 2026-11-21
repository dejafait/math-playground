# Lemma 921: a rank-two obstruction to the finite-moment origin-sign implication

## Hypotheses

Use the coefficient conventions of L874/L917 and the origin quadratic
J of L918(5). The finite relaxation consists of real y0,...,y6 with
y0=1, y1>0 and

    M3=(y_(i+j))_(0<=i,j<=3) PSD,
    N2=(y_(i+j+1))_(0<=i,j<=2) PSD.

In the formal ring R[x]/(x^7), define

    g(x)=sum_(k=0)^6 (-1)^k y_k x^k/(2k)!,
    log g(x)=-sum_(k=1)^6 S_k x^k/k,
    1/g(x)=sum_(k=0)^6 a_k x^k,       a0=1,
    H2=(S_(i+j+2))_(0<=i,j<=2).

Require H2 PSD and a real unit vector c=(c0,c1,c2) with c2!=0 and
all three rows H2*c=0. Define, without changing L918's convention,

    J=sum_(i,j=0)^2 c_i c_j ((i+j+2)a_(i+j+2)+a_(i+j+1)).

These are exactly the fixed relaxation in the prior assessment
`drafts/literature/2026-11-09-l918-origin-joint-elimination-test.md`.
They do not assert equality with actual theta moments, a parameter
lambda in (0,1/20], its exponential-tilt relations, full support,
higher moments, or a representing measure for y.

## Conclusion

This finite relaxation does not imply J>=0. In fact put epsilon=10^(-6),

    (S1,S2,S3,S4,S5,S6)=(1,epsilon,epsilon,2epsilon,5epsilon,13epsilon),
    c=(1,-3,1)/sqrt(11),

and define y by g=exp(-sum_(k=1)^6 S_k x^k/k) modulo x^7. Explicitly,

    y0=1,
    y1=2,
    y2=2999997/250000,
    y3=2999997/25000,
    y4=20999790000063/12500000000,
    y5=37802645999811/1250000000,
    y6=415386279060290993763/625000000000000.

For this one tuple M3 and N2 are positive definite, H2 is PSD of
rank exactly two, all three null rows and normalization hold, and

    J=-6533305000003999999/88000000000000000000,
    -3/40 < J < -7/100 < 0.                              (1)

Thus the obstruction does not rely on H2=0 or a singular leading
two-by-two logarithmic block. It blocks an origin-sign certificate
using only the nominated finite constraints, even with that leading
block positive definite. It gives no actual-theta contact or negative
actual-theta J. No representing measure is claimed. It neither
disproves RH nor rules out an origin-sign argument using more actual
theta information. The full compact residual, contact existence,
flux, initialization/equality cases, higher degrees and global
continuation remain open. This is a checked local obstruction, not a
certified originality claim. The separate step211 audit below accepts
its finite arithmetic and scope, without strengthening the conclusion.

## Proof

### Interface and applicability of the known raw-moment conditions

At an actual contact, L874/L917 use x=z^2 and
y_k=E[u^(2k)] under the normalized positive theta density. All the
needed moments are finite. The raw-moment and localizing conditions
are the specialization of M. Laurent, *Sums of squares, moment
matrices and optimization over polynomials*, author manuscript
updated 6 February 2010, Lemma 4.2(i)-(ii), printed pp. 54-55:
https://homepages.cwi.nl/~monique/files/moment-ima-update-new.pdf.
The theorem and its proof cases were inspected in the saved assessment.
Here its nonnegative variable is v=u^2, its truncation is t=3,
and its localizing polynomial is v. Since ceil(deg(v)/2)=1,
the localizing matrix has order 2. Concretely the two quadratic
forms are E[(sum_(i=0)^3 b_i v^i)^2] and
E[v(sum_(i=0)^2 b_i v^i)^2], respectively. This verifies the
specialization and uses moments only through y6. The theorem gives
necessary conditions; no converse, flat extension, infinite kernel
ideal or representation of a logarithmic matrix is imported.

The sign interface of L918(5) can be checked without assuming its
remaining conclusions. The L874 finite definition gives, for n>=2,

    T_n(u)=a_n-a_(n-1)u^2/2+O(u^4).

Therefore u^2 R(u) has coefficient -sum_(i,j)(i+j+2)c_i c_j
a_(i+j+2) at u^2, and sum_i c_i u V_i'(u) has coefficient
-sum_(i,j)c_i c_j a_(i+j+1). The fixed density correction
c2^2(13u^12+s_lambda(u)u^13) is O(u^12), because the actual
score is smooth near zero and K(0)>0 as used in L918. This confirms
W_*(u)/u^2 -> -J with precisely the stated inverse coefficients.
This interface check is not a full independent audit of L918's
density identity or tail proof. No sign theorem is imported from
the zero-mean density rule.

### One exact joint-row reduction, retaining singular cases

Put h=S1, b=S2, r=S3, p=c0/c2 and q=c1/c2. Division by c2 is
permitted; no division by c0, c1, S2 or any minor is made. The
three rows in order give exactly

    S4=-pb-qr,
    S5=pqb+(q^2-p)r,
    S6=(p^2-pq^2)b+(2pq-q^3)r.                           (2)

Conversely these identities imply all three null rows for the vector
(p,q,1). With

    A=[[b,r],[r,-pb-qr]],  B=[[1,0,-p],[0,1,-q]],

one has H2=B^T A B. Thus H2 PSD is equivalent to A PSD: one
direction follows from this congruence and the other from its upper
principal block. This remains valid when A is singular or zero.
Unit normalization gives c2^2=1/(1+p^2+q^2); the denominator is
strictly positive with no lower bound for |c2| assumed.

The L917 finite coefficient convention, applied also to 1/g, gives

    n a_n=sum_(k=1)^n S_k a_(n-k),   1<=n<=6.            (3)

Indeed (1/g)'=(sum S_k x^(k-1))(1/g) to the required orders.
Use (2) in (3) and keep all signed terms. The exact reduced expression is

    (1+p^2+q^2)J
      =p^2(2a2+a1)+2pq(3a3+a2)+(q^2+2p)(4a4+a3)
                         +2q(5a5+a4)+(6a6+a5),          (4)

where every a_n is the polynomial in h,b,r,p,q determined by
(2)-(3). This is a finite signed expression, not a presumed positive
decomposition. No extra shifted logarithmic rows or higher-degree
PSD assumptions have been inserted. Equation (4) applies also in
the zero-coordinate and singular-minor cases. One fixed specialization
of this joint reduction suffices to test the proposed implication.

### The single witness and every constraint

In (2) choose h=1, b=r=epsilon=1/1000000, p=1 and q=-3.
This is a single exact tuple, with no parameter or support-family
sweep. It gives the displayed S values and

    H2=epsilon*[[1,1,2],[1,2,5],[2,5,13]],
    A=epsilon*[[1,1],[1,2]].

A is positive definite: its first entry and determinant are epsilon
and epsilon^2. H2's one-by-one principal minors are epsilon,
2epsilon,13epsilon; its two-by-two principal minors in index order
{0,1},{0,2},{1,2} are epsilon^2,9epsilon^2,epsilon^2; its determinant
is zero. This verifies every H2 principal minor and rank exactly two.
Its product with (1,-3,1) is epsilon*(0,0,0). Also
(1^2+(-3)^2+1^2)/11=1 and c2^2=1/11>0.

For explicit verification of the raw moments, let q_n=[x^n]g and q0=1.
The coefficient identity from L917 reads

    n q_n=-sum_(k=1)^n S_k q_(n-k).

It yields the stated y_n=(-1)^n(2n)!q_n. Equivalently these rational
y values, substituted into the finite logarithm
log(1+w)=sum_(j=1)^6 (-1)^(j+1)w^j/j modulo x^7, give exactly
the displayed S values; the full six zero residuals are saved in the
certificate below. This inverse check guards against a convention
error or a tuple specified only in logarithmic coordinates.

For completeness all nonempty principal minors of the two raw
matrices are listed here. Every denominator and numerator in these
tables is strictly positive. Index sets are zero-based.

| Index set | Principal minor of M3 |
| --- | --- |
| 0 | 1 |
| 1 | 2999997/250000 |
| 2 | 20999790000063/12500000000 |
| 3 | 415386279060290993763/625000000000000 |
| 0,1 | 1999997/250000 |
| 0,2 | 47999484000153/31250000000 |
| 0,3 | 406386297060281993763/625000000000000 |
| 1,2 | 17999397000773999811/3125000000000000 |
| 1,3 | 402583205487644913438007371/78125000000000000000 |
| 2,3 | 1577824406238544544434929497607069/7812500000000000000000000 |
| 0,1,2 | 23998968001781999541/7812500000000000 |
| 0,1,3 | 244389413458277916381007371/78125000000000000000 |
| 0,2,3 | 3303947836043410337156986379045739/19531250000000000000000000 |
| 1,2,3 | 297903073633930039500373484585529464373/976562500000000000000000000000 |
| 0,1,2,3 | 339515649023856448018032344670589127763/2441406250000000000000000000000 |

| Index set | Principal minor of N2 |
| --- | --- |
| 0 | 2 |
| 1 | 2999997/25000 |
| 2 | 37802645999811/1250000000 |
| 0,1 | 6000002999991/62500000000 |
| 0,2 | 14401331999901/312500000 |
| 1,2 | 126047942910729029294996031/156250000000000000000 |
| 0,1,2 | 14410339184192398082999433/39062500000000000000 |

These finite determinants can be verified directly by the Leibniz
formula from the stated y values. In particular all leading principal
minors are positive, so the standard Sylvester criterion makes M3
and N2 positive definite. Thus every specified raw PSD condition,
not only the logarithmic null constraints, is satisfied; y0=1 and
y1=2>0 are explicit. Nothing in this verification asserts a measure.

Finally (3) gives

    (a0,a1,a2,a3,a4,a5,a6)=
      (1,1,1000001/2000000,66667/400000,
       333342000001/8000000000000,
       66680666669/8000000000000,
       22278111119666667/16000000000000000000).

The convolution of this series with g is 1 modulo x^7. In (4) the
five signed weights are (1,-6,11,-6,1), and the normalization divisor
is 11. Substitution gives exactly (1). Both comparisons in (1)
follow by multiplication by the positive denominators. Hence all
the hypotheses of the relaxation hold and its proposed conclusion
J>=0 fails, as claimed.

### Exact certificate, scope and stopping decision

Reproduction from the active notebook:

    python3 scripts/heat/l918-joint-origin-relaxation-209.py

The standard-library integer/Fraction program writes the full
certificate to `scripts/heat/l918-joint-origin-relaxation-209.json`.
It uses the Leibniz determinant formula for every principal minor,
checks the finite log independently by its truncated power series,
checks the inverse by both the logarithmic recurrence and direct
convolution recurrence, and checks all null rows, the congruence,
normalization and the two exact formulas for J. All 45 checks pass;
there are 15 positive M3 minors, 7 positive N2 minors, 6 positive
and 1 zero H2 minors. It uses no floating-point or interval-library
correctness premise. The complete moment, inverse, J, principal-minor,
row and check fields were inspected, not merely previewed. These
checks support the finite proof, not an independent later audit.

This finishes the single authorized joint-row attempt with a scoped
negative result. In particular it is not another unsigned remainder
or a failed numerical search. Its assumptions omit equality with the
actual theta moments, the lambda-dependent exponential tilt and
actual parameter band, the actual full-support density, and every
unprescribed higher-moment/analytic relation. Even though the known
first two logarithmic principal-minor signs also hold here, none of
the quantitative actual-theta moment bounds is asserted. Neither
the existence nor the sign of an actual contact follows.
The finite-relaxation sign route stops here; a future actual-theta
argument would need a separately assessed additional input. No compact
residual tuning, further tuple, changed band or continuation proof
is authorized by this obstruction.

### Independent fixed-witness audit, 9 November 2026 (step211)

The unchanged SPECIALIZE assessment for this exact audit was available
before invocation. Its Laurent coverage is reused; no converse moment
theorem, new literature claim, or actual-theta sign is needed. The audit
accepts the stated finite obstruction and only the local coefficient
interface of L918(5). L918's other conclusions remain unaudited.

The general row reduction is valid without omitted coordinate cases.
Divide H2*c=0 by c2, which is nonzero by hypothesis. The first row
gives S4=-pb-qr; substituting that value into the second row gives S5,
and the third then gives S6 as in (2). Reversing these substitutions
proves the converse. Multiplying B^T A B gives the six specified
entries of H2. If A is PSD, congruence gives H2 PSD; if H2 is PSD,
its leading principal block A is PSD. Neither direction inverts A.
Thus singular A and p=0 or q=0 are retained. The norm is always
1+p^2+q^2>0. Grouping the nine terms of J by i+j gives exactly
the five weights of (4), including its factor c2^2. No additional
row, shifted PSD condition, or higher coefficient is used.

For the fixed witness the independent program

    python3 scripts/heat/l921-independent-audit-211.py

starts with the seven literal rational y values printed above. It does
not import or execute the generating program. It computes the finite
logarithm from powers of g-1, and the reciprocal from the finite
geometric series sum_(k=0)^6 (1-g)^k, rather than either generating
recurrence. Since g-1 has zero constant term, omitted powers have
degree at least seven, so these are exact identities modulo x^7.
They reproduce every S and a value displayed in the proof. Direct
convolution is 1, and the logarithmic derivative recurrence also holds.

Each principal determinant is recomputed by rational Gaussian
elimination with pivot search and row-swap sign, independently of
the original Leibniz computation. The audit compares all 29 exact
values against the complete original certificate, and all 22 raw
values against the canonical tables above. All agree: M3 has 15
strictly positive minors, N2 has 7, and H2 has 6 positive minors and
one zero determinant. Sylvester's criterion therefore gives strict
raw positive definiteness. The positive leading H2 minor and zero
determinant give rank exactly two; its displayed congruence proves
PSD. Its three rows annihilate (1,-3,1), whose squared norm is 11.
Dividing this vector by sqrt(11) preserves the null rows, gives a
unit vector and c2^2=1/11. Both J formulas reproduce (1), including
the strict bounds and the required threshold zero.

The full independent certificate is
`scripts/heat/l921-independent-audit-211.json`: 58 exact checks, no
failures. Its complete relevant values were compared, not just a
preview or the original pass flags. Integer/Fraction arithmetic and
ordinary Python execution are trusted; no Decimal, interval or theta
quadrature contract enters this finite verification.

The sign convention was checked directly from the finite L874
definition: T_n=a_n-a_(n-1)u^2/2+O(u^4). Thus u^2 R contributes
-sum_(i,j)(i+j+2)c_i c_j a_(i+j+2) to its u^2 coefficient;
the row-derivative sum contributes -sum_(i,j)c_i c_j a_(i+j+1).
Smoothness of the actual score near zero makes the density correction
O(u^12). Hence the interface is -J, with x=z^2 as stipulated, not
its negative. This verifies that the finite obstruction concerns the
intended necessary origin condition. It does not instantiate the
residual at the artificial tuple as an actual-theta function.

In particular no actual parameter lambda, equality to its normalized
moments, exponential-tilt relations, full-support density, or higher
moment/analytic constraints have been checked for this tuple. Those
are essential missing hypotheses for an actual-contact conclusion.
No representing measure is asserted or needed to refute the finite
implication. The audit supplies local verification of the existing
negative result, with no progress beyond the checked source scope
claimed. Stop this finite-relaxation mechanism; the actual origin,
compact residual and flux signs remain open.

## Mathlib

Full matching coverage of this finite-relaxation obstruction and the
theta origin-sign interface has not been checked. Supporting Mathlib
coverage of formal power series and principal-minor criteria has not
been checked either; availability is unknown, not asserted absent.
No formal sign or realization theorem is imported. Reference:
https://leanprover-community.github.io/mathlib4_docs/.
