# C744x: The fixed mixed uniform-tail lower certificate fails

## Hypotheses

Use C744v's complete single-cell representation on L2(0,ell),
ell=log(3)/2, inner product linear in its first slot. Write
A=D+W0, W0=S+256 C*C, and let T be its complete separation-seven
cross operator, including all sixteen prime powers and the entire
archimedean cross response. The neutral smooth space N has both
moments integral exp(x/2)f(x)dx and integral exp(-x/2)f(x)dx zero.
All original functions are extended by zero.

Retain the exact frozen parameters of C744v/w: P consists of cosine
indices0,...,511, tau=143/100, and the finite complementary output
indices are512,...,65535. Let Q_< denote these outputs and Q_>=
the indices n>=65536. Use C744w's audited raw covariance matrices,
entry-error ledger and infinite-tail bounds, under its explicit
IEEE754 basic-operation, square-root and dot-product error contract.
This computation retains that contract; it is not a formal machine
verification. Exact dyadic rational evaluation below needs only
integer arithmetic once the stored finite matrix is specified.

The analytic response input is Hongmin Li, *Cutoff-free positivity of
localized Weil forms through the (log 11)/2 threshold*,
[paper45, displayed v2, 9 November2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Lemma3.1/(2.1)-(3.4), specialized and audited in C744v/w. Its complete
form comparison(4.7)-(5.5) is the method precedent. The digamma error
input is [DLMF5.11.2](https://dlmf.nist.gov/5.11.E2) and
[5.11(ii)](https://dlmf.nist.gov/5.11#ii), with the exact shifted
arguments and error bounds in C744w. No source numerical positivity,
RH-conditional formula, new coordinate change or new theorem is used.

## Conclusion

The direct independent-profile block has the valid sufficient lower
comparison described below. Its finite Schur residual R_< has a
specific nonzero retained vector v with

    <R_< v,v>/||v||^2 < 51/500 = .102.

Consequently the frozen uniform-tail lower comparison is not positive:

    <(R_< - (7/40)I)v,v>/||v||^2 < -73/1000.             (1)

The scalar charge7/40=.175 bounds the entire omitted covariance;
(1) refutes this sufficient lower certificate, not the actual full
Schur residual, and not the independent-profile inequality

    d(f)+d(g)+2 Re H(f,tau_(7ell)g)>=0,   f,g in N.       (2)

No negative smooth pair was found. The retained direction is a vector
in the penalized cosine comparison, with no exact-neutral or compact
smooth claim; no two normalized H2 norms are therefore asserted.
The sign of(2), composition, other separations, strict H2 slack,
C744q's strict margin, non-neutral coverage and RH remain open.

This is REPRODUCTION of the approved complete-block method with new
local negative certificate evidence, under assessment535 separately
approved in step536. It is not a mathematical discovery claim or an
RH candidate. A separate conceptual audit of this result is pending.

## Proof

### 1. Original two-profile block and the entire complementary floor

In C744v's cross-kernel calculation replace the two occurrences of
f by f and g. Both pole products and the j=0 cross-response product
vanish by the exact moments of each profile. Absolute uniform
convergence on the separated square justifies the remaining sum.
The arithmetic cross term is -a_n integral f(x+7ell-log(n))conj(g(x))dx.
Thus, with no extra factor of two,

    H(f,tau_(7ell)g)=-<Tf,g>.

The closed form on the product of the two diagonal form domains is

    B=[[A,-T*],[-T,A]].                                 (3)

On N times N it equals exactly(2), since each separate moment penalty
vanishes. Bounded W0 and T perturb the diagonal D direct sum, so the
form is closed and semibounded on the domain specified in C744v.
Equality is required only on original smooth profiles; cosine vectors
are not asserted to belong to the causal generator domain.

For the projection P2=P direct-sum P, C744v's complementary D floor
and ||T||<4.71 give

    (I-P2)B(I-P2)>=1.43(I-P2).

Indeed the off-diagonal form is bounded in absolute value by
||T||(||y||^2+||z||^2); S and both penalties are positive. Completing
the square in this product form therefore gives the sufficient
complete Schur residual M-F*F/tau, with M=P2 B P2 and F=(I-P2)B P2.
All these operations are on the already specified form domain.

### 2. Complete mixed covariance and its uniform-tail comparison

Put B0=Q_< W0P, Bc=Q_< (T+T*)P/2, Bg=Q_< (T-T*)P/2.
The finite output part of F is exactly

    F_<=[[B0,-(Bc-Bg)],[-(Bc+Bg),B0]].                   (4)

For a,b in {0,c,g}, write Cab=Ba*Bb. All matrices are real, so
the adjoint here is transpose. The nine stored head/covariance
matrices in C744w include the six raw products used here. Direct
multiplication, without any scalar-phase inference, gives

    (F_<*F_<)11=C00+Ccc+Cgg+Ccg+Ccg*,
    (F_<*F_<)22=C00+Ccc+Cgg-Ccg-Ccg*,
    (F_<*F_<)12=-C0c+C0g-C0c*-C0g*,
    (F_<*F_<)21=((F_<*F_<)12)*.                         (5)

The head is [[M0,-(Mc-Mg)],[-(Mc+Mg),M0]] in the saved notation.
In particular the mixed covariance uses the symmetric Ccg sum;
the scalar phase-family certificate did not establish its sign.

The finite and infinite output ranges are orthogonal, hence
F*F=F_<*F_<+G*G, with G=Q_>= direct-sum Q_>= applied to F.
By C744w(6)-(8), the diagonal part of G has norm at most the
response-tail bound plus the moment-tail bound. Its off-diagonal
part has norm at most the maximum of the two T/T* tail bounds,
each at most prime-tail plus continuous-tail. Therefore

    ||G|| < .495201122 < 1/2,
    G*G/tau <=(25/143)I < (7/40)I.                      (6)

This is a bound on the entire combined operator: every mixed term
inside G*G remains paid. There are no products between the two
orthogonal output ranges. Define R_< = M - F_<*F_</tau. The lower
comparison tested in this attempt is R_<-(7/40)I. The true residual
is R_<-G*G/tau; (6) gives a lower bound, never an equality.

### 3. Error ledger for the new block

The complete audited factors have stored Frobenius norms less than
.586,1.485,1.091. Let b=sqrt((65536-512)*512)*10^-7.
C744w supplies response errors eQ<.000000181 and eH<.000184.
The diagonal-plus-off-diagonal product-space structure of(4) gives

    ||F_<-Fhat_<|| <= eQ+3b =: eF,
    ||Fhat_<|| <= ||Bhat0||_F+||Bhatc||_F+||Bhatg||_F,
    ||M-Mhat|| <= eH+3*512*10^-7 =: eM.                 (7)

The factor3 charges one W0 entry allowance and both Wc/Wg allowances.
There is no additional sqrt(2) loss: a repeated diagonal has the
single-block operator norm, and a two-block off-diagonal operator
has the maximum norm of its two blocks. The same facts bound the
head. All complex vectors are covered by these real operator norms.

The six raw products were computed in127 blocks of512 rows. Their
dot-product bounds are gamma_1024 times the respective factor
Frobenius products, followed by127-step accumulation. Applying
Cauchy--Schwarz over these blocks, the sum of squared factor norms
is below5. Even bounding each covariance error by10^-10, each diagonal
block of(5) costs at most5*10^-10 and each off-diagonal block at most
4*10^-10. The resulting full product-space error, all additions,
head assembly, division by the encoded1.43 and symmetrization are
far below the reserved10^-6. The same ample allowance covers norm
evaluation roundoff. Symmetrization is contractive toward the exact
Hermitian matrix. Thus the exact R_< differs from the saved symmetric
binary64 matrix Rhat by operator norm less than

    eM+[(2 sum||Bhatj||_F+eF)eF+10^-6]/1.43 < .012.     (8)

The calculated value is below.007991. This is inherited analytic
entry control applied to the new block, not a trust assumption
about a computed eigenvalue. The input archive hashes match the
complete independent replay in C744w's step534 audit.

### 4. Exact failed direction and scope of the negative result

Before running, the working note froze a proposed finite floor1/5.
A Cholesky proposal for Rhat-(1/5)I failed. That failure alone is
not evidence of a mathematical sign. An eigensolver then located
a direction, stored in `scripts/separation-seven/mixed-block-failed-direction-537.npz`.
No eigenvalue accuracy is used: every stored vector and matrix entry
is converted by as_integer_ratio to an exact dyadic rational.

The program accumulates all1048576 terms of the quadratic form
using integers and divides by the exact positive squared norm.
More explicitly, it writes v_i=a_i/2^p and Rhat_ij=b_ij/2^q,
with integer a_i,b_ij and common finite exponents, and checks

    sum_ij a_i b_ij a_j / (2^q sum_i a_i^2) < 9/100.     (9)

The complete integers, exact numerator/denominator and comparison
are saved in the certificate. The displayed floating value about
.089797583 is only a locator description. Combining the exact(9)
with(8) gives <R_< v,v>/||v||^2<.09+.012=.102.
Subtracting the frozen.175 proves(1). The proposed.2 floor and,
more strongly, positivity of the stated uniform-tail lower comparison
are impossible. This does not prove a negative value of the true
Schur residual: its actual direction-dependent G*G charge may be
much smaller. Even failure of that sufficient Schur comparison
would not by itself refute(2).

Reproduce, without modifying earlier artifacts:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/mixed-block-certificate-537.py

The full matrices are in `scripts/separation-seven/mixed-block-matrices-537.npz`;
the proof checks, hashes, ledger, exact dyadic evidence and preserved
Cholesky failure are in `scripts/separation-seven/mixed-block-certificate-537.json`.
The earlier failure-locator JSON is explicitly uncertified and is
preserved. No separation, ratio, head size, covariance cutoff, penalty
or denominator was retuned. The bounded attempt ends with the actual
mixed sign and its direction-dependent infinite covariance unresolved.

## Mathlib

Full matching coverage of this mixed localized Weil certificate and
its computational obstruction has not been checked. No absence claim
is made. Block multiplication, Hilbert-space norm bounds, Schur square
completion and rational arithmetic are supporting mathematics, not
an asserted formalization of this result or RH.
