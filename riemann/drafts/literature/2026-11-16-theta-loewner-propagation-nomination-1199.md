# Theta differential propagation — completed source review1200

TARGET: Assess a theta-derived Loewner differential inequality H_N^epsilon'(t)+C_N(t)H_N^epsilon(t)>=0, with locally integrable C_N independent of inverse eigenvalue bounds, screening N=2 before any degree-uniform propagation claim.
CHECKED: 2026-11-16
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1200 searched exact Xi heat-trace/differential-inequality/Hankel, theta/Hankel/Loewner/propagation and null-eigenvector terminology; compared scoped stops1117/1181/1193, L727, the October30 nullvector/direct-theta assessments and November5 theta-adjoint stop. No matching coefficient theorem was identified; queries and primary passages below, without novelty or impossibility claims.
SOURCE_EVIDENCE: Read Abdillah viXra2609.0027v1 Sections5.3-5.5/(5.11)-(5.20),7.4-7.10/(7.12)-(7.33),7.13-7.15/(7.38)-(7.44),8.1-8.7/(8.1)-(8.16),9.1-9.2/(9.1)-(9.7), pp17-18,24-31; Li-Zhang2024 DOI10.1007/s00526-024-02668-x Theorem1.1 and Section3.1 entire proof/(3.1)-(3.4), Section3.2 opening growth qualification; Polson1708.02653v24 Theorem12.5/entire proof p39, Theorem5.3/(5)-(6)/entire proof p9, TheoremA p3 and Section6.3 p15. Reused unchanged assessments1117/1198.
COMPARISON: The theta source has a boundary-coupled signed resolvent kernel, not a heat-block evolution inequality; its operator identity retains the original kernel and a signed defect. Matrix Harnack needs a positive heat solution, Ricci-flow geometry, curvature bounds and a verified null-eigenvector reaction sign, with no supplied realization for W's derivative blocks. Neither source supplies C_N.
GAP: No specific signed theta input or independent locally integrable C_N emerged, even for N=2. Park propagation. A separate scalar-resolvent source-overlap audit is nominated; it neither pays this coefficient gap nor propagates all-degree positivity.
REASON: New primary-source scope evidence fails the continuation test and changes routing, an informative source-application NEGATIVE rather than a mathematical counterexample. No inequality was derived or tested; finite-block and boundary-forcing stops remain preserved.
LITERATURE_REASON: Supplied nomination1199 was REVIEW_REQUIRED and lacked essential primary coverage for this differential comparison; this completes that comparison rather than extending ready scalar-audit coverage.
SCOPE: Completed literature-only comparison for the exact TARGET and both actual-W blocks, N=2 as proposed screen. No mathematical attempt, lemma/script write, propagation theorem or coefficient bound. Original nomination paragraphs below are historical; this completion supersedes their pending-review wording.

The main gap is actual-Xi Q(q)>=0 for every degree. A plausible use
of the proposed differential inequality is propagation of the imported
near-time block signs through arbitrary positive times, followed by the
already recorded finite heat-to-moment transfer separately at each N.
C_N may depend on N and t, but needs a specified locally integrable
bound on every compact subinterval of t>0. It may not be defined by
dividing by an unproved positive least eigenvalue, by a zero-free
premise, or by the desired quadratic-form sign. No differential
inequality or propagation theorem is proved here.

Continuation test: locate an exact signed theta/arithmetic identity
or theorem supporting such an explicit comparison, then nominate only
its bounded N=2 screen for separate approval. Restating positivity,
controlling individual entries or citing finite signs does not qualify.
If no specific input emerges, abandon this mechanism after the bounded
comparison. Even a passed N=2 screen leaves arbitrary N, analytic
propagation hypotheses, all-degree signs and graph realization open.

Compare stops1117/1181/1193, L727's first-sign work and existing
nullvector/moment-flow failures before a research nomination. Polson
v24 Theorem12.5's finite-block countermodels and their changed arithmetic
term in Theorem12.2(vi) are essential negative controls, not blanket
prohibitions. The proposal must use a specific exact arithmetic input
absent from those controls; renaming cannot reopen a stopped mechanism.
Locate relevant claims before narrowly reading their proofs. No
cross-notebook input is proposed.

Creative routing is not yet justified: the signed identity, source
coverage and discriminating finite test are missing. If comparison
supplies them, nominate proof_attempt/creative with the precise
obstruction and bounded test for separate approval. Full matching
Mathlib coverage is unchecked. This nomination does not approve work.

## Completed comparison — 16 November2026, step1200

The bounded search checked three interfaces: exact theta differential
structure, matrix comparison, and the arithmetic finite-block theorem.
None passes the specified signed-input continuation test.

**Theta interface.** Agum Abdillah, *A Theta-Geometric Framework for the
Hankel Positivity Problem in the Riemann Hypothesis*,
[viXra2609.0027v1](https://vixra.org/pdf/2609.0027v1.pdf), September2026,
40pp, uses x=r^2>0 and density Phi(u)cosh(ru)/A(r). Sections7.4-7.10,
pp24-26, retain the endpoint contribution
(f'(0)Y(0)-f(0)Y'(0))/2; its shorter adjoint formula requires both
test traces zero. Sections8.2-8.7, pp29-30, give
(L_y L_z-c^2)K=8, c=1-1/(4r^2), but retain K and a signed defect,
including K(0,z)=z*tanh(z)-z^2. No positive bulk completion or
propagation theorem is asserted. Sections9.1-9.2, pp30-31, retain
the all-orders gap. These are resolvent identities in r and the theta
integration variables, not an equation for heat-time derivative blocks.
No transfer or coefficient bound is imported. The integration-by-parts,
boundary and operator-identity cases were inspected; their algebra and
upstream results were not independently audited.

**Matrix interface.** Xiaolong Li and Qi S. Zhang, *Matrix Li-Yau-Hamilton
estimates under Ricci flow and parabolic frequency*, Calc.Var.63,63
(26February2024), [version of record](https://doi.org/10.1007/s00526-024-02668-x),
Theorem1.1, assumes a complete Ricci flow, positive heat solution,
nonnegative sectional curvature and Ric<=kappa*g, kappa>0. It concludes
Hess(log u)+kappa/(1-exp(-2kappa*t))*g>=0. Section3.1's whole compact-case
proof derives a reaction inequality and checks it on null eigenvectors;
Section3.2 discusses growth/derivative control in the noncompact argument.
That full noncompact proof was not read or imported. No geometric heat
solution, tensor identification or reaction sign has been supplied for
H_N^epsilon. Smooth entries verify none of these missing premises.
This applicability failure is not a counterexample to another theorem.

**Arithmetic interface and duplicates.** Reuse C030b, C030j and
assessment1198: their theorem retains growing verification height and
supplies no differential comparison. Polson,
[*On Hilbert's 8th Problem*,1708.02653v24](https://arxiv.org/pdf/1708.02653v24),
Theorem12.5 p39 was rechecked, including N=1 and special N=3 cases;
reuse comparison1117's Theorem12.2(vi)/(53), pp36-37, for the changed
arithmetic term. These countermodels obstruct finite-input inference,
not an actual arithmetic identity. Stops1181/1193 do not prohibit a
new signed input; none emerged here.

L727's conclusion/(5) and signed-transfer audit leave its local-head
margin unknown; it is also a spatial Xi comparison, not heat-time
block propagation. The October30 nullvector arithmetic screen retains
its unpaid signed prime slope; the November5 theta-adjoint stop retains
boundary/forcing obligations. These are relevant overlaps, not blanket
bans. Reused their adequate primary comparisons without repeating
their proofs. No cross-notebook theorem is used.

Queries included `"Polson" "1708.02653" theta heat Hankel`,
`"Hankel" "differential inequality" "theta" Riemann`,
`"theta" "Hankel" "Loewner" Riemann`,
`"Xi" "heat trace" "differential inequality" Hankel`,
`"theta" "Hankel" "propagation" positivity`, and
`"Hankel" "null eigenvector" positivity differential`.
Uninspected hits are not theorem evidence. An initial notebook-local
search returned too much output; subsequent reads used exact paths and
ranges. No truncation was used to verify a claim.

**Decision.** Park propagation: its signed-input test was not met.
No mathematical falsity or nonexistence theorem is claimed. A different,
independently testable overlap issue emerged: compare the theta source's
scalar first-derivative problem (8.16) with the positive heat-trace
Laplace representation. This is a proposed reliability audit, not a
proved overlap or a new positivity mechanism. Its separate assessment is
`2026-11-16-theta-resolvent-overlap-audit-1200.md`; no specialization
is performed this turn. A creative central attempt remains blocked by
the absent signed heat-block input, not source access or a historical
global ban. Full Mathlib coverage is unchecked. Primary web text was
accessible; shell DNS and two screenshot requests failed. Unseen images
are not evidence.
