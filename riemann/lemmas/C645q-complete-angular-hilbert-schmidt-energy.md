# Corollary 645q: complete angular Hilbert--Schmidt energy

## Hypotheses

Retain C645g's normalized Hardy spaces and C645o's angular family:
n>=5, x=-d=-5/4, R=11/8, U=R^2, eta=1/100, t_j=j/n, and a
finite set Z of distinct poles with Re(a)=x, |a|<=R-eta, x in Z.
Original simple-pole residues r_a are positive integers and
M=sum_a r_a<=n/3. Write m=|Z|. The same poles and residues are used
at every angle; no separation or ordinate symmetry is assumed.

With u=i exp(i theta), |u|=1, put

    W_a(u)=(x/a)*product_(j=1)^(n-1)
              (x-t_j*u)/(a-t_j*u)*(U*u-t_j*a)/(U*u-t_j*x),
    I(a,b)=mean_u W_a(u)*conjugate(W_b(u)),
    q_theta(zeta)=sum_a [r_a*W_a(u)/R]/(zeta-a/R),
    H_theta f=P_-(q_theta*f): H^2 -> H^2_-.

The measure on each circle is normalized by 1/(2*pi). These W_a are
exactly B_theta(x)/B_theta(a) for

    B_theta(v)=product_(j=0)^(n-1)
        R*(v-i*exp(i*theta)*t_j)/(U+i*exp(-i*theta)*t_j*v).

In particular, the denominator angle is conjugated. Let

    E_op=mean_theta ||H_theta||^2,
    E_HS=mean_theta ||H_theta||_HS^2,

where the first norm is the largest operator norm and the second is
the Hilbert--Schmidt norm.

## Conclusion

The complete signed energy and its norm comparison are

    E_HS=sum_(a,b in Z) r_a*r_b*U*I(a,b)/(U-a*conjugate(b))^2,   (1)
    E_HS/m <= E_op <= E_HS.                                    (2)

Both angular Fourier signs, the constant angular mode, and every
spatial coefficient are retained. Formula (1) is not an entrywise
positive bound; no signed cross term can be discarded. C645o's
finite residue formula evaluates I(a,b) if desired.

Consequently a proved upper estimate
sqrt(E_HS)<=C n^A exp(-(1/32+epsilon)n), epsilon>0, along an
admissible sequence would refute the proposed uniform angular detector.
No such estimate is established here. More generally

    0 <= log(sqrt(E_HS)/sqrt(E_op))/n <= log(m)/(2*n),           (3)

so the two root energies have the same upper/lower exponential rates
along sequences with n tending to infinity and m<=n/3. The polynomial
loss cannot be omitted at the exact threshold: a lower bound for
sqrt(E_HS) by c exp(-n/32) alone gives only c exp(-n/32)/sqrt(m)
for sqrt(E_op), not the required uniform constant.

The radius-adjusted family

    m>=3 odd, n=3m, 0<r<=1/2,
    a_k=x+i*r*cos((2k-1)*pi/(2m)), r_(a_k)=1, 1<=k<=m,         (4)

is admissible in (1)--(3), including radii depending on n. Its energy
has not been bounded at the required rate. This is an unaudited
specialization of standard Fourier and finite-rank identities, not a
new theorem beyond the checked sources or an RH advance.

## Proof

### Source scope and why this calculation is needed

The unchanged invocation-start
[EXPLORE assessment](../drafts/literature/2026-11-02-rotation-averaged-anchor-line-hankel.md)
covers precisely this angular family, Fourier/coefficient analysis,
and admissible full-mean countersequences. Reuse the operator
conventions in L. Baratchart, S. Chevillard and T. Qian,
*Minimax principle and lower bounds in H2-rational approximation*,
J. Approx. Theory 206 (2016), 17--47, preprint v2 (24 March 2015),
[Section 4, (17)--(19)](https://arxiv.org/pdf/1501.01161v2),
[DOI](https://doi.org/10.1016/j.jat.2015.03.004).
Use scalar Fourier orthogonality and Hilbert-space Parseval from
A. Levitt, *Analyse de Fourier et applications*,
[author PDF](https://www.imo.universite-paris-saclay.fr/~antoine.levitt/blog/fourier/article.pdf),
version retrieved 2 November 2026, Theorem 1.3/Exercise 1.2 and
Theorem 1.11/Corollary 1.12, printed pp.6,8 (PDF pp.12,14).
Normalized measure makes each circle exponential have norm one.

C645g supplies the spaces; C645o supplies the exact W_a and I(a,b).
Its independently unaudited residue evaluation is not needed to
establish (1) using the integral definition of I. None of C645m's
ellipse obstruction, C645n's inner input or C645p's projection estimate
is a premise. Their method-specific stops are preserved. The elementary
specialization below is needed to distinguish an upper bound for the
entire operator response from the earlier lower bounds and angular
projections. No Nehari or Parseval theorem is reproved, and no Parseval
identity is asserted for the operator norm itself.

### Complete spatial energy and angular integration

For fixed n and Z, W_a is continuous on |u|=1. Indeed |a|>=d>1>t_j,
while |U*u-t_j*x|>=U-t_j*d>0. Thus there is a finite bound A for
every |W_a| on the angular circle. Put rho=(R-eta)/R<1. The exterior
series is

    q_theta(zeta)=sum_(k>=0) c_k(theta)*zeta^(-k-1),
    c_k(theta)=sum_a r_a*W_a(u)*a^k/R^(k+1),
    |c_k(theta)| <= (M*A/R)*rho^k.                             (5)

It converges absolutely and uniformly in both angular variables.
For the normalized input basis e_j(zeta)=zeta^j, j>=0, projection
onto the negative modes gives

    H_theta e_j=sum_(l>=0) c_(j+l)(theta)*zeta^(-l-1).

Scalar Parseval and the nonnegative double sum therefore give

    ||H_theta||_HS^2
       =sum_(j,l>=0)|c_(j+l)(theta)|^2
       =sum_(k>=0)(k+1)|c_k(theta)|^2.                         (6)

This is finite, uniformly in theta for the fixed family, by the
summable majorant (M*A/R)^2*(k+1)*rho^(2k). No bound on A uniform in
n or Z is asserted or needed for these identities. Expand each square
in (6). There are finitely many a,b, and each resulting series converges
absolutely and uniformly. The geometric derivative identity gives

    sum_(k>=0) (k+1)*(a*conjugate(b))^k/R^(2k+2)
      = (1/U)/(1-a*conjugate(b)/U)^2
      = U/(U-a*conjugate(b))^2.                               (7)

Its denominator is nonzero since |a*conjugate(b)|<=rho^2*U<U.
Angular integration can be interchanged with the series and finite
sums by the stated majorant. Equations (6)--(7) prove (1).
Although (1) is a squared norm, its complex summands have signed real
cross contributions. The identity retains all of them.

### Rank and operator-norm comparison

For alpha=a/R and any polynomial f, the exterior expansion directly
shows

    P_-(f(zeta)/(zeta-alpha))=f(alpha)/(zeta-alpha).

This extends to every f in H^2: polynomials are dense; evaluation at
alpha is bounded by ||f||_2/sqrt(1-|alpha|^2); the boundary symbol and
the projection are bounded. Hence

    H_theta f=sum_a (r_a*W_a(u)/R)*f(a/R)/(zeta-a/R).          (8)

The range lies in the span of the m displayed exterior kernels, so its
rank is at most m. For completeness, a finite-rank operator vanishes
on its kernel and has a subspace (ker H)^perp of dimension equal to
its rank. Choose an orthonormal basis there and extend it through
the kernel. Hilbert-space Parseval shows that the sum of ||H e_j||^2
is independent of the chosen input basis: expand in an output
orthonormal basis and interchange nonnegative sums. In this adapted
basis at most m terms are nonzero, each at most ||H||^2. Conversely,
for any unit input, Cauchy--Schwarz in the same finite basis gives
||Hf||^2<=sum_j ||H e_j||^2. Thus

    ||H_theta||^2 <= ||H_theta||_HS^2 <= m*||H_theta||^2.

All functions involved are measurable (indeed continuous in theta
by (5)--(8)); integration proves (2). Each q_theta is nonzero because
its distinct simple poles have nonzero residues, so H_theta 1 is
nonzero and both mean energies are positive. Taking logarithms proves
(3). Since log(m)/n<=log(n/3)/n tends to zero, the exponential-rate
assertion follows, with the exact-threshold qualification stated above.

As a scaling check, for the one-pole family Z={x}, residue M, W_x=1,
both energies equal M^2*U/(U-x^2)^2, by (8) and the norm of evaluation.
The constant-input energy instead equals M^2/(U-x^2). This verifies
the squared denominator and the factor U in (1); the two energies
must not be confused.

### Admissibility of the varying radius

Cosine is strictly decreasing on (0,pi); with r>0 the m nodes in (4)
are distinct. Odd m gives the anchor at k=(m+1)/2. Every pole has
real part x and

    |a_k|^2 <= d^2+r^2 <= 29/16,
    (R-eta)^2-29/16 = 2029/40000 > 0.

All rotated grid zeros have modulus t_j<1, whereas |a_k|>=5/4.
No angle creates a collision. Also the B_theta denominators are
nonzero on |v|<=R, since their modulus is at least U-t_j*R>0.
The original residues are all one, so M=m=n/3, n>=9, and every
hypothesis is satisfied. These statements hold separately for each
positive r and thus also for arbitrary sequences 0<r_n<=1/2; no
uniform separation as r_n tends to zero has been assumed.

### What the finite screen does and does not show

`scripts/one-sided-hankel/angular-chebyshev-full-energy-screen.py`
saves diagnostic sampled/truncated values to the corresponding JSON
file. It evaluates (5) directly before taking squares, retaining all
angular samples and 256 spatial coefficients weighted as in (6).
This avoids discarding cross terms, but neither the spatial tail,
angular quadrature, nor rounding is enclosed. The resulting numbers
are not upper bounds for E_HS and are not certificates of any rate.
Their role is only to nominate a more specific analytic test. Formulae
(1)--(8), not the screen, are the proved content of this note.
The full-family angular bound and a countersequence remain unresolved.

## Mathlib

Full matching coverage has not been checked. No absence claim is made.
The proof uses normalized Fourier Parseval, bounded point evaluation,
finite-rank linear algebra and a differentiated geometric series.
The cited general results do not evaluate (1) for the present growing
Chebyshev family. A separate independent audit remains outstanding.
