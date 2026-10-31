# Lemma 480: the complete second moment and the remaining fourth-moment scale

## Hypotheses

Use the exact residual R_T in L477 (1)--(2), its actual theta and
fixed cutoff, and the audited complete cross-term evaluation L479.
Write

    L=log T, M=floor(sqrt(T/(2 pi))), T<=t<=2T,
    c_nm=log(n/m)^2/sqrt(nm),             1<=n,m<=M,
    U(t)=sum_(n,m<=M)c_nm exp(it log(m/n)),
    V(t)=sum_(n,m<=M)c_nm exp(-it log(nm)),
    R_T(t)=U(t)+Re(exp(2i theta(t))V(t)),
    I_j(T)=integral_T^(2T)|R_T(t)|^j dt,  j=1,2,4.

Here U is real by interchange of n,m. T tends to infinity through
arbitrary real values. The phase estimates retained from L477 are

    2theta'(t)=log(t/(2 pi))+O(T^-2),
    2theta''(t)=1/t+O(T^-3),              T<=t<=2T.       (1)

These are uniform analytic estimates for the actual phase, with the
remainder justification in L316, not formal differentiation of a
real error. No RH, simplicity, spacing, half-plane, independent-phase
or conjectural moment hypothesis is imposed. Constants and onsets
below are absolute and existential.

## Conclusion

For all sufficiently large real T there are fixed positive constants
c_2,C_2,c_4,C_4 such that

    c_2 T L^8 <= I_2(T) <= C_2 T L^8,                    (2)
    c_4 T L^18 <= I_4(T) <= C_4 T^2 L^8.                 (3)

The charge-two term in the exact second-moment expansion is O(T).
Both nonchirped squares are nonnegative and O(T L^8); no cancellation
from an unspecified cross term is omitted in (2).

The lower bound in (2) and upper bound in (3), used with the standard
interpolation inequality, certify only the following lower scale:

    I_1 >= I_2^(3/2)/I_4^(1/2)
        >= (c_2^(3/2)/sqrt(C_4)) sqrt(T) L^8.             (4)

The displayed certificate divided by T L^3 tends to zero. This does
not bound the actual quotient above by a subthreshold quantity and
does not prove I_1=o(T L^3). More precisely, on any unbounded family
of heights, a fixed positive lower bound for

    [I_2^(3/2)/I_4^(1/2)]/(T L^3)

is equivalent to a fixed upper bound for I_4/(T L^18). Thus the exact
remaining requirement for this interpolation test is

    I_4(T) <= C T L^18 along an unbounded sequence.       (5)

The certified upper bound in (3) exceeds this scale by a factor
T/L^10. Its lower bound is a necessary scale, not a proof of (5).
No bound strictly above that necessary scale is established here.

This is a new local full-second-moment input obtained from L479 and
elementary estimates under the previously assessed target. No matching
full-residual theorem was established by the recorded search; that is
not an originality claim. The separate critical audit in Section 6
accepts these bounds without correction or improvement.
It settles neither L477 defect threshold, the negative-mass saving,
any individual-height sign nor all-degree mixed positivity.

## Proof

### 1. The complete second-moment identity

Let

    A(T)=integral_T^(2T) U(t)^2 dt,
    B(T)=integral_T^(2T) |V(t)|^2 dt,
    H(T)=(1/2) Re integral_T^(2T) exp(4i theta(t))V(t)^2 dt.

The elementary identity (Re z)^2=(|z|^2+Re(z^2))/2 gives exactly

    I_2=A(T)+B(T)/2+C(T)+H(T),
    C(T)=2 Re integral_T^(2T) exp(2i theta(t))U(t)V(t)dt.
                                                               (6)

In C(T), multiplying the U index pair n,m by the V pair k,l gives
phase 2theta(t)+t log(m/(nkl)) and coefficient
log(n/m)^2 log(k/l)^2/sqrt(nmkl). Thus C(T) is exactly L479's
complete cross term, with no missing factor or different cutoff:

    C(T)=Q(T)+O(T L^6),
    c T L^8 <= Q(T) <= C T L^8.                           (7)

The second-moment identity also appears in L478; the direct check
above avoids relying on its unaudited expansion. No part of C(T)
is estimated by L478's failed coefficientwise stationary majorant.
All sums here and below are finite.

### 2. The entire charge-two contribution, including the endpoint

For a tuple n,m,k,l<=M with nonzero coefficient, put

    a=log(M/n), b=log(M/m), c=log(M/k), d=log(M/l),
    D=a+b+c+d,
    W=log(n/m)^2 log(k/l)^2.

These four logarithms are nonnegative. Nonzero W implies that at
least one index is below M, so, for M>=2,

    D>=log(M/(M-1))>=1/M,
    W=(a-b)^2(c-d)^2 <= D^4.                              (8)

The phase f(t)=4theta(t)-t log(nmkl) obeys

    f'(t)=2log(t/(2 pi M^2))+D+O(T^-2)>=D/2,
    f''(t)=2/t+O(T^-3)>0,                  T<=t<=2T,       (9)

eventually, uniformly in the tuple. Indeed T>=2 pi M^2, and the
error is o(1/M), so the small endpoint derivative is included.
Integration by parts, retaining both boundary terms, gives

    |integral_T^(2T) exp(if(t))dt|
       <=1/f'(T)+1/f'(2T)+integral_T^(2T) f''/(f')^2 dt
       =2/f'(T)<=4/D.                                   (10)

This is the elementary monotone-first-derivative calculation covered
by Tao, *247B Lecture Notes 8*, Section 2, Lemma 2.4 and its proof,
printed p. 5 ([primary notes](https://www.damtp.cam.ac.uk/user/gold/pdfs/teaching/notes8.pdf)).
The explicit boundary calculation records the uniform cost when D
shrinks with T; no stationary endpoint is discarded. When all four
indices equal M, D=0 but W=0 exactly. Every other zero-coefficient
tuple is likewise omitted before division by D.

For each fixed integer j>=0 define

    S_j(M)=sum_(n<=M) log(M/n)^j/sqrt(n),
    S_j(M)<=C_j sqrt(M).                                 (11)

For j=0 the power is 1. To verify the inequality, partition into
M/2^(h+1)<n<=M/2^h. In each nonempty block the logarithm is at
most (h+1)log 2 and the sum of n^-1/2 is at most
2sqrt(M)2^(-h/2). Summing the convergent geometric series with
the polynomial factor proves (11), including the last block at 1.
Since D^3<=(4^2)(a^3+b^3+c^3+d^3), (8)--(11) imply

    |H(T)|<=2 sum_(W!=0) W/(D sqrt(nmkl))
           <=C S_3(M) S_0(M)^3 <= C M^2 <= C T.          (12)

This treats the complete charge-two sum and every closed endpoint.

### 3. A finite mean-square estimate with an explicit time majorant

We need only a crude upper bound for each nonchirped square. For
distinct ordered real frequencies lambda_1<...<lambda_N with
adjacent separation at least delta>0, and arbitrary complex z_j,
direct finite integration gives

    integral_T^(2T) |sum_j z_j exp(i lambda_j t)|^2 dt
       <=(4T+16/(T delta^2)) sum_j |z_j|^2.               (13)

Here is an elementary proof with sufficient constants. Let
chi=1_[-T,T] and

    w(t)=(chi*chi)(t-3T/2)/T.

Then w is nonnegative, supported on [-T/2,7T/2], and is at least
3/2 on [T,2T]. Its integral is 4T. Direct multiplication of the
two interval integrals, justified on their compact rectangle, gives

    integral_R w(t) exp(i omega t)dt
       =exp(3i omega T/2) (2sin(omega T)/omega)^2/T
       for omega!=0.                                    (14)

Its absolute value is at most 4/(T omega^2). Expanding the finite
square under w, the diagonal is 4T sum |z_j|^2. Since
|lambda_j-lambda_k|>=delta|j-k| and
2|z_j z_k|<=|z_j|^2+|z_k|^2, the absolute off-diagonal is at most

    4/(T delta^2) sum_(j!=k) |z_j z_k|/(j-k)^2
       <=16/(T delta^2) sum_j |z_j|^2.

We used sum_(r>=1) r^-2<=2, so each two-sided row sum is at most
4. This proves (13). It is a special-purpose elementary version of
a standard separated-frequency mean-square estimate, not a new
general theorem. The ready literature assessment leaves the exact
Montgomery--Vaughan displays unread; this short direct proof supplies
everything needed without importing an unverified display or constant.
It uses only finite expansions and explicit interval integration,
within the assessed scope. Only the frozen sums U,V are extended to
the support of w; no gamma phase or zeta approximation is used there.

### 4. Grouping all exact coincidences and bounding both squares

For relatively prime a,b<=M, a!=b, the coefficient of frequency
log(b/a) in U is exactly

    u_ab=log(a/b)^2 H_floor(M/max(a,b))/sqrt(ab),
    H_j=sum_(d<=j)1/d.                                   (15)

This follows by the unique representation n=da,m=db. For V, the
coefficient at frequency -log h is

    v_h=sum_(nm=h; n,m<=M)c_nm,             h<=M^2.        (16)

These group every coincidence. Distinct ratios b/a and d/c have
logarithmic separation |log(bc/(ad))|>=1/M^2: the unequal positive
integers bc,ad are at most M^2, and integrating 1/x between them
gives that lower bound. Distinct integers h<=M^2 give the same
separation for their logarithms. The sorted frequencies in each sum
therefore satisfy (13) with delta=1/M^2. Since M^2<=T/(2 pi),
its multiplier is at most C T.

Both squared coefficient masses are O(L^8). In detail, (15) gives

    sum_(a,b)u_ab^2
       <=(log M)^4(1+log M)^2 (sum_(a<=M)1/a)^2
       <=C L^8.                                         (17)

If d(h) is the number of divisors of h, then
v_h<=(log M)^2 d(h)/sqrt(h). Also d(h)^2<=d_4(h), where d_4
counts ordered four-factor factorizations. An explicit injection maps
two divisors r,s of h to

    (gcd(r,s), r/gcd(r,s), s/gcd(r,s), h/lcm(r,s)).

The product is h and the first three entries recover r,s. Thus

    sum_(h<=M^2)v_h^2
       <=(log M)^4 sum_(h<=M^2)d_4(h)/h
       <=(log M)^4 (1+log(M^2))^4 <=C L^8.               (18)

The second inequality enlarges a nonnegative sum to four independent
factors each at most M^2. Equations (13)--(18) prove

    0<=A(T)<=C T L^8,   0<=B(T)<=C T L^8.               (19)

Together (6), (7), (12), (19) give the upper bound in (2).
For the lower bound, retain A,B as nonnegative and obtain
I_2>=Q(T)-C T L^6-C T>=c_2 T L^8 eventually. This proves (2)
for every sufficiently large real T, without favorable endpoint or
phase selection.

### 5. Complete fourth-moment bounds and the exact interpolation gap

By |log(n/m)|^2<=2log(M/n)^2+2log(M/m)^2 and (11),

    S=sum_(n,m<=M)c_nm <=4 S_2(M) S_0(M)<=C M.

Consequently |R_T|<=|U|+|V|<=2S<=C M at every height in the
interval. Multiplying the resulting |R_T|^4<=C M^2|R_T|^2
and integrating, using the complete I_2 upper bound in (2), gives

    I_4<=C M^2 I_2<=C_4 T^2 L^8.                         (20)

This is an upper bound for the full fourth moment, including every
charge and cross term, not for an isolated component. It needs no
eighth-moment theorem, reduced product length or sign assumption.

Tao, *245C Notes 1: Interpolation of L^p spaces*, 30 March 2009,
Lemma 9 ([primary statement and Holder proof](https://terrytao.wordpress.com/2009/03/30/245c-notes-1-interpolation-of-lp-spaces/)),
applied to Lebesgue measure dt on [T,2T], p_0=1, p_1=4 and
theta=2/3, gives

    ||R_T||_2<=||R_T||_1^(1/3)||R_T||_4^(2/3),
    I_2^(3/2)<=I_1 I_4^(1/2).                            (21)

The function is a continuous finite sum, so all norms are finite.
Equation (2) ensures I_2>0 and hence I_1,I_4>0 for the heights used.
Thus division is legitimate. The known interpolation theorem is
cited rather than reproved. Combining (21) with the previously
audited L477 bound I_1<=C T L^3 and (2) gives

    I_4>=I_2^3/I_1^2>=c_4 T L^18.                        (22)

This proves the lower part of (3); it uses an established L1 upper
bound, not the proposed L1 lower bound. Combining (21), the lower
part of (2), and (20) proves (4).

Finally (2) bounds the interpolation quotient above and below by
positive fixed multiples of T^(3/2)L^12/sqrt(I_4). This proves
the stated equivalence with (5). The certificate in (4) divided by
T L^3 is a fixed multiple of L^5/sqrt(T), which tends to zero;
the upper bound in (20) divided by T L^18 is C_4 T/L^10.
These compare certified scales only. They do not assert that the
actual fourth moment is as large as its upper envelope, or that the
actual quotient fails the target. In particular the I1 lower bound
in (4) is too small to survive L477's O(T L^(5/2)) defect-transfer
error as a positive lower bound for E(T).

### 6. Separate critical audit, 29 October 2026

The audit accepts (1)--(22) with their stated absolute existential
constants and sufficiently-large-real-T qualification. Its scope is
this complete residual calculation with the audited L477 and L479
conclusions retained as inputs. It does not independently reprove
L317's AFE, Gonek's scalar lemma or L479's arithmetic evaluation.
No new moment bound, source theorem or assumption is introduced.

First, L477 (2) makes the ratio cosine sum exactly U, since c_nm=c_mn
and the swapped exponentials are conjugates. The product cosine sum
is exactly Re(exp(2i theta)V). Thus R_T is real on the whole interval.
Expanding its square yields (6): the middle term is 2U Re(exp(2i
theta)V), and the last square contributes B/2 and H. In the middle
term the frequency is log(m/n)-log(kl)=log(m/(nkl)). The four
coefficients, ordered-pair convention, M, actual theta, interval and
outer factor 2 all agree with L479 (2)--(4). Hence its signed positive
main term Q, including its uniform O(T L^6) error, applies to this
complete cross term. L478 is only a comparison, not an additional
unverified identity used in this proof.

L477's phase estimates come from the analytic remainder in L316 (7),
whose Cauchy bounds give the required first and second derivatives.
On [T,2T] these errors are uniformly O(T^-2) and O(T^-3). For every
nonzero charge-two coefficient, all four logs in (8) are nonnegative
and some index is at most M-1; therefore D>=1/M. This holds even at
T=2 pi M^2. Since M=O(sqrt T), a single large-T onset makes the
absolute derivative error at most D/2 for every tuple. The derivative
in (9) is positive and increasing. The two boundary terms in (10)
are 1/f'(T) and 1/f'(2T); the integral of f''/(f')^2 is their
difference. Thus their total really is 2/f'(T), not a bound requiring
a fixed separation from the endpoint. The all-M tuple and every
other zero-coefficient tuple are removed before dividing by D.

The dyadic estimate (11) includes n=1 and the j=0 convention. More
explicitly, sum_(n<=x) n^-1/2<=2 sqrt x for x>=1 bounds each
nonempty block by 2 sqrt M 2^(-h/2); multiplying by
((h+1)log 2)^j gives a convergent series. The inequality
(a+b+c+d)^3<=16(a^3+b^3+c^3+d^3) then pays for the entire W/D
sum by a fixed multiple of S_3 S_0^3. Consequently (12) is a
uniform O(M^2)=O(T) bound on H, with every endpoint retained.

For (13), convolution gives the explicit nonnegative majorant
w(t)=max(2-|t-3T/2|/T,0). Its support is [-T/2,7T/2], it is at
least 3/2 on [T,2T], and its integral is 4T. Thus integration
against w bounds the desired unweighted integral from above. Formula
(14) has no missing Fourier normalization: the convention is
exp(i omega t), and each interval integral is 2sin(omega T)/omega.
The compact rectangle justifies multiplying these integrals. Sorted
adjacent separation gives |lambda_j-lambda_k|>=delta|j-k|.
After 2|z_j z_k|<=|z_j|^2+|z_k|^2, each row contributes at most
2 sum_(r>=1) r^-2<=4. The off-diagonal coefficient is therefore
at most 16/(T delta^2), as stated. The finite exponential sums alone
are extended outside [T,2T]; no phase expansion or Hardy estimate is
used on the extra support, which can include negative t.

Equation (15) groups each ratio uniquely by n=da,m=db with (a,b)=1.
The ratio 1 has zero coefficient. Distinct grouped ratios give
unequal integers bc and ad, each at most M^2. Integrating 1/x
between these integers gives |log(bc/ad)|>=1/M^2. Grouped product
frequencies obey the same bound for distinct integers h<=M^2.
Thus using delta=1/M^2 after grouping is valid for both signs of
the ratio frequencies and for every floor-cutoff value. Since
M^4/T<=T/(4 pi^2), the multiplier in (13) is O(T).

For U, the log-fourth-power bound, squared harmonic factor and two
remaining harmonic sums contribute respectively O(L^4), O(L^2)
and O(L^2), proving (17). For V, the map in Section 4 is indeed
an injection: if g=gcd(r,s), then lcm(r,s)=rs/g; the four entries
multiply to h, are positive integers, and recover r and s from
the first three. Thus d(h)^2<=d_4(h). Expanding d_4(h)/h as a
sum of reciprocal four-factor products and dropping only the
product constraint proves (18). No pointwise asymptotic for the
divisor function is used. These estimates prove the complete
nonnegative bounds (19). In particular the lower estimate for I_2
does not subtract an uncontrolled A or B: it is at least
Q-O(T L^6)-O(T), which is >=c_2 T L^8 at a common onset.

For the supremum estimate, summing 2a^2+2b^2 over each ordered
pair gives exactly 4 S_2 S_0, hence S=O(M). Each exponential has
modulus one and |Re z|<=|z|, so |R_T|<=2S uniformly. Therefore
I_4<=C M^2 I_2 is a bound on the entire fourth power, regardless
of its internal signs. It does not require termwise estimates for
the fourth-power expansion or an eighth zeta moment.

Finally the cited interpolation theorem uses ordinary Lebesgue dt,
not normalized measure: 1/2=(1-2/3)/1+(2/3)/4. Thus its norm
inequality gives exactly I_2^(3/2)<=I_1 I_4^(1/2). Positivity
of I_2 and continuity ensure both denominators are nonzero. Using
the already proved upper bound I_1<=C T L^3 gives a lower bound
on I_4, namely (22); it never assumes the desired lower bound
on I_1. Conversely (20) gives the lower certificate (4), not an
upper bound on the true interpolation quotient.

For a further check on the sequence quantifiers, let
x_T=I_2/(T L^8) and y_T=I_4/(T L^18). The normalized quotient
is exactly x_T^(3/2)/sqrt(y_T), with c_2<=x_T<=C_2. Hence a
uniform positive lower bound on that quotient along an unbounded
sequence implies a uniform upper bound on y_T along that same
sequence, and a uniform upper bound on y_T gives the converse.
All constants may depend on the chosen bounds, but not on its
heights. Discarding a finite initial segment handles the common
onset. The necessary positive lower bound on y_T does not provide
its missing upper bound. The certified ratio L^5/sqrt T tends
to zero, while the available upper envelope for y_T grows as
T/L^10. Also (4) is smaller than L477's defect-transfer error,
so it yields no positive lower bound for E(T).

The direct DAG inputs L477 and L479 account for all retained
mathematics; L316's phase enters through L477. The audit closes
the verification obligation for this local input only. Both L1
thresholds, the required fourth-moment upper scale, negative-mass
saving and all-height mixed positivity remain unresolved. The
supremum-certificate stop stands; no true-quotient failure or
RH consequence follows from this audit.

## Mathlib

Full matching theorem: not checked. Supporting finite sums, elementary
oscillatory integration, triangular convolution, harmonic/divisor
bounds and Holder interpolation: no specific declarations checked.
Unknown coverage is not absence. The external inputs used here are
the two precisely cited Tao statements, with L477's retained phase
and L1 bound and L479's audited cross-term theorem. The elementary
mean-square calculation is included for the source-access reason
given after (14); no unread general mean-value or eighth-moment
result is invoked. Local progress does not establish novelty beyond
the sources compared or any new Xi sign range.
