# Corollary C028t: fixed two-site theta quartic Jacobian has rank two

## Hypotheses

Let K be the full positive kernel of L019 and write, in L021's
half-line convention,

    I_(2j)=integral_0^infinity u^(2j)*K(u)du,
    dmu_0(u)=K(|u|)du/(2*I_0).

Thus mu_0 is exactly C028q's even theta probability, not a finite
kernel truncation or a quadrature law. For real a<b put

    nu_(a,b)=(mu_0+delta_a+delta_b)/3.

Let p(x;a,b)=x^4+c_3*x^3+c_2*x^2+c_1*x+c_0 be its degree-four
monic orthogonal polynomial. Its four simple real zeros are r_i.
Use equally weighted empirical moments, as in C028q:

    m=(sum_i r_i)/4,
    V=(sum_i (r_i-m)^2)/4,
    T=(sum_i (r_i-m)^3)/4,
    Q=(sum_i (r_i-m)^4)/4,
    g=T/V^(3/2), k=Q/V^2.

Assume the saved moment containment of L917, accepted in its
audit197, under exactly L037's Decimal-library contracts. Only the
complete panel0 boxes for I_0,I_2,I_4,I_6 are used; the actual
lambda=0 lies in that closed panel [0,1/5120]. All source and accepted
audit input hashes were checked unchanged. Decimal correctness remains
assumed; the new finite propagation uses exact integer/rational
arithmetic and rational outward rounding. No actual-Xi root reality,
RH, determinacy, general-degree rank or zero-motion monotonicity is
assumed.

## Conclusion

At exactly (a,b)=(0,1), with Jacobian rows (g,k) and columns (a,b),

    -603/1000 < det D_(a,b)(g,k) < -349/1000 < 0.       (1)

In particular this reference invariant map has rank two there,
conditional on the stated input containment/arithmetic assumptions.
This is a finite specialization and calculation from known moment
formulas, not a claimed mathematical discovery beyond the sources
checked. It supplies a local reference feasibility input. It certifies
no quantitative image neighborhood, actual-target inclusion, actual
coefficient matching, higher-degree conclusion, full residual cost,
H_d=o(d), actual-Xi positivity or RH conclusion. The separate proof,
code and evidence audit1923 below accepts this conditional finite result.

## Proof

### Imported construction and its applicability

Use Walter Gautschi, *Orthogonal Polynomials: Computation and
Approximation*, OUP, 2004, Section2.1.1, Theorem2.1,
(2.1.1)-(2.1.3), printed pp52-54,
[primary book scan, PDF pp63-65](https://csclub.uwaterloo.ca/~pbarfuss/Walter_Gautschi_-_Orthogonal_Polynomials_-_Computation_and_Approximation_%282004%29.pdf).
Its moment-determinant formula is imported, not reproved. Known
multi-site modification coverage is also available in Delgado,
Fernandez, Perez and Pinar, *Multivariate Orthogonal Polynomials and
Modified Moment Functionals*, SIGMA12(2016),090,
DOI10.3842/SIGMA.2016.090,
[arXiv:1601.07194v2, Theorem3.1, Section3 pp8-10](https://arxiv.org/pdf/1601.07194v2).
The calculation uses Gautschi's coefficient form directly; no new
Uvarov theorem is needed. The primary statements/proofs were already
assessed in source reviews1908/1920; assessment1920 covers this exact
fixed test.

L019's positive density and rapid decay give all absolute moments
and positive squared integral for every nonzero polynomial. Adding
two positive atoms preserves this property. Thus the finite Gram
matrices are positive definite. Division by3 changes no monic
orthogonal polynomial; use the unnormalized mixed functional below.
The mixed-measure orthogonality definition and simple-real-zero
theorem apply by
[DLMF18.2(i), (18.2.4_5)](https://dlmf.nist.gov/18.2#i)
and the opening zero statement of
[DLMF18.2(vi)](https://dlmf.nist.gov/18.2#vi).
These facts concern reference zeros only. All coefficients are smooth
in the sites: their moment entries are polynomials in a,b and their
Gram determinant is nonzero. Newton sums therefore differentiate
smoothly without differentiating labeled individual zeros. V>0
also follows from four distinct real reference zeros; numerical
division by V is separately certified below.

Put u=I_2/I_0, v=I_4/I_0, w=I_6/I_0. These are probability moments,
with no factorial conversion. Write beta_0=1, beta_2=u, beta_4=v,
beta_6=w and beta_j=0 for odd j through7. Define

    s_j=beta_j+a^j+b^j, 0<=j<=7, including s_0=3,
    H_ij=s_(i+j), t_i=s_(i+4), 0<=i,j<=3.

Gautschi's formula in coefficient form is H*c=-t, with c in ascending
order(c_0,c_1,c_2,c_3). If D=det H and N_j is the determinant obtained
by replacing column j of H by -t, then

    c_j=N_j/D,
    partial_x c_j=(partial_x N_j-c_j*partial_x D)/D,
    partial_a s_j=j*a^(j-1), partial_b s_j=j*b^(j-1)  (j>=1),
    partial_a s_0=partial_b s_0=0.                  (2)

At the fixed sites, s=(3,1,1+u,1,1+v,1,1+w,1).
The a-derivative is1 only at index1 and is0 at every other index;
the b-derivative at index j is j. Thus no odd atom moment is dropped.
The required base orders are0,2,4,6; the coefficient system uses
mixed orders through7, not order8. Its existence and positive norm
nevertheless have all higher integrability available from L019.

### Entire centering and normalization calculation

Let P_j=sum_i r_i^j. Newton's identities give

    P_1=-c_3,
    P_2=-c_3*P_1-2*c_2,
    P_3=-c_3*P_2-c_2*P_1-3*c_1,
    P_4=-c_3*P_3-c_2*P_2-c_1*P_1-4*c_0.

Set R_j=P_j/4. The empirical centering formulas are

    m=R_1,
    V=R_2-m^2,
    T=R_3-3*m*R_2+2*m^3,
    Q=R_4-4*m*R_3+6*m^2*R_2-3*m^4.              (3)

All values and both derivatives in (2)-(3) are propagated, including
the derivative of D and every term involving m. For x=a,b define

    A_x=V*partial_x T-(3/2)*T*partial_x V,
    B_x=V*partial_x Q-2*Q*partial_x V.

Then direct quotient differentiation gives

    partial_x g=A_x/V^(5/2),
    partial_x k=B_x/V^3,
    det D(g,k)=(A_a*B_b-A_b*B_a)/V^(11/2).       (4)

Thus the sign calculation retains all normalization derivatives;
it is not a determinant of uncentered or quadrature moments.

### Complete rational certificate

The producer is `scripts/heat/two-site-theta-jacobian-1921.py`;
its full output is `scripts/heat/two-site-theta-jacobian-1921.json`.
The saved `selected_inputs` contains all decimal endpoints copied
verbatim from panel0 of `scripts/heat/low-time-h2-uniform-195.json`.
It checks their equality to audit197's accepted records and all hashes
in that audit's input register. I_0 has positive lower endpoint;
normalizing the three even moments uses interval division. Odd base
moments remain exactly0 and beta_0 exactly1.

Before enclosing, each of D,N_0,...,N_3 and its two partial derivatives
is collected exactly as a polynomial in u,v,w. This removes algebraic
cancellation between identical monomials without restricting the input
boxes. The producer uses all24 terms of each 4-by-4 permutation
determinant and the product rule on triples (value,da,db). The
complete fifteen polynomials, all coefficients and exponent triples
are retained in `polynomials`. Formula(2) then divides by the enclosed
D; no denominator derivative is suppressed.

The arithmetic uses Python Fraction endpoints. After each arithmetic
operation, its exact lower endpoint is floored and upper endpoint
ceiled to the rational grid10^(-50). Products enclose all four endpoint
products; reciprocal intervals are [1/upper,1/lower] and reject zero.
For sqrt(V), integer square roots of floor(endpoint*10^100) provide
the enclosing grid endpoints, with the upper endpoint incremented
when needed. Exact squared inequalities are checked. Induction over
the recorded expression graph proves inclusion. These operations use
no floating point or transcendental evaluations; abbreviated display
strings in the summary do not supply proof bounds.

The complete primary intervals imply the following strictly weaker
rational bounds (all are for the fixed sites):

    386/10^6 < D < 387/10^6,
    2688/10^4 < V < 2692/10^4,
    -439/10^6 < A_a*B_b-A_b*B_a < -255/10^6,
    -603/1000 < det D(g,k) < -349/1000.

The full determinant enclosure is

    [-60260542634616891377496411143313853498905414870639/10^50,
     -6989618220286959911416477650126957777667399682899/(2*10^49)].

All twelve recorded divisions exclude zero: three by I_0, four by D,
and the five positive variance-based divisors in(4). The required
threshold is exclusion of0, not a small numerical determinant at a
midpoint. It is met with negative upper endpoint. The direct
determinant of the four enclosed Jacobian entries is also retained
as a consistency check, without intersecting/narrowing either bound.

### Verification and limitations

Run from this notebook:

```text
python3 scripts/heat/two-site-theta-jacobian-1921.py
python3 scripts/heat/two-site-theta-jacobian-check-1921.py
```

The independent checker imports no producer code and saves its full
output in `scripts/heat/two-site-theta-jacobian-check-1921.json`.
It checks all1633 trace records and endpoints, all12 divisors, all
result copies, input copies and producer input hashes. It constructs
the general moments as five-variable polynomials in u,v,w,a,b,
expands determinants recursively by Laplace expansion, differentiates
those exact polynomials and then substitutes(a,b)=(0,1). All15
coefficient dictionaries equal the producer's independently organized
dual/permutation expansion, including both derivatives of D.

As an additional centering check, translating the quartic gives

    q_2=c_2-3*c_3^2/8,
    q_1=c_1-c_2*c_3/2+c_3^3/8,
    q_0=c_0-c_1*c_3/4+c_2*c_3^2/16-3*c_3^4/256,
    V=-q_2/2, T=-3*q_1/4, Q=q_2^2/2-q_0.

The checker differentiates these alternative coefficient formulas,
independently encloses the numerator in(4), and again obtains a
strictly negative upper endpoint. It checks overlap of each centered
value/derivative as a consistency test; no intersections are used.
The complete independent numerator lies between -378/10^6 and
-317/10^6. Both certificates have empty failure lists. These are
finite arithmetic/algebra checks, not independent verification of
Decimal.exp or a second proof of L917's analytic quadrature inclusion.

Equation(4), V>0 and the certified negative numerator prove(1).
The test uses one fixed point, with no site sweep, new moment
integration or automatic moment refinement. It gives no bound on how
large a neighborhood is attainable and no inclusion of the actual
cubic/quartic pair. Reflection changes g's sign and preserves k;
it is not an extra independent quartic parameter. Even successful
actual degree-four matching would leave the all-degree and cost gaps
in the main argument. The stopped scalar/width/H2 mechanisms retain
their original scopes.

### Separate proof/code/evidence audit1923

20 November 2026. The fixed conditional statement passes its separately
approved audit under assessment1921. This is reproduction and acceptance
of the finite specialization, not a new rank theorem beyond the sources
checked. No hypotheses or source moment boxes are changed.

**Construction and conventions.** L019's positive density and decay
give positive squared norm for every nonzero polynomial and all absolute
moments of the even probability. Two unit atoms preserve positivity.
These verify the hypotheses of the cited Gautschi construction and
mixed-measure simple-real-zero theorem, whose primary coverage is reused
from source-notes1908/1920. The factor3 is immaterial to orthogonality;
the factor2 in the even measure cancels between numerator and mass.
Hence its base even moments are exactly I_(2j)/I_0, without factorials.
The system H*c=-t uses orders through7 and no numerical order8 input.
All higher moments needed for the existence/zero theorem are available
analytically. Its determinant is nonzero for nearby real sites, so
coefficients and their Newton sums are smooth there.

**Derivative and observable semantics.** The complete producer was
inspected. Its fixed-site dual entries give s_0=3 and the displayed
seven remaining mixed moments. The first-site derivative is1 at index1
only; the second-site derivative is j at index j, including zero at0.
Both the Gram and replaced-column determinants retain these entries.
Permutation parity, product rules and the quotient derivative in(2)
are correct. The checker instead differentiates the unspecialized
five-variable Laplace determinants before substituting the sites; all
15 complete polynomial dictionaries agree. Reproduction of the full
producer evidence connects those dictionaries to the evaluated trace;
checking abstract dictionaries alone would not establish that connection.

Newton sums, their empirical division by4 and all centering terms in(3)
are implemented with both derivatives. Translation by the mean removes
the cubic coefficient; applying Newton sums to that depressed quartic
gives the checker's alternative V,T,Q formulas. Differentiating them
gives exactly its separately enclosed derivatives. In(4), differentiating
V^(-3/2) and V^(-2) yields respectively the coefficients3/2 and2,
and the denominator exponents add to11/2. The producer uses V^5*sqrt(V)
for that denominator. No labeled-root differentiation, Gauss weights,
uncentered replacement or dropped normalization term is used.

**Inclusion, provenance and complete replay.** The four complete raw
panel0 moment records and all twelve full divisor intervals were
inspected. L917/audit197 covers the closed parameter panel containing0;
its unchanged source hashes and accepted input copies are checked, as
are the original checker hashes. The audit reuses L917's accepted
analytic containment; it does not reintegrate moments or verify Decimal.
The inspected Fraction operations enclose exact endpoint operations:
floor/ceiling enlarge the bounds, four-corner products handle signs,
and the integer-square-root inequalities enclose sqrt(V). All twelve
divisors are in fact strictly positive: I_0 three times, D four times,
V^(5/2) twice, V^3 twice and V^(11/2) once. Repeated interval factors
may widen bounds but cannot invalidate inclusion.

Run `python3 scripts/heat/two-site-theta-jacobian-audit-1923.py`.
It preserves both original1921 certificates and writes complete
reproductions to `scripts/heat/two-site-theta-jacobian-replay-1923.json`
and `scripts/heat/two-site-theta-jacobian-check-replay-1923.json`.
All mathematical producer fields, all1633 trace records and all
checker conclusion/evidence fields reproduce exactly; only output-path
provenance and any runtime-version metadata are exempted from comparison.
The replay checks every trace endpoint, all12 divisors, both full site
derivatives of all five determinants and all independent centered
formulas. Its finite algebra and arithmetic failures are empty.
The alternative formula overlaps are consistency checks only: neither
they nor the direct determinant are intersected with primary intervals.

The wrapper's full certificate
`scripts/heat/two-site-theta-jacobian-audit-1923.json` records56 passing
checks, full actual/required rational bounds and source/output hashes.
Exact comparisons verify every bound quoted in this proof, including
the printed complete determinant endpoints and the independent numerator
bound. In particular the primary numerator has negative upper endpoint,
the variance lower endpoint is positive, and (1) excludes0 with the
claimed strict margins. The independent numerator also has negative
upper endpoint. This accepts the conditional rank-two input at the one
stated reference point. It verifies neither Decimal-library correctness
nor actual-target membership, a quantitative image radius, full residual
payment or degree-uniform control. The existing DAG inputs are sufficient
and unchanged; no actual-Xi positivity enters the rank argument.

## Mathlib

Not checked for the full two-observable fixed Jacobian theorem.
No matching Mathlib result or verified implementation is claimed.
The imported moment and mixed-measure zero results are precisely
cited above; the finite specialization and conditional computer
certificate are supplied here. Supporting polynomial/linear-algebra
results alone would not certify this numerical rank statement.
