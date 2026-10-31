# L492 — Explicit local circle count at positive-time phase centers

## Hypotheses

Use exactly H_t and M_t of D. H. J. Polymath, *Effective approximation
of heat flow evolution of the Riemann xi function, and a new upper
bound for the de Bruijn–Newman constant*, Research in the Mathematical
Sciences **6** (2019), article 31,
[arXiv:1904.12438v2, 4 August 2019](https://arxiv.org/html/1904.12438v2),
equations (4),(6)–(11). In particular, H_t is entire and
H_t(conj(z))=conj(H_t(z)) for real t, as stated after (4).

For clarity the normalization is M_t(s)=exp(ell_t(s)), where, on
Omega=C minus (-infinity,1], the fixed holomorphic logarithm is

    ell_0(s)=Log(s)+Log(s-1)-(s/2)*log(pi)+log(sqrt(2*pi)/16)
             +(s/2-1/2)*Log(s/2)-s/2,
    alpha(s)=1/(2s)+1/(s-1)+(1/2)*Log(s/(2*pi)),
    ell_t(s)=ell_0(s)+(t/4)*alpha(s)^2.

Here Log is the principal logarithm off its cut. This is the specified
logarithm from L491, not a principal logarithm of the value M_t(s).
Assume t and X are real and

    1/25<=t<=11/50,       X>=4*pi*exp(10000)+2,
    L=log(X/(4*pi)),
    g(X,t)=(X/(4*pi))*L-X/(4*pi)+11/8+(t/16)*L is an integer.

Use the audited quantitative statements of L490 and L491. L490
retains its imports of source Theorem 1.3 and Proposition 6.6(ii);
their saddle proofs have not been independently audited locally.
No RH, zero-reality or simplicity hypothesis is assumed.

## Conclusion

The open disk |z-X|<1/L contains exactly one zero of H_t counted
with multiplicity. That zero is real and simple, and there is no zero
on the boundary. All assertions hold uniformly on the closed time
band and the unbounded X range in the hypotheses.

This is an explicit quantitative specialization of the known local
counting method in source Theorem 1.5(ii), Section 9, pp.59–60,
equations (102)–(104). It does not assert exhaustion of high zeros,
a real/simple tail for all zeros, spatial edge transfer, finite
collision exclusion, or a conclusion as t decreases to zero. The
proof below passed its first separate critical application audit on
2026-10-30, recorded below; its imported saddle estimates remain unaudited.

## Proof

### One nonvanishing holomorphic normalization

Put r=1/L and z=X+w. We have L>10000, so r<1. On |w|<=1,
x=Re(z)>=X-1>4*pi*exp(10000)>0. The two affine arguments

    (1+iz)/2=(1-Im(z))/2+i*x/2,
    (1-iz)/2=(1+Im(z))/2-i*x/2

avoid Omega's cut, also on a neighborhood of this closed unit disk.
Therefore the functions

    A(z)=M_t((1+iz)/2),       B(z)=M_t((1-iz)/2),
    G(z)=ell_t((1+iz)/2)-ell_t((1-iz)/2)

are holomorphic there; A and B never vanish and A/B=exp(G) exactly.
For Im(z)>=0, B is precisely the source B_t and A/B is its gamma
in (16). In L490 the name s_+ refers to B's argument; in L491 it
refers to A's argument. The explicit formulas here settle that
notational difference without reversing the ratio.

The fixed logarithms commute with conjugation on Omega, and t is
real. Thus M_t(conj(s))=conj(M_t(s)), and

    conj(A(conj(z)))=B(z),       conj(B(conj(z)))=A(z).

Set R(z)=H_t(z)-A(z)-B(z). The displayed identities and H_t's
conjugation symmetry imply conj(R(conj(z)))=R(z).

### Reflection with the same denominator

Let d=153/10^6. For |w|<=r and Im(z)>=0, we have
0<=Im(z)<=r<1 and Re(z)>=X-r>4*pi*exp(10000).
Every hypothesis of L490 holds, including both t endpoints, so

    |R(z)/B(z)|<d.                                      (1)

For |w|<=r and Im(z)<0, apply (1) at conj(z), which lies in the
same disk and the upper half-plane. Conjugating gives

    |R(z)/A(z)|<d,
    |R(z)/B(z)|<d*|A(z)/B(z)|=d*|exp(G(z))|.             (2)

Thus the reflected estimate is not assumed to retain the upper-half
constant in the B normalization. Both halves below use the one
holomorphic quotient H_t/B.

### Total error against the explicit holomorphic model

Write n=g(X,t) in Z, v=i*L*w/2, and eta=5010/10^12. L491, applied
on its closed unit disk, gives the exact representation

    G(X+w)=i*(2*pi*n-pi)+v+epsilon(w),
    |epsilon(w)|<eta.                                  (3)

On |w|<=r, |v|<=1/2. Since the first term of (3) is purely imaginary
and eta<1/100, we have Re(G)<=1/2+|epsilon|<2/3. For real
0<=q<1 the exponential series gives exp(q)<=1/(1-q).
Consequently

    |exp(G)|<=exp(|v|+|epsilon|)<3.                     (4)

Equations (1)–(2) and (4) bound |R/B| by 3d everywhere on this
closed disk. Define the entire model

    F_0(w)=1-exp(i*L*w/2)=1-exp(v).

Because exp(i*(2*pi*n-pi))=-1, equation (3) gives

    (1+A/B)-F_0(w)=exp(v)*(1-exp(epsilon(w))).

The same series majorant yields exp(1/2)<=2 and, since eta<1/2,
exp(eta)-1<=eta/(1-eta)<2*eta. Using
|exp(u)-1|<=exp(|u|)-1 for complex u, we obtain

    |(1+A/B)-F_0(w)|<4*eta,
    |H_t(X+w)/B(X+w)-F_0(w)|<3*d+4*eta
       =459020040/10^12 <1/1000.                       (5)

The last rational comparison is 459020040<1000000000.
This bound includes the full reflected residual and the gamma-model
error in the same normalization. It is uniform in every allowed
t and X, without evaluating exp(10000) numerically. The comparison
uses no floor-dependent finite sum as a holomorphic function.

### Strict boundary bound and count with multiplicity

On |w|=r we have |v|=1/2. The exponential series and the reverse
triangle inequality imply

    |F_0(w)|>=|v|-sum_(k>=2) |v|^k/k!
       >1/2-(1/2)*sum_(k>=2) (1/2)^k=1/4.             (6)

The strict inequality holds because 1/k!<=1/2 for every k>=2
and is strictly smaller for k=3, with a positive corresponding
term. The geometric series on the right sums to 1/2.
Combining (5)–(6), the total error is strictly less than |F_0|
at every boundary point.

Both F_0 and H_t(X+w)/B(X+w) are holomorphic on a neighborhood of
the closed disk. The zeros of F_0 occur exactly at w=4*pi*k/L,
k in Z, since exp(u)=1 exactly when u is in 2*pi*i*Z. Only k=0
lies in |w|<r, because 4*pi>1; its derivative is -i*L/2, nonzero.
Rouché's theorem therefore gives exactly one zero with multiplicity
for H_t/B in the disk. The strict boundary inequality also excludes
boundary zeros. Nonvanishing of B preserves all zero multiplicities,
so the same conclusions hold for H_t.

Finally, complex conjugation preserves this disk, its real center,
and the zeros of H_t. A nonreal zero would have a distinct conjugate
zero in the same disk, contradicting the count of one. Hence the
zero is real, and the multiplicity count makes it simple. This
reality argument uses no preexisting real-zero theorem for the tail.

### Scope of the specialization

L488 already treats qualitative counts; it supplies no numerical
constant here and is not used as a premise. The present proof is
needed because the cited source leaves the local radius/onset
constants unnamed. Its method is retained, while the explicit
inputs are L490 and L491 and the standard named Rouché theorem.
Neither source (76) nor the coarse error in (104) is used as a
numerical bound. No independent saddle-proof audit, global strip
argument, exhaustion or collision estimate is part of this result.

### Separate critical application audit, 2026-10-30

The unchanged statement passes independent replay on its full domain.
This verifies the local quantitative specialization, not a new counting
method or a result beyond the sources assessed. The direct source check
used the linked v2, (4) and the following symmetry statement, (6)–(11),
and (16). The quantitative premises are the audited conclusions of L490
and L491; their proofs are not silently strengthened or re-audited here.
In particular no source saddle-proof verification is claimed.

For each fixed allowed t, both affine arguments have nonzero imaginary
part whenever Re(z)>0. Thus the whole open right half-plane supplies a
common domain for A, B and G. Exponentiating the specified ell_t gives
the source M_t exactly, including sqrt(2*pi)/16; hence B is holomorphic
and nowhere zero there. The unit disk is strictly inside that domain.
On the smaller closed disk, x>=X-r>X-1>=4*pi*exp(10000)+1 and
0<=y<=r<1 in its upper half. This checks L490's height and strip
hypotheses with room at the edge and retains both closed time endpoints.
L491 applies to every |w|<=r because r<1. No continuity extension from
an open time or spatial range is needed.

For upper-half z, source (11),(16) give exactly B and A/B, respectively.
Conjugation exchanges A and B, while preserving R=H_t-A-B. Consequently
the upper bound at conj(z) transfers below the axis to |R(z)/A(z)|<d,
not to |R(z)/B(z)|<d. Multiplication by |A/B|=|exp(G)| is necessary
and is present in (2). The real diameter is already covered by L490.
These identities check that the piecewise estimates bound one globally
holomorphic quotient; no piecewise definition of that quotient is used.

To check the complete error independently, set q=1/2+eta. L491 implies
Re(G)<=|v|+|epsilon|<q<51/100<2/3 throughout the closed disk. Thus
exp(Re(G))<=exp(q)<=1/(1-q)<3. Also

    |exp(v)|<=exp(1/2)<=2,
    |exp(epsilon)-1|<=exp(|epsilon|)-1
                       <exp(eta)-1<=eta/(1-eta)<2*eta.

The integer phase gives exp(i*(2*pi*n-pi))=-1, so the gamma-model
difference is exp(v)*(1-exp(epsilon)), with the sign in (5) correct.
Adding this error to the reflected residual yields exactly

    3*d+4*eta=(459000000+20040)/10^12
             =459020040/10^12<1/1000<1/4.

These are rational comparisons after applying the universal exponential
series majorants; they do not involve evaluating exp(10000) or sampling
t, X or the circle. The strict inequalities survive the allowed endpoints.

On |w|=r, the geometric sum used in (6) is explicitly
sum_(k>=2) 2^(-k)=1/2. Termwise comparison of the absolutely convergent
exponential series gives sum_(k>=2) 2^(-k)/k!<1/4, with strictness
already at k=3. Hence |1-exp(v)|>1/4 at every boundary point. Combined
with the preceding error, this verifies Rouché's strict hypothesis on
the whole circle. Both functions are holomorphic in its neighborhood.
The model zeros are precisely 4*pi*k/L; only k=0 is inside, and its
derivative is -i*L/2 != 0. Rouché counts multiplicities, so H_t/B has
total multiplicity one. The boundary inequality excludes boundary zeros,
and nonvanishing of B preserves both conclusions for H_t. The disk is
conjugation invariant; a nonreal zero would contribute two distinct zeros.
The unique zero is therefore real and has multiplicity one.

No statement repair or dependency change was needed. This first audit
certifies the selected-disk application only: it proves neither that
arbitrary high zeros belong to these disks nor any finite collision or
zero-time assertion. Full matching Mathlib coverage remains unchecked.

## Mathlib

Full matching coverage of this explicit local count is not checked;
unknown coverage is not an absence claim. Supporting formal results
for Rouché's theorem, holomorphic quotients, exponential zeros and
conjugation have not been looked up for this step. No formal
verification is claimed. The informal proof supplies the uniform
analytic comparison; its rational constants require no numerical
sampling or computational certificate.
