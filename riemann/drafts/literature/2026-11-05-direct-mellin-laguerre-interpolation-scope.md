# Direct Mellin-factor interpolation — completed source comparison

TARGET: Assess direct Laguerre interpolation of the actual gamma-normalized Mellin factor E, and prepare the single necessary-condition test E'(0)^2-E(0)E''(0)>=0 without assuming a q-index or Xi zero count.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step647 inspected Runckel's primary Theorem4 and type(A), Patrick's Theorem1 and its product/limit case, Craven–Csordas Theorem2.4, and the named local scope stops; exact queries and read limits appear below. No actual derivative or sign was evaluated and no novelty is inferred.
SOURCE_EVIDENCE: Runckel Trans.AMS143(1969),343–362, Section3 type(A) p356, Theorem4 p357, proof pp359–360; Patrick Pacific J.Math.44(1973),675–682, (1.1), Theorem1/(2.3)/(2.15), pp675–679; Craven–Csordas JMAA314(2006),109–125, Definition2.1/Theorem2.4 pp112–113; DLMF5.5.5/5.4.13; Johansson arXiv:1802.07942v1 Section2 pp2–3. Exact links and qualifications below; reuse L828/C828a construction only.
COMPARISON: A precise genus-one negative-zero interpolation class supplies a sufficient theorem; the actual factorial interface matches, and the first Laguerre inequality is necessary. Complete-Bernstein exclusion does not itself exclude this class. Integer moment feasibility and universal residual preservers are different hypotheses.
GAP: Actual membership, every global zero/growth assertion and the fixed scalar's certified sign remain unresolved. Source coverage permits preparing one actual-data necessary-condition diagnostic, not importing membership or deriving new mathematics in this turn.
REASON: Essential theorem/growth/limit coverage is now available for a bounded specialization. The source review establishes no actual-Xi sign or advance beyond the inspected results; nominate the fixed calculation for separate approval.
LITERATURE_REASON: Direct entire-factor interpolation and a real-point Laguerre inequality are different hypotheses from finite negative-square recurrence transfer; the latter review supplies no approval for this target.
SCOPE: Completed literature-only step647 for the exact TARGET. The historical nomination below is superseded by the completed comparison. No new theorem, differentiated-Mellin formula, derivative value, membership result, lemma or mathematical script was produced.

## Completed comparison — step647, 5 November 2026

The main gap is actual-Xi all-degree mixed positivity. The intermediate
target is a sufficient class for the specified E, with one necessary
diagnostic to reject an unsuitable class before global membership work.
Continue only with exact class, coefficient and evaluation contracts;
these are now available. A negative certificate would reject the class.
A pass or unresolved interval ends this fixed diagnostic; neither signs Xi.

### Primary sufficient theorem

H.-J. Runckel, *Zeros of entire functions*, Trans. Amer. Math. Soc.
**143** (1969),343–362,
[Section3 type(A) p356; Theorem4 p357; proof pp359–360](https://www.ams.org/tran/1969-143-00/S0002-9947-1969-0252641-X/S0002-9947-1969-0252641-X.pdf),
uses the multiplier function

    G(s)=exp(beta s) product_j (1+s/a_j)exp(-s/a_j),
    beta real, a_j>0, sum_j a_j^(-2)<infinity.

Finite and empty products are allowed. The input is a real entire
f=exp(a z^2)h, a<=0, with h of the stated genus-at-most-one canonical
product type and f having only real zeros or none. Multiplication of
its coefficients by G(n) preserves real zeros. Here the input would be
exp(z), with no zeros. Read the positive-linear-factor logarithmic
derivative argument and scaled finite-product compact limit/Hurwitz
case. No finite exponential-type bound or interpolation-uniqueness
hypothesis is needed in addition to the displayed product. Membership
of actual E is not imported.

This is KPS's reference[52]. Its Section5.2.6 pp416–417 first constructs
the entire reciprocal factor using separation; that preliminary premise
is not assumed here. Craven–Csordas's lead is actually titled *The
Fox–Wright functions and Laguerre multiplier sequences*, JMAA **314**
(2006),109–125,
[Definition2.1 and Theorem2.4, pp112–113](https://math.hawaii.edu/~tom/mathfiles/fox_wright.pdf).
It also covers sampling an LP function with nonpositive zeros, including
a nonpositive quadratic exponent and square-summable reciprocal zeros.
Its (2.7), p113, gives compact Jensen approximation. Runckel's narrower
product suffices here. Mere entireness and real zeros without the growth
or product qualification are not the assessed premise.

### Integer interface: source applicability, not a new lemma

L828 (6), C828a (1)–(2) and L021 fix E, p and the Fourier coefficients.
Legendre duplication, [DLMF5.5.5](https://dlmf.nist.gov/5.5.E5), at
z=n+1/2 gives (2n)!=4^n n! Gamma(n+1/2)/sqrt(pi).
Thus E(n)/n! is exactly M(n)/(M(0)(2n)!), not E(n)/(n!)^2
or an unshifted F(n). The coefficient transform of exp(z), followed
by z=-t^2, has precisely the normalized actual-Xi coefficients.
Before substitution the coefficients are positive; any real zeros
supplied by the theorem would therefore be negative. L021 already
supplies entire convergence for this actual series. A later full
conditional assembly must state the substitution's zero-location
consequence. No Xi-zero premise or recurrence identification is used
in this applicability check.

### Necessary inequality

M. L. Patrick, *Extensions of inequalities of the Laguerre and Turan type*,
Pacific J.Math. **44** (1973),675–682,
[(1.1), Theorem1/(2.3)/(2.15), pp675–679](https://msp.org/pjm/1973/44-2/pjm-v44-n2-p26-s.pdf),
assumes a real canonical product with square-summable reciprocal real
zeros, real linear exponent and nonpositive quadratic exponent. It
gives f'(x)^2-f(x)f''(x)>=0 for every real x. Read its product positivity
and convergent-series proof case, including derivative order zero.
Simple zeros and strictness are not required. The nominated product
class is included, and E(0)=1 is already available from L828 (6).
Hence the one-point inequality is necessary, allowing equality; no
converse from it is asserted. Cardon arXiv:0911.1122v1 Theorem1.1 pp1–2
corroborates this statement; its all-orders converse is not used.

### Duplicate and failure comparison

The narrowly scoped November4–5 literature/attempt searches for E(s),
gamma-normalized Mellin, direct interpolation and the fixed derivative
test found step646's nomination, not a completed actual-E calculation.
Failed searches establish no novelty.

L828 Section2 constructs E without representation assumptions. Its
Section5 additionally uses separated simple zeros and a census obtained
under complete Bernstein membership. Runckel's product does not grant
those premises; C828a's exclusion therefore does not itself decide this
class. No new implication between classes is proved here. Step508's
actual-Xi Levy comparison supplies only conditional ordinary Bernstein
membership. Its persistent supplement blocker is not reopened.
Step637 concerns integer reciprocal-moment measures; L827's feasibility
does not evaluate logarithmic Mellin derivatives or this scalar.
Step407 correctly requires an independently real-rooted input and
factorial conversion: exp(z) supplies the former here, while actual-E
global membership remains unpaid. Universal residual preservation and
common Favard orthogonality are different claims and remain stopped.

### Evaluation contract for a future mathematical turn

Only s=0 and derivatives through order two are nominated. L828 Section2
and C828a Section1 provide Mellin holomorphy and logarithmic domination.
The future step must write out differentiation, reciprocal-gamma formulas
and error propagation; none is derived or evaluated here.
[DLMF5.4.13](https://dlmf.nist.gov/5.4.E13) gives the half-integer
digamma/trigamma constants, not the actual Mellin integrals.

F. Johansson, *Numerical integration in arbitrary-precision ball arithmetic*,
[arXiv:1802.07942v1, 22 February2018, Sections2/2.1 pp2–3](https://arxiv.org/pdf/1802.07942),
provides a finite-segment enclosure contract. Evaluators must enclose
the integrand on the requested balls and, for analytic quadrature,
certify holomorphy on the whole complex neighborhood. Logarithm branch
cuts must be checked. Direct real interval boxes are a fallback;
subdivision limits retain an enclosure, not a tolerance guarantee.
Singular endpoints and infinite tails require separate bounds.

Use the explicit positive theta series on x>=0. Bound the logarithmic
contribution of a small endpoint interval analytically; enclose the
finite middle interval with certified theta-series remainder; and
bound the infinite tail using C828a/L019's superexponential envelope.
Complex quadrature requires uniform kernel-tail bounds on its entire
requested boxes inside |Im x|<pi/4. Save endpoint, series, quadrature,
infinite-tail and roundoff contributions and the full final interval.
Uncertified mpmath values or two-precision agreement do not qualify.
No backend or actual error estimate was verified in this source turn.

Stop at a sound sign certificate or after two declared precision and
subdivision stages. A negative interval excludes the class; a nonnegative
interval passes only this necessary condition; overlap with zero is
inconclusive. A pass or uncertainty authorizes no point/order sweep.
An unavailable rigorous backend warrants a saved analytic reduction
and a blocker report, not an asserted sign.

### Search record and decision

Queries included `Runckel "Zeros of entire functions" "Theorem 4" 1969 pdf`,
`Laguerre theorem entire function negative zeros values integers multiplier
sequence genus one interpolation`, `"Riemann" "Mellin" "Laguerre" "E(s)"`,
`"Laguerre" "gamma" "Mellin" "xi" interpolation`, `"E'(0)" "Mellin"
Laguerre`, `Patrick Extensions inequalities Laguerre Turan type 1973 44
675 pdf`, and `Johansson 2018 numerical integration arbitrary precision
ball arithmetic rigorous Petras analytic pdf`.

Primary hypotheses and essential proof cases were inspected before
larger passages. Craven–Csordas's survey Theorem4.1 p23 was corroboration,
not the sole theorem evidence. Other converse/interpolation discussions
and search-only leads are not imported. A shell download of Runckel
failed DNS; the publisher's needed theorem and proof were accessible
through the web reader, so essential source coverage is not blocked.
Full matching Mathlib coverage is not checked; no absence is inferred.
No cross-notebook input was used.

This review supplies coverage for a known diagnostic, no actual sign
or new mathematical result. The new fixed-test assessment below is
`2026-11-05-direct-mellin-fixed-laguerre-test.md`, awaiting separate
approval. A creative mechanism remains blocked on an independently
payable global class/sign premise; this routine test is not creative.

## Original nomination — retained; review status superseded above

The main gap is actual-Xi all-degree mixed positivity. The intermediate
question is whether an adequately specified Laguerre class for the
actual E provides a sufficient interpolation theorem, and whether its
first Laguerre inequality at the one prescribed point can reject that
class. A surviving sufficient class would offer a direct sign route;
a failed necessary test would park that class before expensive global
membership work. Passing one scalar test proves neither membership
nor RH. It does not justify an automatic point/order sweep.

Use precisely the displayed construction of L828 (6):

    E(s)=sqrt(pi) 4^(-s) M(s)/(M(0) Gamma(s+1/2)),
    M(s)=integral_0^infinity x^(2s) p(x) dx.

C828a fixes p and M(0)=1/2. L828's density-based Taylor subtraction
and gamma cancellation are existing construction inputs; the equality
with a distinguished reciprocal Bernstein-gamma function is conditional
on the representation and must not be used automatically. Verify the
integer-coefficient interface from the actual definitions before any
sufficient theorem is applied. No zero-freeness beyond those definitions
is an assumption licensed by this nomination.

Inspect primary Laguerre interpolation and first Laguerre-inequality
statements, including genus/order, real-axis zeros, signs, and limit
conditions. Useful leads are KPS reference[52], Craven–Csordas,
*Stability, multiplier sequences and the zeros of certain Fox–Wright
functions*, JMAA314(2006),109–125,
https://math.hawaii.edu/~tom/mathfiles/fox_wright.pdf,
and their composition/CZDS survey. These are unread leads for this
target, not theorem evidence. A theorem assuming real zeros of the
resulting Xi transform does not meet the threshold.

Narrowly compare L828/C828a, the actual-Xi Levy assessment, the prior
gamma-reciprocal moment scope, and the recorded exceptional-coefficient
multiplier source limit. Search the active notebook for this precise E
interpolation class and test; do not scan sibling proofs. Distinguish
complete Bernstein exclusion, integer moment-law feasibility, universal
residual preservers and direct interpolation of E. If the proposed
class is already excluded, dominated or equivalent to an unproved Xi
premise, record that exact evidence rather than computing the scalar.

Continue only if an exact sufficient theorem and a justified necessary
fixed-point test survive the comparison with a feasible actual-data
evaluation contract. The intended future mathematical target is only
the sign of E'(0)^2-E(0)E''(0), with certified truncation/tail errors;
no derivative formula or quadrature is derived here. A strict negative
certificate would exclude the nominated class. A nonnegative or
unresolved value ends this fixed diagnostic unless materially new
independent information supplies a discriminating continuation.

This is not yet an approved creative mechanism. A routine known
necessary-condition evaluation must retain that classification; any
later creative attempt needs an independent central claim, bounded
test and NEXT_ESCALATION. No cross-notebook input; matching Mathlib
coverage unchecked.
