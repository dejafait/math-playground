# Corollary C033d: conditional error budget for the fixed saved coefficient

## Hypotheses

Use C032m/q's qualified actual-divisor family on W=[1,2], at the
single fixed point w=i/4. Write E=E_sigma(i/4), O=O_sigma(i/4),
kappa=exp(-E)*sinh(O). Retain their actual positive-ordinate divisor,
multiplicity, no-ordinate-zero, strip/counting and inherited finite-zero,
heat and fixed-v1 qualifications. These source inputs are not
independently verified here. No reality of E or O is used.

Let c be the exact rational entry
`/candidate/coefficients/Im_kappa_imaginary_1~14` in
`scripts/smoothed-law/bounded_variation_dual_1571.json`, namely

    c=-1313856261460852651698517424056740423120000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000/35468128185841057810934033462631278307784452433174229572507840657635824754834175109863281250004123020165856090648277558652033231447112095364941.

Set C=|c|>0 and q(sigma)=c*Im(kappa). Every other coefficient of the
saved candidate is zero. Treat c only as fixed rational data; neither
the correctness of its generating boxes, their optimum nor their E
constant21 is an assumption. No coefficient optimization is performed.

Suppose complex approximants Ehat_sigma and Ohat_sigma and real constants
a, B, e, o satisfy, for EVERY sigma in the closed interval W,

    Re(Ehat_sigma)>=a,  |Ohat_sigma|<=B,
    |E-Ehat_sigma|<=e,  |O-Ohat_sigma|<=o,       B,e,o>=0.       (1)

Suppose a real evaluated function qtilde has a separate uniform final
arithmetic allowance h>=0:

    |qtilde-c*Im(exp(-Ehat_sigma)*sinh(Ohat_sigma))|<=h.        (2)

For the residual conclusion assume additionally a certified m>0 with

    ||1+qtilde||_infinity<=1/2-m.                            (3)

Equation (3) is an explicit unpaid premise, not furnished by saved1571.
In particular a reported upper bound greater than999/1000 supplies no
such margin. All uniform assertions require width enclosures, not
values on a finite grid. Continuity of the approximants is unnecessary
for this pointwise uniform error statement.

For the optional gamma application1706, use C032z(5) in its exact
normalization E_sigma(w)=U_sigma(w)+Gamma_sigma(w), where

    U_sigma(w)=h_(sigma,w)(i/2)
       +sum_(n>=2) Lambda(n)/(sqrt(n)*log(n))
          *exp(-sigma*(log(n))^2)*(cosh(w*log(n))-1).

Here h_(sigma,w) is C032z's integrated spectral test, not the arithmetic
allowance h in(2). Use exactly C033e's rational expression Q with
cutoff16, n4096, h_step=1/256 and degree2336. Suppose a complex
approximation Uhat_sigma has a certified uniform error
|U_sigma(i/4)-Uhat_sigma|<=epsilon_U, epsilon_U>=0, for every sigma
in W. All primitive arithmetic in Uhat belongs to epsilon_U. Set
Ehat_sigma=Uhat_sigma+Q(sigma,i/4), with Q evaluated exactly at the
mathematical level. Any additional approximation of Q must have its
own uniform error added to epsilon_U. Conditions on a,B,o,h,m in
(1)-(3) remain additional premises; none follows from this decomposition.

## Conclusion

The sufficient weighted error bound is

    ||q-qtilde||_infinity <= H(e,o)+h,
    H(e,o)=C*exp(-a)*[(exp(e)-1)*sinh(B)
                        +exp(e)*o*cosh(B+o)].                (4)

Consequently (3) and H(e,o)+h<m imply ||1+q||_infinity<1/2.
Here is an explicit O allowance: choose a cap t>0 and put

    D=m-h-C*exp(-a)*(exp(e)-1)*sinh(B).

If D>0, it suffices that

    0<=o<=t,
    o < D*exp(a-e)/(C*cosh(B+t)).                            (5)

These are sufficient conditions only. Failure of D>0 or of (5) proves
neither necessary precision nor an actual-kernel obstruction.

For the special zero approximant Ohat=0, B=0, C033c supplies

    o0=2*A,
    A=3*(40*(3/8)^18+10^(-100)),
    0<o0<1/65536.                                          (6)

Thus (4) becomes H(e,o0)=C*exp(-a+e)*o0*cosh(o0).
One may take t=1/65536 in (5) if the OTHER hypotheses, including (3),
hold. But if the whole fixed candidate is evaluated with Ohat=0 and
exact final arithmetic, qtilde=0 and its residual is exactly1; (3)
then fails for every m>0. The zero-centered O allowance by itself
does not provide a successful residual. Nonzero approximants or
independent actual residual evidence are not supplied by this lemma.

For application1706, the combined gamma error satisfies, uniformly on
the full component domain sigma in[1,2], |w|<=2,

    |Gamma_sigma(w)-Q(sigma,w)|<=delta_Gamma,
    delta_Gamma=4*exp(-128)+1139/98304+2^-135
                   <g=95/8192<1/64.                     (10)

In particular at the saved w=i/4 one can use e=epsilon_U+g in(4).
Under all the remaining hypotheses (1)-(3), the sufficient residual
test is therefore

    H_Gamma+h<m,
    H_Gamma=C*exp(-a)*[(exp(epsilon_U+g)-1)*sinh(B)
              +exp(epsilon_U+g)*o*cosh(B+o)].             (11)

The O allowance(5) applies with this same e. This is an explicit
conditional allocation, not a numerical residual certificate. No value
of epsilon_U,a,B,o,h or successful m is furnished by(10).
Separate critical audit1708 below validates application1706 without
correction, reusing the component audits and retaining all these premises.

Conditional on C032q's full measure hypotheses, a verified bound
||1+q||<1/2 would exclude mass-one full odd annihilators with variation
at most2. No such bound is established here. Unrestricted variation,
positive-output feasibility, H_d=o(d), S_F=0, unsmoothed Xi realization
and actual-Xi all-degree positivity remain open.

## Proof

### Imported scalar tools and necessity of the specialization

Reuse the ready SPECIALIZE assessment
`drafts/literature/2026-11-18-fixed-coefficient-kappa-budget-1619.md`.
Import NIST DLMF, release1.2.8, equations
[4.2.22](https://dlmf.nist.gov/4.2.E22) (complex exponential modulus),
[4.7.7](https://dlmf.nist.gov/4.7.E7) (exponential derivative),
[4.28.1-2](https://dlmf.nist.gov/4.28) (sinh/cosh definitions), and
[4.34.1](https://dlmf.nist.gov/4.34.E1) (sinh derivative).
Use the standard fundamental theorem of calculus along a finite real
parameter interval and the triangle inequality. These known results
are not reproved. We must specialize them because C032w(13) propagates
errors in polynomial coefficients to E/O, and expressly does not pay
the later nonlinear operations or this dictionary multiplier.

For any complex z, the imported definitions and triangle inequality
give |cosh(z)|<=cosh(|z|); integration of the imported sinh derivative
from0 to z gives |sinh(z)|<=sinh(|z|). The same finite-segment formula
gives |exp(z)-1|<=exp(|z|)-1. These are scalar consequences used only
for the present specialization, not new general evaluation theorems.

### Separate the two primitive errors

Fix sigma and put dE=E-Ehat, dO=O-Ohat. The identity

    exp(-E)*sinh(O)-exp(-Ehat)*sinh(Ohat)
      =exp(-E)*[sinh(O)-sinh(Ohat)]
        +[exp(-E)-exp(-Ehat)]*sinh(Ohat)                   (7)

has no real-valuedness assumption. By (1) and exponential modulus,

    |exp(-E)|<=exp(-a+e),
    |exp(-E)-exp(-Ehat)|
      =|exp(-Ehat)|*|exp(-dE)-1|
      <=exp(-a)*(exp(e)-1).                              (8)

Every point Ohat+s*dO, 0<=s<=1, has modulus at most B+o.
The finite-segment fundamental theorem gives

    sinh(O)-sinh(Ohat)=dO*integral_0^1 cosh(Ohat+s*dO) ds,
    |sinh(O)-sinh(Ohat)|<=o*cosh(B+o).                    (9)

Also |sinh(Ohat)|<=sinh(B). Inserting (8)-(9) into (7), taking
imaginary parts (|Im z|<=|z|), multiplying by C and adding (2)
proves (4). The constants are independent of sigma; endpoints are
included. No infinite sum, limiting interchange or spatial contour
is introduced. For a residual, the triangle inequality gives

    ||1+q||<=||1+qtilde||+||q-qtilde||
             <=1/2-m+H(e,o)+h<1/2.

If D>0 and o<=t, monotonicity of real cosh on [0,infinity) bounds
the O-dependent term in (4) by C*exp(-a+e)*o*cosh(B+t).
The strict inequality (5) makes that term less than D, yielding the
strict residual threshold. This proves the stated sufficient tolerance,
including e=0, o=0 and B=0; C and cosh(B+t) are strictly positive.
An arbitrarily bad majorant does not imply a lower bound on true error.

### Source of primitive errors, and the zero-centered comparison

If Ehat/Ohat are obtained from C032w, e and o must include BOTH its
analytic errors(12) and coefficient/final primitive arithmetic errors(13).
Its final primitive arithmetic belongs in e/o. The later exp/sinh,
imaginary-part evaluation and multiplication by c belong in h. No
numerical value of a or e is imported from calculation1571. In general
a bound on |Ehat| is stronger than needed: a lower bound on Re(Ehat)
is the relevant input to (8). A bound on Re(E) alone could also bound
that factor, but it would need its own certificate.

C033c gives |O_sigma(w)|<=8*|w|*A on |w|<=2. At w=i/4 this is
exactly o0=2*A, uniformly for sigma in[1,2]. The rational inequality
16*A<1/8192 from that lemma implies o0<1/65536, proving (6).
For B=0 the E-error summand in (4) vanishes; the factor exp(-a+e)
still requires a certified E enclosure. The weighted rational factor
C*o0 is approximately1.9119813272e-10. This is not the weighted
kernel bound: exp(-a+e) and cosh(o0) remain. The decimal is descriptive;
the exact fraction and strict rational comparisons are stored by
`scripts/smoothed-law/fixed_coefficient_budget_1620.py` in
`scripts/smoothed-law/fixed_coefficient_budget_1620.json`.
Run the script with python3 from this notebook. It checks the full
coefficient object, equality with the literal c above, (6), and the
stated rational factor. It checks neither E nor any residual premise.

Finally C032q supplies J_eta=0 and finite variation norm pairing.
For such a mass-one eta, integral q deta=c*Im(J_eta(i/4))=0,
so 1=|integral(1+q)deta|<=2*||1+q||. Thus the strict threshold
would contradict variation<=2. This only explains downstream use;
the threshold remains unmet. Nonnegative output is allowed in that
feasible class but is not needed for this single odd constraint.

### Gamma application1706 — 19 November2026

This bounded application uses the preexisting SPECIALIZE assessment
`drafts/literature/2026-11-19-saved-coefficient-gamma-application-1704.md`.
Reuse C033a/b/e's completed component audits; no component is rebuilt.
Check the existing finite-segment argument above before applying it:
the real-parameter map s -> sinh(Ohat+s*dO) is continuously
differentiable on[0,1], with derivative dO*cosh(Ohat+s*dO).
Every segment point has modulus at most B+o. Hence its derivative
norm is at most o*cosh(B+o) on the entire closed segment, including
when dO=0. This justifies(9) for complex endpoints. The exponential
segment likewise gives |exp(-dE)-1|<=exp(|dE|)-1, including dE=0.
Since Re(E)>=Re(Ehat)-|dE|>=a-e, (8) and the split(7) apply without
a real E or O assumption. These checks validate the scalar argument
needed here; they do not independently audit its inherited divisor
inputs or the newly recorded application.

Let M(sigma,w) be C033b's exact midpoint sum. C033a(5), C033b(4)
and C033e(3), on their identical closed parameter domain, give

    |Gamma-Q|<=|Gamma-integral_0^16 I(v)dv|
                +|integral_0^16 I(v)dv-M|+|M-Q|
             <=4*exp(-128)+1139/98304+2^-135.

The coefficient of Gamma in C032z(5) is exactly one. Thus no factor
of2, pi or saved dictionary coefficient belongs in this primitive
error. There is no exchange of limits: these are three already
established uniform bounds and a finite triangle inequality.
For the rational allowance use the existing exp(1)>2 comparison
from C033a's proof. It implies 4*exp(-128)<2^-126. Furthermore

    2^-126+2^-135<2^-125<1/98304,
    98304=3*2^15<2^17<2^125.

Consequently delta_Gamma<1140/98304=95/8192, and
95/8192<128/8192=1/64. This proves(10) without decimal arithmetic
or evaluating the large rational polynomial Q.

At w=i/4, C032z(5) and the definition of Ehat now give

    |E-Ehat|<=|U-Uhat|+|Gamma-Q|
             <=epsilon_U+delta_Gamma<epsilon_U+g.

Choose e=epsilon_U+g. If the separately required uniform lower
enclosure Re(Ehat)>=a, O enclosures |Ohat|<=B, |O-Ohat|<=o,
final arithmetic bound(2) and residual margin(3) are all certified,
then (1) holds and applying(4) gives exactly(11). In particular,
the primitive gamma error enters both exponential factors in(11);
it is not a final error C*g. The allowance h covers subsequent
exp/sinh, imaginary-part evaluation and multiplication by the exact c;
it does not conceal primitive U or Q arithmetic. Neither width samples
nor the unaudited constant21 can furnish the uniform E enclosure.

No such independent numerical premises are established in this step.
With Ohat=0 and exact final arithmetic, qtilde=0 for every sigma
regardless of this gamma replacement; the residual is still exactly1,
so no positive m satisfies(3). This refutes only that approximant's
ability to pass the sufficient test. It is not a lower bound for the
actual residual, a necessary precision estimate, or an obstruction
to a different approximant. Stop at the conditional application and
park numerical evaluation/optimization. Its separate critical audit is
recorded below; it supplies none of the missing numerical premises.

### Critical audit1708 — 19 November2026

Application1706 passes the independent audit under the unchanged
SPECIALIZE assessment1706, separately source-approved1707. This is
REPRODUCTION: an independently checked local allocation of already
established component errors, with no result beyond the sources checked.
The audit reuses the full component audits in C033a/b/e and the qualified
interfaces of C032m/q/z; it does not independently certify their external
divisor, finite-zero, heat or fixed-v1 source premises.

**Same domain and exact expressions.** C033a(5), C033b(4) and C033e(3)
all hold for every real sigma in[1,2] and complex |w|<=2, including their
boundaries. The integral in the first two statements uses the identical
I(v), with its removable endpoint. The sum in the last two statements is
the identical exact midpoint sum M, with v_j=(2j+1)/512, j=0,...,4095
and weight1/256. C033e's Q uses degree2336 and nonzero constant rational
denominators, and is exact at the mathematical level. Consequently the
triangle inequality through integral_0^16 I and M gives exactly

    |Gamma-Q|<=4*exp(-128)+1139/98304+2^-135.

No rounding, width interpolation or new quadrature error is absorbed in
this sum. If Q is subsequently approximated, its uniform primitive
error must be added separately, as the hypotheses require.

**Strict rational allowance and normalization.** The existing exp(1)>2
comparison implies 4*exp(-128)<2^-126. Since

    2^-126+2^-135<2*2^-126=2^-125,
    98304=3*2^15<2^17<2^125,

the two small terms have sum less than1/98304. Adding1139/98304 gives
strictly less than1140/98304=95/8192. Also95<128 proves g<1/64.
This verifies the stated actual bound against its required allowance,
without a decimal approximation or a numerical Q evaluation.
C032z(5) has Gamma exactly as the integral divided by4*pi; C033a(2)
defines that same Gamma. The other terms in C032z(5) are precisely U
in the hypotheses. Thus E=U+Gamma, with coefficient one, and

    E-Ehat=(U-Uhat)+(Gamma-Q),
    |E-Ehat|<=epsilon_U+delta_Gamma<epsilon_U+g.

There is no extra divisor-pair factor, Fourier factor or coefficient C
at this primitive-error stage. Fixed c is only rational data in the
later real linear functional. Its generating boxes and constant21
play no role, and its exact magnitude need not be evaluated for this
conditional argument.

**Finite complex segments.** For dO=O-Ohat, the map
s -> sinh(Ohat+s*dO) is C^1 on the real interval[0,1]. Its derivative
is dO*cosh(Ohat+s*dO), and every segment point has modulus at most
B+o. The imported exponential definitions imply
|cosh z|<=cosh(|z|); hence the derivative norm is bounded throughout
the interval by o*cosh(B+o). The fundamental theorem on that real
interval proves(9), including dO=0 and both endpoints. Integrating
cosh(s*z)*z from0 to1 likewise gives |sinh z|<=sinh(|z|).
For the exponential difference the exact real-segment identity is

    exp(-dE)-1=-dE*integral_0^1 exp(-s*dE)ds.

Its modulus is at most integral_0^1 |dE|*exp(s*|dE|)ds, which equals
exp(|dE|)-1 when |dE|>0 and is0 when dE=0. Also
Re(E)>=a-e and |exp(-Ehat)|<=exp(-a). These facts give both estimates
in(8). Only finite real integration and complex norm inequalities are
used; a complex mean-value point is neither asserted nor needed.

**Both nonlinear factors and the residual.** Identity(7) puts the
exponential-difference term with sinh(Ohat) and the O-difference term
with exp(-E). The preceding bounds therefore give respectively

    exp(-a)*(exp(e)-1)*sinh(B),
    exp(-a+e)*o*cosh(B+o).

Taking the imaginary part, multiplying by C=|c| and adding the
separate final arithmetic allowance h gives(4). Taking
e=epsilon_U+g changes BOTH exp(e) occurrences, giving exactly(11).
The bound is not C*g, and h cannot pay U or Q primitive errors twice
or silently replace them. The same e is required in D and(5).
All constants are uniform on the closed width interval, so taking
the supremum preserves the pointwise bounds without assuming
continuity of the approximants.

If the separately certified premise(3) and H_Gamma+h<m hold, the
triangle inequality proves ||1+q||<1/2. For C032q's mass-one signed
eta with J_eta=0 and variation<=2, finite-variation pairing yields

    integral q deta=c*Im(J_eta(i/4))=0,
    1=|integral(1+q)deta|<=2*||1+q||,

which would be a contradiction. This downstream implication needs
C032q's entire qualified family, not just scalar calculus. It asserts
neither such a residual nor feasibility for unrestricted variation.
With Ohat=0 and exact final arithmetic, sinh(Ohat)=0, qtilde=0 and
||1+qtilde||=1. Premise(3) is then impossible for every m>0,
independently of Gamma, Uhat or a. This is an exact check on that
approximant, not a lower bound for the actual-kernel residual.

Thus the conditional allocation is validated; epsilon_U,a,B,o,h and
a successful positive m remain unpaid. Numerical evaluation stays
parked. No all-order cancellation, positive-output construction,
H_d=o(d), S_F=0, unsmoothed Xi realization or actual-Xi sign follows.
Full matching Mathlib coverage remains unknown; the supporting
real-convex mean-value interface below is consistent with these finite
real-segment checks and is not a formal verification of this audit.

### Decision and qualifications

The approved target is completed as a conditional sufficient budget.
Park dependent evaluator/optimizer construction: no audited E enclosure
and successful residual margin are presently established. In particular
the unweighted zero O approximation cannot itself supply the missing
margin. Preserve stops1536/1571/1576/1586/1608 in their original scopes.
Application1706, independently validated in audit1708, supplies the
combined gamma allowance and its conditional downstream substitution,
but does not pay the independent numerical premises. This is
reproduction/specialization of known scalar tools, with no
new RH sign result, no actual-dictionary lower bound and no claimed
progress beyond the inspected sources. It is not a complete candidate.

## Mathlib

Full matching coverage is unchecked and unknown. No Mathlib theorem
is invoked, and no absence claim is made. Complex exponential and
hyperbolic-function estimates, finite-interval integration and rational
arithmetic are supporting interfaces; coverage of this full conditional
coefficient/width specialization has not been established.
Assessment1704 records supporting coverage in the pinned
[Mathlib mean-value source](https://github.com/leanprover-community/mathlib4/blob/a97078fa10bf05fba8125e4be8917ccb5b33ff80/Mathlib/Analysis/Calculus/MeanValue.lean#L640),
`Convex.norm_image_sub_le_of_norm_hasDerivWithin_le`: it requires
both endpoints in a real-convex set, derivatives within that set
everywhere and a uniform derivative norm bound. The segment check
above supplies the analogous scalar hypotheses; this is supporting
coverage, not a formal verification or full matching theorem.
