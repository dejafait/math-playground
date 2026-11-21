# Corollary C028w: exact three-residual reduction and a necessary shape limit

## Hypotheses

Use C028a's actual real monic polynomial and coefficients

    b_j=j!*M_(2j)/((2j)!*M_0),
    P_d(x)=sum_(j=0)^d binom(d,j)*b_j*x^(d-j), d>=4.

Put v=b_1^2-b_2>0 and tau=(b_3-3*b_1*b_2+2*b_1^3)/2>0,
as proved in C028a, and put

    omega=b_4-4*b_1*b_3+6*b_1^2*b_2-3*b_1^4.

No sign or numerical value of omega is assumed. Let mu_0 be the full
even probability K(|u|)du/(2*M_0), using L019/L021. For each d choose
real t,A<B and s>0, without any bounds uniform in d, and set

    nu=((u->t+s*u)_*mu_0+delta_A+delta_B)/3.

Let q_j be its monic orthogonal polynomials, h_j=integral q_j^2 dnu,
and P_d=sum_(j=0)^d a_j*q_j. Assume exactly a_(d-1)=0. The statistic
is the approved retained cost

    B_d=sum_(k=2)^4 h_(d-k)*a_(d-k)^2/h_(d-1).

All degrees and all four parameters may vary; no actual-root reality,
RH, compact parameter range, base recurrence asymptotic or small full
cost is assumed. No numerical moment certificate is imported.

Hereafter a=(A-t)/s and b=(B-t)/s are standardized sites, with a<b;
the scalar a is distinct from the indexed expansion coefficients a_j.
Let pi_j and eta_j be the monic orthogonal polynomials and their
squared norms for the unnormalized measure mu_0+delta_a+delta_b.
Let m be the mean of the d zeros of pi_d, counted equally. Define

    pi_j(z+m)=sum_(k=0)^j e_(j,k)*z^(j-k), e_(j,0)=1,
    E=-e_(d,2),
    G=e_(d,3)/E^(3/2), L=e_(d,4)/E^2,
    U=e_(d-2,1)/sqrt(E), V=e_(d-2,2)/E,
    W=e_(d-3,1)/sqrt(E).

The same m from degree d centers every pi_j in these definitions.
In particular lower-degree polynomials are not independently centered.

## Conclusion

E>0. Feasibility a_(d-1)=0 is equivalent to t=-b_1-s*m.
Thus every s>0 and a<b has exactly one feasible translation, with
A=t+s*a and B=t+s*b. This parameterization loses no allowed choices.

Set

    x=s*sqrt(E)/d>0,
    A_d=binom(d,2)*v/d^2,
    C_d=2*binom(d,3)*tau/d^3,
    D_d=binom(d,4)*omega/d^4,
    R_2=x^2-A_d,
    R_3=C_d-x^3*G-x*R_2*U,
    R_4=D_d-x^4*L-x^2*R_2*V-x*R_3*W,
    Lambda_k=E^(k-1)*eta_(d-k)/eta_(d-1), k=2,3,4.

These are exact identities, not asymptotic approximations:

    a_(d-k)=d^k*R_k, k=2,3,4,
    B_d/d^2=Lambda_2*R_2^2/x^2
             +Lambda_3*R_3^2/x^4+Lambda_4*R_4^2/x^6.       (1)

Uniformly over every admissible finite choice,

    Lambda_2>=1, Lambda_3>=4, Lambda_4>=27,
    |U|<=2, -1<=V<=2, |W|<=sqrt(6),
    |G|<=2*sqrt(2)/3, -1/2<=L<=1/2.                       (2)

Consequently any feasible sequence with d->infinity and B_d/d^2->0
necessarily satisfies

    x^2 -> v/2,
    G -> G_*=(tau/3)/(v/2)^(3/2),
    L -> L_*=(omega/24)/(v/2)^2=omega/(6*v^2).             (3)

A sufficient, presently unproved condition for the requested uniform
floor is the following exact separation statement: there exist
epsilon>0 and D>=4 such that, for every d>=D and every a<b,

    |G_d(a,b)-G_*|+|L_d(a,b)-L_*|>=epsilon.               (4)

Under (4), there exist c>0 and D'>=4 with B_d>=c*d^2 for all
d>=D' and every feasible original parameter choice. No effective c
is claimed in this conditional implication.

Neither (4), a uniform cost floor, nor a vanishing-cost sequence is
established here. Approaching the pair in (3) alone is insufficient:
the positive Lambda_k can grow, and (1) still requires the corresponding
rates of residual decay. Omitted lower terms of Schmeisser's full cost
remain unpaid in every case. This finite specialization and exploratory
reduction is not a new general Uvarov theorem or an RH resolution.
Independent critical audit of the full statement is pending. The
separate audit1942 in C028z accepts the used affine normalization,
translation and coefficient identities (6),(8)-(9); it does not audit
the other weight bounds or necessary-limit claims here.

## Proof

### Imported finite interfaces and applicability

A. M. Delgado, L. Fernandez, T. E. Perez and M. A. Pinar,
*Multivariate Orthogonal Polynomials and Modified Moment Functionals*,
SIGMA12(2016),090, DOI10.3842/SIGMA.2016.090,
[Theorem3.1, (3.1)-(3.14), printed pp8-10](https://www.emis.de/journals/SIGMA/2016/090/sigma16-090.pdf),
supplies the finite-site connection and norm formulas. Both the original
and modified functionals must be quasi-definite. L019/L021 give finite
absolute moments and a strictly positive density for mu_0. Every
nonzero polynomial therefore has positive squared integral, and adding
the two positive atoms preserves this fact. Both functionals are positive
definite in every degree. The source applies to arbitrary distinct real
sites with unit masses; exterior-support assumptions are unnecessary.
The statement and complete proof were assessed in source-notes1931 and
its reused1908/1920/1926 coverage. They are imported, not reproved.

NIST [DLMF18.2(iv),(vi), equations18.2.11_4-8 and18.2.18](https://dlmf.nist.gov/18.2)
supplies the monic recurrence, norm ratios, real Jacobi matrix and
reference real-zero statements, under the same positive-measure
hypotheses. Evenness of the base supplies its parity, as in
[DLMF18.2.21](https://dlmf.nist.gov/18.2#E21). This is the finite
coverage reused in source-notes1931, not an imported asymptotic theorem.

Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
a Polynomial*, Mathematica Balkanica16(2002),203-217,
[Theorem1 and Corollary1, pp205-207; Lemmas1/4/5 and Theorem1 proof,
pp211-214](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
is the reason for considering this cost. For this real monic expansion
his statistic satisfies I^2=sum_(j=0)^(d-2)h_j*a_j^2/h_(d-1) and
the total absolute imaginary root height is at most I. Thus I^2>=B_d.
A lower bound on B_d obstructs this upper payment only; it gives no
lower bound on actual heights. These source facts are not reproved.
The new work below is the exact finite coordinate specialization and
its limits; the source formulas alone do not establish the target floor.

### Shared positive two-site formulas, with every needed coefficient

Let p_n be the base monic polynomials, k_n=integral p_n^2 dmu_0>0,
and beta_n=k_n/k_(n-1)>0 for n>=1. Set

    v_n=(p_n(a),p_n(b))^t,
    M[n]=I_2+sum_(j=0)^(n-1) v_j*v_j^t/k_j,
    u_(n,j)=v_n^t*M[n]^(-1)*v_j/k_j, 0<=j<n.

For n=0 use the empty sum M[0]=I_2; this matrix is distinct from the
theta moment M_0. The imported formulas in scalar
monic, column-vector notation are

    pi_n(z)=p_n(z)-sum_(j=0)^(n-1)u_(n,j)*p_j(z),
    eta_n=k_n+v_n^t*M[n]^(-1)*v_n.                        (5)

M[n] is positive definite, since its quadratic form is the Euclidean
squared norm plus a sum of nonnegative squares. In particular all
divisions in (5) exist and eta_n>0; eta_0=3. The same sites and same
matrix M[n] determine all coefficients at a fixed degree. No update
coefficient or norm is varied independently. Normalizing by3 gives

    q_j(z)=s^j*pi_j((z-t)/s), h_j=s^(2j)*eta_j/3.         (6)

For a completely finite way of extracting the top coefficients in (5),
write T_r=sum_(i=1)^r beta_i and

    Z_n=sum_(1<=i<j<=n-1, j-i>=2) beta_i*beta_j.

Empty sums are0. The even-base recurrence gives coefficients
1,0,-T_(n-1),0,Z_n in degrees n,n-1,n-2,n-3,n-4 when those
degrees exist. To check the only extra coefficient here, the recurrence
p_n=z*p_(n-1)-beta_(n-1)*p_(n-2) gives
Z_n=Z_(n-1)+beta_(n-1)*T_(n-3); this adds exactly the nonadjacent
pairs with larger index n-1. The coefficient -T_(n-1) follows by
the analogous sum recurrence, starting with p_0=1,p_1=z.

Writing c_(n,k)=[z^(n-k)]pi_n(z), formula (5) consequently gives

    c_(n,1)=-u_(n,n-1),                                  n>=1,
    c_(n,2)=-T_(n-1)-u_(n,n-2),                          n>=2,
    c_(n,3)=u_(n,n-1)*T_(n-2)-u_(n,n-3),                 n>=3,
    c_(n,4)=Z_n+u_(n,n-2)*T_(n-3)-u_(n,n-4),             n>=4.

These follow by collecting every possible degree: at degree n-3 the
p_(n-1) correction contributes +u_(n,n-1)*T_(n-2), and at degree
n-4 the p_(n-2) correction contributes +u_(n,n-2)*T_(n-3).
Parity excludes the other omitted terms. Finally m=-c_(d,1)/d and
the ordinary finite binomial expansion gives, for k<=min(4,j),

    e_(j,k)=sum_(r=0)^k c_(j,r)*binom(j-r,k-r)*m^(k-r),
    c_(j,0)=1.                                         (7)

Equations (5)-(7) specify the full two-site shape and every norm used
in (1), including the lower-degree centering contributions. They do
not assert any degree-uniform limit of base or modified recurrence data.

### Exact elimination of translation and extraction of residuals

The degree d-1 coefficient of q_d in (6) is
s*c_(d,1)-d*t=-d*(s*m+t). The same coefficient of P_d is d*b_1.
Since the expansion is monic, a_(d-1)=d*(b_1+t+s*m).
This proves the exact feasibility statement in the conclusion.

Set y=z+b_1 and Q_d(y)=P_d(y-b_1). A direct binomial expansion of
the first five coefficients of P_d gives

    Q_d(y)=y^d-binom(d,2)*v*y^(d-2)
               +2*binom(d,3)*tau*y^(d-3)
               +binom(d,4)*omega*y^(d-4)+lower terms.    (8)

For example the centered coefficients are respectively
b_2-b_1^2, b_3-3*b_1*b_2+2*b_1^3 and
b_4-4*b_1*b_3+6*b_1^2*b_2-3*b_1^4, times the indicated binomial
factors. Formula (8) is exact also at d=4, when the last displayed
term is constant. It uses no assertion about roots of Q_d.

Under the forced translation, (6) becomes

    q_j(y-b_1)=s^j*pi_j(y/s+m).

Its degree j-k coefficient is s^k*e_(j,k), and e_(d,1)=0.
Triangular coefficient comparison, retaining all lower-degree
contributions, gives

    a_(d-2)=-binom(d,2)*v+s^2*E,
    a_(d-3)=2*binom(d,3)*tau-s^3*e_(d,3)
                                -a_(d-2)*s*e_(d-2,1),
    a_(d-4)=binom(d,4)*omega-s^4*e_(d,4)
                  -a_(d-2)*s^2*e_(d-2,2)
                  -a_(d-3)*s*e_(d-3,1).                (9)

The vanished a_(d-1) contributes nothing. Divide these equations by
d^2,d^3,d^4 and substitute x=s*sqrt(E)/d to obtain R_2,R_3,R_4.
Using (6), each retained term divided by d^2 is exactly

    (s^(-2k+2)*eta_(d-k)/eta_(d-1))
                     *(d^(2k)*R_k^2)/d^2
      =E^(k-1)*eta_(d-k)/eta_(d-1)*R_k^2/x^(2k-2).

This proves (1) once E>0 is verified below. It also checks that the
normalizing factor3 cancels from every ratio, not from individual norms.

### Uniform bounds from the actual positive modified Jacobi matrix

Use modified recurrence coefficients alpha_j real and
beta'_j=eta_j/eta_(j-1)>0. Let J_d be the symmetric d-by-d Jacobi
matrix with diagonal alpha_0,...,alpha_(d-1) and off-diagonal
sqrt(beta'_1),...,sqrt(beta'_(d-1)). The imported recurrence identifies
det(z*I-J_d)=pi_d(z); its leading principal matrices represent pi_j.
Put X=J_d-m*I. Then tr X=0 and the characteristic polynomial of X
is pi_d(z+m). Newton's finite coefficient identity gives

    E=tr(X^2)/2
     =sum_(j=1)^(d-1) beta'_j
          +(1/2)*sum_(j=0)^(d-1)(alpha_j-m)^2>0.         (10)

For k=2,3,4, the k-1 distinct coefficients beta'_(d-k+1),...,beta'_(d-1)
occur in the positive sum in (10). Their product is
eta_(d-1)/eta_(d-k). The arithmetic-geometric mean inequality gives

    product_(j=d-k+1)^(d-1) beta'_j
          <=(E/(k-1))^(k-1).

Taking positive reciprocals proves Lambda_k>=(k-1)^(k-1), including
d=4, when the three coefficients for k=4 are beta'_1,beta'_2,beta'_3.

Let X_j be the leading j-by-j principal matrix of X, and put
delta_i=alpha_i-m. Since tr X=0, (7) or the characteristic-polynomial
coefficient formula yields

    e_(d-r,1)=-tr X_(d-r)=sum_(i=d-r)^(d-1) delta_i.

Cauchy-Schwarz and (10) bound its square by
r*sum_i delta_i^2<=2*r*E. Taking r=2,3 gives |U|<=2 and
|W|<=sqrt(6). Also

    e_(d-2,2)=((tr X_(d-2))^2-tr(X_(d-2)^2))/2.

Here 0<=tr(X_(d-2)^2)<=tr(X^2)=2E, since these traces are sums
of squares of entries, and (tr X_(d-2))^2<=4E by the bound just
proved. Dividing by E gives -1<=V<=2.

For completeness, let lambda_i be the real eigenvalues of X. Then
sum_i lambda_i=0 and sum_i lambda_i^2=2E. Newton's identities give

    e_(d,3)=-(1/3)*sum_i lambda_i^3,
    e_(d,4)=E^2/2-(1/4)*sum_i lambda_i^4.

Since sum_i|lambda_i|^3<=(sum_i lambda_i^2)^(3/2) and
0<=sum_i lambda_i^4<=(sum_i lambda_i^2)^2, these prove the bounds
for G and L in (2). These are facts about the reference matrix only;
there is no use of actual-root reality. This proves all of (2).

### The necessary limit, conditional floor and unpaid step

Take any feasible sequence with d->infinity and B_d/d^2->0.
By (1)-(2), R_2^2/x^2->0, so x-A_d/x->0. Because
A_d->v/2>0, the positive solution of x^2-y*x-A_d=0, with
y=x-A_d/x, shows x->sqrt(v/2). In particular x stays bounded
above and away from0 eventually, and R_2->0.

The next two nonnegative terms in (1), with Lambda_3>=4 and
Lambda_4>=27, imply R_3->0 and R_4->0. The uniform bounds on
U,V,W now apply to (9) in normalized form: R_2*x*U->0,
R_2*x^2*V->0 and R_3*x*W->0. Since C_d->tau/3 and
D_d->omega/24, solving the equations for G and L proves (3).
All these are finite identities followed by limits of scalar sequences;
no interchange of site/degree limits or infinite sums is used.

If (4) held but no eventual uniform positive floor existed, then for
each n one could select d_n>=max(n,D) and a feasible parameter choice
with B_(d_n)/d_n^2<1/n. This is exactly the negation of an eventual
uniform floor. Formula (3) contradicts (4), proving the conditional
implication. Actual parameters may escape or coalesce in this argument;
only each finite choice has s>0 and a<b, as required.

What remains is a restriction on the two-site image (5)-(7), or a
construction in that image with the rates required by (1). None of
the bounds (2) proves separation from the actual pair. They cannot
be inverted into an upper bound on B_d. The shared positive system
has been retained, but its degree-dependent shape image is not yet
controlled. This is the stopping point of attempt1933. C028p's even
reference floor and C028c's prescribed-recurrence floor remain scoped
comparisons, not inputs or conclusions about this family.

## Mathlib

Full matching coverage of this two-site specialization and uniform
three-residual reduction is not checked. The cited orthogonal-polynomial
and finite matrix results are supporting mathematical inputs, not a
claimed formal proof of this statement. No Mathlib absence or novelty
claim is inferred. No formal audit is claimed; conceptual audit1942
accepts only the identities used by C028z, as qualified above.
