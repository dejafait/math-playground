# Averaged cancellation-budget source comparison

TARGET: Review whether mean_(|u|=1/2) log^+(A_n(u)/S_(n,1)(u))=o(n), with A_n=R^(-1)sum_a|W_a|, is a viable sufficient route to the fixed L703 spatial-growth target.
CHECKED: 2026-11-03
DECISION: EXPLORE
SEARCH_EVIDENCE: Step 161 completed the bounded signed-moment, power-sum, Vandermonde-conditioning and total-variation comparison below, reusing the ready sampling and spatial-growth assessments. No inspected theorem settles the prescribed averaged budget; this does not establish novelty.
SOURCE_EVIDENCE: Gautschi, Numer. Math. 4 (1962), Theorem 1/(3.1) and proof pp.118-119 https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/016.pdf ; Gautschi, Numer. Math. 23 (1975), Section 3/(3.3)-(3.4) p.339 and (4.1) p.340 https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/051.pdf ; Pan arXiv:1504.02118v2 (26 April 2015), Theorem 3.1(v), proof and Corollary 3.1(iv), PDF p.3 https://arxiv.org/pdf/1504.02118v2 ; reused primary sampling/Fourier references and limited Nazarov inspection are delimited below.
COMPARISON: Generic inversion has the familiar Lagrange product cost; small singular values concern worst-case vectors and do not lower-bound the prescribed weights' cancellation. Unit-circle sampling, exact rational quadrature and the radius-one Fourier gap supply no matching radius-1/2 logarithmic estimate. L707 (3) remains a sufficient, not necessary, condition for B_sp=o(n).
GAP: Establish the actual sublinear budget or find a fixed positive-measure radius-1/2 arc on which the full signed norm is exponentially smaller than A_n. Neither alternative is established; the family-specific relative norm comparison is outside the inspected theorems.
REASON: Essential source comparison is complete for a bounded full-family test, with no essential access blocker. A fixed-arc obstruction test is nominated in a separate ready scope for next-turn approval; no mathematical estimate is derived here.
LITERATURE_REASON: The invocation-start REVIEW_REQUIRED target isolates a new absolute-envelope-to-signed-norm premise outside the ready spatial-growth transfer assessment.
SCOPE: The same actual L703 profile fixed before n=12q+3; the full L666 weights and all M=n/3 moments; |u|=1/2 and spatial radius 1; A_n is only the absolute-weight envelope, with the original diagonal D unchanged.

The following nomination was the question at invocation start. The completed
comparison below supersedes its requests for further source work.

The mathematical result being continued is the conditional coefficient
bound in L707 (3). Review its new premise, not the already covered
three-circles or boundary-Poisson theorems. Known matching theorems
should be imported if available; an obstruction must concern this
same profile and radius. A failed upper certificate is not an
obstruction to the actual budget. Generic freely chosen weights and
n-dependent displacements do not settle this target.

Before a later mathematical attempt, compare the exact statement and
stronger known results with the recorded signed-moment and Fourier-gap
failures. In particular distinguish the positive-radius Fourier limit
used by L704 from the radius-1/2 circle average now required. L698's
unit-angular-circle conclusion cannot simply be moved to this circle.
No prior stop is promoted to a global ban.

Possible downstream use is L707 (3), then L707 (1), to pay the
complementary spatial Jensen defect. This would still require separate
angular amplitude, full L657 charge, H/support, Xi realization and
actual-Xi positivity. If the stronger budget has a positive linear
obstruction, stop this sufficient subroute without claiming that
B_sp=o(n) or J_sp=o(n) has failed.

Essential local inputs for the comparison are L666, L703, L706 and
L707. The saved parent source comparison is ready only for its original
target, not an approval of this newly isolated premise. Full matching
Mathlib coverage is not checked. No new source theorem, lemma or
asymptotic conclusion is asserted by the nomination above.

## Completed comparison — 3 November 2026, step 161

### Primary inversion results and their limits

W. Gautschi, *On inverses of Vandermonde and confluent Vandermonde
matrices*, Numer. Math. **4** (1962), 117–123,
[Theorem 1, (3.1), pp.118–119](https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/016.pdf),
uses distinct complex nodes and V_(k,j)=z_j^k, 0<=k<N. It states

    ||V^(-1)||_infinity
        <=max_j product_(l!=j) (1+|z_l|)/|z_j-z_l|.

Read its complete proof and the Section 2 symmetric-function lemma,
including zero nodes and the strict triangle-inequality case. The
inverse-entry formula is cited there; Gautschi's later
[*Norm Estimates for Inverses of Vandermonde Matrices*, Numer. Math.
**23** (1975), 337–347, Section 3, (3.3)–(3.4), p.339](https://www.cs.purdue.edu/homes/wxg/selected_works/section_01/051.pdf)
supplies the full Lagrange-polynomial derivation, which was also read.
Its (4.1), p.340, repeats the bound. This identifies L707's
interpolation mechanism as standard; no new reproof is justified.
The local nodes are distinct, but the theorem's matrix norm is not
the prescribed vector's ratio A_n/S_(n,1). It supplies no sublinear
logarithmic bound for that ratio. No ray or reflection symmetry of
the L703 nodes is assumed; the stronger equality cases are not used.

V. Y. Pan, [*How Bad Are Vandermonde Matrices?*,
arXiv:1504.02118v2](https://arxiv.org/pdf/1504.02118v2), 26 April 2015:
read definitions (1.1)–(1.2), Theorem 3.1(v), its full proof and
Corollary 3.1(iv), PDF p.3. For the square N-node case, if the first
k nodes satisfy |z_i|<=nu^(-1), nu>1, the source gives

    sigma_min(V)<=nu^(2-k)*sqrt(k)/(nu-1),
    condition_2(V)>=(nu-1)*|V|/[nu^(2-k)*sqrt(k)],
    |V|=max(1,max_i |z_i|^(N-1)).

Its proof deletes a block to lower rank and bounds the perturbation.
These are worst-case spectral statements, allowing arbitrary vectors.
L707 places the spatial nodes inside a fixed disk of radius rho<1,
so generic conditioning is relevant. It does not identify the actual
W(u) with a near-nullvector or settle an angular average. No local
exponent, actual counterexample or norm conversion is derived here.

### Reused sampling and Fourier coverage

Reuse the completed primary readings in
[the signed-angular-sampling assessment](2026-11-02-displaced-signed-angular-sampling.md):
Moitra, [arXiv:1408.1681v4](https://arxiv.org/pdf/1408.1681v4),
Theorems 2.2–2.3 and proof, pp.5–7, and Danchenko–Semin,
[arXiv:1503.06476v1](https://arxiv.org/pdf/1503.06476v1), Theorem 2
and proof, PDF pp.1–2,6–7. Moitra requires unit-circle exponential
nodes, wrap-around separation and a sufficiently long observation
interval. Our nodes p_a=a/R are inside that circle; rescaling or
translating them changes the moment map and its norm. No cost-free
map was established. The rational quadrature theorem exactly observes
a combined rational function with specified reflected pole orders.
L666 applies it on the angular unit circle. The identity supplies
neither coercivity against sum |W_a| nor a radius-1/2 logarithmic bound.
The ready statements were reused, not rederived or freshly audited.

Reuse Lev's spectral-prescription Theorem 4.8 and complete proof
from [the anchored-gap assessment](2026-11-03-anchored-half-lattice-fourier-gap.md),
and its already checked Gevrey specialization in L703. These preserve
positive unit counting masses; they do not impose signs on the finite
rational W_a. L698's complete-polynomial decay is on |u|=1. L704's
positive-point limit uses u=1/10000. Neither reaches an arc of
|u|=1/2. L706 pays the spatial Jensen defect near -1/2; that
conclusion alone does not compare A_n and S_(n,1). No radius or
observable has been changed by mathematical derivation in this review.

The parent spatial-growth assessment's three-circles, boundary-zero
Poisson–Jensen, Mahler and integrability coverage remains adequate.
L707 remains unaudited; this comparison is not a critical audit of it.

### Additional inspection and search limits

F. L. Nazarov, *Local estimates for exponential polynomials and their
applications to inequalities of the uncertainty principle type*,
Algebra i Analiz **5** (1993), no.4, 3–66:
[publisher-hosted Russian original](https://www.mathnet.ru/php/getFT.phtml?jrnid=aa&option_lang=eng&paperid=397&what=fullt).
Read Theorem I's hypotheses on p.5 and the complex-exponent discussion
in Section 4.1, pp.57–59. The theorem compares suprema of a finite
exponential polynomial on a real interval and a measurable subset of
positive length, rather than coefficient total variation and a signed
spatial norm. Text extraction loses parts of its displayed constants;
no exact constant or full proof is imported. A guessed author PDF URL
failed and direct local download was blocked by DNS; publisher text
was accessible. A future quantitative Nazarov application would need
its exact formula/proof checked. None is essential to the nominated test.

Queries combined `signed discrete moments total variation polynomial
supremum Vandermonde exponential condition number`, `Turan power sum
inequality sum absolute coefficients close nodes lower bound`,
`Littlewood exponential sums complex coefficients imaginary frequencies
signed moments lower bound`, `Turan complex coefficients power sums
inequality`, `Norm estimates for inverses of Vandermonde matrices`,
`How Bad Are Vandermonde Matrices`, `Local estimates for exponential
polynomials`, `weighted power sums lower bound complex coefficients
Turan`, `total variation moments Vandermonde signed stability`, and
`cancellation truncated Cauchy transform norm`.

Littlewood/pure-power-sum results, Prony reconstruction and recent
super-resolution papers appeared as unread leads. Their primary
statements/proofs were not inspected; no claim of their applicability,
inadequacy or strongest conclusion rests on snippets. The inspected
matrix theorems and reused sampling/Fourier sources supply the actual
comparison. Failure to find a match does not certify originality.

### Decision and a discriminating continuation

Outcome: EXPLORATION. The budget is unproved and unrefuted. Generic
conditioning does not turn the failed interpolation upper certificate
into a lower bound for actual cancellation. Preserve
`ATTEMPTS/2026-11-03-spatial-doubling-interpolation-unpaid.md` and
the scoped global-endpoint stop; neither is reopened by renaming it.

Nominate one test: seek a fixed positive-measure arc I on |u|=1/2
and epsilon>0 with S_(n,1)<=A_n*exp(-epsilon*n) eventually, for
the same fixed L703 profile. This tests a positive linear obstruction
to the stronger budget. Keep the anchor, unit masses, inverse angle,
j=0, both endpoints and every spatial coefficient. No such arc,
inequality or transfer from the radius-one gap is established here.
A point sample, arbitrary weights, n-dependent profile or divergent
upper certificate would not pass the test. Failure to obtain a valid
relative estimate is inconclusive, not a disproof of either asymptotic.

The new ready continuation is scoped in
`drafts/literature/2026-11-03-spatial-cancellation-arc-attempt-scope.md`
for separate next-turn approval. No lemma, mathematical script, DAG
edge or PROOF assembly changed. Full matching Mathlib coverage for
the budget or arc test is unchecked.
