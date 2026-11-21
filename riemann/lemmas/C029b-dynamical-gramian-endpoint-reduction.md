# Corollary C029b: dynamical Gramian endpoint reduction

## Hypotheses

Use C028b's actual coefficients b_j=gamma_j/gamma_0>0, b_0=1,
entire function F(z)=sum_(j>=0)b_j*z^j/j!, and complete imaginary
root height H_d. Use C028h's exact centered polynomial and companion:

    Q_d(y)=P_d(y-b_1)=sum_(k=0)^d c_(d,k)*y^(d-k),
    c_(d,k)=binom(d,k)*sum_(j=0)^k binom(k,j)*b_j*(-b_1)^(k-j),
    (A_d)_(j+1,j)=1,  (A_d)_(j,d)=-c_(d,d-j+1).

Here d>=3 is an integer, 1<=j<d in the subdiagonal prescription,
1<=j<=d in the last-column prescription, and other entries vanish.
Fix exactly assessment1947's objects:

    D_d=diag(1,d,...,d^(d-1)),  C_d=d^(-1)*D_d*A_d*D_d^(-1),
    M_d=[0 -C_d; C_d 0],  T_d=d^2,
    W_d=integral_0^(T_d) exp(t*M_d^T)*exp(t*M_d) dt,
    G_d=T_d^(-1) times the upper-left d by d block of W_d.

Let E_d include coordinates d-2,d-1,d, in that order, and define

    Gamma_d=E_d^T*G_d*E_d,
    R_d=Gamma_d^(-1/2)*E_d^T*(G_d*C_d-C_d^T*G_d)*E_d
                              *Gamma_d^(-1/2)/(2i),
    r_d=||R_d||_1,
    J_d=(G_d^(1/2)*C_d*G_d^(-1/2)
                  -G_d^(-1/2)*C_d^T*G_d^(1/2))/(2i),
    k_d=||J_d||_1.

In this file J_d denotes this matrix, not C028b's Jensen polynomial.
All square roots of positive matrices are the positive symmetric ones;
||.||_1 is the Schatten trace norm and ||.||_op is the Euclidean
operator norm. No real or simple spectrum, diagonalizability,
spectral separation, numerical coefficient enclosure, bounded metric
conditioning or RH is assumed.

## Conclusion

G_d and Gamma_d are positive definite, and the correctly scaled
comparisons are

    r_d <= k_d,                  H_d/d <= k_d.                 (1)

The following finite formulas retain the complete matrix C=C_d.
Suppress d, write T=d^2, E=E_d, and put

    X(t)=cos(t*C),  Y(t)=sin(t*C),
    H(t)=E^T*(X(t)^T*X(t)+Y(t)^T*Y(t))*E,
    B=integral_0^T H(t)dt=T*Gamma_d,
    L=E^T*(X(T)^T*Y(T)-Y(T)^T*X(T))*E,
    a=(L_23,-L_13,L_12)^T.

Then B is positive definite, L is real skew-symmetric, and exactly

    R_d=B^(-1/2)*L*B^(-1/2)/(2i),
    r_d^2=(a^T*B*a)/det(B).                                  (2)

In particular the explicit factor 1/T in the unnormalized endpoint
identity does not by itself give a factor 1/T in r_d.

Define the finite, degree-independent constant A=exp(b_1)*F(1)>1.
One has the uniform but insufficient bounds

    ||C_d||_op <= A,
    0 <= r_d <= 2*A/(1-exp(-2*A*d^2)),
    limsup_(d->infinity) r_d <= 2*A.                          (3)

For the same H(t), the terminal Krylov chain gives the further exact
endpoint identity

    a=(-H_22'(T)/2, H_12'(T), -H_11'(T)/2)^T.                 (4)

Thus the sought escape requires a^T*B*a=o(det B); a positive liminf
of that ratio would instead give the stipulated compression floor.
Neither alternative is proved. Equation (3) is O(1), not o(1), and
is an upper bound, not evidence for a positive liminf. Full k_d=o(1),
H_d=o(d), and RH remain open. This is a finite specialization and an
inconclusive bounded attempt, not a claimed new asymptotic discovery.

The integrated signed calculation below also gives the exact split

    r_d^2=(B_13-B_22)^2/det(P) + v^T*P*v/[det(P)*eta],       (8)

where P is B's leading two by two block, z=(B_13,B_23)^T,
eta=B_33-z^T*P^(-1)*z>0, and
v=(a_1,a_2)^T+(B_13-B_22)*P^(-1)*z. Both terms are nonnegative.
Neither term has been bounded by o(1), nor has a positive liminf
of their sum been established. This refinement is still inconclusive.

## Proof

### Imported results and applicability

Tony Stillfjord and Filip Tronarp, *Computing the matrix exponential
and the Cholesky factor of a related finite horizon Gramian*,
arXiv:2310.13462v2, 30 April 2024,
[Section 1, (1b)-(2), p.1; Section 1.2, (5), p.4](https://arxiv.org/pdf/2310.13462v2),
gives the finite-horizon Gramian, positivity for controllable input,
and its endpoint identity. With N=T*M_d^T and input sqrt(T)*I, its
unit-interval controllability integral is exactly W_d after the
change t=T*s. The identity input has full range, so controllability
holds without any spectral condition. Hence W_d is positive definite;
its principal block, its positive multiple G_d, and the restriction
Gamma_d to three independent coordinates are positive definite.
The source's endpoint equation here is

    M_d^T*W_d+W_d*M_d=exp(T*M_d^T)*exp(T*M_d)-I.              (5)

This is the integral's identity, not an assertion of a unique solution
to an algebraic Lyapunov equation. The spectral-disjointness premise
of Martin Redmann and Patrick Kuerschner, *An H2-Type Error Bound for
Time-Limited Balanced Truncation*, manuscript 2 July 2018,
[Lemma 2.1 and following product-rule remark, pp.5-6](https://pure.mpg.de/rest/items/item_2491617_13/component/file_2630664/content),
is not assumed or needed for (5). No numerical algorithm is imported.

Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
a Polynomial*, Mathematica Balkanica 16 (2002), 203-217,
[Section 3, Lemma 1, pp.211-212](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
bounds the sum of absolute imaginary eigenvalue parts of any complex
square matrix by the trace norm of its Hermitian imaginary part.
Algebraic multiplicities are included. John Watrous, *The Theory of
Quantum Information*, 2018 author version,
[Section 1.1, (1.165)-(1.175), (1.179)-(1.181), pp.32-34](https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf),
supplies the Schatten ideal inequality for compatible rectangular
operators. These results are imported under assessment1947 and the
reused source-notes1947/1523. Their proofs are not repeated. The work
below checks this realification, metric compression, degree scale,
and signed three-column specialization, which the sources do not
evaluate for the actual family.

### Compression and height scale

Let V=G_d^(1/2)*E_d*Gamma_d^(-1/2). Direct multiplication gives
V^*V=I_3 and V^*J_d*V=R_d. Thus ||V||_op=||V^*||_op=1 and
Watrous's ideal inequality at p=1 gives r_d<=k_d.

C028h's companion has characteristic roots alpha=z+b_1, where z
ranges over the roots of P_d with algebraic multiplicity. C_d is
similar to A_d/d, so its roots are alpha/d. The real centering
b_1 does not change imaginary parts, and d>0 divides their absolute
sum by d. G_d^(1/2)*C_d*G_d^(-1/2) is another similarity, with the
same roots. Schmeisser therefore gives H_d/d<=k_d. Neither inequality
requires a uniform bound on the similarities or their inverses.
These two upper comparisons cannot turn a lower bound on r_d into
a lower bound on H_d.

### Endpoint block and the three-dimensional norm

The absolutely convergent matrix power series for exp, cos and sin
give

    exp(t*M_d)=[X(t) -Y(t); Y(t) X(t)].

Consequently the diagonal blocks of exp(t*M_d^T)*exp(t*M_d)
are both X(t)^T*X(t)+Y(t)^T*Y(t). Its upper-right block is
Y(t)^T*X(t)-X(t)^T*Y(t). The upper-right block of the left side
of (5) is T*(C_d^T*G_d-G_d*C_d). Reading the same block on the
right side proves, with its sign fixed,

    G_d*C_d-C_d^T*G_d
        =[X(T)^T*Y(T)-Y(T)^T*X(T)]/T.                      (6)

Since Gamma_d=B/T, one has Gamma_d^(-1/2)=sqrt(T)*B^(-1/2).
Substitution in the definition of R_d cancels both factors of T
and proves the first identity in (2).

For completeness the three-dimensional norm evaluation is finite
algebra, not an imported asymptotic claim. A real skew-symmetric
three by three matrix L has entries determined by
a=(L_23,-L_13,L_12)^T. For a real symmetric B, expansion of the
three by three determinant gives

    det(lambda*B-L)=lambda^3*det(B)+lambda*a^T*B*a.

Dividing by det B is legitimate because B is positive definite.
It follows that B^(-1/2)*L*B^(-1/2) has eigenvalues 0,+i*s,-i*s,
where s=sqrt(a^T*B*a/det B)>=0. Dividing by 2i gives the Hermitian
eigenvalues 0,s/2,-s/2, including the zero case. Their absolute sum
is s. This proves the second identity in (2) with no missing factor
of two, and also proves ||R_d||_1=2*||R_d||_op.

### What the coefficient and energy norm estimates actually give

The subdiagonal of C_d is exactly 1, and its last column is the
reverse of the list -c_(d,k)/d^k, 1<=k<=d. Put

    m_k=sum_(j=0)^k binom(k,j)*b_j*(-b_1)^(k-j).

Since binom(d,k)/d^k<=1/k! and every b_j is positive,

    |c_(d,k)|/d^k
        <= sum_(j=0)^k (b_j/j!)*(b_1^(k-j)/(k-j)!).

Sum over 1<=k<=d and extend the nonnegative sum to all k>=1.
The convergent Cauchy product, or Tonelli for these nonnegative
terms, gives

    sum_(k=1)^d |c_(d,k)|/d^k <= exp(b_1)*F(1)-1=A-1.

F(1) is finite by C028b's entire-series input; b_1>0 gives A>1.
Writing C_d as the unit subdiagonal shift plus its last-column
rank-one matrix proves ||C_d||_op<=1+(A-1)=A. This estimate uses
all coefficients and no numerical moment contracts. Also
||M_d||_op=||C_d||_op<=A, by computing M_d^T*M_d.

Put Z(t)=exp(t*M_d)*[E;0], so H(t)=Z(t)^T*Z(t). For 0<=t<=T,
the semigroup identity and the exponential power-series norm bound
give, for every real v in R^3,

    ||Z(T)*v||^2 <= exp(2*A*(T-t))*||Z(t)*v||^2.

Integrating the reverse inequality in t yields the matrix inequality

    B >= [(1-exp(-2*A*T))/(2*A)]*H(T).                       (7)

All matrices in (7) are real symmetric, so it also holds on complex
vectors. Let q=||B^(-1/2)*H(T)*B^(-1/2)||_op. Equation (7) gives
q<=2*A/(1-exp(-2*A*T)).

For U(T)=X(T)+i*Y(T), the two positive semidefinite matrices
(U(T)*E)^*(U(T)*E) and its complex conjugate are H(T)+i*L and
H(T)-i*L. Hence -H(T)<=i*L<=H(T). After congruence by B^(-1/2),
this bounds ||R_d||_op by q/2. The exact three-dimensional relation
||R_d||_1=2*||R_d||_op now proves r_d<=q and (3).

The denominator in (3) tends to 1 at T=d^2; its numerator stays
2*A>0. Thus this norm-only estimate misses the escape threshold.
It also supplies no lower bound on r_d. Increasing the horizon in
this estimate would not remove its constant numerator; no changed
horizon is tested here. No bounded condition number was hidden in
(7): the unresolved question is the stronger signed ratio in (2).

### Terminal Krylov structure and the remaining signed bound

For the first two columns e_1,e_2 of E (whose ambient indices are
d-2,d-1), one has C_d*e_1=e_2 and C_d*e_2=e_3 exactly. These
columns are not the last column of the companion. Therefore, with
u(t)=U(t)*e_1 and using commutation of U(t) with C_d,

    U(t)*E=[u(t), C_d*u(t), C_d^2*u(t)]
          =[u(t), -i*u'(t), -u''(t)].

For all t, let L(t)=Im((U(t)*E)^*(U(t)*E)); the L in (2) is
L(T). Differentiating the entries, using u'=i*C_d*u, gives

    H_11'(t)=2*Re(i*u(t)^*C_d*u(t))=-2*L_12(t),
    H_12'(t)=Re(-i*||C_d*u(t)||^2
                           +i*u(t)^*C_d^2*u(t))=-L_13(t),
    H_22'(t)=2*Re(i*(C_d*u(t))^*C_d^2*u(t))=-2*L_23(t).

This proves (4). The identities involve full propagated vectors;
they do not replace C_d by a three by three terminal matrix.
They exhibit a more specific unresolved estimate than an unspecified
condition number: at T=d^2, the signed endpoint derivative vector
in (4) must satisfy a^T*B*a=o(det B), or be separated from zero
relative to det B, uniformly as d tends to infinity. The present
coefficient/semigroup bound proves neither. Dropping these signs
and using only endpoint energy gives precisely the inadequate (3).

The continuation may test this signed derivative mechanism at the
same fixed horizon. Any assumption of real roots, bounded inverse
energy, spectral dominance or uniform cancellation would be a new
unproved premise, not a consequence of Gramian positivity. The old
C028h/i/o/p and C029a floors are contrasts only and are not used to
infer a floor for this G_d. No possible complete RH argument is
asserted.

### Integrated signed energies and the remaining Schur residual

This is a second, signed attempt on the same actual family and horizon.
It retains all coefficients; it does not replace the original matrix
by its terminal block. For 0<=j<=3 define

    f_j(t)=C^j*exp(it*C)*e_(d-2),
    <f,g>_T=integral_0^T Re(f(t)^*g(t))dt.

The latter is the real Hilbert-space inner product on these complex
vector-valued functions. In particular B_ij=<f_(i-1),f_(j-1)>_T
for 1<=i,j<=3. All functions are smooth on this finite interval;
f_j'=i*f_(j+1) whenever the latter is used. The product rule gives

    d/dt Im(f_i^*f_j)
        =Re(f_i^*f_(j+1)-f_(i+1)^*f_j).

The initial vectors f_0(0), f_1(0), f_2(0) are the three real
coordinate vectors, so every initial imaginary inner product is zero.
Integration, with these initial endpoints retained, yields exactly

    a_1=<f_1,f_3>_T-B_33,
    a_2=B_23-<f_0,f_3>_T,
    a_3=B_13-B_22.                                         (9)

For example L_12(T)=<f_0,f_2>_T-<f_1,f_1>_T; this agrees
with -H_11'(T)/2 in (4). Likewise L_13(T)=<f_0,f_3>_T-B_23,
whose negative is a_2, and L_23(T)=<f_1,f_3>_T-B_33.
Thus no unsigned replacement or missing initial boundary term enters
the integrated identities.

One can expose precisely where the other companion coordinates enter.
Write q_(d,k)=c_(d,k)/d^k. Since C^2*e_(d-2)=e_d and C commutes
with exp(itC), its complete last column gives

    f_3=-q_(d,2)*f_1-q_(d,3)*f_0+w,
    w(t)=-sum_(k=4)^d q_(d,k)*exp(itC)*e_(d-k+1).            (10)

The sum is empty if d=3; q_(d,1)=0 exactly. Substitution in (9)
therefore gives

    a_1=-q_(d,2)*B_22-q_(d,3)*B_12+<f_1,w>_T-B_33,
    a_2=B_23+q_(d,2)*B_12+q_(d,3)*B_11-<f_0,w>_T.

The coefficients in w are the actual ones, not an error term licensed
for deletion. The coefficient bound proved above bounds their initial
vector norm, but does not bound these propagated signed pairings
relative to the integrated Gram determinant. In particular, the old
diagonal-similarity terminal-block floor cannot be substituted here.

Now write B in blocks as [P z; z^T B_33]. Positive definiteness
implies P>0. Completing the square in (x,1)^T*B*(x,1) shows

    eta=B_33-z^T*P^(-1)*z
       =min_(x in R^2) (x,1)^T*B*(x,1)>0.

The minimum is attained at x=-P^(-1)*z. Eliminating the lower-left
block by a triangular matrix of determinant one gives
det B=det(P)*eta. With a=(a_1,a_2,a_3)^T, a second completion of
the square gives

    a^T*B*a=v^T*P*v+eta*a_3^2,
    v=(a_1,a_2)^T+a_3*P^(-1)*z.

Combining this identity with (2) and (9) proves (8). These are finite
matrix operations on positive matrices, not additional asymptotic
theorems. Geometrically eta is the squared real L2 distance of f_2
from the span of f_0,f_1. No independence of energy-normalized columns
uniform in d is inferred from their independence in each finite d.

There is an absolute coercivity bound, which must not be confused
with the needed relative estimates. For real y in R^3,

    ||exp(itC)*E*y|| >= exp(-A*t)*||y||,

because its inverse exp(-itC) has operator norm at most exp(A*t).
Consequently

    B >= beta*I_3,  P >= beta*I_2,  eta >= beta,
    beta=(1-exp(-2*A*T))/(2*A)>0.

The bound on eta follows from its displayed minimum. In particular
neither det(P) nor eta can tend to zero absolutely along this family:
T=d^2>=9 gives beta>=(1-exp(-18*A))/(2*A). This does not control
their size relative to the growing entries and signed endpoint terms.
For example Cauchy--Schwarz provides only
|B_13-B_22|<=sqrt(B_11*B_33)+B_22, with no small factor after
division by sqrt(det P). Bounding the pairings with w by their
unsigned norms likewise supplies no estimate relative to eta.

The precise sufficient and necessary conditions furnished by (8) for
the proposed escape are the simultaneous limits

    (B_13-B_22)^2/det(P) -> 0,
    v^T*P*v/[det(P)*eta] -> 0.

This equivalence follows just from the two nonnegative summands. It
does not prove either condition. A lower bound on their sum would
instead be needed for the prescribed positive-liminf test. The signed
integration-by-parts attempt establishes neither alternative: it
exposes the propagated fourth-vector pairings and the relative Schur
residual that are still unpaid. Formal positivity, fixed initial
coercivity, or a further rearrangement of (9) cannot be reported as
vanishing normalized cost. No spectrum, conditioning, cancellation,
or actual-Xi sign hypothesis has been added. The full k_d and RH
remain independently unresolved, and this section is not a new
asymptotic discovery or a complete candidate proof.

## Mathlib

Not checked. Full matching coverage for the actual degree-dependent
Gramian, its endpoint compression, and this coefficient bound is
unknown, not claimed absent. The cited finite-horizon, majorization
and Schatten results are mathematical inputs; this file is an informal
finite specialization and has not received a separate critical audit.
