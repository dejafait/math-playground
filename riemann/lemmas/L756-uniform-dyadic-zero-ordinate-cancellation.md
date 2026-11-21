# Lemma 756: uniform dyadic zero-ordinate cancellation

## Hypotheses

Let the sum below run over all nontrivial zeros rho=beta+i gamma of
zeta, with their analytic multiplicities and gamma>0. Distinct zeros
sharing gamma contribute separately. Let T tend to infinity through
real values and let tau be real with T<=tau<=2T. All logarithms are
natural and u^(-i tau)=exp(-i tau log u) for u>0.

Use the following unconditional standard inputs, in their stated
normalizations.

1. The Riemann--von Mangoldt formula and von Mangoldt's bound
   S(u)=O(log u). Here S is the argument obtained along
   2 -> 2+iu -> 1/2+iu, with arg zeta(2)=0, and averaged between its
   one-sided limits at an ordinate. Write N_+(u) for the count with
   0<gamma<=u, m(u) for the sum of all orders at gamma=u, and
   N_*(u)=N_+(u)-m(u)/2 for the half-endpoint count. Put

       M(u)=u/(2pi) log(u/(2pi e))+7/8.

   Then

       N_*(u)=M(u)+S(u)+q(u),
       |q(u)|<=1/(150u), u>=2pi.                         (1)

   The precise correction bound, conventions and continuity of q at
   zero heights are from Richard P. Brent, David J. Platt and Timothy
   S. Trudgian, *Accurate estimation of sums over zeros of the Riemann
   zeta-function*, Math. Comp. **90** (2021), 2923--2935,
   [DOI 10.1090/mcom/3652](https://doi.org/10.1090/mcom/3652),
   Section 2, (5)--(8), Lemma 2 and proof, pp.2926--2927,
   [published author offprint](https://maths-people.anu.edu.au/brent/pd/rpb276-MC-preprint.pdf).
   Reuse the inspected source coverage in
   `drafts/literature/2026-10-07-signed-count-oscillation-comparison.md`;
   no fresh successful retrieval of that offprint is asserted here.
   The standard pointwise S bound is also explicitly recorded in
   Garunkstis--Sourmelidis--Steuding,
   [arXiv:2505.14228v1](https://arxiv.org/html/2505.14228v1),
   *The Lindelof Hypothesis for Zeta Zero Ordinates* (20 May 2025),
   (3)--(4), pp.2--3. A bound first stated off ordinates extends to
   both one-sided limits and their average, with the same asymptotic
   constant. None of the RH-dependent bounds is used.

2. Selberg's unconditional second moment:

       integral_0^X |S(u)|^2 du
         = X/(2pi^2) log log X + O(X sqrt(log log X)).    (2)

   Citation: Atle Selberg, *Contributions to the theory of the Riemann
   zeta-function*, Arch. Math. Naturvid. **48** (1946), no.5, 89--155,
   Theorems 6--7; the precise unconditional restatement (2) and S
   conventions were inspected in Andres Chirre and Emily
   Quesada-Herrera, *The second moment of S_n(t) on the Riemann
   hypothesis*, [arXiv:2006.08503v2](https://arxiv.org/html/2006.08503v2)
   (6 October 2021), Section 1.1 and Section 1.2, (1.4), PDF pp.1--2.
   Import the named standard theorem through that explicit restatement.
   Selberg's original proof is independently unchecked. The modern
   paper's RH-dependent Theorem 1 and its stronger conditional
   remainder are excluded. Only the upper bound O(X log log X) is
   needed; no reproof is attempted.

3. L467's closed-unit-shell estimate, retaining all orders, gives

       m(u)<=18 log(u+2), u>=0,                          (3)

   by counting the subset at u inside [u,u+1]. This is used only
   for endpoint bookkeeping, not for oscillatory cancellation.

The ready assessment at invocation is
`drafts/literature/2026-11-04-zero-ordinate-selberg-specialization.md`
(SPECIALIZE), with duplicate/failure comparison in its parent assessment.
This proof localizes the Stieltjes argument of GSS Section 2, (6)--(8),
pp.3--5, and substitutes (2) for its pointwise integral estimate.
That elementary specialization is the reason for writing it out.
Neither the contour proof nor GSS's RH corollary is an input.

## Conclusion

Uniformly for all real T<=tau<=2T,

    Z(T,tau):=sum_{T<gamma<=2T} gamma^(-i tau)
      =O(T sqrt(log log T)+log T)=o(T log T).             (4)

The estimate retains all zero orders at arbitrary real endpoints.
Strict, closed and half-weight endpoint conventions differ by
O(log T) uniformly, as specified in the proof. Constants are absolute
and independent of tau,T in the stated asymptotic range. This is a
specialization of known inputs, not a claim of progress beyond the
inspected literature or of originality. It supplies no RH conclusion,
beta-dependent witness weights, shorter-window estimate, paid analytic
margin, initial Laguerre sign or actual-Xi positivity.

## Proof

Fix T sufficiently large that T>=2pi, log log T>0 and the upper bound
from (2) applies at 2T. The multiset of zeros in a bounded positive
height interval is finite. Thus N_+ is right continuous, locally of
bounded variation, and its Stieltjes measure has mass equal to the
full total order m(u) at u. Let

    f(u)=u^(-i tau),   R(u)=N_+(u)-M(u).

Then |f(u)|=1 and f'(u)=-i tau f(u)/u. Partial summation for the
right-continuous count, with lower endpoint excluded and upper included,
gives the exact identity

    Z(T,tau)
      = integral_T^(2T) f(u) M'(u) du
        + f(2T)R(2T)-f(T)R(T)
        + i tau integral_T^(2T) R(u)f(u)/u du.           (5)

To see the endpoint convention directly, for each ordinate gamma the
count contribution is 1_{u>=gamma} times its order. In
[f N_+]_T^(2T)-integral_T^(2T) N_+ f', a gamma<=T contributes zero,
a T<gamma<=2T contributes f(gamma), and a gamma>2T contributes zero.
The gamma=2T contribution is f(2T). The finite-sum identity therefore
proves partial summation at arbitrary endpoints without a good-height
assumption. Applying ordinary integration by parts to the smooth M
then gives (5). No infinite sum/integral interchange is used.

Equation (1) implies at every endpoint

    R(u)=S(u)+q(u)+m(u)/2.                              (6)

The pointwise S bound, (1) and (3) give

    |R(T)|+|R(2T)|=O(log T).                            (7)

In particular (6) does not replace an inclusive count by an averaged
count. The set of ordinates is discrete on compact positive-height
intervals and has measure zero. Away from it, m=0 and R=S+q. Hence
(5) becomes exactly

    Z=I+[fR]_T^(2T)
          +i tau integral_T^(2T) S(u)f(u)/u du
          +i tau integral_T^(2T) q(u)f(u)/u du,
    I=integral_T^(2T) f(u)/(2pi) log(u/(2pi)) du.         (8)

Here all remaining integrals are ordinary Lebesgue integrals; changing
values at the discrete ordinate set does not change them. The smooth
7/8 is included in M, has zero derivative, and cancels exactly in (5).
No unestimated count correction has been dropped.

The antiderivative of the smooth integrand is

    F_tau(u)=u^(1-i tau)/(2pi(1-i tau))
               * (log(u/(2pi))-1/(1-i tau)).

Differentiation gives F_tau'(u)=f(u)log(u/(2pi))/(2pi), so
I=F_tau(2T)-F_tau(T). Since |1-i tau|>=tau>=T and u is T or 2T,

    |I| <= (3T)/(2pi tau)*(log(2T)+1/tau)
         <= 3/(2pi)*(log(2T)+1/T)=O(log T).             (9)

We used u>=2pi to bound the absolute logarithm by log(2T).
Thus even the smooth term is retained and estimated uniformly.

Choose an absolute C>0 and an absolute X_0 so that (2) gives
integral_0^X |S|^2<=C X log log X for X>=X_0. Nonnegativity and
Cauchy--Schwarz yield, for 2T>=X_0,

    |tau integral_T^(2T) S(u)f(u)/u du|
      <=tau*(integral_T^(2T)|S(u)|^2 du)^(1/2)
             *(integral_T^(2T) u^(-2) du)^(1/2)
      <=tau*(2C T log log(2T))^(1/2)*(1/(2T))^(1/2)
      =tau*sqrt(C log log(2T))
      <=2T sqrt(C log log(2T)).                         (10)

No cancellation inside the S integral is assumed. Localization to a
dyadic interval before applying (2) is essential: it gives the factor
integral_T^(2T) u^(-2) du=1/(2T).

The full count correction obeys

    |tau integral_T^(2T) q(u)f(u)/u du|
       <=tau/150 * integral_T^(2T) u^(-2) du
       =tau/(300T)<=1/150.                             (11)

Inserting (7), (9)--(11) into the exact (8) proves the big-O statement
in (4). Since log log(2T) is asymptotic to log log T,

    sup_{T<=tau<=2T} |Z(T,tau)|/(T log T)
      <=C_1 sqrt(log log(2T))/log T + C_2/T ->0,         (12)

with absolute constants and one absolute sufficiently large onset.
This proves the required uniform little-o, not merely a typical-height
or averaged-tau assertion.

For completeness write a=T, b=2T and let H be the sum with full weights
on a<gamma<b and half weights at a,b. The strict sum, closed sum and
half-weight sum are, respectively,

    sum_{a<gamma<b} f(gamma) = Z-m(b)f(b),
    sum_{a<=gamma<=b} f(gamma) = Z+m(a)f(a),
    H = Z+(m(a)/2)f(a)-(m(b)/2)f(b).                   (13)

Similarly the [a,b) sum equals Z+m(a)f(a)-m(b)f(b).
Every correction is O(log T) by (3), including separate zeros with
coincident ordinates. These formulas explicitly relate strict, inclusive
and averaged endpoint choices. No simplicity, RH, Lindelof hypothesis,
typical endpoint or zero-free region has entered the argument.

The continuation threshold is met: every error in (8) is uniformly
below T log T. Future use in a signed Xi witness must still justify
its beta weights, any shorter interval, analytic costs and sign margin;
(4) alone pays none of those independently unresolved requirements.
The bounded independent audit below verifies this specialization under
its cited inputs. It is not a candidate solution to RH.

### Critical audit — 2026-11-04, step 348

The invocation-start SPECIALIZE assessment is
`drafts/literature/2026-11-04-zero-ordinate-selberg-audit.md`.
The verdict is that (4) passes the specified audit. This is local
verification of a known-input specialization, not a new cancellation
theorem beyond the sources checked. The audit reuses the inspected
source statements and their qualifications; it does not independently
verify Selberg's original proof, BPT's full manuscript or Bellotti--Wong's
computations. No additional mathematical premise is introduced.

**Normalization and orders.** The saved BPT Section 2/Lemma 2 evidence
uses the half-endpoint total strip count, the stated path branch for S,
and the constant 7/8 inside M. Consequently its correction is exactly
q=N_*-M-S, with the bound in (1), not N_+-M-S. The extension at a zero
height is the averaged convention recorded in the source evidence.
Hence (6) has the plus sign before m/2. L467's conclusion applies to
the entire closed interval [u,u+1], so its subset at u gives (3), with
all orders and all distinct zeros sharing that ordinate. Its prior
critical audit establishes that no generic-height restriction remains.
Von Mangoldt's pointwise bound, including averaged endpoint values,
therefore bounds (7); the endpoint mass has not been absorbed into q.

**Exact identity at arbitrary endpoints.** Let a=T and b=2T. For an
individual count atom of unit mass, its contribution to
[f N_+]_a^b-integral_a^b N_+(u)f'(u)du is as follows. If gamma<=a,
it is f(b)-f(a)-integral_a^b f'=0, including gamma=a. If a<gamma<b,
it is f(b)-integral_gamma^b f'=f(gamma). If gamma=b, it is f(b),
since the indicator is zero almost everywhere in the integral. If
gamma>b, it is zero. Multiplying each case by its order and summing
over the finite count up to b proves the asserted half-open identity.
Subtracting the ordinary integration-by-parts identity for M gives
(5), with a plus sign on i tau integral R f/u because f'=-i tau f/u.
Local bounded variation suffices. No convergence of an infinite
Stieltjes sum or contour passage is involved.

The equality R=S+q fails precisely by m/2 at ordinates, but these form
a finite set on [a,b]. Thus substituting R=S+q in the Lebesgue integral
in (5) is legitimate, while leaving both endpoint values of R intact.
The constant 7/8 contributes [7f/8]_a^b-integral_a^b (7/8)f'=0;
it introduces no omitted term into (8).

**Smooth term and correction.** Put alpha=1-i tau and
L(u)=log(u/(2pi)). Differentiating
u^alpha(L(u)-1/alpha)/(2pi alpha) gives
u^(alpha-1)((L(u)-1/alpha)+1/alpha)/(2pi)=f(u)L(u)/(2pi).
This verifies the displayed primitive without a branch ambiguity,
since u>0 and log u is real. At a,b, the inequalities
|alpha|>=tau>=T, 0<=L(u)<=log(2T), and a+b=3T prove exactly (9).
The bound on q gives tau/(150) times 1/(2T)=tau/(300T);
tau<=2T proves (11), including its constant 1/150. No derivative
estimate for q or cancellation in that term is required.

**Moment and uniformity.** The inspected unconditional Selberg
restatement has S normalized by 1/pi, exactly as in (1). Its
asymptotic implies an absolute upper bound C X log log X beyond one
absolute onset. Positivity gives
integral_T^(2T)|S|^2<=integral_0^(2T)|S|^2<=2C T log log(2T);
there is no subtraction of two uncontrolled asymptotic errors.
Cauchy--Schwarz with |f|=1 and
integral_T^(2T)u^(-2)du=1/(2T) yields (10) as written, and the only
remaining tau factor is bounded by 2T. Combining this with (7), (9)
and (11) proves (12) for the supremum over the whole band.
Both sqrt(log log(2T))/log T and 1/T tend to zero. All constants and
the common sufficiently large onset are independent of tau and of
whether T or 2T is an ordinate. No explicit numerical onset is claimed.

**Endpoint conventions and scope.** Starting from the verified (a,b]
sum, removing its b atoms gives the strict sum; adding its a atoms
gives the closed sum. Taking half of each endpoint mass gives the
third formula in (13); doing both full changes gives [a,b). Thus all
four displayed correction signs are correct, with O(log T) cost by
L467, uniformly and with multiplicities. The direct local input remains
L467; the proof uses no extra local lemma beyond that DAG edge.
The audit meets its continuation test only for this scalar dyadic
input. Beta-dependent weights, shorter windows, witness costs and
actual-Xi signs remain unresolved. Neither RH nor a candidate RH
argument follows from the audit.

## Mathlib

Full matching coverage for (4), Selberg's moment and the exact
multiplicity/endpoint conventions has not been checked. No assertion
of absence is made. Partial summation, integration by parts and
Cauchy--Schwarz are standard supporting tools, not substitutes for a
formal theorem covering the analytic number-theory inputs.
