# Hardy-translate inverse cost: bounded dual-test scope

TARGET: Test a Fourier-filtered dual certificate for the saved Hardy-translate bump and compare its total-variation lower bound with the fully summed unamplified shifted-moment error.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed bounded searches, exact-target comparison and failure checks in drafts/literature/2026-11-01-hardy-translate-localization-cost-review.md and its query register. Searches for Hardy-Z bandlimitation, local Riemann--Siegel Fourier structure, atomic-TV duality and actual-Hardy inverse approximation identified no matching cost theorem; no originality claim.
SOURCE_EVIDENCE: Reused the parent review and verified direct access to Hughes--Young v2 Theorem 1.1/(11)--(17), pp. 3--5 https://arxiv.org/pdf/0709.2345v2#page=3 ; Chandrasekaran et al. v3 Section 2.1/(2)--(3), p. 5 https://arxiv.org/pdf/1012.0621v3#page=5 ; Bodmann--Flinth--Kutyniok v1 Definition 2/Lemma 1/Proposition 1 with proof, pp. 6--8 https://arxiv.org/pdf/1803.04218v1#page=6 ; DLMF 25.10.1--3 https://dlmf.nist.gov/25.10#E3 ; Hughes July 2017 Theorem 2.2, pp. 18--19 https://personal.maths.manchester.ac.uk/jm/wiki/uploads/LMS/Hughes-lectures.pdf#page=20 . Full previously inspected qualifications remain in the parent review; no new theorem is imported.
COMPARISON: Standard atomic duality and the real-axis O(t^(-1/4)) Riemann--Siegel remainder are adequate inputs for a bounded construction attempt, not a ready theorem about this dictionary. The necessary weighted Fourier-filter estimate, bump overlap and arbitrary-atom moment summation are not supplied by those sources. No exact bandlimitation, kernel normalization, density, attainment or signed approximation theorem is imported.
GAP: Find a bounded-norm dual vector with overlap above the 1/4 tolerance and X-uniform correlation O_w(T^(-1/4)/sqrt(log T)) against every allowed atom, or identify a failure of this filter design; prove the finite-complex-atomic moment error in the actual TV norm before comparing costs.
REASON: Separate literature-only recovery on 2026-11-01 repaired missing direct URLs and approved the unchanged bounded subtarget using the adequate parent assessment. The quantitative dual mechanism is distinct from fixed forward-block and pure Dirichlet-weight tests; it remains mathematically unexecuted. Further literature is unnecessary absent changed hypotheses or a new essential source need.
SCOPE: Exactly the parent review's fixed psi, normalized g_(T,X), w,u0, a=X+u0*T, L=log T, T<=X<=2T, finite complex atomic mu on [-1,1], no amplifier and L2(w_XT dt) tolerance 1/4. Number of atoms unrestricted; uniformity in X and shifts mandatory. No change of target bump, coefficient norm, signed-error tolerance or presumed negative interval.

## Import boundary and mathematical obligations

The main gap remains actual-Xi pointwise initial signs at unbounded
heights and all-degree mixed positivity. This cost test examines a
necessary feature of one proposed realization mechanism; even success
does not give the missing signs.

Use L622's actual Z,W and weight definitions. L622 Sections 1--4
supply the audited phase-weight/Cauchy and gamma-curvature toolkit
under their named imports; extending their coefficient accounting
is a proof obligation. L636's forward two-height margin and L620's
pure-weight concentration stop are contrasts, not mathematical
premises for an inverse-cost theorem. L465's analytic gamma/strip
bounds support phase and tail control, if used. Read those exact
proof ranges before applying them. No cross-notebook input is needed.

Import the real-axis Riemann--Siegel formula by its precise classical
citation in the parent assessment. Its remainder is pointwise
O(t^(-1/4)); do not differentiate it. The cosine phase is not linear
in t and its cutoff moves with t. The formula does not put Z in a
global Paley--Wiener space. Use the ordinary smooth Hardy phase
consistent with L622, rather than a discontinuous argument branch.

The proposed design is a Fourier-filtered test vector at microscopic
scale x=L(t-a). Seek ||q_(T,X)||<=B with B independent of T,X and

    Re <g_(T,X),q_(T,X)> -(1/4)||q_(T,X)|| >= b>0,
    sup_(|s|<=1) |<Z(.+s/L),q_(T,X)>|
                              <= B' T^(-1/4)/sqrt(L).

These inequalities are targets, not established claims. The inner
product is the original weighted L2 inner product, linear in its
first slot. The constants may depend on the fixed w,u0,psi and filter.
The later proof must cover complex coefficients using absolute
pairings, not just real sums. No equality of primal and dual extrema
or measure minimizer is required. A short finite-sum weak-duality
proof is justified because the sources' normalized RKHS and
finite-dimensional conventions differ from this dictionary.

All weight divisions must stay where w is bounded below. Fourier
tails, cutoff boundaries, both cosine orientations, phase curvature
and the real-axis remainder must be charged. A sampled shift grid
or finite-dimensional interpolation cannot replace the supremum.
If a standard Plancherel/Fourier-multiplier estimate is specialized,
state its angular-frequency convention and preserve all constants
needed to exceed the tolerance.

The moment comparison must retain the exact complete source main
term and all c_j conjugate(c_k) contributions. Test the parent
review's proposed raw error envelope

    C_w ||mu||_TV^2 [T^(19/25)L^2+T^(-1)L^4],

including coefficient summation, collision-safe differentiation,
uniform complex phase weights and curvature. This expression has
not been proved here. The h=k=1 case has no amplifier N factor;
do not substitute L636's two-vector Euclidean estimate. Constants
must be independent of atom count, locations, T,X and coefficients.

Compare the resulting cost lower bound with the *proved* error
envelope, initially even at the coarse T L^6 scale. The actual
unit-bump signed signal may require a smaller error. A failure of
this sufficient absolute envelope is not a lower bound on the true
remainder or a prohibition on cancellation-sensitive methods.

## Continuation / abandonment test and routing

A successful overlap-and-correlation certificate gives a checkable
TV lower bound for every admissible finite approximant, regardless
of whether the infimum is attained. Compare it with the complete
absolute error budget; record a cost obstruction only to that
certificate mechanism. If localization is not excluded by this
test, signed |W|-weighted approximation and observer positivity
remain separate, uncovered tasks. If either the overlap or the
uniform correlation target fails, identify the exact failed estimate
and preserve the attempt before choosing another mechanism. Do not
repeat qualitative density retrieval or enlarge a forward block.

This is proposed proof_attempt/creative routing: the obstruction is
realizing a microscopic signed witness using arbitrarily many actual
Hardy translates without spending the moment-error budget. The bounded
test is the displayed dual certificate and complete TV error comparison.
It tests a new inverse mechanism at the pointwise-sign gap; elementary
duality itself is known mathematics. A later report must distinguish
imported/reproduced tools from any locally established estimate and
must not claim originality from this bounded search. Full matching
Mathlib coverage is unchecked and unknown. No RH candidate exists.

This assessment was originally nominated during a literature-only turn.
The separate 2026-11-01 direct-URL recovery review approves its unchanged
scope for a later research invocation; approval does not assert that the test passes.

## Direct-source recovery review, 2026-11-01

LITERATURE_REASON: Supervisor requires direct primary-source URLs in this ready assessment; reuse the parent coverage and repair that omission without repeating discovery or executing mathematics.

All five URLs in SOURCE_EVIDENCE resolved to the stated source. Rechecked
Hughes--Young Theorem 1.1 and its collision-holomorphy remark, the
Bodmann--Flinth--Kutyniok Proposition 1 pairing, the finite-dimensional
setup in Chandrasekaran et al., and Hughes's Theorem 2.2 statement.
Reuse the parent's complete proof reading and scope comparison. DLMF
25.10.1--3 supplies the normalization and classical theorem reference.
No accessible source has changed the comparison or established the
proposed Hardy correlation estimate or complete TV error envelope.

The parent review's recorded duplicate/failure checks remain applicable:
L620 is a pure-weight concentration stop; L636 is a forward block;
Runge/prolate and qualitative theta density do not establish this inverse
TV bound. Nonessential blocked high-order sources remain parked. No
additional retrieval, source theorem or novelty finding is claimed.
The main gap, fixed bump, arbitrary finite complex coefficients, all
uniformities and explicit continuation/abandonment test above are unchanged.
Mathlib matching coverage remains unchecked. This is a process repair,
not mathematical progress; the next invocation should attempt the test.
