# Lemma 600: the uncorrected Jacobi heat derivative is not square integrable

## Hypotheses

Use the DLMF elliptic convention

theta_3(z|tau)=1+2 sum_(n>=1) exp(i pi tau n^2) cos(2nz), Im(tau)>0.

For every real u and complex z define

B(u,z)=(1/2)exp(u/2)[theta_3(z|i exp(2u))-1],
H(u)=partial_z^2 B(u,z)|_(z=0),
Q(u)=(2 d^2/du^2-1/2)H(u).

L2 means ordinary Lebesgue L2(R,du), with no weight, regulator,
endpoint subtraction or distributional interpretation.

## Conclusion

H and Q are real and smooth for every finite real u. As u tends to
minus infinity,

Q(u)=-(12/pi)exp(-5u/2)+O(exp(-17u/2)exp(-pi exp(-2u))).

Consequently Q(u)/exp(-5u/2) tends to -12/pi and Q is not in L2(R).
More precisely there is a finite u_0<=0 such that

|Q(u)|>=(6/pi)exp(-5u/2) for all u<=u_0.

At the other endpoint, for all u>=0,

|Q(u)|<=C exp(9u/2)exp(-pi exp(2u))

for an absolute finite C. Thus Q is square integrable on [0,infinity);
the negative endpoint alone prevents full-line membership.

These conclusions concern exactly this auxiliary derivative. They
reject it as an ordinary L2 autocorrelation factor, without deciding
any actual-Xi sign or excluding corrected profiles, mixed pairings,
weighted spaces or complete identities with compensating residuals.

## Proof

**Imported identities and differentiation.** Import the theta series
from [NIST DLMF 20.2.3](https://dlmf.nist.gov/20.2#E3) and the Jacobi
modular transformation from [20.7.32](https://dlmf.nist.gov/20.7#E32).
The conventions immediately preceding 20.7.30 specify tau'=-1/tau
and principal square roots. For x>0 the exact specialization is

theta_3(z|ix)=x^(-1/2)exp(-z^2/(pi x))theta_3(iz/x|i/x).       (1)

Indeed tau=ix and tau'=i/x both lie in the upper half-plane,
(-i tau)^(1/2)=sqrt(x)>0, and i tau'=-1/x. This imports modularity;
no new proof of that standard identity is claimed. The source version
and prior comparison are recorded in
`drafts/literature/2026-10-31-jacobi-heat-profile-integrability.md`.
[DLMF 20.1](https://dlmf.nist.gov/20.1) and
[20.2(ii)](https://dlmf.nist.gov/20.2#ii) fix the normalization and
analytic domains. No value or analyticity at tau=0 is imported.

Here is sufficient uniform control for every differentiation used.
On a compact real-u interval, x=exp(2u) lies in [a,b] with a>0;
on |z|<=R each summand and any fixed number of its z and u
derivatives are bounded by

C n^m exp(-pi a n^2+2nR)

for suitable finite C and nonnegative integer m. This is summable.
For the transformed series the corresponding bound is
C n^m exp(-pi n^2/b+2nR/a). Gaussian multipliers and their fixed
derivatives are bounded on these compact sets. These bounds justify
termwise z differentiation through order two, subsequent u
differentiation through order two, and their interchange, by local
uniform convergence. The same bounds for arbitrary fixed derivative
orders give smoothness. All terms at z=0 are real.

**The entire negative-endpoint expansion.** Differentiate (1) twice
in z at zero. The Gaussian has first derivative zero and second
derivative -2/(pi x). The transformed argument contributes
(i/x)^2=-1/x^2 to its second derivative. Therefore

partial_z^2 theta_3(0|ix)
 =x^(-1/2)[-2 theta_3(0|i/x)/(pi x)
           -partial_z^2 theta_3(0|i/x)/x^2].                 (2)

In the last theta derivative z denotes its own elliptic argument.
Equation (2) retains both the Gaussian multiplier and transformed
argument; the cross term vanishes since the Gaussian's first
derivative is zero. The subtracted constant in B has zero z
derivative. Set y=1/x=exp(-2u). The complete series in (2) gives

H(u)=-(1/pi)y^(5/4)
     -(2/pi)y^(5/4)sum_(n>=1)exp(-pi n^2 y)
     +4y^(9/4)sum_(n>=1)n^2 exp(-pi n^2 y).                (3)

The first term in (3) is exactly the transformed zero mode; it cannot
be dropped. Write E=y d/dy, so d/du=-2E and
2d^2/du^2-1/2=8E^2-1/2. For real a, b>0 and v=by,

(8E^2-1/2)[y^a exp(-by)]
 =[8a^2-1/2-8(2a+1)v+8v^2]y^a exp(-by).                  (4)

This follows by applying E twice: E^2 of that term is
[a^2-(2a+1)v+v^2] times the term. At a=5/4 the bracket in
(4) is 12-28v+8v^2; at a=9/4 it is 40-44v+8v^2.
Thus, with v_n=pi n^2 y, the exact full-series identity is

Q(u)=(y^(5/4)/pi)[-12+sum_(n>=1)P(v_n)exp(-v_n)],
P(v)=32v^3-192v^2+216v-24.                                (5)

For clarity the polynomial comes from
-2(12-28v+8v^2)+4v(40-44v+8v^2).
Local uniform estimates above justify the operations producing (5).
The operator multiplies the zero mode y^(5/4) by 12, rather than
annihilating it. The cancellation for the actual one-variable kernel
in L239 concerns different exponential modes and is not used here.

**A bound for the complete remainder.** For y>=1, v_n>=pi>1;
the elementary bound pi>1 suffices, and

|P(v_n)|<=464 v_n^3.

The constant

S_6=sum_(n>=1)n^6 exp(-pi(n^2-1))

is finite, by Gaussian domination of powers. Since
exp(-pi n^2 y)<=exp(-pi y)exp(-pi(n^2-1)) for y>=1,
the sum of the absolute values of all nonzero modes in (5) is at most

464 pi^3 S_6 y^3 exp(-pi y).                              (6)

It follows in particular that the remainder in Q is bounded by
464 pi^2 S_6 y^(17/4)exp(-pi y). This is a bound on the entire
series after all derivatives, not on a finite truncation. The same
argument also gives, for j=0,1,2,

|(d/du)^j[H(u)+(1/pi)y^(5/4)]|
 <=C_j y^(9/4+j)exp(-pi y), y>=1,

because each derivative of a term in (3) increases the polynomial
degree in v_n by at most one. This verifies directly the derivative
remainder control used in forming Q.

As y tends to infinity, y^3 exp(-pi y) tends to zero. Choose Y>=1
so that the right side of (6) is <=6 for every y>=Y; existence
follows from that limit and requires no numerical estimate. Formula
(5) then implies Q(u)<=-(6/pi)y^(5/4) whenever y>=Y. Setting
u_0=-(1/2)log Y proves the asserted lower bound. In particular

integral_(-infinity)^(u_0)|Q(u)|^2 du
 >=(36/pi^2)integral_(-infinity)^(u_0)exp(-5u)du=infinity.   (7)

Equations (5)-(6) also prove the stated asymptotic, with relative
error O(y^3 exp(-pi y)). No claim at the singular parameter tau=0
has been used: every identity holds at finite u, followed by a
controlled one-sided limit.

**The positive endpoint.** The original complete series gives

H(u)=-4exp(u/2)sum_(n>=1)n^2 exp(-pi n^2 exp(2u)),
Q(u)=sum_(n>=1)[48pi n^4 exp(5u/2)
                -32pi^2 n^6 exp(9u/2)]exp(-pi n^2 exp(2u)). (8)

For example, writing v=pi n^2 exp(2u), the operator applied to
exp(u/2)exp(-v) gives (8v^2-12v)exp(u/2)exp(-v),
which checks both coefficients in (8). For u>=0 set x=exp(2u)>=1
and factor out exp(-pi x). The remaining infinite sum is bounded
by (48pi+32pi^2)S_6 exp(9u/2), using n^4<=n^6 and
exp(-pi n^2 x)<=exp(-pi x)exp(-pi(n^2-1)). This proves the
claimed positive-endpoint bound. Its square is integrable: under
x=exp(2u) the bound reduces, up to a finite constant, to

integral_1^infinity x^(7/2)exp(-2pi x)dx<infinity.

Smoothness handles finite intervals. Together with (7) this completes
the full-line membership test. The only result established is the
specialization for the fixed Q; modularity and theta analyticity are
known imported inputs. This is an obstruction to that implementation,
not a discovery beyond the sources checked or a disproof of RH.

**Independent critical audit (2026-10-31).** The fixed statement and
the full proof above have been independently checked under
`drafts/literature/2026-10-31-l600-integrability-critical-audit.md`.
No change of hypotheses or repair was required. The following checks
make explicit the differentiation and endpoint evidence for acceptance.

For a summand T=y^a exp(-v), v=by, direct differentiation gives

D_u T=-2(a-v)T,
D_u^2 T=4[a^2-(2a+1)v+v^2]T.

For j=0,1,2 its j-th derivative is bounded by C_(a,j) v^j T
when y>=1 and b=pi n^2. Consequently the two nonzero-mode parts
of (3), after j derivatives and summing absolute values, are bounded
respectively by constants times

y^(5/4+j) exp(-pi y) sum_(n>=1)n^(2j)exp(-pi(n^2-1)),
y^(9/4+j) exp(-pi y) sum_(n>=1)n^(2+2j)exp(-pi(n^2-1)).

Both entire sums are finite; y>=1 gives exactly the claimed common
y^(9/4+j) remainder bound. These are endpoint bounds in addition to,
not substitutes for, the compact-set uniform differentiation bounds.
The transformed Gaussian contributes -2/(pi x), and the elliptic
argument contributes (i/x)^2=-1/x^2; their combination reproduces
all three terms of (3). The operator multiplies its zero mode by 12.
Independently combining the other terms gives cubic coefficients
(32,-192,216,-24), with absolute coefficient sum 464 as used in (6).
Thus the relative error is at most
(464 pi^3 S_6/12)y^3 exp(-pi y), which tends to zero. This verifies
the eventual lower bound on a whole negative half-line, rather than
on a sequence. Squaring gives exp(-5u), whose integral there diverges.

For the direct positive-endpoint summand f=exp(u/2)exp(-v),
v=pi n^2 exp(2u), one has f'/f=1/2-2v and
f''/f=1/4-6v+4v^2. Multiplication by -4n^2 after applying
2D_u^2-1/2 reproduces both coefficients in (8). The same finite
S_6 controls the whole sum, and its squared bound integrates to a
constant times integral_1^infinity x^(7/2)exp(-2pi x)dx.
The audit therefore accepts precisely the ordinary-L2 implementation
stop, not any correction, mixed correlation or actual-Xi conclusion.

## Mathlib

Coverage of this full logarithmic-pullback statement and its
supporting Jacobi modular/elliptic-derivative identities was not
checked. Availability is unknown; no absence or matching formal
theorem is claimed. The proof uses the precisely cited DLMF inputs
and the explicit analytic estimates above, with no Mathlib dependency.
