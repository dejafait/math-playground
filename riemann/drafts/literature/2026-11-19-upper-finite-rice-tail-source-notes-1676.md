# Upper finite Rice tail: source comparison1676

19 November2026. LITERATURE / literature_comparison / REPRODUCTION.
Review of nomination1675's exact target, retaining c=-1/4,
u_d=d^(2/3)/2, v_d=d/log d, actual F_d=F_d^I, Q_d=F_d'/F_d
and the specified lower-endpoint relative error. This review proves
no estimate for that new range and approves no new mathematical claim.

## Primary theorem comparison for the changed range

P. Flajolet and R. Sedgewick, *Mellin transforms and asymptotics:
Finite differences and Rice's integrals*, Theoretical Computer
Science144(1995),101--124, DOI10.1016/0304-3975(94)00281-M,
[author-hosted final PDF](https://algo.inria.fr/flajolet/Publications/FlSe95.pdf).
Reused notes1656/1660's precise Section2 Lemma1/(6), pp104--105,
finite formula. Refreshed Section4 Theorem2 and both proof cases,
pp110--111: polynomial growth on escaping concentric circles, or
outside a compact subset of a half-plane, licenses the corresponding
closing contours. Neither case supplies this moving finite tail.
Refreshed Section5's entire-function example, p120: the coefficient
function is reciprocal gamma, without the present theta-Mellin factor.
Newly read Section6's opening discussion, pp120--121: reduction of
the Rice kernel to a Mellin kernel is presented as a heuristic whose
direct use can fail through lack of uniformity. It supplies no
degree-uniform replacement for the exact kernel here. Odlyzko and
Szpankowski are references, not newly inspected or essential inputs.
Obscured PDF displays are not used for any new identity; notes1656's
readable prepublication corroboration remains the finite-formula record.

P. Flajolet and L. Vepstas, *On Differences of Zeta Values*,
[arXiv:math/0611332v2, 11July2007](https://arxiv.org/pdf/math/0611332v2),
Section4, printed pp6--9, (19)--(30). Refreshed the actual
integrand(19), full-argument approximations(20)--(24), contour
choice and vertical-tail case(28), and the slanted-complement
case(29)--(30). The observable is a difference of zeta values;
the integrand contains zeta(1+s), sin(pi*s/2), Gamma(s+1)
and the rising finite product. Formula(24) is uniform for
s=x*sqrt(n) with x in a compact subset of the open first quadrant.
The contour has vertical abscissae c_j*sqrt(n), with
0<c_1<sqrt(pi)<c_2<2sqrt(pi), joined through its saddle.
The vertical-tail estimate is relative to that saddle scale.
Neither the function, contour nor normalization matches this target.
In particular its tail estimate does not import an endpoint-relative
bound on Re(s)=-1/4 up to d/log d. No part of that asymptotic is
used as a sign or a uniform theorem for F_d^I.

NIST DLMF [5.11.2 and5.11(ii)](https://dlmf.nist.gov/5.11),
accessed19November2026; version and previously inspected derivative
details are recorded in notes1663/1670. Refreshed the fixed-sector
digamma statement and first complex-remainder paragraph, and the
constant-a,b,c restriction preceding [5.11.12--13](https://dlmf.nist.gov/5.11#iii).
The former controls a full argument away from the negative-real cut;
the latter does not assert a ratio expansion uniform in growing shifts.
Use full arguments p, -s and d+1-s and verify their sectors on the
eventual neighborhoods. The theorem itself has no degree-power
annulus restriction. This observation concerns source hypotheses,
not an upper-tail phase inequality. The new gamma-phase comparison
and its competition with the Lambert contribution remain unproved.
No Stirling remainder may be differentiated without justification.

## Reused ready tools, without repeat discovery

Source-notes1673 already inspected Beck--Marchesi--Pixton--Sabalka,
*A First Course in Complex Analysis*, edition1.6 (August2025),
[Theorem4.2.5, printed p65, and Exercise4.5.10, p76](https://matthbeck.github.io/papers/complex.pdf).
Import the named fundamental theorem and complex integration by
parts under their holomorphy/path/primitive hypotheses. The exercise
is not misrepresented as a proved asymptotic theorem. Exact finite
calculus can be applied separately at each degree after its domains
are verified; uniform error still requires a separate estimate.

Source-notes1670 inspected A. Nagel, *Math722: Complex Analysis*,
Spring2012, [Corollaries3.11--3.12, pp10--11](https://people.math.wisc.edu/~nagel/Math722Spring2012.pdf),
including the proof and all-orders closed-disk Cauchy estimate.
Reuse it for first and second derivatives, with the complete closed
disk in an open holomorphic domain and its whole-circle value bound.
No new derivative theorem is needed because the endpoints changed.
The principal Lambert equation/derivative tools are covered in
notes1663 and C048a/m; no asymptotic expansion of W is imported.

Reuse notes1673's full comparison of Temme Section3.1(3.3)--(3.6),
DLMF2.3(i)/2.4(iii), and Pemantle--Wilson Theorem2.3/Corollary2.4.
Their fixed-data, phase or stationary-point hypotheses have not become
automatic on this changed contour. Exact calculus avoids depending
on a new uniform endpoint theorem. There is no reason to repeat
the basic integration-by-parts or Cauchy literature search.

## Duplicates, failures and bounded search

Read C048a/j/l/m/n/o's hypotheses and conclusions and the relevant
exact-derivative/domain/endpoint proof passages. Reuse their audits.
C048j supplies a value estimate in its full sector, independent of
d. C048m/n supply the sign margin only in their stated annulus;
C048o ends at the present lower endpoint. C048l's horizontal-edge
derivative and absolute closing budget do not control this vertical
integral. None duplicates the target. C048m(7)'s rho/d term was
absorbed using its annulus; that absorption must not be reused here.
The exact gamma and S derivative formulas have broader local domains,
but their applicability and estimates must be established afresh.

Scoped searches covered C048*.md and the specifically named
19November Rice source records, histories and stops. Read
stops1657/1665/1667 completely: fixed-degree absolute infinite
opening, in-sector main-term stationary points, and theta-boundary
crossing remain stopped. None of those operations is part of this
finite endpoint target. This review neither reopens them nor treats
them as global prohibitions. No cross-notebook input was used.

Fresh external queries actually issued: `"Rice integrals" "uniform"
"endpoint"`; `"finite differences" "Rice" "logarithmic derivative"`;
`"Rice" "d/log" Mellin integrals`; `"Rice's integrals" "endpoint"`;
`"Mellin" "Rice" "theta" "tail"`; and `"finite differences" "Rice"
"uniform asymptotic"`. Mostly irrelevant results and the already
known Rice sources were returned. Snippets, secondary reposts and
uninspected papers are not theorem evidence. Vallée2018 remains an
unimported lead already noted in notes1660; no essential tool in the
proposed exact-calculus attempt depends on it. A failed search
establishes no novelty or absence theorem. No essential source blocker
remains for one bounded attempt.

## Decision, remaining specialization and stopping test

SPECIALIZE, provisionally REPRODUCTION, for the unchanged target.
The inspected tools cover the proposed method outside the former
annulus, provided their actual hypotheses are checked. No inspected
theorem directly proves the desired uniform relative small-o.
Submit this changed-scope assessment for separate next-turn approval;
after approval default to mathematics without another source search.

The later attempt must verify the entire segment and complete complex
neighborhoods, with one eventual integer onset, for actual I, S,
the kernel, gamma factors and principal branches. It must control
actual Q_d and Q_d', retaining the full phase of d+1-s and the
Lambert contribution instead of extending C048m/n by name. It must
justify nonzero denominators, compare the integrated amplitude to
the specified lower endpoint, and bound the complete finite
integration-by-parts remainder relative to |F_d(c+iu_d)/Q_d(c+iu_d)|.
Retain s-derivatives, p=s+1/2 and ds/dt=i. Import the standard
calculus and Cauchy theorems; only these application obligations
justify a new proof. No disk radius, phase margin, derivative bound
or relative-error rate for the new segment is asserted here.

Continue only if that normalized remainder tends to zero uniformly
as integer d tends to infinity. An uncontrolled neighborhood,
denominator, gamma-phase loss or relative remainder is a precise
failure to record and a reason to park this mechanism. Absolute
smallness, a pointwise estimate, numerical samples or cancellation
of the endpoint difference do not meet the threshold.

The possible downstream use is one additional retained piece of
C048l's contour for J_d(-1). It does not pay the bounded core,
remaining pieces, total cancellation, other polynomial arguments,
C028b's sublinear height, C028g's compact nonreal-zero mass or the
sufficient signed Xi bridge at L030--L032/C032a. No source-covered
new central mechanism is prepared; this analytic specialization must
not be relabeled creative. Full matching Mathlib coverage is unchecked,
which is not evidence of absence. No lemma, mathematical script,
PROOF assembly or DAG change was made in this literature-only step.
