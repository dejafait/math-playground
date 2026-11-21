# Direct actual-coefficient partial biorthogonality — completed review2059

TARGET: Review whether the strictly sign-consistent Meixner-Pollaczek transform admits an N-2 real-zero transfer from the prescribed actual coefficient polynomial, with N=6 as the sole input-condition screen.
CHECKED: 2026-11-21
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reused auxiliary-review2058 and the named November20–21 Pollaczek/Jensen assessments; scoped searches found no earlier Musin0903.1908 or completed partial-node count assessment there. Exact biorthogonal/Chebyshev/sign-change searches located Musin's explicit general theorem. No exhaustive search or novelty claim; queries and inspected primary ranges below.
SOURCE_EVIDENCE: Musin arXiv:0903.1908v2 (27Apr2009), Section2 definitions pp2–3 and Theorem1/full proof p4; Iserles–Norsett1988 Section3/Lemma4/Theorem5 pp459–460; Iserles–Saff1989 Section2/Theorem2 pp562–563 and Proposition6 pp566–567; Kuznetsov2008 Proposition4.1 p567; DLMF18.23.7,18.19.6–9,5.11.9. Links, exact hypotheses and remaining applicability work below.
COMPARISON: Musin's orthogonality theorem counts sign changes from the dimension of the annihilated Chebyshev system without requiring that dimension to equal the degree of the function. This supplies the missing general partial-count input, beyond the full-degree conclusions of the two Iserles papers. It does not assert the prescribed transform identity or actual Q_6 roots; both remain separate specialization/input tasks.
GAP: No partial-node theorem for the exact U_N is proved here. Its moment identity on the real parameter line needs a justified normalization, integration and analytic-continuation argument; the generating power series itself is only cited for |z|<1. Q_6's four-distinct-real-node condition, uniform input estimates, initialization and Xi transfer remain unproved.
REASON: The general partial-count source is now available, so park further generic searching. Nominate one independently testable Q_6 input-condition screen, with no U_N output-root count or sweep. A successful screen would still leave the transform specialization and all-N premise open; a failed screen stops only this N=6 sufficient-condition baseline.
LITERATURE_REASON: Changed essential hypothesis from real-rooted auxiliary inputs plus a composite operator bound to partial real zeros of the actual scalar coefficient polynomial. The inspected full-real-input theorem does not state the requested partial-root conclusion.
SCOPE: Completed literature-only review2059; no new partial-orthogonality proof, input-root calculation, lemma, mathematical script, output inertia computation or degree sweep. Ready sources justify a later specialization attempt, not a claimed actual-family zero bound.

## Source comparison2059

The original nomination below is preserved. The main gap and threshold
are unchanged: L030–L032/C032a and C029m's eventual full-family
Hermite index<=1. Only source coverage advanced; no mathematics beyond
the inspected sources is claimed.

### General partial count, precisely cited

Oleg R. Musin, *Chebyshev systems and zeros of a function on a convex
curve*, [arXiv:0903.1908v2, 27 April 2009](https://arxiv.org/pdf/0903.1908v2),
Section2, pp2–4, defines a Chebyshev system of n continuous functions
on an interval D by the bound n-1 on the distinct zeros of every
nonzero linear combination. The continuous weight rho has constant
sign. Orthogonality means that each integral of f*f_j*rho is zero.
Theorem1, p4, concludes that continuous f has at least n sign changes
when f*rho is not identically zero. Its full proof uses a generalized
polynomial matching the alleged fewer sign changes and contradicts
the zero integral of the resulting constant-sign product. This is
the relevant general statement: f is not assumed to have degree n.
It counts sign changes of f, not algebraic multiplicities of input
nodes. The proposed application must establish existence/absolute
convergence of its integrals on the unbounded interval; truncation
would not preserve the required zero integrals.

Iserles–Norsett, *On the theory of biorthogonal polynomials*, Trans.
AMS306(1988),455–474,
[DOI](https://doi.org/10.1090/S0002-9947-1988-0933301-8),
[author-uploaded primary PDF](https://www.researchgate.net/profile/Arieh-Iserles/publication/247048824_On_the_Theory_of_Biorthogonal_Polynomials/links/56a9e70f08aef6e05df36a5f/On-the-Theory-of-Biorthogonal-Polynomials.pdf),
Section3 pp459–460: dphi=omega*dalpha with alpha independent of the
parameter; interpolation at distinct spatial/parameter nodes is
equivalent to the determinant condition in Lemma4. Theorem5 assumes
parameter C1 regularity, interpolation and a regular distribution,
and concludes m distinct interior roots for the degree-m BOP with m
conditions. Its proof was read, including the interpolation/positive
integral contradiction. It is not quoted as a partial-degree theorem;
Musin supplies the explicit general formulation instead. PDF OCR is
imperfect, and screenshot calls returned no image payload; no claim
about the correctness of every displayed inequality in this scan is
needed or made.

### Matching sources and the work still to do

Iserles–Saff, *Zeros of expansions in orthogonal polynomials*, Math.
Proc.Camb.Phil.Soc.105(1989),559–573,
[DOI](https://doi.org/10.1017/S0305004100077938),
[author-uploaded primary PDF](https://www.researchgate.net/profile/Arieh-Iserles/publication/248493711_Zeros_of_expansions_in_orthogonal_polynomials/links/00463529d8b1ee5edf000000/Zeros-of-expansions-in-orthogonal-polynomials.pdf),
Section2 pp562–563 assumes positive orthogonality measure, nonzero
basis norms and generating coefficients, and a convergent SSC kernel.
Theorem2 requires all scalar roots in the parameter interval and uses
inverse generating-coefficient/norm weights. Proposition6 pp566–567
treats Meixner second kind with real delta and eta>0. These complete
relevant passages were retrieved; no partial-degree result is inferred
merely from their all-root conclusions.

Kuznetsov, CMB51(4)(2008),561–569,
[Proposition4.1 p567](https://doi.org/10.4153/CMB-2008-055-0),
fixes exactly the scalar weights (2k+1)!!/(2k)!! of the nomination.
Reuse that normalization; C029n's N=6 degree/nonvanishing data and
C029q's finite setup do not establish any uniform-degree statement.

The independent normalization references are
[DLMF18.23.7](https://dlmf.nist.gov/18.23.E7), the generating function
with |z|<1, and [DLMF18.19.6–9](https://dlmf.nist.gov/18.19#E6),
orthogonality on R with lambda>0, 0<phi<pi, weight
|Gamma(lambda+ix)|^2 exp((2phi-pi)x) and squared norm
2pi*Gamma(n+2lambda)/((2sin(phi))^(2lambda)*n!).
[DLMF5.11.9](https://dlmf.nist.gov/5.11.E9) gives the gamma-modulus
asymptotic for fixed real part and imaginary part tending to either
infinity. These primary entries were inspected, including the norm
and parameter restrictions. For the later applicability argument the
parameters are lambda=3/4, phi=pi/2 and x=t/2. Candidate kernel is
the real analytic expression associated with the generating function,
(1+mu^2)^(-3/4)*exp(t*arctan(mu)); this expression is a specialization
target, not a newly proved integral identity in this review.

Do not promote the real-domain closed expression to a generating
series convergent for all real mu. DLMF only asserts |mu|<1 for that
series. To cover arbitrary real scalar nodes, the later proof must
first justify the moment identity where the series is usable and then
continue it on a connected analytic domain with compact integrable
bounds, or use a cited direct integral identity. The source assertions
in Proposition6 at delta=0 do not waive that check. Absolute
integrability, a positive weight and the Chebyshev property of distinct
kernel sections must all be explicitly matched before asserting the
conditional U_N count. No confluent-node theorem has been assessed;
use distinct scalar roots only. No new specialization was derived here.

### Bounded search and decision

Queries included the exact Iserles–Saff and Iserles–Norsett titles,
`strictly sign consistent sign changes biorthogonal polynomials partial`,
`Chebyshev system orthogonal at least sign changes theorem`,
`Laplace transform sign changes zeros theorem polynomial`, and
`Chebyshev systems and zeros of a function Musin`. Vanderbilt timed
out; corrected AMS journal PDF returned403, but the two primary
author-uploaded PDFs were accessible. Musin's full v2 statement/proof
was read, not inferred from its abstract or a snippet.

Tokarev, *A generalisation of Descartes' rule of signs*, J.Aust.Math.Soc.
91(2011),415–420, [Theorems1/7, Remark8 and proofs pp416–419](https://doi.org/10.1017/S144678871100156X),
was inspected as a scope comparison. Its positive-half-line measure
and positive-transform-zero statement is not an automatic bilateral
substitute here; it is not an input to the proposed specialization.
No further source chase is needed for the independent fixed-Q_6
algebraic screen. The generic auxiliary composition, boundary metric,
fixed residue, inverse-map and consecutive-kernel stops remain in their
original scopes. None was retested. Named local November20–21
assessments were searched for overlap; no novelty is inferred from
that bounded search. No cross-notebook input; Mathlib matching unchecked.

The next nominee tests only whether the prescribed Q_6 has four
distinct real roots. It is an independent necessary premise of this
particular sufficient-condition baseline even while the analytic
specialization remains unwritten. Fewer than four parks this N=6
baseline; four or more permits a later conditional-transfer proof,
not an all-N claim. A finite failure would neither refute the eventual
C029m hypothesis nor RH. A new ready assessment for that exact screen
is saved separately for next-turn approval. Creative priority remains
blocked by the absence of an independently supported uniform actual-
coefficient mechanism; this finite specialization is not creative.

## Original nomination2058 (historical)

The main gap is L030–L032/C032a; C029m's eventual full-family
Hermite index<=1 remains unproved. A count theorem could leave a
separate actual scalar root-condition problem, bypassing auxiliary
inversion. Such a conditional interface is not the uniform input
estimate or RH.

Fix U_N=sum A_(N,k)p_k exactly as in C029m/n/q, retaining odd terms
and N's own weights. For this nomination only, define the source's
scalar test polynomial

    Q_N(x)=sum_(k=0)^N [(2k+1)!!/(2k)!!] A_(N,k) x^k.

This is the coefficient polynomial named by Kuznetsov Proposition4.1,
not a new integral identity. No Q_N coefficients or roots were computed.
The proposed threshold, subject to the precise source interval and
nondegeneracy hypotheses, is N-2 distinct real input nodes: four at
N=6. The review must establish that these nodes give the required
moment vanishings and that a count theorem controls U_N's real sign
changes. Four scalar roots alone are not yet an approved implication.

Retrieve exact partial-biorthogonality/Chebyshev-system hypotheses
and relevant proof cases, reusing full-real-input coverage in completed
review2058. Check Meixner normalization, interval including delta=0,
positive measure, integrability, convergence and needed exchanges.
Multiple parameter nodes would need derivative/confluent coverage;
distinct nodes suffice for the proposed discriminator. Establish actual
degree, using C029n/q only at their covered degrees, not uniformly.

Continue only if a cited count theorem or identified specialization
supports a fixed independent condition on this Q_N, specifying an
exact N=6 test before computation. If the source handles only all-real
input, has incompatible interval/measure hypotheses, or no partial-count
mechanism can be assessed, park this proposal. Do not substitute
repeated U_N root counts or a larger N sweep. A failed finite input
screen would stop this baseline sufficient condition, not the eventual
target or RH.

Essential inputs: C029m actual family; C029n/q normalization and finite
degrees; C029l distinct-limit interface; completed auxiliary review2058.
Preserve L530/L955, stops111/1596 and C029q/r/s/t/v/w/x in their separate
scopes. Uniform actual-input root/sign control, initialization, degree
drops, weighted convergence/upstream[9] qualifications and Xi transfer
remain open. No cross-notebook input. Mathlib matching unchecked.

Creative priority considered: an all-N actual-coefficient sign mechanism
could deserve a bounded creative attempt, but no such independently
supported mechanism is ready. This partial-biorthogonality theorem
comparison is standard source work. Resolve its essential source scope,
then route the exact surviving mathematical target on its merits.
