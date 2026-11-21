# Lemma 686: exact spatial clearing controls a fixed positive fraction of displaced nodes

## Hypotheses

Use L666's exact family. Let q>=1 be an integer, n=12q+3,
M=4q+1=n/3, x=-d=-5/4, R=11/8, U=121/64, h=27/(10n),
and t_j=j/n for 0<=j<n. Put

    a_m(e)=x+i*h*(m+1/2+e_m),       -2q<=m<2q,
    Z_e={x} union {a_m(e): -2q<=m<2q},
    e_m real, |e_m|<=1/8,
    B_u(v)=product_(0<=j<n) R*(v-t_j*u)/(U-t_j*v/u),
    W_a(u)=B_u(x)/B_u(a),
    F_e(u,z)=sum_(a in Z_e) W_a(u)/(R-a*z),
    V_e=max_(|u|=|zeta|=1) |F_e(u,zeta/32)|,
    D_e=mean_(|u|=1) sum_(a in Z_e) |W_a(u)|^2/(U-|a|^2).

The circle mean is normalized. All original residues are one;
every product factor, including j=0 and the denominator angle 1/u,
is retained. The same displacement vector is used for every angle.
Let L be an integer, 1<=L<=2q, and assume

    #{m: e_m!=0} <= 2L.                                  (1)

The displaced indices can occur anywhere in the full index range;
they need not be central, consecutive or symmetric.

## Conclusion

For n>=183 the following exact finite-n estimate holds uniformly
under (1), with no limiting local-node approximation:

    V_e >= (128/181)*(L/(150*n))^(4L)
                           -1000*n*exp(-n/6000).         (2)

In particular, for every admissible n,L with

    n>=10^6,            L<=n/10^6,                       (3)

one has

    V_e >= (64/181)*exp(-n/12500).                        (4)

Writing sigma^2=137/5000, the original diagonal satisfies

    V_e/[n*exp(-n/48)*sqrt(D_e)]
      >= (64/181)*sqrt(3*sigma^2)*exp(-3)
                      *n^(-3/2)*exp(383*n/150000) > 1.   (5)

Thus the approved original-D norm target holds with c=1 and the
absolute onset 10^6 for this fixed positive, small support fraction.
It includes any locations of at most 2*floor(n/10^6) displaced nodes.
The full cube has 4q~n/3 potentially displaced nodes and is not covered.
Inserting L=2q in (2) gives a negative lower value, not a full-cube
estimate or counterexample. This is local subfamily progress within
the assessed target, not certified originality or an RH candidate.
L684's inherited undisplaced estimate and the present specialization
have not received a separate critical audit. H/support, L683's transfer
audit, actual-Xi realization and all-degree mixed signs remain open.

## Proof

### 1. Approved scope, prior failures and standard input

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-inner-spatial-rational-response.md`.
The full-cube norm target and its hypotheses are unchanged; (1) is
a subfamily inside it. L684/L685 used an approximation to limiting
exponentials whose additive 1/n error obstructs larger support.
Only L684's undisplaced estimate (4), not that approximation, is used
below. L661 supplies its audited original-diagonal envelope.

The scoped comparison checked L650's close-pair pole-dual obstruction,
L670/L671's complete angular clearing costs, the ready rational-response
assessment and the preceding support attempts. L650 has a broader,
unseparated family and a different retained-energy functional; it does
not prohibit the explicitly paid separated-node calculation here.
L670/L671 concern their complete angular coefficient/Mahler transfers,
not this finite spatial replacement response. L669's fixed-angle
cancellation and L682's highest-moment stop supply no upper bound on
the whole small-circle resolvent. These are comparisons, not lower-bound
premises. No novelty conclusion follows from the comparison.

Import the standard maximum modulus principle for holomorphic functions
on a neighborhood of a closed disk. Its specialization below is to one
explicit reversed polynomial, including possible degree drop. The full
pole-extraction cost is computed; no general rational coercivity or
unpaid pole-isolating dual is assumed. The contour theorem underlying
L684's estimate is the standard residue theorem, precisely cited there
as Howell--Mathews, *Complex Analysis*,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html).
That contour proof is inherited, not reproved or independently audited.
No new external source, quadrature formula or source claim is used.

### 2. An exact replacement response and its anchor value

Fix u=-1 throughout this calculation and put r=1/32. Write
a_m^0=a_m(0). L684 (4), evaluated at its allowed angle theta=0,
states that for every admissible n>=183,

    F_0(-1,z)=1/(R-x*z)+E_n(z),
    max_(|z|<=r) |E_n(z)|<=1000*n*exp(-n/6000).           (6)

The undisplaced lattice is the same full lattice as here. This use of
L684 does not impose its support restriction on e, because (6) concerns
only e=0. Its complete finite contour, full angular products and
resolvent disk estimate remain the input, with no limit in n.

Choose a set S of exactly 2L indices containing every index where
e_m!=0; this is possible by (1) and 2L<=4q. Indices added for padding
have e_m=0. Define the exact rational function

    A_e(z)=1/(R-x*z)+sum_(m in S)
       [W_(a_m(e))(-1)/(R-a_m(e)*z)
                         -W_(a_m^0)(-1)/(R-a_m^0*z)].    (7)

Then F_e(-1,z)=A_e(z)+E_n(z) identically. Every term outside S cancels
in F_e-F_0. No residue or W coefficient is changed or approximated.

Let b_1,...,b_N be the labelled list consisting of a_m(e),a_m^0 for
m in S, with N=4L. Repetitions are allowed in this list, including
the identical pairs created by padding. L666 gives |b_j|<R and
b_j!=x, since every nonanchor ordinate has magnitude at least 3h/8.
The complete angular products are finite and nonzero at u=-1.
Consequently the following is a polynomial of degree at most N:

    Q_e(z)=(R-x*z)*product_(j=1)^N(R-b_j*z),
    P_e(z)=Q_e(z)*A_e(z).                               (8)

Each summand in (7) removes one linear denominator from Q_e; repeated
factors cause no difficulty. At the anchor pole z_0=R/x, all replacement
terms in P_e vanish, while the anchor term remains. Thus

    P_e(z_0)=product_j(R-b_j*z_0),
    |P_e(z_0)|=(R/d)^N*product_j |Im b_j| > 0.           (9)

This is the exact finite-n normalization. It uses the unchanged anchor
coefficient W_x=1, not an approximate exponential normalization.

### 3. The paid observation cost on the small spatial circle

For any polynomial P of degree at most N define the polynomial
P^*(w)=w^N P(r/w), with its polynomial extension at w=0. On |w|=1,
|P^*(w)|<=max_(|z|=r)|P(z)|. Since |z_0|=R/d>r, applying the
maximum modulus principle at w=r/z_0 gives

    |P(z_0)|*(r/|z_0|)^N<=max_(|z|=r)|P(z)|.            (10)

This also covers degree smaller than N and multiple factors in (8).
For |z|=r, since |b_j|<R,

    |Q_e(z)|<=(R+d*r)*[R*(1+r)]^N.

Apply (10) to P_e, use (9), and then (8). With
A_*=R+d*r=181/128 and r/[R*(1+r)]=8/363, this proves

    max_(|z|=r)|A_e(z)|
       >= A_*^(-1)*product_(j=1)^N [8*|Im b_j|/363].    (11)

No coefficient-size, sign, noncancellation or angular averaging premise
appears in (11). The price for extracting the anchor is exactly the
displayed separation product.

To bound that product for arbitrary S, order its 2L indices by
increasing |m+1/2|, breaking ties arbitrarily. The full lattice has
exactly two indices at each magnitude k-1/2, 1<=k<=2q. Hence the
j-th selected index, with k=ceil(j/2), obeys

    |m+1/2|>=k-1/2,
    |m+1/2+e_m|>=k-5/8>=3k/8.

The unshifted magnitude is also at least 3k/8. Each selected index
contributes its two labelled ordinates to (11), so

    product_(j=1)^N |Im b_j| >= (3*h/8)^(4L)*(L!)^4.

Together with (11) and h=27/(10n),

    max_(|z|=r)|A_e(z)|
       >= (128/181)*(27/(1210*n))^(4L)*(L!)^4
       >= (128/181)*(L/(150*n))^(4L).                  (12)

For the last step, the elementary log-integral comparison gives
L!>=(L/exp(1))^L, also at L=1. Since exp(1)<3,
27/[1210*exp(1)]>9/1210>1/150. Finally (6)--(7), the triangle
inequality for circle suprema and V_e>=max_(|z|=r)|F_e(-1,z)|
give (2). All suprema are attained on compact circles; denominators
have no zeros there. The same fixed displacement vector is retained.

### 4. A positive support fraction pays the entire undisplaced error

Assume (3). For 0<t<=n/10^6 the function
t*log(150*n/t) is increasing, because its derivative is
log(150*n/t)-1>0. Also log(150000000)<20: the positive exponential
series gives exp(1)>8/3, so exp(3)>18, exp(2)>7, and
exp(20)>7*18^6=238085568>150000000. It follows that

    4L*log(150*n/L) <= (4n/10^6)*log(150000000)
                                           < n/12500. (13)

Thus the first term in (2) is at least
(128/181)*exp(-n/12500). The exact error-rate margin is

    1/6000-1/12500=13/150000.

The function 1000*n*exp(-13*n/150000) decreases for n>=10^6.
At n=10^6 its exponent has magnitude 260/3>32, so, using
exp(1)>2 and 2^32=4294967296>4*10^9, its value is less than
1/4<64/181. Therefore throughout (3),

    1000*n*exp(-n/6000)
                           < (64/181)*exp(-n/12500).    (14)

Subtract (14) from the first term guaranteed by (12)--(13). This
proves (4), with every additive error paid and no 1/n approximation.

### 5. Original-D comparison and the remaining full-cube gap

L666 verifies admissibility and unit residues throughout the cube.
L661's audited envelope (3), with sigma^2=137/5000, hence gives

    D_e <= n*exp(2*(91/5000)*n+6)/(3*sigma^2).

Combining this with (4) proves the non-strict inequality in (5), since

    1/48-91/5000-1/12500=383/150000.

Its constant is greater than 1/324: use 64/181>1/3,
sqrt(3*sigma^2)>1/4 and exp(-3)>1/27. The function
383*n/150000-(3/2)*log n is increasing for n>=10^6. At that onset,
using 383/150000>1/400 and log(10^6)<20, it exceeds 2470.
Finally exp(2470)>2^9>324. This proves the strict inequality in (5)
at the same absolute onset, without replacing D_e by the anchor alone.

For the full cube one must allow L=2q=(n-3)/6. The guaranteed first
term in (2) is then less than (128/181)*900^(-4L)<exp(-n/2)
for n>=183, since 4L=2(n-3)/3>n/2 and log 900>1. It is smaller
than the subtracted error 1000*n*exp(-n/6000). Thus (2) by itself
has no positive full-cube consequence. This is a limitation of the
explicit certificate, not an upper bound on V_e or proof that every
anchor-extraction method must fail. Merely improving the old limiting
approximation was avoided; extending the support fraction to the full
cube still needs a materially stronger estimate using additional
structure. No full-family joint norm or H conclusion is asserted.

The downstream L683 transfer is a possible use, not a premise of this
proof, and retains its separate audit requirement. L657/L658's slice,
integrability and localization qualifications, H/support and actual-Xi
realization/signs are not settled here. No numerical experiment or
mathematical script is used as proof evidence.

## Mathlib

Full matching coverage of this exact replacement-response bound and its
support-fraction specialization has not been checked. The supporting
inputs are the standard maximum modulus principle, finite polynomial
algebra, factorial/logarithm estimates, and the separately qualified
L684 contour and L661 diagonal bounds. No new named Lean theorem or
formal verification is claimed. Unknown full coverage is not evidence
of absence; the inherited audit qualifications remain.
