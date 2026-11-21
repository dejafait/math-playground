# Beta-weight transfer — completed source comparison

TARGET: Establish or refute uniform beta-weight transfer E(T,tau)=sum_{T<gamma<=2T}[(gamma+i(1/2-beta))^(-i tau)-gamma^(-i tau)]=o(T log T) for T<=tau<=2T, using principal logarithms and all zero orders at arbitrary endpoints.
CHECKED: 2026-11-04
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Exact complex-node difference, horizontal first-moment, Selberg integrated-density and zero-ordinate searches; reused the two named assessments and scoped duplicate/failure searches. Primary comparison and queries below; no originality claim.
SOURCE_EVIDENCE: Reused saved GSS v1 Theorem 2/Section 3 and Simonic v2 Theorem 1/Sections 4.2 and 4.5; reopened their statements, count conventions, Littlewood setup and complete (73)--(75), including constants and endpoint/microscopic cases. Precise citations below.
COMPARISON: The integrated density input is adequate for a separate displacement-weight specialization, although it did not furnish the earlier sublinear height-union target. GSS supplies an alternative complex-node formula; its RH ordinate corollary remains excluded. No theorem found states this exact difference verbatim.
GAP: Prove the finite-count horizontal-displacement identity, reflection/order matching, principal-log weight comparison and uniform summation at arbitrary endpoints. These elementary applicability steps, including any resulting rate, are deferred; E=o(T log T) is not established in this literature turn.
REASON: Source coverage now supports a concrete routine specialization of known results for the unchanged target. It neither reopens the parked census/Cartan routes nor reproduces unchanged scalar source approval. Separate supervisor approval precedes mathematics.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target changes from scalar ordinates to beta-sensitive complex nodes; essential hypothesis comparison was missing despite reusable source evidence.
SCOPE: All nontrivial zeros rho=beta+i gamma, with analytic orders; distinct zeros sharing gamma contribute separately. T tends through real values, T<=tau<=2T. Use the principal logarithm of gamma+i(1/2-beta), whose real part is positive. No RH, Lindelof, simplicity, typical heights or stronger zero-free premise.

## Purpose, alternatives and bounded test

Main gap: actual-Xi all-degree mixed positivity and initial Laguerre
signs. The proposed intermediate target removes one identified obstacle
to interpreting scalar ordinate cancellation at the actual complex Xi
nodes. Downstream use is only a possible witness-remainder estimate;
shorter windows, witness realization, analytic costs, positive margins
and sign transfer remain independent gaps. No paid witness follows from
this nomination or from L756.

Compare these mechanisms before approving further work:

1. A uniform off-line census under a registered half-plane premise is
   parked in `ATTEMPTS/2026-11-04-uniform-offline-census-source-block.md`.
   Its Lindelof/source-scope obstruction remains. This nomination asks
   for neither a unit-window census nor an implication from that premise.
2. Adaptive interior Cartan certification is parked in
   `ATTEMPTS/2026-11-04-interior-cartan-paid-certificate-stop.md`.
   Its normalized loss exceeds its paid allowance. This nomination
   supplies no improvement to that disk/envelope mechanism.
3. Select the beta-weight difference above for separate assessment.
   A possible mechanism is a branch-controlled comparison of individual
   weights combined with unconditional displacement-sensitive density.
   The prior charged-block union stop concerns a different threshold;
   check its relevance rather than assuming either success or failure.

The present turn completes source coverage only. After separate approval,
continue with one finite-sum applicability calculation for the unchanged
TARGET. The discriminating threshold remains uniform o(T log T).
An O(T log T) estimate, fixed tau, RH or typical endpoints would fail.
An absolute displacement-weight comparison is the selected mechanism;
no additional oscillatory cancellation is assumed. Stop this
specialization if the branch estimate or density application loses the
required saving. No mathematical estimate or expansion is proved here.

## Primary input and qualifications

Aleksander Simonic, *Explicit zero density estimate for the Riemann
zeta-function near the critical line*,
[arXiv:1910.08274v2](https://arxiv.org/pdf/1910.08274v2),
29 November 2019, Introduction p.1, Theorem 1 p.2,
Section 4.2 p.29 and Section 4.5 p.33, especially (74).
Write D_T(u)=N(u,2T)-N(u,T). The source counts beta>u and
0<gamma<=T. Its displayed inequality is

    integral_sigma^1 D_T(u) du
      <= (2e^2/pi+alpha) T^(1-(sigma-1/2)/4)
         + b log T+c log log T+d+0.88
         +2.4 log log T_0/log T_0+20/log T_0.             (74)

Here T>=T_0>=e^24, 1/2<=sigma<=1/2+8/log T_0; the constants
are defined immediately after (73), using sigma_1>=2.4. The final
proof takes T_0=H_0=3.0610046*10^10, sigma_1=2.40764,
alpha<15291.986, b<4.416, c<0.6881, d<0. The input already
covers sigma=1/2 with an O(T) integrated bound. Its proof separates
the microscopic band using total counts and explicitly extends to
boundary ordinates. Littlewood's lemma retains zero orders. Full
moment proofs and numerical constants are imported, not independently
audited. No reproof is needed for this application.

The symbols b,c,d above rename the source's beta,gamma,delta constants
to distinguish them from coordinates of zeros. This is a transcription
of the cited input, not a new density or displacement estimate. The
source's restriction on sigma concerns the lower integration limit;
the integral itself ends at 1. Do not mistakenly truncate the zeros
at beta=0.831. Strict horizontal cuts, repeated ordinates and the
one-sided endpoint interpretation still require explicit bookkeeping
in the later finite-sum application; counts themselves are not
continuous functions of height.

## Exact and stronger-result comparison

Garunkstis--Sourmelidis--Steuding, *The Lindelof Hypothesis for Zeta
Zero Ordinates*, [arXiv:2505.14228v1](https://arxiv.org/html/2505.14228v1),
20 May 2025, Theorem 2 and Section 3, pp.2--3 and 5--8, supplies
an unconditional formula for the complex-node sum. Its range is
comparable x,y>=2, 0<=tau<<x log x. Above c x log 2, fixed
0<c<1, it uses a prime sum over exp(tau/y)<=n<=exp(tau/x)
with an explicit uniform remainder; below it, a smooth integral.
It is therefore a relevant alternative for the nominated band, not
a theorem only about fixed tau. Corollary 1's pure-ordinate conclusion
assumes RH and cannot be imported. To obtain the exact difference
from Theorem 2 would still require bounding its arithmetic expression,
subtracting L756 and reconciling [x,y) with (T,2T]. The previously
recorded unqualified log-derivative display (11) and endpoint proof
qualification are preserved. No new audit of that proof is claimed;
the selected density mechanism does not depend on it.

The density input is stronger information about displacement than a
mere count of off-line zeros. The remaining work is not a new density
theorem: convert its finite integral to the appropriate displacement
sum, use L018's reflection with multiplicity, and compare the weights
along a segment in the right half-plane using the principal logarithm.
The dependence on tau/gamma must be tracked uniformly on the entire
specified band. These are the precise specialization obligations;
no bound for their outcome has been derived or certified here.
L756 can be assembled only after transfer is proved. Smaller windows,
general beta-dependent witnesses, analytic costs, positive margins and
Laguerre signs lie outside this assessment.

## Searches, overlap and continuation coverage

Queries included `zeta zeros horizontal distance critical line sum beta
minus half Selberg density integrated T`, `zeta zeros horizontal first
moment`, `zeta gamma+i beta density`, `zeta zero ordinates density complex`,
and `2505.14228 gamma beta`. Results located the already relevant
primary papers, surveys and unrelated material; no additional exact
matching theorem was inspected. Search snippets are leads only.
No absence or originality conclusion follows from these searches.

Reused `2026-11-01-charged-block-bad-height-measure.md` and
`2026-11-04-zero-ordinate-exponential-cancellation-scope.md` in this
directory. Read L018's full correspondence and L756's hypotheses and
relevant partial-summation proof. Scoped searches covered these
assessments, the zero-ordinate assessments/failure and density failures.
The canonical scalar result is a distinct input, not a duplicate
beta-transfer theorem. `ATTEMPTS/2026-11-01-charged-block-density-source-limit.md`
parks direct import of an o(T) height union, not this o(T log T)
displacement-weight target. Its O(T) source limitation is preserved.
The census/source-access, Cartan/paid-loss and scalar-approval stops
were checked and remain closed. No cross-notebook input is used.

Essential inputs for the later specialization are L018 and the cited
integrated-density bound; L756 is needed only for downstream assembly.
The segment comparison uses standard holomorphic differentiation of
the principal logarithm in the right half-plane and the fundamental
theorem of calculus on a finite segment. These elementary steps need
an application proof, not a separate source-discovery turn or a reproof
of Selberg density. All zero orders, coincident ordinates, arbitrarily
small displacements and arbitrary real T must remain explicit.
No RH, Lindelof, simplicity or spacing hypothesis is introduced.
Full matching Mathlib coverage is not checked; availability is unknown.

This is routine specialization coverage, not creative mathematics.
The blocker to a protected creative witness attempt remains the lack
of an assessed concrete window/margin mechanism connecting this scalar
input to a paid sign. The same exact TARGET is now SPECIALIZE, subject
to the separate approval turn required for newly changed assessments.
No lemma, mathematical script, transfer proof or RH candidate was made.
