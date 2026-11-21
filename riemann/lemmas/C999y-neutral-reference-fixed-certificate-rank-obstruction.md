# C999y: Two exact moments cannot repair the unchanged598 lower matrix

## Hypotheses

Use C999k's unchanged positive selfadjoint reference R on the complex
Hilbert space H=L2(0,ell), ell=log(3)/2. Its form domain is V, its raw
head0:511 is the exact rational H of that result, and its complement is
D/2. In particular R>=.239999 I and B=R^-1 is bounded, positive and
injective; R itself is unbounded. Use C999k's two bounded moments
C:H->C^2, C_c(f)=integral_0^ell exp(c x)f(x)dx, c=+/-1/2.
Put H0=ker C, V0=V intersect H0, and use C744z Section1's density of
V0 in H0. Retain the complete original D,S,T,T*,U and the exact neutral
coordinate map Z on raw0:1023 from C999q Section1.

The fixed endpoint family is f=Z alpha, h=Z beta, with independent
complex alpha,beta in C^1022. For x=(alpha,beta), let

    A=Z*LZ, J=Z*[TZ,T*Z], g_G=ZA^-1Jx,
    F x=rho_G=Tf+T*h-Lg_G, L=D+S+256C*C.

The finite A is positive under certificate598's retained contracts;
the exact Galerkin map, rather than its saved dyadic proposal, defines F.
All columns of ZA^-1J lie in Dom(L); bounded T,T* imply F:C^2044->H is
bounded. C999k's full reference and C999q's general strong-trial/form-order
argument apply to this finite family. The inherited analytic-response,
IEEE754/Decimal, whole-neutral-core and unreplayed c_* qualifications
remain in force for its interpretation as an actual-form bound. They
are not needed for the exact finite-matrix rank obstruction below.

Define M598 to be the EXACT dyadic array `comparison_lower` in
`scripts/separation-seven/joint-galerkin-family-certificate-598.npz`,
SHA256 `f5035b5e28bf85b7b8329a6675f910a8545208ad931bb983938ee14f30970876`.
Keep every entry, including all finite/infinite-output, trial and
exact-predictor allowances. Its associated JSON is SHA256
`42a2b96a000ec519cb926a752e32bf364c3e880cfb06436d59a6ecc4cdbfb290`;
the supplementary ledger JSON is SHA256
`d531db86b4b1c98ae9e41a9c973d8d5528336c7e6e6b0649c921b16df587dce2`.
The old final-factor failure remains recorded. This result does not
upgrade598's lower-enclosure validity to an independent analytic audit.

## Conclusion

Let R0 be the selfadjoint operator on H0 represented by R's form
restricted to V0, and P0 the orthogonal projection onto H0. Then, as
bounded operators on the full H,

    R0^-1 P0 = B - B C*(C B C*)^-1 C B.                   (1)

The saving Delta=B C*(C B C*)^-1 C B is positive of rank exactly two.
Thus Gamma=F*Delta F is positive of rank at most two, including the
FULL infinite residual, with no moment-tail truncation.

For t=999/10^6, there is a specified dyadic injection X:C^3->C^2044
such that the exact matrices satisfy

    X*X > .999 I3,
    -X*(M598-tI)X > .08 I3.                              (2)

Consequently M598+K is NOT >=tI for ANY Hermitian K of rank at most
two, including the ideal exact Gamma. Retaining this same lower matrix
and adding only the two-moment saving cannot certify the desired floor.
No numerical evaluation of the infinite moment Gram or residual tails
is needed for this necessary rank test.

This is a standard-method specialization with a new local negative
decision for the fixed repair, not a new general shorting theorem or
a counterexample to the actual comparison. A lower matrix below tI
gives no upper bound on the actual form. Sharper independently justified
enclosures, other references, actual S3, higher endpoints, mixed signs,
C744q, H2, non-neutral coverage, source/core/c_* validation and the
global actual-Xi/RH gap remain unresolved. The separate conceptual
audit642 in Section4 upholds the result under these qualifications.

## Proof

### 1. Imported results and the restricted-form specialization

Import the bounded shorting theorem from Corach--Maestripieri--Stojanoff,
[*Oblique projections and Schur complements*, arXiv:math/0006120v1,
16June2000](https://arxiv.org/pdf/math/0006120v1), Proposition3.3/proof
p6 and Theorem4.1 pp9-10, Proposition4.2/full proof p10. The closed-form
representation/domain results are Teschl, *Mathematical Methods in
Quantum Mechanics*, GSM99, [author version12February2009](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
Theorems2.13/2.18 pp71-72/77. Reuse the precise hypotheses/proof cases
inspected in assessments611/619/638/639; these general theorems are
not reproved. The following local domain/compatibility calculation is
necessary because the bounded theorem applies to B, not unbounded R.

The two moment functionals are independent: C*z=0 would mean
z_+ exp(x/2)+z_- exp(-x/2)=0 almost everywhere. This continuous
function is then zero everywhere in the interval; multiplying by
exp(x/2) and evaluating at two distinct points gives z_+=z_-=0.
Hence C* is injective. Put G=C B C*. For nonzero z,

    <Gz,z>=||B^(1/2)C*z||^2>0,

since B is positive injective and so is B^(1/2). Thus the finite
two-by-two G is positive definite, and its bounded inverse exists.
Define S=ran C*, a closed two-dimensional subspace, and

    E=C*G^-1 C B.

One checks E^2=E, E C*=C*, ran E=S, and
BE=E*B=B C*G^-1 C B. Thus E is a B-selfadjoint projection onto S,
which verifies compatibility in the cited theorem. Proposition4.2
identifies the short of B to S-perp=H0 as B(I-E).

It remains to identify that short with the inverse of the restricted
FORM, rather than assuming a projected inverse identity. The form r
of R is closed and coercive on V. Since C is bounded on H and the
form norm dominates the H norm, V0 is closed in that form norm.
It is dense in H0 by the stated C744z input. Representation gives
R0>=.239999 I on H0 and a bounded inverse there.

For arbitrary rho in H set

    w=B rho-B C*G^-1 C B rho.

Both terms lie in Dom(R), because B maps all H to Dom(R). Also
Cw=C B rho-GG^-1 C B rho=0. Thus w lies in V0, and

    Rw=rho-C*G^-1 C B rho.

For every v in V0 the last term pairs to zero, because Cv=0;
therefore r(w,v)=<rho,v>=<P0 rho,v>. The unique coercive weak
solution is w=R0^-1 P0 rho. This proves (1), including its entire
form domain. No commutation with P0 or closed range of B is assumed.

Writing U=B C*, Delta=UG^-1U* proves positivity. U is injective
from C^2 since B and C* are injective, so rank Delta=2. Composing
with the complete bounded residual map F proves rank Gamma<=2.
The rank bound concerns the exact entire map, not a truncated Gram.
Since R|V0<=L|V0, the same inverse-order application as C999k on
H0 allows the stronger residual upper bound <R0^-1P0rho,rho>.
Equivalently the unrestricted-reference comparison is increased by
the exact Gamma. Inverse order is the imported Behrndt--Hassi--de
Snoo--Wietsma, [arXiv:1403.5704v1](https://arxiv.org/pdf/1403.5704v1),
Proposition2.1 p4, Theorem3.4 nonnegative case p11, Corollary3.5 p12,
with the same restriction/domain qualifications as C999k/q.

### 2. Complete exact compression certificate

Reproduce from the active notebook with

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/neutral-reference-rank-obstruction-640.py

Full evidence, including all96 integer vector coordinates, is
`scripts/separation-seven/neutral-reference-rank-obstruction-640.json`.
The script pins the598 source/archive/certificate/ledger and every
inherited598 input before calculation and preserves the original failure.
All finite-matrix arithmetic used for certification is Python Fraction
on exact integers. There is no rounding allowance or eigenvalue premise.

The three columns of X have denominator2^24 and zero entries outside
the explicitly listed support

    {0,...,15,1022,...,1037}.

The support lies in the FULL2044 free coordinates, using both endpoint
copies of free modes2:17; it imposes no endpoint symmetry. The saved
32-by-three integer array defines X completely. An eigensolve on this
principal32-square merely proposes that array; arbitrary proposals
are acceptable only if the subsequent exact checks pass. Symmetry and
finiteness of the full pinned M598 are checked before use. Since every
omitted coordinate of X is exactly zero, its compression of M598 is
exactly the principal-support product, with no discarded matrix term.

The script computes every entry of G_X=X*X and
A_X=X*(M598-tI)X exactly. It records the COMPLETE two matrices and
their exact diagonal-dominance lower bounds:

    min_i[(G_X)_ii-sum_(j!=i)|(G_X)_ij|]
      =281474955222765/281474976710656 > .999,

    min_i[(-A_X)_ii-sum_(j!=i)|(-A_X)_ij|]
      =72695772437179941380714963210255091 /
       811296384146066816957890051440640000 > .08.

The displayed decimals .999 and .08 mean exact rationals. For any
complex z in C^3 and real symmetric N, expanding z*Nz and using
2|z_i||z_j|<=|z_i|^2+|z_j|^2 gives

    z*Nz >= sum_i [N_ii-sum_(j!=i)|N_ij|]|z_i|^2.

Apply this elementary inequality to both exact matrices. It proves (2)
over the complex field and proves independence of all three columns.
Three separately negative Rayleigh quotients are not used. The full
certificate's checks all pass and its failures array is empty.

### 3. Rank-nullity stop and its scope

This is the elementary specialization of standard rank-perturbation
interlacing; see Higham's author exposition,
[*Eigenvalue inequalities for Hermitian matrices*,9March2021](https://nhigham.com/2021/03/09/eigenvalue-inequalities-for-hermitian-matrices/),
the complex Hermitian Courant--Fischer/Weyl statements and general
rank-r displays. No proof is imported from that proof-free exposition;
the particular rank-nullity argument is given here.

For any K of rank<=2, KX:C^3->C^2044 has a nonzero kernel
vector z. By (2), x=Xz is nonzero and Kx=0. Consequently

    x*(M598+K-tI)x=z*A_X z<-.08||z||^2<0.

This proves the asserted impossibility, even if K is not positive.
In particular it covers the ideal positive exact Gamma, without
evaluating any infinite tail of G or F. An erroneous or lossy LOWER
enclosure is still not an upper estimate for the actual corrected
form. The test therefore stops only adding this rank-two saving to
the SAME saved lower matrix, and licenses no conclusion about the
actual comparison's sign or a different fully justified enclosure.

### 4. Separate conceptual audit — 12 November2026, step642

The invocation-start SPECIALIZE assessment640, separately approved641,
licenses this audit only. The source statements and proof cases in
Section1 were reused from638/639 and611/619 without repeat browsing.
This is REPRODUCTION of a standard-method specialization, not a new
general theorem or a mathematical discovery beyond those sources.

**Domains and weak identification.** C744z Section1's cutoff estimate
and fixed two-bump correction prove that V0 is dense in H0; continuity
of C for the form norm makes V0 closed in V. The two facts concern
different norms and are both needed. Restricting the closed coercive
form therefore gives R0 on H0, with the same .239999 lower bound.
Because R has a bounded everywhere-defined inverse, B(H)=Dom(R).
For every rho in H the displayed w in Section1 is consequently in
Dom(R) intersect H0, and testing against every v in V0 gives the
stated weak equation. Uniqueness identifies R0^-1 P0 on ALL H.
This proves an operator identity, not merely equality on finite cosine
tests. Neither B's range being closed nor commutation with P0 is used.

Independence of the two continuous exponentials proves C* injective;
injectivity and positivity of B give G>0. Thus every inverse in E and
Delta is a finite positive inverse. The identities E^2=E, EC*=C*,
BE=E*B verify precisely the compatibility required for the cited
bounded shorting theorem with S=ran C*. They do not apply it to R.
Writing U=BC*, U* is onto C^2 since U is injective with finite-dimensional
domain. Hence ran(UG^-1U*)=ran(U) has dimension two. This supplies the
exact rank, not just an upper bound inferred from the number of moments.

The strong-domain obligation belongs to the columns of ZA^-1J: they
are finite cosine sums, and bounded S,C give Dom(L)=Dom(D). Applying
L to each is legitimate. Bounded T,T* and finite source dimension
then give the entire residual F as a bounded map into H. No assertion
F(C^2044) subset Dom(L) is needed; the Hypotheses now disambiguate that
point. Delta is bounded on H, so F*Delta F is positive with rank at
most two without truncating output modes or moment tails.

On H0 the two closed forms satisfy r0<=a0 with common domain V0.
The cited inverse-order theorem gives A0^-1<=R0^-1 there, with the
direction required for an upper residual debt. Thus replacing B by
R0^-1P0 adds exactly Gamma to the same trial comparison. This uses
the original R<=L and analytic/arithmetic contracts; it does not
independently validate their certificates, the whole neutral-core
construction or the original c_* computation.

**Independent exact check.** Run from the active notebook:

    python3 scripts/separation-seven/neutral-reference-rank-audit-642.py

The full evidence is
`scripts/separation-seven/neutral-reference-rank-audit-642.json`.
This checker uses the saved96 integers, not a new eigensolve or a
regenerated640 report. It lifts all1024 entries of the selected32-square
dyadic matrix to common denominator2^62, contracts with the integer
columns and divides only afterward. All nine Gram entries, all nine
shifted-compression entries and all six alternate principal minors
match640 exactly. All three row bounds for both matrices are saved.
Their minima equal the exact fractions displayed in Section2; in
particular they exceed .999 and .08 strictly (approximately
.9999999236596757 and .08960445757896007, respectively). The exact
threshold is999/10^6. The two support ranges lie in distinct endpoint
copies; zero extension to2044 means no omitted cross term. Real
symmetric matrices with these strict row bounds are positive over C,
by Section2's quadratic inequality, so X is a complex injection.

The checker verifies the full598 array's dimensions, finiteness and
symmetry; all three canonical hashes;640 and598 executed-source pins;
every598 inherited input; and the ledger/certificate cross-pins. It
retains the original `quarter_comparison factor unavailable` failure.
Inspection of598's full source and ledger confirms that its quarter
metric is zero: the requested target here is the Euclidean floor.
Its unchanged array includes the trial, head solve, all finite-output,
entire-tail and exact-predictor allowances. Retaining the pinned array
retains every allowance; they were not recomputed or reduced. Recorded
598 ledger checks are provenance evidence, not a new analytic audit.
All642 arithmetic checks pass and its failures array is empty; all
original artifacts remain byte-for-byte unchanged.

**Inference and route.** For any rank-at-most-two K, the map KX has
a nonzero kernel vector over C. Independence of X makes its image
nonzero, while the full shifted compression is strictly negative on
it. This verifies the universal rank-nullity step, including the ideal
Gamma. It does not rely on individual Rayleigh quotients, approximate
eigenvalues, or positivity of K. Even a defective lower enclosure is
still not an upper bound on the actual form. Therefore the audited
stop concerns only adding this saving to the SAME598 matrix. It does
not refute actual S3, other enclosures or RH, and does not reopen the
parked600/603/635 prescriptions. The exact finite stop itself needs
none of598's analytic assumptions. No full RH candidate is asserted.

## Mathlib

Full matching Mathlib coverage for this unbounded restricted-form
identity, its local exact moment specialization and the fixed2044
certificate has not been checked. The cited standard shorting,
closed-form and inverse-order results are mathematical inputs; their
presence in Mathlib is not asserted. Exact rational arithmetic here
is an informal certificate, not a Lean verification.
