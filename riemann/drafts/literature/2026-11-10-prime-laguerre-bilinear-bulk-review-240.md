# Degree-averaged prime-Laguerre bulk — completed source comparison

TARGET: Assess Vaughan-type bilinear estimates for the compensated degree-averaged Laguerre block exp(n)<m<=exp(2*n), seeking every-epsilon one-sided subexponential control without RH.
CHECKED: 2026-11-10
DECISION: EXPLORE
SEARCH_EVIDENCE: Step241 searched Vaughan/nonlinear-phase Type I/II estimates, logarithmic phases and exact Laguerre/von-Mangoldt/bilinear combinations; checked the named local averaging, lobe and criterion stops. No inspected theorem supplies this compensated block bound; this bounded search establishes no novelty or general impossibility.
SOURCE_EVIDENCE: Inspected Tao arXiv1201.6656v4 Lemma4.11/(4.18)-(4.19), pp23-24 and proof; Theorem1.3/(1.7)-(1.12), pp4-5 and the Type II separation case (5.19)-(5.22), p29. Inspected Tao 254A Notes5 (7 February2015), Theorem2/(3), Proposition6 and complete proof, Proposition7; Robert author preprint2015, Theorem1 and proof Sections3.1-3.2, pp5-6. Reuse review231/review233's DLMF contracts; inspected live DLMF18.15.17-20 and10.17.2-3/10.17(iii). Precise scope and unread leads below.
COMPARISON: A primary Vaughan variant handles arbitrary finitely supported weights, but its explicit minor-arc estimate uses a fixed additive frequency and a particular cutoff. General derivative estimates have explicit phase-scale hypotheses; neither an applicable gain for this logarithmic Laguerre weight nor compensation control has been established. The sources justify a bounded phase-and-loss test, not payment of B_n.
GAP: Compute the exact degree-sum specialization, phase scales on dyadic factors and differenced Type II phases, and available versus required gains, retaining compensation and fixed-order errors. The full block bound and its complementary logarithmic ranges in A_n(X_n) are unpaid.
REASON: Essential tools for one phase-range obstruction test are now accessible; no further general search is needed before that test. Its separate nomination requires next-turn approval. No arithmetic estimate, new lemma or mathematical script is established in this literature turn.
LITERATURE_REASON: The start-of-turn assessment was REVIEW_REQUIRED; primary arbitrary-weight Vaughan and n-dependent derivative-range contracts lay outside the reused averaging/lobe assessments.
SCOPE: Actual Lambda, every integer n>=2, full right endpoint and excluded left endpoint, K_n(u)=(n-1)^(-1)*sum_(k=2)^n L_(k-1)^(1)(u), and B_n defined below. No RH, prime-only replacement, simple-zero premise, uniform fixed-index limit or unexplained removal of a remainder.

The nomination below is preserved as step240's historical proposal.
Its missing-source language is superseded by the step241 comparison
at the end; it is not a claim that the block has been bounded.

## Exact proposed test and downstream use

Define the finite block to be assessed, without asserting any bound:

    B_n=sum_(exp(n)<m<=exp(2*n)) Lambda(m)*K_n(log m)/m
                         -integral_n^(2*n) K_n(u) du.

The proposed threshold is: for every epsilon>0 there is a finite
C_epsilon>=0, independent of n, with B_n<=C_epsilon*exp(epsilon*n)
for all n>=2. An eventual estimate may include a rigorously handled
finite prefix. A two-sided estimate would suffice, but is not assumed.
Every prime power and the compensating integral are part of the test.

This is one interior block of the arithmetic average in L984's unpaid
(H). Its plausible use is to pay an oscillatory portion of that
average by actual arithmetic cancellation. The portions with log m
at most n or above 2*n up to log X_n, including their matching
integrals, remain independent gaps. The remote Cauchy tail in L981
does not pay those portions. A result on B_n alone would not prove
(H), RH or actual-Xi positivity. L984, L981 and L982 supply context
and the precise eventual interface, not a bound on this new block.

## Comparison of three mechanisms and selection

1. Automatic degree smoothing: the step235 stop preserves the unpaid
   two-sided threshold through an exact inverse. The accepted L984
   audit proves only one-sided sufficiency. Another criterion or
   automatic-smoothing claim gives no new payment; park this route.
2. Universal spatial lobe signs: L983's positive actual-prime pair
   refutes the nonpositive-pair rule. Repeating that rule or collecting
   more signs does not pay a growing block; preserve this stop.
3. Arithmetic bilinear decomposition: select a source comparison of
   Vaughan-type Type I/II estimates applied to this fixed family of
   compensated blocks. It uses multiplicative structure of Lambda
   rather than an assumed lobe sign or a sequence-averaging inverse.
   Applicability and a sufficient gain are questions, not conclusions.

The source review should first inspect exact identity hypotheses and
theorem ranges for the relevant weighted exponential sums. Compare
them with the primary Laguerre asymptotics only where their scaled
uniformity actually covers u in [n,2*n]. In particular determine
whether the phase varies sufficiently on the dyadic factor ranges;
the label "oscillatory" alone supplies no cancellation. Retain Type I,
Type II, any remaining terms, compensation and boundary errors.

Continue to a separate bounded mathematical attempt only if a concrete
applicable inequality or phase-range obstruction can be tested with
explicit required versus available gains. Abandon this payment
mechanism if its hypotheses assume RH-sized input, if its phase ranges
do not apply, or if the complete bound still has a fixed positive
exponential rate with no identified way to remove it. An informative
obstruction may justify one covered test, not a claim that all prime
cancellation is impossible. Do not reopen the parked Coffey, original
1999 or kenan source-access routes without a new essential reason.

No new identity, inequality, lemma or mathematical script for this
block is established in step240. No creative proof attempt is yet
justified: the missing arithmetic gain is the specific blocker.
If the source review produces a viable new central mechanism, its
later proof_attempt/creative nomination must state that gain, the
bounded test and its decisive evidence in NEXT_ESCALATION. Full
matching Mathlib coverage is unchecked and unknown.

## Completed comparison — step241, 10 November 2026

The main gap and the exact B_n threshold above are unchanged. This
step supplies source coverage, not a new inequality. L981's tail,
L982's fixed-degree identification and L984's hypothesis/conclusion
were read for definitions and scope only. Reused review231's variance
and lobe comparison and review233's connection-formula assessment.
The step235 automatic-average and step240 criterion-only stops were
read; the recorded L983 positive pair remains a contrast, not an input
for bilinear cancellation. No cross-notebook result is used.

### Primary arithmetic contract and its limitation

T. Tao, *Every odd number greater than 1 is the sum of at most five
primes*, [arXiv1201.6656v4, 3 July2012](https://arxiv.org/pdf/1201.6656v4),
Lemma4.11 and proof, pp23-24, permits any complex F on the integers
supported strictly inside (V, U*V^2), U,V>1. It bounds the Mangoldt sum
by Type I terms with d<=U*V and Type II terms with d>U,w>V;
|c_d|<=1 and g(w)=sum_(b|w,b>V) Lambda(b)-(log w)/2,
|g(w)|<=(log w)/2. Equation(4.18) retains Lambda restricted to <=V;
support, rather than an estimate, removes that term.

Theorem1.3, pp4-5, concerns S_(eta0,q0)(x,alpha), x>10^20,
4alpha=a/q+beta, (a,q)=1, 100<=q<=x/100, |beta|<=q^(-2),
prime factors of q0<=sqrt(x). Here eta0(t)=4(log2-|log(2t)|)_+.
Its(1.9) is

    |S| <= (.14*x/sqrt(q)+.64*sqrt(x*q)+.15*x^(4/5))
                                      *log(x)*(log(x)+11.3).

Inspected the differing q cases(1.10)-(1.12) and Type II proof
(5.19)-(5.22), p29: rational separation of 4jalpha is essential.
No varying-frequency or arbitrary-cutoff version of this estimate
is imported. The algebraic lemma needs no reproof.

For our target, applying the arbitrary-F lemma would require an
explicit choice with V below the first retained integer and U*V^2
strictly above the last. A discontinuous cutoff is permitted there;
it is not thereby permitted in the explicit eta0 bound at its stated
constants. Every prime power remains in Lambda. An estimate for the
uncentered prime sum is also not an estimate for its compensated
difference: the integral must be accounted for on the same interval.
These are applicability conditions, not a decomposition performed here.

### Phase-scale tools, not a prime discrepancy theorem

T. Tao, [*254A, Notes5*, 7 February2015](https://terrytao.wordpress.com/2015/02/07/254a-notes-5-bounding-exponential-sums-and-the-zeta-function/),
Proposition6: on an interval of length at most N>=1, a smooth real
phase with T/(A*N^j)<=|f^(j)|<=A*T/N^j, j=1,2, A>=1,
T>0 and T<=N/(2A), has normalized sum O(A^3/T).
Read its full summation-by-parts proof, including the endpoint deletion.
Theorem2 instead assumes 2<=N<<T and all derivative bounds(3);
it cannot be invoked merely because a phase is nonlinear.
Proposition7 supplies differencing with 1<=H<=N and the shortened
intersection interval. These are unweighted integer-sum tools;
coefficients and amplitude variation still need handling.

O. Robert, *On van der Corput's k-th derivative test for exponential
sums*, [author preprint marked2015](https://perso.univ-st-etienne.fr/rool6510/robert-2015-indag.pdf),
Theorem1, p5: for fixed a>=1, M>=1 integer, lambda>0 and real
C^2 f on [1,M] with lambda<=|f''|<=a*lambda,

    |sum_(m=1)^M exp(2*pi*i*f(m))|
                      <=C(a)*(M*sqrt(lambda)+1/sqrt(lambda)).

Read Sections3.1-3.2, pp5-6: the lambda>=1 trivial case,
replacement by -f, Poisson endpoint convention and concluding
derivative-range count. This supplies a uniform second-derivative
test; it does not assert cancellation at arbitrarily small curvature.
Only these stated tools are proposed for specialization, without reproof.

### Laguerre scope and error obligations

Reuse [review233](2026-11-10-prime-laguerre-degree-average-review-233.md)'s
inspected [DLMF18.18.18](https://dlmf.nist.gov/18.18.E18), with
alpha=1,beta=2, for the future finite degree-sum substitution.
Degree zero is omitted in K_n and must be removed explicitly.
For the resulting degree d=n-1, parameter2 is fixed;
[DLMF18.15.17-20](https://dlmf.nist.gov/18.15.E19) uses
nu=4d+2alpha+2, t=u/nu and
xi(t)=(sqrt(t-t^2)+arcsin(sqrt(t)))/2.
Its Bessel argument is nu*xi(t), its prefactor contains exp(u/2),
and its additive remainder is an envelope bound with fixed
truncation order. Reuse the inspected fixed-delta uniformity in
[the scaled-asymptotic assessment](2026-11-05-theta-laguerre-uniform-oscillatory-localization.md),
equations18.15.17-20; the new source page was checked directly.
The compact-argument formula18.15.14 does not cover u in [n,2n].

[DLMF10.17.2-3 and(iii)](https://dlmf.nist.gov/10.17) gives fixed-order
J_a(z)'s cosine/sine expansion with phase z-a*pi/2-pi/4,
and real z>0 remainder conditions. Fixed a=2,3 is within scope.
These are additive errors, not relative errors near cosine zeros.
Do not differentiate the Laguerre remainder or let its truncation
order grow with n without another source. No actual-prime asymptotic,
integrated error bound or exponential-rate comparison is derived here.

### Search record, exclusions and decision

Queries included `Vaughan identity exponential sums primes nonlinear
phase derivative Type I Type II logarithm`, `Vaughan exponential sums
primes alpha x bound N 4/5 theorem lecture notes`, `Laguerre polynomials
log n von Mangoldt bilinear sums`, `Vaughan logarithmic phase`,
`Laguerre Vaughan primes`, and exact `Laguerre von Mangoldt exponential`
combinations. Scoped local searches covered the 10 November
prime-Laguerre assessments and named ATTEMPTS. No adequate matching
compensated-block theorem was inspected; a failed search establishes
neither novelty nor absence from the literature.

Kumchev's [author-hosted survey](https://tigerweb.towson.edu/akumchev/a35.pdf),
Section1.1/(7), pp3-4, confirms the standard Type I/II ranges, but
explicitly treats the cancellation estimates as black boxes. It is
orientation only; use Tao's primary arbitrary-weight lemma instead.
Granville's [*An alternative to Vaughan's identity*](https://dms.umontreal.ca/~andrew/PDF/RevisedVaughanId.pdf),
Section4/Proposition1, p3, was partially read. Its displayed inequality
was not reliably extracted, so no constants or theorem are imported.
PDF screenshot calls returned no inspectable image; direct shell
download failed DNS resolution. This is not an essential source
blocker because the inspected Tao lemma supplies the needed contract.
Search hits for newer linear-frequency bounds and the parked kenan
route were not inspected or used; a sharper additive-frequency
exponent would still require a justified transfer to our weight.

Decision: no direct arithmetic payment is ready. Prepare exactly one
phase-range/loss test using the covered tools, with all hypotheses
and all remaining terms visible. This is ordinary specialization and
an obstruction test, not yet a creative central mechanism. A justified
creative attempt still lacks an identified gain for the compensated
sum. The separately nominated continuation is
[review241](2026-11-10-prime-laguerre-bulk-phase-test-review-241.md).
It must receive separate approval before execution. Full matching
Mathlib coverage is unchecked and unknown. No change to the proof
argument, DAG, lemmas or mathematical scripts is made.
