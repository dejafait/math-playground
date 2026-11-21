# Two-observation primal certification: source review1797

19 November 2026. Literature-only completion of assessment1796's exact
TARGET. No weights, determinant, numerical bounds or new lemma were
derived. The central gap remains actual-Xi all-degree positivity in
L030-L032/C032a; cancellation, signed-height control and realization
remain independent. This intermediate target could supply one admissible
finite-observation primal input for C033w. It cannot settle RH.

## Primary numerical statements inspected

Siegfried M. Rump, *Verification methods: Rigorous results using
floating-point arithmetic*, Acta Numerica19(2010),287-449,
[corrected author PDF](https://www.tuhh.de/ti3/rump/intlab/ActaNumerica2010.pdf),
Section10.3, PDF p53 (internal pagination), Theorem10.2 and its preceding
proof (10.8)-(10.9), read completely. For real square A,R and real
vectors b,x0, if a subordinate matrix norm satisfies q=||I-RA||<1,
then A is nonsingular and

    ||A^(-1)b-x0|| <= ||R(b-A*x0)||/(1-q).

No prior invertibility assumption on R is needed. The infinity norm
provides component bounds. The proof verifies nonsingularity a
posteriori and bounds the inverse through the norm condition; no
positivity, total positivity or analytic-kernel condition occurs.
A floating-point condition estimate is not this hypothesis. Both norm
bounds must be rigorous. Failure of the sufficient test proves neither
singularity nor nonexistence of an interpolant. Import this theorem;
no reproof is authorized or needed. Later interval algorithms in
Sections10.5ff are not selected.

Arb2.23.0, [arb_mat reference](https://arblib.org/arb_mat.html),
introductory approximate-method warning, norm section and linear-solving
section, especially arb_mat_solve and arb_mat_solve_preapprox, inspected
with their success/failure cases. Nonzero return certifies invertibility
and an enclosure of the exact solution; zero leaves output undefined
and may reflect insufficient precision. Approximate methods ignore
radii and carry no error bound. arb_mat_bound_inf_norm bounds the
largest absolute row sum. These are implementation contracts, not an
installed-library check or an assertion that exact transform inputs
have been enclosed. The frozen2.23 documentation states Arb merged
into FLINT in2023; record actual version if implementing.

Current [FLINT verified-linear-algebra documentation](https://flintlib.org/doc/algorithms/ball-arithmetic/linear-systems.html),
Theorem2 and certification section, was also read. It agrees with the
residual bound but carries an October2026 LLM-generated-content notice.
The independent primary Rump statement is the mathematical authority;
no new algorithm or asymptotic precision guarantee from that page is
needed here.

## Reused analytic coverage and corrected input map

C033w's full hypotheses and finite-observation conclusion (2)-(3) were
read, with its primary minimax citations. Source-notes1792/1748 already
cover the unchanged signed measure and transform contracts; no fresh
functional-analysis discovery is claimed. C033o's complete support
proof and C033l's hypotheses were inspected. Neither supplies the
three desired weights. C033g concerns a different observable.

The nomination understated local effectivity: C033m's conclusion,
Sections3-5 and relevant audit1755 cases explicitly provide rational
absolute enclosures for this exact residual, not merely a proposed
evaluator. C032w's hypotheses/conclusion and C032x's cost-stop statement
and mechanism were read. Primary explicit-formula and quadrature
coverage1752/1754 is reused: Connes, Section2(4)-(9),
[author PDF](https://alainconnes.org/wp-content/uploads/heat-zeta.pdf),
and Talvila--Wiersma, Section1(1.1)/composite rule and Section4,
[1202.0249v1](https://arxiv.org/pdf/1202.0249v1).
Their general identities need no reproof. C033m does not claim feasible
runtime, and its full exponent uses C032w's costly construction.

C032w gives uniform primitive enclosures for real widths in[1,2];
C032q identifies the positive-real lift with B_sigma. Their application
to k(s,sigma)=exp(-B_sigma(s)) at the specified arguments still needs
explicit arithmetic and exponential propagation. C033m covers m(s)
for rational s>0. C033s's compact integrals are for another observable;
they cannot be substituted. No new zero coordinates are available or
required by these analytic interfaces.

The two-observation nomination and narrowly searched residual/minimax
notes contain no completed fixed-three-width solution. Searches were
restricted to these local claims and failure comparisons; no global
originality is asserted. C032x stops a specified literal common-disk
scheme; stop1571 concerns independent boxes for another dictionary.
Neither is a lower bound on the actual entries or on all evaluators.
Do not execute either stopped scheme. Gaver, common-prime and other
previously stopped evaluations are not reopened by a solver citation.

## Approved bounded test, still to be performed

Keep the target unchanged. Set up the real3-by-3 system with columns
indexed by sigma=1,3/2,2: first row all1, second row k(1,sigma), third
row k(2,sigma), and right-hand side (1,m(1),m(2)). This merely specifies
the nominated equations, not their solvability. Exact mass and exact
matching, rather than rounded residuals, are the required result.

Before evaluating large expressions, budget the eight scalar entries
at trial absolute radii 2^(-8),2^(-16),2^(-32),2^(-64). Check the existing
scalar bounds and explicit term counts first. Bound this screen to
10^6 elementary scalar/node/prime-power terms in total; this is an
operational cap, not a mathematical threshold or lower complexity
bound. Record the actual allowance and required counts. If the existing
formula cannot meet a trial within the cap, preserve that obstruction
and end the screen without executing its huge sums or pretending to
have measured conditioning. This may leave every actual matrix entry
unknown. Do not replay C032x's common-disk calculation as new evidence;
only an instance-specific scalar budget or actual enclosure is relevant.
A different evaluator would need separate scope review.

If affordable enclosures exist, choose finite rational R and x0 from
approximations, compute rigorous q and residual bounds using the full
input radii, and apply the imported theorem only after q<1 is proved.
Next check an upper bound for the sum of the three absolute exact
weights against2, using certified component enclosures. These remain
application obligations: no coefficient, amplification constant, TV
margin or determinant value has been established in this source turn.
If feasible, justify its finite-problem consequence using C033w in
the later research step. If a nonsingular exact system is certified
and the variation is instead rigorously greater than2, reject only
this fixed support. Overlapping TV bounds or an uncertified matrix
leave the outcome unresolved. Equality at the cap may require exact
information; shrinking intervals alone need not decide it.

Independent interval enclosures can overestimate correlated entries;
success is sound but failure is not an actual-kernel counterexample.
A finite feasible primal input would not evaluate the full interval,
produce a strict dual witness, give an arbitrary-variation rate or
realize Xi. Full positivity, excluded ordinate-zero, actual divisor,
conjugation/multiplicity, strict strip/gamma>14, counting, through100,
retained-real-zero, reciprocal-square-tail, heat positivity, separate
fixed-j errors, Gaussian half-variance and both fixed-v1 qualifications
are retained wherever the law/separation interpretation uses them.
The numerical theorem itself needs none of the zeta hypotheses. No
source-wide correctness or finite-zero verification is claimed. Full
matching Mathlib coverage is unchecked/unknown.

## Search evidence and routing

Queries: `site.arblib.org arb_mat solve precond rigorous error bound`;
`Rump verification linear systems approximate inverse residual infinity
norm theorem interval`; `Siegfried Rump Verification methods rigorous
results floating point arithmetic 2010 Theorem10.2 pdf`; `capped signed
Laplace interpolation total variation`; `Gaussian zeta Laplace
interpolation signed widths`. No exact-family theorem was identified.
Search hits alone are not imported; the primary statements above were
opened. No essential source blocker remains for this bounded test.

SPECIALIZE is appropriate: verified solving is known, while numerical
inputs and their feasibility are unknown. Next defaults to a standard
calculation/preflight, not a creative central proof. The central
mechanism batch1796 remains parked for lack of an independent signed
upper term or representation; no creative mechanism is invented to
satisfy a scheduling preference. This review uses no mathematical
exploration budget and resets no counters.
