# Actual Mellin interpolation: fixed vertical Rice viability test

TARGET: Test whether L829's actual E admits the unbounded Rice contour for J_d(-1)/gamma_0 by verifying the finite-contour specialization and determining absolute convergence of E(s)d!/product_(k=0)^d(s-k) on Re(s)=-1/4 for each fixed d>=3.
CHECKED: 2026-11-19
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Reuse the exact Jensen/Mellin/Rice searches and local overlap comparison in 2026-11-19-mellin-jensen-contour-source-notes-1656.md. L718 treats another size interpolation; L829's completed fixed diagnostic supplies no vertical test. No inspected ready duplicate of this exact calculation was located; no originality claim.
SOURCE_EVIDENCE: Flajolet--Sedgewick, TCS144(1995),101--124, Section2 Lemma1/(6)--(7), pp104--105, Section4 Theorem2/proof pp110--111, https://algo.inria.fr/flajolet/Publications/FlSe95.pdf ; DLMF5.11.9 https://dlmf.nist.gov/5.11.E9 and5.5.5 https://dlmf.nist.gov/5.5.E5 . Hypotheses and inspected proof cases are in source-notes1656; reuse assessment647's actual-E factorial interface and C048j's audited contract.
COMPARISON: Finite Rice representation and vertical gamma asymptotics are known; actual E is already constructed. Citation alone does not compute full weighted growth or verify the shifted I normalization. This is established-route specialization, not a new interpolation theorem or creative mechanism.
GAP: Analytic-domain/sample applicability, finite orientation, shifted I/S applicability, vertical growth and absolute integrability need verification. No growth rate, convergence, divergence, closing-arc estimate, degree-uniform sign or height estimate is established here.
REASON: One fixed-line calculation can independently stop an invalid contour opening or isolate its next condition before signs work. Coverage is adequate; this newly ready continuation receives separate approval next turn before research. No calculation was performed in preparing it.
SCOPE: Exact TARGET with L829's normalized actual E, c=-1/4, x=-1 and each integer d>=3 fixed during |Im(s)| tending to infinity. REPRODUCTION only; no interpolation uniqueness, conditional Bernstein membership, opening from convergence alone or moving-degree asymptotics.

## Inputs and purpose

The central gap remains L030--L032/C032a. C028b specifies J_d, R_d
and the H_d=o(d) criterion; C028g leaves S_F=0 open. This is only
a viability gate for a coefficient-contour mechanism that might later
support a degree-dependent signed comparison, with no height saving
following from a pass.

Reuse L828 Section2's unconditional density/entire construction and
L829's hypotheses, L019/L021 moments and assessment647's factorial
interface. Use precisely L829's E, M, M(0) and density normalization.
No conditional complete-Bernstein representation or finished derivative
diagnostic is growth evidence. Retain C048j's factor2 in I.

C048a supplies the principal W branch and continued I; C048j supplies
the audited full relative bound and explicit S. Verify p=s+1/2 and
the large-modulus sector; retain the compact remainder exactly.
For the Lambert factor use w exp(w)=2p/pi and C048a's branch bounds,
without an unproved growing-shift expansion. Import DLMF5.11.9 for
bounded real gamma arguments and5.5.5 within their stated domains.
No general gamma or Rice theorem reproof is needed.

## Bounded test and decision

Verify the finite Rice template for the actual samples at x=-1 on
a positive rectangle about 0,...,d, with left edge c=-1/4, right
edge d+1/2 and finite height T>0. Write residues, normalization and
orientation explicitly. No horizontal or right edge may be silently
discarded in a later limiting operation.

Determine the large-|t| logarithmic growth of

    E(c+it)d!/product_(k=0)^d(c+it-k), c=-1/4,

and decide absolute integrability over real t for each fixed d>=3.
A strictly positive exponential lower rate or another rigorous
divergent lower bound abandons this specific absolute vertical opening.
An integrable upper bound passes only its first gate. Closing arcs,
degree-uniform signs and zero-height conversion remain separate.
If a zero exponential rate is inconclusive, name the exact missing
slower bound and stop. No upper bound alone proves divergence.

L718's noninteger-size pole accumulation is a different obstruction.
The existing actual Cauchy circle in Ono2610.38870v1/(2.9),
assessment1344 and C019c/d is a separate representation; do not
reopen its edge signs or relabel existing results. Preserve the
global-import and endpoint-loop stops and L829's completed diagnostic.

Any justified canonical research result needs exact hypotheses, full
finite-contour/asymptotic reasoning and Mathlib status. Matching coverage
is unchecked. No script is required for this analytic calculation.
The route is calculation/standard/high, not a creative proof attempt.
