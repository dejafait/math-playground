# Auxiliary polynomial BRST Ward test — working record

## Preflight, relevance and discriminating test

Read the shared GOAL.md and PROMPT.md, local GOAL.md and PROGRESS.md,
the whole PROOF.md overview and DAG.md, the saved SPECIALIZE assessment
in drafts/literature/2026-10-03-auxiliary-brst-ward-identity.md, L013,
the preceding covariance record, and relevant L003 cochain hypotheses.
The unchanged assessment covers exactly the saved action. Reuse its
Gaussian, Fourier and Berezin inputs; this is one mathematical
specialization, with no further literature retrieval. Existing local
overview changes, L013 and its script and source notes are preserved.

The gap is a justified free Ward identity for polynomial auxiliary and
ghost insertions in the ordered finite-cochain prescription. Its plausible
use is a legitimate free starting point before attempting a nonlinear or
physical-boundary Ward formulation. Exact polynomial convergence and
vanishing of the regulator breaking insertion would justify continuing;
an undefined extension, sign inconsistency or surviving breaking term
would stop this realization. L003's cochain positivity and L013's
connection covariance are inputs, not targets to reproduce again.
L012's strong smooth-domain counterexample and the exhausted bulk-locality
route remain preserved.

Even success here would supply no interacting error estimate. The required
matched reflected error <= c_box/2, finite matching on a specified coupling
trajectory, physical-boundary subtraction and remainder, field
construction, limiting reflection positivity, infrared removal and finite
positive mass remain unresolved.

## Reasoning saved before completion

For one colour put delta = D*, H_epsilon = L1 + epsilon I and

\[
S_\epsilon=\tfrac12\|EA\|^2+\tfrac12\|b\|^2
-i(b,\delta A)+(\bar c,L_0c)+\tfrac\epsilon2\|A\|^2.
\]

The candidate odd left derivation is sA = Dc, sc = sb = 0,
s bar c = i b. Its unregulated action variations cancel. At epsilon > 0,
every Grassmann coefficient has absolutely convergent bosonic integrals,
so ordinary A integration by parts and finite Berezin differentiation
should give, for parity-homogeneous P,

\[
\langle sP\rangle_\epsilon
=(-1)^{|P|}\epsilon\langle P(\delta A,c)\rangle_\epsilon.
\]

At fixed A, integrating any b polynomial against its Gaussian Fourier
factor gives a polynomial in delta A times exp(-||delta A||^2/2).
Finite ghost integration leaves another polynomial. Consequently the
ordered polynomial integral has the positive connection Hessian
H_epsilon after those integrations, including at epsilon = 0.
Dominated convergence using L1 > 0 is the candidate removal argument;
it must apply to P(delta A,c) as well as P. A bare epsilon alone is
insufficient.

The expected mixed bosonic covariance blocks are H_epsilon^-1,
i H_epsilon^-1 D and I - delta H_epsilon^-1 D. Since
H_epsilon D = D(L0 + epsilon I), the last block should be
epsilon(L0 + epsilon I)^-1. The ghost order matters:
<bar c_i c_j> should be -(L0^-1)_(ji). These signs and two mixed
antighost witnesses require checking before recording the completed proof.
No joint unregulated absolute integral, positive auxiliary measure,
mesh-uniform estimate or nonlinear forest-measure replacement is claimed.

## Completed result and decision

[L014](../lemmas/L014-auxiliary-polynomial-free-brst-ward.md) contains
the full all-polynomial, all-fixed-mesh proof. The polynomial extension
is well defined by the unchanged integration order. Every transformed
numerator is a polynomial against L1 + epsilon I, with one fixed-mesh
Gaussian dominating it for 0 <= epsilon <= 1. Positive normalization
therefore gives convergence of all normalized polynomial expectations,
including the breaking insertion. Its expectation is bounded before
multiplication by epsilon. Regulated joint integration by parts and the
left graded product rule then prove the exact modified identity and its
zero-regulator Ward limit.

The two mixed antighost tests detect the imaginary auxiliary convention,
ghost order and parity sign. They have nonzero breaking at positive
epsilon and vanish at epsilon = 0. The normalized pure auxiliary
covariance tends to zero while the mixed A,b covariance does not;
imposing b = 0 would lose valid insertions. The ordered zero-regulator
functional remains complex and its original joint modulus remains
nonintegrable. No contour shift, strong connection boundary condition,
continuum trace, ultraviolet interchange or nonlinear replacement is used.

Outcome: ADVANCE, RESEARCH / REPRODUCTION. This closes the specified
finite free applicability gap using known Gaussian/Berezin machinery;
it makes no claim beyond the checked literature. No candidate solution
or improved interacting reflected-error bound results. There are zero
inconclusive mathematical exploration attempts on the auxiliary route;
the earlier stopped route remains stopped.

The next direction checks whether a global compact nonlinear gauge
fixing can have the nonzero normalization needed for a Wilson-measure
replacement. This is a changed hypothesis requiring a separate source
comparison, not another calculation in this turn. A new REVIEW_REQUIRED
record is drafts/literature/2026-10-04-compact-brst-gauge-fixing-normalization.md;
the current exact action is recorded only in PROGRESS.md. No nonlinear
lemma or script is written. The saved SPECIALIZE assessment is unchanged.

The exact script `PYTHONDONTWRITEBYTECODE=1 python3
scripts/auxiliary-cochains/check_ward.py` checks the complete N=2 relative
complex and every bosonic monomial of degree <= 4 times each exterior
monomial at epsilon = 0, 1/3 and 2. All 8,580 rational identities pass.
For the first link, the antighost/connection defects are 0, 1/5 and 2/5;
the antighost/beta defects are 0, 2/5 and 4/5. Beta = -i b is only an
algebraic coordinate in the check. The script supplements the proof;
it does not establish convergence, all-mesh validity or nonlinear control.

## Validation

The mathematical proof was checked against the left-derivation product
rule, L013's positive Fourier phase and Berezin orientation, nonzero
normalization, complete relative cell spaces, and the domination needed
for the breaking insertion. L014 uses L013's cochain setting as its sole
direct mathematical input; the source precedents are imported supporting
formulas, and L012 is only a contrast. The documentation checker with
--problem yang-mills passed with 14 nodes and 23 unique edges. All 29
pre-existing lemma, script and assessment hashes remain unchanged.
Read-only field checks confirm unchanged prior SPECIALIZE coverage,
RESEARCH / REPRODUCTION metadata, and exact matching of the new pending
assessment to the current Next action. The local whitespace diff check
passed. These checks establish no nonlinear or continuum conclusion.
