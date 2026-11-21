# Actual-theta adjoint Laguerre comparison: completed source review

TARGET: Assess whether L811's exact Laguerre equation yields a closed signed comparison for L795's P_d at x=kappa*d/(log d)^2, retaining actual theta-kernel derivatives and all boundary terms.
CHECKED: 2026-11-05
DECISION: EXPLORE
SEARCH_EVIDENCE: Step565 searched weighted Laguerre adjoints, Pearson closure, forced Sturm comparison, gamma Stein integration by parts and theta/Laguerre differential equations; exact queries and local overlap checks below. No applicable closed signed theta comparison was identified; no novelty or impossibility claim.
SOURCE_EVIDENCE: Inspected live DLMF https://dlmf.nist.gov/18.8 Table18.8.1 rows8–10; Teschl author preliminary PDF https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf (5.43)–(5.45), Lemma5.19/Theorem5.20 and complete proofs pp153,170–171, Theorem3.12/derivation pp83–84; Ley–Reinert–Swan https://arxiv.org/pdf/1408.2998 v3 (2016-03-25), Definitions1–2,(6)–(9),(15)–(21), printed pp4–8 and integration/centering argument. Local inputs and reused assessments below.
COMPARISON: Homogeneous comparison needs actual equations, coefficient inequalities and endpoint data; density adjoints retain integrability, boundary and centering obligations; variation of constants retains forcing. These statements supply no actual-K signed residual estimate at L811's scale. The envelope is not a signed margin.
GAP: An independent signed residual bound, compatible comparison data and nonzero signed reference margin remain unavailable in the reviewed scope. No failure of P_d or impossibility of another adjoint construction is established.
REASON: Informative source-scope NEGATIVE parks automatic closure; reopening needs an explicit actual-theta equation or independently paid forcing/boundary estimate against a known signed margin. Choose an independent validation task rather than repeat source screening.
SCOPE: Literature-only comparison for actual K, integer d>=3, x=kappa*d/(log d)^2, 1<=kappa<=2, L795 normalization and full support. EXPLORE records the bounded search outcome; no new residual calculation is authorized under this Assess target. No lemma or mathematical script changed.

## Original nomination retained

The following nomination preceded step565. Its pending-review wording
is historical; the completed source decision is above and below.

The main gap is actual-Xi all-degree mixed positivity. The proposed
intermediate target is source coverage for a signed comparison obtained
from the exact finite-degree Laguerre equation under theta averaging.
Its possible downstream use is a Sturm or oscillation argument for the
particular actual weighted polynomials. This would require a genuine
closed comparison or a separately controlled residual; an equation
containing an unspecified signed theta transform would not close it.
No conclusion about all-degree positivity follows from writing an
identity, and this nomination derives none.

The review should search the exact weighted-adjoint problem and standard
Laguerre/Sturm terminology, read applicable primary theorem hypotheses
and essential proof cases, and compare the retained theta derivative
terms with the recorded transfer failure. Use at most three concrete
candidate comparison mechanisms. Do not assume a positive auxiliary
energy, a vanishing theta boundary form or an RH-equivalent sign.
The old comparison transform's nonzero boundary datum cannot be removed
by identifying it with actual Xi. The present question concerns P_d;
it does not claim that the historical auxiliary transform has changed.

Continue toward a separately approved mathematical test only if the
review specifies an exact applicable comparison theorem, or an explicit
residual estimate with a falsifiable threshold and a plausible use for
actual P_d. If the proposed closure merely renames an unknown Xi sign,
or the same missing eigenvalue equation, park this direct mechanism and
retain that obstruction. Failure to locate a source alone is not proof
of impossibility or novelty. A changed identity or scale needs its own
coverage; no mathematical derivation is authorized by this nomination.

L019/L021/L795 and the accepted L811 are the essential local material
for the next review. The historical energy-transfer stop is a contrast,
not a theorem input. Other independent gaps remain: signed bulk margins,
scale adequacy, initial degrees, edges and shifted/mixed transfer. Full
matching Mathlib coverage is unchecked. No cross-notebook input is used.

LITERATURE_REASON: The new target asks about signed weighted differential
comparison with kernel derivatives and boundary terms, outside the
accepted exterior-envelope assessment and the earlier real-axis
asymptotic source screen. Essential theorem-level coverage is missing.

This is a new uncovered continuation, requiring a separate literature
turn. The completed step564 audit is independent of its future outcome.

## Completed comparison — 5 November 2026, step565

Main gap: actual-Xi all-degree mixed positivity. The intermediate target
was an applicable signed comparison, potentially useful for oscillation
of the particular theta averages. The acceptance test required either
an applicable theorem or a residual threshold independent of unknown Xi
signs. Neither was supplied by the inspected sources. This is a source-
scope negative, not an impossibility theorem. No new identity was derived.

### Three primary mechanisms

**Homogeneous Laguerre/Sturm comparison.**
[DLMF Table18.8.1](https://dlmf.nist.gov/18.8#T1), row8, gives
z y''+(alpha+1-z)y'+d y=0 for L_d^(alpha); rows9–10 concern
specified transformed Laguerre functions. Alpha=-1/2 and multiplication
by L795's constant fit row8; L811 already has this finite equation.
The statements concern reference functions, not their theta average.

[Teschl](https://www.mat.univie.ac.at/~gerald/ftp/book-ode/ode.pdf),
author preliminary PDF accessed 2026-11-05, p153 (5.45), assumes real
continuous q,r, C1 p and p,r>0 on a compact interval. Lemma5.19 and
Theorem5.20, pp170–171, concern homogeneous solutions
L_j u_j=lambda_j u_j with p_1<=p_0 and
lambda_0 r_0-q_0<=lambda_1 r_1-q_1. At both comparison endpoints,
either the mixed Wronskian or u_0 vanishes. An interior zero of u_1
follows except for proportional solutions; that exception requires
equal comparison coefficients. Read both complete proofs and equality
cases. Theorem3.12, pp83–84, for continuous matrix A and forcing g,
represents a solution by propagated initial data plus
integral Pi(t,s)g(s)ds. Its complete derivation was read; it asserts
no propagator sign and retains the forcing.

For actual P_d no such pair of homogeneous equations, ordered
coefficients and boundary data has been supplied. The compact theorem
does not justify an unbounded-support limit. Retaining an actual
residual would require an additional estimate or a different theorem;
reference root geometry and L811's envelope do not verify these premises.

**Density-adjoint/Stein closure.**
[Ley–Reinert–Swan v3](https://arxiv.org/pdf/1408.2998),
*Stein's method for comparison of univariate distributions*,
25 March2016, printed pp4–8: Definition1 uses a positive interval-supported
density p and differentiable fp with integrable derivative and zero fp
endpoint limits. The operator is T_p f=(fp)'/p. Definition2/(9) also
requires integrable g(fp)' and g'fp and zero endpoint product gfp.
Equations(15)–(18) center the test function by its p-expectation;
the inverse integrates the centered function. Read these definitions,
the integration argument and Section2.5's setup (20)–(21). The source
warns that constants need not belong to the Stein class. No converse
characterization theorem is imported.

L019/L021 give the actual positive law and moments, not all proposed
test-function boundary hypotheses. Its unknown theta expectation in
a centered inverse cannot be treated as independent sign information
about P_d. A classical gamma law changes the averaging measure: matching
a reference equation does not verify the actual density-adjoint premises.
The relevant score/derivative contributions have not been computed or
signed here. In particular no theta boundary term has been assumed zero.

**Forced comparison by variation of constants.**
The exact representation cited above retains the unknown forcing and
initial data. Here neither an actual closed equation, a specified
propagator nor a separately nonzero signed reference margin has been
supplied. Thus it gives no falsifiable numerical threshold for the
actual-K residual at the stated scale. Bounding an unspecified forcing
by an unknown desired sign would restate the missing comparison.

These are citation-level comparisons, not reproofs. Full matching
Mathlib coverage is unchecked. No equation for the averaged polynomial,
residual estimate, eigenvalue realization or sign conclusion is asserted.

### Overlap and evidence

Read canonical L019/L021/L795/L811 for their exact definitions and
qualifications. The September20 comparison-energy transfer audit is a
contrast: its J datum is not a Dirichlet zero at a Xi zero. The current
finite-degree problem does not repair that datum; the old stop is not
a global ban on adjoints. L795's full-support interlacing stop remains.
Step561's uniform real-axis assessment was reused for its signed-margin
limitation; no Bessel/Airy source screen was repeated.

Also read the October31 actual-theta Stein-premise assessment and the
November1 sextic/Stein review: their spatial shape/hazard coverage is
not a signed Laguerre-average transfer. Step502's logarithmic variation-
diminution assessment retains its lower-oscillation gap. These existing
coverage records neither provide the new residual estimate nor need
another broad literature search. No cross-notebook input was used.

Queries included `Laguerre polynomial differential equation adjoint
integral transform Pearson weight Sturm comparison inhomogeneous
residual`; `Laguerre Stein operator gamma distribution integration by
parts boundary differential equation`; `theta kernel Laguerre polynomials
averaged differential equation Riemann Jensen`; `Sturm comparison theorem
inhomogeneous equation residual Green function sign primary`; and
`Ley Reinert Swan Stein method for comparison of univariate distributions
density approach boundary class pdf 2017`. Local searches were limited
to the relevant named theta/adjoint assessments, ATTEMPTS and histories.
The initial oversized scoped git-status output was truncated and was
not used as exhaustive evidence.

The Stein PDF is v3, not the 2017 published pagination. Teschl's PDF
labels itself preliminary; no revision date is asserted. Its landing
page failed, but its theorem PDF was accessible. Associated/exceptional
Laguerre families, a 2026 theta-concavity preprint and the theta/Laguerre
Li-constant formulation are unread search leads, not theorem inputs.
No source-access blocker remains for the statements actually used.
Nonmatches establish neither novelty nor nonexistence.

### Decision and continuation

NEGATIVE: park automatic signed closure until an explicit actual-theta
equation or independently paid forcing/boundary estimate against a known
signed margin is supplied. This supplies precise source-hypothesis
evidence absent from the former nomination; actual-Xi signs remain open.
The source stop is recorded separately without a new mathematical claim.

A narrow continuation check found canonical L809 already records its
step557 audit, despite the older overview label. Do not repeat it.
L806's all-n,d classification remains unaudited in its canonical file
and step545 history. Nominate its independent audit using the ready
derivative-sign sources, under a separately saved audit scope. This
validates a domain restriction and does not reopen the stopped sign-only
mechanism. A creative central-gap target still lacks an independently
justified signed bridge; no creative label is manufactured. The new
audit scope needs separate approval next turn. No lemma, mathematical
script, PROOF or DAG was modified.
