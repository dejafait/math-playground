# Lemma 936: an algebraic positive-flux member of the fixed-panel contact relaxation

## Hypotheses

For j=0,...,6 let J_j be the complete closed interval at
`/panels/0/moments/2j` in `scripts/heat/low-time-h2-uniform-195.json`,
with decimal-string key 2j. Every endpoint is interpreted as its exact
rational value. This is L917's panel [0,1/5120], with source SHA256
`f0afdc26fd2463272ee7918073b5abed7e3170a64cbf8226bf16291820acc792`.
These intervals define a finite class; actual-law inclusion additionally
retains L917/L037's directed-arithmetic and library hypotheses.

The class consists of m_j in J_j, m0>0, y0=1, y_j=m_j/m0 for 1<=j<=6,
one further real y7, and real c=(c0,c1,c2). Define, modulo t^8,

    g(t)=sum_(j=0)^7 (-1)^j y_j t^j/(2j)!,
    log g(t)=-sum_(j=1)^7 S_j t^j/j,
    M3=(y_(i+j))_(0<=i,j<=3), N3=(y_(i+j+1))_(0<=i,j<=3),
    H2=(S_(i+j+2))_(0<=i,j<=2), Delta=S2*S4-S3^2.

Require M3,N3,H2 PSD, c^T c=1, c2!=0, all three rows H2*c=0, and

    S2>3.714e-5,       9.7e-16<Delta<7.026e-15.

Let Phi be exactly the finite functional in L874(2) with d=r=2,N=6:

    b_n=sum_(i+j=n-2)c_i*c_j,
    B=-2 sum_(n=2)^5 n(2n+1)b_n S_(n+1)
       +4 sum_(n=2)^6 n b_n sum_(a=2)^(n-1) S_a S_(n+1-a),
    Phi=-156c2^2 S7+B.

For arbitrary tuples this names an algebraic functional, not an actual
theta derivative. No representing measure, actual tilt, invertibility
of every raw block, extra moment or full-support premise is imposed.

## Conclusion

This class has a member with

    5.339503291e-15 <= Phi <= 5.339503292e-15.

Thus the stated finite conditions imply neither emptiness nor Phi<=0.
This is a local obstruction to that sufficient sign mechanism. It does
not produce an actual theta contact, a failure of an actual-Xi sign,
an RH counterexample or a complete candidate solution. The constructed
N3 is singular, as the class permits; no full-support realization is
asserted. The separate step41 proof/code audit below accepts this
finite-class conclusion, with the same scope qualifications.

## Proof

### Exact root and common mass

Set the fixed raw moments to the following terminating decimals:

    m0=0.497123021571, m1=0.022972233662,
    m2=0.002962906960, m3=0.000599311666,
    m4=0.000160971754, m6=0.000020475993.

They are nearest 10^-12 rational roundings of the corresponding exact
interval midpoints, with half ties upward. Put m5=X for now and retain
the single mass m0 for all y_j. Finite coefficient extraction from
g'=g(log g)' gives

    q_j=(-1)^j y_j/(2j)!,
    S_n=-n*q_n-sum_(k=1)^(n-1) S_k q_(n-k).

This is the L917 finite-log convention. Through n=6, S2,S3,S4 and
Delta are constant in X, and S5,S6 are affine. Define

    P(X)=Delta*S6-S4^3+2*S3*S4*S5-S2*S5^2.

After multiplication by a positive rational, its exact coefficients,
in ascending order, are

    -62771292108354521989752161390673854977603807286751227007139,
     2354209566613457384125275894062626786021779646664218000000000000,
    -22072745990611555673606165989356026991593537500000000000000000000000.

Let the following exact decimals be a and b:

    a=0.0000530387415958154365906397391693872935932598188,
    b=0.00005303874159581543659063973916938729359325981881.

Exact rational substitution gives

    -8.215998683e-73 <= P(a) <= -8.215998682e-73,
     8.329330327e-73 <= P(b) <=  8.329330328e-73.

The intermediate value theorem supplies a real alpha in (a,b) with
P(alpha)=0. Take m5=alpha. No uniqueness assertion is needed: the
remaining certificates hold for every such root in this bracket.
The bracket is inside J5; its relative position in that interval is
between 0.03096974943 and 0.03096974944. All other fixed moments are
strictly inside their J_j. The complete two-sided membership slacks
are rationally enclosed in the certificate cited below; every lower
slack endpoint is positive. Thus the common-mass box condition holds.

### Exact contacts and raw PSD

The following certified enclosures are uniform over the root bracket:

    0.00003717365974 <= S2 <= 0.00003717365975,
    3.860818896e-15 <= Delta <= 3.860818897e-15.

They verify every strict H1 bound in the hypotheses, and the real
leading block D=[[S2,S3],[S3,S4]] is positive definite by Sylvester's
criterion. Division by Delta is therefore legitimate. Set

    p=(S3*S5-S4^2)/Delta,
    r=(S3*S4-S2*S5)/Delta,
    v_c=(p,r,1),       c=v_c/sqrt(1+p^2+r^2).

The first two rows of H2*v_c vanish identically by these formulas.
The third row multiplied by Delta equals P(alpha), so it also vanishes
exactly. In particular, writing u=(p,r)^T, H2 has the factorization

    H2 = [ I ; -u^T ] D [ I , -u ].

Indeed its first two entries in the last column are -D*u, and its
bottom-right entry is u^T D u by the third null row. Hence H2 is PSD.
The square root in c is the positive real one, so c is a real unit
vector with c2!=0. Its certified c2^2 is between 0.9999623958 and
0.9999623959. This normalization preserves all three null rows.

Define W=(y_(i+j+1))_(0<=i,j<=2), v=(y4,y5,y6)^T. The leading
principal minors of W have positive lower bounds

    0.04621035974,  0.00002018647578,  2.096762179e-10.

Thus W is positive definite for this candidate. Choose

    y7=v^T W^-1 v.

Import the Schur-complement PSD criterion from J. Gallier,
*The Schur Complement and Symmetric Positive Semidefinite (and
Definite) Matrices*, author version 24 August 2019,
Proposition 4.2 and Theorem 4.3, pp.9--12,
https://www.cis.upenn.edu/~jean/schur-comp.pdf . Its leading block here
is W, its column is v, and its scalar Schur complement is exactly zero.
Since W is positive definite its range is all R^3, settling the theorem's
range condition. Therefore N3=[[W,v],[v^T,y7]] is PSD, with determinant
zero. No inverse or dropped range condition for other members of the
original class is assumed. This is an applicability argument, not a
reproof of the general theorem.

M3 is positive definite by Sylvester's criterion: its four leading
principal minors have respective positive lower bounds

    1,  0.003824710777,  2.374392163e-7,  4.711710199e-13.

For completeness, the certificate also checks all 15 principal minors
of each raw matrix and all seven of H2. Every one is nonnegative;
the determinants of H2 and N3 are exactly zero, rather than intervals
merely containing zero. Leading minors are used here only to establish
positive definiteness of W and M3, not as a semidefinite criterion.

### Exact finite flux and reproducible arithmetic

With y7 as above, recompute the finite logarithm through seven and
use the normalized products c_i*c_j=v_c[i]*v_c[j]/(v_c^T v_c).
Substitution in the displayed L874 functional gives the claimed strict
positive interval for Phi. Independently contracting the full finite
heat recurrence gives exactly the same algebraic value; the endpoint
S1 terms cancel by the three exact null rows. This is evaluation of
that functional on the constructed tuple, without an assertion that
any actual theta parameter produces it.

All exact polynomial coefficients, both root brackets and endpoint
values, the complete original interval strings, moment definitions,
matrices, principal minors, flux and equality residuals are in
`scripts/heat/contact-s7-root-slice-39.json`. Reproduce with

    python3 scripts/heat/contact-s7-root-slice-39.py

The script uses only exact Fraction arithmetic for the construction
and signs. First it forms the full polynomials in X through degree
six before imposing P=0. It brackets one root by 160 rational
bisections inside J5, encloses that bracket by the displayed terminating
decimals, and rechecks their opposite signs. This refines one scalar
root bracket, not a search over other slices or a parameter sweep.

For subsequent equalities, write alpha^2=A+B0*alpha with
A=-P0/P2 and B0=-P1/P2. An element (h,k) denotes h+k*alpha. Products
reduce by that quadratic relation. For a nonconstant denominator its
conjugate product is h^2+h*k*B0-k^2*A; the implementation requires this
exact rational to be nonzero, and checks multiplication by the proposed
inverse gives exactly (1,0). All actually used real denominators are
also enclosed away from zero on the chosen bracket. Consequently
zero coefficient pairs certify exact identities at the existing real
root; small approximate residuals are never used as equalities.

For signs, enclose h+k*alpha using alpha in [a,b] by exact rational
interval arithmetic. All outward decimal summaries are themselves
checked to contain these complete rational intervals, so their printed
endpoints are exact sufficient rational bounds. The finite logarithm
is independently recomputed as sum_(r=1)^7 (-1)^(r+1)(g-1)^r/r
modulo t^8; all eight residual coefficient pairs vanish. All three null
rows vanish as coefficient pairs. The script reports 114 exact checks,
zero failures. The full `/complete_outward_sign_evidence` object was
inspected, including all membership slacks, principal-minor bounds,
inverse-denominator bounds, both root-sign pairs and strict quantities;
the selected polynomial, bracket, check and exact-residual records
were also inspected. A preview is not used as evidence.

The work specializes standard finite-log and Schur tools to this
previously undecided class. The local negative witness changes the
route decision, without asserting a new general moment theorem or
certified originality. L917's stopped determinant enclosure and the
earlier failed midpoint slice retain their original evidence. Actual
tilt/realization, initialization/tangency, other panels/degrees and
global continuation remain unresolved.

### Independent proof/code audit, 9 November 2026 (step41)

The audit accepts the unchanged witness and its finite-class conclusion.
It imports the same Gallier criterion cited above, not a stronger
moment-representation converse. The prior SPECIALIZE assessment is
`drafts/literature/2026-11-09-l936-independent-witness-audit-40.md`.
No actual tilt or theta parameter is inferred from finite membership.

The independent replay is

    python3 scripts/heat/contact-s7-independent-audit-41.py

Its full evidence is
`scripts/heat/contact-s7-independent-audit-41.json`. It reads but never
imports or executes the producer, and leaves the producer certificate
unchanged. It verifies the complete source SHA256 and all seven original
endpoint strings against the source itself. All fixed raw values, including
their midpoint-rounding rule, and the common-mass identities are checked.
Every lower and upper membership slack is strictly positive, including
the previously problematic twelfth raw moment m6. This assertion uses
exact rational endpoints; actual-law inclusion retains L917/L037's
separate analytic and directed-arithmetic contracts.

The replay independently forms log(1+h) by its finite power expansion
before imposing the quadratic relation. This reproduces all formal
S1,...,S6 polynomials, the complete P, and its positive integer scaling.
It checks the initial signs, all 160 bisections, the displayed final
bracket and the exact endpoint evaluations. Thus continuity and IVT
give an existing real alpha strictly inside the original m5 interval.
Existence is sufficient: every subsequent rational enclosure holds on
the whole bracket. No uniqueness or irreducibility assumption is used.

Rather than using the producer's conjugate-inverse implementation, the
replay uses polynomial division and extended Euclid modulo the full P.
It accepts an inverse only when the gcd is a nonzero rational constant,
verifies the exact product identity, and encloses the denominator away
from zero. Every one of the producer's 12 nonconstant inverse records
is independently verified, including its exact nonzero conjugate product,
recorded inverse and complete rational bounds. In the inspected producer,
constant denominators take the same branch with norm h^2, so zero is
rejected; the constants actually required are nonzero m0, Delta,
factorials and interval widths. At any existing bracket root the quotient
evaluation is a real algebra homomorphism, and each checked product
identity evaluates to denominator times inverse equal to 1. Therefore
all used divisions are legitimate even if P were reducible.

Gaussian elimination independently computes (p,r) and W^-1 v, instead
of using the producer's formulas/Cramer's rule. Recursive cofactor
determinants independently reproduce all 44 nonempty principal minors
of W,M3,N3,H2. Every W and M3 minor is strictly positive; every N3 and
H2 minor is nonnegative, with exact zero full determinants. The replay
also verifies all entries of the displayed H2 factorization, its three
null rows and the zero N3 Schur complement. In the Schur criterion W is
positive definite, so its range is all R^3; singular N3 is permitted.
The H2 factorization with D positive definite also proves PSD directly.
The positive normalization yields a real unit c and c2!=0. The strict
S2 and both Delta inequalities pass with the quoted bounds.

Finally the replay extracts the finite logarithm through seven, checks
every coefficient of its recurrence and compares all eight exact zero
residuals with the original evidence. It contracts the full recurrence
directly over the nine entries c_i*c_j, verifies the endpoint-term
cancellation and reproduces both B and Phi in (2). The complete rational
Phi interval lies in [5.339503291e-15,5.339503292e-15], strictly above
zero. All stored matrices, moments, normalized products, principal
minors, inverse records, flux values and outward summaries used in the
proof agree with the independent construction. The replay reports
231 checks, 34 exact record comparisons, 57 checked replay divisions
and no failures. Complete selected root, rational sign/minor, residual
and inverse evidence was inspected; producer success flags alone were
not used to establish membership or the flux sign.

A first replay stopped at its JSON comparison of integer b_n keys with
JSON string keys; all preceding mathematical checks passed. Its record
is preserved as `scripts/heat/contact-s7-independent-audit-41-first-pass.json`.
Normalizing comparison keys fixes this audit-harness serialization error;
no witness, class, producer or original evidence was changed. The final
replay passes. This is local validation of an existing obstruction,
not a new general theorem or a result beyond the sources checked.
Actual realization, initialization/tangency, other panels/degrees and
global continuation remain open.

## Mathlib

Full matching coverage and supporting specialized coverage were not
checked. This certificate and its Python arithmetic are not formalized
in Lean. The intermediate value theorem, Sylvester's criterion and
Schur-complement theorem are standard mathematical inputs; unknown
Mathlib coverage is not evidence of absence.
