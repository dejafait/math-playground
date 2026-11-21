# C999u: The fixed signed energy-image reference comparison fails

## Hypotheses

Retain C744z's complex H0=ker C, restricted A0>=c_*I, E=A0^-1/2,
ell=log(3)/2 and its exact bounded S3. Use C999t's N512, Z,A,
W_512=ran(A0^(1/2)Z), orthogonal projection P_W and the WHOLE positive
operator

    B0=(P0 R_ref^-1 P0)|H0-Z A^-1 Z*.

Here R_ref is C999k's unchanged full-L2 reference: head H on raw
cosine modes0:511 and diagonal D_n/2 on n>=512, D_n=h(n*pi/ell).
In particular ||R_ref^-1||<5. Do not confuse this reference with
C744z's normalized separation7 operator. C999t(4)-(6) give

    0<=E(I-P_W)E<=B0,
    B_h=H^-1-Z A^-1 Z* on the raw head, 0<=B_h, ||B_h||<5.  (1)

Use the COMPLETE T,U of C744v/C744z, with ||T||<4.71, ||U||<30,
and positive single-cell response S>=0. Retain C999n's exact fixed
independent endpoints and audited one-sided inverse estimate. Its
free coordinates y_f,y_h are the1024 integers `free_numerators`
in `scripts/separation-seven/endpoint-complement-locator-581.npz`,
divided by2^40, on512:1023. No integers or operators are optimized here.

All original analytic-response, IEEE754/Decimal, whole-neutral-core
and unreplayed c_*=8.9e-18 source qualifications remain hypotheses.
The result is conditional on these contracts, without revalidating
them. Assessment615, saved before this invocation as SPECIALIZE,
covers exactly this fixed REPRODUCTION attempt and witness test.

The standard bounded factorization input is R. G. Douglas,
*On majorization, factorization, and range inclusion of operators on
Hilbert space*, Proc. AMS17(2)(1966),413-415, Theorem1/full proof
pp413-414, DOI10.1090/S0002-9939-1966-0203464-1,
[published scan](https://home.agh.edu.pl/~rudol/Operat/DouglasFactorizationLemma.pdf).
For bounded operators X,Y on a real or complex Hilbert space,
XX*<=YY* yields X=YC with ||C||<=1, including nonclosed ranges.
Import this theorem; no new factorization theorem is claimed.
C999k/t already justify the restricted spectral calculus and the
full-reference inverse order, using Teschl GSM99, author version
12February2009, Theorems2.13/2.18 pp71-72/77 and Theorems3.1/3.2
pp90-92, and Behrndt–Hassi–de Snoo–Wietsma1403.5704v1,
Proposition2.1 p4, Theorem3.4's nonnegative proof case p11 and
Corollary3.5 p12. Their domain/order qualifications are retained.

## Conclusion

On H0 direct-sum H0 define B=diag(B0,B0), and the bounded Hermitian
M_ref by its real quadratic form

    m_ref(f,h)=2 Re<Uf,h>
                 +<R_ref^-1(Tf+T*h),Tf+T*h>.

The inverse acts on full L2. Both induced middle products and their
cross terms, as well as the actual U, are retained. The comparison

    B-B M_ref B>=0                                           (2)

would suffice for nonnegativity of S3 on W_512-perp squared. However,
there is a specified exact finite neutral pair x such that

    <(B-B M_ref B)x,x>
       < -71572923236209923/268435456000000000
       < -.266 <0.                                         (3)

Thus this particular sufficient reference comparison fails under
the inherited contracts. This is an informative local obstruction,
not a new general source-level theorem. The separate conceptual audit619
in Section5 upholds the implication and transfer under the same contracts.
Neither an actual negative
S3 direction nor a negative smooth triple, off-line zero, or RH
candidate follows. Head/complement mixed payment, C744q, H2,
non-neutral coverage and actual-Xi assembly remain open.

## Proof

### 1. Sufficiency, with kernels and nonclosed range retained

Work on the pair Hilbert space. Put Q=diag(I-P_W,I-P_W),
E_2=diag(E,E), and X=E_2 Q. By(1), XX*<=B. All are bounded;
Douglas Theorem1 applies with Y=B^(1/2), giving X=B^(1/2)C,
||C||<=1. No invertibility of B is needed.

Suppose(2). With D_1=I-B^(1/2)M_ref B^(1/2), it states
B^(1/2)D_1 B^(1/2)>=0. Thus D_1 is nonnegative on ran B^(1/2).
This range is dense in (ker B)-perp, so boundedness extends that
inequality to its closure. On ker B, D_1=I; selfadjointness makes
the cross terms with that kernel zero. Consequently D_1>=0 on
the whole space. Congruence gives

    X* M_ref X
      =C* B^(1/2)M_ref B^(1/2) C<=C*C<=I.                 (4)

This argument never assumes M_ref>=0 and never commutes unequal
factors. For v=Qv, Xv=E_2v. If (f,h)=E_2v and rho=Tf+T*h,
C744z(3)-(4) express the actual endpoint form as

    <S3 v,v>=||v||^2-2 Re<Uf,h>
                      -<A0^-1 P0rho,P0rho>.

C999k/t's relation inverse order gives
<A0^-1 P0rho,P0rho><=<R_ref^-1rho,rho>. Hence (4) implies
<S3 v,v>>=||v||^2-m_ref(E_2v)>=0, proving sufficiency only.

### 2. Exact transferred test vector and its whole output

Write r_n for C999n's exact neutral moment ratios. For a free finite
tail y let N(y) have coefficients y_n for512<=n<=1023,
-sum_(n mod2=p) r_n y_n at p=0,1, and zero otherwise. Both
moments vanish algebraically. C999t Section4 gives
0<r_n<2/n^2<=1/131072 on this band.

Set F=(f,h)=(N(y_f),N(y_h)), exactly C999n's physical pair, and

    x=(x_f,x_h),  x_a=N((D_tail/2)y_a), a=f,h.             (5)

This specifies an exact finite vector, even though its coefficients
involve actual D_n. It belongs to H0 squared and is nonzero since
D_n>6.14 and the frozen free pair is nonzero. Let p_a=P x_a and
l_a=P f_a, for P the raw0:511 projection, and put W=Bx.
The exact block structure of R_ref^-1 and the fact that ran Z
is neutral and in the raw head give

    B0 x_a=P0(B_h p_a direct-sum y_a),
    ||B0 x_a-f_a||<=5||p_a||+||l_a||.                    (6)

For the inequality use f_a=P0 f_a and ||P0||<=1. This pays the
ENTIRE output of P0, including its infinite cosine tail. It does
not replace P0 by a finite projection. For the quadratic pairing,
x_a is neutral, so the exterior P0 drops out and

    <B0 x_a,x_a>=<B_h p_a,p_a>
                         +(1/2)sum_n D_n|y_(a,n)|^2.     (7)

No inverse of B, compression/inverse identity or actual E is computed.

### 3. Complete scalar bounds and the signed debt

The new verifier uses exact rational arithmetic on ALL frozen free
integers and stored dyadic diagonal centers. C999n Sections2/4's
audited entry ledger supplies |D_n-Dhat_n|<.0001 on0:1023.
Every new comparison passes, yielding

    ||y_a||_1<1.442, sum_a||y_a||_2^2<1/5,
    D_n<8 on512:1023, |D_0|,|D_1|<401,
    sum_(a,n) D_n|y_(a,n)|^2<1.001.                     (8)

For the last bound the exact dyadic center sum is enlarged by
.0001 sum_a||y_a||_2^2. C744v(5) gives D_n>=d_n on the band;
C999n's full directed enclosure has sum d_n|y|^2>1. Therefore
the same exact tail energy is >1. Define the rational constants

    a=1.442/131072, delta=.0004.

The moment ratios and(8) imply ||l_a||<=a, ||p_a||<=4a.
Consequently

    ||F||^2<1/5+2a^2<1/4,
    ||W-F||^2<=2(21a)^2<delta^2,
    <Bx,x><1.001/2+160a^2=:b_upper.                     (9)

The last inequality uses(7) and ||B_h||<5; all remaining components
of x vanish. The single-cell response is positive, so

    a0(f,f)+a0(h,h)>1-802a^2.

C999n's independently audited witness gives endpoint energy

    E_end=a0(f,f)+a0(h,h)-2 Re<Uf,h><.723746547

and full inverse debt <R_ref^-1rho,rho>>.5917169000.
The latter is a LOWER bound from one finite variational trial,
not an upper inverse truncation. Subtracting E_end therefore gives

    m_ref(F)>1-802a^2-.723746547+.5917169000=:m_lower.     (10)

The complete forcing map (f,h)->Tf+T*h has norm at most
sqrt(2)||T||. Thus, without assuming a sign for M_ref,

    ||M_ref||<=||U||+2||T||^2||R_ref^-1||
              <30+10(4.71)^2=251.841<252.

For bounded Hermitian M the identity for the difference of two
quadratic forms and Cauchy–Schwarz give
|<MW,W>-<MF,F>|<=||M||||W-F||(2||F||+||W-F||).
Using(9) pays all the full-operator output debt by

    |m_ref(W)-m_ref(F)|<252 delta(1+delta)=.10084032.      (11)

Combining(9)-(11), with exact rational evaluation, yields

    <(B-B M_ref B)x,x>=<Bx,x>-m_ref(W)
       <b_upper-m_lower+.10084032
       =-71572923236209923/268435456000000000<-.266.

This proves(3). The sign is for the proposed sufficient comparison
itself, rather than for a failed lower enclosure. Since (2) is only
sufficient, its failure cannot reverse the implication in Section1.

### 4. Evidence, stopping scope and reproducibility

Reproduce from this notebook with

    python3 scripts/separation-seven/energy-image-signed-comparison-617.py

The full certificate is the matching `.json`; its complete checks,
all exact values and empty failures were inspected. All27 checks pass.
It pins the original archive, scalar certificate and audit, verifies
their recorded passes and generator/input pins, and imports their
mathematical conclusions under the canonical C999n qualifications.
This is not a replay of source/core correctness. No eigenvalue, solve,
factorization, FFT accuracy or numerical minimum enters the new proof.

Stop this fixed B-B M_ref B comparison without retuning N512,
R_ref, the reference tail allocation, or projection. Preserve
stops537/544/545/546/598/600/603 and C999n/r; (3) is a different
exact target from their scalar/quarter/raw-complement comparisons.
Its new local information is the witness transfer to the full
finite-rank-subtracted energy-image majorant. It says nothing about
the actual signed S3 compression. A materially different mechanism
would be required to continue seeking that sign after audit.

### 5. Separate conceptual audit — step619, 12 November2026

**Scope and result.** The invocation-start SPECIALIZE617, separately
approved618, covers this RESEARCH/REPRODUCTION audit. Both the sufficient
implication and the strict bound(3) are upheld. The new evidence is an
independent proof check and complete exact scalar reconstruction, not a
new source-level theorem. N512, the free integers, full reference, floor,
projection and allocations are unchanged. No source/core computation or
large matrix audit is replayed. Every qualification in the hypotheses,
including the unreplayed c_* source, remains essential.

**Bounded factorization and the actual form.** C999t(4)-(6) supply
positive bounded B0, hence positive bounded B. On H0 squared the
operator X=E_2 Q obeys XX*=E_2 Q E_2<=B. Douglas Theorem1, with its
precise citation in the hypotheses, applies to X and Y=B^(1/2).
It gives X=B^(1/2)C with ||C||<=1 even when the range is not closed.

The equivalence used in Section1 requires no inverse of B. If
B^(1/2)D_1 B^(1/2)>=0, then <D_1w,w>>=0 first for
w in ran B^(1/2), then for w in (ker B)-perp by density and
boundedness. For k in ker B, D_1k=k. Selfadjointness gives
<D_1w,k>=<w,k>=0 on the orthogonal complement, so D_1>=0
on the whole pair space. Congruence by C is valid for an indefinite
M_ref: B^(1/2)M_ref B^(1/2)<=I implies X*M_ref X<=C*C<=I.
This does not assert that order is preserved by multiplying unequal
factors or that M_ref itself is positive.

For v=Qv, f,h=E_2v lie in the restricted form domain V0. The bounded
forcing Tf+T*h is a full L2 vector. C744z(3)-(4), including both
middle square terms and their cross term, give exactly the S3 formula
in Section1. The selfadjoint relation from C999k has operator part A0
on H0 and multivalued part H0-perp; its inverse is A0^-1P0. Its form
domain V0 is contained in the reference form domain V, and R_ref<=a0
on V0. The cited nonnegative inverse antitonicity therefore gives the
UPPER bound for actual debt used there. This establishes sufficiency
on Q's range, without identifying a compressed inverse or commuting
E and P_W. It establishes no converse.

**Exact moments and entire projection.** In each parity, C999k's
integrated moment formula makes both exponential-moment coefficients
equal to their nonzero parity-base coefficient times r_n. The two base
columns at0,1 are independent. Thus the two finite parity sums for N(y)
vanish identically. Replacing each free coefficient by D_n y_n/2 and
recomputing BOTH low coefficients proves x in H0 squared exactly.
Finite support also gives the required form-domain membership; no rounded
neutrality residual is used. The lower band bound D_n>6.14 and nonzero
frozen free coordinates ensure x is nonzero.

Since Z* annihilates raw-tail inputs and P0 Z=Z, block inversion of the
already block-diagonal full reference gives

    B0 x_a=P0[(H^-1-Z A^-1 Z*)p_a direct-sum y_a].

This is a block identity for R_ref, not for A0. Subtracting
f_a=P0(l_a direct-sum y_a) and applying the norm-one P0 pays its
entire output, including all modes above1023. For the pairing against
neutral x_a, selfadjointness moves P0 onto x_a and removes it there
alone. The high pairing is exactly sum D_n|y_(a,n)|²/2. These facts
justify(6)-(7) without computing B0's output coefficients or E.

The parity formula in C999t gives 0<r_n<2/n²<=1/131072.
The sum of the two absolute low coordinates bounds their Euclidean
norm, so ||l_a||<=a and, using 0<D_n<8, ||p_a||<=4a.
Consequently the pair error square is at most2(21a)²; there is no
missing factor for the two endpoints or parities. Positivity of S and
|D_0|,|D_1|<401 give the combined low-diagonal loss at most802a².
The inherited weighted lower bound uses
d_n=log(n/(2ell))-2ell²/(9n²)<=D_n, using pi>3 in C744v(5).
It therefore proves the exact high diagonal energy exceeds1.

**Opposite inverse direction and all scalar evidence.** The LOWER
bound in(10) is C999n's distinct positive-pair variational theorem:
the finite trial is in Dom(R_ref^(1/2)), its denominator is positive,
and R_ref^(-1/2)rho supplies the positive-pair range condition for the
full forcing. Its exact primary citation is Friedrich, Gunther and
Klotz, arXiv1708.01545v1, Definition4.1/Lemma4.2 p5, (4.1)-(4.2) p6,
Corollary6.5/full proof p11,
[pinned PDF](https://arxiv.org/pdf/1708.01545v1).
Its upper denominator and positive lower pairing produce the quotient
lower endpoint. Subtracting the endpoint-energy UPPER bound from the
single-cell LOWER bound bounds 2Re<Uf,h> from below; adding the
inverse LOWER bound gives(10). No inverse UPPER bound is substituted
in this subtraction.

The off-diagonal Hermitian U form has norm at most||U|| on the pair
space; the forcing map has norm at most sqrt(2)||T||. Therefore the
whole M_ref norm is below251.841<252. Writing W=F+e and expanding
the Hermitian form gives error at most||M_ref||(2||F||||e||+||e||²).
Since ||F||<1/2 and ||e||<1/2500, this is below157563/1562500.
All signed terms and the infinite projection output are covered by
this bound; no sign of M_ref or equality of the endpoint vectors is
assumed.

Reproduce the independent exact verification from this notebook with

    python3 scripts/separation-seven/energy-image-signed-comparison-audit-619.py

The full certificate is the matching `.json`. It reads every frozen
free integer and diagonal entry, checks integer/finite-binary64 types,
and independently reconstructs all27 original617 checks and all eight
reported exact values. It verifies the original and audit583 artifact
pins, positive denominators, outward LOWER quotient directions and
the inherited analytic diagonal allowance. All104 checks pass with
empty failures. No earlier generator is executed or artifact changed.
The complete load-bearing sums and bounds, rather than previews,
were inspected. In particular,

    sum_a||y_a||²=92476315127417267050871/604462909807314587353088,
    2(21a)²=229249881/2147483648000000 < (1/2500)²,
    b_upper-m_lower+157563/1562500
      =-71572923236209923/268435456000000000<-.266<0.

The audit imports C999n's audited entry ledger and C999t's operator
order with their stated qualifications; hashes and pass flags do not
independently establish those source statements. The above proof checks
their exact applicability. The test x is allowed anywhere in H0 squared
for the proposed operator inequality; it need not lie in W_512-perp.
Its negative value therefore stops that sufficient comparison, not the
actual S3 compression. Preserve all recorded scalar/quarter/projection
stops. Future sign work needs a different, separately assessed target.

## Mathlib

Full matching coverage for the bounded Douglas theorem, this precise
signed comparison and the transferred infinite-dimensional witness
has not been checked. No absence claim is made. Positive square
roots, orthogonal projections, bounded adjoints and quadratic-form
perturbation estimates are supporting mathematics, not a cited
formalization of this qualified result.
Audit619 does not change this unchecked full-matching status.
