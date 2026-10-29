# Lemma 474: a cubic small-displacement pair-mass bound

## Hypotheses

Use the actual entire Xi function and zero symmetries of L018, and
the definitions A, P_T, d_j, gamma_j, m_j, F_j and J_j(T) in L471.
In particular F_j removes exactly one conjugate pair, not all of its
m_j copies. Put L=log T and, for T>=2 and 0<epsilon<=1, define

    B_epsilon(T)=sum_(j in P_T, d_j L<=epsilon) m_j d_j^3
       integral_(J_j(T)) (1-v^2)
          |F_j(gamma_j+d_j v)/A(gamma_j+d_j v)|^2 dv.

Each distinct conjugate nonreal pair is counted once with its full
multiplicity m_j. Retain the actual clipped windows J_j(T).
No RH, simplicity, separation, lower displacement bound, zero-count
bound or external fixed-half-plane premise is assumed.

## Conclusion

There exist absolute constants C and T_0 such that

    B_epsilon(T)<=C epsilon^3 T(log T)^3                      (1)

for every real T>=T_0 and every 0<epsilon<=1, with the same constants.
Thus the approved target holds with alpha=3. The proof below is a
local application of classical finite Blaschke factorization and a
known shifted second moment; no originality of those tools is claimed.
The separate critical application audit in Section 6 found no correction
necessary. The arithmetic moment theorem remains an imported result.

This controls only the indicated small-displacement sector. It does
not prove the full B(T)=o(T(log T)^3) required in L471, a saving on
the complementary sector, individual-height signs or RH. Taking
epsilon small bounds only that restricted sector, not all pairs.

## Proof

### 1. Imported tools and normalization on microscopic rectangles

Import the finite bounded-holomorphic-function statement in Kevin
Broughan, *Equivalents of the Riemann Hypothesis*, Volume Two:
*Analytic Equivalents*, Cambridge (2017), Theorem 3.3, proof (1),(4),
printed pp. 26--27 ([primary preview, pp. 47--48](https://api.pageplace.de/preview/DT0400.9781108195430_A31720577/preview-9781108195430_A31720577.pdf#page=48)).
Dividing by any finite list of Blaschke factors at zeros, repeated
according to their multiplicity, preserves the disk supremum bound.
Only this finite statement is used. Our functions extend across the
closed disks, so the maximum modulus argument in that proof applies
directly. There is no infinite Blaschke product or rearrangement.

The arithmetic input is Sandro Bettin, *The second moment of the
Riemann zeta function with unbounded shifts*, Int. J. Number Theory
6 (2010), 1933--1944, [arXiv:1111.0925v1, Theorem 1, p. 2,
small-shift proof completion pp. 9--10](https://arxiv.org/pdf/1111.0925v1#page=2).
Use its uniform shifts Re a,Re b=O(1/log U) and error
O((sqrt(U)+sqrt(|Im a|)+sqrt(|Im b|))log^2 U), at endpoints U
comparable to T. Its two main terms are always combined at their
coincident pole. This imports the theorem, without independently
auditing its arithmetic proof. The approved assessment already covers
this small-shift scope. The following arguments supply the necessary
uniform specialization, rather than assume zero-dependent sampling.

Write g(s)=log(pi^(-s/2) Gamma(s/2)) on the high upper/lower disks
with the conjugate branches used in L465 Sections 1--2. Its sector
digamma estimate is

    g'(s)=(1/2)Log(s/(2pi))-1/(2s)+O(T^(-2)).                 (2)

All points below have |Im s| comparable to T and Re s in a fixed
compact interval. L018 gives, with s=1/2+iz,

    Xi(z)=P(z) zeta(1/2+iz),
    P(z)=[s(s-1)/2] pi^(-s/2) Gamma(s/2).

For large T these factors are holomorphic and nonzero whenever
T/2<=Re z<=3T and |Im z|<=9/L. At real x, |P(x)|=A(x).
The logarithmic derivative of P with respect to z has modulus O(L)
by (2); the polynomial terms contribute O(1/T). Integrating along
the vertical segment from x to x+iy therefore gives, uniformly,

    |Xi(x+iy)|/A(x) <= C |zeta(1/2-y+ix)|,
           T/2<=x<=3T, |y|<=9/L.                            (3)

This uses only a holomorphic logarithm of P on the segment's disk,
never a holomorphic extension of the modulus A. On the real axis,
(2) also gives (log A)'=-pi/4+O(1/T). Hence for real c,x in this
range with |x-c|<=9/L,

    C^(-1)<=A(x)/A(c)<=C.                                   (4)

The constants in (2)--(4) are absolute once T exceeds one fixed
onset; they do not depend on epsilon or the selected zeros.

### 2. Continuous second moment, with the pole cancellation uniform

For every real |y|<=9/L, the imported theorem implies

    integral_(T/2)^(3T) |zeta(1/2-y+ix)|^2 dx <= C T L.       (5)

Here are the details needed for uniformity down to y=0. Set a=-y,
b=y and apply the theorem at U=3T and U=T/2, keeping these same
shifts in both applications. They are real and O(1/log U), and
conjugation makes the product on the left an absolute square.
The combined integrand on the right over [T/2,3T] is

    zeta(1-2y)+zeta(1+2y) E(y,x),
    E(y,x)=|chi(1/2-y+ix)|^2.                               (6)

The functional-equation convention is
chi(s)=exp(g(1-s)-g(s)). At y=0, E(0,x)=1 exactly. Taking the
real derivative of its logarithm and using (2) gives

    partial_y log E(y,x)=2 log(x/(2pi))+O(1/x).

Indeed the derivative is twice the real part of
g'(1/2+y-ix)+g'(1/2-y+ix). Integrating from zero proves

    log E(y,x)=2y log(x/(2pi))+O(|y|/x),
    |E(y,x)|<=C,  |E(y,x)-1|<=C |y| L.                     (7)

The error has the factor |y|: an unanchored O(1/x) error followed
by division by y would not suffice. For y!=0 the Laurent expansions
at the zeta pole combine (6) as

    (E(y,x)-1)/(2y) + gamma_E(1+E(y,x)) + O(|y|)(1+E(y,x)),

where gamma_E is Euler's constant. This is O(L) uniformly by (7).
At y=0 its continuous limit is also O(L), as required by Bettin's
pointwise limiting prescription. Integrating the combined expression
costs O(TL). The two endpoint errors are O(sqrt(T)L^2), absorbed
by O(TL) at one absolute onset. This proves (5) with no constants
depending on y or epsilon. No derivative of a moment error is used.

### 3. One cell: keep all selected zeros before removing one pair

Partition the real axis into half-open cells

    C_k=[k/L,(k+1)/L),  c_k=(k+1/2)/L,  k integer.

Assign each selected pair in B_epsilon to its unique center cell.
There are finitely many such pairs by L471. Write S_k for the
assigned pair indices and M_k=sum_(j in S_k) m_j. Ignore empty
cells. Since each selected window meets [T,2T] and d_j<=1/L,
their centers lie in [T-1/L,2T+1/L]. Thus every nonempty cell
center lies in [T-3/(2L),2T+3/(2L)].

Fix such a cell, abbreviate c=c_k, M=M_k and set R=8/L. Define

    f(w)=Xi(c+Rw)/A(c),
    S=sup_(|w|<=1) |f(w)|.

For every assigned pair its two roots in disk coordinates are
a_(j,+)=(gamma_j+id_j-c)/R and a_(j,-)=conj(a_(j,+)). They obey

    |a_(j,+)|,|a_(j,-)| <= sqrt(5)/16 <3/16.

For every t=gamma_j+d_j v, |v|<=1, its coordinate w=(t-c)/R
satisfies |w|<=3/16. Define b_a(w)=(w-a)/(1-conj(a)w).
For all the roots above and all these evaluation points,

    |b_a(w)| <= (3/16+3/16)/(1-9/256)
              =96/247 <1/2,
    |1-conj(a)w| >=247/256.                                (8)

Form the finite product of the 2M factors b_a from all assigned
zeros, repeated m_j times for each member of pair j. The imported
finite factorization gives f=G product b_a, with G holomorphic
and |G(w)|<=S on the unit disk. Extra zeros of Xi, including any
real zero at the cell center, need not be divided out; they cause
no difficulty in this finite statement.

For a fixed j remove just one factor at each of a_(j,+),a_(j,-).
Since q_j(c+Rw)=R^2(w-a_(j,+))(w-a_(j,-)), the exact identity is

    F_j(c+Rw)/A(c)
      = R^(-2) G(w) [product of the other 2M-2 factors]
         /[(1-conj(a_(j,+))w)(1-conj(a_(j,-))w)].             (9)

In particular the other copies of this same pair remain when m_j>1.
Equations (4), (8) and (9) imply, at every t in its full real window,

    |F_j(t)/A(t)|^2 <= C L^4 S^2 2^(-4M+4).                (10)

Here |t-c|<=3/(2L), so (4) applies. Integrating only over J_j(T)
can decrease the bound: integral_(-1)^1 (1-v^2) dv=4/3.
Using d_j<=epsilon/L, the entire cell's contribution is at most

    C epsilon^3 L S^2 M 16^(-(M-1)) <= C epsilon^3 L S^2.    (11)

For integers M>=1, M 16^(-(M-1))<=1: its value at 1 is 1,
and the successive ratio is (M+1)/(16M)<=1/8. This is the
cluster compensation. No bound on microscopic occupancy or
multiplicity has been assumed, and arbitrarily close distinct
centers cause no denominator involving their distance.

### 4. Sum disk suprema using a continuous area norm

Restore the index k and write

    S_k^*=sup_(|z-c_k|<=8/L) |Xi(z)|/A(c_k),
    D_k={z: |z-c_k|<9/L}.

This S_k^* is the S of the preceding calculation, not the pair
index set S_k. By the submean value property of the subharmonic
function |Xi(z)/A(c_k)|^2, the radius-1/L disk about any point in
the closed radius-8/L disk yields

    (S_k^*)^2 <= (L^2/pi) integral_(D_k) |Xi(z)/A(c_k)|^2 dArea(z).

All these disks are contained in
[T/2,3T]+i[-9/L,9/L] at one fixed large onset. Equations (3)--(4)
turn the last integrand into at most C|zeta(1/2-y+ix)|^2.
The centers are spaced by 1/L, so a point belongs to at most 19
of the radius-9/L disks: membership requires |x-c_k|<9/L.
Summing the nonnegative area integrals and then using (5) gives

    sum_k (S_k^*)^2
      <= C L^2 integral_(-9/L)^(9/L)
                    integral_(T/2)^(3T) |zeta(1/2-y+ix)|^2 dx dy
      <= C T L^2.                                         (12)

Only finitely many disks are summed; the area integrands are continuous
and nonnegative on the compact rectangle. There is no zero-sampled
moment import or infinite interchange. Summing (11) and applying
(12) gives C epsilon^3 L * T L^2, exactly (1).

All constants depend only on the fixed disk radii and the uniform
bounded-shift theorem. A common absolute T_0 makes every displayed
domain and absorbed error valid. The argument works for all epsilon
simultaneously, including windows reduced to endpoints (whose
integrals vanish), repeated zeros, and an empty selected pair set.

### 5. Scope of the improvement

The cubic weight survives because the other zero factors are kept
until after division by the chosen pair. Replacing F_j by -AZ/q_j
and applying an unconditioned real fourth moment would instead lose
displacement as recorded in L471. Here finite factorization offsets
occupancy before a continuous second moment is used. Divided-difference
interpolation from the assessment is unnecessary for this successful
version; no reproof of that classical formula is made.

For every fixed epsilon, (1) is still a full-scale O(TL^3) bound.
Uniformity implies only that the normalized small sector is O(epsilon^3).
There is no estimate here for d_j L>epsilon. No limit exchanging that
uncontrolled complement with epsilon tending to zero is licensed.

### 6. Separate critical application audit, 28 October 2026

The audit replays the specialization, not Bettin's arithmetic proof or
Broughan's infinite factorization. The conclusion (1), its quantifiers
and its hypotheses survive unchanged. The precise source passages in
Section 1 and [DLMF 5.11.2/5.11(ii)](https://dlmf.nist.gov/5.11)
were checked against the following application steps.

**Common domains and gamma normalization.** Increase a fixed T_0 so
L>=36. Then |y|<=9/L implies 1/4<=Re(1/2+iz)<=3/4 on the
rectangle in (3); L018's completion formula applies directly there.
Both upper and lower gamma arguments lie in a fixed closed sector
strictly inside the cut plane, with modulus comparable to T. The
nonzero polynomial and gamma factors admit the logarithms used in
Section 1. More explicitly,

    d/dz log P(z)=i[1/s+1/(s-1)+g'(s)], s=1/2+iz.

Equation (2) bounds this by C L, so its integral over a vertical
segment of length at most 9/L is bounded by 9C. This proves (3)
with a constant independent of epsilon, without extending A
holomorphically. On real x its real part is -pi/4+O(1/x),
which gives (4). All divisions by A are at positive real heights.

**Moment convention and the coincident poles.** Bettin's left side
uses zeta(1/2+a+ix)zeta(1/2-b-ix), so a=-y,b=y indeed gives
the absolute square in (5). His c=a-b is -2y, and his chi convention
is the one in (6). At both U=T/2 and U=3T the same shifts satisfy
|a|log U,|b|log U<=18 after increasing T_0; thus one fixed
bounded-shift constant covers all applications. Subtract the two
endpoint formulas before estimating; their common lower integration
range cancels and the sum of their absolute error bounds is
O(sqrt(T)L^2). No shift is selected as a function of a zero.

Put s_-=1/2-y+ix and s_+=1/2+y-ix. Conjugation gives
E(0,x)=1, and differentiating its real logarithm gives exactly
2 Re(g'(s_+)+g'(s_-)). Equation (2) makes this
2 log(x/(2pi))+O(1/x), uniformly on the whole y interval.
Integrating from zero establishes the O(|y|/x) remainder in (7).
In particular (E-1)/(2y) is uniformly O(L) and has limit
log(x/(2pi))+O(1/x) at zero. The other combined Laurent terms
are bounded. This verifies the limit prescription, including negative
y and arbitrarily small nonzero y, without dividing an unanchored
error by y. Since L/sqrt(T) tends to zero, the two moment errors
are absorbed at one T_0 independent of y and epsilon.

**Finite factors, repeated roots and clustering.** In one occupied
cell, |gamma_j-c|<=1/(2L) and d_j<=1/L imply
|a_(j,+/-)|<=sqrt(5)/16; the whole real pair window has
|w|<=3/16. The bounds (8) therefore hold for every selected
root at every such evaluation point. The finite quotient G is
holomorphic across the closed unit disk, and the product has modulus
one on its boundary. This verifies the hypotheses of the imported
finite bound even if f has other zeros. With the explicitly chosen
b_a convention, q_j=R^2(w-a_(j,+))(w-a_(j,-)) gives exactly
the two denominator factors of (9); no phase or modulus-square
replacement enters that identity.

For a pair of multiplicity m_j, exactly one copy of each of its
two roots is removed. There remain 2M-2 factors in total, including
2m_j-2 from this pair. Squaring their modulus bounds gives
2^(-4M+4)=16^(-(M-1)); it does not give an inverse multiplicity
factor. The scalar sum of m_j is M, and
M*16^(-(M-1))<=1 for every integer M>=1 as checked in (11).
This handles a single pair, arbitrary repeated roots and arbitrarily
close distinct pairs. An unremoved real zero, including at c or at
an evaluation point, stays in G and can only make that value zero.
No root-distance denominator or zero-count bound is used.

**Area cost, endpoints and simultaneous epsilon.** Occupied centers
lie within [T-3/(2L),2T+3/(2L)]. Hence their radius-9/L disks
lie horizontally within [T-21/(2L),2T+21/(2L)], contained in
[T/2,3T] once T L>=21. At a point attaining S_k^*, the open
radius-1/L disk is contained in D_k, including when the maximizing
point lies on the radius-8/L circle. Submean thus has exactly the
factor L^2/pi in (12). Within D_k, |x-c_k|<9/L permits (4),
and (3) supplies the zeta integrand. The spacing 1/L bounds overlap
by 19, independent of the number and multiplicity of selected pairs.
The logarithmic cost is explicitly

    L^2 * (18/L) * O(TL) = O(TL^2).

Multiplication by the cell factor epsilon^3 L in (11) is exactly
O(epsilon^3 T L^3), with no extra logarithm. All sums are finite;
the area functions are continuous on the enclosing compact rectangle.
Selecting fewer cells as epsilon decreases requires no new constant
or limit interchange. The full v-window bounds dominate every clipped
J_j(T); a singleton at either dyadic endpoint has zero integral.
Empty sectors have zero sum. Taking the maximum of the fixed onsets
above and the imported uniform-moment onset proves the asserted common
T_0, with no dependence on epsilon, occupancy or root separation.

This is verification of the existing application, not a new bound or
an informative obstruction. The complementary sector d_j L>epsilon,
the full L471 little-o criterion and individual signs remain unresolved.

## Mathlib

Full matching coverage was not checked; availability is unknown, not
established absence. The classical supporting tools are finite Blaschke
division/maximum modulus, the submean value property for the squared
modulus of a holomorphic function, sector digamma asymptotics and the
cited shifted zeta second moment. No supporting formal theorem names
were verified in this step. [Mathlib documentation](https://leanprover-community.github.io/mathlib4_docs/).
