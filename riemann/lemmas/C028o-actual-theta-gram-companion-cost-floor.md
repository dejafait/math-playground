# Corollary C028o: fixed actual-theta Gram companion cost floor

## Hypotheses

Use the full positive kernel K of L019 and the real centered monic
polynomial Q_d and last-column/subdiagonal companion A_d of C028h,
for integers d>=3. In particular, with the fixed actual constant
S_2=b_1^2-b_2>0,

    Q_d(x)=x^d-binom(d,2)*S_2*x^(d-2)+lower-degree terms,

where binom(d,2)=d(d-1)/2.
The coefficient of x^(d-1) is zero. No root-reality hypothesis is made.
Define exactly the following measure and metric, without fitted scales,
finite theta truncations or atomic replacements:

    Z=2*integral_0^infinity K(u)du,
    dmu(u)=K(|u|)du/Z on R,
    G_d=(integral_R (d*u)^(i+j)dmu(u))_(0<=i,j<d),
    G_d=S_d^T*S_d,
    B_d=S_d*A_d*S_d^(-1),
    K_d^theta=||(B_d-B_d^*)/(2i)||_1.

Here S_d is upper triangular with positive diagonal; existence is
verified below. The norm is the Schatten trace norm. Let p_n be the
monic orthogonal polynomials for mu, h_n=integral p_n^2 dmu, and

    beta_n=h_n/h_(n-1)>0 (n>=1),
    T_n=sum_(k=1)^n beta_k.

All these objects are determined by the prescribed full measure.
No bounded recurrence, polynomial density, positive symmetrizer,
individual recurrence asymptotic, diagonalizability or RH is assumed.

## Conclusion

Write p_j^(d)(x)=d^j*p_j(x/d) and expand uniquely

    Q_d(x)=p_d^(d)(x)+sum_(j=0)^(d-1) alpha_(d,j)*p_j^(d)(x).

Then the full cost is exactly

    K_d^theta^2
      =sum_(j=0)^(d-2) d^(2j-2d+2)*h_j/h_(d-1)*alpha_(d,j)^2.  (1)

In particular,

    alpha_(d,d-1)=0,
    alpha_(d,d-2)=d^2*T_(d-1)-binom(d,2)*S_2,
    K_d^theta/d >= |T_(d-1)-(1-1/d)*S_2/2|/sqrt(beta_(d-1)).    (2)

The cumulative recurrence satisfies T_n->infinity, and consequently

    K_d^theta/d -> infinity.                                  (3)

Thus K_d^theta>=d for all sufficiently large d. The onset is not
evaluated. This abandons the fixed metric as an o(d) height-majorant
mechanism. The actual total imaginary root height H_d still satisfies
H_d<=K_d^theta, but (3) gives no lower bound on H_d, no nonreal zero
and no disproof of RH. C028b's H_d=o(d) criterion remains unpaid.
This is a specialization of known orthogonal-polynomial companion
methods, not a claim of a new general matrix theorem. The independent
audit1697 below confirms this fixed-metric stop.

## Proof

### Imported inputs and why a specialization is needed

Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
a Polynomial*, Mathematica Balkanica 16 (2002), 203-217,
[Lemmas 1, 4, 5, pp.211-213, and Theorem 1 proof, pp.213-214](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
supplies the Jacobi-plus-last-column representation for a monic real
polynomial expanded in monic orthogonal polynomials of a positive
measure with infinite support and all moments. If f=p_d+sum a_j*p_j,
its correction entries are -sqrt(h_j/h_(d-1))*a_j. The real-polynomial
case c=kappa=0 in the Theorem 1 proof identifies the Hermitian
imaginary part's two possible nonzero eigenvalues as +/-I/2, where

    I^2=sum_(j=0)^(d-2) h_j*a_j^2/h_(d-1).

Its trace norm is I. Lemma 1 bounds total absolute imaginary eigenvalue
parts by that trace norm, including algebraic multiplicities.
The measure need not have bounded support. These general matrix
results are imported; their proofs are not repeated here.

NIST [DLMF 18.2(iv), equations 18.2.11_4-18.2.11_8, and
18.2.21](https://dlmf.nist.gov/18.2), accessed in source review1694,
supplies the monic three-term recurrence, beta_n=h_n/h_(n-1),
and even-measure parity. Here parity makes the diagonal recurrence
coefficient zero. Only these finite orthogonality facts are used.
No unbounded Favard construction or moment-determinacy theorem is
needed, because the measure is supplied explicitly.

Assessment1694 covers these results and this exact fixed-metric test.
The necessary specialization identifies the Cholesky orientation,
the full norm rather than a characteristic polynomial alone, and the
quadratic coefficient at scale d. The final finite-moment argument
below justifies the support implication without assuming that bounded
Jacobi data identify an arbitrary unbounded measure by uniqueness.

### Measure, positive Gram and orthogonal-polynomial coordinates

L019 gives K(u)>0 for all u>=0 and integrable superexponential
domination. Hence 0<Z<infinity and mu is an even probability measure,
has every absolute moment finite, and has positive mass on every
nonempty real interval. In particular its support is unbounded.
For every nonzero polynomial q, its finitely many real roots have
Lebesgue measure zero; thus integral |q|^2 dmu>0. The same applies
after scaling u by d>0. This proves that all finite Gram matrices
are strictly positive definite, so the Cholesky factorization theorem
gives an invertible S_d with positive diagonal.
It also proves h_n>0 and permits Gram-Schmidt in every degree.

Let nu_d be the image of mu under u->d*u. Then G_d is its monomial
Gram matrix. The scaled polynomials p_j^(d) are monic and orthogonal
for nu_d, with squared norms

    h_j^(d)=d^(2j)*h_j.                                      (4)

Use column coefficient vectors in the ordered monomials
1,x,...,x^(d-1). A vector c has norm squared c^*G_d*c=||S_d*c||_2^2.
The columns of the upper triangular S_d^(-1) are mutually
orthonormal polynomials: their Gram matrix is
(S_d^(-1))^T*G_d*S_d^(-1)=I. Column j has degree j and positive
leading coefficient. By uniqueness in Gram-Schmidt it is precisely

    q_j^(d)=p_j^(d)/sqrt(h_j^(d)), 0<=j<d.

Thus the orthonormal coordinate vector of a polynomial with monomial
coefficient vector c is z=S_d*c, not S_d^(-1)*c. The quotient
multiplication map q->x*q mod Q_d has monomial matrix exactly A_d:
its first d-1 columns shift x^j to x^(j+1), and its last column is
the coefficient vector of x^d-Q_d. Consequently its orthonormal
matrix is precisely B_d=S_d*A_d*S_d^(-1). No transpose, merely
isospectral representation or arbitrary similarity norm invariance
is substituted at this step.

### Identification of the full cost

Evenness gives p_n(-u)=(-1)^n*p_n(u). The imported recurrence is

    u*p_n(u)=p_(n+1)(u)+beta_n*p_(n-1)(u), n>=1,
    p_0=1, p_1=u.

In the scaled orthonormal basis the internal off-diagonal entries
are d*sqrt(beta_j), j=1,...,d-1. Let J_d be this real symmetric
tridiagonal matrix with zero diagonal. Multiplication on the last
basis polynomial before reduction has its extra term
p_d^(d)/sqrt(h_(d-1)^(d)). Reduction modulo Q_d replaces that term
by -sum alpha_(d,j)*p_j^(d)/sqrt(h_(d-1)^(d)). Thus the same B_d is

    B_d=J_d-v_d*e_(d-1)^T,
    (v_d)_j=alpha_(d,j)*sqrt(h_j^(d)/h_(d-1)^(d)), 0<=j<d.

Here e_(d-1) is the final coordinate vector, using indices 0,...,d-1.
Both Q_d and p_d^(d) have zero coefficient at x^(d-1), so
alpha_(d,d-1)=0 and v_d is perpendicular to e_(d-1). This is the
actual matrix representation to which the imported Schmeisser cost
applies. Its Hermitian imaginary part has eigenvalues
+/-||v_d||_2/2 and zeros (all zero if v_d=0), so its trace norm is
||v_d||_2. Substituting (4) proves the complete identity (1).
It also verifies H_d<=K_d^theta by the imported majorization:
the companion's roots are those of Q_d; the real translation and
positive normalization in C028h preserve the imaginary-root statistic.
No reality of any actual Q_d roots enters this reasoning.

### Quadratic residual with all scale factors

Induction in the monic recurrence shows, for n>=2,

    p_n(u)=u^n-T_(n-1)*u^(n-2)+terms of degree at most n-3.       (5)

The base case is p_2=u^2-beta_1. For the induction step subtracting
beta_n*p_(n-1) from u*p_n adds -beta_n to the indicated next
coefficient. Parity supplies the missing degree n-1 term in every
degree. Thus p_d^(d) has coefficient -d^2*T_(d-1) at x^(d-2).
Since alpha_(d,d-1)=0, comparison with C028h's exact coefficient
-binom(d,2)*S_2 gives the second identity in (2).

Retain j=d-2 in the nonnegative sum (1). Its square-root norm ratio is

    sqrt(h_(d-2)^(d)/h_(d-1)^(d))
      =1/(d*sqrt(beta_(d-1))).

Consequently K_d^theta>=|alpha_(d,d-2)|/(d*sqrt(beta_(d-1))).
Division by d proves (2), including the factor (1-1/d)/2.
Only this one residual is needed for the floor; no upper bound on
the full cost is inferred from retaining it.

### Finite-moment exclusion of bounded cumulative recurrence

Suppose for a contradiction that the increasing T_n are bounded.
There is then a finite M>0 such that beta_n<=M for all n>=1.
Put q_n=p_n/sqrt(h_n). The same recurrence gives

    u*q_n=sqrt(beta_(n+1))*q_(n+1)+sqrt(beta_n)*q_(n-1),

with the second term absent for n=0. For a polynomial f=sum t_n*q_n
the two resulting finite coefficient sequences each have l^2 norm
at most sqrt(M)*(sum |t_n|^2)^(1/2). The triangle inequality and
orthonormality therefore imply

    ||u*f||_(L^2(mu))<=2*sqrt(M)*||f||_(L^2(mu)).               (6)

All sums are finite and all norms finite; there is no density or
closed-operator assertion. Starting with f=1 and successively using
f=u^k in (6) yields

    integral |u|^(2k)dmu <= (4M)^k, k>=0.

Choose R>2*sqrt(M). Unbounded support with a positive density gives
epsilon=mu({|u|>=R})>0. The same integral is at least
epsilon*R^(2k). Hence epsilon<=(4M/R^2)^k for every k, which is
impossible as k->infinity. The increasing T_n are therefore unbounded,
so T_n->infinity. No individual beta_n asymptotic or uniqueness of
the unbounded moment problem has been assumed.

### Threshold and method-specific stop

Let C=S_2/2>0 and put T=T_(d-1). For sufficiently large d, T>C,
and beta_(d-1)<=T gives from (2)

    K_d^theta/d >= (T-C)/sqrt(T) -> infinity.

Indeed T-(1-1/d)*C>=T-C>0, and replacing sqrt(beta_(d-1)) by
sqrt(T) only decreases this nonnegative lower bound. For an explicit
eventual test, whenever T_(d-1)>=max{S_2,4}, the right side is at
least sqrt(T)/2>=1. Such a fixed finite onset exists by the preceding
argument, although its value is not computed. This proves (3) and
the requested positive linear floor.

The required payment was K_d^theta=o(d); instead its ratio to d
diverges. This is decisive for exactly the prescribed measure,
Cholesky factor and scale d. No claim about other metrics, changed
scales or actual lower root heights follows. In particular an upper
majorant's divergence cannot be reversed to contradict the RH-equivalent
criterion of C028b. The metric floors in C028a/c/h/i and the failed
reference-root assumptions in stops551/571 are comparisons; those
floors are not additional premises. C028h is used for its actual
polynomial, companion convention and established coefficient only.

### Independent proof audit1697 — 19 November 2026

This audit uses the separately approved assessment1695 and the inspected
Schmeisser/DLMF interfaces recorded in source-notes1694. It confirms
the proof above without changing its hypotheses or extending its scope.
The essential local inputs are L019's full positive kernel and decay,
C028h's actual centered polynomial and companion convention, and
C028b for the downstream height criterion. The other metric stops are
comparisons only. No source refresh or new general theorem is needed.

For clarity, let E=S_d^(-1). Then E^T*G_d*E=I, column j of E has
degree j and positive leading coefficient, and E*z is the monomial
coefficient vector of the polynomial with orthonormal coordinates z.
Thus multiplying and reducing gives z'=S_d*A_d*E*z. This checks the
actual metric, rather than only the eigenvalues of a comrade matrix.
Orthogonality fixes that column as p_j^(d)/sqrt(h_j^(d)); positivity
of G_d follows because the density is positive and a nonzero polynomial
has only finitely many real zeros. Every required moment is finite by
L019's domination, so this argument applies in every finite degree.

The normalized recurrence at internal column j gives the two entries
d*sqrt(beta_j) and d*sqrt(beta_(j+1)), when present. At column d-1,
the row d-2 entry is d*sqrt(beta_(d-1)); the remaining term before
reduction is p_d^(d)/sqrt(h_(d-1)^(d)). Substitution of Q_d=0 gives
exactly -v_d in that last column. These computations check all columns
of B_d=J_d-v_d*e_(d-1)^T, including d=3. The degree d-1 coefficient
vanishes, so v_d is real and perpendicular to e_(d-1). Writing r=||v_d||,
when r>0 the Hermitian imaginary part on the orthonormal pair
(v_d/r,e_(d-1)) is

    [ 0  i*r/2; -i*r/2  0 ].

Its eigenvalues are r/2 and -r/2 and it is zero on the perpendicular
complement. If r=0 the whole matrix is zero. Therefore the full trace
norm is r in both cases, with no missing factor two. Equation (4)
gives h_j^(d)/h_(d-1)^(d)=d^(2j-2d+2)*h_j/h_(d-1), proving (1)
for every residual, not merely the retained quadratic one.

In the monic recurrence the coefficient of u^(n-2) is
-sum_(k=1)^(n-1) beta_k. Scaling multiplies this coefficient by d^2,
while the prescribed Q_d coefficient is -d(d-1)*S_2/2. Hence the
quadratic residual is d^2*T_(d-1)-d(d-1)*S_2/2. Its normalized norm
factor is 1/(d*sqrt(beta_(d-1))). Dividing its cost contribution by d
gives exactly (2). All other terms in (1) are nonnegative; dropping
them is only a lower estimate for the full cost.

If T_n were bounded, choose one finite M>0 bounding every beta_n.
On finite orthonormal coefficient sequences the upward and downward
weighted shifts separately have norm at most sqrt(M). Their sum
therefore proves (6), even though their images can overlap. Repeated
application to 1,u,...,u^(k-1) gives the same bound (4M)^k for every
even moment; h_0=1 because mu is a probability measure. For any fixed
R>2*sqrt(M), positivity on (R,R+1) gives a fixed positive tail mass
epsilon, independent of k. The inequality epsilon<=(4M/R^2)^k for
all k contradicts that positivity. This checks the limit argument
without polynomial density, operator closure, or moment uniqueness.

Thus T_n increases to infinity along all integers. Once T=T_(d-1)>C,
C=S_2/2, the numerator in (2) is positive and at least T-C, while
0<beta_(d-1)<=T. This verifies the direction of both inequalities in
the lower bound (T-C)/sqrt(T). For T>=max{S_2,4} it is at least one;
as T tends to infinity it diverges. The threshold is existential,
not effective, and holds for all sufficiently large integer d.

Verdict: the full identity, quadratic scaling and finite-moment
contradiction pass. The known matrix method has a valid local
specialization stopping this prescribed metric. The audit establishes
no result beyond the stated specialization and no bound H_d=o(d).
In particular H_d<=K_d^theta cannot be reversed; a divergent upper
majorant supplies neither a nonreal root nor an RH conclusion.

## Mathlib

Not checked. Full matching coverage of this fixed actual-theta Gram
similarity, its exact cost and the support-based degree floor is unknown.
The cited recurrence and matrix inputs are imported with their stated
hypotheses; the local scaling and finite-moment specialization are
proved here. No formal verification or absence from Mathlib is claimed.
