# Lemma 596: radial boundary growth of the exact first associated theta kernel

## Hypotheses

Use the actual theta kernel of L019 and its holomorphic continuation k
to S={z: |Im z|<pi/4} established in L239. Thus, on S,

    k(z)=sum_(m>=1) [8pi^2 m^4 exp(9z/2)-12pi m^2 exp(5z/2)]
                      exp(-pi m^2 exp(2z)).

The series converges locally absolutely, k is even, and on each closed
smaller strip |Im z|<=a<pi/4 it satisfies

    |k(r+iv)|<=C_a exp(9|r|/2-c_a exp(2|r|)),
    c_a=pi cos(2a)>0.

Define, subject to the convergence proved below,

    A(z)=integral_R s^2 k(s+z)k(s-z) ds,     z in S.

This A is the associated kernel, not the auxiliary theta function called
A in L019 and L239. No RH or zero-simplicity hypothesis is made.

## Conclusion

A is an absolutely convergent holomorphic function on S. For real
0<delta<pi/4, put h=sin(2delta), y=pi/4-delta,
s0=(1/2)log(10/(pi h)), and w=(log 2)/2. Then

    A(iy)=integral_R s^2 |k(s+iy)|^2 ds
          >=16pi^4 exp(-40) w s0^2 exp(9s0).

In particular, with the explicit positive constant

    C=16pi^4 exp(-40) w [(1/2)log(10/pi)]^2 (5/pi)^(9/2),

one has A(i(pi/4-delta))>=C delta^(-9/2), and consequently

    lim_(delta->0+) delta*A(i(pi/4-delta))=+infinity.

This excludes a radial O(delta^(-1)) bound at this boundary point. It
does not establish a horizontal boundary trace, classify singularities,
exclude arbitrary integrable horizontal traces, justify a boundary
contour shift, or prove any Fourier sign.

## Proof

### Definition and holomorphy on the open strip

Let E be a compact subset of S. Choose finite M>=0 and 0<a<pi/4
such that |Re z|<=M and |Im z|<=a for z in E. If z=u+iv, the
closed-substrip estimate in the hypotheses, together with
|s+-u|<=|s|+M and |s+-u|>=|s|-M, gives

    |s^2 k(s+z)k(s-z)|
      <=C_a^2 s^2 exp(9(|s|+M)-2c_a exp(2(|s|-M))).       (1)

The notation s+-u means either s+u or s-u in these inequalities.
The right side is integrable on R: at either end its negative
exponential term dominates every linear function of |s|. It also
bounds the integrand on each bounded interval. This proves absolute
convergence for every z and local uniform domination, including all
bounded real shifts of z; it does not assert domination uniform up
to the boundary of S.

Dominated convergence proves continuity of A. For any closed triangle
contained in S, apply (1) on its compact filled interior. Fubini applies
to its boundary integral because its perimeter is finite and (1) is
integrable. For each fixed s the integrand is holomorphic in z, so
Cauchy's integral theorem makes its boundary integral zero. Morera's
theorem now proves holomorphy of A on S. These are applications of the
standard dominated convergence, Cauchy integral and Morera theorems,
not an interchange of a boundary limit and an infinite integral.

The exact locally absolutely convergent series has real coefficients
and commutes with conjugation. Thus k(conjugate(z))=conjugate(k(z)).
For real s,y with |y|<pi/4, this gives
k(s-iy)=conjugate(k(s+iy)), proving the displayed nonnegative integral
for A(iy). In particular a lower bound on any real-s interval is valid.

### A full-series first-mode lower bound

Let z=s+iy and v=pi exp(2z), at any point with Re v>=10.
Factoring the exact series, without truncating it, yields

    k(z)=8pi^2 exp(9z/2-v) B(v),
    B(v)=1-3/(2v)
          +sum_(m>=2) (m^4-3m^2/(2v)) exp(-(m^2-1)v).   (2)

Here |v|>=10, hence 3/(2|v|)<=3/20. The entire remaining series
is absolutely bounded by

    (23/20) sum_(m>=2) m^4 exp(-10(m^2-1)).             (3)

Indeed m^2<=m^4 and the coefficient's modulus is at most
m^4+(3/20)m^2<=(23/20)m^4. For integers m>=2,
m<=2^(m-1) (by induction) and m^2-1>=3(m-1), the latter
because (m-1)(m-2)>=0. Consequently (3) is at most

    (23/20) sum_(j>=1) q^j = (23/20) q/(1-q),
    q=16 exp(-30).

The exponential series gives exp(30)>1+30+30^2/2=481, so
q<16/481<1. The last bound is strictly less than

    (23/20)(16/465)=368/9300<1/20.

The reverse triangle inequality in (2) therefore gives

    |B(v)|>1-3/20-1/20=4/5>1/2.                       (4)

This bound includes every theta mode, uniformly for all Im v whenever
Re v>=10. It uses no lower bound for a complex sum from a single
summand and makes no claim about cancellation in Re v<10.

### Moving interval and the radial limit

For the stated y and h, cos(2y)=h>0. On the interval

    s0<=s<=s0+w,

one has Re(pi exp(2(s+iy)))=pi h exp(2s) in [10,20].
Also s0>0, since h<=1 and pi<10. Applying (2) and the weaker
factor 1/2 from (4) gives throughout this interval

    |k(s+iy)|>=4pi^2 exp(9s/2-20).

All terms of the integral for A(iy) are nonnegative. Thus

    A(iy)>=16pi^4 exp(-40) integral_[s0,s0+w] s^2 exp(9s) ds
          >=16pi^4 exp(-40) w s0^2 exp(9s0),           (5)

where s^2>=s0^2 and exp(9s)>=exp(9s0) since s>=s0>0.
Finally h=sin(2delta)<=2delta and h<=1 imply

    s0>=(1/2)log(10/pi)>0,
    exp(9s0)=(10/(pi h))^(9/2)>=(5/pi)^(9/2) delta^(-9/2).

Substitution in (5) gives the claimed C. Multiplying by delta yields
delta*A(iy)>=C delta^(-7/2), which tends to positive infinity.
This proves the precise radial discriminator; no boundary value was
inserted into the integral. The exponent is a lower bound, not an
assertion of a sharp asymptotic. The independent audit below passes
without changing the statement or proof.

### Independent audit — 31 October 2026

The audit replayed the complete proof under the preexisting exact-scope
assessment, including all of L019 and the relevant strip proof of L239.
It confirms the following details; no additional mathematical premise
or boundary regularity is imported.

For (1), each of |s+u| and |s-u| lies between |s|-M and |s|+M.
Exponentiation preserves the lower inequalities even if |s|-M<0.
The two negative exponential terms therefore sum to at most
-2c_a exp(2(|s|-M)), while the two positive linear terms sum to at
most 9(|s|+M). This gives precisely (1). Its right side is bounded
on finite intervals and integrable at both ends, uniformly on E.
The maps z -> k(s+z) and z -> k(s-z) are both holomorphic on S;
the minus sign in the latter argument creates no antiholomorphic
factor. The triangle/Fubini/Morera argument uses only interior compact
sets. Conjugation follows term by term from local absolute convergence,
before identifying the absolutely convergent integral on z=iy.

For (2), division of the lower-degree term by the factored leading
coefficient gives (3/(2pi))exp(-2z)=3/(2v), including its complex
phase. Also |exp(-(m^2-1)v)|=exp(-(m^2-1)Re v). The induction
m+1<=2m propagates m<=2^(m-1), and
m^2-1-3(m-1)=(m-1)(m-2)>=0. Thus the geometric majorant retains
every mode. From exp(30)>481 one gets q<16/481 and
q/(1-q)<16/465; multiplying by 23/20 gives 368/9300.
The final comparison with 1/20 is equivalent to 7360<9300.
The reverse triangle bound is consequently strictly greater than 4/5;
using 1/2 later is valid. This check is uniform in Im v and assumes
only Re v>=10, not dominance of a lone summand without a tail bound.

For (5), h is positive and at most 1, s0>0, and
exp(2w)=2. Hence the entire moving interval lies in 10<=Re v<=20.
Taking the modulus of the factored exponential gives
exp(9s/2-Re v); squaring its weaker lower bound gives exactly
16pi^4 exp(9s-40). Integrating over an interval of length w and
using s>=s0>0 verifies every factor in (5). Finally h<=2delta
gives exp(9s0)>=(5/pi)^(9/2)delta^(-9/2), while h<=1 gives
s0^2>=[(1/2)log(10/pi)]^2. The stated C is therefore fixed and
strictly positive. The limit follows by comparison with
C delta^(-7/2), without an interchange of a limit and an integral.

The audit establishes only the stated radial model exclusion. A
horizontal trace or a stronger boundary singularity is not bounded by
this argument. No sign theorem is imported from Tuck and no Fourier
sign or all-degree Xi conclusion is verified. This is verification of
an existing local analytic estimate, not a claim of progress beyond
the inspected literature. No numerical experiment is part of the proof.

### Source comparison and qualification

This is an elementary analytic development of the exact standard theta
series and closed-substrip estimate, rather than a reproof of theta
modularity or an import of a positivity theorem. Its purpose is to test
the radial O(delta^(-1)) boundary models singled out by the preexisting
source assessment. E. O. Tuck, *On positivity of Fourier transforms*,
Bull. Austral. Math. Soc. 74 (2006), 133–138, pp.135–137, equations
(5)–(13), https://doi.org/10.1017/S0004972700047511, discusses bounded
shifted-origin, boundary-singularity and simple-pole cases; no theorem
from that paper is a mathematical input to this lower bound. Its
positivity hypotheses have not been verified for this A. L233 gives
the downstream identity for the actual theta normalization, but is not
used to prove (1)–(5). Higher-degree Xi signs remain independent gaps.
The bounded search in the approved assessment found no matching radial
limit theorem; no originality is asserted.

## Mathlib

Full matching result: not checked; availability is unknown. Supporting
holomorphic parameter integrals, dominated convergence, conjugation,
geometric-series and exponential inequalities: not checked here. No
absence claim or matching theorem name is asserted. The full elementary
tail certificate is (2)–(4), requiring no numerical script.
General documentation: https://leanprover-community.github.io/mathlib4_docs/
