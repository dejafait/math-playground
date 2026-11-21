# Corollary C033n: rational stability of capped signed Laplace separators

## Hypotheses

Retain exactly C033l's qualified residual probability mu on
X=[0,infinity), probability laws nu_sigma for sigma in W=[1,2],
and real signed width class

    A_2={eta : eta finite real signed Borel on W,
               eta(W)=1, |eta|(W)<=2}.

Thus mu is C033i's width-one residual obtained by removing the Levy
measure on I=[1,3/2], not a fitted or discretized law. Write

    m(s)=integral_X exp(-s*u) dmu(u),
    k_s(sigma)=integral_X exp(-s*u) dnu_sigma(u)
             =exp(-B_sigma(s)), s>0.

The probability kernel and signed law nu_eta are those of C032q;
its bounded Borel integration identity and |nu_eta|(X)<=|eta|(W)
remain in force. In particular k_s is continuous on all of W by
C033l. All width atoms, infinite support and singular parts are
allowed. No positivity of eta or nu_eta is assumed.

Retain C033l's actual divisor, conjugation and multiplicity conventions,
excluded ordinate zero, strip |beta-1/2|<1/2, first-zero bound gamma>14,
counting N(T)=O(T log(T+2)), verified zeros through height 100,
retained real zero in (14,15), heat positivity, both fixed-v1 preprint
inputs and Gaussian half-variance convention. Its C033j/C032s
exclusion and separate j=0,1 heat-error qualifications are inherited.
No source-wide or finite-zero verification is performed here.

Fix any finite data supplied by C033l: n>=1, s_j>0, real a_j not all
zero, and a prescribed epsilon>0 satisfying

    U:=sum_j a_j*m(s_j) >= epsilon+S,
    S:=sup_(eta in A_2) integral_W sum_j a_j*k_(s_j) deta.     (1)

These data and epsilon are mathematical parameters, not computed
quantities. No undamped moment at zero, absence of a zero atom,
full odd cancellation, positivity of p_sigma or actual-Xi realization
is assumed.

## Conclusion

Set the explicit positive tolerances

    A=max_j |a_j|>0,
    tau=min{epsilon/(12*n), A/2},
    d_j=min{s_j/2, epsilon*s_j/(24*n*(1+|a_j|))}.             (2)

For any real q_j,b_j with

    |q_j-s_j|<=d_j,    |b_j-a_j|<=tau,                       (3)

one has q_j>=s_j/2>0 and b not identically zero. Define

    U'=sum_j b_j*m(q_j),
    S'=sup_(eta in A_2) integral_W sum_j b_j*k_(q_j) deta,
    D=sum_j [|b_j-a_j|+(2*|a_j|/s_j)*|q_j-s_j|].             (4)

Then all suprema in (1),(4) are finite and

    D<=epsilon/6,    |U'-U|<=D,    |S'-S|<=2*D,
    U'-S'>=epsilon-3*D>=epsilon/2.                           (5)

In particular the q_j may all be chosen positive rational and the
b_j may all be chosen nonzero rational. This gives a rational finite
Laplace separator retaining at least half the prescribed gap, over
the entire signed class A_2. It controls both separator sides; no
finite width grid or positive-width replacement is made.

This is a quantitative specialization of known regularity and signed
integration tools, not a novelty claim. The budget is explicit in the
given real data. It does not compute those data or their gap, evaluate
the signed support value, prove search termination or useful runtime,
or produce an executed numerical certificate. C033m's rational-input
residual evaluator is a possible downstream use only. Uncapped
variation, moments, cancellation and actual-Xi signs remain open.
The proof was completed on 19 November 2026. Separate application
audit1759 below passes under the unchanged qualified hypotheses.

## Proof

### Imported positive-argument regularity and its applicability

Reuse assessment1756 and its source-notes1756. Import Ante Mimica,
*Laplace transform*, Dresden course, 27 April-1 May 2015,
[Remark 1.2(i) and Proposition 1.4(i)-(ii), printed pp.5-7](https://web.math.pmf.unizg.hr/~amimica/lt.pdf).
For a positive measure rho on X whose Laplace transform is finite
at every positive argument, Proposition 1.4(i) gives smoothness there
and, in particular,

    (Lrho)'(r)=-integral_X u*exp(-r*u) drho(u), r>0.          (6)

The moment assertion at zero in part (ii) is not a hypothesis for
(6). The positive probability measures mu and each nu_sigma have
transforms bounded by 1 at every positive argument, so (6) applies
to each separately. We do not differentiate a signed width mixture
or reprove the general differentiation theorem. The local work is
the finite-data, uniform signed error propagation absent from that
source. The mean value theorem and density of the rationals are
the other standard named tools used below.

### A modulus uniform over all the probability laws

For r>=s_j/2 and u>=0 one has u*exp(-r*u)<=1/r<=2/s_j:
indeed, putting x=r*u, x*exp(-x)<=1 follows from exp(x)>=x
for x>=0. Since rho is a probability, (6) therefore gives

    |(Lrho)'(r)|<=2/s_j, r>=s_j/2.                          (7)

This bound is independent of rho; it applies both to mu and to every
nu_sigma with the same constant. By (2),(3), the closed interval
joining s_j and q_j lies in [s_j/2,infinity). The mean value theorem
and (7) yield

    |Lrho(q_j)-Lrho(s_j)|<=(2/s_j)*|q_j-s_j|.               (8)

Also 0<=Lrho(q_j)<=1. Splitting the coefficient perturbation as

    b_j*Lrho(q_j)-a_j*Lrho(s_j)
      =(b_j-a_j)*Lrho(q_j)
        +a_j*(Lrho(q_j)-Lrho(s_j))

and summing the triangle inequalities gives a bound of D for any
such probability rho. Taking rho=mu proves |U'-U|<=D. Taking each
rho=nu_sigma gives the uniform width bound

    sup_(sigma in W) |g(sigma)-f(sigma)|<=D,
    f(sigma)=sum_j a_j*k_(s_j)(sigma),
    g(sigma)=sum_j b_j*k_(q_j)(sigma).                      (9)

Both functions are continuous and bounded on W. No uniform derivative
bound at argument zero is asserted or needed. An atom of rho at
u=0 is retained in its transform and contributes zero to (6).

### Both sides of the full signed supremum

The class A_2 is nonempty, since it contains delta_1. For every
eta in A_2, C032q's bounded integration and variation bound give

    |integral_W (g-f) deta|
      <= |eta|(W)*||g-f||_infinity <=2*D.                   (10)

All these integrals are finite: for example
|integral_W f deta|<=2*sum_j |a_j|, and the corresponding bound
holds with b_j for g. Thus S and S' are real finite numbers.
For each eta, (10) gives integral g deta<=S+2*D; taking its
supremum gives S'<=S+2*D. Reversing f and g gives S<=S'+2*D.
Consequently |S'-S|<=2*D without interchanging a supremum with
an integral or restricting eta's support or sign. Together with
the residual-side bound and (1), this proves

    U'-S'>=(U-D)-(S+2*D)>=epsilon-3*D.                    (11)

C032q also identifies each finite width integral above with the
corresponding bounded test integrated against nu_eta, so (11)
has precisely C033l's signed-output meaning on all of X, including
possible atoms at zero. All integrations are bounded signed integrations; no
positivity of nu_eta or unbounded interchange is used.

### Budget, nonzero coefficients and rational choices

The coefficient contribution satisfies

    sum_j |b_j-a_j|<=n*tau<=epsilon/12.

For each j the argument contribution obeys

    (2*|a_j|/s_j)*|q_j-s_j|
      <=epsilon*|a_j|/(12*n*(1+|a_j|))<=epsilon/(12*n).

Summing proves D<=epsilon/6. Substitution into (11) gives the
required threshold epsilon/2 in (5). If j_* attains A, then

    |b_(j_*)|>=|a_(j_*)|-|b_(j_*)-a_(j_*)|
             >=A-tau>=A/2>0,

so every perturbation satisfying (3) has a nonzero coefficient vector.

All d_j and tau are strictly positive. Rational density allows
q_j in Q with |q_j-s_j|<d_j. Each such q_j is positive because
d_j<=s_j/2. The nonzero rationals are also dense in R, so choose
b_j in Q\{0} with |b_j-a_j|<tau, including when a_j=0. There
are only finitely many independent choices; all simultaneously
satisfy (3). This establishes rational existence with the explicit
stability budget, without requiring a computable representation
of the original real data or a known numerical lower bound on
their existential gap. The proof is complete. ∎

No stronger hypothesis than the approved scope was needed. The
coarse-box failure1571 and literal-evaluator cost stop1576 are
unchanged; neither concerns the finite perturbation statement proved
here. This result does not supply a full signed support formula,
certified continuum extrema, coefficient-amplified numerical gap,
uniformity as the variation cap grows, or a solution of RH.

### Application audit1759 — 19 November 2026

Verdict: the finite perturbation statement passes the exact target of
SPECIALIZE assessment1757, separately approved1758. No correction or
additional hypothesis is required. This independently checks a local
application of known tools; it does not establish a new general theorem,
verify the inherited external inputs, or supply separator data.

1. **Positive neighborhoods, including their boundary.** Every s_j is
   strictly positive and every a_j finite, so both entries defining d_j
   in (2) are positive. From (3), q_j>=s_j-d_j>=s_j/2>0, even when
   equality holds in either tolerance. Every point between s_j and q_j
   has this same lower bound. The finite maximum A is positive because
   a is nonzero; hence tau>0. There is no common lower bound required
   as the given data vary, and no claim about s=0.

2. **Exactly the imported regularity hypotheses.** C033l gives positive
   probability measures mu and each nu_sigma on the whole closed
   half-line. Their transforms are finite, bounded by one, at every
   positive argument. Thus Mimica Proposition1.4(i), in the source
   version and pages cited above, applies separately to each measure.
   For r>=s_j/2 its derivative formula and
   u*exp(-r*u)<=1/r<=2/s_j prove (7). The constant is independent of
   the law and sigma. The mean value theorem on the interval in item1
   proves (8); if q_j=s_j both sides are zero. Part(ii)'s undamped
   moment assertion is unused. A zero atom contributes to the
   transform but contributes zero to its derivative. No derivative of
   a signed mixture, width derivative, or interchange over sigma is
   used.

3. **Coefficient amplification and both probability evaluations.**
   In the displayed splitting before (9), the coefficient error
   multiplies Lrho(q_j), whose absolute value is at most one. The
   argument error multiplies the original |a_j|, so no missing
   |b_j| or product of perturbation errors is present. Taking absolute
   values and summing gives exactly D in (4). With rho=mu this proves
   |U'-U|<=D. With rho=nu_sigma it gives (9) uniformly on the full
   closed width interval. C033l supplies continuity of k_q for every
   positive q, so f and g are bounded continuous real functions on W.

4. **Full signed class and reversed supremum comparison.** A_2 contains
   delta_1. For every eta in this same class, the bounded signed
   integral inequality gives |integral(g-f) deta|<=2D. Finiteness of
   S and S' follows from the respective bounds 2*sum|a_j| and
   2*sum|b_j| and nonemptiness. For each eta,

       integral g deta <= integral f deta+2D <= S+2D,
       integral f deta <= integral g deta+2D <= S'+2D.

   Taking suprema separately gives S'<=S+2D and S<=S'+2D.
   These are both needed for |S'-S|<=2D. No maximizer, positivity,
   atomic approximation, or restriction of support is assumed.
   C032q's bounded Borel identity applies to each finite Laplace
   sum on all of X, so the width integrals have exactly the signed
   output interpretation claimed in (11). Atoms at zero and singular
   parts remain included.

5. **Budget and retained threshold.** Equation(2) gives n*tau<=epsilon/12.
   Its second bound for d_j gives, separately for every j,

       (2|a_j|/s_j)*d_j
         <= epsilon*|a_j|/(12*n*(1+|a_j|))
         <= epsilon/(12*n).

   For a_j=0 the left side is exactly zero. Summing the n bounds
   gives D<=epsilon/12+epsilon/12=epsilon/6. Combining
   U'>=U-D, S'<=S+2D and (1) gives
   U'-S'>=epsilon-3D>=epsilon/2. Thus all three error allowances
   are paid, without an assumption on the size of epsilon or A.

6. **Nonzero and rational choices.** An index attaining the finite
   maximum A satisfies |b_j|>=A-tau>=A/2>0 for every allowed
   perturbation, including tolerance endpoints. For rational
   existence the open intervals of radii d_j and tau are nonempty.
   Rational density supplies positive rational q_j in the first
   intervals; density of Q excluding zero supplies nonzero rational
   b_j in the second, also when a_j=0. Finitely many independent
   choices satisfy (3) simultaneously. This is existence, not a
   procedure to compute unknown real input data or their margin.

The direct mathematical inputs remain C033l and C032q, as already
recorded in the DAG. C033i's probability and C033j/C032s's qualified
exclusion enter through C033l; they are not reproved here. In
particular all divisor, multiplicity, conjugation, excluded-zero,
strip/counting, first-zero/through100/retained-real-zero, heat,
fixed-v1 and half-variance qualifications remain unchanged. No new
edge or change to the assembled RH argument is warranted. Stops1571
and1576 remain scheme-specific evidence. Finite separator data,
signed support evaluation, certified continuum extrema, a numerical
gap, uncapped variation, cancellation, moments and Xi realization
remain unresolved. No numerical script is needed for these universal
finite inequalities.

## Mathlib

Full matching coverage of this qualified rational separator result
has not been checked and remains unknown. Supporting Laplace
differentiation, mean-value, rational-density and signed-integration
APIs have not been inspected in this step. No formal verification
of this proof, its inherited preprint inputs or the finite-zero data
is claimed.
