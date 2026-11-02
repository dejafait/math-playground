# Lemma 607: a sextic monotone-Stein law with negative first Fourier sign

## Hypotheses

For b>0 put k_b(u)=exp(-u^6-bu^2), Z_b=integral_R k_b,
p_b=k_b/Z_b, h_b(u)=integral_u^infinity v p_b(v)dv,
and tau_b=h_b/p_b. Use F_b(z)=integral_R p_b(u)exp(izu)du.
The spatial monotonicity assertion means nonincrease on [0,infinity);
tau_b is even, not nonincreasing on the entire real line.

Import Mark Bagnoli and Theodore C. Bergstrom, *Log-Concave Probability
and Its Applications*, [4 March 2004 manuscript](https://escholarship.org/content/qt0xt8k6sd/qt0xt8k6sd_noSplash_d3b995fc634e40551bbd3dc90a1b0e43.pdf),
Theorem 3 and Corollary 2, p. 4: a positive C1 log-concave probability
density on an interval has nondecreasing hazard. The concave proof case
in Appendix 8.2, p. 25, is covered by the prior assessment. Its final
sign/reference typo does not replace the stated nondecreasing-hazard
conclusion or the preceding inequality.

Import Adrien Saumard, *Weighted Poincare inequalities, concentration
inequalities and tail bounds related to Stein kernels in dimension
one*, [arXiv:1804.03926v3](https://arxiv.org/pdf/1804.03926v3),
Section 2 (5)-(6), printed pp. 3-4: for an existing connected-support
density with finite first absolute moment the centered tail ratio is
a version of its Stein kernel, with integrability and vanishing boundary
products required for the associated integration-by-parts identity.
Import the named composite Simpson error theorem for real C4 functions
from Anne Kværnø and Markus Grasmair, *Numerical integration*,
[2 September 2022 notes](https://www.math.ntnu.no/emner/TMA4130/2022h/html_notes/Quadrature.html),
“Error analysis of Simpson's rule”: with an even number of equal mesh
intervals and node spacing h, the absolute error is at most
(b-a)h^4 sup|f^(4)|/180. The single-panel proof is not reproved here.
No Newman theorem, zero motion, or finite collision is an input.

## Conclusion

Each p_b is a strictly positive even smooth probability density on R,
centered, strictly decreasing for u>0, with every derivative decaying
faster than every exponential. Its tau_b is positive, even and smooth,
nonincreasing on [0,infinity), with tau_b'(0)=0 and tau_b(u)->0 at
both infinities. Nevertheless

    F_4'(10)^2-F_4(10)F_4''(10) <= -1281153/(10^12 Z_4^2) < 0.

Thus these spatial hypotheses, including the auxiliary log-concavity,
do not imply the first Fourier Laguerre inequality. This is a generic
counterexample, not an actual-Xi sign, an RH disproof, or a claim about
all-degree signs. The independent application and certificate audit below
passes; originality is not asserted.

## Proof

**Density and endpoints.** Since 0<k_b<=exp(-b u^2), 0<Z_b<infinity.
Evenness and absolute integrability of u k_b give mean zero. Each
k_b^(j) is a polynomial times k_b, so for every j>=0 and A>0,
|p_b^(j)(u)|<=C_(j,A)exp(-A|u|). Differentiation of k_b shows strict
decrease on u>0. The integral h_b is smooth with h_b'=-u p_b.
The zero mean and evenness give h_b(-u)=h_b(u)>0; hence tau_b is
positive, smooth and even, and tau_b'(0)=0. Both tails of h_b vanish:
the positive one by absolute integrability and the negative one using
zero mean. In fact h_b decays faster than every exponential, by
integrating a corresponding bound for |u|p_b(u). Thus the Stein
identity holds, for example, for C1 functions whose values and first
derivatives have at most exponential growth: all terms are integrable
and the endpoint product with h_b vanishes. No unrestricted test class
is being asserted.

**Hazard specialization, not a reproof.** On (0,infinity) define
q_b(s)=exp(-s^3-bs), J_b=integral_0^infinity q_b(s)ds, f_b=q_b/J_b.
Here 0<J_b<=1/b, and q_b(0)=1. The density f_b is positive and C1
on its support interval, and (log f_b)''(s)=-6s<0. Its survival
S_b(s)=integral_s^infinity f_b is finite and strictly positive there.
The imported hazard theorem gives nondecrease of r_b=f_b/S_b.
For u>0 the substitution s=v^2 in the absolutely convergent tail gives

    tau_b(u) = (1/2) integral_(u^2)^infinity q_b(s)ds / q_b(u^2)
             = 1/(2 r_b(u^2)).

This auxiliary law is f_b(s)ds, not the squared-variable law with a
Jacobian. Thus tau_b is nonincreasing for u>0. At zero the formula
extends continuously with tau_b(0)=J_b/2, proving nonincrease on the
closed half-line. For s>=0 and t>=s, convexity of V(s)=s^3+bs gives
V(t)>=V(s)+(3s^2+b)(t-s). Consequently

    0<tau_b(u)<=1/[2(3u^4+b)]   (u>=0),

which proves the stated limits, including the negative tail by evenness.
The density, support, moments and endpoints required for the centered
Stein interpretation have all been checked, rather than inferred from
an arbitrary prescribed ratio.

**Fourier integrals and rigorous sign.** Let G(z)=integral_R k_4(u)exp(izu)du.
For each compact complex z set and every integer j>=0, the integrands
are dominated by |u|^j exp(A|u|-u^6-4u^2), which is integrable.
Thus G is entire, differentiation under the integral is justified, and
on R its first three derivatives in use are

    G(x)   = 2 integral_0^infinity exp(-u^6-4u^2) cos(xu)du,
    G'(x)  = -2 integral_0^infinity u exp(-u^6-4u^2) sin(xu)du,
    G''(x) = -2 integral_0^infinity u^2 exp(-u^6-4u^2) cos(xu)du.

Here is the complete error scheme for the certificate at x=10.
On [0,2] set Q(u)=u^6+4u^2 and H(u)=exp(-Q(u)+10iu).
Bounds for |-Q'+10i|, |Q''|, |Q'''|, |Q''''| are respectively
A=218, B=488, C=960, D=1440. Also |H|<=1. Differentiating H gives

    H2=A^2+B=48012,
    H3=A^3+3AB+C=10680344,
    H4=A^4+6A^2 B+3B^2+4AC+D=2399233840

as upper bounds for |H''|, |H'''|, |H''''|. Leibniz's formula gives
fourth-derivative bounds for H,uH,u^2H respectively

    M0=H4=2399233840,
    M1=2H4+4H3=4841189056,
    M2=4H4+16H3+12H2=9768397008.

They also bound the required real/imaginary parts and their negatives.
Composite Simpson with even N=8192, spacing 2/N, therefore has error
at most 16 Mj/(45 N^4) for twice each integral on [0,2]. Numerically
these bounds are below 1.90e-7, 3.83e-7, and 7.72e-7, respectively;
the exact fractions, not these decimal summaries, are used.

For u=2+v>=2, convexity gives Q(u)>=80+208v. Since e>2,
exp(-80)<2^(-80). Full-line moment-tail errors are bounded by

    T0=2*2^(-80)/208,
    T1=2*2^(-80)*(2/208+1/208^2),
    T2=2*2^(-80)*(4/208+4/208^2+2/208^3).

These follow by integrating (2+v)^j exp(-208v), for j=0,1,2,
and control the absolute sine/cosine tails regardless of their signs.

**Exact evaluation and arithmetic enclosure.** Run
`python3 scripts/sextic/certify_first_sign.py`. It uses integer interval
arithmetic with scale S=2^256: [l,h] denotes [l/S,h/S]. Addition and
negation are exact; multiplication takes the minimum/maximum of the
four endpoint products and rounds outward after division by S;
division by a positive integer rounds both endpoints outward.
All sample coordinates u=2i/N, Q(u), 10u, u^2 have exact initial
representations at this scale. Endpoint rounding is never discarded.

For exp(-Q), evaluate its Taylor polynomial of degree 80 at -Q/128,
then square the enclosure seven times. Since 0<=Q/128<=5/8, the
Lagrange remainder is at most (5/8)^81/81!<1/S. For cos and sin,
evaluate at y=10u/32, 0<=y<=5/8, using degrees 80 and 81 respectively.
Their remainders are bounded by (5/8)^82/82! and (5/8)^83/83!, each
<1/S. Widen each Taylor enclosure by one scale unit before the seven
squarings or five double-angle steps. All three remainder comparisons
are checked as exact rational inequalities by the script. Recurrences
for the Taylor terms use outward interval multiplication/division;
trigonometric double-angle steps use the old sine and cosine enclosures
simultaneously. Thus no unbounded floating-point or cancellation error
enters the certificate.

Simpson weights are 1 at endpoints, 4 at odd interior indices, 2 at
even interior indices. Multiplying their interval sum by 4/(3N)
accounts for both the spacing and the full-line factor 2. Add each
Simpson error and Tj outward. Exact rational comparison encloses the
result in

    2041/10^6 <= G(10) <= 2043/10^6,
    -552/10^6 <= G'(10) <= -550/10^6,
    777/10^6 <= G''(10) <= 779/10^6.

The full rational enclosures, derivative constants, tail errors and
all comparison outcomes are saved in
`scripts/sextic/first-sign-certificate.json`. The positive lower bounds
for G and G'' and the absolute bound for G' give

    G'(10)^2-G(10)G''(10)
       <= (552^2-2041*777)/10^12 = -1281153/10^12 < 0.

Finally F_4=G/Z_4 with positive Z_4, so its determinant is the last
quantity divided by Z_4^2. This proves the claimed strict inequality.

The locating search `python3 scripts/sextic/first_sign_search.py`
used exactly 256 exploratory triples in 0<b<=16, |x|<=64; its full
uncertified samples are in `scripts/sextic/first-sign-exploration.json`.
They are not premises of the certificate. Only b=4,x=10 received the
rigorous candidate test. No assertion of positivity at unsampled points,
finite collision, or global zero dynamics is used.

**Independent audit, 1 November 2026.** Both conclusions survive review.
The hazard theorem is applied on the auxiliary support interval, with
one-sided endpoint extension at zero; no global C1 extension of f_b by
zero to negative s is needed. The full-line Stein density p_b, unlike
that auxiliary extension, is positive and smooth everywhere. For the
stated test class, u*p_b*phi and h_b*phi' are integrable and h_b*phi
vanishes at both endpoints. Thus the imported identity's test and
boundary hypotheses really hold. The monotonicity conclusion is exactly
on [0,infinity). Compact complex domination justifies the entire Fourier
transform and its derivatives before real-variable quadrature is used.

The 74-line original certifier was inspected completely. For positive
denominators, Python integer division gives floor even for negative
integers, and -((-n)//d) gives ceiling. Hence each interval operation
encloses the true scalar operation. Induction on the Taylor-term
recurrences proves enclosure of every term and their sum; dependence
between repeated intervals only enlarges the bounds. The cosine
polynomial of displayed degree 80 is also its Taylor polynomial through
degree 81, and the sine polynomial through degree 81 is also its Taylor
polynomial through degree 82, since the additional coefficients vanish.
This justifies remainder orders 82 and 83. On the negative exponential
Taylor segment its derivative has magnitude at most 1. All three
remainders are below one scale unit, which is added before propagation.
The double-angle right-hand sides are evaluated simultaneously using
the old c,s values. Exact mesh input and rounded intermediate operations
are both checked; positivity of an approximate exponential is not an
unproved premise of the interval multiplication.

For an independent derivative-constant check, the audit starts from
P_(j,0)(u)=u^j, j=0,1,2, and performs four exact polynomial operations

    P_(j,r+1)=P_(j,r)' + (-6u^5-8u+10i)P_(j,r).

Then (u^j H)^(4)=P_(j,4)H. For polynomial coefficients a_k+i b_k,
sum_k (|a_k|+|b_k|)2^k bounds its magnitude on [0,2]. The resulting
three integer bounds are exactly M0,M1,M2 displayed above. Full
coefficient lists are saved in the audit artifact. The Simpson theorem
is applied separately to the real or imaginary component in use;
2*(2/180)*(2/N)^4 Mj=16 Mj/(45 N^4), so the full-line factor is
present. Independently summing the binomial moments gives

    Tj=2*2^(-80)*sum_(k=0)^j binom(j,k)2^(j-k) k!/208^(k+1),

which reproduces every tail, including both terms beyond the leading
one for j=2. Convexity at u=2 uses Q(2)=80 and Q'(2)=208; absolute
trigonometric bounds make these tails valid for the signed derivatives.

Reproduction: `python3 scripts/sextic/audit_first_sign.py`. The original
quadrature replay is byte-identical to its saved certificate. Its SHA256
is `8b1fbabf6182432f62accfb2b4c62b47305bda2e065b39492149da7fad92768f`.
The audit saves the raw integer Simpson sums, independently regenerated
derivative polynomials/errors/tails, all reconstructed rational endpoints,
and all six strictly positive coarse-enclosure margins in
`scripts/sextic/first-sign-audit.json`. The complete relevant values,
not a preview, were inspected. All 17 recorded checks pass; failures
are empty. This is replay plus independent error arithmetic and a
program-inclusion proof, not a second quadrature method. The positive
G and G'' lower bounds and the negative G' interval give the maximum
of G'^2 at -552/10^6; the final rational subtraction and positive
Z_4^2 normalization therefore preserve the strict sign as claimed.

This audit validates the local counterexample; it proves no new sign
beyond that certificate. Named external theorems are still imported,
their full source proofs are not independently re-established here,
and no Xi transfer, collision or all-zero statement is inferred.

## Mathlib

Full matching coverage for this counterexample and its certificate was
not checked. The result combines imported hazard/Stein facts, ordinary
calculus and explicit exact arithmetic. The informal independent audit
above is complete; a matching formal verification is not supplied.
