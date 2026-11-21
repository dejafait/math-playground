# Corollary C033o: exact capped signed Laplace support

## Hypotheses

Let W=[1,2], let f:W -> R be continuous, and set

    A_2={eta : eta finite real signed Borel on W,
               eta(W)=1, |eta|(W)<=2}.

All Borel measures in this class are allowed, including atoms,
singular continuous parts and infinite support. No positivity of eta,
moment, cancellation or density condition is imposed. Put

    M=max_(sigma in W) f(sigma), m=min_(sigma in W) f(sigma).

For the qualified finite Laplace application, take exactly C033l's
probability kernel, signed laws and normalization, and let

    f(sigma)=sum_(j=1)^n b_j*k_(q_j)(sigma),
    k_q(sigma)=exp(-B_sigma(q)), n>=1, b_j real, q_j>0.

Here C033l supplies reality and continuity on the closed W. Keep its
actual-divisor/conjugation/multiplicity conventions, excluded ordinate
zero, strip |beta-1/2|<1/2, first-zero bound gamma>14, counting
N(T)=O(T log(T+2)), verified zeros through height 100, retained real
zero in (14,15), heat positivity, both fixed-v1 preprint inputs and
Gaussian half-variance convention. Its C033i/j residual and separate
j=0,1 C032s heat-error qualifications remain when interpreting a
separator against that residual. Neither those imports nor finite-zero
data are independently verified here. They are unnecessary for the
abstract continuous-function identity itself.

## Conclusion

The support value over the entire class is

    sup_(eta in A_2) integral_W f deta = (3*M-m)/2.          (1)

It is attained. If M>m, choose any maximizer sigma_+ and minimizer
sigma_- of f. Then an attaining measure is

    eta_*=(3/2)*delta_(sigma_+) - (1/2)*delta_(sigma_-),     (2)

with mass one and total variation two. If M=m=c, every eta in A_2
has payoff c; in particular eta_*=delta_1 attains (1) with total
variation one. Thus no saturation assumption is needed for constants.

For the finite Laplace application, (1) evaluates exactly the signed
support functional occurring in C033l and C033n. It identifies which
two continuum extrema must be controlled; it does not compute them,
construct separator data or certify a numerical gap. This is a routine
specialization of known Jordan/variation tools, with no claim of
progress beyond the inspected source results. Uncapped variation,
full odd cancellation, moments and actual-Xi realization remain open.

## Proof

### Imported theorem and reason for specialization

Reuse SPECIALIZE assessment1760 and source-notes1760, available before
this calculation. Import Richard F. Bass, *Signed measures*, Chapter 12,
version 4 November 2011,
[Theorem 12.8 and (12.1), printed p.97](https://webspace.science.uu.nl/~kraai101/SignedMEasures):
on a measurable space a signed measure has mutually singular positive
Jordan parts eta^+, eta^- with eta=eta^+-eta^- and
|eta|=eta^++eta^-. Finite variation makes both parts finite. This
includes every measure in A_2; no support or absolute-continuity
restriction is involved. The bounded signed integration and variation
inequality already used in C032q apply here. The standard named extreme
value theorem supplies finite attained M and m because W is nonempty
and compact and f is real continuous. No effective extremum theorem
is used.

These results are imported, not reproved. The remaining calculation
imposes the two simultaneous scalar constraints and proves attainment;
the assessed sources did not supply this exact joint-constraint formula.

### Upper bound for every allowed Borel input

Fix eta in A_2 and write p=eta^+(W), r=eta^-(W). Both are finite
and nonnegative. The mass and cap give

    p-r=1, p+r<=2,
    p=1+r, 0<=r<=1/2.                                   (3)

The integrals of f against both positive parts are finite because f
is bounded. Positivity of integration and m<=f<=M give

    integral_W f deta
      =integral_W f deta^+ - integral_W f deta^-
      <=p*M-r*m
      =M+r*(M-m)
      <=M+(M-m)/2=(3*M-m)/2.                             (4)

Neither sign of M or m matters: the first inequality integrates f<=M
against eta^+ and f>=m against eta^- separately. The last inequality
uses M-m>=0 and (3), not an assumption that the cap is saturated.
This proves the upper bound for arbitrary finite signed Borel eta,
including nonsaturated, nonatomic and infinite-support inputs.

### Feasible attainment and the degenerate case

If M>m, extremizers sigma_+ and sigma_- exist and are distinct,
since one point cannot have both unequal function values. Their
singletons are disjoint Borel sets. Consequently the two positive
atomic measures in (2) are mutually singular and are its Jordan
parts by the imported uniqueness theorem. Direct evaluation gives

    eta_*(W)=3/2-1/2=1,
    |eta_*|(W)=3/2+1/2=2,
    integral_W f deta_*=(3*M-m)/2.

Thus eta_* is feasible and matches (4). Finite atomic attainment is
an output of the calculation, not a restriction on the input class.

If M=m=c, the inequalities m<=f<=M force f identically c. For every
eta in A_2, bounded signed integration gives

    integral_W f deta=c*eta(W)=c=(3*c-c)/2.

The measure delta_1 has mass one, variation one and payoff c. This
avoids treating coincident extremizers as two nonzero mutually
singular Jordan parts, and proves (1) in the constant case as well.

### Qualified Laplace interpretation and remaining gap

For the finite Laplace payoff, each k_(q_j) is real continuous on all
of W by C033l, so the abstract result applies without any restriction
on signs or repeated arguments in the finite data. Define the bounded
real function h(u)=sum_j b_j*exp(-q_j*u) on X=[0,infinity).
Its absolute value is at most sum_j |b_j|. C032q's bounded integration
identity and finite linearity give, for every eta in A_2,

    integral_X h dnu_eta=integral_W f deta.

Thus the same exact value and the same feasible attainer apply to
the signed-output expression. The output law is not asserted positive.
No unbounded integration, derivative, moment, interchange of infinite
sums, width grid, or condition J_eta=0 has entered the proof.

In particular existence of M,m does not provide their numerical
values or an algorithm with useful runtime. There is no actual
separator vector, certified continuum extremum or coefficient-amplified
margin in this calculation. Stops1571 and 1576 are preserved; neither
their coarse boxes nor their literal evaluator has been retried.
The result makes no claim about RH or actual-Xi all-degree positivity.
Application audit1763 below passes under the unchanged hypotheses.

### Application audit1763 — 19 November 2026

Verdict: the full-class support identity, attainment and qualified
finite Laplace application pass the saved SPECIALIZE assessment1761,
separately approved1762. No correction or additional hypothesis is
required. This verifies a local specialization of the cited Jordan
and integration tools, not a result beyond the inspected sources.
The source extraction in source-notes1760 is reused; it does not
independently certify the inherited preprints or finite-zero data.

1. **Entire input class and existence of extrema.** Bass Theorem12.8
   and (12.1), in the version and page cited above, apply on the Borel
   measurable space W to every allowed eta. Finite total variation
   makes both Jordan parts finite. No regularity, density or support
   reduction is necessary. The extreme value theorem applies because
   W is nonempty compact and f is real continuous, so m and M are
   finite and attained. Boundedness makes every integral in (4)
   integrable against both Jordan parts.

2. **Mass constraint, nonsaturation and negative extrema.** The two
   equalities p-r=1 and |eta|(W)=p+r imply p=1+r and
   0<=r<=1/2. Integrating f<=M against eta^+ gives at most pM;
   integrating f>=m against eta^- gives at least rm. Subtraction
   therefore has the orientation in (4), even when M and m are
   negative. Its final inequality uses only r<=1/2 and M-m>=0.
   In particular a measure with r=0 or any intermediate variation
   was included, rather than replaced by a saturated input.

3. **Attainment and constants.** If M>m, any selected maximum and
   minimum occur at different points. Their Borel singletons witness
   mutual singularity of the two positive atoms in (2); Jordan
   uniqueness then gives variation exactly 3/2+1/2=2. Their mass is
   one and their integral is exactly the upper bound. If M=m=c,
   f is identically c, and the integral for every eta is c*eta(W)=c.
   Delta_1 is feasible with variation one. There is no claim that
   coincident atoms of weights 3/2 and 1/2 are Jordan parts. Zero
   payoffs, negative constants and all-zero Laplace coefficients are
   covered by this same constant case.

4. **Finite Laplace interface.** C033l's continuous-coordinate proof
   identifies k_q(sigma)=exp(-B_sigma(q)) as real continuous on the
   entire closed width interval for every q>0. For finitely many real
   coefficients, h(u)=sum b_j exp(-q_j u) is real continuous on
   X=[0,infinity) and |h|<=sum |b_j|, including at u=0. C032q
   Conclusion (1) applies to this bounded real Borel h. Probability
   integration and finite linearity give Th=sum b_j k_(q_j)=f,
   hence the claimed equality of the two payoffs for every eta.
   The atomic attainer is in that same class, so it also attains the
   output support. Possible overlap of the positive output measures
   does not matter: C032q requires no output Jordan decomposition
   or positivity. Repeated q_j and coefficients of either sign cause
   no change. There is no infinite sum or unbounded law test here.

5. **Conditional scope and uncomputed quantities.** The abstract
   identity uses neither a zeta zero nor the residual mu. Applying it
   to C033l/n keeps their divisor/conjugation/multiplicity conventions,
   excluded ordinate zero, strict strip, gamma>14, counting bound,
   verified data through100, retained real zero in (14,15), heat
   positivity, both fixed-v1 sources and half-variance normalization.
   Interpretation against C033i's exact residual retains C033j's
   exclusion and C032s's separate j=0,1 heat errors and qualified
   reciprocal-square-tail input. None is reverified by this audit.
   No moment at zero, positivity of the mixed output, full odd
   cancellation or actual-Xi realization follows. Existence of the
   extrema and an attainer supplies neither effective extrema nor a
   finite separator, a computed margin or useful runtime. Stops1571
   and1576 remain intact.

This completes the bounded application audit. The main all-degree
actual-Xi positivity gap remains open.

## Mathlib

Full matching Mathlib coverage of the joint mass/cap support identity
and this qualified Laplace application is unchecked and unknown.
The general Jordan, integration and extremum tools above are cited
as informal mathematical inputs; no formal verification is claimed.
