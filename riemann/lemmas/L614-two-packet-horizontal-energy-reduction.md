# Lemma 614: partial domination and the remaining two-packet energy inequality

## Hypotheses

Let 0<a<=4, 0<=u,v<=2 and m,n in {1,2}. The multiset Z has
m copies of each label -a/2+iu, -a/2-iu and n copies of each
label a/2+iv, a/2-iv. At a zero depth the two coincident labels
retain their combined multiplicity. All pairs below are ordered and
count the product of multiplicities. Put

    K(z)=sin(pi*z)/(pi*z), K(0)=1,
    E=sum_(z,s in Z) K(z-s)^2,
    M=sum_(z,s in Z; Re z=Re s) 1.

The square in E is algebraic. No minimum spacing, zeta realization,
thin-box assumption, simplicity assumption or discarded pair is used.

## Conclusion

The following are partial results for the stipulated finite family:

1. If (m-n)(u-v)>=0, including either equality, then

       E >= M+8mn K(a)^2 >= M.                            (1)

2. If 0<a<=1/2, then E>=M for all the allowed parameters.
   For m!=n the stronger lower bound is

       E >= 16(1+K(a)^2) >= 16+64/pi^2 > 20=M.            (2)

3. Up to interchanging the packets, the only remaining case is
   m=1, n=2, 1/2<a<=4 and 0<=v<u<=2. Write

       w(t)=(1-|t|) on [-1,1],
       A(t)=cosh(2pi*u*t), B(t)=cosh(2pi*v*t),
       c(t)=cos(2pi*a*t).

   Its exact residual is

       (E-M)/4 = 4K(a)^2
         + int_[-1,1] w(t)[(A(t)-2B(t))^2-1
                         +4(A(t)B(t)-1)(1+c(t))] dt.     (3)

   The integral need not have a termwise nonnegative integrand;
   domination in this remaining case is NOT proved here.

4. Let u_* = arcosh(2)/(2pi). In case 3, if u<=u_*, the energy
   with u,a fixed is nondecreasing as v runs from 0 to u. Thus this
   small-depth portion reduces to v=0. Define

       H(b)=(sinh(pi*b)/(pi*b))^2, H(0)=1,
       F(a,b)=Re K(a+ib)^2.

   At v=0 its still-unresolved inequality is

       E-M = 2(H(2u)-1)+16F(a,u) >= 0.                   (4)

No full two-packet verdict, general finite-multiset domination,
equal-ordinate zeta count, charge estimate or Xi sign follows.

## Proof

### Known input and its finite specialization

Use the triangular Fourier pair

    int_[-1,1] (1-|t|) exp(2pi*i*z*t) dt = K(z)^2,

including complex z and its removable value at zero. This is the
fixed Fejer kernel in Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh,
*Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions
of Simple Zeros and Critical Zeros*,
[arXiv:2501.14545v3](https://arxiv.org/html/2501.14545v3), (4.1).
The compact support permits complex arguments; changing the Fourier
sign has no effect because the triangle is even.

The associated complete-energy norm identity is the input assessed
from Youness Lamzouri, *A new proof that more than 2/3 of the zeros
of the Riemann zeta function are simple and on the critical line*,
[arXiv:2609.02882v1](https://arxiv.org/html/2609.02882v1),
Proposition 2.1, (2.4), (2.10) and the proof through (2.21).
Its allowed choice eta=1 on [-1/2,1/2] and zero outside has L2 norm
one, is real-even and has compact support inside (-1,1); its Fourier
transform of eta^2 is K. The proposition gives the simple-real deficit
bound, not M<=E. That inequality is not strengthened by citation.
The norm identity and Fourier pair are imported, not reproved.

For clarity, their specialization to this finite multiset is

    E = int_[-1,1] w(t) |sum_(z in Z) exp(2pi*i*z*t)|^2 dt
      = 4 int_[-1,1] w(t)
          [m^2 A(t)^2+n^2 B(t)^2+2mn A(t)B(t)c(t)] dt.    (5)

Conjugation invariance is essential in the first equality: conjugating
the exponential sum replaces the summed label s by its conjugate,
with exactly the same multiplicity. Expanding the two packet sums
then gives the second equality. This is a finite expansion, so there
is no infinite interchange. Although (5) is a modulus norm, the
original individual pair contributions remain algebraic squares.

The two distinct real parts have total multiplicities 2m and 2n.
Consequently M=4m^2+4n^2 even when u=0 or v=0. Also
int w=1 and int w c=K(a)^2. Direct enumeration gives the equivalent
complete formula

    E-M = 2m^2(H(2u)-1)+2n^2(H(2v)-1)
          +4mn[F(a,u-v)+F(a,u+v)].                       (6)

Within the first packet the contribution is 2m^2[1+H(2u)],
and similarly for the second. The cross pairs in both directions
sum to 4mn times the two real parts in (6). Thus none of the
coincident labels or signed cross pairs is omitted.

### Aligned depths and multiplicities

For every real t, A,B>=1 and 1+c>=0. The integrand bracket in
(5) has the exact decomposition

    m^2 A^2+n^2 B^2+2mn ABc
        = (mA-nB)^2+2mn AB(1+c).                         (7)

If m>n and u>=v, then A>=B and
mA-nB=m(A-B)+(m-n)B>=m-n. If m<n and u<=v the reversed
inequality gives |mA-nB|>=|m-n|. If m=n this last bound is
automatic for all u,v. These cases include every possibility with
(m-n)(u-v)>=0. In all of them (7) is at least

    (m-n)^2+2mn(1+c)=m^2+n^2+2mn c.

Integrating (5) proves (1), including the endpoints and equal depths.

### A uniform bound and the small-spacing region

For m!=n the permitted values give mn=2 and M=20. Dropping
the first square in (7) and using AB>=1 gives E>=16(1+K(a)^2).
For 0<a<=1/2, concavity of sin on [0,pi/2] gives
sin(pi*a)>=2a, hence K(a)>=2/pi. Finally pi<4 proves
16+64/pi^2>20. Equal multiplicities were already covered by (1).
This proves (2) without a restriction on the depths.

### Exact residual and the small-depth reduction

If the preceding cases do not apply, exchange packet names if needed
to obtain m=1, n=2, u>v, a>1/2. This exchange leaves the energy
unchanged, as is explicit in (6). Subtracting M=20 from (5) and
using (7), int w=1 and int w c=K(a)^2 proves (3) exactly.
The term (A-2B)^2-1 can be negative; it has not been removed.

For fixed a,u, differentiating (5) with respect to v gives

    dE/dv = 16 int_[-1,1] w(t) (2pi*t) sinh(2pi*v*t)
                           [2B(t)+A(t)c(t)] dt.          (8)

All functions and derivatives are continuous on the compact integration
interval and bounded uniformly for v in [0,u], which justifies this
differentiation, including one-sided endpoint derivatives. If u<=u_*,
then A(t)<=cosh(2pi*u)<=2. Since B>=1 and c>=-1, the bracket
in (8) is at least 2B-A>=0. The remaining factors are nonnegative
because t*sinh(2pi*v*t)>=0 for v>=0. Thus dE/dv>=0.
Substituting v=0 in (6) gives (4). This proves the reduction, not
the remaining sign of (4).

### Verification limits and source comparison

The new work is the finite family reduction (1)--(4); it does not
reprove or improve a cited zeta theorem. The unchanged source
assessment is `drafts/literature/2026-11-01-aggregate-horizontal-energy-test.md`.
It found no matching full domination statement among the sources
checked, which is not a novelty certificate. L612 and L613 concern
different finite diagnostics and are contrasts only.

The floating-point search reproduced by
`python3 scripts/aggregate-energy/two_packet_probe.py` records its
grids, tolerances, minima and limitations in
`scripts/aggregate-energy/two-packet-probe.json`. It found no negative
sample at its stated tolerance. It is not an interval certificate,
does not cover unsampled parameters, and is not used in any proof
above. In particular it does not establish (3) or (4) as nonnegative.
The separate 2026-11-01 audit checked the norm specialization, ordered
multiplicities, formulas (1)--(8), compact differentiation and packet
exchange directly. C614a completes the bounded test and records its
separately implemented full arithmetic/partition audit. This does not
extend the conclusions here to general finite multisets or zeta zeros.

## Mathlib

Full matching coverage for this finite energy/count reduction is not
checked. Supporting finite sums, real hyperbolic functions, integral
identities and complex conjugation results have not been checked for
this specialization either. Unknown availability is not evidence of
absence; no Lean verification is claimed.
