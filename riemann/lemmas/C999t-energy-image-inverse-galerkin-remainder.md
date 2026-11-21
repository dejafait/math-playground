# C999t: The fixed energy-image complement inverse factor is below one

## Hypotheses

Use C744z Sections1-3 on the complex Hilbert space H0=ker C in
L2(0,ell), ell=log(3)/2, with closed restricted form a0, form domain
V0, and selfadjoint representative A0>=c_*I, c_*=8.9e-18. Set
E=A0^-1/2. Retain the original analytic response, IEEE754 binary64
basic-operation/sqrt and directed Decimal contracts, whole-neutral-core
qualification and unreplayed source computation for c_*.

Use C999k's unchanged full-space reference R<=L=D+S+256C*C, with
P the raw cosine projection onto indices0,...,511, Q=I-P, head H,
and complementary form QDQ/2. In particular H>=.239999 I,
QDQ>=6.14Q, and the relation inverse comparison of its Sections1-2
and audit557 are retained under their stated qualifications. All
response/penalty covariance and infinite-output errors used there
remain inputs. This proof does not replay that large computation.

Use C999l's exact Z:C^510->H_512=H0 intersect ran P, finite metric
A=Z*LZ, A>=.779I, and ||Z||<1.008. Import audit561's complete
coefficient conversion and finite-head error bounds. Use C999s's
J=A0^(1/2)Z, J*J=A and W_512=ran J, with P_W its orthogonal
projection in H0. No invariance of H_512 or finite square root of A0
is assumed. Neither C999l's endpoint margin nor C999s's S3 margin
supplies the inverse bound proved here.

Standard inputs, imported without reproof, are Gerald Teschl,
*Mathematical Methods in Quantum Mechanics*, GSM99, author version
12February2009, Theorem1.7/proof p43, Theorem2.13/proof pp71-72,
Theorems3.1/3.2 pp90-92 and (3.25)-(3.27),
[author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf),
and Behrndt–Hassi–de Snoo–Wietsma, *Antitonicity of the inverse for
selfadjoint matrices, operators, and relations*, arXiv1403.5704v1,
Proposition2.1 p4, Theorem3.4's nonnegative proof case p11 and
Corollary3.5 p12, [pinned PDF](https://arxiv.org/pdf/1403.5704v1).
Assessment611, separately approved612 before this attempt, covers
their projection, spectral and relation-order specialization. The
local work is the fixed effective inverse-error comparison;
no new general Galerkin or inverse-order theorem is claimed.

## Conclusion

Under exactly these qualifications,

    E(I-P_W)E = A0^-1-Z A^-1 Z*,                              (1)
    ||E(I-P_W)||^2 <= 1981/2000 = .9905 < 1.                  (2)

The adjoint factor (I-P_W)E has the same norm. This proves the nominated
threshold1 for the fixed W_512, as a local REPRODUCTION/specialization.
The separate conceptual audit615 in Section7 upholds both claims under
exactly the retained qualifications. It removes the
global c_*^-1/2 loss from this factor only; it does not strengthen c_*
or validate its source. Signed separation7/14 mixed couplings, other
norm factors, full endpoint positivity, C744q, H2, non-neutral coverage
and actual-Xi positivity remain unresolved. This is not an RH candidate.

## Proof

### 1. The exact projection and the correct squared norm

The imported restricted spectral calculus gives bounded selfadjoint E
on H0 and E A0^(1/2)f=f for every f in V0. Every column of Z is in
Dom(A0), hence V0, by C999l's strong-domain argument. The finite map J
is bounded, injective and has closed range W_512. Since J*J=A>0,
J A^-1 J* is selfadjoint, idempotent, and has range W_512, so the
orthogonal projection theorem identifies it with P_W.

All following products are bounded and everywhere defined on their
indicated spaces. Spectral calculus on the columns of Z gives EJ=Z.
Taking bounded adjoints gives J*E=Z*. Thus

    E P_W E = (EJ) A^-1 (J*E) = Z A^-1 Z*.

This proves(1) on all H0 without moving E through P_W. For
T=E(I-P_W), T*=(I-P_W)E and

    TT*=E(I-P_W)E >=0,   ||T||^2=||TT*||.                   (3)

In particular the norm in the target has the adjoint orientation in(3).

### 2. Keep the finite-rank subtraction in the full reference order

Let P0 be the full L2 projection onto H0. C999k encodes the restriction
by the nonnegative selfadjoint relation with operator part A0 on H0
and purely multivalued part H0-perp. Its form domain is V0 subset V;
R<=L=a0 on V0. The cited relation inverse order gives
A0^-1 P0<=R^-1 on full L2. Consequently, as bounded operators on H0,

    0<=E(I-P_W)E <= B0,
    B0=(P0 R^-1 P0)|H0-Z A^-1 Z*.                         (4)

Both surrounding projections are present. For x in H0 their quadratic
pairing with x can be removed, without asserting an inverse-compression
identity. Write x=p+y, p=Px, y=Qx. Since ran Z is in ran P,

    <B0 x,x>=<B_h p,p>+<2D^-1 y,y>,
    B_h=H^-1-Z A^-1 Z* on ran P.                         (5)

The whole inverse subtraction remains inside B_h. R<=L on finite
neutral vectors gives Z*HZ<=A. Hence
||H^(1/2)Z A^-1/2||<=1, and conjugation by H^-1/2 gives

    0<=B_h<=H^-1,    ||B_h||<=1/.239999<5.                (6)

These finite positive square roots prove an order statement; they do
not replace the actual E. The complete diagonal tail in(5) satisfies
2D^-1<=100/307 on ran Q. No tail truncation is made.

### 3. Finite neutral-head inequality and complete numerical allowances

Put G=Z*Z. The finite assertion needed is

    Z*B_h Z = Z*H^-1 Z-G A^-1 G <= .99 G.                (7)

Hats below are complete stored dyadic matrices, not exact analytic
entries. Mhat,Chat are C999k's fixed m0,cov00; Zhat,Ahat are the
pinned arrays z,a of C999l/audit561. Define

    Hhat=fl(Mhat-.00024I-(100/307)(Chat+.0046I)),
    Ghat=fl(Zhat*Zhat).

The inherited bounds and the arithmetic ledger below give

    ||H-Hhat||<d_H=10^-8,  ||Z-Zhat||<d_Z=10^-14,
    ||A-Ahat||<=eta_A=.00024395536,
    ||G-Ghat||<d_G=10^-7.                                (8)

The script proposes X,Y from Hhat X=Zhat and Ahat Y=Ghat, then
checks their entire residuals. Their exact stored Frobenius norms
are below100; their complete exact-dyadic equation residual norms
are below10^-6. Therefore

    ||H^-1 Z-X||<=e_X=(10^-6+100d_H+d_Z)/.239999,
    ||A^-1 G-Y||<=e_Y=(10^-6+100eta_A+d_G)/.779.           (9)

For example H(X-H^-1 Z)=(H-Hhat)X+(Hhat X-Zhat)+(Zhat-Z).
The second proof is identical for finite A. No approximate eigenvalue
supplies an inverse bound. Let Bhat be the symmetrized rounded
Zhat*X-Ghat Y. Since ||G||<1.008^2, expansion gives

    ||Z*B_h Z-Bhat|| <= e_B
      =100d_Z+1.008e_X+100d_G+1.008^2 e_Y+10^-7
      =5952684418352310837/186959221000000000000.          (10)

Indeed Z*H^-1Z-Zhat*X=Z*(H^-1Z-X)+(Z-Zhat)*X, and
G A^-1G-Ghat Y=G(A^-1G-Y)+(G-Ghat)Y. The last10^-7 pays
all product/subtraction/symmetrization rounding. Symmetrization
cannot increase distance to the exact Hermitian matrix.

The complete factor proposal is for the symmetrized rounded matrix
Fhat=fl(.99Ghat-Bhat-.05I). Its exact reconstruction by the stored
factor has norm error below10^-6; assembly of this expression from
exact dyadic operands has error below10^-7. Positivity of the factor
times its adjoint and (8)-(10) give

    .99G-Z*B_h Z >= s I,
    s=.05-10^-6-10^-7-.99d_G-e_B
      =3395052467541710163/186959221000000000000
      > .01815 >0.                                      (11)

Thus(7) holds for every complex coefficient vector. Real stored
matrices and factors give the same Hermitian bounds over C.

Here is the arithmetic bridge. Let u=2^-53 and
gamma=gamma_1024=1/(2^43-1). Every contraction has at most512 terms.
Use the inherited bound ||fl(UV)-UV||_F<=gamma||U||_F||V||_F.
Squared Frobenius norms of full stored arrays are computed as exact
sums of squares of dyadic rationals, using Python integers. The
script checks

    ||Mhat||_F<400, ||Chat||_F<1, ||Zhat||_F<23,
    ||Hhat||_F,||Ahat||_F<500, ||Ghat||_F<100,
    ||X||_F,||Y||_F<100,
    ||fl(Zhat*X)||_F<2301, ||fl(Ghat Y)||_F<10001,
    ||Bhat||_F<20000, ||Fhat||_F<20001.

Both computed equation residual norms and the computed full factor
reconstruction norm are below10^-7. The factor's exact squared
Frobenius norm is below90000<100000. Complete allowances are

    solve rounding <=gamma*500*100+u*(500*100+100+1)<10^-7,
    Gram error <=gamma*23^2+d_Z(2*1.009+d_Z)<d_G,
    B assembly <=gamma*(23*100+100*100)+10u*50000<10^-7,
    factor rounding <=gamma*100000+10u*50000,
    10^-7+factor rounding<10^-6,
    F assembly <=10u*50000<10^-7.

Coefficient conversions are included in the last10u*50000 bounds.
For H assembly, the three scalar conversions, diagonal additions,
scalar multiplication and final subtraction use the same norms and
||I||_F<23; the deliberately larger total50u*500<10^-8 covers them.
This also reproduces the inherited H assembly allowance. Ghat is
checked exactly symmetric. Its operator norm is below1.009^2 by(8),
although the coarser Frobenius bound100 suffices for products.
Rounded norm calls, factorization success and matrix previews are
never used as proofs of the required operator inequalities.

### 4. Exact neutrality bounds the remaining raw-head component

In(5), p=Px need not be neutral. Use C999l's exact moment ratios for
every n of parity p0=n mod2, with r_0=r_1=1:

    r_n=(nu_n/nu_p0)(1/4+k_p0^2)/(1/4+k_n^2),
    k_n=n*pi/ell, nu_0=ell^-1/2, nu_n=sqrt(2/ell) (n>0).

The two moment columns at0,1 are independent. Hence x in H0 is
equivalent to the two equations sum_(n of parity p0) r_n x_n=0.
They converge absolutely by Cauchy-Schwarz because the ratio rows
are square summable. Let F_h be these two rows on raw indices0:511
and F_t their complete tail n>=512. Their supports have disjoint
parities and F_h F_h*>=I, since each head row contains coefficient1
at0 or1. In particular ker F_h=H_512 inside ran P.

Orthogonally decompose p=v+w, v in H_512, w perpendicular to H_512
inside ran P. Neutrality says F_h w=-F_t y. The unique solution
in ran F_h* is

    w=-F_h*(F_h F_h*)^-1 F_t y,
    ||w||<=||F_t|| ||y||,                                (12)

because the squared norm of that right inverse is the norm of
(F_h F_h*)^-1<=I. Let t=(ell/(2pi))^2<1/36, using ell<1 and
pi>3. For odd n, r_n=(1+t)/(n^2+t)<2/n^2; for even n>=2,
r_n=sqrt(2)t/(n^2+t)<2/n^2. Thus

    ||F_t||^2 <=sum_(n>=512) r_n^2
       <4 sum_(n>=512)n^-4
       <=4/(3*511^3)=4/400298493<10^-8.

The integral comparison is over [511,infinity), with no sample or
unknown onset. Therefore ||w||<=epsilon||y||, epsilon=10^-4.

### 5. All blocks and the infinite tail give the target

Equation(7) gives <B_h v,v><=.99||v||^2 for every v=Zalpha in H_512,
since ||v||^2=alpha*Galpha. Equations(5),(6),(12) now give

    <B0 x,x> <= .99||v||^2+10epsilon||v||||y||
                    +(100/307+5epsilon^2)||y||^2
       <=(.99+5epsilon)||v||^2
                    +(100/307+5epsilon+5epsilon^2)||y||^2.

Here 2||v||||y||<=||v||^2+||y||^2 pays the mixed raw-head
component. The coefficients are .9905 and
2003070307/6140000000<.9905. Orthogonality gives
||x||^2=||v||^2+||w||^2+||y||^2, so B0<=.9905 I on H0.
Equations(3),(4) prove(2).

### 6. Evidence and limits

Reproduce with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/energy-image-inverse-613.py

Full scalar evidence is `scripts/separation-seven/energy-image-inverse-613.json`;
all proposed matrices, solves, residuals and factor are in the matching
`.npz`. The script pins the exact input archives through audit561,
checks imported bounds, writes every exact norm and inequality,
and prints the threshold, result, failures and artifact paths.
All43 checks pass. The complete checks, final comparison, selected
load-bearing exact value and empty failures were inspected; a preview
is not evidence for the full certificate. The factors are proposals
until the reconstruction and arithmetic estimates above are applied.

This is one fixed N512 test, without tuning or reference/allocation
change. K65536 belongs to the retained reference certificate only;
(12) and the diagonal inverse bound cover every n>=512. Preserve
stops537/598/600/603 and C999r's different-projection ineffective bound.
No signed coupling or inherited source/core qualification is resolved.

### 7. Separate conceptual audit — 12 November2026, step615

**Result and scope.** The invocation-start SPECIALIZE assessment613,
separately approved614, covers exactly this audit. Claims(1)-(2) are
upheld with their original constants, projection, reference and cutoff.
This independently verifies a local standard-method specialization;
it establishes no result beyond the assessed methods, signed endpoint
comparison or RH candidate. All inherited qualifications remain.

**Restricted identity and order.** C999l Section1/audit561 and C999s
Section5/audit611 supply the strong-domain argument: finite Zalpha
belongs to Dom(D), and bounded S and C*C give LZalpha in L2. Testing
against all V0 gives its restricted representative P0LZalpha. Thus
J=A0^(1/2)Z is well defined and J*J=A by the exact restricted form,
not by a compressed square root. Its range is finite dimensional and
closed. The imported projection theorem and spectral calculus, with
the precise citations in the hypotheses, apply on H0 and give
P_W=J A^-1 J*, EJ=Z and J*E=Z*. Taking the adjoint of the bounded
finite map EJ avoids any unbounded-product adjoint assumption.
Consequently the identity is E P_W E=Z A^-1 Z* on all H0.
For T=E(I-P_W), TT*=E(I-P_W)E; it is positive and has norm ||T||^2.
There is no commutation of E with P_W or invariance of H_512.

The relation in Section2 is the selfadjoint orthogonal sum of A0 on
H0 and the purely multivalued part on H0-perp. Its inverse is A0^-1P0
on the full L2 space, including zero action on H0-perp. The audited
reference has form domain V containing V0, and R<=L=a0 on V0.
These are the hypotheses and the direction of the cited nonnegative
relation inverse order. Compression therefore retains BOTH P0 factors
in(4). Subtracting the same bounded Z A^-1 Z* preserves the order;
no inverse-compression identity is used. In a quadratic pairing with
x in H0, P0x=x, and raw P/Q split the block-diagonal R^-1 exactly.
Since Z*Q=0, the subtraction occurs only in B_h, giving(5).

For every alpha, Z*HZ<=A follows by applying the reference form order
to Zalpha. Thus B=H^(1/2)Z A^-1/2 obeys B*B<=I, whence ||B||<=1
and BB*<=I. Congruence with H^-1/2 proves 0<=B_h<=H^-1.
This verifies(6) for the rectangular Z; it does not assume that the
head is all of H0. The whole raw tail obeys 2D^-1<=100/307, using
the inherited diagonal bound on every n>=512.

**Complete finite arithmetic.** Reproduce the independent audit with

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/energy-image-inverse-audit-615.py

The full certificate is
`scripts/separation-seven/energy-image-inverse-audit-615.json`;
its log has the same basename. All original613 artifacts and imported
archives are preserved and hash-checked before and after the audit.
The full saved Z,A agree with the audit561-pinned input. Every matrix
shape, finite real binary64 entry, required exact symmetry, free identity
block and parity-zero row is checked. The large covariance and original
source computations are qualified imports, not rerun or newly validated.

For each stored array, convert EVERY entry to an exact integer over a
common power-of-two denominator. Matrix multiplication then uses Python
integer dot products, and the complete Frobenius square is the exact
sum of squared integer numerators over the squared common denominator.
No floating norm or sampled submatrix certifies a bound; decimal norm
prints are diagnostic only. There is no solve, eigensolver or new factor
proposal in this audit. In particular it independently verifies

    ||H-Hhat||_F<10^-8,
    ||Zhat*Zhat-Ghat||_F<10^-7,
    ||Hhat X-Zhat||_F, ||Ahat Y-Ghat||_F<10^-6,
    ||sym(Zhat*X-Ghat Y)-Bhat||_F<10^-7,
    ||.99Ghat-Bhat-.05I-Fhat||_F<10^-7,
    ||Fhat-FF*||_F<10^-6.

Here F is the entire saved factor, and sym(B)=(B+B*)/2.
The first line reconstructs the exact rational reference as
Mhat-(100/307)Chat-[6671/(307*12500)]I. The Gram line concerns the
dyadic Zhat; the inherited exact-neutral conversion is separately paid.
All complete stored magnitude bounds and both product magnitudes are
checked. Thus factor positivity follows from FF*>=0 plus its FULL
reconstruction, not from Cholesky success. Real matrices establish the
same Hermitian inequalities for all complex coefficients.

The original floating ledger is also checked, including all scalar
conversions. For the solve subtraction, ||fl(Hhat X)||_F is at most
(1+gamma)500*100, so the extra1 in its subtraction allowance covers
gamma*500*100; the same statement applies to Ahat Y. The B and Fhat
assembly allowances include both products, additions and symmetrization.
H assembly uses the exact rational coefficients above. The integer
checks independently verify these actual fixed operations, while the
original binary64/Decimal contracts remain necessary for inherited inputs.

The conversion estimate d_Z together with ||Z||<1.008 gives
||Zhat||<1.009. Expanding Z*Z-Zhat*Zhat and adding the complete Gram
product error proves d_G in(8). Substituting the qualified finite floors
.239999 and .779 into both residual equations gives exactly(9).
The expansions in(10) retain the exact Z and G on the inverse-error
factors. Symmetrization is contractive in operator norm and fixes the
exact Hermitian target. The audit recomputes exactly

    e_B=5952684418352310837/186959221000000000000,
    s=3395052467541710163/186959221000000000000>.01815.

Every term of(11), including .99d_G, factor reconstruction and trial
assembly, is deducted. Hence(7) follows on the entire finite complex
coefficient space. The .779 floor is used only for finite A.

**Entire neutral space and final mixed term.** The two exponential
moments are bounded L2 functionals. Their cosine coefficients are the
two independent parity base columns times r_n. Since each ratio row
is square summable, the two moment equations extend from finite sums
to every x in L2, with absolute convergence by Cauchy-Schwarz. The
independent columns at0,1 therefore give the exact equivalence used
in Section4. Both parities occur in F_h, with their unit entries,
so F_h F_h*>=I. The orthogonal decomposition p=v+w has
w in ran F_h*, and the stated right inverse is its unique solution.
Its squared norm is ||(F_h F_h*)^-1||<=1, proving(12) also for
complex coefficients.

For t=(ell/(2pi))^2<1/36, the odd ratio is
(1+t)/(n^2+t), and the even ratio for n>=2 is
sqrt(2)t/(n^2+t). Both are <2/n^2. The integral of u^-4 on
[511,infinity) therefore pays EVERY n>=512, with

    ||F_t||^2<=4/(3*511^3)=4/400298493<10^-8.

No finite neutrality residual or cutoff replaces this bound. In(5),
the head contribution expands into v,w, so its mixed term costs at
most 2*5||v||||w||<=10epsilon||v||||y||, and its w-square costs
5epsilon^2||y||^2. Section5 pays both terms before using the orthogonal
norm identity ||x||^2=||v||^2+||w||^2+||y||^2. The resulting exact
coefficients are1981/2000 and2003070307/6140000000, with the second
strictly smaller. Thus B0<=1981/2000 on all H0, proving(2).

All105 independent checks pass. The complete exact residual squares,
assembly errors, factor reconstruction, scalar ledger and final bounds
were inspected; previews do not substitute for these checks. No new
mathematical input or DAG edge is needed. Stops537/598/600/603 and
C999r's different projection are unaffected. Signed complement and
mixed blocks, other norm factors, original core/c_* validation, C744q,
H2, non-neutral coverage and global actual-Xi positivity remain open.

## Mathlib

Full matching Mathlib coverage for this numerical restricted-operator
statement is not checked. The assessment imports the named projection,
closed-form, spectral-calculus and relation-order theorems above;
generic formal projection or positive-matrix results would not verify
this finite certificate and infinite-moment specialization.
