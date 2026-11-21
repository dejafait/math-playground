# C999s: A normalized margin on the fixed energy-image endpoint head

## Hypotheses

Use exactly C744z Sections1-3 and its bounded endpoint operator S3 in(4),
on H0 direct-sum H0, with ell=log(3)/2, H0=ker C in complex L2(0,ell),
restricted closed form a0 on V0 and self-adjoint representative A0>=c_*I.
Use C999l's fixed exact neutral map Z:C^510->H_512, its complete finite
metric A=Z*LZ, L=D+S+256C*C, and its audited inequality(2):

    Q_min(Z alpha,Z beta)>=.000999 (||alpha||^2+||beta||^2).

Here H_512=H0 intersect span(e_0,...,e_511); alpha,beta are independent
complex vectors. Q_min minimizes over the entire neutral middle form
domain; it retains the actual U and every induced middle product.

Retain all C999l qualifications: the analytic response identity,
IEEE754 binary64 basic-operation/sqrt and directed Decimal contracts,
whole-neutral-core qualification, and unreplayed source computation
c_*=8.9e-18. This does not validate those inputs or strengthen c_*.
C999l Section7/audit561 is imported as an existing qualified result;
its large residual certificate is not replayed here.

The standard results are imported from Gerald Teschl, *Mathematical
Methods in Quantum Mechanics*, GSM99, version12February2009,
Theorem2.13 and Lemma2.14, pp71-73, Theorems3.1/3.2, pp90-92,
including(3.24)-(3.27), and Theorem3.7, p96,
[author PDF](https://www.mat.univie.ac.at/~gerald/ftp/book-schroe/schroe.pdf).
Closed-form representation and spectral calculus identify the actual
square-root coordinates and their norm. The finite metric comparison
is the generalized complex Hermitian type1 normalization in Anderson
et al., *LAPACK Users Guide*, third edition, SIAM1999, Table2.13,
[computational routines](https://netlib.org/lapack/lug/node54.html), and
[Section4.10](https://netlib.org/lapack/lug/node98.html).
Their approximate numerical error estimates are not used as rigorous
certificates. Assessment608, separately approved609 before this attempt,
covers this fixed specialization; no general theorem is reproved.

## Conclusion

Set W_512=A0^(1/2)H_512, and let P_W be the L2 orthogonal projection
in H0 onto W_512. Under precisely the retained qualifications,

    <S3 (xi,zeta),(xi,zeta)>
        >=.00014 (||xi||^2+||zeta||^2),   xi,zeta in W_512.       (1)

Equivalently, the compression of S3 to W_512 direct-sum W_512 is
at least .00014 times its identity in its actual L2 metric. The separate
conceptual audit611 in Section5 upholds this local REPRODUCTION under
the retained contracts. It is not mathematics beyond the assessed methods.

No invariance of H_512 under A0 or its square root is assumed.
There is no finite inverse square root, new scalar floor for A0,
band-margin transfer or C999r complement transfer. Complement and
mixed-block control for P_W, source/core validation, C744q, H2,
non-neutral directions and actual-Xi positivity remain unresolved.

## Proof

### 1. Identify exactly the energy image and its complete metric

C999l Section1 shows that Z is a complex-linear bijection onto the
exact raw neutral head H_512. Every finite vector in that image lies
in V0 and in Dom(A0). C744z's restricted-form representation gives

    a0(f,f)=||A0^(1/2)f||^2,       f in V0.

Thus J=A0^(1/2)Z is defined, injective, and has range exactly W_512.
In particular W_512 is finite dimensional and closed. The metric is

    ||J alpha||^2=a0(Z alpha,Z alpha)=alpha* A alpha,             (2)

where A is exactly C999l(3). The moment penalty vanishes on ran Z;
the response S is its entire single-cell response, including j=0.
Polarization identifies J*J=A. The positive definiteness of A is
also independently available from C999l's finite bound A>=.779 I;
that bound is not substituted for the full-domain c_* qualification.

C744z(3)-(7), minimized over its entire middle form domain, identify

    <S3(J alpha,J beta),(J alpha,J beta)>
                   =Q_min(Z alpha,Z beta).                     (3)

This equality uses the actual restricted A0 and its full inverse
in the middle minimization. It neither requires J to preserve the
raw head nor replaces full middle products by compressed products.
Both arbitrary complex endpoints are covered by C999l(2).

### 2. Pay the full finite-metric upper bound

The following are imported from C999l Sections2,6,7, with complete
factor reconstruction and allowances already upheld in audit561:

    ||Z||<1.008,    ||Z-Zhat||<=||Z-Zhat||_entry-L1<10^-14,
    ||Mhat Zhat||<6.190001,
    ||Mhat||_F<400,    ||Zhat||_F<23,
    ||A-Ahat||<=eta_A=.00024*(1.008)^2+10^-7
                         =.00024395536.                        (4)

Mhat is the saved COMPLETE head of L, not D or a fixed response
prefix. Ahat is the saved assembly fl(fl(Zhat^t Mhat)Zhat). The
bound on Mhat Zhat refers to the exact dyadic product: its proposed
6.19^2 I-(Mhat Zhat)^t(Mhat Zhat) factor was fully reconstructed,
with error<10^-6; the enlarged6.190001 already includes that error
and operand assembly. Zhat is real, so transpose equals adjoint;
all norm inequalities extend to complex free coefficients.

For explicitness, bound the remaining Ahat assembly using the same
imported arithmetic contract. Put u=2^-53 and

    gamma=1024u/(1-1024u)<1.2*10^-13.

Each inner product has at most512 terms. The standard product ledger
used in C999l gives ||fl(BC)-BC||_F<=gamma ||B||_F||C||_F.
Also ||Zhat||<1.008+10^-14<1.009. Writing
P=fl(Zhat^t Mhat), its first error is less than

    e1=gamma*23*400,
    ||P||_F<23*400+e1<9201.

The second product error is less than e2=gamma*9201*23. Hence

    ||Ahat-Zhat^t Mhat Zhat||
         <=e1*1.009+e2<10^-7.                                  (5)

The Frobenius bounds dominate operator norms in(5). No computed
eigenvalue or uninspected matrix sample is used in this conversion.
The exact dyadic product satisfies

    ||Zhat^t Mhat Zhat||<=1.009*6.190001.

Combining with(4)-(5) yields the certified rational bound

    ||A||<1.009*6.190001+10^-7+.00024395536
          =6.24595506436<7.                                    (6)

The allowance eta_A covers the exact-neutral conversion and all
original head errors. The extra10^-7 in(5) only overpays the saved
assembly comparison; no error is subtracted or silently omitted.
Equation(6) bounds the full energy metric on the fixed head, with
no response truncation or claim about an infinite metric norm.

### 3. Apply the standard finite Hermitian metric comparison

For t=(alpha,beta), let w=(J alpha,J beta). Equations(2),(6) give

    ||w||^2=alpha* A alpha+beta* A beta<=7||t||^2.

By(3) and the imported C999l inequality,

    <S3 w,w>>=.000999||t||^2
                >=(.000999/7)||w||^2
                >=.00014||w||^2,

since7*.00014=.00098<.000999. Every w in W_512 direct-sum W_512
has exactly this parametrization, so(1) follows, including w=0.
This is the explicit applicability argument for standard finite
metric normalization; it does not assert that finite norm equivalence
alone proves positivity or says anything about the orthogonal complement.

### 4. Scalar certificate and verification scope

Run from this notebook:

    python3 scripts/separation-seven/energy-image-margin-610.py

The certificate is `scripts/separation-seven/energy-image-margin-610.json`.
All eight checks pass using exact rational arithmetic. It records the
complete assembly error1104529/43980465111035<10^-7, full metric bound
156148876609/25000000000=6.24595506436<7, positive chosen margin7/50000,
all actual/required bounds, input hashes and failures (none). The complete
checks and rational-values fields were inspected. This script verifies
only these scalar consequences of C999l's imported bounds; it does not
replay audit561, validate its execution contract, or constitute an
independent proof audit of the coordinate identification. Section5 supplies
that separate audit. Those limitations do not enlarge the conclusion.

### 5. Separate conceptual audit — 12 November2026, step611

**Result and scope.** The unchanged invocation-start SPECIALIZE
assessment608, approved609, covers exactly this audit. Inequality(1)
is upheld with its original constant and every inherited qualification.
The audit validates the local specialization, not a new theorem beyond
the inspected sources. No change to the family, reference, predictor,
floor, matrix allocation or projection was made.

**Restricted coordinates and full middle.** C999l Section1 proves
ran Z=H_512 by independence of the two moment columns and exact parity
completion. It works over C; the independent endpoint dimension is1020.
For each f=Zalpha, finiteness of its cosine expansion puts f in Dom(D).
Since S and C*C are bounded, Lf is in L2. For every v in V0,
a0(f,v)=<P0Lf,v>. The representation theorem in C744z Section1 therefore
puts f in Dom(A0), with A0f=P0Lf. This argument proves the strong-domain
assertion used above without any invariance or causal-generator claim.

C744z's spectral calculus makes A0^(1/2):V0->H0 a bijection with
inverse E=A0^-1/2, under the retained c_* qualification. Restricting it
to ran Z makes J injective with range exactly W_512. The norm identity
and polarization give J*J=A, not a finite approximation to A0 or its
square root. Thus the two endpoint L2 norms have exactly the metric(2).
The entire response, including its single-cell j=0 term, is present;
only the exactly zero moment penalty disappears on ran Z.

For w=(Jalpha,Jbeta), C744z(3) has middle energy coordinate y ranging
over all H0, because the original middle ranges over all V0. Its square
has minimum zero at y=R Jalpha+R* Jbeta. The remaining expression is
precisely <S3w,w> with both defects and V14+R^2. This verifies(3),
including attainability of the full middle minimum. It does not minimize
over a finite middle space. In the first-slot-linear convention,
<Rx,R*z>=<R^2x,z>, so no conjugation or orientation is lost.

**Complete metric arithmetic.** C999l Sections2/6/7 and audit561 are
imported qualified results. Their complete factor reconstruction for
the head product has error below2.228e-7<10^-6, including operand
assembly. Moreover

    (6.190001)^2-(6.19)^2=.000012380001>10^-6.

Thus the enlarged bound applies to the exact dyadic Mhat Zhat, not
merely its rounded product. The complete exact-neutral conversion is
<10^-14 in entry L1, which bounds the operator norm; hence
||Zhat||<1.009. The full metric error is exactly the imported allowance
eta_A=.00024395536; it includes the complete head response errors.

The stored assembly in559 is left-associated Zhat^t Mhat Zhat. Both
products have512-term contractions. With gamma_1024=1/(2^43-1), its
two-product bound is exactly

    gamma_1024[9200*(1009/1000)+9201*23]
       =1104529/43980465111035<10^-7.

The first intermediate Frobenius bound9201 is valid since
9200+9200*gamma_1024<9201. Consequently(5)-(6) pay the complete
assembly and all imported errors, even if part of the rounding is
overpaid in eta_A. Positive definiteness is supplied by the restricted
form (also by C999l's finite floor), not by assuming the target sign.
Real stored matrices act on complex coefficients with the same operator
norms; the full Hermitian comparison is therefore valid for both endpoints.

**Normalization and independent evidence.** From the verified metric
bound, ||w||^2<=7||t||^2. The direction of the comparison is correct:
.000999||t||^2>=(.000999/7)||w||^2, and the coefficient slack is
.000999-7*.00014=.000019>0. The zero vector is included by equality.
This proves the claimed compression bound, without any claim for P_W's
orthogonal complement or its mixed blocks.

The separate exact-rational checker is

    python3 scripts/separation-seven/energy-image-margin-audit-611.py

Its full evidence is `scripts/separation-seven/energy-image-margin-audit-611.json`.
All40 checks pass: the eight original inequalities are independently
recomputed, every stored rational value is matched, the selected complete
factor/conversion/metric allowances are checked, and the610 input hashes
and559 pin from audit561 agree. The complete checks and exact-values
fields were inspected; no preview is used as proof. The checker imports
audit561 rather than replaying its large covariance and matrix factors.
Its scalar success is accompanied by the domain and operator argument
above; hashes alone do not prove those claims or validate source contracts.

No error requiring a changed conclusion was found. The tiny c_* source,
neutral-core and analytic/execution contracts remain qualifications.
Stops537/598/600/603 and C999r's ineffective different-projection bound
are unchanged. C744q, H2, non-neutral coverage and actual-Xi assembly
remain open; this is not a complete candidate argument.

## Mathlib

Full matching coverage for this qualified energy-image compression and
numerical certificate has not been checked. No absence claim is made.
Closed-form representation, spectral calculus, matrix/operator norms
and finite Hermitian metric normalization are supporting results,
not an asserted matching formal proof or a global sign theorem.
