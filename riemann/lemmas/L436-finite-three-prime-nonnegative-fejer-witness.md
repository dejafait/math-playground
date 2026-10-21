# Lemma 436: a fixed finite nonnegative witness for the three-prime cubic data

## Hypotheses

Use L435's audited density W, normalized Haar measure dh on the angular
three-torus, real coefficients c_v=g_v/beta, beta>0, and separately
fixed-character physical asymptotics. In particular W is continuous,
centrally symmetric, and has the absolutely convergent expansion
W(x)=sum_(v in Z^3)c_v exp(i v.x), with c_v>0, c_0=1 and c_-v=c_v.
Use its rational functions Q_p, positive numbers B_p(0), and point
a=(theta_*,phi_*,psi_*) specified by

    u_2=1+i, u_3=1+i sqrt(2), u_5=1+2i,
    u_p=sqrt(p) exp(i a_p), p=2,3,5.

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-18-three-prime-finite-nonnegative-witness.md`.
No physical sine limit, nonnegative physical product, variable character,
law realization, clipping or regulator margin is assumed.

## Conclusion

Fix n=131071 once and for all. Let

    F_n(s)=sum_(j=-n)^n (1-|j|/(n+1)) exp(i j s),
    K_n(x)=F_n(x_2) F_n(x_3) F_n(x_5),
    P(x)=[K_n(x-a)+K_n(x+a)]/2.                         (1)

Then P is real, centrally symmetric, nonnegative everywhere, has
Haar integral one, and has degree at most n in each coordinate. Its
complete finite real cosine expansion is

    P(x)=sum_(|v|_infinity<=n) w_v cos(v.a) cos(v.x),
    w_v=product_(p=2,3,5)(1-|v_p|/(n+1)),               (2)
    cos(v.a)=Re[product_(p=2,3,5)(u_p/sqrt(p))^v_p].

Both v and -v occur in (2); there is no extra factor two. Negative
powers in its coefficient formula are of nonzero algebraic numbers.
For this fixed polynomial its complete finite coefficient contraction
satisfies

    I=integral P W dh
     =sum_(|v|_infinity<=n) w_v cos(v.a)c_v
     < -1936867/131072000 < -1/100.                      (3)

An independent direct evaluation of the same finite contraction by
outward rational arithmetic gives the enclosure

    -2584151874139662159245424023/2^96
       <= I <= -2584151874139662159245423689/2^96.       (4)

Thus already the finite set of moments indexed by this cube cannot
be the cosine moments of a positive torus measure. Also, with n held
fixed before H tends to infinity, L435 gives

    E_H[Delta Bcal P(t log 2,t log 3,t log 5)]
       =beta I (log H)^2+o((log H)^2).                  (5)

This is a local REPRODUCTION specialization of a known kernel, not a
new general approximation theorem. The separate step-242 critical audit
below validates its stated finite scope and both sign certificates.
It does not resolve global mixed positivity or RH. L431's selected
finite calibration and the positive lower-dimensional marginals remain
valid. No actual/global law, actual clipped mean, capped nondegeneracy,
full-error regulator margin or new zero-exclusion range is supplied.

## Proof

### Imported kernel and central symmetrization

Import the finite kernel, its nonnegativity, mass and product formula
from Huichi Huang, *A generalized Fejer's theorem for locally compact
groups*, March 17, 2016 author manuscript,
[Propositions 2.2--2.3, pp. 4--5](https://huichihuang.wordpress.com/wp-content/uploads/2016/03/fejergr3.pdf).
Huang uses R/Z and normalized Haar measure; replacing his coordinate
by s/(2pi) gives exactly F_n above. The product proposition applies
in dimension three. Translation preserves nonnegativity and mass;
averaging the two translates does also. Since F_n(-s)=F_n(s), central
reflection exchanges the two translates, proving P(-x)=P(x).
The finite product expansion gives coefficients w_v exp(-i v.a) and
w_v exp(i v.a) for the two translates. Averaging and pairing v with
-v gives (2). This establishes P's properties without assuming W>=0
or coordinatewise reflection symmetry.

The cited approximate-identity theorem qualitatively motivates this
construction; an effective estimate and complete finite arithmetic
are still necessary here. The following calculation supplies only
that density-specific specialization, not a reproof of the general
Fejer localization theorem.

### Effective absolute first Fourier moment

Here and below all finite arithmetic constants are rational. This
also specifies exact coefficient extraction for the later contraction.
Fix p in {2,3,5}, set a0=p^(-2), K=-p^3(p-1)^2, and write

    Q_p(u)=K u^3 / [(u-1)(u-p)^2(u-a0)^2(u-p^3)].       (6)

For a root b of multiplicity m_b in the denominator, define

    H_b=K b^3/product_(d!=b)(b-d)^m_d.

The coefficient of (u-b)^(-1) at a simple root is H_b. At a double
root the coefficients of (u-b)^(-2) and (u-b)^(-1) are respectively
H_b and H_b[3/b-sum_(d!=b)m_d/(b-d)]. These formulas follow by
evaluating and differentiating the numerator divided by the other
factors at b. Their partial fractions equal (6): the difference has
no pole, hence is a polynomial, and tends to zero at infinity.
All roots are distinct and nonzero for these p, so no denominator
in these expressions vanishes.

Denote the resulting coefficients at roots 1,p,a0,p^3 respectively by
D; (O,T); (U,V); J, listing the simple-pole coefficient first and
the double-pole coefficient second. Put

    A=-O/p+T/p^2, B=T/p^2, C=-J/p^3,
    E=U/a0-V/a0^2, G=V/a0^2, b0=A+C.

Expand the outer poles p,p^3 in nonnegative powers of u, and the
inner poles 1,a0 in negative powers. All expansions converge absolutely
on 1<|u|<p, so uniqueness of Laurent coefficients in L435 gives

    B_p(j)=(A+B j)p^(-j)+C p^(-3j),           j>=0,
    B_p(-h)=D+(E+G h)a0^h,                   h>=1,     (7)
    B_p(0)=b0>0.

The double inner pole contributes V(h-1)a0^(h-2), zero when h=1;
this is included in (7). Although E,G are negative, each coefficient
B_p(j) is positive by L435's original convergent positive sum.
One must use that positivity, rather than separately treating E,G
as positive terms.

For a real R in (1,p), define the positive and negative parts of
the Laurent mass and absolute first moment by

    Pp(R)=A/(1-z)+B z/(1-z)^2+C/(1-w),
    Np(R)=D/(R-1)+E t/(1-t)+G t/(1-t)^2,
    Pm(R)=A z/(1-z)^2+B z(1+z)/(1-z)^3+C w/(1-w)^2,
    Nm(R)=D R/(R-1)^2+E t/(1-t)^2+G t(1+t)/(1-t)^3,
    z=R/p, w=R/p^3, t=a0/R.                            (8)

These are respectively sum_(j>=0)B_p(j)R^j,
sum_(h>=1)B_p(-h)R^(-h), and their index-weighted sums.
They follow by summing the geometric series and its first two
derivatives; |z|,|w|,|t|<1 justifies those operations.

The following strict bounds use (8) at rational radii L<sqrt(p)<U.
Every radius assertion follows by squaring positive rationals.

| p | L | U | B_p(0) | S_p upper | M_p upper |
|---|---|---|---|---|---|
| 2 | 141421/100000 | 141422/100000 | 571520/329623 | 103/10 | 42 |
| 3 | 173205/100000 | 173206/100000 | 152029305/128665108 | 61/10 | 151/10 |
| 5 | 223606/100000 | 223607/100000 | 603597109375/581483140832 | 39/10 | 31/5 |

Here

    S_p=sum_(j in Z)B_p(j)p^(j/2)/b0
        <=[Pp(U)+Np(L)]/b0 < (table upper),
    M_p=sum_(j in Z)|j|B_p(j)p^(j/2)/b0
        <=[Pm(U)+Nm(L)]/b0 < (table upper).              (9)

The inequalities before evaluating (8) follow term by term from the
positivity of B_p(j); the positive-index parts increase with R and
the negative-index parts decrease with R. All table comparisons are
exact rational substitutions in (6)--(8), not decimal approximations.
The full coefficients, cleared identities and rational intermediate
values are recorded in the certificate described below. In particular
this computation does not truncate an infinite local tail.

L435 expresses c_v as the central symmetrization of the product of
a_p(j)=B_p(j)p^(j/2)/B_p(0). Tonelli and (9) imply

    sum_v (|v_2|+|v_3|+|v_5|)c_v
       =M_2 S_3 S_5+S_2 M_3 S_5+S_2 S_3 M_5
       <1995293/1000<2000.                              (10)

Absolute index weights are unchanged by central reflection, which
is why the unsymmetrized product gives exactly this moment. All
normalizing b0 factors have been retained.

### One selected degree and its strict sign

Extend w_v to all Z^3 by replacing each factor with
max(1-|v_p|/(n+1),0). Thus w_v=0 outside the finite cube, 0<=w_v<=1,
and the elementary product inequality gives

    1-w_v <= (|v_2|+|v_3|+|v_5|)/(n+1).

Absolute convergence and (10) therefore give

    |sum_v w_v c_v exp(i v.a)-W(a)|
       <=sum_v(1-w_v)c_v < (1995293/1000)/(n+1).         (11)

By (2) and L435's Fourier coefficients, the finite sum on the left
is real and equals I. Equivalently convolution at either a or -a
has the same value, since W is centrally symmetric. L435's audited
exact negative-point bound is

    W(a)<-2845531063062452632131264/
                92613754219265544503359375 < -3/100.

Select the single degree n=2^17-1 from this error budget, before
evaluating its finite integral. Combining with (11) gives

    I < -3/100+1995293/(1000*131072)
      =-1936867/131072000 < -1/100.

No degree escalation or growing-minor search is used. This proves
the strict sign independently of the direct enclosure (4).

### Complete exact finite contraction

For |z|<1 define the following finite polynomials; the rational
expressions are their closed forms:

    f_n(z)=sum_(j=0)^n(1-j/(n+1))z^j
          =[(n+1)-(n+2)z+z^(n+2)]/[(n+1)(1-z)^2],
    g_n(z)=sum_(j=0)^n j(1-j/(n+1))z^j=z f_n'(z)
          =z/(n+1){(n+2)(z^(n+1)-1)/(1-z)^2
             +2[(n+1)-(n+2)z+z^(n+2)]/(1-z)^3}.        (12)

The first identity follows by subtracting the differentiated finite
geometric sum from that sum, and differentiating gives the second.
At each u_p specified in the hypotheses, (7) now gives the complete
local finite weighted sum

    T_p=1/b0 {A f_n(u_p/p)+B g_n(u_p/p)+C f_n(u_p/p^3)
          +D[f_n(1/u_p)-1]+E[f_n(a0/u_p)-1]
          +G g_n(a0/u_p)},
    I=Re[T_2 T_3 T_5].                                 (13)

All four types of arguments in (12)--(13) have modulus less than one:
their moduli are p^(-1/2), p^(-5/2), p^(-1/2), p^(-5/2).
Thus denominators 1-z are nonzero. The subtractions of 1 exclude
exactly the h=0 negative-index terms. Product factorization in
(13) evaluates every character in the cube, including mixed-sign
triples, before taking the real part. No term is omitted, and the
imaginary parts of the local factors cannot be discarded.

Run `python3 scripts/discriminant/three_prime_finite_fejer_witness.py`.
It writes the complete certificate to
`scripts/discriminant/three_prime_finite_fejer_witness_certificate.json`.
Its exact Fraction arithmetic checks each full partial-fraction
identity after clearing denominators, each constant term against
L435's convergent valuation formula, both radius squares and all
six table bounds, (10), the imported negative-point comparison and
the selected a priori sign bound. All 22 checks pass, failures=[].

For (13), every real arithmetic operation is rounded outward to a
dyadic interval with denominator 2^96. The integer
r=floor(sqrt(2)*2^96) is obtained by integer square root and checked
by r^2<2*2^192<(r+1)^2; hence the initial interval for sqrt(2) is
rigorous. Complex products use the full real/imaginary formula;
inverses use the conjugate divided by the squared modulus. Every
division interval is checked to exclude zero. Powers are enclosed
by repeated squaring, including both finite boundary powers in
(12), rather than dropping them as small. The certificate records
all 2993 real interval operations and replays every endpoint
inclusion by exact rational comparisons, with no replay failures.
By induction on that operation record, the exact algebraic values
in (13) belong to the recorded intervals, proving (4).

The complete local coefficient/bound records, finite contraction,
effective bound, checks, failures and replay failures were inspected
through the scoped JSON inspector. The full tape is automatically
replayed, not claimed to have received a separate human-style audit.
Its implementation is corroboration of the independent sign proof
(9)--(11); neither an approximate decimal nor a bounded preview is
used to establish the sign. Full evidence and reproduction commands
are retained for a later critical audit.

### Finite consequences and limitations

If a positive measure mu had the finitely many cosine moments c_v
in this cube, (2) would imply integral P dmu=I<0, contrary to
P>=0. This direct finite argument does not require Fourier uniqueness
or an infinite family of moment constraints. It does not say that
L431's much smaller selected calibration was invalid.

Substitute x=(t log 2,t log 3,t log 5) into the finite identity (2).
Each term is one of L435's separately fixed cosine characters.
Sum those finitely many asymptotics, with n already fixed, to obtain
(5). No infinite character sum or degree depending on H is passed
through a height limit. Constants and onset can depend on this very
large fixed polynomial; no effective onset or practical enumeration
of its cube is claimed. A negative product average with a nonnegative
test does not distinguish the two possible opposite-sign orientations
of Delta and Bcal, and it supplies no clipped or regulator estimate.
All independent global gaps stated in the conclusion remain open.

### Separate critical audit — 2026-10-19, step 242

This RESEARCH / REPRODUCTION / proof_audit uses the prior SPECIALIZE
assessment `drafts/literature/2026-10-18-finite-three-prime-witness-critical-audit.md`.
The audit reuses Huang's inspected Propositions 2.2--2.3 and audited
L435, and finds no defect in (1)--(13). It validates a local finite
input; it establishes no new general theorem beyond the checked sources
or RH positivity assertion. No mathematical input or assembly changes,
so DAG.md and PROOF.md are unchanged.

**Kernel, normalization and symmetry.** Huang's n+1 convention gives
exactly the weights in (1) after angular rescaling. Each factor has
mass one and is nonnegative, so both translates and their average
have those properties. The coefficient of exp(i v.x) in the average
is w_v cos(v.a), real and invariant under v->-v. Replacing each
exponential by its cosine in this full symmetric sum preserves the
sum, with both signs of v still present and no new factor two.
All three numbers u_p have modulus sqrt(p) and are nonzero, so their
integer powers specify these coefficients exactly. No individual
coordinate reflection of W is used. Since c_-v=c_v, integration of
each cosine against W gives c_v, justifying the first equality in (3).

**Laurent coefficients and first moment.** Converting L435's Q_p
to (6) uses (p^2u-1)^2=p^4(u-p^(-2))^2 and
p^3-u=-(u-p^3), producing K=-p^3(p-1)^2. At a double root,
the derivative of the pole-removed rational function is precisely
H_b times the stated logarithmic derivative. The proper partial
fraction decomposition has no polynomial term. The independent
checker below reconstructs the entire cleared numerator at each p;
every coefficient vanishes, not just its value at the selected point.

For an outer simple pole the coefficient of u^j is -b^(-j-1);
for an outer double pole it is (j+1)b^(-j-2). These give A+Bj and C.
At an inner pole, 1/(u-b) has coefficient b^(h-1) at u^(-h),
whereas 1/(u-b)^2 has coefficient (h-1)b^(h-2) for h>=2
and zero for h=1. Thus the inner coefficient is D plus
U a0^(h-1)+V(h-1)a0^(h-2), exactly (7); at h=1,
(E+G)a0=U, with no spurious double-pole term. The constant term
is A+C and agrees with the audited L435 normalization. The annulus
1<|u|<p permits all these expansions and their differentiated sums.

Differentiating the positive-index geometric series once and twice,
and weighting the negative-index series by h, gives all four formulas
in (8). Monotonicity is asserted for their complete series of positive
coefficients supplied by L435, not for the signed summands involving
E and G. Positive indices use U; negative indices use L. The strict
radius squares, full rational substitutions and all six table bounds
were independently checked. Finiteness precedes Tonelli for the joint
first moment: the product mass and its three index-weighted terms are
finite. Central reflection preserves the sum of absolute indices, so
the normalized moment is exactly the three products in (10).
Their stated upper bounds give 1995293/1000 without a missing factor
from symmetrization or normalization.

Inside the cube the inequality 1-product(1-x_p)<=sum x_p applies;
outside it at least one |v_p|>=n+1 makes the same stated inequality
valid with w_v=0. Absolute Fourier convergence now proves (11).
The imported strict bound on W(a) is below -3/100. Hence the
preselected n=131071 gives the exact upper bound
-1936867/131072000<-1/100. This analytic sign argument does not
depend on the direct finite interval enclosure.

**Finite formulas, arithmetic and independent computation.** Write
m=n+1. Subtracting (1/m) times the first weighted finite geometric
sum from the unweighted one gives the numerator
m-(m+1)z+z^(m+1) in f_n. Its derivative is
(m+1)(z^m-1), which gives exactly g_n in (12), retaining both
z^(n+1) and z^(n+2). All arguments in (13) have the claimed moduli
strictly below one, so no rational denominator vanishes. The two
subtractions remove exactly the h=0 negative-index terms. Multiplying
the three complete local finite Laurent sums produces the whole cube.
Taking the real part centrally symmetrizes their coefficients; it does
not replace the complex factors by their real parts.

Read the complete construction program and inspect the full /local,
/effective_bound, /finite_contraction, /checks and failure fields of
its saved certificate. The assignment of arguments, coefficients and
normalization in `smoothed_local` matches (13). The real arithmetic
uses exact Fraction endpoints rounded down/up to the dyadic grid.
Addition, negation and the four-corner product enclose the respective
operations. Inversion uses [1/b,1/a] only when ab>0. Complex inversion
uses the conjugate divided by the enclosed squared modulus; correlation
loss may widen a box but cannot invalidate inclusion, and every actual
division box excludes zero. Repeated squaring preserves inclusion by
induction and does not discard the finite boundary powers.

Run `python3 scripts/discriminant/three_prime_finite_fejer_audit.py`.
It reads the saved construction certificate without importing or running
the construction program, and writes the full audit certificate to
`scripts/discriminant/three_prime_finite_fejer_audit_certificate.json`.
It checks all 2993 operation entries, their earlier-operand indexing,
constant inputs, the strict squared sqrt(2) bracket, all 15 nonzero
division intervals and the recorded output-to-tape indices. Every
endpoint inclusion passes. This validates the entire tape, rather
than its original self-reported success flag.

For an independent check that the implemented contraction represents
the full finite sum, the audit also uses 160-bit outward integer-grid
arithmetic and a different finite evaluation. For m=1 start with
q=z, S0=1, S1=S2=0. If Sk=sum_(j=0)^(m-1) j^k z^j and q=z^m,
splitting the length-2m sum at m gives

    S0_new=S0+q S0,
    S1_new=S1+q(S1+m S0),
    S2_new=S2+q(S2+2m S1+m^2 S0), q_new=q^2.

These identities follow term by term from (j+m)^k for k=0,1,2.
Seventeen doublings reach m=n+1 exactly. Then
f_n=S0-S1/m and g_n=S1-S2/m evaluate every term of (12)
without using its rational closed forms or omitting any boundary power.
The independent rational grid rounds each product and reciprocal
outward and checks all division signs. Its initial sqrt(2) enclosure
is again verified by exact integer squares, now at 160 bits.

All six independent local real/imaginary enclosures and both final
product enclosures lie inside the original saved intervals. In particular
the independent real product is enclosed by

    [-23834594134925622024284065285143521321786631557 /
       730750818665451459101842416358141509827966271488,
     -5958648533731405506071016321285880330446474869 /
       182687704666362864775460604089535377456991567872],

whose upper endpoint is below -1/100. Thus (4), including both exact
endpoints, survives the independent method. All 32 audit checks pass,
with no tape or other failures; the full relevant result fields were
inspected using the scoped JSON inspector. The certificate records the
source-certificate SHA-256. Neither approximate decimal evaluation nor
a bounded preview is the arithmetic evidence.

**Consequences and remaining limits.** The finite cosine expansion
integrates to I for any measure with the stated finite cosine moments.
The zero character fixes its mass at one; positivity would contradict
P>=0 and I<0. No sine data, symmetry assumption on that measure, or
infinite-measure uniqueness theorem is needed. For the physical limit,
fix this entire polynomial first. There are finitely many coefficients,
so for any error tolerance one can choose a common height onset for
their finitely many separately fixed L435 remainders and then sum with
their fixed absolute coefficient weights. This proves (5), with no
claim about effective onset, a degree growing with H, or an infinite
character limit. The negative average gives no distinction between
Delta>0,Bcal<0 and Delta<0,Bcal>0. Actual clipping, capped
nondegeneracy, actual/global realization, L413's full-error margin
and global mixed positivity remain unresolved; L431's smaller
calibration and the positive marginals are unaffected.

## Mathlib

Full matching coverage for this finite three-prime specialization,
its physical asymptotic and its effective certificate has not been
checked. Huang's precise finite-kernel statements are the imported
general results; L435 supplies the audited analytic interface. The
exact arithmetic program is not a Lean proof. Unknown matching
Mathlib coverage is not evidence of absence.
