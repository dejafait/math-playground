# Corollary 32b: an enclosure-only cluster polynomial detector

## Hypotheses

Let (beta_j) be a finite or countable multiset of nonzero complex numbers,
invariant under conjugation including multiplicity. Supply finite real
parameters A, B, r_0, r_1 and a complex number w such that

    sum_j |beta_j| <= A,       0 < r_0 < B,       r_1 > 0,
    y = Im(w) > r_1.

Write D(c,r) for the closed disk with center c and radius r. Define

    E_0 = D(0,r_0) union [-B,B],
    E_+ = D(w,r_1),            E_- = D(conjugate(w),r_1),
    K = E_0 union E_+ union E_-.

Assume these three compact sets are pairwise disjoint and contained in
D(0,B). Every node belongs to K, and at least one node belongs to E_+.
The hypotheses include boundary nodes and all multiplicities. Neither
individual node locations nor separation within either cluster is given.
In particular A>0. Define the algebraic-square form, in L895's generic
summable-node convention extending L030, by

    Q(q) = sum_j beta_j^2 q(beta_j)^2.

## Conclusion

There is an explicit real polynomial q, depending only on the supplied
parameters, for which

    Q(q) <= -3/2 < -1,      deg(q) <= M,
    ||q||_{coeff,1} <= C = W T_J.                            (1)

The norm is the sum of the absolute values of the monomial coefficients.
Here are finite formulas and recurrences for the bounds; all logarithms
with subscript 2 have base two:

    d = min{r_1, y-r_1, |w|-r_0-r_1}/8,
    rho = r_1+d,             m = |w|-rho,        H = 4(B+1),
    epsilon = min{1/(8A), 1/(2 sqrt(A B))},
    L = rho^2/(m^2 d) + rho/(m d) + rho^2/(m d^2),
    n = max{1, ceil(4 pi L/epsilon)},           W = 2 rho/m,
    J = ceil(4(2 pi rho+H+B)/d)+3,
    F = max{1,2/d},          G = max{1,d/2}.

Start K_0=1, T_0=1. For s=0,...,J-1 set

    N_s = max{0, ceil(log_2(4 W J T_s F^(K_s)/epsilon))},
    K_{s+1} = K_s+N_s,
    T_{s+1} = T_s 2^(K_s) (N_s+1) G^(N_s).

Finally set

    M = max{0, ceil(log_2(4 W T_J/epsilon))}.

The polynomial is specified by the finite quadrature, chain subdivision,
binomial truncations and real symmetrization in the proof. These formulas
are mathematical expressions in the supplied real and complex parameters;
a numerical implementation would additionally require certified input
representations and rounding. The bounds are deliberately coarse and
make no efficiency claim.

Construction dated 17 November2026, step1257; independent conceptual
audit passed in step1259, with the checks recorded below. The hypotheses,
construction and constants were retained without repair. This is a
quantitative specialization of known Runge tools, not a claimed original
approximation theorem. It supplies no
actual-Xi nonreal node, full-support enclosure, all-degree sign, finite
unconditional RH cutoff or RH conclusion. L032's qualitative detection
and L895's exact-node bounds are comparisons; here no inverse internal
node separation appears.

## Proof

### Source and reason for the specialization

Use the standard finite Cauchy-sum and pole-moving construction in
H. P. Boas, [Class Notes, Math618: Complex Variables II](https://haroldpboas.gitlab.io/courses/618-2016a/notes2016.pdf),
29 April2016, Section4, named Runge theorem p26, Section4.1 pp27-28;
and J. G. Burkill, [Lectures on Approximation by Polynomials](https://mathweb.tifr.res.in/Documents/Publications/Lectures/tifr16.pdf),
TIFR1959, concluding Runge section, TheoremA pp60-62 and the pole-moving
lemma p61. The latter moves the entire finite Laurent polynomial,
including every higher pole order, along an arc disjoint from the compact
set, and then expands at a pole beyond a containing disk.

Those sources do not state degree, coefficient or complete Q-error
bounds for these enclosures. We calculate those constants, using two
explicit Cauchy circles and explicit paths, rather than reprove general
Runge density or import unchecked finite constants from another source.
The Cauchy integral formula and the integer negative-binomial identity
(1-t)^(-k)=sum_{l>=0} binom(k+l-1,l)t^l for |t|<1 are the standard
analytic and algebraic inputs. Every use below is on a uniformly
separated contour or with ratio at most 1/4. No assumption about a
connected analytic neighborhood across the three components is made.

### Positive constants, circles and target values

Disjointness of the two closed disks D(0,r_0) and D(w,r_1) gives
|w|-r_0-r_1>0. Thus d>0, and each of r_1, y-r_1 and
|w|-r_0-r_1 is at least 8d. In particular

    m = |w|-rho >= r_0+7d > 0.

Containment E_+ in D(0,B) gives |w|+r_1<=B and hence d<=B/8.
All constants and the finite recurrence above are therefore well-defined.

Define f on K by f=0 on E_0, f(z)=i/z on E_+, and f(z)=-i/z
on E_-. These definitions extend holomorphically to the disjoint open
d-neighborhoods of the respective components: their original distances
are at least 8d, and zero lies outside the two
enlarged cluster disks of radius rho. Also
f(conjugate(z))=conjugate(f(z)).

For sigma in {+1,-1}, put c_sigma=Re(w)+sigma i y and

    a_sigma(t) = c_sigma+rho exp(i t),       0<=t<=2 pi.

Each circle has distance d from its own cluster disk. The upper circle
has distance at least |w|-rho-r_0>=7d from D(0,r_0), at least
y-rho>=7d from the real interval, and at least
2y-rho-r_1=2(y-r_1)-d>=15d from the lower disk. Reflection proves the
same bounds for the lower circle. Thus the distance of either circle
from all of K is at least d. The other components lie outside the
circle's closed interior, not merely off its circumference, by the
same inequalities. Every point on either circle has modulus at least m.

The complement of K has no bounded component. To check this directly,
take z outside K in the upper half-plane. Its upward vertical ray
avoids D(0,r_0), since the modulus increases along that ray, and also
avoids the real interval and E_-. Choose 0<eta<min{d,dist(z,E_+)}.
If the ray meets D(w,r_1+eta), replace its passage through that disk
by an arc on the disk's boundary from entry to exit. This enlarged
disk is disjoint from E_0 and E_- and stays strictly above the real
axis, so the detour avoids K. The resulting path reaches arbitrarily
large height. Reflection covers the lower half-plane. Real points
outside K have modulus greater than B. Since the exterior of D(0,B)
is path connected, these paths show that the whole complement of K
is path connected. The bounded contour-pole paths used below give
the quantitative information that this qualitative check alone lacks.

Write f_sigma(z)=sigma i/z. Cauchy's formula, with both circles
positively oriented, gives for every z in K

    f(z) = sum_sigma (1/(2 pi)) integral_0^(2 pi)
             f_sigma(a_sigma(t)) rho exp(i t)/(a_sigma(t)-z) dt.  (2)

For z in that circle's cluster the integral is f_sigma(z); for z on
the other components it is zero, since both zero and z are outside
the integration disk. This verifies all cases of (2), including
cluster boundary nodes since their distance from the circle is d.

### Finite Cauchy sum with a uniform error

For a fixed z in K, the derivative in t of the integrand in (2) has
absolute value at most

    rho^2/(m^2 d) + rho/(m d) + rho^2/(m d^2) = L.

Indeed |f_sigma(a)|<=1/m, |f_sigma'(a)|<=1/m^2,
|a'|=rho, and |a-z|>=d; differentiating its three factors gives
the three displayed terms. On each interval of length 2 pi/n the
left-endpoint quadrature error for the unnormalized integral is at
most L(2 pi/n)^2/2. Division by 2 pi and summation over n intervals
gives pi L/n per circle, uniformly for all z in K.

Let t_l=2 pi l/n for 0<=l<n, a_{sigma,l}=a_sigma(t_l), and define

    lambda_{sigma,l}
        = -rho exp(i t_l) f_sigma(a_{sigma,l})/n,
    R(z) = sum_{sigma,l} lambda_{sigma,l}/(z-a_{sigma,l}).

The minus sign converts (a-z)^(-1) in (2) to (z-a)^(-1). Then

    ||R-f||_K <= 2 pi L/n <= epsilon/2,
    sum_{sigma,l} |lambda_{sigma,l}| <= 2 rho/m = W.            (3)

Only the supplied circles are sampled; no node of the unknown multiset
is located or sampled.

### Explicit chains with uniform clearance and a bounded number of moves

An upper pole a_{+,l} first follows its circle counterclockwise to
w+i rho, through an angular increment in [0,2 pi). It then travels
vertically, at real part x=Re(w), to x+iH, and horizontally to iH.
For a lower pole use the reflection of this rule applied to its
conjugate, ending at -iH. This specifies a path for each pole.

The circular part has clearance at least d by the preceding estimates.
On the vertical part a=x+it with t>=y+rho. Its distance from E_+
is t-y-r_1>=d, from E_- is t+y-r_1>d, from the real interval is
at least t>d, and from D(0,r_0) is at least |w|-r_0>d since
|x+it|>=|x+iy|. The vertical segment goes upward: y+rho<=B+d<H.
On the horizontal part |Im(a)|=H, every z in K has |Im(z)|<=B,
so its clearance is at least H-B>d. Reflection covers the lower path.

The lengths of the three parts have sum at most 2 pi rho+H+B.
Divide each nonzero part into ceil(4 length/d) equal arclength pieces;
omit zero-length parts. The sum of the three resulting integers is at
most J. Consecutive endpoints have Euclidean distance at most d/4,
and every endpoint has distance at least d from K. Append stationary
moves at the final endpoint if necessary to obtain exactly J moves.
This gives endpoints a_0,...,a_J for every initial pole, with

    a_0=a_{sigma,l},       a_J=sigma iH,
    dist(a_s,K)>=d,        |a_{s+1}-a_s|<=d/4.                 (4)

No topological assumption about an unconstructed complementary path
or an unspecified positive separation is used. Explicit paths (4)
provide the pole-moving hypothesis needed from the standard method.

### Every higher pole order and its truncation error

For each chain approximate its unweighted kernel (z-a_0)^(-1).
Start with R_0(z)=(z-a_0)^(-1). At stage s write

    R_s(z) = sum_{k=1}^{K_s} u_{s,k} (z-a_s)^(-k),
    sum_k |u_{s,k}| <= T_s.

Zero coefficients are permitted. Set a=a_s, b=a_{s+1}. Replace every
inverse power in R_s by

    (z-a)^(-k)  ->  sum_{l=0}^{N_s}
        binom(k+l-1,l) (a-b)^l (z-b)^(-(k+l)).                (5)

Formula (5) is the negative-binomial expansion because
z-a=(z-b)(1-(a-b)/(z-b)). It converges uniformly on K since
|a-b|/|z-b|<=1/4. Its new largest inverse power is at most K_s+N_s.

For k>=1 and l>=0, binom(k+l-1,l)<=2^(k+l). If N>=0 and h=|a-b|,
the discarded tail for a single power, uniformly on K, is bounded by

    d^(-k) sum_{l>N} 2^(k+l) (h/d)^l
       <= (2/d)^k sum_{l>N} 2^(-l)
        = (2/d)^k 2^(-N).

After summing all current coefficients this gives

    ||R_{s+1}-R_s||_K <= T_s F^(K_s) 2^(-N_s)
                      <= epsilon/(4 W J).                  (6)

The last inequality follows from the definition of N_s, including
the case its logarithm is nonpositive, when N_s=0 suffices.
Coefficient collisions in the new Laurent polynomial can only reduce
the following absolute bound:

    sum_k |u_{s+1,k}|
      <= T_s 2^(K_s) sum_{l=0}^{N_s} (2h)^l
      <= T_s 2^(K_s) (N_s+1) max{1,d/2}^(N_s) = T_{s+1}.     (7)

Thus the same recurrences apply to every chain, without dependence on
any individual pole order after cancellation. Stationary padded moves
also satisfy (5)-(7). Summing (6) gives a kernel approximation at the
final pole b=sigma iH with error at most epsilon/(4W).

### Polynomial completion, coefficient bound and real symmetry

For each final power use its Taylor polynomial in z through degree M:

    (z-b)^(-k)  ->  (-b)^(-k) sum_{l=0}^{M}
                              binom(k+l-1,l) (z/b)^l.       (8)

For |z|<=B, |z/b|<=B/H<1/4. The same binomial estimate gives tail
at most (2/H)^k 2^(-M)<=2^(-M), since H>4. With all Laurent
coefficients included, the error in (8) is at most

    T_J 2^(-M) <= epsilon/(4W).                             (9)

The coefficient norm of each polynomial in (8) is at most

    H^(-k) sum_{l=0}^{M} binom(k+l-1,l) H^(-l)
       <= H^(-k)(1-1/H)^(-k) = (H-1)^(-k) <= 1.             (10)

Consequently the polynomial P_{sigma,l} approximating the unweighted
initial kernel has degree at most M, coefficient norm at most T_J,
and total uniform error at most epsilon/(2W) on K. Define

    p(z) = sum_{sigma,l} lambda_{sigma,l} P_{sigma,l}(z),
    q(z) = (p(z)+conjugate(p(conjugate(z))))/2.

By (3), (6), (9) and (10), deg(p)<=M, ||p||_{coeff,1}<=WT_J,
and ||p-f||_K<=epsilon. The conjugated expression in q is the
polynomial with conjugate coefficients. Thus q has real coefficients
and its coefficient norm cannot increase. As K and f are invariant
under conjugation in the stated sense, its uniform error also cannot
increase. We have proved

    deg(q)<=M,       ||q||_{coeff,1}<=WT_J,
    |q(z)-f(z)|<=epsilon for every z in K.                  (11)

### The complete summable-node algebraic-square form

The generic absolute-convergence and reality argument in L895 applies:
|beta_j|<=B, sum_j |beta_j|^2<=BA, and a fixed polynomial is bounded
on D(0,B). Conjugation including multiplicity and real coefficients
make Q(q) real. We do not replace the algebraic square by a modulus
square; absolute values below bound only its error.

Every cluster node has modulus at least s_0=|w|-r_1>0, so the total
number N_c of node copies in E_+ union E_- is finite and at most A/s_0.
Nonemptiness of E_+ and conjugation invariance give N_c>=2. At each
such node beta, beta^2 f(beta)^2=-1; on E_0 it is zero. Hence

    sum_j beta_j^2 f(beta_j)^2 = -N_c <= -2.

Put e(z)=q(z)-f(z). For every node, the exact error is
beta^2(2 f(beta)e(beta)+e(beta)^2). Since f vanishes on E_0 and
|f(beta)|=1/|beta| on the two clusters, (11) implies

    sum_j |beta_j^2(q(beta_j)^2-f(beta_j)^2)|
       <= 2 epsilon sum_{cluster copies} |beta_j|
                         + epsilon^2 sum_j |beta_j|^2
       <= 2 A epsilon+BA epsilon^2 <= 1/4+1/4 = 1/2.        (12)

This bounds the full infinite sum, not a selected finite head or an
uncontrolled residual. All boundary nodes and repeated copies occur
in (12). The ideal sum and Q(q) are real, so (12) gives
Q(q)<=-N_c+1/2<=-3/2. Together with (11), this proves (1).

The constructed polynomial and its bounds use only A,B,r_0,r_1,w.
Collisions within either cluster change neither the construction nor
its estimates. They strengthen the number of negative summands but
do not establish additional linearly independent negative directions.
Actual-Xi use would still require independent support and mass data
and the interpretation supplied by L024/L025; no such use is made here.

### Independent conceptual audit, 17 November2026, step1259

The audit replays the full construction under exactly the stated support
and mass hypotheses. It imports no exact node location, internal separation,
cluster count, actual-Xi assumption or additional approximation theorem.
The Boas/Burkill source scope had separate approval before this audit;
their qualitative results are not taken as verification of the constants.

**Geometry and Cauchy cases.** The lower bounds defining d give
dist(E_+,E_0)>=8d and dist(E_+,E_-)>=16d. Enlarging a cluster by d
therefore leaves clearance at least 7d from E_0 and 15d from the other
cluster, while its own contour clearance is d. The origin is outside
both integration disks because m>=r_0+7d>0. Thus f_sigma is analytic
through each closed integration disk. For a point in its own cluster,
Cauchy's integral is f_sigma(z); for each other component both poles
0 and z are outside that disk, so the integral is zero. This verifies
the identity also on the boundaries of K. In the no-hole argument the
choice eta<dist(z,E_+) puts the starting point outside the enlarged
detour disk; the detour is disjoint from the other components. Hence
that topological assertion requires no additional geometric premise.

The path rises from y+rho<=B+d<H. Its vertical segment moves away
from the origin and both cluster centers, and its horizontal segment
has clearance H-B>d. Reflection gives the lower path. If there are
j<=3 nonzero segments of lengths l_i, their subdivision count is
sum_i ceil(4 l_i/d)<=ceil(4 sum_i l_i/d)+j-1<=J. On a circle, chord
length is at most arc length. Every endpoint therefore has clearance
d and every move has length at most d/4, as required in the actual
expansion about the *new* pole. Padding changes none of these facts.

**All orders, signs and rounding cases.** Direct factorization gives
z-a=(z-b)(1-(a-b)/(z-b)), verifying the sign of (5). For every k>=1,
the tail beyond N is bounded by (2/d)^k sum_{l>N}2^(-l)
=(2/d)^k 2^(-N). This includes N=0; it is not a simple-pole-only
estimate. Since F>=1 and F>=2/d, summing coefficients through K_s
gives the uniform bound T_s F^(K_s) 2^(-N_s). For any X>0,
N=max(0,ceil(log_2 X)) implies X 2^(-N)<=1, including X<=1.
Apply this with X=4WJT_sF^(K_s)/epsilon to obtain (6).
The retained coefficient bound uses 2|a-b|<=d/2 and the finite sum
of N_s+1 nonnegative terms, each at most G^(N_s); this proves (7)
even when d/2<1. Colliding powers are combined using the triangle
inequality. When a=b, the l=0 term is unchanged and all l>=1 terms
vanish, so stationary padding causes no error. All K_s>=1 and T_s>0
are finite by induction for the finite integer J. No stability bound
on earlier errors is missing: R_J-R_0 is the telescoping sum of the
successive differences bounded in (6).

**Final completion and symmetrization.** At b=+/-iH, expansion (8)
has ratio |z/b|<=B/H<1/4. Its tail is at most (2/H)^k2^(-M),
and H>4 makes this at most 2^(-M) for every generated k. The same
rounding implication with X=4WT_J/epsilon proves (9), even if M=0.
The full coefficient-series sum is (H-1)^(-k)<=1, proving the
monomial coefficient bound independently of the degree or k. The
quadrature derivative estimate gives 2pi L/n<=epsilon/2; its kernel
sign is correct because (a-z)^(-1)=-(z-a)^(-1). Weighting the two
kernel errors by total coefficient mass at most W gives the complete
uniform budget epsilon/2+epsilon/4+epsilon/4=epsilon. Finally,
(q-f)(z)=((p-f)(z)+conjugate((p-f)(conjugate(z))))/2.
Conjugation invariance of K and f proves (11) without
requiring the separately constructed pole chains to be conjugate.

**Complete sum and threshold.** For a fixed q, its supremum on D(0,B)
is finite and sum_j |beta_j|^2<=BA, so Q(q) is absolutely convergent.
Conjugation with multiplicity makes it real. The cluster-copy count
is finite because every such node has modulus at least s_0>0; the
nonempty upper cluster has an equally populated, disjoint conjugate
cluster, so N_c>=2. The ideal sum is exactly -N_c. Equation (12)
bounds every copy in the full multiset, using f=0 on E_0 and
|f(beta)|=1/|beta| only on the clusters. The chosen epsilon separately
ensures 2A epsilon<=1/4 and BA epsilon^2<=1/4. Therefore the audited
actual bound is Q(q)<=-3/2, stronger than the required Q(q)<=-1.
Absolute values occur only in error estimates, not in the defining
algebraic square. No limit interchange or omitted tail remains here.

The audit verifies this conditional input and its explicit bounds. It
does not certify a numerical implementation, usable complexity, errors
in computed polynomial coefficients, actual-Xi support or positivity.
No repair, new theorem or progress beyond the cited approximation method
is claimed by the audit. L895 is the only direct local mathematical
input, through its generic convergence convention; L030 fixes the
normalization and L032 remains a comparison. The existing DAG row is
unchanged. Full Mathlib coverage remains unchecked as specified below.

## Mathlib

Coverage of this full quantitative enclosure theorem has not been
checked; availability is unknown, not asserted absent. No Mathlib
theorem is imported. General Cauchy, binomial-series or polynomial
support would not by itself verify the path, truncation and complete
Q-error constants here.
