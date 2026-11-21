# Actual-density compact-shell residual certificate — reviewed continuation

TARGET: Seek one degree-at-most-13 face-preserving polynomial divergence certificate for v'(E)>0 at every zero of L938's actual density on 1/4<=E<=4.
CHECKED: 2026-11-09
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse step63's completed exact-object, Dirichlet Stein, singular-face divergence and signed-observable searches and specific C938a/L937/L940/L941 failure comparisons; recorded in 2026-11-09-l938-simplex-divergence-source-notes-63.md. No inspected matching signed crossing theorem or finite-degree feasibility guarantee; originality uncertified.
SOURCE_EVIDENCE: Gan–Röllin–Ross https://arxiv.org/pdf/1602.07010v3 Lemma3.1/Theorem3.2; Andres–von Renesse https://arxiv.org/pdf/0903.5085v1 Proposition2.1; Andres2009 https://d-nb.info/994899424/34 Proposition3.7/full cutoff proof printed pp54–55 (PDF pages64–65); Mijoule et al. https://arxiv.org/pdf/2101.05079v2 Definitions3.1–3.2/3.11, Proposition3.3/full proof. Hypotheses/exclusions in step63 notes; primary statements and cutoff proof rechecked in step64; unchanged step46 Laplace coverage reused.
COMPARISON: Known results cover singular-face mean-zero integration identities under explicit boundary conditions, not the actual signed radial response. This actual energy-conditioned law differs from L937's stopped unconditioned coefficient box; it does not assume the stopped global ratio or pointwise balancing properties.
GAP: Derive the exact unnormalized radial identity, specialize the singular-face cutoff framework and certify strict residual positivity at actual density zeros, or produce a rigorous obstruction to this fixed sufficient certificate class. Neither existence nor impossibility is established.
REASON: One new actual-law cancellation mechanism at the finite H2 gap is justified after source review; citation cannot provide the missing sign. Step64 separately reviewed the unchanged target and repaired direct source URLs; its EXPLORE coverage permits one subsequent research attempt, without asserting the missing specialization or sign.
SCOPE: Exactly TARGET with the finite ansatz and stopping rules below. No larger degree/interval/parameter sweep or return to generic covariance bounds. Full/supporting Mathlib coverage unchecked.

The main gap is L030–L032/C032a actual-Xi all-degree mixed positivity.
This intermediate target could supply only the compact-energy part
of the global crossing premise for the ready Laplace route. Below-1/4
and above-4 energies, contacts, parameter endpoint signs, other degrees,
initialization, realization and continuation remain independent gaps.
L939's eventual tail gives no certified onset of 4.

Essential inputs are L019, L938(5)–(10) and L940(1)'s exact Pbar.
L938's analytic k(x)=K(sqrt(x)) is the relevant existing regularity
input; retain all 34 rows, factorials, twelve factors and M_0^12.
C938a and L937/L940/L941 constrain routes; they are not positivity
premises. No cross-notebook input or numerical B_0 sign is required
as a derivative premise. No new lemma or calculation is in this file.

Use the actual unnormalized simplex weight W_E(t) specified in the
source notes. The research attempt must first identify the exact
radial integrand D_E, including every E-dependent prefactor, so that
its integral represents v'(E) with a strictly positive common factor.
This identity is an obligation, not an asserted formula. Do not
differentiate only the normalized conditional expectation and omit
its mass derivative. Prove compact uniform domination for this
differentiation, including t_i=0, from the existing analytic kernel.

The fixed certificate class consists of a single E-independent rational
polynomial field X(t), component degree <=13, equivariant under every
permutation of the twelve coordinates. On sum t_i=1 require sum X_i=0
and X_i=0 on t_i=0 for every i. Choose one scalar affine function
a(E)=a_0+a_1 E with rational coefficients and a rational epsilon>0.
The prospective residual test is

    D_E(t) + div_Delta(W_E X)(t)/W_E(t) - a(E) Pbar(t) >= epsilon

for all interior t and 1/4<=E<=4. This is a proposed sufficient
inequality to investigate, not a derived identity or sign claim.
Intrinsic divergence must be defined in a consistent independent
coordinate chart, with its measure/Jacobian checked against L938(9).
The future proof must justify why the divergence integrates to zero,
why the Pbar term cancels at actual zeros, and why the resulting
strict sign has the stated orientation for v'.

The cumulative-gap source dictionary to check is N=11,beta=6.
Give the transformed field and prove every truncated-face limit,
including endpoint faces and intersections. Multiplication by the
full theta product is a specialization requiring a compact C^1
bound. Do not invoke canonical componentwise Stein-class membership
without checking its stronger derivative conditions. A tailored
face-cutoff proof may be needed even though the general method is
known; reprove only that specialization, not the cited general theorem.

Success requires the exact identity, zero flux and a rigorous uniform
residual certificate with positive margin. Floating-point feasibility,
sampled signs and a formal integration identity do not suffice.
Any polynomial approximation must pay the full theta and derivative
remainders on the entire compact domain; no positivity-completeness
theorem or arbitrary numerical solver is assumed to do this.

A finite positive combination of residual evaluations annihilating
all allowed field and scalar columns and having a certified nonpositive
radial value would be an informative obstruction to this strict
sufficient ansatz. Such a witness must include exact coefficients
and rigorous full-kernel bounds. No such witness has been sought here.
Failure to find a certificate is inconclusive. Stop after one coherent
attempt at this fixed class, preserve partial reasoning and reassess;
do not increase degree, interval or multiplier class in that turn.
Even a rigorous obstruction does not refute all divergence mechanisms,
the actual crossing claim or RH.

Prospective routing: proof_attempt/creative, deep_research/max.
The precise obstruction is the uncontrolled signed radial response
of the actual energy-conditioned law after both global ratio and
pointwise balancing sufficient orders failed. The bounded residual
test would exploit actual-law integral cancellation and could change
the decision on a finite-degree positivity route. This file nominates
that test; step64 supplies the separate source-scope review. Supervisor
routing remains external to this notebook.


## Step64 separate review and URL recovery (9 November 2026)

LITERATURE_REASON: Supervisor-required direct-source-URL repair of the saved ready assessment; unchanged target and assumptions, no repeated discovery search.

Reopened the primary PDFs linked in SOURCE_EVIDENCE and checked the
identified statements against the step63 notes. Andres Proposition3.7
and its complete proof are on printed pp54–55, PDF pages64–65
(one-based); the endpoint faces are explicitly included by reference
to the same argument. Those source cases do not replace the promised
local chart, multiplier and face-intersection verification. Gan's
positive-parameter characterization and Mijoule's compact-support
sufficient condition retain their recorded scope exclusions.

The framework supports a later specialization attempt, not a signed
response theorem or finite-degree existence guarantee. No mathematical
claim, certificate or novelty assessment changed. Keep EXPLORE for the
exact fixed target; this repair is STALLED mathematical progress.
Mathlib remains unchecked. No essential source blocker remains.
