# C744y: Directional payment of the complete separation-seven mixed tail

## Hypotheses

Use the audited C744v/w representation on L2(0,ell), ell=log(3)/2,
with the inner product linear in its first slot. N denotes the complex
compact smooth profiles in (0,ell) whose integrals against both
exp(x/2) and exp(-x/2) vanish. Extend profiles by zero. Write

    A=D+W0, W0=S+256 C*C,
    P={cosine indices 0,...,511}, Q=I-P,
    Q_<={512,...,65535}, Q_>={n>=65536}, tau=143/100.

Here C is the two-moment map, S the entire positive single-cell
response, and T the complete separation-seven cross operator of
C744v(1), including all sixteen prime powers and its infinite
continuous kernel. Thus d(f)=H(f,f), and polarizing C744v gives
H(f,tau_(7ell)g)=-<Tf,g> on N times N. Only the unconditional
definitions underlying C744v are used. Neither RH-conditional
positivity nor C744x's unaudited formulas/sign is an input.

The analytic source remains Hongmin Li, *Cutoff-free positivity of
localized Weil forms through the (log 11)/2 threshold*,
[paper45, displayed v2, 9 November2026](https://rstation.ai/problems/riemann_hypothesis/papers/45),
Lemma3.1, (2.1)-(3.4), specialized and audited in C744v/w. Its
(4.7)-(5.5) supplies the complete-covariance method, not this fixed
mixed sign. The finite entry error uses the precise specialization of
[DLMF5.11.2](https://dlmf.nist.gov/5.11.E2) and
[5.11(ii)](https://dlmf.nist.gov/5.11#ii) in C744w(11)-(17).
No source numerical supplement, differentiated asymptotic remainder,
coordinate theorem or larger output prefix is imported.

Use the C744v/w IEEE754 binary64 nearest basic-operation/square-root
and dot-product gamma_r=ru/(1-ru), u=2^-53, execution contract,
with no overflow and the stated negligible absolute underflow charge.
Directed Decimal uses their 60-digit interval class; ln/sqrt are
rounded nearest then widened to neighboring Decimal values. Library
Cholesky only proposes a factor: its full reconstruction is checked.
There is no assumed accuracy for eigenvalues or library trigonometry.
This remains a computational proof under that explicit contract,
not formal verification of the runtime or BLAS.

## Conclusion

On the full1024-dimensional complex retained product space there is
the explicit positive definite matrix

    U=(1/5000) Z*Z+(1/125000)I,                         (1)

defined below, which bounds the entire omitted covariance G*G.
For the exact finite mixed Schur residual R_<, the certificate gives

    G*G<=U,   R_<-U/tau >= .027998 I.                 (2)

Consequently the original independent-profile inequality holds:

    d(f)+d(g)+2 Re H(f,tau_(7ell)g)>=0, f,g in N.     (3)

This is one fixed separation and the sufficient larger-class
penalized comparison. It gives neither a compatible composition
law, all-separation signs, C744q's strict margin, non-neutral
coverage, strict H2 slack/existence nor RH. Both moments vanish
separately, so no penalty is added to the original neutral energy.
No H2 cutoff is needed for (3). The separate step541 conceptual audit
in Section5 upholds this result under the explicit computational
contracts; STATUS remains IN_PROGRESS.

The exact target entered with the pre-existing EXPLORE assessment537
and the supervisor directed this attempt. Classification is
POTENTIALLY_NEW: the assessed sources did not supply this mixed
certificate; this is no certified originality claim. Schur completion
and the source response identity are reused. The local difference
proved here is the directional enclosure (1)-(2), not a reproof of
those known theorems. No general-purpose new asymptotic result is used.

## Proof

### 1. Product-space interface and all finite covariance products

Polarizing the complete cross-cell calculation of C744v replaces
its two f factors by f,g. Each pole product and the j=0 separated
response product vanishes by the two moments of each profile.
Uniform absolute convergence on M+x-y>=6ell justifies the entire
remaining kernel sum. The arithmetic term is precisely
-a_n integral f(x+7ell-log(n))conj(g(x))dx, with no extra factor2.
Thus the closed product form is

    B=[[A,-T*],[-T,A]].                                (4)

W0,T are bounded; D has the diagonal logarithmic form domain
specified in C744v. Hence this is a bounded form perturbation of
D direct-sum D, equal to (3) on the original smooth neutral class.
No cosine vector is claimed to belong to the causal generator domain.
On the full complementary product form domain, C744v's D floor
and ||T||<4.71 give QBQ>=tau Q: the off-diagonal form is bounded
below by -||T|| times the sum of the two squared norms, and both
diagonal S and moment penalties are positive. The audited scalar
floor1.4342765416 exceeds tau. This uses the original energy metric.

Put P2=P direct-sum P, F=(I-P2)BP2, M=P2BP2. The form-domain
Schur completion already used in C744v shows that nonnegativity of
M-F*F/tau suffices for B>=0. Split its output orthogonally:

    F*F=F_<*F_<+G*G, R_<=M-F_<*F_</tau.               (5)

For B0=Q_<W0P, Bc=Q_<(T+T*)P/2, Bg=Q_<(T-T*)P/2,
the actual product factor, calculated directly, is

    F_<=[[B0,-(Bc-Bg)],[-(Bc+Bg),B0]].                 (6)

Writing Cab=Ba*Bb, multiplication gives

    (F_<*F_<)11=C00+Ccc+Cgg+Ccg+Ccg*,
    (F_<*F_<)22=C00+Ccc+Cgg-Ccg-Ccg*,
    (F_<*F_<)12=-C0c+C0g-C0c*-C0g*,
    (F_<*F_<)21=((F_<*F_<)12)*.                       (7)

The head is [[M0,-(Mc-Mg)],[-(Mc+Mg),M0]]. All nine input
matrices are the audited C744w archive; its full replay agrees
bit for bit, and both input archive hashes match that audit.
The scalar-phase sign is not used to infer a mixed sign.

### 2. Entire high-output factors: finite-rank part and paid error

Let K=65536, k_n=n*pi/ell, v_0=1/sqrt2 and v_m=1 for1<=m<512.
Define the finite map Z on retained coefficient pairs x=(x1,x2) by

    (Zx)_(i,p)=sum_(0<=m<512, m mod2=p) v_m x_(i,m),
    i=1,2, p=0,1.                                    (8)

Its four rows have disjoint supports and ||Z||^2=256. This is a
finite linear map, not a change of the energy metric or an endpoint
trace assertion on an infinite-dimensional form domain.

We prove G=HZ+E with ||H||^2<1/10000 and ||E||<1/500. Both maps
retain all output indices n>=K. First, C744v(9) gives for matching
parity, with alpha_n alpha_m=(4/ell)v_m for n>=K,

    S_nm=(4/ell)v_m sum_j c_j^2(1-(-1)^n exp(-ell c_j))
                       /[(c_j^2+k_n^2)(c_j^2+k_m^2)].

Opposite parities are zero. Define U0(k)=sum_j(c_j^2+k^2)^(-1).
Integral comparison of the decreasing summand at c_j=1/2+2j gives

    |U0(k)-pi/(4k)|<=1/k^2, k>0,
    U0(k)<=1/k^2+pi/(4k).                             (9)

Explicitly the sum lies between half the integral from1/2 to
infinity and that integral plus its first term. Replacing the
integral's lower endpoint by0 changes it by at most1/(4k^2).
These inequalities imply (9), without an asymptotic interchange.
Also

    sum_j c_j^2/[(c_j^2+k_n^2)(c_j^2+k_m^2)]
      =U0(k_n)-k_m^2 sum_j1/[(c_j^2+k_n^2)(c_j^2+k_m^2)].

For m>0 the subtracted quantity is at most
(1+pi*k_m/4)/k_n^2 by (9); for m=0 it is exactly zero.
The absolute exponential addition is at most
E0/k_n^2, E0=sum_j exp(-ell c_j)=(3/2)3^(-1/4).
Consequently the same-parity response has the leading entry v_m/n
and remainder bounded by

    |S_nm-v_m/n| <= v_m(m+b0)/n^2,
    b0=4ell(2+E0)/pi^2<.7.                            (10)

Thus its entire operator error is at most its Hilbert--Schmidt norm,
bounded (even ignoring the parity restriction) by

    eS=[sum_(m<512)(m+.7)^2/(3(K-1)^3)]^(1/2)<.000231. (11)

For the prime part J, use the exact normalized shift entries in
C744w Section3. Put eta_j=(-1)^j, theta_r=pi*delta_r/ell,
delta_r=7ell-log(r), and a_r=Lambda(r)/sqrt(r), for its sixteen
listed powers. Their leading entries, for n>=K, are

    delta>0: -(2/pi) v_m eta_n eta_m sin(n theta)/n,
    delta<0: +(2/pi) v_m sin(n theta)/n.                (12)

Subtracting (12) from the exact antiderivative expression leaves
absolute error at most

    (2/pi) v_m m/[n^2(1-m/n)].                        (13)

Indeed before normalization the error numerator is bounded by
k_m+k_m^2/k_n over k_n^2-k_m^2; cancellation of k_n+k_m gives
k_m/[k_n(k_n-k_m)]. Normalization converts this to (13), including
m=0, where the error vanishes. This holds for both signs of delta,
so also for J* by replacing every delta by -delta. With a=sum_r a_r,
both complete prime remainders have operator norm at most

    eJ=(2a/pi)/(1-511/K)
                      [sum_(m<512)m^2/(3(K-1)^3)]^(1/2)<.001130. (14)

Here and in (11) the whole series sum_(n>=K)n^-4 is bounded by
1/[3(K-1)^3]. No inner response or output truncation is hidden.

Use the complete continuous-kernel norm kappa<.000106 from C744v(2)
for T and T*, and the full moment-tail norm eC<.000001 from
C744w(8), with pi>3.14. In product space, a repeated diagonal
remainder has its single-block norm, while the two off-diagonal
remainders have their maximum norm. Hence the combined remainder E
after removing (10)'s leading part and (12) satisfies

    ||E||<=eS+eC+eJ+kappa<.001466290<.002.             (15)

This includes the entire S, both moments, all sixteen translations,
their adjoints and the entire continuous kernel. Its norm bound
pays every product involving these remainders when used below.

### 3. Directional leading covariance with all oscillatory terms paid

Set A_+(n)=sum_(delta_r>0)a_r sin(n theta_r) and
A_-(n)=sum_(delta_r<0)a_r sin(n theta_r). For J, the coefficient
of v_m in (12) is 2[A_-(n)-eta_n eta_m A_+(n)]/(pi n).
For J* it is 2[-A_+(n)+eta_n eta_m A_-(n)]/(pi n).
Along with the response entry v_m/n at matching parity, these
form the explicit map H from C^4 to the two full output sequences.
It follows by summing all its entries' squares that

    ||H||_HS^2=2 sum_(n>=K)1/n^2
              +(16/pi^2)sum_(n>=K)[A_+(n)^2+A_-(n)^2]/n^2. (16)

For each J output row, summing the two input-parity squares cancels
the A_+ A_- terms exactly. The J* row has the same sum. The response
and prime entries occupy different columns in a given product-output
row, so their squares add in this Hilbert--Schmidt norm. This is
not deletion of any cross product inside G*G: the operator norm
bound on HZ and the combined inequality below retain all of them.

For any nonzero frequency phi mod2pi, finite geometric sums and
summation by parts give the full tail bound

    |sum_(n>=K)exp(i n phi)/n^2|
                    <=2/[|1-exp(i phi)|K^2].          (17)

To see the tail control, all partial sums starting at K have norm
at most2/|1-exp(i phi)|. Abel summation against the decreasing
weights1/n^2 bounds each finite weighted sum by that constant/K^2;
the terminal term tends to zero, proving (17).

For two powers in the same sign group we need phi=theta_i+theta_j,
and also theta_i-theta_j when i!=j. The zero self-difference supplies
the diagonal1/2 term in sin^2, not (17). All136 ordered sums and120
nonzero ordered differences are certified with chord>.01.
Specifically r_i=delta_i/ell lies in (-1,1), and directed intervals
for r_i+/-r_j give

    |1-exp(i*pi*r)|>=2 dist(r,2Z)>.01.

The nearest even integer is among -2,0,2. This chord inequality
follows from sin(t)>=2t/pi for0<=t<=pi/2. The certificate contains
all256 complete interval checks; the smallest certified chord lower
bound exceeds.036443. No floating sine value enters these checks.

Using sin u sin v=(cos(u-v)-cos(u+v))/2, (17) bounds every nonconstant
weighted cosine tail by200/K^2. For either sign group I, therefore,

    sum_(n>=K)(sum_(i in I)a_i sin(n theta_i))^2/n^2
     <= [sum_(i in I)a_i^2]/[2(K-1)]
                       +200(sum_(i in I)a_i)^2/K^2.   (18)

The diagonal cosine error only needs100/K^2; the displayed common
200 bound covers it too. Both group sums of weight squares together
give sum_r a_r^2, and the two squared weight sums are at most a^2.
Combining (16)-(18), using pi>3.14, proves

    ||H||^2<=||H||_HS^2
     <=2/(K-1)+(16/3.14^2)[sum_r a_r^2/(2(K-1))+200a^2/K^2]
     <.000085388<.0001.                               (19)

The primary series in (16) are absolutely summable, so the finite
sixteen-frequency expansion and all limiting sums are justified.
This is an elementary enclosure of the existing exact factors,
not an unproved asymptotic leading-term claim.

For every complex retained vector x, G=HZ+E and (15),(19) imply

    ||Gx||^2 <=2||HZx||^2+2||Ex||^2
             <=(1/5000)||Zx||^2+(1/125000)||x||^2.

Thus G*G<=U with U positive definite, as claimed. Orthogonal output
ranges split (5); no response/prime/moment/continuous product within
the high-output range is omitted. In particular entrywise scalar
upper endpoints have not been mistaken for a Loewner upper matrix.

### 4. Full finite certificate, arithmetic and conclusion

The program reconstructs (7) from the audited archive, rather than
reading C744x's saved mixed matrix. C744w's finite errors apply
directly to (6): with b=sqrt((K-512)*512)*10^-7,

    eF=eQ+3b, eM=eH+3*512*10^-7,
    ||Fhat_<||<=||Bhat0||_F+||Bhatc||_F+||Bhatg||_F.

The product-space diagonal/off-diagonal norm bounds introduce no
sqrt2 loss. All six raw products, additions and symmetrization are
covered by the inherited10^-6 covariance allowance: each raw-product
error is below10^-10, the diagonal combinations use at most five
copies and the off-diagonal combinations at most four. The127 blocks
of512 rows use C744w's gamma_1024 dot bound and Cauchy--Schwarz
over their Frobenius norms. The exact R_< and stored real symmetric
Rhat therefore differ in norm by at most

    eM+[(2sum||Bhat_j||_F+eF)eF+10^-6]/tau
       <.007991<.012.                                 (20)

The audited values eH<.000184,eQ<.000000181 and factor norms
<.586,1.485,1.091 are unchanged. Real operator bounds here apply
equally to the full complex space; no real-profile restriction enters.

Compute Uhat from (8) using the correctly rounded sqrt2 and ordinary
basic operations. Exact ||Z||=16 and ||Z||_F^2=1023 imply
||Zhat-Z||<10^-14. The four-term Gram products have Frobenius
rounding error bounded by gamma_8||Zhat||_F^2<10^-12 before the
division by5000. Thus U's evaluation error is far below10^-12.
The subsequent division by the encoded1.43, subtraction from Rhat
and storage symmetrization have norm error below10^-6. For example
the stored matrix's entries are below400, its Frobenius norm is
below409600, and each added element requires only a bounded number
of basic operations; even100u times that norm is below5*10^-9.
This separate10^-6 debt also covers encoding the rational shifts.

Before computing the finite sign, the working note fixed the matrix
(1) and a proposed paid floor1/25. The proposed real factor L has
all entries finite, max|L_ij|<20, squared Frobenius norm
5813.338987<20000, and the full measured reconstruction norm is

    ||Rhat-Uhat/fl(1.43)-.04I-fl(LL*)||_F
                         <6.202*10^-14<10^-7.          (21)

Every one of the1024^2 entries is included. The standard real
dot-product bound gives gamma_2048*20000<5*10^-9 for the exact
LL* reconstruction error; subtraction and the real-square norm
evaluation fit well inside10^-6. Thus (21), without trusting any
Cholesky success flag, implies the stored paid matrix is at least
(.04-.000001)I. Together with (20) and the separate10^-6 U/assembly
debt, the exact paid residual satisfies

    R_<-U/tau >=(.04-.012-.000002)I=.027998I.           (22)

This completes the frozen sign test; no floor or parameter was
retried after a failure. Equations (2),(5) and the form-domain
Schur completion prove (3). The original two moment penalties vanish
exactly on N times N. No numerical neutrality or smooth-witness
transfer is used, and no RH-equivalent positive zero measure enters.

Reproduce from the notebook, preserving all earlier artifacts:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/matrix-tail-certificate-539.py

Full intervals, all256 nonresonance checks, input hashes, arithmetic
ledger, reconstruction data and failures are in
`scripts/separation-seven/matrix-tail-certificate-539.json`.
The complete head, finite covariance, residual, Z, U and paid matrix
are in `scripts/separation-seven/matrix-tail-matrices-539.npz`;
all factor entries are in `scripts/separation-seven/matrix-tail-factor-539.npz`.
The certified scalar upper endpoints are below.000085388 and
.001466290, compared with the required.0001 and.002 respectively.
The failures list is empty. These are original-attempt checks;
the independent conceptual audit of (4)-(22) follows.

### 5. Separate conceptual audit — 12 November 2026, step541

**Verdict.** Equations (1)-(3) are upheld at the original frozen
parameters, under exactly the analytic inputs and execution contracts
in the Hypotheses. The paid floor remains .027998. This is
REPRODUCTION of the existing local certificate, not a new inequality,
new general theorem, or evidence beyond the sources checked. The
prior SPECIALIZE assessment539, separately approved in step540,
covered this audit. No parameter, proposed factor or input archive
was replaced. C744x's scalar-tail stop is not a proof premise.

The bounded-block source is Dritschel and Rovnyak, *The Operator
Fejer-Riesz Theorem*, [arXiv:0903.3639v1](https://arxiv.org/pdf/0903.3639v1),
AppendixA, LemmasA.1-A.2, printed pp28-30. Positivity is a hypothesis
of the maximal-short statement A.2, so it is not used to assume the
sign being tested. The closed-form bridge is the audited C744v
extension, followed by its square completion. Rump, *Verification of
Positive Definiteness*, BIT46(2006),433-452,
[author PDF](https://www.tuhh.de/ti3/paper/rump/Ru06c.pdf),
Theorem2.3, (2.12) and Corollary2.7, supplies the inspected finite
verification precedent. The full reconstruction below verifies its
own norm/error bounds; it does not assert that a library factorization
success flag implements that corollary. These source assessments are
reused, not new literature or reproved operator theorems.

**Complex form and finite products.** The diagonal identity for the
sesquilinear cross form on every complex f determines that form by
complex polarization, even though the cross operator T is not
self-adjoint. Alternatively, the direct separated integral in C744v
Section7 replaces its first factor by f and second by conjugate(g).
Thus the cross term is exactly -2Re<Tf,g>. The two pole products and
separated j=0 term vanish by the two moments of each profile. Uniform
absolute convergence on M+x-y>=6ell justifies the remaining integral
and sum. Consequently (4) has the displayed adjoint orientation.

The extension has the logarithmically weighted coefficient domain
of C744v in each component. Equivalently this is
Dom((D+cI)^(1/2)) for any c making D+cI>=I; no positivity of D
itself is assumed.
Every retained cosine vector and every original compact smooth
profile lies in this form domain. W0 and T are bounded. The
complementary lower comparison is the same D floor minus ||T||,
since 2|<Ty1,y2>|<=||T||(||y1||^2+||y2||^2). It exceeds
1.4342765416>tau on the whole complementary product domain.
Square completion is therefore valid without a positive inverse of
the whole unproved block. Direct multiplication of (6) gives (7):
the off-diagonal product is
B0*(-Bc+Bg)+(-Bc-Bg)*B0, with precisely the four displayed signs.
Orthogonality splits the output ranges only; no product within
either range is discarded. These checks cover complex coefficients.

**All infinite-output modes.** Integral comparison bounds U0(k)
between half its integral from1/2 and that integral plus the first
summand. The lower-endpoint error against pi/(4k) is <=1/(4k^2),
and the upper error is <=1/k^2. In the subtracted term of Section2,
k_m^2 U0(k_m)/k_n^2 <=(1+pi*k_m/4)/k_n^2 when m>0;
it is exactly zero when m=0. The exponential term has absolute
bound E0/k_n^2 for either parity. Since
(4ell/pi^2)(pi*k_m/4)=m, the leading coefficient and every term of
(10) follow with v0=1/sqrt2. Taking the square sum over all m,n,
even ignoring parity, proves (11). There is no asymptotic limit
interchanged with an unbounded m range.

For delta>0, subtract -eta_n eta_m sin(k_n delta)/k_n from the
unnormalized exact formula in C744w Section3. The remaining two
terms have combined absolute value at most
(k_m+k_m^2/k_n)/(k_n^2-k_m^2)=k_m/[k_n(k_n-k_m)].
For delta<0 the same bound follows after subtracting
sin(k_n delta)/k_n. Multiplication by (2/ell)v_m proves (12)-(13),
also for m=0, where both remainders vanish. Replacing delta by -delta
proves the adjoint formula independently. The complete sixteen-term
sum, the entire continuous norm kappa and both moment tails thus
give (14)-(15). Repeated diagonal errors have their single-block
operator norm; the off-diagonal error matrix has the maximum of its
two block norms. The triangle bound in (15) has no omitted factor.

For explicit sign checking, write epsilon_np=(-1)^(n+p). With rows
indexed by output component i and mode n>=K, and columns by component
j and parity p, the leading map in G=HZ+E is

    H_(1n,1p)=H_(2n,2p)=1_(n mod2=p)/n,
    H_(1n,2p)=2[A_+(n)-epsilon_np A_-(n)]/(pi n),
    H_(2n,1p)=2[-A_-(n)+epsilon_np A_+(n)]/(pi n).

Summing the squares over both input parities cancels the A_+ A_-
terms, giving exactly (16). The response and prime entries occupy
different columns in each output row. This calculation bounds the
Hilbert--Schmidt norm of H; it is not a diagonalization of H*H or
G*G. Both complex cross terms and all remainder products are paid
by ||HZx+Ex||^2<=2||HZx||^2+2||Ex||^2.

The finite geometric-sum bound and summation by parts in (17) apply
to every nonzero frequency. The zero self-difference contributes
the nonoscillating half diagonal in (18), rather than using a
nonresonance bound there. Independent prime-power enumeration gives
6 positive-delay and10 negative-delay powers. Every one of the136
ordered sums and120 nonzero ordered differences was recalculated
with90-digit directed intervals. Their ratios lie in (-2,2), so
-2,0,2 include all nearest even integers. The distance/chord
inequality is valid throughout, including near either endpoint.
All810 recalculated scalar intervals (including every weight, ratio,
distance and chord) lie inside the original60-digit enclosures.
The minimum chord lower bound exceeds .036443003>.01. The complete
independent bounds are

    ||H||^2 <= ||H||_HS^2 < .000085388 < .0001,
    ||E|| < .001466290 < .002.

Thus the same U bounds the whole infinite covariance. Its identity
term is strictly positive; entrywise upper intervals were never
substituted for a matrix-order bound.

**Full finite evidence and arithmetic.** All original539 artifact
hashes and the inherited534 input hashes match. Every entry of all
nine532 matrices was compared with the already audited534 replay;
all agree exactly. This audit reuses that complete input verification,
rather than claiming to regenerate the original65024 output rows.
It rebuilt all six539 arrays with separate block assignments. The
largest full Frobenius discrepancy is <1.76e-16; Z, U and the head
agree exactly. Different addition ordering accounts for the tiny
covariance/residual discrepancies, far inside the arithmetic debts.

For a conservative independent finite ledger, use only the already
audited rounded-up bounds eH<.000184, eQ<.000000181 and factor norms
<.586,1.485,1.091. Their sum is <3.162. Directed evaluation of (20)
with these larger bounds gives .007996261<.008<.012. The finite
matrix error bound is unchanged. Each raw covariance dot error is
<1e-10 by the127-block Cauchy--Schwarz argument of C744w; at most
five such products enter each diagonal and four each off diagonal.
The block norm is bounded by the maximum diagonal norm plus the
maximum off-diagonal norm. All multiplication, addition and
symmetrization errors remain inside the separate10^-6 covariance
allowance. No statistical cancellation of errors is used.

The exact dyadic squared error of the stored zero-mode weight from
1/2 is <10^-14. Both that weight and 1/sqrt2 exceed1/2, so the
corresponding weight error is smaller still. The four-row Gram
evaluation therefore meets Section4's U allowance, including the
two occurrences of v0. All retained directions are included.

The original stored factor, without any new Cholesky call, was
multiplied against the independently rebuilt1024-dimensional paid
matrix. All1048576 entries enter the reconstruction norm. The
measured Frobenius residual is <6.202e-14<10^-7, the squared factor
norm is <5814<20000, max|L_ij|<18<20 and max|paid_ij|<293<400.
The real-square norm operation count gives gamma_(2097162)<10^-9;
its error cannot approach the generous norm thresholds. The exact
rational product-error bound is

    gamma_2048*20000=20000/4398046511103<5*10^-9.

Including norm rounding, subtraction, reconstruction ordering and
rational encodings gives an upper reconstruction debt <1.455e-8,
strictly below the allotted10^-6. The independent U/assembly debt
is also retained as10^-6. In particular no eigenvalue estimate or
assumed library Cholesky accuracy certifies the sign. The exact
rational subtraction remains

    1/25-12/1000-2/1000000=13999/500000=.027998>0.

The runtime reports nearest rounding and binary64, with its versions
recorded in the certificate. This is identification under the stated
operation/dot-product contracts, not formal verification of NumPy,
BLAS or the interpreter. Under those contracts no mathematical defect
was found. Exact moments remove the penalties on the original
profiles; no H2 assumption or numerical smoothing is used.

Reproduce this audit without overwriting earlier evidence:

    OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 scripts/separation-seven/matrix-tail-audit-541.py

The complete810 interval checks, all256 chord checks, hashes, all
matrix comparisons, reconstruction and exact rational error bounds
are in `scripts/separation-seven/matrix-tail-audit-541.json`.
The failures list is empty. Composition, other separations, strict
H2 slack/existence, C744q's strict margin, non-neutral coverage and
global assembly remain open. This audit is not an RH candidate.

## Mathlib

Full matching coverage of the localized response identity or this
fixed mixed covariance certificate has not been checked. No absence
or full formalization claim is made. Integral comparison, geometric
summation, Hilbert--Schmidt bounds, Schur completion and finite Gram
positivity are supporting mathematics, not an imported RH sign.
