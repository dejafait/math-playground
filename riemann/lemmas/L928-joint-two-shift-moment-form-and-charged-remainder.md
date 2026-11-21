# Lemma 928: exact joint two-shift main form and charged remainder

## Hypotheses

Use L637's real Hardy function Z, smooth Hardy phase theta, and fixed
nonnegative w in C_c^infinity((0,1)), with integral w=1. Put

    L=log T, N=floor(T^(1/5)), T<=X<=2T,
    w_XT(t)=w((t-X)/T), ||f||_T^2=integral w_XT |f|^2,
    P_s(t)=sum_(n<=N)c_(s,n)n^(-it), s in {-1,+1},
    U(t)=Z(t-1/L)P_-(t)+Z(t+1/L)P_+(t),
    S=||c_-||_2^2+||c_+||_2^2.

Both coefficient vectors are arbitrary complex vectors, including
T,X-dependent vectors. Constants and sufficiently-large-T onsets below
are independent of X and both vectors. No RH, nonvanishing, positivity
of a mixed matrix, or restriction to real coefficients is assumed.

The arithmetic inputs are named imports:

* Kyle Pratt and Nicolas Robles, *Perturbed moments and a longer
  mollifier for critical zeros of zeta*, Research in Number Theory 4,
  article 9 (2018), DOI
  [10.1007/s40993-018-0103-4](https://doi.org/10.1007/s40993-018-0103-4),
  [arXiv:1706.04593v3, Theorem 1.2, pp. 3-4](https://arxiv.org/pdf/1706.04593v3).
  Only its general-coefficient case at alpha=beta=+i/L or -i/L
  is used. The exact mixed-polynomial statement is also displayed in
  [the primary HTML, Section 1.3](https://arxiv.org/html/1706.04593v3#S1.SS3).
  Smooth-weight and coefficient uniformity use the inspected operations
  in Sections 2.1, 3.1, 3.2.1-3.2.4 and 4.1, pp. 4-15 and 19.
* S. Bettin, V. Chandee and M. Radziwill, *The mean square of the
  product of the Riemann zeta-function with Dirichlet polynomials*,
  J. reine angew. Math. 729 (2017), 51-79,
  [arXiv:1411.7764v1, Theorem 1, pp. 1-2](https://arxiv.org/pdf/1411.7764v1),
  DOI [10.1515/crelle-2014-0133](https://doi.org/10.1515/crelle-2014-0133).
  The equal-shift application uses the weight and normalization
  justification in L737 and the padded error computation in L927.

These arithmetic estimates are not reproved. L637 supplies exact
Z(v)=exp(i theta(v))zeta(1/2+iv), its gamma-phase bounds and smooth
phase-weight method. L737 supplies its finite form and common windows;
audited L926 supplies Q(c)>=q0 N^(-1/4)||c||_2^2 with q0>0.
L925 is not used. The invocation-start EXPLORE assessment was
drafts/literature/2026-11-09-joint-two-shift-coercivity-test.md.
The complete source comparison is
drafts/literature/2026-11-09-joint-two-shift-arithmetic-dictionary-scope.md.

## Conclusion

For positive t on the support of w_XT define, for m,n<=N,

    d=gcd(m,n), q_mn=d/sqrt(m*n),
    ell_t=log(t/(2*pi)), H_t(m,n)=ell_t-log(m*n/d^2),
    epsilon_t=theta(t+1/L)-theta(t-1/L)-ell_t/L,
    R_t(m,n)=q_mn*[exp(i*H_t(m,n)/L)*zeta(1+2i/L)
                         +exp(-i*H_t(m,n)/L)*zeta(1-2i/L)],
    (D_s c)_n=n^(i*s/L)c_n,
    A_(t,s)=log((t+s/L)/(2*pi))+2*gamma,
    F_A(v)=sum_(m,n<=N) v_m conjugate(v_n) q_mn
                            *[A-log(m*n/d^2)].                 (1)

All positive-base powers use their real logarithms. R_t is exactly real
and symmetric. The following integrated expression is a real Hermitian
form on the two coefficient vectors:

    M(c_-,c_+)=integral w_XT(t) [
        F_(A_(t,-1))(D_- c_-)+F_(A_(t,+1))(D_+ c_+)
        +2 Re {exp(i*epsilon_t)
               sum_(m,n<=N)c_(+,m)conjugate(c_(-,n))R_t(m,n)}] dt.
                                                               (2)

It satisfies the coefficient-uniform identity and bound

    ||U||_T^2=M(c_-,c_+)+E(c_-,c_+),
    |E(c_-,c_+)|<=C_w N T^(51/80) S<=C_w T^(67/80) S.           (3)

For each of the two diagonal main forms separately,

    integral w_XT F_(A_(t,s))(D_s c_s) dt
        >=(q0/10) T L N^(-1/4)||c_s||_2^2.                    (4)

In particular the available full remainder is small enough for the
requested joint margin, if that margin can be proved for M:

    |E|/[T L N^(-1/4) S] <= C_w T^(-9/80)/L ->0              (5)

when S>0. At S=0 all forms vanish. Equation (4) is NOT a lower bound
for (2). No lower bound c T L N^(-1/4) S for M or ||U||_T^2 is proved
here, and no joint projection conclusion follows yet.

This is a local REPRODUCTION of a covered moment application, not a
new arithmetic moment theorem or a discovery beyond the checked
sources. It is a partial result of the approved coercivity test. Written
9 November 2026; the separate application audit below validates (1)-(5)
under the named imports without establishing (11). Actual-Xi signs,
signed transfer and L030-L032/C032a remain unresolved.

## Proof

### 1. Common windows, weights and coefficient normalization

Reuse L737's fixed smooth nonnegative partition rho_j, with sum one on
a neighborhood of [1,3], supported inside (a_j,2a_j), where
a_j=3/4,5/4,2. Set Y_j=a_j T and x=X/T. On these windows

    phi_(j,x)(v)=rho_j(a_j v)w(a_j v-x)

has common compact support in (1,2) and uniformly bounded derivatives
of every fixed order. The exact weight for a cross block is this
function multiplied by

    p_(s,r)(Y_j v),
    p_(s,r)(t)=exp(i[theta(t+s/L)-theta(t+r/L)]).              (6)

L637's smooth gamma-phase estimates give
partial_t^k p_(s,r)(t)=O_k(T^(-k)) on these comparable intervals,
including k=0, for these fixed real shifts. Consequently
partial_v^k p_(s,r)(Y_j v)=O_k(1). Product differentiation proves
common bounds for every required scaled weight seminorm. Mellin
separation is uniform as well: after v=exp(y), repeated integration
by parts on the common compact y support bounds its Mellin transform
on each fixed vertical line by C_j(1+|tau|)^(-j). Boundary terms
vanish. This is the same weight argument as L737's checked application.
Complex weights are allowed by the source's linear proof operations;
alternatively split into real and imaginary parts and then into a
difference of nonnegative smooth weights by adding one fixed smooth
majorant. Each split has the same compact support and common bounds.

Use the fixed source cutoffs M_j=K_j=Y_j^(1/4). Eventually N is
below both cutoffs for every j, since N/Y_j^(1/4)=O(T^(-1/20)).
If c_s is nonzero put B_s=max_(n<=N)sqrt(n)|c_(s,n)| and use

    a_(s,n)=sqrt(n)c_(s,n)/B_s  (n<=N),
    a_(s,n)=0                 (N<n<=Y_j^(1/4)).             (7)

All source coefficients have modulus at most one, independent of their
positions, phases and parameter dependence. A zero block is handled
directly. Restoring the two factors B_s B_r in a mixed moment costs

    B_s B_r<=N||c_s||_2||c_r||_2.                          (8)

There is no entrywise summation of source errors.

For alpha=beta=+/-i/L their sum is +/-2i/L. The source's pole
annihilator G(z)=exp(z^2)[1-4z^2/(alpha+beta)^2] therefore has at
most polynomial logarithmic losses in its fixed seminorms. There is
no passage through zero shift sum. Use the source estimates with a
total power allowance 1/80: one may first choose their arbitrarily
small epsilon losses with total at most 1/160, and absorb the fixed
remaining logarithmic factors in T^(1/160). The finitely many smooth
weight operations just described preserve this allowance. At padded
lengths Y_j^(1/4), the three exponents in Theorem 1.2 are then

    1/2+1/80+(1/2)(1/4)=51/80,
    3/20+1/80+(1/2)(7/10)+(1/4)(1/4)=23/40,
    1/80+(1/2)(7/8)+(1/4)(1/8)=77/160.                  (9)

The first is largest. All three terms, including the (M+K) powers,
have been charged; replacing this error by BCR's smaller error is
not justified. Summing the three comparable windows and restoring (8)
gives cross-block remainder at most
C_w N T^(51/80)||c_s||_2||c_r||_2.

### 2. Exact off-diagonal kernel, with no frozen phase

For s=+1,r=-1, the exact Hardy identity converts the cross moment
into the source integrand with alpha=beta=i/L and weight (6).
After (7), the source coefficient factor becomes q_mn. The remaining
kernel before the Hardy phase is

    q_mn*(d^2/(m*n))^(i/L)
       *[zeta(1+2i/L)+zeta(1-2i/L)
                              *(2*pi*m*n/(t*d^2))^(2i/L)].    (10)

Multiplying by p_(+,-)(t) gives exactly exp(i*epsilon_t)R_t(m,n)
in (1), by H_t=ell_t-log(m*n/d^2). This is algebra, not a Laurent
approximation. Zeta conjugation on these two points and symmetry in
m,n make R_t real symmetric. The reversed cross block is the conjugate
transpose, as is also seen by taking alpha=beta=-i/L. Adding the
two cross blocks gives precisely the real part in (2) and an error
bounded by C_w N T^(51/80) S, using 2||c_-||||c_+||<=S.

Both source shifts are equal in each of these cross-block applications.
No assertion for an unequal alpha,beta orientation is needed. There is
no use of the source's singular zero-sum formula for equal Hardy shifts.

For perspective only, L637's theta'(t)=ell_t/2+O(T^(-1)) implies
epsilon_t=O(1/(T L)): integrate theta' from t-1/L to t+1/L and
bound the change in log(t/(2*pi)) on that interval. This does not
authorize deleting epsilon_t from (2); it is retained exactly.

### 3. Translated diagonal blocks and the full charged error

For one s substitute v=t+s/L in its squared norm. The polynomial
coefficients become c_(s,n)n^(i*s/L), with unchanged magnitudes,
and the weight becomes w((v-X)/T-s/(T L)). Partition on v using
the same rho_j. Because supp(w) is compact in (0,1), the translated
support remains in [T,3T] eventually. The new scaled weights are

    rho_j(a_j z) w(a_j z-x-s/(T L)).

They have the same common compact support and bounded seminorms.
BCR's theorem at padded exponent 1/4, with coefficient normalization
B_s and error allowance 1/80, gives the L927 bound
C_w B_s^2 T^(23/40). Its main form, after returning to t, is exactly
the diagonal form in (2); in particular both the coefficient rotation
D_s and log((t+s/L)/(2*pi)) are present. Thus the two diagonal errors
sum to at most C_w N T^(23/40) S. Adding the cross-block bound proves
(3), since 23/40<51/80 and N<=T^(1/5).

### 4. Paid diagonal margins and the unpaid joint comparison

L737's finite identity and relative estimate apply to every complex
vector v: F_A(v)>=(A-4log N)Q(v). Here A_(t,s)>=L-C uniformly,
and 4log N<=4L/5. Hence A_(t,s)-4log N>=L/10 eventually.
L926 applies to D_s c_s with the same q0, since D_s preserves the
coefficient Euclidean norm. Integration against w_XT, whose integral
is T, proves (4). Direct division in (3) gives

    C_w N^(5/4) T^(51/80-1)/L
        <=C_w T^(1/4-29/80)/L=C_w T^(-9/80)/L,

which proves (5). Thus the imported error permits the requested
margin, but supplies none of its cross-block spectral content.

To state that missing content explicitly, denote the two integrated
diagonal forms in (2) by D_-(c_-) and D_+(c_+), and denote its
integrated complex cross pairing by C(c_+,c_-). A sufficient estimate
would be, for one fixed eta>0 at one common onset,

    |C(c_+,c_-)| <= (1-eta)*sqrt(D_+(c_+)D_-(c_-))          (11)

for every pair of vectors. Then 2sqrt(ab)<=a+b would give
M>=eta(D_++D_-), and (4)-(5) would prove the target. Estimate (11)
has NOT been proved. It is only sufficient; failure to establish it
would not disprove the original lower bound. Separate diagonal
coercivity and Cauchy-Schwarz for the actual moments provide no fixed
eta. An entrywise absolute bound or a scalar two-atom calculation
likewise does not establish (11) for growing complex coefficient blocks.

The approved attempt ends at this explicit unpaid finite comparison.
No bad vector was found and no negative eigenvalue is asserted. All
sums above are finite, all errors homogeneous, and the named arithmetic
inputs have only been specialized within the assessed scope.

### Separate conceptual application audit — 9 November 2026, step 8

The prior SPECIALIZE assessment was
drafts/literature/2026-11-09-joint-two-shift-moment-audit.md.
This audit checks the stated moving-vector application, using the
full proof above, L637's exact normalization and phase-weight bounds,
L737's finite form and step261 weight audit, and audited L926/L927.
The arithmetic theorems remain named imports. In particular, this is
not an independent certification of their deeper arithmetic proofs.
The exact theorem and relevant weight operations were cross-checked in
[Pratt--Robles v3, Theorem 1.2 and Sections 2.1, 3.2.1-3.2.4, 4.1](https://arxiv.org/html/1706.04593v3#S1.SS3);
the previously inspected BCR cases are reused through L737 and L927.
No change to the statements or mathematical inputs is needed.

**Common source class.** The three fixed open windows cover [1,3].
Write K_j for the compact support of rho_j(a_j v) inside (1,2).
Every cross weight is supported in K_j, independently of T,X and
the coefficients. L637's phase Phi in (19), with b=(s,0,r,0),
is exactly p_(s,r); its bounds preceding (20) therefore give
partial_t^k p_(s,r)=O_k(T^(-k)). No higher derivative bound for Z
or a logarithm of Z is needed. Multiplication by phi_(j,x) and the
chain rule give one bound for each scaled derivative, uniformly in
x in [1,2] and the two possible cross orientations. On each fixed
Mellin line, v=exp(y) turns the transform into a Fourier integral of
exp(sigma*y) times this weight on a common compact interval. Integrating
by parts any fixed number of times proves uniform integrable decay;
there are no endpoint terms. These are the weight quantities used in
the cited integration-by-parts and Mellin-separation estimates.

Complex weights cause no positivity assumption: choose a fixed smooth
chi_j, supported in (1,2), equal to one on K_j. Adding C chi_j to
either real component makes it nonnegative for one common C; subtract
C chi_j afterwards. This preserves common support and derivative
bounds and uses only finitely many linear applications of the source.
Translated diagonal weights have the same properties. If
supp(w) lies in [delta,1-delta] with delta>0, then |s|/L<delta T
keeps their physical supports in [T,3T], including when X=T or 2T.

On every window log(Y_j)=L+O(1), so |alpha|=|beta|=1/L is within
the source's O(1/log Y_j) shift range. Both cutoffs have fixed exponent
1/4, and N/Y_j^(1/4)=O(T^(-1/20)); padding is admissible at one
onset independent of both vectors. For each nonzero block, (7) gives
A_s(1/2+it)=P_s(t)/B_s and |a_(s,n)|<=1 throughout the padded
prefix. Thus a mixed source remainder must be multiplied by B_s B_r,
whereas a diagonal remainder must be multiplied by B_s^2. The source
estimates are uniform in this common coefficient class, so allowing
the vectors to vary with T,X does not change the constants. Equation
(8) applies to both factors; a zero block is omitted before normalization.

For either cross orientation the source's auxiliary function is exactly
G(z)=exp(z^2)(1+L^2 z^2). Its fixed-strip decay and any fixed number
of derivatives therefore cost only a fixed power of L. The other shift
factors occur on polynomial ranges, with shifts O(1/L). The reused
source operations require finitely many such bounds at any fixed error
precision. Choosing their total arbitrary positive power loss at most
1/160 and absorbing the remaining fixed logarithmic power in T^(1/160)
justifies the total 1/80 allowance. This is only for delta=+/-2i/L;
no uniform assertion through delta=0 is being inferred.

**Exact phases and translations.** Put h=log(m*n/d^2), so H=ell_t-h.
For the (+,-) cross block, Z(t+1/L) times conjugate(Z(t-1/L))
equals the source zeta product with alpha=beta=i/L, multiplied by
exp(i[theta(t+1/L)-theta(t-1/L)]). The Dirichlet factors remain
P_+(t) conjugate(P_-(t)), with no translation of their coefficients.
The restored lcm coefficient is q_mn. The two remaining phase products
in (10) are, exactly,

    exp(i*(ell_t/L+epsilon_t))*exp(-i*h/L)
        =exp(i*epsilon_t)*exp(i*H/L),
    exp(i*(ell_t/L+epsilon_t))*exp(-i*h/L)
        *exp(2i*(h-ell_t)/L)
        =exp(i*epsilon_t)*exp(-i*H/L).

This verifies both signs in R_t. Since the two zeta values are complex
conjugates, R_t is real; its m,n symmetry is explicit. Reversing the
blocks conjugates this expression and swaps the coefficient indices,
giving exactly the real cross term in (2). The small estimate for
epsilon_t in the proof is unnecessary for the identity and is never
used to delete it.

In a diagonal block, v=t+s/L gives
n^(-it)=n^(i*s/L)n^(-iv). Its coefficient vector is therefore
D_s c_s, and its weight is w((v-X)/T-s/(T L)), with the minus sign
shown in the proof. BCR's logarithm is log(v/(2*pi))+2*gamma;
returning to t yields precisely A_(t,s). Neither rotation nor shift
of the logarithm can be dropped. This also checks Hermitian reality
of each diagonal form for complex coefficients.

**Every remainder and the threshold.** With both source lengths
Y_j^(1/4), their product has exponent 1/2, and their sum contributes
the exponent 1/4. The three Pratt--Robles exponents, including the
allowance, are respectively

    1/2+1/8+1/80=51/80,
    3/20+7/20+1/16+1/80=23/40,
    7/16+1/32+1/80=77/160.

The first is largest. After both normalization factors, the two cross
remainders total at most C_w N T^(51/80) S by 2||c_-||||c_+||<=S.
For the translated BCR applications the two raw exponents are

    3/20+33/80+1/80=23/40,
    1/3+1/80=83/240<23/40.

Their errors total at most C_w N T^(23/40) S and are dominated by
the cross bound. The finite number of windows changes only C_w.
Finally 1/5+51/80=67/80, proving precisely (3), not a smaller
unrestored source error.

L737's finite complex-vector inequality gives F_A(v)>=(A-4log N)Q(v).
Uniformly on both translated supports, A_(t,s)>=L-C and
4log N<=4L/5, hence A_(t,s)-4log N>=L/10 eventually. L926 at
the fixed exponent 1/4 applies to D_s c_s and preserves the Euclidean
norm; it does not assert Q(D_s c_s)=Q(c_s). Integrating w_XT,
whose integral is T, gives (4) with the same q0 for both blocks.
For S>0 the full-error ratio is bounded by

    C_w N^(5/4) T^(-29/80)/L
        <=C_w T^(1/4-29/80)/L=C_w T^(-9/80)/L ->0.

For S=0 the two vectors, norm and every form vanish. All onsets depend
only on the fixed data and imported constants, not on X or the vectors.
This validates (5) and the simultaneous quantifiers in (3)-(4).

**Audit boundary.** Equations (1)-(5) pass this separate application
audit without correction. This establishes the retained partial input
under its named imports; it is no stronger moment result than the
source-covered specialization. The ratio in (5) shows that the charged
error would be absorbable if a fixed joint margin were established.
It does not establish that margin, the contraction (11), a joint
projection exclusion, signed transfer, or any Xi sign. The prior
coercivity stop remains in force for the unchanged mechanism. All
sums in the local application are finite. No new DAG edge is needed.

## Mathlib

Full matching Mathlib coverage for this joint moment application, the
Pratt--Robles mixed moment and the BCR theorem is not checked and remains
unknown. No absence or formal-verification claim is made. Finite
Hermitian forms, complex conjugation and elementary norm inequalities
are supporting mathematics, not a checked matching library theorem.
