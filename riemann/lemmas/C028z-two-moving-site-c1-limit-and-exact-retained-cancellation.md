# Corollary C028z: moving-site C^1 limit and exact retained cancellation

## Hypotheses

Use C028x's full even theta probability mu_0, monic orthogonal
polynomials p_j, squared norms k_j, and beta_j=k_j/k_(j-1)>0.
In particular k_0=1, p_0=1, p_1(x)=x. For integers d>=4 set

    T_d=sum_(j=1)^(d-1) beta_j, L_d=sqrt(T_d),
    M_d=max_(1<=j<=d-1) beta_j, delta_d=M_d/T_d.

Use the audited C028x bound delta_d=O(1/d). All constants implicit
below are independent of d but may depend on the fixed parameter
neighborhood and the constants in that bound. No leading recurrence
constant or monotonicity is assumed.

For c>0 and y_1>y_2>0 prescribe

    a_d=-L_d*y_1/c, b_d=-L_d*y_2/c, s_d=d*c/L_d.

Let lambda_i, 1<=i<=d, be the zeros, with multiplicity, of the degree-d
monic polynomial for mu_0+delta_(a_d)+delta_(b_d), and let
m_d=(sum_i lambda_i)/d. Define exactly the assessed observable

    F_d(c,y_1,y_2)=(
      (s_d/d)^2*sum_i(lambda_i-m_d)^2,
      -(s_d/d)^3*sum_i(lambda_i-m_d)^3,
      (s_d/d)^4*sum_i(lambda_i-m_d)^4).

For the actual-coefficient application use C028w's real coefficients
b_j, v=b_1^2-b_2, tau=(b_3-3*b_1*b_2+2*b_1^3)/2, and
omega=b_4-4*b_1*b_3+6*b_1^2*b_2-3*b_1^4. Put
kappa=(3*v^2-omega)/6. Use C028y's strict solution

    x_1>x_2>0, x_1^3+x_2^3=tau, x_1^4+x_2^4=kappa,
    x_1^2+x_2^2<v,
    c_0=sqrt((v-x_1^2-x_2^2)/2)>0.

This last input inherits C028c's L778 entire-evaluator and
Python3.15.2/Decimal1.70/libmpdec4.0.1 correctly rounded arithmetic
contracts, including allcr=1. Backend correctness is not independently
attested here. The general local limit does not use those numerical
contracts. Audit1942 below accepts the portions of C028w/y used here;
their other claims retain their previous audit status.

The measure retains its full support R and both atomic masses are1.
No exterior-support hypothesis, actual-P_d root reality, unproved zero
attraction, variable masses, or small full cost is assumed.

## Conclusion

On every compact parameter neighborhood inside c>0,y_1>y_2>0,
with the C^1 norm including the three first partial derivatives,

    ||F_d-F_infinity||_(C^1)=O(1/d),                     (1)
    F_infinity=(2*c^2+y_1^2+y_2^2,
                y_1^3+y_2^3,y_1^4+y_2^4).

More precisely the estimates hold on an open neighborhood of such a
compact set. They do not assert uniformity up to coincident sites,
y_2=0 or c=0, or throughout an unbounded parameter region.

Under the additional strict-solution input, for every sufficiently
large integer d there are parameters

    (c_d,y_(1,d),y_(2,d))=(c_0,x_1,x_2)+O(1/d)

and a common fixed neighborhood containing them, such that with

    t_d=-b_1-s_d*m_d,
    A_d=t_d+s_d*a_d < B_d^site=t_d+s_d*b_d,
    nu_d=((u->t_d+s_d*u)_*mu_0+delta_(A_d)+delta_(B_d^site))/3,

the expansion P_d=sum_j a_j*q_j in the monic orthogonal basis of nu_d
satisfies

    a_(d-1)=a_(d-2)=a_(d-3)=a_(d-4)=0.                 (2)

Here A_d and B_d^site denote sites, not C028w's auxiliary constants
or its retained cost. The latter cost, denoted here by B_d^cost, is
exactly zero. Thus an eventual positive uniform floor for these three
retained terms fails in this family. The onset and parameter values
are existential, not effective numerical certificates.

Conceptual audit1942 accepts this local result of attempt1940 under
the stated inputs; it is not a resolution of RH. All omitted full
Schmeisser terms remain uncontrolled; zero
retained cost does not imply small full cost or C028b's H_d=o(d).
The bounded source search did not supply this precise joint C^1
statement; the audit establishes no general novelty claim.

## Proof

### Imported interfaces and scope

NIST [DLMF18.2(iv),(vi), equations18.2.11_4-8 and18.2.18](https://dlmf.nist.gov/18.2)
supplies the positive-measure monic recurrence, norm ratios and
Jacobi-zero identification. Its even-base parity is equation18.2.21.
The full theta density is positive with all moments by the inputs to
C028x. Adding two positive unit atoms preserves positive definiteness
in every degree; scaling the entire measure by1/3 does not change
its monic polynomials. These facts justify all finite uses here.

A. M. Delgado, L. Fernandez, T. E. Perez and M. A. Pinar,
*Multivariate Orthogonal Polynomials and Modified Moment Functionals*,
SIGMA12(2016),090,
[Theorem3.1,(3.1)-(3.14),pp8-10](https://www.emis.de/journals/SIGMA/2016/090/sigma16-090.pdf),
gives C028w's shared finite Uvarov system under original and modified
quasi-definiteness, both implied by the positivity just checked.
C028y's finite multiplication compression represents exactly that
same measure. Neither theorem supplies a degree-uniform estimate;
we derive the graph and trace bounds needed for this specialization.
The general Uvarov theorem is imported, not reproved.

W. Rudin, *Principles of Mathematical Analysis*, third edition(1976),
[Theorems9.23-9.24 and full proof,pp220-223](https://djvu.online/file/cNW6EtZ7m9PIB),
supplies contraction and local inversion for C^1 maps with invertible
derivative. Its common-ball hypotheses for this varying-degree family
are verified explicitly below. Source-notes1931/1934/1938 cover these
imports and C028x's recurrence inputs. Fixed-degree exterior-support
and increasing-mass attraction theorems are not used.

### Uniform recurrence ratios at the two sites

First work in independent variables z_1=a_d/L_d and z_2=b_d/L_d.
Fix a compact set in z_1<z_2<0 and an open neighborhood on which

    q<=|z_i|<=Q, z_2-z_1>=g,                            (3)

for fixed q,g>0 and Q<infinity. Estimates on this neighborhood give
both the value and derivative bounds on the compact set. Suppress d
in L,T,M,delta, and let epsilon_j=sqrt(beta_j)/L<=sqrt(delta).
For j>=1 put

    h_j(z)=p_j(L*z)/(L*p_(j-1)(L*z)).

The even-base recurrence gives

    h_1(z)=z,
    h_j(z)=z-(beta_(j-1)/T)/h_(j-1)(z), 2<=j<=d-1.     (4)

For all sufficiently large d, uniformly in those indices and in (3),

    |h_j|>=q/2, |h_j-z|<=2*delta/q,
    |h_j'|<=2, |h_j'-1|<=8*delta/q^2.                 (5)

Here and below primes mean derivative with respect to z. To verify
both existence and the estimates, start with p_0=1 and h_1=z.
If |h_(j-1)|>=q/2, (4) gives the stated difference from z;
delta<=q^2/8 makes that difference at most q/4 and prevents a zero.
Thus all polynomial denominators and h_j exist by induction.
Differentiating the finite recurrence gives
h_j'=1+(beta_(j-1)/T)*h_(j-1)'/h_(j-1)^2.
If |h_(j-1)'|<=2, its deviation from1 is at most8*delta/q^2<=1.
This proves (5), including the j=1 case.

Let phi_j=p_j/sqrt(k_j). Then phi_0=1 and

    r_j(z):=phi_(j-1)(L*z)/phi_j(L*z)=epsilon_j/h_j(z).

With theta=2*sqrt(delta)/q, taken <=1/2 by increasing the onset,

    |r_j|<=theta, |r_j'|<=(4/q)*theta.                 (6)

Any product of ell consecutive such factors consequently has absolute
value at most theta^ell and derivative at most
(4/q)*ell*theta^ell. This is the finite product rule, including signs;
no derivative-limit interchange or individual polynomial asymptotic
has been used.

### A joint coordinate system with a small graph

Set n=d-2. In the base orthonormal coordinates of degrees0,...,d-1,
let V have rows (phi_j(L*z_i))_j, and split

    V=[V_low H],

where H consists of degrees n,n+1 and V_low of degrees0,...,n-1.
Put epsilon=epsilon_(n+1). The exact factorization is

    H=diag(phi_n(L*z_1),phi_n(L*z_2))
         *S*diag(1,1/epsilon),
    S=[1 h_(n+1)(z_1); 1 h_(n+1)(z_2)].                (7)

The determinant of S is h_(n+1)(z_2)-h_(n+1)(z_1).
By (3),(5) it is at least g-4*delta/q>=g/2 eventually.
The entries of S and their first partial derivatives are uniformly
bounded. The explicit two-by-two inverse and
partial(S^(-1))=-S^(-1)*(partial S)*S^(-1) therefore bound S^(-1)
and its derivatives independently of d.

Let U_(i,j)=phi_j(L*z_i)/phi_n(L*z_i) for 0<=j<n.
It is a product of n-j factors (6). Summing their squared bounds and
the derivative bounds gives

    ||U||_F + ||partial_(z_1)U||_F
              +||partial_(z_2)U||_F <= C*theta,         (8)

because sum_(ell>=1)theta^(2ell) and
sum_(ell>=1)ell^2*theta^(2ell) are at most constants times theta^2
for theta<=1/2. The subscript F is the Frobenius norm. The other
variable's derivative of each row is zero.

Also 1/phi_n(L*z_i)=product_(j=1)^n r_j(z_i). Hence its value and
first derivatives are bounded by C*(n+1)*theta^n. Formula (7) now
gives the two exact expressions

    H^(-1)=diag(1,epsilon)*S^(-1)
                       *diag(1/phi_n(L*z_i)),
    W:=H^(-1)V_low=diag(1,epsilon)*S^(-1)*U.

Here epsilon<=1 eventually and is independent of z_1,z_2. Thus

    ||W||_(C^1,F)<=C*sqrt(delta),
    ||H^(-1)||_(C^1,F)<=C*(n+1)*theta^n
                            <=C*sqrt(delta).           (9)

The last inequality follows from
(n+1)*theta^(n-1)<=(n+1)*2^(-(n-1)), uniformly bounded for n>=2.
Every inverse in (9) is joint in the two sites; large individual
kernel entries have not been treated as a conditioning estimate.

For clarity, a polynomial's first n base coefficients will be w and
its two values at L*z_1,L*z_2 will be v. Its remaining two base
coefficients are exactly H^(-1)*v-W*w. In the enlarged space
(base coefficients,atomic values), reorder coordinates as

    E=(first n base coordinates,two atomic coordinates),
    N=(last two base coordinates).

The actual polynomial space is the graph N=B*E, where

    B=[-W H^(-1)],
    ||B||_F+sum_(i=1)^2||partial_(z_i)B||_F
                                      <=C*sqrt(delta). (10)

The fixed masses1 and k_0=1 are retained in this exact Euclidean
embedding. In particular its metric on E is G=I+B^t*B.

### Trace control without a dimension loss

Let J_d be the base Jacobi matrix and J_n its leading n-by-n block.
It has zero diagonal and off-diagonal sqrt(beta_j). The elementary
quadratic-form estimate in C028y gives ||J_d||<=2*sqrt(M).
The enlarged normalized multiplication form diag(J_d/L,z_1,z_2),
in the order E,N, is

    [D C; C^t R], D=diag(J_n/L,z_1,z_2).                (11)

Only base coordinates occur in C,R. Therefore these matrices are
independent of z_1,z_2, and

    ||C||_F<=2*sqrt(2*delta), ||R||<=2*sqrt(delta),
    ||D||<=max(2*sqrt(delta),Q), ||partial_(z_i)D||=1.

The actual graph multiplication matrix, with its metric included, is

    K=G^(-1)*(D+C*B+B^t*C^t+B^t*R*B).                 (12)

By C028y's finite compression, or the same inner-product matrix in
the new invertible coordinates, K is similar to the symmetric
modified Jacobi matrix divided by L. Its eigenvalues are exactly
lambda_i/L. It need not itself be symmetric. All entries in (12)
are smooth functions of the sites; differentiability of individual
zeros is neither used nor needed.

Write ||.||_* for the sum of singular values. Finite singular-value
decomposition gives ||UXV||_*<=||U||*||X||_* *||V|| and
|tr X|<=||X||_*. Also ||AB||_*<=||A||_F*||B||_F:
expand AB as a sum of column-times-row matrices, whose trace norms
are products of their vector lengths, and apply Cauchy-Schwarz.
These elementary finite bounds are used to prevent a factor d.

Put P=G^(-1). Positivity gives ||P||<=1, and

    P-I=-P*B^t*B,
    partial P=-P*((partial B)^t*B+B^t*(partial B))*P.

It follows from (10) that P-I and each partial P have trace norm
at most C*delta. In particular the operator norms obey the same
bounds. In (12) put Z=C*B+B^t*C^t+B^t*R*B. The product bounds,
(10),(11), and the ordinary product rule give

    ||Z||_*+sum_i||partial_(z_i)Z||_*<=C*delta.

For example ||C*B||_*<=||C||_F*||B||_F=O(delta), and
||B^t*R*B||_*<=||B||_F^2*||R||=O(delta^(3/2)); its two derivative
terms have the same bound. Since K-D=(P-I)*D+P*Z, we obtain

    ||K-D||_*+sum_i||partial_(z_i)(K-D)||_*
                                         <=C*delta.   (13)

Both K,D and their first partial derivatives have bounded operator
norms, independently of d. For each fixed k=1,...,4 use the finite
noncommutative telescoping identity

    K^k-D^k=sum_(j=0)^(k-1) K^j*(K-D)*D^(k-1-j).

Taking traces and differentiating this finite identity, each summand
contains either K-D or its derivative with trace norm O(delta);
the other factors and derivatives have bounded operator norms.
Consequently

    tr(K^k)-tr(D^k)=O_(C^1)(delta), k=1,...,4.          (14)

This estimate is independent of dimension. It accounts for changes
to the bulk and the atomic directions together.

### Raw traces, centering and the prescribed limit

Let rho_k=sum_i(lambda_i/L)^k=tr(K^k). The zero diagonal and parity
of J_n give tr J_n=tr J_n^3=0. Moreover

    tr((J_n/L)^2)=2*sum_(j=1)^(d-3)beta_j/T
                 =2-2*(beta_(d-2)+beta_(d-1))/T,
    0<=tr((J_n/L)^4)
           <=||J_n/L||^2*tr((J_n/L)^2)<=8*delta.

These quantities are independent of the two sites. Thus (14) proves

    rho_1=z_1+z_2+O_(C^1)(delta),
    rho_2=2+z_1^2+z_2^2+O_(C^1)(delta),
    rho_3=z_1^3+z_2^3+O_(C^1)(delta),
    rho_4=z_1^4+z_2^4+O_(C^1)(delta).                  (15)

In particular all four are bounded in C^1 and m_d/L=rho_1/d.
Writing sigma_k=sum_i((lambda_i-m_d)/L)^k, finite binomial expansion
gives exactly

    sigma_2=rho_2-rho_1^2/d,
    sigma_3=rho_3-3*rho_1*rho_2/d+2*rho_1^3/d^2,
    sigma_4=rho_4-4*rho_1*rho_3/d
                  +6*rho_1^2*rho_2/d^2-3*rho_1^4/d^3.

The centering corrections and their first derivatives are O(1/d).
Since delta=O(1/d), (15) therefore remains valid for sigma_k, k=2,3,4,
with errors O_(C^1)(1/d).

Finally z_i=-y_i/c. On any fixed compact neighborhood in the stated
parameter domain, these variables satisfy (3) after slightly enlarging
the compact set, and their first derivatives are bounded. The chain
rule in these finite formulas, followed by multiplication by
c^2,-c^3,c^4 respectively, gives precisely (1). No infinite
sum is interchanged with a degree limit, and no rootwise convergence
or derivative-limit interchange is used.

### Common inverse neighborhood and the exact finite target

Let u_0=(c_0,x_1,x_2) and f=F_infinity. By the strict-solution input,
f(u_0)=(v,tau,kappa). Its derivative has determinant

    det Df(c,y_1,y_2)=48*c*y_1^2*y_2^2*(y_2-y_1),       (16)

because only the first row has a nonzero c derivative, namely4c,
and the remaining two-by-two determinant is
12*y_1^2*y_2^2*(y_2-y_1). It is nonzero at u_0.

The exact target for degree d is the real vector

    tgt_d=((1-1/d)*v,
         (1-1/d)*(1-2/d)*tau,
         (v^2/2)*(1-1/d)^2
          -(omega/6)*(1-1/d)*(1-2/d)*(1-3/d)).           (17)

It tends to f(u_0) with error O(1/d). To check (17), C028w(8)
gives the actual centered polynomial P_d(Y-b_1) coefficients

    e_2=-binom(d,2)*v, e_3=2*binom(d,3)*tau,
    e_4=binom(d,4)*omega, e_1=0.

Newton's finite identities give centered root sums
-2*e_2,-3*e_3,2*e_2^2-4*e_4. With the negative sign in F_d's
third-power component and division by d^2,d^3,d^4, these are exactly
(17). This is a coefficient calculation; actual roots need not be real.

Here are the uniform hypotheses for Rudin's contraction construction.
Put A=Df(u_0). By continuity choose a fixed closed Euclidean ball
of radius r>0 centered at u_0, contained in the parameter domain,
on a neighborhood of which

    sup ||I-A^(-1)*Df(u)||<=1/4.

Equation (1) gives, for every sufficiently large d, the same bound
with DF_d in place of Df and right side1/2. Thus A^(-1)*DF_d=I-E
with ||E||<=1/2, whose inverse is the convergent geometric matrix
series sum_(j>=0)E^j. This also verifies finite-degree nondegeneracy
throughout the common ball. Equation (1) also gives

    ||A^(-1)*(F_d(u_0)-tgt_d)||<=r/2.

The map u -> u-A^(-1)*(F_d(u)-tgt_d) is therefore Lipschitz with
constant at most1/2 on this convex ball, by integration along a
line segment. The last displayed bound makes it a self-map of the
ball. The ball is nonempty and complete. The imported contraction
theorem supplies a fixed point u_d and hence F_d(u_d)=tgt_d for every
sufficiently large integer d, all in this same ball. Moreover

    ||u_d-u_0||<=2*||A^(-1)*(F_d(u_0)-tgt_d)||=O(1/d).

This verifies a common finite-degree image neighborhood and target
control as follows. Increase the onset so that
||F_d(u_0)-f(u_0)||<=r/(4*||A^(-1)||). Every target within
r/(4*||A^(-1)||) of f(u_0) then meets the same self-map bound by
the triangle inequality. The contraction argument applies uniformly
to every such target. Its uniqueness and the finite nondegeneracy
already proved give local inverses on the interior of this common
image ball. In particular (17) lies in it eventually.

### Exact cancellation and remaining costs

Choose the sites and scale from u_d and the translation
t_d=-b_1-s_d*m_d, exactly as required in C028w. Since c_d>0 and
y_(1,d)>y_(2,d)>0, s_d>0 and a_d<b_d, so A_d<B_d^site. All
parameters are real and the reference measure has positive norms.
The translation gives a_(d-1)=0 and centers q_d(Y-b_1).

The equality F_d(u_d)=tgt_d in (17) says that this centered reference
polynomial and P_d(Y-b_1) have identical second, third and fourth
root-power sums.
Both are monic of degree d with first centered sum zero. Newton's
identities therefore make their coefficients of degrees d-2,d-3,d-4
equal as well. Equivalently C028w(9) first gives a_(d-2)=0; then
its cubic equation gives a_(d-3)=0; finally its quartic equation,
with both lower cross terms zero, gives a_(d-4)=0. This proves (2).
All three positive norm-weighted retained terms are exactly zero,
so no upper estimate on their possibly large weights is needed.

The Schmeisser statistic still includes degrees below d-4. No bound
on their sum, no small full statistic, and no actual-root-height
conclusion follows from this proof. Stops1933/1937 are preserved as
failures of their respective positivity-only and envelope-separation
mechanisms; neither asserted that this realization was impossible.

### Separate conceptual audit1942 (20 November 2026)

Under the unchanged EXPLORE assessment review1940, separately approved
in1941, this audit accepts (1)-(2) with their stated scope. No failed
estimate or change to the mathematical conclusion was found. The
verification below reproduces the local argument; it is not a new
general theorem, a new source assessment, or an independent attestation
of the numerical backend. Source-notes1931/1934/1938 and the already
audited C028x are reused. In particular no fixed-degree exterior-support
or increasing-mass theorem is substituted for a joint-degree estimate.

**Used finite interfaces.** C028w's formula (6) has exactly
q_j(x)=s^j*pi_j((x-t)/s) and h_j=s^(2j)*eta_j/3. Positivity of the
full density gives finite strictly positive norms before and after
adding the two unit masses. Normalizing by3 changes those norms,
but not the monic polynomials. If c_(d,1)=-d*m, the coefficient of
x^(d-1) in q_d is -d*(t+s*m). Comparison with d*b_1 gives
a_(d-1)=d*(b_1+t+s*m), proving the exact translation used here.
Then q_j(Y-b_1)=s^j*pi_j(Y/s+m). This uses the degree-d mean for
every j, exactly as in C028w; no separate centering of lower degrees
is permitted. Direct binomial comparison verifies C028w(8)-(9),
including all lower-degree cross terms when they are present. The
present proof ultimately sets their coefficients to zero, rather than
estimating or ignoring them. C028w's other weight and limiting-shape
claims are not required for this audit.

For C028y's compression, in the degree<d base coordinates a polynomial
with coefficient vector h has squared modified norm
h^t*(I+V^t*V)*h and multiplication form h^t*(J_d+V^t*diag(a,b)*V)*h.
These follow from the two point evaluations and the base integrals,
including the top-degree base entry: the degree-d component of
x*phi_(d-1) is orthogonal to all degree<d polynomials. Thus using
J_d as a form loses no boundary contribution. Orthogonalizing for the
modified norm identifies the resulting symmetric form with the
modified degree-d Jacobi matrix. Its characteristic polynomial is
pi_d by the imported DLMF recurrence. This proves precisely the
finite eigenvalue identification used in (12), with no assumption
that an actual P_d zero is real and no asymptotic zero attraction.

**Joint graph and indices.** Choose the onset so that
delta<=min(q^2/16,q*g/8), and increase it if necessary. The first
condition both preserves |h_j|>=q/2 inductively in (4) and gives
theta<=1/2. The derivative recurrence bounds |h_j'|<=2 and
|h_j'-1|<=8*delta/q^2. Hence differentiating r_j gives
|r_j'|<=8*epsilon_j/q^2=(4/q)*(2*epsilon_j/q)
<=(4/q)*theta. There is no accumulation of a factor j in this
recurrence estimate. Products acquire only the explicit length ell
in their derivative bound. The convergent majorants
sum_(ell>=1)theta^(2ell) and sum_(ell>=1)ell^2*theta^(2ell) are
O(theta^2) uniformly for theta<=1/2; they bound finite sums, without
interchanging a derivative and an infinite limit.

The last two columns are degrees n=d-2 and n+1=d-1. The denominator
epsilon in (7) is therefore sqrt(beta_(d-1))/L; its inverse cancels
as diag(1,epsilon) in H^(-1). No lower bound for an individual beta
is needed in this inversion. The determinant of S is at least
g-4*delta/q>=g/2 even though the two rows separately have enormous
evaluations. The identity 1/phi_n(L*z)=product_(j=1)^n r_j(z)
uses k_0=1. Its derivative has the bound C*n*theta^n, and
(n+1)*theta^n<=theta*(n+1)*2^(-(n-1))=O(sqrt(delta)) uniformly
for n>=2. These facts verify the value and both site derivatives
in (8)-(10). The graph coordinates are invertible because H is;
their metric is exactly I+B^t*B, with no missing mass or norm factor.

**Dimension-independent traces.** In (11) C has only the link from
base degree n-1 to n, with normalized entry sqrt(beta_n)/L. R has
the link between n and n+1, with entry sqrt(beta_(n+1))/L. Both
indices lie within the maximum defining M. They are independent of
the sites, and the stated bounds for C and R are valid. D includes
the unaltered leading J_n/L and the two scalar site coordinates.
The pullback multiplication form is exactly D+C*B+B^t*C^t+B^t*R*B;
left multiplication by G^(-1) is necessary for its operator matrix.
Indeed K is similar, via G^(1/2), to the symmetric matrix
G^(-1/2)*(D+C*B+B^t*C^t+B^t*R*B)*G^(-1/2).

The products B^t*B and each differentiated product have trace norm
O(delta), by the displayed Frobenius bounds. Multiplication on
either side by P=G^(-1), with ||P||<=1, preserves this order.
Thus P-I and partial P have trace norm O(delta). Likewise C*B
and its derivatives have trace norm O(delta), while B^t*R*B and
its two differentiated terms have order delta^(3/2). Differentiating
(P-I)*D+P*Z adds only bounded operator factors. This checks (13)
for both sites and for the nonsymmetric K itself.

For (14), differentiating the finite telescoping sum always leaves
either K-D or its derivative as a trace-norm O(delta) factor.
Derivatives of the other factors have bounded operator norms;
in particular partial K=partial D+O_*(delta) is bounded. There are
only finitely many terms for each k<=4, independent of d. The
inequality |tr X|<=||X||_* therefore incurs no dimension factor.
The bulk tr((J_n/L)^2) removes exactly beta_(d-2),beta_(d-1)
from 2*T/T, an O(delta) error. Bipartite parity gives zero odd
traces, and the positive second trace and operator bound give the
fourth-trace bound8*delta. All these bulk terms have zero site
derivatives. This verifies (15), including its derivative claims.

**Centering, actual input and exact target.** The three binomial
centering identities after (15) are exact with m/L=rho_1/d.
Both rho_k and their derivatives are O(1), so every displayed
centering correction is O_(C^1)(1/d). On a compact parameter set
bounded away from c=0, y_2=0 and y_1=y_2, the change z_i=-y_i/c
has bounded first derivatives and retains fixed q,g,Q. Multiplication
by c^2,-c^3,c^4 proves the claimed three-variable C^1 bound using
delta=O(1/d). No regularity of individually ordered roots is needed.

The actual coefficient convention has
F(z)=sum b_j*z^j/j!. The coefficient of z^4 in F(z)*exp(-b_1*z)
is both omega/24 and v^2/8-kappa/4 in C028c's local logarithm.
Thus kappa=(3*v^2-omega)/6 is exactly its S_4. The corresponding
quadratic and cubic comparisons identify v=S_2 and tau=S_3, agreeing
with C028a's audited convention. C028c's enclosures (8) are reused,
including its entire complex-disk remainder and Cauchy errors before
normalization. The complete selected /actual_and_required_bounds/S_2,
/actual_and_required_bounds/S_3 and /actual_and_required_bounds/S_4
records in scripts/jacobi-reference/audit-penultimate-1506.json were
inspected with the shared inspect_json.py and --full. This is a
bounded input read, not a rerun of certificate1506 or its evaluator.

For sigma=1/200 their coarse bounds imply
v/sigma^2>37/25, 23/20<tau/sigma^3<29/25 and
53/50<kappa/sigma^4<107/100. Exact rational arithmetic gives the
three strict margins in C028y as 0.0504, 0.52396325 and 0.57139264,
respectively. They imply v^2>2*kappa>0 and
kappa^3<tau^4<2*kappa^3. The continuous f(r) in C028y takes
values1 and2 at r=0 and1, so an intermediate value strictly between
them is attained at some interior r. No monotonicity or uniqueness
of r is needed. Its positive fourth-root construction then gives
x_1>x_2>0 with cubic sum tau and fourth sum kappa. Cauchy--Schwarz
gives (x_1^2+x_2^2)^2<=2*kappa<v^2, proving c_0>0.
This verifies precisely the strict solution used here under C028c's
L778/Decimal contracts; no full audit of C028y's other envelope
claims or fresh backend verification is asserted.

For P_d(Y-b_1), its first centered coefficient is zero. Newton's
identities are p_2=-2*e_2, p_3=-3*e_3 and
p_4=2*e_2^2-4*e_4. Substitution of C028w(8), and the negative
sign in F_d's cubic component, gives every factor in (17). In
particular the limiting quartic target is v^2/2-omega/6=kappa.
These are identities of coefficients, valid even with nonreal roots.

**One common inverse ball and cancellation.** Expanding the limiting
Jacobian along its first column gives exactly (16), nonzero at the
strict point. Continuity permits a fixed closed ball with a slightly
larger open neighborhood inside the parameter domain and the limiting
derivative bound1/4. The C^1 estimate on that neighborhood gives
the finite-degree bound1/2 on the same ball for all sufficiently
large d. The segment estimate applies because this ball is convex;
the center displacement is O(1/d), hence at most r/2. Consequently
the stated contraction is a self-map of a nonempty complete ball.
Its fixed point is at distance O(1/d) from u_0, not just somewhere
in an unrelated degree-dependent neighborhood. For target points
in the open image ball of radius r/(4*||A^(-1)||), the displacement
bound is strict after the stated onset, so their fixed points are
interior; the invertible derivative and uniqueness give the local
inverses claimed. The exact tgt_d is included eventually.

Finally q_d(Y-b_1) has roots s_d*(lambda_i-m_d). The equality of
F_d and tgt_d therefore matches the first four centered power
sums of this reference polynomial and the actual P_d, with the
correct powers of d. Both polynomials are monic. Newton's identities
match their first four coefficients, and triangular expansion in
the monic q_j basis makes a_(d-1),...,a_(d-4) exactly zero. All
retained weights are finite and positive for each finite d, so their
possible growth does not affect this exact vanishing.

This accepts only the local C^1 result and its conditional actual-input
application. All degrees below d-4, their norm-weighted costs and
H_d=o(d) remain uncontrolled. The previous stops1933/1937 keep their
original scopes. No omitted cost or stronger actual-Xi conclusion has
been added to the argument.

## Mathlib

Full matching coverage is not checked. The cited recurrence, Uvarov
and local-inverse theorems are informal standard inputs; finite
matrix and Newton identities are supporting calculations. No formal
verification, absence from Mathlib or certified originality is claimed.
The informal conceptual audit1942 above accepts the stated local result;
it does not supply formal coverage or remove the arithmetic contracts.
