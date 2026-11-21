# Lemma 688: the inverse-phase Taylor filter can cancel exactly at the fixed angle

## Hypotheses

Use L666's exact family, with integer q>=1,

    n=12q+3, M=4q+1=n/3, x=-d=-5/4, R=11/8, U=121/64,
    alpha=27/10, h=alpha/n, t_j=j/n (0<=j<n),
    Z_e={x} union {x+i*h*(m+1/2+e_m): -2q<=m<2q},
    e_m real, |e_m|<=1/8,
    B_u(a)=product_j R*(a-t_j*u)/(U-t_j*a/u),
    W_a(u)=B_u(x)/B_u(a).

All original residues are one; the full j=0 factor and denominator
angle 1/u are retained. Extend W_(x+v)(-1) by this rational formula
near v=0. Set J=floor(sqrt(n)), and let p_n(v) be the degree-J Taylor
polynomial at zero of 1/W_(x+v)(-1). Write P_n(a)=p_n(a-x) and

    S_n(e)=sum_(a in Z_e) W_a(-1)*P_n(a),
    A=R/(1/32)=44,
    C(P)=sum_(k=0)^deg(P) |P_k|*A^k,  P(a)=sum_k P_k*a^k.

Thus the coefficient norm is centered at a=0, not at the anchor x.
The multiplier P_n depends on n, but not on the displacement vector.

## Conclusion

For every admissible n,

    1 <= C(P_n) <= exp(1)*(J+1)*(362*n)^J,
    log C(P_n)=o(n).                                      (1)

Nevertheless, for every sufficiently large admissible n there is a
positive index m_n^* and a real s_n with 0<s_n<1/32 such that the
admissible vector

    e_(m_n^*)=s_n, e_(-m_n^*-1)=-s_n,
    e_m=0 at every other index

satisfies exactly

    S_n(e)=0.                                             (2)

The two shifted nodes have ordinates of magnitude
n^(-1/4)+O(1/n). In particular the proposed uniform bound
|S_n(e)|>=1/2 fails beyond every onset, despite (1). The complete
undisplaced response is 1+o(1); every remaining node is included in
the construction and in its error estimate.

This is an unaudited, fixed-angle filter obstruction, not an upper
bound on the joint norm V_(1/32), not a full-cube countersequence to
the original-D estimate, and not an RH candidate. The witness has
only two displaced nodes, within the sparse class studied in L686;
there is no conflict with that lemma's joint-norm lower bound. Other
angles, angularly optimized multipliers, L683's transfer audit,
H/support, actual-Xi realization and signs remain separate.
The classification POTENTIALLY_NEW records the prior bounded source
comparison, not certified originality.

## Proof

### 1. Approved scope, comparisons and imported inputs

Reuse the unchanged invocation-start EXPLORE assessment
`drafts/literature/2026-11-03-inner-spatial-rational-response.md`.
This is the proposed inverse-phase filter test inside its exact joint
resolvent target. L687's coefficient-extraction argument makes

    |sum_a W_a(u)*P(a)|/[R*C(P)] <= V_(1/32)               (3)

a valid lower certificate. Its polynomial zero-removal obstruction
does not decide this test, which prescribes no discarded nodes.
L669's audited fixed-angle cancellation has a fixed order K with
K-dependent constants/onsets. It does not by itself control the
present n-dependent polynomial of degree floor(sqrt(n)), whose
coefficients grow faster than every fixed power of n. L686's sparse
joint-response result is a contrast, not a premise of this proof.
The scalar-energy derivative stop supplies no signed lower bound.

We use L664's audited complete-rectangle product bounds and kernel
expansion at offset delta=1/4. Their extension to the holomorphic
multiplier p_n is justified in Section 3, including its full contour
cost. The analytic import is the standard residue theorem in
R. W. Howell and J. H. Mathews, *Complex Analysis*, online edition,
[Section 8.1, Theorems 8.1.5 and 8.1.7](https://complexanalysis.org/web/sec_residue-thm.html),
already read and specialized in L664. It applies to a meromorphic
function with finitely many interior poles and none on the positively
oriented rectangular boundary. We do not reprove that theorem or
claim a new quadrature result. We also use the standard intermediate
value theorem for a real continuous function on a closed interval.
No new source theorem or numerical certificate is a premise.

### 2. Exact coefficients and the centered observation cost

Put

    A_j=1/(d-t_j), b_j=t_j/(U-d*t_j).

All denominators are positive, and 4/5<=A_j<=4, 0<=b_j<2.
Exact division, including j=0, gives

    W_(x+v)(-1)=product_j (1+b_j*v)/(1-A_j*v),
    H_n(w):=1/W_(x-w)(-1)
           =product_j (1+A_j*w)/(1-b_j*w)
           =sum_(k>=0) c_k*w^k,                         (4)
    c_k>=0, c_0=1, p_n(v)=sum_(k=0)^J (-1)^k*c_k*v^k.

The power series converges near zero; each coefficient can also be
read as a finite sum of nonnegative monomials. Namely choose a subset
S of numerator factors and denominator multiplicities l_j>=0 with
|S|+sum_j l_j=k, assigning weight product_(j in S) A_j times
product_j b_j^(l_j). This convention includes b_0=0 and its vanishing
monomials without changing the sum.

For every representation of degree k-1, add one unused numerator
factor. There are n-|S|>=n-k+1 such factors, each at least 4/5.
The total added weight is therefore at least
(4/5)*(n-k+1)*c_(k-1). A resulting degree-k representation is
counted exactly |S| times, at most k. Hence

    k*c_k >= (4/5)*(n-k+1)*c_(k-1).

Since J<=n/2 for n>=4, for 1<=k<=J this proves

    c_(k-1)/c_k <= 5*k/(2*n),
    c_J >= [2*n/(5*J)]^J.                              (5)

In particular all these coefficients are strictly positive.

At w=1/(8n), the bounds log(1+z)<=z for z>=0 and
-log(1-z)<=2z for 0<=z<=1/2 give

    log H_n(w) <= sum_j(A_j*w+2*b_j*w) <=8*n*w=1.

Nonnegative coefficients then yield c_k<=exp(1)*(8n)^k.
For a polynomial in a, the coefficient norm of (a-x)^k is
exactly (A+d)^k. The triangle inequality and A+d=181/4 give

    C(P_n) <= sum_(k=0)^J c_k*(A+d)^k
            <= exp(1)*(J+1)*(362*n)^J.                 (6)

Also |x|<A and P_n(x)=1 imply 1<=C(P_n). Taking logarithms
in (6), with J<=sqrt(n), proves (1). Translation from v to a
has been charged; using only coefficients about v=0 would not
justify (3).

For later use, on |v|<=1 put

    Q_n=exp(1)*(J+1)*(8*n)^J,
    |p_n(v)|<=Q_n,       log Q_n=o(n).                 (7)

### 3. The complete undisplaced response, including all outer nodes

Let e=0. Use L664's rectangle with spacing h'=2h,

    Y_n=q*h', b=1/50, c=1/200,
    Gamma_n=boundary([-Y_n,Y_n]+i[-b,c]),
    omega=2*pi/h',
    K(y)=i*omega/[exp(i*omega*y-pi*i/2)-1]
                   +i*omega/[exp(i*omega*y+pi*i/2)-1].

The contour is positively oriented. Its kernel poles are exactly
the 4q undisplaced nonanchor ordinates h*(m+1/2), with residue one;
there is no pole on the boundary or at zero. These are L664's
delta=1/4 census and moving endpoints, not an infinite lattice.
On a neighborhood of its closed interior, W_(x+i*y)(-1) is
holomorphic: its variable denominator zeros x+i*y=-t_j are outside
the rectangle, as verified in L664 Section 2. The polynomial p_n(i*y)
introduces no poles. The residue theorem gives the exact raw sum

    S_n(0)=1+(1/(2*pi*i))*integral_(Gamma_n)
                           W_(x+i*y)(-1)*K(y)*p_n(i*y) dy. (8)

Here the leading 1 is W_x(-1)*p_n(0), and every other original
unit-residue term is in the integral. Throughout the rectangle,
|y|^2< (9/20)^2+(1/50)^2<1, so (7) bounds the multiplier.

For n>=183, reuse L664 Sections 3--4, equations (9)--(15).
Their upper-edge and complete-side estimate uses only the multiplier
bound 33; replacing it by Q_n gives the upper bound
(72/5)*n*Q_n*exp(-n/3000). This remains valid for the raw sum (8),
since 1/(2*pi)<1 just as the earlier 1/(2*pi*R)<1; neither
normalization was used for a sharper constant. On the complete
lower edge the kernel expansion is uniformly absolutely convergent:

    K(y)=2*i*omega*sum_(l>=1) cos(pi*l/2)*exp(-i*l*omega*y).

The l=1 term is exactly zero. L664's bound on the entire tail l>=2,
with 33 replaced by Q_n, is (24/5)*n*Q_n*exp(-n/3000).
The cited bounds cover the whole moving sides and all lower-edge
frequencies; there is no truncation depending on J. Therefore

    |S_n(0)-1| <= (96/5)*n*Q_n*exp(-n/3000)=o(1).       (9)

The last limit follows from log Q_n=o(n). Conjugation symmetry
and the real coefficients in (4) make S_n(0) real. In particular
S_n(0)>1/2 for all sufficiently large admissible n. No estimate of
the sum of individual outer-node moduli has replaced (8).

### 4. A large, slowly varying amplitude outside the Taylor core

For real y define

    T_n(y)=W_(x+i*y)(-1)*p_n(i*y).

This notation denotes a single weighted term, not the full response.
For y>0 and k<=J, (5) gives

    c_(J-l)*y^(J-l)/(c_J*y^J)
                          <=[5*J/(2*n*y)]^l,  1<=l<=J.

Consequently, whenever epsilon=5J/(2ny)<1,

    p_n(i*y)=c_J*(-i*y)^J*(1+rho_n(y)),
    |rho_n(y)|<=epsilon/(1-epsilon).                  (10)

Uniformly for (1/2)n^(-1/4)<=y<=2n^(-1/4), this error is O(n^(-1/4)).
Also, directly from (4),

    |W_(x+i*y)(-1)|
       =product_j sqrt[(1+b_j^2*y^2)/(1+A_j^2*y^2)]
       >=exp(-8*n*y^2),                               (11)

using log(1+A_j^2*y^2)<=16*y^2 and the nonnegative numerator
logarithms. For all large n, (5), (10), (11) hence give uniformly
on that interval

    log|T_n(y)|
       >= J*((log n)/4-log 5)-32*sqrt(n)-log 2
       >= (1/8)*sqrt(n)*log n.                        (12)

The second inequality holds beyond an absolute existential onset,
since J/sqrt(n)->1. In particular these terms diverge in modulus.
They lie outside the scale J/n of direct central Taylor approximation;
their individual amplification must not be ignored.

We next control their phase change over a bounded number of lattice
steps, retaining the exact finite products. Put

    g_n=(1/n)*sum_j(A_j+b_j),
    g=integral_0^1 [1/(d-t)+t/(U-d*t)]dt,
    kappa=alpha*g.

Riemann sums of this continuous function give g_n->g. L664's
audited bounds g(R)>9/5 and g(123/100)<11/5, and its monotonicity
in the real-part parameter, apply at d and give

    9/5<g<11/5,       243/50<kappa<297/50.             (13)

Along the real y-axis all factors of W are nonzero and

    d_y log W_(x+i*y)(-1)
       =i*sum_j [b_j/(1+i*b_j*y)+A_j/(1-i*A_j*y)].

This means W'/W; no global logarithm is assumed. Its difference
from i*n*g_n has modulus at most 20*n*|y|, because the real-axis
denominators have modulus at least one. Integrating over a segment
of length h*s, for bounded real s and y=n^(-1/4)+O(1/n), gives

    W_(x+i*(y+h*s))(-1)/W_(x+i*y)(-1)
                             =exp(i*kappa*s)+o(1).     (14)

The integral error is at most
20*n*h*|s|*max(|y|,|y+h*s|)=O(n^(-1/4)); the Riemann-sum
error also tends to zero. All errors are uniform for, say, |s|<=129
and the fixed windows used below.

Equation (10), applied at both y and y+h*s, gives

    p_n(i*(y+h*s))/p_n(i*y)=1+o(1),

since its leading-power ratio is (1+h*s/y)^J and
J*h*|s|/y=O(n^(-1/4)). The denominators here are nonzero by
(10) for large n. Combining this with (14),

    T_n(y+h*s)/T_n(y)=exp(i*kappa*s)+o(1)              (15)

uniformly in the same ranges. This is a local ratio of exact terms;
it is not an approximation of the whole signed response.

### 5. Select a controllable phase among a fixed number of nodes

Let

    m_n=floor(n^(3/4)/alpha-1/2),
    y_(n,k)=h*(m_n+k+1/2),       0<=k<=128.

Then y_(n,k)=n^(-1/4)+O(1/n) uniformly in this fixed window.
For all sufficiently large n these are positive allowed nodes:
m_n>=0 and m_n+128<2q, since m_n=O(n^(3/4)) and 2q=(n-3)/6.
Their conjugates are allowed distinct nodes too.

Write delta=2*pi-kappa. From (13) and 3<pi<22/7,

    3/50<delta<499/350<3/2,
    127*delta>2*pi.                                   (16)

For any real phase phi, the real interval

    [phi-128*delta+delta/2, phi-delta/2]

has length 127*delta>2*pi, so contains some pi/2+2*pi*l.
The closest point among phi-k*delta, 0<=k<=128, is within
delta/2<499/700 of that target. By (15), the actual phase of
T_n(y_(n,k)) differs modulo 2*pi from
arg T_n(y_(n,0))+k*kappa by o(1), uniformly over these finitely
many k. The positive margin 3/4-499/700 lets us choose, for every
large n, an index k_n with a representative phase phi_n satisfying

    |phi_n-pi/2|<3/4,
    T_n(y_(n,k_n))=|T_n(y_(n,k_n))|*exp(i*phi_n).        (17)

No irrational rotation, equidistribution or n-dependent sampling
count is assumed in this finite selection.

### 6. The symmetric pair gives an exact zero of the full response

Set m_n^*=m_n+k_n, y_n=y_(n,k_n), and s_0=1/32. Vary only
e_(m_n^*)=s and e_(-m_n^*-1)=-s, with -s_0<=s<=s_0.
This remains inside L666's cube, and the two changed ordinates are
exactly y_n+h*s and its negative. Real coefficients give
T_n(-y)=conjugate(T_n(y)). Consequently the full response along
this path, including every unchanged term, is the real continuous
function

    S_n(s)=S_n(0)+2*Re[T_n(y_n+h*s)-T_n(y_n)].          (18)

Continuity follows directly from nonzero real-axis denominators.
Put theta=kappa/32, so

    243/1600<theta<297/1600.

By (15), normalized by |T_n(y_n)|, the two real changes in (18)
at s=+s_0 and s=-s_0 respectively are

    cos(phi_n+theta)-cos(phi_n)+o(1),
    cos(phi_n-theta)-cos(phi_n)+o(1).                  (19)

In (17), |phi_n-pi/2|+theta/2<1. Thus
sin(phi_n+theta/2)>1/2 and sin(phi_n-theta/2)>1/2,
by cos t>=1-t^2/2. Also sin(theta/2)>=theta/4. The cosine
difference identities bound the first main expression in (19)
above by -theta/4 and the second below by theta/4. Since
theta/4>243/6400>1/40, the uniform o(1) errors imply eventually

    Re[T_n(y_n+h*s_0)-T_n(y_n)] <=-|T_n(y_n)|/40,
    Re[T_n(y_n-h*s_0)-T_n(y_n)] >= |T_n(y_n)|/40.       (20)

Equation (12) makes these magnitudes tend to infinity. Equations
(9), (18), (20) therefore give S_n(0)>1/2, S_n(s_0)<0 and
S_n(-s_0)>0 for all sufficiently large admissible n. The intermediate
value theorem on [0,s_0] gives s_n in (0,s_0) with S_n(s_n)=0.
This proves (2), with exactly two nonzero allowed displacements.

The onset is the maximum of finitely many absolute existential
onsets in the proof, independent of any subsequently selected node
or shift. No effective numerical value is asserted. The zero is
proved by continuity and strict analytic signs, not by floating
point evidence. It annihilates the particular lower certificate (3)
at u=-1 and does not bound the maximum over u and the spatial circle.

## Mathlib

Full matching coverage of this n-dependent inverse-Taylor filter
and exact two-node cancellation has not been checked. Supporting
mathematics is finite product algebra, nonnegative power-series
coefficients, Riemann sums of a continuous function, the residue
theorem, and the real intermediate value theorem. L664 retains its
audited contour estimates and source qualifications; L687 retains
its separate audit status. No named matching Lean theorem or formal
verification is claimed. Unknown coverage is not evidence of absence.
