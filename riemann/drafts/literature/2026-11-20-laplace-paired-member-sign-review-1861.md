# Complete paired-member determinant sign — review1862 of nomination1861

TARGET: Review source coverage for a nonpositive symmetrized determinant of two complete real even Gaussian divisor members, retaining C034c's origin subtractions and C034f/g's contour terms, for sigma in [1,2], both ordinates >14, |delta|<1/2, and delta=0 through height100.
CHECKED: 2026-11-20
DECISION: EXPLORE
SEARCH_EVIDENCE: Review1862 completed nine exact/standard-term searches and the narrow November20 Laplace duplicate/failure comparison; queries and inspected ranges are in drafts/literature/2026-11-20-laplace-paired-member-source-notes-1862.md. No applicable complete-member sign theorem was found; no novelty inference.
SOURCE_EVIDENCE: Yang--Tian arXiv:1803.02513v1 Theorem2 pp4-5, positive-denominator and endpoint proof cases pp5-8, Theorem3 p9; Mao--Tian arXiv:2306.04659v1 CW11/CW12 pp2-3, rule2.4 p7 and rule2.5 statement/proof pp7-8. These are scope comparisons, not imports. Reuse Ruzza/Forrester1842, Gaussian/Voigt1846, Galapon1858 and finite-contour/Fubini1854.
COMPARISON: Ratio sign rules require a common positive kernel and proved ratio shape; no such representation is established for the four subtracted member functionals or their unequal-pair expression. C034c(21) covers absolute expansion; C034f/g cover retained core and corrections, not their total sign. Stops1843/1847 test spatial signs, not the completely integrated member pair.
GAP: Uniform P_sigma(z,w)<=0, including diagonal, unequal, low real and displaced high members, remains unproved and untested. Neither Gaussian TP nor contour convergence pays this sign or the S4^3/5 threshold.
REASON: The completed comparison supplies adequate tool coverage for one independently testable stronger sufficient mechanism, without a matching imported inequality or essential source blocker. A later uniform proof or certified admissible positive pair discriminates it; no dependent mathematics was done in review1862.
SCOPE: Completed literature-only review of the exact pair sign question below. The concrete mathematical continuation is separately nominated in 2026-11-20-laplace-paired-member-sign-attempt-1862.md; no sign proof, script, scalar-formula project or repeat representation audit was performed.

LITERATURE_REASON: the target changes from validity of a linear contour
representation to the sign of a completely integrated two-member
determinant. Reuse existing integration/finite-part sources; inspect
only essential determinant-sign coverage and obstructions.

## Precise proposed test, not a result

The main gap is L030-L032/C032a actual-Xi all-degree positivity. The
intermediate gap is C034c(20)'s upper bound C<=S4^3/5, sufficient for
the final Laplace-width prefix. Independent realization, height,
conditioning, weight and observation gaps remain after that bound.

Use C034c's real even member, with z=gamma-i*delta,

    h_z(x)=Re([G_sigma(x-z)+G_sigma(x+z)]/2),
    D_j(z)=int_0^infinity (h_z(x)-h_z(0))*Q_j(x) dx,
    E_j(z)=int_0^infinity (h_z''(x)-h_z''(0))*Q_j(x) dx.

These are the existing member integrals of C034c(21). The proposed
object for comparison is the symmetrized determinant

    P_sigma(z,w)=[D_1(z)E_2(w)+D_1(w)E_2(z)
                    -D_2(z)E_1(w)-D_2(w)E_1(z)]/2.

The proposed stronger sufficient inequality is P_sigma(z,w)<=0 for
all sigma in [1,2] and both admissible members: ordinates >14,
|delta|<1/2, and delta=0 when the ordinate is <=100. This last
restriction retains the inherited verified-height qualification;
it is not newly verified here. Diagonal and unequal pairs, both
displacement signs, even translates, conjugation and every multiplicity
must be retained. No individual divergent half-interval integral is
used. The desired use is assembly by C034c(21) to control C at(20).
This paragraph nominates a target, not a derived sign theorem.

The discriminating mathematical test, only after source approval,
is a uniform proof of this inequality or a rigorously certified
admissible pair with P_sigma>0. A positive pair would reject this
stronger pairwise mechanism, not the actual total curvature bound
or RH. Samples alone would be exploration, not either verdict.
A representation-only rewrite or independent unsigned D/E bounds
would not meet the test. No repeated contour audit is proposed.

The distinction from stops1843/1847 is the order of the sign question:
keep the complete signed integral of each even member, including
origin and contour corrections, before testing pairs of divisor
parameters. No spatial profile is assumed positive or ordered. The
audit is newly completed, but it does not itself justify this sign.
The nomination's narrow local search was incomplete; review1862's
source notes now complete the bounded duplicate/source comparison.

## Source scope and continuation

Check standard terminology and stronger results for Gaussian-regularized
finite-part rational kernels and determinant/composition sign criteria,
including their hypotheses on real arguments, positive measures and
complex displacement. Reuse1842/1846/1854/1858 where their scope is
unchanged. Retrieve primary hypotheses and essential proof cases;
do not infer a sign from heat regularity, ordinary Gaussian total
positivity, Galapon's contour identity or C034e's spatial core sign.
Approve at most one concrete bounded mathematical target after this
comparison, or record the exact obstruction and choose another test.

Essential inputs: C034g with C034f, C034d/e, C034c(16)-(21), C034b
and C032n(8)-(9)/(13). C032m/C033w through C033l/C032q retain the
probability context. Preserve the actual divisor/conjugation/multiplicity,
ordinate0 exclusion, strict strip/gamma>14, count, through100/retained
real zero, reciprocal-square tail, heat positivity/separate fixed-j
errors, both fixed-v1 inputs, zero drift/killing and Gaussian
half-variance, with uniformity on [1/2,3] where limits require it.
Keep even origin pairs and quadratic subtractions. Source-wide and
finite-zero validity, global Sobolev membership and full Mathlib
matching remain unverified. Omega, C034c(20), conditioning, entries/m,
weights, TV<=2, full observations, signed height/cancellation and Xi
realization remain unpaid. Preserve stops1839/1843/1847 and
1746/1798/1823/1832/1837.

The preceding nomination text records the question at invocation1861.
Review1862 is now complete; its evidence, precise source hypotheses,
unimported leads and retained qualifications are in
[source-notes1862](2026-11-20-laplace-paired-member-source-notes-1862.md).
It found no applicable sign theorem and authorizes preparing one
EXPLORE continuation, not asserting its sign. The newly written
attempt1862 assessment requires separate approval next turn. Central
realization/signed-height coverage is still missing; do not relabel
this intermediate development as creative for scheduling. No lemma,
mathematical script, PROOF or DAG was changed in the literature step.
