# Mesh-restricted diagonal transfer — source comparison, step488

TARGET: Assess whether finite diagonal stability on simple positive-rooted polynomials with a prescribed lower consecutive-root ratio admits nonhyperbolic binomial symbols and gives a degree-explicit residual tolerance beyond L792's constant pencil.
CHECKED: 2026-11-05
DECISION: SPECIALIZE
SEARCH_EVIDENCE: New bounded q-separated-multiplier and coefficient-perturbation searches located Lamprecht 1210.1102v1 and Leake--Ryder 1712.02499v1; primary cases and local step484/485/487 records inspected below. No exact residual tolerance located; no absence or novelty claim.
SOURCE_EVIDENCE: Lamprecht 1210.1102v1 (3 October 2012), pp.2--5 definitions/Theorem4, pp.21--22 Theorem27/full proof, pp.26--28 Theorem31/full proof, Lemma32/full proof and proof of Theorem4; versioned HTML resolves closure bars lost in PDF extraction. Leake--Ryder 1712.02499v1 (7 December 2017), pp.1--3 conventions/Theorems1.2,1.7 and pp.15--16 Corollary1.2/full limiting proof.
COMPARISON: Restricted-class classification uses a q-binomial symbol and preserves the same mesh, unlike ordinary-binomial universal preservation. Its nonextremal strict-log-concavity consequence gives an exact prefix-admissibility test, not a residual tolerance or growing-degree Xi estimate. C792a/L792 retain their scopes.
GAP: No inspected theorem supplies epsilon(d,Q) allowing arbitrary small coefficient residuals while retaining positive roots with mesh loss. Matched-prefix same-mesh application is unperformed; growing-degree model existence/separation and actual signed control remain independent gaps.
REASON: Park direct quantitative import from q-classification; its equality/extremal cases supply one independently testable restricted-class admissibility target. No failure of mesh-losing or family-specific transfer is inferred.
LITERATURE_REASON: Changed input hypothesis from universal preservation to separated positive roots; essential restricted-class theorems were unread at entry.
SCOPE: Completed literature-only step488; no lemma/script writes, tolerance derivation, q-prefix application or degree sweep. The new SPECIALIZE continuation needs separate approval before mathematics.

## Completed review — 5 November 2026

Main gap: actual-Xi all-degree mixed positivity. Intermediate aim:
separated-model transfer with a degree-explicit residual tolerance.
Downstream use still needs growing-degree models, their separation and
actual signed residual estimates. Stop direct source import if it only
requires another root-location premise or gives no quantitative tolerance.
The inspected classification meets that stop test, without ruling out
the weaker transfer problem.

### Primary statements and proof cases

Martin Lamprecht, [*Suffridge's Convolution Theorem for Polynomials and
Entire Functions Having Only Real Zeros*, arXiv:1210.1102v1](https://arxiv.org/html/1210.1102v1),
3 October 2012 ([PDF](https://arxiv.org/pdf/1210.1102v1)),
pp.2--5, 21--22, 26--28. For 0<q<1 write

R_d(q;z)=prod_(j=0)^(d-1)(1+q^j z)=sum C_j^d(q)z^j,
C_j^d(q)=q^(j(j-1)/2) prod_(i=1)^j (1-q^(d-j+i))/(1-q^i).

N_d(q) allows nonpositive roots with strict same-sign ratios <q;
bar(N_d(q)) denotes its closure. Source conventions include zero
polynomials and zero roots. PN_d(q) consists of f with
f*R_d(q) in N_d(q), where * multiplies ordinary coefficients.
Theorem4(b): M(N_d(q))=bar(PN_d(q)). Theorem4(c), Theorem27
and the proof of Theorem4 give strict coefficient log-concavity for
nonextremal members of the closed pre-coefficient class. Extremality
means f*R_d(q;z)=a R_d(q;b z), with nonzero real a,b.

Inspected Theorem31(b)'s sufficient/necessary cases, (c)'s strictification
with 0<r<q, and Theorem27's full quadratic reduction, including zero
coefficients and both root-sign cases. Lemma32's converse is existential
as q tends to zero, with separate zero-coefficient asymptotics; it gives
no epsilon(d,Q). No q-prefix application is derived here.

Jonathan Leake and Nick Ryder,
[*Connecting the q-Multiplicative Convolution and the Finite Difference
Convolution*, arXiv:1712.02499v1](https://arxiv.org/pdf/1712.02499v1),
7 December 2017, pp.1--3, 15--16. Definition1.1/Theorem1.2 use q>1,
nonnegative roots and weak logarithmic mesh at least q. Their convolution
weights ordinary coefficients by
(-1)^j q^(-j(j-1)/2)/[d choose j]_q. Theorem1.7 assumes both
full-degree inputs already have the mesh. Read Corollary1.2's entire
positive-root argument and extension by roots tending to zero/infinity.
These confirm boundary/degree qualifications, not a coefficient
perturbation radius. Their conventions are not silently identified with
Lamprecht's.

### Applicability, searches and decision

For positive roots rho_(i+1)/rho_i>=Q>1, comparison uses Lamprecht
q=1/Q and reflection z=-y; a real diagonal operator commutes with
reflection. Preserve weak versus strict separation. Full-degree positive
inputs and nonzero images require justification when a source class also
allows lower degrees, zero roots or the zero polynomial. The source
q-symbol sum C_j^d(q)c_j z^j differs from the ordinary symbol
sum binom(d,j)c_j z^j of C792a. Its criterion does not require ordinary
symbol hyperbolicity. That distinction alone neither exhibits an
admissible nonhyperbolic ordinary symbol nor supplies a residual norm
tolerance. Replacing unpaid ordinary-symbol roots by unpaid q-symbol
roots would not meet the target.

The exact matched prefix c_0=...=c_4=1, 0<c_5<1 now has a source-backed
equality/extremal test. Its application is deliberately left unproved
until separate approval and a mathematical turn. Even a negative answer
would concern the same mesh, not positive-root retention with mesh loss.

Executed queries included `q separated zeros multiplier sequences
diagonal operators finite Lamprecht theorem`; `logarithmic mesh Schur
Szego convolution q multiplier sequences coefficient perturbation`;
`real rooted polynomial relative coefficient perturbation logarithmic
mesh explicit bound roots Rouche`; `q separated roots coefficient
perturbation stability diagonal operator real rooted quantitative`;
`polynomial coefficientwise Rouche bound roots`; and `Lamprecht
perturbation roots`. Componentwise-condition-number searches returned
numerical sensitivity/Hurwitz-stability leads, not inspected matching
finite residual theorems. Snippets/unread leads support no conclusion.
The search is bounded, not exhaustive.

Read step484's central discovery comparison and step484/485/487 histories;
C792a's hypotheses/conclusion/proof and needed L791/L792 model and
normalization ranges; prescribed-primitive and central-wedge source stops.
A filename search for mesh/q-separated/Lamprecht and root perturbation
found only this nomination in local drafts/history/attempts. No novelty
inference follows. Initial notebook status/search output was oversized;
subsequent targeted records supply the mathematical comparisons.

PDF extraction lost closure bars; versioned arXiv HTML resolved them.
Local curl DNS failed but web access succeeded. The Leake--Ryder v2 URL
returned404; the inspected PDF is v1. No essential source remains blocked.
Mathlib matching coverage is unchecked; no absence is inferred.

NEGATIVE: park direct quantitative import from this classification.
New source coverage supports the
[separate prefix-admissibility test](2026-11-05-same-mesh-prefix-admissibility.md),
not its conclusion. This is local route evidence, not a new theorem or
actual-Xi sign. No mathematical exploration budget was spent/reset.
PROOF/DAG and unfinished work stay unchanged. Missing independent signed
control blocks a justified central creative target; the next ordinary
specialization is not labeled creative.

## Original nomination, retained as entry scope

For this nomination, order the roots 0<rho_1<...<rho_d and prescribe
rho_(i+1)/rho_i>=Q>1. Determine whether a theorem for that class can
allow a nonhyperbolic *ordinary* binomial symbol. If a source uses
q-binomial coefficients, another convolution, a different root sign
class or strict rather than weak separation, preserve those distinctions
and justify any eventual translation; no identification is assumed.

Bound the review to the restricted-class multiplier/perturbation lead.
Search terms to test include finite q-separated multiplier sequences,
diagonal operators on logarithmically separated roots, and quantitative
root stability under coefficient multipliers. These are planned queries,
not completed search evidence. Follow primary references only as needed
to obtain one exact sufficient condition with its degree dependence, or
a precise obstruction showing that it supplies no different test.

The continuation test is whether the inspected theorem yields a
nonvacuous, explicitly stated tolerance depending on d and Q for a
residual that need not have a real-rooted ordinary binomial symbol.
If it assumes the missing universal-symbol property, only restates
root reality, or supplies no usable quantitative condition, stop this
lead rather than perform another finite degree sweep. Do not derive
that tolerance or test it mathematically during the coverage turn.

Plausible downstream use is a family-specific transfer criterion for
central matched models. Such a criterion would still require independent
growing-degree model existence, a suitable separation estimate and
actual signed residual bounds. None is available from the present audit.
Even success would not establish actual all-degree mixed positivity.

Essential local inputs are C792a and L791/L792, with inherited
L778/L018/L021/L776 and their exact-data/software qualifications.
L791's five root brackets and L792's margins are fixed-degree evidence,
not a uniform mesh or residual estimate. The new scope must be compared
with step484's universal/mesh observations and the recorded finite-pencil,
prescribed-primitive and eventual-shift stops before approval. No
cross-notebook input is proposed. Mathlib matching coverage is unchecked.

A creative mathematical turn is not yet approved. Missing restricted-class
coverage and an independently justified growing-degree signed condition
remain the blocker; source review must first decide whether this proposed
mechanism is more than a reformulation of the existing unpaid estimate.
