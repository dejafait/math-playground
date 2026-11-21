# Lemma 959: terminal completion splitting recovers the critical weight

## Hypotheses

Use the actual functions of L018 and the critical-multiplicity
conventions of L958. Thus f(z)=Xi(z)=xi(1/2+iz) is real entire, and

    H(s)=s(s-1) pi^(-s/2) Gamma(s/2)/2,       h(s)=H'(s)/H(s),
    G_u(s)=zeta'(s)+u h(s)zeta(s).

Fix an interior point x in one L958 interval (a,b), put
s0=1/2+ix, and suppose xi'(s0)=0 of finite positive order m.
Assume explicitly Re h(s0)>0. The point, its order, and its interval
are fixed before choosing any neighborhoods or perturbation scales.
No simplicity, RH, uniform zero separation or intermediate-parameter
boundary exclusion is assumed.

## Conclusion

There are delta>0 and epsilon0>0 such that, for every
0<epsilon=1-u<epsilon0, the following holds in |s-s0|<delta.
Zeros are always counted with full orders.

* If xi(s0)!=0, G_(1-epsilon) has exactly m zeros there. All are
  simple and none is on Re(s)=1/2. Exactly kappa(x) lie in
  Re(s)<1/2 and m-kappa(x) lie in Re(s)>1/2, where

      kappa(x)=m/2                         for even m,
               (m+1)/2  if m odd and f(x)f^(m+1)(x)>0,
               (m-1)/2  if m odd and f(x)f^(m+1)(x)<0.

* If xi(s0)=0 of order r, then r=m+1>=2. G_(1-epsilon) has
  exactly r-1 zeros in the disk, all at s0: it retains that entire
  persistent divisor and has no moving local zeros. These r-1
  orders remain on the boundary; they are not part of kappa or K.

Consequently this fixed-point, one-sided terminal splitting supplies
exactly the already defined noncommon critical weight, with a
separately retained common divisor. It gives no independent sign
datum or estimate for K. No assertion is made at interval endpoints,
for parameters away from 1, or uniformly as x or the local order
varies. In particular it constructs no global crossing index and
justifies no sum or height-uniform limit of these local counts.

## Proof

### Imported tool and the specialization required

Use Rouche's theorem in Tsogtgerel Gantumur, *Isolated singularities
and meromorphic functions*, author notes dated 16 April 2015,
[Theorem 15, p8](https://www.math.mcgill.ca/gantumur/math249w15/residue.pdf).
For meromorphic functions on a neighborhood of a null-homologous
cycle, |p-q|<|q|<infinity on the cycle implies equality of the
index-weighted sums of orders inside. Its holomorphic small-circle
case counts all zero multiplicities. Section 5, p9 applies this
to finite-order local zeros; neither statement assigns half-plane
sides. The saved pre-step assessment inspected the full theorem and
its homotopy proof. We specialize only this tool and local Taylor
factorization, giving the missing orientation calculation below.
There is no reproof of a general root-count theorem or novelty claim.

### 1. Exact coordinate and completion identities

Since x>0, a sufficiently small disk about s0 lies in 0<Re(s)<1,
has a<Im(s)<b, and avoids s=1. On its closure H is holomorphic and nonzero:
the factors s,s-1 are nonzero there, Gamma(s/2) is holomorphic
and zero-free, and the exponential factor is nonzero. Zeta and h
are holomorphic there. L018 and differentiation give exactly

    H(s)G_(1-epsilon)(s)=xi'(s)-epsilon h(s)xi(s).       (1)

Put s=s0+iw and F(w)=f(x+w)=xi(s0+iw). Then
xi'(s0+iw)=-i F'(w). Multiplying (1) by i yields the holomorphic
local family

    P_epsilon(w)=F'(w)-i epsilon h(s0+iw)F(w).          (2)

Multiplication by iH and this invertible linear coordinate change
preserve each zero order. Moreover

    Re(s)<1/2  if and only if  Im(w)>0.                (3)

Reality of f on the real axis makes every Taylor coefficient of
F at zero real. The order m of xi' is also the order of F'.

### 2. Noncommon root: all local roots are accounted for

Suppose F(0)!=0. Taylor expansion gives

    F'(w)=c w^m+O(w^(m+1)),  c=f^(m+1)(x)/m! in R\{0}.

Choose delta>0 so that F' has no zero in 0<|w|<=delta and the
closed disk is within the neighborhood of part 1. On |w|=delta
let d=min |F'(w)|>0 and M=max |h(s0+iw)F(w)|<infinity.
For sufficiently small epsilon>0, epsilon M<d. Rouche applied
on this circle to (2) and F' proves that exactly m zeros of
P_epsilon lie in the disk, counting all multiplicities, and none
is on its boundary. This is the fixed-disk total count; the scaling
argument next identifies every one of those m zeros.

Set tau=epsilon^(1/m)>0 and w=tau v. The scaled holomorphic family

    Q_tau(v)=tau^(-m)F'(tau v)-i h(s0+i tau v)F(tau v)

has, on each bounded v-disk, the uniform expansion

    Q_tau(v)=Q_0(v)+O(tau),
    Q_0(v)=c v^m-i h(s0)F(0).                          (4)

Indeed F'(w)=w^m(c+w B(w)) with B holomorphic, while h and F
are holomorphic at their fixed centers; substitution gives the
claimed bounded remainders, including at tau=0. The limiting roots
are the m roots of

    v^m=A,             A=i h(s0)F(0)/c,
    Im A=(Re h(s0))F(0)/c != 0.                       (5)

They are nonzero and simple, since c!=0 and the derivative of
Q_0 at such a root is mc v^(m-1)!=0. None is real, since a real
v would have real v^m. Choose disjoint closed small disks about
these roots, each wholly in its root's open upper or lower half-plane
and containing no other root of Q_0. On each boundary |Q_0| has a
positive minimum. The uniform convergence in (4), on a single
bounded set containing all these disks, permits Rouche on every
one for all sufficiently small tau>0. Thus each disk contains
exactly one root of Q_tau, counted with multiplicity; it is simple.

If R bounds all these disks, further require tau R<delta. Their
images in the w-plane supply m roots inside the fixed disk of the
preceding paragraph. Its total count is m, so no other roots occur
there, including on the real axis. All the roots retain the sides
specified by their limiting disks. For completeness they may be
labeled so that

    w_j(epsilon)=epsilon^(1/m)(v_j+O(epsilon^(1/m))).   (6)

To verify the error, on the j-th disk factor
Q_0(v)=(v-v_j)R_j(v), where |R_j| is bounded below by a positive
constant. At its unique Q_tau root, (4) gives |Q_0|=O(tau),
hence |v-v_j|=O(tau). No root plot, simple-root assumption at
epsilon=0 or uncontrolled perturbation limit is being used.

### 3. Orientation and parity give exactly kappa

If m is even, the limiting roots occur in pairs v,-v. None is
real, so exactly m/2 have positive imaginary part.

For odd m=2k+1 write A=|A|exp(i theta), with 0<theta<2pi.
By (5), theta is neither 0 nor pi. The roots have arguments

    (theta+2pi j)/m,                 j=0,...,m-1,

all strictly between 0 and 2pi. Such a root is in the upper
half-plane precisely when j<m/2-theta/(2pi). If 0<theta<pi,
this threshold is strictly between k and k+1/2, giving k+1
upper roots. If pi<theta<2pi, it is strictly between k-1/2
and k, giving k upper roots (zero if k=0).

Finally the sign of Im A is the sign of

    F(0)/c = m! f(x)/f^(m+1)(x),

which is the sign of f(x)f^(m+1)(x), since the latter derivative
is real and nonzero. Equation (3), the stable side allocation in
part 2, and this parity count give exactly all three cases of kappa
in L958. In particular the direction Re(s)<1/2 is essential; it
corresponds to the upper, not the lower, w-half-plane.

### 4. Common root: retain its complete boundary divisor

If F(0)=0, finite order of F' implies
F(w)=w^r B(w), with r=m+1>=2, B holomorphic and B(0)!=0.
Equation (2) then factors identically as

    P_epsilon(w)=w^(r-1) V_epsilon(w),
    V_epsilon(w)=r B(w)+w B'(w)
                   -i epsilon h(s0+iw)w B(w).        (7)

Choose a smaller fixed disk such that
|rB(w)+wB'(w)-rB(0)|<|rB(0)|/3 throughout its closure.
On a slightly larger allowable disk, h(s0+iw)B(w) is bounded;
shrinking the first disk again ensures
|h(s0+iw)wB(w)|<|rB(0)|/3 there. Consequently, for
0<=epsilon<=1, |V_epsilon(w)|>|rB(0)|/3 throughout this
small disk. In particular V_epsilon has no zeros there and
V_epsilon(0)=rB(0). Thus the full order r-1 stays exactly at
w=0, on Re(s)=1/2, with no other nearby roots. This case does
not require the sign assumption on h; nothing has been divided
by F before its persistent divisor was retained.

L958 excludes common roots only from K, retaining their orders in
the original zero counts. Equation (7) uses precisely that convention:
it does not declare these r-1 boundary orders to be split roots or
assign the noncommon formula for kappa to them. The two cases
exhaust every finite positive order of xi' at the fixed point. ∎

**Qualifications and stopping test.** The completed test recovers
the old critical weight exactly. It therefore stops this terminal
local-splitting mechanism as independent sign control. It does not
stop every completion-parameter strategy, nor establish K=0, an
arithmetic bound, global transfer, higher signs or RH. The explicit
Re h(s0)>0 hypothesis has not been removed or made effective at
all heights. Although the pre-step assessment records a digamma
source for future large-height applicability, no such additional
application is needed or claimed here. All scales may depend on
the fixed point and its order. This is a known-tool specialization
(REPRODUCTION), accepted by the separate critical audit below.

### Critical audit — 10 November 2026, step131

The fixed-point conditional statement passes this audit. No equation,
hypothesis or dependency needs correction. This accepts the existing
known-tool specialization and its local route stop; it adds no sign
estimate beyond the proof above or the sources checked.

**Actual family and orientation.** L018 applies throughout a closed
disk strictly inside the open s-strip, at the fixed positive height.
Every factor of H there is holomorphic and nonzero, so multiplication
by iH preserves orders and creates no zeros or poles. Directly,

    F'(w)=i xi'(s0+iw),
    iH(s0+iw)G_(1-epsilon)(s0+iw)
       =F'(w)-i epsilon h(s0+iw)F(w).

For w=p+iq, Re(s0+iw)=1/2-q. Thus upper w-roots are left
s-roots. As an independent sign check in the first-order case,
the displacement in the original coordinate is

    s-s0=-epsilon h(s0)f(x)/f''(x)+O(epsilon^2).

Its real part has the required negative sign when f(x)f''(x)>0
and the positive sign when that product is negative. This includes
both m=1 cases; the zero weight in the latter case is intentional.

**Strict contour estimates and exhaustiveness.** The fixed-circle
minimum d is positive by isolation of the finite-order F' zero.
The maximum M is finite, so epsilon M<d can be made strict.
For the scaled circles, put A_1(w)=h(s0+iw)F(w) and write
F'(w)=w^m(c+w B_1(w)). Choose one R containing all the root disks.
On a fixed closed w-disk containing |w|<=tau R, bounds M_B for
|B_1| and M_A for |A_1'| give the complete error estimate

    sup_{|v|<=R}|Q_tau(v)-Q_0(v)|
       <=tau (R^(m+1) M_B+R M_A).

The derivative bound follows on line segments in this disk; it is
valid for the actual variable h, not just a constant perturbation.
Each of finitely many scaled-circle minima of |Q_0| is positive.
Choose tau so that this error is smaller than every such minimum,
tau R<delta, and tau^m M<d. Rouche then gives one full order
on each scaled disk and exactly m in the fixed disk. Thus the
roots are simple, every root is accounted for, and no real or
additional boundary branch has escaped the scaling argument.
All these choices depend on the fixed point and m, as stated.

**Every finite order and the common divisor.** For even m the
opposite-root pairing gives m/2 upper roots. For odd m=2k+1,
the integer condition j<k+1/2-theta/(2pi) gives j=0,...,k
when Im A>0 and j=0,...,k-1 when Im A<0; the second set is
empty for k=0. Since Re h(s0)>0, these alternatives have exactly
the sign of f(x)f^(m+1)(x). No odd-order sign is omitted.
If F(0)=0 instead, the order of F' forces r=m+1, and (7)
is an identity before any division by F. Both strict one-third
bounds in part4 hold simultaneously on a sufficiently small
closed disk. The triangle inequality gives
|V_epsilon|>|rB(0)|/3 for 0<=epsilon<=1, while
V_epsilon(0)=rB(0)!=0. Hence precisely r-1 orders remain
at the boundary point, with no other local roots. This part
needs no sign assumption on h.

L958 excludes those common orders only from K. The noncommon
allocation reproduces its kappa in every case. Therefore this
audit accepts the conditional local obstruction to obtaining an
independent signed term by terminal splitting. It supplies no
uniform scale, endpoint extension, intermediate-u boundary
exclusion, global index, bound on K or all-degree Xi positivity.
The only direct mathematical inputs remain L018 and L958.

## Mathlib

Full matching Mathlib coverage for this completion-family splitting
and critical-weight comparison has not been checked and is unknown.
Rouche's theorem, analytic Taylor factorization and finite polynomial
root counting are supporting tools; no matching formal theorem for
this entire specialization is identified. No formal verification
is claimed. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
