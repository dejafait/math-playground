# Short-resonator fourth-moment test: completed source comparison

TARGET: Test whether the short polynomial F_T(t)=sum_{n<=floor(T^(1/24))} n^(-1/2-it), through correlation with |F_T|^6, certifies I_4(T)>=c T(log T)^24 for L477's complete residual for all sufficiently large T.
CHECKED: 2026-10-29
DECISION: EXPLORE
SEARCH_EVIDENCE: Bounded exact-residual, short-polynomial lower-moment, Riemann--Siegel, Wronskian/Laguerre and derivative-moment searches on 2026-10-29; read the primary passages below and reused the local interpolation, saddle and finite-summation assessments and both certificate stops. No matching complete-residual theorem was established; no novelty follows.
SOURCE_EVIDENCE: Rudnick--Soundararajan arXiv:math/0502042v1, Theorem and complete proof pp. 2--4; Heap--Soundararajan arXiv:2007.13154v1, Theorem 1 p. 1, Section 5 (14) and its preceding proof p. 9, (16) pp. 10--11 and Section 6 pp. 11--12; Gao arXiv:2108.13116v1, definition and Theorem 1.1 pp. 1--2, comparison only; reuse Gonek (1984) Lemma 2 (24)--(25), p. 130 and Tao's finite cyclic/geometric summation as assessed in 2026-10-29-grouped-residual-cross-term-coverage.md, with L477, audited L479 and audited L480 retained. Direct links and exact applicability are below.
COMPARISON: Known lower-moment methods and finite mean squares support one complete-correlation test; neither the character-family theorem, actual-zeta moment lower bounds nor derivative moments estimate this real chirped residual. The scalar saddle formula covers rational parameters but does not supply the new summed error. L479's four-index result is not coverage for the added six short factors. No conjectural eighth moment is needed merely to attempt the explicit finite calculation.
GAP: Prove the proposed signed correlation lower scale T(log T)^18 and auxiliary eighth-polynomial-moment upper scale T(log T)^16, or an adequate alternative pair, before claiming the requested fourth-moment bound. The logarithmically weighted diagonal, complete chirped rational-phase sum, all sharp cutoffs and both summed endpoint errors remain unproved. The exponent 24 is a test threshold, not an asymptotic or source conclusion.
REASON: Essential method/source comparison is complete for one bounded EXPLORE attempt on the unchanged target, with the signed remainder and error obligations identified below. This review proves no residual estimate. The changed ready assessment requires separate next-turn approval before mathematical invocation; no further generic resonance search is justified for this limited scope.
LITERATURE_REASON: The proposed short arithmetic resonator and lower bound above the necessary fourth-moment scale are outside the inspected full-residual finite-expansion test and require an essential unread lower-moment theorem/method comparison.
SCOPE: Actual L477 R_T and theta on [T,2T], M=floor(sqrt(T/(2 pi))), arbitrary sufficiently large real T, the fixed short cutoff floor(T^(1/24)), and full signed integral of R_T|F_T|^6; no RH, independent phases, conjectural eighth moment, discarded chirped term or weighted use of L477's unweighted transfer error.

## Original nomination (preserved; unread-source status superseded below)

## Relevance and the bounded source decision

The main gap is still actual-Xi all-degree mixed positivity. This
nomination addresses only the viable use of the norm diagnostic, not
an actual-height sign. Audited L480 shows that its second/fourth-moment
interpolation can reach c T(log T)^3 along an unbounded sequence exactly
when I_4<=C T(log T)^18 on that sequence. A uniform eventual lower
bound with a strictly larger logarithmic exponent would therefore stop
this particular interpolation route. It would not decide L477's actual
L1 threshold, prove a negative-mass saving, or refute RH. This downstream
implication is already the audited L480 criterion, not a new result.

The proposed test changes the missing input from a crude supremum-based
upper envelope to a signed correlation with a specified short arithmetic
polynomial. The correlation to assess is

    integral_T^(2T) R_T(t) |F_T(t)|^6 dt.

It must retain both U and Re(exp(2i theta)V) from L480. Neither its sign
nor its size is assumed. The source review must identify the complete
primary hypotheses of a suitable lower-moment resonance argument and
the relevant proof cases, including the norm of the auxiliary weight,
before deriving any exponent specialization. Rudnick--Soundararajan
lower bounds for moments are an unread search lead, not a cited input.
The earlier scalar extreme-value theorem alone does not give the needed
signed correlation or a uniform eventual moment bound for R_T.

Continue to a separately approved mathematical attempt only if the
sources and retained elementary inputs support a concrete calculation
with all remaining signed sums and error thresholds identified. Track
the product lengths after the sixth power, exact coincidences, actual
finite interval, ratio/product cross terms, stationary points and every
cutoff. The Gonek scalar lemma already used in L479 may be reused only
after checking its summed-error scope for the new coefficients; L479's
specific four-index evaluation is not an eight-index theorem.

Abandon this specified correlation certificate if its source comparison
requires an essential conjectural moment or leaves no independently
testable signed remainder; do not repeat generic scalar large-value or
Hardy-space searches as progress. A mere failure of coverage does not
disprove the proposed lower bound. A mathematical failure must identify
the actual obstruction and does not stop other concentration mechanisms.

## Local overlap and stops retained

The [October 11 arithmetic-resonator assessment](2026-10-11-arithmetic-resonator-discriminant.md)
approves only a specific growing Mobius-weighted physical replacement
and tail estimate; it leaves its discriminant carrier and signed total
unresolved. Its Bui--Hall/Young/Bettin--Chandee--Radziwill inputs do not
automatically evaluate this complete residual correlation. Only its
target and approved scope were read here; none of its lemma inputs is
used mathematically in this audit or nomination.

The [October 21 actual-excursion assessment](2026-10-21-width-one-actual-excursion-input.md)
inspected Soundararajan's scalar extreme-value resonance and separate
derivative extrema. They did not supply its joint excursion. That is
a distinct failure, neither coverage nor a ban for the proposed moment
test. No earlier excursion theorem is imported here.

Preserve the [supremum stop](../../ATTEMPTS/2026-10-29-residual-supremum-fourth-moment-certificate.md),
the [coefficientwise stop](../../ATTEMPTS/2026-10-29-full-residual-termwise-moment-certificate.md)
and L319's stationary-involution obstruction. L472/L473's abstract laws
do not give this actual-height correlation. No change of route name,
independent phases, automatic Haar transfer, or component lower bound
substitutes for its signed arithmetic calculation. Full matching
Mathlib coverage is unchecked. No new lemma, script or resonator
estimate has been produced or approved in this nomination.

This is an established-method concentration diagnostic, not yet a
justified creative mechanism for central sign control. The current
blocker for such a creative nomination is a concrete sign-sensitive
actual-height input: neither the audited norms nor the old clipping
and scalar-resonance sources supply one. This review should not be
relabeled creative merely to satisfy a scheduling target.

## Completed comparison, 29 October 2026

### Primary lower-moment method and its limits

**Rudnick--Soundararajan, _Lower bounds for moments of L-functions_,
[arXiv:math/0502042v1](https://arxiv.org/pdf/math/0502042v1),
2 February 2005, Theorem p. 2 and full proof pp. 2--4.**
For fixed natural k and sufficiently large prime q the theorem gives
the lower scale q(log q)^(k^2) for the 2k-th central-value moment over
nonprincipal characters modulo q. Its proof takes x=q^(1/(2k)),
A(chi)=sum_(n<=x)chi(n)/sqrt(n), and compares
S_1=sum L(1/2,chi) A(chi)^(k-1) conjugate(A(chi))^k with
S_2=sum |A(chi)|^(2k) by Holder. Read the truncated divisor
coefficients, the exact diagonal for S_2, and the S_1 congruence
off-diagonal estimate before its positive diagonal restriction.
These are inspected proof cases, not a transfer of character
orthogonality to time. The theorem does not concern R_T, real parts
with theta, or sharp finite-interval stationary phases. Only the
correlation method and the stated fixed-integer divisor-square input
on p. 3 are reusable here. A residual-specific weighted diagonal is
still needed; the ordinary divisor-square asymptotic alone does not
handle log(n/m)^2.

**Heap--Soundararajan, _Lower bounds for moments of zeta and
L-functions revisited_, [arXiv:2007.13154v1](https://arxiv.org/pdf/2007.13154v1),
26 July 2020.** Theorem 1, p. 1, gives dyadic actual-zeta lower
bounds, uniformly for (log T)^(-1/2)<=k<=(log T)^(1/2-delta),
fixed delta>0. Section 6, pp. 11--12, supplies the k>=1
correlation/Holder argument. It does not identify R_T with an
L-function. Section 5, p. 9, (14) and its preceding calculation give,
for any finite complex coefficient sequence,

    integral_T^(2T)|sum_(n<=H) a(n)n^(-it)|^2 dt
       =(T+O(H log H)) sum_(n<=H)|a(n)|^2.

Read the diagonal/off-diagonal expansion and the coefficient-square
bound giving this error. It applies to growing sharp polynomials
when the displayed error is retained. The later factorization (16),
pp. 10--11, additionally assumes coprime supports across distinct
factors. It cannot factor overlapping full-integer short polynomials
or replace their actual finite-time correlation by independent means.
The detailed small-k prime-block estimates are unnecessary here.

**Gao, _Lower bounds for moments of the derivative of the Riemann
zeta function_, [arXiv:2108.13116v1](https://arxiv.org/pdf/2108.13116v1),
30 August 2021, pp. 1--2.** Read I_(k,l)'s definition and
Theorem 1.1: for fixed real k>=0 its conclusion is the lower scale
T(log T)^(k^2+2k) for integral_1^T |zeta'(1/2+it)|^(2k)dt.
This concerns an actual derivative and a different interval, not a
signed determinant residual. No subtraction of cumulative lower
bounds gives a dyadic lower bound. This is an inspected comparison,
not an imported estimate or independent proof audit; no further Gao
proof case is essential to the approved finite-polynomial alternative.

### Analytic and arithmetic coverage reused

The [ready grouped-cross-term assessment](2026-10-29-grouped-residual-cross-term-coverage.md)
already inspected S. M. Gonek, _Mean values of the Riemann
zeta-function and its derivatives_, Invent. Math. 75 (1984),
123--141, [author PDF](https://sas.rochester.edu/mth/people/faculty/gonek-steve/assets/pdf/5-mvzdrvs.pdf),
Lemma 2, p. 130, (24)--(25), with its readable exact formula.
Reuse that scalar statement: fixed real a, large A<B<=2A,
arbitrary real r>0; the saddle indicator is A<r<=B and each
endpoint error has denominator |endpoint-r|+sqrt(endpoint).
The primary text's near-endpoint, interior and far-exterior proof
cases were also inspected in this review. They retain full saddle-size
errors in the endpoint layers. They do not provide an asymptotic
uniformly small relative error at either endpoint. Lemmas 4--5 instead
require a>1 and sum integer parameters; they cannot be applied at
a=1/2 to these rational parameters. L479's normalization is reusable;
its summed four-index error is not. No whole-paper audit is claimed.

The same ready assessment covers finite cyclic orthogonality and
geometric-series summation from Tao, _245C Notes 2: The Fourier
transform_ (6 April 2009), Section 2, Lemma 17 and the finite cyclic
case of Theorem 21 ([primary notes](https://terrytao.wordpress.com/2009/04/06/the-fourier-transform/)).
These allow composite moduli and exact resonances. Abel summation
still requires a bound for the variation of the actual weight on
each actual clipped interval; a logarithmic square is not assumed
monotone across its zero. This is algebraic coverage, not a new
bound for the changing arithmetic sum. No new Shiu, contour-shift
or twisted-zeta-moment input is needed for this finite alternative.

Reuse the [finite-interval interpolation assessment](2026-10-29-l477-residual-moment-interpolation-coverage.md)
and Tao's Lemma 9/Holder proof there. The new method uses the
ordinary Holder dual exponents 4 and 4/3 on dt over [T,2T];
all functions are finite and continuous. There is no independent
need to reprove Holder or a new general mean-square theorem.

### Concrete calculation scope for the next mathematical attempt

The following are calculation obligations, not estimates proved by
this literature turn. Keep the TARGET unchanged. Put N=floor(T^(1/24))
and retain L480's U,V,R_T and the actual theta. Assess

    S(T)=integral_T^(2T)R_T(t)|F_T(t)|^6 dt,
    H(T)=integral_T^(2T)|F_T(t)|^8 dt.

The proposed sufficient scales for the standard Holder certificate are
S(T)>=c T(log T)^18 and H(T)<=C T(log T)^16, with c,C>0
independent of sufficiently large real T. These are unproved
subtargets for the requested fourth-moment exponent, not claimed
specializations of an L-function moment theorem. A different rigorously
established pair can be tested against the unchanged I_4 threshold.

1. **Auxiliary norm and nonchirped correlation.** In the source's
   notation d_j(a;N) counts ordered j-factor products with each
   factor at most N. The finite expansions to verify use F_T^3
   of length N^3 and F_T^4 of length N^4<=T^(1/6).
   The two sides of the nonchirped product have length at most
   M N^3=O(T^(5/8)). Group all equal products before applying
   the finite mean square (or its finite bilinear consequence).
   Source length hypotheses thus leave room for an error test;
   they do not prove the required coefficient bounds. Verify the
   exact diagonal condition n a=m b and its log(n/m)^2 weight,
   where a,b are three-factor short products. An adequate weighted
   diagonal lower bound and all off-diagonal errors must be proved,
   rather than inferred from unweighted d_4^2 or a component moment.

2. **Complete chirped correlation.** Retain the term
   Re integral exp(2i theta(t)) V(t)|F_T(t)|^6 dt.
   Its proposed finite regrouping has phase
   2theta(t)-t log(nm a/b), with n,m<=M and a,b<=N^3,
   coefficients d_3(a;N)d_3(b;N)log(n/m)^2/sqrt(nmab).
   Verify this expansion before use. The numerator product length
   is M^2 N^3=O(T^(9/8)); the denominator bound is N^3<=T^(1/8).
   This is not a polynomial of the short norm's length. The scalar
   saddle parameter to check is r=2pi nm a/b. After normalization,
   the rational phase exp(-2pi i nm a/b), original individual
   cutoffs and T<r<=2T all remain. Track the exact resonances
   b|ma when summing over n and the entire complementary signed
   sum. Composite reduced denominators b/gcd(ma,b), partial
   summation across n=m, empty intervals and nonintegral endpoints
   must be accounted for. Whether those operations give a usable
   signed lower bound is the independently testable remainder;
   neither nonnegativity of the total nor cancellation is assumed.

3. **Uniform summed errors and final certificate.** Recheck the
   actual-theta phase-replacement cost after multiplication by all
   six short factors. Sum both endpoint kernels and the scalar
   remainder over every coefficient, including distant saddles,
   near misses and exact endpoint coincidences. The error sought
   for the proposed correlation scale is o(T(log T)^18), uniformly
   for all sufficiently large real T, together with explicit
   auxiliary coefficient/norm control. A termwise bound failing
   this test is a certificate failure, not a bound on the signed sum.
   Only then specialize Holder and compare the resulting I_4 lower
   exponent with 18 and 24. No new bound is supplied here.

This finite correlation and residue-class calculation is covered for
one bounded attempt under EXPLORE; success is not promised. The
source statements are accessible, and the residual-specific differences
are identified calculation obligations rather than missing essential
theorems. A claimed result must be written and later audited in a
canonical lemma with its full hypotheses and Mathlib qualification.
Full matching Mathlib coverage remains unchecked; it supplies no
assumed estimate.

Continue only with a complete signed estimate capable of dominating
its errors. Stop this specified certificate if the controlled diagonal
and chirped contribution fail the required scale, or if its available
error bounds do not separate them; preserve any finer unresolved
signed sum rather than declare the proposed bound false. A uniform
eventual fourth-moment lower exponent strictly above 18 would obstruct
L480's interpolation route. It would not decide I_1, transfer a weighted
L477 error, prove a negative-mass saving or give an individual-height
sign. L478's termwise, the supremum and L319's stationary-involution
stops remain valid for their original mechanisms.

### Search/access record and classification

Queries included `Rudnick Soundararajan lower bounds moments L functions
simple proof short Dirichlet polynomial`; `Dirichlet polynomial residual
resonator fourth moment`; `lower bounds moments Dirichlet polynomials
derivatives`; `Hardy Wronskian moments zeta`; `log(n/m) moment zeta
polynomial`; `Riemann Siegel polynomial lower bounds moments`;
`Riemann-Siegel resonance moments`; `Dirichlet polynomial Wronskian`;
`zeta moments Laguerre lower`; and the exact Gao title.
Generic scalar extreme-value leads and derivative/zero averages do
not replace this statistic. The existing Bui--Hall fourth-jet and
twisted-fourth-moment comparisons were reused within their assessed
scope, without claiming a matching residual eighth-moment theorem.
No novelty is inferred from these bounded searches.

The primary PDFs above were readable through web extraction. One
shell attempt to fetch Heap--Soundararajan failed DNS; the web reading
sufficed. Gonek screenshot requests returned no inspectable image;
no image verification is claimed. Reuse of the earlier readable exact
scalar-source assessment avoids treating that optional access failure
as an essential blocker. No API key or mathematical script was used.

The completed work is a new source comparison, classified
NOVELTY_UNCHECKED, with outcome EXPLORATION. It establishes no new
residual estimate and spends no mathematical exploration turn. The
next attempt is established-method development, not a creative central
sign mechanism: a concrete sign-sensitive actual-height or tail input
remains absent. Separate approval of this changed ready continuation
must precede its research invocation.
