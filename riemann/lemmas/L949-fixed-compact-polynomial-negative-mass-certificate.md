# Lemma 949: the fixed compact polynomial negative-mass allowance vanishes

## Hypotheses

Use exactly L938's continuous signed density v and polynomial replacement
v_p in (18), with all34 rows, twelve labelled factors, factorials and
retained M_0^12 normalization. Keep its degree256 kernel p,257 nodes,
theta cutoff8,precision200,coefficient grid10^-120 and full epsilon.
Use tilt1/10 and precisely the sixteen quarter-cells partitioning[4,8].
The original theta inclusion, complete integer-polynomial execution,
directed arithmetic and Python integer/Fraction contracts of L938
remain explicit hypotheses for the numerical result. C948a's independently
audited bound B in (12) retains its derivative-prefix execution and
arithmetic contracts. The present new conversions are checked completely
below; prior hashes and saved flags establish input identity, not a new
audit of the original producers. No RH, density sign, residual sign,
contact, global crossing or effective tail-onset hypothesis is assumed.

Let m=8.935649629627030e-35 be the qualified L947 positive endpoint
margin. Write R_l,C as in L938(18), including every0<=l<=3072, and put
den=C^12. All bounds below use the actual density units, including pi^6.

## Conclusion

Subject to these contracts, the complete polynomial obeys

    v_p(E)>=0,                         4<=E<=8,                  (1)
    integral_4^8 exp(E/10)max(-v_p(E),0)dE = 0.                 (2)

Consequently C947b's negative-part transfer and audited C948a give

    integral_4^8 exp(E/10)max(-v(E),0)dE <= B < m,              (3)
    8.078176384036186e-50 <= B <=8.078176384036187e-50.

The complete fixed compact certificate is thus zero plus the exact
C948a B, with outward ratio and remaining margin

    9.040390703382318e-16 <= B/m <=9.040390703382319e-16,
    8.935649629627021e-35 <= m-B <=8.935649629627022e-35.       (4)

This is a local specialization of the inspected finite Bernstein/Jensen
methods, not a new general theorem beyond those sources. The actual
tail beyond8 is unpaid. In particular (3) does not establish B_4<m,
pointwise nonnegativity of v, global primitive variation, parameter
signs, contacts, other degrees, realization or RH. L939 has no effective
onset that can be inserted at8. The separate unsigned-error stop in
C947b remains valid for that stopped certificate.

## Proof

### Imported finite identities and their specialization

For n>=0 write B_j^n(x)=binom(n,j)x^j(1-x)^(n-j). We import the
normalized Bernstein partition of unity, power conversion and affine
restriction identities from Javier Sanchez-Reyes, *Algebraic
manipulation in the Bernstein form made simple via convolutions*,
Computer-Aided Design35(2003),959-967, DOI10.1016/S0010-4485(03)00021-6,
[primary paper](https://www.cise.ufl.edu/research/SurfLab/seminar/algebraicmanipulation.pdf),
Sections1.2,2.1-2.4,2.6, formulas1.2,2.1-2.8, printed pp960-962.
Its scaled coefficients must be converted to the normalized convention
above. The de Casteljau restriction recurrence is also in Farouki,
*The Bernstein polynomial basis: a centennial retrospective*,
[author slides](https://faculty.engineering.ucdavis.edu/farouki/wp-content/uploads/sites/51/2021/07/Bernstein-polynomial-basis.pdf),
PDF pp12,16-19,24-25. These are exact finite identities allowing signed
coefficients and closed interval endpoints; the sources certify no
floating implementation or numerical sign in this problem.

Finite Jensen and convexity of phi(t)=max(-t,0) are imported from
Boyd and Vandenberghe, *Convex Optimization*, Cambridge2004, corrected
seventh printing2009, [Sections3.1.8,p77 and3.2.3,p80](https://www.stanford.edu/~boyd/cvxbook/bv_cvxbook.pdf).
Here the finitely many weights B_j^n(x) are nonnegative and sum1 on
the whole[0,1]; phi is convex on all real numbers including0.
No signed-measure Jensen or infinite interchange is used.
Euler's beta integral [DLMF5.12.1](https://dlmf.nist.gov/5.12#E1)
applies with positive parameters j+1,n-j+1, including endpoint indices,
and gives integral_0^1 B_j^n=1/(n+1). These standard identities are
imported, not reproved; the formulas and exact arithmetic below justify
their application to the present factorial normalization and cells.

### Entire density, global conversion and complete independent check

Set n=3089=17+3072 and G=10^120. The power coefficients of
F(x)=v_p(8x)/pi^6 are exactly

    t_s=0 (s<17),
    t_s=R_(s-17)8^s/[den s!] (17<=s<=n).                    (5)

The full input has3073 entries, including its zero coefficients, and
R_3072!=0. Thus the E^17 factor has not been lost, and the degree is
3089, independently of L948's different response degrees or prefix.
The normalization den=C^12 is checked against L938's original C,
not against a reduced determinant or a density with fewer factors.

The normalized degree-n Bernstein coefficients of F are

    b_j=sum_(s=0)^j t_s binom(j,s)/binom(n,s),  0<=j<=n.     (6)

For each s, exact integer floor and ceiling enclose Gt_s by
[L_s,U_s], with U_s-L_s<=1. To evaluate(6), start [L_j,U_j] and
for s=j-1,...,0 replace [lo,hi] by

    [L_s+floor((j-s)lo/(n-s)),
     U_s+ceil ((j-s)hi/(n-s))].                             (7)

The denominators are positive and the multipliers belong to[0,1].
The nested weight through index s is binom(j,s)/binom(n,s), so
induction gives an enclosing integer interval for Gb_j, including
negative accumulators. There is no discarded high-degree remainder.
The numerical width check is a diagnostic, not the inclusion proof.

Every one of these3090 global intervals is also checked independently
by an exact integer transform, without the producer's rounded Horner
contraction. Let

    H=den n!,
    z_s=0 (s<17), z_s=R_(s-17)8^s(n-s)! (s>=17).

Substitution into(6) gives exactly

    H b_j=sum_(s=0)^j binom(j,s)z_s=:T_j.                    (8)

The verifier initializes an integer array with z and, for r=0,...,n-1,
updates T_j<-T_j+T_(j-1) in descending j=n,...,r+1. Before pass r,
at indices j>=r the running value is
sum_(q=0)^r binom(r,q)z_(j-q). Descending order preserves the old
T_(j-1), and Pascal's identity gives the invariant for the next pass
at j>=r+1. Index j is frozen after pass j-1 with exactly the right
side of(8); index0 is initially correct. Hence this computes every
exact T_j using integers alone. This is an independent implementation
of the imported finite conversion, not a new conversion theorem.

For every j, the verifier checks the exact cross-multiplied inequality

    H lower_j <= G T_j <= H upper_j.                         (9)

All3090 inequalities pass. Full T_j and H are saved in
`scripts/heat/l938-compact-global-exact-94.json`. An evaluation at
selected points, selected coefficients, interval overlap or a hash is
not substituted for this complete check.

### Restriction to precisely the prescribed cells

The first midpoint restriction retains the right half[4,8] of[0,8].
Four further uniform binary restriction levels yield precisely
[j/4,(j+1)/4], j=16,...,31. These are computational restrictions to
the fixed cells, with no adaptive mesh change or extra tested cells.
Every cell retains the common degree n, including zero coefficients.

At each de Casteljau step, interval lower endpoints are replaced by
floor((lo_i+lo_(i+1))/2), and upper endpoints by
ceil((hi_i+hi_(i+1))/2). Division by G encloses the exact midpoint
coefficient because this averaging map is positive. The left edge of
the triangle, and reversed right edge, enclose the two restricted
coefficient vectors by the cited de Casteljau identity. Endpoints
are included. Induction through the sixteen triangles therefore
encloses every coefficient of every final cell.

The separate verifier replays all76360080 midpoint updates with exact
Euclidean quotients and remainders, checking both endpoint divisions
and their outward inequalities, including negative intermediate values.
It checks all left/right arrays of every split and all49440 final
coefficient intervals against the saved artifact. This is a complete
independent enclosing replay, while(8)-(9) independently check the
global conversion by different arithmetic. Library execution remains
an explicit contract. The certificate does not claim a formally
verified Python interpreter or a later independent conceptual audit.

### Positive integration, zero allowance and actual-density transfer

On a final cell [a,a+1/4], write

    v_p(a+u/4)/pi^6=sum_(j=0)^n b_(a,j) B_j^n(u), 0<=u<=1.

Let ell_(a,j)/G be the saved enclosing lower endpoint for b_(a,j).
Finite Jensen, monotonicity of phi and the positive beta integrals give

    integral_a^(a+1/4) exp(E/10)max(-v_p(E),0)dE
       <= e_+ p_+^6/[4(n+1)G] sum_j max(-ell_(a,j),0),       (10)

where e_+ and p_+ are the unchanged rational upper enclosures for
exp(4/5) and pi. Both are positive, and exp(E/10)<=exp(4/5) on all
sixteen cells. The Jacobian is1/4. All rounding is paid by taking the
lower coefficient endpoint before applying the negative part.

Every one of the49440 final lower endpoints is nonnegative. Thus
the sum in(10) is zero on every cell. Positivity and the partition
of unity prove(1) pointwise, including the cell boundaries, and(2).
In particular there is no finite exponential Taylor error to pay
for this zero allowance. The saved positive exponential enclosure
is nevertheless checked against its unchanged positive degree32
series and geometric remainder, as in C947b.

For any real a,b, max(-a,0)<=max(-b,0)+|a-b|, the transfer already
used in C947b. Apply it to v(E),v_p(E), multiply by the positive
exponential and integrate. C948a(12) supplies the separately audited
integrated absolute error on the identical shell in identical units.
Together with(2) it proves(3), without paying the replacement error
twice or inferring a residual sign. The exact rational B is read from
`scripts/heat/c948a-complete-budget-audit-92.json`, field
`/exact/total_upper`, and checked against its producer's complete
total. Comparisons with exact decimal rational m give(4). The full
selected rational B, complete cell results and summaries were inspected;
bounded previews are not evidence for these assertions.

### Reproduction and verification scope

Run

    python3 scripts/heat/l938-compact-negative-mass-94.py
    python3 scripts/heat/check-l938-compact-negative-mass-94.py

The full producer report is `scripts/heat/l938-compact-negative-mass-94.json`;
all power, global, subdivision and final coefficient enclosures are
`scripts/heat/l938-compact-bernstein-enclosures-94.json`.
The full independent report is
`scripts/heat/l938-compact-negative-mass-check-94.json`.
All6228 producer checks and55706 independent checks pass, with no
failures. Both preserve exact totals. The independent check
reconstructs every new global coefficient and restriction inclusion,
all sixteen cell masses, exact B, combined total and strict threshold
comparison. It inherits the already audited input polynomial and
replacement bound, rather than rerunning theta-node production,
34-row polynomial multiplication or signed derivative-prefix production.
No mathematical estimate for the actual tail beyond8 was computed.

## Mathlib

Full or supporting Mathlib coverage of this exact degree3089 polynomial
and compact negative-mass certificate is not checked. Unknown coverage
is not evidence of absence. The source inputs are the precisely cited
finite Bernstein conversion/restriction, finite Jensen/maximum convexity
and positive beta integral, specialized with all original arithmetic
qualifications above.
