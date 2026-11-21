# Corollary C028j: affine Laguerre three-coefficient admissibility stop

## Hypotheses

Use exactly the unchanged actual polynomial and real coefficients of C028a:

    P_d(x)=sum_(j=0)^d binom(d,j)b_j*x^(d-j), b_0=1,
    v=b_1^2-b_2=S_2>0,
    b_3-3*b_1*b_2+2*b_1^3=2*S_3=2*tau>0.

Here d>=5 is an integer and v,tau are fixed actual-Xi constants,
independent of d. Their identities and strict signs are the established
C028a input. No higher actual coefficient, numerical enclosure, RH,
simple-zero or real-root assumption is used.

For each d choose real alpha>-1, m, sigma!=0, with the same parameters
at every degree 0<=n<=d, and define

    q_n(x)=sigma^n*(-1)^n*n!*L_n^(alpha)((x-m)/sigma).

Let mu be the pushforward, under x=m+sigma*z, of the probability measure
z^alpha*exp(-z) dz/Gamma(alpha+1) on z>0. Put
h_n=integral q_n(x)^2 dmu(x), and write uniquely

    P_d=sum_(n=0)^d a_n*q_n.

Parameters may depend arbitrarily on d, approach the admissible boundary,
or be unbounded. In particular negative sigma is allowed. Call the
choice feasible when a_(d-1)=a_(d-2)=a_(d-3)=0.

## Conclusion

All q_n are monic, orthogonal for the positive measure mu, and

    h_n=sigma^(2n)*n!*Gamma(n+alpha+1)/Gamma(alpha+1)>0,
    h_n/h_(n-1)=sigma^2*n*(n+alpha)  (1<=n<=d).

Set N_*=v^3/tau^2, a fixed finite positive real number. Feasibility in
degree d holds if and only if d<N_*+1, and its parameters are then unique:

    alpha=N_*-d, sigma=-tau/v, m=-b_1+v^2/tau.             (1)

Consequently no feasible sequence exists for all sufficiently large d,
or even along any unbounded sequence of degrees. For example, every
integer d>=max{5,ceil(N_*+1)} is infeasible. No numerical bound on N_*
or claim about the remaining finite degrees is needed.

This meets the prescribed eventual-inadmissibility stopping test before
the fourth/fifth retained cost B_d is evaluated. It excludes this
three-coefficient-matched affine generalized-Laguerre family as a route
to a Schmeisser I(P_d)=o(d) payment. It does not exclude unmatched
references, other positive measures or other height estimates; it proves
no lower bound on actual imaginary root heights and does not decide RH.

## Proof

### Imported formulas and affine normalization

NIST Digital Library of Mathematical Functions, version1.2.8,
[Table18.3.1](https://dlmf.nist.gov/18.3#T1), gives Laguerre
orthogonality with weight z^alpha*exp(-z) on (0,infinity), alpha>-1,
leading coefficient (-1)^n/n!, and squared norm
Gamma(n+alpha+1)/n!. Its exact finite formula is
[(18.5.12)](https://dlmf.nist.gov/18.5#E12), with the orthogonality
parameter qualification in Section18.5(iii):

    L_n^(alpha)(z)=sum_(ell=0)^n
       (alpha+ell+1)_(n-ell)*(-z)^ell/((n-ell)!*ell!).     (2)

The parenthesized subscript here is the rising factorial. These formulas
were inspected in source-notes1591 and are imported, not reproved.
Qiongqiong Pan and Jiang Zeng, *Combinatorics of (q,y)-Laguerre
polynomials and their moments*, Seminaire Lotharingien de Combinatoire
81 (2020), B81e, [p1 (1.1)-(1.4)](https://www.mat.univie.ac.at/~slc/wpapers/s81panzeng.pdf),
provides the previously inspected monic normalization cross-check.
No source asymptotic with fixed alpha is used for varying alpha_d.

The leading term in the definition of q_n is
sigma^n*((x-m)/sigma)^n=(x-m)^n, so q_n is monic even for sigma<0.
For fixed parameters, integration against the pushforward is exactly
integration after x=m+sigma*z against the normalized Gamma measure.
Thus orthogonality follows from the imported formula, and multiplying
its squared norm by sigma^(2n)*(n!)^2/Gamma(alpha+1) gives precisely
the claimed h_n. The Gamma recurrence gives its consecutive ratio.
The measure has infinite support and all moments; alpha>-1 makes its
normalization and every h_n finite and strictly positive. Reflection
does not change positivity: pushforward integration introduces no signed
Jacobian. No uniform-in-d support or norm bound is assumed.

### Exact three-coefficient calculation

For this paragraph fix d and put N=d+alpha, so N>d-1>=4. Write
N^[j]=N*(N-1)*...*(N-j+1), with N^[0]=1. Set ell=d-j in (2).
Multiplication by the monic and affine factors gives exactly

    q_d(x)=sum_(j=0)^d binom(d,j)*(-sigma)^j*N^[j]
                                *(x-m)^(d-j).           (3)

In particular this is a finite coefficient identity for every admitted
parameter, with no asymptotic approximation. Define c_j by

    q_d(x)=sum_(j=0)^d binom(d,j)*c_j*x^(d-j).

Expanding each (x-m)^(d-j) in (3), and using
binom(d,k)*binom(d-k,j-k)=binom(d,j)*binom(j,k), gives

    c_j=sum_(k=0)^j binom(j,k)*(-m)^(j-k)*(-sigma)^k*N^[k].

Thus c_0=1 and, writing A=m+sigma*N, the first three are

    c_1=-A,
    c_2=A^2-sigma^2*N,
    c_3=-A^3+3*A*sigma^2*N-2*sigma^3*N.                 (4)

For example the uncollected third expression is
-m^3-3*m^2*sigma*N-3*m*sigma^2*N*(N-1)
-sigma^3*N*(N-1)*(N-2), which expands to (4).
It follows directly that

    c_2-c_1^2=-sigma^2*N,
    c_3-3*c_1*c_2+2*c_1^3=-2*sigma^3*N.                (5)

These are finite polynomial identities. They require no logarithm
branch, interchange of limits, or assumption on the roots of q_d or P_d.

Because q_d and P_d are monic, a_d=1. Triangular comparison in the
monic basis shows that the three a-coefficients in the hypothesis
vanish if and only if P_d-q_d has degree at most d-4. Equivalently
c_j=b_j for j=1,2,3; the binomial factors are nonzero. Combining
(4)-(5) with the exact C028a identities, feasibility is equivalent to

    -(m+sigma*N)=b_1,
    sigma^2*N=v,
    -sigma^3*N=tau.                                    (6)

Conversely (6) fixes the same first coefficient, second centered
coefficient and third centered coefficient, so (4)-(5) recover
c_1=b_1, c_2=b_2, c_3=b_3. There is no implication missing in this
equivalence.

### Complete feasibility classification and stopping test

Divide the third equation of (6) by the second; v>0 makes this
legitimate. This forces sigma=-tau/v!=0. The second then forces
N=v^3/tau^2=N_*>0. The first forces m=-b_1+v^2/tau, and N=d+alpha
forces alpha=N_*-d. This proves uniqueness and necessity of (1).

Conversely these parameters satisfy (6). They define an admitted
reference exactly when alpha>-1, that is d<N_*+1. This proves both
directions of the degree criterion. At equality alpha=-1 is excluded:
the stipulated Gamma probability weight is not integrable at zero.
For larger d it is likewise inadmissible. Every integer
d>=ceil(N_*+1) fails the strict inequality, including when N_*+1 is
an integer. Restriction to d>=5 gives the stated sufficient threshold.

The classification already includes all real translations, both signs
of nonzero scale, arbitrary degree dependence, and every approach to
alpha=-1 or to zero/infinite scale. Matching itself fixes the scale
and N, so no boundary sequence can evade the obstruction. Only the
fixed positivity of v and tau was used; no quantitative evaluator or
sign of S_4 or S_5 enters.

Schmeisser, *Estimates for the Imaginary Parts of the Zeros of a
Polynomial*, Mathematica Balkanica16 (2002),203-217,
[Theorem1/Corollary1, pp205-207](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf),
is the downstream height interface already specified in C028a. The
present positive measure meets its measure hypotheses, but the proposed
three cancellations fail eventually. Therefore the approved feasibility-
first diagnostic stops without estimating B_d or the full residual sum.
This is an obstruction to that stipulated upper-bound construction,
not a lower-bound argument for actual heights. C028b's RH-equivalent
height payment remains missing and is motivation only, not a premise.
C028c's terminal-Hermite cost floor is a comparison, not an input.

This is a local known-method specialization under assessment1591.
No originality beyond the checked sources is claimed. The finite
coefficient, norm and endpoint audit is recorded below.

### Independent finite audit1594 (2026-11-18)

Under the pre-existing SPECIALIZE assessment1592, independently replayed
the imported finite formula and positive-measure normalization. For
ell=d-j its rising factorial is
(alpha+d-j+1)_j=N*(N-1)*...*(N-j+1), not (N)_j. The factor multiplying
(x-m)^(d-j) is therefore exactly
(-1)^j*sigma^j*d!*N^[j]/(j!*(d-j)!). In particular the uncollected
binomial-normalized coefficients are

    c_1=-m-sigma*N,
    c_2=m^2+2*m*sigma*N+sigma^2*N*(N-1),
    c_3=-m^3-3*m^2*sigma*N-3*m*sigma^2*N*(N-1)
          -sigma^3*N*(N-1)*(N-2).

Subtracting the square of c_1 from c_2 leaves -sigma^2*N.
In c_3-3*c_1*c_2+2*c_1^3 the m-dependent terms cancel; the remaining
sigma^3 coefficient is

    -N*(N-1)*(N-2)+3*N^2*(N-1)-2*N^3=-2*N.

This checks both centered identities without an asymptotic expansion
or an assumption about root locations. The actual centered second
coefficient is -v and the third is 2*tau, as supplied by C028a.

To check both matching implications, put r=P_d-q_d. Its coefficient
of x^(d-1) is d*(b_1-c_1). Since the basis is monic, it is also
a_(d-1). If this vanishes, the coefficient of x^(d-2) is simultaneously
binom(d,2)*(b_2-c_2) and a_(d-2). If these two vanish, the next
coefficient is simultaneously binom(d,3)*(b_3-c_3) and a_(d-3).
Conversely degree(r)<=d-4 forces all three a-coefficients to vanish
in the unique monic-basis expansion. Thus neither direction uses a
higher coefficient or a property of the roots. Given c_1=b_1, equality
of the centered second coefficients recovers c_2=b_2; the centered
third then recovers c_3=b_3. Equations (6) are genuinely equivalent
to the three requested cancellations.

For the norm, direct pushforward integration gives

    h_n=sigma^(2n)*(n!)^2/Gamma(alpha+1)
          *[Gamma(n+alpha+1)/n!].

Here h_0=1 and h_1=sigma^2*(alpha+1)>0. Taking the consecutive ratio
gives sigma^2*n*(n+alpha), positive for every n>=1 under alpha>-1.
For sigma<0 the same pushforward remains a positive probability
measure on x<m; writing a density would introduce 1/abs(sigma),
never 1/sigma. Its moments are finite for each fixed admitted triple.
No uniform norm or support assertion is needed across degrees.

Finally sigma^2*N=v and -sigma^3*N=tau force the negative scale
sigma=-tau/v, then N=N_* and the unique stated translation. Substitution
back into all three equations verifies sufficiency, rather than merely
necessity. Writing beta=alpha+1 makes the admissibility check explicit:

    N=d-1+beta, beta>0;
    beta=N_*-d+1>0  iff  d<N_*+1.

At equality the weight has a z^(-1) singularity at zero and cannot be
normalized as the stipulated Gamma probability measure. Above equality
the singularity is worse. Approaching this boundary with d-dependent
parameters cannot help, because matching fixes N and sigma exactly.
The ceiling threshold includes the integral-equality case. No numerical
size of N_* is required.

The audit finds no correction to the statement or direct mathematical
input C028a. It verifies the existing known-method specialization, not
a new family obstruction beyond the statement already proved. The stop
concerns only exact three-coefficient matching in this family; an
unmatched Laguerre basis is not excluded. No retained-cost calculation,
actual-height lower bound, full Schmeisser upper payment or RH result
follows. C028b and C028c remain motivation and comparison, respectively,
and introduce no additional direct inputs to this corollary.

## Mathlib

Not checked. Full matching coverage for the affine normalization and
actual-Xi feasibility obstruction is unknown; no absence or formal
verification is claimed. The imported formulas have precise citations,
and the required finite specialization is proved above.
