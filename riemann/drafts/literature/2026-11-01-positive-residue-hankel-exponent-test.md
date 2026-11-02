# Positive-residue full Hankel exponent — bounded test nomination

TARGET: Test whether a sufficiently small positive-residue pole census preserves half the exact grid exponent in the full Hardy-space Hankel norm, without pole separation.
CHECKED: 2026-11-01
DECISION: EXPLORE
SEARCH_EVIDENCE: Reuse the completed full-pole Hankel comparison's bounded Nehari/AAK, rational-symbol, positive-residue, logarithmic-derivative and SPF searches and scoped duplicate/failure checks. They identify no inspected theorem for this exact weighted, growing-census bound; no novelty or exhaustive-absence claim.
SOURCE_EVIDENCE: Adamjan–Arov–Krein (1971), Theorems 0.1/0.2, pp.31–33, finite-rank-relevant Theorem 1.1 cases pp.41–43, https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=3284&what=fullteng ; Baratchart–Chevillard–Qian (2016), Theorem 2/(17)–(19), Theorem 4/Corollary 1 and proofs, Section 5.2/(24)–(27), finite-Blaschke Lemma 1/Theorem 5 proof case, pp.24–30, https://www.must.edu.mo/images/SCSE/qiantao/QianTao_P147.pdf ; Chunaev–Danchenko 1907.07437v1, Theorem 1/(8) and Sections 2.1/2.4, https://arxiv.org/pdf/1907.07437v1 . Full hypotheses and scope comparison are recorded in the parent assessment.
COMPARISON: Standard theory covers the complex-symbol operator, distance identity and finite rational realization, but leaves a quantitative spectral estimate. Inner-symbol unit singular values and unweighted SPF lower bounds do not cover the exact complex inverse-grid amplitudes. C645d stops scalar sums; C645e/C645f only control a small unit-residue cluster. The proposed exponentially small operator threshold tolerates polynomial losses without asserting separation or positivity of weighted residues.
GAP: Prove or obstruct the precisely quantified sparse-census norm bound below, including integer residues and arbitrary close poles. Its principal-part application, actual-Xi census/clearance, interpolant realization, independent boundary upper bound and signs remain unresolved.
REASON: A genuinely different full-operator test could replace the three-pole restriction while retaining a useful part of the grid gain. This nomination specifies an unproved bound, not a theorem application or a completed calculation. It awaits separate supervisor approval before research.
SCOPE: Only the synthetic full Hankel norm test below and its explicitly checked contour implication or limitation. Reuse standard operator results by citation; do not reprove Nehari/AAK, assume positive weighted amplitudes, silently impose pole separation, or infer actual-Xi signs.

## Proposed statement, not a result

Fix 0<delta<1/2 and 0<eta<delta/2. Use C645f's exact definitions
of d=3/2-delta, R=3/2-delta/2, x=-d, n>=5, and the complex B_n.
Define the positive number Lambda by C645c's exact integral

    Lambda = integral_0^1
      -log(R sqrt(d^2+t^2)/sqrt(R^4+d^2 t^2)) dt.

C645c's audited product statement supplies this rate without its
conditional zeta assumptions. Cite it within that scope if used.
No new integral bound is requested here.

Let Z be any finite set of distinct points in |a|<=R-eta, containing
x and avoiding every grid point i*j/n. Assign positive integer
residues r_a, with M=sum_(a in Z) r_a. For |zeta|=1 define the
explicit proper rational symbol

    q_(n,Z,r)(zeta) = sum_(a in Z)
        [r_a B_n(x)/(R B_n(a))] / (zeta-a/R),

and define H_q h=P_minus(q h) from H2 to H2_minus with the normalized
circle L2 norms of BCQ (17). This defines the proposed test object;
it does not prove that a given actual-Xi residual has this operator.
The residue of q at a/R is the displayed bracket, not r_a.

Ask whether for each fixed delta,eta there exist explicitly controlled
constants kappa>0, c>0 and integer N>=5 such that

    ||H_(q_(n,Z,r))|| >= c exp(-Lambda*n/2)

for every integer n>=N and every allowed Z,r with M<=kappa*n.
The constants must be independent of n, Z, the residues and all
pairwise distances. Stating an infimum, a finite matrix formula or
positivity for each fixed configuration does not answer this question.
An effective positive kappa, or a rigorous lower bound on an admissible
kappa in terms of delta,eta, is required for a positive outcome.

## Bounded attempt and discriminating evidence

Test this single sparse-census statement, using the exact complex
amplitudes. It may be approached by a finite model-space dual or a
confluent extremal family. Those are possible techniques, not extra
targets or assumed lemmas. Save partial reasoning before lengthy work.

Continue if the stated uniform inequality is proved with controlled
constants, or if a rigorous obstruction identifies a sharp additional
condition and a materially refined useful scale. Abandon this precise
universal sparse-census claim if an admissible family rules it out:
in particular, n_j->infinity, M_j/n_j->0 and
exp(Lambda*n_j/2)||H_(q_j)||->0 would do so. For a claim of a different
obstruction, check its quantifiers against arbitrary kappa,c,N.
A floating-point small singular value, scalar cancellation, or
vanishing least nonzero singular value alone is not decisive: the
target is the largest singular value/operator norm.

This is not a request to prove a constant-in-n bound or to ignore
polynomial losses. Failure to settle the displayed exponential
threshold is EXPLORATION. Do not repeat it without new input, a
certified obstruction or a refined mechanism.

Plausible downstream use: if the full principal-part reduction is
proved, the existing boundary division and this operator test could
give a necessary residual size retaining half the grid exponent,
rather than requiring an isolated cluster of at most three poles.
Any contradiction would still need a separately established smaller
boundary upper bound. The sparse-census hypothesis M<=kappa*n is
not supplied by the general O(log height) shell count: the required
coefficient, selection of a zero/contour and fixed clearance are open.
Neither a toy success nor failure decides RH.

Essential local inputs: C645f's exact factors/grid removals/boundary
normalization, C645c's audited product-rate portion, and the parent
source assessment's operator conventions. C645d and C645e are
obstruction/comparison evidence, not assumed full-census estimates.
No cross-notebook input. Mathlib matching coverage remains unchecked.

The required creative escalation is the central obstruction: complex
inverse-grid phases can cancel unit residues, and existing moments
handle only three poles. The bounded evidence sought is a uniform
operator lower bound at the specified half-rate, or a certified
sparse-census family violating it. The creative content would be the
quantitative positive-residue mechanism; standard AAK identities and
finite rational matrix construction are known inputs. This literature
nomination derives no result and does not authorize immediate research
in the same invocation.
