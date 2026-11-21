# Corollary 948a: the complete fixed signed replacement budget fits the margin

## Hypotheses

Use L938's actual density v, all34 signed rows, twelve labelled factors,
factorials and retained normalization M_0^12. Keep its degree256 rational
kernel polynomial p,257 nodes,theta cutoff8,precision200,coefficient
grid10^-120 and full uniform residual bound epsilon on[0,8]. Write
r=k-p, where k(x)=K(sqrt(x)), and use exactly L948's signed response,
complete second-order remainder and full-degree Bernstein allowance A_1.
The tilt is1/10, the shell[4,8] has sixteen quarter-cells, and the
residual variable has the single interval[0,1]. No parameter is changed.

All numerical conclusions retain the inherited theta inclusion,
derivative-prefix integer multiplication, directed arithmetic and
Python exact-integer/Fraction execution contracts. L948's saved exact
prefixes d_(k,l),0<=l<=1411, are reused. They and the theta producer
are not independently audited here. No residual sign, density sign,
RH premise, effective global join or independence of residual values
is assumed. The independent step92 audit below validates this local
specialization under those contracts. This is an application of the
approved Taylor/beta/Bernstein methods, not a new general theorem.

## Conclusion

Let m=8.935649629627030*10^-35 be L947's qualified positive margin.
There is a certified rational upper bound B for the complete allowance
A_1+A_2 in L948, such that

    integral_4^8 exp(E/10)|v(E)-v_p(E)|dE <= A_1+A_2 <= B,
    8.078176384036186*10^-50 <= B <=8.078176384036187*10^-50,
    B <8.079*10^-50 < m.                                      (1)

The displayed two-sided interval encloses the computed upper bound B,
not the actual error or the exact coefficient allowance A_1. Every
degree through the full response degrees(2816,2822) is paid, on every
one of the sixteen fixed cells. In particular, no small selected
coefficient is substituted for a complete norm bound.

This pays one component of a possible B_4 certificate. The polynomial
negative part on[4,8], the actual tail beyond8, head/global primitive
variation, parameter signs, contacts, other degrees and realization
remain open. There is no RH resolution or global crossing conclusion.

## Proof

### The precise positive coefficient functional

Retain L948's notation D=2816,N=2822,C,d_(k,l),f_(k,l), and

    Q(E,y)=sum_(k=0)^6 sum_(l=0)^D
                 f_(k,l) E^l y^(l+6-k)(1-y)^k,
    w(y)=y^(21/2)(1-y)^(-1/2),
    f_(k,l)=d_(k,l)4^h h!/[2C^11(2k)!(2h)!], h=17-k+l.

For a polynomial R with these degree bounds let

    S(R)=sum_(a,i,j) |b_(a,i,j)(R)| m_(a,i) nu_j,              (2)

where b,m,nu are exactly L948(6)'s coefficients and positive rational
masses. Thus A_1=exp(4/5)epsilon*pi^6 S(Q). Finite coefficient
linearity gives S(R+T)<=S(R)+S(T). If R has nonnegative coefficients
in those bases, the partition of unity and beta integration give

    S(R)=pi^-1 integral_4^8 E^17 integral_0^1 w(y)R(E,y)dy dE. (3)

All integrals here are finite; w has positive beta parameters23/2,1/2.
L948 already justifies the full residual response and its singular
faces by absolute Fubini. The present argument bounds its prescribed
coefficient allowance, so it controls absolute density error before
integrating E. No cancellation of signed E integrals is invoked.

We use the positive Bernstein basis and its binomial partition of
unity as in Farouki, *The Bernstein polynomial basis: a centennial
retrospective*, [author slides](https://faculty.engineering.ucdavis.edu/farouki/wp-content/uploads/sites/51/2021/07/Bernstein-polynomial-basis.pdf),
PDF pp12,16-18, assessed in assessment85 and reused in assessment87;
the accessible alternate author copy was inspected in assessment90.
The composition identities below are written out to justify this
specific coefficient bound. Positive beta/gamma evaluation uses
[DLMF5.12.1](https://dlmf.nist.gov/5.12#E1) and
[DLMF5.5.1,5](https://dlmf.nist.gov/5.5#E5), with strictly positive
arguments throughout; no extra theorem or unverified range claim is
imported.

### Complete control of the signed prefix by positive composition

Put J=1411 and split Q=Q_<=J+Q_>J exactly. Define

    F_k(z)=sum_(l=0)^J t_(k,l) z^l,  t_(k,l)=8^l f_(k,l).

Then, without approximation,

    Q_<=J(E,y)=sum_(k=0)^6 y^(6-k)(1-y)^k F_k(Ey/8).          (4)

Write F_k in degree D Bernstein form on[0,1], with coefficients c_(k,j).
The usual binomial expansion of z^l(z+(1-z))^(D-l) gives exactly

    c_(k,j)=sum_(l=0)^min(j,J) t_(k,l) binom(j,l)/binom(D,l).
                                                                    (5)

Suppose |c_(k,j)|<=M_k for all0<=j<=D. We now prove the requisite
coefficient inequality on each original cell, not just a pointwise
inequality for F_k. Set x=E/8. Every B_j^D(xy) has nonnegative
coefficients in the tensor Bernstein basis of degrees(D,D) in(x,y).
Indeed,

    B_j^D(xy)=binom(D,j)x^j y^j [x(1-y)+(1-x)]^(D-j).

Expanding the bracket yields positive multiples of
x^(j+s)(1-x)^(D-j-s)y^j(1-y)^s. Elevating its y degree from j+s
to D by multiplication by(y+(1-y))^(D-j-s) retains nonnegative
coefficients. The x degree already equals D. Since sum_j B_j^D(xy)=1,
the resulting coefficients, summed over j, equal1 at every tensor
index, by uniqueness of the Bernstein basis.

On a cell[a,a+1/4], x=alpha(1-u)+beta u with
alpha=a/8,beta=(a+1/4)/8 in[0,1]. Substitution in x^s(1-x)^(D-s)
uses nonnegative coefficients for both x and1-x, and therefore
preserves these nonnegativity and sum identities. This applies to
all sixteen cells, including beta=1 in the final one.

Multiplication by z_k(y)=y^(6-k)(1-y)^k is again coefficientwise
positive, since it is B_(6-k)^6(y)/binom(6,k). Products of Bernstein
basis polynomials are positive multiples of the basis of the summed
degree, as follows directly from their binomial definitions. Thus
the final degrees are exactly(D,D+6)=(2816,2822), the required common
degrees. Linearity, |c_(k,j)|<=M_k and the preceding sum identity show
that the absolute coefficients of z_k F_k(Ey/8) are bounded by those
of M_k z_k. Finally triangle-inequality summation over k proves

    S(Q_<=J) <= T_0 sum_(k=0)^6 M_k beta_k,
    T_0=(8^18-4^18)/18,
    beta_k=B(35/2-k,k+1/2)/pi
          =O_(17-k)O_k/(2^17*17!),                            (6)

where O_h=product_(s=1)^h(2s-1),O_0=1. Both beta arguments are
positive, with sum18. Formula(6) bounds the entire prescribed
two-variable coefficient sum using seven complete one-variable
coefficient enclosures. It does not replace that sum by sampled
values or maxima of the actual polynomial on a real interval.

All row and labelled-position cancellations in each d_(k,l) were
performed before (5). Absolute values are not applied to the original
34 rows in this prefix bound. The final triangle inequality between
the seven residual-factor types is only an upper estimate for (2).

### Enclosing every prefix coefficient with exact rational arithmetic

Set G=10^120. For h=17-k+l, the identity4^h h!/(2h)!=2^h/O_h gives

    G t_(k,l)=G d_(k,l)2^(h+3l)/[2C^11(2k)!O_h].             (7)

Exact integer floor and ceiling yield integers L_(k,l),U_(k,l)
enclosing(7), with U-L<=1. No coefficient of p or d is rounded or
changed; these are enclosing arithmetic intervals for the new
contraction. All9884 scalar inclusions are checked by integer
cross multiplication.

For fixed j let q=min(j,J). Evaluate (5) backwards, starting with
the interval[L_(k,q),U_(k,q)] and for l=q-1,...,0 replacing it by

    [ L_(k,l)+floor((j-l)lo/(D-l)),
      U_(k,l)+ceil((j-l)hi/(D-l)) ].                          (8)

The multiplier is nonnegative and at most1, and D-l>0. Expanding
this nested expression gives the weights
product_(s=0)^(l-1)(j-s)/(D-s)=binom(j,l)/binom(D,l), proving
the inclusion inductively, including negative accumulators. The
endpoints divided by G enclose c_(k,j). Each rounded update increases
the integer width by at most3, so the recorded width bound3(q+1)
is valid. Interval width alone is not used as proof of inclusion;
the exact floor/ceiling operations and induction are essential.

Every0<=j<=2816 is evaluated for all seven k, giving19719 intervals.
M_k is the largest absolute endpoint in its whole row, divided by G.
The following are outward upper displays of those exact rationals:

| k | M_k upper bound | maximizing index |
|---:|---:|---:|
| 0 | 1.752235707594655e-34 | 170 |
| 1 | 4.967557202530917e-32 | 172 |
| 2 | 1.879220041416438e-30 | 173 |
| 3 | 2.184728028655592e-29 | 176 |
| 4 | 9.800351686125698e-29 | 179 |
| 5 | 1.752663643872049e-28 | 182 |
| 6 | 1.028710116498409e-28 | 187 |

The rational upper bound in(6) is less than5.665664337771549e-18.
All signed prefixes are retained in the saved input. Neither the
original 200-digit kernel arithmetic nor its grid is changed. New
divisions in(7)-(8) are exact rational enclosures; no floating-point
sign or cancellation assumption enters them.

### Paying every remaining degree

For a single monomial E^l y^(l+6-k)(1-y)^k the coefficients in the
prescribed basis are nonnegative. Its energy expansion on a positive
cell has nonnegative power coefficients, and power-to-Bernstein
conversion is positive; its y factor has nonnegative degree-elevation
coefficients. Here l<=D and l+6<=N. Equations(2)-(3), positive beta
integration and the displayed f_(k,l) therefore give

    S(Q_>J) <= sum_(k=0)^6 sum_(l=J+1)^D
      |d_(k,l)|/[2C^11 4^k k!]
                  *(8^(l+18)-4^(l+18))/(l+18)!.             (9)

For clarity, the beta factor before energy integration is

    |f_(k,l)| B(l+35/2-k,k+1/2)/pi
        =|d_(k,l)|/[2C^11 4^k k!(l+17)!].

This pays the entire omitted polynomial, not only the first omitted
coefficient. To bound its uncomputed d values use L938's exact Q_k
and all34 rows. For rho=1/32 put

    q_k^+(rho)=sum_(l=0)^256 |[z^l]Q_k| rho^l/C,
    V_k(rho)=sum_alpha |c_alpha| alpha_k
                  product_j q_j^+(rho)^(alpha_j-delta_(j,k)),

omitting rows with alpha_k=0. These are positive rationals computed
from the full unchanged p. The coefficient triangle inequality for
the derivative of the original row polynomial gives, for every l,

    |d_(k,l)|/C^11 <= V_k(rho)rho^(-l).                       (10)

This use of absolute rows only majorizes the fully paid complement
of the already combined signed polynomial; it does not undo the
prefix cancellations. It is not an extrapolation of observed decay.

Let L=J+1=1412. Successive terms of (8/rho)^l/(l+18)! for l>=L
have ratio at most q=256/1431<1. Dropping the negative4^(l+18)
in(9), applying(10) and extending a positive finite sum to infinity
gives the exact rational bound

    S(Q_>J) <= T_tail
      :=8^18 (8/rho)^L/[(L+18)!(1-q)]
                    *sum_(k=0)^6 V_k(rho)/(2*4^k k!)
       < 1.225*10^-82.                                      (11)

Its computed outward enclosure is
[1.224964179327678,1.224964179327679]*10^-82. All powers and row
majorants are included. The infinite geometric majorant only enlarges
the finite-degree error; no limiting interchange or unproved
analytic continuation is used.

### Total allowance and verification scope

Let P be the exact upper rational from(6), Tcap=1.225e-82, and use
the inherited upper rational enclosures e_+ for exp(4/5),p_+ for pi
and A_(2,+) for L948's complete second-order allowance. Define

    B=e_+ epsilon p_+^6(P+Tcap)+A_(2,+).                     (12)

All quantities are positive. Equations(2),(6),(11) and L948 prove
A_1+A_2<=B. The rational comparisons in the certificate prove(1).
They include the complete epsilon; no reduced residual bound is used.
The second-order remainder pays all terms with two or more replaced
factors and is less than1.496e-67. The new computation changes its
first-order allowance, not that remainder or the original kernel.

Producer:

    python3 scripts/heat/l938-signed-response-complete-90.py

Full report: `scripts/heat/l938-signed-response-complete-90.json`.
All new scalar and Bernstein enclosures:
`scripts/heat/l938-response-bernstein-enclosures-90.json`.
All29626 producer checks pass, with no failures. The report saves
complete rational maxima, all positive row evaluations, the exact
tail bound and the complete total. The coefficient file saves all
9884 power enclosures and all19719 Bernstein enclosures. The old
exact signed prefix artifact is unchanged and hash checked.

Additional independent normalization and contraction check:

    python3 scripts/heat/check-l938-signed-response-complete-90.py

Its full report is
`scripts/heat/l938-signed-response-complete-check-90.json`.
All21005 checks pass. It independently computes the seven maximizing
coefficients by exact factorial gamma normalization and direct
binomial contraction, rather than the producer's odd products and
rounded Horner form. Each result belongs to its recorded interval.
It checks every saved interval against its reported row maximum,
recomputes beta masses with factorials, sums all sixteen cell masses,
reconstructs q_k^+ using L938's integer Q_k normalization, and checks
the exact final budget against8.079e-50 and the required margin.

This is not an independent replay of all19719 Horner contractions,
an audit of the derivative-prefix producer or theta enclosure, or
a later conceptual review of the positive-composition argument.
Those limitations are retained explicitly. The full small result,
tail, failure and check-summary fields were inspected, while the
scripts consume all load-bearing coefficient evidence; previews of
large artifacts are not treated as verification. No result beyond
the inspected standard methods is claimed.

### Independent complete conceptual audit — 9 November 2026, step92

The unchanged SPECIALIZE assessment90 covered precisely this audit.
The result survives, conditional on the original theta inclusion,
signed derivative-prefix multiplication and arithmetic execution
contracts. All new coefficient intervals have now been independently
replayed; the seven selected contractions above are no longer the
only independent arithmetic evidence. No original artifact was altered.

The standard finite identities are imported from Javier Sanchez-Reyes,
*Algebraic manipulation in the Bernstein form made simple via
convolutions*, Computer-Aided Design35(2003),959-967,
DOI10.1016/S0010-4485(03)00021-6,
[primary paper](https://www.cise.ufl.edu/research/SurfLab/seminar/algebraicmanipulation.pdf),
Sections1.2,2.1-2.4,2.6,3.1, equations1.2,2.1-2.8,3.1-3.3,
printed pp960-963. These supply finite product, degree-elevation,
composition and tensor algebra in the correct coefficient convention.
They do not assert positivity for an arbitrary range-preserving
substitution. The explicit expansion in(4)-(6) is the necessary
specialization: each B_j^D(xy) has nonnegative tensor coefficients,
and summing over j gives coefficient1 at every index by uniqueness.
Both x=alpha(1-u)+beta u and1-x have nonnegative coefficients for
0<=alpha<=beta<=1. This proves affine restriction even when beta=1;
strict positivity is not needed. Multiplication by z_k has nonnegative
coefficients and raises only the y degree by6. Consequently
-M_k times the coefficient of z_k <= the corresponding coefficient
of z_k F_k <= M_k times that coefficient, at every index in the
prescribed basis. Positive integration and the triangle inequality
give(6), with no substitution of a pointwise supremum for S.

The audit also checks the essential L948(1)-(6) normalization. The
twelve original beta parameters sum to18. Deleting one labelled
factor of type k leaves eleven factors, total index12-k, and beta
sum35/2-k+l in degree l. Differentiating P counts its alpha_k
labelled choices exactly once. Writing h=17-k+l, the half-integer
gamma formula changes pi^(11/2)/Gamma(h+1/2) to
pi^5 4^h h!/(2h)!. The remaining factor1/[2(2k)!] gives exactly
f_(k,l), not an additional square root of pi or a permutation factor.
The substitution x=E(1-y), including dx=E dy, produces E^(17+l)
and w(y)y^(l+6-k)(1-y)^k. The beta parameters of w are23/2,1/2;
those after multiplication are l+35/2-k,k+1/2, with sum l+18.
All are positive. This verifies both the nu_j factorial formula and
the beta factor in(9); the latter cancels exactly to
|d_(k,l)|/[2C^11 4^k k!(l+17)!]. Energy integration adds the factor
1/(l+18), so the tail denominator is(l+18)!, not(l+17)!.
Explicitly, for every0<=j<=N,
integral w(y)B_j^N(y)dy=binom(N,j)B(j+23/2,N-j+1/2).
The two gamma arguments are positive even at j=0,N and sum toN+12;
their half-integer factorial expressions divide by(N+11)! and
give exactly pi nu_j as printed in L948. Each energy mass m_(a,i)
is also strictly positive because its integrand is positive inside
the cell. Thus all coefficient comparisons use positive masses.

For the full remainder, g(s) is a polynomial on[0,1] and each
interpolating factor is bounded by8. Its132 ordered second-derivative
pairs have two factors bounded by epsilon; integrating1-s gives66.
The original simplex weights, including k_i=0 faces, are integrable
and dominate all these expressions on the compact domain. Thus the
cited Taylor theorem, dominated convergence and absolute Fubini apply
without differentiating a singular weight or discarding a boundary
piece. Cancelling the original factorials gives the row sum
W=293/540 and Z=W/(2^36*17!). This pays every higher replacement
term, not merely the quadratic monomials of a truncated expansion.

For the complement, positivity of each full-degree monomial basis
representation justifies equality(3) termwise before using absolute
d coefficients. The generating polynomial with absolute Q coefficients
dominates every coefficient of each derivative row. Evaluation at
rho=1/32 therefore proves(10) for all degrees, including every
1412<=l<=2816. The first successive factorial ratio is256/1431
and later ones decrease. Extending this nonnegative finite sum to
a geometric majorant pays the complete complement; no observed
coefficient decay or residual sign is assumed. All sixteen energy
cell masses sum exactly to(8^18-4^18)/18, and the residual interval
remains the single full[0,1].

Reproduce the new, separate certificate with

    python3 scripts/heat/audit-c948a-complete-budget-92.py

Full evidence: `scripts/heat/c948a-complete-budget-audit-92.json`.
The audit does not import or execute the producer. It reconstructs
all9884 scalar intervals using the factorial gamma expression in(7),
rather than the producer's odd products. For any integer numerator n
and positive denominator d it uses divmod(n,d)=(q,r), verifies
n=qd+r and0<=r<d, and uses[q,q+1_(r>0)]. This includes negative n.
At each Horner update the multiplier lies in[0,1], so its lower
endpoint is rounded downward and its upper endpoint upward. The
induction in(8) then encloses the exact rational contraction.
All20,850,347 updates are replayed; all19719 resulting pairs match
the saved pairs, including j=0,j=J,j=J+1 and j=D in all seven rows.
The complete replay pairs and scalar endpoints are saved, not just
hashes, widths or selected values. Maxima and their first maximizing
indices are recomputed from all intervals and agree with the table.

The script checks every canonical row and its deleted multiplicities,
rebuilds all257 epsilon contributions, all seven beta masses and
sixteen cell masses, and reconstructs the full Q_k positive evaluations
by direct rational summation of integer-normalized coefficients.
It then recomputes every derivative row majorant, the complete tail,
the exponential-series enclosure, both second-order endpoints and
the total. The inherited pi endpoints are checked for identity and
positivity; their analytic inclusion remains inherited. The exact
prefix/tail upper bounds respectively lie in
[5.665664337771548,5.665664337771549]*10^-18 and
[1.224964179327678,1.224964179327679]*10^-82. The full total is
the same rational B as(12), lies in the interval in(1), and satisfies

    B/m <=9.040390703382319*10^-16 <1.

All31886 recorded checks pass, with no failures. The complete summary
and failure list were inspected; the independent program consumes and
checks every load-bearing scalar and coefficient, rather than relying
on artifact previews. Exact rational comparisons verify all displayed
outward bounds. The audit supplies local verification of an existing
specialization, not a stronger estimate or a theorem beyond the sources.

Theta-node inclusion, derivative-prefix multiplication and correctness
of the arithmetic libraries remain explicit inherited assumptions;
source hashes establish identity only. The selected-coefficient claims
later in L948 were unnecessary to this complete upper bound and were
not separately audited. Polynomial negative mass, tail beyond8,
effective global joins and actual-Xi all-degree signs remain open.
The direct mathematical inputs and main argument assembly are unchanged.

## Mathlib

Full or supporting Mathlib coverage of this specialized coefficient
certificate has not been checked. Unknown coverage is not absence.
The standard inputs are the already assessed Bernstein partition,
positive beta/gamma identities and L948's complete Taylor remainder.
The finite composition, normalization and omitted-degree estimates
are proved here for the exact unchanged polynomial and fixed cells.
