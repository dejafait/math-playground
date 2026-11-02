# Full-action positive-arc mass — completed source comparison

TARGET: Test whether every full L666 action A_n with A_n(x)=1, Re A_n(x+i*y)>=0 for all |y|<=9/20 and ||psi_n||_2<=exp(n/100)*n^C has normalized central-arc mass M_n>=n^(-K_C) for some K_C and onset depending only on fixed C, without a polynomial-degree restriction, prescribed zero or rational-pole ansatz.
CHECKED: 2026-11-02
DECISION: SPECIALIZE
SEARCH_EVIDENCE: Step 58 searched Bernstein-ellipse Chebyshev approximation, analytic local Remez/Bernstein-index inequalities, Markov polynomial derivative bounds and analytic Nikolskii mass estimates; exact queries, inspected primary sources, reused local coverage and unused leads are recorded below. No exact theorem for the L666 action was identified; no novelty claim follows.
SOURCE_EVIDENCE: Inspected Trefethen, Approximation Theory and Approximation Practice, author repository chapter sources retrieved 2026-11-02, Theorems 8.1--8.2 and proofs, chap8.m lines 104--169, and chap4.m (4.8)--(4.9); Totik--Zhou, author manuscript dated 2016-11-21, Section 1/(1)--(5), printed p.1; Nazarov--Sodin--Volberg math/0108213v2 (2001-11-04), Section 1 theorem and Lemma B, printed pp.1--3, as comparison statements only.
COMPARISON: Known quantitative Chebyshev approximation and the named Markov inequality cover the analytic-approximation and polynomial-derivative inputs. Their application still needs uniform full-kernel growth, real-part handling, approximate-positivity error accounting and normalized mass transfer. L677/L678 require exact finite degree or pole removal; L674's open-domain sign hypothesis is stronger than this target. No inspected result alone settles the exact full-action assertion.
GAP: Specialize the cited inputs to arbitrary complex full L666 actions, proving all uniform neighborhood/norm/error/measure bounds, or rigorously obstruct that specialization; the target mass bound itself is unproved. Do not replace the action by an exact finite-degree or positive-real-domain ansatz.
REASON: Essential source coverage for one bounded specialization attempt is now complete, with no essential source blocker. Import approximation and Markov rather than reprove them; only the explicitly listed family-specific applicability and transfer work remains. This separate literature turn approves the unchanged TARGET for later mathematics and proves no new mass estimate.
LITERATURE_REASON: At invocation the new target lacked primary approximation/mass coverage because it removed exact degree, pole and zero assumptions; this review fills that essential gap rather than refreshing ready rational coverage.
SCOPE: Exactly TARGET and its fixed-C uniform quantifiers, using the complete L666 product and normalized angular L2. A later REPRODUCTION attempt may bound the full kernel on a fixed neighborhood, apply the cited polynomial approximation and Markov inequality, and justify real-part, sign-error and mass transfer, or identify a rigorous obstruction. No cone/H/support/Xi conclusion, imposed zero, degree restriction on the action, or open-domain positivity is approved.

## Exact intended hypotheses and mass (preserved nomination)

Use q>=1, n=12q+3, tau=(n-1)/n, x=-d=-5/4, R=11/8,
U=121/64, and the complete L666 kernel, including j=0 and the
denominator angle 1/u. For arbitrary complex psi_n in normalized
L2(T), let

    A_n(a)=mean_u conjugate(psi_n(u))*W_a(u), |a|>tau,
    theta0=2*arctan(9/25),
    M_n=(1/(2*pi))*integral_(-theta0)^theta0
                  Re A_n(x+i*d*tan(theta/2)) dtheta.

For each fixed real C, the proposed assertion is that there exist
K_C>=0 and n_C, independent of the eligible psi_n, such that M_n
is at least n^(-K_C) whenever n>=n_C and the TARGET hypotheses
hold. No symmetry of psi_n, Taylor coefficient nonvanishing, choice
of inverse, exact zero at -R, or polynomial/rational representation
is assumed. All unused modes remain free. An empty feasible family
would make this conditional mass assertion vacuous; it would not
be an existence theorem for a separator.

## Relevance and bounded future test

The main unresolved claim remains actual-Xi all-degree mixed positivity.
The present intermediate question concerns the strength of continuum
angular separators. A uniform mass bound could be combined with
L678's audited complementary-ray attenuation and the separately
qualified parameter-circle estimate in L674 to test this broader
separator route. Such a combination is not proved or approved here.
The general displacement-dependent cone, original unit-residue H,
support and Xi realization remain independent gaps.

The proposed mechanism is analytic approximation on a fixed complex
neighborhood of the segment/circle trace, with degree proportional
to n and an explicitly controlled error, followed by positive-mass
transfer. This is a suggestion to assess, not a claim that its uniform
bounds or positivity transfer hold. Symmetrization if needed, the
full-product norm on the larger domain, the approximation error and
the effect of small negative approximation errors are unresolved.
The action may depend on n arbitrarily within the stated budget.

After source approval, the discriminating mathematical test is a
proof of the stated uniform polynomial mass bound, or a rigorous
eligible sequence for one fixed C whose positive mass violates
every such polynomial lower bound. A failure of a particular
approximation estimate only stops that mechanism, rather than
refuting the mass statement. Finite fits, an assumed degree cutoff,
or positivity on an added open domain do not pass the test.

Essential local input IDs for later comparison: L666 (full kernel),
L677 (finite-degree mass calculation), L678 (audited all-ray estimate),
and L674 (proposed holomorphy/parameter-circle attenuation, whose
independent audit remains open). L675 and the former finite-polar
screen are comparison stops, not assumed analytic approximation
theorems. No cross-notebook input is involved. Full matching Mathlib
coverage has not been checked.

This nomination is materially different from choosing another pole
location or raising the rational numerator degree: it asks for a
norm-controlled mass estimate for actual angular actions without an
exact finite-dimensional form. The stopped rational family remains
stopped. No new lemma, mathematical script, proof of this target or
ready approval was produced in the nomination turn. That turn required
the separate literature comparison completed below.

## Completed comparison — 2 November 2026, step 58

### Primary approximation input

L. N. Trefethen, *Approximation Theory and Approximation Practice*,
Chapter 8, Theorems 8.1--8.2, equations (8.1)--(8.3). Read the author's
[chapter source](https://raw.githubusercontent.com/chebfun/ATAP/development/chap8.m),
development version retrieved 2026-11-02, lines 104--169; the
[author's book page](https://people.maths.ox.ac.uk/trefethen/ATAP/)
identifies these chapter M-files as the book source. For a function
holomorphic in an open Bernstein ellipse E_rho, rho>1, and bounded
there by B, its degree-m Chebyshev projection has uniform interval
error at most 2*B*rho^(-m)/(rho-1). The interpolation bound has 4
in place of 2. Read the full coefficient proof, including limiting
contours when analyticity is only on the open ellipse, and the
projection-tail formula (4.8) in the
[Chapter 4 source](https://raw.githubusercontent.com/chebfun/ATAP/development/chap4.m),
lines 151--157. No boundary holomorphy is silently required. The
post-theorem discussion distinguishes analyticity from boundedness
on the chosen ellipse. This supplies a quantitative approximation
input, not a uniform bound for our n-dependent actions. No reproof
or numerical Chebfun computation is needed.

### Primary derivative input

Import the named A. A. Markov polynomial inequality as explicitly
stated in V. Totik and Y. Zhou, *Sharp constants in asymptotic higher
order Markov inequalities*,
[author manuscript](https://www.math.u-szeged.hu/pot/Markovk.pdf),
dated 21 November 2016, Section 1, equation (2), printed p.1. Read the
polynomial/norm conventions and (1)--(5). For any complex polynomial
p of degree at most m, ||p'||_[-1,1]<=m^2*||p||_[-1,1]. This is a
global closed-interval estimate, including endpoints; degree zero
is allowed with zero derivative. It needs no nonvanishing, positive
coefficients or root restriction. The later general-compact-set
asymptotics are not inputs. The standard named theorem is imported,
not reproved; its use for a mass bound with approximation error
still requires a written applicability/transfer argument.

### Stronger analytic comparison and source limits

F. Nazarov, M. Sodin and A. Volberg, *Local dimension-free estimates
for volumes of sublevel sets of analytic functions*,
[arXiv:math/0108213v2](https://arxiv.org/pdf/math/0108213v2),
4 November 2001, Section 1, printed pp.1--3. Inspected the main
theorem and Lemma B statements, not their proofs. The main theorem
assumes a nonconstant analytic function bounded by one on a complex
unit ball and a real ball inside radius 1-epsilon, epsilon<=1/4;
its distribution exponents retain log(1/|F(0)|). Lemma B additionally
requires equal nonzero moduli at opposite real points. These are
not sign theorems, paid angular inverses or a direct polynomial-mass
bound for this target. No specialization or import of them is used;
they are inspected comparison results rather than hidden premises.

Shadrin's *Twelve Proofs of the Markov Inequality* author PDF was
located, but retrieval failed (502, then timeout). Search snippets
were not treated as a reading. It is not essential: the standard
named first-derivative theorem with its full hypotheses is available
in the inspected Totik--Zhou text. No dependent work is source-blocked.
Recent sharp Bernstein--Nikolskii work (arXiv:2609.32072), the
quasianalytic NSV papers and general exponential-sum inequalities
were search leads only; their theorems/proofs were not read or used.

### Exact remaining specialization, without a derivation this turn

The future attempt must retain arbitrary complex psi, both normalized
angular means, all factors including j=0, and every free Fourier mode.
Its proof obligations are:

1. Choose a complex neighborhood of the ordinate interval independent
   of n, verify separation from all parameter and angular denominators,
   and prove an explicit uniform bound for the complete product and
   action there from the actual L2 norm budget. Compact holomorphy
   separately for each n is not the required growth estimate.
2. Treat the real trace rigorously. The real part of a holomorphic
   function is not itself holomorphic on a complex domain. Either
   approximate the complex action before taking its real trace or
   justify a holomorphic reflected extension on a common domain.
   No real/even assumption on psi may be introduced.
3. Use the imported approximation theorem with a proved rho and B_n,
   and an explicit degree and error uniform over eligible psi. The
   degree is an approximation parameter, not a restriction on A_n.
4. Account for small negative approximation errors before applying
   any nonnegative-polynomial mass argument. Apply Markov on the
   correct scaled interval, handle a possible endpoint maximum and
   degree zero, and show that the resulting mass survives the error.
5. Transfer to precisely M_n with its stated positive angular measure,
   including endpoints and all normalization constants. Produce K_C
   and an onset depending only on fixed C, with any uniform prefactor
   explicitly absorbed. C is an arbitrary fixed real number.

These are prospective applicability tasks, not proved intermediate
claims. The sources do not supply their L666-specific constants.
Only such a specialization is authorized, with classification
REPRODUCTION; no claim of new analytic approximation mathematics is
warranted. A citation alone does not perform these tasks, but there
is no missing essential theorem that forces another source-only step.

### Duplicate/failure comparison and decision

Scoped reads covered L666 Section 2, L674 Sections 1--4, L675's
hypotheses, L677 Section 3, the supplied L678 audit checkpoint, and
the ready positive-real, inverse-polynomial, polynomial-audit and
repeated-pole assessments. Also read the finite-degree and parameter-
disk stop records in ATTEMPTS. No sibling notebook or shared scheduler
state was read or changed. The initial git inspection showed substantial
existing notebook work; all of it is preserved.

L677's exact degree controls its Fourier count and L678 removes an
exact repeated pole; neither permits replacing an arbitrary action
by a polynomial without an error. L674's Herglotz import requires
open-domain nonnegativity and cannot give the present segment-only
mass statement. Its holomorphy argument is relevant local guidance;
its independent audit remains open and its attenuation claim is not
an essential premise for proving the mass target alone. Failed
finite screens or low-degree fits do not decide this assertion.

The main RH gap and the proposed downstream attenuation comparison
are unchanged. A mass bound would supply only an intermediate input;
it would neither construct an eligible action nor close the general
cone/H/support/Xi realization gaps. Failure of an approximation bound
would stop that mechanism only. A counterexample must be an actual
eligible sequence for one fixed C, not arbitrary analytic functions
or finite fitted values. This review contains no such sequence.

The essential comparison is now sufficient for one later bounded
SPECIALIZE attempt on the unchanged TARGET. Outcome EXPLORATION:
source scope is newly actionable, but no mathematical mass estimate
or source-exceeding result has been established. No new lemma,
mathematical script, PROOF.md assembly or DAG edge was written.
Matching Mathlib coverage of these quantitative approximation/mass
statements was not checked; supporting analytic/polynomial facts
would not establish the full action assertion.

### Search record

Queries on 2026-11-02 included `Trefethen Approximation Theory
Approximation Practice theorem 8.2 Bernstein ellipse analytic
polynomial error pdf`; `Nazarov Sodin Volberg local dimension analytic
functions Remez inequality Bernstein index pdf`; `Trefethen ATAP
chap8.m theorem 8.2 github`; `nonnegative analytic function point
evaluation integral polynomial logarithm analytic norm Nikolskii
inequality`; `Markov inequality polynomial interval theorem n squared
sup derivative Totik pdf`; `analytic function nonnegative interval
integral lower bound log maximum Nikolskii`; `Shadrin Twelve proofs
Markov inequality arxiv pdf`; `analytic functions Nikolskii inequality
logarithm Bernstein index interval L1 Linfinity`; `analytic functions
Markov Bernstein index interval`; and `nonnegative analytic polynomial
approximation Nikolskii`. Returned secondary pages/snippets located
sources but were not mathematical evidence. The search was bounded;
absence of an exact match does not imply novelty.
