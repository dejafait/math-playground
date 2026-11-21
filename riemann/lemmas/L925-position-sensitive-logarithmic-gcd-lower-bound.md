# Lemma 925: position-sensitive lower bound at coefficient log N

## Hypotheses

Let N>=2 be an integer and c=(c_1,...,c_N) any complex vector.
All logarithms are natural. For real A use the full finite form

    F_A(c)=sum_(m,n<=N) c_m conjugate(c_n) gcd(m,n)/sqrt(m*n)
                         *[A+2 log gcd(m,n)-log m-log n].

With Euler's totient phi(1)=1 and von Mangoldt function Lambda(1)=0,
put

    b_n=c_n/sqrt(n),   B_d=sum_(k<=N/d) b_(dk),
    C_d=sum_(k<=N/d) b_(dk) log k,
    Q(c)=sum_(d<=N) phi(d)|B_d|^2,
    kappa(d)=sum_(p|d) log p/(p-1),   kappa(1)=0.

All indices in these sums are integers; cutoffs N/d are real and
empty sums are zero. Import L737's finite identities (5)-(8),
totient comparison (9) and inversion (11), and L924's scalar bound
(4) and position-dependent rows (7). Their analytic moment, height,
bump and multiplier-length assumptions are not used: the cited finite
identities apply to arbitrary finite complex vectors.

Fix the same absolute nonnegative constant as L924,

    C_* = M+3 log 2+2,

where M>=0 satisfies sum_(n<=x) Lambda(n)/n<=log x+M for all real
x>=1. Existence of one such M is the first Mertens estimate: Terence
Tao, *254A, Notes 1: Elementary multiplicative number theory*,
23 November 2014, Section 2, Theorem 13, equation (22),
[primary source](https://terrytao.wordpress.com/2014/11/23/254a-notes-1-elementary-multiplicative-number-theory/).
L924 proves from it that

    sum_(2<=r<=x) Lambda(r)/phi(r)<=log x+C_*   (real x>=1),

including all prime powers and empty cutoffs. That proof and constant
are reused without a new Mertens proof or constant optimization.

The additional standard inputs are:

- Daniel Leitner, *CO-MAT2 Lecture Notes*, WS2013/14, Section 1.1.1,
  Theorem 1.1.3, printed p2 (PDF p6),
  [Gershgorin circle theorem](https://www.csc.univie.ac.at/files/Numerik_WS13-14/Lecture_Notes2.pdf):
  every eigenvalue of a finite complex matrix A belongs to a closed
  disk centered at a_ii with radius sum_(j!=i)|a_ij|. Use also the
  preceding invariance of eigenvalues under nonsingular similarity.
- David Bindel, *CS6210: Matrix Computations — Theory for SEP and SVD*,
  3 November 2025,
  [Symmetric eigenvalue basics / Variational approaches](https://www.cs.cornell.edu/courses/cs6210/2025fa/lec/2025-11-03.html):
  for a finite Hermitian H and any complex y, y*Hy<=lambda_max(H)||y||^2.
  This follows from the stated Hermitian spectral/Rayleigh theorem;
  repeated eigenvalues are allowed.

These named matrix results are imported, not reproved. Their complete
relevant source inspections and exact arithmetic scope were ready
before this step in
drafts/literature/2026-11-09-logarithmic-gcd-position-sensitive-coercivity.md.

## Conclusion

For every N>=2 and every complex c,

    F_(log N)(c)
      >= -C_* Q(c)+2 sum_(d<=N) phi(d) kappa(d)|B_d|^2
      >= -C_* Q(c).                                      (1)

The same absolute C_* works for all N,c and every real cutoff.
Q(c)>0 for c!=0; the zero vector gives equality at zero. No explicit
numerical M, optimal constant, nonnegative-form assertion or uniform
condition number is claimed.

This improves the locally established coefficient 2 log N in L924
to log N by a finite specialization of the reviewed matrix results.
It is classified REPRODUCTION, with no originality claim beyond the
sources checked. It supplies no moment estimate, longer-multiplier
projection theorem, realization, signed transfer or Xi positivity.
Written 9 November 2026, step232; separate finite audit completed in
step234 below under the stated named imports.

## Proof

Put ell=log N, y_d=sqrt(phi(d))B_d and h_d=1/sqrt(phi(d))>0.
The exact identities of L737, as restated in L924 (5)-(7), give

    Q=||y||_2^2,
    F_A=sum_d (A+2*kappa(d))|y_d|^2-2 Re(y*Ky),             (2)
    K_(d,n)=Lambda(n/d)sqrt(phi(d)/phi(n)) if d|n and n>d,
    K_(d,n)=0 otherwise.

Indeed, (Ky)_d=sqrt(phi(d))C_d, so y*Ky is exactly
sum_d phi(d)C_d conjugate(B_d). K is real and nonnegative, with
zero diagonal. Define H=K+K*=K+K^T. Then H is real symmetric
and Hermitian, has zero diagonal and nonnegative entries, and

    y*Hy=2 Re(y*Ky).                                      (3)

Thus the full factor two in (2) is already present in H.

For each index d, L924 (7) retains the bound

    sum_n K_(d,n) h_n/h_d
      =sum_(2<=r<=N/d) Lambda(r) phi(d)/phi(dr)
      <=log(N/d)+C_*.                                    (4)

This uses phi(dr)>=phi(d)phi(r) and the all-real-cutoff scalar
bound above. The incoming contribution in the same weighted row is

    sum_n K_(n,d) h_n/h_d
      =sum_(n|d,n<d) Lambda(d/n)
      =log d.                                            (5)

In (5), multiplication of the weights cancels the square root in
K_(n,d), rather than giving the totient ratio from (4). This is
the exact weighted column identity of L737 (8), applied at column d.
For d=1 both sides are zero. For N/d<2 the sum in (4) is empty
and its bound still holds. Combining (4)-(5) at the same index gives

    sum_n H_(d,n) h_n/h_d
      <=log(N/d)+C_*+log d=ell+C_*.                        (6)

Let D=diag(h_1,...,h_N). It is nonsingular, and S=D^(-1)HD has
entries H_(d,n)h_n/h_d. Its diagonal is zero; its off-diagonal
entries are nonnegative, so (6) bounds each absolute row sum.
Gershgorin's theorem places every eigenvalue of S in |z|<=ell+C_*.
Similarity gives the same eigenvalues for H, which are real because
H is Hermitian. Consequently lambda_max(H)<=ell+C_*.
We do not assume S is Hermitian or transport its Euclidean quadratic
form through the similarity. Instead, apply the Hermitian Rayleigh
bound to H itself, obtaining for every complex y

    y*Hy<=(ell+C_*)||y||_2^2.                             (7)

Equations (2)-(3) with A=ell and (7) now imply

    F_ell
      =ell||y||^2+2 sum_d kappa(d)|y_d|^2-y*Hy
      >=-C_*||y||^2+2 sum_d kappa(d)|y_d|^2.

This proves the first inequality of (1); kappa(d)>=0 proves the
second. No complex coefficient product has been assigned a sign.
Every matrix and divisor sum used in the specialization is finite.

No division by Q or y is required, so c=0 is included. If Q=0,
positivity of phi(d) forces B_d=0 for every d. The finite inversion
from L737 (11), b_n=sum_(k<=N/n)mu(k)B_(nk), gives c=0. Hence Q>0
for nonzero c without any improved condition-number assumption.

The decisive difference from L924's global norm estimate is the
same-index cancellation log(N/d)+log d in (6). It pays the complete
cross term at coefficient log N with the one absolute remainder C_*.
No numerical trials or spectral approximations are premises. The
independent moment, conditioning, realization and Xi-sign gaps remain.

### Independent finite audit — 9 November 2026, step234

The approved target is exactly (1), with the existing absolute constant,
not a new coefficient threshold or analytic observer theorem. Reuse
the separately approved primary-source coverage in
drafts/literature/2026-11-09-position-sensitive-logarithmic-gcd-audit.md.
Leitner's Theorem 1.1.3 applies to arbitrary finite complex square
matrices and closed Gershgorin disks; nonsingular similarity preserves
their eigenvalues. Bindel's Hermitian spectral/Rayleigh theorem applies
to complex vectors and repeated eigenvalues. Neither result assumes
irreducibility or positive definiteness. These named sources are
imported, not reproved. L924 supplies the already audited scalar
estimate from Tao, Section 2, Theorem 13, equation (22).

**Finite identity and full complex cross term.** Replayed L737
(5)–(11)/step261 and L924 (4)–(7)/step230. For q=gcd(m,n), finite
differentiation of sum_(d|q)J_z(d)=q^z at z=1 gives
sum_(d|q)phi(d)(log d+kappa(d))=q log q. The derivative has the
positive kappa sign. Substituting in the full F_A cancels the two
log d terms against log m+log n. The remaining logarithmic terms
are -C_d conjugate(B_d)-B_d conjugate(C_d), giving (2).
The coefficient of b_(dk) in sum_(r>=2)Lambda(r)B_(dr) is
sum_(r|k,r>=2)Lambda(r)=log k; k=1 contributes zero. Consequently
(Ky)_d=sqrt(phi(d))C_d and y*Ky=sum_d phi(d)conjugate(B_d)C_d.
Taking H=K+K* gives exactly y*Hy=2 Re(y*Ky). No extra factor
one-half or additional factor two enters the estimate. These finite
identities do not use L737's analytic hypotheses.

**Weights at the same index.** For n=dr with r>=2, multiplication
gives K_(d,dr)h_(dr)/h_d=Lambda(r)phi(d)/phi(dr). The Euler-product
ratio phi(dr)/(phi(d)phi(r)) is the product of p/(p-1) over shared
primes, hence at least 1. The outgoing sum is therefore at most
S_phi(N/d)<=log(N/d)+C_* by L924 (4). For the transpose entry
with n|d and n<d, the actual weight is instead

    K_(n,d)h_n/h_d=Lambda(d/n).

There is no residual totient ratio. Summing gives log d by the
divisor formula; the excluded divisor r=1 has Lambda(1)=0.
Both calculations use the same index d, so their sum is bounded by
log(N/d)+C_*+log d=log N+C_*. Separate global maxima would lose
this improvement and are not used.

For every d<=N, N/d>=1. When N/d<2, the outgoing sum is empty
and log(N/d)+C_*>=0. For d=1 the incoming sum and log d are
zero. The column n=1 of K is zero, but its row need not be; H
includes that row correctly. For d=N the outgoing row is empty
while the incoming sum is log N. No coordinate is discarded.

**Constant and spectral interface.** L924's scalar proof retains all
prime powers: their correction to sum Lambda(r)/r is bounded by
sum_p log p/(p-1)^2<=4 sum_(n>=2)log n/n^2<=3 log 2+2.
The geometric-series correction and decreasing integral comparison
are justified there with nonnegative terms. Tao's absolute upper
constant M, increased once for bounded real cutoffs if necessary,
therefore yields C_*=M+3 log 2+2 for every row and N. No large-cutoff
asymptotic substitutes for an all-cutoff bound.

All phi(d)>0, so D=diag(h_d) is nonsingular. Matrix multiplication
verifies (D^(-1)HD)_(d,n)=H_(d,n)h_n/h_d. Its diagonal is zero
and its off-diagonal entries are nonnegative, making (6) its absolute
row bound. Gershgorin places its spectrum in |z|<=log N+C_*.
Similarity passes this statement to H. H is Hermitian, so its real
largest eigenvalue has that upper bound. Rayleigh applied to H and
the original complex y gives (7). The similar matrix is generally
non-Hermitian; no Euclidean quadratic form is transported through D.
This verifies both theorem hypotheses and similarity orientation.

**Return to the original coefficients.** With A=log N, (2)–(3)
and (7) give the first inequality (1), retaining exactly
2 sum_d phi(d)kappa(d)|B_d|^2. Each kappa(d)>=0 since each
log p/(p-1)>0; kappa(1)=0. Dropping only this contribution gives
the second inequality. All arguments hold for arbitrary complex
y,c; no sign is assigned to a complex coefficient product. No
division by y or Q occurs; c=0 yields zero throughout. If Q=0,
each B_d=0. In b_n=sum_(k<=N/n)mu(k)B_(nk), the coefficient
of b_(nr) is sum_(k|r)mu(k), equal to 1 for r=1 and 0 otherwise.
Thus the finite inversion is valid and forces c=0. Strict positivity
of Q on nonzero vectors supplies no uniform coefficient lower bound.

Audit result: (1) passes with exactly the stated C_* for every
integer N>=2 and complex vector, including every real/empty cutoff
occurring in the proof. No argument or dependency correction is
required. This is local verification of an existing specialization,
classified REPRODUCTION, not a new discovery beyond checked sources.
No numerical or mathematical-script evidence is needed. The dyadic
pilot remains parked. Conditioning, moment remainders, realization,
signed transfer and actual-Xi mixed positivity remain unpaid; no RH
candidate is established. Matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage for (1), the totient-weighted specialization,
Gershgorin and the Mertens input has not been checked and is unknown.
No absence claim is made and no Mathlib declaration is imported.
The supporting mathematics is finite divisor inversion, the existing
all-cutoff scalar estimate, diagonal similarity and the named
Hermitian spectral/Rayleigh theorem. Precise primary citations and
all necessary applicability checks are given above.
