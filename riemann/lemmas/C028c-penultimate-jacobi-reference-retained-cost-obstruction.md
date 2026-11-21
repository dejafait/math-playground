# Corollary C028c: penultimate Jacobi reference retained-cost obstruction

## Hypotheses

Use precisely the actual polynomial P_d=R_d/gamma_0 and b_j of C028a,
with integer d>=5. Use L025's absolutely convergent real S_k and L027's
unconditional S_2,S_3>0. Write

    v=S_2, tau=S_3, kappa=S_4, lambda=S_5,
    F(z)=sum_(j>=0) b_j z^j/j!,
    P_d(x)=sum_(j=0)^d binom(d,j)b_j x^(d-j).

The finite actual-coefficient enclosure below imports only L778's
audited entire evaluator and its complete analytic remainder, under
its stated directed-arithmetic and correctly rounded exp/sqrt contracts.
In particular it retains the Python3.15.2/Decimal1.70/libmpdec4.0.1
contracts, including allcr=1, and does not independently attest that
backend. No fitted model, L827 representing measure, RH or root-reality
assumption is used. The finite arithmetic and analytic argument passed
the separate conceptual audit1506 below, under those same contracts.

For each d let m,u,w be real and s,r>0, all allowed to depend on d.
Define q_(-1)=0, q_0=1 and

    q_n(x)=(x-alpha_n)q_(n-1)(x)-beta_(n-1)q_(n-2)(x),
    alpha_n=m (1<=n<=d-2), alpha_(d-1)=m+u, alpha_d=m+w,
    beta_j=s*j (1<=j<=d-2), beta_(d-1)=r*s*(d-1).

Set alpha_n=0 for n>d and beta_j=1 for j>=d; beta_0 is immaterial.
Let mu_d be the positive reference probability measure justified below,
h_n=integral q_n^2 dmu_d, and expand uniquely

    P_d=sum_(nu=0)^d a_nu q_nu,    a_d=1.

Call a parameter choice feasible when a_(d-1)=a_(d-2)=a_(d-3)=0.
For feasible choices set

    B_d=(h_(d-4)*a_(d-4)^2+h_(d-5)*a_(d-5)^2)/h_(d-1).

All coefficients are real. At d=5 the second residual is a_0.

## Conclusion

Subject to the inherited evaluator contracts, feasible positive choices
exist for every d>=5. Nevertheless there are constants c>0 and D>=8,
depending only on the actual coefficients, such that every feasible
choice in every integer degree d>=D satisfies

    B_d >= c*d^4.

Thus no feasible degree-dependent choice in this family has B_d=o(d^2).
The full Schmeisser statistic satisfies I(P_d)^2>=B_d, so it cannot
satisfy I(P_d)=o(d). This is a failure of the stipulated reference-family
upper bound, not a lower bound on actual root heights, a nonreal zero,
or a resolution of RH. No effective c or D is claimed. Other recurrence
families are outside the conclusion; no lower bound on s or r, or
upper bound on m,u,w independent of d, is assumed.

## Proof

### Imported positive-measure and height interfaces

Barry Simon, *Szego's Theorem and Its Descendants: Spectral Theory for
L^2 Perturbations of Orthogonal Polynomials*, Princeton UP,2011,
[Proposition1.3.6 and Theorem1.3.7, pp16-17](https://assets.press.princeton.edu/chapters/s9377.pdf),
provides the bounded Favard theorem. For each fixed d our real diagonal
sequence is bounded, and a_j=sqrt(beta_j)>0 is bounded with a positive
constant tail. With b_j=alpha_j in Simon's notation, the theorem supplies
a compactly supported probability measure with infinite support and
this recurrence. All moments and all h_n are finite, and h_n>0.
The support bound may depend on d; no uniform bound is imported.

Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
a Polynomial*, Mathematica Balkanica16(2002),203-217,
[(1.1)/(1.5), pp203-204, Theorem1 and Corollary1, pp205-207](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
supplies h_n/h_(n-1)=beta_n and the coefficient-height statistic used
in C028a. The positive infinite-support measure just constructed meets
its hypotheses. Here h_0=1 and the expansion is real and monic, so
its imaginary penultimate coefficient is zero. Hence

    I(P_d)^2=sum_(nu=0)^(d-2) (h_nu/h_(d-1))*a_nu^2,
    sum_(P_d(z)=0) |Im z| <= I(P_d).

Roots count multiplicities. Both retained terms are nonnegative members
of this sum. These source theorems and their relevant proofs were
covered in source-notes1503 and C028a's existing assessment. They are
imported, not reproved. The following calculation addresses only this
family's cancellation and cost, which those sources do not supply.

### Exact finite equations and retained costs

Put delta=m+b_1 and A=s-v. Let H_n denote the monic Hermite polynomial
in x-m with variance s, normalized by

    exp((x-m)z-s*z^2/2)=sum_(n>=0) H_n(x)z^n/n!.

The stipulated recurrence gives q_n=H_n for 0<=n<=d-2. At its last
two steps, using (x-m)H_j=H_(j+1)+s*j*H_(j-1), it gives exactly

    q_(d-1)=H_(d-1)-u H_(d-2),
    q_d=H_d-(u+w)H_(d-1)
        +[uw+(1-r)s(d-1)]H_(d-2)-u*s(d-2)H_(d-3).          (1)

Define g_k by

    F(z) exp(mz+s*z^2/2)=sum_(k>=0) g_k z^k/k!.

Multiplication by the displayed Hermite generating function, followed
by extraction of a single finite coefficient, yields

    P_d=sum_(k=0)^d binom(d,k)g_k H_(d-k).                 (2)

L025's locally convergent normalized logarithm, with the same even
substitution as C028a, gives

    log F(z)=b_1*z-v*z^2/2+tau*z^3/3-kappa*z^4/4
             +lambda*z^5/5+O(z^6).

This uses no global logarithm or positivity of formal zero moments.
Exponentiation through degree five gives

    g_1=delta,
    g_2=delta^2+A,
    g_3=delta^3+3delta*A+2tau,
    g_4=delta^4+6delta^2*A+8delta*tau+3A^2-6kappa,
    g_5=delta^5+10delta^3*A+20delta^2*tau+15delta*A^2
        -30delta*kappa+20A*tau+24lambda.                  (3)

By monicity, the three cancellations are equivalent to P_d-q_d having
degree at most d-4. Comparing (1) and (2) proves their exact equations:

    u+w=-d*delta,
    uw+(1-r)s(d-1)=binom(d,2)g_2,
    -u*s(d-2)=binom(d,3)g_3.                             (4)

There is no lost positive branch: given real delta and s>0 these force

    m=delta-b_1, u=-d(d-1)g_3/(6s), w=-d*delta-u,
    r=1+[uw-binom(d,2)g_2]/[s(d-1)],

and conversely they satisfy (4) whenever the resulting r is positive.
Under (4), all remaining q_(d-k)=H_(d-k), k>=4. Therefore
a_(d-4)=binom(d,4)g_4 and a_(d-5)=binom(d,5)g_5, without lower-term
contamination. The norm recurrence gives

    h_(d-1)=r*s^(d-1)*(d-1)!,
    h_j=s^j*j! (0<=j<=d-2).

In particular the factor r belongs in the denominator. Thus

    B_d = d^2(d-1)(d-2)(d-3) g_4^2/(576*r*s^3)
        + d^2(d-1)(d-2)(d-3)(d-4) g_5^2/(14400*r*s^4).   (5)

All factorials and indices in this identity are valid at d=5.

### Finite actual-coefficient certificate

L778's evaluator is G(w)=xi(1/2+sqrt(w)/2)/8, understood by its entire
even series, with an exact finite-integral polynomial P_0. It encloses
every coefficient of P_0 and proves

    |G-P_0|<=E_G<3.141e-48 on |w|<=1600.

These coefficient widths already include quadrature errors; the complex
remainder additionally includes all theta, integration and cosh tails.
Cauchy's coefficient estimate therefore encloses A_j=[w^j]G by adding
[-E_G/1600^j,E_G/1600^j] to the saved jth coefficient interval.
This is done for j=0,...,5 before normalization or division.

C028a's actual F convention gives G(w)=gamma_0*F(w/4)/8. Consequently

    f_0=1, f_j=[z^j]F(z)=4^j*A_j/A_0 (1<=j<=5),
    b_j=j!*f_j.

All A_j lower endpoints are positive. If ell_n=[z^n]log F(z), finite
coefficient comparison in F'=F*(log F)' gives

    ell_n=f_n-(1/n)sum_(k=1)^(n-1) k*ell_k*f_(n-k),
    S_n=(-1)^(n+1)*n*ell_n.                              (6)

This recovers the same L025 constants, not moments of an assumed
positive zero law. For later use set sigma=1/200 and

    T=tau/sigma^3, Q=kappa/sigma^4, H=lambda/sigma^5,
    E(X)=X^6-8T*X^3+9Q*X^2-2T^2,
    J(X)=T*X^3-3Q*X^2+3H*X-T^2.                         (7)

Let M be the 9 by 9 matrix whose rows are coefficients in descending
powers X^8,...,1 of X^2 E, X E, E, X^5 J, X^4 J, ..., J. The complete
interval calculation proves the following deliberately coarse strict
enclosures (the certificate retains 100-place outward endpoints):

    3.7172599285269686e-5 < v < 3.7172599285269687e-5,
    1.4417393140097327e-7 < tau < 1.4417393140097329e-7,
    6.6303168025299086e-10 < kappa < 6.6303168025299088e-10,
    3.2136641506166011e-12 < lambda < 3.2136641506166013e-12,
    1.6659e-14 < (9v/10)^3-tau^2 < 1.6660e-14,
    -21.518952570 < det M < -21.518952569.                (8)

Implementation: `scripts/jacobi-reference/penultimate_cost_1504.py`.
Full certificate: `scripts/jacobi-reference/penultimate-cost-1504.json`.
Reproduce with `python3 scripts/jacobi-reference/penultimate_cost_1504.py`.
There is no degree or parameter sweep. The program consumes only the
first six audited P_0 coefficients and the full uniform remainder;
source hash and equality with L778's audited evaluator replay are checked.

New arithmetic uses exact Python integers and Fraction, rounding every
interval endpoint outwards to a multiple of 10^-100. Addition uses
endpoint sums, multiplication the extrema of the four endpoint products,
and division the reversed reciprocal endpoints only when zero is excluded.
These operations retain enclosure by induction, including correlated
true coefficients: independent interval ranges only enlarge the set.
The determinant is the full signed Leibniz sum, evaluated by subset
dynamic programming with no pivots. A state for selected columns sums
all assignments to the first number-of-selected-columns rows. Appending
column j adds one inversion for each previously selected column greater
than j, giving its exact sign. Thus induction over the rows equals the
complete determinant. All 512 state enclosures and all matrix entries
are saved, along with input coefficients, Cauchy errors, (6), (7),
provenance, all 21 checks and an empty failure list. Input files remain
unchanged. No transcendental numerical operation occurs in this program.

The complete load-bearing coefficient, sum, polynomial and determinant
enclosures were inspected. L778's evaluator and analytic audit are reused,
not replayed as a new transcendental verification. Its trusted arithmetic
contracts and the lack of formal verification remain qualifications.

### Feasibility really holds

Put c_*=9v/10 and s=v/10. By (8), 0<tau<c_*^(3/2). The polynomial
f(delta)=delta^3-3c_*delta+2tau is positive at zero and negative at
sqrt(c_*). The intermediate value theorem gives a root
0<delta<sqrt(c_*). For every d>=5 choose

    m=delta-b_1, u=0, w=-d*delta,
    r=1+d*(c_*-delta^2)/(2s)>1.

Here A=-c_* and g_3=0. Substitution into (4) proves all three
cancellations, with s,r strictly positive. No omitted coefficient or
residual estimate is asserted for this explicit feasible family.

### Positivity controls every scaling

For an arbitrary feasible choice, let J_d be its real symmetric d by d
Jacobi matrix. Its characteristic polynomial is q_d by determinant
expansion of the tridiagonal matrix. The first two matched coefficients
of P_d(y-b_1) are zero and -binom(d,2)v. The trace and second coefficient
identity, equivalently Newton's second identity, therefore give

    tr(J_d+b_1 I)=0,
    tr((J_d+b_1 I)^2)=d(d-1)v.

Directly from the diagonal and off-diagonal entries and u+w=-d*delta,
the second identity is

    u^2+w^2-d*delta^2+s(d-1)(d-2+2r)=d(d-1)v.            (9)

The elementary inequality u^2+w^2>=(u+w)^2/2 gives

    d(d-2)delta^2/2+s(d-1)(d-2+2r)<=d(d-1)v.

All terms on the left are nonnegative. For d>=5 this proves

    delta^2<=8v/3,    0<s<=5v/3,    rs<=dv/2.             (10)

Equation (9) also gives u^2+w^2<=d(d-1)v+d*delta^2<=4d^2 v,
so |u|<=2d*sqrt(v). The last equation in (4) then implies uniformly

    |g_3|=6s|u|/[d(d-1)]<=20v^(3/2)/(d-1).              (11)

No lower bound on s or r has been used. In particular (10)-(11) cover
unbounded u,w,r and feasible choices with s or r tending to zero.

### The limiting cancellations are impossible

Suppose real delta,s, even allowing s=0, satisfied g_3=g_4=g_5=0.
Since tau>0, g_3=0 forces delta!=0. Put x=delta. Equation (3) gives

    A=-(x^3+2tau)/(3x).

On g_3=0, substitution in g_4 gives

    x^6-8tau*x^3+9kappa*x^2-2tau^2=-(3x^2/2)g_4=0.      (12)

On g_3=g_4=0, (3) first simplifies to
g_5=6(x^5-5x*A^2+4lambda). Substituting A again gives

    x^6-5tau*x^3-5tau^2+9lambda*x=(3x/8)g_5=0.           (13)

Subtract (12) from (13) and divide by three. This gives

    tau*x^3-3kappa*x^2+3lambda*x-tau^2=0.

After x=sigma*X, these are exactly E(X)=J(X)=0 from (7).
The nonzero vector (X^8,X^7,...,X,1) would consequently lie in the
kernel of M. This contradicts (8). Thus the three polynomials in (3)
have no simultaneous zero, in particular none on the compact rectangle

    K={ (delta,s): |delta|<=sqrt(8v/3), 0<=s<=5v/3 }.

No exclusion of the boundary s=0 is needed. By continuity and the extreme
value theorem, eta=min_K(g_3^2+g_4^2+g_5^2)>0. Choose D>=8 large
enough that 400v^3/(d-1)^2<=eta/2 for every d>=D. Every feasible choice
then satisfies, by (10)-(11),

    g_4^2+g_5^2>=eta/2.                                 (14)

This is uniform over the entire feasible parameter set, not just a
convergent chosen sequence or a search over a compact interior.

### Comparison with the required cost threshold

From (10), rs^3<=(25/18)d*v^3 and rs^4<=(125/54)d*v^4.
For d>=8, each d-j with 1<=j<=4 is at least d/2. Applying these
bounds separately to the two nonnegative terms of (5) gives

    B_d >= d^4*g_4^2/(6400*v^3)
           +3*d^5*g_5^2/(1600000*v^4)
         >= d^4*C*(g_4^2+g_5^2),
    C=min{1/(6400*v^3), 3/(1600000*v^4)}>0.

Combine with (14) and set c=C*eta/2. This proves the claimed uniform
B_d>=c*d^4 eventually. In particular B_d/d^2 tends to infinity along
every feasible family. Positive reference-norm freedom in this specified
family does cancel the cubic but cannot meet even the two-term necessary
budget. No lower residual can cancel either retained square. The full
residual sum, actual heights and actual-Xi positivity are not established;
C028b's height criterion is motivation, not an extra premise here.

### Separate conceptual and complete certificate audit1506 (2026-11-18)

The unchanged SPECIALIZE assessment1504, approved in step1505, covers
this audit. No error affecting the statement was found. This verifies
the existing family obstruction; it neither strengthens that obstruction
nor counts it again as a new negative result beyond the checked sources.
Favard and Schmeisser are reused at the precise locations above.

**Finite expansion and norm indexing.** In the last recurrence,
(x-m)H_(d-2)=H_(d-1)+s(d-2)H_(d-3); multiplication by -u
therefore produces the negative last term of (1). Subtracting (1)
from (2), in descending degree, gives exactly (4). Once these three
coefficients vanish, the entire remainder is a linear combination of
H_0,...,H_(d-4), all of which equal the corresponding q polynomials.
Thus the fourth and fifth residuals in (5) do not acquire triangular
correction terms. At d=5 they are a_1=5g_4 and a_0=g_5.

The norm ratio beta_n=h_n/h_(n-1) occurs in the recurrence for q_(n+1),
not q_n. In particular the changed beta_(d-1) really changes h_(d-1),
although q_(d-1) itself contains no r. For k=4,5,

    (h_(d-k)/h_(d-1))*binom(d,k)^2
      =d^2*(d-1)...(d-k+1)/(k!^2*r*s^(k-1)).

This proves both constants in (5), including the endpoint d=5. The
Gaussian generating function and the local logarithm give (3) by finite
coefficient comparison; neither a global logarithm nor a limit exchange
is required. All source height terms are nonnegative squares with real
expansion coefficients, so retaining these two terms is legitimate.

**Analytic coefficient transfer and complete arithmetic.** The actual
even moment series in C028a is F(z)=sum M_(2j)z^j/((2j)!M_0).
Substitution in L778's G gives A_j=M_(2j)/(8*4^j*(2j)!), hence
4^j*A_j/A_0=f_j exactly. L778's (3) bounds errors in the coefficients
of the exact finite-integral polynomial P_0; its (4)-(5) bound the
separate theta-index, integration-range and cosh-series tails on the
whole complex disk. Their sum is not a real-axis-only error. Since
G-P_0 is entire, Cauchy's formula on radius1600 gives the additional
E_G/1600^j bound for every j=0,...,5, including j=0 before division.
Adding this to the saved coefficient widths accounts for both errors.

The independent checker `scripts/jacobi-reference/audit_penultimate_1506.py`
uses unrounded Fraction endpoint operations and imports no arithmetic
code from script1504. It verified source/program hashes, equality of
the whole saved evaluator with audit433's replay, the disk radius and
complete remainder, all six input coefficients, all normalized and
logarithmic coefficients, S_1,...,S_5, the feasibility margin, all
polynomial and matrix entries, and every one of the 512 determinant
states. For each nonempty mask it sums over the last selected column;
the new inversion count is the number of previous columns to its right.
Each saved state encloses that exact interval sum from previously checked
states. Induction from the empty determinant therefore checks the full
signed Leibniz sum, with no skipped states, pivots or floating arithmetic.
There were 643 enclosure checks, all passed. All six strict enclosures
in (8), including the signed determinant, passed with their printed
endpoints. Every input file remained unchanged.

Full exact required/actual endpoints and check records are in
`scripts/jacobi-reference/audit-penultimate-1506.json`, status PASS,
no failures. Reproduce with
`python3 scripts/jacobi-reference/audit_penultimate_1506.py`.
This is a second implementation of the finite certificate check, not
a fresh transcendental evaluator or an attestation of the Decimal
backend. L778's recorded analytic audit and arithmetic contracts remain
essential qualifications; the certificate is not formally verified.

**Elimination and boundary-uniform compactness.** The positive
feasibility margin in (8) gives tau<c_*^(3/2), so f(0)>0 and
f(sqrt(c_*))=2(tau-c_*^(3/2))<0. The open-interval root produces
the stated s>0,r>1 in every degree d>=5. No endpoint root is used.
For arbitrary feasible parameters, shifting the characteristic polynomial
by -b_1 gives second coefficient -binom(d,2)v. Its real symmetric
Jacobi matrix therefore has the trace square used in (9). The resulting
delta^2 bound is 2(d-1)v/(d-2)<=8v/3; the s and rs bounds are
d*v/(d-2)<=5v/3 and d*v/2. They imply (11) without dividing by a
lower bound for s or r. Thus no boundary scaling is lost.

For completeness, the elimination can be checked without an implicit
division by a possibly zero residual. On g_3=0, x=delta is nonzero
because tau>0, and A=-x^2/3-2tau/(3x). Substitution gives (12).
The following polynomial identity, before either residual is set to zero,
checks the other simplification:

    g_5-6(x^5-5x*A^2+4lambda)
      =5x*g_4+10(A-x^2)*g_3.

It yields (13) on g_3=g_4=0 after substituting A. Subtraction and
the scale x=X/200 give exactly (7). A common root would annihilate
each shifted E/J row of M; the vector ending in 1 is nonzero.
The checked determinant excludes that possibility over C, hence over R.
At delta=0 the already nonzero g_3=2tau handles the excluded division.

The rectangle K is closed and bounded and includes s=0. Continuity and
absence of a simultaneous zero make its minimum eta strictly positive.
The uniform estimate (11), not a selected convergent parameter subsequence,
then gives (14) for all feasible parameters when d>=D. Possible r tending
to zero cannot reduce the cost; all denominator bounds follow from the
upper bound on rs and the upper bound on s. At d>=8 the four factors
d-j are at least d/2, giving exactly the two constants in the final
comparison. Dropping the additional factor d>=1 in its second term
and using (14) proves the claimed c*d^4 bound. No effective eta,c,D
is extracted. Schmeisser still bounds actual heights from above: a lower
bound on I(P_d) proves no positive lower bound on those heights.

## Mathlib

Not checked. Full matching coverage, including the actual coefficient
enclosure and all-scaling reference-cost obstruction, is unknown.
No absence or formal verification is claimed. Favard and Schmeisser are
imported by precise citations; the local finite algebra, parameter bounds
and compactness argument are written above. The inherited numerical
contracts remain qualifications after the completed separate audit1506.
