# Corollary C030s: a multiplicity-weighted subdiagonal phase bound

## Hypotheses

Use the finite family and actual derivative-Hankel determinants of
C030r. Thus m>=1, n>=2m, 2<=d<=floor(n/2), a_l,r>0, b_l real,
x>0, A=sum_l |b_l|, M=sum_l b_l^2, and x*A<=1/4. The rates are

    (a_1+i*b_1,a_1-i*b_1,...,a_m+i*b_m,a_m-i*b_m,r,...,r).

Set D_0=diag(a_1,a_1,...,a_m,a_m,r,...,r) and
B=diag(b_1,-b_1,...,b_m,-b_m,0,...,0), so the complex rate matrix
is D_0+i*B. Here D_0 is a rate matrix; the scalar D_(k,b) below is
C030r's signed Hankel determinant. The reference b=0 retains every
real rate, n,m,r and x. Define, for 1<=i<d,

    beta_(i,b)=sqrt(D_(i+1,b)*D_(i-1,b))/D_(i,b),
    beta_(i,0)=sqrt(D_(i+1,0)*D_(i-1,0))/D_(i,0).

Partition the coordinate set by equal diagonal entries of D_0. For
each resulting real-rate class E let g_E be its size and set

    M_E=sum_(l:a_l is the rate of E) b_l^2.

Any background entries with that same rate belong to E too. Classes
with M_E=0 are omitted from subsequent sums. An included class has
g_E>=2, its phase block B_E has trace zero, and tr(B_E^2)=2*M_E.
In particular sum_E M_E=M. Put

    T=sum_(E:M_E>0) M_E*g_E/(g_E^2-1),
    epsilon=x^2*T/4.

Empty sums are zero. No separation between distinct real rates, bound
on their contrasts, or independence of compressed orbital blocks is
assumed. Repeated rates, vanishing phases, n=2m and the closed phase
boundary are included.

## Conclusion

The following estimates hold throughout this family:

    0<=epsilon<=x^2*M/6<=1/96,
    |beta_(i,b)-beta_(i,0)|
       <= beta_(i,0)*epsilon/(1-epsilon)
       <= (24/95)*x*sqrt(i*(n-i))*T
       <= (16/95)*x*n*sum_E M_E/g_E.                 (1)

Consequently, for any fixed 0<rho<=1, the additional hypothesis

    g_E>=rho*n for every class with M_E>0            (2)

gives the absolute bound

    |beta_(i,b)-beta_(i,0)| <= (16/(95*rho))*x*M.     (3)

The constant in (3) is independent of n,d,m, the phases, x and all
real-rate contrasts, with rho fixed. In particular 16/95 suffices
when every real rate is equal. If all a_l=a and 2m>=rho*n, (3) holds
for every positive a,r, whether or not a=r. Background multiplicity
can only enlarge the active class when a=r.

This is a partial answer to the full uniform target of assessment1228,
obtained in bounded attempt1230. It is a source-based specialization
(REPRODUCTION), not a claim of mathematical novelty beyond the cited
Haar-moment and determinant machinery. Independent audit is pending.
When phases occupy many distinct classes of size two, (1) still has
an n factor; (3) does not prove the unrestricted target. No unbounded
normalized-difference family, shift norm, actual-Xi transfer, all-degree
positivity or RH candidate is asserted.

## Proof

### Imported identities and their precise uses

C030r supplies the determinant identity, positivity and actual beta
interface. Its real-rate determinant input is S. Sra, *On some
positivity properties of the Riemann Xi function*,
[author-v3, 2 November 2026](https://suvrit.github.io/papers/riem-xi/riem-xi-v3.pdf),
Lemma C.6/(C.10), pp23-25. The real variance calculation and recurrence
comparison are in C.5/(C.9), pp22-23, and C.9/(C.18)-(C.23), pp27-28,
as inspected in assessment1228/review1229. We use the real coefficient
bound only; C.9's additional shift-norm hypotheses and conclusion are
not imported. The short determinant sign check below states exactly
why the needed coefficient bound has the present scope.

For orientation averaging use the degree-two identity already
specialized in C030o's proof, (3)-(6). Its source is B. Collins and
P. Sniady, *Integration with respect to the Haar measure on unitary,
orthogonal and symplectic group*,
[arXiv math-ph/0402073v1, 26 February 2004](https://arxiv.org/pdf/math-ph/0402073v1),
Corollary 2.4/(11)-(12), p5, with (9)-(10), pp4-5, and Proposition 2.5,
p6; these passages were inspected in coverage1213. For probability
Haar W in U(g), g>=2, and a traceless real diagonal B_* the contraction is

    E_W tr(B_* W C W*)=0,
    E_W tr(B_* W C W*)^2
       =tr(B_*^2)/(g^2-1)
                        *[tr(C^2)-tr(C)^2/g]        (4)

for every Hermitian C. Diagonalize C by unitary invariance to apply
C030o's displayed calculation. The calculation uses only trace zero,
the squared trace and g>=2; its main theorem's restriction g=2m is not
needed for (4). Thus extra zero phase entries and odd g cause no change.
The first identity follows also by E_W W C W*=tr(C)*I/g. This imports
the known finite Haar contraction, without rederiving integration theory.

### The known real-reference coefficient bound with its sign checked

For any smooth f write tau_k=det[f^(u+v)]_(0<=u,v<k), tau_0=1.
The Desnanot--Jacobi determinant identity gives

    tau_i*tau_i''-(tau_i')^2=tau_(i+1)*tau_(i-1).   (5)

Here is the differentiation check needed for its use. In the derivative
of tau_i by rows, all but the last row give a repeated row. Hence tau_i'
has row indices 0,...,i-2,i and column indices 0,...,i-1. Differentiate
this determinant by columns: again only the last column survives, so
tau_i'' has both index sets 0,...,i-2,i. These are the four minors of
the size i+1 Hankel matrix in the Desnanot--Jacobi identity obtained by
deleting either of its last two rows and columns. The two mixed minors
equal tau_i' by symmetry. For i=1, (5) is directly
f*f''-(f')^2=tau_2. All derivatives exist by C030r's finite-convolution
formula and compact domination.

For C030r's D_(k,0)=(-1)^(k*(k-1)/2)*tau_k, the adjacent signs on the
right side of (5) multiply to -1. Since these D are positive,

    (log D_(i,0))''=-beta_(i,0)^2.                  (6)

C030r(2) expresses D_(i,0) as a positive constant independent of x
times x^(i*(n-i))*Z_(i,0)(x). The latter orbital integral has the
positive real weight exp(-x*L), L=tr(D_0*Q), Q=V P_i V*. For fixed
finite real rates, L is bounded on the compact unitary group.
Differentiation twice under that integral therefore gives
(log Z_(i,0))''=Var_(i,0,x)(L)>=0. Combining this with (6) yields

    0<beta_(i,0)^2
       =i*(n-i)/x^2-Var_(i,0,x)(L)
       <=i*(n-i)/x^2.                              (7)

This is the cited standard real-rate variance estimate, with its signs
and required sizes checked for the actual determinants. It is not a
variance assertion for the complex-weight law and is not presented as
a new lemma or discovery. It imposes no extra rate-spread or degree
hypothesis. In particular i+1<=d<=floor(n/2) is within C030r's sizes.

### Averaging within each equal-real-rate class

Fix a rank k in {0,...,n}. Let E_(k,0,x) denote expectation under its
own probability law proportional to exp(-x*tr(D_0*Q))dV. Put

    F_k=Z_(k,b)(x)/Z_(k,0)(x)
       =E_(k,0,x) exp(-i*x*tr(B*Q)).                 (8)

Conjugation by the simultaneous coordinate swaps in each conjugate
pair preserves D_0 and changes B to -B. Thus F_k is real and equals
E_(k,0,x) cos(x*tr(B*Q)), in particular F_k<=1.

This real tilted law is invariant under every block diagonal unitary
W whose blocks W_E act inside the real-rate classes. Indeed W commutes
with D_0, and Haar invariance preserves the untilted orbital measure.
Take these W_E independently with probability Haar measure, independently
of Q. This is an auxiliary averaging operation; it makes no assertion
that the actual compressions of Q are independent.

For fixed Q let C_E=Q|_E be its principal compression and
R_E(W_E)=tr(B_E W_E C_E W_E*). We have 0<=C_E<=I. Conditional on this
fixed Q, (4) gives E_W R_E=0 and

    E_W R_E^2
       =2*M_E/(g_E^2-1)
                       *[tr(C_E^2)-tr(C_E)^2/g_E]
       <=M_E*g_E/(2*(g_E^2-1)).                    (9)

For the inequality, if s=tr(C_E), its eigenvalues are in [0,1], so
tr(C_E^2)-s^2/g_E<=s-s^2/g_E<=g_E/4, exactly C030o's cube estimate.
The independent auxiliary W_E and their zero means make all cross
terms E_W R_E R_H vanish for E!=H, for each fixed Q. Blocks with zero
phase contribute zero. After integrating Q and using invariance,

    E_(k,0,x) tr(B*Q)^2 <= T/2.                     (10)

All quantities are bounded in these finite integrals, so the iterated
integrations and finite sums are justified. No conditional density for
corner eigenvalues, strict spectra or common normalizer across ranks
has been used.

The inequality cos u>=1-u^2/2, (8) and (10) now imply for every rank

    1-epsilon<=F_k<=1.                             (11)

For g>=2, g/(g^2-1)<=2/3: equivalently
2g^2-3g-2=(2g+1)*(g-2)>=0. Hence T<=2M/3 and
epsilon<=x^2*M/6<=1/96, using M<=A^2 and x*A<=1/4.
This proves a strict floor at the closed boundary as well.

### The determinant ratio and absolute comparison

In C030r's determinant formula, the product of rates contributes R_b^k
at size k. Its exponent in D_(i+1,b)*D_(i-1,b)/D_(i,b)^2 is zero.
The remaining factorial and x factors are identical in the b and 0
references. Consequently, with positive square roots throughout,

    beta_(i,b)/beta_(i,0)=sqrt(F_(i+1)*F_(i-1))/F_i. (12)

This keeps all three orbital normalizers separate. By (11), both
sqrt(F_(i+1)*F_(i-1)) and F_i lie in [1-epsilon,1]. Their difference
has absolute value at most epsilon, so (12) gives

    |beta_(i,b)-beta_(i,0)|
       <= beta_(i,0)*epsilon/(1-epsilon)
       <= (24/95)*x*sqrt(i*(n-i))*T.                (13)

The last step uses (7), epsilon=x^2*T/4 and
1/(1-epsilon)<=96/95. Finally g/(g^2-1)<=4/(3g) for g>=2, since
g^2/(g^2-1)<=4/3, and sqrt(i*(n-i))<=n/2. These give the last
inequality in (1). Under (2), sum_E M_E/g_E<=M/(rho*n), giving (3).

If M=0, all phases vanish and both sides of (1) are zero, without
division by M or any class size in an empty sum. When n=2m there is
no background block; the same class partition and averaging apply.
Coincident a_l are put in the same class, including coincidences with
r when that rate occurs. Rank endpoints, if used in (12), have F_0=F_n=1.
All arguments are pointwise on the closed phase window, so no extension
of a complex positivity claim or interchange of dimension and limit is
needed. These observations cover the declared degeneracies.

### The remaining obstruction

For many distinct active real parts with g_E=2,
n*sum_E M_E/g_E=n*M/2. Thus the last bound in (1) becomes
(8n/95)*x*M and does not give an absolute constant. This is a limitation
of the rankwise variance envelope followed by (7), not an admissible
counterexample: it proves no lower bound on the actual difference.
Sharper rank dependence or a relation between compressed variances and
the local real beta could remove this loss, but neither is established
here. No lower bound on beta_(i,0) is assumed. Actual-Xi supply, finite
evolution norms and signed-complement payment remain separate even
within the subfamily (2).

## Mathlib

Full matching coverage of (1)-(3), the unitary degree-two contraction
and this multiplicity specialization is unchecked; no absence claim is
made. Finite determinant identities, Haar invariance, variance positivity
for a real probability law and elementary quadratic inequalities are
supporting mathematics. Exact matching Mathlib theorem names were not
checked, and no formal verification is claimed.
[Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
