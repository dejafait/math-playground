# Actual Rice phase transfer: source review1670

19 November2026. Literature-only work on nomination1669's exact target.
No disk inclusion, derivative estimate, nonvanishing result or phase
inequality for the actual integrand is proved in this source review.

## Essential inspected primary material

K. Kawano, *Logarithmic Inequalities of Arbitrary Order for the Riemann
Xi Coefficients*, Preprints.org202611.0383v1, posted4November2026,
DOI10.20944/preprints202611.0383.v1,
[Version1](https://www.preprints.org/manuscript/202611.0383/v1).
Accessed19November2026; the URL redirected to the manuscript page,
which still displayed Version1 and the non-peer-reviewed qualification.
Read Section5.1(25), Section5.2(28)-(30), Lemma5.1's differentiation
paragraph, and AppendixC.1's first paragraph and displayed derivative
bound. The latter fixes Re(p)>=-5 and r>=169995, uses the disk radius
r/(6log r), and claims a second derivative bound for Log(I/S).
Its disk inclusion and logarithm control precede Cauchy's estimate.
Those explicit constants have not been audited here. The hypothesis
Re(p)>=-5 does not cover the proposed curved left boundary. Its final
G-H_0 conclusion also has a different observable. The method is
relevant; neither conclusion directly settles nomination1669.

A. Nagel, *Math722: Complex Analysis*, Spring2012 lecture notes,
[Corollaries3.11--3.12, printed pp10--11, PDF pp10--11](https://people.math.wisc.edu/~nagel/Math722Spring2012.pdf),
accessed19November2026. Read Corollary3.11's derivative formula and
its uniform difference-quotient proof, and the complete Corollary3.12
(Cauchy Estimates). If f is holomorphic on an open set Omega and the
closed disk centered at a of radius R>0 lies in Omega, then

    |f^(n)(a)| <= n! R^(-n) sup_(|z-a|=R) |f(z)|, n>=0.

This is the standard named theorem to import, without a reproof.
The n=1 case is the relevant source tool. A bound at the center or
along a real ray is not its hypothesis. The entire closed circle must
have the required value estimate, and the disk needs an open
holomorphic neighborhood. No applicability to a selected disk for the
present target is asserted here.

NIST DLMF [1.9.30--1.9.31](https://dlmf.nist.gov/1.9#E31),
accessed19November2026, independently states the Cauchy integral and
derivative formulas with continuity on and inside a simple closed
contour, analyticity inside, and the evaluation point inside. These
are supporting coverage; no new derivative theorem is needed.

Also inspected S. G. Krantz, *Complex Variables: A Physical Approach*,
[Section4.1.2(4.2), printed pp94--95, PDF pp109--110](https://jontalle.web.engr.illinois.edu/Public/BOOKS/Kranz-ComplexVariables.pdf),
the complete closed-disk hypothesis, bound and direct Cauchy-formula
proof. It gives the same named estimate; this is corroborating book
coverage, not a second input to be reproved.

NIST DLMF [2.1(ii), differentiation paragraph](https://dlmf.nist.gov/2.1#ii)
states Ritt's theorem: an analytic O(z^nu) estimate in an exterior
sector, for real nu, differentiates to O(z^(nu-1)) in a closed sector
properly interior to it with the same vertex; both symbols may be o.
The section refers to Olver(1997b), pp8--11; that book was not separately
read or imported. This fixed-sector statement supplies methodological
overlap, not the quantitative shrinking-clearance result nominated
here. Use the explicit closed-disk theorem for the later attempt.

## Local scope and remaining specialization

Read C048a's hypotheses, conclusion and continuation/branch setup;
C048j's hypotheses, conclusion, holomorphy and reflection discussion;
and C048m's full proof. These are scope comparisons, not fresh audits.
C048j controls the actual I/S in value in its wider closed sector;
C048a specifies the possible Mellin poles and principal Lambert
neighborhoods. C048m concerns only the explicit S Rice integrand and
states the positive margin1/(30log|p|). Its independent audit remains
separate. No actual-I derivative conclusion is present in those files.

The remaining task is to choose and justify Cauchy neighborhoods
uniformly over the nominated inner sector, including its closed
boundary, put their complete value bounds into the imported theorem,
justify the relevant quotient and all nonzero factors, and compare
the resulting logarithmic-derivative error with the proposed margin.
The shift p=s+1/2 and derivative variable must be retained. These are
unproved obligations for a later mathematical attempt, not results of
this literature turn. The value bound must not be formally
differentiated. A local logarithm, if used, needs its own justification;
it is also possible to formulate the future test directly for I/S-1.

## Bounded discovery, duplicates and recorded failures

External queries actually issued: `Cauchy estimates derivative
holomorphic closed disk theorem complex analysis site:edu pdf`;
`"Logarithmic Inequalities of Arbitrary Order" "C.1"`;
`"Mellin" "Rice" "logarithmic derivative" theta`;
`"Kawano" "I/S" derivative Riemann`;
`"theta" "Mellin" "Rice" phase derivative`; and
`asymptotic expansions differentiation analytic sector Cauchy Ritt
site:dlmf.nist.gov/2.1`. Search snippets were discovery aids only.
The primary passages above were actually read. No inspected result
settled the exact combined actual-I phase threshold. This bounded
comparison establishes no novelty.

Searched C048*.md and the specifically named Mellin/Rice assessments
and histories for Cauchy, I/S, differentiation, actual-I and phase
claims. Reused assessment1662/source-notes1663's primary Rice-saddle
comparisons: the finite-difference examples have different coefficient
functions, and the inspected Li asymptotic assumes GRH. They are not
matching unconditional phase theorems. No repeat import is needed.
The local search found no ready actual-I transfer duplicate; C048a's
Cauchy use concerns theta coefficients, while C048m differentiates S.
Other Mellin derivative hits concerned different observables and were
not treated as matches.

Read stop1665 and stop1657 completely and reused assessment1656's
finite-Rice scope and its source-notes' actual-E/sector comparison.
The first stops the in-region S stationary-point proposal; the second
stops fixed-d absolute vertical opening. Neither asserts failure of
this finite-degree derivative prerequisite. C828b's audited boundary
crossing stop remains in force; the nominated test asks for no
continuation of theta through its boundary.

## Decision and bounded continuation

SPECIALIZE, provisionally REPRODUCTION: import the named Cauchy
estimate and reuse the existing local value and S-phase statements.
The newly inspected differentiation case supplies relevant precedent,
but its narrower hypothesis prevents a direct final-theorem import.
No essential source remains unread for one bounded transfer attempt.
There is no reason to reprove Cauchy's estimate or the Rice theorem.
The only proposed new proof work is the stated neighborhood/domain,
nonvanishing and quantitative error specialization. No uniform disk
radius, error rate or actual-integrand sign has been obtained here.

Continue only if that attempt establishes the claimed1/(60log|p|)
margin uniformly on the entire nominated region for sufficiently large
integer d, with a justified common onset and all factors defined.
An inability to control admissible neighborhoods or the resulting
derivative error must be recorded precisely and parks this transfer
prerequisite; enlarging numerical degrees is not a repair. Even a
successful prerequisite leaves contour direction, amplitude, endpoint
terms, signed total control and a sufficient Xi/height bridge open.

The main gap remains L030--L032/C032a actual-Xi all-degree algebraic
square positivity, with C028b's H_d=o(d), C028g's S_F=0 and the signed
Mellin bridge unpaid. The plausible use is a later nonstationary
cancellation argument, not a sign deduction in this turn. Full matching
Mathlib coverage has not been checked; no absence is inferred.
The completed assessment requires separate next-turn source-scope
approval before mathematics. This transfer remains routine analytic
specialization. No justified source-covered creative signed-Xi
mechanism is ready; the central signed bridge remains its blocker.
