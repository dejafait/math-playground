# L129 — Exact two-angle formulas for the three physical H constants

## Hypotheses

Import L128(2)--(4)'s physical tensor definitions, centered-phase
qualification and absolute convergence. Keep its scope: SU(2), both
actual L010 probes i=3,6, straight lower-rooted direction-1 forest,
all-face relative fixed-link box D=(-4,4)^4, admitted even N, a=8/N,
flow time 1/16, and the bare small-coupling coefficient at fixed mesh
before refinement. This calculation evaluates one frequency integral
in the universal tensor, without a new mesh limit or alteration of the
physical exterior fields, prefix, heat sum or ordered generators.

Use normalized torus measure and transverse indices 2,3,4. Set
x=d_2, y=d_3, z=d_4, A=eta_2, B=eta_3, C=eta_4, where
d_mu=2 sin(theta_mu/2), eta_mu=cos(theta_mu/2). Write
X=x^2, Y=y^2, Z=z^2, a=A^2=1-X/4, b=B^2=1-Y/4,
c=C^2=1-Z/4, k=X+Z and L=k+Y. The letter a in this local
algebra is A^2, not the lattice spacing. Frequency derivatives in the
proof are distinguished from the physical derivatives in L128(1).

## Conclusion

For k>0 put

    j0=1/sqrt(k(k+4)),
    j1=(k+2)/[k(k+4)]^(3/2),
    u0=((k+4)j0-1)/4,
    u1=((k+4)j1-j0)/4,
    v0=((k+4)^2 j0-k-6)/16,
    v1=((k+4)^2 j1-2(k+4)j0+1)/16,
    w=u0-k u1.                                           (1)

Then the three L128 constants are exactly

    h_D=(1/pi^2) integral_[0,pi]^2 F_D dtheta_2 dtheta_4,
    h_X=(1/pi^2) integral_[0,pi]^2 F_X dtheta_2 dtheta_4,
    h_A=(1/pi^2) integral_[0,pi]^2 F_A dtheta_2 dtheta_4,  (2)

where

    F_D=X(4+Z)v0/2-2aZ[k v1+c w],
    F_X=aZ[k v1+c k u1+2c w],
    F_A=a-2a k u0-X(4+Z)v0/2.                           (3)

These extend continuously to k=0 by F_D=F_X=0, F_A=1.
In particular no corner or frequency region is omitted. More explicitly,

    |F_D|<=4 sqrt(k),  0<=F_X<=2 sqrt(k),
    |F_A-1|<=k/4+3 sqrt(k)                              (4)

for 0<k<=8. The crossed constant is strictly positive: h_X>0.
No numerical value or enclosure for h_D,h_X,h_A is claimed.

The three-dimensional integrands before angle integration are

    g_D=X(4+Z)b^2/(2L)-2abZ[bk+cY]/L^2,
    g_X=abZ[(b+c)k+2cY]/L^2,
    g_0=2a[bY+cZ]/L,                                    (5)

with h_A equal to the integral of g_0-g_D-2g_X. This supplies a
nonnegative full integrand for h_X, not a sign of its contraction with
the actual fields. All other scalar and physical contractions in L128,
the five other L124 coefficients, and K_(i,oo)+4 gamma D_i remain
unevaluated. No compensation, finer-scale/logarithmic estimate,
interacting error <=c_box/2, continuum axioms, reflection positivity,
infrared control or finite positive mass follows.

## Proof

### 1. Contract both ordered generators before integrating

In plaquette order (23),(24),(34), put

    v=(y,z,0)^T, wv=(-x,0,z)^T, t=(0,x,y)^T,
    n=(z,-y,x)^T, S=I-n n^T/L.

The notation wv distinguishes this vector from the scalar w in (1).
L128's exterior columns are f_2=2A v, f_3=2B wv,
f_4=-2C t. Their inner products with n vanish; hence S f_q=f_q.
The two complete ordered displacement-2 factors in L128's J are

    a_3=-B wv, c_3=AB, pi_3=(23),
    a_4=C t,   c_4=AC, pi_4=(24),
    W_nu=c_nu epsilon_(pi_nu)^T S.

Here a_nu is L128's vector A_nu, and c_nu is its signed clover
factor at rho=2. Both ordered signs are positive. All three output
rows and every exterior plane remain. For a prime in direction m,

    J_(2,m) f_q=sum_(nu=3,4) {
      a_nu[c'_nu (f_q)_(pi_nu)
                    +c_nu (S' f_q)_(pi_nu)]
      -a'_nu c_nu (f_q)_(pi_nu) }.                       (6)

Differentiate S f_q=f_q to get S' f_q=(I-S)f'_q.
This keeps the projection derivative; it is not set to zero by the
undifferentiated identity. We use (6) only at L>0.

For m=2, x'=A, A'=-x/4; all y,z,B,C are constant. Thus

    S'f_2=0, S'f_3=-2AB z n/L,
    a'_3=AB e_(23), a'_4=AC e_(24),
    c'_3=-xB/4, c'_4=-xC/4.

Substitution into (6) gives, with plaquette unit vectors,

    J_(2,2)f_2=A x B^2 y wv/2-2A^3 B^2 y e_(23)
                       -A x C^2 z t/2-2A^3 C^2 z e_(24),
    J_(2,2)f_3=-B^3[X/2-2aZ/L] wv
                       +2a B^3 x e_(23)+2a B C^2 yz t/L.

Using v dot wv=-xy, v dot t=xz, wv dot t=yz,
|wv|^2=X+Z and X+4a=4, these give

    f_2^T J_(2,2)f_2=-4a(bY+cZ),
    f_3^T J_(2,2)f_3=-b^2 X(4+Z)
                                  +4abZ[bk+cY]/L.       (7)

For m=3, y'=B, B'=-y/4, with the other variables constant.
Now S'f_2=2AB z n/L, S'f_3=0. The nonzero derivative factors
are a'_3=y wv/4, c'_3=-Ay/4 and a'_4=BC e_(34).
In (6) the two terms proportional to y^2 wv cancel for f_2,
and the two terms proportional to xy wv cancel for f_3. Explicitly,

    J_(2,3)f_2=-2a B^3 Z wv/L
                         -2a B C^2 yz t/L-2a B C^2 z e_(34),
    J_(2,3)f_3=0,
    f_3^T J_(2,3)f_2=-4abZ[bk/L+cY/L+c].                (8)

Equations (7)--(8), in L128's symmetrized definition
H_(rho,m;qr)=-(f_r^T J f_q+f_q^T J f_r)/(4L), give
exactly (5). The diagonal has the factor 2 from symmetrization;
the crossed entry retains both orientations although one is zero here.
L128's integrated centered-phase justification is imported. No frequency
integration by parts, path-phase deletion before integration or scalar
replacement of an unequal filter occurs.

### 2. Integrate theta_3 at fixed positive k

Let brackets denote the normalized theta_3 integral. The elementary
inverse moments are exactly L127(9), with the same k and Y:

    <1/(k+Y)>=j0, <1/(k+Y)^2>=j1, <Y>=2, <b>=1/2.       (9)

For completeness of the specialization, t=tan(theta_3/2) changes the
first integral to (1/pi) integral_R dt/[k+(k+4)t^2]. Rescaling t
and integrating 1/(1+t^2) gives j0. At fixed k>0, differentiation
under the integral is justified by the lower bound k and gives
j1=-j0'. This is the existing elementary input, not a new theorem
about the Yang--Mills coefficient or a reproof of its mesh limit.

Since b=(k+4-L)/4 and <L>=k+2, polynomial division gives

    <b/L>=u0, <b/L^2>=u1,
    <b^2/L>=v0, <b^2/L^2>=v1,
    <bY/L^2>=u0-k u1=w,
    <bY/L>=1/2-k u0.                                   (10)

All these are ordinary integrals with denominator at least k.
Applying (10) to (5) gives F_D,F_X in (3), and
F_0=a+2a(cZ-k)u0. A useful exact cancellation is

    F_D+2F_X=X(4+Z)v0/2+2acZ u0,

which proves the displayed F_A=F_0-F_D-2F_X. No positivity
of a signed difference is inferred from this cancellation.

The original integrands are absolutely integrable. In fact (5) and
0<=a,b,c<=1 show |g_D|<=6, 0<=g_X<=2 and 0<=g_0<=2:
use X/L,Z/L<=1, bk+cY<=L and (b+c)k+2cY<=2L.
These estimates permit Fubini. They also show that at X=Z=0,
the theta_3 integrands for Y>0 are g_D=g_X=0 and g_0=2b,
whose averages agree with the stated corner values. The single
point L=0 has measure zero. Evenness in theta_2,theta_4 changes
the two full-circle integrals to the normalized [0,pi]^2 integrals
in (2); no multiplicative factor is lost.

### 3. Control the corner and the crossed sign

Formula (10) directly proves u0,u1,v0,v1,w are nonnegative.
Moreover, since b<=1 and Y<=L,

    u0,v0,w<=j0, u1,v1<=j1,
    j0<=1/(2 sqrt(k)), j1<=j0/k<=1/(2 k^(3/2)).

The first F_D term is at most 4k j0<=2 sqrt(k).
The absolute value of its second term is at most
2k[k j1+j0]<=2 sqrt(k). For F_X its three nonnegative
terms total at most k[2k j1+2j0]<=2 sqrt(k).
Finally X<=k, 4+Z<=8 and |a-1|=X/4 imply

    |F_A-1|<=k/4+2k j0+4k j0<=k/4+3 sqrt(k).

This proves (4) and the continuous extension. Away from k=0 the
formulas are smooth functions of X,Z on their compact square. Therefore
all reduced integrands are continuous on the closed angle square;
the proof omits no singular region and needs no unproved interchange
of a k limit with a diverging separate inverse moment.

In (5), g_X is nonnegative everywhere except the harmless undefined
zero point. At theta_2=theta_3=theta_4=pi/2, a=b=c=1/2,
X=Y=Z=2 and g_X>0. It remains positive on an open neighborhood,
so its normalized integral h_X is strictly positive. This is a universal
tensor scalar sign, not an actual heat-weighted response sign or a
comparison with -4 gamma D_i.

### 4. Verification and remaining scope

The supporting script
`python3 scripts/combined-ward-response/check_h_angle_reduction.py`
checks the full matrix construction of J, both ordered generators and
all three target entries at 216 exact rational signed points. It also
checks the F_A cancellation at 16 formal rational moment tuples.
The full records are saved in
`scripts/combined-ward-response/h-angle-reduction-certificate.json`:
648 matrix residuals and 16 moment residuals are exactly zero, against
the requirement of zero failed residuals. These checks support the
algebra, not its general validity; (6)--(10) are the analytic proof.
No quadrature preview, floating-point coefficient or uninspected large
certificate is used as proof. The script needs only Python's standard
library and does not modify the earlier certificates.

The unchanged EXPLORE assessment
`drafts/literature/2026-10-10-other-other-cubic-leading-scale.md`
covers this coefficient evaluation within the complete other/other
comparison. This is RESEARCH / REPRODUCTION: L128's tensor and
L127's inverse moments are imported, and the finite contraction and
polynomial division are supplied because neither input gives (2)--(5).
It is local progress using standard algebra, with no novelty claim.
No new source theorem or source search is needed. In particular no
already-stopped universal deletion mechanism is reopened.

Actual numerical enclosure needs a separate rigorous two-dimensional
integration error bound; continuity and the supporting checks do not
provide one. The other constants and physical bilinear integrals,
the other five canonical coefficients, other response jets and all
construction gaps in the conclusion remain open.

## Mathlib

Full matching physical H one-angle reduction: **not checked**.
Supporting rational matrix algebra, elementary trigonometric inverse
integrals, dominated differentiation, Fubini, and continuous extension:
**not checked**. Unknown coverage is not evidence of absence.
