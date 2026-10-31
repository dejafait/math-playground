# Primary coverage for the retained trace input

TARGET: Assess the primary renewal and boundary-regularity inputs needed to audit bramble_trace v1 equation (3.19) for bounded signed forcing, including the geometric-stable parameter-two normalization.
CHECKED: 2026-10-30
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Searched exact-title, geometric-stable/signed-boundary-potential and renewal-normalization queries; inspected the named primary papers rather than search snippets. Narrow Weil assessments, L512 and the two recorded Weil stops contain no duplicate trace-input audit; public discussion is an unread secondary lead, not certification.
SOURCE_EVIDENCE: Read Grzywny–Ryznar arXiv:1107.0745v1 Sections 2–3 normalization and occupation formula, Proposition 3.2, Proposition 3.5 upper-bound proof/Remark 3.6, Lemma 4.1 including its parameter-two proof case, and Lemma 4.3; Hernandez-Santamaria–Lopez Rios–Saldana arXiv:2401.18033v2 Theorem 1.1, variational definitions and its Section 4 signed-data proof; Chen–Weth arXiv:1710.03416v6 Theorem 1.1, weak-form conventions and Theorem 1.11; paper 67 v1 Sections 3.2–3.3 and references [4]–[6].
COMPARISON: Primary coverage includes parameter two, a fixed ladder-local-time convention, a nonnegative occupation representation and a signed bounded-data boundary upper estimate. It does not directly state paper 67's normalized signed trace identity; that specialization and its absolute-potential identification remain a separate audit.
GAP: Independently audit the factor-two time normalization, exact renewal asymptotic, signed Green identification with the half-line extension, and passage from almost-everywhere representation to a pointwise endpoint limit; keep the stated domain split explicit.
REASON: Essential unread-source coverage is now supplied for a bounded reproduction audit. No trace theorem, new specialization or removal of L512's hypotheses is proved during this literature-only step.
LITERATURE_REASON: The start-of-turn REVIEW_REQUIRED target changes scope from assuming endpoint traces in L512 to assessing their existence and normalization; the essential original sources had not been inspected.
SCOPE: A fixed ell>0 and G=(1/2)log(1-D_x^2); audit paper 67's argument for u in the interval part-operator domain with u and h=G_(0,ell)u bounded, conditional on the stated domain split. This does not cover arbitrary bounded half-line forcing, arithmetic positivity, uniform varying-operator limits or collar resolvents.
COVERED_TARGET: Audit bramble_trace v1 equations (3.11)–(3.19) for u in Dom(G_(0,ell)) with u and G_(0,ell)u bounded, retaining the stated interval-to-half-line domain split.

## Primary theorem scope

[Grzywny–Ryznar, v1](https://arxiv.org/html/1107.0745v1),
Sections 2–3, fix the characteristic exponent log(1+|xi|^alpha),
0<alpha<=2, with Brownian exponent xi^2 and ladder-local-time
constant one. Proposition 3.2 assumes a symmetric non-compound-Poisson
process whose exponent is psi(xi^2), psi complete Bernstein; it gives
a Bernstein renewal function and completely monotone derivative.
The derivative formula includes its constant b: Lemma 4.1's alpha=2
case explicitly has b=1. Do not discard that term.

Proposition 3.5's upper-bound proof states the occupation identity for
nonnegative measurable f, citing Bertoin, *Levy Processes*, Chapter VI,
Theorem 20, p. 176 (the book itself was not inspected). Remark 3.6
assumes the half-line Green function exists and gives
integral_0^R G_+(x,y)dy<=V(x)V(R), x<=R/2. Lemma 4.3 gives
G_+(x,y)=integral_0^x v(s)v(y-x+s)ds for 0<x<y.
Lemma 4.1 includes alpha=2, but supplies comparability, not the exact
leading constant needed here. These statements are adequate kernel
inputs; signed inversion requires additional justification.

[Hernandez-Santamaria–Lopez Rios–Saldana, v2](https://arxiv.org/html/2401.18033v2),
Theorem 1.1, assumes a bounded open set with a uniform exterior sphere
condition, f in L-infinity, and a weak solution u in
H(Omega) intersect L-infinity(R^N), zero outside Omega. It concludes
continuity and |u(x)|<=C ell(dist(x,boundary Omega))^(1/2), where
ell(r)=1/|log(min(r,0.1))|. The operator symbol is 2 log|xi|,
not log(1+xi^2). Definitions (1.15)–(1.19) specify the full
zero-extension energy and weak pairing. Section 4's proof treats u
and -u using barriers and a small-domain maximum principle; it imposes
no sign on f or u and no global positivity assumption. It gives no
normalized trace limit. The interval satisfies the geometric hypothesis;
the operator and weak-form comparison must still be checked.

[Chen–Weth, v6](https://arxiv.org/html/1710.03416v6),
Theorem 1.1(ii), identifies symbol 2 log|xi| on compactly supported
Holder functions. Section 1's energy definitions and Section 3,
equations (3.9)–(3.11), define zero-exterior weak solutions through
the full form, not merely the nonnegative short-range energy.
Theorem 1.11 gives continuity and decay with every exponent below
1/2 for bounded weak solutions with bounded forcing on Lipschitz
exterior-sphere domains. It does not replace the later sharp estimate
or provide the trace identity. Positivity needed for existence by
Riesz representation is distinct from regularity of a given solution.

## Manuscript interface and separate audit

[Paper 67 v1](https://rstation.ai/problems/riemann_hypothesis/papers/67),
27 October 2026, Sections 3.2–3.3, is readable at the canonical page;
the /v1 page failed. Its reported rescaling is kappa=kappa_GR/sqrt(2),
V=sqrt(2)V_GR, v=sqrt(2)v_GR and Green kernel twice GR's.
Equations (3.13)–(3.15) supply the exact renewal asymptotic through
a Laplace argument, beyond the cited comparability result.

Its bounded data are u and interval forcing h. The extended forcing g
in (3.16) may be logarithmically singular just beyond ell; the source
claims g in L1 intersect L2 and exponential decay. It uses the domain
split and a zero-kernel spectral-semigroup argument in (3.17), then
absolute Green-potential bounds in (3.18) to obtain (3.19).
This is the manuscript's signed specialization, not a signed theorem
imported directly from GR. No assertion that g is globally bounded
is licensed. Its normalization, integrability, inversion and
representative arguments are reserved for the covered audit.

The source inputs have now been located; no access blocker remains.
This is source-coverage progress, not independent verification of the
trace identity. No lemma or mathematical script is changed.

## Audit test and remaining gap

The next audit must distinguish an available theorem from its
application. Check its listed domain and boundedness assumptions;
verify the normalization against the inspected local-time convention;
justify all absolute integrals before using signed occupation or
Fubini; and justify the endpoint limit for a continuous representative,
including zero traces and complex data. Do not infer a limit from
an upper bound. Standard spectral, Tonelli and dominated-convergence
theorems may be cited with their actual hypotheses. Audit reproduction
is justified because L512 deliberately retained this analytic input;
reproving the boundary theorem itself is unnecessary.

Continue only if the fixed-interval identity passes under those explicit
hypotheses; otherwise preserve the first failed implication and retain
the corresponding assumption in L512. Do not silently add a spectral
gap to the half-line operator. A full domain-split proof and boundedness
of every full-operator eigenfunction are outside this narrowed audit;
Sections 3.1–3.2 remain external where used.

The main gap remains actual-Xi all-degree positivity. Reliable fixed
endpoint traces could support a later arithmetic flux estimate, but
do not yield cancellation as a ground eigenvalue vanishes. The
[automatic-support stop](../../ATTEMPTS/2026-10-30-weil-automatic-support-propagation-source-stop.md)
and [rank-trace stop](../../ATTEMPTS/2026-10-30-weil-rank-trace-single-pair-scope-stop.md)
remain valid for their stated mechanisms. Near-zero uniformity,
multiple clusters, collar inputs and arithmetic positivity remain open.
There is no justified creative target supplied by this source review.
No cross-notebook input. Full matching Mathlib coverage is unchecked;
no absence claim is made. No novelty follows from the searches.

The prior REVIEW_REQUIRED nomination is superseded only as a source
coverage decision. The newly covered audit is a separate future step,
subject to the supervisor's next-turn approval; none of its conclusions
is approved here.
