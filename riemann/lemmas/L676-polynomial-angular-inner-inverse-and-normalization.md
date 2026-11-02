# Lemma 676: an exact inner-factor polynomial inverse and inexpensive normalization

## Hypotheses

Use the complete product, normalized circle measure and action convention
of L675. Explicitly, q>=1 is an integer, n=12q+3, J=n-1,
x=-5/4, R=11/8, U=R^2, t_j=j/n, and

    B_u(a)=product_(0<=j<n) R*(a-t_j*u)/(U-t_j*a/u),
    W_a(u)=B_u(x)/B_u(a),
    A(a)=mean_u conjugate(psi(u))*W_a(u), |a|>J/n.

Use the rational continuation at removable singularities. Retain j=0
and the denominator angle 1/u. Put

    s_j=t_j/R, lambda=R/x=-11/10, r=10/11,
    b(v)=product_(j=1)^J (v-s_j)/(1-s_j*v)=sum beta_k*v^k,
    F(u)=b(lambda*u),
    alpha_j=s_j/lambda=t_j*x/U, gamma_j=lambda*s_j=t_j/x,
    B(u)=product_(j=1)^J (u-alpha_j)/(1-alpha_j*u)=sum b_k*u^k,
    E(u)=product_(j=1)^J (1-alpha_j*u)/(1-gamma_j*u), Q(u)=1/E(u).

The symbol B here is an angular finite Blaschke product, distinct from
B_u(a). All beta_k, b_k and coefficients of E,Q are real. Nonvanishing
of higher beta_k is not assumed. In this proof H2 denotes the subspace
of normalized circle L2 with no negative Fourier coefficients; only
Fourier orthogonality and multiplication by the displayed rational
functions will be used. Write coeff_(u^m)(G) for the coefficient of u^m
in the Taylor series of G.

## Conclusion

For every real polynomial h(u)=sum_(l=0)^J h_l*u^l, the explicit inverse

    conjugate(psi_h(u))=u^(-J)*B(u)*h(u)                         (1)

has exact norm and full exterior-domain action

    ||psi_h||_2^2=sum_(l=0)^J h_l^2,
    A_h(a)=P_h(x/a),
    P_h(w)=sum_(k=0)^J lambda^(k-J)*beta_k*
                         coeff_(u^(J-k))(Q(u)*h(u))*w^(k+1).          (2)

Thus P_h is real, has degree at most n and vanishes at zero. Formula
(2) includes every coefficient and permits zero beta_k. These inverses
cover every real polynomial action allowed by L675's range criterion.

Within the subclass in which f=conjugate(psi)/F has all moments
mean(f*u^k)=0 for k>J, allowing additional Fourier modes cannot improve
on the least-norm h of degree at most J giving the chosen P. Formula
(1) and its Euclidean norm are exact for this subclass. This is NOT a
claim of minimal norm among all possible angular inverses: an inverse
may have nonzero such moments where beta_k=0.

There is a uniform inexpensive normalization. With

    K=sum_(k=0)^J b_k^2, h_l=b_(J-l)/K,

one has

    K>=1/n, P_h(1)=1, ||psi_h||_2=1/sqrt(K)<=sqrt(n).           (3)

No prescribed zero at r or segment sign is asserted for (3). For all
sufficiently large allowed n, L675 implies that this construction has
degree greater than 3n/7. Hence its low cost is a higher-degree result;
the earlier low-degree obstruction is unchanged.

The prescribed zero can also be imposed exactly in these coordinates.
Define real vectors indexed by 0<=l<=J,

    v_l=b_(J-l),
    z_l=r*lambda^(-J)*coeff_(u^(J-l))(Q(u)*b(-u)),
    a=v.v=K, b0=z.z, c=v.z, Delta=a-c^2/b0.

Then b0>0 and Delta>0. The least squared norm in subclass (1) subject
to P_h(1)=1 and P_h(r)=0 is exactly

    h_*=(v-(c/b0)*z)/Delta, ||psi_(h_*)||_2^2=1/Delta.          (4)

This does not supply a uniform lower bound on Delta. Nor does minimizing
these two value constraints enforce signs. For n=15 the exact h_* in
(4) violates the required segment sign at y=1/10:

    -17/500 < Re P_(h_*)(x/(x+i/10)) < -33/1000 < 0.           (5)

The finite failure in (5) is not an asymptotic obstruction: the saved
target allows a later onset and different h. The full target remains
simultaneous P_h(r)=0, signs on every |y|<=9/20 and a uniform
exp(n/100)*n^C norm. The useful advance is the exact unweighted inverse
coordinate system and (3), not a positive-cone lower bound. Original
unit-residue H, support, Xi realization and mixed positivity remain
open. This lemma has not received a separate critical audit.

## Proof

### 1. Scope and standard input

Reuse the prior EXPLORE assessment
`drafts/literature/2026-11-02-inverse-parameter-polynomial-separator.md`.
Its approved difference includes complete rational/Fourier coefficient
analysis for this exact polynomial action and its paid inverse. No
source scope has been changed and no new literature conclusion is
asserted. L675 supplies the exact product identity, coefficient range,
nonzero beta_0,beta_1 and the low-degree cost obstruction. L674's
open-domain positivity obstruction is a comparison, not a premise;
no open-domain positivity is assumed here.

Import normalized scalar Fourier orthogonality and Parseval from
A. Levitt, *Analyse de Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and
Theorem 1.11/Corollary 1.12, printed pp.6,8 (PDF pp.12,14), with
the completeness proof on printed p.53. This is the already inspected
source in the reused assessment. Dividing angular measure by 2*pi
makes the monomials orthonormal. No general inner/outer factorization,
range-factorization or transform-isometry theorem is assumed or
reproved. The particular rational factorization below is necessary
to compute the exact cost for this product.

### 2. Exact factorization and full action

Directly from the finite products,

    F(u)=lambda^J*B(u)*E(u).                                 (6)

Indeed lambda*u-s_j=lambda*(u-alpha_j) and
1-s_j*lambda*u=1-gamma_j*u. Moreover

    |alpha_j|<80/121<1, |gamma_j|<4/5<1.

Consequently E and Q have no zero or pole on the closed unit disk
and are bounded there, for each n. Their power series converge on
a disk of radius greater than one. No bound on those multipliers
uniform in n is being asserted or used to estimate (1).

For |u|=1 each factor of B has modulus one, since alpha_j is real
and |u-alpha_j|=|1-alpha_j*u|. Thus (1) has norm ||h||_2, which
is the Euclidean coefficient norm in (2). By (6),

    f_h(u)=conjugate(psi_h(u))/F(u)
           =lambda^(-J)*u^(-J)*Q(u)*h(u).                     (7)

L675's full product formula, including j=0, is

    W_a(u)=w*b(lambda*u*w)/F(u), w=x/a.

The Taylor series for b(lambda*u*w) converges uniformly in u on each
compact subdisk of |w|<|x|/(J/n). This is precisely the full exterior
parameter domain after inversion. Since f_h is in L2 and hence L1,
termwise integration gives

    A_h(x/w)=w*sum_(k>=0) beta_k*lambda^k*w^k*mean(f_h*u^k).

Equation (7) has Fourier modes only at indices >=-J. Its kth required
moment is lambda^(-J)*coeff_(u^(J-k))(Q*h) for 0<=k<=J, and is zero
for k>J. This proves (2) throughout the stated domain, including the
analytic extension at w=0. It does not fit finitely many parameter
values or discard any angular poles.

### 3. Range coverage and the qualified norm minimization

The constant coefficient of Q is one. Therefore the map from
(h_0,...,h_J) to the first J+1 coefficients of Q*h is an invertible
real triangular linear map. For a feasible polynomial P, prescribe

    coeff_(u^(J-k))(Q*h)=p_(k+1)/(lambda^(k-J)*beta_k)

only where beta_k is nonzero; choose these coefficients arbitrarily
where beta_k=0. L675's criterion requires p_(k+1)=0 in the latter
case. Triangular inversion now gives a real polynomial h of degree
at most J realizing P. No nonzero higher coefficient is assumed.

For the norm qualification, let any inverse in the stated subclass
be given and put f=conjugate(psi)/F. Its moment conditions say exactly
that g=u^J*f belongs to H2. Multiplication by E and Q preserves this
Fourier subspace: their Taylor series are absolutely summable on the
circle. Set h=lambda^J*E*g. Equation (6) gives

    conjugate(psi)=u^(-J)*B*h.

Hence ||psi||_2=||h||_2 even for this general h. Its moments determining
the polynomial use only h_0,...,h_J. Truncating h to those coefficients
leaves the entire action unchanged and weakly decreases the norm by
Parseval. Subsequent minimization is therefore a finite Euclidean
problem. This establishes precisely the stated subclass result. When
some beta_k with k>J vanishes, polynomial action equality alone need
not impose the subclass moment condition; such extra inverses have
not been excluded or assigned a norm here.

### 4. A uniform polynomial bound for normalization

At w=1, equation (6) implies Q(u)*b(lambda*u)=lambda^J*B(u).
The coefficient formula consequently gives

    P_h(1)=coeff_(u^J)(B*h)=sum_(l=0)^J b_(J-l)*h_l.                (8)

We need a quantitative lower bound on K. The rational B is analytic
on a disk of radius greater than one, so its Taylor series and its
derivative converge uniformly on the circle. Its modulus is one there.
Orthogonality yields both

    sum_(k>=0) b_k^2=1,
    mean(conjugate(B(u))*u*B'(u))=sum_(k>=0) k*b_k^2.         (9)

To evaluate the second mean, direct differentiation of the finite
product, and |B|=1, give on the circle

    conjugate(B(u))*u*B'(u)
       =sum_(j=1)^J (1-alpha_j^2)/|u-alpha_j|^2.

Each summand has mean one. For example the absolutely convergent
geometric expansion for |alpha_j|<1 gives
1+2*sum_(k>=1) alpha_j^k*cos(k*theta), whose constant coefficient
is one. Thus the second sum in (9) is J. In particular,

    J >= (J+1)*sum_(k>=J+1) b_k^2=(J+1)*(1-K),

so K>=1/(J+1)=1/n. Taking h_l=b_(J-l)/K in (8) proves (3).
For fixed n this is also the least-norm normalization within the
subclass, by the ordinary vector Cauchy--Schwarz inequality.

It has P_h(0)=0 and degree at most n by (2), without a condition on
beta_J. Since sqrt(n)<=exp(n/100)*n^(1/2), the norm requirement alone
is paid with an absolute polynomial factor. If this family had degree
at most 3n/7 for arbitrarily large n, L675's lower bound
(1254/1495)*exp((1503/97790)*n) would contradict sqrt(n). The ratio
of that bound to sqrt(n) tends to infinity. This justifies the stated
eventual higher-degree qualification, without presuming the degree
is exactly n at every finite n.

### 5. The additional prescribed zero and its remaining cost

At w=r, lambda*r=-1. Formula (2) gives

    P_h(r)=r*lambda^(-J)*coeff_(u^J)(Q*b(-u)*h)=z.h.               (10)

Together (8) and (10) give the two stated vector constraints. The
vectors v and z are independent. To see this without a numerical
rank assumption, let Q_1=[u]Q. Their last two coordinates are

    v_J=lambda^(-J)*beta_0,
    z_J=r*lambda^(-J)*beta_0,
    v_(J-1)=lambda^(-J)*(beta_0*Q_1+lambda*beta_1),
    z_(J-1)=r*lambda^(-J)*(beta_0*Q_1+lambda*r*beta_1).

L675 proves beta_0>0 and beta_1<0 for every allowed n. If z were a
multiple of v, the last coordinate would force the multiple to be r.
The next coordinate would then force lambda*(r-1)*beta_1=0, which
is false. Thus b0>0 and Delta>0 by strict vector Cauchy--Schwarz.

The vector v-(c/b0)*z is orthogonal to z, has squared norm Delta,
and has dot product Delta with v. This proves feasibility and the
norm in (4). Every other real h satisfying the two constraints differs
from h_* by a vector orthogonal to v and z, and hence to h_*.
Its squared norm is 1/Delta plus that vector's squared norm. Adding
the previously discarded higher Fourier coefficients cannot lower
it. These facts establish (4), but provide no n-uniform bound on
Delta and no segment positivity. The latter constraints concern all
values of the polynomial, not merely its two real interpolation data.

### 6. Exact finite sign failure and verification limits

For n=15 use (4) with its exact rational coefficients. At y=1/10,
t=4y/5=2/25 and

    x/(x+i*y)=1/(1-i*t)=(625+50*i)/629.

Exact substitution in (2) and (4) gives -N/D, where the full positive
integers are

    N=1050246342172978881892172551019489084132921050060569063354917316232358414714258288691221214552710755757142219962786890084826044640437771194293263359756655189703584926730353600685600809066499342586746961280441932829403210023805111296296996612105476698655291556730061531836609682428239940617896176617609901492088682717657245325128689340147
    D=31298819174475742799860811244825212476289888089642602301343527129936707666370523928434789707485928761956998887893252404518506916557781573090041759225876437521018837050623787913228917545132242257268106442128367873043599112640005212223053168748175738966174626005283600363792872949882531342628949763150741364082383400504384802173614501953125

These integers give 33*D<1000*N and 500*N<17*D, proving (5).
In particular the exact point lies within |y|<=9/20 and disproves
segment positivity for this specific n=15 least-norm construction.
It does not decide any sufficiently-large-n assertion or a different
feasible h at n=15.

Run `python3 scripts/one-sided-hankel/polynomial-inner-inverse-check.py`.
The script uses rational arithmetic throughout, constructs every
coefficient of h_* and P_h, and checks the two action vectors on
every coordinate basis vector. It also checks normalization, the
prescribed zero, the norm identity and the rational negative enclosure.
The complete certificate is
`scripts/one-sided-hankel/polynomial-inner-inverse-check.json`.
Its 40 algebra checks pass; its separate sign-constraint failure list
contains 12 exact negative rational-point evaluations. The displayed
failure is sufficient; the remaining samples are not used as a proof
of continuum behavior. The finite squared costs are approximately
1.5000724 for normalization alone and 48.8801011 with the zero;
these decimal summaries are not premises of an asymptotic bound.

The certificate's complete selected negative value and Schur complement
were inspected. Neither finite arithmetic nor this derivation is a
separate critical audit. To continue the approved target one must find
or obstruct h with the two exact values, all closed-segment signs and
the uniform rate-1/100 Euclidean cost, or account rigorously for the
additional possible inverse freedom identified in Section 3.

### 7. Independent coefficient reproduction and larger finite tests

The independently written
`scripts/one-sided-hankel/inner-factor-polynomial-check.py` uses the
rotated coordinate v=-u and computes Taylor products by the recurrence
for each factor (a+b*v)/(1-c*v), rather than the convolution used above.
Since J is even, its negative-frequency coefficients H_k correspond to
H_k=(-1)^k*h_(J-k). Its outer inverse includes lambda^(-J), and its
zero functional omits the nonzero scalar r; these changes leave the
projection and the action polynomial unchanged.

For n=15, every action coefficient, every inverse coefficient after
this rotation, the Schur complement and the squared norm agree exactly
with the certificate in Section 6. The same independent formulas were
then evaluated at n=27 and n=51, without any sign optimization or
coefficient fitting. All seven exact algebra checks pass at each of
the three n. At each tested n the two-value minimizer has norm at most
n, but the following exact rational enclosures give further sign failures:

    n=27, y=2/27: -16/125 <= Re P_h(x/(x+i*y)) < -127/1000;
    n=51, y=1/17: -69/125 <= Re P_h(x/(x+i*y)) < -551/1000.

Both ordinates lie in the required closed segment. The full rational
values, all coefficients and every check are in
`scripts/one-sided-hankel/inner-factor-polynomial-check.json`.
The complete selected negative values and the coefficient-comparison
results were inspected. These are finite failures of the particular
two-value minimizer, not an asymptotic obstruction or a sign-constraint
infeasibility result. Likewise the three finite norm bounds do not
establish a uniform rate. The analytic uniform bound in this lemma
remains (3), for anchor normalization alone. This reproduction does
not change the outstanding separate critical-audit qualification.

## Mathlib

Full matching coverage for this finite-product inverse, quantitative
normalization and constrained sign test has not been checked. Scalar
Fourier/Parseval is imported from the precise inspected source above.
The remaining proofs are explicit rational factorization, Fourier
coefficient computations and finite Euclidean projection. No unverified
Mathlib theorem identifier or claim of absence is made.
