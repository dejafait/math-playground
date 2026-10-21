# L131 — The complete exterior-circulation scalar is strictly positive

## Hypotheses

Import L128(6)--(7), its centered symbols, complete two-orientation
contraction, integrated phase qualification, and absolute convergence.
Retain its scope: SU(2), both actual L010 probes i=3,6, straight
lower-rooted direction-1 forest, all-face relative fixed-link box
D=(-4,4)^4, admitted even N, lattice spacing 8/N, flow time 1/16,
and the bare small-coupling coefficient at fixed mesh before refinement.
The actual physical fields, lower prefix including the constant axial
mode, and complete exterior heat sum are unchanged. No new mesh limit
is taken. Use normalized torus measure.

Import L129(9)--(10)'s elementary inverse moments at a strictly positive
parameter, and L127 proof section 5's integer interval operations,
Machin pi enclosure and cosine Taylor remainder. Its different midpoint
quadrature bound is not used here.

## Conclusion

L128's complete scalar xi obeys

    2/125 < xi < 7/400.                                  (1)

More precisely, with Y=2-2cos(theta_3), Z=2-2cos(theta_4), k=Y+Z,

    xi=(1/pi^2) integral_[0,pi]^2
            Y Z (Z-Y)^2/[16 k^(3/2) sqrt(k+4)]
                                      dtheta_3 dtheta_4, (2)

where the integrand is defined to be zero at k=0. It is continuous
there and nonnegative everywhere; its integral is strictly positive.
Neither mixed orientation of K_(i,f) has been deleted.

This completes the scalar inputs of L128's retained transverse-H
functional, together with L130's H enclosures and L127's tau enclosure.
It does not determine the sign of the actual heat-weighted K_(i,f)
or transverse-H functional for either probe. The five other L124
coefficients E,ax,-Q,G,R and the complete compensation comparison remain
unevaluated. No finer-scale/logarithmic estimate, interacting reflected
error <=c_box/2, continuum axioms, reflection positivity, infrared
control or finite positive mass follows.

## Proof

### 1. Contract the complete matrices before frequency integration

Write x=d_2,y=d_3,z=d_4, A=eta_2,B=eta_3,C=eta_4,
X=x^2,Y=y^2,Z=z^2, a=A^2,b=B^2,c=C^2 and L=X+Y+Z.
Here a is a squared filter, not the lattice spacing. Thus
a=1-X/4,b=1-Y/4,c=1-Z/4. At L>0 let d=(x,y,z)^T,
P=d d^T/L and Q=I-P. With the test h=h^23,v=e_3,u=e_2
specified in L128(7), its matrices are

    Zmat=[-y  x  0; -z  0  x; 0  -z  y],
    R=[-2B  0  0; 0  0  0; 0  0  2B],
    C0=2AB[e_2 e_3^T-e_3 e_2^T],
    U=A[b e_3 epsilon_(23)^T+c e_4 epsilon_(24)^T],
    G=U Zmat=A[0  0  0; -b y  b x  0; -c z  0  c x].

All three plaquette planes and both ordered displacement-2 generator
outputs are retained. Define the edge columns

    r=2B(xy,-(X+Z),zy)^T,
    s=2AB(-y,x,0)^T.

Direct multiplication gives d^T R Zmat=r^T and d^T C0=s^T.
Both r and s are orthogonal to d. Therefore L128's full projected
factors are exactly

    A(v)=P R Zmat Q=d r^T/L,
    beta0(h)=P C0 Q=d s^T/L.

In particular beta0^T A-A^T beta0=(s r^T-r s^T)/L.
Since Qs=s and Qr=r, the complete scalar integrand in L128(6) is

    -[r^T Gs-s^T Gr]/L^2.                              (3)

This retains the two terms in that equation, with their minus sign
and no additional half or outside factor. The imported phase argument
removes the imaginary C1 part only after integration; the present
calculation concerns the complete remaining real integral.

Put t=X+Z. Explicitly,

    Gs=(0,2a B^3(X+Y),2a Bc zy)^T,
    Gr=(0,-2A B^3 xL,0)^T,
    r^T Gs=-4ab^2 t(X+Y)+4abc YZ,
    s^T Gr=-4ab^2 XL.

Using XL-t(X+Y)=-YZ, equation (3) becomes

    g=a b YZ(Z-Y)/L^2.                                  (4)

No projection has crossed a component filter. These algebraic
identities hold for every L>0, including cases with some zero
components; the single L=0 point is immaterial to the integral.

### 2. Symmetrize a frequency pair and perform one complete integral

The function (4) is absolutely integrable: 0<=a,b<=1,
YZ/L^2<=1/4 and |Z-Y|<=4 imply |g|<=1. Exchange the two
dummy frequency variables theta_3 and theta_4 in its full torus
integral. This preserves L and a and changes b to c. Averaging
the original and exchanged expressions, using b-c=(Z-Y)/4, gives

    xi=integral a YZ(Z-Y)^2/(8L^2).                      (5)

The half here comes from a justified averaging of two equal full
integrals, not from deleting a mixed K_f orientation. It does not
assert an orientation-by-orientation positivity identity.

For fixed k=Y+Z>0, L129(9)--(10), with the integrated coordinate
relabeled as theta_2, gives

    <a/(X+k)^2>=((k+4)j1-j0)/4
      =1/[2 k^(3/2) sqrt(k+4)],
    j0=1/sqrt(k(k+4)), j1=(k+2)/[k(k+4)]^(3/2).          (6)

The filter a=1-X/4 is exactly the numerator of that imported
moment. Its positive-parameter hypothesis holds off the measure-zero
set Y=Z=0. Absolute integrability already permits this integration
by Fubini; equivalently the symmetrized integrand is nonnegative
and bounded by 1/2. Combining (5)--(6) gives (2), with the
normalized full-circle integrals reduced to [0,pi]^2 by evenness.

Let F denote its integrand. For k>0, YZ<=k^2/4,
(Z-Y)^2<=k^2 and sqrt(k+4)>=2 show

    0<=F<=k^(5/2)/128.                                  (7)

Thus F extends continuously with value zero at the corner. This
bound controls that entire region without omitting any frequencies
or assuming bounded derivatives. On an open rectangle where Y,Z>0
and Y!=Z, F>0, proving strict positivity independently of arithmetic.

### 3. Complete cell enclosure and exact recorded evidence

Divide each true angle interval [0,pi] into n=256 equal cells;
n is an integration subdivision count, not the lattice mesh N.
Each angle rectangle has exact normalized weight 1/n^2. Enclose
all n+1 endpoints theta_j=j pi/n and their values 2-2cos(theta_j)
using the integer operations imported from L127. Monotonicity on
[0,pi] then encloses Y on cell j by the lower bound at j and
the upper bound at j+1, and likewise for Z. Intersect with [0,4]
and assign the exact endpoint values 0 and 4.

Only the first rectangle contains k=0. On it use [0,K^(5/2)/128]
from (7), where K is its outward upper bound for k. On every
other rectangle the verified k lower endpoint is positive. Enclose
F by evaluating

    Y Z (Z-Y)^2/[16 k sqrt(k(k+4))]

with outward integer intervals. Squaring an interval [l,h] uses
minimum zero if it contains zero, otherwise min(l^2,h^2), and
maximum max(l^2,h^2), rounded outward. Thus squaring the difference
does not introduce a false negative lower bound. Every divisor
has positive lower endpoint. Sum all cell intervals and divide by
n^2. These sums bound the entire integral by monotonicity, without
midpoint approximation or a missing quadrature remainder.

Reproduction commands from the active notebook:

    python3 scripts/combined-ward-response/enclose_xi_scalar.py
    python3 scripts/combined-ward-response/enclose_xi_scalar.py --audit

The scale is 10^30, with arbitrary-precision integer arithmetic.
L127's interval primitive proof supplies outward addition, products,
positive-denominator division and integer square roots. Pi is
enclosed using 60 and 20 alternating-series terms in Machin's
formula; all endpoint angles are less than 4. The cosine Taylor
polynomial through degree 94 has absolute remainder at most
4^96/96!, as in L127. The endpoint uncertainty does not change the
exact normalized cell area 1/n^2.

The full certificate
scripts/combined-ward-response/xi-scalar-enclosure-certificate.json
stores all 257 endpoint records, 65,536 cell records, integer totals,
216 complete exact rational matrix checks of (3)--(5), final rational
bounds and failures. Its full bounds are

    526849221969035314666393315689087
      /32768000000000000000000000000000000 <= xi,
    xi <= 22816193872227409605708820505443
      /1310720000000000000000000000000000.               (8)

Exact rational comparison gives (1). The initial containing thresholds
were 1/100 and 1/10; the achieved interval has width less than
0.001330. The finite matrix checks have zero residuals for both the
original contraction and its symmetrized expression. They support
the analytic proof, rather than proving the general matrix identity.

The complete audit replays every endpoint, cell, matrix check and
aggregate and reports no failures in
scripts/combined-ward-response/xi-scalar-enclosure-audit.json.
The complete /bounds and /failures values were inspected and the
weakened endpoints in (1) checked by exact rational comparison.
This is a saved-record audit using the same implementation, not
independent processor or independently implemented verification.
Printed floating approximations do not enter the enclosure.

This is RESEARCH / REPRODUCTION under the unchanged ready assessment
drafts/literature/2026-10-10-other-other-cubic-leading-scale.md.
The existing scalar and inverse-moment formulas are imported with
their applicability justified above. Finite algebra, frequency
symmetrization and cell inclusion are supplied because the imported
results do not evaluate xi. This is local progress by standard methods,
with no originality claim beyond the checked sources.

## Mathlib

Full matching exterior-circulation scalar formula and enclosure:
**not checked**. Supporting finite matrix/trace identities, Fubini,
elementary inverse moments and integer interval inclusion:
**not checked**. Unknown coverage is not evidence of absence.
