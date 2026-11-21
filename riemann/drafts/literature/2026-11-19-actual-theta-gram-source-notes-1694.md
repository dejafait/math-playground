# Actual-theta Gram companion: source comparison1694

Literature-only completion of nomination1693. Main gap:
L030-L032/C032a actual-Xi all-degree positivity, equivalently the unpaid
C028b condition H_d=o(d). The intermediate target is exactly the fixed
full-theta metric in nomination1693. An o(d) full cost would pay that
criterion; a positive degree-linear floor would stop this metric only.
No coefficient, similarity, residual or asymptotic is derived here.

## Primary inputs actually inspected

Gerhard Schmeisser, *Estimates for the Imaginary Parts of the Zeros of
a Polynomial*, Mathematica Balkanica16(2002),203-217,
[primary PDF](https://www.math.bas.bg/infres/MathBalk/MB-16/MB-16-203-217.pdf):
read pp203-204 hypotheses, Lemmas1/4/5 pp211-213 and the complete
Theorem1 proof pp213-214. For a positive real measure of infinite
support with all moments, write a real monic polynomial as
f=sum a_j p_j, a_n=1, with monic orthogonal p_j and h_j=integral p_j^2.
Lemma4 gives a symmetric Jacobi matrix plus a last-column perturbation
b_j=-sqrt(h_j/h_(n-1))*a_j. Lemma5 and the proof's c=kappa=0 case give
imaginary-part eigenvalues 0 (n-2 times) and +/-I/2, where

    I^2=sum_(j=0)^(n-2) h_j*a_j^2/h_(n-1).

Lemma1 bounds total imaginary root height by this trace norm.
This imports a full cost for that representation. Identification with
the nominated Cholesky similarity remains to be checked, not assumed.
Reuse source-notes1523 for majorization's scope and its upstream
Gohberg-Krein citation; the upstream book was not independently read.
The screenshot request for p214 timed out; its complete formula/proof
was accessible as PDF text and agrees with the reused source coverage.

V. Noferini, L. Robol and R. Vandebril, *Structured backward errors in
linearizations*, ETNA54,420-442, DOI10.1553/etna_vol54s420,
[publisher PDF in institutional repository](https://acris.aalto.fi/ws/portalfiles/portal/65515241/Structured_backward_errors_in_linearizations.pp420_442.pdf):
the article imprint says2021, repository cover says2020. Read
Definition2.1/Theorem2.2 and all three proof parts, pp422-423, and
Section2.2 pp423-425 through the symmetric scaling construction.
Degree-graded bases give confederate matrices; orthogonal bases give
comrade matrices. The paper uses reversed evaluation-vector and row
conventions. It supplies a multiplication/quotient interpretation and
a symmetric tridiagonal part plus a rank-one correction, not a theta
cost estimate. Its Section2.2 states a closed-real-interval hypothesis;
do not silently extend that statement to unbounded theta support.
Schmeisser supplies the needed unbounded-measure interface instead.
Later numerical backward-error bounds were not read or imported.

NIST [DLMF18.2](https://dlmf.nist.gov/18.2), accessed19November2026:
read (i), monic recurrence/norm formulas (iv), 18.2.11 and
18.2.11_5-6, even-weight parity18.2.21, and (viii).
Finite absolute moments and a positive measure admit the usual
orthogonal system; monic recurrence beta_n=h_n/h_(n-1)>0.
Bounded-interval orthogonality makes the measure unique up to scale.
These general statements do not evaluate the actual recurrence data.

Barry Simon, *Szego's Theorem and Its Descendants*, PrincetonUP2011,
[Chapter1](https://assets.press.princeton.edu/chapters/s9377.pdf),
Proposition1.3.6 and Theorems1.3.7-8, pp16-17: read statements and
complete proofs, extending the reused1503 coverage by Theorem1.3.8.
Bounded real diagonal and positive off-diagonal Jacobi parameters
give a bounded operator and a bounded-support probability measure.
The correspondence in Theorem1.3.8 is between bounded Jacobi matrices
and bounded-support measures. It must not alone be quoted as uniqueness
among arbitrary unbounded-support measures. Combine only with a
justified moment/uniqueness comparison, using DLMF(viii), if a later
proof needs to exclude bounded recurrence for the actual measure.
The unbounded Favard proof deferred to Section3.8 was not read and is
not needed: the proposed measure is supplied, rather than constructed.

## Applicability obligations and overlap

Read L019 in full: it supplies the full positive K and integrable
superexponential domination. The future specialization must explicitly
verify Z finite/nonzero, every moment, infinite support and strict
positivity of each finite Gram form. Evenness is prescribed by K(|u|).
Do not replace it by a finite summand, Gaussian or atomic quadrature.

Read C028h's exact A_d convention, coefficient identities and diagonal
floor proof; C028i's stated shear scope; C028a's Gaussian proof;
C028b's criterion; and C028c's full hypotheses, conclusion and imported
interface. Reused review495 for the Newton-sum distinction, stops551/571
for failed reference-root assumptions, and1502/1503 for non-Gaussian
reference coverage. These references are comparisons, not extra
mathematical premises of the proposed test.

C028c assumes a particular Hermite-prefix Jacobi family and three
vanishing expansion coefficients. It is not a theorem about all positive
reference measures. Those hypotheses have not been verified for this
metric, so its floor cannot simply be imported. C028h/i do not cover
arbitrary triangular basis changes. Conversely, a dense metric is no
evidence that the present cost escapes either obstruction. The proposed
identification with the standard comrade construction would show that
the general method is already known, leaving only its specified metric
specialization. Review495 concerns a different, root-dependent trace form.
The finite-prefix Favard stop concerns orthogonality of the actual
Jensen family itself, not an external basis for representing Q_d.

## Bounded discovery and exact remaining difference

Queries: `orthogonal polynomial companion matrix colleague comrade
matrix rank one perturbation Jacobi matrix imaginary parts Schmeisser`;
`"Estimates for the Imaginary Parts" "Schmeisser"`;
`"comrade matrix" "orthogonal" "rank" Jacobi`;
`"Schmeisser" "orthogonal" "imaginary" companion theta`;
`"theta" "Gram" "companion matrix" Jensen`;
`"orthogonal polynomial" "imaginary parts" "measure" Schmeisser bound`;
`"Jacobi parameters" "bounded" "unbounded support" measure`.
A rapid-weight recurrence query also returned general asymptotic papers;
their hypotheses/proofs were not inspected and none is an input.
Search-only Sobolev-comrade papers, forums and general exponential-weight
asymptotics remain unread leads, not approved theta estimates. No exact
theta-metric bound was located; no novelty or impossibility follows.

Narrow local screening used companion/symmetrizer/reference/theta-Gram
filenames and the specific source notes/stops named above, not sibling
notebooks. No matching completed full-theta metric test was identified.

Decision SPECIALIZE: retain exactly the given measure, scaling and A_d.
Before any high-degree Cholesky computation, check its basis correspondence
to the imported full-cost formula. Then test only the quadratic residual,
with exact recurrence norm ratios and the prescribed degree scaling,
against the fixed actual second coefficient already present in C028h.
The source-covered support/recurrence interface permits testing whether
a positive linear floor follows without detailed theta asymptotics.
Neither the residual formula nor that implication is established here.
If this diagnostic fails, retain the unresolved full cost and stop after
that one test; it is not authorization for a parameter sweep.

Continue only on a complete o(d) cost proof or a proved uniform positive
linear floor; a finite sample or small retained term proves neither.
The approved source interface supports conventional specialization,
not a creative mechanism or new theorem claim. No justified new central
creative target is yet available within this fixed-metric review.
Mathlib matching coverage is unchecked. No cross-notebook input.
