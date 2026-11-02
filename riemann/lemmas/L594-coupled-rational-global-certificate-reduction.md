# Lemma 594: exact reduction of the stipulated coupled rational certificate

## Hypotheses

Use real coordinates v=(x,y,z,X,Y,Z), w=(x,y,X,Y) and
dot_w=(y,z,Y,Z). Let P be any real homogeneous quartic in w, and set

    q(w)=x^2/2+6y^2+X^2/2+6Y^2,
    V(w)=P(w)/q(w) for w!=0,       V(0)=0,
    B(v)=xz-y^2,                  Q(v)=max(0,B(v)).

Let H be any real symmetric six-by-six matrix. For a polynomial F in
w write D F(v)=gradient F(w) dot dot_w; once regularity has been
proved, use the same definition for V. Define homogeneous sextics

    F_b(v)=q(w)^2 [v^T H v-b B(v)]-q(w) D P(v)+P(w) D q(v),
    b=0,1.                                                     (1)

Use the exact spectral data and finite cone in L586:

    I=[-1/2,1/2],
    A_((r,j),(s,k))(u)=Re((iu)^j(-iu)^k exp(i(r-s)u)),
    K=integral_I A(u) du,
    C_I={finite sums sum_l alpha_l A(u_l):alpha_l>=0,u_l in I}.

The index order is r=0,1 and j=0,1,2, matching v. For a smooth real
P_0-periodic function h, P_0>0, let J_h and C(h) be L586's lag-one
six-jet and its period-averaged raw second matrix. The period P_0 is
unrelated to the numerator P. No cutoff on v, extra parity restriction,
positivity of V, path realization of an arbitrary law, or cone closure
is assumed.

## Conclusion

V is globally C1, has quadratic growth, and its gradient has linear
growth. Its derivative at w=0 vanishes, so D V(0,0,z,0,0,Z)=0 for
arbitrary z,Z. Both of the following conditions are equivalent:

    v^T H v-D V(v)>=0 and
    v^T H v-D V(v)-B(v)>=0 for every v in R^6;              (2)

    F_0(v)>=0 and F_1(v)>=0 for every v in R^6.             (3)

Moreover the first branch of (2) alone implies

    trace(H A(u))>=0 for every real u,                     (4)

including zero and both endpoints of I. Thus no additional frequency
enclosure is needed for the cone condition once the global first
branch has been established. If (2) holds and K-C(h) belongs to the
actual finite C_I, then

    average Q(J_h)<=trace(HK).                             (5)

An exact sum-of-squares identity for each sextic in (1) is sufficient
for (3). This statement does not assert a certificate with cost below
1/288, any optimum or family-wide obstruction. Neither nonnegative
sextics nor this fixed-degree SOS subclass have been proved feasible
at that cost. These are local applicability/reduction results for an
imported method, not a new general rational-duality theorem or an RH
claim. This write-up has not had a separate critical audit.

## Proof

### 1. Precise known method and the zero extension

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-10-31-coupled-rational-global-certificate-scope.md`.
Import only the sufficient rational pointwise-dual method in
A. Chernyavsky, J. J. Bramburger, G. Fantuzzi and D. Goluskin,
*Convex relaxations of integral variational problems: pointwise dual
relaxation and sum-of-squares optimization*,
[arXiv:2110.03079v1, Lemma 2.1, (2.4)--(2.11), and Remark 3.1,
printed pp.8--10 and 14--16](https://arxiv.org/pdf/2110.03079v1).
Remark 3.1 permits a fixed nonnegative denominator, clearing interior
constraints by its square, provided zeros do not make the field
inadmissible. The C1 field/integrable chain-rule conditions are also
given in G. Fantuzzi, *Verification of some functional inequalities via
polynomial optimization*,
[arXiv:2201.00362v1, Lemma 5, (7)--(10), PDF p.3](https://arxiv.org/pdf/2201.00362v1).
The ready assessment inspected these cases. No converse, fixed-degree
SOS completeness, Lyapunov theorem or independent audit of the source
manuscripts is imported. The following checks the exact specialization,
especially the denominator-zero cases omitted by formal division.

Write r=|w|, M_0=max_{|a|=1}|P(a)| and
M_1=max_{|a|=1}|gradient P(a)|. These constants are finite by
continuity on the compact sphere. Polynomial homogeneity gives
|P(w)|<=M_0 r^4 and |gradient P(w)|<=M_1 r^3. Also

    r^2/2<=q(w)<=6r^2,             |gradient q(w)|<=12r.

Off zero, the quotient rule therefore gives

    |V(w)|<=2M_0 r^2,
    gradient V=gradient P/q-P gradient q/q^2,
    |gradient V(w)|<=(2M_1+48M_0)r.                       (6)

The first bound proves Frechet differentiability of the zero extension
at the origin with derivative zero: |V(w)|/|w| tends to zero. The last
bound proves continuity there of the off-origin gradient, agreeing
with that derivative. Smoothness off zero proves global C1. The bounds
extend to zero. In particular, with C=2M_1+48M_0,

    |D V(v)|<=C |w| |dot_w|<=C |v|^2.                     (7)

Both state vectors have norm at most |v|. These estimates verify the
quadratic value and p=2 integrability conditions for each fixed P;
there is no claim of constants uniform over all numerators. They also
show that D V is continuous on all R^6, including w=0 with arbitrary
accelerations. Indeed there the gradient is zero.

### 2. Denominator clearing with the entire zero set restored

For w!=0, q(w)>0 and the quotient rule gives

    F_b(v)=q(w)^2 [v^T H v-D V(v)-b B(v)].                (8)

Thus (2) implies (3) off w=0, and at w=0 all terms in (1) vanish,
which proves (3) everywhere. Conversely, (3) and (8) prove both
inequalities of (2) off w=0. Fix arbitrary z,Z and approach
v_0=(0,0,z,0,0,Z) by v_n=(1/n,0,z,0,0,Z). Continuity of D V,
of B, and of the quadratic form passes both inequalities to v_0.
In particular this forces (z,Z)^T H_{acc,acc}(z,Z)>=0; the value
F_b(v_0)=0 by itself would not force that conclusion. This verifies
the entire two-dimensional zero-denominator set, not just v=0.
It proves the claimed equivalence without assuming positivity of H.

### 3. Periodic zero flux and the automatic spectral condition

For each smooth periodic h, its four-state path w_h is C1 and
dot_w_h=(h',h'',h'(t+1),h''(t+1)). The ordinary C1 chain rule is
valid even at w_h=0. All terms are integrable on its compact period
interval by (7). The endpoints agree also at lag one, since
h(P_0+1)=h(1) and h'(P_0+1)=h'(1), for every P_0>0. The fundamental
theorem of calculus therefore gives

    integral_0^{P_0} D V(J_h(t)) dt=0.                    (9)

This is the required source zero-flux specialization; no extra jet,
common period, lag commensurability or uniform compact state domain
has been assumed.

For u!=0 use L586 Section 1's exact generator
g_u(t)=sqrt(2)cos(ut), with period 2pi/|u| and C(g_u)=A(u).
Integrate the first branch of (2) along this path and use (9). This
gives trace(H A(u))>=0, with the full trace. At u=0 use g_0(t)=1
with any positive period; its jet is (1,0,0,1,0,0), its second matrix
is A(0), and D V=0 directly. This proves (4) for every real u,
so in particular on the stipulated closed I. It uses an established
exact generator, not a sampled frequency test or a closure argument.

The two global branches assert v^T H v-D V(v)>=Q(v). Integrating
and using (9) gives average Q(J_h)<=trace(H C(h)). If
K-C(h)=sum_l alpha_l A(u_l) with the required nonnegative finite
weights and nodes in I, then (4) gives

    trace(H(K-C(h)))=sum_l alpha_l trace(H A(u_l))>=0.

This proves (5) with all cross-lag entries and both off-diagonal
copies in the trace. No PSD replacement of the spectral cone is used.

### 4. The precise sufficient computational subclass

The 35 degree-four monomials in the four states span all permitted P.
Each F_b has total degree six and acceleration degree at most two,
where acceleration degree means total exponent of z and Z. A
sufficient SOS test uses the 40 cubic monomials with acceleration
degree at most one: 20 pure-state cubics, and z or Z times each of
the 10 pure-state quadratics. With this monomial vector m(v), exact
identities F_b=m^T G_b m and real symmetric G_b>=0 imply (3) by
the finite-dimensional spectral theorem. These conditions are linear
in H, the coefficients of P and the entries of G_b except for the
PSD constraints. This sufficient subclass is all that is used here;
no failure of its numerical search decides polynomial nonnegativity.

The bounded experiment in
`scripts/coupled-flux/rational_sos_probe.py` uses the invertible rational
coordinate change t=(x,4y,8z,X,4Y,8Z). In these coordinates

    q=t_0^2/2+3t_1^2/8+t_3^2/2+3t_4^2/8,
    dot_(t_0,t_1,t_3,t_4)=(t_1/4,t_2/2,t_4/4,t_5/2),
    B=t_0 t_2/8-t_1^2/16.

It retains every quartic coefficient. If T=diag(1,4,8,1,4,8), then
K_t=T K T and H=T H_t T, so trace(HK)=trace(H_t K_t).
The script equates coefficients of the two sextics with the two Gram
forms. There are 301 possible sextic monomials of acceleration degree
at most two per branch: 84+112+105. The additional cost equation uses
a nonnegative slack and the trial threshold 1/300<1/288. This stricter
trial is sufficient for success and cannot be used to reject the
original threshold even if rigorously infeasible.

Rational Taylor arithmetic forms the spectral-matrix approximation
before floating conversion. For lag difference d=r-s, the entry's
truncation through n=24 before state scaling is

    sum_{0<=n<=24, j+k+n even}
      (-1)^((j-k+n)/2) d^n/[n! 2^(j+k+n)(j+k+n+1)].

For |d|=1 its absolute entry error is at most
2/[25! 2^(j+k+25)(j+k+26)], by the exponential Taylor remainder
and exp(1/2)<2. For d=0 it is exact. Multiply this error by T_aa T_bb
for the scaled entry. Floating solver iterates are not exact identities
or PSD certificates; the retained files explicitly mark them as probes.
No numerical iterate is used in the proofs of (2)--(5).

### 5. Exact rejection of one apparently cheap numerical candidate

The bounded floating SOS experiment does not solve the family problem.
The first run used 12000 projection iterations; a warm-started
refinement used 300000. The latter still had scaled coefficient/cost
residual about 0.000925575 and an affine Gram minimum eigenvalue about
-0.000690697. Its apparent cost about 0.003440041 is not a certificate.
These diagnostics are numerical, not infeasibility bounds. They are
saved in `scripts/coupled-flux/rational_sos_probe_refined.json`, with
the full coefficient maps and iterates in the adjacent `_maps.npz` file.

There is also an exact failure of the following explicit rounded
candidate. In the scaled t coordinates of Section 4 let H_t be
10^(-9) times the integer matrix

    [ 3024389956,  365438984,   15034633, -2988698054,  233110522,  43754072]
    [  365438984,  760727286,   61310813,  -467984907, -648877812, 225164103]
    [   15034633,   61310813,  146231989,    85709012, -218613028,  25802259]
    [-2988698054, -467984907,   85709012,  2974952869, -142417982,  -5287332]
    [  233110522, -648877812, -218613028,  -142417982,  814233870,  20894796]
    [   43754072,  225164103,   25802259,    -5287332,   20894796,  70819788].

Write a=(t_0,t_1,t_3,t_4). Enumerate all nonnegative exponent tuples
(e_0,e_1,e_2,e_3) with sum four in increasing lexicographic order,
from (0,0,0,4) through (4,0,0,0). The coefficients of P_t in this
order are 10^(-9) times the following 35 integers:

    176908878, -352338608, -126127873, 40383030, 241028719,
    104975408, 929549579, -550692571, -288044082, -128541160,
    -174464631, 710620121, 123547571, 338487433, -200239920,
    374475849, 778954259, -61593370, 369841842, -667921725,
    712301463, 768537402, 234714452, -698625516, -334455562,
    -228790807, -437449270, -645904752, -211888, 139932366,
    -380479229, 632026796, -47868294, -375839822, 29390276.

These coefficients, together with H=T H_t T and
P(w)=P_t(x,4y,X,4Y), specify one member of the original target family.
At the rational point

    t=(-515819,-568800,2060006,-478651,425782,1770449)/10^6,

substitution gives q=174758766841/400000000000>0. With the scaled
velocity in Section 4, direct differentiation of this polynomial and
the quotient rule give exactly

    t^T H_t t-D V
      =-201316183314715605829243698445752008755209
       /38175783234733751399101250000000000000000000
      <-1/200.                                             (10)

For a second way to check the substitution, multiply this fraction
by q^2; the numerator stays -201316183314715605829243698445752008755209
and the denominator becomes 200000000000000000000000000000000000000000000.
It equals q^2(t^T H_t t)-q D P_t+P_t D q exactly. Thus it is the
first global branch that fails, without any uncertainty about which
clipping branch applies. This is an exact rational counterexample to
this one candidate, not a numerical positivity test.

Using the full scaled K_t and the Taylor remainder in Section 4,
exact rational interval arithmetic also gives

    3440040029/10^12 < trace(H_t K_t)
                      < 3440040031/10^12 < 1/288.           (11)

All 36 entries contribute, including both off-diagonal copies. This
confirms that an attractive cost cannot replace the failed inequality.
The script `scripts/coupled-flux/check_rational_probe_candidate.py`
reproduces (10)--(11), their strict rational comparisons, and the
cleared-identity equality. Full exact coefficients, point, intermediate
fractions and cost interval are retained in
`scripts/coupled-flux/rational_probe_candidate_violation.json`.
The random sample used to find the point has no role in verifying it.

Neither this counterexample nor the projection residual excludes the
SOS subclass or the entire P4/q family. In particular the experiment's
1/300 target is stricter than the requested 1/288, and no conclusion
about the intervening costs follows. No global certificate, family-wide
lower bound, periodic realization or actual-Xi sign has been obtained.

## Mathlib

Full matching Mathlib coverage for this exact coupled rational family
and its reduction has not been checked. The quotient/chain rules,
Frechet differentiability, fundamental theorem of calculus, polynomial
coefficient identities and PSD Gram implication are supporting
standard mathematics, not a claimed formalization of this result.
Unknown coverage is not evidence of absence. The named primary
sufficient-method imports retain their qualifications above.
