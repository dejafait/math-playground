# Corollary C029a: the first omitted cost obstructs the local two-site branch

## Hypotheses

Use exactly C028z's full even theta base, two unit masses, strict point
(c_0,x_1,x_2) with c_0>0 and x_1>x_2>0, and its common local inverse
branch (c_d,y_(1,d),y_(2,d))=(c_0,x_1,x_2)+O(1/d). Integers d>=5
tend to infinity beyond that branch's existential onset. In its notation,

    T_d=sum_(j=1)^(d-1) beta_j, L_d=sqrt(T_d),
    a_d^site=-L_d*y_(1,d)/c_d, b_d^site=-L_d*y_(2,d)/c_d,
    s_d=d*c_d/L_d, t_d=-b_1-s_d*m_d.

Here beta_j are base norm ratios and m_d is the mean of the degree-d
zeros for mu_0+delta_(a_d^site)+delta_(b_d^site). The probability
measure nu_d is its affine pushforward by u -> t_d+s_d*u, divided
by3. Write q_j for its monic orthogonal polynomials, h_j for their
squared norms, and P_d=sum_j a_j*q_j for the actual real polynomial

    P_d(X)=sum_(j=0)^d binom(d,j)*b_j*X^(d-j).

The indexed a_j are expansion coefficients, distinct from sites.
All these objects may depend on d. Use C028z's exact cancellations
a_(d-1)=a_(d-2)=a_(d-3)=a_(d-4)=0 and its accepted finite graph
and trace-norm estimates. No other C028w weight claim is assumed.

Use C028c's actual coefficients v=S_2, tau=S_3, kappa=S_4 and
lambda=S_5, with

    x_1^3+x_2^3=tau, x_1^4+x_2^4=kappa,
    log F(z)=b_1*z-v*z^2/2+tau*z^3/3-kappa*z^4/4
                                  +lambda*z^5/5+O(z^6),
    F(z)=sum_(j>=0)b_j*z^j/j!.

Its audited coefficient enclosures retain L778's entire-evaluator
remainder and Python3.15.2/Decimal1.70/libmpdec4.0.1 correctly rounded
arithmetic contracts, including allcr=1. These are inherited inputs,
not a new backend attestation. No actual-root reality, exterior-support
condition, leading recurrence constant, effective onset or small full
cost is supplied.

## Conclusion

Put Delta=lambda-x_1^5-x_2^5. Under those inputs,

    Delta > (1/200)^5/200 > 0,
    a_(d-5)/d^5 = Delta/5+O(1/d),                       (1)
    liminf_(d->infinity) [h_(d-5)*a_(d-5)^2/(h_(d-1)*d^2)]
        >= 4096*Delta^2/(25*v^4) > 1/50000000.         (2)

The full Schmeisser statistic I(P_d) for this branch therefore is
not o(d). This obstructs its proposed upper payment for C028b's
H_d=o(d); it gives no lower bound on actual root heights, nonreal
zero or resolution of RH. It does not exclude other branches or
other reference families. C028z's exact retained cancellation remains
valid. All other omitted costs and the main positivity gap remain open.

This is a branch-specific result of attempt1944, not supplied by the
general imported theorems. Separate conceptual audit1946 below accepts
it under the stated inputs; no certified originality is claimed.

## Proof

### Imported finite interfaces and applicability

NIST [DLMF18.2(iv),(vi), equations18.2.11_4-8 and18.2.18](https://dlmf.nist.gov/18.2)
supplies the real monic recurrence, positive norm ratios and finite
Jacobi-zero identification. C028z's full positive theta density has
all moments. Adding two positive unit atoms, applying the invertible
real affine map s_d>0, and normalizing by3 preserve positivity in
every polynomial degree. Thus all norms below are finite and strictly
positive, and these interfaces apply separately for every d.

A. M. Delgado, L. Fernandez, T. E. Perez and M. A. Pinar,
*Multivariate Orthogonal Polynomials and Modified Moment Functionals*,
SIGMA12(2016),090,
[Theorem3.1,(3.1)-(3.14),pp8-10](https://www.emis.de/journals/SIGMA/2016/090/sigma16-090.pdf),
supplies the shared finite two-site system inherited through C028z.
Original and modified quasi-definiteness follow from the positivity
just checked. That theorem is imported, not reproved or used as an
asymptotic zero-attraction theorem.

Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros
of a Polynomial*, Mathematica Balkanica16(2002),203-217,
[(1.1)-(1.5),Theorem1/Corollary1,pp203-207; proof pp211-214](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
gives, for this real monic expansion,

    I(P_d)^2=sum_(j=0)^(d-2) h_j*a_j^2/h_(d-1),
    sum_(P_d(z)=0)|Im z| <= I(P_d).

Roots count multiplicities. The source's imaginary penultimate
coefficient is zero here. Each summand is nonnegative, so (2) obstructs
I=o(d) only. Source-review1943 covers these precise interfaces and
their applicability. The following fifth-order specialization and
norm comparison are the uncovered work; no general source theorem
is being reproved.

### Extending the finite trace comparison to power five

Use C028z's independent variables z_i=a_i^site/L_d=-y_i/c on the
fixed parameter neighborhood, and its matrices K,D in (11)-(13).
K has eigenvalues lambda_i/L_d, where lambda_i are the unscaled
reference zeros. With n=d-2,

    D=diag(J_n/L_d,z_1,z_2),
    ||K-D||_* = O(delta_d), ||K||+||D||=O(1),
    delta_d=max_(j<d)beta_j/T_d=O(1/d).

The norm ||.||_* is the sum of singular values. These estimates hold
uniformly on that neighborhood; K need not be symmetric. The exact
finite telescoping identity is

    K^5-D^5=sum_(j=0)^4 K^j*(K-D)*D^(4-j).

The inequalities |tr X|<=||X||_* and
||AXB||_*<=||A||*||X||_* *||B|| consequently give

    |tr(K^5)-tr(D^5)| <= 5*C^4*||K-D||_* = O(1/d),

with a fixed bound C for both operator norms and no dimension factor.
The even-base Jacobi matrix J_n has zero diagonal. Conjugating it
by diag(1,-1,1,-1,...) gives -J_n; hence its odd traces, including
tr J_n^5, are exactly zero. Put rho_k=tr K^k for k>=1. We obtain

    rho_5=z_1^5+z_2^5+O(1/d).

C028z already bounds rho_1,...,rho_4 uniformly, with m_d/L_d=rho_1/d.
The complete finite centering identity is

    sum_i((lambda_i-m_d)/L_d)^5
      =rho_5-5*rho_1*rho_4/d+10*rho_1^2*rho_3/d^2
              -10*rho_1^3*rho_2/d^3+4*rho_1^5/d^4.

Thus centering changes this trace by O(1/d). The roots of
q_d(Y-b_1) are s_d*(lambda_i-m_d). If N_5^q is their fifth
power sum, multiplication by (s_d*L_d/d)^5=c_d^5 yields

    N_5^q/d^5=-y_(1,d)^5-y_(2,d)^5+O(1/d)
             =-x_1^5-x_2^5+O(1/d).                    (3)

Only finitely many products and the accepted uniform neighborhood
are involved. No limit exchange, individual zero differentiation,
actual-root reality or fifth-power assertion from an unaudited input
has been assumed.

### The actual fifth coefficient and triangular residual

Let E_k^P=[Y^(d-k)]P_d(Y-b_1), and define E_k^q analogously.
Finite binomial expansion of P_d gives

    E_k^P=binom(d,k)*g_k,
    g_k=k! times the coefficient of z^k in F(z)*exp(-b_1*z).

For completeness, the coefficient at Y^(d-k) is
sum_(j=0)^k binom(d,j)*b_j*binom(d-j,k-j)*(-b_1)^(k-j);
factor out binom(d,k) to obtain that identity. Exponentiating
C028c's local logarithm through degree five gives

    g_1=0, g_2=-v, g_3=2*tau, g_5=24*lambda-20*v*tau.

Indeed the only contributions to the fifth Taylor coefficient are
lambda/5 and (-v/2)*(tau/3). These are coefficients of a local
analytic logarithm, not moments of an assumed positive zero measure.

Newton's finite identities for a centered monic polynomial give
N_2=-2E_2, N_3=-3E_3 and

    N_5+E_2*N_3+E_3*N_2+5*E_5=0,
    N_5=5*E_2*E_3-5*E_5.

They are algebraic identities, also for nonreal roots with multiplicity.
Since binom(d,k)/d^k=1/k!+O(1/d) for these fixed indices,

    E_2^P/d^2=-v/2+O(1/d),
    E_3^P/d^3=tau/3+O(1/d),
    E_5^P/d^5=lambda/5-v*tau/6+O(1/d),
    N_5^P/d^5=-lambda+O(1/d).                          (4)

The first four exact cancellations say that the monic P_d and q_d
have identical first four lower coefficients. Translation by -b_1
preserves this equality, and their common first centered coefficient
is zero. Monicity in the triangular expansion therefore gives

    a_(d-5)=E_5^P-E_5^q=(N_5^q-N_5^P)/5.

There is no cross term from lower q_j, and the coefficients of
q_(d-1),...,q_(d-4) vanish exactly. Equations (3)-(4) prove the
asymptotic formula in (1), including its sign and factor1/5.

### A strictly positive actual coefficient gap

Set sigma=1/200, X=x_1/sigma, Y=x_2/sigma, and

    V=v/sigma^2, T=tau/sigma^3, Q=kappa/sigma^4,
    H=lambda/sigma^5.

C028c's audited enclosures (8) imply the deliberately coarse rational
bounds

    0<V<3/2,
    11533/10000<T<11534/10000,
    10608/10000<Q<10609/10000,
    H>10283/10000.                                     (5)

They concern the actual coefficients, not fitted values. We inspected
the complete selected S_2,S_3,S_4,S_5 records in certificate1506 and
reuse its prior audit under the stated evaluator contracts.

Because X>Y>0, put r=Y/X in (0,1). The equations for the strict
point imply

    f(r):=(1+r^3)^4/(1+r^4)^3=T^4/Q^3,
    X^4=Q/(1+r^4).

Logarithmic differentiation of this positive rational function gives

    f'(r)/f(r)=12*r^2*(1-r)/((1+r^3)*(1+r^4))>0.

The following strict comparisons involve only rational numbers:

    f(57/100)<(11533/10000)^4/(10609/10000)^3,
    (11534/10000)^4/(10608/10000)^3<f(59/100),
    10609/10000<(99/100)^4*(1+(57/100)^4).              (6)

Thus 57/100<r<59/100, X<99/100, and
Y=r*X<(59/100)*(99/100)<59/100. In particular this argument applies
to the strict point chosen in C028z without selecting a different
branch. It follows that

    Delta/sigma^5=H-X^5-Y^5
      >10283/10000-(99/100)^5-(59/100)^5
      =29087601/5000000000 > 1/200.                    (7)

The exact comparisons (5)-(7), including all source interval
endpoints used, are saved in
`scripts/jacobi-reference/first-omitted-two-site-cost-1944.json`.
Reproduce with
`python3 scripts/jacobi-reference/first_omitted_two_site_cost_1944.py`.
It uses integer Fraction arithmetic only, records the reused input's
hash, complete selected bounds, all rational comparison margins and
failures. It does not rerun or attest L778's transcendental evaluator,
solve for finite-degree sites or verify the analytic proof above.

### Four adjacent norms from the exact centered variance

Use a new symbol gamma_j=h_j/h_(j-1)>0 for the modified, scaled
measure's ratios, 1<=j<=d-1. Its d-by-d real symmetric Jacobi
matrix J has these square roots on the off-diagonal and real diagonal
entries alpha_j. This is the reference matrix, not a matrix for P_d.
The first two matched centered coefficients imply exactly

    tr((J+b_1*I)^2)=d*(d-1)*v.

Indeed its eigenvalues are the roots of q_d shifted by b_1, and
their squared sum is -2E_2^q=-2E_2^P=d*(d-1)*v. In matrix entries,

    sum_(j=1)^d (alpha_j+b_1)^2
                 +2*sum_(j=1)^(d-1)gamma_j=d*(d-1)*v.

All terms here are nonnegative. The arithmetic-geometric mean
inequality on precisely the four positive ratios with indices
d-4,d-3,d-2,d-1 consequently gives

    product_(j=d-4)^(d-1)gamma_j
      <= ((sum_(j=d-4)^(d-1)gamma_j)/4)^4
      <= (d*(d-1)*v/8)^4,
    h_(d-5)/h_(d-1) >= (8/(d*(d-1)*v))^4.             (8)

These indices are valid already at d=5. The normalization by3 cancels
in every ratio; the affine scaling is already included in gamma_j
and in the matched variance. No lower bound or asymptotic formula
for an individual gamma_j is needed. This proves the required norm
comparison directly rather than importing C028w's other weight claims.

Combining (8) with the residual gives, at every allowed d,

    h_(d-5)*a_(d-5)^2/(h_(d-1)*d^2)
      >= (8/v)^4*(d/(d-1))^4*(a_(d-5)/d^5)^2.

Taking the lower limit and using (1) proves the first inequality (2).
By (5),(7) its right side is strictly greater than

    (4096/25)*((sigma^5/200)^2)/((3*sigma^2/2)^4)
       =16/791015625 > 1/50000000.

The exact final comparison is in the same rational certificate. It
provides a limiting floor, not an effective onset. Schmeisser's sum
contains this nonnegative fifth term for every d>=5, which proves
the stated branch obstruction and no stronger root-height assertion.

### Separate conceptual and complete rational-evidence audit1946

20 November 2026. Assessment1944, separately approved1945, covers exactly
this audit. No error affecting (1)-(2) was found. This supplies local
verification of the existing conditional branch obstruction, not a
stronger obstruction, a new theorem or a second informative negative.
The finite source coverage and the evaluator qualifications above are
reused. C028z's accepted graph/trace estimates and its used C028w/y
reductions suffice; their other claims are not silently accepted here.

**Fixed neighborhood and fifth trace.** C028z(11)-(13) control the
operator norms of K,D and the trace norm of K-D on one neighborhood
containing the entire eventual inverse branch. With n=d-2, the only
bulk block in D is J_n/L_d; both its even-base parity and the two scalar
site blocks are retained. The telescoping formula has exactly five
terms. In each term only K-D needs a trace-norm estimate, and all four
other factors have bounded operator norm. Thus its trace is O(1/d)
independently of matrix dimension, even though K is nonsymmetric.
The alternating-sign conjugation of J_n proves its fifth trace is zero
also when n is odd. Similarity to the reference Jacobi matrix justifies
the spectral power sums without assuming anything about actual P_d.

Writing mu=rho_1/d, direct finite binomial expansion gives
rho_5-5*mu*rho_4+10*mu^2*rho_3-10*mu^3*rho_2
+5*mu^4*rho_1-d*mu^5. The last two terms combine to
4*rho_1^5/d^4. The accepted bounds rho_1,...,rho_4=O(1)
therefore make every centering correction O(1/d). The roots of
q_d(Y-b_1) are exactly s_d*(lambda_i-m_d): t_d+b_1=-s_d*m_d.
Multiplication by c_d^5 cancels the denominator in
z_i=-y_(i,d)/c_d and gives the minus sign in (3). Uniformity on
the common neighborhood and y_(i,d)=x_i+O(1/d) prove the stated
remainder. No fifth derivative, infinite trace or individual-root
regularity is needed.

**Actual normalization and triangular comparison.** C028c's audited
normalization is G(w)=gamma_0*F(w/4)/8, hence
[z^j]F=4^j*[w^j]G/[w^0]G, before taking the logarithm.
Its S_5 is therefore the lambda used here, without a missing 4^5
or factorial. That audit includes the entire complex-disk remainder
before division by the constant coefficient. We reuse that input;
the present rational script does not certify its evaluator backend.

After centering, the degree-five exponential coefficient is
lambda/5-v*tau/6. Multiplication by 5! gives
g_5=24*lambda-20*v*tau. The finite binomial coefficient extraction
for E_k^P uses binom(d,j)*binom(d-j,k-j)=binom(d,k)*binom(k,j),
so its limiting normalization is 1/k!, as written. Newton's identity
N_5=5*E_2*E_3-5*E_5 cancels the v*tau contributions and yields
N_5^P/d^5=-lambda+O(1/d). The matched first four coefficients
make P_d-q_d have degree at most d-5. Its coefficient at that
degree is a_(d-5), since every q_j is monic. Translation preserves
this leading difference, giving (N_5^q-N_5^P)/5 with the positive
sign in (1). These algebraic steps permit nonreal roots and multiplicity.

**Strict gap and complete saved evidence.** The complete selected
/actual_and_required_bounds/S_2 through /S_5 records of
`scripts/jacobi-reference/audit-penultimate-1506.json` were inspected,
along with every original1944 rational comparison and its implementation.
The exact positive derivative of f on (0,1) gives both strict r bounds
from (6); positive fourth powers then give X<99/100, and
Y=r*X<5841/10000<59/100. This applies to the existing strict point,
without choosing a new solution. All inequality directions are retained
when subtracting the fifth powers. The gap lower bound is exactly
29087601/5000000000 in sigma^5 units, exceeding 1/200 by
4087601/5000000000.

The independent checker
`scripts/jacobi-reference/audit_first_omitted_cost_1946.py`
imports no code from script1944. It reconstructs all 25 comparisons
from the selected source intervals and the printed rational constants,
compares every saved operand and margin, and checks positivity by integer
cross multiplication. It also checks complete selected-record copies,
all normalized intervals, source hash, coarse bounds, summary and failure
fields. All 76 checks pass, with no failures. Source1506, certificate1944
and its implementation remain byte-for-byte unchanged. Full evidence is
`scripts/jacobi-reference/audit-first-omitted-cost-1946.json`;
reproduce with `python3 scripts/jacobi-reference/audit_first_omitted_cost_1946.py`.
This is finite rational verification, not a new transcendental replay.

**Four norms and lower limit.** For the affine measure,
h_j=s_d^(2j)*eta_j/3, where eta_j is the unscaled squared norm.
Thus gamma_j=s_d^2*eta_j/eta_(j-1), and the Jacobi trace identity
already uses exactly the scaled ratios. Dividing the measure by3
has no residual effect. Centering by b_1 gives squared eigenvalue sum
d*(d-1)*v because the second actual centered coefficient is
-binom(d,2)*v. The diagonal squares of the real symmetric reference
matrix are nonnegative, so the bound on the sum of gamma_j in (8)
is valid. Telescoping h_(d-1)/h_(d-5) gives exactly
gamma_(d-4)*gamma_(d-3)*gamma_(d-2)*gamma_(d-1), four factors.
At d=5 this is gamma_1*gamma_2*gamma_3*gamma_4=h_4/h_0;
there is no missing endpoint or fifth norm factor. AM-GM then gives
precisely the denominator 8 in (8).

The resulting lower bound is
(8/v)^4*(d/(d-1))^4*(a_(d-5)/d^5)^2. Its right side converges
to 4096*Delta^2/(25*v^4); taking a lower limit is legitimate even
if the left side has no limit. The strict input bounds yield
16/791015625>1/50000000, with margin 23/101250000000.
All finite degrees below the existential onset remain outside the claim.

The accepted C028z estimates and C028c enclosures are used only within
their stated hypotheses. The downstream C028b criterion is not assumed.
Schmeisser supplies H_d<=I(P_d),
so this accepted floor only rules out I(P_d)=o(d) on this branch.
It implies neither a positive lower bound for H_d nor failure of RH.
Other branches, full-cost upper control and the inherited arithmetic
contracts remain unresolved. The proof assembly and DAG are unchanged.

## Mathlib

Full matching coverage has not been checked. The cited finite
orthogonal-polynomial interfaces, Newton identities, trace identities
and AM-GM are supporting inputs and calculations; no matching formal
theorem, absence from Mathlib or formal verification is claimed.
The rational certificates check only the displayed arithmetic.
The separate informal conceptual audit1946 accepts the local proof;
it provides no formal verification or new backend attestation.
