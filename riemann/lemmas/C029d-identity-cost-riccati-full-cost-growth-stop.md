# Corollary C029d: identity-cost Riccati full-cost growth stop

## Hypotheses

Use C029b's actual positive coefficients b_j, b_0=1, entire function
F(z)=sum_(j>=0)b_j*z^j/j!, and centered normalized companion C_d.
Explicitly, for every integer d>=3, put

    c_(d,k)=binom(d,k)*sum_(j=0)^k binom(k,j)*b_j*(-b_1)^(k-j),
    q_(d,k)=c_(d,k)/d^k,
    (C_d)_(j+1,j)=1                  (1<=j<d),
    (C_d)_(j,d)=-q_(d,d-j+1)         (1<=j<=d),
    M_d=[0 -C_d; C_d 0],
    A=exp(b_1)*F(1)>1,
    m_2=b_2-b_1^2.

All other companion entries vanish. The two prescribed sets of entries
are disjoint. C029b proves ||C_d||_op=||M_d||_op<=A with this finite,
degree-independent A. Do not use C029b's finite-horizon Gramian here.

Instead prescribe the identity-cost stabilizing Riccati solution

    M_d^T*X_d+X_d*M_d-X_d^2+I_(2d)=0,
    X_d real symmetric positive definite,
    spectrum(M_d-X_d) contained in {z: Re z<0}.

Let G_d^R be its upper-left d by d principal block and set

    B_d^R=(G_d^R)^(1/2)*C_d*(G_d^R)^(-1/2),
    J_d^R=(B_d^R-(B_d^R)^*)/(2i),
    k_d^R=||J_d^R||_1,
    u=sqrt(1+A^2)+A,
    a=sqrt(1+A^2)-A=1/u>0.

Square roots are positive symmetric square roots. The norms ||.||_1,
||.||_F and ||.||_op are respectively Schatten trace, Frobenius and
Euclidean operator norms, without dimension normalization. No actual
root reality, diagonalizability, separation, conditioning assumption,
numerical moment contract or RH is imposed. In particular the sign of
m_2 is not assumed.

## Conclusion

The prescribed X_d exists uniquely among positive definite stabilizing
solutions. The block G_d^R is positive definite, and

    a*I_(2d) <= X_d <= u*I_(2d),
    a*I_d <= G_d^R <= u*I_d,
    cond_2(G_d^R) <= u/a=u^2.                              (1)

For the complete matrix cost, not a terminal compression,

    (k_d^R)^2 >= max{0,
        [a^2*(d-1)+(1-1/d)*m_2]/2}.                       (2)

Consequently

    liminf_(d->infinity) k_d^R/sqrt(d) >= a/sqrt(2)>0,
    k_d^R -> infinity.                                    (3)

An explicit sufficient onset for k_d^R>=a*sqrt(d)/2 is

    d >= d_0=max{3, ceil(2+2*|m_2|/a^2)}.                 (4)

Thus the prescribed identity-cost Riccati metric cannot pay the desired
k_d^R=o(1) sufficient condition for C028b's H_d=o(d). This is a local
specialization under assessment1954, independently audited1958 below;
no originality beyond the sources checked is certified. It stops this
metric's upper-majorant route, not RH or general positive metrics.

## Proof

### Imported results and exact applicability

Harald K. Wimmer, *On the algebraic Riccati equation*, Bulletin of the
Australian Mathematical Society 14 (1976), 457-461,
[equations (1)-(3), pp.457-458; definitions and Theorems 2-3,
pp.459-461](https://doi.org/10.1017/S0004972700025387), covers the real
equation A_0+W*B_0+B_0^T*W+W*C_0*W=0 with A_0 symmetric
positive semidefinite, C_0 symmetric negative semidefinite,
controllable (B_0,C_0), and observable stacked (B_0;A_0).
It supplies a positive definite stabilizing solution, uniquely in the
positive stabilizing class, with B_0+C_0*W stable. Substitute

    A_0=I_(2d), B_0=M_d, C_0=-I_(2d), W=X_d.

The input -I has full range, so the controllability matrix already
has full row rank in its first block. The output I has zero kernel,
so the observability matrix already has full column rank in its first
block. The coefficient signs and symmetry hold exactly. Thus no
condition on the spectrum or Jordan form of M_d is needed. Import
this existence result; its general proof is not repeated.

John Watrous, *The Theory of Quantum Information*, 2018 author version,
[Section 1.1, (1.165)-(1.181), printed pp.32-34](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf),
supplies the Schatten norm definitions, Frobenius formula, monotonicity
||J||_1>=||J||_F, and the ideal inequality
||U*V*W||_F<=||U||_op*||V||_F*||W||_op. The operators here are
finite square matrices of compatible sizes; complex Hermitian J is
within scope. The source assessments1954/1523/1947 already cover these
inputs. Only the quantitative Riccati and actual-companion algebra
below is derived here, rather than reproving the imported theorems.

### Degree-uniform spectral enclosure

Suppress d. Since X is real symmetric positive definite, choose any
real unit eigenvector v with eigenvalue x>0. Taking v^T(. )v in the
Riccati equation gives

    2*x*t-x^2+1=0,       t=v^T*M*v,       |t|<=A.

Indeed v^T*M^T*X*v=x*(M*v)^T*v=x*t and
v^T*X*M*v=x*t; this uses the eigenvector of X, not one of M.
The positive root is x=t+sqrt(t^2+1). Equivalently
t=(x-x^(-1))/2 is strictly increasing for x>0, so -A<=t<=A
implies a<=x<=u. The spectral theorem yields the first enclosure
in (1). For any y in R^d, inserting (y,0) into that enclosure gives

    a*||y||^2 <= y^T*G_d^R*y <= u*||y||^2.

This proves block positivity, its enclosure and its condition bound.
The equality a*u=1 follows by multiplying sqrt(1+A^2)-A and
sqrt(1+A^2)+A. All constants are independent of d.

### Complete companion Frobenius size and square trace

The coefficient definition gives exactly

    q_(d,1)=0,
    q_(d,2)=(d-1)*m_2/(2*d).

The d-1 unit subdiagonal entries and the last column are disjoint.
Therefore, with every last-column entry retained,

    ||C_d||_F^2=d-1+sum_(k=1)^d q_(d,k)^2 >= d-1.          (5)

For clarity compute the square trace directly, without any spectral
assumption on C_d. In tr(C_d^2)=sum_(j,k)(C_d)_(j,k)(C_d)_(k,j),
a product of two subdiagonal entries vanishes. A last-column entry
can pair with a subdiagonal entry only at the positions (d-1,d) and
(d,d-1). These contribute -q_(d,2) each. The sole possible diagonal
contribution is (C_d)_(d,d)^2=q_(d,1)^2=0. Hence

    tr(C_d^2)=-2*q_(d,2)=-(1-1/d)*m_2.                   (6)

In particular this trace is bounded in absolute value by |m_2|,
although (5) grows with degree. No last-column term is deleted from
the matrix or from its Frobenius norm to obtain these statements.

### Similarity and full imaginary-part lower bound

Write G=G_d^R and B=B_d^R, both real. Reconstructing the original
companion from the similarity and using the p=2 ideal inequality gives

    ||C_d||_F=||G^(-1/2)*B*G^(1/2)||_F
       <= sqrt(u/a)*||B||_F=u*||B||_F.

Consequently ||B||_F^2>=a^2*||C_d||_F^2>=a^2*(d-1).
Cyclicity of the finite trace gives tr(B^2)=tr(C_d^2) exactly.
Also B^*=B^T. Entrywise expansion, summing all ordered pairs, shows

    ||J_d^R||_F^2
      =sum_(j,k) (B_(j,k)-B_(k,j))^2/4
      =[||B||_F^2-sum_(j,k)B_(j,k)*B_(k,j)]/2
      =[||B||_F^2-tr(B^2)]/2.

Thus (5)-(6) imply

    ||J_d^R||_F^2 >= [a^2*(d-1)+(1-1/d)*m_2]/2.

The trace norm dominates the Frobenius norm, and both squared norms
are nonnegative. This proves (2), including the positive part for
small degrees. Dividing by d and taking lower limits yields
liminf (k_d^R/sqrt(d))^2>=a^2/2; since the sequence is nonnegative,
this implies (3). For d>=2+2*|m_2|/a^2, the right side before
taking its positive part is at least

    [a^2*(d-1)-|m_2|]/2 >= a^2*d/4.

This proves (4) and also directly proves divergence of k_d^R.
These are exact inequalities, with no computed-sample or limit
interchange assumption.

### Meaning for the height criterion and route stop

Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
a Polynomial*, Mathematica Balkanica 16 (2002), 203-217,
[Lemma 1, pp.211-212](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
bounds the sum of absolute imaginary eigenvalue parts by the trace
norm of the Hermitian imaginary part. Its applicability and degree
scale are the same as in C029b: C_d is similar to the centered
companion divided by d, the real centering preserves imaginary parts,
and G^(1/2) is invertible. Algebraic multiplicities are retained.
Thus H_d/d<=k_d^R, with C028b's complete root height H_d.

If k_d^R=o(1), this comparison would give H_d=o(d) and hence RH
by C028b. Instead (3) stops that sufficient payment for this metric.
A growing upper majorant of H_d/d is not a lower bound on H_d/d;
it is compatible with H_d=0. No off-line zero, failure of RH,
actual signed-positivity violation, or obstruction to all other
metrics is inferred. Finite existence and stabilization alone cannot
remove the present full-matrix cost. Stops1948/1949 and the nilpotent
model C029c are contrasts only, not inputs to this proof.

### Independent application audit1958

20 November 2026. The separate audit under the preexisting SPECIALIZE
assessment1956, approved1957, passes without repair. The inspected
primary-source coverage in source-notes1954/1523 is reused; this audit
does not claim fresh browsing or verification of Gohberg--Krein.

Wimmer's substitution has symmetric state coefficient I>=0 and
quadratic coefficient -I<=0. The first controllability and observability
blocks already have rank 2d, and the stable matrix is exactly M-X.
The positive stabilizing solution therefore exists for the actual
possibly nonnormal companion. No spectrum premise is introduced.
C029b's coefficient argument retains the entire positive Cauchy product
and bounds both ||C||_op and ||M||_op by the finite constant A.

For an eigenvector of X, the two linear compressions each equal xt,
not a Rayleigh quotient of M on its own eigenvectors. Of the roots
t+/-sqrt(1+t^2), exactly the plus root is positive. Monotonicity gives
[a,u], and principal restriction gives the same block bounds. In
reconstructing C from B, the norm multiplier is sqrt(u/a)=u; squaring
and reversing yields a^2, not a. The d-1 shift entries are disjoint
from the full last column for every d>=3. Both ordered products at
(d-1,d) and (d,d-1) enter tr(C^2); q_(d,1)=0 removes its sole possible
diagonal term. No omitted column term changes either formula.

The real-matrix expansion of ||(B-B^T)/(2i)||_F^2 counts every ordered
entry and gives exactly (||B||_F^2-tr(B^2))/2. Combining it with the
trace-norm domination proves (2) even when its inner expression is
negative. The onset check reduces to a^2*d-2*a^2-2*|m_2|>=0, exactly
the sufficient threshold (4); d_0 also enforces the integer range.
The normalized squared lower bound tends to a^2/2, and nonnegativity
permits taking square roots to obtain (3).

Finally C029b's monic normalization preserves C028b's root multiset;
the real centering preserves imaginary parts, the positive factor 1/d
divides their absolute sum, and the G similarity preserves algebraic
multiplicities. Schmeisser supplies H_d/d<=k_d^R in this direction
only. Thus the audit sustains this prescribed metric's decay stop,
without a lower bound on H_d, a restriction on arbitrary metrics, a
stronger estimate than (2)-(4), or a complete RH candidate.

## Mathlib

Not checked. Full matching coverage for this actual Riccati-block
sequence and its cost growth is unknown, not claimed absent. The
standard existence and norm inputs are imported by precise citations;
the explicit spectral, coefficient and trace specialization is proved
above and passes the separate application audit1958. No formal verification or complete
RH candidate is claimed.
