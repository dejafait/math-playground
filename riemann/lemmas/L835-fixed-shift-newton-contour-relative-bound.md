# Lemma 835: explicit Newton-contour relative bound at shift 6002

## Hypotheses

Use the actual F, simple positive poles p_1<...<p_k, separating radius
R=(p_k+p_(k+1))/2, matrices Q_r,E_r and determinant D_(r,k) of L834,
with k=6002. In particular F(0)=1, F is real entire, and its only zeros
in the closed radius-R disk are the simple p_1,...,p_k. No quantitative
zero enclosures, gap lower bounds, RH or residual total positivity are
assumed. Fix an integer r>=k-1 and a real s with q=p_k/R<s<1. Put

\[
x_l=p_l/R,\quad N=r+k-1,\quad f(z)=F(Rz),\qquad
P(w)=\prod_{l=1}^k(1-w/p_l),\quad
g(z)=\frac{F(Rz)}{P(Rz)}.
\]

The quotient uses its removable values. It is entire and has no zero
on or inside the unit circle. Define the following positive, explicit
analytic quantities and finite products (an empty product is 1):

\[
M_s=\max_{|z|=s}|g(z)|,\qquad m_1=\min_{|z|=1}|g(z)|>0,
\]
\[
B_i=\prod_{a=1}^{i}(1+x_a),\qquad
\Lambda_i=\prod_{a=i+2}^{k}(s+x_a),\quad 0\le i<k,
\]
\[
T_s=\sum_{i=0}^{k-1}B_i\Lambda_i,\qquad
d_s=\prod_{a=1}^{k}(s-x_a)>0,\quad
d_1=\prod_{a=1}^{k}(1-x_a)>0,
\]
\[
\mathcal C(s)=\frac{M_s}{m_1}\frac{T_s^2}{d_sd_1},\qquad
\delta_r(s)=\mathcal C(s)s^{r+k+1}.                         \tag{1}
\]

Neither M_s nor m_1 is supplied with a numerical certificate here.

## Conclusion

There is an explicitly defined real invertible matrix S_s, independent
of r, such that the maximum absolute row-sum norm satisfies

\[
\left\|S_s^{-1}Q_r^{-1}E_rS_s\right\|_\infty
       \le\delta_r(s).                                    \tag{2}
\]

Formula (1) contains no inverse individual difference x_b-x_a, no
reciprocal F'(p_l), and no inverse Vandermonde norm. It retains the
actual quotient g, all contour factors and all r-dependence. Distances
from the packet to the chosen contours and the lower bound for the
quotient remain essential. This is a bound in a genuine similarity
coordinate system; it is not asserted for L834's original matrix norm.

If delta_r(s)<1, then D_(r,6002)>0. For one fixed s this holds at every
integer rank at least

\[
r_*(s)=\max\left\{k-1,
 \left\lfloor\frac{\log\mathcal C(s)}{-\log s}-k-1\right\rfloor+1
 \right\}.                                               \tag{3}
\]

This is an analytic expression for a sufficient onset, not a certified
numerical onset. To overlap a separately justified PF_m range, it is
sufficient that m+1>=k-1 and

\[
\log(M_s/m_1)+2\log T_s-\sum_a\log(s-x_a)
 -\sum_a\log(1-x_a)+(m+k+2)\log s<0.                       \tag{4}
\]

Then the finite range gives nonnegativity through rank m and (2) gives
strict positivity at every rank r>=m+1, at this one shift only. L832
already justifies m=6001. Its cited sector source permits the condition
m+1<=pi H, H=3,000,175,332,800; using an enlarged integer m still requires
that cutoff's applicability argument. This lemma neither selects nor
proves an enlarged finite-PF cutoff, and does not verify (4) for any m.
No all-rank conclusion, growing-shift theorem or RH conclusion follows
without the unpaid quantitative obligations. The finite-range signs
would remain nonnegative, not necessarily strict.

This is a standard interpolation/residue specialization with new local
bookkeeping, not a claim of new interpolation theory or originality.
The separate conceptual audit of 2026-11-06, step674, validates (1)–(4)
at the stated fixed-shift and conditional-overlap scope. It supplies no
numerical contour bounds, enlarged PF cutoff or actual overlap.

## Proof

**Imported tools and purpose of the specialization.** Carl de Boor,
*Divided Differences*, Surveys in Approximation Theory **1** (2005),
46–69, [author PDF](https://ftp.cs.wisc.edu/Approx/dvdsurvey.pdf),
[arXiv:math/0502036v1](https://arxiv.org/pdf/math/0502036v1),
Proposition25/(24)–(26), pp.53–54, supplies the Newton coordinate
convention; Proposition35/Definition37, pp.58–59, supplies Hermite
function data; Example9/(41), p.60, and (49)–(51), pp.62–63, give
the distinct-node sum and holomorphic contour formula for divided
differences. The author copy's June2005 Corollary30 correction is not
used. We import these formulas, not reprove their general statements.
The sampled-data norm in (42) would retain inverse node derivatives;
our data instead come from one analytic function, as shown below.

For the contour with an origin pole use Matthias Beck, Gerald Marchesi,
Dennis Pixton and Lucas Sabalka, *A First Course in Complex Analysis*,
[Section8.1, Theorem8.1.5](https://complexanalysis.org/web/sec_residue-thm.html).
Its residue theorem for a simple positively oriented closed contour in
a simply connected domain retains all interior isolated singularities.
The present integrands are meromorphic on neighborhoods of the closed
disks, with no boundary singularities; all poles are identified below.
The finite-minor duality, actual simple packet and strict sign of det Q_r
are the already justified inputs of L834. The work here identifies the
particular inverse and remainder matrices and bounds them together;
none of these sources already supplies (1) for the actual F.

**1. Scaled Newton matrices and exact similarity.** Write

\[
\pi(z)=\prod_{a=1}^k(z-x_a),\qquad
J(z)=f(z)/\pi(z)=g(z)/\pi(0),\qquad
b_i(z)=\prod_{a=1}^{i}(z-x_a),\qquad
\lambda_i(z)=\prod_{a=i+2}^{k}(z-x_a).
\]

Here pi(0)=(-1)^k prod_a x_a is nonzero. J is entire, with the values
at the selected nodes filled in. Let C be the real lower triangular
coefficient matrix defined by

\[
(b_0(z),\ldots,b_{k-1}(z))^T=C(1,z,\ldots,z^{k-1})^T.
\]

Each diagonal entry of C is 1, so it is invertible without dividing by
any node difference. Let W be the column-reversal matrix and let
D=diag(R^(-i))_(i=0)^(k-1). Set

\[
\widehat Q=R^NDQ_rWD,\quad \widehat E=R^NDE_rWD,\qquad
Q^b=C\widehat Q C^T,\quad E^b=C\widehat E C^T.
\]

Because reversing columns changes r+j-i into N-i-j, these matrices obey

\[
\widehat Q_{ij}=\sum_l A_l x_l^{i+j-N},\qquad
\widehat E_{ij}=R^{N-i-j}b_{N-i-j}^{\rm rem},              \tag{5}
\]

where b_n^rem=h_n-sum_l A_l p_l^(-n) is L834's remainder coefficient.
All these indices are nonnegative since N>=2k-2. The original b_n^rem
and the Newton polynomial b_i(z) are distinct notations.

If S_0=WDC^T, direct multiplication gives

\[
(Q^b)^{-1}E^b=S_0^{-1}Q_r^{-1}E_rS_0.                   \tag{6}
\]

In particular this is similarity, even though each individual moment
matrix was transformed on both sides. No determinant sign is inferred
from the column reversal itself. Later put
L=diag(Lambda_i) and S_s=S_0L; all Lambda_i are strictly positive.
Both S_0 and S_s are real, invertible and independent of r.

**2. The inverse entries as coupled divided differences.** Let
V_(il)=b_i(x_l). Distinct nodes make V invertible. From (5),

\[
Q^b=V\operatorname{diag}(A_l x_l^{-N})V^T,\qquad
A_l=-\frac1{x_lf'(x_l)}
    =-\frac1{x_l\pi'(x_l)J(x_l)}.                         \tag{7}
\]

The factor R in f'(x_l)=R F'(p_l) verifies that these A_l are exactly
L834's residues. In particular none is zero.

The finite product identity

\[
\frac{\pi(z)-\pi(t)}{z-t}
       =\sum_{i=0}^{k-1}b_i(z)\lambda_i(t)                \tag{8}
\]

holds as a polynomial identity, including z=t. It is the telescoping
difference of the two products prod(z-x_a) and prod(t-x_a), replacing
one factor at a time. At t=x_l, division by pi'(x_l) gives the Lagrange
polynomial equal to 1 at x_l and 0 at the other nodes. Consequently
column l of V^(-T) is (lambda_i(x_l)/pi'(x_l))_i. Inserting these
columns and (7) into the inverse factorization gives exactly

\[
((Q^b)^{-1})_{ij}
 =-\sum_{l=1}^k
  \frac{x_l^{N+1}J(x_l)\lambda_i(x_l)\lambda_j(x_l)}{\pi'(x_l)}
 =-[x_1,\ldots,x_k]\bigl(t^{N+1}J(t)\lambda_i(t)\lambda_j(t)\bigr).
                                                               \tag{9}
\]

The bracket denotes the order k-1 divided difference. All its values
belong to the same entire function. The cited contour formula applies
on |t|=s because all nodes have modulus <s, J is entire, and the integer
exponent N+1 is positive. It yields

\[
((Q^b)^{-1})_{ij}
 =-\frac1{2\pi i}\int_{|t|=s}
   \frac{t^{N+1}J(t)\lambda_i(t)\lambda_j(t)}{\pi(t)}\,dt.
                                                               \tag{10}
\]

There is no origin singularity in (10). In particular no reciprocal
node derivative survives after using analytic coupling. The derivation
used the actual distinct simple nodes throughout. Hermite continuity
motivates the choice of coordinates but does not change any actual
multiplicity or assert a new confluent-pole theorem.

**3. The remainder contour, including zero.** The exact companion formula
is

\[
E^b_{ij}=\frac1{2\pi i}\int_{|u|=1}
     \frac{u^{-N-1}b_i(u)b_j(u)}{f(u)}\,du.                \tag{11}
\]

To check it, near zero 1/f(u)=sum_(n>=0) R^n h_n u^n. The product
b_i(u)b_j(u) has degree at most 2k-2<=N. Thus the residue at zero is
exactly the (i,j) entry of C[R^(N-a-b)h_(N-a-b)]_(a,b) C^T,
the transformed full reciprocal coefficient block. The residue at x_l
is x_l^(-N-1)b_i(x_l)b_j(x_l)/f'(x_l), equal by (7) to
-A_l x_l^(-N)b_i(x_l)b_j(x_l). Summing over the packet gives -Q^b.
These and zero are all interior poles, and there is no boundary pole,
by L834's separation. The residue theorem therefore gives full block
minus Q^b, proving (11). The Taylor series was used only near zero;
it has not been continued through a pole, and the origin contribution
has not been discarded.

**4. All constants and the weighted norm.** On the two circles,

\[
|\lambda_i(t)|\le\Lambda_i\quad(|t|=s),\qquad
|b_i(u)|\le B_i\quad(|u|=1),\qquad
|\pi(t)|\ge d_s,\quad |\pi(u)|\ge d_1.
\]

Since J=g/pi(0) and f=pi g/pi(0), (10)–(11) imply

\[
|((Q^b)^{-1})_{ij}|
 \le s^{N+2}\frac{M_s}{|\pi(0)|d_s}\Lambda_i\Lambda_j,
\qquad
|E^b_{ij}|\le\frac{|\pi(0)|}{d_1m_1}B_iB_j.              \tag{12}
\]

The exponent N+2 includes both t^(N+1) and the length factor s of the
inner circle after division by 2pi. The outer circle has radius 1, so
its corresponding factor and |u|^(-N-1) both equal 1. No constants
are suppressed. Multiplying the entry bounds before taking row sums
cancels |pi(0)| and gives

\[
|((Q^b)^{-1}E^b)_{ij}|
 \le s^{N+2}\frac{M_s}{m_1d_sd_1}\Lambda_i B_j
                         \sum_{a=0}^{k-1}\Lambda_a B_a.
\]

Conjugate by L=diag(Lambda_i). Its (i,j) bound now has Lambda_i canceled
and Lambda_j inserted, so every row sum is at most

\[
s^{N+2}\frac{M_s}{m_1d_sd_1}
              \left(\sum_a B_a\Lambda_a\right)^2.
\]

Using N+2=r+k+1 and (6) proves (1)–(2). This extra diagonal change of
coordinates uses only positive products s+x_a; it introduces no
individual pole-gap denominator. For an optional evaluation formula,
the same product telescoping as (8) gives

\[
T_s=\frac{\prod_a(1+x_a)-\prod_a(s+x_a)}{1-s}.
\]

The finite positive sum defining T_s avoids numerical cancellation and
is the definition used in the bound. No limiting operation in s is used.

**5. Sign transfer and the precise overlap obligation.** Formula (2)
and delta_r(s)<1 make I+t S_s^(-1)Q_r^(-1)E_rS_s invertible for every
0<=t<=1 by the Neumann-series criterion. These matrices are real; the
continuous determinant starts at 1 and never vanishes. Similarity
preserves it. Hence det(I+Q_r^(-1)E_r)>0. L834 gives det Q_r>0 and
D_(r,k)=a_0^r det(Q_r+E_r) with a_0>0, proving the claimed sign.

All factors in C(s) are positive and finite for the chosen s. Taking
logarithms in (1) gives delta_r(s)<1 exactly when
r>log C(s)/(-log s)-k-1. This proves the sufficient onset (3), with
the strict inequality handled by floor plus one even at an integer
threshold. For a fixed s, delta_r decreases as r increases. Applying
that fact at r=m+1 gives exactly (4), with exponent m+k+2. Combining
it with an independently proved finite-PF range yields the stated
conditional overlap, without asserting strictness of the finite signs.

The condition m+1<=pi H is the sector statement recorded in L832 from
Michałowski, arXiv:2607.16795v1 Section1.2 and Katkova's TheoremB.
It is mentioned to state the remaining comparison, not used as a
premise of (1)–(3) or as proof of an enlarged local PF theorem.

Thus the individual-node conditioning loss has been replaced by
specified analytic and contour data. Packet-to-complement separation
still enters R, q, s, d_s, d_1 and m_1. Even a very large upper bound
in (1) is not evidence of a negative minor or of matrix singularity.
No existing hybrid determinant ratio, unproved residual sign, RH-
equivalent positivity, arbitrary independent sampled errors, or
unjustified limit interchange is a premise. Effective values of the
analytic data and (4) remain unresolved.

**Conceptual audit (2026-11-06, step674).** The proof passes without a
mathematical correction. The previously assessed de Boor and residue
formulas are reused with their stated hypotheses; no new source or
general interpolation theorem is claimed. The full specialization above
was checked, including the relevant L834 identities and L832's finite
range. The following checks identify what is validated.

For the orientation, put A=R^N C D. Then Q^b=A Q_r S_0 and
E^b=A E_r S_0, with S_0=W D C^T. Cancellation of the common left
factor gives exactly (6); neither W nor D may be moved across C^T.
The scalar R^N cancels and is absent from S_s, so S_s is independent
of r. If H_(il)=lambda_i(x_l)/pi'(x_l), evaluation of (8) gives
V^T H=I, hence H=V^(-T). Therefore the inverse uses H on the left
and H^T on the right. Its two factors of pi'(x_l) combine with
1/(A_l x_l^(-N))=-x_l^(N+1)pi'(x_l)J(x_l) to give (9), with
its negative sign and precisely one remaining node derivative before
the analytic divided-difference formula is applied. This uses distinct
simple poles, not independent sampled perturbations or confluent poles.

The inner numerator in (10) is entire and N+1>=1, so the origin is
regular there. The outer integrand in (11) instead has its origin
contribution. Every monomial index N-a-b is nonnegative because
N>=2k-2. Its origin residue gives the full scaled reciprocal block;
the selected-pole residues give minus Q^b. No other zero is enclosed
and neither contour contains a zero on its boundary. In particular,
no Taylor series of 1/f is evaluated outside its disk of convergence.

The circle factors are s and 1, respectively. The factors |pi(0)|
cancel only after the two entry bounds in (12) are multiplied. The
remaining index sum is T_s; conjugation by the positive diagonal L
then gives a second T_s in the row sum, with no additional k factor.
Thus the exponent is N+2=r+k+1 and the norm is in the claimed genuine
similarity coordinates. All distances s-x_a and 1-x_a are positive;
no lower bound for an individual x_b-x_a is invoked. The actual
contour distances and m_1 still cannot be omitted or assumed uniform.

Finally the real Neumann segment preserves a positive determinant
starting at 1; L834 supplies both det Q_r>0 and the factor a_0^r.
For fixed s, the strict scalar condition is r>log C(s)/(-log s)-k-1,
so (3) retains floor plus one, including equality at an integer
threshold. For an independently justified integer PF order m>=1
with m+1>=k-1, substitution r=m+1 gives exponent m+k+2 in (4).
L832 provides only the local PF6001 assertion; the quoted sector
condition is not an enlarged PF theorem in this lemma. Finite-range
signs remain nonnegative. Neither (4) nor any actual value of r_* is
certified by this audit, and the all-degree mixed-positivity gap remains.

## Mathlib

Full matching coverage is unchecked; no presence or absence claim is
made. Newton/Hermite divided differences, residue and Cauchy formulas,
finite matrix changes of basis, and the Neumann-series criterion are
standard supporting inputs. The complete actual-Xi specialization and
its quantitative constants have not been checked against Mathlib.
