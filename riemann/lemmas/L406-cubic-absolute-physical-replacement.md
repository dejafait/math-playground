# Lemma 406: absolute cubic physical replacement

## Hypotheses

Use the fixed actual functions and ordinary height derivatives of L369,
L370, L390 and L405 on the positive ray t>=40. Specifically, let

    T=1+t, L=log(2+t), f=F_0/A,
    (x,y,z)=(f,f'/L,f''/L^2), U=x^2+y^2+z^2,
    R=exp(i phi), Z=zeta(5/2+it), a=Re(RZ), h=Im(RZ), c=1/(4pi),
    M=(z^2+3xz/2+x^2/16-y^2)/2,
    K=((z-x/4)-iy)^2/2,
    d=c^2[M|Z|^2+Re(K R^2 Z^2)],
    B0=c[(x/4-z)a-yh].

Bcal is L369's exact normalized linear coefficient and Delta is L370's
exact normalized physical discriminant, as defined in L405's hypotheses.
The response is complete, including its infinite first two derivative
series. H tends to infinity through real values and ell=log H. No RH,
zero, phase independence, response truncation or signed cancellation
hypothesis is imposed.

## Conclusion

Uniformly for sufficiently large real H,

    H^(-1) integral_[H,2H] U(t)^(3/2) dt = O(ell^(9/4)),       (1)
    H^(-1) integral_[H,2H] |Delta Bcal-d B0| dt
                                      = O(ell^(5/4))
                                      = o(ell^2).            (2)

This is a local REPRODUCTION specialization of an unconditional known
absolute derivative-moment bound and the canonical physical errors.
The separate step-106 critical audit below validates (1)--(2). It removes
a transfer obligation at the stated test threshold; it neither evaluates the signed
cubic mean nor establishes its scale or sign. Clipping, the full-tail
signed arithmetic mean, total regulator-pencil margin, actual common-zero
upper counts and global mixed positivity remain unresolved. No RH
candidate follows. Constants and onset are unevaluated.

## Proof

The prior SPECIALIZE assessment is
`drafts/literature/2026-10-13-cubic-physical-replacement.md`.
Its COVERED_TARGET is precisely (2), and its fixed ordinary-jet,
complete-response scope is unchanged. The invocation explicitly approves
the mathematical attempt on this subtarget. The recorded signed cubic
source failure is independent of this absolute estimate; L405's quartic
weight replacement does not itself establish (2). No polynomial
coefficient or carrier mean is recomputed here.

### Imported absolute moment and ordinary derivatives

Import M. J. Curran and A. Heycock, *Sharp bounds for joint moments of
the Riemann zeta function*,
[arXiv:2403.00902v1, 1 March 2024, Theorem 1.1/(2) and Section 4](https://arxiv.org/html/2403.00902v1).
The inspected unconditional range has fixed derivative order n,
0<=k<=2, h_j>=0 and sum h_j<=k, with logarithmic exponent
k^2+2 sum j h_j. We use only k=3/2 and the following cases: all
h_j=0, or a single h_j=3/2 for j=1 or 2. Thus, for j=0,1,2,

    integral_[H,2H] |zeta^(j)(1/2+it)|^3 dt
                            <= C_j H ell^(9/4+3j).           (3)

The cited theorem is stated directly on [H,2H]; no change of interval
is needed. Take n=2 and (h_1,h_2)=(0,0), (3/2,0), (0,3/2), respectively.
All parameters and orders are fixed, and equality sum h_j=k
is permitted. There is no leftover negative power of |zeta| and hence
no issue at its zeros. Section 4's derivative transfer is already part
of the imported result; we do not reprove that theorem or assume RH.

L369 (4)--(6) gives exactly f=-R V for V=zeta(1/2+it), |R|=1,
omega=phi'=O(L), omega'=O(1/t). Differentiating before applying any
normalizing divisor, with zeta primes denoting complex derivatives,

    f=-R V,
    f'=-i R(omega V+zeta'),
    f''=R[(omega^2-i omega')V+2 omega zeta'+zeta''].       (4)

These identities hold at zeros too. The separately controlled gamma
phase bounds imply uniformly on [H,2H]

    |x| <= |V|,
    |y| <= C(|V|+|zeta'|/L),
    |z| <= C(|V|+|zeta'|/L+|zeta''|/L^2).               (5)

In particular the omega' contribution costs at most
C|V|/(t L^2); it has not been dropped or obtained by differentiating
an unspecified asymptotic error. For nonnegative b_0,b_1,b_2,
(b_0+b_1+b_2)^3<=9 sum b_j^3, by Holder. Applying this to (5),
and using L comparable to ell and (3), bounds each of the averaged
third powers of x,y,z by C ell^(9/4). Finally

    (x^2+y^2+z^2)^(3/2)
               <= sqrt(3)(|x|^3+|y|^3+|z|^3)

by the same finite-dimensional norm inequality. This proves (1).

### Complete physical error, curvature and sharp endpoints

The pointwise part of audited L390 (4)--(5) and its leading polynomial
calculation proves

    |Delta-d|<=C U/L, |d|+|Delta|<=C U.                 (6)

Indeed the actual response triple differs from (ca,-ch/2,-ca/4)
by O(1/L), with all triples bounded, and its discriminant polynomial
is quadratic in each triple. Its complete common-envelope correction
is 4q(x v_1-y v_0)^2/L^2 with |q|<=C/T^2, so this contributes
at most C U/(T^2 L^2), within (6). The full derivatives of Z have
absolute bounds sum n^(-5/2)(log n)^j for j<=2. Consequently this
replacement uses the full response, with no head or order-of-limits
assumption.

Audited L405 (2)--(5), retaining that same curvature, gives

    |Bcal-B0|<=C sqrt(U)/L,
    |Bcal|+|B0|<=C sqrt(U).                            (7)

The exact polarization includes -2q x v_0/L^2, bounded by
C sqrt(U)/(T^2 L^2). In particular both physical error bounds are
zero-safe, and use the sign of B0 already established in L405.
Combining the exact product difference with (6)--(7),

    |Delta Bcal-d B0|
       <= |Delta-d| |Bcal|+|d| |Bcal-B0|
       <= C U^(3/2)/L.                               (8)

Integrating directly over the closed sharp interval and using (1)
proves (2). There is no smoothing or signed endpoint interchange.
The achieved exponent 5/4 is strictly below the required exponent 2;
the quotient is O(ell^(-3/4)), tending to zero. Neither (8) nor the
absolute bound determines the signed arithmetic integral of d B0.

### Separate critical audit — 2026-10-13, step 106

This REPRODUCTION proof_audit uses the prior SPECIALIZE assessment
`drafts/literature/2026-10-13-cubic-physical-replacement-audit.md`.
Both assertions pass with their original hypotheses, exponents and
direct mathematical inputs. This verifies a local known-tool
specialization; it is not a new moment theorem or an RH consequence.

**Source endpoints.** Theorem 1.1/(2) in the cited version explicitly
allows sum h_j=k. The three choices above give exponents 9/4, 21/4
and 33/4, respectively, on the sharp dyadic interval. The two equality
cases are pure derivative moments, with no inverse zeta factor.
Section 3.1/(3)--(4) reduces to scalar derivatives. Section 4 applies
for k>=1/2, covers both real-shift signs using reflection and bounds
the strip integral; k=3/2 uses its unconditional k<=2 branch.
Its analytic rectangle approximation addresses the sharp interval.
There is no restriction to integer H or to a selected height sequence.

The displayed Cauchy identity in Section 4 has a harmless fixed-order
factor typo: the exact coefficient is n!/(2 pi i), not
1/(n! 2 pi i). For the fixed orders used here this changes only a
constant in its ensuing inequalities, not the exponent or the imported
upper bound. No source asymptotic, lower bound or signed moment is used.

**Ordinary derivatives and moment normalization.** At s=1/2+it,
dV/dt=i zeta'(s) and d(zeta'(s))/dt=i zeta''(s). Differentiating
-i R(omega V+zeta') yields

    R[omega(omega V+zeta')-i omega' V
                       +omega zeta'+zeta''],

which is precisely (4). In particular the omega' term has the stated
minus imaginary sign. Since |R|=1, omega/L is bounded and
|omega'|/L^2<=C/(t L^2), (5) follows without differentiating L.
All jets are ordinary derivatives followed by division; they are not
iterations of L^(-1)d/dt. The constants are independent of H.
For j=0,1,2, L>=ell on [H,2H], so (3) gives

    H^(-1) integral |zeta^(j)(1/2+it)/L^j|^3
                                               <= C ell^(9/4).

Applying the displayed finite Holder inequalities then proves (1),
including the omega' contribution. No pointwise zeta lower bound or
choice of a zero-free interval enters this argument.

**Full response and the two curvature signs.** To make the response
normalization explicit, let g=G/A, v_j=g^(j)/(T^2 L^j). L390
differentiates the exact b=(t^2/4-3/16-it/2)/pi before dividing,
using b'=(t/2-i/2)/pi, b''=1/(2pi), and both ordinary derivatives
of R and Z. Its complete triple is uniformly bounded and differs
from (ca,-ch/2,-ca/4) by O(1/L). Absolute convergence of the
three right-line series is uniform in t, including their logarithmic
weights. Thus these estimates contain every response derivative.

Write a_1=xv_1-yv_0, a_2=xv_2-zv_0, a_3=yv_2-zv_1.
L370 gives exactly Delta=a_2^2-4a_1 a_3+4q a_1^2/L^2.
Each a_j is O(sqrt(U)); replacing the response changes it by
O(sqrt(U)/L). Hence the polynomial error is O(U/L), and its
plus curvature correction is O(U/(T^2 L^2)). L390's leading
polynomial is exactly d, proving both bounds in (6).
Separately L369's polarization gives

    Bcal=2y v_1-x v_2-z v_0-2q x v_0/L^2.

The leading triple yields c[(x/4-z)a-yh]=B0 with this sign;
the three response errors cost O(sqrt(U)/L), and the minus
curvature term costs O(sqrt(U)/(T^2 L^2)). This proves (7).
Both identities are polynomial in the jets and remain valid at every
zero. In particular no relative comparison with d or B0 is asserted.

**Absolute product and threshold.** Use the exact identity
Delta Bcal-d B0=(Delta-d)Bcal+d(Bcal-B0). The preceding bounds
give (8) pointwise, with a fixed constant. Integration and L>=ell
give C ell^(-1) ell^(9/4)=C ell^(5/4); division by ell^2
gives C ell^(-3/4), tending to zero for all sufficiently large
real H. Closed endpoints have measure zero and no smoothing limit
or response-head limit is taken. This proves the claimed absolute
transfer at the test scale only. The signed cubic leading scale/sign,
signed full-tail passage and clipping remain unproved independently.

## Mathlib

Full matching coverage of the joint cubic derivative-moment theorem
and this actual-family physical transfer has not been checked. Finite
Holder inequalities and product differentiation are supporting standard
tools, not a formalization of (1)--(2). No library absence or formal
verification is claimed.
