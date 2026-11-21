# Corollary C033f: full-divisor phase at the fixed argument

## Hypotheses

Use C032j/m's actual positive-ordinate zeta divisor Z+, counting
multiplicity, with z_rho=gamma_rho-i*delta_rho, gamma_rho>14 and
|delta_rho|<1/2. Retain conjugation symmetry, the real anchor in
(14,15), the finite-height verification and the fixed-v1 preprint
qualifications of those results. For 1<=sigma<=2 put

    G_sigma(z)=exp(-z^2/(4*sigma))/sqrt(4*pi*sigma),
    p_sigma(x)=(1/2)*sum_(rho in Z+)
                    [G_sigma(x-z_rho)+G_sigma(x+z_rho)],
    A_sigma(y)=2*pi*integral_0^y p_sigma(x) dx.

Use the two primary theorem inputs specified in the proof below:
Sra's cumulative positivity with verified height T=3*10^12, and
Bellotti-Wong v2's inclusive count bound. The former remains an
imported preprint result; neither its source-wide proof nor the
external finite-height computation is independently verified here.
No RH, pointwise p_sigma>=0, simplicity, individual ordinate list,
signed-W estimate or unsmoothed limit is assumed.

## Conclusion

Uniformly on the closed width interval,

    0 < A_sigma(1/8) < pi*2^(-18) < pi.                (1)

Thus the real kernel in C032n(15) obeys

    k_sigma(1/8)=exp(-E_sigma(i/8))*sin(A_sigma(1/8))>0.

This supplies only the nonvanishing premise in C032n(19). No sign
of W or of an ordered two-point minor is proved. General signed
measures, output positivity, moments, actual-Xi realization and
L030-L032/C032a all-degree positivity remain unresolved.

## Proof

### Source reuse, overlap and reason for the specialization

The approved source comparison is assessment1721, separately approved
in1722. The lower sign is imported, not reproved. Suvrit Sra,
*Some positivity properties of Riemann Xi under smoothing*, fixed
[2611.00345v1](https://hexagonmath.org/pdf/2611.00345v1), released
11 November 2026, Theorem3.3, printed p6, uses
P_sigma(x)=2*integral_0^x p_sigma(t)dt. For T>=10^11 satisfying
its verified-divisor condition V(T), it gives P_sigma(x)>0 for x>0
and sigma>=1/(16*log T). Its Gaussian convention is Section3.1,
and the three proof ranges are AppendixC.5, pp23-24. These exact
hypotheses and proof cases were inspected in comparison1721 and
approval1722; their coverage is reused here.

Take T=3*10^12. Dave Platt and Tim Trudgian,
*The Riemann hypothesis is true up to 3 times 10^12*, Bull. LMS53
(2021), 792-797, [arXiv:2004.09765v1](https://arxiv.org/pdf/2004.09765v1),
Theorem1 and Section2, p2, give completeness and critical-line
verification through 3,000,175,332,800, including that endpoint.
This supplies V(T); the first-ordinate and anchor qualifications are
retained as above. Since log T>1, every sigma in [1,2] exceeds the
required threshold. Also x=1/8>0. Consequently
A_sigma(1/8)=pi*P_sigma(1/8)>0. The factor pi, rather than 2*pi,
in this last identity is essential.

For the upper estimate use Chiara Bellotti and Peng-Jie Wong,
*Improved estimates for the argument and zero-counting function of
the Riemann zeta-function*,
[2412.15470v2, 7 July 2025](https://arxiv.org/pdf/2412.15470v2),
Theorem1.1, p1, with Section5, pp23-24. With N(t) counting positive
ordinates <=t inclusively and with multiplicity, for every t>=e,

    N(t)<=M(t)+0.11200*log t+0.12567*log log t+3.77417,
    M(t)=t/(2*pi)*log(t/(2*pi*e)).                     (2)

These are the inspected v2 constants, not the older count constants
or the midpoint convention in a primed-tail theorem. No primed-tail
theorem is needed here.

C033c already implies a stronger small upper bound for this phase
on a larger complex disk, conditional on its numerical count and
reciprocal-square inputs. That is overlap, not a new discovery.
Its displayed source count differs from (2). The short independent
shell specialization here checks the approved target directly from
(2), without importing that displayed count or either extra numerical
consequence. It is a reproduction/specialization, not a general
Gaussian positivity theorem. C033c is a comparison, not a premise.

### Inclusive counts and a complete shell bound

For t>=14, log log t<=log t<=t and pi>3. If
log(t/(2*pi*e))<=0, then M(t)<=0<t^2/6. Otherwise both factors
are positive, t/(2*pi)<t/6 and log(t/(2*pi*e))<log t<=t,
so again M(t)<t^2/6. The error in (2) is less than t/4+4, since
0.11200+0.12567<1/4 and 3.77417<4. Since t>=14>4,
t/4<=t^2/4 and 4<=t^2/4. Therefore

    N(t)<(1/6+1/4+1/4)*t^2<t^2.                    (3)

Set a=1/8 and c0=exp(1/16)/sqrt(4*pi). For real 0<=x<=a,
the exact complex Gaussian modulus, simultaneously at both width
endpoints, gives

    |G_sigma(x-z_rho)|
      <=c0*exp(-(x-gamma_rho)^2/8)
      <=c0*exp(-(gamma_rho-a)^2/8).

The same bound holds for G_sigma(x+z_rho), since
x+gamma_rho>=gamma_rho-a. Here the positive modulus exponent is
delta_rho^2/(4*sigma)<=1/16 and the negative exponent uses
1/(4*sigma)>=1/8. The factor 1/2 in p cancels the two equal
majorants, including for conjugate off-line members, each of which
is still counted separately with its multiplicity. Hence

    |p_sigma(x)|<=c0*S,
    S=sum_rho exp(-(gamma_rho-a)^2/8).                (4)

To pay every occurrence in S, partition gamma>14 into the disjoint
shells [n,n+1), integers n>=14. A zero at n+1 belongs to the next
shell, once. The number in each shell is at most the inclusive
N(n+1)<(n+1)^2; the harmless overcount in this inequality is allowed.
The weight is decreasing in gamma>=14. It follows that

    S<=sum_(n=14)^infinity u_n,
    u_n=(n+1)^2*exp(-(n-1/8)^2/8).

For n>=14,

    u_(n+1)/u_n
      =((n+2)/(n+1))^2*exp(-(2*n+3/4)/8)
      <=(256/225)*exp(-115/32)<1/8.                 (5)

For the strict comparison, 115/32>3 and the first five terms of
exp(3) sum to 131/8>16. Thus the last bound is less than
256/(225*16)=16/225<1/8. This proves convergence as well as
the complete geometric tail estimate

    S< (8/7)*225*exp(-12321/512)
      < (1800/7)*2^(-24).                            (6)

Indeed 12321/512>24 and e>2. There is no finite unassigned tail:
(6) sums every shell to infinity, regardless of off-line signs.
No zero is discarded at a cutoff and no half-endpoint convention
has been substituted into (2).

### Phase and downstream interpretation

The exponential series gives exp(1/16)<=sum_(j>=0)(1/16)^j=16/15.
Since sqrt(4*pi)>3, c0<16/45<1/2. C032m supplies uniform normal
convergence, the real profile by conjugation, and the legitimate
compact integral. Alternatively (4)-(6) directly supply its absolute
uniform majorant on the real segment used here. Therefore

    |A_sigma(a)|<=2*pi*a*c0*S
      < pi*225/(7*2^24)<pi*2^(-18),                  (7)

where the last exact comparison is 225<7*2^6=448.
All bounds are independent of sigma in the closed interval; this
is an analytic enclosure, not a width grid or floating point preview.
Combining (7) with the cited strict lower sign proves (1).

C032n(15) applies to these same primitives. Its E_sigma(i*a) is
real, so exp(-E_sigma(i*a))>0, and (1) makes the sine strictly
positive. This proves the claimed fixed-argument nonvanishing.
Equation C032n(19) additionally needs a strict sign of W, still
unproved. No ordered-minor or RH conclusion follows from (1).

Its lower sign retains the preprint and finite-verification limitations
specified above; the upper bound uses no lower-sign or anchor input.

### Critical audit1725, 19 November 2026

The fixed-argument enclosure and the nonvanishing specialization pass
this later proof audit under precisely the stated source qualifications.
This verifies the saved quantitative specialization; it establishes no
new general positivity result and is not a source-wide proof audit.
The prior SPECIALIZE assessment1723, including its separate approval1724,
covers this exact audit. C033c was checked for overlap: it supplies a
stronger conditional upper bound with additional numerical inputs,
whereas this proof uses the corrected inclusive count directly.

The direct primary passages were reopened: Sra's fixed v1 (1.1),
Section2's cumulative convention, Section3.1, V(T) and Theorem3.3;
Platt--Trudgian Theorem1/Section2; and Bellotti--Wong v2 Theorem1.1
with its inclusive definition. The saved coverage of the essential
proof cases is reused; Sra AppendixC.5's three ranges and its final
appeal to PropositionC.1 were also read again. No external computation,
interval certificate or source-wide proof was rerun. The inputs are
the published/cited results with the limitations above.

In particular the two translated profiles, the divisor multiplicities,
and the half-variance parameter agree exactly with the source. An
off-line pair contributes two positive-ordinate members with equal
multiplicity, not one representative. Conjugation makes the entire
profile real on R. The source defines P=2 integral p, whereas here
A=2*pi integral p; hence A=pi*P. Platt--Trudgian's verified height
strictly exceeds the chosen 3*10^12, so any endpoint issue at that
chosen height is covered. V(T) says all zeros through T are on the
line; it does not require a high-precision coordinate list or a new
simplicity assumption. The retained first ordinate and real anchor
remain source inputs. Since T>e and x=1/8>0, Theorem3.3 applies to
all 1<=sigma<=2, giving exactly the strict lower sign used here.

For the upper bound, the decimal constants in (2) are exact stated
upper constants: their logarithmic coefficients sum to
23767/100000<1/4, and 377417/100000<4. The two cases for the sign
of the logarithm in M(t) have now been made explicit above; no
inequality is multiplied by a negative logarithm. The resulting
N(t)<(2/3)*t^2<t^2 is valid for every t>=14, not just integer t.
The shell majorant uses this bound only at integers n+1>=15.
Every gamma>14 belongs to exactly one [n,n+1); an ordinate equal
to n+1 moves to the next shell and is not omitted. The inclusive
N(n+1) can overcount that shell but is always an upper bound.
No midpoint or half-weight counting convention enters the argument.

The modulus estimate follows from

    |G_sigma(x-z_rho)|=(4*pi*sigma)^(-1/2)
        *exp(-(x-gamma_rho)^2/(4*sigma)
                      +delta_rho^2/(4*sigma)).

On the whole closed width interval its three bounds are respectively
1/sqrt(4*pi), exp(-(x-gamma)^2/8), and exp(1/16).
For 0<=x<=1/8<gamma, gamma-x>=gamma-1/8, and
gamma+x>=gamma-1/8 handles the other translate. The factor 1/2
in p therefore leaves one copy of S. Both off-line members and
all their multiplicities remain in that sum. This also supplies
an absolute uniform segment majorant independently of the lower sign.

The complete rational replay is as follows. The exponent difference
in successive shells is

    ((n+1-1/8)^2-(n-1/8)^2)/8=(2*n+3/4)/8,

whose minimum is 115/32, while the squared prefactor ratio decreases
to one and is at most 256/225. The exponential series through degree
four at 3 sums to 131/8>16. Thus the ratio is less than
16/225<1/8 (128<225). The first exponent is exactly
(14-1/8)^2/8=12321/512>24 (12321>12288). Summing the full geometric
majorant gives (6); e>2 makes its last comparison strict. This is
a proof for every shell to infinity, rather than a finite calculation.

Finally exp(1/16)<=16/15 by comparison of the exponential and
geometric series; pi>3 implies sqrt(4*pi)>3, and
16/45<1/2. Consequently

    |A_sigma(1/8)| < (pi/8)*(1800/7)*2^(-24)
                   = pi*225/(7*2^24) < pi*2^(-18),

since 225<448. These strict upper inequalities hold with one common
constant on the closed interval. The imported lower sign is pointwise
strict at every width; no explicit positive lower constant is claimed.

For the downstream interface only C032n(15),(19) is audited here,
not its other heat/PDE or coefficient claims. Its real even E has
E(i/8) real, and its straight primitive gives O(i/8)=i*A(1/8).
Therefore Im(exp(-E)*sinh(O))=exp(-E(i/8))*sin(A(1/8))>0.
C032m gives the required continuity and finite values. Hence f in
(19) is nonzero at every width and f(s)*f(t)>0. A later use of
(19) still needs its width regularity and a separately proved common
strict W sign: (g/f)'=W/f^2 is only a conditional identity for the
minor's sign. This audit neither assumes nor proves that missing sign.
It does not reopen stop1711's symmetric modulus enclosure.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is invoked. Supporting Gaussian, geometric-series and exponential
inequality APIs have not been assessed for this specialization.
