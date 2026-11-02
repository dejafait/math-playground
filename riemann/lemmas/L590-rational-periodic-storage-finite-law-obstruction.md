# Lemma 590: a finite-law obstruction to the specified rational storage family

## Hypotheses

Use L586's ordinary six-coordinate vector, jet, covariance and spectral data:

    v=(x_0,y_0,z_0,x_1,y_1,z_1),
    J_h(t)=(h(t),h'(t),h''(t),h(t+1),h'(t+1),h''(t+1)),
    C(h)=P^(-1) integral_0^P J_h(t)J_h(t)^T dt,
    I=[-1/2,1/2],
    A_((r,j),(s,k))(u)=Re((iu)^j(-iu)^k exp(i(r-s)u)),
    K=integral_I A(u) du,
    C_I={finite sums sum_l alpha_l A(u_l):alpha_l>=0, u_l in I}.

Here r,s in {0,1} and j,k in {0,1,2}. Let

    Q(v)=max(0,x_0 z_0-y_0^2),
    w=(x_0,y_0,x_1,y_1),   dot_w=(y_0,z_0,y_1,z_1),
    R(x,y)=x^3 y/(x^2+y^2) for (x,y)!=(0,0), R(0,0)=0,
    V(w)=W(w)+c R(x_0,y_0).

The coefficient c is any real number, and W(w)=w^T S w for any real
symmetric four-by-four S. Thus every homogeneous quadratic storage
in these four states, including every lag-cross term, is allowed.
Put D V(v)=gradient V(w) dot dot_w; the asserted differentiability
of R is proved below. Suppose a real symmetric six-by-six H satisfies
both inequalities on the entire six-dimensional state domain:

    v^T H v-D V(v)>=0                         for all v in R^6,
    v^T H v-D V(v)-(x_0 z_0-y_0^2)>=0          for all v in R^6.  (1)

For a sufficient periodic upper bound also require

    trace(H A(u))>=0 for every u in the closed interval I.       (2)

The trace is the full matrix trace. No compact state restriction,
frequency grid, prescribed period, stationary finite law, autonomous
flow, probability normalization of C_I, or dual attainment is assumed.
Only L473's exact finite-matrix facts are used, not its arithmetic
moment imports, corrected height-dependent law or actual Hardy jets.

## Conclusion

The extension R is globally C1, with quadratic growth and a gradient
of at most linear growth. For every smooth real P-periodic h, P>0,
with K-C(h) in C_I, (1)--(2) imply the sufficient upper bound

    P^(-1) integral_0^P Q(J_h(t)) dt <= trace(HK).                (3)

However, every H,S,c satisfying (1) alone has

    trace(HK)>=625/48384>1/288,
    625/48384-1/288=457/48384.                                  (4)

Thus the entire specified W+cR family cannot give a cost below
1/288, even before imposing the full-I condition (2). This is an
exact obstruction, not a solver failure or a sampled positivity test.
It does not assert an optimal cost, a periodic path attaining this
clipped mean, an obstruction to other nonlinear storage, or any
actual-Xi sign. The independent conceptual audit in Section 6 passes. The local
specialization uses known sufficient machinery; no originality beyond
the scope of the saved source comparison is claimed.

## Proof

### 1. Source import, origin and periodic applicability

Import only the sufficient pointwise-dual/zero-divergence method from
A. Chernyavsky, J. J. Bramburger, G. Fantuzzi and D. Goluskin,
*Convex relaxations of integral variational problems: pointwise dual
relaxation and sum-of-squares optimization*,
[arXiv:2110.03079v1, Section 2.1, Lemma 2.1 and (2.4)--(2.11)](https://arxiv.org/pdf/2110.03079v1).
The admissible C1 field and integrable chain-rule conditions are also
stated in G. Fantuzzi, *Verification of some functional inequalities
via polynomial optimization*,
[arXiv:2201.00362v1, Section 3.1, (7)--(10), Lemma 5, PDF p.3](https://arxiv.org/pdf/2201.00362v1).
Their relevant statements and proof cases were inspected in the prior
assessment `drafts/literature/2026-10-31-rational-periodic-storage-test.md`.
We reuse that assessment without a new source-proof audit. Neither
source supplies (4). No general divergence theorem is reproved here;
the following verifies the changed field's precise applicability.

Write d=x^2+y^2 and r=sqrt(d). Off the origin, the quotient rule gives

    R_x=x^2 y(x^2+3y^2)/d^2,
    R_y=x^3(x^2-y^2)/d^2.                                      (5)

Since |xy|<=d/2,

    |R(x,y)|<=x^2/2<=r^2/2,
    |R_x(x,y)|<=3|y|<=3r,
    |R_y(x,y)|<=|x|<=r.                                        (6)

The first bound implies |R(x,y)|/r -> 0 at the origin, so R is
Frechet differentiable there with derivative zero. The two derivative
bounds make the off-origin gradient converge to that zero derivative.
Together with smoothness off the origin, this proves global C1 and
|gradient R|<=sqrt(10)r. This argument neither assumes C2 regularity
nor deletes the denominator-zero set.

For the derivative data (y,z), define D R(0,0,z)=0. Formula (5) gives

    D R(x,y,z)
      =x^2 y^2(x^2+3y^2)/d^2+x^3(x^2-y^2)z/d^2              (7)

off the origin. The global bounds (6) imply

    |D R(x,y,z)|<=3y^2+|xz|<=3y^2+(x^2+z^2)/2.                (8)

At x=y=0 this remains valid for every z. In particular the whole
zero-denominator plane in R^6 is retained in (1), with D R=0 there.
The homogeneous quadratic W also has quadratic growth and a gradient
of at most linear growth. Thus V and its composition derivative have
the p=2 growth/integrability required by the sufficient method; the
constant may depend on S and c, which are fixed for each certificate.

For a fixed smooth periodic h, set

    w_h(t)=(h(t),h'(t),h(t+1),h'(t+1)).

The ordinary C1 chain rule applies even at crossings of
(h(t),h'(t))=(0,0). Its derivative is exactly D V(J_h(t)); no third
derivative is used. The state and derivative are bounded on [0,P],
so (8) and the quadratic bound for W ensure integrability. Periodicity
gives w_h(P)=w_h(0), including h(P+1)=h(1) and h'(P+1)=h'(1).
The fundamental theorem of calculus therefore verifies the source's
zero-flux hypothesis for every P>0, without a lag commensurability
condition:

    integral_0^P D V(J_h(t)) dt=V(w_h(P))-V(w_h(0))=0.           (9)

Both branches in (1) are equivalent to

    v^T H v-D V(v)>=Q(v).                                    (10)

Applying the imported sufficient method with (9) gives
average Q(J_h)<=trace(H C(h)). To verify the last bound in (3), use
L588 Section 1's necessary finite-cone implication: if
K-C(h)=sum_l alpha_l A(u_l), then (2) gives

    trace(H(K-C(h)))=sum_l alpha_l trace(H A(u_l))>=0.          (11)

This is the actual finite cone with all u_l in closed I, with no
closure or ambient-PSD substitution. Also
trace(H vv^T)=v^T H v includes both off-diagonal copies. These facts
prove (3) with precisely the full-trace convention in the hypothesis.

### 2. The original witness does not by itself obstruct every c

For x=epsilon, y=v, z=k epsilon, epsilon in {+1,-1}, put q=v^2.
Then x^2=1 and xz=k. Formula (7) reduces exactly to

    D R=[q(1+3q)+k(1-q)]/(1+q)^2.                            (12)

The signs of epsilon and v drop out, while Q=max(0,k-q).
In L473 Section 4's original B, k has probabilities 1/6 and 5/6
at 1/12 and -7/60, hence E k=-1/12; q is independent with equal
probabilities at 0 and 1/6. The two conditional derivative means
in (12) are -1/12 and 13/98. Consequently

    E D R(B)=(-1/12+13/98)/2=29/1176.                        (13)

L589's quadratic cancellation would therefore only yield
trace(HK)>=1/144+c*(29/1176) from that law. For negative c this
does not furnish a uniform obstruction. Nonzero (13) alone gives
neither a successful certificate nor a periodic realization. The next
finite witness addresses this specific failure without changing V.

### 3. A modified bounded law annihilates the rational derivative

Let epsilon and sigma be independent uniform signs, and let k and q
be independent of these and of each other, with laws

    P(k=1/12)=1/6,       P(k=-7/60)=5/6,
    P(q=0)=625/672,      P(q=1)=38/672,      P(q=2)=9/672.

Set

    X=epsilon,   Y=sigma sqrt(q),   Z=k epsilon,
    Btilde_0=(X,Y,Z).                                        (14)

At q=0 both sigma choices coincide. Thus this marginal has at most
twenty atoms. All variables are bounded and all its means are zero.
The probabilities sum to one, and

    E q=(38+18)/672=1/12,
    E k=-1/12,             E k^2=1/80.

Independence and symmetric signs give E XY=E YZ=0. Also X^2=1,
XZ=k and Z^2=k^2. Hence its complete second matrix is

    E Btilde_0 Btilde_0^T=K_0
       =[[1,0,-1/12],[0,1/12,0],[-1/12,0,1/80]],             (15)

exactly L473's same-height block. This verifies every entry, not just
the diagonal or the expectation of the clipped observable.

For completeness, the exhaustive (q,k) table is below. It suffices
for D R and Q because (12) eliminates both independent signs.

| q | k | probability | D R | Q |
| --- | --- | --- | --- | --- |
| 0 | 1/12 | 625/4032 | 1/12 | 1/12 |
| 0 | -7/60 | 3125/4032 | -7/60 | 0 |
| 1 | 1/12 | 19/2016 | 1 | 0 |
| 1 | -7/60 | 95/2016 | 1 | 0 |
| 2 | 1/12 | 1/448 | 167/108 | 0 |
| 2 | -7/60 | 5/448 | 847/540 | 0 |

Equivalently, the conditional derivative means at q=0,1,2 are
-1/12, 1 and 169/108. Their weighted sum cancels exactly:

    E D R(Btilde_0)
      =(625*(-1/12)+38+9*(169/108))/672
      =(-625+456+169)/(12*672)=0.                            (16)

Since k<=1/12, clipping is positive only at q=0,k=1/12. Thus

    E Q(Btilde_0)=(625/672)*(1/6)*(1/12)=625/48384.             (17)

### 4. Restore every cross-lag moment and test the whole family

Write L473's positive definite K as [[K_0,D_0],[D_0^T,K_0]].
The inverse of K_0 and the positive square root of the Schur complement

    T_0=K_0-D_0^T K_0^(-1)D_0>0

exist by L473 Sections 3--4. Use its same extension, with the new
marginal (14): for an independent vector e of three independent
uniform signs, put

    Btilde_1=D_0^T K_0^(-1) Btilde_0+T_0^(1/2)e,
    Btilde=(Btilde_0,Btilde_1).                               (18)

This is a necessary specialization to a changed marginal, not a new
general extension theorem. Since E e=0 and E ee^T=I_3, (15) yields

    E Btilde_0 Btilde_1^T=K_0 K_0^(-1)D_0=D_0,
    E Btilde_1 Btilde_1^T
       =D_0^T K_0^(-1)D_0+T_0=K_0.

Mixed terms with e vanish by independence and centering. Therefore

    E Btilde=0,            E Btilde Btilde^T=K.              (19)

The extension has at most 160 atoms and finite norm. Its first three
coordinates are unchanged, so (16)--(17) hold for the full law.
No numerical eigenvalue bound or path-realization theorem is needed.

Apply L589 Section 2's exact quadratic cancellation to (19). It states
that every allowed W satisfies E D W(Btilde)=0: for all four-state
indices a,b, K_(a+,b)+K_(a,b+)=0, including every lag-cross pair.
All successor coordinates have derivative order at most two. This
statement is about the full second matrix, so the changed higher
moments of Btilde do not affect its applicability. Combining it with
(16) gives, for every real c and every symmetric S,

    E D V(Btilde)=E D W(Btilde)+c E D R(Btilde)=0.             (20)

Now evaluate (10) at every atom of Btilde and take the finite weighted
sum. All quantities are integrable because this law is bounded.
Using (17), (19) and (20),

    trace(HK)=E[Btilde^T H Btilde]
       >=E Q(Btilde)+E D V(Btilde)=625/48384.                 (21)

Since 48384=168*288, subtraction of 1/288 gives exactly
(625-168)/48384=457/48384>0, proving (4).
This step uses only the two global branches (1). Condition (2) cannot
evade it, regardless of its full-I feasibility. The finite law is only
a test measure for a global inequality; it has not been claimed to be
a stationary process or the occupation law of a periodic path. Nothing
here justifies replacing actual Xi data by this law or inferring a
bound for a larger storage class whose derivatives need not cancel.

### 5. Exact arithmetic evidence and qualifications

Run, relative to the notebook,

    python3 scripts/rational-periodic/verify_finite_witness.py

It writes `scripts/rational-periodic/finite-witness-certificate.json`.
The original four-row and modified six-row reduced tables were checked
with exact rational arithmetic, including normalization, E q, E k,
E k^2, every K_0 entry, E D R, E Q and the strict threshold margin.
All checks pass with zero failures. The complete `/old_law`, `/new_law`
and `/failures` values were inspected using
`python3 ../scripts/loop/inspect_json.py` with the selected pointer
and `--full`; no bounded preview is being used as verification.
The script does not verify differentiability, a symbolic full-K
extension, periodic flux, or global certificate feasibility. Those
analytic and logical obligations are proved above and checked separately
in Section 6.

### 6. Independent conceptual audit, 31 October 2026

This audit checks the previously written assertion (4), with unchanged
hypotheses, constants and direct inputs. It reuses the invocation-start
SPECIALIZE assessment
`drafts/literature/2026-10-31-l590-independent-audit-scope.md` and the
saved primary hypotheses in the construction assessment. The general
source proofs are still imports, not independently audited here. No
sharp-duality theorem, stationary realization or arithmetic moment
theorem is needed for the implications being checked.

**Origin and integrability.** Differentiating x^3 y/d gives numerators
3x^2 y d-2x^4 y and x^3 d-2x^3 y^2, respectively, which reduce to
(5). The bounds follow from x^2(x^2+3y^2)<=3d^2 and
x^2|x^2-y^2|<=d^2. The bound |R|<=r^2/2 establishes the Frechet
derivative zero at the origin, not merely directional derivatives.
Both partial derivatives then converge to zero, so the extension is
C1 on the whole plane. With the zero derivative at the origin,
|D R|<=3y^2+|xz| holds for every (x,y,z), including x=y=0 with
arbitrary z. In particular no atom or path crossing is discarded.

For the operator norm of S,

    |D W(v)|<=2||S|| |w| |dot_w|
             <=||S|| (|w|^2+|dot_w|^2)<=2||S|| |v|^2.

Together with (8), |v^T H v|<=||H|| |v|^2 and
Q(v)<=(x_0^2+z_0^2)/2, this verifies the quadratic integrability
of every tested term. The field V itself has quadratic growth and
linear-gradient growth. These are the stated p=2 sufficient-method
conditions, and smooth periodic states in particular satisfy them.
Only h, h' and h'' occur. Applying the ordinary C1 chain rule to
w_h on [0,P] is valid even at an origin crossing; periodicity gives
both h(P+1)=h(1) and h'(P+1)=h'(1). Thus the complete boundary flux
vanishes for every P>0, including periods incommensurate with one.

**Complete finite witness.** The reduced derivative (12) follows by
substituting x^2=1, y^2=q, z=kx into each term of (7); both signs
drop out before taking expectations. For the old law, the q=1/6
expression is (9+30k)/49, giving 23/98 and 11/98 in its two rows.
Together with its q=0 rows these yield 29/1176, confirming that the
old law alone is inconclusive when c is arbitrary.

For the modified law, all probabilities are nonnegative and
625+38+9=672. The complete new six-row table in Section 3 was checked:
at q=1 the derivative is one for either k; at q=2 it is (14-k)/9,
giving exactly 167/108 and 847/540. The signs in (14) are independent
and centered, so E X=E Y=E Z=E XY=E YZ=0, while

    E Y^2=56/672=1/12,
    E XZ=1/72-7/72=-1/12,
    E Z^2=1/864+49/4320=1/80,   E X^2=1.

These are all nine entries of the symmetric second matrix (15),
including the negative XZ entry. The conditional derivative means
are -1/12, 1 and 169/108; their weighted sum has numerator
-625+456+169=0 over 8064. Since the largest k is 1/12, the only
positive clipping row is q=0,k=1/12, of probability 625/4032.
This verifies both the exact cancellation and 625/48384 clipped mean.
The marginal has four atoms at q=0 and eight at each of q=1,2,
so the claimed twenty-atom bound also includes the coincident signs.

**Every cross-lag entry and every quadratic storage term.** L473's
Gram formula uses exactly the spectral phases in the hypotheses here.
If its quadratic form vanishes, the entire function
P_0(iu)+e^(iu)P_1(iu) vanishes; evaluation at u=iv, v tending to
positive infinity, forces P_0=0 and then P_1=0. This verifies strict
positivity of this K without any arithmetic-source premise. Its
same-height block is (15), since the integrals of 1,u^2,u^4 over I
are 1,1/12,1/80 and odd integrands vanish. Thus K_0 is invertible.
For nonzero b, evaluating K on (-K_0^(-1)D_0 b,b) proves
b^T T_0 b>0, justifying the real symmetric square root in (18).

Replaying (18) with the changed marginal gives the complete blocks
D_0 and D_0^T K_0^(-1)D_0+T_0=K_0. The mixed noise terms vanish
by independence and centering. The extra eight sign states leave the
first marginal unchanged and give at most 160 bounded atoms. No
independence of the two lagged marginals is assumed.

For each of the sixteen ordered pairs a=(r,j), b=(s,k) of the four
storage coordinates, j,k are zero or one. The integrand for the sum
of successor entries is

    Re((iu)^j(-iu)^k exp(i(r-s)u) (iu+(-iu)))=0.

Both successors are among the six available jet coordinates. This
checks the entire quadratic derivative sum, including both copies
of every cross term and the y_0 y_1 term; it uses no third derivative.
It agrees with the complete pair table in L589's independent audit.
Therefore (19) suffices for E D W=0 under the changed law, and (16)
then proves E D V=0 for every real c, without differentiation under
expectation or a stationarity assumption.

**Global inequalities, trace and scope.** The two inequalities (1)
give a common left side at least max(0,x_0 z_0-y_0^2). Both branches
are retained. Integrating them along a periodic path with the checked
zero flux yields trace(H C(h)); applying (2) to a finite nonnegative
representation of K-C(h) gives trace(H C(h))<=trace(HK). Nodes at
both closed endpoints of I are permitted. There is no PSD replacement,
cone-closure assertion or missing factor of two in the full trace.

Independently of that sufficient periodic application, the globally
imposed branches hold at every atom of (18). Their finite weighted
sum is exactly (21), because the full second matrix is K and the
entire storage derivative has mean zero. The law need not be an
occupation measure to test a global inequality. Finally
48384=168*288, so the excess over 1/288 is exactly 457/48384>0.
This proves the class-wide stop even without (2), but proves neither
that the lower bound is optimal nor that a periodic path attains it.

The existing exact-arithmetic script was replayed with zero failures;
the complete `/old_law`, `/new_law` and `/failures` certificate values
were inspected with the JSON inspector's selected-pointer `--full`
mode. Its code checks the displayed rational tables, not the analytic
steps just audited. The audit passes without repairing the argument.
This is verification of the existing local obstruction, not a new
bound or progress on actual-Xi signs. General clipping, bounded
periodic realization and nonlinear actual-Xi transfer remain open.

## Mathlib

Full matching Mathlib coverage for this specified rational-storage
obstruction and its finite law has not been checked. The ordinary
C1 chain rule, fundamental theorem of calculus, finite-dimensional
positive square root, finite sums and trace identities are supporting
standard mathematics, not a claimed formalization of (4). No full
matching theorem or Mathlib theorem identifier is asserted; unknown
coverage is not evidence of absence.
