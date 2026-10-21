# Product Spin(7) criterion — actual-equation mismatch

TARGET: Assess whether Galt–Ma's product Spin(7) calibration has an applicable instanton equation and alpha-charge exclusion criterion for L071's equality kernel at the retained common quaternionic metric.
CHECKED: 2026-10-19
DECISION: IMPORT
SEARCH_EVIDENCE: Reused the product-splitting assessment and scoped L071/L131, ATTEMPTS/073–075 and history/398–399 comparisons; exact hyperholomorphic/Spin(7)/product/Fueter searches located Walpuski's explicit product eigenspace decomposition, which was read rather than inferred from snippets.
SOURCE_EVIDENCE: Galt–Ma arXiv:2405.17086v2 (25 January 2025), Table 1, Definitions 1.1–1.2 and 2.11, section 2.5, section 5.2 (5.16), Proposition 4.2 and Lemma 4.3 with their energy-comparison proof cases; Walpuski, Spin(7)–instantons, Cayley submanifolds, and Fueter sections, author PDF dated 2016-05-09, Example 2.8, (2.9), Propositions 2.12 and 2.14, Definition 2.17, printed pp. 4–6.
COMPARISON: For the same ordered triples the cited all-minus product Cayley form has a forbidden Lambda^2_7 mixed summand characterized by sum_i J_i L I_i=-3L; this includes common-quaternionic-linear mixed coefficients, whereas the instanton equation requires their Lambda^2_7 projection to vanish. L071's compatibility is therefore not the needed instanton import.
GAP: No applicable actual-instanton hypothesis has been obtained for this all-minus form, so its alpha-charge cannot be used to exclude F or deduce splitting; no charge was computed and no kernel nonexistence is asserted.
REASON: The primary mixed-eigenspace statement gives a concrete hypothesis mismatch and changes the route from possible charge application to parking this lead; the imported result is a source-applicability diagnosis, not a new curvature theorem.
SCOPE: Only the source-equation comparison for L071's hypothetical equality F with the retained common ordered triples, exact metric and full c_2=14e_1+21e_2+tau_D. IMPORT authorizes the cited diagnosis only, not a charge calculation, rotated-frame application, kernel exclusion or new lemma.

LITERATURE_REASON: The startup gate required this separate comparison because the product Spin(7) actual-equation and frame hypotheses were outside the ready Kähler assessment.

## Relevance and primary comparison

The main gap is universal primitive rational Hodge realization; even
existence of the conditional equality F is open. The intermediate target
was an applicable energy criterion, whose downstream use would have been
one necessary-condition test on F. The startup continuation test required
an actual-equation match and usable threshold before any charge work.
That test fails at the equation hypothesis, so the all-minus criterion is
parked. This is new source-comparison evidence, not a Hodge advance.

[Galt–Ma v2, section 5.2 (5.16) and Table 1](https://arxiv.org/html/2405.17086v2#S5.SS2)
use Phi=vol_Y+vol_X-sum_i tau_i wedge omega_i and
alpha=vol_X-sum_i tau_i wedge omega_i, with beta=1. Their
[section 2.5, Definition 2.11](https://arxiv.org/html/2405.17086v2#S2.SS5)
requires *(Phi wedge F_A)=-F_A, not merely an arbitrary compatible
connection on the same Riemannian product. The eigenvalues are -1 and 3.
The product orientation is that of the two hyperkähler surfaces and both
volume restrictions are positive. Neither multiplying Phi by -1 nor
changing one ordered triple is a harmless substitution for this test.

The decisive primary input is
[Walpuski, author PDF dated 2016-05-09, Example 2.8, Propositions 2.12 and 2.14, Definition 2.17, pp. 4–6](https://walpuski.com/Research/Spin7InstantonsCayleys.pdf#page=4).
His (2.9) is exactly the same product form; the flat-frame paragraph
following Example 2.10 specifies equal positive self-dual triples.
For quaternionic lines S,T, Proposition 2.14 states

\[
\Lambda^2_7=\bigoplus_{i=1}^3\mathbb R(\tau_i-\omega_i)
\ \oplus\ \{\langle L\,\cdot,\cdot\rangle:
                 \textstyle\sum_i J_iLI_i=-3L\}.
\]

Here I_i and J_i are the complex structures corresponding to those
same two triples. This statement concerns the full mixed real form,
not a harmonic moduli quotient. Proposition 2.12 assigns eigenvalue
3 to this summand; Definition 2.17 requires pi_7(F_A)=0.

For applicability, L071 supplies coefficientwise diagonal quaternionic
invariance. Written as a mixed bilinear coefficient
B(u,v)=g_T(Lu,v), that invariance means L I_i=J_i L.
Thus the source's displayed sum has three terms -L: these coefficients
are in its forbidden summand. This is the necessary hypothesis
comparison with the imported decomposition, not a reproof of it or a
new kernel-exclusion argument. In particular one cannot replace
pi_7(F_A)=0 by L071's compatibility. No vanishing of actual mixed
curvature is assumed or deduced here. No independent triple rotations
are imported to change this comparison.

## Energy hypotheses and stopping decision

[Galt–Ma, Proposition 4.2 and Lemma 4.3](https://arxiv.org/html/2405.17086v2#S4)
require the actual theta-instanton throughout. Read the orthogonal
curvature-energy comparison (4.10)–(4.16), including the negative-charge
case. Negative alpha-charge excludes such instantons; null charge with
matched minima gives the stated product-curvature vanishings. The
positive-charge alternative additionally needs -1<eta_beta<0 and
kappa_alpha<Vol(Y) kappa_beta(-1-1/eta_beta). Here the cited Spin(7)
normalization and beta=1 give the matched minima -1, so that strict-gap
alternative is unavailable even before considering topology. These
theorems concern instantons for their chosen form, not all bundles on
the underlying product. No Spin(7) charge or sign has been evaluated.

L131's Kähler charge and ATTEMPTS/075 remain a different, parked test.
ATTEMPTS/073–074 retain the coherent-vanishing and diagonal stops.
The present import changes neither L071 nor a canonical mathematical
argument, so no lemma, DAG row or PROOF.md change is required. Any
later use of the source decomposition to prove additional conditional
curvature assertions would require its own approved mathematical target.

## Search scope and qualifications

Queries included `"hyperholomorphic" "Spin(7)" instanton product`,
`"Spin(7)" "hyperkähler" product "minus" quaternionic`, and
`"Cayley" "Fueter" "hyperkähler" instanton product`.
Walpuski's explicit local product proposition supplies the needed
comparison; his gluing theorem is not applied.
Muñoz, arXiv:1307.8000v2 (9 January 2014), section 4.1, pp. 7–9, was
also inspected: its HYM/Spin(7) discussion fixes a compatible SU(4)
form, and its stated context there is flat complex tori. It is not a
theorem identifying the all-minus product form with L071's common
complex structure. A Fowdar search hit was only a lead; an attempted
PDF fetch failed and no claim relies on it. There is no essential
source blocker because the explicit product decomposition is accessible.
No exhaustive search or novelty claim is made. Matching Mathlib
coverage was not checked; unknown availability is not absence.

Essential retained inputs are L071 and L044's actual metric and full
tensor, with L131 and ATTEMPTS/073–075 preserved as contrasts. F
existence, separation, reconstruction, ambient extension, transport and
universal primitive Hodge realization remain unresolved.
